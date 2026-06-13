import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

os.makedirs("plots", exist_ok=True)

# --- Constants ---
d_LiF = 2.01  # Angstroms
c = 2.9979e8  # m/s
e = 1.6022e-19  # C
h_theoretical = 6.626e-34  # J s
me_c = 2.73e-22 # kg m/s (approx m_e * c)

# Background rate from Image 1
N0 = 0.267

# --- Part 1: Determination of Planck's Constant ---
theta_deg = np.array([4, 5, 6, 7, 8, 8.5, 9, 9.5, 10, 10.5, 11, 12])
theta_rad = np.radians(theta_deg)
lambda_A = 2 * d_LiF * np.sin(theta_rad) # in Angstroms

# Intensities for different voltages
N_V3 = np.array([0.5, 0.7, 0.9, 1.3, 5, 9.9, 19.1, 13.7, 16.9, 15.1, 12.6, 9.3])
N_V6 = np.array([4.7, 5.2, 18, 34.6, 41.8, 42.3, 92.1, 43.5, 100.9, 35.6, 26, 20.7])
N_V7 = np.array([6.2, 10.1, 35.3, 50.9, 51.9, 53.6, 125.8, 49.6, 161.1, 39.3, 35.5, 25.4])

# Subtract background
N_V3_net = np.maximum(N_V3 - N0, 0)
N_V6_net = np.maximum(N_V6 - N0, 0)
N_V7_net = np.maximum(N_V7 - N0, 0)

plt.figure(figsize=(10, 6))
plt.plot(lambda_A, N_V3_net, marker='o', label='$V_3$ (17.58 V)')
plt.plot(lambda_A, N_V6_net, marker='s', label='$V_6$ (23.33 V)')
plt.plot(lambda_A, N_V7_net, marker='^', label='$V_7$ (25.33 V)')
plt.xlabel('Wavelength $\\lambda$ ($\\AA$)')
plt.ylabel('Net Intensity (counts/s)')
plt.title('X-Ray Diffraction Spectra of LiF Crystal')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/xray_spectra.pdf')
plt.close()

# Duane-Hunt law: lambda_min = hc / (e * U_actual)
V_meter = np.array([17.58, 23.33, 25.33])
U_actual = V_meter * 1000 * np.sqrt(2)

# Estimate lambda_min dynamically with a threshold of 10 counts/s
lambda_min_exp = np.zeros(3)
for i, N_net in enumerate([N_V3_net, N_V6_net, N_V7_net]):
    idx = np.argmax(N_net > 10)
    if idx > 0:
        x0, x1 = lambda_A[idx-1], lambda_A[idx]
        y0, y1 = N_net[idx-1], N_net[idx]
        lambda_min_exp[i] = x0 + (x1 - x0) * (10 - y0) / (y1 - y0)
    else:
        lambda_min_exp[i] = lambda_A[0]

inv_U = 1.0 / U_actual

slope, intercept, r_value, p_value, std_err = linregress(inv_U, lambda_min_exp * 1e-10) # convert to meters
h_exp = slope * e / c
h_error = abs(h_exp - h_theoretical) / h_theoretical * 100

print("--- Planck's Constant Analysis ---")
print(f"Accelerating Voltages (V): {U_actual}")
print(f"Experimental lambda_min (A): {lambda_min_exp}")
print(f"Experimental h = {h_exp:.4e} J s")
print(f"Theoretical h = {h_theoretical:.4e} J s")
print(f"Relative Error = {h_error:.2f}%")

plt.figure(figsize=(10, 6))
plt.scatter(inv_U, lambda_min_exp, color='red', label='Experimental Data', zorder=5)
plt.plot(inv_U, (slope * inv_U + intercept) * 1e10, color='blue', label='Linear Fit')
plt.xlabel('$1/U$ ($V^{-1}$)')
plt.ylabel('$\\lambda_{min}$ ($\\AA$)')
plt.title('Duane-Hunt Law: $\\lambda_{min}$ vs $1/U$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/duane_hunt.pdf')
plt.close()


# --- Part 2: Copper Absorption Calibration ---
M = np.array([2.13, 3.83, 20.13, 22.13, 15.73, 14.63, 28.33, 10.53, 29.53, 7.93, 6.83, 5.33])
M_net = np.maximum(M - N0, 0.01)

T_exp = M_net / N_V7_net

lambda_theory = np.linspace(0.2, 0.9, 100)
T_theory = np.exp(-7.6 * (lambda_theory)**2.75)

plt.figure(figsize=(10, 6))
plt.scatter(lambda_A, T_exp, color='purple', label='Experimental $T$', zorder=5)
plt.plot(lambda_theory, T_theory, color='orange', linestyle='--', label='Theoretical Formula')
plt.xlabel('Wavelength $\\lambda$ ($\\AA$)')
plt.ylabel('Transmission $T$')
plt.title('Copper Foil Transmission vs. Wavelength')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/cu_transmission.pdf')
plt.close()


# --- Part 3: Compton Shift ---
def theoretical_compton_shift(theta_deg):
    return (h_theoretical / (9.11e-31 * c)) * (1 - np.cos(np.radians(theta_deg))) * 1e10 # in Angstroms

def lambda_from_T(T):
    return (-np.log(T) / 7.6)**(1/2.75)

# 125 degrees
# WE DO NOT SUBTRACT BACKGROUND HERE. The raw data clearly proves it was already subtracted manually.
N1_125, N2_125, N3_125 = 1.54, 0.31, 0.18
T1_125 = N2_125 / N1_125
T2_125 = N3_125 / N1_125
T2_prime_125 = (3 * T2_125 - T1_125) / 2.0

# 145 degrees
N1_145, N2_145, N3_145 = 3.88, 0.669, 0.498
T1_145 = N2_145 / N1_145
T2_145 = N3_145 / N1_145
T2_prime_145 = (3 * T2_145 - T1_145) / 2.0

print("\n--- Compton Shift Analysis ---")
for angle, T1, T2_prime in [(125, T1_125, T2_prime_125), (145, T1_145, T2_prime_145)]:
    lam1 = lambda_from_T(T1)
    lam2 = lambda_from_T(T2_prime)
    delta_lam = lam2 - lam1
    theory_lam = theoretical_compton_shift(angle)
    print(f"Angle {angle} deg:")
    print(f"  T1 = {T1:.4f} -> lambda = {lam1:.4f} A")
    print(f"  T2' = {T2_prime:.4f} -> lambda' = {lam2:.4f} A")
    print(f"  Experimental Shift = {delta_lam:.4f} A")
    print(f"  Theoretical Shift = {theory_lam:.4f} A")

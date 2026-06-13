import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

os.makedirs("plots", exist_ok=True)

# --- Constants & Parameters ---
T0_C = 18.5
T0_K = T0_C + 273.15
sensitivity = 28.8  # microVolts / (W/m^2)
sigma_theoretical = 5.67e-8 # W / (m^2 K^4)

# --- Table 1: Stefan-Boltzmann Law ---
# Temperature in C
T_C = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 335, 340])
T_K = T_C + 273.15

# Voltage in 10^-4 V, so multiply by 100 to get microVolts
V1_raw = np.array([7.97, 8.84, 9.74, 10.65, 11.6, 12.61, 13.71, 14.83, 15.97, 17.31, 18.74, 19.9, 21.4, 22.9, 23.7, 24.4])
V1_uV = V1_raw * 100

# Intensity I (W/m^2) = V(uV) / Sensitivity
I1 = V1_uV / sensitivity

# For Table 1, r = 8.8 cm, d = 2 cm
r_table1 = 0.088 # m
d_table1 = 0.02  # m

# Radiant Emittance R(T) = I * (4 * r^2 / d^2)
R_T = I1 * (4 * r_table1**2 / d_table1**2)

# X-axis is (T^4 - T0^4)
T4_diff = (T_K**4) - (T0_K**4)

# Linear Regression: R(T) = sigma * (T^4 - T0^4)
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(T4_diff, R_T)
sigma_exp = slope1
sigma_error = abs(sigma_exp - sigma_theoretical) / sigma_theoretical * 100

print("--- Table 1 Analysis ---")
print(f"Experimental Stefan-Boltzmann Constant (sigma) = {sigma_exp:.4e} W/(m^2 K^4)")
print(f"Theoretical sigma = {sigma_theoretical:.4e}")
print(f"Relative Error = {sigma_error:.2f}%")
print(f"R-squared = {r_value1**2:.4f}")

# Plot Table 1
plt.figure(figsize=(10, 6))
plt.scatter(T4_diff, R_T, color='red', label='Experimental Data', zorder=5)
plt.plot(T4_diff, slope1 * T4_diff + intercept1, color='blue', label=f'Linear Fit (slope = {slope1:.2e})')
plt.xlabel('$(T^4 - T_0^4)$ $[K^4]$')
plt.ylabel('$R(T)$ $[W/m^2]$')
plt.title('Stefan-Boltzmann Law: $R(T)$ vs. $(T^4 - T_0^4)$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/stefan_boltzmann.pdf')
plt.close()


# --- Table 2: Inverse Square Law ---
x1 = 28.5 # cm
x2 = np.array([42, 45, 48, 51, 54, 57, 60, 63, 66, 69]) # cm
r_cm = x2 - x1
r_m = r_cm / 100.0

V2_raw = np.array([32.6, 20.5, 14.1, 10.55, 8.48, 6.98, 5.87, 5.04, 4.2, 3.55])
V2_uV = V2_raw * 100

I2 = V2_uV / sensitivity
inv_r2 = 1.0 / (r_m**2)

# Linear Regression: I = const * (1 / r^2)
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(inv_r2, I2)

print("\n--- Table 2 Analysis ---")
print(f"Inverse Square Law Fit R-squared = {r_value2**2:.4f}")

# Plot Table 2
plt.figure(figsize=(10, 6))
plt.scatter(inv_r2, I2, color='green', label='Experimental Data', zorder=5)
plt.plot(inv_r2, slope2 * inv_r2 + intercept2, color='orange', label='Linear Fit')
plt.xlabel('$1/r^2$ $[m^{-2}]$')
plt.ylabel('Intensity $I$ $[W/m^2]$')
plt.title('Inverse Square Law: Intensity vs. $1/r^2$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/inverse_square.pdf')
plt.close()

# --- LaTeX Table Output ---
print("\n--- LaTeX Table 1 Output ---")
for i in range(len(T_C)):
    print(f"{T_C[i]} & {T_K[i]:.2f} & {V1_raw[i]} & {I1[i]:.2f} & {T4_diff[i]:.2e} & {R_T[i]:.2f} \\\\")

print("\n--- LaTeX Table 2 Output ---")
for i in range(len(x2)):
    print(f"{x2[i]} & {r_cm[i]:.1f} & {V2_raw[i]} & {I2[i]:.2f} & {inv_r2[i]:.2f} \\\\")

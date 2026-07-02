import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

os.makedirs("plots", exist_ok=True)

# --- Experiment 1: Saturation Curves ---
U_c = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 160, 180, 200, 250, 300])

I_U1 = np.array([0, 0.07, 0.1, 0.12, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.12, 0.12, 0.12, 0.11, 0.11, 0.11, 0.1, 0.095, 0.09])
I_U2 = np.array([0, 0.23, 0.38, 0.48, 0.52, 0.54, 0.55, 0.54, 0.54, 0.53, 0.53, 0.52, 0.52, 0.51, 0.5, 0.48, 0.47, 0.45, 0.42, 0.42])
I_U3 = np.array([0, 0.33, 0.62, 0.9, 1.08, 1.2, 1.25, 1.28, 1.3, 1.3, 1.3, 1.3, 1.3, 1.28, 1.28, 1.25, 1.23, 1.2, 1.18, 1.15])
I_U4 = np.array([0, 0.42, 0.87, 1.3, 1.66, 1.97, 2.17, 2.28, 2.35, 2.42, 2.45, 2.45, 2.47, 2.47, 2.45, 2.47, 2.45, 2.43, 2.37, 2.35])
I_U5 = np.array([0, 0.52, 1.07, 1.62, 2.15, 2.6, 3.05, 3.35, 3.55, 3.65, 3.75, 3.8, 3.85, 3.9, 3.9, 3.95, 3.9, 3.95, 3.9, 3.9])

plt.figure(figsize=(10, 6))
plt.plot(U_c, I_U5, 'o-', label='$V_A = 35$ kV')
plt.plot(U_c, I_U4, 's-', label='$V_A = 30$ kV')
plt.plot(U_c, I_U3, '^-', label='$V_A = 25$ kV')
plt.plot(U_c, I_U2, 'd-', label='$V_A = 20$ kV')
plt.plot(U_c, I_U1, 'x-', label='$V_A = 15$ kV')
plt.xlabel('Capacitor Voltage $U_C$ (V)')
plt.ylabel('Ionization Current $I_C$ (nA)')
plt.title('Experiment 1: Ionization Saturation Curves')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/saturation_curves.pdf')
plt.close()

# --- Experiment 2: Current vs Emission Current ---
I_em = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
I_vs_em = np.array([0.02, 0.48, 0.92, 1.3, 1.72, 2.1, 2.45, 2.8, 3.2, 3.55, 3.9])

def linear_func(x, a, b):
    return a * x + b

popt_em, _ = curve_fit(linear_func, I_em, I_vs_em)

plt.figure(figsize=(8, 5))
plt.scatter(I_em, I_vs_em, color='blue', label='Experimental Data', zorder=5)
plt.plot(I_em, linear_func(I_em, *popt_em), color='red', linestyle='--', label=f'Linear Fit (slope = {popt_em[0]:.2f})')
plt.xlabel('Emission Current $I_{em}$ (mA)')
plt.ylabel('Ionization Current $I$ (nA)')
plt.title('Experiment 2: Ionization Current vs. Emission Current')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/current_vs_em.pdf')
plt.close()

# --- Experiment 3: Current vs Anode Voltage ---
V_A = np.array([5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35])
I_vs_VA = np.array([0.02, 0.02, 0.02, 0.03, 0.1, 0.26, 0.49, 0.81, 1.25, 1.82, 2.4, 3.1, 3.9])

# Since X-ray intensity is roughly proportional to V^2, we expect n around 2
# Let's fit a simple quadratic just to guide the eye
popt_va, _ = curve_fit(lambda x, a, b, c: a*x**2 + b*x + c, V_A, I_vs_VA)

plt.figure(figsize=(8, 5))
plt.scatter(V_A, I_vs_VA, color='purple', label='Experimental Data', zorder=5)
V_A_smooth = np.linspace(5, 35, 100)
plt.plot(V_A_smooth, popt_va[0]*V_A_smooth**2 + popt_va[1]*V_A_smooth + popt_va[2], color='orange', linestyle='--', label='Quadratic Fit')
plt.xlabel('Anode Voltage $V_A$ (kV)')
plt.ylabel('Ionization Current $I$ (nA)')
plt.title('Experiment 3: Ionization Current vs. Anode Voltage')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('plots/current_vs_va.pdf')
plt.close()

# --- Effective Ionic Capacity (j) ---
# Maximum saturation current observed
I_max = 3.95e-9 # A (from U5 max)
volume = 122 # cm^3
rho = 1.205e-6 # kg/cm^3
mass = rho * volume # kg

j = I_max / mass

print("--- Ionization Data Analysis ---")
print(f"Air Volume = {volume} cm^3")
print(f"Air Density = {rho} kg/cm^3")
print(f"Air Mass = {mass:.2e} kg")
print(f"Maximum Saturation Current = {I_max:.2e} A")
print(f"Effective Ionic Capacity (j) = {j:.4e} C/(kg s)")

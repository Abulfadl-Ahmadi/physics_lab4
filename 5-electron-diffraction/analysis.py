import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os

# Create plots directory
os.makedirs("plots", exist_ok=True)

# Data
# Voltage (V), Radius 1 (mm), Radius 2 (mm)
data = np.array([
    [1650, 19, 33],
    [2000, 18, 30],
    [2400, 16, 28],
    [2800, 15, 26],
    [3200, 14, 24],
    [3600, 13, 23],
    [4000, 13, 22],
    [4500, 12, 21],
    [5000, 11, 20],
    [5600, 11, 18]
])

V = data[:, 0]
r1 = data[:, 1]
r2 = data[:, 2]

# Constants
L = 135.0 # mm (Distance from target to screen)
R_bulb = 67.5 # mm (Radius of the spherical bulb)
h = 6.626e-34 # J*s
e = 1.602e-19 # C
m_e = 9.109e-31 # kg

# Instrumental Uncertainties
delta_V = 10.0 # V
delta_r = 0.5 # mm

# Geometric conversions based on the bulb's spherical geometry
# sin(alpha) = r / R_bulb
# tan(2*theta) = sin(alpha) / (1 + cos(alpha)) = tan(alpha / 2)
# Therefore, 2*theta = alpha / 2  =>  theta = alpha / 4
# Or theta = 0.25 * arcsin(r / R_bulb)

def calculate_theta(r):
    sin_alpha = r / R_bulb
    alpha = np.arcsin(sin_alpha)
    theta = alpha / 4.0
    return theta

# Error propagation for theta
# d(theta)/dr = 1 / (4 * R_bulb * sqrt(1 - (r/R_bulb)^2))
def calculate_delta_theta(r, delta_r):
    dtheta_dr = 1.0 / (4.0 * R_bulb * np.sqrt(1.0 - (r/R_bulb)**2))
    return dtheta_dr * delta_r

theta1 = calculate_theta(r1)
delta_theta1 = calculate_delta_theta(r1, delta_r)
sin_theta1 = np.sin(theta1)
delta_sin_theta1 = np.cos(theta1) * delta_theta1

theta2 = calculate_theta(r2)
delta_theta2 = calculate_delta_theta(r2, delta_r)
sin_theta2 = np.sin(theta2)
delta_sin_theta2 = np.cos(theta2) * delta_theta2

# x-axis data: 1 / sqrt(V)
x = 1.0 / np.sqrt(V)
# Error in x: d(V^(-1/2)) = -1/2 * V^(-3/2) * dV
delta_x = 0.5 * (V**(-1.5)) * delta_V

print("--- OLS Regressions ---")

# Regression for Ring 1
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(x, sin_theta1)
print(f"Ring 1: slope = {slope1:.6f} \pm {std_err1:.6f}, R^2 = {r_value1**2:.4f}")

# Regression for Ring 2
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x, sin_theta2)
print(f"Ring 2: slope = {slope2:.6f} \pm {std_err2:.6f}, R^2 = {r_value2**2:.4f}")

# Plotting sin(theta) vs 1/sqrt(V)
plt.figure(figsize=(8, 6))

plt.errorbar(x, sin_theta1, xerr=delta_x, yerr=delta_sin_theta1, fmt='bo', label='Ring 1 Data', capsize=3)
x_fit = np.linspace(min(x)*0.9, max(x)*1.1, 100)
plt.plot(x_fit, slope1 * x_fit + intercept1, 'b-', label=f'Fit 1: slope = {slope1:.4f}')

plt.errorbar(x, sin_theta2, xerr=delta_x, yerr=delta_sin_theta2, fmt='ro', label='Ring 2 Data', capsize=3)
plt.plot(x_fit, slope2 * x_fit + intercept2, 'r-', label=f'Fit 2: slope = {slope2:.4f}')

plt.xlabel(r'$1/\sqrt{V}$ (V$^{-1/2}$)')
plt.ylabel(r'$\sin(\theta)$')
plt.title(r'Bragg Diffraction: $\sin(\theta)$ vs. $1/\sqrt{V}$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('plots/regression.pdf')
plt.close()

# Calculate lattice spacings d1 and d2
# Theoretical relationship: sin(theta) = [h / (2 * d * sqrt(2 * m_e * e))] * (1 / sqrt(V))
# So slope = h / (2 * d * sqrt(2 * m_e * e))
# d = h / (2 * slope * sqrt(2 * m_e * e))

constant_factor = h / (2 * np.sqrt(2 * m_e * e))

d1 = constant_factor / slope1
d1_err = d1 * (std_err1 / slope1) # Error propagation for d1

d2 = constant_factor / slope2
d2_err = d2 * (std_err2 / slope2) # Error propagation for d2

print("\n--- Physical Results ---")
print(f"d1 = {d1*1e10:.4f} \pm {d1_err*1e10:.4f} Angstroms")
print(f"d2 = {d2*1e10:.4f} \pm {d2_err*1e10:.4f} Angstroms")

ratio = d1 / d2
ratio_err = ratio * np.sqrt((d1_err/d1)**2 + (d2_err/d2)**2)
print(f"Ratio d1/d2 = {ratio:.4f} \pm {ratio_err:.4f} (Theoretical: sqrt(3) = 1.732)")

# Calculate carbon-carbon distance (a_cc)
# For hexagonal lattice, d1 is d_10, so d1 = a * sqrt(3) / 2  where a is the lattice constant
# And a_cc = a / sqrt(3) = d1 * (2 / sqrt(3)) / sqrt(3) = 2 * d1 / 3
# Wait, a = d1 * 2 / sqrt(3).
# In graphite, distance between adjacent carbon atoms is a / sqrt(3).
# So distance = (d1 * 2 / sqrt(3)) / sqrt(3) = 2/3 * d1.
# Let's verify: 2.13 * 2 / 3 = 1.42 A. Yes!
a_cc = (2.0 / 3.0) * d1
a_cc_err = (2.0 / 3.0) * d1_err
print(f"Carbon-Carbon bond distance = {a_cc*1e10:.4f} \pm {a_cc_err*1e10:.4f} Angstroms (Theoretical: 1.42 A)")

# Print LaTeX table for data
print("\n--- LaTeX Table Data ---")
print("\\begin{table}[H]")
print("\\centering")
print("\\caption{Experimental data for the first and second diffraction rings. $\\theta$ is calculated using the spherical geometry of the tube.}")
print("\\label{tab:data}")
print("\\resizebox{\\textwidth}{!}{")
print("\\begin{tabular}{c c c c c c c}")
print("\\toprule")
print("$V$ (V) & $1/\\sqrt{V}$ (V$^{-1/2}$) & $r_1$ (mm) & $\\theta_1$ (rad) & $r_2$ (mm) & $\\theta_2$ (rad) \\\\")
print("\\midrule")
for i in range(len(V)):
    print(f"${int(V[i])}$ & ${x[i]:.5f}$ & ${r1[i]:.1f}$ & ${theta1[i]:.4f}$ & ${r2[i]:.1f}$ & ${theta2[i]:.4f}$ \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("}")
print("\\end{table}")

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os

# Create plots
os.makedirs("plots", exist_ok=True)

# 1. I-V Data
# Data: Current I(A), Violet U(V), Green U(V)
iv_data = np.array([
    [3, 0.737, 0.44],
    [2.8, 0.766, 0.45],
    [2.6, 0.75, 0.46],
    [2.4, 0.807, 0.474],
    [2.2, 0.833, 0.483],
    [2, 0.847, 0.494],
    [1.8, 0.871, 0.507],
    [1.6, 0.895, 0.521],
    [1.4, 0.921, 0.536],
    [1.2, 0.947, 0.55],
    [1, 0.976, 0.559],
    [0.8, 1.005, 0.578],
    [0.6, 1.048, 0.602],
    [0.4, 1.086, 0.637],
    [0.2, 1.147, 0.733],
])

currents = iv_data[:, 0]
u_violet = iv_data[:, 1]
u_green = iv_data[:, 2]

# Instrumental errors (based on data precision)
delta_U = 0.001 # V
delta_I = 0.1 # A

# Plot I-V characteristic curve (Note: Usually I is on y-axis and V is on x-axis)
plt.figure(figsize=(8, 6))
plt.errorbar(u_violet, currents, xerr=delta_U, yerr=delta_I, fmt='o', label='Violet Light', color='purple', markersize=4, capsize=3)
plt.errorbar(u_green, currents, xerr=delta_U, yerr=delta_I, fmt='s', label='Green Light', color='green', markersize=4, capsize=3)

# Smooth curve through points (or simple line connections)
# sorting values for plot just in case
sort_v = np.argsort(u_violet)
plt.plot(u_violet[sort_v], currents[sort_v], color='purple', alpha=0.5)

sort_g = np.argsort(u_green)
plt.plot(u_green[sort_g], currents[sort_g], color='green', alpha=0.5)

plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Photocurrent $I$ (A)')
plt.title('Photocurrent vs. Retarding Voltage')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('plots/IV_curve.pdf')
plt.close()


# 2. Stopping Potential vs Frequency Data
# Frequencies in Hz
nu = np.array([5.19e14, 5.49e14, 6.10e14, 6.88e14, 7.41e14])
colors = ['Yellow', 'Green', 'Green-Blue', 'Blue', 'Violet']

# U0 values for each trial
u0_t1 = np.array([0.819, 0.897, 0.921, 0.941, 1.219])
u0_t2 = np.array([0.834, 0.914, 0.912, 0.928, 1.204])
u0_t3 = np.array([0.820, 0.899, 0.908, 1.012, 1.218])

u0_all = np.vstack((u0_t1, u0_t2, u0_t3))
u0_avg = np.mean(u0_all, axis=0)

# Statistical error in U0
# Stdev of the mean
u0_std = np.std(u0_all, axis=0, ddof=1) / np.sqrt(3)
# take max between std and instrumental error
delta_U0 = np.maximum(u0_std, delta_U)

print("--- U0 Average and Errors ---")
for i in range(len(nu)):
    print(f"nu = {nu[i]:.2e} Hz ({colors[i]}): U0 = {u0_avg[i]:.4f} \pm {delta_U0[i]:.4f} V")

# OLS Regression
# U0 = (h/e) * nu - (Phi/e)
# y = m * x + c
x = nu
y = u0_avg

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Manually compute intercept standard error
n = len(x)
mean_x = np.mean(x)
sum_sq_x = np.sum((x - mean_x)**2)
s_yx = np.sqrt(np.sum((y - (slope*x + intercept))**2) / (n - 2))

m_err = s_yx / np.sqrt(sum_sq_x)
c_err = s_yx * np.sqrt(1/n + mean_x**2 / sum_sq_x)

print("\n--- OLS Regression Results ---")
print(f"Slope (h/e) = {slope:.4e} \pm {m_err:.4e} V*s")
print(f"Intercept (-Phi/e) = {intercept:.4f} \pm {c_err:.4f} V")
print(f"R^2 = {r_value**2:.4f}")

# Plot Regression
plt.figure(figsize=(8, 6))
plt.errorbar(x, y, yerr=delta_U0, fmt='ko', label='Data Points', markersize=5, capsize=4)
# Best fit line
x_fit = np.linspace(min(x)-0.2e14, max(x)+0.2e14, 100)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, 'r-', label=f'Fit: $U_0 = ({slope:.3e})\\nu {intercept:+.3f}$')

# Show intercept at nu=0 (threshold frequency)
threshold_freq = -intercept / slope
plt.axhline(0, color='black', linewidth=0.8)
plt.plot(threshold_freq, 0, 'rx', markersize=8, label=f'Threshold Freq: {threshold_freq:.2e} Hz')

plt.xlabel(r'Frequency $\nu$ (Hz)')
plt.ylabel(r'Stopping Potential $U_0$ (V)')
plt.title(r'Stopping Potential vs. Light Frequency')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('plots/U0_vs_nu.pdf')
plt.close()

# Calculate Planck's Constant and Work Function
e = 1.60217663e-19 # C
# h = slope * e
h_exp = slope * e
h_err = m_err * e

# Phi = -intercept * e (in Joules), convert to eV
phi_eV = -intercept
phi_err_eV = c_err

h_theoretical = 6.62607015e-34 # J*s
rel_error_h = abs(h_exp - h_theoretical) / h_theoretical * 100

print("\n--- Final Physics Results ---")
print(f"Planck's Constant h = {h_exp:.4e} \pm {h_err:.4e} J*s")
print(f"Theoretical h = {h_theoretical:.4e} J*s")
print(f"Relative Error in h = {rel_error_h:.2f} %")
print(f"Work Function Phi = {phi_eV:.3f} \pm {phi_err_eV:.3f} eV")
print(f"Threshold Frequency nu_th = {threshold_freq:.3e} Hz")

# Generate LaTeX tables
print("\n--- LaTeX Tables ---")
# I-V table
print("\\begin{table}[H]")
print("\\centering")
print("\\caption{Photocurrent $I$ as a function of the retarding potential $U$ for Violet and Green incident light.}")
print("\\label{tab:iv_data}")
print("\\begin{tabular}{l c c}")
print("\\toprule")
print("Current $I$ (A) & Violet Voltage $U$ (V) & Green Voltage $U$ (V) \\\\")
print("\\midrule")
for i in range(len(currents)):
    print(f"${currents[i]:.1f}$ & ${u_violet[i]:.3f}$ & ${u_green[i]:.2f}$ \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}")

# U0 vs nu table
print("\\begin{table}[H]")
print("\\centering")
print("\\caption{Measured stopping potentials ($U_0$) across three trials for different frequencies ($\\nu$) of incident light.}")
print("\\label{tab:u0_data}")
print("\\begin{tabular}{lcccccc}")
print("\\toprule")
print("Frequency $\\nu$ ($10^{14}$ Hz) & $5.19$ & $5.49$ & $6.10$ & $6.88$ & $7.41$ \\\\")
print("Colour & Yellow & Green & Green-Blue & Blue & Violet \\\\")
print("\\midrule")
print(f"$U_{{0, \\text{{Trial 1}}}}$ (V) & {u0_t1[0]} & {u0_t1[1]} & {u0_t1[2]} & {u0_t1[3]} & {u0_t1[4]} \\\\")
print(f"$U_{{0, \\text{{Trial 2}}}}$ (V) & {u0_t2[0]} & {u0_t2[1]} & {u0_t2[2]} & {u0_t2[3]} & {u0_t2[4]} \\\\")
print(f"$U_{{0, \\text{{Trial 3}}}}$ (V) & {u0_t3[0]} & {u0_t3[1]} & {u0_t3[2]} & {u0_t3[3]} & {u0_t3[4]} \\\\")
print("\\midrule")
print(f"\\textbf{{Average $U_0$}} (V) & $\\mathbf{{{u0_avg[0]:.3f} \\pm {delta_U0[0]:.3f}}}$ & $\\mathbf{{{u0_avg[1]:.3f} \\pm {delta_U0[1]:.3f}}}$ & $\\mathbf{{{u0_avg[2]:.3f} \\pm {delta_U0[2]:.3f}}}$ & $\\mathbf{{{u0_avg[3]:.3f} \\pm {delta_U0[3]:.3f}}}$ & $\\mathbf{{{u0_avg[4]:.3f} \\pm {delta_U0[4]:.3f}}}$ \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}")

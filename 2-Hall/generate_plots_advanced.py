import numpy as np
import matplotlib.pyplot as plt

# Apply professional publication styling
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Computer Modern", "DejaVu Serif", "Times New Roman"],
    "axes.labelsize": 11,
    "font.size": 11,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.figsize": [6.0, 4.5],
    "grid.alpha": 0.5,
    "grid.linestyle": "--"
})

# ----------------------------
# Data
# ----------------------------
I_mA = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
I_A = I_mA * 1e-3
delta_I_mA = 1.0  # mA
delta_I_A = 1.0 * 1e-3  # A

# VH (mV)
VH_0 = np.array([0, 0.4, 0.9, 1.4, 1.9, 2.4, 2.8, 3.4, 3.8, 4.3, 4.8])
VH_1 = np.array([0, 3.1, 6.1, 9.3, 12.4, 15.5, 18.6, 21.7, 24.8, 27.9, 30.9])
VH_2 = np.array([0, 5.1, 10.2, 15.3, 20.2, 25.2, 30.3, 35.1, 40.3, 45.3, 50.2])
delta_VH_mV = 0.1  # mV
delta_VH_V = 0.1 * 1e-3  # V

# Convert to Volts (V)
VH_0_V = VH_0 * 1e-3
VH_1_V = VH_1 * 1e-3
VH_2_V = VH_2 * 1e-3

# Vx (mV)
Vx_0 = np.array([0, 127.6, 258.6, 387.1, 513, 642, 767, 898, 1023, 1148, 1276])
Vx_1 = np.array([0, 132, 258.2, 389.8, 519.0, 645.0, 773.0, 902.0, 1032.0, 1160.0, 1286.0])
Vx_2 = np.array([0, 134.3, 265.2, 396.9, 522.0, 651.0, 782.0, 908.0, 1040.0, 1169.0, 1297.0])
delta_Vx_mV = 1.0  # mV
delta_Vx_V = 1.0 * 1e-3  # V

# Convert to Volts (V)
Vx_0_V = Vx_0 * 1e-3
Vx_1_V = Vx_1 * 1e-3
Vx_2_V = Vx_2 * 1e-3

# Dimensions
W = 0.5 * 1e-3
delta_W = 0.01 * 1e-3
d = 6.0 * 1e-3
delta_d = 0.1 * 1e-3
l = 13.0 * 1e-3
delta_l = 0.1 * 1e-3

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# -----------------------------------------------------------------------------
# Plot 1: VH vs I for Im = 0, 1, 2 A (with Error Bars)
# -----------------------------------------------------------------------------
plt.figure()
for VH, label, col in zip([VH_0, VH_1, VH_2], ["$I_m = 0$ A", "$I_m = 1$ A", "$I_m = 2$ A"], colors):
    coef, cov = np.polyfit(I_mA, VH, 1, cov=True)
    se_slope = np.sqrt(cov[0, 0])
    trend = np.polyval(coef, I_mA)
    
    plt.errorbar(I_mA, VH, xerr=delta_I_mA, yerr=delta_VH_mV, fmt='o', color=col, ecolor='gray', capsize=2, elinewidth=1, markersize=4)
    plt.plot(I_mA, trend, linestyle='--', color=col,
             label=f"{label} (fit: $y=({coef[0]:.4f} \\pm {se_slope:.4f})x{coef[1]:+.2f}$)")

plt.xlabel("Sample Current $I$ (mA)")
plt.ylabel("Hall Voltage $V_H$ (mV)")
plt.title("Hall Voltage vs. Sample Current with Error Bars")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("VH_vs_I_errorbars.pdf")
plt.close()

# -----------------------------------------------------------------------------
# Plot 2: B vs Im (with Error Bars)
# -----------------------------------------------------------------------------
RH_avg = 4.360668e-4
dRH_avg = 9.256484e-6
Im_tab5 = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
delta_Im = 0.01  # A
VH_tab5_mV = np.array([4.8, 9.9, 15.3, 20.5, 26.2, 30.4, 35.0, 40.8, 43.4, 46.5, 50.1])
VH_tab5_V = VH_tab5_mV * 1e-3
I_tab5 = 0.2  # A

B_tab5 = (VH_tab5_V * W) / (I_tab5 * RH_avg)
dB_tab5 = B_tab5 * np.sqrt((delta_VH_V/VH_tab5_V)**2 + (delta_W/W)**2 + (delta_I_A/I_tab5)**2 + (dRH_avg/RH_avg)**2)

plt.figure()
coef_B, cov_B = np.polyfit(Im_tab5, B_tab5, 1, cov=True)
se_slope_B = np.sqrt(cov_B[0, 0])
trend_B = np.polyval(coef_B, Im_tab5)

plt.errorbar(Im_tab5, B_tab5, xerr=delta_Im, yerr=dB_tab5, fmt='o', color='#d62728', ecolor='gray', capsize=2, elinewidth=1, markersize=4, label="Calculated $B$")
plt.plot(Im_tab5, trend_B, linestyle='--', color='#d62728',
         label=f"Fit: $B = ({coef_B[0]:.4f} \\pm {se_slope_B:.4f}) I_m {coef_B[1]:+.4f}$")

plt.xlabel("Magnet Current $I_m$ (A)")
plt.ylabel("Magnetic Field $B$ (T)")
plt.title("Magnetic Field Calibration Curve with Error Bars")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("B_vs_Im_errorbars.pdf")
plt.close()

# -----------------------------------------------------------------------------
# Plot 3: Vx vs I (with Error Bars)
# -----------------------------------------------------------------------------
plt.figure()
for Vx, label, col in zip([Vx_0, Vx_1, Vx_2], ["$I_m = 0$ A", "$I_m = 1$ A", "$I_m = 2$ A"], colors):
    coef, cov = np.polyfit(I_mA, Vx, 1, cov=True)
    se_slope = np.sqrt(cov[0, 0])
    trend = np.polyval(coef, I_mA)
    
    plt.errorbar(I_mA, Vx, xerr=delta_I_mA, yerr=delta_Vx_mV, fmt='o', color=col, ecolor='gray', capsize=2, elinewidth=1, markersize=4)
    plt.plot(I_mA, trend, linestyle='--', color=col,
             label=f"{label} ($R = {coef[0]:.4f} \\pm {se_slope:.4f}\\;\\Omega$)")

plt.xlabel("Sample Current $I$ (mA)")
plt.ylabel("Longitudinal Voltage $V_x$ (mV)")
plt.title("Longitudinal Voltage vs. Sample Current with Error Bars")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Vx_vs_I_errorbars.pdf")
plt.close()

# -----------------------------------------------------------------------------
# Plot 4: Vx vs VH (with Error Bars)
# -----------------------------------------------------------------------------
plt.figure()
for VH_V, Vx_V, label, col in zip([VH_0_V, VH_1_V, VH_2_V], [Vx_0_V, Vx_1_V, Vx_2_V], ["$I_m = 0$ A", "$I_m = 1$ A", "$I_m = 2$ A"], colors):
    coef, cov = np.polyfit(VH_V, Vx_V, 1, cov=True)
    se_slope = np.sqrt(cov[0, 0])
    trend = np.polyval(coef, VH_V)
    
    plt.errorbar(VH_V * 1e3, Vx_V * 1e3, xerr=delta_VH_mV, yerr=delta_Vx_mV, fmt='o', color=col, ecolor='gray', capsize=2, elinewidth=1, markersize=4)
    plt.plot(VH_V * 1e3, trend * 1e3, linestyle='--', color=col,
             label=f"{label} (slope = ${coef[0]:.2f} \\pm {se_slope:.2f}$)")

plt.xlabel("Hall Voltage $V_H$ (mV)")
plt.ylabel("Longitudinal Voltage $V_x$ (mV)")
plt.title("Longitudinal Voltage vs. Hall Voltage with Error Bars")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Vx_vs_VH_errorbars.pdf")
plt.close()

print("All advanced plots with error bars generated successfully.")

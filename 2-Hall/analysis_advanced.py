import numpy as np

# ----------------------------
# 1. Raw Data & Instrument Errors
# ----------------------------
# Current through sample (mA)
I_mA = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
I_A = I_mA * 1e-3  # Convert to A
delta_I = 1.0 * 1e-3  # delta I = 1 mA = 0.001 A

# Hall Voltage (mV) for three magnet currents
VH_0 = np.array([0, 0.4, 0.9, 1.4, 1.9, 2.4, 2.8, 3.4, 3.8, 4.3, 4.8])
VH_1 = np.array([0, 3.1, 6.1, 9.3, 12.4, 15.5, 18.6, 21.7, 24.8, 27.9, 30.9])
VH_2 = np.array([0, 5.1, 10.2, 15.3, 20.2, 25.2, 30.3, 35.1, 40.3, 45.3, 50.2])

VH_0_V = VH_0 * 1e-3
VH_1_V = VH_1 * 1e-3
VH_2_V = VH_2 * 1e-3
delta_VH = 0.1 * 1e-3  # delta VH = 0.1 mV = 1e-4 V

# Longitudinal voltage (mV)
Vx_0 = np.array([0, 127.6, 258.6, 387.1, 513, 642, 767, 898, 1023, 1148, 1276])
Vx_1 = np.array([0, 132, 258.2, 389.8, 519.0, 645.0, 773.0, 902.0, 1032.0, 1160.0, 1286.0])
Vx_2 = np.array([0, 134.3, 265.2, 396.9, 522.0, 651.0, 782.0, 908.0, 1040.0, 1169.0, 1297.0])

Vx_0_V = Vx_0 * 1e-3
Vx_1_V = Vx_1 * 1e-3
Vx_2_V = Vx_2 * 1e-3
delta_Vx = 1.0 * 1e-3  # delta Vx = 1.0 mV = 1e-3 V

# Dimensions
W = 0.5 * 1e-3
delta_W = 0.01 * 1e-3  # delta W = 0.01 mm = 1e-5 m
d = 6.0 * 1e-3
delta_d = 0.1 * 1e-3   # delta d = 0.1 mm = 1e-4 m
l = 13.0 * 1e-3
delta_l = 0.1 * 1e-3   # delta l = 0.1 mm = 1e-4 m

# Magnetic Fields (point estimates from lab settings)
B1 = 0.19
delta_B1 = 0.005  # delta B1 = 0.005 T
B2 = 0.27
delta_B2 = 0.005  # delta B2 = 0.005 T

# ----------------------------
# OLS Regression Helper
# ----------------------------
def ols_fit(x, y):
    N = len(x)
    m, c = np.polyfit(x, y, 1)
    y_pred = m * x + c
    residuals = y - y_pred
    ss_res = np.sum(residuals**2)
    s_yx = np.sqrt(ss_res / (N - 2))
    ss_x = np.sum((x - np.mean(x))**2)
    se_m = s_yx / np.sqrt(ss_x)
    se_c = s_yx * np.sqrt(1/N + np.mean(x)**2 / ss_x)
    # R^2
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = 1 - (ss_res / ss_tot)
    return m, se_m, c, se_c, r2

# ----------------------------
# 2. Fits for VH vs I (for RH)
# ----------------------------
m0, se_m0, c0, se_c0, r2_0 = ols_fit(I_A, VH_0_V)
m1, se_m1, c1, se_c1, r2_1 = ols_fit(I_A, VH_1_V)
m2, se_m2, c2, se_c2, r2_2 = ols_fit(I_A, VH_2_V)

print("=== OLS Fits for VH vs I ===")
print(f"Im = 0 A: slope = {m0:.6f} +/- {se_m0:.6f} V/A, intercept = {c0:.6e} +/- {se_c0:.6e} V, R^2 = {r2_0:.6f}")
print(f"Im = 1 A: slope = {m1:.6f} +/- {se_m1:.6f} V/A, intercept = {c1:.6e} +/- {se_c1:.6e} V, R^2 = {r2_1:.6f}")
print(f"Im = 2 A: slope = {m2:.6f} +/- {se_m2:.6f} V/A, intercept = {c2:.6e} +/- {se_c2:.6e} V, R^2 = {r2_2:.6f}")
print()

# ----------------------------
# 3. Calculation of RH and n
# ----------------------------
# RH = (slope * W) / B
# delta RH = RH * sqrt( (se_slope/slope)^2 + (delta_W/W)^2 + (delta_B/B)^2 )

RH1 = (m1 * W) / B1
dRH1 = RH1 * np.sqrt((se_m1/m1)**2 + (delta_W/W)**2 + (delta_B1/B1)**2)

RH2 = (m2 * W) / B2
dRH2 = RH2 * np.sqrt((se_m2/m2)**2 + (delta_W/W)**2 + (delta_B2/B2)**2)

# Average RH
# RH_avg = (RH1 + RH2) / 2
# delta_RH_avg = 0.5 * sqrt(dRH1^2 + dRH2^2)
RH_avg = (RH1 + RH2) / 2
dRH_avg = 0.5 * np.sqrt(dRH1**2 + dRH2**2)

print("=== Hall Coefficient (RH) ===")
print(f"RH1: {RH1:.6e} +/- {dRH1:.6e} m^3/C")
print(f"RH2: {RH2:.6e} +/- {dRH2:.6e} m^3/C")
print(f"RH_avg: {RH_avg:.6e} +/- {dRH_avg:.6e} m^3/C")
print()

# Carrier Concentration: n = 1 / (RH_avg * e)
# delta n = n * (delta_RH_avg / RH_avg)
e_charge = 1.602176634e-19
n = 1.0 / (RH_avg * e_charge)
dn = n * (dRH_avg / RH_avg)

print("=== Carrier Concentration (n) ===")
print(f"n: {n:.6e} +/- {dn:.6e} m^-3")
print()

# ----------------------------
# 4. Residual Field (B0)
# ----------------------------
# B0 = (m0 * W) / RH_avg
# delta B0 = B0 * sqrt( (se_m0/m0)^2 + (delta_W/W)^2 + (delta_RH_avg/RH_avg)^2 )
B0 = (m0 * W) / RH_avg
dB0 = B0 * np.sqrt((se_m0/m0)**2 + (delta_W/W)**2 + (dRH_avg/RH_avg)**2)

print("=== Residual Magnetic Field (B0) ===")
print(f"B0: {B0:.6f} +/- {dB0:.6f} T = {B0*1e4:.2f} +/- {dB0*1e4:.2f} G")
print()

# ----------------------------
# 5. Longitudinal Resistance (Vx vs I)
# ----------------------------
r_slope0, r_se0, r_c0, r_se_c0, r_r2_0 = ols_fit(I_A, Vx_0_V)
r_slope1, r_se1, r_c1, r_se_c1, r_r2_1 = ols_fit(I_A, Vx_1_V)
r_slope2, r_se2, r_c2, r_se_c2, r_r2_2 = ols_fit(I_A, Vx_2_V)

print("=== Longitudinal Resistances (R = slope) ===")
print(f"R1 (Im = 0 A): {r_slope0:.4f} +/- {r_se0:.4f} Ohm, R^2 = {r_r2_0:.6f}")
print(f"R2 (Im = 1 A): {r_slope1:.4f} +/- {r_se1:.4f} Ohm, R^2 = {r_r2_1:.6f}")
print(f"R3 (Im = 2 A): {r_slope2:.4f} +/- {r_se2:.4f} Ohm, R^2 = {r_r2_2:.6f}")
print()

# ----------------------------
# 6. Electromagnet Calibration Table 5
# ----------------------------
# B = (VH * W) / (I * RH_avg)
# delta B = B * sqrt( (delta_VH/VH)^2 + (delta_W/W)^2 + (delta_I/I)^2 + (delta_RH_avg/RH_avg)^2 )
Im_tab5 = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
VH_tab5_mV = np.array([4.8, 9.9, 15.3, 20.5, 26.2, 30.4, 35.0, 40.8, 43.4, 46.5, 50.1])
VH_tab5_V = VH_tab5_mV * 1e-3
I_tab5 = 0.2  # A

B_tab5 = (VH_tab5_V * W) / (I_tab5 * RH_avg)
dB_tab5 = B_tab5 * np.sqrt((delta_VH/VH_tab5_V)**2 + (delta_W/W)**2 + (delta_I/I_tab5)**2 + (dRH_avg/RH_avg)**2)

print("=== Table 5: B vs Im ===")
for im, vh, b, db in zip(Im_tab5, VH_tab5_mV, B_tab5, dB_tab5):
    print(f"Im = {im:.1f} A: VH = {vh:.1f} mV ==> B = {b:.4f} +/- {db:.4f} T")
print()

# Fit B vs Im
slope_B, se_slope_B, intercept_B, se_int_B, r2_B = ols_fit(Im_tab5, B_tab5)
print(f"B vs Im Fit: B = ({slope_B:.4f} +/- {se_slope_B:.4f})*Im + ({intercept_B:.4f} +/- {se_int_B:.4f}), R^2 = {r2_B:.6f}")
print()

# ----------------------------
# 7. Conductivity and Mobility (Vx vs VH)
# ----------------------------
# slope = s
# sigma = l / (s * B * d * RH)
# delta sigma = sigma * sqrt( (delta_l/l)^2 + (se_s/s)^2 + (delta_B/B)^2 + (delta_d/d)^2 + (delta_RH/RH)^2 )
# mu = sigma * RH
# delta mu = mu * sqrt( (delta_sigma/sigma)^2 + (delta_RH/RH)^2 )

s0, se_s0, int_v0, se_int_v0, r2_v0 = ols_fit(VH_0_V, Vx_0_V)
s1, se_s1, int_v1, se_int_v1, r2_v1 = ols_fit(VH_1_V, Vx_1_V)
s2, se_s2, int_v2, se_int_v2, r2_v2 = ols_fit(VH_2_V, Vx_2_V)

print("=== OLS Fits for Vx vs VH ===")
print(f"Im = 0 A: slope = {s0:.4f} +/- {se_s0:.4f}, R^2 = {r2_v0:.6f}")
print(f"Im = 1 A: slope = {s1:.4f} +/- {se_s1:.4f}, R^2 = {r2_v1:.6f}")
print(f"Im = 2 A: slope = {s2:.4f} +/- {se_s2:.4f}, R^2 = {r2_v2:.6f}")
print()

# Calculate sigma and mu with propagated error
# Case 1: Im = 0 A
sigma0 = l / (s0 * B0 * d * RH_avg)
dsigma0 = sigma0 * np.sqrt((delta_l/l)**2 + (se_s0/s0)**2 + (dB0/B0)**2 + (delta_d/d)**2 + (dRH_avg/RH_avg)**2)
mu0 = sigma0 * RH_avg
dmu0 = mu0 * np.sqrt((dsigma0/sigma0)**2 + (dRH_avg/RH_avg)**2)

# Case 2: Im = 1 A
sigma1 = l / (s1 * B1 * d * RH1)
dsigma1 = sigma1 * np.sqrt((delta_l/l)**2 + (se_s1/s1)**2 + (delta_B1/B1)**2 + (delta_d/d)**2 + (dRH1/RH1)**2)
mu1 = sigma1 * RH1
dmu1 = mu1 * np.sqrt((dsigma1/sigma1)**2 + (dRH1/RH1)**2)

# Case 3: Im = 2 A
sigma2 = l / (s2 * B2 * d * RH2)
dsigma2 = sigma2 * np.sqrt((delta_l/l)**2 + (se_s2/s2)**2 + (delta_B2/B2)**2 + (delta_d/d)**2 + (dRH2/RH2)**2)
mu2 = sigma2 * RH2
dmu2 = mu2 * np.sqrt((dsigma2/sigma2)**2 + (dRH2/RH2)**2)

# Average
sigma_avg = (sigma0 + sigma1 + sigma2) / 3
dsigma_avg = np.sqrt(dsigma0**2 + dsigma1**2 + dsigma2**2) / 3
mu_avg = (mu0 + mu1 + mu2) / 3
dmu_avg = np.sqrt(dmu0**2 + dmu1**2 + dmu2**2) / 3

print("=== Conductivity (sigma) and Mobility (mu) ===")
print(f"Case 1 (Im = 0 A): sigma = {sigma0:.2f} +/- {dsigma0:.2f} S/m, mu = {mu0:.4f} +/- {dmu0:.4f} m^2/(V s)")
print(f"Case 2 (Im = 1 A): sigma = {sigma1:.2f} +/- {dsigma1:.2f} S/m, mu = {mu1:.4f} +/- {dmu1:.4f} m^2/(V s)")
print(f"Case 3 (Im = 2 A): sigma = {sigma2:.2f} +/- {dsigma2:.2f} S/m, mu = {mu2:.4f} +/- {dmu2:.4f} m^2/(V s)")
print(f"Average: sigma = {sigma_avg:.2f} +/- {dsigma_avg:.2f} S/m, mu = {mu_avg:.4f} +/- {dmu_avg:.4f} m^2/(V s)")

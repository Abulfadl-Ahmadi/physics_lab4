import numpy as np
import scipy.stats as stats

# Given parameters
delta_theta_deg = 0.01
delta_theta_rad = delta_theta_deg * np.pi / 180

print("--- 1. Grating Calibration ---")
# Calibration data (Sodium and Mercury)
calib_data = [
    {"color": "Red",    "lambda_A": 6154.4, "theta_deg": 21.89},
    {"color": "Yellow", "lambda_A": 5890.0, "theta_deg": 21.01},
    {"color": "Green",  "lambda_A": 5682.7, "theta_deg": 20.11},
]

d_values = []
delta_d_values = []

for row in calib_data:
    theta_rad = row["theta_deg"] * np.pi / 180
    lam = row["lambda_A"]
    d = lam / np.sin(theta_rad)
    
    # Error in d: d = lam / sin(theta) => dd = lam * cos(theta) / sin^2(theta) * dtheta
    dd = lam * np.cos(theta_rad) / (np.sin(theta_rad)**2) * delta_theta_rad
    
    d_values.append(d)
    delta_d_values.append(dd)
    
    row["d"] = d
    row["delta_d"] = dd
    row["N"] = 1e7 / d # mm^-1

d_values = np.array(d_values)
delta_d_values = np.array(delta_d_values)

d_avg = np.mean(d_values)
# For the error of the mean, we can either use standard deviation / sqrt(N) or propagation
d_std = np.std(d_values, ddof=1)
d_err_prop = np.sqrt(np.sum(delta_d_values**2)) / len(delta_d_values)
delta_d_avg = max(d_std / np.sqrt(len(d_values)), d_err_prop)

N_avg = 1e7 / d_avg
delta_N_avg = N_avg * (delta_d_avg / d_avg)

print(f"d_avg = {d_avg:.2f} \pm {delta_d_avg:.2f} A")
print(f"N_avg = {N_avg:.2f} \pm {delta_N_avg:.2f} lines/mm")

print("\n--- 2. Hydrogen Spectrum & Rydberg Constant ---")
# Hydrogen data
h_data = [
    {"color": "Violet", "theta_deg": 14.41, "ni": 6},
    {"color": "Blue",   "theta_deg": 15.37, "ni": 5},
    {"color": "Green",  "theta_deg": 17.32, "ni": 4},
    {"color": "Red",    "theta_deg": 23.62, "ni": 3},
]

R_values = []
delta_R_values = []

for row in h_data:
    theta_rad = row["theta_deg"] * np.pi / 180
    lam = d_avg * np.sin(theta_rad)
    
    # Error in lambda: lam = d * sin(theta)
    # dlam = sqrt( (sin(theta) * dd)^2 + (d * cos(theta) * dtheta)^2 )
    term1 = np.sin(theta_rad) * delta_d_avg
    term2 = d_avg * np.cos(theta_rad) * delta_theta_rad
    dlam = np.sqrt(term1**2 + term2**2)
    
    nf = 2
    ni = row["ni"]
    factor = (1/(nf**2) - 1/(ni**2))
    
    # R_inf = 1 / (lam * factor)
    # R_inf is in A^-1. Multiply by 1e7 to get nm^-1 or 1e10 to get m^-1.
    R = 1 / (lam * factor)
    dR = R * (dlam / lam)
    
    R_nm_inv = R * 1e1  # A^-1 to nm^-1 (10 A = 1 nm)
    dR_nm_inv = dR * 1e1
    
    R_m_inv = R * 1e10
    dR_m_inv = dR * 1e10
    
    row["lam"] = lam
    row["dlam"] = dlam
    row["R_nm_inv"] = R_nm_inv
    row["dR_nm_inv"] = dR_nm_inv
    row["R_m_inv"] = R_m_inv
    row["dR_m_inv"] = dR_m_inv
    
    R_values.append(R_m_inv)
    delta_R_values.append(dR_m_inv)

R_values = np.array(R_values)
delta_R_values = np.array(delta_R_values)

R_avg = np.mean(R_values)
R_std = np.std(R_values, ddof=1)
R_err_prop = np.sqrt(np.sum(delta_R_values**2)) / len(delta_R_values)
delta_R_avg = max(R_std / np.sqrt(len(R_values)), R_err_prop)

theoretical_R = 1.097373e7 # m^-1
relative_error = abs(R_avg - theoretical_R) / theoretical_R * 100

print(f"R_avg = {R_avg:.2e} \pm {delta_R_avg:.2e} m^-1")
print(f"Relative error: {relative_error:.3f} %")

print("\n--- 3. Sodium Doublet ---")
doublet_data = [
    {"theta_deg": 45.55, "n": 2},
    {"theta_deg": 45.61, "n": 2},
]

lams = []
dlams = []
for row in doublet_data:
    theta_rad = row["theta_deg"] * np.pi / 180
    n = row["n"]
    lam = d_avg * np.sin(theta_rad) / n
    
    term1 = (np.sin(theta_rad) / n) * delta_d_avg
    term2 = (d_avg * np.cos(theta_rad) / n) * delta_theta_rad
    dlam = np.sqrt(term1**2 + term2**2)
    
    lams.append(lam)
    dlams.append(dlam)
    print(f"Lambda = {lam:.2f} \pm {dlam:.2f} A")

delta_lambda = lams[1] - lams[0]
delta_lambda_err = np.sqrt(dlams[0]**2 + dlams[1]**2)
print(f"Delta Lambda = {delta_lambda:.2f} \pm {delta_lambda_err:.2f} A")

print("\n--- Generating LaTeX Tables ---")
# Grating table
print("\\begin{table}[H]")
print("\\centering")
print("\\caption{Calibration of the diffraction grating using spectral lines of known wavelength.}")
print("\\label{tab:calibration}")
print("\\begin{tabular}{lcccccc}")
print("\\toprule")
print("Colour & $\\lambda$ (\\AA) & $\\theta$ ($^\\circ$) & $\\sin\\theta$ & Order ($m$) & $d$ (\\AA) & $N$ (lines/mm) \\\\")
print("\\midrule")
for r in calib_data:
    print(f"{r['color']} & {r['lambda_A']} & {r['theta_deg']} & {np.sin(r['theta_deg']*np.pi/180):.4f} & 1 & ${r['d']:.1f} \\pm {r['delta_d']:.1f}$ & ${r['N']:.1f}$ \\\\")
print("\\midrule")
print(f"\\multicolumn{{5}}{{l}}{{\\textbf{{Average}}}} & $\\mathbf{{{d_avg:.1f} \\pm {delta_d_avg:.1f}}}$ & $\\mathbf{{{N_avg:.1f} \\pm {delta_N_avg:.1f}}}$ \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}")

# Hydrogen table
print("\\begin{table}[H]")
print("\\centering")
print("\\caption{Experimental data for the Hydrogen Balmer series and the calculated Rydberg constant.}")
print("\\label{tab:hydrogen}")
print("\\begin{tabular}{lcccccc}")
print("\\toprule")
print("Colour & $n_i \\to n_f$ & $\\theta$ ($^\\circ$) & $\\lambda$ (\\AA) & $\\delta\\lambda$ (\\AA) & $R_\\infty$ ($10^7$ m$^{-1}$) \\\\")
print("\\midrule")
for r in h_data:
    r_val = r['R_m_inv'] / 1e7
    r_err = r['dR_m_inv'] / 1e7
    print(f"{r['color']} & {r['ni']}$\\to 2$ & {r['theta_deg']} & {r['lam']:.2f} & {r['dlam']:.2f} & ${r_val:.4f} \\pm {r_err:.4f}$ \\\\")
print("\\midrule")
R_avg_print = R_avg / 1e7
R_err_print = delta_R_avg / 1e7
print(f"\\multicolumn{{5}}{{l}}{{\\textbf{{Average $R_\\infty$}}}} & $\\mathbf{{{R_avg_print:.4f} \\pm {R_err_print:.4f}}}$ \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}")

# Doublet table
print("\\begin{table}[H]")
print("\\centering")
print("\\caption{Resolution of the Sodium D-lines doublet ($m=2$).}")
print("\\label{tab:doublet}")
print("\\begin{tabular}{lcccc}")
print("\\toprule")
print("Line & $\\theta$ ($^\\circ$) & $m$ (Order) & $\\lambda$ (\\AA) & $\\Delta\\lambda$ (\\AA) \\\\")
print("\\midrule")
print(f"$D_1$ & {doublet_data[0]['theta_deg']} & 2 & ${lams[0]:.2f} \\pm {dlams[0]:.2f}$ & \\multirow{{2}}{{*}}{{${delta_lambda:.2f} \\pm {delta_lambda_err:.2f}$}} \\\\")
print(f"$D_2$ & {doublet_data[1]['theta_deg']} & 2 & ${lams[1]:.2f} \\pm {dlams[1]:.2f}$ & \\\\")
print("\\bottomrule")
print("\\end{tabular}")
print("\\end{table}")


import numpy as np
import itertools
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

# Constants
eta = 1.82e-5      # N s m^-2
rho_i = 875.0      # kg m^-3
rho_l = 1.29       # kg m^-3
g = 9.81           # m s^-2
d = 6e-3           # m
e_theoretical = 1.602e-19 # C

# ---------------------------------------------------------
# Static Method Data (Table 1-7)
# S(m), t(s), U(V)
static_data_raw = np.array([
    [0.0008, 2.02, 520],
    [0.00176, 4.89, 520],
    [0.001067, 6.6, 520],
    [0.000427, 6.66, 520],
    [0.00064, 2.01, 520],
    [0.000747, 2.32, 520],
    [0.00064, 2.36, 520],
    [0.000693, 2.63, 520]
])

S_static = static_data_raw[:, 0]
t_static = static_data_raw[:, 1]
U_static = static_data_raw[:, 2]

v1_static = S_static / t_static

# Equation 3 for Static Method
# q = (18 * pi * d * v1 / U) * sqrt( (eta * v1) / (2 * (rho_i - rho_l) * g) ) * eta
# Wait, let's use the exact equation from the manual:
# q = (18 * pi * eta * d * v1 / U) * sqrt( (eta * v1) / (2 * (rho_i - rho_l) * g) )
q_static_original = (18 * np.pi * eta * d * v1_static / U_static) * np.sqrt( (eta * v1_static) / (2 * (rho_i - rho_l) * g) )

# Calculate pairwise differences for static drops
q_static_diffs = []
for i, j in itertools.combinations(range(len(q_static_original)), 2):
    q_static_diffs.append(abs(q_static_original[i] - q_static_original[j]))

q_static_diffs = np.array(q_static_diffs)
q_static_expanded = np.concatenate((q_static_original, q_static_diffs))


# ---------------------------------------------------------
# Dynamic Method Data (Table 2-7)
# S1(m), t1(s), S2(m), t2(s), U(V)
dynamic_data_raw = np.array([
    [0.000853, 2.75, 0.000664, 1.0, 520],
    [0.002, 4.52, 0.001967, 6.7, 530],
    [0.00131, 3.42, 0.001237, 6.4, 530],
    [0.001067, 5.08, 0.00176, 9.4, 540],
    [0.0009, 2.92, 0.00188, 3.22, 550],
    [0.00099, 6.47, 0.001057, 6.42, 580],
    [0.001077, 3.55, 0.001343, 16.9, 600]
])

S1_dyn = dynamic_data_raw[:, 0]
t1_dyn = dynamic_data_raw[:, 1]
S2_dyn = dynamic_data_raw[:, 2]
t2_dyn = dynamic_data_raw[:, 3]
U_dyn = dynamic_data_raw[:, 4]

v1_dyn = S1_dyn / t1_dyn
v2_dyn = S2_dyn / t2_dyn

# Equation 4 for Dynamic Method
# q = (v1 + v2) * (v1**0.5 / U) * eta**1.5 * 18 * pi * d / sqrt(2 * (rho_i - rho_l) * g)
q_dyn_original = (v1_dyn + v2_dyn) * (np.sqrt(v1_dyn) / U_dyn) * (eta**1.5) * 18 * np.pi * d / np.sqrt(2 * (rho_i - rho_l) * g)

# Calculate pairwise differences for dynamic drops
q_dyn_diffs = []
for i, j in itertools.combinations(range(len(q_dyn_original)), 2):
    q_dyn_diffs.append(abs(q_dyn_original[i] - q_dyn_original[j]))

q_dyn_diffs = np.array(q_dyn_diffs)
q_dyn_expanded = np.concatenate((q_dyn_original, q_dyn_diffs))

# Master Dataset
q_master = np.concatenate((q_static_expanded, q_dyn_expanded))


# ---------------------------------------------------------
# Analysis Function to find e
def estimate_e(q_data, label):
    # Sort data
    q_sorted = np.sort(q_data)
    
    # Exclude near-zero differences (noise)
    q_filtered = q_sorted[q_sorted > 0.5e-19] 
    
    # Guess n by dividing by theoretical e and rounding
    n_guess = np.round(q_filtered / e_theoretical)
    
    # We only want to use data where n >= 1
    valid_idx = n_guess >= 1
    n_valid = n_guess[valid_idx]
    q_valid = q_filtered[valid_idx]
    
    # Experimental e for each point
    e_exp_array = q_valid / n_valid
    
    # Mean e
    e_mean = np.mean(e_exp_array)
    e_std = np.std(e_exp_array, ddof=1)
    e_stderr = e_std / np.sqrt(len(e_exp_array))
    
    rel_error = abs(e_mean - e_theoretical) / e_theoretical * 100
    
    print(f"\n--- {label} ---")
    print(f"Total points analyzed (n >= 1): {len(e_exp_array)}")
    print(f"Calculated e = {e_mean:.4e} \pm {e_stderr:.4e} C")
    print(f"Relative Error = {rel_error:.2f}%")
    
    return e_mean, q_valid, n_valid

e_static, q_val_stat, n_val_stat = estimate_e(q_static_expanded, "Expanded Static Dataset (36 pts)")
e_dyn, q_val_dyn, n_val_dyn = estimate_e(q_dyn_expanded, "Expanded Dynamic Dataset (28 pts)")
e_master, q_val_mast, n_val_mast = estimate_e(q_master, "Master Combined Dataset (64 pts)")


# ---------------------------------------------------------
# Plotting
def plot_histogram(q_data, e_est, title, filename):
    plt.figure(figsize=(16, 5))
    bins = np.arange(0, max(q_data) + 0.5e-19, 0.5e-19)
    plt.hist(q_data, bins=bins, color='skyblue', edgecolor='black')
    
    # Mark the calculated e and its multiples
    max_n = int(np.ceil(max(q_data) / e_est))
    for n in range(1, max_n + 1):
        plt.axvline(n * e_est, color='red', linestyle='dashed', alpha=0.7)
        plt.text(n * e_est, plt.gca().get_ylim()[1]*0.9, f'{n}e', color='red', ha='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

    plt.xlabel('Calculated Charge $q$ (C)')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'plots/{filename}.pdf')
    plt.close()

plot_histogram(q_static_expanded, e_static, 'Charge Distribution (Static Expanded)', 'hist_static')
plot_histogram(q_dyn_expanded, e_dyn, 'Charge Distribution (Dynamic Expanded)', 'hist_dynamic')
plot_histogram(q_master, e_master, 'Charge Distribution (Master Combined)', 'hist_master')

# ---------------------------------------------------------
# LaTeX outputs
print("\n--- LaTeX Outputs ---")

# Print the original static q values for the LaTeX table
print("\nStatic Table 1-7 $q(C)$ column:")
for q in q_static_original:
    print(f"${q:.3e}$ \\\\")

print("\nDynamic Table 2-7 $q(C)$ column:")
for q in q_dyn_original:
    print(f"${q:.3e}$ \\\\")

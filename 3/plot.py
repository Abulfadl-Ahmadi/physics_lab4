import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import scipy.stats as stats
from scipy.interpolate import PchipInterpolator

# Apply professional publication styling
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Computer Modern", "DejaVu Serif", "Times New Roman"],
    "axes.labelsize": 11,
    "font.size": 11,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "grid.alpha": 0.5,
    "grid.linestyle": "--"
})

def plot_smooth(ax, x, y, fmt, label):
    # Sort just in case, though U2 is already sorted
    idx = np.argsort(x)
    x = x[idx]
    y = y[idx]
    
    x_smooth = np.linspace(x.min(), x.max(), 300)
    spl = PchipInterpolator(x, y)
    y_smooth = spl(x_smooth)
    
    # plot smooth line
    p = ax.plot(x_smooth, y_smooth, '-')
    color = p[0].get_color()
    # plot points
    ax.plot(x, y, fmt, color=color, markersize=4, label=label)

# Read data.md
with open('data.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

u2_list = []
table1 = []
table2 = []
table3 = []

for line in lines[2:]:
    parts = [p.strip() for p in line.split('|') if p.strip()]
    if len(parts) == 4:
        u2 = float(parts[0])
        t1 = float(parts[1])
        t2 = float(parts[2])
        t3 = float(parts[3])
        u2_list.append(u2)
        table1.append(t1)
        table2.append(t2)
        table3.append(t3)

u2_arr = np.array(u2_list)
t1_arr = np.array(table1)
t2_arr = np.array(table2)
t3_arr = np.array(table3)

# Find peaks and valleys for Table 1 (optimal)
peaks_idx, _ = find_peaks(t1_arr, distance=5, prominence=0.2)
valleys_idx, _ = find_peaks(-t1_arr, distance=5, prominence=0.2)

peak_V = u2_arr[peaks_idx]
valley_V = u2_arr[valleys_idx]

n_peaks = np.arange(1, len(peak_V) + 1)
n_valleys = np.arange(1, len(valley_V) + 1)

# Linear regression for Peaks
slope_p, intercept_p, r_value_p, p_value_p, std_err_p = stats.linregress(n_peaks, peak_V)

# Linear regression for Valleys
slope_v, intercept_v, r_value_v, p_value_v, std_err_v = stats.linregress(n_valleys, valley_V)

# --- Plot 1: I-V Curves ---
plt.figure(figsize=(8, 5))
plot_smooth(plt.gca(), u2_arr, t1_arr, 'o', 'Table 1 ($U_1$, $U_3$ opt.)')
plot_smooth(plt.gca(), u2_arr, t2_arr, 's', 'Table 2')
plot_smooth(plt.gca(), u2_arr, t3_arr, '^', 'Table 3')

plt.xlabel('Accelerating Voltage $U_2$ (V)')
plt.ylabel('Anode Current $I_A$ (Relative)')
plt.title('Franck-Hertz I-V Curves')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('franck_hertz_plot.pdf')
plt.savefig('franck_hertz_plot.png')
plt.close()

# --- Plot 2: Linear Regression ---
plt.figure(figsize=(8, 5))

# Regression equation: V = m*n + c
v_fit_p = intercept_p + slope_p * n_peaks
v_fit_v = intercept_v + slope_v * n_valleys

plt.errorbar(n_peaks, peak_V, yerr=0.5, fmt='bo', label='Peak Positions', capsize=5)
plt.plot(n_peaks, intercept_p + slope_p * n_peaks, 'b--', linewidth=1.5, label=f'Peak Fit ($E_{{exc}}={slope_p:.2f}$ eV)')

plt.errorbar(n_valleys, valley_V, yerr=0.5, fmt='ro', label='Valley Positions', capsize=5)
plt.plot(n_valleys, intercept_v + slope_v * n_valleys, 'r--', linewidth=1.5, label=f'Valley Fit ($E_{{exc}}={slope_v:.2f}$ eV)')

plt.xlabel('Extremum Order ($n$)')
plt.ylabel('Accelerating Voltage $U_2$ (V)')
plt.title('OLS Regression of Extrema')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('regression_plot.pdf')
plt.savefig('regression_plot.png')
plt.close()

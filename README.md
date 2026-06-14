# Physics Lab IV — General Physics Laboratory

**Sharif University of Technology**
**Department of Physics**
**Student:** Abulfadl Ahmadi
**Semester:** Semester 4 (Spring 2026)
**Professor:** Dr. Khademi
**Teaching Assistants:** Yasin Amiri, Sonia

---

## Overview

This repository contains the complete data, analysis scripts, and final LaTeX reports for the **Physics Lab IV** course at Sharif University of Technology. The course covers 10 experiments spanning foundational topics in modern physics — from the quantum nature of light and matter to semiconductor physics and atomic spectroscopy.

Each experiment directory encapsulates the entire workflow: raw data extraction, Python-based rigorous statistical error propagation, Ordinary Least Squares (OLS) regression, and a professionally typeset LaTeX academic report.

### Physics Covered

The experiments trace the historical development of quantum mechanics:

1. **Hall Effect** — Semiconductor physics, charge carrier quantization in solids
2. **Franck-Hertz** — First direct evidence for atomic energy quantization (1914)
3. **Photoelectric Effect** — Particle nature of light, Einstein's photon hypothesis (1905)
4. **Rydberg Constant** — Hydrogen emission spectrum, Bohr model validation
5. **Electron Diffraction** — Wave-particle duality, de Broglie hypothesis (1924)
6. **Black Body Radiation** — Birth of quantum mechanics, Stefan-Boltzmann law
7. **X-Ray Detection** — Beer-Lambert attenuation, photoelectric Z-dependence
8. **Compton Scattering** — Photon momentum, particle collisions of light
9. **Ionization** — Atomic ionization energies from electron impact
10. **Millikan Oil Drop** — Quantization of electric charge

---

## Repository Structure

### 1. [1-Hall Effect](./1-Hall/)
**Objective:** Investigate the Hall effect in an n-type Indium Antimonide (InSb) semiconductor.

**Key Results:** Hall coefficient R_H = (−4.36 ± 0.09) × 10⁻⁴ m³/C, carrier density n = 1.43 × 10²² m⁻³, conductivity σ̄ = 675 S/m, mobility μ̄ = 0.294 m²/(V·s), positive magnetoresistance verified.

**Tools:** `analysis_advanced.py` for OLS regression and full partial-derivative error propagation; `generate_plots_advanced.py` for plots with error bars.

### 2. [2-Franck-Hertz Experiment](./2-franck-hertz/)
**Objective:** Verify quantization of atomic energy levels using a Mercury (Hg) vapor tube.

**Key Results:** Excitation energy E_exc = 5.40 ± 0.08 eV, emitted UV wavelength λ = 229.6 ± 3.4 nm. Periodic current drops from inelastic electron-atom collisions.

**Tools:** `plot.py` for I-V curve smoothing, peak/valley extraction, and OLS regression of extrema.

### 3. [3-Photoelectric Effect](./3-photoelectric/)
**Objective:** Confirm the quantum nature of light and Einstein's photoelectric equation.

**Key Results:** Planck's constant h = 2.26 × 10⁻³⁴ J·s (65.8% systematic error from contact potential and dark currents). Demonstrates the linear U₀ vs. ν relation.

**Tools:** `analysis.py` for multi-trial averaging and stopping potential regression.

### 4. [4-Rydberg Constant](./4-rydberg-constant/)
**Objective:** Analyze the Balmer series emission spectrum of hydrogen using a diffraction grating spectrometer.

**Key Results:** R∞ = (1.0907 ± 0.0021) × 10⁷ m⁻¹ (0.608% relative error). Grating constant d = 16487.8 ± 30.4 Å. Sodium D-lines doublet resolved in second order.

**Tools:** `analysis.py` for trigonometric error propagation and LaTeX table generation.

### 5. [5-Electron Diffraction](./5-electron-diffraction/)
**Objective:** Demonstrate wave-particle duality via electron diffraction through polycrystalline graphite.

**Key Results:** Lattice spacings d₁ = 2.150 ± 0.075 Å and d₂ = 1.201 ± 0.027 Å. Ratio d₁/d₂ ≈ 1.79 confirms hexagonal graphite structure. C-C bond distance = 1.433 Å. Theoretical: 1.42 Å.

**Tools:** `analysis.py` for Bragg angle geometry, OLS regression of sin(θ) vs. 1/√V.

### 6. [6-Black Body Radiation](./6-black-body/)
**Objective:** Study spectral energy distribution and verify the Stefan-Boltzmann law and inverse-square law.

**Key Results:** σ = 4.845 × 10⁻⁸ W/(m²·K⁴) (14.56% relative error), R² = 0.9997 for T⁴ dependence. Inverse-square law verified with R² = 0.9959.

**Tools:** `analysis.py` for regression of R(T) vs. (T⁴ − T₀⁴) and I vs. 1/r².

### 7. [7-X-Ray Detection and Absorption](./7-x-ray/)
**Objective:** Characterize GM counter, verify Beer-Lambert law, and study Z-dependence of X-ray absorption.

**Key Results:** Geiger plateau at 300–500 V. Linear attenuation coefficient μ = 2.972 cm⁻¹ for Al. Transmission drops from 95% (C, Z=6) to 0.2% (Ag, Z=47), confirming μ ∝ Z⁴.

**Tools:** `analysis.py` for plateau analysis, semi-log attenuation regression, and Z-dependence plots.

### 8. [8-Compton Scattering](./8-compton/)
**Objective:** Verify the Compton wavelength shift and Duane-Hunt law using X-ray diffraction on LiF.

**Key Results:** Compton shift at 145° = 0.0543 Å (23% error, theoretical 0.0441 Å). Planck's constant via Duane-Hunt: h = 1.095 × 10⁻³³ J·s (systematic limitations).

**Tools:** `analysis.py` for spectra analysis, Cu foil absorption calibration, and Compton kinematics.

### 9. [9-Ionization](./9-ionization/)
**Objective:** Measure the ionization potential of mercury vapor by electron impact.

**Key Results:** Ionization threshold of Hg ≈ 10.44 eV, complementing the Franck-Hertz excitation energy (4.9 eV) to map the full atomic energy level structure.

### 10. [10-Millikan Oil Drop](./10-millikan/)
**Objective:** Verify charge quantization and measure the elementary charge e.

**Key Results:** e = (1.597 ± 0.019) × 10⁻¹⁹ C (0.29% error) from expanded static dataset of 36 points using pairwise-difference technique. Master combined dataset (64 points) gives 1.03% error.

**Tools:** `analysis.py` for charge calculation, pairwise-difference expansion, quantization search, and histogram generation.

---

## How to Use This Repository

### Prerequisites

- Python 3.8+ with `numpy`, `scipy`, `matplotlib`
- A LaTeX distribution (e.g., TeX Live, MiKTeX) with `pdflatex`
- Recommended LaTeX packages: `booktabs`, `siunitx`, `fouriernc`, `amsmath`, `amssymb`, `graphicx`, `geometry`, `float`, `hyperref`, `multirow`

### Compiling a Report

Navigate to any experiment directory and run:

```bash
pdflatex <report_name>.tex
```

Some reports require running the Python analysis script first to generate plots:

```bash
cd <experiment_directory>
python analysis.py        # or plot.py, depending on the experiment
pdflatex <report_name>.tex
```

### Running the Analysis Scripts

Each experiment's `analysis.py` (or equivalent) can be run standalone:

```bash
cd <experiment_directory>
python analysis.py
```

This will typically:
1. Process raw data from `.md` files or hardcoded arrays
2. Perform OLS linear regression with standard errors
3. Calculate physical parameters with partial-derivative error propagation
4. Generate publication-quality PDF plots in the `plots/` subdirectory
5. Print LaTeX-formatted tables to stdout (for copy-paste into the `.tex` file)

---

## Methodology

### Error Analysis Philosophy

All experiments follow a consistent, rigorous approach to uncertainty:

1. **Instrumental uncertainties** — precision limits from multimeters, micrometers, and angular vernier scales
2. **OLS regression** — Ordinary Least Squares fitting with standard error of slope and intercept
3. **Partial-derivative propagation** — for any derived quantity q(x, y, z, ...):
   ```
   δq = √((∂q/∂x · δx)² + (∂q/∂y · δy)² + (∂q/∂z · δz)² + ...)
   ```
4. **Confidence intervals** — all results reported as x ± δx

### Report Standards

All LaTeX reports use:
- `booktabs` for professional table rules
- `siunitx` for consistent SI unit formatting
- `fouriernc` (New Century Schoolbook) font
- Scatter plots with horizontal and vertical error bars
- OLS best-fit lines with R² values
- Full derivations of all equations used

---

## Technologies & Tools

| Tool | Purpose |
|------|---------|
| **Python 3** | Data processing, regression, error propagation |
| **NumPy** | Array operations, linear algebra |
| **SciPy** | `linregress` for OLS, `find_peaks` for extrema |
| **Matplotlib** | Publication-quality plots with error bars |
| **LaTeX** | Professional academic report typesetting |
| **pdflatex** | PDF compilation |

---

## Academic Integrity

These reports reflect deep theoretical understanding and rigorous data analysis. All answers to post-lab questions are thoroughly derived from fundamental quantum and classical mechanics principles. The analysis methods (pairwise-difference expansion, systematic error decomposition) go beyond standard lab requirements.

---

## Quick Reference — Key Physical Constants Used

| Constant | Symbol | Value |
|----------|--------|-------|
| Planck's constant | h | 6.626 × 10⁻³⁴ J·s |
| Elementary charge | e | 1.602 × 10⁻¹⁹ C |
| Electron mass | m_e | 9.109 × 10⁻³¹ kg |
| Speed of light | c | 2.998 × 10⁸ m/s |
| Stefan-Boltzmann constant | σ | 5.67 × 10⁻⁸ W/(m²·K⁴) |
| Rydberg constant | R∞ | 1.097 × 10⁷ m⁻¹ |
| Wien's displacement constant | b | 2.898 × 10⁻³ m·K |
| Compton wavelength | h/(m_e·c) | 0.0243 Å |

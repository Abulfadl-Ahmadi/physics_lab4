# Experiment 1: The Hall Effect

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Hall Effect** experiment.

## Overview

The goal of this experiment is to investigate the Hall effect in an n-type Indium Antimonide (InSb) semiconductor crystal. By applying a transverse magnetic field to a current-carrying sample, a Hall voltage is generated perpendicular to both the current and the field directions.

## Theoretical Background

### The Hall Effect

When a current I flows through a conductor of width W and thickness d, and a magnetic field B is applied perpendicular to the current, charge carriers experience a transverse Lorentz force:

```
F_L = q(v_d × B)
```

For electrons (the majority carriers in n-type InSb), this force deflects carriers to one side of the sample, creating a charge separation. This separation establishes a transverse Hall electric field E_H. In steady state, the electric force balances the Lorentz force:

```
qE_H + qv_dB = 0  →  E_H = v_d · B
```

The Hall voltage measured across the sample width is:

```
V_H = E_H · W = (I · B) / (n · q · d)
```

The **Hall coefficient** is defined as R_H = 1/(nq). For n-type semiconductors, R_H is negative:

```
R_H = V_H · W / (I · B)
```

### Magnetoresistance

In addition to the Hall effect, the longitudinal resistance of the sample increases with magnetic field — this is called **positive magnetoresistance**. It occurs because the transverse magnetic field curves the charge carrier trajectories, effectively increasing the path length and thus the scattering rate.

### Conductivity and Mobility

The electrical conductivity σ and carrier mobility μ are derived from the Hall coefficient and the longitudinal voltage V_x:

```
σ = l / (s · B · d · R_H)     where s = dV_x/dV_H
μ = σ · |R_H|
```

## Experimental Setup

- InSb semiconductor crystal (l = 13.0 mm, W = 0.50 mm, d = 6.0 mm)
- Electromagnet with adjustable coil current I_m (0–2.5 A)
- Dual DC current source for sample bias current I (0–200 mA)
- Microvoltmeter for Hall voltage V_H
- Voltmeter for longitudinal voltage V_x

## Key Analyses

- **V_H vs. I regression**: OLS linear fits at three magnet currents (0, 1, 2 A) to extract the Hall coefficient
- **Hall coefficient calculation**: R_H = (slope · W) / B with full partial-derivative error propagation
- **Carrier density**: n = 1 / (|R_H| · e)
- **Residual field B₀**: calculated from the I_m = 0 A data
- **Magnetoresistance**: comparing longitudinal resistances R₁, R₂, R₃ at different fields
- **Electromagnet calibration**: B vs. I_m curve with error bars
- **Conductivity and mobility**: from V_x vs. V_H regression slopes

## Results

| Parameter | Value |
|-----------|-------|
| Hall coefficient R_H | (−4.36 ± 0.09) × 10⁻⁴ m³/C |
| Carrier density n | (1.43 ± 0.03) × 10²² m⁻³ |
| Residual field B₀ | 277 ± 8 G |
| Conductivity σ̄ | 675 ± 16 S/m |
| Mobility μ̄ | 0.294 ± 0.009 m²/(V·s) |
| R₁ (0 A), R₂ (1 A), R₃ (2 A) | 6.378, 6.428, 6.468 Ω |

## Files

- `hall.tex` — LaTeX source for the full report
- `hall.pdf` — Compiled report
- `analysis_advanced.py` — Python script for all regressions, error propagation, and parameter calculations
- `generate_plots_advanced.py` — Python script for generating scatter plots with error bars
- `VH_vs_I_errorbars.pdf` — Hall voltage vs. current at three magnet currents
- `Vx_vs_I_errorbars.pdf` — Longitudinal voltage vs. current
- `Vx_vs_VH_errorbars.pdf` — Longitudinal vs. Hall voltage
- `B_vs_Im_errorbars.pdf` — Electromagnet calibration curve
- `README.md` — This file
- `sut.jpg` — University logo
- `unused_files/` — Earlier analysis scripts and exploratory code (archived)
- `sample/` — Sample data and reference materials

## How to Compile

```bash
pdflatex hall.tex
```

## Notes

- The sign of V_H reverses when either I or B is reversed, confirming the Lorentz force direction
- The Hall effect is much easier to observe in semiconductors than in metals because carrier density is orders of magnitude lower, yielding larger Hall voltages (mV vs. nV)
- Thermoelectric and thermomagnetic effects (Ettingshausen, Peltier, Seebeck) are sources of systematic error

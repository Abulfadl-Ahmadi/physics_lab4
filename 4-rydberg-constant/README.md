# Experiment 4: Measurement of the Rydberg Constant

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Rydberg Constant** experiment.

## Overview
This experiment involves analyzing the visible emission spectrum (Balmer series) of the hydrogen atom to determine the fundamental Rydberg constant ($R_\infty$). It utilizes a diffraction grating spectrometer to accurately measure the wavelengths of the emitted photons.

## Key Analyses
- **Grating Calibration:** The diffraction grating constant ($d$) and line density ($N$) were first precisely calibrated using known spectral lines (Red, Yellow, Green) from a multi-wavelength lamp.
- **Rydberg Constant Calculation:** Measured the diffraction angles for the four visible hydrogen Balmer lines (Violet, Blue, Green, Red) to calculate their wavelengths and ultimately determine $R_\infty$.
- **Sodium Doublet Resolution:** Demonstrated the resolving power of the grating by measuring the wavelength splitting ($\Delta\lambda$) of the fine-structure Sodium D-lines ($D_1$ and $D_2$) in the second diffraction order.
- **Rigorous Error Propagation:** The analysis includes exact partial derivative error propagation stemming from the instrumental angular reading uncertainty ($\delta\theta = 0.01^\circ$).

## Files
- `rydberg.tex`: The main LaTeX source file for the report.
- `analysis.py`: Python script used for rigorous trigonometric error propagation and generating LaTeX tables.
- `data.md`: Raw angular and color data collected during the experiment.
- `rydberg-constant.pdf`: The original Persian lab manual.

## How to Compile
```bash
pdflatex rydberg.tex
```

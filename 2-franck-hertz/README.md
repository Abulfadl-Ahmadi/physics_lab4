# Experiment 2: The Franck-Hertz Experiment

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Franck-Hertz** experiment.

## Overview
This classic experiment provides direct, non-spectroscopic evidence for the quantization of atomic energy levels (the Bohr model). A beam of electrons is accelerated through a tube containing Mercury (Hg) vapor. As the accelerating voltage increases, electrons undergo inelastic collisions with mercury atoms, losing discrete amounts of kinetic energy corresponding to the first excitation energy of mercury.

## Key Analyses
- **I-V Characteristic Curves:** Plotted the periodic drops in anode current as a function of accelerating voltage, superimposed on the background space-charge current.
- **Excitation Energy ($E_{\text{exc}}$):** Used Ordinary Least Squares (OLS) linear regression on the positions of the peaks and valleys to accurately determine the first excitation energy of mercury ($\sim 4.9 \text{ eV}$). This method automatically factors out contact potentials.
- **Error Analysis:** Standard error bands and propagated uncertainties were calculated for the excitation energy and the corresponding emitted photon wavelength in the UV spectrum.

## Files
- `report.tex`: The main LaTeX source file for the report.
- `report.pdf`: The compiled final report.
- `plot.py`: Python script used to extract peak/valley extrema and perform regressions.
- `*.pdf` / `*.png` (Plots): Generated $I-V$ curves and regression fits.

## How to Compile
```bash
pdflatex report.tex
```

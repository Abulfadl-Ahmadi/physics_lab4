# Experiment 1: The Hall Effect

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Hall Effect** experiment.

## Overview
The goal of this experiment is to investigate the Hall effect in an n-type Indium Antimonide (InSb) semiconductor crystal. By applying a transverse magnetic field to a current-carrying sample, a Hall voltage is generated. 

## Key Analyses
- **Hall Coefficient ($R_H$):** Determined through Ordinary Least Squares (OLS) linear regression of Hall voltage vs. sample current.
- **Carrier Density ($n$):** Calculated to find the concentration of majority charge carriers in the n-type semiconductor.
- **Magnetoresistance:** Analyzed the longitudinal resistance of the sample at different magnetic field strengths to verify positive magnetoresistance.
- **Error Propagation:** Rigorous partial derivative error propagation was applied to all secondary parameters ($\sigma$, $\mu$, $B_0$) using instrumental tolerances and regression standard errors.

## Files
- `hall.tex`: The main LaTeX source file for the report.
- `hall.pdf`: The compiled final report.
- `analysis_advanced.py` / `generate_plots_advanced.py`: Python scripts used for statistical regressions and plot generation.
- `*.pdf` (Plots): Generated scatter plots with horizontal and vertical error bars alongside their OLS best-fit lines.

## How to Compile
```bash
pdflatex hall.tex
```

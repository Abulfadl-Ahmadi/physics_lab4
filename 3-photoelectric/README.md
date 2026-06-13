# Experiment 3: The Photoelectric Effect

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Photoelectric Effect** experiment.

## Overview
This experiment investigates the quantum nature of light as proposed by Albert Einstein. By illuminating a photocathode with monochromatic light (using filters and a mercury lamp), electrons are ejected. We apply a retarding potential to halt the photocurrent, allowing us to measure the maximum kinetic energy of the emitted photoelectrons as a function of light frequency.

## Key Analyses
- **Photocurrent vs. Voltage ($I-V$):** Plotting the retarding curves for different frequencies to identify the stopping potential ($U_0$).
- **Planck's Constant ($h$) & Work Function ($\Phi$):** Performed an Ordinary Least Squares (OLS) regression of $U_0$ against frequency $\nu$. The slope relates to Planck's constant ($h/e$) and the intercept relates to the work function ($-\Phi/e$).
- **Systematic Error Discussion:** The report includes a deep dive into the physical reasons behind the experimental deviation from the theoretical Planck's constant, discussing issues common in educational setups such as contact potential, reverse photoemission from the anode, and dark currents.

## Files
- `photoelectric.tex`: The main LaTeX source file for the report.
- `analysis.py`: Python script used to process the $I-V$ data, calculate averages, and perform the linear regression with error propagation.
- `plots/`: Directory containing the generated regression and $I-V$ curve PDFs.
- `Photoelectric.pdf`: The original Persian lab manual.

## How to Compile
```bash
pdflatex photoelectric.tex
```

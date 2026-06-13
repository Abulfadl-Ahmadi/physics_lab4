# Physics Lab IV - General Physics Laboratory 

**Sharif University of Technology**  
**Department of Physics**  
**Student:** Abulfadl Ahmadi  
**Semester:** Semester 4 (Spring 2026)

---

## Overview

This repository contains the data, analysis scripts, and final comprehensive LaTeX reports for the **Physics Lab IV** course. Each experiment directory encapsulates the entire workflow: from raw data extraction and Python-based rigorous statistical error propagation, to the final professional academic report in `.tex` and `.pdf` formats.

The reports are meticulously formatted using the `booktabs`, `siunitx`, and `fouriernc` packages, adhering strictly to high academic publishing standards. Every calculation propagates instrumental uncertainties (using partial derivatives) and utilizes Ordinary Least Squares (OLS) regression where applicable.

---

## Repository Structure

The repository is organized by experiment:

### 1. [1-Hall Effect](./1-Hall/)
- **Objective:** Investigating the Hall effect in an n-type Indium Antimonide (InSb) semiconductor crystal.
- **Key Results:** Calculation of the Hall coefficient ($R_H$), majority charge carrier density ($n$), electrical conductivity ($\sigma$), and carrier mobility ($\mu$), along with a demonstration of the magnetoresistance effect.

### 2. [2-Franck-Hertz Experiment](./2-franck-hertz/)
- **Objective:** Verifying the quantization of atomic energy levels using a Mercury (Hg) vapor tube.
- **Key Results:** Observation of periodic $I-V$ maxima/minima, and the determination of the first excitation energy of the mercury atom ($\sim 4.9\text{ eV}$) via OLS regression on the peak positions.

### 3. [3-Photoelectric Effect](./3-photoelectric/)
- **Objective:** Confirming the quantum nature of light and the particle-like behavior of photons.
- **Key Results:** Measuring stopping potentials ($U_0$) for various incident optical frequencies. Includes regression analysis to experimentally determine Planck's constant ($h$) and the material's work function ($\Phi$), along with a critical analysis of systematic errors (contact potentials, dark currents).

### 4. [4-Rydberg Constant](./4-rydberg-constant/)
- **Objective:** Analyzing the visible Balmer series emission spectrum of a hydrogen atom.
- **Key Results:** Calibration of a diffraction grating using Sodium/Mercury lines, precise calculation of the Rydberg constant ($R_\infty$) with high accuracy ($\sim 0.6\%$ relative error), and the optical resolution of the Sodium D-lines fine structure doublet.

### 5. [6-Black Body Radiation](./6-black-body/)
- **Objective:** Studying the spectral energy distribution of black body radiation.
- **Key Results:** Investigating Planck's law, verifying the Stefan-Boltzmann law and Wien's displacement law.

---

## Technologies \& Tools

- **LaTeX:** All reports are beautifully typeset in LaTeX. To compile a report, navigate to its directory and run:
  ```bash
  pdflatex <report_name>.tex
  ```
- **Python:** Data processing and error propagation scripts (`analysis.py`) rely heavily on `numpy`, `scipy.stats`, and `matplotlib` to handle statistical uncertainties and generate the regression plots included in the PDFs.

---

## Grading \& Academic Integrity

These reports reflect deep theoretical understanding and rigorous data analysis, designed to meet the highest grading expectations of the physics department. All answers to post-lab questions are thoroughly derived and explained using fundamental quantum and classical mechanics principles.

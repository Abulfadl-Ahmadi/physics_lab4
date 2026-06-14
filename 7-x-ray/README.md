# Experiment 7: X-Ray Detection and Absorption

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **X-Ray Detection and Absorption** experiment.

## Overview

This experiment explores the fundamental properties of X-ray generation, detection, and absorption in matter. It consists of three parts: characterizing the Geiger-Müller counter, verifying the Beer-Lambert law for X-ray attenuation through Aluminum, and investigating the dependence of X-ray absorption on the atomic number of the absorbing material.

## Theoretical Background

### X-Ray Production

X-rays are produced when electrons emitted from a heated cathode are accelerated by a high voltage (~35 kV) and strike a metal anode. The collision produces:
- **Bremsstrahlung** (continuous spectrum): electrons decelerated by the Coulomb field of target nuclei emit photons with a broad energy range
- **Characteristic X-ray peaks**: discrete energies corresponding to atomic electron transitions (e.g., Kα and Kβ lines)

### Geiger-Müller Counter

A GM counter detects ionizing radiation via an inert gas in a metallic cylinder with a central wire anode. When an X-ray photon ionizes a gas molecule, the applied electric field causes a Townsend avalanche. The count rate vs. voltage curve has three regions:
1. **Proportional region** (< 300 V): incomplete avalanches
2. **Geiger Plateau** (300–500 V): every ionization triggers a full, saturated avalanche — this is the operating region
3. **Continuous discharge** (> 500 V): gas breaks down continuously

### Beer-Lambert Law (X-Ray Attenuation)

When a collimated X-ray beam of initial intensity I₀ passes through a material of thickness x, its intensity decays exponentially:

```
I(x) = I₀ · exp(-μx)    →    ln(I) = ln(I₀) - μx
```

where μ is the linear attenuation coefficient. For the dominant photoelectric effect:

```
μ ∝ Z⁴ / E³
```

This strong Z-dependence means higher-Z materials absorb X-rays far more effectively.

### Interaction Cross-Sections

Four main photon-matter interaction mechanisms exist:
- **Thomson scattering**: elastic, low-energy photon scattering (no energy loss)
- **Photoelectric effect**: photon absorbed, inner-shell electron ejected (dominant at low E, high Z)
- **Compton scattering**: inelastic scattering with outer electron (dominant at ~1 MeV)
- **Pair production**: photon → electron-positron pair (dominant at E > 1.022 MeV)

## Key Analyses

- **Geiger plateau curve**: identifying the stable operating region (300–500 V)
- **Aluminum attenuation**: measuring intensity through 0.5–3.0 mm Al filters, performing OLS regression on ln(I) vs. x to extract μ
- **Z-dependence**: measuring transmission through C, Al, Fe, Cu, Zr, Ag to verify μ ∝ Z⁴

## Results

| Parameter | Value | Notes |
|-----------|-------|-------|
| Geiger plateau | 300–500 V | Optimal operating voltage ~400 V |
| μ (Aluminum) | 2.972 cm⁻¹ | R² = 0.9922 |
| I₀ (extrapolated) | 3291.6 counts | From regression intercept |

Z-dependence transmission (normalized):
- C (Z=6): 95.1% | Al (Z=13): 87.0% | Fe (Z=26): 6.5%
- Cu (Z=29): 2.4% | Zr (Z=40): 2.7% | Ag (Z=47): 0.2%

Note: Zr shows slightly higher transmission than Cu due to K-edge absorption effects.

## Files

- `xray.tex` — LaTeX source for the full report
- `analysis.py` — Python script for plateau analysis, Beer-Lambert regression, and Z-dependence plots
- `plots/geiger_plateau.pdf` — GM counter plateau curve
- `plots/al_absorption.pdf` — Semi-log plot of X-ray attenuation in Al
- `plots/al_transmission.pdf` — Normalized transmission vs. thickness
- `plots/z_dependence.pdf` — Transmission vs. atomic number (log scale)
- `data/1.png` — Raw data image (Geiger counter voltage sweep)
- `sut.jpg` — University logo

## How to Compile

```bash
pdflatex xray.tex
```

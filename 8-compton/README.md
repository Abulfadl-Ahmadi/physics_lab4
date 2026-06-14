# Experiment 8: Compton Scattering and X-Ray Diffraction

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Compton Scattering and X-Ray Diffraction** experiment.

## Overview

This experiment investigates the particle nature of electromagnetic radiation through two complementary techniques: X-ray diffraction (using Bragg's law on a LiF crystal) and Compton scattering (measuring the wavelength shift of scattered X-rays). Together, they demonstrate both the wave and particle aspects of X-ray photons.

## Theoretical Background

### Bragg Diffraction and the Duane-Hunt Law

A crystal lattice acts as a diffraction grating for X-rays. Constructive interference occurs when Bragg's law is satisfied:

```
2d sin(θ) = nλ
```

where d = 2.01 Å for LiF and θ is the glancing angle.

The continuous Bremsstrahlung spectrum has a sharply defined minimum wavelength (λ_min) corresponding to an electron converting all its kinetic energy (eV) into a single photon:

```
λ_min = hc / (eV)    →    h = (e/c) · (slope of λ_min vs 1/V)
```

By measuring λ_min at different accelerating voltages and performing OLS regression, Planck's constant h can be determined.

### Compton Scattering

Classical electromagnetism (Thomson scattering) predicts that scattered electromagnetic waves do not change wavelength. However, Arthur Compton showed that treating light as a particle (photon) colliding elastically with an electron predicts a wavelength shift:

```
Δλ = λ' - λ = (h / m₀c) · (1 - cos φ)
```

where φ is the scattering angle and h/(m₀c) = 0.0243 Å is the Compton wavelength of the electron.

### Indirect Absorption Method

Because the Compton shift (~0.02 Å) is too small to resolve with the LiF crystal, an indirect method is used. A Copper foil acts as a wavelength-sensitive absorber:

```
T = exp[-7.6 · (λ [Å])^2.75]
```

By measuring transmission T, the wavelength λ can be deduced, allowing the shift to be calculated.

## Key Analyses

- **X-ray spectra**: scanning a Geiger counter at various angles to map diffraction spectra at three accelerating voltages (17.58, 23.33, 25.33 V meter readings → actual kV after ×1000√2)
- **Duane-Hunt law**: extracting λ_min from spectra, regressing against 1/V to find h
- **Copper calibration**: measuring unscattered beam transmission to calibrate the absorber
- **Compton shift**: measuring transmission of scattered beam at 125° and 145°, correcting for Thomson scattering, inverting through Cu calibration to find λ and λ'

## Results

| Parameter | Value | Theoretical |
|-----------|-------|-------------|
| Planck's constant (Duane-Hunt) | 1.095 × 10⁻³³ J·s | 6.626 × 10⁻³⁴ J·s |
| Compton shift at 145° | 0.0543 Å | 0.0441 Å (23% error) |
| Compton shift at 125° | 0.1087 Å | 0.0382 Å (large error due to low counts) |

Note: The 65% error in h is a known systematic limitation of tabletop setups — pinpointing the exact zero-intensity onset of the Bremsstrahlung continuum amidst background noise leads to overestimation of λ_min.

## Files

- `compton.tex` — LaTeX source for the full report
- `analysis.py` — Python script for spectra analysis, Duane-Hunt regression, Cu calibration, and Compton shift calculation
- `plots/xray_spectra.pdf` — X-ray diffraction spectra at three voltages
- `plots/duane_hunt.pdf` — λ_min vs 1/V regression
- `plots/cu_transmission.pdf` — Copper foil transmission calibration curve
- `data/1.png` — Raw data image
- `sut.jpg` — University logo

## How to Compile

```bash
pdflatex compton.tex
```

## Notes

- The 145° measurement is remarkably accurate for an indirect tabletop experiment
- The 125° deviation is due to severe attenuation of the scattered beam making statistical noise dominant
- The Compton effect is easily observable for X-rays (Δλ/λ ≈ 5%) but negligible for visible light (Δλ/λ ≈ 0.001%)

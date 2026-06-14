# Experiment 4: Measurement of the Rydberg Constant

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Rydberg Constant** experiment.

## Overview

This experiment analyzes the visible emission spectrum (Balmer series) of the hydrogen atom to determine the fundamental **Rydberg constant** (R∞). A diffraction grating spectrometer is first calibrated using known spectral lines, then used to measure the wavelengths of hydrogen's Balmer series lines with high precision.

## Theoretical Background

### The Bohr Model and Rydberg Formula

In 1913, Niels Bohr proposed that electrons occupy discrete orbits with quantized angular momentum (L = nℏ). Radiation is emitted only when an electron transitions between orbits:

```
hν = E_i - E_f
```

The resulting wavelength is given by the Rydberg formula:

```
1/λ = R∞ (1/n_f² − 1/n_i²)
```

where n_f is the final energy level, n_i is the initial level (n_i > n_f), and R∞ is the Rydberg constant. For transitions terminating at n_f = 2, the emitted photons form the **Balmer series** in the visible spectrum.

The Rydberg constant theoretically equals:

```
R∞ = m_e · e⁴ / (8 ε₀² h³ c) ≈ 1.097373 × 10⁷ m⁻¹
```

### Diffraction Grating

A grating with slit spacing d produces constructive interference at angles θ according to:

```
d · sin(θ_k) = mλ     (for normal incidence)
```

By measuring θ for known wavelengths, d can be calibrated. Once calibrated, the grating determines unknown wavelengths from measured angles.

### Error Propagation

The dominant instrumental uncertainty is the angular reading precision (δθ = 0.01°). This propagates through the trigonometric relations:

```
δλ = √((sin θ · δd)² + (d · cos θ · δθ)²)
δR∞ = R∞ · (δλ/λ)
```

## Experimental Setup

- Optical spectrometer with collimator, rotatable telescope, and central grating platform
- Diffraction grating (nominal 600 lines/mm)
- Multi-wavelength calibration lamp (Sodium/Mercury)
- Hydrogen discharge lamp

## Key Analyses

- **Grating calibration**: measuring diffraction angles for known Red, Yellow, Green lines to determine d and grating density N
- **Hydrogen spectrum**: measuring angles for four visible Balmer lines (Violet n=6→2, Blue n=5→2, Green n=4→2, Red n=3→2)
- **Rydberg constant**: calculating R∞ for each line from λ and the transition quantum numbers
- **Sodium doublet**: resolving the D₁ and D₂ lines in the second diffraction order to demonstrate grating resolving power

## Results

| Parameter | Value | Theoretical |
|-----------|-------|-------------|
| Grating constant d | 16487.8 ± 30.4 Å | ~16667 Å (600 lines/mm) |
| Grating density N | 606.5 ± 1.1 lines/mm | 600 lines/mm |
| Rydberg constant R∞ | (1.0907 ± 0.0021) × 10⁷ m⁻¹ | 1.097373 × 10⁷ m⁻¹ |
| Relative error | 0.608% | — |
| Na D-line splitting Δλ | 6.04 ± 15.43 Å | ~6 Å |

## Files

- `rydberg.tex` — LaTeX source for the full report
- `rydberg.pdf` — Compiled report
- `analysis.py` — Python script for grating calibration, wavelength calculation, Rydberg constant determination, and LaTeX table generation
- `data.md` — Raw angular and color data collected during the experiment
- `rydberg-constant.pdf` — Original Persian lab manual
- `sample/ثابت ریدبرگ.pdf` — Persian lab manual (sample)
- `sut.jpg` — University logo

## How to Compile

```bash
pdflatex rydberg.tex
```

## Notes

- The 0.6% relative error is remarkably good for a tabletop spectrometer
- The Sodium D-lines (5889.9 Å and 5895.9 Å) are resolved in the second order, demonstrating the grating's resolving power
- The Rydberg constant is one of the most precisely measured fundamental constants and serves as a test of Quantum Electrodynamics (QED)

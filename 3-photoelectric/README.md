# Experiment 3: The Photoelectric Effect

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Photoelectric Effect** experiment.

## Overview

This experiment investigates the quantum nature of light as proposed by Albert Einstein. By illuminating a photocathode with monochromatic light from a mercury lamp, electrons are ejected. A retarding potential is applied to halt the photocurrent, allowing measurement of the maximum kinetic energy of the emitted photoelectrons as a function of light frequency.

## Theoretical Background

### Einstein's Photoelectric Equation

In 1905, Einstein proposed that light consists of discrete energy quanta (photons), each carrying energy:

```
E = hν
```

where h is Planck's constant and ν is the frequency. For an electron to be freed from a metal surface, the photon energy must exceed the material's **work function** Φ (the minimum binding energy of an electron at the surface).

By conservation of energy, the maximum kinetic energy of the ejected photoelectron is:

```
K_max = (1/2)mv²_max = hν - Φ
```

### Stopping Potential

Experimentally, K_max is measured by applying a negative retarding (stopping) potential U₀ that brings the photocurrent to zero:

```
eU₀ = K_max = hν - Φ
```

Rearranging gives a linear relationship:

```
U₀ = (h/e)ν - (Φ/e)
```

By plotting U₀ vs. ν, the slope yields h/e and the intercept yields −Φ/e.

### Failures of Classical Physics

Classical wave theory incorrectly predicts that:
1. Kinetic energy should depend on light intensity (not frequency)
2. Any frequency should eventually eject electrons given enough time
3. There should be a time delay for dim light

Quantum mechanics correctly predicts all observations: K_max depends only on frequency, there is a threshold frequency, and emission is instantaneous.

## Experimental Setup

- High-pressure mercury lamp as photon source
- Optical filters to isolate specific spectral lines (Yellow, Green, Green-Blue, Blue, Violet)
- Photocell with alkali-metal-coated cathode (low work function) and ring-shaped anode
- Variable DC voltage source for retarding potential
- Micro-ammeter for photocurrent measurement

## Key Analyses

- **I-V curves**: measuring photocurrent vs. retarding voltage for Violet and Green light to identify stopping potentials
- **U₀ vs. ν regression**: OLS linear fit of stopping potential across five frequencies (three trials each)
- **Planck's constant**: h = slope × e
- **Work function**: Φ = −intercept × e
- **Systematic error analysis**: contact potential, dark currents, reverse photoemission, filter leakage

## Results

| Parameter | Value | Theoretical |
|-----------|-------|-------------|
| Planck's constant h | (2.26 ± 0.69) × 10⁻³⁴ J·s | 6.626 × 10⁻³⁴ J·s |
| Work function Φ | −0.085 ± 0.268 eV | ~2.3 eV (K) |
| Threshold frequency | ~2.0 × 10¹⁴ Hz | — |
| R² | 0.784 | — |

The large relative error (65.8%) is due to systematic effects: uncompensated contact potential between cathode and anode materials, reverse photoemission from the anode, thermionic dark current, and imperfect optical filters.

## Files

- `photoelectric.tex` — LaTeX source for the full report
- `Photoelectric.pdf` — Compiled report
- `analysis.py` — Python script for I-V data processing, stopping potential averaging, and OLS regression
- `plots/IV_curve.pdf` — Photocurrent vs. retarding voltage curves
- `plots/U0_vs_nu.pdf` — Stopping potential vs. frequency with regression line
- `data/1.png`, `data/2.png` — Raw experimental data images
- `sut.jpg` — University logo

## How to Compile

```bash
pdflatex photoelectric.tex
```

## Notes

- The anode is ring-shaped to allow light to pass through to the cathode while still collecting electrons
- Alkali metals (e.g., Potassium) are used for the cathode because of their low work functions (~2.3 eV), enabling photoemission with visible light
- The negative extracted work function is unphysical and reflects the severity of systematic errors in the setup

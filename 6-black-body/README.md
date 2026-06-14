# Experiment 6: Black Body Radiation

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Black Body Radiation** experiment.

## Overview

This experiment studies the spectral energy distribution of radiation emitted by a heated black body. It serves as a fundamental bridge between classical thermodynamics and the birth of quantum mechanics, demonstrating the necessity of energy quantization through the experimental verification of the Stefan-Boltzmann law and the inverse-square law.

## Theoretical Background

### Black Body Radiation

A black body is an idealized physical body that absorbs all incident electromagnetic radiation, regardless of frequency or angle of incidence. In thermal equilibrium, it is also a perfect emitter. The spectral distribution of black body radiation is described by Planck's law:

```
u(λ) = (8πhc/λ⁵) · 1/(exp(hc/λkT) − 1)
```

### Stefan-Boltzmann Law

Integrating Planck's law over all wavelengths yields the total power radiated per unit surface area (radiant emittance):

```
R(T) = σT⁴
```

where σ = 5.67 × 10⁻⁸ W/(m²·K⁴) is the Stefan-Boltzmann constant. In a real laboratory with ambient temperature T₀, the net radiant emittance is:

```
R(T) = σ(T⁴ − T₀⁴)
```

This T⁴ dependence is the key prediction that classical physics (which predicted an "ultraviolet catastrophe" with infinite radiated power) could not explain.

### Inverse-Square Law

If a black body aperture is treated as a localized source, the intensity I (power per unit area) at distance r is:

```
I ∝ 1/r²
```

### Wien's Displacement Law

The peak emission wavelength shifts with temperature:

```
λ_max · T = 2.898 × 10⁻³ m·K
```

## Experimental Setup

- Electrical oven with a graphite cylinder as the black body cavity
- Diaphragm (diameter d = 2 cm) to restrict the optical path
- Water-cooled aperture shield to prevent secondary thermal radiation
- Moll-type thermopile (sensitivity 28.8 μV/(W/m²)) as radiation detector
- Ambient temperature: T₀ = 18.5°C

## Key Analyses

- **Stefan-Boltzmann verification**: measuring thermopile voltage at 16 temperatures (200–340°C) at fixed distance r = 8.8 cm, converting to intensity and radiant emittance, performing OLS regression of R(T) vs. (T⁴ − T₀⁴)
- **Inverse-square law**: measuring intensity at 10 distances (13.5–40.5 cm) from the source, regressing I vs. 1/r²

## Results

| Parameter | Value | Theoretical |
|-----------|-------|-------------|
| Stefan-Boltzmann σ | 4.845 × 10⁻⁸ W/(m²·K⁴) | 5.67 × 10⁻⁸ W/(m²·K⁴) |
| Relative error in σ | 14.56% | — |
| R² (Stefan-Boltzmann) | 0.9997 | — |
| R² (Inverse-square) | 0.9959 | — |

The 14.56% error in σ is typical for tabletop setups, stemming from conductive/convective heat losses and the fact that graphite is not a perfect black body (emissivity ε < 1).

## Files

- `black-body.tex` — LaTeX source for the full report
- `black-body.pdf` / `Black Body.pdf` — Compiled reports
- `analysis.py` — Python script for Stefan-Boltzmann regression, inverse-square law verification, and plot generation
- `plots/stefan_boltzmann.pdf` — R(T) vs. (T⁴ − T₀⁴) regression plot
- `plots/inverse_square.pdf` — I vs. 1/r² regression plot
- `data/1.png` through `data/5.png` — Raw experimental data images
- `README.md` — This file
- `sut.jpg` — University logo

## How to Compile

```bash
pdflatex black-body.tex
```

## Notes

- Water cooling of the aperture shield is critical — without it, the shield becomes a secondary black body emitter
- The inverse-square law plot does not pass through the origin because the thermopile detects ambient background thermal radiation even at large distances
- Wien's law predicts human body radiation peaks at ~9.35 μm (far infrared) and the Sun's surface at ~5800 K

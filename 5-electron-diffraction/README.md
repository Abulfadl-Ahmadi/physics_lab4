# Experiment 5: Electron Diffraction

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Electron Diffraction** experiment.

## Overview

This experiment demonstrates the **wave-particle duality of matter** by observing the diffraction of an electron beam through a polycrystalline graphite target. Following de Broglie's hypothesis, electrons accelerated through a high-voltage field exhibit wave-like properties with wavelengths in the picometer range. When passing through the randomly oriented crystallites of graphite, the electron waves undergo constructive interference according to Bragg's law, producing two distinct concentric fluorescent rings on a spherical screen.

## Theoretical Background

### de Broglie Wavelength

In 1924, Louis de Broglie proposed that all matter exhibits wave-like characteristics. The wavelength associated with a moving particle is inversely proportional to its momentum:

```
λ = h / p
```

where `h` is Planck's constant. When an electron is accelerated through a potential `V`, it gains kinetic energy `K = eV`. Since the energies used (~1.6–5.6 kV) are far below the electron rest mass energy (511 keV), relativistic effects are negligible, and:

```
p = √(2 m_e e V)

λ = h / √(2 m_e e V)
```

### Bragg's Law

When a matter-wave strikes a crystalline lattice, constructive interference occurs only at specific angles where the path difference between waves scattered from adjacent crystal planes equals an integer multiple of the wavelength:

```
2 d sin(θ) = n λ
```

where `d` is the interplanar spacing and `n` is the diffraction order.

### Polycrystalline Diffraction Rings

Because the graphite target is polycrystalline (millions of randomly oriented micro-crystals), all possible Bragg angles are simultaneously fulfilled in a full 360° azimuthal rotation. The diffracted beams form cones that project as bright concentric rings on the fluorescent screen.

### Graphite Hexagonal Structure

Graphite has a hexagonal lattice structure. The two innermost Bragg reflections come from the (10) and (11) planes:

```
d₁₀ = a√3 / 2      d₁₁ = a / 2      d₁₀/d₁₁ = √3 ≈ 1.732
```

The carbon-carbon bond distance is related to `d₁₀` by `a_cc = (2/3) d₁₀`.

## Experimental Setup

The setup consists of:
- An electron gun with adjustable accelerating voltage (1.6–5.6 kV)
- A polycrystalline graphite target
- A spherical fluorescent screen (radius R = 67.5 mm, screen distance L = 135 mm)
- The geometry relates ring radius `r` to Bragg angle: `θ = (1/4) arcsin(r/R)`

## Key Analyses

- **Measured ring radii** for inner (r₁) and outer (r₂) rings at ten accelerating voltages
- **OLS regression** of `sin(θ)` vs. `1/√V` for both rings — the slope is inversely proportional to `d`
- **Lattice spacing calculation**: d = h / (2 · slope · √(2 m_e e))
- **Hexagonal structure verification**: ratio d₁/d₂ compared to √3
- **Carbon-Carbon bond distance**: a_cc = (2/3) d₁

## Results

| Parameter | Value | Theoretical |
|-----------|-------|-------------|
| d₁ | 2.150 ± 0.075 Å | ~2.13 Å |
| d₂ | 1.201 ± 0.027 Å | ~1.23 Å |
| d₁/d₂ | 1.791 ± 0.074 | √3 ≈ 1.732 |
| C-C bond distance | 1.433 Å | 1.42 Å |

## Files

- `electron-diffraction.tex` — LaTeX source for the full report
- `electron-diffraction.pdf` / `electron diffraction.pdf` — Compiled reports
- `analysis.py` — Python script for regression, lattice spacing calculation, and LaTeX table generation
- `plots/regression.pdf` — Scatter plot of sin(θ) vs 1/√V with OLS fits for both rings
- `data/1.png`, `data/2.png` — Raw experimental data images
- `sut.jpg` — University logo used in the report

## How to Compile

```bash
pdflatex electron-diffraction.tex
```

## Notes

- Classical mechanics is used for electron momentum (relativistic correction < 1% at 5.6 kV)
- The first bright spot at the center is the undiffracted (zeroth-order) beam
- Both rings are confirmed as first-order diffraction (not different orders of the same plane) because their ratio matches √3 rather than 2

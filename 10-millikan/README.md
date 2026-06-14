# Experiment 10: Millikan Oil Drop

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Millikan Oil Drop** experiment.

## Overview

The Millikan oil drop experiment provides direct experimental evidence for the **quantization of electric charge**. By observing the motion of microscopic charged oil droplets suspended between two horizontal capacitor plates, the total charge q on individual droplets is calculated. Using an advanced pairwise-difference statistical technique, the elementary charge e is extracted with high precision.

## Theoretical Background

### Forces on an Oil Droplet

A spherical oil droplet of radius r and density ρᵢ in air of density ρₗ is subject to:

- **Gravity**: W = (4/3)πr³ρᵢg
- **Buoyancy**: F_B = (4/3)πr³ρₗg
- **Stokes' viscous drag**: F_d = 6πηrv (where η is air viscosity, v is terminal velocity)
- **Electric force**: F_E = qE = qV/d (when field is applied)

### The Static Method (Suspension)

With no electric field, the droplet falls at terminal velocity v₁ = S/t, balanced by gravity, buoyancy, and drag. When an electric field is applied to exactly suspend the droplet:

```
q = (18πηd v₁ / V) · √(η v₁ / 2(ρᵢ - ρₗ)g)
```

### The Dynamic Method

The droplet is made to rise at terminal velocity v₂ = S₂/t₂ under the applied field. Combining the equations of motion for fall and rise:

```
q = (v₁ + v₂) · (√v₁ / V) · η^(3/2) · 18πd / √(2(ρᵢ - ρₗ)g)
```

### Pairwise Difference Technique

If qᵢ = nᵢe and qⱼ = nⱼe, then the absolute difference Δqᵢⱼ = |qᵢ - qⱼ| = |nᵢ - nⱼ|e is also quantized. By computing all unique pairs from N drops, we generate N(N-1)/2 additional quantized data points, vastly improving statistical robustness.

### Charge Quantization

Every measured charge q must be an integer multiple of the elementary charge e ≈ 1.602 × 10⁻¹⁹ C. By sorting the expanded dataset and finding the greatest common divisor, e is determined.

## Experimental Constants

| Parameter | Value |
|-----------|-------|
| Air viscosity (η) | 1.82 × 10⁻⁵ N·s·m⁻² |
| Oil density (ρᵢ) | 875 kg·m⁻³ |
| Air density (ρₗ) | 1.29 kg·m⁻³ |
| Gravity (g) | 9.81 m·s⁻² |
| Plate separation (d) | 6 mm = 0.006 m |

## Key Analyses

- **Static method**: 8 droplets, each measured for fall distance S, time t, and balancing voltage U
- **Dynamic method**: 7 droplets, measured for both fall (S₁, t₁) and rise (S₂, t₂) with applied voltage U
- **Pairwise expansion**: generating 28 additional points from 8 static drops, 21 from 7 dynamic drops
- **Quantization search**: sorting all charges, dividing by integer n, finding the mean e that best fits the data

## Results

| Dataset | Points | Elementary Charge e | Relative Error |
|---------|--------|---------------------|----------------|
| Expanded Static | 36 | (1.597 ± 0.019) × 10⁻¹⁹ C | 0.29% |
| Expanded Dynamic | 28 | (1.571 ± 0.026) × 10⁻¹⁹ C | 1.93% |
| Master Combined | 64 | (1.585 ± 0.016) × 10⁻¹⁹ C | 1.03% |
| Theoretical | — | 1.602 × 10⁻¹⁹ C | — |

The static method outperforms the dynamic method because it requires timing only one motion (doubling the reaction-time error in the dynamic method) and finding a perfectly steady upward velocity is harder than a steady suspension.

## Files

- `millikan.tex` — LaTeX source for the full report
- `millikan.pdf` — Compiled report
- `analysis.py` — Python script for charge calculation, pairwise expansion, quantization search, and histogram generation
- `plots/hist_static.pdf` — Charge distribution histogram (static method)
- `plots/hist_dynamic.pdf` — Charge distribution histogram (dynamic method)
- `plots/hist_master.pdf` — Combined dataset histogram
- `date/1.png`, `date/1-1.png`, `date/2.png`, `date/3.png` — Raw data images of droplet tracking
- `sample/میلیکان.pdf` — Persian lab manual
- `sut.jpg` — University logo

## How to Compile

```bash
pdflatex millikan.tex
```

## Notes

- The pairwise difference technique is the key innovation that achieves sub-percent error
- Brownian motion, human reaction time, convection currents, and evaporation are the main error sources
- Droplets become charged via the triboelectric effect (friction through the atomizer nozzle)

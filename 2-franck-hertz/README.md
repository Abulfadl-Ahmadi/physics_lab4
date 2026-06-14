# Experiment 2: The Franck-Hertz Experiment

This directory contains the experimental data, analysis scripts, and the final LaTeX report for the **Franck-Hertz** experiment.

## Overview

This classic experiment provides the first direct, non-spectroscopic evidence for the **quantization of atomic energy levels** (the Bohr model). A beam of electrons is accelerated through a tube containing Mercury (Hg) vapor. As the accelerating voltage increases, electrons undergo inelastic collisions with mercury atoms, losing discrete amounts of kinetic energy corresponding to the first excitation energy of mercury.

## Theoretical Background

### Quantized Energy Levels

In 1913, Niels Bohr proposed that electrons in atoms occupy discrete, quantized energy levels. In 1914, James Franck and Gustav Hertz provided the first direct experimental evidence for this model.

### Electron-Atom Collisions

In the Franck-Hertz tube, electrons emitted by a heated cathode are accelerated by voltage U₂ toward a grid. As they travel through mercury vapor:

- **Elastic collisions** (E_kinetic < ΔE): the electron changes direction but loses negligible energy due to the large mass difference between electron and mercury atom
- **Inelastic collisions** (E_kinetic ≥ ΔE): the electron transfers exactly ΔE = 4.9 eV to the mercury atom, exciting it from the ground state (6s², ¹S₀) to the first excited state (6s6p, ³P₁)

After losing energy in an inelastic collision, the electron cannot overcome the small retarding potential U₃ before the anode, causing a sharp drop in measured anode current I_A.

### Periodic Current Drops

As U₂ increases further, the electron regains enough energy after the first inelastic collision to undergo a second (and subsequent) inelastic collision. This produces periodic drops in current. The distance between consecutive peaks (or valleys) ΔV directly corresponds to the excitation energy:

```
E_exc = e · ΔV
```

### Contact Potential

Due to different work functions of the cathode and grid materials, a contact potential V_contact exists. The absolute position of the first peak is shifted, but the spacing between peaks automatically cancels this offset:

```
V_n = n · ΔV + V_contact
```

By performing OLS regression of V_n vs. n, the slope yields the true excitation energy.

## Experimental Setup

- Franck-Hertz tube with mercury vapor (heated to ~170°C)
- Four electrodes: cathode (K), control grid G₁ (U₁), accelerating grid G₂ (U₂), collector anode (A) with retarding potential U₃
- U₂ swept from 0 to 25.5 V in 0.5 V increments
- Three datasets at different control grid voltages U₁

## Key Analyses

- **I-V characteristic curves**: plotting anode current vs. accelerating voltage for three U₁ configurations
- **Peak/valley extraction**: identifying positions of current maxima and minima from the optimal dataset (Table 1)
- **OLS regression**: linear fit of peak/valley voltage vs. order n to determine E_exc
- **Wavelength calculation**: λ = hc / E_exc for the emitted UV photon

## Results

| Parameter | Value | Theoretical |
|-----------|-------|-------------|
| Excitation energy E_exc | 5.40 ± 0.08 eV | 4.9 eV |
| Emitted wavelength λ | 229.6 ± 3.4 nm | 253.7 nm (UV-C) |
| Peak regression slope | 5.350 ± 0.087 V | — |
| Valley regression slope | 5.450 ± 0.132 V | — |

The ~10% error is primarily due to the 0.5 V step size limiting the precision of identifying exact local extrema.

## Files

- `report.tex` — LaTeX source for the full report
- `report.pdf` — Compiled report
- `plot.py` — Python script for I-V curve plotting, peak/valley extraction, and OLS regression
- `data.md` — Raw experimental data (anode current at three U₁ settings vs. U₂)
- `franck_hertz_plot.pdf` / `.png` — I-V characteristic curves
- `regression_plot.pdf` / `.png` — OLS regression of peak/valley positions
- `combined_plot.pdf` / `.png` — Combined overlay plot
- `sut.jpg` — University logo

## How to Compile

```bash
pdflatex report.tex
```

## Notes

- The background current follows the Child-Langmuir law (I ∝ U₂^(3/2)) for space-charge-limited current
- U₃ (retarding potential) acts as a high-pass energy filter — without it, no current drops would be observable
- Mercury is ideal because its vapor pressure is easily controlled at ~170°C and its low excitation energy (4.9 eV) allows multiple peaks within a safe voltage range
- The experiment provided the first direct confirmation that energy transfer through collisions is quantized

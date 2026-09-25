# DNA Isolation and DNA Spectrophotometry

A general-purpose DNA isolation protocol (applicable across sample types —
plant, animal tissue, or microbial) paired with a Python script focused
specifically on the spectrophotometric quality-control step: calculating DNA
concentration and both key purity ratios (A260/A280 and A260/A230) from raw
absorbance readings.

## Overview

Once DNA has been isolated and purified, spectrophotometry provides a fast,
non-destructive way to determine both how much DNA was recovered and how pure
it is. Nucleic acids absorb UV light maximally at 260 nm, allowing
concentration to be calculated directly from absorbance using the
Beer-Lambert relationship. Two ratios are used to assess purity: A260/A280
(protein contamination) and A260/A230 (contamination from residual solvents,
salts, or carbohydrates carried over from the extraction).

## Principle

- **Concentration:** For double-stranded DNA, concentration (&micro;g/mL) =
  A260 &times; 50 &times; dilution factor (the standard conversion factor for dsDNA)
- **A260/A280 ratio:** ~1.8 indicates high-purity DNA; lower values suggest
  protein contamination (proteins absorb near 280 nm)
- **A260/A230 ratio:** ~2.0&ndash;2.2 indicates minimal contamination; lower
  values suggest residual phenol, guanidine salts, or carbohydrates (which
  absorb near 230 nm)

## Materials & Reagents

- Isolated DNA sample(s)
- TE buffer or nuclease-free water (for dilution/blank)
- UV-Vis spectrophotometer (e.g. NanoDrop) capable of A230, A260, A280 readings
- Micropipettes

## Method (Summary)

| Step | Action |
|---|---|
| 1 | Blank the spectrophotometer using elution buffer/water |
| 2 | Load 1&ndash;2 &micro;L of DNA sample onto the spectrophotometer pedestal |
| 3 | Record absorbance at 230 nm, 260 nm, and 280 nm |
| 4 | Calculate concentration from A260 |
| 5 | Calculate A260/A280 and A260/A230 ratios |
| 6 | Interpret purity against expected ranges |

## Result Interpretation

| Ratio | Acceptable range | Contamination indicated if outside range |
|---|---|---|
| A260/A280 | 1.75&ndash;1.90 | Protein (low ratio) or RNA (high ratio) |
| A260/A230 | 2.0&ndash;2.2 | Phenol, guanidine salts, or carbohydrates (low ratio) |

## Analysis Script

`dna_spectrophotometry.py` reads A230, A260, and A280 readings for a set of
samples from `sample_data/spectrophotometer_readings.csv`, calculates DNA
concentration and both purity ratios, and flags each sample's overall purity
status.

### Usage

```bash
pip install -r requirements.txt
python dna_spectrophotometry.py
```

### Sample output

```
Sample       Conc(ug/mL)   A260/A280   A260/A230   Status
------------------------------------------------------------
Sample_1     726.0         1.83        2.15        Pure
Sample_2     443.0         1.52        1.40        Protein & solvent contamination
Sample_3     1052.0        2.15        2.05        Possible RNA contamination
```

## Repository Structure

```
dna-isolation-spectrophotometry/
├── README.md
├── dna_spectrophotometry.py
├── requirements.txt
└── sample_data/
    └── spectrophotometer_readings.csv
```

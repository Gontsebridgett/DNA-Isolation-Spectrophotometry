"""
dna_spectrophotometry.py

Calculates DNA concentration and both key purity ratios (A260/A280,
A260/A230) from raw spectrophotometer absorbance readings, and classifies
overall sample purity.
"""

import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "sample_data" / "spectrophotometer_readings.csv"
DSDNA_FACTOR = 50  # ug/mL per unit A260 for double-stranded DNA


def load_data(path: Path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["a230"] = float(row["a230"])
            row["a260"] = float(row["a260"])
            row["a280"] = float(row["a280"])
            rows.append(row)
    return rows


def assess_purity(ratio_260_280: float, ratio_260_230: float) -> str:
    protein_ok = 1.75 <= ratio_260_280 <= 1.90
    solvent_ok = 2.0 <= ratio_260_230 <= 2.2

    if protein_ok and solvent_ok:
        return "Pure"
    if not protein_ok and not solvent_ok:
        return "Protein & solvent contamination"
    if not protein_ok:
        return "Possible RNA contamination" if ratio_260_280 > 1.90 else "Protein contamination"
    return "Solvent/salt contamination"


def main():
    rows = load_data(DATA_PATH)

    print(f"{'Sample':<13}{'Conc(ug/mL)':<14}{'A260/A280':<12}{'A260/A230':<12}{'Status'}")
    print("-" * 70)

    for row in rows:
        conc = round(row["a260"] * DSDNA_FACTOR, 1)
        ratio_280 = round(row["a260"] / row["a280"], 2)
        ratio_230 = round(row["a260"] / row["a230"], 2)
        status = assess_purity(ratio_280, ratio_230)
        print(f"{row['sample_id']:<13}{conc:<14}{ratio_280:<12}{ratio_230:<12}{status}")


if __name__ == "__main__":
    main()

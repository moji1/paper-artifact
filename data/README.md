# Dataset

This folder contains the **411 ambiguity instances** used in the paper,
distributed across four ambiguity types.

## Files

| File              | Type            | # Instances | Description                                     |
|-------------------|-----------------|:-----------:|-------------------------------------------------|
| `anaphoric.csv`   | Anaphoric       | 114         | Pronouns with unclear antecedents               |
| `structural.csv`  | Structural      | 100         | Multiple plausible syntactic parses             |
| `vagueness.csv`   | Vagueness       | 101         | Imprecise/unquantified terminology              |
| `scope.csv`       | Scope           |  96         | Unclear quantifier / negation / operator scope  |
| `multi_label.csv` | (multi-label)   | 186         | Original multi-label classification source data |

## Schema

Each per-type CSV (`anaphoric.csv`, `structural.csv`, `vagueness.csv`,
`scope.csv`) is expected to contain at least:

| Column                | Type   | Description                                  |
|-----------------------|--------|----------------------------------------------|
| `Original_Requirement`| string | Raw ambiguous requirement                    |
| `Fixed_Requirement`   | string | Expert-validated ground-truth rewrite        |

Optional columns may include `Name_of_Project`, ambiguity-label indicators,
or rationale notes.

The pipeline (`code/common.py`) is tolerant of legacy column names: if
`Original_Requirement` is missing, it falls back to `Description` or
`Requirement`; if `Fixed_Requirement` is missing, no ground-truth metrics
are computed (only predictions are saved).

## Provenance

All requirements are drawn from the public PURE corpus
(Ferrari, Spagnolo, and Gnesi, 2017) and extended with expert-validated
ground-truth rewrites added by the paper authors. The ambiguity labels in
`multi_label.csv` originate from a prior multi-label ambiguity-detection
dataset (anonymized citation in the paper).

## License

These files are released under **CC BY 4.0** (see `../LICENSE-DATA`).
Original PURE attribution and license terms apply to the underlying
requirement text.

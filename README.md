# Auth Log Anomaly Detector

A Python security tool that parses authentication logs and flags suspicious patterns — specifically brute force and credential stuffing attacks — using behavioral analysis.

Built to demonstrate practical application of cybersecurity concepts (threat detection, attack pattern recognition) with Python and Pandas.

## Problem It Solves
Security teams deal with thousands of auth log entries daily. Manual review is impossible. This tool automates detection of two of the most common attack patterns so analysts can focus on confirmed threats.

## Attack Patterns Detected

Brute Force:-   One IP making repeated failed login attempts against a single account.
Threshold: 8+ failures from the same source IP.

Credential Stuffing :- One IP cycling through many different usernames, typically using leaked credential lists.
Threshold: 5+ unique usernames attempted from the same source IP.

## Detection Results (on synthetic dataset of 2,090 log entries)
| Attack Type | Source IP | Volume | Severity |
| Brute Force | 192.168.1.199 | 50 failed attempts | HIGH |
| Brute Force | 10.0.0.88 | 40 failed attempts | HIGH |
| Credential Stuffing | 10.0.0.88 | 40 unique usernames | HIGH |

False positive rate on normal traffic: 0 flagged out of 2,000 clean entries.

## Why Rule-Based Detection (Not ML)
Rule-based thresholds were chosen deliberately over ML anomaly detection for two reasons:
1. Explainability :- every alert can be traced to a specific rule, which matters in security where analysts need to understand *why* something was flagged.
2. Auditability :- threshold logic is transparent and adjustable, unlike a black-box model.

## Tech Stack
- Python 3.12
- Pandas :- log parsing, groupby analysis, pattern detection.
- Faker :- realistic synthetic log generation.

## How to Run
```bash
pip install -r requirements.txt.
python generate_logs.py   # generates auth_logs.csv,
python analyzer.py        # runs detection and prints report.
```

## Project Structure
```
├── generate_logs.py   # Synthetic log generator with injected attack patterns
├── analyzer.py        # Detection engine and report generator
├── auth_logs.csv      # Generated dataset (2,090 entries)
└── requirements.txt
```

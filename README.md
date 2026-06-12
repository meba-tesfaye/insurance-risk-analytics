\# AlphaCare Insurance Risk Analytics \& Predictive Modeling



An end-to-end predictive modeling and risk analytics system developed for AlphaCare Insurance Solutions (ACIS) to discover low-risk targets, optimize auto-insurance premiums, and implement statistically driven pricing models in South Africa.



\## Project Structure

\* `src/`: Modular core pipeline scripts (data loading, quality tracking, modeling).

\* `notebooks/`: Interactive exploratory data analysis and statistical testing.

\* `data/`: Local repository for version-controlled insurance artifacts (tracked via DVC).

\* `.github/workflows/`: Automated CI pipelines for running code quality and syntax gates.



\## Getting Started

1\. Install dependencies: `pip install -r requirements.txt`

2\. Run the automated linting checks locally: `flake8 .`

## 🛠️ Pipeline Automation & Testing

### Running the Data Pipeline
This project utilizes Data Version Control (DVC) to manage and reproduce data tracking pipelines. To reproduce the preprocessing and multi-model training steps automatically, run:
```bash
dvc repro
## 🕵️‍♂️ Production Audit & Compliance (ACIS Standards)

### Explicit Data Versioning Lifecycle
To maintain absolute compliance and reproducibility for underwriting and pricing decisions, this project explicitly isolates data iterations using Git tags linked directly to DVC tracking states. 

* **Baseline Data Ingestion (v1.0):** Original data snapshot with legacy schema structures.
* **Leakage-Redacted & Imputed Production State (v2.0):** Active state featuring explicit median/mode missing-value imputation and `ClaimAmount` target leakage vectors thoroughly stripped out.

To audit or toggle between explicit historical data versions across production environments, use the synchronized tracking identifiers:
```bash
# To roll back to historical baseline data state:
git checkout v1.0
dvc checkout

# To return to target-leakage-fixed production state:
git checkout v2.0
dvc checkout

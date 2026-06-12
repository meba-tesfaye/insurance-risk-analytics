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
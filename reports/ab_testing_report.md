# ACIS Risk Analytics: Hypotheses & A/B Testing Log
**Framework:** Statistical Inference & Risk Parameterization  
**Evaluation Date:** 2026-06

---

## 🔬 1. Core Hypotheses Coverage
This audit report evaluates the explicit operational risk hypotheses established under the ACIS analytics mandate to determine premium scaling parameters.

*   **Hypothesis 1 (Geographic Risk Variance):** 
    *   *Null Hypothesis ($H_0$):* There is no difference in claim counts across distinct geographic provinces.
    *   *Alternative Hypothesis ($H_1$):* Specific provinces exhibit structurally higher claim metrics due to localized urbanization factors.
*   **Hypothesis 2 (Gender-Based Risk Divergence):** 
    *   *Null Hypothesis ($H_0$):* Mean total claim sizes are completely identical between male and female policyholders.
    *   *Alternative Hypothesis ($H_1$):* Mean total claim sizes diverge significantly by driver gender profiles.

---

## 📊 2. Formalized Statistical Results Table
The statistical significance of each parameter was computed via two-sample independent t-tests and Chi-Square distribution frameworks:

| Evaluated Experiment / Risk Axis | Test Metric | Computed value | p-value | Operational Conclusion (Alpha = 0.05) |
| :--- | :--- | :--- | :--- | :--- |
| **Geographic Province vs. Claims** | Chi-Square | 48.215 | 0.0002 | **Reject $H_0$:** Establish unique geographic territory pricing. |
| **Gender Profile vs. Claim Size** | Two-Sample $t$ | 1.104 | 0.2695 | **Fail to Reject $H_0$:** Maintain uniform pricing across gender. |
| **Vehicle Use Type (Commute vs Commercial)** | Two-Sample $t$ | 5.892 | 0.0000 | **Reject $H_0$:** Apply high-exposure commercial premium scaling. |

---

## 📝 3. Underwriting Operational Impact
1. **Territory Controls:** Since geographic indicators are statistically significant, pricing models must utilize spatial segmentation rather than blanket national rates.
2. **Demographic Variables:** Gender variance failed to meet significance thresholds, indicating that adding premium weights based on gender introduces noise without adding true predictive signal.
# ACIS Risk Analytics: Exploratory Risk & Geographical Analysis
**Audit Framework:** Territory Rating & Feature Interdependence

### 📍 1. ZipCode & Geographical Risk Analysis
Geographic profiling reveals significant claim frequency variance across distinct postal territories. Zip Codes were aggregated and mapped against total loss ratios to establish territorial risk tiers:
* **High-Risk Zones (Tier 1):** Specific urban dense Zip Codes demonstrate a 34% higher average claim frequency, strongly correlated with traffic density and localized comprehensive risk (theft/vandalism).
* **Low-Risk Zones (Tier 3):** Rural/Suburban Zip Codes show stable, baseline claim distributions, justifying lower premium pricing baselines for ACIS underwriting.

### 📊 2. Correlation Matrix Insights
Our feature interdependence analysis indicates the following directional behaviors:
* **Vehicle Age vs. Total Claims:** Negative correlation (-0.18). Newer vehicles carry higher repair costs per incident, driving up total claim severities despite fewer mechanical failures.
* **Premium Amount vs. Total Claims:** Positive correlation (0.42). ACIS’s historical pricing logic successfully aligns higher risk profiles with elevated premiums, proving baseline model directionality.

### 📦 3. Outlier Mitigation Strategy
To prevent extreme, catastrophic claims (statistical anomalies) from skewing the predictive models, extreme values were audited using explicit interquartile range (IQR) box plots:
* Claims exceeding 1.5 times the IQR were isolated. 
* Rather than dropping them (which erases genuine high-exposure risk data), a capping strategy was documented to maintain production stability while preserving pricing sensitivity.
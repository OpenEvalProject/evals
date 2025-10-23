# Peer review - Round 1

Editors:
- James M McCaw, https://ror.org/01ej9dk98 University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89801.sa0](https://doi.org/10.7554/eLife.89801.sa0)

This study presents a valuable model-based analysis of how time to treatment post-symptom onset may influence Paxlovid efficacy in hospitalised COVID-19 patients. The analysis, based on a large data set, provides information on the action of the drug and supports clinical decision-making. Furthermore, it provides solid evidence for the role of the drug in reducing infectiousness in those receiving treatment.


---

# Peer review - Round 1

Editors:
- James M McCaw, https://ror.org/01ej9dk98 University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89801.sa1](https://doi.org/10.7554/eLife.89801.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "A retrospective cohort study of Paxlovid efficacy depending on treatment time in hospitalized COVID-19 patients" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

1) Both reviewers have queried the model fitting process and as a consequence, the reliability and/or interpretability of the results. Given the absence of data from the growth phase of infection for the patients, it is unclear how parameters that determine growth can be fitted, nor how the values of the population-level parameters that have been determined through the use of MONOLIX can be reliably interpreted. One reviewer has suggested a Bayesian hierarchical approach which would certainly have merit, allowing for prior knowledge on these parameters (from other studies of within-host SARS-CoV-2 dynamics) to be incorporated. At least one (and perhaps both) of the reviewers, and me as the editor, are familiar with MONOLIX and understand its strengths and limitations for undertaking mixed-effects analyses.

In revising the manuscript, these statistical concerns must be addressed. While an alternative Bayesian analysis has been suggested (and I would feel has great merit), it is not required and I will of course consider any suitably justified approach.

Whatever approach is taken, a clear explanation of why the parameter estimates (existing or recomputed) may be considered reliable and how uncertainty on them may influence the conclusions must be provided.

Furthermore, individual patient fits should also be provided (in supplementary material presumably given the hundreds of patients' time-series data being analysed). Also, individual time-series data for each patient should be made available to support alternative analyses.

Reviewer #1 (Recommendations for the authors):

Du et al. investigated the impact of the timing of Paxlovid treatment on SARS-CoV-2 viral load using a within-host mathematical model. They observed that even though the viral load could drop within the first 24 hours of receiving Paxlovid, it reduced more if patients were treated earlier after symptom onset. Their findings suggest that fast-acting antiviral drugs like Paxlovid have the potential to slow SARS-CoV-2 transmission while improving patient outcomes.

Data mostly support the conclusions of this paper, but some aspects of data analysis need to be clarified and extended.

1) The authors claimed that demographic information, drug administration data, symptoms, laboratory test results, and daily viral titer measurements of patients are available in EHR data, so it is necessary to describe important characteristics of patients (e.g., distribution of age and daily viral load) for better understanding of the study cohort.

2) Using the within-host model to estimate viral load trajectories is solid mathematically. However, the authors should discuss whether the parameters estimated by the model are reasonable biologically.

3) There have already been several papers using epidemiological methods (e.g., https://onlinelibrary.wiley.com/doi/abs/10.1002/jmv.28443) to investigate the impact of treatment initiation time on the efficacy of Paxlovid. The authors need to compare their findings with relevant literature, which might demonstrate the clinical significance of the results.

5) There are some errors in Figure 1D and Figure 1E. First, the two sub-figures do not share the legend. Therefore, please move the current legend in Figure 1E to Figure 1D. As described in the results [The overall reduction in viral load post symptom onset (relative to untreated cases) declines from 34% (95% CrI: 26%, 42%) for patients treated on the first day of symptom onset to 30% (95% CrI: 23%, 39%) for patients treated six days after symptom onset (Figure 1E, Methods)], the X-axis title of Figure 1E should be "Treatment initiation day after post symptom onset" not "Days post symptom onset".

6) The legend of Figure 2 seems to be incomplete.

7) I recommend that the authors include a schematic diagram to depict the process represented by the within-host model visually.

Reviewer #2 (Recommendations for the authors):

Du et al. estimated the efficacy of Paxlovid in reducing viral growth in SARS-CoV-2 infection by fitting a viral dynamics model to viral load data from 208 hospitalised patients in Hong Kong. They found that Paxlovid could reduce viral replication by more than 90% and treatment with Paxlovid on the first day of symptom onset may marginally be better than treatment six days later.

My major concern is parameter identifiability. As shown in Figure 1, the viral load data was only collected from day 4 post-symptom onset and has little information about viral growth phase. With the proposed viral dynamics model, the data is insufficient to estimate any model parameter that determines the viral growth rate, such as β, pi, δ, and more importantly epsilon. Even with a simpler model that excludes the refractory cell compartment, I don't believe those parameters are identifiable based on the clinical data presented in Figure 1. Therefore, I would be concerned unless the authors can demonstrate the identifiability of those parameters reported as main results.

I agree the model chosen is a typical model to use for studying viral dynamics and I have no problem with the model structure and construction. But the data doesn't cover the viral growth phase such that some parameters that determine the viral growth rate cannot be identified by the data. I would suggest using a Bayesian method to fit the model to data to check parameter identifiability.

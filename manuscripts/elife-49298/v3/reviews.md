# Peer review - Round 1

Editors:
- Floris P de Lange, Radboud University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49298.sa1](https://doi.org/10.7554/eLife.49298.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study aimed to characterize the temporal evolution of different neurological disorders in terms of their topological profile – a combination of graph-theoretical descriptors (e.g., centrality, segregation) that together best describe the progression of pathology. The study clearly shows the advantage of looking at a combination of topological features, rather than a single descriptor; and investigating disease progression longitudinally, rather than relying on end-stage data. Moreover, this work sets the stage for potentially improving the sensitivity of clinical diagnosis. As such, this work may be of significant interest to both fundamental researchers interested in disease mechanisms and clinicians aiming to use state-of-the-art methods to improve diagnostic success.

Decision letter after peer review:

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Differences in topological progression profile among neurodegenerative diseases from imaging data" for consideration by eLife. Your article has been reviewed by a Reviewing Editor and a Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

We recognize that the paper introduces the concept of "topological profiles", and using this novel method, can distinguish between neurological conditions. Unfortunately, the reviewers have raised concerns with the manuscript both in methodology and scientific advance. After discussion between with the editors and reviewers, the decision is to reject the paper without possibility of reconsideration at eLife. eLife is focused on publishing the most exciting and impactful research, but in this instance, the study fell short of our bar for publication.

Reviewer #1:

In this study by Garbarino et al., the authors investigated the topological progression profiles of Alzheimer's disease (AD), primary progressive MS (PPMS) and normal aging. They use the term "topological profile" which they define as the combination of topological descriptors showing the pathology propagation of a particular disease.

By investigating the relationship between topology of brain network connectivity and pattern of pathology, they aim to understand underlying mechanisms of propagation in AD and PPMS.

The neurodegeneration profile was found different in AD and PPMS as expected. The neurodegeneration profile in AD and PPMS were also different from the community-dwelling aging individuals (HA), however since this was a longitudinal study, what is the contribution of the aging process in AD and PPMS groups? Can the topological profile detect the influence of aging in the AD and PPMS groups? What was the mean age in each group? Was any age matching used? What was the time between each longitudinal scan?

Please discuss why the PPMS outliers showed no significant differences compared with the rest of the PPMS group.

If a PPMS patient is presented with dementia, although clinical features usually point out the origin, can the topological profile also distinguish whether dementia is due to MS or AD? Providing a case example may help.

Is the topological profile method applicable to other phenotypes of MS? Progressive MS (primary or secondary) is essentially the same except for preceding relapse(s), but there are more secondary progressive MS patients and therefore any clinical application would be more meaningful. Please discuss.

As neurodegeneration likely starts in the relapsing phase of MS, all the way back to asymptomatic phase of MS (radiologically isolated syndrome – RIS); please discuss the potential use of the "topological profile" method in RIS.

What is the clinical application of this method, how does this approach change the clinical evaluation of patients?

How does this method help understand the underlying mechanisms? Please discuss.

Reviewer #2:

This work aims at better understanding the longitudinal progression of gray matter atrophy in the brain in disease and aging. Specifically, it aims at understanding the topological organization of grey matter atrophy as a function of the disease progression, in parallel, for multiple diseases, including Dementia and Multiple Sclerosis. Three disjoint datasets (or cohorts) are used.

The methodology proceeds in four steps: (1a) computation of ROI descriptors for each ROI and each image. (1b) computation of graph-based (or topological) features for each ROI. (2) Computation of grey matter atrophy trajectories for each ROI and each dataset using a disease Progression Model (DPM). (3) Regression of the output of the DPM onto the graph-based features and (4) Statistical analysis of this regression.

In my view, the approach is of great interest. However, the analysis in steps (3) and (4) is lacking important details without which it is difficult to assess the validity and replicability of the approach. Specifically,

ν

A) in equation (2), what is the range of values of τ that is used? In the DPM, τ is not bounded as I understand, thus Yν might not even exist. In figure 2, in the 4 columns related to AD, how do you explain that the topological profiles are different while the left-hand side of (2) does not depend on τ. The same question applies to the columns related to PPMS and HA.

B) How much of the variance is explained in (3)? This is important because at this point it is not clear if the topological features, aside from the constant term, have any significant explanatory power. On a similar note, the null hypothesis β = 0 in Table 1 should be replaced by a less stringent baseline, e.g. β = 0 aside of the term associated with the constant progression. Other confounding, e.g. volume in healthy subjects could also be investigated.

In summary, the methodology is not rigorous enough to assess the validity and reproducibility of the findings in my view.

# Peer review - Round 1

Editors:
- Theodore Satterthwaite, University of Pennsylvania United States

Reviewers:
- Kate Mills, University of Oregon United States
- Ben Fulcher, University of Sydney Australia

## Review text

DOI: [10.7554/eLife.50482.023](https://doi.org/10.7554/eLife.50482.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Acceptance Summary:

This novel and important study capitalizes upon a large sample of youths scanned twice with magnetization transfer imaging, in order to map developmental profiles of cortical myelin. The authors use this approach to demonstrate that the human cortex undergoes dissociable, depth-specific changes in cortical myeloarchitecture during development. Critically, greater imaging markers of myelin were spatially associated with gene expression markers of oligodentrocytes, and align with a gradient ranging from primary sensory to higher-order association cortex. Together, this approach provides a new understanding of how cortical myelin develops during the critical period of adolescence. Furthermore, this data has numerous implications for understanding both healthy brain maturation and abnormal brain development associated with neuropsychiatric syndromes.

Decision letter after peer review:

Thank you for submitting your article "Shifts in myeloarchitecture characterise adolescent development of cortical gradients" for consideration by eLife. Your article has been reviewed by Joshua Gold as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Kate Mills (Reviewer #1); Ben Fulcher (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a study investigating intracortical microstructure in a sample of 223 individuals scanned twice between ages 14-27 years. Authors estimated myelin content in the cortex of magnetic resonance images using magnetization transfer, and by using central moments to test the hypothesis that mean and skewness of the magnetization transfer profiles would show different developmental trajectories and relate to different gene expression patterns. The study is comprehensive and the methods are sound. Writing and presentation are excellent, and code for reproducing the analyses is made available (and processed data where possible), further enhancing the impact of this work. Nonetheless, reviewers felt that several aspects of the work could be strengthened on revision.

Essential revisions:

1) NSPN sample. More details about the full sample (the full NSPN sample) compared to the included sample for this study would be useful. A visualization of the sampling design would be helpful.

2) Quality control. More details regarding the exclusion criteria and brain image quality control procedures are needed. What was the procedure for inspection, criteria used to determine exclusion, and number of scans excluded? Were both the raw images and processed images inspected for quality? Please describe the extent of manual intervention of processed images, including the protocol and number of scans that were successfully processed post-intervention and included in analyses.

3) AIBS. Further details regarding the processing of the gene expression maps is necessary (see: Arnatkeviciūtė et al., 2019). Furthermore, authors should clearly state that AIBS data are based on adult postmortem oligodendrocyte density. As such, it seems warranted to temper their claims (example: "confirmed a spatio-temporal overlap of our findings from NSPN with myelin processes during adolescence").

4) MT and myelin. The authors should clarify how sensitive is MT to myelin. The strength of this link is crucial to a lot of the interpretation and biological novelty of the results. MT (like T1w:T2w) may be sensitive not just to myelin, but also potentially other biological variables. Some evidence/discussion of this, and the extent to which the reader can safely make the association to myelin content would be helpful in the introduction. Furthermore, many features are different between the myelin stains and MT profiles (Figure 1B). Some brief discussion of the differences would be helpful. Finally, it would be useful to clarify if to the author's knowledge this is the first time anyone has matched MT depth profiles to a histological measurement (or discuss relevant literature of past efforts).

5) MT skewness and relative layer thickness. MT skewness may depend on the relative thickness of the different layers. It would be useful to clarify how much results explain the data beyond a simple cytoarchitectural analysis (e.g., are the depth profiles acting as a quantitative substitute for cytoarchitecture 'types', or is the inferred connection to myeloarchitecture relevant?) Furthermore, it would be useful to clarify if every node is squashed to the same absolute depth? This could impact interpretation: two areas with an identical ratio of myelination in deep relative to superficial layers would have different skewnesses if their middle layer was made thicker or thinner (thicker middle layer could push out the skewness). If this is the case, MT skewness could not simply be interpreted as a "ratio of myelination in deeper compared to more superficial layers"; it would more represent a measure of the preferential distribution of MT closer to the white matter boundary. Clarification is needed.

6) Statistical testing. Every time a statistical analysis is performed (and a test statistic/p-value quoted), it should be clearly stated to the reader what it is. Non-normal distributions seem common in this data; Spearman's correlations may be appropriate. Furthermore, it appears that the spin-test based permutations are only used for some analyses but not others (e.g., only from the "Age-related changes… MT profiles" section onwards). Were spin tests used for earlier spatial association analyses? If not, can this be justified?

7) Utility of low-dimensional embedding. Regarding this statement: "Nodes closer in this embedding space increase in microstructural similarity during adolescence, whereas distant nodes decouple", it is unclear why a low-dimensional embedding is useful a direct measurement of change is available. Couldn't you more easily do an analysis directly (e.g., investigate the structure of the 'increasing' edges?) What is gained from this harder-to-interpret nonlinear embedding that helps test/interpret your hypotheses? Perhaps more importantly, it is unclear if this statement is supported by the data: Wouldn't the embedding put nodes close in the space that have similar "patterns" of age-related MPC change with other network nodes? In the plot of the behavior of G1_dev, it does not display the claimed behavior (Figure 4B) – instead, it seems like the largest values of G1_dev already have ~maximal G1_MPC, and thus barely change at all between the <16 and >24 groups. Clarification is warranted.

8) Biological interpretation. In the discussion, the biological interpretation of the results at times is rather thin. If MT is a strong myelin marker, then why would myeloarchitecture be reorganizing like this (e.g., to support what behavior)? Axonal myelination improves transmission speeds and prevents the formation of new synaptic connections. Could you speculate on how this might alter behavior relevant to the longitudinal changes analyzed? Relevant papers to consider include:

*Micheva et al., (2016).

*Braitenberg, (1962).

*Huntenburg et al., (2017).

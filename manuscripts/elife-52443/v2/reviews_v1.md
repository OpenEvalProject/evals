# Peer review - Round 1

Editors:
- Thomas Yeo, National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52443.sa1](https://doi.org/10.7554/eLife.52443.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Hahn and colleagues analyzed data from 22 participants performing a complex cognitive task (Tetris) during concurrent fMRI-PET. The study demonstrated that performing the complex cognitive task yielded significant reconfiguration of brain connectivity (relative to rest). Yet increases in task difficulty yielded relatively small changes (compared with between rest and task). The convergence between two very different approaches – Metabolic Connectivity Mapping (based on PET-MR) and dynamic causal modeling (based on fMRI) – was impressive.

Decision letter after peer review:

Thank you for submitting your article "Reconfiguration of functional brain networks and metabolic cost converge during task performance" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the current manuscript, Hahn and colleagues analyzed data from 22 participants in a concurrent fMRI-PET dataset. Participants were either at rest or asked to play a Tetris game at two different levels of difficulty. While playing, fMRI BOLD or ASL was collected concurrently with FDG PET imaging. In addition, a set of baseline fMRI (BOLD and ASL) resting state scans and a final set of blocked BOLD task scans were collected in the absence of PET imaging. With this data, the authors examined the overlap of glucose metabolism (PET), BOLD, and cerebral blood flow (ASL) during the task. The authors then used a combination of the PET and BOLD data to make estimates of directed connectivity during the Tetris task, a technique called Metabolic Connectivity Mapping (MCM), and compared the results of this MCM analysis to a DCM analysis on the BOLD data.

This is a unique and interesting dataset, providing the authors with concurrent measurements of both fMRI and PET measures. The first analysis (Figure 2) demonstrating substantial overlap between glucose metabolism, BOLD, and ASL appears quite compelling. The convergence between two very different approaches (DCM and MCM; Figure 3) is quite impressive.

Essential revisions:

1) Throughout the manuscript, the authors refer to BOLD measurements as "neural activation" measurements. This is imprecise terminology to use, especially in the current context, where the BOLD measurements are being contrasted with measurements of cerebral blood flow and glucose metabolism. Likely all of these measures are at some level related to neural activity, but all are indirect, and it's not clear why BOLD measurements receive a privileged status on this front in this manuscript. I would strongly recommend shifting this terminology.

2) This terminological distinction is important because it obscured the approach used in the MCM analyses in this paper. The authors argue that glucose metabolism tends to occur largely post-synaptically, and thus a comparison between BOLD functional connectivity and PET glucose metabolism profiles allows for the determination of directed information flow. But there is also substantial evidence that the BOLD signal is better related to neural post-synaptic potentials than action potentials (e.g., Logothetis et al., 2001). Thus this logic is unclear. It would be helpful if the authors could expand further on the motivation and validation for this analysis.

3) Given general issues in the field with interpreting directed connectivity (e.g., Ramsey et al., 2010; Smith et al., 2011), validation with DCM seems like an insufficient standard. The authors should be explicit about the pitfalls of both approaches (DCM and MCM) and whether they cover each other's pitfalls. For example, DCM is probably sensitive to missing nodes, while MCM won't have that issue (as far as we can tell), so the two approaches nicely complement each other in this respect. Are there pitfalls that apply to both DCM and MCM? If so, how serious are these pitfalls and can they be addressed with control analyses?

4) Given the large amount of spatial smoothing that was performed across all modalities (8 mm), how informative is a spatial correlation calculated within ROIs for MCM? One way to test for this more robustly is to perform permutation testing by comparing a BOLD connectivity map from one subject to a glucose metabolism map of a different subject (and build a null distribution through many such permutations), rather than performing a basic t-test against zero (and similarly for the comparison against rest). This will determine whether spatial similarity is truly indicative of connectivity-metabolic coupling, or whether it is observed as a function of the large smoothing kernel (and relatively small ROIs).

5) Why were DCM ROIs different from the MCM ROIs (Figure 4—figure supplement 1)? If DCM is used for validation, it seems to make sense to use the same regions in both analyses. Furthermore, how does the interaction between the size of the ROIs (5 mm) and the smoothing kernel (8mm) affect the results?

6) Some of the statistical tests are unclear. The authors wrote that "the significance of each connection was tested separately using one-sample t-tests against zero". So let's consider one connection: FEF to IPS. The MCM analysis yields one spatial correlation for each subject. So can I confirm the t-test involves 22 numbers (corresponding to the 22 subjects)? Because a p value of 10e-12 is quite impressive with only 22 subjects; one would need a t-score of around 14?

7) For Figure 3, the authors say that the thickness of arrows depend on r values. More details will be useful. For example, when looking at Occ -> FEF, the two box plots for easy and hard conditions look highly overlapping, but the green arrow was much thicker in the hard condition than easy condition. And from what I gather from the plot, the IPS->FEF during hard condition has higher MCM correlation than Occ->FEF during hard condition. So why is the green arrow thickness than the yellow arrow during the hard condition?

8) It would be important to report the pure functional connectivity among the 3 regions. More specifically, are there region pairs with strong functional connectivity, but the MCM connectivity is weak in both directions. If so, how can this be interpreted? Similarly, are there regions with weak functional connectivity but the MCM connectivity is strong? If so, how can this be interpreted?

9) The DCM modeling needs to be further elaborated. Maybe the current details are sufficient for a practiced DCM user, but as someone who is somewhat familiar with DCM (but do not actively use it), I found it hard to know how task modulation and intrinsic connection were modeled in the generative model.

10) "A putative mediation effect of FEF was suggested by the observation that Occ -> IPS MCM values decreased in the easy condition (from 0.17 to 0.14, pBonf-Holm = 0.017) when controlling for the indirect pathway (Occ -> FEF -> IPS)." – Please elaborate on how this is done.

11) Literature review and discussion.

A) Given the nature of the paper, the authors should include a discussion of how their findings compare to a large and long-standing literature on cerebral blood flow and metabolism, which explicitly contrasts cerebral blood flow, oxygen consumption, and glucose metabolism to one another in and outside of tasks contexts, e.g., from Marc Raichle and others (see for example: Gusnard and Raichle, 2001). The current work would have substantially greater impact if it were to engage more deeply with this older literature. For example, do the authors mean to suggest (as might appear from their statement in the Abstract that "dynamic regulation of neural-metabolic coupling is essential to support human cognition") that different mechanisms exist to couple neural activity with glucose consumption depending on the task at hand? This claim seems quite large and far reaching given the evidence, and if true, would have profound implications in invalidating the current use and interpretation of many neuroimaging methods.

B) The authors should also be more precise about differences with previous work (e.g., Jamadar et al., 2019; Rischka et al., 2018). For example, "Here we extend upon previous work by providing a comprehensive assessment of the neural and metabolic processes supporting performance in a complex cognitive visuo-motor task" can be briefly expanded to mention that Rischka investigated a finger-tapping task and Jamadar investigated a visual checkerboard task.

12) The Discussion states: "Our results extend this knowledge by highlighting that the convergence between metabolic factors and functional network reconfiguration is pivotal to support cognition". However, the relationship with cognition or performance was not tested here (e.g. MCM was not shown to be stronger for those subjects who performed better). As such, I would recommend adjusting this interpretation.

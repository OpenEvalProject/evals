# Peer review - Round 1

Editors:
- Lucina Q Uddin, University of Miami United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62116.sa1](https://doi.org/10.7554/eLife.62116.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We believe that your work contributes novel insights into functional brain organization.

Decision letter after peer review:

Thank you for submitting your article "Topographic gradients of intrinsic dynamics across neocortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Lucina Q Uddin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Maxwell Bertolero (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This manuscript describes a study that examines topographic gradients of intrinsic dynamics in the human brain. The authors identify two gradients with distinct temporal compositions and gene expression, myelin, cortical thickness, network embedding, and functional activation properties. The reviewers agreed that the reproducibility analyses (replication on independent datasets, use of two different parcellation schemes), and comparisons of data with and without (grey-matter signal regression) are particularly compelling. The similarities in temporal features between distinct brain regions revealed a ventromedial-dorsolateral (PC1) and a unimodal-transmodal (PC2) topographic gradients. Interestingly, analyses suggest a weak correlation between "temporal profile similarities" and functional connectivity. Broadly, these initial set of results suggest that the organization of spontaneous BOLD signal fluctuations link to both the geometrical and topological embedding of regions in macroscopic networks. The second set of analyses suggest that various measures of signal autocorrelations link to PC1 while measures of distribution shape (dynamic range) link to PC2. Moreover, the detected gradients are correlated with the spatial distribution of gene expression, cortical thickness, T1w/T2w, and functional hierarchy in an opposite fashion. The third set of analyses focus on linking topographic patterns in spontaneous fMRI signals with probability maps of task-based fMRI signals. The output of this analysis reveals that PC1 recapitulates a cognitive-affective axis, whereas the PC2 link to a sensory-cognitive axis. Overall, the reviewers were all in agreement regarding the execution, significance and approach of the study.

Essential revisions:

1) The overall narrative and rationale for the approach is missing. Some additional comments and suggestions regarding conceptual framing are below:

a) The Introduction as it is written includes a great deal of jargon that should be unpacked. In particular, the terms "contextual information", "network embedding", "spectral power", and "nonlinear dynamic models" should be defined clearly as they are introduced.

b) Cognitive ontologies come out of the blue in the Results, and are not mentioned at all in the Introduction. Similarly, the significance of gene expression and its relationship to network structure is not at all discussed in the Introduction. Again in the Discussion, the rationale, significance, and relevance of the gene expression findings are missing.

c) The paper provides numerous "confirmatory" findings, but after reading the paper a few times, I am left wondering what new fundamental knowledge the study provides. We know that fluctuations in spontaneous fMRI signal are patterned across the cortex, and that such patterns link to genetics, microstructural gradients and macroscopic functional and structural patterns. Perhaps the most novel/unexpected result is that biologically meaningful time-series features are not associated with functional connectivity. However, this result is only superficially discussed. The authors should make an extra effort to highlight better how the paper confirms (still a vital endeavour) and extends existing knowledge.

d) I am confused about the use of the term "dynamic". The adopted measures have little to do with dynamic measures of neural synchronization per se; they are more summary measure of these dynamics. The authors should be careful in their terminology and discuss the results for what they are (i.e., summary measures of spontaneous changes in fMRI signal).

2) Points of clarification and queries regarding analyses are below:

a) It seems that temporal features (autocorrelation, variance, spectral power, etc) are all considered together in the hctsa analysis. How do the authors account for the fact that these features are not necessarily independent? In other words, does the analysis consider the inter-relationships between these individual features?

b) Perhaps consider including a comparison evolutionary expansion or the participation coefficient (PC2 is likely anti-correlated with these).

c) The statistics reporting needs work. Please report all degrees of freedom. Also, please either report the results in the figure that shows the data, or in the text. In many places, the statistics are divided up, and that makes it hard to read. Also, there seem to be many points where a t-test was done, but only a p-value, not a t-value, is reported. Just saying p is close to zero is not informative if I don't know the DoF and the t value. For each finding, report the test type, the test value, the p value (with DoF), and then reference the panel. Or just reference the panel and put those stats in it. Or both! Also, don't put a * if you are not going to explain what it means.

d) Several temporal features do not seem orthogonal (e.g., power spectrum and autocorrelations). I may have missed this information but, were redundant features removed to obtain a balanced set of features describing the resting-state fMRI signal? If similar features were not removed, results might have been biased towards aspects of rest fMRI signals that are over-represented. The Results section suggests that this may be the case.

e) Patterns of structural connectivity are known to be linked to spontaneous fluctuations in functional connectivity. I suggest extending these results by providing a quantification of the shared/distinct contributions of functional network topology and anatomical factors to temporal profile similarity.

f) Could the authors consider using an estimate of functional connectivity that accounts for shared signal (e.g., partial correlation, multiple regression)? I think this would shed light on the relationships identified in the paper and how much can be related to likely false positives found in correlation FC.

g) There is little discussion regarding why the variables (e.g., Figure 4) should (or should not) be related to each other (see also reviewer comment a). Given that many of these measures are inter-related, it is not entirely clear to me if they are meaningful. An example of this is the positive/negative relationships observed in Figure 4: Is this bound to happen because of the relationship between PC1 and PC2? Is this an interesting relationship, or just a statistical consequence of PCA?

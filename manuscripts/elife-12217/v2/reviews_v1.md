# Peer review - Round 1

Editors:
- Mark Jit, London School of Hygiene & Tropical Medicine, and Public Health England , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12217.018](https://doi.org/10.7554/eLife.12217.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Quantifying the global antigenic diversity of swine influenza A viruses" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Vijaykrishna Dhanasekaran, and the evaluation has been overseen by Mark Jit as the Reviewing Editor and Prabhat Jha as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision based on their comments. All of them agreed that this is a well written, comprehensive study of the antigenic diversity of swine influenza A viruses. The effort in assembling virus samples from several labs in Europe, USA, and Asian countries to carry out HI assays is a significant effort, and rectifies the lack of antigenic data from swine in recent years. The analysis adds important information to inform vaccine design and risk assessment of viruses that may present human threats. They also agreed that the antigenic analysis is the strength and novelty of this study, and could be expanded on significantly.

Essential revisions:

The reviewers and editors had two major concerns both of which need to be addressed. We would like to give you the opportunity to submit a revised version addressing the two major concerns within two months.

1) The antigenic maps presented in Figure 2 and supporting information are difficult to understand and interpret. Furthermore, the description that the antigenic diversity is greater or smaller is largely descriptive throughout the manuscript. To alleviate both problems, we suggest that you use the methods in your previous paper (Bedford et al. 2014), which integrates both genetic and antigenic data.

2) The reviewers all agreed that the greatest weakness of this manuscript is the phylogenetic analysis. The dataset used to generate Figure 1 includes several erroneously generated sequences. However, if you decide to use the Bedford et al. (2014) method as they suggested, the phylogenetic analysis could be dropped entirely, as it simultaneously characterises antigenic and genetic evolution and provides a method to visualize both simultaneously.

We have listed the issues identified by the reviewers with the phylogenetic analysis below. Even if you decide to address them rather than to drop this section entirely, we suggest that the large amount of text describing the phylogenetic analysis in the Results section is removed and replaced with further analysis of antigenic evolution.

A) The analysis has not inferred any ML trees. Relying just on BEAST trees is going to produce errors Bayesian time-scaled trees are very good at obscuring contaminants and sequencing errors. Most glaringly, the claim that there are 2 main lineages of classical H1N1 viruses arose because ML trees were not made. Colombia/0401, Guangdong/L3, and StHyacinthe/148 – these are all clearly sequencing errors if you make an ML tree, and not a second classical lineage that has managed to persist mostly undetected in swine for five decades, as the authors claim. The maximum-likelihood phylogeny in conjunctions with root-to-tip regression (using software such as Path-o-Gen) can be used easily to identify and remove sequences prior to BEAST analysis.

B) The legend says the branch colors are supposed to represent cross-species introductions, but there are plenty of examples where independent human-to-swine introductions (described in previously published literature) are colored the same (the green clade on the δ tree is a particularly glaring example of this, with at least 5 separate human-to-swine introductions all shaded green as if a single introduction – if the authors used more human background data this would be readily apparent). Although the text states that there are 36 separate human-to-swine transmission events of human H3N2 seasonal viruses, these are not labeled on the tree and there don't appear to be nearly this many, at least that currently circulate.

C) The presentation of the phylogenetic trees is perplexing. Why are there node labels for the age of nodes, when this can be determined from the x-axis already, but no node labels for node support (posterior probabilities), the key indication of clades and topological robustness? The shaded circles are inane – you can tell the length of the branch just from looking at the tree.

D) The data set is not well curated. There are avian-origin viruses in the tree (e.g., Saskatchewan/18789) that are presented as part of the avian-like Eurasian lineage, which incorrectly dates the tMRCA for this lineage all the day back to 1964 (when it should be the late 1970s).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The global antigenic diversity of swine influenza A viruses" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha as the Senior editor, Mark Jit as the Reviewing editor, and three reviewers, one of whom, Vijaykrishna Dhanasekaran, has agreed to reveal his identity.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below.

The reviewers agreed that the revised manuscript is a commendable and substantial improvement over the first submission. In particular they appreciated the work in correcting the phylogenies, using the BMDS approach to quantify rates of antigenic drift and new figures which better reflect the genetic and antigenic variation among the different lineages.

Their chief remaining concern is with the 'risk profiles for the global movement of swine and the potential for swine influenza-derived infections in humans.' The manuscript uses antigenic distances between viruses circulating in pig populations in different countries and in humans as a way to predict the likelihood of (a) viruses from one pig population invading another; or (b) transmitting successfully to humans, either as an outbreak or pandemic. The issue with (a) is that competition dynamics between strains are poorly understood in swine. There are repeated introductions of similar HAs and NAs into the same swine population, often with co-circulation. There is anecdotal evidence that the lack of onward transmission of the pandemic H1 in US and other swine populations is related to strain competition with not too distantly related classical H1s. But the idea that the probability of invasion is positively correlated with antigenic distance is an oversimplification and not based on any empirical evidence. It also fails to take into account reassortment, and even if the HA is outcompeted other segments can persist (as has been the case with the pandemic virus). For (b), it is clear that the restrictions on an animal virus successfully transmitting to humans have relatively little to do with antigenic properties. Antigenic distances are very likely to predict the age-specific attack rate of a pandemic virus, skewing the burden towards younger age groups. But the notion that antigenic distance is a good predictor of the likelihood of the pandemic occurring in the first place is not supported by any evidence. The paper relies on anecdotal evidence from H3N2v that it has not caused a pandemic due to existing immunity in adults. But this did not stop the pandemic of 1977. Your manuscript gets credit for stating up front that antigenic distance is not likely to be a key factor in pandemic emergence, but it then contains maps that likely misrepresent pandemic risk.

Hence we feel that (i) Figure 3 should be removed because it is based on the unjustified premise that antigenic distance is predictive of viral invasion or pandemic emergence, and (ii) the discussion of risk assessment should be qualified with the caveats above.

# Peer review - Round 1

Editors:
- Franz-Ulrich Hartl, Max Planck Institute for Biochemistry Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38795.036](https://doi.org/10.7554/eLife.38795.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Enhanced ER proteostasis and temperature differentially impact the mutational tolerance of influenza hemagglutinin" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ulrich Hartl as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Wenhui Li as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Raul Andino (Reviewer #2); Jeffery W Kelly (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Philips et al. explore the impact of ER proteostasis on the mutational and fitness landscape of a model substrate of the secretory pathway – influenza virus hemagglutinin (HA). The authors extend upon their (and others') previous work on host cell cytosolic proteostasis influence on viral sequence space.

The authors make use of a saturating library of single site HA mutants in a cellular assay of infection and replicative fitness of the mutant virions in comparison to the wild type HA in various conditions. Using targeted deep sequencing of HA, they were able to identify the spectrum of mutations which were either enriched or depleted (deep mutational scanning or DMS) under these conditions. They show that enhancing host cell ER proteostasis broadly increases mutational tolerance across the length of the model substrate HA and is likely to be relevant to shaping evolutionary trajectories of endogenous secretory pathway proteins. Importantly, they observe a striking rescue of high-temperature sensitive mutants by such an enhanced ER proteostatic state.

The data presented is comprehensive and extends our understanding of how compartment specific proteostasis mechanisms assist in shaping protein evolution.

Essential revisions:

1) A major issue with the authors’ central conclusion is that they did not examine other viral protein. If the proteostasis machinery has a direct effect on HA evolution it would be important to present evidence that other viral proteins are not affected, e.g. those that are not translocated into the ER. This point is important because it is possible that upregulation of the ER proteostasis pathway may result in pleiotropic and indirect effects on virus evolution. For example, ER proteostasis factors may affect expression of other factors that regulate HA function. Indeed, XBP1s regulates ~350 genes and ATF6f also affects a number of chaperones and quality control components. If other viral proteins are not analyzed, it is difficult to conclude that the observed effect is direct on client proteins.

It is suggested that the authors make a clear statement to the effect that their data cannot exclude the possibility that proteostasis effects not specific for the ER play a role.

2) Similarly, the increase on temperature (39°C) could modify factors and the kinetics of infection that indirectly can affect selection on HA variants. For example, have the authors considered the effect on translation and ER translocation rates?

This point could be addressed either experimentally or verbally.

3) In Figure 2—figure supplement 1, the authors examine the modified background conditions prior to conducting the DMS using RNAseq and claim consistency with their previous dataset. A visual comparison in the form of a Venn diagram (fold change based, at least, given that their previous dataset was from microarrays) can be presented to clarify the degree of overlap and outliers, if any.

4) Subsection “Modulating ER proteostasis during influenza infection”, third paragraph. The authors state that reduced growth did not affect the interpretation of the data. They should provide the average depth per sample and other related statistics either as a supplementary table or describe this in the methods. A replicate fidelity measure like a correlation coefficient or simple PCA would add to the validity of the dataset as a whole.

5) In the section describing the data filtering (subsection “Deep mutational scanning of HA in modulated ER proteostasis environments”, third paragraph), the reader would like to know the actual dropout percentages as per exclusion criteria (given numerically as a table).

6) In Figure 5A, the authors describe that at high temperature there is a gross reduction in the variant growth, consistent with the hypothesis of biophysical constraints imposed on them. Physiologically, this is likely due to a misfolding and degradation of the variants. Given that host cells do not upregulate components of ERAD at higher temperature (Figure 2 and Figure 2—figure supplement 1E) – is ERAD engaged more at such temperatures without burdening the overall proteostasis? Also, in conditions of UPR activation, at permissive and higher temperatures, the RNAseq data reveal highly upregulated ERAD components (in addition to other factors). Should the same variants not be subject to degradation? How many variants do not get enriched upon the ER proteostasis boost? The authors could explain their results in some more specific details.

7) Again related to Figure 5A, in the subsection “Deep mutational scanning of HA in modulated ER proteostasis environments”, fifth paragraph, describe the redundancy of the variants having a positive diffsel score between XBP1s and ATF6f/XBP1s conditions. Although the authors comment about the similarity, it would be interesting to see which sites overlap and which do not, possibly shedding light on subtle differences between the two modes of UPR activation.

8) Figure 7A describes the mutational tolerance in the XBP1s condition alone. What about the ATF6f/XBP1s condition?

9) In Figure 7B and 7C, the y-axis is unclear – is it a continuum from conserved to variable? Buried to exposed?

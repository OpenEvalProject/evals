# Peer review - Round 1

Editors:
- Tony Hunter, Salk Institute for Biological Studies , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18638.026](https://doi.org/10.7554/eLife.18638.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dynamic control of Hsf1 during heat shock by a chaperone switch and phosphorylation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Matthias P Mayer (Reviewer #1) and David S Gross (Reviewer #3), and the evaluation has been overseen by Tony Hunter as the Senior Editor and Reviewing Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Here, the authors rigorously tested two previously proposed hypotheses for Hsf1-dependent transcriptional regulation of heat shock genes upon temperature upshift in yeast: the chaperone titration model, which assumes that chaperones inhibit Hsf1 under non-stress conditions and are titrated away by stress-denatured proteins, and the Hsf1 phosphorylation model, which argues that Hsf1 is inhibited and activated by differential phosphorylation. They also re-assessed the somewhat enigmatic role of Hsf1 phosphorylation in its transcriptional activation. Through the use of mass spectrometry to identity a large number of heat shock-induced Hsf1 phosphorylation sites, the generation of phosphosite mutants, yeast genetic analysis, mathematical modeling, and a synthetic biology approach, the authors provide convincing evidence that Hsf1 is repressed by the Hsp70 chaperone in the non-stressed state and that titration of Hsp70 by unfolded proteins dominates the initial phase of the heat shock response. Phosphorylation of Hsf1 occurs only at later stages of the response and is responsible for sustained induction of target genes by recruitment of the mediator complex to the heat shock promoters, rather than Hsp70 dissociation.

Essential revisions:

1) There are a number of issues with the modeling of the heat shock response that need addressing:

A) The differential equations mentioned in the Materials and methods seems to contain some mistakes:

First equation: shouldn't it be "- k3[HSP][UP] " instead of "+ k3[HSP][UP]", as one would expect the concentration of free Hsp to decrease as it associates with unfolded protein?

B) Third equation: a "- k6[UP] " parameter could be added to the equation, as the unfolded proteins could also be degraded independently of Hsp70 or in other ways like aggregation be taken out of the equation.

C) How are the initial conditions used for the mathematical model established? Although the model nicely recapitulates the authors' observations, the basic settings of the parameters are far from known values. For example, the number of Hsf1 molecules per yeast cells was determined to be 49 (Chong et al. 2015) to 361 (Kulak et al. 2014), and the number of Ssa1 + Ssa2 molecules together was 19,306 (Chong et al. 2015) to 435,927 (Kulak et al. 2014), which gives a ratio of Hsp70 to Hsf1 of 394 to 1207. In their model the authors use a value of 10. Also, does 10.51 times more unfolded proteins than Hsp70 make sense? Since Hsp70 is considered to be 1% of cellular proteins, such a ratio would mean that 10% of cellular proteins misfold at a temperature when yeast is still able to grow.

D) k1 and k3 are bimolecular rate constants and should have the unit min-1 M-1. The actually observed association rate depends on the concentration of the components, in this case Hsp70, which changes after heat shock.

E) It would also be interesting to look at recovery from heat shock when the unfolded proteins are cleared out and the system returns to its baseline. Does the authors' model also recapitulate the shut-off phase of the heat shock response?

2) The authors present intriguing genetic evidence indicating that Hsp40 enhances the ability of Hsp70 to suppress Hsf1 function (Figure 3B). This raises the question of whether Hsp40 enhances Hsp70 binding to Hsf1 in vivo (Figure 1A). The authors should compare the co-IP heat shock time course in WT and ydj1Δ mutant cells?

3) The prior literature on the interaction of Hsf1 with Hsp70 needs to be discussed in more depth (see below for examples).

A) To strengthen their argument, Guisbert et al. (2013) should be cited, where the Morimoto lab shows through a genome wide screen that knockdown of hsp70 not hsp90 yields the largest activation of heat shock responders, hsp70 and a small hsp.

B) It was shown that deletion of hsc82, the yeast Hsp90, and cpr7, an Hsp90 cochaperone, leads to the induction of the heat shock response (Duina et al. 1998 JBC). The authors should discuss this discrepancy with their inability to find a role for Hsp90.

C) The Shi et al. (1998) paper from the Morimoto group addressing the regulatory mechanism of human HSF1 and deriving similar conclusions to the authors with respect to the role of Hsp70, is relevant, and should be discussed by the authors in the context of their findings.

D) It is becoming more apparent in recent years that Hsf1 has pleotropic effects in cell growth, proliferation, protein translation and stress protection which appear independent of chaperone activation (e.g. Baird et al., Science 2014; Mendillo et al., Cell 2013; Santagata et al., Science 2013). Because Hsf1 has a role in so many cellular processes, some discussion of the possibility that the highly mutagenized Hsf1 protein may not totally reflect wild type Hsf1 function with respect to chaperone activation but still may retain some basal function required for cell viability is needed.

In this regard, although not essential, further experimental evidence that the highly mutated non-phosphorylatable Hsf1 is not acting as a neomorph would strengthen the paper, as would some experiments with another non-amyloidogenic unfolded protein.

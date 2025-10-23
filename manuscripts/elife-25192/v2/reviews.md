# Peer review - Round 1

Editors:
- Alvaro Sanchez, Yale University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25192.019](https://doi.org/10.7554/eLife.25192.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "On the Mechanistic Nature of Epistasis in a Canonical cis-Regulatory Element" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Alvaro Sanchez (Reviewer #1), is a member of our Board of Reviewing Editors and the evaluation has been overseen by Aviv Regev as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lucas B Carey (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper addresses an interesting question, concerning the ability to predict the sign of epistasis. Non-additive (or non-multiplicative) effects of mutations on gene expression are common. The authors show that in a complex system in which both an activator (RNA Pol) and a repressor (CI) bind to the same sequence, the effect of mutations depends on both the environment (CI concentration) and on other mutations. This is an important problem in quantitative biology, and the authors have successfully resolved it for a specific system using a combination of theory and experiment.

Essential revisions:

All three referees expressed concerns regarding the presentation and a general lack of clarity of the manuscript. In order for the paper to be ready for publication, several major changes need to be made to the writing to improve its clarity and rigor. A consolidated list of required changes is below:

1) The thermodynamic model is an integral part of the paper and it needs to be described in detail in its own separate "Modeling" or "Theory" section of the paper. The authors should start the section by explaining what assumptions go into the model, explicitly stating which features of the system are being included and which excluded for the sake of simplicity. For instance, the authors should make it clear that their model ignores well known features of this system, such as explicit modeling of cI dimerization, cooperative binding of two cI dimers to OR1 and OR2, as well as any other assumptions that are currently implicit and not discussed. The authors should also explicitly discuss the limitations of their approach. For instance, if the model ignores any of these features for the sake of clarity, the authors should explicitly state how they expect this to affect a quantitative comparison between theory and experiment, and whether the model should be taken as a semi-quantitative comparison or not.

2) Along these lines, the referees were concerned about the lack of quantitative calibration of the model. Although it is understood that the model is used in a semi-quantitative fashion as a way to obtain the sign of epistasis rather than its magnitude, all referees found it would be necessary to establish how quantitatively accurate their model is, given the many assumptions it makes (as opposed to, for instance, more detailed models such as those of Ian Dodd et al. (Genes Dev 2004)). A way to do this would be to provide a quantitative comparison between their model and an independent data set. This is an approach that has been followed multiple times to calibrate thermodynamic models; See for instance the comparison between theory and experiment by Vilar & Saiz (PNAS 2005, NAR 2008), or Bintu et al. using the data from Muller-Hill et al. on the lac system (Bintu et al. 2005). One good data set where single point mutants have been studied can be found in the paper by by Sarai and Takeda, 1989. The authors should compare their theory with the results of Sarai & Takeda (or an alternative paper if the authors know of it). Note that we do not expect a perfect correlation between theory and experiment, but rather that the authors use such a comparison to establish how quantitative their model is, and whether we should just take it as a toy model that still provides some useful insights or a more serious thermodynamic model that captures the essentials of the system and provides reasonable predictive power. Either way would be fine, but the authors need to discuss this.

3) In the box (which may be instead re-purposed as a Figure that could go with the new theory section), Panel b is rather perplexing (and needs to be explained better). The authors plot Gene expression (Shouldn't this be fold-change in expression?) as a function of Ep (which, if interpreted correctly, is the free energy of binding of the polymerase). The plot is unusual because the free energy goes from +0.05 to +10 (in units of kT?). A positive free energy represents the case of repulsion between polymerase and the promoter. While technically the plot is correct, in that for a repulsive free energy, the higher the energy the lower expression would be, that is never the case and all known binding free energies between RNAP and promoters are of course negative and thus favorable (see Bintu et al., Dodd et al., and a long etc.). This point is particularly unclear in its relation with the rest of the paper, so it should be clarified.

4) A second panel to Figure 2 should be presented containing the +CI data.

5) The authors should explain in Figure 4 why they synthesized 30 new variants, 17 with statistically significant epistasis, to test the model? Why not use all 141 mutants, and use the single mutants to predict the doubles? The authors should explain their logic for doing this, particularly in relation to how quantitatively calibrated their model is.

6) The concept of sign epistasis should be better explained and motivated in the introduction. For example, when it is first introduced (in the Introduction section), it is not defined. For many readers, this will make it very difficult to understand the paper. The importance of sign epistasis is detailed in the second paragraph of the Discussion. As this is important to motivate the work, the authors should move it to the introduction.

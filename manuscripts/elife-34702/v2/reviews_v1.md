# Peer review - Round 1

Editors:
- Dominique C Bergmann, Stanford University/HHMI United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34702.031](https://doi.org/10.7554/eLife.34702.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Synthetic hormone-responsive transcription factors can monitor and re-program plant development" for consideration by eLife. Your article has been favorably evaluated by Christian Hardtke (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Given the interesting applications of your reporter system, we think this manuscript is a better fit as a Tools and Resources paper. This in no way changes the value we place on publishing this submission, but given the nature of this contribution, we feel it is more of a technical rather than a conceptual advance.

Summary:

With the expansion of systems and modeling approaches in developmental biology (and plant biology) the need for tools to test predictions of these approaches is increasing. This paper describes a bioengineering tool that uses CRISPR-Cas9 based targeting to bring selected genes under the control of phytohormones that signal by targeted protein degradation. This provides a way to (a) tune the transcription from these genes by exogenous hormone addition; (b) report levels of endogenous hormone signaling; and (c) re-parameterize hormone signaling networks at specific nodes. The basic system has already been described in yeast, but this paper aims to provide in planta evidence of the efficacy of these three applications.

Overall, the work described is an important a proof of concept, and all three reviewers felt that the HACRs could be valuable tools for the research community. The two major concerns were about (1) the limited robustness of the phenotypic analysis, and (2) whether it was clearly demonstrated that these tools enabled manipulations not possible with existing tools. Experiments suitable to address these issues are delineated below.

Essential revisions:

1) Analysis of phenotypes should be extended to T3 plants not grown under antibiotic selection. The authors argue that it is robust, given their controls and the long time between the selection and the phenotypic analysis. However, antibiotic selection often has long term effects in the primary shoot apical meristem, which can affect both the phenotypes analysed. Therefore use of unselected homozygous T3 lines necessary for truly reliable data. Extension of the n=25 T3 approach to additional independent lines is advisable.

2) Clear evidence that addition of the targeted HACR repressor will affect the dynamics of PIN1 induction and dampen positive feedback between auxin and PIN1 levels is needed. The authors assume that addition of the targeted HACR repressor will affect the dynamics of PIN1 induction and dampen positive feedback between auxin and PIN1 levels. This is never directly tested. Ideally it would be better to use a tagged PIN1 that rescues the pin1 mutant phenotype and validate the authors hypotheses about PIN polarization in buds and meristems more directly.

Alternatively some transcription dose-response analysis could be undertaken to test whether the induction threshold for auxin really is shifted as expected.

3) An example of an experiment that could only have been done with HACRs (and not weak alleles or existing tools) would be a strong addition to this paper. This could be done alongside a transcription dose-analysis as suggested in point 2. Alternatively, taking advantage of the inducibility of the constructs to provide spatial or temporally restricted manipulations followed by phenotypic analysis.

4) More information about the predictions from existing models is necessary. It is not clear from notes 1 and 2 whether the authors ran simulations to generate these predictions or rather intuited them from examination of model terms. Because of the relationship between auxin transport and auxin concentration, it is not easy to predict what the effects of changing the relationship between auxin concentration and PIN1 expression might be. If expression of PIN1 increases proportionately PIN1 at the plasma membrane, then increasing PIN1 expression will decrease cellular auxin concentration. Because of this negative feedback of PIN1 on auxin concentration, the effects on the system of reducing the positive feedback of auxin on PIN1 may not be very intuitive, especially at a tissue level.

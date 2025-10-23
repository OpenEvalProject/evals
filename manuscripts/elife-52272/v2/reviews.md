# Peer review - Round 1

Editors:
- Bavesh D Kana, University of the Witwatersrand South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52272.sa1](https://doi.org/10.7554/eLife.52272.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Deeper study of enzymes that play multiple, unexpected roles contributes to a more enhanced understanding of biological circuits and how these are regulated in response to changing environments and cues. Your study provides an intriguing description of how citrate synthase, an enzyme involved in primary carbon metabolism in the citric acid cycle, plays an additional role in the cell cycle as a regulator of the G1-S transition. A fascinating aspect of this finding was that this regulatory role was not related to the primary catalytic activity of the enzyme, highlighting the complexity in how bacterial cells regulate the transition between growth phases, using seemingly unrelated enzymes. The clever use of screens to uncover these effects confirms the utility of this, and similar approaches, for discovering new regulatory networks.

Decision letter after peer review:

Thank you for submitting your article "Bacterial cell cycle control by citrate synthase independent of enzymatic activity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jared M Schrader (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Berge et al. reports the results of a forward-genetic screen to identify novel regulators of the bacterial cell cycle using C. crescentus as a model system, revealing that one isoform of citrate synthase (CitA) is a regulator of the G1-S transition. This result was particularly intriguing as the phenotype did not dependent on citrate synthase activity. Indeed, a second citrase synthase homologue (CitB) could not rescue the phenotypic effects of a citA-deletion but was sufficient to provide complementation of enzymatic activity. The authors report that this is an example of protein "moonlighting" by providing a new, unexpected function for which there are a growing number of examples. These findings could be of broad interest, pending some further mechanistic insight.

Essential revisions:

1) In the initial Tn-Seq comparing WT and tipN deletion cells, the tipN deletion mutant had 33% of the hits as wildtype in the tipN gene-how could there be any hits in the tipN gene if it was a clean deletion (Supplementary file 1)? By contrast, the cpdR deletion had 0 hits in the cpdR gene. Is this an error? Please address

2) The authors should use ChIP-seq and lacZ promoters fusions to assess CtrA activity in citA mutants and to determine if the entire CtrA region or only a subset is under CitA control. These assays are regularly used in the Viollier lab. The in vivo phosphorylation level of CtrA could also be measured in a ∆citA mutant.

3) In the text as well as the model drawn in Figure 5D, the authors propose that CitA inhibits the Pts-Ntr pathway ultimately leading to inhibition of ppGpp synthesis. Thus, deletion of citA restores normal cell division in the tipN/cpdR mutant by activating SpoT and elevating ppGpp to block S-phase entry. While this model is consistent with the data, there are alternative interpretations. For example, citA deletion may have no effect on ppGpp levels at all and instead inhibits S-phase entry through another mechanism; however, when ppGpp levels are decreased in the evolved-fast growing PtsP mutants identified in the genetic screen, this is sufficient to promote S-phase entry. In order to demonstrate causality, it is critical to compare ppGpp levels in wildtype, citA-deletion, and citA/PtsP-double deletion strains. If the model is correct, one might expect that the citA-deletion increases ppGpp while the double deletion restores ppGpp back to wildtype levels. This is important to establish the model.

4) As an addendum to point 3, the authors should also measure motility behaviour of ∆citA mutants. Indeed, if ∆citA cells accumulate (p)ppGpp, the motility should be increased since the G1 cells would be blocked as swarmer cells. At least, Caulobacter mutants accumulating (p)ppGpp strongly increase their motility behaviour. However, based on the pictures of ∆citA cells shown in Figures 4 and 5, stalks are clearly visible on G1 cells. This suggests that cell cycle and development are uncoupled in ∆citA mutants, a phenotype typically observed when CtrA activity is enhanced but not when (p)ppGpp accumulates. Verification of this would make the story stronger.

5) The manuscript would benefit from a brief bioinformatics analysis reporting whether CitA and CitB were both conserved across α-proteobacterial species containing CtrA, or whether this only occurs in Caulobacteraceae. In the Discussion the authors note that there is evidence that nutritional stress may act on CtrA in Sinorhizbium meliloti, which does contain a citA ortholog, suggesting this moonlighting may be conserved. Examining the conservation of CitA/B may help others studying diverse α-protoebacteria to explore whether this might be happening elsewhere.

6) The story line of this manuscript is unclear. The authors start with negative genetic interactions between a polarity factor (TipN) and ClpXP proteolytic adaptors (CpdR, RcdA and PopA) due to the stabilisation of an oxidoreductase-like (KidO), which in turn decrease CtrA activity. Then, they set up a genetic screen in which they found citA mutants that, based on their initial hypothesis, should increase CtrA activity. But instead of characterising this potential negative regulation of CitA on CtrA activity, the authors moved to another genetic screen and found that inactivating (p)ppGpp synthesis suppressed ∆citA phenotypes. Finally, based only on these genetic interactions, the authors proposed a model in which CitA might regulate (p)ppGpp synthesis. There may be a plausible alternative model that would take into account all the data. Indeed, a recent publication of the Viollier lab (Delaby et al., 2019) showed that (p)ppGpp is required to support CtrA activity during stationary phase. Thus, CitA might inhibit CtrA activity so that ∆citA cells would have an exacerbated CtrA activity that leads to a G1 block, and inactivating (p)ppGpp production with spoT mutations would decrease CtrA activity back to level close to wild-type. Alternatively, (p)ppGpp and CitA could work independently of each other to antagonistically regulate G1-S transition. Therefore, the manuscript would be improved by keeping a more straightforward story line and to reinforce the likely link between CtrA and CitA. The genetic screen with the PpilA::nptII was originally used by the authors "to find mutations that maintain CtrA active in the absence of TipN and CpdR". Please consider how to better present the story.

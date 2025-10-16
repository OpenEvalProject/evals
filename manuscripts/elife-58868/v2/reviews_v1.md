# Peer review - Round 1

Editors:
- Ahmet Yildiz, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58868.sa1](https://doi.org/10.7554/eLife.58868.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript explores the molecular determinants enabling the kinesin-II motor protein to drive intraflagellar transport (IFT) and its contribution to ciliary length control. Kinesin-II has two motor subunits and a non-motor subunit. In this study, the authors demonstrate that kinesin-II is an obligate heterodimer, as engineered homodimeric motors are either unstable or undergo protein degradation. They also showed that engineering of a slow kinesin-II mutant results in shorter flagella, which provides the missing evidence for the primary role of kinesin-II in flagellar length control in Chlamydomonas.

Decision letter after peer review:

Thank you for submitting your article "Functional Exploration of Heterotrimeric Kinesin-II in IFT and Ciliary Length Control in Chlamydomonas" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Ahmet Uildiz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This work explores the molecular determinants enabling kinesin-II to drive anterograde IFT and its contribution to ciliary length control. Kinesin-II homologs across species are thought to be obligate heterodimeric kinesins. In Chlamydomonas, the kinesin-2 complex has two heavy chains, FLA8 and FLA10, and a non-motor subunit KAP. The authors showed that both FLA8 and FLA10 tend to self-dimerize when overexpressed in cultured human cells. While FLA10 pulls down KAP, FLA8 does not. Therefore, the authors interpret this observation as FLA10 is the main interacting partner of KAP, while FLA8's main role is to connect the complex to IFT particles. As a result, neither homodimer should be biologically functional. They could not detect FLA10 protein in fla8 deleted cells, suggesting that a homodimer is either unstable or undergoes protein degradation. The finding that a kinesin-II engineered to comprise two equal motor domains can drive IFT in Chlamydomonas is in principle exciting but could be better demonstrated (see below).

Perhaps, more compelling part of this manuscript begins when the authors replaced the motor domain of FLA8 with that of slower KIF3B (FLA8 homolog in humans). This chimeric motor walked slower in vitro, and rescued aflagellate phenotype in fla8 deleted cells. Surprisingly, the slowdown of kinesin-2 driven transport led to a 15% reduction in ciliary length at equilibrium and a reduction in the IFT injection rate. Using mathematical modeling based on the balance point model, the authors try to explain the shorter flagella in the rescue strain, but the conclusions drawn need to be supported by additional experimental evidence.

Overall, the manuscript pushes the field forward by providing experimental evidence for a biophysical model developed for the flagellar length control. We can recommend the publication of this work in eLife if the authors sufficiently address the concerns below.

Essential revisions:

1) The presumable distinct reason for the requirement of heterodimerization in Chlamydomonas is not convincing: The question of why kinesin-II is a heterodimer and if this feature is required for its function in IFT in most cells and organisms is an intriguing and long-standing question in the field. The finding that an engineered motor with identical motor domains rescues a knockout strain is exciting, but the conclusions drawn need additional evidence because the claim for the distinct requirement for heterodimerization in Chlamydomonas is built on CoIP data. These data do not reveal if the observed interactions are biologically meaningful. Given how efficient FLA10 and FLA8 form homodimers the interaction they observe in pull-down assays, it is not clear what prevents these motors to form a significant fraction of dysfunctional homodimers in cells. Kinesin-2 may be stabilized by ternary interactions (rather than binary interactions, as slightly implied in the last paragraph of the subsection “The requirement of heterotrimeric organization of CrKinesin-II for IFT”) and self-dimerization only occurs under overexpression conditions. We recommend two ways to test this possibility. First, measure self-dimerization efficiency in the presence of KAP and the other kinesin heavy chain. Second, reduce the expression level and test if self-dimerization occurs only under overexpression conditions.

In addition, can FLA8 or FLA10 homodimers move along microtubules in vitro? What is the stoichiometry of interaction? Indeed, for vertebrate kinesin-II there are contradictory reports if KIF3A homodimers can form, but only Funabashi et al. (vs. Rashid et al., Chana et al., De Marco et al.) was cited. This section should also comprise a comprehensive discussion of why heterodimerization might be necessary for IFT function.

2) The manuscript relies too heavily on ensemble methods (pull-downs and Western blots) for quantification (such as Figure 3G), and it would greatly benefit from fluorescently tagging kinesin-2 complexes in their Chlamydomonas strains for quantification. It would also be highly informative how changes in kinesin-2 speed affect its flagellar localization. Rather than modeling the size of the population of diffusive and ballistically moving motors, fluorescent tagging would allow for the direct measurement of these populations. If the values agree with the model predictions, this would strengthen the interpretation that it is indeed decreased motor speed that causes the observed reduction in ciliary length.

3) The findings that kinesin-II chimeras can move, albeit at low speed, and can rescue IFT in knockout strains which possess shorter flagella are intriguing. However, the chosen mathematical modeling approach to explain the shorter cilia has several issues:

a) Modeling: The authors use the assumptions of Hendel et al., but use the model of Fai et al., who reported that the only way to reproduce all experimental findings with their model is the integration of a length-dependent change of the axoneme disassembly rate. This parameter was, however, not considered in this study.

b) Assumptions: The stated assumptions for IFT (subsection “Modeling: relationship between motor speed, ciliary assembly and length control”, last paragraph) and the limitation of the motor (or ciliary building block) as a key determinant of ciliary length (Introduction, last paragraph) are exactly what Chien et al. and Hendel et al. suggested as a key determinant.

c) Different limitation regimes: The authors postulate three motor populations: Mf (free motors at the cilium base available for binding to IFT), Mb (ballistically moving motors engaged in transporting IFT along the axoneme), and Md (motors that are diffusing back to the base of the cilium). Their modeling reveals that for the slower chimeric motors the population Mb is increased and hence the population of Mf is decreased, additionally limiting the motor. In regenerating flagella they postulate a regime switch (subsection “Motor limitation is a major determinant of ciliary length”, last paragraph) and this is based on the data in Figure 4D, E. The change in the IFT injection rate seems very small and is based on noisy data (error bars). The authors should demonstrate if this is statistically significant.

d) Non-linear scaling: The authors need to explain more clearly how the strongly reduced speed of the chimera (and injection rate) leads only to a moderately shortened flagella.

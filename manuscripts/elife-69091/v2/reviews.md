# Peer review - Round 1

Editors:
- Aaron Frank, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69091.sa1](https://doi.org/10.7554/eLife.69091.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This study finds that the receptor-binding domains (RBD) of variants containing the N501Y mutation exhibits higher affinity for ACE2, which provides a possible explanation for their higher transmission for SARS-CoV-2. While follow-up studies will be undoubtedly required to more thoroughly establish this hypothesis, we believe that this manuscript, which has shown vast improvements during this peer-review process, will be broad of interest to eLife readers.

Decision letter after peer review:

Thank you for submitting your article "COVID-19 N501Y Mutation of Spike Protein Strengthens the binding to its Receptor ACE2" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another and with the Editors. Based on this discussion, we would like to invite you to submit a revised version of your manuscript. The Reviewing Editor has drafted this letter to help you prepare a revised submission.

Essential revisions:

1. A concern is regarding the AFM measurement is how do the authors know that the AFM pulling procedure is not pulling ACE2 out of the cell membrane?

2. The authors provide estimates of error in the off-rates measured using SPR (Figure 2d). However, they do not for the koff measured using AFM-SM. Why is the error estimates neglected in the latter case? As presented, the differences in koff derived from AFM-SM seem small. Without knowing the errors in the estimates, it isn't easy to gauge whether the observed differences are meaningful. The authors should therefore address this.

3. Can the authors please comment on why they did not carry out AFM-SM experiments on the K417N and E484K mutants?

4. The B.1.351 variant exhibits higher transmission and is less sensitive to existing vaccines than wild-type. The N501Y mutation might explain the increased transmission rate. The authors should comment on whether the additional mutations render the vaccines less neutralizing to B.1.351 variant in the Discussion section.

5. Moreover, the effects they have identified might be statistically significant, but they are modest. The authors must put forward an argument to explain why this difference is enough to drive the known differences in the SARS-CoV-2 variants.

6. In the abstract, the authors stated that "Molecular dynamics simulations of RBD-ACE2 complexes indicated that the N501Y introduced additional π-π and π-cation interaction for the higher 11 force/interaction." Unfortunately, though the authors observed higher maximum forces during the simulated unfolding of the Triple mutant, they did not perform a detailed contact analysis that links it to the additional π-π and π-cation interaction. Without such analysis, one cannot know why they observed higher forces for the mutant. The simulations have not yielded any more information beyond what is already evident from the AFM-SM experiments. Put differently, the current simulations and analyses have added little biophysical insights.

7. In the caption of Figure 4, the authors state that "Arrows indicate the key step during the dissociation of these complexes, of which structures are shown in (b-d), respectively." What do they mean by key step, how was it determined, and is it consistent over many independent trajectories? Related to the latter, the authors appear only to carry out three independent simulations per system. They should repeat the simulations at least 20 times and show that their observations are converged or consistent across the 20 trajectories.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "N501Y Mutation of Spike Protein in SARS-CoV-2 Strengthens its Binding to Receptor ACE2" for further consideration by eLife. Your revised article has been evaluated by Aaron Frank as Reviewing Editor and José Faraldo-Gómez as Senior Editor.

While we recognize the manuscript has improved, there remain substantial issues that must be resolved prior to publication – as outlined below. We urge you to address all of these issues as thoroughly and convincingly as possible before submitting the next revision of the manuscript.

In the abstract reference is made to "COVID-19 variants". The variants are of the virus, and so should be "SARS-CoV-2 variants".

Regarding Response 1: The transition to the added paragraph (Page 12; Line 305) is abrupt. The authors might consider something like:

"One concern was whether ACE2 was pulled out of the cell membrane during our AFM experiments. First, the unbinding force measured (~50 pN) is much smaller than the typical force needed to pull a membrane-bound protein out of the cell membrane…."

Regarding Response 2: It is stated that "In addition, as this reviewer pointed out later, it is a modest effect with a relatively small difference. That's another reason we performed a range of different methods to measure the kinetics and confirm this difference." This rationale should be explicitly articulated in the discussion of the manuscript. It will have the reader understand why multiple biophysical approaches were employed and the value-added by combining these methods.

Regarding Response 5: It is stated that "Enhanced affinity of SARS-CoV-2 variants contribute to the increased infectivity by lowering the effective virion concentration required for cell entry. Thus, a modest change in affinity will cause a significant arising in the infection rate." However, no direct or supporting evidence is present that supports this statement. Thus, it would be more appropriate if the authors should state this as an untested hypothesis. For example, "We speculate that enhanced affinity of SARS-CoV-2 variants may contribute to the increased infectivity by lowering the effective virion concentration required for cell entry. Thus, a modest change in affinity could cause a significant increase in the infection rate."

Regarding Response 6:

– Are the traces (4A-4E) from one simulation or an aggregate of 20 simulations? If from multiple simulations, we urge that you plot the error (or variation) in the force (4A-4C) and distance (4D and 4E) at each extension so that readers can get a sense of the uncertainty in the simulation data.

– Also, the statement that "SMD simulations revealed a higher unbinding force due to additional interactions for the complex with RBD mutant" needs to be revised to enhance clarity.

– Also, on Pg. 10, Line 247, it is written that "In the wild-type RBD-ACE2 interaction, T500 forms two hydrogen bonds with Y41 and D355 from ACE2. K417 from RBD forms a salt bridge with D30 from ACE2 (Figure 4A, Snapshot 1)" and on Pg. 252 that "In the RBDN501Y-ACE2 complex, Y501 forms an additional π-π interaction with Y41 and an additional π-cation interaction with K353(Figure 4B, Snapshot 1)." However, the referenced figure does not highlight these contacts. It will help the reader if close-up views of all the contacts that refer to in the text are included. These images should specifically show the contacts between the center of mass (COM) of benzene rings of Y41 from the ACE2 and the benzene ring of Y501 (for the π-π contact) and the distance between the hydrogen atom on the sidechain nitrogen-hydrogen bond of K353 from the ACE2 and COM of the benzene ring of Y501 (π-cation interaction).

– After reading the responses and the caption, it is not clear what Snapshot 1 and 2 are. Figure 4 caption states that "Snapshots (1) and (2) represent the difference of RBDs dissociated from ACE2 sequentially." What does "the difference of RBDs dissociated from ACE2 sequentially" mean? The caption and the references to Snapshot 1 and 2 in the main text should be revised to make it understandable to the general reader.

– In the representative SMD videos, we suggest that you render the specific contact π-π interaction between Y501 and Y41 and the rupture of the π-cation interaction between Y501 and K353. These contacts, between the center of mass (COM) of benzene rings of Y41 from the ACE2 and the benzene ring of Y501 (for the π-π contact) and the distance between the hydrogen atom on the sidechain nitrogen-hydrogen bond of K353 from the ACE2 and COM of the benzene ring of Y501 (π-cation interaction), can be displayed as dashed lines. The distances associated with these contacts at each frame should also be displayed. It will also help if the first frame in the video is annotated with labels highlighting which residue is Y501, Y41, and K353, and which contact is the contact π-π and π-cation. These modifications will enhance the information content of these animations.

– It remains unclear how the rupture force is determined. Please clarify, in the revised manuscript, what criteria were used to determine when a rupture has occurred.

The Discussion section lacks appropriate citations. It can also need to be further expanded to better place the results presented in the manuscript within the broader context of what is already known. Moreover, a careful and thoughtful discussion of the specific caveats associated with the experiments and simulation techniques employed currently is lacking but should be included in the revised manuscript.

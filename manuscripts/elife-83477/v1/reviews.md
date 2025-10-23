# Peer review - Round 1

Editors:
- Sudarshan Rajagopal, https://ror.org/00py81415 Duke University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83477.sa0](https://doi.org/10.7554/eLife.83477.sa0)

This important work advances our understanding of the structural basis of allosteric modulation of the M4 muscarinic receptor but has broad implications for GPCRs. The evidence supporting the conclusions is exceptional, with multiple cryo-EM structures that are complemented by excellent pharmacological and dynamics studies.


---

# Peer review - Round 1

Editors:
- Sudarshan Rajagopal, https://ror.org/00py81415 Duke University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83477.sa1](https://doi.org/10.7554/eLife.83477.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Pharmacological hallmarks of allostery at the M4 muscarinic receptor elucidated through structure and dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Sudarshan Rajagopal as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please address the comment from reviewer 1 regarding log tau vs log tau/KD for assessing the efficacy of ligands.

2) Please address the comments from reviewers 2-3, especially with the presentation of the data/figures for improved readability.

Reviewer #1 (Recommendations for the authors):

I have a concern about the use of a transducer coupling coefficient (log(tau/K)) in the manuscript. As the authors note, this is typically used to quantify agonist bias, usually by comparing it to a coupling coefficient for a different signaling pathway by the same agonist. But coupling coefficients really can't be used to compare different agonists because of different dissociation constants for each agonist – a reference is made to Kenakin, 2012 (which I went back to and didn't find this argument) that the coupling coefficient characterizes agonism of a specific pathway defined as the interaction between an agonist, receptor, and transducer. This leads to some questionable interpretations in lines 177-181. I believe the proper interpretation is that ACh is more efficacious as it has a larger log tau (which has been shown to be related to proportional efficacy by Onaran et al. – Sci Rep. 2017 Mar 14;7:44247. doi: 10.1038/srep44247.) – the transducer coupling coefficient doesn't matter as it is being driven by the tighter binding. Using the ternary complex model, efficacy is proportional to the differences in affinity between the transducer-bound and unbound states, while affinity largely reflects the interaction with the transducer-unbound state (depending on the experimental platform).

The same issue arises in lines 613-619 where an argument is made that "structures of GPCRs in a ternary complex… are better represented by their transducer coupling coefficient than the efficacy of the agonist…." Essentially, this is making the argument that efficacy/affinity is a better representation of the ternary complex than efficacy. Let's take an example of the b2 adrenergic receptor (which I know better than the M4) – isoproterenol has a log KD of -6 but is a full agonist hitting Emax. Pindolol is a very weak partial agonist but binds tightly with log KD -9.3 but with an efficacy of 10% of isoproterenol. If I calculate tau/KD for these two compounds, pindolol would have a much higher value – but it would be completely driven by the high binding affinity. It would not reflect the stability of the ternary complex. The interpretation that the transducer coupling coefficient is in contradiction to basic tenets of pharmacology.

I think the section on "Structural and dynamic insights into orthosteric and allosteric agonism" proposes some plausible ideas but probably overstates the insights that can be obtained from transducer-bound structures. As with other crystal or cryoEM structures, the observed conformation of the receptor is largely driven by the bound transducer and not by the pharmacological characteristics of the agonist (partial vs full, etc. – although I doubt you could get an antagonist bound to a transducer-bound receptor). This limitation has to be highlighted as it is a major one for these structural studies (and is theoretically less of an issue with solution-based studies).

Figure 6. It would be helpful to label some of the microswitches in the figure, as it may not be obvious to all readers, e.g., me, what specific residues they are looking at.

Figure S2. Any comment on the different populations of complexes with the PAMs? It is interesting that VU154 induces a large population of presumably a different conformation.

- Consider focusing on log tau as a readout of efficacy as opposed to the transduction coefficients, which have limited utility when comparing agonists.

- A sentence or two on limitations of the cryoEM approach in studying agonism due to the stabilization of the A-R-T complex.

Reviewer #2 (Recommendations for the authors):

1. The abstract focuses on the questions and the methods used to address them, with relatively little in terms of specific details about what is found. Simply saying the work offers "in-depth insights", while true, is a bit vague and leaves the reader guessing. Some more specific statements about key findings (e.g., the superior coupling to G protein induced by ACh) would be appreciated.

2. Figure 2 panels B-E and G-J might be made larger, and the data points for the other panels smaller, for clarity. The data points obscure error bars in all but a few cases.

3. Figure 3 shows a huge amount of structural data, but this means all panels in the figure are very small. The authors may want to consider a more focused presentation, with fewer essential components left for the SI. Panels A-C are somewhat redundant, for example, and a single representative example might suffice.

4. The discussion of Wang et al. 2022 and the corresponding figure S5 are very important. Figure S5 was difficult to interpret and see clearly, perhaps in part due to image compression by the journal. Even so, a more focused presentation would still be helpful, ideally with a finer map mesh. A transparent surface view may be even easier to interpret.

5. The discussion is clearly written and helpful, but reads as being targeted to a specialist pharmacology audience. Including more of a broad perspective and relating this to allostery in other GPCRs and other protein families could enhance the overall breadth of appeal.

6. The final sentence about signaling bias (line 624) is important, and the authors may want to state explicitly that the structural and mechanistic basis for biased signaling (and allostery as well) is likely to vary from one receptor to another. This is implied, but if the authors feel justified in making a stronger statement it may be helpful for clarity and emphasis.

Reviewer #3 (Recommendations for the authors):

1. I would propose merging Figures 1 and 2 to clarify which aspect is covered for each experiment in Figure 2. It would be great to use a color code (or any other sort of label) for each parameter (K, α, etc.) and highlight the respective plots (including supplements), for readers to follow the discussion.

2. It would also be helpful to show the structures of all four compounds in the main text, for clarity. These could be used to highlight which parts of the ligands were observed in the structure, vs. which ones were disordered (i.e. which bonds are rotating freely), as discussed for both Ipx and VU154.

3. All pharmacological experiments have been performed with a full-length wild type, however, the cryoEM structure contains a major deletion of ICL3. While I understand that previous experiments have used similar constructs for structure determination, I believe it would be helpful to confirm binding affinities, as well as the efficacy of the respective drugs with the truncated cryoEM construct. If this is not feasible, please highlight the caveat that all structures, and consequently all MD simulations, are based on data obtained from an engineered construct, rather than the wildtype sequence.

4. Line 190: What is a "NAL" (i presume it should spell 'NAM')? Please also discuss the impact of this observation.

5. The pharmacological experiments were conducted with all possible combinations of ligands (ACh, Ipx with LY298, VU154). I understand that it could have been merely a factor of resources, but were any attempts made to elucidate structures of the PAM-complexes with ACh?

6. It is not clear to the reader, whether the above pharmacological experiments (Figure 2) have been carried out for the very first time, or if others have attempted similar studies. Please clarify exactly what part of the work is novel.

7. Figure 2A: the fact that increasing concentrations of LY298 appear to block the overall binding of ACh is not described or discussed anywhere. Based on this plot LY298 would be a PAM-antagonist (see for example Figure 1, Grundmann et al. 2021, 10.3390/ijms22041763). This would be an important aspect, which would need to be addressed.

8. I would suggest placing some of the MD simulation traces into the supplementary materials, as these currently take up a large fraction of all figures. Alternatively, different complexes could be color coded and overlaid in one figure to highlight differences.

9. Figure 4 B and H: given the structure in Figure 4 H, it means that the binding pocket around Ipx leaves no room for any movement. Overall, I am not able to follow the discussion regarding the alkyne group/linker of Ipx not being visible. If the start and end points are fixed (visible densities), and have a rigid, planar triple bond involved (alkyne), I find it hard to imagine that the linker is flexible enough to wash out the signal for the linker. Also, the representative Figure S3F is not very convincing, as (A) all iperoxo densities seem to be of rather poor quality and (B) the average of all aligned structures would still likely result in an 'average-able' linker density. I would suggest either elaborating on or omitting this claim.

10. Line 301, The predominate χ2 angle of W413 was approximately 60◦ and 105◦ in the ACh-bound and Ipx-bound simulations, respectively, corresponding to the cryo-EM conformations. As depicted in Figure 4L, W413 when bound to ACh also samples angles close to 90 degrees or higher in the majority of Sim2 and part of Sim1. What is the significance of this conformational sampling?

11. On the note of ligands having flexible parts in VU154, and therefore no resolved densities in the maps, is there any pharmacological evidence (i.e. SAR) for these regions not contributing to binding/signaling? Analogously, are there any SAR data for replacing the alkyne bond in Ipx? It would be conceivable that a rigid replacement linker would affect (either positively or negatively) receptor binding and signaling.

12. According to the GaMD simulation results in Figure S7C, the minimum distance for the T433 and VU154 seems to be close to 4 Å while the predominant distance is around 7 Å. Therefore, I am wondering what the significance of this hydrogen bond is observed in the cryoEM structure. Additionally, T433R mutant showed increased binding to VU154 and showed the importance of T433 in species selectivity. Is this increased binding of VU154 with T433R mutant a result of a more "stable" hydrogen bond between receptor and VU154?

13. Regarding the species selectivity aspect, there is no mention of the V91L mutant in Figure 7, only as part of the triple mutant. It is hard to judge which mutations are responsible for species selectivity without either showing results for the D432E/T433R double mutant, or the additional V91L single mutant.

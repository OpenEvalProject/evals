# Peer review - Round 1

Editors:
- Kenton J Swartz, https://ror.org/01cwqze88 National Institute of Neurological Disorders and Stroke, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82175.sa0](https://doi.org/10.7554/eLife.82175.sa0)

This study uses a single-molecule polarization microscopy approach to identify the different conformation states that the arginine/agmatine antiporter AdiC transitions through during transport. Four states are identified and proposed to correspond to the key steps in the transport cycle, including inward-open, inward occluded, outward occluded and outward open, setting the stage for measurements of equilibrium constants and kinetics associated with transport. This is a cutting-edge and challenging approach that offers the potential for obtaining direct information of protein conformational equilibria that will be of interest to anyone studying membrane transport mechanisms.


---

# Peer review - Round 1

Editors:
- Kenton J Swartz, https://ror.org/01cwqze88 National Institute of Neurological Disorders and Stroke, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82175.sa1](https://doi.org/10.7554/eLife.82175.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Tracking multiple conformations occurring on Å-and-millisecond scales in single amino-acid-transporter molecules" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, including Janice L Robertson as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

The reviewers agreed that your study presents a cutting-edge approach that offers the potential for monitoring conformational equilibria of proteins, such as membrane transporters. In particular, the observation of arginine linked changes in the polarization distributions of AdiC is promising. However, major questions were raised during the review that indicate additional investigation is necessary to test whether the single-molecule data, and post-processing, leads to a robust determination of conformational states that pertain to transport. All of the points are listed in the comprehensive reviews below, but the major concerns are summarized here:

1. In both studies, it is reported that Ex-Ix, i.e. external-occluded to internal-occluded or C1-C4, transitions occur in the apo condition. The analysis also shows that equilibrium between these states (K4,1) is comparable to that in substrate saturating conditions. Therefore, this presents a model for AdiC that is an uncoupled uniporter. This means that if arginine is present on one side of the membrane, without any substrate on the other side, then AdiC would be expected to dissipate the arginine gradient because it could return back to the substrate-loaded side via the apo transition. However, Fang et al., JBC, 2007, carried out these experiments and showed that AdiC does not transport unless there is substrate on both sides of the membrane. Therefore, AdiC is a coupled antiporter that does not transition between the Ex-Ix states without substrate. Since the current study reports the observation of apo occluded state transitions, it raises a major concern that the states that have been identified do not represent the states in the full transport cycle. Further investigation is needed to consolidate the proposed model with the strictly coupled mechanism that has already been demonstrated for AdiC.

2. The conversion of the single-molecule trajectories to state transitions requires substantial post-processing, including averaging, step detection and clustering. Numerous reviewers raised the question of whether the four-state model that is being proposed is objectively determined from the traces or is imposed by restraining the k-means clustering analysis. Along these lines, testing alternate state models and comparing other clustering algorithms that do not require a pre-classification of states is necessary here in order to know if the 4-state model is robust, or equally likely compared to other multi-state models.

3. Following this, the study would be greatly strengthened if additional validation was carried out to test the identification of states, and perturb AdiC transport in a known way. Can a certain state be cross-linked to see whether the single-molecule trajectories report on the isolation of a single state? For perturbing transport, there are examples of mutations or conditions (i.e. high pH, different substrates) that are known to slow transport. Is the data capable of reporting on these changes, and do they agree with the expected shift in transport behavior? These validation studies are important to test the robustness of the single-molecule data and the state models to inform on the overall transport cycle.

4. Finally, macroscopic transport assays of AdiC would be extremely informative alongside the single-molecule studies. This would allow for important controls that will test transport activity of the actual construct being studied here, as well as help to consolidate any discrepancies in the protein behavior that was raised above.

Reviewer #1 (Recommendations for the authors):

1. Confirmation of function after labeling. The version of AdiC that is being studied here is labelled by a bis-maleimide-TMR, solubilized in POPC nanodiscs, removed 2 native cysteines, N-terminal Avi-tag and Strep-tag, and C-terminal Strep-tag. However, I do not see that a validation has been carried out to test if this construct/conditions independently yield the same KD for arginine or agmatine binding, or similar transport properties. Experiments of binding (e.g. by ITC) and transport (e.g. by radioactive uptake assays in proteoliposomes) of the labelled construct that is currently being studied are important controls to validate whether the single-molecule polarization data can be compared to wild-type data published previously.

2. The effect of anchoring AdiC on the slide. The strategy for conjugating the sample to the slide is via Strepavidin binding to the protein termini directly. The need for anchoring the protein to slide in order to observe polarization changes is understood. However, it also raises questions whether this anchoring may bias the observation of conformational equilibria. Since there is a small linker at both N- and C-termini, some benchmarking studies would be appropriate to test whether the linker length impacts the equilibria. Shortening the linkers may shift the balance to stabilize certain states, and lengthening (to a limit, within the range where polarization changes can still be observed) would demonstrate if more states become observable and the number of states becomes invariant with linker length.

3. Background labeling? Considering the labeling conditions of pH 8.0 and 4 hours, there is a possibility of background labeling of the maleimides with primary amines. Was the background labeling measured, for instance with constructs that do not contain the reactive cysteines? Also, it was mentioned that bleaching steps were used to assess labeling, but this was not shown so it is unclear what information was being obtained from these analyses. Both of these points should be addressed to give confidence that the label is attaching in the mode described and that there are no other possibilities of non-specific labeling.

4. Robustness of the clustering results. The clustering, as indicated in Figure 5, is not evident by eye and appears more as a continuum of conformations. It also reasons that the clustering results are dependent on the averaging, changepoint detection and k-means clustering parameters. Thus, the robustness of the identification of states should be shown across a range of parameters for each analysis step. In addition, testing different state models (e.g. 2-8 states) would be important to understand if the 4-state clustering is robustly determined or other state models also suitably fit the data.

5. Validation of the model with mutations that are known to shift the equilibrium between states. While the results showing the linkage of the states to arginine binding corresponding to the macroscopic measurements of AdiC KD provides some supportive evidence, additional investigation that tests the different states would strengthen the proposed model. For example, can a mutation be engineered, or reagent applied that stabilizes the inward-open or outward-open state, to see that conferred in the single-molecule polarization traces?

6. A cartoon of the full gene sequence and schematic of the AdiC construct that is being used here would be useful as supplementary information, in order to understand the sizes of tags and linkers applied to the protein.

7. In Figure 9, the colors in the plot do not appear to match the legend (different shades of blue).

8. Since the data is analyzed over single trajectories, how long are these traces typically? How long do the traces have to be in order to observe enough transitions between states?

9. The fitting of the KDs for states C1 and C4 are not justified as there does not appear to be a significant change in the probabilities over the arginine titration. Therefore, they should not be reported with confidence. Along these lines, are the errors that are being reported in Table 1 on the best-fits or are they over different samples?

Reviewer #2 (Recommendations for the authors):

Moreover, the identified 4 states and their substrate affinities reported in this manuscript do not significantly advance our understanding of Adic and the APC superfamily. Therefore, I would suggest combining this and the companion manuscript into a single paper. In addition, some more specific questions and suggestions are:

1) The key difference of the data processing described in this manuscript compared to the earlier published work is the introduction of the normalization step. Due to the random X-Y orientation of the transporter proteins on the surface, each protein molecule needs to be analyzed individually to get its own theta and phi angles in the laboratory frame (Cartesian coordinate). Normalization of the angles based on one of the identified states allows to directly compare the results for different particles directly. This is an interesting improvement, so the authors may need to mention this in the abstract.

2) In principle, the normalization may improve the accuracy of the mean angle values even as the deviations might increase. It would be helpful if the authors compared the ensemble-averaged mean values and the single-trace mean values.

3) From my understanding, to better differentiate the states, traces visiting all 4 states should be analyzed. When the authors select the traces with at least 12 transition events, do the events include transitions between all four states? The authors might want to clarify.

4) It is unclear how the authors establish the number of distinct states to be considered in the system. Is the number of states based on the expected structurally resolved 4 states or obtained from the analysis of the traces themselves? There is a proposed so-called full occluded state. Could/should this state be included in the data analysis?

5) The fluorophore is attached via two cysteines. Therefore, in the same conformation, the fluorophore has two orientations related by 180-degree rotation. Will this affect the detected signal? If not, then would a protein conformational change, which makes the fluorophore rotate by 180 degrees, be detected?

6) The protein is modified by a bi-functional fluorophore and surface-immobilized with multiple binding tags. How do you evaluate whether these manipulations affect the state populations and transport activity? The structures of Adic were all solved in the outward-facing states. Simulation (PLoS ONE 11(8): e0160219) also indicated that the inward-facing states, especially the inward-open state, are relatively unstable, suggesting that the population of the inward-facing states should be low. However, in Figure 7B, the inward-open state is highly populated, which seems inconsistent with the expectations. It seems that some additional experiments and or more extensive discussion are needed to support the authors' estimates of the state populations.

7) The state assignments are based on the similarity of the theta and phi angles to those calculated from the four crystal structures. To me, this does not seem entirely convincing, especially regarding the inward-facing states, expected to be lowly populated. The authors might need to use mutants or ligands to stabilize the inward-facing states to verify the assignment.

8) The authors need to describe how they estimate the errors in Table 1.

Reviewer #3 (Recommendations for the authors):

1. This work monitors only a single transmembrane helix (helix 6a) in AdiC. This was presented as an advantage, but in reality it also creates strong limitations for data interpretation. By comparing the orientations of helix 6a in PM-identified states (C1-C4) and in structural states, C1-C4 were dubbed externally open (Eo), externally occluded (Ex), internally open (Io), and internally occluded (Ix) states. Such assignment comes with high uncertainty even in optimal conditions. For example, without "seeing" the rest of the protein, how do the authors know that a particular PM state is not an intermediate state not observed in structural studies? Such a concern arises in part because of the assignment of C1 as Ex and C4 as Ix, with a state possibility of 0.19 and 0.14, respectively. Why would an antiporter sample occluded states so often without ligands? Is it possible that C1/C2 are both externally open (with some differences in helix 6a orientations) and C3/C4 both internally open and the occluded states are too rare to be observed when there is no ligand?

2. The assignment of PM states was actually done under not-so-optimal conditions. AdiC structures were only determined in ligand-free Eo and ligand-bound Ex states, so the authors used BasC and ApcT structures to represent the Io and Ic states of AdiC. Multiple questions about data treatments follow naturally. What's the justification to compare ligand-free PM states with ligand-bound structural states (Figure 6)? Although BasC (complexed with a nanobody) and ApcT have similar LeuT fold like AdiC, their sequences are not particularly similar and it's conceivable that AdiC's helix 6a might have significantly different orientations in Io and Ic states than the helix 6a in BasC and ApcT. How would such a possibility affect the assignment of the PM states?

3. Another main issue is about the relation of ligand-free and ligand-bound PM states. There are four ligand-bound PM states, labeled as C1L, C2L, C3L, and C4L to indicate that they correspond to the ligand-free C1, C2, C3, C4 states. However, the ligand-free and ligan-bound PM states appear to have quite different θ/ψ profiles (Figure 5), and the latter were not compared to the structures. How did the authors link ligand-bound PM states to the structural states? How to know for sure that C1 is related to C1L, C2 to C2L, etc? Moreover, it could be misleading to distinguish the corresponding ligand-bound and -free states just by an "L" as if their only difference is the ligand – the technique here provides no such resolution.

4. The authors might want to consider utilizing additional strategies to verify their state assignments. One possibility is to use structures as guidance to lock AdiC in a particular state via Lysine crosslinking and see how such maneuver affects PM results. The determined KD reflects how ligands drive the protein from ligand-free to ligand-bound conformational equilibria without providing much insight into the conformational details in each set of equilibrium.

Reviewer #4 (Recommendations for the authors):

In this paper, Zhou et al. propose a polarization microscope for measuring the emission polarization of bifunctional rhodamine molecules attached to AdiC transporters. The polarization is used to resolve the orientation of the fluorophores, which allows the authors to successfully resolve the four conformations of AdiC at a temporal resolution of tens of milliseconds. The measured orientation for each conformation is validated with the results using crystallography.

Overall, I believe the paper is well written and demonstrates a great application for orientation imaging using polarized microscopes. Detailed experimental procedures, calibrations, and mathematical frameworks are included. I have the following recommendations to improve the manuscript.

1) On page 20, the authors note that they set a threshold to filter out molecules whose total intensity varies during the measurements. The statement that "while fluorescence intensity is expected to vary among different polarization directions, the total intensity should be essentially invariant" is not true. Since the authors use TIRF illumination to excite the molecules, the excitation polarization component along the tilting direction (e.g., along the y-axis) of the excitation is 0, i.e., molecules oriented along that direction (e.g., y-oriented) will be excited less effectively compared to other orientations.

2) Could the authors provide more details regarding how the clusters are ranked? The authors note that C1-C4 are "ranked according to the values of both angles". It is not clear to me how this is done. Also, what is the range of the measured theta_L and phi_L? And how is the warping of the spherical coordinates handled in the ranking process, e.g., a change from 350 deg to 10 deg is +20 deg or -340 deg.

3) Is the k-means clustering also based on the distance in the Cartesian space, similar to the state identification?

Following comment (1) from above, could the authors comment on the possibility of further improving the measurement precision and accuracy using the excitation-dependent total intensity? Since the authors report a wobble angle of 22.5 degrees, the excitation dipole moments should be mostly aligned with the emission dipole moments.

# Peer review - Round 1

Editors:
- Janice L Robertson, https://ror.org/01yc7t268 Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74901.sa0](https://doi.org/10.7554/eLife.74901.sa0)

This paper presents a detailed single-molecule, multi-color microscopy study of the real-time assembly of perfringolysin O, a member of the membrane attack complex perforin cholesterol-dependent cytolysin superfamily. With the ability to resolve different reaction species simultaneously with membrane leakage, this work provides key mechanistic details including identifying assemblies involved in membrane lysis, and how membrane binding, oligomerization, and pore transitioning depends on concentration and pH. This study will be of interest to many, particularly those studying cytolysin mechanisms, but also the broader field of single-molecule studies of membrane binding proteins.


---

# Peer review - Round 1

Editors:
- Janice L Robertson, https://ror.org/01yc7t268 Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74901.sa1](https://doi.org/10.7554/eLife.74901.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Single-molecule analysis of the entire perfringolysin O pore formation pathway" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Janice L Robertson as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Nancy Carrasco as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ana J Garcia-Saez (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers found this to be an intriguing study, offering exquisite resolution into the complex reaction of perfringolysin O pore formation on membranes. However, all of the reviewers raised concerns about controls that are needed to interpret the data. It is anticipated that the following essential revisions can be reasonably addressed with further elaboration of the methods, revised analysis of the current data, or a limited number of control experiments. In general, the manuscript should also be revised to consider alternate interpretations of the data.

1) Mapping corrections between the co-localization fields. For co-localization of single-molecules, an experimental mapping correction is often performed in order to calculate the translational and magnification transformations that may be needed to map a pixel from one emission field to the other. This can be calculated using a sample that is known to contain co-localized molecules and imaged in both fields. Were experimental mapping corrections carried out in this study? In the following, it sounds that this mapping is carried out by the software: "We then used a software developed for single-molecule localisation microscopy (Schnitzbauer et al., 2017) to detect and track AF647-PFO spots appearing and disappearing at the locations of individual liposomes." If this is the case, please elaborate on how this works and whether you have data confirming that this method provides an adequate correction.

2) Estimating the number of PFO molecules from intensities. Since the single-molecule intensities follow a broad distribution (Figure 2D), it is likely that any estimation of the number of PFOs from intensities will have a large uncertainty and will have to include consideration of different labeling probabilities. Along these lines, the PFO quantities should be reported as the raw AF647 intensities in the figures. A clear description of how the number estimations are calculated along with the uncertainty on these estimates can be included in the discussion, as these number values are rough estimations.

3) The effect of photobleaching. A main result of this work is that the dimer has a much higher association stability with the membrane than monomers. However, monomers and dimers were measured with widely different power intensities and at different frame rates. Hence, it should be absolutely clear to the reader that this observation does not simply reflect the different bleaching rates of the two different molecules. For example, the monomer was sampled with high wattage powers and at 17 frames per second (˜1000 per minute). The dimers are sampled at high wattage (how high?) and 3 frames per minute. Considering that the measured dwell time for monomers is 0.5 s, while the one for dimers is ˜20 min (or 1200 s), it follows that if the authors are measuring the bleaching of the molecule rather than the association of the molecules with the membranes, then there would actually be no difference between the association of monomers and dimers.

To address this, more evidence is required to show that what is being measured is association and not bleaching. Specifically, what is the bleaching rate of the dye under the experimental conditions? This could be easily measured for the dimer, as single-step intensity reductions of the fluorescence should provide information on bleaching. The authors might also consider using different dyes with different bleaching rates and compare the association rates. In addition, they say that the signal disappeared in one step, which is indicative of dissociation of the dimer from the membrane, rather than a photobleaching step (perhaps the authors should mention this). It is assumed that occasionally, the signal disappeared in two steps. Please indicate how many times a two-step process was observed. The kinetics of the two-step process can also be used to characterise the photobleaching time. Please indicate here how fast is photobleaching and how that compares with the dwell time of the monomer binding. Comparison of rates measured at different fluorescent power of frames per seconds might provide a quick way to establish what is measured here.

4) Possibility of multiple complexes on a single liposome. One weakness of the study is the inability to distinguish between one or more complexes simultaneously assembling in one liposome. It is unclear how one can distinguish whether the estimated PFO numbers reflect the stoichiometry of one oligomer and not multiple oligomers on one liposome? The continued growth would suggest that this cannot be distinguished. Are there any abrupt steps in the oligomerization process that could be attributed to additional pore structures growing from defined seeding points? The single-step dye loss was interpreted to mean that only one pore is likely to permeate the liposome (Pg. 6), with multi-step signals interpreted as being from multilamellar liposomes. While plausible, there is no clear evidence of this, and it remains possible that the multi-step increases are due to more than one pore forming in the liposome. To clarify this, it would be beneficial to measure the full width at half maximum of the AF647-PFO fluorescence intensity profiles on individual liposomes and plot them as a normal distribution. This would allow to exclude measurements with a full width at half maximum outside the population average (e.g. the 95th percentile of the distribution) which most likely correspond to liposomes containing more than on PFO complex. In addition, the paper requires revisions to consider the alternate possibility that the data reflect multiple pore forming reactions on the single liposomes.

5) Please address the recommendations raised by the reviewers below. These suggestions are directed at clarifying the manuscript and interpretation of the results.

Reviewer #1 (Recommendations for the authors):

1. In Figure 1D, it will be useful to add examples of the "single step", "no step", and "other" traces directly in this main figure, as has been depicted in Figure 1 —figure supplement 3. Visualization of these representative traces is important to allow the reader to properly interpret the different behaviors.

2. In 2G, the super-resolution approach for PFO monomer binding appears to outline the liposome size quite well. Can you quantify the liposome size distribution based on this approach? Do you find that there is a significant amount of non-uniformity to indicate that your results may depend on liposome size?

3. Addition of uncertainty and statistical information. Much of the data presented lacks a description of the uncertainty or variability. For example, in the frequency/percentage bar plots, the binomial standard deviation could be used. In other plots, the mean is shown but without standard deviation. Please add this information and provide details in the legends about population or sample numbers.

4. Revise the following paragraph on page 4 as this paper is no longer accompanying:

"In an accompanying paper, Wallace and colleagues use single-molecule fluorescence tracking of PFO assembly on a droplet interface bilayer (Senior et al., 2021). These imaging studies support the insertion of incomplete arc-shaped membrane lesions, suggesting an alternative mechanism of pore formation that is distinct from the canonical prepore formation prior to insertion. This discrepancy raises the question as to when and how release of the membrane spanning regions is triggered, which cannot be correlated with key assembly steps using ensemble methods. Related to this matter, it is also unclear whether release and insertion of the membrane spanning regions from each of the subunits occurs in a concerted or sequential fashion."

5. Further technical details would be useful in this paper, such as how the co-localization was determined and corrected for different mappings between fields, as well as how the number of PFO molecules was ascertained by intensity analysis.

Reviewer #2 (Recommendations for the authors):

1. Page 7. How was the surface area of the liposome established?

2. Page 9-10. The authors go to a great length to describe the kinetics of oligomer formation. However, it is not clear how the authors can actually distinguish between the formation of many independent dimers and the formation of oligomers. Do they assume that once the dimers are on the membrane they will eventually meet up into oligomers? Is this a reasonable assumption given the diffusion time of the dimers and the size of the liposome?

3. Furthermore, it is not clear how the authors can distinguish between the formation of conductive arc pores and full pores. Since it is only possible to observe a full liposome, all these species should have the same fluorescence properties. How can the authors know the number of subunits of a pore, considering that the fluorescent signal can only estimate the overall number of units in the membrane? How can the authors distinguish a full pore from two arcs?

4. Page 10. The authors argue that the arc pores with at least four subunits can form pores. How did they come to this conclusion? Only on the basis of fluorescence intensity? If that is the case, has photobleaching taken into account? The authors identified the oligomer-length specific insertion rates from the insertion times. However, it is not clear how this was done. The authors should either point to the methods where more details should be given, or explain more in detail how this was done (e.g. is the number of subunit estimated by the fluorescence intensity?).

5. The kinetic model (Figure 6B) also assumes that a monomer is added to a nucleated pore. However, since monomers are transient and dimers rather stable, would it make more sense that dimers are constantly formed from monomers and these structures move around the membrane until they meet each other and then form full pores? Would it also not be easier for a full pore to be formed from two arc pores? The authors should spend a few arguments to convince the reader that the experimental setting can distinguish between these different scenarios?

6. Pore insertion kinetics (Page 12). This connects to the arguments above. How can the authors distinguish between the growing of arc pores from the formation of unrelated structures in the same liposome? Why this cannot be explained with a new nucleation process.

7. The authors observed a marked pH dependence of pore formation. How is the fluorescent signal affected by the pH? Please also indicate where the reader can find the mathematical models that allow distinguishing between membrane and lateral interactions.

8. Furthermore, the authors should measure directly (on and off rates) the monomer and dimer affinity for the liposomes at different pH values by fluorescence.

9. Figures. Please add the condition (salt, buffer and pH) in the legend of the figures.

Reviewer #3 (Recommendations for the authors):

Overall, the quality of the experiments and their analysis is excellent, and I have only some questions to be addressed:

1. The authors attribute the heterogeneous release profiles to heterogeneity in the liposome preparation. What about the stochastic nature of pore formation? That would also support the distributions observed between time of nucleation/poration.

2. The fluorescence signal of PFO on individual liposomes seems heterogeneous, which the authors attribute to differences in cholesterol distribution. However, the lipid composition is not expected to present phase separation. Could this be due to complex assembly on part of the liposome leading to heterogeneous distribution? Otherwise, the authors might test their hypothesis of inhomogeneous cholesterol distribution by fluorescence microscopy on giant unilamellar vesicles or lipid bilayers containing a lipophilic dye.

3. Please explain how the different kinetics of monomer addition to the pre-pore or the pore states are considered in the mathematical model.

4. Please explain how the oligomerization rate by monomer addition before and after insertion can be the same. One would expect that the energetics of the interactions of the monomers with the non-inserted and inserted oligomers would differ. This part of the model is not very convincing yet and requires elaboration.

5. Do the complete rings continue to grow indefinitely? Please explain.

6. While the authors nicely confirm that AF647-labelled PFO is functional and that the effect of self-quenching is small using different ratios of labelled to unlabeled PFO (Figure 1 —figure supplement 2), this analysis also revealed that a 100% ratio of labelled PFO is more active in perforating liposomes. While this effect can be caused by an underestimation of the amount of unlabeled protein (as the authors mention), they should also discuss the option that AF647-PFO is indeed more active due to possible structural alterations caused by the label.

7. The authors use photobleaching step counting of sparsely distributed AF647-PFO immobilized on glass coverslips to measure the reference monomer fluorescence intensity (as shown in Figure 1E and D). Considering that AF647-PFO has an estimated labeling efficiency of ~1.5 fluorophores/PFO, it would be beneficial to compare the population distribution of the determined monomer intensities (Figure 1E) to the intensity distribution measured for monomeric AF647 dye immobilized on glass.

8. In order to measure the oligomeric state of AF647-PFO at different time points in the liposomes, the authors determine the ratio of the fluorescence intensity associated with the liposome to the monomer fluorescence intensity derived from single photobleaching events. Given that not all PFO molecules are labelled with one single AF647 fluorophore (Figure 2E), the calculation of molecular units from fluorescence intensity is somewhat error prone. Labelling efficiency correction of the measured fluorescence intensities should be used to test if there is an influence of the labelling efficiency on the determined oligomeric state of AF647-PFO.

9. Considering the lipid composition of the outer leaflet of the plasma membrane (as a biological target for PFO pore formation), a concentration of 55% cholesterol seems very high. The authors should state in the manuscript why they chose the specific lipid mixture and how it might affect the mechanistic regulation of PFO (membrane binding, oligomerization, etc.) compared to the physiological scenario of the plasma membrane.

10. When discussing the possible explanations why PFO pores continue to grow over time with wit a membrane insertion rate increasing with concentration, the authors should also discuss the effect of continuous protein insertion on the physical properties of a toroidal pore. Increasing number of protein molecules inserted in a membrane increase the membrane tension and at the same time decrease the line tension at the pore rim both promoting the stabilization of an open pore.

11. In this line, the authors should also include a figure showing the oligomerization characteristics of PFO (as in Figure 4 B) beyond the expected number of molecules required to form a full pore ring until the oligomerization reaches saturation. The possible explanation for the continuous increase in the number of PFO molecules that "eventually multiple pores form" (page 6) is contradictory to the valid assumption made later that an existing PFO oligomer in the liposome "acts as a sink for monomers" (page 12) that newly bind to the membrane.

12. The authors should state in the manuscript why a Cysteine-free version of PFO (PFO(C459A)) was used.

13. Quantify the percentage of unpermeabilized liposomes in Figure 2 —figure supplement 2.

14. Please provide statistics (i.e. number of measured vesicles or complexes, number of technical replicates and test for statistical significance if applicable) for the data shown in Figure 1 D and E, Fig, 2 E and D, and Figure 1 —figure supplement 1.

15. It is misleading that PFO oligomers with a number of subunits below the reported number needed to form a full ring are referred to as arcs. There is no experimental prove in this study that these oligomeric states of PFO indeed assemble to an arc-like structure in the membrane.

16. The terminology "oligomer length" implies a structural parameter. Better refer to it as "molecular size" / "oligomeric state2 / "no of subunits/molecules".

17. Please clarify that Figure 3D shows the sum of individual localizations over time and not multiple simultaneous localizations of AF647-PFO to one liposome.

18. The deliberate offset of the two fluorescence channels in Figure 2 —figure supplement 2 is somewhat misleading as it hinders the correct interpretation of the data. It would be better to show the correctly aligned image of the overlay and the single channel images and the merge of the cropped area for better visualization.

19. Please specify the meaning of the orange line in Figure 7 F and H.

20. Page 8: Please specify in the sentence "To determine the stoichiometry of AF647-PFO in the long-lived state, we measured the average intensity of all long-lived signals on liposomes." that it is averaging over time and not over several particles.

21. Please include scale bars in the microscopy images in Figure 1C, Figure 2C, Figure 2B, Figure 2 —figure supplement 1, and Figure 2 —figure supplement 2.

22. Refer to Table 1 also in the main text of the manuscript.

23. Page 13: Please correct the referencing to the different panels in Figure 7 F-I.

24. Page 6: Please correct the typos "Figur1 Figure Supplement 3" and "Figur1 Figure Supplement 3B".

25. Figure 3D: Please correct the typo "AF4647-PFO" in Figure 3D.

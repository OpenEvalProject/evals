# Peer review - Round 1

Editors:
- Andreas Martin, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63042.sa1](https://doi.org/10.7554/eLife.63042.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study provides the first structural and biochemical evidence that RuvBL1/RuvBL2 directly interacts with the RNA helicase DHX34, suggesting a potential mechanism for the previously described activity of this AAA ATPase in the initiation of nonsense-mediated mRNA decay (NMD). The presented cryo-EM structure reveals how DHX34 binding to the RuvBL1/RuvBL2 heterohexamer induces a conformational change of RuvBL2's N-terminus and consequently modulates nucleotide binding and hydrolysis in every other subunit of the ATPase ring, potentially acting as a switch in orchestrating the assembly of NMD factors.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Regulation of RUVBL1-RUVBL2 AAA-ATPases by the nonsense-mediated mRNA decay factor DHX34, as evidenced by Cryo-EM" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Andreas Martin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

As you will see in the individual reviews, there are a number of issues and weaknesses, both, for the structure determination and the biochemical characterization, and with several of them consistently picked up by multiple reviewers. Our decision has been reached after consultation between the reviewers, and based on these discussions and the individual reviews below, we regret to inform you that your work cannot be considered for publication in eLife at this point. However, reviewers agreed that the manuscript is potential interesting, and we invite you re-submit your manuscript after the critical corrections, analyses, and additional experiments have been completed.

Reviewer #1:

López-Perrote and colleagues present the structure of DHX34-bound RUVBL1-RUVBL2, which is implicated in nonsense-mediated mRNA decay (NMD). This structure demonstrates how DHX34 uses most of its domains to interact with the internal regions of the DII domains in both RUVBL1 and RUVBL2, and causes large conformational changes in the RUVBL1-RUVBL2 hexamer, in particular the ATPase domain of RUVBL2. DHX34 is identified as a potential regulator of RUVBL1-RUVBL2's ATPase activity, which represents an important step in determining the mechanisms underlying the initiation of NMD.

However, before this manuscript can be considered for publication in eLife, the authors should address several concerns, as outlined below.

Major Points:

1) The authors suggest that oligomerization of RUVBL1 and RUVBL2 hampers nucleotide exchange, yet this model seems not sufficiently supported by the data and the authors should adjust their discussion in this respect.

The ATP-binding pocket is located between neighboring protomers, with critical motifs contributed by both AAA domains, such that monomeric RUVBL1 and RUVBL2 are not capable of ATP hydrolysis. The comparison between hexamer and monomer is therefore unnecessary, and proposing that hexamerization lowers the ATP-hydrolysis rate does not make much sense. In fact, the subunit interface between RUVBL1 and RUVBL2 appears highly similar to that of other AAA+ motors, and it is in my opinion unlikely that the pocket itself "traps" the nucleotide and prevents exchange. At the various stages of the ATPase cycle (or positions in the hexameric ring), individual subunits of numerous other AAA+ hexamers show differential opening and closure of their nucleotide-binding sites. Depending on the averaging for the RUVBL1-RUVBL2 structure, subunits may appear uniformly closed, which, however, is not necessarily inconsistent with hydrolysis activity. What could contribute to the low rates, as suggested by the authors and previous studies, are the N-termini of RUVBL1/2 that seem to contact the nucleotide and in the case of RuvBL2 get released upon binding of DHX34. Given the minimal ATPase rate of 1 per min, RUVBL1/2 may indeed not work as a processive ATPase, but only as a switch that could get triggered by DHX34. In that respect this new structure is very interesting.

2) The overall analysis of nucleotide occupancies is problematic, considering that the resolution is not high enough to confidently assign nucleotides to each site.

The inherent averaging that occurs in single-particle cryo-EM image processing may very well explain the absence of detectable nucleotide in all RUVBL2 pockets of the DHX34-bound complex. As observed for many other cryo-EM structures of AAA+ motors, nucleotide pockets are highly dynamic and often less well resolved compared to the rest of the structure. Whether binding of DHX34 indeed induces a 3-fold symmetric state of the hexamer in which all 3 RUVBL2 sites are nucleotide free remains questionable. Building the class averages was likely determined by the asymmetric DHX34 density above the ring, and if the orientation of DHX34 is not well correlated with the nucleotide occupancy in a particular RuvBL2 subunit, averaging particles based on DHX34 could make it look like all 3 RuvBL2 sites are empty or lower in nucleotide density, whereas in reality it may be just one. If this were the case, the structure would resemble other AAA+ motors that show a small gap in the hexameric ring flanked by a nucleotide-free "seam" subunit, while all other subunits represent a continuum of nucleotide states.

To better evaluate the local resolution of the nucleotide pockets, it is necessary to have a zoomed-in view of these pockets on the ResMap of the 4.18Å RUVBL1-RUVBL2 hexameric ring (Figure 3—figure supplement 2D), highlighting the ADPs in RUVBL1. It is important to know the local resolution for these pockets, because based on the current evidence, the map alone may not provide enough detail to accurately assign nucleotides. One way to address this is by doing a more thorough analysis of the pockets themselves, including the overall size, shape, and location of key hydrolysis residues in comparison to known hydrolysis states of these pockets.

For example, in both Figure 4E and 4F it would be helpful to include labels of hydrolysis-relevant residues, like Arginine fingers and Walker A/B motifs, such that readers can easily orient themselves. In Figure 4E, the pocket looks just as "open" in the ATP-bound state (2XSZ) as in the DHX34-bound structure, and it is important to explain why this is considered a nucleotide-free rather than ADP- or ATP-bound state. Are there retracted residues that make this pocket incompetent for nucleotide binding? And could an ATP possibly fit into the RUVBL1 pocket? The current thresholding in Figure 4F does not exclude this possibility. It would also be appropriate to include the N-terminal histidines that directly interact with ADP in RUVBL1, as this may provide further evidence that it is indeed an ADP.

In general, it may be worth processing the data again and building class averages while masking out DHX34 to assess whether the hexamer indeed adopts a clear 3-fold symmetric state.

3) Regarding the very low ATPase rate of just 1 min-1, one potential issue may be that RUVBL1/2 was not purified in the presence of ATP and an ATP regeneration system. There are several examples of AAA+ motors that irreversibly lose robust activity when purified in the absence of ATP, and it may be worth testing whether RUVBL1/2 shows higher activities when purified in ATP.

The NADH consumption shown in Figure 5A is not linear, but increases over the 30 min measurements (30 – 60 min) for both, RUVBL1/2 and the DHX34-bound complex. What is the reason for that and what do the traces look like between the addition of RUVBL1/2 and the 30 min mark? The regeneration of ADP present in the RUVBL1/2 sample at the time of mixing should be completed within a couple of seconds, and temperature equilibration is expected to take only a couple of minutes. Non-linear absorbance changes over tens of minutes and a slow acceleration indicate that the system was not at steady state, which could also be consistent with the AAA+ motor being trapped in an inhibited state due to purification in the absence of ATP.

The authors discuss a model where ATP hydrolysis may regulate the interactions of RUVBL1/2 with other partners during NMD initiation, and the more stable binding of RUVBL1/2 to partners of the R2TP chaperone pathway in the absence of ATP hydrolysis is mentioned as an example. Similar effects have indeed been observed for various other AAA+ motors whose interactions are more dynamic during ATP hydrolysis. For RUVBL1/2, how does the very low ATPase activity of 1 min-1 compare to the off rate of its binding partners?

The authors propose that the ATPase inhibition of RUVBL1/2 by DHX34 may stabilize complexes. However, according to the presented model, DHX34 binding induces nucleotide release from every other site in the hexamer, which is expected to have distinct or even opposite effects compared to preventing hydrolysis and trapping hexamers in permanent ATP-bound states.

It is also suggested that DHX34 binding fully eliminates ATP hydrolysis (and even nucleotide interactions) in the RUVBL2 sites, while RUVBL1 "continues hydrolyzing at comparable levels to those measured in the absence of HBX34". This would mean that ATPase subunits in the hexamer are completely independent in their ATP hydrolysis, with no communication between neighbors. Although this is not ruled out, it has to my knowledge not been reliable described for other AAA+ hexamers, which usually show coordinated transitions and subunit communications that are mediated by arginine fingers and various other interactions within the topologically-closed rings. In fact, the ATPase rates for the single Walker-B mutants RUVBL1(E303Q)-RUVBL2 and RUVBL1-RUVBL2(E318Q) do not show 50% lower activity, but a reduction by 80 or 75% (Figure 5—figure supplement 1B) compared to wild type, suggesting that there is indeed communication between neighboring subunits.

The authors may consider further investigating this, for instance by characterizing hexamers with Walker-A or Walker-B mutations in RUVBL2, or an Arginine-finger mutation in RUVBL1 in the presence and absence of HDX34. If the authors' model is correct, the ATPase activity of these RUVBL1/2 variants should not respond to DHX34 binding and be similar to that of DHX34-bound wild-type RUVBL1/2.

Reviewer #2:

Lopez-Perrote et al. show that RUVBL1-RUVBL2 participates in the nonsense-mediated mRNA decay (NMD) pathway through direct interaction with the DHX34 RNA helicase. The authors present a cryo-EM structure of the complex, as well as pulldowns and functional assays that indicate DHX34 affects the conformation and activity of RUVBL1-RUVBL2.

Is there any indication of stoichiometry of DHX34 binding beside the triangular shape of the DHX34 density in the map (in Figure 3 and Figure 3—figure supplement 3)? The homology model fit into the map (in Figure 3—figure supplement 3) is unconvincing as there are clear helical densities in the map that appear not to fit any of the homology model helices. Overall, the homology model and experimental map do not appear to be in good agreement. Could more than one DHX34 be binding? The map and model in their current form do not seem sufficient to answer this question.

It seems surprising that the deletion of any of the domains of DHX34 (Figure 3—figure supplement 4C) results in no loss of binding to RUVBL1-RUVBL2. This observation is particularly surprising because it suggests that any domain can be deleted without affecting the folding or soluble expression of DHX34. It is not clear from this experiment that there is a definitive threshold for "loss of binding".

Further, the large variance in signal in the western blot appears to indicate that there could be a dependence on certain domains to bind (for instance RecA1), but the threshold for "no binding" is defined poorly. The authors should likely revise or modify the conclusion that this experiment supports the binding of all domains of DXH34 to RUVBL1-RUVBL2.

It is unclear if the 50% inhibition seen is due to incomplete binding of RUVBL1-RUVBL2 by DHX34 or if that 50% inhibition is an inherent property of the complex between the two.

Reviewer #3:

The work described in this manuscript is potentially of interest but is not ready for publication in its present form for a number of reasons. While it may be difficult (impossible?) for additional lab work to be conducted at present, this should not mean that incomplete studies are suitable for publication.

1) The experiments in Figure 1 Panel D are done by mixing components in solution and allowing them to come to some sort of equilibrium. This can lead to results that are not easy to interpret correctly in the absence of appropriate controls. For example, the amount of RvbL1/2 is not constant across the 2nd gel (compare lanes 10 and 11), which suggests a problem. If the whole RvbL/SMG1/RPAP3/PIH1D1 complex is unable to be bound to the resin, then an amount will remain in solution in samples with RPAP3/PIH1D1. This is not the same result as competing for sites on RvbLs, this is competition between Rvbs and RPAP3-PIH1D1 for a site or sites on SMG1-8-9. Alternatively, a complex between SMG complex or its components and RPAP3-PIH1D1 would not stick to the resin but might prevent binding of RvbLs to SMG1. Pull downs using the FLAG tag would provide a necessary control (i.e. repeating part (C) but in the presence of RPAP3-PIH1D1). However, it would also need to be shown that SMG8-9 does not interact with RPAP3-PIH1D1 as well.

Also, in the final lane (lane 14) all bands are more intense than even the 1:4 ratio lane (lane 13), which could be consistent with a portion of RPAP3/PIH1D1 remaining in solution (e.g. bound to SMG complex or a component of it) when the SMG complex is present. It also needs to be stated somewhere what the concentration on RPAP3-PIH1D1 is in lanes 2, 7, 9 and 14. From the gel band densities in the input it would appear to be 1:4.

Consequently, the data cannot distinguish between at least three different situations (a) competition between SMG1 and RPAP3-PIH1D1 for RvbL hexamer, (b) both binding simultaneously (as discussed by authors), or (c) binding of RPAP3-PIH1D1 to some component of SMG complex that then precludes binding of either to RvbL hexamer. These alternatives need to be distinguished for these data to be of any value.

In fact, since these data have no relevance to the rest of the paper they could be deleted. If they are included, then they need to be improved e.g. by cryoEM to show whether SMG1-Rvb complex is hexamer or dodecamer and/or where SMG1 is located. In their present form the data are not convincing without further validation and/or suitable controls.

2) For the cryoEM study, it is not clear to me why after the Rvb component was masked off so a 4.2Å structure could be obtained, this was not then used to subtract the Rvb density to allow a better local refinement of the DHX34 component? This could improve the DHX34 density dramatically. The observation that the Rvb hexamer density improves so much when the DHX34 component is removed, suggests that there is enough signal from that part to cause the misalignment of the RvbL hexamer so should be sufficient to allow refinement of that part alone, even if that requires several conformational classes to be defined.

3) For the ATPase inhibition experiments there are a number of issues.

First, why do the activity traces begin at 30mins rather than time zero? The rates should be shown from the start of ATP turnover, initiated by, for example, addition of ATP or magnesium after allowing an incubation period for components to form complexes if necessary.

Second, the rates are not linear but are curves. The whole point of the coupled assay is that the ATP is regenerated so remains at a constant level and therefore the rates should be linear unless other factors such as subunit association/disassociation are occurring that mean the system is not at equilibrium. Unless the rates are linear then they are meaningless because they are not steady state. Which part of these curves were measured to estimate the rates? The Materials and methods section suggests an amount after 30 mins was determined, presumably simply a difference over that time? Which time interval? Obviously, this is not accurate or appropriate for a rate that is curving. Interesting, in every assay shown, the curves are getting faster showing the rates are getting quicker as time progresses. This needs to be explained, particularly for DHX34.

Third, the experiments need to address whether it is the Vmax for the reaction that has altered or whether affinity for ATP is different. Furthermore, the structure raises the intriguing possibility that the rate may be halved because only half of the ATPase sites are now active i.e. those in the RvbL1 subunits. The authors have already created the tools to follow this up biochemically by making so-called Walker B mutants for each RvbL subunit. If it is indeed the RvbL2 subunits that are inactivated by the helicase binding, then binding should have no, or lesser, effect on the ATPase activity in the RvbL1/RvbL2EQ hexamer while the RvbL1EQ/RvbL2 hexamer should show a more dramatic effect than wildtype RvbL1/RvbL2 hexamers, or even complete inhibition of activity.

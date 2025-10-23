# Peer review - Round 1

Editors:
- Lucie Delemotte, https://ror.org/026vcq606 KTH Royal Institute of Technology Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75122.sa0](https://doi.org/10.7554/eLife.75122.sa0)

This manuscript explores the mechanisms of permeation and selectivity in the unusual potassium-selective ion channel TMEM175, which lacks a canonical selectivity filter. The study is led by molecular dynamics simulations and free energy calculations, complemented by a cryoEM analysis and electrophysiological recordings. The authors propose a novel, single ion-based mechanism of permeation, together with a partial dehydration-driven selectivity mechanism. This study will appeal to readers interested in the structure and function of ion channels and in molecular mechanisms of ion translocation.


---

# Peer review - Round 1

Editors:
- Lucie Delemotte, https://ror.org/026vcq606 KTH Royal Institute of Technology Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75122.sa1](https://doi.org/10.7554/eLife.75122.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Differential ion dehydration energetics explains selectivity in the non-canonical lysosomal K+ channel TMEM175" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Improved justification of methodological choices.

2) A characterization of the uncertainties on the free energies.

3) A demonstration that a reasonable choice of a different force field would give similar results.

4) A more thorough discussion of agreement (or lack thereof) with other (e.g., experimental) data.

Reviewer #1 (Recommendations for the authors):

1) The Introduction reads as if the authors were the first and only group of determining the structure of a TMEM175 channel. While they were the first for the human isoform, two bacterial isoforms have been structurally characterized and were found to have almost identical pore structure. Those works also formulated hypotheses about the mechanisms of selectivity and gating; both identified the isoleucine constriction. One of these articles is mentioned in passing (Lee et al., 2017, and it's not becoming clear that this was a structural work), while the other one is not cited at all in the entire manuscript (Brunner et al. 2020, eLife 9, the authors cite a preprint of this work in their 2020 article). Also, the only previous theoretical work on the TMEM175 (Rao et al. 2018 in Faraday Discuss. 209) is not cited. With only a low single-digit number papers available on the structure and mechanism of TMEM175, they should be given credit. The same applies for the discussion; a discussion of these new results in relation to the literature is lacking.

2) The section "Improved cryo-EM structures of hTMRM175" is a follow-up to the previous paper (Oh et al., 2020), reporting on a refined on the crystal structure data.

a) It is unclear to me how the new and improved structural model relates to that one from last year. The authors merely mention that it is similar.

b) Were there any changes in the structure or ion position due to the new refinement, or were the now better resolved densities in the expected places? Are the ion binding sites K1-K4 in the same position as in the previous work? Since the notation K1-K4 was dropped (why?), it is very hard for the reader to tell by comparison.

3) Sections "Energetics and mechanism of K+ permeation" and "Differentials in ion dehydration relative to bulk explain selectivity for K+ over Na+"

a) It is not mentioned whether the minima in the energy surfaces or the binding sites observed in the time traces coincide with the ion binding sites in the cryoEM structure. This is important in the light that the authors specifically point out that they made no a priori assumptions about this.

b) The comparison of K+ and Na+ comes a bit short. Although the degree of water depletion is different for K+ and Na+, they end up at the same number of 4 remaining waters. Coordination by the protein is also very similar and it stays unclear whether these two points are relevant for selectivity. Permeation simulations for both K+ and Na+ were performed, but the numerical results (number of permeation events, estimated conductivity) are only given for K+, so the comparison of both ions remains somewhat vague.

c) How appropriate is it to use a constant electric field for a channel with an hourglass pore, where most of the field drops likely over the narrow constriction?

d) The Supplement 2 to Figure 2 is not very helpful. It is very crowded. I was able to pick out some instances where one line seems to cross the entire gap in the middle, which I presume is an ion transition. But I see those both for K+ and Na+. In Figure 3, Na+ is also seen to permeate. How are the statistics of permeation events for K+ and Na+? What is the estimated conduction for 100 mM Na+? I am aware that permeation does not equal selectivity, but I am curious as to why this basic information was left out.

4) Section "Role of the isoleucine constriction in ion selectivity and permeation"

a) Brunner et al. (2020) showed experimentally that not only the isoleucine, but also a stack of polar residues strongly contribute to selectivity in both the bacterial and human isoforms. They also formulated a hypothesis on the gating mechanism. Does this contradict or complement the results of this paper? The hypothetical open state modelled by Rao et al. (2018) is also not mentioned.

b) The new blocker AP-6 seems to be indeed slightly more effective at blocking the mutants than 4-AP. But it seems do drop out of thin air. Neither the design rationale nor whether it is specific to TMEM175 is discussed.

Reviewer #2 (Recommendations for the authors):

1) Error estimates for the calculated free energies and free energy profiles should be provided to see if found differences of ca. 1 kcal/mol are statistically significant. Similarly, the applied field simulations show two permeation events, a rather low number, that should also be treated with care.

2) The differences of ca. 1 kcal/mol are around the accuracy of current force fields for free energy predictions, and the authors are using only one force field (CHARMM) for a somewhat difficult target (an ion in a hydrophobic environment) that was not explicitly parameterized in this force field. Given that in the field of canonical potassium channels force field inaccuracies led to some 20 years long discussion about the permeation mechanisms, I'd suggest to either include an investigation with another force field, or tone down the conclusions (for example that this is a 'proposed permeation mechanism for TMEM175') and discuss potential issues with the current methodology. A recent paper showing a likely too hydrophobic character of the TMEM175 cavity in nonpolarizable force fields (Lynch et al., ACS Nano 2021) will be also of interest here.

3) The authors state in the abstract that the channel is 'capable of permeating K+ ions at the expected rate' and later (page 12) their estimated conductance of human TMEM175 is 0.1-0.5 pS, which the authors comment as "well within the broad range of experimentally measured permeation rates". Can the authors actually provide some numbers here? For example, the bacterial TMEM175 shows a conductance of ca. 70 pS (Brunner et al. eLife 2020) and Slo1 K+ ca. 100 pS (Tao et al. Nature 2017).

4) For clarity, I suggest calculating the conductance for sodium from PMFs the way it was done for potassium; then, compare the K+/Na+ permeability ratios obtained from MD with the experiment. If possible, the error estimates for the permeability ratios should be included as well.

5) Throughout the manuscript, the authors sometimes use the thermodynamic description (i.e. differences in binding free energies between K+ and Na+ ions at a given site) to explain experimentally measured ion selectivity (i.e. permeation rates), that naturally also contains the kinetic part (height of free energy barriers). For example: 'it is useful to keep in mind that dehydration of Na + is much more costly than that of K + ; the penalty for full dehydration is ~18 kcal/mol greater, rendering it a trillion-fold less probable. However, the observed selectivity of biological K+channels against Na+is only 1000-fold or less, implying Na+ establishes much more favorable interactions with the selectivity filters of this kind of K+ channels.'

I'd be careful to directly connect Na+ dehydration penalty with experimentally observed permeation rates, and make a clear distinction in the manuscript between kinetic and thermodynamic selectivity derived from MD. Moreover 'Na + establishes much more favorable interactions with the selectivity filter of this kind of K+ channels' is not only implied but actually shown before, see free energy calculations in Kim et al., PNAS 2011 and Kopec et al. Nat. Chem. 2018.

6) The authors seem to ignore several interesting insights into ion selectivity of TMEM175 channels reported recently by Brunner et al. eLife 2020 – the paper is not even cited. It would be very beneficial for the whole field to include a discussion on how the authors' mechanism and findings agree (or not) with those of Brunner et al.

7) line 78 – table S1 is absent in the manuscript.

8) line 129 – "we detected no evidence of a multi-ion process (Figure 2—figure supplement 2)" – I assume it refers to the number of ions present at the same time at the level of the constriction, however it is not clear from the figure. I suggest defining a "multi-ion" permeation process in the text and put coordinates of SF on Figure 2—figure supplement 2 to make it clear.

9) line 203 – "specifically, the calculations indicate this mutant is about 2-fold less K+ selective than the wild-type channel" – it is not calculated in the manuscript at the moment.

10) lines 177-181 – "We observe that the depletion in the both the first and second solvation shells, relative to bulk numbers, is significantly smaller for Na+than for K+. As will be further discussed below, this relative difference in dehydration energetics likely explains whyTMEM175 is only~30-fold more permeable to K+, even though the bulk water selectivity for Na+is over a trillion-fold." – it may not be clear how the number of water molecules lost during dehydration affects selectivity by itself (rather than the free energy difference between the processes of going from the bulk to the constriction). If it's the case, it should be explained more clearly.

11) Figure 5 Supplementary Figure 3 – the points for the raw currents before adding AP-6 are much more scattered than before 4-AP. What could be the reason for this behavior?

6. line 492 – "To measure currents reduced by AP-6, bath solutions were perfused" – the method for measuring the currents reduced by 4-AP are not described.

12) The starting structure for the simulations is stated to be 6WC9, the previously published structure of the open TMEM175, even though structures with higher resolution were obtained in this study. The reasoning behind using a lower-resolution structure should be provided.

13) Even though the positions of ions as a function of time are shown in Figure 2 Supplementary Figure 2, it may not be enough to estimate the convergence of metadynamics simulations. Can the authors provide an example of the time dependence of the CVs, or the deposited potential, or some other suitable measure for convergence as well?

14) As another control for the metadynamics simulations, would it be possible to run MD of TMEM175 with the potassium ions and water molecules not removed from the initial structure? It could show if there are some energy minima not resolved by metadynamics, and if those ions/water molecules have any effect on the overall behavior of TMEM175. Also, would you expect any side effects from not modelling residues 164-253?

Reviewer #3 (Recommendations for the authors):

1) While the refined static structure of the open channel is discussed in detail, the conformational dynamics of the pore is not: was there any conformational isomerization of side chains? What is the extent of fluctuations in pore radius and relative helix arrangement? Do the apparent kink and tilt of the pore helices fluctuate?

2) There seems to be a discrepancy between the fully-hydrated state of ions in the cryoEM densities (lines 95-97, Figure 1 Suppl. Figure 2) and their partial dehydration in the simulations (Figure 2). This is not a trivial point, since the major finding of the paper is that selective K+ permeation arises from ion (de)solvation effects.

3) Systematic error analysis of the simulation results would strengthen the confidence in the numerical agreement noted above.

4) A broader discussion of the general significance of the findings, including the role of ion desolvation effects and the novelty that a hydrophobic locus controls both gating and selectivity in K+ channels and ion channels in general, would be welcome.

5) The introduction could provide a bit more background. What is the biological function of this protein? Only dysfunction is mentioned.

6) Please specify which atoms were used for the analysis shown in Figure 2 Suppl. Figure 1 (Calpha atoms, etc).

7) It would be useful to computational biophysicists if the authors could clarify the rationale for specific methodological choices. In particular, what are the considerations that presided over the choice of force field? Same question for the collective variable used in the metadynamics simulations.

8) Likewise, why did the authors use the particular functional form of Equation 6 to compute the ion coordination number rather than a simple cut-off distance? Please provide references for that choice if appropriate. Also, please note that brackets are missing in the summations in Eq. 6.

9) Error estimates should be provided systematically. In the current manuscript, they are sometimes vague or non-existent. In particular:

– Please provide data for estimating the convergence for metadynamics; and generally, error estimates as appropriate for all the numerical results.

– The penultimate sentence in the caption of Figure 2 is unclear: "gray profiles represent the same quantity shown in black/blue calculated using only the first or second half of the simulations data."

10) Please provide a reference for variations in the value of the diffusion constant (see lines 453-454).

11) I would recommend including a schematic figure of a thermodynamic cycle to the Discussion for clarity and to highlight the consistency between the two different pathways followed for the DeltaDeltaG calculation (see "Strengths" in public review above).

12) The statement in lines 236-237 seems to imply that the balance of channel-ion, ion-ion, and water-ion interactions controls selective ion permeation. The authors may consider including the effect of channel-water (and arguably also water-water and channel-channel) interactions for the sake of completeness and generality.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Differential ion dehydration energetics explains selectivity in the non-canonical lysosomal K+ channel TMEM175" for further consideration by eLife. Your revised article has been evaluated by Richard Aldrich (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. We anticipate acceptance after these changes have been implemented.

Please address the comments by reviewers 1 and 3, as detailed below.

In addition, regarding the justification of the force field choice, we wish to highlight that claiming that default CHARMM ion parameters from 1994 (Beglov and Roux, 1994) reproduce the relative free-energies of hydration (and thus dehydration) of the alkali cations 'with excellent accuracy' somewhat invalidates next 20 years of ion force field development. When addressing the issue in the article's text, as requested by reviewer 3, please ensure the comment is accurate and well-substantiated, and do not forget to mention possible shortcomings of the chosen force field.

Reviewer #1 (Recommendations for the authors):

I thank the authors for their careful revision of the manuscript. Most of my previous comments have been addressed adequately, except for these two:

Regarding the position of the ion binding sites in the different figures created by different methods: Noting the residues in Figure 2 is certainly helpful (as has already been done in the original manuscript). However, indicating K1-K5 directly as I suggested in my initial review would spare the reader to flip back and forth the figures and comparing each single residue manually. There is still no indication of the binding sites in the time traces of the MD simulations, my request "All figures where this applies: please indicate the location of the binding sites from the structural data" has been ignored by the authors without any comment.

I still strongly suggest amending the figures accordingly as this would make them more accessible.

This comment of mine has maybe been overlooked by the authors: What is the meaning of the numbers in the bracket in Figure 3A? I presume the number of water molecules?

Reviewer #2 (Recommendations for the authors):

All points have been adequately addressed. I recommend the paper for publication.

Reviewer #3 (Recommendations for the authors):

The authors have addressed most of the comments appropriately.

In their response concerning the choice of forcefield, they write: "It could be convincingly argued that a mechanism that relies on dehydration energetics, rather than specific ion-protein interactions, will be reasonably described by this forcefield, as it is in fact parametrized, with excellent accuracy, to reproduce the relative free energies of hydration (and thus dehydration) of the alkali cations." That is the kind of justification that I was hoping for. Please make that convincing argument in the text, including references as needed.

# Peer review - Round 1

Editors:
- Hannes Neuweiler, https://ror.org/00fbnyb24 University of Würzburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79565.sa0](https://doi.org/10.7554/eLife.79565.sa0)

This study uses a broad range of experimental and theoretical biophysical techniques to provide fundamental insights into the conformational pathway of the human dynamin-related GTPase guanylate-binding protein 1 from its resting to an active state. The convincing integrative approach identifies hitherto hidden, dynamic conformers. The work will be of interest to the communities of experimental and theoretical protein biophysics and protein dynamics in signal transduction.


---

# Peer review - Round 1

Editors:
- Hannes Neuweiler, https://ror.org/00fbnyb24 University of Würzburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79565.sa1](https://doi.org/10.7554/eLife.79565.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Integrative dynamic structural biology unveils conformers essential for the oligomerization of a large GTPase" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, including Hannes Neuweiler as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this letter to help you prepare a revised submission.

All four reviewers are in support of publishing your manuscript in a revised form. The reviewers were impressed by the breadth and depth of biophysical methods and analyses applied to the complex problem of deciphering conformational heterogeneity and dynamics of hGBP1. However, as you will see from the reviews below, there are certain concerns that need to be addressed before publication. Required revisions include additional experiments on a farnesylated variant of hGBP1, which is the physiologically relevant form, and the application of GTP as a nucleotide in ligand-binding experiments (see comments from reviewers #3 and #4). It is also suggested that more mechanistic information is contained in the MD simulation data.

We ask you to address all comments of the reviewers with a point-by-point response letter highlighting changes.

Reviewer #1 (Recommendations for the authors):

The manuscript "Integrative dynamic structural biology unveils conformers essential for the oligomerization of a large GTPase" by Peulen et al. reports investigations on the solution structural ensemble and dynamics of human guanylate binding protein 1 (hGBP1) using a combination of complementary biophysical techniques. The authors apply single-molecule fluorescence resonance energy transfer (smFRET) spectroscopy on a number of donor/acceptor fluorophore pairs labeled to engineered cysteine (Cys) residues covering the entire structure of hGBP1. Time-resolved smFRET spectroscopy is used to determine distance distributions and correlation spectroscopy to study dynamics. A subset of double Cys mutants designed for FRET experiments was channeled into double electron-electron resonance (DEER) measurements, complementing the determination of distance distributions. The shape of hGBP1 in solution and its dynamics were further characterized using small-angle x-ray scattering (SAXS) and neutron spin echo (NSE) spectroscopy. In-silico studies were carried out using MD simulations and integrative modelling. The authors arrive at the conclusion of having resolved a novel native-state conformer of hGBP1 together with its time scales of interconversion, which is part of a mechanism of structural remodeling of hGPB1 dimers that form competent precursors in the human host defense system.

Uncovering protein functional mechanisms requires knowledge of both structure and dynamics. Dynamic structural biology is an emerging and important research field. Methods and their applications to observe changes in protein conformation in solution lag behind the ever-increasing number of high-resolution structures solved. The GTPase hGPB1 is a central player in cell-autonomous immunity, which acts by cycling between dimeric, polymeric, and membrane-bound states on infectious pathogens driven by the binding and hydrolysis of GTP. This manuscript shows, within one piece of work, the impressive application of a combination of five different biophysical methods that complement each other in the exploration of spatial and temporal scales of protein conformation. The conformational heterogeneity and dynamics of hGBP1 detected in this work report on a hitherto unknown intermediate state in the conversion of hGBP1 from the resting to an active state. Some uncertainties remain in some of the experimental designs applying extensive mutagenesis and modification.

I have the following comments.

The authors use smFRET to measure distance distributions and apply a subset of the same Cys mutants to also measure distances using DEER. Can the authors comment on the difference in spatial scales probed by both techniques? To which degree are they complementary or does one technique benchmark/test the other?

In Figure 2A, the fit of the crystal structure (blue line) overlays well with the Kratky plot of SAXS data. Still, the authors argue that the crystal structure would disagree with the SAXS data, which appears unreasonable from looking at the fit to the data.

On page 7 the authors argue that observed deviations of distances from the crystal structure and reduced spread, measured by DEER, could originate from a denser packing of the spin labels. How can a packing of spin labels in a solution structure be denser than in that of a crystal, which is optimally packed? The DEER/SAXS result appears to be in conflict with the conformational spread detected by smFRET. Won't a conformationally heterogeneous solution-structural ensemble always represent a more loose structure than that of a crystal? The discrepancies are also mentioned in the paragraph summary, in lines 211-212 on page 10, but appear not to be reconciled.

Wild type hGBP1 contains nine native Cys residues. The authors designed their Cys mutants for FRET and DEER spectroscopy on the background of a construct where all nine native Cys residues were replaced through mutagenesis to prevent their interference with site-specific modification. Replacement of such a high number of native Cys can potentially cause structural/energetic perturbations. Although the authors state in supporting note 1 that these mutations would only weakly affect hGBP1's function, some of the single and double Cys mutants (labeled/unlabeled), shown in Supporting Figure 4A, exhibit significant deviations/reductions of activity. What is the activity of the wild-type protein that contains all native Cys? It would be nice to see the wild-type activity also in the plots in Figure 4A for comparison. Can the authors exclude that their modifications induce conformational heterogeneity detected in smFRET experiments (the M1/M2 conformational ensemble)?

As a result of smFRET correlation spectroscopy, the authors find that dynamics in the middle and effector domain are an order of magnitude faster (~14 µs) than in the LG GTPase domain (~140 µs), highlighted in Figure 3E. This is an interesting finding. Since the secondary structure is the same throughout all hGBP1 domains one may have expected similarity in kinetics. The detected differences may report on functional motions. smFRET correlation spectroscopy covers the ns-µs time scale, which is indeed the relevant scale of motion of protein secondary and tertiary structure. NSE spectroscopy nicely complements the faster time scale of up to 200 ns. This faster time scale is also covered by MD simulations. Can we learn more details about the onset of the µs conformational changes seen in experiments from the computed atomistic MD data?

Collective motions of protein domains are often slower than ms, in general. There may thus be functionally relevant motions of hGBP1 that were missed out. Can the authors comment on such potential motions and how they could be detected?

The authors applied GDP-AlFx to generate a nucleotide-bound hGBP1 construct that remained monomeric under solution conditions of smFRET spectroscopy. It would be interesting to see how dimerization influences the measured hGBP1 dynamics. This could be studied by smFRET through the application of an excess of unlabeled hGBP1 to fluorescently modified, GDP-AlFx-bound hGBP1 construct. Have the authors considered such experiments?

Binding of GMP is known to stabilize the compact resting state of hGBP1 (reviewed in Kutsch & Coers, FEBS J. 2021, 288, 5826-5849). Have the authors considered experiments using GMP as a ligand? Such experiments would be interesting because one would expect that binding of GMP stalls the dynamics of hGBP1 and thus the M1/M2 motions. Experiments involving the binding of GMP could provide insights into the functional relevance of the detected M1/M2 motions.

Model (iii), "dimer induced flexibility", in Figure 1B seems to be ruled out by the fact that the binding of GTP triggers the opening of GBP1 (reviewed in Kutsch & Coers, FEBS J. 2021, 288, 5826-5849).

The last sentence of the abstract aims to highlight the conclusions of the work, which is deciphering intrinsic flexibility and conformational heterogeneity of hGBP1, but also mentions the GTP-triggered association of GTPase domains, assembly-dependent GTP hydrolysis, and functional design principles that control hGBP1's reversible oligomerization reported by others.

Reviewer #2 (Recommendations for the authors):

In their work, Peulen et al. investigate the conformational flexibility of the GTPase hGBP1, a dynamin-like protein responsible for the membrane disruption of intracellular parasites. The work was motivated by the apparent disagreement of the X-ray structure of the monomer with the previous FRET- and DEER experiments that suggested at least two conformations of the protein in its GTP-induced dimeric state. This disagreement indicates substantial flexibility, either in the monomeric state, which might or might not be induced by ligand binding or in the dimer. To understand the origin of this flexibility, the authors combined an impressive number of techniques, SAXS, NSE (neutron-spin echo spectroscopy), EPR, and FRET, in an integrative approach to unravel the structures and interconversion timescales of conformers in the apo- and holo-form of the protein. The authors found that at least two conformers (M1 and M2) interconvert at timescales from a few up to hundreds of microseconds. Integrative modeling combining the experimental results with rigid-body docking and structural refinement of a coarse-grained model of hGB1, following the previously published protocol of the authors (Dimura et al. 2020 Nature Comms, 11, 5394), was used to determine low-resolution models of M1 and M2. These models give rise to two potential dimers M1:M2 and M1:M1. The structural differences in M1 and M2 suggested by this integrative approach are substantial and indicate two different binding sites of the α12/13 helices on the ligand-binding (LG) domain.

In some parts, the article is written in a rather technical style, which might complicate an understanding by readers unfamiliar with the techniques and approaches (structural biologists for instance). In addition, I have a number of technical comments that the authors should address.

1. Figure 1B of the manuscript gives the impression that the authors investigate flexibility in the apo- and holo-form of the monomer but also in the dimer. I was therefore wondering why the authors excluded experiments in the presence of an excess of unlabeled monomer to investigate flexibility in the dimer. Does the formation of higher oligomers in the presence of GTP and high protein concentrations prevent such experiments?

2. Why are M1 and M2 not seen in the experimental DEER distance distributions, e.g., in the Q344C/A496C variant? Do the conformations re-equilibrate during the fast cooling period required in EPR? In fact, all EPR distributions are unimodal (p. 7, and Supplementary Figure 2), which is difficult to understand given the evidence for the existence of M1 and M2 from TCSPC and MFD histograms.

3. I was a bit puzzled by the eTCSPC analysis. The authors find bi-exponential lifetime decays for the donor in the absence of an acceptor, which is explained by the environment of the dyes after labeling. This indicates the presence of conformers with different degrees of dynamic donor quenching and hence different radiative rates of the donor dye. Yet, the combination of eq. 9 and 10 in the Supporting Information does not account for the propagation of these differences in the transfer rate. In fact, eq. 10 indicates that the same radiative rate (k0) was used to determine distance distributions. Although this approach is convenient as it allows εD to be obtained by the ratio of donor decay in the presence of the acceptor and in the absence of the acceptor, I am not yet convinced the approach is justified. If

fD0 = ∑ xD(i) exp[-kD(i) t]

is the donor decay in the absence of the acceptor (sum goes over i components), I'd expected that the donor decay in the presence of acceptor is

fDA = ∑{xD exp[-kD(i) t] ∫exp[-kT(i,r) t]dr} (A)

with kT(i,r)=kD(i) (R0/r)^6 being the component-dependent transfer rate and r is the donor-acceptor distance. Instead, the authors used eq. 9 and 10, which give

fDA = {∑xD exp[-kD(i) t] } ∫exp[-kT(r) t]dr (B)

with kT(r)=kD (R0/r)^6 with kD = k0 = 1⁄τ0.

Clearly, A and B are two very different scenarios. In the latter, εD can simply be determined via fDA / fD0, but not in the former. Hence, if expression A is more adequate, a MEM-analysis of fDA / fD0 might provide false results.

4. Related to point 3, the sub-population-specific TCSPC decays in the single-molecule FRET experiments seem to indicate single-exponential decays for donor-only molecules, at least by visual inspection (see Supporting Figure 3B). How is this reconciled with the double-exponential decays found for singly donor labeled hGBP1 in the ensemble TCSPC experiments?

5. Have the authors checked whether static quenching of the acceptor (or donor) affects the ratiometric FRET efficiencies? Direct excitation of the acceptor in a (anti)-bunching experiment can reveal the significance of static quenching.

6. Supporting Figure 4: Panels (C) and (D) are switched in the caption.

7. It is known that D2O (used in the EPR experiment) can affect protein stabilities and flexibilities (Makhadatze et al. 1995 Nat Struct Biol, 2, 852 / Cioni & Strambini (2002) Biophys J, 82, 3246 / Pica & Graziano (2017) Biopolymers, 109 and many more). Did the authors find differences in the populations and or dynamics of the state between the two solvents? Controls with MFD should be straightforward.

Reviewer #3 (Recommendations for the authors):

In their work, Peulen et al. applied an integrative modeling approach to scrutinize the conformational dynamics of the human guanylate binding protein (hGBP1), which is an essential part of the cell's intrinsic immune response to intracellular parasites. The assortment of biophysical methods used is striking – the fact that the authors have been able to plan and assign experiments/simulations, collect and process data, and integrate the diverse data into a meta-analysis workflow to derive molecular candidates for hGBP1 conformers is exemplary and not self-evident. This has allowed deriving important conclusions about the mechanism of hGBP1 self-assembly. In particular, the authors propose that hGBP1 undergoes GTP-independent conformational transitions on the µs-timescale between at least two conformational states, which is essential for the slower, GTP-dependent hGBP1 oligomerization. It is highly unlikely that these conclusions could ever have been made without the cross-disciplinary scheme presented by the authors. On the other hand, it is also crucial to note that the study has to incorporate several caveats that will be important when placing the proposed oligomerization pathway (Figure 6 of the paper) in a broader biological context and that several clarifications will need to be provided to delineate the conclusions based on measurements/calculations actually done by the authors from speculations based on physics intuition and/or other people's work.

As mentioned in the public review, I generally consider the work done by the authors timely and solid and would highly recommend it for publication in eLife, provided that a number of questions are addressed to improve the scientific rigor.

- Page 12: "The measure Deff(q) agrees well with the theoretical calculations, accounting for rigid body diffusion alone".

Can the authors provide a more objective way to assess the data-theory agreement in Figure 3A? The agreement doesn't really look good around q = 0.5/nm. It is not clear how large "a significant additional contribution of internal protein dynamics" should be to be visible as a clear deviation from the rigid-body diffusion.

- Page 13: fFCS experiments.

What does "treated as a single dataset" means for the 48 fFCS curves? The average fFCS curve? A multivariate fit to 48-dimensional data? Please clarify in the main text.

It is not clear why a 3-state model with varying amplitudes was used to recover the three correlation times shown in Figure 3C, D. The authors provide no justification for why 3 states are actually sufficient or insufficient. One way to address this could be to set up a Bayesian inference optimization and use the Bayesian-Schwarz criterion to discriminate between models with different parameter numbers.

- Why was the api-holo comparison done only for the kinetic measurements? Can the authors rule out any effects of GTP binding on the equilibrium quantities measured in Figure 2? The statement that the M1-M2 transition is GTP-independent is only complete and valid if both kinetic and equilibrium parameters of these systems are demonstrated to remain unchanged upon GTP binding.

- Why did the authors use a GTP-analog for their measurements? At picomolar concentrations of hGBP1 were monomeric (page 13, lines 297-298). Therefore, it wouldn't dimerize even in the presence of GTP at that concentration.

- The authors don't mention which version of aMD was used: the one that lowers the kinetic barriers or the one that raises the energy valleys? The use of aMD requires an explanation of how it might affect conclusions about kinetics (the authors do perform autocorrelation analysis).

- Potential GTP-dependent effects on the simulated hGBP1 are not sufficiently discussed. The RMSD distributions look different for apo vs. holo (Supp. Figure 6A). The average correlation times in the presence and absence of GTP differ as well, but the author seems to not take this result into consideration, nor do they comment on why this may or may not be statistically insignificant. Overall, the MD data contains much more valuable information than what the authors present. For example, one could assess the inter-domain correlations within hGBP1 as a function of the nucleotide state or compare the simulated data to smFRET measurements (of course, for the main conformer M1 only). Just to throw in a few ideas.

- Page 18: "indicative for a frustrated potential energy landscape". Do the authors mean a ragged landscape with several substrates and multiple kinetic barriers?

- As far as I can tell, the dimerization kinetics/thermodynamics were not assessed in the study because of the low hGBP1 concentrations necessary to keep it monomeric. It is not clear where the data comes from that supports the middle part of Figure 6 (D1 vs D2 states).

- Along the same lines, the claim that "ligand binding leads to dimerization because of the increased affinity between the LG domain" (page 20) doesn't seem to be supported by data at all.

- Also, what do the authors actually mean by "intrinsic flexibility"? When the widths of the M1/M2 potential wells are changed? When the transition rate between M1 and M2 is increased? When the equilibrium populations of M1 and M2 are changed? Or all of these at the same time?

- Page 21: "Upon addition of GTP the LG domain can bind to another promoter whilst the conformational dynamics appear to remain unchanged" and "As the M1:M2 dimer has a higher stability, …". Again, not clear whether the authors are referring to their own data, which I, unfortunately, wasn't able to find.

Overall, there are many places in the conclusions section where the actual findings by the authors should be clearly delineated from other people's work and/or physics intuition. This is very puzzling.

Reviewer #4 (Recommendations for the authors):

Peulen et al. provide a well-drafted manuscript describing dynamic conformers of the dynamin-related GBP1 GTPase. Using integrative modelling with DEER, FRET, and SAXS data, the authors identify at least two conformational states M1 and M2 in nucleotide-free GBP1 distinguished by a rotation around a pivot point between the GTPase and middle domain. The structural data are used to interpret the GTP-induced dimerization pathway, suggesting that intrinsic conformational flexibility between the GTPase and GTPase effector domain (GED) is a prerequisite for forming a bridged GBP1 dimer.

The manuscript provides and integrates a vast amount of structural and biophysical data that appear overall convincing. The chosen approach is of general interest since there is only a limited example combining biophysical approaches in such a systematic fashion to identify dynamic conformers of multi-domain molecular assemblies. Unfortunately, the authors appear to have used only non-farnesylated GBP1 for their studies while native GBP1 is C-terminally farnesylated. Consequently, it is not yet clear whether the observed conformational flexibility in the C-terminal GED is an intrinsic feature of GBP1 or a consequence of the missing post-translational modification. This and a few other minor issues should still be addressed to support the claim of the biological relevance of this study.

Figure 2, Figure 6, supporting Figure 2-4, farnesylation

In the cell, GBP1 is constitutively C-terminally farnesylated and the farnesyl moiety is known to bind into a pocket of the helical domains. If I understand Figure 6 correctly, the authors have used only non-farnesylated protein to characterize conformational flexibility in GBP1 (please mention the used construct explicitly in the Methods). Thus, it cannot be excluded that the observed flexibility in the C-terminal GED is related to the missing farnesyl moiety and may therefore not be an intrinsic property of the farnesylated protein. To exclude this scenario, farnesylated protein should be used to repeat at least a few of the DEER or FRET measurements in which two conformational states can clearly be discerned for the non-farnesylated protein (for example, Q344C/A496C and A496C/V540C). The two boxes 'non-farnesylated' and 'farnesylated' in Figure 6 are confusing since the relevant protein species in the cell is obviously farnesylated throughout the assembly.

Figure 3D, GDP-AlFx

AlFx is known to bind to GTPases when a stable transition state is achieved. For small GTPases, GDP-AlFx binding was demonstrated in the presence of GTPase activating proteins (GAP), while I am not aware of any study demonstrating GDP-AlFx-binding in the absence of a GAP. Accordingly, one would assume that GBP1 binds GDP-AlFx only in the context of a catalytic dimer, e.g. likely not at a protein concentration of 20 pM, as shown in Figure 3D. In this case, the measurements would represent the GDP-bound form, which would also explain the missing effect of nucleotide on protein dynamics. The authors should repeat the measurements for the selected three mutants in the presence of the relevant substrate GTP-Mg2+. At 20 pM protein concentration, GTP hydrolysis should be slow enough to allow FRET assays in the constant presence of GTP.

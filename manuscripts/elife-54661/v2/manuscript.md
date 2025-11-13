# Local frustration determines loop opening during the catalytic cycle of an oxidoreductase

## Authors

- Lukas S Stelzl<sup>1</sup> ([ORCID: 0000-0002-5348-0277](https://orcid.org/0000-0002-5348-0277))
- Despoina AI Mavridou<sup>2</sup> ([ORCID: 0000-0002-7449-1151](https://orcid.org/0000-0002-7449-1151))
- Emmanuel Saridakis<sup>3</sup>
- Diego Gonzalez<sup>4</sup>
- Andrew J Baldwin<sup>5</sup> ([ORCID: 0000-0001-7579-8844](https://orcid.org/0000-0001-7579-8844))
- Stuart J Ferguson<sup>1</sup>
- Mark SP Sansom<sup>1</sup> ([ORCID: 0000-0001-6360-7959](https://orcid.org/0000-0001-6360-7959)) †
- Christina Redfield<sup>1</sup> ([ORCID: 0000-0001-7297-7708](https://orcid.org/0000-0001-7297-7708)) †

### Affiliations

1. Department of Biochemistry, University of Oxford Oxford United Kingdom
2. Department of Molecular Biosciences, University of Texas at Austin Austin United States
3. Institute of Nanoscience and Nanotechnology, NCSR Demokritos Athens Greece
4. Laboratoire de Microbiologie, Institut de Biologie, Université de Neuchâtel Neuchâtel Switzerland
5. Department of Chemistry, Physical and Theoretical Chemistry Laboratory, University of Oxford Oxford United Kingdom

† Corresponding author

## Abstract

Local structural frustration, the existence of mutually exclusive competing interactions, may explain why some proteins are dynamic while others are rigid. Frustration is thought to underpin biomolecular recognition and the flexibility of protein-binding sites. Here, we show how a small chemical modification, the oxidation of two cysteine thiols to a disulfide bond, during the catalytic cycle of the N-terminal domain of the key bacterial oxidoreductase DsbD (nDsbD), introduces frustration ultimately influencing protein function. In oxidized nDsbD, local frustration disrupts the packing of the protective cap-loop region against the active site allowing loop opening. By contrast, in reduced nDsbD the cap loop is rigid, always protecting the active-site thiols from the oxidizing environment of the periplasm. Our results point toward an intricate coupling between the dynamics of the active-site cysteines and of the cap loop which modulates the association reactions of nDsbD with its partners resulting in optimized protein function.

## Introduction

Molecular recognition, the specific non-covalent interaction between two or more molecules, underpins all biological processes. During protein-protein association, molecular recognition often depends on conformational changes in one or both of the protein partners. Important insight into the mechanisms of molecular recognition has come from NMR experiments probing dynamics on a range of timescales (Baldwin and Kay, 2009; Sekhar et al., 2018). NMR, and especially the relaxation dispersion method, is unique in providing not only kinetic, but also structural information about the conformational changes leading up to protein association (Lange et al., 2008; Sugase et al., 2007). In some cases, molecular dynamics (MD) simulations have been successfully paired with NMR experiments (Olsson and Noé, 2017; Pan et al., 2019; Robustelli et al., 2012; Zhang et al., 2016; Wang et al., 2016; Stiller et al., 2019) to provide a more complete picture of the conformational dynamics landscape (Paul et al., 2017; Peters and de Groot, 2012; Robustelli et al., 2013). However, we still do not have a general understanding of the molecular determinants that enable some proteins to access their bound-like conformation before encountering their binding partners in a 'conformational-selection' mechanism, while others undergo conformational change only after recognizing their ligands in an 'induced-fit' mechanism (Boehr et al., 2009).

Local structural frustration (Baldwin et al., 2011b; Ferreiro et al., 2018; Freiberger et al., 2019), the existence of multiple favorable interactions which cannot be satisfied at the same time, has emerged as an important concept in rationalizing why some regions in proteins undergo conformational changes in the absence of a binding partner (Ferreiro et al., 2007; Ferreiro et al., 2011; Ferreiro et al., 2014). In general, globular proteins are overall minimally frustrated and, thus, adopt well-defined native structures. Nonetheless, the existence of a set of competing local interactions can establish a dynamic equilibrium between distinct conformational states. Locally frustrated interactions (Jenik et al., 2012) are indeed more common for residues located in binding interfaces of protein complexes (Ferreiro et al., 2007) and can play an important role in determining which parts of these proteins are flexible. However, very few studies (Danielsson et al., 2013; Das and Plotkin, 2013) have analyzed in atomic detail how frustration shapes conformational dynamics and, therefore, can enable protein association. This lack of understanding hampers the exploitation of local frustration, and associated dynamic equilibria, as a design principle for generating optimal protein constructs that could be used in the production of synthetic molecular machines.

To investigate the role of frustration in conformational dynamics, we have used as a model system the N-terminal domain of the transmembrane protein DsbD (nDsbD), a key oxidoreductase in the periplasm of Gram-negative bacteria. DsbD is a three-domain membrane protein (Figure 1A) which acquires two electrons from cytoplasmic thioredoxin and, through a series of thiol-disulfide exchange reactions involving pairs of conserved cysteine residues, transfers these electrons to multiple periplasmic pathways (Figure 1B/C; Cho and Collet, 2013; Depuydt et al., 2009). nDsbD, the last component of the DsbD thiol-disulfide cascade, is essentially the redox interaction hub in the bacterial periplasm; it first interacts with the C-terminal domain of DsbD (cDsbD) to acquire the electrons provided by cytoplasmic thioredoxin and then passes these on to several globular periplasmic proteins, including DsbC, CcmG and DsbG (Figure 1A/B; Stirnimann et al., 2006). All these thiol-disulfide exchange steps involve close interactions between nDsbD and its binding partners, which are essential so that their functional cysteine pairs can come into proximity leading to electron transfer (Haebel et al., 2002; Mavridou et al., 2011). As nDsbD is essentially a reductase in the oxidative environment of the bacterial periplasm, its interactions with its multiple partners must happen in an optimal manner, making this protein an ideal model system to study.

![Figure 1.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig1-v2.jpg)

**Figure 1.:** (A) DsbD comprises a central domain with eight transmembrane helices (tmDsbD) and two periplasmic globular domains (nDsbD and cDsbD). The electron transfer pathway from thioredoxin (Trx) to periplasmic partner proteins is shown. cDsbD, DsbC, CcmG and DsbG have a thioredoxin fold (circle), typical of thiol-disulfide oxidoreductases, while nDsbD adopts an immunoglobulin fold (square). nDsbD and cDsbD are shown in cyan and grey, respectively. (B) Electron transfer reactions involving DsbD are shown. Two electrons and two H+ are transferred in each step. Trxred reduces the disulfide bond in tmDsbDox, tmDsbDred then reduces cDsbDox, and cDsbDred subsequently reduces nDsbDox. Oxidized DsbC, CcmG and DsbG subsequently accept electrons from nDsbDred. (C) Schematic representation of the thiol-disulfide exchange reaction (bimolecular nucleophilic substitution) between cDsbD and nDsbD. (D) The central panels illustrate two possible mechanisms mediating cap loop opening in the formation of the nDsbD-cDsbD complex. In the upper scheme, a steric clash upon binding induces cap loop opening. In the lower scheme, the sampling of an open conformation by nDsbD allows formation of the complex without steric clashes. nDsbDox is illustrated on the left (PDB: 1L6P); the cap loop (residues 68–72), which covers the active site is in teal. F70 (stick and surface representation) shields the active-site disulfide bond (yellow) in this closed conformation. The nDsbD cap loop adopts an open conformation in the complex between nDsbD and cDsbD (PDB: 1VRS), shown on the right, allowing interaction of the cysteine residues of the two domains. All structures in this and other figures were rendered in Pymol (Version 2.3.5, Schrödinger, LLC) unless otherwise indicated.

X-ray structures show that the cap-loop region of nDsbD, containing residues D68-E69-F70-Y71-G72, plays a key role in the association reactions of this domain with its binding partners (Haebel et al., 2002; Rozhkova et al., 2004; Stirnimann et al., 2005). The catalytic subdomain of nDsbD is inserted at one end of its immunoglobulin (Ig) fold with the two active-site cysteines, C103 and C109, located on opposite strands of a β-hairpin (Figure 1D). For both oxidized and reduced nDsbD (with and without a C103-C109 disulfide bond, respectively), the active-site cysteines are shielded by the cap-loop region which adopts a closed conformation (Figure 1D; Haebel et al., 2002; Mavridou et al., 2011; Goulding et al., 2002). Strikingly, all structures of nDsbD in complex with its binding partners, cDsbD, DsbC, and CcmG (Haebel et al., 2002; Rozhkova et al., 2004; Stirnimann et al., 2005), show the cap loop in an open conformation that allows interaction between the cysteine pairs of the two proteins (Figure 1D; Haebel et al., 2002; Stirnimann et al., 2005; Rozhkova and Glockshuber, 2007).

While these X-ray structures provide static snapshots of the closed and open states of the cap loop, they do not offer any insight into the mechanism of loop opening that is essential for the function of nDsbD. To understand the drivers of this conformational change, two hypotheses regarding the solution state of nDsbD need to be examined (Figure 1D). Firstly, it is possible that the cap loop only opens when nDsbD encounters its binding partners, in an 'induced-fit' mechanism consistent with the hypothesized protective role of this region of the protein (Goulding et al., 2002). Secondly, it is also plausible that in solution the cap loop is flexible so that it samples open states, and thus allows binding of partner proteins via 'conformational selection' (Boehr et al., 2009). Of course, if the cap loop did open in the absence of a binding partner, that could compromise the transfer of electrons in an environment as oxidizing as the periplasm, and particularly through the action of the strong oxidase DsbA (Denoncin and Collet, 2013). Therefore, one could hypothesize that a protective role for the cap loop would be more important in reduced nDsbD (nDsbDred), raising the question of whether nDsbD interacts with its partners via different loop-opening mechanisms depending on its oxidation state. In this scenario, the pair of cysteines could modulate the conformational ensemble of nDsbD as has been hinted at by structural bioinformatics (Schmidt et al., 2006; Zhou et al., 2014).

Here, we use both state-of-the-art NMR experiments and MD simulations to describe different behaviors for the cap loop depending on the oxidation state of nDsbD. The atomic-scale insight afforded by these two methods reveals how the disulfide bond introduces local frustration specifically in oxidized nDsbD (nDsbDox), allowing the cap loop and active site in nDsbDox to sample open bound-like conformations in the absence of a binding partner. Our observations have implications not only for the function of DsbD, but more broadly for the role of local frustration in ensuring optimized protein-protein interactions.

## Results and discussion

### The solution structure of nDsbD as probed by NMR

NMR experiments demonstrate that the cap loop has an important protective role in shielding the active-site cysteines of nDsbD. For nDsbDox, we showed previously that reduction of the disulfide bond by dithiothreitol (DTT) is very slow, with only 50% of nDsbDox reduced after ~2 hr. This indicates that the cap loop shields C103 and C109 from the reducing agent (Mavridou et al., 2011). In addition, NMR spectra for nDsbDred collected between pH 6 and 11 show no change in cysteine Cβ chemical shifts. This indicates that the pKa of C109, the cysteine residue thought to initiate reductant transfer (Rozhkova et al., 2004), is above 11, thus making it unreactive in isolated nDsbDred. This suggests that shielding of the active site by the cap loop in nDsbDred protects C103 and C109 from non-cognate reactions in the oxidizing environment of the periplasm.

The cap loop shields the active site by adopting a closed conformation as in the X-ray structures of oxidized (PDB: 1L6P and 1JPE) (Haebel et al., 2002; Goulding et al., 2002) and reduced (PDB: 3PFU) (Mavridou et al., 2011) nDsbD. These structures are very similar to each other with pairwise Cα RMSDs for residues 12 to 122 of less than 0.15 Å. To probe the solution structure of oxidized and reduced nDsbD, we measured 1H-15N residual dipolar couplings (RDCs), which are sensitive reporters of protein structure (Figure 2—figure supplement 1 and Figure 2—figure supplement 1—source data 1). Analysis of these data indicates that the orientation of the active-site/cap-loop residues relative to the core β-sandwich of both oxidized and reduced nDsbD in solution is well described by the X-ray structures in which the cap loop adopts a closed conformation. Nevertheless, the cap loop must open to expose the active site in order for nDsbD to carry out its biological function.

### NMR spin-relaxation experiments and model-free analysis

To investigate whether the cap loop is flexible in solution and whether the dynamic behavior of the loop differs in the two oxidation states, we studied the fast time-scale (ps-ns) dynamics of nDsbD using NMR relaxation experiments. 15N relaxation experiments, analyzed using the ‘model-free’ approach (Lipari and Szabo, 1982a; Lipari and Szabo, 1982b), showed that most of the protein backbone is relatively rigid. The majority of order parameters (S2) for the backbone amide bonds are above 0.8 (Figure 2). The N- and C-terminal regions of nDsbD gave very low S2 values and are clearly disordered in solution. Other residues with order parameters below 0.75 are located in loops or at the start or end of elements of secondary structure, but are not clustered in a specific region. For example, lower order parameters are observed for residues 57 and 58 in both redox states. These residues are located in a long 'loop' parallel to the core β-sandwich but not identified as a β-strand due to the absence of hydrogen bonds.

![Figure 2.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig2-v2.jpg)

**Figure 2.:** The experimental order parameters for reduced and oxidized nDsbD are shown in blue (A) and red (B), respectively. The average order parameters calculated from the combined 1 μs MD simulation ensembles starting from closed structures for reduced (A) and oxidized (B) nDsbD are shown in black. Errors in S2 were determined by Monte Carlo simulations (experiment) and resampling of S2 from trajectory segments (MD simulations). The simulations of both oxidized and reduced nDsbD reproduced even subtle features of sequence-dependent variation of S2 values. For example, S2 values for residues 57–60 were lowered in both experiment and simulation. These residues are not part of the regular secondary structure of the Ig fold in both the X-ray structures of nDsbD and in the MD simulations.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** To probe the solution structure of nDsbD, 1H-15N RDCs, which are sensitive reporters of protein structure, were measured for (A) reduced and (B) oxidized nDsbD. Experimental RDCs are indicated by the open circles while RDCs calculated by fitting the alignment tensor to the X-ray structure (PDB:3PFU for reduced and PDB:1L6P for oxidized nDsbD) are indicated by the solid line. For most residues, very similar RDCs were measured for reduced and oxidized nDsbD. The small RDCs measured for residues 1–8 and 126–135 in both redox states are likely to indicate conformational dynamics that lead to averaging of these RDCs; values for most of these residues cannot be predicted from the X-ray structures because electron density is not observed before residue eight and after residue 125 in the structures. By contrast, the RDCs for the core β-sandwich are accurately predicted by the X-ray structures; Q values of 0.17 and 0.21 are obtained for reduced and oxidized nDsbD, respectively (Figure 2—figure supplement 1—source data 1). When fits are carried out for residues 12–122, which includes the core β-sandwich and the active-site/cap-loop residues, Q values of 0.19 and 0.24 are obtained for reduced and oxidized nDsbD, respectively (Figure 2—figure supplement 1—source data 1). The similar Q values for the two sets of RDCs suggest that the orientation of the active-site/cap-loop residues relative to the core β-sandwich of both reduced and oxidized nDsbD in solution is described well by the X-ray structures in which the cap loop adopts a closed conformation. Experimental RDCs are compared with RDCs calculated from MD simulations for (C) reduced and (D) oxidized nDsbD. For both nDsbDred and nDsbDox, the agreement between calculated and experimental RDCs improved for the 1μs MD ensemble compared to the static X-ray structures. It is also interesting to note that the RDCs for residues 106 and 108, which gave poor agreement in the fits to the static X-ray structures due to crystal contacts, agree well with the values predicted from the MD simulations. Errors in RDCs calculated from the MD simulations were determined using resampling of RDCs from trajectory segments.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Comparison of experimental {1H}-15N heteronuclear NOE values for nDsbDred (blue) and nDsbDox (red). (B) Comparison of order parameters (S2) derived from model-free analysis of 15N relaxation data for nDsbDred (blue) and nDsbDox (red). (C) Comparison of order parameters (S2) derived from the MD simulations for nDsbDred (blue) and nDsbDox (red). Errors in the experimental {1H}-15N heteronuclear NOE and the S2 order parameters were determined as described previously using Monte Carlo error estimation (Smith et al., 2013).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** The extent of the fast-time scale (ps-ns) dynamics observed experimentally by NMR is on the whole correctly reproduced by the MD simulations. The root mean-square deviation (RMSD) between the order parameters detemined from model-free analysis and from the simulations is 0.08 for both reduced and oxidized nDsbD. The N- and C-termini were very flexible, but most residues in the folded segments of nDsbD were well ordered with S2 >0.80, which agrees with experiment. Errors in S2 calculated from the MD simulations were determined using resampling of S2 from trajectory segments.

In both oxidation states, the S2 values for the cap-loop region are similar to the rest of the folded protein. Thus, on average, the cap loop of nDsbD does not undergo large amplitude motions on a fast timescale, which means that the active-site cysteines remain shielded. However, close inspection of the {1H}-15N NOE values for the cap-loop residues in oxidized and reduced nDsbD does show a clear difference between the two oxidation states (Figure 2—figure supplement 2 and Figure 2—figure supplement 2—source data 1). In nDsbDox, the residues between V64 and G72 have NOE values at or below 0.7, while in nDsbDred there is only one residue with an NOE value at or below 0.7. The consequence of this difference is that the majority of amino acids in this region of nDsbDox require a more complex model (with the τe parameter ranging from ~50 to 350 ps) to obtain a satisfactory fit in the analysis, in contrast to the majority of residues in nDsbDred which can be fitted with the simpler S2 only model (with a τe value of faster than ~10 ps). Therefore, although the amplitude of motions of cap-loop residues is limited and does not appear to differ very much between the two oxidation states, the timescale of the fast dynamics, as described by the approach of Lipari and Szabo, does differ.

### Molecular dynamics simulations

To evaluate the differences between the conformational dynamics of reduced and oxidized nDsbD with atomic resolution, molecular dynamics (MD) simulations were employed. We tracked the orientation of the cap loop relative to the active site in the generated MD trajectories, by calculating the distance between the center of the aromatic ring of F70 and the sulfur atom of C109. Multiple simulations, for a total of 1 μs, were started from the X-ray structure of reduced nDsbD (3PFU). The distance between F70 and C109 remained close to the value in the X-ray structure of nDsbDred, as shown for sample trajectories in Figure 3A and B (Figure 3—figure supplement 1). In addition, C103 and C109 remained largely shielded, as assessed by the solvent accessible surface area (SASA) (Figure 3—figure supplement 2). Therefore, opening of the cap loop in nDsbDred was not observed in 1 μs of simulation time (Figure 3D and Figure 3—figure supplement 1). This confirms that the cap loop protects the active-site cysteines of nDsbDred from the oxidizing environment of the periplasm.

![Figure 3.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig3-v2.jpg)

**Figure 3.:** The conformational state of the cap loop was followed by tracking the distance between the center of the aromatic ring of F70 and the sulfur atom of C109. The solid and dashed lines at ~3–4 and~11 Å show the F70 ring to C109 Sγ distance in the closed (3PFU/1L6P) and open (1VRS) X-ray structures, respectively. The cap loop remains stably closed in simulations of nDsbDred, as shown in (A) and (B). The cap loop in nDsbDred closes within 3 ns for a simulation started from an open conformation based on the 1VRS structure (C). The 1 μs simulation ensemble for nDsbDred shows a closed conformation of F70 relative to C109 (D). The cap loop conformation is more flexible in simulations of nDsbDox; in some simulations it remains closed (E) while in others the loop opens (F). The loop closes in some simulations of nDsbDox started from an open conformation (G). Overall, the 1 μs simulation ensemble for nDsbDox shows a preference for the closed conformation of F70 relative to C109, with open conformations sampled relatively rarely (H).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Data for an additional 600 ns of MD simulations, not illustrated in Figure 3, are shown for reduced (left) and oxidized (right) nDsbD. The conformational state of the cap loop was followed by tracking the distance between the center of the aromatic ring of F70 and the sulfur atom of C109. The solid and dashed lines at ~3–4 and ~11 Å show the F70 ring to C109 Sγ distance in the closed (3PFU/1L6P) and open (1VRS) X-ray structures, respectively. The cap loop remains stably closed in simulations of nDsbDred (left). The cap loop conformation is more flexible in simulations of nDsbDox (right) showing several transient and longer-lived opening events. Data for ten 20 ns simulations are combined in the bottom panels; the vertical grey lines show the starting and ending points of these shorter 20 ns simulations.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** SASA is plotted for the aromatic cap loop residues F70 and Y71 and for the Sγ of C103 and C109 in simulations of nDsbDred (left) and nDsbDox (right). The Sγ of C103 and C109 remain largely shielded from solvent in nDsbDred but become more exposed during loop opening in nDsbDox. The SASA of the aromatic rings of F70 and Y71 also increases during the main loop opening event between 80 and 200 ns. These data are derived from the trajectories shown in Figure 3A and F.

By contrast, nDsbDox showed more complex dynamics in the 1 μs of simulations launched from the closed 1L6P X-ray structure (Figure 3 and Figure 3—figure supplement 1). In one 200-ns simulation the cap loop remained closed (Figure 3E), only showing occasional fluctuations. In a different simulation the fluctuations in the cap loop were much more pronounced (Figure 3F); after ~80 ns the cap loop opened, as judged by the F70-C109 distance, and stayed open for the remainder of the 200 ns MD trajectory. A further 600 ns of simulations showed cap loop opening events with durations ranging from <1 ns to 22 ns (Figure 3—figure supplement 1, Figure 5—figure supplement 1). Calculations of SASA confirmed that opening of the loop increases the solvent exposure of C103 and C109 (Figure 3—figure supplement 2). The spontaneous loop opening of nDsbDox and the relative stability of partially open conformations observed in our MD simulations (Figure 3H), mark a clear difference in the conformational ensembles sampled by oxidized nDsbD, as compared to those sampled by the reduced protein (Figure 3D,H).

We have also employed MD to probe the behavior of the cap loop in simulations starting from an open conformation of nDsbD observed in the 1VRS X-ray structure of the nDsbD/cDsbD complex (Rozhkova et al., 2004). Five of the eight trajectories that were started from an open loop conformation for nDsbDred, closed within 10 ns (Figure 3C). Similarly, simulations of nDsbDox, that were started from a fully open 1VRS oxidized structure, closed within 10 ns in 3 out of 10 trajectories (Figure 3G). Together, these simulations demonstrate that in both reduced and oxidized nDsbD the cap loop can close rapidly in the absence of a bound interaction partner.

To validate the MD simulations, we used the generated trajectories to predict 1H-15N RDC and S2 values and to compare these to our experimental values. RDCs provide information about the average orientation of peptide bonds and are therefore well-suited for comparison with MD simulations. For both nDsbDred and nDsbDox, the agreement between calculated and experimental RDCs improved for the 1 μs MD ensemble compared to the static X-ray structures (Figure 2—figure supplement 1 and Figure 2—figure supplement 1—source data 1). In addition, the extent of the fast-time scale (ps-ns) dynamics observed experimentally by NMR is on the whole correctly reproduced by the MD simulations (Figure 2 and Figure 2—figure supplement 3). The trend for the cap loop is consistent with experiment; the S2 values for the cap-loop region for both oxidized and reduced nDsbD are on par with the rest of the well-ordered protein core (Figure 2—figure supplement 3 and Figure 2—figure supplement 2—source data 1). The observed cap-loop opening in the MD simulations of nDsbDox is too rare an event to lower the S2 values in a significant way. Nonetheless, the lowered experimental {1H}-15N NOE values for nDsbDox, and the need to fit them using a model that includes a τe parameter, are consistent with the observation of loop opening events in the MD simulations for nDsbDox. The good level of agreement between experimental NMR parameters and values calculated from the MD trajectories provides confidence that the 1 μs simulations of oxidized and reduced nDsbD allow us to glean a realistic picture of the fast timescale dynamics of nDsbD with atomic resolution.

### NMR and MD simulations reveal local frustration in nDsbDox

The differences in the cap loop dynamics, with the loop being more flexible in nDsbDox than in nDsbDred, must be a direct effect of the oxidation state of the two cysteine residues in the active site of nDsbD. X-ray crystallography (Mavridou et al., 2011) and solution NMR show that the average structures of the two redox states are very similar, with the only major difference between the two states being the presence of a disulfide bond in the active site of nDsbDox in lieu of a pair of thiol groups in nDsbDred.

Analysis of the MD simulations shows that the disulfide bond introduces local structural frustration in nDsbDox. The side chains of C103 and C109, which form the disulfide bond, adopt gauche- conformations (χ1 ~ −60o) in X-ray structures. This conformation is maintained throughout the MD simulations with only rare excursions (Figure 4C). The C103-C109 disulfide bond provides a flat binding surface for the side chain of F70. This aromatic ring packs onto the disulfide bond with its sidechain in either a gauche- or a trans orientation (Figure 4A and B). These two conformations are populated approximately equally and exchange rapidly in MD, on a timescale of tens of ns (Figure 4—figure supplement 1). This conformational averaging is evidenced experimentally by the almost identical F70 Hβ chemical shifts, which differ by only 0.015 ppm. TALOS-N (Shen and Bax, 2013) analysis of nDsbDox chemical shifts does not predict a single fixed χ1 value for F70, consistent with the averaging between a gauche- and a trans orientation seen for this side chain in MD simulations.

![Figure 4.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig4-v2.jpg)

**Figure 4.:** (A) In nDsbDox, the side chain of F70 switches between a gauche- and trans orientation in MD simulations as shown by the mass density calculated for F70 (red). (B) The gauche- and trans conformations are approximately equally populated in the 1 μs MD simulations of nDsbDox. (D) The cap loop and the active site of nDsbDred are rigid as shown by the mass density calculated for F70 (blue). The well-defined density closely circumscribes the position of the F70 side chain in the 3PFU crystal structure. (E) F70 is locked in the gauche- conformation. The surfaces in (A) and (D) surround points with at least 0.12 relative occupancy; these structures were rendered using VMD (Humphrey et al., 1996). The side chains of C103 and C109 in the active site of nDsbD adopt different conformations in the oxidized (C) and reduced (F) isoforms as shown by contour plots of their χ1 dihedral angles. Here 1 μs of MD simulations is analysed for each redox state.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** With the exception of a brief excursion to the trans (t) conformer (χ1 = −180o) in the top left panel, F70 remains in the gauche- (g-) conformer (χ1 = −60o) throughout the 1μs of MD simulations in nDsbDred (left panels). By contrast, in nDsbDox, F70 interconverts frequently between the g- and t conformers (right panels). In closed structures (F70-C109 distance <6 Å), the g- and t conformers are sampled 61.5% and 38.5% of the time, respectively, while in open structures the g- and t conformers are sampled 52.9% and 47.1% of the time, respectively. Data for ten 20 ns simulations are combined in the bottom panels; the vertical grey lines show the starting and ending points of these shorter 20 ns simulations.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** N. meningitidis nDsbDox crystallizes in the P213 space group with six molecules (denoted A to F) in the asymmetric unit (PDB: 6DPS [Smith et al., 2018]). (A) One of the six molecules (E) in the asymmetric unit has an open ‘Phen cap’ loop. This structure superimposes well with the open conformation of E. coli nDsbDox observed in MD simulations. (B) The other five molecules in the N. meningitidis nDsbDox asymmetric unit have a closed ‘Phen cap’ loop with the aromatic ring of F66 packing onto the C100-C106 disulfide bond in both gauche- and trans conformations. Shown here is a superposition of molecules B and C from the unit cell. (C) Superposition of two closed conformations of E. coli nDsbDox observed in the MD simulations showing F70 adopting the ‘frustrated’ gauche- and trans orientations. (A–C) The backbone of nDsbDox from E. coli and N. meningitidis are shown in cyan and salmon, respectively. F70 (dark teal), Y71 (dark grey), F66 (dark salmon), F67 (light grey) and the C103-C109 and C100-C106 disulfide bonds (yellow) are shown in a stick representation.

By contrast, in nDsbDred F70 packs onto the active site in a single well-defined conformation, explaining why the cap loop is rigid in nDsbDred. The side chains of C103 and C109 both adopt trans conformations (χ1 ~180o) in the X-ray structure of nDsbDred. This conformation is maintained throughout the MD simulations of nDsbDred with only rare excursions (Figure 4F). This trans conformation of the cysteines, along with the fact that the two thiols are bulkier than a disulfide bond, result in the cysteine thiols providing a snug-fitting binding site for F70 (Figure 4D) in which one of the C109 Hβ interacts closely with the aromatic ring of F70. Consequently, F70 is locked in its gauche- conformation (Figure 4E and Figure 4—figure supplement 1). NMR data support this packing arrangement of the cap loop onto the active site of nDsbDred. The Hβ of C109 are upfield shifted at 1.83 and 0.66 ppm, from a random coil value of ~3 ppm, consistent with the close proximity to the aromatic ring of F70. The two distinct Hβ shifts for F70 of nDsbDred, which are separated by ~0.2 ppm, show NOEs of differing intensity from the backbone HN, consistent with a single conformation for the F70 side chain. TALOS-N (Shen and Bax, 2013) analysis of chemical shifts predicts a gauche- χ1 conformation for F70, in agreement with the MD simulations.

Recently determined X-ray structures of nDsbD from Neisseria meningitidis (Smith et al., 2018) provide support for our observation of oxidation-state-dependent differences in the dynamics of the cap loop. Despite sharing only 27% sequence identity with the E. coli domain, nDsbDred from N. meningitidis shows a very similar structure with a closed ‘Phen cap’ loop in which the aromatic ring of F66 adopts a gauche- conformation packing tightly against C106. Interestingly, nDsbDox from N. meningitidis crystallizes in the P213 space group with six molecules in the asymmetric unit. One of these molecules is observed to have an open ‘Phen cap’ loop which superimposes very well with the open conformation observed in our MD simulations (Figure 4—figure supplement 2A). The five molecules with a closed ‘Phen cap’ loop show F66 packing onto the C100-C106 disulfide bond in both trans and gauche- orientations reminiscent of the two almost equally populated closed structures observed for E. coli nDsbDox in our MD simulations (Figure 4—figure supplement 2B/C). The range of ‘Phen cap’ loop conformations observed in N. meningitidis nDsbDox are likely to reflect conformations sampled by the protein in solution. Thus, local structural frustration appears to be a conserved feature for nDsbDox across many Gram-negative bacterial species.

### Structural features of cap loop opening

To understand how local structural frustration gives rise to cap loop opening in nDsbDox, we characterized loop opening events in our MD simulations. First, we investigated whether cap loop opening is linked directly to one of the two frustrated F70 χ1 conformers. The opening of nDsbDox at 82.5 ns in Figure 3F coincides with a change of the F70 χ1 from gauche- (−60o) to trans (−180o) (Figure 5 and Figure 5—figure supplements 2–4). During the 1 μs trajectory, the cap loop experiences several shorter opening events; twenty events with a duration of at least one ns and a F70-to-C109 distance of at least 10 Å are observed (Figure 3, Figure 3—figure supplement 1, Figure 5—figure supplements 1, 2). In only one of these events does F70 undergo a similar gauche- to trans transition at the point of opening. Fourteen of the openings start from F70 in the trans conformer, while five openings start from the gauche- conformer. Thus, loop opening is not underpinned by a specific F70 χ1 conformer.

![Figure 5.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig5-v2.jpg)

**Figure 5.:** Top: Snapshots of structures generated from the MD simulation between 65 and 105 ns show the range of cap loop conformations and, in particular, the F70 and Y71 side chain positions that are sampled. The backbone of nDsbD is shown as a cartoon in pale cyan. F70, Y71 and C103/C109 are shown in a stick representation and colored deep teal, grey and yellow, respectively. Two structures are overlaid in the 82.5 ns panel; these illustrate the conversion of F70 from the gauche- to the trans conformation observed simultaneously with loop opening. A surface representation is used in the 93.2 ns snapshot to illustrate how Y71 blocks closing of the cap loop. Bottom: Structural parameters are plotted as a function of simulation time. The distance from the center of the rings of F70 and Y71 to C109 Sγ are shown in black and grey in the first panel. The distance between the ring centres of F70 and Y71 are shown in the second panel. The solid and dashed lines show these distances in the closed (1L6P) and open (1VRS) X-ray structures, respectively. In the third and fourth panels, the F70 χ1 torsion angle and the E69 ϕ and ψ torsion angles are shown. These and additional structural parameters are shown in the figure supplements for the entire loop opening period (60–200 ns) and for a second 22 ns loop opening event.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Structural parameters, derived from the first 30 ns of the MD trajectory shown in Figure 3—figure supplement 1 (middle right panel), are plotted as a function of time. The four panels on the left show the distance between C109 Sγ and the centres of the F70 (black) and Y71 (red) aromatic rings, the distance between the center of the aromatic rings of F70 and Y71, and the χ1 torsion angles of F70 and Y71. The four panels on the right show the ϕ (black) and ψ (red) torsion angles for E69, F70, Y71 and G72. The cap loop opens after 3.8 ns and remains open for 21.7 ns. The loop opens with F70 in the trans conformer but this χ1 angle changes several times while the loop is open. Before loop opening, the aromatic ring of Y71 is farther away from C109 than in the 1L6P X-ray structure. This is due to the trans χ1 conformer. At ~20 ns the Y71 χ1 switches to the gauche- conformer; this brings the ring of Y71 closer to C109 and places the ring in between F70 and C109 in a ‘blocking’ conformation. At ~22 ns the ring of Y71 moves out of this position, and away from C109, allowing the loop to close at 25.5 ns. The backbone torsion angles of E69, F70, Y71 and G72 show some of the features in the open conformations that have been highlighted for the major opening event in Figure 5—figure supplement 4. When the loop closes at 25.5 ns, these torsion angles return to values typical of the closed conformation of nDsbD. Snapshots of structures from this opening event are shown in Figure 5—figure supplement 5.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Distances are derived from the MD trajectory shown in Figure 3F. Top panel: The distance between the center of the F70 aromatic ring and C109 Sγ (red) or the center of mass (c.o.m.) (black) are plotted as a function of time. The solid and dashed lines in the three panels show these distances in the closed 1L6P and open 1VRS X-ray structures. The center of mass of nDsbD in the 1L6P X-ray structure was determined to coincide with W33 Cε2. Both these distances are a good indicator of whether the cap loop is closed or open. The distance to the center of mass decreases at ~66 ns because of the change of the F70 χ1 conformation from gauche- to trans. Middle panel: The distance between the center of the Y71 aromatic ring and C109 Sγ (red) or the center of mass (c.o.m) (black) are plotted as a function of time. The distance from Y71 to C109 is a less clear indicator of cap loop opening because this distance first decreases as Y71 moves past C109 and then increases again as Y71 adopts more open conformations. In structures in which Y71 sits between F70 and C109, and blocks loop closing, the distance of Y71 to C109 is reduced. Bottom panel: The distance between the centres of the aromatic rings of F70 and Y71 is plotted as a function of time. This can vary from ~5 to ~11 Å. The shorter distance usually corresponds to F70 χ1 in the trans conformation. The longer distance, observed at ~95–100 and ~125–135 ns, corresponds to the rings pointing in opposite directions usually with the F70 and Y71 χ1 in the gauche- and trans conformations, respectively.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** The sidechain χ1 and χ2 torsion angles of F70 and Y71 are plotted as a function of time. In nDsbDox, F70 interconverts between the gauche- (−60o) and trans (−180o) conformations. At 60 ns, the cap loop is closed with F70 χ1 in the gauche- conformation. At ~66 ns, F70 χ1 switches to the trans conformation; this is accompanied by a change in the F70 χ2 angle from ~120o to ~65o. The cap loop begins to open at 82.5 ns and this coincides with a change of the F70 χ1 from −60o to −180o. After loop opening, F70 χ1 continues to interconvert between the gauche- and trans conformations. In the more exposed open conformation the aromatic ring of F70 undergoes frequent ring flips, as evidenced by 180°Changes in χ2, but also changes between the ~120o (or ~ −60o) to ~65o (or ~ −115o) orientations observed before loop opening. The Y71 χ1 torsion angle changes less frequently than F70 and has a marked preference for the gauche- conformer. Transitions to the trans conformer correlate with the largest F70-Y71 ring-to-ring distances observed in panel (A); these changes to the trans conformer are coupled to changes in χ2 from ~120o (or ~ −60o) to ~65o (or ~ −115o). Ring flips of Y71 are less frequent due to its less exposed conformation.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** Backbone ϕ (black) and ψ (red) torsion angles are plotted as a function of time for residues D68, E69, F70, Y71 and G72. These angles change at 82.5 ns, the time at which the cap loop opens. The ϕ and ψ values for E69 become less variable in the open loop while the values for the other residues appear to be more variable. Between ~160 and 180 ns, the ϕ and ψ angles of D68 and E69 return to values observed when the loop is closed. These changes are correlated with the presence (in the closed structure) or absence (in most of the open conformations) of a hydrogen bond between the backbone HN of Y71 and the D68 sidechain carboxyl group.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** (A) Two structures taken from the major loop opening described in Figure 5 and Figure 5—figure supplements 2–4. At 145.1 ns the cap loop adopts a very open conformation (F70-to-C109 distance of >16 Å) that may be important for the initial docking of cDsbD leading to complex formation. At 151.9 ns Y71 adopts a position between F70 and C109 that blocks loop closing. (B) A structure taken from the loop closing simulation of nDsbDox shown in Figure 3G (in pink). At 2.8 ns Y71 adopts a position in between F70 and C109 which blocks the loop from closing immediately. (C) Six structures taken from the ~22 ns loop opening event described in Figure 5—figure supplement 1. Prior to loop opening, at 3.75 ns, F70 and Y71 both adopt the trans χ1 conformation with Y71 farther away from C109 than observed in the closed 1L6P X-ray structure. Loop opening at 3.8 ns involves F70 moving up and away from C109. At 20.4 ns the Y71 χ1 changes to the gauche- conformer bringing the ring of Y71 closer to C109 allowing it to adopt a ‘blocking’ conformation at 21 ns. Prior to loop closing Y71 returns to the trans conformation (25.47 ns) allowing F70 to approach C109 and leading to loop closure (25.51 ns). In all panels the backbone of nDsbD is shown as a cartoon in pale cyan. F70, Y71 and C103/C109 are shown in a stick representation and colored deep teal, grey and yellow, respectively. A surface representation is used in the snapshots that show the ‘blocking’ conformation of Y71.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig5-figsupp6-v2.jpg)

**Figure 5—figure supplement 6.:** The figure shows a sequence alignment of representative nDsbD protein sequences from β- and γ-proteobacteria; only part of each nDsbD sequence is shown, spanning residues A53 to L119 in E. coli nDsbD. 2753 representative bacterial and archaeal proteomes were selected for homologues of nDsbD, and a subset of 731 sequences clustering around the E. coli DsbD were selected for subsequent analysis as a consistent phylogenetic group of proteins, belonging to mostly β- and γ-proteobacteria. 134 sequences, on per bacterial genus, were aligned along with E. coli nDsbD (top). The cap loop region and active-site cysteines are indicated by the red dashed lines, and positions 70 and 71 in E. coli nDsbD are indicated by blue arrows.

By contrast, we found that the dynamics of Y71 and the relative orientation of F70 and Y71 seem to be important for cap loop opening. In closed nDsbDox Y71 also samples both gauche- and trans χ1 conformers, showing a strong preference for gauche- (86%). Despite this preferred conformation, we note that there is no correlation between the χ1 values of F70 and Y71; the less common Y71 trans conformer is observed for both frustrated F70 conformers. We observed the sequence of events leading to loop opening (Figure 5 and Figure 5—figure supplements 2–4). Although the cap loop remains closed from 60 to 80 ns, the side chains of both F70 and Y71 sample a number of different conformations. From 60 to 65 ns, both F70 and Y71 are in the gauche- χ1 conformation observed in the 1L6P X-ray structure. At 65.9 ns, F70 χ1 switches to the trans conformer. This brings the F70 and Y71 rings closer together. From 66 to 80 ns, F70 remains primarily in the trans conformer with only brief excursions to gauche- (at ~72.7 and~77.7 ns), and at 79.9 ns F70 returns to the gauche- χ1 conformer. Meanwhile, at 76.9 and 80.3 ns the ring of Y71 transiently moves into more exposed conformations as a result of changes to χ1 and χ2, but the loop remains closed (Figure 5 and Figure 5—figure supplement 3). Immediately before loop opening the F70 and Y71 rings are in close proximity, while Y71 is also close to C109. This flexible and dynamic nature of the side chains of F70 and Y71 in the closed state is reflected in their RMSD, to the equilibrated X-ray structure, observed during the MD trajectories. In the nDsbDox 1 μs trajectories, F70 and Y71 have RMSDs of 2.8 ± 0.8 and 2.6 ± 0.7 Å, respectively when the loop is closed (F70-C109 < 6 Å). By contrast, these RMSD values are 1.7 ± 0.6 and 1.6 ± 0.8 for F70 and Y71, respectively in nDsbDred trajectories. It is worth noting here that the aromatic ring of F67 in N. meningitidis nDsbDox, which is homologous to Y71 in E. coli nDsbD, is also dynamic, adopting different conformations in the crystallized closed structures (Figure 4—figure supplement 2; Smith et al., 2018). Taking these observations together, we propose that the existence of local structural frustration for F70 results in increased dynamics for both F70 and Y71, which leads to occasional loop opening in nDsbDox.

Following opening of the cap loop at 82.5 ns, Y70 and Y71 continue to sample a variety of conformations, which could be important for the cap loop to access a fully open structure. The initial open states show the ring of F70 pointing inwards, due to its trans conformation. Transition of F70 to the gauche- conformer after loop opening, leads to a more extended orientation for F70. The extent of loop opening, as measured by the F70-to-C109 distance, fluctuates during the 120 ns open period; for example, at 85.6 ns the loop is in a more open conformation (12.5 Å) than at 93.2 ns (8.6 Å) (Figure 5). Interestingly, as the F70-to-C109 distance decreases, the loop is often prevented from closing fully by the side chain of Y71 which sits in between C109 and F70 in a ‘blocking’ conformation (for example at 93.2 ns and later at 151.9 and 155.8 ns [Figure 5 and Figure 5—figure supplement 5]). The orientation of F70 relative to Y71 also changes while the loop is open. At 98.2 ns the position of Y70 is similar to that observed in the open 1VRS X-ray structure but Y71 points inwards. At 102.2 ns the Y70 and F71 orientations are more similar to the 1VRS structure (Figure 5). The cap loop can also adopt conformations that are more open than the open 1VRS structure (at ~145 and~181 ns); these structures are characterized by larger F70-C109 and Y71-C109 distances (>16 Å and 10 Å, respectively) (Figure 5—figure supplements 2, 5). These conformations may be important for the initial docking of cDsbD prior to nDsbD/cDsbD complex formation, as they would minimize the steric clashes between the two domains during binding.

The backbone ϕ and ψ torsion angles of D68, E69, F70, Y71 and G72 also show clear changes at 82.5 ns when the loop begins to open (Figure 5 and Figure 5—figure supplement 4). E69 ϕ and ψ become less variable in the open loop while the ϕ and ψ values for D68 and F70 become more variable. These torsion angle changes are correlated with loss of the hydrogen bond between the amide nitrogen of Y71 and the side chain carboxyl group of D68 upon loop opening. This hydrogen bond is observed in the 1L6P X-ray structure and in 95% of structures between 60 and 82.5 ns, prior to loop opening. Notably, D68 and E69 adopt ϕ and ψ values more reminiscent of the closed state between 160 and 180 ns, despite the loop remaining open (Figure 5—figure supplement 4); during this period the Y71HN-D68Oδ hydrogen bond is again observed in 62% of structures. By contrast, the backbone hydrogen bonds which define the antiparallel β-hairpin of the cap loop and which involve D68-G72 and H66-S74, are always retained in the open loop structures.

We have also investigated the dynamics of Y71 in the simulations of loop closing, and in particular those simulations in which the loop fails to close completely within 10 ns. During these trajectories Y71 adopts conformations in which it sits between F70 and C109 thus blocking complete closure of the loop as observed, for example, at 93.2 ns in the major opening event and at 2.8 ns in the incomplete loop closing seen in Figure 3G (Figure 5 and Figure 5—figure supplement 5).

In the light of the important roles identified for both F70 and Y71 in cap loop opening, we investigated the conservation of cap loop residues using bioinformatics. We have used 134 representative sequences, one from each bacterial genus, for our sequence alignment (Figure 5—figure supplement 6). We find that the cap-loop motif is more conserved than the flanking β-strands, in agreement with the central role that this structural motif plays in nDsbD function. In 53% of the sequences an F or a Y is found at position 70; in a further 36.4% of the sequences a residue with a relatively bulky side chain (K/I/L/E/V/T/N), which would shield the cysteines from solvent, is found at position 70. Interestingly, in 85% of sequences an F or a Y is found at position 71; in a further 5.2% of the sequences position 71 is occupied by a bulky hydrophobic residue (I or L). This high conservation of an aromatic amino acid observed for this position further highlights the key role played by Y71 in contributing to loop opening and, more importantly, in preventing rapid loop closure, thus likely facilitating the interaction of nDsbD with cDsbD prior to reductant transfer.

### NMR relaxation dispersion experiments

Using 15N NMR relaxation dispersion experiments (Baldwin and Kay, 2009; Loria et al., 1999) we also detected a difference in the μs-ms timescale dynamics of reduced and oxidized nDsbD. For nDsbDred, no evidence for μs-ms dynamics in the cap loop or the active site were found (Figure 6A–C). This observation is consistent with the absence of a significantly populated open state of nDsbDred. By contrast, in nDsbDox, eight residues, V64, W65, E69, F70, Y71, G72, K73 and S74, all in the cap-loop region, showed strong relaxation dispersion effects (Figures 6D–F and 7A). These results are consistent with previous observations about peak intensities in 1H-15N HSQC spectra (Mavridou et al., 2012). The peaks of C103, C109 and Y110 are not visible and the peak of A104 is very weak in the spectrum of nDsbDox, but not nDsbDred (Mavridou et al., 2012), likely due to extensive chemical exchange processes in nDsbDox leading to 1HN and/or 15N peak broadening. Thus, the cap loop of nDsbDox, and likely also the active-site cysteines, exchange between different conformations on the μs-ms timescale, whereas nDsbDred adopts a single conformation on this timescale.

![Figure 6.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig6-v2.jpg)

**Figure 6.:** For nDsbDred, flat relaxation dispersion profiles were obtained as illustrated for (A) W65, (B) E69 and (C) F70 in the cap loop. For nDsbDox clear relaxation dispersion effects were measured for (D) W65, (E) E69 and (F) F70; error bars were determined as described in Figure 6—figure supplement 1—source data 1. In the oxidized cap-loop deletion mutant (Δloop-nDsbDox), flat relaxation dispersion profiles were obtained for (G) W65, (H) A104 and (I) C103/C109 in the active site. Experimental data are represented by circles and fits to the data for wild-type nDsbDox are shown by solid lines.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Global fitting of relaxation dispersion data measured for twelve residues in nDsbDox at 10°C, 15°C, 20°C, 25°C and 35°C at 500 MHz and at 15°C and 25°C at 750 MHz was performed using CATIA (Cpmg, Anti-trosy, and Trosy Intelligent Analysis)(Alderson et al., 2019; Baldwin et al., 2011a; Vallurupalli et al., 2008), where the specific pulse sequence was simulated incorporating differential relaxation rates between the coherences generated, and off-resonance effects of the 180o pulses. Error bars were determined as described in Figure 6—figure supplement 1—source data 1. Relaxation dispersion data measured for W65 and the curves from the global fitting are shown in (A) (Figure 6—figure supplement 1—source data 1). The global fits at five different temperatures yield a description of the free energy landscape of the exchange process shown in (B). The minor state of nDsbDox is enthalpically more favorable than the ground state. This is reflected in the decrease in the population of the minor state from 7.1% to 1.6% when the temperature is increased from 10°C to 35°C (Figure 6—figure supplement 1—source data 1). The minor state is entropically less favorable than the ground state. Overall, the reaction coordinate in (B) shows that the minor state is less favorable by 8.8 kJ mol−1 at 25°C. The fitting of the experimental curves at the five temperatures also reports on the barrier between the two states. The transition state is enthalphically more favorable than the ground state. There is, however, a sizeable free-energy barrier as the transition state is lower in entropy than the ground state, and so the rate for the forward reaction, while approximately temperature independent, decreases slightly with increasing temperature. Note that $ΔS^{‡}$ and hence $ΔG^{‡}$ depend on the transmission coefficient κ that is used in Equation 1.

$$
k=κ(\frac{k_{B}T}{h})e^{−ΔH^{‡}/(k_{B}T)}e^{ΔS^{‡}/k_{B}}(1)
$$

$ΔH^{‡}$ and $ΔS^{‡}$ are the activation enthalpy and entropy for the reaction. The transmission coefficient κ was set to 1.4 × 10−7 s−1 K−1 (Fersht, 1984).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** The backbone/cap loop of wild-type nDsbDox (1L6P) and Δloop-nDsbDox (5NHI) are shown in cyan/deep teal and grey/black, respectively. F70 (dark teal), in wild-type DsbDox, and the C103-C109 and C98-C104 disulfide bonds (yellow/pale yellow) are shown with a stick representation. The overlaid structures (C) have a Cα RMSD of 0.25 Å for residues 12–122.

![Figure 7.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig7-v2.jpg)

**Figure 7.:** (A) Residues 64, 65 and 69–74 with chemical shift differences between the major and minor states of >1 ppm are shown in a stick representation in dark teal. C103 and C109 are shown in yellow. The magnitude of the 15N chemical shift differences between the major and minor states are compared in (B) with the magnitude of predicted shift differences between the native and random coil states and in (C) with the magnitude of the experimental shift difference between nDsbDox and nDsbDred. Shift differences between the major and minor states for W65, E69, F70, Y71, G72 and K73, for which the sign has been obtained experimentally, are compared with the predicted shift differences between the native and random coil states in (D) and between nDsbDox and nDsbDred in (E). The experimentally determined chemical shift differences are shown in light grey, with error bars. Random coil shifts were predicted using POTENCI (Nielsen and Mulder, 2018). Details of the fitting procedures used for the dispersion data and the determination of errors in the chemical shift differences are presented in Figure 6—figure supplement 1 and Figure 6—figure supplement 1—source data 1 and Figure 7—source data 1.

Analysis of the relaxation dispersion data collected at 25°C (using CATIA [Vallurupalli et al., 2008; Baldwin et al., 2011a; Alderson et al., 2019]) showed that nDsbDox undergoes a single global exchange process, between a dominant major state (pA98%) and an alternative minor state (pB2%) (Figure 6—figure supplement 1—source data 1). To corroborate that a single exchange process gives rise to the relaxation dispersion curves, we repeated the experiments at four additional temperatures (10, 15, 20°C and 35°C). If the residues underwent different exchange processes we would expect them to show a differential response to temperature (Grey et al., 2003). The relaxation dispersion data for all residues in the cap loop recorded at the five temperatures could be fitted simultaneously (Baldwin et al., 2011a; Alderson et al., 2019; Figure 6—figure supplement 1A and Figure 6—figure supplement 1—source data 1). This confirmed that a single process underlies the μs-ms chemical exchange in the cap loop of nDsbDox. In addition, the analysis of the data at all five temperatures yielded a detailed description of the thermodynamics and kinetics of the exchange process (Figure 6—figure supplement 1B and Figure 6—figure supplement 1—source data 1). The minor ‘excited’ state is enthalpically, but not entropically, more favorable than the major ground state of nDsbDox. The fits also demonstrated that no enthalpic barrier separates the ground and excited state of nDsbDox. This absence of an enthalpic barrier between the two states might mean that no favorable interactions have to be broken in the transition state, but that the diffusion process itself may limit the speed of the transition (Dill and Bromberg, 2010).

Analysis of the chemical shift differences determined from the relaxation dispersion experiments suggests that the conformation adopted by the cap loop in the minor state of nDsbDox might be similar to the conformation of nDsbDred. To interpret the chemical shift differences, we calculated the shift changes expected if the minor state features a disordered cap loop (Nielsen and Mulder, 2018). Such a state would include more open conformations and such structures might facilitate the binding of the nDsbD interaction partners. The lack of correlation in Figure 7B demonstrates that the cap loop does not become disordered in the less populated minor state. The 15N chemical shift differences between the major and minor states do, however, resemble the chemical shift differences between the oxidized and reduced isoforms of nDsbD (Figure 7C; Mavridou et al., 2012). Nonetheless, the correlation in Figure 7C is not perfect; the differences between the chemical shifts of the minor state of nDsbDox and those of nDsbDred likely reflect the local electronic and steric differences between having a disulfide bond (in the minor state of nDsbDox) and two cysteine thiols (in nDsbDred) in the active site. Importantly, the sign of the chemical shift differences between the major and minor state, which could be determined experimentally for W65, E69, F70, Y71, G72 and K73, further indicated that the minor state structure of the cap loop of nDsbDox is not disordered (Figure 7D and Figure 7—source data 1), but instead may be similar to that adopted in nDsbDred (Figure 7E and Figure 7—source data 1).

### Coupling between the active site and the cap loop gives rise to the alternative minor state of oxidized nDsbD

The alternative minor state of nDsbDox, which we detected by NMR relaxation dispersion, can also be attributed to coupling between the dynamics of the active-site cysteine residues and the cap loop. In this alternative minor state, the C103 and C109 side chains likely adopt a 'reduced-like' conformation. Both side chains adopt a gauche- conformation (χ1 ~ −60o) in nDsbDox, but a trans conformation (χ1 ~ 180o) in nDsbDred. In MD simulations of both redox states, rare excursions of one or the other χ1, but never both, to the alternative conformation are observed (Figure 4C/F). We postulate that in the minor state of nDsbDox, both of the cysteine side chains adopt the 'reduced-like' trans conformation. In this state, the cap loop could pack tightly onto the active-site disulfide bond, as observed in MD simulations of nDsbDred. The backbone 15N chemical shifts of this minor state consequently resemble those of the reduced protein. Model building of a disulfide bond into the reduced 3PFU crystal structure followed by energy minimization with XPLOR (Brunger, 1992) showed that the resulting 'oxidized' structure maintains the 'reduced-like' trans conformation (χ1 ~ −140o) for the cysteine side chains and the gauche- conformation for F70 (Figure 8B). This 'reduced-like' conformation for nDsbDox, with a more tightly packed active site and a cap loop which lacks frustration, might be enthalpically more favorable and entropically less favorable than the major state of nDsbDox as shown by the analysis of relaxation dispersion data collected at multiple temperatures (Figure 6—figure supplement 1 and Figure 6—figure supplement 1—source data 1). Previously, NMR relaxation-dispersion experiments and MD simulations have detected complex dynamics in BPTI stemming from one of its disulfide bonds (Grey et al., 2003; Shaw et al., 2010; Xue et al., 2012), further suggesting that the disulfide bond shapes the μs-ms dynamics of the active-site and cap-loop regions of nDsbDox.

![Figure 8.](https://cdn.elifesciences.org/articles/54661/elife-54661-fig8-v2.jpg)

**Figure 8.:** (A) The cap loop in nDsbDred maintains a closed conformation shielding the active-site cysteine thiols. The cap loop may only open to expose the cysteine thiols via an induced-fit mechanism when it encounters its legitimate binding partners, CcmG, DsbC and DsbG. (B) nDsbDox undergoes more complex dynamics as a result of local structural frustration. F70 interacts with C109 Sγ both in its gauche- (top left structure in dashed box) and trans (lower left structure in dashed box) orientations. These mutually competing interactions destabilize the packing of the cap loop onto the active site. Consequently, open conformations (right-hand structure in dashed box) are accessible in nDsbDox and these would allow nDsbDox to form complexes with its legitimate binding partner, cDsbDred, via a conformational selection mechanism. The left-hand structure shows a reduced-like minor (2%) conformation identified by relaxation dispersion experiments and populated on a slower timescale. The backbone of nDsbD and cDsbD are shown in cyan and grey, respectively. F70 (dark teal), C103 and C109 (yellow) are shown with sticks and a surface representation. (A) is from the 3PFU X-ray structure of nDsbDred, the left-hand panel in (B) is the energy minimized 3PFU structure with a disulfide bond incorporated, the structures in the dashed rectangle in (B) are 'snapshots' from the MD simulations of nDsbDox. The bound complexes shown on the right in (A) and (B) are based on the 1VRS X-ray structure.

### NMR relaxation dispersion experiments using a loop deletion variant

We confirmed the tight coupling between the dynamics of the cap loop and the active site by NMR relaxation dispersion experiments using an nDsbD variant. We generated an nDsbD protein with a truncated cap loop in which the eight residues H66-K73 were replaced by A-G-G (Δloop-nDsbD). The X-ray structure of oxidized Δloop-nDsbD shows that deletion of the cap loop does not cause any significant changes in structure; a Cα RMSD of 0.25 Å is obtained for residues 12–122 (Figure 6—figure supplement 2 and Figure 6—figure supplement 2—source data 1). Nevertheless, in the absence of F70, the shorter cap loop can no longer closely pack onto the disulfide bond. As a result, no relaxation dispersion is detected in the truncated cap loop variant, as shown for W65 (Figure 6G). For A104 (A99), a much sharper amide peak is observed in the HSQC spectrum of Δloop-nDsbDox and this residue shows a flat dispersion profile (Figure 6H). Importantly, the 1HN-15N peaks for C103 (C98) and C109 (C104), which are not observed in the wild-type oxidized protein, can be detected for Δloop-nDsbDox. Finally, 15N relaxation dispersion profiles for these cysteines are also flat (Figure 6I). Thus, truncation of the cap loop alters the μs-ms dynamics of the cap-loop region and the active-site cysteines, further supporting our proposed model of tight coupling between the cap loop and active-site cysteines.

### Conclusion

We have studied oxidized and reduced nDsbD using NMR experiments and microsecond duration MD simulations, and have demonstrated that the conformational dynamics of the active-site cysteines and the cap loop are coupled and behave in an oxidation-state-dependent manner. We showed that the cap loop is rigid in nDsbDred, whilst it exhibits more complex dynamics in nDsbDox (Figure 8). Although the cap loop is predominately closed and ordered in both oxidation states, for nDsbDred we found no evidence for a significant population with an open cap loop. Our results argue that the cap loop of nDsbDred remains closed at all times, to protect the active-site cysteine thiol groups from non-cognate reactions in the oxidizing environment of the periplasm. As such, the nDsbDred cap loop may only open to expose the cysteine thiols via an induced-fit mechanism when it encounters its legitimate binding partners, for example CcmG, DsbC and DsbG. In nDsbDox, on the other hand, the cap loop opens spontaneously in MD simulations and while fully open conformations of the cap loop tended to close, partially open structures were stable. Thus, nDsbDox may form a complex with its sole legitimate binding partner, cDsbDred, via a conformational selection mechanism. Notably, NMR relaxation dispersion experiments provided no evidence for a long-lived open or disordered conformation of the cap loop as might have been expected. Instead, a minor state with a 'reduced-like' conformation in the active site and cap loop is observed solely for nDsbDox.

Importantly, combining NMR experiments and MD simulations, we showed how local frustration (Ferreiro et al., 2007; Ferreiro et al., 2011) in nDsbDox, but not in nDsbDred, gives rise to differences in the dynamics of the two redox isoforms, on multiple timescales, providing insight into how this could affect protein function. Local frustration has been highlighted in the interaction interfaces of many protein complexes (Ferreiro et al., 2007), where mutually exclusive favorable interactions result in a dynamic equilibrium of competing structures and determine which parts of a protein are flexible. In nDsbDred, the cap loop packs perfectly onto the active-site cysteines and the closed conformation is stable, something that is crucial in the very oxidizing environment in which the domain has to provide electrons. By contrast, in nDsbDox, the disulfide bond disrupts this tight fit of the aromatic ring of F70. Consequently F70 is no longer locked in a single conformation and switches freely between gauche- and trans orientations. This results in increased flexibility for both F70 and Y71 and drives occasional opening of the cap loop, which in this oxidation state might facilitate nDsbDox receiving electrons from its partner. This is further enabled by a possible role of Y71 in preventing rapid loop closing. The observation from sequence alignments that the general architecture of the cap-loop region in β- and γ-proteobacteria is conserved, highlights that our observations in E. coli nDsbD can be generalized for many other bacterial species where reductant provision is driven by DsbD in the cell envelope.

Overall, our results show that it is the oxidation state of the cysteine pair in nDsbD that acts as a 'switch' controlling the presence or absence of local frustration in its active site. This oxidation-state-dependent 'switch' determines the dynamic behavior of the cap loop which translates into optimized protein-protein interaction and biological activity. We propose that redox-state modulation of local frustration, such as that observed here for nDsbD, may play a wider role in biomolecular recognition in other pathways involving redox proteins which are ubiquitous in all organisms. Ultimately, the understanding gained from studies like this would allow controlled introduction of frustration, mimicking intricate natural systems such as DsbD, for more translational applications such as the production of synthetic molecular devices.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Escherichia coli)</td>
      <td>DSBD</td>
      <td></td>
      <td>DSBD_ECOLI</td>
      <td>UniprotID P36655</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21(DE3)</td>
      <td>Stratagene</td>
      <td></td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pDzn3</td>
      <td>DOIs:10.1007/s12104-011-9347-9 and 10.1074/jbc.M805963200</td>
      <td>N-terminal domain of DsbD (nDsbD) (L2-V132)</td>
      <td>Plasmid for wild-type nDsbD expression</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pDzn8</td>
      <td>This study.</td>
      <td>nDsbD (L2-V132) with residues H66-K73 replaced by AGG</td>
      <td>Plasmid for Δ-loop nDsbD expression</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Δ-loop nDsbD</td>
      <td>This study. Synthesized by Sigma Aldrich.</td>
      <td></td>
      <td>PCR primer (forward): 5′-(AGGAAGCGAGATTTACCGCGATCGGCTG)−3′</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Δ-loop nDsbD</td>
      <td>This study. Synthesized by Sigma Aldrich.</td>
      <td></td>
      <td>PCR primer (reverse): 5′-(CCGGCCCAGACGCCTTGCGGCAGCTGC)−3′</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Wild-type nDsbd</td>
      <td>DOIs:10.1007/s12104-011-9347-9 and 10.1074/jbc.M805963200</td>
      <td>N-terminal domain of DsbD (nDsbD) (L2-V132)</td>
      <td>Purified using a thrombin-cleavable C-terminal poly-His tag</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Δ-loop nDsbd</td>
      <td>This study.</td>
      <td>nDsbD (L2-V132) with residues H66-K73 replaced by AGG</td>
      <td>Purified using a thrombin-cleavable C-terminal poly-His tag</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Sigma Thrombin CleanCleave Kit</td>
      <td>Sigma-Aldrich</td>
      <td></td>
      <td>Used for removal of the poly-His tag</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KOD Hot Start DNA polymerase</td>
      <td>Novagen</td>
      <td></td>
      <td>Used for PCR</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pf1 phage</td>
      <td>ASLA Biotech AB</td>
      <td></td>
      <td>Used for partial alignment for RDC measurements</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NMRPipe</td>
      <td>DOI:10.1007/BF00197809</td>
      <td></td>
      <td>Processing of NMR data</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CCPN Analysis (version 2.4.2)</td>
      <td>DOI:10.1002/prot.20449</td>
      <td>RRID:SCR_016984</td>
      <td>Analysis of NMR spectra</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CATIA</td>
      <td>DOIs:10.1073/pnas.0804221105 and 10.1016/j.jmb.2011.07.017 and 10.1038/s41467-019-08557-8</td>
      <td>https://www.ucl.ac.uk/hansen-lab/catia/</td>
      <td>Global fitting of relaxation dispersion NMR data</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GROMACS 4.5</td>
      <td>DOI:10.1002/jcc.20291</td>
      <td>RRID:SCR_014565</td>
      <td>Used for MD simulations</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>WHAT-IF</td>
      <td>DOI:10.1093/nar/gkq453</td>
      <td>https://swift.cmbi.umcn.nl/whatif</td>
      <td>Used to add missing atoms prior to MD simulations</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Visual Molecular Dynamics (VMD)</td>
      <td>DOI:10.1016/0263-7855(96)00018-5</td>
      <td>RRID:SCR_001820</td>
      <td>Used for analysis of distances, angles, hydrogen bonds in MD simulations and for rendering protein structures</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MDAnalysis Python Library</td>
      <td>DOI:10.1002/jcc.21787</td>
      <td></td>
      <td>Used for analysis of distances, angles, hydrogen bonds in MD simulations</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>blast 2.2.28+ (blastp)</td>
      <td>NCBI</td>
      <td>RRID:SCR_001010 https://blast.ncbi.nlm.nih.gov/Blast.cgi</td>
      <td>Used to search for DsbD protein homologs</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>fasttree 2.1.7</td>
      <td>DOI:10.1371/journal.pone.0009490</td>
      <td>RRID:SCR_015501</td>
      <td>Used for building a phylogenetic tree</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>muscle 3.8.31</td>
      <td>DOI:10.1093/nar/gkh340</td>
      <td>RRID:SCR_011812</td>
      <td>Used for sequence alignment</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Pymol Version 2.3.5</td>
      <td>Schrodinger, LLC</td>
      <td>RRID:SCR_000305</td>
      <td>Used for rendering protein structural figures</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Denzo/ Scalepack</td>
      <td>DOI:10.1016/S0076-6879(97)76066-X</td>
      <td></td>
      <td>Used for processing and scaling of X-ray data</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MOLREP</td>
      <td>DOI: 10.1107/S0907444996012255</td>
      <td></td>
      <td>Used for molecular replacement in solving X-ray structure</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix.refine</td>
      <td>DOI:10.1107/S09074444909052925</td>
      <td>RRID:SCR_016736</td>
      <td>Used for refinement of X-ray structure</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>DOI:10.1107/S0907444910007493</td>
      <td>RRID:SCR_014222</td>
      <td>Used for manual fitting of electron density in X-ray structure</td>
    </tr>
  </tbody>
</table>

### Construction of plasmids and protein production

The plasmid pDzn3, described in previous work (Mavridou et al., 2012; Mavridou et al., 2009), encodes isolated wild-type nDsbD (L2-V132) bearing a thrombin-cleavable C-terminal poly-histidine tag. This construct was used as a template to produce a cap-loop deletion variant of nDsbD (Δloop-nDsbD), where residues H66-K73 were replaced by the amino acid sequence A-G-G. Site-directed mutagenesis (ExSite, Stratagene) was performed using oligonucleotides 5'-(AGGAAGCGAGATTTACCGCGATCGGCTG)−3' and 5'-(CCGGCCCAGACGCCTTGCGGCAGCTGC)−3'. PCR was performed with KOD Hot Start DNA polymerase (Novagen) and oligonucleotides were synthesized by Sigma Aldrich. DNA manipulations were conducted using standard methods. The resulting plasmid was named pDzn8. nDsbD and Δloop-nDsbD were expressed using BL21(DE3) cells (Stratagene) and purified from periplasmic extracts of E. coli using a C-terminal poly-histidine tag, as described previously (Mavridou et al., 2012; Mavridou et al., 2007). Thrombin cleavage of the affinity tag was performed using the Sigma Thrombin CleanCleave Kit (Sigma) according to the manufacturer's instructions.

### NMR spectroscopy

NMR experiments were conducted using either home-built 500, 600 and 750 MHz spectrometers equipped with Oxford Instruments Company magnets, home-built triple-resonance pulsed-field gradient probeheads and GE/Omega data acquisition computers and software, or using a 750 MHz spectrometer equipped with a Bruker Avance III HD console and a 5 mm TCI cryoprobe. All experiments were conducted at 25°C and at pH 6.5 in 95% H2O/5% D2O, unless stated otherwise. Spectra were processed using NMRPipe (Delaglio et al., 1995) and analyzed using CCPN Analysis (Skinner et al., 2016; Vranken et al., 2005).

Residual dipolar couplings (RDCs) were measured using Pf1 phage (ASLA Biotech AB) on separate samples for oxidized and reduced nDsbD. RDCs were measured at 600 MHz for 0.5 mM nDsbD with 10 mg/ml Pf1 phage, 2 mM K2PO4, 0.4 mM MgCl2, 0.01% NaN3 and 10% D2O. Measurements were also carried out for isotropic solutions prior to the addition of the Pf1 phage. RDCs were measured using the InPhase-AntiPhase (IPAP) approach (Ottiger et al., 1998). The F2 1H and F1 15N dimensions were recorded with 128 scans per increment, sweep widths of 7518.8 and 2000.0 Hz, respectively, and 1024 and 128 complex points, respectively. The quality factor (Q) that describes the agreement between calculated and observed RDCs was determined using the procedure of Ottiger et al., 1997.

{1H}-15N heteronuclear NOE, 15N T1 and T2 data (Boyd et al., 1990; Kay et al., 1989; Palmer et al., 1992) were measured at 600 MHz. The {1H}-15N heteronuclear NOE was also measured at 500 MHz. For the T1 measurement, spectra with 14 different relaxation delays, ranging from 20 ms to 2 s, were collected. The T2 was measured by recording spectra with 14 relaxation delays between 8 ms and 400 ms, with a Carr-Purcell Meiboom Gill (CPMG) delay τCPMG of 0.5 ms. For the T1 and T2 measurements, a recycle delay of 2 s was used. The {1H}-15N NOE was measured by comparing peak heights in interleaved spectra recorded with and without saturation of the protons for 3 and 4 s at 500 and 600 MHz, respectively. The F2 1H and F1 15N dimensions were recorded with sweep widths of 7518.8 and 1785.7 Hz, respectively, and with 1024 and 128 complex points, respectively. The T1 and T2 and NOE experiments were collected with 16, 16 and 128 scans per increment, respectively.

15N relaxation data were collected for 107 and 117 of the 126 non-proline residues of oxidized and reduced nDsbD, respectively. Data for the remaining residues could not be measured due to weak or overlapping peaks. T1, T2 and {1H}-15N NOE values were determined as described previously (Smith et al., 2013). Uncertainties in the T1, T2 and {1H}-15N NOE values were estimated from 500 Monte Carlo simulations using the baseline noise as a measure of the error in the peak heights (Smith et al., 2013). Relaxation data were analyzed using in-house software (Smith et al., 2013); this incorporates the model-free formalism of Lipari and Szabo (Lipari and Szabo, 1982a; Lipari and Szabo, 1982b) using spectral density functions appropriate for axially symmetric rotational diffusion (Abragam, 1961) and non-colinearity of the N-H bond vector and the principal component of the 15N chemical shift tensor (Boyd and Redfield, 1998) with model selection and Monte Carlo error estimation as described by Mandel et al., 1995. Calculations were carried out using an N-H bond length of 1.02 Å, a 15N chemical shift anisotropy, (σ|| - σ⊥), of −160 ppm, and a D||/D⊥ ratio of 2.0.

15N relaxation-dispersion experiments (Loria et al., 1999) were recorded at multiple magnetic field strengths and temperatures. Recycle delays of 1.2 and 1.5 s were used at 500 and 750 MHz, respectively. Typically 12 to 14 spectra were recorded with refocusing fields, νCPMG, between 50 and 850 Hz and two reference spectra (Mulder et al., 2001) were collected to convert measured peak intensities into relaxation rates. At 15°C and 25°C, experiments were collected at both 500 and 750 MHz. Experiments at 10°C, 20°C and 35°C were recorded at 500 MHz only. Δloop-nDsbD, was studied at 25°C at 750 MHz. The experiments were analyzed by global fitting using CATIA (Cpmg, Anti-trosy, and Trosy Intelligent Analysis, https://www.ucl.ac.uk/hansen-lab/catia/) (Vallurupalli et al., 2008; Baldwin et al., 2011a; Alderson et al., 2019) using transition state theory to restrict the rates and linear temperature-dependent changes in chemical shifts when analyzing data across multiple temperatures (Vallurupalli et al., 2008; Baldwin et al., 2011a; Alderson et al., 2019).

The HSQC and HMQC pulse sequences developed by Skrynnikov et al., 2002 were used to determine the sign of the chemical shift differences between the major and minor states. Bruker versions of the sequences were kindly provided by Prof. LE Kay. Experiments were recorded in triplicate at 750 MHz using a spectrometer equipped with a cryoprobe. 48 scans were collected per 15N increment, using 1H and 15N sweep widths of 11904.762 and 2493.767 Hz, respectively, and with 1024 and 175 complex points in the 1H and 15N dimensions, respectively.

### Molecular dynamics simulations

MD simulations were run using GROMACS 4.5 (Van Der Spoel et al., 2005). Simulations were started from the closed crystal structures of reduced nDsbD (nDsbDred) (PDB: 3PFU) (Mavridou et al., 2011) and oxidized nDsbD (nDsbDox) (PDB 1L6P) (Goulding et al., 2002). For each redox state of nDsbD, four simulations of 200 ns and ten simulations of 20 ns, all with different initial velocities, were run giving a combined duration of 1 μs for each protein. Trajectories were also initiated from open structures (PDB: 1VRS chain B) (Rozhkova et al., 2004); eight and ten 10 ns trajectories were run for nDsbDred and nDsbDox, respectively. Missing side-chain atoms were added using the WHAT-IF Server (https://swift.cmbi.umcn.nl/whatif) (Hekkelman et al., 2010). The histidine side chains were protonated and the cysteine side chains (C103 and C109) in the active site of nDsbDred were represented as thiols; these choices were based on pH titrations monitored by NMR (Mavridou et al., 2012). The protein was embedded in rhombic dodecahedral boxes with a minimum distance to the box edges of 12 Å at NaCl concentrations of 0.1 M. Trajectories using a larger distance of 15 Å to the box edges showed no significant differences. The CHARMM 22 force field (MacKerell et al., 1998) with the CMAP correction (Mackerell et al., 2004) and the CHARMM TIP3P water model was used. Electrostatic interactions were calculated with the Particle Mesh Ewald method (PME) (Essmann et al., 1995). The Lennard-Jones potential was switched to zero between 10 Å and 12 Å (Bjelkmar et al., 2010). The length of bonds involving hydrogen atoms was constrained using the PLINCs algorithm (Hess, 2008). The equations of motion were integrated with a 2 fs time step. The simulation systems were relaxed by energy minimization and 4 ns of position-restrained MD in the NVT ensemble before starting the production simulations in the NPT ensemble at 25°C and 1 bar for 10 ns, 20 ns or 200 ns. The Bussi-Donadio-Parinello thermostat (Bussi et al., 2007), with a τT of 0.1 ps, and the Parinello-Rahman barostat (Parrinello and Rahman, 1981), with a τP of 0.5 ps and a compressibility of 4.5 × 105 bar−1, were used.

### Analysis of the MD simulations

The Visual Molecular Dynamics (VMD) program (Humphrey et al., 1996), GROMACS (Van Der Spoel et al., 2005) and the MDAnalysis Python library (Michaud-Agrawal et al., 2011) were used to measure parameters including distances, torsion angles, accessibility and hydrogen bonds from the MD simulations. To validate our MD simulations, amide order parameters (S2) and residual dipolar couplings (RDCs) were calculated from them. Before calculating S2 and RDCs, we removed the overall tumbling from the simulations by aligning each frame to a reference structure. Order parameters were calculated in five ns blocks from the MD trajectories (Chandrasekhar et al., 1992) with S2 given by:

$$
S^{2}=\frac{1}{2}[3\sum\alpha=13\sum\beta=13⟨\mu^_{\alpha}\mu^_{\beta}⟩−1],
$$

where α and β denote the x,y,z components of the bond vector μ.

To calculate RDCs, the principle axes of the reference structure were aligned with the experimentally determined alignment tensor. The use of a single reference structure is justified given the stability of the overall fold of nDsbD in the simulations. The RDC for a given residue in a given structure was then calculated using:

$$
D¯=\frac{k}{R^{3}}(A_{x}cos^{2}\theta_{1}+A_{y}cos^{2}\theta_{2}+A_{z}cos^{2}\theta_{3}),
$$

where κ depends on the gyromagnetic ratios γI γS, the magnetic permittivity of vacuum μ0 and Planck's constant and is defined as:

$$
k=−\frac{3}{8\pi^{2}}\gamma_{I}\gamma_{S}\mu_{0}ℏ
$$

R is the bond length and was uniformly set to 1.04 Å. The angles θ1, θ2 and θ3 describe the orientation of the individual bonds with respect to the three principal axes of the alignment tensor. Ax, Ay and Az are the principal components of the alignment tensor. Errors in these S2 and RDC values were estimated using random sampling with replacement of the 200 five ns simulation segments.

### Bioinformatics

2753 bacterial and archaeal representative proteomes from the NCBI database were searched for homologs of the N-terminal domain of Escherichia coli DsbD (nDsbD) (residues M1-V132) using blastp 2.2.28+ (NCBI) with the following cut-off values: evalue <0.01, identity >20%, coverage >50%. Hits were subsequently used as a blastp query against the E. coli MG1655 proteome (evalue <0.01) and only the ones giving DsbD as best hit were retained. A full-length DsbD phylogenetic tree was built using fasttree 2.1.7 (Price et al., 2010) using the wag option. A subset of 731 sequences clustering around the E. coli DsbD were selected for subsequent analysis as a consistent phylogenetic group of proteins, mostly belonging to the β- and γ-proteobacteria. One sequence per bacterial genus was selected; this gave a set of 134 sequences which were aligned using muscle 3.8.31 (Edgar, 2004). Percent conservation of individual positions was calculated using an in-house script.

### Crystallization, data collection, and structure determination of Δloop-nDsbDox

Crystals of Δloop-nDsbDox were obtained in vapour diffusion hanging drops containing a 1:1 mixture of Δloop-nDsbDox (10 mg/ml) in 20 mM Tris-HCl (pH 7.5), 50 mM NaCl and reservoir solution containing 28% w/v PEG 4000, 0.1 M ammonium sulphate and 0.1 M sodium acetate (pH 5.0); these conditions had previously yielded diffraction-quality crystals for nDsbDred (Mavridou et al., 2011). The reservoir was sealed with vacuum grease and incubated at 16°C. Crystals were cryoprotected by soaking for a few seconds in 20% v/v glycerol and 80% v/v reservoir solution, and frozen directly in the nitrogen stream of the X-ray apparatus. Datasets were collected with an oscillation angle of 162° (1°/frame) on a Rigaku RU-H3R rotating anode X-ray generator equipped with an R-AXIS IV image plate detector and an Oxford Cryosystems cryostream.

Diffraction data were processed and scaled with the Denzo/Scalepack package (Otwinowski and Minor, 1997). Although datasets were initially collected to a resolution of 2.20 Å, completeness was low due to damage of the crystals because of ice formation. It was, therefore, decided to refine the data to 2.60 Å resolution to have satisfactory completeness (overall above 80%). The crystals belonged to space group P21 (a = 37.33 Å, b = 81.34 Å, c = 46.39 Å and β = 100.66°). Five percent of reflections were flagged for Rfree calculations. The structure was solved by molecular replacement with MOLREP (Murshudov et al., 1997) using the wild-type nDsbDred structure (PDB accession code 3PFU) as a search model (Mavridou et al., 2011), and refined with Phenix.refine (Adams et al., 2010) and Coot (Emsley et al., 2010), which was used for manual fitting. The refinement converged at R = 25.2% and Rfree = 29.2%. Two protein molecules were found per asymmetric unit and 59 water molecules were also modelled. No electron density was observed before residue 10 and after residue 120, and before residue nine and after residue 121 in chains A and B, respectively. The coordinates are deposited in the Protein Data Bank (PDB accession code 5NHI).

# Decoding the physical principles of two-component biomolecular phase separation

## Authors

- Yaojun Zhang<sup>1</sup> ([ORCID: 0000-0003-4587-6834](https://orcid.org/0000-0003-4587-6834))
- Bin Xu<sup>2</sup>
- Benjamin G Weiner<sup>2</sup> ([ORCID: 0000-0002-1995-8660](https://orcid.org/0000-0002-1995-8660))
- Yigal Meir<sup>2</sup>
- Ned S Wingreen<sup>4</sup> ([ORCID: 0000-0001-7384-2821](https://orcid.org/0000-0001-7384-2821)) †

### Affiliations

1. Center for the Physics of Biological Function, Princeton University Princeton United States
2. Department of Physics, Princeton University Princeton United States
3. Department of Physics, Ben Gurion University of the Negev Beersheba Israel
4. Department of Molecular Biology, Princeton University Princeton United States
5. Lewis-Sigler Institute for Integrative Genomics, Princeton University Princeton United States

† Corresponding author

## Abstract

Cells possess a multiplicity of non-membrane-bound compartments, which form via liquid-liquid phase separation. These condensates assemble and dissolve as needed to enable central cellular functions. One important class of condensates is those composed of two associating polymer species that form one-to-one specific bonds. What are the physical principles that underlie phase separation in such systems? To address this question, we employed coarse-grained molecular dynamics simulations to examine how the phase boundaries depend on polymer valence, stoichiometry, and binding strength. We discovered a striking phenomenon – for sufficiently strong binding, phase separation is suppressed at rational polymer stoichiometries, which we termed the magic-ratio effect. We further developed an analytical dimer-gel theory that confirmed the magic-ratio effect and disentangled the individual roles of polymer properties in shaping the phase diagram. Our work provides new insights into the factors controlling the phase diagrams of biomolecular condensates, with implications for natural and synthetic systems.

## Introduction

Eukaryotic cells are host to a multiplicity of non-membrane-bound compartments. Recent studies have shown that these compartments form via liquid-liquid phase separation (Brangwynne et al., 2009; Li et al., 2012; Molliex et al., 2015). The phase-separated condensates enable many central cellular functions – from ribosome assembly, to RNA regulation and storage, to signaling and metabolism (Shin and Brangwynne, 2017; Banani et al., 2017). Unlike conventional liquid-liquid phase separation, for example water-oil demixing, the underlying interactions that drive biomolecular phase separation typically involve strong one-to-one saturable interactions, often among multiple components (Ditlev et al., 2018). As a result, the phase diagrams of biomolecular condensates are complex and are sensitive to a variety of physical properties of the biomolecules, included number of binding sites, binding strengths, and additional nonspecific interactions. Importantly, these physical parameters can be subject to biological regulation, and can thus directly impact the organization and function of the condensates. It is therefore crucial to understand how the physical properties of the components shape the phase diagram of biomolecular condensates.

Biomolecular condensates typically contain tens to hundreds of types of molecules. Yet, when characterized in detail, only a small number of components are responsible for condensate formation (Ditlev et al., 2018). One class of such condensates are those formed by the association of two essential components. In the simplest case, each component consists of repeated domains/stickers that bind in a one-to-one fashion with the domains of the other component (Figure 1A and B; Choi et al., 2019; Xu et al., 2020). Such two-component condensates have been observed in both natural and engineered contexts. For example, the pyrenoid, an organelle responsible for carbon fixation in the alga Chlamydomonas reinhardtii, is a condensate of the CO2-fixing enzyme Rubisco with the linker protein Essential PYrenoid Component 1 (EPYC1). EPYC1 consists of five evenly-spaced Rubisco-binding regions, while Rubisco holoenzyme has eight specific binding sites for EPYC1. Multivalent interactions between Rubisco and EPYC1 are responsible for pyrenoid formation (Freeman Rosenzweig et al., 2017; Wunder et al., 2018; He et al., 2020). Promyelocytic leukemia (PML) nuclear bodies are condensates of PML proteins. PML is SUMOylated at three main positions and several minor sites. These modifications and a C-terminal SUMO Interaction Motif (SIM) found in most PML isoforms contribute to the formation of these bodies (Shen et al., 2006). Engineered polySUMO and polySIM proteins (10 repeats of Small Ubiquitin-like Modifier [SUMO] and SIM, respectively) phase separate when mixed together, but not as individual components (Banani et al., 2016; Ditlev et al., 2018).

![Figure 1.](https://cdn.elifesciences.org/articles/62403/elife-62403-fig1-v1.jpg)

**Figure 1.:** (A) Schematic of multivalent associative polymers. Each polymer consists of complementary domains (stickers) connected by flexible linkers (spacers). A and B denote the polymer type and m and n denote their valences (number of stickers). (B) Association of stickers drives phase separation, leading to the formation of a dense, network phase coexisting with a dilute phase of small oligomers (depicted by a dimer). (C) The phase diagram depends on variety of biologically tunable parameters. In this study, we focus on the effects of sticker-sticker binding strength, sticker:sticker concentration ratio (i.e. stoichiometry), and polymer valences. (D) Schematic of a representative 3D phase diagram of an $A_{n}:B_{n}$ system as a function of temperature (inverse of binding strength) and A and B sticker concentrations. The dilute-phase concentration displays anomalous dependence on the binding strength and sticker concentrations in the strong binding regime. This is the ‘magic-ratio’ effect which we explore here in detail.

Previous simulations (Freeman Rosenzweig et al., 2017; Xu et al., 2020) of average cluster size in such two-component systems revealed a striking phenomenon – for sufficiently strong binding, the formation of large clusters is suppressed when the valence of one species equals or is an integral multiple of the valence of the other species, favoring the formation of small stable oligomers instead of a condensate. The phenomenon reminiscent of the exact filling of atomic shells leading to the unreactive noble gases was termed the ‘magic-number’ effect. A similar effect was found in a ternary system modeling the clustering of nephrin, Nck, and NWASP proteins which regulates cell-cell adhesion in podocyte cells of the kidney (Chattaraj et al., 2019). However, cluster size may reflect a sol-gel percolation transition rather than a thermodynamic phase transition (Harmon et al., 2017), and thus provides at best a qualitative measure of phase separation. Moreover, these previous studies focused on equal sticker stoichiometry, whereas biomolecular condensates cover a broad range of stoichiometries both in vitro (Li et al., 2012; Banani et al., 2016) and in vivo (Sanders et al., 2020).

Here, we directly delineate the full phase diagram of such two-component systems. Using coarse-grained molecular dynamics simulations, we explore systematically how phase boundaries depend on valence, stoichiometry, and binding strength of two associating polymers (Figure 1C and D). Our studies reveal an unanticipated effect – when the numbers of polymers of the two types have a rational stoichiometry (1:1, 1:2, etc.), phase separation can be strongly suppressed, which we call the ‘magic-ratio’ effect (Figure 1D, phase diagram at low temperatures). To understand the magic-ratio effects better, we develop a two-component sticker theory à la Semenov and Rubinstein (Semenov and Rubinstein, 1998). We model the system as dominated by polymer dimers in the dilute phase and by a condensate of independent stickers in the dense phase (Figure 1B). The resulting analytical theory captures the magic-ratio effect discovered in simulations, and allows us to disentangle the individual roles of valence, stoichiometry, specific-bond strength, and nonspecific attraction in determining the phase boundaries of two-component multivalent systems. Living cells regulate the valence and interactions of biomolecules through chemical modification, or on a slower timescale, tune the stoichiometry via synthesis/degradation or sequestration, and over evolutionary time, adapt the strength of specific and nonspecific interactions through mutation of molecular sequences. Understanding the individual roles of these biologically tunable variables thus brings new insights into possible cellular strategies for regulating the formation and dissolution of biomolecular condensates.

## Results

### Coarse-grained molecular-dynamics simulations

We perform coarse-grained molecular-dynamics simulations using LAMMPS (Plimpton, 1995) to determine the phase boundaries of two-component multivalent systems (Figure 2). Briefly, we model the two polymer species as flexible linear chains of beads connected by harmonic springs (Figure 2A). Each bead represents one associative domain/sticker of the polymer. To ensure associative domains of different polymer types bind in a one-to-one fashion, we impose a finite-ranged attractive interaction between beads of different types. This, however, could lead to more than one-to-one associations. Therefore, to avoid such unwanted associations, we impose strong repulsive interactions between beads of the same type over a large enough range to prevent other beads overlapping with a bound pair, thus preventing multiple-to-one binding (Figure 2B and Appendix 1—figure 1), see Appendix 1 for details.

![Figure 2.](https://cdn.elifesciences.org/articles/62403/elife-62403-fig2-v1.jpg)

**Figure 2.:** (A) The system consists of two types of polymers A (blue) and B (red) of varying lengths and concentrations. Depicted are A and B polymers of length 10, denoted as A10 and B10. Each polymer is modeled as a linear chain of spherical particles connected by harmonic bonds. Stickers of different types interact pairwisely through an attractive potential, while repulsion between stickers of the same type prevents them from overlapping and thus ensures one-to-one binding of stickers of different types (see Appendix 1 for details). (B) Snapshots of dimers formed by A10 and B10 with one-to-one bonds. (C) Snapshot of a simulation with 125 A10 and 125 B10 polymers. The system phase separates into a dense phase (middle region) and a dilute phase (two sides) in a 250 nm×50 nm×50 nm simulation box with periodic boundary conditions. (D) Same as C but with 138 A10 and 112 B10 polymers, yielding an overall sticker concentration ratio 1.23. (E) Sticker concentration profiles of A10:B10 systems at various overall sticker stoichiometries (total global sticker concentration fixed at 6.64 mM), each with the center of the dense phase aligned at $x=0$ and averaged over time and over ten simulation repeats (see Appendix 1). All simulations performed in LAMMPS (Plimpton, 1995).

To find the binodal phase boundaries, we simulate hundreds of polymers of types A and B with, respectively, m and n stickers (an $A_{m}:B_{n}$ system) in a box with periodic boundary conditions (Figure 2C and D). We initialize the system by constructing a dense slab of polymers in the middle of the box (Dignon et al., 2018). The system evolves and relaxes according to Langevin dynamics (Langevin, 1908). After the system has achieved equilibrium, two phases coexist: a dilute phase consisting of dimers and other small oligomers, and a dense phase of an interconnected polymer condensate. We measure the corresponding density profile (Figure 2E) and calculate the dilute- and dense-phase concentrations by averaging the density profile over the regions ($x\leq−100nm$ or $x\geq100nm$) and ($−10nm\leqx\leq10nm$), respectively. See Appendix 1 for simulation details.

#### Effect of valence

It was shown previously that for equal sticker stoichiometry in the strong-binding regime, clustering is substantially suppressed when the number of binding sites on one polymer species is an integer multiple of the number of binding sites on the other, as this condition favors the assembly of small oligomers in which all binding sites are saturated (Freeman Rosenzweig et al., 2017; Xu et al., 2020). What does this magic-number effect imply for the actual phase diagram? To address this question, we fix the valence of polymer A at 14 and systematically vary the valence of polymer B from 5 to 16 while keeping the two sticker concentrations the same, that is, at equal global sticker stoichiometry.

Figure 3A and B show simulation results for the total sticker concentrations of the dilute and dense phases for A14:B5 to A14:B16 systems. In the strong binding regime, for magic-number cases, that is when the valence of B is 7 or 14, the dilute-phase concentration shows pronounced peaks (Figure 3A, black curve). What is the origin of the peak at A14:B14? Intuitively, when the dilute phase of the two-component system is dominated by dimers (for systems A14:B12 to A14:B16, as supported by cluster size analysis in Appendix 1—figure 2), each of these dimers has high translational entropy, whereas polymers in the dense condensate have low translational entropy. For A14:B14, all binding sites can pair up in a dimer just as well as in the condensate, so the energy per polymer is not necessarily lower in the condensate. Why then is the condensate still competitive with the dilute phase? In a dimer, the binding sites of A14 must match all the binding sites of B14, leading to a reduced overall conformational entropy. By comparison, the polymers in the condensate are more independent, binding to multiple members of the other species and enjoying a relatively higher overall conformational entropy. Because the translational entropy of each dimer decreases as their concentration goes up, the condensed phase eventually becomes more favorable and so the system phase separates with increasing concentration. Therefore, phase separation in A14:B14 is primarily driven by a competition between translational entropy and conformational entropy.

![Figure 3.](https://cdn.elifesciences.org/articles/62403/elife-62403-fig3-v1.jpg)

**Figure 3.:** Total sticker concentrations (type A plus type B) in (A) dilute and (B) dense phases for simulated polymer systems at different binding strengths. U0 denotes the depth of the potential well, in units of $k_{B}⁢T$ (see Appendix 1 for details). The valence of polymer A is 14, and the valence of polymer B ranges from 5 to 16. Global sticker stoichiometry is one and total global sticker concentration is 6.64 mM. Histograms of cluster size in (C) A14:B14 and (D) A14:B6 systems, for $U_{0}=14$. ‘Counts’ refer to number of clusters. Cluster size is measured in stickers. Red dots indicate the dominant oligomer in the dilute phase.

By contrast, for A14:B13 and A14:B15, one of the stickers in the dimer cannot be paired, and for A14:B12 and A14:B16, two stickers per dimer cannot be paired. Therefore, forming a condensate not only increases the conformational entropy but more importantly lowers the energy of these systems. This significantly tilts the balance in favor of condensation. As a result, the dilute-phase concentration is sharply peaked at A14:B14, falling off rapidly for increasingly unequal polymer lengths. We note that the dense-phase concentration shows no such feature (Figure 3B), indicating that the peak at A14:B14 does not arise from differences in the internal structure of the dense phase.

The dilute phase of two-component systems is not always dominated by dimers (Appendix 1—figure 2). For example, the dilute phase of the A14:B7 system is dominated by fully-bonded trimers with 1 A14 and 2 B7, the dilute phase of A14:B8 is dominated by trimers with 1 A14 and 2 B8, which has two unpaired stickers per trimer, and the dilute phase of A14:B6 is dominated by oligomers with 3 A14 and 7 B6, which although fully-bonded is not small (Figure 3D). Consistent with the above logic, we find another peak in the dilute-phase concentration at A14:B7 (Figure 3A). More generally, in contrast to the magic-number systems, the dilute phases in other cases are dominated by oligomers which are not capable of being fully bonded (high energy) and/or not small (low translational entropy) (Appendix 1—figure 2). The dilute-phase concentration is therefore lower in these non-magic-number cases.

#### Effect of binding strength

How do the phase boundaries depend on the strength of binding? Figure 3A shows that, for non-magic-number systems, the dilute-phase concentration decreases monotonically with increasing binding strength, whereas for magic-number systems the dependence can be non-monotonic. This difference is attributed to the distinct underlying driving forces for phase separation. For non-magic-number systems, as clustering allows a larger fraction of binding sites to be paired, the stronger the binding, the more the energy is lowered by condensate formation. Therefore, the dilute-phase concentration drops as binding strength increases (or as temperature decreases). Such energy-dependence is expected for conventional phase-separation models, such as Flory, 1942; Huggins, 1941.

Interestingly, for the magic-number system A14:B14, the dilute-phase concentration first decreases with increasing binding strength in the weak binding regime, similar to non-magic-number systems. However, as the binding energy is increased further, most of binding sites pair up in both dilute and dense phases. Phase separation is then primarily driven by a competition between conformational and translational entropy. The pairing up of binding sites reduces the conformational entropy of both the dense and dilute phases. By contrast, the translational entropy of the dilute-phase components is almost unaffected. Consequently, the dilute phase becomes more competitive relative to the condensate, so the dilute phase boundary shifts to higher concentration.

By comparison, the dense-phase concentration increases monotonically with increasing binding strength for all systems (Figure 3B). This follows because the stronger the binding, the more stickers are paired, which tightens the condensate structure. We note that at substantially higher binding energies than studied here, essentially all the binding sites are satisfied in both magic-number and non-magic-number systems, and the phase boundaries become independent of binding energy.

#### Effect of sticker stoichiometry

How do the phase boundaries depend on overall sticker stoichiometry? Figure 4A and B show total sticker concentrations of the dilute and dense phases for magic-number systems A8:B8 to A14:B14 at different global sticker stoichiometries. For each system, the dilute-phase concentration peaks at equal sticker ratio, falls off initially as the ratio deviates from 1, and then curves back up. What is the origin of the peak at equal sticker stoichiometry? Recall that, in the strong binding regime, phase separation of magic-number systems is primarily driven by a competition between translational entropy and conformational entropy. Now consider starting with a system at equal sticker concentration, and adding more of one polymer species to the system. At the beginning, the added polymers readily enter the dense phase, which relaxes the conformational constraint that every sticker in the condensate has to pair with a partner. This increase of the conformational entropy of the condensate makes it more competitive, so the dilute-phase concentration decreases. However, as the ratio between the two polymers is increased further, it becomes possible to form a spectrum of dilute-phase oligomers which typically contain one extra polymer of the majority type (Appendix 1—table 1). These new oligomers have more relaxed structures than fully bonded dimers, which raises the conformational entropy of the dilute phase. Therefore, the dilute phase is favored over the condensate and its concentration curves back up.

![Figure 4.](https://cdn.elifesciences.org/articles/62403/elife-62403-fig4-v1.jpg)

**Figure 4.:** Sticker concentrations in (A) dilute and (B) dense phases for equal polymer length systems (i.e. $A_{n}:B_{n}$) at different global sticker stoichiometries. Sticker concentrations in (C) dilute and (D) dense phases for systems where polymer B is one sticker shorter than polymer A (i.e. $A_{n}:B_{n−1}$) at different global sticker stoichiometries; black dots indicate cases where the number of polymers of each type is the same. Interaction strength $U_{0}=14$ and total global sticker concentration 6.64 mM.

Figure 4A also reveals that the dilute-phase concentration decreases with increasing polymer valence. This follows in part because translational entropy in the dilute phase is per dimer center of mass, whereas conformational entropy in both phases scales with the number of stickers. The entropic gain of joining the dense phase is therefore more on a per sticker basis for longer polymers, so the dilute-phase concentration decreases with increasing valence. As a less apparent yet important point, Figure 4A also shows that increasing polymer valence enhances both the width and relative height of the peak in the dilute-phase concentration. The inferred phase diagram for the A8:B8 system at $U_{0}=14⁢k_{B}⁢T$ is shown in Appendix 1—figure 3 together with the homogeneous gelation/percolation threshold obtained at $U_{0}=8⁢k_{B}⁢T$. We also report in Appendix 1—figure 5C the volume fraction of the polymers in the dense phase, which is ∼10%, comparable to the volume fraction of proteins in the cell cytoplasm.

Figure 4C and D show total sticker concentrations of the dilute and dense phases for unequal valence polymers A8:B7 to A14:B13 at different global sticker stoichiometries. The dilute phase boundary shows a symmetric minimum around equal stoichiometry for A8:B7, yet surprisingly, the phase boundary becomes asymmetric and then peaks at equal polymer stoichiometry with increasing polymer length (Figure 4C). What is the origin of these peaks? Taking the A14:B13 system as an example, its dilute phase is dominated by dimers with an unpaired A sticker. This strongly disfavors the dilute phase in the strong binding regime at equal sticker stoichiometry. However, as the overall A:B sticker stoichiometry increases, the excess As cannot be paired anyway. In particular, at equal polymer stoichiometry (denoted as black dots in Figure 4C), forming dimers is no longer energetically costly. Therefore, to the left of the A14:B13 peak at equal polymer stoichiometry, the dilute-phase concentration is low because dimers are energetically disfavored as more bonds can be satisfied in the condensate. By contrast, to the right of the peak, the dilute-phase concentration is low for a different reason – because the condensate is entropically favored, similar to the peak with respect to stoichiometry for magic-number systems. Eventually, the dilute-phase concentration curves back up due to formation of higher oligomers in the dilute phase, as discussed for magic-number systems.

We note that for all these systems the dense-phase concentration shows no such striking features. Rather, the concentration decreases monotonically as the global sticker stoichiometry departs from one and as the valence of polymers decreases (Figure 4B and D).

#### Effect of valence and stoichiometry

Above, we considered the role of both relative valence and relative stoichiometry. By plotting phase boundaries as joint functions of valence and stoichiometry, we obtain a unified picture: Figure 5A and B show the dilute- and dense-phase concentrations for systems A14:B12-16 at global sticker stoichiometries 14:12-16. Notably, the dilute-phase concentration is peaked along the diagonal (Figure 5A), that is at equal polymer stoichiometry, which we term the 'magic-ratio' effect because it occurs for rational ratios of associative polymers. Intuitively, all cases along the diagonal favor 1:1 polymer dimers: the dimers enjoy high translation entropy and there is no energy penalty involved in their formation. Thus, a dilute phase of dimers is strongly favored at equal polymer stoichiometry.

![Figure 5.](https://cdn.elifesciences.org/articles/62403/elife-62403-fig5-v1.jpg)

**Figure 5.:** Sum of concentrations of stickers A and B in (A) dilute and (B) dense phases for systems A14:B12-16 at global sticker stoichiometries 14:12-16. Parameters: interaction strength $U_{0}=14$ and total global sticker concentration 6.64 mM.

As for the dense phase concentration, it decreases monotonically as the global sticker stoichiometry departs from one and as the valence of polymers decreases (Figure 5B). This again indicates that the anomalous dependence of the dilute-phase concentration on valence and stoichiometry does not arise from special properties of the dense phase.

### Dimer-gel theory

While our simulations have revealed that a magic-ratio effect influences the boundaries of phase separation for associating polymers, we desire a deeper understanding of the interplay of factors such as overall valence, stoichiometry, and interaction strength. To this end, we develop a mean field theory of two-component associative polymers à la Semenov and Rubinstein (Semenov and Rubinstein, 1998; Xu, 2018).

Specifically, we consider a system of A and B polymers as in our simulations. Each polymer is a linear chain of L1 or L2 stickers of type A or type B, respectively. Without loss of generality, we take $L_{1}\geqL_{2}$. stickers of different types associate in a one-to-one fashion. Our simulations suggest that for polymers of similar valence close to equal polymer stoichiometry the dilute phase is dominated by dimers and the dense phase is a gel network. Therefore, we assume that polymers can associate either as dimers or, alternatively, as a condensate in which pairs of stickers bind independently. This assumption of independence is a mean field approximation, as it neglects correlations between stickers in the same chain, and thus only applies when the polymers strongly overlap, that is at densities above the semidilute regime (De Gennes, 1979).

The partition function of such a system can be divided into three parts: $Z=Z_{ni}⁢Z_{s}⁢Z_{ns}$, where $Z_{ni}$, the partition function of a solution of non-interacting polymers, captures the translational and conformational entropy of the two polymer species, $Z_{s}$ captures specific interactions between associating stickers, and $Z_{ns}$ captures all nonspecific interactions.

The corresponding free-energy density for the mixed non-interacting polymers is Semenov and Rubinstein, 1998:

$$
\frac{F_{ni}}{k_{B}⁢T}=\frac{c_{1}}{L_{1}}⁢ln⁡\frac{c_{1}}{e⁢L_{1}}+\frac{c_{2}}{L_{2}}⁢ln⁡\frac{c_{2}}{e⁢L_{2}},
$$

where c1 and c2 are the concentrations of A and B polymers measured in terms of stickers. Note that the terms for the conformational entropy of non-interacting polymers are omitted in Equation 1, as they are linear in c1 and c2 and thus do not influence the phase boundaries.

To include specific interactions, we first consider the partition function $Z_{s}⁢(N_{d1},N_{d2},N_{b})$ for states with exactly $N_{d1}$ and $N_{d2}$ total numbers of stickers of A and B types in dimers (i.e. number of dimers equals $N_{d1}/L_{1}=N_{d2}/L_{2}$) and $N_{b}$ additional sticker pairs,

$$
Z_{s}⁢(N_{d1},N_{d2},N_{b})=P⁢(N_{d1},N_{d2},N_{b})⁢W⁢(N_{d1},N_{d2},N_{b})⁢exp⁡(N_{d1}⁢ϵ_{d}/L_{1}+N_{b}⁢ϵ_{b}).
$$

In Equation 2, P is the number of different ways that polymers and stickers can be chosen to pair up to form dimers and independent bonds,

$$
P(N_{d1},N_{d2},N_{b})=(N_{1}/L_{1}N_{d1}/L_{1})(N_{2}/L_{2}N_{d2}/L_{2})(N_{d1}/L_{1})!(N_{1}−N_{d1}N_{b})(N_{2}−N_{d2}N_{b})N_{b}!,
$$

where N1 and N2 are the total numbers of stickers of A and B types. (Note that in Equation (3) if $L_{1}>L_{2}$, the excess stickers of type A in dimers do not form additional bonds.) In Equation (2), W is the probability that all chosen polymers and stickers are, respectively, close enough to their specified partners in the non-interacting state to form dimers and independent bonds,

$$
W⁢(N_{d},N_{b})=(\frac{v_{d}}{V})^{\frac{N_{d1}}{L_{1}}}⁢(\frac{v_{b}}{V})^{N_{b}},
$$

where $v_{d}$ and $v_{b}$ are effective interaction volumes and V is the system volume. The last term in Equation (2) is the Boltzmann factor for specific interactions, where $ϵ_{d}$ and $ϵ_{b}$ are the effective binding energies of dimers and sticker pairs, in units of $k_{B}⁢T$.

The part of the free-energy density due to specific interactions is

$$
\frac{F_{s}}{k_{B}⁢T}=-\frac{1}{V}⁢ln⁡Z_{s}.
$$

Using Stirling’s approximation $ln⁡N!=N⁢ln⁡N-N$, we obtain

$$
\frac{F_{s}}{k_{B}T}=−\frac{c_{1}}{L_{1}}ln⁡c_{1}+(1−L_{1})\frac{c_{1}−c_{d1}}{L_{1}}ln⁡(c_{1}−c_{d1})+(c_{1}−c_{d1}−c_{b})ln⁡(c_{1}−c_{d1}−c_{b})−\frac{c_{2}}{L_{2}}ln⁡c_{2}+(1−L_{2})\frac{c_{2}−c_{d2}}{L_{2}}ln⁡(c_{2}−c_{d2})+(c_{2}−c_{d2}−c_{b})ln⁡(c_{2}−c_{d2}−c_{b})+\frac{c_{d1}}{L_{1}}ln⁡(ec_{d2}L_{1}K_{d})+c_{b}ln⁡(ec_{b}K_{b}),
$$

where $K_{d}≡e^{-ϵ_{d}}/v_{d}$ and $K_{b}≡e^{-ϵ_{b}}/v_{b}$ are, respectively, the dissociation constants of a dimer and of a pair of stickers. $c_{d1}$ and $c_{d2}$ are the concentrations of stickers of A and B types in dimers (so $c_{d1}/L_{1}=c_{d2}/L_{2}$), and $c_{b}$ is the concentration of independent bonds.

In the thermodynamic limit, $F_{s}$ will be minimized with respect to $c_{d1}$, $c_{d2}$ and $c_{b}$, which implies

$$
K_{d}c_{d2}L_{1}(c_{1}−c_{d1})^{L_{1}−1}(c_{2}−c_{d2})^{L_{2}−1}=(c_{1}−c_{d1}−c_{b})^{L_{1}}(c_{2}−c_{d2}−c_{b})^{L_{2}},
$$



$$
K_{b}c_{b}=(c_{1}−c_{d1}−c_{b})(c_{2}−c_{d2}−c_{b}).
$$

Note that if $c_{b}$ in Equation (7) and $c_{d1}$ and $c_{d2}$ in Equation (8) are set to zero, these equations reduce to

$$
K_{d}ρ_{d}=(ρ_{1}−ρ_{d})(ρ_{2}−ρ_{d}),
$$



$$
K_{b}c_{b}=(c_{1}−c_{b})(c_{2}−c_{b}),
$$

where $ρ_{1}$, $ρ_{2}$, and $ρ_{d}$ are the total concentrations of A and B polymers and dimers (measured in polymeric units), that is, $ρ_{1}=c_{1}/L_{1}$, $ρ_{2}=c_{2}/L_{2}$, and $ρ_{d}=c_{d1}/L_{1}=c_{d2}/L_{2}$. Equations (9) and (10) are consistent with the definitions of the dissociation constants of a dimer and of an independent bond, respectively.

The free-energy density due to nonspecific interactions can in general be written as a power expansion in the concentrations (Semenov and Rubinstein, 1998; De Gennes, 1979),

$$
\frac{F_{ns}}{k_{B}⁢T}=\frac{1}{2}⁢\sumi⁢jv_{i⁢j}⁢c_{i}⁢c_{j}+\frac{1}{6}⁢\sumi⁢j⁢kw_{i⁢j⁢k}⁢c_{i}⁢c_{j}⁢c_{k},
$$

where the sum is over all the species in the system, including free polymers/stickers, dimers and independent bonds, and $v_{i⁢j}$ and $w_{i⁢j⁢k}$ are two- and three-body interaction parameters. For our simulation system, we derive a specific form of $F_{ns}$ by taking into account that (1) we are interested in the strong-binding regime where the magic-ratio effect is observed, (2) there is no nonspecific interaction between free polymers of different types in our simulation, and (3) nonspecific interactions are only important at high concentrations. The result is

$$
\frac{F_{ns}}{k_{B}⁢T}=\frac{v_{b}}{2}max(c_{1},c_{2})^{2}+\frac{w_{b}}{6}max(c_{1},c_{2})^{3},
$$

where vb and wb are the two- and three-body interaction parameters for a solution of independent bonds. See Appendix 2 for details of the derivation.

Finally, substituting the conditions Equations (7) and (8) into Equation (6), we obtain the total free-energy density $F=F_{ni}+F_{s}+F_{ns}$,

$$
\frac{F}{k_{B}T}=\frac{c_{1}}{L_{1}}ln⁡\frac{c_{1}−c_{d1}}{eL_{1}}+c_{1}ln⁡\frac{c_{1}−c_{d1}−c_{b}}{c_{1}−c_{d1}}+\frac{c_{d1}}{L_{1}}+\frac{c_{2}}{L_{2}}ln⁡\frac{c_{2}−c_{d2}}{eL_{2}}+c_{2}ln⁡\frac{c_{2}−c_{d2}−c_{b}}{c_{2}−c_{d2}}+c_{b}+\frac{v_{b}}{2}max(c_{1},c_{2})^{2}+\frac{w_{b}}{6}max(c_{1},c_{2})^{3},
$$

where $c_{d1}$, $c_{d2}$, and $c_{b}$ are the solutions of Equations (7) and (8). Equations (7), (8) and (13) form a complete set which predicts the free-energy density of the two-component associative polymer system at given total global sticker concentrations, c1 and c2, of the two species.

Intuitively, in the strong-binding regime, that is when $c_{1},c_{2}≫K_{d},K_{b}$, polymers either associate as dimers or as independent bonds depending on their relative free energies. In the limit that dimers are preferred ($ρ_{d}=min⁡(ρ_{1},ρ_{2})$ and $c_{b}=0$), the contribution from specific interactions is

$$
\frac{F_{s}^{dim}}{k_{B}⁢T}=ρ_{d}⁢ln⁡K_{d}+(ρ-ρ_{d})⁢ln⁡\frac{ρ-ρ_{d}}{e}-ρ⁢ln⁡\frac{ρ}{e},
$$

where $ρ=max⁡(ρ_{1},ρ_{2})$ is the concentration of the majority species in polymeric units. The terms on the right of Equation (14) reflect, respectively, the free-energy density due to dimer formation, translational entropy of leftover polymers, and loss of translational entropy of the majority species (in effect, the formation of each dimer removes the translation entropy of one free polymer). In the opposite limit that independent bonds are preferred ($c_{b}=min⁡(c_{1},c_{2})$ and $ρ_{d}=0$),

$$
\frac{F_{s}^{ind}}{k_{B}⁢T}=c_{b}⁢ln⁡K_{b}+(c-c_{b})⁢ln⁡\frac{c-c_{b}}{e}-c⁢ln⁡\frac{c}{e},
$$

where $c=max⁡(c_{1},c_{2})$, and the terms are analogous to those in Equation (14). Numerical studies show that the full $F_{s}⁢(c_{1},c_{2})$ in Equation (6) is always well approximated by the lower of the two limiting values of $F_{s}$ (Equation (14) and (15)).

In which regions of concentration space are dimers versus independent bonds preferred? For a magic-number system composed of two polymer species of valence L at equal sticker stoichiometry, $F_{s}^{dim}/k_{B}⁢T=ρ⁢ln⁡(K_{d}⁢e/ρ)$ and $F_{s}^{ind}/k_{B}⁢T=c⁢ln⁡(K_{b}⁢e/c)$. Comparing the two expressions, dimers are favored at low concentrations, whereas a network of independent bonds is favored at high concentrations. The transition occurs when $F_{s}^{dim}=F_{s}^{ind}$, that is at concentration $c_{0}=e⁢(K_{b}^{L}/(K_{d}⁢L))^{1/(L-1)}$. Away from equal stoichiometry, the transition occurs at a lower concentration $c_{s}=c_{0}⁢(s-1)^{s-1}⁢s^{-s}$, where $s=max⁡(c_{1},c_{2})/min⁡(c_{1},c_{2})>1$ (see Appendix 2 for details). As cs decreases rapidly with increasing s (Figure 6A inset, white curve), the preference for dimers over a gel exhibits a sharp peak around equal stoichiometry.

![Figure 6.](https://cdn.elifesciences.org/articles/62403/elife-62403-fig6-v1.jpg)

**Figure 6.:** Phase diagrams of (A) A8:B8 and (B) A8:B7 systems: one-phase region white, two-phase region green. The dilute- and dense-phase concentrations are connected by representative tie lines. The tie line along the direction of equal polymer stoichiometry is denoted with a black dot. Insets: fraction of stickers in dimers for (A) A8:B8 and (B) A8:B7 systems. White curve in A inset is the transition boundary between dimer- and independent bonds-dominated regions predicted by cs. Dashed white line in (B) inset denotes equal polymer stoichiometry. Sticker concentrations in (C) dilute and (D) dense phases for systems A8:B6-10 at global sticker stoichiometries 8:6-10. The total global sticker concentration is the same as in simulations, 6.64 mM. For details see Appendix 2. Parameters: $v_{b}=9\times10^{-2}⁢mM^{-1}$, $w_{b}=7\times10^{-3}⁢mM^{-2}$, $K_{b}=3.8\times10^{-3}⁢mM$, and $K_{d}$ values in Appendix 1—table 3.

To give a concrete example of the above analysis, we extract the values of $K_{d}$ for dimers from simulations, choose a value of $K_{b}$ for independent bonds close to the dissociation constant of a pair of stickers (see Appendix 2 for details), and numerically solve Equation (7) and (8) for $c_{d1}$, $c_{d2}$, and $c_{b}$ to find the fraction of stickers in dimers and independent bonds for all concentrations $(c_{1},c_{2})$. We find that indeed for polymers of equal valence, dimers are favored at low concentrations and independent bonds at high concentrations. The dimer dominated region extends sharply to higher concentrations in a narrow zone around the diagonal, as quantitatively captured by cs (Figure 6A inset and Appendix 2—figure 1A). For polymers of similar but unequal valence, the dimer dominated region extends to higher concentrations along the direction of equal polymer stoichiometry (Figure 6B inset and Appendix 2—figure 1B).

Finally, to extract the binodal phase boundaries, we substitute the values of $c_{d1}$, $c_{d2}$, and $c_{b}$ into Equation (13) to first obtain the free energy as a function of c1 and c2. The free-energy landscape has two basins, one at small concentrations corresponding to the dilute dimer-dominated phase, and one at high concentrations corresponding to the dense independent-bond-dominated gel-phase (Appendix 2—figure 2). We locate the phase boundaries by applying convex-hull analysis to this free-energy landscape (see Appendix 2).

Does the dimer-gel theory capture the magic-ratio effect revealed by our simulations? Figure 6A and B show the phase diagrams of A8:B8 and A8:B7 systems. In both cases, the phase boundaries on the dilute side extend sharply into the two-phase region along the direction of equal polymer stoichiometry (tie lines along this direction are denoted by black dots). Figure 6C and D show the dilute- and dense-phase concentrations for systems A8:B6-10 at global sticker stoichiometries 8:6-10. Notably, the dilute-phase concentrations are substantially shifted up around the diagonal, verifying the magic-ratio effect observed in simulations (Figure 5A).

One of the major assumptions of the dimer-gel theory is a mean-field approximation. Mean-field theory ignores correlations in binding between stickers in the same chain, and therefore has been applied to long chains in the weak binding regime (such that not every sticker is bound) (Prusty et al., 2018; Choi et al., 2020b). Our dimer-gel theory bypasses this stringent requirement by explicitly assuming the dilute-phase components to be dimers, and only considers stickers to associate independently in the dense phase. This approximation captures a key feature of the dense phase, namely that a single polymer binds to multiple partners. Nevertheless, because stickers belonging to the same polymer are tethered together with relatively short linkers in our simulations, correlations in binding exist (Appendix 2—figure 5A). Therefore, what should be considered to be ‘independent’ is not individual stickers but rather segments of the binding correlation length (∼1.8 stickers). The dense phase of a valence 14 system is thus more accurately described by the theory at valence $14/1.8≈8$. We therefore present results for valence eight systems in Figure 6. (The theoretical phase diagrams and the dilute- and dense-phase concentrations for valence 14 systems also verify the magic-ratio effect (Appendix 2—figure 4)).

The dimer-gel theory has only a handful of parameters: the valences L1 and L2 of polymers A and B, the dissociation constants $K_{d}$ and $K_{b}$ of dimers and independent bonds, and the nonspecific interaction parameters $v_{b}$ and $w_{b}$. How are the phase boundaries and the magic-ratio effects determined collectively by these parameters? If valence is increased while keeping all other parameters fixed in the theory, for equal valence polymers we find that the dilute-phase concentration decreases, while the dense-phase concentration increases, and the peak with respect to stoichiometry is enhanced in terms of the dilute-phase peak-to-valley ratio (Appendix 2—figure 6A and B). If valence is increased for unequal valence polymers, we observe that the shape of the dilute phase boundary transitions from a shoulder to a peak (Appendix 2—figure 6C and D). All these features are consistent with the simulation results in Figure 4.

For the theory to agree quantitatively with the phase boundaries from simulations, we find that smaller values of nonspecific interaction parameters are necessary for higher valence systems (Appendix 2—figure 6C and D). Intuitively, this follows because higher valence polymers have more backbone bonds, which bring bound sticker pairs closer together in the dense phase – effectively reducing the nonspecific repulsion between them. Finally, the dimer-gel theory also predicts that the magic-ratio effect disappears in the weak-binding regime (Appendix 2—figure 7), consistent with our simulation results (Figure 3).

## Discussion

Intracellular phase separation is driven by multivalent interactions between macromolecules. These interactions are separated into two classes (Ditlev et al., 2018; Pak et al., 2016): (1) specific interactions, such as binding between protein domains, are relatively strong and involve specific partners and (2) nonspecific interactions, such as electrostatic and hydrophobic interactions, which are much weaker, more generic, and non-saturable. Multivalent systems with specific interactions allow for ‘orthogonal’ condensates to form: the specific interactions holding together one class of droplets will typically not interfere with those holding together another class. Motivated by the key role of specific interactions in intracellular phase separation, we focused on exploring the effects of specific interactions on the phase boundaries of two-component associative polymers. Specifically, we combined coarse-grained molecular dynamics simulations and analytical theory to examine the individual roles of valence, stoichiometry, and binding strength on the phase boundaries. In particular, we identified a magic-ratio effect: for sufficiently strong binding, phase separation is strongly suppressed at equal polymer stoichiometry.

The magic-ratio effect occurs exclusively in the strong-binding regime. Are specific protein-protein, protein-RNA, and RNA-RNA interactions strong enough to lead to the magic-ratio effect? The onset of the effect in our simulations occurs around $U_{0}=9⁢k_{B}⁢T$ (Figure 3A), which corresponds to a sticker-sticker dissociation constant $K_{d}=0.4mM$. This value is consistent with the onset $K_{d}$ of 1–2.5 mM estimated from 3D lattice simulations with one polymer and one rigid component (Xu et al., 2020). For comparison, the measured $K_{d}$ for a SUMO protein domain with a SIM peptide is 0.01 mM (Banani et al., 2016) and the $K_{d}$ for an SH3 domain and a PRM peptide is 0.35 mM (Li et al., 2012). Thus for systems as strongly interacting as SUMO-SIM or SH3-PRM, the magic-ratio effect in principle should manifest in their phase diagrams. However, the magic-ratio effect has not been observed in these systems (Li et al., 2012; Banani et al., 2016), possibly due to size and linker length mismatch between the two associating polymers. Furthermore, real biological systems are more complex than our simple model. For example, there can be multiple-to-one binding, multiple components, and the spacers/linkers can also play nontrivial roles (Banjade et al., 2015; Harmon et al., 2017). Currently, the in vivo relevance of the effects explored in this work remains an open question. Magic-ratio effects could also manifest in other experimental systems, such as non-biological polymers, DNA origami (Hu and Niemeyer, 2019), or patchy colloid systems (Bianchi et al., 2011). As an inverse problem, the magic-ratio effect could be exploited to determine the relative valence of associating biomolecules by measuring their phase diagram.

The magic-ratio effect allows for novel mechanisms of regulation. Chemical modifications, such as phosphorylation or SUMOylation, which change the effective valence of one component into or out of a magic-ratio condition could shift the phase boundary as a means of condensate regulation. Cells may also have evolved to avoid magic ratios so as to better promote condensate formation. For example, EPYC1 has valence five and Rubisco has valence eight, and the geometry of binding sites on Rubisco and the length of linkers in EPYC1 are such that they disfavor fully-bonded Rubisco-EPYC1 dimers even at equal polymer stoichiometry, which suppresses the magic-ratio effect (He et al., 2020). However, active removal of a terminal EPYC1 binding site, for example by phosphorylation (Turkina et al., 2006), would dramatically change the valence ratio to 1:2, which would then favor stable trimer formation, as previously suggested (Freeman Rosenzweig et al., 2017). We hope that our work will stimulate exploration of magic-ratio effects in both natural and synthetic multivalent, multicomponent systems.

The simulations and theory presented here are aimed at providing conceptual insights into the phase separation of associating polymers that form one-to-one specific bonds. Quantitative descriptions of related real systems will likely require additional features, such as details of molecular shape and flexibility, linker lengths, as well as range and type of interactions. For example, while the magic-ratio effect is robust with respect to the strength of nonspecific interactions and linker length, these variables do strongly influence phase boundaries. The dilute-phase concentrations in our simulations are ∼mM, while the reported values for biological systems are typically tens of μM or less. The discrepancy is likely due to different strengths of nonspecific attraction, different length scales of steric replusion between stickers, and/or different lengths and flexibilities of the linkers (Bhandari et al., 2021). Indeed, increasing the nonspecific attraction in our simulations by a small amount $0.07⁢k_{B}⁢T$ leads to a 50% reduction in the dilute-phase concentration (Appendix 1—figure 4A). Reducing the steric repulsion between beads of the same type has a similar effect (Appendix 1—figure 5A). More significantly, increasing the mean linker length from 4.7 nm to 5.9 nm leads to a more than 10-fold reduction in the dilute-phase concentration (Appendix 1—figure 6A). On the other hand, the dense-phase concentration strongly depends on the steric repulsion — increasing the sticker size from 2.5 to 2.9 nm decreases the dense phase concentration by a factor of 2 (Appendix 1—figure 5B). This is consistent with results from previous studies on the role of linkers: a self-avoiding random coil linker which occupies a large volume can substantially lower the dense-phase concentration and even prevent phase separation (Harmon et al., 2017). Future work will explore the interplay between specific and nonspecific interactions, and other molecular properties, and their roles in determining the physical properties of droplets, such as surface tension, viscosity, and rate of exchange between phases.

# Noncovalent antibody catenation on a target surface greatly increases the antigen-binding avidity

## Authors

- Jinyeop Song<sup>1</sup> ([ORCID: 0000-0002-4113-5185](https://orcid.org/0000-0002-4113-5185))
- Bo-Seong Jeong<sup>2</sup> ([ORCID: 0000-0003-0629-6722](https://orcid.org/0000-0003-0629-6722))
- Seong-Woo Kim<sup>2</sup> ([ORCID: 0000-0002-4374-2093](https://orcid.org/0000-0002-4374-2093))
- Seong-Bin Im<sup>2</sup> ([ORCID: 0000-0003-1488-6386](https://orcid.org/0000-0003-1488-6386))
- Seonghoon Kim<sup>2</sup>
- Chih-Jen Lai<sup>3</sup>
- Wonki Cho<sup>2</sup>
- Jae U Jung<sup>3</sup>
- Myung-Ju Ahn<sup>4</sup>
- Byung-Ha Oh<sup>2</sup> ([ORCID: 0000-0002-6437-8470](https://orcid.org/0000-0002-6437-8470)) †

### Affiliations

1. Department of Physics, Korea Advanced Institute of Science and Technology Daejeon Republic of Korea ([ROR:05apxxy63](https://ror.org/05apxxy63))
2. Department of Biological Sciences, KAIST Institute for the Biocentury, Korea Advanced Institute of Science and Technology Daejeon Republic of Korea ([ROR:05apxxy63](https://ror.org/05apxxy63))
3. Cancer Biology Department, Infection Biology Program, and Global Center for Pathogen and Human Health Research, Lerner Research Institute, Cleveland Clinic Cleveland United States ([ROR:03xjacd83](https://ror.org/03xjacd83))
4. Department of Medicine, Samsung Medical Center, Sungkyunkwan University School of Medicine Seoul Republic of Korea ([ROR:04q78tk20](https://ror.org/04q78tk20))

† Corresponding author

## Abstract

Immunoglobulin G (IgG) antibodies are widely used for diagnosis and therapy. Given the unique dimeric structure of IgG, we hypothesized that, by genetically fusing a homodimeric protein (catenator) to the C-terminus of IgG, reversible catenation of antibody molecules could be induced on a surface where target antigen molecules are abundant, and that it could be an effective way to greatly enhance the antigen-binding avidity. A thermodynamic simulation showed that quite low homodimerization affinity of a catenator, e.g. dissociation constant of 100 μM, can enhance nanomolar antigen-binding avidity to a picomolar level, and that the fold enhancement sharply depends on the density of the antigen. In a proof-of-concept experiment where antigen molecules are immobilized on a biosensor tip, the C-terminal fusion of a pair of weakly homodimerizing proteins to three different antibodies enhanced the antigen-binding avidity by at least 110 or 304 folds from the intrinsic binding avidity. Compared with the mother antibody, Obinutuzumab(Y101L) which targets CD20, the same antibody with fused catenators exhibited significantly enhanced binding to SU-DHL5 cells. Together, the homodimerization-induced antibody catenation would be a new powerful approach to improve antibody applications, including the detection of scarce biomarkers and targeted anticancer therapies.

## Introduction

Immunoglobulin G (IgG) antibodies have become the principal therapeutic biologic. IgG antibodies are a homodimer of a heterodimer composed of two copies of each heavy chain (~50 kDa) and light chain (~25 kDa). They have two functional regions: the antigen-binding fragment (Fab) region at the N-terminal end and the fragment crystallizable (Fc) region at the C-terminal end. With an overall shape of the letter Y, the two identical regions of Fab form two arms that can bind two antigen molecules. This antibody-antigen engagement could prevent the antigen from binding to cognate partners or eliminate the antigen molecules from the cell surface by receptor-mediated endocytosis (Liu, 2018). The two copies of Fc form a homodimeric tail that enables a long half-life via binding to the neonatal Fc receptor (FcRn) and exerts effector functions via binding to the Fcγ receptors on effector immune cells or the complement factor C1q (Hogarth and Pietersz, 2012; Lee et al., 2017), which could lead to the death of cells to which antibody molecules are bound (Carter and Lazar, 2018; Goydel and Rader, 2021; Jiang et al., 2011).

IgG antibodies have desirable properties for use as a therapeutic drug, including high specificity for a target antigen, low immunogenicity and long serum half-life (Weiner et al., 2010). On the other hand, therapeutic monoclonal antibodies (mAbs) show side effects, albeit to a lesser degree in comparison with conventional chemotherapeutics, such as low or high blood pressure and kidney damage (Hansel et al., 2010). In the case of targeted cancer therapy, where mAbs target a specific antigen on cancer cells, the side effects likely arise due to the expression of the target antigen not only on cancer cells but also on normal cells, which therefore are targeted indiscriminately by mAbs administered in patients (Scott et al., 2012). Moreover, mAbs often suffer from shortcomings such as moderate therapeutic efficacy (resulting in the development of resistance) and their efficacy in a fraction of patients (as observed for mAbs against immune checkpoint inhibitors; Aldeghaither et al., 2019; Hansel et al., 2010; Wang et al., 2021). Insufficient blockade of target antigens for various reasons, including insufficient antigen-binding affinity, could be responsible for the moderate therapeutic efficacy.

In general, diagnostic and therapeutic antibodies are required to exhibit low nanomolar or higher antigen-binding affinity (KD <10 nM) (Sliwkowski and Mellman, 2013). To reach this level of affinity, laborious experiments for affinity maturation are usually followed after an initial discovery of an antibody (Hoogenboom, 2005). Increasing the valency of binding interaction could be a method of choice. It was shown that irreversibly dimerized monovalent binders can bind targets significantly better than monomeric counterparts (Foreman and Vilar, 2017). This enhancement of the binding affinity arises from the proximity effect, where the binding of one subunit of the dimer to a target restricts the search space for the other subunit. Reversibly dimerized binders could also exhibit significantly enhanced binding affinity depending on the affinity for binder-target interaction, affinity for homodimerization and the length of the connecting linker, as predicted by a reacted-site probability approach (Foreman and Vilar, 2017). Such approaches to increase the valency of binding have been applied to IgG antibodies, and a considerable increase in the antigen-binding affinity was observed in vitro (White et al., 2014). However, as the size of an IgG-type antibody is large (~150 kDa), irreversible cross-linking or tight reversible dimer formation of the antibody would result in poor solubility and tissue penetration in vivo.

Owing to the overall dimeric structure, IgG antibodies genetically fused to a homodimeric protein at the C-terminus can be catenated in an arm-in-arm fashion as long as the homodimer can be formed, not within an antibody molecule, but between two antibody molecules. In theory, it would be possible to generate a soluble fusion protein that remains monomeric in solution, but becomes catenated by the proximity effect on a cell surface where target antigen molecules are abundant, provided that the fused protein has appropriately low homodimerization affinity. Importantly, this proximity effect-driven catenation, in turn, should result in enhanced bivalent antigen-binding affinity (=avidity). In this work, by agent-based modeling (ABM) and proof-of-concept experiments, we demonstrate that antibody catenation induced by intermolecular homodimerization can enormously enhance the antigen-binding avidity of an antibody on a target surface.

## Results

### The concept of antibody catenation on a target surface

This concept was based on (i) the unique dimeric structure of the IgG-type antibody and (ii) a proximity effect that potentially takes place on a target cell surface. In the structure of IgG, the Fc domain is composed of two copies of the constant regions of the heavy chain (CH2 and CH3) forming a homodimer, in which the two C-termini are ~23 Å apart and point away from each other (Figure 1A, Left). This structural feature indicated that a homodimer-forming protein genetically fused to the C-terminus can be prevented from forming a homodimer intramolecularly by controlling the length of the connecting linker or its homodimerization affinity. Instead, the fusion protein can form a homodimer intermolecularly, and then such a homodimerization could result in a catenation of the antibody molecules (Figure 1A, Right). We designate the fusion protein between an antibody and a homodimeric protein as antibody-catenator (catAb). A proximity effect for catAb is expected on a target surface where multiple copies of target antigen are present, because the local concentration of catAb on the surface will increase owing to the antibody-antigen binding interaction. Consequently, the homodimerization between the catenator molecules will increase to form catenated antibodies in an arm-in-arm fashion (Figure 1B). Importantly, the effective antigen-binding affinity of catAb will increase in parallel with the catenation, and the fold enhancement would depend on the degree of the catenation. Thus, it appeared possible to enhance the antigen-binding avidity of the IgG-type antibodies by genetically fusing a weakly homodimer-forming protein.

![Figure 1.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig1-v1.jpg)

**Figure 1.:** (A) Molecular model for catenator-fused antibodies. A flexible linker (Gly-Gly-Ser) between Fc and the catenator and the hinge segment between Fc and Fab were modeled by using the ROSETTA software. The catenator is an α-helical hairpin that forms four-helix anti-parallel coiled coils (PDB entry: 1ROP). The structure of Fc was derived from the IgG1 antibody (PDB entry: 1IGY) and that of Fab from an antibody against the receptor-binding domain of the SARS-CoV-2 spike protein (PDB entry: 6XE1). (B) Decreased dissociation by antibody catenation. Pairs of catAb-antigen complexes adjacent to each other can be catenated, and the catAb molecules are increasingly harder to dissociate from each other with increased catenation. The effective antigen-binding avidity would increase owing to a decreased off rate of catAb.

### Agent-based modeling to simulate the behavior of catAb

ABM is a computational modeling approach that has been employed in a variety of research areas, including statistical physics (Perc et al., 2017; Fu and Wang, 2008) and biological sciences (An et al., 2009; Metzcar et al., 2019; McLane et al., 2011). ABM enables the understanding of macroscopic behaviors of a complex system by defining a minimal set of rules governing microscopic behaviors of agents which compose the system.

We constructed an ABM to simulate the behavior of the catAb molecules on a target surface, where target antigen (Ag) molecules form antibody-binding sites. To circumvent complexity, we presumed that each binding site is a pair of two antigen molecules (2Ag), and catAb make a bivalent interaction with the binding site in a 1:1 stoichiometry to form an occupied binding site (catAb-2Ag; Figure 2A, Left). For catenation to occur between two adjacent catAb-2Ag complexes, the distance between the centers of two adjacent complexes (d) should be closer than the reach length (L) defined as l+c/2, the sum of the linker length (l) and the half the catenator length (c) (Figure 2A, Right). Therefore, multiple parameters affect the catenation on the target surface. In our ABM model, we regarded every possible binding site on the target surface as an individual agent in the ABM formalism, and each binding site is assigned to a fixed position on a three-dimensional (3D) surface with a periodic boundary condition. Three rules in our ABM govern the behaviors of the catAb molecules on the target surface. The first rule is about the intrinsic antibody-antigen binding. An unoccupied binding site binds to one free catAb through bivalent interaction to form an occupied binding site. Bound catAb may dissociate from the occupied binding site, leaving the binding site unoccupied. The equilibrium population of the occupied and unoccupied binding sites is determined by the antibody’s intrinsic avidity for the antigen with no effect of the catenator on the antigen-binding avidity assumed. Then, the relative likelihood of the occupied state compared to the unoccupied state for any binding site (the likelihood of intrinsic antigen binding) is defined as [catAb-2Ag]/[2Ag] and thus can be expressed as [catAb]/KD, where [catAb] is the concentration of catAb and KD is the dissociation constant for the bivalent catAb-2Ag interaction (Figure 2B, Left). The second rule is about catenation. A pair of catAb-2Ag complexes on the target surface can be bridged by intermolecular homodimerization between catenators (Figure 2B, Middle). For a pair of catAb-2Ag complexes separated by d (Figure 2A, Right), the relative likelihood of the catenation state as compared to the non-catenation state is the ratio of the forward reaction rate (catenation) to the reverse reaction rate (decatenation). The forward reaction rate (Rcatenation) and the reverse reaction rate (Rdecatenation) are given as,

$$
R_{catenation}=(k_{f})_{catination } *\frac{1}{N_{A}}*\frac{1}{V_{sphere}}^{2}*V_{overlap}(d)   
$$



$$
R_{decatenation}=(k_{r})_{catenation} *\frac{1}{N_{A}}
$$

![Figure 2.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig2-v1.jpg)

**Figure 2.:** (A) (Left) Each binding site is composed of two antigen molecules (2Ag). (Right) The gray circles indicate the sphere sampled by the catenator, and Voverlap is the overlapping volume between the adjacent spheres. Catenation between two catAb molecules is possible only in Voverlap. (B) The three rules of the ABM model. (Left) catAb-2Ag binding occurs with a relative likelihood, [catAb]/KD. (Middle) The catenation between adjacent catAb-2Ag complexes occurs with an indicated relative likelihood, f(d)/(KD)Catenator, determined by (KD)Catenator and the inter-complex distance d. (Right) It was assumed that catAb molecules that are catenated do not dissociate from the surface. (C) The simulation requires specification of the parameters for the binding site, antibody and catenator. Through the MCMC sampling, the state of binding sites on the target surface is iteratively updated with the ABM rules and eventually sampled. A sufficient number of sampling results are collected to quantify the binding occupancy and the effective dissociation constant.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Definition of parameters and the equation of f(d). The forward catenation rate at which two catenators dimerize is proportional to the volumetric overlap (V(d)) between the effective concentration of the catenator, which is assumed to be uniformly distributed over a sphere defined by the reach length (L). V(d) depends on the distance (d) between the two adjacent catAb-2Ag complexes as well as the reach length. (B) Plot of f(d) as a function of d calculated for the indicated reach length (L).

, where kf and kr are the reaction rate constant of the forward and reverse reaction, respectively, $N_{A}$ is the Avogadro number, Vsphere is the local spherical volume within the reach of the catenator, and Voverlap(d) is the volume where two catenators can come in contact to form a homodimer (Figure 2A, Right). In approximating the forward reaction rate, the catenator was assumed to sample Vsphere uniformly. The relative likelihood, defined as Rcatenation/Rdecatenation, is then expressed as

$$
\frac{R_{catenation}}{R_{decatenation}}=\frac{(k_{f})_{catenator}}{(k_{r})_{catenator}}*\frac{1}{N_{A}}*\frac{1}{V_{sphere}}^{2}*V_{overlap}(d) =\frac{f(d)}{(K_{D})_{catenator}}
$$

where

$$
fd=\frac{1}{N_{A}}*\frac{1}{V_{sphere}}^{2}*V_{overlap}(d)
$$

The relative likelihood is thus a function of d, and it is inversely proportional to the dissociation constant of the catenator in the bulk medium, (KD)catenator. The function f(d) can be viewed as the effective local concentration of the catenator in Voverlap(d). As expected, f(d) and thus the relative likelihood is sensitively affected by the reach length and limited by the catAb-catAb distance (Figure 2—figure supplement 1). Finally, the third rule is about restricted dissociation which assumes that catenated antibodies are not allowed to dissociate from the binding site, because the catenated arms would hold the dissociated antibody near its binding site, forcing it to rebind immediately (Liese and Netz, 2018). Under this assumption, antibody molecules are allowed to dissociate from the binding site, only if its catenator is not engaged in the homodimerization with nearby catAb-2Ag complexes (Figure 2B, Right).

### Simulations show significant enhancement of the antigen-binding avidity

According to the postulated rules, we simulated the effects of the antibody catenation on the binding interaction between catAb and 2Ag on a three-dimensional surface by using the Markov Chain Monte-Carlo (MCMC) sampling method (Hooten and Wikle, 2010) (see Methods section). Our sampling procedure is composed of three steps (Figure 2C). The first step is an initialization, where a target surface with the antibody-binding sites is defined by specifying the coordinates for each site. A set of binding sites are positioned equidistant from each other or randomly positioned, and the inter-site distance or the number of binding sites were set as variables. The next step is an MCMC stochastic update step. In each iteration, a binding site is randomly selected from the target surface, and the probability of changing the status of the selected binding site (occupied or not) is calculated by the Metropolis-Hasting algorithm (Hastings, 1970; Grazzini et al., 2017). Then, the ‘on’ or ‘off’ state of this site is updated with the calculated probability. Accordingly, the catenation state is probabilistically updated for each update step. In the following sampling step, the total number of the occupied binding sites is counted, which is then collected through multiple simulation runs for the statistical analysis of the binding site occupancy and the effective antigen-binding avidity. The binding site occupancy is the mean value of the number of occupied binding sites collected for more than 1024 MCMC samplings. For each simulation, we calculated the mean binding occupancy and the effective dissociation constant, (KD)eff, which takes into account the effect of the antibody catenation, and is expressed as:

$$
(K_{D})_{eff}=\frac{(1-Binding Site Occupancy)*[^{cat}Ab]}{Binding Site Occupancy}
$$

Since the catenator homodimerization should be affected by how the binding sites are distributed on a 3D surface, simulations were conducted for different arrays of binding sites. In the simulations, (KD)catenator was the main variable, while other parameters were set constant. First, we simulated the binding sites forming a square lattice to find that the Ab-catenator exhibited enhanced binding site occupancy in a sigmodal manner, and that it could be enhanced to near full saturation by a catenator that forms a homodimer with quite low binding affinity. For instance, a catAb with (KD)catenator of ~1 μM exhibited ~70-fold enhancement of the effective antigen-binding avidity (=reduction of (KD)eff) in comparison with the same antibody without a fused catenator (Figure 3). As a means of comparison across different simulation setups, we employed ‘(KD)catenator,50’ which is defined as the (KD)catenator that enables half-maximal enhancement of the binding site occupancy (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig3-v1.jpg)

**Figure 3.:** (Left) Binding site occupancy. The simulations were carried out for a square array of the binding sites. The values for a set of variables were KD = 10–8 M, [catAb]=10–9 M, reach length = 7 nm, spacing between the binding sites = 12 nm and the number of total binding sites = 98. The mean value and standard deviations of 1024 MCMC simulations for each (KD)catenator value are shown in blue, and the data are shown as a scatter plot of representative runs (orange). (Right) The effective dissociation constant. The data shown on the left were converted into the (KD)eff values. The dashed line represents the KD value for the same antibody without a catenator. The maximum fold enhancement of the effective binding avidity, which is equivalent to the reduction of (KD)eff, is 70.6.

### Comparison of the simulations for different arrays of the binding sites

Next, we carried out simulations for other regular arrays of the binding sites and for randomly distributed binding sites. Depending on the pattern of regularly distributed binding sites, the number of possible catenations for a given binding site (designated as connectivity number) varies: 3, 4 and 6 for a hexagonal, square or triangular array of the binding sites, respectively (Figure 4A). These three arrays showed varying but similar enhancement of the binding site occupancy and the effective antigen-binding avidity by the catenator (Figure 4A). As expected, the higher the connectivity number was, the lower (KD)catenator,50 an array exhibited; the (KD)catenator,50 was 8.0, 9.2 and 12.2 µM for the hexagonal, square and triangular array of the binding sites, respectively. The simulations showed that, as the connectivity number increased, the effective antigen-binding avidity increased with the maximum 41-, 73-, and 93-fold enhancement for the triangular, square and hexagonal array, respectively (Figure 4A). Thus, regardless of the distribution patterns, the effective antigen-binding avidity could be increased by at least 41 folds under the simulation conditions where the target surface contains only 98 binding sites.

![Figure 4.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig4-v1.jpg)

**Figure 4.:** (A) Comparison for regularly distributed binding sites. Three different regular arrays of the binding sites are shown at the top. The black dots represent the binding sites and the gray lines the connectable pairs by the catenators. The red circles and the blue lines represent the maximum range of catenation and the connectivity number, respectively, for a given binding site. Binding site occupancy and (KD)eff in response to (KD)catenator are shown at the bottom. 1024 trials were sampled for each (KD)catenator value and the results are plotted. The variables were KD = 10–8 M, [catAb]=10–9 M, reach length = 7 nm, spacing between the binding sites = 12 nm, and the number of total binding sites were 98 for the square array and 102 for hexagonal and triangular array, respectively. The numbers on the right are the maximum fold enhancement of the effective binding avidity for each array. (B) Comparison for randomly distributed binding sites. Three random arrays of the binding sites with different binding site densities (ρ) are shown at the top. The surface area for the simulation was 5760 nm2. The simulation conditions were the same as in (A). Binding site occupancy and (KD)eff in response to (KD)catenator are plotted as in (A).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** 1024 trials were sampled for each (KD)catenator value at the indicated density and the results are plotted. The variables were KD = 10–8 M, [catAb]=10–9 M, reach length = 7 nm, spacing between the binding sites = 12 nm, and the surface area = 5760 nm2. The maximum fold enhancement of the effective binding avidity and (KD)catenator,50 are tabulated at the bottom.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) The binding occupancy and (B) the effective dissociation constant (KD)eff in response to [catAb]/KD for [catAb]/KD = 1.0, 0.3, 0.1, 0.03, 0.01, where [catAb] was fixed to 10–9 M and KD was varied from 10–8 to 10–6. The simulations were carried out with a square array of the binding sites as in Figure 3. The set values for the variable parameters were reach length = 7 nm, spacing between the binding sites = 12 nm and the number of total binding sites = 98. The mean binding occupancy of 1024 MCMC simulations was plotted. (KD)catenator was varied from 1 mM to 10 nM. The antibody binding avidity is substantially enhanced across a broad range of [catAb]/KD.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (A) The binding occupancy and (B) the effective dissociation constant (KD)eff in response to [catAb] for (KD)catenator = 1, 10, 100 μM. KD was set to 10 nM, and [catAb] was varied from 0.1 to 10 nM. The simulations were carried out essentially the same as for Figure 2.

For the case of randomly distributed binding sites on a 3D surface, which is relevant to target antigen distribution on cell surfaces, we introduced the binding site density (ρ), the number of binding sites per unit area which is set to the square of the reach length (7 nm; Figure 4B). In the simulations, the total surface area was 5760 nm2, and the number of binding sites was 15, 30, 45, 90, or 120, which correspond to the ρ of 1.47, 2.94, 4.41, 8.82, or 11.76. Denser binding sites would increase the connectivity number for a given binding site. As expected, simulations showed that higher binding site density resulted in a higher level of binding site saturation and a much more significant increase in the effective antigen-binding avidity; the maximum fold enhancement ranged from 15 (ρ=1.47)–1062 (ρ=11.76). Likewise, significantly different (KD)catenator,50 values were observed: for example, 4.2x10–6 M at the ρ of 11.76 vs 74x10–6 M at the ρ of 1.47 (Figure 4B). The maximal saturation and the onset (KD)catenator, which begins to exert the catenation effect, were also considerably different. Thus, the catenation effects are sensitively affected by the binding site density, in contrast with the all-or-none catenation effect observed for the regular arrays of the binding sites (Figure 4B). In particular, the catenation-induced enhancement of the antigen-binding avidity was remarkably and sensitively affected by the (KD)catenator values at high binding site density (ρ>4.41; Figure 4B). Much greater enhancement was observed as we further increased the density of randomly distributed binding sites:~29,000 maximum fold enhancement at the ρ of 58.8 (Figure 4—figure supplement 1), which roughly corresponds to two-hundredths of the density of the HER2 receptor on HER2-overexpressing breast cancer cells (Peckys et al., 2019). Together, our simulations show that randomly distributed binding sites at high density enormously enhance the effective antigen-binding avidity of catAb.

Additionally, we performed simulations for different values of [catAb]/KD to estimate the effect of KD with respect to [catAb]. Varying [catAb]/KD from 0.01 to 1.0 (by varying KD from 10–8 to 10–6) resulted in 85- to 900-fold enhancement of the antigen-binding avidity, suggesting that the catenation effect works for a broad range of KD values (Figure 4—figure supplement 2). We also performed simulations to estimate the effect of [catAb]. Varying [catAb] from 0.1 to 10 nM resulted in far less than a 100-fold increase of (KD)eff, showing that the enhancement of (KD)eff by increasing the concentration of catAb is much less dramatic than that by increasing the affinity for catenator homodimerization (Figure 4—figure supplement 3).

### Proof-of-concept experiments

For experimental validation, we chose stromal cell-derived factor 1α (SDF-1α) as a catenator. SDF-1α is a small (Mr = 8 kDa) and weakly homodimerizing protein (KD = 150 µM; Veldkamp et al., 2005). Initially, by using a 10-residue connecting linker, (G4S)2, SDF-1α was fused to the homodimeric heavy chain (H chain) of two different antibodies: Trastuzumab(N30A/H91A), a variant of the clinically used anti-HER2 antibody Trastuzumab and a germline-encoded glCV30, an antibody against the receptor-binding domain (RBD) of the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) spike protein. The Fab fragment of Trastuzumab(N30A/H91A) binds to the ectodomain of HER2 with a KD of 353 nM (Slaga et al., 2018), and glCV30 binds to the RBD with a similar binding affinity (not avidity, KD = 407 nM; Hurlburt et al., 2020). Both antibody-catenator constructs exhibited drastic enhancements of the (KD)eff for the target proteins immobilized on the biosensor surface. However, as described below in the ‘incidental observations’ section, we now believe that these constructs likely formed reversible heterogeneous oligomers in solution, and the resulting data would not be a correct reflection of the effect of antibody catenation.

It was possible to obviate the oligomerization problem by dually fusing a pair of two different catenators, SDF-1α and SAM, to the knobs-into-holes heterodimeric Fc (HetFc) (Leaver-Fay et al., 2016), via a (G4S)2 linker. The sterile alpha motif (SAM) domain of SLy1 is also a small (Mr = 7.4 kDa) and weakly homodimerizing protein (KD=117 μM; Kukuk et al., 2019). Fusion of the homodimeric proteins to HetFc would also result in the antibody catenation on a target surface in a fashion shown in Figure 5A, while their catenation efficiency would be reduced compared with a corresponding homodimeric antibody-catenator construct. Employing a HetFc is instrumental to generate a control antibody, which has a single catenator. This construct can at best form a dimer, but cannot be catenated (Figure 5A; Right).

![Figure 5.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig5-v1.jpg)

**Figure 5.:** (A) By employing a heterodimeric Fc (HetFc), an antibody fused to two different catenators (Left) or an antibody with one catenator arm (Right) can be generated. Only the former could form catenated antibodies on a surface where target antigens are abundant. (B) Elution profile and BLI analyses of Trastuzumab(N30A/H91A) and SAM-Trz(2 m)/HetFc-SDF-1α. Trz(2 m)/Het stands for Trastuzumab(N30A/H91A) with its homodimeric Fc replaced by a HetFc. The two heavy chains were fused to SAM or SDF-1α. The two antibodies were eluted from a size-exclusion column as if they were monomeric (Left). Elution positions of the size marker proteins are indicated by triangles. BLI runs for the two antibodies are shown (Right). The ectodomain of HER2 was immobilized on the biosensor tip. (C) Elution profile and BLI analyses of glCV30 and SAM-glCV30/HetFc-SDF-1α. The two antibodies were analyzed as described in (B). Commonly for all BLI runs, the experimental signals and fitted curves are shown in red and black, respectively. For curve fitting, 1:1 binding was assumed. The kinetic parameters are shown in the insets. ka, association rate constant; kd, dissociation rate constant. The experiments were performed in triplicates, and representative sensorgrams are shown.

By replacing the original heavy chain with two heavy chains containing the ‘knobs’ or ‘holes’ mutations fused to SAM or SDF-1α, we first generated SAM-Trastuzumab(N30A/H91A)/HetFc-SDF-1α (in short, SAM-Trz(2 m)/HetFc-SDF-1α) and SAM-glCV30/HetFc-SDF-1α (Figure 5B and C). While the heterodimer formation was not 100%, it was possible to purify the heterodimeric antibodies homogenously that exhibited a single elution peak from a size-exclusion column that corresponds to the size of the heterodimer (Figure 5B and C). Trastuzumab(N30A/H91A) and SAM-Trz(2 m)/HetFc-SDF-1α exhibited similar association kinetics in bio-layer interferometry (BLI) experiments: the association rate constants (kas) of the two antibodies were 1.9x105 Ms–1 and 2.9x105 Ms–1, respectively. In contrast, the dissociation rate constants (kds) of the two antibodies were significantly different: 2.2x10–4 Ms–1 versus <1.0 × 10–7 Ms–1. As a result, SAM-Trz(2 m)/HetFc-SDF-1α exhibited the KD less than 0.01 nM (the limit of the instrumental sensitivity), at least 110-fold higher binding avidity compared with that of Trastuzumab(N30A/H91A) (KD of 1.1 nM; Figure 5B). These observed kinetics are consistent with the expectation that fused catenators would not affect the association of the antibodies, but would slow down the dissociation of the antibodies into the bulk solution via catenation of the antibody molecules on the sensor tip. The glCV30 and SAM-glCV30/HetFc-SDF-1α pair also exhibited similar association and dissociation kinetics, and the catenator fusion increased the binding avidity by at least 130 folds (Figure 5C).

To prevent the avidity enhancement beyond the instrumental sensitivity limit, we constructed triply mutated Trastuzumab(N30A/H91A/Y100A)/HetFc, which exhibited reduced binding avidity (KD of 243 nM for HER2) (Figure 6A; Bottom Left). The two catenator arms were fused to this antibody, and mScarlet to the light chain (for later cell-based experiments) to generate SAM-Trastuzumab(N30A/H91A/Y100A)/HetFc-SDF-1α (L-mScarlet) (in short, SAM-Trz(3 m)/HetFc-SDF-1α (L-mScarlet)). For a control experiment, SAM-Trastuzumab(N30A/H91A/Y100A)/HetFc (L-mScarlet) was generated that contains a single catenator arm. The two antibody-catenator constructs behaved as if they were monomeric in solution (Figure 6A, Top). BLI analyses showed that Trastuzumab(N30A/H91A/Y100A) and SAM-Trz(3 m)/HetFc-SDF-1α (L-mScarlet) exhibited similar association kinetics, but significantly different dissociation kinetics. As a result, SAM-Trz(3 m)/HetFc-SDF-1α (L-mScarlet) exhibited the KD of 0.8 nM, 304-fold higher binding avidity compared with that of Trastuzumab(N30A/H91A/Y100A) (Figure 6A, Bottom Middle). In support of the view that the observed avidity enhancement arises from the catenation of antibody molecules, SAM-Trz(3 m)/HetFc (L-mScarlet), which has one catenator arm and thus cannot catenate the antibody molecules (Figure 5A), exhibited high dissociation kinetics and the KD of 373 nM, which are close to those of the mother antibody (Figure 6A, Bottom Right).

![Figure 6.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig6-v1.jpg)

**Figure 6.:** (A) The triply mutated Trastuzumab(N30A/H91A/Y100A), the antibody with two catenator arms (SAM-Trz(3 m)/HetFc-SDF-1α) and the same antibody with one catenator arm (SAM-Trz(3 m)/HetFc) were prepared with their light chain (L) fused to mScarlet at the C-terminus. The two antibody-catenators were eluted from a size-exclusion column as if they were monomeric (Left). The SDS-PAGE of the peak fractions shows the correct sizes of the indicated chains (Right). BLI was performed similarly as described in Figure 5B. The two catenator-armed antibody exhibits a significant increase in the binding avidity, but the one catenator-armed antibody did not (KD values in the inset). (B) Obnutuzumab(Y101L) and SAM-Obz(Y101L)/HetFc-SDF-1α were prepared, and BLI was performed with biotinylated human CD20 immobilized on the biosensor tip (Top). Flow cytometric analyses of SU-DHL5-binding by the two antibodies were performed (Bottom). For this experiment, the two antibodies were labeled with muGFP at the C-terminus of the light chain. The fluorescent signal from muGFP was detected by using a 525/40 bandpass filter.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Elution profile and SDS-PAGE analysis of SAM-Obz(Y101L)/HetFc-SDF-1α.

Another antibody with intentionally reduced binding avidity was constructed: Obinutuzumab(Y101L), a mutant version of the clinically used anti-CD20 antibody (Evans and Clemmons, 2015). In our measurement, Obinutuzumab(Y101L) exhibited the KD of 30.4 nM for CD20 (Figure 6B). Also generated was SAM-Obinutuzumab(Y101L)/HetFc-SDF-1α (in short, SAM-Obz(Y101L)/HetFc-SDF-1α), which was monomeric in solution (Figure 6—figure supplement 1). This antibody/antibody-catenator pair also exhibited similar association kinetics, but significantly different dissociation kinetics: kas were 3.3x105 Ms–1 vs 1.8 x105 Ms–1, and kds were 1.0x10–2 Ms–1 vs 2.3 x10–5 Ms–1 (Figure 6B, Top). As a result, SAM-Obz(Y101L)/HetFc-SDF-1α increased the binding avidity by 234 folds in comparison with the mother antibody. We asked whether the enhanced binding avidity observed for SAM-Obz(Y101L)/HetFc-SDF-1α could be reproduced in binding to SU-DHL5, a cell line derived from diffuse large B-cell lymphoma that overexpresses CD20. Flow cytometric analysis showed that SAM-Obz(Y101L)/HetFc-SDF-1α bound to the SU-DHL5 cell much more effectively than Obinutuzumab(Y101L) (Figure 6B, Bottom). This result indicates that the SAM-Obz(Y101L)/HetFc-SDF-1α molecules were likely catenated on the surface of the SU-DHL5 cell. Together, these data demonstrate that noncovalent antibody catenation on a target surface is a way to greatly enhance antigen-binding avidity.

### Incidental observations

The homodimeric glCV30-SDF-1α construct showed three eluted fractions from a size-exclusion column: a void, a broad peak, and a narrow peak fraction (Figure 7A). The narrow peak fraction was a mixture of the L chain and H chain missing the catenator as a result of partial proteolytic cleavage. In contrast, the broad peak did not contain the cleaved H chain. The broad peak fraction was highly soluble, as it could be concentrated at least to 200 μM. Assuming that the broad peak fraction was in a dynamic equilibrium between monomeric and oligomeric species in solution as a result of the weak intermolecular interaction of SDF-1α, we used it to assess their ability to enhance the binding avidity for the target antigens. glCV30-SDF-1α also exhibited association-dissociation kinetics similar to those of the dual catenator-fused antibodies: a similar ka but very low kd in comparison with those of the mother antibody (Figure 7). glCV30-SDF-1α exhibited virtually no dissociation and enhanced the binding avidity by at least 5120 folds (Figure 7B).

![Figure 7.](https://cdn.elifesciences.org/articles/81646/elife-81646-fig7-v1.jpg)

**Figure 7.:** (A) Elution profile and SDS-PAGE analysis of glCV30-SDF-1α. (B) The BLI runs shown on the left of Figure 5C are reused here for easy comparison with those for glCV30-SDF-1α. The KD values could not be accurately determined due to instrumental insensitivity (KD <10 pM). The affinity-matured version, CV30, was analyzed and its BLI sensorgrams are shown on the right. (C) Neutralization of VSV virus pseudotyped with the SARS-CoV-2 spike protein. Each of the three antibodies was serially diluted and added to the rVSV-ΔG-Luc bearing the SARS-CoV-2 Spike protein of the Wuhan-Hu-1 strain. The mixture was incubated with HEK293T-hACE2 cells and the luciferase activity was measured. The geometric mean titer (GMT) values with a 95% confidence interval are shown on the right, which corresponds to the IC50 values of 0.25, 3.22 and 0.21 μg/ml of CV30, glCV30 and glCV30-SDF-1α, respectively.

Consistently, the glCV30-SDF-1α construct exhibited notable activity in a virus neutralization assay using vesicular stomatitis virus (VSV) pseudotyped with the SARS-CoV-2 Spike protein. This virus is expected to harbor multiple copies of the Spike protein on its envelope. In comparison with glCV30, glCV30-SDF-1α exhibited a~15 fold lower inhibition constant 50 (IC50) value. This neutralization potency of glCV30-SDF-1α (IC50 of 0.21 μg/ml) is comparable to that (IC50 of 0.25 μg/ml) of CV30, which is an affinity-matured version of glCV30 (Figure 5C). CV30 bound to the RBD domain with the KD of less than 10 pM in our measurement by BLI, similarly as glCV30-SDF-1α did (Figure 7C).

We believe that the avidity enhancement and the strong neutralization activity of glCV30-SDF-1α reflect not only the catenation effect but also reversible oligomerization in solution, which further increases the binding avidity. Likely, some fraction of SDF-1α underwent a structural change at the low pH step in the protein purification, leading to reversible heterogeneous oligomerization. Although it is yet unclear why the reversible oligomerization, if this is the case, didn’t enhance the association rate constant, these incidental observations suggest a possible approach for producing noncovalent IgG antibody multimers that could enhance the sensitivity of diagnostic antibodies.

## Discussion

In the current phage display for antibody screening, many candidates that do not satisfy a required affinity for a target antigen are rejected, although they might have high specificity of binding. A simple and general way of increasing the antigen-binding affinity of antibodies would be highly valuable for various applications of antibodies. Taking advantage of the particular homodimeric structure of IgG antibodies, we put forth a concept to enhance the bivalent antigen-binding interaction by fusing a weakly homodimerizing protein to the C-terminus of Fc. The validity of the concept was tested by simulations based on an ABM and supported by experimental demonstrations.

Our ABM with the three postulated rules was the basis for predicting the enhancement of effective antigen-binding avidity. The model has caveats. First, the assumption of uniform density for the fused catenators within a sphere oversimplifies the dynamics of the catenators, which would highly depend on physical contexts, such as molecular orientations and potential intramolecular interaction with the antibody (Zhou, 2001). Second, the binding sites representing antigens are fixed on a surface in our model, but in real situations, antigens move their positions, e.g., receptor molecules on cellular membranes (Saxton and Jacobson, 1997). Advanced molecular dynamics simulations incorporated into the ABM would take account of these microscopic details to result in a more accurate prediction of the behaviors of the catAb molecules and the binding sites. Despite these caveats, the simulations provided valuable insights into the proper ranges of the antigen-binding avidity of an antibody and catenator-catenator binding affinity. According to the simulation, we adopted SDF-1α and SAM, as catenators, both of which are weakly homodimerizing proteins (KD of 100–150 μM). When fused to antibodies, they resulted in great enhancement of the effective antigen-binding avidity of the antibodies, which was due to drastically reduced rate of dissociation of the fused antibody molecules from the immobilized antigens.

The ‘antibody catenation on a target surface’ method presented herein might find practical applications. First, it can be applied to therapeutic antibodies against viruses, which have multiple copies of target antigens on their surface. Second, it can be used for sandwich-type point-of-care biosensors in which a second antibody is catenated to increase the sensitivity of detection. Third, this method can be used to sense biomarkers that exist in a very low number on a target cell (e.g. copy number <10), which requires an extremely high-binding avidity of a probe antibody. For this application, employing an antibody with high antigen-binding affinity (e.g. KD <1 nM) and a catenator with high homodimerization affinity (e.g. (KD)catenator <1 μM), would be necessary to overcome the low proximity effect due to the scarcely present antigen molecules. Fourth, it might also be applied to antibody-based targeted cancer therapy where side effects arising from antibody binding to normal cells are a general problem. Since cancer-associated antigen molecules are lower in number on normal cells than they are on cancer cells, catenated anticancer antibodies would be concentrated on the surface of cancer cells, because the effective binding avidity of a catAb depends on the number of antigen molecules on a target surface. In particular, this approach would greatly reduce the intrinsic toxicity of antibody-drug conjugates that are widely used currently. Of note, a catenator fused to the C-terminus of Fc would not affect the effector function Fc through the Fcγ receptor-binding site and FcRn binding site on it.

While we demonstrated that dual catenator-fused heterodimeric IgGs can enhance binding avidity, a higher (or at least the same) catenation effect should be observed for the conventional homodimeric IgGs. To prevent the oligomer formation of the homodimeric IgGs or potential intramolecular homodimerization of the catenator, a more robust catenator has to be employed. Specifically, the ideal catenator should geometrically disallow intramolecular homodimerization, exhibit fast association kinetics, and be able to withstand the standard low pH purification step. On the other hand, our demonstration indicates that this approach can be applied to bispecific antibodies employing a heterodimeric Fc.

## Materials and methods

### MCMC simulation

Simulation runs were carried out in the three steps stated below with specification of the target surface, KD (for antibody-antigen interaction), (KD)catenator (for catenator-catenator interaction) and $f(d)$ (effective local concentration of the catenator). In all simulations, the number of catAb was far more than that of the binding sites, and therefore, the concentration of free catAb was assumed to be the same as that of total catAb (free catAb +antigen-bound catAb). Simulation parameters their set values are listed in Table 1.

**Table 1.**
 Simulation specifications.The definition and values of the parameters used in the presented simulations are tabulated.


<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Description</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">Specification of catAb</td>
    </tr>
    <tr>
      <td>KD</td>
      <td>Dissociation constant of antibody</td>
      <td>10 nM</td>
    </tr>
    <tr>
      <td>(KD)catenator</td>
      <td>Dissociation constant of catenator</td>
      <td>10 nM-10 mM</td>
    </tr>
    <tr>
      <td>[catAb]</td>
      <td>Antibody concentration</td>
      <td>1 nM</td>
    </tr>
    <tr>
      <td>l</td>
      <td>Length of the flexible linker</td>
      <td>6 nm</td>
    </tr>
    <tr>
      <td>c</td>
      <td>Length of the catenator</td>
      <td>2 nm</td>
    </tr>
    <tr>
      <td>L</td>
      <td>Reach length (l+c/2)</td>
      <td>7 nm</td>
    </tr>
    <tr>
      <td colspan="3">Specification of the target surface</td>
    </tr>
    <tr>
      <td>Ntotal_binding_sites(in Figures 3 and 4)</td>
      <td>Number of antibody-binding sites</td>
      <td>98–102</td>
    </tr>
    <tr>
      <td>Connectivity number(in Figures 3 and 4)</td>
      <td>Number of possible catenation</td>
      <td>3 (Hexagonal)4 (Square)6 (Triangular)</td>
    </tr>
    <tr>
      <td>d (in Figures 3 and 4)</td>
      <td>Distance between adjacent binding sites</td>
      <td>12 nm</td>
    </tr>
    <tr>
      <td>Lsurface (in Figure 4)</td>
      <td>Surface area of the target surface</td>
      <td>40 nm2</td>
    </tr>
    <tr>
      <td>Binding site density(in Figure 4)</td>
      <td>Surface density of the binding sites</td>
      <td>1.47–11.76(per 7x7 nm2)</td>
    </tr>
    <tr>
      <td colspan="3">Specification of simulation</td>
    </tr>
    <tr>
      <td>Updates/MCMC step</td>
      <td>Number of updates in one MCMC step</td>
      <td>30,000–100,000</td>
    </tr>
    <tr>
      <td>Sampling size</td>
      <td>Number of sampling for a parameter set</td>
      <td>1024</td>
    </tr>
  </tbody>
</table>

#### Step 1. Initialization step

#### Step 2. MCMC stochastic update step

The following sub-steps (1-3) are iterated sufficient times to ensure thermodynamic equilibration.

#### Step 3. Sampling step

The codes for the model system and simulations are available in MATLAB and available on Github (copy archived at Song, 2020). A detailed description is provided in Readme.

### Preparation of antibodies and catenator-fused antibodies

For preparing SAM-Trz(2 m)/HetFc-SDF-1α, DNA fragments encoding the two heavy chains containing the knobs mutations or the holes mutations (Leaver-Fay et al., 2016) were synthesized (IDT) and cloned into the pCEP4 vector (Invitrogen). The final cloned vectors were to express the knob H chain fused to SAM-(His)6, and the hole H chain fused to SDF-1α-MBP. The two vectors were amplified using the NucleoBond Xtra Midi kit (Macherey-Nagel) and introduced into the CHO-S cells (Gibco) together with the light chain-encoding vector. The transfected cells were grown in the ExpiCHO expression medium (Gibco) for seven days post-transfection. Cell cultured media were collected by centrifugation at 4 °C, filtered through 0.45 µm filters (Millipore), and loaded onto Ni-NTA resin (Thermo Scientific) and subsequently onto amylose resin (NEB). The MBP tag was cleaved by TEV protease. The MBP was intentionally used to remove homodimeric fraction. The antibody was further purified using a HiLoad 26/60 Superdex 200 gel-filtration column (Cytiva) equilibrated with a buffer solution containing 20 mM Tris-HCl (pH 7.5) and 150 mM NaCl. SAM-Trz(3 m)/HetFc-SDF-1α, SAM-Obinutuzumab(Y101L)/HetFc-SDF-1α and SAM-glCV30/HetFc-SDF-1α were prepared similarly.

For preparing the homodimeric glCV30-SDF-1α, each DNA fragment encoding heavy chain variable regions (VH) and light chain variable regions (VL) of glCV30 were synthesized (IDT) and cloned into the pCEP4 vector. DNA fragments of CH1-CH2-CH3 of the gamma heavy chain and CL of the kappa-type light chain were inserted into the pCEP4 vector encodingVH or VL, and the resulting vectors were named glCV30 Hc and glCV30 Lc, respectively. DNA fragment encoding SDF-1α was synthesized (IDT) and cloned into the glCV30 Hc next to CH3 of glCV30 with (G4S)2 linker sequence (glCV30-SDF-1α Hc). The glCV30-SDF-1α Hc and glCV30 Lc vectors were introduced into the CHO-S cells (Gibco). The transfected cells were grown in the ExpiCHO expression medium (Gibco) for ten days post-transfection. The culture supernatant was diluted by the addition of a binding buffer (150 mM NaCl, 20  mM Na2HPO4, pH 7.0) to a 1:1 ratio, loaded onto an open column containing Protein A resin (Sino Biological), and eluted with an elution buffer (0.1 M glycine, pH 3.5). The eluent was immediately neutralized by a neutralizing buffer (1 M Tris-HCl, pH 8.5), and the antibodies were further purified using a HiLoad 26/60 Superdex 200 gel-filtration column. The cloning, protein production, and purification procedures for mother antibodies were virtually identical to those used for glCV30-SDF-1α.

### Bio-layer interferometry

BLI experiments were performed to measure dissociation constants using an Octet R8 (Sartorius). Biotinylated SARS-CoV-2 RBD (Acrobio system) or biotinylated Her2/ERBB2 (Sino Biological) was loaded to a streptavidin biosensor tip (Sartorius) for 120s or 180s. A baseline was determined by incubating the sensor with Kinetics Buffer (Sartorius) for 60s. Antibody samples at different concentrations went through the association phase for 240s or 480s, and the dissociation phase for 720s or 1080s. All reactions were carried out in the Kinetics Buffer (Satorius). The binding kinetics were analyzed using the Octet DataAnalysis 10.0 software (Sartorius) to deduce the kinetic parameters. Experiments were performed in triplicate for glCV30 and glCV30-SDF-1α and duplicate for Trastuzumab(N30A/H91A) and Trastuzumab(N30A/H91A)-SDF-1α.

### Cell-binding assay

Flow cytometry experiments were performed to compare the binding efficiencies of Obinutuzumab(Y101L) and SAM-Obz(Y101L)/HetFc-SDF-1α. The SU-DHL5 cell line (DSMZ) was used for the experiments. Cells were cultured in RPMI media (Sigma-Aldrich) containing 10% fetal bovine serum at 37 °C and under 5% CO2. The cells were subcultured every 2–3 days to maintain >95% cell viability. After centrifugation, the cell pellet was resuspended in the PBS buffer containing 1% BSA (PBSF), and more than 2x105 cells per well were plated in 96-well round bottom plates containing 200 μL media. The cells were treated with the antibody samples at room temperature for 1 h, and washed three times using PBSF and resuspended in 200 μL of PBSF. Each well was analyzed using Cytoflex_Plate Loader (Beckman Coulter). The sample flow rate was 30 μL/min, and 15,000 cells were counted per well.

### Pseudovirus neutralization assay

To prepare of VSV pseudotyped with the SARS-CoV-2 Spike protein of the Wuhan-Hu-1 strain, HEK293T cells (ATCC) plated overnight previously at 3x106 cells in a 10 cm dish were transfected using calcium phosphate with 15 μg plasmid encoding the spike protein of SARS-CoV-2 with 18-residue deletion at the cytoplasmic tail. At 24 hr post-transfection, cells expressing the Spike protein were infected for 1 hr with recombinant VSV, in which G gene was replaced with a luciferase gene (rVSV-ΔG-Luc). The cells were washed three times with Dulbecco’s phosphate-buffered saline, and 7–10 mL of the same media with 10% FBS was added. At 24–48 hr post-infection, the culture media were harvested, filtered with a 0.45 μm filter, and then stored at –80 °C for neutralization assay. For the pseudovirus neutralization assay, serially diluted CV30, glCV30 and glCV30-SDF-1α antibodies were mixed with the pseudovirus solution for 1 hr, and the mixture was added to HEK293T cells expressing human ACE2 (HEK293T-hACE2; 3x104 cells per well in 96-well plate), which were previously seeded overnight. Cells were lysed with Passive Lysis Buffer (Promega, E1941) At 24 hr post-transfection, LAR II (Promega, E1501) was added to the lysate, and the luciferase activity was measured. The percent neutralization was normalized to uninfected cells (100% neutralization) and infected cells (0% neutralization), both in the absence of antibody. The IC50 titers were determined with the nonlinear curves of the log(antibody) versus normalized response using Prism v9 (GraphPad).

### Cell lines

The CHO-S (Gibco), SU-DHL5 (DMSZ), and HEK-293T (ATCC) cell lines were negative for mycoplasma. Additionally, the identity of the SU-DHL5 and HEK-293T cell lines was confirmed by Short Tandem Repeat profiling.

### Figure preparation

The computational models of an antibody and an antibody-catenator in Figure 1A were generated by using the ROSETTA software (Leman et al., 2020), and are presented by PyMOL (Delano, 2004).

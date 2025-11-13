# Allosteric modulation of the adenosine A2A receptor by cholesterol

## Authors

- Shuya Kate Huang<sup>1</sup> ([ORCID: 0000-0003-0637-4313](https://orcid.org/0000-0003-0637-4313))
- Omar Almurad<sup>1</sup>
- Reizel J Pejana<sup>1</sup>
- Zachary A Morrison<sup>1</sup>
- Aditya Pandey<sup>1</sup>
- Louis-Philippe Picard<sup>1</sup>
- Mark Nitz<sup>1</sup>
- Adnan Sljoka<sup>3</sup> ([ORCID: 0000-0002-2398-9523](https://orcid.org/0000-0002-2398-9523))
- R Scott Prosser<sup>1</sup> ([ORCID: 0000-0001-9351-178X](https://orcid.org/0000-0001-9351-178X)) †

### Affiliations

1. Department of Chemistry, University of Toronto Toronto Canada
2. Department of Chemical and Physical Sciences, University of Toronto Mississauga Mississauga Canada
3. RIKEN Center for Advanced Intelligence Project Tokyo Japan
4. York University, Department of Chemistry Toronto Canada
5. Department of Biochemistry, University of Toronto Toronto Canada

† Corresponding author

## Abstract

Cholesterol is a major component of the cell membrane and commonly regulates membrane protein function. Here, we investigate how cholesterol modulates the conformational equilibria and signaling of the adenosine A2A receptor (A2AR) in reconstituted phospholipid nanodiscs. This model system conveniently excludes possible effects arising from cholesterol-induced phase separation or receptor oligomerization and focuses on the question of allostery. GTP hydrolysis assays show that cholesterol weakly enhances the basal signaling of A2AR while decreasing the agonist EC50. Fluorine nuclear magnetic resonance (19F NMR) spectroscopy shows that this enhancement arises from an increase in the receptor’s active state population and a G-protein-bound precoupled state. 19F NMR of fluorinated cholesterol analogs reveals transient interactions with A2AR, indicating a lack of high-affinity binding or direct allosteric modulation. The combined results suggest that the observed allosteric effects are largely indirect and originate from cholesterol-mediated changes in membrane properties, as shown by membrane fluidity measurements and high-pressure NMR.

## Introduction

In mammalian cell membranes, cholesterol accounts for ~5–45% of the total lipid content across different cell types and subcellular components (Casares et al., 2019; Ingólfsson et al., 2017). It is a critical metabolic precursor to steroid hormones, bile salts, and vitamin D, while numerous cardiovascular and nervous system disorders are attributed to abnormalities in cholesterol metabolism (Arsenault et al., 2009; Martín et al., 2014). The rigid planar structure of cholesterol promotes ordering of bilayer lipids, thus modulating membrane fluidity and thickness. Cholesterol also drives the formation of raft-like microdomains and commonly interacts with membrane proteins as a ligand or allosteric modulator (Hulce et al., 2013).

Here, we investigate how cholesterol influences the conformational equilibria and signaling of a well-studied integral membrane protein, the adenosine A2A receptor (A2AR), in reconstituted phospholipid/cholesterol nanodiscs. Specifically, we seek to understand if the effects on A2AR function are a consequence of direct allosteric interplay between cholesterol and the receptor, or if the observed effects result primarily from cholesterol-driven changes in viscoelastic properties and thickness of the lipid bilayer.

A2AR is a member of the rhodopsin family of G-protein-coupled receptors (GPCRs). The GPCR superfamily of 7-transmembrane receptors includes well over 800 species and are targeted by over one-third of currently approved pharmaceuticals (Hauser et al., 2017). A2AR activates the stimulatory heterotrimeric G protein (Gsαβγ) and is a target for the treatment of inflammation, cancer, diabetes, and Parkinson’s disease (Effendi et al., 2020; Guerrero, 2018; de Lera Ruiz et al., 2014; Yu et al., 2020; Zheng et al., 2019). Several GPCRs have been shown to interact with cholesterol, including the serotonin 5-HT1A receptor, the β2-adrenergic receptor, the oxytocin receptor, the smoothened receptor, the CCR5 and CXCR4 chemokine receptors, the CB1 cannabinoid receptor, and A2AR (Gimpl, 2016; Jafurulla et al., 2019; Kiriakidi et al., 2019). Presently, 38 out of 57 published structures of A2AR contain co-crystallized cholesterol (Figure 1). In detergent preparations of A2AR, the soluble cholesterol analog, cholesteryl hemisuccinate (CHS), is important for receptor stability and ligand binding (O’Malley et al., 2011a; O’Malley et al., 2007). Apart from those found in crystal structures, cholesterol interaction sites within A2AR have also been proposed in computational studies. These include the widely conserved cholesterol consensus motif (CCM) in GPCRs, various hydrophobic patches around A2AR, and regions of the receptor interior (Genheden et al., 2017; Guixà-González et al., 2017; Lee et al., 2013; Lee and Lyman, 2012; Lovera et al., 2019; McGraw et al., 2019; Rouviere et al., 2017; Sejdiu and Tieleman, 2020; Song et al., 2019). The CRAC (cholesterol recognition/interaction amino acid consensus) motif, another sequence commonly found in membrane proteins that bind cholesterol, is also present in A2AR (Figure 1B; Li and Papadopoulos, 1998). Additionally, cell-based assays have shown that A2AR-dependent cyclic adenosine monophosphate (cAMP) production is positively correlated with membrane cholesterol (Charalambous et al., 2008; McGraw et al., 2019).

![Figure 1.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig1-v1.jpg)

**Figure 1.:** (A) Overlay of 38 currently published A2AR crystal structures containing co-crystallized cholesterol (extracellular view, with cholesterols shown as orange sticks). For simplicity, extracellular loops and fusion proteins are removed and only one receptor structure is shown (PDB: 4EIY). (B) Side views of (A) highlighting the CCM (blue), the CRAC motifs (green), and V229C 19F labeling site (violet).

Despite the prevalence of cholesterol or its analogues in many crystal structures, there is little consensus on the role that membrane cholesterol plays in A2AR function. While some studies found that ligand binding was unaffected by cholesterol depletion (Charalambous et al., 2008; McGraw et al., 2019), others have observed opposite effects (Guixà-González et al., 2017; O’Malley et al., 2011a; O’Malley et al., 2011b). One study in particular suggested that cholesterol may laterally diffuse in the membrane and enter the receptor interior at the orthosteric site (Guixà-González et al., 2017). Additionally, whereas A2AR is found in both non-raft and raft-like membranes, its colocalization and modulatory effects on other cellular binding partners, including tyrosine receptor kinase B, Ca2+-activated K+ (IK1) channel, and the stimulatory G protein, have been reported to depend on cholesterol-rich microdomains (Charalambous et al., 2008; Lam et al., 2009; Mojsilovic-Petrovic et al., 2006). One possible source of discrepancy between studies is the use of different cell lines. For instance, Guixà-González et al. observed an increased binding by A2AR inverse agonist [3H]ZM241385 upon cholesterol depletion in C6 glioma cells. This effect was absent in a study by McGraw et al., who employed HEK293 cells. Cholesterol extraction or enrichment from cells exhibiting different membrane compositions and signaling patterns may trigger variable cellular response and complicates the comparison of results from different cell lines. The in vitro studies, on the other hand, relied on measuring ligand affinity in detergent micelles while titrating water-soluble cholesterol analogs. Although the composition of detergent preparations can be carefully controlled, the micellar environment is quite different from a lipid bilayer from the perspective of both receptor and cholesterol.

To mitigate the many complexities encountered in live cells or the inherent biases associated with detergent micelles, we employed reconstituted discoidal high density lipoprotein particles (rHDLs, also known as nanodiscs) to investigate the role of cholesterol in A2AR conformation and signaling. In this case, both the size and composition of these phospholipid bilayer model systems can be controlled. Through fluorine nuclear magnetic resonance spectroscopy (19F NMR) and in vitro assays, we find that cholesterol is a weak positive allosteric modulator of A2AR. This can be attributed to a subtle rise in population of the receptor’s active state conformers and a stronger coupling to the G protein. Interactions between A2AR and fluorinated cholesterol analogs appear to be short-lived and non-specific, indicating a lack of high-affinity binding sites or direct allosteric modulation. Rather, the observed allostery is likely a result of indirect membrane effects through cholesterol-mediated changes in bilayer fluidity and thickness, which can be recapitulated (without the use of cholesterol) by the application of hydrostatic pressure.

## Results

### Cholesterol is a weak positive allosteric modulator of A2AR

We sought to explore receptor-cholesterol allostery in a native lipid bilayer environment, free from the complexities associated with other cellular response to membrane alteration in live cells. To this end, we reconstituted A2AR (residues 2–317 with valine 229 mutated to cysteine for 19F-labeling) in nanodiscs containing a 3:2 ratio of 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine (POPC) and 1-palmitoyl-2-oleoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (POPG), supplemented with different amounts of cholesterol. In our hands, cosolubilization of cholesterol with phospholipids prior to reconstitution (Midtgaard et al., 2015) resulted in polydisperse particles and low cholesterol incorporation. We therefore adapted a procedure commonly used in cells and liposomes, to deliver cholesterol via methyl-β-cyclodextrin (MβCD) to preformed nanodiscs (Zidovetzki and Levitan, 2007). This allowed us to incorporate up to ~15 mol% cholesterol into A2AR-embedded nanodiscs without affecting their size distribution (Figure 2—figure supplement 1).

To examine the effects of cholesterol on receptor-mediated G-protein activation, we measured the GTPase activity of purified G proteins (Gsαshortβ1γ2, henceforth referred to as Gαβγ) in the presence of A2AR-nanodiscs containing 0%, 3%, 8%, 11%, and 13% cholesterol. As shown in Figure 2A, similar agonist dose-response profiles were obtained across different cholesterol concentrations. GTP hydrolysis (cumulative over 90 min) was higher in the presence of A2AR relative to G protein alone and was amplified by the agonist 5'-N-ethylcarboxamidoadenosine (NECA) in a dose-dependent manner. Upon careful inspection, a small yet notable decrease in agonist EC50 values can be observed as a function of cholesterol. There is also a slight enhancement in receptor basal activity at high cholesterol concentrations (Figure 2B–C). Thus, functionally cholesterol behaves as a positive allosteric modulator (PAM) of A2AR, although there is very weak cooperativity between cholesterol and agonist.

![Figure 2.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig2-v1.jpg)

**Figure 2.:** (A) Agonist (NECA) dose-response curves for A2AR-nanodiscs containing varying concentrations of cholesterol. The vertical axis represents GTP hydrolysis by purified Gαβγ (cumulative over 90 min) in the presence of A2AR and agonist, relative to GTP hydrolysis by Gαβγ alone in the absence of A2AR. Each data point represents the mean ± SEM (n = 6, technical triplicates). (B) Relative GTP hydrolysis in the presence of apo A2AR (no agonist) in nanodiscs containing varying concentrations of cholesterol. Data represents mean ± SD (n = 6, averages from each technical triplicate presented as individual points) and the asterisk represent statistical significance relative to the 0% cholesterol condition. Statistical significance was determined by one-way ANOVA followed by the Tukey’s multiple comparison test. * p ≤ 0.05. (C) pEC50 values of the NECA dose-response curves in (A). Error bars represent 95% (asymmetrical profile likelihood) confidence intervals.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Hydrodynamic diameters of A2AR-nanodiscs containing varying levels of cholesterol, measured through dynamic light scattering. Data represent mean ± SD (n ≥ 3, technical triplicates).

The weak cholesterol dependence above implies that either cholesterol does not form tight interactions with A2AR, or that the interactions it establishes with the receptor do not grossly overlap with the predominant allosteric pathways established by the agonist. The observed enhancement may also be a consequence of an indirect effect resulting from changes to membrane physical properties. Although the amounts of cholesterol used in this study were lower than that of a typical plasma membrane, they greatly exceed the concentrations needed to saturate potential high-affinity binding sites. Therefore, a simple allosteric mechanism involving specific binding by cholesterol is unlikely.

Using 19F NMR, it is possible to directly assess the effects of cholesterol on the distribution of receptor functional states. Based on the agonist dose-response curves, we expected a stabilization of activation intermediates or active states, at least in the presence of G protein. 19F NMR spectra of A2AR were recorded as a function of ligand, G protein, and cholesterol (Figure 3A and Figure 3—figure supplement 1). In this case, the receptor was labeled at the intracellular side of transmembrane helix 6 (TM6), in a region known to undergo large conformational changes upon activation (Figure 3B). The resulting resonances have been assigned in our previous works and are shown as cartoons in Figure 3C (Huang et al., 2021; Ye et al., 2016). Briefly, S1 and S2 represent two inactive state conformers differentiated by a conserved salt bridge (‘ionic lock’) between TM3 and TM6. The A3 state is an activation intermediate stabilized by Gαβγ binding in the absence of ligands and is hence associated with the ‘precoupled’ state. A1 and A2 represent distinct active state conformers that facilitate nucleotide exchange in the receptor G-protein complex. It was found that while A1 is preferentially stabilized by full agonist, A2 is more pronounced in the presence of partial agonist.

![Figure 3.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig3-v1.jpg)

**Figure 3.:** (A) 19F NMR spectra of A2AR in nanodiscs containing 0, 4, and 13% cholesterol, as a function of ligand and G protein. Two inactive states (S1-2) and three active states (A1-3), previously identified, are indicated by gray dashed lines. For each ligand condition, spectra from the three cholesterol concentrations are normalized via their inactive state intensity. (B) Intracellular view of an inactive (gray, PDB: 4EIY) and an active (yellow, PDB: 5G53) crystal structure of A2AR highlighting the movement of TM6 upon activation. The 19F-labeling site is shown in violet. (C) Cartoon representations of the key functional states of A2AR indicated in (A). At the bottom are two inactive states (S1 and S2) where a conserved salt bridge is either intact or broken. A3 is an intermediate state that facilitates G-protein recognition and precoupling. A1 and A2 are active states that drive nucleotide exchange. While A1 is more efficacious and preferentially stabilized by the full agonist, A2 is less efficacious and reinforced by a partial agonist.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Non-overlapped (relative to Figure 3) 19F NMR spectra of A2AR-V229C in nanodiscs containing 0, 4, and 13% cholesterol.

Inspection of the overlaid spectra in Figure 3A reveals nearly identical distributions of conformational states between A2AR in the presence of 0% and 4% membrane cholesterol. At 13% cholesterol, subtle changes can be observed in the inverse agonist-saturated, apo, full agonist-saturated, and full agonist+ Gαβγ spectra. In particular, we observed a small population shift toward the active states, A1 and A2. The results imply that cholesterol is a positive allosteric modulator of A2AR and acts in part through stabilization of the active state ensemble. Interestingly, 13% cholesterol resulted in line-broadening and a 0.09 ppm downfield shift of the A1 state in the full agonist-saturated spectrum, changes which are not observed in the full agonist+ Gαβγ condition. The changes seen with the A1 resonance in the presence of 13% cholesterol and NECA alone are likely a consequence of exchange between A1 and the inactive ionic lock broken state (S2) and/or a perturbation of the average orientation of TM6. Clearly, cholesterol exerts differential effects on distinct conformers in the ensemble. The outcome of the NMR experiments is consistent with the GTPase activity assay. Nearly complete overlap between the 0% and the 4% spectral series suggest that the principal allosteric mechanism is unlikely related to high-affinity binding. While the subtle changes observed at 13% cholesterol are evidence for positive allosteric modulation, the effects are much smaller than those of any orthosteric ligands or other known allosteric modulators of A2AR (Gao et al., 2020; Ye et al., 2018).

To understand if the weakly activating role of cholesterol arises because of enhanced efficiency in nucleotide exchange or pre-association with G protein (precoupling), we carried out 19F NMR experiments on apo-A2AR in the presence of Gαβγ without agonist. As mentioned above, this condition produces the precoupled receptor-G protein complex and greatly stabilizes the A3 state (Huang et al., 2021). This is recapitulated in Figure 4 for all three cholesterol concentrations, where a shift in the equilibrium populations toward the active conformers, particularly A3 and A2, is observed upon the addition of Gαβγ. Importantly, an increase in cholesterol further enhanced the A3 state in addition to a decrease in the peak width. The magnitudes of these changes are small, consistent with results shown in Figures 2–3. The results suggest that membrane cholesterol may help to stabilize the precoupled complex of A2AR and G protein, and possibly modulates the amplitudes of motion about the precoupled state. This in turn may favor further conformational exchange to A1 or A2. Taken together, 19F NMR showed that mechanistically, the PAM effect of cholesterol in A2AR can be attributed to an increase in the population of active state conformers as well as a more robust coupling to the G protein.

![Figure 4.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig4-v1.jpg)

**Figure 4.:** 19F NMR spectra of apo A2AR in the presence of 0, 4, and 13% cholesterol, and as a function of Gαβγ. The key functional states are indicated by gray dashed lines and the three spectra in the presence of G protein are normalized via the A2 state.

### Allosteric network analysis reveals small negative allosteric modulation by cholesterol

Given the above observations, we employed rigidity-transmission allostery (RTA) analysis (Sljoka, 2021) to survey allosteric activation pathway perturbation by cholesterol within the ternary complex. The RTA algorithm is a computational tool based on mathematical rigidity theory and has been used to identify allosteric networks within proteins (Jacobs et al., 2001; Sljoka, 2021; Whiteley, 2005). It predicts how changes in the conformational rigidity or flexibility of one region in the protein are transmitted to distal sites by quantifying the resulting differences in the degrees of freedom within the system. Similarly, ligand-induced perturbations can be examined by rigidifying the ligand itself or its binding pocket. Using a model of an agonist- and GDP-bound A2AR-Gsαβγ complex, equilibrated in a 1 µs simulation in POPC bilayer with 20% cholesterol, our previous work revealed that rigidification of the agonist NECA results in changes in the degrees of freedom which can be transmitted from the orthosteric pocket to the Gα nucleotide binding site (Huang et al., 2021). This allosteric network encompasses large portions of the receptor, the N- and C-terminal helices of Gα, parts of the Gα Ras domain, three out of seven beta propellers within Gβ, and a section of the Gβ N-terminal helix that forms coiled-coil interactions with Gγ.

Using the above model, we repeated the RTA analysis to examine whether this previously identified allosteric network is sensitive to the presence of cholesterol. Seven cholesterol molecules were found in the vicinity (within 6 Å) of A2AR and were removed prior to rigidification of the agonist. The resulting change in degrees of freedom is mapped in Figure 5 for each residue within the ternary complex. Removal of cholesterol gave rise to an allosteric pathway which is very similar to that in the presence of cholesterol, although with altered intensities for some regions. Higher allosteric transmission is observed for the CWxP motif of TM6, in particular the tryptophan toggle switch W2466.48, in the absence of cholesterol. On the other hand, stronger allosteric transmission is observed for the NPxxY motif of TM7 in the presence of cholesterol. Interestingly, the removal of cholesterol resulted in a slight overall enhancement in allosteric transmission to the G protein. This includes the Gα N- and C-terminal helices which interact with the receptor, as well as Gβ which has been found to play a role in conferring ligand efficacy (Huang et al., 2021). The above observations suggest that the overall presence of cholesterol, while not drastically perturbing, reduces signal transmission across the ternary complex. While these results are inconsistent with our experimental observations, it is also possible that there are indirect effects from cholesterol (e.g., stretching of the hydrophobic bilayer thickness) that override the effects predicted by the allosteric network analysis, as discussed below.

![Figure 5.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig5-v1.jpg)

**Figure 5.:** (A) Allosteric networks within the A2AR-Gαβγ complex in the presence and absence of cholesterol, revealed through RTA analysis via rigidification of the agonist NECA (yellow spheres). The intensity of allosteric transmission is measured by the resulting regiospecific changes in degrees of freedom and is mapped in color (red/blue gradient bar). Cholesterol molecules are shown as orange sticks while green spheres represent GDP. (B) The intensity of allosteric transmission is plotted for each residue in A2AR, Gα, and Gβ. Secondary structural elements are indicated on the right. Gray blocks denote α-helices and β-strands, while white gaps represent loops. For the Gα subunit, the common Gα numbering system is used (Flock et al., 2015).

### A2AR-cholesterol interactions are short-lived and non-specific

To further evaluate the nature of cholesterol-A2AR interactions, we carried out 19F NMR experiments of fluorinated cholesterol analogs, delivered into either empty or A2AR-embedded nanodiscs via MβCD. Two different molecules were tested (Figure 6). 3β-Fluoro-cholest-5-ene (3β-F-chol) was synthesized in house and features a fluorine atom in place of the cholesterol hydroxyl headgroup. The fluoro group is a relatively benign substitute for the hydroxyl due to its similar size and electronegativity. It also retains some ability to accept hydrogen bonds (Hoffmann and Rychlewski, 2002). Another cholesterol analog, referred to as F7-chol, was purchased commercially and had the tail isopropyl group replaced by CF(CF3)2. Incorporation of these analogs did not affect the response of A2AR toward ligands nor its ability to activate the G protein (Figure 6—figure supplement 1).

![Figure 6.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig6-v1.jpg)

**Figure 6.:** Non-decoupled 19F NMR spectra of 3β-F-chol (A) and F7-chol (B) in chloroform, empty nanodisc, and A2AR (apo)-embedded nanodisc. The fluorine groups contributing to each of the resonances are circled and shown above the corresponding peak.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Cumulative hydrolysis of GTP by Gαβγ in the presence of A2AR-nanodiscs with and without 19F-cholesterol analog, relative to GTP hydrolysis by Gαβγ alone in the absence of A2AR. To assess ligand sensitivity, samples were saturated with either inverse agonist (ZM241385), no ligand, partial agonist (LUF5834), or full agonist (NECA). Data represent mean ± SEM (n = 3, technical triplicates).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** 19F NMR spectra of 3β-F-chol (A) and F7-chol (B) in A2AR-embedded nanodiscs in the presence of inverse agonist (ZM241385), no ligand, full agonist (NECA), or NECA+ mini Gs. The fluorine groups giving rise to each resonance are shown above their corresponding peaks and the blue arrows indicate the direction of chemical shift change in response to the addition of ligand and mini-Gs.

The NMR resonances were significantly broadened for both cholesterol analogs upon incorporation into the membrane (Figure 6). This is expected for lipid molecules situated in a slow-tumbling nanodisc. In the case of F7-chol, the peak shapes are further complicated by resonance overlap of the two CF3 groups, which are inequivalent and exhibit complicated multiplicity patterns. Comparison between the spectra of 3β-F-chol in empty nanodiscs and A2AR-embedded nanodiscs shows a clear environmental difference in the presence of receptor (Figure 6A). The resonance is ~0.5 ppm upfield shifted and broader relative to empty nanodiscs. However, the lack of difference in chemical shift or line width between 4% and 11% 3β-F-chol suggests that the above changes are predominantly a result of altered environment (i.e., availability of hydrophobic proteinaceous surfaces) rather than a shift toward receptor-bound states at specific binding pockets.

The spectra of F7-chol are harder to interpret. Due to the two overlapping CF3 resonances, a small change in chemical shift for either one could bring about dramatic variation in the overall peak shape (Figure 6B). For example, it is clear from the two empty nanodisc spectra (containing either 6% or 9% F7-chol) that the membrane environment is altered with increasing F7-chol. Therefore, we cannot be confident about whether the observed changes in the CF3 peaks in the presence of to A2AR are a consequence of specific binding or simply changes in the membrane environment. Based on the rough chemical shift values of the CF3 and CF resonances, the latter explanation is more probable. Overall, the NMR data from the two 19F-cholesterol analogs show environmental differences between empty and A2AR-embedded nanodiscs as well as between different cholesterol concentrations. However, there is no direct evidence of a long-lived receptor-bound state.

In the case of a classical PAM, stronger receptor binding is expected in the presence of an agonist or G protein, versus an inverse agonist. The opposite would hold for a classical negative allosteric modulator (NAM). Yet, there was no apparent difference in chemical shift sensitivity toward agonist or inverse agonist for either 19F cholesterol analogs (Figure 6—figure supplement 2). The NMR spectra of 3β-F-chol in A2AR-embedded nanodiscs are nearly identical upon the addition of inverse agonist, full agonist, and mini-Gs, a G-protein mimetic that has been shown to stabilize the A1 active state (Carpenter et al., 2016; Huang et al., 2021). Small chemical shift changes were observed for F7-chol between the apo receptor and the ligand/mini-Gs-bound conditions. However, the direction of shift is the same between full agonist and inverse agonist. Thus, cholesterol interactions are independent from the identity of the orthosteric ligand bound to A2AR, despite being observed as a functional PAM in vitro (Figures 2–3) and predicted as a NAM in silico (Figure 5). It is distinctly possible that the small shift perturbations observed with ligand and mini-Gs are a consequence of F7-chol contacting multiple sites on the receptor. Nevertheless, the lack of any pronounced shift perturbation (particularly in the presence of agonist since we observe cholesterol to behave as a PAM) leads us to consider that cholesterol interactions are transient. It is therefore more likely that the observed positive allosteric effects of cholesterol are predominantly indirect and relayed through the physical changes to the membrane bilayer.

### Cholesterol allostery in A2AR may be a result of indirect membrane effects

The effects of cholesterol on the physical properties of lipid bilayers have been well documented. The planar structure of cholesterol promotes orientational order in the liquid disordered phase of the bilayer, leading to reduced lateral diffusion and increased hydrophobic thickness (Figure 7A; Crane and Tamm, 2004; de Meyer and Smit, 2009; Filippov et al., 2003; Hung et al., 2007). For instance, as much as 20% increase in thickness can be expected for a POPC bilayer when the cholesterol concentration is varied from 0% to 30% (Mouritsen and Bagatolli, 2016; Tharad et al., 2018).

![Figure 7.](https://cdn.elifesciences.org/articles/73901/elife-73901-fig7-v1.jpg)

**Figure 7.:** (A) The lipid bilayer can be rigidified and thickened upon addition of cholesterol or an increase in lateral pressure. (B) Averaged fluorescence spectra (n = 4) of Laurdan in A2AR-embedded nanodiscs containing varying concentrations of cholesterol. (C) The emission intensity of Laurdan at 440 nm and 490 nm were used to calculate the generalized polarization values. Data represent mean ± SEM (n = 4, technical triplicates). Astrisks represent statistical significance over both the 0% and the 3% conditions. Statistical significance was determined via one-way ANOVA followed by Tukey’s multiple comparisons test. ** p ≤ 0.01. (D) 19F NMR spectra of A2AR, in the absence of ligand or cholesterol, acquired at 1, 200, 1000, and 2000 bar pressures. The key functional states are indicated by gray dashed lines.

We employed the lipophilic fluorescent probe Laurdan to monitor the membrane orientational order of A2AR-embedded nanodiscs as a function of cholesterol. The generalized polarization (GP = $\frac{I_{440}-I_{490}}{I_{440}+I_{490}}$) of Laurdan fluorescence is a consequence of solvent contact. Fluid (disordered) membranes exhibit smaller GP values, a consequence of dipole relaxation between Laurdan and nearby water molecules which causes a red shift of the emission wavelength. In a phospholipid bilayer, greater water accessibility at the hydrophobic-hydrophilic interface is typically a signature of enhanced reorientational dynamics within the lipid milieu (Yu et al., 1996). As shown in Figure 7B–C, we observed a consistent shift of the Laurdan fluorescence spectra which gave rise to higher GP values at elevated cholesterol concentrations. This indicates that cholesterol incorporation enhances lipid orientational order in A2AR-embedded nanodisc bilayers.

An enhanced orientational order arises from a higher fraction of trans conformers in the lipid chains and consequently, an increased hydrophobic thickness. In the case where A2AR adopts an ensemble of states, the equilibrium is expected to shift toward those states which are more compatible with an increased hydrophobic thickness (Andersen and Koeppe, 2007). Bilayer thickness can be readily modulated by changing the composition of lipids or acyl chain lengths. Alternatively, the application of hydrostatic pressure can be used in an NMR experiment to affect changes in bilayer properties while avoiding potential complications associated with specific lipid-receptor interactions. For a typical liquid-crystalline phosphatidylcholine bilayer, pressure-induced compression is far more significant in the lateral than in the transverse/perpendicular direction (Stamatoff et al., 1978). An elevation in pressure at constant temperature promotes ordering of the fatty acyl chains. This leads to an increase in lipid packing density and hydrophobic thickness, and a reduction of lateral diffusion (Ding et al., 2017). Thus, hydrostatic pressure provides an effective way to mimic the ordering effects of cholesterol on a lipid bilayer (Figure 7A).

We recorded the 19F NMR spectra of the apo receptor in nanodiscs without cholesterol, at a pressure of 1, 200, 1000, and 2000 bar. Like increasing cholesterol, the rise in pressure resulted in a bias toward the active ensemble, particularly the A1 (full agonist) state (Figure 7D). Interestingly, the magnitude of change is non-linear and considerably larger at 2000 bar in comparison to 1000 and 200 bar. This is consistent with the expected change in membrane thickness as a function of pressure. For a pure POPC bilayer at 20 °C, the increase in hydrophobic thickness is small (up to ~2 Å) and roughly linear below 1200 bar. Above this pressure, the bilayer transitions to a solid ordered phase which results in a rapid increase of membrane thickness on the order of 10 Å (Rappolt et al., 2003). In comparison, the thickness increase as a result of 10–15% cholesterol is on the order of 1–3 Å (Hung et al., 2007).

The NMR results are similar to that of previous pressure studies of theβ1AR and β2AR in detergent micelles (Abiko et al., 2019; Lerch et al., 2020). In both cases, a shift toward the active state was observed in response to pressure, which was correlated with a reduction in void volume of the active receptor relative to the inactive form. Here, 19F NMR allowed a more detailed delineation of the conformational landscape of A2AR. Unlike agonist- or G-protein-induced activation, where the inactive ensemble is significantly diminished and all three active state conformers are promoted, the redistribution of states brought about by pressure saw a smaller decrease of the inactive ensemble and a specific shift in equilibrium toward the A1 state (Figure 7D). The effects from pressure directly exerted on the receptor cannot be easily separated from indirect effects that are manifested through changes in the lipid bilayer. However, more influence from the membrane is expected since the molecular assembly of lipid bilayers is much more sensitive to pressure relative to the conformation of proteins (Kato and Hayashi, 1999). Both lipid bilayers and detergent micelles are well-known soft systems whose hydrophobic dimensions change precipitously with pressure and whose compressibilities are thus significantly higher than those of membrane proteins (Alvares et al., 2014; Lerch et al., 2020). The lipid bilayer, relative to detergent micelles, was shown to protect integral membrane proteins from pressure-induced denaturation (Kangur et al., 2008). Overall, our pressure-resolved NMR data suggest that A2AR can be regulated indirectly through changes in the lipid bilayer. While the mechanism may be complex and the effects are subtle, receptor activation appears to be favored in an environment with higher packing density, acyl chain order, and hydrophobic thickness.

## Discussion

A2AR has been intensely studied by both X-ray crystallography and more recently by electron cryomicroscopy (cryo-EM). In many cases, cholesterol or CHS have proven useful in stabilizing the receptor and obtaining high-resolution structures. Earlier in vitro and cell-based studies, along with the clear delineation of cholesterol in many crystal structures of A2AR suggest that the molecule may play a direct allosteric role in modulating receptor function. A body of computational work has since showcased cholesterol hot spots across the receptor and some of these studies proposed state-dependent interactions (Lovera et al., 2019; McGraw et al., 2019). Nevertheless, there is no literature consensus on the allosteric role of cholesterol on this prototypical GPCR.

In this study, we set out to investigate both the magnitude and origin of the allosteric interplay between cholesterol and A2AR in phospholipid bilayers, using an identical model membrane system for all functional assays and biophysical experiments. Nanodiscs have been used extensively in functional and structural characterization of complex membrane proteins (Sligar and Denisov, 2021). The protocols used in the current experiments generated monodisperse 8 nm diameter nanodiscs containing a single receptor and roughly 35–40 lipids per leaflet in addition to cholesterol (Hagn et al., 2013; Huang et al., 2021). This is a reductionist system featuring a single receptor surrounded by a fluid POPC/POPG lipid bilayer, with 1–5 cholesterol molecules per leaflet across the concentration range that was investigated. Thus, cholesterol-mediated lateral phase separation, or receptor oligomerization are excluded in this analysis. On the other hand, the receptor can be complexed with heterotrimeric G protein, and the role of cholesterol in modulating the receptor’s state distribution and G-protein coupling can be studied with exquisite sensitivity.

Here, functional and spectroscopic studies in nanodiscs identify cholesterol as a weak PAM. Specifically, GTP hydrolysis assays found a marginal increase in basal activity with increasing cholesterol, in addition to a weak enhancement in the agonist potency. 19F NMR experiments revealed little or no difference in the receptor spectra upon addition of 4% cholesterol. A very modest shift in equilibrium toward the active states (A1 and A2) was observed at 13% cholesterol, corroborating the observed allosteric effects. A distinct enhancement of A3 is also found at 13% cholesterol for the apo receptor bound to G protein, implying that cholesterol either directly or indirectly stabilizes the precoupled A2AR-Gαβγ complex.

Despite the observed enhancement in both G-protein coupling and the activation states, 19F NMR of two fluorinated cholesterol analogs implied a weak or transient interaction between cholesterol and A2AR. Moreover, the confining conditions of the nanodisc would be expected to favor a cholesterol-bound state. There was also no correlation between the chemical shifts of the cholesterol analogs and orthosteric ligand efficacy, suggesting that the origin of the observed positive allostery is through the indirect effects of cholesterol on the membrane itself.

Laurdan fluorescence experiments confirmed that lipid orientational order is increased by cholesterol in the presence of A2AR. Similarly, hydrostatic pressure is well-known to give rise to increased orientational order in lipid bilayers (Ding et al., 2017; Nicolini et al., 2006). We therefore sought to use hydrostatic pressure as a surrogate to cholesterol to consider potential indirect effects on receptor function that arise simply from membrane ordering. Under conditions where hydrostatic pressure is known to exert similar changes in membrane thickness as 11–13% cholesterol, 19F NMR revealed comparable responses in the conformational ensemble of the receptor – namely a shift in equilibrium to the active states at pressures of 1000 bar or more. We note that denaturation of the protein with these pressures was not observed, based on the observation of 19F NMR spectra of misfolded A2AR which tend to exhibit a single upfield resonance whose shift is insensitive to ligand (unpublished results).

While we cannot rule out the possibility of a cumulative influence from multiple fast-exchanging, weakly binding interactions, results from the current study strongly suggest that changes in membrane physical properties are the primary means by which cholesterol regulates A2AR. There may also be subtle NAM effects from direct interaction with cholesterol, as suggested by our computational analysis, which at the same time are overcome by stronger indirect effects through the membrane. It is possible that this is also the mechanism through which CHS enhances the ligand binding activity of A2AR in detergent micelles (i.e., by modulating the micellar structure to a more bilayer-like morphology). In support of this idea, an evaluation of A2AR reconstituted in various mixed micelle systems revealed a correlation between receptor activity to those detergent/CHS compositions that gave rise to a micellar hydrophobic thickness that closely matches that of native mammalian bilayers (O’Malley et al., 2011b).

Although the nanodisc is an effective membrane mimetic, it is not a perfect replacement of the biological membrane. For example, lipids in nanodiscs exhibit slightly more motional freedom in their headgroup region and less motional freedom at the center of the bilayer in comparison to liposomes (Stepien et al., 2015). They also display a broader phase transition in response to temperature in addition to a transition temperature that is 3-4 °C higher than that of liposomes (Shaw et al., 2004). Nevertheless, we have not performed detailed pressure-dependent NMR studies of the POPC/POPG lipids to confirm that a bilayer-like morphology is maintained throughout the range of pressures used in these experiments.

Another limitation of the current study is the range of cholesterol concentrations being probed, which is below the physiological norm. In cell-based experiments, total cholesterol depletion is not possible without adversely affecting cellular integrity. In many cases, the amount of cholesterol left in the membrane was not quantified and the focus was instead on the disruption of raft-like domains. Our nanodisc samples contained 0–13% cholesterol, which is below the concentration regime for raft formation (Barrett et al., 2013; Crane and Tamm, 2004). These two strategies (extraction from cholesterol-rich membranes and delivery into cholesterol-free membranes) explore largely different processes; the former involves the disruption of rafts while the latter allows studies of the interaction of cholesterol species with the receptor in a monomeric state.

Our data suggests that such interactions, if present for A2AR, are non-specific and short-lived. This may explain why structural and computational work has yet to converge upon a single cholesterol binding site. Like lipids, the observation of cholesterol in crystal structures may simply be a consequence of having cholesterol as a part of the crystallization matrix. In fact, many A2AR structures which do not contain co-crystallized cholesterol (all the active state structures and some inactive state structures) had the molecule present in large quantities during crystallization. In one example, complexes of A2AR bound to an engineered mini-G protein were crystallized in octylthioglucoside micelles either in the presence or absence of CHS. No discernible difference was found between crystals that grew with or without CHS and the structure was solved using data collected from two crystals, one from each condition (Carpenter et al., 2016). Similarly, the numerous cholesterol ‘hot spots’ predicted through computational approaches may not necessarily indicate functional specificity, but rather geometric compatibility between certain hydrophobic patches or grooves surrounding the receptor and the cholesterol backbone. This is reflected in the fact that nearly all seven transmembrane helices and grooves between helices in A2AR have been predicted in various studies to bind cholesterol (Genheden et al., 2017; Guixà-González et al., 2017; Lee and Lyman, 2012; Lovera et al., 2019; McGraw et al., 2019; Rouviere et al., 2017; Sejdiu and Tieleman, 2020; Song et al., 2019). Furthermore, the presence of CCM or CRAC motifs has recently been shown to not be predictive of cholesterol binding in GPCRs (Taghon et al., 2021).

The current work shows that A2AR does not require cholesterol to function in an in vitro bilayer setting. However, many experiments have highlighted the role of cholesterol-rich domains for A2AR to function in a cellular context. As alluded to above, a major shortcoming of our nanodisc system is the upper limit of cholesterol that can be delivered. This prevented us from evaluating the system at higher, more physiological cholesterol concentrations and probing the effects from protein partitioning between liquid ordered and liquid disordered phases (Gutierrez et al., 2019). It is unclear whether A2AR alone prefers certain regions on the plasma membrane. Nevertheless, both the stimulatory G protein and many isoforms of adenylyl cyclase were shown to partition into raft-like domains (Kamata et al., 2008; Oh and Schnitzer, 2001; Ostrom et al., 2001; Ostrom and Insel, 2004). Spatial co-localization of the receptor with other cellular binding partners in these membrane regions may therefore be required to form and maintain signaling complexes.

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
      <td>Strain, strain background (Pichia pastoris)</td>
      <td>SMD 1163</td>
      <td>Invitrogen</td>
      <td></td>
      <td>A2AR expression host</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21 (DE3)</td>
      <td>Invitrogen</td>
      <td>Cat#: C600003</td>
      <td>Gα expression host</td>
    </tr>
    <tr>
      <td>Strain, strain background (Spodoptera frugiperda)</td>
      <td>Sf9</td>
      <td>ATCC</td>
      <td>ATCC: CRL-1711</td>
      <td>Gβγ expression host</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Plasmid: pET15b containing wild type Gsα</td>
      <td>This paper</td>
      <td></td>
      <td>The plasmid is available upon request to the corresponding author</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>GTPase-Glo</td>
      <td>Promega</td>
      <td>Cat#: V7681</td>
      <td>For GTP hydrolysis assay</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Cholesterol quantification kit</td>
      <td>R-Biopharm and Roche Diagnostics</td>
      <td>Cat#: 10139050035</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2-Bromo-N-(4-(trifluoromethyl)phenyl)acetamide (BTFMA)</td>
      <td>Apollo Scientific</td>
      <td>Cat#: PC8478</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>5'-N-Ethylcarboxamidoadenosine (NECA)</td>
      <td>Tocris</td>
      <td>Cat#: 1,691</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>LUF 5834</td>
      <td>Tocris</td>
      <td>Cat#: 4,603</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ZM 241385</td>
      <td>Tocris</td>
      <td>Cat#: 1,036</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Methyl-β-cyclodextrin</td>
      <td>Millipore Sigma</td>
      <td>Cat#: 332,615</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Guanosine 5'-diphosphate (GDP)</td>
      <td>Millipore Sigma</td>
      <td>Cat#: 51,060</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-Palmitoyl-2-oleoyl-glycero-3-phosphocholine (POPC)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat#: 850457 C</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-Palmitoyl-2-oleoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (POPG)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat#: 840457 C</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cholesterol</td>
      <td>Millipore Sigma</td>
      <td>Cat#: C8667</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>F7-Cholesterol (25,26,26,26,27,27,27-heptafluorocholesterol)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat#: 700,002</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3β-Fluoro-cholest-5-ene</td>
      <td>This paper</td>
      <td></td>
      <td>Synthetic methods are described in this paper. The compound is available upon request to the corresponding author</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Laurdan</td>
      <td>Millipore Sigma</td>
      <td>Cat#: 850582 P</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MestReNova version 12.0.4 or higher</td>
      <td>Mestrelab Research</td>
      <td>https://mestrelab.com/</td>
      <td></td>
    </tr>
  </tbody>
</table>

### A2AR expression, purification, and nanodisc reconstitution

Receptor cloning, expression, and purification have been described previously (Huang et al., 2021; Ye et al., 2016). Briefly, Pichia pastoris (P. pastoris) SMD 1163 (Δhis4 Δpep4 Δprb1) cells carrying the gene for A2AR (residues 2–317 with the V229C mutation for 19F-labeling) were grown to high density in either shaker flasks or a bioreactor. Methanol (5% v/v) was added every 12–16 hr to induce expression and the cells were harvested after 60–72 hr post induction. The receptors were extracted from the yeast membrane, reacted with the fluorine tag 2-Bromo-N-[4-(trifluoromethyl)phenyl] acetamide (BTFMA) when applicable, and further purified in the absence of cholesterol or cholesterol analogs. Prior to cholesterol incorporation, the receptors were reconstituted in rHDL nanodiscs using a 3:2 ratio of 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine (POPC) to 1-palmitoyl-2-oleoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (POPG) and the MSPΔH5 membrane scaffold protein (Hagn et al., 2013). The sample was purified using a HiLoad 16/600 Superdex 200 preparatory grade size exclusion column equilibrated with nanodisc storage buffer (50 mM HEPES, pH 7.4, 100 mM NaCl), and the peak containing monodisperse nanodiscs were collected for cholesterol incorporation and further purification.

### Incorporation of cholesterol and cholesterol analogs

Incorporation of cholesterol and its fluorinated analogs in nanodiscs was achieved via incubation of the nanodiscs with cholesterol solubilized in methyl-β-cyclodextrin (MβCD, MilliporeSigma Canada, Oakville, Canada). One to 2 days prior to incorporation, a concentrated MβCD-cholesterol stock was prepared by mixing cholesterol (MilliporeSigma) with MβCD buffer (50 mM HEPES, pH 7.4, 100 mM NaCl, 40 mM MβCD) to a final concentration of 8 mM (4 mM in the case of fluorinated analogs, due to their increased hydrophobicity). The mixture was sonicated briefly to disperse any large chunks, then incubated at 30 °C for 24–36 hr with shaking until the solution is clear to the eye. The solution is filtered through a 0.2 µM filter to eliminate any undissolved particles, then diluted with MβCD buffer to make MβCD-cholesterol stocks containing 0.8 mM, 2 mM, 3 mM, and 4 mM cholesterol (0.8 mM and 3 mM in the case of fluorinated analogs). These stocks were mixed with nanodiscs collected from the size exclusion column described above (containing both empty and A2AR-embedded nanodiscs, which co-eluted) in a 1:3 v/v ratio, such that the final concentrations in the mixtures are 10 mM MβCD, 20–30 µM nanodisc, and 0.2 mM, 0.5 mM, 0.75 mM, or 1 mM cholesterol, for different levels of cholesterol incorporation. The mixtures were incubated at room temperature for 15 min with gentle shaking, then diluted 10-fold with nanodisc storage buffer containing 1–2 mL bed volume of Ni-NTA resin prior to incubation at 4 °C for 2 hr. After incubation, Ni-NTA resins were collected using a gravity column and washed extensively with nanodisc storage buffer to remove residual empty nanodiscs, MβCD, and MβCD-cholesterol. Nanodiscs containing the His-tagged A2AR were eluted from the column using elution buffer (50 mM HEPES, pH 7.4, 100 mM NaCl, 250 mM imidazole), concentrated, and exchanged to nanodisc storage buffer for subsequent experiments. For empty nanodiscs, a His6-tagged MSPΔH5 protein was used. The reconstituted discs were treated with MβCD-cholesterol as above, incubated with Ni-NTA resins, and the MβCD was washed away prior to elution and concentration.

### Lipid quantification

Phospholipid concentrations were measured using a modified sulfo-phospho-vanillin assay (Frings and Dunn, 1970). Each sample containing unsaturated phospholipids (nanodiscs or phospholipid standards) was dissolved in 50-fold volume of concentrated sulfuric acid and incubated in a boiling water bath for 10 min. The samples were cooled in a cold-water bath for 5 min, then diluted 16-fold with a phospho-vanillin reagent (0.12% w/v vanillin dissolved in 68% v/v phosphoric acid). The samples were incubated in the dark for 30 min prior to absorbance measurements at 525 nm using a spectrophotometer. Lipid concentrations were determined using standard curves of A525 from pure POPC and POPG. In the case of nanodiscs, the lipid concentrations were determined using standard curves of both POPC and POPG:

$$
[Lipid_{nanodisc,adjusted}]=\frac{3}{5}[Lipid_{nanodisc,POPC}]+\frac{2}{5}[Lipid_{nanodisc,POPG}]
$$

### Quantification of cholesterol and fluorinated cholesterol analogs

Cholesterol concentrations were measured calorimetrically using a commercial kit (R-Biopharm and Roche Diagnostics, Cat. No. 10139050035) following the manufacturer’s protocol. The concentrations of 3β-F-cholesterol and F7-cholesterol (Avanti Polar Lipids) were estimated via integration of 19F NMR resonances of the cholesterol analog in relation to a reference compound (fluoroacetate in the case of 3β-F-cholesterol and trifluoroacetate in the case of F7-cholesterol), where the relative signal loss in the reference peak due to shortened relaxation delay was corrected for. Percent cholesterol in a given sample was calculated as follows:

$$
%cholesterol=\frac{[Cholesterol]}{[Lipid]}\times100
$$

### G-protein cloning, expression, and purification

The expression and purification of Gsα, Gβγ, and mini-Gsα have been described previously (Huang et al., 2021) with the only difference being that a wild-type Gsα was used in the current work. To generate this construct, a double-stranded DNA fragment for the wild-type Gsα short isoform was codon optimized and synthesized using the GeneArt service from Thermofisher. This fragment carried overlapping sequences with the previously described pET15b MBP-Gsα mutant sequence (Huang et al., 2021). The plasmid was digested with XhoI and SacI (New England BioLabs, Ipswich, MA, USA) to remove the mutant Gsα sequence and purified via electrophoresis and gel extraction kit (Bio Basic, Markham, Canada). The resulted plasmid backbone and DNA fragment were fused using the pEasy assembly kit from TransGen Biotech following manufacturer’s instructions. The plasmid was transformed into Escherichia coli (E. coli) BL21 (DE3) cells and a resulting colony containing the gene for the wild-type Gsα was selected for protein expression.

### NMR experiments

NMR samples were prepared in nanodisc storage buffer with 20–100 µM A2AR-V229C (BTFMA-labelled for receptor NMR, unlabeled for 19F-cholesterol NMR), 10% D2O, and 20 µM sodium trifluoroacetate (TFA, for receptor NMR) or 100 µM fluoroacetate (for 19F-cholesterol NMR) as the 19F chemical shift reference. For samples containing G protein (1.1-fold excess), the buffer also included 100 µM GDP, 2 mM MgCl2, and 5% glycerol. When applicable, A2AR ligands were added at saturating concentrations (1 mM NECA, 500 µM LUF5834, or 500 µM ZM241385). All samples were sterile-filtered and prepared in sterile Shigemi tubes to prevent microbial contamination. NMR experiments were acquired at 20 °C on a 500 MHz Varian Inova spectrometer equipped with a 5 mm room temperature inverse HFX probe. A typical fluorine NMR experiment included a 100ms recycle delay, a 5.5 μs (45°) excitation pulse, and a 500ms acquisition time. Each experiment acquired between 100,000–400,000 scans, yielding a S/N of approximately 50–100. Spectra were processed using MestReNova (Mestrelab Research S.L.) employing chemical shift referencing (–75.6 ppm for TFA and –217 ppm for fluoroacetate), baseline correction, zero filling, and exponential apodization equivalent to a 5–20 Hz line broadening. For high-pressure NMR, the sample was transferred to a 3 mm zirconia tube (Daedalus Innovations, Aston, PA, USA) and covered with paraffin oil. The tube was placed inside a 600 MHz Varian Inova spectrometer equipped with a triple-resonance cryoprobe tunable to 19F, via a stainless-steel fluid line connected to an Xtreme-60 syringe pump (Daedalus Innovations) prefilled with paraffin oil as the pressurizing fluid. Pressure was increased at a rate of 100 bar/min to the desired value, and the sample was equilibrated for 5 min at the final set pressure prior to acquisition at 20 °C.

### Membrane fluidity measurements

A2AR-embedded nanodiscs were incubated with the fluorescent probe Laurdan (MilliporeSigma) at room temperature for 30 min in the dark at a final concentration of 1 μM A2AR and 10 μM Laurdan (diluted from a 10 mM dimethylformamide stock). Free Laurdan was removed by extensive buffer-exchange with the nanodisc storage buffer and subsequently filtering the sample through a 0.2 μm filter. Flow-through from the final round of buffer-exchange was kept for background correction. The samples were transferred to a black 384-well plate and the fluorescent emission spectra (410 nm – 520 nm) were acquired using a TECAN Spark multi-mode plate reader (Tecan, Männedorf, Switzerland) at 26 °C with an excitation wavelength of 350 nm. Each emission spectrum was background-corrected, then area-normalized to the 13% cholesterol condition. The generalized polarization (GP) of each sample was determined using the formula $GP=\frac{I_{440}-I_{490}}{I_{440}+I_{490}}$ , where I440 and I490 represent the emission intensities at 440 nm and 490 nm, respectively.

### GTP hydrolysis experiments

GTP hydrolysis experiments were carried out using the GTPase-Glo assay kit (Promega, Madison, WI, USA) following the manufacturer’s protocol (Mondal et al., 2015). Briefly, purified receptor and G protein were incubated at room temperature in a buffer containing 50 mM HEPES, pH 7.4, 100 mM NaCl, 2 mM MgCl2, 1 μM GDP, and 4 μM GTP, at a final concentration of 250 nM G protein, 250 nM A2AR, and various concentrations of the agonist NECA. Control reactions included buffer with GTP but in the absence of either A2AR or both A2AR and G protein. After 90 min, unreacted GTP was converted to ATP prior to the addition of a detection reagent containing luciferase. The resulting luminescence, which is proportional to the amount of unreacted GTP, was measured using a TECAN Spark multi-mode plate reader with an integration time of 1 min. GTP hydrolysis was determined as follows:

G protein only (in the absence of A2AR):

$$
ΔLum_{G}=Lum(bufferonly)−Lum(Gproteinonly)
$$

In the presence of A2AR:

$$
ΔLum_{G+R}=Lum(bufferonly)−Lum(Gprotein+A_{2A}R)
$$

where Lum is the luminescence signal intensity.

The relative GTP hydrolysis for each A2AR (NECA) sample was calculated as follows:

$$
RelativeGTPhydrolysis=\frac{ΔLum_{G+R}}{ΔLum_{G}}\times100
$$

The NECA dose-response data were fit using a variable slope model in GraphPad Prism 8.4.2 employing the equation:

$$
Response=E_{min}+\frac{x^{n}E_{max}-E_{min}}{x^{n}+EC_{50}^{n}}
$$

where $x$ is the agonist concentration, $E_{min}$ is the minimum response, $E_{max}$ is the maximum response, $EC_{50}$ is the agonist concentration that promotes half-maximum response, and $n$ is the Hill coefficient.

### Dynamic light scattering

DLS samples were prepared in nanodisc storage buffer containing 5 μM A2AR-embedded nanodiscs supplemented with different mol% of cholesterol. Each sample was filtered through a 0.2 μm syringe filter to remove large dust particles before transferring to a small-volume 10 mm quartz cuvette (Starna Cells, Atascadera, CA, USA). DLS measurements were carried out inside a Zetasizer Nano-ZS particle size analyzer (Malvern Panalytical, Malvern, United Kindom) equipped with a He-Ne laser (λ = 633 nm). Samples were equilibrated at 25 °C for 2 min and the scattered light was measured at a 173° backscatter angle. The resulting correlation function was analyzed using the general purpose (non-negative least squares) analysis model in the Zetasizer software (v7.13, Malvern Panalytical) for distribution analysis, assuming a buffer viscosity of 0.9066 cP, a buffer refractive index of 1.332, and a protein refractive index of 1.450. Data was averaged over three or four independent trials, each having three replicate measurements of 10–20 scans.

### Synthesis of 3β-fluoro-cholest-5-ene

3β-Fluoro-cholest-5-ene was synthesized from cholesterol in one step, using the deoxyfluorination reagent DAST (diethylaminosulfur trifluoride, Toronto Research Chemicals, North York, Canada). Although fluorinations with DAST often proceed through an SN2 mechanism, fluorination of cholesterol is known to retain its stereochemistry (Rozen et al., 1979). This results from homoallylic participation forming a carbonium ion intermediate (Li et al., 2016; Rozen et al., 1979).

Cholesterol (650 mg, 1.68 mmol) was dissolved in dry CH2Cl2 (15 mL) in a plastic reaction vessel under argon. The mixture was cooled to –20 °C and DAST (four eq., 0.89 mL) was added dropwise over 5 min. The solution was stirred at –20 °C for 1 hr. The cooling bath was removed, and the reaction was continued at rt for 3 hr. It was quenched by slowly pouring the mixture into a vigorously stirred solution of sodium bicarbonate at 0 °C. After the bubbling stopped, the aqueous phase was extracted twice with CH2Cl2 (50 mL). The organic layer was washed with brine and concentrated to give an orange syrup. Silica column chromatography (eluent: 100% pentanes, Rf = 0.27) yielded the product as a white solid (283 mg, 43%). The product’s spectroscopic characterization was consistent with published data (Li et al., 2016; Reibel et al., 2015).

1 H NMR (400 MHz, CDCl3) δ 5.39 (d, J = 4.9, 1 H), 4.67–4.13 (dm, 2JH-F = 50.4 Hz, 1 H), 2.44 (t, J = 7.0, 2 H), 2.10–1.92 (m, 3 H), 1.93–1.78 (m, 2 H), 1.77–1.63 (m, 1 H), 1.63–0.80 (m, 32 H), 0.69 (s, 3 H). 19 F NMR (377 MHz, CDCl3) δ –167.82 (dm, 2JF-H = 50.4 Hz). 13 C NMR (101 MHz, CDCl3) δ 139.50 (d, J = 12.6 Hz), 123.16 (d, J = 1.3 Hz), 92.98 (d, J = 174.1 Hz), 56.88, 56.33, 50.17 (d, J = 1.8 Hz), 42.49, 39.91, 39.69, 39.57 (d, J = 19.3 Hz), 36.69 (d, J = 1.2 Hz), 36.53 (d, J = 10.8 Hz), 36.36, 35.95, 32.09 (d, J = 1.1 Hz), 32.03, 28.95 (d, J = 17.5 Hz), 28.39, 28.18, 24.45, 24.01, 22.98, 22.73, 21.29, 19.47, 18.89, 12.02. HRMS (EI): Calcd. For C27H45F: 388.3505; Found: 388.3506.

### Computational rigidity-transmission allostery analysis

The fully active state of A2AR in complex with Gsαβγ, NECA and GDP was constructed, equilibrated and relaxed in a 1 µs MD simulation in 4:1 POPC:cholesterol extended membrane as previously described (Huang et al., 2021). This model was used to probe agonist-induced allosteric communication in the A2AR-Gαβγ complex with rigidity-transmission allostery (RTA) algorithm, whose details have been previously described (Huang et al., 2021; Ye et al., 2018). The RTA algorithm is a computational method based on mathematical rigidity theory, which predicts how perturbations of conformational rigidity and flexibility (conformational degrees of freedom) at one site transmit across a protein or a protein complex to modify degrees of freedom at other distant sites (Sljoka, 2021). Here, RTA was applied to examine the allosteric pathways between the orthosteric pocket and distal regions in the A2AR-Gαβγ complex with and without cholesterol. We quantified the available conformational degrees of freedom at every residue before and after rigidification of the agonist NECA. The change in degrees of freedom was then extracted for each residue, which represents the extent of allosteric transmission from the orthosteric pocket. In the presence of cholesterols, the analysis was carried out as previously described (Huang et al., 2021). To measure the impact of cholesterol on allosteric communication, the same analysis was repeated upon removal of all seven cholesterols found within 6 Å of the receptor.

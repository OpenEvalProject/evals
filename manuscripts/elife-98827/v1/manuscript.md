# Induction of hepatitis B core protein aggregation targeting an unconventional binding site

## Authors

- Vladimir Khayenko<sup>1</sup>
- Cihan Makbul<sup>1</sup>
- Clemens Schulte<sup>1</sup>
- Naomi Hemmelmann<sup>1</sup>
- Sonja Kachler<sup>1</sup>
- Bettina Böttcher<sup>1</sup> ([ORCID: 0000-0002-7962-4849](https://orcid.org/0000-0002-7962-4849)) †
- Hans Michael Maric<sup>1</sup> ([ORCID: 0000-0002-2719-4752](https://orcid.org/0000-0002-2719-4752)) †

### Affiliations

1. Rudolf Virchow Center, Center for Integrative and Translational Bioimaging; University of Würzburg Würzburg Germany ([ROR:00fbnyb24](https://ror.org/00fbnyb24))
2. Biocenter, University of Würzburg Würzburg Germany ([ROR:00fbnyb24](https://ror.org/00fbnyb24))

† Corresponding author

## Abstract

The hepatitis B virus (HBV) infection is a major global health problem, with chronic infection leading to liver complications and high death toll. Current treatments, such as nucleos(t)ide analogs and interferon-α, effectively suppress viral replication but rarely cure the infection. To address this, new antivirals targeting different components of the HBV molecular machinery are being developed. Here we investigated the hepatitis B core protein (HBc) that forms the viral capsids and plays a vital role in the HBV life cycle. We explored two distinct binding pockets on the HBV capsid: the central hydrophobic pocket of HBc-dimers and the pocket at the tips of capsid spikes. We synthesized a geranyl dimer that binds to the central pocket with micromolar affinity, and dimeric peptides that bind the spike-tip pocket with sub-micromolar affinity. Cryo-electron microscopy further confirmed the binding of peptide dimers to the capsid spike tips and their capsid-aggregating properties. Finally, we show that the peptide dimers induce HBc aggregation in vitro and in living cells. Our findings highlight two tractable sites within the HBV capsid and provide an alternative strategy to affect HBV capsids.

## Introduction

The hepatitis B virus (HBV) infects the liver and can cause acute and chronic hepatitis. In childhood and infancy, the virus is particularly dangerous as the recovery rate among children is approximately 50%, while among infants infected through perinatal transmission, only 10% will naturally recover, the remainder will develop chronic infection (Thomas, 2019; Block et al., 2021). On the global scale, the most effective approach to address hepatitis B is through preventive treatment with vaccinations. However, the goals of achieving sufficient vaccination coverage and timely immunization have yet to be met (Thomas, 2019; Cox et al., 2020). Furthermore, vaccinations are ineffective for individuals who are already infected (Dienstag et al., 1982). With about 300 million chronic carriers and over 800,000 hepatitis-related yearly deaths, chronic hepatitis B is a global health problem (Block et al., 2021; World Health Organisation, 2022) that requires a solution.

Currently, there are two approved classes of medications for the treatment of chronic hepatitis B: nucleos(t)ide analogs (NAs) and interferon-α and its derivatives (IFN-α) (Hepatitis B Foundation, 2023; Jeng et al., 2023). NAs compete for binding with the natural nucleotide substrates, inhibiting the viral protein P in charge of the reverse transcription of the viral pre-genomic RNA (pgRNA) into HBV DNA (Menéndez-Arias et al., 2014) IFN-α serves as both an immunomodulator and immunostimulant, activating genes with diverse antiviral functions to target various steps of viral replication. Additionally, it indirectly suppresses HBV infection by modifying cell-mediated immunity (Liang et al., 2015).

Present treatments effectively suppress HBV replication, reduce liver inflammation, fibrosis, and the risk of cirrhosis and hepatocellular carcinoma (HCC), but IFN-α treatment is associated with significant adverse effects and NAs typically require long-term oral administration, often lifelong, as treatment discontinuation often results in viral rebound and disease recurrence in many patients. While current therapies manage the disease, a clinical cure is seldom achieved, and the risk of HCC, although reduced, remains (Jeng et al., 2023). Consequently, various classes of direct-acting antivirals and immunomodulatory therapies are currently under development, aiming to achieve a functional cure following a finite treatment duration (Cornberg et al., 2020).

New HBV antivirals capitalize on the enhanced understanding of the viral life cycle and can be categorized into several classes (Table 1): entry inhibitors that disrupt HBV entry into hepatocytes by blocking the binding to the sodium/taurocholate co-transporting polypeptide (NTCP) receptor (Yan et al., 2012). HBsAg inhibitors based on nucleic acid polymers that interfere with the production of HBV surface antigens, and viral gene repressors based on nucleases. Translation inhibitors based on small interfering RNAs or antisense oligonucleotides that silence HBV RNA, thereby decreasing the viral antigen production. Finally, the capsid assembly modulators (CAMs) target the hepatitis B core protein (HBc) that participates in multiple essential steps of the HBV life cycle (Jeng et al., 2023).

**Table 1.**
 Direct-acting hepatitis B virus (HBV) antivirals.


<table>
  <thead>
    <tr>
      <th>Class</th>
      <th>Mechanism of action</th>
      <th>Examples</th>
      <th>Development stage (Hepatitis B Foundation, 2023)</th>
      <th>Molecule type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Entry inhibitors</td>
      <td rowspan="2">NTCP (sodium/taurocholate co-transporting polypeptide) receptor (Watashi and Wakita, 2015) inhibition.</td>
      <td>Bulevirtide (Ligat et al., 2021)</td>
      <td>Phase III</td>
      <td>Lipopeptide</td>
    </tr>
    <tr>
      <td>A2342 (Bonn et al., 2022)</td>
      <td>Preclinical</td>
      <td>Small molecule</td>
    </tr>
    <tr>
      <td>HBsAg inhibitor</td>
      <td>Inhibition of the host HSP40 chaperone DNAJB12 that mediates spherical HBV assembly. Reduces the HBsAg in the circulation and lowers intracellular HBsAg (Vaillant, 2022).</td>
      <td>REP 2139 (Vaillant, 2019)</td>
      <td>Phase II</td>
      <td>Nucleic acid polymer</td>
    </tr>
    <tr>
      <td rowspan="2">Translation inhibitors</td>
      <td rowspan="2">Antisense oligonucleotide (ASO) or small interfering RNAs (siRNA) (Gareri et al., 2022) that target HBV messenger RNAs and act to decrease levels of viral proteins.</td>
      <td>Bepirovirsen (Yuen et al., 2022)</td>
      <td>Phase III</td>
      <td>ASO</td>
    </tr>
    <tr>
      <td>VIR-2218 (Gane et al., 2023)</td>
      <td>Phase II</td>
      <td>siRNA</td>
    </tr>
    <tr>
      <td rowspan="2">Viral gene repressors</td>
      <td rowspan="2">Specific cleavage mediation of viral covalently closed circular DNA (cccDNA) via nucleases (Ono and Bassit, 2021).</td>
      <td>PBGENE-HBV (Gorsuch et al., 2022)</td>
      <td>Preclinical</td>
      <td>Endonuclease I-CreI</td>
    </tr>
    <tr>
      <td>EBT107 (Ono and Bassit, 2021)</td>
      <td>Preclinical</td>
      <td>CRISPR-Cas9</td>
    </tr>
    <tr>
      <td rowspan="2">Capsid assembly modulators</td>
      <td rowspan="2">Target the hydrophobic pocket located at the dimer-dimer interface near the C termini of HBc subunits and induce misassembly of the core protein, thereby impeding the formation of infectious progeny virions (Ono and Bassit, 2021; Kim et al., 2021; Zheng et al., 2023).</td>
      <td>Canocapavir (Zheng et al., 2023)</td>
      <td>Phase II</td>
      <td>Small molecule</td>
    </tr>
    <tr>
      <td>EDP-514 (Feld et al., 2022)</td>
      <td>Phase I</td>
      <td>Small molecule</td>
    </tr>
  </tbody>
</table>

Among the direct acting antivirals that are in preclinical or clinical studies, a third are CAMs (Hepatitis B Foundation, 2023). Capsids are attractive targets due to the absence of human homologues for HBc and their involvement in crucial stages of the HBV life cycle, including nuclear entry, encapsulation of the pgRNA and polymerase, optional nuclear recycling to replenish the covalently closed circular DNA (cccDNA) pool, and eventual coating and secretion from infected cells (Jeng et al., 2023; Kim et al., 2021).

The capsid is composed of 120 units of HBc dimers, assembling into a T = 4 icosahedron. Within this structure, 60 asymmetric units are formed by four HBc monomers each, designated as A, B, C, and D, or AB dimers and CD dimers (Crowther et al., 1994). The ultrastructure formed by the HBc dimer reveals several binding pockets that can be exploited as potential targets for modulating protein activity (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig1-v1.jpg)

**Figure 1.:** (A) Left: close-up view of the three addressable effector sites within HBc-dimers (shown as cartoon model with transparent surface in gray) together with representative ligands shown as stick models: SLLGRM peptide (marine blue, PDB: 7PZN); geraniol, resolved here (cyan); heteroaryldihydropyrimidine (HAP [(2S)-1-[[(4R)-4-(2-chloranyl-4-fluoranyl-phenyl)-5-methoxycarbonyl-2-(1,3-thiazol-2-yl)-1,4-dihydropyrimidin-6-yl]methyl]-4,4-bis(fluoranyl)-pyrrolidine-2-carboxylic acid], green, PDB: 5WRE). HAP is a representative example of a canonical capsid assembly modulator (CAM) that targets a hydrophobic pocket mediating HBc-dimer multimerization, an essential step in capsid assembly. A blue arrow indicates how dimeric peptide-based ligands may induce aggregation. Right: the general architecture of an HBc-dimer is depicted as a cartoon with transparent surface model in gray and the three ligands that target distinct binding pockets are in color. The binding sites of two HBc dimers can be linked by dimeric ligands, here exemplified with the peptide ligand. (B) Hypothetical mode of action of HBc aggregation triggered by cross-linking the spikes of individual HBc dimers, HBc multimers or the whole capsid.

CAMs target the hydrophobic pocket at the HBc dimer–dimer interface, upon binding they strengthen the association energy between HBc-dimer subunits, thereby promoting capsid assembly, rather than inhibiting it (Venkatakrishnan et al., 2016; Stray et al., 2005). As a result, abnormal or empty capsids may form, sometimes accompanied by the aggregation of core proteins, consequently inhibiting HBV DNA replication. Additionally, CAMs can disrupt the disassembly of incoming virions and the intracellular recycling of capsids, thereby impeding the establishment and replenishment of cccDNA (Jeng et al., 2023; Kim et al., 2021; Zoulim et al., 2022; Schlicksup and Zlotnick, 2020).

Recently, a new potentially druggable site was discovered in the HBc dimer—a hydrophobic pocket formed at the base of the spike. This site was targeted by the detergent Triton X-100 (TX100), ultimately causing conformational alterations in the capsid structure (Lecoq et al., 2021; Makbul et al., 2021b). In addition to the spike base hydrophobic pocket, there is another less-explored interacting domain located on the spike tip of the HBc dimer. Previous studies have shown that peptides targeting the cleft on the spike tip reduced viral replication in a cell model, likely by interfering with viral assembly through modulation of the HBc interaction with the surface antigen (Böttcher et al., 1998). These two effector sites could serve as a foundation for the development of new types of HBc modulators and provide alternatives ways for controlling HBV infections.

In this study, we characterize and explore these alternative HBc binding pockets at the inner-dimer interface in the center and at the tips of capsid spikes (Lecoq et al., 2021; Makbul et al., 2021b; Makbul et al., 2021a), and unveil the HBc aggregating properties of a spike-binding dimeric peptide.

## Results

HBV capsid assembly modulation via the binding pockets on the HBc multimer ultrastructure represents a promising pharmacological strategy but until now only one site located on the HBc dimer–dimer interface was explored (Figure 1A; Kim et al., 2021; Zheng et al., 2023). We designed and synthesized bivalent binders specifically targeting two distinct regions of the HBV core protein (HBc)—the hydrophobic pocket at the dimer interface and the tips of the capsid spikes (Figure 1). These binders, designed to engage both sites with avidity enhanced affinity, were evaluated for their binding affinity and their effects on HBV capsids in both in vitro assays and living cell models.

### Geranyl dimer targets the central hydrophobic pocket of HBc-dimers with micromolar affinity

Hydrophobic post-translational modifications, such as myristylation of the large hepatitis B virus surface protein (L-HBs), are essential for HBV infectivity and play a role in mediating viral assembly (Gripon et al., 1995). Additionally, farnesylation, another hydrophobic post-translational modification, is involved in the envelopment of hepatitis D virus (HDV) (Koh et al., 2015), which relies on the presence of HBV and its protein machinery for propagation. Recently, TX100, a nonionic surfactant sharing a similar hydrocarbon binding motif as the natural HBV post-translational modifications, was identified as a ligand of a distinct hydrophobic pocket in the center of HBc-dimers (Lecoq et al., 2021; Makbul et al., 2021b; Roseman et al., 2005).

Several of the pocket forming amino acids, such as K96 and 129-PPAY-132 (Rost et al., 2006) and the natural occurring point mutations HBcP5T, L60V, F97L, and P130T (; Le Pogam et al., 2000; Yuan and Shih, 2000; Yuan et al., 1999a; Ehata et al., 1992) are involved in the secretion of enveloped virions from the cell. These findings lead to the infectious HBV particles signal hypothesis where this hydrophobic pocket is involved in the regulation of the envelopment of nucleocapsids and thus could be an alternative druggable pocket to block virus envelopment (Roseman et al., 2005).

We reasoned that compounds mimicking the natural HBV/HDV compounds and sharing a hydrophobic motif similar to that of TX100 can prove to be potent binders of this key hydrophobic pocket. Therefore, we set out to test n-decyl-beta-d-maltopyranoside (DM) (1), geraniol (2), and its synthesized dimer (3), as the mimetics of myristic acid and farnesyl, respectively.

The isothermal calorimetric titration (ITC) of HBc capsids with DM (1) resolved micromolar affinity (KD = 133 ± 38 µM) to all four hydrophobic pockets of HBc capsids’ asymmetric unit (N = 1.05 ± 0.1) (Figure 2B, Figure 2—figure supplement 1). ITC of geraniol with HBc showed a slightly enhanced micromolar affinity (KD = 94 ± 8 µM) (Figure 2A and B, Supplementary file 1, Supplementary file 2 and Figure 2—figure supplement 1) and a stoichiometry of N = 1.01 ± 0.04, implying that all four hydrophobic pockets of the asymmetric unit are occupied simultaneously. To confirm geraniol’s binding to the capsids and resolve the molecular details of this interaction, we conducted cryo-EM of a mixture of HBc with excess of geraniol followed by single-particle analysis. This experiment resolved an additional density for geraniol in all four hydrophobic pockets within the asymmetric unit of HBc capsids (Figure 2D, Figure 2—figure supplement 2), confirming the thermodynamic binding data and further defining the underlying molecular interactions of the involved HBV residues P5, L60, K96, and F97.

![Figure 2.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig2-v1.jpg)

**Figure 2.:** (A) Structures of different substances used for the isothermal calorimetric titration (ITC) and cryo-EM experiments. N-Decyl-beta-d-maltopyranoside (DM) (1) and geraniol (2). Using geranic acid, we synthesized geranyl dimer (3), a dimeric binder forked by a lysine and having a linker of six dioxaoctanoic units. (B) Representative ITC heat signatures of DM (1), geraniol (2), and the geranyl dimer (3) with HBc capsids. Heat release is detected upon titration of the ligands to the HBc solution, indicating stoichiometric binding interaction. 4 mM geraniol (2) was titrated into a solution of 210 µM HBc. A solution of 2 mM geranyl dimer (3) was titrated into a solution 200 µM HBc. 1.6–2 mM solutions of DM (1) were titrated into solutions with 90, 100, and 150 µM HBc, respectively. The control experiments where geraniol, geranyl dimer, and DM were titrated into buffer are shown in Figure 2—figure supplement 1. Integrated heat signatures in kcal⋅mol–1 plotted against the molar ratio of titrants to HBc. Binding isotherms (solid lines) were determined using a curve fitting procedure based on a one-site model. Among the ligands, the geranyl dimer has the strongest affinity to HBc, expectedly surpassing the monovalent geraniol by twofold. (C) Structure of the geraniol (magenta) within the HBc binding site (yellow and red) together with close-up view of the binding site with the EM-densities. Geraniol and residues (P5, L60, K96, E64, and V13) involved in hepatitis B virus’s (HBV) envelopment with natural phenotypes are depicted in stick representation. The EM density of geraniol is shown in the zoom-out in blue. (D) Side-by-side comparison of the overlapping HBc geraniol and TX100 (Makbul et al., 2021b) binding sites suggests conformational flexibility and the ability of the hydrophobic pocket to accommodate larger hydrophobic molecules.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** All substances were dissolved in buffer A and titrated into buffer A as a control for experiments where equal concentrations of these substances were titrated into solutions of HBc (see Figures 2 and 3). (A) 4 mM geraniol, (B) 2 mM geranyl dimer, (C) 1.7 mM DM, (D) 0.3 mM P1d, (E) 0.5 mM P2d, and (F) 1.5 mM SLLGRM dimer. X and Y axes are scaled differently in the panels.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Slice of the EM-map with fitted model: The slice shows the center of the two quasi-equivalent spikes with the fitted models of geraniol in brown. One geraniol molecule is bound to each of the quasi-equivalent sites. The surface of the EM-map is transparent and colored according to the chains. For clarity, the density attributed to geraniol is highlighted in green (color blob option of Chimera; Pettersen et al., 2004). Geraniol binds to the same site as Triton X100 (Makbul et al., 2021b) but does not change the rotamer conformation of F97. Binding of geraniol is not linked to conformational changes in the HBc-dimers. (B) Slices of the EM-map at the center of the spikes shown above. The surface of the map is colored according to the relative occupancy estimated with ‘OccuPy’ (Forsberg et al., 2023) based on the gray value distribution. The relative occupancies at the geraniol moiety are somewhat lower than the surrounding protein. Considering that flexibility and occupancy have a similar effect on the gray value distribution, the geraniol has an increasing flexibility towards the outside of the pocket and has at least 80–90% occupancy at the interior of the pockets. The color key for the relative occupancy is shown below.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** This figure illustrates the rationale behind the design of the PEG linker length in the peptide- and geraniol-dimers. The binding site A, where the peptide or geranyl dimer binds, is located at the tip of a capsid spike or in a hydrophobic pocket (depicted as a yellow circle). The possible additional interactions of the dimers are shown as yellow circles labeled B1, B2, B3, and B4. The PEG linker, depicted as a dotted blue line, has been carefully chosen to allow simultaneous binding between two opposing sites. (I) The distance between the tip of a ‘central’ capsid spike A and the surrounding four spikes B1, B2, B3, and B4 is approximately 6 nm (60 Å). The PEG linker, with a length of about 8 nm (80 Å), was selected to provide flexibility and ensure the dimer can potentially bridge two adjacent spike tips, optimizing binding avidity by enabling interaction with any combination of the adjacent spikes. (II) For geranyl dimers, the hydrophobic pockets are separated by a distance of approximately 4 nm (40 Å), and the designed PEG linker (~3.8 nm or 38 Å) was chosen to match this distance, allowing for optimal interaction with two pockets in close proximity.

Encouraged by structural confirmation of geraniol binding to the central hydrophobic pocket, we designed and synthesized a dimeric version of geraniol potentially capable of simultaneous binding to the HBc dimer. We connected the two geranyl moieties with a polyethylene glycol (PEG) linker that could bridge the distance of 38 Å between the two opposing hydrophobic pockets (see Figure 2—figure supplement 3 for the design rationale). After synthesis, purification and mass spectrometric validation (Appendix 1) we determined the HBc capsid binding parameters of the geranyl dimer via ITC. The analysis suggested that the dimer engages with both HBc binding sites simultaneously, resulting, however, only in a moderately enhanced micromolar affinity of 63 ± 8 µM (Figure 2B).

### Targeting the pocket of capsid spike tips with sub-micromolar affinity peptide dimers

Although geraniol and geranyl dimer displayed improved affinity to HBc and allowed structural insights on a binding pocket located at the center of HBc dimers, micromolar affinity is suboptimal for a functional compound. Therefore, we proceeded to explore another binding site located on the capsid spike tips formed by HBc dimers (Figure 1; Böttcher et al., 1998).

Earlier studies have shown that phage display-derived peptides were binding to the spike tips of recombinant HBc capsids. These peptides were also observed to disrupt the interaction between HBc and HBV’s surface protein, L-HBs (Wang et al., 1995). Recently, we have shown that these peptides MHRSLLGRMKGA (P1), GSLLGRMKGA (P2), and the core binding motif SLLGRM bind to wild-type (wt) and mutant HBc variants (P5T, L60V and F97L) with intermediate micromolar KDs of 26, 68, and 130 µM, respectively (Makbul et al., 2021a).

Here, we designed dimeric peptides with a PEG linker capable of bridging the distance of 50 Å between the capsid spikes, thus tailoring our binders for simultaneous binding of two HBc dimers (Figure 1B, Figure 2—figure supplement 3). The three distinct dimeric peptides, the minimal SLLGRM dimer (4), the P2 dimer (P2d) (5), and two P1 dimers (P1d) (6) and P1dC (7), were synthesized, purified, and validated using mass spectrometry (Appendix 1). Subsequently, their binding to the HBV capsid was evaluated through ITC (Figure 3A, Supplementary file 2, Figure 2—figure supplement 1, Figure 3—figure supplement 1). With a KD value of 4.9 ± 0.7 µM, the SLLGRM-dimer (4) has the lowest affinity to HBc, followed by the P2-dimer (5) (KD = 1.9 ± 0.4 µM). Finally, the P1-dimers (6) and (7) displayed sub-micromolar affinities of 312 nM and 420 nM. Thus, P1-, P2-, and SLLGRM-dimers show 83-, 36-, and 27-fold increased affinities compared to their monomeric counterparts.

![Figure 3.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig3-v1.jpg)

**Figure 3.:** (A) Chemical structures of the dimeric peptides, all contain the core binding sequence -SLLGRM and share the same PEG linker and a lysine as the branching element of the dimer. (B) Exemplary isothermal calorimetric titration (ITC) thermograms showing the titration heat signature of HBc with dimers. A solution of 1500 µM (4) was titrated into a solution 150 µM HBc. A solution of 125 µM (5) was titrated into a solution 25 µM HBc. A solution of 200 µM (6) was titrated into a solution 25 µM HBc. A solution of 100 µM (7) was titrated into a solution 25 µM HBc. (C) The peptide dimers display low micromolar to sub-micromolar affinity to HBc, the affinity increases with the elongation of the binding sequence. (D) Sequence requirements of the HBc Spike binding site. Full positional scan of the P1 peptide sequence in microarray format, in which each residue was varied to each other proteogenic amino acid. Note that a drop in binding intensity upon variation of the core motif SLLGRM (highlighted in bold) substantiates its critical involvement in HBc binding. Refer to Supplementary file 3 for the corresponding absolute grayscale values. Affinity gains observed for exchanging positively charged for negatively charged amino acids may be assay-specific false-positives as highlighted previously (Makbul et al., 2021a).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) 0.1 mM solution of the scrP1dC-dimer (scrambled version of the P1dC-dimer) was titrated into a solution of 0.025 mM HBc. (B, C) 0.1 mM solutions of scrP1dC-dimer and P1dC-dimer were titrated into buffer A as additional controls. In all cases no heat change was examined, validating the lack of HBc–scrambled peptide interaction and excluding residual binding interactions from the handle or linker. (D) Heat fluctuations from Figure 3B on identical y-axis scaling.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The asymmetric unit of HBc capsids (T = 4) consists of a tetramer which is composed of the A/B (closest to the fivefold symmetry axes in the icosahedron) (in blue) and the C/D-dimer (closest to the threefold symmetry axes) (in red). The peptide moiety of the dimers is depicted as yellow filled circles connected by a flexible PEG linker symbolized as a dotted line. Peptide dimers interact with the asymmetric unit in four different states (S1, S2, S3, and S4). The concentration of every state is dictated by the energetics of the respective state and the concentration of the peptide-dimer. At low concentrations, S1 and the possible degenerative permutations could be expected to be favored and at high concentrations S4. For the sake of simplicity, only a single (abstract) asymmetric unit is depicted here, which represents capsid with 60 asymmetric units.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Assessment of turbidity of capsid solutions induced by peptide dimers. The optical densities (OD) of HBc solutions (10 or 50 µM) with and increasing peptide-dimer concentrations were measured at a wavelength of 350 nm and plotted against peptide-dimer concentrations. All peptides showed increased turbidity with increasing concentrations, with P1 (7) and P2 (5) dimers inducing turbidity at low micromolar concentrations, while the SLLGRM dimer (4) induced turbidity at high micromolar concentrations.

The significant increase in affinity of the P1-dimer over the monomer, by almost two orders of magnitude, may not be solely attributed to binding to two sites simultaneously. Once the P1-dimer binds, it can interact with up to four binding partners in its vicinity (Figure 3—figure supplement 2; Wynne et al., 1999). This may enable detachment and immediate reattachment to a nearby binding partner, further enhancing the local concentration and the overall binding strength of the P1 dimer.

Notably, while performing the ITC titrations we have noticed fast fluctuations of the heat signature baseline across the tested ligands (Figure 3, Figure 3—figure supplement 1), at least for the P1 dimer this phenomenon may be attributed to aggregation. To rule out any non-specific interactions caused by the PEG linker or handle for both the geranyl dimers as well as the P1/2 dimers, a scrambled dimeric peptide was used as a negative control. This scrambled peptide showed no detectable binding (Figure 3C), thereby confirming that the observed binding is specific to the designed peptide sequence and not influenced by the linker or other structural components.

To further substantiate and quantify a possible dimer-induced HBc aggregation, we next performed a turbidity assay (Zhao et al., 2016). We found that P1 dimer induces turbidity of a HBc solution already at 1:10 equivalents of HBc, whereas the P2 dimer was slightly less potent and the SLLGRM dimer did not induce turbidity at the same conditions and further required significantly higher concentrations ratio relative to HBc (Figure 3—figure supplement 3). To shed light on the seemingly sequence-specific aggregation properties of the different dimers, we analyzed the binding of 240-point mutated P1 peptide variants in array format (Figure 3D, Supplementary file 3). The analysis recapitulated our earlier resolved sequence requirement for HBc binding and substantiated that the minimal sequence SLLGRM is the major mediator of HBc binding. Importantly, it further indicates that the additional N-terminal residues in P1 sequence are neither conserved nor critically required for binding despite their importance in inducing HBc aggregation.

### P1dC aggregates HBc in living HEK293 cells

The sub-micromolar affinity of the P1-dimer, along with its ability to induce capsid aggregation in vitro, prompted us to evaluate its effect on HBV core protein in living cells. To adapt the peptide for the intracellular delivery, we synthesized a C-terminally cysteinated version of P1-dimer, P1dC (7) (Figure 3A), and its scrambled counterpart scrP1dC scr(7), as well as a thiol-reactive polyarginine-based cell penetrating peptide (CPP), containing a cysteine, with a 5-thio-2-nitrobenzoic acid (TNB)-modified thiol (Figure 4A, Appendix 1). At the core of this intracellular delivery method is the in situ conjugation of the cargo molecule to a molar excess of a CPP via a disulfide bond, and the application of this reaction mix on living cells. The excess of the CPP over the active compound enable the reaction of CPP-thiols with the cellular surface, facilitating the penetration of the cargo-CPP conjugate. In turn, the disulfide bond between CPP and the cargo is reduced in the cytosol, separating the cargo from the CPP, allowing unhindered activity of the cargo molecule within the cell (Figure 4B; Schneider et al., 2021a; Schneider et al., 2021b).

![Figure 4.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig4-v1.jpg)

**Figure 4.:** (A) A polyarginine cell-penetrating peptide containing a cysteine with a TNB-activated thiol (gray highlight (8)). (B) The live cell experiment flow. First, mammalian cells are transfected with HBc coding plasmid. Then, after the cells express the protein, a mix of (8) and (7) is applied. The excess CPP facilitates membrane permeation, allowing (7) to enter the cell after a brief incubation. Once inside, (7) is separated from the CPP and can interact with the capsids. (C) After 1 hour incubation with (7) or scr(7), the cells were immediately washed, fixed, and labeled with anti HBc mAb16988 and a secondary DyLight650 conjugated antibody. The cells were visualized on wide-field fluorescent microscope with identical conditions and are presented with the same grayscale range. Transfected and untreated cells display diffuse HBc distribution, with clear fluorescence at the nucleus. Transfected cells treated with (7) display bright aggregates, whereas transfected cells treated with scr(7) have similar diffuse labeling as the untreated cells. Non-transfected cells are non-fluorescent. Scale bar 20 µm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Live HEK293 cells expressing HBc were treated with either P1dC or with the scrambled (scr) P1dC analogue together with the cell penetrating peptide. After treatment, the live cells were fixed and labeled with HBc antibody and a secondary DyLight650 conjugated antibody (1:500). The imaging showed HBc aggregates in P1dC treated cells (A), while scrP1dC-treated cells showed little to none aggregates (B). All images shown with identical grayscale range. Scale bar 10 μm.

To verify that the P1dC performs similarly to P1-dimer,, we performed another ITC assay to determine the affinity of the compound to HBc. The ITC confirmed that P1dC has an affinity of 420 ± 38 nM, comparable to P1-dimer, while the scrambled peptide did not display binding to HBc (Figure 3, Figure 3—figure supplement 1, Supplementary file 2). Thereafter we transfected mammalian cells (HEK293) with a plasmid coding for HBc. The cells expressed the protein for 2 days and were then treated for 1 hour with the thiol-activated cell penetrating peptide and P1dC or the respective negative control peptide scrP1dC (Figure 4B). Afterward, the cells were immediately washed and fixed and HBc was visualized with anti-HBc antibody and a secondary DyLight650 conjugated antibody. Transfected but otherwise untreated cells showed a homogeneous distribution of recombinant HBc molecules in the nucleus and to a lesser extent in the cytoplasm (Figure 4C). Yet, upon administration of 10 µM of P1dC (7), we observed aggregates of HBc (in the form of large bright spots) within the cells (Figure 4C, Figure 4—figure supplement 1). At a concentration of 10 µM, the scrambled dimer scrP1dC did not induce aggregation and the distribution of HBc remained largely homogenous.

Our live cell experiments have corroborated our in vitro findings, providing us a visual proof of P1dC-mediated HBc aggregation in a living cell. Thus, the peptide dimer causes an aggregation that resembles the HAP induced aggregation of the core protein and, like CAMs, can be expected to have the potential to disrupt the HBV life cycle.

### Cryo-EM confirms peptide-induced HBc aggregation

To affirm the capsid-aggregation property of our peptide dimers, we incubated solubilized purified capsid-like particles (CLPs, spherical capsid-like HBc multimers purified from Escherichia coli) with an excess of SLLGRM-dimer or P1dC, applied them on carbon grids, and imaged them using cryo-EM. The effect of peptide dimers on CLPs was already seen on the microscale cryo-EM images (Figure 5—figure supplements 1 and 2), with P1dC inducing large protein aggregates with multimicron diameter. The less potent SLLGRM-dimer also induced visible aggregation, although with smaller aggregate size, while geraniol-treated samples showed minimal aggregation, and the smallest observed aggregate sizes. In the nanoscale, we observed clumped CLPs (Figure 5—figure supplement 3) and resolved the binding of both peptide dimers to the spike tips (Figure 5, Figure 5—figure supplement 3). The densities corresponding to bound peptide-dimers in both EM-reconstructions have volumes, which can accommodate a peptide chain of approximately six amino acid residues (Figure 5, Figure 5—figure supplement 3).

![Figure 5.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig5-v1.jpg)

**Figure 5.:** Close-up of the surface representation of the EM-maps of capsid-like particle (CLP) incubated with geraniol (2), with SLLGRM-dimer (4) and P1dC (7). (A) The surface of the map is colored according to the local resolution. The map of (7) has a lower overall resolution, which is consistent with the lower number of particles in the reconstruction (Supplementary file 4). In all three maps the tips of the spikes are less well resolved than the capsid shell regardless of whether peptides are bound or not. This is in line with the general flexibility of the protruding spikes in HBc-CLPs (Böttcher et al., 1998; Hadden et al., 2018). (B) The surface of the maps is colored according to the relative occupancy based on the gray value distribution as determined with OccuPy (Forsberg et al., 2023). Low relative occupancy cannot be distinguished from local flexibility. As the tips of the spike are flexible, they show generally lower occupancy than the protein shell. Comparing the relative occupancies in samples incubated with (4) and (7) suggests a lower occupancy with (4) than with (7). (C) Fit between the model and the map (gray, translucent) at the tips of spikes. Binding of an (4) or of (7) splays the helices at the tips apart similar as previously reported for binding of a P2-monomer (Makbul et al., 2021a). (4) binds to both quasi equivalent sites in contrast to SLLGRM-monomers, which binds only to the CD-dimer and does not show such a prominent splaying (Makbul et al., 2021a). Geraniol binds at the center of the spikes and does not change the conformation at the tips of the spikes.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) CLPs with bound geraniol, (B) HBc-CLPs with bound SLLGRM-dimer, and (C) HBC-CLPs with bound P1dC. (a) shows a representative micrograph. All micrographs are shown at the same scale; (b) shows the 2D-class averages of the five most populated classes after automated template picking. All class averages are shown at the same scale; (c) shows a close-up of the surface representation of the final map after post-processing with relion (filtered by Fourier shell correlation [FSC], B-factor sharpened). One unit cell is colored according to the density covered by the model (HBc chains A, B, C, D in blue, cyan, yellow, and red respectively) and binders (geraniol, SLLGM-dimer and P1dC in green); (d) FSC plot of the final map. FSC = 0.143 is marked by a thin, solid line. Green curve: FSC between unmasked half-maps; blue curve: FSC between masked half-maps; red curve: FSC between phase-randomized masked half-maps; black curve: FSC corrected for the contribution of the mask.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Low-magnification cryo-EM images of CLPs + P1 dC (7) (A), (B) CLPs + SLLGRM-dimer (4), and (C) CLPs + geraniol (2). The micrographs are part of the grid-atlas of the respective data acquisition. Each image shows four meshes of the respective grid atlas at a similar ice thickness. For representation, the images were aligned to show a similar orientation of the meshes. CLP aggregates are seen as dark speckles (yellow arrow). The size of the aggregates is largest in P1dC-treated samples, while aggregates are frequent and smaller in samples treated with SLLGRM-dimer. Geraniol treated samples have very few aggregates, which are generally smaller than 1 µm.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/98827/elife-98827-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** HBc capsids with bound SLLGRM-dimer (4) or P1dC-dimer (7) imaged by electron cryo-microscopy. (A) and (B) show selected areas of micrographs of CLPs treated with (4) or with (7). One exemplary aggregate of multiple HBc capsids is indicated by an arrow in each micrograph. (C) and (D) show close-ups of the asymmetric unit of HBc capsids with bound SLLGRM dimers or with bound P1dC. Models of a single asymmetric unit consisting of two HBc dimers are fitted into the asymmetric unit. Both maps show a density at the tips of the spikes (arrow) that accounts for approximately six amino acids of the peptide-dimer. The flexible linker between the peptides was not resolved. The position of the symmetry axes of the icosahedral capsid is labeled with numbers in (C).

The asymmetric unit of HBc capsids (T = 4) is a tetramer consisting of an A/B- and C/D-dimer, which have slightly different 3D structures. Interestingly, the SLLGRM-dimer binds the A/B-dimer as well as the C/D-dimer, in contrast to the monomeric SLLGRM, which binds only to the tip of the C/D-dimer (Makbul et al., 2021a; Figure 5), in line with the multivalent binding and the higher affinity we measured with ITC. A possible mode of action of the peptide-dimer-induced aggregation is shown in Figure 1B.

The live cell experiments showed the formation of HBc aggregates upon incubation with P1dC. Yet, in live cells HBc may exist as a monomer, a dimer, a multimer, or a whole capsid; therefore, the observed aggregates were not necessarily formed by whole capsids. The cryo-EM experiment, however, provides confirmation that the peptide dimers have the capability to interact with complete CLPs, an important feature, which implies that the dimers have the potential to affect intact capsids upon cell infection.

## Discussion

In this study, we focused on the HBV core protein, a protein essential for HBV proliferation and virulence. We explored the druggability of two alternative, non-HAP, binding pockets on the HBc ultrastructure and developed synthetic dimers that target these pockets with sub-micromolar affinity, resulting in the aggregation of HBc.

DM and geraniol were selected as the water-soluble mimetics of the natural post-translational modifications of HBV/HDV components. We have demonstrated their ability to interact with the vital central hydrophobic pocket of HBV and showed a binding affinity improvement upon dimerization of the geraniol ligand. Higher affinity ligands may be developed into even more potent binders of the hydrophobic pocket using the outlined linker design, potentially exerting a pharmacological effect on HBV (Briday et al., 2022).

Earlier works demonstrated that point mutations within the HBc can significantly affect HBV infectivity, particularly through disruptions in HBc interactions (Yuan et al., 1999b; Bruss, 2007; Ponsel and Bruss, 2003; Koschel et al., 1999). These mutations at the base of the spike and the groove between spikes highlight the importance of these regions in viral replication. Using our structural knowledge of the capsid, particularly the distances between the spikes, we designed peptide dimers with the ability to simultaneously bind to neighboring spikes on the same capsid or attach to two distinct capsids (Figure 3—figure supplement 2). Our in vitro assays demonstrated that these peptide dimers display a robust affinity ranging from low micromolar to sub-micromolar levels (Figure 3 and Supplementary file 2). Specifically, the peptide dimer (P1dC) with sub-micromolar affinity (KD = 420 ± 40 nM) is a promising candidate for a lead molecule for new a new class of CAMs. The peptide dimer, but not its scrambled dimeric counterpart, induced HBc aggregation in live mammalian cells expressing HBc. An effect resembling the aggregation was observed after a treatment with the classical CAM HAP (Wu et al., 2013).

An intriguing possibility would be that the spike and hydrophobic pocket interact or influence each other when binding different ligands. Molecular dynamics simulations reveal notable flexibility in HBV capsids, suggesting that structural asymmetry might impact ligand binding. Structural analysis of the HBV capsid shows that P2 peptide binding to the capsid spikes increases flexibility, while exerting a minimal impact on the underlying hydrophobic pocket. However, TX100 binding within the hydrophobic pocket influences the spike tips by flipping Phe97, whereas geraniols bound within the same pocket do not induce this change, indicating that this interaction is ligand-specific. Nevertheless, simultaneous application of spike binders and hydrophobic pocket ligands that modify spike conformation may offer valuable structural and functional insights into HBV capsids.

An intriguing possibility would be that the spike and the hydrophobic pocket could interact or exert an effect on each other upon binding various ligands. Molecular dynamics simulations revealed significant flexibility of the HBV capsids and suggested that structural asymmetry may affect ligand binding (Pavlova et al., 2018; Perilla et al., 2016; Pavlova et al., 2022). HBV capsid structural analysis showed that P2 peptide binding to the capsid spikes increases flexibility (Makbul et al., 2021a) while exerting a minimal impact on the hydrophobic pocket beneath. However, TX100 binding to the hydrophobic pocket affected the spike tips by flipping Phe97 (Makbul et al., 2021b) in the pocket, but the geraniols resolved within the hydrophobic pocket did not flip Phe97, thus suggesting that this cross-talk is ligand-specific. Nevertheless, a simultaneous application of spike binders and hydrophobic pocket ligands able to affect the spike conformation may provide valuable structural and functional insights into HBV capsids.

While our results are highly encouraging, application in complex organisms may require alternative delivery methods, investigation of HBV proliferation in infection models, and further study of immunogenicity and stability. Future studies should thoroughly assess the cytotoxic potential of peptide-induced HBc aggregation to determine any adverse effects at the cellular level, which will be crucial for evaluating the therapeutic potential of these compounds. Long-term cytotoxicity studies on cellular viability are essential to optimize these binders for clinical applications. Although our study targets two ligand-binding pockets on the capsid surface, a direct effect on HBV infectivity remains to be demonstrated. Prior mutational data, however, suggest that even minor perturbations, such as ligand binding, could mimic deleterious mutations and impair viral function. This study’s insights into the unexplored pharmacological potential of these binding pockets and the compounds targeting them may lead to the development of new agents that impact viral capsids. Unlike classical CAMs, the peptide dimers exhibit a different mechanism of action and may act synergistically with CAMs or other antivirals. Further biological investigations will clarify the antiviral potential, applicability, and potency of compounds targeting the non-HAP binding pockets.

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
      <td>Gene (hepatitis B virus genome)</td>
      <td>CLP coding region; complement (733.1371)</td>
      <td>GenBank: V01460.1</td>
      <td></td>
      <td>Genotype D; strain ayw</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK293</td>
      <td>DSMZ</td>
      <td>Cat# ACC 305RRID:VCL_0045</td>
      <td>Epithelial morphology; embryo kidney</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>pEGFP-C2</td>
      <td>Clontech</td>
      <td></td>
      <td>Donor vector for CLP expression</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-Hepatitis B Virus Antibody; core Antigen; clone C1-5, monoclonal; a.a. 74–89</td>
      <td>MilliporeSigma</td>
      <td>Cat# MAB16988RRID:AB_11212378</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-Mouse IgG (H+L), polyclonal</td>
      <td>Invitrogen</td>
      <td>Cat# 84545RRID:AB_2633280</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>n-Decyl-β-D-maltopyranoside (DM)</td>
      <td>Anatrace</td>
      <td>Cat# D310</td>
      <td>Used in binding assays.</td>
    </tr>
    <tr>
      <td>Software algorithm</td>
      <td>Relion 3.1. and 4.0</td>
      <td>https://github.com/3dem/relion; Scheres, 2012a; Scheres, 2012b</td>
      <td></td>
      <td>Image processing</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cryosparc 4.0</td>
      <td>https://Cryosparc.com/</td>
      <td></td>
      <td>Image processing</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCorr2</td>
      <td>Zheng et al., 2017</td>
      <td></td>
      <td>Movie processing</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix</td>
      <td>https://phenix-online.org/</td>
      <td></td>
      <td>Model building</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/binaries/</td>
      <td></td>
      <td>Model building</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Chimera</td>
      <td>https://www.rbvi.ucsf.edu/chimera</td>
      <td></td>
      <td>Preparation of figures from pdb models and EM-maps</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MicroCal ITC200 Analysis</td>
      <td>Malvern Panalytical, Malvern</td>
      <td></td>
      <td>Processing of the ITC dataimplemented in Origin and supplied with the MicroCal iTC200</td>
    </tr>
  </tbody>
</table>

Unless otherwise noted, all resins and reagents were purchased from IRIS biotechnologies or Carl Roth and used without further purification. All solvents were HPLC grade. All water-sensitive reactions were performed in anhydrous solvents under positive pressure of argon.

### Peptide synthesis

The peptides were produced using standard solid-phase peptide synthesis with Fmoc chemistry. Shortly, 2-chlorotrityl resin (1.6 mmol/g) was swollen in dry dichloromethane (DCM) for 30 minutes, then, the desired amino acid (AA) (1eq) and the Boc-Gly-OH (1eq) with 4 eq. of dry N,N-diisopropylethylamine (DIEA) were added to the resin slurry. After overnight (ON) reaction at room temperature (RT) with agitation, the resin was capped with MeOH and washed with DCM and dimethylformamide (DMF). For the synthesis of cysteinated peptides, a 1% divinylbenzene Wang resin, preloaded with a 9-fluorenylmethyloxycarbonyl-Cysteine(Trityl)-OH [Fmoc-Cys(Trt)-OH] (0.4 mmol/g), was swollen in DMF for 30 minutes. Then, regardless of the resin type, Fmoc was removed using 20% piperidine in DMF solution and the resin was washed with DMF and DCM. After washes, the peptide chain was elongated by adding the desired amino acid (AA, 3 eq.) with ethylcyanohydroxyiminoacetate (Oxyma, 3 eq.) and N,N'-diisopropylcarbodiimide (DIC, 3 eq.). Capping was done with DIEA (50 eq.) and acetic anhydride (50 eq.) in N-methyl-2-pyrrolidone for 30 minutes. Coupling efficiency was monitored by measuring the absorption of the dibenzofulvene–piperidine adduct after deprotection. The peptide chain was elongated with further identical deprotection-conjugation cycles and after the completion the peptides were cleaved from the resin using a cocktail of 94% trifluoracetic acid (TFA), 3% H2O, 3% triisopropylsilane (TIPS), for 4 hours at RT. The peptides were precipitated in ice-cold ether and then purified with semi-preparative HPLC and analyzed by LC-MS, as described below.

### Geranyl-dimer synthesis

2-Chlorotrityl resin (1.6 mmol/g) was swollen in dry DCM for 30 minutes. Then, 4 equivalents of Fmoc-Lys(Fmoc)-OH and 8 equivalents of dry DIEA were added to the resin slurry. The reaction was carried out ON at RT with agitation. After completion, the resin was capped with MeOH and washed with DCM and DMF. Fmoc deprotection was performed using a 20% piperidine solution in DMF, followed by thorough washing with DMF and DCM. The linker chain was then elongated by coupling 8-(9-fluorenylmethyloxycarbonyl-amino)–3,6-dioxaoctanoic acid (Fmoc-O2Oc-OH, 6 eq.) with Oxyma (6 eq.) and DIC (6 eq.). Capping was performed using 50 equivalents of DIEA and acetic anhydride in N-methyl-2-pyrrolidone for 30 minutes. Coupling efficiency was monitored by measuring the absorption of the dibenzofulvene–piperidine adduct after deprotection. The linker chain was further extended through two additional deprotection-conjugation cycles with Fmoc-O2Oc-OH. Subsequently, conjugation with geranic acid was carried out under similar conditions. The resulting dimer was cleaved from the resin using a 20% hexafluoroisopropanol solution in DCM. The solvents were removed via rotary evaporation, and the compound was purified using semi-preparative HPLC and analyzed by LC-MS, as described below.

### 5-(thio)-2-nitrobenzoate conjugation to the thiolated cell penetrating peptide (CPP)

A 10-mer oligoarginine peptide connected to a cysteine (C-RRRRRRRRRR) was reacted with 10 equivalents of 5,5-dithio-bis-(2-nitrobenzoic acid) in 1:1 DMF: 0.1 M phosphate buffer for 30 minutes with agitation at RT. Then the reaction mixture was directly injected in semi-preparative HPLC, purified, and analyzed by LC-MS, as described below.

### Purification and characterization of peptide-based probes

The compounds were purified from the crude reaction mix by reverse-phase HPLC using a water acetonitrile gradient with 0.1% formic acid (FA). Semi-preparative HPLC was performed on Shimadzu Prominence equipped with a diode-array detector (DAD) system using a C18 reverse-phase column (Phenomenex Onyx Monolithic HD-C18 100×4.6 mm or Onyx Monolithic C18 100×10 mm). Purity and structural identity were verified using a DAD equipped 1260 Infinity II HPLC with a C18 reverse-phase column (Onyx Monolithic C18 50×2 mm), coupled to a mass selective detector single quadruple system (Agilent Technologies). Compounds analyzed in ESI+ mode were run in a water-acetonitrile gradient with 0.1% FA. Compounds analyzed in ESI- mode were run in a 10 mM pH = 7 ammonium bicarbonate – acetonitrile gradient.

### Protein expression and purification HBc CLPs

The expression and purification of CLPs were done as previously described (Makbul et al., 2021b). Shortly, the recombinant HBV core protein (HBc) was overexpressed in E. coli (BL-21) and formed CLPs. CLPs were purified by fractionated ammonium sulfate precipitation followed by sucrose density gradient centrifugation. The major capsid type (ca. 95%) was formed by 240 subunits (Triangulation: T = 4).

### Isothermal titration calorimetry (ITC)

Samples (ca. 8 mL) of purified capsids were filtered (Rotilabo syringe filter with a pore size of 220 nm, Carl Roth GmbH Co. KG, Karlsruhe, Germany), dialyzed against 1.4 L buffer A (40 mM HEPES, 200 mM NaCl, 1 mM MgCl2, 1 mM CaCl2, pH 7.5) using a dialysis membrane tube (Spectra Por Biotech cellulose ester tube, 1 MDa MWCO, Spectrum Laboratories, Inc, Rancho Dominguez, CA, USA). The dialysis was performed at 4°C under gentle stirring for 16 hours ON. The next day, the dialyzed sample was removed from the dialysis tube and concentrated in a centrifuge using a concentrator (30 kDa MWCO Spin-X UF 6 mL, Corning Inc, Corning, NY, USA). The concentrate was filtered (centrifugal filter unit Ultrafree MC, pore size of 100 nm, Merck KGaA, Darmstadt, Germany) and the concentration determined by the Bradford assay (Roti Nanoquant, Carl Roth GmbH Co. KG).

The peptide dimers were dissolved in the buffer from the dialysis of the capsids. In this buffer, SLLGRM dimer and P2 dimer have solubilities of at >8 mM and the P1 dimer of >2 mM. 4 mM geraniol was titrated into a solution of 210 µM HBc.

A solution of 2 mM geranyl dimer was titrated into a solution 200 µM HBc. 1.6–2 mM solutions of DM were titrated into solutions with 90, 100, and 150 µM HBc, respectively.

Before filling the ITC cell and syringe, all samples were degassed for 10 minutes at 20°C (ThermoVac, Malvern Panalytical, Malvern, Worcestershire, UK). Solutions of peptide dimers were titrated into solutions of capsids using a MicroCal iTC200 instrument (Malvern Panalytical) according to the specifications in Supplementary file 1. The resulting thermograms and isotherms were processed and fitted using the Origin software supplied with the iTC200 instrument. The thermograms were integrated and the corresponding isotherms were fitted using a one-site model. The peptide and geranyl dimers are bivalent and have 120 or 240 potential binding sites on CLPs, respectively. The two binding sites of peptide and geranyl dimers are not identical but very similar. This also true for the binding sites on capsids, so the binding energetics of the dimers are very similar and are best represented by a one-site model. All obtained thermodynamic parameters refer to concentrations of monomeric HBc. All ITC experiments were complemented with control experiments where solutions of peptide dimers were titrated into the dialysis buffer.

### Turbidity assay

All peptides were dissolved in buffer A (40 mM HEPES, 200 mM NaCl, 1 mM MgCl2, 1 mM CaCl2, pH 7.5) and the capsid solutions were filtered once (centrifugal filter unit Ultrafree MC, pore size of 100 nm, Merck KGaA). The concentrations of the P1, P2, and SLLGRM dimers were varied between 0.1 and 100 µM, and the concentration of HBc was kept constant at 10 µM for the P1 and P2 dimer and at 50 µM for the SLLGRM dimer. All experiments were performed using a standard photometer (GENESYS UV/VIS spectral photometer, Thermo Fisher Scientific, Hillsboro, OR, USA) at RT and at a wavelength of 350 nm using disposable UV transparent cuvettes (SARSTEDT AG & Co. KG, Sarstedtstraße 1, 51588 Nümbrecht/Germany).

### Cryogenic grid preparation of capsids in complex with peptide-dimers

In a plasma cleaner (model PDC-002. Harrick Plasma, Ithaca, NY, USA) holey carbon grids (R1.2/1.3, 300 mesh Cu grids, Quantifoil Micro Tools, Jena, Germany) were made hydrophilic by plasma cleaning. This was done at a pressure of 29 Pa for 2 minutes using ambient air as plasma medium at ‘medium power’ of the instrument. Solutions of purified HBc (200 µM) in complex with the P1dC- and the SLLGRM-dimer (each 400 µM) were prepared in buffer A. After the end of ITC experiment with geraniol and HBc (Figure 2), a sample from the cell of the ITC instrument was retrieved and used for freezing grids. 3.5 µL aliquots of each sample were applied onto the grids. For plunge freezing of grids, ethane was used as medium (liquefied by liquid nitrogen) with the help of a Vitrobot (mark IV, FEI Company, Hillsboro, OR, USA) using Whatman filter papers (type 541). The Vitrobot had the following settings: no wait and drain times, 6 s of blot time, blot force of 25 and a nominal humidity of 100%. The frozen grids were stored in liquid nitrogen for at least one night before being used for image acquisition.

### Cryo-EM and image processing

Cryo-EM was done as previously described (Makbul et al., 2021b). Shortly, movies were acquired with the software EPU on a Krios G3 electron microscope equipped with a Falcon III camera (Thermo Fisher Scientific) in integrating mode at a magnification of 75,000 with an accelerating voltage of 300 kV. The total exposure was 40 e−/Å² and was fractionated over 20 fractions. For HBc CLPs with bound P1dC, three movies were acquired per hole and one hole was acquired per stage position. For HBc CLPs with bound SLLGRM dimers or bound geraniol, at each stage position three movies were acquired per hole from the central hole and from the four closest neighboring holes. The different movie positions at the same stage position were centered with image shift. Movies were motion corrected, exposure weighted, and averaged with MotionCorr2. Figure 5—figure supplement 1A shows representative corrected movie averages, which were imported to Relion for further processing. Each image shift position was treated as a different optics group in the subsequent image processing. Image processing was done with Relion 3.1 or Relion 4. As previously described (Makbul et al., 2021b), imposing icosahedral symmetry. At the end of the image processing with Relion (for CLPs with bound P1dC or SLLGRM-dimers), particle images were imported into CryoSparc 4.02 and were further refined with none uniform refinement (Punjani et al., 2020), including global and local CTF refinement and Ewald’s sphere correction. Final maps were filtered with deepemhancer, or B-factor sharpened (CryoSPARC ‘Sharpen’ or ‘relion_postprocess’). The resolution of the final maps was estimated by Fourier shell correlation (FSC = 0.143; after gold standard refinement) with ‘relion_postprocess’ (Figure 5—figure supplement 1). Parameters of the image acquisition and the processing are summarized in Supplementary file 4.

### Modeling of cryo-EM maps, refinement of PDB files and their validation

For modeling of the EM densities of HBc in complex with the peptide dimers, the PDB file 7od6 (Makbul et al., 2021a) was used as a starting model. This model represents the asymmetric unit of the HBc capsids with T = 4 packing. After slight modifications, the PDB model was fitted into the EM-map as a rigid body and refined iteratively using the software packages Coot (Casañal et al., 2020) and Phenix (Liebschner et al., 2019) and validated with MolProbidity (Prisant et al., 2020). The resolution of the density at the tips of the capsids which we attributed to the binding segments of the peptide dimers was low. Therefore, these densities could only be modeled as poly-alanine chains. All figures showing EM-densities with or without the corresponding PDB models were prepared with Chimera (Yang et al., 2012).

### Cloning

Full-length wild-type (fl wt) HBc (genotype D; strain ayw; GenBank: V01460.1, MQLFHLCLIISCSCPTVQASKLCLGWLWGMDIDPYKEFGATVELSFLPSDFFPSVRDLLDTASALYREALESPEHCSPHHTALRQAILCWGELMTLATWVGVNLEDPASRDLVVSYVNTNMGLKFRQLLWFHISCLTFGRETVIEYLVSFGVWIRTPPAYRPPNAPILSTLPETTVVRRRGRSPRRRTPSPRRRRSQSPRRRRSQSRESQC) (Galibert et al., 1979) was cloned into the pEGFP-C2 vector (Clontech) using Gibson assembly Gibson, 2011 by replacing the gene sequence coding for eGFP. The vector and insert were amplified by PCR and purified by gel extraction (FastGene Gel/PCR Extraction Kit, Nippon Genetics Europe GmbH, Düren, Germany). The purified PCR products were assembled into a single plasmid construct using a home-made Gibson assembly reaction mixture. An aliquot of the reaction product was transformed into XL1 blue cells, plated onto LB-amp agar-plates, and grown at 37°C ON. Six colonies were used for the inoculation of 6 × 5 mL LB-amp medium. The cell cultures were grown under vigorous shaking in an incubator at 37°C ON. The next day, the plasmid DNA was extracted from the cell cultures (FastGene Plasmid Mini Kit, Nippon Genetics Europe GmbH) and sequenced by Sanger sequencing (Microsynth Seqlab GmbH, Göttingen, Germany). A plasmid construct containing the correct gene sequence of HBc was used for endotoxin-free plasmid DNA preparation (NucleoBond Xtra Midi EF, Macherey Nagel GmbH & Co. KG, Düren, Germany).

### HEK293 cell cultures and transfection

HEK293 cells were cultured in DMEM (Gibco), supplemented with GlutaMax and pyruvate (Gibco), 10% fetal bovine serum (FBS) (Gibco) and 1% Penicillin/Streptomycin (Sigma) at 37°C and with 5% CO2. The cells were plated on 0.15-mm-thick 18 mm glass coverslips coated with 35 µg/mL poly-d-lysine in a 12-well plate and were transfected with the cloned 1 µg plasmid DNA per coverslip using polyethylenimine (PEI). The transfection was performed at 60–80% confluence. Shortly before transfection, the medium was changed to fresh DMEM. The DNA was added to 100 µL DMEM without additives and mixed, 4 µL fresh PEI (1 mg/mL) was added, mixed immediately, and incubated for 20 minutes at RT. The transfection mix was pipetted drop-wise on cells while swirling and incubated ON. The medium was changed to fresh DMEM with 2% FBS after 12–24 hours, and on the following day the cells were used for live assays, then fixed and stained.

### Cell assays and immunocytochemistry

Live HEK293 cells expressing HBc were incubated in DMEM with 10 µM P1dC and with 10 µM of the scrambled version of the peptide, both peptides in situ activated with the reactive CPP. After 1 hour incubation at 37°C, the treated and untreated live HEK293 cells expressing HBc and the untransfected HEK293 cells were washed and fixed with 0.1 M sodium phosphate buffer pH 7.4 containing 4% paraformaldehyde (EM grade, Polysciences) and 1% sucrose for 10–20 minutes at 37°C. After three rinses in phosphate-buffered saline (PBS), the cells were permeabilized with 0.1% Triton X-100 in PBS for 10 minutes at RT, rinsed again and blocked for 1 hour in PBS with 3% bovine serum albumin. Then, primary mAb16988 (#6B9780, MilliporeSigma) and secondary DyLight650 (#84545, Invitrogen) antibodies were applied sequentially with 1:500 dilution in blocking solution for 1 hour.

### Wide-field fluorescence microscopy

The coverslips with the cell samples were inserted in an imaging chamber (Ludin Chamber Type 1, Life Imaging Services) and imaged in PBS. The measurements were taken from distinct samples with a sample size ≥2 for each group. A series of images, used to generate the datapoints, were acquired from different regions of the sample, each region having a distinct group of cells.

The samples were imaged on an inverted Leica DMI6000B microscope with a ×100 oil-immersion objective (NA 1.49) using a Leica DFC9000 GTC VSC-05760 sCMOS camera (16-bit, image pixel size: 130 nm). The 628/40 excitation and 692/40 emission filter was used for DyLight650, 10 images were acquired at a frame rate (exposure time) of 100 ms, and constant illumination intensity to ensure comparability (n≥10).

### Automated solid-phase peptide synthesis

μSPOT peptide arrays (Dikmans et al., 2006) were synthesized using a MultiPep RSi robot (CEM GmbH, Kamp-Lindford, Germany) on in-house produced, acid-labile, amino-functionalized, cellulose membrane discs containing 9-fluorenylmethyloxycarbonyl-β-alanine (Fmoc-β-Ala) linkers (average loading: 130 nmol/disc – 4 mm diameter). Synthesis was initiated by Fmoc deprotection using 20% piperidine (pip) in DMF followed by washing with DMF and ethanol (EtOH). Peptide chain elongation was achieved using a coupling solution consisting of preactivated amino acids (aas, 0.5 M) with ethyl 2-cyano-2-(hydroxyimino)acetate (oxyma, 1 M) and DIC (1  M) in DMF (1:1:1, aa:oxyma:DIC). Couplings were carried out for 3 × 30  min, followed by capping (4% acetic anhydride in DMF) and washes with DMF and EtOH. Synthesis was finalized by deprotection with 20% pip in DMF (2 × 4  µL/disc for 10 min each), followed by washing with DMF and EtOH. Dried discs were transferred to 96 deep-well blocks and treated, while shaking, with sidechain deprotection solution, consisting of 90% TFA, 2% DCM, 5% H2O, and 3% TIPS (150  µL/well) for 1.5 hours at RT. Afterward, the deprotection solution was removed, and the discs were solubilized ON at RT, while shaking, using a solvation mixture containing 88.5% TFA, 4% trifluoromethanesulfonic acid (TFMSA), 5% H2O, and 2.5% TIPS (250  µL/well). The resulting peptide-cellulose conjugates (PCCs) were precipitated with ice-cold ether (0.7  mL/well) and spun down at 2000 × g for 10 minutes at 4°C, followed by two additional washes of the formed pellet with ice-cold ether. The resulting pellets were dissolved in DMSO (250 µL/well) to give final stocks. PCC solutions were mixed 2:1 with saline-sodium citrate (SSC) buffer (150 mM NaCl, 15 mM trisodium citrate, pH 7.0) and transferred to a 384-well plate. For transfer of the PCC solutions to white-coated CelluSpot blank slides (76 × 26 mm, Intavis AG), a SlideSpotter (CEM GmbH) was used. After completion of the printing procedure, slides were left to dry ON.

### Peptide microarray-binding assay

The microarray slides were blocked for 60 minutes in 5% (w/v) skimmed milk powder (Carl Roth) PBS (137 mM NaCl, 2.7 mM KCl, 10 mM Na2HPO4, 1.8 mM KH2PO4, pH 7.4). After blocking, the slides were incubated for 15 minutes with 55 nM (monomer equivalent) of HBc in the blocking buffer, then washed 3× with PBS. HBc was detected with a primary 1:2500 diluted mAb16988 (anti-HBV antibody, core antigen, clone C1-5, aa 74–89, MilliporeSigma, Darmstadt, Germany) and a secondary 1:5000 diluted HRP-coupled anti-mouse antibody (31430, Invitrogen). The antibodies were applied in blocking buffer for 15 minutes, with three PBS washes between the antibodies and after applying the secondary antibody. The chemiluminescent readout was obtained using SuperSignal West Femto maximum sensitive substrate (Thermo Scientific GmbH, Schwerte, Germany) with a c400 Azure imaging system (lowest sensitivity, 90 s exposure time).

Binding intensities were quantified with FIJI (Schindelin et al., 2012) using the ‘microarray profile’ plugin (OptiNav Inc, Bellevue, WA, USA). The raw grayscale intensities for each position were obtained for the left and right sides of the internal duplicate on each microarray slide, n = 3 arrays in total. Blank spots were used to determine the average background grayscale value that was subtracted from the raw grayscale intensities of non-blank spots. Afterward, the spot intensities were normalized to the average grayscale value of the 14 replicates of peptide binder P1 (‘MHRSLLGRMKGA’).

# A parasitic fungus employs mutated eIF4A to survive on rocaglate-synthesizing Aglaia plants

## Authors

- Mingming Chen<sup>1</sup> ([ORCID: 0000-0003-4453-1105](https://orcid.org/0000-0003-4453-1105))
- Naoyoshi Kumakura<sup>3</sup> ([ORCID: 0000-0003-0259-2444](https://orcid.org/0000-0003-0259-2444))
- Hironori Saito<sup>1</sup> ([ORCID: 0000-0001-9623-4132](https://orcid.org/0000-0001-9623-4132))
- Ryan Muller<sup>4</sup> ([ORCID: 0000-0002-8868-7841](https://orcid.org/0000-0002-8868-7841))
- Madoka Nishimoto<sup>5</sup> ([ORCID: 0000-0003-0948-2504](https://orcid.org/0000-0003-0948-2504))
- Mari Mito<sup>2</sup> ([ORCID: 0000-0003-2564-6273](https://orcid.org/0000-0003-2564-6273))
- Pamela Gan<sup>3</sup>
- Nicholas T Ingolia<sup>4</sup> ([ORCID: 0000-0002-3395-1545](https://orcid.org/0000-0002-3395-1545))
- Ken Shirasu<sup>3</sup> ([ORCID: 0000-0002-0349-3870](https://orcid.org/0000-0002-0349-3870))
- Takuhiro Ito<sup>5</sup> ([ORCID: 0000-0003-3704-5205](https://orcid.org/0000-0003-3704-5205))
- Yuichi Shichino<sup>2</sup> ([ORCID: 0000-0002-0093-1185](https://orcid.org/0000-0002-0093-1185))
- Shintaro Iwasaki<sup>1</sup> ([ORCID: 0000-0001-7724-3754](https://orcid.org/0000-0001-7724-3754)) †

### Affiliations

1. Department of Computational Biology and Medical Sciences, Graduate School of Frontier Sciences, The University of Tokyo Kashiwa Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))
2. RNA Systems Biochemistry Laboratory, RIKEN Cluster for Pioneering Research Wako Japan
3. Plant Immunity Research Group, RIKEN Center for Sustainable Resource Science Yokohama Japan ([ROR:010rf2m76](https://ror.org/010rf2m76))
4. Department of Molecular and Cell Biology, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
5. Laboratory for Translation Structural Biology, RIKEN Center for Biosystems Dynamics Research Yokohama Japan ([ROR:023rffy11](https://ror.org/023rffy11))
6. Department of Biological Science, Graduate School of Science, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))

† Corresponding author

## Abstract

Plants often generate secondary metabolites as defense mechanisms against parasites. Although some fungi may potentially overcome the barrier presented by antimicrobial compounds, only a limited number of examples and molecular mechanisms of resistance have been reported. Here, we found an Aglaia plant-parasitizing fungus that overcomes the toxicity of rocaglates, which are translation inhibitors synthesized by the plant, through an amino acid substitution in a eukaryotic translation initiation factor (eIF). De novo transcriptome assembly revealed that the fungus belongs to the Ophiocordyceps genus and that its eIF4A, a molecular target of rocaglates, harbors an amino acid substitution critical for rocaglate binding. Ribosome profiling harnessing a cucumber-infecting fungus, Colletotrichum orbiculare, demonstrated that the translational inhibitory effects of rocaglates were largely attenuated by the mutation found in the Aglaia parasite. The engineered C. orbiculare showed a survival advantage on cucumber plants with rocaglates. Our study exemplifies a plant–fungus tug-of-war centered on secondary metabolites produced by host plants.

## Introduction

Fungi that infect plants are of great economic relevance because they cause severe crop losses (~10%) worldwide (Oerke, 2006). Therefore, the mechanisms underlying plant–fungus interactions have attracted great interest and have been extensively studied (Lo Presti et al., 2015). Secondary metabolites with antimicrobial activities are among the means naturally developed by plants for the control of fungal infections (Collemare et al., 2019). For example, tomatine, a glycoalkaloid secreted from the leaves and stems of tomato, has both fungicidal properties and insecticidal activities (Vance et al., 1987). Camalexin, an indole alkaloid produced by Brassicaceae plants, including the model plant Arabidopsis thaliana, also has antifungal properties (Nafisi et al., 2007).

However, some fungi can overcome these toxic compounds to infect plants. The best-known strategy is the detoxification of antifungal compounds by the secretion of specific enzymes (Crombie et al., 1986; Osbourn et al., 1995; Pareja-Jaime et al., 2008). Thus, plants and infectious fungi are engaged in an arms race during the course of evolution. However, other than detoxification, the mechanistic diversity of the plant–fungus competition centered on plant secondary metabolites is largely unknown.

Rocaglates, small molecules synthesized in plants of the genus Aglaia, exemplify antifungal secondary metabolites (Engelmeier et al., 2000; Iyer et al., 2020). In addition to its antifungal properties, this group of compounds is of particular interest because of its antitumor activities (Alachkar et al., 2013; Bordeleau et al., 2008; Cencic et al., 2009; Chan et al., 2019; Ernst et al., 2020; Lucas et al., 2009; Manier et al., 2017; Nishida et al., 2021; Santagata et al., 2013; Skofler et al., 2021; Thompson et al., 2021; Thompson et al., 2017; Wilmore et al., 2021; Wolfe et al., 2014). Moreover, recent studies have suggested potency against viruses such as SARS-CoV-2 (Müller et al., 2021; Müller et al., 2020) and hepatitis E virus (Praditya et al., 2022). Rocaglates target translation initiation factor (eIF) 4A, a DEAD-box RNA binding protein, and function as potent translation inhibitors with a unique mechanism: rocaglate treatment does not phenocopy the loss of function of eIF4A but instead leads to gain of function. Although eIF4A activates the translation of cellular mRNA through ATP-dependent RNA binding, rocaglates impose polypurine (A and G repeated) sequence selectivity on eIF4A, bypassing the ATP requirements and evoking mRNA-selective translational repression (Chen et al., 2021; Chu et al., 2020; Chu et al., 2019; Iwasaki et al., 2019; Iwasaki et al., 2016; Rubio et al., 2014; Wolfe et al., 2014). The artificial anchoring of eIF4A (1) becomes a steric hindrance to scanning 40S ribosomes (Iwasaki et al., 2019; Iwasaki et al., 2016), (2) masks cap structure of mRNA by tethering eIF4F (Chu et al., 2020), and (3) reduces the available pool of eIF4A for active translation initiation events by the sequestration of eIF4A on mRNAs (Chu et al., 2020).

Since eIF4A is an essential gene for all eukaryotes, Aglaia plants must have a mechanism to evade the cytotoxicity of the rocaglates they produce. This self-resistance is achieved by the unique amino acid substitutions at the sites in eIF4A proteins where rocaglates directly associate (Iwasaki et al., 2019). Given the high evolutionary conservation of eIF4A and thus its rocaglate binding pocket (Iwasaki et al., 2019), these compounds may target a wide array of natural fungi.

Irrespective of the antifungal nature of rocaglates, we found a parasitic fungus able to grow on Aglaia plants. De novo transcriptome analysis from the fungus revealed that this species belongs to the Ophiocordyceps genus, whose members infect ants and cause a 'zombie' phenotype (Andersen et al., 2009; Araújo and Hughes, 2019; de Bekker et al., 2017), but constitutes a distinct branch in the taxon. Strikingly, eIF4A from this fungus possessed an amino acid substitution in the rocaglate binding site and thus showed resistance to the compound. Using Colletotrichum orbiculare, a cucumber-infecting fungus, as a model, we demonstrated that the genetically engineered fungus with the substitution showed insensitivity to the translational repression induced by rocaglates, facilitating its infection of plants even in the presence of this compound. Our results indicate fungal resistance to plant secondary metabolites independent of detoxification enzymes and a unique contest between plants and fungi centered on secondary metabolites synthesized in the host plant.

## Results

### Identification of a fungal parasite on the rocaglate-producing plant Aglaia

Considering that Aglaia plants possess antifungal rocaglates (Engelmeier et al., 2000; Iyer et al., 2020), parasitic fungi should have difficulty infecting rocaglate-producing plants. In contrast to this idea, we identified a fungus growing on the surface of the stem of the Aglaia odorata plant with tremendous vitality (Figure 1A). To characterize this fungus, we isolated the RNA, conducted RNA sequencing (RNA-Seq), reconstructed the transcriptome, and annotated the functionality of each gene (Supplementary file 1).

![Figure 1.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig1-v1.jpg)

**Figure 1.:** (A) Image of a parasite fungus growing on Aglaia odorata. (B) Multilocus phylogenetic tree of Ophiocordyceps species generated from maximum likelihood phylogenetic analysis of ITS, SSU, LSU, RPB1, and TEF1α sequences. Tolypocladium species were used as outgroups. The best DNA substitution models of ITS, LSU, SSU, RPB1, and TEF1α were calculated as TIM3ef + G4, TIM1 + I + G4, TIM3ef + I + G4, TrN + I + G4, and TIM1 + I + G4, respectively. Numbers on branches are percent support values out of 1000 bootstrap replicates. Only bootstrap values greater than 50% support are shown. Endophytes are highlighted with green dots.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The maximum likelihood best scoring trees based on ITS locus from the Ophiocordyceps species with Tolypocladium species as outgroups. Numbers at nodes are percentages of bootstrap support values out of 1000. Only bootstrap values above 50% are shown.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** The maximum likelihood best scoring trees based on SSU locus from the Ophiocordyceps species with Tolypocladium species as outgroups. Numbers at nodes are percentages of bootstrap support values out of 1,000. Only bootstrap values above 50% are shown.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** The maximum likelihood best scoring trees based on LSU locus from the Ophiocordyceps species with Tolypocladium species as outgroups. Numbers at nodes are percentages of bootstrap support values out of 1000. Only bootstrap values above 50% are shown.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** The maximum likelihood best scoring trees based on RPB1 locus from the Ophiocordyceps species with Tolypocladium species as outgroups. Numbers at nodes are percentages of bootstrap support values out of 1000. Only bootstrap values above 50% are shown.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** The maximum likelihood best scoring trees based on TEF1α locus from the Ophiocordyceps species with Tolypocladium species as outgroups. Numbers at nodes are percentages of bootstrap support values out of 1000. Only bootstrap values above 50% are shown.

This Aglaia-infecting fungus belonged to the Ophiocordyceps genus, which is known as zombie-ant fungus (Andersen et al., 2009; Araújo and Hughes, 2019; de Bekker et al., 2017). Ophiocordyceps spp. are members of the phylum Ascomycota and constitute the taxonomic groups with the highest number of entomopathogenic species among all fungal genera. In most cases, each Ophiocordyceps spp. has a specific host insect species, develops fruiting bodies from the remains of host insects, and produces spores. In addition to insect infection, a moth parasite, Ophiocordyceps sinensis, has been found to reside on many plant species, suggesting that Ophiocordyceps also has an endophytic lifestyle (Wang et al., 2020; Zhong et al., 2014). We performed a BLASTn search (Camacho et al., 2009) using the internal transcribed spacer (ITS) between rRNAs as a query and found that, among all the deposited nucleotide sequences in the database, 29 of the top 30 hits were from Ophiocordyceps species (Supplementary file 2).

To identify the species-level taxon of the Aglaia-infecting fungus, we conducted a multilocus phylogenetic analysis for comparison with currently accepted species in the Ophiocordyceps genus (Supplementary file 3). For this purpose, sequences of the ITS, small subunit ribosomal RNA (SSU), large subunit rRNA (LSU), translation elongation factor 1-alpha (TEF1α), and RNA polymerase II largest subunit (RPB1) were used as previously reported for the classification of Ophiocordyceps species (Xiao et al., 2017; Supplementary file 3). These sequences from 68 isolates were aligned, trimmed, and concatenated, resulting in a multiple sequence alignment comprising 3910 nucleotide positions, including gaps (gene boundaries ITS, 1–463; LSU, 464–1363; SSU, 1364–2248; RPB1, 2249–2922; TEF1α, 2923–3910). Then, the best-scoring maximum likelihood (ML) tree was generated from the concatenated sequence alignment using the selected DNA substitution models for each sequence (Figure 1B). This analysis indicated that the Aglaia-infecting fungus was distinct from the other species of Ophiocordyceps (Figure 1B). In particular, the strain isolated from Aglaia was positioned on a long branch separated from the most closely related strain, O. coccidiicola NBRC 100682, as supported by the 95% bootstrap value. The separation of Aglaia-infecting fungus from other Ophiocordyceps species was also confirmed by single-locus alignments (Figure 1—figure supplements 1–5), although the positions of the Aglaia-infecting fungus in the tree were different. We note that RPB1-locus alignment was an exception since the de novo-assembled transcriptome from the Aglaia-infecting fungus lacked the sequence of the homolog.

Given that the most closely related Ophiocordyceps species is sufficiently distinct from the Aglaia-infecting fungus in sequence and that no similar fungi grown in Aglaia plants were reported before, we named the fungus Ophiocordyceps sp. BRM1 (Berkeley, Ryan Muller, strain 1). Consistent with its isolation from the Aglaia plant, this fungus was closely related to known endophytic Ophiocordyceps spp. (Figure 1B and Supplementary file 3; Wang et al., 2020; Zhong et al., 2014).

### Transcriptome assembly uncovers the unique mutation in eIF4A of the Aglaia-infecting fungus

The parasitic nature of Ophiocordyceps sp. BRM1 on plants producing the antifungal rocaglate led us to hypothesize that the fungus may have a mechanism to evade the toxicity of the compounds. Indeed, the host plant Aglaia achieves this task by introducing an amino acid substitution in eIF4A, a target of rocaglates (Iwasaki et al., 2019). The substituted amino acid (Phe163, amino acid position in human eIF4A1) lies at the critical interface for rocaglate interaction (Figure 2A and D; Iwasaki et al., 2019). Accordingly, we investigated possible amino acid conversions in eIF4As of the Ophiocordyceps sp. BRM1. Among the de novo-assembled transcriptome, ~60 DEAD-box RNA binding protein genes, including 4 transcript isoforms of eIF4A, were found (Supplementary file 1).

![Figure 2.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig2-v1.jpg)

**Figure 2.:** (A, B) Alignments of eIF4A protein sequences from higher eukaryotes (A) and fungal species (B), including the de novo-assembled Ophiocordyceps sp. BRM1 eIF4A gene with four transcript isoforms (iso). (C) The summary of Kd determined by fluorescence polarization assay in Figure 2—figure supplement 2A–H is depicted. WT and mutated eIF4A proteins from the indicated species were used. To measure ATP-independent RNA clamping induced by RocA (50 µM), ADP and Pi (1 mM each) were included in the reaction. The data are presented as the mean and s.d. values. (D) RocA (sphere model with light pink-colored carbons), the modeled His, Gly, and Leu residues (surface model with cyan-colored carbons) at the Phe163 residue in human eIF4A1 (surface model with green-colored carbons), and RNA (surface model with yellow-colored carbons) in the complex of human eIF4A1•RocA•AMP-PNP•polypurine RNA (PDB: 5ZC9) (Iwasaki et al., 2019).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Alignment of eIF4A protein sequences from the indicated species. Percent similarity and percent identity to H. sapiens eIF4A1 are shown at the top. (B) Coomassie brilliant blue staining of recombinant eIF4A proteins used in this study. (C) Chemical structures of rocaglates used in this study.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A–H) Fluorescence polarization assay for FAM-labeled RNA ([AG]10) (10 nM). WT and mutated eIF4A proteins from the indicated species were used. To measure ATP-independent RNA clamping induced by RocA (50 µM), ADP and Pi (1 mM each) were included in the reaction. The data are presented as the mean and s.d. values (n = 3).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A–H) Fluorescence polarization assay for FAM-labeled RNA ([AG]10) (10 nM). WT and mutated eIF4A proteins from the indicated species were used. The ground-state ATP analog AMP-PNP (1 mM) was included in the reaction with RocA (50 µM). The data are presented as the mean and s.d. values (n = 3). (I) Affinity fold changes between DMSO and RocA treatment by amino acid substitutions in (A–H) were calculated. The data are presented as the mean and s.d. values.

Remarkably, we observed an amino acid conversion in Ophiocordyceps sp. BRM1 eIF4A at the same residue as in the Aglaia plant eIF4A. A Gly residue replaced Phe163 (human position) in all four transcript isoforms (from the same eIF4A gene) in Ophiocordyceps sp. BRM1 (Figure 2B, Figure 2—figure supplement 1A), whereas His residues prevailed in the close kin of Ophiocordyceps species and other fungi.

### Gly153 in Ophiocordyceps sp. BRM1 eIF4A eliminated rocaglate-mediated polypurine RNA clamping

Indeed, we found that the Gly substitution confers rocaglate resistance on eIF4A. To investigate rocaglate-targetability, we harnessed the fluorescence polarization assay with fluorescein (FAM)-labeled short RNA and purified recombinant eIF4A proteins (Figure 2—figure supplement 1B). As observed previously (Chen et al., 2021; Chu et al., 2020; Chu et al., 2019; Iwasaki et al., 2019; Iwasaki et al., 2016; Naineni et al., 2021), rocaglamide A (RocA), a natural rocaglate derivative isolated from Aglaia plants (Figure 2—figure supplement 1C; Janprasert et al., 1992), clamped human eIF4A1 on polypurine RNA ([AG]10) in an ATP-independent manner (e.g., in the presence of ADP + Pi) (Kd = ~0.42 µM, Figure 2C, left, Figure 2—figure supplement 2A, and Table 1). Whereas a high affinity for polypurine RNA was observed for eIF4A from O. sinensis (CO18 GCA 000448365) (Kd = ~0.11 µM, Figure 2C middle; Figure 2—figure supplement 2D; and Table 1) — the closest relative among whole-genome-sequenced Ophiocordyceps species (Figure 1B; de Bekker et al., 2017), Ophiocordyceps sp. BRM1 eIF4A showed a fairly high Kd (~17 µM, Figure 2C, right, Figure 2—figure supplement 2H, and Table 1).

**Table 1.**
 Summary of Kd (µM) between eIF4A protein and RNAs.A fluorescence polarization assay between FAM-labeled RNA ([AG]10) and the indicated recombinant proteins was conducted to measure Kd in the presence of DMSO, RocA, or aglafoline. ND, not determined.


<table>
  <thead>
    <tr>
      <th colspan="6">[AG]10</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="3">ADP + Pi</th>
      <th colspan="2">AMP-PNP</th>
    </tr>
    <tr>
      <th>Protein</th>
      <th>DMSO</th>
      <th>RocA</th>
      <th>Aglafoline</th>
      <th>DMSO</th>
      <th>RocA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>H. sapiens WT Phe163</td>
      <td></td>
      <td>0.42 ± 0.061</td>
      <td></td>
      <td>11 ± 2.9</td>
      <td>0.067 ± 0.023</td>
    </tr>
    <tr>
      <td>H. sapiens Phe163His</td>
      <td></td>
      <td>4.0 ± 0.71</td>
      <td></td>
      <td>16 ± 2.7</td>
      <td>0.11 ± 0.025</td>
    </tr>
    <tr>
      <td>H. sapiens Phe163Gly</td>
      <td></td>
      <td>14 ± 2.0</td>
      <td></td>
      <td>21 ± 6.7</td>
      <td>0.58 ± 0.13</td>
    </tr>
    <tr>
      <td>O.sinensis WT His154</td>
      <td></td>
      <td>0.11 ± 0.022</td>
      <td></td>
      <td>41 ± 11</td>
      <td>0.090 ± 0.014</td>
    </tr>
    <tr>
      <td>O.sinensis His154Gly</td>
      <td></td>
      <td>0.85 ± 0.12</td>
      <td></td>
      <td>27 ± 7.0</td>
      <td>0.37 ± 0.046</td>
    </tr>
    <tr>
      <td>Ophiocordyceps sp. BRM1 Gly172Phe</td>
      <td>ND</td>
      <td>0.27 ± 0.050</td>
      <td>0.11 ± 0.021</td>
      <td>110 ± 58</td>
      <td>0.053 ± 0.023</td>
    </tr>
    <tr>
      <td>Ophiocordyceps sp. BRM1 Gly172His</td>
      <td>ND</td>
      <td>3.9 ± 0.98</td>
      <td>1.5 ± 0.14</td>
      <td>3.3 ± 0.83</td>
      <td>0.051 ± 0.0091</td>
    </tr>
    <tr>
      <td>Ophiocordyceps sp. BRM1 WT Gly172</td>
      <td>ND</td>
      <td>17±7.4</td>
      <td>2.6±0.40</td>
      <td>7.1±2.3</td>
      <td>0.23±0.050</td>
    </tr>
  </tbody>
</table>

Given the Gly substitution in Ophiocordyceps sp. BRM1 eIF4A (Figure 2A), we hypothesized that this amino acid substitution explains the differential sensitivity to RocA. Indeed, both the Gly-to-Phe (human) and Gly-to-His (O. sinensis) substitutions in Ophiocordyceps sp. BRM1 eIF4A (Gly172Phe and Gly172His, respectively) sensitized the protein to RocA (Figure 2—figure supplement 2F and G), significantly reducing the Kd (Figure 2C, right, and Table 1). Conversely, introduction of a Gly residue into human and O. sinensis eIF4As reduced the affinity for polypurine RNA (Figure 2C, left, middle; Figure 2—figure supplement 2C and E, and Table 1).

A similar rocaglate sensitivity in RNA binding was also observed for adenylyl-imidodiphosphate (AMP-PNP), a ground-state ATP analog (Figure 2—figure supplement 3A–H and Table 1). Unlike ADP + Pi, the nonhydrolyzable analog AMP-PNP allowed basal binding to polypurine RNAs in the absence of RocA. The affinity was further increased by RocA in eIF4A with a Phe or His residues at 163 (human position). In contrast, the proteins with the Gly residue showed the relatively small affinity changes (Figure 2—figure supplement 3I and Table 1).

Taking these biochemical data together, we concluded that the Ophiocordyceps sp. BRM1 eIF4A evades rocaglate targeting by substituting a critical amino acid involved in its binding. When Phe163 was replaced by Gly in the crystal structure of the human eIF4A1•RocA complex (Iwasaki et al., 2019), the π-π stacking with ring C of RocA was totally lost (Figure 2D and Figure 2—figure supplement 1C), likely leading to reduced affinity for RocA. This mechanism to desensitize eIF4A to rocaglates was distinct from the Leu substitution found in Aglaia, which fills the space of the rocaglate binding pocket and thus prevents the interaction (Iwasaki et al., 2019).

Our data showed that eIF4A with His at position 163 (human position) is also a target of rocaglate (Figure 2C, Figure 2—figure supplement 2, Figure 2—figure supplement 3, and Table 1). This is most likely due to the functional replacement of the aromatic ring in Phe by the imidazole ring in His for stacking with ring C of rocaglates (Figure 2D). Although compared to the Phe substitution, the His substitution in human and Ophiocordyceps sp. BRM1 eIF4As was accompanied by an attenuated potency of RocA (Figure 2C, Figure 2—figure supplement 2, Figure 2—figure supplement 3, and Table 1), our data suggested that a wide array of fungi that possess the His variant (Figure 2A), including C. orbiculare (see below for details), are also susceptible to rocaglates.

### Gly153 found in Ophiocordyceps sp. BRM1 eIF4A confers resistance to rocaglate-induced translational repression

The reduced affinity to polypurine RNA gained in the Ophiocordyceps sp. BRM1 eIF4A by Gly substitution led us to investigate the impact on rocaglate-mediated translational repression. To test this, we applied a reconstituted translation system with human factors (Iwasaki et al., 2019; Machida et al., 2018; Yokoyama et al., 2019). As observed in an earlier study (Iwasaki et al., 2019), this system enabled the recapitulation of translation reduction from polypurine motif-possessing reporter mRNA but not from mRNA with control CAA repeats in a RocA dose-dependent manner (Figure 3A). In contrast, replacing wild-type human eIF4A1 with the Phe163Gly mutant prevented the translation repression mediated by RocA (Figure 3A), consistent with the affinity between the recombinant human eIF4A1 proteins and polypurine RNA (Figure 2C, Figure 2—figure supplement 2, Figure 2—figure supplement 3, and Table 1).

![Figure 3.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig3-v1.jpg)

**Figure 3.:** (A) RocA-mediated translational repression recapitulated by an in vitro reconstitution system with human factors. Recombinant proteins of H. sapiens eIF4A1 WT or Phe163Gly were added to the reaction with RocA. Reporter mRNA with CAA repeats or polypurine motifs was translated in the reaction. The data are presented as the mean and s.d. values (n = 3). (B) Translation of complex-preformed mRNAs to test the RocA gain of function. Recombinant proteins of Ophiocordyceps sp. BRM1 eIF4A1 WT or the Gly172His mutant were preincubated with the reporter mRNA possessing polypurine motifs in the presence or absence of RocA. After removal of free RocA by gel filtration, the protein-mRNA complex was added to RRL to monitor protein synthesis. The data are presented as the mean and s.d. values (n = 3). (C) MA (M, log ratio; A, mean average) plot of the translation efficiency changes caused by 3 µM aglafoline treatment in C. orbiculare eIF4AWT conidia. Resistant and sensitive mRNAs (FDR < 0.05) are highlighted. (D) Cumulative distribution of the translation efficiency changes in aglafoline-sensitive mRNAs (defined in C) in C. orbiculare eIF4AWT conidia treated with 0.3 or 3 µM aglafoline. (E) Cumulative distribution of the translation efficiency changes in aglafoline-sensitive mRNAs (defined in C) induced by 3 µM aglafoline treatment in C. orbiculare eIF4AWT and eIF4AHis153Gly conidia. (F) Cumulative distribution of the global translation alterations, which are footprint changes normalized to mitochondrial footprints, in aglafoline-sensitive mRNAs (defined in C) induced by 3 µM aglafoline treatment in C. orbiculare eIF4AWT and eIF4AHis153Gly conidia. (G) Box plot of the translation efficiency changes caused by 3 µM aglafoline treatment in conidia across mRNAs with or without an [A/G]6 motif in the 5′ UTR. The p values in (D–G) were calculated by the Mann–Whitney U test.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Schematics of eIF4A recombination in C. orbiculare. NPTII, neomycin phosphotransferase II. (B) PCR-based screening of the recombined strains. The primer sets used for screening are depicted in (A). (C, D) Colony formation of the indicated C. orbiculare strains cultured in PDA for 5 days (C). The measured colony diameters are shown in the box plot (n = 5) (D). (E–G) Fluorescence polarization assay for FAM-labeled RNA ([AG]10) (10 nM). WT and mutated Ophiocordyceps sp. BRM1 eIF4A proteins were used. To measure ATP-independent RNA clamping induced by aglafoline (50 µM), ADP and Pi were included in the reaction. The data are presented as the mean and s.d. values (n = 3). (H) Summary of the Kd values in (E–G) under treatment with aglafoline. The data are presented as the mean and s.d. values.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) Distribution of ribosome footprint length in conidia and mycelia. (B) Tile plot of reading frames at each ribosome footprint length in conidia and mycelia. The 5′ end positions of the ribosome footprints are depicted. The footprint count scales are shown in the color bars. (C) Metagene plot of 29-nt ribosome footprints around start (left) and stop (right) codons in conidia and mycelia. The 5′ end positions of the ribosome footprints are depicted. RPM: reads per million mapped reads.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) GO term analysis of aglafoline-sensitive mRNAs (defined in Figure 3C). GO terms associated with yeast homologs were analyzed by DAVID (Huang et al., 2009a; Huang et al., 2009b). (B) MA plot of the translation efficiency changes induced by 3 µM aglafoline treatment in C. orbiculare eIF4AWT mycelia. Resistant and sensitive mRNAs (false discovery rate [FDR] < 0.05) are highlighted. (C) Cumulative distribution of the translation efficiency changes in aglafoline-sensitive mRNAs (defined in B) in C. orbiculare eIF4AWT mycelia treated with 0.3 or 3 µM aglafoline. (D) Cumulative distribution of the translation efficiency changes in aglafoline-sensitive mRNAs (defined in B) induced by 3 µM aglafoline treatment in C. orbiculare eIF4AWT and eIF4AHis153Gly mycelia. (E) Cumulative distribution of the global translation alterations, which are footprint changes normalized to mitochondrial footprints, in aglafoline-sensitive mRNAs (defined in B) induced by 3 µM aglafoline treatment in C. orbiculare eIF4AWT and eIF4AHis153Gly conidia. (F) Box plot of translation efficiency changes caused by 3 µM aglafoline treatment in mycelia across mRNAs with or without an [A/G]6 motif in the 5′ UTR. (G) Venn diagram of the overlap between aglafoline-sensitive mRNAs in conidia (defined in Figure 3C) and mycelia (defined in B). The p values in (C–F) were calculated by the Mann–Whitney U test.

Given that rocaglate-mediated translational repression is driven by a gain of function (Chen et al., 2021; Iwasaki et al., 2016; Iwasaki et al., 2019), Ophiocordyceps sp. BRM1 eIF4A should not have this mode. To investigate this possibility, we used a preformed RocA-eIF4A-mRNA complex for the translation reaction (Iwasaki et al., 2019; Iwasaki et al., 2016). We first preincubated recombinant Ophiocordyceps sp. BRM1 eIF4A or the corresponding Gly172His mutant protein with a reporter mRNA possessing polypurine motifs in the presence or absence of RocA. If RocA could target the eIF4A protein, eIF4A should be stably clamped on the polypurine tract, providing steric hindrance to scanning ribosomes and thus repressing protein synthesis in rabbit reticulocyte lysate (RRL). Whereas WT Ophiocordyceps sp. BRM1 eIF4A could not alter translation (Figure 3B, left) due to its weaker ability to clamp on polypurine RNAs, the Gly172His mutant could act as a translation repressor (Figure 3B, right). These data indicated that Gly172His in Ophiocordyceps sp. BRM1 eIF4A restores the gain-of-function mechanism of RocA.

We further tested the impact of the Gly conversion in eIF4A in a fungus. Due to the difficulty of culturing and manipulating the genetics of Ophiocordyceps sp. BRM1 (data not shown), we instead harnessed C. orbiculare, an anthracnose-causing fungus (Gan et al., 2019; Gan et al., 2013). Through homology-directed repair induced by CRISPR–Cas9-mediated genome cleavage, we replaced endogenous eIF4A with wild-type (WT) or Gly-mutated (His153Gly) C. orbiculare eIF4A (Figure 2—figure supplement 1A, Figure 3—figure supplement 1A and B). Notably, we did not find any significant growth defects resulting from these genetic manipulations (Figure 3—figure supplement 1C and D).

Since the culture of the isolated strains requires a significant amount of the compounds, we used aglafoline (methyl rocaglate) (Figure 2—figure supplement 1C), a less expensive, commercially available natural derivative of rocaglates (Ko et al., 1992), instead of RocA. The difference between RocA and aglafoline is the dimethylamide group versus the methoxycarbonyl group (Figure 2—figure supplement 1C), which do not contribute to the association with eIF4A or polypurine RNA (Iwasaki et al., 2019), suggesting that the compounds should have similar mechanisms of action. As expected, aglafoline resulted in essentially the same molecular phenotype of ATP-independent polypurine clamping of the Ophiocordyceps sp. BRM1 eIF4A (Figure 3—figure supplement 1E–H and Table 1) as RocA (Figure 2C, right, Figure 2—figure supplement 2F–H; and Table 1).

To understand the translational repression induced by aglafoline in a genome-wide manner, we applied ribosome profiling, a technique based on deep sequencing of ribosome-protected RNA fragments (i.e., ribosome footprints) generated by RNase treatment (Ingolia et al., 2019; Ingolia et al., 2009; Iwasaki and Ingolia, 2017), to the isolated fungus strains. The ribosome footprints obtained from C. orbiculare (in the culture of conidia and mycelia) showed the signatures of this experiment: two peaks of footprint length at ~22 nt and ~30 nt (Figure 3—figure supplement 2A), which respectively represent the absence or presence of A-site tRNA in the ribosome (Lareau et al., 2014; Wu et al., 2019), and 3-nt periodicity along the open reading frame (ORF) (Figure 3—figure supplement 2B and C). By normalizing the footprint reads by the RNA abundance as measured by RNA-Seq, we calculated the translation efficiency and quantified its change induced by aglafoline treatment.

Strikingly, this genome-wide approach revealed that His153Gly confers translational resistance to aglafoline on C. orbiculare. Consistent with the mRNA-selective action of the compound, we observed that a subset of mRNAs showed high aglafoline sensitivity in terms of translation efficiency in conidia (Figure 3C) and that the reduction was compound dose dependent (Figure 3D). Intriguingly, we observed that genes associated with the ribosome and its assembly were susceptible to rocaglate-mediated translational repression (Figure 3—figure supplement 3A). The reduction in translation efficiency mediated by aglafoline was attenuated by the His153Gly substitution (Figure 3E). This conclusion was also supported by global translation assessment (Figure 3F), which is based on cytosolic ribosome footprint alterations normalized to the mitochondrial footprints as internal spike-ins (Iwasaki et al., 2016). Consistent with earlier reports (Chen et al., 2021; Chu et al., 2020; Chu et al., 2019; Iwasaki et al., 2016; Iwasaki et al., 2019), the reduction in translation efficiency was associated with the presence of polypurine motifs in the 5′ UTR (Figure 3G). However, the His153Gly substitution compromised the polypurine-dependent translational repression. Although the mycelial stage of the fungus showed the similar trends in translational repression mediated by aglafoline (Figure 3—figure supplement 3B–F), the sensitive mRNAs were distinct from those in conidia (Figure 3—figure supplement 3G), suggesting differential impacts of rocaglates during the fungal life cycle.

### Rocaglate-resistant fungi show an advantage in infection of plants with rocaglates

We were intrigued to test the role of Gly substitution in the parasitic property of fungi. Here, we used the infection process of C. orbiculare on cucumber leaves as a model system. The conidia of WT or His153Gly eIF4A-recombined strains were sprayed on Cucumis sativus (cucumber) cotyledons, and the biomass after inoculation with rocaglate was quantified (Figure 4A). Indeed, aglafoline reduced the biomass of the WT eIF4A-recombined strain on cucumber leaves, showing the antifungal effect of rocaglate (Figure 4B). In stark contrast, the His153Gly mutation in eIF4A affected fungal growth on cucumber leaves and resulted in rocaglate resistance in the fungi (Figure 4B). We note that the differential biomass of C. orbiculare could not be explained by the damage to cucumber leaves by aglafoline treatment as no morphological alteration of the leaves was observed under our conditions (Figure 4—figure supplement 1A). These results demonstrated that the Gly substitution found in Ophiocordyceps sp. BRM1 eIF4A provides the molecular basis of antirocaglate properties and allows the growth of the parasitic fungus in the presence of rocaglate (Figure 5).

![Figure 4.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig4-v1.jpg)

**Figure 4.:** (A) Workflow for monitoring the biomass of C. orbiculare eIF4AWT or eIF4AHis153Gly strains on cucumber leaves under treatment with aglafoline. (B) Comparison of in planta fungal biomass of C. orbiculare eIF4AWT or eIF4AHis153Gly strains with or without treatment with 1 µM aglafoline. Relative expression levels of the C. orbiculare 60 S ribosomal protein L5 gene (GenBank: Cob_v012718) normalized to that of a cucumber cyclophilin gene (GenBank: AY942800.1) were determined by RT–qPCR at 3 dpi (n = 8). The relative fungal biomasses of C. orbiculare were normalized to those of eIF4AWT without aglafoline. Significance was calculated by Student’s t-test (two-tailed). Three independent experiments showed similar results.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) C. sativus leaves were sprayed with DMSO or aglafoline (1 µM) in water and incubated for 3 days using the same method as C. orbiculare inoculation.

![Figure 5.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig5-v1.jpg)

**Figure 5.:** The ancestors of the Aglaia plants may have been subjected to fungal infection. To counteract this, Aglaia plants may have developed rocaglates to target the conserved translation factor eIF4A and to suppress in planta fungal growth. Simultaneously, Aglaia plants exhibit amino acid substitutions in the rocaglate binding pocket of eIF4As to prevent self-poisoning. Some fungi may impede rocaglate toxin by converting eIF4A to a rocaglate-insensitive form, enabling them to parasitize these plants.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/81302/elife-81302-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Alignment of DDX3 protein sequences from higher eukaryotes and fungal species, including Ophiocordyceps sp. BRM1 DDX3s.

## Discussion

Since plants often produce antifungal secondary metabolites, a specific compound in the host plant may define the interaction between that plants and parasitic fungi (Pusztahelyi et al., 2015). The antifungal activity of rocaglates may protect Aglaia plants from phytopathogenic fungi (Figure 5, top and middle). Rocaglate may suppress protein synthesis from survival-essential genes such as translation machinery. To survive the presence of rocaglate, which targets the general translation initiation factor eIF4A, this plant adapts eIF4A through specific amino acid substitutions (Phe163Leu-Ile199Met: hereafter, we use the human position to specify amino acid residues) to evade the toxicity of the compounds (Iwasaki et al., 2019). This study showed that the parasitic fungus Ophiocordyceps sp. BRM1, which possibly originates from Ophiocordyceps spp. with an endophytic life stage, on Aglaia could also overcome this barrier by introducing an amino acid conversion (Phe163Gly) in eIF4A (Figure 5, bottom). Our results highlighted a tug-of-war between host plants and parasitic fungi through the production of translation inhibitory compounds and mutagenization in the target translation factor.

The molecular basis of secondary metabolite resistance in Ophiocordyceps sp. BRM1 is markedly distinct from the known strategies developed in other fungi. Avenacin from oats — an example of a plant-secreted antimicrobial substance (Morrissey and Osbourn, 1999) — is a triterpenoid that forms complexes with sterols in fungal cell membranes, causes a loss of membrane integrity, and thus exerts an antifungal effect (Armah et al., 1999; Osbourn et al., 1994). To counteract this compound and infect oats, the phytopathogenic fungus Gaeumannomyces graminis var. avenae (Gga) secretes avenaciase (Crombie et al., 1986; Osbourn et al., 1995), a β-glycosyl hydrolase that hydrolyzes terminal D-glucose in the sugar chain of avenacin. Indeed, avenacin degradation by this enzyme determines the host range of the fungus (Bowyer et al., 1995). In contrast to the detoxification strategy, Ophiocordyceps sp. BRM1 may cope with rocaglates through desensitization of the target protein eIF4A by an amino acid substitution (Figure 2), leaving the compound intact.

The different resistance mechanisms to toxic small molecules should be highly related to the compound targets. Since sterols targeted by avenacin are biosynthesized via complicated multiple steps with diverse enzymes, thus generating diverse sterol structures, the conversion of target sterols to evade avenacin requires many enzyme modifications and occurs only rarely. On the other hand, the target of rocaglates is an eIF4A protein (and a DDX3 protein, see below for details), and thus, evasion by a single amino acid mutation is relatively likely. These results exemplify the mechanistic diversity of attack and counterattack during plant–fungal pathogen interactions.

Although we observed that Gly163 in Ophiocordyceps sp. BRM1 eIF4A produced a substantial change in sensitivity to rocaglate, the resistance may not be as complete as that obtained by the substitution found in Aglaia Phe163Leu (Iwasaki et al., 2019). Additionally, the translation factor DDX3, which was recently found to be an alternative target of rocaglate (Chen et al., 2021), did not have amino acid substitutions in Ophiocordyceps sp. BRM1 (Figure 5—figure supplement 1A), whereas Aglaia DDX3s harbor a substitution at Gln360 (Chen et al., 2021). This may indicate that Ophiocordyceps sp. BRM1 is still in the process of evolving fitness for growth in Aglaia plants. Alternatively, the rocaglate-resistant amino acid conversions may involve a trade-off with the basal translation activity. Even with the inefficiency in translation, given that other fungi could not use the resources from the plant, this substitution may still be beneficial to fungi because of the lack of competition from other fungal species. These possibilities are not mutually exclusive.

## Materials and methods

### RNA-Seq and de novo transcriptome assembly of Ophiocordyceps sp. BRM1

Fungi on the stem of A. odorata (grown in Berkeley, CA) were harvested and subjected to RNA extraction with hot phenol. After further chloroform extraction, RNA was subjected to rRNA depletion by a Ribo-Zero Gold rRNA Removal Kit (Yeast) (Illumina). The RNA-Seq library was generated by a TruSeq Stranded mRNA Kit (Illumina) and sequenced by HiSeq4000 (Illumina) with a paired-end 100 bp option. Notably, reads from rRNA genes (i.e., internal transcribed spacer [ITS]) remained after rRNA depletion and were used for phylogenetic analysis.

Transcriptome assembly and functional annotation were performed as described previously (Iwasaki et al., 2019) using Trinity (Grabherr et al., 2011) and Trinotate (Haas et al., 2013). The eIF4A and DDX3 homologous sequences were aligned with MUSCLE (https://www.ebi.ac.uk/Tools/msa/muscle/) and depicted by ESPript 3.0 (Robert and Gouet, 2014; http://espript.ibcp.fr/ESPript/ESPript/). eIF4A and DDX3 homologous sequences of model species were obtained from UniProt. For Ophiocordyceps species, Tolypocladium species, and C. orbiculare, the ORF databases were obtained from EnsemblFungi (https://fungi.ensembl.org/index.html) or the Ohm laboratory (http://fungalgenomics.science.uu.nl; de Bekker et al., 2017). To survey the eIF4A and DDX3 homologs, the closest homologs of all the proteins in each species were searched with BLASTp (Camacho et al., 2009; https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/).

### Phylogenetic analysis

To identify the genus of the Aglaia-infecting fungus, closely related species were predicted. The de novo-assembled transcriptome sequence of the Aglaia-infecting fungus was searched by BLASTn (Camacho et al., 2009; https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/) using the C. aotearoa ICMP 18537 ITS sequence (GenBank accession: NR_120136) (Schoch et al., 2014) as a query. Using the best hit sequence as a query, a BLASTn search was performed against the NCBI nucleotide collection (nr/nt) (Supplementary file 2).

A multilocus phylogenetic analysis of the Aglaia-infecting fungus with Ophiocordyceps species was performed. A total of 68 isolates were used for phylogenetic analysis, including an Aglaia-infecting fungus, 63 previously classified Ophiocordyceps strains consisting of 52 species, and 4 Tolypocladium species that were expected to serve as outgroups (Supplementary file 3). DNA sequences of ITS, SSU, LSU, TEF1α, and RPB1 were used as previously reported for the classification of Ophiocordyceps species (Xiao et al., 2017). Additional genomic sequences of Ophiocordyceps species identified by BLASTn were added to the analysis (Supplementary file 3). A phylogenetic tree was calculated as previously described (Gan et al., 2017; Xiao et al., 2017). Each locus (ITS, LSU, SSU, RPB1, and TEF1α) of the 68 isolates (Ban et al., 2015; Castlebury et al., 2004; Chen et al., 2013; de Bekker et al., 2017; Hu et al., 2013; Kepler et al., 2012; Liu et al., 2002; Luangsa-Ard et al., 2011; Luangsa-Ard et al., 2010; Quandt et al., 2018; Quandt et al., 2014; Sanjuan et al., 2015; Schoch et al., 2012; Spatafora et al., 2007; Sung et al., 2007; Wen et al., 2013; Will et al., 2020; Xiao et al., 2017) was aligned using MAFFT v7.480 (Katoh and Standley, 2013) and trimmed by trimAl v1.4.rev15 (Capella-Gutiérrez et al., 2009) with an automated setting. The processed sequences obtained from every 68 isolates were concatenated by catfasta2phyml v1.1.0 (Nylander, 2018; https://github.com/nylander/catfasta2phyml) to generate sequences comprising 3910 nucleotide positions, including gaps (gene boundaries ITS, 1–463; LSU, 464–1363; SSU, 1364–2248; RPB1, 2249–2922; TEF1α, 2923–3910). The best model for nucleotide substitutions under the BIC criterion was determined by ModelTest-NG v.0.1.6 (Darriba et al., 2020; https://github.com/ddarriba/modeltest) as follows: ITS, TIM3ef + G4; LSU, TIM1 + I + G4; SSU, TPM3 + I + G4; RPB1, TIM1 + I + G4; and TEF1α, TrN + I + G4. Then, the maximum likelihood phylogeny was estimated based on concatenated sequences by RAxML-NG v.0.9.0 (Kozlov et al., 2019; https://github.com/amkozlov/raxml-ng) using the ModelTest-NG specified best models for each partition with 1000 bootstrap replicates. The best-scoring maximum likelihood trees with bootstrap support values were visualized in iTOL v6 (Letunic and Bork, 2021; https://itol.embl.de/). Given sufficient separation from other known Ophiocordyceps, the fungus was named Ophiocordyceps sp. BRM1.

### Compounds

RocA (Sigma-Aldrich) and aglafoline (MedChemExpress) were dissolved in dimethyl sulfoxide (DMSO) and used for this study.

### Plasmid construction

#### pColdI-H. sapiens eIF4A1 WT, Phe163Gly, and Phe163His

pColdI-H. sapiens eIF4A1 WT has been reported previously (Iwasaki et al., 2019). Phe163Gly and Phe163His substitutions were induced by site-directed mutagenesis.

#### pColdI-O. sinensis eIF4A WT and His154Gly

DNA fragments containing the O. sinensis eIF4A gene were synthesized by Integrated DNA Technologies (IDT) and inserted into pColdI (TaKaRa) downstream of the His tag with In-Fusion HD (TaKaRa). The His154Gly substitution was induced by site-directed mutagenesis.

#### pColdI-Ophiocordyceps sp. BRM1 eIF4A iso4 WT, Gly172His, and Gly172Phe

The cDNA library of Ophiocordyceps sp. BRM1 was reverse-transcribed with ProtoScript II Reverse Transcriptase (New England Biolabs) and Random Primer (nonadeoxyribonucleotide mix: pd(N)9) (TaKaRa) from the total RNA of Ophiocordyceps sp. BRM1 (see details in the section 'RNA-Seq and de novo transcriptome assembly for Ophiocordyceps sp. BRM1'). Using the cDNA as a template, DNA fragments containing eIF4A iso4 were PCR-amplified and inserted into pColdI (TaKaRa) downstream of the His tag with In-Fusion HD (TaKaRa). The Gly172His and Gly172Phe substitutions were induced by site-directed mutagenesis.

#### pENTR4-C. orbiculare eIF4A WT and His153Gly

To replace the eIF4A (GenBank: Cob_v000942) sequence in the C. orbiculare genome with synthesized C. orbiculare eIF4A WT or His153Gly, donor DNAs for homology-directed repair were constructed. DNA fragments, including 2 kb genome sequences upstream and downstream of C. orbiculare eIF4A (as homology arms), the C. orbiculare eIF4A genome sequence, and the neomycin phosphotransferase II (NPTII) expression cassette, were fused into the pENTR4 plasmid (Thermo Fisher Scientific) by HiFi DNA assembly (New England Biolabs). These fragments were PCR-amplified using C. orbiculare genomic DNA, which was isolated from the mycelium, or pII99 plasmid (Namiki et al., 2001). The His153Gly substitution was induced by site-directed mutagenesis. sgRNA-targeted sequences in homology arm sequences were deleted by site-directed deletion to prevent cleavage by CRISPR-Cas9.

### Recombinant protein purification

His-tagged recombinant proteins were purified as described previously (Chen et al., 2021). BL21 Star (DE3) (Thermo Fisher Scientific) cells were transformed with pColdI plasmids (see 'Plasmid construction' section). After the induction of protein expression by isopropyl-β-D-thiogalactopyranoside (IPTG) at 15°C overnight, cells were collected by centrifugation and flash-frozen in liquid nitrogen. Subsequently, the thawed cells were lysed by sonication.

The His-tagged protein was purified by Ni-NTA agarose (QIAGEN). Eluted proteins from beads were then applied to the NGC chromatography system (Bio-Rad). Using a HiTrap Heparin HP column (1 ml, GE Healthcare), proteins were fractionated via an increased gradient of NaCl. The peak fractions were collected, buffer-exchanged with NAP-5 or PD-10 (GE Healthcare) into the storage buffer (20 mM HEPES-NaOH pH 7.5, 150 mM NaCl, 10% glycerol, and 1 mM dithiothreitol [DTT]), concentrated with a Vivaspin 6 centrifugal concentrator (10 kDa MWCO) (Sartorius), flash-frozen in liquid nitrogen, and stored at −80°C. Proteins in the SDS-PAGE gel were stained with EzStainAQua (ATTO).

### Fluorescence polarization assay

The fluorescence polarization assay was performed as previously described (Chen et al., 2021). The reaction was prepared with 0–25 μM recombinant protein, 10 nM FAM-labeled [AG]10 RNA, 1 mM AMP-PNP (Roche), 1 mM MgCl2, 20 mM HEPES-NaOH pH 7.5, 150 mM NaCl, 1 mM DTT, 5% glycerol, and 1% DMSO (as a solvent of RocA) with or without 50 μM RocA/aglafoline. After incubation at room temperature for 30 min, the mixture was transferred to a black 384-well microplate (Corning), and the fluorescence polarization was measured by an Infinite F-200 PRO (Tecan). Under ADP + Pi conditions, 1 mM ADP (Fujifilm Wako Chemicals) and 1 mM Na2HPO4 were used as substitutes for AMP-PNP. The data were fitted to the Hill equation to calculate Kd values and visualized by Igor Pro v8.01 (WaveMetrics). The affinity fold change was calculated as the fold reduction in the Kd of RocA compared to the Kd of DMSO.

### Reporter mRNA preparation

The DNA fragments PCR-amplified from psiCHECK2−7×AGAGAG motifs or psiCHECK2-CAA repeats (Iwasaki et al., 2016) were used as a template for in vitro transcription with a T7-Scribe Standard RNA IVT Kit (CELLSCRIPT). RNA was capped and poly(A) tailed with a ScriptCap m7G Capping System, a ScriptCap 2′-O-Methyltransferase Kit, and an A-Plus Poly(A) Polymerase Tailing Kit (CELLSCRIPT).

### In vitro translation assay in reconstituted system

The reconstitution system for human translation has been described previously (Iwasaki et al., 2019; Machida et al., 2018; Yokoyama et al., 2019). The in vitro translation reaction and luciferase assay were performed as previously described (Iwasaki et al., 2019) with some modifications. The final concentrations of mRNA and the eIF4A protein were 60 ng/µl and 2.16 µM, respectively. The translation mixture was incubated for 2.5 hr. The fluorescence signal was detected using the Renilla-Glo Luciferase Assay System (Promega) and measured in an EnVision 2104 plate reader (PerkinElmer).

### In vitro translation in RRL with complex-preformed mRNAs

Preformation of the eIF4A, RocA, and mRNA complex and subsequent in vitro translation in RRL were performed as previously described (Iwasaki et al., 2019; Iwasaki et al., 2016), with modifications. For preformation of the complex containing eIF4A, RocA, and reporter mRNA, 1.4 µM recombinant eIF4A, 90.9 nM reporter mRNA, and 9.1 µM RocA were incubated at 30°C for 5 min in preformation buffer (16.6 mM HEPES-NaOH pH 7.5, 55.3 mM KOAc, 2.8 mM Mg(OAc)2, 1.8 mM ATP, 0.6 mM DTT, and 0.2% DMSO). After supplementation of Mg(OAc)2 to 26.3 mM, 30 µl of the reaction was loaded into a MicroSpin G-25 column (Cytiva) equilibrated with equilibration buffer (30 mM HEPES-NaOH pH 7.5, 100 mM KOAc, 1 mM Mg(OAc)2, and 1 mM DTT), centrifuged at 700 × g for 1 min at 4°C to remove free RocA, and mixed with 2.5 μl of storage buffer (20 mM HEPES-NaOH pH 7.5, 150 mM NaCl, 10% glycerol, and 1 mM DTT). Then, 4 µl of complex-preformed mRNA was incubated with 50% RRL (Promega) in a 10 µl reaction volume for 1 hr at 30°C, according to the manufacturer’s instructions. The fluorescence signal was detected using the Renilla-Glo Luciferase Assay System (Promega) and measured with the GloMax Navigator System (Promega). In the control experiments, instead of recombinant eIF4A proteins, storage buffer was used. Moreover, recombinant eIF4A proteins were added to the G-25 flowthrough solution in place of the storage buffer.

### Fungal transformation

C. orbiculare strain 104-T (NARO GeneBank ID: MAFF 240422), a causal agent of anthracnose disease in Cucurbitaceae plants, was used. The isolated strains in this study are also listed in Supplementary file 4.

#### Preparation of protoplasts

C. orbiculare protoplasts were prepared as previously described (Kubo, 1991; Rodriguez and Yoder, 1987; Vollmer and Yanofsky, 1986) with modifications. A frozen glycerol stock of C. orbiculare was streaked on 3.9% (w/v) potato dextrose agar (PDA) medium (Nissui) in a 90 mm dish and incubated at 25°C in the dark for 3 days. Outer edges of a colony were transferred to 20 ml of 2.4% (w/v) potato dextrose broth (BD Biosciences) and incubated for 2 days at 25°C in the dark. The proliferated mycelium was collected using a 70 µm cell strainer (Corning) and incubated in 150 ml of potato-sucrose liquid medium supplemented with 0.2% yeast extract (BD Biosciences) at 25°C with shaking at 140 rpm. The mycelium was harvested, washed with sterile water, and resuspended in 20 ml of filter-sterilized (0.2 µm pore size, GE Healthcare) osmotic medium (1.2 M MgSO4 and 5 mM Na2HPO4) containing 10 mg/ml driselase from Basidiomycetes sp. (Sigma-Aldrich) and 10 mg/ml lysing enzyme from Trichoderma harzianum (Sigma-Aldrich) in a 50 ml tube (Falcon, Corning). The suspension was gently agitated in a rotary shaker at 60 rpm for 90 min at 30°C. Then, the suspension was underlaid with 20 ml of trapping buffer (0.6 M sorbitol, 50 mM Tris-HCl pH 8.0, and 50 mM CaCl2) and centrifuged at 760 × g for 5 min using a swinging-bucket rotor (Hitachi, T4SS31). Protoplasts isolated from the interface of the two layers were pelleted, washed twice using STC (1 M sorbitol, 50 mM Tris-HCl pH 8.0, and 50 mM CaCl2), resuspended in STC at 108–109 protoplasts/ml, added to a 25% volume of polyethylene glycol (PEG) solution (40% [w/w] PEG3350, 500 mM KCl, 40 mM Tris-HCl pH 8.0, and 50 mM CaCl2), and stored at −80°C until use.

#### gRNA preparation

Template DNA fragments for sgRNA in vitro transcription were PCR-amplified using the primers listed in Supplementary file 5. Using the DNA fragments, sgRNAs (sgRNAUP-1, sgRNAUP-2, sgRNADW-1, and sgRNADW-2) were prepared with a CUGA7 gRNA Synthesis Kit (Nippon Gene) following the manufacturer’s protocol.

#### Transformation

The transformation was performed as previously described (Foster et al., 2018; Kubo, 1991; Yelton et al., 1984) with modifications. The mixture of plasmid DNA (5 µg, pENTR4-C. orbiculare eIF4A WT or His153Gly), the four sgRNAs (250 ng each), and Cas9 nuclease protein NLS (15 µg, Nippon Gene) were added to 150 µl of C. orbiculare protoplasts, followed by the addition of 1 ml of STC and 150 µl of PEG solution. The resulting suspension was incubated for 20 min on ice, supplemented with 500 µl of PEG solution, and gently agitated by hand. The suspension was serially diluted with a second addition of 500 µl, a third addition of 1 ml, and fourth and fifth additions of 2 ml of PEG solution, with gentle agitation at every dilution step. After incubation for 10 min at room temperature, the PEG solution was removed by centrifugation. The protoplasts were resuspended in 1 ml of STC, diluted with 15 ml of regeneration medium (3.12% [w/v] PDA and 0.6 M glucose), and then spread onto a plate containing 40 ml of selection medium (3.9% [w/v] PDA and 0.6 M glucose) containing 200 µg/ml G418 (Fujifilm Wako Chemicals). The plate was incubated for 5 days at 25°C in the dark. The G418-resistant colonies were further seeded in fresh selection medium containing G418 and subjected to selection for an additional 5 d.

#### Screening by PCR

Then, the genomic DNA isolated from each colony was subjected to PCR to ensure the desired transformation (see Figure 3—figure supplement 1A for the design). The primers used for the PCR screening are listed in Supplementary file 5. The selected transformed conidia were suspended in 25% glycerol and stored at −80°C until use.

### Growth comparison of C. orbiculare strains

A C. orbiculare strain was seeded into 500 µl of PDA containing 0.04% (v/v) DMSO in one well of a 12-well plate with a toothpick and incubated in the dark at 25°C for 5 days. Colony sizes were measured with a ruler.

### C. orbiculare mitochondrial genome assembly

Reads from three PacBio RSII cells of the C. orbiculare 104-T whole genome sequencing (Gan et al., 2019) were mapped onto C. orbiculare scaffolds that were identified as potential mitochondrial sequences by the NCBI Genomic contamination screen with minimap2 v2.17-r941 (Li, 2018) using the map-bp setting. Aligned fasta reads were then assembled using flye v2.8.1-b1676 (Kolmogorov et al., 2019) with default settings (min overlap = 5000 bp). The assembly (GenBank accession: MZ424187) possessed a 36,318 bp contig with 2023.72× coverage and showed the highest homology to the C. lindemuthianum completed mitochondrial genome (KF953885) according to nucmer (Delcher et al., 2003). These genome data were used for data processing for ribosome profiling.

### Ribosome profiling and RNA-Seq

#### Cell culture; mycelia

Glycerol stocks of C. orbiculare eIF4AWT#1 and eIF4AH153G#1 strains were streaked on PDA in 90 mm plastic Petri dishes and incubated for 3 days. A single colony of each strain was transferred onto PDA and incubated for 3 days. The outer edges of colonies were transferred to 90 mm plastic dishes filled with 20 ml of PDB using plastic straws and incubated for 4 days. Aglafoline (0.3 or 3 µM) or DMSO was added to dishes and incubated for 6 h.

#### Cell culture; conidia

A single colony from the glycerol stocks was cultured by the same method used for mycelium preparation. The outer edges of colonies of each strain were transferred into six 300 ml flasks filled with 100 ml of PDA. Two milliliters of sterilized water was added to each flask, and the flasks were shaken well to ensure that the mycelial cells adhered to the entire surface of the PDA evenly. After 6 days of incubation in the dark, conidia generated on the surface of PDA were suspended in 20 ml of sterilized water. The conidial suspension was filtered through a 100 µm pore-size cell strainer and collected by centrifugation at 760 × g for 5 min at room temperature. Twenty milliliters of resuspended conidia at 0.5 OD600 (approximately 2.5 × 106 conidia/ml) was dispensed in 50 ml ProteoSave SS tubes (Sumitomo Bakelite) and then treated with aglafoline (0.3 or 3 µM) or DMSO for 6 h in the dark with shaking at 140 rpm.

#### Cell harvest

Cells were filtered by an MF membrane (0.45 µm pore size, Millipore), immediately scraped from the filter, and soaked in liquid nitrogen for 30 s. Then, 600 µl of lysis buffer (20 mM Tris-HCl pH 7.5, 150 mM NaCl, 5 mM MgCl2, 1 mM DTT, 100 µg/ml cycloheximide, 100 µg/ml chloramphenicol, and 1% Triton X-100) or 400 µl of TRIzol reagent (Thermo Fisher Scientific) was added dropwise into a tube containing the cell pellet and liquid nitrogen to form ice grains for ribosome profiling or RNA-Seq, respectively. The samples were stored at −80°C to evaporate the liquid nitrogen.

#### Library preparation

For ribosome profiling, the frozen cells and lysis buffer grains were milled by a Multi-beads Shocker (YASUI KIKAI) at 2800 rpm for 15 s for one cycle. The lysates were thawed on ice and centrifuged at 3000 × g and 4°C for 5 min. The supernatant was treated with 25 U/ml Turbo DNase (Thermo Fisher Scientific) for 10 min and then clarified by centrifugation at 20,000 × g and 4°C for 10 min. Then, the supernatant was used for downstream ribosome profiling library preparation as described previously (Mito et al., 2020). Briefly, the lysates containing 10 µg of total RNA were treated with 20 U RNase I (Lucigen) at 25°C for 45 min. After ribosomes were collected by a sucrose cushion, the RNAs were separated in 15% urea PAGE gels, and the RNA fragments ranging from 17 to 34 nt were excised. Subsequently, the RNAs were dephosphorylated and ligated to linkers. Following rRNA removal with a Ribo-Minus Eukaryotes Kit for RNA-Seq (Thermo Fisher Scientific), the RNA fragments were reverse-transcribed, circularized, and PCR-amplified.

For RNA-Seq, frozen cells with TRIzol grains were lysed in a Multi-beads Shocker instrument at 2800 rpm for 15 s and thawed on ice. Then, 0.5 µg of RNA extracted with a Direct-zol RNA Microprep Kit (Zymo Research) was used for library preparation. Poly(A) selection and cDNA synthesis were performed using an Illumina Stranded mRNA Prep, Ligation (Illumina), and subsequent steps were performed with a TruSeq Stranded Total RNA Library Prep Gold (Illumina).

The final DNA libraries for ribosome profiling and RNA-Seq were sequenced on a HiSeq X (Illumina) with a paired-end 150 bp option.

#### Data processing

Sequence data were processed as previously described (McGlincy and Ingolia, 2017) with modifications. For ribosome profiling, using the Fastp v0.21.0 (Chen et al., 2018) tool, sequences of reads 1 were corrected by reads 2, and quality filtering and adapter sequence removal were performed on reads 1. The adapter-removed reads 1 were split by the barcode sequence. Reads mapped to rRNA and tRNA sequences of C. orbiculare, which were predicted by RNAmmer (Lagesen et al., 2007) (http://www.cbs.dtu.dk/services/RNAmmer/) and tRNA-scan SE (Chan et al., 2021) (http://lowelab.ucsc.edu/tRNAscan-SE/) in the genome of C. orbiculare 104T (Gan et al., 2019) (PRJNA171217), using STAR v2.7.0a (Dobin et al., 2013), were removed from analysis. For all predicted tRNAs, the CCA sequence was added to the 3′ end. The remaining reads were mapped to the C. orbiculare genome (Gan et al., 2019) by STAR v2.7.0a. The A-site offset of footprints was empirically estimated to be 15 for the 19–21 nt and 24–30 nt footprints. Footprints located on the first and last five codons of each ORF were omitted from the analysis. For RNA-Seq, both reads 1 and 2 were used for analysis, and an offset of 15 was used for all mRNA fragments.

The translation efficiency change induced by aglafoline was quantified by DESeq2 (Love et al., 2014). Significance was calculated by a likelihood ratio test in a generalized linear model.

For Gene Ontology (GO) analysis, IDs of sensitive mRNAs in C. orbiculare conidia were converted to IDs of Saccharomyces cerevisiae homologs predicted using BLASTp (https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/; Camacho et al., 2009) and the S288C reference from the Saccharomyces Genome Database (SGD). A functional annotation chart for this list was obtained from DAVID (https://david.ncifcrf.gov/home.jsp; Huang et al., 2009a; Huang et al., 2009b). GO terms with a false discovery rate (FDR) of <0.05 were considered.

For 5′ UTR assignment of C. orbiculare, published RNA-Seq data (GSE178879) (Zhang et al., 2021) were aligned to the C. orbiculare genome by STAR 2.7.0a and were then assembled into transcript isoforms by StringTie v2.2.1 (Kovaka et al., 2019). The extensions upstream of the annotated start codons were assigned as the 5′ UTRs. The 5′ UTRs of transcripts expressed in conidia and mycelia were obtained separately. For analysis of the polypurine sequence in Figure 3F and Figure 3—figure supplement 3E, we used the 5′ UTR with the highest coverage in StringTie when multiple 5′ UTR isoforms were assigned.

The global translation change (i.e., the ribosome footprint change without consideration of the RNA abundance) was quantified by DESeq2 (Love et al., 2014) and renormalized to the mitochondrial footprints (as an internal spike-in standard) (Iwasaki et al., 2016).

### Fungal inoculation

Fungal inoculation was performed as previously described (Hiruma and Saijo, 2016; Kumakura et al., 2019) with modifications. Cucumber cotyledons were used for C. orbiculare inoculation. Seeds of cucumber, Cucumis sativus Suyo strain (Sakata Seed Corp.), were planted on a mix of equal amounts of vermiculite (VS Kakou) and Supermix A (Sakata Seed Corp.). Cucumbers were grown at 24°C under a 10 hr light/14 hr dark cycle using biotrons (NK Systems). Cotyledons were detached from seedlings of cucumbers and inoculated with C. orbiculare at 13 days post-germination. C. orbiculare strains (eIF4AWT#1 and eIF4AH153G#1, Supplementary file 4) were cultured on 100 ml of 3.9% PDA in a 300 ml flask at 25°C for 6 days in the dark. Conidia that appeared on the surface of PDA were suspended in 20 ml of sterilized water, filtered through cell strainers (100 µm pore size, Corning), pelleted by centrifugation at 760 × g for 5 min, and resuspended in sterilized water. The concentration of conidia was measured with disposable hemacytometers (Funakoshi) and adjusted to 105 conidia/ml with or without aglafoline (1 µM). Both conidial suspensions contained DMSO at 0.005% (v/v). Conidial suspensions were sprayed onto detached cotyledons using a glass spray (Sansho) and an air compressor (NRK Japan). Inoculated leaves were placed in plastic trays and incubated at 100% humidity for 3.5 days under the same conditions used for plant growth. Using a 6 mm trepan (Kai Medical), 6 leaf discs (LDs) were cut from each leaf, and 48 LDs were collected per sample. Six LDs were placed in a 2 ml steel top tube (BMS) with Φ5-mm zirconia beads (Nikkato), and eight tubes were prepared for each sample (n = 8). Samples were frozen in liquid nitrogen, ground at 1500 rpm for 2 min using a Shakemaster NEO (BMS), and stored at −80°C until RNA extraction.

### Quantification of fungal biomass in planta

The living fungal biomass in cucumber leaves at 3.5 days postinoculation (dpi) was measured by RT-qPCR. Relative expression levels of the C. orbiculare 60S ribosomal protein L5 gene (GenBank: Cob_v012718) (Gan et al., 2013) normalized to that of a cucumber cyclophilin gene (GenBank: AY942800.1) (Liang et al., 2018) were determined. Total RNA was extracted with the Maxwell RSC Plant RNA Kit (Promega) and Maxwell RSC 48 Instrument (Promega) with the removal of genomic DNA according to the manufacturer’s protocol. cDNA was synthesized from 500 to 1000 ng of total RNA per sample with a ReverTraAce qPCR RT Kit (TOYOBO) following the manufacturer’s instructions. All RT-qPCRs were performed with THUNDERBIRD Next SYBR qPCR Mix (TOYOBO) and an MX3000P Real-Time qPCR System (Stratagene). The primers used are listed in Supplementary file 5.

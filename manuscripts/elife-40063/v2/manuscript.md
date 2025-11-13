# Mycobacterium tuberculosis SatS is a chaperone for the SecA2 protein export pathway

## Authors

- Brittany K Miller<sup>1</sup> ([ORCID: 0000-0003-2093-4436](https://orcid.org/0000-0003-2093-4436))
- Ryan Hughes<sup>2</sup>
- Lauren S Ligon<sup>1</sup>
- Nathan W Rigel<sup>1</sup>
- Seidu Malik<sup>1</sup>
- Brandon R Anjuwon-Foster<sup>1</sup>
- James C Sacchettini<sup>2</sup>
- Miriam Braunstein<sup>1</sup> ([ORCID: 0000-0003-1180-0030](https://orcid.org/0000-0003-1180-0030)) †

### Affiliations

1. Department of Microbiology and Immunology University of North Carolina at Chapel Hill North Carolina United States
2. Department of Biochemistry and Biophysics Texas A&M University College Station United States

† Corresponding author

## Abstract

The SecA2 protein export system is critical for the virulence of Mycobacterium tuberculosis. However, the mechanism of this export pathway remains unclear. Through a screen for suppressors of a secA2 mutant, we identified a new player in the mycobacterial SecA2 pathway that we named SatS for SecA2 (two) Suppressor. In M. tuberculosis, SatS is required for the export of a subset of SecA2 substrates and for growth in macrophages. We further identify a role for SatS as a protein export chaperone. SatS exhibits multiple properties of a chaperone, including the ability to bind to and protect substrates from aggregation. Our structural studies of SatS reveal a distinct combination of a new fold and hydrophobic grooves resembling preprotein-binding sites of the SecB chaperone. These results are significant in better defining a molecular pathway for M. tuberculosis pathogenesis and in expanding our appreciation of the diversity among chaperones and protein export systems.

## Introduction

With 1.7 million deaths from tuberculosis in 2016, Mycobacterium tuberculosis continues to have a significant impact on world health (World Health Organization, 2017). For M. tuberculosis to cause disease, the bacillus must export effector proteins to the host-pathogen interface. These effectors enable M. tuberculosis to grow in macrophages and avoid clearance by the host immune response (Awuh and Flo, 2017). At least some of these effectors are exported by M. tuberculosis via the specialized SecA2 export pathway (Sullivan et al., 2012).

The mechanism of SecA2 export remains poorly understood. SecA2 is a paralog of the SecA ATPase of the general Sec protein export pathway. The general Sec pathway transports preproteins with N-terminal signal sequences across the inner membrane through a channel comprised of SecY, SecE and SecG proteins (Brundage et al., 1990). Preproteins must be in an unfolded state to travel through the SecYEG channel and, in Gram-negative bacteria, the SecB chaperone binds a subset of preproteins to maintain them in an unfolded translocation competent state. Following export across the membrane, the signal sequence is cleaved and the mature protein is released (Tsirigotaki et al., 2017). While all bacteria possess an essential Sec pathway that carries out the majority of protein export, only mycobacteria and a subset of Gram-positive bacteria possess specialized Sec export systems that are defined by a second SecA (Bensing et al., 2014; Miller et al., 2017). In these organisms, SecA1 is the name given to the canonical SecA and the specialized SecA is named SecA2. For the mycobacterial SecA2 system, the housekeeping SecYEG channel, and possibly SecA1, as well, are also involved (Ligon et al., 2013; Prabudiansyah et al., 2015). However, SecA1 and SecA2 are functionally distinct, as shown by their inability to compensate for the loss of one another (Braunstein et al., 2001; Rigel et al., 2009), and it remains unclear how SecA2 functions to export its relatively small and specific subset of proteins.

Here, we carried out a suppressor screen using a dominant negative secA2 K129R mutant of Mycobacterium smegmatis, a fast-growing model mycobacteria, as a means to identify new components of the mycobacterial SecA2 pathway. The K129R substitution is in the ATP binding site of SecA2, and past studies lead to a model where SecA2 K129R is defective for SecA2-dependent export but still able to interact with its normal binding partners that include SecYEG (Rigel et al., 2009; Ligon et al., 2013). As a result, SecA2 K129R disrupts SecYEG channels at the membrane, which hinders both general Sec and specialized SecA2 export as evidenced by more severe phenotypes of secA2 K129R than a ΔsecA2 null mutation (Ligon et al., 2013). A large collection of secA2 K129R suppressor mutations mapped to msmeg_1684, a gene of unknown function that we renamed satS for SecA2 (two) Suppressor. SatS is also present in M. tuberculosis and, remarkably, the M. tuberculosis satS gene is in an operon with the gene encoding SapM, which is a secreted phosphatase exported by the SecA2 pathway (Zulauf et al., 2018).

Here, we demonstrated that SatS, which we revealed is required for M. tuberculosis growth in macrophages, functions in the export of SapM and an additional subset of the proteins exported by the SecA2 pathway. We further identified properties of SatS that indicate a function as a protein export chaperone that protects its substrates from inappropriate interactions in the cytoplasm and additionally assists in their export. Finally, we determined the structure of the C-domain of SatS (SatSC), which reveals a new fold lacking similarities to any solved chaperone structures, yet contains surface hydrophobic grooves resembling those of the SecB chaperone. The identification of SatS expands our understanding of SecA2 export in mycobacteria and provides another example of the diversity of molecular chaperones across biological systems.

## Results

### satS suppressors of secA2 K129R

A secA2 K129R mutant of M. smegmatis exhibits more exacerbated phenotypes (i.e. azide sensitivity and poor growth on Mueller-Hinton agar) than a ΔsecA2 deletion mutant (Ligon et al., 2013) (Figure 1A). Starting with cultures of ∆secA2 expressing the secA2 K129R allele on an integrating plasmid (this strain is referred to as secA2 K129R from hereon), we collected spontaneous suppressor mutants that restored growth on Mueller-Hinton agar. Whole-genome sequencing of six extragenic suppressors revealed mutations in the same gene msmeg_1684 (Figure 1B). Three additional suppressors with mutations in msmeg_1684 were identified by directly sequencing the msmeg_1684 gene and upstream sequence in our pool of suppressors (Figure 1B). Msmeg_1684 is a highly acidic protein (pI 3.83) of unknown function with conserved homologs in all mycobacterial species, as well as other actinomycetes (Marmiesse et al., 2004). However, no homologous proteins exist outside of actinomycetes and Msmeg_1684 does not have any conserved domains to predict function. Henceforth, we refer to msmeg_1684 as satS (secA2 (two) suppressor).

![Figure 1.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig1-v2.jpg)

**Figure 1.:** (A) Mueller-Hinton growth phenotypes and azide sensitivity of M. smegmatis ∆secA2 mutant expressing wild-type secA2 (∆secA2 +psecA2), an empty vector, or secA2 K129R (secA2 K129R), and two representative suppressors. (B) Nine suppressor mutations affected satS (msmeg_1684). Red stars indicate approximate locations of mutations. For panels C, D, E and F, wild-type M. smegmatis mc2155, ∆secA2, secA2 K129R, ∆satS/secA2 K129R, and ∆satS/secA2 K129R complemented with satSMsm or satSMtb were used. (C) Mueller-Hinton growth phenotypes and azide sensitivity of the strains described above. (D) Whole cell lysates (WCL), subcellular envelope (ENV) and soluble (SOL) fractions were separated by SDS-PAGE, and SecA2 protein was detected by Immunoblot. (E) Densitometry was used to quantify SecA2 levels in the soluble and envelope fractions (ImageJ). Percent localization to a given fraction for SecA2 is reported as the percentage of the total (soluble +envelope). Error bars indicate the standard error of the mean of three independent experiments. (E) Subcellular fractions were separated by SDS-PAGE and SecY protein was detected by Immunoblot. All results shown are representative of at least three independent experiments.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Liquid cultures of M. smegmatis mc2155 and ΔsatS were grown in 96-well plates with a starting cell count of 1 × 104 cells/well. After 24 hr, resazurin was added and relative fluorescence units (RFU) were measured over the next 20 hr. Polyclonal antibodies against SatS were generated in rabbits and used to localize SatS in M. smegmatis mc2155 by Immunoblot, using the ∆satS mutant as a control for specificity. GroEL and MspA were used to validate the purity of the fractions.

Seven of the nine suppressor mutations in satS were expected to be loss-of-function mutations (i.e frameshifts or truncations). To validate that loss of satS suppresses secA2 K129R phenotypes, we deleted satS in the secA2 K129R mutant background. For future experiments, we also constructed a ∆satS mutant in a secA2+ background. The ∆satS mutant had no in vitro growth defect compared to wild-type M. smegmatis mc2155 (Figure 1—figure supplement 1A). Deletion of satS suppressed the exacerbated phenotypes of secA2 K129R, and the suppression phenotype of ΔsatS could be complemented by adding back a copy of satS from M. smegmatis (Figure 1C). Complementation was also successful with the M. tuberculosis satS homolog rv3311 indicating that SatS function is conserved in M. smegmatis and M. tuberculosis (Figure 1C).

Unlike wild-type SecA2, which is predominantly in the cytoplasm, the majority of SecA2 K129R is localized to the membrane-containing cell envelope fraction, consistent with SecA2 K129R being trapped in a non-functional complex with SecYEG (Rigel et al., 2009). We assessed the ability of ∆satS to suppress the mislocalization of SecA2 K129R using immunoblot analysis of envelope (cell wall and membrane) and soluble (cytoplasm) fractions with SecA2 antibodies. Total SecA2 K129R levels were unchanged in the ∆satS background (Figure 1D). However, the absence of SatS suppressed the aberrant localization of SecA2 K129R (i.e. in the ∆satS/secA2 K129R strain) such that SecA2 K129R was now primarily localized to the cytoplasm, similar to wild-type SecA2 (Figure 1D and E). We immunoblotted for the cell wall MspA porin and the cytoplasmic GroEL protein as fractionation controls (Figure 1—figure supplement 1B). SecA2 K129R is also associated with reduced levels of SecY, which is a presumed mechanism to eliminate jammed SecA2 K129R-SecYEG channels (Ligon et al., 2013). When we immunoblotted fractions from the ∆satS/secA2 K129R strain with SecY antibodies, we observed that the absence of SatS suppressed the SecA2 K129R effect on SecY. Both the rescued localization of SecA2 K129R and SecY levels observed in the ∆satS mutant could be complemented by introduction of satSMsm (Figure 1D, E and F). These results indicate that SatS is required for SecA2 K129R retention at the membrane in non-productive complexes with SecYEG. By extension, these results suggest a role for SatS in the SecA2 export pathway.

### SatS is required for export of the SecA2-dependent SapM phosphatase

In M. tuberculosis, the gene encoding SatS is immediately downstream of the gene encoding SapM. Reverse transcriptase (RT) PCR performed on RNA from wild-type M. tuberculosis strain H37Rv was used to demonstrate that sapM and satS are in an operon (Figure 2—figure supplement 1). This genomic arrangement is striking as SapM, a secreted phosphatase of M. tuberculosis is exported by the SecA2 pathway (Zulauf et al., 2018). While SapM does not have an ortholog in M. smegmatis, we identified 26 mycobacterial species in which the sapM-satS gene arrangement is conserved (Wattam et al., 2017).

We constructed a ∆satS mutant of M. tuberculosis H37Rv to test if SatS is required for SapM secretion. The ∆satS mutant of M. tuberculosis did not exhibit an in vitro growth defect (Figure 2—figure supplement 2A). We monitored SapM secretion into culture media by immunoblotting culture filtrate proteins (CFPs) prepared from H37Rv, the ∆secA2 mutant, the ∆satS mutant, and the ∆satS mutant complemented with satSMtb using SapM antibodies. As expected, a SapM secretion defect was observed in the ∆secA2 mutant. Even more striking was the SapM secretion defect of the ∆satS mutant, which was reproducibly more severe than the ∆secA2 mutant (Figure 2A). This phenotype could be partially complemented with a satSMtb plasmid that produced 26% of wild type levels of SatS (Figure 2A and Figure 2—figure supplement 3A). As controls, we immunoblotted the CFPs for detection of Mpt32, which is exported in a SecA2-independent manner and was not affected in the ∆satS mutant (Figure 2A), and also for the cytoplasmic SigA protein to rule out cell lysis contaminating the culture filtrates (Figure 2—figure supplement 3B). Since SapM is a phosphatase, we also quantified SapM secretion by measuring phosphatase activity in the culture filtrates, using p-Nitrophenyl Phosphate (PNPP) as a substrate. Consistent with the immunoblot data, there was significantly less phosphatase activity in the supernatant of a ∆secA2 mutant compared to H37Rv, the ∆satS mutant exhibited an even more severe reduction in secreted phosphatase activity, and the ∆satS mutant phenotype could be complemented (Figure 2B). These results extend our identification of SatS as a SecA2 suppressor by revealing a role of SatS in the SecA2-dependent secretion of SapM by M. tuberculosis.

![Figure 2.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig2-v2.jpg)

**Figure 2.:** (A) Equal protein from culture supernatants from M. tuberculosis H37Rv, ∆secA2, ∆satS and the complemented strain (∆satS +psatSMtb) were immunoblotted for SapM and Mpt32. (B) Phosphatase activity in triplicate culture supernatant samples was examined by quantifying cleavage of pNPP. Rates of pNPP cleavage were normalized to H37Rv. (C) Equal protein from culture supernatants from M. smegmatis mc2155, ∆secA2, ∆satS and the complemented strain (∆satS +psatSMsm) were examined for levels of SapM and Mpt32 by Immunoblot (D) Whole cell phosphatase activity assay in M. smegmatis. All strains are expressing SapM, SapM lacking its signal sequence (∆ss-SapM), or an empty vector as indicated. Triplicate wells containing 2 × 105 cells/well were grown in a 96 well plate for 24 hr at 37°C before measuring phosphatase activity by quantifying cleavage of pNPP. Rates were normalized to mc2155 +SapM. (E) Equal protein levels from whole cell lysates prepared from the same cultures as used for panel A or (F) the soluble, cytoplasmic fraction of M. tuberculosis H37Rv, ∆secA2, ∆satS and the complemented strain (∆satS +psatSMtb) were immunoblotted for SapM and SigA. (G) Equal protein levels from whole cell lysates of prepared from the same cultures as used for panel C were immunoblotted for SapM and GroEL. Densitometry of blots from three experiments was performed (ImageJ). Percent difference of the mean intensity relative to wild-type is reported below each immunoblot. All data are representative of at least three independent experiments and all error bars represent standard deviation of the mean of three independent replicates for each strain. n.s. – no significant difference; *, p<0.05; **, p<0.01; ***, p<0.001; ****, p<0.0001 by ANOVA and Tukey’s post hoc test.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Visualization of the operon structure of sapM and satS and the location of the primers used. Primer set FR flanking the intergenic region between sapM and satS and a control primer set in the housekeeping gene sigA were used to amplify M. tuberculosis H37Rv RNA in the presence or absence of RT.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) The ΔsatS mutant of M. tuberculosis and the parental H37Rv strain were grown in liquid 7H9 medium with ADS supplementation. Growth was monitored by measuring optical density (OD600) over time. Polyclonal antibodies against SatS were generated in rabbits and used to localize SatS in M. tuberculosis H37Rv by Immunoblot, using the ∆satS mutant as a control for specificity. SigA, PhoS1 and HbHA were used to validate the purity of the fractions.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Equal protein from whole cell lysates of M. tuberculosis H37Rv, ∆secA2, ∆satS and the complemented strain (∆satS +psatS) were immunoblotted for SatS or SigA. (B) Equal protein from culture supernatants from M. tuberculosis H37Rv, ∆secA2, ∆satS and the complemented strain (∆satS +psatS) were immunoblotted for SapM, Mpt32, and SigA as a control for lysis. (C) Equal protein from culture supernatants from M. smegmatis mc2155, ∆secA2, ∆satS and the complemented strain (∆satS +psatSmsm) were examined for levels of SapM, Mpt32, and GroEL as a control for lysis by Immunoblot. Densitometry of blots from three experiments was performed (ImageJ). Percent difference of the mean intensity relative to wild-type is reported below each immunoblot. *p<0.05 by ANOVA and Tukey’s post hoc test.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) RNA was isolated from M. tuberculosis H37Rv and ∆satS. sapM transcript levels were measured by quantitative RT-PCR and normalized to the level of sigA transcript. Data shown are for the mean of three biological replicates. (B) Expression of the promoterless lacZ gene in pYUB76 when fused to the 170 bp region upstream of sapM, containing the putative promoter and first 15 bp of sapM, was measured in liquid medium by measuring hydrolysis of o-nitrophenyl-β-D-galactoside. The results are from a representative experiment performed in triplicate. In all experiments, the error bars represent standard deviations. n.s. – no significant difference; ***, p<0.001 when compared to H37Rv or ∆satS by ANOVA.

Even though M. smegmatis lacks a SapM orthologue, when we expressed M. tuberculosis sapM in M. smegmatis, SapM was also secreted in a SecA2 and SatS dependent manner (Figure 2C). Again, the SapM secretion defect of a ∆satS mutant was more severe than that of a ∆secA2 mutant and this phenotype could be complemented (Figure 2C). As controls we immunoblotted for secreted Mpt32, which was not affected by the ∆satS mutation (Figure 2C), and for the cytoplasmic GroEL protein to rule out cell lysis (Figure 2—figure supplement 3C). This result indicates functional conservation of SatS in M. smegmatis and M. tuberculosis, and it indicates that the more amenable M. smegmatis is a valid model for studying SatS function.

To develop a higher throughput method for monitoring SatS and SecA2-dependent export, we established a whole cell assay for measuring secreted SapM phosphatase activity from M. smegmatis grown in 96 well plates. Importantly, this assay was specific for secreted SapM; it did not detect cytoplasmic SapM, as demonstrated by background levels of phosphatase activity of a M. smegmatis strain expressing non-exported cytoplasmic SapM lacking a signal sequence (∆ss-SapM). In contrast, M. smegmatis expressing full length SapM preprotein, which is secreted, exhibited significantly greater activity (Figure 2D). When the ∆secA2 mutant and the ∆satS mutant were tested in this whole cell phosphatase assay, the results confirmed the immunoblot data. Secreted phosphatase activity was reduced in both ∆satS and ∆secA2 mutants, and the reduction was significantly more dramatic in the satS mutant (Figure 2D). The reduced activity of the ∆satS mutant could be complemented with either SatSMtb or SatSMsm (Figure 2D).

### SatS effects on cellular levels of SapM

In addition to the reduced levels of secreted SapM, the total cellular (i.e. in whole cell lysate) and cytoplasmic levels of SapM were dramatically reduced in the M. tuberculosis ∆satS mutant compared to H37Rv, the ∆secA2 mutant and the complemented ∆satS strains (Figure 2E and F). Notably, the reduction observed in the ∆satS mutant differed from a modest intracellular reduction of SapM in the ∆secA2 mutant, and was specific to SapM as the levels of SigA were comparable across strains (Figure 2E and F). The same results were obtained with SapM-expressing M. smegmatis strains (Figure 2G). In M. smegmatis, GroEL was used as a loading control and is comparable across strains (Figure 2G).

The reduced cellular and cytoplasmic levels of SapM in the ∆satS mutant might have reflected transcriptional or translational effects of SatS on sapM. Alternatively, SatS might act post-translationally to stabilize SapM prior to its export. Using quantitative Real-Time PCR (qRT-PCR) (Figure 2—figure supplement 4A) and a translational sapM’-‘lacZ fusion (Figure 2—figure supplement 4B), we ruled out the possibilities of SatS functioning in transcription or translation. Thus, the effect of SatS on SapM levels in the cytoplasm was post-translational, which leaves the most likely role for SatS being to protect SapM protein prior to export.

### Mce proteins exported by the SecA2 pathway require SatS

We also tested if SatS had an effect on additional SecA2 substrates. Multiple protein components of Mce transporters, which import lipids, depend on SecA2 to be exported to the cell wall (Feltcher et al., 2015). Immunoblot analysis of M. tuberculosis samples with Mce1A and Mce1E antibodies revealed that the levels of Mce1A and 1E were reduced in cell wall of a ∆satS mutant (Figure 3A), with the defect in the ∆satS mutant again being more severe than the ∆secA2 mutant. Mce importers are conserved in M. smegmatis and similar results were obtained upon immunoblotting M. smegmatis cell wall fractions with a Mce1D antibody (Figure 3B). The same effect was seen when a Mce4AMsm-HA protein was expressed in M. smegmatis (Figure 3B). In contrast to these results, the level of the SecA2-independent 19 kDa lipoprotein in M. tuberculosis and MspA porin in M. smegmatis were unchanged in cell wall fractions of ∆satS mutants (Figure 3A and B). Like SapM, total cellular levels of Mce1A and Mce1E were also reduced in the M. tuberculosis ∆satS mutant compared to H37Rv, the ∆secA2 mutant and the complemented ∆satS strain (Figure 3C).

![Figure 3.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig3-v2.jpg)

**Figure 3.:** (A) Equalized cell wall fractions of M. tuberculosis H37Rv, ΔsecA2, ΔsatS and complemented (ΔsatS +psatSMtb) strains were analyzed by immunoblot using Mce1A, Mce1E, and 19 kDa antibodies to monitor differences in protein levels. (B) Equalized M. smegmatis mc2155, ΔsecA2, ΔsatS, and ΔsatS +psatSMsm cell wall fractions were analyzed by immunoblot using Mce1D, HA (Mce4A-HA), and MspA antibodies. (C) Equalized protein from whole cell lysates of M. tuberculosis H37Rv, ∆secA2, ∆satS and the complemented strain (∆satS +psatSMtb) were immunoblotted for Mce1A, Mce1E, and 19 kDa. (D) Equalized cell wall fractions of M. tuberculosis H37Rv, ΔsecA2, and ΔsatS strains were analyzed by immunoblot using PknG, PhoS1, and 19 kDa antibodies. (E) Equalized M. smegmatis mc2155, ΔsecA2, and ΔsatS, cell wall fractions were analyzed by immunoblot using HA (Msmeg1704-HA) and MspA antibodies. Densitometry of blots from three experiments was performed (ImageJ). Percent difference of the mean intensity relative to wild-type is reported below each immunoblot. *, p<0.05 by ANOVA and Tukey’s post hoc test.

We next tested whether SatS contributes to export of the SecA2-dependent protein kinase PknG and solute binding protein PhoS1 of M. tuberculosis, as well as the solute-binding protein Msmeg1704 of M. smegmatis (Feltcher et al., 2013; Feltcher et al., 2015; van der Woude et al., 2014). Immunoblotting of cell wall fractions confirmed that PknG, PhoS1, and Ms1704 depend on SecA2 for export; however, export of these proteins was not impaired in a ∆satS mutant (Figure 3D and F). These data demonstrate a level of specificity in the exported proteins affected by SatS. SatS affects multiple, but not all, of the proteins exported by the SecA2 pathway.

### SatS is required for M. tuberculosis growth in macrophages

The dramatic reductions in export of SapM and Mce proteins in the ∆satS mutant suggested that SatS is required for the pathogenesis of M. tuberculosis. SapM functions in limiting M. tuberculosis delivery to degradative lysosomes in macrophages while Mce proteins import lipids and thereby contribute to M. tuberculosis growth in macrophages and persistence in the host (Vergne et al., 2005; Puri et al., 2013; Wilburn et al., 2018). We tested a role for SatS during growth in macrophages by infecting murine bone marrow-derived macrophages with M. tuberculosis H37Rv, the ∆secA2 mutant, ∆satS mutant, or ∆satS mutant complemented with satSMtb, and comparing intracellular growth over time. Compared to H37Rv, the ∆satS mutant demonstrated a significant defect in intracellular growth that was comparable to the previously demonstrated, attenuated phenotype of the ∆secA2 mutant, and the ∆satS mutant phenotype could be complemented (Figure 4) (Sullivan et al., 2012; Kurtz et al., 2006). Thus, like SecA2, SatS plays an important role in enabling M. tuberculosis growth in macrophages even though only a subset of SecA2 substrates are affected by SatS.

![Figure 4.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig4-v2.jpg)

**Figure 4.:** Nonactivated BMDM were infected at an MOI of one with M. tuberculosis H37Rv + EV, ΔsecA2 + EV, ΔsatS + EV, or ΔsatS + psatS, and CFU burden was monitored over the course of a 4 day infection. The fold change in CFU over the course of the 4 day macrophage infection for each strain was calculated; the points represent means of triplicate wells, and the error bars represent standard deviations (SD). *, p<0.01; when compared to H37Rv by ANOVA and Tukey’s post hoc test. Shown is a representative experiment of four independent experiments.

### SatS and SapM interact

SatS has no sequence similarity to help predict function. However, the post-translational effect of SatS on cellular SapM levels was reminiscent of protein export chaperones of Type III and Type VII secretion systems (T3SS and T7SS), which stabilize their substrates in the cytoplasm and protect them from degradation prior to assisting in their secretion (Thomas et al., 2012; Korotkova et al., 2014). Thus, we considered the possibility that SatS is a protein export chaperone for specific substrates. To perform their functions, protein export chaperones interact with their substrates.

We tested whether SatS interacts with SapM in mycobacteria using co-immunoprecipitation. Immunoprecipitations were performed from M. smegmatis strains co-expressing C-terminally tagged SapM-FLAG and C-terminally tagged SatS-HA proteins. These epitope tags did not disrupt SapM or SatS functions (Figure 5—figure supplement 1A and B).

Reasoning that it may be easier to detect a SatS-SapM interaction when SapM export was compromised, we first performed co-immunoprecipitations in a ∆secA2 mutant background. For these experiments we used a ∆secA2/∆satS double mutant expressing SatSMtb ± HA tag and SapM-FLAG and immunoprecipitated from whole cell lysates using anti-HA agarose. The resulting immunoprecipitates were analyzed by immunoblotting with FLAG antibodies to detect SapM and SatS antibodies to detect SatS. SapM-FLAG was detected in the immunoprecipitates of the samples from the strain expressing SatSMtb-HA (Figure 5A) indicating SatS and SapM interact. As a control, SapM-FLAG was not recovered when the anti-HA immunoprecipitation was performed from a strain expressing untagged SatSMtb. Using high percentage (15%) SDS-PAGE, we detected two SapM-FLAG species: a ~ 31 kDa product corresponding to full length preprotein and a ~ 29 kDa product corresponding to the cleaved exported product. We confirmed the assignment of the smaller species as mature, cleaved SapM by immunoblotting lysate from a strain expressing ∆ss-SapM-FLAG (Figure 5A). It is striking that while the smaller exported species was more abundant in the input lysate, the full length preprotein SapM was the species that co-immunoprecipitated with SatS (Figure 5A). This is consistent with SatS interacting with SapM preprotein in the cytoplasm, prior to its export and signal sequence cleavage. We investigated whether the signal sequence of SapM is required for the SatS-SapM interaction by immunoprecipitating from a strain co-expressing SatS-HA and ∆ss-SapM-FLAG. SatS-HA and ∆ss-SapM-FLAG co-immunoprecipitated indicating that the signal sequence is not required for the SatS-SapM interaction (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig5-v2.jpg)

**Figure 5.:** (A) Lysate from M. smegmatis ∆secA2/∆satS expressing SapM-FLAG and either SatSMtb-HA or SatSMtb without a tag, ∆satS expressing ∆ss-SapM-FLAG and SatSMtb-HA, or mc2155 with two empty vectors (as shown above the blot) were used for co-immunoprecipitation using anti-HA conjugated beads. Lysates (left) and immunoprecipitations (right) for each strain were probed with SatS antibody and FLAG antibody for SapM. Two different sizes of SapM-FLAG corresponding to the full-length (signal sequence-containing) and mature (cleaved signal sequence) species were detected. (B) Lysate from M. smegmatis ∆satS expressing SapM-FLAG and either SatSMtb-HA or SatSMtb without a tag were used for co-immunoprecipitation using anti-HA conjugated beads. Lysates (left) and co-immunoprecipitations (right) for each strain were probed with SatS antibody, FLAG antibody, and MspA antibody. All data are representative of at least three independent experiments.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Whole cell phosphatase activity assay of M. smegmatis strains expressing SapM-FLAG or an empty vector. The error bars represent standard deviation from the mean of three independent replicates. *, p<0.05; ***, p<0.001; ****, p<0.0001 by ANOVA. (B) Equal protein levels from whole cell lysates and culture supernatants of mc2155, ∆satS, and the HA-tagged complemented strain (∆satS +psatS HA) were examined for levels of SapM-FLAG and GroEL by Immunoblot.

We were also able to co-immunoprecipitate SapM-FLAG with SatS-HA from cell lysates of a M. smegmatis ∆satS strain expressing the same constructs (i.e. a secA2 wild-type background), although there was reproducibly less SapM-FLAG recovered when export was not inhibited (Figure 5B). Once again, the SapM preprotein species preferentially co-immunoprecipitated with SatS. To address the specificity of SatS interacting with SapM, we also immunoblotted SatS immunoprecipitates with antibody to MspA, which is a cell wall porin that is exported in a SecA2 and SatS-independent manner (Wolschendorf et al., 2007; Feltcher et al., 2013) (Figure 2F). MspA did not co-immunoprecipitate with SatS (Figure 5B).

The interaction between the preprotein species of SapM and SatS implied that SatS is a cytoplasmic protein. Using an antibody raised against SatS, we confirmed that in both M. tuberculosis and M. smegmatis SatS is cytoplasmic (Figure 2—figure supplement 2B and Figure 1—figure supplement 1B). Interestingly, SatS in M. tuberculosis and M. smegmatis migrated on SDS-PAGE at ~65 kDa rather than at its predicted molecular weight of 46 kDa. SatS purified from Escherichia coli also ran at 65 kDa (data not shown).

### SatS functions prior to SecA2

If SatS functions as a chaperone for preproteins exported by the SecA2 pathway, we predicted its role should come before the role of SecA2 in exporting SapM across the membrane. To test this order of events, we constructed a M. smegmatis ∆secA2/∆satS double mutant expressing SapM-FLAG and compared the cellular and secreted levels of SapM of the double mutant to single ∆secA2 or ∆satS mutants. If SatS acts prior to SecA2 in exporting SapM, the ∆satS mutation should be epistatic to the ∆secA2 mutation, which proved to be the case. The ∆secA2/∆satS double mutant exhibited the equivalent dramatic reduction in cellular and secreted levels of SapM as exhibited by the ∆satS mutant (Figures 6A, B and C). Further, there was no additive effect evident on the SapM secretion defect in the ∆secA2/∆satS double mutant compared to the ∆satS mutant (Figure 6B).

![Figure 6.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig6-v2.jpg)

**Figure 6.:** (A) Equal protein from culture supernatants (CFP) from M. smegmatis mc2155, ∆secA2, ∆satS, the ∆secA2/∆satS double mutant, and ∆secA2/∆satS expressing wild-type SatS (∆secA2/∆satS +psatSMsm) were examined for levels of SapM-FLAG and Mpt32, by Immunoblot. (B) Whole cell phosphatase activity assay using the above M. smegmatis strains. All strains are expressing SapM, SapM lacking its signal sequence (∆ss-SapM), or an empty vector as indicated. Rates were normalized as described above. (C) Whole cell lysates from the above M. smegmatis strains were examined for levels of SapM-FLAG and GroEL by Immunoblot. For panels A and C, densitometry of blots from three experiments was performed (ImageJ). Percent difference of the mean intensity relative to wild-type is reported below each immunoblot. All data are representative of at least three independent experiments and all error bars represent standard deviation of the mean of three independent replicates for each strain. n.s. – no significant difference; **, p<0.01; ****, p<0.0001 by ANOVA and Tukey’s post hoc test.

### SatS behaves as a chaperone to prevent SapM aggregation

The data thus far were consistent with the hypothesis that SatS functions as a chaperone for a subset of SecA2 dependent substrates. The hallmark of a chaperone is that it binds to unfolded or misfolded regions of proteins to prevent inappropriate interactions, such as aggregation (Ellis, 1997). To obtain more direct evidence for chaperone activity of SatS, we purified SatSMtb and preSapM-His (full length SapM preprotein containing the signal sequence) from E. coli and tested the ability of SatS to prevent aggregation in vitro of preSapM-His. preSapM-His was solubilized from inclusion bodies using 8 M urea, rapidly diluted into refolding buffer (150 fold), and its aggregation was followed by change in light scattering at 350 nm. In the absence of SatS, dilution of denatured preSapM-His rapidly led to the formation of light scattering aggregates (Figure 7). However, inclusion of SatS in the dilution buffer prevented preSapM-His aggregation in a dose-dependent manner (Figure 7). As controls, BSA and lysozyme did not reduce preSapM-His aggregation (Figure 7). In fact, BSA or lysozyme modestly had the opposite effect of increasing the light scattering signal. A SatS:preSapM-His molar ratio of 2.5:1 was sufficient to completely ablate preSapM-His aggregation and even a 0.5:1 ratio was sufficient to reduce aggregation by 33%. The data from this in vitro anti-aggregation assay provide strong support for SatS acting as a chaperone and for a direct interaction between SatS and SapM preprotein.

![Figure 7.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig7-v2.jpg)

**Figure 7.:** Denatured SapM-His was diluted 150 fold to a final concentration of 1 µM in 40 mM HEPES, 100 mM NaCl, pH 7.4. SapM-His aggregation was monitored by light scattered (350 nm) at 25°C in the presence or absence of SatS/SatSC or, as controls, lysozyme or BSA. A molar ratio of 2.5:1 of SatS:SapM-His could prevent SapM-His aggregation and aggregation was significantly reduced using a molar ratio of 0.5:1.

### SatS has a new fold and hydrophobic grooves that share similarity with the preprotein binding sites of the SecB chaperone

Although the amino acid sequence of SatS bears no similarity to any known chaperones, the data above support a role for SatS as a protein export chaperone. To gain further insight into SatS function, we collected diffraction quality crystals and determined the crystal structure of SatS to 2.3 Å. Upon inspection, the electron density map only corresponded to the last 185 amino acids (L237-E420) C-domain of the SatS sequence (SatSC). The molecular weight of the SatSC crystal was ~25 kDa as determined by SDS-PAGE, indicating that the protein underwent in situ proteolysis in the crystallization buffer. Further investigation revealed striking similarity between the experimentally derived SatSC secondary structure and the predicted secondary structure of the first ~180 amino acids of the N-domain of SatS (SatSN) (Figure 8—figure supplement 1A and B). The SatSC and SatSN domains are also similar in size with 41% sequence similarity at the amino acid level (Figure 8—figure supplement 1A and B). This raised the possibility that SatS is comprised of two similar domains with an intervening ~60 amino acids that is predicted to be a flexible, disordered linker (Figure 8—figure supplement 1A). Subsequently, constructs expressing SatSC or SatSN in E. coli were used to purify the individual domains to homogeneity for crystallization trials. Only SatSC yielded diffraction quality crystals diffracting to 1.4 Å resolution (Figure 8A).

![Figure 8.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig8-v2.jpg)

**Figure 8.:** (A) The overall secondary structure of SatSC. The hydrophilicity of SatSC is a colored gradient from cyan (hydrophilic) to maroon (hydrophobic). SatSC exposes ~2,900 Å2 of hydrophobic surface. The predicted primary and secondary polypeptide binding site(s) are delineated. (B) The overall secondary structure of SecB monomer (PDB ID:1QYN) (Dekker et al., 2003). The hydrophilicity of SecB is a colored gradient from cyan (hydrophilic) to maroon (hydrophobic). The primary and secondary client binding site(s) are delineated. Each SecB monomer exposes ~1,900 Å2 of hydrophobic surface for client protein interactions (Huang et al., 2016). Molecular graphics and analyses were performed with the UCSF Chimera package (Petersen et al., 2011).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) SatS is composed of two domains of similar secondary structure joined by a potential linker of 60 amino acids with little predicted secondary structure. The disordered linker region was predicted using IUPred2A (Mészáros et al., 2018). (B) Multiple sequence alignment of N-domain (SatSN) with C-domain (SatSC) without the linker region. Secondary structure elements for each domain are depicted above and below their corresponding sequence. SatSN has 22% sequence identity (highlighted in red) and 41% sequence similarity to SatSC (highlighted in yellow and red);TT - tight turn.

SatSC displays α/β secondary structure comprised of a mostly parallel, four stranded β-sheet core, flanked by seven α-helices (Figure 8A). The structure revealed a new fold sharing no similarities with any previously solved protein structure in the PDB based on DELTA-BLAST and VAST similarity searches (Boratyn et al., 2012; Madej et al., 2014). Although the overall polypeptide fold was not similar to known proteins, the surface of SatSC had pronounced electronegative charge potential that is comparable to many export chaperones, including SecB (Francis, 2010). Furthermore, the SatSC structure featured two surface localized hydrophobic grooves, mapped by the Kyte-Doolittle hydrophobicity scale (Kyte and Doolittle, 1982) (Figure 8A). These grooves bore similarity to the hydrophobic grooves on SecB (Figure 8B) that serve as primary and secondary client binding sites to regions of unfolded preproteins (Xu et al., 2000). The proximity of the smaller hydrophobic groove in SatSC (Site 2) to the larger groove in SatSC (Site 1) as well as their amino acid composition (aromatic and bulky side chains) resembled the arrangement and composition of the client binding sites of SecB. The larger of the two hydrophobic grooves in SatSC (Site 1) was comparable in size to the ~60 Å long, main binding site in SecB. Because of the similarities between SecB and SatSC, we speculated that SatSC may be sufficient to perform SatS chaperone functions. In fact, when we tested SatSC for chaperone activity in the in vitro anti-aggregation assay, SatSC alone was sufficient to ablate preSapM-HIS aggregation comparable to full length SatS (Figure 7).

### SatS has at least two separable roles in protein export

The majority of satS suppressor mutations were expected to behave like satS null mutations (Figure 1B). However, one mutation (3S) that caused a single amino acid substitution (G134D) produced wild-type levels of full length SatS protein when compared to wild-type SatS expressed from the same vector backbone (Figure 9C). Using this expression plasmid, we tested the importance of the G134 residue, which is ubiquitous in SatS homologs in mycobacteria.

![Figure 9.](https://cdn.elifesciences.org/articles/40063/elife-40063-fig9-v2.jpg)

**Figure 9.:** (A) Equal protein from culture supernatants (CFP) from M. smegmatis mc2155, ∆secA2, ∆satS and the ∆satS mutant expressing either wild-type SatS (∆satS +psatSMsm) or SatS G134D (∆satS +psatSMsmG134D) were examined for levels of SapM-FLAG and Mpt32 by Immunoblot. (B) Whole cell phosphatase activity assay of M. smegmatis strains expressing SapM. Rates were normalized as described above. (C) Equal protein from whole cell lysates (WCL) from M. smegmatis strains described above were examined for levels of SapM-FLAG, SatS and GroEL by Immunoblot. For panels A and C, densitometry of blots from three experiments was performed (ImageJ). Percent difference of the mean intensity relative to wild-type is reported below each immunoblot. (D) Lysate from M. smegmatis ∆satS expressing SapM-FLAG and either SatSMtbG134D-HA or SatSMtbG134D without a tag were used for co-immunoprecipitation using anti-HA conjugated beads. Lysates (left) and co-immunoprecipitations (right) for each strain were probed with SatS antibody and FLAG antibody. All data are representative of at least three independent experiments and all error bars represent standard deviation of the mean of three independent replicates for each strain. n.s. – no significant difference; ****, p<0.0001 by ANOVA and Tukey’s post hoc test.

We first tested if satS G134D could complement the SapM-FLAG secretion defect of the M. smegmatis ∆satS mutant by immunoblotting culture filtrates. Since satS G134D behaved like the ∆satS null mutant in suppressing secA2 K129R, we predicted that satS G134D would fail to complement the SapM secretion defect of the ∆satS mutant. Along these lines, satS G134D exhibited a SapM secretion defect. However, with either satSMsmeg G134D or satSMtb G134D the SapM secretion defect was comparable to the level of the secretion defect of the ∆secA2 mutant not a ∆satS mutant in the immunoblot and whole cell secreted phosphatase activity assays (Figure 9A and B).

We also evaluated the effect of SatS G134D on cellular SapM levels. To our surprise, satS G134D did not behave like a ∆satS mutant. Rather, it fully complemented the dramatic ∆satS reduction in SapM levels seen in whole cell lysates (Figure 9C). Furthermore, we were able to co-immunoprecipitate SatS G134D-HA and SapM-FLAG preprotein (Figure 9D) indicating that SatS G134D retains the ability to interact with SapM-FLAG. Our discovery that SatS G134D still binds SapM preprotein and maintains cellular levels of SapM, yet satS G134D exhibits a defect in SapM secretion equivalent to that of a ∆secA2 mutant, indicates that SatS has more than one role in SapM secretion by the SecA2 pathway. Moreover, these multiple functions of SatS in export can be uncoupled.

## Discussion

As with all bacterial pathogens, the protein export pathways of M. tuberculosis are critical to virulence. Here, we identified SatS, a previously uncharacterized protein of unknown function, as a new protein export factor with a role in intracellular growth of M. tuberculosis. We further discovered multiple properties of SatS that indicate a function as a protein export chaperone. As the amino acid sequence of SatS bears no similarity to chaperones and the structure of the SatSC domain reveals a new fold, SatS appears to represent a new type of protein export chaperone.

### Suppressor analysis led to the identification of SatS

Suppressor analysis is a classic approach for identifying genes in pathways, and it was used extensively in early studies of the general Sec pathway in E. coli (Bieker-Brady and Silhavy, 1992; Flower et al., 1995). Here, we carried out a suppressor screen using secA2 K129R, which encodes a variant of SecA2 that is unable to hydrolyze ATP (Rigel et al., 2009). Past studies lead to a model where SecA2 K129R is locked in a nonfunctional complex with SecY while attempting to export its substrates (Ligon et al., 2013). As a result, SecA2 K129R is trapped at the membrane and SecY proteins are degraded (Ligon et al., 2013). Our discovery that loss-of-function satS mutations suppress secA2 K129R phenotypes suggests that SatS is required for the detrimental interaction of SecA2 K129R with SecYEG to occur. In fact, deletion of satS significantly reversed SecA2 K129R retention at the membrane and the associated SecY degradation, which is consistent with avoidance of the interaction. By extension, these results support a role for SatS in enabling wild-type SecA2 to interact with the SecYEG channel.

One possibility for how SatS promotes SecA2 interactions with the SecYEG channel is that SatS is a core component of a SecA2-specific export apparatus with a function mediating the interaction between SecA2 and SecYEG. However, if SatS were to function this way, we would expect all SecA2-dependent substrates would require SatS for export, which was not the case. An alternate possibility is that in order for SecA2 to be delivered to or engage the SecYEG channel it must first be bound to a substrate in a translocation competent state and that SatS functions as a protein export chaperone that facilitates this SecA2-substrate interaction. We favor this role for SatS as it would not only help explain why phenotypes of secA2 K129R depend on the presence of SatS but it is also consistent with our identification of an interaction between SatS and SapM and the chaperone activities of SatS. However, a question raised by this model is how elimination of SatS suppresses secA2 K129R if there are also SatS-independent proteins that could interact with SecA2 K129R. The answer may be that the threshold for phenotypic suppression does not require all SecA2 K129R to be diverted from the SecYEG channel.

### SatS as a protein export chaperone

Molecular chaperones are defined by their ability to transiently bind unfolded regions of proteins and, thereby, protect them from inappropriate interactions, such as aggregation, incorrect/premature folding or degradation (Ellis, 1997). Chaperones are a common component of protein export systems, with SecB of the general Sec pathway in Gram-negative bacteria and Type III Secretion System Chaperones (T3SCs) being examples. In mycobacteria, EspG proteins of Type VII Secretion Systems are the only protein export chaperones identified so far (Daleke et al., 2012; Ekiert and Cox, 2014). As a subset of molecular chaperones, protein export chaperones have additional functions in export, such as targeting substrates to export machinery. Although there is a notable lack of amino acid and structural similarity between different types of protein export chaperones, commonalities exist. Protein export chaperones are all highly acidic (pI <5.0) proteins that transiently interact with their substrates in the cytoplasm and remain in the cytoplasm when the substrate is exported (Randall and Hardy, 2002; Thomas et al., 2012; Ekiert and Cox, 2014). Additionally, a hallmark of a protein export chaperone is that its role is limited to a subset of the proteins exported by a given system (Collier et al., 1990; Thomas et al., 2005; Daleke et al., 2012). Finally, in some cases, the genes encoding the chaperone and substrate are co-expressed and in an operon (Parsot et al., 2003; Daleke et al., 2012).

SatS has many features of a protein export chaperone. SatS is a highly acidic (pI 3.83), cytoplasmic protein with a role promoting export of a subset of the proteins exported by the SecA2 pathway. Further, the satS and sapM genes are co-transcribed in an operon and we obtained evidence of a SatS:SapM interaction occurring in mycobacteria. SatS preferentially interacted with the full-length preprotein of SapM indicating that the interaction occurs in the cytoplasm prior to SapM export. However, like other protein export chaperones (T3SCs, SecB, and EspG5) (Stebbins and Galán, 2001; Huang et al., 2016; Ekiert and Cox, 2014) where binding occurs in regions of the mature domain of the substrate, the signal sequence was not required for the SatS-SapM interaction. The in vitro anti-aggregation effect of SatS on SapM preprotein provided the most direct proof of a SatS:SapM interaction and a chaperone function for SatS. Finally, in the absence of SatS, the level of SapM in the cytoplasm was dramatically reduced. This effect of SatS on intracellular SapM levels is post-translational and is also reminiscent of effects of T3SCs and EspG chaperones (Thomas et al., 2005; Korotkova et al., 2014).

In comparison to the dramatic reduction in intracellular SapM in the ∆satS mutant, the ∆secA2 mutant exhibited only a modest effect on intracellular SapM levels. This difference in intracellular SapM levels translates to the more severe secretion defect of the ∆satS mutant versus the ∆secA2 mutant. Export defects of mycobacterial ∆secA2 mutants are never 100% (i.e. residual export is observed in ∆secA2 mutants) (Braunstein et al., 2001; van der Woude et al., 2014; Feltcher et al., 2015; Zulauf et al., 2018). The pathway responsible for the residual export in a ∆secA2 mutant remains unknown although the general Sec pathway involving SecA1 is an attractive candidate. Thus, it is possible that SatS also works with SecA1 and the general Sec pathway, at least when SecA2 is absent. Moreover, we cannot rule out the possibility that there are SatS substrates that are exported in a completely SecA2-independent manner. Additional studies will be required to address these unknowns.

Because of the dramatically reduced levels of SapM in the whole cell lysate of the ΔsatS mutant, it was not immediately clear if the role of SatS in SapM secretion was solely to maintain intracellular levels of SapM preprotein or if SatS had additional roles. By evaluating the satS G134D mutant, we revealed the existence of at least one additional role for SatS in promoting SapM secretion. In the satS G134D mutant, intracellular SapM was maintained at wild-type levels; yet, there remained a SapM secretion defect. It is noteworthy that the SapM secretion defect of the satS G134D mutant was on the order of a ∆secA2 mutant, which is consistent with SatS G134 working in the SecA2 pathway. Future studies should address this second function, which could be a role for SatS in targeting substrates to the SecA2 pathway and/or in maintaining SapM in an unfolded state for protein translocation across SecYEG.

### The SatS structure defines a new fold with hydrophobic grooves typical of substrate binding sites

Although we set out to solve the structure of SatS in its entirety, we were only able to obtain structural information for the C-terminal half of the protein (SatSC), which arose during crystallization. However, the primary sequence and secondary structure similarity between the N-terminal and C-terminal halves of SatS raise the possibility of SatS being comprised of tandem SatSC-like domains. Investigation of the SatSC structure revealed a large network of negatively charged amino acids surrounding two surface exposed hydrophobic grooves, which are similar in arrangement, shape and size to the hydrophobic client binding sites of a SecB monomer (Huang et al., 2016). In the solution structure of SecB in complex with a preprotein, the unfolded preprotein wraps around the SecB tetramer through interactions with the hydrophobic client binding sites. This binding architecture helps explain the means by which SecB maintains Sec preproteins in an unfolded state, as is required for their transport through the SecYEG channel (Tsirigotaki et al., 2017). The similarity in hydrophobic grooves in SatS and SecB is intriguing since SatS works with the SecA2 pathway, which also uses the SecYEG channel. Moreover, these similarities suggest that the hydrophobic grooves in SatS may serve as similar substrate binding sites. In fact, in the anti-aggregation assay the SatSC domain was sufficient for preventing SapM preprotein aggregation, indicating that SatSC is capable of directly interacting with SapM preprotein. Mycobacteria lack a canonical SecB protein export chaperone, although in M. tuberculosis there is a SecB-like protein that functions as a chaperone for a toxin-antitoxin system (Bordes et al., 2011). Thus, even though SecB and SatS are not evolutionarily conserved, it is interesting to speculate a SecB-like function for SatS. SatS may be an adaptation for export of specific proteins by Actinomycetales, since SatS orthologs are not found outside of this order.

### SatS is required for growth of M. tuberculosis in macrophages

Prior TraSH/Tnseq analyses using pooled libraries of transposon mutants predicted SatS to be required during murine and macrophage infections (Rengarajan et al., 2005; Zhang et al., 2013); however, this prediction had never been validated. Here, using a ∆satS mutant and a complemented strain, we directly demonstrated a role for SatS in M. tuberculosis growth in macrophages. These data argue for an important role of SatS and its specific substrates in pathogenesis. Given that only a subset of SecA2 substrates are affected by SatS, future studies should include investigation of SatS substrates and their contribution to pathogenesis. Since our approach for identifying SatS substrates was not exhaustive, there may also exist SatS-dependent proteins that remain to be identified.

### Conclusion

By way of a genetic screen in M. smegmatis, we identified a new protein SatS with roles in protein export in M. tuberculosis. This work not only expands our understanding of the specialized SecA2 protein export pathway of mycobacteria but it provides important functional information for a previously uncharacterized M. tuberculosis protein that contributes to pathogenesis. Further, by assigning a chaperone function to SatS, our studies expand our appreciation of the diversity of chaperones in biological systems. Although chaperones have common functions, substantial structural diversity exists among these proteins, which is further highlighted by the new fold revealed in the structure of SatSC.

## Materials and methods

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
      <td>Strain, Mycobacterium tuberculosis</td>
      <td>MBTB508; (WT Mtb)</td>
      <td>Zulauf et al., 2018</td>
      <td></td>
      <td>M. tuberculosis wild-type H37Rv + Ev (pMV306.kan)</td>
    </tr>
    <tr>
      <td>Strain, M. tuberculosis</td>
      <td>MBTB443</td>
      <td>Zulauf et al., 2018</td>
      <td></td>
      <td>∆secA2 + Ev (pMV306.kan)</td>
    </tr>
    <tr>
      <td>Strain, M. tuberculosis</td>
      <td>MBTB512</td>
      <td>this paper</td>
      <td></td>
      <td>∆satS + Ev (pMV306.kan)</td>
    </tr>
    <tr>
      <td>Strain, M. tuberculosis</td>
      <td>MBTB513</td>
      <td>this paper</td>
      <td></td>
      <td>∆satS + psatS (pBM13)</td>
    </tr>
    <tr>
      <td>Strain, Mycobacterium smegmatis</td>
      <td>mc2155; (WT Msm)</td>
      <td>Snapper et al., 1990</td>
      <td></td>
      <td>M. smegmatis wild-type (WT)</td>
    </tr>
    <tr>
      <td>Strain, M. smegmatis</td>
      <td>NR116</td>
      <td>Rigel et al., 2009</td>
      <td></td>
      <td>∆secA2</td>
    </tr>
    <tr>
      <td>Strain, M. smegmatis</td>
      <td>BAF1</td>
      <td>this paper</td>
      <td></td>
      <td>∆secA2/∆satS</td>
    </tr>
    <tr>
      <td>Strain, M. smegmatis</td>
      <td>BM10</td>
      <td>this paper</td>
      <td></td>
      <td>∆satS</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMtb US flank F</td>
      <td>this paper</td>
      <td>GCGGTACCGCCGTGGGTCAACTTCAGTAAC</td>
      <td>Contains engineered KpnI site, used to amplify US flank for pSM42</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMtb US flank R</td>
      <td>this paper</td>
      <td>GCGTCTAGAGGTGCTGATGATCTCGTCGATG</td>
      <td>Contains engineered XbaI site, used to amplify US flank for pSM42</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMtb DS flank F</td>
      <td>this paper</td>
      <td>GCGAAGCTTATGATCGACCGATCTTCCTG</td>
      <td>Contains engineered HindIII site, used to amplify DS flank for pSM42</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMtb DS flank R</td>
      <td>this paper</td>
      <td>GCGACTAGTCGGGCTGTTTTCTACGTTGT</td>
      <td>Contains engineered SpeI site, used to amplify DS flank for pSM42</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMsm US flank F</td>
      <td>this paper</td>
      <td>AACATATGCGCAACTGGGTGTGCCGTATCACTG</td>
      <td>Contains engineered NdeI site, used to amplify US flank for pLL50</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMsm US flank R</td>
      <td>this paper</td>
      <td>AAGCTAGCAGCAGCCATGCGGCACAGCCTAAC</td>
      <td>Contains engineered NheI site, used to amplify US flank for pLL50</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMsm DS flank F</td>
      <td>this paper</td>
      <td>ATGCTAGCTCCCGGCTCCGTCAGGAGTAGCG</td>
      <td>Contains engineered NheI site, used to amplify DS flank for pLL50</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSMsm DS flank R</td>
      <td>this paper</td>
      <td>AACATATGAGCCACCCGGCGAAATTGAAGCCAC</td>
      <td>Contains engineered NdeI site, used to amplify DS flank for pLL50</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>1684-F-Native</td>
      <td>this paper</td>
      <td>AGTTAATTAACGTGTGCTCGACGGCCTGGTTGCC</td>
      <td>Contains engineered PacI site, used to construct satSMsm plasmids pBM4, pBM22, and pBM23</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>1684 R</td>
      <td>this paper</td>
      <td>AATGGCCACTACTCCTGACGGAGCCGGGACTCCAC</td>
      <td>Contains engineered BalI site, used to construct satSMsm plasmids pBM4 and pBM22</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>1684 R-HA</td>
      <td>this paper</td>
      <td>ATTGGCCATCAGGCGTAGTCCGGCACGTCGTACGGGTACTCCTGACGGAGCCGGGACTCCAC</td>
      <td>Contains engineered HA tag and BamHI site, used to construct satSMsm-HA plasmid pBM23</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Rv3311-F</td>
      <td>this paper</td>
      <td>AATGGCCACTGACCTCGTACCCATCCGCTTGAG</td>
      <td>Contains engineered MscI site, used to construct satSMtb plasmids pBM13, pBM60, and pBM80</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Rv3311-R</td>
      <td>this paper</td>
      <td>AATGGCCACTAGCCTTCGCCGGCTGAC</td>
      <td>Contains engineered MscI site, used to construct satSMtb plasmid pBM80</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Rv3311-HA-R</td>
      <td>this paper</td>
      <td>TTAAGCTTCGCGCCTGAGCCGCGACTCC</td>
      <td>Contains engineered HindIII site, used to construct satSMtb plasmids pBM13 and pBM60</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Rv3311-G134D-F</td>
      <td>this paper</td>
      <td>GCCCAGGATGGGATTGTCGTTGAAGAACTTCGA</td>
      <td>Used for site directed mutagenesis on pBM80 to generate pBM87</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Rv3311-G134D-R</td>
      <td>this paper</td>
      <td>TCGAAGTTCTTCAACGACAATCCCATCCTGGGC</td>
      <td>Used for site directed mutagenesis on pBM80 to generate pBM87</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>SapM-F</td>
      <td>this paper</td>
      <td>TGGCCAACCGCGGAATCCAGGCTCTC</td>
      <td>Contains engineered MscI site, used to construct sapM plasmids pJTS130, and pBM56</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Dss-SapM-F</td>
      <td>this paper</td>
      <td>TGGCCAAGACCTTCGCGCACGTGG</td>
      <td>Contains engineered MscI site, used to construct sapM plasmids pJTS132 and pBM61</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>SapM-R</td>
      <td>this paper</td>
      <td>AAGCTTCCATGCGGCACAGAATAGCGAC</td>
      <td>Contains engineered HindIII site, used to construct sapM plasmids pJTS130 and pJTS132</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>SapM-FLAG-R</td>
      <td>this paper</td>
      <td>ACTAAGCTTTCACTT GTCGTCGTCGTCCTTGTAGTCCGTATACGAGCCGCCGTCGCCCCAAATATCG</td>
      <td>Contains engineered linker-FLAG and HindIII site, used to construct sapM plasmids pBM56 and pBM61</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>SapM-Promoter F</td>
      <td>this paper</td>
      <td>ACTGGTACCTTCACGCAGCGTGGTCAGTC</td>
      <td>Used with EcoRI site in TOPO to construct sapM-lacZ reporter pBM94</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>PsapM-LacZ R</td>
      <td>this paper</td>
      <td>AGGATCCATTCCGCGGAGCATGCCGGGAG</td>
      <td>Contains engineered BamHI site to construct sapM-lacZ reporter pBM94</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>SapM-3311 gap F</td>
      <td>this paper</td>
      <td>GACGGGTTATGCGACCAATG</td>
      <td>Amplify the region between sapM and satS for RT-PCR</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>SapM-3311 gap R</td>
      <td>this paper</td>
      <td>CTCAAGCGGATGGGTACGAG</td>
      <td>Amplify the region between sapM and satS for RT-PCR</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Mce4A hsp60 F</td>
      <td>this paper</td>
      <td>AAGATATCCGAACGGAAACGCCAAACG</td>
      <td>Contains engineered EcoRV site, used to construct mce4AMsmeg-HA plasmids pBM44</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>Mce4A hsp60 R</td>
      <td>this paper</td>
      <td>TAAGCTTCGTCCCTTTCCGCGAAC</td>
      <td>Contains engineered HindIII site, used to construct mce4A Msmeg-HA plasmids pBM44</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>sigA RT F</td>
      <td>this paper</td>
      <td>AAGCGAACAGCGGCGAAGTC</td>
      <td>qRT-PCR primer for sigA</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>sigA RT R</td>
      <td>this paper</td>
      <td>TTCGGGATGGTGCTGGTCGTAG</td>
      <td>qRT-PCR primer for sigA</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>sapM RT F</td>
      <td>this paper</td>
      <td>ATCGTTGCTGGCCTCATGG</td>
      <td>qRT-PCR primer for sapM</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>sapM RT R</td>
      <td>this paper</td>
      <td>AGGGAGCCGACTTGTTACC</td>
      <td>qRT-PCR primer for sapM</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>sapM E. coli F</td>
      <td>this paper</td>
      <td>GTCTCTCCCATGC TCCGCGGAATCCAG</td>
      <td>Used to express sapM in the E. coli pMSCG -28 vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>sapM E. coli R</td>
      <td>this paper</td>
      <td>GGTTCTCCCCAGCGTCGCCCCAAATATCGGTTATTGG</td>
      <td>Used to express sapM in the E. coli pMSCG-28 vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satS E. coli F</td>
      <td>this paper</td>
      <td>TTTTTTCATATGGTTGCTGACCTCGTACCCATC</td>
      <td>Contains engineered NdeI site, used to express satS in E. coli Pet28b vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satSC E. coli F</td>
      <td>this paper</td>
      <td>TTTTTTCATATGCGGGACTTCTGGTTGCAG</td>
      <td>Contains engineered NdeI site, used to express satSC in E. coli Pet28b vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (primers)</td>
      <td>satS/satSC E. coli R</td>
      <td>this paper</td>
      <td>TTTTTTAAGCTTCT ATTCGCGCCTGAGCC</td>
      <td>Contains engineered HindIII site, used to express satS/satSC in E. coli Pet28b vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pMV261.kan</td>
      <td>Stover et al., 1991</td>
      <td></td>
      <td>Multicopy mycobacterial vector with hsp60 promoter (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pMV361.kan</td>
      <td>Stover et al., 1991</td>
      <td></td>
      <td>Single-copy mycobacterial vector with hsp60 promoter, integrates in mycobacteriophage L5 attB site (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pMV306.kan</td>
      <td>Stover et al., 1991</td>
      <td></td>
      <td>Single-copy, promoterless mycobacterial vector, integrates in mycobacteriophage L5 attB site (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pJSC77</td>
      <td>Glickman et al., 2000</td>
      <td></td>
      <td>Multicopy mycobacterial vector, HA tag cloned into pMV261 (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pLL2</td>
      <td>Ligon et al., 2013</td>
      <td></td>
      <td>single-copy mycobacterial shuttle vector, integrates in mycobacteriophage Tweety attB site (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pYA810</td>
      <td>Gibbons et al., 2007</td>
      <td></td>
      <td>Integrating M. smegmatis secA2 complementation plasmid in pMV361.kan (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pNR25</td>
      <td>Rigel et al., 2009</td>
      <td></td>
      <td>Integrating M. smegmatis secA2 K129R in pMV361.kan (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pLL50</td>
      <td>this paper</td>
      <td></td>
      <td>Suicide vector pMP62 containing flanking regions to delete satSMsm (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM11</td>
      <td>this paper</td>
      <td></td>
      <td>Suicide vector pMP62 containing secA2Msm and flanking regions to reintroduce secA2 to the BAF1 strain (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM4</td>
      <td>this paper</td>
      <td></td>
      <td>satSMsm under native promoter in pLL2 (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM80</td>
      <td>this paper</td>
      <td></td>
      <td>satSMtb under hsp60 promoter in pLL2 (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pSM42</td>
      <td>this paper</td>
      <td></td>
      <td>satSMtb upstream and downstream flanks inserted into pYUB854 (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pSM45</td>
      <td>this paper</td>
      <td></td>
      <td>Phasmid for knocking out satSMtb (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pSM60</td>
      <td>this paper</td>
      <td></td>
      <td>Phage for knocking out satSMtb (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM13</td>
      <td>this paper</td>
      <td></td>
      <td>satSMtb under hsp60 promoter in pMV306.kan (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pJTS130</td>
      <td>Zulauf et al., 2018</td>
      <td></td>
      <td>sapM under hsp60 promoter in pMV261.kan (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pJTS132</td>
      <td>this paper</td>
      <td></td>
      <td>∆ss-sapM under hsp60 promoter in pMV261. kan (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pYUB76</td>
      <td>Barletta et al., 1992</td>
      <td></td>
      <td>Multicopy mycobacterial shuttle vector with promoterless lacZ gene (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM94</td>
      <td>this paper</td>
      <td></td>
      <td>psapM-sapM’-‘lacZ in pYUB76 (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM56</td>
      <td>this paper</td>
      <td></td>
      <td>sapM under hsp60 promoter in pMV261.kan containing a C-terminal linker and FLAG tag (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM60</td>
      <td>this paper</td>
      <td></td>
      <td>satSMtb under hsp60 promoter in pLL2 containing a C-terminal HA tag (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM61</td>
      <td>this paper</td>
      <td></td>
      <td>∆ss-sapM under hsp60 promoter in pMV261.kan containing a  C-terminal linker and FLAG tag (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM22</td>
      <td>this paper</td>
      <td></td>
      <td>satSMsm under native promoter in pLL2 amplified from suppressor 3S to contain the G134D point mutation (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM23</td>
      <td>this paper</td>
      <td></td>
      <td>satSMsm under native promoter in pLL2 amplified from suppressor 3S to contain the G134D point mutation and containing a C-terminal HA tag (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM87</td>
      <td>this paper</td>
      <td></td>
      <td>satSMtb under hsp60 promoter in pLL2 with point mutation G134D generated by site directed mutagenesis (HygR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pBM44</td>
      <td>this paper</td>
      <td></td>
      <td>Mce4AMsm under hsp60 promoter in pJSC77 containing a C-terminal HA tag (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pHSG58</td>
      <td>Gibbons et al., 2007</td>
      <td></td>
      <td>Multi-copy Ms1704-HA expression vector under hsp60 promoter (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pRH1</td>
      <td>this paper</td>
      <td></td>
      <td>sapM in the E. coli pMSCG-28 vector containing a C terminal His tag (CarbR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pRH2</td>
      <td>this paper</td>
      <td></td>
      <td>satS in E. coli Pet28b vector (KanR)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (plasmids)</td>
      <td>pRH3</td>
      <td>this paper</td>
      <td></td>
      <td>satSC in E. coli Pet28b vector (KanR)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-SatS</td>
      <td>this paper</td>
      <td>rabbit polyclonal raised against SatSMtb: PA6753 for Mtb and PA6754 for Msm</td>
      <td>(1:20,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-SapM</td>
      <td>Vergne et al., 2005</td>
      <td></td>
      <td>Provided by Vojo Deretic; (1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-Mce1A</td>
      <td>Feltcher et al., 2015</td>
      <td></td>
      <td>Provided by Chris Sassetti; (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-Mce1E</td>
      <td>Feltcher et al., 2015</td>
      <td></td>
      <td>Provided by Chris Sassetti; (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-Mce1D</td>
      <td>Perkowski et al., 2016</td>
      <td></td>
      <td>Provided by Chris Sassetti; (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-19kDa</td>
      <td>Feltcher et al., 2015</td>
      <td></td>
      <td>Provided by Douglas Young; (1:20,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-PhoS1</td>
      <td>NIH Biodefense and Emerging Infections Research Resources Repository, NIAID</td>
      <td>Cat. #: IT23</td>
      <td>(1:20,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-PknG</td>
      <td>Feltcher et al., 2015</td>
      <td></td>
      <td>Provided by Yossef Av-Gay; (1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-SecA2</td>
      <td>Rigel et al., 2009</td>
      <td></td>
      <td>(1:20,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-SigA</td>
      <td>Feltcher et al., 2015</td>
      <td></td>
      <td>Provided by Murty Madiraju; (1:15,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-MspA</td>
      <td>Feltcher et al., 2013</td>
      <td></td>
      <td>Provided by Michael Niederweis; (1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-SecY</td>
      <td>Ligon et al., 2013</td>
      <td></td>
      <td>(1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-Mpt32</td>
      <td>NIH Biodefense and Emerging Infections Research Resources Repository, NIAID</td>
      <td>Cat. #: NR-13807</td>
      <td>(1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-FLAG</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #: F7425</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-FLAG</td>
      <td>Sigma-Aldrich</td>
      <td>clone M2</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclona l anti-HA</td>
      <td>Sigma-Aldrich</td>
      <td>clone HA-7</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-HIS</td>
      <td>Abgent</td>
      <td>Cat. #: AM1010a</td>
      <td>(1:20,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Mouse IgG</td>
      <td>Bio-Rad</td>
      <td>Cat. #: 1721011</td>
      <td>(1:25,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Rabbit IgG</td>
      <td>Bio-Rad</td>
      <td>Cat. #: 1706515</td>
      <td>(1:25,000)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>p-Nitrophenyl Phosphate (PNPP)</td>
      <td>NEB</td>
      <td>Cat. #: P0757</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>https://imagej.nih.gov/ij/</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Graphpad Prism 7</td>
      <td>https://www.graphpad.com/ scientific-software/prism/</td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Plasmids, bacterial strains, and culture conditions

For plasmid construction, PCR products were amplified with primers described in the Key Resources Table, ligated into TOPO cloning vectors (Invitrogen, Carlsbad, CA), digested with restriction enzymes, and ligated into their final vectors. Final vectors are described in the Key Resources Table. In all cases, newly constructed plasmids were verified by sequencing and diagnostic digests. In the case of SatS G134D plasmids, satSMsm was amplified by PCR from the 3S suppressor and satSMtb G134D was designed using site directed mutagenesis (SDM) on the satSMtb complementation plasmid pBM81. Amino acid G134 was confirmed to be highly conserved in mycobacterial SatS homologs using ConSurf (Ashkenazy et al., 2016).

M. tuberculosis and M. smegmatis strains are described in the Key Resources Table. For all experiments in this study, wildtype and mutant strains had empty vector plasmids to enable comparison to complemented strains. M. tuberculosis was grown at 37°C in Middlebrook 7H9/7H11 supplemented with 1x albumin dextrose saline (ADS), 0.5% glycerol and 0.025% Tween 80. M. smegmatis was grown at 37°C or 30°C in Middlebrook 7H9/7H10 or Mueller-Hinton medium. Media were supplemented with 0.5% glycerol plus 0.2% glucose (7H9/7H10 medium only) and 0.05% Tween 80 (all media). For all mycobacteria, the antibiotics kanamycin (20 µg/mL) and hygromycin B (50 µg/mL) were added as needed. E. coli strains were grown at 37°C in Miller LB broth or on Miller LB agar. The antibiotics kanamycin (40 µg/mL) and hygromycin B (150 µg/mL) were added as needed.

M. smegmatis growth was monitored using resazurin. At an OD600 nm of 1, cells were diluted to 105 c.f.u. ml−1 in the same medium and 100 µl were added to 96-well plates. After 24 hr of growth at 37°C, resazurin (12.5 µg ml−one final concentration; Sigma-Aldrich, St. Louis, MO) was added and fluorescence with excitation at 530 nm and emission at 590 nm was monitored over time. M. tuberculosis growth was monitored by measuring the optical density (OD600) of liquid broth cultures over time.

### Suppressor collection and sequencing

The suppressor screen was performed as described previously (Ligon et al., 2013). Suppressors of the secA2 K129R allele were isolated by plating independently grown cultures of the secA2 K129R strain onto Mueller-Hinton agar at 37°C. Genomic DNA from six suppressors was submitted for whole genome sequencing at the High-Throughput Sequencing Facility at the University of North Carolina at Chapel Hill. Sequencing was performed using Illumina GA II technology. Reads were aligned to the M. smegmatis mc2155 reference genome (NCBI RefSeq accession number NC_008596.1) using SOAP (Li et al., 2008).

### M. smegmatis mutant construction

The M. smegmatis unmarked ∆secA2/∆satS double mutant was created by two-step allelic exchange using plasmid pLL50 in the ∆secA2 mutant strain NR116, resulting in strain BAF1. Briefly, the suicide plasmid pLL50, containing a hygromycin-resistance selectable marker, a sacB counter-selectable marker, and flanking regions for satS was transformed into M. smegmatis. Transformants were selected by plating on media containing hygromycin B. Hygromycin-resistant transformants were grown to saturation, diluted 1:100 in media lacking hygromycin B, and then grown overnight at 37°C. Bacteria in which a second recombination event occurred were selected by plating on 7H10 supplemented with 0.2% glucose and 4.5% sucrose. BAF1 was assessed for the desired chromosomal deletion by PCR and Southern blot.

The M. smegmatis unmarked ∆satS single mutant was created by adding back secA2 into the BAF1 strain by two-step allelic exchange using plasmid pBM11, resulting in strain BM10. BM10 was assessed for the desired chromosomal insertion by PCR and Southern blot. Additionally, immunoblots of SecA2 were performed to ensure SecA2 levels were fully restored.

### M. tuberculosis mutant construction

The satS deletion mutant was created in H37Rv using the specialized transducing phage system as previously described (Braunstein et al., 2001). Briefly, cosmid pSM42 was created by subcloning satS upstream and downstream flanks into pYUB854 surrounding the hygromycin cassette. Cosmid pSM42 was ligated into phAE159 to generate recombinant phasmid pSM45. The recombinant phasmid, pSM45 was packaged into phage head using a λ in vitro packaging extract kit (Gigapack III XL, Agilent, Santa Clara, CA) and was transduced into E. coli. Phasmid DNA was electroporated into M. smegmatis mc2155 to make phage (pSM60). Transduced phage was plaque purified and amplified for high titer phage lysate. H37Rv was transduced with high phage lysate as previously described (Braunstein et al., 2001). Transductants were grown at 37°C on Middlebrook 7H10 plates containing hygromycin for 4 weeks. To confirm the satS deletion in transductants, PCR and Southern blotting were used.

### Azide sensitivity assays

Cultures were plated for azide sensitivity as previously described, by mixing 200 μL of a saturated culture with 7H9 top agar and pouring over 7H10 agar plates lacking tween in three technical replicates (Ligon et al., 2013). The diameter of the zone of inhibition was measured after two days and reported as a percentage of the entire plate diameter, yielding percent azide inhibition.

### Subcellular fractionation and immunoblotting

When whole cell lysates were prepared from the same cultures used to isolate culture filtrate proteins, exponential phase M. tuberculosis cultures grown in Sauton media without detergent were fixed in an equal volume of 10% formalin for 1 hr. Fixed cells were pelleted by centrifugation, resuspended in extraction buffer, and lysed by bead beating.

When prepared for subcellular fractionation, cultures of M. smegmatis and irradiated M. tuberculosis grown in Middlebrook 7H9 medium were isolated as previously described (Perkowski et al., 2016; Feltcher et al., 2013). Briefly, cells suspended in 1X PBS containing protease inhibitors were lysed by passage through a French pressure cell. Unlysed cells were removed by centrifugation at 3000 x g for 30 min to generate clarified whole cell lysates (WCLs). The WCLs were either spun at 100,000 x g for 2 hr to collect the cell envelope fraction containing both the cell wall and membrane (ENV) or at 27,000 x g for 30 min to pellet the cell wall fraction only (CW). The supernatant following CW isolation was spun at 100,000 x g for 2 hr to separate the membrane fraction (MEM) and collect the soluble cytoplasm-containing fraction (SOL). Protein concentrations were determined by bicinchoninic acid assay (Pierce, ThermoFisher, Waltham, MA).

Samples containing equal protein were separated by SDS-PAGE and transferred to nitrocellulose membranes. After blocking, proteins were detected using antibodies described in the Key Resources Table.αHis (Abgent, San Diego, CA) was used to detect the mycobacterial GroEL1 which has a string of endogenous histidines. αMouse and αRabbit IgG conjugated horseradish peroxidase secondary antibodies (Bio-Rad, Hercules, CA) were used and signal was detected using Western Lightning Plus-ECL chemiluminescent detection reagent (Perkin-Elmer, Waltham, MA).

### Culture filtrate protein preparation

M.M. tuberculosis culture filtrates were collected as described previously (Zulauf et al., 2018). Briefly, 200 mL cultures were grown in Sauton media at 37°C for 24 hr. The supernatants were double filtered through a 0.2 µm filter. Supernatant proteins were concentrated 200 fold using 3,000 MW cut off centrifuge filters (Amicon) by centrifugation at 3,000 rpm at 4°C. For immunoblotting, protein was precipitated overnight at 4°C with 10% trichloroethanoic acid (TCA). Protein pellets were washed with acetone, resuspended in 250 uL of 1 x SDS-PAGE buffer.

For M. smegmatis culture filtrate collection, samples were obtained as previously described (Feltcher et al., 2013). In brief, 10 mL cultures were grown without Tween 80 to an OD600 nm of 0.4 to 0.7. Supernatant was separated from cells first by centrifugation at 3000 x g and then filtration through a 0.2-μm-pore-size filter. Protein from 2 mL of supernatant was TCA precipitated as described above and then resuspended in 50 μL of 1 × SDS PAGE buffer.

### Phosphatase activity assay

SapM activity was assayed as described previously (Saleh and Belisle, 2000; Zulauf et al., 2018). In a 96 well plate, 3 µg of CFP protein was diluted with water and added to 10X buffer (1M Tris base pH 6.8) with 20 mM Sodium tartrate to reduce background phosphatase activity, and 50 mM p-nitrophenyl phosphate (pNPP) for a total volume of 200 µL (New England Biolabs, Ipswich, MA). Tartrate is an inhibitor of some phosphatases, but SapM activity is unaffected by tartrate (Saleh and Belisle, 2000). Despite the addition of tartrate, the phosphatase assay used is not specific for SapM. The residual activity in the ∆secA2 and ∆satS mutants can be attributed to SatS-independent phosphatases. The plate was incubated at 37°C in a plate reader, and the absorbance at 405 nm was measured every three minutes for four hours. Over the linear portion of the kinetic assay, we calculated the rate of pNPP conversion by calculating the slope of the line generated by plotting Abs405 nm as a function of time. These slopes were then normalized to the WT rate of change, which we set to 100%.

### Whole cell phosphatase activity assay

To perform the whole cell phosphatase activity assay, M. smegmatis strains expressing SapM (±ss) or an empty vector were grown in 7H9 medium to an OD600 of 1, pelleted, and washed once in 7H9 medium. Cells were diluted to 6.25 × 105 CFU/mL in 7H9 medium and 160 μL was added in triplicate to a 96-well plate. Plates were incubated at 37°C for 24 hr. After 24 hr, 20 μL of 10X buffer (1M Tris base pH 6.8) with 20 mM Sodium tartrate and 50 mM p-nitrophenyl phosphate (pNPP) were added to the wells for a total volume of 200 µL. The plate was incubated at 37°C in a plate reader, and the absorbance at 405 nm was measured every three minutes for four hours. We calculated the rate of pNPP conversion as described above.

### Macrophage infection

To assess M. tuberculosis survival in macrophages, 2 × 105 BMDMs from C57BL/6 mice were seeded 1 day prior to infection with M. tuberculosis (H37Rv, ∆secA2, ∆satS, or ∆satS +psatS) at an MOI of 1 as previously described (Sullivan et al., 2012; Zulauf et al., 2018). At 4 hr post infection, macrophages were washed four times and at the indicated time points were lysed with 0.1% Triton X-100. Serial dilutions of the lysates were plated on 7H11 agar plates and CFUs were counted three weeks later.

### Reverse transcriptase-PCR

To assess the operon nature of sapM and satS, RNA was extracted from mid-log phase cultures of M. tuberculosis H37Rv (see qRT-PCR for Materials and methods). Reverse transcription reaction was carried out using iScript cDNA Synthesis Kit (Bio-Rad) and random primers. PCR amplification of the intergenic regions on cDNA were performed using specific primers on sapM and satS (Key Resources Table). Controls included primers for the housekeeping gene sigA, PCR amplification from genomic DNA, and PCR amplification from RNA lacking reverse transcriptase.

### Quantitative Real-Time PCR

Triplicate M. tuberculosis cultures were grown in modified 7H9 medium to an OD600 of 1 and RNA was isolated as previously described using a chloroform-methanol and Trizol (Invitrogen) extraction (Perkowski et al., 2016; Feltcher et al., 2015). RNA samples were treated with DNase (Promega, Madison, WI) and then column purified (Zymo RNA clean and concentrator Kit, Irvine, CA). Following RNA isolation, cDNA was synthesized with random primers using the iScript cDNA Synthesis Kit (Bio-Rad). Real-time PCR was completed using 25 ng of cDNA template in triplicate technical replicates using the SensiMix SYBR and fluorescein kit (Bioline, Toronto, Canada). Transcripts were normalized to the housekeeping gene sigA. Primer sequences are provided in the Key Resources Table.

### LacZ (β-galactosidase) activity assays

LacZ activity assays in M. tuberculosis were performed using a modified protocol previously described for M. smegmatis (Ligon et al., 2013). Strains were grown in 7AGT to mid-log phase and 800 μL was pelleted. Pellets were resuspend in 800 μL Z buffer (60 mM Na2HPO4, 40 mM NaH2PO4, 10 mM KCl, 1 mM MgSO4, 50 mM β-mercaptoethanol), then lysed with 35 μL chloroform and 1 μL of 0.1% SDS by vortexing for 30 s followed by sonication. 640 µg of o-nitrophenyl-β-D-galatopyranoside was added to each reaction and mixtures were incubated for 24 min at room temperature. Reactions were terminated by addition of 400 μL of 1 M Na2CO3. Debris was removed by centrifugation at 3,000 rpm for 10 min, and the OD420 nm was read from the supernatant. LacZ activity (Miller units) was calculated by the following formula: (1000 x OD420 nm)/([reaction time in minutes] x [culture volume used in the reaction, in mL] x OD600 nm).

### SatS antiserum production

To generate polyclonal antisera against SatS, purified SatSMtb was produced in E. coli and injected into two rabbits using Titermax adjuvant (ThermoFisher). The serum from both rabbits was tested against wild-type M. tuberculosis and M. smegmatis and the ∆satS mutants for specificity. The serum from rabbit PA6753 recognizes SatSMtb but does not recognize SatSMsm and is only used for SatSMtb. The sera from rabbit PA6754 has a non-specific band at the same size as SatSMtb, but recognizes SatSMsm and is only used for SatSMsm.

### Co-immunoprecipitation

For in vivo co-immunoprecipitation, M. smegmatis cells were transformed with SatSMtb (±HA) tag and SapM-FLAG (±signal sequence). Transformed cells were grown in 50 mL of 7H9 medium to an OD600 nm of 0.5. Cells were pelleted and resuspended in 2.5 mL 1X PBS buffer containing a protease inhibitor cocktail. Cells were lysed by passage through a French pressure cell. Unlysed cells were removed by centrifugation at 3000 x g for 30 min to generate clarified whole cell lysates (WCLs). 200 μL of lysate was diluted in 1 mL of 1X PBS + protease inhibitors, added to 25 μL anti-HA agarose (Sigma-Aldrich), and mixed end to end at 4°C for 4 hr, followed by four washes with 1X PBS. The immunoprecipitated SatS-HA along with co-immunoprecipitated proteins were eluted in 25 μL of 1X SDS-PAGE buffer, run on 15% SDS-PAGE gels for 4.5 hr, transferred onto nitrocellulose membranes, and immunoblotted.

### Cloning, expression, and purification of SapM inclusion bodies (IBs)

The sapM full length gene was PCR amplified from genomic DNA of H37Rv using Phusion high-fidelity DNA polymerase and the primers sapM E. coli F and sapM E. coli R. The resulting PCR product treated with T4 polymerase and mixed with linear, T4 treated, pMSCG-28 vector, and transformed into chemically competent BL21 (DE3) cells as previously described (Eschenfeldt et al., 2010).

SapM containing a C-His6-tag and tobacco etch virus (TEV) protease cleavage site were grown in Luria-Bertani (LB) broth containing 100 µg/mL carbenicillin at 37°C to an OD of 0.8 (A600 nm). SapM expression was induced with the addition of 0.5 mM isopropyl-β-D-thiogalactoside (IPTG) and cells were grown for an additional 5 hr at 37°C. Cells were harvested and resuspended in lysis buffer (40 mM HEPES pH 7.4, 300 mM NaCl, 10 mM imidazole). Cells were broken using a high-pressure homogenizer in the presence of protease inhibitor cocktail (EMD Millipore, Burlington, MA) and centrifuged at 30,000 x g.

In order to clarify SapM IBs, a modified protocol was adopted (Palmer and Wingfield, 2004). The supernatant obtained after cell lysis was decanted and the pellet resuspended in 40 mM HEPES pH 7.4, 2% Triton X-100, 5 mM EDTA. The suspension was then homogenized using sonication for 3 cycles for 30 s each, centrifuged at 30,000 x g for 15 min, and the supernatant decanted. This was repeated three times to remove cell wall, membrane material, and lipid/membrane associated proteins. In the final step, detergent was omitted, and SapM purity of greater than 95% was confirmed via SDS-PAGE.

### Protein aggregation assay

Inclusion bodies of SapM pre protein with a 6X C-terminal His tag were denatured in 8 M urea, 40 mM HEPES pH 7.4, 100 mM NaCl, 1 mM EDTA to a final concentration of 150 µM. Denatured SapM (1 µL) was rapidly diluted into buffer (150 µL) containing 40 mM HEPES pH 7.4, 100 mM NaCl, and 1 mM EDTA. Protein aggregation was monitored in the absence or presence of SatS at 25°C by measuring light scattering in a time dependent manner using a Cary Eclipse Varian with excitation and emission at 350 nm.

### Cloning, expression, purification, and crystallization of SatS and SatSC

The satS and satSC genes were PCR amplified from genomic DNA of H37Rv using Phusion high-fidelity DNA polymerase and the primers satS E. coli F, satSC E. coli F, and satS/satSC E. coli R. The resulting PCR products were digested with NdeI and HindIII, ligated into Nde/HindIII digested Pet28b vector, and transformed into chemically competent BL21 (DE3) cells.

SatS and SatSC with a N-His6-tag and TEV protease cleavage site were grown separately in LB broth containing 50 µg/mL kanamycin at 37°C to an OD of 0.8 (A600 nm). SatS and SatSC expression was induced with the addition of 0.5 mM IPTG and cells were grown for an additional 5 hr at 37°C. Cells were harvested and resuspended in lysis buffer (40 mM HEPES pH 7.4, 300 mM NaCl, 10 mM imidazole). Cells were broken using a high-pressure homogenizer in the presence of protease inhibitor cocktail (EMD Millipore) and centrifuged at 30,000 x g. SatS and SatSC were purified using a cOmplete His-tag purification resin (Roche, Basel, Switzerland), followed by removal of the tag using TEV protease at 25°C and further purified by size exclusion chromatography using a Superdex 200 26/60 (GE Healthcare, Chicago, IL). Protein purity was greater than 95% as determined by SDS-PAGE. Protein concentration was measured spectrophotometrically at 595 nm using Bradford reagent.

Crystals of SatS (20 mg/mL) were produced after screening 768 individual conditions using sitting drop vapor diffusion method at 16°C with a 50 µL well solution and a drop consisting of 1.2 µL of 0.6 µL protein and 0.6 µL of well solution. A single diffraction quality crystal appeared within 6 months in 3.5 M ammonium sulfate and 0.1 M sodium acetate trihydrate pH 4.6. SatS was indexed into space group P212121 with the unit cell parameters a = 50, b = 51, c = 76. The unit cell was comprised of a single molecule in the asymmetric unit.

Crystals of SatSC (12 mg/mL) were produced after screening 384 individual conditions using sitting drop vapor diffusion method at 16°C with a 50 µL well solution and a drop consisting of 1.2 µL of 0.6 µL protein and 0.6 µL of well solution. Initial crystal hits were optimized using hanging drop vapor diffusion method at 16°C with a 1 mL well solution and a 4.0 µL drop consisting of random ratios of protein to well solution. The highest quality crystals appeared overnight in 3.5 M ammonium citrate pH 6.4 and continued to mature for an additional 2 weeks. SatSC indexed into space group P212121 with the unit cell parameters a = 50, b = 51, c = 76. The unit cell was comprised of a single molecule in the asymmetric unit.

### Data collection and structure determination of SatSC

X-ray diffraction data were collected from a single crystal at beamline 23-ID of the GM/CA-CAT facilities of the Advanced Photon Source, Argonne National Laboratory. The structure of SatS was solved by single-wavelength anomalous dispersion (SAD) using a Bromine (Br) derivative. The data were processed and reduced using the HKL3000 software package. A single Br site was identified using Phenix HySS, and Phenix AutoSol was used to produce the initial electron density map. Simultaneous rounds of model building and structure refinement were performed manually in Coot and Phenix Refine. Additional structures of SatSC were solved by molecular replacement using the initial structure of SatSC as a model in Phenix Phaser MR. Simultaneous rounds of model building and structure refinement were carried out in Coot and Phenix Refine.

### Statistical analyses

For comparisons between the groups for the determination of (i) phosphatase activity in the mycobacterial culture filtrates, (ii) whole cell phosphatase activity (iii) ‘lacZ reporter fusions and (iv) growth in macrophages, one-way analysis of variance (ANOVA) with the Tukey post test was employed. For the statistical analysis and generation of graphs, Prism five software (version 7; GraphPad Software Inc., CA) was used.

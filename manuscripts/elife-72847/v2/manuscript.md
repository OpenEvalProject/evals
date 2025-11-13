# Resurrecting essential amino acid biosynthesis in mammalian cells

## Authors

- Julie Trolle<sup>1</sup> ([ORCID: 0000-0002-2497-3531](https://orcid.org/0000-0002-2497-3531))
- Ross M McBee<sup>2</sup> ([ORCID: 0000-0003-1926-2863](https://orcid.org/0000-0003-1926-2863))
- Andrew Kaufman<sup>3</sup>
- Sudarshan Pinglay<sup>1</sup>
- Henri Berger<sup>1</sup>
- Sergei German<sup>1</sup>
- Liyuan Liu<sup>3</sup>
- Michael J Shen<sup>1</sup>
- Xinyi Guo<sup>5</sup>
- J Andrew Martin<sup>1</sup>
- Michael E Pacold<sup>6</sup> ([ORCID: 0000-0003-3688-2378](https://orcid.org/0000-0003-3688-2378))
- Drew R Jones<sup>7</sup>
- Jef D Boeke<sup>1</sup> ([ORCID: 0000-0001-5322-4946](https://orcid.org/0000-0001-5322-4946)) †
- Harris H Wang<sup>3</sup> ([ORCID: 0000-0003-2164-4318](https://orcid.org/0000-0003-2164-4318)) †

### Affiliations

1. Institute for Systems Genetics, Department of Biochemistry and Molecular Pharmacology, NYU Langone Health New York United States ([ROR:005dvqh91](https://ror.org/005dvqh91))
2. Department of Biological Sciences, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))
3. Department of Systems Biology, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))
4. Department of Internal Medicine, NYU Langone Health New York United States ([ROR:005dvqh91](https://ror.org/005dvqh91))
5. Department of Biology, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
6. Department of Radiation Oncology, NYU Langone Health New York United States ([ROR:005dvqh91](https://ror.org/005dvqh91))
7. Department of Biochemistry and Molecular Pharmacology, NYU Langone Health New York United States ([ROR:005dvqh91](https://ror.org/005dvqh91))
8. Department of Biomedical Engineering, NYU Tandon School of Engineering Brooklyn United States ([ROR:0190ak572](https://ror.org/0190ak572))
9. Department of Pathology and Cell Biology, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))

† Corresponding author

## Abstract

Major genomic deletions in independent eukaryotic lineages have led to repeated ancestral loss of biosynthesis pathways for nine of the twenty canonical amino acids. While the evolutionary forces driving these polyphyletic deletion events are not well understood, the consequence is that extant metazoans are unable to produce nine essential amino acids (EAAs). Previous studies have highlighted that EAA biosynthesis tends to be more energetically costly, raising the possibility that these pathways were lost from organisms with access to abundant EAAs. It is unclear whether present-day metazoans can reaccept these pathways to resurrect biosynthetic capabilities that were lost long ago or whether evolution has rendered EAA pathways incompatible with metazoan metabolism. Here, we report progress on a large-scale synthetic genomics effort to reestablish EAA biosynthetic functionality in mammalian cells. We designed codon-optimized biosynthesis pathways based on genes mined from Escherichia coli. These pathways were de novo synthesized in 3 kilobase chunks, assembled in yeasto and genomically integrated into a Chinese hamster ovary (CHO) cell line. One synthetic pathway produced valine at a sufficient level for cell viability and proliferation. 13C-tracing verified de novo biosynthesis of valine and further revealed build-up of pathway intermediate 2,3-dihydroxy-3-isovalerate. Increasing the dosage of downstream ilvD boosted pathway performance and allowed for long-term propagation of second-generation cells in valine-free medium at 3.2 days per doubling. This work demonstrates that mammalian metabolism is amenable to restoration of ancient core pathways, paving a path for genome-scale efforts to synthetically restore metabolic functions to the metazoan lineage.

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
      <td>Strain, strain background (E. coli)</td>
      <td>TransforMax EPI300</td>
      <td>Lucigen</td>
      <td>C300C105</td>
      <td>Chemically competent</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>NEB 10-beta</td>
      <td>New England Biolabs</td>
      <td>C3020K</td>
      <td>Electrocompetent</td>
    </tr>
    <tr>
      <td>Cell line (C. griseus)</td>
      <td>CHO Flp-In</td>
      <td>ThermoFisher</td>
      <td>R75807</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (C. griseus)</td>
      <td>CHO pMTIV</td>
      <td>This paper</td>
      <td></td>
      <td>Cell line maintained in J.D.Boeke lab</td>
    </tr>
    <tr>
      <td>Cell line (C. griseus)</td>
      <td>CHO pCtrl</td>
      <td>This paper</td>
      <td></td>
      <td>Cell line maintained in J.D.Boeke lab</td>
    </tr>
    <tr>
      <td>Cell line (C. griseus)</td>
      <td>CHO pMTIV-ilvD+</td>
      <td>This paper</td>
      <td></td>
      <td>Cell line maintained in J.D.Boeke lab</td>
    </tr>
    <tr>
      <td>Cell line (C. griseus)</td>
      <td>CHO pCtrl-ilvD+</td>
      <td>This paper</td>
      <td></td>
      <td>Cell line maintained in J.D.Boeke lab</td>
    </tr>
    <tr>
      <td>Cell line (C. griseus)</td>
      <td>CHO pPro</td>
      <td>This paper</td>
      <td></td>
      <td>Cell line maintained in H.H.Wang lab</td>
    </tr>
    <tr>
      <td>Cell line (C. griseus)</td>
      <td>CHO pCtrl-mCh</td>
      <td>This paper</td>
      <td></td>
      <td>Cell line maintained in H.H.Wang lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pJTR0381 (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>Encodes Ec ilvD transcription units for lentiviral transduction</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-2A peptide (mouse monoclonal)</td>
      <td>Novus Biologicals</td>
      <td>NBP2-59627</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-α/β-tubulin (rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>2148</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IRDye 800CW Anti-mouse IgG (goat polyclonal)</td>
      <td>LI-COR</td>
      <td>926–32210</td>
      <td>1:20000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IRDye 680 RD Anti-rabbit IgG (goat polyclonal)</td>
      <td>LI-COR</td>
      <td>926–68071</td>
      <td>1:20000 dilution</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PrestoBlue Cell Viability Reagent</td>
      <td>ThermoFisher</td>
      <td>A13261</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NEBNext poly(A) mRNA Magnetic Isolation module</td>
      <td>New England Biolabs</td>
      <td>E7490</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NEBNext Ultra RNA Library Prep Kit for Illumina</td>
      <td>New England Biolabs</td>
      <td>E7770</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>F-12K medium without amino acids, powder base</td>
      <td>US Biological</td>
      <td>N8545</td>
      <td>Dropout medium base</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>RPMI 1640 without amino acids &amp; glucose, powder base</td>
      <td>US Biological</td>
      <td>R9010-01</td>
      <td>Dropout medium base</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Gibco fetal bovine serum, dialyzed</td>
      <td>Fisher Scientific</td>
      <td>26400044</td>
      <td>Lot 2140178</td>
    </tr>
  </tbody>
</table>

_CHO: Chinese hamster ovary._

### Pathway completeness analysis

For pathway completeness analysis, the EC numbers of each enzyme in each amino acid biosynthesis pathway (excluding pathways annotated as only occurring in prokaryotes) were collected from the MetaCyc database (Supplementary file 4). Variant biosynthetic routes to the same amino acid were considered as separate pathways, generating distinct EC number lists. The resulting per-pathway EC number lists were checked against the KEGG, Entrez Gene, Entrez Nucleotide, and Uniprot databases using their respective web APIs for each listed organism. If the combination of all databases contained at least one complete EC numbers list, corresponding to an end-to-end complete biosynthetic pathway, the organism was considered ‘complete’ for that essential amino acid.

### Cell lines and media

CHO Flp-In cells (ThermoFisher, R75807) were used in all experiments. All cell lines tested negative for mycoplasma. For growth assays involving amino acid dropout formulations, medium was prepared from an amino acid-free Ham’s F-12 (Kaighn’s) powder base (US Biological, N8545), and custom combinations of amino acids were added back in as needed to match the standard amino acid concentrations for Ham’s F-12 (Kaighn’s) medium or as specified. Custom amino acid dropout medium was adjusted to a pH of 7.3, sterile filtered, and supplemented with 10% dialyzed Fetal Bovine Serum (Fisher Scientific, 26400044) and Penicillin-Streptomycin (100 U/mL) prior to use. For metabolomics experiments, medium was prepared from an amino acid-free and glucose-free RPMI 1640 powder base (US Biological, R9010-01), and custom combinations of amino acids and isotopically heavy glucose and sodium pyruvate were added in to match the standard amino acid concentrations for RPMI 1640 or as specified. pH was adjusted to 7.3, sterile filtered and supplemented with 10% dialyzed Fetal Bovine Serum and Penicillin-Streptomycin (100 U/mL) prior to use. Where specified, cells were cultured on plates coated with 0.1% gelatin (EMD Millipore, ES-006-B) for 30 min at room temperature. Plates were washed with PBS prior to use.

### Cell counting and quantification

For evaluating effects of amino acid dropout on cell growth curves, cells were seeded at 1×104 into 6-well plates into F12-K media with lowered amino acid concentrations relative to typical F12-K media and then allowed to grow for 5 days. Media was then aspirated off and replaced with PBS with Hoechst 33342 live nuclear stain for automated imaging and counting using a DAPI filter set on an Eclipse Ti2 automated inverted microscope. To count, an automated microscopy routine was used to Figure 5 random locations within each well at 10× magnification, and then the cells present in imaged frames counted using automatic cell segregation and counting software. Given differences in cell response to starvation, segregation and counting parameters were tuned in each experiment, but kept constant between starvation conditions and cells with and without the pathway. For synthetic prototroph pathway tests, raw cell counts were performed using the Countess II Automated Cell Counter (ThermoFisher, A27977) in accordance with the manufacturer’s protocol, or using the Scepter 2.0 Handheld Automated Cell Counter (Millipore Sigma, C85360) in accordance with the manufacturer’s protocol. Where indicated, relative cell quantification was measured using PrestoBlue Cell Viability Reagent (ThermoFisher, A13261) in accordance with the manufacturer’s protocol.

### Cell culture in conditioned medium

Conditioned medium was generated by seeding 1×106 pMTIV cells into 10 mL complete F12-K medium on 10 cm plates and replacing the medium with 10 mL freshly prepared valine-free F12-K medium the next day following a PBS wash step. Cells conditioned the medium for 2 days at which point the medium was collected, centrifuged at 300×g for 3 mins to remove potential cell debris, sterile filtered, and collected in 150 mL vats to reduce batch-to-batch variation. This 100% conditioned medium was subsequently mixed in a 1:1 ratio with freshly prepared, unconditioned valine-free medium to generate so-called 50% conditioned valine-free medium, which was used throughout the long-term culturing process of synthetic prototrophic cells without exogenous supply of valine where specified.

### DNA assembly, recovery and amplification

Integrated constructs were synthesized de novo in 3 kb DNA segments with each segment overlapping neighboring segments by 80 bp. Assembly was conducted in yeasto by co-transformation of segments into S. cerevisiae strain BY4741 made competent by the LiOAc method (Pan et al., 2007). After 2 days of selection at 30°C on SC–Ura medium, individual colonies were picked and cultured overnight. 1.5 mL of each resulting yeast culture was resuspended in 250 µl P1 resuspension buffer (Qiagen, 19051) containing RNase. Glass beads were added to each resuspension and the mixture was vortexed for 10 mins to mechanically shear the cells. Next, cells were subject to alkaline lysis by adding 250 µl of P2 lysis buffer (Qiagen, 19052) for 5 mins and then neutralized by addition of Qiagen N3 neutralization buffer (Qiagen, 19053). Subsequently, cell debris was spun down and plasmid DNA was collected using the Zymo Zyppy plasmid preparation kit (Zymo Research, D4036) according to the manufacturer’s instructions. Plasmid DNA was eluted in Zyppy Elution buffer and subsequently transformed into TransforMax EPI300 chemically competent E. coli in accordance with the manufacturer’s protocols (Lucigen, C300C105) for plasmid amplification.

### Protein extraction and western blot

Cell were lysed in SKL Triton lysis buffer (50 mM Hepes pH7.5, 150 mM NaCl, 1 mM EDTA, 1 mM EGTA, 10% glycerol, 1% Triton X-100, 25 mM NaF, 10 μM ZnCl2) supplemented with protease inhibitor (Sigma 11873580001). NuPAGE LDS sample buffer (ThermoFisher, NP0007) supplemented with 1.43  M β-mercaptoethanol was added to samples prior to heating at 70°C for 10 mins. Gel electrophoresis was performed using 4–12% Bis-Tris gels (ThermoFisher, NP0326BOX) and run in NuPAGE MOPS running buffer (ThermoFisher, NP0001). Proteins were then transferred onto a PVDF membrane (Milipore Sigma, IPFL00010) using the Biorad Trans-Blot Turbo system in accordance with the manufacturer’s instructions. The transfer membrane was blocked in Odyssey blocking buffer (LI-COR, 927–40000) for 1 hr at room temperature prior to incubation in primary antibody (Novus Biologicals, NBP2-59627 [1:1000 dilution]; Cell Signaling Technology, 2148 [1:1000 dilution]) solubilized in a 1:1 mixture of Odyssey blocking buffer and TBS-T buffer (50  mM Tris Base, 154  mM NaCl, 0.1% Tween20) overnight at 4°C. Secondary antibodies (LI-COR, 926–32210 [1:20,000 dilution]; LI-COR, 926–68071 [1:20,000 dilution]),were also solubilized in Odyssey blocking buffer / TBS-T buffer. The membrane was incubated in the secondary antibody solution for 1.5 hr at room temperature.

### Metabolomics

Cells were cultured in RPMI medium containing 13C-glucose and/or 13C-sodium pyruvate were indicated prior to cell harvest. Cell pellets were generated by trypsinization, followed by low speed centrifugation, and the pellet was frozen at –80°C until further processing. A metabolite extraction was carried out on each sample with an extraction ratio of 1e6 cells per mL (80% methanol containing internal standards, 500 nM), according to a previously described method (Pacold et al., 2016). The LC column was a Millipore ZIC-pHILIC (2.1×150 mm, 5 μm) coupled to a Dionex Ultimate 3000 system and the column oven temperature was set to 25°C for the gradient elution. A flow rate of 100 μL/min was used with the following buffers; (A) 10 mM ammonium carbonate in water, pH 9.0, and (B) neat acetonitrile. The gradient profile was as follows; 80–20%B (0–30 min), 20–80%B (30–31 min), 80–80%B (31–42 min). Injection volume was set to 1 μL for all analyses (42 min total run time per injection). MS analyses were carried out by coupling the LC system to a Thermo Q Exactive HF mass spectrometer operating in heated electrospray ionization mode (HESI). Method duration was 30 min with a polarity switching data-dependent Top 3 method for both positive and negative modes, and targeted MS2 scans for the monoisotopic, U-13C, and U-13C/U-15N valine m/z values. Spray voltage for both positive and negative modes was 3.5 kV and capillary temperature was set to 320°C with a sheath gas rate of 35, aux gas of 10, and max spray current of 100 μA. The full MS scan for both polarities utilized 120,000 resolution with an AGC target of 3e6 and a maximum IT of 100 ms, and the scan range was from 67 to 1000 m/z. Tandem MS spectra for both positive and negative mode used a resolution of 15,000, AGC target of 1e5, maximum IT of 50ms, isolation window of 0.4 m/z, isolation offset of 0.1 m/z, fixed first mass of 50 m/z, and 3-way multiplexed normalized collision energies (nCE) of 10, 35, 80. The minimum AGC target was 1e4 with an intensity threshold of 2e5. All data were acquired in profile mode. All valine data were processed using Thermo XCalibur Qualbrowser for manual inspection and annotation of the resulting spectra and peak heights referring to authentic valine standards and labeled internal standards as described.

### RNA Seq

RNA was extracted from cells using the Qiagen RNeasy Kit (Qiagen, 74104) according to the manufacturer’s protocol. QIAshredder homogenizer columns (Qiagen, 79654) were used to disrupt the cell lysates. mRNA was purified using the NEBNext poly(A) mRNA Magnetic Isolation module (New England Biolabs, E7490) in accordance with the manufacturer’s protocol. Libraries were prepared using the NEBNext Ultra RNA Library Prep Kit for Illumina (New England Biolabs, E7770), and sequenced on a NextSeq 550 single-end 75 cycles high output with v2.5 chemistry. Reads were adapter and quality trimmed with fastP using default parameters and psuedoaligned to the GCF_003668045.1_CriGri-PICR Chinese hamster genome assembly using kallisto. Differential gene enrichment analysis was performed with in R with DESeq2 and GO enrichment performed and visualized with clusterProfiler against the org.Mm.eg.db database, with further visualization with the pathview, GoSemSim, eulerr packages. Differentially expressed were considered to be statistically significant if their DEseq2 corrected expression was than or equal to the package default of p≤0.05. GO categories were considered to be statistically significantly regulated if their de/enrichment was calculated as a multiple testing corrected value of p≤0.05. For mTOR-related genes, all genes present in all GO categories containing the keyword ‘TOR’ were tested for significance with a multiple testing corrected value of p≤0.05. For ISR genes, a manually curated list of genes consisting of Eif2ak4, Eif2ak2, Atf4, Ddit3, Asns, Trib3, Nlrp1, Map1lc3b, Atg3, Atg5, Atg7, Atg10, Atg12, Atg16, Becn1, Gabarap, Gabarapl2, Sqstm1, Ddit4, Nupr1, Bcl2l11, Bbc3, Atf5, Pmaip1, Txnip were tested using a corrected value of p≤0.05.

### Lentiviral packaging

Target plasmid was maintained in and purified from NEB 10-beta electrocompetent E. coli (New England Biolabs, C3020K). Lentivirus was packaged by plating 4×106 HEK293T cells on 10 cm2 and incubating cells overnight at 37°C. Cells were transfected with a plasmid mix consisting of 3.5 µg of the target plasmid, 6.0 µg psPAX2 (Addgene, 12260), and 3.0 µg pMD2.G (Addgene, 12259) using Lipofectamine 2000 (ThermoFisher Scientific, 11668019) in accordance with the manufacturer’s instructions. Transfected HEK293T cells were incubated for 48 hr, before medium was collected, and centrifuged at 200×g for 5 mins. The resulting supernatant was filtered using a 0.45 µm filter before infection. CHO cells were plated at 20–30% confluency in and incubated overnight prior to infection. The packaged virus was applied to cells for 24 hr before the medium was exchanged for fresh medium. After another 24 hr of incubation, the medium was exchanged for fresh medium containing 10 µg/ml puromycin for 8 days.

### qPCR

gDNA and RNA were extracted from cells using the QIAamp DNA Kit (Qiagen, 51304) the Qiagen RNeasy Kit (Qiagen, 74104), respectively, in accordance with the manufacturer’s protocol. For RNA extraction, QIAshredder homogenizer columns (Qiagen, 79654) were used to disrupt the cell lysates. cDNA was generated from RNA using Invitrogen SuperScript IV Reverse Transcriptase (Invitrogen, 18090200) and oligo(dT) primers. Each qPCR reaction was performed using SYBR Green Master I (Roche, 04707516001) on a Light Cycler 480 (Roche, 05015243001) using the recommended cycling conditions. Primers were designed to amplify amplicons 150–200 bp in size.

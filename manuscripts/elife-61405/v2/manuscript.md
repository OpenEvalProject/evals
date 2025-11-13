# Cohesin mutations are synthetic lethal with stimulation of WNT signaling

## Authors

- Chue Vin Chin<sup>1</sup>
- Jisha Antony<sup>1</sup>
- Sarada Ketharnathan<sup>1</sup>
- Anastasia Labudina<sup>1</sup>
- Gregory Gimenez<sup>1</sup>
- Kate M Parsons<sup>4</sup>
- Jinshu He<sup>4</sup>
- Amee J George<sup>4</sup> ([ORCID: 0000-0002-0265-4476](https://orcid.org/0000-0002-0265-4476))
- Maria Michela Pallotta<sup>5</sup>
- Antonio Musio<sup>5</sup> ([ORCID: 0000-0001-7701-6543](https://orcid.org/0000-0001-7701-6543))
- Antony Braithwaite<sup>1</sup>
- Parry Guilford<sup>6</sup>
- Ross D Hannan<sup>4</sup>
- Julia A Horsfield<sup>1</sup> ([ORCID: 0000-0002-9536-7790](https://orcid.org/0000-0002-9536-7790)) †

### Affiliations

1. Department of Pathology, Otago Medical School, University of Otago Dunedin New Zealand
2. Maurice Wilkins Centre for Molecular Biodiscovery, The University of Auckland Auckland New Zealand
3. Genetics Otago Research Centre, University of Otago Dunedin New Zealand
4. The John Curtin School of Medical Research, The Australian National University Canberra Australia
5. Istituto di Ricerca Genetica e Biomedica (IRGB), Consiglio Nazionale delle Ricerche (CNR) Pisa Italy
6. Department of Biochemistry, University of Otago Dunedin New Zealand
7. Department of Biochemistry and Molecular Biology, University of Melbourne Parkville Australia
8. Sir Peter MacCallum Department of Oncology, University of Melbourne Parkville Australia
9. School of Biomedical Sciences, University of Queensland St Lucia Australia

† Corresponding author

## Abstract

Mutations in genes encoding subunits of the cohesin complex are common in several cancers, but may also expose druggable vulnerabilities. We generated isogenic MCF10A cell lines with deletion mutations of genes encoding cohesin subunits SMC3, RAD21, and STAG2 and screened for synthetic lethality with 3009 FDA-approved compounds. The screen identified several compounds that interfere with transcription, DNA damage repair and the cell cycle. Unexpectedly, one of the top ‘hits’ was a GSK3 inhibitor, an agonist of Wnt signaling. We show that sensitivity to GSK3 inhibition is likely due to stabilization of β-catenin in cohesin-mutant cells, and that Wnt-responsive gene expression is highly sensitized in STAG2-mutant CMK leukemia cells. Moreover, Wnt activity is enhanced in zebrafish mutant for cohesin subunits stag2b and rad21. Our results suggest that cohesin mutations could progress oncogenesis by enhancing Wnt signaling, and that targeting the Wnt pathway may represent a novel therapeutic strategy for cohesin-mutant cancers.

## Introduction

The cohesin complex is essential for sister chromatid cohesion, DNA replication, DNA repair, and genome organization. Three subunits, SMC1A, SMC3, and RAD21, form the core ring-shaped structure of human cohesin (Dorsett and Ström, 2012; Horsfield et al., 2012). A fourth subunit of either STAG1 or STAG2 binds to cohesin by contacting RAD21 and SMC subunits (Shi et al., 2020), and is required for the association of cohesin with DNA (Dorsett and Ström, 2012; Horsfield et al., 2012; Shi et al., 2020). The STAG subunits of cohesin are also capable of binding RNA in the nucleus (Pan et al., 2020). Cohesin associates with DNA by interaction with loading factors NIPBL and MAU2 (Wendt, 2017), its stability on DNA is regulated by the acetyltransferases ESCO1 (Wutz et al., 2020) and ESCO2 (van der Lelij et al., 2009), and its removal is facilitated by PDS5 and WAPL (Wutz et al., 2017; Shintomi and Hirano, 2009). The cohesin ring itself acts as a molecular motor to extrude DNA loops, and this activity is thought to underlie its ability to organize the genome (Vian et al., 2018; Mayerova et al., 2020). Cohesin works together with CCCTC-binding factor (CTCF) to mediate three-dimensional genome structures, including enhancer-promoter loops that instruct gene accessibility and expression (Hansen, 2020; Rowley and Corces, 2018). The consequences of cohesin mutation therefore manifest as chromosome segregation errors, DNA damage, and deficiencies in genome organization leading to gene expression changes.

All cohesin subunits are essential to life: homozygous mutations in genes encoding complex members are embryonic lethal (Horsfield et al., 2012). However, haploinsufficient germline mutations in NIPBL, ESCO2, and in cohesin genes, cause human developmental syndromes known as the ‘cohesinopathies’ (Horsfield et al., 2012). Somatic mutations in cohesin genes are prevalent in several different types of cancer, including bladder cancer (15–40%), endometrial cancer (19%), glioblastoma (7%), Ewing’s sarcoma (16–22%) and myeloid leukemias (5–53%) (De Koninck and Losada, 2016; Hill et al., 2016; Waldman, 2020). The prevalence of cohesin gene mutations in myeloid malignancies (Kon et al., 2013; Papaemmanuil et al., 2016; Thol et al., 2014; Thota et al., 2014; Yoshida et al., 2013) reflects cohesin’s role in determining lineage identity and differentiation of hematopoietic cells (Galeev et al., 2016; Mazumdar et al., 2015; Mullenders et al., 2015; Viny et al., 2015). Of the cohesin genes, STAG2 is the most frequently mutated, with about half of cohesin mutations in cancer involving STAG2 (Waldman, 2020).

While cancer-associated mutations in genes encoding RAD21, SMC3, and STAG1 are always heterozygous (Thota et al., 2014; Kon et al., 2013; Tsai et al., 2017), mutations in the X chromosome-located genes SMC1A and STAG2 can result in complete loss of function due to hemizygosity (males), or silencing of the wild type during X-inactivation (females). STAG2 and STAG1 have redundant roles in cell division, therefore complete loss of STAG2 is tolerated due to partial compensation by STAG1. Loss of both STAG2 and STAG1 leads to lethality (Benedetti et al., 2017; van der Lelij et al., 2017). STAG1 inhibition in cancer cells with STAG2 mutation causes chromosome segregation defects and subsequent lethality (Liu et al., 2018). Therefore, although partial depletion of cohesin can confer a selective advantage to cancer cells, a complete block of cohesin function will cause cell death. The multiple roles of cohesin provide an opportunity to inhibit the growth of cohesin-mutant cancer cells via chemical interference with pathways that depend on normal cohesin function. For example, poly ADP-ribose polymerase (PARP) inhibitors were previously shown to exhibit synthetic lethality with cohesin mutations (Waldman, 2020; Liu et al., 2018; Mondal et al., 2019; McLellan et al., 2012; O'Neil et al., 2013). PARP inhibitors prevent DNA double-strand break repair (Zaremba and Curtin, 2007), a process that also relies on cohesin function.

To date, only a limited number of compounds have been identified as inhibitors of cohesin-mutant cells (Waldman, 2020). Here, we sought to identify additional compounds of interest by screening libraries of FDA-approved molecules against isogenic MCF10A cells with deficiencies in RAD21, SMC3, or STAG2. Unexpectedly, our screen identified a novel sensitivity of cohesin-deficient cells to a GSK3 inhibitor that acts as an agonist of the Wnt signaling pathway. We found that β-catenin stabilization upon cohesin deficiency likely contributes to an acute sensitivity of Wnt target genes. The results raise the possibility that sensitization to Wnt signaling in cohesin-mutant cells may participate in oncogenesis, and suggest that Wnt agonism could be therapeutically useful for cohesin-mutant cancers.

## Results

### Cohesin gene deletion in MCF10A cells results in minor cell cycle defects

To avoid any complications with pre-existing oncogenic mutations, we chose the relatively ‘normal’ MCF10A line for creation and screening of isogenic deletion clones of cohesin genes SMC3, RAD21, and STAG2. MCF10A is a near-diploid, immortalized, breast epithelial cell line that exhibits normal epithelial characteristics (Tait et al., 1990) and has been successfully used for siRNA and small molecule screening (Telford et al., 2015). Two sgRNAs per gene were designed targeting the 5' and 3' UTR regions, respectively, of RAD21, SMC3, and STAG2 genes. Single cells were isolated and grown into clones that were genotyped for complete gene deletions (Figure 1, Supplementary file 1). We isolated several RAD21 and SMC3 deletion clones, and selected single clones for further characterization that grew normally and were essentially heterozygous. In the selected RAD21 deletion clone, one of three RAD21 alleles (on chromosome 8, triploid in MCF10A) was confirmed deleted, with one wild type and one undetermined allele. In the selected SMC3 deletion clone, one of two SMC3 alleles (on chromosome 10) was deleted. In the selected STAG2 deletion clone, homozygous loss of STAG2 was determined by the absence of STAG2 mRNA and protein. For convenience here, we named the three cohesin-mutant clones RAD21+/-, SMC3+/-, and STAG2-/-.

![Figure 1.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig1-v2.jpg)

**Figure 1.:** (A) Top, schematic diagram shows the deletion strategy for genes encoding cohesin subunits RAD21, SMC3, and STAG2 using two sgRNAs targeting the 5'UTR and the 3'UTR of each gene. Bottom, heterozygous clones were identified by PCR using specific primer pairs flanking the deletion region. Representative DNA gel shows the PCR products yielded using specific primer pairs for MCF10A parental and RAD21+/- deletion clone. M, ladder marker. (B,C,D) Schematic deletion strategy and summary of the allele sequences for the STAG2 homozygous deletion clone, and the RAD21 and SMC3 heterozygous deletion clones. (E) RNA levels of the targeted genes in MCF10A cohesin-deficient clones. (F) Representative immunoblot and (G) quantification of cohesin protein levels. γ-tubulin was used as loading control. n = 3 independent experiments, mean ±s.d., one-tailed student t test: **p≤0.01; ****p≤0.0001. Guide RNAs and PCR primers can be found in Supplementary file 1.

The RAD21+/-, SMC3+/-, and STAG2-/- clones had essentially normal cell cycle progression when compared to parental cells, although the RAD21+/- and SMC3+/- clones proliferated more slowly than the others (Figure 2A,B). Chromosome spreads revealed that only the STAG2-/- clone had noteworthy chromosome cohesion defects characterized by partial or complete loss of chromosome cohesion and gain or loss of more than one chromosome (Figure 2C,D; Figure 2—figure supplement 1A). Remarkably, SMC3+/- cells had noticeably larger nuclei that appeared to be less dense (Figure 2E,F; Figure 2—figure supplement 1B), possibly owing to decompaction of DNA in this clone. RAD21+/- and SMC3+/- clones exhibited occasional lagging chromosomes and micronuclei, while the STAG2-/- clone did not (Figure 2G; Figure 2—figure supplement 1C–E). Cell growth and morphology in monolayer culture was essentially normal in all three cohesin-mutant clones (Figure 2—figure supplement 2).

![Figure 2.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig2-v2.jpg)

**Figure 2.:** (A) Proliferation curves of MCF10A parental and cohesin-deficient clones. n = 3 independent experiments, mean ± sd, two-way ANOVA: **p≤0.01; ****p≤0.0001. Doubling times in hours of MCF10A parental cells are 15.5 ± 0.1; RAD21+/-, 17.1 ± 0.2; SMC3+/-, 21.4 ± 0.9; STAG2-/-, 16.4 ± 0.2 respectively. (B) Flow cytometry analysis of cell cycle progression. (C) Representative metaphase spread images of cohesin-deficient cells. Black arrow indicates a normal chromosome; Red arrow indicates premature chromatid separation (PCS). (D) Quantification of chromosome cohesion defects. A minimum of 20 metaphase spreads were examined per individual experiment, n = 2 independent experiments, mean ±s.d. (E) Representative confocal images of nuclear morphology. Scale bar, 15 μM. Yellow arrow indicates a micronucleus. (F) Quantification of nuclear area. (G) Quantification of micronuclei (MN). A minimum of 1000 cells was examined per individual experiment. n = 5 independent experiments (square symbols), mean ±s.d., one-way ANOVA: *p≤0.05; ****p≤0.0001. Source data is available for A,D,F,G in Figure 2—source data 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Frequency of aneuploidy in cohesin-deficient MCF10A clones compared to parental MCF10A (WT). (B) Threshold compactness in the nuclei of cohesin-deficient clones compared to wild type MCF10A (R.U. = relative units). n = 5 independent experiments (square symbols), mean ± s.d., one-way ANOVA: ***p≤0.001. (C) Representative images of abnormal interphase nuclei showing chromosome bridges, micronuclei, and lagging chromosomes at anaphase. (D) Quantification of chromosome bridges and micronuclei events in MCF10A cohesin-deficient cells. (E) Quantification of chromosome mis-segregation observed in MCF10A cohesin-deficient clones. At least 100 mitotic cells were examined per condition, n = 3 independent experiments, mean ±s.d., one-way ANOVA **p≤0.01; ***p≤0.0005; ns, not significant.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** MCF10A cells were grown in low (1000 cells/well) and high density (4000 cells/well) in 96-well plates. Cohesin-deficient cells display a cobblestone-like morphology that is similar to MCF10A parental cells (WT). Scale bar, 250 μM.

Overall, the cohesin deletion clones appear to have infrequent but specific cell cycle anomalies that are shared between some, but not all clones. Anomalies include loss of chromosome cohesion, lagging chromosomes, or micronuclei, but these features do not appear to majorly impact on cell cycle progression or morphology.

### Cohesin-depleted cells have altered nucleolar morphology and are sensitive to DNA damaging agents

Cohesin-deficient cells have been demonstrated to display compromised nucleolar morphology and ribosome biogenesis (Bose et al., 2012; Harris et al., 2014), as well as sensitivity to DNA damaging agents (Bailey et al., 2014; Mondal et al., 2019). Analysis of our RAD21+/-, SMC3+/-, and STAG2-/- clones confirmed these findings. Cohesin-deleted cells in steady-state growth had abnormal nucleolar morphology, as revealed by fibrillarin and nucleolin staining (Figure 3—figure supplement 1). Furthermore, we found that treatment with DNA intercalator/transcription inhibitor Actinomycin D caused marked fragmentation of nucleoli in all three cohesin-deficient cell lines as determined by fibrillarin staining (Figure 3A,B). Actinomycin D treatment increased γ-H2AX and TP53 in the nuclei of RAD21+/- and SMC3+/- cells, in particular, indicating that these cells are compromised for DNA damage repair relative to the parental MCF10A cells (Figure 3C–F). In contrast, immunostaining for γ-H2AX and TP53 levels were comparable at baseline between cohesin-deficient clones and parental cells. Interestingly, the STAG2-/- deletion clone was much more resistant to DNA damage caused by Actinomycin D (Figure 3C–F), even though nucleoli are abnormal in this clone (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig3-v2.jpg)

**Figure 3.:** (A) Representative image and (B) quantification of nucleolar dispersal observed in parental (WT) MCF10A cells and cohesin-deficient clones after exposure to a DNA damaging agent, Actinomycin D (ActD) 8 nM. Fibrillarin (FBL) staining was used as a marker for nucleoli. (C) Representative image and (D) quantification of DNA damage foci observed in parental (WT) MCF10A cells and cohesin-deficient clones after exposure to ActD. An antibody detecting γH2AX was used to visualize foci of DNA double-strand breaks. (E) Representative image and (F) quantification of nuclear p53 in parental (WT) MCF10A cells and cohesin-deficient clones after exposure to ActD. A minimum of 500 cells was examined per individual experiment. n = 3 independent experiments, mean ± s.d., one-way ANOVA: *p≤0.05; **p≤0.01; ***p≤0.0005. Scale bar, 15 μM. Source data is available for Figure 2B,D,F in Figure 3—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Representative images of nucleolar morphology as determined using fibrillarin (FBL) as a marker of nucleoli. (B,C) Quantification of FBL intensity and number of FBL spots per cell in each genotype. A minimum of 1000 cells was examined per individual experiment, n = 3 independent experiments, mean ± s.d., one-way ANOVA: *p≤0.05; **p≤0.01; ***p≤0.0005. (D) Types of nucleolar morphology observed in MCF10A parental cells. (E) Representative images of nucleolar morphology determined by using nucleolin (NCL) as a marker. (F) Quantification of NCL intensity per cell in each genotype. At least 500 cells were examined per individual experiment, n = 3 independent experiments, mean ±s.d., one-way ANOVA: **p≤0.01; ***p≤0.0005. (G) Quantification of NCL morphology classes present in cohesin-deficient cells. A.U., Arbitrary unit.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** STAG2- and SMC3-deficient MCF10A cells show reduced viability following 48 hr of treatment with the PARP inhibitor, Olaparib, relative to parental cells (WT). n = 2 independent experiments, mean ±s.d., one-way ANOVA: *p≤0.05.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) Summary of the allele sequences for additional RAD21 and SMC3 heterozygous clones, RAD21+/- clone two and SMC3+/- clone 2. (B) Cohesin-deficient clone 2 cells display a cobblestone-like morphology that is similar to MCF10A parental cells (WT). (C) RNA levels of the targeted genes in the additional MCF10A cohesin-deficient clones. (D) Quantification of chromosome cohesion defects in RAD21+/- clone two and SMC3+/- clone 2. A minimum of 20 metaphase spreads were examined per individual experiment, n = 2 independent experiments, mean ±s.d. (E) Trypan blue measurement of cell viability for all cohesin-deficient clones in this study. Survival rates of mutant clones under standard culture conditions are not significantly different from wild type, n = 2 independent experiments, mean ±s.d. (F) Proliferation curves of MCF10A parental and RAD21+/- clone two and SMC3+/- clone 2. (G) Dose-response curves were generated for validation of LY2090314 in RAD21+/- clone two and SMC3+/- clone two compared with MCF10A cells. For (F) and (G), n = 3 independent experiments, mean ± sd, two-way ANOVA: *p≤0.05; **p≤0.01.

Overall, increased susceptibility of RAD21+/- and SMC3+/- clones to DNA damage is consistent with cohesin’s role in DNA double-strand break repair (Sjögren and Ström, 2010), and highlights the different requirements for RAD21 and SMC3 versus STAG2 in this process. Cohesin mutations were previously shown to sensitize cells to PARP inhibitor, Olaparib (Mondal et al., 2019; Matto et al., 2015). We confirmed a mild to moderate sensitivity to Olaparib in our cohesin-deficient MCF10A clones relative to parental cells (Figure 3—figure supplement 2).

Collectively, characterization of our cohesin-deficient clones provided confidence that they represent suitable models for synthetic lethal screening. To confirm that the phenotypes of our chosen clones are representative, we selected a further two clones with heterozygous deletions in SMC3 and RAD21, and monitored their growth, morphology and chromosome cohesion (Figure 3—figure supplement 3). These analyses showed that the two additional deletion clones were similar to those already characterized (Figures 1–3), providing surety that our cohesin-deficient cell lines have properly representative phenotypes. Furthermore, none of the cohesin-deficient clones exhibited enhanced cell death compared with parental MCF10A cells (Figure 2B; Figure 3—figure supplement 3).

### A synthetic lethal screen of FDA-approved compounds identifies common sensitivity of cohesin-mutant cells to WNT activation and BET inhibition

To identify additional compounds that inhibit the growth of cohesin-deficient cells, we screened the cohesin-deficient MCF10A cell lines with five dose concentrations (1–5000 nM) of 3009 compounds, including FDA-approved compounds (2399/3009), kinase inhibitors (429/3009), and epigenetic modifiers (181/3009) (Figure 4A). DMSO and Camptothecin were included as negative and positive viability controls, respectively (Figure 4—figure supplement 1). We assayed cell viability after 48 hr of compound treatment.

![Figure 4.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig4-v2.jpg)

**Figure 4.:** (A) Schematic overview of the synthetic lethal screen. (B,C,D) Overview of the differential area over the curve (AOC) activity of all compounds tested in cohesin-deficient cell lines relative to parental MCF10A cells in the primary screen. A threshold of differential AOC ≥ 0.15 (red dashed lines) was used to filter candidate compounds of interest. (E) Venn diagram showing the number of common and unique compounds that inhibited RAD21+/-, SMC3+/-, and STAG2-/- in the primary screen. (F,G) Dose-response curves of I-BET-762 and LY2090314. Source data is available for B–E in Figure 4—source data 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) DMSO (negative control) and (B) Camptothecin (positive control) titrations were used to establish a cytotoxicity range in MCF10A cells and cohesin-deleted derivatives. n = 2 independent experiments, mean ±s.d.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Common and (B,C,D) unique categories of compounds identified in the primary screen. See Figure 4—source data 1 for details. (E,F) Dose-response curves were generated for validation of I-BET-762 and LY2090314 in MCF10A cells. (G) Dose-response curve of LY2090314 in the K562 STAG2R614* mutant cell line. Two-way ANOVA: ****p≤0.0001 Source data is available for Figure 4A–D in Figure 4—source data 2.

Synthetic lethal candidate compounds were ranked based on the differential area over curve (AOC) values that are derived from a growth rate-based metric (GR) (Figure 4B–D; Figure 4—source data 1). The GR metric takes into account the varying growth rate of dividing cells to mitigate inconsistent comparison of compound effects across cohesin-deficient cell lines (Hafner et al., 2016). Compounds that caused ≥30% growth inhibition in cohesin-deficient clones compared with parental MCF10A cells were selected for further analysis. The screen identified candidate 206 synthetic lethal compounds, of which 18 inhibited all three cohesin-deficient cell lines ≥ 30% more than the parental MCF10A cells (Figure 4E; Figure 4—source data 2; Table 1; Table 1—source data 1).

**Table 1.**
 Significant inhibitors of all three cohesin-deficient clones.Table 1—source data 1.Compounds with growth inhibitory activity (AOC) ranked to produce Table 1.Table 1—source data 2.Compounds effective in the secondary screen ranked to produce Table 1.


<table>
  <thead>
    <tr>
      <th rowspan="2">Compound</th>
      <th rowspan="2">Rank 1° screen</th>
      <th rowspan="2">Rank 2° screen</th>
      <th rowspan="2">Target</th>
      <th rowspan="2">Pathway</th>
      <th colspan="3">1° differential AOC activity</th>
    </tr>
    <tr>
      <th>RAD21+/-</th>
      <th>SMC3+/-</th>
      <th>STAG2-/-</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WAY-600</td>
      <td>1</td>
      <td>3</td>
      <td>mTORC1/2</td>
      <td>PI3K/AKT/mTOR</td>
      <td>0.30</td>
      <td>0.37</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>I-BET-762</td>
      <td>2</td>
      <td>8</td>
      <td>BET proteins</td>
      <td>Epigenetics</td>
      <td>0.25</td>
      <td>0.27</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>LY2090314</td>
      <td>3</td>
      <td>6</td>
      <td>GSK3</td>
      <td>WNT</td>
      <td>0.25</td>
      <td>0.22</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>Vistusertib (AZD2014)</td>
      <td>4</td>
      <td>1</td>
      <td>mTORC1/2</td>
      <td>PI3K/AKT/mTOR</td>
      <td>0.18</td>
      <td>0.33</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>P276-00</td>
      <td>5</td>
      <td>17</td>
      <td>CDK1/4/9</td>
      <td>Cell Cycle</td>
      <td>0.17</td>
      <td>0.29</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>MK-8745</td>
      <td>6</td>
      <td>22</td>
      <td>Aurora A</td>
      <td>Cell Cycle</td>
      <td>0.18</td>
      <td>0.30</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>Ethacridine lactate</td>
      <td>7</td>
      <td>28</td>
      <td>Anti-infection</td>
      <td>Microbiology</td>
      <td>0.18</td>
      <td>0.25</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>CUDC-101</td>
      <td>8</td>
      <td>36</td>
      <td>EGFR, HDAC, HER2</td>
      <td>Epigenetics</td>
      <td>0.16</td>
      <td>0.25</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>Dabrafenib (GSK2118436)</td>
      <td>9</td>
      <td>9</td>
      <td>BRAF</td>
      <td>MAPK</td>
      <td>0.18</td>
      <td>0.27</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>SAR131675</td>
      <td>10</td>
      <td>34</td>
      <td>VEGFR3</td>
      <td>Protein Tyrosine Kinase</td>
      <td>0.15</td>
      <td>0.17</td>
      <td>0.33</td>
    </tr>
    <tr>
      <td>ZM 447439</td>
      <td>11</td>
      <td>41</td>
      <td>Aurora A/B</td>
      <td>Cell Cycle</td>
      <td>0.16</td>
      <td>0.22</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>Gitoxigenin Diacetate</td>
      <td>12</td>
      <td>32</td>
      <td>NA</td>
      <td>Other</td>
      <td>0.17</td>
      <td>0.24</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>UNC669</td>
      <td>13</td>
      <td>62</td>
      <td>Epigenetic Reader Domain</td>
      <td>Epigenetics</td>
      <td>0.18</td>
      <td>0.23</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>4-Phenylbutyric Acid</td>
      <td>14</td>
      <td>29</td>
      <td>Endoplasmic reticulum stress</td>
      <td>Other</td>
      <td>0.20</td>
      <td>0.17</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>Ipatasertib (GDC-0068)</td>
      <td>15</td>
      <td>12</td>
      <td>AKT</td>
      <td>PI3K/AKT/mTOR</td>
      <td>0.21</td>
      <td>0.19</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td>VX-702</td>
      <td>16</td>
      <td>43</td>
      <td>P38 MAPK</td>
      <td>MAPK</td>
      <td>0.15</td>
      <td>0.19</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>RVX-208</td>
      <td>17</td>
      <td>58</td>
      <td>BET proteins</td>
      <td>Epigenetics</td>
      <td>0.16</td>
      <td>0.20</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>Dihydroergotamine mesylate</td>
      <td>18</td>
      <td>49</td>
      <td>NA</td>
      <td>Other</td>
      <td>0.16</td>
      <td>0.19</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td>Olaparib</td>
      <td>351</td>
      <td></td>
      <td>PARP1/2</td>
      <td>DNA Damage</td>
      <td>0.11</td>
      <td>0.13</td>
      <td>0.22</td>
    </tr>
  </tbody>
</table>

Most of the 206 compounds inhibited at least two cohesin-deficient cell lines and were classed in similar categories of inhibitor (Figure 4—figure supplement 2A–D; Figure 4—source data 2; Table 1). Of the 206 primary screen hits, 85 (including the 18 that inhibited all three cohesin-deficient clones, plus the most effective candidates from each inhibitor category) were subjected to secondary screening in an 11-point dose curve ranging from 0.5 nM to 10 μM. Notable sensitive pathways included: DNA damage repair, the PI3K/AKT/mTOR pathway, epigenetic control of transcription, and stimulation of the Wnt signaling pathway (Table 1; Table 1—source data 2; Figure 4—source data 2).

The identification of DNA damage repair inhibitors in our screen agrees with previous studies showing synthetic lethality of PARP inhibition with cohesin mutation (McLellan et al., 2012). Differential sensitivity of the cohesin deletion cell lines to PI3K/AKT/mTOR inhibitors is consistent with the observed nucleolar deficiencies in cohesin-mutant cells (Figure 3—figure supplement 1). The PI3K/AKT/mTOR pathway stimulates ribosome biogenesis and rDNA transcription; because rDNA is contained in nucleoli, it is likely that rDNA transcription and ribosome production is already compromised in the cohesin gene deletion cell lines. We had previously shown that BET inhibition is effective in blocking precocious gene expression in the chronic myelogenous leukemia cell line K562 containing a STAG2 mutation (Antony et al., 2020). Growth inhibition of cohesin-deficient MCF10A cells by I-BET-762 (Figure 4F; Figure 4—figure supplement 2E) reinforces the idea that targeting BET could be therapeutically effective in cohesin-mutant cancers.

Interestingly, we found that LY2090314, a GSK3 inhibitor and stimulator of the Wnt signaling pathway, inhibits all three cohesin deletion lines (Table 1, Figure 4G, Figure 4—figure supplement 2F). LY2090314 also inhibited the growth of K562 STAG2 R614* mutant leukemia cells that we had previously characterized (Antony et al., 2020; Figure 4—figure supplement 2G) as well as the two additional MCF10A RAD21- and SMC3-deficient clones (Figure 3—figure supplement 3G). Wnt signaling appears to act upstream of cohesin (Xu et al., 2014; Estarás et al., 2015), and also to be primarily downregulated downstream of cohesin mutation (Mills et al., 2018; Schuster et al., 2015; Avagliano et al., 2017). Therefore, we were prompted to further investigate why Wnt stimulation via GSK3 inhibition might cause lethality in cohesin-deficient cells.

### Stabilization of β-catenin in cohesin-deficient MCF10A cells

In ‘off’ state of canonical Wnt signaling, β-catenin forms a complex including Axin, APC, GSK3, and CK1 proteins. β-catenin phosphorylated by CK1 and GSK3 is recognized by the E3 ubiquitin ligase β-Trcp, which targets β-catenin for proteasomal degradation. Activation of Wnt signaling by ligand binding, or by GSK3 inhibition, releases β-catenin, allowing it to accumulate in the nucleus where it binds TCF to activate Wnt target gene transcription (Logan and Nusse, 2004; Clevers et al., 2014). We found that there was no difference in GSK3 levels between parental MCF10A cells and the cohesin-deficient clones, and upon treatment of cells with LY2090314, levels of GSK3 were reduced in all cells as expected (Figure 5—figure supplement 1). In contrast, in untreated cells we found that β-catenin is stabilized in all three cohesin-deficient clones compared with parental MCF10A cells. When Wnt signaling is in the ‘off’ state, phospho-Ser33/37/Thr41 marks β-catenin targeted for degradation. Membrane-associated phospho-Ser33/37/Thr41-β-catenin was increased in cohesin-deficient clones, and disappeared upon treatment with LY2090314 (Figure 5A). Phospho-Ser675 β-catenin, the active form of β-catenin that is induced upon Wnt signaling, was noticeably increased in the cytoplasm of cohesin-deficient cells following treatment with LY2090314 (Figure 5B,C). The results imply that inactive β-catenin that would normally be targeted for degradation is instead stabilized in cohesin-deficient cells, and is available to be converted into the active form following inhibition of GSK3.

![Figure 5.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig5-v2.jpg)

**Figure 5.:** (A) Immunoblot of the membrane fraction of parental (WT) and cohesin-deficient MCF10A cells shows increased basal level of β-catenin phosphorylation at Ser33/37/Thr41. (B) Immunoblot of the cytoplasmic fraction shows increased level of both total and phosphorylated β-catenin at Ser675 after parental (WT) and cohesin-deficient MCF10A cells were treated with LY2090314 at 100 nM for 24 hr. (C) Quantification of protein levels for total and phosphorylated β-catenin at Ser675. n = 3 independent experiments, mean ± s.d., one-way ANOVA: *p≤0.05, **p≤0.01. (D) Immunofluorescence images show cytosolic accumulation of active β-catenin in cohesin-deficient MCF10A cells treated with LY2090314 100 nM for 24 hr, relative to parental (WT) MCF10A cells. White arrows indicate puncta of β-catenin (pSer675). Scale bar = 25 μM. Full length blots and molecular size markers are available for A,B in Figure 5—source data 1. Source quantification data is available for C in Figure 5—source data 2.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Anti-GSK3 immunoblot of membrane fraction from parental MCF10A (WT) or cohesin-deficient cells treated with either DMSO or 100 nM LY2090314. (A) Membrane fraction after 6 hr of treatment with DMSO, or with LY2090314. (B) Cytoplasmic fraction after 6 hr of treatment with DMSO, or with LY2090314. Untrimmed blots and molecular size markers are available for A,B in Figure 5—source data 3.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Unmodified HCT116 cells (WT), and cells modified to contain SMC1A mutations: SMC1A (1), c.2027A > G; SMC1A (2), c.2479 C > T, were treated with DMSO or LY2090314 at 100 nM for 24 hr. (A) Immunoblot of the membrane fraction of HCT116 wild type (WT) and SMC1A mutant-expressing HCT116 cells. The proteasome-targeted form of β-catenin phosphorylated at Ser33/37/Thr41 is slightly less abundant in the SMC1A mutants, and this phospho isoform is degraded in all cells following treatment with LY2090314. (B) Immunoblot of the cytoplasmic fraction shows increased basal level of phosphorylated β-catenin at Ser675 in the SMC1A mutant-expressing cells compared with HCT116 WT, and LY2090314 treatment markedly increased total β-catenin in the SMC1A mutants compared with HCT116 WT. Untrimmed blots and molecular size markers are available for A,B in Figure 5—source data 4.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Immunofluorescence images show that (A) parental MCF10A (WT) or cohesin-deficient cells treated with 0.5% DMSO have no β-catenin puncta. In contrast, 24 hr of treatment with both (B) LY2090314 and (C) WNT3A leads to formation of β-catenin puncta in the cytoplasm of cohesin-deficient cells (arrows), but not in parental MCF10A (WT) cells. Scale bar = 25 µm.

To determine if stabilization of β-catenin is conserved in a second model of cohesin-mutant cancer, we performed an identical LY2090314 treatment on HCT116 cells that were stably transfected to express two SMC1A mutations identified in human colorectal carcinomas, c.2027A > G (leading to p.E676G change near the hinge domain) and c.2479 C > T (leading to a truncated protein, p.Q827X) (Cucco et al., 2014; Sarogni et al., 2019). The limitation is that these cells are not a model of cohesin deficiency, but rather, one in which normal cohesin function is perturbed by expression of a mutant version of SMC1A (Sarogni et al., 2019). We observed an increased basal level of phosphorylated β-catenin at Ser675 in cells that express either of these SMC1A mutants. Furthermore, LY2090314 treatment markedly increased total β-catenin in both the SMC1A mutants compared with HCT116 wild type controls (Figure 5—figure supplement 2A,B). The results indicate that abnormally high levels of active β-catenin are also present following Wnt stimulation when a fourth subunit of cohesin, SMC1A, is perturbed.

Immunofluorescence labeling of MCF10A cells showed that in LY2090314-treated cells, the stabilized active phospho-Ser675 β-catenin (and total β-catenin, Figure 5—figure supplement 3B) mainly locates to puncta in the cytoplasm (Figure 5D). In contrast, no β-catenin accumulation was observed in DMSO-treated cells (Figure 5—figure supplement 3A). β-catenin-containing puncta were also observed upon WNT3A treatment of cohesin-deficient clones (Figure 5—figure supplement 3C). This indicates that Wnt stimulation rather than a secondary effect of LY2090314 is responsible for β-catenin accumulation. We could not reliably detect an increase of β-catenin in the nucleus of cohesin-deficient MCF10A clones by immunofluorescence (Figure 5D), therefore we decided to use transcriptional response to determine the consequences of β-catenin stabilization for Wnt signaling.

### Cohesin-deficient leukemia cells are hypersensitive to Wnt signaling

RNA-sequencing analysis of the cohesin gene deletion clones compared with parental MCF10A cells revealed that gene expression changes strongly track with the identity of the deleted cohesin gene (Figure 6—figure supplement 1A). However, expressed transcripts encoding Wnt signaling pathway components did not cluster differently in cohesin-deficient clones compared with parental MCF10A cells, and cohesin mutation-based clustering remained dominant (Figure 6—figure supplement 1B). We reasoned that stimulation of Wnt signaling in a more responsive cell type might be necessary to determine how stabilized β-catenin in cohesin-deficient cells affects transcription.

Myeloid leukemias are frequently characterized by cohesin mutations, particularly in STAG2. Furthermore, activation of Wnt signaling is associated with transformation in AML (Wang et al., 2010; Beghini et al., 2012; Kang et al., 2020) and AML patients were identified with mutations in AXIN1 and APC that lead to stabilization of β-catenin (Erbilgin et al., 2012). CMK is a Down Syndrome-derived megakaryoblastic cell line that typifies myeloid leukemias that are particularly prone to cohesin mutation (Yoshida et al., 2013). We edited CMK to contain the STAG2-AML associated mutation R614* (Antony et al., 2020) and selected single clones with complete loss of the STAG2 protein to create the cell line CMK-STAG2-/- (Figure 6—figure supplement 2A–C).

Immunofluorescence showed that β-catenin is increased by 20% in the nuclei of CMK-STAG2-/- cells relative to parental cells upon WNT3A stimulation (Figure 6A,B). To determine immediate early transcriptional responses to Wnt signaling, RNA-sequencing was performed on CMK-STAG2-/- and parental CMK cells at baseline and after stimulation with WNT3A for 4 hr. Around 76% more genes were upregulated in response to WNT3A in CMK-STAG2-/- compared with CMK parental cells (616 in CMK-STAG2-/- vs 350 in CMK parental, FDR ≤ 0.05, Figure 6C), while around the same number were downregulated. About one quarter of differentially expressed genes overlapped between CMK-STAG2-/- and CMK parental cells.

![Figure 6.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig6-v2.jpg)

**Figure 6.:** (A) Immunofluorescence images showing slightly increased nuclear accumulation of β-catenin in STAG2-CMK cells (STAG2-/-) compared to parental (WT) following treatment with LY2090314 at 100 nM for 24 hr. (B) Quantification of nuclear total β-catenin in parental (WT) and STAG2-CMK cells (STAG2-/-) cells. Fluorescence of nuclear total β-catenin was determined relative to the nuclear area. Image J was used quantify cells from 10 different confocal fields. The graph depicts s.e.m. from analyses of 170–188 cell nuclei, and the p value was calculated using a student’s t test. (C) Histogram showing the number of genes upregulated or downregulated at FDR ≤ 0.05 upon WNT3A treatment in parental (WT) and STAG2-/- CMK cells. WNT3A stimulation was performed on three biological replicates, from three independent experiments. (D) Overlap of genes significantly upregulated or downregulated (FDR ≤ 0.05) upon WNT3A treatment between parental (WT) and STAG2-/- CMK cells. (E) Top enriched pathways (ranked by gene count) from the significantly downregulated and upregulated genes (FDR ≤ 0.05) following WNT3A treatment in STAG2-/- and parental (WT) CMK cells using the ClusterProfiler R package on the Gene Ontology Biological Process dataset modeling for both cell types (WT or STAG2-/-) and regulation pattern (up- or downregulation). Source data is available for C,D in Figure 6—source data 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Whole genome correlation matrix of MCF10A cells. The dendrogram shows a common clustering of the biological replicates. There are two main clusters. The STAG2-/- (MT10_1–3) transcriptomes are more similar to the WT (MWT_1–3). SMC3+/- (MS_1–3) and RAD21+/- (MR50_1–3) populate the second cluster. (B) MCF10A gene expression profile of genes involved in WNT signaling pathways according to Gene Ontology annotation (GO:0016055). The heatmap shows the clustering of the scaled (z-score) normalized count (log2RPKM) for each replicate. RNA-sequencing data is available in the GEO database under GSE154086.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) Sanger sequencing shows successful CRISPR-CAS9 editing introducing the STAG2 R614* C > T mutation site into CMK cells. (B) Reduced STAG2 mRNA and (C) protein in STAG2-/- CMK cells. (D) Heatmap showing log2 RPKM values of 402 genes upregulated only in STAG2 mutant cells (FDR ≤ 0.05) following 4 hr of WNT3A treatment. (E) GSEA analyses of the 402 upregulated genes. (F) Heatmap showing log2 RPKM values of 171 genes downregulated only in STAG2 mutant cells (FDR ≤ 0.05) following 4 hr of WNT3A treatment. (G) GSEA analyses of the 171 genes significantly downregulated only in the STAG2 mutant line. Gene lists are provided in Figure 6—source data 1.

Strikingly, 402 genes that were not Wnt-responsive in CMK parental cells became Wnt-responsive upon introduction of the STAG2 R614* mutation (Figure 6D). Genes upregulated in CMK-STAG2-/- markedly increased the number of Wnt-sensitive biological pathways following WNT3A treatment compared with parental CMK cells (Figure 6E). A strongly upregulated cluster of 244 transcripts in CMK-STAG2-/- included genes encoding signaling molecules (JAG2, IL6ST, SEMA3G) and transcription factors (SP7, KLF3, SMAD3, EP300, and EPHA4) (Figure 6—figure supplement 2D). Genes in this cluster were enriched for LEF1 and TCF7 binding sites, indicating their potential to be directly regulated by β-catenin. Enriched biological pathways included Wnt signaling, cell cycle and metabolism (Figure 6—figure supplement 2E). Pathway analyses of genes significantly downregulated only in CMK-STAG2-/- also showed enrichment for metabolism (Figure 6—figure supplement 2F,G).

Overall, our results show that CMK-STAG2-/- cells are exquisitely sensitive to Wnt signaling. Introduction of the STAG2 R614* mutation amplified expression of Wnt-responsive genes and sensitized genes and pathways that are not normally Wnt-responsive in CMK. This sensitivity could be due at least in part to stabilized β-catenin.

### Conservation of WNT sensitivity in cohesin-deficient zebrafish

To determine if enhanced Wnt sensitivity is conserved in a cohesin-deficient animal model, we used two previously described zebrafish cohesin mutants: stag2bnz207 (Ketharnathan et al., 2020), which has a seven base-pair deletion in stag2b leading to a prematurely truncated Stag2b protein, and rad21nz171 (Horsfield et al., 2007), which has a nonsense point mutation in the rad21 gene that eliminates Rad21 protein. To provide a readout for Wnt signaling, we used transgenic zebrafish carrying a TCF/β-catenin reporter in which exogenous Wnt stimulation induces nuclear mCherry: Tg(7xTCF-Xla.Siam:nslmCherry)ia5 (Moro et al., 2012). The Wnt reporter construct, which drives nuclear mCherry red fluorescence in Wnt-responsive cells, was introduced into zebrafish carrying the stag2bnz207 and rad21nz171 mutation by crossing.

Zebrafish embryos heterozygous for Tg(7xTCF-Xla.Siam:nslmCherry)ia5, and either homozygous for stag2bnz207, rad21nz171, or wild type, were exposed to 0.15 M LiCl, an agonist of the Wnt signaling pathway (Figure 7). Expression of mCherry in the midbrain of embryos was detected at 20 hr post-fertilization (hpf) by epifluorescence and confocal imaging. A constitutive low level of mCherry is present in the developing midbrain of both untreated wild type (Figure 7A,B,I,J), and rad21nz171 embryos (Figure 7M,N). On the other hand, untreated stag2bnz207 embryos exhibited noticeably higher basal mCherry levels than wild type siblings (Figure 7E,F compared with A,B). This observation indicates that the Wnt pathway is more intrinsically active in these embryos. However, the addition of LiCl did not result in much additional fluorescence owing to stag2bnz207 mutation (Figure 7G,H compared with C,D). While mCherry expression in rad21nz171 mutants resembled that in wild type embryos at baseline, LiCl treatment dramatically increased the existing midbrain mCherry expression in rad21nz171 mutants compared with wild type embryos (Figure 7O,P compared with K,L). This observation indicates that rad21nz171 mutants are more sensitive to Wnt stimulation than wild type.

![Figure 7.](https://cdn.elifesciences.org/articles/61405/elife-61405-fig7-v2.jpg)

**Figure 7.:** Wnt reporter Tg(7xTCF-Xla.Siam:nlsmCherry)ia5 control embryos, Tg(7xTCF-Xla.Siam:nlsmCherry)ia5;stag2bnz207 and Tg(7xTCF-Xla.Siam:nlsmCherry)ia5;rad21nz171 cohesin-mutant embryos were treated with 0.15 M LiCl from 4 hpf to 20 hpf. (A–H) max projections of 4 (10 μm) optical sections. (A,C,E,G) TD (transmitted light detector) images merged with confocal images. (B,D,F,H) confocal images alone. (I,K,M,O) Brightfield/fluorescent and (J,N,L,P) confocal images of the same embryos in I,K,M,O. (A–D) and (I–J) Tg(7xTCF-Xla.Siam:nlsmCherry)ia5 control embryos (WT) have low level fluorescence (Wnt reporter activity) in the midbrain that is increased following treatment. (E–H) Tg(7xTCF-Xla.Siam:nlsmCherry)ia5; stag2bnz207 embryos have elevated baseline levels of fluorescence (Wnt reporter activity) relative to controls (yellow arrow) with not much further increase upon LiCl treatment. (M–P) Tg(7xTCF-Xla.Siam:nlsmCherry)ia5; rad21nz171 cohesin-mutant embryos show enhanced Wnt reporter activity in the midbrain (green arrow) upon LiCl treatment, relative to controls. hpf, hours post-fertilization. mb, midbrain. Scale bar, 50 µm.

Overall, the results show that Wnt signaling is sensitized in cohesin-mutant zebrafish embryos, similar to our observations in MCF10A and CMK cell lines. Our findings agree with previous work showing that canonical Wnt signaling is hyperactivated in cohesin-loader nipblb-loss-of-function zebrafish embryos (Mazzola et al., 2019). Altogether, the results suggest that hyperactivation of Wnt signaling is a conserved feature of cohesin-deficient cells, and that enhanced sensitivity to Wnt is at least in part due to stabilization of β-catenin.

## Discussion

The cohesin complex and its regulators are encoded by several different loci, and genetic alterations in any one of them may occur in up to 26% of patients included in The Cancer Genome Atlas (TCGA) studies (Romero-Pérez et al., 2019). Therefore, we were motivated to identify compounds that interfere with cell viability in more than just one type of cohesin mutant. The generation of RAD21, SMC3, and STAG2 cohesin mutations in the breast epithelial cell line MCF10A resulted in mild cell cycle and nucleolar phenotypes that are consistent with the many cellular roles of cohesin. Differences between RAD21 and SMC3 heterozygotes vs STAG2 homozygotes could be explained by the fact that RAD21 and SMC3 are obligate members of the cohesin ring, whereas STAG2 can be compensated by STAG1.

Synthetic lethal sensitivities of cohesin-mutant cells that emerged from our screen mostly related to the phenotypes of cohesin-mutant cells, and/or their previously identified vulnerabilities. For example, cohesin-mutant cells were sensitive to inhibitors of the PI3K/Akt/mTOR pathway that feeds into ribosome biogenesis, epigenetic inhibitors that could interfere with cohesin’s genome organization and gene expression roles, and a limited sensitivity to PARP inhibitors. The observed sensitivity to PI3K/AKT/mTOR inhibitors is consistent with the nucleolar disruption present in cohesin-deficient cell lines, and with cohesin’s known involvement in rDNA transcription and ribosome biogenesis (Bose et al., 2012). We have also previously described evidence for sensitivity of cohesin-deficient cell lines to bromodomain (BET) inhibition (Antony et al., 2020). However, the Wnt agonist LY2090314, which mimics Wnt activation by inhibiting GSK3-β (Atkinson et al., 2015), emerged as a novel class of compound that inhibited the growth of all three cohesin mutants tested. Because there is pathway convergence between Wnt signaling and the PI3K/AKT/mTOR pathway (Prossomariti et al., 2020) it is possible that these pathways represent a common avenue of sensitivity. The identification of PI3K/AKT/mTOR inhibitors in the screen supports this notion.

Wnt signals are important for stem cell maintenance and renewal in multiple mammalian tissues (Clevers et al., 2014). Canonical Wnt signaling is required for self-renewal of leukemia stem cells (LSCs) (Kang et al., 2020), and is reactivated in more differentiated granulocyte-macrophage progenitors (GMPs) when they give rise to LSCs (Wang et al., 2010). Wnt signaling is an important regulator of hematopoietic stem cell (HSC) self-renewal as well (Rattis et al., 2004). Our results suggest that cohesin-deficient cells are sensitive to Wnt agonism because they already have stabilization of β-catenin. Interestingly, multiple experimental systems showed that dose-dependent reduction in cohesin function causes HSC expansion accompanied by a block in differentiation (Viny and Levine, 2018; Mazumdar and Majeti, 2017). It is possible that the effects of cohesin deficiency on HSC development could be in part due to enhanced Wnt signaling.

Cohesin mutations are particularly frequent (53%) in Down Syndrome-associated Acute Megakaryoblastic Leukemia (DS-AMKL) patients (Yoshida et al., 2013). In the edited DS-AMKL cell line STAG2-CMK, there was a dramatically enhanced immediate early transcriptional response to WNT3A, including induction of hundreds of genes that are not normally responsive to WNT3A in this cell line. It is possible that STAG2 deficiency in CMK leads to an altered chromatin structure that sensitizes genes to Wnt signaling. However, we observed increased nuclear localization of β-catenin in STAG2-CMK, increasing the likelihood that stabilization of β-catenin in STAG2-CMK cells accounts at least in part for amplified gene expression in response to WNT3A. Interestingly, DS-AMKL leukemias are often associated with amplified Wnt signaling caused by Trisomy 21 (Emmrich et al., 2014) suggesting a possible synergy between cohesin mutations and Wnt signaling dysregulation in DS-AMKL.

We observed an enhanced Wnt reporter response to Wnt activation in rad21- and stag2b-mutant zebrafish, arguing that Wnt sensitivity upon cohesin mutation is a conserved phenomenon. Previous research shows that cohesin genes are at once both targets (Xu et al., 2014; Ghiselli et al., 2003) and upstream regulators (Estarás et al., 2015; Schuster et al., 2015; Avagliano et al., 2017; Mazzola et al., 2019) of Wnt signaling. For example, depletion of cohesin-loader nipbl in zebrafish embryos was reported to downregulate Wnt signaling at 24 hpf (Pistocchi et al., 2013), but to upregulate it at 48 hpf (Mazzola et al., 2019). What determines the directionality of cohesin’s effect on Wnt signaling is unclear. It is possible that feedback loops operate differently in cell- and signal-dependent contexts (MacDonald et al., 2009) in cohesin-deficient backgrounds.

Is Wnt pathway activation a conserved feature of cohesin-mutant cancers? Using publicly available data at TCGA (Grossman et al., 2016), we correlated expression of genes in the Wnt pathway (Hallmark WNT β-catenin signaling) with nonsense mutation of STAG2, the most common of the cohesin mutations, in the four most represented cancers (bladder cancer, endometrial carcinoma, glioblastoma multiforme and cervical kidney renal papillary cell carcinoma). In comparative ranking, the Wnt pathway ranks 8th for enrichment in upregulated genes (after DNA repair/G2 checkpoint, MYC/E2F targets, oxidative phosphorylation and the unfolded protein response; Supplementary file 2). While our analysis could indicate conserved upregulation of the Wnt pathway in STAG2 mutant cancers, a caveat is that the true situation is likely to be more complex. If β-catenin is stabilized, upstream and in-parallel effectors such as Wnt ligands, receptors, signaling intermediates might trend to downregulation owing to negative feedback loop regulation of the Wnt pathway for example via DKK1 (Niida et al., 2004). Furthermore, because cancer collections are unlikely to be under Wnt stimulation at the time of RNA collection, it is possible that their true Wnt sensitivity will be missed in a steady-state transcription analysis.

A remaining question is exactly what causes β-catenin stabilization and Wnt hyperactivation in cohesin-mutant cells. One possibility is that stabilization of β-catenin upon cohesin deficiency is linked to energy metabolism. For example, in developing amniote embryos, glycolysis in actively growing cells of the embryonic tail bud raises the intracellular pH, which in turn causes β-catenin stabilization (Oginuma et al., 2020; Oginuma et al., 2017). This mode of glycolysis is similar to that observed in cancer cells and is known as the Warburg effect (Parks et al., 2013; Wang et al., 2016). Metabolic and oxidative stress disturbances in cohesin-mutant cells observed in this study and others (Bose et al., 2012; Cukrov et al., 2018) might similarly influence β-catenin stability and in turn, sensitivity to incoming Wnt signals. Further research will be needed to determine how β-catenin is stabilized in cohesin-deficient cells, whether β-catenin stabilization is part of a transition to malignancy, and if the associated Wnt sensitivity represents a therapeutic opportunity in cohesin-mutant cancers.

## Materials and methods

### Cell culture

MCF10A (a spontaneously immortalized breast epithelial cell line) was purchased from Sigma (product #: CRL 10317). Sigma use STR analysis to verify the line. A PCR test in our laboratory showed that all cells were mycoplasma free. CMK (acute megakaryocytic leukemia associated with Down Syndrome) was a gift from Dr Motomi Osato, National University of Singapore. These cells tested negative with MycoAlert Mycoplasma Detection Kit in our laboratory. K562 (chronic myelogenous leukemia) were purchased from ATCC, CCL-243. These cells tested mycoplasma free using B3903-Mycoplasma Detection Kit - QuickTest-com from Biotool. The HTC116 cell line was purchased form ATCC. STR analysis is used by ATCC to verify all cell lines.

MCF10A and its cohesin-deficient derivatives were maintained in Dulbecco’s modified Eagle medium (DMEM) (Life Technologies) supplemented with 5% horse serum (Life Technologies), 20 ng/mL of epidermal growth factor (EGF) (Peprotech), 0.5 mg/mL of hydrocortisone, 100 ng/mL of cholera toxin and 10 μg/mL of insulin (local pharmacy). All supplements were purchased from Sigma-Aldrich unless otherwise stated. K562 cells were maintained in Isocove’s Modified Dulbecco’s Media (IMDM) (Life Technologies) containing 10% fetal bovine serum. CMK cells were maintained in RPMI 1640 media containing 10% fetal bovine serum. CMK cells and adherent K562-STAG2 null line were detached for subculture using trypsin-EDTA (0.005% final concentration, Life Technologies). For WNT stimulation, recombinant Human WNT-3A Protein (5036-WN, R and D systems) was used at 200 ng/mL for 4 hr. Human colorectal carcinoma HCT116 cells were grown in DMEM with 10% fetal calf serum and antibiotics. Stable transfection of HCT116 cells with SMC1A mutations c.2027A > G and c.2479 C > T was described previously (Sarogni et al., 2019). All cells were cultured at 37°C in 5% CO2.

### Generation of isogenic cell lines using CRISPR-CAS9 editing

We used CRISPR-CAS9 sgRNAs targeting the 5' and 3' UTR regions of RAD21, SMC3 and STAG2 gene to create MCF10A RAD21+/-, MCF10A SMC3+/-, and MCF10A STAG2-/-. Specific sgRNAs were cloned into the px458 plasmid (Ran et al., 2013) and transfected into MCF10A cells. Single GFP-positive cells were isolated into 96-well plates using a FACSAriaII (Becton Dickinson) and clonally expanded. PCR screening and Sanger sequencing identified cells with heterozygous deletion of RAD21 or SMC3 and homozygous deletion of STAG2. Primer and guide sequences are provided in Supplementary file 1. Editing of K562 to create STAG2 R614* mutation has been described previously (Antony et al., 2020). The CMK line with the STAG2 R614* mutation was generated using the same sgRNA and method.

### Quantitative PCR (RT-qPCR)

Total RNA was extracted using NucleoSpin RNA kit (Machery-Nagel). cDNA was synthesized using qScript cDNA SuperMix (Quanta Biosciences). RT-qPCR was performed on a LightCycler 480 II (Roche Life Science) using SYBR Premix Ex Taq (Takara). Expression values relative to reference genes cyclophilin and glyceraldehyde 3-phosphate dehydrogenase (GAPDH) were derived using qBase Plus (Biogazelle). Primer sequences are provided in Supplementary file 1.

### Antibodies

Primary antibodies used are as follows: anti-RAD21 (ab992), anti-SMC3 (#5696, CST), anti-STAG2 (ab4463), anti-γ-Tubulin (T5326; Sigma-Aldrich) in 1:5000, anti-fibrillarin (ab5821), anti-nucleolin (ab13541), anti-gamma H2AX (ab26350), anti-TP53 (ab131442), anti-β-catenin (#9562, CST), anti-phospho-β-catenin (Ser675) (#9567, CST), anti-phospho- phospho-β-catenin (Ser33/37/Thr41) (#9561, CST). Secondary antibodies used for immunofluorescence were anti-mouse Alexa Fluor 488 (1:2000, Life Technologies), anti-rabbit Alexa Fluor 488 (1:2000, Life Technologies), anti-rabbit Alexa Fluor 568 (1:2000, Life Technologies). All antibodies were used in 1:1000 for immunoblotting or immunofluorescence unless otherwise stated.

### Immunoblotting

Immunoblotting was performed as described previously (Antony et al., 2015; Dasgupta et al., 2016). Primary antibodies were detected using IRDye 800CW Donkey anti-Goat IgG and IRDye 680CW Goat anti-mouse IgG, IRDye 800CW Goat anti-rabbit IgG (LICOR). LI-COR Odyssey and LI-COR Image Studio software was used to image and quantify blots.

### Proliferation assays

MCF10A parental and isogenic cohesin-deficient cell lines were seeded in 96-well plates at 2000 cells per well. Cell confluence was monitored by time-lapse microscopy using IncuCyte FLR with a 10X objective for 5 days.

### Cell cycle analysis

Cells were synchronized using double thymidine block as described previously (Dasgupta et al., 2016). Samples were harvested, fixed, and stained with 10 μg/mL propidium iodide (PI) and 250 μg/mL RNase A, 37°C for 30 min. Cells were then analyzed using a Beckman Coulter Gallios Flow Cytometer.

### Immunofluorescence and imaging

Cells stained for FBL, gH2AX, and TP53 were imaged using an Opera Phenix high content screening system, with 63x water objectives in confocal mode. Spot enumeration and signal intensities were analyzed using Harmony software (PerkinElmer). CMK or MCF10A cells were fixed with 4% (v/v) paraformaldehyde in PBS for 10 min, then permeablized with 0.1% Triton in PBS. CMK cells were spun onto slides using SHANDON cytospin prior to fixation. Cells were blocked with 2% (w/v) bovine serum albumin in PBS, then incubated with primary antibody overnight at 4°C. The next day, cells were washed with PBS and incubated with secondary antibody and Hoechst 33342 (1 µg/mL) at room temperature for 1 hr. Cells were then washed and mounted on slides using ProLong Gold Anti-fade (Life Technologies) or DAKO mounting medium. Imaging was done using a Nikon C2 confocal microscope with NIS Elements software and images were processed and quantified using Image J or FIJI software.

### High-throughput compound screen

3009 compounds from an FDA-approved, kinase inhibitors and epigenetic libraries (Compounds Australia, Griffith University, Australia) were screened against MCF10A parental and MCF10A cohesin-deficient clones. Compounds are stored by Compounds Australia under robust environmental conditions and supplied in assay ready plate format. MCF10A parental cells and cohesin-deficient derivatives were screened as single biological replicates with two technical replicates for each drug concentration. MCF10A parental cells were seeded at 600 cells/well, RAD21+/- at 800 cells/well, SMC3+/- at 1200 cells/well and STAG2-/- at 700 cells/well, into 384-well CellCarrier-384 Ultra microplates (PerkinElmer) with EL406 microplate washer dispenser (BioTek). 24 hr later, growth media was aspirated from the plates and 35 µL of fresh MCF10A complete growth media was added into each well using BioTek EL406TM Microplate washer dispenser. 5 µL of 8x concentrated compound solution (diluted in MCF10A complete growth media) was added into each well with a JANUS automated liquid handling system (PerkinElmer). At the time of drug treatment, one untreated plate was retained to determine the cell number at t = 0. For the rest of the assay plate, compounds were added in 40 µL of complete medium per well using an Echo 550 Liquid Handler (Labcyte). Positive (Campthothecin, 40 nM) and negative controls (DMSO 0.1%) were added to each assay plate for quality control. Duplicated control plates of each cell line were also prepared for cell count quantification prior to the addition of drugs, to be used in the growth rate inhibition (GR) metrics. After 48 hr, control and treated cells in were fixed and stained simultaneously using 4% PFA/0.5 µg/mL DAPI/0.1% Triton X-100 solution. Cells were imaged using an Opera Phenix high content screening system and analyzed using Columbus software (PerkinElmer) using 20x water objectives. To determine compound activity, dose-response curves for each compound was plotted and using an R package, GRmetrics (Clark et al., 2017). Synthetic lethal candidate compounds were selected and ranked based on the differential area over curve (AOC) metrics (Hafner et al., 2016) derived from dose-response curves of MCF10A parental and cohesin-deficient cell lines. Compounds that caused ≥30% growth inhibition (AOC ≥0.15) in cohesin-deficient clones compared with parental MCF10A cells were selected as hits. A secondary screen was performed with 85 candidate hits identified from primary screen (two technical replicates per clone per concentration). The secondary screen was added to independently validate primary screen data. Activity of the selected compounds was tested in eleven concentrations (0.5 nM to 10 µM). Secondary screen hit compounds were selected based on the same threshold used in primary screen.

### Cell viability assays to validate compounds identified from the screen

Individual compounds were purchased from Sigma-Aldrich, Selleck Chem or MedChemExpress and dissolved in DMSO at recommended concentrations. MCF10A parental cells were seeded in 96-well plates at 3000 cells/well, RAD21+/- at 4500 cells/well, SMC3+/- at 5000 cells/well and STAG2-/- at 3500 cells/well. Cells were incubated for 24 hr then treated with compounds for 48 hr. DAPI-stained cells were counted using a Lionheart FX automated microscope (BioTek). K562 parental and STAG2-/- cells were seeded at 2000 cells per well in 96 well plates, incubated with the compound for 48 hr after which viability was measured using 3-(4,5-dimethylthiazol-2-yl)−2,5-diphenyltetrazolium bromide or MTT.

### RNA-sequencing and analyses

Total RNA was extracted using NucleoSpin RNA kit (Machery-Nagel). MCF10A libraries from three biological replicates of each cell type were prepared using NEBNext Ultra RNA Library Prep Kit (Illumina) and sequenced on HiSeq X by Annoroad Gene Technology Ltd. (Beijing, China), contracted through Custom Science (NZ). CMK lines were treated with 200 ng/mL of recombinant human WNT3A (R and D systems) for 4 hr. Libraries were prepared from baseline (non-treated) and WNT3A treated CMK cell lines using Illumina TruSeq stranded mRNA library and sequenced on the HiSeq 2500 V4 at the Otago Genomics Facility (Dunedin, New Zealand). RNA-sequencing reads were first trimmed for sequencing adapters and low quality (q < 20). Cleaned reads were then aligned to the human genome GRCh37 (hg19) using HISAT2 version 2.0.5 with gene annotation from Ensembl version 75. Read counts were retrieved by exon and summarized by gene using featureCount (Liao et al., 2014) version v1.5.3. Differentially expressed genes in the STAG2-/- mutants versus wild type were identified using DESeq2 (Love et al., 2014). P-values were adjusted for multi-test following Benjamini-Hochberg methodology. Pathways analyses were performed using Molecular Signature Databases ReactomePA (Yu and He, 2016) and clusterProfiler (Yu et al., 2012) on differentially expressed genes.

### Zebrafish methods and imaging

Wild type (WIK), TCF reporter line Tg(7xTCF-Xla.Siam:nslmCherry)ia5 (Moro et al., 2012), stag2bnz207 (Ketharnathan et al., 2020) and rad21nz171 (Horsfield et al., 2007) mutant fish lines were maintained according to established husbandry methods (Westerfield, 1995). We crossed heterozygous rad21nz171 or homozygous stag2bnz207 mutants to the TCF reporter line then crossed these fish (rad21nz171/+;TCF/+) to rad21nz171/+, or (stag2bnz207/+;TCF/+) to stag2bnz207/+. Progeny carrying the TCF reporter were incubated with 0.15 M lithium chloride (LiCl) from 4 hpf for 16 hr. LiCl salt was directly dissolved in embryo water and added to embryos in six well plates. 50 embryos were used per treatment group. At 20 hpf, embryos were washed, anesthetized with MS-222 (200 mg/L) and mounted in low melting agarose (0.6%) or 3% methyl cellulose for imaging. Z-stacks were acquired using a Nikon C2 confocal microscope. Embryos were genotyped post-imaging.

### Statistical analyses

All statistical analyses were carried out using R Studio or Prism version eight software (GraphPad).

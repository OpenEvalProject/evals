# A zebrafish embryo screen utilizing gastrulation identifies the HTR2C software inhibitor pizotifen as a suppressor of EMT-mediated metastasis

## Authors

- Joji Nakayama<sup>1</sup> ([ORCID: 0000-0003-1077-140X](https://orcid.org/0000-0003-1077-140X)) †
- Lora Tan<sup>1</sup>
- Yan Li<sup>1</sup>
- Boon Cher Goh<sup>2</sup>
- Shu Wang<sup>1</sup>
- Hideki Makinoshima<sup>3</sup>
- Zhiyuan Gong<sup>1</sup> †

### Affiliations

1. Department of Biological Science, National University of Singapore Singapore Singapore
2. Cancer Science Institute of Singapore, National University of Singapore Singapore Singapore
3. Tsuruoka Metabolomics Laboratory, National Cancer Center Tsuruoka Japan
4. Shonai Regional Industry Promotion Center Tsuruoka Japan
5. Institute of Bioengineering and Nanotechnology Singapore Singapore
6. Division of Translational Research, Exploratory Oncology Research and Clinical Trial Center, National Cancer Center Kashiwa Japan

† Corresponding author

## Abstract

Metastasis is responsible for approximately 90% of cancer-associated mortality but few models exist that allow for rapid and effective screening of anti-metastasis drugs. Current mouse models of metastasis are too expensive and time consuming to use for rapid and high-throughput screening. Therefore, we created a unique screening concept utilizing conserved mechanisms between zebrafish gastrulation and cancer metastasis for identification of potential anti-metastatic drugs. We hypothesized that small chemicals that interrupt zebrafish gastrulation might also suppress metastatic progression of cancer cells and developed a phenotype-based chemical screen to test the hypothesis. The screen used epiboly, the first morphogenetic movement in gastrulation, as a marker and enabled 100 chemicals to be tested in 5 hr. The screen tested 1280 FDA-approved drugs and identified pizotifen, an antagonist for serotonin receptor 2C (HTR2C) as an epiboly-interrupting drug. Pharmacological and genetic inhibition of HTR2C suppressed metastatic progression in a mouse model. Blocking HTR2C with pizotifen restored epithelial properties to metastatic cells through inhibition of Wnt signaling. In contrast, HTR2C induced epithelial-to-mesenchymal transition through activation of Wnt signaling and promoted metastatic dissemination of human cancer cells in a zebrafish xenotransplantation model. Taken together, our concept offers a novel platform for discovery of anti-metastasis drugs.

## Introduction

Metastasis, a leading contributor to the morbidity of cancer patients, occurs through multiple steps: invasion, intravasation, extravasation, colonization, and metastatic tumor formation (Nguyen et al., 2009; Welch and Hurst, 2019; Chaffer and Weinberg, 2011). The physical translocation of cancer cells is an initial step of metastasis and molecular mechanisms of it involve cell motility, the breakdown of local basement membrane, loss of cell polarity, acquisition of stem cell-like properties, and epithelial-to-mesenchymal transition (EMT) (Tsai and Yang, 2013; Lu and Kang, 2019). These cell-biological phenomena are also observed during vertebrate gastrulation in that evolutionarily conserved morphogenetic movements of epiboly, internalization, convergence, and extension progress (Solnica-Krezel, 2005). In zebrafish, the first morphogenetic movement, epiboly, is initiated at approximately 4 hr post fertilization (hpf) to move cells from the animal pole to eventually engulf the entire yolk cell by 10 hpf (Latimer and Jessen, 2010; Solnica-Krezel, 2006). The embryonic cell movements are governed by the molecular mechanisms that are partially shared in metastatic cell dissemination.

At least 50 common genes were shown to be involved in both metastasis and gastrulation progression: Knockdown of these genes in Xenopus or zebrafish induced gastrulation defects; conversely, overexpression of these genes conferred metastatic potential on cancer cells and knockdown of these genes suppressed metastasis (Yang and Weinberg, 2008; Dongre and Weinberg, 2019; Thiery et al., 2009; Nieto et al., 2016; Table 1). This evidence led us to hypothesize that small molecules that interrupt zebrafish gastrulation may suppress metastatic progression of human cancer cells.

**Table 1.**
 A list of the genes that are involved between gastrulation and metastasis progression.A list of the 50 genes that play essential role in governing both metastasis and gastrulation progression. The gastrulation defects in Xenopus or zebrafish that are induced by knockdown of each of these genes were indicated. The molecular mechanism in metastasis that is inhibited by knockdown of each of the same genes was indicated.


<table>
  <thead>
    <tr>
      <th>Genes</th>
      <th>Gastrulation defects</th>
      <th>Ref</th>
      <th>Effects in metastasis</th>
      <th>Ref</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BMP</td>
      <td>Convergence and extension</td>
      <td>Kondo, 2007</td>
      <td>EMT</td>
      <td>Katsuno et al., 2008</td>
    </tr>
    <tr>
      <td>WNT</td>
      <td>Convergence and extension</td>
      <td>Tada and Smith, 2000</td>
      <td>Migration and invasion</td>
      <td>Vincan and Barker, 2008</td>
    </tr>
    <tr>
      <td>FGF</td>
      <td>Convergence and extension</td>
      <td>Yang et al., 2002</td>
      <td>Invision</td>
      <td>Nomura et al., 2008</td>
    </tr>
    <tr>
      <td>EGF</td>
      <td>Epiboly</td>
      <td>Song et al., 2013</td>
      <td>Migration</td>
      <td>Lu et al., 2001</td>
    </tr>
    <tr>
      <td>PDGF</td>
      <td>Convergence and extension</td>
      <td>Damm and Winklbauer, 2011</td>
      <td>EMT</td>
      <td>Jechlinger et al., 2006</td>
    </tr>
    <tr>
      <td>CXCL12</td>
      <td>Migration of endodermal cells</td>
      <td>Mizoguchi et al., 2008</td>
      <td>Migration and invasion</td>
      <td>Shen et al., 2013</td>
    </tr>
    <tr>
      <td>CXCR4</td>
      <td>Migration of endodermal cells</td>
      <td>Mizoguchi et al., 2008</td>
      <td>Migration and invasion</td>
      <td>Shen et al., 2013</td>
    </tr>
    <tr>
      <td>PIK3CA</td>
      <td>Convergence and extension</td>
      <td>Montero et al., 2003</td>
      <td>Migration and invasion</td>
      <td>Wander et al., 2013</td>
    </tr>
    <tr>
      <td>YES</td>
      <td>Epiboly</td>
      <td>Tsai et al., 2005</td>
      <td>Migration</td>
      <td>Barraclough et al., 2007</td>
    </tr>
    <tr>
      <td>FYN</td>
      <td>Epiboly</td>
      <td>Sharma et al., 2005</td>
      <td>Migration and invasion</td>
      <td>Yadav and Denning, 2011</td>
    </tr>
    <tr>
      <td>MAPK1</td>
      <td>Epiboly</td>
      <td>Krens et al., 2008</td>
      <td>Migration</td>
      <td>Radtke et al., 2013</td>
    </tr>
    <tr>
      <td>SHP2</td>
      <td>Convergence and extension</td>
      <td>Jopling et al., 2007</td>
      <td>Migration</td>
      <td>Wang et al., 2005</td>
    </tr>
    <tr>
      <td>SNAI1</td>
      <td>Convergence and extension</td>
      <td>Ip and Gridley, 2002</td>
      <td>EMT</td>
      <td>Batlle et al., 2000</td>
    </tr>
    <tr>
      <td>SNAI2</td>
      <td>Mesoderm and neural crest formation</td>
      <td>Shi et al., 2011</td>
      <td>EMT</td>
      <td>Medici et al., 2008</td>
    </tr>
    <tr>
      <td>TWIST1</td>
      <td>Mesoderm formation</td>
      <td>Castanon and Baylies, 2002</td>
      <td>EMT</td>
      <td>Yang et al., 2004</td>
    </tr>
    <tr>
      <td>TBXT</td>
      <td>Convergence and extension</td>
      <td>Tada and Smith, 2000</td>
      <td>EMT</td>
      <td>Fernando et al., 2010</td>
    </tr>
    <tr>
      <td>ZEB1</td>
      <td>Epiboly</td>
      <td>Vannier et al., 2013</td>
      <td>EMT</td>
      <td>Spaderna et al., 2008</td>
    </tr>
    <tr>
      <td>GSC</td>
      <td>Mesodermal patterning</td>
      <td>Sander et al., 2007</td>
      <td>EMT</td>
      <td>Hartwell et al., 2006</td>
    </tr>
    <tr>
      <td>FOXC2</td>
      <td>Unclear, defects in gastrulation</td>
      <td>Wilm et al., 2004</td>
      <td>EMT</td>
      <td>Mani et al., 2007</td>
    </tr>
    <tr>
      <td>STAT3</td>
      <td>Convergence and extension</td>
      <td>Miyagi et al., 2004</td>
      <td>Migration</td>
      <td>Abdulghani et al., 2008</td>
    </tr>
    <tr>
      <td>POU5F1</td>
      <td>Epiboly</td>
      <td>Lachnit et al., 2008</td>
      <td>EMT</td>
      <td>Dai et al., 2013</td>
    </tr>
    <tr>
      <td>EZH2</td>
      <td>Unclear, defects in gastrulation</td>
      <td>O’Carroll et al., 2001</td>
      <td>Invasion</td>
      <td>Ren et al., 2012</td>
    </tr>
    <tr>
      <td>EHMT2</td>
      <td>Defects in neurogenesis</td>
      <td>Lin et al., 2005</td>
      <td>Migration and invasion</td>
      <td>Chen et al., 2010</td>
    </tr>
    <tr>
      <td>BMI1</td>
      <td>Defects in skeleton formation</td>
      <td>van der Lugt et al., 1994</td>
      <td>EMT</td>
      <td>Guo et al., 2011</td>
    </tr>
    <tr>
      <td>RHOA</td>
      <td>Convergence and extension</td>
      <td>Zhu et al., 2006</td>
      <td>Migration and invasion</td>
      <td>Yoshioka et al., 1999</td>
    </tr>
    <tr>
      <td>CDC42</td>
      <td>Convergence and extension</td>
      <td>Choi and Han, 2002</td>
      <td>Migration and invasion</td>
      <td>Reymond et al., 2012</td>
    </tr>
    <tr>
      <td>RAC1</td>
      <td>Convergence and extension</td>
      <td>Habas et al., 2003</td>
      <td>Migration and invasion</td>
      <td>Vega and Ridley, 2008</td>
    </tr>
    <tr>
      <td>ROCK2</td>
      <td>Convergence and extension</td>
      <td>Marlow et al., 2002</td>
      <td>Migration and invasion</td>
      <td>Itoh et al., 1999</td>
    </tr>
    <tr>
      <td>PAR1</td>
      <td>Convergence and extension</td>
      <td>Kusakabe and Nishida, 2004</td>
      <td>Migration</td>
      <td>Shi et al., 2004</td>
    </tr>
    <tr>
      <td>PRKCI</td>
      <td>Convergence and extension</td>
      <td>Kusakabe and Nishida, 2004</td>
      <td>EMT</td>
      <td>Gunaratne et al., 2013</td>
    </tr>
    <tr>
      <td>CAP1</td>
      <td>Convergence and extension</td>
      <td>Seifert et al., 2009</td>
      <td>Migration</td>
      <td>Yamazaki et al., 2009</td>
    </tr>
    <tr>
      <td>EZR</td>
      <td>Epiboly</td>
      <td>Link et al., 2006</td>
      <td>Migration</td>
      <td>Khanna et al., 2004</td>
    </tr>
    <tr>
      <td>EPCAM</td>
      <td>Epiboly</td>
      <td>Slanchev et al., 2009</td>
      <td>Migration and invasion</td>
      <td>Ni et al., 2012</td>
    </tr>
    <tr>
      <td>ITGB1/ ITA5</td>
      <td>Mesodermal migration</td>
      <td>Skalski et al., 1998</td>
      <td>Migration and invasion</td>
      <td>Felding-Habermann, 2003</td>
    </tr>
    <tr>
      <td>FN1</td>
      <td>Convergence and extension</td>
      <td>Marsden and DeSimone, 2003</td>
      <td>Invasion</td>
      <td>Malik et al., 2010</td>
    </tr>
    <tr>
      <td>HAS2</td>
      <td>Dorsal migration of lateral cells</td>
      <td>Bakkers et al., 2004</td>
      <td>Invasion</td>
      <td>Kim et al., 2004</td>
    </tr>
    <tr>
      <td>MMP14</td>
      <td>Convergence and extension</td>
      <td>Coyle et al., 2008</td>
      <td>Invasion</td>
      <td>Perentes et al., 2011</td>
    </tr>
    <tr>
      <td>COX1</td>
      <td>Epiboly</td>
      <td>Cha et al., 2006</td>
      <td>Invasion</td>
      <td>Kundu and Fulton, 2002</td>
    </tr>
    <tr>
      <td>PTGES</td>
      <td>Convergence and extension</td>
      <td>Speirs et al., 2010</td>
      <td>Invasion</td>
      <td>Wang and Dubois, 2006</td>
    </tr>
    <tr>
      <td>SLC39A6</td>
      <td>Anterior migration</td>
      <td>Yamashita et al., 2004</td>
      <td>EMT</td>
      <td>Lue et al., 2011</td>
    </tr>
    <tr>
      <td>GNA12 /13</td>
      <td>Convergence and extension</td>
      <td>Lin et al., 2005</td>
      <td>Migration and invasion</td>
      <td>Yagi et al., 2011</td>
    </tr>
    <tr>
      <td>OGT</td>
      <td>Epiboly</td>
      <td>Webster et al., 2009</td>
      <td>Migration and invasion</td>
      <td>Lynch et al., 2012</td>
    </tr>
    <tr>
      <td>CCN1</td>
      <td>Cell movement</td>
      <td>Latinkic et al., 2003</td>
      <td>Migration and invasion</td>
      <td>Lin et al., 2012</td>
    </tr>
    <tr>
      <td>TRPM7</td>
      <td>Convergence and extension</td>
      <td>Liu et al., 2011</td>
      <td>Migration</td>
      <td>Middelbeek et al., 2012</td>
    </tr>
    <tr>
      <td>MAPKAPK2</td>
      <td>Epiboly</td>
      <td>Holloway et al., 2009</td>
      <td>Migration</td>
      <td>Kumar et al., 2010</td>
    </tr>
    <tr>
      <td>B4GALT1</td>
      <td>Convergence and extension</td>
      <td>Machingo et al., 2006</td>
      <td>Invasion</td>
      <td>Zhu et al., 2005</td>
    </tr>
    <tr>
      <td>IER2</td>
      <td>Convergence and extension</td>
      <td>Hong et al., 2011</td>
      <td>Migration</td>
      <td>Neeb et al., 2012</td>
    </tr>
    <tr>
      <td>TIP1</td>
      <td>Convergence and extension</td>
      <td>Besser et al., 2007</td>
      <td>Migration and invasion</td>
      <td>Han et al., 2012</td>
    </tr>
    <tr>
      <td>PAK5</td>
      <td>Convergence and extension</td>
      <td>Faure et al., 2005</td>
      <td>Migration</td>
      <td>Gong et al., 2009</td>
    </tr>
    <tr>
      <td>MARCKS</td>
      <td>Convergence and extension</td>
      <td>Iioka et al., 2004</td>
      <td>Migration and invasion</td>
      <td>Rombouts et al., 2013</td>
    </tr>
  </tbody>
</table>

Here, we report a unique screening concept based on the hypothesis. Pizotifen, an antagonist for HTR2C, was identified from the screen as a ‘hit’ that interrupted zebrafish gastrulation. A mouse model of metastasis confirmed pharmacological and genetic inhibition of HTR2C suppressed metastatic progression. Moreover, HTR2C induced EMT and promoted metastatic dissemination of non-metastatic cancer cells in a zebrafish xenotransplantation model. These results demonstrated that this concept could offer a novel high-throughput platform for discovery of anti-metastasis drugs and can be converted to a chemical genetic screening platform.

## Results

### Small molecules interrupting epiboly of zebrafish have a potential to suppress metastatic progression of human cancer cells

Before performing a screening assay, we validated a core of our concept through comparing the genes expressed in zebrafish gastrulation with the genes which expressed in EMT-mediated metastasis. Gene set enrichment analysis (GSEA) demonstrated that 50%-epiboly, shield, and 75%-epiboly stage of zebrafish embryos expressed the genes which promote EMT-mediated metastasis: EMT induction, TGF-β signaling, wnt/β-catenin signaling, Notch signaling (Figure 1—figure supplement 1).

We further conducted preliminary experiments to test the hypothesis. First, we examined whether hindering the molecular function of reported genes, whose knockdown induced gastrulation defects in zebrafish, might suppress cell motility and invasion of cancer cells. We chose protein arginine methyltransferase 1 (PRMT1) and cytochrome P450 family 11 (CYP11A1), both of whose knockdown induced gastrulation defects in zebrafish but whose involvement in metastatic progression is unclear (Tsai et al., 2011; Hsu et al., 2006). Elevated expression of PRMT1 and CYP11A1 was observed in highly metastatic human breast cancer cell lines and knockdown of these genes through RNA interference suppressed the motility and invasion of MDA-MB-231 cells without affecting their viability (Figure 1—figure supplement 2A-C).

Next, we conducted an inverse examination of whether chemicals which were reported to suppress metastatic dissemination of cancer cells could interrupt epiboly progression of zebrafish embryos. Niclosamide and vinpocetine are reported to suppress metastatic progression (Weinbach and Garbus, 1969; Sack et al., 2011; Huang et al., 2012; Szilágyi et al., 2005). Either niclosamide- or vinpocetine-treated zebrafish embryos showed complete arrest at very early stages or severe delay in epiboly progression, respectively (Figure 1—figure supplement 2D).

These results suggest that epiboly could serve as a marker for this screening assay and epiboly-interrupting drugs that are identified through this screening could have the potential to suppress metastatic progression of human cancer cells.

### 132 FDA-approved drugs induced delayed in epiboly of zebrafish embryos

We screened 1280 FDA, EMA, or other agencies-approved drugs (Prestwick, Inc) in our zebrafish assay. The screening showed that 0.9% (12/1280) of the drugs, including antimycin A and tolcapone, induced severe or complete arrest of embryonic cell movement when embryos were treated with 10 μM. 5.2% (66/1280) of the drugs, such as dicumarol, racecadotril, pizotifen, and S(-)eticlopride hydrochloride, induced either delayed epiboly or interrupted epiboly of the embryos. 93.3% (1194/1280) of drugs have no effect on epiboly progression of the embryos. 0.6% (8/1280) of drugs induced toxic lethality. Epiboly progression was affected more severely when embryos were treated with 50 μM; 1.7% (22/1280) of the drugs induced severe or complete arrest of it. 8.6% (110/1280) of the drugs induced either delayed epiboly or interrupt epiboly of the embryos. 4.3% (55/1280) of drugs induced a toxic lethality (Figure 1A and B, Table 2). Among the epiboly-interrupting drugs, several drugs have already been reported to inhibit metastasis-related molecular mechanisms: adrenosterone or zardaverine, which target HSD11β1 or PDE3 and -4, respectively, are reported to inhibit EMT (Nakayama et al., 2020; Kolosionek et al., 2009); racecadotril, which targets enkephalinase, is reported to confer metastatic potential on colon cancer cell (Sasaki et al., 2014); and disulfiram, which targets ALDH (aldehyde dehydrogenase), is reported to confer stem-like properties on metastatic cancer cells (Liu et al., 2013). This evidence suggests that epiboly-interrupting drugs have the potential for suppressing metastasis of human cancer cells.

![Figure 1.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig1-v2.jpg)

**Figure 1.:** (A) Cumulative results of the chemical screen in which each drug was used at either 10 µM (left) or 50 µM (right) concentrations. 1280 FDA, EMA, or other agencies-approved drugs were subjected to this screening. Positive ‘hit’ drugs were those that interrupted epiboly progression. (B) Representative samples of the embryos that were treated with indicated drugs.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The zebrafish transcriptomic data was sourced from White et al., 2017 eLife (Subramanian et al., 2005). Gene sets that were significantly enriched (FDR < 0.25) were presented with the normalized enrichment score (NES) and nominal p value. Source data files for analysis of either gene expression and enriched pathways are uploaded as gene set enrichment analysis (GSEA) Source data 1 and 2, respectively.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Western blot analysis of protein arginine methyltransferase 1 (PRMT1) (upper left) and cytochrome P450 family 11 (CYP11A1) (middle left) protein levels in non-metastatic human cancer cell line (MCF7) and highly metastatic human cancer cell lines (MDA-MB-231, MDA-MB-435, MIA-PaCa2, PC9, HCCLM3, PC3, and SW620); β-actin loading control is shown (bottom left). Preliminary experiments confirmed that epiboly could serve as a marker for this screening assay. Quantification analyses of western blotting bands. The analyses were performed by ImageJ. Signal strength of bands of PRMT1 (Top right) and CYP11A1 (bottom right) was normalized by that of β-actin. (B) Knockdown of PRMT1 or CYP11A1 in MDA-MB-231 cells. MBA-MB-231 cells were transfected with a control short hairpin RNA (shRNA) targeting LacZ, and one of four independent shRNAs targeting PRMT1 (clones #1 to #4), or one of two independent shRNAs targeting CYP11A1 (clones #1 to #4). Reduced PRMT1 and CYP11A1 expression, determined by western blot, in sub-cell lines of MDA-MB-231 cells expressing PRMT1 shRNA (clones #3 and #4) or CYP11A1 (clones #2 and #4), compared with controls (parental cell line MDA-MB-231 and control shRNA cells); β-actin levels shown as a loading control. Quantification analyses of western blotting bands. The analyses were performed by ImageJ. Signal strength of bands of PRMT1 (top right) and CYP11A1 (bottom right) was normalized by that of β-actin. (C) Effect of shRNAs targeting either PRMT1 or CYP11A1 on cell motility and invasion of MBA-MB-231 cells. Parental MDA-MB-231 cells and four sub-cell lines of MDA-MB-231 cells that were transfected with either shRNA targeting either LacZ, two independent shRNAs targeting PRMT1 (clones #3 and #4) or two independent shRNAs targeting CYP11A1 (clones #2 and #4) were subjected to Boyden chamber assays. (D) Zebrafish embryos treated with either vehicle (DMSO), 10 μM niclosamide, or 50 µM vinpocetine. Approximately 20 embryos were treated with either DMSO as a vehicle control, niclosamide, or vinpocetine. The treatment was started at 4 hours post fertilization (hpf) when all of embryos reached sphere stage and ended at 9 hpf when control embryos reached 80–90% epiboly stage. Each experiment was performed at least twice. Statistical analysis was determined by Student’s t test.

**Table 2.**
 A list of the drugs that interfere with epiboly progression in zebrafish.Related to Figure 1. A list of positive ‘hit’ drugs that interfered with epiboly progression. Gastrulation defects or status of each of the zebrafish embryos that were treated with either 10 or 50 μM concentrations are indicated.


<table>
  <thead>
    <tr>
      <th>Chemical name</th>
      <th>Chemical formula</th>
      <th>Effect of 10 µM</th>
      <th>Effect of 50 µM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Acitretin</td>
      <td>C21H26O3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Adrenosterone</td>
      <td>C19H24O3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Albendazole</td>
      <td>C12H15N3O2S</td>
      <td>Severe delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Alfadolone acetate</td>
      <td>C23H34O5</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Alfaxalone</td>
      <td>C21H32O3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Alprostadil</td>
      <td>C20H34O5</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Altrenogest</td>
      <td>C21H26O2</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ampiroxicam</td>
      <td>C20H21N3O7S</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Anethole-trithione</td>
      <td>C10H8OS3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Antimycin A</td>
      <td>C28H40N2O9</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Avobenzone</td>
      <td>C20H22O3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Benzoxiquine</td>
      <td>C16H11NO2</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Bosentan</td>
      <td>C27H29N5O6S</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Butoconazole nitrate</td>
      <td>C19H18Cl3N3O3S</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Camptothecine (S,+)</td>
      <td>C20H16N2O4</td>
      <td>Severe delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Carbenoxolone disodium salt</td>
      <td>C34H48Na2O7</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Carmofur</td>
      <td>C11H16FN3O3</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Carprofen</td>
      <td>C15H12ClNO2</td>
      <td>Severe delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Cefdinir</td>
      <td>C14H13N5O5S2</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Celecoxib</td>
      <td>C17H14F3N3O2S</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Chlorambucil</td>
      <td>C14H19Cl2NO2</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Chlorhexidine</td>
      <td>C22H30Cl2N10</td>
      <td>Non-effect</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Ciclopirox ethanolamine</td>
      <td>C14H24N2O3</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Cinoxacin</td>
      <td>C12H10N2O5</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Clofibrate</td>
      <td>C12H15ClO3</td>
      <td>Non-effect</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Clopidogrel</td>
      <td>C16H16ClNO2S</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Clorgyline hydrochloride</td>
      <td>C13H16Cl3NO</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Colchicine</td>
      <td>C22H25NO6</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Deptropine citrate</td>
      <td>C29H35NO8</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Desipramine hydrochloride</td>
      <td>C18H23ClN2</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Diclofenac sodium</td>
      <td>C14H10Cl2NNaO2</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Dicumarol</td>
      <td>C19H12O6</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Diethylstilbestrol</td>
      <td>C18H20O2</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Dimaprit dihydrochloride</td>
      <td>C6H17Cl2N3S</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Disulfiram</td>
      <td>C10H20N2S4</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Dopamine hydrochloride</td>
      <td>C8H12ClNO2</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Eburnamonine (-)</td>
      <td>C19H22N2O</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ethaverine hydrochloride</td>
      <td>C24H30ClNO4</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ethinylestradiol</td>
      <td>C20H24O2</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Ethopropazine hydrochloride</td>
      <td>C19H25ClN2S</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ethoxyquin</td>
      <td>C14H19NO</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Exemestane</td>
      <td>C20H24O2</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ezetimibe</td>
      <td>C24H21F2NO3</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Fenbendazole</td>
      <td>C15H13N3O2S</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Fenoprofen calcium salt dihydrate</td>
      <td>C30H30CaO8</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Fentiazac</td>
      <td>C17H12ClNO2S</td>
      <td>Toxic lethal</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Floxuridine</td>
      <td>C9H11FN2O5</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Flunixin meglumine</td>
      <td>C21H28F3N3O7</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Flutamide</td>
      <td>C11H11F3N2O3</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Fluticasone propionate</td>
      <td>C25H31F3O5S</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Furosemide</td>
      <td>C12H11ClN2O5S</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Gatifloxacin</td>
      <td>C19H22FN3O4</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Gemcitabine</td>
      <td>C9H11F2N3O4</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Gemfibrozil</td>
      <td>C15H22O3</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Gestrinone</td>
      <td>C21H24O2</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Haloprogin</td>
      <td>C9H4Cl3IO</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Hexachlorophene</td>
      <td>C13H6Cl6O2</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Hexestrol</td>
      <td>C18H22O2</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ibudilast</td>
      <td>C14H18N2O</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Idazoxan hydrochloride</td>
      <td>C11H13ClN2O2</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Idazoxan hydrochloride</td>
      <td>C11H13ClN2O2</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Idebenone</td>
      <td>C19H30O5</td>
      <td>Severe delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Indomethacin</td>
      <td>C19H16ClNO4</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ipriflavone</td>
      <td>C18H16O3</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Isotretinoin</td>
      <td>C20H28O2</td>
      <td>Non-effect</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Isradipine</td>
      <td>C19H21N3O5</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Lansoprazole</td>
      <td>C16H14F3N3O2S</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Latanoprost</td>
      <td>C26H40O5</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Leflunomide</td>
      <td>C12H9F3N2O2</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Letrozole</td>
      <td>C17H11N5</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Lithocholic acid</td>
      <td>C24H40O3</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Lodoxamide</td>
      <td>C11H6ClN3O6</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Lofepramine</td>
      <td>C26H27ClN2O</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Loratadine</td>
      <td>C22H23ClN2O2</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Loxapine succinate</td>
      <td>C22H24ClN3O5</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Mebendazole</td>
      <td>C16H13N3O3</td>
      <td>Severe delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Mebendazole</td>
      <td>C22H26N2O2</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Meloxicam</td>
      <td>C14H13N3O4S2</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Methiazole</td>
      <td>C12H15N3O2S</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Mevastatin</td>
      <td>C23H34O5</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>MK 801 hydrogen maleate</td>
      <td>C20H19NO4</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Nabumetone</td>
      <td>C15H16O2</td>
      <td>Non-effect</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Naftopidil dihydrochloride</td>
      <td>C24H30Cl2N2O3</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Nandrolone</td>
      <td>C18H26O2</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Naproxen sodium salt</td>
      <td>C14H13NaO3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Niclosamide</td>
      <td>C13H8Cl2N2O4</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Nifekalant</td>
      <td>C19H27N5O5</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Niflumic acid</td>
      <td>C13H9F3N2O2</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Nimesulide</td>
      <td>C13H12N2O5S</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Nisoldipine</td>
      <td>C20H24N2O6</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Nitazoxanide</td>
      <td>C12H9N3O5S</td>
      <td>Severe delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Norethindrone</td>
      <td>C20H26O2</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Norgestimate</td>
      <td>C23H31NO3</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Oxfendazol</td>
      <td>C15H13N3O3S</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Oxibendazol</td>
      <td>C12H15N3O3</td>
      <td>Severe delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Oxymetholone</td>
      <td>C21H32O3</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Parbendazole</td>
      <td>C13H17N3O2</td>
      <td>Severe delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Parthenolide</td>
      <td>C15H20O3</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Penciclovir</td>
      <td>C10H15N5O3</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Pentobarbital</td>
      <td>C11H18N2O3</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Phenazopyridine hydrochloride</td>
      <td>C11H12ClN5</td>
      <td>Delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Phenothiazine</td>
      <td>C12H9NS</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Phenoxybenzamine hydrochloride</td>
      <td>C18H23Cl2NO</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Pizotifen malate</td>
      <td>C23H27NO5S</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Pramoxine hydrochloride</td>
      <td>C17H28ClNO3</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Prilocaine hydrochloride</td>
      <td>C13H21ClN2O</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Primidone</td>
      <td>C12H14N2O2</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Racecadotril</td>
      <td>C21H23NO4S</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Riluzole hydrochloride</td>
      <td>C8H6ClF3N2OS</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Ritonavir</td>
      <td>C37H48N6O5S2</td>
      <td>Non-effect</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>S(-)Eticlopride hydrochloride</td>
      <td>C17H26Cl2N2O3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Salmeterol</td>
      <td>C25H37NO4</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Streptomycin sulfate</td>
      <td>C42H84N14O36S3</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Sulconazole nitrate</td>
      <td>C18H16Cl3N3O3S</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Tegafur</td>
      <td>C8H9FN2O3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Telmisartan</td>
      <td>C33H30N4O2</td>
      <td>Severe delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Tenatoprazole</td>
      <td>C16H18N4O3S</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Terbinafine</td>
      <td>C21H25N</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Thimerosal</td>
      <td>C9H9HgNaO2S</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Thiorphan</td>
      <td>C12H15NO3S</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Tolcapone</td>
      <td>C14H11NO5</td>
      <td>Severe delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Topotecan</td>
      <td>C23H23N3O5</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Tracazolate hydrochloride</td>
      <td>C16H25ClN4O2</td>
      <td>Severe delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Tribenoside</td>
      <td>C29H34O6</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Triclabendazole</td>
      <td>C14H9Cl3N2OS</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Triclosan</td>
      <td>C12H7Cl3O2</td>
      <td>Delayed</td>
      <td>Severe delayed</td>
    </tr>
    <tr>
      <td>Trioxsalen</td>
      <td>C14H12O3</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Troglitazone</td>
      <td>C24H27NO5S</td>
      <td>Severe delayed</td>
      <td>Toxic lethal</td>
    </tr>
    <tr>
      <td>Valproic acid</td>
      <td>C8H16O2</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Voriconazole</td>
      <td>C16H14F3N5O</td>
      <td>Non-effect</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Zardaverine</td>
      <td>C12H10F2N2O3</td>
      <td>Slightly delayed</td>
      <td>Delayed</td>
    </tr>
    <tr>
      <td>Zuclopenthixol dihydrochloride</td>
      <td>C22H27Cl3N2OS</td>
      <td>Delayed</td>
      <td>Delayed</td>
    </tr>
  </tbody>
</table>

### Identified drugs suppressed cell motility and invasion of human cancer cells

It has been reported that zebrafish have orthologues to 86% of 1318 human drug targets (Gunnarsson et al., 2008). However, it was not known whether the epiboly-interrupting drugs could suppress metastatic dissemination of human cancer cells. To test this, we subjected the 78 epiboly-interrupting drugs that showed a suppressor effect on epiboly progression at a 10 μM concentration to in vitro experiments using a human cancer cell line. The experiments examined whether the drugs could suppress cell motility and invasion of MDA-MB-231 cells through a Boyden chamber. Before conducting the experiment, we investigated whether these drugs might affect viability of MDA-MB-231 cells using an MTT assay. Out of the 78 drugs, 16 of them strongly affected cell viability at concentrations less than 1 μM and were not used in the cell motility experiments. The remaining 62 drugs were assayed in Boyden chamber motility experiments. Out of the 62 drugs, 20 of the drugs inhibited cell motility and invasion of MDA-MB-231 cells without affecting cell viability. Among the 20 drugs, hexachlorophene and nitazoxanide were removed since the primary targets of the drugs, D-lactate dehydrogenase and pyruvate ferredoxin oxidoreductase, are not expressed in mammalian cells. With the exception of ipriflavone, whose target is still unclear, the known primary targets of the remaining 17 drugs are reported to be expressed by mammalian cells (Figure 2A and Table 3).

![Figure 2.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig2-v2.jpg)

**Figure 2.:** (A) Effect of the epiboly-interrupting drugs on cell motility and invasion of MBA-MB-231 cells. MBA-MB-231 cells were treated with vehicle or each of the epiboly-interrupting drugs and then subjected to Boyden chamber assays. Fetal bovine serum (1% v/v) was used as the chemoattractant in both assays. Each experiment was performed at least twice. (B) Western blot analysis of HTR2C levels (top) in a non-metastatic human cancer cell line, MCF7 (breast) and highly metastatic human cancer cell lines, MDA-MB-231 (breast), MDA-MB-435 (melanoma), PC9 (lung), MIA-PaCa2 (pancreas), PC3 (prostate), and SW620 (colon); GAPDH loading control is shown (bottom). (C) Effect of pizotifen on cell motility and invasion of MBA-MB-231, MDA-MB-435, and PC9 cells. Either vehicle or pizotifen treated the cells were subjected to Boyden chamber assays. Fetal bovine serum (1% v/v) was used as the chemoattractant in both assays. Each experiment was performed at least twice. (D) and (E) Representative images of dissemination of 231R, shLacZ 231R or shHTR2C 231R cells in zebrafish xenotransplantation model. The fish larvae that were inoculated with 231R cells were treated with either vehicle (top left) or the drug (lower left) (D). The fish larvae that were inoculated with either shLacZ 231R or shHTR2C 231R cells (lower left) (E). White arrows head indicate disseminated 231R cells. The images were shown in 4× magnification. Scale bar, 100 µm. The mean frequencies of the fish showing head, trunk, or end-tail dissemination were counted (graph on right). Each value is indicated as the mean ± SEM of two independent experiments. Statistical analysis was determined by Student’s t test.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Quantification analyses of western blotting bands in Figure 2B. The analyses were performed by ImageJ. Signal strength of bands of HTR2C (left) and DRD2 (right) was normalized by that of GAPDH. (B) Western blot analysis of DRD2 levels in non-metastatic human cancer cell line, MCF7 (breast) and highly metastatic human cancer cell lines, MDA-MB-231 (breast), MDA-MB-435 (melanoma), MIA-PaCa2 (pancreas), PC3 (prostate), and SW620 (colon); GAPDH loading control is shown (bottom). GAPDH control was obtained in the same experiment from Figure 2B. (C) Effect of S(-)eticlopride hydrochloride on cell motility and invasion of MBA-MB-231, MDA-MB-435, and PC9 cells. Either vehicle- or pizotifen-treated cells were subjected to Boyden chamber assays. Fetal bovine serum (1% v/v) was used as the chemoattractant in both assays. Each experiment was performed at least twice. Statistical analysis was determined by Student’s t test.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Representative images of dissemination of 231R cells in zebrafish xenotransplantation model. The fish larvae that were inoculated with 231R cells were treated with either vehicle (top left, bottom left) or pizotifen (top right, bottom right). (B) Representative images of dissemination of MIA-PaCa2 cells in zebrafish xenotransplantation model. The fish were inoculated with MIA-PaCa2 cells, and treated with either vehicle (top left) or drug (lower left). White arrow heads indicate disseminated MIA-PaCa2 cells. The images were shown in 4× magnification. Scale bar, 100 μm. The mean frequencies of the fish showing head, trunk, or end-tail dissemination were tabulated (right). Each value is indicated as the mean ± SEM of two independent experiments. Statistical analysis was determined by Student’s t test.

**Table 3.**
 Primary targets of the identified drugs.


<table>
  <thead>
    <tr>
      <th>The identified drugs</th>
      <th>Primary targets of the identified drugs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hexachlorophene</td>
      <td>D-Lactate dehydrogenase (D-LDH), not expressed in mammalian cells</td>
    </tr>
    <tr>
      <td>Troglitazone</td>
      <td>Agonist for peroxisome proliferator-activated receptor α and γ (PPARα and -γ)</td>
    </tr>
    <tr>
      <td>Pizotifen malate</td>
      <td>5-Hydroxytryptamine receptor 2C (HTR2C)</td>
    </tr>
    <tr>
      <td>Salmeterol</td>
      <td>Adrenergic receptor beta 2 (ADRB2)</td>
    </tr>
    <tr>
      <td>Nitazoxanide</td>
      <td>Pyruvate ferredoxin oxidoreductase (PFOR), not expressed in mammalian cells</td>
    </tr>
    <tr>
      <td>Valproic acid</td>
      <td>Histone deacetylases (HDACs)</td>
    </tr>
    <tr>
      <td>Dicumarol</td>
      <td>NAD(P)H dehydrogenase quinone 1 (NQO1)</td>
    </tr>
    <tr>
      <td>Loxapine succinate</td>
      <td>Dopamine receptor D2 and D4 (DRD2 and DRD4)</td>
    </tr>
    <tr>
      <td>Adrenosterone</td>
      <td>Hydroxysteroid (11-beta) dehydrogenase 1 (HSD11β1)</td>
    </tr>
    <tr>
      <td>Riluzole hydrochloride</td>
      <td>Glutamate R andvoltage-dependent Na+ channel</td>
    </tr>
    <tr>
      <td>Naftopidil dihydrochloride</td>
      <td>5-Hydroxytryptamine receptor 1A (HTR1A) andα1-adrenergic receptor (AR)</td>
    </tr>
    <tr>
      <td>S(-)Eticlopride hydrochloride</td>
      <td>Dopamine receptor D2 (DRD2)</td>
    </tr>
    <tr>
      <td>Racecadotril</td>
      <td>Membrane metallo-endopeptidase (MME)</td>
    </tr>
    <tr>
      <td>Ipriflavone</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>Flurbiprofen</td>
      <td>Cyclooxygenase 1 and 2 (Cox1 and -2)</td>
    </tr>
    <tr>
      <td>Zardaverine</td>
      <td>Phosphodiesterase III/IV (PDE3/4)</td>
    </tr>
    <tr>
      <td>Leflunomide</td>
      <td>Dihydroorotate dehydrogenase (DHODH)</td>
    </tr>
    <tr>
      <td>Olmesartan</td>
      <td>Angiotensin II receptor alpha</td>
    </tr>
    <tr>
      <td>Disulfiram</td>
      <td>Aldehyde dehydrogenase (ALDH)Dopamine β-hydroxylase (DBH)</td>
    </tr>
    <tr>
      <td>Zuclopenthixol dihydrochloride</td>
      <td>Dopamine receptors D1 and D2 (DRD1 and -2)</td>
    </tr>
  </tbody>
</table>

We confirmed that highly metastatic human cancer cell lines expressed target genes through western blotting analyses. Among the genes, serotonin receptor 2C (HTR2C), which is a primary target of pizotifen, was highly expressed in only metastatic cell lines (Figure 2B and Figure 2—figure supplement 2A). Clinical data also shows that that HTR2C expression is correlated with tumor stage of breast cancer patients and is higher in metastatic and Her2/neu-overexpressing tumors (Pai et al., 2009). Pizotifen suppressed cell motility and invasion of several highly metastatic human cancer cell lines in a dose-dependent manner (Figure 2C). Similarly, dopamine receptor D2 (DRD2), which is a primary target of S(-)eticlopride hydrochloride, was highly expressed in only metastatic cell lines, and the drug suppressed cell motility and invasion of these cells in a dose-dependent manner (Figure 2—figure supplement 2A-C).

These results indicate that a number of the epiboly-interrupting drugs also have suppressor effects on cell motility and invasion of highly metastatic human cancer cells.

### Pizotifen suppressed metastatic dissemination of human cancer cells in a zebrafish xenotransplantation model

While a number of the epiboly-interrupting drugs suppressed cell motility and invasion of human cell lines in vitro, it was still unclear whether the drugs could suppress metastatic dissemination of cancer cells in vivo. Therefore, we examined whether the identified drugs could suppress metastatic dissemination of these human cancer cells in a zebrafish xenotransplantation model. Pizotifen was selected to test since HTR2C was overexpressed only in highly metastatic cell lines supporting the hypothesis that it could be a novel target for blocking metastatic dissemination of cancer cells (Figure 2B). Red fluorescent protein (RFP)-labelled MDA-MB-231 (231R) cells were injected into the duct of Cuvier of Tg (kdrl:eGFP) zebrafish at 2 dpf and then maintained in the presence of either vehicle or pizotifen. Twenty-four hours post injection, the numbers of fish showing metastatic dissemination of 231R cells were measured via fluorescence microscopy. In this model, the dissemination patterns were generally divided into three categories: (i) head dissemination, in which disseminated 231R cells exist in the vessel of the head part; (ii) trunk dissemination, in which the cells were observed in the vessel dilating from the trunk to the tail; (iii) end-tail dissemination, in which the cells were observed in the vessel of the end-tail part (Nakayama et al., 2020).

Three independent experiments revealed that the frequencies of fish in the drug-treated group showing head, trunk, or end-tail dissemination significantly decreased to 55.3% ± 7.5%, 28.5 ± 5.0%, or 43.5% ± 19.1% when compared with those in the vehicle-treated group; 95.8% ± 5.8%, 47.1 ± 7.7%, or 82.6% ± 12.7%. Conversely, the frequency of the fish in the drug-treated group not showing any dissemination significantly increased to 45.4% ± 0.5% when compared with those in the vehicle-treated group; 2.0% ± 2.9% (Figure 2D, Figure 2—figure supplement 2 and Table 4).

**Table 4.**
 Effects of pharmacological inhibition of HTR2C on metastatic dissemination of MDA-MB-231 cells in zebrafish xenografted models.Related to Figure 2D. The numbers and frequencies of the fish showing the dissemination patterns in vehicle- or pizotifen-treated group were indicated. The fish showed both patterns of dissemination were redundantly counted in this analysis.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Experiment_#1</th>
      <th>Experiment_#2</th>
      <th>Experiment_#3</th>
      <th>Average of experiments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Drug: VehicleCell: MDA-MB-231</td>
      <td>Non-dissemination</td>
      <td>0% n1 = 0/17</td>
      <td>0% n2 = 0/12</td>
      <td>6.66% n3 = 1/15</td>
      <td>2.22% ± 3.84%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>58.82% n1 = 10/17</td>
      <td>91.66% n2 = 11/12</td>
      <td>6.66% n3 = 1/15</td>
      <td>72.38% ± 17.15%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>52.94% n1 = 9/17</td>
      <td>8.33% n2 = 1/12</td>
      <td>20% n3 = 2/15</td>
      <td>27.09% ± 23.13%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>100% n1 = 17/17</td>
      <td>100% n2 = 12/12</td>
      <td>86.66% n3 = 13/15</td>
      <td>95.55% ± 7.69%</td>
    </tr>
    <tr>
      <td rowspan="4">Drug: PizotifenCell: MDA-MB-231</td>
      <td>Non-dissemination</td>
      <td>55% n1 = 11/20</td>
      <td>31.57% n2 = 6/19</td>
      <td>45.45 % n3 = 10/22</td>
      <td>44.01% ± 11.77%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>5% n1 = 1/20</td>
      <td>31.57% n2 = 6/19</td>
      <td>18.18% n3 = 4/22</td>
      <td>18.25% ± 13.28%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>5% n1 = 1/20</td>
      <td>10.52% n2 = 2/19</td>
      <td>4.45% n3 = 1/22</td>
      <td>6.69% ± 3.32%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>45% n1 = 9/20</td>
      <td>57.89% n2 = 11/19</td>
      <td>50% n3 = 11/22</td>
      <td>50.96% ± 6.50%</td>
    </tr>
  </tbody>
</table>

Similar effects were observed in another xenograft experiments using an RFP-labelled human pancreatic cancer cell line, MIA-PaCa-2 (MP2R). In the drug-treated group, the frequencies of the fish showing head, trunk, or end-tail dissemination significantly decreased to 15.3% ± 6.7%, 6.2% ± 1.3%, or 41.1% ± 1.5%; conversely, the frequency of the fish not showing any dissemination significantly increased to 46.3% ± 8.9% when compared with those in the vehicle-treated group; 74.5% ± 11.1%, 18.9% ± 14.9%, 77.0% ± 9.0%, or 17.2% ± 0.7% (Figure 2—figure supplement 2A and Table 5).

**Table 5.**
 Effects of pharmacological inhibition of HTR2C on metastatic dissemination of Mia-PaCa2 cells in zebrafish xenografted models.Related to Figure 4. The numbers and frequencies of the fish showing the dissemination patterns in vehicle- or pizotifen-treated group were indicated. The fish showed both patterns of dissemination were redundantly counted in this analysis.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Experiment_#1</th>
      <th>Experiment_#2</th>
      <th>Average of experiments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Drug: VehicleCell: MIA-PaCa2</td>
      <td>Non-dissemination</td>
      <td>17.64% n1 = 3/17</td>
      <td>16.66% n2 = 2/12</td>
      <td>17.15% + 0.69%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>82.35% n1 = 14/17</td>
      <td>66.66% n2 = 8/12</td>
      <td>74.50% + 11.09%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>29.41% n1 = 5/17</td>
      <td>8.33% n2 = 1/12</td>
      <td>18.87% + 14.90%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>70.58% n1 = 12/17</td>
      <td>83.33% n2 = 10/17</td>
      <td>76.96% + 9.01</td>
    </tr>
    <tr>
      <td rowspan="4">Drug: PizotifenCell: MIA-PaCa2</td>
      <td>Non-dissemination</td>
      <td>40% n1 = 4/10</td>
      <td>52.63% n2 = 10/19</td>
      <td>46.31% + 8.93%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>20% n1 = 2/10</td>
      <td>10.52% n2 = 2/19</td>
      <td>15.26% + 6.69%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>10% n1 = 1/10</td>
      <td>5.26% n2 = 1/19</td>
      <td>7.63% + 3.34%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>40% n1 = 4/10</td>
      <td>42.05% n2 = 8/19</td>
      <td>41.4% + 1.48%</td>
    </tr>
  </tbody>
</table>

To eliminate the possibility that the metastasis suppressing effects of pizotifen might result from off-target effects of the drug, we conducted validation experiments to determine whether knockdown of HTR2C would show the same effects. Sub-clones of 231R cells that expressed short hairpin RNA (shRNA) targeting either LacZ or HTR2C were injected into the fish at 2 dpf and the fish were maintained in the absence of drug. In the fish that were inoculated with shHTR2C 231R cells, the frequencies of the fish showing head, trunk, and end-tail dissemination significantly decreased to 6.7% ± 4.9%, 6.7% ± 0.7%, or 20.0% ± 16.5%; conversely, the frequency of the fish not showing any dissemination significantly increased to 80.0% ± 4.4% when compared with those that were inoculated with shLacZ 231R cells; 80.0% ± 27.1%, 20.0% ± 4.5%, 90.0% ± 7.7%, or 0% (Figure 2E and Table 6).

**Table 6.**
 Effects of genetic inhibition of HTR2C on metastatic dissemination of MDA-MB-231 cells in zebrafish xenografted models.Related to Figure 2E. The numbers and frequencies of the fish showing the dissemination patterns in the zebrafish that were inoculated with either shLacZ or shHTR2C MDA-MB-231 cells were indicated. The fish showed both patterns of dissemination were redundantly counted in this analysis.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Experiment_#1</th>
      <th>Experiment_#2</th>
      <th>Average of experiments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">shLacZ</td>
      <td>Non-dissemination</td>
      <td>0% n1 = 0/10</td>
      <td>0% n2 = 0/10</td>
      <td>0%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>60% n1 = 6/10</td>
      <td>100% n2 = 10/10</td>
      <td>80%± 28.28%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>30% n1 = 3/10</td>
      <td>10% n2 = 1/10</td>
      <td>20% ± 14.14%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>80% n1 = 8/10</td>
      <td>100% n2 = 10/10</td>
      <td>90% ± 14.14</td>
    </tr>
    <tr>
      <td rowspan="4">shHTR2C</td>
      <td>Non-dissemination</td>
      <td>80% n1 = 12/15</td>
      <td>76.84% n2 = 14/19</td>
      <td>76.84 ± 4.46%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>6.66% n1 = 1/15</td>
      <td>15.78% n2 = 3/19</td>
      <td>11.22% ± 6.45%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>6.66% n1 = 1/15</td>
      <td>5.26% n2 = 1/19</td>
      <td>5.96% ± 0.99%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>20% n1 = 3/15</td>
      <td>26.31% n2 = 5/19</td>
      <td>23.15% ± 4.46%</td>
    </tr>
  </tbody>
</table>

These results indicate that pharmacological and genetic inhibition of HTR2C suppressed metastatic dissemination of human cancer cells in vivo.

### Pizotifen suppressed metastasis progression of a mouse model of metastasis

We examined the metastasis-suppressor effect of pizotifen in a mouse model of metastasis (Tao et al., 2008). Luciferase-expressing 4T1 murine mammary carcinoma cells were inoculated into the mammary fat pads (MFP) of female BALB/c mice. On day 2 post inoculation, the mice were randomly assigned to two groups and one group received once daily intraperitoneal injections of 10 mg/kg pizotifen while the other group received a vehicle injection. Bioluminescence imaging and tumor measurement revealed that the sizes of the primary tumors in pizotifen-treated mice were equal to those in the vehicle-treated mice on day 10 post inoculation. The primary tumors were resected after the analyses. Immunofluorescence (IF) staining also demonstrated that the percentage of Ki67-positive cells in the resected primary tumors of pizotifen-treated mice were the same as those of vehicle-treated mice (Figure 3A–C), additionally, both groups showed less than 1% cleaved caspase 3 positive cells (Figure 3—figure supplement 1). Therefore, no anti-tumor effect of pizotifen was observed on the primary tumor. After 70 days from inoculation, bioluminescence imaging detected light emitted in the lungs, livers, and lymph nodes of vehicle-treated mice but not those of pizotifen-treated mice (Figure 3C). Vehicle-treated mice formed 5–50 metastatic nodules per lung in all 10 mice analyzed; conversely, pizotifen-treated mice (n = 10) formed 0–5 nodules per lung in all 10 mice analyzed (Figure 3D). Histological analyses confirmed that metastatic lesions in the lungs were detected in all vehicle-treated mice; conversely, they were detected in only 2 of 10 pizotifen-treated mice and the rest of the mice showed metastatic colony formations around the bronchiole of the lung. In addition, 4 of 10 vehicle-treated mice exhibited metastasis in the liver and the rest showed metastatic colony formation around the portal tract of the liver. In contrast, none of 10 pizotifen-treated mice showed liver metastases and only half of the 10 mice showed metastatic colony formation around the portal tract (Figure 3E). These results indicate that pizotifen can suppress metastasis progression without affecting primary tumor growth.

![Figure 3.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig3-v2.jpg)

**Figure 3.:** (A) Mean volumes (n = 10 per group) of 4T1 primary tumors formed in the mammary fat pad of either vehicle- or pizotifen-treated mice at day 10 post injection. (B) Ki67 expression level in 4T1 primary tumors formed in the mammary fat pad of either vehicle- or pizotifen-treated mice at day 10 post injection. The mean expression levels of Ki67 (n = 10 mice per group) were determined and were calculated as the mean ration of Ki67-positive cells to 4’,6-diamidino-2-phenylindole (DAPI) area. (C) Representative images of primary tumors on day 10 post injection (top panels) and metastatic burden on day 70 post injection (bottom panels) taken using an IVIS Imaging System. (D) Representative images of the lungs from either vehicle- (top) or pizotifen-treated mice (bottom) at 70 days post tumor inoculation. Number of metastatic nodules in the lung of either vehicle- or pizotifen-treated mice (right). (E) Representative hematoxylin and eosin (H&E) staining of the lung (top) and liver (bottom) from either vehicle- or pizotifen-treated mice. Black arrow heads indicate metastatic 4T1 cells. (F) The mean number of metastatic lesions in step sections of the lungs from the mice that were inoculated with 4T1-12B cells expressing short hairpin RNA (shRNA) targeting for either LacZ or HTR2C. (G) Representative H&E staining of the lung and liver from the mice that were inoculated with 4T1-12B cells expressing shRNA targeting for either LacZ or HTR2C. Black arrow heads indicate metastatic 4T1 cells. Each value is indicated as the mean ± SEM. Statistical analysis was determined by Student’s t test.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig3-figsupp1-v2.jpg)

To eliminate the possibility that the metastasis suppressing effects of pizotifen might result from off-target effects, we conducted validation experiments to determine whether knockdown of HTR2C would show the same effects. The basic experimental process followed the experimental design described above except that sub-clones of 4T1 cells that expressed shRNA targeting either LacZ or HTR2C were injected into the MFP of female BALB/c mice and the mice were maintained without drug. Histological analyses revealed that all of the mice (n = 5) that were inoculated with 4T1 cells expressing shRNA targeting LacZ showed metastases in the lungs. The mean number of metastatic lesions in a lung was 26.4 ± 7.8. In contrast, only one of the mice (n = 5) were inoculated with 4T1 cells expressing shRNA targeting HTR2C showed metastases in the lungs and the rest of the mice showed metastatic colony formation around the bronchiole of the lung. The mean number of metastatic lesions in the lung significantly decreased to 10% of those of mice that were inoculated with 4T1 cells expressing shRNA targeting LacZ (Figure 3F–H).

Taken together, pharmacological and genetic inhibition of HTR2C showed an anti-metastatic effect in the 4T1 model system.

### HTR2C promoted EMT-mediated metastatic dissemination of human cancer cells

Although pharmacological and genetic inhibition of HTR2C inhibited metastasis progression, a role for HTR2C on metastatic progression has not been reported. Therefore, we examined whether HTR2C could confer metastatic properties on poorly metastatic cells.

First, we established a stable sub-clone of MCF7 human breast cancer cells expressing either vector control or HTR2C. Vector control expressing MCF7 cells maintained highly organized cell-cell adhesion and cell polarity; however, HTR2C-expressing MCF7 cells led to loss of cell-cell contact and cell scattering. The cobblestone-like appearance of these cells was replaced by a spindle-like, fibroblastic morphology. Western blotting and IF analyses revealed that HTR2C-expressing MCF7 cells showed loss of E-cadherin and EpCAM, and elevated expressions of N-cadherin, vimentin, and an EMT-inducible transcriptional factor ZEB1. Similar effects were validated through another experiment using an immortal keratinocyte cell line, HaCaT cells, in that HTR2C-expressing HaCaT cells also showed loss of cell-cell contact and cell scattering with loss of epithelial markers and gain of mesenchymal markers (Figure 4A–C and Figure 4—figure supplement 1A). Therefore, both the morphological and molecular changes in the HTR2C-expressing MCF7 and HaCaT cells demonstrated that these cells had undergone an EMT.

![Figure 4.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig4-v2.jpg)

**Figure 4.:** (A) The morphologies of the MCF7 and HaCaT cells expressing either the control vector or HTR2C were revealed by phase contrast microscopy. (B) Immunofluorescence staining of E-cadherin, EpCAM, vimentin, and N-cadherin expressions in the MCF7 cells from A. (C) Expression of E-cadherin, EpCAM, vimentin, N-cadherin, and HTR2C was examined by western blotting in the MCF7 and HaCaT cells; GAPDH loading control is shown (bottom). (D) Effect of HTR2C on cell motility and invasion of MCF7 cells. MCF7 cells were subjected to Boyden chamber assays. Fetal bovine serum (1% v/v) was used as the chemoattractant in both assays. Each experiment was performed at least twice. (E) Representative images of dissemination patterns of MCF7 cells expressing either the control vector (top left) or HTR2C (lower left) in a zebrafish xenotransplantation model. White arrow heads indicate disseminated MCF7 cells. The mean frequencies of the fish showing head, trunk, or end-tail dissemination tabulated (right). Each value is indicated as the mean ± SEM of two independent experiments. Statistical analysis was determined by Student’s t test.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Quantification analyses of western blotting bands in Figure 4C. The analyses were performed by ImageJ. Signal strength of bands of E-cadherin, EpCAM, N-cadherin, vimentin, ZEB1, and HTR2C was normalized by that of GAPDH. (B) Representative images of dissemination patterns of MCF7 cells expressing either the control vector (top left, middle left, bottom left) or HTR2C (top right, middle right, bottom right) in a zebrafish xenotransplantation model.

Next, we examined whether HTR2C-driven EMT could promote metastatic dissemination of human cancer cells. Boyden chamber assay revealed that HTR2C expressing MCF7 cells showed an increased cell motility and invasion compared with vector control-expressing MCF7 cells in vitro (Figure 4D). Moreover, we conducted in vivo examination of whether HTR2C expression could promote metastatic dissemination of human cancer cells in a zebrafish xenotransplantation model. RFP-labelled MCF7 cells expressing either vector control or HTR2C were injected into the duct of Cuvier of Tg (kdrl:eGFP) zebrafish at 2 dpf. Twenty-four hours post injection, the frequencies of the fish showing metastatic dissemination of the inoculated cells were measured using fluorescence microscopy. In the fish that were inoculated with HTR2C expressing MCF7 cells, the frequencies of the fish showing head, trunk, and end-tail dissemination significantly increased to 96.7% ± 4.7%, 68.8% ± 6.4%, or 89.5% ± 3.4%; conversely, the frequency of the fish not showing any dissemination decreased to 0% when compared with those in the fish that were inoculated with vector control expressing MCF7 cells; 33.1% ± 18.5%, 0%, 56.9% ± 4.4%, or 43% (Figure 4E, Figure 4—figure supplement 1B and Table 7).

**Table 7.**
 Effects of HTR2C overexpression on metastatic dissemination of MCF7 cells in zebrafish xenografted models.Related to Figure 4E. The numbers and frequencies of the fish showing the dissemination patterns in the zebrafish that were inoculated with MCF7 cells expressing either vector control (VC) or HTR2C were indicated. The fish showed both patterns of dissemination were redundantly counted in this analysis.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Experiment_#1</th>
      <th>Experiment_#2</th>
      <th>Average of experiments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">VC</td>
      <td>Non-dissemination</td>
      <td>46.15% n1 = 6/13</td>
      <td>40% n2 = 4/10</td>
      <td>43.07% ± 4.35%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>46.15% n1 = 6/13</td>
      <td>20% n2 = 2/10</td>
      <td>33.07% ± 18.49%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>0% n1 = 0/13</td>
      <td>0% n2 = 0/10</td>
      <td>0%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>53.84% n1 = 7/13</td>
      <td>60% n2 = 6/10</td>
      <td>56.92% ± 4.35%</td>
    </tr>
    <tr>
      <td rowspan="4">HTR2C</td>
      <td>Non-dissemination</td>
      <td>0% n1 = 0/14</td>
      <td>0% n2 = 0/15</td>
      <td>0%</td>
    </tr>
    <tr>
      <td>Head</td>
      <td>100% n1 = 14/14</td>
      <td>93.33% n2 = 14/15</td>
      <td>96.66% ± 4.71%</td>
    </tr>
    <tr>
      <td>Trunk</td>
      <td>64.28% n1 = 9/14</td>
      <td>73.33% n2 = 11/15</td>
      <td>68.80% ± 6.39%</td>
    </tr>
    <tr>
      <td>End-tail</td>
      <td>85.71% n1 = 12/14</td>
      <td>93.33% n2 = 14/15</td>
      <td>89.52% ± 5.38%</td>
    </tr>
  </tbody>
</table>

These results indicated that HTR2C promoted metastatic dissemination of cancer cells through induction of EMT, and suggest that the screen can easily be converted to a chemical genetic screening platform.

### Pizotifen induced mesenchymal-to-epithelial transition through inhibition of Wnt signaling

Finally, we elucidated the mechanism of action of how pizotifen suppressed metastasis, especially metastatic dissemination of cancer cells. Our results showed that HTR2C induced EMT and that pharmacological and genetic inhibition of HTR2C suppressed metastatic dissemination of MDA-MB-231 cells that had already transitioned to mesenchymal-like traits via EMT. Therefore, we speculated that blocking HTR2C with pizotifen might inhibit the molecular mechanisms which follow EMT induction. We first investigated the expressions of epithelial and mesenchymal markers in pizotifen-treated MDA-MB-231 cells since the activation of an EMT program needs to be transient and reversible, and transition from a fully mesenchymal phenotype to a epithelial-mesenchymal hybrid state or a fully epithelial phenotype is associated with malignant phenotypes (Kröger et al., 2019). IF and FACS analyses revealed 20% of pizotifen-treated MDA-MB-231 cells restored E-cadherin expression. Also, western blotting analysis demonstrated that 4T1 primary tumors from pizotifen-treated mice has elevated E-cadherin expression compared with tumors from vehicle-treated mice (Figure 5A–C and Figure 5—figure supplement 1). However, mesenchymal markers did not change between vehicle and pizotifen-treated MDA-MB-231 cells (data not shown). We further analyzed E-cadherin-positive (E-cad+) cells in pizotifen-treated MDA-MB-231 cells. The E-cad+ cells showed elevated expressions of epithelial markers KRT14 and KRT19; and decreased expression of mesenchymal makers vimentin, MMP1, MMP3, and S100A4. Recent research reports that an EMT program needs to be transient and reversible and that a mesenchymal phenotype in cancer cells is achieved by constitutive ectopic expression of ZEB1. In accordance with the research, the E-cad+ cells and 4T1 primary tumors from pizotifen-treated mice had decreased ZEB1 expression compared with vehicle-treated cells and tumors from vehicle-treated mice (Figure 5D and Figure 5—figure supplement 2). In contrast, HTR2C-expressing MCF7 and HuMEC cells expressed ZEB1 but not vehicle control MCF7 and HuMEC cells (Figure 4C and Figure 5—figure supplement 3). HTR2C-expressing MCF7 cells expressed not only ZEB1 but also Twist1 and Snail. In contrast, pizotifen-treated MDA-MB-231 cells showed decreased expression of ZEB1 and Twist1 compared with that in vehicle-treated cells. Furthermore, in the primary tumors of pizotifen-treated mice, only ZEB1 expression was decreased compared with those of vehicle-treated mice. These results indicate that HTR2C-mediated signaling induced EMT through up-regulation of ZEB1 and blocking HTR2C with pizotifen induced mesenchymal-to-epithelial transition through down-regulation of ZEB1 (Figure 5—figure supplement 4).

![Figure 5.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig5-v2.jpg)

**Figure 5.:** (A) Immunofluorescence (IF) staining of E-cadherin in either vehicle- or pizotifen-treated MDA-MB-231 cells. (B) Surface expression of E-cadherin in either vehicle (black)- or pizotifen (red)-treated MDA-MB-231 cells by FACS analysis. Non-stained controls are shown in gray. (C) Protein expressions levels of E-cadherin, ZEB1, and β-catenin in the cytoplasm and nucleus of 4T1 primary tumors from either vehicle- or pizotifen-treated mice are shown; Luciferase, histone H3, and β-tubulin are used as loading control for whole cell, nuclear, or cytoplasmic lysate, respectively. (D) Protein expression levels of epithelial and mesenchymal markers and ZEB1 in either vehicle- or pizotifen-treated MDA-MB-231 cells or E-cadherin-positive (E-cad+) cells in pizotifen-treated MDA-MB-231 cells are shown. (E) IF staining of β-catenin in the MCF7 cells expressing either vector control (top left, bottom left) or HTR2C (top right, bottom right). (F) Expressions of β-catenin in the cytoplasm and nucleus of MCF7 cells. (G) IF staining of β-catenin in either vehicle (top left, bottom left) or pizotifen-treated MDA-MB-231 cells (top right, bottom right). (H) Expressions of β-catenin in the cytoplasm and nucleus of MDA-MB-231 cells and the E-cad+ cells.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The analyses were performed by ImageJ. Signal strength of bands of E-cadherin, EpCAM, p-GSK-3β, GSK-3β were normalized by that of luciferase. Signal strength of bands of nuclear and cytoplasmic β-catenin was normalized by that of histone H3 and β-tubulin, respectively.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The analyses were performed by ImageJ. Signal strength of bands of E-cadherin, EpCAM, KRT18, KRT19, MMP1, MMP3, vimentin, and S100A4 was normalized by that of GAPDH.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** The analyses were performed by ImageJ. Signal strength of bands of nuclear and cytoplasmic β-catenin was normalized by that of histone H3 and β-tubulin, respectively. Signal strength of bands of p-GSK-3β and GSK-3β was normalized by that of GAPDH.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** Protein expression levels of Twist1 in either vehicle- or pizotifen-treated MDA-MB-231 cells are shown (middle): GAPDH loading control is shown (bottom). Protein expression levels of Snail and Twist1 of 4T1 primary tumors from either vehicle- or pizotifen-treated mice are shown (right); luciferase is used as loading control for whole cell. Luciferase control was obtained in the same experiment from Figure 5C.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/70151/elife-70151-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** The analyses were performed by ImageJ. Signal strength of bands of nuclear and cytoplasmic β-catenin was normalized by that of histone H3 and β-tubulin, respectively. Signal strength of bands of p-GSK-3β and GSK-3β was normalized by that of GAPDH.

We further investigated the mechanism of action of how blocking HTR2C with pizotifen induced down-regulation of ZEB1. In embryogenesis, serotonin-mediated signaling is required for Wnt-dependent specification of the superficial mesoderm during gastrulation (Beyer et al., 2012). Wnt signaling plays critical role in inducing EMT. In cancer cells, overexpression of HTR1D is associated with Wnt signaling (Sui et al., 2015; Zhan et al., 2017). This evidence led to a hypothesis that HTR2C-mediated signaling might turn on transcriptional activity of β-catenin and that might induce up-regulation of EMT-TFs. IF analyses revealed β-catenin was accumulated in the nucleus of HTR2C-expressing MCF7 cells but it was located in the cytoplasm of vector control-expressing cells (Figure 5E). Nuclear accumulation of β-catenin in HTR2C-expressing MCF7 cells was confirmed by western blot (Figure 5F and Figure 5—figure supplement 2). In contrast, pizotifen-treated MDA-MB-231 cells showed β-catenin located in the cytoplasm of the cells. Vehicle-treated cells showed that β-catenin accumulated in the nucleus of the cells. (Figure 5G), and western blotting analysis confirmed that it was located in the cytoplasm of pizotifen-treated MDA-MB-231 cells (Figure 5H and Figure 5—figure supplement 5). Furthermore, immunohistochemistry and western blotting analyses showed that β-catenin accumulated in the nucleus, and phospho-GSKβ and ZEB1 expression were decreased in 4T1 primary tumors from pizotifen-treated mice compared with vehicle-treated mice (Figure 5C and Figure 5—figure supplement 1). These results indicated that HTR2C would regulate transcriptional activity of β-catenin and pizotifen could inhibit it.

Taken together, we conclude that blocking HTR2C with pizotifen restored epithelial properties to metastatic cells (MDA-MB-231 and 4T1 cells) through a decrease of transcriptional activity of β-catenin and that suppressed metastatic progression of the cells.

## Discussion

Reducing or eliminating mortality associated with metastatic disease is a key goal of medical oncology, but few models exist that allow for rapid, effective screening of novel compounds that target the metastatic dissemination of cancer cells. Based on accumulated evidence that at least 50 genes play an essential role in governing both metastasis and gastrulation progression (Table 1), we hypothesized that small molecule inhibitors that interrupt gastrulation of zebrafish embryos might suppress metastatic progression of human cancer cells. We created a unique screening concept utilizing gastrulation of zebrafish embryos to test the hypothesis. Our results clearly confirmed our hypothesis: 25.6% (20/76 drugs) of epiboly-interrupting drugs could also suppress cell motility and invasion of highly metastatic human cell lines in vitro. In particular, pizotifen, which is an antagonist for serotonin receptor 2C and one of the epiboly-interrupting drugs, could suppress metastasis in a mouse model (Figure 3A–E). Thus, this screen could offer a novel platform for discovery of anti-metastasis drugs.

Among the 20 drugs which suppressed both epiboly progression and cell motility and invasion of MDA-MB-231 cells, hexachlorophene and troglitazone showed the strongest effect on suppressing cell motility and invasion of MDA-MB-231 cells. However, the drug could not suppress cell motility and invasion of other highly metastatic human cancer cell lines: MDA-MB-435 and PC3. With the exception of pizotifen and S(-)eticlopride hydrochloride, the remaining 18 drugs could not show the suppressor effect on more than three highly metastatic human cancer cell lines. These results indicate that the strength of interrupting effect of a drug on epiboly progression is not proportional to the strength of suppressing effect of the drug on metastasis.

We have provided the first evidence that HTR2C, which is a primary target of pizotifen, induced EMT and promoted metastatic dissemination of cancer cells (Figure 4A–E). Clinical data shows that HTR2C expression is correlated with tumor stage of breast cancer patients and is higher in metastatic and Her2/neu-overexpressing tumors (Pai et al., 2009). That would support our finding.

Pharmacological inhibition of DRD2 with S(-)eticlopride hydrochloride suppressed cell invasion and migration of multiple human cancer cell lines in vitro. However, overexpression of DRD2 could not induce EMT on MCF7 cells. Therefore, we stopped focusing on DRD2 and S(-)eticlopride hydrochloride.

There are at least two advantages to the screen described herein. One is that the screen can easily be converted to a chemical genetic screening platform. Indeed, our screen succeeded to identify HTR2C as an EMT inducer (Figure 4A–E). In this research, 1280 FDA approval drugs were screened, this is less than a few percent of all of druggable targets (approximately 100 targets) in the human proteome in the body. If chemical genetic screening using specific inhibitor libraries were conducted, more genes that contribute to metastasis and gastrulation could be identified. The second advantage is that the screen enables one researcher to test 100 drugs in 5 hr with using optical microscopy, drugs, and zebrafish embryos. That indicates this screen is not only highly efficient, low-cost, and low-labor but also enables researchers who do not have high-throughput screening instruments to conduct drug screening for anti-metastasis drugs.

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
      <td>Strain, strain background (Zebrafish)</td>
      <td>AB line</td>
      <td>National University of Singapore</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Zebrafish)</td>
      <td>Tg (kdrl:eGFP) zebrafish</td>
      <td>Provided by Dr Stainier</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>BALB/c</td>
      <td>Charles River Laboratories</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>MDA-MB-231</td>
      <td>ATCC</td>
      <td>HTB-26</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>MCF7</td>
      <td>ATCC</td>
      <td>HTB-22</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>MDA-MB-435</td>
      <td>ATCC</td>
      <td>HTB-129</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>MIA-PaCa2</td>
      <td>ATCC</td>
      <td>CRM-CRL-1420</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>PC3</td>
      <td>ATCC</td>
      <td>CRL-3471</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>SW620</td>
      <td>ATCC</td>
      <td>CCL-227</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>PC9</td>
      <td>RIKEN BRC</td>
      <td>RCB0446</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HaCaT</td>
      <td>CLI</td>
      <td>300493</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (BALB/c Mus)</td>
      <td>4T1-12B</td>
      <td>Provided from Dr Gary Sahagian</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>PRMT1 (A33)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_2449</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CYP11A1 (D8F4F)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_14217</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>E-cadherin (4A2)(Mouse monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_14472</td>
      <td>WB (1:1000)IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>EpCAM (VU1D9)(Mouse monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_2929</td>
      <td>WB (1:1000)IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Vimentin (D21H3)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_5741</td>
      <td>WB (1:1000)IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>N-cadherin (D4R1H)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_13116</td>
      <td>WB (1:1000)IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>ZEB1 (D80D3)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_3396</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Histone H3 (D1H2)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_4499</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>β-Tubulin (9F3)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_2128</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>GAPDH (14C10)(Rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#_2118</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HTR2C (ab133570)(Rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>Cat#_ab133570</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>DRD2 (ab85367)(Rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>Cat#_ab85367</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Phospho-GSK3β (Ser9) (F-2)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-373800</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>GSK3β (1F7)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-53931</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>KRT18 (DC-10)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-6259</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>KRT19 (A53-B/A2)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-6278</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>MMP1 (3B6)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-21731</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>MMP2 (8B4)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-13595</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>S100A4 (A-7)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-377059</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Luciferase (C-12)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-74548</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>ki67 (ki-67)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-23900</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>β-Catenin (E-5)(Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-7963</td>
      <td>WB (1:1000)IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>FITC-conjugated E-cadherin antibody (67A4)</td>
      <td>Biolegend</td>
      <td>Cat#_324104</td>
      <td>FACS (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse anti-rabbit immunoglobulin G (IgG) antibodies conjugated to Alexa Fluor 488</td>
      <td>Life Technologies</td>
      <td>A-11029</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-goat anti-rabbit immunoglobulin G (IgG) antibodies conjugated to Alexa Fluor 488</td>
      <td>Life Technologies</td>
      <td>A-11034</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLVX-shRNA1</td>
      <td>Clontech</td>
      <td>Cat#_ 632,177</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCDH-CMV-MCS-EF1α-Hygro</td>
      <td>System Biosciences</td>
      <td>Cat#_CD515B-1</td>
      <td>Gene expression vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMDLg/pRRE</td>
      <td>Addgene</td>
      <td>Addgene Plasmid #12251 RRID:Addgene_12251</td>
      <td>Lentivirus packaging vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pRSV-rev</td>
      <td>Addgene</td>
      <td>Addgene Plasmid #12253 RRID:Addgene_12253</td>
      <td>Lentivirus packaging vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMD2.G</td>
      <td>Addgene</td>
      <td>Addgene Plasmid #12259 RRID:Addgene_12259</td>
      <td>Lentivirus packaging vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Providing pCMV-h5TH2C-VSV</td>
      <td>Provided from Dr Herrick</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FDA-approved chemical libraries</td>
      <td>Prestwick Chemical</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pizotifen</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_sc-201143</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>S(-)Eticlopride hydrochloride</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat#_E101</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism7</td>
      <td>GraphPad Software Inc</td>
      <td>RRID:SCR_002798</td>
      <td>Data analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlowJo</td>
      <td>BD Biosciences</td>
      <td>RRID:SCR_008520</td>
      <td>FACS data analysis</td>
    </tr>
  </tbody>
</table>

### Zebrafish embryo screening

Zebrafish embryos at two-cell stage were collected at 20 min after their fertilization. Each drug was added to a well of a 24-well plate containing approximately 20 zebrafish embryos per well in either 10 or 50 μM final concentration when the embryos reached the sphere stage. Chemical treatment was initiated at 4 hpf and approximately 20 embryos were treated with two different concentrations for each compound tested. The treatment was ended at 9 hpf when vehicle- (DMSO) treated embryos as control reach 80–90% completion of the epiboly stage. The compounds which induced delay (<50% epiboly) in epiboly were selected as hit compounds for in vitro testing using highly metastatic human cancer cell lines. The study protocol was approved by the Institutional Animal Care and Use Committee of the National University of Singapore (protocol number: R16-1068).

### Reagents

FDA, EMA, and other agencies-approved chemical libraries were purchased from Prestwick Chemical (Illkirch, France). Pizotifen (sc-201143) and S(-)eticlopride hydrochloride (E101) were purchased from Santa Cruz (Dallas, TX) and Sigma-Aldrich (St Louis, MO).

### Cell culture and cell viability assay

MCF7, MDA-MB-231, MDA-MB-435, MIA-PaCa2, PC3, SW620, PC9, and HaCaT cells were obtained from American Type Culture Collection (ATCC, Manassas, VA). Luciferase-expressing 4T1 (4T1-12B) cells were provided from Dr Gary Sahagian (Tufts University, Boston, MA). All culture methods followed the supplier’s instruction. Cell viability assay was performed as previously described (Nakayama et al., 2020). PCR-based mycoplasma testing on these cells was performed once in 4 months.

### Plasmid

A DNA fragment coding for HTR2C was amplified by PCR with primers containing restriction enzyme recognition sequences. The HTR2C coding fragment was amplified from hsp70l:mCherry-T2A-CreERT2 plasmid (Huang et al., 2012).

### Immunoblotting

Western blotting was performed as described previously (Nakayama et al., 2020). Raw data of images of western blotting analyses are uploaded as source data for western. Anti-PRMT1 (A33), anti-CYP11A1 (D8F4F), anti-E-cadherin (4A2), anti-EpCAM (VU1D9), anti-vimentin (D21H3), anti-N-cadherin (D4R1H), anti-ZEB1 (D80D3), anti-histone H3 (D1H2), anti-β-tubulin (9F3), and anti-GAPDH (14C10) antibodies were purchased from Cell Signaling Technology (Danvers, MA). Anti-HTR2C (ab133570) and anti-DRD2 (ab85367) antibodies were purchased form Abcam (Cambridge, UK). Anti-phospho-GSK3β (Ser9) (F-2), anti-GSK3β (1F7), anti-KRT18 (DC-10), anti-KRT19 (A53-B/A2), anti-MMP1 (3B6), anti-MMP2 (8B4), anti-S100A4 (A-7), anti-luciferase (C-12), anti-ki67 (ki-67), and anti-β-catenin (E-5) antibodies were purchased from Santa Cruz Biotechnology (Dallas, TX).

### Flow cytometry

Cells were stained with FITC-conjugated E-cadherin antibody (67A4, Biolegend, San Diego, CA). Flow cytometry was performed as described (Nakayama et al., 2009) and analyzed with FlowJo software (TreeStar, Ashland, OR).

### shRNA-mediated gene knockdown

The shRNA-expressing lentivirus vectors were constructed using pLVX-shRNA1 vector (632177, TAKARA Bio, Shiga, Japan). PRMT1-shRNA_#3-targeting sequence is GTGTTCCAGTATCTCTGATTA; PRMT1-shRNA_#4-targeting sequence is TTGACTCCTACGCACACTTTG. CYP11A1-shRNA_#4-targeting sequence is GCGATTCATTGATGCCATCTA; CYP11A1-shRNA_#4-targeting sequence is GAAATCCAACACCTCAGCGAT. Human HTR2C-shRNA-targeting sequence is TCATGCACCTCTGCGCTATAT. Mouse HTR2C-shRNA-targeting sequence is CTTCATACCGCTGACGATTAT. LacZ-shRNA-targeting sequence is CTACACAAATCAGCGATT.

### Immunofluorescence

IF microscopy assay was performed as previously described (Nakayama et al., 2020). Goat anti-mouse and goat anti-rabbit immunoglobulin G (IgG) antibodies conjugated to Alexa Fluor 488 (A-11029 and A-11034, Life Technologies, Carlsbad, CA) and diluted at 1:100 were used. Nuclei were visualized by the addition of 2 μg/ml of 4’,6-diamidino-2-phenylindole (DAPI) (62248, Thermo Fisher, Waltham, MA) and photographed at 100× magnification by a fluorescent microscope BZ-X700 (KEYENCE, Osaka, Japan).

### Boyden chamber cell motility and invasion assay

These assays were performed as previously described (Nakayama et al., 2020). In Boyden chamber assay, either 3 × 105 MDA-MB-231, 1 × 106 MDA-MB-435 or 5 × 105 PC9 cells were applied to each well in the upper chamber.

### Zebrafish xenotransplantation model

Tg(kdrl:eGFP) zebrafish was provided by Dr Stainier (Max Planck Institute for Heart and Lung Research). Embryos that were derived from the line were maintained in E3 medium containing 200 μM 1-phenyl-2-thiourea (P7629, Sigma-Aldrich, St Louis, MO). Approximately 100–400 RFP-labelled MBA-MB-231 or MIA-PaCa2 cells were injected into the duct of Cuvier of the zebrafish at 2 dpf. The fish were randomly assigned to two groups. One group was maintained in the presence of pizotifen-containing E3 medium and the other group was maintained in vehicle-containing E3 medium.

### Spontaneous metastasis mouse model

4T1-12B cells (2 × 104) were injected into the #4 MFP while the mice were anesthetized. To monitor tumor growth and metastases, mice were imaged biweekly by IVIS Imaging System (ParkinElmer, Waltham, MA). The primary tumor was resected 10 days after inoculation. D-Luciferin Potassium Salt (LUCK-100) was purchased from GoldBio (St Louis, MO). The study protocol (protocol number: BRC IACUC #110612) was approved by A*STAR (Agency for Science, Technology and Research, Singapore).

### Gene set enrichment analysis

Gene expression profiles obtained from zebrafish embryos at either 50%-epiboly, shield, or 75%-epiboly stage were analyzed based on the hallmark gene sets derived from the Molecular Signatures Database (MSigDB) (Subramanian et al., 2005; Liberzon et al., 2015). The zebrafish transcriptomic data was sourced from White et al., 2017. Gene sets that were significantly enriched (FDR < 0.25) were presented with the normalized enrichment score (NES) and nominal p value. Source data files for analysis of either gene expression and enriched pathways are uploaded as GSEA Source data 1 and 2, respectively.

### Histological analysis

All OCT-embedded primary tumors, lungs, and livers of mice from the spontaneous metastasis 4T1 model were sectioned on a cryostat. Eight micron sections were taken at 500 µm intervals through the entirety of the livers and lungs. Sections were subsequently stained with hematoxylin and eosin. Metastatic lesions were counted under a microscope in each section for both lungs and livers.

### Statistics

Data were analyzed by Student’s t test; p < 0.05 was considered significant.

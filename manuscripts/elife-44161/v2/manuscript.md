# Renal medullary carcinomas depend upon SMARCB1 loss and are sensitive to proteasome inhibition

## Authors

- Andrew L Hong<sup>1</sup> ([ORCID: 0000-0003-0374-1667](https://orcid.org/0000-0003-0374-1667))
- Yuen-Yi Tseng<sup>3</sup>
- Jeremiah A Wala<sup>3</sup>
- Won-Jun Kim<sup>2</sup>
- Bryan D Kynnap<sup>2</sup>
- Mihir B Doshi<sup>3</sup>
- Guillaume Kugener<sup>3</sup>
- Gabriel J Sandoval<sup>2</sup>
- Thomas P Howard<sup>2</sup>
- Ji Li<sup>2</sup>
- Xiaoping Yang<sup>3</sup>
- Michelle Tillgren<sup>2</sup>
- Mahmhoud Ghandi<sup>3</sup>
- Abeer Sayeed<sup>3</sup>
- Rebecca Deasy<sup>3</sup>
- Abigail Ward<sup>1</sup>
- Brian McSteen<sup>4</sup>
- Katherine M Labella<sup>2</sup>
- Paula Keskula<sup>3</sup>
- Adam Tracy<sup>3</sup>
- Cora Connor<sup>5</sup>
- Catherine M Clinton<sup>1</sup>
- Alanna J Church<sup>1</sup>
- Brian D Crompton<sup>1</sup>
- Katherine A Janeway<sup>1</sup>
- Barbara Van Hare<sup>4</sup>
- David Sandak<sup>4</sup>
- Ole Gjoerup<sup>2</sup>
- Pratiti Bandopadhayay<sup>1</sup>
- Paul A Clemons<sup>3</sup>
- Stuart L Schreiber<sup>3</sup>
- David E Root<sup>3</sup>
- Prafulla C Gokhale<sup>2</sup>
- Susan N Chi<sup>1</sup>
- Elizabeth A Mullen<sup>1</sup>
- Charles WM Roberts<sup>6</sup>
- Cigall Kadoch<sup>2</sup>
- Rameen Beroukhim<sup>2</sup> ([ORCID: 0000-0001-6303-3609](https://orcid.org/0000-0001-6303-3609))
- Keith L Ligon<sup>2</sup>
- Jesse S Boehm<sup>3</sup> ([ORCID: 0000-0002-6795-6336](https://orcid.org/0000-0002-6795-6336))
- William C Hahn<sup>2</sup> ([ORCID: 0000-0003-2840-9791](https://orcid.org/0000-0003-2840-9791)) †

### Affiliations

1. Boston Children’s Hospital Boston United States
2. Dana-Farber Cancer Institute Boston United States
3. Broad Institute of Harvard and MIT Cambridge United States
4. Rare Cancer Research Foundation Durham United States
5. RMC Support North Charleston United States
6. St. Jude Children’s Research Hospital Memphis United States
7. Brigham and Women’s Hospital Boston United States

† Corresponding author

## Abstract

Renal medullary carcinoma (RMC) is a rare and deadly kidney cancer in patients of African descent with sickle cell trait. We have developed faithful patient-derived RMC models and using whole-genome sequencing, we identified loss-of-function intronic fusion events in one SMARCB1 allele with concurrent loss of the other allele. Biochemical and functional characterization of these models revealed that RMC requires the loss of SMARCB1 for survival. Through integration of RNAi and CRISPR-Cas9 loss-of-function genetic screens and a small-molecule screen, we found that the ubiquitin-proteasome system (UPS) was essential in RMC. Inhibition of the UPS caused a G2/M arrest due to constitutive accumulation of cyclin B1. These observations extend across cancers that harbor SMARCB1 loss, which also require expression of the E2 ubiquitin-conjugating enzyme, UBE2C. Our studies identify a synthetic lethal relationship between SMARCB1-deficient cancers and reliance on the UPS which provides the foundation for a mechanism-informed clinical trial with proteasome inhibitors.

## Introduction

Renal medullary carcinoma (RMC) was first identified in 1995 and is described as the seventh nephropathy of sickle cell disease (Davis et al., 1995). RMC is a rare cancer that occurs primarily in patients of African descent that carry sickle cell trait and presents during adolescence with symptoms of abdominal pain, hematuria, weight loss and widely metastatic disease. Due to the aggressive behavior of this disease and the small numbers of patients, no standard of care exists. Patients are generally treated with multimodal therapies including nephrectomy, chemotherapy and radiation therapy. Despite this aggressive regimen, the mean overall survival rate is only 6–8 months (Alvarez et al., 2015; Beckermann et al., 2017; Ezekian et al., 2017; Iacovelli et al., 2015).

Recent studies have implicated loss of SMARCB1 in RMC (Calderaro et al., 2016; Carlo et al., 2017; Cheng et al., 2008). SMARCB1 is a tumor suppressor that when conditionally inactivated in mice leads to rapid onset of lymphomas or brain tumors (Han et al., 2016; Roberts et al., 2002). Furthermore, SMARCB1 is a core member of the SWI/SNF complex where alterations of one or more members have been identified in up to 20% of all cancers (Helming et al., 2014; Kadoch et al., 2013) including malignant rhabdoid tumors (MRTs) and atypical teratoid rhabdoid tumors (ATRTs). MRTs and ATRTs harbor few somatic genetic alterations other than biallelic loss of SMARCB1 and occur in young children (Chun et al., 2016; Gröbner et al., 2018; Lee et al., 2012; Ma et al., 2018; Torchia et al., 2016). In contrast, RMC patients present as adolescents/young adults, are primarily of African descent and have been found to have fusion events in SMARCB1 and gene mutations in ERG, PDGFRB, MTOR, and ERBB2 (Calderaro et al., 2016; Carlo et al., 2017). Other pathways implicated in this disease included loss of TP53 and VEGF/HIF1A (Swartz et al., 2002).

An unresolved question is whether these cancers depend upon loss of SMARCB1. Furthermore, there is an unmet need to identify therapeutic targets to provide better treatments for these patients. Here, we have developed and characterized faithful cell lines of this rare cancer. We demonstrate that RMC depends on loss of SMARCB1 for survival and, through integrated genetic and pharmacologic studies, we uncover the proteasome as a core druggable vulnerability in RMC and other SMARCB1-deficient cancers.

## Results

### Derivation and genomic characterization of RMC models

From September 2013 until September 2018, three patients who had a diagnosis of renal medullary carcinoma (RMC) were consented to IRB approved protocols (Materials and methods). All patients were of African descent and adolescents. We first attempted to create a patient-derived xenograft from each patient by implanting tissue in the sub-renal capsule or subcutaneously in immunodeficient mice but these samples did not form tumors after 6 months of monitoring. We then attempted to develop cell lines from these patients and generated cell lines from two of the three patients (CLF_PEDS0005 and CLF_PEDS9001) (Materials and methods). For the first patient (CLF_PEDS0005), we obtained the primary tissue from our local institution at the time of the initial nephrectomy. We generated a short-term culture normal kidney cell line, CLF_PEDS0005_N, and a tumor cell line, CLF_PEDS0005_T1 (Figure 1—figure supplement 1a). In addition, we obtained fluid from a thoracentesis performed when the patient relapsed 8 months into therapy. We isolated two cell lines that grew either as an adherent monolayer, CLF_PEDS0005_T2A, or in suspension, CLF_PEDS0005_T2B. Each of these tumor cell lines expressed the epithelial marker, CAM5.2, and lacked expression of SMARCB1 similar to that observed in the primary tumor (Figure 1—figure supplement 1b). For the second patient (CLF_PEDS9001), we partnered with the Rare Cancer Research Foundation and obtained samples through a direct-to-patient portal (www.pattern.org). The primary tumor tissue from the second patient was obtained at the time of the initial nephrectomy. From this sample, we generated the tumor cell line, CLF_PEDS9001_T1. Cell lines were generated from patients who received 4–8 weeks of neoadjuvant chemotherapy prior to their nephrectomy.

Sequencing and cytogenetic efforts have identified deletion of one allele of SMARCB1 along with fusion events in the second allele of SMARCB1 in RMC patients (Calderaro et al., 2016; Carlo et al., 2017). We performed WES (CLF_PEDS0005) or whole genome sequencing (WGS; CLF_PEDS9001) on the primary kidney tumor tissues. In both patients, we confirmed the presence of sickle cell trait but also found tumor purity was <20%, which, like prior studies, prevented the identification of the fusion events (Figure 1—figure supplement 1c). This low tumor purity is attributable to the stromal desmoplasia seen in RMC (Swartz et al., 2002).

We then performed WES on the normal cell line (CLF_PEDS0005_N) or whole blood (CLF_PEDS9001) and compared it to the primary tumor cell lines (CLF_PEDS0005_T1 and CLF_PEDS9001_T) and metastatic cell lines (CLF_PEDS0005_T2A and CLF_PEDS0005_T2B). We found a low mutation frequency (1–3 mutations/mb; Materials and methods; Figure 1a) in the tumor cell lines similar to that of other pediatric cancers and cell lines such as MRT, ATRT and Ewing sarcoma (Cibulskis et al., 2013; Johann et al., 2016; Wala et al., 2018). We found that only the metastatic cell lines harbored mutations in TP53 and TPR (Materials and methods; Supplementary file 1) (Cibulskis et al., 2013). Using copy number analysis, we confirmed the heterozygous loss of SMARCB1. In agreement with prior studies, we failed to find an identifiable mutation or deletion to account for the loss of the second SMARCB1 allele with WES.

![Figure 1.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig1-v2.jpg)

**Figure 1.:** (a) Copy number analysis of RMC models from WES identifies heterozygous loss of alleles particularly at 22q where SMARCB1 resides or low-level gains in primary and metastatic tumors. Red indicates degree of genomic amplification while blue indicates degree of genomic loss. Rates of mutations per megabase are consistent with patients with RMC or other pediatric cancers such as rhabdoid tumor. (b) Circos plots from WGS to represent structural alterations seen in RMC cell lines. Red indicates a deletion. All deletions are located in the introns. Blue arcs indicate fusions identified with SvABA v0.2.1 (Wala et al., 2018). Blue star indicates a SMARCB1 rearrangement. (c) Read counts from WGS identify single copy deletion of SMARCB1 in CLF_PEDS0005_T1 indicated by a Tumor/Normal ratio of approximately 0.5 where SMARCB1 is located. (d) Second allele of SMARCB1 is lost by a balanced translocation occurring in intron 1 of SMARCB1 and fuses to the C-terminal end of C1orf116 in chromosome one in CLF_PEDS0005_T1. (e) Read counts from WGS identify single copy deletion of SMARCB1 in CLF_PEDS9001_T1. (f) Second allele of SMARCB1 is lost by a balanced translocation occurring in intron 6 of SMARCB1 and fuses to the anti-sense intron 10 of PLEKHA5 in chromosome 12 in CLF_PEDS9001_T1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) Gross pathology of CLF_PEDS0005 nephrectomy. Circle highlights treated tumor. (b) Immunohistochemistry of CLF_PEDS0005 cells highlighting same staining patterns as seen in RMC. For CAM5.2, the positive control is the brown staining of skin cells and for SMARCB1, the positive control is the brown nuclear staining of tonsil cells. (c) Integrated Genomic Viewer (IGV) screen shot of the hemoglobin beta (HbB) loci. At amino acid 7, there is a T/A heterozygous mutation (Glutamic acid/Valine) leading to sickle cell trait. (d) Mapping of how exons of SMARCB1 correlate to known domains of SMARCB1 (Allen et al., 2015; Das et al., 2013). (e) Quantitative reverse transcriptase PCR (qRT-PCR) of each exon-exon junction of SMARCB1 confirms expression loss in RMC samples. Relative expression of these exon-exon junctions in the RMC models was compared to TC32, a Ewing Sarcoma cell line with wild-type SMARCB1. (f) Immunoblot of SMARCB1 across BT16 (ATRT cell line), G401 (MRT cell line), CLF_PEDS0005 and CLF_PEDS9001 (RMC cell lines), and HA1E and CLF_PEDS1012_T1 (SMARCB1 WT cell lines). SMARCB1 is lost in ATRT, MRT and RMC cell lines. For CLF_PEDS9001_T1, there is a faint band (*) above the nonspecific band (**) that likely represents a truncated SMARCB1. (g) Sequence alignment across breakpoints of SMARCB1 and fusion partners from this and published studies (Calderaro et al., 2016). There are no clear consensus sequences identified.

We used dual-color break apart FISH and found that a fusion event led to loss of the second SMARCB1 allele as seen in prior studies (Materials and methods; Supplementary file 2) (Calderaro et al., 2016; Carlo et al., 2017). We then performed WGS to assess for structural variations that would not be captured by WES to elucidate the breakpoint of the rearrangement in SMARCB1 (Figure 1b; Materials and methods). For CLF_PEDS0005_T1, we found a large deletion between BCR and MYH9 which is predicted to lead to loss of one allele of SMARCB1 (Figure 1c) along with a balanced translocation between intron 1 of SMARCB1 to the intron region following the C-terminal end of C1orf116, yielding a non-functional allele (Figure 1d and Supplementary file 3). For CLF_PEDS9001_T1, we found a large deletion between TTC28 and VPREB that would lead to loss of one allele of SMARCB1 (Figure 1e) along with a balanced translocation that leads to fusion of intron 10 of PLEKHA5 to intron 6 of SMARCB1 (Figure 1f and Supplementary file 4). Both translocations involved inactivation of the C-terminal end of SMARCB1 (Figure 1—figure supplement 1d). We confirmed these findings by Sanger sequencing of the breakpoint, by qRT-PCR and by immunoblotting to demonstrate loss of SMARCB1 expression (Supplementary file 5, Figure 1—figure supplement 1e–f; Materials and methods). We then assessed previously identified breakpoint SMARCB1 sequences with the breakpoints identified in this study and failed to find alignments, fragile sites or other repetitive DNA elements that were shared amongst these sequences (Figure 1—figure supplement 1g). Taken together, we have developed in vitro cell line models from two patients with RMC which faithfully recapitulate known genomics of this disease.

### Patient-derived models of RMC are similar to SMARCB1 deficient cancers

We performed RNA-sequencing and transcriptomic profiling to compare the RMC models to other renal tumors or tumors that harbor loss of SMARCB1. Specifically, we compared the Therapeutically Applicable Research to Generate Effective Treatments (TARGET) RNA-sequencing data from pediatric renal tumors (e.g. Wilms Tumor, Clear Cell Sarcoma of the Kidney, and Malignant Rhabdoid Tumor) or normal kidney tissues with the RMC models using t-distributed stochastic neighbor embedding (tSNE) (Materials and methods). The normal cell line, CLF_PEDS0005_N, clustered with TARGET normal kidney tissues and RMC cell lines from both patients clustered with the TARGET Rhabdoid Tumor samples (Figure 2a). These observations showed that these RMC cell lines share expression patterns with patients with MRTs.

![Figure 2.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig2-v2.jpg)

**Figure 2.:** (a) Using tSNE, gene expression by RNA-sequencing from patients with pediatric renal tumors profiled in TARGET such as clear cell sarcoma of the kidney (CCSK), malignant rhabdoid tumor (MRT) or Wilms tumor (WT) was compared with patient-derived models of RMC. RMC cell lines (red) cluster with rhabdoid tumor samples (purple). The normal cell line (orange) (CLF_PEDS0005_N) clusters with other normal kidneys profiled in TARGET. (b) tSNE analysis of gene-expression array data shows RMC cell lines (red) clustering with RMC patients (blue) and these cluster with other MRT (purple) or ATRT (yellow) samples. However, these do not cluster as closely with synovial sarcomas (black). (c) Glycerol gradients (10–30%) followed by SDS-PAGE analysis of rhabdoid tumor cell line G401, as compared to SMARCB1 wild-type cell line HA1E, show ARID1A is seen in higher fractions when SMARCB1 is expressed (left). Gradients were then performed on patient-derived models of RMC with doxycycline-inducible SMARCB1. A similar rightward shift of ARID1A occurs upon re-expression of SMARCB1. These same shifts occur with SMARCA4 (right). These experiments are representative of at least two biological replicates. (d) Fraction 14 of the glycerol gradients shows a modest increase in SWI/SNF complex members, SMARCC1, SMARCC2, SMARCA4 and ARID1A in HA1E, a SMARCB1 wild type cell line. When SMARCB1 is re-expressed in G401 and RMC lines, a similar pattern is seen. Images are representative of 2 biological replicates. (e) Using cell lines with stably transfected and inducible SMARCB1, cell viability was assessed with or without expression of SMARCB1 over 8 days. There is no significant difference in SMARCB1 wild type cell line, HA1E. Re-expression of SMARCB1 leads to significant decreases in cell viability as compared to LacZ control in SMARCB1 deficient cancer cell lines G401, CLF_PEDS9001_T, and CLF_PEDS0005. Error bars are standard deviations based on number of samples in parentheses. (f) CLF_PEDS0005_T2A cell line shows signs of senescence following re-expression of SMARCB1. Images representative of 3 biological replicates.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) CellTiter-Glo of parental cell lines treated with increasing doses of doxycycline for 96 hr. Error bars shown are standard deviations from two biological replicates. Dotted line at doxycycline of 1 ug/mL (or log 0) indicates dosage used in this study. (b) SMARCB1 inducible vectors were stably transfected into cell lines. Administration of doxycycline caused similar induction of SMARCB1 across all cell lines. Blots are representative of at least two biological replicates. (c) SMARCB1 immunoblot from 10–30% glycerol gradients. SMARCB1 is prominently in fractions 13 and 14. Blots are representative of at least two biological replicates. (d) Representative images from three biological replicates of β-galactosidase staining following 7 days of SMARCB1 or LacZ re-expression across CLF_PEDS0005 cell lines. (e) When SMARCB1 is re-expressed, SMARCB1 expression is maintained at the transcriptional level by qRT-PCR over 5 days. (f) Kinetics of differentially expressed genes when SMARCB1 is re-expressed over 120 hr. Left panel shows a more rapid decline followed by overall stabilization while the right panel shows a gradual decline of transcripts over time.

To determine if the RMC cell lines clustered separately among other SMARCB1-deficient cancers, we performed gene expression analysis of our RMC models and compared them to publicly available datasets of MRT cell lines, patients with RMC, MRT or ATRT or synovial sarcoma (a cancer driven by the fusion oncoprotein SSX-S18 which displaces SMARCB1; Materials and methods) (Barretina et al., 2012; Calderaro et al., 2016; Han et al., 2016; Johann et al., 2016; Richer et al., 2017). Using tSNE, we found that the RMC cell lines closely mapped to a French cohort of RMC, MRT and ATRT patients (Figure 2b). These observations demonstrated that RMC cell lines and SMARCB1 deficient patients express similar gene expression programs.

We then assessed the consequences of re-expressing SMARCB1. Specifically, we generated doxycycline-inducible open reading frame (ORF) vectors harboring SMARCB1 and stably infected our RMC models, G401 (MRT cell line) and HA1E (SMARCB1 wild-type immortalized epithelial kidney cell line) (Hahn et al., 1999). We confirmed that the addition of doxycycline used in our studies did not affect the proliferation of the parental cell lines (Materials and methods and Figure 2—figure supplement 1a–b).

We used these inducible cell lines to assess the biochemical stability of the SWI/SNF complex by using 10–30% glycerol gradient sedimentation followed by SDS-PAGE (Figure 2c–d and Figure 2—figure supplement 1c). In HA1E SMARCB1 wild-type cells, the SWI/SNF complex members SMARCB1, ARID1A and SMARCA4 were robustly expressed at higher molecular weights (e.g. fractions 13–16). In G401 SMARCB1 deficient cells, the SWI/SNF complex is smaller and seen at lower molecular weights (e.g. fractions 10–14). Furthermore, expression of SWI/SNF complex members was modestly decreased in G401, consistent with our prior studies (Nakayama et al., 2017; Wang et al., 2017). In our RMC cell lines, we found that the majority of ARID1A and SMARCA4 was observed in fractions 11–13 similar to what we found in the MRT cell line G401. In addition, we found increased expression and a shift of ARID1A and SMARCA4 to larger fractions 13–15 upon re-expression of SMARCB1 in the RMC lines similar to what we observed in the SMARCB1 wild-type HA1E cell line. We concluded that the composition of the SWI/SNF complex is similar between RMC and other SMARCB1 deficient cancers.

We then used the inducible cell lines to measure the consequence of SMARCB1 re-expression on the viability of the cells. We also generated cell lines with inducible expression of a LacZ control to compare with re-expression of SMARCB1. In the HA1E SMARCB1 wild type cells, we found no significant difference in viability between induction of SMARCB1 versus induction of LacZ using direct counting of viable cells (Figure 2e). In contrast, induction of SMARCB1 in the MRT G401 SMARCB1 deficient cells decreased the number of viable cells by 41%. Similar to G401, we found that re-expression of SMARCB1 in each of the RMC models led to significant decreases in cell viability (37–62%) (Figure 2e; Figure 2—source data 1). These observations suggest loss of SMARCB1 is required for the proliferation and viability of RMC cells.

Since MRT cell lines arrest and senesce when SMARCB1 is re-expressed (Betz et al., 2002), we looked for evidence of senescence by staining for senescence-associated acidic β-galactosidase in the RMC cells when SMARCB1 was re-expressed. Following 7 days of SMARCB1 or LacZ re-expression, we stained the cells for β-galactosidase (Materials and methods). We failed to observe cells expressing β-galactosidase upon expression of LacZ in the RMC cells, but when SMARCB1 was expressed, we found 44.6% (±17%) of the RMC cells stained for β-galactosidase (Figure 2f and Figure 2—figure supplement 1d). These studies showed that re-expression of SMARCB1 in RMC cells may also lead to senescence.

We then assessed what genes were differentially expressed upon SMARCB1 re-expression in the RMC and MRT cell lines as another way to assess the similarity between these two cancers. We performed RNA-sequencing on the doxycycline-induced SMARCB1 RMC cell lines and compared them to the uninduced cell lines or doxycycline-induced LacZ cell lines. We then re-analyzed our previously published studies of MRT cells with SMARCB1 re-expression and compared them to our RMC cells (Wang et al., 2017). We found 1719 genes to be significantly different (false discovery rate of <0.25) in the RMC cells and 2735 genes in MRT cells. We identified 527 genes that significantly overlapped between the RMC and MRT cell lines (hypergeometric p-value less than 4.035e-63; Supplementary file 6). We compared this group of genes to the genes differentially expressed between MRT tumor and normal tissues from TARGET (n = 6,311). We identified 257 genes that overlapped with the 527 significantly differentially expressed genes induced by re-expression of SMARCB1 (Supplementary file 6).

Using this list of 257 genes, we performed gene ontology (GO)-based Gene Set Enrichment Analysis (GSEA) (Subramanian et al., 2005) and identified significantly enriched genes sets (q-value <0.1), including those related to the cell cycle and the ubiquitin-proteasome system (UPS). We then analyzed the kinetics by which these gene expression changes occur after SMARCB1 was re-expressed. Specifically, we analyzed 5 genes of these 257 genes that are implicated in regulation of the G1/S (RRM2, TOP2A) or G2/M (PLK1, CCNB1, UBE2C) phases of the cell cycle. For PLK1 and CCNB1, we observed a gradual decrease in expression over the course of 120 hr whereas RRM2, UBE2C and TOP2A exhibited a more profound decrease in expression after the first 24 hr and then a modest decrease over the following 96 hr (Figure 2—figure supplement 1e–f).

These findings confirm that changes in the transcriptome following SMARCB1 re-expression in RMC cell lines are similar to other SMARCB1 deficient cancer cell lines. In sum, these observations indicate that the RMC cell lines are functionally similar to those derived from other SMARCB1 deficient cancers.

### RNAi and CRISPR-Cas9 loss-of-function screens and small-molecule screens in RMC models identify proteasome inhibition as a vulnerability

MRT, ATRT and RMC are aggressive and incurable cancers. We performed genetic (RNAi and CRISPR-Cas9) and pharmacologic screens to identify druggable targets that would decrease proliferation or survival for these cancers. Specifically, we used the Druggable Cancer Targets (DCT v1.0) libraries and focused on targets that were identified by suppression with RNAi, gene deletion with CRISPR-Cas9-based genome editing, and perturbation by small molecules (Hong et al., 2016; Seashore-Ludlow et al., 2015). We accounted for off-target effects in the RNAi screens by using seed controls for each shRNA.

We performed these three orthogonal screens on both metastatic models of RMC, CLF_PEDS0005_T2A and CLF_PEDS0005_T2B (Figure 3a). We introduced the shRNA DCT v1.0 lentiviral library into these two cell lines and evaluated the abundance of the shRNAs after 26 days using massively parallel sequencing (Materials and methods). We confirmed depletion of known common essential genes such as RPS6 (Figure 3—figure supplement 1a). We then analyzed the differential abundance between the experimental and seed control shRNAs to collapse individual shRNAs to consensus gene dependencies with RNAi Gene Enrichment Ranking (RIGER) (Luo et al., 2008). Of 444 evaluable genes, 72 genes scored with a RIGER p-value<0.05 in CLF_PEDS0005_T2A and 74 genes scored in CLF_PEDS0005_T2B.

![Figure 3.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig3-v2.jpg)

**Figure 3.:** (a) Left: RNAi suppression of 444 evaluable genes (red) identifies 72 genes that when suppressed caused a significant viability loss in CLF_PEDS0005_T2A. Genomic indels created by CRISPR-Cas9 in 445 evaluable genes (blue) identify 124 genes that cause a viability loss. RNAi and CRISPR-Cas9 screens were performed in biological replicates. Small-molecule screen (performed in technical replicates) with 417 evaluable compounds (green) identifies 75 compounds that lead to significant viability loss. 21 genes overlap across these three screens. Right: The same screens were performed with CLF_PEDS0005_T2B and 27 genes were found to be significantly depleted when suppressed by RNAi, genomically deleted by CRISPR-Cas9 or inhibited when treated with a small molecule. Center: List of 19 genes that overlapped between functional screens from CLF_PEDS0005_T2A and CLF_PEDS0005_T2B can be categorized into genes involving the ubiquitin-proteasome system, cell cycle and nuclear export (Supplementary file 7). (b) Comparison of Z-score normalized small-molecule screens between CLF_PEDS0005_T2 and CLF_PEDS0005_N (normal isogenic cell line). Small molecules targeting the genes identified in Figure 3a are either in red (proteasome inhibitors) or blue (other hits). Each dot is representative of the average of two technical replicates. (c) Relative log2 fold change in abundance from CRISPR-Cas9 screens between sgRNA controls (grey) and genes in the DCT v1.0 screen involving the proteasome (red). Data is taken at 23 days following selection and compared to an early time point. As compared to the undifferentiated sarcoma cell line CLF_PEDS015_T1, inhibition of the proteasome subunits leads to a more profound viability loss as compared with controls. Each dot is representative of a minimum of 2 biological replicates. (d) Short term cultures of the normal cell line (CLF_PEDS0005_N) or early passage of the heterogenous cell line (CLF_PEDS9001_early) were compared for assessment of viability to the primary tumor cell lines following treatment with bortezomib. Two-tailed t-test p-value=0.008 for PEDS0005_T1 and two-tailed t-test p-value=4.76e-5 for PEDS9001_T1. Error bars represent standard deviations from two biological replicates. (e) Short term cultures of the normal cell line (CLF_PEDS0005_N) or early passage of the heterogenous cell line (CLF_PEDS9001_early) were compared for assessment of viability to the primary tumor cell lines following treatment with MLN2238. Error bars represent standard deviations from two biological replicates. (f) Re-expression of SMARCB1 in G401 leads to a rightward shift in the dose-response curve with bortezomib compared with uninduced cells. Error bars represent standard deviations from two biological replicates. (g) Re-expression of SMARCB1 in CLF_PEDS9001_T leads to a rightward shift in the dose-response curve with MLN2238 compared with uninduced cells. Error bars represent standard deviations from three biological replicates.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a) Suppression of RPS6 in CLF_PEDS0005_T2A in RNAi screens. Following log2 normalized counts, shRNAs (black) and paired seed controls (grey) were assessed for off-target effects. Most pairs showed minimal off-target effects while Pair four showed significant off-target effects. Error bars represent standard deviation from at least two replicates. *** indicates a two-tailed t-test p-value<0.0005, **<0.005. (b) and (c) Correlation of replicates from normalized counts of CRISPR-Cas9 screens in CLF_PEDS0005_T2A or CLF_PEDS0005_T2B at the early day six timepoint. (d) and (e) Correlation of replicates from normalized counts of CRISPR-Cas9 screens in CLF_PEDS0005_T2A or CLF_PEDS0005_T2B at the end of the screen (e.g. day 23) timepoint. (f) and (g) Log2 fold change in abundance of sgRNAs in CRISPR-Cas9 loss of function screens. Controls include sgControls (black) and common essential gene, RPS6. In comparison to these, genes involving the proteasome were similarly depleted like RPS6. (h) Gene deletion by CRISPR-Cas9 of PSMB5 leads to significant decrease in viable cells in RMC cell lines. Error bars represent standard deviation from at least two replicates. (i) Gene deletion by CRISPR-Cas9 of PSMB5 is confirmed by immunoblot. (j) Confirmation that the normal cell line, CLF_PEDS0005_N, early passaged tumor cell line, CLF_PEDS9001_T1 and Wilms tumor cell line, CLF_PEDS1012_T1, express SMARCB1 as compared to the primary RMC cancer cell lines.

In parallel, we introduced the CRISPR-Cas9 DCT v1.0 lentiviral library to determine the differential representation of the CRISPR-Cas9 sgRNAs between 6 and 23 days to identify genes depleted or enriched in this screen by massively parallel sequencing (Materials and methods). We confirmed that the distribution of sgRNAs among biological replicates was highly correlated (Figure 3—figure supplement 1b–e). When compared to the controls, there was significant depletion of essential genes such as RPS6 (Figure 3—figure supplement 1f–g). We used RIGER to collapse the individual sgRNAs to consensus gene dependencies and found 124 genes (of a total of 445 evaluable genes) and 136 genes (of a total of 445 evaluable genes) with a RIGER p-value<0.05 in CLF_PEDS0005_T2A and CLF_PEDS0005_T2B cell lines, respectively.

We performed a small-molecule screen using a library of 440 compounds that have known targets in the RMC cells (CLF_PEDS0005_T2A and CLF_PEDS0005_T2B) (Hong et al., 2016). This library includes 72 FDA approved compounds, 100 compounds in clinical trials and 268 probes based on our prior studies. We calculated an area under the curve (AUC) based on an 8-point concentration range and considered AUCs < 0.5 as significant. Of the evaluable compounds, 75 (18%) compounds significantly decreased cell viability in CLF_PEDS0005_T2A and 82 (20%) compounds significantly decreased cell viability in CLF_PEDS0005_T2B.

We then looked for genes or targets of the small molecules that scored in all three of the RNAi, CRISPR-Cas9 and small-molecule screens. We identified 21 genes in CLF_PEDS0005_T2A and 27 genes in CLF_PEDS0005_T2B (Supplementary file 7) of which 19 genes scored in both screens (Figure 3a). Among the 19 genes were components of the ubiquitin-proteasome system (e.g. PSMB1, PSMB2, PSMB5, PSMD1, PSMD2, and CUL1), regulators of the cell cycle (CDK1, CDK6, KIF11 and PLK1) and genes involved in nuclear export (KPNB1 and XPO1).

To eliminate small molecules and targets that affect normal renal tissue, we screened the normal cell line (CLF_PEDS0005_N) with the small-molecule library. We calculated the robust Z-scores for these screens in relationship to the Cancer Cell Line Encyclopedia (CCLE) to normalize the responses to various compounds (Barretina et al., 2012; Rees et al., 2016; Seashore-Ludlow et al., 2015). We then compared the results of this small-molecule screen with the RMC cancer cell lines (CLF_PEDS0005_T2A and CLF_PEDS0005_T2B). We found that the tumor cells were differentially sensitive (up to two standard deviations) upon treatment with proteasome inhibitors, bortezomib and MLN2238, when compared to the normal cell line (Figure 3b; Figure 3—source data 1). These findings suggest that the vulnerability to proteasome inhibition may be dependent on loss of SMARCB1.

### Validation of proteasome inhibition as a specific therapy in SMARCB1 deficient cancers

To validate the dependency of SMARCB1 deficient tumors to the ubiquitin-proteasome system, we assessed the consequences of inhibiting proteasome function on survival of the primary tumor cell line, CLF_PEDS0005_T1, by deleting components of the proteasome with CRISPR-Cas9. We compared these findings with a model of undifferentiated sarcoma, CLF_PEDS015T, that does not harbor mutations in SMARCB1 (Hong et al., 2016). We scaled the results based on the non-targeting sgRNA negative controls and positive controls targeting RPS6, a common essential gene (Hart et al., 2015). Compared to the control sgRNAs, there was an average decrease of 29% in viability in CLF_PEDS015T while there was an average decrease of 74% in CLF_PEDS0005_T1 (Figure 3c; Materials and methods). Although deletion of the proteasome members affected proliferation in all of the models (two tailed t-test p=1.1e-5 for CLF_PEDS015T and p=5.4e-20 for CLF_PEDS0005_T1), we found that suppression of proteasome components affected the RMC model CLF_PEDS0005_T1 to a statistically greater degree (two tailed t-test p=7.1e-8). We subsequently validated that gene deletion by CRISPR-Cas9 of PSMB5, one of the primary targets of proteasome inhibitors, in the CLF_PEDS0005_T2A and CLF_PEDS9001_T1 cell lines led to decreased viability (Figure 3—figure supplement 1h–i).

We then determined whether this vulnerability to proteasome inhibition was specific to the loss of SMARCB1. We treated the normal cell line, CLF_PEDS0005_N, and an early passage of CLF_PEDS9001_T1 while it was a heterogenous population and retained SMARCB1 (Figure 3—figure supplement 1j) with bortezomib or the second-generation proteasome inhibitor, MLN2238. We observed significantly decreased sensitivity to the proteasome inhibitors in the SMARCB1 retained isogenic cell lines as compared to the SMARCB1 deficient cell lines (Figure 3d–e). We then treated our SMARCB1-inducible RMC and MRT cell lines with DMSO, bortezomib or MLN2238. Re-expression of SMARCB1 led to a decrease in sensitivity to bortezomib or MLN2238 as compared to the isogenic SMARCB1 deficient lines (Figure 3f–g). The observed differential resistance to SMARCB1 re-expression was between 2–3-fold with either bortezomib or MLN2238 (Figure 4—figure supplement 1a–b). We concluded that re-expression of SMARCB1 partially rescued the sensitivity of MRT or RMC cell lines to proteasome inhibition.

We then compared the results of small-molecule screens performed in SMARCB1-deficient cancer cell lines in CCLE to the rest of the CCLE cell lines (n = 835). We found that SMARCB1-deficient cell lines were significantly more sensitive (two-tailed t-test p-value=0.011) to treatment with MLN2238 than non-multiple myeloma CCLE cell lines (Figure 4a; Figure 4—source data 1) (Rees et al., 2016; Seashore-Ludlow et al., 2015). The degree of sensitivity was similar to that of multiple myeloma cell lines which are known to be sensitive to proteasome inhibition (Dimopoulos et al., 2016). These findings confirm that SMARCB1 deficient cell lines are selectively vulnerable to proteasome inhibition.

![Figure 4.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig4-v2.jpg)

**Figure 4.:** (a) Multiple myeloma cell lines and SMARCB1-deficient lines are similarly sensitive to proteasome inhibitor, MLN2238. Both are significantly different from other CCLE cell lines based on Z-score normalized sensitivity. * two-tailed t-test p-value<0.05. n.d. no difference. (b) Early passage Wilms tumor (SMARCB1 wild-type) cell line CLF_PEDS1012_T1 is not as sensitive to treatment with bortezomib compared with RMC and MRT cell lines. Error bars represent standard deviations following at least two biological replicates. (c) Early passage Wilms tumor (SMARCB1 wild-type) cell line CLF_PEDS1012_T1 is not as sensitive to treatment with MLN2238 compared with RMC and MRT cell lines. Error bars represent standard deviations following at least two biological replicates. (d) Analysis of differentially expressed genes when SMARCB1 was re-expressed in SMARCB1 deficient cancers compared with differentially expressed genes when SMARCB1 deficient cancers were treated with 200 nM MLN2238. Gene sets enriched based on GO-based GSEA involved the cell cycle (blue) and regulation of the ubiquitin-proteasome system (black). (e) Treatment with proteasome inhibitor, MLN2238 at 200 nM for 24 hr leads to G2/M arrest in CLF_PEDS9001_T1. Values shown represent the percent of cells in G1 or G2/M. Error values shown are standard deviations from two biological replicates. (f) Treatment with MLN2238 at 200 nM for 24 hr leads to G2/M arrest in CLF_PEDS0005_T2B which can be prevented by re-expression of SMARCB1. Error values shown are standard deviations from two biological replicates. (g) Treatment of CLF_PEDS9001_T1 with MLN2238 at 200 nM for 48 hr leads to increased frequency of cells with Annexin V/PI staining and PI only staining. Error values shown are standard deviations from two biological replicates. (h) G401 cells stably infected with inducible SMARCB1 treated with either bortezomib at 15 nM or MLN2238 at 200 nM induce cleaved caspase-3 compared with DMSO controls after 24 hr. When SMARCB1 is re-expressed, cleaved caspase-3 levels are decreased compared to uninduced cell lines. Blots are representative of a minimum of 2 biological replicates.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) Using the inducible SMARCB1 cell lines, SMARCB1 deficient lines have increased sensitivity to bortezomib (btz) at 15 nM when compared to cells with SMARCB1 re-expressed. Error bars represent standard deviation from at least three biological replicates. ** indicates a two-tailed t-test p-value<0.005. (b) Using the inducible SMARCB1 cell lines, SMARCB1 deficient lines have increased sensitivity to MLN2238 at 100 nM when compared to cells with SMARCB1 re-expressed. Error bars represent standard deviation from at least three biological replicates. * indicates a two-tailed t-test p-value<0.05 and **<0.005. (c) Sensitivity to bortezomib as measured by IC50s. RMC cell lines (red), MRT cell lines (blue) and ATRT cell lines (yellow) are similarly sensitive to RPMI8226, multiple myeloma cell line. This is in comparison to H2172 which is significantly less sensitive to proteasome inhibition. Error bars represent standard deviation from at least three biological replicates. n.d. no difference. ** indicates a two-tailed t-test p-value<0.005. (d) c-MYC is not downregulated upon proteasome inhibition at the protein level. Cell lines were treated with DMSO, bortezomib at 15 nM or MLN2238 at 200 nM for 48 hr. c-MYC protein levels in RPMI8226, a multiple myeloma cell line, decrease following proteasome inhibition by immunoblot. However, this does not occur in the SMARCB1 deficient cancer cell lines. Immunoblots are representative of at least two biological replicates. (e) c-MYC is not downregulated upon proteasome inhibition in the transcriptome. Cell lines were treated with DMSO or MLN2238 at 200 nM for 48 hr. Samples from three biological replicates were subjected to RNA-sequencing and c-MYC levels were assessed. Across all the SMARCB1 deficient cell lines, c-MYC transcript levels were increased. Error bars represent standard deviation from at least three biological replicates.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (a) and (b) Immunoblots from total, cytoplasmic and nuclear protein fractions show no significant difference in SWI/SNF complex members upon treatment of proteasome inhibitors (MLN2238 at 200 nM). Lamin A/C and alpha tubulin are loading controls. Blots representative of at least two biological repeats. (c) Treatment with proteasome inhibitor, MLN2238 at 200 nM, leads to induction of IRE1α and GRP78. However, induction of these ER stress proteins is not rescued upon re-expression of SMARCB1. (d) Treatment with cell cycle inhibitors nocodazole (microtubule assembly inhibitor; red) at 100 nM for G401 and 300 nM for CLF_PEDS9001_T1 or RO-3306 (CDK1 inhibitor; orange) at 10 μM for both cell lines leads to accumulation of cells in G2/M after 24 hr similar to that of MLN2238 (blue). (e) Nocodazole and RO-3306 treatment for 24 hr leads to activation of cleaved caspase-3 and accumulation of cyclin B1. (e) Treatment with cell cycle inhibitors nocodazole or RO-3306 at 72 hr leads to a maximum decrease in cell viability of 65–90% depending on the cell line and compound.

We then performed in vitro studies to confirm the findings from these high throughput small molecule screens. We treated an additional 6 SMARCB1 deficient cell lines (4 MRT and 2 ATRT) with bortezomib. We compared these results to H2172, a lung cancer cell line that was not sensitive to proteasome inhibition in CCLE small-molecule screens, and RPMI8226, an established multiple myeloma cell line that is responsive to proteasome inhibition (Hideshima et al., 2001). We found that our SMARCB1 deficient cell lines exhibited single digit nanomolar sensitivity to proteasome inhibition similar to that observed in the multiple myeloma cell line RPMI8226 (Figure 4—figure supplement 1c). In contrast, we found that the IC50 in H2172 was at least 3-fold higher. Since there are no SMARCB1 wildtype pediatric kidney cancer cell lines in CCLE, we compared the sensitivity to bortezomib or MLN2238 in our RMC models with wildtype SMARCB1 patient-derived Wilms tumor cell line, CLF_PEDS1012_T (Figure 4b–c and Figure 3—figure supplement 1j). We found that CLF_PEDS1012_T was more resistant to proteasome inhibition as compared to our RMC models and MRT cell line, G401. These findings suggest that SMARCB1-deficient cells are more sensitive to proteasome inhibition.

### Proteasome inhibition leads to cell cycle arrest in G2/M and subsequent cell death

We then studied how SMARCB1 loss leads to a dependency on the ubiquitin-proteasome system. Since activation of c-MYC has been observed in SMARCB1-deficient cancers (Cheng et al., 1999; Genovese et al., 2017), we assessed how c-MYC levels are altered upon proteasome inhibition. Compared to RPMI8226, a multiple myeloma cell line that relies on c-MYC for survival (Tagde et al., 2016), we failed to observe suppression of c-MYC protein levels following bortezomib or MLN2238 treatment (Figure 4—figure supplement 1d). We then assessed c-MYC expression levels in the G401, CLF_PEDS9001T, and CLF_PEDS00005_T1 cell lines following treatment with MLN2238 and found that c-MYC levels were increased after MLN2238 treatment (Figure 4—figure supplement 1e). In our models of RMC and MRT, these findings suggest proteasome inhibition does not lead to suppression of c-MYC.

We then assessed if the SWI/SNF complex is altered upon treatment with a proteasome inhibitor. We treated uninduced and induced SMARCB1 cells with DMSO or a proteasome inhibitor. We failed to see a consistent significant change in total or nuclear protein when immunoblotting for SWI/SNF complex members (SMARCE1, SMARCD1, SMARCD1, SMARCC1, SMARCC2, SMARCA4 and ARID1A) other than increases in SMARCB1 levels upon doxycycline treatment (Figure 4—figure supplement 2a–b). These findings suggest that inhibition of the proteasome in SMARCB1 deficient cancers and its subsequent resistance upon SMARCB1 expression does not alter the total or nuclear levels of SWI/SNF complex members.

ER stress has been implicated as a mechanism by which proteasome inhibitors act on multiple myeloma cells (Obeng et al., 2006). We saw an increase in protein expression of markers of ER stress, GRP78 and IRE1α, following treatment with MLN2238 (Figure 4—figure supplement 2c). Upon re-expression of SMARCB1 and subsequent treatment with a proteasome inhibitor, we did not see changes in either GRP78 or IRE1α protein levels (Figure 4—figure supplement 2c). These observations suggest that although ER stress markers are elevated upon proteasome inhibition in SMARCB1-deficient cell lines, they are not rescued by SMARCB1 re-expression.

We then performed GO-based GSEA (Subramanian et al., 2005) on the 527 significantly altered genes upon re-expression of SMARCB1 (Supplementary file 6) to identify classes of gene function enriched in this group of genes. We identified numerous gene sets that involved the ubiquitin-proteasome system (Supplementary file 8). We then performed RNA-sequencing on G401 and the RMC cell lines treated with DMSO or MLN2238. We identified 1758 genes which were significantly (FDR < 0.1) up- or down-regulated upon treatment with MLN2238 (Supplementary file 9). We compared the 527 differentially expressed genes identified upon re-expression of SMARCB1 with the 1758 differentially expressed genes identified upon treatment with MLN2238 and identified 92 genes which overlapped. Of these genes, we identified 63 genes which were differentially expressed with re-expression of SMARCB1 and were inversely differentially expressed with treatment with MLN2238 (Figure 4d; Figure 4—source data 2). From this refined gene set, we performed GO-based GSEA (Subramanian et al., 2005) and found significant enrichment (adjusted p-value ranging from 0 to 0.0061) in gene sets involving the cell cycle (Supplementary file 10).

We subsequently assessed the cell cycle by DNA content with cells treated with DMSO or MLN2238 for 24 hr as proteasome inhibitors have been found to cause a G2/M cell cycle arrest in lymphomas, colorectal carcinomas, hepatocellular carcinomas, and glioblastoma multiforme (Augello et al., 2018; Bavi et al., 2011; Gu et al., 2017; Yin et al., 2005). We observed a significant shift in cells to G2/M (two-tailed t-test p-value 0.0005; Figure 4e). Upon re-expression of SMARCB1, we saw that this phenotype was rescued (Figure 4f). By 48 hr, we saw a significant increase in markers of programed cell death such as Annexin V and PI positive cells (Figure 4g).

We found that treatment with a proteasome inhibitor led to increased cleaved caspase-3 levels in addition to changes to Annexin V and PI, suggesting that inhibition of the ubiquitin-proteasome system leads to programmed cell death (Figure 4h). We then asked whether restoration of SMARCB1 expression inhibited cleaved caspase-3 activation. We found that induction of cleaved caspase-3 was less pronounced when SMARCB1 was re-expressed (Figure 4h). These observations suggest that proteasome inhibitors initially lead to a SMARCB1-dependent G2/M cell cycle arrest and subsequent programmed cell death.

To assess whether RMC cells exhibit an increased proclivity to undergo cell death after cell cycle arrest, we asked whether treatment of SMARCB1-deficient cancers with cell cycle inhibitors led only to cell cycle arrest or arrest followed by cell death. Specifically, we used nocodazole, an anti-mitotic agent that disrupts microtubule assembly in prometaphase, and RO-3306, a CDK1 inhibitor which disrupts the CDK1-cyclin B1 interaction during metaphase (Vassilev et al., 2006; Wolf et al., 2006). We treated both G401 and CLF_PEDS9001_T with nocodazole or RO-3306 for 24 hr and observed accumulation of cells in G2/M as well as increased cyclin B1 and cleaved caspase-3 (Figure 4—figure supplement 2d–e) similar to what we observed after treatment with MLN2238. By 72 hr, we found that treatment with either nocodazole or RO-3306 induced cell death in the majority of cells (65–90%) (Figure 4—figure supplement 2f), similar to what we observed when we treated cells with MLN2238 (Figure 4c). These observations suggest that SMARCB1-deficient cell lines are susceptible to programmed cell death following treatment with a cell cycle inhibitor and that the cell cycle arrest observed after treatment with MLN2238 leads to programmed cell death.

### Proteasome inhibitor induced G2/M arrest is mediated in part by inappropriate cyclin B1 degradation driven by a dependency on UBE2C

We subsequently searched for genes related to the ubiquitin-proteasome system and SMARCB1 function. We defined a set of 204 genes that were upregulated when comparing the log2 fold change between SMARCB1 deficient cells and SMARCB1 re-expressed cells in RMC and MRT cell lines (Supplementary file 6). We then took this set of 204 genes and examined the Project Achilles (genome scale CRISPR-Cas9 loss of function screens) DepMap Public 18Q3 dataset (Meyers et al., 2017) to determine whether any SMARCB1 deficient cell lines required expression of these genes for survival. This dataset included loss of function screens from 485 cancer cell lines and included three ATRT SMARCB1-deficient cancer cell lines: COGAR359, CHLA06ATRT and CHLA266. We found that SMARCB1 deficient cancer cell lines required UBE2C, an ubiquitin-conjugating enzyme, for survival. We noted that these cell lines were in the top 5% of cell lines (n = 485) that required UBE2C for survival (empirical Bayes moderated t-test p-value=0.00016; Figure 5a–b; Figure 5—source data 1). These observations suggested that cancer cell lines that lack SMARCB1 were also dependent on UBE2C.

![Figure 5.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig5-v2.jpg)

**Figure 5.:** (a) Volcano plot identifying genes that are required for survival in SMARCB1 deficient cancers. 204 genes were significantly upregulated when comparing the log2 fold change between SMARCB1 deficient cells and SMARCB1 re-expressed cells (Supplementary file 6). We assessed how loss of these genes affected viability in 3 cell lines with loss of SMARCB1 as compared to the rest of the 482 cell lines in Project Achilles DepMap 18Q3, a genome-wide loss of function screen using CRISPR-Cas9 and calculating an effect size (e.g. differential of the 3 cell lines to 482 cell lines). A negative effect size identifies genes when deleted are required for cells for survival and the 204 genes are identified in red. Deletion of UBE2C was significantly depleted. Deletion of SMARCB1 serves as a positive control in these SMARCB1 deficient cancers as these cell lines have loss of SMARCB1. (b) SMARCB1 deficient lines are in the top 5% of cell lines ranked by how dependent they are on UBE2C based on Project Achilles DepMap 18Q3 dataset. Three ATRT cancer cell lines (red dots; CHLA266, CHLA06, COGAR359) were compared to 482 cell lines profiled in Project Achilles (CERES dataset 18Q3). (c) Gene deletion of UBE2C by CRISPR-Cas9 leads to significant viability defects in RMC and MRT cell lines as compared to either SWI/SNF wt cell line, JMSU1 (day 10), or SMARCA4 mutant cell line, A549 (day 6). Error bars shown are standard deviations from two biological replicates. * indicates a two-tailed t-test p-value<0.05 and **<0.005. (d) Treatment with proteasome inhibitor, MLN2238 at 200 nM, leads to upregulation of cyclin B1 and this phenotype is rescued upon SMARCB1 re-expression in both CLF_PEDS0005_T1 and CLF_PEDS9001_T1. Cyclin D1 is included as a control to ensure that the effects of proteasome inhibition are specific to cyclin B1. Blots are representative of two biological replicates. (e) G401 xenograft tumor growth over time by individual mouse shows that treatment effects from MLN2238 can be seen as early as 8 days from treatment initiation as compared to vehicle control. Over 26 days, tumor volumes were significantly decreased in MLN2238 treated mice. **** indicates two-way ANOVA test with p-value<0.0001. (f) Waterfall plot of each tumor by log2 change in tumor volume on the left y-axis and correlative percent change in tumor volume on the right y-axis following 26 days of treatment with either vehicle (black) or MLN2238 (red). * indicates a two-tailed t-test p-value<0.05. (g) Kaplan-Meier curves from mice with G401 xenograft tumors treated with either vehicle or MLN2238 over 61 days. * indicates a p-value of 0.0489 by log-rank (Mantel-Cox) test.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a) Suppression of UBE2C protein by immunoblot when utilizing CRISPR-Cas9 guide RNAs targeting UBE2C. c-MYC levels modestly decreased upon UBE2C deletion in SMARCB1 deficient cell lines. Blots representative of at least two biological repeats. (b) Proteasome inhibitors suppress proteasome activity following one hour of treatment by assessing the cell’s ability to cleave Suc-LLVY-aminoluciferin following a one-hour treatment with a proteasome inhibitor as indicated in the figure (Materials and methods). Bortezomib was at 15 nM, MLN2238 was at 100 nM and MLN2238 pulse was at 2.5 μM. Error bars represent standard deviation from at least three biological replicates. (c) Pulse treatment with MLN2238 at 2.5 μM leads to significant viability defects in SMARCB1 deficient cell lines similar to multiple myeloma cell line, RPMI8226, and contrasts to lung non-small cell lung cancer cell line, H2172. Error bars are standard deviations from a two biological replicates. ** indicates a p-value<0.005 and *** indicates a p-value<0.0005. (d) and (e) Cell cycle analysis of G401 (d) or CLF_PEDS9001_T1 (e) treated with a continuous dose (200 nM) or a pulse dose (2.5 μM) of MLN2238 shows an increase in cells arrested in G2/M. Error bars represent standard deviation from at least two biological replicates. (f) Pulse treatment with MLN2238 (2.5 μM) in CLF_PEDS9001_T1 leads to increased populations that are Annexin V/PI and PI positive. Figures representative of 3 biological replicates.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/44161/elife-44161-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (a) Pulse treatment with MLN2238 (2.5 μM) in CLF_PEDS9001_T1 in the setting of re-expression of SMARCB1 leads to a decreased fold change in double Annexin V+/PI + cells. Error bars represent standard deviation from at least two biological replicates. * two-tailed t-test p-value<0.05. (b) Viability defects seen with pulse treatment with MLN2238 can be rescued with re-expression of SMARCB1 in SMARCB1 deficient cell lines. Error bars shown are standard deviations from two biological replicates. * indicates a two-tailed t-test p-value<0.05, **<0.005, ***<0.0005. (c) Pulse treatment with proteasome inhibitor, MLN2238, leads to upregulation of cyclin B1 and this phenotype is rescued upon SMARCB1 re-expression in both CLF_PEDS0005_T1 and CLF_PEDS9001_T1. Cyclin D1 is included as a control to ensure that the effects of the proteasome are specific to cyclin B1. Blots are representative of two biological replicates. (d) and (e) Primary tumor RMC cell lines (CLF_PEDS0005_T1 and CLF_PEDS9001_T) do not form tumors in vivo. 5 million cells were injected subcutaneously into Taconic immunodeficient mice and were monitored for tumor formation over 41 to 54 days. (f) % change in body weight of mice at day 26 as compared to day one following treatment with vehicle or with MLN2238. n.s. not significant based on a two-sided t-test p-value. (g) Immunoblot comparing pairs of vehicle and MLN2238 treated mice. One mouse tumor which responded to MLN2238 had activation of cleaved caspase-3 and increased cyclin B1 while one non-responder had no activation of these biomarkers.

Since the 3 cell lines profiled were ATRTs, we validated that the RMC cell lines were also dependent on UBE2C for survival. We generated sgRNAs specific for UBE2C and assessed viability by cell counting following gene deletion. We saw a significant decrease in cell viability in SMARCB1 deficient cell lines as compared to urothelial carcinoma cell line, JMSU1 (SWI/SNF wild type), or non-small cell lung cancer cell line, A549 (SMARCA4 mutant) (two-tailed t-test p-values 4.5e-5 and 4.6e-5; Figure 5c and Figure 5—figure supplement 1a).

UBE2C serves as the E2 enzyme which adds the first ubiquitin (Ub) to cyclin B1 for degradation (Dimova et al., 2012; Grice et al., 2015). Cyclin B1 degradation is required in G2/M at the end of metaphase to enter anaphase (Chang et al., 2003). Our integrated RNAi, CRISPR-Cas9 and small molecule screens identified that our RMC models required expression of PLK1 and CDK1, genes involved in G2/M, for survival (Figure 3a–b), and prior studies have identified that inhibition of PLK1 in ATRT or MRT cells leads to arrest in G2/M (Alimova et al., 2017; Morozov et al., 2007). Treatment of the RMC cell lines with MLN2238 led to accumulation of cyclin B1 as compared to cyclin D1 suggesting that MLN2238 inhibits degradation of cyclin B1 (Figure 5d). When we re-expressed SMARCB1, we found that cyclin B1 levels were unchanged upon MLN2238 treatment. Although APC/C serves as the E3 ligase for cyclin B1, genetic deletion of APC/C in Project Achilles showed that APC/C was an essential gene across all cancer cell lines. These findings suggest SMARCB1 deficient cancer cells require UBE2C expression for survival, in part by regulating cyclin B1 stability.

### Effects of proteasome inhibition in vivo

These studies identify a lethal interaction between suppressing the UPS and SMARCB1-deficient cancers in vitro. The doses used in this study were based on in vitro studies of multiple myeloma or lymphoma cell lines (Chauhan et al., 2011; Garcia et al., 2016; Hideshima et al., 2003; Hideshima et al., 2001). For patients with primary or refractory multiple myeloma, use of proteasome inhibitors has led to significant clinical responses (Jagannath et al., 2004; Moreau et al., 2016; Richardson et al., 2005; Richardson et al., 2003). We reasoned that if our SMARCB1 deficient cancers were susceptible to proteasome inhibitors at similar in vitro dosing, we would also see similar in vivo responses. We first determined whether these doses led to proteasome inhibition by assessing the ability of these cell lines to cleave Suc-LLVY-aminoluciferin. We found that treatment of the SMARCB1 deficient cell lines with either bortezomib or MLN2238 led to inhibition of the proteasome to a similar extent observed when the multiple myeloma cell line RPMI8226 was treated (Figure 5—figure supplement 1b; Materials and methods). We also simulated the pharmacodynamics of proteasome inhibitors in vivo by treating cells in vitro with a pulse dose of proteasome inhibitors as has been performed in multiple myeloma and chronic myeloid leukemia cell lines (Crawford et al., 2014; Kuhn et al., 2007; Shabaneh et al., 2013). We found that upon treatment with MLN2238, SMARCB1 deficient cells arrested in G2/M, which led to cell death as measured by Annexin V/PI staining and led to accumulation of cyclin B1 similar to treatment with a continuous dose of MLN2238 (Materials and methods; Figure 5—figure supplement 1c–f and Figure 5—figure supplement 2a–c).

We subsequently performed in vivo studies to confirm the effect of proteasome inhibition in tumor xenografts. We used the rhabdoid tumor cell line, G401, for our in vivo studies because we noted that the primary tumor cell lines (CLF_PEDS0005_T1 and CLF_PEDS9001_T) did not form subcutaneous xenograft tumors in immunodeficient mice (Figure 5—figure supplement 2d–e; Materials and methods). We allowed tumors to achieve an average volume of 148 mm3 and then treated mice with either vehicle or MLN2238 at the maximum tolerated dose at 7 mg/kg twice a week in the Taconic NCr-nude mouse strain. Treatment with MLN2238 over 26 days induced significant tumor stabilization or regression as compared to vehicle treated tumors as assessed by absolute tumor volume (two-way ANOVA test with p-value<0.0001; Figure 5e–f) and did not induce significant changes in body weight as compared to vehicle-treated tumors (two-tailed t-test p-value 0.154; Figure 5—figure supplement 2f). Furthermore, mice treated with MLN2238 survived significantly longer [p-value 0.0489 by log-rank (Mantel-Cox) test; Figure 5g].

We noted that several tumors in the treatment arm had a suboptimal response to MLN2238 (Figure 5e–f). We harvested tumors from two pairs of mice that either showed regression or no response to MLN2238 and assessed cleaved caspase-3 and cyclin B1 levels. We found increased cyclin B1 and cleaved caspase-3 by immunoblotting in the tumor that responded to MLN2238 but did not observe increased cyclin B1 accumulation or activation of cleaved caspase-3 in the tumor without response (Figure 5—figure supplement 2g) suggesting that adequate inhibition of the proteasome was not achieved in mice with a suboptimal response. Combined, these results demonstrate that MLN2238 induces a cytostatic response in SMARCB1-deficient tumors in vivo.

## Discussion

We have developed faithful patient-derived models of RMC which have been genomically validated using WGS, WES, RNA-sequencing and gene expression profiling. We have shown that these models are dependent upon the loss of SMARCB1 for survival. Re-expression of SMARCB1 in RMC leads to a significant decrease in cell counts and a senescence phenotype. Biochemically, re-expression of SMARCB1 in RMC leads to stabilization of the SWI/SNF complex in the same manner as re-expression of SMARCB1 in MRT. Diagnostically, patients with RMC are often misdiagnosed with renal cell carcinoma (RCC) due to the rarity of RMC, the lack of access to SMARCB1 histological stains and unknown sickle cell status (Beckermann et al., 2017). Although SMARCB1 is currently included in targeted sequencing efforts nationwide (AACR Project GENIE Consortium, 2017), our studies along with prior studies (Calderaro et al., 2016; Carlo et al., 2017) suggest that conventional target exome sequencing may fail to identify patients with RMC.

Patients with RMC and other SMARCB1 deficient cancers have a poor prognosis despite aggressive multi-modal therapy. Using genetic and pharmacologic screens in these RMC models, we identified the ubiquitin-proteasome system as a specific vulnerability in RMC. When we looked more broadly at other SMARCB1 deficient cancers such as MRT and ATRT, we found that these models were similarly sensitive to inhibition of the ubiquitin-proteasome system. Re-expression of SMARCB1 partially rescued the sensitivity to proteasome inhibitors in RMC and MRT models.

Prior studies have implicated MYC signaling and downstream activation of ER stress as a mechanism for sensitivity to proteasome inhibitors in Kras/Tp53 mutant pancreatic cancers with Smarcb1 deficiency (Genovese et al., 2017; Moreau et al., 2016). However, the background of mutant KRAS may be contributing to these findings as mutant HRAS or KRAS cancers are sensitive to enhanced proteotoxic stress and ER stress. Furthermore, KRAS mutant cancers depend on several proteasome components in genome scale RNAi screens (Aguirre and Hahn, 2018). Our studies have identified that the ubiquitin-proteasome system is a core vulnerability among a compendium of druggable targets as tested by orthogonal methods of RNA interference, CRISPR-Cas9 gene deletion or small molecule inhibition. We found that proteasome inhibition in SMARCB1-deficient cancer cell lines results in G2/M arrest due to inappropriate degradation of cyclin B1.

Although in multiple myeloma cells, tumor regression has been observed in xenografts following treatment with MLN2238 (Chauhan et al., 2011), we found that treatment with MLN2238 of SMARCB1 deficient xenografts led to a cytostatic response. This finding is similar to what has been observed in xenograft models of non-small cell lung cancer (14 tumor models) and colon cancer (6 tumor models) (Chattopadhyay et al., 2015). We note that these studies were performed in mice that tolerated MLN2238 treatments at 11–14 mg/kg (Chauhan et al., 2011), a dose which we were unable to achieve in the Taconic Ncr-nude mice and may have led to the observed heterogeneous tumor response to MLN2238 treatment. Nevertheless, these studies still support the importance of testing this hypothesis in patients, particularly since there are no standard therapies for SMARCB1-deficient cancers.

There have been case reports of one adult and two children with RMC who exhibited extraordinary responses for 2–7 years following diagnosis after empiric therapy with bortezomib either as monotherapy or in combination with chemotherapy (Carden et al., 2017; Ronnen et al., 2006). Our findings suggest that testing oral proteasome inhibitors such as MLN2238 for patients with RMC and potentially more broadly across SMARCB1-deficient cancers is warranted.

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
      <td>Gene (Homo sapiens)</td>
      <td>SMARCB1</td>
      <td>NA</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>PSMB5</td>
      <td>NA</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>CCNB1</td>
      <td>NA</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>UBE2C</td>
      <td>NA</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>CrTac:NCr-Foxn1nu</td>
      <td>Taconic Biosciences</td>
      <td>RRID:IMSR_TAC:ncrnu</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent ()</td>
      <td>Luciferase</td>
      <td>this paper</td>
      <td>RRID:Addgene_117072</td>
      <td>Backbone: pXPR_BRD003</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>UBE2C guide 1</td>
      <td>this paper</td>
      <td>RRID:Addgene_117068</td>
      <td>Backbone: pXPR_BRD003</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>UBE2C guide 2</td>
      <td>this paper</td>
      <td>RRID:Addgene_117071</td>
      <td>Backbone: pXPR_BRD003</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>PSMB5 guide 1</td>
      <td>this paper</td>
      <td>RRID:Addgene_117073</td>
      <td>Backbone: pXPR_BRD003</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>PSMB5 guide 2</td>
      <td>this paper</td>
      <td>RRID:Addgene_117074</td>
      <td>Backbone: pXPR_BRD003</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>pDONR223 SMARCB1</td>
      <td>this paper</td>
      <td>RRID:Addgene_111181</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>pLXI_401 LacZ</td>
      <td>this paper</td>
      <td>RRID:Addgene_111183</td>
      <td>Backbone: pLXI_403</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>pLXI_403 LacZ</td>
      <td>this paper</td>
      <td>RRID:Addgene_111184</td>
      <td>Backbone: pLXI_403</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>pLXI_401 SMARCB1</td>
      <td>this paper</td>
      <td>RRID:Addgene_111182</td>
      <td>Backbone: pLXI_401</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>pLXI_403 SMARCB1</td>
      <td>this paper</td>
      <td>RRID:Addgene_111185</td>
      <td>Backbone: pLXI_403</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>CP1050</td>
      <td>PMID: 27329820</td>
      <td></td>
      <td>Druggable Cancer Targets v1.0 library (shRNA)</td>
    </tr>
    <tr>
      <td>Genetic reagent (Homo sapiens)</td>
      <td>CP1074</td>
      <td>PMID: 27329820</td>
      <td></td>
      <td>Druggable Cancer Targets v1.0 library (CRISPR-Cas9)</td>
    </tr>
    <tr>
      <td>Cell line (Homo  sapiens)</td>
      <td>CLF_PEDS0005_N</td>
      <td>this paper</td>
      <td></td>
      <td>normal kidney cell line</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>CLF_PEDS0005_T1</td>
      <td>this paper</td>
      <td></td>
      <td>primary RMC cell line</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>CLF_PEDS0005_T2A</td>
      <td>this paper</td>
      <td></td>
      <td>metastatic RMC cell line (adherent)</td>
    </tr>
    <tr>
      <td>Cell line (Homo  sapiens)</td>
      <td>CLF_PEDS0005_T2B</td>
      <td>this paper</td>
      <td></td>
      <td>metastatic RMC cell line (suspension)</td>
    </tr>
    <tr>
      <td>Cell line (Homo  sapiens)</td>
      <td>CLF_PEDS9001_T1</td>
      <td>this paper</td>
      <td></td>
      <td>primary RMC cell line</td>
    </tr>
    <tr>
      <td>Cell line (Homo  sapiens)</td>
      <td>CLF_PEDS1012_T1</td>
      <td>this paper</td>
      <td></td>
      <td>Wilms tumor cell line</td>
    </tr>
    <tr>
      <td>Cell line (Homo  sapiens)</td>
      <td>G-401</td>
      <td>ATCC</td>
      <td>CRL-1441 RRID:CVCL_0270</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>RPMI 8226</td>
      <td>ATCC</td>
      <td>CCL-155 RRID:CVCL_0014</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo  sapiens)</td>
      <td>NCI-H2172</td>
      <td>ATCC</td>
      <td>CRL-5930 RRID:CVCL_1537</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>A549</td>
      <td>ATCC</td>
      <td>CCL-185 RRID:CVCL_0023</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HA1E</td>
      <td>other</td>
      <td></td>
      <td>Cell line maintained in W. C. Hahn lab</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>JMSU1</td>
      <td>PMID: 30777879</td>
      <td>RRID:CVCL_2081</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-cytokeratin CAM5.2</td>
      <td>BD Biosciences</td>
      <td>349205 RRID:AB_2134314</td>
      <td>Immunohistochemistry</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-SMARCB1/BAF47</td>
      <td>BD Biosciences</td>
      <td>612110 RRID:AB_399481</td>
      <td>Immunohistochemistry</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-ARID1A (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-373784 RRID:AB_10917727</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>antii-α-tubulin (mouse monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>T9026 RRID:AB_477593</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-β-actin (C-4) (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-47778 RRID:AB_2714189</td>
      <td>1:10,000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-β-actin (D6A8) (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#8457 RRID:AB_10950489</td>
      <td>1:10,000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-BAF57/SMARCE1 (rabbit polyclonal)</td>
      <td>Bethyl Laboratories, Inc.</td>
      <td>A300-810A RRID:AB_577243</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-BAF60a (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-135843 RRID:AB_2192137</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-SMARCC1/BAF155 (D7F8S) (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#11956</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-BAF170 (G-12) (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-166237 RRID:AB_2192013</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-SMARCA4 (G-7) (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-17796 RRID:AB_626762</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Cleaved Caspase-3 (Asp175) (5A1E) (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#9664 RRID:AB_2070042</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-c-Myc (N-262) (rabbit polyclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-764 RRID:AB_631276</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-c-Myc (rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#9402 RRID:AB_2151827</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-cyclin B1 (V152) (mouse monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#4135 RRID:AB_2233956</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-cyclin B1 (rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#4138 RRID:AB_2072132</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-cyclin D1 (M-20) (rabbit polyclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-718 RRID:AB_2070436</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GAPDH (14C10) (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#2118 RRID:AB_561053</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GAPDH (D4C6R) (mouse monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#97166 RRID:AB_2756824</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GRP78 (mouse monoclonal)</td>
      <td>Rockland Immunochemicals</td>
      <td>200–301 F37 RRID:AB_2611159</td>
      <td>1:10,000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-IRE1α (14C10) (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#3294 RRID:AB_823545</td>
      <td>1:2000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Lamin A/C (rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#2032 RRID:AB_2136278</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-PSMB5 (rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>ab3330 RRID:AB_303709</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-SMARCB1/SNF5 (rabbit polyclonal)</td>
      <td>Bethyl Laboratories, Inc.</td>
      <td>A301-087A RRID:AB_2191714</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-UBE2C (mouse monoclonal)</td>
      <td>Proteintech</td>
      <td>66087–1 RRID:AB_11232220</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QIAamp DNA Blood Midi Kit</td>
      <td>Qiagen</td>
      <td>51183</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QIAprep Spin Miniprep Kit</td>
      <td>Qiagen</td>
      <td>27106</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Rneasy Plus Mini Kit</td>
      <td>Qiagen</td>
      <td>74134</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Qubit RNA HS Assay Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>Q32852</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>KAPA Stranded mRNA-Seq Kit</td>
      <td>Kapa Biosystems</td>
      <td>KK8420</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>KAPA Library Quantification Kit</td>
      <td>Kapa Biosystems</td>
      <td>KK4835</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>High-Capacity cDNA Reverse Transcription Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>4368814</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Power SYBR Green PCR Master Mix</td>
      <td>Thermo Fisher Scientific</td>
      <td>4368708</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Senescence β-Galactosidase Staining Kit</td>
      <td>Cell Signaling Technology</td>
      <td>9860S</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>CellTiter-Glo Luminescent Cell Viability Assay</td>
      <td>Promega</td>
      <td>G7570</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Proteasome-Glo Chymotrypsin-Like Cell-based Assay</td>
      <td>Promega</td>
      <td>G8660</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Annexin V: FITC Apoptosis Detection Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>BD 556547</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PI/Rnase Staining Buffer</td>
      <td>BD Pharmingen</td>
      <td>550825</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>FxCycle PI/Rnase Staining Solution</td>
      <td>Invitrogen</td>
      <td>F10797</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>bortezomib (PS-341)</td>
      <td>Selleck Chemicals</td>
      <td>S1013</td>
      <td>in vitro studies</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ixazomib (MLN2238)</td>
      <td>Selleck Chemicals</td>
      <td>S2180</td>
      <td>in vitro studies</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>nocodazole</td>
      <td>Selleck Chemicals</td>
      <td>S2775</td>
      <td>in vitro studies</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ro-3306</td>
      <td>Selleck Chemicals</td>
      <td>S7747</td>
      <td>in vitro studies</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MLN2238</td>
      <td>MedChem Express</td>
      <td>HY-10453</td>
      <td>in vivo studies</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SvABA v0.2.1</td>
      <td>PMID: 29535149</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlowJo v10.0</td>
      <td></td>
      <td>RRID:SCR_008520</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ComBat</td>
      <td></td>
      <td>RRID:SCR_010974</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism v8.0</td>
      <td></td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GSEA</td>
      <td>Broad Institute</td>
      <td>RRID:SCR_003199</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GATK v.4.0.4.0</td>
      <td>PMID: 20644199</td>
      <td>RRID:SCR_001876</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>TopHat v2.0.11</td>
      <td>PMID: 22383036</td>
      <td>RRID:SCR_013035</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>PMID: 25516281</td>
      <td>RRID:SCR_015687</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Derivation of RMC models

Patients assented or families consented to IRB approved protocols. Patient PEDS0005 whole blood, adjacent normal kidney and tumor tissue were obtained within 6 hr as part of the nephrectomy following neoadjuvant chemotherapy. Upon relapse, pleural fluid was obtained from a palliative thoracentesis. The tumor and adjacent normal kidney tissue was minced into 2–3 mm3 cubes. CLF_PEDS0005 primary tissue was then dissociated as previously described and cultured in both RPMI media containing 10% FBS (Sigma) or DMEM/F-12 media containing ROCK inhibitor, Y-27632, insulin, cholera toxin, 5% FBS, and penicillin/streptomycin (Liu et al., 2012). Samples were gently passaged when cultures achieved 80–90% confluence. The normal kidney cell line was named CLF_PEDS0005_N. The tumor kidney cell line was named CLF_PEDS0005_T1. For the pleural fluid sample, samples were grown initially in conditioned media as previously published (Liu et al., 2012). Adherent and suspension cells were continuously passaged when cells reached confluence. By passage 5, cells were noted to be growing as adherent and suspension cells, and these were sub-cultured to yield CLF_PEDS0005_T2A and CLF_PEDS0005_T2B, respectively. Samples were then transitioned to DMEM/F-12 media or RPMI as above at passage 13.

Patient PEDS9001 whole blood, adjacent normal kidney and tumor tissue were obtained similarly to PEDS0005. Discarded tissue from the nephrectomy following neoadjuvant chemotherapy was sent to our institution within 24 hr of resection. For the normal kidney and tumor tissue, samples were minced to 2–3 mm3 and plated onto six well plates (Corning, NY). Following mincing, tumor samples were cultured without further digestion. Tumor samples were grown in culture in the DMEM/F-12 media as described above to yield CLF_PEDS9001_T1, while the normal samples yielded a cell culture that matched the tumor cell line.

### Immunohistochemistry

All immunohistochemical staining was done in the clinical histopathology laboratory at Boston Children’s Hospital with appropriate positive controls performed with each run. Antibodies used included anti-cytokeratin CAM5.2 (BD Biosciences, 349205) and SMARCB1/BAF47 (BD Biosciences, 612110).

### Breakapart fluorescent in situ hybridization (FISH)

We developed a custom dual-color breakapart FISH probe, using BAC probes surrounding SMARCB1 at 22q11.23: RP11-662F7 (telomeric to SMARCB1, labeled in green) and RP11-1112A23 (centromeric to SMARCB1, labeled in red) (Empire Genomics, Buffalo, NY). The probe set was hybridized to a normal control to confirm chromosomal locations and to determine the frequency of expected fusion signals in normal cells. 50 nuclei were scored by two independent observers (n = 100 per cell line) in the CLF_PEDS0005 and CLF_PEDS9001 models.

### Whole Exome Sequencing

We performed whole exome sequencing (WES) from genomic DNA extracted from whole blood, normal/tumor tissues, and our patient-derived cell lines as noted in the text. One microgram of gDNA (as measured on a Nanodrop 1000 (Thermo Fisher Scientific)) was used to perform standard (~60 x mean target coverage for normal) or deep (~150 x mean target coverage for tumor and cell lines) WES. Illumina (Dedham, MA) chemistry used.

### Whole Genome Sequencing

We performed PCR-free whole genome sequencing (WGS) from gDNA extracted from whole blood, normal/tumor tissues, and our patient-derived cell lines as noted in the text. Two micrograms of gDNA were used to perform standard (for normal) or deep (for tumor and cell lines) coverage. Illumina (Dedham, MA) HiSeq X Ten v2 chemistry was used. We achieved an average depth of coverage of 38x for the germline DNA and 69x for the tumor cell line DNA.

### RNA-sequencing

For Figure 2a, samples were processed using Illumina TruSeq strand specific sequencing. We performed poly-A selection of mRNA transcripts and obtained a sequencing depth of at least 50 million aligned reads per sample. For SMARCB1 re-expression RNAseq experiments and MLN2238 vs DMSO-treated experiments, samples were collected as biological replicates or triplicates. RNA was extracted using Qiagen RNeasy Plus Mini Kit (Qiagen, Hilden, Germany). RNA was normalized using the Qubit RNA HS Assay (Thermo Fisher Scientific). Five hundred ng of normalized RNA was subsequently used to create libraries with the Kapa Stranded mRNA-seq kit (Kapa Biosystems, KK8420; Wilmington, MA). cDNA libraries were then quantitatively and qualitatively assessed on a BioAnalyzer 2100 (Agilent, Santa Clara, CA) and by qRT-PCR with Kapa Library Quantification Kit. Libraries were subsequently loaded on an Illumina HiSeq 2500 and achieved an average read depth of 10 million reads per replicate.

### Genomic analyses

WGS - Samples were aligned to Hg19. Structural variation and indel Analysis By Assembly (SvABA) v0.2.1 was used to identify large deletions and structural variations. (Wala et al., 2018). WES – Samples were aligned to Hg19. Samples were analyzed using GATK v4.0.4.0 for copy number variation (CNV), single nucleotide polymorphism (SNP) and indel identification across our RMC samples simultaneously using filtering parameters set by GATK (Broad Institute, Cambridge, MA) (McKenna et al., 2010). MuTect 2.0 was used to identify candidate somatic mutations and these were filtered based on the Catalogue of Somatic Mutations in Cancer (COSMIC) (Forbes et al., 2015). RNA – CLF_PEDS0005 and CLF_PEDS9001 samples and TARGET Wilms and Rhabdoid tumor samples (dbGaP phs000218.v19.p7) were aligned or re-aligned with STAR and transcript quantification performed with RSEM. The TARGET initiative is managed by the NCI and information can be found at https://ocg.cancer.gov/programs/target. These normalized samples were then analyzed with t-SNE (Maaten, 2014). The following parameters were used in the t-SNE analyses: perplexity 10, theta 0, iterations 3000. RNA sequencing samples in the SMARCB1 re-expression studies were subsequently aligned and analyzed with the Tuxedo suite (e.g. aligned with TopHat 2.0.11, abundance estimation with CuffLinks, differential analysis with CuffDiff and CummeRbund) (Trapnell et al., 2010). For the comparison to previously published work (Wang et al., 2017), the published RNA sequencing samples along with our samples were re-aligned with TopHat 2.0.11 and analyzed with the Tuxedo suite. For samples treated with DMSO or MLN2238, samples were aligned as above and analyzed with DESeq2 (Love et al., 2014).

### Sanger sequencing confirmation of WGS findings

gDNA was extracted using QIAamp DNA mini kit (Qiagen). We performed a mixing study of our RMC cell lines with gDNA isolated from the G401 MRT cell line and then performed PCR amplification. We determined that the lower limits of detection of these fusions with our methods were ~1% of tumor cell line gDNA with a minimum 50 ng of gDNA. We subsequently performed the same PCR reactions with 100 ng of gDNA from the tumor tissue samples. Samples were gel purified and submitted for Sanger sequencing (Eton Bio). We found that the sequences from the tumor tissue samples matched those of the cell lines, confirming that the genomic alterations that we found in the cell lines reflect those found in the original tumor. Primers utilized were CLF_PEDS0005 chr1 forward (ATAAGACATAACTTGGCCGG), CLF_PEDS0005 SMARCB1 reverse (TTTTCCAAAAGGTTTACAAGGC), CLF_PEDS9001 chr12 forward (AAAAGCATATGTATCCCTTGCT), CLF_PEDS9001 SMARCB1 reverse (CCTCCAGAGCCAGCAGA).

### Quantitative RT-PCR

RNA was extracted as above and normalized using the Nanodrop to one microgram. One microgram of RNA was then added to the High Capacity cDNA Reverse Transcription Kit (Thermo Fisher Scientific) and PCR reactions were performed as per manufacturer’s recommendations. cDNA was then diluted and added to primers (Supplementary file 11) and Power SYBR Green PCR Master Mix (Thermo Fisher Scientific). Samples were run on a BioRad CFX384 qPCR System in a minimum of technical quadruplicates. Results shown are representative of at least two biological replicates.

### Gene-expression array analysis

We performed Affymetrix Human Genome U133 Plus 2.0 on our RMC cell lines. We then combined the following GEO datasets using a GenePattern module with robust multi-array (RMA) normalization GSE64019, GSE70421, GSE70678, GSE36133, GSE94321 (Barretina et al., 2012; Calderaro et al., 2016; Johann et al., 2016; Richer et al., 2017; Wang et al., 2017). We utilized COMBAT and then tSNE to account for batch effects and to identify clusters of similarity (Chen et al., 2011; Johnson et al., 2007; Maaten, 2014).

### Glycerol gradients followed by SDS-PAGE

Nuclear extracts and gradients were performed as previously published (Boulay et al., 2017). Briefly, 500 micrograms of nuclear extract from approximately 30 million cells were resuspended in 0% glycerol HEMG buffer containing 1 mM DTT, cOmplete protease inhibitors and PhosStop (Roche). This was placed on a 10–30% glycerol gradient and ultracentrifuged at 40 k RPM for 16 hr at 4C. Following centrifugation, fractions of 550 µL were collected. Samples were then prepared with 1x LDS Sample Buffer (Thermo). Samples were run on a 4–12% Bis-Tris gel and then transferred by immunoblotting in tris-glycine-SDS buffer with methanol. Immunoblots were subsequently blocked with Licor Blocking Buffer (Lincoln, NE) and then incubated with antibodies as noted in the methods section. Immunoblots shown are representative of at least two biological replicates.

### Cell lines

Primary cell lines were authenticated by Fluidigm or WES/WGS sequencing or by qRT-PCR. Cells were tested for mouse antibody production (Charles Rivers Laboratories; Wilmington, MA) and mycoplasma using the Lonza MycoAlertPLUS Mycoplasma Detection Kit (Morristown, NJ). Established cell lines were authenticated by Fluidigm SNP testing. Cell lines were refreshed after approximately 20 passages from the frozen stock.

### Small molecules

Bortezomib, MLN2238, nocodazole and RO-3306 were purchased from SelleckChem (Houston, TX) for the in vitro studies. Compounds were resuspended in DMSO and frozen down in 20 microliter aliquots to limit freeze-thaw cycles. Compounds were added as noted in the figure legends. In vitro studies used 15 nM for bortezomib and 100 nM for MLN2238 or are otherwise specified in the text. For the pulse experiments, we used 2.5 micromolar of MLN2238.

### SMARCB1 induction studies

pDONR223 SMARCB1 was Sanger sequenced (Eton Bio) and aligned to variant 2 of SMARCB1. SMARCB1 was subsequently cloned into the inducible vector pLXI401 or pLXI403 (Genomics Perturbation Platform at the Broad Institute, Cambridge, MA) by Gateway Cloning. LacZ was used as a control. Lentivirus was produced using tet-free serum (Clontech, Mountain View, CA). Cell lines were infected with lentivirus to generate stable cell lines. Cell lines were then confirmed to re-express LacZ or SMARCB1 by titrating levels of doxycycline (Clontech). Parental cell lines were treated with increasing doses of doxycycline to determine the toxicity to cells and measured by Cell-TiterGlo after 96 hr. Cells were then grown with or without doxycycline in a six well plate. Cells were counted by Trypan blue exclusion on a ViCELL XR (Beckman Coulter, Brea, CA) every 4–5 days. Results shown are the average of at least three biological replicates.

### Senescence assays

Cells were plated in a six well dish and treated with or without doxycycline for up to 7 days. Senescence was assessed with the Senescence β-Galactosidase Staining Kit without modifications (Cell Signaling Technologies, Danvers, MA).

### Druggable Cancer Targets (DCT) v1.0 shRNA/sgRNA libraries, pooled screens and small-molecule profiling

These were performed as previously published (Hong et al., 2016). Briefly, we utilized the DCT v1.0 shRNA (CP1050) and sgRNA (CP0026) libraries from the Broad Institute Genetic Perturbation Platform (GPP) (http://www.broadinstitute.org/rnai/public/). Viruses from both pools were generated as outlined at the GPP portal. As CLF_PEDS0005_T2A and CLF_PEDS0005_T2B were expanded, we performed titrations with the libraries as outlined at the GPP portal. For the sgRNA pool, both cell lines were first transduced with Cas9 expression vector pXPR_BRD111. We screened the DCT v1.0 shRNA library in biological replicates and the Cas9 expressing cell lines with the sgRNA pools at an early passage (<20) and at a multiplicity of infection (MOI) <1, at a mean representation rate above 500 cells per sgRNA or shRNA. gDNA was extracted and was submitted for sequencing of the barcodes. We achieved sequencing depths of at least 500 reads per shRNA or sgRNA.

### CRISPR-Cas9 validation studies

sgRNAs targeting the genes noted in the manuscript (e.g. PSMB5, UBE2C and controls; Supplementary file 12) were generated and introduced into the pXPR_BRD003 backbone. These were then sequence confirmed by Sanger sequencing (Eton Biosciences). Lentivirus was produced and used for infection to generate stable cell lines expressing Cas9. Cells were counted or harvested for protein as noted in the text.

### Immunoblots

After indicated treatments, cell lysates were harvested using RIPA buffer (Cell Signaling Technologies) with protease inhibitors (cOmplete, Roche) and phosphatase inhibitors (PhosSTOP, Roche). Antibodies used were as follows: ARID1A (Santa Cruz; sc-373784), α-tubulin (Santa Cruz; sc-5286), β-Actin (C-4) (Santa Cruz; sc-47778), β-Actin (Cell Signaling; 8457), BAF57/SMARCE1 (Bethyl Laboratories, A300-810A), BAF60a (Santa Cruz; sc-135843), BAF155 (Cell Signaling; 11956), BAF170 (Santa Cruz; sc-166237), SMARCA4 (Santa Cruz; 17798), Cleaved Caspase-3 (Cell Signaling; 9664), c-MYC (Santa Cruz; sc-764) or c-MYC (Cell Signaling; 9402), cyclin B1 (Cell Signaling; 4135 and 4138), cyclin D1 (Santa Cruz; sc-718), GAPDH (Cell Signaling; 2118S and 97166S), GRP78 (Rockland Antibodies, Limerick, PA; 200–301 F36), IRE1-alpha (Cell Signaling; 3294), lamin A/C (Cell Signaling; 2032), PSMB5 (Abcam, Cambridge, MA; ab3330), SMARCB1/SNF5 (Bethyl A301-087A), UBE2C (Proteintech, Rosemont, IL; 66087–1). Results shown are representative of at least two biological replicates.

### Cell cycle and Annexin V/PI

Cells were treated using the conditions noted in the text. One million cells were spun down and resuspended in PBS. Cells were then subjected to FITC Annexin V and PI staining as described (BD Pharmigen; 556547). Another set of cells were subjected to PI/RNAse staining (BD Pharmingen; 550825 or Invitrogen F10797). Samples were analyzed within 1 hr with the SA3800 Spectral Analyzer (Sony Biotechnology). Biological replicates were performed. Data were analyzed with FlowJo v10 (FlowJo, Ashland, OR).

### Proteasome function assay

We measured the cell’s ability to cleave Suc-LLVY-aminoluciferin utilizing Proteasome-Glo (Promega) following a one-hour treatment with the noted proteasome inhibitor and measured luminescence. Results shown are from at least two biological replicates.

### In vivo tumor injections

This research project has been reviewed and approved by the Dana-Farber Cancer Institute’s Animal Care and Use Committee (IACUC), in compliance with the Animal Welfare Act and the Office of Laboratory Welfare (OLAW) of the National Institutes of Health (NIH). Five million cells of G401 in 100 µL of a 50% PBS/50% Matrigel (BD Biosciences) mixture were injected subcutaneously into flanks unilaterally in Taconic NCr-Nude (CrTac:NCr-Foxn1nu) female mice at 7 weeks of age. When tumors reached approximately 150 mm3, mice were randomized into various treatment groups: vehicle control (5% 2-hydroxypropyl-beta-cyclodextrin (HPbCD)) or MLN2238 (7 mg/kg IV twice a week for 4 weeks). MLN2238 (diluted in 5% 2-HPbCD) was purchased from MedChem Express. Randomizations to the treatment arm occurred. Blinding was not performed. Statistical analysis was performed using the two-tailed t-test or Mantel-Cox as noted in the text.

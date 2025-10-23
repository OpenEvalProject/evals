# Discovery of novel determinants of endothelial lineage using chimeric heterokaryons

## Authors

- Wing Tak Wong<sup>1</sup>
- Gianfranco Matrone<sup>1</sup> ([ORCID: 0000-0002-6064-0734](https://orcid.org/0000-0002-6064-0734))
- XiaoYu Tian<sup>1</sup>
- Simion Alin Tomoiaga<sup>1</sup>
- Kin Fai Au<sup>1</sup>
- Shu Meng<sup>1</sup>
- Sayumi Yamazoe<sup>3</sup>
- Daniel Sieveking<sup>3</sup>
- Kaifu Chen<sup>1</sup>
- David M Burns<sup>4</sup>
- James K Chen<sup>3</sup>
- Helen M Blau<sup>4</sup>
- John P Cooke<sup>1</sup> ([ORCID: 0000-0003-0033-9138](https://orcid.org/0000-0003-0033-9138)) †

### Affiliations

1. Department of Cardiovascular Sciences Houston Methodist Research Institute Houston United Staes
2. Department of Internal Medicine University of Iowa Iowa City United Staes
3. Department of Chemical and Systems Biology Stanford University School of Medicine Stanford United States
4. Baxter Laboratory for Stem Cell Biology Stanford University School of Medicine Stanford United States

† Corresponding author

## Abstract

10.7554/eLife.23588.001 We wish to identify determinants of endothelial lineage. Murine embryonic stem cells (mESC) were fused with human endothelial cells in stable, non-dividing, heterokaryons. Using RNA-seq, it is possible to discriminate between human and mouse transcripts in these chimeric heterokaryons. We observed a temporal pattern of gene expression in the ESCs of the heterokaryons that recapitulated ontogeny, with early mesodermal factors being expressed before mature endothelial genes. A set of transcriptional factors not known to be involved in endothelial development was upregulated, one of which was POU class 3 homeobox 2 (Pou3f2). We confirmed its importance in differentiation to endothelial lineage via loss- and gain-of-function (LOF and GOF). Its role in vascular development was validated in zebrafish embryos using morpholino oligonucleotides. These studies provide a systematic and mechanistic approach for identifying key regulators in directed differentiation of pluripotent stem cells to somatic cell lineages. DOI: http://dx.doi.org/10.7554/eLife.23588.001

## Introduction

Our understanding of the genetic and epigenetic processes governing endothelial development and differentiation is limited (Yan et al., 2010; De Val and Black, 2009). Accordingly, our methodologies for obtaining endothelial cells from pluripotent stem cells are empirically driven and suboptimal (Choi et al., 2009; James et al., 2010; Huang et al., 2010a, 2010b; Wong et al., 2012). There is unexplained inconsistency in the yield of iPSC-ECs; in the stability of their phenotype; and in the fidelity of differentiation (in terms of replicating the epigenetic and genetic profile of a mature endothelial cell). Furthermore, our ability to efficiently generate specific endothelial subtypes (e.g. arterial, venous, lymphatic) is poor. Thus, a systematic approach is needed to more completely define the genetic and epigenetic programs required for differentiating pluripotent stem cells to the endothelial phenotype. Here, we propose an unbiased systematic approach to discover determinants of differentiation. We use interspecies heterokaryons, RNA sequencing and third-generation bioinformatics to discover novel candidate genes critical for proper endothelial differentiation and specification.

## Results

## Interspecies heterokaryons as a discovery tool

To discover new genes involved in endothelial specification, we made heterokaryons consisting of human endothelial cells (hEC) and murine embryonic stem cells (mESC) (

![Figure 1.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig1-v2.jpg)

**Figure 1.:** (a) Scheme for heterokaryon generation. GFP-labeled murine ESCs (mESCs) were fused with Cell Tracker Red labeled human ECs (hECs) by HVJ-enveloped fusagen to induce multinucleated heterokaryons. (b) Representative image of non-dividing multinucleated heterokaryons labeled with CD31 (Red) and GFP (Green), Hoechst (Blue) dye were used to label nuclei. (c) Representative FACS plots for heterokaryons. (d–g) Up-regulation of murine EC genes including Kdr, Tie2, Cdh5 and Vwf in heterokaryons consisting of mESC and hEC compared to co-culture control. (h–k) Up-regulation of human EC genes including Kdr, Tie2, Cdh5 and Vwf in heterokaryons consisting of human iPSC (hiPSC) and murine EC (mEC) compared to Co-culture control. (l–n) Increased expression of transcription factors involved in endothelial development such as Etv2, Ets1 and Tal1 during cell fusion of mESC with hEC. (p–r) Increased expression of transcription factors involved in endothelial development such as Etv2, Ets1 and Tal1 during cell fusion of hiPSC with mEC. (o and s) Down-regulation of genes encoding pluripotent factors (Oct4, Sox2 and Nanog) in heterokaryons compared to Co-culture control. All data represented as mean ± S.E.M. (n = 3). p<0.05 vs Co-culture control.DOI: http://dx.doi.org/10.7554/eLife.23588.003

## Optimization and testing of the heterokaryon system

Reprogramming of the cell population is synchronized upon the addition of the fusagen. Since there is no nuclear fusion, chromosome rearrangement, or chromosome loss in the heterokaryons (Bhutani et al., 2010), we reasoned that this synchronization would permit us to study the temporal sequence of reprogramming to endothelial lineage using RNA seq. We optimized the cell fusion strategy using the fusagen HVJ (Sendai virus) envelope protein. By skewing the ratio of the input cells so that endothelial cells outnumbered pluripotent stem cells in the multinucleate heterokaryon, we forced reprogramming of the pluripotent stem cell nuclei toward an endothelial phenotype. To confirm that the system was working as anticipated, we assessed the expression of the mESC mRNA transcripts using murine-specific primers. In mESCs which were fused with human endothelial cells, we observed upregulation of murine endothelial genes including Kdr, Tie2, Cdh5 and Vwf (Figure 1d–g), and transcription factors involved in endothelial development such as Etv2, Ets1 and Tal1 (Figure 1l–n). Intriguingly, the expression of these genes seemed to mirror ontogeny, in that genes involved early in mesoderm specification (e.g. Kdr) were expressed earlier in the heterokaryon, whereas genes that are more specific to hemato-endothelial lineage (e.g. Von Willebrand factor) were expressed later. In parallel to the upregulation of genes involved in endothelial development, we observed down-regulation of genes encoding pluripotent factors (Oct4, Sox2 and Nanog) (Figure 1o).

As a complementary approach, we generated heterokaryons consisting of murine endothelial cells (mEC) and human-induced pluripotent stem cells (hiPSC). We fused hiPSCs with mECs, and the expression of human mRNA transcripts was assessed using human specific primers. We observed in the pluripotent cells an upregulation of human genes including Kdr, Tie2, Cdh5 and Vwf (Figure 1h–k), and transcription factors involved in endothelial development such as Etv2, Ets1 and Tal1 (Figure 1p–r). Again, we observed a temporal sequence that mirrored ontogeny, with a parallel downregulation of genes encoding pluripotent factors (Oct4, Sox2 and Nanog) (Figure 1s). These results demonstrate rapid induction of endothelial genes in the heterokaryon which appears to recapitulate endothelial development.

## RNA seq for novel EC determinants

Having observed that the heterokaryon system seemed to mirror endothelial ontogeny, we applied RNA-seq to identify novel determinants of endothelial lineage (

![Figure 2.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig2-v2.jpg)

**Figure 2.:** (a) Heat map to show expression level of genes that are up- or down-regulated either uniquely in the Heterokaryon (Het) at 6 hr after fusion or commonly in all het samples relative to the mESC samples. mESCs were exposed to a standard endothelial differentiation protocol for 4 or 8 days. Het_6 hr, Het_12 hr, and Het_24 hr indicate mouse stem cells (mESC) fused with human endothelial cells (hEC) for 6, 12 or 24 hr. Co-Culture_6 hr and Co-Culture_24 hr indicate mESC co-cultured but not fused with hEC. (b) Venn diagram to show overlap of upregulated (left) or downregulated (right) mouse genes in heterokaryon at 6, 12 and 24 hr after fusion relative to mESC. (c) Unbiased hierarchical clustering of all samples based on all genes that are differentially expressed in mESC samples relative to at least one of the other samples. (d) Heat map displaying upregulated and downregulated genes in heterokaryons and in differentiating mESC at different time points. Genes differentially expressed were clustered into groups for functional analysis and presented as a heat map based on their enrichment Q value.( e–f) Bar plot showing enrichment Q values of 17 functional terms in genes upregulated (left) or downregulated (right) in mESCs within heterokaryons relative to the mESCs. Upregulated or downregulated genes were defined based on EdgeR FDR cutoff 1e-5. Overlap p value in pie chart was calculated based on Fisher’s Exact test. N = 3 for Het, n = 2 for mESCs, n = 1 for co-culture.DOI: http://dx.doi.org/10.7554/eLife.23588.004

Unbiased hierarchical clustering analysis indicated that the transcriptome of the mESC in the heterokaryon is closer to that of mESCs differentiated toward EC lineage, than to the parental mESCs (Figure 2c). By contrast, the transcriptome of mESC co-cultured (but not fused) with hECs bears a closer relationship to the transcriptome of the parental mESCs. Global gene function enrichment analysis indicates that differentially up- or down-regulated genes in the mESC in heterokaryons are similar to those in mESC exposed to the endothelial differentiation protocol (Figure 2d). In particular, the upregulated genes in the heterokaryons tend to be involved in transcription regulation, RNA alternative splicing, DNA binding, embryonic organ development, differentiation and regulation of cell proliferation (Figure 2e), whereas downregulated genes are implicated in ATP and ribonucleotide binding (Figure 2f). These results suggest that the heterokaryon system may serve as an effective model for cell differentiation.

## Validation of Pou3f2 in differentiation to EC lineage

To validate our approach in discovery of novel determinants of cell lineage, we focused on Pou3f2, which was identified as a candidate EC transcription factor in the RNA seq studies. Accordingly, we examined the temporal sequence of gene expression of Pou3f2 in the heterokaryon system (

![Figure 3.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig3-v2.jpg)

**Figure 3.:** (a) Gene expression pattern of Pou3f2 in heterokaryons consisting of mESC and hEC compared to Co-culture control. (b) Validation of expression of Pou3f2 during differentiation of mESC into endothelial lineage. (c) Lentiviral mediated shRNA KD of Pou3f2 reduced the gene expressions of endothelial markers including Kdr, Tie2, Nos3, Cdh5 and Vwf at Day 8 following endothelial differentiation from mESC. (d) KD of Pou3f2 reduced the gene expressions of transcription factors involved in endothelial differentiation such as Ets1, Erg, Etv2 and Fli1 in mESC differentiated to endothelial lineage at Day 8. (e) No differences were found in the expressions of mesodermal (Bmp4, T), endodermal (Cxcr4 and Gata4) and ectodermal (Pax6 and Nestin) in Pou3f2 shRNA treated mESC following endothelial differentiation at Day 8. (f and g) Representative FACS plots and summarized diagram showing that Pou3f2 KD reduces the yield of mESC-derived CD31+ and CD144+ cells at Day 10 of endothelial differentiation protocol. (h) Representative images showing that Pou3f2 KD mESC-derived ECs manifest an impaired ability to form endothelial networks on matrigel. All data represented as mean ± S.E.M. (n = 3). p<0.05 vs control shRNA.DOI: http://dx.doi.org/10.7554/eLife.23588.005

To further characterize the role of Pou3f2 in the differentiation of mESC into EC, we performed lentiviral shRNA knockdown (KD) of Pou3f2 in mESCs, and subjected the KD mESCs to the endothelial cell differentiation protocol. We found that KD of Pou3f2 reduced the expression of endothelial genes including Kdr, Tie2, Nos3, Cdh5 and Vwf at Day 8 of the differentiation protocol (Figure 3c). Similarly, the expression of endothelial transcription factors such as Ets1, Erg, Etv2 and Fli1 were also reduced in the Pou3f2 KD mESC (Figure 3d). The KD of Pou3f2 in mESC did not affect the expression of mesoderm- (Bmp4, T), endoderm- (Cxcr4, Gata4) or ectoderm- (Pax6 and Nestin) related genes (Figure 3e). Notably, the generation of mESC-derived CD31+ and CD144+ cells were reduced by over 50% in Pou3f2 KD group (Figure 3g). Furthermore, Pou3f2 KD mESC-derived endothelial cells manifested poor network formation on matrigel (Figure 3h). To summarize, Pou3f2 seems to be necessary for the full expression of genes known to be involved in endothelial development, and for the efficient generation of fully functioning endothelial cells. Amongst the factors released from endothelial cells in the heterokaryons that could control Pou3f2 expression there is Wnt and β-catenin. The Wnt/B-catenin signalling pathway is highly conserved and regulates vascular cell fate and development through Dll4/Notch signalling (Corada et al., 2010). The promoter for the Pou3f2 gene is a direct target for β-catenin/Lef1 (Goodall et al., 2004a). Endothelial cells in the heterokaryon might also contribute phosphatidylinositol 3-kinase to activate Pou3f2. The PI3K pathway mediates angiogenesis and the expression of growth factors in endothelial cells (Jiang et al., 2000) and also regulates Pou3f2 in melanoma cells (Bonvin et al., 2012).

## Importance of Pou3f2 in EC development

Pou3f2 promotes neurogenesis (Jaegle et al., 2003; Castro et al., 2006; Dominguez et al., 2013; Sugitani et al., 2002). Specifically, it activates the Notch ligand Delta1, synergistically with Mash1, to maintain a subset of neural progenitors in an undifferentiated state (Castro et al., 2006), whereas it suppresses the Notch effector Hes5 (Dominguez et al., 2013) that negatively regulate transcription of neurogenesis-promoting genes Neuregulins (Imayoshi et al., 2008). In human melanoma spheres and tumor xenograft, Pou3f2 is proposed to induce the Notch pathway (Thurber et al., 2011). In our studies, the importance of Pou3f2 in endothelial development in vivo was assessed using the zebrafish model. The availability of transgenics expressing endothelial-specific fluorescent reporters, for example Tg(fli1:EGFP)y1, combined with the transparency of the embryo, facilitate visualization of vascular development and blood flow in real time (Baldessari and Mione, 2008; Ellertsdóttir et al., 2010; Holden et al., 2011; Kamei et al., 2010).

In situ hybridization for

![Figure 4.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig4-v2.jpg)

**Figure 4.:** tg(fli1:EGFP) zebrafish embryo.y1(a) Bright-field images of embryos injected with caged morpholino against Pou3f2 translation start site in the absence of photoactivation (control), or with photoactivation with UV light at 6 or 24 hpf. (b) Fluorescence images of embryos at 48 hpf. Experimental groups were injected with caged morpholino against Pou3f2 in the absence of photoactivation (control), or with photoactivation with UV light at 6 or 24 hpf, or with photoactivation at 6 hr in the presence of rescue mRNA encoding Pou3f2. (c) Quantitation of the number of intersegmental vessels in 20 somites in embryos at 48 hpf. (d) In situ hybridization with antisense RNA probes specific for Kdr and Fli1 in whole zebrafish embryos 28 hpf. (e) Western blotting showing the reduction level of Pou3f2 following morpholino injection and rescue by mRNA encoding Pou3f2. β-Tubulin was used as loading control. ISV – Intersegmental Vessels; hpf – hour post fertilization. (f and g). Representative FACS plot and scatter plot showing a significant reduction of GFP+ cells in Pou3f2 KD embryos. GFP+ cells were sorted following isolation by enzymatic digestion from tg(fli1:EGFP) zebrafish embryos at 24 hpf. All data represented as mean ± S.E.M. N = 3. Student t-test, *p=0.01; ***p=0.001.y1DOI: http://dx.doi.org/10.7554/eLife.23588.00610.7554/eLife.23588.007Figure 4—source data 1.DOI: http://dx.doi.org/10.7554/eLife.23588.007

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Sense and Pou3f2-specific antisense RNA probe shows high expression of Pou3f2 in the head region, including the eye, hindbrain, midbrain and forebrain. Sense RNA probe was used as negative control.DOI: http://dx.doi.org/10.7554/eLife.23588.008

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Endothelial (A) and hematopoietic (B) cells were FACS purified from Tg(Fli1:EGFP cells) and Tg(C-myb:EGFP) larvae at 48 and 96 hpf, respectively. Total RNA was extracted and real-time PCR performed for Pou3f2 (β-actin was used as housekeeping gene). All data represented as mean ± S.E.M. N = 3.DOI: http://dx.doi.org/10.7554/eLife.23588.00910.7554/eLife.23588.010Figure 4—figure supplement 2—source data 1.DOI: http://dx.doi.org/10.7554/eLife.23588.010

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Total RNA was isolated from whole embryos injected with Pou3f2-targeted morpholino (Pou3f2-Mo) or a mismatch (Ctrl-Mo). Real-time PCR showed that Pou3f2 KD impaired significantly the expression of Fli1 and Kdr. All data represented as mean ± S.E.M. N = 3. Student t-test, *p=0.01; **p=0.001.DOI: http://dx.doi.org/10.7554/eLife.23588.011

## Role of Pou3f2 in human EC differentiation

To determine the role of Pou3f2 during endothelial differentiation from human iPSC, we examined the expression of Pou3f2 in the heterokaryon system consisting of hiPSCs and murine endothelial cells (

![Figure 5.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig5-v2.jpg)

**Figure 5.:** (a) Gene expression pattern of Pou3f2 in heterokaryons consisting of hiPSC and mEC compared to co-culture control. (b) Validation of expression of Pou3f2 during differentiation of hiPSC into endothelial lineage. (c) Expression of Pou3f2 in lentiviral mediated shRNA KD of Pou3f2 in hiPSC following differentiation into endothelial phenotype compared to Control shRNA group. (d) Representative images of Western blots showing the KD effects of Pou3f2 in hiPSC during endothelial differentiation, the same results were obtained at least three times. (e–j) Pou3f2 KD reduced the gene expression of endothelial markers including Kdr, Tie2, Cdh5, Pecam1, Nos3 and Vwf following endothelial differentiation of hiPSC. All data represented as mean ± S.E.M. (n = 3). p<0.05 vs co-culture control or control shRNA group.DOI: http://dx.doi.org/10.7554/eLife.23588.012

Next, we assessed the effects of shRNA-mediated KD of Pou3f2 on differentiation of endothelial cells from human iPSC. Pou3f2

![Figure 6.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig6-v2.jpg)

**Figure 6.:** (a–c) Representative FACS plots and summarized diagram showing Pou3f2 KD reduced iPSC-EC generation compared to scrambled control. (d) Representative immunofluorescence images revealed lower expression of CD31, CD144 and Vwf in Pou3f2 KD iPSC-ECs. (e) The iPSC-ECs generated from Pou3f2 KD cells manifested poor formation of networks of tubular structures on matrigel. (f) The ability of Pou3f2 KD iPSC-ECs to produce nitric oxide in response to calcium ionophore A23187 was significantly reduced compared to scrambled control iPSC-ECs. (g) Reduced capacity in taking up AcLDL in Pou3f2 KD iPSC-ECs compared to scrambled control iPSC-ECs. (h) Reduced gene expression of endothelial markers including Kdr, Tie2, Nos3, CD31, Cdh5 and Vwf in Pou3f2 KD human iPSC-ECs. (i) Arterial markers (Notch4, Efnb2, Hey2) but not venous (Ephb4 and Coup-TFII) nor lymphatic markers (Pdpn and Lyve1) were affected in Pou3f2 KD iPSC-ECs compared to scrambled control iPSC-ECs. All data represented as mean ± S.E.M. (n = 3). p<0.05 vs Control shRNA group.DOI: http://dx.doi.org/10.7554/eLife.23588.013

## Pou3f2 interacts with known endothelial promoters

To determine if Pou3f2 binds to the promoters of endothelial-related transcription factors, we performed ChIP-PCR. We observed that during differentiation of iPSCs to ECs, the binding of Pou3f2 to the promoters of endothelial related transcription factors including Ets1, Lmo2, Hey1 and Hey2 (

![Figure 7.](https://cdn.elifesciences.org/articles/23588/elife-23588-fig7-v2.jpg)

**Figure 7.:** (a–d) Binding of Pou3f2 to the promoters of endothelial-related transcription factors including Ets1, Lmo2, Hey1 and Hey2 was significantly inhibited in Pou3f2 KD cells compared to scrambled control at Day 8 of endothelial differentiation protocol, without affecting the control promoter RPL30 Exon 3 (e). (f–i) Downregulation of gene expression of Ets1, Lmo2, Hey1 and Hey2 in Pou3f2 KD cells during differentiation into endothelial lineage. (j) Rescue experiments with modified mRNA encoding Pou3f2 improved CD31+CD144+ cell generation from Pou3f2 KD cells. All data represented as mean ± S.E.M. (n = 3). p<0.05 vs co-culture control or control shRNA group.DOI: http://dx.doi.org/10.7554/eLife.23588.014

## Discussion

Our current understanding of the genetic and epigenetic processes governing endothelial development and differentiation is limited. We lack comprehensive knowledge regarding all endothelial lineage factors and have sparse information regarding the magnitude and temporal sequence of their expression. In this paper, we find that the bi-species heterokaryons combined with RNAseq can provide new insights into determinants of endothelial lineage. Our work suggests that transcription factors and epigenetic machinery which actively maintain endothelial phenotype can also act on the pluripotent cell nucleus to recapitulate ontogeny. This system is likely to generate useful insights to improve the yield and fidelity of reprogramming to endothelial phenotype. A tangible and immediate outcome of this line of inquiry will be a more complete knowledge of the hierarchy of genes regulating differentiation to the EC lineage. Insights into these processes will be of general interest to investigators of vascular differentiation and development and may lead to new therapeutic targets for endothelial regeneration and the treatment of vascular diseases.

Finally, and perhaps most importantly, this model system should be amenable to discovery of novel determinants of other cell lineages. We believe that our studies provide proof-of-concept for using bi-species heterokaryon technology as a tool to elucidate novel genes regulating differentiation to any somatic cell. Our work opens a new vista of exploration for the broader community of scientists working in tissue regeneration, development, differentiation and the therapeutic applications of these insights.

## Materials and methods

## Cell culture

Human-induced progenitor stem cells (Takara Bio USA, Mountain View, CA) line authentication was achieved by genetic profiling using polymorphic short tandem repeat (STR profiling) loci. Our cell cultures were tested weekly for mycoplasma by real-time PCR approach and were mycoplasma-free. HiPSC lines were generated using retroviral factors encoding Oct4, Sox2, Cmyc and Klf4 in adult dermal fibroblasts. The hiPSCs were characterized for their pluripotency using PCR and IHC for known pluripotency markers, and were maintained in mTeSR1 (Stem Cell Technology, Vancouver, Canada). Murine ESCs (D3, ATCC, Manassus, VA) of the SV129 strain were cultured on gelatin-coated dish and maintained in ESGRO media plus GSK3β inhibitors. Human microvascular endothelial cells (HMVECs) (obtained from Lonza, Walkersville, MD) and murine endothelial cells (obtained from Applied Stemcell, Menlo Park, CA) were cultured in EC growth medium EGM-2 MV (cc-3162). Cells were used for all experiments at passage 6–8.

## Heterokaryon formation and isolation

One day before cell fusion, 4 × 105 endothelial cells were seeded on one well of a 6-well dish. The endothelial cells were confluent on the day of cell fusion. On the same day, 1 hr prior to cell fusion, the endothelial cell medium was replaced with fresh EGM-2 MV medium supplemented with 1 μM Cell Tracker Red, then cells were incubated at 37°C in darkness for 30 min. Human iPSCs or murine ESCs labeled by transduction with retroviruses encoding GFP were rinsed with PBS followed by accutase treatment at 37°C for 5 min to dissociate the pluripotent stem cells into single-cell suspension. The cells were then collected in conical tubes after neutralization by MEF media containing 10% FBS. The cells were then counted with hemocytometer and 2 × 105 pluripotent stem cells were taken. The cells were then centrifuged at 200 x g for 5 min at 4°C, the supernatant was removed, and the cell pellet was resuspended in 25 μL ice-cold cell fusion buffer with 2.5 μL ice-cold HVJ-envelope fusagen. The reaction mixture was placed on ice for 5 min with regular agitation in 2.5 min apart. After 5 min, the cells were centrifuged again and the supernatant was discarded and 2 ml cell fusion buffer was added. The pluripotent cells were then plated onto the endothelial cells. The six-well dish was then centrifuged at 200 g for 5 min at 4°C. After centrifugation the dish was placed into a 37°C incubator to induce cell fusion. Twenty minutes later, the medium was removed and EGM-2 MV medium was added. For the Co-culture Control, the described procedure was the same except HVJ-enveloped fusagen was not added. The heterokaryons (double-positive cells) can be efficiently sorted by FACS. Heterokaryons (GFP+ and CellTracker Red+) were harvested by FACS at 6, 12, 24, 48 and 72 hr post-fusion.

## Preparation of RNA-seq libraries and sequencing

The species-specific nucleotide differences between the mouse and human transcripts enable us to differentiate between reads of transcripts from the murine ESC versus those from the human EC when the sequences are aligned to their respective genomes. Heterokaryons (GFP+ and CellTracker Red+) were harvested by FACS at 6, 12 and 24 hr post-fusion and prepared for analysis by RNA-seq. Total RNA from heterokaryons were isolated. Human and mouse mRNA transcripts were isolated from the total RNA samples using polyA-based enrichment using oligo-dT magnetic beads. The majority of contaminating ribosomal RNA was eliminated by this approach. The resulting mRNA was fragmented, reverse transcribed to cDNA, ligated to adapters, and subject to brief PCR amplification in preparation of the Illumina library. The integrity and quality of RNA and complementary DNA were monitored using an Agilent Bioanalyzer 2100. The samples were sequenced using pair-end 100 base-pair reads. For the estimation of gene expression and data analysis, any remaining ribosomal reads were discarded, and the resulting murine and human transcripts were mapped to their respective genomes. Reads that map to both transcriptomes would be discarded and the RPKMs adjusted accordingly (discarded reads represent only 5% of the total reads; furthermore, virtually all genes have at least one unique read that is different between species, so that no gene is completely discarded).

## RNA-seq read mapping and gene expression

RNA-Seq reads were aligned to the mouse genome version mm9 using TopHat version 2.1.0. We use the full set of knownGene downloaded from the UCSC Genome browser (http://genome.ucsc.edu/cgi-bin/hgTables) as reference genes. RNA-Seq read counts for each gene in each sample was calculated using Cuffdiff function in Cufflinks version 2.2.1. The Cuffdiff also calculates fragment per kilobase per million reads (FPKM) for each gene. We further subject the reads counts to EdgeR version 3.12.0 for differential expression analysis, and define differential genes based on false discovery rate (FDR) cutoff 1e-5. We subject interesting gene groups to the DAVID website (https://david.ncifcrf.gov) for functional enrichment analysis. Enriched functional terms were defined based on Benjamini adjusted p value cut-off 0.05. Hierarchical clustering of gene expression heatmap was conducted using MEV based on Pearson correlation distance metric and the average linkage method.

## RNA extraction and quantitative PCR

Using RNeasy Mini Kit (Qiagen, Chatsworth, CA), total RNA was extracted. The Quantitect reverse transcription kit (Qiagen) was used to generate cDNA and SYBR Green PCR kit (Invitrogen, Carlsbad, CA) was used for real-time qPCR with the QuantStudio 12 k Flex system (Applied Biosystems, Foster City, CA) following the manufacturer’s instructions. Genes were analyzed with the data normalized to Gapdh and expressed as relative fold changes using the ΔCt method of analysis.

## Endothelial differentiation protocol

Murine ESC-EC Differentiation: Endothelial differentiation of ESCs was carried out using the suspension culture approach with modifications. To initiate differentiation, ESCs were cultured in ultralow nonadhesive dishes to form embryoid body aggregates in a differentiation medium that consisted of α-Minimum Eagle’s Medium, 10% FBS, 1% penicillin/streptomycin, and 0.05 mmol/L β-mercaptoethanol (Sigma, St Louis, MO). After 4 days of suspension culture, the embryoid bodies were reattached onto 0.2% gelatin-coated dishes and cultured in differentiation medium. After 3 weeks of differentiation, the cells were purified by fluorescence-activated cell sorting (FACS) using anti-mouse vascular endothelial cadherin (VE-cadherin) antibody (Ab) (BD Biosciences, Bedford, CA).

Human iPSC-EC differentiation: Confluent cultures of hiPSCs were incubated with 1 mg/ml type IV collagenase for 10 min and transferred to ultra low attachment dishes containing differentiation media for 4 days to form embryoid bodies (EBs). The differentiation media used consisted of α-Minimum Eagle’s Medium, 20% fetal bovine serum, L-glutamine, β-mercaptoethanol (0.05 mmol/L) and 1% non-essential amino acids supplemented with bone morphogenetic protein-4 (BMP-4, 50 ng/ml, Peprotech) and vascular endothelial growth factor (VEGF-A, 50 ng/ml, Peprotech). The four-day EBs were reattached to gelatin-coated dishes in the presence of VEGF-A for another 10 days before purification.

## Fluorescence-activated cell sorting (FACS)

ECs derived from pluripotent stem cells were purified using FACS. Cells were dissociated into single cells with Accutase (Invitrogen) for 5 min at 37°C, washed with 1x PBS containing 5% BSA and passed through a 70-μm cell strainer. Cells were then incubated with either Alexa Fluor 488-conjugated CD31 antibody (BD Bioscience, San jose, CA) or PE-conjugated CD144 antibody (BD Bioscience) for 30 min. Isotype-matched antibody served as negative control. The purified ESC- or iPSC-ECs were expanded in EGM-2 media.

## Immunofluorescent imaging

Human iPSC-ECs were fixed with 4% paraformaldehyde, permeabilized with 0.1% Triton X-100, blocked with 1% normal goat serum and stained for anti-human CD31 (R and D Systems), anti-human CD144 (R &D Systems, Minneapolis, MN), anti-human von Willebrand factor (vWF, Abcam, Cambridge, UK) overnight at 4°C. After washes with PBS, the cells were treated with Alexa Fluor-488 or -594 secondary antibodies. Cell nuclei were stained with Hoechst 33342 (Sigma). Images were acquired on a confocal microscope (FV1000-IX81, Olympus, Tokyo, Japan).

## Western blotting

Cells were homogenized with ice-cold RIPA lysis buffer containing 1 µg/mL leupeptin, 5 µg/mL aprotonin, 100 µg/mL PMSF, 1 mmol/L sodium orthovanadate, 1 mmol/L EDTA, 1 mmol/L EGTA, 1 mmol/L sodium fluoride and 2 µg/mL β-glycerolphosphate. The protein concentration was determined by Bradford method and aliquots of 20 µg of the total proteins were separated on 10% SDS-poly-acrylamide gel. Proteins were then transferred to immobilon-P polyvinylidene difluoride (PVDF) membrane (Millipore, Billerica, MA). Membranes were blocked with 5% non-fat milk in TBS-T and subsequently exposed to Pou3f2 primary antibody (Genetex, Irvine, CA) followed by HRP-conjugated secondary antibody and developed by chemiluminescence.

## Functional assays

Uptake of Ac-LDL: was evaluated by incubating cells with ac-LDL-594 at 1:200 dilution for 5 hr before washing the cells with PBS and then measuring the mean fluorescence of the cells. Endothelial network formation,the ability of cells to form tube-like structures, was assessed in vitro by seeding 1.2 × 105 cells in wells coated with matrigel in the presence of EGM-2 media containing 50 ng/ml VEGF and incubated for 24 hr.

## Nitric oxide production

The ability of the cells to produce NO was assessed by measuring the concentration of NO in the culture medium using the NO detection kit (Molecular Probe, Carlsbad, CA) according to the manufacturer’s instructions. The amount of nitrate was determined by converting it to nitrite, followed by the colorimetric determination of the total concentration of nitrite as a colored azo dye product of the Griess reaction that absorbed visible light at 540 nm using a microplate reader.

## Chromatin immunoprecipitation and ChIP-qPCR

hiPSCs were differentiated towards EC lineage and collected at Day 8. Samples were prepared by SimpleChIP enzymatic chromatin IP kit (Cell Signaling Technology). Chromatin immunoprecipitation was performed using human Pou3f2 antibody (Genetex), rabbit IgG (CST), histone H3 antibody (CST). DNA was purified using Nucleospin PCR clean-up kit (Macherey-Nagel, Bethlehem, PA) and used for quantitative PCR with primers against regions predicted within the promoter of Ets1, Lmo2, Hey1 and Hey2. Recovery of genomic DNA as the percentage input was calculated as the ratio of copy numbers in the immunoprecipitate to the input control.

## Zebrafish aquaculture and husbandry

Adult zebrafish (wild-type Wik and tg(fli1:EGFP)y1 strains) were acquired from the Zebrafish International Resource Center and raised according to standard procedures and kept at 28°C under a 14/10 hr light/dark cycle and fed with dry meal (Gemma Micro, Westbrook, ME) twice per day. Embryos used in these studies were obtained by natural matings and cultured in E3 embryo medium at 28.5°C. Animals were housed and all experiments were carried out in accordance with the recommendations of the Institutional Animal Care and Use Committee. All surgery procedures were performed under anesthesia with Tricaine 0.02 mg/ml.

## Morpholinos and caged morpholinos injections

Pou3f2 KD in zebrafish was achieved using two different antisense morpholinos (Gene Tools, Oregon) targeting the Pou3f2 mRNA AUG translational start site with sequence: (Mo1) 5’-ATGATTGGATGCTGTAGTCGCCATG-3’, and (Mo2) 5’-CGGACTGATCGCTCCTATTAAAGGA-3’. As one control we used a 5-base pair mismatch MO: sequence 5’-ATcATTcGATcCTGTAcTCcCCATG-3’. To decipher the roles of Pou3f2 transcription factor in specific stages of endothelial development, we used Pou3f2-targeted caged morpholino (cMOs) (Shestopalov et al., 2007). This chemically modified morpholino allowed temporal gene silencing by using targeted UV illumination. An optimized dose of 0.5 ng/eggs (0.5 nL bolus) of Pou3f2 targeted morpholino was injected in each embryo at 1–2 cell stage, just below the cell mass.

## cMOs photoactivation

To photoactivate the cMOs, injected zebrafish embryos were arrayed in an agarose microinjection template (560 μm x 960 μm wells), with the animal pole facing the light source. Then, the mercury lamp light was focused onto individual embryos for 10 s, using a Leica DM4500B epifluorescence microscope equipped with an A4 filtercube (Ex: 360 nm, 40 nm bandpass) and a 20 x/0.5 NA water-immersion objective. Individual embryos were irradiated at 6 or 24 hr post-fertilization.

## Morpholino phenotype rescue by modified mRNA

As control, we also performed rescue experiments by co-injecting Pou3f2-targeted MO together with Pou3f2 modified mRNA into one-cell-stage embryos. The Pou3f2 modified mRNA version used, produced from the RNA Core available in our Institute, was modified at the 5′ untranslated region so that it was not recognized by the morpholino. An optimized dose of 300 pg was co-injected with the morpholino in rescue experiments.

## Zebrafish imaging

The embryos were manually dechorionated at 24 or 48 hpf. Brightfield images were acquired using a Leica M205FA fluorescence stereoscope equipped with a Leica DFC500 digital camera. For immunofluorescence imaging, bright-field images of embryos were obtained with a Leica DM4500B compound microscope equipped with a 20 x/0.12 NA water-immersion objectives and a QImaging Retiga-SRV digital camera. Fluorescence images were obtained with the DM4500B/Retiga-SRV system equipped with a mercury lamp and GFP (Ex: 470 nm, 40 nm bandpass; Em: 525 nm, 50 nm bandpass) filter sets.

## Western blot analysis of Pou3f2 in zebrafish

The embryos were de-yolked in TM1 buffer (100 mM NaCl, 5 mM KCl, 5 mM HEPES pH 7.0, 1% (w/v) PEG-200,000). Twenty de-yolked embryos from each experimental condition were homogenized in SDS-PAGE loading buffer (50 μH 7.0, 1% (w/mM 2-mercaptoethanol, 4% (w/v) glycerol, 100 mM DTT, 100 mM Tris-HCl, pH 6.8), vortexed, and heated to 95°C for 5 min. The resulting lysates were used for gel electrophoresis followed by blotting with Pou3f2 antibody (rabbit polyclonal, Abcam 137469). β-Tubulin (rabbit polyclonal, Abcam 6046) was used as loading control.

## In situ hybridization in zebrafish

The preparation of sense (used as control) and antisense RNA probes for Kdr and Fli1 and in situ hybridization procedure were performed according to Thisse and Thisse (Thisse and Thisse, 2008).

## FACS-based analysis of GFP+ cell from zebrafish

Cells were isolated according to Shestopalov et al. (Shestopalov et al., 2012) with modifications. Briefly, Tg(fli1:EGFP)y1 embryos at the appropriate developmental stage were dechorionated, transferred in an eppendorf tube with calcium-free Ringer’s solution (200 μl for 25–30 embryos; 116 mM NaCl, 2.6 mM KCl, 5 mM HEPES, pH 7.0) and dissociated with a 200 μl pipette tip. Then 1 ml solution of 1X PBS containing trypsin (0.25%, Gibco), 50 μg collagenase P (Roche, Indianapolis, IN) and 1 mM EDTA was added and samples were incubated for 30 min at 28.5°C with further pipetting every 5 min. Enzymatic processing was quenched with stop solution (200 μl; 1X PBS containing 30% (v/v) calf serum and 10 mM CaCl2), and cells were collected by centrifugation (400 g, 5 min, 4°C). After aspirating the supernatant, cells were resuspended in a chilled solution of DMEM containing 1% (v/v) calf serum, 0.8 mM CaCl2, 50 V ml−1 penicillin/streptomycin, centrifuged and resuspended in the same medium. The cell suspension was filtered through a 40 μm cell strainer (BD Biosciences) into FACS sample tubes. Cell suspensions were analyzed using a BD FACSAria. Wild-type zebrafish (Wik) was used as GFP negative control. Viable fluorescent single cells were identified as DAPI-negative. Cells viability was confirmed under fluorescence stereomicroscope (Leica M205) by using a Neubauer chamber.

## Data access

All RNA-Seq data have been deposited to the GEO database by the accession number GSE84558.

## Statistical analyses

Statistical analysis was performed with SPSS software (SPSS Inc., Chicago, IL, USA). Results were expressed as mean ± SEM. The Shapiro-Wilk test was used to confirm the null hypothesis that the data follow a normal distribution. Statistical comparisons were performed via Student t-test for two groups and via one-way ANOVA test for multiple groups. Bonferroni corrections test was applied for multiple comparisons. p<0.05 was considered significant.

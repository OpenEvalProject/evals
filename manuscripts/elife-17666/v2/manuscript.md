# Dissecting the pre-placodal transcriptome to reveal presumptive direct targets of Six1 and Eya1 in cranial placodes

## Authors

- Nick Riddiford<sup>1</sup> ([ORCID: 0000-0002-4739-4233](https://orcid.org/0000-0002-4739-4233))
- Gerhard Schlosser<sup>1</sup> ([ORCID: 0000-0002-1300-1331](https://orcid.org/0000-0002-1300-1331)) †

### Affiliations

1. School of Natural Sciences National University of Ireland Galway Ireland
2. Regenerative Medicine Institute (REMEDI) National University of Ireland Galway Ireland

† Corresponding author

## Abstract

The pre-placodal ectoderm, marked by the expression of the transcription factor Six1 and its co-activator Eya1, develops into placodes and ultimately into many cranial sensory organs and ganglia. Using RNA-Seq in Xenopus laevis we screened for presumptive direct placodal target genes of Six1 and Eya1 by overexpressing hormone-inducible constructs of Six1 and Eya1 in pre-placodal explants, and blocking protein synthesis before hormone-inducing nuclear translocation of Six1 or Eya1. Comparing the transcriptome of explants with non-induced controls, we identified hundreds of novel Six1/Eya1 target genes with potentially important roles for placode development. Loss-of-function studies confirmed that target genes encoding known transcriptional regulators of progenitor fates (e.g. Sox2, Hes8) and neuronal/sensory differentiation (e.g. Ngn1, Atoh1, Pou4f1, Gfi1) require Six1 and Eya1 for their placodal expression. Our findings provide insights into the gene regulatory network regulating placodal neurogenesis downstream of Six1 and Eya1 suggesting new avenues of research into placode development and disease.

## Introduction

The cranial placodes give rise to many sense organs of the vertebrate head (including nose, ear and lateral line) and contribute to the anterior pituitary and sensory ganglia of the cranial nerves. Together with the neural crest, which also contributes to cranial ganglia as well as the head skeleton, they originated as an evolutionary novelty in stem vertebrates, on the adoption of a more active and exploratory life style (Northcutt and Gans, 1983; Schlosser, 2015). Defects in placode development underlie many congenital diseases of sensory organs and the endocrine system (Petit et al., 2001; Davis et al., 2013; Xu, 2013), however, despite this central importance of placodes in the evolution and development of the vertebrate head, they have been much less well studied than the neural crest, and little is known about the gene regulatory networks (GRNs) driving early placode development.

Fate mapping studies have shown that all cranial placodes develop from a common precursor region, the pre-placodal ectoderm (PPE) (Streit, 2002; Bhattacharyya et al., 2004; Xu et al., 2008; Pieper et al., 2011). In neural plate stage embryos, the PPE is located as a horseshoe-shaped domain around the anterior neural plate (and abutting the cranial neural crest laterally) which subsequently breaks up into individual placodes (Schlosser, 2010; Grocott et al., 2012; Saint-Jeannet and Moody, 2014). Molecularly, the PPE is characterised by the expression of Six1 and Eya1, which also continues in most placodes derived from the PPE (Schlosser and Ahrens, 2004). Whereas Six1 encodes a transcription factor, Eya1 encodes a transcriptional co-activator that also has phosphatase activity (Kumar, 2009; Tadjuidje and Hegde, 2013), and Six1 and Eya1 have been shown to form a protein complex and synergistically activate transcription (Ohto et al., 1999; Li et al., 2013). However, both Six1 and Eya1 also interact with other protein interaction partners; Six1, for example, has been shown to act as a transcriptional repressor after binding to the co-repressor Groucho (Brugmann et al., 2004) whereas Eya1 is known to form protein complexes with other binding partners including the transcription factor Sox2 (Ahmed et al., 2012a; Tadjuidje and Hegde, 2013).

Loss of Six1 or Eya1 function in mouse, zebrafish, chick or Xenopus embryos leads to a similar spectrum of PPE and placodal defects, with altered expression of other PPE genes, decreased proliferation and increased apoptosis in many placodes, compromised morphogenetic movements (invagination or cell delamination) and a decreased production of sensory cells and neurons (Xu et al., 1999; Laclef et al., 2003; Zheng et al., 2003; Brugmann et al., 2004; Zou et al., 2004; Kozlowski et al., 2005; Schlosser et al., 2008; Christophorou et al., 2009; Ahmed et al., 2012a, 2012b). In human patients, mutations in both Six1 and Eya1 lead to branchio-oto-renal (BOR) and branchio-otic (BO) syndromes with congenital hearing loss (Kochhar et al., 2007). These findings suggest that these proteins are core regulators of placode development and promote multiple aspects of placode development synergistically, although Eya1-independent roles of Six1 have also been reported (Brugmann et al., 2004; Bricaud and Collazo, 2011). Specifically, Six1 and Eya1 have been shown to play central roles, during multiple steps, in the development of sensory cells (e.g. hair cells in the inner ear) as well as sensory neurons, and promote both the proliferation of sensory/neuronal progenitors as well as sensory and neuronal differentiation in a dosage dependent fashion (Zou et al., 2004; Schlosser et al., 2008; Zou et al., 2008; Ahmed et al., 2012b, 2012a). Recently Atoh1, an essential determination gene for hair cell development, has been shown to be directly transcriptionally activated by Six1/Eya1 binding to its enhancer (Ahmed et al., 2012a). Moreover, the neuronal progenitor genes Sox2 and Sox3 have been shown to be up-regulated by Six1 and Eya1 in the absence of protein synthesis, suggesting that they are also direct target genes (Schlosser et al., 2008). Several other direct target genes of Six1 have been identified (Kumar, 2009; Xu, 2013), but no specific screen for direct target genes of Six1 and Eya1 in the PPE and the developing placodes has yet been conducted.

Here, using RNA-Seq in Xenopus laevis, we present the first comprehensive screen for presumptive direct target genes of Six1 and Eya1 in the developing placodes in any vertebrate. Hormone-inducible constructs of Six1 and Eya1 (fused with the human glucocorticoid receptor [GR]) were overexpressed, either alone or in combination, in Xenopus embryos. We then explanted the PPE at neural fold stages and activated nuclear translocation of Six1 or Eya1 in these explants by the addition of dexamethasone (DEX) after blocking protein synthesis by cycloheximide (CHX). This approach has previously been shown to reliably activate direct targets of GR-fusion constructs only in the presence of DEX (Kolm and Sive, 1995; Seo et al., 2007). We then analysed the transcriptome of placodal explants by RNA-Seq and compared this to control explants which were not hormone induced, in order to specifically survey target genes directly activated or repressed by Six1 or Eya1 in the PPE and developing placodes. Using this method, we were able to identify a large number of novel target genes with potentially important roles for cranial placode development. We were further able to show in loss of function studies that several target genes encoding known regulators of progenitor fates (e.g. Sox2, Hes8) and neuronal/sensory differentiation (e.g. Ngn1, Atoh1, Pou4f1.2, Gfi1a) required both Six1 and Eya1 for their expression in the developing placodes. Our findings provide pioneering insights into the GRNs regulating placode development downstream of Six1 and Eya1, and suggest exciting new avenues of research for understanding placode development and disease.

## Results

### The pre-placodal transcriptome

RNA was extracted from explants cut from the PPE of un-injected embryos and characterised using RNA-Seq to provide a complete transcriptome of the PPE. After removing genes expressed at low levels (FPKM < 1) and annotation against a Xenopus mRNA database (see Materials and methods), we assembled a transcriptome comprising 15,794 transcripts, and the top 1000 expressed genes are shown in Supplementary file 1. Gene Set Enrichment Analysis (GSEA) on these genes revealed that RNA processing/splicing was very highly enriched in the PPE transcriptome (enrichment score [E]: 43), suggesting that RNA-binding proteins and mRNA splicing mechanisms may play an important role in placodal development as has also been reported for the neural crest (Simões-Costa et al., 2014). Translation elongation and ribosomal proteins were also highly enriched (E: 32), perhaps reflecting the high rate of protein turnover in the rapidly changing PPE (McCabe et al., 2004).

### Identification of direct targets of Six1 and Eya1 in PPE

To identify presumptive direct targets of Six1 and Eya1, Six1-GR and Eya1-GR fusion proteins were overexpressed either alone or together in the PPE. In combination with a protein synthesis inhibitor (CHX), nuclear translocation of Six1 and Eya1 was induced by adding DEX for 2.5 hr, and gene expression was analysed using RNA-Seq (Figure 1). Presumptive direct targets of Six1 and Eya1 were determined by comparing Six1-GR-, Eya1-GR- or Six1-GR+Eya1-GR-injected embryos treated with CHX alone (as controls) against CHX+DEX-treated samples. Resultant data sets from such individual treatment groups (each with two biological replicates) are henceforth referred to as Six1i, Eya1i and Six1+Eya1i. In this paradigm, the expression of target genes for which either Six1 or Eya1 concentrations are limiting in the PPE should be affected in Six1i and Eya1i treatment groups, respectively (and potentially also in Six1+Eya1i), while the expression of target genes limited by both Eya1 and Six1 concentrations in the PPE should be modulated only in the Six1+Eya1i treatment group.

![Figure 1.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig1-v2.jpg)

**Figure 1.:** (A) Both blastomeres of two-cell stage embryos were injected with Six1-GR, Eya1-GR or Six1-GR+Eya1-GR and explants were cut from pre-placodal ectoderm. Explants were incubated in CHX for 30 min before being split into two groups; 50% were kept in CHX for 2.5 hr and 50% were transferred to CHX+DEX for 2.5 hr. RNA was extracted from both treatment groups and submitted to RNA-Sequencing. (B) On average, 80 million reads were generated in sequencing for each treatment group, and 65 million quality-trimmed reads were successfully mapped to the Xenopus genome. An average of 49,000 transcript models were assembled, of which 80% (39,000) were successfully annotated against a Xenopus mRNA database. Annotated transcript models were then filtered to condense duplicate annotations into 15,794 uniquely annotated transcript models, and differential expression analysis was then performed using CHX treated explants as a control for those treated with CHX+DEX.

Using this approach, we identified 365 genes up-regulated at least twofold that satisfied all criteria for differential expression (log2 fold change [FC] ≥ 1; FPKM ≥ 1; FC < 0.5 in un-injected control) in Six1i, 508 in Eya1i and 836 in Six1+Eya1i, treatment groups, while 292 genes were down-regulated in Six1i, 218 in Eya1i and 490 in Six1+Eya1i treatment groups (Figure 2A and B; Supplementary file 2). As an initial means of estimating data quality, we searched for targets of Six1 established in previous studies (Atoh1 (Ahmed et al., 2012a); Slc12a2 (Ando et al., 2005); CyclinA1 (Coletta et al., 2004); CyclinD1 (Li et al., 2013); c-Myc (Li et al., 2003); Ezrin (Yu et al., 2006); Gdnf (Li et al., 2003); Sox3 (Schlosser et al., 2008); Sox2 (Schlosser et al., 2008); Sall1 (Chai et al., 2006); and MyoD1 (Liu et al., 2013)) in the Six1i and Six1+Eya1i data sets. With the exception of c-Myc, all genes were present in the transcriptome, and most were found in either Six1i (CyclinD1 [ccndx] FC: 7.48; Slc12a2, FC: -2.75; CyclinA1, FC: -3.68; Sox2, FC: 1.2; MyoD, FC: 3.4) or Six1+Eya1i (Sox3, FC: 0.9; Atoh1, FC: 1.4; Sall1, FC: 0.99) data sets, confirming the utility of our approach in identifying direct targets. Moreover, Atoh1, Sox2 and MyoD1 were found both in our Six1+Eya1i and Eya1i datasets as expected based on the known coregulation of these Six1 target genes by Eya1 (Ahmed et al., 2012a; Grifone et al., 2007; Schlosser et al., 2008). We suggest that overexpression of Eya1 alone may upregulate such genes in those parts of the ectoderm where Six1 is already expressed at high levels but Eya1 at relatively low levels in vivo.

![Figure 2.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig2-v2.jpg)

**Figure 2.:** Plots A and B show number of genes differentially regulated after overexpression of Six1 alone (Six1i; yellow), Eya1 alone (Eya1i; blue) or Six1 and Eya1 combined (Six1+Eya1i; green). Each Venn diagram shows the number of genes (red) unique for each treatment group or shared between them. (A) Number of genes up-regulated and (B) down-regulated after injection with Six1, Eya1 or Six1+Eya1. (C) The merged analysis resulted in hundreds of significantly differentially expressed genes in the PPE data set. Plot shows log2 transformed (FPKM+1) values after overexpression of Six1 or Eya1 (combination of all treatment groups; Six1+Eya1m). Green points represent significantly (q<0.05) up-regulated genes and red points show significantly down-regulated genes. Plot D shows the enrichment of molecular function terms after overexpression of Six1 or Eya1 based on significantly differentially expressed genes from the merged data set (Six1+Eya1m; Supplementary file 3, Table 5). The area of the pie represents the total number of functional terms contained in the analysis, with each slice representing the percentage of genes against this total. Molecular functions shown can be broadly divided into five categories: Green slices are related to binding functions (53%); purple/blue represents enzyme activity (30%); pink/red shows transmembrane proteins (13%); orange cytoskeleton (3%) and yellow anti-oxidant (1%).

### Six1 and Eya1 co-regulate many but not all PPE target genes

Comparison between our different treatment groups allows us to distinguish genes likely co-regulated by Six1 and Eya1 from those that are not and, thus, may be regulated by Six1 or Eya1 alone or in conjunction with other protein-binding partners. Since ectodermal expression of Six1 and Eya1 is widely overlapping in vivo but not completely congruent, genes co-regulated by Six1 and Eya1 may be differentially expressed not only after coinjection of Six1 and Eya1 (Six1+Eya1i treatment group) but also after injection of Six1 or Eya1 alone (Six1i and Eya1i treatment groups, respectively) because elevation of Six1 or Eya1 levels will produce higher levels of the coregulatory complex in those parts of the ectoderm where the respective protein is expressed at much lower levels than its binding partner. Hence, a subset of target genes with high response thresholds to the Six1-Eya1 coregulatory complex (e.g. due to low affinity binding sites) will respond to overexpression of Six1 or Eya1 alone with differential expression in these parts of the ectoderm while another subset of genes with low response thresholds (e.g. due to high affinity binding sites) will not. The latter subset will, thus, only be differentially expressed after overexpression of both Six1 and Eya1, creating expanded areas of Six1 and Eya1 coexpression in the ectoderm. Notably, the false discovery rate is expected to be lower for the former subset, which is supported by three independent treatment groups (Six1i, Eya1i and Six1+Eya1i), than in the latter subset, supported only by one (Six1+Eya1i).

About half of all genes differentially expressed in the PPE in our various treatment groups show evidence of co-regulation by Six1 and Eya1. This includes 690 (633+57) up-regulated and 444 (440+4) down-regulated genes (Figure 2A and B). Indeed, the top 10% of transcripts (ranked by FC; post DEX-filtering) up-regulated in Six1i, Eya1i or Six+Eya1i treatment groups were each highly enriched for the top 10% of transcripts up-regulated in any of the other experimental treatment groups (p<0.0001; Fisher’s exact test). More genes co-regulated by Six1 and Eya1 were up-regulated than were down-regulated (690/1134 = 60.8% for all co-regulated genes, 57/61 = 93.4% for co-regulated genes identified in each treatment group; Figure 2A and B), corroborating previous findings that Six1 and Eya1 typically act synergistically to activate transcription (Ahmed et al., 2012b, 2012a; Brugmann et al., 2004; Christophorou et al., 2009; Li et al., 2003; Ruf et al., 2004). However, our identification of a subset of genes synergistically down-regulated by Six1 and Eya1 suggests that Eya1 may not always act as a co-activator of Six1.

In contrast, there is no support for co-regulation for genes that are differentially expressed only in Six1i but not Eya1i treatment groups (and vice versa) even for those genes that are also differentially expressed after Six1+Eya1i treatment. We identified 283 (190+93) genes up-regulated and 270 (233+37) genes down-regulated by Six1 but not Eya1, indicating that these are regulated by Six1 in an Eya1 independent way but possibly dependent on other co-factors. Conversely, we identified 426 (373+53) genes up-regulated and 196 (187+9) genes down-regulated by Eya1 but not Six1 (Figure 2A,B) suggesting that these are regulated by Eya1 in conjunction with transcription factors other than Six1.

To add statistical power to our analysis, we next merged treatment groups and determined significantly differentially expressed genes (q<0.05) in these merged groups. We first created a data set Six1+Eya1m in which all replicates that involved overexpression of either Six1 or Eya1 were considered as equivalent (injection of Six1-GR, Eya1-GR or Six1-GR+Eya1-GR; 6 replicates in total). This allowed us to identify genes that are significantly differentially expressed across all treatment groups. We also created a data set Six1m, in which all replicates that involved Six1 overexpression were considered as equivalent (injection of Six1-GR or Six1-GR+Eya1-GR; 4 replicates). This allowed us to identify genes with significant differential expression after Six1 upregulation. Similarly, we created data set Eya1m based on all replicates that involved Eya1 overexpression (injection of Eya1-GR or Six1-GR+Eya1-GR; 4 replicates) allowing us to identify genes differentially expressed after Eya1 upregulation. We found 181 significantly (q<0.05) up-regulated genes in the Six1+Eya1m group, 149 in Six1m and 112 in Eya1m (Supplementary file 3, Tables 1–3). Substantially fewer genes were negatively regulated in these merged groups, with only 14 significantly down-regulated genes found in Six1+Eya1m, 11 in Six1m and 13 in Eya1m (Supplementary file 3, Tables 4–6), re-enforcing the notion that together, Six1 and Eya1 act primarily as transcriptional activators (Figure 2C).

### Target genes of Six1 and Eya1 are implicated in sensory neurogenesis

Presumptive direct targets that were significantly up-regulated in our merged data set (Six1+Eya1m) were analysed using Panther (Mi et al., 2013) to examine the representation of genes grouped by molecular function (Figure 2D). Transcription factors and protein binding together accounted for the largest fraction of up-regulated genes (53% in total), followed by enzymes (30%) and transporter molecules (13%), suggesting a developmental function of many of the genes up-regulated by either Six1 or Eya1. GSEA was then conducted using DAVID (Huang et al., 2009) on the sets of significantly up- or down-regulated genes in our merged data sets, as well as in various combinations of subsets of differentially expressed genes from our individual treatment groups (Figure 3 and Figure 3—figure supplement 1). This analysis showed that genes directly up-regulated by Six1, Eya1 or Six1+Eya1 were highly enriched for terms associated with sense organ development, inner-ear development, mechanoreceptor differentiation, eye morphogenesis, neurogenesis and axon guidance consistent with their synergistic role in sensory development (Grocott et al., 2012; Schlosser, 2010) and neurogenesis (Maier et al., 2014; Schlosser and Northcutt, 2000). Apart from genes encoding transcription factors involved in sensory development (see below), genes encoding cell cycle regulators (CyclinD, RGCC), cell surface receptors and adhesion molecules (e.g. CXCR7, EDAR, Protocadherin11, Claudin3, Fzd1, Fzd4,), secreted proteins (e.g. FGF3, FGF19, Dkk1, Neurotrophin3) and cytoskeletal regulators (e.g. RhoV, Espin) with known or potential roles in placode development were also up-regulated.

![Figure 3.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig3-v2.jpg)

**Figure 3.:** In each case, treatment groups considered are highlighted and outlined in bold in the accompanying Venn diagram. Yellow colouring indicates Six1 treatment; blue shows Eya1 and green Six1+Eya1. Enrichment scores ≥1.5 are reported for individual treatment groups (Ind.) and, where available, ≥0.5 for merged treatment groups (Merg.). (A) Up-regulated genes from all treatment groups included in analysis; (B) Six1 overexpression only; (C) Eya1 overexpression only. (D) Genes differentially expressed after overexpression of both Six1 and Eya1; (E) exclusively after Six1 overexpression; (F) exclusively after Eya1 overexpression.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** In each case, treatment groups considered are highlighted and outlined in bold in the accompanying Venn diagram. Yellow colouring indicates Six1 treatment; blue shows Eya1 and green Six1+Eya1. Enrichment scores ≥1.5 are reported for individual treatment groups (Ind.) and, where available, ≥0.5 for merged treatment groups (Merg.). (A) Down-regulated genes from all treatment groups included in analysis; (B) Six1 overexpression only; (C) Eya1 overexpression only. (D) Genes differentially expressed after overexpression of both Six1 and Eya1; (E) exclusively after Six1 overexpression.

GSEA analysis of discrete subsets of genes exclusively regulated by Six1 or Eya1 suggested that they also regulate some categories of genes independently of one another. A particularly interesting finding was the extreme enrichment of Hox genes (specifically of the Antennapedia-type) in the Eya1-specific subset of up-regulated genes (Figure 3F), suggesting that Eya1 may play a previously un-identified role in regulating Hox gene expression independently of Six1.

### Characterisation of transcriptional regulators activated by Six1 or Eya1

To verify our RNA-Seq data, we selected a number of target genes for further characterisation and, in order to gain insight into the GRN downstream of Six1 and Eya1, we restricted candidates to transcription factors or co-factors up-regulated by Six1 or Eya1. First, we generated a list of well-supported target genes containing all genes with at least a two-fold up-regulation in at least two of our three treatment groups (Table 1). From the 228 genes in this list we selected all 30 transcription factors or co-factors for further analysis. However, we were unable to amplify two genes from this list (Egr3, Fbxo41) from cDNA and therefore omitted these genes from further characterisation. We additionally included Sox3 and Ngn1 - which were found to be slightly below our threshold of twofold up-regulation in at least two treatment groups - because previous studies have implicated these genes in the regulation of placodal neurogenesis downstream of Six1 and Eya1 (Ma et al., 1996, 1998; Schlosser et al., 2008; Ahmed et al., 2012b) (Table 2).

**Table 1.**
 Genes with at least two-fold up-regulation in at least two out of three individual treatment groups (Six1i; Eya1i; Six1+Eya1i).


<table>
  <thead>
    <tr>
      <th></th>
      <th>Annotation*</th>
      <th>Accession</th>
      <th>Six1 FC†</th>
      <th>Eya1 FC‡</th>
      <th>Six1+Eya1 FC§</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Chromosome unknown open reading frame</td>
      <td>XM_002938866.2</td>
      <td>6.2</td>
      <td>-</td>
      <td>7.9</td>
    </tr>
    <tr>
      <td></td>
      <td>cDNA clone IMAGE:7022272</td>
      <td>BC094950.1</td>
      <td>5.6</td>
      <td>5.1</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis cyclin Dx (ccndx)</td>
      <td>NP_001087887.1</td>
      <td>7.5</td>
      <td>-</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Calcitonin gene-related peptide-like</td>
      <td>XM_002941675.2</td>
      <td>7</td>
      <td>-</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis tripartite motif containing 63, E3 ubiquitin protein ligase (trim63)</td>
      <td>NM_001093214.1</td>
      <td>5.3</td>
      <td>3.6</td>
      <td>6.3</td>
    </tr>
    <tr>
      <td></td>
      <td>ATP-sensitive inward rectifier potassium channel 11-like</td>
      <td>XM_004916278.1</td>
      <td>5.1</td>
      <td>-</td>
      <td>6.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Leucine rich repeat containing 52 (lrrc52)</td>
      <td>XM_002933773.2</td>
      <td>6.1</td>
      <td>-</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td>#</td>
      <td>SIX homeobox 2 (six2)</td>
      <td>NM_001100275.1</td>
      <td>5</td>
      <td>3.5</td>
      <td>5.9</td>
    </tr>
    <tr>
      <td></td>
      <td>Potassium voltage-gated channel shaker-related subfamily member 2 (kcna2)</td>
      <td>XM_004910736.1</td>
      <td>5.1</td>
      <td>-</td>
      <td>4.9</td>
    </tr>
    <tr>
      <td></td>
      <td>Butyrophilin subfamily 2 member A1 (btn2a1)</td>
      <td>NM_001094508.1</td>
      <td>-</td>
      <td>1.2</td>
      <td>4.9</td>
    </tr>
    <tr>
      <td></td>
      <td>Glutathione peroxidase 2 (gpx2)</td>
      <td>NM_001256315.1</td>
      <td>-</td>
      <td>2.5</td>
      <td>4.8</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis for Xsox17-alpha protein</td>
      <td>AJ001730.1</td>
      <td>3.6</td>
      <td>2.6</td>
      <td>4.8</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis ectodysplasin A receptor (edar)</td>
      <td>NM_001087047.1</td>
      <td>2.8</td>
      <td>2.5</td>
      <td>4.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC101734405)</td>
      <td>XM_004918247.1</td>
      <td>4.4</td>
      <td>0.8</td>
      <td>3.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Glutathione peroxidase 2 (gpx2)</td>
      <td>NM_001256315.1</td>
      <td>3.4</td>
      <td>2.1</td>
      <td>4.4</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis cytochrome P450, family 2, subfamily D, polypeptide 6 (cyp2d6)</td>
      <td>NM_001093574.1</td>
      <td>1.1</td>
      <td>-</td>
      <td>4.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Calcium/calmodulin-dependent protein kinase kinase 2beta (camkk2)</td>
      <td>XM_002937701.2</td>
      <td>4.4</td>
      <td>2.6</td>
      <td>3.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Cytochrome P450 family 26 subfamily B polypeptide 1 (cyp26b1)</td>
      <td>NM_001079187.2</td>
      <td>3.3</td>
      <td>4</td>
      <td>4.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Troponin I type 1 (skeletal, slow)</td>
      <td>BC061268</td>
      <td>1.8</td>
      <td>-</td>
      <td>4.3</td>
    </tr>
    <tr>
      <td></td>
      <td>72 kDa inositol polyphosphate 5-phosphatase-like (LOC101734556)</td>
      <td>XM_004916572.1</td>
      <td>-</td>
      <td>4.2</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Chemokine (C-X-C motif) receptor 7 (cxcr7)</td>
      <td>NM_001030434.1</td>
      <td>3</td>
      <td>2.8</td>
      <td>4.1</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis xSox17 alpha 2</td>
      <td>AB052691.1</td>
      <td>1.7</td>
      <td>1.4</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td>Espin (espn) transcript variant X3</td>
      <td>XM_004916193.1</td>
      <td>-</td>
      <td>2.1</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td>B-cell CLL/lymphoma 11B (zinc finger protein) (bcl11b)</td>
      <td>XM_004917116.1</td>
      <td>-</td>
      <td>1.9</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td>C-X-C motif chemokine 10-like</td>
      <td>XM_002940578.2</td>
      <td>1.9</td>
      <td>4</td>
      <td>3.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis hedgehog-interacting protein</td>
      <td>BC046952.1</td>
      <td>-</td>
      <td>2.7</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td>X-linked inhibitor of apoptosis (xiap)</td>
      <td>NM_001030412.1</td>
      <td>4</td>
      <td>3.1</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis uncharacterized (LOC496300)</td>
      <td>NM_001095458.1</td>
      <td>1.4</td>
      <td>3.9</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis RDC1 like protein</td>
      <td>BC098974.1</td>
      <td>3.6</td>
      <td>2.1</td>
      <td>3.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis for frizzled 4 protein (fz4 gene)</td>
      <td>AJ251750.1</td>
      <td>1.3</td>
      <td>0.6</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td></td>
      <td>Espin (espn) transcript variant X1</td>
      <td>XM_002933856.2</td>
      <td>3.1</td>
      <td>2.7</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Paired box 1 (pax1) transcript variant X1</td>
      <td>JQ929179.1</td>
      <td>-</td>
      <td>3</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Potassium voltage-gated channel subfamily F member 1 (kcnf1)</td>
      <td>NM_001102926.1</td>
      <td>3.6</td>
      <td>-</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Echinoderm microtubule-associated protein-like 1-like</td>
      <td>XM_004917169.1</td>
      <td>-</td>
      <td>3.6</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td></td>
      <td>Leucine rich adaptor protein 1-like (lurap1l)</td>
      <td>XM_002940127.2</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Sine oculis binding protein homolog (Drosophila)</td>
      <td>BC154687.1</td>
      <td>2.7</td>
      <td>1.6</td>
      <td>3.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RNA-directed DNA polymerase homolog</td>
      <td>XM_004916122.1</td>
      <td>3.4</td>
      <td>-</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Kinesin family member 3C (kif3c) transcript variant X1</td>
      <td>XM_004914940.1</td>
      <td>1.4</td>
      <td>0.8</td>
      <td>3.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Anoctamin 2 (ano2)</td>
      <td>XM_002932297.2</td>
      <td>2.2</td>
      <td>1.3</td>
      <td>3.4</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis natriuretic peptide C (nppc)</td>
      <td>NM_001112924.1</td>
      <td>2.1</td>
      <td>-</td>
      <td>3.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC101734952)</td>
      <td>XM_004916172.1</td>
      <td>2.5</td>
      <td>-</td>
      <td>3.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Poly (ADP-ribose) polymerase 14-like (LOC101731378)</td>
      <td>XM_004920062.1</td>
      <td>3.1</td>
      <td>-</td>
      <td>3.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Protocadherin-11 X-linked-like (LOC100493938)</td>
      <td>XM_004916890.1</td>
      <td>-</td>
      <td>3.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC101733225)</td>
      <td>XM_004919937.1</td>
      <td>2.5</td>
      <td>3.2</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Calcium channel voltage-dependent beta 4 subunit (cacnb4)</td>
      <td>NM_001142151.1</td>
      <td>3.1</td>
      <td>-</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>F-box protein 32 (fbxo32) transcript variant X1</td>
      <td>XM_002941397.2</td>
      <td>1.8</td>
      <td>-</td>
      <td>3.1</td>
    </tr>
    <tr>
      <td></td>
      <td>cDNA clone TEgg026p17</td>
      <td>CR761997.2</td>
      <td>3</td>
      <td>2.6</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis transforming growth factor beta-induced (tgfbi)</td>
      <td>NM_001095238.1</td>
      <td>1.3</td>
      <td>-</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td>Mucin-2-like (LOC100494747)</td>
      <td>XM_002936043.2</td>
      <td>3</td>
      <td>2</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis uncharacterized protein (MGC68450)</td>
      <td>NM_001089841.1</td>
      <td>2.2</td>
      <td>-</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis neuregulin alpha-1</td>
      <td>AF076618.1</td>
      <td>1.4</td>
      <td>0.8</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Potassium voltage-gated channel Isk-related (kcne1)</td>
      <td>XM_004912135.1</td>
      <td>2.2</td>
      <td>1.5</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Olfactory receptor 5G3-like (LOC100492086)</td>
      <td>XM_002942220.1</td>
      <td>1.9</td>
      <td>-</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Alpha-kinase 2 (alpk2)</td>
      <td>XM_004910401.1</td>
      <td>1.1</td>
      <td>2.2</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis arginyl amino peptidase (amino peptidase B) b (rnpep-b)</td>
      <td>NM_001092079.1</td>
      <td>-</td>
      <td>2.7</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis SRY-box containing protein (Sox1)</td>
      <td>EF672727.1</td>
      <td>-</td>
      <td>2.6</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Copine II (cpne2) transcript variant X1</td>
      <td>XM_004913481.1</td>
      <td>1</td>
      <td>1.2</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis hemoglobin, gamma A (hbg1)</td>
      <td>NM_001096347</td>
      <td>1.2</td>
      <td>-</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td></td>
      <td>KIAA0895 protein (kiaa0895)</td>
      <td>NM_001114073.1</td>
      <td>1.6</td>
      <td>2.6</td>
      <td>-</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis empty spiracles homeobox 1gene 2 (emx1.2)</td>
      <td>NM_001093430.1</td>
      <td>2.6</td>
      <td>1.9</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Homeobox B8 (hoxb8) transcript variant X1</td>
      <td>XM_002938021.2</td>
      <td>1.1</td>
      <td>2.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Monocyte to macrophage differentiation-associated (mmd)</td>
      <td>XM_004918560.1</td>
      <td>-</td>
      <td>1.2</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis uncharacterized (LOC100036933)</td>
      <td>NM_001097704.1</td>
      <td>1.5</td>
      <td>1.5</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Finished cDNA clone TNeu143f19</td>
      <td>CR760056.2</td>
      <td>2.2</td>
      <td>2.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Chromosome unknown open reading frame C2orf80</td>
      <td>XM_002937119.2</td>
      <td>1.4</td>
      <td>2.1</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Single-minded homolog 1 (sim1) transcript variant X2</td>
      <td>XM_004914545.1</td>
      <td>-</td>
      <td>1.4</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Transmembrane protein 2-like (LOC100491930)</td>
      <td>XM_002932255.2</td>
      <td>2.4</td>
      <td>1.9</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>PX domain containing 1 (pxdc1)</td>
      <td>NM_001130262.1</td>
      <td>1.4</td>
      <td>-</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Aldehyde dehydrogenase 1 family member L2 (aldh1l2)</td>
      <td>XM_002938070.2</td>
      <td>0.9</td>
      <td>1.3</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC100490228)</td>
      <td>XM_002942932.2</td>
      <td>1.8</td>
      <td>-</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Beta-1 3-galactosyltransferase 2-like (LOC101732799)</td>
      <td>XM_004918863.1</td>
      <td>1.6</td>
      <td>2.3</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Alpha-2 3-sialyltransferase ST3Gal V (st3gal5)</td>
      <td>FN550108.1</td>
      <td>1.8</td>
      <td>-</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis uncharacterized protein (MGC64538)</td>
      <td>NM_001086337.1</td>
      <td>-</td>
      <td>1.6</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Transmembrane channel-like protein 7-like (LOC100493700)</td>
      <td>XM_002932222.2</td>
      <td>1.4</td>
      <td>0.9</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Kinase insert domain receptor (a type III receptor tyrosine kinase) (kdr)</td>
      <td>XM_002934669.2</td>
      <td>1.9</td>
      <td>0.9</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Serine/threonine kinase 32A (stk32a)</td>
      <td>XM_002936707.2</td>
      <td>1.3</td>
      <td>2.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Pancreatic lipase-related protein 2 (pnliprp2)</td>
      <td>NM_001089647.1</td>
      <td>2.1</td>
      <td>0.7</td>
      <td>2.2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis nephrin (NPHS1)</td>
      <td>AY902238.1</td>
      <td>-</td>
      <td>2.2</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Poly (ADP-ribose) polymerase 14-like (LOC100485144)</td>
      <td>XM_002943546.2</td>
      <td>2</td>
      <td>2.2</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Frizzled family receptor 4 (fzd4)</td>
      <td>XM_002936543.2</td>
      <td>1.4</td>
      <td>0.7</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Neuropeptide Y receptor Y2 (npy2r)</td>
      <td>XM_004911153.1</td>
      <td>2.1</td>
      <td>-</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Deoxyribonuclease gamma-like (LOC100497175)</td>
      <td>XM_002938386.2</td>
      <td>1.8</td>
      <td>2.1</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis dehydrogenase/reductase (SDR family) member 11 (dhrs11)</td>
      <td>NM_001094963.1</td>
      <td>-</td>
      <td>1.5</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis gamma-glutamyl hydrolase (ggh)</td>
      <td>NM_001092691.1</td>
      <td>2.1</td>
      <td>1.3</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>Opsin-3-like</td>
      <td>XM_002932623.2</td>
      <td>1</td>
      <td>1.2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis transmembrane protein 56 (tmem56-b)</td>
      <td>NM_001086447.1</td>
      <td>-</td>
      <td>1.1</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis pyruvate dehyrogenase phosphatase catalytic subunit 1 (pdp1)</td>
      <td>NM_001094221.1</td>
      <td>1.5</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>ArfGAP with SH3 domain ankyrin repeat and PH domain 3 (asap3)</td>
      <td>XM_002939360.2</td>
      <td>1.7</td>
      <td>-</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Early growth response 3 (egr3)</td>
      <td>XM_002932703.2</td>
      <td>1.6</td>
      <td>0.8</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td>#</td>
      <td>POU class 4 homeobox 1 (pou4f1.2)</td>
      <td>NM_001097307.1</td>
      <td>1.3</td>
      <td>1</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>Activin beta B subunit</td>
      <td>S61773.1</td>
      <td>-</td>
      <td>1.7</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>Monocyte to macrophage differentiation-associated (mmd)</td>
      <td>XM_002937811.2</td>
      <td>1.7</td>
      <td>1.1</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis ribosomal protein S2e</td>
      <td>BC130122.1</td>
      <td>-</td>
      <td>1.8</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis ras homolog family member V (rhov)</td>
      <td>NM_001128659.1</td>
      <td>1.2</td>
      <td>0.8</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis adenomatosis polyposis coli down-regulated 1 (apcdd1)</td>
      <td>NM_001094109.1</td>
      <td>1.2</td>
      <td>1</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis zinc finger protein 214 (znf214)</td>
      <td>NM_001097042.1</td>
      <td>1.2</td>
      <td>0.8</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis cdc25Ba</td>
      <td>AB363840.1</td>
      <td>1.2</td>
      <td>-</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis apelin (apln-a)</td>
      <td>NM_001097924.1</td>
      <td>0.9</td>
      <td>1.3</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Suppressor of cytokine signaling 2 (socs2)</td>
      <td>NM_001095760.1</td>
      <td>-</td>
      <td>1.1</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>#</td>
      <td>cAMP responsive element modulator (crem)</td>
      <td>XM_002935162.2</td>
      <td>-</td>
      <td>1.4</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis clone IMAGE:4684003</td>
      <td>BC042305.1</td>
      <td>1.4</td>
      <td>-</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis ets-2a proto-oncogene</td>
      <td>BC133183.1</td>
      <td>1.3</td>
      <td>1</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis similar to envoplakin</td>
      <td>BC045116.1</td>
      <td>1.4</td>
      <td>1.4</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Ras homolog family member V (rhov)</td>
      <td>NM_001095566.1</td>
      <td>1.4</td>
      <td>1</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Samd9l protein (samd9l)</td>
      <td>XM_002943522.2</td>
      <td>-</td>
      <td>1.2</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Flocculation protein FLO11-like (LOC100490389)</td>
      <td>XM_002942555.2</td>
      <td>1.2</td>
      <td>-</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>c-Jun-amino-terminal kinase-interacting protein 4-like (LOC100493724)</td>
      <td>XM_002939963.2</td>
      <td>1.1</td>
      <td>-</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis Dickkopf-1 (Xdkk-1)</td>
      <td>AF030434.1</td>
      <td>1</td>
      <td>1.2</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis ectoderm neural cortex related-3 (Encr-3)</td>
      <td>AY216793.1</td>
      <td>1.1</td>
      <td>0.8</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC101730819)</td>
      <td>XM_004915204.1</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis LIM class homeodomain protein</td>
      <td>BC084744.1</td>
      <td>1.1</td>
      <td>0.7</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Ceramide kinase-like (cerkl)</td>
      <td>XM_002932015.2</td>
      <td>1.4</td>
      <td>1.3</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>Mannosyl (alpha-1 3-)-glycoprotein beta-1 4-N-acetylglucosaminyltransferase (mgat4b)</td>
      <td>NM_001091975.1</td>
      <td>2</td>
      <td>-</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>Fibroblast growth factor 19 (fgf19)</td>
      <td>NM_001142825.1</td>
      <td>-</td>
      <td>2</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>#</td>
      <td>F-box protein 41 (fbxo41)</td>
      <td>NM_001079043.1</td>
      <td>1.3</td>
      <td>0.6</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>Avidin-like (LOC100487365)</td>
      <td>XM_002939983.2</td>
      <td>2</td>
      <td>1.6</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Four and a half LIM domains 2 (fhl2)</td>
      <td>NM_001126761.1</td>
      <td>-</td>
      <td>1.1</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>Metalloprotease TIKI1-like (LOC100491951)</td>
      <td>XM_002936336.2</td>
      <td>1.1</td>
      <td>1.4</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis Kazal-type serine peptidase inhibitor domain 1 (kazald1)</td>
      <td>NM_001092073.1</td>
      <td>1.6</td>
      <td>1.1</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC101734664)</td>
      <td>XM_004910525.1</td>
      <td>1.2</td>
      <td>0.6</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis similar to calsequestrin 2 (cardiac muscle)</td>
      <td>BC097545.1</td>
      <td>1.8</td>
      <td>1.5</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis COMM domain containing 3 (commd3)</td>
      <td>NM_001095386.1</td>
      <td>1.1</td>
      <td>1.9</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis alcohol dehydrogenase iron containing1 (adhfe1)</td>
      <td>NM_001127802.1</td>
      <td>-</td>
      <td>1.9</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis ectonucleoside triphosphate diphosphohydrolase 1 (entpd1)</td>
      <td>NM_001092268.1</td>
      <td>1.8</td>
      <td>0.6</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Protein fosB-like transcript variant X2</td>
      <td>XM_004916957.1</td>
      <td>-</td>
      <td>1.7</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Tocopherol (alpha) transfer protein (ttpa)</td>
      <td>NM_001008184.1</td>
      <td>-</td>
      <td>1.7</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis tetratricopeptide repeat domain 39B (ttc39b)</td>
      <td>NM_001094701.1</td>
      <td>1.1</td>
      <td>-</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis Tbx6 (Tbx6)</td>
      <td>DQ355794.1</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis uncharacterized (LOC100036989)</td>
      <td>NM_001097746.1</td>
      <td>-</td>
      <td>1.3</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis cDNA clone IMAGE:6947552</td>
      <td>BC093552.1</td>
      <td>1.3</td>
      <td>1.7</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>B-cell CLL/lymphoma 10 (bcl10)</td>
      <td>NM_001015777.2</td>
      <td>1.7</td>
      <td>-</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC100494710)</td>
      <td>XM_002939048.2</td>
      <td>1.4</td>
      <td>1.6</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis keratin 17 (krt17)</td>
      <td>NM_001094941.1</td>
      <td>-</td>
      <td>1.2</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Membrane metallo-endopeptidase-like 1 (mmel1)</td>
      <td>NM_001127095.1</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Putative methyltransferase KIAA1456 homolog</td>
      <td>XM_002934674.2</td>
      <td>1.1</td>
      <td>-</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Phospholipase Cdelta 3 (plcd3)</td>
      <td>XM_002935518.2</td>
      <td>1.1</td>
      <td>1.5</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>IdnK gluconokinase homolog (E. coli) (idnk)</td>
      <td>NM_001126592.1</td>
      <td>1.4</td>
      <td>0.9</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC100486093) transcript variant X2</td>
      <td>XM_002939117.2</td>
      <td>1.5</td>
      <td>-</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis similar to calsequestrin 2 (cardiac muscle)</td>
      <td>BC041283.1</td>
      <td>1.1</td>
      <td>-</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Piwi-like RNA-mediated gene silencing 2 (piwil2)</td>
      <td>NM_001112999.1</td>
      <td>1.1</td>
      <td>-</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Zinc finger and BTB domain containing 20 (zbtb20)</td>
      <td>XM_002939649.2</td>
      <td>1.4</td>
      <td>-</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>#</td>
      <td>V-maf musculoaponeurotic fibrosarcoma oncogene homolog A (mafa)</td>
      <td>NM_001032304.1</td>
      <td>1.4</td>
      <td>0.9</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis uncharacterized protein (MGC81120)</td>
      <td>NM_001091225.1</td>
      <td>1.4</td>
      <td>0.9</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Single-minded homolog 1 (Drosophila) (sim1) transcript variant X3</td>
      <td>XM_004914546.1</td>
      <td>1.1</td>
      <td>1.3</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Xenopus laevis alpha-2-macroglobulin-like 1 (a2ml1)</td>
      <td>NM_001135077.1</td>
      <td>1.1</td>
      <td>-</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis chromogranin A (parathyroid secretory protein 1) (chga)</td>
      <td>NM_001094724.1</td>
      <td>1.6</td>
      <td>1.4</td>
      <td>2.2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis lipaseendothelial (lipg)</td>
      <td>NM_001090061.1</td>
      <td>1.2</td>
      <td>1.3</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td></td>
      <td>G protein-coupled receptor 56 (gpr56)</td>
      <td>XM_002931653.2</td>
      <td>1.7</td>
      <td>-</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis family with sequence similarity 101member B (fam101b)</td>
      <td>NM_001093870.1</td>
      <td>1.5</td>
      <td>0.8</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis CD81 protein (cd81-a)</td>
      <td>NM_001086613.1</td>
      <td>0.7</td>
      <td>1.1</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis calbindin D28k</td>
      <td>BC170542.1</td>
      <td>2.2</td>
      <td>-</td>
      <td>3.1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis ATPaseNa+/K+ transportingbeta 1 polypeptide (atp1b1)</td>
      <td>NM_001086759.1</td>
      <td>1.2</td>
      <td>1</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis 7-transmembrane receptor frizzled-1</td>
      <td>AF231711.1</td>
      <td>1.4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis prostaglandin reductase 2 (ptgr2)</td>
      <td>NM_001079334.1</td>
      <td>1.4</td>
      <td>1.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis TGF-beta2 for transforming growth factor-beta2</td>
      <td>X51817.1</td>
      <td>1.3</td>
      <td>-</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>#</td>
      <td>SRY (sex determining region Y)-box 2 (sox2)</td>
      <td>NM_213704.3</td>
      <td>1.1</td>
      <td>1.3</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis for enhancer of split related 9 (esr9 gene)</td>
      <td>AJ009282.1</td>
      <td>1.7</td>
      <td>1.6</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis mal T-cell differentiation protein (mal)</td>
      <td>NM_001086577.1</td>
      <td>-</td>
      <td>1.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Transmembrane proteaseserine 13 (tmprss13)</td>
      <td>XM_002932904.2</td>
      <td>1.5</td>
      <td>1.1</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis Ras-related associated with diabetes (rrad)</td>
      <td>NM_001092750.1</td>
      <td>8</td>
      <td>4.6</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Integrin beta 4 (itgb4) transcript variant X1</td>
      <td>XM_002939974.2</td>
      <td>1.4</td>
      <td>-</td>
      <td>2.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Xenopus (Silurana) tropicalis FERM domain containing 4A (frmd4a)</td>
      <td>XM_002935243.2</td>
      <td>1.1</td>
      <td>0.6</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis complement factor I (cfi-a)</td>
      <td>NM_001085952.1</td>
      <td>1.4</td>
      <td>1.2</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis SIX homeobox 1 (six1)</td>
      <td>NP_001082027.1</td>
      <td>1.4</td>
      <td>1.2</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>FH2 domain-containing protein 1-like (LOC100496216)</td>
      <td>XM_002934907.2</td>
      <td>1.9</td>
      <td>0.9</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis mab-21-like 2 (mab21l2-b)</td>
      <td>NM_001096770.1</td>
      <td>-</td>
      <td>2.8</td>
      <td>2.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis regulator of cell cycle (rgcc)</td>
      <td>NM_001093976.1</td>
      <td>1.3</td>
      <td>1.1</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis Cep63</td>
      <td>FJ464988.1</td>
      <td>-</td>
      <td>1.4</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis CD81 antigen (target of anti proliferative antibody 1)</td>
      <td>BC041217.1</td>
      <td>1.7</td>
      <td>1.1</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>Transmembrane serine protease 9</td>
      <td>BC087611.1</td>
      <td>1.1</td>
      <td>1.1</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis POU class 3 homeobox 2 (pou3f2-b)</td>
      <td>NM_001096751.1</td>
      <td>3</td>
      <td>2.3</td>
      <td>2.9</td>
    </tr>
    <tr>
      <td></td>
      <td>G protein-coupled receptor 153 (gpr153)</td>
      <td>NM_001128052.1</td>
      <td>2.5</td>
      <td>1.1</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis Myoblast determination protein 1 homolog A</td>
      <td>BC041190.1</td>
      <td>3.5</td>
      <td>2.7</td>
      <td>4.7</td>
    </tr>
    <tr>
      <td>#</td>
      <td>T-cell leukemia homeobox 1 (tlx1) transcript variant 1</td>
      <td>XM_002936768.2</td>
      <td>2.6</td>
      <td>2.3</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis neurotrophin 3 (ntf3)</td>
      <td>NM_001092740.1</td>
      <td>1.4</td>
      <td>1.5</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis p21 GTPase-associated kinase 1 (PAK1)</td>
      <td>AF000239.1</td>
      <td>1.2</td>
      <td>-</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis hairy and enhancer of split 9, gene 1 (hes9.1-b)</td>
      <td>NP_001089097.1</td>
      <td>1.8</td>
      <td>1.5</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis tetraspanin 1 (tspan1)</td>
      <td>NM_001095473.1</td>
      <td>1.2</td>
      <td>0.7</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis uncharacterized protein (MGC83079)</td>
      <td>NM_001091250.1</td>
      <td>2</td>
      <td>1.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis cDNA clone IMAGE:5085355</td>
      <td>BC073731.1</td>
      <td>1.3</td>
      <td>-</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Family with sequence similarity 198member A (fam198a)</td>
      <td>XM_002937853.2</td>
      <td>1.7</td>
      <td>0.7</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Progestin and adipoQ receptor family member IX (paqr9)</td>
      <td>XM_004914351.1</td>
      <td>1.7</td>
      <td>-</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Hairy and enhancer of split 8 (hes8)</td>
      <td>XM_002933849.2</td>
      <td>2.8</td>
      <td>1.7</td>
      <td>3.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis p21 GTPase-associated kinase 1</td>
      <td>BC081113.1</td>
      <td>1.3</td>
      <td>0.8</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Finished cDNA clone TNeu008g03</td>
      <td>CR761907.2</td>
      <td>1.2</td>
      <td>1.1</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td></td>
      <td>WD repeat domain 27 (wdr27)</td>
      <td>XM_002931515.2</td>
      <td>1.2</td>
      <td>2.2</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Growth factor independent 1 transcription repressor (gfi1)</td>
      <td>XM_002933803.2</td>
      <td>1.8</td>
      <td>1.8</td>
      <td>3.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Protein phosphatase 2 regulatory subunit B'beta (ppp2r5b)</td>
      <td>NM_001100279.1</td>
      <td>2.4</td>
      <td>1.4</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Ornithine decarboxylase antizyme 2 (oaz2), transcript variant 2</td>
      <td>NP_001106583.2</td>
      <td>1.8</td>
      <td>-</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis fast troponin T (TNNT3)</td>
      <td>AY114144.1</td>
      <td>-</td>
      <td>1.1</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis xRipply3 for xRipply3 protein</td>
      <td>AB455086.1</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>RAS-like family 11member B (rasl11b)</td>
      <td>NM_001015774.1</td>
      <td>-</td>
      <td>1.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis for thimet oligopeptidase</td>
      <td>BC070748.1</td>
      <td>3.8</td>
      <td>-</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis fibroblast growth factor 3 (fgf3)</td>
      <td>NM_001008153.1</td>
      <td>2</td>
      <td>1.2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis cDNA clone IMAGE:8332229</td>
      <td>BC155363.1</td>
      <td>1.5</td>
      <td>0.9</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>Proline rich 15 (prr15)</td>
      <td>XM_002933381.2</td>
      <td>1.6</td>
      <td>-</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>Integrin beta 6 (itgb6)</td>
      <td>NM_001097306.1</td>
      <td>2.3</td>
      <td>0.6</td>
      <td>2.8</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Xenopus laevis empty spiracles homeobox 1, gene 2 (emx1.2)</td>
      <td>NM_001093430.1</td>
      <td>2.6</td>
      <td>1.4</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis p21-activated kinase (PAK1)</td>
      <td>AF169794.1</td>
      <td>1.4</td>
      <td>1.8</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td>#</td>
      <td>ISL LIM homeobox 2 (isl2)</td>
      <td>NM_001166041.1</td>
      <td>1.5</td>
      <td>-</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td>#</td>
      <td>Atonal homolog 1 (Drosophila) (atoh1)</td>
      <td>XM_004911085.1</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Ectodysplasin A receptor (edar)</td>
      <td>NM_001087047.1</td>
      <td>4.3</td>
      <td>-</td>
      <td>3.3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis degr03</td>
      <td>DQ096846.1</td>
      <td>2.1</td>
      <td>2.2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>Calcyphosine (caps)</td>
      <td>NM_001097320.1</td>
      <td>-</td>
      <td>1.4</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis kiaa0930</td>
      <td>NM_001086221.1</td>
      <td>1.5</td>
      <td>1</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Putative N-acetyltransferase 16-like (LOC100490742)</td>
      <td>XM_002943189.1</td>
      <td>2.1</td>
      <td>1</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td>#</td>
      <td>T-box 15 (tbx15)</td>
      <td>XM_002940981.2</td>
      <td>2</td>
      <td>1</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>#</td>
      <td>SRY (sex determining region Y)-box 1 (sox1)</td>
      <td>NM_001080996.1</td>
      <td>0.6</td>
      <td>1.5</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Cytochrome P450 family 2 subfamily C polypeptide 18 (cyp2c18)</td>
      <td>NM_001091776.1</td>
      <td>2.1</td>
      <td>1.4</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis calcitonin receptor-like (calcrl)</td>
      <td>NM_001086737.1</td>
      <td>1.1</td>
      <td>0.8</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis claudin 3 (cldn3)</td>
      <td>NM_001005709.1</td>
      <td>2.1</td>
      <td>1.3</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Atlastin GTPase 1 (atl1)</td>
      <td>NM_001078754.1</td>
      <td>1.8</td>
      <td>2</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>Rho GTPase activating protein 9 (arhgap9), transcript variant X2</td>
      <td>XM_012957829</td>
      <td>1.8</td>
      <td>1.2</td>
      <td>3.4</td>
    </tr>
    <tr>
      <td>#</td>
      <td>X. laevis Hes2</td>
      <td>BC084134.1</td>
      <td>1.7</td>
      <td>0.9</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis U3 snRNA</td>
      <td>X07318.1</td>
      <td>1</td>
      <td>2.8</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Uncharacterized (LOC101732195)</td>
      <td>XM_004912378.1</td>
      <td>2</td>
      <td>-</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>Tumor necrosis factor receptor superfamilymember 21 (tnfrsf21)</td>
      <td>NM_001079136.1</td>
      <td>1.1</td>
      <td>0.8</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis arginase 3</td>
      <td>U08408.1</td>
      <td>-</td>
      <td>1.3</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>ChaC cation transport regulator homolog 1 (chac1)</td>
      <td>XM_002939546.2</td>
      <td>1.2</td>
      <td>1.3</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis DIRAS familyGTP-binding RAS-like 3 (diras3)</td>
      <td>NM_001095243.1</td>
      <td>0.8</td>
      <td>1.7</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>X. laevis DnaJ (Hsp40) homolog subfamily C member 27 (dnajc27-b)</td>
      <td>NM_001095422.1</td>
      <td>1.1</td>
      <td>0.8</td>
      <td>1.1</td>
    </tr>
  </tbody>
</table>

_* Genes are ranked by FC value, using the highest FC in each of the three treatment groups. Genes included must have FC ≥ 1 in at least two out of the three treatment groups as well as showing at least a two-fold difference in FC to the un-injected control (not shown). Corresponding values ≥0.5 are shown for all treatments.† Log2 Fold change values after Six1-GR overexpression.‡ Log2 Fold change values after Eya1-GR overexpression.§ Log2 Fold change values after Six1-GR+Eya1-GR overexpression.# Denotes transcription factors with at least a two-fold change in at least two treatment groups selected for further analysis._

**Table 2.**
 Transcription factors and co-factors selected for characterisation by in-situ-hybridisation ranked by FC value in individual treatment.


<table>
  <thead>
    <tr>
      <th>Annotation</th>
      <th>Gene</th>
      <th>Accession</th>
      <th colspan="3">Individual</th>
      <th colspan="3">Merged</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>Six1*</td>
      <td>Eya1†</td>
      <td>Six1+Eya1‡</td>
      <td>Six1§</td>
      <td>Eya1#</td>
      <td>Six1+Eya1¶</td>
    </tr>
    <tr>
      <td>SIX homeobox 2 (Six2)</td>
      <td>Six2</td>
      <td>NM_001100275.1</td>
      <td>5</td>
      <td>3.5</td>
      <td>5.9</td>
      <td>5.4**</td>
      <td>5**</td>
      <td>4.9**</td>
    </tr>
    <tr>
      <td>X. laevis for Xsox17-alpha protein</td>
      <td>Sox17</td>
      <td>AJ001730.1</td>
      <td>3.6</td>
      <td>2.6</td>
      <td>4.8</td>
      <td>4.4**</td>
      <td>3.3**</td>
      <td>3.5**</td>
    </tr>
    <tr>
      <td>X. laevis Myoblast determination protein 1 homolog A</td>
      <td>MyoD1</td>
      <td>BC041190.1</td>
      <td>3.5</td>
      <td>2.7</td>
      <td>4.7</td>
      <td>4.1**</td>
      <td>4.2**</td>
      <td>3.9**</td>
    </tr>
    <tr>
      <td>Hairy and enhancer of split 8 (Hes8)</td>
      <td>Hes8</td>
      <td>XM_002933849.2</td>
      <td>2.8</td>
      <td>1.7</td>
      <td>3.6</td>
      <td>3.2**</td>
      <td>3.2**</td>
      <td>3.1**</td>
    </tr>
    <tr>
      <td>Growth factor independent 1 transcription repressor (Gfi1)</td>
      <td>Gfi1a</td>
      <td>XM_002933803.2</td>
      <td>1.8</td>
      <td>1.8</td>
      <td>3.2</td>
      <td>2.4**</td>
      <td>2.6**</td>
      <td>4.1**</td>
    </tr>
    <tr>
      <td>X. laevis POU class 3 homeobox 2 (Pou3f2-b)</td>
      <td>Pou3f2b</td>
      <td>NM_001096751.1</td>
      <td>3</td>
      <td>2.3</td>
      <td>2.9</td>
      <td>3**</td>
      <td>2.6**</td>
      <td>2.7**</td>
    </tr>
    <tr>
      <td>X. laevis Mab-21-like 2 (Mab21l2-b)</td>
      <td>Mab21l2b</td>
      <td>NM_001096770.1</td>
      <td>-</td>
      <td>2.8</td>
      <td>2.9</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>T-cell leukemia homeobox 1 (Tlx1) transcript variant 1</td>
      <td>Tlx1</td>
      <td>XM_002936768.2</td>
      <td>2.6</td>
      <td>2.3</td>
      <td>2.6</td>
      <td>2.4**</td>
      <td>2.4**</td>
      <td>2.4**</td>
    </tr>
    <tr>
      <td>X. laevis empty spiracles homeobox 1 gene 2 (Emx1.2)</td>
      <td>Emx1.2</td>
      <td>NM_001093430.1</td>
      <td>2.6</td>
      <td>1.9</td>
      <td>1.1</td>
      <td>-</td>
      <td>-</td>
      <td>1.7**</td>
    </tr>
    <tr>
      <td>X. laevis SRY-box containing protein (Sox1)</td>
      <td>Sox1</td>
      <td>EF672727.1</td>
      <td>-</td>
      <td>2.6</td>
      <td>2.1</td>
      <td>-</td>
      <td>2**</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Single-minded homolog 1 (Sim1) transcript variant X2</td>
      <td>Sim1</td>
      <td>XM_004914545.1</td>
      <td>-</td>
      <td>1.4</td>
      <td>2.4</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>X. laevis SIX homeobox 1 (Six1)</td>
      <td>Six1</td>
      <td>AF279254.1</td>
      <td>1.4</td>
      <td>1.2</td>
      <td>2.3</td>
      <td>1.9**</td>
      <td>1.6**</td>
      <td>1.6**</td>
    </tr>
    <tr>
      <td>F-box protein 41 (Fbxo41)</td>
      <td>Fbxo41</td>
      <td>NM_001079043.1</td>
      <td>1.3</td>
      <td>0.6</td>
      <td>2</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>T-box 15 (Tbx15)</td>
      <td>Tbx15</td>
      <td>XM_002940981.2</td>
      <td>2</td>
      <td>1</td>
      <td>1.8</td>
      <td>2**</td>
      <td>1.4**</td>
      <td>1.7**</td>
    </tr>
    <tr>
      <td>X. laevis xRipply3 for xRipply3 protein</td>
      <td>Ripply3</td>
      <td>AB455086.1</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>2</td>
      <td>1.6**</td>
      <td>1.4**</td>
      <td>1.3**</td>
    </tr>
    <tr>
      <td>Early growth response 3 (Egr3)</td>
      <td>Egr3</td>
      <td>XM_002932703.2</td>
      <td>1.6</td>
      <td>0.8</td>
      <td>1.9</td>
      <td>1.7**</td>
      <td>1.3**</td>
      <td>1.9**</td>
    </tr>
    <tr>
      <td>SRY (sex determining region Y)-box 2 (Sox2)</td>
      <td>Sox2</td>
      <td>NM_213704.3</td>
      <td>1.1</td>
      <td>1.3</td>
      <td>1.9</td>
      <td>1.6**</td>
      <td>1.6**</td>
      <td>1.5**</td>
    </tr>
    <tr>
      <td>POU class 4 homeobox 1 (Pou4f1.2)</td>
      <td>Pou4f1.2</td>
      <td>NM_001097307.1</td>
      <td>1.3</td>
      <td>1</td>
      <td>1.9</td>
      <td>1.6**</td>
      <td>1.5**</td>
      <td>1.5**</td>
    </tr>
    <tr>
      <td>X. laevis for enhancer of split related 9 (Esr9 gene)</td>
      <td>Hes9.1a</td>
      <td>AJ009282.1</td>
      <td>1.7</td>
      <td>1.6</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ISL LIM homeobox 2 (Isl2)</td>
      <td>Isl2</td>
      <td>NM_001166041.1</td>
      <td>1.5</td>
      <td>-</td>
      <td>1.7</td>
      <td>1.6**</td>
      <td>1.1**</td>
      <td>1.4**</td>
    </tr>
    <tr>
      <td>X. laevis Tbx6 (Tbx6)</td>
      <td>Tbx6</td>
      <td>DQ355794.1</td>
      <td>1.4</td>
      <td>1.7</td>
      <td>1</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Protein FosB-like transcript variant X2</td>
      <td>FosB</td>
      <td>XM_004916957.1</td>
      <td>-</td>
      <td>1.7</td>
      <td>1.4</td>
      <td>-</td>
      <td>1.4**</td>
      <td>1.2**</td>
    </tr>
    <tr>
      <td>X. laevis Hes2</td>
      <td>Hes2</td>
      <td>BC084134.1</td>
      <td>1.7</td>
      <td>0.9</td>
      <td>1.3</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>cAMP responsive element modulator (Crem)</td>
      <td>Crem</td>
      <td>XM_002935162.2</td>
      <td>-</td>
      <td>1.4</td>
      <td>1.5</td>
      <td>-</td>
      <td>1.4**</td>
      <td>1.2**</td>
    </tr>
    <tr>
      <td>X. laevis zinc finger protein 214 (Znf214)</td>
      <td>Znf214</td>
      <td>NM_001097042.1</td>
      <td>1.2</td>
      <td>0.8</td>
      <td>1.5</td>
      <td>1.2**</td>
      <td>5.9**</td>
      <td>5.8**</td>
    </tr>
    <tr>
      <td>Xenopus laevis SRY (sex determining region Y)-box 21 (Sox21)</td>
      <td>Sox21</td>
      <td>NM_001172213.1</td>
      <td>1.2</td>
      <td>0.6</td>
      <td>1.5</td>
      <td>1.4**</td>
      <td>1.2**</td>
      <td>1.2**</td>
    </tr>
    <tr>
      <td>Atonal homolog 1 (Drosophila) (Atoh1)</td>
      <td>Atoh1</td>
      <td>XM_004911085.1</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>1.5</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>X. laevis Ets-2a proto-oncogene</td>
      <td>Ets2a</td>
      <td>BC133183.1</td>
      <td>1.3</td>
      <td>1</td>
      <td>1.4</td>
      <td>1.3**</td>
      <td>1.2**</td>
      <td>1.2**</td>
    </tr>
    <tr>
      <td>V-maf musculoaponeurotic fibrosarcoma oncogene homolog A (Mafa)</td>
      <td>Mafa</td>
      <td>NM_001032304.1</td>
      <td>1.4</td>
      <td>0.9</td>
      <td>1.1</td>
      <td>1.9**</td>
      <td>-</td>
      <td>1.8**</td>
    </tr>
    <tr>
      <td>X. laevis LIM class homeodomain protein</td>
      <td>Lhx5</td>
      <td>BC084744.1</td>
      <td>1.1</td>
      <td>-</td>
      <td>1.1</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Xenopus (Silurana) tropicalis neurogenin 1 (Neurog1)</td>
      <td>Ngn1</td>
      <td>NM_001123423.1</td>
      <td>0.8</td>
      <td>0.9</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>0.8**</td>
    </tr>
    <tr>
      <td>Xenopus laevis SOX3 protein</td>
      <td>Sox3</td>
      <td>BC072222.1</td>
      <td>0.5</td>
      <td>-</td>
      <td>0.9</td>
      <td>0.7</td>
      <td>0.7</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>

_*Log2 fold change values after Six1 overexpression (Six1i).† Log2 fold change values after Eya1 overexpression (Eya1i).‡ Log2 fold change values after Six1+Eya1 overexpression (Six1+ Eya1i).§ Log2 fold change values after overexpression of Six1 or Six1+Eya1 (Six1m).# Log2 fold change values after overexpression of Eya1 or Six1+Eya1 (Eya1m).¶ Log2 fold change values after overexpression of Six1 or Eya1 or Six1+Eya1 (Six1+Eya1m).** Denotes statistically supported data (q < 0.05)._

The expression of genes previously undescribed in Xenopus (Crem, FosB, Hes8, Isl2, Tbx15, Znf214) was fully characterised in neural fold, and early and late tail bud stages, along with those for which expression has been described for relatively few stages (Atoh1, Emx1.2, Gfi1a, Hes2, Hes9, Lhx5, Mab21l2b, Pou3f2b, Pou4f1.2, Ripply3, Sim1, Sox21, Tbx6, Tlx1) (summarised in Figure 4A–T; Figure 4—figure supplements 1–5). Genes with extensively characterised expression patterns (Ngn1 (Nieber et al., 2009); Six1 (Pandur and Moody, 2000); Six2 (Ghanbari et al., 2001); Sox2 (Mizuseki et al., 1998); Sox3 (Penzel et al., 1997); Sox17 (Hudson et al., 1997), MyoD1 (Hopwood et al., 1989), Sox1 (Nitta et al., 2006), Ets2a (Salanga et al., 2010), Mafa (Coolen et al., 2005)) are not shown here.

![Figure 4.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig4-v2.jpg)

**Figure 4.:** Genes expressed at neural plate stages (stages 14–18) are shown in panels A–L, and those only expressed at later stages are shown at mid/late tail bud stage (stages 28–32) in panels M–T. Several of the genes surveyed (Lhx5, Pou3f2b, Tbx15, Tbx6, Emx1.2 and Sim1 (A–D, M and N), were not expressed in the PPE, nor any placodal derivatives in later stages. Instead, such genes were expressed in the adjacent neural folds (Lhx5, Pou3f2b and Tbx15), ectoderm (Tbx6), or in the forebrain at later stages (Emx1.2). Several other genes were expressed broadly across the cranial ectoderm, at least partially overlapping with the PPE at neural plate stages (Ripply3, Crem, FosB and Znf214; E,O–Q), some of which are also maintained in placodal derivatives such as Znf214 in the otic vesicle (Q). The remaining genes (F–L, R–T) are expressed in parts of the PPE and maintained in some placodes (Hes2, Hes8, Hes9, Mab21l2b, Sox21, Isl2, Pou4f1.2, and Tlx1) or are expressed in a subset of placodes only (Atoh1, Gfi1a) (see Figure 4—figure supplements 1–4 for additional stages). Yellow arrows mark placodal expression. Arrowheads mark non-placodal expression. Abbreviations: pA: anterior placodal region; pAD: anterior lateral line placode; pE: epibranchial placode; pL: lens placode; L: lens; pM: middle lateral line placode; pO: olfactory placode; pP: posterior placodal region; pPrV: profundal/trigenimal placodes; vOt: otic vesicle. Plots U and V show qPCR after Six1 or Eya1 overexpression. Log2 fold change values were calculated from qPCR data obtained after overexpression of Six1-GR (U) or Eya1-GR (V) in placodal explants and are shown next to corresponding fold change values obtained from the RNA-Seq data. In all cases shown, qPCR values broadly corroborate those from the RNA-Seq data - showing up-regulation of target genes after either Six1 or Eya1 overexpression. Vertical error bars show the standard deviation of the mean of biological triplicates.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Expression dynamics for each target are shown across a range of developmental stages: A1–F1 show expression in neural plate stage embryos, A2–F2 show early tail bud stage embryos and A3–F3 show late tail bud stage embryos. (A) Expression of PPE marker gene Six1 is shown as reference for placodal domains (for details see Pandur and Moody, 2000; Schlosser and Ahrens, 2004). (B) Emx1.2 is expressed broadly in the neural plate in neural plate stages (B1), and becomes restricted to the forebrain in late tail bud stages (B3; asterisk). (C) Lhx5 is expressed in the forebrain at all developmental stages (C1–C3; asterisk), and at early and late tail bud stages Lhx5 is also expressed in the hindbrain and spinal cord (C3; arrowhead). (D) Pou3f2b is expressed in the neural plate and developing neural tube (D1; asterisk) at neural plate stages. Expression in the brain and spinal cord is maintained during early and late tail bud stages (D2 and D3 ; arrowhead and asterisk, respectively). (E) Tbx15 is expressed in a restricted domain of the anterolateral neural folds in neural plate stages (E1; asterisk). At tail bud stages expression is prominent in somites (E2 and E3; arrowhead) and migrating neural crest cells of the hyoid and first branchial neural crest streams (Nc). Both of these expression domains are maintained into late tail bud stages (E3 and E4). E4 shows section at the level indicated in E3 (dotted line). Bar in E4: 100 μm. (F) Throughout all developmental stages (F1–F3) Tbx6 is expressed strongly in the posterior paraxial and lateral plate mesoderm (F1 and F2; asterisk) with weaker expression in the pharyngeal arches (F2; arrowhead). Subsequently, it’s expressed in somites, as indicated by a diamond in F2. Abbreviations: pA: anterior placodal region; pAD: anterior lateral line placode; pE: epibranchial placode; pM: middle lateral line placode; pO: olfactory placode; vOt: otic vesicle; pPrV: profundal/trigeminal placodes.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Expression dynamics for each target are shown across a range of developmental stages: A1–E1 show expression in neural plate stage embryos, A2–E2 show early tail bud stage embryos and A3–E3 show late tail bud stage embryos. (A) Expression of PPE marker gene Six1 is shown as reference for placodal domains (for details see Pandur and Moody, 2000; Schlosser and Ahrens, 2004). (B) Crem is initially expressed broadly in paraxial mesoderm (B1; asterisk) and cranial ectoderm (B1; arrowhead) at neural plate stages and in pharyngeal arches and overlying ectoderm at early and late tail bud stages (B2 and B3 ; diamond). (C) FosB is expressed in a broad pattern across the cranial ectoderm and trunk mesoderm at both neural fold and early tail bud stages (C1 and C2). At late tail bud stages expression is maintained in cranial ectoderm as well as becoming apparent in the migrating neural crest cells (Nc) and weakly in the somites (C3; arrowhead). (D) Znf214 is expressed broadly across the ectoderm at all developmental stages (D1–D3). At both early and late tail bud stages there is expression in the migrating neural crest cells (Nc) as well as in the retina (D2 and D3; asterisk), and in late tail bud stages Znf214 is expressed in the otic vesicle and lens. (E) Ripply3 is expressed broadly in the posterior placodal region at neural fold stages (E1). At both early and late tail bud stages expression is confined to posterior cranial ectoderm (E2 and E3; asterisk). Yellow arrows mark placodal expression. Abbreviations: pA: anterior placodal region; pAD: anterior lateral line placode; pE: epibranchial placode; L: lens; pM: middle lateral line placode; pO: olfactory placode; vOt: otic vesicle; pP: posterior placodal region; pPrV: profundal/trigeminal placodes.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Expression dynamics for each target are shown across a range of developmental stages: A1–E1 show expression in neural plate stage embryos, A2–E2 show early tail bud stage embryos and A3–E3 show late tail bud stage embryos. (A) Expression of PPE marker gene Six1 is shown as reference for placodal domains (for details see Pandur and Moody, 2000; Schlosser and Ahrens, 2004). (B) Hes2 is expressed very strongly in a broad region corresponding to the posterior placodal domain including the prospective otic and lateral line placodes, as well as weakly in a scattered subset of neuroectodermal cells (B1; asterisk) at neural plate stages (see Figure 4—figure supplement 5 for section). Expression is later restricted to the otic vesicle and a new expression domain becomes established in the developing retina at early and late tail bud stages (B2 and B3; arrowhead). (C) During neural plate stages (C1), Hes8 is expressed in the developing profundal and trigeminal placodes as well as in the anterior placodal region, the anterior neural plate (C1 ; asterisk) and the primary neurons (motor neurons, intermediary neurons and sensory neurons) of the posterior neural plate (C1; arrowheads; see Figure 4— figure supplement 5 for section). In early tail bud stages (C2) trigeminal expression is lost and replaced by expression in the otic vesicle, as well as lateral line, epibranchial and olfactory placodes. Throughout late tail bud stages (C3), expression is maintained in these regions and the brain (C3; cross) and is initiated in the retina (C3; diamond). (D) During neural plate stages (D1), Hes9 is expressed in the developing profundal and trigeminal placodes as well as in the anterior placodal region, the anterior neural plate (D1; asterisk) and the primary neurons (motor neurons, intermediary neurons and sensory neurons) of the posterior neural plate (D1; arrowheads; see Figure 4—figure supplement 5 for section). In early tail bud stages (D2) trigeminal expression is lost but expression is apparent in the olfactory placodes, as well as in the otic and lateral line placodes and retina (D2; diamond). In late tail bud stages (D3) Hes9 is expressed broadly thoughout the brain (D3 ; cross), and is maintained in the lateral line and olfactory placodes as well as the otic vesicle. (E) During neural plate stages (E1), Mab21l2b is expressed in the prospective lens placode, as well as in the eye field (prospective retina) of the forebrain (E1; asterisk) and the prospective midbrain (E1; arrowhead). At early tail bud stages expression in the lens and midbrain is maintained and its expression becomes apparent in the hindbrain (E2; diamond). In late tail bud stages Mab21l2b is additionally prominently expressed in migrating neural crest cells (E3 ; Nc). (F) During neural plate stages Sox21 is expressed broadly throughout the anterior neural plate (F1; asterisk). At early tail bud stages (F2), this expression becomes confined to the forebrain (asterisk in F2) and midbrain-hindbrain boundary (arrowhead in F2) and is maintained into late tail bud stages, (F3). In late tail bud stages, Sox21 is also expressed in the olfactory placode, otic vesicle and becomes up-regulated in the hindbrain (F3; diamond). Yellow arrows mark placodal expression. Dotted lines in B1–D1 indicate levels of sections shown in Figure 4—figure supplement 5. Abbreviations: pA: anterior placodal region; pAD: anterior lateral line placode; pE: epibranchial placode; pLl: lateral line placodes; L: lens; pL: lens placode; pM: middle lateral line placode; pO: olfactory placode; vOt: otic vesicle; pP: posterior placodal region; pPrV: profundal/trigeminal placodes.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Expression dynamics for each target are shown across a range of developmental stages: A1–F1 show expression in neural plate stage embryos, A2–F2 show early tail bud stage embryos and A3–F3 show late tail bud stage embryos. B4–D4 and B5 –D5 shows sections at level indicated in B3–D3, respectively (dotted lines). (A) Expression of PPE marker gene Six1 is shown as reference for placodal domains (for details see Pandur and Moody, 2000; Schlosser and Ahrens, 2004). (B) Atoh1 is initially expressed at very low levels in presumptive otic placodes at neural plate stages (B1). This expression becomes more pronounced in the otic vesicle at early tail bud stages (B2) concomitant with the initiation of expression in lateral line ganglia and strong expression in the hindbrain (B2; asterisk). Expression becomes more pronounced in all three regions at late tail bud stages (B3 –B5). (C) Gfi1a is expressed at high levels in haematopoietic cells during neural plate stages (C1; asterisk). At early tail bud stages (C2) expression becomes more pronounced and diffuse, and expression is also initiated in the otic vesicle. At late tail bud stages Gfi1a is expressed in lateral line placodes as well as otic vesicles as the haematopoietic expression begins to subside (C3–C5). (D) During neural plate stages Isl2 is expressed in the profundal and trigeminal placodes and in the anterior placodal region along the anterior edge of the neural plate (D1). At early tail bud stages Isl2 expression is maintained in the profundal and trigeminal placodes/ganglia as well as in otic and lateral line placodes/ganglia and primary neurons in the spinal cord (D2; asterisk). Expression is maintained in cranial ganglia at late tail bud stages (D3–D5) and becomes apparent in the forebrain and lens (D3; arrowhead). (E) During neural plate stages Pou4f1.2 is expressed in the profundal and trigeminal placodes as well as in a stripe of primary sensory neurons (E1; asterisk; see Figure 4—figure supplement 5 for section). In early tail bud stages (E2) expression in the profundal/trigeminal placodes/ganglia and primary neurons is maintained, and expression in the otic and lateral line placodes is strengthened. Expression is maintained in all domains as well as in the cranial ganglia derived from placodes into late tail bud stages when expression becomes up-regulated in the retina (E3; diamond). Dotted line in E1 indicates the level of section shown in Figure 4— figure supplement 5. (F) Tlx1 is expressed in the presumptive ventral visceral arches at neural plate stages (F1; asterisk). This is maintained into early and late tail bud stages (F2 and F3), which also exhibit prominent expression in the profundal/trigeminal placodes and ganglia and the otic vesicle. Yellow and black arrows mark placodal expression. Bar in B4, C4 and D4: 100 μm (also for B5, C5 and D5, respectively). Abbreviations: pA: anterior placodal region; pAD: anterior lateral line placode; gAD: ganglion of the anterodorsal lateral line nerve; pE: epibranchial placode; pLl: lateral line placodes; L: lens; pL: lens placode; pM: middle lateral line placode; pO: olfactory placode; vOt: otic vesicle; pOt: presumptive otic placode; pPr: profundal placode; pP: posterior placodal region; pPL: posterior lateral line placode; pPrV: profundal/trigeminal placodes; pV: trigeminal placode; gV: ganglion of the trigeminal nerve.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** Neural crest and (NC) and neural plate (NP) domains are indicated. (A–D): Hes2 (A), Hes8 (B), Hes9 (C) and Pou4f1.2 (D) are all expressed in parts of the PPE (for level of sections see Figure 4 —figure supplements 3 and 4). While the exact boundaries of NC and NP cannot be determined in these sections, comparisons with sections through embryos stained by double in-situ-hybridisation for the PPE marker Six1 and the NP marker Sox3 (E) or Six1 and the NC marker FoxD3 (F) indicate that expression of each of these target genes is largely confined to the PPE although some overlap with the lateral NC region cannot be ruled out (E and F modified from Schlosser and Ahrens, 2004; Figure 6). Bar in A: 100 μm (also for B–F).

We found 19/30 (63.3% ) of these transcriptional regulators to be expressed in PPE or placodal derivatives, while 11/30 (Sox17, MyoD1, Sox1, Ets2a, Mafa, Emx1.2, Lhx5, Pou3f2b, Tbx6, Tbx15, Sim1) were not expressed in either the PPE or any placodal derivatives. However, many of the genes in the latter group were expressed in the adjacent neural folds or other tissues. Thus, it is possible that such genes may be direct targets of Six1 or Eya1 in domains surrounding the PPE, likely to have been included in our screen as a result of non-PPE contamination during dissection. Of the transcriptional regulators identified in our list of well-supported targets and expressed in the PPE or placodal derivatives 79% (15/19) were statistically supported in the analyses of merged datasets (Table 2). These included genes broadly expressed in cranial ectoderm including the PPE (Crem, FosB, Znf214, Ripply3), and genes expressed in the PPE or subdomains of the PPE and subsequently in some placodes (Hes2, Hes8, Hes9, Mab21l2b, Six1, Six2, Sox2, Sox3, Sox21, Atoh1, Ngn1, Gfi1a, Isl2, Pou4f1.2, Tlx1) (Figure 4A–T).

To begin to elucidate the GRN downstream of Six1 and Eya1 we chose ten transcription factors showing expression in posterior placodes (i.e. those derived from the posterior placodal area; the lateral line, otic and epibranchial placodes) for additional functional studies including genes implicated in the maintenance of neuronal progenitors (Sox2, Sox3, Hes8 and Hes9) as well as genes implicated in the regulation of sensory or neuronal differentiation (Atoh1, Gfi1a, Isl2, Ngn1, Pou4f1.2 and Tlx1). Selected genes were independently verified as being direct targets of either Six1 (Isl2) or of both Six1 and Eya1 (all other targets; Sox3 not analysed) in the PPE by qPCR, and the results were broadly consistent with the RNA-Seq data (Figure 4U and V).

### Six1 and Eya1 are required for expression of transcriptional regulators of neurogenesis in the PPE and placodes

To explore whether Six1 or Eya1 were required for the expression of selected target genes, the expression of each target was analysed by in-situ-hybridisation after MO-mediated knockdown of Six1 or Eya1. The efficacy and specificity of both co-injected Six1-MOs (Six1-MO1 and Six1-MO2; Brugmann et al., 2004) and Eya1-MOs (Eya1-MO1 and Eya1-MO2; Schlosser et al., 2008) have been previously reported. Compared to injection with a control MO (Eya1-mmMO with 5 mismatches relative to Eya1-MO2), knockdown of either Six1 or Eya1 significantly reduced the expression of all direct target genes in PPE or placodes, demonstrating that both Six1 and Eya1 are required for their expression (Figure 5 and Figure 5—figure supplement 1; Table 3). To control for off-target effects associated with MO use, target gene expression was also analysed after overexpression of a dominant-negative version of Six1 (Six1-EnR; Brugmann et al., 2004). Expression patterns of all target genes were highly similar to those seen after MO-knockdown of either Six1 or Eya1, suggesting that the observed reductions in expression were caused by Six1 or Eya1 knockdown as opposed to being an artefact of MO use (Figure 5—figure supplement 2). Taken together, these findings show that Six1 and Eya1 are essential direct upstream regulators of multiple genes encoding transcription factors that promote neuro- and sensorigenesis in the PPE and placodes.

![Figure 5.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig5-v2.jpg)

**Figure 5.:** Tail bud (A–G) and neural plate (H–I) stage embryos after unilateral injection of Eya1-MO1+2. In each case, lacZ was co-injected as a lineage tracer and panels A1–G1 show the control (un-injected) side and A2–G2 show the injected side (lacZ staining out of frame in most specimens). The injected side is positioned to the right in H–J, as marked by blue lacZ staining. Arrows and arrowheads mark reductions in marker gene expression in placodal and non-placodal derivatives, respectively.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Tail bud stage (A–G) and neural plate stage (H–J) embryos after unilateral injection of Six1-MO1+2. In each case, lacZ was co-injected as a lineage tracer and panels A1–G1 show the control (un-injected) side and A2–G2 show the injected side. The injected side is positioned to the right in H–J, as marked by blue lacZ staining (lacZ staining out of frame in some specimens). Arrows mark reductions in marker gene expression in placodal derivatives, and asterisks indicate increased expression.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Tail bud stage (A–C) and neural plate stage (D–I) embryos after unilateral injection of Six1-EnR. In each case, lacZ was co-injected as a lineage tracer and panels A1–C1 show the control (un-injected) side and A2–C2 show the injected side. The injected side is positioned to the right in D–I, as marked by blue lacZ staining (lacZ staining out of frame in some specimens). Arrows mark reductions in marker gene expression in placodal derivatives, and asterisks indicate increased expression.

**Table 3.**
 Changes in marker gene expression in the placodes after injection of various constructs.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Injection</th>
      <th>Six1-MO*</th>
      <th>Eya1-MO*</th>
      <th>Six1-EnR</th>
      <th>Eya1-mmMO</th>
      <th>Six1-GR§</th>
      <th>Eya1-GR§</th>
    </tr>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Phenotype</th>
      <th>%</th>
      <th>%</th>
      <th>%</th>
      <th>%</th>
      <th>%</th>
      <th>%</th>
    </tr>
    <tr>
      <th>(n)</th>
      <th>(n)</th>
      <th>(n)</th>
      <th>(n)</th>
      <th>(n)</th>
      <th>(n)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Atoh1</td>
      <td rowspan="2">Reduced</td>
      <td>77**</td>
      <td>90‡</td>
      <td>94</td>
      <td>10</td>
      <td>26</td>
      <td>42</td>
    </tr>
    <tr>
      <td>(26)</td>
      <td>(20)</td>
      <td>(18)</td>
      <td>(21)</td>
      <td>(19)</td>
      <td>(12)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>35</td>
      <td>42</td>
    </tr>
    <tr>
      <td>(26)</td>
      <td>(20)</td>
      <td>(18)</td>
      <td>(21)</td>
      <td>(17)</td>
      <td>(12)</td>
    </tr>
    <tr>
      <td rowspan="4">Gfi1a</td>
      <td rowspan="2">Reduced</td>
      <td>82†</td>
      <td>67†</td>
      <td>69</td>
      <td>31</td>
      <td>57</td>
      <td>36</td>
    </tr>
    <tr>
      <td>(27)</td>
      <td>(17)</td>
      <td>(16)</td>
      <td>(26)</td>
      <td>(14)</td>
      <td>(14)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>43</td>
    </tr>
    <tr>
      <td>(27)</td>
      <td>(17)</td>
      <td>(16)</td>
      <td>(26)</td>
      <td>(14)</td>
      <td>(14)</td>
    </tr>
    <tr>
      <td rowspan="4">Hes8</td>
      <td rowspan="2">Reduced</td>
      <td>74‡</td>
      <td>83‡</td>
      <td>70</td>
      <td>17</td>
      <td>60</td>
      <td>57</td>
    </tr>
    <tr>
      <td>(35)</td>
      <td>(35)</td>
      <td>(46)</td>
      <td>(24)</td>
      <td>(40)</td>
      <td>(56)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>0</td>
      <td>24</td>
      <td>0</td>
      <td>15</td>
      <td>29</td>
    </tr>
    <tr>
      <td>(35)</td>
      <td>(35)</td>
      <td>(46)</td>
      <td>(24)</td>
      <td>(40)</td>
      <td>(56)</td>
    </tr>
    <tr>
      <td rowspan="4">Hes9</td>
      <td rowspan="2">Reduced</td>
      <td>73‡</td>
      <td>76‡</td>
      <td>84</td>
      <td>11</td>
      <td>75</td>
      <td>29</td>
    </tr>
    <tr>
      <td>(45)</td>
      <td>(33)</td>
      <td>(38)</td>
      <td>(27)</td>
      <td>(12)</td>
      <td>(29)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>(45)</td>
      <td>(33)</td>
      <td>(38)</td>
      <td>(27)</td>
      <td>(12)</td>
      <td>(29)</td>
    </tr>
    <tr>
      <td rowspan="4">Isl2</td>
      <td rowspan="2">Reduced</td>
      <td>66†</td>
      <td>100‡</td>
      <td>nd</td>
      <td>27</td>
      <td>50</td>
      <td>24</td>
    </tr>
    <tr>
      <td>(38)</td>
      <td>(17)</td>
      <td>nd</td>
      <td>(22)</td>
      <td>(18)</td>
      <td>(17)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>6</td>
      <td>0</td>
      <td>nd</td>
      <td>0</td>
      <td>31</td>
      <td>41</td>
    </tr>
    <tr>
      <td>(38)</td>
      <td>(17)</td>
      <td>nd</td>
      <td>(22)</td>
      <td>(16)</td>
      <td>(17)</td>
    </tr>
    <tr>
      <td rowspan="4">Ngn1</td>
      <td rowspan="2">Reduced</td>
      <td>65‡</td>
      <td>49†</td>
      <td>84</td>
      <td>17</td>
      <td>17</td>
      <td>36</td>
    </tr>
    <tr>
      <td>(51)</td>
      <td>(43)</td>
      <td>(31)</td>
      <td>(24)</td>
      <td>(30)</td>
      <td>(59)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>16</td>
      <td>6</td>
      <td>4</td>
      <td>23</td>
      <td>41</td>
    </tr>
    <tr>
      <td>(51)</td>
      <td>(43)</td>
      <td>(31)</td>
      <td>(24)</td>
      <td>(30)</td>
      <td>(59)</td>
    </tr>
    <tr>
      <td rowspan="4">Pou4f1.2</td>
      <td rowspan="2">Reduced</td>
      <td>67‡</td>
      <td>63†</td>
      <td>71</td>
      <td>16</td>
      <td>47</td>
      <td>81</td>
    </tr>
    <tr>
      <td>(48)</td>
      <td>(30)</td>
      <td>(35)</td>
      <td>(19)</td>
      <td>(15)</td>
      <td>(37)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
    </tr>
    <tr>
      <td>(48)</td>
      <td>(30)</td>
      <td>(35)</td>
      <td>(19)</td>
      <td>(15)</td>
      <td>(37)</td>
    </tr>
    <tr>
      <td rowspan="4">Sox2</td>
      <td rowspan="2">Reduced</td>
      <td>74‡</td>
      <td>78‡</td>
      <td>87</td>
      <td>6</td>
      <td>90</td>
      <td>48</td>
    </tr>
    <tr>
      <td>(19)</td>
      <td>(18)</td>
      <td>(30)</td>
      <td>(16)</td>
      <td>(21)</td>
      <td>(33)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>0</td>
      <td>23#</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
    </tr>
    <tr>
      <td>(19)</td>
      <td>(18)</td>
      <td>(30)</td>
      <td>(16)</td>
      <td>(21)</td>
      <td>(33)</td>
    </tr>
    <tr>
      <td rowspan="4">Sox3</td>
      <td rowspan="2">Reduced</td>
      <td>68‡</td>
      <td>54†</td>
      <td>39</td>
      <td>9</td>
      <td>49</td>
      <td>40</td>
    </tr>
    <tr>
      <td>(25)</td>
      <td>(26)</td>
      <td>(31)</td>
      <td>(22)</td>
      <td>(25)</td>
      <td>(23)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>0</td>
      <td>0</td>
      <td>71#</td>
      <td>0</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <td>(25)</td>
      <td>(26)</td>
      <td>(31)</td>
      <td>(22)</td>
      <td>(25)</td>
      <td>(23)</td>
    </tr>
    <tr>
      <td rowspan="4">Tlx1</td>
      <td rowspan="2">Reduced</td>
      <td>84†</td>
      <td>91‡</td>
      <td>100</td>
      <td>33</td>
      <td>40</td>
      <td>7</td>
    </tr>
    <tr>
      <td>(31)</td>
      <td>(32)</td>
      <td>(13)</td>
      <td>(15)</td>
      <td>(10)</td>
      <td>(15)</td>
    </tr>
    <tr>
      <td rowspan="2">Increased</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>73</td>
    </tr>
    <tr>
      <td>(31)</td>
      <td>(32)</td>
      <td>(13)</td>
      <td>(15)</td>
      <td>(10)</td>
      <td>(15)</td>
    </tr>
  </tbody>
</table>

_* Significant differences (Fisher’s exact test);† p<0.05,‡ p<0.001) to Eya1-mmMO injections are indicated.§ Dexamethasone treatment from stages 16–18 on.# Expression ectopic in epidermis.n: Number of embryos analysed at both neural plate (stage 14–16) and tail bud (stage 21–26) stage.nd: Not determined._

### Six1 and Eya1 affect expression of presumptive direct target genes in complex ways

To complement the loss-of-function studies, and to examine the spatial distribution of presumptive direct targets of Six1 and Eya1 in gain-of-function experiments, we injected Six1-GR and Eya1-GR individually and, to ensure that overexpression did not affect early embryogenesis, induced their nuclear translocation by adding DEX at neural fold stage (stages 16–18), after PPE commitment (Ahrens and Schlosser, 2005). Surprisingly, although injection of Six1-GR or Eya1-GR resulted in up-regulation of direct targets in a minority of cases (Table 3; Figures 6 and 7), the dominant observed phenotype was down-regulation of target gene expression in the PPE or placodes (Table 3; Figures 8 and 9). Considering that here, unlike in the initial RNA-Seq screen and qPCR experiments, CHX was not used to block protein synthesis, these results indicate that Six1 and Eya1 additionally affect expression of many of their direct target genes in indirect and partly opposing ways.

![Figure 6.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig6-v2.jpg)

**Figure 6.:** Tail bud stage embryos (A–F) after unilateral injection of Six1-GR and DEX induction at neural plate stage (16–18). In each case, lacZ was co-injected as a lineage tracer and panels A1–F1 show the control (un-injected) side and A2–F2 show the injected side. Arrows and arrowheads mark expansions in marker gene expression in placodal and non-placodal derivatives, respectively.

![Figure 7.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig7-v2.jpg)

**Figure 7.:** Tail bud stage embryos (A–G) after unilateral injection of Eya1-GR and DEX induction at neural plate stage (16–18). In each case, lacZ was co-injected as a lineage tracer and panels A1–G1 show the control (un-injected) side and A2–G2 show the injected side. Arrows and arrowheads mark expansions in marker gene expression in placodal and non-placodal derivatives, respectively.

![Figure 8.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig8-v2.jpg)

**Figure 8.:** Tail bud stage embryos (A–H) after unilateral injection of Six1-GR and DEX induction at neural plate stage (16–18). In each case, lacZ was co-injected as a lineage tracer and panels A1–H1 show the control (un-injected) side and A2–H2 show the injected side. Arrows mark reductions in marker gene expression in placodal derivatives.

![Figure 9.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig9-v2.jpg)

**Figure 9.:** Tail bud stage embryos (A–J) after unilateral injection of Eya1-GR and DEX induction at neural plate stage (16–18). In each case, lacZ was co-injected as a lineage tracer and panels A1–J1 show the control (un-injected) side and A2–J2 show the injected side. Arrows mark reductions in marker gene expression in placodal derivatives.

## Discussion

Overexpression of GR-fusion constructs followed by DEX-induced nuclear translocation in the presence of protein synthesis inhibitors has been previously used successfully to screen for direct target genes of transcription factors or cofactors in Xenopus (Kolm and Sive, 1995; Taverner et al., 2005; Seo et al., 2007). Here, we combine this approach with high-throughput sequencing of tissue-specific RNA to identify several hundred novel presumptive direct target genes of Six1 and Eya1 in the PPE. We show that this strategy indeed recovers the majority of direct Six1 target genes known from previous studies, indicating its reliability. Our in situ and qPCR analyses of target genes predicted from the RNA-Seq screen also provided independent verification of selected target genes suggesting a low false discovery rate. Moreover, the expression of all genes selected for detailed analysis proved to be dependent on Six1 and Eya1 in the PPE, indicating that many genes our screen predicted as Six1/Eya1 targets are also functionally dependent on these upstream regulators in the PPE. A comparison of our data set with recently identified direct target genes of sine oculis, the Six1 orthologue in the developing eye of Drosophila (Jusiak et al., 2014; Jin et al., 2016) also reveals that homologues to six out of the 12 sine oculis target genes identified with high confidence in Jin et al. (2016) are differentially expressed in our Sixi or Six1+Eya1i (and often also in Eya1i) treatment groups, viz. Six1 and Six2; Eya4; Shh; various matrix metalloproteases (e.g. MMP9); Ets2; and Frizzled1 and Frizzled4. This suggests that a relatively high proportion of Six1 target genes may be evolutionarily conserved.

Our finding that many of the presumptive direct target genes of Six1 or Eya1 are not up-regulated in the absence of CHX indicates that without blocking protein synthesis it is not possible to reliably identify direct target genes, presumably due to the existence of indirect interactions with such targets. We believe that this is one of the reasons why our findings differ substantially from the study of Yan et al. (2015), which analysed differentially expressed genes in Xenopus animal cap explants after overexpression of Six1 without first blocking protein synthesis. None of the transcription factors in our prioritised list was identified in the study by Yan et al. (2015); and we found none of the transcription factors differentially expressed in their study. A second likely reason for the discrepancy between the results presented here and in Yan et al. (2015) is that, while we specifically analysed PPE tissue (presumably containing tissue-specific cofactors required for the activation or repression of Six1 and Eya1 target genes specific for the developing placodes), they analysed target genes in animal cap tissue, known to be composed of pluripotent cells.

Previous studies have shown that Six1 and Eya1 are essential for both the establishment of the PPE (Brugmann et al., 2004; Christophorou et al., 2009), as well as for the subsequent development of placode-derived sense organs (Xu et al., 1999; Laclef et al., 2003; Zheng et al., 2003; Brugmann et al., 2004; Zou et al., 2004; Kozlowski et al., 2005; Schlosser et al., 2008; Ahmed et al., 2012b, 2012a) but the mechanisms through which they act are poorly understood. The continued expression of both genes in almost all placodes developing from the PPE (Schlosser and Ahrens, 2004), combined with the observed deficiencies in derivatives from most placodes after loss-of-function of either Six1 or Eya1, indicates that they play a role in generic aspects of placode development shared by all placodes. Indeed, our data show that genes revealed as presumptive direct targets of Six1 and Eya1 were highly enriched for GO terms associated with neurogenesis and placode development. Our screen also confirms previous studies suggesting that Six1 and Eya1 synergistically regulate many genes in the PPE, and that the Six1-Eya1 protein complex predominantly acts by activating transcription (Li et al., 2003; Brugmann et al., 2004). However, we also find support for independent action of Six1 and Eya1 in the PPE, possibly in conjunction with other interacting partners (Brugmann et al., 2004; Ahmed et al., 2012a). Surprisingly, we found Hox genes to be strongly enriched in the list of target genes activated by Eya1 only. This deserves further study since Eya1 has not previously been recognised as an upstream regulator of Hox genes.

It has previously been suggested (Schlosser, 2006) that a generic role of Six1 and Eya1 for all placodes could be implemented in two possible ways: (1) By the direct contribution to the activation of genes regulating developmental processes shared between different placodes such as proliferation, morphogenetic movements and neuronal or sensory cytodifferentiation; or (2) by direct contribution to the activation of genes defining the identity of different individual placodes within the PPE. Our data strongly suggest that Six1 and Eya1 act predominantly in the first rather than in the second mode. A large number of transcription factor encoding genes, including several Pax, Pitx, ANF and FoxI genes, have been implicated in conferring identity to individual placodes, or groups of placodes, within the PPE (reviewed in Schlosser, 2006, 2010; Grocott et al., 2012; Saint-Jeannet and Moody, 2014) however only a few of these genes were recovered as targets of Six1 or Eya1, e.g. Gbx2 (FC 1.7 in Six1+Eya1i) and FoxI4 (FC 1.09 in Six1i). In contrast, we found a large number of genes encoding transcription factors with roles in neuronal/sensory cytodifferentiation but also other proteins with likely roles for the maintenance of proliferating progenitors (e.g. Cyclin D, RGCC), the regulation of cell adhesion and morphogenetic movements (e.g. EDAR, CXCR7, Protocadherin11, RhoV, Claudin3) and cytodifferentiation (e.g. Espin, Neurotrophin3). This suggests that, similar to Hox or Pax genes, Six1 and Eya1 act as both master genes and micro-managers (Akam, 1998; Thompson and Ziman, 2011; Rezsohazy et al., 2015), acting upstream of a GRN co-ordinating cell differentiation in the PPE as well as directly activating terminal differentiation gene batteries.

Considering that Six1 and Eya1 have previously been shown to promote a proliferative progenitor state at high doses but neuronal and sensory differentiation at lower doses (Schlosser et al., 2008), it is particularly interesting that we identified presumptive direct target genes encoding transcription factors previously implicated in progenitor maintenance (Sox2, Sox3, Hes8, Hes9) and differentiation (Ngn1, Atoh1, POU4f1, Gfi1a, Isl2, Tlx1). Both Hes (Hes8, Hes9) and SoxB1 (Sox2, Sox3) proteins are known to keep progenitor cells in an undifferentiated state, and must be down-regulated for neuronal differentiation to proceed. While Sox2 and Sox3 play multiple roles including activity as pioneer factors, which open up chromatin for transcription (Bylund et al., 2003; Graham et al., 2003; Pevny and Placzek, 2005; Bergsland et al., 2011), Hes proteins generally repress neuronal/sensory determination genes such as Ngn1 or Atoh1 as effectors of Notch signalling (Kobayashi and Kageyama, 2014; Su et al., 2015; Abdolazimi et al., 2016). Conversely, Ngn1 and Atoh1 are known to act as proneural factors that initiate differentiation of sensory neurons and hair cells, respectively (Ma et al., 1996, 1998; Bermingham et al., 1999; Millimaki et al., 2007), whereas POU4f1 (previously known as Brn3a), Gfi1a, Isl2 and Tlx1 act further downstream in differentiation of sensory neurons (Patterson and Krieg, 1999; Wallis et al., 2003; Cheng et al., 2004; Eng et al., 2004; Lanier et al., 2009; Dykes et al., 2011), and Gfi1a and the related POU domain factor POU4f3 (or Brn3c) are required for hair cell maintenance and survival (Xiang et al., 1998; Wallis et al., 2003). Our findings strongly indicate that Six1 and Eya1 directly promote multiple steps during sensory and neuronal development, and act to drive both progenitor maintenance and neuronal differentiation programmes in placodes (summarised in Figure 10), although further functional studies are needed to clarify the mechanism allowing Six1 and Eya1 to maintain the balance between activation of progenitor and differentiation genes. Additionally, direct binding of Six1 to regulatory regions of targets identified in this study should be confirmed by methods such as ChIP-Seq.

![Figure 10.](https://cdn.elifesciences.org/articles/17666/elife-17666-fig10-v2.jpg)

**Figure 10.:** Six1/Eya1 act to promote neuronal differentiation, by activation of pro-neural genes (Ngn1, Atoh1), as well as progenitor state maintenance, by activation of genes such as SoxB1 and Hes genes. Arrows indicate direct (solid line) and indirect (dotted line) activation; barred lines show direct (solid line) and indirect (dotted line) repression. Evidence for interactions: Six1 positively autoregulates (Sato et al., 2012); Six1/Eya1 directly activate Sox2, Sox3, Hes8, Hes9, Ngn1, Atoh1, Isl2, Pou4f1.2, Tlx1 and Gfi1a (this study); Sox2 synergises with Six1/Eya1 (Ahmed et al., 2012b, 2012a); Sox2 directly activates Atoh1 (Ahmed et al., 2012a) and Ngn1 (Cimadamore et al., 2011); Atoh1 and Ngn1 indirectly repress each other (Gowan et al., 2001); Ngn1 indirectly represses Sox2 (Evsen et al., 2013); Ngn1 directly activates NeuroD1 (Seo et al., 2007); Atoh1 positively autoregulates (Helms et al., 2000); Atoh1 indirectly represses Sox2 (Neves et al., 2012) and activates Gfi1 (Wallis et al., 2003); NeuroD1 directly activates Pou4f1.2 (Hutcheson and Vetter, 2001) and Isl1 (Lee et al., 1995); Pou4f1.2 directly activates Gfi1 (Hertzano et al., 2004) and indirectly activates Tlx1 (Hutcheson and Vetter, 2001).

The analysis of Six1 and Eya1 presumptive direct target genes presented here establishes a GRN regulating the development of cranial vertebrate sensory organs and neurons from the PPE (Figure 10), and identifies a large number of novel putative direct target genes encoding a diverse array of proteins. Among these are many promising candidates potentially involved in mediating the effects of Six1 or Eya1 on proliferation, morphogenesis and cytodifferentiation in developing placodes. This makes our data an invaluable repository of information for designing further functional studies on early sensory development in vertebrates. Finally, while our study focussed on the role of Six1 and Eya1 during sensory development, cell proliferation, morphogenesis and cytodifferentiation are also known to be affected in human patients in which Six1 and Eya1 are dysregulated, leading to sensory deficits after Six1 or Eya1 loss of function mutations (Kochhar et al., 2007) or enhanced tumour progression after Six1 or Eya1 up-regulation (Blevins et al., 2015; Liu et al., 2016). This suggests that many target genes identified in our study may also be misregulated in these diseases, potentially opening up exciting new avenues for therapeutic intervention.

## Materials and methods

### Expression constructs and morpholinos

Capped RNAs of Xenopus Six1-GR, Eya1-GR and Six1-EnR were made by in vitro transcription using the mMessage mMachine SP6 kit (Ambion, Austin, Texas) from the following templates: pCS2+-GR-myc-Six1, pCS2+-GR-myc-Eya1α (Schlosser et al., 2008) and pCS2-EnR-Six1 (Brugmann et al., 2004).

Translation blocking morpholinos (MO) for Six1 (Six1-MO1: 5’-GGAAGGCAGCATAGACATGGCTCAG-3’; Six1-MO2: 5’-CGCACACGCAAACACATACACGGG-3’) and Eya1 (Eya1-MO1: 5’-TACTATGTGGACTGGTTAGATCCTG-3’; Eya1-MO2: 5’-ATATTTGTTCTGTCAGTGGCAAGTC-3’) were previously described (Brugmann et al., 2004; Schlosser et al., 2008). An Eya1-MO carrying 5 mismatches was used as a control (Eya1-mmMO; mismatches shown in lower case: 5’-ATtTTaGTTCTGaCAGTGGgAAcTC-3’).

### Microinjection

Six1-GR (500 pg), Eya1-GR, (500 pg), Six1-EnR (100 pg) mRNAs and Six1-MO1+2 (2 ng), Eya1-MO1+2 (2 ng), and Eya1-mismatch-MO (2 ng) were freshly prepared before each injection. lacZ (250 pg) or myc-GFP (125 pg) mRNAs were co-injected to mark the injected side. Embryos of Xenopus laevis were obtained by in vitro fertilisation, staged according to (Nieuwkoop and Faber, 1967) and injected unilaterally into two-cell blastomeres according to standard procedures (Sive et al., 2000). Six1-EnR was injected at the four-cell stage into single blastomeres that give rise to the dorsal ectoderm as previously described (Brugmann et al., 2004).

### Conditional overexpression of GR-fusion constructs and isolation of placodal RNA

To obtain RNA for RNA-Seq or qPCR, both blastomeres of two-cell stage embryos were injected with either 1) Six1-GR (500 pg) + myc-GFP (125 pg), 2) Eya1-GR (500 pg) + myc-GFP (125 pg), or 3) Six1-GR (500 pg) + Eya1-GR (500 pg) + myc-GFP (125 pg). Each of these treatment groups was allowed to develop to early neural plate stage before being sorted under a fluorescent microscope. The lateral part of the preplacodal region (LPR of Ahrens and Schlosser, 2005) was explanted from GFP positive embryos (~100 per biological replicate) in 1 × MBSH (Sive et al., 2000) supplemented with 2 mM CaCl2, 25 mg/l gentamycine (Sigma, St Louis, Missouri), 400 mg/l penicillin (Sigma), and 400 mg/l streptomycin sulphate (Sigma). Explants were pre-treated with 0.1 × modified Barth’s solution (MBS; Sive et al., 2000) with cycloheximide (CHX; final concentration 10 μg/ml) for 30 min at 25°C. After pre-treatment, 50% of the explants were transferred to 0.1 × MBS with CHX + dexamethasone (DEX; final concentration 10 μM) and incubated for 2 hr 30 at 25°C (Figure 1) when control embryos had reached stage 20. Explants were immediately homogenised in Trizol (Invitrogen, Carlsbad, California) and total RNAs extracted. Isolated RNA was quality assayed in an Agilent 2100 Bioanalyzer and all samples used for sequencing had an RIN >7.0.

### RNA-sequencing, mapping and annotation

Libraries were prepared from 1 mg total RNAs and subjected to deep sequencing with Illumina Hi-Seq1000 at the EMBL Genecore facility. Paired-end (100 bp) sequence reads were quality-filtered using Trimmomatic (Bolger et al., 2014), and mapped to the Xenopus laevis genome (XL7.0) with Bowtie2 (version 2.2.5; Langmead and Salzberg, 2012) and Tophat2; (version 2.0.13; Kim et al., 2013). An average of 65 million reads (~80% of quality filtered reads) were mapped with 90% of reads properly paired in sequencing across treatment groups. Transcript models were assembled using Cufflinks2 (version 2.1.1; Trapnell et al., 2012), and differential expression was determined using Cuffdiff2 (version 2.1.1; Trapnell et al., 2012). Gene models were annotated against a combined Xenopus mRNA database (X. laevis: ftp://ftp.xenbase.org/pub/Genomics/Sequences/xlaevisMRNA.fasta; X. tropicalis: ftp://ftp.xenbase.org/pub/Genomics/Sequences/xtropMRNA.fasta) using blastn with an e-value cut-off of 1E-5. Using this approach we were able to annotate an average of 80% of mapped reads.

### Differential expression analysis for individual treatment groups

Initially, two samples of CHX- and CHX+DEX-treated explants were independently collected, sequenced and mapped for each treatment group (injection of Six1-GR, Eya1-GR or Six1-GR+Eya1-GR), and were specified as two biological replicates in Cuffdiff. To preclude the inclusion of genes affected by DEX treatment alone, we also analysed explants taken from un-injected embryos and treated as above (CHX vs. CHX+DEX). Two biological replicates of this control treatment group were included in sequencing. Presumptive direct targets of Six1, Eya1 or Six1+Eya1 were determined by comparing Six1-GR, Eya1-GR or Six1-GR+Eya1-GR-injected embryos treated with CHX (as controls) against CHX+DEX-treated samples. Genes were considered to be differentially expressed if (1) the FPKM (Fragments Per Kilobase of exon per Million fragments mapped) for that gene was >1 in the CHX+DEX treatment group, (2) the gene was at least two-fold up-/down-regulated after CHX+DEX treatment compared to CHX treatment, (3) there was at least a two-fold difference between the control (un-injected) and experimental (injected with either Six1-GR, Eya1-GR or Six1-GR+Eya1-GR) fold change (FC) values in response to DEX treatment. The Pearson correlation was high for each of the treatment groups (>0.9 for all pairwise comparisons), indicating the similarity of expression profiles between independently treated samples.

### Re-analysis of differential expression for combined treatment groups

As a second approach to finding genes that showed differential expression in response to DEX treatment, RNA-Seq data of several treatment groups were merged to add statistical power to the analysis. In one analysis, all replicates from our three different treatment groups were considered as equivalent to focus on genes with similar differential expression profiles across all treatment groups (comprising the Six1+Eya1m dataset with six replicates). In another analysis, all treatment groups involving Six1 overexpression (i.e. injection of Six1-GR alone or Six1-GR+Eya1-GR: Six1m with 4 replicates) were treated as equivalent as were all treatment groups involving Eya1 overexpression (Eya1-GR, Six1-GR+Eya1-GR: Eya1m with 4 replicates). This allowed us to focus on genes whose activation was limited by either Six1 or Eya1 levels. We considered a gene to be significantly differentially expressed if it passed Cuffdiff’s statistical test (q < 0.05) in addition to meeting the criteria outlined above.

### Gene set enrichment analysis (GSEA) and Gene Ontology

Xenopus annotations were converted to their human orthologs from the Human Uniprot database, and functionally annotated using the online tools ‘PantherDB’ (Mi et al., 2013; http://pantherdb.org) and ‘DAVID’ (Huang et al., 2009; https://david.ncifcrf.gov). For GSEA of placodal transcriptomes after injection of Six1 and/or Eya1, the placodal transcriptome of un-injected, CHX treated placodal explants was specified as a background set, whereas GSEA of the transcriptome of untreated explants was conducted using the default 'human dataset' in DAVID as background. The enrichment score (E) for each group is reported as the geometric mean of the EASE scores (a modified Fisher’s exact score) that are associated with the enriched annotation terms belonging to that group (Huang et al., 2007).

### cDNA synthesis and qPCR

RNA was extracted from explants after CHX or CHX+DEX treatment as detailed above. cDNA was synthesised using the QuantiTect Reverse Transcription Kit (Qiagen, Hilden, Germany), using 500 ng total RNA according to the manufacturer’s protocol. qPCR was performed using Taqman reagents on a StepOne Plus machine (Applied Biosystems, Foster City, California), using Smn2 as a reference (Dhorne-Pollet et al., 2013; Supplementary file 4). qPCR was performed in triplicate and the entire experiment was repeated three times from independently prepared RNA. Relative Quantification (RQ) values and log2 fold change (FC) were averaged across biological replicates.

### Subcloning and gene synthesis

The full coding region of Hes8, Crem, FosB, Tbx15, Atoh1 and Isl2 was synthesised from transcript models from RNA-Seq data (KT722743; KT722744; KT722745; KT722746; KT722747; KT722748) by Genescript into the cloning vector pUC57 and subsequently sub-cloned into the expression vector pCS2+ using the following restriction sites: Hes8 and Crem: ClaI/EcoRI; Atoh1: XbaI; Tbx15 and FosB: BamHI/EcoRI; Isl2: EcoRI/StuI. Primers with added ClaI and EcoRI sites (to the forward and reverse primers, respectively) were designed (Supplementary file 4) to amplify the entire coding region of Tbx6, which was then subcloned into pCS2+ between the ClaI/EcoRI sites. Znf214, Mab21l2-b and Pou3f2b were ordered (pCMV-SPORT6, Fisher Scientific, Waltham, Massachusetts; Clone IDS: 5512398, 5515985 and 4203106).

Hes9 (pCR4-TOPO) was ordered from Source Bioscience (Clone accession: BC169570) and was subcloned into the EcoRI site of pCS2+.

### In-situ-hybridisation

Embryos injected with myc-GFP were sorted under a fluorescent microscope and fixed using a standard protocol (Sive et al., 2000). LacZ-injected embryos were fixed and then stained with X-gal solution to reveal lacZ. Wholemount in-situ-hybridisation was carried out under high stringency conditions at 60°C as previously described (Harland, 1991) using digoxigenin-labelled antisense probes. Probes for Six1 (Pandur and Moody, 2000), N-tubulin (Oschwald et al., 1991 Sox2 (De Robertis et al., 1997), Sox3 (Penzel et al., 1997), Ripply3 (Janesick et al., 2012), Hes2 (Sölter et al., 2006), Sim1 (Martin et al., 2007), Gbx2 (von Bubnoff et al., 1996), Lhx5 (Bachy et al., 2001), Sox21 (Cunningham et al., 2008), Emx1.2 (Green and Vetter, 2011), Pou4f1.2 (Hutcheson and Vetter, 2001), and Tlx1 (Patterson and Krieg, 1999) were synthesised as previously described. Primers were designed with promoter sites added (forward, T7; reverse, SP6) for Hes8, Hes9, Gfi1a, Tbx15, Ngn1, Pou4f1.2 and Isl2 and were used to amplify a ~800 bp fragment from plasmid DNA (Supplementary file 4) which was then used as a template for probe synthesis using T7 RNA polymerase to make an antisense probe. pCMV-SPORT6 with Znf214, Mab21l2-b and Pou3f2b were linearised with SalI and antisense probes synthesised with T7. pCS2+ vectors containing Tbx6, FosB and Crem were linearised with BamHI and transcribed with T7. pCS2+ with Atoh1 was linearised with NotI and transcribed with SP6.

### Vibratome sections and immunohistochemistry

In order to analyse the distribution of gene expression domains in finer detail, serial 40–50 μM vibratome sections were cut from selected embryos after wholemount in-situ hybridisation. Where staining with X-gal was insufficient to reveal the injected site, lacZ distribution was revealed immunohistochemically using a polyclonal rabbit anti-LacZ (MP Biomedicals Cappel, Santa Ana, California; Cat.: 55976; 1:1000) and an Alexa594-conjugated anti-rabbit antibody (1:1000).

### Availability of data and material

All sequencing data have been deposited in the NCBI BioProject database under BioProject PRJNA317049. All scripts used in analysis are available at https://github.com/nriddiford/Six1-Eya1-RNA-Seq.git.

# Genetically manipulating endogenous Kras levels and oncogenic mutations in vivo influences tissue patterning of murine tumorigenesis

## Authors

- Özgün Le Roux<sup>1</sup> ([ORCID: 0000-0002-9885-6872](https://orcid.org/0000-0002-9885-6872))
- Nicole LK Pershing<sup>1</sup>
- Erin Kaltenbrun<sup>1</sup>
- Nicole J Newman<sup>1</sup>
- Jeffrey I Everitt<sup>2</sup> ([ORCID: 0000-0003-0273-6284](https://orcid.org/0000-0003-0273-6284))
- Elisa Baldelli<sup>3</sup>
- Mariaelena Pierobon<sup>3</sup>
- Emanuel F Petricoin<sup>3</sup>
- Christopher M Counter<sup>1</sup> ([ORCID: 0000-0003-0748-3079](https://orcid.org/0000-0003-0748-3079)) †

### Affiliations

1. Department of Pharmacology & Cancer Biology, Duke University Medical Center Durham United States ([ROR:03njmea73](https://ror.org/03njmea73))
2. Department of Pathology, Duke University Medical Center Durham United States ([ROR:03njmea73](https://ror.org/03njmea73))
3. Center for Applied Proteomics and Molecular Medicine, School of Systems Biology, George Mason University Manassas United States ([ROR:02jqj7156](https://ror.org/02jqj7156))

† Corresponding author

## Abstract

Despite multiple possible oncogenic mutations in the proto-oncogene KRAS, unique subsets of these mutations are detected in different cancer types. As KRAS mutations occur early, if not being the initiating event, these mutational biases are ostensibly a product of how normal cells respond to the encoded oncoprotein. Oncogenic mutations can impact not only the level of active oncoprotein, but also engagement with proteins. To attempt to separate these two effects, we generated four novel Cre-inducible (LSL) Kras alleles in mice with the biochemically distinct G12D or Q61R mutations and encoded by native (nat) rare or common (com) codons to produce low or high protein levels. While there were similarities, each allele also induced a distinct transcriptional response shortly after activation in vivo. At one end of the spectrum, activating the KrasLSL-natG12D allele induced transcriptional hallmarks suggestive of an expansion of multipotent cells, while at the other end, activating the KrasLSL-comQ61R allele led to hallmarks of hyperproliferation and oncogenic stress. Evidence suggests that these changes may be a product of signaling differences due to increased protein expression as well as the specific mutation. To determine the impact of these distinct responses on RAS mutational patterning in vivo, all four alleles were globally activated, revealing that hematolymphopoietic lesions were permissive to the level of active oncoprotein, squamous tumors were permissive to the G12D mutant, while carcinomas were permissive to both these features. We suggest that different KRAS mutations impart unique signaling properties that are preferentially capable of inducing tumor initiation in a distinct cell-specific manner.

## Introduction

Why specific driver mutations track with different cancers is unknown, yet speaks to the very origins of cancer, with implications for early detection and prevention. This is particularly well illustrated with the RAS family of small GTPases, comprised of KRAS, NRAS, and HRAS. Focusing on KRAS, the most commonly mutated of the three (Prior et al., 2020), single-point mutations at one of three hotpot positions (G12, G13, and Q61) result in six possible substitutions that inhibit the intrinsic or extrinsic GTPase activity of the protein. These mutations render KRAS constitutively GTP-bound and active, which is well known to be oncogenic (Simanshu et al., 2017). Although this amounts to 18 possible oncogenic mutations, specific subsets tend to be found in different cancer types. For example, the most common oncogenic KRAS mutation is G12C in non-small cell lung cancer but Q61H in plasma cell myeloma (Prior et al., 2020). Mice similarly exhibit a bias of specific oncogenic Kras mutations towards different cancer types as different mutant Kras alleles have different tumorigenic potential when activated in different tissues (Li et al., 2018; Poulin et al., 2019; Winters et al., 2017; Wong et al., 2020; Zafra et al., 2020). Different oncogenic mutations also affect the ability of Nras to induce tumorigenesis in mice, as do the same mutations in different RAS isoforms (Burd et al., 2014; Haigis et al., 2008; Kong et al., 2016; Murphy et al., 2022). While this tissue ‘tropism’ of cancers towards specific RAS mutations has been appreciated for decades (Bos, 1989), the underlying mechanism is unclear.

Variation in the ability of specific KRAS mutants to be tumorigenic (or not) in different tissues ostensibly results from differences in oncogenic signaling between mutants and the response of normal cells thereof. Generally speaking, oncogenic signaling is a product of the amplitude of the signal (quantitative signaling) and/or the pathways engaged (qualitative signaling). In terms of quantitative signaling, different mutations can exhibit different degrees of activation (GTP-loading) and/or different sensitivities to positive (Ras GTP exchange factors [RasGEFs]) or negative (RAS GTPase activating proteins [RasGAPs]) regulators (Gebregiworgis et al., 2021; Munoz-Maldonado et al., 2019; Simanshu et al., 2017). Various methods to manipulate quantitative Kras signaling, such as through modulating recombination rates (Singh et al., 2021), homozygous expression of the mutant allele (Wang et al., 2011), changing codon usage to increase protein expression (Pershing et al., 2015), additional pharmacological activation of the mitogen-activated protein kinase (MAPK) pathway (Cicchini et al., 2017), and so forth (Li et al., 2018), all affect tumorigenesis. On the other hand, perhaps one of the best examples of qualitative differences in KRAS signaling is the G12R mutant. Unlike the more canonical G12D mutation, the G12R mutant exhibits reduced the RAS effector PI3Kα binding and PI3K/AKT signaling (Hobbs et al., 2020). Activating an inducible KrasLSL-G12R allele in the pancreas led to fewer early premalignant lesions compared to the much more tumorigenic KrasLSL-G12D allele (Zafra et al., 2020). Despite an appreciation that different KRAS mutations can manifest in quantitative or qualitative signaling differences, how each contributes to the mutational patterns of this oncogene in cancer is unclear.

KRAS mutations are often initiating, being sufficient to induce tumorigenesis in mice and truncal in many human cancers. Thus, the bias of specific cancers towards distinct KRAS mutations could arise from potential tissue-specific differences of normal cells in the mutagenic process or repair capacity and/or in their responses to the nature of the signaling imparted by specific KRAS mutations (Li et al., 2018). In regard to the latter, determining the immediate response of normal cells to different KRAS mutations in vivo may help elucidate the mutational patterning of this oncogene. Identifying an oncogenic mutation arising in the KRAS gene from the cell-of-origin prior to becoming a tumor is challenging in humans. Mice, on the other hand, provide an ideal model system to experimentally explore this phenomenon as the point of tumor initiation can be precisely defined using inducible oncogenic Kras alleles. To therefore explore why different cancer types have a bias towards specific KRAS mutations, we created four novel inducible murine Kras alleles with different oncogenic mutations that were expressed at either low or high levels. In this way, we hypothesize that tissues in which tumor initiation is driven by the level of oncogenic signaling would preferentially develop tumors at higher protein levels while those driven by a specific mutant would preferentially develop tumors with just one of the two mutants.

We chose two completely different oncogenic mutations for these alleles, G12D and Q61R. G12D places a negatively-charged headgroup into the catalytic cleft of RAS and blocks extrinsic (RasGAP-mediated) GTPase activity (Parker et al., 2018). On the other hand, Q61R replaces the catalytic amino acid with one that has a positively-charged headgroup, disrupting the position of the active site water molecule necessary for intrinsic GTP hydrolysis (Buhrman et al., 2010). Q61 is also essential for extrinsic GTP hydrolysis, as it stabilizes the transition state via hydrogen bonds to the γ-phosphate and nucleophilic water while providing another hydrogen bond to the RasGAP arginine finger (Grigorenko et al., 2007; Kötting et al., 2008; Rabara et al., 2019; Scheffzek et al., 1997). Comparing these two mutants directly reveals Q61R to have significantly lower GTP exchange and hydrolysis rates than G12D in Nras (Burd et al., 2014) and reduced RasGAP-mediated GTP hydrolysis rates in Kras (Rabara et al., 2019), akin to other substitutions at these two positions (Gebregiworgis et al., 2021; Smith et al., 2013). In those few cases in which the tumorigenic potential of the G12D and Q61R mutants of the same Ras isoform has been directly compared in mice, tissue-specific expression of the G12D mutant was less oncogenic than Q61R in both Nras-induced melanoma (Burd et al., 2014) and Kras-induced myeloproliferative neoplasm (Kong et al., 2016).

To alter the expression of these two mutants, the first three coding exons of Kras were fused and encoded by either their native rare codons, which is known to retard Kras protein expression, or common codons to increase Kras protein expression (Ali et al., 2017; Fu et al., 2018; Lampson et al., 2013; Pershing et al., 2015). We chose the novel approach of altering mammalian codon usage to modulate protein expression in vivo (Li and Counter, 2021; Pershing et al., 2015; Sasine et al., 2018) as no additional elements are required to change protein levels, providing a simple, reproducible, and uniform way of modulating Kras levels in mice and derived cell lines.

These four alleles were activated and immediately thereafter the in vivo transcriptome was determined in the lungs. This revealed that while these four alleles certainly shared similarities, each also induced unique transcriptional responses. Increased expression shifted the transcriptional hallmarks from those indicative of an expansion of multipotent cells to that of hyperproliferation and oncogenic stress. Changing the mutation type shifted the hallmark of estrogen response in the G12D mutant to that of the p53 pathway and DNA repair in the Q61R mutant. All four alleles were then globally activated, revealing that hematolymphopoietic lesions were permissive to the level of active oncoprotein, squamous tumors were preferentially permissive to the G12D mutant, while carcinomas tended to be permissive to both these changes. These findings support tissue-specific responses to the degree and type of signaling imparted by different oncogenic mutations molds the tissue tropism of cancers towards specific oncogenic KRAS mutations.

## Results

### A panel of inducible oncogenic Kras alleles designed to separate the effects of mutation type from the activity level of the oncoprotein

To explore how specific cancers are driven by distinct KRAS mutations, we reasoned that effects unique to a mutation could be separated from those imparted by activation level by simply comparing two different oncogenic mutants expressed at high or low levels. To this end, we created the four novel Cre-inducible oncogenic Kras alleles KrasLSL-natG12D, KrasLSL-natQ61R, KrasLSL-comG12D, and KrasLSL-comQ61R (Figure 1A). Each began with an LSL transcriptional/translational repressor sequence (STOP) flanked by loxP sites (Jackson et al., 2001) engineered into the intron of Kras following the first non-coding exon to provide temporal and spatial control of gene expression. This was followed by a fusion of the first three coding exons encoded by either their native (nat) rare codons, which are known to retard protein expression, or 93 of these rare codons converted to their common (com) counterparts to increase protein expression (Figure 1—figure supplement 1 and Figure 1—source data 6). Each version contained either a G12D or Q61R mutation. As noted above, these two mutants alter RAS activity in a biochemically different manner (Munoz-Maldonado et al., 2019; Simanshu et al., 2017), with Q61R reported to yield higher levels of active (GTP-bound) Ras (Burd et al., 2014; Kong et al., 2016; Pershing et al., 2015). This was followed by the next intron containing an FRT-NEO-FRT cassette for ES selection, which was excised via Flp-mediated recombination in the resultant animals, after which the Flp transgene was outbred. Finally, the remainder of the gene was left intact so as to generate the two Kras4a and Kras4b isoforms, as both contribute to tumorigenesis (To et al., 2008), potentially through unique protein interactions (Amendola et al., 2019).

![Figure 1.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig1-v1.jpg)

**Figure 1.:** (A) Schematic of generating and activating KrasLSL alleles with the first three coding exons fused and encoded by native (nat) versus common (com) codons with either a G12D or Q61R mutation. (B) PCR genotyping of two independently derived mouse embryonic fibroblast (MEF) cultures (two biological replicates) with the indicated Kras alleles in the absence and presence of Cre recombinase (CRE) to detect the unaltered wild-type Kras allele product (WT, 488 bp) and the unrecombined (KrasLSL*, 389 bp) and recombined (LoxP recombined, 616 bp) KrasLSL allelic products. Gel images were cropped and color inverted for optimal visualization. Full-length gel images are provided in Figure 1—source data 2. (C) Expression levels, determined by immunoblot with an anti-Kras antibody, RAS activity levels, determined by RBD pull-down (RBD-PD) of lysates collected from MEF cells derived from mice with the indicated Kras alleles in the presence of Cre recombinase (CRE). MEF cultures derived from KrasLSL-natG12D/+ mice in the absence of Cre recombinase were used as negative control. MEF cultures were either serum starved overnight (starved) or serum starved overnight followed by serum stimulation for 5 min (stimulated). 20% of the elute from RBD-PD and 30 μg total protein from the total cell lysates were loaded. Tubulin serves as loading control. One of two biological replicates; see Figure 1—figure supplement 3 for the second biological replicate. Full-length gel images are provided in Figure 1—source data 3.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Codon usage index versus codon position of Kras with native (nat, blue line), common (com, red line), and rare (rare, orange line) codons. Maximum rare (all rare, gray dotted line) and common (all common, solid black line) codon usage is shown for reference.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** Expression levels, determined by immunoblot with an anti-FLAG antibody, and activity levels, determined by RBD pull-down (RBD-PD) followed by (A, B) immunoblots of lysates derived from HEK-HT cells transiently expressing the indicated FLAG-tagged Kras proteins and (C, D) by ELISA (n=2). (A, B) and (C, D) are two biological replicates. Tubulin and empty vector (EV) serve as loading and negative controls, respectively. Full-length gel images are provided in Figure 1—source data 1.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** RBD pull-down (RBD-PD) of lysates of mouse embryonic fibroblast (MEF) cells derived from the indicated KrasLSL alleles in the presence of Cre recombinase (CRE) after serum starvation overnight (Starved) or then stimulated with serum for 5 min (Stimulated). RBD-PD was performed with two serial dilutions of 500 μg (top) and 200 μg (bottom) MEF lysates. Lysates of KrasLSL-natG12D/+ MEFs in the absence of Cre recombinase serve as negative controls. Full-length gel images are provided at Figure 1—source data 3.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (A) Schematic of the experimental design. Two mice from cohorts of KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ in a Rosa26CreERT2/+ background, injected with tamoxifen at six to eight weeks of age, seven days later the lungs were removed at the time of necropsy, and protein lysates were subjected to the RBD pull-down (RBD-PD) assay. Two Rosa26CreERT2/+ mice were treated similarly as a control. (B) RAF1-RBD pull-down (RBD-PD) of lysates of lungs from the indicated KrasLSL alleles after tamoxifen injection. 20% of the RBD pull-downs were immunoblotted for Kras. Immunoblots of two separate pull downs from total lung lysates are shown as RBD-PD 1 and RBD-PD 2. 30 μg total protein was loaded in each lane as input. (C) The ratio of median Kras activity levels determined by densitometry in each genotype in comparison to the KrasnatG12D/+ allele, calculated from both technical and biological replicates in (B). p-Values calculated by one-way ANOVA multiple pairwise comparisons with Tukey testing (C). ***p<0.001, ****p<0.0001. Full-length gel images are provided in Figure 1—source data 4.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** qRT-PCR validates an increase in RAS target gene expression with increased Kras activity. Two mice from cohorts of KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ in a Rosa26CreERT2/+ background, injected with tamoxifen at six to eight weeks of age and RNA was extracted from lungs seven days later. Two Rosa26CreERT2/+ mice were treated similarly as a control (A). First-strand cDNA synthesis and qRT-PCR of selected genes downstream ERK/MAPK pathway were performed using GoTaq 2-Step RT-qPCR kit (B, C). All measurements were normalized against Actin as the internal control using the 2-ΔΔCt method (n=3). (B, C) Biological replicates. Measurements are provided in Figure 1—source data 5.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** Heatmap of the log2 fold change of the average abundance of protein and phosphorylated proteins within the MAPK pathway via RPPA analysis upon activation of the KrasLSL-natG12D/+ and KrasLSL-comQ61R/+ alleles in comparison to the wild-type Kras allele. Data is representative of three technical replicates from three biological replicates.

To confirm that the expression and activity of these four versions of oncogenic Kras was reflected in their design, we ectopically expressed the corresponding FLAG-tagged murine Kras cDNAs in HEK-HT cells that critically depend upon oncogenic RAS for tumorigenesis (Hahn et al., 1999). The total amount of ectopic Kras protein was then determined by immunoblot with an anti-FLAG antibody, and the level of GTP-bound and active Kras was determined by pull-down with a Ras binding domain (RBD) peptide followed by immunoblot or ELISA. Based on common codons increasing protein expression and Q61R leading to higher levels of GTP-bound RAS, the four constructs display the expected stepwise increase in RBD-bound Kras in the ascending order of KrasnatG12D<KrasnatQ61R <KrascomG12D<KrascomQ61R in both assays (Figure 1—figure supplement 2, Figure 1—source data 1).

### The effect of codon usage and mutation type on Kras activity in derived murine cells

To evaluate the endogenous functionality of this allelic set, we derived and characterized two separate mouse embryonic fibroblast (MEF) cultures from each of the genotypes KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+, and validated that all four alleles could be recombined upon the expression of Cre recombinase (Figure 1B, Figure 1—source data 2). We then confirmed that this allelic set yields an increase in endogenous Kras activity consistent with codon usage and mutation type. These pairs of MEF cultures expressing Cre were either serum starved or stimulated to assess basal or stimulated Kras activity, respectively. RBD pull-down followed by immunoblot demonstrated the stepwise increase in Kras expression and activity levels in the ascending order of KrasnatG12D<KrasnatQ61R <KrascomG12D<KrascomQ61R in both conditions (Figure 1C, Figure 1—figure supplement 3, Figure 1—source data 3). Thus, endogenous expression of these four alleles revealed that the Q61R mutant is more active than the G12D mutant, and changing rare codons to common increases the expression and activity of endogenous Kras oncoprotein.

### The effect of codon usage and mutation type on Kras activity in vivo

To validate these findings in vivo, we crossed the KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ genotypes into a Rosa26CreERT2/+ background, which expresses a tamoxifen-inducible Cre from the endogenous Rosa26 promoter that is active in a broad spectrum of tissues (Ventura et al., 2007). Two adult mice from each of the four derived cohorts, as well as the control strain (Rosa26CreERT2/+), were injected with tamoxifen, and seven days later humanely euthanized, their lungs removed, and duplicate samples of derived protein lysates subjected to RBD pull-down followed by immunoblot (Figure 1—figure supplement 4A). As in the case of the MEF cultures, we observed a stepwise increase in Kras expression and activity consistent with the codon usage and oncogenic mutation in this allelic set (Figure 1—figure supplement 4B C, Figure 1—source data 4). To assess whether this was reflected in the expression of downstream target genes, we generated the same four cohorts of mice, but in this case isolated RNA from the lungs of euthanized mice seven days after tamoxifen injection and determined the level of mRNA encoded by five known Ras target genes by qRT-PCR (Figure 1—figure supplement 5A). This revealed the expected increase in three such transcripts when Kras was encoded with common codons, which was further increased in the Q61R-mutant background (Figure 1—figure supplement 5B C, Figure 1—source data 5). To further validate this effect at the protein level, we performed reverse-phase protein array (RPPA) analysis of lung tissue upon activation of the two extreme alleles, KrasLSL-natG12D versus KrasLSL-comQ61R in the Rosa26CreERT2/+ background, with Rosa26CreERT2/+ serving as a control. Three mice from each genotypes were injected with tamoxifen and seven days later euthanized, their lungs removed, embedded, and derived protein lysates subjected to RPPA analysis. When normalized to the control tissue, there was a clear increase in the level of phosphorylated proteins of the MAPK pathway and downstream transcription factors upon activating the KrasLSL-comQ61R allele compared to activating the KrasLSL-natG12D allele (Figure 1—figure supplement 6, Supplementary file 1). Thus, the increase in Kras activity imparted by the Q61R mutant or by common codons observed in cultured cells is recapitulated in lung tissue.

### The effect of codon usage and mutation type on Kras biological activity in vivo

We next assessed whether these alleles were proportionally tumorigenic in a side-by-side comparison in the same organ. Each of these four alleles were crossed into a CC10CreER/+ (and Rosa26CAG-fGFP/+) background, and the resultant mice were injected with tamoxifen to specifically induce Cre-mediated recombination in the lung, after which every month thereafter for 6 months, five mice from each of the four cohorts were euthanized (Figure 2—figure supplement 1A). The lungs from all mice were visually analyzed for the presence of surface pulmonary tumors (Figure 2—figure supplement 1B), and in addition, two H&E-stained sections from pairs of mice were assayed for the presence and type of pulmonary tumors by a veterinarian pathologist blinded to the genotype (Figure 2A). This revealed a stepwise increase in early-onset and tumor burden of pulmonary lesions in lock step with the increased biochemical activity of the oncoproteins in the ascending order of KrasnatG12D<KrasnatQ61R <KrascomG12D<KrascomQ61R (Figure 2A, B). These tumorigenic phenotypes were the result of activating the inducible Kras alleles in the lungs as five control wild type (Kras+/+) mice in the same background that were injected with tamoxifen failed to develop tumors after 13 months, twice the length of the study (Figure 2—figure supplement 1C, D). Finally, we find preliminary evidence in a few animals that the G12D-mutant alleles preferentially developed atypical alveolar hyperplasia (AAH), whereas bronchiolar hyperplasia/dysplasia (BH) lesions were more prevalent with the Q61R-mutant alleles (Figure 2—figure supplement 1E F). We conclude that this allelic set exhibits an increase in tumorigenic potential consistent with the activity of the encoded oncoproteins, but potentially may also display evidence of mutation-specific effects on tumorigenesis.

![Figure 2.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig2-v1.jpg)

**Figure 2.:** (A) Examples of H&E-stained lung sections and (B) the mean ± SD % tumor burden from microscopic analysis of two lung sections from five mice with the indicated KrasLSL alleles in a CC10CreER/+;Rosa26CAG-fGFP/+ background at each of the indicated times post-tamoxifen injection.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Schematic of the experimental design. (B) Percentage of mice with at least one visible lung lesion. (C) Representative H&E staining of lungs and (D) mean ± SD% tumor burden from microscopic analysis of two lung sections from two CC10CreER/+;Rosa26CAG-fGFP/+;Kras+/+ mice 13 months after tamoxifen. (E, F) Predominant proliferative lesions in lungs of CC10CreER/+;Rosa26CAG-fGFP/+;KrascomG12D/+ and CC10CreER/+;Rosa26CAG-fGFP/+;KrascomQ61R/+ differ. Photomicrograph of lung section from (E) CC10CreER/+;Rosa26CAG-fGFP/+;KrascomG12D/+ mouse at 4 months showing multiple large pulmonary adenomas, and (F) CC10CreER/+;Rosa26CAG-fGFP/+;KrascomQ61R/+ mouse at 1 month showing extensive proliferation of airway epithelium into papillary projections of hyperplastic and dysplastic cells as well as pulmonary adenoma. H&E staining, ×40 magnification.

### The response of lung tissue to Kras alleles with different codon usage or mutations in vivo

As the different tumor types and grades that arose upon activation of each of these four inducible oncogenic Kras alleles are presumably a product of tumor initiation, understanding these effects presumably lies in how cells immediately respond to these different oncoproteins. We thus compared the immediate transcriptional response, as a measure of the cellular changes upon activation of each allele, in the lung. Cohorts of three adult mice from each of the four inducible oncogenic Kras alleles in Rosa26CreERT2/+ background were injected with tamoxifen, and seven days later the animals were euthanized, their lungs removed, and RNA was isolated for bulk transcriptome sequencing (Figure 3—figure supplement 1A).

The resultant transcriptomes (GSE181628) exhibited a gradual increase in the number of genes differentially expressed with the level of active Kras (as assessed above by the RBD pull-down assay in lung tissue). Namely, we identified 7, 15, 73, and 701 genes were differentially expressed (with absolute log2 fold change larger than 2, and adjusted p-value less than 5%) upon activation of the KrasLSL-natG12D, KrasLSL-natQ61R, KrasLSL-comG12D, and KrasLSL-comQ61R alleles, respectively, compared to the wild-type Kras allele (Figure 3A, Figure 3—figure supplements 2–6, Figure 3—source data 1). Principal component analysis of these four transcriptomes revealed that the transcriptome upon activating both alleles encoded by native rare codons differed from both alleles encoded with common codons,while the G12D mutant was most distinct from the Q61R mutant in the KrasLSL-com background (Figure 3—figure supplement 1B). Similarly, when two mutants were compared, the ratio of uniquely differentially expressed genes specific to each allele increased from the G12D to the Q61R mutant when Kras was encoded with common codons (34–93%) more than it did when encoded with native rare codons (0–6%) (Figure 3—figure supplement 6, Figure 3—source data 1). Comparing the transcriptomes of the two Kras alleles encoded with native rare versus common codons revealed that the two native-encoded alleles decreased KRAS Signaling UP hallmarks while the two common-encoded alleles induced signaling events related to oncogenic stress, such as an increase in Oxidative Phosphorylation, Glycolysis, Reactive Oxygen Species, MTORC1 signaling, Peroxisome, Xenobiotic Metabolism, and UV Response UP hallmarks and a decrease in UV Response DN, Hedgehog Signaling, and Apical Junction hallmarks (Figure 3B, Figure 3—figure supplement 1C, Figure 3—source data 2). We interpret this as expression level largely dictating the degree of oncogenic signaling in this allelic set. Comparing the G12D versus Q61R transcriptomes revealed both G12D-mutant alleles induced the Estrogen Response Late hallmark while the Q61R-mutant alleles induced DNA Repair and P53 Pathway and decreased Interferon Alpha Response hallmarks, suggesting that there is a strong tumor-suppressive response uniquely activated by the Q61R-mutant alleles (Figure 3C, Figure 3—figure supplement 1C, Figure 3—source data 2).

![Figure 3.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-v1.jpg)

**Figure 3.:** (A) Volcano plot of the log2 fold change versus p-value of the genes showing differential expression in each allele compared to the wild-type (+/+) Kras allele in the lung. Full-sized plots are provided in Figure 3—figure supplements 2–5. (B, C) Normalized enrichment score and patterns of the indicated Gene Set Enrichment Analysis (GSEA) hallmarks differentially enriched by Kras codon usage (expression) (B) and mutation type (C). Only hallmarks with a false discovery rate (FDR) < 5% are shown. Dot size is adjusted to RAS activity for better visualization. All GSEA hallmarks differentially enriched upon activating KrasLSL alleles with an FDR < 5% are provided in Figure 3—figure supplement 7. (D) STRING analysis of the top ten genes in the differentially enriched GSEA hallmarks identified in RNA-seq analysis of the lungs of Rosa26CreERT2/+;KrasLSL-natG12D/+ versus Rosa26CreERT2/+;KrasLSL-comQ61R/+ mice seven days after tamoxifen injection.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Schematic of the experimental design. (B) Principal component analysis of the transcriptome signatures of engineered alleles. Alleles with high quantitative signaling are highlighted with blue (KrascomG12D/+) and pink shade (KrascomQ61R/+), and alleles with and low signaling (Krasnat) in green shade. (C) Transcriptome Gene Set Enrichment Analysis (GSEA) hallmarks upon activating the panel of KrasLSL alleles. Purple stars show hallmarks that show enrichment or depletion patterns of hallmarks correlated with the Kras expression (enriched in Krascom and depleted in Krasnat). Only hallmarks with a false discovery rate (FDR) < 5% are shown. Dot size is adjusted according to RAS activity for better visualization.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Volcano plot of the log2 fold-change versus p-value of differentially expressed genes from RNA-seq analysis of the lungs of Rosa26CreERT2/+;KrasLSL-natG12D/+ versus Rosa26CreERT2/+;Kras+/+ mice seven days after tamoxifen injection.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Volcano plot of the log2 fold-change versus p-value of differentially expressed genes from RNA-seq analysis of the lungs of Rosa26CreERT2/+;KrasLSL-natQ61R/+ versus Rosa26CreERT2/+;Kras+/+ mice seven days after tamoxifen injection.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** Volcano plot of the log2 fold-change versus p-value of differentially expressed genes from RNA-seq analysis of the lungs of Rosa26CreERT2/+;Kras LSL-comG12D/+ versus Rosa26CreERT2/+;Kras+/+ mice seven days after tamoxifen injection.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp5-v1.jpg)

**Figure 3—figure supplement 5.:** Volcano plot of the log2 fold-change versus p-value of differentially expressed genes from RNA-seq analysis of the lungs of Rosa26CreERT2/+;Kras LSL-comQ61R/+ versus Rosa26CreERT2/+;Kras+/+ mice seven days after tamoxifen injection.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp6-v1.jpg)

**Figure 3—figure supplement 6.:** Number of commonly identified genes from the differentially expressed transcriptome in each KrasLSL allele with |log2FC| larger than 2 and adjusted p-value larger than 5% when compared to the WT Kras allele (top: depleted; middle: enriched; bottom: total). Venn diagrams are color coded according to KrasLSL allele for better visualization (cyan: KrasLSL-natG12D/+; blue: KrasLSL-natQ61R/+; orange: KrasLSL-comG12D/+; red: KrasLSL-comQ61R/+).

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp7-v1.jpg)

**Figure 3—figure supplement 7.:** (A) Heatmap of the log2 fold change of selected genes from RNA-seq analysis of the lungs of indicated KrasLSL alleles in the Rosa26CreERT2/+ background in comparison to the wild-type Kras allele seven days after tamoxifen injection. (B, C) Validation of signaling responses via qRT-PCR analysis of the selected genes in (A) from pathways of TNFα Signaling via NF-κB and Interferonγ Signaling (B), and EMT and Myogenesis (C) (n=3). Two biological replicates.

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp8-v1.jpg)

**Figure 3—figure supplement 8.:** (A) Volcano plot of the log2 fold change versus p-value of differentially expressed genes and (B) the false discovery rate (FDR) versus normalized enrichment score of the indicated Gene Set Enrichment Analysis (GSEA) hallmarks determined from RNA-seq analysis of the lungs of Rosa26CreERT2/+; KrasLSL-comQ61R/+ versus Rosa26CreERT2/+;Kras LSL-natG12D/+ mice seven days after tamoxifen injection.

![Figure 3—figure supplement 9.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig3-figsupp9-v1.jpg)

**Figure 3—figure supplement 9.:** Heatmap of the log2 fold change of abundance of proteins and phosphorylated proteins in the lungs of Rosa26CreERT2/+;KrascomQ61R/+ and Rosa26CreERT2/+;KrasnatG12D/+ mice in comparison to the control Rosa26CreERT2/+;Kras+/+ mice seven days after tamoxifen injection. The downstream pathways of RAS/MAPK, PI3K/AKT, Growth, IL/Jak/STAT, DNA repair, Apoptosis, Autophagy, and Senescence were selected based on the enrichment of the Gene Set Enrichment Analysis (GSEA) hallmarks in the lung transcriptome analysis in Figure 3D.

To validate the transcriptional responses detected by bulk RNA-seq analysis, we quantified four to six marker genes in a subset of selected hallmarks. Two adult mice from each of the four cohorts and control mice were injected with tamoxifen as above, and seven days later the animals were euthanized, their lungs removed, RNA isolated, and the level of select transcripts determined by qRT-PCR. We identified similar expression patterns to the transcriptome signature in the hallmarks of TNFα Signaling via NFκβ and Interferon-γ, which increase with Kras activity (Figure 3—figure supplement 7A B, Figure 3—source data 3), and EMT and Myogenesis, as these hallmarks were enriched in G12D mutants but depleted in Q61R mutants (Figure 3—figure supplement 7A C, Figure 3—source data 3).

To probe these transcriptomes for evidence of an orchestrated response of normal cells to different Kras mutants, we repeated transcriptome analysis of lung tissue on the two extreme cases, namely, KrasLSL-natG12D versus KrasLSL-comQ61R (GSE181627). Activation of the KrasLSL-natG12D allele resulted in transcriptional signatures suggestive of an expansion of multipotent cells (Figure 3—figure supplement 8A B). Namely, Gene Set Enrichment Analysis (GSEA) hallmarks indicative of Epithelial Mesenchymal Transition (EMT, TGFβ Signaling, Wnt/βcatenin Signaling, Notch Signaling, Apical Junction, Apical Surface, and Estrogen Response Early) and multiple cell lineages (Adipogenesis, Myogenesis, Hedgehog Signaling, and Pancreas β Cells). Conversely, activation of the KrasLSL-comQ61R allele had all features of a potent oncogenic signaling leading to hyperproliferation and oncogenic-induced stress. Namely, GSEA hallmarks indicative of high oncogenic signaling (KRAS Signaling UP) and unrestrained proliferation (MYC Targets V1, and E2F Targets), leading to reactive oxygen species (Oxidative Phosphorylation, and Reactive Oxygen Species Pathway) and a DNA damage response (DNA Repair, P53 Pathway, and G2M Checkpoint) followed by apoptosis (Apoptosis) and inflammation (Inflammatory Response, IL6 JAK STAT3 Signaling, TNFα Signaling via NF-κβ, and Allograft Rejection).

To assess the response of cells at the protein level, we performed RPPA analysis of lung tissue from these same two genotypes. This revealed that the level of protein/phosphoproteins of RAS/MAPK, PI3K/AKT, Growth, DNA repair, senescence/autophagy/apoptosis, and IL/Jak/Stat pathways was higher upon activation of the KrasLSL-comQ61R compared to the KrasLSL-natG12D allele (Figure 3—figure supplement 9 and Supplementary file 1), consistent with the transcriptome analysis. Finally, STRING analysis of the top ten genes from each of these GSEA hallmarks revealed potential crosstalk between the various signaling pathways, suggesting a consolidated signaling program by the two different oncoproteins manifests in very different responses by normal cells (Figure 3D). We suggest that this allelic set moves the response of normal lung cells from an expansion of multipotent cells to one of extreme oncogenic signaling and stress, with the type of oncogenic mutation potentially further modulating these responses.

### Tissue sensitivities to the different oncogenic Kras alleles

We next addressed the ‘tropism’ of tissues towards specific Kras mutants by determining the tumor landscape upon globally activating each allele. As each allele is expected to have a different oncogenic potential, we opted for a moribundity endpoint, as opposed to a fixed endpoint, to identify the tissues most permissive to tumorigenic conversion in a competition-based approach. To this end, each allele was again activated by tamoxifen using the aforementioned ubiquitous Cre driver Rosa26CreERT2. Mice were regularly monitored for moribundity endpoints, indicative of ensuing mortality due to cancer, at which time the animals were euthanized (Figure 4—figure supplement 1). As a control to rule out a tumor phenotype being a product of variations in gene activation, we validated Cre-mediated recombination between all four alleles across 14 diverse tissues seven days after tamoxifen injection. Only the ovary displayed reduced recombination, and hence was not included in the study (Figure 4—figure supplement 2, Figure 4—source data 1, and Supplementary file 2).

Plotting the percent survival for each of the four genotypes by the Kaplan–Meier approach revealed that the median life span of mice progressively increased from 14 days upon activating the KrasLSL-comQ61R allele to 150 days upon activating the KrasLSL-natG12D allele (Figure 4A). Not surprisingly, the number of tumors per animal mirrored these survival differences (Figure 4—figure supplement 3). Pairwise comparisons revealed that median survivals were statistically different, except between the KrasLSL-natG12D/+ versus KrasLSL-natQ61R/+ cohorts (Figure 4—figure supplement 4 and Supplementary file 3). Of note, median survival was significantly decreased in mice with when Kras was encoded with common compared to native rare codons. Survival was also decreased in the mice with the Q61R compared to the G12D mutation when the allele contained the same codon usage (KrasLSL-natQ61R versus KrasLSL-natG12D and KrasLSL-comQ61R versus Kras LSL-comG12D). As both common codons and the Q61R mutation increase Kras activity, we suggest that the level of active oncoprotein is the dominant determinant of cancer survival in this model.

![Figure 4.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-v1.jpg)

**Figure 4.:** (A) Kaplan–Meier survival curve of the mice with the indicated KrasLSL alleles after activation by tamoxifen. Dotted lines: 50% survival. (B) Number of mice with the indicated number of different tumor types. Examples of H&E-stained slides of the indicated tissues are provided in Figure 4—figure supplement 5. (C–F) Percentage of the indicated grades of hematolymphopoietic (C), forestomach (D), oral (E), and lung (F) lesions at moribundity endpoint in Rosa26CreERT2/+ mice (n = 8–10) with one of the four indicated KrasLSL alleles after activation by tamoxifen.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Schematic of the experimental design. Cohorts of three adult male and female Rosa26CreERT2/+;Kras LSL-natG12D/+, Rosa26CreERT2/+;Kras LSL-natQ61R/+, Rosa26CreERT2/+;Kras LSL-comG12D/+, and Rosa26CreERT2/+;Kras LSL-comQ61R/+ mice were injected with tamoxifen and euthanized at moribundity. Selected set of organs were fixed in formalin, sliced and embedded in paraffin, sectioned, and H&E stained.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Schematic of the experimental design. Two mice from each KrasLSL genotype in a Rosa26CreERT2/+ background seven days after tamoxifen injection were euthanized, and their organs were removed. Genomic DNA was isolated and subjected to genotyping PCR. One mouse in Rosa26CreERT2/+;Kras LSL-comG12D/+ background was used as a no-tamoxifen control. (B) Gel images from duplicate recombination analysis and (C) mean ± SEM of the ratio of the recombined KrasLSL (LoxP recombined, 616 bp) to unaltered wild-type Kras (WT, 488 bp) allele products determined by PCR genotyping. Two technical replicates of two biological replicates. Full-length gel images are provided at Figure 4—source data 1. (D, E) One-way ANOVA with Bonferroni’s multiple-comparisons test with a single pooled variance and a 95% CI shows variation in recombination rate across different alleles (D) compared to the KrasnatG12D/+ allele or across organs (E) compared to the colon, with the exception of ovary, was not statistically significant (*p<0.1 and ***p<0.001).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** Number of mice with the indicated number of different tumor types (see Supplementary file 4).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** p-Values calculated by log-rank (Mantel–Cox) test of the pairwise comparisons of alleles (see Supplementary file 3).

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** Examples of H&E-stained sections from the indicated organs in each allele upon global activation at the moribundity endpoint.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-figsupp6-v1.jpg)

**Figure 4—figure supplement 6.:** Mean ± SD of number of AHA and adenoma lesions per animal with stars denoting animals with extensive myeloid infiltration in the lungs (A), mean ± SD of peripheral lesions observed as percent surface area (B), and percent animals manifesting hyperplasia localized to bronchioles (C). p-Values calculated by two-way ANOVA multiple comparisons with Sidak testing (A) or one-way ANOVA multiple comparison with Tukey testing (B). **p<0.01, ***p<0.001, ****p<0.0001.

![Figure 4—figure supplement 7.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig4-figsupp7-v1.jpg)

**Figure 4—figure supplement 7.:** Percent of the indicated organs with tumors from Rosa26CreERT2/+;KrasLSL-rareG12D/+ mice (n = 7) 20 months after tamoxifen injection.

To identify the tissues permissive to tumorigenesis by each of these different alleles, eight different organs were removed from the mice during necropsy and analyzed for pathological changes as above. While there was much overlap, the prevalence and severity of specific cancer types varied between alleles, arguing that the different alleles can lead to differences in the tumor landscape (Figure 4B, Figure 4—figure supplement 5). This manifested in four general patterns of tissue permissivity: hematolymphopoietic neoplasias increased in severity with the level of active oncoprotein, squamous tumors were preferentially induced by the G12D-mutant alleles, carcinomas were induced by all four alleles, while many organs were resistant to oncogenic RAS-driven tumorigenesis within the time frame of the study (Figure 4B, Figure 4—figure supplement 5, and Supplementary file 4).

### A tissue sensitive to Kras activity

The incidence of hematolymphopoietic neoplasias increased with the biochemical activity of the Kras oncoprotein, as determined from analysis of MEF cultures and lung tissue. In more detail, the spleen and thymus from eight to ten mice from each of the four cohorts were removed at necropsy, after which H&E-stained sections were assayed for the presence and grade of hematolymphopoietic neoplasias as above. Beginning with the least active oncoprotein, most of the KrasLSL-natG12D mice after tamoxifen injection had no evidence of hematolymphopoietic neoplasms, although some mice had pathological features consistent with malignant lymphoma. The incidence of malignant lymphoma increased with KrasLSL-natQ61R allele, and then again upon activating the KrasLSL-comG12D allele. Pathological analysis also revealed medullary hyperplasia in the thymus, as well as leukemic infiltrates in the kidneys and pancreas of these latter mice, suggesting further progression of the lymphomas with this allele. Lastly, activating the KrasLSL-comQ61R allele induced severe myeloproliferative disease (MPD) with 100% penetrance, with extensive myeloproliferative infiltrates throughout many tissues (Figure 4B, C, Figure 4—figure supplement 5, Supplementary file 4 and 5, and not shown). While we cannot discount high oncogenic activity leading to a different hematopoietic disease in these later mice, we suggest that the incredibly short latency of the onset of severe systemic myeloid neoplasia may instead preclude development of longer latency tumors, such as lymphopoietic neoplasms. Thus, with this proviso, we suggest that hematolymphopoietic neoplasia are sensitive to the level of oncogenic activity, being induced at the lowest level of active Kras and progressively becoming more aggressive with increased activity.

### Tissues sensitive to Kras mutation type

Proliferative lesions of forestomach and oral squamous epithelium were preferentially induced by the oncogenic G12D mutant of Kras encoded by either native or common codons. In the case of the forestomach tumors, pathological analysis performed as above revealed that activation of the KrasLSL-natG12D allele induced squamous hyperplasia as well as mild and moderate grades of ‘atypical’ or dysplastic squamous lesions in the forestomach mucosa. Conversely, we did not detect any squamous proliferative changes upon activating the KrasLSL-natQ61R allele (Figure 4B and D, Figure 4—figure supplement 5, and Supplementary files 4 and 5), despite the previously detected higher activity of the KrasnatQ61R oncoprotein in MEFs and lung tissue. The same trend was observed when Kras was encoded with common codons, except the difference was less extreme between the two mutants, and shifted towards more aggressive disease. Specifically, activating the KrasLSL-comG12D allele induced more severe grades of forestomach squamous lesions while activation of the KrasLSL-comQ61R allele now induced lesions that were of moderate grades (Figure 4B and D, Figure 4—figure supplement 5, and Supplementary file 5). Similar analysis of oral tumors revealed that activating the KrasLSL-natG12D allele induced minimal to mild grade squamous lesions, while activating the KrasLSL-natQ61R allele was not tumorigenic. Again, when Kras was encoded with common codons there was a shift to a more aggressive disease. Namely, activating the KrasLSL-comG12D allele induced severe squamous papilloma in all mice, while activating the KrasLSL-comQ61R allele induced a mixture of moderate and severe grade squamous papillomas (Figure 4B and E, Figure 4—figure supplement 5, and Supplementary file 5). As such, in these two organs, the G12D mutant is associated with more severe phenotypes than the Q61R mutant, and changing codon usage to increase expression shifts this difference to a more advanced stage.

### Tissues sensitive to both Kras oncogenic activity and mutation type

Pathological analysis performed as above in the lung revealed that the G12D mutation consistently induced more AAH and/or adenomas than the Q61R mutation when Kras was encoded with either common or native rare codons, both in terms of the number of animals with these lesions and the total number of these lesions per animal (Figure 4B and F, Figure 4—figure supplements 5; 6A, and Supplementary file 5). As was the case with forestomach and oral lesions, converting rare codons to common amplified the severity of lesions detected, which was particularly evident in the confluence of large peripheral AAH lesions induced preferentially by theKrasLSL-comG12D allele (Figure 4B and F, Figure 4—figure supplements 5; 6B). However, no BH lesions were induced by either mutant when Kras was encoded with native rare codons and instead were only prevalent when Kras was encoded with common codons. Further, the number of animals with BH lesions was higher upon activating the KrasLSL-comQ61R compared to the KrasLSL-comG12D allele (Figure 4—figure supplements 5; 6C). Assuming that AAH and BH lesions represent different types of tumors (and not different stages of the same tumor type), we suggest that tumorigenesis in the lung is influenced by both the degree of Kras activation and the mutation type, although temporal analysis argues (Figure 2) that the level of Kras activation nevertheless dominates tumorigenesis in this tissue.

### Tissues resistant to oncogenic Kras

Despite widespread tumorigenesis, we note that no overt proliferative lesions were detected at necropsy or by histopathological analysis in the pancreas, kidney, or liver (Figure 4—figure supplement 5 and Supplementary file 4). A gross survey of other organs such as the colon, intestine, heart, skin, and mammary glands similarly failed to reveal macroscopically detectable tumors (not shown). In agreement, many of these same tissues, including pancreatic, were reported to be refractory to tumorigenesis upon activating a KrasLSL-G12D allele in the adult mice by CreER expressed from the Rosa26 (Parikh et al., 2012; van der Weyden et al., 2011), CK19 (Ray et al., 2011), or Ubc9 (Matkar et al., 2011) loci. Thus, many organs appear to be intrinsically resistant to the tumorigenic effects of oncogenic Kras, regardless of the mutation type or expression levels tested, at least within the time frame of this study and in the tested Rosa26CreERT2/+ background.

## Discussion

Here, we describe the effect of activating four inducible oncogenic Kras alleles encoding two very different mutants in a native rare versus common codon background to explore the mechanisms underlying the bias of specific oncogenic KRAS mutations towards distinct cancer types. We suggest that the unique tumor patterns arising from each of these mutant alleles implies that tissues differ in their sensitivities to quantitative and/or qualitative RAS signaling, both as a product of oncoprotein signaling and the cellular response thereof. We acknowledge four caveats to this approach. First, these four alleles were generated by fusing the first three coding exons, an artificial gene architecture, and hence can only be compared to themselves and not to other types of Kras alleles. Second, these alleles were induced by an injection of tamoxifen to activate CreER expressed from the Rosa26 locus. Admittedly, this is an unnatural situation whereby oncogenic Kras is expressed all at once in a multitude of tissues, potentially perturbing homeostasis in the whole animal. Nevertheless, as the identical design was applied to all four alleles, comparisons can be made within this allelic set. Third, Kras activity of this allelic set was defined in MEFs and lung tissue. We therefore acknowledge that cell-type differences in regulatory feedback pathways (Lake et al., 2016; Liu et al., 2018) or codon-dependent expression (Peterson et al., 2020) could result in different levels of Kras expression, activation, or signaling compared to that observed in MEF cultures and lung tissue, which were used to define the activity of each Kras oncoprotein. Fourth, by the nature of the experimental design, tissue types with slower tumor progression are underrepresented, and hence may respond differently to activation of the different Kras alleles when assessed more specifically.

With these limitations in mind, transcriptome analysis shortly after activating these alleles revealed similarities between the four, but also distinct transcriptional changes. This began with activation of the KrasLSL-natG12D allele, which induced EMT and differentiation hallmarks. EMT is known to promote stem cell-like fates (Floor et al., 2011; Mani et al., 2008) and activation of oncogenic Kras in the murine lung generates tumors with many tissue lineages (Tata et al., 2018). Taken together, we suggest that the transcriptional signature induced by the KrasnatG12D oncoprotein reflects either reprogramming towards or an expansion of cells with multipotent characteristics. In support, single-cell transcriptome profiling of lung tumors induced by targeted delivery of AAV-Cre in an KrasLSL-G12D/+;Trp53fl/fl background identified a distinct population with a mixed cellular identity (Marjanovic et al., 2020). At the other end of the spectrum, activating the KrasLSL-comQ61R allele induced transcriptional hallmarks consistent with overt oncogenic signaling. Thus, as the level of Kras biochemical activity increased, so did the transcriptional signatures of RAS signaling, which at its crescendo resulted in transcriptional signatures indicative of hyperproliferation and oncogenic stress. Nevertheless, within this overarching pattern of increased signaling we also find evidence for both mutation- and codon (expression)-specific transcriptional responses.

Globally activating these four alleles revealed four tumorigenic patterns. First, hematolymphopoietic neoplasias appeared to be largely driven by the amount of active Kras, as defined by RBD pull-down in both MEFs and lung tissue, as well as qRT-PCR of Kras target genes, transcriptome analysis, and RPPA analysis in lung tissue. Namely, these neoplasias were induced at the lowest level of oncogenic activity and increased in aggressiveness with increased Kras activity. To independently validate this result, we found that globally activating a ‘super-rare’ version of KrasLSL-rareG12D allele encoded by the rarest codons induced hematolymphopoietic neoplasias, although in a much-protracted time frame (Figure 4—figure supplement 7 and Supplementary file 4). This further supports hematolymphopoietic tissues as being more permissive to oncogenic Ras activity, suggestive of a dependency on quantitative signaling. Second, proliferative lesions of forestomach and oral squamous epithelium were preferentially induced by G12D-mutant alleles. Such a finding points towards qualitative signaling differences potentially driving these tumors, with higher expression shifting the effects to more aggressive grades. Equally plausible, however, perhaps either a RasGEF or RasGAP is uniquely expressed in these tissues that preferentially interacts with or affects signaling of only one of these mutants, implying quantitative signaling unique to the G12D mutant in these specific tissues. In support, GEF-mediated GTP exchange is more rapid with a Q61L versus G12V mutant of Kras (Smith et al., 2013), the RasGEF SOS1 is inactive toward KRASG12R (Hobbs et al., 2020), and KRASQ61H has diminished sensitivity to SHP2 inhibitors when compared to G12 or G13 mutants (Gebregiworgis et al., 2021). Third, the lung was sensitive to both the activation level and mutation type, with the G12D mutants favoring AAH and adenomas while high Ras activity favored BH lesions, perhaps reflecting a different cell-of-origin for these different lesions (Sutherland et al., 2014; Xu et al., 2014). AAH lesions may also speak to mutation-specific signaling, as here is a case in which we document Q61R mutants are more active, yet G12D mutants are more tumorigenic. With the caveat that Kras-GTP levels were determined in the entire lung, which may not reflect the actual levels in the cell-of-origin for AAH lesion, this implies qualitative differences may underlie these specific lesions. Fourth, many organs failed to develop lesions. We acknowledge that the short life span of some of the tested mice may very well prevent longer latency tumors from developing, and even though Rosa26-restricted Cre expression activated the four inducible oncogenic Kras alleles in tissues that did not form tumors, Cre may not be expressed in the tumor cell-of-origin within these tissues. With these caveats mind, these data suggest that many tissue are intrinsically resistant to the tumorigenic effects of oncogenic Kras. Instead, the hematopoietic system, lungs, forestomach, and oral mucosa are unique in being permissive to the tumorigenic potential of Kras oncoproteins, again, however, within the confines of the experimental design. Interestingly, these tissue sensitivities share some similarity to that of humans, namely, both species have RAS-associated cancers in the lung, mouth, and hematopoietic system but not in the mammary gland, skin, central nervous system, and so forth, but there is also some discordance (Prior et al., 2020).

How these different alleles drive the observed tumor patterns remains to be determined. However, comparing the two extreme cases – activation of the KrasLSL-natG12D versus the KrasLSL-comQ61R alleles in the lung – reveals transcription factors linked to the unique transcriptional responses of these two alleles. Specifically, we cross-referenced the transcriptome with a curated eukaryotic transcription factor database (Matys et al., 2003; Matys et al., 2006), identifying a set of upregulated transcription factors that tracked with the GSEA hallmarks of each oncoprotein (Figure 5—figure supplement 1A, B and Supplementary file 6). Namely, transcription factors tracking with GSEA hallmarks EMT, Estrogen Response Early, KRAS Signaling DN, and Apical Junction in the case of activating the KrasLSL-natG12D allele in the lung, and GSEA hallmarks TNFα Signaling via NFκβ, Complement, P53 Pathway, KRAS Signaling UP, and Inflammatory Response in the case of activating the KrasLSL-comQ61R allele, again in the lung (Figure 5—figure supplement 1A, B). Further, our finding that oncogenic RAS mutations are not identical in terms of activity (GTP-loading), oncogenic potential (induction of lung tumors), and cellular response (transcriptome and RPPA analysis) suggests the intriguing possibility that different initiating RAS mutations may have different therapeutic sensitivities. Indeed, again censoring the GSEA hallmarks in these two extreme cases for pharmacological targets already drugged in the clinic identified FLT4/PDGFRB/KIT, EGFR, and ABL1/SRC as specific to an activated KrasLSL-natG12D allele, while AKT1/2, PI3KCA/CD/CG, SYK, RAF1, JAK2, TGFBR1, and CDK1/2/9 were specific to an activated KrasLSL-comQ61R allele (Figure 5).

![Figure 5.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig5-v1.jpg)

**Figure 5.:** Druggable kinases positively enriched in GSEA hallmarks identified in Figure 3D (blue KrasLSL-natG12D/+, red KrasLSL-comQ61R/+). * Adjusted p-value<5%.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/75715/elife-75715-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A, B) Mean ± SEM of log2 fold change (Log2FC) differential expression of genes (Kras LSL-comQ61R versus Kras LSL-natG12D) activated by transcription factors enriched in GSEA hallmarks of (A) Kras LSL-natG12D, and (B) Kras LSL-comQ61R transcriptome (adjusted p-value less than 5%). +, genes common to more than one GSEA hallmark.

In summary, we suggest that tissues differ in their sensitivities to quantitative and/or qualitative RAS signaling both as a product of oncoprotein signaling and the cellular response thereof. We find that the level of oncogenic activity favors hematolymphopoietic neoplasias, the G12D mutant uniquely gives rise to oral and forestomach squamous tumors, while lung adenocarcinomas are sensitive to both mutation type and expression levels. The unique signaling dependencies of these tissues may, in turn, be capitalized upon to identify new therapeutic opportunities to target early tumorigenesis, when the tumors are particularly vulnerable, perhaps either as an early intervention or as a preventative measure in high-risk populations.

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
      <td>Antibody</td>
      <td>Anti-FLAG (mouse monoclonal)</td>
      <td>Sigma</td>
      <td>F1804</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-KRAS (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-30</td>
      <td>WB (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-βTubulin (mouse monoclonal)</td>
      <td>Sigma</td>
      <td>T5201</td>
      <td>WB (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-SV40 large T antigen (rabbit monoclonal)</td>
      <td>Cell Signaling</td>
      <td>15729</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>STBL3</td>
      <td>Thermo Fisher Scientific</td>
      <td>C737303</td>
      <td>Chemically competent cells</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>FuGENE 6 Transfection Reagent</td>
      <td>Promega</td>
      <td>E2691</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DC Protein Assay</td>
      <td>Bio-Rad</td>
      <td>5000112</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DNeasy Blood and Tissue DNA extraction Kit</td>
      <td>QIAGEN</td>
      <td>69504</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tamoxifen</td>
      <td>Sigma-Aldrich</td>
      <td>T5648-5G</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAeasy Kit</td>
      <td>QIAGEN</td>
      <td>74104</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNase-Free DNase Set</td>
      <td>QIAGEN</td>
      <td>79254</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>GenPoint kit</td>
      <td>Agilent</td>
      <td>K062011-2</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MycoAlert PLUS Mycoplasma detection kit</td>
      <td>Lonza</td>
      <td>LT07-703</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit IgG antibody</td>
      <td>Vector Laboratories</td>
      <td>BA-1000-1.5</td>
      <td>RPPA</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse IgG antibody</td>
      <td>Vector Laboratories</td>
      <td>BA-9200-1.5</td>
      <td>RPPA</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Active Ras Detection Kit</td>
      <td>Cell Signaling</td>
      <td>8821</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Ras GTPase ELISA Kit</td>
      <td>Abcam</td>
      <td>ab134640</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK-HT</td>
      <td>Counter et al., 1992</td>
      <td>Cell line created and maintained in C. Counter lab, validated by immunoblot for SV40 Large T antigen</td>
      <td>Cultured in DMEM and 10% FBSTested negative for mycoplasma</td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>MEF derived from KrasLSL-natG12D/+ mice</td>
      <td>This paper</td>
      <td>Validated by genotyping PCR</td>
      <td>Cultured in DMEM and 10% FBSTested negative for mycoplasma</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>MEF derived from KrasLSL-natQ61R/+ mice</td>
      <td>This paper</td>
      <td>Validated by genotyping PCR</td>
      <td>Cultured in DMEM and 10% FBSTested negative for mycoplasma</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>MEF derived from KrasLSL-comG12D/+ mice</td>
      <td>This paper</td>
      <td>Validated by genotyping PCR</td>
      <td>Cultured in DMEM and 10% FBSTested negative for mycoplasma</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>MEF derived from KrasLSL-comQ61R/+ mice</td>
      <td>This paper</td>
      <td>Validated by genotyping PCR</td>
      <td>Cultured in DMEM and 10% FBSTested negative for mycoplasma</td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>KrasLSL-natG12D/+</td>
      <td>This paper</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>KrasLSL-natQ61R/+</td>
      <td>This paper</td>
      <td></td>
      <td>Generated in Counter</td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>KrasLSL-comG12D/+</td>
      <td>This paper</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>KrasLSL-comQ61R/+</td>
      <td>This paper</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>KrasLSL-rareG12D/+</td>
      <td>This paper</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>ACTBFLPe/FLPe</td>
      <td>Jackson Laboratory</td>
      <td>003800</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>CC10CreER/CreER; Rosa26CAG-fGFP/CAG-fGFP</td>
      <td>Xu et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>Rosa26CreERT2/CreERT2</td>
      <td>Jackson Laboratory</td>
      <td>008463</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pcDNA3.1</td>
      <td>Thermo Fisher Scientific</td>
      <td>V79020</td>
      <td>Mammalian expression vector backbone</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pcDNA3.1+FLAG-KrasnatG12D</td>
      <td>This study</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pcDNA3.1+FLAG-KrasnatQ61R</td>
      <td>This study</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pcDNA3.1+FLAG-KrascomG12D</td>
      <td>This study</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pcDNA3.1+FLAG-KrascomQ61R</td>
      <td>This study</td>
      <td></td>
      <td>Generated in Counter Lab</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBABE-neo largeTcDNA</td>
      <td>Hahn et al., 2002</td>
      <td>Addgene #1780</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>MSCV-Cre-Hygro</td>
      <td>Wang et al., 2010</td>
      <td>Addgene #34565</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ version 1.52k with Java 1.8.0_172</td>
      <td>Schneider et al., 2012</td>
      <td>https://imagej.nih.gov/ij/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Image Lab</td>
      <td>Bio-Rad</td>
      <td>https://www.bio-rad.com/en-us/product/image-lab-software</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism v8</td>
      <td>GraphPad</td>
      <td>https://www.graphpad.com/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>bcl2fastq</td>
      <td>Illumina</td>
      <td>https://support.illumina.com/sequencing/sequencing_software/bcl2fastq-conversion-software.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR RNA-Seq alignment tool v2.7.8a</td>
      <td>Dobin et al., 2013</td>
      <td>https://github.com/alexdobin/STAR</td>
      <td>STAR (RRID:SCR_004463)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>Love et al., 2014</td>
      <td>http://www.bioconductor.org/packages/release/bioc/html/DESeq2.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GSEA</td>
      <td>Mootha et al., 2003</td>
      <td>https://www.gsea-msigdb.org/gsea/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R Studio</td>
      <td>R Development Core Team, 2020</td>
      <td>https://www.R-project.org</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MicroVigene Software Version 5.1.0.0</td>
      <td>VigeneTech</td>
      <td>http://www.vigenetech.com/Protein.htm</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BioRender</td>
      <td></td>
      <td>http://www.biorender.com</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Generation of KrasLSL-natG12D, KrasLSL-natQ61R, KrasLSL-comG12D, and KrasLSL-comQ61R alleles

A bacteria artificial chromosome was engineered with 7.5 kbp of 5′ flanking sequence Kras intron 1 DNA, a Lox-STOP-Lox cassette (LSL) (Feil et al., 1996), the first three coding exons fused together and encoded by either native (nat) codons or with 93 rare codons converted to the most commonly used codons in the mouse genome (com) and either a G12D or Q61 oncogenic mutation, followed by the N-terminal 564 bp of intron 4, an FRT-Neomycin-FRT cassette, and a further 1.5 kbp of 3′ flanking sequence (Figure 1A, Figure 1—figure supplement 1). The targeting cDNAs were each cloned into the targeting PL253 vector (Liu et al., 2003) and electroporated into 129S6/C57BL/6N (G4) ES cells. After selection, clones were screened using PCR and positive clones were selected for each engineered Kras allele, expanded, and frozen. At least two targeted clones per allele confirmed with a Southern hybridization were then microinjected into blastocysts to produce chimeras using standard procedures (Behringer, 2014). KrasLSL-natG12D(+neo)/+, KrasLSL-natQ61R(+neo)/+, KrasLSL-comG12D(+neo)/+, and KrasLSL-comQ61R(+neo)/+, chimeras (still retaining the neo cassette in the engineered Kras alleles) were crossed back to 129S6 mice. A genotyping PCR specific to the engineered Kras alleles with neo cassette was used to screen for germline transmission in clones. Each 129S6-KrasLSL-nat(+neo)/+ and 129S6-KrasLSL-com(+neo)/+ cohort was crossed with ACTBFLPe/FLPe (Jackson Laboratory, strain 003800) mice to remove the selection marker via FLP-mediated excision of the neo cassette (Dymecki, 1996). Removal of the neo cassette was confirmed with genotyping PCR. Resultant strains were backcrossed with 129S6 mice for five generations, generating the KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ strains used in this study. All mouse care and experiments were performed in accordance with a protocol approved by the Institutional Animal Care and Use Committee (IACUC) of Duke University (protocol no. A195-19-09).

### Codon usage plots

The codon usage index (Sharp and Li, 1987) was calculated using the relative codon frequency derived from codon usage in the mouse exome (Nakamura et al., 2000) with a sliding windows of 25 codons across the open reading frame (ORF) of each transcript. A theoretical murine Kras ORF encoded by the rarest codons at each position (gray dotted line) was plotted for reference (Figure 1—figure supplement 1).

### Genotyping

Genomic DNA was isolated from 1 to 2 mm piece of toes by boiling for 30 min in 100 μl Toe Lysis Buffer (25 mM NaOH and 0.2 mM EDTA), followed by neutralization with 1.5 volume of Neutralization Buffer (40 mM Tris–HCl pH 6.0). 1.2 μl of the isolated genomic DNA was subjected to PCR. Genotyping cell lines and mouse tissue was performed as above with 20 ng of genomic DNA isolated with a QIAGEN DNeasy Blood and Tissue DNA Extraction Kit (QIAGEN, #69504). All genotyping PCR reactions were performed using 0.4 U (0.08 μl) Platinum Taq polymerase (Invitrogen, #10342046) in 12.5 μl reaction volume with final concentration of 1.5–2 mM MgCl2, 0.2 mM of each dNTP, and 0.5 μM of each primer. Full-length gels and replicates are provided (Figure 1—source data 2, Figure 4—source data 1). Mice were genotyped using the following primers (also provided in Appendix 1):

KrasLSL(+neo) alleles:

KrasLSL-com alleles:

KrasLSL-nat alleles:

Recombination PCR:

CC10CreER alleles:

Rosa26CAG-fGFP alleles:

Rosa26CreERT2 alleles:

Kras LSL element:

CreER validation:

KrasLSL-rare alleles:

### Plasmids

N-terminal FLAG-tagged murine Kras cDNAs encoding KrasnatG12D, KrasnatQ61R, KrascomG12D, and KrascomQ61R were designed using the same sequence of the first three coding exons as described in the engineered alleles with the addition of the native Kras4B to the C-terminus and cloned into pcDNA3.1+ (Thermo Fisher). Plasmid sequences were verified by sequencing.

### Ectopic expression, immunoblots, and Ras activity assay

To validate the expression levels of the FLAG-tagged murine Kras cDNA constructs, 2 × 106 HEK-HT cells (Counter et al., 1992) were seeded in 10 cm tissue culture plates in DMEM with high glucose (Sigma-Aldrich, D5796) supplemented with 10% FBS (VWR, 97068-085), and transiently transfected the next day with the pcDNA3.1+ (empty vector) or the same plasmid encoding FLAG-KrasnatG12D, FLAG-KrasnatQ61R, FLAG-KrascomG12D, or FLAG-KrascomQ61R using FuGene 6 reagent (Promega, E2691) according to the manufacturer’s protocol. 48 hrs later, transfected cells were washed with cold PBS and pelleted. Cell pellets were lysed in 5 volumes of 1× lysis buffer (50 mM Tris–HCl pH 8.0, 150 mM NaCl, 1% NP40, 0.5% sodium deoxycholate, 0.1% SDS, and 5 mM EDTA) containing Protease Inhibitor Cocktail (Roche, 11836170001). The DC Protein Assay (Bio-Rad, 5000112) was used to measure protein concentration and 30 μg protein of each sample was resolved by SDS-PAGE, transferred to a PVDF membrane (Bio-Rad, 1704273), blocked in 5% milk, and immunoblotted by the following antibodies in 5% BSA (Sigma, A7906-500G): FLAG (Sigma, F1804; diluted 1:1000), KRAS (Santa Cruz, SC-30; diluted 1:500), and ß-Tubulin (Sigma, T5201; diluted 1:10,000). Primary antibody incubation was performed at room temperature for 1 hr followed by the secondary antibody incubation at 4°C overnight. To measure biochemical activity of the FLAG-tagged Kras constructs, cells were seeded, transfected, washed with PBS as above, after which cell pellets were lysed and immediately assayed with the Active Ras Detection Kit (Cell Signaling, #8821) or Ras GTPase ELISA Kit (Abcam, ab134640) according to the manufacturer’s protocol. Measurements were done with two technical replicates of four serial dilutions and data shown are representative of two independent biological replicates. HEK-HT cells were confirmed to be mycoplasma-negative. Full-length images of immunoblots and replicates are provided (Figure 1—source data 1).

### Mouse embryonic fibroblasts (MEFs)

KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ mice were crossed with 129S6 mice for timed pregnancies to isolate embryos 12.5 to 13.5 days postcoitum, as previously described (Serrano et al., 1997). Pairs of primary MEF cultures derived from two separate embryos from each cohort were cultured in DMEM with high glucose (Sigma-Aldrich, D5796) supplemented with 10% FBS (VWR, 97068-085) and then immortalized by infection with an amphotropic retrovirus derived from plasmid pBABE-neo largeTcDNA (a gift from Robert Weinberg, Addgene plasmid #1780) (Hahn et al., 2002) using standard methodologies (O’Hayer and Counter, 2006). Paired parental MEF lines that were not infected with the pBABE-neo largeTcDNA were used as a negative control for antibiotic selection. Stable immortalized MEF cultures were selected in 400 μg/ml Geneticin (Thermo Fisher, 10131035) and again infected with an amphotrophc retrovirus derived from plasmid MSCV-Cre-Hygro (a gift from Kai Ge, Addgene plasmid #34565) to activate the mutant Kras allele (Wang et al., 2010). The stable Cre-expressing MEF cultures were selected in 500 μg/ml Hygromycin (Thermo Fisher, 10687010). Paired immortalized KrasLSL-natG12D/+ MEF lines that were not infected with MSCV-Cre-Hygro were used as negative control for Hygromycin selection. Genomic DNA was isolated from the resultant cells using QIAGEN DNeasy Blood and Tissue DNA Extraction Kit (QIAGEN, #69504) and subjected to PCR to detect recombination of the KrasLSL alleles as described above. Paired immortalized MEF lines for each clone that were not infected with the MSCV-Cre-Hygro were used as negative control for recombination PCR. MEF cultures were confirmed to be mycoplasma-negative. Full-length gel image is provided (Figure 1—source data 2).

### Immunoblot and Ras activity assays in MEF cultures

The aforementioned pairs of independently derived KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ MEF cultures stably expressing Cre were grown in DMEM with high glucose (Sigma-Aldrich, D5796) supplemented with 10% FBS (VWR, 97068-085) in 15 cm dishes to prepare lysates for immunoblots and Ras activity assays. We note here that immortalized MEF cultures derived from KrasLSL-comQ61R/+ mice exhibited decreased recombination rate compared to MEFs derived from the other three genotypes, potentially due to resistance to hygromycin. Given this, we generated single colonies from this line after hygromycin selection for all experiments investigating Kras expression and activity. Two independent cell lines from immortalized KrasLSL-natG12D/+ MEF cultures without Cre were used as negative control to Cre-induced Kras expression. Once cells reached 85 to 90% confluency, FBS supplemented media was removed and replaced with plain DMEM with high glucose (Sigma-Aldrich, D5796) without FBS overnight. For serum stimulated lysates, cells were serum stimulated for 5 min by adding FBS to a final concentration of 10%. After serum starvation and stimulation, MEF cells were washed with cold PBS and pelleted. Cell pellets were lysed in 1 ml of lysis buffer provided in the Active Ras Detection Kit (Cell Signaling, #8821) supplemented with Halt Protease Inhibitor Cocktail (Thermo Fisher, 78430). The DC Protein Assay (Bio-Rad, 5000112) was used to measure protein concentration and 20 μg protein of each sample was used to immunoblot for total cell lysates. To measure biochemical activity of the endogenous Kras, 500 μg or 200 μg of each cell lysate was immediately assayed with the Active Ras Detection Kit (Cell Signaling, #8821) according to the manufacturer’s protocol, except that incubation of lysates with RBD peptide was performed at 4°C overnight. Total cell lysates and lysates after RBD pull-down were resolved by 18% SDS-PAGE, transferred to a PVDF membrane (Bio-Rad, 1704273), blocked in 5% milk, and immunoblotted by the following antibodies in 5% BSA (Sigma, A7906-500G): KRAS (Santa Cruz, SC-30; diluted 1:500) and ß-Tubulin (Sigma, T5201; diluted 1:10,000). Primary antibody incubation was performed at 4°C overnight followed by the secondary antibody incubation for 3 hrs at room temperature. Immunoblots shown are representative of two independent MEF lines. Full-length images of immunoblots and replicates are provided (Figure 1—source data 3).

### Tumorigenesis studies

KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ mice were crossed with either CC10CreER/CreER;Rosa26CAG-fGFP/CAG-fGFP (a gift from Mark Onaitis) (Xu et al., 2012) or Rosa26CreERT2/CreERT2 (Jackson Laboratory, strain 008463) mice and resultant offspring with the desired alleles were selected by genotyping. At six to eight weeks of age, selected littermates with random distribution of males and females received four intraperitoneal injections of tamoxifen (Sigma-Aldrich, T5648-5G, CAS# 10540-29-1) dissolved in corn oil (Sigma-Aldrich, C8267) and filter sterilized for a dose of 250 μg/g body weight to induce Cre-mediated recombination of the LSL cassette, activating the engineered oncogenic mutant Kras alleles. Mice from the first cross were humanely euthanized 1, 2, 3, 4, 5, or 6 months later while mice from the second cross were euthanized upon moribundity. To prevent age-related outcomes, four mice that did not reach moribundity by 300 days were euthanized at one year of age, which we reasoned to suffice to show tumorigenesis as it is about eight times longer than the previously identified average moribundity of five to six weeks with the tamoxifen-treated Rosa26CreERT2/+;KrasLSL-G12D/+ mice (Parikh et al., 2012). Selected tissues were removed at necropsy and fixed in 10% formalin (VWR, 89370-094) for 24 to 48 hrs, then post-fixed in 70% ethanol (VWR, 89125-166) until analysis.

### Tissue analysis

Animals were euthanized with inhaled carbon dioxide and subjected to a complete necropsy. Selected organs were sampled for microscopic examination, including lung, liver, kidney, spleen, thymus, stomach, pancreas, and macroscopic lesions. All tissues were fixed for 48 hrs in 10% neutral buffered formalin (VWR, 89370-094) and then post-fixed in 70% ethanol (VWR, 89125-166), processed routinely, embedded in paraffin with the flat sides down, sectioned at a depth of 5 μm, and stained by the H&E method. Routine processing of the lungs from CC10CreER/+;Rosa26CAG-fGFP/+ mice was performed by the Duke Research Immunohistology Lab, while all tissues from Rosa26CreERT2/+ mice were processed by IDEXX Laboratories. Tissues and H&E slides were evaluated by a board-certified veterinary anatomic pathologist with experience in murine pathology (Supplementary file 4 and 5).

### Tissue recombination analysis

At six to eight weeks of age, two female mice from each of the genotypes KrasLSL-natG12D/+, KrasLSL-natQ61R/+, KrasLSL-comG12D/+, and KrasLSL-comQ61R/+ in a Rosa26CreERT2/+ background were injected with tamoxifen as above, and seven days later euthanized. One age-matched female Rosa26CreERT2/+;KrasLSL-comG12D/+ mouse was alsoeuthanized as a no-tamoxifen control. At necropsy, the colon, duodenum, ileum, cecum, jejunum, pancreas, spleen, glandular stomach, forestomach, kidney, liver, lung, heart, and ovaries were removed, genomic DNA extracted, and the status of recombination of each of the four oncogenic mutant KrasLSL alleles determined by recombination PCR in duplicate, as described above. The intensities of bands corresponding to the unaltered wild-type Kras allele (WT) as well as the unrecombined and recombined oncogenic mutant KrasLSL alleles were quantified with ImageJ software and the recombination rates for each tissue type from each mouse calculated by dividing the densitometry of recombined allele to that of the wild-type allele. Full-length gels and replicates are provided (Figure 4—source data 1).

### Statistical analysis

Statistical analyses were performed using GraphPad Prism software version 8 (GraphPad Software). One-way ANOVA with Bonferroni’s multiple-comparisons test with a single pooled variance and a 95% CI were used for experiments with more than two groups. Reported p-values are adjusted to account for multiple comparisons. A p-value of <0.05 was considered statistically significant.

### Ras activity assay on lung tissue

At six to eight weeks of age, two mice with random distribution of males and females from each of the genotypes Rosa26CreERT2/+;KrasLSL-natG12D/+, Rosa26CreERT2/+;KrasLSL-natQ61R/+, Rosa26CreERT2/+;KrasLSL-comG12D/+, Rosa26CreERT2/+;KrasLSL-comQ61R/+, and Rosa26CreERT2/+ (control) were injected with tamoxifen as above, seven days latereuthanized, and their lungs were removed. Lungs were lysed in 5 ml of lysis buffer provided in the Active Ras Detection Kit (Cell Signaling, #8821) supplemented with Halt Protease Inhibitor Cocktail (Thermo Fisher, 78430). The DC Protein Assay (Bio-Rad, 5000112) was used to measure protein concentration, and 30 μg protein of each sample was used to immunoblot for total cell lysates. To measure biochemical activity of the endogenous Kras, 1 mg of each cell lysate was immediately assayed with the Active Ras Detection Kit (Cell Signaling, #8821) according to the manufacturer’s protocol, except for overnight incubation of the RBD pull-down reaction at 4°C. 30 μg of total cell lysates and 20% of the RBD pull-down mixture were resolved by 8 to 18% gradient SDS-PAGE, transferred to a PVDF membrane (Bio-Rad, 1704273), blocked in 5% milk, and immunoblotted by the following antibodies in 5% BSA (Sigma, A7906-500G): KRAS (Santa Cruz, SC-30; diluted 1:500), and ß-Tubulin (Sigma, T5201; diluted 1:10,000). Primary antibody incubation was performed at 4°C overnight followed by the secondary antibody incubation for 2 hrs at room temperature. Full-length images of immunoblots and replicates are provided (Figure 1—source data 4).

### RNA-seq

For the first experiment, at six to eight weeks of age, three mice with random distribution of males and females from each of the genotypes Rosa26CreERT2/+;KrasLSL-natG12D/+, Rosa26CreERT2/+;KrasLSL-natQ61R/+, Rosa26CreERT2/+;KrasLSL-comG12D/+, Rosa26CreERT2/+;KrasLSL-comQ61R/+, and Rosa26CreERT2/+ (control) were injected with tamoxifen as above, seven days later euthanized, and their lungs were removed. For the second RNA-seq experiment, the experiment was repeated exactly as before except with Rosa26CreERT2/+;KrasLSL-natG12D/+ versus Rosa26CreERT2/+;KrasLSL-comQ61R/+ mice. Tissue lysis and RNA extraction steps were performed in a chemical hood, and all instruments and tools were sprayed with RNaseZAP (Sigma, R2020) to prevent RNA degradation. Isolated lungs were immediately stored in RNA stabilizing solution RNAlater (Sigma, R0901) at 4°C overnight and then transferred to –80°C for long-term storage. Lung tissues were thawed, weighed, and pulverized with mortar and pestle in the presence of liquid nitrogen. RNA extraction was performed immediately thereafter using RNAeasy Kit (QIAGEN, 74104) according to the manufacturer’s instructions. Briefly, tissue lysates were prepared according to the kit instructions and tissue clumps were removed using QIAshredder columns (QIAGEN, 79654). Cleared lysates were applied to RNeasy silica columns and on-column DNase digestion was performed using RNase-Free DNase Set (QIAGEN, 79254) to remove DNA in silica membrane. Following wash steps, RNA was eluted in RNase-free water that was treated with RNAsecure RNase Inactivation Reagent (Thermo Fisher, AM7005) according to the manufacturer’s instructions. Extracted total RNA quality and concentration were assessed on Fragment Analyzer (Agilent Technologies) and Qubit 2.0 (Thermo Fisher Scientific), respectively. Samples with RIN less than 7 were not sequenced. RNA-seq libraries were prepared using the commercially available KAPA Stranded mRNA-Seq Kit (Roche). In brief, mRNA transcripts were captured from 500 ng of total RNA using magnetic oligo-dT bead. The mRNA was then fragmented using heat and magnesium, and reverse transcribed using random priming. During second-strand synthesis, the cDNA:RNA hybrid was converted into to double-stranded cDNA (dscDNA) and dUTP was incorporated into the second cDNA strand, effectively marking this strand. Illumina sequencing adapters were ligated to the dscDNA fragments and amplified to produce the final RNA-seq library. The strand marked with dUTP was not amplified, allowing for strand-specific sequencing. Libraries were indexed using a dual-indexing approach allowing for all the libraries to be pooled and sequenced on the same sequencing run. Before pooling and sequencing, fragment length distribution for each library was first assessed on a Fragment Analyzer (Agilent Technologies). Libraries were also quantified using Qubit. Molarity of each library was calculated based on Qubit concentration and average library size. All libraries were then pooled in equimolar ratio and sequenced. Sequencing was done on an Illumina NovaSeq 6000 sequencer. The pooled libraries were sequenced on one lane of an S-Prime flow cell at 50 bp paired-end. Once generated, sequence data was demultiplexed and Fastq files generated using bcl2fastq v2.20.0.422 file converter from Illumina. The RNA-seq data has been deposited in NCBI’s Gene Expression Omnibus (Edgar et al., 2002). Initial and secondary RNA-seq data are available through GEO Series accession numbers GSE181628 and GSE181627, respectively, and are accessible under the project GSE181629 (https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE181629).

### Transcriptome analysis

RNA-seq data was processed using the TrimGalore toolkit (http://www.bioinformatics.babraham.ac.uk/projects/trim_galore), which employs Cutadapt (Martin, 2011) to trim low-quality bases and Illumina sequencing adapters from the 3′ end of the reads. Only reads that were 20 nucleotides or longer after trimming were kept for further analysis. Reads were mapped to the GRCm38v73 version of the mouse genome and transcriptome (Kersey et al., 2012) using the STAR RNA-seq alignment tool (Dobin et al., 2013). Reads were kept for subsequent analysis if they mapped to a single genomic location. Gene counts were compiled using the HTSeq tool (http://www-huber.embl.de/users/anders/HTSeq/). Only genes that had at least ten reads in any given library were used in subsequent analysis. Normalization and differential expression were carried out using the DESeq2 (Love et al., 2014) Bioconductor (Huber et al., 2015) package with the R statistical programming environment (http://www.R-project.org). The false-discovery rate was calculated to control for multiple hypothesis testing (GSE181628). GSEA (Mootha et al., 2003) was performed to identify hallmarks and pathways associated with altered gene expression for each of the comparisons performed (Figure 3B and C, Figure 3—figure supplement 8, Figure 3—source data 2). To identify transcription factors significantly enriched, the differential expression data from KrasLSL-natG12D/+ and KrasLSL-comQ61R/+ transcriptomes was trimmed to genes whose adjusted p-value is less than 5% and whose log2 fold-change either larger than +1 or lower than –1. The trimmed dataset was cross-referenced with TRANSFAC, a curated eukaryotic transcription factor dataset, retrieved from Harmonizome web portal (Matys et al., 2003; Matys et al., 2006; Rouillard et al., 2016). Retrieved gene transcription factor pairs from TRANSFAC were then censored to the transcription factors enriched in KrasLSL-natG12D/+ and KrasLSL-comQ61R/+ specific GSEA hallmarks including more than four such gene transcription factor pairs both with p-value less than 5% (Figure 5—figure supplement 1). To identify low and high Kras-specific druggable kinases, the transcriptome enriched in KrasLSL-natG12D/+ and KrasLSL-comQ61R/+ specific GSEA hallmarks were cross-referenced with kinases whose clinical inhibitors were previously surveyed (Klaeger et al., 2017). The kinases enriched in KrasLSL-natG12D/+ and KrasLSL-comQ61R/+ are shown in blue and red, respectively, with adjusted p-value less than 5% highlighted (Figure 5).

### Reverse transcription quantitative real-time PCR (qRT-PCR)

At six to eight weeks of age, two to three mice with random distribution of males and females from each of the genotypes Rosa26CreERT2/+;KrasLSL-natG12D/+, Rosa26CreERT2/+;KrasLSL-natQ61R/+, Rosa26CreERT2/+;KrasLSL-comG12D/+, Rosa26CreERT2/+;KrasLSL-comQ61R/+, and Rosa26CreERT2/+ (control) were injected with tamoxifen as above, and seven days later euthanized to harvest lungs. RNA extraction was performed as mentioned above, followed by first-strand cDNA synthesis from 2 μg RNA, and real-time quantitative PCR using GoTaq 2-Step RT-qPCR kit (Promega, A6110). All measurements were normalized against Actin as the internal control using the 2-ΔΔCt method (Figure 1—source data 5, Figure 3—source data 3). For qRT-PCR analysis for the second biological replicate, one of two negative controls did not have numerical data for two transcripts and hence was not used for plotting. Data shown are representative of two independent biological replicates, and the primer sequences are provided in Appendix 1.

### Reverse-phase protein microarray (RPPA)

At six to eight weeks of age, three to four mice with random distribution of males and females from each of the genotypes Rosa26CreERT2/+;KrasLSL-natG12D/+, Rosa26CreERT2/+;KrasLSL-comQ61R/+, and Rosa26CreERT2/+ (control) were injected with tamoxifen as above, seven days later euthanized, and their lungs were removed. Lungs were snap froze, and embedded in Optimal Cutting Temperature (O.C.T.) compound (Tissue-Tek, 4583). Five sections of 8 μm were cut, mounted on uncoated glass slides, and stored at −80°C until lysed. Whole-tissue lysates were obtained directly from the glass slides after sections were fixed in 70% ethanol, washed with deionized water, stained with hematoxylin (Sigma-Aldrich, H9627, CAS# 517-28-2) and Scott’s Tap Water (Electron Microscopy Sciences, 2607006), and dehydrated in an ascending series of ethanol (70, 95, and 100%). Solutions were supplemented with cOmplete Mini Protease Inhibitors (Roche Applied Science, 11836153001) to avoid proteins and phosphorylated residues degradation. Stained tissues were lysed in a 1:1 solution of Tissue Protein Extraction Reagent (Pierce, 78510) and 2× Tris-Glycine SDS Sample buffer (Invitrogen Life Technologies, LC2676) supplemented with 2.5% β-mercaptoethanol (Sigma-Aldrich, M3148, CAS# 60-24-2). Tissue lysates were immobilized onto nitrocellulose-coated slides (Grace Bio-labs, 505278) in three technical replicates using an Aushon 2470 arrayer (Quanterix) equipped with 185 μm pins as previously described (Baldelli et al., 2017). Reference standard curves for internal quality control were arrayed along with the tissue lysates along with a bovine serum albumin serial dilution curve to quantify total protein amount on each sample. To assess the amount of protein in each sample and for normalization purposes, selected arrays were stained with Sypro Ruby Protein Blot Stain (Molecular Probes, S12000) following the manufacturer’s instructions as previously described (Baldelli et al., 2021). Reblot Antibody Stripping solution (Chemicon, 2500) was used to treat the remaining arrays for 15 min at room temperature before antibody staining. Arrays were subsequently washed with PBS and incubated for at least 4 hrs in I-block reagent (Tropix, T2015). Using an automated system (Dako Cytomation), arrays were probed with selected antibodies targeting total proteins and post-translationally modified epitopes of kinases and their downstream substrates (Supplementary file 1). For their use on the array, antibodies were validated as previously described (Signore et al., 2017). After incubation with a primary antibody, each array was probed with a biotinylated anti-rabbit (Vector Laboratories, Inc BA-1000-1.5) or anti-mouse (Vector Laboratories, BA-9200-1.5) secondary antibodies matching the species of the primary antibody. Signal detection was performed using the GenPoint kit (Agilent, K062011-2), a commercially available tyramide-based avidin/biotin amplification system, coupled with a fluorescent streptavidin-conjugated IRDye680 dye (LI-COR Biosciences, 680RD) according to the manufacturer’s recommendation. As negative controls for the background signal, selected arrays were probed with the secondary antibody alone. Antibody, negative control, and Sypro Ruby-stained slides were scanned at the appropriate wavelength channel using a laser scanner (TECAN). Image analysis was performed by spot finding, subtraction of local background and unspecific binding generated by the secondary antibody, and normalization to the amount of total protein obtained from the Sypro Ruby-stained slide by MicroVigene Software Version 5.1.0.0 (VigeneTech) as previously described (Pin et al., 2014). Replicate values are averaged to generate a single-intensity RPPA value per sample. Raw data with these average values are shown in Supplementary file 1.

### RPPA analysis

RPPA data for each tissue was first processed by replacing intensity values of 0 with 1 to ease computation. Each value was then converted to log2 scale. To calculate log2 fold-change, we calculated the average log2 values of each target in each genotype and subtracted the average log2 values of the wild-type Kras allele of that target. Heatmaps for the log2 fold-change were plotted using R statistical programming environment (http://www.R-project.org). Note that RPPA analysis of one of the Rosa26CreERT2/+;KrasLSL-natG12D/+ mouse lungs was deemed an outlier as it shared little commonality with the other three biological replicates. As such, the RPPA analysis of this mouse was not included in Figure 1—figure supplement 6 and Figure 3—figure supplement 9.

### Generation of KrasLSL-rareG12D/+ mice and tumorigenesis study

An additional inducible Kras allele with the rarest codons was generated in the same manner as mentioned above from BAC design to chimera production (Figure 1—figure supplement 1). KrasLSL-rareG12D(+neo) chimeras were crossed back to 129S6 mice followed by ACTBFLPe/FLPe (Jackson Laboratory, strain 003800) mice to remove the neo selection marker via FLP-mediated excision (Dymecki, 1996). Both germline transmission and the removal of the neo cassette were confirmed with genotyping PCR as mentioned above. Resultant strain was backcrossed with 129S6 mice for five generations, generating the KrasLSL-rareG12D/+ strain. KrasLSL-rareG12D/+ mice were crossed with Rosa26CreERT2/CreERT2 (Jackson Laboratory, strain 008463) mice and animals with the desired alleles selected by genotyping. At six to eight weeks of age, seven mice with random distribution of males and females were injected with tamoxifen as above, and 22 months later euthanized. Lung, liver, kidney, spleen, thymus, stomach, pancreas, and femurs were removed at necropsy and fixed in 10% formalin (VWR, 89370-094) for 24 to 48 hrs, then post-fixed in 70% ethanol (VWR, 89125–166), processed routinely, embedded in paraffin with the flat sides down, sectioned at 5 μm, and stained with H&E. Routine processing of the tissues was performed by IDEXX Laboratories. Tissues and H&E slides were evaluated by a board-certified veterinary anatomic pathologist with experience in murine pathology.

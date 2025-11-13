# Generative modeling of multi-mapping reads with mHi-C advances analysis of Hi-C studies

## Authors

- Ye Zheng<sup>1</sup> ([ORCID: 0000-0002-8806-2761](https://orcid.org/0000-0002-8806-2761))
- Ferhat Ay<sup>2</sup>
- Sunduz Keles<sup>1</sup> ([ORCID: 0000-0001-9048-0922](https://orcid.org/0000-0001-9048-0922)) †

### Affiliations

1. Department of Statistics University of Wisconsin-Madison Madison United States
2. La Jolla Institute for Allergy and Immunology La Jolla United States
3. School of Medicine University of California, San Diego La Jolla United States
4. Department of Biostatistics and Medical Informatics University of Wisconsin-Madison Madison United States

† Corresponding author

## Abstract

Current Hi-C analysis approaches are unable to account for reads that align to multiple locations, and hence underestimate biological signal from repetitive regions of genomes. We developed and validated mHi-C, a multi-read mapping strategy to probabilistically allocate Hi-C multi-reads. mHi-C exhibited superior performance over utilizing only uni-reads and heuristic approaches aimed at rescuing multi-reads on benchmarks. Specifically, mHi-C increased the sequencing depth by an average of 20% resulting in higher reproducibility of contact matrices and detected interactions across biological replicates. The impact of the multi-reads on the detection of significant interactions is influenced marginally by the relative contribution of multi-reads to the sequencing depth compared to uni-reads, cis-to-trans ratio of contacts, and the broad data quality as reflected by the proportion of mappable reads of datasets. Computational experiments highlighted that in Hi-C studies with short read lengths, mHi-C rescued multi-reads can emulate the effect of longer reads. mHi-C also revealed biologically supported bona fide promoter-enhancer interactions and topologically associating domains involving repetitive genomic regions, thereby unlocking a previously masked portion of the genome for conformation capture studies.

## Introduction

DNA is highly compressed in the nucleus and organized into a complex three-dimensional structure. This compressed form brings distal functional elements into close spatial proximity of each other (Dekker et al., 2002; de Laat and Duboule, 2013) and has a far-reaching influence on gene regulation. Changes in DNA folding and chromatin structure remodeling may result in cell malfunction with devastating consequences (Corradin et al., 2016; Won et al., 2016; Javierre et al., 2016; Rosa-Garrido et al., 2017; Spielmann et al., 2018). Hi-C technique (Lieberman-Aiden et al., 2009; Rao et al., 2014) emerged as a high throughput technology for interrogating the three-dimensional configuration of the genome and identifying regions that are in close spatial proximity in a genome-wide fashion. Thus, Hi-C data is powerful for discovering key information on the roles of the chromatin structure in the mechanisms of gene regulation.

There are a growing number of published and well-documented Hi-C analysis tools and pipelines (Heinz et al., 2010; Hwang et al., 2015; Ay et al., 2014a; Servant et al., 2015; Mifsud et al., 2015; Lun and Smyth, 2015), and their operating characteristics were recently studied (Ay and Noble, 2015; Forcato et al., 2017; Yardımcı et al., 2017) in detail. However, a key and common step in these approaches is the exclusive use of uniquely mapping reads. Limiting the usable reads to only uniquely mapping reads underestimates signal originating from repetitive regions of the genome which are shown to be critical for tissue specificity (Xie et al., 2013). Such reads from repetitive regions can be aligned to multiple positions (Figure 1A) and are referred to as multi-mapping reads or multi-reads for short. The critical drawbacks of discarding multi-reads have been recognized in other classes of genomic studies such as transcriptome sequencing (RNA-seq) (Li and Dewey, 2011), chromatin immunoprecipitation followed by high throughput sequencing (ChIP-seq) (Chung et al., 2011; Zeng et al., 2015), as well as genome-wide mapping of protein-RNA binding sites (CLIP-seq or RIP-seq) (Zhang and Xing, 2017). More recently, (Sun et al., 2018) and (Cournac et al., 2016) argued for a fundamental role of repeat elements in the 3D folding of genomes, highlighting the role of higher order chromatin architecture in repeat expansion disorders. However, the ambiguity of multi-reads alignment renders it a challenge to investigate the repetitive elements co-localization with the true 3D interaction architecture and signals. In this work, we developed mHi-C (Figure 1—figure supplements 1 and 2), a hierarchical model that probabilistically allocates Hi-C multi-reads to their most likely genomic origins by utilizing specific characteristics of the paired-end reads of the Hi-C assay. mHi-C is implemented as a full analysis pipeline (https://github.com/keleslab/mHiC) that starts from unaligned read files and produces a set of statistically significant interactions at a given resolution. We evaluated mHi-C both by leveraging replicate structure of public of Hi-C datasets of different species and cell lines across six different studies, and also with computational trimming and data-driven simulation experiments.

![Figure 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig1-v2.jpg)

**Figure 1.:** (A) Standard Hi-C pipelines utilize uni-reads while discarding multi-mapping reads which give rise to multiple potential contacts. (B) The total number of reads in different categories as a result of alignment to reference genome across the study datasets. Percentages of high-quality multi-reads compared to uni-reads are depicted on top of each bar. (C) Multi-mapping reads can be reduced to uni-reads within validation checking and genome binning pre-processing steps. (D) Aligned reads after validation checking and binning. Percentage improvements in sequencing depths due to multi-reads becoming uni-reads are depicted on top of each bar. (E) mHi-C modeling starts from the prior built by only uni-reads to quantify the relationship between random contact probabilities and the genomic distance between the contacts. This prior is updated by leveraging local bin pair contacts including both uni- and multi-reads and results in posterior probabilities that quantify the evidence for each potential contact to be the true genomic origin.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** 1. Read ends are aligned to reference genome separately allowing multi-reads and chimeric reads to be rescued. 2. Read ends are paired by their read query names. Multi-reads form more than one read pair with the same read query name. Read ends that fail to align form either unmapped reads or singleton reads and are discarded. Multi-reads with ends aligning to more than 99 positions are regarded as low-quality multi-reads and are excluded from the downstream analysis. 3. Validation checking to filter short-range contacts and alignments far away from restriction enzyme recognition sites. Contacts residing within the same restriction fragment, that is dangling end or self-circle, as well as adjacent fragments (religation) are discarded. The above three processing steps are applied to each read independently enabling parallel implementation.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** 4. PCR duplicates are removed to ensure that when a uni-read and a multi-read have the same alignment position and strand direction, the uni-read is kept. In the case of multi-reads that overlap with other multi-reads, the ones with alphabetically larger IDs are removed. 5. Genome is split into fix-sized non-overlapping intervals, that is bins or a fixed number of restriction fragments and, as a result, read alignment position pairs are reduced to bin pairs. Multi-reads, candidate alignment positions of which fall into the same bin, are reduced to uni-bin pairs. 6. mHi-C model estimates an allocation probability for each potential contact and enables filtering of contacts by thresholding this allocation probability.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Coverage is approximated as the ratio of the sequencing depth to the genome size. (B) Cis-to-trans ratio is defined as the number of valid intra-chromosomal contacts divided by the number of valid inter-chromosomal contacts.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Both the aligned uni-reads and multi-reads are taken into consideration.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) Percentages of mapped reads in different alignment categories. (B) Percentages of valid reads with both ends uniquely aligned to reference genome (Uni-reads), at least one end aligning to multiple positions and resulting in only one valid alignment after validation and binning (Multi-reads (Reduce to Uni-reads)), and reads with multiple potential valid alignment positions (Multi-reads (Modeling)).

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** (A) Numbers of multi-reads compared to the numbers of chimeric reads at each read end level. For Hi-C datasets with shorter read lengths, multi-reads constitute a larger percentage of the usable reads compared to chimeric reads. (B) Proportion of multi-reads among full-length alignable reads compared with that among chimeric reads. As expected, chimeric reads lead to larger percentages of multi-reads.

## Results

### Multi-reads significantly increase the sequencing depths of Hi-C data

For developing mHi-C and studying its operating characteristics, we utilized six published studies, resulting in eight datasets with multiple replicates, as summarized in Table 1 and with more details in Figure 1—source data 1: Table 1. These datasets represent a variety of study designs from different organisms, that is human and mouse cell lines as examples of large genomes and three different stages of Plasmodium falciparum red blood cell cycle as an example of a small and AT-rich genome. Specifically, they span a wide range of sequencing depths (Figure 1B), coverages and cis-to-trans ratios (Figure 1—figure supplement 3), and have different proportions of mappable and valid reads (Figure 1—figure supplement 4). Before applying mHi-C to these datasets and investigating biological implications, we first established the substantial contribution of multi-reads to the sequencing depth across these datasets with diverse characteristics. At read-end level (Supplementary file 1 for terminology), after the initial step of aligning to the reference genome (Figure 1—figure supplements 1 and 2), multi-reads constitute approximately 10% of all the mappable read ends (Figure 1—figure supplement 5A). Moreover, the contribution of multi-reads to the set of aligned reads further increases by an additional 8% when chimeric reads (Supplementary file 1) are also taken into account (Figure 1—source data 1: Table 2). Most notably, Figure 1—figure supplement 6A demonstrates that, in datasets with shorter read lengths, multi-reads constitute a larger percentage of usable reads compared to uniquely mapping chimeric reads that are routinely rescued in Hi-C analysis pipelines (Servant et al., 2015; Lun and Smyth, 2015; Durand et al., 2016). Moreover, multi-reads also make up a significant proportion of the rescued chimeric reads (Figure 1—figure supplement 6B). At the read pair level, after joining of both ends, multi-reads increase the sequencing depth by 18% to 23% for shorter read length datasets and 10% to 15% for longer read lengths, thereby providing a substantial increase to the depth before the read pairs are further processed into bin pairs (Figure 1C; Figure 1—source data 1: Table 3).

**Table 1.**
 Hi-C Data Summary.


<table>
  <thead>
    <tr>
      <th>Cell line</th>
      <th>Replicate</th>
      <th>Read length (bp)</th>
      <th>Restriction enzyme</th>
      <th>HiC protocol</th>
      <th>Source</th>
      <th>Resolution (kb)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IMR90</td>
      <td>rep1-6</td>
      <td>36</td>
      <td>HindIII</td>
      <td>dilution</td>
      <td>(Jin et al., 2013)</td>
      <td>40</td>
    </tr>
    <tr>
      <td>GM12878</td>
      <td>rep2-9</td>
      <td>101</td>
      <td>MboI</td>
      <td>in situ</td>
      <td>(Rao et al., 2014)</td>
      <td>5, 10*, 40*</td>
    </tr>
    <tr>
      <td>GM12878</td>
      <td>rep32, rep33</td>
      <td>101</td>
      <td>DpnII</td>
      <td>in situ</td>
      <td>(Rao et al., 2014)</td>
      <td>5</td>
    </tr>
    <tr>
      <td>A549</td>
      <td>rep1-4</td>
      <td>151</td>
      <td>MboI</td>
      <td>in situ</td>
      <td>(Dixon et al., 2018)</td>
      <td>10, 40</td>
    </tr>
    <tr>
      <td>ESC(2012)</td>
      <td>rep1, rep2</td>
      <td>36</td>
      <td>HindIII</td>
      <td>dilution</td>
      <td>(Dixon et al., 2012)</td>
      <td>40</td>
    </tr>
    <tr>
      <td>ESC(2017)</td>
      <td>rep1-4</td>
      <td>50</td>
      <td>DpnII</td>
      <td>in situ</td>
      <td>(Bonev et al., 2017)</td>
      <td>10, 40</td>
    </tr>
    <tr>
      <td>Cortex</td>
      <td>rep1-4</td>
      <td>50</td>
      <td>DpnII</td>
      <td>in situ</td>
      <td>(Bonev et al., 2017)</td>
      <td>10, 40</td>
    </tr>
    <tr>
      <td>P. falciparum</td>
      <td>three stages</td>
      <td>40</td>
      <td>MboI</td>
      <td>dilution</td>
      <td>(Ay et al., 2014b)</td>
      <td>10, 40</td>
    </tr>
  </tbody>
</table>

_*Replicates 2, 3, 4, and 6 of the GM12878 cell line datasets were process at 10 kb and 40 kb resolutions._

### Multi-reads can be rescued at multiple processing stages of mHi-C pipeline

As part of the post-alignment pre-processing steps, Hi-C reads go through a series of validation checking to ensure that the reads that represent biologically meaningful fragments are retained and used for downstream analysis (Figure 1—figure supplements 1 and 2, Supplementary file 1). mHi-C pipeline tracks multi-reads through these processing steps. Remarkably, in the application of mHi-C to all six studies, a subset of the high-quality multi-reads are reduced to uni-reads either in the validation step when only one candidate contact passes the validation screening, or because all the alignments of a multi-read reside within the same bin (Figure 1C; Supplementary file 1 and see Materials and methods). Collectively, mHi-C can rescue as high as 6.7% more valid read pairs (Figure 1D) that originate from multi-reads and are mapped unambiguously without carrying out any multi-reads specific procedure for large genomes and 10.4% for P. falciparum. Such improvement corresponds to millions of reads for deeper sequenced datasets (Figure 1—source data 1: Table 4). For the remaining multi-reads (Figure 1D, colored in pink), which, on average, make up 18% of all the valid reads (Figure 1—figure supplement 5B), mHi-C implements a novel multi-mapping model and probabilistically allocates them.

mHi-C generative model (Figure 1E and see Materials and methods) is constructed at the bin-pair level to accommodate the typical signal sparsity of genomic interactions. The bins are either fixed-size non-overlapping genome intervals or a fixed number of restriction fragments derived from the Hi-C protocol. The resolutions at which seven cell lines are processed are summarized in Table 1. In the mHi-C generative model, we denote the observed alignment indicator vector for a given paired-end read $i$ by vector $Y_{i}$ and use unobserved hidden variable vector $Z_{i}$ to indicate its true genomic origin. Contacts captured by Hi-C assay can arise as random contacts of nearby genomic positions or true biological interactions. mHi-C generative model acknowledges this feature by utilizing data-driven priors, $\pi_{(j,k)}$ for bin pairs $j$ and $k$, as a function of contact distance between the two bins. mHi-C updates these prior probabilities for each candidate bin pair that a multi-read can be allocated to by leveraging local contact counts. As a result, for each multi-read $i$, it estimates posterior probabilities of genomic origin variable $Z_{i}$. Specifically, $Pr(Z_{i,(j,k)}$ = 1 $|𝒀_{𝒊}$$Y_{i},\pi)$ denotes the posterior probability, that is allocation probability, that the two read ends of multi-read $i$ originate from bin pairs $j$ and $k$. These posterior probabilities, which can also be viewed as fractional contacts of multi-read $i$, are then utilized to assign each multi-read to the most likely genomic origin. Our results in this paper only utilized reads with allocation probability greater than 0.5. This ensured the output of mHi-C to be compatible with the standard input of the downstream normalization and statistical significance estimation methods (Imakaev et al., 2012; Knight and Ruiz, 2013; Ay et al., 2014a).

### Probabilistic assignment of multi-reads results in more complete contact matrices and significantly improves reproducibility across replicates

Before quantifying mHi-C model performance, we provide a direct visual comparison of the contact matrices between Uni-setting and Uni&Multi-setting using raw and normalized contact counts. Figure 2A and Figure 2—figure supplements 1–4 clearly illustrate how multi-mapping reads fill in the low mappable regions and lead to more complete matrices, corroborating that repetitive genomic regions are under-represented without multi-reads. Quantitatively, for the combined replicates of GM12878, 99.61% of the 5 kb bins with interaction potential are covered by at least 100 raw contacts under the Uni&Multi-setting, compared to 98.72% under Uni-setting, thereby allowing us to study 25.55 Mb more of the genome. For normalized contact matrices, the coverage increases from 99.42% in Uni-setting to 99.97% in Uni&Multi-setting (Figure 2—figure supplement 5). In addition to increasing the sequencing depth in extremely low contact bins for both raw and normalized contact counts, higher bin-level coverage after leveraging multi-mapping reads appears as a global pattern across the genome for raw contact matrices (Figure 2—figure supplements 6 and 7). Figure 2—figure supplement 8 provides the histogram of bin-level differences of normalized contact counts between the two settings and indicates a positive average difference. While some bins appear to have their contact counts decreased in the Uni&Multi-setting compared to Uni-setting after normalization (purple bar in Figure 2—figure supplement 8A), comparison of the raw contact counts in Figure 2—figure supplement 8B shows that these bins do indeed have lower raw contact counts in the Uni-setting compared to Uni&Multi-setting and that the reduction observed is an artifact of normalization. This also highlights that multi-reads alleviate the inflation of low raw contact count regions due to normalization. These major improvements in coverage provide direct evidence that mHi-C is rescuing multi-reads that originate from biologically valid fragments.

We assessed the impact of multi-reads rescued by mHi-C on the reproducibility from the point of both raw contact counts and significant interactions detected. We used the stratum-adjusted correlation coefficient proposed in HiCRep (Yang et al., 2017) for evaluating the reproducibility of Hi-C contact matrices. Figure 2B and Figure 2—figure supplements 9 and 10 illustrate that integrating multi-reads leads to increased reproducibility and reduced variability of stratum-adjusted correlation coefficients among biological replicates across all the study datasets. Furthermore, we observe that, for some chromosomes, for example, chr17 of IMR90 and chr16 of GM12878, the improvement in reproducibility stands out, without a systematic behavior across datasets. A close examination of improvement in reproducibility as a function of the ratio of rescued multi-reads to uni-reads across chromosomes highlights the larger proportion of multi-reads rescued for these chromosomes (Figure 2—figure supplement 11). To further assess that the improvement in reproducibility did not manifest due to an unaccounted systematic bias in the assignment of multi-reads, we evaluated reproducibility similarly between replicates of GM12878 and replicates of IMR90. Figure 2—figure supplement 12 shows that Uni-setting and Uni&Multi-setting lead to similar levels of reproducibility between replicates of these unrelated samples with all Wilcoxon rank-sum test p-values of the pairwise comparisons between Uni- and Uni&Multi-settings > 0.21; therefore, ruling out the possibility of a systematic bias as the source of improvement in reproducibility due to multi-reads.

In addition to the direct comparison of the raw contact matrices and their reproducibility, we identified the set of significant interactions by Fit-Hi-C (Ay et al., 2014a) and assessed the reproducibility of the identified interactions. Figure 2C shows that mHi-C significantly improves reproducibility of detected interactions across all the pairwise comparisons of replicates within each study dataset. Figure 2—figure supplement 13A presents more details on the degree of overlap among the significant interactions identified at 5% and 10% false discovery rate (FDR) across replicates for the IMR90 datasets. These comparisons highlight that significant interactions specific to Uni&Multi-setting have consistently higher reproducibility than those specific to Uni-setting across all pairwise comparisons. Since random contacts tend to arise due to short genomic distances between loci, we stratified the significant interactions based on distance and reassessed the reproducibility as a function of the genomic distance between the contacts (Figure 2—figure supplement 13B). Notably, significant interactions identified only by the Uni-setting and those common to both settings have a stronger gradual descending trend as a function of the genomic distance, indicating decaying reproducibility for long-range interactions. In contrast, Uni&Multi-setting maintains a relatively higher and stable reproducibility for longer genomic distances.

![Figure 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-v2.jpg)

**Figure 2.:** (A) Contact matrices of GM12878 with combined reads from replicates 2–9 are compared under Uni-setting and Uni&Multi-setting using raw and normalized contact counts for chr6:25.5 Mb - 28.5 Mb. White gaps of Uni-reads contact matrix, due to lack of reads from repetitive regions, are filled in by multi-reads, hence resulting in a more complete contact matrix. Such gaps remain in the Uni-setting even after normalization. Red squares at the left bottom of the matrices indicate the color scale. (B) Reproducibility of Hi-C contact matrices by HiCRep across all pairwise comparisons between replicates under the Uni- and Uni&Multi-settings (IMR90 and GM12878 are displayed). (C) Reproducibility of the significant interactions across replicates of the study datasets. Reproducibility is assessed by overlapping interactions detected at FDR of 5% for pairs of replicates within each study dataset.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp1-v2.jpg)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp2-v2.jpg)

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp3-v2.jpg)

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp4-v2.jpg)

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp5-v2.jpg)

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** Only chromosome 1–9 are shown and the pattern for the rest chromosomes are very similar. The dashed line is y = x.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** Uni&Multi-setting for (A) includes multi-reads with a posterior probability > 0.5, whereas (B) depicts more strict filtering with an allocation probability > 0.9 The dashed line is y = x. mHi-C rescues multi-reads from valid ligation fragments, resulting in a significant increase in contact counts.

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp8-v2.jpg)

**Figure 2—figure supplement 8.:** (A) Histogram of the bin-level differences between normalized contact counts of the Uni&Multi- and Uni-settings. Green bars represent increased counts under the Uni&Multi-setting, and purple ones indicate no change or decrease. Bins in the purple bar group are low coverage bins under the Uni-setting and have inflated normalized contact counts. Only chromosome 1–3 are shown, and the pattern for the rest of the chromosomes are very similar. (B) Raw contact count comparison of the top 0.01% bins of Panel A with drastically higher normalized contact counts under the Uni-setting compared to the Uni&Multi-setting (purple bars). The contact counts of these bins get inflated by normalization. The dashed lines are y = x.

![Figure 2—figure supplement 9.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp9-v2.jpg)

**Figure 2—figure supplement 9.:** Note that the box plots for the ESC-2012 cell line which only has two replicates are not displayed.

![Figure 2—figure supplement 10.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp10-v2.jpg)

![Figure 2—figure supplement 11.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp11-v2.jpg)

![Figure 2—figure supplement 12.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp12-v2.jpg)

**Figure 2—figure supplement 12.:** Each box contains reproducibility measurements on 23 chromosomes between every two pairs of replicates from GM12878 and IMR90. Within each panel, one GM12878 replicate contact matrix is compared with each of the six IMR90 replicates respectively for Uni- and Uni&Multi-settings.

![Figure 2—figure supplement 13.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig2-figsupp13-v2.jpg)

**Figure 2—figure supplement 13.:** (A) Significant interactions are classified into three categories: Uni-setting specific or Uni&Multi-setting specific or common to both. Reproducibility is evaluated by the percentage of significant interactions reproduced in another replicate within the same category. (B) Reproducibility of significant interactions stratified by genomic distance. Reproducibility is evaluated by the percentage of significant interactions reproduced in another replicate within the same category and genomic distance range.

### 2.4 Multi-reads detect novel significant interactions

At 5% false discovery rate, mHi-C detects 20% to 50% more novel significant interactions for relatively highly sequenced study datasets (Figure 3A and Figure 3—source data 1; Figure 3—figure supplement 1 for other FDR thresholds and resolutions). The gains are markedly larger for datasets with smaller sequencing depths (e.g., ESC-2012) or extremely high coverage (e.g., P. falciparum). Overall gains in the number of novel contacts persist as the cutoff for mHi-C posterior probabilities of multi-read assignments varies (Figure 3—figure supplement 2). At fixed FDR, significant interactions identified by the Uni&Multi-setting also include the majority of significant interactions inferred from the Uni-setting, indicating that incorporating multi-reads is extending the significant interaction list (low level of purple lines in Figure 3—figure supplement 2).

![Figure 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-v2.jpg)

**Figure 3.:** (A) Percentage increase in detected significant interactions (FDR 5%) by comparing contacts identified in Uni&Multi-setting with those of Uni-setting across study datasets at 40 kb resolution. (B) Percentage change in the numbers of significant interactions (FDR 5%) as a function of the percentage of mHi-C rescued multi-reads in comparison to uni-read and cis-to-trans ratios of individual datasets at 40 kb resolution. (C) Recovery of significant interactions identified at 1% FDR by analysis at 10% FDR, aggregated over the replicates of GM12878 at 40 kb resolution. Detailed descriptions of the groups are provided in Figure 3—figure supplement 6. (D) Average number of contacts falling within the significant interactions (5% FDR) that overlapped with each chromHMM annotation category across six replicates of IMR90 identified by Uni- and Uni&Multi-settings. (E) Average number of contacts (5% FDR) that overlapped with significant interactions and different types of ChIP-seq peaks associated with different genomic functions (IMR90 six replicates). Red/Green labels denote smaller/larger differences between the two settings compared to the differences observed in the ”Others’ category that depict non-peak regions.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Percentage change in the numbers of significant interactions gained (Green) and lost (Purple) by the Uni&Multi-setting compared to the Uni-setting across individual IMR90 replicates for varying FDR and allocation probability thresholds.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The relative percentage of multi-reads added to uni-reads as well as cis-to-trans ratio is leading impact factors (with p-values $\leq$ 0.005) followed by the percentage of mappable reads and valid reads.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Cis-to-trans ratio is defined as the number of valid intra-chromosomal contact counts divided by the number of valid inter-chromosomal contact counts.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** (A) Percentage change in the numbers of significant interactions of GM12878 datasets at 5 kb, 10 kb, 40 kb resolutions, respectively, across varying FDR thresholds. (B) Percentage change in the numbers of significant interactions of 8 replicates that are based on MboI as the restriction enzyme and two replicates with DpnII as restriction enzyme at 5 kb resolution across different FDR thresholds. (C) Percentage change in the numbers of significant interactions with respect to the replicate sequencing depth of all 10 replicates of GM12878 at 5 kb resolution across different FDR thresholds.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** Coverage is approximated as the ratio of the sequencing depth to the genome size.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp7-v2.jpg)

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp8-v2.jpg)

**Figure 3—figure supplement 8.:** Uni&Multi-setting. Specific (Uni FDR 10%) is the set of significant interactions identified at 1% FDR by the Uni&Multi-setting but are still unrecoverable by the Uni-setting even with a liberal FDR of 10%. The detailed descriptions of the groups are as follows: Uni-setting (FDR 1%): # of significant interactions identified by the Uni-setting at 1% FDR. Uni&Multi-setting (FDR 1%): # of significant interactions identified by the Uni&Multi-setting at 1% FDR. Uni-setting.Specific (Uni&Multi FDR 1%): # of significant interactions identified by Uni-setting (FDR 1%) but not by Uni&Multi-setting at 1% FDR. Uni-setting.Specific (Uni&Multi FDR 10%): # of significant interactions identified by Uni-setting (FDR 1%) but not by Uni&Multi-setting at 10% FDR. Uni&Multi-setting.Specific (Uni FDR 1%): # of significant interactions identified by Uni&Multi-setting (FDR 1%) but not by Uni-setting at 1% FDR. Uni&Multi-setting.Specific (Uni FDR 10%): # of significant interactions identified by Uni&Multi-setting (FDR 1%) but not by Uni-setting at 10% FDR.

![Figure 3—figure supplement 9.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp9-v2.jpg)

**Figure 3—figure supplement 9.:** Color labels are the same as Figure 3—figure supplement 8.

![Figure 3—figure supplement 10.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp10-v2.jpg)

**Figure 3—figure supplement 10.:** Color labels are the same as Figure 3—figure supplement 8.

![Figure 3—figure supplement 11.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp11-v2.jpg)

**Figure 3—figure supplement 11.:** Color label is the same as Figure 3—figure supplement 8.

![Figure 3—figure supplement 12.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp12-v2.jpg)

**Figure 3—figure supplement 12.:** Color label is the same as Figure 3—figure supplement 8.

![Figure 3—figure supplement 13.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp13-v2.jpg)

**Figure 3—figure supplement 13.:** Sets of ‘True’ interactions and ‘True’ non-interactions are defined by reproducible significant/insignificant interactions across replicate 1–4 of both Uni-setting and Uni&Multi-setting (See Materials and methods). Significant interactions of replicates 5 and 6 are utilized to compare ROC (A) and PR (B) curves among the Uni- and Uni&Multi-settings.

![Figure 3—figure supplement 14.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp14-v2.jpg)

**Figure 3—figure supplement 14.:** (A) Grouping the significant interactions into three groups (Uni-setting specific, Uni&Multi-setting specific, Common to both settings) reveals the largest enrichment differences in chromHMM annotation categories related to repetitive regions, such as Zinc Finger Genes & Repeats as well as Heterochromatin. (B) Average number of significant interactions across regions with a variety of ChIP-seq signals. Red/green labels denote smaller/larger differences between Uni-setting specific and Uni&Multi-setting specific compared to the differences observed in the ‘Others’ category that depicts non-peak regions.

![Figure 3—figure supplement 15.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp15-v2.jpg)

**Figure 3—figure supplement 15.:** Highlighted in grey is a region with significantly different marginal Hi-C signal between Uni-setting and Uni&Multi-setting.

![Figure 3—figure supplement 16.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp16-v2.jpg)

**Figure 3—figure supplement 16.:** Highlighted in grey is a region with significantly different marginal Hi-C signal between Uni-setting and Uni&Multi-setting.

![Figure 3—figure supplement 17.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig3-figsupp17-v2.jpg)

**Figure 3—figure supplement 17.:** Highlighted in grey is a region with significantly different marginal Hi-C signal between Uni-setting and Uni&Multi-setting.

We leveraged the diverse characteristics of the study datasets and investigated the factors that impacted the gain in the detected significant interactions due to multi-reads. The top row of Figure 3—figure supplement 3 summarizes the marginal correlations of the percentage change in the number of identified significant interactions (at 40 kb resolution and FDR of 0.05) with the data characteristics commonly used to indicate the quality of Hi-C datasets (excluding the high coverage P. falciparum dataset). These marginal associations highlight the significant impact of the relative contribution of multi-reads to the sequencing depth compared to uni-reads and cis-to-trans ratio of contacts (Figure 3—figure supplement 4). Figure 3—figure supplement 5 increase in the number of novel significant interactions for the GM12878 datasets in more detail across a set of FDR thresholds and at different resolutions, and includes two types of restriction enzymes. Specifically, Figure 3—figure supplement 5C illustrates a clear negative association between the sequencing depth and the percent improvement in the number of identified significant interactions at 5 kb resolution due to the larger impact of multi-reads on the smaller depth replicates. As an exception, we note that P. falciparum datasets tend to exhibit significantly higher gains in the number of identified contacts especially under stringent FDR thresholds (Figure 3A), possibly due to the ultra-high coverage of these datasets (Figure 3—figure supplement 6). In addition to these marginal associations, Figure 3B and Figure 3—figure supplement 7 display the percentage increase in the number of identified significant interactions as a function of the percentage increase in the real depth due to multi-reads and the cis-to-trans ratio across all the study datasets. A consistent pattern highlights that short read datasets with large proportion of mHi-C rescued multi-reads compared to uni-reads enjoy a larger increase in the number of identified significant interactions regardless of the FDR threshold, while for datasets with similar relative contribution of multi-reads, for example within lower depth IMR90, cis-to-trans ratios positively correlate with the increase in the number of identified significant interactions.

We next asked whether novel significant interactions due to rescued multi-reads could have been identified under the Uni-setting by employing a more liberal FDR threshold. Leveraging multi-reads with posterior probability larger than 0.5 and controlling the FDR at 1%, Fit-Hi-C identified 32.49% more significant interactions compared to Uni-setting (comparing dark green to dark purple bar in Figure 3C) and 36.43% of all significant interactions are unique to Uni&Multi-setting (light green bar over dark green bar in Figure 3C) collectively for all the four replicates of GM12878 at 40 kb resolution. We observed that 34.89% of these novel interactions (yellow bar over the light green bar in Figure 3C) at 1% FDR (i.e., 12.71% compared to the all the significant interactions under Uni&Multi-setting) cannot be recovered even by a more liberal significant interaction list under Uni-setting at 10% FDR. Conversely, Uni&Multi-setting is unable to recover only 4.60% of the Uni-setting contacts once the FDR is controlled at 10% for the Uni&Multi-setting (light blue over dark purple bar in Figure 3C), highlighting again that Uni&Multi-setting predominantly adds on novel significant interactions while retaining interactions that are identifiable under the Uni-setting. A similar analysis for individual replicates of IMR90 are provided in Figure 3—figure supplement 8 as well as those of GM12878 at the individual replicate level or collective analysis at 5 kb, 10 kb, and 40 kb resolutions in Figure 3—figure supplements 9–12. We further confirmed this consistent power gain by a Receiver Operating Characteristic (ROC) and a Precision-Recall (PR) analysis (Figure 3—figure supplement 13). The PR curve illustrates that at the same false discovery rate (1-precision), mHi-C achieves consistently higher power (recall) than the Uni-setting in addition to better AUROC performance.

### Chromatin features of novel significant interactions

To further establish the biological implications of mHi-C rescued multi-reads, we investigated genomic features of novel contacts. Annotation of the significant interactions with ChromHMM segmentations from the Roadmap Epigenomics project (Kundaje et al., 2015) highlights marked enrichment of significant interactions in annotations involving repetitive DNA (Figure 3D, Figure 3—figure supplement 14A). Most notably, ZNF genes and repeats and Heterochromatin states exhibit the largest discrepancy of the average significant interaction counts between the Uni- and Uni&Multi-settings. To complement the evaluation with ChromHMM annotations, we evaluated the Uni-setting and Uni&Multi-setting significant interaction enrichment of genomic regions harboring histone marks and other biochemical signals (ENCODE Project Consortium, 2012; Jin et al., 2013) (See Materials and methods) by comparing their average contact counts to those without such signal (Figure 3E and data on Dryad, https://doi.org/10.5061/dryad.v7k3140). Notably, while we observe that multi-reads boost the average number of contacts with biochemically active regions of the genome, they contribute more to regions that harbor H3K27me3 peaks (Figure 3E, Figure 3—figure supplement 14B). Such regions are associated with downregulation of nearby genes through forming heterochromatin structure (Ferrari et al., 2014). Figure 3—figure supplement 15–17 further provide specific examples of how increased marginal contact counts due to multi-reads are supported by signals of histone modifications, CTCF binding sites, and gene expression. Many genes of biological significance reside in these regions. For example, NBPF1 (Figure 3—figure supplement 15) is implicated in many neurogenetic diseases and its family consists of dozens of recently duplicated genes primarily located in segmental duplications (Safran et al., 2010). In addition, RABL2A within the highlighted region of Figure 3—figure supplement 16 is a member of RAS oncogene family.

### Multi-reads discover novel promoter-enhancer interactions

We found that a significant impact of multi-reads is on the detection of promoter-enhancer interactions. Overall, mHi-C identifies 14.89% more significant promoter-enhancer interactions at 5% FDR collectively for six replicates for IMR90 (Figure 4—source data 1: Table 1 and Figure 4—source data 2). Of these interactions, 13,313 are reproducible among all six replicates under Uni&Multi-setting (Figure 4—source data 1: Table 2) and 62,971 are reproducible for at least two replicates (Figure 4—source data 1: Table 3) leading to 15.84% more novel promoter-enhancer interactions specific to Uni&Multi-setting. Figure 4A provides WashU epigenome browser (Zhou et al., 2011) display of such novel reproducible promoter-enhancer interactions on chromosome 1. Figure 4—figure supplements 1–2 provides more such reproducible examples and Figure 4—figure supplement 3 depicts the reproducibility of these interactions in more details across the six replicates.

![Figure 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig4-v2.jpg)

**Figure 4.:** (A) mHi-C identifies novel significant promoter-enhancer interactions (green arcs) that are reproducible among at least two replicates in addition to those reproducible under the Uni-setting (purple arcs). Shaded and the boxed regions correspond to the anchor and target bins, respectively. The top track displays the contact counts associated with the anchor bin under Uni- and Uni&Multi-settings. Related chromHMM annotation color labels are added around the track. The complete color labels are consistent with ChromHMM 15-state model at https://egg2.wustl.edu/roadmap/web_portal/chr_state_learning.html. (B) Average gene expression with standard errors for five different scenarios of interactions that group promoters into six different categories. In the first panel, significant interactions involving promoters are classified into five settings, and the average gene expressions across genes with the corresponding promoters are depicted. The second panel involves two alignment settings and genes without any promoter interactions at 5% FDR. This panel is further separated into two categories: promoters that overlap with enhancer annotated regions and those that do not. The latter one serves as the baseline for average expression. Genes contributing to the third and fourth panel have promoter-enhancer, promoter-promoter interactions at 5% FDR. The fifth panel considers genes promoters of which have significant interactions with non-enhancer and non-promoter regions. Numbers in the parenthesis correspond to the number of transcripts in each category.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig4-figsupp1-v2.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig4-figsupp2-v2.jpg)

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** This is the individual replicate level data for Figure 4—figure supplement 2 in a large genome region.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Genes harboring significant interactions (at 5% FDR) within their promoters are grouped into different gene expression categories.

We next validated the novel promoter-enhancer interactions by investigating the expression levels of the genes contributing promoters to these interactions. Figure 4B supports that genes with significant interactions in their promoters generally exhibit higher expression levels (comparing bars 1–5 to bars 8–9 in Figure 4B). Furthermore, if these interactions involve an enhancer, the average gene expression can be 38.17% higher than that of the overall promoters with significant interactions (comparing bars 10–11 to bars 1–2 in Figure 4B). Most remarkably, newly detected significant promoter-enhancer interactions (bar 13 in Figure 4B) exhibit a stably higher gene expression level, highlighting that, without multi-reads, biologically supported promoter-enhancer interactions are underestimated. In addition, an overall evaluation of significant interactions (5% FDR) that considers interactions from promoters with low expression (TPM $\leq$ 1) as false positives illustrate that mHi-C specific significant promoter interactions have false positive rates comparable to or smaller than those of significant promoter interactions common to Uni- and Uni&Multi-settings (Figure 4—figure supplement 4). In contrast, Uni-setting specific interactions have elevated false positive rates.

### Multi-reads refine the boundaries of topologically associating domains

We next investigated the impact of mHi-C rescued multi-reads on the topologically associating domains (TADs) (Pombo and Dillon, 2015), where we used a broad definition of TADs to include contact and loop domains. We used the DomainCaller (Dixon et al., 2012; Dixon et al., 2015) to infer TADs of IMR90 datasets at 40 kb resolution and Arrowhead (Rao et al., 2014) for GM12878 datasets at 5 kb resolution under Uni&Multi-settings (Figure 5—source data 1 and 2). The detected TADs are compared to those under the Uni-setting. While this comparison did not reveal stark differences in the numbers of TADs identified under the two settings (Figure 5—figure supplement 1), we found that Uni&Multi-setting identifies 2.01% more reproducible TADs with 2.36% lower non-reproducible TADs across replicates (Figure 5A). Several studies have revealed the role of CTCF in establishing the boundaries of genome architecture (Ong and Corces, 2014; Tang et al., 2015; Hsu et al., 2017). While this is an imperfect indicator of TAD boundaries, we observed that a slightly higher proportion of the detected TADs have CTCF peaks with convergent CTCF motif pairs at the boundaries once multi-reads are utilized (Figure 5—figure supplement 2A–C). Figure 5B provides an explicit example of how the gap in the contact matrix due to depletion of multi-reads biases the inferred TAD structure. In addition to discovery of novel TADs (Figure 5—figure supplement 3) by filling in the gaps in the contact matrix and boosting the domain signals, mHi-C also refines TAD boundaries (Figure 5—figure supplements 4 and 5), and eliminates potential false positive TADs that are split by the contact depleted gaps in Uni-setting (Figure 5—figure supplements 6–8). The novel, adjusted, and eliminated TADs are largely supported by CTCF signal identified using both uni- and multi-reads ChIP-seq datasets (Zeng et al., 2015) as well as convergent CTCF motifs (Figure 5—figure supplement 2D), providing support for mHi-C driven modifications to these TADs and revealing a slightly lower false discovery rate for mHi-C compared to Uni-setting (Figure 5C, Figure 5—figure supplement 2E, and Figure 5—figure supplement 9).

![Figure 5.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-v2.jpg)

**Figure 5.:** (A) Percentage of topologically associating domains (TADs) that are reproducibly detected under Uni-setting and Uni&Multi-setting. TADs that are not detected in at least 4 of the six replicates are considered as non-reproducible. (B) Comparison of the contact matrices with superimposed TADs between Uni- and Uni&Multi-setting for chr10:72,550,000–97,550,000. Red squares at the left bottom of the matrices indicate the color scale. TADs affected by white gaps involving repetitive regions are highlighted in light green. Light green outlined areas correspond to new TAD boundaries. (C) False discovery rate of TADs detected under two settings. TADs that are not reproducible and lack CTCF peaks at the TAD boundaries are labeled as false positives. (D) Average number of repetitive elements at the boundaries of reproducible TADs compared to those within TADs and genomewide intervals of the same size for GM12878 at 5 kb resolution.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Total number of TADs identified across six replicates for each chromosome. (B) Total number of TADs identified across 23 chromosomes for each replicate.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Percentages of TADs that have CTCF peaks at boundaries. (B) Percentages of TADs that have both CTCF peaks and convergent CTCF motifs at the boundaries. (C) Percentages of four types of CTCF motifs orientations at TAD boundaries. Convergent motif pairs are those with a forward strand motif upstream of TAD boundaries and a reverse strand motif downstream of TAD boundaries. Tandem Right, similarly, represents forward-forward CTCF motif pairs. Tandem Left refers to reverse-reverse motif pairs. Divergent is reverse-forward motif pairs (D) Some TAD boundaries are adjusted under Uni&Multi-setting. Box plots depict the percentage of adjusted TADs that have convergent CTCF motifs at the boundaries. (E). False discovery rate of TADs detected under the two settings. TADs that are not reproducible and lack CTCF convergent motifs at the TAD boundaries are considered as false positives.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Gene tracks, 24mer mappability tracks as well as CTCF peaks are displayed above the contact matrices. (A) Example at chr6:5,350,000–33,850,000. Even in the lack of obviously low mappable contact gaps, multi-reads can enhance the existing interaction signal and reveal detectable TAD structures supported by CTCF peaks. (B) Example on chr9:15,150,000–43,650,000. TAD structure, supported by CTCF peaks at the TAD boundaries, becomes detectable as multi-reads fill in the gap in the contact matrix. Red squares at the left bottom of the matrices indicate the color scale.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (A) An example from chr1:66,800,000–95,300,000. (B) An example from chr5:0–28,500,000. Red squares at the left bottom of the matrices indicate the color scale.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** (A) An example from chr12:0–25,000,000. (B) An example from chr13:42,800,000–71,300,000. Red squares at the left bottom of the matrices indicate the color scale.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp6-v2.jpg)

**Figure 5—figure supplement 6.:** TADs that are split by white gaps are no longer detected once multi-reads are incorporated, indicating that they are highly likely false positives under the Uni-setting. (A) Example on chr2:105,600,000–134,100,000. (B) Example on chr3:60,000,000–88,500,000. Red squares at the left bottom of the matrices indicate the color scale.

![Figure 5—figure supplement 7.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp7-v2.jpg)

**Figure 5—figure supplement 7.:** TADs that are split by white gaps are no longer detected once multi-reads are incorporated, indicating that they are highly likely false positives under the Uni-setting. (A) Example on chr4:0–28,500,000. (B) Example on chr16:0–28,500,000. Red squares at the left bottom of the matrices indicate the color scale.

![Figure 5—figure supplement 8.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp8-v2.jpg)

**Figure 5—figure supplement 8.:** TADs that are split by white gaps are no longer detected once multi-reads are incorporated, indicating that they are highly likely false positives under the Uni-setting. (A) Example on chr21:14,350,000–42,850,000. (B) Example on chrX:60,800,000–117,800,000. Red squares at the left bottom of the matrices indicate the color scale.

![Figure 5—figure supplement 9.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp9-v2.jpg)

**Figure 5—figure supplement 9.:** TADs that are not reproducible are labeled as false positives without considering the CTCF peaks at the TAD boundaries.

![Figure 5—figure supplement 10.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp10-v2.jpg)

![Figure 5—figure supplement 11.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig5-figsupp11-v2.jpg)

**Figure 5—figure supplement 11.:** Such enrichment is compared to those within TADs and genomewide intervals of the same size.

Next, we assessed the abundance of different classes of repetitive elements, from the RepeatMasker (Open R, 2015) and UCSC genome browser (Tyner et al., 2017) hg19 assembly, at the reproducible TAD boundaries. Specifically, we considered segmental duplications (DUP), short interspersed nuclear elements (SINE), long interspersed nuclear elements (LINE), long terminal repeat elements (LTR), DNA transposon (DNA) and satellites (SATE). We utilized ± bin on either side of the edge coordinate of a given domain as its TAD boundary. At a lower resolution, that is 40 kb for IMR90, each boundary is 120 kb region and the percentages of TAD boundaries with each type of repetitive element illustrate negligible differences between the Uni-setting and Uni&Multi-setting (Figure 5—figure supplement 10A). Similarly, due to the large sizes of the TAD boundaries, a majority of TAD boundaries harbor SINE, LINE, LTR, and DNA transposon elements. However, higher resolution analysis of the GM12878 dataset at 5 kb reveals SINE elements as the leading category of elements that co-localizes with more than 99% of TAD boundaries followed by LINEs (Figure 5—figure supplement 10B). This is consistent with the fact that SINE and LINE elements are relatively short and cover a larger portion of the human genome compared to other subfamilies (15% for SINE and 21% for LINE; Treangen and Salzberg, 2012). We further quantified the enrichment of repetitive elements at TAD boundaries by comparing their average abundance with those within TADs and the genomic intervals of the same size across the whole genome as the baseline. Figure 5D and Figure 5—figure supplement 11 show that SINE elements, satellites, and segmental duplications are markedly enriched at the TAD boundaries compared to the whole genome and within TADs. More interestingly, at higher resolution, that is 5 kb for GM12878, the SINE category both have the highest average enrichment and is enhanced by mHi-C (Figure 5D). In summary, under Uni&Multi-setting, the detected TAD boundaries tend to harbor more SINE elements supporting prior work that human genome folding is markedly associated with the SINE family (Cournac et al., 2016).

### Large-scale evaluation of mHi-C with computational trimming experiments and simulations establishes its accuracy

Before further investigating the accuracy of mHi-C rescued multi-reads with computational experiments, we considered heuristic strategies for rescuing multi-reads at different stages of the Hi-C analysis pipeline as alternatives to mHi-C (Figure 6A; see Materials and methods for detailed descriptions of the model-free approaches and related analysis). Specifically, AlignerSelect and DistanceSelect rescue multi-reads by simply choosing one of the alignments of a multi-read pair by default aligner strategy and based on distance, respectively. In addition to these, we designed a direct alternative to mHi-C, named SimpleSelect, as a model-free approach that imposes genomic distance priority in contrast to leveraging of the local interaction signals of the bins by mHi-C (e.g., local contact counts due to other read pairs in candidate bin pairs).

![Figure 6.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-v2.jpg)

**Figure 6.:** (A) Intuitive heuristic strategies (AlignerSelect, DistanceSelect, SimpleSelect) for model-free assignment of multi-reads at various stages the of Hi-C analysis pipeline. (B) Accuracy of mHi-C in allocating trimmed multi-reads with respect to trimmed read length, compared with model-free approaches as well as random selection as a baseline. (C) Allocation accuracy with respect to mappability for 75 bp reads. Red solid line depicts the overall accuracy trend. ‘Not assigned’ category refers to multi-reads with a maximum posterior probability of assignment $\leq$ 0.5. (D) mHi-C accuracy among different repetitive element classes.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Numbers of uni-reads and multi-reads across trimmed read lengths compared to the sequencing depth of uni-reads of full read length A549 dataset (replicate 2), not including uni-reads rescued from chimeric reads. (B) Percentage of multi-reads over uni-reads in the full-length A549 datasets (four replicates, excluding uni-reads from chimeric reads) and the trimmed datasets. Multi-to-uni percentages of the read sets in the trimmed datasets cover the range of the percentages observed in the study datasets. (C) Numbers of multi-reads from different trimming lengths compared to sequencing depths of the full read length A549 datasets. For the trimming setting (ii) described in Materials and methods, multi-reads (green bars) added to the uni-read datasets (blue bars) constitute a smaller percentage of the sequencing depth while enabling analysis at the higher resolution of 10 kb.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** mHi-C > 0.5 refers to the fact that only the allocations with posterior probability of assignment greater than 0.5 are evaluated.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-figsupp3-v2.jpg)

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** (A) Allocation accuracy of mHi-C at 40 kb and 10 kb resolutions. (B) Allocation accuracy for simulated reads of different lengths among regions of varying mappability.

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-figsupp5-v2.jpg)

![Figure 6—figure supplement 6.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-figsupp6-v2.jpg)

**Figure 6—figure supplement 6.:** (A) mHi-C accuracy among different types of repetitive element classes with respect to trimmed read length. (B) Allocation accuracy across different classes of repetitive elements at 10 kb and 40 kb resolutions using uni-reads of replicate 1, 3, and 4 combined with multi-reads of replicate 2 (trimming setting (ii)).

![Figure 6—figure supplement 7.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig6-figsupp7-v2.jpg)

**Figure 6—figure supplement 7.:** (A) Comparison of genomic distance distributions of significant interactions between SimpleSelect and mHi-C for IMR90 rep5 (FDR $<$ 0.001). (B) Comparison of significant interactions among the three life stages of P. falciparum. Y-axis in each panel, namely rings, trophozoites, and schizonts, depicts the percentage of contacts that are significant only in the panel condition compared to the other two conditions. Under varying FDR thresholds, mHi-C and Uni-setting tend to have similar percentages of differential interactions among ring - trophozoites - schizonts plasmodium life stages. In contrast, SimpleSelect tends to underestimate differential interactions due to over-emphasizing contact distance prior.

To evaluate the accuracy of mHi-C in a setting with ground truth, we carried out trimming experiments with the A549 151 bp read length dataset and Hi-C data simulations where we compared mHi-C to both a random allocation strategy as the baseline and the additional heuristic approaches we developed (Figure 6A). Specifically, we trimmed the set of 151 bp uni-reads from A549 into read lengths of 36 bp, 50 bp, 75 bp, 100 bp, and 125 bp. As a result, a subset of uni-reads at the full read length of 151 bp with known alignment positions were reduced into multi-reads, generating gold-standard multi-read sets with known true origins. The resulting numbers of valid uni- and multi-reads are summarized in Figure 6—figure supplement 1A in comparison with the numbers of valid uni-reads in the original A549 datasets. The corresponding multi-to-uni ratios of these settings vary with the lengths of the trimmed reads, and their range covers the typical multi-to-uni ratios observed in the full read length datasets (Figure 6—figure supplement 1B).

We first investigated the multi-read allocation accuracy with respect to trimmed read length, sequencing depth, and mappability at resolution 40 kb. Figure 6B exhibits superior performance of mHi-C over both the model-free methods and the random baseline in correctly allocating multi-reads of different lengths to their true origins across intra- and inter-chromosomal contacts. As expected and illustrated by Figure 6B, the accuracy of multi-read assignment has an increasing trend with the read length. Specifically, it ranges between 70% and 90% for mHi-C and 20% and 35% for the random allocation strategy for the shortest and longest trimmed read lengths of 36 bp and 125 bp, respectively. When the allocated multi-reads are stratified as a function of the mappability, reads with the lowest mappability (<0.1) have accuracy levels of less than 32% to 70% across the trimmed read lengths (Figure 6C for 75 bp, Figure 6—figure supplement 2 for the other trimming lengths). Notably, the accuracy quickly reaches 74% to 87% for reads with mappability of at least 0.5 (Figure 6C, Figure 6—figure supplement 2).

Next, we assessed the allocation accuracy among different classes of repetitive elements (Figure 6D). Allocations involving segmental duplication regions exhibit a systematically lower performance compared to other repeat classes and the overall average across the whole genome for all five trimming settings. Notably, even for these segmental duplication regions, the accuracy of mHi-C is markedly higher than both the model-free approaches and the random selection baseline displayed in Figure 6B. To finalize the accuracy investigation, we further varied the trimming setting by mixing uni-reads and multi-reads from different replicates (see setting (ii) of trimming strategies in Materials and methods) and considering resolutions of 10 kb and 40 kb in addition to an empirical Hi-C simulation. Figure 6—figure supplements 3–6 provide accuracy results closely following the results presented in this section from these additional settings and further validate significantly better performance of mHi-C compared to the random allocation and other heuristic approaches across different trimmed read lengths.

After establishing accuracy, we evaluated the impact of mHi-C rescued multi-reads of the trimmed datasets on the recovery of the (original) full read length contact matrices, topological domain structures, and significant interactions. To assess the recovery of the original contact matrix, we compared both the trimmed Uni- and Uni&Multi-settings with the gold standard Uni-setting at the full read length utilizing HiCRep (Yang et al., 2017). Figure 7A and Figure 7—figure supplement 1 illustrate that mHi-C achieves significant improvement in the reproducibility across all chromosomes under all trimming settings compared to the Uni-setting. While the pattern of reproducibility with different read lengths in Figure 7A is consistent with the expectation that the longer trimmed reads should yield contact matrices that are more similar to the full read length one, the improvement in reproducibility due to mHi-C is markedly larger compared to the gains from longer read sequences making multi-read rescue essential. For example, the reproducibility for Uni&Multi-setting at 50 bp is 8.84% to 27.33% higher than that of Uni-setting at 125 bp. We further evaluated reproducibility under each trimming setting across replicates and benchmarked the results against the reproducibility of the Uni-setting with the original read length of 151 bp. Figure 7—figure supplements 2 and 3 confirm the gain in reproducibility across replicates due to Uni&Multi-setting for all the trimming lengths. As expected, the reproducibility across replicates based on the uni-reads of the original read length is higher than the levels achievable by the Uni&Multi-Setting at trimmed read lengths. This comparison further supports that mHi-C assigns multi-reads in a biologically meaningful manner as was evidenced earlier by the increased reproducibility among replicates of the same condition (Figure 2B and Figure 2—figure supplements 9 and 10) but not across replicates of the different conditions (Figure 2—figure supplement 12). It also rules out the possibility of inflation of the reproducibility metric by consistent but biologically irrelevant assignment of multi-reads to certain loci. TAD identification with these trimmed sets highlights the sensitivity of TAD boundary detection to the sequencing depth. Figure 7B and Figure 7—figure supplements 4–7 display examples where the trimmed Uni&Multi-setting achieved better recovery of TAD structure of the full-length dataset compared to trimmed Uni-setting. Overall, this performance is attributable to the accuracy of mHi-C assignments and the resulting increase in sequencing depth of the trimmed uni-read dataset. Finally, we compared the significant interactions detected by the trimmed Uni- and Uni&Multi-settings and observed that mHi-C rescued multi-reads in trimmed datasets enable detection of a larger number of interactions across a range of FDR thresholds (Figure 7—figure supplement 8). Most notably, an evaluation of detection power for the top 10K significant interactions of the full-length dataset demonstrates that, while the Uni-setting can only recover 50% of these at the trimmed read length of 36 bp, Uni&Multi-setting recovers 70% (Figure 7C and Figure 7—figure supplement 9). We note that these power values are slightly underestimated because the full-length uni-read dataset also included chimeric reads that were rescued as uni-reads. In contrast, trimmed reads in the trimming experiments were generated from uni-reads without rescuing chimeric reads (see Materials and methods; Figure 7—figure supplement 10). Despite this, the 26.19% increase in sequencing depth due to multi-reads at the trimmed read length of 36 bp (Figure 6—figure supplement 1B) translated into a significantly better recovery of the significant interactions. Further assessment by ROC and PR analysis (Figure 7D, E and Figure 7—figure supplement 11) of the set of significant contacts identified by both settings illustrates that Uni&Multi-setting exhibits these advantages without inflating the false discoveries. As reads get longer towards the full length, the ROC and PR curves converge under the two settings (Figure 7—figure supplement 11).

![Figure 7.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-v2.jpg)

**Figure 7.:** (A) mHi-C rescued multi-reads of the trimmed dataset along with trimmed uni-reads lead to contact matrices that are significantly more similar to original contact matrices compared to only using trimmed uni-reads. (B) TAD detection on chromosome six with the original longer uni-reads contact matrix with black TAD boundaries, trimmed uni-reads (36 bp) contact matrix with green TAD boundaries, and trimmed uni- and multi-reads (36 bp) contact matrix with blue TAD boundaries. (C) The power of recovering top 10,000 significant interactions of full read length dataset using trimmed reads under FDR10%. (D, E) Receiver Operating Characteristic (ROC) and Precision-Recall (PR) curves for trimmed Uni- and Uni&Multi-setting. The ground truth for these curves is based on the significant interactions identified by the full read length dataset at FDR of 10%. The dashed line is y = x.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp1-v2.jpg)

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp2-v2.jpg)

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp3-v2.jpg)

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp4-v2.jpg)

![Figure 7—figure supplement 5.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp5-v2.jpg)

![Figure 7—figure supplement 6.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp6-v2.jpg)

![Figure 7—figure supplement 7.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp7-v2.jpg)

![Figure 7—figure supplement 8.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp8-v2.jpg)

![Figure 7—figure supplement 9.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp9-v2.jpg)

![Figure 7—figure supplement 10.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp10-v2.jpg)

**Figure 7—figure supplement 10.:** Downstream analysis of trimming experiments beyond evaluating the accuracy of multi-read assignments utilized Uni-reads of rep2 displayed here for deriving gold standard interaction sets.

![Figure 7—figure supplement 11.](https://cdn.elifesciences.org/articles/38070/elife-38070-fig7-figsupp11-v2.jpg)

**Figure 7—figure supplement 11.:** In the ROC curves, the false positive rates are displayed up until 10% as the values of both the x- and y-axis rates shoot up to one after this value. Ground truth for these curves is based on the significant interactions identified by the full read length dataset at FDR of 10%.

## Discussion

Hi-C data are powerful for identifying long-range interacting loci, chromatin loops, topologically associating domains (TADs), and A/B compartments (Lieberman-Aiden et al., 2009; Yu and Ren, 2017). Multi-mapping reads, however, are absent from the typical Hi-C analysis pipelines, resulting in under-representation and under-study of three-dimensional genome organization involving repetitive regions. Consequently, downstream analysis of Hi-C data relies on the incomplete Hi-C contact matrices which have frequent and, sometimes, severe interaction gaps spanning across the whole matrix. While centromeric regions contribute to such gaps, our results indicate that lack of multi-reads in the analysis is a significant contributor. Our Hi-C multi-read mapping strategy, mHi-C, probabilistically allocates high-quality multi-reads to their most likely positions (Figure 1E) and successfully fills in the missing chunks of contact matrices (Figure 2A and Figure 2—figure supplements 1–4). As a result, incorporating multi-reads yields remarkable increase in sequencing depth which is translated into significant and consistent gains in reproducibility of the raw contact counts (Figure 2B) and detected interactions (Figure 2C). Analysis with mHi-C rescued reads identifies novel significant interactions (Figure 3), promoter-enhancer interactions (Figure 4), and refines domain structures (Figure 5). Our computational experiments with trimmed and simulated Hi-C reads validate mHi-C and elucidate the significant impact of multi-reads in all facets of the Hi-C data analysis. We demonstrate that even for the shortest read length of 36 bp, mHi-C accuracy exceeds 74% (85% for longer trimmed reads) for regions with underlying mappability of at least 0.5 (Figure 6C and Figure 6—figure supplement 2). mHiC significantly outperforms a baseline random allocation strategy as well as several other model-free and intuitive multi-read allocation strategies while achieving its worst allocation accuracy of 63% for reads originating from segmental duplications (Figure 6B and D). Trimming experiments further demonstrated the utility of multi-reads for contact matrix, TAD, and significant interaction recovery (Figure 7).

The default setting of mHi-C is intentionally conservative. In this default setting, mHi-C rescues high-quality multi-reads that can be allocated to a candidate alignment position with a high probability of at least 0.5. mHi-C allows relaxation of this strict filtering where instead of keeping reads with allocation probability greater than 0.5, these posterior allocation probabilities can be utilized as fractional contacts. We chose not to pursue this approach in this work as the current downstream analysis pipelines do not accommodate such fractional contacts. Currently, mHi-C model does not take into account potential copy number variations and genome arrangements across the genome. While mHi-C model can be extended to take into account estimated copy number and arrangement maps of the underlying sample genomes as we have done for other multi-read problems (Zhang and Keleş, 2014), our computational experiments with cancerous human alveolar epithelial cells A549 does not reveal any notable deterioration in mHi-C accuracy for these cells with copy number alternations.

## Materials and methods

### mHi-C workflow

We developed a complete pipeline customized for incorporating high-quality multi-mapping reads into the Hi-C data analysis workflow. The overall pipeline, illustrated in Figure 1—figure supplements 1 and 2, incorporates the essential steps of the Hi-C analysis pipelines. In what follows, we outline the major steps of the analysis to explicitly track multi-reads and describe how mHi-C utilizes them.

#### Read end alignment: uni- and multi-reads and chimeric reads

The first step in the mHi-C pipeline is the alignment of each read end separately to the reference genome. The default aligner in the mHi-C software is BWA (Li and Durbin, 2010); however mHi-C can work with any aligner that outputs multi-reads. The default alignment parameters are (i) edit distance maximum of 2 including mismatches and gap extension; and (ii) a maximum number of gap open of 1. mHi-C sets the maximum number of alternative hits saved in the XA tag to be 99 to keep track of multi-reads. If the number of alternative alignments exceeds the threshold of 99 in the default setting, these alignments are not recorded in XA tag. We regarded these alignments as low-quality multi-mapping reads compared to those multi-mapping reads that have a relatively smaller number of alternative alignments. In summary, low-quality multi-mapping reads are discarded together with unmapped reads, only leaving uniquely mapping reads and high-quality multi-mapping reads for downstream analysis. mHi-C pipeline further restricts the maximum number of mismatches (maximum to be 2 compared to three in BWA default setting) to ensure that the alignment quality of multi-reads is comparable to that of standard Hi-C pipeline.

Chimeric reads, that span ligation junction of the Hi-C fragments (Figure 1—figure supplement 1) are also a key component of Hi-C analysis pipelines. The ligation junction sequence can be derived from the restriction enzyme recognition sites and used to rescue chimeric reads. mHi-C adapts the pre-splitting strategy of diffHiC (Lun and Smyth, 2015), which is modified from the existing Cutadapt (Martin, 2011) software. Specifically, the read ends are trimmed to the center of the junction sequence. If the trimmed left 5' ends are not too short, for example ≥ 25 bps, these chimeric reads are remapped to the reference genome. As the lengths of the chimeric reads become shorter, these reads tend to become multi-reads.

#### Valid fragment filtering

While each individual read end is aligned to reference genome separately, inferring interacting loci relies on alignment information of paired-ends. Therefore, read ends are paired after unmapped and singleton read pairs as well as low-quality multi-mapping ends (Figure 1—figure supplement 1 and Supplementary file 1) are discarded. After pairing, read end alignments are further evaluated for their representation of valid ligation fragments that originate from biologically meaningful long-range interactions (Figure 1—figure supplement 1). First, reads that do not originate from around restriction enzyme digestion sites are eliminated since they primarily arise due to random breakage by sonication (Belaghzal et al., 2017). This is typically achieved by filtering the reads based on the total distance of two read end alignments to the restriction site. We required the total distance to be within 50–800 bps for the mammalian datasets and 50–500 bps for P. falciparum. The lower bound of 50 for this parameter is motivated by the chimeric reads with as short as 25 bps on both ends. Second, a single Hi-C interaction ought to involve two restriction fragments. Therefore, read ends falling within the same fragment, either due to dangling end or self-circle ligation, are filtered. Third, because the nature of chromatin folding leads to the abundance of random short-range interactions, interactions between two regions that are too close in the genomic distance are highly likely to be random interaction without regulatory implications. As a result, reads with ends aligning too close to each other are also filtered according to the twice the resolution rule. Notably, as a result of this valid fragment filtering, some multi-mapping reads can be counted as uniquely mapping reads (Supplementary file 1 - 2b). This is because, although a read pair has multiple potential genomic origins dictated by its multiple alignments, only one of them ends up passing the validation screening. Once the multi-mapping uncertainty is eliminated, such read pairs are passed to the downstream analysis as uni-reads. We remark here that standard Hi-C analysis pipelines do not rescue these multi-reads.

#### Duplicate removal

To remove PCR duplicates, mHi-C considers the following two issues. First, due to allowing a maximum number of 2 mismatches in alignment, some multi-reads may have the exact same alignment position and strand direction with uni-reads. If such duplicates arise, uni-reads are granted higher priority and the overlapping multi-reads together with all their potential alignment positions are discarded completely. This ensures that the uni-reads that arise in standard Hi-C analysis pipelines will not be discarded as PCR duplicates in the mHi-C pipeline. Second, if a multi-mapping read alignment is duplicated with another multi-read, the read with smaller alphabetical read query name will be preserved. More often than not, if multi-read A overlaps multi-read B at a position, then it is highly likely that they will overlap at other positions as well. This convention ensures that it is always the read pair A alignments that are being retained (Figure 1—figure supplement 2).

#### Genome binning

Due to the typically limited sequencing depths of Hi-C experiments, the reference genome is divided into small non-overlapping intervals, that is bins, to secure enough number of contact counts across units. The unit can be fix-sized genomic intervals or a fixed number of consecutive restriction fragments. mHi-C can switch between the two unit options with ease. After binning, the interaction unit reduces from alignment position pairs to bin pairs. Remarkably, multi-mapping reads, ends of which are located within the same bin pair, reduce to uni-reads as their potential multi-mapping alignment position pairs support the same bin pair contact. Therefore, there is no need to distinguish the candidate alignments within the same bin (Figure 1—figure supplement 2 and Supplementary file 1 - 3b).

#### mHi-C generative model and parameter estimation

mHi-C infers genomic origins of multi-reads at the bin pair level (Supplementary file 1). We denoted the whole alignment vector for a given paired-end read $i$ by vector $𝐘_{i}$. If the two read ends of read $i$ align to only bin $j$ and bin $k$, respectively, we set the respective components of the alignment vector as: $Y_{i,(j,k)}$ = 1 and $Y_{i,(j^{^{′}},k^{^{′}})}=0$, $∀ j^{^{′}}\neqj$, $k^{^{′}}\neqk$. Index of read, $i$, ranges from 1 to $N$, where $N$ is total number of valid Hi-C reads, including both uni-reads and multi-reads that pass the essential processing in Figure 1—figure supplements 1 and 2. Overall, the reference genome is divided into $M$ bins and $j$ represents the bin index of the end, alignment position of which is upstream compared to the other read end position indicated by $k$. Namely, $j$ takes on a value from 1 to $M−1$ and $k$ runs from $j+1$ to the maximum value $M$. For uniquely mapping reads, only one alignment is observed, that is $\sum_{(j,k)}^{(M-1,M)}Y_{i,(j,k)}=1$. However, for multi-mapping reads, we have $\sum_{(j,k)}^{(M-1,M)}Y_{i,(j,k)}>1$.

We next defined a hidden variable $Z_{i,(j,k)}$ to denote the true genomic origin of read $i$. If read $i$ originates from position bin pairs $j$ and $k$, we have $Z_{i,(j,k)}=1$. In addition, a read can only originate from one alignment position pair on the genome; thus, $\sum_{(j,k)}^{(M-1,M)}Z_{i,(j,k)}=1$ for both uni- and multi-reads. We define $O_{i}$ = ${$($j$, $k$): $Z_{i,(j,k)}$ = 1$}$ to represent true genomic origin of read $i$ and $S_{O_{i}}$ as the set of location pairs that read pair $i$ can align to. Hence, $Y_{i,(j,k)}$ = 1, if ($j$, $k$) $\inS_{O_{i}}$. Under the assumption that the true alignment can only originate from those observed alignable positions, $O_{i}$ must be one of the location pairs in $S_{O_{i}}$. We further assume that the indicators of true origin for read $i$, $𝒁_{𝒊}$ = $(Z_{i,(1,2)},Z_{i,(1,3)},…,Z_{i,(M-1,M)})$ are random draws from a Dirichlet - Multinomial distribution. Specifically,

$$
Z_{i}∼i.i.d.Multinomial(\pi_{(1,2)},\pi_{(1,3)},⋯,\pi_{(j,k)},⋯,\pi_{(M−1,M)}),i=1,⋯,N,
$$

where $\pi_{(j,k)}$ can be interpreted as contact probability between bin $j$ and $k$ ($j<k$). We further assume that

$$
\pi∼Dirichlet(\gamma_{(1,2)},\gamma_{(1,3)},⋯,\gamma_{(j,k)},⋯,\gamma_{(M−1,M)}),
$$

where $\pi=(\pi_{(1,2)},\pi_{(1,3)},⋯,\pi_{(M−1,M)})$ and $\gamma_{(j,k)}$ is a function of genomic distance and quantifies random contact probability. Specifically, we adapt the univariate spline fitting approach from Fit-Hi-C (Ay et al., 2014a) for estimating random contact probabilities with respect to genomic distance and set $\gamma_{(j,k)}=Spline⁢(j,k)\timesN+1$. Here, $N$ is the total number of valid reads as defined above and $Spline⁢(j,k)$ denotes the spline estimate of the random contact probability between bins $j$ and $k$. Therefore, $Spline⁢(j,k)\timesN$ is the average random contact counts (i.e., pseudo-counts) between bin $j$ and $k$. As a result, the probability density function of $\pi$ can be written as:

$$
P(\pi|\gamma)=\frac{Γ(\sumj=1M−1\sumk=j+1M\gamma_{(j,k)})}{\prodj=1M−1\prodk=j+1MΓ(\gamma_{(j,k)})}\prodj=1M−1\prodk=j+1M\pi_{(j,k)}^{(\gamma_{(j,k)}−1)}=\frac{Γ(\sumj=1M−1\sumk=j+1M(Spline(j,k)\timesN+1))}{\prodj=1M−1\prodk=j+1MΓ(Spline(j,k)\timesN+1)}\prodj=1M−1\prodk=j+1M\pi_{(j,k)}^{Spline(j,k)\timesN}.
$$

We next derive the full data joint distribution function.

Lemma 1. Given the true genomic origin under the mHi-C setting, the set of location pairs that a read pair can align to will have observed alignments with probability $1$.

Proof.

$$
P(Y_{i}|Z_{i,(j,k)}=1)=(Y_{i}|O_{i})=\prodj=1M−1\prodk=j+1MP(Y_{i,(j,k)}|O_{i})=\prodj=1M−1\prodk=j+1M[1(Y_{i,(j,k)}=1,(j,k)\inS_{O_{i}})+1(Y_{i,(j,k)}\neq1,(j,k)∉S_{O_{i}})]=1.◻
$$

Based on Lemma 1, we can get the joint distribution $P⁢(𝐘,𝐙|\pi)$ as

$$
P(Y,Z|\pi)=\prodiNP_{\pi}(Y_{i},Z_{i})=\prodiN\prodj=1M−1\prodk=j+1MP_{\pi}(Y_{i},Z_{i,(j,k)}=1)^{Z_{i,(j,k)}}=\prodiN\prodj=1M−1\prodk=j+1M[P_{\pi}(Y_{i}|Z_{i,(j,k)}=1)\pi_{(j,k)}]^{Z_{i,(j,k)}}=\prodiN\prodj=1M−1\prodk=j+1M\pi_{(j,k)}^{Z_{i,(j,k)}}.
$$

Using the Dirichlet-Multinomial conjugacy, we derive the posterior distribution of $\pi$ as

$$
P(\pi|Z)∝P(\pi,Z)=\prodi=1NP(Z_{i}|\pi)P(\pi)∝\prodj=1M−1\prodk=j+1M\pi_{(j,k)}^{(\sumi=1NZ_{i,(j,k)}+\gamma_{(j,k)}−1)}=\prodj=1M−1\prodk=j+1M\pi_{(j,k)}^{(\sumi=1NZ_{i,(j,k)}+Spline(j,k)\timesN)}.
$$

We next derive an Expectation-Maximization algorithm for fitting this model.

E-step.

$$
Z_{i,(j,k)}^{(t)}=E(Z_{i,(j,k)}|𝒀_{𝒊},𝝅)=\frac{\pi_{(j,k)}^{(t)}}{\sum_{(j^{^{′}},k^{^{′}})\inS_{O_{i}}}\pi_{(j^{^{′}},k^{^{′}})}^{(t)}}1[(j,k)\inS_{O_{i}}].
$$

M-step.

$$
\pi_{(j,k)}^{(t+1)}=\frac{\sum_{i=1}^{N}Z_{i,(j,k)}^{(t)}+S⁢p⁢l⁢i⁢n⁢e⁢(j,k)\timesN}{N+\sum_{j^{^{′}}=1}^{M-1}\sum_{k^{^{′}}=j+1}^{M}S⁢p⁢l⁢i⁢n⁢e⁢(j^{^{′}},k^{^{′}})\timesN}.
$$

Estimate of the contact probability $\pi_{(j,k)}$ in the M-step can be viewed as an integration of local interaction signal, encoded in $\sum_{i=1}^{N}Z_{i,(j,k)}^{(t)}$, and random contact signal due to prior, that is, $Spline⁢(j,k)\timesN$.

The by-products of the EM algorithm are posterior probabilities, P($Z_{i,(j,k)}$=1 $|𝒀_{𝒊}$$Y_{i},\pi$), which are utilized for assigning each multi-read to the most likely genomic origin. To keep mHi-C output compatible with the input required for the widely used significant interaction detection methods, we filtered multi-reads with maximum allocation posterior probability less than or equal to 0.5 and assigned the remaining multi-reads to their most likely bin pairs. This ensured the use of at most one bin pair for each multi-read pair. We repeated our computational evaluations by varying this threshold on the posterior probabilities to ensure robustness of the overall conclusions to this threshold.

### Assessing false positive rates for significant interactions and TADs identification under the Uni- and Uni&Multi-settings

To quantify false positive rates of the Uni- and Uni&Multi-settings at the significant interaction level, we defined true positives and true negatives by leveraging deeply sequenced replicates of the IMR90 dataset (replicates 1–4). Significant interactions reproducibly identified across all four replicates at 0.1% FDR by both the Uni- and Uni&Multi-settings were labeled as true positives (i.e., true interactions). True negatives were defined as all the interactions that were not deemed significant at 25% FDR in any of the four replicates. We then evaluated significant interactions identified by smaller depth replicates 5 and 6 with ROC and PR curves (Figure 3—figure supplement 13) by using these sets of true positives and negatives as the gold standard. To quantify false positive rates at the topologically associating domains (TADs) level (Figure 5C, Figure 5—figure supplement 2E), we utilized TADs that are reproducible in more than three replicates of the IMR90 dataset and/or harbor CTCF peaks at the boundaries as true positives. The rest of the TADs are supported neither by multiple replicates nor by CTCF, hence are regarded as false positives.

### Evaluating reproducibility

Reproducibility in contact matrices was evaluated using HiCRep in the default settings. We further assessed the reproducibility in terms of identified interactions by grouping them into three categories: those only detected under Uni-setting, those unique to Uni&Multi-setting, and those that are detected under both settings. The reproducibility is calculated by overlapping significant interactions between every two replicates and recording the percentage of interactions that are also deemed significant in another replicate (Figure 2—figure supplement 13).

### Chromatin states of novel significant interactions

We annotated the novel significant interactions with the 15 states ChromHMM segmentations for IMR90 epigenome (ID E017) from the Roadmap Epigenomics project (Kundaje et al., 2015). All six replicates of IMR90 are merged together in calculating the average enrichment of significant interactions among the 15 states (Figure 3D and Figure 3—figure supplement 14A).

### ChIP-seq analysis

ChIP-seq peak sets for IMR90 cells were obtained from ENCODE portal (https://www.encodeproject.org/) and GEO (Barrett et al., 2013). Specifically, we utilized H3K4me1 (ENCSR831JSP), H3K4me3 (ENCSR087PFU), H3K36me3 (ENCSR437ORF), H3K27ac (ENCSR002YRE), H3K27me3 (ENCSR431UUY) and CTCF (ENCSR000EFI) from the ENCODE project and p65 (GSM1055810), p300 (GSM1055812) and PolII (GSM1055822) from GEO (Barrett et al., 2013). In addition, raw data files in fastq format were processed by Permseq (Zeng et al., 2015) utilizing DNase-seq of IMR90 (ENCODE accession ENCSR477RTP) to incorporate multi-reads and, subsequently, peaks were identified using ENCODE uniform ChIP-seq data processing pipeline (https://www.encodeproject.org/pages/pipelines/#DNA-binding). CTCF motif quantification for topologically associating domains was carried out with FIMO (Grant et al., 2011) under the default settings using CTCF motif frequency matrix from JASPAR (Khan et al., 2017).

### Promoters with significant interactions

Significant interactions across six replicates of the IMR90 study were annotated with GENCODE V19 (Harrow et al., 2012) gene annotations and enhancer regions from ChromHMM. Gene expression calculations utilized RNA-seq quantification results from the ENCODE project with accession number ENCSR424FAZ.

### Marginal Hi-C tracks in Figure 3—figure supplement 15–17

Uni-setting and Uni&Multi-setting Hi-C tracks displayed on the UCSC genome browser figures (Figure 3—figure supplement 15–17) are obtained by aggregating contact counts of six replicates of IMR90 for each genomic coordinate along the genome.

### Visualization of contact matrices and interactions

We utilized Juicebox (Durand et al., 2016), HiGlass (Kerpedjiev et al., 2017), and WashU epigenome browser (Zhou et al., 2011) for depicting contact matrices and interactions, respectively, throughout the paper. Normalization of the contact matrices for visualization was carried out by the Knight-Ruiz Matrix Balancing Normalization (Knight and Ruiz, 2013) provided by Juicebox (Durand et al., 2016).

### Model-free multi-reads allocation strategies

The simplified and intuitive strategies depicted in Figure 6A correspond to rescuing multi-reads at different essential stages of the Hi-C analysis pipeline. AlignerSelect relies on the base aligner, for example BWA, to determine the primary alignment of each individual end of a multi-read pair. DistanceSelect enables the distance prior to dominate. It selects the read end alignments closest in the genomic distance as the origins of the multi-read pair and defaults to the primary alignment selected by base aligner for inter-chromosomal multi-reads. Finally, SimpleSelect follows the overall mHi-C pipeline closely by making use of the standard Hi-C validation checking and binning procedures. For the reads that align to multiple bins, it selects the bin pair closest in the genomic distance as the allocation of the multi-read pair. Bin-pair allocations for inter-chromosomal multi-reads are set randomly in this strategy.

### Comparison of mHi-C with model-free multi-reads allocation for their impact on identifying differential interactions

We evaluated the direct biological consequence of heavily biasing read assignment by genomic distance, as employed by SimpleSelect, by comparing the significant interactions among three life stages of P. falciparum. We reasoned that the better multi-reads allocation strategy would reveal a differential analysis pattern more consistent with the Uni-setting, whereas a genomic distance biased strategy - SimpleSelect - will underestimate differences since multi-reads will be more likely to be allocated to candidate bin pairs with shortest genomic distance regardless of other local contact signals (Figure 6—figure supplement 7A). Figure 6—figure supplement 7B corroborates this drawback of SimpleSelect and demonstrates that mHi-C differential patterns agree better with that of the Uni-setting. Moreover, Figure 6—figure supplement 7B suggests that rings stage is more similar to schizonts, an observation consistent with existing findings on P. falciparum life stages (Ay et al., 2014b; Bunnik et al., 2018).

### Trimming procedures

We considered two approaches for generating evaluation datasets where we combined the trimmed multi-reads from replicate two, which has the median sequencing depth among all replicates of the A549 study set, with (i) trimmed reads of replicate two that remain uniquely aligned to the reference genome at the same trimmed read length (Figures 6 and 7), and (ii) uni-reads from other replicates, that is, replicates one, three, and four in the A549 dataset individually (Figure 6—figure supplements 3, 5 and 6). The first setting enables a direct comparison of the set of uni- and multi-reads at trimmed read length compared to uni-reads at the full read length to evaluate accuracy. The numbers of reads are summarized in Figure 6—figure supplement 1A along with multi-to-uni ratios in Figure 6—figure supplement 1B. In the second trimming setting (ii), the uni-read sets are of the original sequencing depth and the added multi-reads constitute a smaller proportion compared to observed levels in the data (Figure 6—figure supplement 1C) due to the chimeric read rescue that was part of full-length datasets (Figure 7—figure supplement 10). Therefore, for this setting, we leverage the higher overall depth of the datasets and evaluate the multi-read assignment accuracy at different resolutions, that is, 10 kb and 40 kb.

### Simulation procedures

We devised a simulation strategy that utilizes parameters learned from the Hi-C data and results in data with a similar signal to noise characteristics as the actual data.

We generated numbers of multi-reads comparable to those of replicate six. In the final step of the simulation studies, we merged the simulated set of multi-reads with uni-reads of replicates three and six and ran mHi-C step4 (binning) - step5 (prior already available) - step6 (assign multi-reads posterior probability) independently at resolutions 10 kb and 40 kb.

### Software availability

mHi-C pipeline is implemented in Python and accelerated by C. The source codes and instructions for running mHi-C are publicly available at https://github.com/keleslab/mHiC (Zheng and Keleş, 2019; copy archived at https://github.com/elifesciences-publications/mHiC). Each step is organized into an independent script with flexible user-defined parameters and implementation options. Therefore, analysis can be carried out from any step of the work-flow and easily fits in high-performance computing environments for parallel computations.

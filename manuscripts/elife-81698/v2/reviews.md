# Peer review - Round 1

Editors:
- Ziyue Gao, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81698.sa0](https://doi.org/10.7554/eLife.81698.sa0)

This important study presents a new method for homozygosity mapping in population-scale datasets, based on an innovative computational algorithm that efficiently identifies runs-of-homozygosity (ROH) segments shared by many individuals. Simulation results provided convincing evidence for good accuracy and power of the new algorithm. Application of this new method to the UK Biobank dataset largely recapitulated previously known associations but also revealed a small number of novel discoveries that were missed by existing genome-wide association study methods, highlighting the utility of this new approach. This study will be of substantial interest to readers in human genetics and quantitative genetics.


---

# Peer review - Round 1

Editors:
- Ziyue Gao, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81698.sa1](https://doi.org/10.7554/eLife.81698.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Discovery of runs-of-homozygosity diplotype clusters and their associations with diseases in UK Biobank" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Molly Przeworski as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Shai Carmi (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

All three reviewers agree that the approach presented is innovative and potentially useful for future applications in large biobank datasets. However, the performance of the algorithm for identifying ROH diplotype clusters is not quantitatively characterized to demonstrate a low false positive rate. Additionally, the reviewers noted that most of the ROH-phenotype associations identified have already been found by standard GWAS, and more would be found by GWAS with recessive effects considered, which raises the question about the power of the new approach over existing GWAS methods. Lastly, the identified ROH clusters and associations have not been fully reported. Hence, below are the essential revisions that the reviewers suggest, and specific analyses are laid out in detail in their reviews below:

1) The authors need to quantify the error rate of all the identified ROH clusters by going back to the diploid genotype data to confirm that (1) each individual in the cluster is truly (nearly) homozygous across the identified ROH segment; (2) individuals in the same ROH cluster do share the same diplotype. It is also recommended to simulate genotypes with errors (or mutations) to characterize the sensitivity and false positive rate of the ROH detection method. These characterizations will help demonstrate the performance of the new approach and justify (or improve) the choice of parameters for defining ROH clusters (i.e., spanning over 100 SNPs and shared by over 100 individuals).

2) When characterizing the false positive rate of ROH cluster detection, particular attention should be paid to the MHC region, as the reviewers have raised considerable concerns regarding the usually large number of signals in this region. Although the high SNP density and complex linkage-disequilibrium patterns may enable the detection of more short haplotypes shared by identity across individuals, these haplotypes are not expected to be more likely in the homozygous state, so more ROH clusters are not necessarily expected. The authors need to (1) verify （or refute) that most of the identified ROH clusters are real based on the full genotype data; (2) characterize and explain the distribution of ROH segment length in terms of physical or genetic distance, and compare it to that of other chromosomes; (3) consider possibilities of potential technical artifacts, either introduced by the "random allele drawing" of the algorithm or already present in the genotype data (e.g., due to cryptic duplication or structural variation).

3) Although the authors listed a couple of examples where the associations are missed by standard additive effect GWAS, many recent GWAS tools provide alternative models (dominant, recessive, or general) for detecting signals with non-additive effects. It is thus important to quantify the power of the ROH-based method vs. standard (single variant) GWAS with a recessive effect considered.

4) The authors should include more comprehensive reports of the identified ROH clusters and associations in the supplemental materials, which will enable other authors to reproduce the results and carry out follow-up studies.

Reviewer #1 (Recommendations for the authors):

Assuming the ROH diplotype cluster identification is accurate, I wonder if the authors could further utilize the identified clusters to explore the genetic architecture of disease risks (or of other complex traits). For example, one can ask if individuals who shared more ROH diplotype clusters tend to be more similar in phenotypes. Such analysis may shed light on the contribution of dominance variance to heritability for traits of interest.

Assuming the ROH association has good power and a low false positive rate, it should be relatively straightforward and of broad interest to extend this analysis to non-disease complex traits. It will also be interesting to compare the results with findings from previous research based on genome-wide aggregate ROH content.

The direction of the ROH association should be reported for each signal in all tables (including supplementary ones) to indicate if homozygosity of certain haplotypes is associated with increased or decreased risk. Similarly, the direction of the effect size of the non-reference allele should be annotated for GWAS results. The linkage pattern between the non-reference allele of GWAS SNP and the ROH segment should be added.

Reviewer #2 (Recommendations for the authors):

The algorithm itself is reasonable, however, my biggest concern is that assessment of whether the identified segments are statistically significant is lacking. The authors mentioned "the rate of false positives should be low". However, it is not obvious, and the results should be more specific and quantitative.

First, given the IBD sharing or genetic relatedness in a group of individuals, would the identified ROH be explained by chance alone? This should be evaluated.

Second, what part does linkage disequilibrium play in ROH? As reported, the MHC region of chr6 has a ROH hotspot. The MHC region is known to have an extremely high level of LD. If taken LD level into account, would the ROH clusters be significant?

Third, if SNPs are pre-processed, for example only SNPs with certain MAF and with certain LD distance are kept, how would the results look like? Also, the numbers 100 markers and 100 individuals are quite arbitrary. How would the results depend on the choice of parameters, say with 50 and 200 markers, 50 and 200 individuals?

Fourth, the definition of ROH clusters, blocks, and hotspots should be clearly described.

Fifth, two optimization rules are mentioned, and for the UKB data, only the width-maximal blocks were reported. In practice, what are the criteria to choose one rule over another?

Sixth, the disease associations discussed do not represent new discoveries. The significant associations can be identified in the first place if a recessive mode of inheritance is assumed or a more powerful imputation panel was implemented.

Reviewer #3 (Recommendations for the authors):

Please see the annotated PDF file. No need to respond to corrections of typos etc.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Discovery of runs-of-homozygosity diplotype clusters and their associations with diseases in UK Biobank" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The newly added evaluation of accuracy and power of ROH diplotype clusters detected by ROH-DICE is appreciated, but this evaluation is based on simulated genotypes of 200 individuals only, and the combination of detection thresholds evaluated do not match those used in the empirical study of UK Biobank data (L=100, W=100). Therefore, it is highly unclear how accurate and powerful ROH-DICE is expected to be in practice. Understandably, simulating a dataset as large as the UK Biobank is infeasible. It will be useful if the authors could provide some back-of-envelope calculation or semi-quantitative estimation of the power in large-scale genomic datasets such as UK Biobank (even an estimate of the order of magnitude would be helpful).

2. The authors argue that the accuracy of ROH diplotype clusters detected in MHC is comparable to other parts of the genome, because there is no excess clusters detected in MHC, when a genetic distance threshold is used instead of the number of consecutive SNPs threshold. However, Figure 3—figure supplement 1 only shows no excess clusters on chromosome 6, without providing specific information regarding the MHC region. Moreover, beyond the total number of clusters, the authors need to show that the size distribution of the ROH diplotype clusters (i.e., number of individuals in each cluster) of MHC is comparable to elsewhere in the genome, as higher SNP density and low recombination rate is not expected to lead to more people sharing the same diplotype. (Related to this point, additional legend/explanation is needed to explain the y-axis, blocks, and colors of Figure 3B, as the current legend is not sufficiently informative.)

3. The evaluation of the power of ROH diplotype association is based on the strong assumption that the causal variant indeed lies in a long, ROH diplotype shared by many individuals (i.e., ROH diplotype clusters). One might argue that the comparison between standard GWAS and ROH-DICE based on this assumption is unfair, because only a small fraction of causal variants reside in ROH diplotype clusters, and standard GWAS may have better power in other scenarios. A more comprehensive and fair comparison is to assign causal variants in the simulated datasets at random, assuming additive, dominant or recessive effect, respectively. The authors can then quantify the frequency of different scenarios (e.g., causal variants in ROH-diplotype clusters of various sizes or not in ROH segments at all) and compare the performance of the two association methods in different scenarios. (Related to this point, more information (such as the simulated sample size, detection thresholds, assignment of causal alleles) is needed in the legend of Figure 1—figure supplement 3.)

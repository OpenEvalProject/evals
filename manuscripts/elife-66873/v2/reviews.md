# Peer review - Round 1

Editors:
- Vincent Castric, https://ror.org/02kzqn938 Université de Lille France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66873.sa0](https://doi.org/10.7554/eLife.66873.sa0)

This is a comprehensive study of genomic and phenotypic diversity in the orphan crop quinoa. Based on whole genome resequencing of 310 accessions and field phenotyping of the same set of accessions for two years, the study identified the genetic basis of agronomically important traits. Based on this promising work, there will likely be scope for quick improvement of this orphan crop through breeding.


---

# Peer review - Round 1

Editors:
- Vincent Castric, https://ror.org/02kzqn938 Université de Lille France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66873.sa1](https://doi.org/10.7554/eLife.66873.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Genome-wide association study in quinoa reveals selection pattern typical for crops with a short breeding history" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Vincent Castric as the Reviewing Editor and Meredith Schuman as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Justin O Borevitz (Reviewer #2); Stig Uggerhøj Andersen (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers appreciated the useful resource for quinoa and competent analysis of the diversity in this orphan crop. Please find below a list of essential revisions that need to be addressed before we can consider inclusion of this work in eLife. The public peer reviews are also appended for your information and for eventual inclusion alongside your preprint.

(1) There was a consensus that the population genomic analyses do not meet the potential of the dataset and should be further developed; while a good descriptive assessment of quinoa, the results do not allow a larger impact. For instance, an Fst scan could pinpoint candidates for local adaptation between lowland and highland quinoa; local PCA is another option suggested by Reviewer 2, https://pubmed.ncbi.nlm.nih.gov/30459280/. A possibility to substantiate the claim that specific traits are relevant for the differentiation of highland and lowland varieties, could be to combine these Fst scans with GWAS and look for skews in Fst distributions.

(2) To be of more general interest, it would be good to see what the GWAS tells us about evolution of this crop species. Can the authors see if it is associated with selection, maybe in highland vs. lowland? Separate GWAS between the highland vs lowland varieties could be used to check whether the same alleles are controlling traits across subpopulations. Besides the temporal replication, this could provide important information on the replicability of the associations across groups. It is possible that different associations are supported in these two different groups. Specific comments from Reviewer 2:

– For GWAS across the major subpopulations (highland/lowland), a joint analysis is only helpful when the same alleles are controlling traits across subpopulations. Is this the case? How much variation does the kinship matrix explain for the traits? What does the histogram (pairwise accession distances) of kinship look like? If 2 clear groups perhaps separate analysis is preferred.

– In particular DTM, days to maturity, could be highly confounded with highland/lowland ecotype. The multi year field trial data is a very strong part of this paper with direct agronomic relevance, but were the growing conditions typical of lowland, longer season conditions, that prevented many accession from reaching maturity? Many yield traits depend on maturity time and could vary jointly with DTM, eg multitrait analysis or a regression of yield on DTM. You investigate this with PCA(CP), but I don't find this unsupervised approach informative, and it could be excluded.

(3) For a resources paper, it is especially important to clarify the way the data and accessions are made available to the community. To ensure accessibility of the accessions, seeds should ideally be deposited in a genebank, where they are propagated and can be ordered online. Otherwise, it might be difficult for others to get hold of the seeds in practice. If that is not possible, please specifically state that the seeds can be obtained from the authors. The genomic data should ideally be made available through a public genome browser, or alternatively deposited in appropriate databases (including the vcf files).

(4) There was also a consensus that the description of the candidate genes was too assertive, as the associations do not demonstrate causality at this stage. This should be toned down.

5) Regarding SNP calling, reviewer 3 made important suggestions to evaluate robustness of the results to a number of potential pitfalls (coverage and repetitive regions):

– The correlation between coverage and heterozygosity levels represents a serious issue that should be addressed. It seems that you need more than 6x coverage to achieve accurate calling. The obvious solution would be to carry out additional sequencing, but this would cause significant delays. Another option would be to scrutinize the information in the VCF files. Many SNP-callers, including GATK, tend to err on the side of caution and call heterozygotes rather than homozygotes in difficult cases. You may well be able to salvage accurate data from the low-coverage individuals by adjusting genotype calls based on the genotype likelihoods. You could require compelling evidence for a heterozygote before it is called, instead favoring the most like homozygous genotype. Please provide a scatter plot of depth versus heterozygosity level to demonstrate that the issue was resolved.

– Although you have very reasonably applied a mapping quality filter to reduce the problem of poor-quality SNPs derived from repetitive regions, problems could persist. If I read Table S5 correctly, there is an overwhelming majority of intergenic SNPs. It would be interesting to see what happens if you eliminate SNPs in repetitive regions, as determined by RepeatMasker or similar, and then rerun the GWAS. If the repetitive regions contribute false positive SNPs with random genotype calls, you should get cleaner results with more significant associations.

– A specific example is lines 218-227, where you argue for mapping resolution. The argument does not appear strong as none of the top SNPs in the region are located in the two candidate genes according to Figure S14b. Also it is unclear from that figure how many other genes reside within the region. It would be preferable to use the extent of LD compared to gene density as a general argument for mapping resolution.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Genome-wide association study in quinoa reveals selection pattern typical for crops with a short breeding history" for further consideration by eLife. Your revised article has been evaluated by Vincent Castric as Reviewing editor and the evaluation has been overseen by Meredith Schuman as Senior Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1 – The section on « genomic patterns of variations between highland and lowland quinoa » has been expanded, but unfortunately at this stage it remains too descriptive. We understand from your response letter that a more comprehensive analysis of the demographic and selective history of quinoa is in preparation, so we suggest that this section could be shortened to include only : (1) the strong population differentiation between highland and lowland accessions, (2) the comparison of LD decay, nucleotide diversity and Tajima's D between highland and lowland, (3) the local PCA and a comparison of average FST across chromosomes to test for heterogeneity of patterns of differentiation. e.g. Do some chromosomes show a lower FST and different contribution to the three corners of the PCA, in particular Cq6B, as would be expected if it experienced recent introgression?

2 – The issue raised by reviewer 3 that the modest sequencing depth could lead to inaccurate SNP calling was correctly addressed by plotting mean heterozygosity vs sequencing depth across the 310+ accessions, but it is incomplete. The reviewer suggested that the genotype likelihood threshold to call heterozygous sites could be adjusted for each accession by examining the mean sequencing depth and mean genotype likelihood between heterozygous and homozygous sites. The eventual difference of means between accessions with high vs low overall coverage could be used to adjust the threshold.

3 – Along the same lines, a missing piece of basic information is the proportion of SNPs called as homozygous vs heterozygous. Given the high selfing rate, a high proportion of homozygous SNPs is expected. Is this observed, and does that vary across accessions?

4 – Finally, reviewer 3 had also suggested restricting the set of SNPs to those outside repeated regions, as identified by e.g. RepeatMasker in the reference genome. Even using stringent filters to identify SNPs will not totally alleviate the problem of SNP calling in repeated regions, and these will remain dubious. Please do consider testing whether the marker-trait associations detected are still detected (and perhaps more convincingly so) when removing SNPs in repeated regions.

5 – The text contains too many acronyms that are rarely useful. Examples of acronyms that are not repeated frequently and could make the text a lot easier to follow if the words were instead written in full include : HCSNPs, NoB, STL, DTM, PL, PH, TSW, GT, DTB, DTF, PCA(PHEN), BLUE, MTA, BBCH60, BBCH94.

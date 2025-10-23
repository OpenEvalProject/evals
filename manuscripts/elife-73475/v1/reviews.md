# Peer review - Round 1

Editors:
- Benny Chain, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73475.sa0](https://doi.org/10.7554/eLife.73475.sa0)

This study demonstrates that genetic differences in areas of the genome outside the regions that encode the TCR genes can affect the molecular properties of the TCRs that are made by somatic recombination. This paper will be of interest to a broad swathe of immunologists who study such variable lymphocyte receptors. It combines several large datasets in an extremely statistically rigorous analysis, producing results consistent with but substantially expanding upon the prior knowledge of the field.


---

# Peer review - Round 1

Editors:
- Benny Chain, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73475.sa1](https://doi.org/10.7554/eLife.73475.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Combining genotypes and T cell receptor distributions to infer genetic loci determining V(D)J recombination probabilities" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Benny Chain as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James M. Heather (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please respond to the specific issues raised by reviewers 2 and 3.

Reviewer #1 (Recommendations for the authors):

The genetic association data seems mostly convincing.

In addition to the Manhattan plots, it would be very informative to see the actual effects on variable gene freqeuncy, their magnitude and the extent to which different genes are regulated together – e.g. do some SNPs regulate several different Vs together? Similarly, more detail on the magnitude and details of the effects seen on basde pair deletion and addition would perhaps contribute to a better understnading of the importance and impact of the genetic regulation.

Weaknesses of the study: 1. Limited additional understanding of the process of regulation of T cell receptors; limited validation of results in an independent data sets.

Overall, the findings are sound, but of incrememental importance in understanding TCR repertoire generation. A more specialised human genetics journal may be a more appropriate place to publish these results, and the methodology for conditioning one outcome on another outcome, rather than the more general readership of eLife.

Reviewer #2 (Recommendations for the authors):

This manuscript is already extremely well put together, making it a genuine pleasure to read, so I have only a few recommendations.

(1a) I think it may be useful to have the ZNF peaks on Fig 1 labelled in some way. They definitely stand out when you the paper, yet are not addressed in the narrative of the paper until a figure or two later.

(1b) On a related note, unless I missed it, it's probably worth explicitly mentioning that the TRVB24-1 association with ZNF443 was also observed in the Sharon et al paper too.

(2) Fig 3 seems to show some signal for a weaker but significant SNP association with trimming on chr23. This is another observation that leaps out to the reader, but one for which I couldn't find a mention of in the text at all.

(3) I appreciate that I may be unwittingly stirring up a well-trodden semantics issue from a field not my own, but would not many of these associations be considered eQTL? At the very least those involving productive gene expression as shown in Fig 1. If so I think it might be helpful to include the term in the text somewhere, even if only buried in the methods, purely to make this paper more likely to be returned in relevant literature searches.

(4) I'm not sure how practical a request this is, but given the discussion of SNP coverage in the public review section: is there any way for the authors to measure (or even speculate) as to what portion of known TCR loci polymorphisms are covered by the SNP arrays used in these datasets? It feels like a number that might be helpful for contextualising the results of this study.

(5) Lines 156/157 report that various SNPs associated with the expression "of the V-genes TRBV24-1 and TRBV24/OR9-2". A very minor pedantic point, but this sentence does make it sound like the expression of both genes (or expression of recombinations using both genes) is going up. Seeing as TRBV24/OR9-2 resides on another chromosome, it's almost certain that in actuality it's just that TRBV24-1 TCRs are increasing and the orphon gene recombination levels are remaining steady around zero. Incidentally this is a good illustration of a case where the short Adaptive reads can't discriminate between two genes, even when the immunological importance differs widely.

(6a) While I didn't have time to actually run the code, I did note that the first step in the README is a little vague ("Download data into the directory ..."). A little more instruction would be very useful here, as in my experience half the battle in getting other people's analyses running is matching input data formats. Obviously the manuscript lists the accessions of the data themselves, but explicit discussion of the pre-processing steps would be extremely helpful for anyone wanting to re-run or adapt these analyses. (I see that some information is planned to be included on Zenodo prior to publication, so if this is to be included there please disregard this comment.)

(6b) On a related note, I noticed that a few details relevant for repeatability have been omitted from the methods. In particular the versions and non-default parameters of software tools used (e.g. for the TCRdist and MiGEC VDJ analyses), and the date of accession of databases (e.g. IMGT/GENE-DB) should be included. Given the nature of this manuscript and the frequency of changes to GENE-DB I would even recommend actually uploading the specific version(s) of the database that were used.

(7) The lines of Fig 9B are very narrow, which makes it very hard to tell the difference between some of the groups (especially in the legend). Perhaps the lines could be made wider, or some lines made dotted or dashed or something, so as to make the groups easier to distinguish.

(8) The observation that the different ancestry-associated groups differ in some of their recombination parameters is very interesting: I can't recall seeing similar data before, beyond some general V gene expression level differences (typically thought to be a consequence of differing HLA allele distributions). However, having never performed such an ancestry-informative PCA before I have what may be naive concerns about it. For instance, of the ~400 people in the cohort, it seems that all are assigned to one of the groups, while I would presume that out of those 400 people there are likely some multiracial individuals or those who just fall out of the typical expected SNP distributions (which Fig 9 would suggest is the case). Some more discussion of this issue may be instructive for those like myself who have never run such an analysis. For example, are those individuals who are further from the center of their respective clusters - or perhaps those whose clustered ancestry group is different to their self-reported one - enriched in the outliers in Figs 7 and 8? Similarly, I'm curious as to how many individuals in each group end up assigned to another, and to which. These considerations seem especially important given the different sizes of the groups (with the 'Caucasian' associated group having hundreds of individuals, and the other groups mostly having fewer than ten), and the fact that the target clusters are themselves informed by the original input reported groupings. While obviously beyond the scope of this manuscript, it's interesting in itself to note that such an observation hasn't been made before. Presumably most TCRseq studies are not large or diverse enough to have detected such differences (even had people been looking)?

Reviewer #3 (Recommendations for the authors):

1. Regarding the datasets, full information regarding the donors from which the data have been used need to be summarized in a Table and couple of figures to identify possible (or no if this is the case) bias in terms of sex, age, ethnicity, influenza exposure in the days before the sample collection, CMV serotype, etc… Indeed, all these factors can influence the repertoire composition, and maybe some correction/normalization should be applied.

2. On the source data table containing 9957 associations, 43 TRBV out the 66 mentioned showed significant associations with 1 to 508 SNPs. For several TRBV genes, the association with SNPs was significantly different according to the productive vs nonproductive origin of the TRBV in the dataset. Same for the 10 TRBJ (out of the 14 tested) showing significant associations with SNPs.

First, the "significant association" column in Table 1 should reflect those results by indicating the number of V genes and J genes found to be associated with at least one SNP above the significance threshold.

Second, in the data source table we can see some V gene usage (and J gene usage as well) from nonproductive and productive rearrangements are associated with various number of SNPs. What is the overlap of the SNPs associated with each V according to its nonproductive/productive origin? In addition, a general comment on the use of nonproductive rearrangement data. Such "part" of the TCR repertoire is believed to reflect TCR generation independently of TCR selection. However, when analysed from blood TCR repertoires (like in this study), it is still unclear how much the nonproductive "repertoire" is biased by the fact that it is directly dependent on the productive, and therefore centrally/peripherally selected. Therefore, the variations associated at the V, J usage (as well as the trimming) may be biased by the immune history of every individual. Author should control on this possible bias or disregard the differences between productive vs. nonproductive sequences. The only dataset that could help address this question would be thymic cells at the different stage of differentiation.

Third, in the text it is indicated that "variation in the TCRB locus is most significantly associated with the expression of the gene TRBV28 for both the productive and nonproductive". Unless I missed something, this is also (maybe more) true for TRBV12-3, TRBV12-4 (known to be highly expressed in general) as well as TRBV24-1, accounting for respectively 353, 358 and 319 SNP associations compared with 424. Are those differences significant? Are you referring to TRBV28 for a particular reason (major overlap between SNPs associations between nonproductive and productive for instance or something else)? This should be clarified and detailed.

3. On the association between HLADRB1 and TRBV10-3, the authors refers to two other studies that found such association however they omit to discuss the fact that on those studies they found in fact other TRBV gene usage to be much more associated with the HLADRB1, notably TRBV20-1 (Gao et al., 2019) which is not found from the Emerson dataset. Are the differences associated with the ethnicity (as Gao paper is mainly done on Asian population)? Maybe to provide some functional relationship of the associations, it could be of interest to analyze data from patients with AIDs, such as RA, SLE, Sjogren syndrome known to be associated with HLADRB1. Data from the Rossetti paper Rosseti et al., (Annals of Rheum Dis, 2017; TCRb data from Adaptive available online) as well as from the Liu et al. (Annals of Rheum Dis, 2019). For instance it could be of interest to determine whether in RA or SLE patients, a differential usage of TRBV10-3, TRBV20 compared to controls has been shown. Eventually, if DNA is still available, ensure the HLADRB1 genotype to correlate with the observations.

4. Regarding the SNPs association with the gene trimming and N-insertion numbers, interestingly the genes showing SNPs association with this TCR repertoire feature are definitely biologically linked. However, although the author distinguish the impact of the gene and on the trimming versus N-insertion, since the resulting repertoire analyzed is a post-selection repertoire, the observation are still bias by the selection effect. Moreover, it is also well known that shorted TCRs are more frequent in general, than long ones. In other word, authors should control for these bias and provide more evidence on the actual SNPs identified between the discovery and the validation cohorts.

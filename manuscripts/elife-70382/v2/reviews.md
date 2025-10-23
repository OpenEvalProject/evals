# Peer review - Round 1

Editors:
- Magnus Nordborg, https://ror.org/03anc3s24 Austrian Academy of Sciences Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70382.sa0](https://doi.org/10.7554/eLife.70382.sa0)

This is an original human GWAS study that treats mitochondrial copy number variation as a trait, and investigates its genetic basis, as well as its association with (and possible causal role in) various human diseases, such as cancer and dementia. The study identifies 71 significant loci, show that these are significantly over-represented in a priori candidates, and argue convincingly that this could help us understand how mitochondrial copy number is regulated at a cellular level.


---

# Peer review - Round 1

Editors:
- Magnus Nordborg, https://ror.org/03anc3s24 Austrian Academy of Sciences Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70382.sa1](https://doi.org/10.7554/eLife.70382.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "GWAS and ExWAS of blood Mitochondrial DNA copy number identifies 71 loci and highlights a potential causal role in dementia" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Magnus Nordborg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Y M Dennis Lo as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Your method for estimating mtDNA copy number needs to be better described and explored. We need: a more detailed description of the approach; a more thorough benchmarking (comparing to standard approaches and against estimates from sequencing data); a more thorough description of the phenotype and its distribution; comparisons with age, sex and other UK Biobank phenotypes; description of samples removed and the rationale for removing them.

2. More thorough Mendelian Randomisation analysis: test for pleiotropy using Heidi; perform comparative analysis using all genome wide significant hits (with accompanying discussion of any differing results).

3. Place work in context of other two highly similar recent studies (Longchamps 2021 and Hagg 2021).

4. Data release: code should be on GitHub, raw data for mtDNA-CN estimates and covariates provided where possible, summary statistics uploaded to GWAS catalogue.

5. A bit more discussion of potential population structure confounding? You focus is on individuals of European decent, with meta-analysis including non-Europeans giving similar results.

Reviewer #1:

This is an original human GWAS study that treats mitochondrial copy number variation as a trait, and investigates its genetic basis, as well as its association with (and possible causal role in) various human diseases. The main strength of the study is the development of a method for estimating mitochondrial number from standard array data. This makes it possible to reuse the vast UK Biobank data (n = 383,476) and work with much larger sample sizes than previous studies. The estimated phenotypes are sensibly QC-ed using various data.

They then carry out a standard GWAS, identify 71 significant loci, show that these are significantly over-represented in a priori candidates, and argue convincingly that this could help us understand how mitochondrial copy number is regulated at a cellular level. They show that rare SAMHD1 variants associated with high copy number are also associated with increased cancer risk, and, finally, that mitochondrial copy number may play a role in dementia.

The study represents clever re-use of data, and the findings appear to be well supported and should be interesting to a broad audience. Unlike many human GWAS, there is clearly real biology here.

Your analyses appear admirably solid to me, but this need to be verified by an expert on human GWAS. The same is true for the novelty of the results.

The only improvement I would like to see lies in the description of the estimated phenotype. There is little detail about its distribution, and I would also like to learn more about the factors influencing it, including, obviously, an estimate of much of the variation your 71 loci explain, and a discussion of what explains the rest of the variation. The UK Biobank is full of data…

Reviewer #2:

Mitochondrial DNA copy number is a significant aspect of mitochondrion function, both of which have been linked to disease states. This is an interesting assessment of the genetic basis for variation in mitochondrial DNA copy number. The authors describe a new method for mtDNA CN estimation, although additional benchmarking and validation is warranted in this reviewer's opinion. The GWAS/ExWAS analyses are fairly standard and identify genetic variants likely influencing mtDNA CN. The implementation of the MR analyses is more superficial; it remains unclear in this reviewer's opinion that pleiotropy has been effectively ruled out. The estimates of mtDNA CN and other non-other non-identifiable information (eg, sex, age, ethnic group, etc) necessary to replicate the author's findings should be made publicly available as easily accessible supplementary files.

1. Regarding the method for mtDNA estimation. The method is barely described in the main body of the manuscript. More information should be provided in the main manuscript given that the method it is so essential for this work. Greater clarity about the reproducibility would have helped. Also, it appears that the estimates of mtDNA CN were not tested against a standard with known CN, could this be performed? Some benchmark was done with qPCR estimates, while the results of the methods here developed and qPCR are positively correlated, the magnitude of the correlation is moderate. Finally, wow does the new method compare with sequencing based estimates? All in all, more benchmarking of the method in the main manuscript would greatly improve the paper.

2. Besides better description of the methods for mtDNA CN estimation, a much more detailed description of the mtDNA CN data should be provided in the main manuscript. It is not possible to properly understand/appreciate the reported associations and MR results without such description of the underlying mtDNA CN data.

3. In this reviewer's opinion the pre-computed mtDNA estimates and other non-identifiable information (eg, sex, age, ethnic group, etc) necessary to replicate the author's findings should be made publicly available in supplementary text format files and that could be easily accessible to readers. If the text files are too large for eLife the authors should upload the files to Dryad, dbGaP, etc.

4. The author's state that "After quality control, 359,689 British, 10,598 Irish, 13,189 Other White, 6,172 South Asian, and 6,133 African samples had suitable array-based mtDNA-CN estimates for subsequent GWAS testing. It is unclear what the authors mean by "suitable" in this case. It would also be good to describe in the main text how many were unsuitable in each case and the reasons why these estimates did not match the requirement for suitability.

5. It is unclear if the authors detected ethnic and/or population differences that might confound the other downstream analyses. It is also unclear what are the error and reproducibility of the CN estimates.

6. The influence of sex and age are not described (or superficially described).

7. The presentation of the MR results is unconvincing. For the analysis, the authors have not ruled out pleiotropy in my opinion. Heterogeneity tests such as Heidi should be used Zhu, Z. et al. Integration of summary data from GWAS and eQTL studies predicts complex trait gene targets. Nat. Genet. 48, 481-487 (2016) in addition to MREgger. Also, dementia seems to have the largest error bars around its OR estimates. More detailed analyses and discussion could help here.

Reviewer #3:

This work develops and presents an adapted approach to quantify mitochondrial DNA copy number (mtDNA-CN) from DNA genotyping arrays (named AutoMitoC) by using the intensity of probes emanating from the mitochondrial genome and then using a series of control and normalisation steps that can be applied within a standard framework across data from different populations. They use their estimates of mtDNA-CN as a quantitative trait within a genome wide association study to identify genes and genetic variants that are associated with variation in this phenotype, using both rare and common polymorphisms. Through multiple complementary approaches they then identify a large number of genes that are linked to mtDNA-CN, including those that are involved in mtDNA depletion disorders and various different components of mitochondrial function. Within this, using rare variant analysis they find SAMHD1 as a potential regulator of mtDNA-CN (and possibly breast cancer risk), and the authors suggest that the product of this gene may make a good draggable target to control the downstream effects of altered mtDNA-CN. Finally, the study uses Mendelian Randomisation analyses between genetically determined mtDNA-CN and a selection of disease phenotypes that have been linked to mitochondrial processes previously, and in doing so they find a link between mtDNA-CN and dementia.

In general, the work appears robust and achieves the aims of uncovering the genetic architecture of a disease relevant phenotype, and its potential downstream implications. Readers of this article should be aware of two further studies that have performed similar analyses on largely the same data as those described in this paper. The first by Hagg et al. (2021) considers largely the same set of individuals and identifies 50 genetic loci associated with variation in mtDNA-CN across individuals. The second by Longchamps et al. (2021), finds 129 independent genetic variant associations and includes additional data from a different cohort. The study presented here discusses the findings of Hagg et al. (although a direct comparison of genes is not given) but does not interrogate and compare results from the Longchamps study, which is necessary to truly understand the genetic architecture of this trait and to place this work in context. For the comparison with Hagg et al., the authors suggest that their improved method for mtDNA-CN quantification leads to a higher number of genetic associations, although a more formal comparison of AutoMitoC and standard approaches against control data like that generated from qPCR would make this statement more robust (there is a comparison between AutoMitoC and Hagg et al. quantification in the Discussion section, although it is not clear whether this comparison is like-for-like using the same set of samples). In general, many of the bigger picture biological findings are shared across the three studies (many shared loci and enrichment of genes involved in mtDNA depletion syndrome and mitochondrial processes), which is an excellent advert for reproducible science.

The additional strength of the work by Kong et al. are two extra pieces of analyses not found in other works – an analysis of rare variants and the implementation of Mendelian Randomisation to link variation in mtDNA-CN to disease risk. For the Mendelian Randomisation analyses, authors select genetic variants associated with mtDNA-CN based on their likely role in mitochondrial processes (those variants falling within or close to a mitocarta gene). This is rational given the assumption in Mendelian Randomisation analyses, that genetic instruments should be causal, but it would also be useful to also consider the full set of genetic variants that are associated with mtDNA-CN at genome wide significance to test the relevance of selecting a subset of genetic variants.

References:

RJ Longchamps et al., Genetic analysis of mitochondrial DNA copy number and associated traits identifies loci implicated in nucleotide metabolism, platelet activation, and megakaryocyte proliferation, and reveals a causal association of mitochondrial function with mortality. bioRxiv 2021.01.25.428086; doi: https://doi.org/10.1101/2021.01.25.428086

Hägg S, Jylhävä J, Wang Y, Czene K, Grassmann F. Deciphering the genetic and epidemiological landscape of mitochondrial DNA abundance. Hum Genet. 2021 Jun;140(6):849-861. doi: 10.1007/s00439-020-02249-w.

1. Page 3, lines 3-8 (but also throughout the text): Whilst it is appreciated that there is a vast body of literature pointing to links between mtDNA-CN and complex disease, I think it is worth briefly discussing caveats to these results in order to properly frame the relevance of the work. For instance, there are many studies showing that links between blood derived mtDNA-CN and age-related diseases may at least in part be driven by cell type composition. There is also plenty of debate around whether mtDNA-CN in blood is indicative of processes in other tissues which might be more relevant for each particular disease. Much of these caveats have been recently neatly summarised in Picard 2021.

2. Page 9, lines 16-17: "We postulated that mtDNA-CN loci may regulate copy number by inducing changes in expression of genes that are directly transcribed from mtDNA.": I don't understand this rationale – are you postulating that lower/higher expression from the MT genome may trigger changes in copy number (and thus these may be modulated by variants influencing expression)? If so, this should be stated more clearly, if not, please explain the thinking here. I also think that it is worth rewording your conclusions from this analysis, as there is no test of directionality.

3. Page 9: lines 31-41: Similar to point 2, it would be good to be a clear rationale for the comparison of loci associated with mtDNA-CN and heteroplasmy level.

4. Page 10: lines 29-35: It would be good to see statistical tests comparing the fractions of genes that fall into the mitochondrial process categories described here, versus proportions of genes in these categories in Mitocarta as a whole – are these categories enriched for genes identified in this study?

5. Page 25: lines 20-31: Links should be provided in any revised manuscript, including the GitHub repository for the method, and summary statistics should be uploaded to the GWAS catalogue.

6. Figures: In general, the figures are not particularly clear and should be improved for publication. For example, axes text is often too small and difficult to read, and text labels on figures 1 and 2 are not aligned properly.

References:

Picard, M., Blood Mitochondrial DNA Copy Number: What Are We Counting? Mitochondrion (2021), doi: https://doi.org/10.1016/j.mito.2021.06.010

# Peer review - Round 1

Editors:
- Eduardo Franco, McGill University Canada

Reviewers:
- Rachel Daniels, Harvard School of Public Health United States
- Bryan Greenhouse, University of California, San Francisco United States
- Steve Schaffner, Broad Institute United States

## Review text

DOI: [10.7554/eLife.40845.039](https://doi.org/10.7554/eLife.40845.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The origins and relatedness structure of mixed infections vary with local prevalence of P. falciparum malaria" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor and Eduardo Franco as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rachel Daniels (Reviewer #1); Bryan Greenhouse (Reviewer #2); Steve Schaffner (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In the discussion among the reviewers, the opinion emerged that this work was more appropriate as a Tools and Resources submission than as a Research Article. One reviewer commented that "the "epi" part is a bit of a stretch but the tool is the real (potential) advance. Regardless, I do think that for the tool to be published still requires additional work on validation and on the clarity of the methods and validation results."

Summary:

The authors address an important and challenging problem – phasing genotypes from deep sequence data obtained from mixed-strain falciparum infections. The manuscript is essentially a methods paper and offers a significant advance on the authors' prior work in this area (DEploid) in that it explicitly considers relatedness (IBD) between strains found within the same infection, primarily as a result of co-transmission. The new tool is validated in lab and in silico mixtures of parasite chromosomes. Following this validation of performance, DEploidIBD is applied to samples from the pf3K database and correlated to data on local prevalence from the Malaria Atlas Project.

The manuscript is overall well-written, with clear pseudocode and well-explained supplementary material; however, there are additional considerations that could perhaps improve the conclusions from the analysis and better delineate the advantages of this improvement over both the previous version and other reports

Essential revisions:

1) In general, I find it difficult to clearly understand how well the method is expected to perform based on the simulations. Most of the comparisons presented are between DEploidIBD and DEploid, and the authors do convincingly show an overall relative improvement. However based on the extent of the simulations and way the results are presented it is difficult for the reader to understand in what settings the method it is likely to perform well and where it is likely to fail. This is critical for the reader to understand the utility of the method. Regarding the extent of the simulations, the laboratory mixtures perform well but with only four strains in the population and optimal reference panels this is not a realistic test. The authors go on to perform in silico mixtures from Asia and Africa, but the former is presented for up to 3 strains while the latter (a more challenging dataset) is only presented for up to two strains. The method as presented is designed to work for up to four strains, and thus should be tested as such. It is quite possible that the information content for some (many) of these cases presents an identifiability problem even with a perfect method, however it would still be useful to provide the reader with information as to the limitations of the data/method. It may also be useful to evaluate the sensitivity of the method to the correctness of the reference panel, for lab mixtures and potentially also for in silico sims.

2) It is difficult for me to understand how well the deconvolution process worked on the simulations. This may in part be a result of my not fully understanding the statistics presented. For switch errors, what are the number of true switches for comparison? How are these errors defined (e.g. if the switch occurs 1 SNP in the wrong direction is it still considered an error?). How is genotype error calculated? Is this the percent of SNPs incorrectly phased within each deconvoluted haplotype? Does the denominator for this error include trivial cases (homozygous calls) or the only the more meaningful heterozygous calls in that sample? This is critical to understand, given the high proportion of "low confidence" haplotypes called on real samples.

3) Because phasing haplotypes is one of the primary goals of the software, evaluating haplotype quality from unknowns is of critical importance. The mechanics of the haplotype quality assessment is explained in the supplementary material, but the authors should explain why outliers in the proportion of alternative calls would be a good indicator of a problematic haplotype. Are these alternative calls with respect to the 3D7 reference genome, or to the reference panel used by the software? I presume the former but if the latter this should be made more clear. It would also be good to evaluate this method for "QC" of the outputs on simulations, in particular more complex simulations as discussed in my comment above.

4) Related to #3, in looking at haplotype quality in the real data (Figure 3A) it appears that more than half of polyclonal samples from Asia and ~75% of polyclonal samples have poor quality haplotypes. These numbers are not reflected well in Appendix 3—table 1, which lump in the (trivial) monoclonal samples, and Appendix 3—table 2 which lump together Asia and Africa. I also cannot reconcile the numbers in Appendix 3—table 2 with Figure 3A, e.g. >80% of COI==4 samples appear poor in Figure 3A but Appendix 3—table 2 mentions this figure at 57%. Perhaps the table and the figure representing different things, but if so I missed that distinction.

5) The impact of the population level correlations of output metrics with epidemiologic data are overstated in a few places in the manuscript, in particular in the impact statement which says that "monitoring fine scale patterns of mixed infections and within sample relatedness will be highly informative for assessing the impact of interventions." It is possible that with additional data and likely some sophisticated modeling this will be turn out to be true, but the general correlations with epidemiologic data presented in this manuscript, while qualitatively showing relationships in the expected direction (for Africa, but not in Asia) are neither unexpected nor quantitative in any way that would provide actionable information beyond basic surveillance data. The potential is certainly there, but the data presented do not support this claim.

6) The results in this manuscript, based on samples collected primarily in symptomatic individuals, cannot be generalized to infections in general, the vast majority of which are asymptomatic in moderate to high transmission areas, and in which the relative probability of superinfection to co-transmission is likely much greater since infections more easily stack up in semi-immune individuals with less chance of symptoms and thus treatment. E.g. "more than half of mixed infections arise from the transmission of siblings".

7) There are major concerns over validation and since this is a methods paper, that is a key component so that the reader can assess the usefulness in their own situation.

The method was validated by analyzing:

A) 27 experimental mixtures of 1 – 3 strains with no IBD betweenthem. The arrangement should provide an easy test for the method,since it employs highly divergent strains and an ideal referencepanel. DEploidIBD performs as well as DEploid, except for one casewhich it gets wrong. The authors comment that "LD information isnecessary to achieve accurate deconvolution". This confuses me, since as described both methods include LD information through the reference panel. What does this mean, and why did the new method perform more poorly than the original?

B) Simulated chromosomes with IBD made of mixtures of (a) pairs of

Asian strains, (b) pairs of African strains, (c) triplets of Asianstrains with a rather artificial IBD pattern. My concern here is thatthe performance of the method has not been tested over the relevantrange of complexity (e.g. that seen in this study). How does it workfor more realistic combinations of 3 strains, or for 3 Africanstrains, or for 4 strains? The method could still be quite valuableeven if it cannot handle something like 4 strains, but it would bevery helpful to know its limits. Also, why was (b) not compared to theperformance of DEploid?

8) The quality of reconstructed haplotypes is determined by comparison with monoclonal samples: haplotypes that look either too similar or too dissimilar to the reference are discarded. Are these haplotypes discarded anywhere besides the meiosis analysis? Are they included in COI estimates? More importantly, the number of discarded haplotypes is sometimes very large, e.g. 45% of all haplotypes for Ghana are discarded, and 57% for COI=4 from all populations. It is hard to have confidence in the remaining haplotypes when so many are clearly wrong, especially since there is no independent basis for exclusion. Further treatment of these poor quality haplotypes how they are generated or how they can be prevented, or what output is unaffected by them is needed.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The origins and relatedness structure of mixed infections vary with local prevalence of P. falciparum malaria" for further consideration at eLife. Your revised article has been favorably evaluated by Eduardo Franco as the Senior and Reviewing Editor, and three reviewers.

The manuscript has been improved. All reviewers acknowledged the substantial improvements and the extra work that was required. They also acknowledged the detailed and thoughtful responses you provided to address the first review round. However, there are some remaining concerns that they raised and which need to be addressed before acceptance, as outlined below.

Comments from the reviewers (edited and rearranged for concision and clarity):

1) It is still not clear how the authors differentiate the probabilities of identity-by-state from identity-by-descent, or how they account for this difference in their methodologies.

2) A few items remain unclear:

a) Appendix 1, subsection “Modelling mixed infections with IBD”: prec is introduced here, but it is not clear how it is calculated.

b) Appendix 1, subsection “In silico mixtures of two field strains”: How are the regions of identity between genomes formed, i.e. how are breakpoints set between segments?

c) The handling of the number of strains (K) is not explained well. The authors say "The priors on the number of strains, K, and their proportions, w, are as in Zhu et al., 2018, with associated hyperparameters being user-defined", but that paper doesn't describe priors or associated hyperparameters for K. Rather, it says the number of strains is fixed at a high value and minor strains dropped in the end. This approach also seems to be reflected in the subsection “MCMC parameters for deconvolution”, of Appendix 1,. Since calculation of other parameters is conditional on K, I find this to be quite confusing.

3) The authors have done a great deal of additional simulation to more fully explore the effectiveness of their algorithm. My only suggestion here is to have a few lines summarizing their conclusions about the situations in which the program works well; ideally, this information should appear in the Abstract as well, since it is one of the more important take-aways from the paper.

4) More context and discussion are now provided about the pruning of haplotypes, which is good. There does seem to be curious gap, however. The error rate for reconstructed haplotypes is determined for simulated complex infections, and low-quality haplotypes are identified and removed from real complex infections, but I do not see any connection described between these two activities. Were low quality haplotypes filtered out from the simulated data? Were there any low-quality simulated haplotypes? The simulated dataset is the obvious context for assessing the effectiveness of the filtering procedure, so it's puzzling that this is not described.

5) Figure 2 attempts to convey a large amount of information, and does this very nicely. A few things still took me some time to decipher and wonder if there is any other way to make this easier for a reader. One was the horizontal histograms of K – the bins go from top to bottom and are indicated by value/α of the orange and blue but since there is a lot of gray and absent bins is took a while to figure this out despite the key at the top. I don't have a great suggestion as numerals would likely be too cluttering, but maybe at least mentioning explicitly in the figure legend that K=1 is at the top and K=4 at the bottom? Also, do the "coverage below 20" mean samples with median sequencing depth <20x? Maybe define explicitly in the legend?

6) Figure 3 re: per site genetic error, because many sites in a given sample will have homozygous calls and always be assigned correctly, it could be useful to convey what the (e.g. mean) null expectation would be as a benchmark, i.e. if assignment occurred at random. I'm not sure how easy this is to do or would be worth it, but would make the error result more interpretable (and likely might vary for different scenarios).

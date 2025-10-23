# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66857.sa1](https://doi.org/10.7554/eLife.66857.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Tonkin-Hill and colleagues present a large set of deep sequencing data from acute SARS-CoV-2 infections with each sample sequenced in duplicate. They use these data to characterize the within-host mutational patterns and diversity and relate them to SARS-CoV-2 diversity in consensus sequences sampled around the globe. It further allows understanding how this variation can or cannot be used to understand transmission dynamics and other applications in genomic epidemiology. The authors also provide extensive raw and processed data that can serve as a basis for further analysis of intra-host variation of SARS-CoV-2.

Decision letter after peer review:

Thank you for submitting your article "Patterns of within-host genetic diversity in SARS-CoV-2" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Richard A Neher as Reviewing Editor and Reviewer #1 and the evaluation has been overseen by Sara Sawyer as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Adam S Lauring (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers agreed that you present a very valuable dataset of impressive size and quality, that illuminates many important questions of within-host diversity. But the reviewers have made a number of suggestions to improve presentation and clarity.

1) Dependence of diversity measures on thresholds. We suggest adding a graph that shows the fraction of variable sites at first, second, and third position of codons above frequency x as a function of the threshold x. The threshold above which biological variation starts dominating over technical variation is usually clearly visible in such a graph. Furthermore, a discussion of the effect on thresholds on the conclusions (e.g. 0.72 variants per sample on average) and the expected number of false positives is necessary. The dependence of within-sample variation on Ct values should also be discussed.

2) Please add a detailed description of the sequencing methods and replication procedure.

3) The work would benefit from a better contextualization in the existing literature of RNA virus within-host variation and mutational processes. The authors have reinvented a fair bit of existing knowledge (several suggestions and pointers can be found in the specific comments below).

4) This work has the potential to serve as a reference resource of SARS-CoV-2 within-host variation and reuse of these data would be greatly facilitated by intermediate files, for example, tabular files for each sample listing the number of times each nucleotide is observed at each position of the genome.

5) Please consider the numerous suggestions to improve presentation and clarity.

Reviewer #1 (Recommendations for the authors):

The authors seem unaware of much of the literature on RNA intra-host sequencing and repeatedly reinvent the wheel. In fact, they often make reference to cancer, bacterial, or DNA virus genomics when placement in the literature of RNA virus genomics would be much more appropriate. A detailed discussion of mutational biases of SARS-CoV-2 and the potential RNA editing enzymes involved can be found here:

https://msphere.asm.org/content/5/3/e00408-20

In contrast, mutational mechanisms relevant in cancer are unlikely relevant here (nuclear dsDNA genome vs cytoplasmic RNA).

The quantification of biases and errors in estimates of within-host variation from replicate samples was for example developed pretty much along the same lines in

https://academic.oup.com/ve/article/3/2/vex030/4629376

http://www.sciencedirect.com/science/article/pii/S0168170216304221

https://academic.oup.com/ve/article/5/1/vey041/5304643

https://jvi.asm.org/content/90/15/6884

Within-host diversity is commonly used to estimate time since infection in HIV, both in acute and chronic infection.

https://link.springer.com/article/10.1186/1471-2105-11-532

https://academic.oup.com/cid/article/52/4/532/380068

http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005775

The observations with respect to within-host purifying selection are also very similar to what is observed in other RNA viruses (HIV, influenza virus, enteroviruses). See for example here:

https://academic.oup.com/ve/article/6/1/veaa010/5739536?login=true

Similarly, co/super-infection has been described in RNA viruses.

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC136598/

https://academic.oup.com/ve/article/5/1/vez007/5479511

This is not to detract from the work the authors have done here, it just reads extremely odd when the authors describe a pattern in the data and then go on to explain how this is reminiscent of work done in bacterial genomics or cancer when it is in fact a common pattern in RNA viruses.

Reviewer #3 (Recommendations for the authors):

None of this precludes publication in eLife. This is a really well done study of an important topic.

1. Figure 1A and 1B shows only a random subset of 100 samples, which is far less than half of the dataset. This figure should be revised to include all of the samples (perhaps histograms of mutations per sample). This should also be broken down to show the number of within-host variants per sample by SNV, insertion/deletion, etc. Modifying this figure would showcase the data better and allow easier comparison to other studies.

2. With respect to variant calling. Again, the authors really should be commended for doing replicate samples. However, they should acknowledge that this limits, but does not remove, false positive variant calls (although it gets one to the level where truth can be hard to come by). From the manuscript it appears that they called variants in replicates down to a frequency of 0.5%. They acknowledge reduced sensitivity. But specificity is not perfect. It is worth looking at McCrone and Lauring JVI 2016, which also used DeepSNV and replicate samples. In this benchmarking study, the specificity at 0.5% frequency threshold was 99.99%. In a genome the size of influenza, this amounted to 3 false positives per sample (even with replicates). For a genome twice the size (SARS-CoV-2), one might expect up to 6 false positive variants. I don't expect the authors to reanalyze the data. But it is important that they discuss the potential that their summary statistics on number of single nucleotide variants per sample or per day could be inflated. Again, nothing wrong with that, but it helps to put this work in context with other data out there.

3. Overall, the variant calling is not clearly described – some in results, some in methods. But lots of details missing.

4. Others have shown (see Grubaugh Genome Biology, for example) that SNV within primer binding sites can cause aberrant frequency estimates. This can be an issue with large amplicon sets like the ARTIC protocol. It isn't clear how this was handled in this paper. Again, I don't think it changes the conclusions substantially.

5. I suspect that they are correct on the mutational/strand bias question and this analysis is fascinating to me. However, there are some important caveats. RT has its own mutational bias. While replicates should reduce the tendency for this to be a problem, it can impact this sort of analysis even in a limited way. The number of strands (plus vs. minus) could also play a role – but experimentally in terms of the degree to which subgenomic messages are sampled in their data. It might be helpful to see if the mutational bias is uniform across the genome or clustered in regions where subgenomic messages could be playing a role. Finally, there is evidence for asymmetric mutational bias in polymerases (see Pauly et al., eLife 2017, which also goes into RT error as well).

6. Is there a relationship between the diagnostic Ct value and the number of within-host variants per sample? This would be a helpful complement to the overdispersion analysis, which is slightly more abstracted. For example, it looks like over half of their samples have Ct > 24, which is where there is a significant up-tick in overdispersion. How will this affect their data on number variants identified and the number per day?

7. The analysis of paired samples is interesting, but the data is limited as the authors note. I am not convinced that there is a real increase in variants per sample over time. The difference in called variants across samples collected on the same day is quite large, in many cases larger than the increase in mutation abundance in the later timepoints. It is equally possible that there are limitations in variant calling sensitivity/specificity. What is the difference in Ct values for these paired samples?

8. The finding of recurrent mutations is nicely done. Several comments related to this:

a. It is interesting that D614G was seen multiple times. Do other recurrent within-host mutations identified in the paper reach high frequencies in GISAID data?

b. There are some sites that are prone to systematic errors, such as 11083 near a poly-U tract. How was this position handed in the analysis?

c. It would be good to have a table with each recurrent mutation and its counts.

d. Is it possible that any of these mutations are from cross-contamination? Are there fixed mutations at the same sites in other samples sequenced in the same batch? Or rather, how were replicates handled to minimize cross contamination?

e. I appreciate the difficulties in displaying multidimensional data. However, in Figure 5B, it is difficult to see the individual lines and pick out any patterns. There are too many overlapping lines. I would encourage trying other ways to display this figure, especially because it represents a central point of the paper.

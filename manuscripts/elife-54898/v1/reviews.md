# Peer review - Round 1

Editors:
- Christian R Landry, Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54898.sa1](https://doi.org/10.7554/eLife.54898.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

DNA replication errors are one of the engines of evolution. However, how errors accumulate at the different steps of the central dogma of molecular biology has received limited attention. Investigating how errors in transcription and translation affect cell biology first requires that we measure their rates and that we examine how they affect various species. In this study, the authors use a recently developed technology to measure transcription error rates in four species of bacteria. Their results reveal that transcription error rates are higher than mutation rates, that many of these errors lead to amino acid changes if translated and that there may be a mechanism in prokaryotes for the quality control of mRNAs. These results open new research avenues on how cells may control the propagation of errors along the steps of the central dogma and why such error rates may be tolerated by evolution.

Decision letter after peer review:

Thank you for submitting your work entitled "Universally high transcript error rates in bacteria" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Joanna Masel (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. But please keep in mind that a substantially changed version could be re-submitted as a new paper.

The reviewers agree that the questions addressed are interesting and important and consider that it is possible to improve the manuscript so that it meets their criticisms. They found particularly interesting the proposed mechanism based on premature termination but found that it was not fully supported by the analyses and may require actual lab experiments. They also identified several issues with the presentation of the data and some of the analyses. In light of this, we cannot consider the manuscript further under its present form. Their complete comments appear below.

Reviewer #1:

The manuscript submitted by Li and Lynch is interested in transcript error rates in bacteria, which were already known to be orders of magnitude more frequent than replication errors. The authors developed a slightly modified version of the previously published CirSeq approach, which produces tandem copies of transcribed fragments from circularized RNA molecules, to allow a more accurate detection of errors on a genome-wide scale. The authors used this method to quantify mutations in transcripts from four representative bacteria, and showed evidence suggesting that the M. florum RNA polymerase is error-prone, with a strong G to A substitution bias compared to the other bacteria. The authors showed data suggesting that nonsense mutations tend to accumulate at the 3' end of transcripts and proposed a model to explain how transcripts containing a premature termination codon could be recognized and degraded by the cell.

Overall, I found the topic interesting but the results rely on a single type of evidence (CirSeq) and are mostly descriptive. Additional experiments would be required in my opinion to fully support the model proposed by the authors. For example, it would be interesting to introduce a premature termination codon at different positions in a reporter gene such as lacZ and evaluate if such mutated transcripts have a shorter half-life compared to the wild-type. I am still debating whether this is essential for this manuscript or not. I also noted a few suggestions or elements that should be clarified:

- It would be useful for readers to include a more detailed description of CirSeq as the manuscript heavily depends on this technique. The manuscript was mentioning reference work but a short explanation would help.

- The average mutation rate of reverse transcriptase is ~1E-4. Since this rate is relatively high, the authors only considered mutations with at least two tandem repetitions in the CirSeq data. Were the reverse transcription errors observed by Gout et al., (2013) evenly distributed across the transcripts (hotspots), and were certain mutations types more predominant than others? If such biases exist, would it still be possible to confidently discriminate between reverse transcription errors versus transcription errors? Can the authors comment on that?

- In Figure 4 and Figure S1 to Figure S3, how were the replicates processed? Were they combined before the sliding window analysis or after? Would it be relevant to show the error frequency calculated for each replicate to see the inter-replicate variability? The Pearson's correlations coefficients should also be present on the figures, especially for Figure S1 as this comparison is very important for the conclusions. My first impression was that Pearson correlation coefficient from Figure S1 (all transcript errors) would be similar to those reported for Figure 4 (nonsense errors) but the comparison is not possible in this version of the manuscript. Is there a reason to not show the Pearson's correlation coefficient on Figure S1 but show them in Figure 4 and Figure S2- Figure S3? From what I understand in subsection “Biased distribution of nonsense errors in RNA transcripts”, the correlation coefficients calculated on data presented in Figure S1 should not be significant. Is that the case?

Reviewer #2:

The manuscript by Li and Lynch reports the mutational spectrum of transcription in 4 bacterial species. The objective, results and discussion are clear and easy to read. However, I found that the methodological descriptions often lack important technicalities that are needed (at least to me) to fully appreciate what the authors have done exactly. I will first raise few general points and then provide a list of missing methodological pieces of info. I have no expertise in the molecular biology part, so I won't comment on it.

- Subsection “A global view of the transcript error distribution”: If the authors used a Bonferroni correction for multiple testing, they should not observe 5% of false positives, but expect 0.05 false positives, that is well below 1. Typically they should observe 0 positive if H0 is correct. If they really observe 5%-ish (as it is implied in the text), they do have a lot of significant genes for which transcripts are enriched in mutations.

- Subsection “Biased distribution of nonsense errors in RNA transcripts”: the authors report an overrepresentation of non-sense mutations near the 3' of the transcript. This is interpreted as a sign of a potential NMD in bacteria. I indeed think this is indeed a possibility. Alternatively, it could also be the case that simply there are more mutations in the 3' end of transcript in general. What is the pattern for missense and synonymous mutations regarding their localization in the genes?

- Subsection “Biased distribution of nonsense errors in RNA transcripts”: I am not sure of what the added value of this measure of relative gene length. Can you get rid of this paragraph and plot?

- Did the authors attempted to look at indels? I think 'long enough' SSRs will also present SSRs copy number variations.

- for Abstract/Introduction: errors can also accumulate without replication nor transcription (see some recent papers on non-replicative/quiescent errors)

As mentioned earlier, many methodological pieces of information are missing. Here is a list of some of them. Consider that the readers must have *everything* to understand and eventually redo the experiments. In this current version, most treatments are opaque.

- Subsection “A global view of the transcript error distribution”: how did you normalized to "the same level"?

- Subsection “Characterization of transcript errors”: sure, ~2/3 of mutations are non-synonymous. So this does not come as a surprise.

- Subsection “Characterization of transcript errors”: "close to" means "close to significance"?

- Subsection “Data analysis”. Can you provide insights on what is the Lou et al., method? What is the autocorrelation method? Where is the python code available, so readers can have a chance to understand what you did? What is the Bayesian approach you mentioned using? What parameters of BWA did you used?

- Subsection “Strategies to distinguish transcript errors from other types of errors”: what is the equation? (you suggested simplifying by \mu g, but I don't see an equation)?

- Subsection “To calculate the expected percentages of transcript errors with different effects”: I suspect these are not probabilities but counts turned into frequencies, right? So at best, probabilities estimates. \mu_i are the relative mutation rates? More generally, I am not sure what did you use this whole calculation (in this paragraph) for?

- Figure 3 legend: what are 'conditional' error rates?

- Table1: How exactly did you compute your p-values? Did you take the spectrum into account?

- Figure 4: Why do you have the x-axis in reverse order? How did you normalize in 0-1.

In conclusion, I believe this manuscript has potential but should be revised with great care before becoming a decent published article.

Reviewer #3:This manuscript measures the single nucleotide transcription error rate and spectrum in four bacterial species. The primary findings are that E. coli errors are an order of magnitude less common than previously reported by Traverse and Ochman, that M. florum has a strikingly high G->A substitution bias, and that nonsense errors are depleted toward the 3' end of mRNA in a manner compatible with previously hypothesized NMD-like quality control in prokaryotes. Overall, a potential obstacle to publication in ELife is the incremental nature of these findings – the methods are not greatly advanced from earlier work including from the same group, this is not the first evidence for NMD-like quality control, and there is speculation about but not proof for the reasons for the high G->A bias and the discrepancy with previous E. coli measurements. I have a number of concerns, especially about the statistics, but correcting them is unlikely to reverse the major findings.

Probably the biggest issue is the contrast between Figure 4 and Figure S3, used to help infer the mechanism of action of the NMD-like system. Frequencies are a kind of binned data, and it is inappropriate to report correlation coefficients from binned data: see eg https://statmodeling.stat.columbia.edu/2016/06/17/29400/ or https://serialmentor.com/blog/2013/8/18/common-errors-in-statistical-analyses for discussions of this point. It is definitely not appropriate to claim that the Figure 4 model is better than the Figure S3 model (subsection “Biased distribution of nonsense errors in RNA transcripts”) because the correlation coefficients are larger, especially because the binning is clearly different in the two cases, eg. with far more zeros in Figure S3.

For these and all similar figures, there should be error bars on each dot from sampling error: for a binomial the error is sqrt(p*(1-p)/n). I was unable to figure out what exactly the normalization to scale the y-axis between 0 to 1 entailed – the fact that no code was made available (despite the ELife reporting form instructions to "Include code used for data analysis") meant that I couldn't compensate for thinly described methods. I see in any case no justification for normalization; it would be better to just give the actual numbers on the y-axis, while keeping the "zoom" the same for visualization purposes.

The best statistical approach is generally to work with the raw data, which in this case is a vast dataset of 0s (no error) and 1s (error). The number of (rare) errors meeting given criteria follows a Poisson distribution, and a generalized linear model can be used to model this error function. This is what we did for transcription errors in https://www.biorxiv.org/content/10.1101/554329v1, and it leads to vastly greater power to discern the kinds of trends hypothesized in Figure 4 and Figure S3. I realize that, as well as some conflict in asking for use and thus citation of my own work, there may be concerns citing a preprint, but the manuscript is now accepted pending minor revisions in GBE, and citable as such. I would really like to know eg whether M. florum really does have a different shape to E. coli in Figure 4 as it appears to, and more sophisticated statistical models are required to answer questions of this sort. Our accepted manuscript provides such models, with code fully available on github.

Our preprint re-analyzes the data of Traverse and Ochman, and finds that the (non-C->U) error rate depends on protein abundance. The Discussion section is the only place in the paper that attempts to say why the currently observed non-C->U error rate is an order of magnitude lower than that previously observed by Traverse and Ochman, attributing all the discrepancy, especially but not limited to cytosine deamination, to RNA damage during library preparation by Traverse and Ochman. This is problematic in the light of our finding of systematic differences that are not expected to be caused by library preparation problems. I don't know why the non-C->U error rates are so different between the studies either, but it clearly isn't all cytosine deamination, nor all library preparation, and it would be useful to acknowledge this puzzle and comment on other possibilities, e.g. differences in strain or experimental condition.

Note that the per-gene method to find outliers described in subsection “A global view of the transcript error distribution” is much lower powered than our test for dependence on protein abundance, and so in no way rules out the variation among genes that we discovered. And if the aim is to detect mutations or programmed errors, it is better to do so per-site than per-gene, as we also did to also find that such problems were rare.

In general, the statistics used in this manuscript assume that sampling error is negligible and that all variance is therefore attributed to biological replication. This underlies the use of t-tests and paired t-tests throughout. However, in tables like Supplementary file 5 and Supplementary file 6, neither error bars nor denominator is given, so I am unable to verify that sqrt(p*(1-p)/n) is negligible. If it is not negligible, then all these t-tests should be weighted rather than the current use of unweighted tests, or better still, a more advanced generalized linear model with a Poisson error term (see above) that simultaneously accounts for all sources of variance should be used instead of t-tests. The problems with the statistical tests used primarily create lower power, and so the positive findings should all hold, but more problematic is that the supplementary data files lack the information needed to allow future reanalysis of the data using better methods.

Another statistical problem is in calculating expected percentages (subsection “To calculate the expected percentages of transcript errors with different effects”). The equation used assumes that while the error rates of the 3 sites within the codon might be different, every codon has an equal error rate. The much more logical alternative would be to assume site-specific error rates that do not depend on which codon the site is found in. If our finding that error rates depend on protein abundance is also true, this will contribute to misleading results even after this correction is made. We found that the difference between error rates at synonymous vs. non-synonymous sites was entirely attributable to the dependence of codon bias strength on protein abundance, i.e. that variation in error rate was at the gene level not the codon level.

Figure 2 legend refers to the analysis only of genes with detected transcript errors. This would seem to create a variety of ascertainment biases, inflating the error rate overall as zeros are neglected, and preferentially neglecting potentially large numbers of genes each of low expression.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Universally high transcript error rates in bacteria" for consideration by eLife. Your article has been reviewed by Patricia Wittkopp as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Joanna Masel (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Li and Lynch measure the rate of transcription errors in a few prokaryotes. This is a revised version of a previous manuscript. The reviewers appreciate the importance of the work and the changes that have been made to the initial version. However, there are still some concerns about the statistical analyses and interpretation of the data. The comments are summarized below.

Essential revisions:

Data analysis and interpretation:

1) They uncovered almost the full spectrum of transcription errors, but somehow omitting indel errors from their data set. As is, this work will serve as a method reference for people interested in transcription errors. Based on their spectrum analysis, the authors speculate about different mechanisms by which these errors can be made. In order to be complete, the authors should analyze and report indels from their existing data.

2) Concerning the model to explain the biased distribution of nonsense errors in mRNA, they proposed an NMD mechanism no yet characterized in bacteria, but this can easily be explained by transcription polarity described first by Morse and Yanofsky, (1969).

3) In order to make the sequencing method user-friendly, I would strongly suggest that the authors include a flowchart for the analysis of the sequencing data as they have done for the technical concept in Figure 1—figure supplement 1.

Statistical analyses:

4) While claims based on comparing the magnitudes of correlation coefficients of different binned data sets has now been removed, correlation coefficients for data that is not just binned (frequency data), but also non-independent (sliding windows) continue to be reported in Figure 4, Figure S2, and Figure S3. Corresponding regression models on these non-independent sliding window datapoints are inappropriately used to generate p-values. An alternative and somewhat less flawed approach is given only in the response to reviews document and not in the manuscript itself. This is presented as being the method of Meer et al., "with minor modifications", although they are not that minor, as they sacrifice the main advantage of that method. A good statistical model should have a good model of the error function. Count data has a binomial error function, well approximated as a Poisson. The advantage of the method of Meer et al., is that it exactly models this Poisson, but the method is dismissed in the response to reviews because it explicitly accounts for the fact that the raw count data depends on the number of reads, as though this were a bad thing. The alternative presented in the response to reviews does avoid the non-independence problem of the sliding window, but it still assumes homoscedasticity with respect to #errors/#reads, an assumption that is violated in practice given many more reads at some sites than others. If the authors want to model Equation (1) instead of Equation (2) (as numbered in the response to reviews), I would find this acceptable if and only if they (a) use a weighted regression to account for the known heteroscedasticity (ie at least model the magnitude of the error even if they don't model its shape), and (b) place this analysis in the manuscript itself as a replacement for doing a regression on the output of non-independent sliding-window-bins. The sliding window is perfectly appropriate and indeed very helpful as a visualization of the data, but inappropriate for the fitting and testing of statistical models.

5) I take issue with the claim in subsection “A global view of the transcript error distribution” that transcript errors are randomly distributed across genes. After a Bonferroni correction for the number of genes, the manuscript has very little power with which to make such a claim of evidence of absence. What is more, Meer et al., showed (using a different E. coli dataset) that the error rate does depend on the strength of selection on the gene in question, as assessed by its protein abundance. This analysis had much higher power than the current study, firstly because there was only one degree of freedom and hence no need for a radical Bonferroni correction, and secondly because explicit modeling of the error function as described above will generally increase power. Given that (uncited) evidence that contradicts the manuscript's claim for randomness has already been published, and the lower power of the current manuscript's basis for making this claim, a claim of randomness should not be made unless the authors are able to apply the same or similarly high-powered method and directly show contradictory results. Should the previously published claim non-randomness be supported, this would have implications for the authors' model of randomly generated transcript error, eg subsection “Characterization of transcript errors”. In this passage too, the statistics are problematic. Observed and expected "data" are compared using a paired t-test, as though the expectations were themselves data with error magnitudes homoscedastic with those of the observed data.

6) I am also confused by the bootstrapped standard deviation in Figure 4, Figure S2, and Figure S3. In Figure 4, why bootstrap rather than use the known formula for a binomial? In Figure S2 and Figure S3, why bootstrap only the numerator and not the denominator of the quantity whose error is being assessed?

7) I still fear that the casual reader will take away from the Discussion section that differences between the two studies in error rates other than C->U are trivial in magnitude, which is not the case.

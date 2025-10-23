# Peer review - Round 1

Editors:
- Simon Creer, https://ror.org/006jb1a24 Bangor University Bangor United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78521.sa0](https://doi.org/10.7554/eLife.78521.sa0)

This landmark study reveals novel temporal arthropod biodiversity insights that can be leveraged from environmental DNA traces, that have been cryopreserved on leaf tissue as part of a long-term monitoring scheme. The strength of the evidence underlying the major conclusions is convincing and limitations in the quantitative aspects of the data synthesis are acknowledged appropriately. The work will be of interest to a breadth of ecological practitioners.


---

# Peer review - Round 1

Editors:
- Simon Creer, https://ror.org/006jb1a24 Bangor University Bangor United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78521.sa1](https://doi.org/10.7554/eLife.78521.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Environmental DNA from archived leaves reveals widespread temporal turnover and biotic homogenization in forest arthropod communities" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Rafael Valentin (Reviewer #1); Thomas Gilbert (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

My colleagues have performed an excellent assessment of the breakthroughs and importance of this novel study and I will not paraphrase their valuable insights and feedback but will also join in the discussion.

It can be frequently observed that low diversity environmental DNA samples can be under sequenced using high throughput sequencing, whereas high diversity samples normally yield higher levels of sequence rates. By rarefying their analysis to 5000 reads (an approach that is increasingly not used, c.f. the McMurdy and Holmes debate https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003531), there is a risk that low diversity samples may be over-sampled and high diversity samples may be under-sampled. I appreciate that 5000 data points are likely to be appropriate when capturing leaf-based arthropod communities, but further evidence of the rarefaction, per sample coverage and rationale, would be valuable.

One of the conclusions of the research, according to qPCR of the 18S ribosomal DNA marker, is that (cellular) biomass appears to have decreased over time; a narrative that is coherent amongst the declining population trends that prevail in contemporary ecology. The challenge here is the use of the degenerate 18S marker, which is not linked to the interspecific copy number variation that will be prevalent amongst the different taxa in the study (e.g. taxon 1, 5 copies; taxon 2, 15 copies; taxon x, y copies…). A potentially equally plausible explanation for the declining copy number is that the copy number of the homogenised communities is lower than the older, non-homogenised communities. Without exhaustive per taxon calibration, the inability to compare interspecific abundance between taxa is one of the downsides of any metabarcoding study, that is focused on multicopy markers that differ either in copy number, or the amount of tandem repeats, as is the case with mitochondrial and nuclear ribosomal markers respectively. I suggest therefore that the investigators devise an additional test to measure, e.g., the level of association between qPCR copy number, time, and the level of homogenization (e.g. Jaccard dissimilarity) simultaneously in order to address this concern head-on.

In addition to my insights above, I will highlight the revisions that have been highlighted as essential amongst the review panel.

Essential revisions:

1) The biomass assay – Explore whether the decrease in qPCR (aka here as biomass) values is associated with homogenization, time, or other identifiable factors simultaneously (e.g. leaf characteristics) and discuss the results in an objective fashion.

2) The data have been rarefied to 5000 reads – is this enough and can the team clearly demonstrate their baseline data strategy? Would anything change by using either proportional data or using read depth as an offset on the total dataset (e.g. https://www.nature.com/articles/s42003-020-01562-4)?

3) Clarity on the nature of controls, decontamination procedures, and how these guided data filtering in the metabarcoding study.

4) Revisit the simplistic modelling and devise appropriate analyses that will take into consideration non-linear trends and different factors where appropriate.

5) Justify the replicability/robustness of the qPCR strategy.

6) Justify OTU picking strategy.

I would also invite the authors to address all the reviewer's comments via standard rebuttal letter and submission of track changed version of the original submitted text where possible. Where reviewers have different opinions, please discuss clearly your views in the context of your study and the evidence presented (cf. discussion of read numbers, qPCR, and abundance).

Reviewer #1 (Recommendations for the authors):

While reading through the methods I was at first deeply concerned that PCR errors remained within the zOTU table, but only later (in the statistical analysis section) did I see that OTUs with three or fewer reads were removed from the dataset. This should be moved up with the rest of the bioinformatic information to make it clear earlier and alleviate that concern.

I saw no mention of methods that would filter out reads, or samples, due to contamination levels. There is always some level of contamination that takes place in eDNA metabarcoding, and addressing this is paramount. Filtering out contaminants can range from removing contaminant reads in technical replicates to removing technical replicates entirely. This extends to the decision to use just two technical replicates for the metabarcoding portion of the study. While not bad, should technical replicates be filtered out it leaves just a single technical replicate to represent the sample, which isn't sufficient?

On line 185 only 413 OTUs were said to be used to assess temporal changes. Why were just these OTUs selected from the larger dataset? This should be explained and justified.

Were beads for the tissuelyzer and cryomil reused? If so, how were they decontaminated to ensure no contamination of subsequent samples took place? If they were not reused this should be made clear in the text.

What was the justification for a 3% OTU radius? Was this a precedent set from another paper, or was it a random selection? More detail here is needed.

Reviewer #2 (Recommendations for the authors):

I elaborate on my concerns regarding the sequence and statistical analyses below.

One of my greatest concerns is in the statistical analyses of the temporal trend. In most cases, the authors used linear models (LM) to test whether there is a temporal trend (i.e., increase or decrease). This is inappropriate because empirical time series often contain temporal autocorrelation structures and because the application of LM to such time series may often result in the false-positive detection of the trend. This means that LM can often detect a "significant" trend even in a random walk time series. This is a well-known issue, and the authors should apply a more appropriate statistical method, e.g., the autocorrelation model, state-space modeling, or some other methods, to judge whether there is a temporal trend.

Another concern is the use of read abundance as an explained variable in the statistical models. In L452-454, the authors claimed that the DNA copy numbers may be a proxy of biomass. I agree with this statement. However, sequence read abundance is not the DNA copy numbers and cannot be a proxy of abundance in most cases. If I understood correctly, the authors rarefied the sequence reads to 5000 reads for each sample, and the read abundance in the statistical model seems to be the relative abundance (e.g., if an OTU produced 500 reads in a sample, the relative abundance of the OTU in the sample is 10%). The authors quantified 18S DNA copy numbers of arthropods, so multiplying the relative abundance by the total 18S DNA copy numbers may produce a better proxy of the abundance of arthropods. I would recommend the authors reconsider the read abundance issue carefully.

Reviewer #3 (Recommendations for the authors):

Line 91. 312 ESB samples. Perhaps expand here on distribution through time etc? Could be part of Figure 1?

Line 125+ – stability of arthropod DNA comment. I'm actually surprised there is no higher diversity in the 8-year RT stored samples, as a result of post-mortem modifications to the DNA. Having said that does the PCR strategy negate that? If yes maybe worth stating this clearly. Actually in general given how critical the assumption that any zOTUs used represent true biological sequence variation (as opposed to PCR error, sequencing error, post mortem DNA damage) I advise the authors to early in the paper make it clear why they believe their zOTU estimates to be accurate.

Line 129. rDNA is typically used for many things. Ribosomal DNA. recombinant DNA. Even relative DNA. Maybe for clarity here state 'information on relative arthropod 18s rDNA copy' then there is no uncertainty.

Figure 5F's label is confusing (e.g. Does < 2020 mean 2010-2020 or all years before 2020 etc?). I suspect the former but that's not how it reads as written in the figure.

Can the authors elaborate on when the leaves were collected in the year? In line 287 the authors state it was the same time point every year. How is that shaped by the time of year the leaves come out every year? (Which must fluctuate a lot with annual weather variation). Also in line 257, the authors state the leaves represent a 'fairly broad phenological window'. Can this be elaborated on?

Line 287/288. It seems odd to write 'a defined amount' of both leaf and number of trees, and then give values prefixed by '>'. And then say 'defined number of branches from each tree' but then not give a value. I think I know what the intended meaning is, but perhaps consider rewording this sentence! Also, I assume the exact numbers are somewhere – maybe refer to where at this point?

Methods in general, it took me a long time to work out exactly how the samples were collected and processed, and I'm still not sure. If I understand it correct – leaves were originally picked from trees immediately into liquid nitrogen, and then shortly after ground to a powder? Thus all happening years/decades ago? If correct please consider re-reading the text assuming you know nothing about the history and add any small clarifications that might be needed so the reader can immediately jump to this conclusion. If however, I misunderstand…then again the text needs clarification.

Line 295 I assume the cryomill was somehow decontaminated between sample batches? Please clarify how.

Ca Line 365. Please state clearly if extraction replicates were made on the samples used in the full experiment, (or not). It's not clear to me as written now. I can see they were used in the sample mass trial and perhaps given the replicate dissimilarity results were ok for the PCR and extraction replicate the decision was taken to not do replicates on the large scale? If so please state it clearly.

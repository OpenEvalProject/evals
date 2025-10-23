# Peer review - Round 1

Editors:
- Peter Turnbaugh, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63642.sa1](https://doi.org/10.7554/eLife.63642.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Oxalate is critical for kidney stones yet the bacteria responsible for its metabolism in humans remain poorly understood. Herein, the authors use a multi-disciplinary approach to study the abundance and expression of genes for human gut bacterial oxalate metabolism in healthy subjects and patients with inflammatory bowel disease. They go on to show that Oxalobacter formigenes significantly alters oxalate levels in mice. These analyses provide a critical step towards a more comprehensive view of oxalate metabolism and its role in health and disease.

Decision letter after peer review:

Thank you for submitting your article "Microbial contributions to oxalate metabolism in health and disease" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individual involved in review of your submission have agreed to reveal their identity: Eric Brown (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Liu and colleagues present a series of finding related to gut bacterial oxalate metabolism. First, they curate a set of previously described proteins and generate a reference database of homologs based upon Interpro annotations. Then, they re-analyze previously published meta-genomes and transcriptomes to find hits to these reference genes in the gut microbiomes of healthy and IBD subjects. Surprisingly, they find an inverse association between oxalate levels and the total transcripts of bacterial oxalate degradation genes. They also include data showing that Oxalobacter formigenes (a model oxalate degrading bacterium) impacts oxalate in mice. These analyses are a good example of how the microbiome field as a whole can utilize complex multi-omic datasets to help answer specific questions of clinical importance. However, there are multiple limitations and points which need to be addressed prior to publication.

Essential revisions

1. The claim that O. formigenes is the dominant oxalate degrading species is not well supported by any of the current data. The sequence analysis is based on a presumably partial knowledge of the full scope of enzymes capable of this activity, so it remains unclear if alternative species or pathways are important to consider. The mouse experiment is used as a "validation" but only shows that this species is sufficient to impact oxalate not that it is necessary in humans. A valuable first step would be to colonize germ-free mice with O. formigenes along with multiple other oxalate degraders, then perform leave-one-out experiments to test which species have a marked impact on oxalate levels when removed.

2. The approaches used to assign genes and species are not state-of-the-art and may not be entirely reliable. I'd suggest trying ShortBRED (Huttenhower lab) or a related tool to quantify the protein families of interest. FishTaco and BURRITO (Borenstein lab) could be used to help link taxonomy to function. This is an important point since it relates to the claim that O. formigenes is the source of most transcripts. Furthermore, it's unclear if these genes are horizontally transferred (which could be assessed by comparing gene and species trees). If so, simple read mapping could assign genes to the wrong genomes. Ignoring these other tools, the validation shown in Figure S3 doesn't make much sense to me. The threshold of 90% misses many of the intraspecies comparisons. I'm also concerned that Oxalobacter, the focus of this work, only has a handful of representative genes, which will make it difficult to reliably assign reads to this genus let alone to O. formigenes specifically.

3. Some attempt needs to be made to experimentally address the counter-intuitive observation that higher substrate (oxalate) is associated with lower expression, which runs counter to how most bacterial genes are regulated. What accounts for the downregulation? Is this related at all to the environment within the IBD gut?

4. The way the oxalate levels in the feces are presented is problematic. In the manuscript, the authors make multiple mentions the observed abundance of oxalate is a "fecal concentration of oxalate" when in fact it is the relative abundance of oxalate as measured by LC-MS. These data are not measuring concentration but relative abundance, which can be influenced by other non-biological factors such as how well the metabolite is ionized in each sample by LC-MS. Authors should not these are relative abundance calculations and not concentrations (for example Line 13 describing Figure 4A). Furthermore, the authors should indicate whether the samples were normalized between cohorts and how they were, and whether the relative abundance measurement is correct for within sample differences (% abundance of all observed metabolites) or a raw abundance? For example, the large difference between IBD and healthy stool could lead to less total metabolites being extracted and ionized thus data normalization between samples may actually increase the correlations you are seeing between oxalate and oxalate-degrading enzyme expression by meta-transcriptomics.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Microbial genetic and transcriptional contributions to oxalate degradation by the gut microbiota in health and disease" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Peter Turnbaugh as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Wendy Garrett as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. In Figure 4 the raw values in the y-axis when reporting oxalate relative abundance are unclear which units? Are they actually negative. The figure legends in general should include more specific information for the metabolomic data so it is easier to interpret.

2. The authors still refer to "oxalate concentrations" in the figure legend for figure 4.

3. It is unclear why the calprotectin cut-off was 50ug/mL please cite literature or a reason for using this value. It seems like there is in fact a trend with inflammation potentially.

4. Along that note Pearson analysis could show whether calprotectin levels correlate with Oxalobacter, something worth mentioning for the differences in abundance across IBD vs healthy controls and will be useful for the field if in fact this were to ever be utilized as a probiotic by others in the future.

5. More clarification is needed in the manuscript text on how comparing metagenomic analysis with metatranscriptomics can successfully pinpoint which taxa contribute to a disease pathway (in this case oxalate degradation). I still find this comparison confusing as a reader and potential pitfalls to this approach should be more clearly stated (sequencing depth as mentioned).

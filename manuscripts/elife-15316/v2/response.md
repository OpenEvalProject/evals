# Author response - Round 1

Authors:
- Aimee M Deaton
- Mariluz Gómez-Rodríguez
- Jakub Mieczkowski
- Michael Y Tolstorukov
- Sharmistha Kundu
- Ruslan I Sadreyev
- Lars ET Jansen
- Robert E Kingston ([ORCID: 0000-0003-3628-4335](https://orcid.org/0000-0003-3628-4335))

## Response text

DOI: [10.7554/eLife.15316.042](https://doi.org/10.7554/eLife.15316.042)

[Editors’ note: the author responses to the first round of peer review follow.]

Reviewer #1:

1) While the method is commendable my sense is that to have a high enough impact for eLife the manuscript really needs to emphasize novel findings from this method that we did not know already.

We respectfully dispute the statement concerning ‘novel findings’; while many in the chromatin field take as a given that regulatory regions such as enhancers will have high turnover, there is scant data on this point, and the data that exists is not particularly compelling. The previous work uses protein induction strategies that have time delays, lessening precision. In addition, the difference between super-enhancers and enhancers is novel, as is the extent to which turnover is increased over gene bodies upon differentiation. We have examined turnover during differentiation, which has not to our knowledge been previously studied, and find that enhancers show the most frequent changes in turnover. Enhancers are central and highly studied, these are key data on a key topic.

2) Why study only the replacement variant of H3. Comparison to H3.1 would have increased the impact of the work. It might also allow some measurements on the rate of turnover during the cell cycle.

We have the H3.1 data on enhancers, and had not included it in the initial version, as we do not have read depth to allow assessment of any other feature of the genome. (The reason H3.1 is difficult to study intensively right now is necessary read depth and attendant cost.) The data are noisy due to read depth even at enhancers. We now include these data (Figure 3—figure supplement 2) and it buttresses the H3.3 data.

3) Other H3 tags have been shown to interfere with modification of the histone. This study needs some general controls for the stability of the nucleosomes containing the tagged histone and for the presence of histone modifications on the tagged vs. endogenous histone.

Looking at modifications on the tagged histone is tough due to the low expression level, however we can see K4me3 on H3.3 and K27me3 on H3.1 and have included these data (Figure 1—figure supplement 2). All of our data speaks to the stability of the tagged histone on chromatin (where we are using it) as we find turnover numbers that span hours and that are concordant with previous estimates. For example, Kraushaar et al. find H3.3 incorporation to occur in a 3-24 hour time frame. This has been added to the text (Results section).

Reviewer #2:

Weaknesses: This study does not break new conceptual ground or add significantly to our present understanding of nucleosome dynamics linked with transcription and silencing. It has long been known from a number of studies that gene expression positively correlates with the occupancy of H3.3 in the regulatory regions (especially promoters and enhancers) and generally associates with high nucleosome dynamics.

See above for the rebuttal on novelty; again the data are scant and no one has rank ordered turnover in active genes vs. enhancers vs. super-enhancers previously and these are high impact issues.

Reviewer #3:

At first glance, the study seems interesting and relevant to the field of nucleosome regulation. However, there were several analytical steps that lacked appropriate details which significantly impaired the full interpretation of the analysis and conclusions. It is difficult to recommend for publication without additional details of the methodology to make an informed decision.

A more detailed description of how the spike-in control was used is critical. How was this spike-in used to normalize or control the data?

The spike-in is a control to verify that the proportion of sequencing reads resulting from pull-down of SNAP-tagged histones was consistent with the experimental data for each time point, one cannot normalize due to the nature of the experiment. We apologize for not having made this clear, and have expanded upon this in the text (subsection “Time-ChIP reports histone H3.3 turnover genome-wide”, second paragraph and Materials and methods).

The authors state that they achieved greater DNA recovery the closer to the pulse they collected chromatin which is expected and serves as a good internal control. However, if the genome-wide normalization is based on the relative chromatin enrichment, the TI calculation could merely be mirroring the increased DNA recovery and not, on any sites, actual turnover. Further details on how the data was specifically normalized would clarify this concern.

Although we used a spike in control (as described above) we did not perform any normalization of the sequencing data. Rather, we look at the relative number of reads for different genomic regions at each time point when assessing turnover. Thus these data are internally compared to each other; the turnover rates reflect that internal comparison. For example, high turnover regions such as enhancers will have fewer reads in later time points compared to regions with slower turnover and the TI calculation reflects this. We apologize for not making this clear initially and have expanded upon this in the text (subsection “Time-ChIP reports histone H3.3 turnover genome-wide”, fifth paragraph).

Additionally, it would be important to know the robustness of this TI calculation given alternative normalization approaches. For example, the authors show there is minimal turnover at silent genes. If this is expected to be a relative constant, how do their findings hold up if normalized to turnover at silent genes?

As discussed above the read counts are not normalized and we compare relative turnover rates between different genomic regions. By its nature, the TI metric is internally “normalized” across the genome as we look at turnover at silent sites as well as active regions, and the metric provides a direct comparison between these rates. The silenced regions, such as those occupied by Polycomb, have lower TI.

What is the rationale for the use of 1kb windows for the calculation of the TI index?

1kb was used as the bin size due to read depth, particularly when looking at regions with lower amounts of H3.3 and when examining H3.1 turnover. Enhancers can be done in smaller windows. We have added Figure 3—figure supplement 1 which shows turnover at enhancers and super-enhancers when TI is calculated using a 300bp bin size (subsection “Time-ChIP identifies regulatory regions in ESCs”, third paragraph).

The use of linear regression slopes as the TI index raises concerns that the authors are assuming a linear relationship in histone turnover. What about regions that experience little turnover for long periods followed by spurts of high turnover?

We examine large numbers of stably pluripotent or differentiated cultures, so do not expect complicated behavior in the regions examined. We agree that a non-linear analysis might well be needed if one is doing an acute response; we do not have data that could be used to test this supposition though.

How is the MACC calculated? There is insufficient information for the nature of this calculation, which is concerning since an entire section of the paper is based on this calculation. A reference to a submitted paper that was not provided is insufficient to judge the nature of the analysis and findings.

We apologize for this oversight, we had thought the paper would be published by the time of submission and should have made the information available. The paper is now published and is cited:

Mieczkowski et al. (2016). MNase titration reveals differences between nucleosome occupancy and chromatin accessibility. Nature communications 7, 11485.

[Editors’ note: the author responses to the re-review follow.]

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

[…]

1) While the Discussion does in fact mention that Zhao came to the same conclusion on enhancers and cites the right paper, it comes too late in the manuscript. Hence, the Abstract makes an inappropriate novelty claim regarding high H3.3 turnover at regions known to be involved in gene regulation. Since Zhao has already shown this then they should acknowledge it in the Abstract and Introduction, i.e., "As previously shown, we found high H3.3 turnover at active regulatory regions including enhancers. However, we also find that even higher turnover occurs at super-enhancers […]".

We have edited the Abstract (“High turnover was seen at enhancers, as observed previously”) and the Introduction (“In ESCs, consistent with previous work, we found high H3.3 turnover at active enhancers (Ha et al., 2014; Kraushaar et al., 2013)[…]”) to refer to both the Kraushaar and Ha papers from Zhao’s group.

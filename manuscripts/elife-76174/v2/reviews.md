# Peer review - Round 1

Editors:
- Joshua T Schiffer, https://ror.org/007ps6h72 Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76174.sa0](https://doi.org/10.7554/eLife.76174.sa0)

This paper provides an important novel methodology to understand the mode of spread of SARS-CoV-2 in schools given sparse data.


---

# Peer review - Round 1

Editors:
- Joshua T Schiffer, https://ror.org/007ps6h72 Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76174.sa1](https://doi.org/10.7554/eLife.76174.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "COVID-19 clusters in schools: frequency, size, and transmission rates from crowdsourced exposure reports" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Joshua T Schiffer as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

1) Please reconstruct how the comparison between the US and Canadian data is done in the paper. All 3 reviewers agreed that the US data likely is hampered by overrepresentation of large super spreader events, leading to biased and inaccurate projections of the over-dispersion distribution. Please weight the 3 reviewers' suggestion for clarifying the presentation of this data.

2) Please either remove the time to detection analysis or incorporate a method to account for the inherent high degree of stochasticity of this outcome.

3) Please define cluster more clearly.

4) Please provide a more complete discussion about the true value of q and how this might impact model conclusions.

Reviewer #1 (Recommendations for the authors):

– Figure 1: x-axis needs labels and ticks to denote quantity.

– Please remove "not all the news is good for children": this language is too casual.

– All figures: increases font size substantially please.

– Figure 2: Please add an actual correlation plot with rho coefficients and p-values to formalize what appears to be true by eye. This will be so helpful to demonstrate that the US data is insufficient for the model used in the paper (Pardon the slang but… garbage in, garbage out). The authors can then emphasize the point that appropriately thorough data is necessary to model crowd sourced data of this nature.

– Table 1: given overdispersion, the median, interquartile range and full range of cluster size would be more informative than just the mean. Please add percentages to schools with multiple clusters column.

– Keeping in mind that this is a generalist journal., it would be helpful to show theoretical distributions with varying values of k as a supplemental figure. This would provide valuable context for Figure 3 and how to interpret k (in addition to Figure 4 which is great).

– The assumption that q=0.75 should be cited, or better yet, acknowledged up front as uncertain. The sensitivity analysis with varying values of q should be emphasized more when q is introduced.

– Figure 3: would it be possible to show the median and mean on the x-axis?

– Figure 4: why not include all provinces in Canada?

– Figure 5 is a bit difficult to interpret except for the most statistical minded among us, and could be a supplement (both the v and β parameters) or not included at all.

– For all figures comparing US and Canada data, please normalize the y-axes so comparisons can be made by eye more easily.

– When T < τ, how is”mingling” implemented? Does the number of contacts switch with movement from “classroom to classroom”. This needs greater explanation.

– Figure 7 is interesting and one of the coolest parts of the paper but lacks sufficient detail. For reduced β, increased social distancing and bubbling, the distribution is impacted to various degrees but is the total number of cases lower? Is the variance in the distributions lower? Are these differences statistically significant?

– Figure 7: The selection of R=0.5 and R=5 seems perhaps too extreme. Most persisting variants have been associated with R~1 (0.8-1.2) whereas omicron was 3-5 fold higher, albeit probably lower overall in classrooms. I would suggest at least testing an intermediate set of R values. Maybe 1 and 3?

– Please mention the omicron variant in the discussion.

– The authors make the excellent point that the crowd sourcing method is cheaper and easier than contact tracing or phylogenetic approaches but should also mention that contact tracing would be a wonderful gold-standard to validate the accuracy of crowd sourcing in terms of identifying cluster size.

– Figure 8: this would be easier to interpret of the panels were square rather than rectangular.

Reviewer #2 (Recommendations for the authors):

The major concern with the presented analysis is the use of sparse and potentially biased data in the analysis. The authors use compiled reports of case cluster sizes in schools across a number of jurisdictions, but have no methodological means to correct for issues clearly present in the underlying data. For example, most schools in the US only report a single cluster in the dataset, which likely biases the US dataset in a number of significant ways. This is contrasted with Canadian data where almost all schools report multiple clusters. The figures showing incident cases in schools and the community recapitulates this point with the US data showing no clear relationship between schools and the community compared with the Canadian data that shows a clear relationship. In either the case where school clusters contribute to transmission in the community or clusters are simply a byproduct of community transmission, we would expect to see correlation between the incident cases. While the authors mention these limitations to their study, I believe these data issues may present an existential issue with the current analysis as it makes it nearly impossible to interpret the results (even though I admit that the authors are fairly careful in their own framing). For example, it will be natural to wonder why Florida's Rc is nearly 8 while Texas's is around 2, and I believe there is very limited to say about the situation without controlling for underlying issues in the data between the states. I would suggest that the authors consider major methodological changes that might address the potential biases in the analysis. Perhaps limiting the analysis solely to Canadian data could also solve this issue, though there are likely biases in the dataset to consider as well.

The paper focuses on describing characteristics of clusters of cases in schools, and the authors give some details on the number of clusters in their datasets, however we never get a proper definition of what is considered a cluster here. According to the text on pages 11 and 12 it seems that an assumption is that all secondary cases in a cluster are infected by the same seed case (directly or indirectly). However, the interpretation of the results generally consider it to be through the direct route, even though public health policies would diverge significantly. For example a cluster that was infected outside of the school environment but were detected in school (imagine a group of close friends) would be counted in the analysis for Rc which ultimately filters to an understanding of how mitigation measures in school could control outbreaks. Alternatively, a cluster of multiple generations sputtering along might be given a large Rc when the actual R_eff for transmission might be below or close to 1.

The cluster definition is extra important, because it also impacts the estimate of the transmission rate. The transmission rate estimation assumes all transmission is happening within schools and in a single generation. In cases where there is actually a chain of transmission, or when transmission is happening outside of the school setting the formula used to calculate β does not hold. The authors partially acknowledge this by restricting the analysis to Canadian reports, but I think it should be more explicitly discussed in the manuscript either through an attempt to handle the complexity mathematically or with a larger discussion of the interpretation of the results.

Finally, the authors use an ascertainment q=0.75, which seems high, at least for the United States reports. For the US, the CDC estimates 1 in 4 infections were reported for a period covering the authors dataset, and detection is even less likely in children who are more likely to be asymptomatic (e.g. Davies et al.). The authors mention they used an alternate model of ascertainment and running a sensitivity analysis on q, where results for q=0.5 are potentially different from the main text results. Given the very possibility that the actual value of q is in that range, I would urge that the authors revisit their main results taking this into account.

Reviewer #3 (Recommendations for the authors):

Probably the most important observation here is that Canadian school cluster sizes and k parameters seem more consistent with a public health system that is accurately identifying (even small) school outbreaks, whereas the absence of single case outbreaks and the large fraction of very large outbreaks in the US data suggests a system which is calibrated to only identify (more obvious) superspreader events. Canada's per capita excess death rate during the pandemic has been notably lower (around 1/3) that seen in the US. Given that a relatively small contribution to mortality has come from pediatric cases, can the authors spell out a bit more explicitly how better surveillance may have blunted the pandemic's impact in Canada relative to the US?

Thank you for making the relevant data (https://github.com/PaulFredTupper/covid-19-clusters-in-schools/tree/main/schools_cluster_paper/datasets) and code accessible.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "COVID-19 cluster size and transmission rates in schools from crowdsourced case reports" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor.

The manuscript has been improved and is very close to satisfactory for acceptance but there are some remaining issues that need to be addressed, as outlined below:

1. Please make the abstract more balanced between methodologic gains and scientific conclusions.

2. Apply techniques to account for multiple generations of infection (or at least rerun the model assuming a smaller 4-5 day window to define clusters in line with the known serial interval) to ensure that this does not substantially impact the model's semi-quantitative conclusions.

Reviewer #1 (Recommendations for the authors):

Thank you for the extensive and extremely helpful changes to the article. It is well written, comprehensive and covers an important topic.

Reviewer #2 (Recommendations for the authors):

I greatly appreciate the authors revisions in response to the reviewer comments. In my previous review, I had a comment about the definition of the cluster and multiple generations of transmission. Now that the authors have provided that definition I have one major comment remaining.

The authors responded to my comment with: "These are indeed limitations of our analysis. We feel that we already addressed some of these limitations in the second-to-last paragraph of the discussion, but we have now added the following text as well: 'Furthermore, we assumed that all clusters consisted of an index case and a number of other cases directly infected by the index case. In reality, there may be longer chains of transmission. Any of these assumptions may bias our estimates of the distribution of ν and β.'"

Without strong evidence otherwise, I think the authors should address this concern within the analysis rather than simply a discussion. The definition of cluster now explicitly includes multiple transmission generations (through linking cases in successive weeks with one another). How many clusters have "multiple generations"? How does cluster size compare between single and multiple generation clusters? I imagine the multiple generation clusters are the largest ones, but it may not be the case.

Since every cluster in the current analysis is finite and small (i.e. the size of the cluster is finite and not close to the herd immunity threshold of the school), the data suggest that the R within schools is less than 1, but the author's analysis suggests otherwise because the analysis focuses solely on the index case transmission (e.g. not accounting for the fact that for a cluster of size 9 a single individual infects 8 individuals but each of those 8 individuals are not transmitting further). There is quite a bit of literature about stuttering chains of transmission (e.g. blumberg and lloyd-smith's work for monkeypox) that could be appropriate for addressing this issue. I believe the authors could adapt their analysis to account for multiple generations explicitly using those methods or in a different way the authors deem appropriate. This point is important because ultimately it impacts the interpretation of R, the estimation of Β for the subsequent analyses, and potentially the impact of interventions.

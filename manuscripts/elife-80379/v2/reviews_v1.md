# Peer review - Round 1

Editors:
- Jason P Lerch, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80379.sa0](https://doi.org/10.7554/eLife.80379.sa0)

This important work is of broad interest to readers studying brain plasticity, individuality, and shared/non-shared environments. The identification of distinct patters of brain networks, in the absence of main effects, between two broad classes defining how mice explore their environments, is especially interesting. The evidence supporting their conclusions is convincing.


---

# Peer review - Round 1

Editors:
- Jason P Lerch, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80379.sa1](https://doi.org/10.7554/eLife.80379.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Individual behavioral trajectories shape whole-brain connectivity in mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jason Lerch as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Yohan Yee (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The division of their cohort into two groups raised concerns by all three reviewers. The authors need to address these concerns by clearly showing the existence of two distinct groups, exploring sensitivity to different cutoffs, better justifying why some mice were excluded entirely, and if an intermediate group of mice are still excluded describing their covariance patterns.

2) The manuscript would also benefit from directly using their key behaviour metric, roaming entropy (RE), by using RE-slopes as continuous variables (in addition to clustering based on RE-slopes).

3) The authors need to slightly expand their statistical analyses by running permutation tests over the chi-squared tests, exploring a range of thresholds for network based statistics, and assessing whether alternate means of removing overall brain volume change their results.

4) The authors need to partially expand their introduction and discussion by being clearer that structural covariance, as used here, is a group measure and not easily applicable to an individual, being more nuanced in associating structural covariance with connectivity, and discussing what aspects of their environment (social vs space) have impacts on structural covariance.

Also, a note of clarification based on discussions with reviewer #2: "On acquiring more data to test whether their elaborate enrichment setup is _required_ for individuality, I don't think that's necessary, since that's not specifically the aim of this study. I should have been clearer about my comment – I meant that more as a Gedanken experiment to illustrate what would be needed to specifically tie their enrichment setup to the increasing variability in roaming entropy."

Reviewer #1 (Recommendations for the authors):

Most of my confusion and possibly critique relates to the division of mice into two groups. Here the authors need to show the data that supports this division in a more convincing fashion, clear up how the automated clustering supports these division, illustrate how the intermediate group behaves on their measures, and possibly show sensitivity analyses as to how sensitive the groupings are to differences in ways of subdividing the cohort. In addition to clearing up the clustering it would be good to show slopes as a distribution/histogram to be convince the reader that it is indeed a bimodal distribution.

Reviewer #2 (Recommendations for the authors):

I genuinely enjoyed reading this paper-it was well written, clear on what was done, concise, and on a relevant and interesting topic.

A common question that came up throughout my reading of the manuscript was on choices made in grouping data: why partition mice into flat and down roamers (while excluding a few with slopes above and in between), as opposed to directly working with the slope. For example, in looking at structural covariance differences, a single analysis (on the entire group of mice) examining covariance differences due to RE-slope could be achieved through the inclusion of RE-slope interaction terms in linear models. Such an approach would benefit from a larger sample size and increased power. Unless the distribution of RE-slopes is bimodal, the justification for stratification is unclear. Similarly, why average the RE over three weeks? Given the temporal resolution of the RFID data and that RE is computed for each night, partitioning into four long periods seems unnecessary.

Clarity on the role of the enriched environment would be helpful. While it is reasonable to believe that individuality emerges from exposure to an enriched environment, it is unclear from this study if this enrichment is required. An explicit comparison of enriched mice with those raised in standard housing would rule out intrinsic age-associated divergence of roaming entropy. In other words, if four cohorts of standard-housed mice were exposed to the enriched environment to track roaming but only during each of the four time periods, would the emergence of individuality not be as pronounced?

Some comments on specific parts of the study and manuscript:

1) Line 100: "Mice that showed in-between slope values (n = 10) were excluded from the clustering" is inconsistent with the subject numbers listed on lines 88 (total n=38) and 96-97 (15 flat roamers, 15 down roamers). Also, this conflicts with the statement on lines 393-394 ("Excluded from the subgroup analysis are 2 mice with in-between slope values and 6 mice with higher than 0.006 slope values").

2) Line 165: do you mean Figure 2B (as opposed to 3B)?

3) Line 175: I would suggest averaging over cortical and subcortical regions separately, given their distinctive function, development, gene expression, connectivity, and covariance patterns.

4) Line 282: missing closing parenthesis.

5) There are various places in the manuscript where structural covariance is used as a proxy to traditional measures of connectivity. While structural covariance has been found to be statistically associated structural and functional connectivity, the idea that structural covariance is driven by synchronized plasticity between structurally connected regions has yet to be confirmed. Therefore, I would caution against making this connection (no pun intended) between covariance and connectivity. A mention of this (and other study limitations) in the discussion might be helpful.

6) Lines 550-551: Could you double check the definition of the p-value? Unless NBS (which I am admittedly not an expert on) defines the p-value differently, the p-value is a probability of observing data given the null, as opposed to a probability of an effect.

7) Reasons for only including female mice should be explicitly listed – I assume male mice were excluded to avoid aggression/mating?

8) Figure 3: it would be helpful to annotate the rows and columns of these matrices with names of coarse structures.

Potential ideas to further improve the study include:

1) Are anatomical changes driven by neurogenesis? I.e., does the size of the dentate gyrus correlate with DCX?

2) Apart from access to a larger and richer space, the ENR group differs from STD in the number of mice and therefore potential social interactions. I'd be curious to know whether these results can be separated into social vs spatial exploration effects. For example, based on RFID data, do flat roamers tend to spend time with other mice more, while down roamers are more isolated? If it is possible to extract from the RFID data, I think an analysis that includes measures of social interactions would make this a far stronger study.

3) Similar to the above comment, can the effect of activity be teased out from the RFID data? Exercise has been shown to correlate with brain structural differences; I wonder if some of the neuroanatomical variation seen comes about from mice just moving around more.

Reviewer #3 (Recommendations for the authors):

– The interpretation of structural covariance is oversimplified especially in introduction. Specifically, REF 19 is being mischaracterized – this paper did suggest some convergence but also significance divergence with white matter connectivity. In the discussion the authors invoke the idea that structural covariance "may reflect synchronized plastic changes occurring across multiple brain regions over time". This idea should be included in the motivation for the investigation as well.

– Given references to prior related work by the authors and others, it is not currently clear what are the exact analyses that have not previously been done which are unique to this paper. The paper would benefit from a clear discussion paragraph stating what this study does that has not been done previously and what is a replication (differentiating replication from restatement of results already reported in the same mice).

– The statement on p.7 that "The majority of these ROIs were conserved as significant group differences when considering relative volumes (% of whole brain), suggesting normal scaling" should be clarified. Do the authors mean normal scaling versus nonlinear scaling cf https://www.science.org/doi/10.1126/science.aar2578? Note that dividing by total brain size is not really an effective way to "control" for the effect of total brain size (https://www.sciencedirect.com/science/article/pii/S1053811922006012)

– The chi-square tests for equality of two correlation matrices would be better if replicated with permutation testing as REF 21 seems to indicate these tests are anti-conservative in small samples.

– NBS uses permutation testing which is good. However it is more rigorous to consider the t-statistic over a range of thresholds not just a single threshold. I'd suggest 2.5-3.5 in 0.1 intervals as a sensitivity analysis. Also it's not clear why t=2.4 is mentioned in results but t=3.1 in mentioned in the methods.

– This is out of my area of expertise but is it possible that genetic differences including de novo mutations could underlie some inter-individual differences between inbred mice?

– I am having trouble understanding the rationale for the precise cut off values between groups. On p.15 manuscript says "Excluded from the subgroup analysis are 2 mice with in-between slope values and 6 mice with higher than 0.006 slope values." while on p.10 it says "Mice that showed in-between slope values (n = 10) were excluded from the clustering to achieve a sharper distinction. Presumably, I am not understanding something but it should be more clear.

– In addition, the rationale for excluding "up roamers" with higher slope values is not clear. These mice should be included in the flat group in a sensitivity analysis to assess robustness of findings.

– Currently it is not clear to what extent findings depend on the specific thresholds chosen to differentiate flat vs down roamers. It would be an improvement to conduct a sensitivity analysis in order to confirm the robustness of the findings to methodological variability to methodological choices which may seem arbitrary to a reader.

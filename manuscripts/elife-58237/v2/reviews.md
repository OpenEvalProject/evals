# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58237.sa1](https://doi.org/10.7554/eLife.58237.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Meta Research: Replication of Significant Results - Modeling the Effects of p-Hacking" to eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by the eLife Features Editor (Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: William Hedley Thompson (Reviewer #2); Gregory Francis (Reviewer #3).

Summary:

The authors present an argument and simulations illustrating the impact of the replication rate of four different questionable research practices. I found the argument both interesting and convincing. The article also raises important points about interpreting replicability that are very much misunderstood by many practicing scientists. However, improvements could be made to clarify certain assumptions and aspects of the argument.

Essential revisions:

1) Equation (1) succinctly related replication rate (RR) to power and alpha. In some sense, almost everything follows from this equation. The details about how different QRPs affect alpha and beta are secondary (but useful) analyses. A further discussion of equation (1) might be worthwhile regardless of how alpha and beta take their values (through QRPs or otherwise).

2) It was not clear to me how the value for β2 was selected. Based on the figure captions, I think it was just set to be β2=0.9, so 90% power. But the problem introduced by QRPs is that they tend to inflate standardized effect sizes. So, a replication of a QRP-influenced study might estimate power based on the effect size reported in the original study. Doing so will often lead to gross underestimation of power for the replication study (even though the replicator thinks they have 90% power, they might actually have 50% power). Also common, the replicator uses the same sample size as the original study, which again tends to lead to low power if the original study used QRPs. It is through these mechanisms that QRPs for an original study contribute to a low replicability rate (provided the replication study uses good practices).

3) As I read it, the headline result seemed to be that p-hacking doesn't have a large impact on replication, and therefore the explanation for surprisingly low replication must lie elsewhere. Unfortunately, the support for this claim hinges on the degree of p-hacking that one envisions, and it seems to me that the degree of p-hacking envisioned here is rather mild. My own experience suggests that most p-hacking flows from investigators' ignorance about what constitutes p-hacking, and in such cases, investigators can easily p-hack to a much greater degree than the simulations here suggest. I suspect that p-hacking investigators can easily conduct dozens if not hundreds of tests for every result ultimately published, which is a much more severe form of p-hacking than the simulations here envision. In these cases, p-hacking very well may be an important cause of non-reproducible results, thus overturning the major finding of this paper.

To be sure, the manuscript is abundantly aware that the degree to which p-hacking generates non-reproducible results depends on the degree of p-hacking, and both the results and text make that clear. So, I don't think the manuscript is 'wrong'. But, I fear that if one really wants to know how much p-hacking contributes to non-reproducible results, one has to know the extent to which p-hacked studies are indeed p-hacked.

-From the Features Editor: The article needs to explore levels of p-hacking higher than those explored in the current version and, if necessary, to revise the discussion and conclusions in the light of what these new analyses find.

Also, please consider discussing and citing the following paper:

Simonsohn et al 2015, http://dx.doi.org/10.1037/xge0000104

4) I also found the last simulation - meant to investigate the effect of removing outliers - unconvincing. As I understand it, the simulation generated hypothetical data sets that were the contaminated by outliers with a standard deviation ten-fold greater than the actual data generating process. It seems to me that this is a poor model for capturing outliers, because the outliers in this case are so anomalous that they corrupt the performance of the good-practice analysis. Thus we wind up with the head-scratching result that selective outlier removal improves FDR and RR. I don't think this set-up captures the actual hazards of selective outlier removal, and wouldn't put much stock in its results. To summarize, the simulation set-up needs to be more realistic and/or better justified.

5) A possible discussion point regarding the assumptions of the RR value. An interesting assumption in the RR value is that null/non-significant results are not replicated. And lowering the alpha threshold for statistical significance will increase the number of false negatives. So a possible outcome of focusing on improving RR with alpha thresholds that more false negatives go undetected and not replicated?

6) The authors use a group size of 20 (so total n=40) but sample size appears to be a key variable that will impact some of these measures (e.g. outlier exclusion). The researchers motivate their value by citing Marszalek, Barber, Kohlhart, & Holmes, 2011, Table 3.

First, I think the authors may be referring to table 1 to get the value of 40 (I am unable to locate the value in Table 3)?

Second, others (e.g. Fraley & Vazire 2014, 10.1371/journal.pone.0109019), found the average sample size (in social-personality) psychology research to be higher (here: 104). How dependent are the results and conclusions on the limited sample size? (especially for outlier exclusion). Also how dependent are the outlier exclusion results if more/less of the data points our outliers (currently 5% of data).

7) In Figure 3,4,6,9,11,12 and the associated text, there is no quantification about how much the "p-hacking" approach is worse and unprecise language is used, e.g. "is modest for high base rates" and the reader has to deduce the differences from the many-paneled figures. I think adding some summary numbers to the text (or an additional figure) to show the differences between methods would be useful (e.g. state RR difference when the base rate is 0.2 and 0.5 (with d=0.5, k=5) or maybe the total difference between the curves). This would be especially helpful when contrasting the differences between the "p-hacking" and "good practice" differences for the different thresholds where the reader has to deduce two differences from the graph and then compare those deduced differences in their heads.

8) One quite surprising result here was that selective outlier removal seems to increase the RR and perhaps needs a little more discussion. At the moment, a reader could read the paper and conclude that performing selective outlier removal is something that should be done to improve the RR. Is this the authors' position? If not, perhaps this should be explicitly stated.

9) The supplemental material (and a few places in the main text) suggest that QRPs might actually be favorable for scientific investigations because they increase the replicability rate. The text describes the situation properly, but I fear some readers will get the wrong impression. The favorable aspects very much depend on what a scientist wants (to avoid) out of their analyses. The supplemental material makes some claims about inflation and setting of Type I error rates and power that seem to contradict the Neyman-Pearson lemma. If not, then the multiple-studies researcher must using a larger sample size, so there are costs involved. This might be worth discussing.

10) In the Discussion the text suggests it will be difficult to increase replicability in fields with low base rates. To the contrary, I think it is easy: just increase the base rate. Scientists should do a better job picking hypotheses to test. They should not waste time testing hypotheses that would be surprising or counterintuitive. The text then goes onto discuss about how campaigns to reduce p-hacking may be ineffective. I get the point, but a field with a low base rate of hypotheses should have a low replication rate. Increasing replicability is not (or, should not) be the goal of scientific investigations.

11) The authors are familiar with some of my work on this topic (they cite several of my papers). There, the problem is not a low replication rate, but a "too high" replication rate. The problem is that if both original and replication scientists are using QRPs, then the replication rate is too high, compared to what would be expected with "good practice" analyses/experiments. In my view, this is the more serious problem with current practice, because it implies that the Type I error rate is higher than "good practice". This suggests that scientists are not doing what they intended to do. This different viewpoint struck me while reading the introduction of the paper. There it is noted that some people suggest that QRPs lead to low replication rates. But this claim never really made sense (at least not without more discussion) because QRPs increase the probability of rejecting the null; so QRPs increase the replication rate. Indeed, if the simulations were revised so that both the original and replication scientists used QRPs, there would be quite an increase in the replication rate, even when the true effect is 0.

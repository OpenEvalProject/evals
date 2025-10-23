# Peer review - Round 1

Editors:
- Caroline Colijn, https://ror.org/0213rcc28 Simon Fraser University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76780.sa0](https://doi.org/10.7554/eLife.76780.sa0)

Grouping pathogen genomes into clusters is a key tool in genomic epidemiology. In this paper, the author takes a simulation-based approach to investigate the epidemiological processes that influence clustering in tuberculosis genomic epidemiology. The simulations explore whether differences in transmission can be detected with clustering-based analysis. This work finds that clustering can be impacted by sampling strategy as well as by changes in transmission and population dynamics, and draws out some interpretations of these results for users of clustering in this field.


---

# Peer review - Round 1

Editors:
- Caroline Colijn, https://ror.org/0213rcc28 Simon Fraser University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76780.sa1](https://doi.org/10.7554/eLife.76780.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Understanding drivers of phylogenetic clustering and terminal branch lengths distribution in epidemics of Mycobacterium tuberculosis" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Jason Andrews (Reviewer #1); Vegard Eldholm (Reviewer #2).

We agree that this paper is interesting, timely and raises important points. As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

1) Both reviewers had some comments about the simulations for R0 or 1.1 and 0.9 – additional clarity on what impacts R0, and more substantively, can TBL and clustering rate help in estimating R0, if the infectious duration is held fixed? R1 notes "These issues should be addressed and/or the conclusions about lack of ability to infer R0 differences should be tempered a bit".

2) While both reviewers (and I) really like the idea of having an illustrative example showing how this could matter in a scenario with two co-circulating lineages in the same community, the differences seem too pronounced.

3) I have an additional comment (as reviewing editor):

You note that you select simulations with 100-2500 tips – how do you initialize the R0 < 1 simulations to end up with at least 100 tips? The tree size will presumably differ with different R0, as will the number of simulations you run that don't meet the size condition.

Given that you also sample in the last 10 years of the simulation. A very different fraction of the process will potentially end up in the last 10 years under the different parameters. Accordingly, the relationship between R0, TBL and clustering will be complex, and the fact that the results don't seem to be informative about R0 may be partly a result of this "simulation bias" and sampling period.

4) R1 notes that more comments on the sources of data that could help to disentangle the impact of differences in latency vs transmission would be helpful. Presumably that's a population-representative sampling that would enable knowing the fraction of cases that are of the two co-circulating types, over time? Or good estimates of the infectious duration? Or either, or both.

5) Please address minor points on clarity and communication raised by the reviewers. In addition, could you comment on the mutation rate during latency, and what might the result be if mutations were not occurring during latency at the rate that they do in active disease?

Reviewer #1 (Recommendations for the authors):

Overall, the manuscript was fairly clear and straightforward to interpret, with a few comments below. The main concern I had was with the overarching conclusion that TBLs are non-informative about R0. The results show that transmission rates are associated with TBL/clustering, but the argument is that R0 is not because it depends on the ratio between the transmission rate and removal rate, each of which can alter those metrics. But it would be reasonable to make assumptions about the infectious duration, for example within a lineage and/or location, enabling comparison between variants within a lineage, within lineage over time or space, etc. Holding infectious duration constant, comparisons of R0 would then be possible through TBL or clustering. Moreover, in some cases, the infectious duration can be directly estimated (i.e. by performing a prevalence study and comparing with notifications), enabling the relation of R0 to TBL/clustering directly through transmission rates. These issues should be addressed and/or the conclusions about lack of ability to infer R0 differences should be tempered a bit. This wouldn't diminish the importance of the study, as explaining the relationship between all of these parameters and these metrics is the valuable task that this article undertakes.

Reviewer #2 (Recommendations for the authors):

First, this is a cool and timely paper, and I really like the approach.

There are however some things I believe could be clarified and perhaps explored a little bit further.

Page 7 "An example": Drawing up an example of how different characteristics of co-circulating TB-types can result in contra-intuitive findings is great. In the example, a less transmissible type nevertheless has an R0 > 1 whereas a more transmissible variant has R0 < 1. Looking at table 2, it seems evident that the more transmissible Type 2 is contracting (R0<1) due to higher cure/death rates and higher sampling compared to the less transmissible Type 1, whereas it exhibits shorter TBLs and higher clustering due to shorter latency and a slower molecular clock compared to Type 1.

I have a few questions/comments which I hope will clear this up a little bit on my part:

- I think the example would be easier to follow if you explained which of the parameters influenced the R0, TBL and clustering rate, as I have tried to do above. If my summary is not correct, I guess that illustrates that this is a bit complex for many readers.

- This is a bit embarrassing, but what specifically should sampling rate be interpreted as here, and throughout the paper? If I get this right, sampling represents both observation and removal (the patient is sampled, and hence also cured and does not transmit further)?

- I think it would also be cool with a little description of the two types in more biological/medical lingo. If I understand correctly, Type 2 is more transmissible, and also characterized by rapid onset of disease (short latency), followed by rapid death, self-cure or health-seeking. This actually makes sense, and the only reason R0 < 1 is that health-seeking, cure and death rates are even more elevated than transmissibility?

Page 3: If I'm not wrong, the model used is a form of birth-death model? Perhaps this could be spelled out, and if not, explain how it differs from a B-D model.

Suppl figures: I believe the numbering of the suppl figures in relation to the text is wrong in quite a few instances

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Understanding drivers of phylogenetic clustering and terminal branch lengths distribution in epidemics of Mycobacterium tuberculosis" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

In response to the question about bias induced by having to choose among your simulations, I fear that you have misunderstood the question and therefore haven't addressed it. (The new exploration of the impact of sampling period is nice to have, though). You write: "Regarding the settings: all simulations are initialized as a single individual, simulations that result in less than 100 tips are discarded. For R0 < 1, a larger number of simulations needs to be discarded, as trees are tendentially smaller. "

This is a source of potentially large bias because the tree you obtain is likely not to meaningfully *have* an R0 of 0.9. To grow from 1 to 100, the mean number of offspring that is realised is definitely above 1 for an extended period, even if the parameter you set in the process was such that the *expected* number was less than 1. (I would be curious to see a birth-death simulation with an R0 of 0.9 that grows from 1 to 100 tips and last over 10 years). The probability of this growth is not zero, but it's small, so the trees you obtain are not at all representative of R0 = 0.9 trees. This means that when the clustering differs or fails to differ, you can't interpret that as being able to identify (or not) trees from R=0.9 vs R=1.1.

The tree sizes will be different too, and from coalescent theory, we know that this alone will change the patterns of genetic diversity (and hence the clustering). I would hazard that if you took simulations from identical parameters (birth, death, sampling, etc all the same) but in one set you chose the rejection criterion to have the trees need to grow bigger or last longer than in the other set, you would also find differences in clustering as a sole function of the cutoff criterion. Some portion of what you find is due probably due primarily to size and you could explore this, as well as not so dramatically biasing the trees you analyse by requiring extremely unlikely events before a tree gets into your sample.

Think of it the other way. If you took trees from a simulation with R0> 1 but you *only* looked at trees that went extinct before reaching 10 taxa, and then you did estimation or some other analysis on those trees, they would look very similar to trees with an R0 < 1 because those also die out. By removing the ones that grew you removed the information that R0 was set to be > 1. Conversely, here, by rejecting the vast majority of trees simulated under R0 < 1 that died out, you are removing the information that R0 was ever < 1.

I have asked for a revision because I think this point is not minor, as quite a bit of the paper is focused on clustering and R0 under simulations, and this same issue could impact many of them. It would be interesting to explore a genuinely declining population (rather than one that is declining in expectation because R0 < 1 but growing in its actual realisation because you start with 1 taxon and branch, rejecting those simulations that do not grow). However, initialising that population is challenging because the results would depend on the initial genetic diversity.

As a side note – under point 4 in the response, you note that "At least, in theory, all the parameters of the model can be estimated with phylodynamic analyses." But this paper finds a fundamental unidentifiability that suggests that these parameters are not identifiable: https://academic.oup.com/mbe/article/38/9/4010/6278301. They use likelihoods, not clustering, but since the likelihoods and portion clustered are fundamentally based on the branching times in the phylogenies it seems that their results would probably carry over.

# Peer review - Round 1

Editors:
- Chris I Baker, National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53498.sa1](https://doi.org/10.7554/eLife.53498.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Dataset decay and the problem of sequential analyses on open datasets" for consideration by eLife. Please note that following a discussion among the relevant editors, your article was considered as a Feature Article rather than as a Research Article.

Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Chris I Baker) and the eLife Features Editor (Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: Chris I Baker (Reviewer #1); Nick Holmes (Reviewer #2); Guillaume A Rousselet (Reviewer #3).

Summary:

The reviewers all agreed that the manuscript focused on an important topic, and they all appreciated the simulations and analyses included it. However, the manuscript would benefit from clarifying a number of points - please see below. In particular, some passages require more in-depth discussion, and the passage that discuss potential solutions need to be fleshed out.

Essential revisions:

1) The notion of exploratory versus confirmatory analyses is ultimately a key issue in this manuscript. Indeed the authors propose that one solution to the problem of sequential analyses is to treat all studies using open data as exploratory. However, the authors do not clearly define or discuss these terms or the implications of labelling analyses as one or the other. I think the manuscript would benefit from more explicitly describing and discussing the distinction between exploratory and confirmatory, rather than assuming that everyone is already on the same page.

2) Another important issue is the ability to determine how many prior tests have been performed on a dataset. As the authors note several times in the discussion, the "file drawer" problem is of major concern here. But the authors do not really consider or discuss how this problem could possibly be dealt with. For example, should authors be required to preregister the analyses they plan to perform before being given access to a dataset? I think this is such an important issue in the context of the current manuscript that it deserves more in depth discussion - even if the field decides on an appropriate method of correction, that will only prove useful if there is a way to track the number of tests performed and not just those that resulted in a significant effect and hence publication.

3) In general, while the manuscript does a good job of highlighting the problem of sequential analyses on open datasets and discusses some possible solutions, it does not really suggest any recommendations for the path forward. How should the field grapple with these issues? Which of the possible solutions should be favored, if any? How should the field decide what is the best solution? How should we keep track of analyses on open datasets.

4) In the abstract, the authors state that "we should expect a dataset's utility for discovering new true relations between variables to decay'. I don't quite follow this. The alpha level is about controlling the false-positive rates. I do not see a clear link between this and the likelihood of new true-positive discoveries (which would require consideration of likely effect sizes, power, etc). If a researcher has a (true) hypothesis which is clearly-predicted by theory, convergent with other datasets, supported by a small experiment, and comes with a precise effect-size, I do not see why *any* number of prior tests of an open dataset should affect that open dataset's ability to support the researcher's well-defined hypothesis. These researchers could, indeed, simply abandon the null-hypothesis significance-testing approach for the open dataset, and simply ask: what are the likely values for the effect that I am quite sure exists? Perhaps by 'new true relations' the authors here mean 'unpredicted' or 'novel' or even 'random' and only within the NHST approach? So, my general comment here is that I am uncomfortable with the idea that open data sets decay in usefulness with time, and I would ask the authors to consider this, and soften or qualify the description.

5) I can see that the definition of what is a 'family' of tests is fundamental here. What I find a bit odd about this sequential testing approach is that, at the outset, the size of the family is not known. But it could be predicted based on prior or concurrent datasets, or could be set at an arbitrary level. Have the authors considered, for example: the first X hypothesis tests can use a certain alpha level, then the next X tests, etc. This stratified sequential approach would set the size of each family from the outset, and allow everyone in the first X groups of researchers to work on a level playing field (there would then, hopefully, be no great rush to be the first researchers to test their dubious hypotheses without thought, thus wasting their scoop of alpha).

6) The sequential correction methods all punish late-comers to the data party. Perhaps a particular dataset is perfect to test an idea which has not yet been developed - the data comes before the idea's time. It seems wrong that good researchers or good ideas who happen to arrive at the dataset late relative to other (worse) researchers or ideas should be 'punished' with higher alphas just for being late. (Not wishing to increase the admin-burden, ) perhaps some of the alpha can be saved up for a rainy day? Perhaps some of the alpha can be won or awarded through a competitive merit-based process? Perhaps researchers who meet a certain level of good research practice (e.g., pre-registration, ethical, open, all the necessary review, meta-analysis, and experimental work already in place, etc), should be allowed to use standard alpha levels, and it is only the disorganised vultures feeding on the data carcass who should be discouraged with alpha-punishment?

7) If the dataset comprises *all* the available data on a particular topic (e.g., brains affected by 'mad cow disease' in Britain in the late 1990s) - i.e., it is the population, and not just a sample - does this change the assumptions or outcomes of the authors' approach at all? It feels like it should be a special case, but maybe not...

8) Relatedly, if a dataset is large, one solution could be simply to restrict researchers to a random sample of the dataset (say, 10% of the available data), and allow them to keep alpha at standard levels. Because exactly the same data will almost never be tested twice on the same or a different hypothesis, does this completely remove the problems of inflated false-positives? It feels to me like it should. Should alpha correction only apply to researchers who use exactly the same subset and/or all the dataset?

9) In the authors' simulations, to estimate the likely number of publications resulting from false-positive findings, they assume that *every single 'significant' finding* will lead directly to a single publication - in effect, that publication bias is absolute, complete, and is itself unbiased. I find this assumption very hard to stomach. Researchers may tend to hold back significant results which don't support their, or their supervisors' or group's prior, current, or proposed research. Publication bias is not simply the immediate publication of (false) positive results, but also the delayed or suppressed publication of (true) negative or opposite-direction (false positive) results. Further, many (good) labs would replicate a result before going to press, or at least report multiple results, true and false, in the same paper. The authors may have stated this in other ways, but I think this strong assumption leads only to a very upper bound on the likely number of resulting (false positive) papers. Perhaps this can be stressed more clearly?

10) The authors used a real dataset to test a series of psychological hypotheses. They seem to have assumed that none of these hypotheses would pick up on any real effects in the data. Can they comment on the likelihood that their tests are establishing the true null distribution of effects, rather than actually being skewed by real effects? One solution would be to scramble the raw data in some way to ensure that even if there was a true effect, randomised and then processed voxels would not show this effect.

11) The introduction and discussion could do a better job at contrasting different empirical traditions and statistical approaches. The introduction could make clearer that the current project assumes that most researchers are engaged in a particular (though dominant) type of research involving confirmatory hypothesis testing in which the goal is to explain rather than predict. Do you think the problem would be different if the focus was on prediction?

The discussion mentions cross-validation and the problem with small sample sizes, but doesn't acknowledge explicitly the tension between explanatory and predictive research - Yarkoni & Westfall (2017) is a great reference on that topic:

https://doi.org/10.1177/1745691617693393

12) FDR is not clearly defined and would need to be better justified given the strong limitations of such a concept, which Richard Morey and Deborah Mayo described as completely flawed:

https://osf.io/ps38b/

https://medium.com/@richarddmorey/redefining-statistical-significance-the-statistical-arguments-ae9007bc1f91

13) What if we are in a field in which inappropriate statistical methods are the norm: should future researcher using appropriate tools be penalised for analysing a dataset after many doomed attempts? You touch indirectly on the subject in the section "Gray-area when families are not clear". For instance, in a field dominated by fixed effect analyses of means, I would argue that researchers attempting to fit carefully justified generalised hierarchical models should be allowed to reset their alpha counter.

14) The discussion mentions Bayesian statistics as a potential solution, but with the current trend in adopting arbitrary thresholds for Bayes factors, the same problems encountered in mindless frequentist practices will also apply to Bayesian/Laplacian ones:

Gigerenzer, G. & Marewski, J.N. (2015) Surrogate Science: The Idol of a Universal Method for Scientific Inference. Journal of Management, 41, 421-440.

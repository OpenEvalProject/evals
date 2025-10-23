# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- Nick Parsons, University of Warwick Coventry United Kingdom
- Nick Holmes, University of Nottingham Nottingham United Kingdom

## Review text

DOI: [10.7554/eLife.48175.004](https://doi.org/10.7554/eLife.48175.004)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Ten common inferential mistakes to watch out for when writing or reviewing a manuscript" to eLife for consideration as a Features Article. Your article has been reviewed by two peer reviewers, who have both agreed to reveal their identity: Nick Parsons; Nick Holmes.

Both reviewers produced very substantial reports, and rather than consolidate them as normally happens at eLife, I have combined them so that all the comments on each section of your article are together. This means that the decision letter is very long – and also somewhat critical in a few places – but both referees really engaged with the manuscript

I would like to invite you to submit a revised version of your article that addresses these comments. While the list of comments below is rather long, the reviewers and myself feel that it should be possible to address them within a reasonable time frame.

Also, please note the following:

1) Please remove section 6 (and consider replacing it with a section on 'circular analyses' – as suggested by the referees).

2) Please revise Figure 1 (see comments below).

3) Please remove Figure 3 and Figure 4.

Summary:

Reviewer #1:

Overall, I enjoyed reading this manuscript. It certainly has some merit.

However, at times I found myself profoundly disagreeing with some of the recommendations. I give a list of some of my more significant gripes below. I think this manuscript could be suitable for publication, but there needs to be a substantial amount of additional work to make it make it so.

First, I do not know the background of the authors (so apologies if I offend), but some of the wording and examples and description suggests that they are not themselves experienced applied statisticians. This manuscript would benefit enormously from the input of such a person, simply to reformulate some of the common mistakes and link in with well-known issues that statisticians typically observe when teaching statisticians, advising colleagues and reviewing manuscripts. I accept that it is important to have the tone and voice of the scientist (and not the statistician) in this manuscript, but it is important that the manuscript is such that it is has a much stronger statistical basis, to give it more weight.

Much of the text here is quite wordy and the explanations of the issues often confusing (e.g. issues 3 and 4). I am sure the authors could make these much simpler and easier to understand. The background of the authors is clearly in the neurosciences. This shows with their choice of examples at times (e.g. issue 1). This manuscript would work just as well with more neutral examples that would be understandable to anyone across the range of scientific disciplines. So, I suggest the authors re-write in such a way.

Manuscripts such as this are important and can have significant impact on not just the reporting of science, but also how it is done. So, I hope the authors decide to make appropriate changes to the manuscript in order to make it more acceptable for publication.

Essential revisions:

0) Introduction

Reviewer #1:

– It is worth making the point in the Introduction that many journals undertake in-house statistical reviews and/or send manuscripts out for more detailed statistical review if reviewers of the substantive content have concerns.

1) Absence of a control condition/group

Reviewer #1:

– This manuscript is at times very neuroscience focused. I understand that is the primary interest of the authors, but at times I think it simply distracts from the message and much simpler examples (that would be universal to all scientists) would have worked much better. That is particularly the case with this first common 'mistake'.

Reviewer #2:

– 'inflating the likelihood of observing spurious changes' – But all statistical tests are done using probabilities of false positives, which depend on the variability in the data. What is the evidence that low test-retest reliability leads to increased false-positive outcomes? As this section notes, it is only the absolute size of the difference that will be 'observed' – statistics will tell us if this difference is reliable or not, and that is where the (fixed) false-positive rate applies.

– I often come across control groups that are sampled after the results of the experimental group are known (e.g., lots of TMS studies). I would add here that control and experimental groups need to be sampled at the same time and with randomised allocation.

– This is not only 'longitudinal', this applies to cross-sectional data too.

2) Interpreting comparisons between two effects without directly comparing them

Reviewer #1:

– Figure 1 – This is an oddly chosen example. Clearly the variance in group B is much greater than the variance in group A. This explains (in part at least) why the test of the group differences is not significant. But, surely pooling here is problematic: we are assuming, for the methods suggested, that the variance is the same in each group whereas, to most, it looks like it is very different. The authors need to choose a better example to illustrate common mistake 2, and modify Figure 1 appropriately.

Reviewer #2:

– This problem applies also not just to 'difference scores' but any effect (e.g., a slope, curve-fit etc., not just 'differences'). I suggest the authors make it more general here (as they do in 'how to detect'), then give the specific and useful example of the simple difference of two differences. It may also be worth noting here that this is often the 'interaction' term in the analysis.

– 'differential statistical significance' – I would say something like 'different binary outcomes when applying a statistical threshold'.

3) Inflating degrees of freedom by violating independence of measures

Reviewer #1:

– This is a very complicated explanation for what most statisticians would describe in a very different way. It is needlessly complicated. This is what most statisticians would describe as the 'unit of analysis' issue – much described in the literature previously see e.g. Parsons, Teare and Sitch (2018, eLife).

Some poor practice is described here, where for example multiple measurements on the same subject are made as a means of ultimately comparing subjects. If a study aims to understand the effect of an intervention on subjects, then that is the 'unit of the analysis' and in order to draw inferences the replication must be at the level of the subject (the unit of analysis), not within subject (within unit). Multiple measurements on subjects improve the precision of estimation of the subject mean (for instance) but tell us nothing about the variability between subjects.

This is often observed as an artificial inflation of the degrees of freedom, pooling between strata in the analysis, but ultimately the problem is the lack of clear identification of the purpose of the analysis and the appropriate unit to use to assess variation that is used to quantify intervention effects. Personally, I don't think bringing correlation into the discussion helps a great deal. All we really need to be aware of is that measurements within (for instance) a subject are likely to be correlated, whereas by definition data from subjects are uncorrelated.

– Mixed-effects analysis – This is the canonical analysis that most statisticians would recommend. When we do this, we naturally estimate the appropriate within subject (cluster) correlations. This methodology should be much more widely used in many areas of science; only in medicine, where studies report patient data, and psychology is it generally recognised as being important. Although its roots go back to the genesis of statistics in agricultural science, where fields were divided into blocks, plots and nested sub-plots and plants etc.

– A priori statistical power analyses are always a good idea, but I really don't think it adds much to the discussion here.

Reviewer #2:

– This is true in some statistical procedures (e.g., where you model a single parameter at a single level for each participant), but not all. For example, I believe linear mixed models (e.g., in R), will have many dfs larger than N-x, yet these remain valid. I remember seeing large dfs in (e.g.) Brain Voyager FMRI outputs. I do not understand these multi-level linear mixed models, but I have questioned and been corrected on this df point by statisticians using R (e.g., see the df in Meteyard and Holmes, 2018; I didn't do the analysis). The recommendation in 'how to detect' should be clarified and/or corrected as necessary.

– 'average the resulting r values (don't forget to normalise the distribution first!)' – Perhaps give specific advice here: e.g., use Fisher's r-to-Z transformation, Z=0.5log[(1+r)/(1-r)]

– 'random factor' – 'random 'effect' would be better

4) Spurious correlations

Reviewer #1:

– Figure 2A, B, C – Surely the issue here is that 'outliers' have a big impact (leverage) on many statistics; means, variances, covariances, regression analyses, ANOVA and yes, correlations. But this is not an issue only of concern when estimating correlations. Surely the issue here is to present data visually and consider the meaning (validity) of any data points that are a long way from the rest of the distribution. I don't like the (implicit) argument here that the Pearson correlations are in some sense 'wrong'. It depends on whether the model is correct (straight line) and whether the assumptions of approximately normality are correct. It is perfectly plausible to believe Figure 2C is correct, and that only one data point was available at X=5, but there is good reason to believe that data are normally distributed. The point I would make here is the importance of error measurements when reporting. The confidence intervals of the Pearson correlation would help us enormously here. Point estimates of correlations alone are not that useful, unless the data are shown visually.

– The other thing I would take issue with here is the implication that Spearman's rank correlation makes more sense in settings Figure 2B and Figure 2C. In general, decisions about whether to assume normality are better made for principled reasons rather than for empirical reasons. Using a non-parametric correlation coefficient would make little sense to me here – they are generally very inefficient, as we convert to ranks first, which is the reason the value does not change from Figure 2B to Figure 2C. If data were reasonably tightly distributed symmetrically about the mean, other than one value which was a big distance away, my first recommendation would be to examine the credence of the extreme data point, not proceed to a non-parametric correlation.

Reviewer #2:

– 'Yet, the use of parametric correlations, such as Pearson's r, requires that both variables are normally distributed.'

No, it doesn't! All parametric linear models (as far as I understand) require that the error is normally distributed. In the case of a single-sample t-test against a single mean, this is identical to the requirement that the variables themselves are normally distributed. But, for everything else, it is the differences or error or residuals after the model is fit which must be normally distributed, not the raw data. The authors repeat in their tutorial what I understand to be a very common mis-interpretation, and it would be good for them to make absolutely certain that what they say here is correct, to avoid perpetuating these errors.

Here is a tutorial from the R team: https://rcompanion.org/handbook/I_01.html, specifically: "In particular, the tests discussed in this section assume that the distribution of the data are conditionally normal in distribution. That is, the data are normally distributed once the effects of the variables in the model are taken into account. Practically speaking, this means that the residuals from the analysis should be normally distributed. This will usually be assessed with a histogram of residuals, a density plot as shown below, or with a quantile-quantile plot… Be careful not to get confused about this assumption. You may see discussion about how "data" should be normally distributed for parametric tests. This is usually wrong-headed."

The authors are correct here that (genuine) outliers can lead to spurious correlations, but the remedy for this is, as they state: (a) plot the data, (b) run some robustness-checks, and to report all the results with their standard errors and with due caution.

One real problem is how do we identify 'genuine' outliers? Perhaps a large sample size is one remedy, so that we have a better coverage of the population? Yet, there will still be cases when clear 'outliers' are genuine observations which obey the law that you are trying to discover. For example, measuring mass vs. body length across the animal kingdom: there will be an awful lot of small animals down the bottom of the scale (e.g., insects), some in the middle (e.g., birds and most mammals), and fewer still at the extremes (e.g., whales or elephants). I would bet that the blue whale follows the same statistical law of mass vs. length as the gnat (with variance away from this model due to shape). A 'spurious' correlation might arise from incomplete sampling of the problem space – if we only sampled insects and whales, we might draw the wrong conclusion and call the correlation between mass and length 'spurious'. Or perhaps the data need log-transforming first?

My laboured point here is: if you don't have any independent reason to exclude a particular datapoint (e.g., the participant didn't do the task properly, wasn't wearing their glasses, is not healthy, is not typical; the elephant was stretching its legs), then I think it is dangerous to conclude that the correlation is spurious just because of one 'outlier'. Rather, authors need to present the data, check their assumptions, and speculate that sampling bias or experimenter error has led to this 'outlier'. In general, the authors are correct here: limited sampling of the intended population may make such outliers more likely, and correlations may then be more problematic. But this is all relative, and error can occur in both directions (Type I, Type II). The only solution is to be very careful, both in including and excluding data.

– 'when the two variables are not independent' – Repeated measures designs will often have highly-correlated scores between different conditions or time-points in the same participants. Again, is the real issue here 'independent error' (residuals) not 'independent data'?

– This is the 'regression towards the mean' error that I discussed in Holmes, (2007, 2009), yet this topic is only an "Honorable mention" here! I would suggest all these 'circular analyses' and 'double-dips' (i.e., both are experimenter-created dependencies in the data) could be in their own section (after dealing with the below comments, in which I suggest removing point 6 entirely).

– Figure 2A – I would bet that the red point is not an outlier here, as claimed in the legend.

– 'they can run some basic simulations' – I agree 100% (Holmes 2007, 2009), but this sentence will have, in my view, about 95% of your target audience hiding under the bedcovers in fear of programming. How does someone who is not sufficiently well-trained to spot these problems in the first place go about 'running some simulations'? Can the authors point to an online tool or tutorial that helps?

5) Use of underpowered groups

Reviewer #1:

– Experiments with small samples sizes are quite often small for very good reasons, not always but often. We should not recommend that scientists don't do small experiments – sometimes there is no option – but we should tell them not to report inferential statistics. Particularly if the study does not have an a priori power calculation. Not sure that Figure 3 adds much here.

Reviewer #2:

– 'In frequentist statistics in which a significance threshold of α=.05 is used, 5% of all statistical tests will yield a significant result even in the absence of an actual effect (false positives; Type I error)' – I think the authors need to clarify this a bit more, to, e.g.: "Assuming that the null is true, then randomly- and independently-sampled data from a normal distribution with a mean of zero will yield a sample that, when tested against a mean of zero, has a p-value below or equal to. 05 approximately 5% of the time." The word 'even' in their claim here is unhelpful – the stats explicitly assume that the null is true (it is never actually true!)

– 'Given that these two variables are random, there should be no significant correlations' – See previous point. There will be 5% 'significant' correlations.

– 'falsely significant' – I don't like this phrase. It seems contradictory. I know what they mean (something like: 'using the standard α criterion, most researchers would conclude that there is a positive correlation in the population when in fact there isn't').

– 'the experiment is underpowered' – But there is no effect in the simulated population. There can therefore be no sample size sufficient to find this effect. This cannot, therefore, be 'underpowered'. Revise.

– '<' should this, in fact, be '≤'? Same throughout the manuscript.

– 'Designs with a small sample size are also more susceptible to Type II errors' – Why? Type II error is a non-linear function of the sample size and the real effect size. Knowing the Type II error requires that you know the population distribution, which is almost never the case (and not required) in the kinds of parametric null-hypothesis tests that the authors are discussing here.

– 'based on a limited number of participants' – I would remove this as I don't think this it is justifiable. I think all effects (especially surprising ones) from a single experiment should be taken with the same degree of caution, regardless of their sample size (who sets the criterion in any case?). The statistics deal with the problem of sample size. Statistics can be biased as a function of sample size, of course, and some come with corrections (e.g., Hedges G instead of Cohen's d) but if you expect a large effect (e.g., removing striate cortex will impair vision), then I see nothing wrong with doing the absolute minimum of testing on your subjects to establish that effect. It would be unethical to remove 30 monkeys' visual cortices when 2 are sufficient to test the hypothesis.

– 'that were not replicated' – Yes, we should be especially skeptical if a second well-powered experiment failed to replicate the first, but I would only be normally skeptical of a single-experiment finding, regardless of its sample size. I think the authors' main point is that small studies will achieve significance only with large effects. True. But some large effects are real, so given a single particular result, how do you know? We must be allowed to search for large statistical effects. Collecting converging and independent evidences should be sought in all investigations, not just in those researchers looking for large effects: Smith and Little (2018).

6) Using parametric statistics with small sample sizes

Reviewer #1:

– Sorry but I cannot agree with much of this section. See my previous comments about normality assumptions. Tests of normality are really not very useful in most circumstances. In small samples, I agree with authors, they are useless. However, in large samples they will always reject with probability of very near one.

– In general, decisions about normality and whether to use parametric or non-parametric methods should be based mainly on scientific principle. For instance, if I collect data on the heights of 10 people, I report a median and IQR, but if I collect data on 50 people a mean and SD? No, that is clearly wrong. I believe that heights are approximately distributed, based on the way it is measured, my own experience and the experience of others (irrespective of what a test of normality tells me!), so I should summarise data on that basis in the appropriate way by a mean and SD.

– This sort of mechanical/automated approach to the implementation of statistical methods is strongly discouraged by the majority of statisticians. This is analogous to the widespread adherence to the (mis-) interpretation of p-values that has been so widely criticized by among others the American Statistical Association. In its guidance for the use of statistical tests for such decisions and the role of p-values it makes clear that "Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold" and "No single index [the p-value] should substitute for scientific reasoning".

– Scientific reasoning and precedent should be used to make decisions about how to appropriately analyse data, not arbitrary ad hoc (data dependent) statistical tests.

Reviewer #2:

– Section 6 is incorrect and should be removed. In part, due to the same problem as point #4 (normal distribution of error), but, what the authors seem to be arguing for (unwittingly) is an abandonment of parametric tests, not for their use only with 'large' samples, as explained below:

Parametric statistics were designed for small samples. If in any doubt about this, please check out Fisher (1925), available in full here: https://psychclassics.yorku.ca/Fisher/Methods/index.htm

In parametric statistics, from a sample of data we extract parameters, for example the mean and the SD (e.g., of the difference between means of two conditions). In our statistical model we compare those parameters to a normal distribution in order to make probabilistic inferences using the theoretical distribution.

When sample size is small (say <30), we do not refer our parameters directly to the normal distribution. Rather, we refer them to the t, F, Chi-Square, Poisson, Binomial, or any other appropriate statistical distribution. These distributions were originally created by sampling small numbers of datapoints, and seeing how they behaved. These distributions are all skewed in interesting ways, but as N increases, they tend to approximate the normal distribution.

The (in my view) often-mistaken 'rule of thumb' that you need at least 30 participants to do parametric statistics is wrong. It is in my understanding, opposite this. As N increases, the t-, F, Binomial, Chi-square, and Poisson distributions converge closer and closer to the normal distribution. So, when N=30, rather than using the t-test, you can just use the Z-test (i.e., essentially ignoring sample size). The critical t-value for 1 degree of freedom (N=2) at α=.05 is 6.31 (i.e., 6.31 standard errors of your sample mean difference away from zero). As N increases to infinity, the critical value converges to 1.645. At N=30, the critical t-value is 1.7, which is arguably close-enough to the population Z-score (1.645) that the t-distribution can be abandoned (i.e., only sample size is relevant for calculating the SE, df is not needed) and that the Z-distribution can be used instead. Small samples are already 'punished' via the df, by requiring much larger effect sizes to pass arbitrary statistical thresholds.

My understanding is that most statistical tests are designed for small samples. Non-parametric tests are for non-interval and non-ratio data (categorical, ordinal), or for interval/ratio data with populations for which no reasonable assumptions can be made (e.g., with large inexplicable outliers). Bootstrapping or other non-parametric statistical methods can be useful to check whether small samples are indeed sufficiently normal to use parametric tests (e.g., from Makin et al., 2009, where Ns=6-11: "In every case, this bootstrapping procedure supported the inferences derived from the t tests, so we report only the standard parametric tests in this manuscript.").

As the authors correctly note, small samples come with biases (e.g., effect sizes are larger for significant effects), but this does not invalidate the use of parametric tests. The authors cite Kar and Ramalingam (2013) in support of their claim, yet from that paper's conclusion: "Hence, there is no such thing as a magic number when it comes to sample size calculations and arbitrary numbers such as 30 must not be considered as adequate."

– 'though it is well agreed that you shouldn't use a parametric test with N<10 (Fagerland, 2012)' – The authors present no evidence for this 'well agreed' rule. I disagree with it, for example, as I believe would the statisticians who invented parametric tests. The article cited by Fagerlund, (2012) was specifically looking at skewed distributions (gamma and log-normal) of the underlying population parameters, and made the same common mistake about normal distribution of the data (should be: error/residuals). Yes, with data producing skewed error distributions, transformation or non-parametric tests are required, or a larger sample, and the central limit theorem can be relied upon. It is absolutely fine to use parametric tests under reasonable assumptions and with reasonable caution with N as low as 2 (Fisher, 1925).

– 'Nonparametric tests… are less sensitive to outliers' – Bootstrapping is a kind of non-parametric test. Such tests may highlight outliers by revealing a multi-modal distribution of summary statistics, but they are just as 'sensitive' to outliers. Inspecting the distributions and checking assumptions is the correct approach.

7) Flexibility of analysis: p-hacking

Reviewer #1:

– The authors advice on how to detect p-hacking is well-meaning but naïve.

In truth, only by pre-registering and providing detailed analysis plans, such as we do in clinical trials, can we ever hope to stop p-hacking. Almost impossible for a reviewer to make much assessment of this, unless they have a study protocol available against which to assess the reporting adherence.

8) Failing to correct for multiple comparisons

Reviewer #1:

– This is a tricky one. The truth is that there is no great consensus amongst statisticians as to the best correction method to use. It is very application area dependent and there are many who would simply disagree on principle that correcting for multiple testing makes any sense (e.g. Rothman, 1990, Epidemiology).

I would draw a distinction between exploratory and confirmatory analyses, and make differing recommendations dependent on the aims of the study. We may be more or less worried about false negatives and false positives in these settings.

This topic is complex and probably beyond the knowledge of most (non-expert) reviewers and beyond the scope of this article.

Reviewer #2:

– 'it is simply unacceptable for the researchers to interpret results that have not survived correction for multiple comparisons' – Even if hypothesised? Perhaps 'exploratory' needs to be added here. I disagree that if an effect 'could' be tested using different comparisons, then corrections for multiple comparisons are required. A reviewer could just say: “well, you could have done this on all the individual blocks of data rather than the subject averages, so you need to correct…” This would be r-hacking (reviewer hacking), and needs to be discouraged. Explicit, limited, pre-registered hypothesis-testing should be encouraged. Exploratory testing is fine, but should be acknowledged and α corrected.

9) Over-interpreting non-significant results

Reviewer #1:

– This is a common error – so common in fact that it is hard to believe anything we suggest will make much difference! The suggestions of the authors are reasonable, but a bit wishy-washy.

Reviewer #2:

– 'non-significant effects could literally mean anything' – So could significant effects. All the problems listed apply equally to significant effects: true positives, over-powered small effects (e.g., much smaller than the meaningful effect that a theory predicts), or ambiguous effects. There is nothing special about the α value, as the authors note.

– 'Otherwise, researchers should not over-interpret non-significant results and only describe them as non-significant.' – So, p=.049 is "significant" and can be interpreted, and p=.051 is "non-significant" and should 'not be over-interpreted'. I think we can do better than this. What rules of thumb do the authors offer to get around this linguistic threshold? My view would be that if there is any doubt in a particular result, then plot the data, check assumptions, run simulations, replicate the experiment with increased power, seek converging evidence, do a systematic review and meta-analysis, present the work at conferences, ask reviewers… Being told to stick rigorously to the 'significant/non-significant' dichotomy is not going to improve the readers' statistical inferences.

– Figure 4 does not show a 'correlation' but two time series data; the right y-axis looks like negative numbers because of the axis ticks; the blue dataset has auto-correlation (mostly the same people eating margarine across different years) but the red does not (mostly different people getting divorced). Since the authors did not create this figure, I suggest removing it from their tutorial. I also suggest they cite primary research data, rather than secondary websites (particularly when that website labels a correlation of r[without degrees of freedom]=.9926 as a '99.26%' correlation. It's not).

10) Correlation and causation

Reviewer #1:

– My sense is that scientists generally have a good understanding of this issue. Not really a statistical issue per se, more about using cautious language when reporting.

Reviewer #2:

– 'Impossibly high correlations' – Replace with 'effect sizes'?

Honourable mentions

Reviewer #1:

– I really don't think section adds much, just a list of terms with little or no more explanation. I would advise deleting.

Conclusions

Reviewer #1:

– Interesting as it is, I don't see why we need a discussion of NHST and p-values as the conclusion. Seems a bit off-topic. A summary of main issues and overlap of the common mistakes and importance would be much more useful. And some recognition of the importance of talking to your statistical colleagues. Most of the issues discussed here are very common issues that all (any) statisticians will be well placed to help with. Whether at study development, writing or reviewing stages of research.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting the revised version of "Ten common inferential mistakes to watch out for when writing or reviewing a manuscript" for consideration by eLife. This version has been seen by the two reviewers who reviewed the original version (Nick Parsons and Nick Holmes), and their comments are below. It should be straightforward to address these comments, so I would like to invite you to submit a second revised version that addresses these comments.

Reviewer #1:

The authors have clearly worked tremendously hard to make changes to the manuscript. It is now quite difficult to read, given all the additions and deletions, so will need a good proof-read to make sure it still makes good sense and scans properly. I make a number of responses to these changes:

Summary:

I still think it is a strange argument to state initially that this paper is motivated by "…ineffective experimental design, inappropriate statistical analysis, and/or flawed reasoning, appearing in published neuroscience papers…", and then to say a little later that all the issues highlighted are "…applicable across a range of scientific disciplines that use statistics to assess findings…". The latter is true – the issues highlighted are very familiar to most applied statisticians who work in science. If there are particular issues that relate to neuroscience – which I imagine there may well be – then that does not come across at all in this manuscript. For me, I think this manuscript would have worked much better if 'neuroscience' had been added to the title and examples and issues specific to neuroscience had been used throughout. Overall, I do not think that this manuscript really delivers on its aim of responding to and talking directly to neuroscience readers. The issues picked-up are the usual suspects; the kind of issues that statistical reviewers and applied statisticians are very familiar with. Nothing wrong with that, per se, but maybe a missed opportunity to do something more impactful. For instance, a survey of the published literature, and description of common reporting and analysis errors would have been an excellent way of motivating this manuscript. Not seriously suggesting that this be done now. But this has proved to be a highly effective way of making real changes to the research culture and the way research is done and reported in other disciplines.

0) Introduction

OK. This is clearly a matter of perspective. I get asked to review papers, with a specific request asking me to look at statistical issues, quite frequently. These often come after requests from non-statistical reviewers who suggest the editor gets a statistician to look at the manuscript.

2) Interpreting comparisons between two effects without directly comparing them

Not really convinced that this is type of "…erroneous inference.…" is "…very common…" in published papers. Almost the first thing we teach in statistics is how to compare group A to group B, using an appropriate statistical test. The error that the authors highlight here feels much more complicated than this; to compare the mean response in two groups, would I really test each against the null hypothesis that the mean is 0, and then conclude if I reject for one group, then I can infer that this group is 'statistically significantly' different to the other group? If this is done, then it is done to deliberately (maliciously) mislead the reader.

4) Spurious correlations

The point I was trying to make about adding confidence intervals seems to have been misunderstood. I would make the general point that, if possible (which it generally is), all point estimates of quantities should be presented with errors; e.g. CIs, range, standard error, bootstrapped intervals etc. The point being that if this had been done for the correlations, then the effect of the outlier on inferences would be much more obvious than it is in a plot that simply presents a point estimate of a correlation as a straight line. The statement that the points in red are clear 'outliers' – presumably because they are a long way from the fitted line – would be much less sustainable as an argument if the line were actually a region of plausible values, given the observed data.

I am absolutely not suggesting that data points should be discarded based simply on post-hoc visualisation of the data. The critical point is that scientists need to always question their own data – and not just at the end of a study when all the data have been collected and they no longer remember why one value is far away from all the others. It is perfectly acceptable to discard values, if there is good reason to believe that something has gone wrong or been recorded incorrectly. This happens all the time – e.g. numbers accidently recorded in the wrong units, calibration not done, days and months confused in dates – there is an almost infinite number of ways that data can be 'wrong'. It is perfectly acceptable to change values such as this – I would advise that the raw data remain unchanged and edits are made in a revised dataset, with changes documented and agreed by all in the study, and made available for others to inspect. If we do this, then what do we make of the data-points the authors highlight as 'outliers'? They are either true errors (things went wrong, but we can't find a reason) or then true data-points. In my view, neither case is a good reason to suggest using robust-correlations, if the rest of the data look reasonably normally distributed. Necessary if you believe the latter is true to modify the model being used, or in the former maybe restrict inferences (model fitting) to the region where you have good data, and not include the extreme value(s).

It is not correct to believe that for instance using a non-parametric method is a solution (good alternative) to a parametric method, in the setting described here. As I stated in my original comment, because values are converted to ranks you simply move the extreme value in Figure 2C closer to the other values. So really what you are doing is saying that you do not believe the data as recorded are correct in the sense that they can be treated in the way that is implied by the plots; i.e. that they are continuous measures, where the distance between them has some sense of measuring the 'closeness' (e.g. Euclidean distance). So if you use a non-parametric correlation you are really saying that you do not believe the value is 'correct'. Ultimately this goes right back to the basics of designing an experiment and writing a statistical analysis plan (SAP) at the start of a study before data collection begins. In that case you need to make clear what your beliefs are about the metric properties of each study outcome – you cannot simply choose to use a non-parametric analysis after the data are collected because that makes life easier. Sorry to labour the point, but this is important, as it goes to the heart of many of the statistical problems in reporting of science.

Reviewer #2:

The commentary/tutorial is more nuanced, fairer, more correct, and thus more publishable. I think it will make a nice addition to a large and very long history of statistical advice to researchers.

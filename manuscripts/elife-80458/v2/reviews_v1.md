# Peer review - Round 1

Editors:
- Taraz Lee, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80458.sa0](https://doi.org/10.7554/eLife.80458.sa0)

This fundamental work provides a comprehensive look at validity of the Proportional Recovery Rule, which states that patients will recover a fixed proportion of lost function after stroke. By undertaking a thorough investigation of the statistical properties of the analysis of change and baseline values the authors elucidate the statistical framework that can be used regardless of the topic of study. In a compelling model comparison across several large sets of data, the authors confirm support for the Proportional Recovery Rule over other models of recovery.


---

# Peer review - Round 1

Editors:
- Taraz Lee, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80458.sa1](https://doi.org/10.7554/eLife.80458.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "The proportional recovery rule redux: Arguments for its biological and predictive relevance" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Howard Bowman (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

The reviewers had significant concerns about both the clarity of the manuscript and the methods employed. They felt that there remained confounds in the analyses that cannot be sufficiently ruled out. Ultimately, there was not sufficient enthusiasm that the manuscript would have broad appeal to the readership of eLife.

Reviewer #2 (Recommendations for the authors):

This paper addresses the inherent potential of motor recovery after stroke. The authors would like to validate the concept of proportional recovery which assumes that stroke patient typically show a fixed amount of recovery of about 70% irrespective of where they start. The authors suggest that after controlling for possibly confounding variables like ceiling effects or mathematical coupling, they still could validate the proportional recovery rule. The Results section is difficult to read for a non-statistician. However, the findings reported in the paper are rather incremental than novel. Most importantly, there are no data that explain the neurobiological basis of proportional recovery. Hence, the novelty of this submission remains low apart from more sophisticated statistical models which ultimately come to a similar conclusion than reported years before.

As stated above, the Results section is very difficult to read and appears somewhat lengthy. Lesion analyses or any other data about the possible neurobiological foundations of the proportional recovery are missing. I acknowledge the relatively large sample size, but the Fugl-Meyer score based view without any further para-clinical evidence is somewhat meager. Therefore, I do not see that this paper has a major impact on the field, as in the best case it confirms the proportional recovery rule which has been published many years before.

Reviewer #3 (Recommendations for the authors):

This paper presents a defence of the proportional recovery theory of how stroke patients with upper limb motor impairments recover. This is a theory that has come under attack due to confounds associated with the analyses used to assess the theory. The paper acknowledges these confounds, which include compression (to ceiling) enhanced mathematical coupling and over-fitting in the differentiation of recovers and non-recovers. The paper then presents a number of methods: use of non-zero nulls; focus on the variance-ratio; bootstrapping to assess variability in parameter and model fits; comparison of model fits; etc. These certainly improve upon the methods classically used in the literature to justify the proportional recovery hypothesis. Additionally, we appreciate the constructive tone of this paper and its effort to arrive at a consensus position on the proportional recovery issue. Indeed, the overall conclusion that there is a proportional (to lost) recovery pattern amongst the moderately impaired group is a position that we have sympathy with, although that pattern is much weaker than some previous claims in the literature.

However, there seem to be remaining problems with the analyses employed, although, it is difficult to definitively judge the methods employed without more detail than the paper currently offers.

The two most important issues that seem to be weaknesses are as follows.

1) Remaining confounds with key measures: Goldsmith et al. argue that particular combinations of correlation between baseline and follow-up, i.e. cor(x,y); correlation between baseline and change, i.e. cor(x,δ); and the variance-ratio, i.e. k, is diagnostic of proportional recovery (PPR). In particular, they argue that the combination of cor(x,y), cor(x,δ) and k shown in table 1 and figure 5 justify their claim that the three datasets they consider, Stinear and Byblow, Winters and Zarahn, definitively exhibit a PPR pattern. However, the simulations presented in Bonkhoff et al. (2020), show that this same combination of measures can be exhibited by a constant recovery model in the presence of ceiling. Indeed, this is the fundamental confound described by Hope et al., Bonkhoff et al. and Bowman et al., which led to the conclusion that the only way the ceiling confound could be avoided is by throwing data points at ceiling away. (This is actually what I believe you should do with the data in this paper. Note, in Bonkhoff et al. (2020), we verified with model recovery simulations that the throwing away procedure enables the correct model to be recovered.) To make this completely clear, I have prepared a figure, which I am assured will be attached with this review.

https://submit.elifesciences.org/eLife_files/2021/09/17/00098237/00/98237_0_attach_15_32737_convrt.pdf

This shows table 1 and figure 5 from Goldsmith et al. on the left and figure 6 from Bonkhoff et al. on the right. I have added annotations to figure 6, which show where the Stinear and Byblow and Winters data sets would sit in the panels for constant recovery. The Zarahn data set does not so obviously correspond to a vertical line, but fits with the general combination of measurements.

2) Limitations of model fits: certainly, the effort to fit models to the three data sets is welcome. However, there is a concern that this model comparison is not a completely fair test of competing theories to proportional recovery. The model fitting comparison in figure 6 is interesting to see. Although, I do find it difficult to interpret the findings, for the following reasons: (a) a criterion has not been given to judge when one model is, in a statistical sense, doing better than another model. I would have expected an assessment of where the MAPE for the best model sits in the bootstrap distribution of MAPEs for each of the other models. This would enable an inference of the kind that the MAPE of the best model is beyond the 95% confidence level of the second best model, and similar for the third. Something of this kind was done in Bonkhoff et al. (2020). (b) I suspect the reason that the Generalised Additive Model does not win is because it is too flexible. It would have been very useful to have seen (perhaps in an appendix) the exact functional form of the Generalised Additive Model. So, I cannot be sure, but I suspect it was not set up to be specifically for saturation at ceiling patterns, with a positive slope leading to a saturation on the right. Consequently, I suspect that the model overfits for many of the bootstrap samples. van der Vliet et al. (2020) give a strong precedent for using a simple exponential, which I suspect would fit the data much better. (c) when I look at figure 4, left panels, lower row, I feel that I do see a strong ceiling pattern in the data. However, this would be much easier to assess if simple x against y (baseline against followup) scatter plots were also presented and model fits for each model were depicted on the scatter plot. This could for example go into an appendix.

van der Vliet, R., Selles, R. W., Andrinopoulou, E. R., Nijland, R., Ribbers, G. M., Frens, M. A., … and Kwakkel, G. (2020). Predicting upper limb motor impairment recovery after stroke: a mixture model. Annals of neurology, 87(3), 383-393.

I have the following more specific comments for the authors.

Abstract: the following statement is made," We describe approaches that can assess associations between baseline and changes from baseline while avoiding artifacts either due to mathematical coupling or regression to the mean due to measurement error". For reasons justified above, and below, I am doubtful that this statement and similar statements made elsewhere in this paper are appropriate.

Introduction section, paragraph beginning "The growing meta-literature discusses …", statement: "the nuanced and sometimes counterintuitive statistical arguments are critical to get right for the sake of furthering our understanding of the biological mechanisms of recovery." I could not agree more than I do with this statement.

Results section, paragraph beginning "A broader argument relates to settings..", with regard to the reference to Bonkhoff et al. (2020) in this paragraph, the reference to "degenerate" is actually most explicitly made in Bowman et al. (2021).

Results section, subsection "Distinguishing true and artifactual signals", paragraph beginning "The value of cor(x, δ) depends on the variance ratio k and..", statement: "The variance ratio can be used as a measure of the extent to which recovery depends on baseline values, regardless of the value of cor(x, y)." As indicated above, if this statement is suggesting that the variance-ratio can be used to unambiguously identify a proportional recovery pattern, we do not agree. Indeed, the variance-ratio could be small even when there is no recovery at all; that is, if the mean at follow-up is the same, or indeed below, the mean at baseline.

Results section, subsection "Distinguishing true and artifactual signals", paragraph beginning "All datasets have x values generated from a Normal distribution…", how is ceiling handled in these simulations – I would have expected that sometimes a followup score there would be, "by chance", above 66. Can you add a explanation of what happens to these?

Results section, subsection "Distinguishing true and artifactual signals", a minor frustration is that the contour plot on the right of figure 1 is the opposite way around to the surface plot in Hope et al., with a baseline by follow-up correlation of one furthest to the right. At the least, could this discrepancy be mentioned in the caption to help the reader.

Results section, subsection "Distinguishing true and artifactual signals", para beginning "Dataset A is a canonical example of mathematical coupling", I am unsure about quite a lot of the points made in this paragraph. It seems to me that a lot of what is said in this paragraph does not sit well with point 1 above.

Results section, subsection "Distinguishing true and artifactual signals", para beginning "Dataset D represents the least controversial..": I would agree that dataset D is a clear example of proportional recovery. However, our central point in previous publications is that on the basis of the methods typically used, including in this paper, that judgment has to be made informally on the basis of visual inspection. This is because one can obtain exactly the same values of statistical measures (r(X,Y), r(x,δ), k), in a dataset without PRR, but which contains a strong ceiling effect, and indeed, datasets do typically exhibit strong ceiling effects; that is, from what I have seen, empirically collected datasets do not typically look like dataset D, because of the ceiling effect.

Results section, subsection "Distinguishing true and artifactual signals", para beginning "Taken together, the..", text: "We also identify a setting, typified by Dataset D, in which each measure suggests the presence of a relevant association. It is not the case that data like these necessarily imply that recovery follows the PRR. Other biological models could produce data similar to Dataset D, and how to compare competing models will be considered in later sections." Just to say, I was a little confused here. What you are saying here seems to be inconsistent with what you said in the previous paragraph in re. what can be deduced from dataset D.

Results section, subsection "Recasting Oldham's method", paragraph beginning "Instead of cor(x + y, x − y), we prefer to focus…": again, some of what is said in this paragraph seems to ignore the confounds that arise from ceiling effects.

Results section, subsection "Correlations, variance ratios, and regression", paragraph beginning "The following expressions relate..", Would it be possible to see a derivation of these two equations? These are not completely standard since \δ = y-x and ii = max-x. This could go in an appendix.

Results section, subsection "Comparing distinct biological models for recovery", paragraph beginning "To illustrate how prediction accuracy…", last sentence: can you give more details of how ceiling is enforced?

Results section, subsection "Comparing distinct biological models for recovery", paragraph beginning "We consider three models for the association …", you say that "Second, we implement the PRR (without intercept) to estimate δ given x, with y taken to be x + δ.", Don't you need to tell us the slope in this eqn, in order to know it is proportional to lost? This is required to rule out proportional to spared or constant recovery. Also, you refer to using a "generalized additive model". Could you give more details of the functional form of this model, perhaps in an appendix? At the least, could you include a relevant reference?

Results section, subsection "Results for reported datasets", paragraph beginning "We next conducted the bootstrap analysis on the subsample…": again, the confound created by ceiling effects impacts this paragraph.

Results section, subsection "Results for reported datasets", paragraph beginning "We compared the performance of three models …": this is where my second point above applies.

Results section, subsection "Results for reported datasets", table 2 caption. Sorry for being dumb, but could you give more explanation of how the R-squared is being calculated here. In particular, could you confirm whether the R-squared equation given in the "Correlations, variance ratios, and regression" subsection is the one being applied here. If it is not this one, can you give the equation that is being used. This is a key issue, since the R-squared values here are much smaller than those given in relevant papers published for some of these data sets.

Results section, subsection "Results for reported datasets", paragraph beginning "The preceding results for …": as previously discussed, the central finding of the work of Hope et al. and Bonkhoff et al. is that, in the presence of ceiling, recovery patterns completely different to the PRR, for example proportional to spared function, can look like PRR, when the measures considered in this paper, cor(\δ, x), cor(x,y), var ratio, are taken. How has the work presented here countered that criticism? I cannot see that it has.

Discussion section, paragraph beginning "Indeed, a recent large-scale cohort study …", it is stated that, "Where Hope et al. (2018) and Bowman et al. (2021) note ceiling effects can compress scores in a way that induces a variance reduction, Lee et al. (2021) observe more than half of all patients, and more than 60% of patients with baseline FMA-UE above 46, recover to the maximum possible value." I do not understand what is being said here. Lee et al. is put in opposition to Hope et al. and Bowman et al., but isn't the Lee et al. ceiling effect going to exactly lead to a reduction in variance at followup?

Discussion section, paragraph beginning "More complex models than the PRR do.." What is being said in this paragraph about Bowman et al. (2020) is not completely clear to me and this may well be a presentational failure on our part when writing Bowman et al. The only place in Bowman et al. (2020) where we refer to mixed models is the following statement, "In particular, van der Vliet et al. present an impressive Bayesian mixture modeling of Fugl-Meyer upper extremity measurements following stroke. Importantly, the authors avoid the confounded correlation of initial scores with change by simply fitting their models to behavioral time-series, that is, raw Fugl-Meyer upper extremity scores, without involving the recovery measure."

However, in the next paragraph, you commend van der Vliet et al. for the same piece of work that we are referring to. Indeed, we were under the impression that the above quoted statement in Bowman et al. (2020), was only a reiteration of what van der Vliet et al. say themselves, which is as follows, "Our current longitudinal mixture model of FM-UE recovery, as opposed to the proportional recovery model, cannot be confounded by mathematical coupling. Hope et al. showed that the correlations between baseline FMUE score (distribution X) and the amount of recovery defined as endpoint FM-UE minus baseline FM-UE (distribution Y-X) found in proportional recovery research could be inflated by mathematical coupling. However, because mathematical coupling applies to correlations of data points (baseline and endpoint FM-UE) and not to models of longitudinal data, the recovery coefficients in our research represent nonconfounded measures of recovery as a proportion of potential recovery. In addition, mathematical coupling does not apply to the outcomes of the cross-validation, as we report correlations between the model predictions and the observed values for endpoint FM-UE and ΔFM-UE rather than correlations of the form X and Y-X."

This leaves us confused, as to what about Bowman et al. (2020) is being criticised in your paragraph beginning "More complex models ….".

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The proportional recovery rule redux: Arguments for its biological and predictive relevance" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed for further consideration, as outlined below:

Essential revisions:

1) Please expand your discussion of the similarities between the current work and previous critiques of the PRR. This should include a brief comment on the justification of some of the analysis choices (e.g. inclusion/exclusion of patients at ceiling) and the relevance of the findings presented here to other areas of research.

2) Address the statistical concerns raised by Reviewer #2

3) Based on some of the reviewers' comments, you may decide to move some of the analyses to a supplement. This is at your discretion.

Reviewer #1 (Recommendations for the authors):

The authors have completed an extensive reworking of their paper, which does a good job of responding to the majority of my comments. Perhaps most importantly, the authors have convincingly countered the argument that I made in my first review that their findings could have arisen from a Constant model with a ceiling. It is excellent to see this rebuttal of my concern. So, I am basically happy with this revision.

It is again good to see the emphasis in this paper on model comparison – that certainly seems to be the right way to go. I also note that the findings in this paper are somewhat consistent with what we have reported in Bonkhoff et al., 2020 – a PRR effect, although considerably weaker than had previously been claimed. So, as the authors point out, there does seem to be convergence in the field, which is excellent.

It remains a pity that the claim that PRR is definitively better on the basis of the presented model fits is still a weak claim. In particular, violin plots for GAM, Exp and PRR are heavily overlapping in figure 6. As you surely know, what is needed is a more sophisticated model comparison, most likely of a Bayesian variety, using something like the model evidence, free energy or deviance information criterion.

The key inference suggested in the paper hinges on an Occams razor argument that if one cannot distinguish between GAM, Exp and PRR, one should pick PRR, since it is more simple. [Although note, I do not believe that Exp is a supermodel of PRR, i.e. I don't think one can get the PRR pattern from Exp, which slightly complicates this line of argument.]

I think that in the absence of a more sophisticated model comparison, of the kind I just highlighted, the Occams razor argument probably is the best one can do. However, since the cross validation is out-of-sample, the flexibility of the model is actually taken into account there.

Obviously, it would be great if this issue could be resolved with a more sophisticated model comparison in a further re-write, however, I don't think this is fair to require at this stage of the review process, but it would be good to acknowledge this weakness in the discussion, and note that competitor approaches are doing better in this respect.

Specific points:

I did not pick this up in the first review, but I spent a lot of time on this review being confused by the right panel of figure 1, which re-represents the surface plot from Hope et al. (2018). I'm now pretty sure your colour bar needs to be inverted. As it is, the yellow contour corresponds to the degenerate region in Hope et al's surface plot, i.e. it does not matter what the value of cor(x,y) is, you always get a correlation of x with change near to -1. However, shouldn't that be for low values of the variability ratio (i.e. log(k) substantially smaller than zero)? Your yellow contour corresponds to log(k) much *bigger* than zero. This issue is also present in Figures 4 and 5.

Top of page 8: "which when baseline (x) and follow-up (y) are uncorrelated and have the same variance." Should the "when" be deleted here?

Page 9, towards bottom: "relationship between of".

Page 10, 2nd para: "data represent in which baseline values".

Page 17, beginning of last para: you talk about there being five models, but in the next sentence you only list 4.

Page 26: you reference Lohse et al. 2021, but I couldn't find this in the bibliography.

Page 38 top of page: there are a couple of typos here. Also, you again talk about there being five models, but in the next sentence you only list 4.

Reviewer #2 (Recommendations for the authors):

1. I think this paper could be made more succinct. It is quite long because the authors used many examples to demonstrate their arguments. Although I feel this approach is well-suited to clinical audience, I am not sure whether the targeted readers may get lost in the technical discussion. For example, I am not sure using bootstrapping is necessary, as we can either directly test the spurious correlation against a more appropriate null hypothesis or using simulation (see the paper in Eur J Oral Sci 2005; 113: 279-288).

2. There are two major issues involving in assessing the relation between change and the baseline. The first is the hypothesis testing and the other is the prediction. Because of mathematical coupling, the usual null hypothesis that the correlation coefficient is zero is inappropriate. This is because the distribution of correlation coefficient is in a restricted space defined by the correlation between x and y, as shown in Figure 1. By the way, I think the paper by Bartko, J. J. and Pettigrew, K. D. (The Teacher's Corner: A Note on the Correlation of Parts with Wholes. Am Stat 22, 41-41, 1968) should be cited, as they are the first to produce such a figure for the correlation between change and the baseline. Another paper of interest is the one by Sutherland, T. M. (The correlation between feed efficiency and rate of gain, a ratio and its denominator. Biometrics 21, 739-749, 1965). Oldham's method is to address this issue of wrong null hypothesis by testing the difference in the variances of X and Y. Other methods are also available as discussed in my previous paper (Tu and Gilthorpe 2007) cited by the authors. As discussed by the authors, Oldham's method or any others based on the same idea has its limitation, if data may be truncated. A possible solution is to design a more sensitive tool to measure the outcome.

3. For the prediction, I think we need to be cautious to use R2 for comparing the performance of different studies. Because R2 is the square of r, i.e. the correlation coefficient. Consequently, the range of R2 is also restricted by the same conditions as r is. Therefore, if different studies have different correlations between X and Y, I do not think their R2 are directly comparable.

4. Moreover, a high R2 does not necessarily mean that patients' recovery can be precisely predicted. Suppose a zero correlation between X and Y, the R2 for using X to predict Y – X will be 0.71^2 = 0.5. Although half of the change's variance can be predicted by the model (i.e. by the baseline value X), this model is useless. This is because R2=0.5 is what we would expect from two sets of random numbers. The baseline and the follow-up values behave like two random variables with zero correlation, this means that X has no use for predicting Y.

5. Regarding to subgroups of patients with different responses, the authors are correct in giving warnings on identifying clusters of patients by using unsupervised methods. Due to regression to the mean, patients with greater baseline diseases are more likely to be identified as good responders, while those with milder diseases are more likely to be identified as poor responders. In fact, the response is actually a continuous spectrum.

6. Finally, I feel a little uneasy that equating the relation between change and the baseline values to the proportional recovery rule. I feel the latter is more akin to the percentage change. Please see the paper: Testing the relation between percentage change and baseline value. Sci Rep 6, 23247 (2016).

I think the authors made great efforts to clarify various misconceptions about testing the relation between change and the baseline. To get your messages across the intended readers, I suggest making your discussion more focused. For example, I do not feel that introducing bootstrapping or GAM is necessary. In contrast, the key concepts of mathematical coupling and regression to the mean were not explained in the paper. In my experience, they are among the most different concepts to comprehend even for statisticians.

Reviewer #3 (Recommendations for the authors):

This is a defence of the Proportional Recovery Rule (PRR), which asserts that stroke survivors recover a fixed proportion of lost function after stroke, from recent, formal/statistical inspired criticisms. The analyses and data show that the PRR is likely to be relevant to ongoing efforts to understand and model post-stroke recovery, and the initial severity of upper limb motor impairments (hemiparesis) after stroke predicts 35-55% of the variance in their subsequent recovery from those deficits.

This manuscript includes a lot of careful analyses that seem reasonable to me and are novel as far as I know in this specific domain. The authors' conclusions also appear to be supported by their methods and data – and their data are impressive, with three large, relevant datasets. I note that other reviewers have identified some detailed issues with the analysis and the text, but in the main the authors have done a very good job of addressing those concerns. The one exception, in my view at least, concerns the best strategy for dealing with patients at or near ceiling in the first two weeks post-stroke. This issue was raised by another reviewer, with whom I co-authored a paper outlining our favoured response, which is to exclude these patients from analyses seeking to quantify the explanatory power of the PRR (Bonkhoff et al., 2021, JNNP). By failing to exclude those acute-near-ceiling patients, the authors have left me somewhat sceptical of the reliability of the variances explained that they report. But this is perhaps more a matter of taste than of statistical rigour, and I can certainly appreciate the authors' reluctance to exclude hard-won empirical data. In their place, I might reference this issue as a possible limitation in the manuscript.

In other words, this paper is not 'broken' in my view, so I have no objection to its publication – and no real requirements for revisions.

That said, I also do not believe that this paper makes a particularly compelling contribution to the field: it 'defeats' a straw man caricature of the criticisms made of the PRR, and offers evidence in support of a position with which even the rule's most critical commentators already agree (and indeed for which some of them have already published supporting evidence).

The original criticism of the PRR was that the analyses used to support it would yield apparently enormous effect sizes entirely regardless of whether the PRR was really relevant to recovery (Hope et al., 2019, Brain). There was never any assertion that the PRR was irrelevant to recovery: that conclusion could never have been justified merely from the recognition that the empirical support for the PRR was unreliable. A follow-up analysis with a large dataset (albeit not as large as that used here) suggested that the PRR was indeed really relevant to recovery, but that it explained a less of the variance in recovery than prior empirical analyses had suggested (Bonkhoff et al., 2020, Brain). That latter work shares much in common with the analyses presented here: i.e., it is a model comparison analysis, with the PRR as one of the considered models. The current work is also a model comparison analysis, with the PRR as one of the considered models, but implemented with different methods and tested against a lot more data. In other words, this paper is in my view a conceptual replication of the earlier study: using different methods and data to run a broadly similar analysis, which yields broadly similar conclusions to those reported previously. Similarly, while the lengthy discussion of clustering is well done, it adds little (in my view) to the conclusions already drawn in Bonkhoff et al., 2022, JNNP.

In other words, much of what this manuscript claims to prove, in response to the critics, has already been reported by some of those same critics. In this sense, the paper is akin to a conceptual replication; using excellent data and novel methods (for the domain at least) to draw conclusions that converge with what has come before, and expressing it all in an accessible manner. These are all strengths in my view: I would merely ask that the links to prior results be made more explicit, at least so that others can follow the timeline of the debate more easily. Or indeed if it's the authors' view that I am wrong, that this be justified more explicitly.

Finally, I am concerned that this issue is rather too narrow to appeal to the readership of eLife. To bolster the more general appeal, I would recommend adding a paragraph or two on variants of this debate that have raged in other subjects – examples of which the authors themselves have given in other papers on this topic.

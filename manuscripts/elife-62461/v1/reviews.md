# Peer review - Round 1

Editors:
- John T Serences, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62461.sa1](https://doi.org/10.7554/eLife.62461.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is paper describes methods to move away from frequentist null hypothesis testing toward a Bayesian approach of estimate the prevalence of within-participant effects. This methodological advance should be widely applicable in many fields, and should promote a more robust evaluation of effects.

Decision letter after peer review:

Thank you for submitting your article "Bayesian inference of population prevalence" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alex Huth (Reviewer #1); Sam Ling (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We will all re-evaluate the manuscript after the re-submission, and I hope the comments below are useful.

Summary:

As you'll see below, the reviewers and I were all enthusiastic about the paper. That said, we all felt that a revision is required to provide concrete examples of when this method is preferred over frequentist approaches, as well as the general types of questions that this method is appropriate for addressing.

In addition, we all felt that the focus of the paper should be expanded to give more attention to non-fMRI studies. For example, there is passing mention in the Discussion section about how this might apply to single unit studies, but that seems more of an afterthought at the moment. Thus, the paper is missing a chance to speak to, and influence, a much broader audience.

Essential revisions:

In addition to revising the text as indicated above (and in the more detailed reviews), it seems likely that some additional simulations may need to be run to address all of the points. This is particularly true of the suggestion to demonstrate a situation where prevalence estimation is more powerful than standard methods.

Reviewer #1 (Recommendations for the authors):

In this paper, Ince and colleagues describe a novel set of Bayesian methods for estimating and working with "population prevalence" of an effect, which they pose as an alternative to NHST on the mean effect in the population. In turns this paper was tantalizing, exciting, and frustrating. I very much want the method the authors propose to be useful, but I was left without a clear sense of (1) what specific questions ("qualitative hypotheses") this method is appropriate for answering, and (2) why (quantitatively) this method should be preferred over others. Specific comments and suggestions are enumerated below.

1. Please show us how prevalence estimation can be more useful than classical approaches! The authors convincingly argued that estimating prevalence amounts to replicating an experiment in each individual subject, a shift in perspective that may help alleviate issues of non-replicability in psychology and neuroimaging (I am very sympathetic to these arguments!). However, it was somewhat frustrating that none of the computational experiments seemed to directly contrast prevalence estimation vs. population mean estimation. If prevalence is indeed a superior way to conceptualize effects in a population, then there should be some experiment where prevalence and population mean give different results for testing the same qualitative hypothesis. For example, in the discussion the authors bring up the issue of uninteresting heterogeneity across subjects, which can reduce the effectiveness of standard approaches (i.e. where the precise anatomical location or timing of an effect is variable across subjects). This paper would be much more convincing if it could experimentally demonstrate a situation like this (in simulation, of course), where prevalence estimation might truly be more powerful than standard methods.

2. Tell us more about what inferences can actually be made using prevalence estimation! The experiment in Figure 1 lays out the differences between prevalence and population mean estimation quite clearly, but the conclusions are much less clear. The authors "suggest that often, if the goal of the analysis is to infer the presence of a causal relationship within individuals in the population, the within-participant perspective may be more appropriate" – but more appropriate for what? Exploring-specifically at this point in the paper-which types of qualitative hypotheses (or some specific examples?) can be meaningfully addressed using prevalence analyses would, in my opinion, greatly strengthen the authors' case.

3. The argument that prevalence estimation is more sensitive to trials per participant than number of participants (Figure 2E) seems circular. The authors define prevalence as the fraction of subjects with "true positive (significant) test results" rather than the fraction where the null hypothesis is actually false, because they can only find a lower bound on the latter measure. Given this definition, the finding that "prevalence greater sensitivity to the number of trials per participant, and less sensitivity to the number of participants" (which is seemingly framed as the main conclusion of the analyses in Figure 2?) is highly unsurprising.

4. How does estimating group differences in prevalence compare to estimating differences in group means? The experiment shown in Figure 3 is tantalizing, but what I really wanted to know here is whether (and under what conditions) comparing groups using prevalence might be more powerful than comparing groups using traditional models.

5. The analysis of prevalence as a function of effect size is missing context and conclusions. Ultimately, I was left without any sense of the utility of estimating prevalence for different effect sizes after reading this section (and Figure 4). What is this specific procedure useful for? What kinds of hypotheses can it test? How does it compare to other methods? Answering these questions would undoubtedly strengthen the paper.

Reviewer #2 (Recommendations for the authors):

This manuscript advocates for a shift in the statistical (and methodological) approaches taken in neuroscience and psychology, wherein effects are considered from the perspective of prevalence, rather than population-centric NHST. They provide simple yet compelling simulations to make their case, and introduce the bayesian prevalence method, along with code to implement on one's own. This manuscript is incredibly well written, the simulations are tightly constructed, and will, I hope, become widely read by the neuroscience and psychology community. It's a straightforward treatment of a statistic that the field needs to consider shifting towards, and the ability to generalize to any NHST will no doubt make this user friendly for most all researchers. I will readily admit that this was a method that my own lab has been in search of for a while, and we plan to deploy this in our own work. Below, I outline my questions/comments, but they are largely meant to support clarification to a broader audience.

1. While the authors promote a Bayesian treatment of the estimate of prevalence, they readily admit that a frequentist approach is suitable as well. It would be worth detailing a bit more the advantages and disadvantages of the two, if any. Particularly because the frequentist approach to neuroimaging has been out in the wild for a while now.

2. The authors simulate individuals within the population as having equal within-subject (or unit) variability. To what degree are the assumptions for prevalence estimation upheld in the case where individual subjects have unequal variance?

3. I assume this rests on the assumption of independence between units of replication (ie subjects, voxels, ROIs, cells). Is this true? And how robust is this method to a lack of independence? I ask because if one were carrying this method out on a voxel-by-voxel basis, within a participant, there's quite a bit of non-independence between these voxels. And likely same goes for between adjacent ROIs, or even between time points. It would be helpful if the authors dedicated some text to this assumption.

4. This comment is more to aid in promotion of the work, but I think the introduction and walkthrough of the simulation would be better serviced by using a case example throughout. It could be a psychophysics example, clinical psych example, or neuroscience example, doesn't matter. I think it would simply help the reader better concretize the reasoning this way. This is entirely up to the authors, but I imagined that the broader audience that they (and I) want to reach would be more likely to engage if this was more explicitly related to their work.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Bayesian inference of population prevalence" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sam Ling (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

This is a paper that describes methods to move away from frequentist null hypothesis testing toward a Bayesian approach of estimate the prevalence of within-participant effects. This methodological advance should be widely applicable in many fields, and should promote a more robust evaluation of effects.

Reviewer #1 (Recommendations for the authors):

In their revised manuscript, Ince and colleagues have added a number of illustrative simulations and clarified several important points, substantially improving the final product. In particular, the simulated EEG analysis (new Figure 2) is an extremely clear and powerful demonstration of the advantages of prevalence estimation over population mean inference for a realistic problem. This is exactly the type of comparison that seemed to be missing in the initial submission, and its inclusion strengthens the paper substantially. The new simulations in Figures 4 and 6 also clarify the related points. Overall, I think the current manuscript is excellent, interesting, and timely.

Here I will respond to two of the authors' points specifically.

Authors: We avoid direct quantitative comparisons because the hypotheses tested (non-zero population mean, vs. posterior estimate of prevalence of within-participant effects) and statistical methods (frequentist vs. Bayesian) are different, although we do invite comparison of the different frequentist p-values (for null of mean zero vs global null of no participants with an effect) for the examples in Figure 1. We focused instead on qualitative arguments in favour of the prevalence view (better match to qualitative hypothesis of interest in psychology and neuroimaging, which we believe should better consider effects within individual behaving brains, and greater robustness given that the effect is shown independently in multiple participants).

This is spot on. The hypotheses tested by these methods are different, but the key question is how these (quantitative) hypotheses map to the implicit, qualitative hypotheses that are actually the subject of inquiry. On the discussion of this point, the current manuscript does not differ substantially from the original. Yet I still found myself much more convinced of its correctness this time around than the first. To this I credit the new simulations that the authors added (Figure 2 and 4). By directly comparing the results of the two methods, these simulations highlight how much better the hypotheses tested by prevalence estimation align with intuitive/qualitative hypotheses than do t-tests.

Minor aside: oddly, I think Figure 1 actually does the authors' arguments something of a disservice on this central point. Yes, it clearly illustrates how the two methods differ. But it presumes a world in which all the assumptions of the hierarchical population mean test are met. This leads to a situation where the standard method matches the reader's expectations (/qualitative hypotheses) much more closely than does the prevalence method. The authors acknowledge the weirdness of the two-sided effects seen in Figure 1B, and point out that this weirdness is actually implicit in the standard hierarchical model, but I worry that by this point the damage is already done. I'm not sure how best to do this – Figure 1 is a very clear illustration of the methods – but it could be worthwhile to consider reorganization that de-prioritizes this simple-but-weird example in favor of less weird examples like Figure 2.

Authors (regarding prevalence as a function of effect size): The main point of this section is to answer the potential criticism that we are dichotomising within participant results and to show that this is not a requirement for valid quantification of population prevalence. Prevalence as a function of effect size gives a fuller picture of the distribution of effect sizes observed. One could argue this is also given by a standard density plot, for example in a violin or raincloud plot, but these are descriptive properties of the specific data sample, without any formal inferential link to the population.

The new simulations shown in Figure 6 certainly clarify this point by showing examples with different underlying population statistics. I'm not specifically asking for anything more – I think this is sufficiently convincing as-is – but I think this would be stronger still with a more concrete example that shows how the prevalence/effect size curve could appear in different real-world situations, with implications for the reader's qualitative hypotheses. For an example like the question posed by Reviewer 2, this curve would look quite different if the individual subject standard deviation was not fixed, but was instead drawn from some distribution. Again, this is not critical, but a more real-world-like example would make this section more convincing.

Reviewer #2 (Recommendations for the authors):

The authors have done an admirable job addressing my questions. I'm eager for this work, which I hope to be influential in the field, to be out in the wild for others to adopt!

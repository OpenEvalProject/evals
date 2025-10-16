# Peer review - Round 1

Editors:
- Geoffrey Schoenbaum, National Institute on Drug Abuse, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56345.sa1](https://doi.org/10.7554/eLife.56345.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this study, the authors tested the ability of humans and rats to track probabilities of reward in a 3-option discrimination task. Paranoia/meth use was associated with worse performance on the task, reflected in fewer reversals in humans and increases in suboptimal win-switch, lose-stay responding, and these tendencies were associated with an increase in the model parameter reflecting phasic volatility and a reduction in the model parameter reflecting contextual volatility. The authors conclude that alterations in perceptions of environmental volatility – uncertainty – may play a significant causal role in paranoia.

Decision letter after peer review:

Thank you for submitting your article "A paranoid style of belief updating across species" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Geoffrey Schoenbaum as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Floris de Lange as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In this study, the authors tested the ability of humans and rats to track probabilities of reward in a 3-option discrimination task. Performance was challenged outright reversal of reward probabilities of the different options (phasic volatility) as well as a shift in the spread of probabilities across blocks (contextual volatility). The effect of different types of volatility on performance were modeled and correlated with paranoia in the humans and with effects of methamphetamine in the rats, the use of which has been associated with paranoia in humans. Paranoia/meth use was associated with worse performance on the task, reflected in fewer reversals in humans and increases in suboptimal win-switch, lose-stay responding, and these tendencies were associated with an increase in the model parameter reflecting phasic volatility and a reduction in the model parameter reflecting contextual volatility. The authors conclude that alterations in perceptions of environmental volatility – uncertainty – may play a significant causal role in paranoia. Overall the reviewers agreed that the paper addressed an important question using an exciting combination of behavior and computational models, and that the results were compelling and potentially important. The main concerns revolved around a desire for more clarity in the presentation and some effort to contrast the current results with other possible models.

Essential revisions:

Key areas of revision were threefold. Together these encompass most of the individual reviewer remarks, which are left below to be addressed rather than reproduced here.

1) Two of the reviewers found it difficult to follow some of the logic and explanations. So the most important revision is to make the specific points raised in the reviews more clear while at the same time simplifying the results to be more digestible for readers who are not computational modelers. This might include removing some experiments, showing more data initially, etc.

2) Remove the rat experiment – it does not really match the others and the paper will be much simpler without it. Of course if the authors disagree, this is their prerogative but in this case it needs to be better explained why the differences are not important. For instance, it is somewhat unclear how the rat behavior can effectively model context volatility as it does not include this in the design. It could also be included as supplemental perhaps.

3) Two reviewers questioned whether the model used is superior to simpler models in interpreting the behavior. Some comparison would be useful to show that the three level model applied is superior.

Reviewer #1:

In this study, the authors tested the ability of humans and rats to track probabilities of reward in a 3-option discrimination task. Performance was challenged outright reversal of reward probabilities of the different options (phasic volatility) as well as a shift in the spread of probabilities across blocks (contextual volatility). The effect of different types of volatility on performance were modeled and correlated with paranoia in the humans and with effects of methamphetamine in the rats, the use of which has been associated with paranoia in humans. Paranoia/meth use was associated with worse performance on the task, reflected in fewer reversals in humans and increases in suboptimal win-switch, lose-stay responding, and these tendencies were associated with an increase in the model parameter reflecting phasic volatility and a reduction in the model parameter reflecting contextual volatility. The authors conclude that alterations in perceptions of environmental volatility – uncertainty – may play a significant causal role in paranoia.

Overall I really like the use of the task variants and modeling to identify links between paranoia and simple learning parameters. I did find it hard to decipher some of the Results sections and the modeling. I think the paper would benefit greatly from being written with more up front handholding for readers who are not well-versed in these concepts. This might be accomplished by laying out more clearly how the different parameters can be understood both intuitively to impact learning/paranoia as well as how they are directly related to behavior in the tasks. This might include presenting more of the behavioral data. Currently all that is presented are the model parameters. It would be more convincing I think if the actual performance was shown from the subjects and then from the model, along with the parameters.

As part of this, I also am not sure the rodent data really fits. I like its inclusion in principle, but the task does not correspond directly to the variants used in humans. Specifically it lacks the shift in context volatility. This seems crucial to me. I think perhaps it might be removed to simplify the presentation. Likewise the task variants that do not include this could be removed.

On an interpretive level, I had two further questions. The first is whether it is possible to reproduced the performance with simpler models? Or how much of an improvement is gained with the use of the more complex model? Beyond this I also wonder if the authors believe that some of the effects might be compensatory – that is if I undertand correctly, they are arguing that there is less of an impact of context volatility on behavior in the experimental subjects. If this is true, it seems to me it might lead to more surprise when there are sudden changes in reward probability when a reversal occurs….?

Reviewer #2:

The authors ran 2 experiments in human subjects (one in the lab, the other online) and re-analysed behavioural data in rats and found that: 1) in humans, paranoid scores are correlated with an impairment in volatility monitoring according to a Bayesian meta-learning framework: 2) in rats meta-amphetamine administration (a pharmacological manipulation that induces paranoia in humans) impairs uncertainty monitoring in a similar way. Overall, I liked this paper; I think it represents an important contribution.

My main questions / suggestions are about the choice model-free metrics and statistical analyses and computational modeling inferences.

1) In Experiment 1, the difference between high/low paranoia is on the “number of reversals” variable. In Experiment 2 (and in the rats) the difference between high/low paranoia (placebo/ meta-amphetamine) is captured by the “win / switch” rate. However, I could not find the “win / switch” rate measure for Experiment 1 and the “number of reversal” metric for Experiment 2. The authors should report the same behavioural metrics for all experiments.

2) Even if expected, the correlation between depression, anxiety and paranoia is a bit annoying. I am convinced that paranoia is the main determinant of the computational effects, but I think the authors could provide some additional evidence that this is the case. A possible solution could be to use a structural equation modeling. Another (possibly better) solution would be to run a PCA on the three scales (the average scores, not necessarily the individual items): my prediction is that the first component will have positive loadings on the three scales and the second will be specific to the paranoia scale. They could then correlate the PCA values instead of the scores of the scales.

3) I think that, in addition to the current model, the authors could also test a simple RL model with different learning rates for positive and negative prediction errors (see Lefebvre et al., NHB, 2017). I think the readers would be interested in knowing these results as the learning rate asymmetry has been shown to correlate with the striatum, as meta-amphetamine affects dopamine and also because in paranoia there seems to be an affective component to paranoia. This analysis could be done in parallel (not in antagonism) of the main model and reported in the SI.

Reviewer #3:

This study takes on the hypothesis that paranoia is actually due to dysfunction in recognizing volatility. They address this through two human experiments (one in-person comparing individuals with and without psychiatric diagnoses; one online using Amazon Mechanical Turk) and a rat experiment in which rats are exposed to methamphetamine or saline. They justify their claims by fitting a model using a Hierarchical Gaussian Filter (HGF) and identifying changes in the underlying parameters, particularly identifying larger priors for higher volatility in the high paranoia group and in the methamphetamine-exposed rats.

The strength of this paper is that it uses a simple task to explore important topics, particularly a transdiagnostic perspective. However, we have several serious problems with the manuscript, including both the communication and the experiments and analysis itself. While we laud the authors for attempting to compare experiments across species, we do not find the rat experiment a good parallel for the human.

Major concerns:

– Overall, it was very difficult to read this paper. Even with multiple read-throughs each and multiple discussions between the reviewers (senior π and graduate student), we are not sure that we understand the manuscript, its goals, or its conclusions. Many of the figures are not referenced in the text (Tables 5 and 9 are never referenced in the paper at all), many of the figures are unclear as to their purpose (what is being plotted in Figure 4?), and many of the figures are very poorly explained (we finally concluded that we are supposed to track colors not position in Figure 3). A careful use of supplemental figures, a better track to the storyline, and better communication overall would improve this paper dramatically.

– The rat experiment is interesting, but it is not a good comparison for the human data. The rat experiment is within-subject, comparing pre and post-manipulation, while the human data is between-subject, comparing high and low paranoia scores. Furthermore, the experiment itself is completely different. While the human experiments had three decks that changed throughout, the rats had two changing and one unchanging deck. We recommend removing the rat experiment.

Unclear concerns

– These Bayesian models (such as the HGF shown in Figure 2) are notoriously unstable. Very small changes can produce dramatically different results. How independent are these variables? Are there other models that can be compared?

– The authors seem to be trying to make the argument that the real issue with paranoia is not the social decision-making process, but rather an underlying issue with measuring volatility (and particularly meta-volatility). As such, the title of the paper should be changed. The important part of this paper (as we understand it) is not the cross-species translation (which is problematic at best), but rather the new model of paranoia as a dysfunction elsewhere than the social sphere.

– The authors need to add citations for using rats exposed to methamphetamine as a model for paranoia. While there appears to be research supporting this method, the authors do not actually cite it. To our knowledge, It is not appropriate to describe methamphetamine as a locus coeruleus disruption or as a change in the noradrenergic gain. Yet, the discussion about the rat experiment seems to be based on noradrenergic gain manipulations.

Specific concerns

– Figure 1: what is the difference between performance independent and performance dependent changes? Explain in figure caption.

– Figure 2B: Once we finally realized that the key to this figure were the colors, we liked that the authors kept the colors consistent across the rats and humans, since the rat comparisons were pre-Rx instead of having two blocks, and therefore likely indistinguishable from the low-paranoia group pre-Rx. However, it makes comparison of the figures confusing, because we expect the comparisons across the figures to mean the same thing to compare the outcomes. This figure requires much better and clearer explanations.

– Figure 3: Is there a reason that the authors expected version 3 to be significant over version 4? Why might the order of context change matter (or not matter)?

– Figure 4: This figure is confusing and at the moment does not provide additional understanding of the results. Consider relabeling and adjusting figure caption to explain what is in the figure and move the results to the Results section or display in a table (or both), or otherwise remove it in total.

– Figure 5 seems important, but shouldn't we see this for all of the important variables? We thought the argument was primarily about metavolatility rather than phasic volatility coupling.

– Figure 7 is important, but was poorly labeled and mostly impenetrable. In particular, panel a is completely unclear. There are no labels, no explanation for colors or any other components. What is the difference between simulated and "recovered" parameters?

– Figure 8 claims a replication between in-person and online, but the online appear significant, while the in-person do not.

– Figures 9 and 10 are impenetrable. What is this cluster analysis and how is it done?

– Figure 11 seems more appropriate to a supplemental figure.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A paranoid style of belief updating across species" for further consideration by eLife. Your revised article has been evaluated by Floris de Lange (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance. In particular, while the concerns of reviewer 1 and 2 were addressed, and the manuscript is markedly improved in terms of clarity, reviewer 3 still has some remaining requests. They are described below.

Reviewer #1:

The authors have addressed my concerns.

Reviewer #2:

The authors successfully addressed my concerns.

Reviewer #3:

Overall, the paper is much clearer in its explanation of the design, analyses, and simulations. The authors have also made a clearer argument for including the rat data. However, we believe they still need to explicitly state the limitations of the human and rat experiments. Additionally, the graphs still need to be brought up to the level of clarity of the writing (particularly Figure 7). In summary, the authors have successfully clarified many questions about the analyses and conclusions of the paper, yet additional work is needed surrounding the rat vs. human experimental comparisons.

Major concerns:

– The title needs to be changed, as it is misleading regarding the findings. What seems to be the main argument is that paranoia-like behaviors are evident in belief-updating outside of a social lens, so perhaps something clearer could be something about how paranoia may arise from belief-updating, rather than social cognition. For example, we recommend a title such as "Paranoia may arise from general problems in belief-updating rather than specific social cognition" or something like that.

– Add a paragraph outlining the limitations of cross-species comparison, particularly the fact that the rats are compared within subject, while the humans are compared between subjects.

– The social nature of rats is heavily debated, and while we know they are not as social as humans, there may be some sociality for the rats. Nevertheless, the task is still asocial, and therefore assists the argument of the paper. However, if the authors are going to discuss that rats are asocial animals, we think they should include a paragraph discussing the support for and against this statement, and relate it to the asocial nature of the task. Along with this argument, please mention how rats were housed, which speaks to their sociality.

– Figure 7 has not been adequately addressed from the first round of revisions. It is still largely impenetrable. For instance, what is the left side of 7A? What are the lines? Can you describe what "choice trajectory" is? Phrases like "the purple shaded errobars indicate…" would be very helpful to the reader.

– In general, the figures need more work. Fonts are too small (particularly Figure 4), which makes it difficult to really interpret the graphs. Along with that, many of the graphs have a lot of panels and not a lot of text to describe what each of the panels means. Thorough explication of the figures would improve the paper tremendously.

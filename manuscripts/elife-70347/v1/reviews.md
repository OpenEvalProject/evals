# Peer review - Round 1

Editors:
- Niel Hens, https://ror.org/04nbhqj75 Hasselt University Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70347.sa0](https://doi.org/10.7554/eLife.70347.sa0)

The authors perform experimental infections with rabbits to study how coinfection with one or more helminths affects the shedding of the respiratory bacterium Bordetella bronchiseptica. The results show that shedding varies strongly from one individual to the next and that co-infections with helminths lead to increased levels of shedding. The authors nicely combine within-host kinetics modelling and their longitudinal data to estimate key parameter values associated with bacterium and immune growth rates in the four conditions. These suggest that the shedding differences can be explained by differences in bacterial growth.


---

# Peer review - Round 1

Editors:
- Niel Hens, https://ror.org/04nbhqj75 Hasselt University Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70347.sa1](https://doi.org/10.7554/eLife.70347.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Gastrointestinal helminths increase Bordetella bronchiseptica shedding and host variation in supershedding" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Samuel Alizon (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors present their results in the context of "supershedding" and, more generally, the idea that the variance in the number of secondary infections caused by an individual (i.e. R0) can matter in addition to the mean. Indeed, as popularized by Lloyd-Smith et al. (2005), even if the mean R0 is constant, an increased heterogeneity between individuals will affect disease emergence and spread. The authors appear to be presenting their work in this context and I agree that co-infections could be increasing the level of individual variation. However, in their results (and even more generally in the context of co-infections), I am not sure this is appropriate because it appears to me that the main consequence of the co-infection is to increase the mean of the distribution (rabbits shed more bacterial) rather than its heterogeneity (the proportion of rabbits that do not shed bacteria remains comparable with co-infections). If the authors really wish to keep the focus on the importance of heterogeneity, they should show that it matters and, for instance, estimate the heterogeneity parameter k of a negative binomial distribution (or a similar distribution) for the distribution of shedding rates (in Figure 3), assuming that this reflects individual R0. The other option is to focus on the mean value instead of heterogeneity, which I think can be done without loss for the integrity of the manuscript.

2) From Table 1, it appears that the authors are estimating at least 27 parameters using the model. This seems like a lot and the large confidence intervals make me wonder whether the model is identifiable. I am unsure this can be shown using likelihood profiles given the number of parameters but perhaps this could be studied by simulating datasets and calculating the mean relative error associated with the inference.

3) The authors mention model comparison in passing but given the number of parameters I think it might be worth exploring this in more details, especially since co-infections seem to be leading to similar patterns.

4) More is needed in the paragraph starting on line 309. The fact that neutrophils are produced during infections by both helminth species makes the explanation in lines 315-317 seem unconvincing. Why do the neutrophils have a different impact in the two helminth infections, and could it be related to different dynamics of helminth growth in the two species? The authors mention work in mice (Rolin et al.) that seems to show a different pattern of neutrophil dynamics and impact-should readers interpret that as merely differences between the immune responses of mice and rabbits, and if so, what differences are most likely? Possibly related to these points, it might be good to emphasize here that the model used did not account for differences in helminth infection intensity-would accounting for those differences in a future model be likely to shed light on the role of neutrophils?

5) More explanation would be helpful in a couple of places, especially regarding the dynamics in B. bronchiseptica singly infected hosts (lines 208-211). The text makes it sound like the data are just not informative as to where the peak is, but it seems clear that the peak occurred at or before the start of sampling. I was surprised that the peak was earlier for the single infections, where bacteria are thought to be replicating more slowly. Naively, I thought that with a slower replication rate, the peak would be later. How do the authors interpret that finding? Is it the case that the single infections are growing slower and also brought under control faster, resulting in an earlier peak than the double and triple infections.

6) The authors should pay particular attention to the specific comments raised as part of the public review and of course all remaining comments in a point-to-point reply.

Recommendations for the authors:

Reviewer #1:

lines 2-3: This sentence is a bit misleading because in Lloyd-Smith et al. the R0 is attributed to the individual.

Figure 1: The numbers on the top of each panel are unclear (I guess they refer to weeks?).

line 147-148: Is it an increase in shedding or in the likelihood to shed?

line 512-514: The writing is clear but I think the manuscript could gain in clarity by discussing a bit more within-host kinetics modelling, which is barely mentioned. Furthermore, regarding the model itself, modelling the immune response is more common now than it was 20 years ago, there are still many different models. For instance, here immune activation is assumed to depend only on parasite load. Referring to earlier models that made similar assumptions would help.

line 561-562: Do you need to make some assumptions regarding the independence of the variables to obtain the final likelihood function in equation 12?

Figure 6: It would be nice to also show in Figure 6 the within-host time series resulting from the model parameter inference and not only the "growth rates" (which are actually a bit unclear). This is already in Figure S1 but I think it would really improve the study.

Instead, showing likelihood profiles in the Appendix might be a good idea.

Reviewer #2:

Some modifications to the language (especially removing jargon and adding further explanation in places) would help make study accessible to a broader audience. For example, the phrase "rapid variation in individual shedding" (abstract) requires more explanation-perhaps "rapid temporal changes in individual shedding" would be clearer? Another example is line 96, where it seems strange to say that "events were null", and it might be more accessible to say that rabbits did not shed at many time points even though they were known to be infected and interacted with the petri dish (assuming I understood that correctly).

Lines 241-245 are confusing, starting with the phrase "negative bacterial growth". Assuming I'm interpreting the words in line 244 as a sharp decline in bacterial abundance, what does it mean to say that "the zero time to reach this peak were represented by the initial inoculum"?

I didn't get a lot out of Figures 7 and 8. The authors might consider moving these figures to the supplement, but regardless it would be helpful to include both parameter symbols and names/brief definitions on the x-axis labels or at the very least in the caption.

Reviewer #3:

Abstract, first two sentences. These sentences are a bit awkward. The authors should consider recasting them.

Abstract, "Model simulations revealed…". This makes no sense as written: simulations by themselves cannot tell us anything about the real world. Please revise this sentence to more accurately characterize the relationship between the data, the conclusions, and the model simulations.

Abstract, "…the rapid variation in individual shedding…". This sentence is very unclear.

Author Summary, line 2. Consider replacing "underline" with "underlie".

Author Summary, "experiments of rabbits together with mathematical modeling". It reads as though the experiments involved rabbits doing math!

Author Summary: "at the host level, …". This sentence is unclear. The authors should revisit it, and perhaps reconsider whether it belongs in the Author Summary.

When "type 1" and "type 2" are first introduced, they should be explained. At least, it should be made clear that "type 1" refers to Th1, etc.

ll 36ff. The connection between B. bronchiseptica and pertussis is tenuous and essentially irrelevant in this context. More generally, there is neither need nor value in this tangent.

Paragraph beginning on l 45. There are a number of facts mentioned here that are not obviously related to the authors' argument. The authors should consider whether these facts belong here. If they decide that they do belong, they should explain how.

ll 56ff. The authors describe some modeling work as if it were evidence. On the face of it, this is absurd. I recommend that they consider whether these sentences are needed, or contribute, to their study. If they conclude that they do, they should revise these sentences to put the earlier modeling work in context.

l 65. I find it strange that the authors jump from the experimental design immediately into the modeling without first describing the data that they generated.

l 72. Simulations cannot, by themselves, explain anything. Moreover, it requires great imagination to interpret the authors' model as "mechanistic".

l 80. "…every week or multiple times a week." This is most vague; the authors should be more precise.

l 91. Why was a nonparametric (Wilcoxon) test used? Does the result change if a parametric (e.g. t) test is used? Are there reasons to avoid such parametric tests? If so, what are they?

ll 93-95. Are the reported differences in median (?) shedding rate among the arms statistically significant? The broad and overlapping confidence intervals suggest not.

ll 105-111. This discussion is confusing and unclear.

ll 276-279. This is speculation, which is not in itself a problem, but it should be labeled as such.

ll 440-443. The choice of sampling times seems arbitrary. Can the authors describe the rationale behind these choices a bit more carefully.

l 449. "exemplifies" → "mimics".

ll 452-455. Explain the logistical constraints and technical difficulties.

ll 468, 470. This is an unwarranted conclusion. The authors should more carefully describe the conclusions that can be drawn from the cited study. In particular, the modeling study rests on strong assumptions about the underlying immunology.

l 568. "Weakly normal prior". "Weakness" is a relative term: the authors should describe the precise form of the priors they assume.

Figures:

Figure 1. There are several problems with this data visualization. First, it makes the "Alabama First" error, whereby the data are arranged according to an irrelevant variable (in this case, animal number within date-of-sacrifice). Second, the boxplots are not appropriate in many cases, since the data are too few or too non-normal. Third, the arbitrariness inherent in the log(1+CFU/s) metric makes it hard to interpret. I cannot confidently recommend any single visualization that will correct these problems: it will probably be necessary for the authors to experiment with, for example, simpler scatterplots, violin plots, and other approaches, before they find a more satisfactory plot or set of plots.

It may be that this figure is attempting to do too much. It seeks to convey information about the stereotypical time-course of infection and about the intra- and inter-animal variability, as well as the variation in both of these with coinfection. It might be helpful to design several figures that tackle each of the above individually.

Figure 2. This figure suffers from some of the same problems as Figure 1. In addition, there is too much cramping and overplotting to distinguish the individual-animal traces. The use of log(1+CFU/s) is problematic. Since the authors are using a zero-inflated model, it seems that the zeros don't belong here.

Finally, and at least as worryingly, the trends (smoothed curves) do not appear to represent the data at all. That is, the trends are not typical. Inasmuch as these median values are the point of contact with the models, this is quite problematic: it seems likely that even if the best-fitting models explain these averages well, they fail to represent any of the individual animals well.

Figure 3. Again, the log(1+CFU/s) metric is problematic. With a different, equally arbitrary, choice of time unit, the shape of these histograms might change appreciably.

ll 64ff. The authors appear to have made choices about the inclusion and exclusion of animals on an ad hoc basis. On its face, this raises questions about the reproducibility and reliability of their conclusions. However, it is strange that they have done so, since their zero-inflated model affords them a principled way of including all animals.

Figure S1 ought to be moved into the main text.

Figure 6. The model does not appear to do a good job in capturing the data. In particular, the individual traces and the overall trend appear to be biased downwards. This may be due to the presence of zeros in the data. If this is the case, then it is puzzling why the authors do not employ their zero-inflated model to focus attention on the non-zero data. Their choice instead to use log(1+CFU/s) is problematic in its own right as well, as discussed above.

This figure also suffers from the same problems as Figure 2: the individual data are not resolved and the individual model trajectories are too crowded.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Gastrointestinal helminths increase Bordetella bronchiseptica shedding and host variation in supershedding" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

First set of remaining issues:

Figure 1-Could the authors include an x-axis label? I assume that would be something along the lines of rabbit ID.

Figures 2, 5, and 7: could the x-axis labels be fixed so that they are all legible? Also in Figure 5, the dark blue line is difficult to see against the thinner black lines.

The paragraph in lines 244-272 could use further proofreading since some phrases are difficult to parse, including "somehow represented by the infection dose" and "shedding was not statistically significant among the three groups".

Line 322-omit "prompted" or rephrase (meaning unclear).

Second set of remaining issues:

162 onwards and 335 – the definition of supershedding raises an interesting point – as noted here, supershedding is usually thought of as the maximum shedding however duration of shedding is an important component as well. Does it change the outcome at all, if the threshold was defined in terms of the integrated shedding profile?

172 Figure 2. I realise these are complex data to represent compactly, but I find it hard to follow the individual trajectories (e.g. to determine if single infections are consistently different from each other). Perhaps a few example trajectories in different colours might help?

Line 191 – Figure 3. It is hard to tell, but it looks like the negative binomial is a reasonable representation of the BT infections but that there may be greater systematic biases for the BG and BTG cases. Is this true and if so, statistically significant?

448 – I would be slightly more reserved about making a definitive statement on the impact of measured super-shedding in an experimental setting, an undefined use of 'contact' and the probability of it resulting in infection and/or a greater number of infections. There is a good chance they are right, but that's not quite the same as proving it.

684 and 932 onwards. Very good to see the convergence plots – it would be helpful also have the scale reduction factors, as its difficult see in the plots what the individual chains are actually doing – based on the text it should be fine, but having the results recorded would be useful.

902 – Good to see figures showing posterior estimates here – I much prefer them to tables. I do generally find it helpful to have figures showing the posterior distribution, preferably in correlation plots to show at least some of the interdependencies between parameters which is particularly important given the number of parameters involved. I realise it would add considerably to the appendix to show more detail for each individual, however, so long as it doesn't misrepresent the variation between individuals, I think an averaged correlation plot across all posteriors would be helpful.

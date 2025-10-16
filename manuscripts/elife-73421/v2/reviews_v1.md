# Peer review - Round 1

Editors:
- Joseph F Cheer, https://ror.org/04rq5mt64 University of Maryland School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73421.sa0](https://doi.org/10.7554/eLife.73421.sa0)

This paper evaluated the lasting effects of acute social isolation on future social interactions in juvenile mice, revealing a compelling oxytocin-mediated mechanism. A clear hypothesis has been laid out within a defined anatomical framework, and social interactions were evaluated using appropriate behavioral paradigms, chemogenetic, and pharmacological tools. The work provides new insights on oxytocin signaling as a key regulator of the neural substrates underlying enduring effects of social interaction.


---

# Peer review - Round 1

Editors:
- Joseph F Cheer, https://ror.org/04rq5mt64 University of Maryland School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73421.sa1](https://doi.org/10.7554/eLife.73421.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Oxytocin neurons control the effects of social isolation via the mesocortical pathway" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michy Kelly (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. In addition to addressing the concerns raised in the public review, please address each of the essential revisions provided below.

Essential revisions:

1) All reviewers noted that the lack of females profoundly lessen the impact of the findings. Ideally, all experiments would need to be conducted in females. However, the reviewers understand that this may not be feasible depending on the availability of animals and staffing levels. If this is the case, it is strongly recommended that the authors at the least acknowledge this significant shortcoming and add extensive discussion related to the effect of oxytocin in females (please see Caldwell, Curr. Op. Behavior. Sci, 2018).

2) There was consensus among the reviewers that the statistical analyses are not appropriate for the experimental design and this also needs to be addressed thoroughly. In particular:

a. Parametric statistics are based on assumptions of normality and equal variance, yet only a test of normality is mentioned and only for t-tests and one way ANOVAs. It is stated that normality was assumed for datasets requiring multifactorial ANOVAs. Please assess each dataset for both normality and equal variance before using parametric statistics. 2way ANOVAs frequently fail one or the other assumption, thus necessitating the employ of multiple non-parametric tests to assess the various factors (or, alternatively, a non-parametric multifactorial ANOVA if you have access to custom analysis software). This is a particular concern because in many datasets, variance appears to systematically increase with increasing mean (usually a sign of failed equal variance).

b. Throughout the manuscript, 2-way ANOVAs are reported for behavioral tasks where 2-way repeated measure ANOVAs should have been used (e.g., in the case of tasks tracking performance in the same subject across multiple compartments or objects). In the ephys data, 2 WAY RM ANOVA were used as appropriate; however, it is surprising there was not a significant interaction for many of those experiments (i.e., only main effects were reported) given the distinct overlap at "0". Was the "0" data not included in the RM ANOVA?

c. Throughout the manuscript, only main effects are reported when a significant interaction between effects would be required for the post hoc testing conducted and conclusions drawn. For example, in Figure 1G, the main effect of chamber that is reported says that across the experimental groups, novel > familiar. To statistically make a conclusion that the group vs isolated mice performed differently, you would need a significant interaction between chamber x housing condition to justify the post hoc tests examining the effect of chamber within group housed and chamber within isolated mice. In Figure 1J as well, you are trying to conclude the housing conditions perform differently across days. But to say that, the 2way rm would need to yield a significant interaction of housing condition x day to warrant a post hoc analysis of days within group housed and days within isolated. Again, this is not limited to Figure 1, I just use them here as examples.

d. Many 2-way ANOVAs have fractional df's reported. In the case of linear models, it is my understanding df's should be whole numbers, so it is not clear why dfs are presented in many 2way analyses as decimals (e.g., "2.027, 20.27). I believe in more complicated analyses, unequal variances can yield fractional df's, but in the case of unequal variance, a non-parametric statistic should be employed. Would you please clarify or revise?

e. The method of data presentation in Figure 1 S2 is not clear. Typically, "preference index" is a single number that incorporates relative preference for a novel object as a function of total time of exploration (=n-f/n+f). I do not believe it would be statistically appropriate to compare normalized data for ob1 vs ob2 because the combined value of both factors would be the same between groups (i.e., there could be no effect of group). The more typical way of analyzing these data is to compare the preference index for the novel object between the group vs. isolated mice to determine if there is a group effect, and then to conduct a one-sample t-test for each group's index vs.5 to determine if they exhibited significant memory (i.e., an index that differed significantly from chance). The authors may refer to the following paper for guidance:

https://www.sciencedirect.com/science/article/pii/S1074742714000070. If you were to analyze the raw seconds of exploration, then you could do a paired analyses of O1 vs O2, that said, the analysis should be a 2factor RM with housing condition vs object as factors. The same applies to the analyses of closed vs open arms.

f. Legend for Figure 3L is missing the post hoc analyses to say which group is different from which. Further, it seems equal variance could possibly fail given that variability increases in parallel with the increases mean (also with study in 3D).

g. In Figure 3 S1B, was there not a significant interaction? It seems there is an effect of increasing intensity within the no CNO group, but not the CNO group. Note that a significant interaction overrides main effects as it states that the effect of one factor depends on the level of the other factor.

3) It is not clear how oxytocin neurons were identified in Figure 3 S1. With current details provided, it appears that recordings of all PVN neurons (non-oxytocin neurons as well) were obtained in mice; please clarify. Moreover, cFOS+ and Oxt+ coexpression images are needed to relate the increase in the activity of PVN (via the IEG proxy) and the density of Oxt+ cells in PVN (figure 3 and page 4, line 11-17). Also, please clarify whether neurons are increasing Oxt production to become more efficiently labeled or changing identity of their synthesized neuropeptides?

4) Although it is reasonable to suggest that the lack of preference for the novel mouse and the failure to habituate to a mouse could reflect a reduced preference for novelty (and is that because they are less motivated to explore novel social stimuli or because they find social stimuli less rewarding?). This could also/alternatively reflect a social learning and/or memory deficit (they fail to form a memory of the first-presented mouse). To disentangle these seemingly opposite consequences, typically habituation sessions are conducted for a longer period of time and behavior examined across time within the same day (e.g., Hedge et al., 2016, Neuroscience https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5031549/).

5) The extensive and definitive use of the term "social craving" throughout is unjustified based on the data presented (e.g., there is no breakpoint data shown). Craving implies having experienced something that is rewarding and wanting more of it; however, these mice never experienced any social interactions with non-cagemates, so how can they crave it? To this end, it might be informative to test these behaviors using cage mates as stimulus mice.

6) Regarding the statement "Indeed, we could speculate that social isolation during adolescence results in an intense urge to interact with whatever conspecific is present." This can be tested in a straightforward fashion by using cage mates as stimulus mice, or measuring interactions in the home cage, instead of using novel mice.

7) It is important to clarify why stimulus mice were 1 week younger and whether this is this true for adolescent and adult studies? This is of particular relevance because in the adult study illustrations, a small (seemingly juvenile) mouse is drawn--which would suggest much more than 1 week younger in the case of testing adults. If adults were tested with juvenile mice, as the illustration implies, it complicates interpretation of the adult isolation study since the differential effect of isolation may not be related to the period of isolation but rather a fundamentally different preference between adolescent and adult mice for other juvenile mice.

8) The authors identified putative DA neurons based on position, morphology, and capacitance, while providing sparse details in the methods. This section should contain detailed information and/or a small post hoc immunohistochemistry validated dataset.

9) The authors have exclusively shown scaled-up excitatory responses by pharmacologically blocking GABAA receptors, determining synaptic scaling after social isolation without considering potential effects on inhibitory post synaptic responses. Please provide prediction for the latter. Furthermore, it is not clear if synaptic scaling reported in Figure 5 induced by adolescent isolation only emerges slowly in the adult, or it is already acutely happening at the end of isolation at p35. Please discuss in detail.

10) It is unclear how oxytocin neuron activity contributes to synaptic plasticity onto VTA-NAc projections. One possibility is that oxytocin expressing PVN neurons projecting to VTA also release glutamate and contribute to the synaptic plasticity. It would be informative to optogenetically examine the synaptic connectivity between PVN->VTA projections and VTA->NAc projection neurons.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Oxytocin neurons mediate the effect of social isolation via the VTA circuits" for further consideration by eLife. Your revised article has been evaluated by Kate Wassum (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1) Please acknowledge the lack of females as a shortcoming of the study and provide more discussion of this limitation; e.g., that differences in the system in males vs females and how these findings here may only apply to the male brain. Please also state the sex of the subjects in the abstract.

2) The post hoc analyses referred to in 2f of the letter are still missing. The statistical interaction was reported, but the post hoc tests were not, nor were significance markers added to the figure to indicate at which pA the groups differ.

3) Please make sure all statistics are reported. For instance, in some cases a 2 way ANOVA was used but only one main effect is reported.

https://reviewer.elifesciences.org/author-guide/full "Report exact p-values wherever possible alongside the summary statistics and 95% confidence intervals. These should be reported for all key questions and not only when the p-value is less than 0.05."

4) As isolated mice show increased social interaction during direct social interaction, but not during the 3 chamber sociability assay, it is important to more thoroughly explore why isolated mice show different outcomes between these two tests. To better understand the cause of increased direct social interaction (social craving vs aggression), it would be informative to conduct additional behavioral testings from isolated mice (e.g. social CPP, aggression assay). If new behavior testing data such as social CPP or aggression assay (resident intruder etc) is not possible, at the very least a more detailed behavioral characterization such as chasing during free social interaction test is needed to address this concern and better distinguish craving vs aggressive encounter. Overall, more careful consideration is required to interpret the nature social behavior in isolated mice captured by free social interaction and 3 chamber task.

5) The response to essential review 2c to statistically compare between groups was not fully addressed. [Results] page 1, lines 18-19 and Figure 1EF. To evaluate if the house condition modifies the sociability, it is essential to run these statistics for Figure 1HI. Related to this, the 3 chamber testing data should be presented and analyzed in a similar way across different sets of data. E.g., Figure 1 HI are missing center chamber time and the preference index data while all the rest of the 3 chamber data include these.

In general, more clarity on whether or not the 3-chamber social preference test results do or do not support the conclusion of social isolation leading to an increase in social interaction would help. E.g., by clarifying whether isolation leads to an increase in social interaction specifically in "free/unrestrained"social interactions in adulthood.

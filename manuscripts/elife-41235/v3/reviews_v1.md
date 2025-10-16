# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41235.030](https://doi.org/10.7554/eLife.41235.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Statistical structure of locomotion and its modulation by odors" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ronald L Calabrese as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, the authors present a creative analysis of fly walking in response to an attractive odor (apple cider vinegar, ACV) in circular arena in the dark and where odor can be strictly limited to a central zone. They monitor fly movement as velocity (parallel and perpendicular to prior movement) prior to and after odor is introduced to the arena center. They then analyze the data with a Hidden Markov Model (HMM) and a Hidden Hierarchal Markov Model (HHMM) and show decisively that the HHMM fits the data better and that the high level sates (HL) describe stereotypical locomotor components and that transitions between them vary in probability such that states with similar velocities have higher transition probability. They then show that introduction of odor affects the probability that a given HL state is occupied and varies inside and outside the odor zone with final spatial structure. A surprising finding is that the average probability distributions of the HL states cannot be used to determine the presence of the odor. Subdividing the flies according to their individual pre and during odor probability distributions and clustering reveal 3-4 categories of responses and there are different cluster of the 34 flies tested for each of the four conditions (pre inside odor zone, pre outside odor zone, during inside odor zone, during outside odor zone). The most interesting conclusions of the paper are: 1) the observation that the HHMM model fits better than the HMM model, implies that there is structure at multiple time scales in the data 2) under the specific conditions imposed that although all flies in dataset use the same set of locomotor features, individual flies vary considerably in how often they employ a given locomotor feature (HL state), and how this usage is modulated by odor. The paper should arouse general interest in the behavioral neuroscience community.

Essential revisions:

1) There are concerns about how well the data constrains particular HHMM put forward that can be allayed by putting confidence intervals on the probability distributions of Figure 5 and Figure 6.

2) Several of the reviewer concerns focus on dwell times in each HL state. These dwell time should be analyzed and distributions presented and interpreted.

3) The observation that the HHMM model fits better than the HMM model, implies that there is structure at multiple time scales in the data. For example, HL states may be prolonged because the systems transitions among nearby LL states within the HL state; is this supported by the dwell time of LL states within a prolonged HL state? The authors also note in the Discussion that there is structure on longer time scales. Can they think of some analysis that would pull this out?

4) The findings about individuality and the fact that the presence of odor can be predicted from a model that takes individuality into account but not from a model that does not are interesting. Here however, some additional analyses or data would help support the claim. For example, can the authors compare the distribution of states early versus late in the trial and show that each individual still occupies a characteristic set of states? How do HL state dwell times vary among individual or early vs. late in a trial? Would more flies analyzed and/or for longer period of time help resolve the individuality issues?

5) The detailed reviewer comments are appended and that should be addressed in light of the consensus concerns above.

Reviewer #1:

Concerns

1) Subsection “A small number of strategies can explain the variability in flies’ response to odor” third paragraph: be explicitly clear as to how many clusters were found for each case illustrated in Figure 9. In Figure 9A, I assume there were at least 5 clusters but that cluster 4 had less than 4 flies; were there other clusters? Be very clear as to the number of clusters for Figure 9A and 9B.

2) Results section: you state in results that flies "…spend 60% of time performing a locomotor feature for >300 milliseconds, and >10% of their time performing a single locomotor feature for >3s (Figure 2—figure supplement 1)”. The first statement appears compatible with the cumulative distribution in the figure, but I don't see the second at all. Am I missing something or is the maximum duration illustrated 1.5 s and less that 5% of states are of this duration or longer? Please plot in a supplemental figure the real distribution of time duration of states in the data. These data are essential if you are to make claims like "These locomotor characteristics can persist over 3 seconds – a time period during which a fly takes 30 steps on average (given a step frequency of 10 Hz). This tight control over 𝑣̂|| over tens of steps strongly suggests that locomotion unfolds, not on a step-by-step basis, but in blocks of tens of steps." Or like "A fly moves at a relatively constant 𝑣̂|| and 𝑣̂⫠ for tens of step." It seems for example, that for states that last 300 ms that only 3 steps are possible and there are many states that last shorter periods. Are moving states distributed in duration longer/shorter that stopping states?

3) Subsection “Odors affect behavior on a fine spatial scale.”, paragraph two: Here you are creating a sequence of behavior based on averages and YET you claim that average data does not describe a fly's behavior but there are distinct strategies. Please clarify.

Reviewer #2:

1) The model assumes that behavior is best modeled as set of discrete states (with the implication, I think, that this is how they are controlled neurally). The alternative possibility, alluded to briefly in subsection “Flies show considerable variability in locomotion despite employing the same locomotor features.”, is that some parts of the behavior could be better represented (or controlled) as continua. Since velocity is a continuous 1D variable, and since the fly must pass through intermediate velocities to transition from low to high velocity and vice-versa, I think this alternative should be considered. I am not suggesting the authors entirely revamp their model but I think this point could be discussed or considered a bit more prominently.

2) In the analysis of spatial structure (Figure 6), the role of time history should be considered/discussed. For example, behavior near the odor border might be different because the fly is more likely to have experienced no odor shortly before odor (or vice versa) than in the center of the arena. The responses of olfactory neurons are well known to show responses that depend on history over multiple time scales, so this point should be considered/discussed. Whether behavior could also be influenced by airflow at different parts of the chamber should be noted (without assuming the reader knows the details of the earlier paper). For example, could the airflow from the vacuum be causing the flies to slow down inside the odorized area, as in Yorozu et al., 2009?

3) The findings about individuality are quite interesting. As mentioned above, the analysis in which the presence of odor can be predicted based on individual flies or clusters of flies, but not the whole dataset is quite interesting. However, as the authors note in the response to Reviewer 3, individuality in responses has also been investigated elsewhere. A typical analysis in these studies (de Bivort, Branson) is to compare behavior of the same individual at different time points and to show that they are more similar to themselves than to each other. The authors might consider splitting their data in time and repeating the analysis, although the time interval of the data here is relatively short (6 min). In addition, it would be nice to know if they could correlate their clusters with anything else about the flies. In the response to reviewers the authors allude to different behaviors produced by different genotypes. I think it would add to the interest of the study if these data were included.

4) The comparison of HMM and HHMM models is nicely rigorous but seems highly technical for this journal. The authors should consider focusing the text on the conceptual conclusions that can be drawn from this comparison.

Reviewer #3:

Before publication some work is needed to address questions about: 1) how to interpret HL behaviors (survival time statistics of HL states and relationship to the structure of a 10HL-5LL model); 2) error bars.

Main comments:

Error bars.

I could not get a clear sense of how well the data is constraining the HHMM model. For example in Figure 5, what is the uncertainty of these distributions? Can the authors bootstrap the data? Likewise in Figure 6 how many data points go in each colored dot? What is the uncertainty of the probability plots as a function of radial distance? There are no error bars on these plots.

Time spent in HLs.

One of the reasons HHMM seems to work better than HMM is that behaviors have extended durations and since the trajectory can jump around the LL states within a single HL state, that HL state can last long. Even though this is a key aspect of the model, there is no analysis or plot of the waiting time distribution in each HL state that would give an idea of the "duration" of such states during behavior and how that duration depends on the number of HL and LL states used in the HHMM model. The only thing I could find was Figure 2—figure supplement 1 (but this includes all states) and the statement made: "A fly moves at a relatively constant 𝑣̂|| and 𝑣̂⫠ for tens of step. This tendency means that a fly's locomotion can be decomposed into a small number of locomotor features – 10 features in the case of the model we present.". However, this main conclusion is provided without plots about it. Supporting this point with quantitative data analysis is important because the authors use it to interpret various aspect of the results. It is also important to know if some HLs state last much longer than other in order to interpret the data. This may also clarify why 10HLs each with 5LLs are used in the HHMM. See below.

Subsection " HHMM reveals that a fly’s locomotion is surprisingly structured in the velocity space…".

An interesting outcome underlined by the authors (last paragraph) is that the resulting HHMM accounts for 80% of all the data (within 85% confidence interval) using 10 locomotor features (10 HLs). Some of the HL states correspond to clearly distinct behavior, such as 1=meander, 2=stop-to-walk or 9=fast right turn, 10=fast left turn. However, other HLs seem to be part of a continuum, such as 4,5,7= medium speed walking, and it is not entirely clear why 3 distinct HLs are needed to describe medium speed walking. Some HLs seem to fit less well the data, e.g. HL 6. I could not find a clear explanation of why 10HLs each with 5LLs were chosen and whether fewer HLs would have worked as well. What would happen if the HHMM had less HL nodes but more LL nodes in each HL? A discussion of survival times in each HLs might help sort this out and provide a way to interpret states 4,5,7. Are these different behaviors or one behavior distributed over 3 HL?

Subsection “Locomotor features and implications for neural control of behavior”.

In the discussion the authors say that v_parallel lies within a narrow range that is distinct for each three state and that 3 states reflect a tight control on locomotion by the brain. They mention these locomotor state can persist up to 3 second/30 steps and suggest that this indicates that the brain controls locomotion in blocks of 10 steps. I find this conclusion drawn from the finding of these 3 clusters too speculative given the data: In Figure 3—figure supplement 1 and Figure 4 the distributions of v_par overlap significantly between HL 4,5 and 7. This is again related to the two points above. Finally, if HL 4 5 7 are really distinct behaviors then another possibility could be that they are needed to account for fly-to-fly variability in the data, and that for a single fly only one state is sufficient to describe medium speed walk.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Statistical structure of locomotion and its modulation by odors" for further consideration at eLife. Your revised article has been favorably evaluated by K VijayRaghavan (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Significant additional revisions are still required. The comments of the expert reviewers, below, are detailed and require full responses.

Reviewer #2:

This manuscript compares HMM and HHMM approaches to clustering behavioral data from flies in an olfactory paradigm. Based on a rigorous comparison of models, the authors conclude that the HHMM model performs better than the HMM model, implying the presence of hierarchical long-time scale structure in the data. They further analyze the behavior of individual flies and show that responses to odor cannot be understood in terms of variation around an "average fly" but rather are better understood as belonging to 3-4 response types. Response types of individuals are stable over the duration of the experiment. Overall the methods introduced for analyzing complex behavioral data appear to be sound and are likely to be of broad interest to scientists studying natural behavior and its neural correlates.

Two points need to be addressed before acceptance:

1) How do the priors used in fitting constrain the structure of the transition matrices found for the models? In the Results section, the authors state that "the assumption of Markov dynamics with a sparse prior on state transitions penalizes the consideration of unlikely state transitions base upon recent history and future destinations." This suggests that a sparse prior was applied in fitting. However, later in the paper the authors state: "The transition probability matrix for the HMM was sparse, suggesting that from each state there are transitions to only a handful of other states." If a sparse prior was applied during fitting than the fact that the resulting transition matrix is sparse is not really a finding about the data.

Similarly, the authors need to clarify what fitting priors or constraints were placed in the HHMM model. The Results state "This is because any HHMM- which puts very specific constraints on the transitions probability matrix- can be represented by an HMM but not vice-versa." What are the constraints on the transition probability matrix for the HHMM? The text says "The transition probability matrix is sparse- a vast majority of transitions from each HL state were to 2-3 other HL states." Was this imposed by fitting priors?

2) Parts of the manuscript are somewhat long and repetitive. I think the manuscript could be productively shortened to have greater impact on its readers.

For example, in the section titled "HHMM reveals that a fly's locomotion is surprisingly structured in the velocity space" the last paragraph is devoted to restating the major conclusion of the first section: HHMM performs better than HMM. I think this could be reduced or folded into section one, which focusses on this comparison, and the section focused more exclusively on describing the HL states uncovered by the model.

In the Discussion subsection “Flies show considerable variability in locomotion despite employing the same locomotor features” paragraphs two and three are highly descriptive of the individual fly data and somewhat repetitive with parts of the Results subsection “Both locomotion and an odor’s effect on locomotion is fly dependent” (already rather long). I think these sections could be condensed to make the major points about individual variability in the Results, and use the Discussion mostly to compare these findings with the results of other studies.

Reviewer #3:

The authors have addressed most of my concerns expect the important one regarding the confidence interval on the distributions in Figure 5. What I am asking is for the authors to use bootstrapping to extract many sample distributions from subsets of the data in order to get a confidence interval on how these bins are populated by the data and how significant the changes are between before and during odor exposure.

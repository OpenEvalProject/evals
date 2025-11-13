# Peer review - Round 1

Editors:
- Matthew PH Gardner, Concordia University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105347.3.sa0](https://doi.org/10.7554/eLife.105347.3.sa0)

This valuable study employs a formalized computational model of learning to assess memory deficits in Alzheimer's Disease with the goal of developing an early diagnosis tool. Using an established mouse model of the disease, the authors studied multiple behavioral tasks and ages with the goal of showing similarities in behavioral deficits across tasks. Using the model, the authors indicate specific deficits in memory (overgeneralization and over differentiation) in mice with the transgene for the disease. The evidence presented is solid, yet certain concerns remain regarding the interpretation of the results of the modeling.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105347.3.sa1](https://doi.org/10.7554/eLife.105347.3.sa1)

I applaud the authors' for providing a thorough response to my comments from the first round of review. The authors' have addressed the points I raised on the interpretation of the behavioral results as well as the validation of the model (fit to the data) by conducting new analyses, acknowledging the limitations where required and providing important counterpoints. As a result of this process, the manuscript has considerably improved. I have no further comments and recommend this manuscript for publication.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105347.3.sa2](https://doi.org/10.7554/eLife.105347.3.sa2)

Summary:

This manuscript proposes that the use of a latent cause model for assessment of memory-based tasks may provide improved early detection in Alzheimer's Disease as well as more differentiated mapping of behavior to underlying causes. To test the validity of this model, the authors use a previously described knock-in mouse model of AD and subject the mice to several behaviors to determine whether the latent cause model may provide informative predictions regarding changes in the observed behaviors. They include a well-established fear learning paradigm in which distinct memories are believed to compete for control of behavior. More specifically, it's been observed that animals undergoing fear learning and subsequent fear extinction develop two separate memories for the acquisition phase and the extinction phase, such that the extinction does not simply 'erase' the previously acquired memory. Many models of learning require the addition of a separate context or state to be added during the extinction phase and are typically modeled by assuming the existence of a new state at the time of extinction. The Niv research group, Gershman et al. 2017, have shown that the use of a latent cause model applied to this behavior can elegantly predict the formation of latent states based on a Bayesian approach, and that these latent states can facilitate the persistence of the acquisition and extinction memory independently. The authors of this manuscript leverage this approach to test whether deficits in production of the internal states, or the inference and learning of those states, may be disrupted in knock-in mice that show both a build-up of amyloid-beta plaques and a deterioration in memory as the mice age.

Strengths:

I think the authors' proposal to leverage the latent cause model and test whether it can lead to improved assessments in an animal model of AD is a promising approach for bridging the gap between clinical and basic research. The authors use a promising mouse model and apply this to a paradigm in which the behavior and neurobiology are relatively well understood - an ideal situation for assessing how a disease state may impact both the neurobiology and behavior. The latent cause model has the potential to better connect observed behavior to underlying causes and may pave a road for improved mapping of changes in behavior to neurobiological mechanisms in diseases such as AD.

The authors also compare the latent cause model to the Rescorla-Wagner model and a latent state model allowing for better assessment of the latent cause model as a strong model for assessing reinstatement.

Weaknesses:

I have several substantial concerns which I've detailed below. These include important details on how the behavior was analyzed, how the model was used to assess the behavior, and the interpretations that have been made based on the model.A (the putative acquisition memory), increases, partially leading to reinstatement. This does not appear to be the case as test 3 (day 36) appears to have similar posterior probabilities for A as well as similar weights for the CS as compared to the last days of extinction. Rather, the model appears to mainly modify the weights in the most recent latent cause, B - the putative the 'extinction state', during reinstatement. The authors suggest that previous experimental data have indicated that spontaneous recovery or reinstatement effects are due to an interaction of the acquisition and extinction memory. These studies have shown that conditioned responding at a later time point after extinction is likely due to a balance between the acquisition memory and the extinction memory, and that this balance can shift towards the acquisition memory naturally during spontaneous recovery, or through artificial activation of the acquisition memory or inhibition of the extinction memory (see Lacagnina et al. for example). Here the authors show that the same latent cause learned during extinction, B, appears to dominate during the learning phase of reinstatement, with rapid learning to the context - the weight for the context goes up substantially on day 35 - in B. This latent cause, B, dominates at the reinstatement test, and due to the increased associative strength between the context and shock, there is a strong CR. For the simulation shown in figure 1, it's not clear why a latent cause model is necessary for this behavior. This leads to the next point.

(1) There is substantial data to suggest that during fear learning in mice separate memories develop for the acquisition and extinction phases, with the acquisition memory becoming more strongly retrieved during spontaneous recovery and reinstatement. The Gershman paper, cited by the authors, shows how the latent causal model can predict this shift in latent causes by allowing for the priors to decay over time, thereby increasing the posterior of the acquisition memory at the time of spontaneous recovery. In this manuscript, the authors suggest a similar mechanism of action for reinstatement, yet the model does not appear to return to the acquisition memory after reinstatement, at least based on the simulation and examples shown in figures 1 and 3. More specifically, in figure 1, the authors indicate that the posterior probability of the latent cause, zA (the putative acquisition memory), increases, partially leading to reinstatement. This does not appear to be the case as test 3 (day 36) appears to have similar posterior probabilities for zA as well as similar weights for the CS as compared to the last days of extinction. Rather, the model appears to mainly modify the weights in the most recent latent cause, zB - the putative the 'extinction state', during reinstatement. The authors suggest that previous experimental data have indicated that spontaneous recovery or reinstatement effects are due to an interaction of the acquisition and extinction memory. These studies have shown that conditioned responding at a later time point after extinction is likely due to a balance between the acquisition memory and the extinction memory, and that this balance can shift towards the acquisition memory naturally during spontaneous recovery, or through artificial activation of the acquisition memory or inhibition of the extinction memory (see Lacagnina et al. for example). Here the authors show that the same latent cause learned during extinction, zB, appears to dominate during the learning phase of reinstatement, with rapid learning to the context - the weight for the context goes up substantially on day 35 - in zB. This latent cause, zB, dominates at the reinstatement test, and due to the increased associative strength between the context and shock, there is a strong CR. For the simulation shown in figure 1, it's not clear why a latent cause model is necessary for this behavior. This leads to the next point.

(2) The authors compared the latent cause model to the Rescorla-Wagner model. This is very commendable, particularly since the latent cause model builds upon the RW model, so it can serve as an ideal test for whether a more simplified model can adequately predict the behavior. The authors show that the RW model cannot successfully predict the increased CR during reinstatement (Appendix figure 1). Yet there are some issues with the way the authors have implemented this comparison:

(2A) The RW model is a simplified version of the latent cause model and so should be treated as a nested model when testing, or at a minimum, the number of parameters should be taken into account when comparing the models using a method such as the Bayesian Information Criterion, BIC.

(2B) The RW model provides the associative strength between stimuli and does not necessarily require a linear relationship between V and the CR. This is the case in the original RW model as well as in the LCM. To allow for better comparison between the models, the authors should be modeling the CR in the same manner (using the same probit function) in both models. In fact, there are many instances in which a sigmoid has been applied to RW associative strengths to predict CRs. I would recommend modeling CRs in the RW as if there is just one latent cause. Or perhaps run the analysis for the LCM with just one latent cause - this would effectively reduce the LCM to RW and keep any other assumptions identical across the models.B, the extinction memory, it may be possible to replicate the pattern of results without requiring a latent cause model. For example, the 12-month-old App NL-G-F mice behavior may have a deficit in learning about the context. Within the RW model, if the alpha for context is set to zero for those mice, but kept higher for the other groups, say alpha_context = 0.8, the authors could potentially observe the same pattern of discrimination indices in figure 2G and 2H at test. Because the authors don't explicitly state which parameters might be driving the change in the DI, the authors should show in some way that their results cannot simply be due to poor contextual learning in the 12 month old App NL-G-F mice, as this can presumably be predicted by the RW model. The authors' model fits using RW don't show this, but this is because they don't consider this possibility that the alpha for context might be disrupted in the 12-month-old App NL-G-F mice. Of course, using the RW model with these alphas won't lead to as nice of fits of the behavior across acquisition, extinction, and reinstatement as the authors' LCM, the number of parameters are substantially reduced in the RW model. Yet the important pattern of the DI would be replicated with the RW model (if I'm not mistaken), which is the important test for assessment of reinstatement.

(2C) In the paper, the model fits for the alphas in the RW model are the same across the groups. Were the alphas for the two models kept as free variables? This is an important question as it gets back to the first point raised. Because the modeling of the reinstatement behavior with the LCM appears to be mainly driven by latent cause zB, the extinction memory, it may be possible to replicate the pattern of results without requiring a latent cause model. For example, the 12-month-old App NL-G-F mice behavior may have a deficit in learning about the context. Within the RW model, if the alpha for context is set to zero for those mice, but kept higher for the other groups, say alpha_context = 0.8, the authors could potentially observe the same pattern of discrimination indices in figure 2G and 2H at test. Because the authors don't explicitly state which parameters might be driving the change in the DI, the authors should show in some way that their results cannot simply be due to poor contextual learning in the 12 month old App NL-G-F mice, as this can presumably be predicted by the RW model. The authors' model fits using RW don't show this, but this is because they don't consider this possibility that the alpha for context might be disrupted in the 12-month-old App NL-G-F mice. Of course, using the RW model with these alphas won't lead to as nice of fits of the behavior across acquisition, extinction, and reinstatement as the authors' LCM, the number of parameters are substantially reduced in the RW model. Yet the important pattern of the DI would be replicated with the RW model (if I'm not mistaken), which is the important test for assessment of reinstatement.

(3) As stated by the authors in the introduction, the advantage of the fear learning approach is that the memory is modified across the acquisition-extinction-reinstatement phases. Although perhaps not explicitly stated by the authors, the post-reinstatement test (test 3) is the crucial test for whether there is reactivation of a previously stored memory, with the general argument being that the reinvigorated response to the CS can't simply be explained by relearning the CS-US pairing, because re-exposure the US alone leads to increase response to the CS at test. Of course there are several explanations for why this may occur, particularly when also considering the context as a stimulus. This is what I understood to be the justification for the use of a model, such as the latent cause model, that may better capture and compare these possibilities within a single framework. As such, it is critical to look at the level of responding to both the context alone and to the CS. It appears that the authors only look at the percent freezing during the CS, and it is not clear whether this is due to the contextual-US learning during the US re-exposure or to increased responding to the CS - presumably caused by reactivation of the acquisition memory. The authors do perform a comparison between the preCS and CS period, but it is not clear whether this is taken into account in the LCM. For example, the instance of the model shown in figure 1 indicates that the 'extinction cause', or cause z6, develops a strong weight for the context during the reinstatement phase of presenting the shock alone. This state then leads to increased freezing during the final CS probe test as shown in the figure. If they haven't already, I think the authors must somehow incorporate these different phases (CS vs ITI) into their model, particularly since this type of memory retrieval that depends on assessing latent states is specifically why the authors justified using the latent causal model. In more precise terms, it's not clear whether the authors incorporate a preCS/ITI period each day the cue is presented as a vector of just the context in addition to the CS period in which the vector contains both the context and the CS. Based on the description, it seemed to me that they only model the CRs during the CS period on days when the CS is presented, and thereby the context is only ever modeled on its own (as just the context by itself in the vector) on extinction days when the CS is not presented. If they are modeling both timepoints each day that the CS I presented, then I would recommend explicitly stating this in the methods section.

(4) The authors fit the model using all data points across acquisition and learning. As one of the other reviewers has highlighted, it appears that there is a high chance for overfitting the data with the LCM. Of course, this would result in much better fits than models with substantially fewer free parameters, such as the RW model. As mentioned above, the authors should use a method that takes into account the number of parameters, such as the BIC.

(5) The authors have stated that they do not think the Barnes maze task can be modeled with the LCM. Whether or not this is the case, if the authors do not model this data with the LCM, the Barnes maze data doesn't appear valuable to the main hypothesis. The authors suggest that more sophisticated models such as the LCM may be beneficial for early detection of diseases such as Alzheimer's, so the Barnes maze data is not valuable for providing evidence of this hypothesis. Rather, the authors make an argument that the memory deficits in the Barnes maze mimic the reinstatement effects providing support that memory is disrupted similarly in these mice. Although, the authors state that the deficits in memory retrieval are similar across the two tasks, the authors are not explicit as to the precise deficits in memory retrieval in the reinstatement task - it's a combination of overgeneralizing latent causes during acquisition, poor learning rate, over differentiation of the stimuli.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105347.3.sa3](https://doi.org/10.7554/eLife.105347.3.sa3)

Summary:

This paper seeks to identify underlying mechanisms contributing to memory deficits observed in Alzheimer's disease (AD) mouse models. By understanding these mechanisms, they hope to uncover insights into subtle cognitive changes early in AD to inform interventions for early-stage decline.

Strengths:

The paper provides a comprehensive exploration of memory deficits in an AD mouse model, covering early and late stages of the disease. The experimental design was robust, confirming age-dependent increases in Aβ plaque accumulation in the AD model mice and using multiple behavior tasks that collectively highlighted difficulties in maintaining multiple competing memory cues, with deficits most pronounced in older mice.

In the fear acquisition, extinction, and reinstatement task, AD model mice exhibited a significantly higher fear response after acquisition compared to controls, as well as a greater drop in fear response during reinstatement. These findings suggest that AD mice struggle to retain the fear memory associated with the conditioned stimulus, with the group differences being more pronounced in the older mice.

In the reversal Barnes maze task, the AD model mice displayed a tendency to explore the maze perimeter rather than the two potential target holes, indicating a failure to integrate multiple memory cues into their strategy. This contrasted with the control mice, which used the more confirmatory strategy of focusing on the two target holes. Despite this, the AD mice were quicker to reach the target hole, suggesting that their impairments were specific to memory retrieval rather than basic task performance.

The authors strengthened their findings by analyzing their data with a leading computational model, which describes how animals balance competing memories. They found that AD mice showed somewhat of a contradiction: a tendency to both treat trials as more alike than they are (lower α) and similar stimuli as more distinct than they are (lower σx) compared to controls.

Weaknesses:

While conceptually solid, the model struggles to fit the data and to support the key hypothesis about AD mice's inability to retain competing memories. These issues are evident in Figure 3:

(1) The model misses trends in the data, including the gradual learning of fear in all groups during acquisition, the absence of a fear response at the start of the experiment, and the faster return of fear during reinstatement compared to the gradual learning of fear during acquisition. It also underestimates the increase in fear at the start of day 2 of extinction, particularly in controls.

(2) The model explains the higher fear response in controls during reinstatement largely through a stronger association to the context formed during the unsignaled shock phase, rather than to any memory of the conditioned stimulus from acquisition (as seen in Figure 3C). In the experiment, however, this memory does seem to be important for explaining the higher fear response in controls during reinstatement (as seen in Author Response Figure 3). The model does show a necessary condition for memory retrieval, which is that controls rely more on the latent causes from acquisition. But this alone is not sufficient, since the associations within that cause may have been overwritten during extinction. The Rescorla-Wagner model illustrates this point: it too uses the latent cause from acquisition (as it only ever uses a single cause across phases) but does not retain the original stimulus-shock memory, updating and overwriting it continuously. Similarly, the latent cause model may reuse a cause from acquisition without preserving its original stimulus-shock association.

These issues lead to potential overinterpretation of the model parameters. The differences in α and σx are being used to make claims about cognitive processes (e.g., overgeneralization vs. over differentiation), but the model itself does not appear to capture these processes accurately.

The authors could benefit from a model that better matches the data and captures the retention and retrieval of fear memories across phases. While they explored alternatives, including the Rescorla-Wagner model and a latent state model, these showed no meaningful improvement in fit. This highlights a broader issue: these models are well-motivated but may not fully capture observed behavior.

Conclusion:

Overall, the data support the authors' hypothesis that AD model mice struggle to retain competing memories, with the effect becoming more pronounced with age. While I believe the right computational model could highlight these differences, the current models fall short in doing so.

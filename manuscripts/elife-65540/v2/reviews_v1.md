# Peer review - Round 1

Editors:
- Redmond G O'Connell, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65540.sa0](https://doi.org/10.7554/eLife.65540.sa0)

The authors conducted an impressive study investigating dynamic adjustments in decision policies as a function of two types of uncertainty: decision conflict and volatility (change point probability). They combine learning model parameters with drift diffusion modeling to assess how the policy (as a combination of drift rate and threshold) varies with uncertainty and also test how these adjustments relate to the LC-NE system via pupil diameter. This work is impressive and will certainly be of interest to many.


---

# Peer review - Round 1

Editors:
- Redmond G O'Connell, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65540.sa1](https://doi.org/10.7554/eLife.65540.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Dynamic decision policy reconfiguration under outcome uncertainty" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Floris de Lange as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Redmond O'Connell (Reviewer #1), Niels A Kloosterman (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors should rewrite sections of the manuscript to more clearly articulate for the reader the core theoretical questions that this study sets out to address. Beyond linking elements of choice uncertainty to parameters of an influential decision model, what were the study goals and why are they important/interesting? Similarly, the authors should clarify the broader implications of their findings for current theory and future research. In addition, the Results section is very long and at times it is hard to follow the rationale for each analysis step or how it relates to the study goals. The authors might consider moving certain details that are not essential to the Methods or Supplemental Materials.

2) The reviewers agreed that the DDM analyses seem overly restricted, being limited to only two parameters when there are other parameters of this model that can plausibly mediate the observed uncertainty effects. The authors make strong claims about the specific nature of the decision policy adjustments observed here but this interpretation would be greatly strengthened if the authors examined model variants that leave other parameters (e.g. non-decision time, drift bias). Please also provide some illustration of the fits to individual data.

3) Several concerns were raised regarding the pupillometry analyses.

a) First, there is a concern that any underlying relationships with choice strategy may have been obscured if the task stimuli evoked strong pupil light reflexes (constrictions) within the measurement window. This cannot be properly assessed without the authors providing plots of the average pupil diameter timecourses along with details regarding the stimuli (e.g. brightness).

b) Second, the authors appear to overlook several relevant metrics. This includes unbaselined prestimulus pupil diameter which has been linked to variations in choice performance in a number of investigations and also to exploration/exploitation switches in at least one report (Jepma and Nieuwenhuis 2011). Previous work has also shown that the LC-NE system is in fact better tracked by using the first time derivative of the pupil signal (Reimer et al., Nat Comm, 2016). The authors should consider looking at the pupil derivative to see if this reveals a link to their experimental manipulations. Importantly, using the derivative instead of the actual pupil time series attenuates the pupil light reflect since only the slope is taken.

c) Third, the authors should check whether they can replicate the relationships between uncertainty and pupil diameter that have been reported in the previous literature. This would go a long way toward confirming the validity both of their pupil data and the null result in the relationship with exploration/exploitation

The authors should also take note of the individual comments of the reviewers provided below as many additional suggestions are provided that should help further improve the manuscript.

Reviewer #1:

In this paper the authors seek to uncover the decision policy adjustments that underpin participants choices on a two-armed bandit task in which the relative reward and probability of reward associated with each alternative varied unpredictably over time. In an extensive modelling analysis the authors examined whether decision dynamics on this task could be understood in terms of adjustments to the bound and/or drift rate parameters of the drift diffusion model. The results indicate that when participants detect a change in which of two choice alternatives is most rewarding they switch from an exploitative to an exploratory decision strategy by lowering both the bound and drift rate of the decision process. My sense is that these findings are supported by extensive analyses reported in the paper.

1. I note that the authors allowed only one decision model parameter to map on to volatility and conflict. It would be interesting to know whether or not allowing either bound or drift rate to account for both volatility and conflict would improve the model fits.

2. The paper also reports a failure to detect any relationship between pupillary responses (here used as a proxy for noradrenergic arousal) during decision making and the aforementioned decision policy adjustments. Here the authors should cite the work of Joshi et al. (2016, Neuron) which, to my knowledge, was the first peer-reviewed paper to report a relationship between locus coeruleus activity and pupil diameter. This paper is also important to consider because they report a failure to observe the tonic/phasic firing modes originally reported by Aston-Jones and colleagues that form the basis for the present hypotheses.

3. The prior literature suggests that there are important functional distinctions between average absolute (i.e. unbaselined) pupil diameter measured in a given time window and the pupil dilation responses that are elicited during decision making. The authors do not consider the former which has been linked to exploration/exploitation strategies at least once in the prior literature (Jepma and Nieuwenhuis, 2011, J Cog Neuro) and which has been linked to variations in choice performance on several occasions (e.g. Murphy et al. 2011, Psychophysiology; Van Kempen et al. 2019, eLife). The authors then conducted a principal component analysis on 7 different metrics extracted from the stimulus-evoked pupil dilation response.

4. Aside from the desire to reduce dimensionality a clear rationale for this approach is not provided. This limits the ability to compare the present results to those in the related literature since most previous studies have investigated relationships between choice behaviour and metrics like pupil dilation amplitude, peak latency and onset latency individually.

5. The manuscript would benefit from more clearly articulating the theoretical advances/insights that it provides. It could be argued that the modelling work results in a situation where one set of cognitive constructs (change point detection and value estimation) are swapped for another set (bound and drift rate) but it is not clear what new understanding is gained from this.

Reviewer #2:

In the present study the authors investigated decision-policy adjustments as a function of two distinct forms of uncertainty, conflict and volatility. They extend previous studies on explore-exploit dynamics by investigating specifically how choice parameters in an evidence accumulation framework vary with uncertainty.

To that aim they experimentally manipulated conflict and volatility in a two armed bandit task and combined bayesian models of learning with evidence accumulation models of decision-making. Then they quantify the degree to which the relationship between estimated choice parameters – indexing the choice policy – varies as a function of the context in which the choice is made. They further recorded pupil diameters to index LC-NE activity and test whether policy adjustments are related to this activity

Choice conflict modulated the rate of evidence accumulation and change points – while also increasing conflict – decreased the boundary height, leading to fast exploratory choices. The authors show that choice dynamics are linked to uncertainty dynamics by driving systematic changes in the decision-policy characterized by the combination of drift rate and threshold. Fast increases in uncertainty following change points drove fast exploratory choices (low drift rate, low threshold) that gradually recovered to exploitatory choices as the new reward contingencies were learned (high drift rate, high threshold).

They further find no evidence that these changes relate to fluctuations in the LC-NE system as indexed with pupil diameter.

This work is methodologically very impressive and theoretically very interesting. It expands the space of decision-policies beyond the explore-exploit dichotomy and characterizes elegantly how decision-policies should dynamically vary along a two-dimensional policy space as the environment is found to change.

Overall, I really liked the study. I do however have some questions and suggestions for additional analyses and edits.

Questions:

1. Typically more similar options/conflict leads to longer RTs. In Exp 1 the authors find no effect and in Exp 2 the opposite. That's usually a pretty robust effect. Any idea why that's not the case here?

2. Also how does this square with the positive effect of ΔB on drift rate? I think that might be worth picking up and unpacking a bit, if only to show the superiority of model-based analyses to raw behavior given that the behavioral findings are super confusing and the parameter results make perfect sense.

3. Could that be some power issue (re number of subjects, not observations)? Is maybe one subject weird in exp. 2 and can't detect change points so well or track the values?

4. What is meant by the similar time course of belief updating for high and low volatility? (p 5 line 178) Shouldn't people update more under higher volatility? Is that what's captured in the change point probability parameter? Maybe that sentence could be clarified so it doesn't confuse readers familiar with work linking volatility and the α parameter in RL (as in more learning/updating under high volatility).

5. If I understand correctly, when change point probability goes up, ΔB always goes down. What's the correlation between the two and if there is a correlation, what does that mean for the impact of those learning parameters on decision parameters? Can you assess conflict effects independent of change point effects (are there period where values are stable and super similar)?

Suggestions:

6. Provide a clearer rationale for the model comparisons to test hypotheses about policy adjustments.

I honestly found it a bit difficult to follow the model comparison for theta. I also think that when the pupil is added, the rationale could be explained a bit more clearly to allow the reader to follow. Specifically I got confused about the intercept and time null models (is that just time or time relative to change point if the latter, why is that a null model?).

7. Replicate relationship between uncertainty parameters and pupil measures before linking it to policy adjustments.

As I understand, you find that the adjustments in the decision-policy are unrelated to pupil diameter. As a sanity check, have the authors looked at pupil diameter as a function of the uncertainty parameters? It would be good to show that earlier effects of uncertainty and their temporal dynamics are replicated (have a plot with the betas over time pre-choice and post feedback). I think the conclusion can be stronger if the authors show that pupil dilation tracks both forms of uncertainty and the anticipation and response dynamics associate with that, but that the subsequent adjustments are not mediated by this system.

Right now something could be wrong with the pupil data and the reader has no way to know. It would also be important just to see that these earlier findings replicate.

8. Reconsider causal language/interpretation of drift rate effects in the discussion.

You say in the discussion that people reduce the drift rate. Isn't the drift rate here determined by the consistency of the evidence? Sure, people can focus more (i.e. in cognitive control tasks, where the response rules are well known and errors are primarily driven by early incorrect activations of prepotent responses or attentional lapses), but I can focus all I want when there's no evidence (when I just don't know what the relative values are because I currently have zero [or little] valid experience to draw from after I detected a change point ) and my drift rate will still be low. No? Couldn't it be that participants have a sense that their drift rate is low (because they have no idea what's going on) and because taking time to sample would be useless (because uncertainty is not reducible other than through action), dropping the threshold is the right thing to do? In that sense the (expected) drift rate would dictate the optimal boundary height. I'm thinking of work by Tajima et al.

9. Reconsider reinterpretation of previous findings in the discussion – add nuance where nuance is due.

I have a bit of a problem with the authors’ assertion that previous findings relating boundary height and conflict could be a misattribution of volatility effects (Frank and colleagues). These previous studies did not have change points. So that is an unlikely explanation of that finding. What is more likely is that the choice dynamics were different because the choices were not temporally dependent, i.e. participants made choices between different options on each trial, meaning that the conflict and thus the optimal decision-strategy differed on every trial (in addition to any learning related uncertainty, but importantly, the true values associated with stimuli never changed). That is not the same as a change point/volatility. Further in the present study, conflict is anticipated, except in the case of change points. So that could equally be the difference between expected and unexpected uncertainty that leads to dissociable effects on decision strategies. In both cases, what drives the threshold adjustment is probably some form of surprise (unexpected conflict). As it stands, the statement in the discussion is inaccurate/misleading. That’s an easy fix though.

Reviewer #3:

Shifting between more explorative and more exploitative modes of decision making is crucial for adaptive human behavior. Therefore, the authors' attempt to investigate the internal processes that allow these modes is important to begin to understand this remarkable ability. In addition, investigating the proposed link to the LC-NE system is sensible and establishing its role in these processes would help the field forward. The authors present a thorough, modelling-heavy set of analysis on two interesting datasets aimed at revealing the underlying mechanisms.

1. Despite these strong points, the manuscript in its current version falls somewhat short of answering the questions that it poses. For one, the DDM analyses are restricted to only two parameters, which begs the question whether other established parameters might be better able to explain the results and thereby shed more light on the underlying mechanisms. Also, regarding the role of the pupil-linked LC-NE system, no strong conclusions can be drawn from the data, since the visual stimulus design likely resulted in strong pupil light reflexes, which might well have overshadowed subtler, more interesting modulations of the pupil. Despite the manuscripts innovative and clever use of Bayesian modelling and PCA, these two shortcomings might limit the impact of the manuscript in its current form on the field.

Shifting between more explorative and more exploitative modes of decision making is crucial for adaptive human behavior. Therefore, the authors' attempt to investigate the internal processes that allow these modes is important to begin to understand this remarkable faculty. In addition, investigating the proposed link to the LC-NE system is sensible and establishing its role in these processes would help the field forward. However, although in general the presented analyses seem thorough, I have two main concerns that in my opinion should be addressed before conclusions can be drawn from the data.

First, the DDM modelling is too restrictive, only focusing on the bound and drift parameters. Besides these two main parameters, another main parameter of the standard DDM is non-decision time, which to my surprise is not mentioned at all in the manuscript. Moreover, recent work has shown that two further parameters can capture internal processes possibly related to explore/exploit policies: starting point (z) and drift bias (called drift criterion or dc by Ratcliff and McKoon (2008)). Including these latter two parameters possibly can explain the RTs better than drift only and shed more light on the components underlying conflict and volatility. In addition, non-decision time might also be affected by the experimental manipulations, and should at least be reported in the manuscript (I assume that the authors did include it in their currently reported DDMs). In my mind, investigating all these further parameters is crucial before the conclusion that bound and drift rate best capture conflict and volatility is warranted.

My second point concerns the pupil analysis.

a) Although I could not find information about visual stimulus size and brightness in the methods, Figure 2AB suggests that there were strong visual transients at trial onset (black screen → stimulus), which presumably resulted in strong pupil constrictions due to the pupil light reflex (PLR).

b) I would have liked to see pupil time courses in this manuscript. The first components of the PCA, as employed by the authors (which in principle I think is a great idea) is likely to capture exactly these PLR dynamics given the large variance due to PLR.

c) Now, previous work has shown that the LC-NE system is in fact better tracked by using the first time derivative of the pupil signal (Reimer et al., Nat Comm, 2016). The authors should consider looking at the pupil derivative to see if this reveals a link to their experimental manipulations. Importantly, using the derivative instead of the actual pupil time series attenuates the PLR since only the slope is taken. Hence, when using the derivative, the PCA might pick up more interesting, cognitive drivers of pupil dynamics, since the PLR dynamics are suppressed. It would be interesting to see if this would reveal a link to the experimental manipulations.

d) Further, please note that the pupil likely not only is linked to the LC-NE system, but generally to catecholamines, which includes dopamine (Joshi et al. Neuron 2015). Therefore, I would recommend to not exclusively link pupil to LC-NE in the manuscript while interpreting the pupil results.

e) In any case, the author should show raw pupil as well as pupil derivative time courses for the different conditions to give insight in their data.

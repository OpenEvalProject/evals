# Peer review - Round 1

Editors:
- Andrew J King, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85706.sa0](https://doi.org/10.7554/eLife.85706.sa0)

This study provides an important contribution to our understanding of the neural basis for the categorical perception of sounds. Although the number of animals included is small, solid evidence is presented to show how categorical information emerges in the ferret primary auditory cortex following sound presentation and persists until a behavioral response is made. The work will be of interest to neuroscientists interested in the neural representation of task–related variables in sensory cortex during decision–making tasks.


---

# Peer review - Round 1

Editors:
- Andrew J King, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85706.sa1](https://doi.org/10.7554/eLife.85706.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Dynamics and maintenance of categorical responses in primary auditory cortex during task engagement" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. More information on how the linear regression analysis used to separate auditory and category–related activity was carried out is needed. This analysis should also be expanded by including other task–relevant parameters (licking, reward, uninstructed movement) in order to provide stronger evidence that the changes in A1 activity represent a categorical response rather than a premotor response or signals related to reward expectation. Related to this point, the reviewers were concerned that the effects reported are very small.

2. More details of the population decoding are needed and there are many places where important methodological and other information is missing (see individual reviewer comments).

3. The naïve animal included in the study was not thought to be an ideal control. Evidence that A1 neurons encode learned categories would be stronger if the comparison could be made with ferrets that have been pre–trained on the task structure. i.e. are performing the task, licking, receiving rewards, etc, but have not learned the stimulus categories. If possible, please provide this more appropriate control.

Reviewer #1 (Recommendations for the authors):

In this study, Chillale et al. investigate auditory cortex population dynamics during sound categorization. The authors train ferrets in a delay go/nogo task and record neuronal activity with multielectrode arrays. The main finding is that learned categories are encoded in A1 population activity, both in a task–engaged and a passive setting. The task–engaged category representation persists during the delay, but its activity pattern is uncorrelated with that during stimulus presentation. Further analyses show that the 'nogo' category sound representation is suppressed during task engagement and that sensory encoding during stimulus presentation is degraded when the ferret makes a mistake. The authors conclude that the A1 category representation is an early contributor to auditory categorization.

Overall, the study uses an elegant task design and provides important insights into the encoding of learned categories early in sensory processing. The task, having a delay period between stimulus presentation and response window, allows the authors to address how the neuronal representation evolves in absence of the stimulus and before the onset of motor behavior. The finding that neural activity during stimulus presentation and delay periods encodes learned categories, but is uncorrelated, is particularly intriguing, as it suggests complex circuit dynamics beyond sensory processing in A1. In addition, the use of stimuli varying in click rates rather than, the more common, sound frequency makes the results less sensitive to sampling biases (i.e. through tonotopy). In general, the focus of this study on characterizing population dynamics rather than describing single–neuron responses provides an interesting contrast to previous studies on sound categorization.

I have two suggestions for how the conclusions could be strengthened and presented in a better interpretable way. The first suggestion concerns the approach to disentangle stimulus from the category–related activity and its description in the manuscript, and the second is regarding the question of whether the category representation is indeed a learned sensory representation, or could reflect other task–related aspects. I will detail both below.

1. The authors use a linear regression model to disambiguate stimulus–specific and category–specific population activity. They then use the learned regressor weights to project population activity onto a category coding dimension. However, from the manuscript, it cannot be inferred whether this model can isolate sensory– and category–related activity. The methods state that the sensory regressor assumes a linear relationship between neural activation and click rate. I am not convinced that this is always the case in the auditory cortex. In addition, since there is a stable mapping between click rate and category identity, the two regressors are not independent, which can lead to unreliable estimation of regression weights and lower statistical power (multicollinearity). This problem potentially extends to the method for calculating the projection of activity using the model weights, the projection axes could be not independent or orthogonal. Therefore, it is hard to determine if the category encoding projection is unique to category encoding. The model also lacks other behavioral parameters, like licking, reward, and uninstructed movement parameters, that therefore go unaccounted for.

In order to address these concerns, the authors should amend the regression model with the other task–relevant parameters, and describe in more detail how it was constructed and fit (e.g. showing a design matrix and/or schematic or toy model illustrating how projections were made), report on its performance (e.g. Rsquared) and show that their choice of regression parameters, and method of calculating projections, leads to separable dimensions/projection axes. In addition, the authors can explore whether single neuron click rate tuning (in naive animals) indeed does not give rise to any 'categorical response'.

2. The authors compare their findings in trained animals to passive recordings in one naive animal. This comparison is used to argue for a learned component of the category representation. However, this finding is (to some degree) confounded with other learned task–related behaviors/associations that covary with the learned categories.

The conclusions of this study would be vastly strengthened if a comparison was done with "naive" animals that have been pre–trained on the task structure. i.e. are performing the task, licking, receiving rewards, etc, but have not learned the stimulus categories (yet). I would find it very useful to know whether the 'categorical response' is absent in behaving animals that did not learn the category association. This approach would also allow the authors to more directly address the specificity of the 'nogo' suppression with learned behavioral inhibition and to compare the influence of motor planning on the category representation during the delay period.

In addition to the two main suggestions, I have some more detailed comments on how the authors could improve their manuscript.

1. Clarity and precision of method descriptions. Several key methods are hard to follow, I listed some questions in the bullet points below:

As mentioned above, the model description is unclear, what is t, time, or trial?

When describing trial–averaged data, what was averaged, frames in a trial, or trial repetitions?

What linear decoder was used?

Was the whole task done head–fixed?

The section on surgical procedures is imprecise, were multiple craniotomies performed? It says the craniotomies were made into cement. How did the craniotomies allow for the visual identification of A1 regions?

2. Clarity and precision of figure legends and statistics descriptions. Often it is not clear from text or legends if a plot shows data from one or both animals (e.g. Figure 2b, but also others), what information the error bars display (e.g. Figure 1b,c Figure 2c), to which time–bin decoders are trained/regressors are fit (e.g. Figure 4a), and what certain figure elements, like black bars, represent (e.g. Figure 3f, 4d). Some statistical tests are only reported in text and not in the respective figure and legends, some vice versa (eg. Figure 2e). Some labels are switched (Figure 2b).

3. In the analysis of error trials, it seems both misses and false alarms are combined. However if the hypothesis is that in nogo trials the category representation, and hence behavioral action, is suppressed, shouldn't there be an interesting difference between misses and false alarms? This should be explored to strengthen the interpretation of the results.

4. The discussion and clarity of the interpretations of results could be improved, specifically regarding the following questions:

Is the interpretation of the uncorrelated stim and delay period decoders (Figure 2b) that different neurons are responsible for the encoding? Are there alternative interpretations?

Can overall changes in population activity (more firing, attention,..) explain the trial–to–trial correlation of stimulus period and delay period activity (Figure 4b)?

It would be very interesting to discuss in more detail how this study's findings relate to the observations on a single neuron level (Xin et al., 2019).

The direction of argumentation is unclear when it comes to the question of whether the feedback–related activity can explain the results. The authors could also consider work in the somatosensory system (e.g. Yang et al., Nat Neuro, 2016).

If underlying rotational dynamics are suspected, would those not lead to a gradual shift in correlation rather than an abrupt switch?

5. The authors state in the first paragraph of the discussion that encoding of behavioral categories was not observed in the naive animal. Does this refer to Figure S4? I do not see any data supporting this claim.

Reviewer #2 (Recommendations for the authors):

The authors trained two ferrets to discriminate high and low–rate click trains with target and non–target categories each comprised of three distinct rates with one animal trained to treat fast rates as targets and the second to treat slow rates as targets. In each case animals are rewarded for licking targets and required to refrain from licking non–target trials. Additional complexity is imposed by ferrets being required to withhold their response until a delay period (indicated with an LED) ends. Requiring that animals wait for this extra delay period offers the potential to parse out sensory, categorical, and motor aspects of the neural response.

Neural recordings are made in passive and active configurations for every neuron. The authors use population decoding to explore the emergence of categorical responses through the trial duration with their key finding being that categorical information exists during the stimulus, the delay period, and the response period, whereas sensory information is predominantly encoded in the stimulus period. During passive listening stimulus and (some) category information exists in the stimulus, but not the later epochs.

Broadly speaking this study confirms similar findings relating to the time course over which single neuron choice probabilities emerge in A1 (which are closely related to categorical perception in animals with good task performance, as they quantify the ability to decode the class of response across multiple stimulus values) from e.g. the Sutter lab, the Bizley lab, the Jaramillo lab.

I was left a little uncertain as to how large the conceptual advance was here, and a little unsatisfied that I don't know anything about the neural responses within the population (or even how the population response is being modelled, see comments below). For example, is the category sensitivity a consequence of a few category–tuned neurons, or is it an emergent property only visible in the population? How does the category selectivity compare to single neurons decoded over analogous time windows? What is the added value of combining information across small groups of neurons? I also don't follow the argument for why their data support that delay activity might be feedback activity (although I agree this is a perfectly plausible theoretical argument).

I have some concerns about to what extent the 'categorical' response really represents an abstraction of the stimulus class, as opposed to a premotor response or feedback from an area generating such signals. In this regard the observation that activity during error trials for all but the latest epochs of the trial is noisy / chance level rather than below chance is reassuring; however, the 'error' trials here include two categories of behaviour – both misses (where there was no motor response) and false alarms (where the motor response was early). This analysis would be more convincing if each class of response was separated out.

I would also like more information on the population decoding approaches. The authors apply a regression model which is an elegant solution to try and tease apart the confounded sensory and category information. However, the coefficient of partial determination (i.e. the variance explained by one or another factor) is tiny – on average ~ 1% of the overall variance. This begs the question of how good the linear models are in the first place, and what proportion of the explainable variance 1% accounts for (maybe it's a large fraction but without more information about model fit we can't assess this). In fact, the sensory information also shows a u–shaped function, being high during the stimulus, low in the delay then nearly as high as the stimulus period in the response window. This doesn't seem to fit with the narrative put forwards in the manuscript. There aren't sufficient details (or code) in the methods to work out what is actually modelled – what is the neural response at time t and how does it relate to the population of units (i.e. is it the average spike rate across the population or a vector of unit spike rates or a matrix of spike rates over time… ?). Without this information, it makes it very hard to understand what is being projected back onto the regression coefficients.

For the linear decoder more details (or as a minimum a reference) are needed – is it a Foffani and Moxon style Euclidean distance decoder, an SVN, or … ? I presume 2A is the result of the linear decoder? It would be nice to see something a little closer to the raw data here instead of just mean {plus minus}SD. 2B is also the linear decoder. Generally speaking, there are insufficient details in the methods for the population decoding to really understand what was run, and even less so to replicate their study. More details need to be provided here (and ideally the code released alongside the paper).

I would have liked the information about the population size to be in the Results section rather than only buried deep in the methods; the populations themselves are really quite small (mean 5 / 11 neurons in the two animals) which is useful in interpreting the modest performance of the decoder (which is clearly above chance but not that much so). Also how confident are they that all units are in A1 as the array sounds like it's quite large (potentially larger than A1) to me?

There are many places in the manuscript where it's not obvious whether the data is from one animal or both (one assumes one animal, as the figures list only a single contingency for high/low rates). The data for both animals are very clearly laid out in the supplemental material but not always well described in the main manuscript.

Reviewer #3 (Recommendations for the authors):

This work investigated the activity of neurons from the primary auditory cortex (A1) of ferrets performing a click–rate categorization go/no–go task or passively listening to these sounds. The authors found that the population of recorded A1 neurons shows a different firing pattern for go vs. no–go stimuli, not only during the stimulus presentation but also during a delay period before the licking response. Prediction of the go vs. no–go categories via neural decoding analysis revealed that these categories were decodable during both the stimulus and delay periods, but the population code was different between these two periods.

The authors provide clear evidence of differences in neural activity patterns for correct trials with go vs no–go stimuli. However, it is not completely clear that these observations reflect auditory categorization as the authors suggest. Most of the data presented seems consistent with alternative interpretations such as a representation of expected reward or pre–motor signals in the auditory cortex. For example: (1) the differences in neural activity between go and no–go stimuli are not present during the passive presentation (Figure 1f) when animals are presumably not licking or expecting reward; (2) the dynamics of neural activity changes consistently with movement when comparing (invalid) early licks, (invalid) late licks and (valid) hit trials (Figure 4c); and (3) the population code that enables decoding of go vs no–go stimuli changes between the stimulus presentation period and the delay period, which suggests a change in what is being represented during these periods (which could be mostly stimulus identity in the first period and motor–preparation signals in the second period). As such, the claim that neural activity reflects the categorization of the stimuli rather than the representation of other variables does not seem fully supported.

The authors try to address some of these concerns in the discussion by suggesting that motor–related activity is expected to have a short latency (~100 ms). However, from their experiments, it seems difficult to rule out that signals related to motor preparation or reward expectation (at possibly multiple latencies) are the main drivers of the observed effects.

If we define perceptual categorization as a maximization of perceptual differences between categories and a minimization of the differences within a category, investigating the neural representation of auditory categories may require a more nuanced comparison of how well one can decode stimuli within vs. across categories from neural activity.

– The manuscript would benefit from a discussion of alternative explanations related to reward expectation.

– The differences in neural activity seem compelling, but the author may want to de–emphasize the idea that these changes are associated with a neural representation of auditory categories.

– Figure 1e: because the structure can appear from random data when sorted, a supplementary figure showing neurons sorted by the delay during passive would illustrate that effects shown in this figure are not just the result of sorting for the active condition.

– It would be useful to clarify whether the "increase" associated with Figure 1f (during the delay period) is with respect to the spontaneous or sound–evoked activity.

– Clarify what "R.W" means. I don't think that is a standard acronym.

– Figure 1f: specify what period(s) of activity the modulation index refers to.

– The authors need to clarify whether the animals are head–fixed or freely moving during training and recordings. While they mentioned "To obtain stable neurophysiological recordings we implanted the ferrets with a stainless steel headpost", it's not clear when the headpost was used since the electrodes were chronically implanted.

– Authors should also specify how sounds were delivered (Figure 1 seems to indicate the ferrets had headphones).

– Authors should be clearer about the passive stimulation sessions. Are the animals licking? are there other differences compared to the active sessions (e.g., inter–trial interval)?

– The first mention of "the naive animal" comes out of nowhere. The authors should introduce that there is a naive animal used for control experiments.

– Figure 2 caption: I don't know what "resp." means.

– Figure 4C: y–label should say "categorical".

– Figure 5a: the caption says "cyan" but it looks purple to me.

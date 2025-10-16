# Peer review - Round 1

Editors:
- Catherine Emily Carr, University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36769.025](https://doi.org/10.7554/eLife.36769.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A novel time-stamp mechanism transforms egocentric encounters into an allocentric spatial representation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Catherine Emily Carr as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Matthew A Wilson (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper contains the first recordings from neurons in the periglomerular complex (PG) in weakly electric fish. This structure receives input from the optic tectum and projects to the dorsolateral pallium (DL). DL is hypothesized to be the site of spatial memory, and thus its input from this thalamic complex is important. The authors have recorded from PG, and show that, despite the topographic nature of the input from the optic tectum, responses are non-topographic. They use a model to support the hypothesis that what occurs in PG is a temporal representation of spatial sequences.

Essential revisions:

The reviewers were divided about your manuscript. Two felt there was sufficient merit in this being the first report of activity in the periglomerular complex, while a third felt that both the analysis and the presentation of data were insufficient. All three reviewers agreed that the conclusions of the paper were not satisfactorily supported by the data. From the Senior Editor: "We note an increasing tendency in submitted manuscripts for authors to "overhype" their results to "sell" their work. We strongly encourage you to let your data speak for themselves and to present the data in a way that the reader can see exactly what you have done and why."

The manuscript lacks the information required to assess the strength and significance of many statements, with a need for substantial improvement in the presentation of results.

The presentation and analysis of the electrophysiological data require careful revision, potentially with a table, to show which cells were evaluated with which stimuli, and where they were located. In many cases the numbers mentioned appear inconsistent. More details are provided below.

The simulations are limited and only demonstrate plausibility of the proposed mechanisms.

The analysis of the behavioral data was not explained with sufficient clarity.

Introduction:

The opening paragraph of the Introduction states that "neural mechanisms underlying the transformation of the egocentric sensory and motor information streams into an allocentric representation.… are completely unknown". This is incorrect. Even though much is still unknown, a lot has been learned about the emergence of an allocentric representation of position and especially heading – in rodents and in other organisms. Some notable recent examples include the discoveries related to representation of orientation in Drosophila; or the recent work by Peyrache et al., reporting on the existence of a conjunctive representation of allocentric heading and egocentric proximity to borders, which may serve as a building block for the allocentric border cells observed in the entorhinal cortex.

There are many assertions throughout the manuscript that appear unsupported. For example, "making PG a feed-forward information bottleneck between egocentric and allocentric spatial representations" could be reconsidered. Just because temporal information, combined with a speed signal, can permit accurate path-integration, does not mean that it does. The authors should critically review all assertions to differentiate between what is shown and what is hypothesized.

Results section:

Further information is required about the PG responses and their analysis in the manuscript. Questions raised in the reviews are summarized below. Part of the confusion experienced when reading the manuscript may emerge from the separation of figures and supplementary figures. These should be integrated to support a logical flow of results. For example, why does Figure 4—figure supplement 2 contains navigation behavior and lateral line physiology?

– What is the relationship between a cell's properties as shown in Figure 2A-C to those shown in Figure 2D-F, to those shown in Figure 3? What are the parameters that characterize the population of time-interval encoding cells, as extracted from the procedures described in the Materials and methods section?

How were the cells, shown in Figure 2 and discussed in subsection “PG cells respond to object encounters”, classified into the different categories?

It is unclear how the various sample pools of cells were selected and how they overlap. 84 cells were recorded, but across how many animals? I assume each animal was implanted with single electrodes (stereo or tri -trodes), and that only single penetrations were made for each animal although this is not stated explicitly.

Of the 84 cells, it is reported that 27 had receptive fields mapped in Figure 1. They then describe 28 cells tested with longitudinal motion. I assume that these are a separate group of cells measured in a separate group of animals, although again not explicitly stated. This is followed by description of 40 cells showed looming-receding responses described in Figure 2. This is slightly confusing given that the receptive field mapping of the 27 cells in Figure 1 used a looming-receding protocol. Did the 40 cells shown in Figure 2 simply go through a more extensive mapping protocol allowing the different detection types (proximity, encounter, change) to be identified (although no such description is given in the methods)? Again, is this a separate pool of cells in a separate group of animals?

Given that the numbers here don't quite add up (27+40+28 = 95) there is something that I am missing. Perhaps there is some overlap between the 27 receptive field mapped cells and the 40 looming-receding cells, and then the question is why the subset?

Figure 3 then describes 33 cells subjected to repeated motion protocols. Again, unclear how this pool of cells relates to the other pools.

Perhaps a summary table in the supplemental information listing the all of the animal/cells/protocol would clarify things.

It would be useful to include data regarding the receptive fields as a function of body position for the units shown in Figure 1 to get a sense of the response distributions along the body.

If the cells are drawn from different animals/recordings, how confident are the authors that the 3 topographic cells shown are drawn from the same pool as the non-topographic and are not the result of sampling from a different site due to variation in electrode placement across implants. This is not essential to the overall interpretation, but it would be important to know whether this reflects an accurate estimate of the relative representational heterogeneity in PG.

I did not understand the terminology used in the manuscript. Most of the cells described in PG exhibit invariance to the heading of an object relative to the animal, but they are selective to the distance of an object from the animal (and they do not acquire selectivity to the animal's heading relative to the environment). Why, then, claim that egocentric spatial information is abolished in PG?

In addition, how do the results in the manuscript show that the time interval encoding observed in PG produces an allocentric spatial representation, as announced in the title? The results of the manuscript only hint at the possibility that the activity in PG might serve as an input to this computation.

The conclusions drawn from the model should, in my opinion, be taken with a great deal of caution, because of the assumptions that were made: first, the memory variable was set to zero (is this justified based on the fits?) Even more importantly, the model assumes independent noise in the different neurons. There are various reasons why this might be incorrect, possibly leading to a greatly reduced ability to decode the interval duration from a large population: one of them is correlated stochasticity. Another reason is that the activity might depend on some latent variables other than the history of time intervals. Overall, I am not convinced that the population activity in PG can be probed to generate a robust readout of the time interval between encounters.

I would also like to comment that the computational analysis in the paper is not strong. I appreciate that the model of neural response is simple but the fit of the data to this simple model is not demonstrated convincingly. The neural readout analysis suffers from technical issues (see below), but even more importantly it relies on assumptions that may be incorrect, and these limitations are not acknowledged or discussed.

The assessment of readout precision is performed by simulating spiking activity (based on the model) and application of a maximum likelihood (ML) decoder. This is unnecessary. Given the assumptions of independent Poisson noise and no history dependence, it is possible to evaluate the Fisher Information analytically, which would clarify how the results scale with various parameters. Considering the large number of cells postulated, this analysis is expected to provide precise agreement with the ML simulation results. However, I also expect to see some assessment for how the observed distribution of the history dependence parameter β might affect decoding precision. This aspect of the analysis may be more difficult to achieve with a full analytical approach, hence simulations can be helpful. A simple estimator that ignores the history dependence might be significantly influenced by the history dependence, as this is a source of variability that is shared across the population. Perhaps a more sophisticated decoder might do better, but this would require a reasonable proposal for implementation by neural circuitry. A decoder that takes into account the history dependence may need to maintain memory of the response from the previous encounter, and it's important to understand whether this is necessary.

The analysis of the behavioral data is not explained with sufficient clarity (for example, what are the parameters theta and A mentioned in subsection “Analysis of behavioral data”?). How the model of neural readout relates to the behavior is even less clear. Finally, in in subsection “PG activity explains path integration acuity” it is stated that "the number of PGI cells is sufficient to attain the observed behavioral precision, even when additional encoding errors e.g. in heading and velocity estimation are taken into account". Where is this demonstrated?

3) Title: The title is a bit misleading given that the egocentric-allocentric transformation is not explicitly demonstrated but rather suggested through simulation. Perhaps qualifying it with "A novel time-stamp mechanism could transform egocentric encounters into allocentric spatial representations".

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "A time-stamp mechanism may provide temporal information necessary for egocentric to allocentric spatial transformations" for consideration by eLife. Your article has been reviewed by Eve Marder as the Senior Editor, a Reviewing Editor, and two reviewers. The following individual involved in review of your submission has agreed to reveal his identity: Matthew A Wilson (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper contains the first recordings from neurons in weakly electric fish that project to the dorsolateral pallium (DL). DL is hypothesized to be the site of spatial memory, and this input is hypothesized to transform egocentric encounters into allocentric spatial representations.

Essential revisions:

1) There remains concern about how well the neural response model captures the measured neural responses. Figure 6—figure supplement 1 demonstrates that the predictions of the model and the measurements are positively correlated, and that this correlation is statistically significant; but this on its own is a relatively weak statement, and it is difficult to interpret the reported values of correlation coefficients. We would like to see a word of caution that the analysis relies on an assumption that the model correctly captures the neural responses.

2) The mathematical analysis of temporal encoding precision assumes that β = 0, and accurate readout using the naive ML estimator requires approx. β < 0.2. Hence, it's relevant to know, what are the characteristic properties of cells with zero or small β: one can imagine a scenario in which these particular cells have very small gains, or short time constants, and are thus less useful for the computation than expected from panels A-C.

3) The authors propose a hypothesis about how animals generate their representation of position relative to the environment, and could discuss how this prediction might be tested in future experiments, either behaviorally or in terms of neural activity in other brain areas. Behaviorally, the model implies that the animal's sense of position is critically dependent on the last encounter with an object. Does this make sense? Another interesting prediction is that there may be a cutoff in the durations of swimming without encounters, over which the animal can estimate its position – determined by the distribution of adaptation time constants.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "A time-stamp mechanism may provide temporal information necessary for egocentric to allocentric spatial transformations" for consideration by eLife.

We'd like to accept your paper, but first suggest you revise the paragraph excerpted below because it does not really address the reviewer's question.

What we asked for in point 3 was "The authors propose a hypothesis about how animals generate their representation of position relative to the environment, and could discuss how this prediction might be tested in future experiments, either behaviorally or in terms of neural activity in other brain areas. Behaviorally, the model implies that the animal's sense of position is critically dependent on the last encounter with an object. Does this make sense?"

You added a paragraph to the Discussion section, discussing several possible lines of behavioral and physiological inquiry for future studies. We would like a shorter reply that is more to the point in addressing this "Behaviorally, the model implies that the animal's sense of position is critically dependent on the last encounter with an object. Does this make sense?"

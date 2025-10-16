# Peer review - Round 1

Editors:
- J Matias Palva, University of Helsinki Finland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60988.sa1](https://doi.org/10.7554/eLife.60988.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study used a novel approach that combined measures of human brain activity with high spatial and temporal resolution (using magnetoencephalography, or MEG) and repetition suppression to identify neural representations of task-specific information processing related to the stimulus, task context, and/or motor response during decision-making. The primary finding, which runs counter to many related studies in non-human primates, is that in premotor cortex, neural activity encodes task-relevant features more strongly than task-irrelevant stimuli. The clever approach, and the use of that approach to draw interesting and well-grounded conclusions about information processing in the human brain, were considered particularly noteworthy and likely to inform future studies of human decision-making.

Decision letter after peer review:

Thank you for submitting your article "Projections of non-invasive human recordings into state space show unfolding of spontaneous and over-trained choice" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Lucas C Parra (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The editors have judged that your manuscript is of interest, but as described below, that extensive revisions are required before it can be considered for publication. The editors and reviewers agree that no further data are required but major conceptual and data-analysis wise clarifications are essential.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this paper the authors use a novel technique to disentangle neural representations of distinct choice-relevant variables in MEG data which leverages the phenomenon of repetition suppression. By presenting an 'adaptation stimulus' before each perceptual choice the authors were able to selectively suppress neural activity for different sensory and response modalities and used these suppression signatures to isolate distinct activity components reflecting task context (instruction to attend to motion vs colour), relevant sensory input, irrelevant sensory input, motor response (index vs middle finger) and choice. Repetition suppression was used here with clever experimental design to determine from MEG whether premotor cortex (PMd) "encodes" different properties of the stimulus, task or response during a decision making task. The premise is that if adaptation is observed for a specific feature, then this feature must have been "encoded" in PMd. The main finding is that stimulus, task and response features are all "encoded" in PMd with increasing delay, and that task-irrelevant stimulus properties are "encoded" less strongly. While, prior NHP studies found little difference in the representation of relevant vs irrelevant sensory inputs at the final integration stage, the present study found that irrelevant representations were significantly weaker. A follow-up study in which humans were extensively trained to mimic the task exposure experienced by NHP replicated these results.

The study is interesting on many fronts and relevant to a wide audience. It is, however, essential the revise the manuscript extensively to address several issues including methodological challenges associated with inferring neural computations underpinning decision making from non-invasive recordings and the more general question of the degree to which irrelevant sensory inputs are subject to top-down filtering.

Essential revisions:

1. The rationale for relying on repetition suppression to isolate a neural readout of the decision process needs to be more clearly articulated. Given the emphasis the authors place on comparing their results to previous NHP studies (Mante et al. 2013, Siegel et al. 2015), the authors should explain why they could not have applied a similar decoding approach. The task design means that task context, sensory modality, sensory input strength and choice are already nicely orthogonalised so why is the adaptation step necessary?

2. The query above relates to a more substantive question regarding the degree to which the authors approach can allow us to draw firm conclusions regarding the relative timing with which these distinct variables are represented. For example the authors highlight that sensory representations precede choice representations.

2a. For starters, this is contrary to what Siegel et al. (2015) found – they reported that choice representations emerged before the stimulus even appeared.

2b. More importantly, to what extent can it be assumed that the relative timing of adaptation effects on sensory vs motor components necessarily translates directly to differences in the time at which these variables influence the decision process?

2c. The authors note the well-established fact that stimulus and response repetition is associated with decreased BOLD/EEG/MEG activity in the relevant brain regions but what do we know about the timing of these effects? Can we assume comparable dynamics underpinning sensory and motor adaptation?

2d. For example, recent studies of choice history biases (e.g. Urai et al. 2019, eLife) suggest that responses on trial N-1 cause a bias in the rate of evidence accumulation for repeated choices suggesting that the neural dynamics associated with repetition may more complex than a simple attenuation. More pertinently, can we assume that these adaptation/attenuation effects have any impact on the information content for the decision process?

Please clarify these aspects in relevant sections of the manuscript and address with data analyses how repetition impacts sensory encoding versus motor preparation signals.

3a. The contrast between the present study and the aforementioned NHP studies on the point of filtering of irrelevant sensory inputs is striking and interesting. The authors have, however, used a different analysis strategy to that of Siegel and Mante, which could conceivably contribute to this difference. This does not necessarily undermine the novelty and importance of the results but points to some additional possibilities. Please clarify this and consider corroborating the results by implementing a more comparable analysis approach.

3b. The authors could further examine the difference in human versus monkey behaviour. In Siegel et al. (2015), the monkeys exhibited quite strong cross-over effects (ie. RT for motion choices being impacted by stimulus colour). How strong are the cross-over effects in the present study? Please quantify and clarify this issue. This would be helpful to know as it would point to a more fundamental cross-species difference and perhaps rule out the possibility that the cause of the discrepancy lies more in the differences in analysis strategy or neural recording methods.

4. A key difficulty with the narrative of this work is the notion that adaptation=eoncoding. If we have understood correctly, what is actually quantified here is whether a change in experimental condition (from one repeat to the next) drives variance in the PMd signals. Therefore, the analysis treats PMd as a the output of a change detector. But the readout of a change detector does not necessarily need to encode the feature itself. So to claim that presence of adaptation (a weaker response to the stimulus) = good encoding of that stimulus, was found confusing to both reviewers and the reviewing editor. A lot of the language in the result sections equates the two and makes it very hard to parse. Please clarify and justify the rationale.

5. Another central terminological confusion pertains to "Projection into state space" that is in the title and much of the introduction. This gives an impression of multi-variate analysis of MEG data, which is largely not the case in this study. Until Figure 5, all the analysis is on uni-variate neural signals and nothing is "projected", nor is there any use of "subspace" or "decoding" or "encoding". It is clear that the investigators see "adaptation" conceptually as a way to quash neural response in some dimensions, and in that sense the term "projection" may be justified. This is, however, very unusual use of terminology and may be seen confusing by many readers. Please reformulate the title and introduction of the paper to more accurately reflect the content of the paper and better set the expectations for the reader.

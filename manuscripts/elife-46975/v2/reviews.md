# Peer review - Round 1

Editors:
- Tobias H Donner, University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- Tobias H Donner, University Medical Center Hamburg-Eppendorf Germany
- Redmond G O'Connell, Trinity College Dublin Ireland

## Review text

DOI: [10.7554/eLife.46975.019](https://doi.org/10.7554/eLife.46975.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Statistical context dictates the relationship between feedback-related EEG signals and learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Tobias H Donner as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jonas Obleser (Reviewer #2); Redmond G O'Connell (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Nassar, Bruckner, and Frank examine the context-dependence of the impact of surprising sensory events on learning and choice behaviour. To this end, they have participants perform a continuous sensory decision-making task in two different statistical contexts: one in which mean of the process generating the evidence changes at unpredictable times ("change point task") and one in which this generative process does not change, but – by design – generates occasional outliers. Surprising evidence samples should elicit an adjustment of choice behavior in the first context, but be ignored in the second context.

Behavioural modelling shows that this normative prediction holds for human participants: They do factor surprising evidence samples into behaviour differently depending on the statistical context. The authors also examine EEG data for signatures of this context-dependent encoding of surprise and learning. A centro-parietal positivity in the evoked response scales with surprise irrespective of statistical context; but the influence of this response component on choice updating is conditional on context. The authors link the response component to the classic P3b or P300 of the EEG. The authors conclude that the P3 provides a general surprise signal, which is fed to a downstream process which translates surprise into a contextually appropriate behavioural adjustment.

This study addresses an interesting and timely question. It uses an original approach and is generally well executed. Specifically, all reviewers were impressed by the behavioral modelling part, but there are some issues pertaining the approach and interpretation of the EEG part, which should be resolved prior to publication.

Essential revisions:

1) Behavioral modelling.

Please present the normative model in more depth, in a longer methods section or supplement. Specifically, you should (i) derive the oddball version of the model, and (ii) explain the difference between the change-point and oddball versions of the model. A description of how the application of the model to a circular stimulus space differs from previous versions of the model would also be helpful.

2) Relationship to previous literature and theory on P3.

2a) Tease apart the novel aspects and the replication of established findings more explicitly.

The finding that P300 indexes surprise is already well-established in the oddball literature. For example, Kollossa et al., 2013 state: "It has long been recognized that fluctuations in P300 amplitude reflect the degree of surprise.". What is novel here seem to be two things: first, the establishment of the same surprise sensitivity in the context of a change point process; and second, the context-dependent relation of the signal to learning. This should be clarified throughout the manuscript, including the Impact Statement. Previous studies quantifying the link between P3 and surprise should be cited and discussed – specifically:

- Mars et al., (2008)

- Work by Bruno Kopp, e.g. Kopp et al., (2016).

2b) Relation to existing accounts of P3.

The discussion of how the present results relate to previous accounts of the P3 is somewhat confusing and should be clarified. In the Introduction the authors initially only allude to the context updating theory of the P3 but other accounts are mentioned in the Discussion section. A key issue here is that no clear initial hypotheses are derived from these models in the Introduction and the efforts to relate the present results to the models in the Discussion section is unclear – in several instances it is initially suggested that the present findings are at odds with a given theory but then acknowledged that the findings are potentially reconcilable. If the authors are unable to generate unique hypotheses for the present data based on previous theories of the P3, then this should be stated clearly.

Much of the P3 literature and the explanatory accounts have tended to centre on responses to stimuli that call for an immediate choice and report. Here the authors are effectively looking at feedback-related responses and it does seem difficult to generate specific predictions from the models in this particular context but that is not necessarily a limitation of the models, more a matter of unexplored territory requiring additional simulations and empirical research. For example, if the P3 reflects the perceptual decision relating to the location of the canonball (i.e. an evidence accumulation process) then, in line with the expectation-related bound modulations proposed in sequential sampling models, one would expect larger responses for less expected canonball locations and this would effectively fit the bill of a surprise response and would be expected to relate to conditional behaviour updating. Alternatively, and the peak timing of the P3 might speak to this, the P3 may largely/partly reflect the process of selecting the next shield position in light of the current outcome and more surprising events may prompt more careful deliberation resulting in high decision bounds and larger signal amplitudes. Our impression is that the present results are interesting in their own right but do not necessarily arbitrate among existing explanatory accounts of the P3.

In the final paragraphs the authors actually lay out a compelling account of what might be going on here without necessitating a full functional account of the P3: the P3 surprise response can play a role in triggering a change in the latent state. We suggest leading with this and following up with a discussion of the relevant theories.

2c) Relationship between P3 and the EEG component identified here.

While we appreciate the general "data-driven" approach used by the authors, we noticed that it inevitably raises questions about the relation to the so-called "P3 components" characterised in the oddball literature. This point requires more discussion.

3. Data analysis.

We believe that several aspects of the data analysis require further attention, specifically:

3a) The authors state that the critical PE*surprise*condition (or PE*EEG*condition) regressors indicate whether "surprise (EEG signal) tends to increase learning in the change-point condition but decrease learning in the oddball condition". But these interaction term regressors only test for a significant interaction – significant β weights do not imply a sign flip between conditions (increase in one condition, decrease in the other). For example, if surprise increased learning in the change point task, but does not correlate with learning in the oddball task, this might still yield a significant interaction. A sign flip should be assessed via posthoc comparisons.

3b) Subsection “Electrophysiological signatures of feedback processing”: With two conditions, oddball and changepoint, in this experiment, how can we have separate regressor weight estimates for both (one dummy variable coding condition would suffice/avoid collinearity)?

3c) The contrast "surprise" based on those two regressors might be modelled too liberally: A contrast setting both conditions to "1" is not necessarily identical to a true conjunction (i.e., both regressors driving the EEG significantly). This has been dealt with extensively in the fMRI/GLM literature. In short, outcomes from this "surprise" contrast are not necessarily as decisive as outcomes from a true difference contrast ("learning").

3c) Figure 5: Why should (behavioural) learning outcome be used to predict (on the y-axis) the temporally preceding positivity in the EEG? Also, the entire figure seems to stand on statistically shaky grounds, with p values in the.02-.04 range in highly sophisticated/convoluted models with many researcher degrees of freedom. Under the null, the result in Figure 5C would be as surprising (4 to 5 heads in row). The authors should do more to convince the reader that we are not looking at some lucky, highly selective results.

3d) The authors highlight an early frontocentral modulation in Figure 3 as being the P3a however the traces 3D indicate that this signal is equal in amplitude for expected and oddball stimuli. Shouldn't it be larger for oddballs if it is indeed a P3a?

3e) We suggest toning down the language in certain instances where the authors seem to imply that they have established a causal role for the P3 in belief updating e.g. Our findings are consistent with a number of studies that have suggested the P300 is related to surprise (9,14,17,24), but extend them by demonstrating the role of the signal in controlling the degree to which new information affects updated beliefs.

3f) The authors excluded 12/37 subjects excluded from EEG analysis because of low data quality. The criterion of excluding any subject with >25% artifactual trials seems rather stringent. Can you provide more rationale for the procedure? Are the main results robust with respect to such (arbitrary) selection criteria?

3g) 0.5 Hz is quite a severe high-pass cutoff and likely to attenuate some of the P3 activity. We don't think this could account for the significant effects of surprise etc but we would encourage the authors to repeat their key analyses with a substantially lower cutoff (e.g. 0.05 Hz) just to make sure that nothing changes

3f) What reference channel did the authors use for the EEG analyses – grand average?

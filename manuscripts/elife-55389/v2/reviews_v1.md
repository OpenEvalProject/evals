# Peer review - Round 1

Editors:
- John T Serences, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55389.sa1](https://doi.org/10.7554/eLife.55389.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "A Bayesian and efficient observer model explains concurrent attractive and repulsive history biases in visual perception" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Timothy Sheehan (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option.

In addition to all of the specific comments from the reviews, we especially focused on the following issues during consultation.

The clarity of model needs to be improved, both in terms of presentation and justifying choices as well as strengthening the link between the Bayesian decoding framework fit and other observations in the literature (e.g. that serial dependence emerges and increases with working memory delay period).

Both reviewers also focused on the importance of accounting for motor biases, which has been shown to be an important contributing factor in response bias for trial history effects (e.g. Akrami et al., 2018). See their comments for more specifics.

During consultation, the reviewers also raised the importance of considering the variability of the discrimination threshold. The current model is based on an efficient coding formulation from Wei and Stocker, which predicts that the discrimination threshold should be inversely proportional to the prior distribution. The authors could re-analyze the data to test this prediction, as least qualitatively.

Reviewer #1:

This manuscript clearly describes a previously underreported perceptual effect including many critical details such as time course and spatial specificity. Reported effects were robust and were replicated in two additional datasets. Fritsche et al. make sense of this phenomenon by building off of recent modeling work utilizing both principals of both Bayesian inference and efficient coding. This model is innovative by combining distinct concepts and introducing an exponential decay of trial influence across time. Critically, it provides a great fit to the pooled data both subjectively (Figure 7—figure supplement 1) and when quantified using cross validation (Figure 7—figure supplement 3). Overall this proposed model adds needed clarity to an area of research with much confusion and apparently contradictory results.

One point of concern is the lack of evidence for efficient encoding being the mechanism leading to repulsion. The authors do not cover an important feature (and the whole theoretical motivation for efficient encoding), that responses are more accurate (or discrimination thresholds smallest) for orientations where Fisher information is highest (see Stoker and Simoncelli, 2006: Figure 4). Since Fisher Information is directly linked to the prior probability, this would be supported by seeing a reduction is absolute error on trials with previous stimuli that are similar in orientation. In line with the exponential decay of efficient encoding, the magnitude of this change in response accuracy (perhaps parameterized with the second derivative of gaussian) should decay with time. If this does not hold true, then the authors should acknowledge other possible explanations for repulsion of previous stimuli including sensory adaptation from, for example, synaptic fatigue (see Solomon and Kohn, 2014).

Reviewer #2:

The authors examined historical effect in perception using data from one new experiment and three previously published datasets. They found both attractive serial dependence (Fischer and Whitney, 2014) and repulsive effect in the same experiments, and crucially the two effects have different time scales. To explain these findings, they modified an efficient coding-bayesian decoding framework (Wei and Stocker, 2015; 2017) and found that a modified model could fit the data well. The new ingredient of the current model is that the predictive prior used in Bayesian inference and efficient coding do not match each other. I think this work contains some interesting results, and could potentially help unify an array of previously disconnected findings. Having said that, I do find that various interpretations of the results to be problematic, and the presentation of the models to be very confusing.

1) Potential confounding factor, i.e., the motor biases, in the reproduction task.

I think it is important to rule this out, in particular for the attractive biases under short time scale. The results in Experiment 4 addresses the perceptual aspect of the long-term repulsive bias to some extent. However, I am puzzled why attractive biases were not observed/reported in this 2-AFC paradigm. If the serial dependence is a perceptual effect, shouldn't we expect attractive biases at short-term scale? I had a difficult time reconciling the results in the two paradigms.

2) The calculation of the historical effect:

Should the attractive/repulsive bias be considered with respect to the orientation of the stimulus or the reported orientation? It would be useful to run the analysis using the reported orientation. Barbosa and Compte (2020, bioRxiv) reports the serial dependence is stronger with using reported stimuli. It would be useful to check whether that's also the case in the authors' data.

If the historical effect need depends on the reported orientation, there seems to be a following-up concern. This one is perhaps naive but could be potentially important if it's true: could attraction biases (toward reported stimulus value) at the short-time scale automatically lead to repulsion at longer time-scale? It would be useful to simulate a ground-truth model with just attraction toward the reported (but no generic repulsion) to see if using the authors' analysis procedure would lead to repulsive effect in longer time scale.

3) The spatial dependence of repulsion and attraction:

The authors claim the attractive biases are not spatially specific (Figure 3), while the repulsive biases are spatially specific. The spatial specificity of the repulsive bias is interpreted as to be consistent with the adaptation effect as measured previously. I found this to be problematic. The two stimulus locations are separated by 13° eccentricity, yet there is still a clear repulsive effect for the "different location" condition. I'd think classical orientation adaptation would lead to almost zero after-effect when the stimulus was to presented to that far away from the adaptor.

4) The role of the noise patch in the experiments is obscure.

If removing the noise patch and using a blank screen instead, would one still observe similar effect? The computational models do not model the noise patch, so I'd think it is fair to say that the model should predict that removing the noise patch would not change any of these biases.

Alternatively, perhaps the noise patch does play a rule. In Experiment 4, noise patch was not used, and interestingly the attractive bias was not observed. So could the noise patch be the main reason why different effects were observed for the two paradigms (this also relates back to my first concern)?

5) The explanation/presentation of the model is highly confusing.

The labeling of efficient coding model and Bayesian decoding model is particularly mis-leading. Each of the models consider in this paper has an efficient encoding component and a Bayesian decoding component. So I found it is strange to label one as encoding model and another as decoding model.

Relatedly, in the sixth paragraph of the subsection “Repulsive and attractive biases can be explained by efficient encoding and optimal decoding of visual information”, the model the authors referring to is a model consisting efficient coding and Bayesian decoding with mismatched prior. It is the mis-match between the encoding and decoding that leads to the explanation power.

Again it is misleading to talk about model with "only Bayesian decoding" or with "only efficient coding". I feel that it is not what actually happens in the models, unless I am profoundly confused with what the authors actually did.

These are some of the instances in the paper which could lead to profound confusions. I'd suggest the authors to systematically re-write the last section of the Results and the related section in the Discussion to make it clear.

6) The dependence of historical biases on time scales within a single experiment has been reported previously. For example, Dekel and Sagi, 2015, reported a sign reversal of the biases when examining different time-scales in adaptation experiments using natural stimuli (their Figure 4). Interestingly, they found the opposite pattern, i.e. repulsion at short-time scale, attraction at longer-time scale. There might be other related studies I missed. I feel that the authors should discuss the relevant findings more thoroughly.

Reference:

Barbosa, João, and Albert Compte. "Build-up of serial dependence in color working memory." bioRxiv (2019): 503185.

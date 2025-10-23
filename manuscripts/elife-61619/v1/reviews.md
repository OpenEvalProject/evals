# Peer review - Round 1

Editors:
- Andrew J King, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61619.sa1](https://doi.org/10.7554/eLife.61619.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This computational modeling study examines how experimentally characterized patterns of spontaneous activity, thought to arise either locally or to be driven by events in the eye, can influence the developmental refinement of connectivity and receptive field properties in the visual cortex. The theoretical framework set out by the authors provides new insight into the role of spontaneous activity, which is present before vision starts, and will no doubt inspire future experimental studies.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Adaptation of spontaneous activity in the developing visual cortex" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: József Fiser (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

This manuscript addresses the important and interesting topic of the role of spontaneous activity at different levels of the visual pathway in the emergence of topographically-organized V1 receptive fields. Although the reviewers commended the modelling and data analyses, as well as the quality of the writing, they did not think that this study provides fundamental insights into the biological mechanisms responsible for establishing the connectivity and response properties of cortical neurons. In addition, it was felt that the study lacked novelty in some aspects and that some of the findings presented had been over interpreted.

Reviewer #1:

This paper provides a detailed theoretical analysis of how different types of spontaneous activity influence receptive field development in the cortex. The model is well-grounded, the simulations are supported by nice mathematical analyses, and the paper is well written. Overall I think it's good work and certainly worthy of publication in a solid journal. However I don't think it provides the level of advance appropriate for eLife. My main concerns in this regard are as follows.

1) The paper shows how the deleterious effects of H events can be mitigated, but it doesn't explain why H events are present in the first place. Overall the results don't seem very surprising, and I don't think there's a huge amount of new insight into the underlying biological principles.

2) The modelling and analytical tools used have already been thoroughly investigated. For instance Equation 2 is Equation 8.9 in the Dayan and Abbott textbook, the eigenvector analysis is very similar to that in Mackay and Miller, 1990, and many of the principles relevant to this work were already established by Willshaw and von der Malsburg, 1976. While all this certainly supports the soundness of the work presented here, it does undermine its novelty.

3) I think the experimental finding that the amplitude of L and H events preceding a given H event are correlated could be explained simply by long-term fluctations in overall cortical excitability, rather than being a confirmation of the model.

Reviewer #3:

This manuscript aims at reconciling the roles of spontaneous activities of thalamic vs. cortical origin in the establishment of cortical connectivity and known neural characteristics of those activities. The authors propose the existence of an amplitude-adaptation mechanism for the cortically generated spontaneous activity and test this idea by re-analyzing previous in vivo data and perform simulation on a 1D model of cortical development.

I find the paper clearly written, the data analyses and the simulations adequately executed. However, I also think some additional effort to clarify the exact contribution of the paper, the link between analyses and the claims of the paper and its link to previous proposals would be necessary to better assess the significance of the proposed model. In addition, clear predictions justifying the insight of the work would further improve the value of the manuscript.

I had three issues when reading the manuscript, handling of which might help to increase the impact of the paper.

First, it seems to me that describing the exact contribution of the paper should be better elaborated. My understanding is that the course of action of the paper is this: (a) taking up the experimental findings of Siegel et al., 2012, about the two independent sources of activity generation in the developing visual system (thalamic and cortical), the authors tried to fold these constraints to the computational requirements of topographic pattern formation. (b) After choosing one particular implementation, they realized and demonstrated that an adaptive tuning of the global H-events' amplitude is needed for stable behavior in this model. Finally, (c) after reanalyzing the original Siegel et al., 2012, data, they found evidence for such an adaptive mechanism. In addition, they linked their work to the concept of sparsification of neural signal for efficient coding.

If this is correct, I would like to know the answer to the following set of questions.

1) Why the postulation of H-events acting homeostatically? It is clear that this assumption can step in for the missing normalization functionality necessary for the Hebbian plasticity rule to operate properly, but there are other options as well. Did the authors have a more established reason to go with this choice? Beyond being a heterosynaptic learning rule, in what way the resulting Hebbian input-threshold learning rule is different from or more adequate than other realizations (e.g. the ones based on pre-post synaptic activities)? And wrt other heterosynaptic rules?

2) When arguing for evidence in the Siegel et al., 2012, data based on the fact that the amplitude of an H-event and the amplitudes of H- and L-events in the preceding 100 msec are correlated, how can they rule out the alternative that the correlation is not a result of an active adaptation mechanism for H-events, but due to a general fluctuation of both L- and H- event amplitude magnitudes in time caused by other factors? Shouldn't the existence of active adaptation mechanism be supported by showing a causal proportionality based on some aggregate sum of amplitudes and frequencies of preceding events in a specified window rather than just a time-insensitive amplitude-to-amplitude correlation the authors demonstrate?

My second issue is related to the notion of sparsification, which has been widely but typically very loosely used in the literature, and the manuscript seem to follow this trend. For a sufficient treatment of sparsification, see Willmore and Tolhurst, 2001, Berkes et al., 2009 and Zylberberg et al., 2013. A full treatment of sparseness includes (a) proper definitions (i.e. distinguishing between population and lifetime sparseness of neural activity), (b) the clarification that sparsification can be interpreted as a principle either for energy conservation, in which case lifetime sparseness is the appropriate measure, and homeostasis is a possible implementation, or for efficient coding for which population sparseness is the proper measurement, and regulation of the individual firing rates is an insufficient proxy, and (c) using the proper sparseness for the actual argument. The Siegel et al., 2012, paper carefully uses the term "event" sparsification, which refers to the occurrence of waves, bursts, which has only indirect connection to information processing capacity as is was implied (but not clearly spelled out) in Olshausen and Field, 1996. The Rochefort et al., 2009, paper does refer to sparsity of neural activity, but it neglects the fact that by measuring percentage of active neurons in any one event itself does not capture the information processing capacity of the network either.

3) My problem is that it is unclear what the present manuscript aims at: is it simply trying to match the Siegel et al. recorded data with their model (which they show in the manuscript) without any attempt to link that to information processing, or alternatively, they give their model a functional spin by tying to link the results to the concept of efficient coding, in which case a whole different set of analyses is required. According to the authors "…we observe a progressive sparsification of the effective spontaneous events during ongoing development in our model. ". This would suggest that they are describing event statistics. But then in the Discussion, they refer to the efficient coding aspect of spike sparsification for which there is no adequate analysis provided in the manuscript. Given that this is a computational modelling paper, it would help to get a clear statement about and the corresponding analysis supporting the goals the authors have with referring to sparsification. The proposed adaptation of the H-events amplitudes would have a significant effect on efficient coding, and this is a different issue from map formation. I wonder if the authors want to dive into that issue, but in any case, it would be necessary to clarify what type of sparsification the authors discuss in the manuscript.

My third comment is pointing out that the authors did not provide any testable prediction based on their new model, if I am not mistaken.

4) If the new idea is that amplitude-adaptation must exist in the cortex, proposing a test that can verify this directly would be invaluable.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Adaptation of spontaneous activity in the developing visual cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: József Fiser (Reviewer #1); Nicholas V Swindale (Reviewer #2); Jianhua Cang (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This modelling study shows that a set of rules involving adaptation can lead to developmental changes in the visual cortex that match those observed experimentally, including receptive field formation, synapse stabilization and a slow sparsification of spontaneous activity. The biological applications of this study are important and interesting. The proposed roles of local low-synchronicity events originating in the retina and global high-synchronicity events originating in the cortex, and the associated predictions from this research, will stimulate future experimental work.

Revisions:

The reviewers were generally positive, but raised several concerns that will need to be addressed satisfactorily before your paper can be considered to be acceptable for publication in eLife. While the assessment of this work took into account the revisions made to the previously rejected manuscript, it was considered as a new submission and has therefore attracted additional comments.

1) The direct comparison with the BCM learning rule has increased the value of the paper significantly. Nevertheless, questions were raised about more conventional normalization schemes. We appreciate that it would be excessive to test all existing alternatives. However, alternatives do need to be considered and the authors should explain how these compare to the non-adaptive-augmented version of your original model, and explain why, if only one contrasting alternative is to be tested, BCM is the right choice.

2) The manuscript has benefited from making the main text lighter and shifting much of the standard mathematical treatment to the Appendix. Nevertheless, the reviewers felt that the presentation of the manuscript could be improved further to more clearly explain the proposed links between model behaviour and real development and to make it easier for experimentalists to follow.

3) There was some discussion among the reviewers about the classification of spontaneous events into H and L types. Because this is critical for the study, further explanation of the previous evidence for this would be helpful.

4) The fact that the model itself produces L and H events seemed to throw a spanner into the works. One criticism of the model is that in the real brain, cortical spontaneous activity is not likely to be imposed from outside, as in the model, but is integral to the overall developmental dynamics and might involve circuits beyond the scope of the model that could regulate plasticity if needed. But now the significance of the imposed events seems to be called into question. It certainly does not help that H events can now be effectively identified as L events, resulting in confusion as to how to interpret what was going on and hence to evaluate the significance of the model.

5) Figure 2: the initial conditions were noisy but arguably not much different in other respects from the final state. Can you use much broader and more scattered initial receptive field widths? Is more than a bit of smoothing and weight thresholding going on?

6) The method used to show adaptation in the experimental data is unclear. Surely the exponential is used to scale the weights of the values that go into the running average, not their amplitude? Assuming that is the case, what is the point of having a time constant for the averaging of 1000s when recordings do not last longer than 300 s? Effectively it is an unweighted average, or close to it.

7) Can the correlation between the amplitude of an H event and the average amplitude of preceding events shown in Figure 5B be more parsimoniously explained by slow changes in the overall signal strength over time? This was felt to be a key issue.

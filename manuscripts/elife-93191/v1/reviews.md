# Peer review - Round 1

Editors:
- Tobias H Donner, University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93191.4.sa0](https://doi.org/10.7554/eLife.93191.4.sa0)

This valuable article explores the idea that transient modulations of neural gain promote switches between distinct perceptual interpretations of ambiguous stimuli. The authors provide solid evidence for this idea by pupillometry (an indirect proxy of neuromodulatory activity), fMRI, neural network modelling, and dynamical systems analyses. The highly integrative nature of this approach is rare in the field.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93191.4.sa1](https://doi.org/10.7554/eLife.93191.4.sa1)

Summary:

This paper proposes a neural mechanism underlying the perception of ambiguous images: neuromodulation changes the gain of neural circuits promoting a switch between two possible percepts. Converging evidence for this is provided by indirect measurements of neuromodulatory activity and large-scale brain dynamics which are linked by a neural network model. However, both the data analysis as well as the computational modeling are incomplete and would benefit from a more rigorous approach.

This is a revised version of the manuscript which, in my view, is a considerable step forward compared to the original submission.

In particular, the authors now model phasic gain changes in the RNN, based on the network's uncertainty. This is original and much closer to what is suggested by the phasic pupil responses. They also show that switching is actually a network effect because switching times depend on network configuration (Fig 2). This resolves my main comments 1 and 2 about the model.

The mechanism, as I understand it, is different from what the authors described before in the RNN with tonic gain changes. As uncertainty increases, the network enters a regime in which the two excitatory populations start to oscillate. My intuition is that this oscillation arises from the feedback loop created by the new gain control mechanism. If my intuition is correct, I think it would be worth to explain this mechanism in the paper more explicitly.

Comments on revisions:

This is a second revision. I have no further comments. The authors have not answered the question that I had in the previous round (about the origin of oscillations in the RNN). I think this topic deserves to be explored in more detail but perhaps that is beyond the scope of the current paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93191.4.sa2](https://doi.org/10.7554/eLife.93191.4.sa2)

This paper tests the hypothesis that perceptual switches during the presentation of ambiguous stimuli are accompanied by changes in neuromodulation that alter neural gain and trigger abrupt changes in brain activity. To test this hypothesis, the study combines pupillometry, artificial recurrent network (RNN) analysis and fMRI recording. In particular, the study uses methods of energy landscape analysis inspired by physics, which is particularly interesting.

Strengths

- The authors should be commended for combining different methods (pupillometry, RNNs, fMRI) to test their hypothesis. This combination provides a mechanistic insight into perceptual switches in the brain and artificial neural networks.

- The study combines different viewpoints and fields of scientific literature, including neuroscience, psychology, physics, dynamical systems. In order to make this combination more accessible to the reader, the different aspects are presented in a pedagogical way to be accessible to all fields.

- This combination of methods and viewpoints is rarely done, so it is very useful.

- The authors introduce dynamic gain modulation in their recurrent neural network, which is novel. They devote a section of the paper to studying the dynamics, fixed points and convergence of this type of network.

Weaknesses

- The study may not be specific to perceptual switches. This is because the study relies on a paradigm in which participants report when they identify a switch in the item category. Therefore, it is unclear whether the effects reported in the paper are related to the perceptual switch itself, to attention, or to the detection of behaviourally relevant events. The authors are cautious and explicitly acknowledge this point in their study.

- The demonstration of the causal role of gain modulation in perceptual switches is partial. This causality is clearly demonstrated in the simulation work with the RNN. However, it is not fully demonstrated in the pupil analysis and the fMRI analysis. One reason is that this work is correlative (which is already very informative).

- Some effects may reflect the expectation of a perceptual switch rather than the perceptual switch itself. To mitigate this risk, the design of the fMRI task included catch trials, in which no switch occurs, to reduce the expectation of a switch. The pupil study, however, did not include such catch trials.

- The paper uses RNN-based modelling to provide mechanistic insight into the role of gain modulation in perceptual switches. However, the RNN solves a task that differs from that performed by human participants, which may limit the explanatory value of the model. The RNN is provided with two inputs characterising the sensory evidence supporting the first and last image category in the sequence (e.g. plane and shark). In contrast, observers in the task don't know in advance the identity of the last image at the beginning of the sequence. The brain first receives sensory evidence about the image category (e.g. plane) with which the sequence begins, which is very easy to recognise, then it sees a sequence of morphed images and has to discover what the final image category will be. To discover the final image category, the brain considers several possibilities for the second images (it is a shark?, a frog?, a bird?, etc.), rather than comparing the likelihood of just two categories. This search process among many alternatives and the perceptual switch in the task is therefore different from the competition between only two inputs in the RNN.

- Another aspect of the motivation for the RNN model remains unclear. The authors introduce dynamic gain modulation in the RNN, but it is not clear what the added value of dynamic gain modulation is. Both static (Fig. S1) and dynamic (Fig. 2F) gain modulation lead to the predicted effect: faster switching when the gain is larger.

- The authors are to be commended for addressing their research questions with multiple tools and approaches. There are links between the different parts of the study. The RNN and the pupil are linked by the notion of gain modulation, the RNN and the fMRI analysis are linked by the study of the energy landscape, the fMRI study and the pupil study are indirectly linked by previous work for this group showing that the peak in LC fMRI activity precedes a flattening of the energy landscape. These links are very interesting but could have been stronger and more complete.

Comments on revisions:

I thank the authors for their responses.

My review presents points that the authors themselves present as weaknesses or limitations. It also includes points that cannot be addressed in a revision (e.g. causality).

Regarding the fact that the RNN only considers two categories, whereas subjects consider more categories (because they don't know the final image), I have toned down my remark (removing "markedly" different, removing the fact that the hypothesis space is vast given that participants have some priors). I also removed the qualifier "mechanistically" different, because it can be understood in different ways. The point remains that the proposed model has 2 inputs, the corresponding network in the brain has >2 inputs (because it considers more categories than the RNN), which is different, and which is the point of my remark. I think it may limit the value of the model, but I don't think it is not "sensible".

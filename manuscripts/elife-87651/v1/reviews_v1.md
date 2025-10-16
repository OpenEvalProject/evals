# Peer review - Round 1

Editors:
- Leonardo Elias, State University of Campinas Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87651.4.sa0](https://doi.org/10.7554/eLife.87651.4.sa0)

The work by O'Reilly and Delis is important to extend the synergy ideas using methods from signal processing and information theory to cluster muscles and task parameters, thereby advancing our understanding of the modular architecture of motor control. The method is innovative, and the findings are compelling from theoretical and practical perspectives. The work will be of broad interest to motor control and neural engineering researchers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87651.4.sa1](https://doi.org/10.7554/eLife.87651.4.sa1)

The proposed study provides an innovative framework for the identification of muscle synergies taking into account their task relevance. State-of-the-art techniques for extracting muscle interactions use unsupervised machine-learning algorithms applied to the envelopes of the electromyographic signals without taking into account the information related to the task being performed. In this work, the authors suggest to include the task parameters in extracting muscle synergies using a network information framework previously proposed. This allows the identification of muscle interactions that are relevant, irrelevant, or redundant to the parameters of the task executed.

The proposed framework is a powerful tool to understand and identify muscle interactions for specific task parameters and it may be used to improve man-machine interfaces for the control of prostheses and robotic exoskeletons.

With respect to the network information framework recently published, this work added an important part to estimate the relevance of specific muscle interactions to the parameters of the task executed.

It is not clear how the well-known phenomenon of cross-talk during the recording of electromyographic muscle activity may affect the performance of the proposed technique and how it may bias the overall outcomes of the framework.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87651.4.sa2](https://doi.org/10.7554/eLife.87651.4.sa2)

This paper is an attempt to extend or augment muscle synergy and motor primitive analyses and ideas with addition of task-driven measures. The authors' idea is to use information metrics (mutual information, co-information) in 'synergy' constraint creation that includes task information directly. By using task related information and muscle information sources and then sparsification, the methods construct task relevant network communities among muscles, together with task redundant communities, and task irrelevant communities. This process of creating network communities may then constrain and help to guide subsequent synergy identification using the authors published sNM3F algorithm to detect spatial and temporal synergies. The revised paper is now much clearer and examples are helpful in various ways.

The impact of the information theoretic constraints developed as network communities on subsequent synergy separation are posited to be benign and to improve separation and identification of synergies over other methods (e.g., NNMF). However, not fully addressed are the possible impacts of the methods on the resulting compositionality and its links with physiological bases: the possibility remains that the methods here sometimes will instead lead to modules that represent more descriptive ML frameworks for task description, and resulting 'synergies' that may not support physiological work easily. Accordingly, there is a caveat for users of this framework. This is recognized and acknowledged by the authors in their rebuttal letters responding to prior reviews. It will remain for other work to explore this issue, likely through testing on detailed high degree of freedom artificial neuromechanical models and tasks. This possible issue and caveat with the strategy proposed by the authors likely should be more fully acknowledged in the paper.

The approach of the methods seeks to identify task relevant coordinative couplings. This identification is a meta problem for more classical synergy analyses. Classical/prior analyses seek compositional elements stable across tasks. These elements may then be explored in causal experiments and in generative simulations of coupling and control strategies. However, task-based understanding of synergy roles and functional uses as captured in the proposed methods are significant, and the field is clearly likely to be aided by methods in this study.

Information based separation has been used in muscle synergy analyses previously, by using infomax ICA, to discover physiological primitives. Though linear mixing of sources is assumed in ICA, minimized mutual information among source (synergy) drives is the basis of the separation and can detect low variance synergy contributions (e.g., see Yang, Logan, Giszter, 2019). In the work in the current paper, instead, mutual information approaches are used to cluster muscles and task features into network communities preceding the SNM3F algorithm use for separation, rather than using minimized information in the separation process directly. This contrast of an accretive or agglomerative mutual information strategy in the paper here, which is used to cluster into networks, versus a minimizing mutual information source separation used in infomax ICA epitomizes a key difference in approach. Indeed, physiological causal testing of synergy ideas is neglected in the literature reviews presented in the paper. Although these are only in animal work (e.g., Hart and Giszter, 2010; Takei and Seki, 2017), the clear connection of muscle synergy analysis choices to physiology is important, and eventually these issues need to be better managed and understood in relation to the new methods proposed here, even if not in this paper. Analyses of synergies using the methods the paper has proposed will likely be very much dependent on the number and quality of task variables included and how these are chosen, and the impacts of these on the ensuing sparsification and network communities used prior to SNM3F has already been noted. The authors acknowledge this in their responses. It would be useful in the future to explore the approach described with a range of simulated data to better understand the caveats, and optimizations for best practices in applications of this approach.

A key component of the authors' arguments here is their 'emergentist' view presented in the work, but perhaps not made fully explicit. Through the reductionist lens, which was used in the other physiological work noted above, muscle groupings are the units (primitives or 'building blocks' with informational separations) of coordinated movement and thus the space of these intermuscular unit interactions and controls is of particular interest for understanding movement construction and underlying physiology. This may allow representation of a hierarchy or heterarchy of neural control elements with clear physiological bases at spinal, brainstem and cortical levels. On the other hand, the emergentist view utilized by the authors here suggests that muscle groupings emerge from interactions between many constituent parts in a more freeform fashion with potentially larger task synergy assemblies (also quantified here using information tools). Information methods are applied differently using the two different lenses. The emergentist lens may potentially obscure fundamental neural controls and make them harder to explore in the descriptions resulting. Nonetheless, the different approaches to muscle synergy research, seeking different sorts of explanation and description of 'synergy', can be complementary and beneficial for the field overall going forward, so long as the caveats and concerns noted here are employed by readers in the interpretation of this new method.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87651.4.sa3](https://doi.org/10.7554/eLife.87651.4.sa3)

In this study, the authors developed and tested a novel framework for extracting muscle synergies. The approach aims at removing some limitations and constrains typical of previous approaches used in the field. In particular, the authors propose a mathematical formulation that removes constrains of linearity and couple the synergies to their motor outcome, supporting the concept of functional synergies and distinguishing the task-related performance related to each synergy. While some concepts behind this work were already introduced in recent work in the field, the methodology provided here encapsulates all these features in an original formulation providing a step forward with respect to the currently available algorithms. The authors also successfully demonstrated the applicability of their method to previously available datasets of multi-joint movements.

Preliminary results positively support the scientific soundness of the presented approach and its potential. The added values of the method should be documented more in future work to understand how the presented formulation relates to previous approaches and what novel insights can be achieved in practical scenarios and confirm/exploit the potential of the theoretical findings.

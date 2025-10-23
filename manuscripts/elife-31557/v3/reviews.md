# Peer review - Round 1

Editors:
- Jack L Gallant, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31557.034](https://doi.org/10.7554/eLife.31557.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Sensory cortex is optimized for prediction of future input" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Reviewing Editor Jack Gallant and Senior Editor Sabine Kastner. The following individuals involved in review of your submission have agreed to reveal their identity: Rhodri Cusack (Reviewer #1); Laurenz Wiskott (Reviewer #2); Christoph Zetzsche (Reviewer #3).

The reviewers have discussed the reviews with one another, and they and the Reviewing Editor agree that your paper is potentially suitable for publication in eLife after appropriate revision. The Reviewing Editor has drafted this decision to help you prepare a revised submission.

The Reviewing Editor hopes that you will address all of the concerns of the authors, most of which are straightforward. But to help you in revision the major issues are listed here:

1) If you look at the reviews you will see that the list of suggestions is very long, but the vast majority of the comments only ask for clarification, they do not require additional data analysis or substantial rewriting. It would be good if you could address all questions in your reply to reviewers and revise the text appropriately where necessary to provide necessary information to the reader.

2) The proposed model is interesting, but it has many components that may differentially contribute to the result, such as the nonlinearity or L1 regularization. The reviewers felt that the paper would be stronger if the specific effects of these various model component choices were analyzed in a bit more detail, in order to try to pin down more precisely why these components are important. (See for example suggestions of reviewer 2.)

3) In some places the choices made during modelling seemed arbitrary (e.g., the choice of temporal windows and the regularization parameters). Either grid search over a training set should be used to choose these parameters, or hyperparameter modelling should be performed to show that the specific values chosen are not critical, or the choices should be justified. The first of these is obviously most desirable.

4) Some of the figures are difficult to interpret (c.f. Figure 7B and Figure 7—figure supplement 2B). Please try to improve the figures where necessary.

5) Please address the concerns of reviewer 3 regarding the introductory material on temporal prediction and the neurobiological plausibility of the approach.

Reviewer #1:

This manuscript compares two stimulus coding principles that could explain the form of receptive fields in sensory cortex: efficient sparse coding and temporal prediction. A simple temporal prediction model was found create receptive fields that were similar in many ways to those seen in sensory cortex. It performed much better than a sparse coding model.

This manuscript makes an interesting and important contribution. The "sparse coding" hypothesis is popular, both in neuroscience and in artificial intelligence, where autoencoding in deep-neural networks implements efficient coding. The authors argue that for dynamic stimuli, the need to predict what will happen next may be a more important than merely encoding efficiently what has happened recently. Their model is simple and elegant, and the results are convincing.

I felt there were some places where choices were made during modelling that seemed arbitrary – such as the choice of temporal windows and the regularization parameters. The manuscript would be stronger if these choices were either justified, or hyperparameter modelling done to show that the specific values chosen are not critical, to allay concerns readers may have of "p-hacking".

I found the manuscript to be well-structured, thorough and well written, clearly conveying a convincing message.

Reviewer #2:

The paper presents a two-layer network optimized for predicting immediate future sensory input (auditory or visual) from recent past sensory input. The resulting spatio- or spectrotemporal receptive fields, i.e. weight vectors of the first layer, are analyzed and compared with physiological receptive fields. For model comparison, results from a sparse coding network are used.

The results show that the predicting neural network captures receptive field properties fairly well, in particular temporal structure is reproduced much better than by the sparse coding network.

The topic is interesting, and the results are highly relevant to the field. I must add, however, that I have not followed the field recently, so I cannot really tell, whether some similar work has been published recently. But the authors seem to have done a careful literature research and discuss alternative approaches fairly.

The paper is well structured and has obviously been written very carefully. I have rarely reviewed a manuscript that feels so ready for publication. So, I am tempted to recommend the paper for publication as it is.

There is just one issue I would invite the authors to consider a bit further: The claim of the paper is that the objective of temporal prediction results in the receptive field properties found. But there are additional factors, such as the nonlinearity and the L1 regularization, that contribute to it. The authors have investigated this to some extent. For example, they find that receptive fields are seriously degraded if the nonlinearity is replaced by a linear activation function. My suggestion is to try to pin down, what objective is implicitly added by the nonlinearity and the L1 regularization. I suggest to perform a similar experiment as in Figure 8, but with a sparseness or independence measure rather than final validation loss. This could also be done on the hidden units.

I suggest this, because I believe that temporal prediction alone does not do the trick. I feel it must be combined with some sparseness or independence objective to yield the receptive fields. And I feel that this missing objective is implicitly added by the nonlinearity and the L1 regularization. Making this more transparent would be great and the suggested experiment should be very easy to do.

Reviewer #3:

The authors propose a new principle for the development of cortical receptive fields which combines the concepts of predictive coding and sparse coding. They train a three-layer network with one hidden layer in order to predict the future visual spatial input or the future auditory auditory spectro-temporal input from the recent spatio-/spectro-temporal input, subject to a sparsity constraint.

They perform this training for two examples: for an auditory network, based on training data which contain human speech, animal vocalization and inanimate natural sounds, and for a visual network based on training data with movies of wildlife in natural settings.

They compare the resulting networks to real cortical neurons from A1 and V1 and to an alternative sparse coding approach intended to provide a sparse representation of the complete spatio/spectro-temporal input.

For their comparison they consider the spectrotemporal and spatiotemporal receptive fields and various population measures, e.g. the temporal decay of power in the receptive fields, the temporal span of excitation an inhibition, orientation and frequency tuning properties, and receptive field dimensions.

Except for orientation, for which the majority of visual units is restricted in their orientation preference to horizontal and vertical orientations, the proposed model can capture neural tuning properties as well as the established models. And in case of the asymmetric emphasis of the most recent past it can even provide a better description.

In my opinion this is a quite interesting paper. First, it presents a novel approach which unifies the principles of sparse coding and of temporal prediction. This combination enables the explanation of a large set of spatio-/spectro-temporal tuning properties within one single integrated framework. Second, the authors have an important point in stressing the asymmetry of the temporal response with its emphasis of the most recent past, as observed in typical cortical neurons. This is indeed a property that other learning schemes, like sparse coding, by the very nature of their objective functions, cannot produce.

There are some points that, in my view, need to be clarified or described in more detail. In the following I describe the modifications and additions which I assume to be helpful in a revision of the paper. Due to my background I will put more emphasis on the visual aspects.

1) The description of the history of the concept of temporal prediction is not clear enough, both in the introduction and in the discussion. I am aware of the pressure for novelty in current science but in my view, there is sufficient novelty in the suggested model to allow the authors to avoid such ambiguities. Currently, the paper might be misinterpreted by a swift non-specialist reader as if the concept of the "prediction of the immediate future" is a novel principle being introduced here (Introduction; Discussion section: "We hypothesized"). Only a few selected papers are cited directly in this context (only Bialek in the Introduction), and in the Discussion section they are characterized as unspecific: "The temporal prediction principle we describe.… has been described in a very general manner"(reference only to Bialek, Palmer). Other references exist but are spread out through the further text. But of course, the principle as such has a long history, there are numerous papers which describe the prediction of the future sensory input as an important goal of neural information processing. I am no specialist, and this is not comprehensive but early examples are corollary discharge theories, and already Sutton and Barto, (1981) and Srinivasan et al., (1982), for example, considered the temporal dimension of prediction. Motion extrapolation has also been interpreted as prediction computed in visual cortex (Nijhawan, 1994). A further, canonical example of a method for the optimal prediction of the future sensory input is the Kalman filter, as considered by, e.g., Rao, (1999). I suggest that the authors devote one paragraph to the history of the concept, with all the appropriate references included there, and then make precisely clear in which aspects their novel contribution extends beyond these earlier approaches.

2) Neurobiological plausibility of the approach: I do not think that the authors have to be as clear about the neural implementation of the suggested architecture as the other predictive coding approaches, but at least some rough or speculative ideas should be presented: What is the status of the second-order units? Where in the cortex are they (V2?) and what do they encode? Really the future INPUT itself? That is, they have no selectivity, no tuning properties? Have such units been observed? Where and how is the prediction error computed? Does this model not require a bypass line which brings the retinal spatial input directly to V1 or V2 to enable the comparison?.…

3) The sparse coding data appear quite unusual. Why are the units not more "localized" in the temporal dimension, in particular for the visual model? Furthermore, it seems as if the visual sparse model is not used in the usual overcomplete regime. I also would have expected a more concentrated distribution of the temporal span of excitation and inhibition for a typical sparse coding model. Please discuss this in the paper.

4) Subsection “Model receptive fields” by inspection: is there really no other possibility to determine the optimal hyperparameters of the sparse coding model? A fit to the neural data? You have Figure 8—figure supplement 1B anyway. Why have you not made use of it? One could use only a training subset, if this seems critical issue. And one can include KS measures of other tuning properties.

5) Subsection “Addition of Gaussian noise”: Noise. For me the use of noise in this investigation is somewhat unclear. First, it seems to favor the prediction model over the sparse model, which is more susceptible to noise. Second, the noise level used appears unusually strong (is this dB?). This issue should be clearly motivated and discussed in the main text of the paper.

6) Subsection “Model receptive fields”: I am a bit skeptic with respect to the sign-flipping of excitation and inhibition. The argument that the signs could as well be flipped if this is done for the first-order and the second-order units alike appears only valid because any specification and relation to real neurons is omitted for the second-order units. In fact, this sign-flipping will inevitably imply a prediction of how excitation and inhibition operate in the second-order units.

Furthermore, if this argumentation would be accepted then one could arbitrarily flip signs to the desired result in any learning model, because one can always argue that appropriate sign flips at some subsequent processing stages could compensate for this. Used in this way, excitation and inhibition would lose any meaning.

It is perfectly ok for me if a model is agnostic with respect to the correct prediction of excitation and inhibition, a model does not have to be perfect in all aspects. But if this is the case this should be clearly visible for the reader in the presented receptive field plots. (This does not exclude to use of an appropriate sign-flip in population measures.)

7) Figure 4—figure supplement 2 and Figure 4—figure supplement 3: Two separate populations? Visual inspection of these figures suggests the possible existence of two distinct populations. Is this related to separability, or blob-like units, or both? (Is ordering according to separability?) I am not sure about the current state in the field, but I remember a discussion about the existence of two distinct populations as opposed to a continuous distribution for separability. This issue should be described and discussed.

8) ibid. The percentage of blob-like units appears quite high. Is this percentage comparable to the neural data? Or only if the mouse data, which are special in this respect, are being included?

9) Figure 4—figure supplement 6 The percentage of blob-like units seems to be substantially reduced in comparison to the noisy case (Figure 4—figure supplement 2). Is there a systematical relation between high noise levels and the emergence of blob-like units? Please discuss this issue in the paper.

10) ibid. It is difficult to understand the relation between Figure 4—figure supplement 2 and Figure 7C as opposed to Figure 4—figure supplement 6 and Figure 7—figure supplement 2F. Can you describe how properties of the receptive field plots relate to properties of the population distribution in these two cases?

11) Figure 7 and others Spatiotemporal population properties: Although the article is about spatiotemporal processing it provides only two population measures of purely static spatial properties and one of a purely temporal property for the vision case. Spatiotemporal measures of particular interest would be: DSI (directional selectivity index)/TDI (tilt direction index) (direction selectivity is considered to be a major spatiotemporal property of visual cortex); if possible: a scatter plot of temporal frequency vs. spatial frequency; population distribution of motion tuning. The necessary data for these plots should be already available.

12) Figure 7B and Figure 7—figure supplement 2B: The orientation scatter plot is visually difficult to interpret. The quantitative degree of concentration of the preferred orientations on the vertical and horizontal orientations as opposed to the oblique orientations remains unclear. Please provide either an orientation histogram or the percentage of units which fall into the 30-60, 120-150 deg range. In both cases the lowest spatial frequencies should be omitted for the analysis.

13) Figure 7—figure supplement 1: I am a bit surprised that only 289/400 sparse-coding units can be fitted by a Gabor function. Why is this? Usually most sparse coding units have a good Gabor fit. And with such a high percentage excluded I see the risk of a systematic bias regarding certain tuning parameters.

14) Figure 7C and Figure 7—figure supplement 2F seem to indicate that the model produces two distinct sub-populations with respect to receptive field parameters n_x and n_y. It should be discussed whether this is the case, and if yes, whether it is systematically related to other parameters (selectivities) of the units. Could this be related related to the two apparent sub-populations regarding separability, blob-like shapes, cf. Figure 4—figure supplement 2? And has such a tendency has also been observed in neural data? In contrast, Ringach, (2004) claimed clustering around a one-dimensional curve. Please describe and discuss in text.

15) Figure 8 and subsection “Implementation details: Are we expected to see here that 1600 hidden units are a distinguished optimum? Does this figure not tell us that the prediction error does not substantially depend on the number? And when a biological system could achieve basically the same prediction quality with 100 neurons why should it then invest 1500 additional units for such a small advantage?

16) Figure 8 and Figure 8—figure supplement 1. The comparison between the models prediction capability and the similarity of the model units to real units should not only be presented for the auditory neurons but also for the visual neurons (according to the text the data seem to be already available).

17) Subsection “Optimising predictive capacity” It is not clear whether the similarity measure (only the span of temporal and frequency tuning is considered) is fair or biased for the comparison with the sparse coding model. What will happen, for example, if the distribution of orientation preference would be used instead (for the visual model)? Would then the sparse coding model appear more similar to the real neurons than the prediction model?

Please motivate and discuss.

18) Discussion section: I cannot follow the argumentation that the class of prediction models (or this specific model) should somehow be unique with respect to the ability to provide an independent criterion for the selection of hyperparameters. Should this somehow be a principle, or a logical conclusion? Or an empirical observation only for this special case? Is it logically impossible that we find a measure, for example something entropy-related or whatever, for sparse coding that could have the same status? Please clarify.

19) Subsection “Visual normative models”:does not refer to prediction of the future: Why not? Is not the temporal prediction made in these models that the future spatial pattern is the same as the previous spatial pattern?

20) Subsection “Visual normative models”:The model is selective, throws away information, as opposed to the information preserving properties of other models. But is this really a good strategy for *early* stages of a multi-stage information processing system? Does the principle of least commitment not suggest just the opposite strategy?

21) For the Discussion section it would be of interest to consider the contributions from the two components of the prediction model, i.e., which properties of the units are genuinely caused by prediction and which are more due to the sparse coding part?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Sensory cortex is optimized for prediction of future input" for further consideration at eLife. Your revised article has been favorably evaluated by Sabine Kastner (Senior Editor/Reviewing Editor), and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have addressed my comments in a careful manner. In particular, I appreciate that they made considerable and appropriate changes to text and figures instead of just providing arguments in the response letter. From my view, the manuscript is basically ready for publication. I have a few final minor suggestions.

1).… We examined linear aspects of the tuning of the output units for the visual temporal prediction model using a response-weighted average to white noise input and found punctate un-oriented RFs that decay into the past..…

This is interesting. Can you mention this somewhere in the text?

2) I understand that the model, by its very nature would not care about the sign. But the fact remains that you have an output of a model and you post hoc manipulate this output to obtain a "better suited" presentation (e.g., to ease comparison). My only point is that it should be totally clear to even a superficial reader that such a post hoc change has been applied. So please just include an appropriate sentence that makes this clear, e.g.:

Note that the model does not care about the sign (excitation/inhibition) and thus provides no systematic prediction of it. We hence switched the signs of the respective receptive fields of the model output appropriately to obtain receptive fields which all have positive leading excitation.

(3) Can you mention this alternative goal of least commitment somewhere in the discussion? And the empirical question.

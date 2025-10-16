# Peer review - Round 1

Editors:
- Jonas Obleser, https://ror.org/00t3r8h32 University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80935.sa0](https://doi.org/10.7554/eLife.80935.sa0)

This study models the predictions a listener makes in music in two ways: how different model algorithms compare in their performance at predicting the upcoming notes in a melody, and how well they predict listeners' brain responses to these notes. The study will be important as it implements and compares three contemporary models of music prediction. In a set of convincing analyses, the authors find that musical melodies are best predicted by models taking into account long-term experience of musical melodies, whereas brain responses are best predicted by applying these models to only a few most recent notes.


---

# Peer review - Round 1

Editors:
- Jonas Obleser, https://ror.org/00t3r8h32 University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80935.sa1](https://doi.org/10.7554/eLife.80935.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cortical activity during naturalistic music listening reflects short-range predictions based on long-term experience" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: William Sedley (Reviewer #2); Keith Doelling (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The one non-standard feature of the analysis is the lack of regularization (e.g., ridge). The authors should perform the analysis using regularization (via nested cross-validation) and test if the predictions are improved (if they have already done this, they should report the results).

2) The authors make a distinction between "Gestalt-like principles" and "statistical learning" but they never define was is meant by this distinction. The Temperley model encodes a variety of important statistics of Western music, including statistics such as keys that are unlikely to reflect generic Gestalt principles. The Temperley model builds in some additional structure such as the notion of a key, which the n-gram and transformer models must learn from scratch. In general, the models being compared differ in so many ways that it is hard to conclude much about what is driving the observed differences in prediction accuracy, particularly given the small effect sizes. The context manipulation is more controlled, and the fact that neural prediction accuracy dissociates from the model performance is potentially interesting. However, we were not confident that the authors have a good neural index of surprise for the reasons described above, and this might limit the conclusions that can be drawn from this manipulation in the manuscript as is.

3) The authors may overstate the advancement of the Music Transformer with the present stimuli, as its increase in performance requires a considerably longer context than the other models. Secondly, the Baseline model, to which the other models are compared, does not contain any pitch information on which these models operate on. As such, it's unclear if the advancements of these models come from being based on new information or the operations it performs on this information as claimed.

4) Source analysis: See below in Rev #1 and Rev #3 for concerns over the results and interpretation of the source localisation.

Reviewer #1 (Recommendations for the authors):

The one non-standard feature of the analysis is the lack of regularization (e.g., ridge). The authors should perform the analysis using regularization (via nested cross-validation) and test if the predictions are improved (if they have already done this, they should report the results).

Source localization analysis with MEG or EEG is highly uncertain. The conclusion that the results are coming from "fronto-temporal" areas doesn't strike me as adding much value; I'd be inclined to remove this analysis from the manuscript. Minimally, the authors should note that source localization is highly uncertain.

The authors should report the earphones/tubes used to present sounds.

Reviewer #3 (Recommendations for the authors):

– Figure 2: Music Transformer is presented as the state-of-the-art model throughout the paper, with the main advantage of grasping regularities on longer time scales. Yet the computational results in figure 2 tend to show that it does not bring much in terms of musical predictions compared to IDyOM. MT also needs a way larger context length to reach the same accuracy. It has a lower uncertainty, but this feature did not improve the results of the neural analysis. This point could be discussed to better understand why MT is a better model of human musical expectations and surprise.

– The source analysis is a bit puzzling to me. The results show that every feature (including Note Onset and Note Repetition) are localized in Broca's area, frontally located. Wouldn't the authors expect that a feature as fundamental as Note Onset should be clearly (or at least partially) localized in the primary auditory cortex? Because these results localize frontally, it is hard to fully trust the MT surprise results as well. Can the authors provide some form of sanity check to provide further clarity on these results? Perhaps the source localizing the M100 to show the analysis pipeline is not biased towards frontal areas? Do the authors expect note onsets in continuous music to be represented in higher-order areas than the representation of a single tone? Figure 7 and source-level results: the authors do not discuss the fact that the results are mainly found in a frontal area. It looks like there is no effect in the auditory cortex, which is surprising and should be discussed.

– The dipole fit shows a high correlation with behavior but it is not compared with any alternatives. Can the authors use some model comparison methods (e.g. AIC or BIC) to show that a single dipole per hemisphere is a better fit than two or three?

– Line 252: the order in which the transformation from axial to planar gradients is applied with respect to other processing steps (e.g., z-scoring of the MEG data and TRF fitting) is not clear. Is it the MEG data that was transformed as suggested here, or is the transformation applied to TRFs coefficients (as explained in line 710), with TRFs trained on axial gradiometers? This has downstream consequences that lead to a lack of clarity in the results. For example, the MEG data shows positive values in the repetition kernel which if the transformation was applied before the TRF would imply that repetition increases activity rather than reduces it as would be expected. From this, I infer that it is the TRF kernels that were transformed. I recognize that the authors can infer results regarding directionality in the EEG data but this analysis choice results in an unnecessary loss of information in the MEG analysis. Please clarify the methods and if the gradiometer transformation is performed on the kernels, I would recommend re-running the analysis with gradiometer transformation first.

– The Baseline model claims to include all relevant acoustic information but it does not include the note pitches themselves. As these pitches are provided to the model, it is difficult to tell whether the effects of surprise are related to model output predictions, or how well they represent their input. If the benefits from the models rely truly on their predictive aspect then including pitch information in the baseline model would be an important control. The authors have done their analysis in a way that fits what previous work has done but I think it is a good time to correct this error.

– I wonder if the authors could discuss a bit more about the self-attention component of the Music Transformer model. I'm not familiar with the model's inner workings but I am intrigued by this dichotomy of a larger context to improve musical predictions and a shorter context to improve neural predictions. I wonder if a part of this dissociation has to do with the self-attention feature of Transformers, that a larger context is needed to have a range of motifs to draw from but the size of the motifs that the model attends to should be of a certain size to fit neural predictions.

– Figure 3C: it could be interesting to show the same figure for IDyOM ltm. Given that context length does not impact ltm as much as MT, we could obtain different results. Since IDyOM ltm gets similar results to MT on the MEG data (figure 3A, no significant difference), it is thus hard to tell if the influence of context length comes from brain processing or the way MT works.

– Figure 8: Adding the uncertainty estimates did not improve the model's predictive performance compared to surprise alone, but what about TRFs trained on uncertainty without surprise? Without this result, it is hard to understand why the surprise was chosen over uncertainty.

– The sentence from lines 272 to 274 is not clear. In particular, the late negativity effect seems to be present in EEG data only, and it is thus hard to understand why a negative correlation between surprise estimates of subsequent notes would have such an effect in EEG and not MEG. Moreover, the same late negativity effect can be seen on the TRF of note onset but is not discussed.

– Some of the choices for the Temperley Model seem to unnecessarily oversimplify and restrict its potential performance. In the second principle, the model only assesses the relationships between neighboring notes when the preceding note is the tonal centroid. It would seem more prudent to include all notes to collect further data. In the third principle, the model marginalizes major and minor scales by weighting probabilities of each profile by the frequency of major and minor pieces in the database. Presumably, listeners can identify the minor or major key of the current piece (at least implicitly). Why not select the model for each piece, outright?

– Stimulus: Many small details make it so that the stimuli are not so naturalistic (MIDI velocity set to 100, monophonic, mono channel…). This results in a more controlled experiment, but the claim that it expands melodic expectation findings to naturalistic music listening is a bit bold.

– Line 478: authors refer to "original compositions" which may give the impression that the pieces were written for the experiment. From the rest of the text, I don't believe this to be true.

– Formula line 553: the first probability of Xt (on the left) should also be a conditional probability of Xt given previous values of x. This is the entropy of the probability distribution estimated by the model.

– Line 667: the study by Di Liberto from which the EEG data come uses a ridge regression (ridge regularization). Is there a reason to use a non-regularized regression in this case? This should be discussed in the methods.

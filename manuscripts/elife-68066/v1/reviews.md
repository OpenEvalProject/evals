# Peer review - Round 1

Editors:
- Anne Kösem, Max Planck Institute for Psycholinguistics; Donders Institute for Brain, Cognition and Behaviour, Radboud University; Lyon Neuroscience Research Center Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68066.sa1](https://doi.org/10.7554/eLife.68066.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The manuscript is of broad interest to readers in the field of speech recognition and neural oscillations. The authors provide a computational model which, in addition to feedforward acoustic input, incorporates linguistic predictions as feedback, allowing a fixed oscillator to process non-isochronous speech. The model is tested extensively by applying it to a linguistic corpus, EEG and behavioral data. The article gives new insights to the ongoing debate about the role of neural oscillations and predictability in speech recognition.

Decision letter after peer review:

Thank you for submitting your article "Oscillatory tracking of pseudo-rhythmic speech is constrained by linguistic predictions" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Anne Kösem as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Andrew King as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Johanna Rimmele (Reviewer #2); Keith Doelling (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers had a very positive assessment of the manuscript. They find the described work highly novel and interesting. However, they also find the manuscript quite dense and complex, and suggest some clarifications in the description of the model and in the methods.

Please find a list of the recommendations below.

Reviewer #1 (Recommendations for the authors):

1. First of all, I think that the concept of "internal language model" should be defined and described in more detail in the introduction. What does it mean when it is weak and when it is strong, for the producer and for the receiver?

2. It is still not fully clear to me what kind of information the internal oscillation is entraining to in the model. From Figure 1, it seems that the oscillation is driven by the acoustics only, but the phase of processing of linguistic units depends on their predictability.

3. If acoustic information arrives at the most excitable phase of the neural oscillation (as described in figure 1), and if predictability makes words arrive earlier, does it entail that more predictable words arrive at less excitable phases of the neural oscillation? What would be the computational advantage of this mechanism?

4. What is "stimulus intensity" in figure 5? Does it reflect volume or SNR?

5. Similarly what is "amplitude" in Figure 6?

6. L. 376-L. 439 "N2 activation predicts either da or ga at 0.2 and 0.1 probability respectively." Please explain why the probabilities are not equal in the model, same for l. 445 "intensity of /da/ would be at max 0.3. and of /ga/ 0.7".

7. Table 3: I feel that the first prediction is not actually a prediction, but a result of the article, as the first data shows that "The more predictable a word, the earlier this word is uttered."

8. Table 3 and Figure 8A: I think that the second prediction that "When there is a flat constraint distribution over an utterance (e.g., when probabilities are uniform over the utterance) the acoustics of speech should naturally be more rhythmic (Figure 8A)." could be tested with the current data. In the speech corpus, are sentences with lower linguistic constraints more rhythmic?

9. Table 3: "If speech timing matches the internal language model, brain responses should be more rhythmic even if the acoustics are not (Figure 8A)." What do the authors mean by "more rhythmic"? Does it mean the brain follows more accurately the acoustics? Does it generate stronger internal rhythms that are distinct from the acoustic temporal structure?

10. Figure 5 C: "Strength of 4 Hz power": what is the frequency bandwidth?

11. Figure 5 D: " Slice of D", Slice of C?

12. L 442: "propotions » -> proportions.

13. Abstract: "Our results reveal that speech tracking does not only rely on the input acoustics but instead entails an interaction between oscillations and constraints flowing from internal language model " I think this claim is too strong, considering that the article does not present direct electrophysiological evidence.

Reviewer #2 (Recommendations for the authors):

1. In the model the predictability is computed at the word-level, while the oscillator operates at the syllable level. The authors show different duration effects for syllables within words, likely related to predictability. Is there any consequence of this mismatch of scales?

2. Furthermore, could the authors clarify whether or not and how they think the model mechanism is different from top-down phase reset (e.g. l. 41). It seems that the excitability cycle at the intermediate word-level is shifted from being aligned to the 4 Hz oscillator though the linguistic feedback from layer l+1. Would that indicate a phase resetting at the word-level layer through the feedback?

3. The model shows how linguistic predictability can affect neuronal excitability in an oscillatory model, allowing to improve the processing of non-isochronous speech. I do not fully understand the claim that the linguistic predictability makes the processing (at the word-level) more isochronous, and why such isochronicity is crucial.

4. The authors showed that word frequency affects the duration of a word. Now the RNN model relates the predictability of a word (output) to the duration of the previous word W-1 (l. 187). Didn't one expect from Figure 1B that the duration of the actually predicted word is affected? How are these two effects related?

5. Title: is "constrained" the right word here, rather "modulated"? As we can process non-predictable speech.

6. See l. 129: "In this way, oscillations do not have to shift their phase after every speech unit and can remain at a relatively stable frequency as long as the internal model of the speaker matches the internal model of the perceiver." It seems to me that in the model the authors introduce, the phase-shifting still occurs. Even though the oscillator component is fixed, the activation threshold fluctuations at the word-level are "shifted" due to the feedback. So there is no feedforward phase-reset, however, a phase-reset due to feedback?

7. l. 219: why was bigrams added as control variable?

8. l. 233 in l. 142 it says that only 2848 words were present in CELEX. Where the 4837 sentences consisting of the 2848 words?

9. Figure 2 D,E the labeling with ρ and p is confusing, I'd at least state consistently both, so one sees the difference.

10. Table 1 legend: could you add why the specific transformations were performed?

11. l. 204: the β coefficient is rather small compared to the duration of W-1 effect. The dependent variable onset-to-onset should be strongly correlated with the W-1 duration. I wonder if this is a problem?

12. l. 249: what is meant with "after the first epoch"?

13. l. 254: how local were these lengthening effects? Did the predictability based on the trained RNN strongly vary across words or rather vary on a larger scale i.e. full sentences being less predictable than others?

14. l. 268: Could you explain where the constants are coming from: like the 20 and 100 ms windows for inhibition and the values -0.2 and -3. The function inhibit(ta) is not clear to me. What is the output when Ta is 0 versus 1?

15. Figure 4: the legend is very short, adding some description what the figure illustrates would make it easier to follow. The small differences in early/late activation are hard to see, particularly for the 4th row. Maybe it would help to add lines?

16. Figure 5 B: could you clarify the effect at late stim times relative to isochronous, i.e. why the supra time relative to isochronous decreases for highly predictable stimuli. I assume this is to the inhibition function?

17. How is the connectivity between layers defined? Is it symmetric for feedforward and feedback?

18. l. 294/l. 205: "with a delay of 0.9*ω seconds, which then decays at 0.01 unit per millisecond and influences the l-level at a proportion of 1.5." where are the constants coming from?

19. l. 347: "the processing itself can actually be closer to isochronous than what can be solely extracted from the stimulus". This refers to Figure 5 D I assume. Did you directly compare the acoustics and the model output with respect to isochrony?

20. l. 437-438: I am not fully understanding these choices: why is N1 represented by N2? Why is the probability of da and ga uneaven, and why are there nodes for da and ga (Nda, Nga) plus a node N2 which predicts both with different probability?

21. Figure 5: why is the power of the high-high predictable condition the lowest. Is this an artifact of the oscillator in the model being fixed at 4 Hz or related to the inhibition function? High-high should like low-low result in rather regular, but faster acoustics?

22. l. 600: "The perceived rhythmicity" In my view speech has been suggested to be quasi-rhythmic, as (1) some consistency in syllable duration has been observed within/across languages, and (2) as (quasi-)rhythmicity seemed a requirement to explain how segmentation of speech based on oscillations could work in the absence of simple segmentation cues (i.e. pauses between syllables). While one can ask when something is "rhythmic enough" to be called rhythmic, I don't understand why this is related to "perceived rhythmicity".

23. l. 604: interesting thought!

Reviewer #3 (Recommendations for the authors):

1. An important question is how the authors relate these findings to the Giraud and Poeppel, 2012 proposal which really focuses on the syllable. Would you alter the hypothesis to focus on the word level? Or remain at the syllable level and speed up and low down the oscillator depending on the predictability of each word? It would be interesting to hear the authors thoughts on how to manage the juxtaposition of syllable and word processing in this framework.

2. The authors describe the STiMCON model as having an oscillator with frequency set to the average stimulus rate of the sentence. But how an oscillator can achieve this on its own (without the hand of its overloads) is unclear particularly given a pseudo-rhythmic input. The authors freely accept this limitation. However, it is worth noting that the ability for an oscillator mechanism to do this under pseudorhythmic context is more complicated than it might seem, particularly once we include that the stimulus rate might change from the beginning to the end of a sentence and across an entire discourse.

3. The analysis of the naturalistic dataset shows a nice correlation between the estimated time shifts predicted by the model and the true naturalistic deviations. However, I find it surprising that there is so little deviation across the parameters of the oscillator (Figure 6A). What should we take from the fact that an oscillator aligned in anti-phase from the with the stimulus (which would presumably show the phase code only stimulus offsets), still shows a near equal correlation with true timing deviations. Furthermore, while the R2 shows that the predictions of the model co-vary with the true values, I'm curious to know how accurately they are predicted overall (in terms of mean squared error for example). Does the model account for deviations from rhythmicity of the right magnitude?

4. Lastly, it is unclear to what extent the oscillator is necessary to find this relative time shift. A model comparison between the predictions of the STiMCON and the RNN predictions on their own (à la Figure 3) would help to show how much the addition of the oscillation improves our predictions. Perhaps this is what is meant by the "non-transformed R2" but this is unclear.

5. Figure 7 shows a striking result demonstrating how the model can be used to explain an interesting finding that phase of an oscillation can bias perception towards da or ga. The initial papers consider this result to be explained by delays in onset between visual and auditory stimuli whereas this result explains it in terms of the statistical likelihood each syllable. It is a nice reframing which helps me to better understand the previous result.

6. The authors show that syllable lengths are determined in part by the predictability of the word it is a part of. While the authors have reasonably restricted themselves to a single hierarchical level, the point invites the question as to whether all hierarchical levels are governed by similar processes. Should syllables accelerate from beginning to end of a word? Or in more or less predictable phrases?

7. Figure 5 shows how an oscillator mechanism can force pseudo-rhythmic stimuli into a more rhythmic code. The authors note that this can be done either by slowing responses to early stimuli and quickening responses to later ones, or by dropping (nodes don't reach threshold) stimuli too far outside the range of the oscillation. The first is an interesting mechanism, the second is potentially detrimental to processing (although it could be used as a means for filtering out noise). The authors should make clear how much deviation is required to invoke the dropping out mechanism and how this threshold relates to the naturalistic case. This would give the reader a clearer view of the flexibility of this model.

8. I found Figure 5 very difficult to understand and had to read and read it multiple times to feel like I could get a handle on it. I struggled to get a handle on why supra time was shorter and shorter the later the stimulus was activated. It should reverse at some point as the phase goes back into lower excitability, right? The current wording is very unclear on this point. In addition, the low-high, high-low analysis is unclear because the nature of the stimuli is unclear. I think an added figure panel to show how these stimuli are generated and manipulated would go a long way here.

9. The prediction of behavioral data in Figure 7 is striking but the methods could be improved. Currently, the authors bin the output of the model to be 0, 0.5 or 1 which requires some maneuvering to effectively compare it with the sinewave model. They could instead use a continuous measure (either lag of activation between da and ga, or activation difference) as a feature in a logistic regression to predict the human subject behavior.

10. I'm not sure but I think there is a typo in line 383-384. The parameter for feedback should read Cl+1◊ l * Al+1,T. Note the + sign instead of the -. Or I have misunderstood something important.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Tracking of pseudo-rhythmic speech is modulated by linguistic predictions in an oscillating computational model" for further consideration by eLife. Your revised article has been evaluated by Andrew King (Senior Editor) and a Reviewing Editor.

The manuscript has been greatly improved, and only these issues need to be addressed, as outlined below:

Reviewer #2 (Recommendations for the authors):

I want to thank the authors for the great effort revising the manuscript. The manuscript has much improved. I only have some final small comments.

Detailed comments

l. 273-275: In my opinion: This is because the oscillator is set as a rigid oscillator in the model that is not affected by the word level layer activation; however, as the authors already discuss this topic, this is just a comment.

l. 344: "the processing itself" I'd specify: "the processing at the word layer".

l. 557/558: Rimmele et al., (2018) do discuss that besides the motor system, predictions from higher-level linguistic processing might affect auditory cortex neuronal oscillations through phase resetting. Top-down predictions affecting auditory cortex oscillations is one of the main claims of the paper. Thus, this paper seems not a good example for proposals that exclude when-to-what interactions. In my view the claims are rather consistent with the ones proposed here, although Rimmele et al., do not detail the mechanism and differ from the current proposal in that they suggest phase resetting. Could you clarify?

l 584 ff.: "This idea diverges from the idea that entrainment should per definition occur on the most excitable phase of the oscillation [3,15]." Maybe rephrase: "This idea diverges from the idea that entrainment should align the most excitable phase of the oscillation with the highest energy in the acoustics [3,15]."

l. 431: "The model consists of four nodes (N1, N2, Nda, and Nga) at which N1 activation predicts a second unspecific stimulus (S2) represented by N2 at a predictability of 1. N2 activation predicts either da or ga at 0.2 and 0.1 probability respectively."

This is still hard to understand for me. E.g. What is S2, is this either da or ga, wouldn't their probability have to add up to 1?

Wording

l. 175/176: sth is wrong with the sentence.

l. 544: "higher and syllabic"? (sounds like sth is wrong in the wording)

l. 546: "within more frequency" (more frequent or higher frequency?)

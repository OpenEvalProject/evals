# Peer review - Round 1

Editors:
- Timothy EJ Behrens, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13665.009](https://doi.org/10.7554/eLife.13665.009)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "VTA dopamine neurons compute inferred and cached value (TD) prediction errors in a common framework" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen Timothy Behrens as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Nathaniel Daw (Peer reviewer) and Paul Phillips (Peer reviewer).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Sadacca and colleagues carried out a sensory preconditioning task to test whether dopamine transmission encodes inferred values of sensory stimuli that had not been directly paired to rewards. They report that when a cue is paired with reward, another cue associated with it (through sensory preconditioning) acquires a dopamine response to its presentation even though the latter cue has never been directly paired with reward. This type of association is not available from standard model-free reinforcement learning algorithms. Therefore, the authors conclude that dopamine transmission can compute prediction errors through (model-based) inference.

All three reviewers regarded this as a potentially major and important result that should be celebrated. For example:

This wonderful study recorded the activity of midbrain dopamine neurons during sensory preconditioning. This is an absolutely critical, long-overdue test of a fundamental question about dopaminergic 'prediction error' signals: exactly what 'prediction' do they use to compute their 'error'? I've been pestering rodent researchers to do this experiment for years (this type of experiment requires naïve subjects and hence is much more easily done in rodents than in monkeys).

This article demonstrates that (putative) dopamine neurons in rat VTA compute reward prediction errors with respect to reward predictions derived by combining information from separate sensory preconditioning and reward conditioning phases in a manner that the simplest TD learning algorithms cannot. This is an important and extremely clean result.

This work is potentially very important and the manuscript is clearly written.

Essential revisions:

However, all three reviewers highlighted several major concerns that need to be dealt with. The essential concerns are in fact very similar between the three reviewers. I have left the native reviews below because each reviewer raises very similar points, but there is nuance in the different expressions of the concerns that, I think, will be useful in preparing the revision.

The essential concerns can be divided, I think, into three categories. Clarification of procedures and results, appropriate reflection of the existing literature, and some extra information (or discussion) about some slightly concerning features of the data – in particular the response to stimulus D.

In the discussion between reviewers, it was clear that the first two of these categories were essential. With respect to last category, there were some discussions about potential causes that might both mitigate some of the concerns below, and suggest some alternative tests. For example,

"My hunch is that D gained a positive response due to the sort of 'generalization'/'alerting'/'pseudo-conditioning' phenomenon that's often seen where if two stimuli of the same modality are presented in the same task environment, they both gain some positive short-latency DA response even if only one is paired with rewards (e.g. old Schultz studies, recent study by Kobayashi and Schultz, voltammetry study by Day et al. 2007, etc.). This effect may be weaker in A and C because during their phase of training session no rewards were delivered."

"A key question here is whether there is bias in the probe phase due to selecting cells based on their response to B and testing them on the same data. I think we all agree that this doesn't bias the key result (the comparison between A and C in Figure 3E) but I think it might indeed bias Figure 3F (which is based in part on the responses to B and D) and more obviously the extended versions of Figure 3F that I think at least two of us asked for (i.e. comparing a scatterplot of that sort between neuronal subtypes). Could they do analyses based on holdouts to avoid directly using the same trials to select and test?"

Reviewer #1:This wonderful study recorded the activity of midbrain dopamine neurons during sensory preconditioning. This is an absolutely critical, long-overdue test of a fundamental question about dopaminergic 'prediction error' signals: exactly what 'prediction' do they use to compute their 'error'? I've been pestering rodent researchers to do this experiment for years (this type of experiment requires naïve subjects and hence is much more easily done in rodents than in monkeys). When I saw this data presented at a recent SfN I was very pleased and eager to see it get in print, so I'm happy to see it here at last!

I like the very clean experimental design that allows measurement and direct comparison between conventional signals consistent with TD learning models as the new unconventional signals. I also like that the authors cite previous work very well, even citing a related voltammetry study from the Phillips group that has only appeared in abstract form. I also appreciate that the paper is a short, sweet, and to the point test of its main hypothesis.

In fact, the paper may have gone slightly too far in this direction. My major comments are about the more sophisticated interpretations and subtler findings that the authors seem to have left out of their short and sweet narrative.

1) "After conditioning, the rats underwent a single probe test, which consisted of three reminder trials of B paired with reward and three trials of D unpaired, followed by presentation of cues A and C, alone, six times each, without reward." This needs to be clarified. Were the B and D reminder trials done in a fixed sequence (e.g. B, B, B, D, D, D), were they randomly interleaved, or something else? The same needs to be clarified for the A and C probe presentations.

This small detail is critical to the logic of the paper. The cues should ideally have been presented in randomized orders. If subjects were always probed with A before C then conceivably the greater behavioral response to A than C could have been due to an effect of time rather than due to a discrimination between the meanings of the cues. For instance, suppose something about the reminder treatment (e.g. the presentations of B/D or the deliveries of rewards) put the animals in a state of generalized enhanced responsiveness to the A/C cues, a state which slowly waned with time or habituated with repeated presentation of A/C cues. If A was always presented before C, then A would have produced greater behavioral responses than C, even if animals failed to assign higher inferred value to A or even if they failed to discriminate at all between A and C.

2) Figure 3 has straightforward logic, but two key points need to be clarified:

2.1) "Notably this was also true for a handful of neurons that exhibited the classic wide, polyphasic waveforms traditionally used to identify dopamine neurons (Figure 3F, filled circles)." It's very hard to make out the data points for the three types of neurons. How many neurons is in the handful (n)? Was the effect significant? The authors present clear statistics for the Type 2 cells but need to present the same statistics for the classically defined DA neurons.

2.2) What responses did cues A and C evoke in the type 1 and 3 neurons, and do they have any significant A-C effect? This is of great interest because these neurons were recently prominently proposed to have a major role in computing DA prediction error signals (Eshel et al., Nature 2015), so one would expect that the important new computations these authors have discovered in DA neurons should be presaged by similar computations in type 1 and 3 neurons.

Currently the authors address a partly related but less critical point. They say these neurons don't have a significant correlation between onset firing for B-D and A-C (without presenting statistics to justify this statement), though that's perhaps to be expected given that their responses are tonic rather than phasic.

The above points 2.1 and 2.2 could be cleared up by showing the same main results that are shown for the type 2 cells (activity plots in Figure 3E and the statistical tests of population responses to B-D and A-C), also for the classical electrophysiologically defined putative DA neurons, and also for the type 1 and type 3 cells. This will also help validate their classification by confirming that the putative DA, type 1 cells, and type 3 cells behaved consistently with prior optogenetically-verified studies.

3) The authors chose the word "inference" as the key word for the novel part of their study, drawing a distinction between "inferred value" and "cached value".

Why not use "model-based"? This is the term that was prominently defined and contrasted with the "cached value" that motivates this study, in a seminal paper on this topic (Daw et al., Nature Neuroscience 2005). It's surprising that the authors don't cite this paper, since it seems to be the origin for the "cached values" terminology the authors use throughout their study and in their title. I find it strange that the authors don't discuss or even mention the concept of model-based vs model-free learning. In that terminology, this study is very important: it is the first, long-awaited test of popular hypotheses about whether DA neurons use model-based or cached values!

"Inference" is a very broadly-defined word that has different meanings in different contexts. If the authors want to use it I would appreciate it if they defined which specific form of inference they're studying, rather than treating "inference" as universally synonymous with model-based learning. Notably this paper places "inference" in contrast with TD learning, but in that field of machine learning "inference" has a more general meaning. There are forms of TD learning that learn without model-based reasoning but which still clearly use forms of inference (e.g. Bayesian Q-learning, which uses Bayesian inference (Dearden, Friedman, and Russell, AAAI 1998)).

Furthermore, "inference" has been used in previous work on dopamine neurons and TD errors, but the present work uses it in a different manner without clearly explaining the difference in definitions. The cited paper by Bromberg-Martin et al. (2010) defined "inferred stimulus value" as updating the value of a stimulus without experiencing that stimulus. This paper, however, uses "inferred value" in a different way apparently synonymous with model-based value. This un-discussed difference in terminology makes it sound like the authors are (perhaps unintentionally) dismissing the previous work as invalid. The authors seem to state that study was merely "suggestive" of inferred prediction errors because it was subject to "confounding" issues, but it would be more accurate to say that both studies had valid results and were simply studying different forms of inference, or were defining "inference" in different ways.

Reviewer #2:

This article demonstrates that (putative) dopamine neurons in rat VTA compute reward prediction errors with respect to reward predictions derived by combining information from separate sensory preconditioning and reward conditioning phases in a manner that the simplest TD learning algorithms cannot. This is an important and extremely clean result, but of interest in great part because it plays into a large literature on this topic in computational modeling and human neuroimaging which is entirely and surprisingly neglected here but provides context and subtlety to the interpretation.

1) My main concern is sort of semantic, but both the Abstract and the final sentence of the article claim that these signals are not TD errors. In my view, a "TD error" is a Bellman residual, the temporal difference between the reward predicted at times t vs t+1, which is precisely consistent with these responses. The issue is where the predictions themselves come from, i.e. whether they can have themselves been learned by caching simple adjustments driven by previous TD errors, vs. some more complicated inference (a computational distinction due to Daw et al., 2005). TD *errors*, in short, need not only arise (only) from TD *learning*, even though the former drive the latter. This was perhaps first pointed out in the context of a human imaging study (Daw et al. 2011) which somewhat presaged these results and their interpretation.

2) A related interpretational subtlety is how the learning and integrative inference that underlies these predictions might have taken place. Again, relevant human imaging work (Wimmer et al., 2012; Kurth-Nelson et al. 2015; Shohamy & Daw 2015) is not discussed; these results suggest that associative retrieval (from B to A) occurs during the conditioning phase, together with which standard TD updating (from the reward to the reactivated A) would suffice. (An alternative – suggested in more human work by Gershman et al., 2012, and computationally by Sutton's, 1991, DYNA – is that replay between the conditioning and transfer phases, driving regular TD updating, would integrate the information.) The former possibility directly instantiates the suggestion, dismissed briefly in the discussion of Bromberg-Martin's (2010) similar result, that this result might be due to simple TD plus some altered state representation (here that state B and A are combined; in general – Dayan 1991 – that states are represented by their successors). I agree that this study is a cleaner and more stripped down test of integrative prediction than Bromberg-Martin's serial reversal, but it is just wrong to distinguish them in the way described here.

Reviewer #3:

Sadacca and colleagues carried out a sensory preconditioning task to test whether dopamine transmission encodes inferred values of sensory stimuli that had not been directly paired to rewards. They report that when a cue is paired with reward, another cue associated with it (through sensory preconditioning) acquires a dopamine response to its presentation even though the latter cue has never been directly paired with reward. This type of association is not available from standard model-free reinforcement learning algorithms. Therefore, the authors conclude that dopamine transmission can compute prediction errors through (model-based) inference.

This work is potentially very important and the manuscript is clearly written. However, one aspect of the control seems to be problematic, making the conclusions of the work somewhat equivocal in my opinion.

Major concern:

The response of putative dopamine neurons to control stimulus D, which was never paired with reward, is quite large. This response was significantly smaller than that for stimulus B in the analysis epoch (first second of cue presentation). However, it is possible that this difference could relate to features other than the reward contingency. Selection criteria for putative dopamine neurons include the responsiveness to a reward-associated cue, specifically stimulus B and so, by design, there is a systematic selection bias towards neurons that respond to stimulus B. Therefore, it is feasible that the increased firing to stimulus B over stimulus D is due to the sensory properties of stimulus B since regardless of which auditory stimulus was designated as stimulus B in a particular subject, neurons were selected that responded to that stimulus. The authors need to address this potential confound, especially given that the mode response of the putative dopamine neurons did not discriminate between stimuli B and D (Figure 3F).

Stimulus A and C also produced significant increases in the firing of putative dopamine neurons. The key comparison of the study was between these two responses, which was indeed, significantly greater for stimulus A. However, it is disconcerting how these responses spanned the response to stimulus D since the B to D and A to C comparisons appear (although it's not completely clear from the manuscript) to have been carried out independently without consideration of the variance of the responses to all of the stimuli. The concern is that if all the stimuli that were not directly paired with reward (A, C and D) were compared, significance would be lost. The authors should test whether the differences between responses to A and C are still significant if the analysis includes the responses to all of the stimuli (two-way ANOVA or comprehensive one-way ANOVA). At very least the authors should discuss if and why the responses to stimuli C and D are not more similar (e.g., more generalization to reward).

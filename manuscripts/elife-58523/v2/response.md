# Author response - Round 1

Authors:
- Teresa M Findley ([ORCID: 0000-0002-2050-4869](https://orcid.org/0000-0002-2050-4869))
- David G Wyrick ([ORCID: 0000-0001-8096-5766](https://orcid.org/0000-0001-8096-5766))
- Jennifer L Cramer
- Morgan A Brown
- Blake Holcomb
- Robin Attey ([ORCID: 0000-0002-9652-8103](https://orcid.org/0000-0002-9652-8103))
- Dorian Yeh
- Eric Monasevitch
- Nelly Nouboussi
- Isabelle Cullen
- Jeremea O Songco
- Jared F King
- Yashar Ahmadian ([ORCID: 0000-0002-5942-0697](https://orcid.org/0000-0002-5942-0697))
- Matthew C Smear ([ORCID: 0000-0003-4689-388X](https://orcid.org/0000-0003-4689-388X))

## Response text

DOI: [10.7554/eLife.58523.sa2](https://doi.org/10.7554/eLife.58523.sa2)

Summary

This paper is a clear account of an odor-guided behavior in which the authors use machine-learning movement analysis to characterize the behavior in detail. The key findings are sniff-synchronized movement (already known), the ability to classify a number of movement motifs (but not strikingly distinct) and the further analysis of relationships between these movements and sniffing. All reviewers felt that this detailed analysis of behavior in a non-invasive manner was exciting and has much promise for the field.

We are gratified by the overall positivity of the review and we are most grateful to the reviewers for thoughtful and thought-provoking comments. We recognize and appreciate the effort and time these reviews must have taken. Most importantly, we feel that we have substantially improved our manuscript by responding to these reviews.

We have organized our response into sections that address the major issues raised in Dr. Bhalla’s summary. To do so, we have organized the comments from individual reviewers into these sections. All comments about other issues are addressed after that.

Essential revisions

Decision points and sensory strategy. Where and when are the mice making decisions, and are these decisions based on absolute concentration or the gradient?

We thank the reviewers for encouraging us to delve deeper into the sensory strategy the mice are using to solve this task. In our revision, we now present data that support our contention that the mice are guided by serial sniffs across odor gradients. To further test this model, we visualized the allocentric structure of investigation and approach, as suggested by reviewer 3.

The occupancy diagram of Figure 3F is fascinating. Together with panel 3D, it suggests that mice undergo fairly stereotyped searches: after poking their nose out of the initiation port, they appear to make a 180 degree rotation (sweep) to face the gradient. The density reaches a maximum at that point (opposite to the position of the initiation port). Is this position (crossing of the alpha shape) dominated by an "investigation" state? Can this position be viewed as a decision point? When/where does the animal tend switch to the "approach" state? More generally, could you map dominate trends in behavioral motifs of Figure 6B onto the stereotyped alpha shape of the occupancy diagram of Figure 3F?

We thank reviewer 3 for these ideas. In a new section of the results with 4 new figures (2 main and 2 supplementary), we now show occupancy maps of investigation and approach states. By overlaying the occupancy histograms from the two states, we show that most of the overlap is restricted to the center of the region between initiation port and decision line. This is at the crossing of the alpha shape of occupancy maps (Figure 9A) where overall occupancy also peaks (Figure 3F). To better quantify this overlap, we show an index of the relative values of investigation and approach occupancy as a function of distance from the initiation port. These data show that the index switches from predominantly investigation to predominantly approach within the alpha shape crossing region, between 5 and 10 cm from initiation. Based on this observation, we now refer to this region (between 5 and 10 cm), as a "transition zone" for the purposes of further analysis. We do not view this region as a "decision point", because we think that term only applies to an instantaneous event, not an across-trial pattern. Investigation-approach transitions are our best guess at the decision points in each individual trial. What we are calling the "transition zone" is the region where most of these transitions occur.

We next use these occupancy maps to evaluate alternative models of the sensory strategy – do the mice use absolute concentration or gradients? As argued by Dr. Bhalla:

The animals could be memorizing absolute concentrations… just memorizing 'expected' gradients or absolute concentrations (100, 80, 60 etc) – which is actually quite easy for mice to learn! In that case, indeed the mouse actually already knows which side the reward will be. If during the alpha turn it smells concentrations 100 or 80 or 60, it sticks to that side, otherwise walk to the other side. Indeed in this scenario – there is no need for lateral comparisons – and the knowledge gathered during the alpha turn already tells the animals which side it should go towards.

We agree that this possibility is logically consistent with the evidence provided in the original submission. We thank Dr. Bhalla for articulating such a clear prediction of the absolute concentration model. Indeed, an absolute concentration-sensing mouse would not need lateral comparisons. If they first turn toward higher concentration, they should stick to that side, and proceed straight to the water port, rather than waste time and sniffs at the midline. They would only need to cross the midline if they sense low concentration while turning out of the initiation port. To depict this intuitive prediction, we have now added auROC maps based on our PID recordings as panel C and D in Figure 1—figure supplement 2. This map (Figure 1—figure supplement 2C) shows absolute concentration differences between left and right trials can best be discriminated if the animal samples directly downwind of the odor ports, along the axes of maximal odor concentration.

On the other hand, if the mouse is using a gradient sensing strategy, it would seem that the best strategy is to sample both sides. As stated by Dr. Bhalla:

I don't think that a sequence of samples on the left and the right side must be taken for the mouse to infer the direction of the gradient… In the videos, I didn't see systematic left-right samples.

We agree that sampling both sides is not necessary for performing the task. However, because the airflow in the arena is turbulent, odor released on one side spreads some distance into the other. Nevertheless, while sampling both sides is not a must, we agree that the gradient sensing model predicts that the animal would achieve the highest performance by sampling across the midline. To depict this intuition, in (Figure 1—figure supplement 2D) we show an auROC map based on gradients derived from the same PID recordings. This map shows that for gradient-sensing, the most informative place to sample is indeed across the midline.

In Figure 10, we use investigation and approach occupancy maps to test these predictions. We show that correct trials are associated with more investigation at and around the midline, particularly on the unchosen side of the arena. By definition, sampling the unchosen side precedes crossing the midline to the chosen side, showing that correct trials feature more sampling on both sides. Incorrect trials have more investigation downwind of the odor ports, particularly near the decision line, where Figure 1—figure supplement 2D shows is the most informative location for absolute concentration discrimination. Thus, these data are inconsistent with the absolute concentration model, and consistent with the gradient model.

One concern with our task is that it forces mice to turn in one direction or the other out of the initiation port. Sometimes the mouse stays on the side it started towards, sometimes it switches to the other side. Could this asymmetry explain why correct trials seem to feature more investigation at the midline? In Figure 10—figure supplement 1, we analyzed stay and switch trials separately. The performance correlations shown in Figure 10 are essentially the same. In both conditions, correct trials are associated with more investigating at the midline and on the unchosen side. Although there are intriguing differences between the patterns, we feel that these are beyond the scope of the present manuscript.

Our analysis of the allocentric structure of state usage supports a serial-sniff gradient sensing model and is inconsistent with an absolute concentration sensing model. On that same topic:

The authors actually do try to rule out the possibility that animals learn absolute concentrations by doing what they refer to as variable |C| sessions… But the data presented is not really conclusive – performance in the first 10 trials is quite low – so its very likely that the animals just learn a new rule.”

We respectfully disagree. Figure 2—figure supplement 2 shows the across-mouse average performance over trials. In the first 10 trials of the first session in which the mice have encountered the 90:30/30:10 version of the task, the mice perform at 75% correct. Therefore, on average, the mice make only 2 or 3 errors in these trials. Even for an ideal observer mouse, we think it would take at least two errors to ascertain that they should learn a new rule. Slotnick and Katz (1974) showed that rats can show learning-set performance for new odor-pair discriminations in a nearly-errorless way, but only after they have already experienced 16 previous odor-pair switches, and thousands of trials. So, while it may be mathematically possible for a mouse to immediately change sensory strategies from C to delta-C, the possibility does not seem very likely given our data.

State transitions and error correction

The authors might want to push the analysis of the search strategy one step further by defining whether/how mice can switch from investigation to approach, back to investigation to perform error correction. This process would rule out that animals find the gradient through an initial guess that leads to a full commitment to one side during the approach phase. The data suggests that error correction takes place (Figure 7C and D), but those cases are not analyzed in detail. Can a statistical analysis of the state transitions reveal any principles in the organization of error correction? Does the animal's state indeed switch from approach to investigation during error correction?

Our new analysis shows that transitions from investigation to approach in the region just before the decision line are more common on error trials (Figure 10C and supplement 1). This pattern shows that the investigation state is not inherently beneficial to performance. Instead, it matters where the mouse investigates, which gives us indication of where informative stimulus features are in the arena. The auROC map (Figure 1—figure supplement 2) shows that absolute concentration features are most informative in this position near the decision line, where investigation is associated with incorrect trials. Thus we interpret this result as further evidence against the absolute concentration model.

What are individual animal differences and how do you explain the lack of stereotypy in movement?

We have shown that a classifier can uniquely identify individual animals based on our ARHMM. Is this because the motifs themselves differ across mice, or does it reflect diversity in how different mice sequence and deploy the motifs? To test the former possibility, in Figure 6—figure supplement 5 we present average shapes of each motif (as in Figure 6B) for each individual mouse. The shapes match across mice, suggesting that the algorithm is identifying consistent behavioral features. Instead, the differences have more to do with where and when the mice deploy different motifs. To accompany Figures 9 and 10, we provide investigation and approach occupancy maps for individual mice in Figure 9—figure supplement 1, showing that mice are diverse in where they transition from investigation and approach. For example, some mice are biased to one side, other mice to the other. We think these are the idiosyncrasies that the classifier is picking up on. Interestingly, we show in Figure 9—figure supplement 1 that if trials are re-oriented with respect to the chosen side (i.e., right-choice trials are flipped so that the trajectory always ends on the upward side of the diagram), all the mice tend to transition from investigation to approach on the chosen side. In this sense, the mice are quite consistent.

We think it is most likely that the lack of stereotypy in individual trial trajectories is attributable to the variable and turbulent nature of our odor stimuli.

Additional comments

1. Poor performance and lack of adaptive strategy:

We too were surprised that the mice did not perform better in the 100:0 condition. Additionally, Reviewer #2 points out mice do not adapt their strategy as the task is made presumably more difficult (i.e. from 80:20 to 60:40). We can only speculate as to why.

First, we don’t know that this is necessarily an easy task for rodents. In previous studies by the Bhalla and Murthy groups, the rodents were able to improve performance by using a memory-guided strategy, and to some degree avoid the problem of tracking the odor source from a distance. Maybe the animals in these studies used memory-guided strategies because odor-guided navigation is harder for them than our intuition and our PID maps would suggest. We know frustratingly little about the statistics of natural olfactory scenes, so perhaps the mice are evolutionarily optimized to operate in different stimulus conditions than we have contrived for this paradigm.

Alternatively, another likely explanation which we have added to the manuscript (lines 460-464) is that mice are strong delay-discounters – they are in a hurry to collect as much reward as possible in as little time as possible. Perhaps if we could more exhaustively search the task parameter space (e.g., ITI durations, reward sizes), we could find a way to slow them down and improve performance, but this has exceeded our experimental bandwidth so far.

2. Nose speed during ITI versus trial:

Reviewer #2 raised the concern that our analysis of sniff-locked movement with regards to nose speed is biased, because of differing nose speeds during the inter-trial interval and the trial. In Figure 5—figure supplement 2, we now separately analyze ITI sniffs in which the mice were moving at or above the average nose speed during the trials. Even in these sniffs, we see very little modulation of nose speed, and none for yaw or z-velocity, consistent with our assertion that sniff-synchronized movement is a pro-active search strategy, and not a default accompaniment of fast locomotion.

3. Asymmetrical odor distribution:

Reviewers and Dr. Bhalla pointed out that there is asymmetry in the right versus left odor delivery, particularly apparent in our 60:40 PID maps. This asymmetry is due to a difference in airflow distribution across the arena. If this asymmetry were relevant to performance, we would see systematic patterns in the position biases across mice. However, our data show no such patterns in the left-right distribution of occupancy as far as we can tell (see Figures 3-supplement 1, 9-supplement 1).

4. Sniff-synchronization novelty:

We have been asked to provide a statement on how our sniff-synchronization finding expands upon what is already known, particularly from the work of Kleinfeld’s group. Most importantly, our task design, which includes trial and ITI periods, allows us to show that kinematic rhythms do not always lock to the sniff cycle. Instead, we show that sniff-synchronized movement is specific to periods when the mouse is searching. From this we can infer that sniff synchronization is a pro-active sampling behavior rather than an odor-gated orientation reflex or a default accompaniment to fast sniffing. This could only be speculated upon in the previous work.

5. Ethological gap between task design and natural conditions:

Reviewer #2 points out that our binary choice-based task design may not require the fine spatial resolution likely needed for olfactory search in natural conditions where the number of possible target locations is quite a bit larger than 2. We agree and acknowledge this limitation of our study. We also have no doubt that there are many features of olfactory search that we cannot capture with a paradigm like this. Despite these limitations, we feel confident that the primary findings of the study – gradient guidance, sniff synchronization, and two-state organization of search behavior – will hold true under more naturalistic conditions of airborne scent tracking. We hope we and others can improve upon this experimental design to better recapitulate the relevant olfactory features and motor affordances of the real world.

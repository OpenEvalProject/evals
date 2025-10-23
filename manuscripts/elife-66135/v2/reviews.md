# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66135.sa1](https://doi.org/10.7554/eLife.66135.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper will be of interest to a wide range of systems neuroscientists seeking to understanding the relationship between neuronal activity and behavior. Building on previous technical advances in brain-wide imaging of neuronal activity (Ca signals) in freely moving animals (Caenorhabditis elegans), it demonstrates that a linear regression model is sufficient reconstruct key parameters of locomotion – velocity and body curvature – from the imaging data and documents differences in activity between freely moving and immobilized worms.

Decision letter after peer review:

Thank you for submitting your article "Decoding locomotion from population neural activity in moving C. elegans" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) Please address concerns by Reviewers #1 and #2 about identifying eigenworms with velocity and curvature (detailed in Recommendations for the authors).

2) Please address the questions with respect to tuning and noise that are raised by Reviewer #2 (detailed in Recommendations for the authors).

3) Both Reviewer #1 and #3 (detailed in Recommendations for the authors) require that you address your conclusion that the population decoder outperforms the best single neuron. Is this a meaningful comparison, and how should such coding be interpreted?

4) The concerns of Reviewers #2 and #3 about the significance of the distribution of weights assigned by the decoder for how behavior is represented in the brain should be addressed (detailed in Recommendations for the authors).

5) All Reviewers (detailed in Recommendations for the authors) have strong suggestions for reorganizing the text and amplifying and deepening Introduction and Discussion. Reviewer #3's concerns about the functional implications of the decoding should be addressed. Limitations of the analysis should be clearly addressed in Discussion.

Reviewer #1 (Recommendations for the authors):

I hope that the authors focus on improving results and discussions sections of their strength (see above), including additional analyses, precise terminology, simplified statements, clarified discussions, and perhaps structural reorganization. I have a few concerns that I ask them to address or respond to, so that this work can be appreciated by and benefit the field. They are raised below, and should be viewed as suggestions for this purpose.

(1) Line 71-85: This first Results section (which lacks a title) is a brief definition of the locomotion features for velocity and curvature as used throughout the paper.

I am uncomfortable with the brevity of the introduction and justification of using eigenworms to represent velocity and curvature. These are two widely used biological terms, and the introduction would confuse many readers and even misled them (in the case of 'curvature').

I share the authors' opinion on the deficiency of defining velocity by the animal's centroid displacement. However, they should be equally clear that their presentation for 'velocity' did not directly address this deficit: their analysis did not calculate and present the wave velocity – the speed of bending wave propagation – which would have the units of mm/sec or body lengths/sec as opposed to radians/sec.

Moreover, in Figure 1-Figure S1, the authors demonstrated that their eigenvalue-derived velocity was well correlated with that of centroid-derived velocity values. This, to me, was a good validation to justify their choice of parameters as a proxy for velocity in later analyses. However, the authors did not cite this validation figure as its purpose, but instead in the context of a statement for the weakness of the centroid-based velocity measure. This is a misleading manipulation of citation of the authors' results.

I have a bigger concern for referencing the third eigenworm as the 'curvature', specifically Lines 82-84 ("Here we report body curvature as a dimensionless quantity that captures bending in the dorsoventral plane, calculated by projecting the animal's body posture onto the third principal component of the eigenvalue decomposition."). To my understanding, this component best represents the body postures during turning. Their relationship with 'curvature' – which most would interpret not as a dimensionless quantity but as a precise measure of the degree of body bending per unit length – should be demonstrated similar to how the authors did so for velocity in Figure 1, Supplementary Figure 1. I personally consider it inappropriate to use 'curvature' when referring to the projections of the third eigenworm.

2) I found their motion correction important, interesting, and potentially useful to the community. The authors should definitely highlight it and elaborate in the text as a separate section instead of putting it away in Methods and at the end of the following Results section (Line 125: Population decoder outperforms best single neuron – this long result section can definitely benefit from 'de-mixing'.)

To me, it would be very helpful to show the example data for the authors' methods for motion correction, including the raw traces of GCaMP and RFP before and after they performed correction by their ICA analyses (e.g. I think that it did not work as well for AVAL in Figure 2b; knowing what the trace was like before the correction would help me to examine why). I also would be curious to know why these authors limited their ICA to give two components instead of collecting all components and subtracting the ones correlated with RFP. It would be good if authors treated the number of ICA components as a parameter and explored the choice of this parameter on the performance of motion correction. A discussion on systematic ways to estimate this parameter would also be very welcome.

3) Section 'Population decoder outperforms best single neuron' and Figure 3a.

Here I have trouble appreciating the significance of this comparison. Previous studies have shown that forward, backward, and turning are three separate motor motifs of C. elegans locomotion. It is possible that multiple neurons may participate in multiple motor behaviors, but it would be truly astonishing (to me at least) if a single neuron plays a dominating role of all motifs of locomotion. Given the state of the field, scientifically it would be much more meaningful to compare the performance of a population decoder to the combination of the four best single neurons e.g. the best for positive velocity, the best for negative velocity, the best for dorsal turning, and the best for ventral turning, instead of one single best neuron.

The authors could also make it clear to readers that due to the lack of knowledge of neuronal identity, as well as the fact that each recording was capturing ~2/3 of the total neuronal population, the best single neuron decoder in each recording was only 'relative' to the captured neuronal population, and likely differed per recording.

4) The organization of multiple Results sections appear lengthy and redundant. They should be combined, compressed, and reorganized. For example, the last section on correlations with AVA seems to contain the same information as "immobilization alters the correlation structure of neural activity". The sections / subsections "Population code for locomotion" (line 193) and "Largely distinct sub-populations contain information for velocity and curvature" (line 256) can be better organized.

I also view AVAL and AVAR coupling more as a benchmarking tool to give the readers confidence that their method works in the non-immobilized setting instead of an interesting new finding as it seems to be portraited in the abstract. Combining these results with an expanded sections to describe their imaging processing pipeline may be a better organization solution.

5) I personally found that among all results from the model, the notion that the simplest linear model works the best is the most interesting. It would be interesting to hear the authors' thoughts on its implication of the C. elegans brain network on motor states and their transitions.

Reviewer #2 (Recommendations for the authors):

My enthusiasm is diminished by a series of major concerns that I believe should be possible to address:

1) An important and interesting claim in the paper is that different neurons have different "tunings" for behavior – for example, some neurons are associated with forward velocity fluctuations, while others are associated with forward/reverse transitions. However, this is not very well explored in the paper. Some example data are shown, but that's about it. I'd suggest characterizing the full range of possible tunings that neurons can display and showing how many neurons in each of their datasets display such tunings. This could be a major strength of the paper if it is clearly characterized and communicated.

2) If the tunings are indeed diverse/complex (i.e. not just linear relationships), I'd suggest trying to predict behavior from single neurons using non-linear decoders. What is the best performance that can be obtained from single neurons using these more complex decoders? (and how does it compare to population-level decoders).

3) While it is readily apparent that the regression models perform better when trained from the full set of neurons (compared to the "best single neurons"), the authors' interpretation that this is because different neurons have different tunings does not yet seem fully supported. My main concern is that there is substantial levels of noise in their GCaMP measurements and that training models from more neurons may simply overcome this noise (the authors actually show that SNR impacts their predictive power in Figure 3-S1). For example, suppose that there were 2 neurons with perfectly correlated ground-truth activity and that they were both perfectly correlated with a behavior. If the activity measurements from these neurons had uncorrelated noise (noise in one neuron was not correlated with noise in the second), then a classifier trained to predict behavior would perform better if both neurons were used. In this case, this would not be due to any difference in the underlying tunings of the neurons. Are such effects occurring here? It is possible that one way to estimate the impact of these types of effects would be to compare models trained on similar amounts of data (e.g. 10min of data from one neuron vs. 5min of data from two simultaneously correlated neurons) or something like that. Another possibility would be to record single neurons (not in a whole brain context) in order to obtain higher SNR recordings and compare classifiers trained on these single neurons to those trained on the full population. (This would require knowing some of the "best single neurons")

4) Related to the above point, models with more parameters almost always perform better. To determine whether the increased model performance justified the use of additional parameters, I'd suggest using AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion) formulations.

5) The Introduction does not properly introduce what is known about the neural circuitry that gives rise to locomotion in C. elegans. The roles of many neurons have been carefully characterized – it would be useful to introduce what is known about their "tunings" from previous work and whether the field already thinks that a population code for locomotion may exist (or not).

6) In Figure 1 -S1 the authors compare velocity in their datasets, as measured by eigenworm analysis vs. center of mass movement. While they are correlated, I was surprised by how frequently they disagree. Why do they disagree at times? Are there errors in one or both of these methods?

7) In Figure 5, I believe it would be important to only present exemplary data from timepoints in the testing datasets, not the training datasets (i.e. only present correlation coefficients for datapoints in testing data; and only show examples of neural activity and behavior from testing data). For example, it is hard to know whether the relationships in Figure 5C are meaningful or just represent overfitting of the model if they are from the training data. (If these are test data already, please just make this clear in figure legend)

8) It is not clear that analyzing the weights in Figure 5A is really all that informative with regards to the underlying roles of the neurons. The fact that the model can predict behavior in withheld data is highly informative, but the specific weights recovered are influenced by the regularization method used, whether a neuron's activity contains information redundant with some other neuron's activity, etc.

9) There are no across-animal summary data of the effects that the authors show in Figure 5. This is just exemplary data. Are these observations consistent across animals?

Reviewer #3 (Recommendations for the authors):

1) Abstract would benefit from a statement of the main conclusion and its significance.

2) It would be helpful to motivate the immobilization experiment by first describing the state of knowledge concerning neuronal dynamics in worms (rather than waiting until the discussion).

3) What is the meaning of the shading in Figure 1d,e and similar places in the paper?

4) For readers unfamiliar with the C. elegans nervous system, it would be useful to make clear what fraction of all head neurons is being recorded, and also what fraction of all neurons is being recorded.

5) It might be more appropriate to move the section on correcting for motion artifacts (pg. 7 [171-182ff]) earlier in the paper, where this correction is first used. Or, move it to Methods.

6) Subscript (i) in Equation 1 is misplaced on pg. 7.

7) For those unfamiliar with the Fano factor, it might be worth pointing out that in Equation 1, the variance (numerator) refers to the signal, not the noise.

8) pg. 15 [379…]. "Our measurements suggest that neural dynamics from immobilized animals may not entirely reﬂect the neural dynamics of locomotion." Consider rephrasing. This sentence is almost a tautology as it says "…neural dynamics in the absence of locomotion may not entirely reflect the dynamics in the presence of locomotion."

9) Line 104-5: please add Faumont et al., 2011.

10) Line 198: Do you mean "Figure 5a,b"?

11) Line 206-7: Is neuron #29 actually in Figure 5x?

12) Line 344-5: Can you unpack this statement?

13) Line 359-361: Give particular examples of some circuit in which this statement is true.

# Peer review - Round 1

Editors:
- Pascal Fries, Ernst Strüngmann Institute (ESI) , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24573.017](https://doi.org/10.7554/eLife.24573.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "β Band Oscillations in Motor Cortex Reflect Neural Population Signals that Delay Movement Onset" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Van Essen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Eric Maris (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study investigates the role of β oscillations in motor control using neurofeedback training of β power and decoding of spike rates across multiple simultaneously recorded neurons. Previous studies have shown that spontaneous fluctuations in β power correlate with several parameters of movement initiation, with higher β power generally slowing movement initiation. Previous studies have also used brain stimulation approaches to provide further evidence for this. The current manuscript adds substantial new evidence by using neurofeedback to modulate β power. Neurofeedback is an alternative way to experimentally control β power. It has the disadvantage that β power modulation is not pure, but accompanied by power changes in other frequency bands; yet it has the advantage over conventional brain stimulation techniques of avoiding potentially unphysiological conditions. Using a novel neurofeedback-reaching task, animals first adjust the LFP-β power in a neurofeedback task to four predetermined states, ranging from very low to very high, and then execute a reach task to a visual target. It was found that reaches preceded by low β power had a significantly faster reaction time and the population state of the neural network was significantly closer to a movement onset state than when the β power was high, demonstrating a correlation of neural population activity with longer reaction times during increased β oscillation activity. Employing neurofeedback to voluntarily modulate β LFP power in specific brain areas and then studying behavioral and neural population effects is highly novel and interesting. In summary, the study provides an interesting and substantial scientific advance. There are several points that need to be addressed to further improve the manuscript.

Results:

Strategies for variation of β power. The authors argue that subjects may choose their own subject-specific strategy for generating or suppressing β activity, including several possible 'internal behaviors'. However, can the authors sufficiently rule out 'external behavior'? In other words, could β power be modulated by more or less overt motor activity, like below-threshold movements or muscle co-contractions? This would be important to check, e.g., by sampling some EMG activity.

Why were the reach movements performed only in one direction? This makes the task highly monotonic and predictable. Animals probably have been trained before to perform the CO task in several directions. Why was it not possible to maintain multiple reach directions in the task? On the one hand, the statistics would probably not have been so conclusive with a smaller number of trials per reach condition. On the other hand, showing the effect of β power in behavior and neural network independent from the intended action would have been much more powerful. This should be properly discussed.

The authors use a complex experimental approach to deal with the fact that non-β frequencies are co-modulated during the β neurofeedback epoch of the task. A much simpler approach (which does not require new data) would be a multiple regression analysis in which one quantifies how much of the variance in the movement onset times can be explained by β power on top of the power in the frequencies below 10 Hz. (Frequencies higher than β may be ignored, because these will only have a small effect on the β power normalization, as a result of the 1/f scaling of the power.)

Results, paragraph two: This paragraph gives the impression that the β power changes were unrelated to power changes in other frequency bands. This is not convincing, because Figure 2E,F shows that monkeys C and G modulate their low-frequency power opposite to the β power. These spectra show z-scored power, in which the power in each frequency bin is normalized by subtracting the mean and dividing by the SD of that frequency bin across trials. However, the normalization for the feedback training was done differently: it was performed directly on the raw power values. Low-frequencies have the largest power and will therefore have the strongest impact on the normalization during feedback training. It is therefore a powerful strategy for the monkeys to modulate their low frequency power. This is precisely what monkeys C and G seem to have done. The authors should fully acknowledge that β power changes are accompanied by systematic changes in other frequency ranges. Even if they had trained monkeys on the non-normalized β power, the animals would have likely learned to co-modulate other frequency bands. Physiologically, fluctuations in power of different frequency bands are positively or negatively correlated, depending on the respective bands. Nevertheless, monkey S has apparently used a different strategy, because Figure 2D suggests that low-frequency power is not modulated opposite to β power. The authors could elaborate on this monkey's data and probably use it to demonstrate that normalized β power was enhanced during feedback training in different ways, but always had the same behavioral effect.

Subsection “Using other methods to compute β power shows the same movement onset relationship”: This is an extra test, which renders the correlation between γ power and MOT insignificant. This same test is not done for any of the other frequency bands, so we do not know whether it would affect them in the same or a different way. Also, here the individual significance testing per animal is a problem. All three subject show negative z-values, two show individually significant effects, only one misses the significance. Is the effect significant, when the data are combined across subjects?

Power in the 65-100 Hz band is typically very small in absolute terms, when compared to β power or even lower-frequency power. Thus, it likely did not contribute very much to the monkeys' strategies during feedback training. I suggest the authors quantify the percentage of 65-100 Hz power contribution to the denominator used for normalization during feedback training. I expect that this number is very small, and that the animals modulate γ power opposite to β power, simply because this is the physiological pattern. This should be acknowledged rather than argued away. It would be interesting to see whether β power and 65-100 Hz power is similarly anticorrelated outside the feedback task, e.g. during CO task performance.

There is the need for further clarification regarding the logistic regression classifier to demonstrate (1) the relation between the population firing rates and movement and (2) how this relation is modulated by β oscillatory power. It is possible that this relation is driven by a small fraction of the recorded neurons, and it would be useful to know this. There are regression techniques (forward, backward, stepwise predictor selection) that provide this information. Given the identification of prediction-relevant neurons, it would be interesting to know exactly how β oscillatory power modulates their activity. Provided the number of prediction-relevant neurons is not too large, this should not be too difficult.

Was there a significant correlation between time to target and movement onset time, when data from all animals are combined?

Where the authors compare neuronal activity during CO and NF tasks, they should acknowledge that the CO task occurs always after the NF task, such that there could be an unspecific effect of time.

Subsection “Modified β neurofeedback task shows 1-10 Hz band power does not account for movement onset time trend”: "…movement onset times followed […] not 1-10 Hz power ordering." For the xy control task, please provide a test for the low frequency band stating the absence of this effect.

Subsection “Comparing single and multi unit responses to β oscillations during the CO and NR tasks” paragraph four: Are those smaller R values significant? Is the difference between within-task slopes and across-task slopes significant?

Paragraph six of the same subsection: "…R2 values less than 0.5 in Figure 6H." Are these values still significant, i.e., when tested by a Monte Carlo test?

Figure 4B shows a cloud of points (small x-axis values and large y-axis values) that stand apart from the main cloud. Are they included in the analysis? Please comment.

Figure 7A: The values for monkey G are about an order of magnitude larger than the values for monkey C. The effects look very similar. The authors should nevertheless comment on the huge difference in magnitude.

Figure 7E: Is this significant after combining monkeys?

Methods:

Calculating the LFP power with the multi-taper method with K=5 tapers from a time window of T=0.2s (see Materials and methods) leads to spectral smoothing with a half-bandwidth W=15 Hz!!! This follows from the equation K=2TW-1 (see your multi-taper method tutorial for reference). This means that your power estimate at frequency f is actually represents the smoothed power from the frequency band [f-15, f+15] Hz. However, this does not seem to be the case, when looking a Figure 1D. Using fewer tapers would reduce frequency smoothing at the expense of more noise. However, since "β_est" was averaged in the frequency range of 25-40 Hz, more noise might not be so problematic. Please clarify what was actually done.

Results are only based on p-values and no effect-size measures are reported. These can easily be provided and are useful (see van Ede et al., 2012, JNPhys, for a related study and a motivation). These effect-size measures could be the percentage of explained variance for the movement onset times (for the first observation) and the probability of correctly classifying a spiking pattern as coming from the pre or the post movement period (for the second observation).

Authors mainly report statistical tests separately for the three monkeys. This should always be accompanied by a test that combines across monkeys. This is particularly relevant, as they also report that some effects are not consistent across subjects. In that case, the decisive test is the one that combines data across subjects.

On a number of occasions, the authors perform a statistical test on the outcome of a classification in which training and test sample were identical. Such a test is biased. Although biased, this does not invalidate the paper's main results, which were obtained with a different training and test sample. This issue should be explicitly addressed.

Results section, paragraph three: "…3-10 days of executing the NR task." This suggests, there are only 3-10 sessions of data per animal, but Figure 1E indicates a much larger number of sessions per animal. Please clarify! Were there multiple sessions per day?

Subsection “NR task controls”: Trials with MOT smaller than 0 and greater than 0.7 s were removed. Was the same pruning done for the target analysis? This should be consistent across analyses.

Subsection “Movement onset trend is specific to β band frequencies”: The analysis should not only be performed on pre-defined bands, but correlations between power and MOT should be calculated for each frequency bin. This is not a must, just a suggestion. In the current frequency-bin definition, the 1-10 Hz bin combines δ, theta and α. The authors should at least make an effort to separate theta and α.

The authors should explain how they derive channel level activity, rather than merely pointing to the paper of Chestek et al., 2011.

Subsection “Comparing single and multi unit responses to β oscillations during the CO and NR task”: This will likely distort results.

In the same section: Is 1.5 sec before go cue not too much for the CO task? Please explain!

Materials and methods section: Please also specify the length of the electrodes.

Also please be more specific on the implantation location of the electrodes, e.g., hand or reach area of M1 and PMd?

Subsection “Chance level performance of β neurofeedback epoch”: Besides the z-score, please also provide some absolute numbers on the performance, e.g., like: "on average, xx successful trials per minute with an overall success rate of yy% ".

Subsection “NR task variant using β band and 1-10 Hz”: Same dpss as used before?

Subsection “Trial re-allocation analysis”: Authors might want to consider this paper, which reveals issues arising when data are binned before calculating correlations: A jackknife approach to quantifying single-trial correlation between covariance-based metrics undefined on a single-trial basis. Richter CG, Thompson WH, Bosman CA, Fries P. Neuroimage. 2015 Jul 1;114:57-70. doi: 10.1016/j.neuroimage.2015.04.040. This does not render r-values obtained through binning invalid, however, their absolute values are typically inflated.

Figure 6F-H: Correlation coefficients might be more appropriate than a linear regression (R2), since the values on the x- and y-axis are 'equally' independent variables.

Figure 6H: If those slopes are to be compared to the subset based slopes, they also need to be based on subsets.

Writing and presentation:

It would be helpful if the first paragraph of the Results section would specify the recorded brain areas, even if this is mentioned elsewhere.

Throughout, the authors use the word "trend" to mean a significant systematic dependence. I guess this is motivated by their use of Cuzick's Test for trend. Readers might misunderstand this, because the word "trend" is often used for an effect that does not reach significance.

Introduction section, final paragraph: It should be mentioned here that monkeys might modulate normalized β power by modulating power outside the β band, i.e. by modulating the denominator. Also mention here that this will be addressed later in more detail.

Subsection “The neurofeedback epoch results in varying levels of initial β power prior to reaching”: The authors should emphasize more that they relate behavioral performance to β targets, not the actual β levels. That is a crucial difference to previous studies, which related behavioral performance to spontaneously occurring β levels. The β levels observed in the present study were likely highly correlated with β targets. However, it is conceptually important that the authors intervene with the system through neurofeedback by setting β targets. This is a crucial distinction to previous related studies and should be made more explicit.

Subsection “Modified β neurofeedback task shows 1-10 Hz band power does not account for movement onset time trend” "within the bin": Do the authors actually mean speed within each bin, or rather the speed during the response?

In the same subsection: Neither "four bins in a row" is clear, nor does the reader now the particular units that are referred to.

Subsection “Comparing single and multi unit responses to β oscillations during the CO and NR 338 tasks”: What is the alignment in Figure 6A, upper and lower panels?

Subsection “Β oscillations during the NR task and CO task reflect a shift in neural population activity away from a movement onset state”: The authors need to mention that they compare pre-MO to post-MO in the NR task. This is clear from the figure, but should also be clear in the main text.

In the same subsection: The lines leading up to the description of Figure 7B. This figure shows distances of the classifier to MO threshold as a function of β target, not as a function of observed β level. The feedback-related definition of β targets is the crucial manipulation in this study. Therefore, the authors should here point to the potential influence of β targets (not β levels) on classifier distances.

In the same subsection, paragraph two: Consider replacing 'lag' with 'history'.

Also in this subsection: "… how far an observation's neural state was [away] from [the state of] movement onset." Consider including the [bracketed] words for improved clarity.

In paragraph five of this section, and also multiple times later: 'NF trials': Do you mean NR trials? Please be consistent throughout the MS and the figures!

Subsection “Advantages of using neurofeedback to study behavioral correlates”: "the neural signal is not tarnished with a stimulation artifact". This comes quite suddenly. The authors should introduce that β could be modulated through tACS or similar methods, and that this poses challenges for simultaneous recording of neural activity.

Subsection “Calculation of β neurofeedback cursor”: This description with new neural data and previous data was confusing for me.

Subsection “Chance level performance of β neurofeedback epoch”: "chance fluctuations": Specify that this is about chance fluctuations in β power.

Subsection “Trial re-allocation analysis”: "assess whether non-normalized β power" should better read "assess whether MOTs for non-normalized β power".

Subsection “Β amplitude to spike rate mapping”: The authors use the word "bin" in two meanings, one of them referring to something like "compound bins" made of three smaller bins. This is confusing and should be reworded.

Subsection “Classification between neurofeedback and reaching tasks”: Please provide a reference here to explain the used method.

Figure 1E: The colors for the different monkeys are hard to separate. If readers print this figure in greyscale, they will be hardly distinguishable. It would also be helpful if different symbols were used (e.g. open and closed circles) for training versus task/recording sessions, respectively.

Figure 1E: Some x-axis ticks would be useful here.

Figure 2: Is this data from one session per animal? Please specify!

Figure 2 would benefit greatly from a color legend inside the figure (rather than merely in the legend). Also, the authors use "teal", which some non-native English speakers do not know. They could circumvent this potential source of confusion by using "green".

Figure 3: What is the sample size here?

Figure 5: The title "Non-β frequencies do not account for the movement onset trend" does not follow from the data presented here (1-10 Hz could also account for it), but only from later control analysis. Therefore, please change the figure title.

Figure 6: The figure would benefit from a color legend inside the figure. Generally, more (color) labeling inside the figures would make it easier to understand the figures.

Figure 7: In subpanel labels, 'NF' should probably read 'NR'.

Legend. "Same colormap as in Figure 6B", (not F-H).

Figure 7B: Blue and green traces are not ordered as predicted. This should be mentioned.

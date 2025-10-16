# Peer review - Round 1

Editors:
- Valentin Wyart, École normale supérieure, PSL University, INSERM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55365.sa1](https://doi.org/10.7554/eLife.55365.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your work addresses an important issue with the standard methodology for modeling perceptual decisions. Your careful simulations of non-integration models show very clearly that non-integration strategies can produce fits that are qualitatively similar to evidence integration (and therefore mimic evidence integration) in widely used paradigms. The novel methodology you propose to distinguish integration from non-integration strategies represents a timely achievement. Altogether, your work provides an important cautionary tale for the existing literature on modeling perceptual decisions. We congratulate you again for this work, which we are happy to publish in eLife.

Decision letter after peer review:

Thank you for submitting your article "Differentiating between integration and non-integration strategies in perceptual decision making" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Valentin Wyart as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marius Usher (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This manuscript describes a behavioral modeling study which aims at differentiating integration from non-integration strategies during perceptual decision-making. For this purpose, the authors rely first on a simulation-based approach by comparing an evidence integration model to two non-integration models (extrema detection and snapshot) in different paradigms used to study perceptual decision-making: fixed stimulus duration (FSD), variable stimulus duration (VSD) and free response (FR). The authors show that non-integration models display qualitative features commonly used as signatures of evidence integration. Based on the results of these simulations, the authors then propose a paradigm combining FR and VSD trials which afford to better distinguish integration from non-integration strategies. The authors report that six human subjects tested in their paradigm are better fitted (both quantitatively and qualitatively) by an evidence integration model.

Both reviewers found that your article addresses an important issue with the standard methodology for modeling perceptual decisions. Indeed, because evidence integration is an optimal (or at least adequate) cognitive strategy for such tasks, it is typically assumed that perceptual decisions rely on evidence integration. Your simulations of non-integration models clearly show that non-integration strategies (e.g., extrema detection) can produce behavior and fits that are qualitatively similar to evidence integration. Furthermore, the paradigm and methodology you propose to distinguish integration from non-integration strategies represents a timely achievement. Both reviewers found your article to be clearly written, and to provide an important cautionary tale for the existing literature on modeling perceptual decision-making. The fact that it emphasizes the importance of simulating competing models of behavior and performing parameter recovery analyses (as proposed by Palminteri et al., 2017 and Wilson and Collins, 2019) is also something very valuable for the field.

Although the reviewers do not have significant reservations that would require essential revisions of your article, they have identified different points (listed below) that would benefit from clarifications in a revised version of your article.

1) Origin of the behavioral similarity of integration and non-integration strategies:

The critical reason why non-integration strategies can mimic integration when fitted to behavioral data in random-dot motion paradigms could be brought up more explicitly in the manuscript. It appears to be that the motion evidence SNR is not measurable directly, and thus the SNR parameter in non-integration models can be set to widely implausible values to fit the behavioral data. The authors rightfully mention at the end of the Discussion that paradigms such as the ones used by Waskom and Kiani, 2019, but also Drugowitsch et al., 2016, afford to measure the sensory SNR and thus put an upper bound on the performance of any non-integration model. The issue of the non-measurability of the motion evidence SNR in random-dot motion paradigms could be stated earlier and more explicitly in the manuscript. It would make even clearer why non-integration models can be tweaked to fit behavioral data simulated using evidence integration.

2) Distinction between differences sources of behavioral variability:

Another related point of discussion could be the definition of SNR in the model. Noise in perceptual decision-making can arise from at least three different sources – as laid out in Drugowitsch et al., 2016: 1. noise in sensory processing (here, motion processing), 2. noise during evidence integration, and 3. noise during response selection. As emphasized in the previous point, the core issue put forward by the authors – that non-integration models can be fitted to data by tweaking a parameter (SNR) that is not measurable independently – illustrates the danger of not characterizing and quantifying the different sources of decision errors in these tasks. It could be useful to state explicitly in the Discussion that an alternative strategy for ruling out non-integration models is to measure the sensory SNR for the evidence used in the perceptual decision-making task. While it is not (at least not easily) possible for random-dot motion stimuli, it is clearly possible for pulsed evidence in terms of gratings (e.g., Drugowitsch et al., 2016), but also contrast (Waskom and Kiani, 2019).

3) Additional discussion of existing literature on integration and non-integration strategies:

i) The mechanism referred to as “extrema detection” may precede integration as an account of perceptual decisions, under the name of Probability Summation over Time (PST; Watson, 1979). While this is cited, it would be helpful to discuss in more detail why PST was historically used in psychophysical tasks, while evidence integration is preferred in studies with stochastic evidence that extends over longer intervals. Unless the authors believe that the two mechanisms were confounded in these older psychophysical studies and that, in fact, evidence integration was misidentified as evidence for PST.

ii) There is at least one recent study that provides a complementary method for distinguishing evidence integration and extrema detection (Glickman and Usher, 2019). The idea was to plot the "integrated evidence" until response in a FR task. As shown in Figure 4D of this paper, extrema detection predicts that the integrated evidence should increase with time. This is quite different for how the integrated evidence varies with time under integration mechanisms (Figure 4A, 4B), where it is either constant or decreasing. If the authors can record the time-varying motion evidence within each trial, they could compare their method to this one. Even without such comparison, a discussion of this complementary approach would be helpful.

4) Decision bounds:

There is some confusion due to the swap between fixed or collapsing bounds within the manuscript. The original comparison is presented using a fixed boundary model, but then suddenly the collapsing boundary is preferred. If the use of collapsing boundary is necessary for the demonstration, the article should mention this model in the first part. Also, one should provide more details about how it fares when compared to the fixed boundary model in terms of model evidence (e.g., BIC).

Another important point for existing research concerns how much model misspecification might impact parameter recovery with respect to decision bounds? Many applications of the drift-diffusion model are used for asking questions about how threshold is adjusted, e.g. to speed-accuracy manipulations, and how that might be altered in different groups (aging, ADHD, OCD, etc.). It would be very important to know, based on additional simulation-based analyses, whether the conclusions about decision thresholds/bounds are somewhat less impacted by model misspecification (i.e., whether there is true integration or not) than non-decision times.

5) Leaky integration:

The authors state that "leakiness" can be seen as a spectrum that links evidence integration with extrema detection. I agree that it is the case in FR paradigms which are modeled with an accumulation-to-bound model. But I can't see how it would be the case for bound-free evidence integration in FSD or VSD paradigms. Could the authors clarify this statement?

Also, the classification of S1 as non-leaky is not particularly convincing, especially since the difference in BIC seems to support leak for this particular subject (and its time constant is similar to that of S4 and S5).

Also, the authors should also mention somewhere in the Discussion that random-dot motion stimuli do not afford to distinguish between a time-dependent leak (as a function of time) and a stimulus-dependent leak (as a function of the presentation of evidence samples). Indeed, recent results obtained by Waskom and Kiani suggest that the "leakiness" observed during perceptual decision-making is stimulus-dependent, not time-dependent.

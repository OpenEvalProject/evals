# Peer review - Round 1

Editors:
- Charles E Schroeder, Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26642.025](https://doi.org/10.7554/eLife.26642.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A quantitative theory of γ synchronization in macaque V1" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Charles E Schroeder (Reviewer #1), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Van Essen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bard Ermentrout (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months.

Summary:

This paper addressed the widely held view that, a stable, shared frequency over time is considered a condition for functional neural synchronization in the gamma range. The findings show that actually, the opposite is true. Instantaneous frequency modulations are critical for adjusting phase relations between different neural ensembles, and thus for synchronization of their oscillatory cycles; this is a key requirement for communication through oscillatory phase synchrony or coherence. The authors show that for local neuron populations oscillating at different gamma frequencies, if similar enough, these frequencies continually attracted and repulsed each other, which enabled preferred phase relations to be maintained in periods of minimized frequency difference. This dynamical interaction is predicted by the theory of weakly coupled oscillators, a fundamental mathematical principle that likely applies widely across brain regions and oscillation frequencies. The paper has a great many strengths, particularly, the outstanding effort at making this topic accessible to the general systems neuroscience audience. However, it could use improvement in several areas.

Essential revisions:

Along with the specific issues noted by the reviewers, there are a few broad concerns that the authors should address: Under reviewer 1 – 1) The issue of a negative control; 2) Negative detuning; and 3) Volume conduction. Reviewer 2's broad concerns were: 1) The authors seem to confuse the PRC and the coupling function throughout the paper; 2) Since they measure Phi, they can now compute the actual interaction function at both sites and this is even more informative than is G; 3) the way that G(φ) is plotted looks very sinusoidal possibly a consequence of the way the phase is extracted; and 4) Since the frequency varies rapidly between the two sites, it may covary between the two populations. Reviewer 3 also wanted to see a control analysis where the full analysis pipeline is applied to non-simultaneously recorded (and so un-synchronised) trials (either by shuffling trials or combining non-synchronously recorded probes), to ensure that the SSD step is not picking up some common effects (e.g. stimulus onset) that are inducing the delta-phase-delta-if relationship. Reviewer 3 also asked that the authors give some heuristic guidance for experimental designs to which these techniques can be applied. Presumably they need to systematically modulate both connection strength and frequency difference, as done here? Finally, reviewer 3 requested that the authors deposit the data in a suitable repository such as Dryad to reduce their future administrative burden and to ensure long-term stable access. https://opennessinitiative.org/

Reviewer #1:

This paper addressed the widely held view that, a stable, shared frequency over time is considered a condition for functional neural synchronization in the gamma range. The findings show that actually, the opposite is true. Instantaneous frequency modulations are critical for adjusting phase relations between different neural ensembles, and thus for synchronization of their oscillatory cycles; this is a key requirement for communication through oscillatory phase synchrony or coherence, and idea championed by Varela and von Stein and others, and more recently by Fries. The authors address a specific paradox: cell ensembles oscillating at different gamma range frequencies can somehow communicate. Recording with laminar multielectrodes placed in areas with different parafoveal receptive fields in monkey visual area V1, they show that for local populations running at different gamma frequencies, if similar enough, these frequencies continually attracted and repulsed each other, which enabled preferred phase relations to be maintained in periods of minimized frequency difference. This dynamical interaction is predicted by a physics theory – that of weakly coupled oscillators. This fundamental mathematical principle of synchronization through instantaneous frequency modulations likely applied widely across brain regions and oscillation frequencies. This paper has a great many strengths, particularly, the outstanding effort at making this topic accessible to the general systems neuroscience audience. We also really like the bicyclist analogy, which is also very Dutch. We do not see any serious flaws, however, the paper could use improvement in several areas. Comments on these are below.

First, a few broad issues.

1) Negative control. It would be nice if authors can show a case that can be considered reasonably as a negative control. The reason is that all figures show the cases of positive effects consistent with the theory. Evidence would be stronger if there are no effects like flat G(θ) when there is no interaction. That would also help in arguing the functional role of gamma synchronization later in Discussion. Figure 3—figure supplement 1 shows a negative dependence of interaction strength on cortical distance, which may suggest what a negative control case could be. However, the lowest values are still above 1 Hz. A more desirable control would be to use elevated gamma activity recorded simultaneously in 2 unrelated cortices. One control possibility might be recordings separated by much greater cortical distances. Assuming the authors do not have such cases, recordings during no stimulation or when animals are asleep may work. Even when control conditions are met, interaction strength still might not be zero. It is possible that there may always be some residual amount, as some interactions could remain even for null conditions. However, one might hope to find that interaction strength under control conditions is significantly smaller than values during test conditions. Also, even with a residual interaction strength, preferred phase could deviate from those during test conditions.

2) Negative detuning. Readers might surmise that for a give pair of sites, a pair of δ IFs, one positive and one negative values of same magnitudes, can be obtained, like IF1-IF2 or IF2-IF1, so that there could be negative detuning as shown in Figure 5. Also, 2 functions of G (θ) can be obtained, and those can be mirror images of each other across the line ΔIF = 0. Is that correct? It may help the authors' case if an example of negative IF is shown in Supplementary Information. If the answer is yes, then I could understand the left-right symmetry of Arnold tongue (as in Figure 5B). However, then why are the cases in Figure 7 not left-right symmetric for physiological data?

3) Results section: "strongly reduce the influence of volume conduction by calculating current-source density (CSD)" Though the authors' have innovated extensively, the basic laminar electrode approach to data collection in awake monkeys is not new. There are quite a number of studies by a number of groups that used this method to analyze the areal and cellular generators of specific VEP, AEP and EEG components in monkeys between ~1990 and the present. It would be helpful to the broad readership of eLife if the present study were put in the context of that literature. Additionally, effects of volume conduction have been subject of debate over the last several years, and it would be helpful to readers to point to that. This all highlights the particular strength of the CSD approach relative to more typical LFP recordings. Note also, that there is a microscale phenomenon in volume conduction that might be relevant to this paper (Kajikawa J Neurophysiol. 2015).

Now, some more specific concerns

Introduction section: It would be helpful if the authors would be more descriptive introducing concepts of detuning and local stimulus contrast.

Results, first paragraph: Gamma power in the deepest layer is remarkable, but is analyzed rather later as an afterthought. This might be brought forward in the analysis and done in parallel with the other layer compartments.

Figure 1D Supposedly the shading represents SEM? Please state.

Results, second paragraph: It would help to state in the manuscript how the specific components were chosen. According to the Supplementary material, they chose the components with the largest fraction of spectral power in gamma frequencies (25-60Hz). They also state that in most cases there was one clear component representing gamma-band fluctuations. What was the percentage of cases where there was no clear component? What happens in cases where there was no one clear component?

Figure 2E: Shouldn't mean IF modulation be called mean ΔIF modulation? Do the number of dots in E reflect time samples across 33 trials presented in D? Number of observations used in this analysis should be clearly stated. Also, the relation should be quantified with statistics. Why is this based on so few trials? I understand that monkeys would usually go through several iterations of an experiment. Does this relation hold through different runs?

Results section: "The key to understanding how this dynamic relationship leads to synchronization is that phase relationships associated with lower frequency differences are maintained than phase relationships- associated with higher frequency differences" This is unclear to me. Yet, understanding this link is critical. What is meant by "maintained" here?

Results, paragraph two, penultimate sentence: typo – "are (better) maintained"

Results, third paragraph: – Re Figure 3B/Figure 3—figure supplement 1: Tell us the IF for each of the V1 sites before giving us the ΔIF. Also are effects of ΔIF linear x the band?

In the same paragraph: How was the 1Hz modulation amplitude derived?

Figure 3E: this description is at odds with the Figure It looks more like 2x that (~3.5 Hz); it only becomes obvious later that the description refers to 1/2 amplitude modulation. The IF modulation in H looks larger than in E (around 4 vs. 3 respectively). This should be clarified. Also, it would be good to quantify if there is any difference in IF modulation between these two cases.

Results: "The chosen examples were representative for the 805 recorded across-probe contact pairs in monkey M1 and 882 pairs in monkey M2." How was this quantified?

Figure 3B, E, H readability of figure would improve if frequency difference (or max and min values used to estimate it) were directly marked on the axes. It would also help to clearly indicate N which was used to obtain these results (same for C, F, I). These results are shown qualitatively. Maybe some quantification using permutations will be beneficial.

Results, fourth paragraph: typo "hence speed is analoguesous to"

The cyclist analogy is outstanding (and very Dutch)!

Subsection “The theory of weakly coupled oscillators (TWCO): A framework for cortical gamma synchronization”: This is a point that occurred at several points throughout the paper. The authors mention horizontal connectivity, but in the communication through synchrony idea (aka CTC of Fries), hierarchical connectivity (e.g., between given RF representations in V1 and V2) is really more relevant lateral connectivity between different eccentricities in V1. Yjis point should be addressed in the Introduction and, while it is mentioned, it should be clarified in the Discussion. Through the authors downplay the notion, the present findings do seem to fit with Prof Singer's Binding Hypothesis.

In the same section: The formula includes only the detuning (Δω) and not the frequency itself. I understand that the authors would like to concentrate on gamma (and they provide clear motivation for that) but it will be good to discuss how this result might be extended to different frequency bands.

Figure 4E-G: Aren't the functions supposed to have the shape of a sine wave? Particularly, Figure 4G does not look like that: downward peak look like they have almost twice the width of upward peaks.

Figure 5 legend: typo "we to we"

Subsection “TWCO predicts synchronization properties of V1 cortical gamma rhythms”: "PLV variations over single contact pairs were substantially captured by the analytical predictions as a function of Δω and ε (model accuracy: M1: R2=0.18, n=7245, M2: R2= 0.32, n=7938 Figure 6 C,D”? It would be helpful to explain why R2 0f 0.18 and 0.32 values are considered substantial.

In the sixth paragraph: Sig s6 is measured data not model result – Should be S5

In the seventh paragraph: Is there any reason for not including noise in the model?

In the same paragraph: "The results show that gamma rhythms with a higher frequency in a pair had the leading phase." This should be unpacked a little. Please state how leading and lagging phases are assigned.

In the tenth paragraph of the same section: "in the (CSD-CSD) gamma band (feedforward-feedback) as a function of detuning and interaction" This should be unpacked a lot. How are feedforward and feedback determined here?

Figure 7 A-C: This Figure is not well motivated, it’s not clear why f-f vs s-f for some and not others. Why are B&C monkeys combined and not in A&B? Does the causality give the same directionality between IF1-IF2 and IF2?

Figure 7: Analyses of MUA for Figure 7 needs more explanation. Not clear how gamma phase was defined for spike timing. Did the authors derive/filter spike density functions? And with what kernel/binsize? Also, it is better to shown raw and processed MUA, as shown for CSD in Figure 2A.

Figure 7—figure supplement 4: Does "gamma amplitude" mean the absolute amplitude of gamma band after Hilbert, or the amplitude of real signal? Also, are those amplitudes reflecting the sums of gamma in 2 sites? Please clarify. I may be wrong, but every panel in the figure shows full cycle of amplitude with a peak near zero phase difference, that makes me think it is real amplitude. Is it worth plotting gamma amplitude against interaction strength, ε?

In those plots, peak position is slightly rightward. Does it relate to phase leading/lagging? Same question again as above: If IF1-IF2 and IF2-IF1 are counted equally, then should the curves be symmetric around Δ-phase = 0?

Supplementary Information – Correction for CSD-induced phase shifts: "we normalized the phase-differences for each given contact pair to the condition having the smallest frequency difference," by doing what? Is this parallel translations of points along axes?

In the final paragraph of the subsection: "in the case of mutually anatomically coupled cortical locations, detuning strongly influences the main direction of information flow" As presented, this is questionable.

While grand G(θ) was used to predict PLV, preferred phase difference could differ among pairs according to Figure 6. Were G(θ) values shifted along the axis of phase difference to align the downward peak of the curve to the preferred phase difference for each pair?

Subsection “The Arnold tongue and the regulative parameters of γ synchronization”. Can authors show the range of detuning? Were there cases that can show large deviations in detuning that break down interactions?

In the same subsection: while larger detuning values would decrease opportunities for synchronization across distance in V1, when they are tied strongly to stimulus information in a cell's RF, e.g., the Gabor stimuli used in Ray and Maunsell, there are still opportunities for the neurons in V1 (seeing low contrast) to synchronize with ones in V2 with overlapping RF (also seeing low contrast) and the same for V1/V2 interactions across the different contrast regions of the Gabor. This means basically frequency segregation of channels seeing different "pixels."

Supplementary information: Equation 18 in Supplementary Information duplicates Equation 17. I guess the label "18" was meant for the line: "V(θ)"?

Summary: Likely many of the concerns are simply a result of our misunderstandings. We really enjoyed reading the paper and must say, it really stimulated our thinking. It should be similarly provocative for many others in the field and will likely prove over time to be a fundamental contribution.

Reviewer #2:

I found this to be a very interesting paper and I was quite excited to see how well the theoretical predictions matched the results of the Arnold tongues. I was surprised that the interaction function was so close to a sine wave (a point that I will address shortly below) I think that the paper needs some revision and it appears that the authors are somewhat confused by some of the mathematical terminology in TWCO and I will address that below as well.

Here are my main comments

1) The authors seem to confuse the PRC and the coupling function throughout the paper. They are not the same thing. In the theory of weak coupling, there are three things:

1) The PRC or adjoint function, Z(t) which is the infinitesimal PRC and is hard to compute with real neurons, but east to compute with models (see for example the tutorial: http://www.math.pitt.edu/~bard/bardware/meth3/node15.html#SECTION00052000000000000000on weak coupling of a simple voltage gated model;

2) The interaction function, H(φ) which is defined as:

H(θ2-θ1) = (1/T) ∫0TZ(s+θ1). C12(u(s+θ1),u(s+θ2)) ds

That is, it is the convolution of the PRC (Z) with the coupling between the oscillators, here denoted by u(t) with 1 = postsynaptic and 2 = presynaptic

3) The odd part of the interaction function which in this paper is G(θ) arises as follows

θ1' = ω1 + ε12 H(θ2 – θ1) Equation 1

θ2' = ω2 + ε21 H(θ1 – θ2)

If you let φ = θ2 – θ1, the phase difference and if ε12=ε21, then

φ' = Δω + εG(φ) Equation 2

where G(φ) = H(-φ) – H(φ) is proportional to the odd part of H(φ)

Equation 2 is what the authors measure; it is not the PRC. I just want to make that clear.

2) Since they measure φ, they can now compute the actual interaction function at both sites and this is even more informative than is G. By measuring θ1' and θ2', and plotting this against φ, equation 1 shows that

θ1' = ω1 + ε12 H(φ)

θ2' = ω2 + ε21 H(-φ)

thus, in addition to G, they will be able to measure ω1 + ε12 H(φ) and ε21 H(-φ). This will give them more information about the direction of coupling and also will give them the full value of H. Indeed, there is nothing here that requires the two H's to even be the same. Thus, I would suggest plotting θ1', θ2' vs φ as well as φ' vs φ.

3) G(φ) is plotted looks very sinusoidal. Is this a consequence of the way the phase is extracted? I suggest taking a model pair of oscillators, such as Hodgkin huxley and coupling them with synapse along with noise and heterogeneity in coupling and in frequency. Then use the method that is used for the data to extract G(φ) and H(φ) and then compare this to the actual determistic values found by setting the noise to zero and computing H and G as in the above. This would assure me that the method of using Hilbert transforms isn’t somehow removing all the Fourier modes beyond the lowest.

4) Since the frequency varies rapidly between the two sites, does this variability covary between the two populations? I ask this because one can take two uncoupled oscillators and apply a broadband correlated signal to them and they will produce a very nice peak in their phase-difference histogram. For example, see Nakao, Arai, Kuramoto PRE 2005, or other papers by Arai & Nakao, or for a neuroscience version, Zhou, Burton, et al. 2013 Frontiers in Comp Neuro.

Reviewer #3:

This study applies the well-known theoretical model of weakly coupled oscillators to experimental data from macaque V1. This is achieved through an elegant experimental design, which obtains simultaneous paired recordings over a large range of coupling strengths and frequency differences, to allow fitting of the oscillator model. While the idea is simple, the work is technically impressive and has broad important applications for interpretation and analysis of phase relations between brain areas. The writing is extremely clear; the authors have done an excellent job of conveying a technically complex piece of work in a way that should be accessible to a broad audience.

The results are impressive, but I would like to see a control analysis where the full analysis pipeline is applied to non-simultaneously recorded (and so un-synchronised) trials (either by shuffling trials or combining non-synchronously recorded probes). This would ensure that the SSD step is not picking up some common effects (e.g. stimulus onset) that is inducing the delta-phase-delta-if relationship e.g. in Figure 2E. (I don't think full permutation inference is necessary for all results, but just some confirmation that indeed the actual experimental data pipeline does produce flat delta-phase / delta-if curves)

The authors propose that the method of fitting TWCO model to data and associated analyses such as Arnold tongue plots might be applicable to other brain regions or frequency band relationships. It would be nice if they could give some heuristic guidance for experimental designs to which these techniques can be applied. Presumably they need to systematically modulate both connection strength and frequency difference, as done here?

The statistical analysis and Figure 6C-D show the overall average over all electrode pairs and stimulus conditions. Presumably the experimental contrast already induces a range of PLVs for each specific recording pair, so perhaps they could be evaluated statistically as well (e.g. scatter with pair PLV R2 as a function of distance between the pairs, or something along similar lines).

The authors indicate that data and code are available on request. I would strongly urge them then to deposit the data in a suitable repository such as Dryad to reduce their future administrative burden and to ensure long term stable access. https://opennessinitiative.org/

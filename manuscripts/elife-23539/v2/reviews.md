# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23539.043](https://doi.org/10.7554/eLife.23539.043)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The cyanobacterial circadian clock follows midday in vivo and in vitro" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior Editor and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors examine how the cyanobacterial clock aligns under varying environmental cycles, revealing a simple scaling law to midday across various Light/Dark cycles. In a very nice follow up they then show that it is possible to recreate these results in vitro using metabolic pulses. It is an impressive strength of the paper that they are able to go from in vivo to in vitro and obtain similar results. They go on to develop a mathematical model, based on the immediate response of the clock to environmental changes, which they then successfully test. The model is elegant and simple and produces experimentally testable predictions that the authors follow up on.

Essential revisions:

1) Please downplay the optimality argument, as requested by the reviewer below. Both reviewers agreed that this argument is not well supported.

2) Most importantly, the experiments lack biological repeats. Please either justify why biological repeats are not needed, or (largely recommended) repeat the experiments to verify reproduciblity. This is important in particular for the in vitro experiments (Figure 2 and 3), where it is stated that the experiment was done once (subsection “Estimation of clock phase in vitro in metabolic cycles”, last paragraph and subsection “Non-parametric bootstrapping of step-response datasets and L and D functions”, first paragraph), but also for the other 96-well based experiments.

Reviewer #1:

The authors study the phase of the cyanobacterial circadian oscillator under entrainment with different photoperiods (day length). A main finding is that the internal clock phase tracks midday under entrainment, both in vivo and in the test tube, and this can be explained by the measured phase shifts at dawn and dusk. Linearity properties of the phase shifting curves in a physiological range are sufficient to explain midday tracking, but this also generalizes to more complex perturbations. Overall, an elegant and general picture emerges, and a simple geometrical interpretation is proposed: that of the deformation of the clock orbit in light vs. dark conditions.

Would there be a more powerful way to exploit the purF reporter? I assume the authors do not have dual reporter strains? I would recommend putting the purF figure in the main, and to analyze the KaiC data in the same way (i.e. multiple peaks etc.).

An important test for the model would be to analyze period mutants. That, is assuming that the phase shifts do not depend on the mutations, it would be straightforward to predict if mode-locking can still occur, and if so what the entrainment phase is. Looking at period mutants seems quite obvious, why did the authors not do this?

Moreover, it would have been informative to identify mutants with entrainment defects. Or perhaps some entrainment mutants are already reported, and could have been analyzed?

Also, from the dynamical systems points of view, 1-d maps like the one proposed exhibit complex behavior (period doubling, chaos, etc.). It would have been very interesting to try and probe whether other regimes besides 1:1 can occur.

Reviewer #2:

The work appears to be of high quality, has very robust data, and should be interesting to the eLife audience. I do have the following concerns however.

1) Concepts developed in the paper. In the paper it is assumed that clocks in individual cells can only track one phase, and it is argued that tracking midday should be the optimal strategy, as it allows proportional expression of dawn and dusk genes. I think both these ideas require further thought and justification. It is well known in the plant clock field that the clock network can track dawn and dusk. For example (Edwards et al., 2010). There has also been theoretical studies on clocks (without assuming any multicellularity or coupling between cells) to examine what it takes to track more than one phase (Rand et al., J. Royal Society Interface, 2004). As the cyanobacterial clock is limited to one feedback loop this presumably means it is limited to tracking one phase, but this point should be discussed. If you are going to track one phase, it is not clear that tracking midday is an optimal decision. It could be that evening genes become more important under shorter days for example. It is not clear to me that equi-partitioning of the resources into two classes is necessarily clearly the optimal strategy.

2) Figure 7F: The cycle in phosphorylation state for the 'Day cycle' in the invitro system is quite elliptical in shape. It is not clear how one would estimate X and R from this ellipse, and whether or not one would gain a linear phase shift relationship in L(θ) from the elliptical orbits. It would be useful if the authors could comment on this, and perhaps show how the experimental orbits would map to the calculated D(θ) and L(θ) from the geometrical model.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The cyanobacterial circadian clock follows midday in vivo and in vitro" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai as the Senior Editor and Reviewing Editor, and two reviewers.

Please see comments below – the reviewers would like you to emphasize aspects related to the reproducibility, as was raised in the previous review. Specifically, please show all that data in the main figures (in Figure 2C, there's plenty of space to plot the two additional in vitro measurements). Also, please adapt your interpretation to take into the observed variability and discuss what the potential sources are.

Reviewer #1:

I believe the revised version addresses the general editorial comments adequately.

In addition, though the authors have partially addressed my comments, I regret that they did not consider my first major point on integrating the purF data in the main text, and also not analyze their KaiC data in the same way. I liked the purF analysis with the multiple peaks, which seemed more thorough than that presented for KaiC in the main. In particular this modification seemed not to represent a lot of extra work, so it is not intuitive why it was not done.

Reviewer #2:

In general I am happy with the revision, but I have the following concerns.

The new in vitro experiments slopes using a different method based on a fluorescent probe are less near to m = 0.5 than one would have expected (at 0.38). It isn't clear why the non-repeated in vitro study based on% KAICP is used in Figure 2 (with a m value of 0.51), whilst the new method that is repeated (showing an answer that is less close to the in vivo values) is in the supplement. This is especially true as Figure 3 now uses the new data from the fluorescent probe. In Figure 2C the comparison is only made between the non-repeated in vitro method based on %P KaiC, but the slopes based on the new method using an in situ fluorescent probe are not included. The authors should include the values from the new experiments in Figure 2C.

In Figure 3A it appears that phase shifts much larger than 4 hours are possible, even though phase shifts of <4 hours are claimed in the text and displayed in Figure 3C. Could the authors please explain the differences?

# Peer review - Round 1

Editors:
- Andrew J King, University of Oxford , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10450.012](https://doi.org/10.7554/eLife.10450.012)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Rate and timing of cortical responses driven by separate sensory channels" for peer review at eLife. Your submission has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor (Andrew King), and three reviewers, one of whom, Stefano Panzeri, has agreed to reveal his identity.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, data-based models were used to examine how information from different mechanoreceptive afferent classes is integrated in the responses of individual cortical neurons. The authors report that cortical activity reflects a combination of rapidly-adapting and Pacinian corpuscle inputs, with the former determining overall firing rate whereas the latter are represented by the precise timing of the activity. Their model results suggest that information about textures is represented in the primary somatosensory cortex by the statistically optimal integration of inputs from these two peripheral receptor channels.

Essential revisions:

Although the three reviewers agree that this is an interesting and important study and that the analysis is rigorous, they have raised the following issues.

1) Are the authors able to say where the inferred convergence of inputs from these two classes of mechanoreceptors takes place – in the cortex or at a subcortical level?

2) Given that model assessment largely revolves around predictive power and predictive power is impacted by reliability, the measurements of reliability mentioned in the Results (second paragraph) should probably be shown. Perhaps the authors could plot reliability vs accuracy. The authors should clarify how they measured reliability.

3) On a related note, factors unrelated to the stimuli, such as the stochasticity of spike generation, lead to a lack of reliability, which the authors comment on. The reader is told how well the model predicts the total variance (about half), but the model is probably performing better than this since some of the variance is due to the lack of reliability in the responses. The authors should estimate how much of the predictable variance (rather than the total) the model accounts for (e.g., Sahani & Linden 2003 NIPS; Ramirez et al. 2014 Nat Neurosci).

4) The authors report (Figure 2A) that most cortical neurons receive "significant contributions" from RA and PC populations. However, if the RA and PC population responses are correlated, a model-fitting algorithm might generate positive weights from a non-connected PC population even though cortical neurons receive input exclusively from RA afferents. It is particularly hard to exclude the possibility that a small (but statistically significant) input might be an artefact. The authors consider this issue in the Materials and methods. They state that the correlations were "low" – but how low? What is the correlation coefficient between the RA and PC population responses as a function of time resolution? Also, the authors use a whitening procedure to attempt to decorrelate (is equation 2 correct? Is the regularizing term not added?), but these procedures are delicate and it is not clear that the correlation issue has been fully dealt with. Further work is needed to address this. It may be useful to use a simulation approach, i.e. simulate cortical neurons with realistic filters that range from single channel to mixed, analyze them with their methods, and test whether their single/mixed nature is accurately recovered. Furthermore, the results (Figure 2A) are based on a statistical test (no details are provided for how this was done or what the critical P value was). Hence, a neuron that counts as convergent might have a strong input from RA together plus a tiny PC input that passes the statistical test, but is functionally irrelevant. Suppose that you define convergent input as where at least 10% of the total input strength comes from each channel, do you still see the same prominent convergence shown in Figure 2A?

5) The authors claim that cortical (time-averaged) firing rates are due to RA, not PC input. They state that their stimuli "drove RA and PC to the exclusion of SA1". On this basis, they consider only RA and PC responses in their study and ignore SA. However, Figures 1–2 of the supporting reference (Muniak et al., 2007) do show SA responses to both sinusoidal and noise stimuli. Given these data, it does not seem appropriate to ignore the SA afferents. Do the authors have peripheral recordings of SA1 responses? If so, they could apply their model-fitting approach. If they are correct, the weights from the SA population should turn out to be zero.

6) For the analyses shown in Figures 3–4 where full and RA/PC only models are compared, how were the RA/PC only results obtained? Were the cortical models retrained on only RA/PC input or were the RA/PC contributions in the full model simply set to zero? Given the concern about correlations, the authors should check whether they get the same results using the retraining method if that is not already what they did.

7) The conclusion that the precise timing of S1 neurons is mainly driven by PC input depends on how good the models for the RA/PC afferents are. The authors show a single neuron example (Figure 4A) where removing PC input degrades timing precision, but in Figure 4C (right – the 3 ms resolution case) it is only for a minority of points that PC explains more variance than RA. In fact, for most of the cortical neurons, RA explains more variance. If correct, this seems to undermine the conclusion that PCs drive cortical spike timing. Figure 1—figure supplement 1 shows that the RA afferent model performs poorly at 3 ms resolution. In this case, how is it possible (in Figure 4C right) that they explain so much variance? (It would be useful to define the R squared measure precisely and exactly what "variance" is meant).

8) The authors report that "filters optimized to convey information about texture closely matched the filters derived from measured S1 responses". This is not currently fully convincing. It seems from the Materials and methods that they find the RA and PC filters that maximize mutual information between the stimulus (measured in a 1 ms bin) and the model's response in that bin. They repeat this for 25 different textures. Then they look through these 25 results and pick out the one that looks most like the filters fitted from spike data (this important part of the process is only mentioned in the legend to Figure 5 – it should be in the Materials and methods). There are several concerns with this approach.

A) In classic studies of this kind (e.g. Olshausen & Field, Nature, 2006; Attick, Network, 1992), the optimization is carried out by averaging across a bunch of natural stimuli, not on individual stimuli. It is possible that cherry-picking from 25 separate optimizations could result in spurious matches. It would be much more convincing if the optimization was carried out across the whole set of 25 textures.

B) Even using the texture-picking method, "close" matches are only shown for 3 examples in Figure 5A. Figure 5B-D show similarities between the distribution of width and other parameters between real and optimized filters, but do not show how close these values are on a neuron by neuron basis (or even the means, medians or shapes of these distributions). If there really is systematic, close matching (which would be impressive), there should be a high correlation coefficient between e.g. actual and optimized filter width, etc. across neurons. Some test or comparison with other models is needed to justify the conclusion that filters for the recorded cells are/aren't optimal. Perhaps the authors could distort the textures or shuffle them somehow to see whether they can create "suboptimal" filters.

C) For the mutual information calculation, is it correct that stimulus and response are measured in the same simultaneous time bin? Should response latency not be taken into account?

9) For fitting the afferent models, how did the authors avoid over-fitting? Was cross-validation used when assessing model accuracy in Figure 1—figure 1? Why the unusual approach of sequentially fitting to individual stimulus types – why not fit on all 3 stimulus sets at once?

10) It is stated in the first paragraph of the Results section that the stimuli for the cortical experiments were "analogous but not identical" to the peripheral ones. This is potentially a problem, since statistically fitted, nonlinear models cannot be relied on to extrapolate outside their training set. At present, there are insufficient methodological details to understand how different the stimuli really were. Please detail, in the Materials and methods, exactly what the stimuli were in the two cases. Related to this, it is stated in the Materials and methods that the peripheral recordings were done in anesthetized animals. What about the cortical ones?

11) Materials and methods, subsection “Electrophysiology”. The paper includes only 4 PC afferents. The authors need to justify why this small sample size is sufficient or increase the number. Similarly, it is unclear whether multiple peripheral models can be generated using only 4 recorded afferents (subsection “Peripheral model”).

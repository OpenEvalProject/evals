# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70777.sa0](https://doi.org/10.7554/eLife.70777.sa0)

The article develops a mathematical approach to study the allocation of cortical area to sensory representations in the presence of resource constraints. The theory is applied to study sensory representations in the somatosensory system. This problem is largely unexplored, the results are novel, and can be of interest to experimental and theoretical neuroscientists.


---

# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70777.sa1](https://doi.org/10.7554/eLife.70777.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Expansion and contraction of resource allocation in sensory bottlenecks" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Memming Park (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the reviewers found the work interesting and engaging, they agreed that some major revisions would greatly strengthen the manuscript. All have consulted with each other and the reviewing editor to compile these major prompts. Please also see the recommended, slightly more minor, revisions below as well as the public reviews provided by each reviewer.

1) Clarifying assumptions made

The paper should explicitly state the assumptions of the model, and discuss their consequences much earlier, and in more depth.

Currently, the Introduction and first paragraphs of the results equate efficient coding with decorrelation (e.g. paragraphs 3 and 4 of the introduction and opening sentences of the Results). The authors address the role of noise only briefly in the Discussion. This could be expanded. "Efficient coding" is a broad conceptual framework, and not a single algorithm such as decorrelation or even redundancy reduction. Currently, the manuscript makes the impression that the two are the same.

Other, unstated assumptions of the model (e.g. constraints on the total variance of the bottleneck, and the assumption that output activity is equalized across all neurons) should be made more explicit. How are those assumptions connected to biology? Is there evidence that cortical neurons in the somatosensory system are equally active? Even if there is not – this should be addressed explicitly.

Also, the analytical results are derived with a number of assumptions about the correlation structure of the stimuli and the structure of the bottleneck. Please clarify these assumptions as well. Importantly, please more clearly define the cost function. Is it simply the squared error loss between receptors and representation?

2) Putting the math more front-and-center

The fact that all results are derived analytically is a clear strength of the manuscript, but the authors have chosen to refrain from presenting any math in the Results section. This is very unfortunate, because this makes the formal arguments more fuzzy than need be. Please find a compromise between a technical and very high-level paper, and include the essential formal steps of the arguments in the main text.

3) Expanding the simulation examples provided, increasing the scope of the results

Along these lines, and looping back to prompt 1 and clarifying the assumptions in the model, please include one or two examples with more complicated input statistics or system architecture. For example, it is frequently the case that a narrow sensory bottleneck is followed by an expansion (e.g. retina -> optic nerve -> V1) – could the theory say something about resource allocation in such scenario?

In another example – what if the correlation structure is more complex? E.g. in the auditory nerve correlations between sensors can spatially non-local, due to the presence of harmonic sounds (e.g. Terashima and Okada, NeurIPS 2012). These are just suggestions of more complex scenarios which the authors could consider. These additional results do not have to be obtained analytically, and could be optimized through simulation. Such additions could greatly strengthen the current paper, broaden its scope, and increase its impact.

To show that those results are robust for small variations in the stimulus distribution, please provide numerical experiments with a different covariance function. Perhaps try a Matérn covariance function with nu=3/2 which is slightly smoother than the OU covariance. The experiments are numerically difficult, so this prompt only requires showing a case in a regime where things are numerically stable (this should be possible since the authors have done something similar in the NeurIPS 2019 paper). We would like to see that the presented results are not qualitatively very different.

4) Provide more details on the star-nosed mole data and predictions from the model

Please report in more detail how the predictions are generated for the data from the star-nosed mole. This could be done in the main text. For example, one could plot predictions for different sizes of the bottleneck. As a field, we should not be afraid of showing the range of predictions for different parameter values (e.g. for different bottleneck sizes), and demonstrating where they match the data, and where they do not – this does not necessarily weaken the theory. In this particular case – the theory could inform us about not-yet-measured properties of the system, such as the size of the bottleneck. Moreover, this will be more explicit way to report these results.

Furthermore, to model the stimulus distribution for star-nosed mole case, the authors simulated a noisy sensory system to convert contact statistics (assuming a circular object) to receptor activation statistics. Star-nose mole parameters (Appendix table) are in the code provided, but it doesn't seem like code for the conversion from the contact statistics to the receptor activation statistics is included. Please share this code, since the text in the manuscript is missing much of the necessary detail for the reproduction of this work.

Recommendations for the authors:

A) page 2 and Discussion: The authors discuss the use of Fisher Information and other measures for their goal. The use of Fisher Information for optimal population coding can be dangerous especially when taking N to infinity, as then the convergence conditions of 1/FI to the MSE are not met (see Berens et al. 2012). The crucial quantity for convergence is the SNR. Thus, the stated reason is not a reason not to use Fisher Information, although it's fine for the authors to choose not to use it. The logic should be improved in the text, though.

B) The claim that full model has better MSE is not very convincing. The difference between using density only and receptor only makes sense. But the full model has an additional degree of freedom, so naturally it should be better then either if tested on the same data that it was fit to. Unfortunately, the dataset the authors have is only 11 points, so there's no easy way of splitting them to show that this is effect is real. Hence, it's hard to make a strong claim about the tiny change in MSE. Please weaken the claim. Also, Figure 5D scatter plot for the full model is very similar to that of the receptor usage model (I ran your code). Please provide the corresponding plots explicitly in the supplement instead of the code only for transparency.

C) The model makes no distinction between the density of sensors in different regions and the exponential decay of the covariance functions. This is not a problem from the perspective of theoretical predictions, but perhaps it could be explained better (maybe with additional illustrations?).

D) It wasn't clear what the authors mean by "second-order". One assumes this means that the input statistics is Gaussian, but perhaps this is wrong. Did the authors mean that they are only analyzing the covariance functions, i.e. second-order statistics? Or was it that the neurons' response entropy were quantified by their variance? Please clarify.

E) In the text, 'activation' and 'activation ratio' are used interchangeably. It would be better to stick with the ratio since it's really only the relative activation of the second population that matters.

E) The 'σ' as 'decay constant' should be explicitly mentioned in the main text in addition to the methods section. At first it seems to be the length-scale, but it turned out to be inverse length-scale which was confusing, since σ is often used to denote the inverse length-scale. (Figures1C, 2C)

F) Please add the following citations to other theoretical work, which considered efficient encoding of somatosensory stimuli and the allocation of cortical space :

a) Bhand, M., Mudur, R., Suresh, B., Saxe, A., and Ng, A. (2011). Unsupervised learning models of primary cortical receptive fields and receptive field plasticity. Advances in neural information processing systems, 24, 1971-1979.

b) Plumbley, M. D. (1999). Do cortical maps adapt to optimize information density?. Network: Computation in Neural Systems, 10(1), 41.

G) page 2: In the discussion about bottlenecks in the retina, recent work by Lindsey et al. (2019, arxiv 1901:00945) should be cited.

H) page 5: "Decorrelation has been found to be a…" -> Please add citations to this claim

Figures:

I) Figure 1D: This figure is quite confusing. The decaying covariance is plotted for a 1-D case, the axes are unlabelled, and it takes a while to figure out that these two block matrices do form a single covariance matrix (even-though they correspond to different regions). Please revise this figure.

J) Figure 2D: small boxes with receptor location is misleading. It shows increased number of receptors when it's the activation ratio that's different. Please revise this figure.

K) Figure 3: A/B-labels seem to be too large; the meaning of the boxes of different colors and the lines was unclear to me. What determines e.g. the line length? The two panels in A should be clearly labeled with what quantity is varied.

L) Figure 4: What are the dashed lines? Is it correct that 4B is a simple restatement of the fact that the lines in 3A left are more spread for smaller bottlenecks? Interpreting this as a sign of more plasticity is an overstatement.

M) Figure 5: Please normalize the RMSE in Figure 5D with respect to the power of the signal. Otherwise the numbers aren't that meaningful, unless some clarifying point is missing. (Or, why not just report r^2?) Please also provide RMSE curves for all different bottleneck sizes and discuss how plausible the optimal values are. Given the right panel, it looks like the RMSE is mainly driven by ray 11, the outlier. How stable is the inferred conclusion if ray 11 is left out? Also, the authors seem to use RMSE to compare percentages. Could the authors comment on the suitability for that loss function?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Expansion and contraction of resource allocation in sensory bottlenecks" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Regarding low-noise regime, it only appears in the discussion and it does not warn the readers that the numerous tiny tail eigenvalues are very sensitive to noise. This affects the robustness of the analysis and should be clearly stated in the text and appear after the first interpretation of the bottleneck results (Figure 2 and 2-supplement 4).

2. It is not stated clearly that decorrelation is an information maximizing transform only in absence of noise, which is a key assumption of the model. In the Methods (lines 493-494) it is written that adding the noise does not affect the eigendecomposition (and, in consequence, resource allocation), but if that is the case – it is an important result which should be highlighted and explored further – a sensory coding transformation which is independent of the noise level seems like an important finding. Please revise the text around this point.

3. It is misleading to claim that the analysis "maximizes information" without qualification in the abstract since this work only deals with variances. Please rephrase.

4. In Line 66, please add a qualifier to the statement that Fisher Information can be used to approximate Mutual Information. This is only true under certain assumptions in certain cases and specifically for optimal coding, the relationship is not straightforward (Berens et al. 2012, PNAS; Bethge et al. Neural Comp 2002).

5. lines 87-88: "We consider linear models which maximize information by decorrelating the sensory inputs, or, equivalently, minimize the mean-squared reconstruction error […]" – in a general case these two goals are not equivalent. The following citations referencing work by Doi and colleagues do not support this claim. This should be revised.

6. In Figure 1, it is hard to parse which colors are kept to mean the same thing across panels and which change meaning. An additional schematic of the model in this figure would help with clarity of the presentation.

7. In Equation 1, is P used at all? If not simplify. The explanation of P sounds complicated without really saying anything specific. Give an example of constraints that could be incorporated.

8. The assumption that the covariance between regions is zero is quite a strong one and seems central to the paper. This should be justified or at least discussed how realistic it is. In the finger tip example, one of course typically touches objects not with one finger but with multiple ones.

9. The brackets in Figure 3 were found to be very confusing, please revise.

10. The covariance functions in Figure 5 are not very different, it is not surprising that these result in very similar outcomes. Comment on this or consider revising.

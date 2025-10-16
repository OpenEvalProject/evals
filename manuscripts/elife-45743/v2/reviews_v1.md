# Peer review - Round 1

Editors:
- Tatyana O Sharpee, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.45743.sa1](https://doi.org/10.7554/eLife.45743.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Inference of nonlinear spatial subunits in primate retina with Spike-Triggered Clustering" for consideration by eLife. Your article has been reviewed by Joshua Gold as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript introduces a new method for the estimation of nonlinear spatial subunits in neural data using an LNLN model (a cascade of two LN stages). The paper has clear merits by showing that it is beneficial to utilize subunit models for predicting parasol RGC responses and V1 neural responses to naturalistic stimuli. Parasol spike data has been previously mostly analyzed without taking this into account.

The main concern to address is that for a "tools and resources" papers needs to include clear benchmarking of the advantages of the current method against other existing and/or published approaches for subunit identification. The consensus among reviewers was that one would need to include comparison with at least one other method for both the retina and the V1 dataset. Some of the relevant methods that you could use are provided below, which offer different trade-offs between accuracy and ease of implementation and the amount of background work needed to set the hyperparameters. It would be helpful if the authors could include a discussion to justify their choice of the alternative method. The alternative method might be different for the V1 and the retina dataset. Including a more detailed discussion of the available methods and the authors' perspective on which would work best at each circumstance or generalize across the light/stimulus conditions would be very helpful to the field.

The second concern was about the apparent inconsistencies in how the steps of the proposed algorithm were chosen (as detailed below) and that more methodological details need to be provided.

Comparison with existing methods:

While the manuscript includes some discussion of the existing methods, it is still not clear which model is the best taken into account that the subunits of the current model do not correlate with the actual bipolar cell receptive fields but rather with their clusters in some way. For the reader to take up this method, one would need to clearly see the pros and cons in speed, resolution, easiness of implementation, neural correlates of subunits and/or other key features of this model against other nonlinear subunit models (e.g. Liu et al., 2017 and the simpler earlier version by Kaardal et al., 2013) and/or simple convolution neural network models (Eickenberg et al., 2013, Vintch et al., 2015). It is critical for the reader to be able to assess the value of the current model. Assuming this is done properly, and these clarifications are added, this paper would be significantly improved.

One would like to understand and document clearly performance of the subunit-identification method across stimulus conditions (white noise vs. naturalistic stimuli) against conventional currently used methods. This could perhaps be done by applying the new model to existing datasets of parasol RGCs in different experimental conditions. If such data are not available, then perhaps the method could be tested using simulated responses constructed to mimic properties of the retinal neurons.

Questions about the proposed methodology:

There are some inconsistencies in the design of the proposed methodology. For examples, the method is motivated with an example that involves hierarchical splitting of subunits, but this hierarchical version is actually not used further on. Then the bare method (without regularization and fairly coarse stimuli) is used to analyze populations of OFF parasol cells (Figure 2B-F), but Figure 3 shows that much better subunits are obtained with regularization and finer white noise. One wonders why this improved method wasn't used to obtain, for example, the distribution of subunit numbers. Further analyses are then again (partly) performed without regularization (e.g. joint fitting of multiple cells, V1 data). In particular when discussing the V1 data, where the subunits have very different structure than in the retina, one wonders whether regularization still works in the same way. Also, it is emphasized how the optimal number of subunits can be determined, but some of the subsequent analyses are performed for a fixed number of subunits (e.g. Figure 2 and Figure 3).

There are also several other parts where that information is difficult to extract or missing, which hinders understanding of the material.

The description of the subunit estimation approach via approximate maximum likelihood (subsection “Subunit estimation”) is central to the manuscript but quite difficult to follow. Some terms in the equation are not defined (K and w with superscript 0, c(K,w)), and the explanations for the derivations are cursory or absent. For example, when Equations 1-5 are derived, there is no mentioning of an iterative procedure (this only comes later; at this point, this seems to be only a reformulation of the log-likelihood), but some manipulations and terms here only make sense in the context of an iterative estimation procedure. This needs to be disentangled.

Relatedly, it seems important to spell out how the clustering algorithm (Equations 6-8) solves the maximum likelihood problem, in particular since this connection is central to the manuscript.

The application of the method to V1 data makes an important point regarding the general applicability of the method. This is nice, but only very little analysis is presented. Maybe the authors could at least show how the model performs for different numbers of subunits as in other analyses, to see how well the simple cell and the complex cell are separated in this respect. Also, the effect of regularization would be interesting here.

This assumption of space-time separability needs further discussion and justification. This assumption might be necessary to reduce the number of parameters to manageable levels, but it would be helpful if the authors could offer guidelines for when it might be appropriate.

About the response prediction to naturalistic stimuli. The use of white noise stimuli rather than natural stimuli might provide a good approximation for estimating of subunit filters, However, bipolar cells, which provide inputs to parasol RGCs, are strongly affected by stimulus correlation through gap-junction connectivity generating a nonlinear enhancement of bipolar activity, which could explain the differences found with real activity (Kuo et al., 2016, Manookin et al., 2018). These elements should be included in the Discussion section as one of the potential pitfalls of the approach.

The null-stimulus description indicated in the Results section needs further discussion and justification. This part should be rewritten extracting elements present in the methods. Also, the results are confusing. According to what is presented in Figure 5, the PSTH variance obtained from the white-noise response is larger than the variance of null-stimulus response, and at some extent, this variance would be reflecting inter-trial variability. At this level, this figure leads to confusion because it is not helping to understand the methodology. What is the role of the null-stimulus in this method paper? The method seems to predict the null-stimulus response better, but again, it is not clear how this clarifies the methodology neither provides insights to understand this behavior. It is counter-intuitive the fact that adding more units in the model subunits the response prediction for white-noise stimulus is not improving (Figure 6).

More detailed comments:

The manuscript was first submitted as original research before the submission as a method paper where essential changes in the structure and content were incorporated. Nevertheless, there is still information more related to retina physiology than the methodology description. Besides, if this is a method valid both for retina and V1 neurons, it is important to mention this in the title, where only the retina application is indicated. Therefore, please consider revising the article title.

In the Introduction, the authors claim there is no widely accepted general computation to infer the structure of nonlinear subunits inputs to a neuron. Nevertheless, relevant references have been published in the last years addressing the same problem noted by the authors. For instance, Liu et al., 2017, which appears in the discussion but not in the introduction, proposes a spike-triggered non-negative matrix factorization, to estimate the non-linear subunits conforming the RGC receptive field in salamander retina, where bipolar cells conforming RGCs can be also encountered.

It would be interesting to obtain and include some information about computational runtime.

The presentation of the analysis of the simulated ganglion cell under fine white noise stimulation (Figure 1—figure supplement 1C) is odd. Why are the subunits shown as sets of photoreceptors, not as pixel layouts? Does the method yield 12 subunits as the optimal number, or is this just the result of what came out when enforcing 12 subunits? A better discussion of how the method performs for simulated data could help better understand the strengths and limitations of the approach.

The figures show the "relative strength" of subunits by a blue scale bar. Is this the weight w? Or the norm of the subunit filter? Both seem to be related to "strength". And both seem to be optimized in the second step of the fitting approach along with the output nonlinearity.

Subsection “Estimated subunits are spatially localized and non-overlapping: The text refers to the Materials and methods section for explaining how the temporal filter was obtained, but the Materials and methods section seem to lack information about receptive field and temporal filter estimation.

Subsection “Regularization for spatially localized subunit estimation”: The chosen value of epsilon in the LNL1 regularization should somehow be related to the typical range of weights. Are the latter of order unity so that a value of epsilon=0.01 is small compared to typical weights?

Figure 4E: It seems odd that the negative log-likelihood keeps decreasing with the number of subunits in the joint fitting procedure. Unlike for the separate fitting. Is there a reason for this? Relatedly: how was the total number of subunits constrained for the separate fitting?

Subsection “Regularization for spatially localized subunit estimation”: The text states that a joint model with 15 subunits gives higher prediction accuracy, referring to Figure 4D. Does this relate to predictions as analyzed in Figure 5? Or to the maximum likelihood of Figure 4E?

Subsection “Subunit model explains spatial nonlinearities revealed by null stimulus”: The text refers to "spatial null spaces", but the Materials and methods section relates to spatiotemporal null spaces. Please clarify.

Subsection “Subunit model explains spatial nonlinearities revealed by null stimulus”, fourth paragraph: Maybe I missed it, but I wasn't sure which version of the subunit estimation is meant by "the subunit model". With or without regularization? Fine or coarse stimuli? A specific instance of the different initial conditions? Same for Figure 7.

Figure 7: The figure and the text around it use the term saccade, but the stimulus seems just to be a switch to a new image without a real motion segment between fixations. This is a bit confusing. Also, how the stimulus is segmented into periods around and between image switches should be better explained and not only mentioned in the legend, in particular how this is used to compute the projection on the receptive field (Figure 7C; is this a spatiotemporal projection?). Furthermore, the difference in Figure 7C seems quite subtle. Is it significant?

In the Materials and methods section, maybe state that the spatiotemporal stimulus was binary white noise (not Gaussian) if this is the case and that the Xt signal that goes into the subunit estimation is the contrast signal (zero mean).

Could the authors explain why the weights and the filter magnitudes need to be refitted in the second model fitting step?

Subsection “Application to neural responses”: What does the 5.2 µm boundary refer to?

For the simulated RGC model, the 180 µm (= 180 g.u.) spacing between cones seems large. Is that a typo? Also, in the description, it is not quite clear what the photoreceptor weights are (used for normalizing the firing rate) and how bipolar weights were varied around 10% of their mean (which mean?).

When describing the null stimulus, it would be good to explain where the original stimulus Sw comes from and how the σ for computing the support of the receptive field is obtained.

The references Maherwaranathan et al., 2018, and Shi et al., 2018 are missing.

Figures are in general of poor quality and the color choice misleading. In Figure 2D is not possible to see the black arrows over the blue bars. In Figure 2B blue line is not well visualized.

Figure 5D, use the same bar width for the inset histograms.

"… was highly reproducible across repeats (Figure 6C,D)," -> "… was highly reproducible across repeats (Figure 5C,D),"

Figure 6B: dashed are filled lines are not indicated in the caption.

Subsection "Application to neural response". The last three paragraphs should be incorporated into the Results section.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Inference of Nonlinear Receptive Field Subunits with Spike-Triggered Clustering" for further consideration at eLife. Your revised article has been favorably evaluated by Joshua Gold (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The comparison to the convolutional subunit model is not completely convincing for the following reasons: (1) The comparison done on V1 data uses a restricted version of the convolutional subunit model (the subunit nonlinearity is forced to be an exponential, despite that Vintch et al., (2015) and others have showed that it is often quadratic when learned from data). (2) No comparison is made on the retinal dataset where the fixed exponential subunit nonlinearity probably is a more realistic assumption. The reader is thus left wondering whether the new method truly has better predictive performance than the simpler convolutional subunit model, and whether the main benefit with the new method is that it can fit multiple subunit filters easily. It would be beneficial at least to clarify these concerns by giving a clearer justification to the selected methodology regarding the above issues.

A description for how/why the clustering algorithm's three step procedure solves the likelihood problem is still missing. It would be helpful if the authors could briefly spell out why the three-step prescription subsection “Subunit Estimation” “minimizes the upper bound of the log-likelihood (Equation 5). Are the update rules derived from the partial derivatives of Equation 5? Is this guaranteed to converge and converge to the actual minimum?

Regarding the validation in V1 data: More than a validation, where there is no ground-truth to compare, the results should be focused to validate the model showing that it reproduces neural data better than previous approaches. For instance, Figure 10 compares the resulting subunits obtained by a convolutional model and the model proposed in this article. It is tough to compare both; it should be more useful to see how the two of them reproduce neural response.

The Discussion section requires a new organization. The comparison with the existing models, such as SNMF and V1 data, shouldn't be placed here. The paragraph describing the work of McIntosh et al., 2016 can be better articulated with the rest of the Discussion section.

- For instance, the sentence "Note, however, that a model with two subunits frequently explained ON parasol data more accurately than a model with one subunit, implying that ON cells do have spatial nonlinearities". This is not related to the method validation, and moreover, there is no result to validate this affirmation.

- Subsection “Modeling linear-nonlinear cascades” states that the paper by Jia et al., (2018) applies a non-negativity constraint on the weights instead of the subunit filters. Looking at their methods and sample subunits in the figures, this doesn't seem to be the case.

- For the receptive field estimation in subsection “Application to neural responses”, the pixels with magnitude larger than 2.5 σ probably refer to magnitude **of the STA**; similarly, averaging the time course of pixels probably refers to averaging the pixels **in the STA**.

Figure 2 is still hard for me to follow. Is there a relationship between the grayscale images and the inner subunits? For instance, the subunits sizes go beyond the stimulus resolution, so, is their spatial location reliably estimated? Why level 3 only divides in two the left component, while the right one is still increasing the subunits number? In fact, the authors, in response to reviewers document and the article, indicate that the hierarchical partitioning is not used for the remainder in the paper. If this is not used, why is it introduced?

-Figure 5D. In the inset histograms, please use the same bin-width.

- Figure 6B. In the text, the authors talk about prediction accuracy. Nevertheless, the figure indicates Δ correlation. Same in Figure 7B.

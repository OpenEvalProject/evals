# Peer review - Round 1

Editors:
- Ruben L Gonzalez, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73860.sa0](https://doi.org/10.7554/eLife.73860.sa0)

Using a Bayesian machine learning approach, the authors of this paper have developed a tool for the analysis of single-molecule fluorescence colocalization microscopy images. The authors develop the algorithm, generate an associated software program, and then benchmark the algorithm and software using both simulated and experimental data. The results provide an important, validated tool for use by the single-molecule fluorescence microscopy community.


---

# Peer review - Round 1

Editors:
- Ruben L Gonzalez, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73860.sa1](https://doi.org/10.7554/eLife.73860.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Bayesian machine learning analysis of single-molecule fluorescence colocalization images" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Colin Kinz-Thompson (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The γ-distributed noise model used in Tapqir captures quite a lot of physics and, given the analyses in Figures 3-6, clearly works, but might be limited to certain types of cameras used in the fluorescence microscopy (e.g., EMCCDs). For instance, sCMOS cameras have pixel-dependent amplification and noise profiles, rather than a single gain parameter, and are sometimes approximately modeled as normal distributions with both mean and variance having intensity-dependent and intensity-independent contributions that are different for each pixel on the camera. The authors should therefore address the question of whether Tapqir can also be used with data collected from different cameras and, specifically, sCMOS cameras.

2) Little information is included about the role of AOI selection. The authors should address the question of how precisely do AOI positions need to be determined and how accurate must the mapping be. Moreover, it appears that the authors use a very large AOI (14x14 pixels, page 18). The authors should therefore address what the dependency is of the analysis on the AOI size and the relative sizes of the AOI and diffraction-limited spots. The authors should also address the question of whether Tapqir can only be used on well-separated, non-overlapping AOIs.

3) The authors should test how the strength of the prior on the location of a specific binder affects the performance of Tapqir. Specifically, it would be very informative to know how the performance of Tapqir degrades as this prior is weakened. In other words, the authors should determine how weak this prior be made before the performance of Tapquir is compromised.

4) The premise of Tapqir assumes that there is no significant "dark" population of tethered molecules on the slide. While this may hold true for the commercially synthesized DNA oligos used in the example data in Table 1, many single-molecule experiments involve a large population of dark, tethered molecules due to incomplete labeling (50% is not uncommon). In these cases, the appropriate control for non-specific binding is a separate experiment in which no molecules or control molecules are tethered to the slide surface. The authors should address the question of whether Tapqir be used in these instances.

5) The head-to-head comparison with "spot-picker" is a bit unconvincing--how commonly is spot-picker being used outside the Gelles lab? A head-to-head comparison with the previously published methods developed by Grunwald would be much more revealing--particularly concerning the utility of having event detection probabilities and the time each analysis method takes to run on the same GPU.

6) The authors offer a new approach to analyzing single-molecule fluorescence colocalization data, yet they don't leverage the full strength of priors in stringing together experiments. Specifically, in their analyses, they mostly end up in a place where their software is recapitulating old analyses and not really leveraging the probabilities they have. The authors, therefore, need to make a clearer case for using the calculated event probabilities. In addition, if they made a subjective decision about what probability cut off to use to identify events for inclusion in the kinetic modeling then that seems to go counter to the objective-based analysis of Tapqir. Can the kinetic modeling include all of the events, weighted by their probabilities?

7) The authors should also respond to the additional concerns raised by the individual reviewers, included below.

Reviewer #1 (Public Review):

"Bayesian machine learning analysis of single-molecule fluorescence colocalization images" by Ordabayev, et al. reports the development, benchmarking, and testing of a Bayesian machine learning-based method, which the authors name Tapqir, for analyzing single-molecule fluorescence colocalization data. Unlike currently available, more conventional analysis methods, Tapqir attempts to holistically model the microscopy images that are recorded during a colocalization experiment. Tapir uses a physics-based, global model with parameters describing all of the features of the experiment that are expected to contribute to the recorded microscopy images, including shot noise of the spots and background, camera noise, size and shape of the spots, and specific- and non-specific binders. Based on benchmarking on simulated data with widely varying properties (e.g., signal-to-noise; amounts, rates, and locations of specific and non-specific binders; etc.), Tapqir generally does as well and, in some cases, better than currently existing methods. The authors also test Tapqir on real microscopy images with similarly varying properties from studies that have been previously published by their research group and demonstrate that their Tapqir-based analysis is able to faithfully reproduce the previously published results, which were obtained using the more conventional analysis methods available at the time the data were originally published. This is a well-designed and executed study, Tapqir represents a conceptual and practical advance in the analysis of single-molecule fluorescence colocalization experiments, and its performance has been comprehensively and rigorously benchmarked on simulated data and tested on real data. The conclusions of this study are well supported by the data, but some of the limitations of the method need to be clarified and discussed in more depth, as outlined below.

1. Given that the AOI is centered at the target molecule and there is a strong prior for the binder also being located at the center of the AOI, the performance of Tapqir is dependent on several variables of the microscopy/optical system (e.g., the microscope point-spread function, magnification, accurate alignment of target and binder imaging channels, accurate drift correction, etc.). Although this caveat is mentioned and some of these factors are listed in the main text of the manuscript, the authors could have expanded this discussion in order to clarify the extent to which the performance of Tapqir depends on these factors.

2. The Tapqir model has many parameters, each with its own prior. The majority of these priors are designed to be uninformative and/or weak and the only very strong prior is the probability that a specific binder is located at or very near the center of the AOI. The authors could have tested and commented on how the strength of the prior on the location of a specific binder affects the performance of Tapqir.

3. Given the priors and variational parameters they report, the authors show that Tapqir performs robustly and seems to require no experiment-to-experiment optimization. This is expected to be the case for the simulated data, since they were simulated using the same model that Tapqir uses to perform the analysis. With regard to the real data, however, it is quite likely that this is due to the fact that the analyzed data all come from the same laboratory and, therefore, likely the same microscope(s). It would have therefore been very useful if the authors would have listed and discussed which microscope settings, experimental conditions, and/or other considerations, beyond those described in point 1 above, would result in a need for re-optimization of the priors and/or variational parameters.

4. Based on analysis of the simulated data shown in Figure 5, where the ground truth is known, the use of Tapqir to infer kinetics is less accurate that the use of Tapqir to infer equilibrium binding constants. The authors do a great job of discussing possible reasons for this. In the case of the real data analyzed in Figure 6 and in Figure 6 —figure supplements 1 and 2, the kinetic results obtained using Tapqir have different means and generally larger error bars than those obtained using Spot-Picker. To more comprehensively assess the performance of Tapqir versus Spot-Picker, the authors could have used the association and dissociation rates to calculate the corresponding equilibrium binding constants and then compared these kinetically calculated equilibrium binding constants to the population-calculated equilibrium binding constants that the authors calculate and report in the bottom plot in Panel D of Figure 6 and Figure 6 —figure supplements 1 and 2. This would provide some information on the accuracy of the kinetics in that the closer the kinetically and population-calculated equilibrium binding constants are to each other, the more accurately the kinetics have been estimated. Performing this type of analysis for the kinetics obtained using Tapqir and Spot-Picker would have allowed a more comprehensive comparison of the two methods.

Reviewer #1 (Recommendations for the authors):

This is a well-designed and executed study, Tapqir represents a conceptual and practical advance in the analysis of single-molecule fluorescence colocalization experiments, and its performance has been comprehensively and rigorously benchmarked on simulated data and tested on real data. Moreover, the conclusions of this study are well supported by the data. Given all of this, I would recommend publication of this study as a Tools and Resources article in eLife, assuming that the authors address the weaknesses I identified in my Public Review as well as the following extensions of those weaknesses.

1. I think the authors should to expand the discussion of how the performance of Tapqir depends on the microscope point-spread function, magnification, accurate alignment of target and binder imaging channels, accurate drift correction, etc. Specifically, if possible, they should describe how a 1-2 pixel offset in the x- or y dimensions between the target and binder imaging channels arising from differences in any of these parameters would affect the performance of Tapqir. This is especially important given the strength of the prior the authors have assigned to the location of the specific binder at the center of the AOI.

2. The authors should list and discuss what microscope settings, experimental conditions, and/or other considerations, beyond the microscope/optical described in point 1 above, would result in a need for re-optimization of the priors and/or variational parameters. For example, in Lines 509-510, the authors state that most microscopes used for colocalization experiments are set up such that diffraction-limited spots occupy 1-2 pixels in the x- and y dimensions on the camera detector. If a microscope is instead set up to spread the spot over 3, 4, or more pixels in each dimension, are there any priors or variational parameters that should be re-optimized? Are there any other such considerations?

4. The authors should comment on whether the kinetic parameters obtained by Tapqir and reported in Figure 6 and in Figure 6 —figure supplements 1 and 2 are actually more accurate and/or precise than those obtained by Spot-Picker. For example, if the association and dissociation rates were used to calculate the equilibrium binding constants, how would these kinetically calculated equilibrium binding constants compare to the population-calculated equilibrium constant that the authors calculate and report in Figure 6 and in Figure 6 —figure supplements 1 and 2? Are the kinetically calculated and population-calculated equilibrium binding constants in closer agreement for the Tapqir-analyzed data versus the Spot-Picker-analyzed data? If one is better than the other, why do the authors think that is?

Reviewer 2 (Public Review):

The work by Ordabayev et al. details a Bayesian inference-based data analysis method for colocalization single molecule spectroscopy (CoSMoS) experiments used to investigate biochemical and biophysical mechanisms. By using this probabilistic framework, their method is able to quantify the colocalization probabilities for individual molecules while accounting for the uncertainty in individual binding events, and accounting for camera and optical noise and even non-specific binding. The software implementation of this method, called Tapqir, uses a Python-based probabilistic programming language (PPL) called pyro to automate and speed-up the optimization of a variational Bayes approximation to the posterior probability distribution. Overall, Tapqir is a powerful new way to analyze CoSMoS data.

Tapqir works by analyzing small regions (14x14 pixels) of fluorescence microscopy images surrounding previously identified areas of interest (AOI). The collection of images of these AOIs through time are then analyzed collectively using a probabilistic model that accounts for each time frame of each AOI and is able to determine whether up to K "binders" (K=2 here) are present and which of them is specifically bound. This approach of directly modeling the contents of the image data is relatively novel, and few other examples exist. The details of the probabilistic model used incorporate an impressive amount of physical insight (e.g., camera gain) without overparameterization.

The γ-distributed noise model used in Tapqir captures quite a lot of physics and, given the analyses in Figures 3-6, clearly works, but might be limited to certain types of cameras used in the fluorescence microscopy (e.g., EMCCDs). For instance, sCMOS cameras have pixel-dependent amplification and noise profiles, rather than a single gain parameter, and are sometimes approximately modeled as normal distributions with both mean and variance having an intensity-dependent and independent contribution that is different for each pixel on the camera. It is unclear how Tapqir performs on different cameras.

The variational Bayes solution used by Tapqir provides many computational benefits, such as numerical tractability using pyro and speed. It is possible that the exact posterior, e.g., as obtained using a Markov chain Monte Carlo method, would be insignificantly different with the amount of data typical for CoSMoS experiments; however, this difference is not explored in the current work.

The intrinsic use of prior probability distributions in any Bayesian inference algorithm is extremely powerful, and in Tapqir offers the opportunity to "chain together" subsequent analyses by using the marginalized posteriors from one experiment as the basis for the priors for subsequent experiments (e.g., in \σ^{xy}) for extremely high accuracy inference. While the manuscript discusses setting and leveraging the power of priors, it does not explore the power of such "chaining" and the positive effects upon accuracy.

A significant number of CoSMoS experiments use multiple, distinct color fluorophores to probe the colocalization of different species to the target. The current work focuses only upon analyzing data with a single color-channel. Extensions to multiple independent wavelengths are computationally trivial, given the automated variational inference ability of PPLs such as pyro, and would increase the impact of the work in the field.

Tapqir analysis provides time series of the probability of a specific binding event, p(specific), for each target analyzed (c.f., Figure 5B), and kinetic parameters are extracted from these time series using secondary analyses that are distinct from Tapqir itself.

The method reported here is well designed, sound, and its utility is well supported by the analyses of simulated and experimental data sets reported here. Tapqir is a cutting-edge image analysis approach, and its proper treatment of the uncertainty inherent to CoSMoS experiments will certainly make an impact upon the analysis of CoSMoS data. However, many of the (necessary) assumptions about the data (e.g., fluorescence microscopy) and desired information (e.g., off-target vs on-target binding) are quite specific to CoSMoS experiments and therefore limit the direct applicability of Tapqir for the analysis of other single-molecule microscopy techniques. With that in mind, the direct Bayesian inference-based analysis of image data, as opposed to integrated time series, as demonstrated here is very powerful, and may encourage and inspire related methods to be developed.

Reviewer #2 (Recommendations for the authors):

– Some of the language in the introduction is a little imprecise (e.g., "binders", "green RNA", "blue DNA spot", "integrating binder fluorescence", "real fluorescent spots"), and could be more explicit to improve clarity.

– Line 63: The concentration barrier could be described more in depth for the eLife readership.

– Line 74-76: Additional description of these effects, perhaps mathematically or through other citations, would help the readers understand the fundamental differences between analyzing image data and intensity data.

– Line 82-83: Describing how and/or the magnitude of the failure that not accounting for spot confidence creates would be useful for the reader to understand the requirement for Tapqir

– Line 84-86: The method described doesn't get a name, but the software does get a name. I think giving the method a descriptive name (e.g., an acronym) would help clarify the discussion and distinction between the approach of probabilistic modeling of the data and using pyro and the chosen priors etc. to do so.

– More referencing of Bayesian image analysis methods for microscopy data, at least in the introduction, (e.g., Bayesian Analysis of Blinking and Bleaching (B3), maybe some super-resolution methods, etc.) would help create the appropriate context for Tapqir.

– A discussion of the benefits of variational as opposed to exact inference is missing and would be useful for the reader.

– Line ~139: It is unclear if the image models or PSFs are integrated over pixel boundaries (i.e., as in Smith et al., "Fast, single-molecule localization that achieves theoretically minimum uncertainty" DOI: 10.1038/nmeth.1449). If not, what effect does this have on the modeling?

– Line 155-161: A discussion of EMCCD versus sCMOS noise differences, or even which one is more applicable to Tapqir, would be helpful here.

– Line 181: It is unclear what the "hierarchichal Bayesian analysis" refers to. I could not find an explanation in the Methods.

– Figure 3: What is the criteria for not having {x,y,h} included on the plot (e.g., at t=101)? I could not find it. Maybe p(m=0)>.5?

– Figure 3: This figure should also include w along with x,y, and h. Is it relatively constant? Does it vary quite a bit?

– Figure 3-supplement 1 A: It was unclear to me why at frame 103, the spot was detected as spot 2 and not spot 1 with equal probability. Isn't there a degeneracy between the two spots? Is this broken by \theta? Regardless of the answer, perhaps a more in-depth discussion of this point would be useful.

– Figure 3-supplement 3 D: How does this plot compare to the theoretical minimum uncertainty of localizing a single molecule (i.e., the Cramer-Rao lower bound) at these photon fluxes? Shouldn't it bottom out at some point?

– Line 214: "… rich enough to accurately capture …" is a very nice way to convey the utility of the model. I think you should use it more often.

– Figure 5C-E: the rate constants are systematically overestimated -- even at the slowest rates. Why? Might these rates constants actually transition probabilities? I did not see a k=-ln(1-P)/dt equation in the Methods section.

– Line 353: Generally, Tapqir is only quantitatively compared to spot-picker, when there is also the Carlas et al., method that could be used for comparison.

– Figure 6B and supplements: Why were no off target controls ever analyzed to be included in the plot B as the yellow curve in C. If nothing else, it would be very useful to show the Tapqir is very accurate.

– Table 1: The computation times are reasonable for a high quality analysis, but are done on a very fast desktop computer (Threadripper with a 2080). It would be useful to show the performance on a less powerful computer as well (e.g., a low-powered laptop) for a least one dataset or perhaps a partial dataset. That way, potential users can judge whether they need to seek out better computational resources before trying Tapqir.

Reviewer #3 (Public Review):

In this manuscript, the authors seek to improve the reproducibility and eliminate sources of bias in the analysis of single molecule colocalization fluorescence data. These types of data (i.e., CoSMoS data) have been obtained from a number of diverse biological systems and represent unique challenges for data analysis in comparison with smFRET. A key source of bias is what constitutes a binding event and if those events are colocalized or not with a surface-tethered molecule of interest. To solve these issues, the authors propose a Bayesian-based method in which each image is analyzed individually and locally around areas of interest (AOIs) identified from the surface tethered molecules. A strength of the research is that the approach eliminates many sources of bias (i.e., thresholding) in analysis, models realistic image features (noise), can be automated and carried out by novice users "hands-free", and returns a probability score for each event. The performance of the method is superb under a number of conditions and with varying levels of signal-to-noise. The analysis on a GPU is fairly quick-overnight-in comparison with by-hand analysis of the traces which can take days or longer. Tapqir has the potential to be the go-to software package for analysis of single molecule colocalization data.

The weaknesses of this work involve concerns about the approach and its usefulness to the single-molecule community at large as wells as a lack of information about how users implement and use the Tapqir software. For the first item, there are a number of common scenarios encountered in colocalization analysis that may exclude use of Tapqir including use of CMOS rather than EM-CCD cameras, significant numbers of tethered molecules on the surface that are dark/non-fluorescent, a high density/overlapping of AOIs, and cases where event intensity information is critical (i.e., FRET detection or sequential binding and simultaneous occupancy of multiple fluorescent molecules at the same AOI). In its current form, the use of Tapqir may be limited to only certain scenarios with data acquired by certain types of instruments.

Second, for adoption by non-expert users information is missing in the main text about practical aspects of using the Tapqir software including a description of inputs/outputs, the GUI (I believe Taqpir runs at the command line but the output is in a GUI), and if Tapqir integrates the kinetic modeling or not. Given that a competing approach has already been published by the Grunwald lab, it would be useful to compare these methods directly in both their accuracy, usefulness of the outputs, and calculation times. Along these lines, the utility of calculating event probability statistics (Figure 6A) is not well fleshed-out. This is a key distinguishing feature between Tapqir and methods previously published by Grunwald et al. In the case of Tapqir, the probability outputs are not used to their fullest in the determination of kinetic parameters. Rather a subjective probability threshold is chosen for what events to include. This may introduce bias and degrade the objective Tapqir pipeline used to identify these same events.

Finally, the manuscript could be improved by clearly distinguishing between the fundamental approach of Bayesian image analysis from the Tapqir software that would be used to carry this out. A section devoted to describing the Tapqir interface and the inputs/outputs would be valuable. In the manuscript's current form, the lack of information on the interface along with the potential requirement for a GPU and need for the use of a relatively new programming language (Pyro) may hamper adoption and interest in colocalization methods by general audiences.

Reviewer #3 (Recommendations for the authors):

1. It is unclear if intensity information is used by Tapqir or if it can be used. This can be useful for including more priors about the experiment (i.e., "real" events would be above a certain threshold due to FRET or presence of multiple fluorophores) or for using Tapqir to analyze experiments in which multiple fluorophore-labeled molecules bind simultaneously and sequentially to the same AOI. As presented, it would seem that Tapqir is "blind" to these types of multiple binding events.

2. A concern for adoption of Tapqir and appreciation of this work by general audiences involves the presentation of the method and software. I think that these should be disentangled from one another and that Tapqir should only be used to refer to the software used to carry out this approach. The manuscript, and the colocalization field, may be better served if a section were included that explicitly describes how to use Tapqir to implement this analysis including the necessary inputs, hardware (how much time would this take if a GPU isn't used?), and outputs/GUI. Ultimately, Tapqir needs to be user-friendly to be adopted and the requirement for a GPU and the Pyro programming language may be significant barriers. A potential model for the authors to consider is the eLife paper describing cisTEM software (https://elifesciences.org/articles/35383) that efficiently describes both the process, benchmarking, and software/user experience.

3. With respect to inputs, the need for use of imscroll to identify AOIs, drift correct, and carry out mapping should be clarified. Is imscroll output essential for Tapqir input?

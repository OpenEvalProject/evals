# Peer review - Round 1

Editors:
- David E James, https://ror.org/0384j8v12 University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85755.sa0](https://doi.org/10.7554/eLife.85755.sa0)

This study presents a valuable finding on the precision conferred by dynamical interpretation of morphogen gradients. The evidence supporting the claims of the authors is convincing, with compelling theoretical analysis and solid experimental data. The authors have adequately addressed most concerns raised and so the work will be of considerable interest to the developmental biology and developmental systems biology communities.


---

# Peer review - Round 1

Editors:
- David E James, https://ror.org/0384j8v12 University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85755.sa1](https://doi.org/10.7554/eLife.85755.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Dynamic readout of the Hh gradient in the Drosophila wing disc reveals pattern-specific tradeoffs between robustness and precision" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by David James as the Senior and Reviewing Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While your manuscript was deemed of interest there were significant shortcomings identified that need to be addressed. Most notably both referees felt the experimental part was less compelling than the modelling part and in fact, one referee indicated that they felt this was at best an incremental advance over previous findings. We would like to provide you with an opportunity to address these serious concerns as both reviewers did see positive aspects of the study. However, it is critical that you address the issue concerning the nature of the advance compared to previous studies before we can proceed.

The reviewer found this study presents at best incremental advances to the field. It doesn't provide substantial progress conceptually or experimentally from Eldar et al., 2003, Adleman et al., 2022 and particularly Nahmad and Stathopoulos, 2009. The experimental data and interpretation appear to lack the rigor needed to challenge the model predictions.

Reviewer #1 (Recommendations for the authors):

The manuscript presents an elegant theoretical analysis of robustness and precision in morphogen ingredients, focusing on hedgehog signaling. I have found the proposal made by the authors interesting and convincing. However, I have found that some parts of the manuscript are not very clear. In addition, I believe the experimental results need to be improved in their presentation and to be broadened in scope if possible. Here below I detail my comments:

1) In the Introduction, paragraph starting at 75 indicates the properties of Hh signaling as if they were disconnected to the features described in the previous paragraph. Please, rewrite it to make all appropriate connections with the previous paragraph.

2) Clarify how robustness is exactly defined. The displacement of the boundary of the pattern upon perturbation of Hh level is used in Figure 1 to say whether a target is more robust. However, the coefficient of robustness is not defined as such displacement. These different definitions should be related and preferably refer to them with different names. In addition, the meaning of m in the definition of the coefficient of robustness is not totally clear to me. A plot depicting it would help. Is m the slope of the non-perturbed gradient at the threshold?

3) The coefficient of robustness used is a different measure of the Robustness introduced by Eldar et al.2003. The latter one considered the displacement upon perturbation relative to the extent of the unperturbed gradient. Why the authors do not use the definition of robustness introduced by Eldar et al? Why the definition of robustness in this manuscript does not take into account whether the gradient spans over a larger or a smaller spatial region? The overshoot gradient produces larger displacements yet it is a gradient spanning a larger domain than the steady-state gradient. I am not sure whether the over-shoot gradient is less robust than the steady gradient if the definition of robustness introduced by Eldar et al. 2003 is used. Please justify and clarify all this.

4) These differences in definitions (point 3) make the comparison of the analysis in Box2 with the results from Eldar et al.2003, described in lines 168-169, awkward. Box 2 analyses exponential gradients. It compares the robustness of two exponential gradients with different spatial characteristic lengths (λ). Based on the definition of the coefficient of robustness of this manuscript, these two exponential gradients have a different robustness. However, if we use the definition of robustness by Eldar et al. 2003, all exponential gradients have the same robustness, R=1, independently of their characteristic length λ. Please clarify.

5) In the text, at the beginning of section 2.3, state more explicitly the concept of precision.

6) Define mathematically how precision is measured. The text refers to Box2 (line 187) but there is no definition of coefficient of precision in that Box (nowhere else either).

7) As far as I understand, precision is related to how fluctuations (noise) on the amount of morphogen impact on the position of the boundary. These fluctuations can be from cell to cell and over time within the same cell. The current manuscript does not model fluctuations or noise. Instead, it uses the slope of the deterministic gradient to define the precision (lines 188-190, using Figure 2A to visualize this idea). The manuscript would benefit from indicating the assumptions behind this claim :

A) It assumes uniform noise, i.e. that noise/fluctuations are independent of the slope of the gradient, in other words, are of the same amplitude at any spatial position. Indeed, what we may expect is not this, since intrinsic noise is proportional to the square root of the number of molecules. Hence, the fluctuations will be larger where the morphogen is in high amounts than where it is in low amounts.

B) It also assumes that the range of Hh concentrations that are not discernible/distinguishable under fluctuations (i.e the widths of the red and green bands in the Hh axis) is independent of the Hh concentration (i.e the width of the red band is located around Hh=0.1 and has the same width as that of the green band which is located at Hh=0.77), and that this range does not change over time (it is the same for the steady and the overshoot gradients).

8) The "Dynamical interpretation" model is used with two (related) different meanings, in my opinion, and this drives confusion. On the one hand, according to Figure 1A',B',C', the Dynamical interpretation model corresponds to a single threshold used by different targets: one uses it in the steady gradient and the other target uses it in the overshoot gradient. On the other hand, in the text, in line 198, the dynamic interpretation is used only to refer to the overshoot gradient. I suggest revising how "dynamical interpretation" is used: whether it applies only to the overshoot gradient and then whether a different name must be used to the whole framework of single-threshold interpretation.

9) The results assume that Dpp and col use the same threshold. This is supported by Nahmad and Stathopoulos 2009. Which threshold value is used? Which value is used for the simulations with different sets of the parameter values?

10) Why Robustness is not analysed for the Signal (x)? I would expect that the target is activated by the Signal and not directly by the morphogen gradient. Hence it is valuable to analyse the robustness in the signal and to add these results. Perhaps Figure 3A-C already compute the magnitudes from the signal profile (and not from the morphogen Hh(x) profile), but it is unclear from the main text and figure caption.

11) In Figure 3 precision is much less analyzed than robustness. I suggest that the type of analysis already done in Figure 3B and C for robustness is also done for precision. These analyses will show whether the conclusions on precision are maintained for different parameter values. By the way, "parameters are varied between 0,5 and 2 of the reported values" means that they are varied between 0,5 and 2 TIMES the reported values? Perhaps is standard but the meaning of the sentence was unclear to me.

12) How the overshoot gradient is identified for the different set of parameters to compute Figure 3B?

13) I suggest computing Figure 4B for the overshoot gradient and therefore show that the trend in Figure 4A is kept for different parameter values.

14) Figures 5-6 should be improved by adding: Scale bars, magnifications of images, and detail at cell resolution to observe the displacements in terms of cell length scales. What is exactly measured should be also depicted: How the width is measured and which width is measured for the blurry boundary of Dpp? Which is the number of samples?

15) The finding that the robustness of Col depends on Ptc regulation supports the results by Eldar et al. 2003 and that Col is a target of the steady gradient. Hence these new experimental results support proposals made in previous papers. In my opinion, this experimental result in this manuscript (section 2.7) is not very relevant since it validates previous proposals but not the new ones from this manuscript.

16) The manuscript indicates that Dpp is less robust but more precise than it would be if it was specified by the steady-state gradient. Since the authors have analysed the case of non-regulated patch, I suggest addressing how Dpp would change when patched is not regulated, and to address it both theoretically, and if possible, experimentally. If Patched is not regulated, then there will not be an overshoot gradient and Dpp should be as robust as col. Is this indeed the theoretical prediction? And experimentally: what is observed? In addition, will precision become worse or better? What is the prediction from the model when patch is not regulated?

Reviewer #2 (Recommendations for the authors):

Figure 5 – elaborate on how exactly the results are consistent with the model predictions? While the Dpp width changes more, the width is also larger to begin with- taking into account these rather small changes, can a much simpler model with noise explain the experimental results already (does one have to resort to overshoot and dynamic interpretation?)

Width panels: individual data points should be shown, with "n" defined in the legends

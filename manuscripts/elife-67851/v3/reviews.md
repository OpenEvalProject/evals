# Peer review - Round 1

Editors:
- Fred Rieke, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67851.sa1](https://doi.org/10.7554/eLife.67851.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper compares the properties of UV cone output synapses in different regions of the zebrafish retina using a combination of electron microscopy, quantitative imaging and computational modeling. These differences are related to ultrastructural differences in synaptic ribbons and evaluated using a previously-developed biophysical model for the operation of the synapse. The finding of regional differences in ribbon behavior is novel and suggests an under-appreciated degree of control of release by ribbon structure and behavior. A further nice feature of the work is that the model developed is made publicly available in an easy-to-use form.

Decision letter after peer review:

Thank you for submitting your article "Eye-Region Specific Ribbon Tuning Supports Distinct Modes of Synaptic Transmission in Same-Type Cone-Photoreceptors" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Fred Rieke as Reviewing Editor and Reviewer #1, and has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Wei Li (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The reviewers agreed that the central question in the paper was broadly interesting and were impressed by the array of approaches used in the work. Several outstanding issues came up in review, however, that need to be strengthened before we can consider the paper further. All three reviewers agreed that these were necessary revisions.

Essential revisions:

1. Description of preprocessing steps. The imaging data went through several steps of processing before being compared across retinal regions. More controls are needed to build confidence that this initial processing did not introduce artifacts into the data – such as baseline shifts.

2. Calcium imaging data. The calcium measurements are noisy, and it is difficult to have confidence in the conclusion that calcium changes are similar across retinal regions. It would enhance the paper considerably if this data set could be strengthened.

3. Description of model. The connection between the model and the physiological data is hard to follow. It is important to clearly delineate what is learned from the model – including areas in which the model disagrees with experiment.

Reviewer #1 (Recommendations for the authors):

In a few cases non-statistically-significant trends in the data are noted (e.g. lines 206-207, 422-423). I have never found such statements helpful as it is not clear what to make of them. My preference would be to remove them.

It would be helpful to include axis labels on each plot – e.g. the probability distributions in Figure 4e.

Lines 288-290: this is not clear – can you explain how this works in a few extra sentences?

Line 386: what is "calcium T"? It seems quite long for a time constant defining the calcium dynamics.

Reviewer #3 (Recommendations for the authors ):

Specific questions and recommendations for the authors:

1. It will be helpful to have a retina diagram indicating the locations of three different regions.

2. Figure 1 d,e,f (and other figure panels in general) there is no need to mark n.s. On the other hand, in the Statistical Analysis section, GAMs models are mentioned only for Figure 1g, but not other results – needs a clarification.

3. Figure 1h is quite confusing, with a mixture of 3D and 2D plot, schematic drawing and statistical marks. What comparisons are these marks for? The legend is not specific and the Suppl Figure S1 doesn't clarify much.

4. It will be good to discuss the properties of the calcium sensor. Deconvolution of the calcium signal (lines 617-619) notwithstanding, presumably, the sensor has neither the temporal nor spatial resolution to catch the nano-domain calcium peak near the vesicles in RRP, which is critical for the release of RRP.

5. Likewise, the kinetics of iGluSnFR and of glutamate concentration in the cleft. Admittedly, Figures2a, 3c etc. show that the glutamate signal drops rapidly following the transition from dark to light, however, the rates of vesicle pool replenishment are a topic in the field-some discussion of how glutamate clearance from the cleft and the kinetics of the sensor will influence your estimates of replenishment rates would help future readers better interpret your findings in the context of their own observations.

6. In Figure 2d, the rising phase kinetics of the Glu for that nasal cone is strikingly different from that of the acute zone cone. However, such difference is not seen in Figure 3. Therefore, the one in Figure 2d may not be a good representation?

7. In Figure 3a, c.u. and v.u. (only defined in Figure 4 in the context of the model) were used here but not S.D. as in Figure 2, any explanation?

8. Lines 186-188, how were traces "normalized with respect to the UV-bright stimulus periods"?

9. Lines 194-195, "In addition, the glutamate release baseline of AZ UV-cones was increased during 50% contrast at the start of the stimulus" – it is unclear whether higher glutamate baseline occurred during the adaptation step (i.e. it increased during that period) or said increase was the level during adaptation compared to that during bright periods?

10. Lines 219-220, "a sigmoidal non-linearity with slope k and offset x0 which drives the final release" – this sentence is not clear, needs to clarify that it is referring to the relationship between calcium and release.

11. Lines 230-232, "x0 can be understood as the inverted calcium baseline (see Methods)" – Methods don't cover this point, though it is described in the f(Ca) equation, but it isn't obvious how x0 should be the inverted baseline, as if Ca=x0, f(Ca) = 0.5 (i.e., the point of half-release probability). Please clarify this. In general, there are places where explanations of model found in methods don't match those described in the main text (also see some of the points below). Please go over carefully to ensure consistency.

12. Figure 4e suggests a 5-10 times difference in RRP size between acute zone and nasal UV cones, which is not in line with the anatomical data (Figure 1h). Some discussions and clarifications will be helpful.

13. From Figure 4h, and Figure S3 b,c, the linear model doesn't look too bad (unless I misunderstand the figure panels, which are not explained in great detail). The explanation in lines 272-274 needs some work to make it clearer.

14. Sobol indices and their explanation are lacking. Are they computed using ca2+ and glutamate signals, or just glutamate? It is hard to parse their relative "contributions" to model behavior as described in the text, when the methods caution against interpreting this analysis as determining the "importance" of parameters (lines 805-806).

15. The sensitivity analysis suggests that vesicle transitions are more important than pool sizes or their calcium dependence. Thus, it appears that one intuition from the model is that ribbon size – the main anatomical difference of the UV cone ribbons from different regions – is not very important for the functional difference observed (also see discussion in lines 438-439). Although, it has been discussed that ribbon size does not necessarily correlate with IP or RRP size, but this appears to be the hallmark of the acute zone.

16. Lines 460-461, intuitively, a slower RRP refill rate will result in more transient response – after the depletion of RRP, less refilled vesicles to give the sustained component of the response. This is the opposite of what model predicted (a faster RRP). Some explanation and discussion will be helpful.

17. Also, the model simplifies vesicle transition rates by removing their calcium dependence. The Methods section indicates that this choice resulted from early fitting results that essentially "dialed out" the calcium dependence. Given the relative freedom that the model seems to have in finding suitable solutions, how is the lack of calcium dependence justified, and what potential impact might it have on the modeling results?

18. Lines 503-508, "In combination with the approximately equal and opposite effects of calcium baseline on the detectability of On- and Off-events (Figure 7b,f), this suggest(s) that the calcium baseline may present a key variable that enables ribbons to trade-off the transmission of high frequency stimuli against providing an approximately balanced On- and Off- response behaviour." – what will be the physiological relevance for such conditions, perhaps the level of adaptation? Any existing data or predictions?

19. I am slightly skeptical of the predictions that the model might make about the ribbon's frequency tuning (Figure 7) in light of the fact that the AZ model in particular seems unable to reliably capture the fast transient response to dark flashes (Figure 4 c,f).

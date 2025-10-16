# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/04xeg9z08 National Institute of Mental Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85812.sa0](https://doi.org/10.7554/eLife.85812.sa0)

This important study presents a simulator for prosthetic vision (with open source code) whose design is informed by previous psychophysical and neuroanatomical work. The simulation is convincing and demonstrates significant improvements over past visual prosthesis simulations. This work will be of interest to those investigating the impact of cortical stimulation on perception, particularly those developing visual prostheses.


---

# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/04xeg9z08 National Institute of Mental Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85812.sa1](https://doi.org/10.7554/eLife.85812.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Biologically plausible phosphene simulation for the differentiable optimization of visual cortical prostheses" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Chris Baker as the Reviewing Editor/Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michael P Barry (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers all think the work has great potential and will be useful to the field, but also highlight a number of major limitations. These are all laid out clearly in their individual comments (below).

In a revision, we would like to see the modeling work extended with a clear acknowledgement of some of the limitations. In particular, a revision should address concerns about:

1) Model validation with quantitative approaches.

2) Cortical folding.

3) Phosphene mapping.

4) Multiple electrode stimulation and electrode interactions.

We anticipate this will require substantial revisions to the modeling and the manuscript and not just a discussion of these issues.

Reviewer #1 (Recommendations for the authors):

The authors should clarify which data was used to fit the model and which data was used to test its predictive ability. As presented, it appears to be more of a descriptive "one size fits all" model than a predictive one that could be used to generalize to new patients and data. To that end, the paper should also make an effort to evaluate the model more thoroughly and more quantitatively.

The paper claims that based on CORTIVIS results, phosphenes are Gaussian blobs. However, this is true only for single-electrode percepts. Ref. 6 clearly states that multi-electrode stimulation does not produce a linear summation of Gaussian blobs. This is therefore quite a strong assumption of the model that needs to be clearly stated and discussed – it makes it unlikely that the results presented in Figure 8 would translate to real patients.

It is puzzling to me that the paper would place such an emphasis on the regularization loss, which was thought to promote "subjective interpretability", but then use a relative weighting of 0.999 for the reconstruction loss and only 0.001 for regularization. I suspect the low weight has to do with training instabilities, but with a relative weight of 0.001 it is hard to argue that this term had any influence on the results at all.

Reviewer #3 (Recommendations for the authors):

– The mapping algorithm for visual field to the cortical surface ignores cortical folding

– It appears the stimulation models also do not take cortical folding into account

– Given the authors' previous report in JoV, 2022, it isn't clear how much of this paper is an advance.

– While the authors repeatedly describe the advances that an end-to-end mode confers, the practicality of such a system is not discussed. In particular, end-to-end optimization can only demonstrate that the critical intermediate representation -- the phosphene brightnesses over time -- retains sufficient information for decoding an approximation of the original image. It says little about the hypothetical implant recipient's ability to extract that information into a usable percept.

– Figure 3 -- the dashed lines are difficult to visually parse.

– The simulator appears to assume perfect knowledge of phosphene location in the visual field; this assumption is implausible

– Some of the claims for performance are questionable: 10,000 phosphenes on an image of 64x64 pixels is not a reasonable assessment.

– Speed is good, but requires substantial hardware to achieve the claimed performance. Other, similar simulations from the literature report as-good or better performance without a multi-thousand dollar GPU. Although the published simulations do not include as detailed models as included here, the substantial difference gives one pause.

– Focusing on cortical stimulation leaves a significant portion of the literature unexplored, an unreasonable narrowing as the majority of simulation literature is fundamentally agnostic as to the targeted brain area, or at least adaptable to different areas with minimal effort, a claim that the authors here also make of their system.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Towards biologically plausible phosphene simulation for the differentiable optimization of visual cortical prostheses" for further consideration by eLife. Your revised article has been evaluated by Chris Baker as Senior and Reviewing Editor.

The revised manuscript was re-evaluated by two of the initial reviewers. While the manuscript has been improved there are some remaining issues that need to be addressed, as outlined below:

Reviewer #3 (Recommendations for the authors):

Thank you for updating the manuscript and further demonstrating the capabilities of your simulator. The manuscript would be improved by addressing the below issues:

1) Overall, the manuscript should focus more on simulator demonstrations that reflect existing visual prosthetic technology, instead of highlighting examples with hundreds or thousands of noninteracting phosphenes in Figures 1 and 6-8. Examples using 10-60 phosphenes with nontrivial interactions should be prominent in the main manuscript. Even when only considering available channels, Fernández et al.'s system, as tested, could only stimulate up to 16 channels simultaneously, and the Orion device only has 60 channels. The ability to optimize hundreds of independent phosphenes will be very important in the future when devices are shown to be able to create that many phosphenes simultaneously. Until the field reaches that point, however, emphasizing examples with such large collections of phosphenes encourages misconceptions regarding the capabilities and existing challenges of visual prostheses.

2) The authors provide nice examples of how nonlinear interactions between single-electrode phosphenes can be rendered in Figure 1—figure supplement 3. While this is a nice demonstration, the authors should put more emphasis on this capability of the simulator. Alongside the end-to-end demonstrations of how the simulator performs assuming independent electrodes and phosphenes, the authors should include at least one end-to-end demonstration of how the simulator performs assuming nontrivial nonlinearities with fewer than 60 phosphenes. If such constraints appear to eliminate the meaningful utility of the simulator and its optimization process, the authors should thoroughly discuss this issue.

3) This simulator attempts to take numerous biological factors into account to translate electrode locations and stimulation parameters into simulated phosphenes, but also offers many points at which users can make manual adjustments. As the ideas of biological plausibility and simulator flexibility are both raised frequently, it would be good for the authors to specify what aspects of biological plausibility might be lost or maintained when users take advantage of different forms of flexibility in the simulator. For example, for the "most basic mode" of phosphene mapping described in lines 283-286, how much of the biological modeling is bypassed? Are V1 stimulation locations assumed based on the phosphene locations to calculate other phosphene characteristics?

4) Do the additions of nonlinear phosphene interactions, such as the ones in Figure 1—figure supplement 3, have any significant effect on simulator speed?

5) Aside from the instances of cross-validation, the authors frequently use the terms "validate" or "validation" when "verify" or "verification" would be more accurate. Particularly when the authors are demonstrating that model output reasonably matches the data for which it was configured to fit, the authors should not use the term validation.

6) The authors refer to cortical-surface electrodes generally as ECoG electrodes, but only a subset of the referenced studies used electrocorticography arrays. The Brindley and Lewin, Dobelle, and Orion systems did not record neural activity, and thus would not be classified as ECoG systems.

7) It would be useful for the authors to provide an example of how brightness accommodation is taken into account by the simulation over time.

8) In the right panel of Figure 2, it is unclear what "1e-7" at the top of the panel signifies.

9) It can be confusing how both memory trace and minimal input charge use the symbol Q.

10) In Figure 1—figure supplement 1, noise from a normal distribution with σ = 0.03 degrees is probably a bad example for representing uncertainty in phosphene location. Pointing responses from implantees can have standard deviations on the order of 3 degrees, so achieving a standard error of 0.03 degrees would require around 1000 localization trials per phosphene. Although this is just an example and the simulator can use any level of uncertainty, a more meaningful example of noise might use σ around 0.5-1.0 degrees.

11) Lines 141-142: The definition for stimulation threshold is vague. The threshold of perception is usually defined as the level at which the probability of stimulus detection is 50%, or sometimes 75%. Is there a specific probability associated with "reliably produce a visible phosphene"?

12) Line 270: The model is described as memory intensive. What ranges of memory are required?

13) Lines 323-329: Phosphene size is calculated based on the current provided, but not total charge. How is pulse width taken into account for phosphene sizes?

14) Lines 381-384: Activation thresholds are determined purely on a per-electrode basis. The authors should discuss how reduced charge-per-electrode thresholds with multi-electrode stimulation can be included in the simulator (e.g., less charge per electrode required when using 2 or 4 adjacent electrodes instead of a single electrode).

15) Line 453: The reference to the coefficient of determination should be paired with a clarification that this was only a verification of the parameter fitting process and not a demonstration of how the simulator matches unseen data.

16) Lines 758-759: The text mentions considerations for phosphene-perception delays after stimulation onset. Stimulation strategies will also be important for addressing phosphene perception persisting after stimulation offset. Is such undesired persistence modeled at all by the simulation?

17) Line 1023: The linked repository appears to be inaccessible: https://github.com/neuralcodinglab/dynaphos-experiments

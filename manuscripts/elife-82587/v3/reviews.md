# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82587.sa0](https://doi.org/10.7554/eLife.82587.sa0)

This manuscript investigates how the fly visual system can encode specific features in the presence of self-generated motion. Using volumetric imaging, it explores the encoding of visual features in population activity in the Drosophila visual glomeruli – a set of visual "feature detectors". Through an elegant combination of neural imaging, visual stimulus manipulations, and behavioral analysis, it demonstrates that two different mechanisms, one based on motor signals and one based on visual input, serve to suppress local features during movements that would corrupt these features. The results of this study open up new directions to determine how motor and visual signals are integrated into visual processing at the level of neural circuits.


---

# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82587.sa1](https://doi.org/10.7554/eLife.82587.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Visual and motor signatures of locomotion dynamically shape a population code for feature detection in Drosophila" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Claude Desplan as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Terufumi Fujiwara (Reviewer #1); Cristopher M Niell (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers appreciate the quality of the work presented in this interesting manuscript. The combination of neural imaging, visual stimulus manipulations, and behavioral analysis elegantly demonstrates that two different mechanisms, one based on motor signals and the other based on visual input, serve to suppress local features during movements that would corrupt these features. In spite of the high quality of the work, the reviewers raised several technical concerns that should be addressed prior to the publication of the manuscript. It is very likely that most of these points can be resolved through the analysis of existing data and/or appropriate editing of the main text. The reviewers agree that the addition of new experimental data can be minimized.

1) You should rule out that the correlated gain modulation observed in Figure 4 (and subsequent) is not due to motion artifacts or other factors that might vary during imaging. This control could be achieved by showing/analyzing red channel traces that you might already have. Alternatively, you could add a few caveats in the discussion about whether other factors might influence correlations across the population of VPNs.

2) In Figure 5, could the walking behavior be decomposed into forward and angular velocity components? This would strengthen the association between visual signals and specific behaviors. Through this analysis, it would be important to clarify the scope of "self-motion" by defining whether the visual inputs associated with rotations and forward movements are processed in the same way. Could the angular velocity range be computed during inter-saccade intervals of free-moving behavior to estimate the corresponding visual responses?

3) We encourage you to split the data in Figure 3D based on walking versus stationary states to demonstrate that the VPNs projecting to LC18 show the modulation seen in Figure 5C. This result would mitigate the possibility that the modulation by self-motion results from other inputs into the glomeruli that weren't completely eliminated by the genetic manipulations.

4) If possible, please complement the data presented in Figure 6 with a comparison of the activity observed upon rotational motion and stationary gratings.

5) Please motivate the idea that stimulus identity is encoded at the level of population activity and that positive correlations enhance stimulus decoding. The enhancement in stimulus decoding appears counter-intuitive. Related to this point, it would be helpful to improve the representation of the trial-to-trial correlations in a stimulus-dependent manner.

Reviewer #1 (Recommendations for the authors):

Figure 4

Even though the analysis looks quite reasonable, I have difficulty understanding how exactly the trial-to-trial activity correlation among glomeruli improves decoding visual feature identity. If the trial-to-trial correlation is totally random across identical visual stimulations, it will not provide extra information on visual feature identity. Therefore, the trial-to-trial correlation needs to be organized such that the shared activity (amplitude) is somehow specific to each visual feature stimulus. For example, the shared activity amplitude is always around 0.8 for looming and always 0.3 for single stripe, etc. Then, isn't such consistent activity already reflected in the total activity at each glomerulus? Alternatively, one possibility I could imagine is like following:

The activity of glomerulus A to looming: total activity = 1 (glomerulus-specific activity=0.2 + shared activity=0.8).

The activity of glomerulus A to single stripe: total activity = 1 (glomerulus-specific activity=0.7 + shared activity=0.3).

In this case, we cannot decode if the visual stimulus was looming or a single stripe from the total activity of glomerulus A, but we can decode if the total activity is divided into glomerulus-specific + shared activities. Is this the correct direction to interpret the result? Anyway, I wonder if the authors could provide a bit more intuitive explanation of how the shared activity contributes to the decoding.

Figure 8

Authors elegantly demonstrated that responses to local visual features are largely suppressed during visual and body saccades. On the other hand, it is not clear yet if the responses are not disturbed by suppression during inter saccade intervals or when the fly wants to process it. I wonder if the authors could estimate the angular velocity range during inter saccade interval from free moving behavior and estimate how many visual responses can be maintained in that range.

Reviewer #2 (Recommendations for the authors):

Overall, the study was well-designed and the data was presented clearly.

1. The authors make a compelling argument that they have restricted the glomerular signals to the PN terminals, and Fig 3 verifies that they match up in terms of mean response. However, it seems possible that some of the modulations by self-motion could represent either pre-synaptic modulation, or other inputs into the glomeruli that weren't completely eliminated with their genetic approach. Splitting the data in Fig 3D based on walking vs stationary and demonstrating that the VPNs projecting to LC18 also show the modulation seen in 5C would be a good way to confirm this.

2. The data in Fig 6A-G compellingly demonstrates that low SF stimuli suppress the response, but it's not clear that it is the rotational motion that is important since there is no comparison to stationary gratings. If that data is available (as it is for Fig 7) it would be very helpful, otherwise, it might be best to clarify that this data supports low SF stimuli suppressing, and the rotational effect is only shown later. On a related point, it is a little surprising that the coherent dots suppress the response since I would expect these to be more like the high SF / whitened stimuli of Fig 7.

3. The fact that visual stimuli can be decoded from the population in the presence of modulation by movement signals is quite similar to the findings of Stringer et al 2021 and Rumyantsev et al 2020, so it might be worth noting these.

Reviewer #3 (Recommendations for the authors):

1) My first concern is about whether any of the correlated gain modulations the authors observe could be due to motion artifacts or other factors that might vary during imaging but might not reflect actual neural signal intensity variations. This is a particular concern in Figure 4 where such shared variability is first introduced. Ideally, the authors would show imaging of the red channel from the same trials showing that this is not modulated by the shared gain factor. At the very least the authors should mention possible confounds that could give rise to this variability and discuss measures taken to rule these out.

2) Although the manuscript is framed in terms of "self-motion," most of the analysis and experiments focus on fast rotational motion evoked by body saccades. For example, the analysis in Figure 1 deals only with rotational motion, as do the visual suppression experiments in Figures 6 and 7. However, Figure 5 shows suppression driven by walking (not necessarily turning) and it is not clear from the figure if these represent rotations or forward movements. Therefore, it is not clear if the two inputs discussed are "working together" as suggested in the Discussion, or cover different types of input (during forward motion versus turns).

Although this does not detract from the interest of the work, it is confusing, as self-motion also includes large translational components which are not discussed (much) here and as saccadic suppression of visual signals has been discussed elsewhere. The authors should clarify in the Abstract and Introduction that their focus will be on rotational motion related to body saccades, and should address the differences between these types of motion in the Discussion.

3) The authors perform a decoding analysis of stimulus identity to argue that stimulus identity is encoded at the level of population activity and that positive correlations enhance stimulus decoding. This seems strange to me because classical studies of correlations in visual encoding (e.g. Shadlen Newsome) emphasized the way that correlated variability reduces the encoding capacity of a network. The emphasis on encoding stimulus identity within the particular stimulus set presented also seemed strange to me because it is not clear that the fly needs to discriminate between each of these stimuli in order to make appropriate behavioral responses. For example, flies are known to respond differently to vertical stripes versus short spots, however, it is not clear if they care about the difference between spots of slightly different sizes, or between spots moving on a gray versus grating background. Presumably, psychophysics experiments combined with connectomics can help determine which combinations of glomerular responses are actually used by the fly to shape its behavior. At any rate, I find that the conclusions about how VPNs encode visual features (e.g. Discussion line 439) rest on an assumption about what the fly is trying to do with these stimuli that may not be accurate.

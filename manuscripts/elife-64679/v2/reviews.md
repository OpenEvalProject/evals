# Peer review - Round 1

Editors:
- Cornelius Schwarz

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64679.sa1](https://doi.org/10.7554/eLife.64679.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Delhaye et al., study the role of local tangential skin strain for tactile neuronal encoding in humans, variables that were not accessed by classic studies. They visualized the fingerprint when moving across a smooth surface together with extracellular recordings of primary afferents with a receptive field on or close to the fingerprint. Focusing on the period, in which the fingertip partially loses contact with the surface and starts to move (partial slip), they found that fast-adapting primary afferents type 1 (FA1) consistently respond to local strain, with predominance of compression over stretch, while the slowly adapting type 1 (SA1) do not. The FA1 responses during partial slip show selectivity to directional/orientation of the compression wave with some initial insights about the contribution of papillary ridges at the site of the neuron's receptive field.

Decision letter after peer review:

Thank you for submitting your article "High-resolution imaging of skin deformation shows that afferents from human fingertips signal slip onset" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Cornelius Schwarz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Rochelle Ackerley (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Delhaye et al., study the role of tangential skin deformation for tactile encoding in humans, variables that were not accessed by classic studies. They use visualizing the fingerprint when moving across a smooth surface together with extracellular recordings of primary afferents with a receptive field on or close to the fingerprint. 'Fast-adapting type 1, one out four classes of human primary afferents, are shown to respond to strain, rather than stretch when the fingerprint's adherence to the surfaces goes from a fixed state to a partial attachment to full slippage.

Essential revisions:

The reviews both see considerable merit in your work. They agree that it contains considerable advances in the field of human tactile coding by combining, for the first time, the visualization of skin strain patterns and microneurography. They state the results on FA1 will be important to students of perception as well prehension. Both generally support future publication. However, they state major comments as well, which I will summarize below. I consider the major points all important enough to expect you to address them either with new analyses or through improvement your treatment of them in the text.

1. The most important criticism was raised unanimously by the reviews. It should be addressed by adequate new analyses. It states that while making excellent points about FA1 afferents, there is a deficiency in covering SA1 primary afferents. (The other two classes are considered to be not sufficiently sampled and should be clearly labeled as circumstantial findings). This deficiency was considered most remarkable as SA1 do fire vigorously to presentation of the stimuli. The authors argue that the unexplained SA1 activity was mainly due to vertical skin deformation that they cannot monitor. In apparent contrast, however, the experiment was designed to abolish or minimize normal, i.e. vertical forces. The authors need to clarify this issue. They should explain what the purpose of robotic normal force control was, and importantly, in how far it worked (or did not work). What is the precision of their normal force measurement? Is the measurement suited to relate spike trains to time series of measured normal force? If yes, the reviewers recommend to use those measurements. In the discussion the authors need to clarify how their speculation about vertical forces activating SA1, relates to the robotic normal force control and measurements and Figure S1.

The reviewers feel that figure S1 is a good start, but more detailed analysis in this direction would be helpful. A possible temporal relationship of tangential deformations and SA1 firing is not sufficiently analyzed. The analyses used (STA and regression) are not systematically focused to bring out temporal relationships between SA1 and skin deformation. The implemented STA analysis seems to consider just one time-bin of 20 ms length for spiking and strain (the camera frame rate), while, in unexplained discrepancy, the regression analysis uses convolution of the spike train with a Gaussian window of 480 ms length – strongly diluting the temporal relationship of spike and strain parameters. The authors need to explain the rationale using the two extreme temporal settings in the two analyses. And they should apply a systematic approach to analyze temporal relationships of spikes and strain maps.

Maybe the authors even have runs/sessions without normal force control? If yes, these could be analyzed and presented.

Toward SA1 coding the reviewers specifically recommended to study/analyze the following:

Is it feasible that SA1 spiking dynamics are different for different directions of skin deformations (indentation vs. horizontal), e.g. could SA1 be slow for vertical but fast for horizontal stimulation, or vice versa, etc.?

The authors should go beyond their present attempts (mainly Figure S1), and build a model that is focused to find out the temporal relationship of strain/stretch/shear as well as normal forces and SA1 spikes.

Could the STA and regression analysis be helped by fitting responses to past skin deformations at longer delays than 20 ms (STA) or 12 ms (Figure S1)?

The authors use 'correlations' of deformation and spikes as basis for their arguments. Maybe it would be more appropriate to calculate delayed correlation, i.e. e.g cross correlation patterns to help to explain SA1 responses to the strain dynamics?

A further observation was that SA1 code for movement without slipping (in apparent contrast to FA1). A related phenomenon observed in the firing rate traces is a conspicuous silencing of SAI firing during movement (especially in the low friction condition). Is it feasible that SA1 signal touch well – albeit through the absence of firing?

It is interesting to note that the only afferents that have any response during movement, but not slipping, are SA units. This would be expected, but it is interesting that the non-slip moving phase show overall less firing than in the initial stationary load phase. Do the authors think that this could be an effect of the general decrease in firing frequency (i.e. adaptation) from SA units (with a re-increase in firing from slip) or is it more specific and somehow related to a difference in fingertip forces? This second idea about a real difference in firing between the stationary and moving-without-slip phases could imply that SA units do encode such specific aspects of touch, which FAs do not. From Suppl. Figure 2, it certainly seems that there are such differences.

2. Another unanimous point of the reviewers was the perceived insufficiency of the analysis of preferred direction. First of all, the definition (line 167) was not clear. Was it medial/lateral/radial/ulnar or in degrees (what does 0 deg refer to)?. The authors are recommended to calculate a standard directionality index (e.g. (pref-unpref)/(pref+unpref), vector sum, etc.). Further, the reviewers see the need to differentiate preference for 'directionality' from that for 'orientation'. In addition, it is recommended to clarify the following parameters related to the issue of directionality/orientation tuning:

a. Receptive field location

b. Orientation of papillary ridges inside the RF

c. Directionality relative to fingertip or papillary ridges?

In 8 of 13 FA1s the direction preference was not detailed. Was it like the other units or did they have no preference? Figure 3C and legend should be improved to clarify these questions.

3. From figure 4 it appears that responses to the same movement direction performed as 'forward' and 'backward' are very different. The reviewers felt that this phenomenon deserves a proper treatment. The authors are asked to clarify how consistent the phenomenon is, and whether there is a possible explanation in terms of different contexts that leads to it? It is considered worth to report whether SA1 show the same.

In Figure 4 please label the top and bottom series of strain maps – what exactly do they represent? High/low friction? The touch does not cover the receptive field in the bottom maps, what does that mean, which effect may it have on firing?

4. The reviews also noted that STA analysis was only done with ||e||. As a main conclusion of the paper is about responses to strain versus stress, shouldn't STA be performed with exx, eyy, exy to differentiate those parameters? In this respect the question was raised why the authors focus on the annular pattern. Given the annular form of the partial slip and the high-correlation of deformations across the fingertip such a pattern is trivially expected (especially using ||e||). The authors are recommended to use the mentioned more specific parameters exx, eyy, exy, and focus first on the RF, and second on deformations elsewhere (maybe using some decorrelation techniques).

5. It was further suggested to attempt using GLMs or similar to capture non-linearities between strain and spikes. The rigid linear model will fail to capture expected non-linear relationships between spike rates and other parameters.

6. Both reviewers found the part of the discussion stimulating, in which the authors touch upon orientation selectivity (line 351-354). It seems an interesting point to consider the differences between slips and edges – both in forces and neural information. Do the authors have evidence to think the brain could tell the difference between a slip and an edge? Alternatively, the speculation starts to explain orientation selectivity of primate tactile neurons in terms of prehension (rather than perception of edge orientation, as is typically assumed). This point is considered to be an outcome of their novel measurements. It should be worked out and presented more prominently.

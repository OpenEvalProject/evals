# Peer review - Round 1

Editors:
- Martin Vinck, Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66400.sa1](https://doi.org/10.7554/eLife.66400.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The visual cortex contains an abundant of recurrent connections that are critical for computation. The authors show how local optogenetic inactivation of a column in macaque V1 leads to heterogeneous and layer-dependent activity changes mediated by lateral interactions. These changes range from full suppression to facilitation, and a mixture of both. The authors further demonstrate that these lateral interactions determine behavioral outcomes, hence suggesting that behavioral outcomes cannot be predicted based on the focal inactivation alone.

Decision letter after peer review:

Thank you for sending your article entitled "Heterogeneous side-effects of cortical inactivation in behaving animals" for peer review at eLife. Your article has been reviewed by four peer reviewers, including Martin Vinck as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor.

As you will see from the reviewers, they are mixed, although three reviewers make numerous positive remarks (and also some critical comments) about the interest of the paper. Notably there are a number of concerns that need to be addressed, in particular the potential need for additional experiments related to the sampling of the contrast. Reviewers raised the concern that sampling of the contrast axis should be based on 7-8 contrasts, and that the under-sampling of contrast space in combination with low trial numbers might affect the claims about increased activity at low vs. high contrasts and the conclusions on heterogeneity. It would be important to understand how this concern will be addressed. One option could be, e.g., to validate the findings in a smaller set of experiments, if possible. Besides this point, you will find numerous other concerns to be addressed below.

Essential revisions:

Reviewer #1:

The authors use focal optogenetic inactivation together with dual laminar recordings in awake primates to study the impact of activity in one column on the activity in another column. With this technique, they investigate the nature of lateral interactions and normalization mechanisms in V1. The key findings are that: (1) Optogenetic inactivation does not yield an overall facilitation or suppression in a nearby column. (2) This is explained by heterogeneous changes in activity that are stimulus dependent, with four main types of responses, the most common one being general suppression across all stimulus contrasts, in particular in the supra-granular layers. (3) A simple E/I network can predict these four types depending on two parameters. (4) There exists a high degree of variability across sessions, however in sessions with predominantly Type-1 responses (suppression), behavioral outcome is also affected. Together, these findings suggest that the effect of optogenetic inactivation on the local circuit is highly complex, that lateral interactions are highly heterogeneous across cells and that focal optogenetics inactivation might impact behavior in a complex manner. My main comments pertain to the statistical analyses:

1. It was not entirely clear to me how the four subgroups were statistically quantified.

A. Where the individual neurons that belong to the four types statistically significant?

B. Was the distribution in four types statistically different from chance?

C. How was the choice of four categories motivated, was this done through a clustering mechanism?

2. It would be useful to discuss how the contrast-dependence of lateral interactions (with visual stimuli) fits or does not fit with the present results.

3. The nature of the model is not entirely clear: Which variables represent the local site and which variables represent the distant site? Do both have E/I neurons? What are the connections between those?

4. It would be useful to explain better what standard normalization models would predict. There is some discussion on this, but it is not clear why one would expect suppression of a distal site rather than activation at these retinotopic distances. In this context it would also be useful to discuss Mexican-hat profiles of activation/suppression in relationship to the present findings.

5. Detailing criteria for spike sorting would be useful for future studies comparing to the present findings.

6. Figure 2C misses a color bar.

7. Unless my PDF renderer has a problem, Figure S5 seems to be the wrong figure (duplicate of Figure 5) and this control should be fixed.

Reviewer #2:

Andrei and colleagues performed an optogenetic experiment in area V1 of monkeys, whereby they inactivated glutamatergic neurons using a lentiviral vector approach with CamKII as promotor and the chloride conducting GtACR2 opsin. To investigate the local network effects of the optogenetic inactivation, they recorded single and multiunit activity nearby the optic fiber and at about 300 micron distance. The major claim of the authors is that local reversible inactivation leads to unexpected or unpredictable activity changes in (nearby and) distant neurons. Neurons affected by the light were classified in 4 groups, depending on the optogenetic-induced dynamic activity changes. These 4 types of responses could be predicted based on a simple spiking model with a linear combination of excitatory feedforward drive and local recurrent excitatory and inhibitory inputs. In addition, monkeys also performed a contrast detection task, and performance was impaired only when the activity in the majority of the (recorded) neurons was suppressed.

This study yielded a number of interesting findings, but contrary to the framing of the authors, ("unexpected" "unpredicted" "most surprising" "unpredictable", "off-target effects have never been investigated…"etc.), a variety of immediate downstream "off-target" effects after optogenetic activation and inactivation have been amply described in primates -already starting with the first optogenetic study in monkeys (Han et al., 2009). The main 'selling' point of the study is unsurprising. Virtually every study so far showed, predictably, a mixture of facilitation and suppression at single unit level, independent of the type of opsin used. In general, more suppression is found with a hyperpolarizing opsin and more (or net) enhancement with depolarizing opsins. That said, the current findings whereby neighboring and distant effects at neuronal level are compared, are certainly a nice addition to the literature, as is the apparent division in four response classes. The authors should significantly tone down their language, however. Of course, this has also consequences for the impact of the paper.

This reviewer also questions the usefulness of GtARC2 due the exceedingly long after hyperpolarization, which may have contributed to the potentially stronger off-target (i.e. facilitation) effects compared to other hyperpolarizing opsins. Also, it is unfortunate that continuous stimulation was used, which prohibits a latency analysis in the distant neurons. Such an analysis would have made the discussion about direct versus indirect effects much simpler, at least compared to the current argumentation of the authors.

The authors argue twice that it is troublesome to interpret optogenetic -induced effects without measuring neuronal activity at distant sites during light exposure. This reviewer does not argue about the usefulness of concurrent recordings. However, it is almost impossible to cover all sites which may show off-target effects. In the present study, one only recorded at (some sites) at 300 micron distance. Yet, all sites connected with the neurons directly affected by the light might show "off-target" effects, even those in remote areas. It is impossible to 'cover' all these sites with electrophysiological recordings. Hence the solution offered by the authors is not workable. Whole brain imaging may be an alternative, yet it remains challenging to relate changes in imaging signals with alterations in neuronal activity.

The authors categorized the optogenetic induced neuronal responses at a distance in four classes, which is a nice finding. It is unclear, however, how the neurons were clustered. Unless I missed it, no clustering approach with objective criteria to determine the number of relevant clusters was used. Please elaborate on this.

The authors emphasize the degree of heterogeneity of the indirect network effects, but this may be highly related to the transduction efficiency and layer-specificity of transduction.

Figure S5 is the same as Figure 5.

Reviewer #3:

The manuscript investigates the important question how local optogenetic silencing of V1 neurons affects neural populations that are located nearby, and whether these effects can impact on behaviour. Based on contrast response functions, the authors identify 4 different effect types, which range from inhibition only through mixed effects that depend on stimulus contrast to facilitation only.

The diversity of effects could be replicated in a network model by varying stimulus sensitivity of network inputs.

Behavioural effects on contrast detection occurred only when off target effects were dominated by type I effects, i.e. those that show inhibition at all contrast levels.

The idea of studying the effects of optogenetic silencing on off target neurons is important, but there are problems with the identification of different effect types given the coarse sampling of stimulus contrasts. Also, the effect on behaviour would benefit from more detailed investigation, e.g. limiting the stimulus dimensions to off target locations, as well as obtaining a lager data base to study effects of other response types on behaviour more quantitatively.

1. In methods the injection procedures are described, but it remains unclear how 'the deepest point' of a column was determined? Was it a fixed depth that was targeted? Also, the 5 injections per column were probably evenly spaced. But the distance between sites should still be given.

2. Methods: "If either the transient or sustained response during optical stimulation was significantly different (P<0.05, Wilcoxon rank sum test)" -- was this corrected for multiple comparisons? After all 2 tests are done on the same activity.

3. The contrast fitting function (aka Nassi) is problematic due to the number of contrasts tested in a single experiment. It has 4 free parameters for 5 data points (when 4 +0% contrast was used). Also, the equation has no numbering.

4. Were the oriented gratings really flashed at 30Hz? i.e. 33ms on time per stimulus? This could induce strong masking effects.

5. In methods the authors state that the light guide was close to the recording electrode in 7 sessions. In figure 1E it states that n=48, while in the text it states that n=41 when the statistics are mentioned. Also, it is unclear whether this is neurons or contacts? Were there depth differences for these n=48(41).

6. Were the effects of light stimulation at different contrasts corrected for multiple comparison? If not, they should be.

7. Unless I am mistaken, equation 1 has 4 free parameters (r0, rmax, P,Q, with c50 and n fixed) that are fit to each neuron with optogenetic stimulation? If so, this is problematic for the reasons mentioned above. The authors only measured 5 data points, and the model is thus likely to overfit. Hence the variance accounted for is not very impressive. If my understanding of the fitting procedure is mistaken, then the authors should explain in detail how it was implemented.

8. The authors should describe in detail how the classification of the 4 response types was arrived at. How was the 'Type' category defined? Ideally this would be done, based on the terms P and Q yielding significant improvements to the fit?

9. The data shown in figure 3D-G are puzzling. The P values are mostly negative, i.e. they seem subtractive, rather than additive? That suggests the network does not provide excitation, unlike stated in the main text. Also, the c50 values of many neurons appear very high, and are in a range where sampling was basically absent. All examples shown in figure 2 have c50 values much lower.

10. While the claim that type 2 neurons are more sensitive to low contrast than other types, is correct, this cannot be inferred from the slope of the fitting function, but from the c50. If a neuron did not respond to any contrast including 20%, but strongly to 100% stimuli, it would have a c50>20%, but could have a very steep response function, which would be an artefact of the fitting in conjunction with the sampling.

Reviewer #4:

In this study the authors examine the effects of optogenetic inactivation directed onto a cortical site on neuronal activity of nearby lateral loci (off-target), and on behavioral performance.

They find that inactivation of the superficial layers, while reliably suppressing activity at the inactivation site, causes heterogeneous effects at off-target cortical loci, with some laminar-bias. The authors further determined that changes in behavioral performance were consistently observed only in sessions where suppressive effects among recorded cells dominated. The study is overall well executed, and well presented, and it is of interest to a broad audience. Some additional analysis would strengthen the claim that photostimulation at the inactivation site does not spread to nearby loci, where the recordings are made. Moreover, it is unclear whether the observed heterogeneous effects would become more homogenous at higher light intensities.

1) Could the effects seen at off-target sites depend on the specific temporal dynamics of the inactivating opsin used in this study? This point should be addressed in the discussion.

2) To strengthen the main claim of the paper, that off-target sites 300µm away from the inactivation site are not directly inactivated by light, the authors should determine the onset latency of suppressive effects at the on vs off-sites. The expectation would be that the latter are suppressed significantly later in time than the former if, indeed suppression is a network effect. While I do not expect that light could inactivate directly the deep layers at the off-site, it could easily spread 300µm away and directly affect the superficial layer cells. In support of this, the type I cells dominate in the superficial layers. Moreover, some of the off-site suppression, e.g. in the example cells in Figure 1F-G, seems to occur very early, possibly suggesting direct inactivation by light spreading to the off-site. Importantly, the latency analysis should be performed on a layer-by-layer basis because it is possible that only the superficial layer cells at the off-site are directly affected by light, while those in deep layers are a result of network effects. On p. 4 the authors state that:" The lack of suppression in the blank condition indicates these responses cannot be due to direct activation of GtACR2 at the distal site". First, the authors could strengthen this claim by showing this at the population level, rather than simply showing the few example cells in Figure 1F-I. On p. 6 the authors further make the point that the temporal profile of suppression seen at the inactivation site is rather different from that at the off-site, with long-lasting responses only found at the inactivation site near the light source. However, one could imagine that these different profiles may result from different light intensities at the inactivation site compared to the off-site; light scatter in tissue may result in reduced photostimulation intensity at the off-site. For the same reason, reduced light intensity at the off-site may also cause significant suppression only when the cell is driven by a visual stimulus, but not be apparent in the baseline response. For all these reasons, an analysis of onset latency of suppression (in the stimulus-driven condition) at the inactivated site vs the off-site could strengthen the authors' claim that the off-site is not directly affected by light.

3) I could not find the light intensity values used for inactivation anywhere in the manuscript. This should be added.

4) Figure 1E. rather than one example cell, it would be preferable to show the full laminar profile of suppression at the photoactivated site to demonstrate that light is, indeed, limited to the SG layers. This is shown in Figure S1B-C, but this figure is difficult to interpret correctly because the Y axis is not labeled, and the estimated top and bottom of cortex as well as L4C are not indicated on the laminar plot.

5) Figure 2E. Judging from the CSD analysis, here the top of the cortex would seem to be contact 2, rather than 0, and the thickness assigned to the G layer is too large. The latter in vivo typically spans about 3, not 4, contacts (if the penetration are vertical which this appears to be). Moreover, the earliest current sink, which is the criterion for identifying layer 4C, would seem such that the top of G should be moved down by at least one contact. The selection should be based on a latency analysis. I am raising this issue because with layers more properly assigned the laminar data could potentially clean up and appear less heterogeneous.

6) Model. Could the 4 different types of responses depend on intrinsic properties of cells (for example their contrast response function), rather than, or in addition to the lateral network connectivity?

7) Model. What determines how strongly the network is driven by the stimulus, in the model and possibly in the real brain? In other words, what determines network sensitivity? Is this the weights of the local connections?

8) There should be a discussion of whether these results could change depending on photostimulation intensity. Is it possible that at higher light intensities the off-site would be more homogeneously suppressed for ex.?

9) Please add all sample size to the figure legends. For ex, sample sizes are missing in panels C and F of Figure 5.

10) Isn't it odd that effects on behavioral performance in Figure S7E are only seen at 20% contrast given that type 2 cells are suppressed at contrasts {greater than or equal to} 10?

11) P. 25 Layer Identification. The granular layer in the CSD analysis should be defined as the location of the earliest current sink, not the "maximum sink" as sated.

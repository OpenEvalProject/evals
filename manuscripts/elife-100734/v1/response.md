# Author response - Round 1

Authors:
- Ecem Altan ([ORCID: 0000-0003-2902-6880](https://orcid.org/0000-0003-2902-6880))
- Catherine A Morgan ([ORCID: 0000-0002-5837-8861](https://orcid.org/0000-0002-5837-8861))
- Steven C Dakin ([ORCID: 0000-0002-3548-9104](https://orcid.org/0000-0002-3548-9104))
- D Samuel Schwarzkopf ([ORCID: 0000-0003-3686-1622](https://orcid.org/0000-0003-3686-1622))

## Response text

DOI: [10.7554/eLife.100734.3.sa3](https://doi.org/10.7554/eLife.100734.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1 (Public Review):

We thank the reviewer for their careful evaluation and positive comments.

Adaptation paradigm

“why is it necessary to use an *adaptation* paradigm to study the link between SF tuning and pRF estimation? Couldn't you just use pRF bar stimuli with varying SFs?”

We thank the reviewer for this question. First, by using adaptation we can infer the correspondence between the perceptual and the neuronal adaptation to spatial frequency. We couldn’t draw any inference about perception if we only varied the SF inside the bar. More importantly, while changing the SF inside the bar might help drive different neuronal populations, this is not guaranteed. As we touched on in our discussion, responses obtained from the mapping stimuli are dominated by complex processing rather than the stimulus properties alone. A considerable proportion of the retinotopic mapping signal is probably simply due to spatial attention to the bar (de Haas & Schwarzkopf, 2018; Hughes et al., 2019). So, adaptation is a more targeted way to manipulate different neuronal populations.

Other pRF estimates: polar angle and eccentricity

We included an additional plot showing the polar angle for both adapter conditions (Figure S4), as well as participant-wise scatter plots comparing raw pRF size, eccentricity, and polar angle between two adapter conditions (available in shared data repository). In line with previous work on the reliability of pRF estimates (van Dijk, de Haas, Moutsiana, & Schwarzkopf, 2016; Senden, Reithler, Gijsen, & Goebel, 2014), both polar angle and eccentricity maps are very stable between the two adaptation conditions.

Variability in pRF size change

As the reviewer pointed out, the pRF size changes show some variability across eccentricities, and ROIs (Figure 5A and 5B). It is likely that the variability could relate to the varying tuning properties of different regions and eccentricities for the specific SF we used in the mapping stimulus. So one reason V2 is most consistent could be that the stimulus is best matched for the tuning there. However, what factors contribute to this variability is an interesting question that will require further study.

Other recommendations

We have addressed the other recommendations of the reviewer with one exception. The reviewer suggested we should comment on the perceived contrast decrease after SF adaptation (as seen in Figure 6B) in the main text. However, since we refer the readers to the supplementary analyses (Supplementary section S8) where we discuss this in detail, we chose to keep this aspect unchanged to avoid overcomplicating the main text.

Reviewer #2 (Public Review):

We thank the reviewer for their comments - we improved how we report key findings which we hope will clarify matters raised by the reviewer.

RF positions in a voxel

The reviewer’s comments suggest that they may have misunderstood the diagram (Figure 1A) illustrating the theoretical basis of the adaptation effect, likely due to us inadvertently putting the small RFs in the middle of the illustration. We changed this figure to avoid such confusion.

Theoretical explanation of adaptation effect

The reviewer’s explanation for how adaptation should affect the size of pRF averaging across individual RFs is incorrect. When selecting RFs from a fixed range of semi-uniformly distributed positions (as in an fMRI voxel), the average position of RFs (corresponding to pRF position) is naturally near the center of this range. The average size (corresponding to pRF size) reflects the visual field coverage of these individual RFs. This aggregate visual field coverage thus also reflects the individual sizes. When large RFs have been adapted out, this means the visual field coverage at the boundaries is sparser, and the aggregate pRF is therefore smaller. The opposite happens when adapting out the contribution of small RFs. We demonstrate this with a simple simulation at this OSF link: https://osf.io/ebnky/. The pRF size of the simulated voxels illustrate the adaptation effect should manifest precisely as we hypothesized.

Figure S2

It is not actually possible to compare R2 between regions by looking at Figure S2 because it shows the pRF size change, not R2. Therefore, the arguments Reviewer #2 made based on their interpretation of the figure are not valid. Just as the reviewer expected, V1 is one of the brain regions with good pRF model fits. We included normalized and raw R2 maps to make this more obvious to the readers.

V1 appeared essentially empty in that plot primarily due to the sigma threshold we selected, which was unintentionally more conservative than those applied in our analyses and other figures. We apologize for this mistake. We corrected it in the revised version by including a plot with the appropriate sigma threshold.

Thresholding details

Thresholding information was included in our original manuscript; however, we included more information in the figure captions to make it more obvious.

2D plots replaced histograms

We thank the reviewer for this suggestion. The original manuscript contained histograms showing the distribution of pRF size for both adaptation conditions for each participant and visual area (Figure S1). However, we agree that 2D plots better communicate the difference in pRF parameters between conditions. So we moved the histogram plots to the online repository, and included scatter plots with a color scheme revealing the 2D kernel density.

We chose to implement 2D kernel density in scatter plots to display the distribution of individual pRF sizes transparently.

(proportional) pRF size-change map

The reviewer requests pRF size difference maps. Figure S2 in fact demonstrates the proportional difference between the pRF sizes of the two adaptation conditions. Instead of simply taking the difference, we believe showing the proportional change map is more sensible because overall pRF size varies considerably between visual regions. We explained this more clearly in our revision.

pRF eccentricity plot

“I suspect that the difference in PRF size across voxels correlates very strongly with the difference in eccentricity across voxels.”

Our original manuscript already contained a supplementary plot (Figure S4 B, now Figure S4 C) comparing the eccentricity between adapter conditions, showing no notable shift in eccentricities except in V3A - but that is a small region and the results are generally more variable. In addition, we included participant-wise plots in the online repository, presenting raw comparisons of pRF size, eccentricity, and polar angle estimates between adaptation conditions. These 2D plots provide further evidence that the SF adapters resulted in a change in pRF size, while eccentricity and polar angle estimates did not show consistent differences.

To the reviewer’s point, even if there were an appreciable shift in eccentricity between conditions (as they suggest may have happened for the example participant we showed), this does not mean that the pRF size effect is “due [...] to shifts in eccentricity.” Parameters in a complex multi-dimensional model like the pRF are not independent. There is no way of knowing whether a change in one parameter is causally linked with a change in another. We can only report the parameter estimates the model produces.

In fact, it is conceivable that adaptation causes both: changes in pRF size and eccentricity. If more central or peripheral RFs tend to have smaller or larger RFs, respectively, then adapting out one part of the distribution will shift the average accordingly. However, as we already established, we find no compelling evidence that pRF eccentricity changes dramatically due to adaptation, while pRF size does.

Other recommendations

We have addressed the other recommendations of the reviewer, except for the y-axis alignment. Different regions in the visual hierarchy naturally vary substantially in pRF size. Aligning axes would therefore lead to incorrect visual inferences that (1) the absolute pRF sizes between ROIs are comparable, and (2) higher regions show the effect most

prominently. However, for clarity, we now note this scale difference in our figure captions. Finally, as mentioned earlier, we also present a proportional pRF size change map to enable comparison of the adaptation effect between regions.

Reviewer #3 (Public Review):

We thank the reviewer for their comments.

pRF model

Top-up adapters were not modelled in our analyses because they are shared events in all TRs, critically also including the “blank” periods, providing a constant source of signal. Therefore modelling them separately cannot meaningfully change the results. However, the reviewer makes a good suggestion that it would be useful to mention this in the manuscript, so we added a discussion of this point in Section 3.1.5.

pRF size vs eccentricity

We added a plot showing pRF size in the two adaptation conditions (in addition to the pRF size difference) as a function of eccentricity.

Correlation with behavioral effect

In the original manuscript, we pointed out why the correlation between the magnitude of the behavioral effect and the pRF size change is not an appropriate test for our data. First, the reviewer is right that a larger sample size would be needed to reliably detect such a between-subject correlation. More importantly, as per our recruitment criteria for the fMRI experiment, we did not scan participants showing weak perceptual effects. This limits the variability in the perceptual effect and makes correlation inapplicable.

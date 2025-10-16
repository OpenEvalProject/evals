# Peer review - Round 1

Editors:
- Laura Dugué, Université de Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53715.sa1](https://doi.org/10.7554/eLife.53715.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript makes an important contribution to the current literature showing how the frequency gradients of human resting-state neuronal oscillations are organized in accordance with cortical hierarchy.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "The frequency gradient of human resting-state brain oscillations follows cortical hierarchies" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Laura Dugué as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

This manuscript presents results from a large dataset of human resting-state MEG recordings. The authors investigated the timely topic of the spatial distribution of low frequency brain oscillations, and found an anterior-posterior gradient in the frequency of brain oscillations. They further show a gradient in cortical thickness (CT), and suggest that CT correlates with oscillations frequency. Although investigating the spatial distribution of brain oscillations goes beyond simply studying their temporal dynamics, other studies have shown before that oscillation frequency varies across the brain. Reviewers have also noticed that such spatial gradients are in fact more specific to the alpha frequency. Some methodological aspects have additionally been raised including addressing the question of spatial leakage, and the possible confound of inter individual differences. Based on these comments and others described below, and on following discussions, the three reviewers concluded that this manuscript will not be considered further for publication in eLife.

Reviewer #1:

Mahjoory et al. present new results on a publicly available, resting-state MEG recording dataset from a large pool of participants. This well-written manuscript provides a systematic analysis of the spatial distribution of high-power, low-frequency, oscillations, based on non-invasive recordings of healthy, human participants. The manuscript is interesting in that the authors go beyond the mere temporal characterization of neural activity, using advanced source reconstruction approach and linear mixed effect modeling for statistics. Based on their results, the authors report a posterior-anterior spatial gradient of the dominant peak frequency, and further our understanding of the link between structure and function.

Numbered summary of any substantive concerns

1) My main concern regards the authors' statement that there is a decrease of the intrinsic resonance frequency from early sensory to higher-order area.

i) In their analysis, the authors identify PF on the 1/f-free power spectra and then select the PF that has the highest power based on the original power spectra. Isn't this approach necessarily increasing the probability to detect a pic at low (around alpha) frequencies? In other words, such decrease in oscillations' frequency is actually a decrease of, specifically, alpha oscillations. The band-specific PF analysis actually suggests such conclusion.

ii) It has been shown before (e.g. Rosanova et al., 2009) that different lobes of the brain have different "intrinsic resonance frequencies," e.g. beta frequency appears in anterior regions, and the proposed analysis does not seem sensitive to it. The Band-specific PF analysis, however, shows that indeed beta increases from posterior to anterior regions.

iii) Based on the results reported in Figure 4A, the authors suggest that there is a change in PF and CT as a function of the region's function (i.e. sensory vs. associative regions). Yet, the data seem to suggest that the effect is driven by the location of the different regions: we see high PF in VIS and DAN, which are mainly located in the posterior part of the brain, and low PF in the other networks. And doesn't this interpretation fit better the fact that there is a link between CT and PF? In other words, change in CT are probably not sparse across the head as some of these networks seem to be, right?

2) Could the authors give an intuition of the variance in ROIs' size for a given participant and across participant, as well as how the size affects the power spectra?

3) The authors argue that there is a posterior-anterior gradient of CT, which strongly correlates with the PF gradient. From the results presented in Figure 3, it seems that the CT gradient is more strongly explained by the Z-axis (thicker in ventral than dorsal regions).

4) Could the authors give an intuition of how stable (within participant) these PF are over time (see for instance Haegens et al., 2014)?

5) Could the authors comment on the absence of gamma oscillations?

6) Could the authors comment on the generalizability of their results given the fact that they analyzed resting-state data?

Reviewer #2:

This study investigated a novel and interesting topic on whether there is anterior-posterior gradient in the frequency of brain oscillations using source-localized MEG data. It was found that the spatial gradient of strongest peak-frequency decreases gradually and robustly along the posterior-anterior axis following the hierarchy of early sensory and higher-order areas. The manuscript is themed around a robust spatial gradient of the frequency of brain oscillations while the main finding was the spatial gradient in the frequency of alpha oscillation but not across oscillatory frequency hierarchy. I would suggest reframing the text to be better in line the findings. Further, the main analysis are mostly sound but methodological details are missing and some parts are difficult to evaluate. Also the contribution of spatial leakage as confounding factor to the results has not been sufficiently well tested and should be better controlled for.

1) The strongest peak in the original power spectrum was selected. Taken the robust alpha oscillations in rest, these peaks were in the alpha-band range (8-12 Hz) as visible in Figure 1A. The results hence describe the spatial gradient of alpha oscillations in narrow frequency range of 7 to 12 Hz. Thus, I find the title of the manuscript "The frequency gradient of human resting-state brain oscillations follows cortical hierarchies" as well as structure of text somewhat misleading and suggestive of the presence of spatial oscillatory frequency hierarchy, which seems not to be the case. Also the spatial gradients of peaks in theta and beta frequencies were estimated, but these data are now only shown in the supplementary material, not thoroughly analysed and only discussed very superficially. It looks like these data were added only for the reviewers. I think the authors should decide do they want to present a frequency gradient or an alpha-frequency gradient and modify the manuscript accordingly.

2) The correlation of the frequency and cortical thickness was estimated to investigate if the frequency is correlated rather with cortical hierarchy than spatial location. A correlation of -0.14 was found (Figure 3B). Albeit very significant, the correlation itself is very weak as also shown by the large scattered peak frequencies. Compared to correlation of -0.84 of the peak frequency with posterior-anterior gradient, this result indicates that alpha peak frequency is not strongly related to cortical hierarchy. The Results and Discussion should be modified to emphasize this point. Moreover, the authors could perform a partial correlation analysis among the peak frequency, posterior-anterior direction and cortical thickness – does the correlation with thickness persist when the posterior-anterior gradient is factored out?

3) Related to the above, in Materials and methods the authors write that to obtain correlation between PF and CT scores, the robust correlation was performed (Pernet et al., 2012). Pernet et al. released a new open source Matlab toolbox for analysis of robust correlations using multiple statistical tests. Which of tests would the authors have used for the correlation analysis?

4) The observed spatial gradient of peak frequencies can reflect a true continuous frequency variation along an anatomical axis or, alternatively, it could be caused by source leakage of distributed alpha sources at different frequencies and different cortical areas. The authors argue that if the spatial gradient is due to leakage then there should not be frequency change in alpha oscillations in V1. As there was a significant correlation of PF of V1 and its nearby 0.5-1.5 cm sources, the authors concluded that there is no source-leakage from the frontal source that could explain the spatial gradient. However, the alpha sources that could become mixed and cause confounding the results do not need to be localized to V1 and frontal cortex and hence estimating the source-leakage of V1 alpha source appears inadequate in my opinion. Classical MEG alpha literature suggests that the strongest alpha sources could actually be located higher in the visual cortical hierarchy, in the parieto-occipital sulcus or in areas near precuneus which could well cause significant leakage affecting the analyses. Second, the spatial accuracy of source-localized MEG is > 1-2 cm and hence the area for which the source-leakage was estimated could have been too small to test whether there is leakage or not.

5) The authors have used a Beamforming approach for source reconstruction. Several details of the source reconstruction approach are missing or unclear. First, if Beamforming was used for the entire brain volume in voxel space, how was data transformed to cortical parcellations and how were the values for each parcel obtained? The sensor covariance matrix was computed for 2 sec trials. Which trials were these?

Reviewer #3:

Mahjoory et al. examined a large dataset of human MEG-recorded neuronal oscillations to probe the relation between oscillation properties across space and cortical thickness. Their main findings are that the brain shows anterior-posterior gradients in the frequency of neuronal oscillations and in the slope of 1/f nonoscillatory MEG patterns. They also find a matching A-P gradient in cortical thickness, and they suggest that cortical thickness correlates closely with oscillation frequency in individual subjects, even after accounting for mean anatomical variations in each pattern.

My enthusiasm for publishing this paper at eLife is limited because most of their findings are not especially novel. Specifically, it is already known that oscillation frequency varies across the brain (see work by Voytek et al., Groppe et al., Zhang et al., and others) and merely replicating this finding in a large open dataset is not extremely innovative. Similarly, Figure 5 on oscillatory peaks is not novel and neither is the result showing an overall A-P gradient in mean cortical thickness.

The paper's novel claim is showing that oscillation frequency correlates with cortical thickness even after accounting for mean anatomical patterns. However, this result is not adequate to justify publishing the entire paper, especially because the data underlying this result were not examined in much detail and there was no compelling and specific proposed mechanism to directly link these two phenomena. Further, I am concerned that this apparent correlation could actually be a reflection of intersubject differences in mean thickness and oscillation properties, rather than by a detailed region-by-region correspondence between these variables within-subject, as the authors suggest. Failing to rule out this possibility is a substantial weakness in this analysis and the authors could do more to demonstrate this effect at the within-subject level.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "The frequency gradient of human resting-state brain oscillations follows cortical hierarchies" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Satu Palva (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The authors have revised the manuscript thoroughly based on the previous comments. The manuscript is a very nice addition to the current literature showing how the frequency gradients of human resting-state neuronal oscillations are organized in accordance with cortical hierarchy. Revisions are still required to clarify in the main text, the Abstract and the figures that the patterns are present within subject, as well as within frequencies in contrast to across frequencies.

Revisions:

1) A key part of the paper is showing frequency gradients both within and across subjects. The rebuttal letter does a good job explaining that the authors' statistical framework identifies this pattern robustly both within and across subjects. But the text related to this is still unclear. The authors should revise the text of the results to more clearly explain how their statistical framework identifies gradients both within and across subjects.

2) The authors should also consider revising their figures to show clear examples of within and across subject gradients. The scatter plots and brain plots in Figure 1, for example, are hard to understand because they seem to combine data both across subjects and regions. It would be very informative if the figures followed the statistical results.

3) In response to one of the reviewers, the revised paper now includes an analysis of analyses within specific bands. This new analysis is a bit hard to follow in the context of the paper because it is unclear how it relates to the paper's primary analyses. Is the idea that there are multiple oscillatory patterns at different frequencies that all show gradients simultaneously? Additional clarity here would be helpful.

# Peer review - Round 1

Editors:
- Martin Vinck, Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63798.sa1](https://doi.org/10.7554/eLife.63798.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Two-photon imaging in area V4 of awake monkeys was used to characterize the organization of tuning for distinct shape elements (curves, corners, and bars). The authors use a combination of wide field/low resolution imaging, to visualize large scale organization, with smaller field/high resolution imaging, to measure tuning and organization of individual neurons underlying the wide field results. At both scales, they establish that most V4 neurons are more responsive to curves and corners than to bars, and they establish anatomical segregation between neurons tuned for curves and neurons tuned for bars. These findings advance our understanding of the topographic organization of neuronal feature selectivity in area V4 of the macaque monkey.

Decision letter after peer review:

Thank you for submitting your article "Clustered Functional Domains for Curves and Corners in Cortical Area V4" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tirin Moore as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Timo van Kerkoerle (Reviewer #2); Ed Connor (Reviewer #3); Jack L Gallant (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

A prominent aspect of the visual cortex is the topographic organization in feature dimensions such as orientation, color, motion etc. The present study uses 2-photon imaging in area V4 of awake monkeys, which is a novel application of 2-photon, to characterize the organization of tuning for established shape elements (curves, corners, and bars). The authors use a combination of wide field/low resolution imaging, to visualize large scale organization, with smaller field/high resolution imaging, to measure tuning and organization of individual neurons underlying the wide field results. At both scales, they establish that most V4 neurons are more responsive to curves and corners than to bars, and they establish anatomical segregation between neurons tuned for curves and neurons tuned for bars.

Overall the reviewers made positive comments about this study especially noting the technological advance and the application of a new high-resolution imaging modality to the question of topographic organisation in area V4, although reviewers also commented that the present study is largely a replication of previous work.

Nonetheless, because of the technology used here, the reviewers assess that the work is of significant interest. The main comments of the reviewers pertained to the statistical analyses in this manuscript, which will require extensive revisions and data analyses.

Essential revisions:

1. Statistics

Major improvements will be required on the level of statistical and data analyses. In light of these concerns, we require the authors publish the data and software underlying the figures so that the statistical analyses become transparent and can be verified by the reviewers.

Reviewers commented that statistical analysis is almost completely lacking and is potentially wrong where it is provided. Complex results such as the ones presented by the authors need to be accompanied by appropriate spatial statistics. This will likely require substantial revision to the data analysis and the text. If necessary, the authors should consult a statistical/data science specialist for advice on how to perform the statistical analyses. It remains unclear whether the main claims will survive after appropriate analysis.

More specifically, it is unclear whether the ANOVA tests for significance of curvature- and corner-selective patches has been performed correctly. It appears that the authors identified curvature-selective patches by subtraction, and then performed the ANOVA on these patches. It is unclear whether this procedure is correct and may amount to double-dipping because regions are pre-selected before statistics are run. This kind of analysis can dramatically increase the Type 1 error rate and lead to false conclusions. Therefore, the significance values that are reported here are likely far more extreme than they would be otherwise. Many tutorials regarding how to do these sorts of tests correctly can be found in the neuroimaging literature, where this sort of problem has been extensively discussed in the literature and where it is standard to address it appropriately. The authors should consult one of those tutorials and implement a strictly correct (probably FDR-based) procedure. For instance, here is a possible starting point (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3221040/).

Reviewers commented that the statistical analysis to determine the significance of clustering also appear to be problematic. In fact, it is not clear from the details of the paper what has been precisely done. It appears that the CVSI and CNSI were not evaluated statistically, but ANOVA was used to evaluate tuning in some way, which remains unclear. It furthermore appears that spatial clustering was not assessed statistically at all. The lack of statistics and unclarity about statistics does not meet the prevailing standards of the field. Single neuron tuning needs to be assessed with the correct statistical tests, as does spatial clustering. Given these data and the pre-selection methods that were used to identify targets for the high-resolution analysis, this could be tricky. The authors should consult a statistical/data science specialist for advice on how do to these analyses correctly.

In general the results with the 16x objective likely suffer from double dipping, as they are preselected, therefore the statistical claims about large-scale topographic organization remain unconvincing.

2. Limitations were noted about the fine-grained analyses with the 16x objective. A limitation of the present work is that there is only one pair of patches for each animal images at 16x. The analyses need to be also extended. The authors should further analyze the topographic organization at the local scale, is the transition sharp or gradual, what is the variability etc. It seems that there is a rather sharp boundary and that the tuning stays relatively flat, looking at the Figures 2A-D, 3A, 4C and seems particular clear in 5A and C (using concentric versus radial gratings). However, there is no real quantification of this. Figure 2I-K shows the tuning over distance, but this analysis seems to be performed without taking the shape of the domain into account. One possibility would be to show a similar plot, but where the axis is taken perpendicular to the boundary of the domain. It seems that the interpretation that the authors give of the data would predict that the selectivity shows a sharp transition at the boundary and stays elevated within the domain. Furthermore, it would be relevant to get an estimate of the averaged selectivity as well as the variability within the domain, separately for the two animals. Finally, it would be relevant to compare both the sharpness of the transition as well as the mean and variability with the domain between the different stimulus set (curves versus angles, and concentric versus radial gratings).

3. Data visualisation

The authors should show more raw data (high-resolution fluorescence images with the field of view used for the main analyses), as well as traces of fluorescence as a function of time as is standard with imaging to appreciate the quality of the fluorescence traces (over tens of seconds). In addition showing dF/F responses for single neurons to different stimuli would be important.

4. Bar tuning

It needs to be very clear if the small amount of bar tuning reported is only in the ROIs that are defined by subtracting bars (where this would be therefore expected) or overall, in the discussion it currently sounds like this is the case overall which was not clear from the results.

5. Choice of stimuli

The exact choice of stimulus needs to be discussed: why only black (other studies used only white stimuli), why only lines (not surfaces as in e.g. Pasupathy et al. study that is referred to), why no colors. Is it assumed that this will not matter for the results and why?

The bar length is matched to the radius of the curve stimuli, which implies to me that the overall number of black pixels is never matched for bars vs the other categories? The authors should discuss if this is a problem.

Do you expect more curve/corner functional domains if you use different color or luminance contrast, or do you expect the non-significantly curve/corner clustered parts of V4 to contain other functional domains?

6. Temporal dynamics

The imaging technique confines analyses to a late time window. If possible refer to literature demonstrating that response preferences remain similar across time for these stimuli, since tuning can be dynamic over time (e.g. Nandy et al. 2016, Issa and DiCarlo eLife).

7. Introduction and Discussion:

Intro and Discussion read quite well and a lot of the relevant literature is referred to. But Intro and Discussion could include further/more explicit clarification why exactly this contrast (curve/corner) was used to study functional domains (or is this just a starting point), what other functional domains there could be.

The paper needs to cite literature relating curve/corner to animate/inanimate contrasts you discuss (e.g. Zachariou et al. 2018, and other work from Yue lab). You may consider a brief discussion/mention the potential use or function of functional topographic clustering (e.g. Kanwisher, DiCarlo), which is proposed to be related to naturalistic experience that is also discussed here without references.

The history presented in the introductory section of this paper is very strange. The first paper that reported curvature tuning in V4 was the Gallant et al. 1993 paper that is cited ambiguously here. It is true that paper used gratings rather than curved lines, but a neuron that is selective for curved gratings is also likely selective for curved lines. A similar principle holds for the hyperbolic grating selectivity reported in Gallant et al. 1993. The authors should address this directly and acknowledge the relationship late in their paper.

Similarly, in their subsequent 1996 longer report Gallant et al. argued that neurons selective for curved and hyperbolic gratings were spatially clustered. The data presented in the paper under review is far better than the data that were available to Gallant et al. way back in 1996, but this result was anticipated by that earlier 1996 report, however this finding is not cited.

The authors should discuss the recent paper by Roe lab on curvature patches using intrinsic optical imaging has just been published in eLife: https://elifesciences.org/articles/57261. This paper is relevant for relevant the points above, as they claim that there is a smooth transition from rectilinear to low curvature to high curvature (figure 7).

The authors should furthermore discuss this recent eLife paper on curvature domains, using both intrinsic and 2-photon imaging: https://elifesciences.org/articles/57502

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Clustered Functional Domains for Curves and Corners in Cortical Area V4" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Tirin Moore as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #2:

The authors replied sufficiently to most of the comments.

One answer is not clear to me, in response to the comment:

"Some more details about the expression levels would be useful. Most importantly, it is unclear from Figure 1C-F how homogenous the expression was in the selected region. Could you show a separate image where it is possible to judge the level of expression? Also, would it be possible to give an estimate of the general expression levels in terms of percentage of total neurons, as well as the percentage of neurons that were nucleus filled? Finally, it would be relevant to know injection speed in this regard."

First of all, they still do not provide the injection speed.

Also, they write: "Most of the neurons that are clearly visible in an average image are not nucleus filled (Figure 1—figure supplement 2)."

However, Figure 1—figure supplement 2 does not show any individual cells. Nor do any of the other supplementary figures provide an image where it is possible to judge the structure of the labelling in individual cells, so allowing to see whether they have a clear donut shape, or are nucleus filled. It would therefore still be relevant to see a large / high resolution image where this can be judged.

Reviewer #4:

The authors have put a lot of work into this revision and the paper is substantially improved over the initial submission. The paper is still largely replicative and confirmatory, but there is a place in the literature for such papers.

It is reported that the V4 receptive fields sampled here were very close to the fovea. That implies that the viewing window was very far lateral, much farther than most prior V4 studies. My intuition is that the ear would have had to be removed in order to access V4 at this location. If the authors recorded more medially then I suggest that they recheck their reported eccentricity to be sure that it is correct.

The indexes that are used here have a pretty unintuitive and unusual scaling range. (For example, an index of 0.2 indicates a 1.5 times difference.) The paper would probably be easier to understand if they had a more intuitive range/form. (For example, if 1.5 indicated a 1.5 times difference.) However, this is up to the authors' discretion.

Figure 2I "significant" is misspelled. There are also a few places throughout the manuscript where pronouns are missing. (I commend the authors on the English though, it is generally quite good!)

Also in Figure 2, please spell out what "CVSI" and "CNSI" mean in the caption. In this and other captions, it is best if the reader can generally understand the caption on its own, w/o having to wade through the text.

The use of hexagonal segments to try to understand differences in tuning for curves versus angles is a weak approach, because hexagonal shapes are a poor intermediate model for these feature classes. A much more powerful method for understanding these differences would be to use an explicit computational model. But that seems to be beyond the scope of this paper…

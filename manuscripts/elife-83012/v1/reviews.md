# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83012.sa0](https://doi.org/10.7554/eLife.83012.sa0)

This paper is expected to be of interest to systems neuroscientists in the fields of emotion, hippocampal function, and anxiety-related behavior. The authors performed recordings in the ventral hippocampus and show that (1) place fields become concentrated near the open areas of a maze, (2) direction-dependent coding decreases in these open areas, and (3) ventral hippocampal population activity in the closed area can be used to predict how mice explore the open area in the immediate future. These valuable findings provide convincing support for the potential role of the ventral hippocampus in the exploration of anxiety-provoking environments.


---

# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83012.sa1](https://doi.org/10.7554/eLife.83012.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Firing patterns of ventral hippocampal neurons predict the exploration of anxiogenic locations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Inah Lee (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Necessary neural analyses are missing from the paper. For example, basic analyses of single cell properties are lacking.

2) Previous dorsal hippocampal studies related to processing anxiety and fear need to be discussed more deeply to put the new findings within the proper context.

3) Behavioral data are not described and analyzed sufficiently. As it stands, it is unclear whether neural effects are due to differences in behavior.

4) Putative principal cells and interneurons should be analyzed separately, and it should be clear how cell types were subdivided.

5) Some details about methods are missing. For example, how were spikes during sharp wave-ripples removed?

6) Histological verification should be shown.

Please see individual reviews below for details and specific recommendations.

Reviewer #1 (Recommendations for the authors):

The primary finding of this study is that it was possible to predict the extent of exploration of the anxiogenic area by using the neural activities of the ventral hippocampus (vHP) before the rat enters such an area (i.e., the open arm) (Figure 5). However, the authors did not provide detailed neural and behavioral data to support their arguments. First of all, to verify the electrophysiological data, they need to report the basic firing properties of single-cell activities and the representative histological photomicrographs showing the electrode tips to verify whether the electrodes were indeed targeted the pyramidal cell layers in the vHP (e.g., the overall distribution of the spike width and mean firing rate during CC, CO, CT condition, raw spiking samples to show cell's recording stability, brain sections with thionin staining, etc.). In addition, the authors need to clarify how pyramidal neurons and interneurons were distinguished from each other (e.g., using the mean firing rate and spike width?), and how they removed sharp-wave ripple-associated spikes (e.g., using a speed filter?). Second, before providing results of principal component analysis (PCA) and support vector machine (SVM), they need to verify that the mean firing rate before entering the open arm was positively or negatively correlated with the exploration types (i.e., proximal and distal exploration). Such correlation analysis may make the results of PCA and SVM more substantial.

Next, the current version of the manuscript lacks detailed behavioral data (e.g., velocity and position differences between proximal and distal exploration trials before entering the open arm), which may raise the alternative hypothesis that the difference in the neural activities between proximal and distal exploration could result from behavioral differences, not the prediction signals in the vHP. For example, in the proximal exploration trials, rats could be more hesitant and stayed longer near the boundary before entering the open arm than in the distal exploration trials. In contrast, in the distal exploration trials, rats might run toward the rewards in the open arm without hesitation. In that case, it is possible that the difference in neural activities between the exploration types could mainly reflect the difference in animal speed or how long they stayed near the boundary, not necessarily reflecting the animal's intention to explore the anxiogenic area. To address these concerns, the authors need to report detailed behavioral and neural data with respect to the issue. For example, they may need to provide a peri-event time histogram of the animal's velocity and position and spikes in relation to the time of entering the open arm. Alternatively, as they used spike-associated activity controlled by speed via the general linear model (GLM) in Figure 3F-3G and 4D-4E, they may apply this model to this analysis in Figure 5 to control the speed factor, etc, to name a few.

Also, it is unclear which neural firing data were used for the PCA and SVM analyses. The authors said "firing rate of each neuron prior to the open arm ~ (line 478)", but it is confusing which moment they indicated by 'prior.' They need to quantitatively define 'prior' (e.g., activities within seconds before entering the open arm or activities within 10cm from the boundary between the open and closed arm). If position or velocity was different depending on the exploration type, it could be that different place cells might be recruited during the "firing rate prior to the open arm," which might result in distinct neural activities between proximal and distal exploration trials. In addition, they need to report how PCs in proximal and distal exploration were quantitatively separated between two exploration types in the entire session, not only for two sessions (Figure 5A).

In SVM analysis, the authors did not show raw data to demonstrate that the neural activities in proximal and distal exploration trials were properly distinguished through the hyperplane of SVM (Figure 5B). Thus, it is impossible to assess the validity of SVM analysis. The authors need to provide the graph whose x and y axes are associated with the neuronal activities and demonstrate that the hyperplane properly distinguished proximal and distal exploration trials. Moreover, they iteratively computed the performance of the SVM for all possible combinations of neurons and chose the combination that gave the highest performance for further analysis (Figure 5B – 5C). This may result in an overestimation of the results. For example, even if most combinations had low performance, it would be considered a high-performance session if there was only one combination of higher performance. Thus, the authors need to provide the results of all combinations. Also, it seems more appropriate to infer performance using the ensemble data rather than based on a combination of two cells.

Reviewer #2 (Recommendations for the authors):

Related suggestions/comments to the Public Review Weakness points:

Related suggestion to W1.

It would be helpful if the authors could make a clear comparison between the dorsal and ventral hippocampus with regard to anxiety responses and highlight what aspects are unique to the vH anxiety driven cells.

Related suggestion to W2.

It would be helpful for readers to know which subpopulation of cells in vH function as the basis for dynamical remapping of anxiety information.

Additionally, it would be helpful to have a table describing how many neurons were recorded from each animal and from what subregions. In Figure 1B, many red dots are missing the cell layer of the vH, especially in the third panel and readers may wonder where the neural data was actually recorded from.

Other specific points:

In line 251

No PCA descriptions in the Methods section.

In lines 399-403

In total, how many sessions did each animal perform per day?

Error bars are missing in Figure 3B, 3F.

In Figure 4A

The representative 'homogenized' cells # 41 and 110 are confusing as the firing rates in closed area (spatial bins up to 10) seem also 'homogenized'. One would expect to see the cells that are only 'homogenized' in the open area (spatial bins between 10-20), no?

In Figure 5A

What does "n=11" and "n=3" indicate here, animals, trials, or neurons?

In lines 511 and 512

While there are descriptions "Figure S1A, B" and "Figure S1C, D", there are no supplemental figures provided with the manuscript.

Reviewer #3 (Recommendations for the authors):

1. The authors should include in their discussion the results from Wang et al., 2012 and Wang et al., 2015 (PMID: 26085635 and PMID: 23136419). The authors also should discuss Kong et al., 2021 (PMID: 34533133) and Schuette et al., 2021 (PMID: 32958567). Kong found more remapping near the threat, while Schuette found a concentration of place field centers near the threat and a decrease in place field size near the threat. These results were different because they done with dorsal hippocampal cells and different types of threats, but these data must be discussed to put the new findings within the proper context.

2. The authors show that after the cc to co transition there are more cells with peak firing rates in the open area. Prior to the transition, is there any difference between the cells that moved their peak firing rate location to the open area compared to the ones that did not move? Are there differences in prior firing rate, field size, spatial information during cc that predict the cell's remapping in co?

3. Comparing the cells that lost directionality and the ones that did not, was there any difference in these cells after or during the transition? Are there differences in prior firing rate, field size, spatial information during cc that predict the cell's loss of directionality in co?

4. In Figure 3d why do the authors use 'peak location' instead of place field center? What would the data look like with place field center plotted instead?

5. Did the data change in any way across the multiple sessions of recordings? Did the results about coverage, directionality and concentration of peak locations in the open area change across the multiple sessions?

6. Please show the main effects separated by animal sex.

7. Provide examples of real histology photos instead of diagrams.

8. Add experimental details showing for each animal how many sessions in ELM were obtained, how many trials and across how many days.

9. I am having trouble understanding what is plotted in Figure 5c. The legend says "Box plots show median, 25th and 75th percentile". But it is the median of what? What is plotted? Is it possible to plot these data in some other way?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Firing patterns of ventral hippocampal neurons predict the exploration of anxiogenic locations" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and Reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Please see the remaining issues noted by Reviewers #1 and 3 below.

Summary:

This paper is expected to be of interest to systems neuroscientists in the fields of emotion, hippocampal function, and anxiety-related behavior. The authors performed recordings in the ventral hippocampus and show that (1) place fields become concentrated near the open areas of a maze, (2) direction-dependent coding decreases in these open areas, and (3) ventral hippocampal population activity in the closed area can be used to predict how mice explore the open area in the immediate future. These valuable findings provide convincing support for the potential role of the ventral hippocampus in the exploration of anxiety-provoking environments.

Reviewer #1 (Recommendations for the authors):

The authors have addressed most of my concerns. However, there are still some concerns that may need to be addressed (see below).

– (Figure 3A) The authors nicely illustrated single-cell examples in Figure 3 (and figure supplement 1A and 1B) to show broader place fields in the ventral hippocampus. However, when examining the individual cases, I am concerned that the z-transformed population rate maps in Figure 3A may give the reader the wrong impression that most cells in the ventral hippocampus have focal place fields. Furthermore, inhibitory interneurons in the hippocampus also have their preferred firing locations where their firing rates are higher than others (Ego-Stengel and Wilson, 2007, Hippocampus). As the current study didn't differentially analyze putative pyramidal cells and interneurons, it might be difficult to distinguish between activities in pyramidal neurons and interneurons when using the z-transformed rate maps. Therefore, it seems inappropriate to show the population activities using a z-transformed population rate map.

– (Figure 6 —figure supplement 1B) The authors used the averaged speed in the arena spanning 15 cm before crossing the open area to argue that there was no behavioral difference between proximal and distal exploration. However, 15 cm is an arbitrarily determined value, and I wonder if it can serve as a representative measurement to compare animal behavior between proximal and distal trials. This is mainly because they calculated firing rates for SVM analysis from the moment heading towards the open area, not the 15cm before crossing the boundary between closed and open areas. Thus, it might be much more appropriate to compare the speed from the moment heading toward the open area to the end of the closed area.

– Additionally, the authors should include statistical testing in Figure 6 —figure supplement 1B. Based on my observations, the speed of future proximal exploration seems significantly lower than that of future distal exploration in session 5. Along with the results of each session, it might be necessary to pool the data from all sessions and perform statistical testing in order to argue that there was no speed difference between proximal and distal exploration.

– (Discussion) Keinath and colleagues (Hippocampus, 2014) argued that cells in the mouse ventral hippocampus showed more spatially selective firing patterns when aversive odor (i.e., predator's urine) was introduced in the open arena. This result contradicts the current manuscript because adding an anxiety factor seemed to decrease spatial firing characteristics in the current study as opposed to the results of Keinath et al. (2014). If the authors explain the potential factors of why there was a contradiction between Keinath and colleagues and the current study, it will be helpful to understand the importance of the ventral hippocampus in emotional information processing. Additionally, if the authors explain why the firing fields became larger but not smaller in anxiogenic space in processing emotional processing, it can give readers a clue about how the ventral hippocampus is involved in processing emotional information.

Reviewer #2 (Recommendations for the authors):

After carefully evaluating the revised manuscript and the authors' response to my previous comments, I am pleased to report that I am satisfied with the changes made by the authors. The authors have addressed all the concerns and/or issues raised in my previous review and have made significant improvements to the manuscript.

The revised manuscript, with the additional supplemental materials, now presents a clear and concise argument, and the additional data analysis, especially on the single unit analyses and presentation has been significantly strengthened.

The author has also provided additional information (incl. Data Availability) and clarification where necessary, which has improved the quality of the manuscript.

Overall, I recommend that the revised manuscript is now suitable for publication in eLife.

Reviewer #3 (Recommendations for the authors):If the authors used only male mice this fact must be stated in the abstract.

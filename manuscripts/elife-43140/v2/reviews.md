# Peer review - Round 1

Editors:
- Sachin Deshmukh, Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43140.sa1](https://doi.org/10.7554/eLife.43140.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

It is important to understand how path integration errors are corrected in MEC. Your demonstration of cue cells in MEC suggests an interesting mechanism complementing border cells in performing this task.

Decision letter after peer review:

Thank you for submitting your article "Visual cue-related activity of cells in the medial entorhinal cortex during navigation in virtual reality" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors use a combination of tetrode recording and calcium imaging while mice ran on virtual linear tracks containing visual cues (towers) on either side to describe a novel cell type in the superficial layers of medial entorhinal cortex (MEC), which they call "cue cells." Correlation based measures using the spatial firing rate of the cells and a landmark cue template were used to classify cells as "cue cells" that respond by firing repeatedly at every landmark. Recordings in two-dimensional open-field environments revealed the cue cells were also conjunctively encoding other, previously characterized, features of cells in the mEC including the presence of borders (border cells), firing in a regular triangular spatial lattice pattern (grid cells) and the animals heading direction (head direction cells, ~50% of cue cells had some orientation tuning). The results were viewed by all reviewers as novel and significant.

However, there are multiple significant concerns, as the manuscript stands, listed below, which the authors should be able to address in the allotted time. The major issues concern the shuffling procedure used to generate control distributions for cue scores, missing details regarding statistics, and other analyses that need to be modified to better control for spatially selective cells that are not anchored to cues.

Essential revisions:

1) The circular permutation procedure undertaken to form a control data set is inadequate for many of the analyses it is used in. Circular permutation destroys spatial selectivity. When the question being addressed is whether the observed spatial selectivity is correlated with the landmark locations (rather than being random), the control distribution of correlation coefficients needs to be obtained using a randomization procedure maintaining spatially selectivity while randomizing the relative positions of the place fields and the objects. A control distribution of correlation coefficients without spatial selectivity, like the one used here, is likely to be more tightly clustered around zero than a control distribution of correlation coefficients obtained from spatially selective (but randomized) data, thus allowing more false positives. One easy way to do this is to randomize landmark locations while keeping the ratemap unchanged. This will work for detection of cue cells, but for some analyses (e.g. the sequence analysis), shuffling the place fields within a ratemap would be a more suitable shuffle.

2) Some of the findings appear to follow tautologically from the definition of the cue score, which correlates firing patterns to a template that matches the locations of the visual cues. a) The distribution of this score appears uni-modal and the authors them pick out one end of the distribution. Are the cue cells really then a discrete population? Following this, are the cue locations really special, or does the template just pick out cells that fire near the cues from amongst a population that uniformly spans the environment? Can you compare the number of cells you would identify with a randomized cue template to the number of cells picked up by the cue template? The cue-score method picks out cells with positive correlations to the cue template. Are there cells with significant negative correlations? ("anti-cue cells")

b) Do cells that fire near the visual cues respond more to the removal of visual cues than cells that fire away from the visual cues, or do all cells lose their spatial tuning in the cue-removed condition?

c) Can the fact that the sequence is repeated at each cue be explained by the fact that the cue template looks for cells with a fixed spatial offset from each cue? One way to control for this would be to identify cells based on one cue only, and test whether the sequence repeats at the other cues. Alternatively, a cue score could be developed that allows the cue template to move independently at each cue. This would be a more convincing test that cells really do have a fixed offset from each spatial cue.

d) What is the distribution of Left-Cue scores for Right-Cue cells and vice versa? Is it really "either/or", or is there a continuum of cells that respond to combinations of left and right cues?

e) "For each environment, we found the activity of all cue cells was best aligned to the center of the cue rather than the start or end of the cues". If the place field size is proportional to the cue size, this will automatically follow. Start and end would be displaced differentially with respect to place field center while the cue center would be the average of the two. The method used for generating cue scores (subsection “Scores for cells in tetrode data”) generates higher scores for cells with field sizes matching cue sizes (over cue cells that have cue independent field sizes), making this analysis circular. Why not use the peak correlation between the cue template and the firing rate map with the smallest absolute shift from zero as the cue score, instead? That will eliminate this confound.

3) Detailed statistics need to be provided at multiple places. For example, the subsection “Cue cell pairwise activity patterns” mentions Pearson correlation coefficients of 0.3 and 0.13. The authors argue that "This suggests that the spike timing relationship between cue cell pairs is present only when cues are present and thus when these cells are driven to be active in a sequential manner by locomotion past the cue." This will hold true if the two coefficients are significantly different from one another, and the coefficient of 0.3 is statistically significantly different from 0. 2. "*p ≤0.05. **p ≤0.01. ***p ≤0.001. n.s. p > 0.5. Student's t-test. Error bars: mean ± SEM.": detailed statistics including sample size, p values, t-statistics, means and STDs need to be reported in the main text. The journal guidelines state "Report exact p-values wherever possible alongside the summary statistics and 95% confidence intervals. These should be reported for all key questions and not only when the p-value is less than 0.05."

Have the authors corrected for multiple comparisons wherever required?

4) The authors report recording up to 301 cells from a single tetrode (Figure 1—figure supplement 1; including 88 cue cells and 93 grid cells; "Recordings were performed on four animals over two months."). Were repeat recordings from the same neurons on consecutive/multiple days identified and eliminated? How? If they were not eliminated, all the reported statistics suffer from inflation of degrees of freedom. Can the authors comment on this?

5) What are the running speed profiles of the mice? Did they tend to slow down near the visual cues?

6) "In layers 2 and 3, we consistently observed that anatomically adjacent cue cells (physical distances around 30 μm) showed more similar spatial shifts, whereas the relationship was more varied if cue cells were further apart (Figure 7G-N). The similar cue responses of adjacent cue cells suggest that they may share similar inputs or be connected."

Do the cross correlations of neighbouring cells (on the same tetrode) maintain the peak at 0ms in B if they had peak at 0ms in A? If not, the two observations with tetrodes and imaging would contradict one another. In general, the claims made in G-N are rather weak. Authors should consider excluding them.

The 'micro-organisation' relating physical separation to spatial shifts in responses relative to cue location is seen restricted to anatomically adjacent cue cells: is there any danger that this reflects contamination/poor localisation/diffusion of light from neighboring sources?

7) One reason for the more specific apparent correlate of firing in the VR track versus the open field might be that the viewing angle is important and this is not systematically sampled in the open field. Do the mice run in both directions on the VR – if so, do the cue cells fire at a similar cue-angle? Does this relate to the observation that place cell firing becomes more directionally modulated in VR than in real open fields (presumably because of the greater influence of vision in visually-generated VR; Acharya, Aghajan et al., 2016; Chen, King et al., 2018). In the comparison to known cell types, might these cue cells be related to landmark-vector cells (Deshmukh and Knierim, 2013) or object-vector cells (Hoydal et al., 2019), or egocentric responses recently reported in lEC (Wang et al., 2018)? Do the cue cell responses depend on the wider context – need the mouse be running (vs. passive viewing) to see firing? To what extent do cue cells fire similarly across VR environments or do they 'remap'? (this is not entirely clear from Figure 1).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Visual cue-related activity of cells in the medial entorhinal cortex during navigation in virtual reality" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers remain positive about the overall importance of these results.

However, although some of the concerns were adequately addressed during the first revision, some major concerns that were raised in the first round of review remain. Moreover, a number of new concerns arose from the revisions. Still, reviewers are confident that the authors can easily address these remaining concerns.

Essential revisions:

Duplicates removed database in Author response image 7, which is used throughout the paper uses spatial firing rate correlations > 0.95 as a threshold for discarding cells as being duplicates. This threshold is unreasonably high, as even stable place cells recorded in consecutive sessions in the hippocampus often have substantially lower correlation coefficients, especially in mice (e.g. Kentros et al., 1998, Figure 3). This means that the duplicates removed database is likely to still have an unreasonably high number of duplicates.

The authors should show the tetrode lowering database figure shown in Author response image 7 at least as supplementary data. They must also include the tetrode lowering database stats and aggregate figures for other analyses using tetrode data, including responses to environmental perturbations, sequences, pairwise correlations etc. to convince the reader that the significance of the patterns reported is not grossly overestimated by inflation of degrees of freedom caused by the inclusion of duplicates in their dataset.

In the revised manuscript, it is no longer clear how many animals the data were collected from, and how many neurons of different types were contributed by each animal. The animal and tetrode – wise breakdown of neurons in the tables included in the previous version are essential. Tables showing number of units of different kinds recorded from each tetrode in each animal have been eliminated from Figure 1—figure supplement 1. They should be put back, with numbers for both duplicates removed database as well as for tetrode lowering database.

Related to this, it is not clear how many animals contributed to the new data shown in the new Figure 7. Hence, it is impossible to figure out if the reported results are reproducible across animals. Please mention number of animals included for each analysis/figure in the Results.

"In Region A, there was a spread in the temporal shifts for pairs of cue cells and these temporal shifts were correlated for the two tracks (Figure 5C left, Pearson correlation = 0.52, p=9×10-5). However, the temporal shifts in Region B of the two tracks were less correlated: while a similar spread of temporal shifts was observed when cue cells were recorded on the with cues track (plotted along the x-axis of the bottom right panel in Figure 5C), most cue cell pairs did not have a correlated phase in the relative spike timing when cues were missing (plotted along the y-axis of the bottom right panel in Figure 5C right, “correlation not significant”). The fact that the spike timing relationship between cue cell pairs is maintained only when cues are present suggests that these cells are driven to be active in a sequential manner by locomotion past cues."

Correlation coefficient and p value for region B needs to be included, as requested in the previous review – stating "correlation not significant" is not sufficient. Furthermore, to make the claim that their data suggests that "cells are driven to be active in a sequential manner by locomotion past cues", the authors should demonstrate that the slopes in region A and B shown in Figure 5C are significantly different from one another.

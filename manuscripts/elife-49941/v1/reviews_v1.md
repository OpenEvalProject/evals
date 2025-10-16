# Peer review - Round 1

Editors:
- Tom Smulders, Newcastle University United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49941.sa1](https://doi.org/10.7554/eLife.49941.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is an intriguing paper that identifies novel brain areas involved in influencing the copying accuracy of birdsong. The paper identifies areas not previously linked to song learning, hence opening up new future investigations. Together with the extensive response to reviewers, this paper is an extensive resource for the birdsong community.

Decision letter after peer review:

Thank you for submitting your article "In vivo assessment of the neural substrate linked with vocal imitation accuracy" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor and Barbara Shinn-Cunningham as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study represents a very interesting new approach in identifying brain areas involved in accurate copying of tutor songs by male zebra finches. Using a whole-brain data-driven structural MRI approach, the authors identify a number of brain areas that either change alongside the improvement in copying as the birds mature, or structurally predict how well a bird will copy the tutor's song on an inter-individual level. Interestingly, none of these structures are in the traditionally-identified song control circuitry (although many are in areas related to auditory processing).

All three reviewers thought this was an interesting paper, but all three would like to see some clarifications of particular points and/or some re-analyses to drive home the message even more strongly. Below, I list the revisions that are required to improve the paper for publication in eLife.

Essential revisions:

Most of the essential revisions relate to the way the data analysis was performed and/or how the data were presented and discussed. No additional experiments are required.

1) A bit more detail on the birds and their experiences would be welcome. Clearly, some of the birds were exposed to the same tutor. But were some of the juveniles the offspring of the same parents? It would be helpful to know to what extent this information could be used to control for innate learning biases. Also, we are not requesting additional experiments, but it would have helped interpret the early left NCM FA values and learning outcomes if the juveniles had not been exposed to a tutor until after 30 days, to separate effects of the tutor song from innate properties of the birds.

2) MRI analysis 1 – Repeated measures: The authors used a two-step approach: first they ignore the fact that some of their measures were coming from the same individuals to perform their statistical analyses at the voxel level, and then, based on these results, used a ROI-based approach to take into account the repeated measures. We think that this approach is flawed because the selection of the voxels to determine the ROI is inaccurate (since each data point was considered to correspond to one subject). The result section should not present results where the repeated measure aspect of the dataset is not taken into account (first section of Results). We are aware that SPM does not currently allow analysing longitudinal datasets where the number of measures is not the same for all the subjects (as this is the case here). It seems that the authors have two options: (1) either they discard the 2 subjects for which they only have 3 data points and use a within-subject design for balanced designs in SPM; (2) or, even better, keeping their 14 subjects, they use the SwE toolbox (http://www.nisox.org/Software/SwE/) that seems to be able to handle unbalanced longitudinal datasets. Mean centering should allow the distinguishing between within- and between-subject effects (cf Guillaume, Hua et al., 2014, NeuroImage, 94).

3) MRI analysis 2 – explaining for non-experts: The manuscript falls short for a general audience in detailing how various structures were identified and assigned significance. One issue relates to the requirement for clusters > 40 contiguous voxels. What is the diameter of a sphere containing that many voxels? And does this volume threshold exclude smaller song nuclei, such as HVC, LMAN, DLM, or Avalanche? Finally, it would help a general reader to report the scale of FA, rather than just reporting absolute values.

4) MRI analysis 3 – correcting for multiple comparisons: The authors need to choose how they want to correct for multiple comparison in their voxel-based approach (voxel wise or cluster wise). If the authors choose a cluster-based approach, they should justify the first p value threshold used to obtain the clusters (recent published recommendations about how to choose these thresholds should be followed and mentioned). If they choose a voxel-size approach, they should justify their minimum cluster size.

5) MRI analysis 4 – Positive controls: A potentially noteworthy feature of the current study is that the only significant anatomical changes were detected in regions outside of the classical song system. But numerous studies have shown that the structure of various song control nuclei (HVC, RA, Area X) changes markedly over the period in which these measurements were made (increasing in volume between 20 and 60 days, and increasing in myelination between 20 and 100 days, eg). Further, some early structural changes in the song system (spine density and dynamics in HVC) are correlated with copying outcome. I would be more confident in the current results if the authors could show that their method is sensitive to structural changes within the song system that are known to occur during development, even (or perhaps especially) if these changes are not correlated with song learning outcomes.

6) Relating MRI to song learning – age: Please clarify how age is controlled for or used in the analysis. Do the authors just go from the assumption (based on the data, maybe) that copying accuracy increases with age, and that the two variables are therefore inextricably confounded? Or is there a way to separate maturation (age) effects from changes related to copying accuracy? It will also make it easier for the reader to understand statements like "However, individual improvements in song learning resulted in a lower local volume of the CM (left: p=0.0126; right: p=0.0075; Figure 3D)", which now may be difficult for some readers to assess, because age is not visible in the figure.

7) Relating MRI to song learning – representing changes in copying accuracy; This study includes multiple measures, using Fractional Anisotropy in Figure 2, and local volume in Figure 3. In both figures we see correlations between song similarity and MRI measure, but we do not see the time course of song learning. Therefore, statistical claims such as correlation between improvements in song learning and a lower local volume of the CM cannot be judged visually from the data as currently presented. To address this, authors should present figures, similar to Figures 2 and 3 but instead of showing the similarity vs MRI, present the similarity gains vs. MRI. For example: for each bird, you present similarity (day 90) – similarity (day 65) vs. MRI on day 90. This will allow the reader to judge visually (and not only statistically) if any of the MRI measure correlates with learning. In addition, it would be nice to have a figure illustrating this statement (e.g., showing similarity gains vs. right NCM activation): "Surprisingly, a small cluster in the right NCM displayed, in addition, a significant repeated-measures correlation."

8) Relating MRI to song learning – dichotomizing copying accuracy: Regarding the correlation between MRI properties at days 20/40dph and learning accuracy, the authors should justify why they dichotomised song accuracy (good vs. bad learners) rather than simply taking the% of song similarity. Why don't the authors test whether MRI properties at day 20 (or 30) allow predicting vocal learning accuracy at day 200 (expressed as% of song similarity)?

9) Discussion – mechanisms: The authors are careful to note the lack of explanatory power in these correlative measurements, which is good. But they need to say more about how they think these developmental changes might relate to learning. What are we supposed to make with the finding that the FA changes over development when there is no link to what that value represents in the songbird's brain? Going back to an earlier point, it would help to see that this method can detect FA changes related to increased myelination of the song system, which is dramatic and presumably should generate a large signal. That said, the authors need to discuss in depth how such changes (decreased volume, increased FA) could be related to better learning.

10) Discussion – Novelty: Prior studies have shown correlations between NCM functional properties and song learning outcome, between CM functional properties and vocal error detection, and between VP and song copying. A strong feature of the current study is that it provides independent validation that these regions correlate with song copying, but given the earlier work, the current findings are not wholly novel even if they are useful contributions. On the other hand, the tFA result is entirely novel but what this fiber tract is needs to be more fully described. The authors are quick to link it to the projections from the basorostral nucleus, but we are uncertain whether such a precise assignment can be made with these methods. Is this distinct from other fiber tracts in this general region, including parts of the occipitomesencephalic tract? Showing some conventional histology of the tFA in relation to the MRI data would be helpful here. And the VP finding is quite timely, given the recently emerging evidence of the role of this structure in song learning. Further, VP is the only region that showed significant correlations in both FA and volume with learning. Perhaps the manuscript should highlight the tFA and VP findings more strongly, while casting the NCM and CM data are more confirmatory in nature, to emphasize novelty.

[Editors' note: the decision after resubmission follows.]

Thank you for resubmitting your article "in vivo assessment of the neural substrate linked with vocal imitation accuracy" for consideration by eLife. Your revised article has been evaluated by a guest Reviewing Editor and Barbara Shinn-Cunningham as the Senior Editor.

We really appreciate the time you have put into writing long, thought-out responses to each of the reviewers' comments.

However, looking at the revised manuscript, it looks like very little has changed. The reasons the reviewers make these constructive comments is not so that you can explain things to them, but so that you can change the manuscript in such a way that readers with similar questions to the reviewers would find their questions already answered in the manuscript. Thank you for the changes you have already made.

I am therefore requesting that you please incorporate the responses you have made to the reviewers into the revised manuscript. Once I receive this revised manuscript, I will send it out for a second review with regards to the technical side of the MRI protocols and analysis methods.

I will here summarize which changes still need to be made to the manuscript itself:

1) Thank you for adding the table to the Supplementary materials. Could you please also add a few sentences to the Discussion laying out what your data can and cannot distinguish between, and what the obvious next studies would be to work out those distinctions? You have done this in the rebuttal, so it should not be difficult to add a bit to the Discussion.

2) This is probably the most important change. Since you have run the analysis now in a more appropriate manner, we feel that you should replace the original analysis with the new analysis, not just add the new analysis as an addendum to the paper. If the new analysis changes the outcomes of the study, then the Results and Discussion should be changed accordingly.

3) Thanks for what you've already added. However, I think you misunderstood the main question asked by the (non-MRI specialist) reviewers here. They just wanted to know how big those clusters were in real life, and how this compares to known song structures. You have clearly done all the calculations for the rebuttal. Now please incorporate that information also into the manuscript.

4) Does adding "peak voxel" to that sentence clarify the reviewers' question? I am not expert in this area, so cannot judge this. I will assume for now that it does.

5) Please do add the additional song control structure data to the manuscript. Other readers, thinking the same as the reviewers, will appreciate that the method can detect changes over time, as should be the case in the song system, but these do not correlate with copying accuracy. You may also want to refer to your 2018 paper when discussing these extra data.

6) Every reader is going to wonder whether the correlation between changes in MRI signal (FA, etc) and song copying accuracy is just a side-effect of both changing with time. So you have to address this in the analysis. If it is, as you say, purely a question of brain behaviour correlations, and age does not mediate this relationship, then show that. If it turns out that age is a major mediator, and removes the correlation between brain and behaviour, then please discuss why the correlation does exist in some brain areas and not in others, which also change with age.

7) This point is related to point 6: by losing time, we don't know whether the main reason for the correlations is that both change over time in a similar way, or that the copying accuracy actually explains the "noise" in the trend over time. So it would be good if the authors could think of some way that allows readers to understand the distinction between parallel trends over time and (not-age-related) correlations between brain and behaviour.

8) Please do add Figure REB8 to the manuscript, wherever you see fit, and add reference to it in the Results.

9) Thank you for a good explanation. Please add some of it to the Discussion, so all readers can benefit from this insight.

10) Can you add something about the Hamaide et al., 2017, paper and how you have done your best to identify the tract (and VP) as best as possible in the Discussion? I am happy for you to keep the emphasis as is on the three main points (if consistent with the new analyses, see (2) above).

a) Please add this justification to the manuscript (in a much shorter form, of course)

b) If this is really relatively uncommon, maybe add another half sentence about why Ashburner and Ridgeway recommend this.

Thank you for the rest of the changes you have already made.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Firstly, I would like to apologize for how long this has taken. The holidays got in the way of finding and selecting an extra MRI-expert to give an opinion on the dispute between yourself and the initial MRI expert among the reviewers.

We have now received this second opinion, and it can be found below. The evaluation has been overseen by a guest Reviewing Editor and Barbara Shinn-Cunningham as the Senior Editor. The reviewers have opted to remain anonymous. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This extra review refers specifically to point number 2 in the previous decision letter. I would like to emphasize that all the other points still stand and would need to be acted upon in order for the paper to be accepted. However, I believe that for most of them, this is not difficult. In addition, because the reviews and the response to reviewers will be published alongside the manuscript, I don't mind if you refer in the main text to the response to reviewers to save space. However, it is crucial that such references are in the main text, because many readers will not scroll down to the reviewers' comments and the responses to such.

As for point number 2, where we asked you to replace the original analysis with the new SWe based analysis, we have now asked an independent expert for their opinion. Their response is as follows:

Reviewer #4:

The authors rely on the correlation analysis method to identify unique brain regions (voxels) in the songbird brains, of which the FA, an integrated/vectorized readout of the diffusion-based MRI signal, varies to specific song learning behavior during development. Previous reviewers raise the concerns on the statistic validity to specify the unique brain regions, in particular, the "circular issue" to define the ROIs based on the selected voxels (beyond a significance threshold).

From the revised manuscript, similar brain regions were highlighted using the new analysis method, which is encouraging. However, the authors have to assign smaller voxel sizes to preserve individual voxels above the statistic threshold, which may break the compensatory/correction rules for multiple comparison problems. This issue has been well reported in the literature and is faced by neuroimaging researchers routinely. In most cases, it is due to the rather small sample size to present the population given a certain size of variability. In the animal MRI field, it is a known problem.

The authors do observe some reliably detected spatial patterns in the songbird brains (n=14). One of the challenges for the voxel-wise analysis is to precisely register the brains from individual subjects to the same template. The mismatch of voxels across subjects leads to pseudo-negative statistic estimates, but if a smoothing step (averaging voxels) is applied, it may reduce the potential FA value differences across different conditions. It is a dilemma.

Here, I suggested two tentative ways to deal with the problem:

An intriguing observation is the symmetric observation of the brain regions (left and right brain nuclei are identified and voxel counts are provided in tables). One possible way to deal with the statistical issue is to create a mirror image for each subject. Then, the authors can just focus on the one-side hemisphere to redo their analysis (hopefully with sufficient power).

The second way is to define the ROI based on the songbird anatomy, but not by the voxel-wise analysis results. If the atlas-ROI can show specific correlation features, it can serve as an alternative way to support the voxel-wise results.

Overall, I see that the main results are convincing and novel. The authors should apply the correct statistical analysis strategy to retrieve their major discoveries in a more convincing way.

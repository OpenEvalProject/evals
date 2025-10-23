# Peer review - Round 1

Editors:
- Matthew J Brookes, University of Nottingham , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23608.031](https://doi.org/10.7554/eLife.23608.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Threat of shock increases excitability and connectivity of the intraparietal sulcus" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Van Essen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Krish Singh (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Your paper was assessed positively by all three reviewers, with all three saying that this is a valuable addition to the literature and of broad scientific interest. In particular, the multi-modal aspect was well received. I am therefore happy to provisionally recommend publication, however a number of significant revisions must be successfully carried out first. On receiving your revised manuscript with explanatory comments, the Reviewing Editor will decide whether the manuscript needs to be seen again by the reviewers.

Essential revisions:

For fMRI, all of the technical concerns raised by reviewer 2 must be addressed comprehensively. These are copied in full below.

For MEG, both reviewers 1 and 3 suggest that a functional connectivity analysis would be a better candidate for comparison with your fMRI results than the current approach. I therefore strongly recommend that you undertake such analyses; here, a key confound is signal leakage between source space regions and an appropriate correction method must be employed. Though multiple schemes are available I would suggest using the approach published by Colclough, Brookes, Smith and Woolrich, 2015. (referenced by reviewer 1) but perhaps applied to a denser parcellation (e.g. the AAL parcellation). Again for completeness the reviewers comments are copied in full below.

Finally, a quantitative analysis of the similarity of the regions identified by MEG and fMRI must be given.

Reviewer #1:

The paper by Balderston et al. describes a study in which both fMRI and MEG are used to investigate the neural correlates of anxiety. To this end, a threat of shock paradigm is employed to increase anxiety in subjects; this increase is then assessed behaviourally in multiple ways. Both fMRI and MEG data are acquired during the paradigm and analysed in an unbiased way; briefly, in fMRI an 'all-to-all' connectivity approach is used to measure connectivity among voxels. In MEG, data are analysed in multiple frequency bands and changes in oscillatory power between task blocks (safe versus threat of shock) characterised. The interesting result is that both the fMRI connectivity analysis and the α band power assessment both implicate the intraparietal sulcus as a key hub in processing anxiety.

Overall I believe this to be a very interesting and exciting paper. The primary finding is not only impactful for basic science but may also, potentially, have significant clinical relevance. The paper is well written and the analyses, for the most part, solid. However I do have a number of suggestions that I think would improve the paper.

Major comments

1) It is assumed that the fMRI and MEG responses occur in the same location, however this was never analysed quantitatively. The distance between the fMRI cluster and the MEG peak location should be quantified. What are the chances that this difference could occur by chance?

2) It is not made clear in the Introduction why complementary analysis is not used – e.g. the MEG is used to assess oscillatory changes whereas fMRI is used to assess connectivity. Why? I realise of course the links that have been made between oscillations and connectivity but this is not well discussed in the paper (I personally didn't find the relation to the simultaneous EEG-fMRI literature very convincing). Why not just do a standard GLM approach to the BOLD analysis to get regions of increased BOLD response during threat and compare that with changes in α oscillations? In short, the analysis pipeline used should be better motivated.

3) Related to the above question, I found the MEG analysis quite limited. Wouldn't it have been better to take advantage of the huge steps forward in MEG connectivity methods that have been made recently and employ one such approach to measure whole brain α band connectivity – and then compare this to the fMRI connectivity. Its true that you couldn't do this at the voxel level spatial scale but with a brain parcellation it should be easily possible. See papers by e.g. Colclough, Brookes, Smith and Woolrich, 2015 or O'Neill et al., http://iopscience.iop.org/article/10.1088/0031-9155/60/21/R271

4) I felt there should be more justification for looking at the α band, which seems to have been chosen specifically, with the other frequency bands treated as an afterthought. Given the apparent close links between β oscillations and functional connectivity why was the β band not chosen? Again just saying that α was the strongest signal at many sensors didn't really convince me.

5) Can the authors give some explanation as to why the α response was lateralised?

Reviewer #2:

General

This study is a nice example of an investigation into neuronal mechanisms of anxiety that uses two different complementary modalities. However, some of the fMRI analysis approaches need further investigation to ensure that the results were not driven by noise, and the manuscript is longer than necessary in some places.

Major comments

1) The within-network results do not pass multiple comparison correction and do not add much to the story. I would therefore suggest that the authors remove these results. In general, the manuscript should be shortened. Specifically the Discussion would benefit from being more concisely written, and the Materials and method could also be reduced (specifically the subject numbers and the 'on the day of the appointment…' text).

2) Was there a difference in motion parameters between the safe and threat blocks in fMRI? If so, this could lead to a shift between short-distance and long-distance connectivity, which could drive the results. The scrubbing that was performed most likely avoids this possibility, but it would be of interest to present the difference in motion parameters, and to potentially run further analyses to explicitly exclude this possibility (for example, by selecting periods or subjects in which the motion was matched between the two conditions).

3) How many time points were removed during scrubbing, and was there a significant difference between the safe and shock blocks for this? If so, the difference in power could bias the results, and it would be worth excluding this possibility by matching the number of timepoints included in shock and safe blocs (within participants).

4) The change in global connectivity during the shock period could occur as a result of the actual shock stimuli that were not present in the safe periods. I know the HRF responses to shocks and button presses were modeled and removed, but this may not capture the changes in functional connectivity resulting from shock stimuli. Would it be possible to repeat the analysis using only shock blocks that contained zero shocks to ensure that this is not driving the results?

5) Cluster-based corrections with an initial cluster forming threshold above 0.001 have been shown to suffer from inflated false positives (Eklund et al., 2016). The authors should at least point this out in the limitations, and should ideally repeat analyses using the latest guidelines.

6) The methods used in this study are described as unbiased and multimodal, which is a strong statement to make given that some of the whole-brain statistics might suffer from a false positive bias, and the different modalities are analysed separately, rather than in a joint multimodal approach.

Reviewer #3:

I really enjoyed reading this paper, which is a valuable contribution to the field. It uses a multi-modal approach of combining fMRI and MEG to reveal changes in both connectivity across the brain (using fMRI) and oscillatory power changes (using MEG) while participants were either in a state of 'Safe' or 'Threat'

To me the results are interesting both in terms of probing the neurophysiological underpinnings of threat/anxiety but also the relationship between fMRI and MEG measures of brain function.

The methods are thorough and well-executed and reveal a good understanding of the state-of-the-art in fMRI and MEG analyses. However I think more could be done with the MEG data (see my comment 1 below).

The paper is well-written and readable and the authors nicely discuss the weaknesses of their approach.

Here are my main comments:

1) It seems as if there is a missed opportunity here in terms of directly comparing connectivity measures in fMRI to those extracted with MEG (albeit at the group-level). Using a sub-sampled atlas approach (say the AAL atlas) the authors could easily compare 'GBC"-type connectivity matrices extracted with fMRI with those extracted with MEG, either using amplitude-amplitude coupling within frequency bands or phase-phase coupling. There are several recent papers using this approach, so it seems odd that the authors did not do this.

2) It is not absolutely clear in the Abstract/Introduction that when the authors talk about neural activity and connectivity in the IPS, they are really talking about haemodynamics measures (i.e. FMRI). This should be made clearer.

3) When presenting the fMRI-GBC (for example in Figure 3) I think it would be useful to show the spatial distribution across the brain of the connectivity measure i.e. after summing across rows but before global summing across the brain. This would be a companion figure to Figure 4, which shows the voxelwise difference in connectivity strength between Threat v. Safe. Based on my comment 1 above it would be great to see similar visualisations based on frequency-specific MEG connectivity maps.

4) In the MEG analysis, it looks like some trials are rejected if contaminated with artefacts. I just wanted to check that the statistical tests performed later (between Safe and Threat) properly account for differing number of trials.

5) In the MEG analysis, did the authors check that there was no difference in head movement between the Safe and Threat blocks?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Threat of shock increases excitability and connectivity of the intraparietal sulcus" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

We thank the authors for their careful consideration of the comments of all three reviewers, and for the extra analyses that have been undertaken. The paper is much improved as a result of these changes and is now close to publication. However, a few points remain to be addressed.

1) I consider the conjunction map, provided in the response to reviewers, to be critical to the paper and I would very much like to see this in the main paper, perhaps added to Figure 7.

2) Its rather a shame that the MEG connectivity analysis didn't work, but nevertheless I thank the authors for attempting it. I wonder however if some extra clarification could be given: What frequency band was connectivity computed in (sincere apologies if I missed it)? I assume α? I'm also unsure as to what is meant by "we then computed the Hilbert transform using a 500 ms sliding window"? The Hilbert transform shouldn't need a sliding window – when undertaking this analysis we usually compute the HT over all time? Please clarify why this was done. Could the authors please show the MEG adjacency matrices for the safe and thread blocks independently, as well as the difference? This would allow the reader to confirm that the two separate matrices look sensible (one expects large occipital connectivity in the α band, see e.g. Hunt et al., 2016). Finally, given the strong finding of MEG connectivity in the β band, I would like to see the connectivity analysis attempted in this band. I of course read the authors argument that "one might expect a high degree of stationarity in coherence of the β oscillations across time" but I disagree, specifically because multiple papers (e.g. O'Neill et al., 2015; O'Neill et al., 2016; Baker et al., 2014) show that, in fact, β band functional connectivity is highly dynamic.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Threat of shock increases excitability and connectivity of the intraparietal sulcus" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior editor) and the Reviewing editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

I thank the authors for going to such lengths on the MEG connectivity analysis. However, something has clearly gone wrong here in the analysis.

By my assessment of the adjacency matrices presented, the case for the α and β bands look virtually identical. However this should not be the case (again see Hunt et al, 2016). It is quite hard for me to judge the spatial signature of connectivity as, unfortunately, in the pdf version the figure quality is too low resolution to read the region names on the axes. However, these matrices do not look correct to me and I would urge the authors to find out why.

In their response, the authors have suggested that they use blocks of only 2 seconds of envelope data. However they also apply downsampling prior to connectivity estimation. This to me seems silly – why apply the downsampling if you have such short blocks. It is well established that connectivity works without the downsampling so perhaps removing that step might improve the adjacency matrices. I also don't understand why such short data setments were used when in fact the blocks are quite long. Why not just try using the whole block?

I remain enthusiastic about this article, but I maintain that the MEG connectivity analysis has not yet been properly carried out. I would want to see this estimated reliably (or a concrete argument on why it cannot be undertaken) put forward before recommending publication.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Threat of shock increases excitability and connectivity of the intraparietal sulcus" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior editor) and the Reviewing editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

I would like to thank the authors for their attempt at addressing my concerns. I'm pleased that the authors were able to spot errors in their pipeline (use of incorrect spatial filters) although it does appear that the major difference came from the down-sampling, as suggested in my previous review. Downsampling over such a small time window is obviously incorrect so these analyses should now be discarded.

Unfortunately, the adjacency matrices still don't look right – without seeing them plotted on a brain it's hard to judge exactly where the primary pathways of connectivity are (and I still can’t read the labels clearly in the pdf). As I have said previously, the highest connectivity in the α band should be in the occipital lobe whilst the highest connectivity in the β band should encompass bilateral parietal and occipital connections alongside tempero-parietal and fronto-parietal networks (again as in Hunt et al, 2016). In fact this does not seem to be the case. In what the authors have provided the α network looks like pure noise. There is clearly some structure to the β band connectivity matrix although this doesn't really look like one would expect. So I strongly suspect something is still wrong with the analysis.

Without looking at the data directly it’s hard for me to judge but I suspect that the problem is the short time windows (unless there are other more basic errors (similar to the incorrect spatial filter) which the authors have not discovered). It is known that a reasonable amount of data is required to make MEG connectivity analyses work reliably (Luizzi et al., Optimising experimental design for MEG resting state functional connectivity measurement, NeuroImage 2016) and perhaps this is the reason the adjacency matrices look so poor. In the light of these failed attempts, I suggest that a paragraph is added to the Discussion stating that MEG connectivity analysis would have been a useful means to probe these data; however the study design was poorly set up to make such analyses work.

Please note that this must now be your final attempt to satisfy the Board.

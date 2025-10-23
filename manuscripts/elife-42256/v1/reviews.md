# Peer review - Round 1

Editors:
- Michael Breakspear, QIMR Berghofer Medical Research Institute Australia

Reviewers:
- Leonardo L Gollo, QIMR Berghofer Medical Research Institute Australia

## Review text

DOI: [10.7554/eLife.42256.020](https://doi.org/10.7554/eLife.42256.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Atypical intrinsic neural timescale in autism" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Michael Breakspear as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Leonardo L. Gollo (Reviewer #2); Warren W Pettine (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All reviewers found the paper to be well motivated, clearly written and of substantial interest. No major statistical or design issues were identified. While the reproducibility data sets were laudable, in general all data sets are small to modest in size.

Some great clarity of analysis should be provided and closer linkages to computational work on time scale hierarchies in the brain should be provided.

None of the reviewers ask for substantial new work that could not be undertaken within a reasonable period of time. All requests for revisions are straightforward and are provided from each of the reviewers below.

Reviewer #1:

Atypical intrinsic neural timescale in autism. I previously supplied some feedback to the authors on their original submission. It's a very interesting paper and has been appropriately revised.

1) The between group contrast, ASD>TD rests upon measures that are almost certainly used to estimate the severity of ASD: I'm therefore concerned there is some dependence between the test for finding the clusters (ASD>TD) and the regression against ASD severity – not quite double dipping, but surely some lack of complete independence. Please comment/respond to this statistical issue.

2) The developmental data set yields very intriguing findings: Are the ROI's used here those discovered in the first cohort? If so, this is important and should be highlighted. Either way, this is a small cohort and should be noted as such.

3) The authors provide nice correlations between fMRI and EEG-based intrinsic time scales (Figure 1): however these differ by two orders of magnitude: This difference should be highlighted in the Discussion and other potential factors, such as neurovascular, should be mentioned.

Reviewer #2:

Watanabe, Rees, and Masuda propose to compare the intrinsic timescales of brain regions in ASD and TD. They find significant differences in brain regions that are associated with the severity of symptoms and their gray-matter volume. This is an outstanding contribution to the understanding of structure, dynamics, and function in the human brain. The results are compelling and the analysis is thorough. I naturally recommend that the paper is published. To improve the presentation and the reproducibility of the results the authors should consider some minor suggestions:

1) The study finds a variety of regions that have atypical intrinsic timescales and the timescales of some of these regions have significant association with ADOS and with RRB. However, the authors do not discuss whether those regions have been reported before in other ASD studies. This should be discussed, and, if they have not been reported before, the authors might want to highlight the sensitivity of their new proposal.

Introduction

2) The authors mention "functional hierarchies" in the Introduction. Although this is a nice motivation, the concept of "hierarchy of timescales" should also be introduced. The hierarchy of timescales proposes a strong link between the well-established hierarchy in brain structure with a hierarchy in brain function with peripheral regions (at the bottom of the hierarchy) exhibiting fast timescales and core regions (at the top of the hierarchy) exhibiting slow timescales. This concept is proposed by Kiebel et al., 2008, and thoroughly explored by Gollo et al., 2015. Moreover, a distinct functional role of regions at the bottom and top of the hierarchy was demonstrated by Cocchi et al., 2016, using brain stimulation.

3) The authors mention "core symptoms" in the Introduction without providing additional details. A brief introduction and motivation of the different (social, communication, RRB) measures is missing in the manuscript, and would improve the presentation. Moreover, it is not clear how ADOS (total) was computed.

Results/Materials and methods

4) It is unclear why the results start with a negative sentence explaining what was not done. Instead of this approach, it would be better to provide a brief summary of what the results will cover (the cohorts, EEG, fMRI, structural imaging, symptom measures).

5) "The largest time lag in calculating the initial positive period was set to the value at which the ACF hit zero for the first time as the time lag was increased". This sentence is misleading because it suggests that an interpolation might be required to find when ACF hits zero, and it also contradicts the caption " The initial positive period is the area under the ACF before the ACF hits zero for the first time as the time lag increases".

6) Figure 1: Please indicate what was the parcellation used here, and how the time series were averaged within regions. A parcellation with 360 regions was used in other results. However, it is not clear if this was also the case for this comparison between EEG and fMRI.

7) Figure 1C and Figure 1—figure supplement 2. These results show the correlation between the intrinsic timescales obtained from fMRI and from EEG at specific frequency bands. Is the correlation also significant if the EEG signal is considered without filtering at specific frequency bands?

8) Figure 2A: Please clarify the colorbar. How was the intrinsic timescale =1 defined?

9) As shown in Table 2, the regions have various cluster sizes. How was the intrinsic timescales computed in Figure 3? Was it averaged across voxels within the cluster size, or did it have a fixed volume? Please clarify.

Discussion

10) The first sentence proposes an interpretation of the meaning of intrinsic timescales " an index for potentially measuring how long neural information is likely to be stored in each brain region". This is an interesting idea. Unfortunately, however, this interpretation is weak. It has "potentially" and "likely" that make the sentence very apologetic. Moreover, it refers to storing information, but the data corresponds to a resting-state task. Although it is possible to understand the main point, there is still some room for improvements in this definition.

11) "…could potentially be used as a biomarker for early diagnosis of this prevalent neurodevelopmental disorder." This is an intriguing point. Have the authors tested whether it is feasible to propose a biomarker based on the intrinsic timescales in this dataset? What is the specificity and the sensitivity of this measure? If this is not feasible, please explain and discuss the reasons.

12) The gray-matter volume was nicely motivated in the Results section: " We focused on GMV because theoretically, an increase in neuronal density, which is measured by GMV [25], would enhance recurrent neural network activity, and then enlarge the autocorrelation strength in the neural signals". It seems that the manuscript could be improved by incorporating some discussion on this topic.

Reviewer #3:

This study used an EEG-validated fMRI measure of intrinsic timescales (IT), along with a structural imaging measure of gray-matter density to compare brain regions in subjects with ASD and typical controls. They find that subjects with ASD show lower IT in the bilateral postcentral gyri and right inferior occipital gyrus, and higher IT in the right caudate. These results correlate both with ASD symptoms, and gray matter density. These findings were replicated in two independent data sets. They also looked at the change in time scales over development in adolescents, and found that these findings correlated with symptomatic progression.

The authors ask well articulated questions and use suitable methodology. While their measure of autocorrelations is innovative, it appears to be well justified by EEG, and by the consistency of their findings. This exploratory case-control study indicates a new direction that can scale to studies in larger and more diverse ASD populations.

My major comment about the work regards the interchangeability in their discussion between timescales observed via single-neuron recordings and timescales observed in fMRI and Ecog. The autocorrelation decay function in their cited electrophysiology papers (refs 10 and 11) last no longer than 800 ms. In their Figure 1A fMRI autocorrelation function, we see the decay last up to 9 seconds. While it is interesting that both methodologies produce brain-region specific differing of autocorrelation functions, they occur on time durations differing by an order of magnitude. By using references to jointly support the investigation of timescales, the authors imply that they represent the same underlying phenomenon. If they really hypothesize that, much more work needs to be done in the Discussion section (and potentially experimentally), to support the claim. If they are agnostic as to the connection between timescales using these different methodologies, that stance also needs to be made explicit.

# Peer review - Round 1

Editors:
- Jody C Culham, University of Western Ontario , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15252.023](https://doi.org/10.7554/eLife.15252.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A hierarchy of timescales explains distinct effects of local inhibition of primary visual cortex and frontal eye fields" for consideration by eLife. Your article has been reviewed by three external peer reviewers, and the evaluation has been overseen by Jody Culham as both the Reviewing Editor and Senior Editor.

The reviewers have discussed the reviews with one another and the Editor has drafted this decision to help you prepare a revised submission.

The following individual involved in review of your submission has agreed to reveal his identity: Michael Arcaro (Peer Reviewer).

Summary of manuscript:

The authors combine fMRI, TMS, and computational modeling to investigate interactions between visual cortical regions. They find that cortical stimulation of posterior visual cortex (V1/V2) leads to an increase in BOLD correlations with FEF, but stimulation of FEF leads to a decrease in BOLD correlations with posterior cortex. The modeling work indicates that these changes are related to the intrinsic timescales of these regions. This is a truly impressive study. The multi-methodology approach and research question is very novel and the results have important implications for understanding the neural processes facilitating interactions along the cortical hierarchy.

Summary of reviews:

While all reviewers of the work were quite positive, they raised a number of concerns that should be addressed in a revision. Although the journal policy is usually only to provide a summary of the main points, given that the reviewers raised a number of important and thoughtful points that may be "lost in translation" by condensation, the full reviews are appended below. The Essential Changes are based on the post-review discussion amongst the reviewers and editor and are outlined below. We also strongly recommend the authors review the full list of suggestions from the reviewers and, at their discretion, determine whether they can improve the manuscript based on the constructive criticism provided. The editor did not think that suggested changes requiring collection of new data were essential, though there are some cases where additional analyses of the extant data could be beneficial in addressing the suggestions.

Essential changes:

1) Most imperatively, two reviewers noted that there is some confusion between the concepts of anticorrelation and connectivity changes that is challenging for the interpretation of the results.

Reviewer #3 states, "Positive and negative correlations are not synonymous with increased and decreased connectivity. The authors summarize their findings as "stimulation of early visual cortex selectively increased feedforward interactions with FEF" and " stimulation of FEF decreased feedback interactions with early visual areas." TMS of FEF resulted in a stronger anti-correlations with V1/V2. An argument could easily be made that connectivity increased in both cases, especially since these areas appear to be moderately anti-correlated at rest (see below)."

Similarly Reviewer #2 points out that the interpretation of connectivity changes depends not solely on changes to correlation values but the magnitude of the r value with respect to no correlation (r=0).

This must be clarified with more careful wording, unpacking of the specific effects (Figure 3) and better explanations/discussion.

2) Two reviewers (#2 and #3) raised questions about the localization of the TMS sites. This must be clarified.

3) Reviewer #1 raised concerns about the accuracy of the structural connectome on which the Kuramoto model is based. The other two reviewers agreed this was a concern so this must be discussed.

4) The Reviewing Editor raised a concern about the asymmetry in connectivity between FEF and V1/V2 at baseline and the other reviewers agreed this should be addressed. Specifically, the data in Figure 2 on baseline resting-state connectivity showing that a V1/V2 seed is negatively correlated with FEF while an FEF seed did not show a negative correlation with V1/V2. One would expect these effects to be roughly symmetric and it would be helpful to clarify why they are not. One possibility is that it's just a thresholding issue (e.g., 2b would show V1/V2 at a slightly more liberal threshold). Another possibility is that the seeds are not exactly in the same location as the sites that are correlated with the opposite seed). Please clarify.

Recommended considerations

5) Two reviewers agreed the manuscript would be strengthened by the inclusion of control sites in the connectivity analysis while a third reviewer disagreed. The most useful additional analysis that the majority agreed would be worth investigating would be to examine the connectivity of the V1/V2 site after FEF stimulation and vice versa. We suggest the authors check this out and see if it adds any value to the paper (and include it if it does or provide a brief summary in the reply letter if it doesn't).

Reviewer #1:

This paper presents a combination of TMS with different analyses of functional/effective connectivity and computational modelling, using a whole-brain formulation based on the Kuramato model. This combination is so far unique and enables the authors to provide evidence for a plausible and quite fundamental principle of cortical organisation, i.e., that cortical areas at different hierarchical levels operate at different time scales. I think this is a strong and innovative paper which elegantly combines complementary techniques. However, from my perspective, a few issues would benefit from clarification or reformulation:

1) I think the presentation of the key findings and the conclusions drawn needs to be improved. In brief, the key conclusion seems to be: inhibitory TMS leads to a local slowing of the timescale (frequency of dominant oscillations) at which an area operates; TMS of V1/V2 decreases and TMS of FEF increases the discrepancy in oscillatory frequencies between these two levels of the visual hierarchy; this explains why the former leads to increased bottom-up connectivity and the latter leads to reduced top-down connectivity. The authors get to this on fourth paragraph in the Discussion, but do not make it as explicit as I think they should. Moreover, it would help if this interpretation and the underlying hypothesis would be pointed out more clearly earlier in the paper, e.g. in the Introduction.

2) To support this conclusion, it would be helpful if not only the correlation between changes in ALFF and changes in connectivity were shown; additionally, it would be important to see the magnitude and direction of the local changes in ALFF, separately at both levels of the hierarchy, that are induced by TMS.

3) One potential concern for the whole-brain Kuramato model is the accuracy of the structural connectome on which the model rests. This connectome was derived from diffusion-weighted imaging data, using probabilistic tractography. It would be helpful if the authors could provide some reassurance that these connectivity estimates are robust and not overly affected by methodological problems of tractography, such as the known bias in reconstructing short- versus long-distance connections.

4) Testing the robustness of the functional connectivity results across a variety of preprocessing strategies for resting state data is a strong aspect of this paper. However, it did not entirely get clear what motion correction procedure the results eventually reported are based on. It would be helpful if this could be clarified.

Reviewer #2:

The aim of the study was to explore long-range connectivity changes (assessed by resting-state fMRI) resulting from a local decrease in excitability induced by continuous theta burst TMS (cTBS). The authors used cTBS to modulate excitability in the V1 and the R-FEF in separate sessions. Inhibition of V1 with cTBS led to an increase in functional connectivity between V1 and R-FEF. Inhibition of R-FEF led to a decrease in functional connectivity between R-FEF and V1. This is an interesting study that looks to combine brain stimulation and neuroimaging with modelling to address a clearly articulated question.

Major Comments:

1) The authors suggest that there is a significant relationship between the amplitude of local BOLD signal within the FEF and changes in connectivity between FEF and V1 (Figure 3—figure supplement 3). Could the connectivity changes therefore be (trivially) explained by merely increased or decreased signal-to-noise in the seed region leading to changes in the connectivity? (If there is greater signal – and therefore greater variability – in the seed region, it is more likely that functional connectivity can be identified between that region and elsewhere).

This is a difficult problem to address, and I admit I do not have an easy solution, but it should be at the least discussed. I admit that I do not understand the sentence "the effects remained after controlling for changes in mean BOLD signal between baseline and post-TMS sessions", which may be aimed at addressing this conflict.

2) The authors present no controls for their study. There are a number of questions raised by this:

a) Can they demonstrate that the fluctuations in connectivity between V1 and FEF, separated in time as these scans were, cannot explain the changes here (i.e. is this just an effect of repeated rs-fMRI scanning, rather than a TMS effect)? It may be possible to get this data from existing datasets – a step towards this would be to study the differences between the two baseline sessions, though this would not account for changes due to differing time spent in the scanner.

b) Are these changes specific to the stimulated regions? If the seeds for the functional connectivity analyses are placed elsewhere in the functional networks, can similar changes be elicited? And similarly for regions outside the networks? The authors have the data to perform these analyses.

c) Are the changes seen specific to stimulation at these sites? If the network was stimulated at a different site, would this result in the same pattern of results (i.e. is this just a reflection of some perturbation to the network as a whole or does it reflect the specific connectivity between these regions). This would require more data to be acquired, but is important for their conclusion that these are specific effects. A step towards this might be to show that stimulation of the FEF does not lead to connectivity changes in the V1 seed and vice versa, which they have the data to demonstrate.

3) One of the major things I struggled with in this study is the authors' interpretation of ante-correlations. To me, the demonstration of a significant, negative functional connection between two regions is not a lack of a functional relationship, a point with which the authors seem to agree. Therefore, a numerical increase in the r value between two regions is not an increase in connectivity if it does not go through 0, but rather is a decrease in (inhibitory) connectivity. If it does go through 0 it is then a reversal of negative to positive functional connectivity and the interpretation is very different.

This is an important point of interpretation, and is currently not clear in the manuscript. If I understand correctly, the authors suggest that inhibitory TMS to V1 led to an increase in connectivity between V1 and FEF. These regions were negatively correlated at baseline (Figure 2A). Does this increase in connectivity mean that these regions are now positively correlated or that they are less negatively correlated? In the caption to Figure 3B they state that these are "antecorrelations" but I do not see the data to support that.

Likewise, inhibitory TMS to the right FEF led to a significant decrease in functional connectivity between this region and V1. Does this mean that there is now a significant functional connectivity between these regions, where there was not previously?

Reviewer #3:

The authors combine fMRI, TMS, and computational modeling to investigate interactions between visual cortical regions. They find that cortical stimulation of posterior visual cortex (V1/V2) leads to an increase in BOLD correlations with FEF, but stimulation of FEF leads to a decrease in BOLD correlations with posterior cortex. The modeling work indicates that these changes are related to the intrinsic timescales of these regions. This is a truly impressive study. The multi-methodology approach and research question is very novel and the results have important implications on the neural processes facilitating interactions along the cortical hierarchy. The manuscript is well written. Several aspects of the data that could affect the interpretation of the results need clarification. Specifically, the authors should evaluate potential influences of the underlying functional organization on the observed interactions, and address the differences between the imaging and modeling results. In addition, I have concerns on the specificity of the localization for both the imaging data and TMS. Conceptually, the authors also need to better address the relation of positive/negative BOLD correlations to increased and decreased connectivity.

Main Comments:

Positive and negative correlations are not synonymous with increased and decreased connectivity. The authors summarize their findings as "stimulation of early visual cortex selectively increased feedforward interactions with FEF" and "stimulation of FEF decreased feedback interactions with early visual areas." TMS of FEF resulted in a stronger anti-correlations with V1/V2. An argument could easily be made that connectivity increased in both cases, especially since these areas appear to be moderately anti-correlated at rest (see below).

Are the observed interactions between V1/V2 and FEF generalizable to posterior visual vs. higher-order (frontal) regions? The modeling certainly appears to predict generalizable effects, but I'm not sure the imaging data specifically demonstrate this.

Could the correlation patterns be related to the underlying topographic organization? Anatomical and functional studies in monkeys have shown that FEF and visual cortex is topographically organized with foveal and peripheral V1/V2 connected to differentiable portions of FEF (Schall et al. 1995; also see Babapoor-Farrokhran et al. 2013; Janssens et al. 2013). The particular increase/decrease in BOLD co-fluctuations may reflect where stimulation was applied relative to the functional organization of these regions (specifically retinotopy). This would still be an interesting result, but should be clarified.

Given that TMS to FEF results in decreased BOLD activity in foveal V1, but increased BOLD activity in peripheral of V1 (Ruff et al. 2006; Ruff et al. 2009; Driver et al. 2010), were increases in BOLD correlations observed in peripheral V1/V2 for Post-FEF-TMS? Were any decreases in correlations observed in frontal cortex for POST-V1-TMS? If so, would this be predicted by the model?

How precise was the TMS? Judging by the provided MNI coordinates, it's not clear that the closest gyrus on the surface is still within V1/V2. It's very close to lateral occipital extrastriate areas such as LO1/2. Given the lateral/medial distinction of FEF in the macaque, is it possible that TMS stimulation of FEF targeted a more foveal region than the seed region for the BOLD correlations?

The authors should address sources of variability in the localization of areas. Closer evaluation of the correlation maps could potentially address this. While the pre- and post- TMS correlation maps of FEF heavily overlap in the ipsilateral hemisphere (Figure 3—figure supplement 1), there is some separation with the post-TMS increase located slightly more inferior and lateral. Slices end at z = 40 in this figure though. Does the increase in correlation post TMS extend further inferior? What is the relationship between the observed correlations in FEF and the seed FEF?

The model predicts that TMS to V1/V2 leads to a general increase in connectivity across cortex, and TMS to FEF leads to a general decrease. Can the model speak to potential topographically specific interactions as noted above?

What accounts for the differences between the model predictions (Figure 4B) and the observed changes in BOLD correlations (Figure 3) post-TMS? Specifically, the model predicts increases in extrastriate cortex, temporal lobe, and much of the frontal lobe after TMS to V1 while changes in BOLD correlation are minimal in non-FEF frontal cortex, the temporal lobe, and extrastriate cortex (with the exception of a surprisingly specific increase in posterior parahippocampal cortex). There also appear to be increases in BOLD correlations within the parieto-occipital sulcus and retrosplenial cortex that are not clearly predicted in the model. After TMS to FEF, the model predicts large decreases in the frontal lobe and anterior, lateral occipital cortex (possibly near area MT) and increases in anterior temporal cortex, which are not apparent in the imaging data.

Reviewing Editor:

I was puzzled by the data in Figure 2 on baseline resting-state connectivity showing that a V1/V2 seed is negatively correlated with FEF while an FEF seed did not show a negative correlation with V1/V2. One would expect these effects to be roughly symmetric and it would be helpful to clarify why they are not. One possibility is that it's just a thresholding issue (e.g., 2b would show V1/V2 at a slightly more liberal threshold). Another possibility is that the seeds are not exactly in the same location as the sites that are correlated with the opposite seed). Please clarify.

I agree with Reviewer #3 that the folded surfaces make it hard to see some sites (esp. FEF) and this could be resolved with partial cortical inflation or other views (e.g., superior view to show FEF).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A hierarchy of timescales explains distinct effects of local inhibition of primary visual cortex and frontal eye fields" for further consideration at eLife. Your revised article has been evaluated by Eve Marder (Senior Editor), Jody Culham (Reviewing Editor), and 3 reviewers (including Michael Arcaro, who agreed to reveal his name).

The manuscript has been improved considerably and two of the reviewers are largely satisfied. However, there are some remaining issues that still need to be addressed, as outlined below. Although at eLife, we try to avoid putting authors through an endless gauntlet of unnecessary revisions, we also aim to ensure that published manuscripts meet our high standards. In this case, the remaining concerns were substantive enough that we think another round of revisions would greatly benefit the clarity and impact of the manuscript.

Again, since the detailed points made by the reviewers were well articulated and are appended in full after the summary from the Reviewing Editor.

Essential points

1) The manuscript has become clearer by rephrasing in terms of changes to positive and negative correlations (rather than just increases or decreases without respect to the initial sign of the correlation as in the first version). However, both Reviewer #3 and the Reviewing Editor still found it hard to interpret without an additional figure to show the post-TMS connectivity. (not just pre and post-pre changes). See their comments for details (Reviewer 3, Point 1; RE, Point 1).

2) Although based on your reply, we understand your justification for displaying data on the folded cortical surfaces, the problem remains that one of your two key areas (FEF) is hardly visible from lateral views. This can be solved simply by presenting either a superior view or a horizontal slice consistently in all figures (not just a subset as it is currently, e.g., slice on Figure 2A, superior view on Figure 3). And you may as well add an inferior view (to show lingual/fusiform cortex).

3) In the post-review consultation, the other reviewers reinforced a suggestion from Reviewer #3 (last line of Reviewer 3, Point 1). Reviewer #1 stated: I think the one issue to resolve is whether the model does or does not predict anti-correlations, that is, the authors should clarify the connection between their description in the main text and the results shown by Figure 4.

Recommended considerations

Reviewer #3 raised two points that the other reviewers (in post-review consultation) were less convinced were essential to resolve. Nevertheless, the Reviewing Editor would encourage you to take this feedback into consideration in case you can use it to strengthen the manuscript.

1) Reviewer #3 (Point 2) still questions the asymmetry of the FEF and V1/V2 correlations,. The Reviewing Editor thinks that if it cannot be fully resolved, it should at least be made more apparent in the main manuscript (by showing the FEF clearly in extant figures and/or moving Figure 3—figure supplement 1 to the main text) and discussed. As is, the main figures don't show this because of the views presented).

2) Further consideration of the earlier results of Ruff and colleagues may be warranted (Reviewer 3, Point 3). The other two reviewers were less convinced of this and noted that the TMS methods by Ruff were quite different and your paper wasn't designed to examine the relationship between connectivity and retinotopy. Nevertheless, Reviewer #3 thought the manuscript could be more compelling on this front (for specifics, see "Added Comments from Reviewer #3 during Post-review discussion"). The Reviewing Editor will leave it as "your call" as to whether you can use Reviewer #3's suggestions to strengthen your manuscript or agree more with the other two reviewers that it is beyond the scope of your aims.

Other points should be considered at the authors' discretion.

Reviewer #1:

I have gone through the authors' response and am happy with the additional analyses and revisions. My only (and slight) reservation is that the introductory sentence ("Probabilistic tractography.… allowed an accurate estimation of the average connectivity strength.…") to the section on "Anatomical connectivity" continues to be a little too optimistic, given that there is an ongoing debate about the pitfalls of tractography (e.g., see Reveley et al. 2015, PNAS). Otherwise, I do not see any major remaining problems and would recommend acceptance of the paper.

Reviewer #2:

The authors have provided a thorough and thoughtful set of answers to my comments and I have no further concerns.

Reviewer #3:

The authors made extensive revisions to the manuscript including several new figures and provided a thorough and thoughtful response to the previous reviews. While the revision addressed several issues, my main concern regarding the interpretation of the correlation changes and their relation to the TMS targets and seed regions remain.

1) The relationship between positive / negative correlations and increased / decreased correlations needs further clarification:

Seventh paragraph of Results section. "Inhibitory TMS of right visual cortex (V1/V2) resulted in the emergence of positive correlations between this region and bilateral FEF." – The difference maps in Figure 3 do not illustrate this and there is no reference to statistical measures. Are the post-TMS, positive correlations significantly different from 0? Or is there just a significant difference between baseline and TMS? It could be very informative to show correlation maps post-TMS for V1/V2 and FEF seeds w/o the baseline subtraction (ala Figure 2).

Results section, subsection “Computational modeling”. "Simulation results showed that virtual inhibition of right V1/V2 within the model increased the positive correlations between this region and the rest of the brain (red in Figure 4a)," – I'm still confused about correlations in the simulation. This statement suggests that simulated V1/V2 connectivity with FEF started out positive and increased following V1/V2 inhibition. That is not entirely consistent with the imaging data (i.e., correlations were negative at baseline). Figure 4 does not illustrate which simulated correlations are positive / negative. This figure could be expanded to parallel the imaging data by showing the baseline connectivity and connectivity post-simulated TMS.

Same section. "Conversely, simulated inhibition of FEF, again by slowing its intrinsic frequency, was associated with the emergence of significant anticorrelations in this region's connectivity with the rest of the brain (blue in Figure 4A)." – In the previous version, this was described as decreased connectivity, which I assumed was a lack of (any) correlation. Does the modeling result actually predict anticorrelations?

2) The authors refer to a common V1/V2 region (also FEF) across TMS targets, seed ROI and observed correlations. However, asymmetry in the correlations and anatomical variability suggest that this is not necessarily the case. The relationship between all three for V1/V2 and FEF needs further clarification.

The data would be more compelling if the seeds were better matched to the observed correlations. For example, the FEF seed could be adjusted to be in better correspondence with the V1/V2 anticorrelations (or vice versa). Further, why not use the FEF seed as an ROI to evaluate correlations pre- and post- V1 TMS (and vice versa)? An ROI approach would be a more direct way for assessing correlation changes due to TMS (vs. the qualitative assessment of the correlation maps).

The FEF seed is noted as being posterior and lateral to the V1/V2 baseline anticorrelation. From the Figure 1—figure supplement 1, the FEF TMS sites appear to be within the FEF seed, but also extend lateral and posterior, suggesting that the TMS-site for FEF and the anticorrelations with V1/V2 only partially overlap. The authors should better address whether such variability had an affect on the correlations. e.g., the authors could show something similar to Figure 3—figure supplement 3, but color code the FEF TMS sites based on the changes in correlation with V1/V2 (and vice versa). If the precise TMS location did not matter, there should be no difference in the correlations between the subset of TMS sites that overlapped with the V1/V2 baseline anticorrelations and the ones that didn't.

Figure 1—figure supplement 1 nicely illustrates the relationship between the TMS sites and seed area, but could be improved. There is no reason to show the whole brain, and that only makes evaluation of the correspondence more difficult. Focal views of V1/V2 and FEF should be shown (such as in Figure 3—figure supplement 3). This figure would further benefit by illustrating the relation between observed correlation changes and TMS sites. e.g., showing the TMS target locations overlaid on a correlation changes post TMS.

Figure 2—figure supplement 2. The control analysis did not yield significant negative FEF correlations with the V1/V2 seed. Is there still a significant increase in correlation when comparing these correlations to the post-TMS?

3) As stated previously, Ruff and colleagues (2006, 2009) found decreased correlations with foveal V1 and increased correlations with peripheral V1 after TMS to FEF. While their experimental paradigm differed with the current study and the reviewers' comment on state dependent effects is well taken, these prior studies looked at correlations during both task (visual) and rest (non-visual) conditions (and found no significant differences). Such findings are clearly relevant to the current work and should be discussed. How can these prior data (specifically the observation of both increases and decreases in V1 correlations) be reconciled with the current proposal on how TMS differentially affects the timescales of early visual cortex and frontal cortex?

Added Comments from Reviewer #3 during Post-review discussion:

The current study proposes a general difference between early visual and higher order regions with interactions governed by their intrinsic timescales of processing. The Ruff studies found that interactions between early visual cortex and FEF vary depending on the topographic sub-region within early visual cortex. Aside from methodological differences, those data suggest heterogeneity in early visual-frontal interactions (there is also substantial evidence from monkey studies showing heterogeneity of anatomical connections and function within both FEF and V1). It's unclear to me how any such heterogeneity can be directly accounted for by the current study's broad short and long timescale differences in early visual cortex and FEF, respectively. More so, it actually seems that their model predicts the opposite (lack of heterogeneity). I think an argument potentially could be made that any heterogeneity in correlations reflects the heterogeneity in connections, though it's not clear to me what that mapping would be, and their data do currently do not speak to this.

On a related note, higher precision in the targeting could mitigate this issue. I completely agree with [one reviewer] that there is a limit to what the authors can do in regards to the localization. However, they easily could have performed seed-to-seed correlations or used an areal atlas (particularly for V1), which would be much more of a control in localization than what they currently have done. These are very simple analyses, and frankly, I don't understand why these weren't done in the first place.

I completely agree with [another reviewer] that it would not be fair to expect the authors to directly address this in their paper as their model clearly wasn't intended to test retinotopy or any other areal substructure. However, I think it's reasonable to expect the authors to have an idea (discuss) on how their model would fit within the well established architecture of the brain regions they've specifically investigated, particularly since their imaging results look like they do not encompass the whole area of V1 or FEF.

For clarification, I was referring to the eccentricity specific correlations for visual areas V1-V4 from TMSing FEF in the Ruff 2009 paper, which seems to expand upon the V1 result in their 2006 paper.

Reviewing Editor:

In trying to wrap my head around the data given the new presentation in terms of not just the direction of changes but their effect on positive and negative correlations, I had to make visual comparisons of Figures 2 and 3. That is, I was trying to see whether increases/decreases in connectivity (Figure 3) meant increases/decreases in positive/negative correlations. I thought it would be easier for readers to understand this if (1) an additional figure were presented in the main manuscript to show post-TMS connectivity (not just differences in connectivity); and (2) the same brain views were presented in the same order (as is, Figure 1 doesn't show superior views to highlight FEF or inferior views to show the lingual and fusiform gyri).

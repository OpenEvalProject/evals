# Peer review - Round 1

Editors:
- Huda Y Zoghbi, Texas Children's Hospital United States

Reviewers:
- Hanna Renvall, Aalto University Finland
- Allison Nugent
- Annika Hulten, Aalto University Finland

## Review text

DOI: [10.7554/eLife.36011.015](https://doi.org/10.7554/eLife.36011.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Disrupted parietal oscillatory connectivity links young APOE-ɛ4 carriers to Alzheimer's disease" for consideration by eLife. Your article has been reviewed by David Van Essen as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Hanna Renvall (Reviewer #1); Allison Nugent (Reviewer #2); Annika Hulten (Reviewer #3).

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study by Koelewijn et al., involves a data set of 183 subjects in an attempt to link APOE-ɛ4 carriers to preclinical changes neural activity, in relation to their increased genetic risk of developing AD. The authors investigated resting-state oscillatory network connectivity across different frequency bands. Key findings: APOE-ɛ4 carries have increased alpha- and beta-band connectivity in bilateral occipital areas and parietal cortices, as compared to non-carriers. The connectivity changes were partially overlapping with decreased connectivity between right hemisphere parietal and temporal areas in a separate population of AD patient. Based on these findings the authors suggest that AD can be characterized by pre-onset hyperconnectivity that, once the disease manifests, turns into hypoconnectivity particularly in the parietal cortex.

In general, the referees were positive and found the study exciting. However, in particular in regard to methodology there were several concerns that require clarifications and justification. Also, it was a general feeling that the Discussion section requires improvement: in its current form the paper lacks deeper discussion and theoretical background needed to interpret the present findings with respect to the majority of the existing literature in AD, as well as on the possible clinical value of the results.

One referee asks for further analysis (see point 14): In the description of the AD subjects, the manuscript states that there was an age-matched cohort. However, it appears they were not compared to the AD subjects. It is proposed to use these as a comparison group rather than the young E4 carriers. The authors are encouraged to follow this advice or provide a strong rationale for why this was not done.

Essential revisions:

Methodology

1) It is unclear why the authors decided to use only eyes open condition here (cf. their earlier study on AD patients with both eyes open and closed data), and not e.g. the difference between eyes closed (with prominent alpha activity) and eyes open conditions that might be a more reliable functional measure? Furthermore, it appears that the differences between AD patients and controls were even more prominent in the eyes closed condition? Please motivate.

2) The section on the Gaussian Mixture Model (GMM) is inadequately described. The authors state that a GMM was applied to all 8100 connection to separate signal from noise. Within each frequency band, however, aren't there only 4005 unique connections, since correlations cannot discern directionality? How many subpopulations were included in the mixture model? Is there any published validation that shows that this method effectively separates true correlations from noise? Was this done for each group separately?

3) Is the discarding of connections +/- two scaled median SD's after the connections were removed by the GMM method? So, each subject now has a different number of valid connections?

4. The authors state that the valid connection masks were added to form a single mask – was this a union or an intersection? It says that it included all valid connections present in either group, but does this include connections that were not valid in all subjects?

5) How were the randomization test (akin to a two-sample t-test) and the uncorrected two sample t-test different, other than that one is parametric and the other non-parametric? The authors seem to indicate that the interpretation is different. (i.e. the two-sample t-test can test whether differences were global across the brain).

6) Please clarify how the power was calculated, what parameters were used to connect the effect size for disease prediction accuracy (the AUC from Escott-Price) to the MEG measures?

7) It is stated that the GMM selected valid datasets as well as valid connections, although the GMM methods do not mention how datasets were defined as valid or invalid.

8) One referee mentions that a main concern is the choice of parcellation scheme used in the connectivity analysis. While it is fair to say that there exists no one correct atlas that always should be used, the AAL is definitely non-optimal for a MEG connectivity analysis as the parcels are of very different size and shape. By selecting only one node from each parcel, the nodes will be unevenly distributed across the cortex, which in itself is somewhat problematic. However, a bigger problem is that large elongate parcels (such as those in the temporal lobe) may contain two (or more) active areas but will be represented by only one node (capturing the strongest source). The worst-case scenario is if a strong active area is situated on the border between two or more large parcels. In this case the nodes from each of these parcels will reflect the same underlying neural activity, whereas a clear but somewhat smaller activation in the other end of one of the parcels would go undetected. Assuming that the multivariate leaking correction works as intended, two nodes capturing the same activity is less of a problem (though it may lead to spatially incorrect inferences) but ignoring an active area may alter the network dynamics radically. The most straight forward way around this is to select a parcellation scheme with optimally sized parcels (not too small, not too big) that are of roughly equal size. To my knowledge no existing atlas fulfills these criteria fully, which is probably reflected in the fact that most connectivity papers use modified versions of existing parcellations. If the number of parcels becomes too big, there is the option to select only those that cover the cortical regions associated with the DMN in the literature. Alternatively, you may wish to try a more sophisticated approach and apply a data driven way of finding all active regions based on some form of clustering algorithm or ICA, and the define parcels/nodes based on these. Please comment on the AAL approach in relation to these alternatives.

9) The use of a multivariate orthogonalization approach is an elegant way to address the problem of spurious (aka ghost) interactions. However, like all methods it has its limitations, and it would be good to acknowledge these in the Discussion section. For example, the SNR is not constant across all cortical regions in MEG and areas which will the source estimate specificity and by extension the rotation done in the correction. Therefore, connectivity between areas with high source power (like the occipital and parietal regions in the alpha band) may be more easily detected than those with low source power (like the frontal cortex). This may, in part be the reason for the different results between the previous fMRI study by Filippini et al.

Results/interpretation

10) The major finding suggest hyperactivity in the right parietal connectivity, but after the statistical analysis the result appears quite modest and very local. How can one be sure that it is not the result of signal leakage?

11) The location for the statistically significant hyperactivity is not anatomically the most evident one, taken that the most prominent structural changes appear in the hippocampus and more generally in the medial temporal lobes. The authors have analyzed the hippocampal volumes and total intracranial volumes in all subjects, but what about the parietal volumes? Is their e.g. any hemispheric difference in the parietal lobe volumes in the APOE-ɛ4 carriers that would correlate with the present finding?

12) In Table 2, the only overlapping, affected areas between non-symptomatic APOE-ɛ4 carriers and AD patients were the right parietal areas, whereas 6/10 nodes with greatest group difference in APOE-ɛ4 carriers and controls were not different between AD patients and age-matched controls. How do the authors explain this disappearing difference along with the progressing disease?

13) In Figure 2, from panels D and H, it appears that all connections were greater in the E4 carriers compared to non-carriers. In panel E, it is clear that most of the valid connections are above the x=y line, indicating that the mean Z is higher for the carriers than non-carriers. However, in panel A, it appears that most of the valid connections are below the x=y line, which would indicate that the mean Z is larger in the non-carriers. Please clarify. Also, in panes F and G, it appears that there are valid connections to frontal areas, however these are not apparent on the glass brains.

14) (also see general comment for this point). The description of participants is confusing, given that a re-analysis of data in AD was performed, but these subjects are not well described. Please clarify. There also seems to be a comparison between young E4 carriers and AD patients: I question the utility of this given that age is a confound. In the description of the AD subjects the manuscript states that there was an age-matched cohort, but I do not see where they were compared to AD subjects. This would be a much better comparison group than young E4 carriers.

15) Table 2 shows nodes most "affected" within each group separately – what is being compared? Eyes open vs. eyes closed? Based upon Figure 4, is it right that the comparisons are young APOE-E4 vs. AD, and AD vs. matched controls? Why are the results for E4 carriers vs. non-carriers in Figure 4 different from the results presented earlier?

Discussion

16) In its current form the paper lacks deeper discussion and theoretical background needed to interpret the present findings with respect to the majority of the existing literature in AD, as well as on the possible clinical value of the results.

17) The AD patients who are APOE-ɛ4 carriers are known to develop the clinical AD at an earlier stage than non-carriers, but in the end with very similar structural and clinical changes to the non-carriers. Why this happens, and what is the role of APOE-ɛ4 allele in the course of the disease remains unclear, but it has nevertheless been studied extensively. The manuscript should provide some light on what is known about the cellular-level functions of APOE-ɛ4, and especially on how these functions might be related to the present neuroimaging results. I do see that it is difficult to draw conclusions between cellular level findings and non-invasive neuroimaging results, but at least some hypothesis/discussion would be needed here.

18) Taken that the ultimate goal is to find individual measures on the connectivity changes in the prodromal patients, the decision to concentrate only on the connections that were consistently present in all datasets would benefit some comment/discussion on the selection's potential drawbacks.

19) PET often shows hypometabolic changes already in the stage of mild cognitive impairment in AD patients – is there literature on PET results in young healthy APOE-ɛ4 carriers? If such exists, it should be discussed with respect to the present results.

20) Taken that MEG may not be the optimal method to study deep brain structures or frontal cortex, some comment on the possible limitations of MEG in this respect would be good to add here.

21) When searching for clinical biomarkers, the consistency of the measures over multiple measurements should be demonstrated. Any such information available to be added here?

22) In discussing both their own findings and the previous literature, the authors should avoid inferring causation from correlation. This line of reasoning occurs both in the introduction and discussion. For example, in the Introduction the authors state that the previous findings "suggest that the presence of an APOE-ɛ4 allele alters oscillatory brain function", when in fact the studies that are referred to have only found an association. The fact that the presence APOE-ɛ4 does not always lead to AD (with accompanying changes in oscillatory brain activity) suggests that other genetic or environmental factors (such as e.g. cholesterol levels) are at play as well. Moreover, it is possible (if not probable) that the APOE-ɛ4 is part of a more multifaceted genetic basis of AD. Assigning the causation to one allele would in this case be misleading.

23) A referee was unable to follow the logic in the Discussion section where the authors compare the present findings to those reported by Filippini et al. The author claim that the previous fMRI study corroborates the present findings even though completely different areas are highlighted in each of the respective studies. I am also uncertain what the word "inconsistency" is referring to in the sentence "In contrast, evidence of the hippocampal volume decrease in young carriers is inconsistent […]". You referring to previous findings being inconsistent or that the present study adds to the inconsistency? I suspect that the authors mean that given the inconsistent findings of reduced hippocampal measures, hemodynamic and/or oscillatory network effect may be better markers of an increased AD risk. Still given that there are only 2 network studies even this seems a bit of an overstatement. In either case, please clarify this paragraph.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Oscillatory hyperactivity and hyperconnectivity in young APOE-ɛ4 carriers and hypoconnectivity in Alzheimer's disease" for further consideration at eLife. Your revised article has been favorably evaluated by Huda Zoghbi as the Senior Editor, a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviews below provide details about the limitations that need to be addressed. In summary, all reviewers agree that revision of the text (especially the claims) and figures is still needed. Please revise the text putting special emphasis on the limitation/claim parts and on the details of the methodology. While we agreed that no additional analyses need to be done, the epoching of the time series should be mentioned, perhaps in limitations.

I hope that the comments below will help you revised the manuscript.

Reviewer #1:

The authors have evidently gone through a big effort in re-analyzing the data and in replying to the reviewer comments on the earlier manuscript. I think that the machine learning approach gives a significant contribution to the analyses.

As to the present manuscript, I would still be careful in using words like "prevention" from which the present data is still quite far. Providing possible predictive information on AD in very early stage is already an important step.

In general, the language is not always best possible and could still be clarified and polished. Also, the amount of given details on the data analysis continues to vary, which would make it difficult to replicate part of the applied analyses: e.g. the analysis based on Graph Theory (subsection “Statistical Analysis of Group Differences in Connectivity”) mainly refer to existing toolboxes, while the SVM approach is rather extensively explained.

Reviewer #2:

The revised paper is significantly improved in terms of clarity of the methods and results. While many of my concerns have been addressed, the number of revisions performed by the authors have prompted a few additional comments:

I have a concern about the division of the time series into 2 second epochs, removal of segments with artifacts, followed by concatenation. While the number of retained epochs were consistent across groups, what about the number of discontinuities introduced into the time series? For example, removing two adjacent epochs would result in one discontinuity, while removing two separate epochs would result in two discontinuities. What is the impact of this on the connectivity? This may be particularly problematic for the lowest frequency band; there will only be 2-8 cycles of the 1-4 Hz band. I am not suggesting that the analyses be re-done, although some commentary on this point may be warranted.

Why was a visual grating used rather than a more "pure" resting state study?

In Figure 1 – I'm not sure how relevant row 2 is, given that I would expect many connections to survive a p<0.05 uncorrected threshold by chance alone. This is especially true since row 2 is quite similar to row 4. Also, in this figure, given the narrow width of the lines, I can't visually detect any differences in opacity. Perhaps line width would be a better indicator of connection strength?

In Figure 2 - I'm not entirely clear on the utility of the lower panel. Although there is some overlap with the areas showing higher gamma activity and areas showing greater connectivity, it is not entirely convincing that these two things are related in any way, given that more regions that don't overlap than regions that do.

Figure 3 – same comment as for Figure 1.

Figure 4 – it may be useful to show which specific connections do overlap, perhaps a conjunction of the graphs shown in the bottom panel of 4A. Is there a negative correlation between the strengths of the connections that are in this conjunction? How many edges actually overlap?

I am concerned that the results are somewhat overstated in the conclusions. There was at best partial overlap between the oscillatory power and connectivity results. Likewise, there was only partial overlap between the connections found in the young sample and the older sample.

Some comment on the regions showing the greatest abnormality may be helpful to put the results in context.

Reviewer #3:

This is a follow-up review on the study by Koelewijn et al. that looks at changes in the oscillatory connectivity in resting state MEG in APOE-ɛ4 carriers and matched controls. The authors have, in my opinion replied to the reviewers’ comments and suggestions in a satisfactory manner, and I am ready to suggest that the manuscript be accepted for publication in eLife.

Before signing off on this review, I would nonetheless like to express that I am somewhat disappointed that the authors, contrary to my suggestion, chose not to change the parcellation template used in the connectivity analysis. I am sympathetic to the authors' argument that the AAL is widely used, but this does mean that it's a good one. Most likely the reason, that is widely used is merely a consequence of the methodological dominance of fMRI where the template is much less problematic. As the authors themselves note in their Discussion, it remains a fact that the AAL is not well-suited for connectivity analysis of MEG data. Bad practices in science do not change unless someone leads the way. Hence, I encourage the authors to at least in their future studies become trail makers that help change suboptimal practices, and thus advancing also the validity of MEG.

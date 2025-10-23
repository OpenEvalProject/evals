# Peer review - Round 1

Editors:
- Chris I Baker, National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63905.sa1](https://doi.org/10.7554/eLife.63905.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study investigates how dysfunction in the anterior temporal lobe (ATL) alters dynamic activity during semantic categorization. Magnetoencephalography (MEG) responses were contrasted between patients with semantic variant Primary Progressive Aphasia (svPPA) and age-matched healthy controls. Despite similar profiles of behavioural performance on the categorization task, the svPPA patients showed enhanced γ synchronization in the occipital lobe compared to controls suggesting an increased engagement of early perceptual mechanisms for completing the task, as opposed to semantic identification of the picture.

Decision letter after peer review:

Thank you for submitting your article "Neural dynamics of semantic categorization in semantic variant of Primary Progressive Aphasia" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Chris Baker as Reviewing and Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alex Clarke (Reviewer #2); Aneta Kielar (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Borghesani and colleagues aimed to understand how dysfunction in the anterior temporal lobe (ATL) alters dynamic activity during semantic categorization. They contrast MEG responses between 18 patients with semantic variant Primary Progressive Aphasia (PPA) and 18 age-matched healthy controls. Both groups show similar profiles of behavioural performance on the task, and broad similarities in MEG responses. Critically, however, svPPA patients show enhanced γ synchronization in the occipital lobe compared to controls. The authors interpret this as reflecting increased engagement of / reliance on early perceptual mechanisms for completing the task, as opposed to semantic identification of the picture.

Overall, the reviewers found the manuscript interesting. As svPPA is a rare (but scientifically informative) disorder, the sample size is impressive, and given that relatively few MEG studies exist in PPA at all, this is an interesting dataset. However, the general opinion is that the results could be more fully characterized, which would allow for more expansive interpretations and inferences.

Essential revisions:

1) Statistical thresholding

Using a high threshold prevents false positives, but may also lead to false negatives, and that may be the case here, with the high threshold contributing to an unrealistic impression of spatial specificity in MEG. It is obvious from the average responses in both groups that these oscillatory responses are widespread through the brain. Indeed, the α and β responses are significant in the majority of cortical voxels. This basic property of the responses should be presented clearly and prominently in the paper – not just in supplementary information where only a minority of readers will even see it. The authors then use an extremely high and conservative statistical threshold to contrast differences between the two groups. P<.005 uncorrected is a highly conservative threshold already, even before cluster-thresholding is added (although with data as smooth as MEG beamforming solutions, cluster-thresholding is unlikely to change anything). Essentially, this makes only the strongest part of the activation survive, and while it is valid to conclude that a significant group difference exists (protected from Type 1 error), this can also give a false impression that the difference is specific to that region. A more realistic characterization of the results would involve measuring differences in the strength of the responses between groups on a broader level, possibly the sensors or in large ROIs – and not ROIs pre-selected to show a dramatic difference by first searching the whole brain for the most significant effects – that is the classic "double-dipping" fallacy in neuroimaging.

2) Frequency bands

The ERD/ERS in each frequency band is treated as a separate entity, ignoring the fact that these bands are arbitrary and frequency is a continuous quantity. This matters because much is made of the fact that svPPA participants exhibited greater ERS in the low-γ range, and that this was correlated with reaction time. Supplementary Figure 1 shows that both groups had strong occipital ERS in the high-γ range, but only svPPA showed it in the low γ range as well. This suggests that the ERS in the svPPA group may simply have been shifted to a lower frequency range. A more fulsome characterization of these group differences via time-frequency analysis and/or power spectral analysis would help clarify what is going on here.

3) Decreased responses in svPPA?

It is surprising that svPPA participants only exhibited increased MEG responses compared to controls – assuming that both γ ERS and β ERD can be interpreted as increased neural activation, which is a reasonable assumption based on the literature. No decreases in the svPPA group are found, and thus the observed increases can be plausibly attributed to compensatory processes as framed by the authors. However, certain analysis choices may play a role in producing this data pattern. In particular, the authors state (line 611): "To remove potential artifacts due to neurodegeneration or eye movement (lacking electrooculograms), we masked statistical maps using patients' ATL atrophy maps (see section MRI protocol and analyses), as well as a ventromedial frontal mask."

It is not clear whether this masking was conducted in group space from average atrophy maps, or on an individual level. In either case, this is not well justified. What is the physical mechanism by which tissue undergoing neurodegeneration can be said to generate an artifactual signal? Atrophied tissue still contains living neurons with ionic currents; these are real signals not artifacts, and furthermore, atrophy is a continuous process with tissue further from the epicenter also undergoing similar neurodegenerative mechanisms. Atrophied tissue may well generate electromagnetic signals that are different from healthy tissue, and such differences should be included in this paper. There may be regions of hypoactivation as well as hyperactivation in this svPPA group. If the hypoactivation localizes to atrophied tissue and the hyperactivation to other regions, that will bolster the case that we are seeing compensatory processes, but it isn't certain with half the story masked. The statistical masking of the frontal region is also not really a valid solution to eye movement artifacts. The authors would have to present evidence that the region that they masked corresponds to the region potentially affected by eye movements. However, many studies have found that beamforming already does a pretty good job of removing ocular artifact from estimated brain signals, except for very close to the eyes.

4) RT correlation

The correlation with reaction time in the occipital cortex is consistent with the idea that the ERS there may reflect compensatory overreliance on perceptual information, but it isn't conclusive. The authors suggest that svPPA patients are able to categorize the stimuli correctly based on visual features, but are unable to name them. What about testing for correlations with the out-of-scanner behavioural measures that established that the patients have a naming deficit? It would strengthen the case if atrophy or hypoactivation (see comment above) correlated with the naming deficit.

5) Neural dynamics

As the paper is about 'Neural dynamics', this aspect could be developed, with the timing of the effects characterized further, and considered more in relation to the conclusions. For example, the main finding is the increased occipital γ response in svPPA compared to controls. Looking at Figure 3, there is a peak in the svPPA group near 200 ms, and very little synchronized activity in the control group. This is interesting as there are many ways we could have seen svPPA > controls, but this suggests that the γ synchronization response associated with compensation is specific to the svPPA group (and largely absent from controls – also from Supp Figure 1), and is distinguished from an initial visual evoked response (peaking ~100 ms). We recommend discussing and characterizing the dynamics of this effect more, such as what a later occipital effect could tell us about dynamics given ATL dysfunction? Is this increase a result of a lack of top-down effects from ATL?

6) Low-level vs. High-level

The occipital γ effect looks like the primary visual cortex, which might suggest the effects are not related to higher-level perceptual features (such as has eyes, teeth) as the authors suggest, but rather low-level visual effects. Do the authors perhaps think the effects could relate to enhanced processing of visual details (as related to the ideas of Hochstein and Asher's reverse hierarchy), or whether the effects relate to additional visual input following a visual saccade?

7) VBM

The VBM results for the svPPA patients were surprising given that all the atrophy appeared in the left hemisphere. There can be hemispheric differences in svPPA, but is this a true lateral pattern (meaning the right ATL is intact) or a product of VBM being run so that the most atrophied hemisphere is shifted to the left side? If the VBM maps are correct, and the svPPA patients are only showing left hemisphere atrophy, then what does this suggest about the role of the right ATL, and the bilateral nature of occipital increased in svPPA?

8) Task performance

Both svPPA patients and healthy controls achieved around 80% accuracy in the categorization task. This seems surprisingly low given, (1) the task (living vs. nonliving after seeing the image for 2 seconds), (2) that all the images were pretested and had high name agreement, and (3) that items were repeated on average 2.5 times. Is there something that explains this low performance for all individuals?

9) Compensation

One question for clarification is whether the recruitment of the occipital areas in svPPA is truly "compensatory", does it indicate a shift of resources due to the anterior temporal atrophy. Is the recruitment of the parieto-occipital regions associated with more accurate performance?

10) Other frequency bands (related to point 2 above)

The main results concentrate on the differences between patient and controls in the low γ range. There are also significant effects in the other frequency bands (e.g., high γ, β and α). What is the functional significance of these effects?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Neural dynamics of semantic categorization in semantic variant of Primary Progressive Aphasia" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Chris Baker as the Reviewing and Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jed A Meltzer (Reviewer #1); Alex Clarke (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. In general, the reviewers are still positive about the manuscript but think that the claims need to be tempered slightly and would like to see the time-frequency dynamics presented in more detail (as requested in the original reviews).

Essential Revisions:

1) Further analysis of the time-frequency dynamics is needed as laid out in the reviewers' comments below.

2) While the findings are consistent with a compensatory interpretation, especially given the equivalent performance in both groups, other interpretations are also possible. This should be discussed more fully, and the discussion could be grounded in earlier literature that has considered similar compensatory accounts e.g. age differences – for example many papers by Cheryl Grady show that older adults have more bilateral activation than younger. Those results were considered in the context of what kinds of findings constitute evidence of compensation vs. pathology.

Reviewer #1:

The revision by Borghesani et al., is much improved in terms of technical procedures and description, and most of the concerns raised by the reviewers have been adequately addressed. It is an interesting finding in a somewhat rare patient group.

I really only have one remaining concern that I still think should be addressed.

This paper puts a lot of emphasis on a particular interpretation of changes in oscillatory dynamics between the svPPA group and the control group. Based mainly on one particular finding – increased low-γ ERS in the occipital cortex for the svPPA group, the authors argue that svPPA patients compensate for their conceptual impairments by increasing their reliance on early perceptual processing implemented in occipital areas. Originally this interpretation was supported by both the increased low-γ ERS and also a correlation with performance. Since the changed analysis procedures resulted in dropping the claim of correlation, everything now rests on the shoulders of that low-γ finding. I think it needs to be unpacked a bit more.

If the increased low-γ finding were unambiguously interpretable as "activation" or "recruitment," this would be a straightforward story. But MEG data is complex and nuanced, more so than fMRI in my opinion, and there are some nuances here that are being overlooked. Both groups have robust activation in a higher band, high-γ, a band which is more strongly linked to increased neural firing and increased BOLD than the low-γ band is. On the other hand, the patients appear to have somewhat less ERD in the β band in this area, and β ERD is also strongly linked to neural firing and BOLD. The low γ band is kind of tricky – sometimes it goes up, sometimes it goes down. To understand this more, it would definitely help to see a real time-frequency decomposition of the activity, at least in this one key area.

We asked for this in the first round of review, and the authors declined to do it, citing concerns about time-frequency resolution tradeoff. That is not very convincing – there is ample resolution available in this data to characterize the effect in both time and frequency, and anyway in this case it is really frequency that raises the important questions – the group difference lasts for at least 400 ms so fine temporal resolution isn't so necessary. The authors argue that a lack of significant difference for the high γ band argues against a "frequency shift" interpretation – perhaps "spread" would be a more precise term than shift; in any case, it is clear that frequency is a key dimension in the difference of oscillatory response between these two groups, and it needs to be characterized better given the importance of this finding.

Perhaps a more practical concern is that the authors used optimized beamforming weights for specific frequency bands, precluding a traditional broad-band time-frequency analysis. However, they can still characterize time-frequency reactivity using an additional post-hoc analysis. This could be done on the sensor level, which I understand the authors do not prefer for legitimate reasons, but it could also be done in source space with non-frequency-optimized beamforming weights. This may not afford the same spatial resolution, but the blob of differential γ activity between groups is very large; precise spatial resolution isn't needed to answer this question.

I also think that given this ambiguity in the central finding, the authors should soften their conclusions somewhat and offer alternative interpretations. There is certainly a difference in the occipital lobe between groups, and that is interesting, but the idea that it's a compensatory increase in the patient group is somewhat speculative – consistent with the data, but not proven.

Reviewer #2:

I've read through all the comments and review responses, and think overall the manuscript is improved and several points made clearer.

I think there are a few points that remain for me:

1. The source analysis procedure is clear, along with thresholding and cluster extent. Yet, I didn't see any information on how the authors control for the effects over the sliding time windows, or for the frequency bands? We're these statistical contrasts taken into account?

2. New ROI data is presented showing the effects in 3 regions and across the frequency bands, with the authors claiming a difference in low γ activity around 100 ms. Yet stating the effect is around 100 ms doesn't seem to capture the data in the plot. It looks like difference may first appear around 100 ms, but peak nearer 200 ms, and continue throughout the epoch. I think a fuller description is warranted.

3. The ATL is no longer masked out from any of the analysis, and I would state this somewhere for clarity. There is also apparent signal coming from the atrophy region – mainly in β and α – it might be worth commenting on this.

4. Finally, to avoid switching back between Figures 2/3 and Table 3, I would consider adding if the effects relate to ERS or ERD in the table.

Reviewer #3:

I thank authors for addressing reviewers' comments. I think that the manuscript has improved. I don't have further comments.

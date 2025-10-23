# Peer review - Round 1

Editors:
- Jody C Culham, University of Western Ontario , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09600.016](https://doi.org/10.7554/eLife.09600.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Using an achiasmic human visual system to quantify the relationship between the fMRI BOLD signal and neural response" for peer review at eLife. Your submission has been favorably evaluated by Timothy Behrens (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors (Jody Culham) and another is Jonathan Victor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

In a clever, elegant, and detailed set of experiments, this study uses a rare individual with achiasma (lack of an optic chiasm) to address how the fMRI (blood oxygenation level dependent or BOLD) signal summates. In achiasma, mirror-symmetric locations of the left and right visual fields are mapped to the same cortical location in visual areas. However, as careful psychophysics and fMRI adaptation experiments here show, stimulation at one site has negligible behavioral or neural effects on processing at the mirror-symmetric site. As such, achiasma provides a unique natural case study to investigate BOLD summation between effectively independent neural populations. The paper shows that doubling the stimulation sites in an achiasmic individual does not double the BOLD response; rather the BOLD response is approximately proportional to the square root of the neural response. These results are of general interest in neuroimaging considering the common use of BOLD fMRI to infer neural function.

Overall the referees were favorable, with all reviewers commenting favorably on the care and detail with which the project was executed.

Essential revisions:

Two main issues were raised by multiple reviewers and must be addressed in a revision.

1) First, two reviewers raised concerns about the imperfect mirror symmetry of the representations in the two visual fields. This must be addressed directly in the Discussion.

Reviewer 1/Reviewing editor:

The data in Figure 1C suggest that the representations across visual fields are largely but not perfectly homotopic (i.e., most points lie below a slope of 1 – and the data look similar across visual areas). Thus one concern is whether the choice of exactly homotopic locations may mean a slight displacement between the retinal locations stimulated, which could affect the data. If I were a stickler, I'd suggest an experiment in which stimulation was delivered to the visual location in the opposite field as determined by fMRI mapping). However, eLife policy is that if new data are essential to the conclusion, the paper will be rejected; in this case, I'm not sure the data is strictly essential. However, this concern needs to be noted and discussed.

Reviewer 3:

The assumption of colocalisation: Large-scale co-localisation of opposing hemifields is clearly demonstrated in the data. However, the representations of the relatively small mirror-symmetrical patches used might not fully overlap due to slight shifts in the representations. This is actually suggested by the eccentricity representations of both hemifields in Figure 1C, where e1 exceeds e2 for by far most voxels in all visual areas examined. This potential problem needs to be addressed directly in the manuscript, e.g. a conservative ROI definition might help here. A related issue are potential partial voluming effects for the comparatively large voxel size used (3 mm isotropic), which might include cortical areas that are not driven by the stimulus, e.g. potentially negative BOLD effects.

2) Two reviewers raised concerns about discrepancies between visual areas. This must be addressed in the revision.

Reviewer 2:

My main substantive concern is the way that the authors present and interpret the discrepancy between V1 and the other areas, V2 and V3. Specifically, for V2 and V3, the confidence limits for the power law exponent include 0.5, and are similar for 6-sec and 1-sec presentations. But for V1, the 6-sec presentation yields a power law of about 0.75, with confidence limits that don't overlap with those for V2 and V3. The 1-sec V1 measurement is like V2 and V3, with confidence limits centered on 0.5. The authors interpret the finding that the 6-sec V1 measurement is closer to 1 as a result of less-complete overlap of the vasculature between the columns. While this may be true, it is unclear why the 1-sec measurement doesn't also show the same effect. So if the non-overlap issue is to be suggested as a plausible explanation for the V1 vs. V2/V3 discrepancy, something needs to be said about why only the 6-sec measurement shows its effect. Whatever the authors do on this point, I think that it is important to add that the explanation is at least somewhat conjectural, and one does need to also maintain the possibility that V1 is somehow different in terms of Z-to-B coupling. The paper's core contribution remains valid and important – the Z-to-B coupling is clear sublinear, in contrast to previous claims.

Reviewer 3:

Treatment of V1 data: V1 data and V2/3 data do not fully match. Therefore, the authors decide to concentrate on the V2/V3 findings. Given the large voxel size used I am not convinced that the respective discussion on V1 hemifield dominance columns fully resolves this issue. The partial exclusion of the V1 data appears critical, especially as we are already dealing with a single case study and the authors draw fairly general conclusions from this data set.

Recommended changes or considerations:

The following points/suggestions should also be considered in the revision, though there is some flexibility for the authors to deal with these as they see fit.

1) The biggest limitation of the study is the small sample size (n=1). The authors nicely addressed potential concerns in the cover letter to the journal. I suggest briefly including some of these arguments in the Discussion of the manuscript.

2) The Reviewing editor found the hypothetical wording of the last paragraph of the Introduction peculiar. While it fulfills the authors aim – to focus the paper on the BOLD question rather that achiasma per se – it would flow better to bring up achiasma first, explain the cortical retinotopic organization, and then explain why it's an ideal model for this particular question.

3) The following comment of Reviewer 2 should be considered: “Secondarily, I would not emphasize the specifically ‘square root’ nature of the relationship; in the absence of a mechanistic basis for such a relationship, it is a phenomenological model, and the exponent just happens to be in the neighborhood of 0.5 (for V2 and V3)”.

4) The authors should consider the following suggestion from Reviewer 2: “I think it is possible to infer the value of the scaling exponent by a simpler procedure, with fewer assumptions. I hope the authors will consider doing this, as it bypasses a complex step that I think is inessential.

But I don't think it's an either-or matter – the suggested simpler approach goes directly to the power-law approximation; the authors' approach uses a spline for the contrast-response as a stepping stone to the power-law fit. One can argue that bypassing the contrast response function is an advantage (because of simplicity and reduced assumptions) or a disadvantage (since it misses an opportunity for contact with known physiology). So these approaches are complementary, and optimally, I think that the authors should retain their original analysis but also add the proposed analysis, as follows:

The suggestion for the simpler analysis is as follows. The starting point is the set of values (z_i, 2z_i) at which they have measured the BOLD responses b_i,1=b(z_i) and b_i,2=b(2z_i). If one assumes a power law b=z^g, then the ratio of a pair of B measurements directly gives the scaling exponent g: b(2z_i)/b(z_i)=2^g. So one can plot these ratios, b(2z_i)/b(z_i), as a function of the index i, and see if these ratios are independent of i – or alternatively, if a trend emerges. If there's no trend, then the power law approximation is valid, the inferred value of the exponent g is the average of these ratios (optionally weighted by their reliabilities). If a trend emerges (which I doubt, given the good fits in the paper), then a power-law relationship cannot hold”.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Using an achiasmic human visual system to quantify the relationship between the fMRI BOLD signal and neural response" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor) and Jody Culham (Reviewing editor).

The manuscript has addressed the concerns raised in the original review but there is one new paragraph that requires revisions to enhance the readability. The problematic paragraph is the last one of the Discussion beginning, "Given their progeny of being binocular neurons…". The first sentence did not make much sense (what are "progeny of being binocular neurons"?). It also did not set up the main goal of the paragraph, to address the discrepancies between areas. Overall, this paragraph should be rewritten/edited to make the arguments clearer.

Once this paragraph is cleaned up, the paper will be accepted without further ado.

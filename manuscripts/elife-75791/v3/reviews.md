# Peer review - Round 1

Editors:
- Ben S Cooper, https://ror.org/01znkr924 Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75791.sa0](https://doi.org/10.7554/eLife.75791.sa0)

This manuscript will be of broad interest to readers interested in understanding the characteristics of variants in ongoing epidemics that lead to faster (or slower) growth rates and will be of particular interest to those wishing to understand the factors leading to the selection of SARS–CoV–2 variants. The selective advantage of a novel strain of a pathogen depends not only on its relative transmissibility but also on its generation time relative to other strains; the relation between transmissibility, transmission advantage and generation time changes across different phases of the epidemic. Key innovations in this paper are a robust framework for using this relationship to make statistical inferences about both the transmissibility advantage and generation time of an emerging variant and conceptual novelty in the general investigation of selection on infectivity profiles. The approach is supported by simulation studies and applied to the Alpha and Delta SARS–CoV–2 variants to show that selection was likely driven by changes in transmissibility rather than changes in the generation time.


---

# Peer review - Round 1

Editors:
- Ben S Cooper, https://ror.org/01znkr924 Mahidol University Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75791.sa1](https://doi.org/10.7554/eLife.75791.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Selection for infectivity profiles in slow and fast epidemics, and the rise of SARS–CoV–2 variants" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. There is a need to clarify the relationship between changes in transmission and changes in selection more explicitly in the text. (specific suggestions for how this could be done are given by reviewer #1)

2. Relevant previous work should be cited and the abstract should more clearly highlight the novelty of this work

3. Additional analysis to establish robustness of the conclusions to assumptions would be helpful (as outlined by reviewer #1)

4. Please highlight the broader applicability. As currently framed the emphasis is on changes in transmissibility due to control measures, but similar considerations apply if there are changes over time in transmissibility for other reasons.

5. Emphasise limitations, for example caveats related to the possible immune escape properties of the Delta variant , and potential biases introduced by vaccination.

6. Could the authors comment on the amount of necessary data (length of the time series) for the method to be useful

7. Clarify multiple country Delta analysis to address reviewer #2's concern.

Reviewer #1 (Recommendations for the authors):

That said, I found myself confused about several points. Most of these issues can be easily clarified, and I encourage the authors to tackle these points to avoid confusion.

The first confusion stems from the idea, described in Day et al. (2020), that selection for transmission isn't constant but declines when contact rates decline. Subsequently, during this pandemic, we have repeatedly observed a decrease in selection for VOC when public health and individual NPI measures increase, as seen as a decrease in s with stringency index (Figure 3, Otto et al. 2021) and as a "kink" in frequency–over–time plots (Figure S2, Otto et al. 2021). This kink is also visible in the current manuscript (Figure 4A), with Α being more strongly favoured prior to week ~50 than after.

It was easy as a reader, however, to think that selection on transmission was modelled in this paper as a constant, not varying with control measures. Diving into the methods more, this isn't the case, but it was easy to miss it. I would suggest clarifying the relationship between changes in transmission and changes in selection more explicitly in the text.

For example:

– Equation (5) – I suggest renaming the terms s1–s3 as delta1–delta3 or some other letter. Labeled with an "s", like the selection coefficient makes it easy to think that selection for transmission is s1. In fact, selection for transmission is given by rE–rH, as in equation (6), which is not linear in the s1–s3 terms. Even when R~1 (r~0), selection is s1/muH. This is because selection to leading order depends on changes in the transmission rate (call this β), not changes in R, consistent with equations (1) and (S6) in Day et al. [This is visible in the grey curves in Figure 1C,D, but I think most people would miss this.]

– In a related way, I saw Figure 5 and thought the analysis was assuming that selection was constant as rH varies. This isn't assumed but is a function of R being near enough to one over the x–axis that the curves do look linear. Still, if one plotted the selection (s=rE–rH) versus rH, it would be easier to see that selection does depend on the growth rate in the model, weakening as rH decreases, even over this span of rH values.

– What about the kink? This analysis hides a bit the temporal changes in selection. Figure 5B makes it seem like selection is constant over the time course, but Figure 4A (and logit plots) shows more of a breakpoint, with stronger selection earlier and weaker selection later. I would suggest some discussion of this; while the kink looks discrete in estimates of selection from Figure 4A, the interpretation in this paper would be that the kink is caused by a sharp reduction in rH, but this is hard to see in Figure 5B (potentially because of noise in the estimates of rH and rE). Any larger change in selection, beyond that predicted by changes in rH, could be examined by fitting a breakpoint in the likelihood analysis (future work). I think that this could be brought out more clearly as a strength of the paper – we expect the strength of selection to change with changing control measures, but the current work attempts to estimate the constant changes to the underlying parameters.

– Because R describes the transmission per generation, wouldn't inferences of s1 capture both changes in transmissibility and changes in the generation time (mu)? However, s1 is discussed only in terms of a change in transmissibility. Wouldn't it be clearer to dissect the two (R=β–(mean generation time)) and focus on selection via the transmission rate per unit time (β) versus selection on the mean generation time? Alternatively, care should be taken throughout to avoid talking about s1 as a change in transmissibility (it is more accurately described on line 358 as a change in the number of secondary infections).

In addition to clarifying the above, other issues that I think would strengthen the paper are:

Citing previous work, not just Day et al. but also the earlier literature (e.g., refs 11, 13, 14, 19 therein). The abstract and text (e.g., line 115, 300) makes it seem like this is the first work to dissect selection into components coming from different disease life history traits (transmission, time to infectiousness, clearance rate, etc.), but there is substantial prior work on this. The novelty, and the focus of the abstract, should be on inference of these components.

It would be good to get a better sense of the robustness of the inferences to changing various assumptions:

– Non–gamma infectiousness curves (e.g., a curve that adds a delay to the start of infectiousness).

– Lags in measuring case case numbers, as individuals typically don’t get tested until having symptoms. A lag is in the simulation, but I didn’t get a sense of how changing the lag affects the inferences.

– Allowing shifts in contact rates or NPI – the method assumes steady state distributions at all times, it might be easier to get at the transients by having a discrete change in r from high to low values and seeing how the inference of the s terms change over time.

Reviewer #2 (Recommendations for the authors):

– I think the emphasis on "level of epidemic control" is misplaced. The whole analysis may work also in an uncontrolled epidemic, right? All that matters is that the effective reproduction number varies significantly with time.

– I would discuss briefly the biases that could arise from incomplete cross–protection or different vaccine protection, in order to clarify the applicability of the method. At present, I think the limitations are not clear enough, and they should be emphasised.

– This approach seems to require a quite dense/long time series. Could the authors comment on this requirement?

– I find the notation for the parameters s1,s2,s3 most unintuitive: s1 is a selection coefficient, but the others aren't, and s2 actually behaves in the opposite way. I'd suggest to pick a more intuitive notation, e.g. Rrel,gtrel,sdrel or any other variant.

– For the Δ analysis: could you briefly discussed the caveats related to the possible immune escape properties of the variant?

– Also for the Δ analysis: multiple countries can differ in their epidemiological situation and therefore correspond to different combinations of R and generation time for the Α variant. It is unclear to me how this may affect your cross–country analysis.

# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79121.sa0](https://doi.org/10.7554/eLife.79121.sa0)

This is a thorough, fundamental study assessing suppression gene drives against mosquitos. The models specifically consider the spatial dynamics of gene drives and whether a form of group selection may prevent the drive from eradicating the population, with mosquito ecology parameters, leading to compelling results. This manuscript will be of interest to those working in the technical development of gene drives, those predicting how such genetically modified insects would spread in the wild, and those evaluating the technology from regulatory and funding standpoints.


---

# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79121.sa1](https://doi.org/10.7554/eLife.79121.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Finding the strongest gene drive: Simulations reveal unexpected performance differences between Anopheles homing suppression drive candidates" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Sebald A.N.R Verkuijl (Reviewer #1); Jim Bull (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers are positive overall about your paper. As you will note from the full reviews further below, consistent comments included that model parameter value changes could lead to different quantitative results and the desire for a more explicit discussion of what is leading to the results. In our consultation discussion, there was a clear consensus that these and other points could be addressed with thoughtful text revision rather than major new analyses. In summary:

1. Expand the justification of your chosen parameters.

2. Expand discussion of the limitations of your study. Consider both of these points in the context of the perspective of the developers of the zpg drive.

3. Add a summary of what fundamental drive biology differences may be leading to your results in terms of the drive efficacy differences between the Anopheles-specific and general model. And is the seemingly detrimental effect of adding an X-shredder due to suppressing female abundances or to something else?

4. Given that gene drives are being evaluated for potential release suitability, the specific focus of this paper may cause it to attract considerable interest from a non-domain expert audience. As such, consider how you might make the writing more accessible to such an audience (including but not limited to explicitly discussing potential limitations of the study as mentioned above, and maybe even modeling in general).

5. Please also consider each individual item noted in the below reviews, and include how you addressed each comment in your point-by-point responses.

Reviewer #1 (Recommendations for the authors):

Sharing the model code is appreciated. I am unfamiliar with PhP and SLIM and was not able to evaluate the model code in the time I had (a limitation of my review, not a reflection of the paper/model).

The authors have gone through considerable effort to get parameter estimates from experimental data. This is very much appreciated. Table 1 gives an overview of the parameters used in the model and may give the impression that the distinction between the nos and zpg drives is substantial.

However, if it is reasonable to explore interpretations of drive data with a 0.45 difference in fitness, I don't think it is meaningful to make a distinction between the common core parameters of the nos and zpg drives (0.02 difference in male HDR, 0.01 difference in male germline resistance, 0.06 difference in maternal embryo resistance rates). It suggests those parameters are known to a far higher certainty than the parameters you vary from drive to drive.

In my opinion, this difference in core parameters needlessly obscures the comparisons between the nos and zpg drives. For example, I would suggest that zpg2 and nosF are practically equivalent conditions with regard to the accuracy of the parameter estimates and the limitations of any computational model. When there is a substantial difference between these conditions it says more about the sensitivity of the model outputs to the starting conditions than any meaningfully accurate estimate of how nos and zpg would differ under those conditions.

Another example: I understand that based on a certain interpretation of the experimental data it may be more reasonable to assume the nos drive has no fitness costs than that the zpg drive has no fitness cost. But simulating the no fitness cost scenario only for nos needlessly obscures the fact that is a practically identical approximation (again, in regards to the accuracy of the parameters and limitations of modelling) of how the zpg drive would perform with no fitness costs.

The authors may consider using the same core parameters for both drives making it easier for the reader to understand what truly underlies the differences between conditions. Allowing comparisons between all 8 conditions, instead of only within 2 groups of 4. Alternatively, the authors can make clear in the text that the difference between the zpg, and nos drives will mostly be due to the fitness/deposition/x-shredding parameters. That realisation also made it much easier for me to understand the results.

The above point may be superseded by this one: The parameters for the nos drive are taken at the nudel locus. The estimates for zpg-Cas9 are taken at the dsx locus. This is despite the fact that the zpg-Cas9 was also tested at the nudel locus and I think performed better there than at the dsx locus (the benefit of the dsx locus being the reduced possibility of functional resistance alleles). As such, I don't think this is a fair comparison, as the nos drive may well show the same reduction in fitness if moved to the dsx locus. And it would not be viable at the nudel locus due to the possibility of functional resistance alleles. The fact that the nos promoter has not been tested at the dsx locus is mentioned, but I think it has not been justified why the more 'fair' comparison at the nudel locus has not been used. Even if both nos and zpg would not perform well at the nudel locus in any real-world test, this study draws conclusions about their relative strength. So it still seems that is a more relevant condition.

Reviewer #2 (Recommendations for the authors):

My major concern is the Anopheles-specific model, including

1) The robusticity of the parameter estimates informed by literature (e.g., what are their likely confidence intervals), and

2) The sensitivity of the model to the different parameters chosen. A well-designed table can address point #1, as noted in the Public Review. For point #2, essentially what I would like to know is what is driving the difference between the outcomes of the discrete generation model and Anopheles model (Figure 1)? By rerunning the simulation with intermediate parameters between the two models, can you tell what is predisposing the Anopheles model to long-term chasing? You note that "[t]hese differences between models were likely at least partially due to the high reproductive capacity of Anopheles mosquitoes," but can this be shown by rerunning the Anopheles model with lower reproductive capacity? Given the stark differences between the outcomes of the two models and the centrality of this difference to your study, I feel such an addition would be useful.

Reviewer #3 (Recommendations for the authors):

Assuming I did not miss it, the paper lacks overviews of WHY the different constructs give rise to different outcomes. I think the authors should consider providing some kind of heuristic explanation of the main differences. For example, the inclusion of X-shredding with female sterility seems to hurt drive success. Is that for an ecological reason (e.g., the drive's greater efficacy on a local scale provides stronger group selection)? Alternatively, it might be something about drive specifics that is responsible for the effects described.

Since drive properties may change from lab to lab, it is worth telling the reader whether the important effects observed here are due to properties that may change with subtle improvements in engineering, or are instead due to basic ecological properties that have little to do with construction nuances.

trivia:

page 2 of the manuscript: 'we still lack a complete understanding of the effects …' can be said no matter what. The claim could be modified to have some meaning.

'chaotic' has a specific meaning in analysis. Is that what is meant here, or is the word chosen just to mean irregular?

page 3: 'Since this target gene is haplosufficient, female drive heterozygotes are potentially fully fertile' I imagine the model assumes full fertility, not potential full fertility.

page 4: first full paragraph. More detail could be used here. And I am guessing that the point of the dual strategy is that the drive causes an increase in the shredder, but the paragraph seems to omit this basic point.

'In the zpg and zpgX drives (but not the zpg2 and zpg2X drives)' -- I didn't easily find a description of what those are.

page 5: I'd like a bit more detail about how the model operates. Maybe a figure or table?

page 11: 'the drive must induce a sufficiently high genetic load in order to overpower the growth of wild-type populations at low density' Overpowering the growth of wild-type POPULATIONS? This is the panmictic model, so I would expect there are only wild-type genotypes. If my comment does not make sense, it's because I don't know what is being said.

Figure 1 legend: 'Offspring were artificially generated from fertile individuals at high rates to prevent complete population suppression ' I'm guessing this means that the population would have disappeared if fecundity hadn't been massively boosted. There might be a more direct way to say it. But why not let the population go extinct?

Page 12, top paragraph. Explain what (a) – (d) mean in population terms.

Page 15: 'The genetic load values measured by both models was within 1% for all of the drives (Figure 1)' Not clear -- what does 1% for all of the drives mean? The reference point is not clear.

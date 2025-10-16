# Peer review - Round 1

Editors:
- Joris Deelen, https://ror.org/04xx1tc24 Max Planck Institute for Biology of Ageing Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72031.sa0](https://doi.org/10.7554/eLife.72031.sa0)

This paper investigates the impact of seasonal variation (e.g. nutrition, environment, and infection) in rural subsistence farmer communities in the Gambia on DNA methylation levels in children. The authors identified a set of CpGs that are associated with season of conception and show that these associations are likely driven by periconceptional environmental influences. These findings open the door for future studies of environmentally sensitive CpGs to link early life exposures to diseases occurring later in life.


---

# Peer review - Round 1

Editors:
- Joris Deelen, https://ror.org/04xx1tc24 Max Planck Institute for Biology of Ageing Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72031.sa1](https://doi.org/10.7554/eLife.72031.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Environmentally sensitive hotspots in the methylome of the early human embryo" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Toby Mansell (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Below are first the most important points coming from the discussion between the reviewers, followed by additional points coming from the individual review reports.

1) The reviewers are worried that there is residual confounding impacting the analyses and that the authors only observe increases in DNA methylation. Regressing out sex is not sufficient to show there is no bias in the analyses. We therefore request a correlation matrix (containing rho's, not p-values) containing all batch effects, arrray covariates (e.g. sentrix row and column), biological covariates (e.g. sex), PCAs before and after functional normalisation, and study covariates (e.g. village, month of collection, month of birth, month of conception). This matrix should show if there is residual confounding remaining that should be taken into account in the analyses.

2) The authors should make clear why some decisions were made regarding certain methods (i.e. adjustment using PCA instead of Houseman estimates) and thresholds (i.e. SoC-associated CpGs with difference <4%). More on this in point 14 and 15.

3) The Discussion section should be rewritten to better reflect the relevance of the findings and the limitations of the study. For example, the actual number of unique seasonal MEs is modest and the discussion should reflect this. Moreover, the findings should be compared with previously published studies on, e.g., folic acid supplementation and famine (this last point also applies to the Introduction). More on this in point 12 and 13.

Additional points from individual review reports:

Results section:

4) Page 3, line 94: Have the authors access to longitudinal intra-individual methylation scores during different seasonal windows?

5) Page 4, line 141: Did the authors re-evaluate SoC CpG positions with alternative methods (e.g. pyrosequencing) to analyse larger groups/ cluster of CpG positions and to control the reliability of array data?

6) Line 238 onward: from 257 Soc-CpGs to the "full" set of 768 SoC-CpGs for enrichment tests out of "power" reasons ◊ not consistent and confusing. I would stick with your choice for the 257.

7) Page 7, line 301: The authors mentioned overlaps with previous studies. It would be helpful, if overlapping or related findings could be summarized (and maybe visualized) in more detail. This would facilitate the comparison of the current data set with previous publications.

8) I would strongly recommend reporting the relationship between methylation of these SoC sites and measures of growth or development in these two cohorts – it's not clear to me why this has not been done so, assuming such data is available under approved ethics. In the field there is an ever-growing body of papers linking various early development exposures to differences in methylation in childhood, but there is a dearth of reproduceable evidence for exposures associating with methylation differences that in turn associate with tangible differences in child health/development. Particularly since the manuscript already mentions things like the relationship between methylation and BMI – while adult BMI is different to child measures of body composition, any evidence for a relationship (or a lack of a relationship) with available phenotypes in these two child cohorts would be a logical conclusion that section of analysis and would provide much greater clarity for the relevant Discussion section.

9) Relatedly, if consistent with approved ethics, this paper would benefit from a table summarising the cohort characteristics for each cohort. If appropriate, stratifying the cohorts summaries by season of conception would also be of interest.

10) Rationale for not doing a meta-analysis for power reasons should be explained.

11) The Results section switches from past to present tense and back again. Please keep it to past tense.

Discussion section

12) From my point of view, the observation of an attenuation of DNA methylation levels until mid-childhood is of interest. It would be helpful, if the authors could discuss this point in more detail within the Discussion section. What is known about methylation changes during aging (epigenetic drift etc.) and are these observations relevant for SoC associated CpGs?

13) The authors might discuss in more detail, why these observations of SoC associated loci are disease relevant.

Methods section

14) As mentioned in the public review, I think there needs to be more clarity about why you do and do not use the SoC-associated CpGs with difference <4% – in the results it is stated that the full list is being used to 'maximise power', but it is unclear why maximising power is necessary/better for that analysis compared to the other analyses where only CpGs with difference >4% are used? A little more detail on why it is important/fine to use there would be helpful.

15) Another point that would benefit from additional clarity would be adjusting for cell composition differences in your models – it appears that you have adjusted for these by including the top 6 PCs, but you also have cell count estimates from the Houseman method. Was there are a particular reason for using the PCs when the Houseman estimates were available?

16) Methods does not read as one coherent story, but fragmented and will require some shuffling to make it easier to read.

17) Outlier removal is with 25th and 75th percentile very aggressive compared to what is standard in the field.

18) You can Check SNPs in 450k dataset for possibility to adjust for genetic background in the discovery cohort and 850k cohort to exclude sample swaps/mixtures etc.

19) Reading the methods you are worried by genome-wide effects on DNAm. Why not look at the LINES ALU effects via: Zheng Y Joyce BT Liu L Zhang Z Kibbe WA Zhang W Hou L. Prediction of genome-wide DNA methylation in repetitive elements. Nucleic Acids Res 2017;45:8697-8711 [works for 450k data]

20) Were African allele frequencies used to filter out CpG probes?

21) Was imputation done with AGVP?

22) Was genetic information used to exclude family relationships, mixtures and sample duplications? [knowing the fluidity of family structures and logistics of sample collection in the Gambia]

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Environmentally sensitive hotspots in the methylome of the early human embryo" for further consideration by eLife. Your revised article has been evaluated by Jessica Tyler (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. Two of the three original reviewers were happy with the way you addressed their comments, but since the other reviewer was no longer available, I have asked an additional reviewer to specifically take a look at the applied adjustment for batch effects (which was one of the main points brought up by this original reviewer). As you can see below, the new reviewer was in general happy with the rebuttal, but brought up some additional points that need to be addressed.

Reviewer #4 (Recommendations for the authors):

Thank you for the opportunity to review the rebuttal to the article titled "Environmentally sensitive hotspots in the methylome of the early human embryo". I would like to say that reading through the rebuttal it appears the authors have been reactive and enthusiastic in their responses to the reviewers. Overall, it appears the changes introduced have help interpretation of the findings as far as I can tell.

In terms of the concerns reviewers have regarding batch effects, on the whole it appears that these have been these addressed as far as is possible within the confines of this particular experiment. The sensitivity analyses reported in table 1s suggest that controlling for the suspected technical confounders (e.g plate, slide, cell proportion estimates) does not significantly attenuate the association between SoC-CpG and doc. As noted, there does appear to be non-randomization with respect to Plate (and by extension, Slide) in the youngest ENID sample, which I suspect is due to assignment of samples to plates as they were collected (i.e in chronological order). What I cannot tell is whether the methylation arrays are also processed as samples are received (i.e. once a plate is filled), or all together at the end of the collection phase. If it is the former, that is a likely source of some variation between plates. Given the use of this cohort as the discovery sample, it would be useful if the authors could declare whether or not this is the case in the methods.

I am however suspicious that there is an alternative confounding factor that could have implications for the interpretation of the results within the paper, and that is the notion of DNA methylation data reliability (or lack of). Multiple studies (e.g. Logue et al. (2017); Epigenomics 9(11):1363-1371; Sugden et al. Patterns 1(2): 100014) have demonstrated that a large proportion of the CpG sites shared between the 450K and EPIC array (as used in this paper) are unreliable, so that it is unlikely they yield the same value when the same sample is measured twice. This of course has implications for determining 'significant associations', for assessing DNA methylation changes over time, and for replication. Because of what we know about reliability and how it manifests, the authors should address reliability in the context of these findings.

Reassuringly for this paper, the SoC-CpGs appear to be pretty robust – cross-referencing the subset of 259 CpGs against the list of reliabilities from Sugden et al., shows the mean ICC is over.7 (close to 'excellent') – this is not the case for the 509 CpGs not taken forward, who have a mean reliability of less than 0.3 ('poor'). The list of CpGs selected as matched and array background controls does not appear available, but I strongly suspect the array background CpGs (at the very least) will have a much lower reliability than the SoC-CpGs (just due to random chance). This clouds the interpretation of any tests that compare these sets of CpGs and should be taken into consideration.

Further, differential reliability should be considered as an alternative explanation for the reduction in mean SoC amplitudes over time – could it be that measurements made using 450K arrays (ENID 2yr) are different to those using EPIC arrays for reasons beyond age-specific effects (i.e. measurement error)?

Finally, the description of the properties of SoC-CpGs (lines 173 onwards) notes that they are more likely to be intermediately methylated – this is again a property of reliable CpGs since arrays do not have the resolution to measure hyper- and hypo- methylated sites very well, leading to unreliable measurements. In all, these points suggest that reliability of DNA methylation is important for interpretation of these results, and, given the high reliability of the SoC-CpGs, is actually a positive feature.

The reviewers were concerned that a large proportion of the discussion was dedicated to MEs and how these findings are related. I believe the authors frame this appropriately, and do not find the references to them excessive. MEs are of great interest, and using cheaper and easier methods to uncover them (such as here) will be beneficial.

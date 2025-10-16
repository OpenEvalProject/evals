# Peer review - Round 1

Editors:
- Christopher S Williams, https://ror.org/02vm5rt34 Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71953.sa0](https://doi.org/10.7554/eLife.71953.sa0)

This work develops a multistage/component mathematical model to analyze advanced colorectal adenomas and the impact that aspirin therapy has on adenoma formation rates. This study will be interesting to the cancer evolution community and in particular those interested in colorectal cancer incidence. While the model is mainly focused on aspirin chemoprevention, the model could be adapted to test other putative preventative agents, and thus could have a broad impact.


---

# Peer review - Round 1

Editors:
- Christopher S Williams, https://ror.org/02vm5rt34 Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71953.sa1](https://doi.org/10.7554/eLife.71953.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The protective effect of aspirin in colorectal carcinogenesis: a multiscale computational study from mutant evolution to age incidence" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: E Georg Luebeck (Reviewer #2); Andrew Chan (Reviewer #3).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

1)) Overall, the manuscript would benefit from a more precise explanation of the assumptions used in the models presented. This would include a more clear discussion/rationalization of advanced adenoma, adenoma classification, and how aspirins effect was implemented at the crypt level (see first reviewers comments)

2) There needs to be increased justification (or modification of the model) for why the assumption of zero crypt death/fusion.

3) Several reviewers mention limitations/concerns with the reliance on mutant KRAS (i.e. lack of determining KRAS status in adenomas/cancers, lack of APC/KRAS mutational status in predicting aspirin response and that the effect estimates are based on preclinical work using relatively high doses of aspirin. Please address these concerns in the manuscript and in response.

4) Addressing the concern from reviewer #3 regarding the assumption that the cell of origin for CRC is an ISC as opposed to more recent theories suggesting alternative origins and suggestions on expanding the discussion to include more recent literature on age-differences in aspirins effects on CRC.

Reviewer #1 (Recommendations for the authors):

In addition to the points raised in the public review, I have the following comments:

It is unclear to me why the effect of reducing the fitness of type 6 is done through reducing the rates of mutation to type 6 (R36 and R56). What is the justification for that?

For the scenario when aspirin reduces gamma3 and gamma4, why does it also not reduce gamma5?

It would also be important to discuss more precisely (i.e. by referring to specific mathematical models) how the findings that aspirin changes division and death rates in cell culture, where there is no tissue hierarchy, translates to the in vivo setting, where the effects of aspirin may be felt by crypts, stem cells or progenitor cells.

Reviewer #3 (Recommendations for the authors):

I read the manuscript with great interest and was pleased to see that the authors took care to acknowledge the limitations and clearly explain the base assumptions used in their approach. The manuscript is well-written and there are only minimal additions that may improve the manuscript.

– Unless I have misunderstood, the basic model allows us to understand the probability of developing APC and/or KRAS mutant adenomas (and using this as a relative measure of the 'advanced' nature of the in silico 'neoplasm'). I appreciated the discussion relative to the formation of aberrant crypts vs. adenomas vs. more advanced precancers. However, it seems that everything operates on the basic premise that an intestinal stem cell must be the tumor cell of origin and that aspirin is having specific effects on these cells. This assumption may be too much an oversimplification to allow the model to have broad reaching applicability. For example, recent work has begun to describe that the tumor cell of origin may not be the classical intestinal stem cell in all CRC cases, especially with advancing age or under different dietary stressors, and separately in parallel, that aspirin may have effects on cell differentiation/states (e.g. Devall et al. Cancer Prev Res 2021), mechanism may be cell-context specific, or be significantly impacted by epithelial cell extrinsic factors not included in the model (e.g. gut microbiome, see A. Prizment et al. Aliment Pharmacol Ther 2020; C. Brennan et al. mBio 2020; R Zhao et al. Gastro 2020) While the authors do describe that these assumptions may be limiting, I think prudent for the authors to discuss the specific impacts of the assumption that aspirin has a direct effect on intestinal stem cells being tumor cell of origin has on model interpretation. How would estimates be potentially influenced if intestinal stem cells were not the target cell or aspirin only had effects in specific cell types or by cell extrinsic factors? What do these assumptions have on the broader generalizability of this model? Can the authors expand on how this may be expected to be accounted for in the future? What additional information or type of data is needed from clinical and preclinical experiments to allow for more accurate biological modeling of these complex interplays? The last question is particularly important to understand the broader impact of these findings and if the models have to potential to more directly inform future research.

– Similarly, I think more discussion could be owed to the emerging literature around the intersection of age-differences and aspirin mechanism, especially in light of the recent results from the ASPREE trial that described an increase in cancer death as a result of aspirin intervention among adults over age 70. Is it possible to model the timing of aspirin intervention using this model, particularly in view of the probability differences arising from differential mutational priming outcomes (APC-/- vs. APC -/+ vs. KRAS+, etc.). The ASPREE results demonstrated that the increase in cancer mortality was not driven by a change in cancer incidence and I wonder if the authors can try to model these effects or at least discuss how the model findings should be interpreted in view of these recent results from trials.

– The manuscript primarily discusses the CAPP2 trial as the evidence supporting aspirin chemoprevention of colorectal cancers. Although this obviously has clear implications for placing the results in the context of prevention of CRCs in Lynch syndrome, these tumors are neither sporadic, nor arise via the pathways included in the model. The authors could broaden the background to include the preponderance of evidence for the preventive effects in sporadic cases (or even FAP patients which are known to have APC mutant cancers) where aspirin has had less of a potent chemopreventive effect than in Lynch syndrome. However, these data are relevant to the most extreme phenotype in their model.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Aspirin's effect on kinetic parameters of cells contributes to its role in reducing the incidence of advanced colorectal adenomas, shown by a multiscale computational study" for further consideration by eLife. Your revised article has been evaluated by the reviewers and by the Editors.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors have carefully addressed previous concerns, and I am satisfied with the revision.

Reviewer #2 (Recommendations for the authors):

The revised manuscript has gained considerably in strength and, by in large, clarifies the main points raised by the reviewers. I appreciate the extra work that went into refining/extending the model analysis, in particular the addition of a growth phase for the type 6 (advanced) adenoma.

Two lingering points. I hope they can be addressed.

1. Please clarify whether the size distribution provided for type 3 (APC-/-) adenoma in Figure Appendix 1 Figure 12 and 13 refer to the particular type 3 adenoma (clone) in which the advanced adenoma first developed or to the entire population of type 3 adenomas in the colon. I think the authors should point out that their ODE model does NOT distinguish individual clones of abnormal crypts (ie individual adenomas). This is a limitation since detectable adenoma number of any kind (other than hyperplastics) is an important clinical factor.

2. I understand the authors' point about postulating other potential gain-of-function mutations, similar to KRAS, such as BRAF. However, BRAF is a poor example as it is associated strongly with mismatch repair deficiency and SSAs, leading frequently to hypermutated cancers. While there may be other yet unidentified gain-of-function drivers for the advanced adenoma, there may also simply none required given the epigenetic plasticity and adaptive epigenetic changes as adenomas sojourn for years. In any case, the mention of BRAF is somewhat misleading in the context defined by the authors.

Reviewer #3 (Recommendations for the authors):

Thank you for a very complete response. The manuscript is excellent!

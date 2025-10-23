# Peer review - Round 1

Editors:
- Yousef Abu-Amer, https://ror.org/036c27j91 Washington University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83658.sa0](https://doi.org/10.7554/eLife.83658.sa0)

This well-presented and sophisticated study provides significant proof-of-concept for the application of the ForensOMICS approach as a new pathway for forensic taphonomy with great promise to advance future research. The solid foundation of the research combining metabolomics, proteomics, and lipidomics is considered very exciting, strong, and expands the boundaries of forensics research.


---

# Peer review - Round 1

Editors:
- Yousef Abu-Amer, https://ror.org/036c27j91 Washington University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83658.sa1](https://doi.org/10.7554/eLife.83658.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The "ForensOMICS" approach to forensic post-mortem interval estimation: combining metabolomics, lipidomics and proteomics for the analysis of human bone." for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mone Zaidi as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Sharni Collins (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please address the following concerns/points:

1. Please consider the inclusion of placement periods/seasons of each of the donors.

Do you collect any environmental/covariate data, like daily temperature, relative humidity, rainfall, etc of the taphonomic field site? Going forward, with future studies, this information could be extremely useful to inform any future conclusions. In addition, it could open the door to linear mixed models where you could investigate the impact of random or fixed effects, alongside the outcomes of the omics results. You could also potentially use this approach to investigate inter-individual variability, as mentioned in your work. This may be more of a long-term goal, but it is definitely something worth looking into.

2. pg. 5, line 127: "so the metabolomic appears…" suggestion → "so the metabolomic approach appears…".

3. pg. 6, line 173: "PMI estimation methods is has not…" suggestion → "PMI estimation methods has not…".

4. From a methodological point of view, as a first step of data analysis, each single data set (metabolomics, lipidomics, and proteomics) should be investigated singularly, independently of the other two data sets, to discover the information of each single data set related to PMI and better understand the advantage to integrate the three data sets. The analysis should be performed by multivariate and univariate data analysis. Moreover, the common and unique information of the three data sets should be investigated in order to better understand what happens when the data are integrated.

5. PMI is a continuous factor, not a categorical factor. I suppose that clustering analysis has been performed in the latent space obtained by modelling the data considering all three data sets and that the discovered groups of similar observations have been characterized by PLS-DA. How many clusters have been obtained? What classes have been used in PLS-DA? If this was the approach, the order between PMI values have not been considered in data analysis. PMI was modeled as a categorical factor instead of a continuous factor or, eventually, an ordinal factor. Moreover, it seems that only two main groups of observations have been discovered and that these two groups correspond to pre- and post-burial. This may be the effect of a different time scale between the three -omics. For example, if metabolomics and lipidomics explain low PMI but not high PMI and proteomics explain only high PMI, only two clusters can be observed by data integration. The analysis suggested at point 1 may clarify the situation. Please, comment on these points and add a brief description of DIABLO in Supplementary Information.

6. Cross-validation must be performed considering explicitly the biological replicates. All replicates of the same subject at the same time must be excluded during each run of cross-validation, i.e. they must belong to the same group. Please repeat cross-validation if this was not the case.

7. The model should be tested by randomization test to discover over-fitting. Please, discuss this point or implement a suitable permutation test.

8. There are garbled codes in the R script file provided by the authors, which seem to be line breaks. Please check the encoding of the script.

9. It is suggested to use a flow chart to describe the general process of the "ForensOMICS" pipeline, instead of only visually displaying the results of different omics analyses, so that readers can intuitively and clearly understand the main content of the study.

10. Significance analysis could be performed in figure 3 to test the significant variations of the selected variables between different PMI.

11. There are still some mistakes in the writing, further revisions and corrections are needed.

12. Consistent with the well-received transparency of the authors' approach pertaining to different aspects of this study, It would also be beneficial to the readership to comment on weaknesses raised by reviewer #3.

Reviewer #1 (Recommendations for the authors):

Overall, a very sophisticated paper that has been both written and presented well. It is exciting to see what the future holds as the field moves towards more robust scientific applications, such as those presented in this work. It is great to see the transparency in the work as well, understanding that much work is still yet to be done before this approach is operational. However, this does not detract from the significance of the work at all. What I think would be beneficial to include in the current paper, if you choose to accept, is the inclusion of placement periods/seasons of each of the donors. This is common practice for some laboratories, and can sometimes be really useful in informing my next point.

Do you collect any environmental/covariate data, like daily temperature, relative humidity, rainfall, etc of the taphonomic field site? Going forward, with future studies, this information could be extremely useful to inform any future conclusions. In addition, it could open the door to linear mixed models where you could investigate the impact of random or fixed effects, alongside the outcomes of the omics results. You could also potentially use this approach to investigate interindividual variability, as mentioned in your work. This may be more of a long-term goal, but it is definitely something worth looking into.

Reviewer #2 (Recommendations for the authors):

The authors should address the following main points.

1. From a methodological point of view, as a first step of data analysis, each single data set (metabolomics, lipidomics, and proteomics) should be investigated singularly, independently of the other two data sets, to discover the information of each single data set related to PMI and better understand the advantage to integrate the three data sets. The analysis should be performed by multivariate and univariate data analysis. Moreover, the common and unique information of the three data sets should be investigated in order to better understand what happens when the data are integrated.

2. PMI is a continuous factor, not a categorical factor. I suppose that clustering analysis has been performed in the latent space obtained by modelling the data considering all three data sets and that the discovered groups of similar observations have been characterised by PLS-DA. How many clusters have been obtained? What classes have been used in PLS-DA? If this was the approach, the order between PMI values have not been considered in data analysis. PMI was modelled as a categorical factor instead of a continuous factor or, eventually, an ordinal factor. Moreover, it seems that only two main groups of observations have been discovered and that these two groups correspond to pre- and post-burial. This may be the effect of a different time scale between the three -omics. For example, if metabolomics and lipidomics explain low PMI but not high PMI and proteomics explain only high PMI, only two clusters can be observed by data integration. The analysis suggested at point 1 may clarify the situation. Please, comment on these points and add a brief description of DIABLO in Supplementary Information.

3. Cross-validation must be performed considering explicitly the biological replicates. All replicates of the same subject at the same time must be excluded during each run of cross-validation, i.e. they must belong to the same group. Please repeat cross-validation if this was not the case.

4. The model should be tested by randomization test to discover over-fitting. Please, discuss this point or implement a suitable permutation test.

Reviewer #3 (Recommendations for the authors):

1. There are garbled codes in the R script file provided by the authors, which seem to be line breaks. Please check the encoding of the script.

2. It is suggested to use a flow chart to describe the general process of the "ForensOMICS" pipeline, instead of only visually displaying the results of different omics analyses, so that readers can intuitively and clearly understand the main content of the study.

3. Significance analysis could be performed in figure 3 to test the significant variations of the selected variables between different PMI.

4. There are still some mistakes in the writing, further revisions and corrections are needed.

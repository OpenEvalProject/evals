# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77945.sa0](https://doi.org/10.7554/eLife.77945.sa0)

This study presents a useful automated package called 'HippUnfold' in form of a BIDS App. The approach is solid and validated by comparing it against other methods in the field and has the potential to be used by a wide audience.


---

# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77945.sa1](https://doi.org/10.7554/eLife.77945.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "HippUnfold: Automated hippocampal unfolding, morphometry, and subfield segmentation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Pierre-Louis Bazin (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Overall, this manuscript is well written, interesting, timely and will help resolve the debate in the field. We have the following suggestions to improve the manuscript:

1. As far as I understood, the U-Net approach defines individual landmarks needed for the unfolding and the unfolding provides a unique mapping between folded and unfolded space. However, if I understood correctly, in the next step the same subfield labels are enforced on every unfolded surface in the same way. My biggest concern is how we can be sure that these labels are valid for everyone.

2. Adding to this point, I find it very difficult to see any hippocampal structure in the 3T T1 data, for example HCP-YA case in figure 6 (but also HCP-A case in Figure 5 A, even true for the T2 image in the HCP-A case). This might be due to the image in the PDF and look better in the actual scan. However, as a human rater I would have no idea how to segment these cases and am wondering how the author's make sure that their approach produces a valid result and does not rely on the respective priors too much.

3. While the authors have addressed this in part by comparing the automated segmentation labels with the manual labels in young adults, there is no such data for populations that deviate more from young and healthy adults. Thus, there remains the question how their approach would deal with data from such populations.

4. I understand that manual segmentations are very tedious and labor intensive and might not be feasible in this project. However, maybe the authors could apply their pipeline to a dataset of a patient case with well-known abnormality and investigate the result? Alternatively, although the literature is less clear here, the authors could report on the differences that they see between HCP-A and HCP-YA on a group level and relate this to other findings in ageing or maybe even already existing work on these specific cohorts (in case these exist).

5. First, I would like to congratulate the authors in building an elegant toolbox for hippocampal analysis, with many valuable features for the basic and advanced users alike. I expect the points I raised can be addressed by reframing the presentation of the software, focusing more on what it provides in terms of a representation and less on whether or not it provides a better subfields definition.

6. My first point above should be addressable by including all algorithmic details either in the main text or in an appendix, so the article is self-contained with regard to the methodology. Details of the UNet preprocessing and architecture, Laplacian coordinate mapping algorithm, and morphometric feature extraction should be included. The 'Hippunfold detailed pipeline' section remains vague: concrete descriptions including mathematical formulas and algorithm parameters would be better. A figure showing the outputs of the different steps would also be helpful.

7. The second point requires carefully re-evaluating the claims made about topology, and separating the unfolding and labeling question. In the end, the provided algorithm does not perform any subfield labeling of individual hippocampi, but only transfers a fixed label map from BigBrain onto individual anatomies, using the unfolding coordinates as a proxy. Thus the results of Figure 4 are misleading, since they compare the quality of the unfolding and not the labeling. This point should be made clear, and the comparisons of Figure 3 need to be altered, maybe discussing rather the limited variability of the unfolded labels from ASHS and FreeSurfer as an indication of the quality of the unfolded representation. If the authors want to compare the quality of subfield labelings across methods, those comparisons should be done in voxel space. Note also that the claim that ASHS and FreeSurfer do not preserve topology is unnecessary and debatable (e.g. internally the FreeSurfer algorithm uses a fixed-topology mesh, so it does preserve its own definition of topology).

8. Here I would rather have a comparison with other representations, e.g. using the volumetric space directly, mapping to the outer surface, or defining a medial axis representation. Why is mapping hippocampal information onto a 2D plane better? Does this preserve more the common features across hippocampi than other options? While this idea is hinted at when discussing variability in folding, it could be empirically tested.

9. This also links to the third question of implicit alignment which could be tested for instance by inspecting the variation in subfield boundaries from volumetric methods in the experiment of Figure 3. Note also that features mapped onto the unfolded representation of Figure 2 could be co-registered into a 2D atlas, and the corresponding deformations could be evaluated.

10. Another question related to representation is the decision to use a rectangular map rather than a more irregular one similar to those used in cortical and cerebellar flat maps: by doing so, some of the regions get a distorted importance (as shown in the mesh maps presented in the documentation). It would be good to provide a measure of the distortion to be expected.

11. Finally, while the software and documentation are very well organized, I was unable to run the app on the test data folders or my own data, using docker, singularity or the poetry installation option, which is absolutely required to complete this review. The 'getting started' section should also include a full processing script example on a test data set, outlining the main steps and basic parameters, especially as the toolbox is quite flexible and thus quite complex. Commands used for visualizing the various results should also be given in the 'Outputs' section, so users can visualize their data as in the examples. Given the richness of the manual delineation and segmentation effort, it would be valuable to release the training and testing data openly (note also that it is quite important for the U-Net step, where the training set properties have a strong impact on performance and potential biases).

12. In general, the paper is well written, but there are multiple areas that I have some issues with following the logical flow of what is being proposed. For example, the paper begins with demonstrating multiple metrics that are projected onto the hippocampal flatmap that includes thickness, myelin, curvature, gyrification, etc. It is unclear as to what information the authors want to convey here. This is the first mention of many of these multiple metrics as well and therefore their relevance is ultimately not extremely clear. As a result, it is hard to support their claim that "differences in morphological and quantitative features can be seen across the hippocampus, particularly across the subfields" as the goals of this particular figure are not at all clear.

13. Line 147: It is not totally accurate to state that ASHS makes use of multi-atlas registration as it also uses AdaBoost to correct for segmentation inaccuracies.

14. For the FreeSufer and ASHS comparisons – is it possible to provide some quantification of errors or anything like that? I think it would be helpful to quantify the differences in a more accurate manner. If this is in a previous publication and I missed it, it could be useful to reiterate here. The qualitative difference is nice – but there is room to compare them more quantitatively to one another.

15. For the validation of the U-NET, details on the manual segmentation protocol, who did it, and its reliability are crucial. Training/testing paradigms would be helpful here. So would Bland-Altmann plots. I think in general the validation of these segmentations is quite poor – so more metrics that demonstrate the segmentation beyond dice overlaps would be helpful.

16. It is unclear how generalizable the method is outside of HCP acquisitions.

Reviewer #1 (Recommendations for the authors):

As far as I understood, the U-Net approach defines individual landmarks needed for the unfolding and the unfolding provides a unique mapping between folded and unfolded space. However, if I understood correctly, in the next step the same subfield labels are enforced on every unfolded surface in the same way. My biggest concern is how we can be sure that these labels are valid for everyone.

Adding to this point, I find it very difficult to see any hippocampal structure in the 3T T1 data, for example HCP-YA case in figure 6 (but also HCP-A case in Figure 5 A, even true for the T2 image in the HCP-A case). This might be due to the image in the PDF and look better in the actual scan. However, as a human rater I would have no idea how to segment these cases and am wondering how the author's make sure that their approach produces a valid result and does not rely on the respective priors too much.

While the authors have addressed this in part by comparing the automated segmentation labels with the manual labels in young adults, there is no such data for populations that deviate more from young and healthy adults. Thus, there remains the question how their approach would deal with data from such populations.

I understand that manual segmentations are very tedious and labor intensive and might not be feasible in this project. However, maybe the authors could apply their pipeline to a dataset of a patient case with well-known abnormality and investigate the result? Alternatively, although the literature is less clear here, the authors could report on the differences that they see between HCP-A and HCP-YA on a group level and relate this to other findings in ageing or maybe even already existing work on these specific cohorts (in case these exist).

Reviewer #2 (Recommendations for the authors):

First, I would like to congratulate the authors in building an elegant toolbox for hippocampal analysis, with many valuable features for the basic and advanced users alike. I expect the points I raised can be addressed by reframing the presentation of the software, focusing more on what it provides in terms of a representation and less on whether or not it provides a better subfields definition.

My first point above should be addressable by including all algorithmic details either in the main text or in appendix, so the article is self-contained with regard to the methodology. Details of the UNet preprocessing and architecture, Laplacian coordinate mapping algorithm, and morphometric feature extraction should be included. The 'Hippunfold detailled pipeline' section remains vague: concrete descriptions including mathematical formulas and algorithm parameters would be better. A figure showing the outputs of the different steps would also be helpful.

The second point requires carefully re-evaluating the claims made about topology, and separating the unfolding and labeling question. In the end, the provided algorithm does not perform any subfield labeling of individual hippocampi, but only transfers a fixed label map from BigBrain onto individual anatomies, using the unfolding coordinates as a proxy. Thus the results of Figure 4 are misleading, since they compare the quality of the unfolding and not the labeling. This point should be made clear, and the comparisons of Figure 3 need to be altered, maybe discussing rather the limited variability of the unfolded labels from ASHS and FreeSurfer as an indication of the quality of the unfolded representation. If the authors want to compare the quality of subfield labelings across methods, those comparisons should be done in voxel space. Note also that the claim that ASHS and FreeSurfer do not preserve topology is unnecessary and debatable (e.g. internally the FreeSurfer algorithm uses a fixed-topology mesh, so it does preserve its own definition of topology).

Here I would rather have a comparison with other representations, e.g. using the volumetric space directly, mapping to the outer surface, or defining a medial axis representation. Why is mapping hippocampal information onto a 2D plane better? Does this preserve more the common features across hippocampi than other options? While this idea is hinted at when discussing variability in folding, it could be empirically tested.

This also links to the third question of implicit alignment which could be tested for instance by inspecting the variation in subfield boundaries from volumetric methods in the experiment of Figure 3. Note also that features mapped onto the unfolded representation of Figure 2 could be co-registered into a 2D atlas, and the corresponding deformations could be evaluated.

Another question related to representation is the decision to use a rectangular map rather than a more irregular one similar to those used in cortical and cerebellar flat maps: by doing so, some of the regions get a distorted importance (as shown in the mesh maps presented in the documentation). It would be good to provide a measure of the distortion to be expected.

Finally, while the software and documentation are very well organized, I was unable to run the app on the test data folders or my own data, using docker, singularity or the poetry installation option, which is absolutely required to complete this review. The 'getting started' section should also include a full processing script example on a test data set, outlining the main steps and basic parameters, especially as the toolbox is quite flexible and thus quite complex. Commands used for visualizing the various results should also be given in the 'Outputs' section, so users can visualize their data as in the examples. Given the richness of the manual delineation and segmentation effort, it would be valuable to release the training and testing data openly (note also that it is quite important for the U-Net step, where the training set properties have a strong impact on performance and potential biases).

Reviewer #3 (Recommendations for the authors):

– Clear definition of goals and the novelty of the work.

– Better comparison against other methods.

– Better comparison against manual segmentation (needs more than just the Dice).

– Lack of demonstration of generalizability. Need to see how this may work in the context of other data acquisition streams.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Automated hippocampal unfolding for morphometry and subfield segmentation using HippUnfold" for further consideration by eLife. Your revised article has been evaluated by Floris de Lange (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The description of some of the central methods used in the article (Laplacian embedding, shape injection) is too limited to understand fully how we obtain the unfolding. I see the point of 'increased complexity with increasing depth', but the article does not reach the level where the algorithms are explicitly described. It is also unclear if the authors used third-party software or their own implementation of these two methods.

2. A second remaining issue I have is the somewhat puzzling fact that the T1w trained version of hippunfold performed better than the T2w one for the HCP-aging dataset: it would be good to understand why that is the case.

3. Finally, I still could not run the algorithm successfully on the provided example. Both Docker and Singularity provide very little information about why they fail. Installing and running the development version almost works, but only after installing several additional packages and non-standard research software from other groups (connectome workbench, NiftyReg, c3d...). None of these dependencies are described in the documentation. I would recommend the authors test their installation procedure on a bare-bones OS, for instance in a Linux virtual machine, as it is often challenging to remember what elements of a customized installation are being used or not. I am confident that the remaining issues are small, and that the usability of the software will be increased in the exercise.

Reviewer #2 (Recommendations for the authors):

I thank the authors for a thorough revision with additional validation experiments, which generally addresses my concerns and issues. I particularly appreciate the addition of the FreeSurfer and ASHS/Magdeburg labelings as options: it clarifies the separation between unfolding and labeling, and also provides continuity for users who have worked with these labels in previous studies. I also commend the authors for releasing their training data, increasing transparency, and for providing actual test data sets.

However, I would still argue that the description of some of the central methods used in the article (Laplacian embedding, shape injection) is too limited to understand fully how we obtain the unfolding. I see the point of 'increased complexity with increasing depth', but the article does not reach the level where the algorithms are explicitly described. It is also unclear if the authors used third-party software or their own implementation of these two methods.

A second remaining issue I have is the somewhat puzzling fact that the T1w trained version of hippunfold performed better than the T2w one for the HCP-aging dataset: it would be good to understand why that is the case.

Finally, while these two issues above are minor, I still could not run the algorithm successfully on the provided example. Both Docker and Singularity provide very little information about why they fail. Installing and running the development version almost works, but only after installing several additional packages and non-standard research software from other groups (connectome workbench, NiftyReg, c3d...). None of these dependencies are described in the documentation. I would recommend the authors to test their installation procedure on a bare-bones OS, for instance in a Linux virtual machine, as it is often challenging to remember what elements of a customized installation are being used or not. I am confident that the remaining issues are small, and that the usability of the software will be increased in the exercise.

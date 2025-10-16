# Peer review - Round 1

Editors:
- Jie Xiao, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65151.sa1](https://doi.org/10.7554/eLife.65151.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Your work of developing the MiSiC package to segment single cells in crowded bacterial colonies and identify different species in the colonies is of great importance to the community. The final version of the manuscript incorporated all reviewers' comments with improved readability. An updated user guide is provided. We are also pleased with your commitment to disseminate this important tool to other research labs in the community.

Decision letter after peer review:

Thank you for submitting your article "MiSiC, a general deep learning-based method for the high-throughput cell segmentation of complex bacterial communities" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gisela Storz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Zach Hensel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted the following to help you prepare a revised submission.

Essential revisions:

All three reviewers recognize the significance and potential impact of the work and would like to see this work being implemented and disseminated to a wider bacterial cell biology field. However, the following essential revisions are required before the work could be considered for publication at eLife. These essential revisions were discussed and agreed upon among the reviewers and the reviewing editor during the consultation. In addition to these essential revisions, detailed comments from the three reviewers should also be addressed in the revision.

1. Please benchmark the performance of MiSiC against currently available segmentation methods using similar approaches such as Supersegger, DeepCell and DeLTA.

2. Please provide a detailed description of the working principle of MiSiC, and a ready-to-use workflow (or a handbook/guide) for users. These descriptions should include not only the essential steps, but also detailed parameters lists/ranges/considerations, such as cell density, size, pixel size, signal-to-noise ratio, and cell shape range etc. The goal of this essential revision is to ensure that the MiSiC tool can be easily disseminated and implemented by other non-technical-driven users in order to maximize the impact of the work.

Reviewer #1 (Recommendations for the authors):

1. It is surprising to see that the authors have not applied the same algorithm to oval or round-shaped cells. Based on the principle of SIM, I do not see why MiSiC cannot be applied to those cells. Could the authors comment further on the limitations or show some results of round cells?

Reviewer #2 (Recommendations for the authors):

The results applying U-Net to the SIM images are very interesting and I look forward to seeing if it will improve performance of the segmentation method (based on DeLTA) that we are using in our lab now; alone or input together with the unprocessed image.

Reviewer #3 (Recommendations for the authors):

– The authors should emphasize that MiSiC is a 2D image analysis tool. It cannot handle 3D image data and it cannot handle 3D+time image data natively at the moment. This needs to be clearly stated.

– The introduction is rather short and does not provide sufficient context for most readers in my opinion. Particularly the 2nd paragraph is so short that the arguments are not clear. The second sentence criticizes machine learning techniques for requiring large amounts of training data. But the method presented in this paper is also a machine learning technique that requires a large amount of training data. I recommend that the authors significantly expand this paragraph to clarify and motivate their methodology.

– More generally, the introduction would benefit by placing the paper into the context of other image analysis tools for bacterial segmentation and colonies. There has been a lot of activity in image analysis for microbiology recently, and I think it would be helpful to readers to learn about this context.

– Results, paragraph 1 +2: Can the authors explain why the images need to be scaled so that the average cell size is set to 10 pixels? I guess this is based on the implicit assumption that there are sufficient intensity gradients on the 2x2 pixel scale used by the Hessian. As the SIM approach is a critical component of the MiSiC method, a clear explanation is needed here.

– A major advantage of MiSiC is that it uses the SIM images as training data for the CNN, which seems to result in a trained CNN model that can produce accurate segmentations for phase contrast, brightfield and fluorescence images. Is this true? Can the authors please very clearly state if this is true? The statements regarding this point in the manuscript are not completely unambiguous in my opinion. If true, this would be a major advance for bacterial image segmentation. Therefore, the authors should also state if the trained CNN model results in equal performance on all 3 imaging modalities. Or does a different CNN model need to be trained for each of the 3 imaging modalities with the same MiSiC workflow?

– Figure 2: In order for MiSiC to perform better on non-rod-shaped bacteria (filamentous bacteria, spirochetes, or cocci) – would the user need to generate new training data and re-train the model? I think this needs to be clarified.

– The authors supplemented their manually annotated data with synthetic data created by images of model rods with synthetic noise. Can the authors explain why this was done? Is the training with the manual annotation not sufficient? If the authors only used this synthetic data, does MiSiC also produce accurate segmentations, or is the real data needed?

– The semantic segmentation obtained by MiSiC (Figure 4) is impressive and works well. It is unclear whether this semantic segmentation also works in cases of strong intermixing between the cell types. Can the authors comment on that?

– Any development of a single cell segmentation method should include a graph of the Jaccard coefficient (and/or Dice index) as a function of the intersection over union, with error bars. The authors need to add such a graph to the manuscript so that authors can judge the quality of the segmentation.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "MiSiC, a general deep learning-based method for the high-throughput cell segmentation of complex bacterial communities" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jie Xiao as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Gisela Storz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Zach Hensel (Reviewer #2).

The reviewers have discussed their reviews with one another, and wished the authors to provide the following before the work can be accepted for publication:

1. Update User Guide to address issues and miscellaneous bugs related to file installations, encoding, handling of multiple images and etc as specified in reviewers 1 and 2's comments.

2. Expand the introductory or Discussion section to include a more detailed comparison with existing algorithms with a focus on the strength and weakness of each method, as specified in Reviewers 1 and 3's comments.

Reviewer #1 (Recommendations for the authors):

The revised manuscript by Panigrahi et al. addresses our major concerns. We are especially pleased to see the handbook created for the github page. Not only will the handbook be a valuable resource to users, but also the handbook can be updated as improvements and additions are made to the MiSiC GUI. Also, the new supplemental figure S1 is a helpful illustration of the two user-set parameters. We understand the difficulty in comparing MiSiC to different methods and appreciate the quantification of MiSiC's performance. Outlining the appropriate uses and limitations of MiSiC in the discussion is also appreciated. We hope the authors could further address the following concerns. The goal is to maximize the usability of MiSic for the community.

1. Cell density should be explicitly addressed in 1a of the handbook to match the heading. The new example of Caulobacter in Figure 3a is less dense than the images from the previous manuscript version, indicating that MiSiC can segment less dense cell populations. Since the majority of the images are still very dense clusters, it is still worth addressing density in the handbook if not in the manuscript text.

2. Suggesting specific preprocessing methods is useful, but the names alone might not be enough detail for the target MiSiC user. Either referencing FIJI plugins that accomplish the recommended processing or adding citations to the methods section would clarify these suggestions.

3. MiSiC is not expected to be absolutely accurate, and sometimes the binary mask output will require manual edits. For example, two cells recognized as one might need to be manually separated by pixels. If the GUI could incorporate the ability to manually modify the mask, that would tremendously increase the functionality of MiSiC. However, if that is too labor intensive, the post-processing section of the handbook should address how to make these manual adjustments to the output. This could also be mentioned in the discussion.

4. Could the authors expand the comparison between MiSiC with DeltaT, DeeptCell and Supersegger in the third paragraph of introduction be incorporating some of the language in the rebuttal letter? The goal is to give a bird's eye view of the current field so readers will have a clear assessment of which is good for what and understand MiSiC's uniqueness better.

5. There are some errors in GUI. They are not related to the segmentation algorithm, but confusing for users sometimes. For instance, the cell width measuring function is not always returning the right measurement. The way to break this function is to draw an extremely long line before actually tracing the short axis of any cell. Furthermore, MiSiC should be able to analyze all images belong to the same directory with just "one click", in theory. However, this was not the case today when we fed the GUI with multiple images. New masks could not be generated unless previous/existing images and masks are all cleared from the workspace. We also realized that applying the same parameter settings based on only one image does not guarantee accurate segmentation for other images, even though these images belong to the same experiment/run. It would be great if the authors could fix these bugs to enhance user experience.

Reviewer #2 (Recommendations for the authors):

I think that the authors have sufficiently addressed issues raised in the reviews. The examples of preprocessing/parameter choices in the handbook will be very useful.

In my opinion, the availability workflows to generate synthetic data and train the models would strengthen the manuscript since some potential users will want to sacrifice general for specific performance. However, anyone with the expertise to do that also has the expertise to reinvent the wheel to some degree based on what is reported in the manuscript.

The only other issue I have now is installation instructions (MiSiCgui page) no longer work for me (Windows 10; following instructions for conda). I created a python environment as specified, installed the misic package, and tried to install the GUI. (1) I think that the "use package" instructions should be updated, because add_noise for example is now in extras.py; (2) The GUI pip install command raised an error regarding file encoding. I don't know whether the 2nd error is specific to my system and did not spend much time trying to diagnose it. Lastly, the screenshots on the github page are the old version (noise=0.0001 rather than 1).

Reviewer #3 (Recommendations for the authors):

Author's response to the general comment 1 (page 1+2 of the rebuttal letter): I now understand better how it can be difficult to benchmark MiSiC against the other segmentation software. I also appreciate that the authors now discuss these other tools in lines 73-84 of the manuscript. However, the essential points that make the other tools unsuitable for the analysis that was desired by the authors are not mentioned in the main text (only in the rebuttal letter). For me, as a potential user of all of these tools, and probably for anyone who reads such a paper, it is important to know the strengths and weaknesses of these tools and why the other tools are not suitable for the authors' application. Therefore, I recommend that the authors should expand further the relevant paragraph in the main text, to more clearly describe why the other tools are not suitable. This doesn't have to be overly critical of the other tools, but it would be helpful to the readers.

All other comments were addressed nicely by the authors in my opinion.

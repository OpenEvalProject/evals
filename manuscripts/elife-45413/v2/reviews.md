# Peer review - Round 1

Editors:
- Valerie Horsley, Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.45413.sa1](https://doi.org/10.7554/eLife.45413.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript provides a novel tool to quantify different parameters of mammalian intercellular junctions, and as such, is aptly called junction mapper. As pointed out by the authors in the Introduction of the manuscript quantification of different mammalian junctional parameters is often rather time consuming as for many programs finding borders and, often, correcting borders, can until now mostly be done manually. This tool will be useful to researchers in many fields for quantifying cell junctions.

Decision letter after peer review:

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision, this was subsequently approved by the editors. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled "Junction Mapper: quantitative analysis to decipher cell-cell contact phenotypes" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor.

Given the list of essential revisions, including new experiments, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

While the reviewers recognized the benefits of the tool to analyze junctions, the reviewers felt that the manuscript lacked details regarding the algorithm testing and methods. Furthermore, the reviewers also would like to see whether this tool can be used on mammalian junctions to rigorously test whether this will be broadly used by the field of epithelial junction biologists.

Reviewer #1:

This very nice manuscript provides a novel tool to quantify different parameters of mammalian intercellular junctions, and as such, is aptly called junction mapper. As pointed out by the authors in the Introduction of the manuscript quantification of different mammalian junctional parameters is often rather time consuming as for many programs finding borders and, often, correcting borders, can until now mostly be done manually. Automated analysis is not trivial and in general requires a strong background in image bioinformatics/analysis or access to a core facility that provides such analysis. The exciting point of the work presented here is that this program provides a general and very accessible platform to quantify junctions in a semi-automatic manner to obtain multiple parameters. Moreover, proper detection of fragmented junctions is an even more complex problem which the authors have apparently solved. The program provides reasonable output parameters and the detection quality and sophistication of junctional staining appears to be outstanding judged by the data presented on both epithelial junctions as well as the already much harder endothelial junctions. Finally, the experiments that were performed convincingly demonstrate the applicability of the program and its sensitivity of detecting minor and specific alterations. Taken together, this manuscript provides convincing and exciting evidence that junction mapper is a great open software to quantitatively analyze junctions, and that allows laboratories not specialized in junctional imaging to also more precisely analyze and assess junctional phenotypes.

I have two comments that need to be addressed:

1) The last author is a well-known specialist on keratinocytes, which in vivo and in culture form multi-layered epithelia upon prolonged induction of differentiation. Although the authors have used keratinocytes, it seems they only used early time points after differentiation when these cells did not form multilayers yet. The multi-layering provides an extra complexity to the proper quantification of junctions. Can the program deal with this complexity? If so, would be very nice to include an example. If not, please also more stringently then discuss the limitations of the program.

2) One important point does need to be clarified. It is not exactly clear from the figures, legends or Materials and methods how the statistics were done. The authors name all the appropriate tests but it is not clear e.g. whether means of technical replicates or the collective number of junctions were used for statistical test. Clearly, the high number of junctions that can be analyzed here is an advantage. However, the variance between experiments is not shown and it is not clear whether the statistics take that into account.

Reviewer #2:

1) This manuscript describes a novel semiautomated software, 'Junction Mapper,' for analyzing cell junctions on parameters such as defining the junctional interphase, intensity, and length. Currently, analyzing cell junctions is often done manually which can be time consuming and laborious, even when using automated software, it is usually tailored to a specific cell type or unable to automatically distinguish nuances of perturbed or fragmented junctions. The authors evaluate their software's performance in several cell types, and in multiple conditions to evaluate its ability to detect a range of phenotypes (from severe to mild). This manuscript presents a new tool that address these significant problems and has the potential to be widely applied. However there are numerous flaws and oversights in this presentation that significantly dampen my enthusiasm. There is also a lack of rigor in evaluating the algorithms as presented which makes it difficult to assess the utility of the software thereby raising a major concern.

2) First, the availability of the software and test data sets is not clear. Nor is the computing language or platform that the software is written in. This is a major oversight. Second, the microscopy needs to be fully described. There are not scale bars on images. Are these max intensity projections, single confocal slices, widefield images, deconvovled? What is the resolution? The quality of the input will impact the ability of the algorithms to function and this needs to be defined.

3) How do different user selected parameters impact the output from the program? Since the skeleton can be manually adjusted, does the specific skeleton have an impact on the results? These factors need to be considered and quantified for their impact on the final measurements.

4) Input parameters need to be discussed – dilation and threshold level are important parameters to disclose for each analyzed data set. How do these impact final measurements?

5) The process of interactive editing, blurring, and sharpening is not shown nor well described. Is this process done manually on every image? Can it be automated for a data set? Seeing these steps, including when manual adjustment is required would be helpful. The reader has no feel for how often user intervention is required (every cell, every image, every border?).

Reviewer #3:

The manuscript describes the development of software for quantifying the phenotype of cell-cell contacts from high resolution images. The authors have been able to produce an impressive data set with the tool. However, the new tool is not validated sufficiently, and the methods are not adequately described. This is particularly important, as by the studying design, the biological ramifications of the analysis were not probed.

1) In the Introduction (third paragraph), the authors make the claim that the software developed for analysis of Drosophilia or nematode epithelia are not applicable to mammalian cells. Image analysis algorithm performance are typically based of the nature of the structures to be analyzed and the quality of data. There is no reason for these parameters to be fundamentally different in all mammalian cells. If the authors, are trying to say that tools for analysis of epithelial cells may not be directly applicable to other cells types or in all possible treatments (points made later), they should be more explicit here. Also, the (Held et al., 2011) does not describe the analysis of cell-cell contacts and does not seem to support the authors point.

2) The development of a new algorithm for image analysis is typically associated with several key endeavors. First is validation. Validation must be performed on data where the ground truth is known. For a "first-of-kind" algorithm this is often associated done with simulated data or data that was analyzed by hand. By this standard definition, the Junction Mapper is not validated. This must be corrected for the manuscript to be considered for publication. It seems that the data shown in Figure 6 may be appropriate for this task, as the data was previously analyzed by hand? This reviewer notes that citations within the manuscript are validated in this manner (i.e. Held et al., 2011). Also, the section in the Materials and methods described "Software validation" actually discusses exclusion criteria and naming procedures.

3) Additionally, there is typically an analysis of when the algorithm begins to fail. This is often done in terms of data with varying signal to noise. The limitations of this of the Junction Mapper are not tested. While it would be preferred that a formal analysis of the performance of the algorithm be performed, at a minimum image quality (which is often reported as signal to noise ratios) requirements (or at least typical image characteristics) should be provided so that users know the criteria for the suitability of the algorithm are met being attempting to use it.

4) The Materials and methods also lack sufficient detail. According to the manuscript, the Junction Mapper is a novel stand alone software. This means specific algorithms for background estimation, skeletonization, segmentation, and parameter calculation were used. Precise definitions (including formulae) or citations to the utilized algorithms need to be provided. Also, formulae describing how the parameters were calculated need to be added. Also, how corners were identified needs to be explained in greater detail. If corners are manually detected, then it is improper to state the Junction Mapper detected them. Additionally, are all junctions analyzed at once or individually? If different segmentation parameters are used on different junctions, are the results actually directly comparable? This reviewer also notes that the required details are not available in the often-cited previous work of Erasmus et al., 2016. This is understandable as that was a highly biological study, but that reference should not be used to described methodological details.

5) In several places the authors make claims that junctions that are straighter are more tensed. This is not true, as the junctions could also be stiffer, and therefore deform less. As no measurements of junctional tension were made, these statements should be removed.

6) The algorithm seems to assume constant width for the junctions. This will likely lead to substantial errors in area estimations. Have the authors given thought to this issue? Are the errors inconsequential? Can the algorithm be readily updated to avoid this artefact?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Junction Mapper is a novel computer vision tool to decipher cell-cell contact phenotypes" for further consideration at eLife. Your revised article has been favorably evaluated by Anna Akhmanova as the Senior Editor, a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #1:

The authors took a lot of effort to address the points that were raised by the reviewers. I do not have the proper expertise to judge whether the authors have sufficiently addressed the points of reviewers 2 and 3.

1) In response to point 2, the authors now describe which statistical tests are used and clarify for which figure panels they used biological or technical replicates. The authors now state that the statistics and the tests used are in Supplementary file 5. Unfortunately, I was unable to find Supplementary file 5 in the present submission, making it impossible whether the statistics were done properly. Importantly, the authors still do not clearly state in the legends and/or Materials and methods the number of replicates on which the data shown are based on. Throughout the manuscript, each measured junction is called a sample and the number of analyzed junctions are now provided in the figures. However, for the statistics the authors should provide information on the number of replicates, meaning number of independent experiments or biological samples, in the figure or legend to clearly show that differences and significance levels are due to the high number of junctions but not because of experimental variation.

2) For siRNA experiments the section on statistical analysis says that only one control and knockdown group was analyzed. If this is not a misunderstanding, then even high number of analyzed junctions from one experiment do not allow strong conclusions as experimental variation upon knockdown of CIP4, EEFA1A or VAV2 has not been assessed. For physiological relevant conclusions one would expect a set of at least 3 independent experiments. I do understand that the authors want to test their very interesting tool for which they provide many different experimental tests. However, the authors should then acknowledge and tune down mechanistic conclusions. For experiments concerning HUVEC cells, there is no information on the number of biological replicates on which the data are based.

3) Thus, at present the way the data are presented now, provides nice evidence that the program allows for quantification of high number of junctions to potentially detect small differences. If the authors want to use the experiments shown in the manuscript to validate the usefulness as well as limits of the software, this approach with limited number of repetitions seems valid but then this has to be made more clearly throughout the manuscript. Not all of the data sets are sufficiently comprehensive to univocally demonstrate a biological relevant junctional outcome upon treatment or knockdown and this should be acknowledged. Having said this, I feel if the authors were able to address the concerns of reviewer 2 and 3, they should be provided the opportunity to properly address and include in the manuscript the comments above.

Reviewer #2:

Overall this tool has the potential to be useful for researchers, and the authors have now included many more rigorous definition of the method and treatments of the parameters both in definition and in comparison of data processed in different ways. This strengthens the manuscript. However, I am still not sure this is sufficient to fully describe the bounds of the junction mapper approach.

1) Most scientific conclusions as presented come from comparisons of values in control/disrupted. When looking at effects of user inputs the graphs are shown for each treatments individually but what are the changes with different thresholds/dilations between treatments (i.e. Figure 3—figure supplements 2 and 3)? Would different biological conclusions be drawn if you push the dilation or threshold "too far"?

2) Authors point out a central issue and why this analysis is challenging – If there is no staining at a cell corner then where the program or user places the junction is arbitrary. Without a second marker of plasma membrane rather than junction this will always be an issue these measurements regardless of what automated algorithm is deployed or with user definition.

3) The authors show secondary characteristics are more robust to error in corner selection and that individual users get same direction of changes but not same absolute values, which does show the value added here. This should be emphasized in the Discussion.

4) For the noise quantification, there should be a metric for measurement accuracy, or deviation from the ground truth. Guidance for user on minimum S/N needed for robust quantification. There is also no information on type of noise added (shot noise, dependent on pixel intensity is dominant noise in most microscopy images and is recommended here). The goal would be for a user to know if a junction has sufficient S/N to be analyzed.

5) This leads me to the quantification of the type "ee" boarders in the H-RasG12V overexpressing cells. There appears to be greatly reduced e-cad staining at the boarders (it is difficult to see by eye any in the examples shown). In this case, how are the interfaces defined? Does this lower signal to noise negatively impact the program? How confident should we feel about comparing images with different S/N levels?

Reviewer #3:

The manuscript is greatly improved and nearly ready for publication.

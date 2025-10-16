# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84112.sa0](https://doi.org/10.7554/eLife.84112.sa0)

This valuable Tools and Resources paper presents a solid workflow for testing and comparing variations in tissue clearing, antigen retrieval, and antibody staining methods using thick slices of tissue. Though staining results vary sensitively with processing conditions, results from screening conditions in mouse brain tissue can be carried over to staining in human brain tissue. This solid story will be of broad interest to those carrying out immunohistochemistry experiments in human tissue samples.


---

# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84112.sa1](https://doi.org/10.7554/eLife.84112.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Tissue libraries enable rapid determination of conditions that preserve antibody labeling in cleared mouse and human tissue" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife at this stage.

Specifically, the reviewers noted and detailed a lack of clarity in key points of the protocol, and a rather large variability in the staining outcomes. Additionally, the reviewers were concerned about a few key assumptions regarding the properties of the subset of antibodies tested, and premature generalization of the results from analysis of these antibodies.

Overall, the work has a lot of potential, and we encourage resubmission of the story when the reviewer comments can be adequately addressed.

The complete and detailed reviewer evaluations are below.

Reviewer #1 (Recommendations for the authors):

Immunohistochemistry (IHC) encompasses a complex set of methods with many possible variations on conditions for tissue fixation, clearing, antigen retrieval, blocking, and staining. Choices of these conditions that are optimized for one antibody/target pair often do not generalize to others, or to other tissue types. As high throughput microscopy (particularly lightsheet microscopy) and clearing methods allow for imaging thicker blocks of tissue, these problems are increasingly a limiting factor in experimental studies. A more systematic understanding of how these various aspects of IHC methods choices should be made is of great interest. Optimizing IHC conditions for a given protein target in a given tissue is currently somewhat of an art. A more systematic approach to carrying out this optimization is also potentially of great interest. This would be particularly helpful for human tissue, as it is too precious to routinely test many IHC method variants.

The authors set out to create a streamlined, standardized tissue processing and image analysis workflow for comparing different tissue preparations in terms of IHC performance. They create a library of mouse brain tissue specimens processed with several variants of each processing step including fixation, clearing, and antigen retrieval. They vary only one parameter at a time to facilitate direct comparison between conditions. They set up a data analysis pipeline that is extremely simple and easy to use but probably underpowered for comparing quantitatively between conditions because it keeps only a signal mask and discards signal intensity information. It is also not clear how the pipeline should be modified to accommodate targets with different types of staining pattern. The results are presented as a 1D heatmap that varies with depth in the specimen, rather than a simple line plot, making it difficult to compare quantitatively between conditions.

Each of 12 process variants is carried out for two antibodies on three replicate specimens to assess repeatability. The authors do not discuss this experiment in detail, but there is high variability between replicates. For example, in Figure S1, the 2 days cleared case has fairly high signal in two replicates and almost none in the middle one. The staining solutions were apparently also not well mixed, as the antibody signals on the two sides of each specimen are very different in all cases, and the amount of difference between the two sides is also highly varying between specimens. From Figure 1, it is also clear that the signal varies across each specimen within the imaging plane. In this comparison of 12 conditions, one result pops out: incubating the antibodies at room temperature (as opposed to the default of 4oC) improves penetration. This effect is dramatic for NeuN. It is probably also present for Glut1, although it is necessary to look at Figure S2, showing all three replicates, to see this clearly. Every other method variant appears to result in worse performance except that in the case of 2 day clearing with Glut1 staining, one replicate has a particularly high signal area (Figure S2).

They then test two antibodies against GFAP and show that varying processing conditions affects both antibodies similarly, though they do not include any quantification. In contrast, they find that two antibodies against tau do vary differently with processing conditions, but again without quantification. Next, they carry out the same screen in human brain tissue that had previously been done in mouse brain tissue in order to assess the suitability of mouse tissue as a proxy for IHC quality in human tissue. The trends of IHC quality as a function of method variant appear to be qualitatively preserved between mouse and human. They finally show that three antibodies (primaries directly conjugated with fluorophores) against Glut1, tau, and NeuN fully penetrate through a 1 mm slice of human brain tissue after incubating for 14 days.

The goal of putting IHC on a more quantitative footing is an admirable and timely one, but the approach presented here requires some more work to deliver on this substantial promise.

Tissue library: Tissue thickness and staining time choices should be justified more carefully. Of particular concern is the antibody staining time, as the optimal time depends strongly on the temperature of incubation. Staining should be quantified at several time points to determine the extent of saturation at the tissue surface. The assumption that antigens have a "relatively constant distribution with the depth of imaging" should also be supported with data. The same goes for lateral variation. Variation between replicates also would ideally be reduced. From the methods, it seems as though the antibody is simply added to the staining buffer with the tissue, which might indicate there is insufficient mixing before and during antibody incubation.

Image analysis: A more sophisticated but still highly user-friendly segmentation strategy such as the Ilastik software package might be a more reliable and versatile choice for analyzing image data. Furthermore, the signal intensity distribution within the masked signal area can be extracted (e.g. in Matlab) to quantitatively compare processing conditions, in addition to the area occupied by the mask as used here. The area outside the mask could potentially be treated as a background segment, whose intensity distribution can also be quantified. This way, quantitative measures of both signal intensity and background staining levels could be used for a more full comparison between method variants. The results should be viewed as a 1D line plot for more quantitative comparison between conditions. Finally, this lineplot could be used to measure derived performance parameters such as the distance into the tissue at which the staining intensity drops by half.

These improvements in quantitation are necessary to draw strong conclusions from any further experiments, but with them this work stands to make a strong contribution to the field.

Reviewer #2 (Recommendations for the authors):

This work presents a systematic approach to evaluation and optimization of antibody labeling in cleared human brain tissue. The authors outline the problems very clearly and present strategies to solve them. First, libraries of tissue prepared using different protocols are generated to easily test the performance of different antibodies and different staining conditions. Importantly, only one condition at a time is varied, which allows to evaluate the contribution of individual variables to the final staining quality. Second, a strategy for finding the optimal conditions for simultaneous staining with several different antibodies is outlined. And third and very important results is that mouse tissue can be used for optimization of antibody labeling of human tissue, thus allowing efficient use of human tissue which is a scarce and very valuable resource.

Strengths

Antibody labeling of tissues, and especially large volume cleared tissues involves a multitude of steps and reagents. Variations in any of the tissue preparation or immunolabeling steps can affect antibody performance and finding the optimal conditions can be a very tedious process. This paper provides clear examples of how much variability there can be even when using the same antibody on the same tissue prepared in different ways or stained under different conditions. It gives a clear solution of how this problem can be addressed by using libraries of tissues prepared by varying a single condition in each instance.

The presented approach results in a huge saving of time as it can be completed much faster (several days) compared to the complete immunolabeling protocol for large volume cleared tissue which can take several weeks.

The demonstration that mouse tissue can be used for optimization of staining conditions for human tissue is very important, allowing the best use of human tissue.

Weaknesses

Results from a small number of antibodies are extrapolated to apply to all antibodies in general. For example, the results from the comparison between 2 different GFAP antibodies, showing that the antibody conjugated to a fluorophore performs better that the antibody that is not conjugated, is used to generalize that primary antibodies directly conjugated to a fluorophore are preferrable to use compared to antibodies that are visualized using indirect immunolabeling with a secondary antibody. Even when considering the 2 GFAP antibodies this conclusion cannot be made, because it is not clear whether the difference in performance is due to the primary antibodies themselves (monoclonal vs. polyclonal) or to the method of their visualization (direct vs indirect).

The authors conclude that "IHC is limited more by denaturation of the epitope than the antibody itself". This conclusion is based on the experiments that show that varying the conditions of tissue preparation and staining can dramatically change antibody performance from no label to excellent label. However, the authors do not take into account that they are using antibodies that have already been shown to work reasonably well for immunolabeling.

Important methodological information is missing in some instances, for example how was the human tissue fixed or how are the tissue libraries stored.

Recommendations in order of appearance in the manuscript:

Introduction: It is very well written! It is important to specify here, as done further below in the paper (in Comparison of IHC conditions for different antibodies directed against a single protein) that the proposed strategies apply when "the antibodies are of high quality, have high specificity and limited off-target binding".

Results, Measuring IHC quality in cleared tissue: It is unclear how the threshold was determined. Another concern is that this "measure of IHC quality" is essentially a measure of what fraction of the tissue is labeled. Thus, it does not account for specific vs non-specific staining.

Conditions that influence antibody and epitope preservation: It is unclear whether the baseline protocol described here applies only to mouse tissue or to human tissue as well. The mention of perfusion leads me to believe this is specifically for mouse, but I couldn't find information on how the human tissue was fixed.

There is no mention here of whether the antibodies (GluT1 and NeuN) are directly conjugated to fluorophores. I assumed that they were, based on the info in the Methods section. But then in the last paragraph of Results the authors say that "Therefore, we directly conjugated three antibodies to three different fluorophores (NeuN-A568, Glut1- A488, and AT8-A647)." Which to me implies that they weren't conjugated in previous experiments.

Comparison of IHC conditions for different antibodies directed against a single protein: As explained in the Public review section, I disagree with the conclusion "it is recommended to use primary antibodies directly conjugated to fluorophores whenever possible." Unless the authors add more experiments that compare direct vs. indirect immmunolabeling with the same primary antibody (for several different antibodies), this conclusion is not justified.

"In order to examine how much of the observed variability in antibody labeling is due to targets being more or less accessible depending on cell type or subcellular location, multiple antibodies were also chosen that recognize tau protein." I don't understand what the comparison of the tau antibodies will tell us about the accessibility of targets depending on cell type or subcellular location.

Mouse brain tissue as a model system for optimizing IHC in cleared human tissue: Determining the optimal protocol for simultaneous staining of 3 antibodies is an important point. It will be very useful if the authors elaborate more on how this optimal protocol was determined. How was the combination of conditions that maximize staining quality established? Minor point: how was the 14 days duration determined?

Discussion: "Rather than the antibody, our data suggests that poor staining is most often due to denaturation or blockage of the epitope." I disagree with this conclusion, as explained above.

"Unfortunately, as we found with the dopamine receptor 2 and GFAP IHC, a protocol may not exist to allow for both targets to be effectively stained simultaneously." – I didn't see this presented in the Results section.

Materials and methods:

How were the human samples fixed? Were the slicing and all the following steps performed in an identical way? I assume they were, but this should be stated clearly in the methods. How were the tissue libraries stored? For how long can they be used after preparation?

Figures

Figures 1, 2 and others. How is the top of the side view determined? Is this the surface of the tissue and therefore conditions where the label in the side view starts lower that in other conditions means that the tissue surface was not labeled? And why would that be? If that is not the case, it will be best to align the side views and have the labeling start at the same level.

Figure S3. This is a very clear way of summarizing the differences in labeling. It would be very helpful to have this summary next to the actual immunostaining images in the main figures.

Figure S9 Representative microtome images taken from the human tissue prior to staining: Do you mean prior to clearing?

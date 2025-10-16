# Peer review - Round 1

Editors:
- Tanya T Whitfield, University of Sheffield United Kingdom

Reviewers:
- Stefan Heller, Stanford University United States

## Review text

DOI: [10.7554/eLife.40946.039](https://doi.org/10.7554/eLife.40946.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cellular cartography of the organ of Corti based on optical tissue clearing and machine learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Stefan Heller (Reviewer #1).

The reviewers have discussed the reviews with one another and agree that the manuscript requires minor revisions, which should be relatively quick to address. The Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Urata and colleagues describe a technical solution to minimize manual processing of cochlear samples from mice for quantitative analysis of hair cell numbers and location. The concept builds on a modified Sca/eS tissue clearing method, combined with immunolabeling of hair cells, 2-photon microscopy, and an elegant way of stitching image stacks and assembling a 3-dimensional image. The core of the automated analysis method is a series of MATLAB scripts that perform the analysis.

Essential revisions:

1) Please give more information about the methodology for the machine learning model and include a comparison with other methods. Transfer to other scripts is not essential, but please comment on whether such a transfer would be an option and how this might be done by someone interested in doing a similar analysis.

The full reviews are appended below.

Reviewer #1:

The MATLAB scripts appear well-documented and utilize common toolboxes. Unfortunately, this reviewer currently does not own a MATLAB license and therefore was not able to run the scripts to test for general applicability.

This brings me to my main critique. The beauty of this work is that it allows the researcher to process a large number of cochlear samples in parallel. With acquisition times of about 4h per sample using a 2-photon microscope and a 25x (NA = 1.1) objective and 30 min for an average analysis workflow, this method is indeed a major advancement for laboratories interested in an efficient and throughput-oriented method for quantitative assessment of hair cells and hair cell loss in the cochlea.

Nevertheless, the requirement for an expensive software package diminishes enthusiasm. What would it take to transfer the scripts to a widely available and free-for-all environment such as Python, Java, or R? Even C/C++ or a combination of languages comes to mind.

The overall approach is quite clever and this reviewer is enthusiastic about the work. Besides the automated data analysis, there is another very interesting hidden gem in this manuscript that this is related to Figure 4, and to the principles of observed clustering of lost hair cells and the two-component model. The use of a combination and dynamically changing (with age or noise challenge) model that takes into account local neighborhoods and position is truly a creative way to approach the analysis of such an observation. In this respect, I consider the results presented in this section of the paper and summarized in the last paragraph of the subsection “Model-based analysis of hair cell loss”, as a quite important and relevant finding.

A second critique concerns the core method used for data analysis. Machine learning is such a buzzword, but it is not a simple method that is replicable for the common reader. Exactly what kind of principle was utilized? Please provide accurate references already in the text presented in the second paragraph of the subsection “Machine learning–based automated detection of sensory hair cells”, and explain in more palatable fashion the kind of neural network approach that was used. Appendix 3 (Step 4) has some of this information, but the description there is difficult to follow and perhaps should be illustrated with some kind of drawing of the process. Appendix 2—figure 5 is a good start as it shows the sample that is investigated directly, but it does not communicate the process. Since this is an important component of the core method that is presented, one would expect a more detailed and more approachable description of the procedure.

Reviewer #2:

This manuscript by Urata et al. reports an application of a tissue clearing method for whole organ of Corti imaging and a following quantitative analysis. This reviewer thinks that the work is very important for the field, because a limited method had been applicable for the observation of the organ. The quantification and modeling analysis on the mechanism of hair cell loss due to aging and noise will also give an impact to the field. This reviewer thus appreciate the basic concept of the study, while I found many points which should be corrected and improved in future manuscript.

1) Please provide a simple and easily understandable figure indicating the step-by-step procedures of data processing according to the information in Materials and methods and Appendix part (e.g., Steps in Appendix 3) by modifying Figure 2. In the current manuscript, it was very difficult to follow and find relations of these steps in Figure 2 and Materials and methods/Appendix. Also, it seems problematic that there is no indication of procedure in Figure 2B (e.g., words such as "raw data" "stitching" "linearize" should be indicated in the panel).

2) The panels in Figure 3A and Figure 3—figure supplement 1A and the graph in panel B seem the same. Reuse of the same figure panel or data should be made explicit in figure legend. Is there any reason why the Figure 3—figure supplement 1A is elongated?

Reviewer #3:

This manuscript describes a method to image and quantitatively characterize the spatial arrangement of sensory hair cells in the organ of Corti. A sorbitol-based optical clearing method was developed to optimize tissue clearing and immunolabeling to improve tissue transparency and antibody accessibility. Two-photon microscopy was used to image the organ of Corti in 3D. The spiral sensory epithelium was then linearized and the positions of the inner and outer hair cells (IHCs and OHCs) were automatically located using a machine learning based algorithm. Using the new sample preparation and imaging analysis method, the authors analyzed age-related and noise-induced cell loss in young, adult, and noise-exposed mice.

One novel aspect of the paper is the modification of the Sca/eS optical clearing protocol, which first decalcifies the bones and then uses a guanidine-based solution to increase transparency of the sample with minimal tissue expansion and GFP fluorescence quenching. The modified Sca/eS method was compared to established methods, including 3DISCO, iDISCO, CLARITY, CUBIC and Sca/eS, and MYO7A and F-actin labeled hair cells were most clearly identified in samples treated with the modified Sca/eS protocol.

The authors then fit a spiral curve based on the 3D image information and linearized the entire sensory epithelium of the organ of Corti for further image analysis. This approach is quite impressive to me, although I have to admit that I am not an expert in this field and am not sure whether this approach (e.g. linearization of the entire sensory epithelium) is novel to the auditory research field.

Localization and classification of IHCs and OHCs using a machine learning method are nice. But very little details were provided to describe the convolution neural network model and how the training and testing were performed. This needs to be further clarified and fleshed out in the revised manuscript. It does not look like that the authors have improved the structure of the machine learning model. The number of samples used for training and testing the machine learning model is limited and can be improved.

Since the two-photon fluorescence images have very high contrast, a standard imaging processing method, such as 3D watershed, may just do the job with sufficient accuracy. It would be helpful to include a direct comparison of the machine learning model and the watershed algorithm. The reviewer also felt that the authors may consider downplaying the role of machine learning in the title and throughout the manuscript as traditional methods may achieve similar performance.

Based on the localization analysis of the IHCs and OHCs, age-related and noise-induced cell loss was quantified and compared between different mice models. I will not comment on the biology of the auditory system since this is beyond my expertise.

Overall, I commend the authors for providing a very careful analysis of the experiment results and assembled a comprehensive manuscript. Addressing the above comments may help to further strengthen the manuscript.

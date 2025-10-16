# Peer review - Round 1

Editors:
- Markus Meissner, University of Glasgow United Kingdom

Reviewers:
- Markus Meissner, University of Glasgow United Kingdom

## Review text

DOI: [10.7554/eLife.40560.020](https://doi.org/10.7554/eLife.40560.020)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Acceptance notification:

The reviewers appreciate that you addressed all major concerns and have no experimental questions. The reviewers point out that your manuscript fits well as a Tools and Resources article, since it is a nice proof of concept study, but doesn't provide novel biological insights.

Decision letter after peer review:

Thank you for submitting your article "An Artificial Intelligence Workflow for Defining Host-Pathogen Interactions" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Markus Meissner as the guest Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Detlef Weigel as the Senior Editor.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

Summary:

In their report Fisch et al., develop an open-source imaging platform (HRMAn) that integrates machine learning and deep learning, in order to analyse of multiple phenotypes related to host-pathogen interactions. The platform is openly available via KNIME Workflows, which will allow others to benefit the presented pipeline. The analysis follows basic principles, established by similar HCI platforms, involving illumination correction, followed by segmentation and infection detection (Stage 1). This is followed by an analysis of host protein recruitment, by detection of p62 at the parasitophorous vacuole. The authors also demonstrate that the analysis pipeline can be easily adjusted to other intracellular pathogens, such as Salmonella typhimurium.

Major concerns:

The reviewers raised some concerns regarding the technical novelty of this analysis pipeline. In particular analysis performed in Stage 1 is quite standard and follows similar methods as described before (see for example Touquet et al., 2018). The analysis in Stage 2, although well performed, does not represent a major methodogical advance in the field of machine learning.

Although the authors present some applications of this analysis pipeline, it would be advisable to provide additional data, demonstrating that HRMAn can detect additional, previously established phenotypes, such as those for ROP18 or ROP5.

Another application could be to probe for protein export from the parasite to the host cell, since this would broaden the analysis to detect additional host-pathogen interactions.

Given that HRMAn only provides a modest improvement over existing software, primarily in the user interphase, it would be appropriate to more extensively test its function in more authentic experimental settings (see also comments of reviewer 3).

The authors should also provide examples, why their analysis platform is superior. The authors acknowledge the existence of many other tools for high throughput analysis, but little to no discussion of similarities or difference to these tools is given.

While all reviewers agree that the experiments have been carefully performed, there is some scepticism regarding the novelty as a method (Reviewer 2) and the breadth of applications this tool will be used for in the field (Reviewer 1 and 3). As it stands, this tool appears to be optimised for the primary research interest of the authors, where it will certainly be very useful. However, it is unclear if other researchers in the field will recognise the advantage of HRMAn over existing HCI platforms (Reviewer 1 and 3).

Separate reviews (please respond to each point):

Reviewer #1:

Summary:

In their report Fisch et al., describe the establishment of a novel, open source programme for High Content Imaging (HCI). The major advantage of this system is the integration of machine learning, making it probably more adaptable to the analysis of different phenotypes related to host-pathogen interactions. The data and analysis appear to be of the highest quality and there is little doubt that HRMAn is a robust new tool to automatically detect phenotypes, which will be a valuable source for HCI. Especially since it is now possible to perform genome wide screens in Toxoplasma gondii, this pipeline comes in very handy for some researchers in order to perform phenotypic, image based screens on this parasite. The authors also demonstrate that the pipeline can be easily adapted to other pathogens, using Salmonella as a proof of principle.

Own opinion:

The described technology will be very useful for researchers planning to perform image based screens on host-pathogen interactions or on intracellular pathogens in general. Therefore, this study will be certainly of interest for a broad readership.

On the downside, it is a technological advance without novel biological insight. As the authors mention, there are many open source platforms available (not to mention commercial software) that allow HCI analysis of parasite growth, invasion, etc. (CellProfiler, CellClassifier, Fijii, etc.). A recent publication used a relatively simple HCI analysis to perform chemical screens in Toxoplsma gondii (see Touquet et al., 2018), which is certainly inferior to the platform presented in this study.

I am a bit unsure, how and why the provided pipeline is superior to other pipelines. At least the basic principles of HCI analysis appear similar:

– Pre-processing for illumination correction

– Segmentation (in this case host cell vs parasites)

– Analysis of pre-defined features (i.e. size of parasitophorous vacuoles, host cell nuclei, etc.)

As such I am not fully convinced if the platform is indeed superior to other imaging analysis software. For example in our lab we used Cell Profiler, which allows us to determine invasion rate, parasite growth rate, host cell number, etc. The authors should provide some examples or an in depth discussion regarding the advantages of their pipeline, when compared to other

Saying that, the described image analysis pipeline is very well designed and if widely used in the field will allow to analyse quantitative phenotypic data that are comparable in between different laboratories.

The manuscript is well written and the techniques used are of the highest quality. The presented data are very solid, demonstrating that this analysis pipeline is very accurate. Unfortunately I cannot comment on machine learning, since this is outside my area of expertise.

At this point the analysis pipeline is well suited for the analysis of host-pathogen interactions, in particular the characterisation of host-protein recruitment to the PV, a key interest of the Frickel lab and this aspect is of somewhat narrow interest.

It would be good to summarise in an additional figure, which phenotypes this imaging platform can differentiate.

For example, instead of host protein recruitment, it would be of great interest to also analyse parasite protein export into the host cell. Parasite lines expressing for example dense granule proteins are well described in the literature and it should be straight forward to add this parameter to the analysis pipeline.

In summary, it is a well described analysis pipeline for HCI that might find broad applications, especially now, that genome wide screens can be performed using CRISPR/cas9.

Reviewer #2:

The proposed analysis will be made openly available via KNIME Workflows. This is certainly a plus since it will allow others to benefit from the presented analysis pipeline. Additionally, KNIME is easy to install, with a bit of practice very intuitive, and could on demand also be used to change/extend the workflow.

The overall analysis pipeline can be divided in 3 steps. An illumination correction step followed by a segmentation and infection detection step (named 'Stage 1'), followed up by an analysis of host protein recruitment ('Stage 2').

The analysis in 'Stage 1' is not bearing surprises or any methodic novelty. The proposed pipeline, a combination of default analysis components, solves the task at hand as long as the provided images (after illumination correction) can be segmented via a simple threshold. The merit of 'Stage 1', as mentioned above, is clearly not any methodological advance or interesting combination of existing methods. It is, never the less, sensible engineering work and might very well help others that desire to perform the same analysis.

In case a host protein recruitment analysis is desired, a 'Stage 2' workflow is proposed. Besides a decision tree that is used in Stage 1, this is the only place where any machine learning technique is applied. More specifically, a variant of the well known AlexNet is used to learn to classify protein recruitment. The relatively shallow network architecture and all parameter and training decisions are sensible set to values used in many neural network applications. While, as before, nothing here is even close to being a methodological advance in the field of machine learning, all decisions seem well thought trough and I have no problems believing that final classification results are good.

It might be desirable to compare the proposed analyses system (or its components) to other existing systems or modules. (The authors acknowledges the existence of many other tools for high throughput analysis, see Supplementary file 1, but little to no discussion of similarities or difference to these tools is given.)

The impact of this work will depend on the presented data and the utility of the proposed analysis pipeline (which is/will be openly available). I am, unfortunately, not the right person to judge how many research project are currently just waiting to use an analysis pipeline as the one presented in this manuscript.

I would like to end my review by stating my biggest concern. After reading the title and Abstract of this manuscript, I expected the presented work to be significantly more involved. It turns out that the presented workflow uses one decision tree in Stage 1 and an 'off the shelve' AlexNet in the optional Stage 2. I would advice the authors to tone down the paper pitch in this regard.

In summary, I do not believe that the presented manuscript contains enough methodological advances to justify publication of the method alone. If the presented data and performed analyses justifies publication will have to be judged by a person in the field of image-based infection biology.

Minor Comments:

The last sentence in the Abstract makes a bold statement about 'operating at human capability'. This was in my point of view not shown in the manuscript and therefore ends up being a bold claim lacking justification.

While I could follow all explanations about network training, some formulations could benefit from feedback by a person with publishing experience in the field of machine learning.

Reviewer #3:

The authors develop an open-source image analysis platform named HRMAn that relies on machine learning algorithms and deep learning. Given input images, the platform characterizes phenotypes such as parasites/vacuole, vacuole size, and host-protein recruitment. The platform is also high-throughput, allowing for the bulk submission of many images simultaneously. To validate the platform, the authors trained the algorithm with an annotated dataset of host cells infected by eGFP-expressing Toxoplasma gondii parasites. Using this training dataset, the authors quantified differences in parasite killing/growth restriction strategies across host cell lines and between Type I and Type II Toxoplasma lines. The authors also validated the algorithm's ability to quantify levels of ubiquitin and p62 recruitment to the PVM. Finally, the authors retrained the algorithm using an annotated dataset of Salmonella typhimurium, demonstrating the ability of HRMAn to recognize and quantify a diversity of pathogens.

HRMAn provides a high-throughput and effective strategy for analyzing phenotypes by microscopy. The platform removes the human component of analysis and bulk-input allows for the rapid analysis of thousands of cells. The interface is remarkably easy to set-up and navigate, particularly alongside the available tutorials. The demonstration of success with two pathogens of drastically different size, Toxoplasma gondii and Salmonella typhimurium, suggests that this could be a valuable tool for a wide array of microbes. While the recruitment of host-proteins to the PVM is a potentially powerful tool, it is currently limited to binary processes (presence or absence of ubiquitin/p62). As shown, it is unclear if HRMAn can detect more subtle, non-binary phenotypes, such as recruitment of mitochondria. The authors demonstrate the ability of HRMAn to quantify differences in ubiquitin and p62 recruitment between both different host cell and different parasite lines upon IFNγ-priming. It would be desirable to demonstrate HRMAn's ability to detect previously established phenotypes, such as those of ROP18 or ROP5. This will more strongly validate HRMAn's potential ability to detect novel phenotypes. Given that HRMAn only provides a modest improvement over existing software, primarily in the user interphase, it would be appropriate to more extensively test its function in more authentic experimental settings.

Major concerns:

a) Since there are many differences between Type I and Type II parasites (including growth rate and viability, which could affect the recruitment measurements), it would be appropriate for the authors to look at isogenic lines that differ only in a particular effector. The authors could test HRMAn's ability to detect previously known phenotypes, such as the increase in GBP recruitment in a ROP18 knockout.

b) It is unclear why the authors, when classifying parasites/vacuole, bin the vacuoles by 1, 2, 4, and greater than 4. The authors should provide rationale, technical or otherwise, for binning all vacuoles >4 together, since some phenotypes might emerge only later during intracellular growth.

c) In Figure 2C, the example picture for >4/vac appears to be a picture of a vacuole containing 4 parasites. This should be corrected.

d) It is important that the training dataset used for the manuscript be released in its entirety to ensure that readers can replicate the results of the paper and account for any differences between lab-specific assignments and HRMAn.

Minor concerns:

a) The authors often use the phrase "cell" ambiguously and it is unclear if they are referring to host cells or parasite cells. The authors should take care to reduce ambiguity by more clearly stating which cells they are referring to.

b) In Figure 2E, the heat map of the confusion matrix is difficult to accurately assess due to the similarity between many values. Number values should be provided as well, or in place of the matrix.

c) In Figure 2—figure supplement 1A, images displaying separation of the channels should be provided. As such, it is difficult to evaluate the presence of GRA2. The current image does not seem to accurately represent the 98% prevalence of GRA2+ vacuoles. By separating the image channels this should be more apparent.

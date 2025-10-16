# Peer review - Round 1

Editors:
- Hina Chaudhry, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71359.sa0](https://doi.org/10.7554/eLife.71359.sa0)

In this manuscript the authors demonstrate that X-ray imaging delivers more detailed information than standard histology by analyzing 3D information in myocardial tissue obtained from COVID-19 patients. The findings are of particular interest regarding the segmentation of the vascular network and intussusceptive angiogenesis. The authors introduce the utilization of machine learning, and state-of-the-art techniques of X-ray phase contrast which is likely to advance future work in this field. Finally, with this manuscript the authors also provide new, more detailed insights into the pathologies associated with cardiac injury due to COVID-19.


---

# Peer review - Round 1

Editors:
- Hina Chaudhry, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71359.sa1](https://doi.org/10.7554/eLife.71359.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "3D virtual Histopathology of Cardiac Tissue from Covid-19 Patients based on Phase-Contrast X-ray Tomography" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Guest Editor and a Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Guest Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please refer to revisions requested by the reviewers below, particularly as outlined by Reviewer 1 whose critique will greatly help to strengthen this manuscript and its conclusions.

Reviewer #1 (Recommendations for the authors):

Below the authors will find my additional comments to increase the clarity of their work and making it suitable for eLife.

Abstract: "first time" Several times the authors mention this paper that this is the first time that such a study is done. It's only partially true. Over the past two years a lot of study have been published or are currently in accepted state about analysis of COVID-19 cardiac samples (for instance Walsh 2021 that the authors cite analyze partially whole heart as well).

l69: "we have introduce". The authors are not the only group working on this topic. A more general sentence saying that this field is growing would be more appropriate.

l76: "entire organ" -> "entire human organ". The example cited of Walsh is on human organs. However, a lot of work has been already done in the past in entire organ of animals such as mouse.

l79: "cytoarchitecture". It's a bit misleading as we expect to see results of the level of TEM. It's true that this level is reached for the results presented with the WG configuration but partially for the core analysis of the paper. Indeed the results focus on the general organization and vasculature.

Why the analysis has not been done in parallel or at the same time?

Is there any risk for this technique on future analysis due to sample degradation for instance?

l92: "based on visual impression" -> Sounds not scientific. Have the data been analyzed by a pathologist for assessment? Is that how it is done by pathologist?

l93: "automated image processing". Partially true, one still need to spend some times for doing manual segmentation. In the document nothing is mentioned about the quantity of images necessary for this process neither.

Figure 1: Later in the paper, the authors are describing the 3 methods used for the analysis as "LJ setup", "PB configuration", "WG configuration". First for clarity I would choose either setup either configuration. Then, I would also introduce those names in the figure or at least in the legend.

(B) -> "from one of the control and one of the Covid-19 samples". Otherwise it's misleading and difficult to understand that only one of each has been analyzed. How the choice actually has been made between the samples?

(D) plane of 3x3. Why 3x3 and not larger or smaller? Would a 360 or half scans be able to cover the interesting part of the biopsy that is in the end analyzes ? (i.e. to avoid the cropping due to the holder)?

(E) "was taken from a control sample". The analysis have been done on a COVID-19 sample as well, no?

Appendix Figure 1: The figure of the Haematoxylin and Eosin staining presents images too pink and no details of the microstructures can be really seen. Are those slices corresponding exactly to the samples before the biopsy punch? Have they been compared to slices for all samples on the X-ray datasets?

l113: "Biopsy punches". How the areas have been selected? Why the amount of biopsy punch are not identical for all samples? i.e. why not taking the entire block or selecting 2 samples per patients as for the CTRL?

l117: "one (Ctr) biopsy". One control and one COVID-19 are presented.

l123: It would be nice to have the source size of the liquid jet as well as the corresponding magnification factor. Where the broad spectrum used or only 9.25 keV? What is the true resolution compare to the pixel size?

l132: The measurement have been done at a different energy. What is the impact of such changes on the results? Would a higher energy be interesting?

l136: "the continuous scan mode". This is the property of the rotation stage I guess, and not the reason of being able to perform 3x3 tomography scans. Isn't it more a question of speed and stability of the stages? Have the scan been perform over 180 degrees?

l137: "dark field images were taken" I guess that flat field as well?

l138: "150 tomographic scans were recorded". It's not clear that this is for the entire amount of samples (with 3x3 for each).

l141: "1mm diameter biopsy punch". How this has been performed? Seems very tricky to extract 1mm rod from the 3.5mm one. How the area has been chosen. Was the height of the sample the same?

l139-153. It was not clear for me from the beginning that the 2 samples have been analyzed in 2 different configuration of the setup. A sentence introducing and explaining this would be helpful.

Table2: the source sample distance is missing for the PB configuration. Why the number of projections in the case of the PB configuration is the double than the 2 other configuration. Why the amount of empties/dark field so large? Empties is not the common name used in the field. Usually the term "flats" is preferred.

What means the acquisition time 3x0.6?

It would be interesting to give the total scan time for each technique.

l156: "local median filtering"

As the authors are using different phase contrast techniques for their analysis, a short introduction and a clearer organization of this paragraph would help in the comprehension for non-specialist. Some references could also be added. It is not easy to follow the difference between the reconstruction and phase retrieval techniques used for each technique.

l177: "datasets were binned by a factor of 2".

Tomographic datasets can indeed become very heavy, specially after stitching. However, here the purpose of using synchrotron is to reach higher resolution and higher throughput than in laboratory. When binning the data, the pixel size / resolution is also reduced. Therefore leading to a similar pixel size than in laboratory. Have the analysis be computed on the binned data or on the full datasets?

Table3: 1/ The d/b ratio values are real values of δ/β or just the result of the ratio? 2/ One can not understand what are the parameters.

l183: "corrupted datasets" What was the issues here? Need clarifications.

l197: "32 pixels for PB datasets" If the analysis has been done on binned data, it would lead to different size compare to the 12 pixels for the LJ acquisitions?

"A smoothing parameter of 2 pixels" It would be nice to have more explanation here. Have this been applied to both PB and LJ datasets?

l213: "the paraffin surrounding" Why the mask has been applied only on the LJ datasets. Isn't it included as well in the acquisition of the PB datasets?

l214: "Since one axis of the shape measure is redundant" Could the author clarify this point?

l231: "A small number of axis-aligned 2D slices was annotated". It would be very interesting to know the amount of annotated datasets that have been necessary to perform the analysis. Indeed, this is the most critical point when performing machine learning technique. Sparsely annotated data sets is a very promising technique, specially for analysing large amount of images. What was the percentage of images of annotated volumes were kept for training / validation?

l236: Why 96x96x96 voxels? What was the total size of the datasets?

l239 "256 subvolumes" How is this amount representative of the entire datasets?

l243: "A separate model" why was it necessary? Doesn't it create bias in the results?

l247: "adding additional annotations" Do I understand correctly that the analysis is run a first time, then the authors look at the images and visually correct some of them and re-run the analysis?

l314: "different areas of the same heart" How those areas have been chosen. Why 3 samples per patients?

l323: "dark stripes" In the figure it's easy to distinguish white stripes, but not the dark ones. Maybe small areas or markers would help to follow the description.

l329 / Figure 3: How to make the difference between paraffin cracks and inclusion compare to other features?

l337: "samples near an artery". How the areas have been chosen and what is the impact on the results presented?

l360: Appendix 1 Figure 2: would be nice to have arrows in the figure to understand what is erythrocytes and capillaries.

l368: "340x340x340um3": Why this size has been chosen and not the entire volume?

l371: "cytosol" would be nice to have this indicated in the figure.

l375: "nucleus" It seems that we can see only on in the figure. Do we see others in the 3D volume?

l386: "speeding-up the measurement sequence" It would be interesting to indeed grasp the difficulties of such measurement and time necessary.

Table 4: mean shape mu_p and mu_s are of the same order (ctrl or diseased) for mu_l there is a difference between control versus diseased however the σ is pretty large (almost 30% in certain case). Similar remarks for the elliptical fit (54% for σ in the case of Control…). The Authors are aware and found an interesting way of representing the results (Figure 5A). However, can the authors comments on why the errors are so huge, and how can one conclude in term of differences according to those results? Because even on the graph, we see tendency but to make strong concluding statement is difficult. I would therefore modify part of the eluding sentence in this direction.

Maybe could they compare with histology analysis conclude beforehand to help in the understanding.

l403: Authors are aware that their methods have some limitation. For instance "depend on tissue preservation and preparations".

l419: Welch t-test: Would be good to have a reference an explanation sentence.

l427: "Surface rendering" from which acquisition? Would be nice also to refer to the corresponding method paragraph.

l438: Could the authors explains a bit more what is the probability density function and how it is obtained. Figure 6E: The authors state clearly that their is a higher amount of branching points in the Covid19 sample. However, this is the results on one sample and the figure is not clearly stating that. For instance for 5 vertex degree the control seems superior than the covid.

l449: "first report" What about Walsch 2021?

l465: "non-destructively". It's not totally non-destructive technique as one still need to make a biopsy punch on the blocks.

l470: "conventional histopathology assessment" It would be nice to have a reference on the histology conventional analysis are adding in supplementary material correlation between X-ray images and histology images.

Figure 5: how those 2 samples have been chosen compare to the previous selection.

l493: "volume throughput of 10ˆ7 um3 /s. Maybe a simpler presentation would be more meaningful for the general audience, like acquisition time for one sample with which setup.

l497: rather than by photon flux: This is valid for the synchrotron acquisition I guess. But then what would be the purpose of the new synchrotron source if the flux is already not fully exploited? Same question concerning the following sentence about the attenuators used to prevent detector saturation. What about dose on the sample then?

l500: why so huge acquisition time range 200ms to 2500ms?

Appendix 1 Figure 3: In all the images we see like a cross in the images creating a white blur. Can the authors comment on that? Specially because grey levels are used for the analysis. How this effect can affect the results? A comment should also be added for the square missing (i.e. areas for corrupted files). Why measurements have not be redone locally?

Reviewer #2 (Recommendations for the authors):

It would be important to improve the samples' statistics.

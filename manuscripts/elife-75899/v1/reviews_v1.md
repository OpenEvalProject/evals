# Peer review - Round 1

Editors:
- Ruben L Gonzalez, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75899.sa0](https://doi.org/10.7554/eLife.75899.sa0)

This is a valuable paper that reports an open-source platform for the storage and processing of single-molecule, camera-based, imaging data. The development and testing of the platform are very compelling and the platform will facilitate data sharing and reproducibility and will be of great interest to practitioners of single-molecule imaging experiments, both experienced and new to the field. The work represents significant and important steps towards unifying and standardizing how the field stores and processes data and expanding the base of researchers who can easily employ single-molecule imaging methods.


---

# Peer review - Round 1

Editors:
- Ruben L Gonzalez, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75899.sa1](https://doi.org/10.7554/eLife.75899.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mars, a molecule archive suite for reproducible analysis and reporting of single molecule properties from bioimages" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Ruben Gonzalez as the Reviewing Editor and Volker Dötsch as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Eitan Lerner (Reviewer #1); Jingyi Fei (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors should further develop the Mars platform to: (i) expand the flexibility of the smFRET input data files in the manner described by Reviewer 2 and, if necessary, to do the same for the other various types of data files (e.g., single-molecule force-extension data from laser tweezer data, particle tracking data from DNA curtain experiments, etc.) and (ii) include validation information/reports of the kind described by Reviewer 1.

2) The authors should comprehensively test and troubleshoot all of the functions of the platform using different computers and operating systems to ensure the robust performance of the platform. Reviewer 2 and her student have kindly provided a detailed, but not exhaustive, list of technical problems that they encountered and that should be resolved.

3) The sample dataset of smFRET trajectories from Hellenkamp et al., (2017) that is analyzed for the work reported in this manuscript is limited in the sense that the trajectories do not exhibit transitions between different FRET efficiency states as a function of time. Given that the majority of smFRET studies typically contain trajectories that do exhibit such transitions, it is important that the authors include a second sample dataset of smFRET trajectories that do exhibit such transitions as a function of time. The authors are encouraged to analyze an already existing dataset from their own laboratory or a collaborator's laboratory or, if that is somehow not possible, to record such a dataset de novo. When adding these new analyses and revising the smFRET section of the manuscript, the authors should take care to also address Reviewer 1's comments regarding the smFRET example(s).

4) The authors should revise the manuscript to include: (i) a beginners-level, practical discussion of why a platform such as Mars is needed to increase the reproducibility of data storage and processing practices (including examples of real-world problems that Mars would address, minimize, or eliminate) and (ii) an easy-to-follow, brief guide explaining the use of Mars within the manuscript aimed at readers who may not necessarily be ready to use the platform or the associated Jupyter notebooks and/or interactive features of the website.

5) The step-by-step instructions for using Mars that are included on the website should be expanded to include further details, particularly in terms of the output files, as well as to include a general troubleshooting guide for users.

Reviewer #1 (Recommendations for the authors):

This report constitutes the review of the manuscript titled "Mars, a molecule archive suite for reproducible analysis and reporting of single molecule properties from bioimages", by Huisjes, Retzer et al. With the ever increasing interest in these techniques, accompanied by ever increasing experimental schemes and analytical frameworks it becomes difficult to report such experimental results in a manner that is universal, one which can adapt to any type of experiment and analysis, one which assists in reproducibility, and one which will keep the data as compact as possible, yet its usage as efficient as possible. This work introduces a novel platform for the reproducible archiving of camera-based single-molecule imaging experiments. This work will appeal to practitioners of single-molecule imaging experiments, both experienced and newbies. The readers of this work would benefit from understanding how to employ a rational data archiving process using Mars, following three examples the authors provide, which exhibit the generality of the platform and its ease of use. Readers who might want to employ Mars for their own single-molecule imaging measurements can also experience an intuitive guide on Mars GitHub or in Jupyter Notebooks the authors provide. However, I believe that it would even be better if the authors could provide a guidance chapter in the manuscript itself, in addition and before sending the readers to the guide online – this way, readers would already have an idea of what to expect when they try constructing their own Mars data archiving.

I judge that to the most part, the manuscript shows concisely and clearly how to use Mars for proper archiving of single-molecule imaging data, in a rational manner, that can be easily read, well understood, without loss of information and with the ability to easily track back and perform changes. The manuscript is very well polished, the figures provide a self-explanatory graphical guide – overall I enjoyed reading it and see how much this tool can advance the field. The importance of this work is very clear to experienced practitioners, who already know what it takes to provide extensive reports on their results, after being analyzed, corrected, filtered and analyzed in one combination of ways out of many others. Although I am very positive about this manuscript, I have a few suggestions for the authors:

1. Readers of the manuscript who are not yet experienced with single-molecule imaging could benefit from a pragmatical discussion that will explain the need for Mars for reproducibility and/or readability of the data: the different types of filtrations a practitioner may perform, all are context dependent, and what might happen if those are not properly documented and annotated. I suggest providing user examples of what might go wrong, and how Mars minimizes such cases.

2. The authors provide a very nice interactive as well as notebook guidance for readers of the manuscript who might want to get acquainted with Mars. However, I think readers of the manuscript would benefit from such a guide already in the manuscript, which will assist them in understanding what to expect when they move to try using Mars. This way, readers who are not yet ready to test Mars, would already be able to follow the guide in text, and then decide if they move to test Mars in action for their datasets.

3. The analysis pipeline provides a nice abstraction all the way from the raw data to the filtered information. However, another layer of validation should be added afterwards. For example, procedures that test all the filtered smFRET data for features that should exist in the data: (1) sum of all donor-excited signals should be constant after corrections were applied; (2) sum of all intensities should be constant, after corrections were applied, (3) transitions between states (FRET dynamics, or photobleaching) should exhibit donor and acceptor anti-correlation; (4) transitions between Stoichiometry states should exhibit donor and acceptor anti-correlation. Adding a filtered data validation procedure will enhance the procedure even better, and provide another layer of credibility, perhaps even in an automated report as an outcome of the validation step applied on all molecules.

4. Comments on the smFRET example:

a. The authors chose to show the TIRF camera-based smFRET data from Hellenkamp et al., (2017), of a static mixture of two DNA FRET constructs with two different mean FRET efficiencies. The procedure they describe was designed to fit the treatment of the static mixture of two types of immobilized molecules. Therefore, the analysis pipeline employed the change point finder only for the identification of photo-bleaching steps, and not for identifying dynamic FRET transitions. While this might be fine for the static heterogeneity of this sample, for the analysis framework to be as generic as possible for analyzing smFRET measurements, it is important to include a step of identification of state dwells within each single molecule FRET trajectory. Importantly, the FRET calculations should be performed on dwells that have been proven to belong to a single state.

b. The analysis pipeline was designed to filter out traces with large intensity changes that are not due to photo-bleaching. Large intensity changes might be interesting if one of the FRET dyes experiences quantum-yield changes that are unrelated to FRET (e.g., smFRET involving Cy3 and Cy5). It could be interesting in the proper context, and hence should allow the user to change the data rejection criteria, in a context-dependent manner.

c. Correction factors 1: the text relies on the correction factors presented by the multi-lab work of Hellenkamp et al., (2017). That approach uses the Lee et al., (2005) approach for calculating the γ correction factor, which relies on the linear dependence of the inverse of the mean stoichiometry on the mean proximity ratio, of multiple single-population smFRET-ALEX measurements. While this correction factor procedure is used by many and is very common, it does suffer from assuming that both donor and acceptor fluorescence quantum yields change in the same manner when positioning the same donor and acceptor dyes at different positions along the same molecule (a dsDNA in this case). This might not be true, as different abelling positions introduce different dye microenvironments, which may introduce different quenching rates that are unrelated to FRET. In other words, it is possible (and not uncommon at all) that different molecules with different FRET values will also be associated with different γ factors. There are alternatives that can assist in calculating per-population γ factors, which require knowledge of the donor and acceptor fluorescence lifetimes per population. However, this is not yet possible in immobilized TIRF camera-based smFRET. Therefore, in page 10 of the bioRxiv preprint, when the authors present the γ correction factor, I suggest they add: “… , under the assumption that placing the same dyes at different bases along the DNA molecule does not influence the ratio of the acceptor and donor fluorescence quantum yields”.

d. Correction factors 2: the text relies on the correction factors presented by the multi-lab work of Hellenkamp et al., (2017). That approach uses the Lee et al., (2005) approach for calculating the γ correction factor. However, Hellenkamp et al., (2017) and not Lee et al., (2005) is cited. I ask the authors to cite Lee et al., (2005), when providing the explanation on the β- and γ-factor calculations.

e. When explaining the FRET-related calculations, sometimes the variables are not explained: (i) in steps 4 and 5, explicitly explain the readers what are FA|A and FD|D; (ii) "FA|D stores the fully corrected acceptor fluorescence intensity value"; (iii) explain for FRET novices what do the variables in equations 1 and 2 mean.

f. At the bottom of page 6 of the bioRxiv preprint, the authors provide their estimations of the FRET efficiency values, and it seems that the accuracy is high, if comparing the values to the mean values reported by Hellenkamp et al., (2017). However, the precision of the reported values (E1-lo = 0.14 {plus minus} 0.13 and E1-mid = 0.51 {plus minus} 0.09) are low compared to the precisions in Hellenlamp et al., (E1-lo = 0.15 {plus minus} 0.02 and E1-mid = 0.56 {plus minus} 0.03). Why such imprecisions? Please explain the readers in the text.

Reviewer #2 (Recommendations for the authors):

Technical issues encountered:

1. Overall the step-wise tutorial on the website is well organized, but can be further improved. Particularly, the expected results/output files/windows should also be included, similar as the parameter setting for the input part. Sometimes it’s unclear what the correct output format should be from each operation.

2. We noticed Mac and Windows systems could encounter different issues. Taking the FRET analysis as an example, we had to switch between the Windows and Mac systems to get it through completely, because certain steps worked in one but not the other. For example:

(1) When we tried to convert the example FRET video to contain channel information using script 1, the Windows system generated a blank image. However, it ran correctly on Mac.

(2) There was some problem with transforming the ROIs to the right part of the split view on a Mac system. We used the same parameters as the instruction, but all the coordinates disappeared after doing Transform ROIs. But it worked well on a windows system.

(3) On a Mac system, after running peak tracer or molecular integrator, we were not able to generate a GUI interface containing the actual output, but a console saying the analysis is successful.

3. It’s very confusing that the output file of the converted FRET data is a composite image of two channels. It is not explained what each of the channels is until explaining the output file of the molecular integrator step. Echoing my point 1, it is necessary to explain to the users the f’rmat of the output files. The composite image makes it appear that two channels are the s’me without any explanation, and each channel is the sum of the red and green signal.

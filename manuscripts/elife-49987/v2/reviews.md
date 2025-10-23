# Peer review - Round 1

Editors:
- Megan R Carey, Champalimaud Foundation Portugal

Reviewers:
- Denise J Cai, Mount Sinai School of Medicine United States

## Review text

DOI: [10.7554/eLife.49987.sa1](https://doi.org/10.7554/eLife.49987.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers and editors appreciated the versatility and practical usability of the openly available NINscope system. Compared to other systems, NINscope incorporates advantages in weight and size that allow for coupling with accelerometers, optogenetic stimulation, and the possibility for dual site imaging. Together, these open up broader possibilities than exist with other systems. Because it is being made openly available, we expect this system will be a particularly useful addition for labs that don't have the ability to develop these additional features on their own through modification of existing systems.

Decision letter after peer review:

Thank you for submitting your article "NINscope: a versatile miniscope for multi-region circuit investigations" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Denise J Cai (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Your paper generated quite a lot of discussion in the consultation phase. On the one hand, the reviewers felt that the individual technical advances here were relatively small. On the other hand, there was agreement that in principle, the small advantages in weight and size, although incremental individually, when coupled with accelerometers, optogenetic stimulation, and possibility for dual site imaging, could together open up broader possibilities than exist with other systems. The main advance of the NINscope was seen as potentially residing in versatility and practical usability rather than in technical specs per se – highlighting HOW to combine imaging with this smaller footprint with other applications (opto, dual imaging) is a nice contribution. If this system were made openly available, it might be a useful addition for labs that don't have the ability to develop these additional features on their own through modification of existing systems.

As a Tools and Resources article, there is no requirement to report major new biological insights or mechanisms, but it must be clear that they will enable such advances to take place. Since the goal here is not to answer biological questions, it needs to be made more clear that the experiments are proof-of-principle (i.e. the scope and associate technology works) demonstration experiments AND the data need to be high quality.

Key issues were raised that would need to be addressed to conclusively demonstrate these points, summarized here:

1) Most importantly, there are concerns about the quality of the imaging data as represented in the supplemental videos, including apparent z-axis motion artifact, deconvolution of GCaMP signals, and Purkinje cell dendrite segmentation (touched on in varying ways by all 3 reviewers, but especially reviewer 3). The videos are also highly processed, with red flashes indicating activity, obscuring the segmentation and signal extraction. To ensure that the smaller footprint of the NINscope does not sacrifice stability and image quality, we ask you to:

– Provide YFP (or other static fluorophore) controls for motion artifacts. This is particularly (but not only) relevant for the instances of increased activity across regions that correlates with head acceleration.

– Provide more raw data and information about segmentation. In the videos, please provide the same data calcium imaging data in raw form, after motion correction, and then again after segmentation. This could be done by showing the same video for these three steps.

2) There was concern that too much is being made in terms of biological findings resulting from the disparate proof-of-principle experiments that are shown. Those studies were seen as underpowered, lacking experimental detail and lacking control experiments to make strong biological conclusions. Moreover, answering all these biological questions in detail is outside the scope of the tools and resource paper. Please focus on the tools and methods aspects (and explicate on that) and temper the conclusions on findings of coordinated neural activity across brain regions.

3) To validate the utility of mounting 2 scopes, in behaving animals please provide

– more revealing images of the dual mounted configuration (as reviewer 1 suggested)

– quantification of behavior with 0,1,2 scopes mounted (suggested by reviewer 2).

4) To enable straightforward evaluation of the specs of NINscope compared with other existing options (UCLA miniscope, Inscopix), please include a comparison table as suggested by reviewer 2.

5) Please provide validation of the true decoupling of stimulation and recording site for optogenetics (Reviewer 3 point 2).

We therefore invite you to submit a revised manuscript that fully addresses these concerns, as well as the full set of reviewers' comments, below.

Reviewer #1:

Groot et al. report the design and application of a novel miniscope – NINscope – whose primary advance over existing miniscope technologies is its small and light-weight nature, which allows implantation of two of them for simultaneous imaging across two brain regions in mice. Further, NINscope is capable of integration with optogenetics, for concurrent imaging and optogenetic manipulation of brain circuits. The authors demonstrate that NINscope is capable of acquiring high resolution videos whose underlying neural activity can be deconvolved using conventional data processing techniques (i.e. CNMF). They then discover synchronous activity patterns (SPs) across cortex and cerebellum during onset of motion, using NINscope to record across the two regions and an integrated accelerometer to measure behavioral motion. To demonstrate that NINscope is amenable to integration with optogenetics, the authors then image cortical calcium activity while stimulating Purkinje cells of 4 cerebellar subregions and show that stimulation of each subregion increases cortical calcium activity. Moreover, assessment of behavioral acceleration suggests that stimulation of one hemisphere of Crus II leads to head movement in the opposite direction. To demonstrate NINscope's capacity to image from deep brain structures, the authors implanted a GRIN lens in the dorsal striatum using a relay lens system and recorded striatal neuron calcium activity as mice explored an open field. Using this system, the authors observe individual neurons tuned to turns in the direction opposite the recorded hemisphere. Finally, the authors use deep brain imaging and optogenetics to demonstrate that optogenetic stimulation of OFC and M2 differentially influence striatal neuronal activity. Overall, NINscope serves as a valuable and flexible tool that allows investigation of neuronal population dynamics across brain regions. Because of its small footprint, it allows for flexible use such as combining it with additional NINscope or optogenetics. This tool will surely benefit the neuroscience community broadly, however, some additional details of methodology and clarification of certain areas (addressed below) would improve this manuscript greatly. And while it is commendable that the authors show several examples of how NINscope can be used experimentally, it is unclear what the biological discovery is across these different experiments which seem to be tackling disparate research questions. The authors may want to more clearly state what the hypotheses are based on prior research and what findings are consistent with prior research and which are novel or challenge prior views. I understand this may increase the scope of this paper too broadly, which I would like to suggest that the authors consider focusing their experimental questions.

Reviewer #2:

de Groot et al. present a new open-source miniature fluorescent microscope. In direct comparison to the most widely used miniature fluorescent microscopes, the new scope (dubbed NINscope) has a few additional features/properties that will make it appealing for some groups to adopt. In particular, the NINscope has a smaller footprint, is lighter, and contains on-board accelerometers and LED drivers to control external LEDs. These features are well-integrated into the design and their utility is demonstrated in the manuscript. To demonstrate functionality of this new microscope and its associated hardware and software, the authors confirmed multiple previous findings from the movement literature. Namely, the authors use NINscope to successfully track activity of purkinje cell dendrites and dorsal striatum neurons during movement, to examine functional connectivity between cerebellum and cortex, and to confirm findings that orbitofrontal and motor cortex provide top-down control of dorsal striatum. In my eyes, the primary deliverable of this paper is the microscope itself and very little more is needed to demonstrate its function and utility. Some modifications, however, would strengthen the dissemination of relevant information about the NINscope. The neurobiological experiments are perhaps underpowered, but not in a way that undermines the microscope itself. For example, the known limitations of detecting a decrease in signal from GCaMP, might provide some bias in Figure 6, but this possibility is not detracting from the technical advances made here.

One addition that would strengthen this manuscript is a more detailed comparison between the NINscope and other open-source (maybe commercial too when applicable) miniature microscopes. This could be in the form of text or figure, but a comprehensive table might be the most succinct manner of conveying information that would inform future users. I recognize that the last author has a review on this topic, but that review does not capture the NINscope itself or much detail on the wire-free scope from Shuman et al. (bioRxiv, 2018). Direct comparisons of weight, footprint size, control schemes, focusing mechanism, software considerations, accessory hardware, and stimulation ability are just some of the variables/limitations that might sway a user from one scope to another.

The other main comparison that would strengthen claims made about the scope hardware itself (should be gathered easily or from existing data) is a quantified comparison of locomotor behavior with zero, one, and two NINscopes headmounted. The authors suggest normal behavior is seen and refer to cage exploration, grooming, eating, and rearing, but these are not actually demonstrated. Rearing epoch is defined by video and IMU data in 2G, presumably number of rears could be collected from one- and two-scope setups and compared.

Including more information about the LEDs for optical stimulation would be helpful. These appear to be very simple applications of standard LEDs and it might be useful for others to employ these with or without the NINscope. Supplementary photos and/or diagrams of these would help.

Light power for imaging was not reported for Figure 6. Was it the same as Figure 5? Due to the possibility of activating the blue tail of ChrimsonR, please include this information.

Reviewer #3:

In this manuscript by de Groot et al., the authors develop and characterize a miniature epifluorecent microscope to be used in freely behaving rodents for calcium imaging. The microscope is similar to previously published miniscopes (UCLA miniscope, Inscopix nVista, and the Finchscope) with a few minor differences. Namely, it is slightly lighter than the Inscopix scope, and contains and accelerometer/LED for positional tracking. It also has an extra LED that can be used for photostimulation. While other systems do not offer this, it seems like it would be easily implemented with other systems if needed.

Specific comments:

1) One of the major points made throughout the manuscript is that this system permits for multisite recording. While this is demonstrated in the cerebellum and frontal cortex, it is unlikely this could be achieved in many other regions. The frontal cortex and cerebellum are quite far apart (thus while it is feasible in this example), but this will be highly limited to other duel sites.

2) The optogenetic stimulation coupled with imaging is interesting, and has been previously reported using the Inscopix nVoke system (where stimulation and recording occur in the same field of view). The advantage in this paper is that stimulation can be decoupled from the recording site. While this is interesting, it does not appear that control experiments where mice were not expressing ChR2 were performed. Thus, it is possible that neural activity evoked by stimulation could be due to some sort of heating or light induced artifact.

3) I have some concerns with the data quality presented in the supplementary videos. Many of them show non-correctable z-motion artifact, and the cerebellar dendritic recordings seem to show a lot of out of focus fluorescence which will make it difficult to extract signals from single dendrites. The authors used the recently published CMNF-E algorithm for signal extraction, which is extracting something from the data, but it is unclear whether extracted signals actually represent bona vide single dendrites.

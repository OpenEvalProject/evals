# Author response - Round 1

Authors:
- Andres de Groot
- Bastijn JG van den Boom ([ORCID: 0000-0002-0853-3763](https://orcid.org/0000-0002-0853-3763))
- Romano M van Genderen
- Joris Coppens
- John van Veldhuijzen
- Joop Bos
- Hugo Hoedemaker
- Mario Negrello ([ORCID: 0000-0002-8527-4259](https://orcid.org/0000-0002-8527-4259))
- Ingo Willuhn ([ORCID: 0000-0001-6540-6894](https://orcid.org/0000-0001-6540-6894))
- Chris I De Zeeuw ([ORCID: 0000-0001-5628-8187](https://orcid.org/0000-0001-5628-8187))
- Tycho M Hoogland ([ORCID: 0000-0002-7444-9279](https://orcid.org/0000-0002-7444-9279))

## Response text

DOI: [10.7554/eLife.49987.sa2](https://doi.org/10.7554/eLife.49987.sa2)

Reviewer #1:

[…] Overall, NINscope serves as a valuable and flexible tool that allows investigation of neuronal population dynamics across brain regions. Because of its small footprint, it allows for flexible use such as combining it with additional NINscope or optogenetics. This tool will surely benefit the neuroscience community broadly, however, some additional details of methodology and clarification of certain areas (addressed below) would improve this manuscript greatly. And while it is commendable that the authors show several examples of how NINscope can be used experimentally, it is unclear what the biological discovery is across these different experiments which seem to be tackling disparate research questions. The authors may want to more clearly state what the hypotheses are based on prior research and what findings are consistent with prior research and which are novel or challenge prior views. I understand this may increase the scope of this paper too broadly, which I would like to suggest that the authors consider focusing their experimental questions.

We thank the reviewer for their time to carefully read through our manuscript, valuable suggestions to improve it, and overall positive assessment. We agree with the conclusion that the experiments demonstrated are not necessarily connected with an overarching hypothesis, but our goal for this Tools and Resources manuscript was above all to show NINscope’s versatility and applicability, which has led to a disparate set of experiments. Acknowledging the above, we have now toned down the conclusions drawn with regard to the biological findings.

Reviewer #2:

[…] Some modifications, however, would strengthen the dissemination of relevant information about the NINscope. The neurobiological experiments are perhaps underpowered, but not in a way that undermines the microscope itself. For example, the known limitations of detecting a decrease in signal from GCaMP, might provide some bias in Figure 6, but this possibility is not detracting from the technical advances made here.

One addition that would strengthen this manuscript is a more detailed comparison between the NINscope and other open-source (maybe commercial too when applicable) miniature microscopes. This could be in the form of text or figure, but a comprehensive table might be the most succinct manner of conveying information that would inform future users. I recognize that the last author has a review on this topic, but that review does not capture the NINscope itself or much detail on the wire-free scope from Shuman et al. (bioRxiv, 2018). Direct comparisons of weight, footprint size, control schemes, focusing mechanism, software considerations, accessory hardware, and stimulation ability are just some of the variables/limitations that might sway a user from one scope to another.

Thank you for this suggestion. We have added a Table in which we compare NINscope to other currently available miniscopes (open-source and commercial).

The other main comparison that would strengthen claims made about the scope hardware itself (should be gathered easily or from existing data) is a quantified comparison of locomotor behavior with zero, one, and two NINscopes headmounted. The authors suggest normal behavior is seen and refer to cage exploration, grooming, eating, and rearing, but these are not actually demonstrated. Rearing epoch is defined by video and IMU data in 2G, presumably number of rears could be collected from one- and two-scope setups and compared.

Including more information about the LEDs for optical stimulation would be helpful. These appear to be very simple applications of standard LEDs and it might be useful for others to employ these with or without the NINscope. Supplementary photos and/or diagrams of these would help.

This is an excellent suggestion. Per the reviewer’s suggestion we have quantified the number of rearings in mice wearing single and dual miniscopes (CBL-CTX configuration) for 4 mice. We find that rearing frequency and duration is unaffected by adding an additional miniscope.

We have updated Figure 1 in that we now include a separate panel (1D) to show the LED probe we built to use in combination with NINscope, and added a short paragraph to the text describing its parts. The assembly of probes is described in detail on our GitHub hardware wiki: https://github.com/ninscope/Hardware/wiki/8.-LED-probe.

Light power for imaging was not reported for Figure 6. Was it the same as Figure 5? Due to the possibility of activating the blue tail of ChrimsonR, please include this information.

We added the information on light power as requested. The reviewer raises a valid point about the possibility that ChrimsonR could be activated by blue light. We believe activation of the blue (excitation) tail of the ChrimsonR is likely mitigated by the following factors:

1) The light power used for striatal imaging as measured under the GRIN relay lens -now reported in Figure 2—figure supplement 1 corresponds to about 170 µW. This light power is more than an order of magnitude lower than the light power of the red LED used to stimulate the OFC and M2 in cortex.

2) We performed these experiments four weeks post-injection when terminal expression of ChrimsonR is still relatively weak.

3) Even if blue light excites terminals expressing ChrimsonR we still observe a differential postsynaptic response upon stimulation of M2 and OFC.

Reviewer #3:

In this manuscript by de Groot et al., the authors develop and characterize a miniature epifluorecent microscope to be used in freely behaving rodents for calcium imaging. The microscope is similar to previously published miniscopes (UCLA miniscope, Inscopix nVista, and the Finchscope) with a few minor differences. Namely, it is slightly lighter than the Inscopix scope, and contains and accelerometer/LED for positional tracking. It also has an extra LED that can be used for photostimulation. While other systems do not offer this, it seems like it would be easily implemented with other systems if needed.

The points made above highlight that perhaps we should have been more explicit about the effort that goes into designing and building integrated circuit boards to allow in-software control of all aspects of the experimental recordings. We designed and built two compact integrated circuit boards for NINscope while reducing the miniscope weight, integrating an accelerometer, adding dual-site imaging capabilities and permitting optogenetic stimulation.

Adding functionality by way of separate components, would add unnecessary weight or cables, which might impact animal behavior and above all would require time-consuming steps to ensure post-hoc data synchronization. Even if these features could be added it would require specific technical skills that not everyone has access to.

We believe that by sharing this resource as an open-source tool we can ensure that a larger group of users can benefit from its specific features and allow them to address novel research questions.

Specific comments:

1) One of the major points made throughout the manuscript is that this system permits for multisite recording. While this is demonstrated in the cerebellum and frontal cortex, it is unlikely this could be achieved in many other regions. The frontal cortex and cerebellum are quite far apart (thus while it is feasible in this example), but this will be highly limited to other duel sites.

Thank you for pointing this out. In order to more clearly demonstrate the suitability of NINscope for multi-site recordings, we now demonstrate additional dual scope configurations in Figure 3—figure supplements 1 and 2, including bi-hemispheric imaging from somatosensory and visual cortex, hippocampus, or two cerebellar hemispheres.

2) The optogenetic stimulation coupled with imaging is interesting, and has been previously reported using the Inscopix nVoke system (where stimulation and recording occur in the same field of view). The advantage in this paper is that stimulation can be decoupled from the recording site. While this is interesting, it does not appear that control experiments where mice were not expressing ChR2 were performed. Thus, it is possible that neural activity evoked by stimulation could be due to some sort of heating or light induced artifact.

We now include Figure 4—figure supplement 1, which demonstrates that stimulation at multiple cerebellar locations neither triggers a response in neurons of cortex nor a behavioral response.

3) I have some concerns with the data quality presented in the supplementary videos. Many of them show non-correctable z-motion artifact, and the cerebellar dendritic recordings seem to show a lot of out of focus fluorescence which will make it difficult to extract signals from single dendrites. The authors used the recently published CMNF-E algorithm for signal extraction, which is extracting something from the data, but it is unclear whether extracted signals actually represent bona vide single dendrites.

We agree with the reviewer that the visualization in the videos as presented was unclear. The red flashes represented mean-subtracted raw fluorescence superimposed on the raw data and the videos were saved in a compressed format, which did not clearly represent the data. We therefore now provide higher quality supplemental videos that include the step-by-step process from raw data to motion correction to segmentation throughout the manuscript. These videos in combination with dual miniscope experiments in which we injected fluorescent beads into cerebellum and cortex reveal that motion artefacts are actually fairly modest.

To show that CNMF-E can successfully segment Purkinje cell dendrites we have updated Figure 2 and other figures to show the extracted spatial footprints. Our spatial footprints of Purkinje cell dendrites meet the criteria of parasagittally aligned elongated structures and the extracted signals match what we expect from complex spike evoked calcium transients having firing rates of around 1Hz. Moreover, given the anatomy of the cerebellum and the fact that we are imaging from the surface of the cerebellar cortex in combination with Purkinje cell selective transduction of GCaMP6f we are confident that we are reporting signals from individual Purkinje cell dendrites.

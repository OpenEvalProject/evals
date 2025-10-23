# Peer review - Round 1

Editors:
- Elena A Levashina, Max Planck Institute for Infection Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56829.sa1](https://doi.org/10.7554/eLife.56829.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript is of great importance to the field as it represents an important technical advance that will support further studies of mosquito biting and disease-transmitting behavior. By combining image-based tracking, computer vision algorithms, and deep learning, the authors quantify the parameters which are of high relevance to future studies of the neurobiology controlling mosquito blood-feeding and, hence, transmission of human pathogens.

Decision letter after peer review:

Thank you for submitting your article "BiteOscope, an open platform to study mosquito blood-feeding behavior" for consideration by eLife. Your article has been reviewed by Dominique Soldati-Favre as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Carlos Ribeiro (Reviewer #2); Philip McCall (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The manuscript describes an experimental framework for studying female mosquito foraging and feeding behavior. By combining previously established stimuli promoting female feeding behavior, with image-based tracking, computer vision algorithms, and deep learning, the setup is able to record trajectories from multiple mosquitos within an acrylic box containing an area that contains an artificial meal which the mosquitos can reach by piercing a parafilm membrane. The authors provide data allowing them to quantify different parameters which are of high relevance to future studies of the neurobiology controlling mosquito blood-feeding and hence the potential transfer of pathogens. As proof of principle, they explore the impact of DEET on An. coluzzii behavior, which leads them to suggest that chemosensory neurons in the legs but not the proboscis are required for the deterring effect of DEET.

This manuscript is of great importance to the field as it represents an important technical advance that will support further studies of mosquito blood-feeding, a disease-transmitting behavior. The method is super useful, but the technical description and the discussion of the data is a bit superficial. Also, the method is limited to clear liquids, this technical limitation that is difficult to overcome and as such should be acknowledged and discussed in the manuscript. While the different aspects of the method are not novel on their own, the experimental framework is intriguing both in terms of the technical aspects as well as the potential to other researchers in the field. Importantly, the authors make the hardware design as well as the software openly available. The manuscript is well written and concise. However, the reviewers raised some major concerns that will need to be addressed.

The Title:

The mention of blood-feeding in the title is misleading. It should reflect the experimental setup. Therefore, blood-feeding should be replaced by feeding. Temperature is not a good proxy for blood.

Essential revisions:

1) The authors have completely avoided a large literature on the difference between the effects of DEET alone versus DEET and human odor. The authors need to review the literature on this topic more thoroughly and address their interpretation of their data. There is substantial data suggesting that DEET cannot repel mosquitoes in the vapor phase without human odor or other attractive odors. For a review on the topic, the authors should read "The mysterious multi-modal repellency of DEET" (https://doi.org/10.1080/19336934.2015.1079360). It is also untrue that there is evidence presented that Aedes aegypti mosquitoes can sense DEET without human odor in the vapor phase in DeGennaro et al., 2013. The section on DEET needs to be revised to address these issues and those below to fairly describe the authors results in context. DeGennaro et al., 2013 also should be referenced when discussing the separation between contact and olfactory actions of DEET in the mosquito as that was one of the key findings of the publication.

2) It is not clear whether Anopheles mosquitoes are any different that Aedes mosquitoes in regard to the effect of DEET in the vapor phase. There is not enough evidence presented in the paper to come to this conclusion for the reasons listed above.

3) There is some literature that states that ATP is not a phagostimulant in Anopheles species (https://doi.org/10.1111/j.1365-3032.1985.tb00029.x). ATP works well in Aedes species to stimulate blood-feeding behavior. In this manuscript, the authors conclude that ATP has no effect on Anopheline feeding when compared to Aedes aegypti. Key components of the feeding solution are important to induce engorgement, but not the ATP. The authors should provide their arguments about the choice of the feeding solution used in the study place their findings in the context of earlier literature.

4) Another major concern is the lack of description and validation of the behavioral classification methods used in the manuscript. In its current form the authors do not explain how they segment the behavior of the animals into approach/take off, stationary, walking, exploration, engorged etc. The quality of the analysis will largely depend on how well these classifications capture the actual behavior. Likewise, the authors never benchmark their algorithms. It is critical that the authors quantify how often their algorithm misses or wrongly assigns a specific behavior. Given that the quantification of the engorgement volume is a key parameter it would be especially important to focus on that aspect of behavior (e.g. how is, for example, full engorgement defined?). Ideally, the authors would validate the video-based quantification of the ingested volume by measuring the actual ingested volume experimentally. But given the difficulty in performing experiments at the moment, a validation of the video data using manual annotations and acknowledging the limitation in terms of quantifying actual volume should suffice.

5) The authors should also validate and benchmark the performance of the deep learning-based detection of the appendages.

6) The authors mostly analyze movies from experiments with multiple animals. It is widely acknowledged that reliably tracking the identity of multiple animals is challenging. The authors should benchmark their algorithm and provide an error rate for assigning the correct identity to animals. This is key for the correct interpretation of the results.

7) While the use of a membrane to visualize the actual feeding behavior of mosquitoes is a key aspect of the setup, the authors did not fully exploit it. It would be important to go beyond the anecdotal data in the first figure and show analyses of the piercing and stylet behavior highlighting this key aspect of the setup.

8) Some of the statements in the manuscript are rather anecdotal and would be better supported by including their quantification in figures. Furthermore, statistical analysis needs to be described in more details for Figure 3, i.e. include exact p-values in the figure. It also seems that the number of samples (n=9-10) is relatively low for making solid interpretations. Finally, some of the numbers described in the main text do not match the caption label for Figure 2.

9) The quantitative analysis shown in Figure 5 is insufficient, especially because it does not fully support the statements made in the main text. How is the landing rate (and dwell time etc.) calculated? Are these values normalized to the area coated by DEET and inhomogeneities for mosquito landing observed on the arena? Furthermore, the authors should control or at least discuss the possibility that aversiveness is being caused by physical attributes of the coated surface (i.e., slippery surface).

10) The authors' efforts to make the setup openly available including parts descriptions and code repository are highly appreciated. However, reproducibility and openness could be further improved by making the software easier accessible and understandable by structuring the code in the repository and documenting it, because currently, it does not explain which files to use to reproduce the findings. I also could not find the source data of Figure 2 and Figure 3 as described in the data availability statement. Data from all figures should be made available, clearly labeled, code should be provided for reproducing all figures, and well documented for others to use.

11) The Discussion section is rather superficial. A more thorough comparison of how the observed behavior compares to feeding and foraging behavior of other animals, especially insects would be a valuable addition. Also, discussing the limitations of the method would be advisable. The authors should openly recognize and discuss how prudent is an extrapolation of questions around vectorial capacity and host-vector interactions from a minimalist system with synthetic skin, blood, and without human-specific attractants to 'real world'. If the authors believe that it would not be difficult to augment the experimental setup with a human odor (synthetic or real) or any other attractant, then the text should state this clearly.

Revisions expected in follow-up work:

While the current experimental design of the BiteOscope provides advantages to tracking mosquito feeding behavior on humans or animals, a key question which remains unanswered is to which extent the behavior observed on the membrane is comparable to the behavior on a living host. Except for the actual blood feeing behavior, tracking animals foraging on a host should be feasible. It would be an extremely important addition to compare the behavior of mosquitoes in such a naturalistic setting with the behavior on the membrane. Understandably, in the current COVID situation performing experiments is challenging. Therefore, the authors should at least discuss this caveat and consider performing such experiments in follow-up work.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "BiteOscope, an open platform to study mosquito blood-feeding behavior" for further consideration by eLife. Your revised article has been evaluated by Dominique Soldati-Favre (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) To avoid confusion and false expectations, the title should not include "blood-feeding" but "biting" behavior.

2) The authors should tone down the enthusiasm about the quality of the stylet imaging data in subsection “Automatic characterization of the blood feeding behavior of multiple species” and also mention that using DeepLabcut to track the stylet is not trivial.

3) Please modify the text to clarify the questions of the reviewer 3 regarding responses of the two mosquito species to DEET.

Reviewer #1:

This manuscript presents an exciting new approach to visualizing and characterizing mosquito blood-feeding behavior. This version of the manuscript is substantially revised. It addresses my prior concerns. In particular, I would point to the improved discussion of DEET and how the results presented in this paper fit into our understanding of DEET-mediated repellency. This paper will be of interest to eLife's broad readership and is ready for publication in its current form.

Reviewer #2:

The authors have done a superb job at revising the manuscript and addressing the concerns of the reviewers. Especially given the difficult times.we are all facing. I especially appreciate the thorough validation of the algorithms and the improved description of the methods and the curation of the code on GitHub.

Reviewer #3:

The manuscript is much improved but I'd like some feedback on the DEET story before going any further.

This is a system with many different elements each of which has resolution limits, and the bulk of the reviewers' comments were directed towards getting them recognised and acknowledged. The authors have addressed everything and, in most cases, they seem to have edited and have altered the manuscript sufficiently.

Nonetheless it is ultimately an imaging system and even the best pictures never tell the complete story. For me, a few issues remain.

Blood feeding – given the artificial membrane, the absence of blood/ necessity for clear liquid and presumably subsequent digestion (e.g. peritrophic mem from. Line brane formation?), this is 'biting' behaviour rather than bloodfeeding? This is likely to be relevant to many of the applications listed in the Discussion section.

Similarly, is engorgement an accurate term for what's being measured? Engorgement = fed to repletion, but here that is not always the case and mosquitoes are simply 'fed'.

Also, I wondered whether viewing from directly beneath the ventral abdomen is the most reliable position to measure an abdomen expanding with ingested volume of fluid – i.e. does the abdomen of all individuals expand similarly in every time (e.g. parous vs. nullipars?); what about 3D?

DEET – I found the authors' reply confusing (which read as if Afify and Potter provided more convincing evidence than the authors had.) but the text in the revised manuscript text was much clearer. Nonetheless, I still have reservations: the contact vs. non-contact observations are fine but is this conclusion justified? Can imaging [alone] provide the evidence to solve this question?

1) If the two genera differ in responses to DEET vapour, then in the real world' Anopheles coluzzii would land frequently on DEET-treated skin, whereas Aedes aegypti would rarely/never land. I have no data but having used DEET as a repellent for over 30 years in Africa and elsewhere, I remember Anophelines being repelled completely.

2) In the insecticide world, we use the terms 'contact-irritancy' and 'repellent-induced response', the latter being a change occurring prior to, or without contact. Both are usually bundled together for convenience, often viewed as being a question of exposure dosage from low/vapour to high/contact. I've always had doubts, increasingly so with the recent papers by Ingham et al.

Is it possible that the different responses reported for the 2 genera are the result of different response thresholds, with Aedes being more sensitive at lower levels (vapour) than Anopheles?.… also, have the olfactory neurons in Anopheles coluzzii been explored (which is not mentioned)?

3) Can results from experiments with DEET in the absence of host stimuli be reliable or indicative of anything other than the mosquito can/cannot detect it?

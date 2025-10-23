# Peer review - Round 1

Editors:
- Alex Fornito, Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101688.3.sa0](https://doi.org/10.7554/eLife.101688.3.sa0)

This valuable study applies transcranial direct current stimulation (tCDS) to the prefrontal cortex of non-human primates during two states: (1) propofol-induced unconsciousness; and (2) wakeful performance of a fixation task. The analysis offers incomplete evidence to indicate that the effect of tDCS on brain dynamics, as recorded with functional magnetic resonance imaging, is contingent on the state of consciousness during which the stimulation is applied. The findings will be of interest to researchers interested in brain stimulation and consciousness.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101688.3.sa1](https://doi.org/10.7554/eLife.101688.3.sa1)

General comments

We thank the reviewers and editor for their thoughtful feedback. We are glad that the minor comments appear resolved. In this revision, we added subject-specific analyses, further FC comparisons, and clarified our rationale for stimulation parameters. We acknowledge that two concerns remain: (1) the 1 mA-2 mA sequence may introduce confounds, and (2) electric field modeling was not included due to technical limitations. We now explicitly note these as limitations in the manuscript and provide justification and discussion accordingly.

Major comments

R.2.1. For the anesthetized monkeys, the anode location differs between subjects, with the electrode positioned to stimulate the left DLFPC in monkey R and the right DLPFC in monkey N. The authors mention that this discrepancy does not result in significant differences in the electric field due to the monkeys' small head size. However, this is incorrect, as placing the anode on the left hemisphere would result in a much lower EF in the right DLPFC than placing the anode on the right side. Running an electric field simulation would confirm this. Additionally, the small electrode size suggested by the Easy cap configuration for NHP appears sufficient to stimulate the targeted regions focally. If this interpretation is correct, the authors should provide additional evidence to support their claim, such as a computational simulation of the EF distribution.

R.2.1 Authors' answer: We thank the Reviewer for the comments. First, regarding the reviewer's statement that placing the anode on the left hemisphere would result in a much lower EF in the right DLPFC than placing the anode on the right side, we would like to clarify that we did not use a typical 4 x 1 concentric ring high-definition setup (which consists of a small centre electrode surrounded by four return electrodes), but a two-electrode montage, with one electrode over the left or right PFC and the other one over the contralateral occipital cortex. According to EF modelling papers, a 4 x 1 high-definition setup would produce an EF that is focused and limited to the cortical area circumscribed by the ring of the return electrodes (Datta et al. 2009; Alam et al. 2016). Therefore, targeting the left or right DLPFC with a 4 x 1 setup would produce an EF confined to the targeted hemisphere of the PFC. In contrast, we expect the brain current flow generated with our 2-electrode setup to be broader, despite the small size of the electrodes, because there is no constraint from return electrodes. Thus, with our setup, the current is expected to flow between the PFC and the occipital cortex (see also our responses to comments R3.3., R.E.C.#2.1. and R.E.C.#2.2.).

Second, we would like to point out that in awake experiments, in which we stimulated the right PFC of both monkeys, there was no gross evidence of left or right asymmetry in the computed functional connectivity patterns (Figure 3A, Figure 3 - figure supplement 2A; Figure 5A). These results, showing that our stimulation montages did not induce asymmetric dynamic FC changes in NHPs, support the idea that our setups did not generate EFs that were spatially focused enough to alter brain activity in one hemisphere substantially more than the other.

Third, it is also worth noting that current evidence suggests that human brains are significantly more lateralized than those of macaques. Macaque monkeys have been found to have some degree of lateralized networks, but these are of lower complexity, and the lateralization is less pronounced and functionally organized than in humans. (Whey et al., 2014; Mantini et al., 2013). This suggests that, even if the stimulation were focal enough to stimulate the left or the right part of the PFC only, the behavioural effects would likely be similar.

Follow-up comment: Thank you for the detailed response and for referencing both experimental data and prior literature. While I appreciate the discussion on the lack of functional asymmetry and reduced lateralization in macaques, my original concern was about the physical distribution of the electric field (EF) due to different anode placements. Functional connectivity outcomes do not necessarily reflect EF symmetry, and without EF modeling, it's difficult to determine whether the stimulation affected both hemispheres equally. I understand the challenges of NHP-specific modeling, but even a simplified simulation or acknowledgment of this limitation in the manuscript would help clarify the interpretability of your results.

R.2.2. For the anesthetized monkeys, the authors applied 1 mA tDCS first, followed by 2 mA tDCS. A 20-minute stimulation duration of 1 mA tDCS is strong enough to produce after-effects that could influence the brain state during the 2 mA tDCS. This raises some concerns. Previous studies have shown that 1 mA tDCS can generate EF of over 1 V/m in the brain, and the effects of stimulation are sensitive to brain state (e.g., eye closed vs. eye open). How do the authors ensure that there are no after-effects from the 1 mA tDCS? This issue makes it challenging to directly compare the effects of 1 mA and 2 mA stimulation.

R.2.2 Authors' answer: We agree with the reviewer's comment that 1 mA tDCS may induce aftereffects, as has been observed in several human studies (e.g., Jamil et al. 2017, 2020). Although the differences between the 1 mA post-stimulation and baseline conditions were not significant in our analyses, it's still possible that the stimulation produced some effects below the threshold of significance that may contribute, albeit weakly, to the changes observed during

Follow-up comment: Thank you for the clarification and for acknowledging the potential for 1 mA after-effects. While I appreciate the authors' transparency and the amendment to the manuscript, I still find it important that the limitation be clearly stated in the Discussion section. The fact that 2 mA stimulation always followed 1 mA introduces a potential confound, making it difficult to attribute observed changes uniquely to 2 mA. If a counterbalanced design was not feasible, I would recommend explicitly noting this as a limitation in the interpretation of dose-dependent effects.

R.2.3. The occurrence rate of a specific structural-functional coupling pattern among random brain regions shows significant effects of tDCS. However, these results seem counterintuitive. It is generally understood that non-invasive brain stimulation tends to modulate functional connectivity rather than structural or structural-functional connectivity. How does the occurrence rate of structural-functional coupling patterns provide a more suitable measure of the effectiveness of tDCS than functional connectivity alone? I would recommend that the authors present the results based on functional connectivity itself. If there is no change in functional connectivity, the relevance of changes in structural-functional coupling might not translate into a meaningful alteration in brain function, making it unclear how significant this finding is without corresponding functional evidence.

R.2.3. Authors' answer: First of all, we would like to make it clear that the occurrence rate of patterns as a function of their SFC is not intended to be used or seen as a 'better' measure of the efficacy of tDCS. Instead, it is one aspect of the effects of tDCS on whole-brain functional cortical dynamics, obtained from refined measures (phase-coherences), that specifically addresses the coupling between structure and function. This type of analysis is further motivated by its increasing use in the literature due to its suspected relationship to wakefulness (e.g., (Barttfeld et al. 2015, Demertzi et al. 2019; Castro et al. 2023)). Also, in our analysis, the structure is kept constant: the connectivity matrix used to correlate the functional brain states is always the same (CoCoMac82). Thus, the influence of tDCS on the structure-function side can only be explained by modulating the functional aspects, as suggested by intuition and previous results.

Then, we agree with the reviewer that studying the functional changes induced by tDCS alone could be valuable. However, usual metrics used in FC analysis are usually done statistically: FC-states are either computed through averaging spatial correlations over time, then analyzed through graph-theoretical properties for instance (or by just directly computing the element-wise differences), or either by considering the properties of the different visited FC-states by computing spatial correlations over a sliding time-window, and then similar analysis can be done as previously explained. But these are static metrics, if the states visited are essentially the same (which is expected from non-invasive neuromodulations that haven't already demonstrated strong and/or characteristic impact), but the dynamical process of visiting said states changes, one would see no difference in that regard. As such, in the case of resting-state fMRI, differences in FCs are hard to interpret given that between-sessions within-condition differences are usually found with some degree of variance for the respective conditions. Trying then to interpret between-condition differences is quite tricky in the case of subtle modulations of the system's activity. On the other hand, more subtle differences can be captured by considering more detailed analysis, such as using phase-based methods like we did, by incorporating some statistical learning component with regard to the dynamicity of the system (supervised learning for instance like we did followed by temporal & transition-based methodology), and by adding some dimensions along which one will be able to give some interpretation to the analysis. In our case we were interested in characterizing resting-state differences between stimulation conditions, which have nuanced and subtle interactions with the biological system. As such, classical measures of differences between FC states are likely to not be refined and precise enough. In fact, we propose additional files investigating those classically used measures such as differences in average FC matrices, or changes in functional graph properties (like modularity, efficiency and density) of the visited FC states. These figures show that, for the first case, comparing region-to-region specific FCs provides very few statistically significant results. With respect to the second part, we show that virtually no differences are observed in the properties of the functional states visited. These results suggest, as expected, that the actual brain states visited across the different stimulation conditions are topologically quite similar, and that only very few region-specific pairwise functional connectivities are particularly modulated by specific tDCS montages while, on the other hand, the actual dynamical process dictating how the brain activity passes from one state to another is in fact being influenced as shown by the dynamical analysis presented in the main figures in a more apparent and meaningful way (in that it is dependent on the montage, somewhat consistent with regard to the post-stimulations conditions, and can be made sense of by considering the theoretical effect of near-anodal versus near-cathodal neuromodulatory effects).

Actions in the text: We have added new supplementary files showing the effects of the stimulations on FC matrices and on classical functional graph properties in awake and anesthesia datasets (Supplementary Files 3 & 4). We have added new sentences about these new analyses on the effects of the stimulations on FC matrices and on classical functional graph properties in the Results section:

Follow-up comment: Thank you for the detailed and comprehensive response. The clarification regarding the use of SFC dynamics and the additional analyses provided are convincing.

R2.4. The authors recorded data from only two monkeys, which may limit the investigation of the group effects of tDCS. As the number of scans for the second monkey in each consciousness condition is lower than that in the first monkey, there is a concern that the main effects might primarily reflect the data from a single monkey. I suggest that the authors should analyze the data for each monkey individually to determine if similar trends are observed in both subjects.

R.2.4. Authors' answer: We agree that the small number of subjects is a limitation of our study. However, we have already addressed these aspects by reporting statistical analyses that consider them, using linear models of such variables, and running them through ANOVA tests. In addition, we experimentally ensured that we recorded a relatively high number of sessions over a period of several years. Regardless, we agree that our study would benefit from further investigation into this matter. We have therefore prepared complementary figures showing the main analysis performed separately for the two monkeys as proposed, as well as further investigations into the inter-condition variability outmatching the inter-individual variability, itself being also outmatched by intra-individual changes.

Actions in the text: We have added a supplementary file showing the main analyses performed separately for the two monkeys (Supplementary File 2) and further investigations into the inter-condition variability (Supplementary Files 3 & 4). We have added new sentences about these analyses performed separately for the two monkeys in the Results section:

Follow-up comment: Thank you for addressing this concern and for providing the individual monkey analysis. The additional figures and statistical explanations are helpful and appreciated.

R2.5. Anodal tDCS was only applied to anesthetized monkeys, which limits the conclusion that the authors are aiming for. It raises questions about the conclusion regarding brain state dependency. To address this, it would be better to include the cathodal tDCS session for anesthetized monkeys. If cathodal tDCS changes the connectivity during anesthesia, it becomes difficult to argue that the effects of cathodal tDCS vary depending on the state of consciousness as discussed in this paper. On the other hand, if cathodal tDCS would not produce any changes, the conclusion would then focus on the relationship between the polarity of tDCS and consciousness. In that case, the authors could maintain their conclusion but might need to refine it to reflect this specific relationship more accurately.

R.2.5. Authors' answer: We agree with the reviewer that it would have been interesting to investigate the effects of cathodal tDCS in anesthetized monkeys. However, due to the challenging nature of the experimental procedures under anesthesia, we had to limit the investigations to only one stimulation modality. We chose to deliver anodal stimulation because, from a translational point of view, we aimed to provide new information on the effects of tDCS under anesthesia as a model for disorders of consciousness. It also made much more sense to increase the cortical excitability of the prefrontal cortex in an attempt to wake up the sedated monkeys rather than doing the opposite.

Actions in the text: We have added a new sentence in the Results section:

"Due to the challenging nature of the experimental procedures under anesthesia, we limited the investigations to only one stimulation modality. We chose to deliver anodal stimulation to provide new information on the effects of tDCS under anesthesia as a model for disorders of consciousness and to increase the cortical excitability of the PFC in an attempt to wake up the sedated monkeys."

Follow-up comment: Thank you for clarifying the rationale behind applying only anodal stimulation under anesthesia. While I appreciate the experimental constraints and the translational motivation, I would still encourage the authors to explicitly acknowledge in the Discussion that the absence of a cathodal condition under anesthesia limits the ability to dissociate polarity-specific effects from state-dependent effects. This clarification would help temper the conclusions and better reflect the scope of the current dataset.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101688.3.sa2](https://doi.org/10.7554/eLife.101688.3.sa2)

Summary:

This study used transcranial direct current stimulation administered using small 'high definition' electrodes to modulate neural activity within the non-human primate prefrontal cortex during both wakefulness and anaesthesia. Functional magnetic resonance imaging (fMRI) was used to assess neuromodulatory effects of stimulation. The authors report on modification of brain dynamics during and following anodal and cathodal stimulation during wakefulness and following anodal stimulation at two intensities (1 mA, 2 mA) during anaesthesia. This study provides some support that prefrontal direct current stimulation can alter neural activity patterns across wakefulness and sedation in monkeys.

Strengths and Weaknesses:

A key strength of this work is the use of fMRI-based methods to track changes in brain activity with good spatial precision. Another strength is the exploration of stimulation effects across wakefulness and sedation, which has the potential to provide novel information on the impact of electrical stimulation across states of consciousness. The authors should be commended for undertaking this challenging and important work.

The lack of a sham stimulation condition is a limitation of the study, as it somewhat restricts the certainty with which the results can be attributed to the active stimulation as opposed to other external factors such as drowsiness or fatigue as a result of the experimental procedure? Nevertheless, I acknowledge the demanding nature of performing this work in non-human primates and that only runs with high fixation rates were included, which should have helped reduce any fatigue-related effects.

In the anaesthesia condition, the authors investigated the effects of two intensities of stimulation (1 mA and 2 mA). However, it is possible that the initial 1 mA stimulation block might have caused some level of plasticity-related changes in neural activity that could have potentially interfered with the following 2 mA block due to the lack of a sufficient wash-out period. This potentially limits the findings from the 2 mA block as they cannot be interpreted as completely separate to the initial 1 mA stimulation period, given that they were administered consecutively. However, I do acknowledge the author's point that differences between the 1 mA post-stimulation and baseline conditions were not significantly different, which provides some evidence against this possibility.

The different electrode placement for the two anaesthetised monkeys (i.e., Monkey R: F3/O2 montage, Monkey N: F4/O1 montage) is potentially problematic, as it might have resulted in stimulation over different brain regions. Electric field models of brain current flow for the monkeys would really be needed to understand with reasonable certainty, however, I recognise that these models are generally designed for human studies making their integration into non-human primate studies challenging.

Finally, the sample size is obviously small. However, I realise this is often a limitation in non-human primate research, which can be both expensive and labour intensive.

Assessment:

This manuscript presents some novel insights into the effects of transcranial direct current stimulation on functional brain dynamics in awake and anaesthetised monkeys using MRI-based connectivity indices. Overall, the study presents several interesting and potentially impactful findings regarding stimulation-induced changes in brain activity. There are some limitations, such as the small sample size, lack of a sham stimulation control, and lack of electric field models, which, if included, would have, in my view, further helped improve the rigour of the study. Nevertheless, the manuscript presents several important findings, which warrant further analysis in future work.

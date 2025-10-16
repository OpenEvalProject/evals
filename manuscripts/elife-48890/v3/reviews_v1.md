# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, National Heart, Lung and Blood Institute, National Institutes of Health United States

Reviewers:
- Thomas Hund, The Ohio State University United States
- Molly Maleckar

## Review text

DOI: [10.7554/eLife.48890.sa1](https://doi.org/10.7554/eLife.48890.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work constitutes a significant advancement in the field of theoretical cardiac electrophysiology. Not only is the proposed mathematical model of the human ventricular myocyte an improvement over existing models, in terms of its correspondence with experimental data and its potential to accelerate therapeutic developments in human cardiac electrophysiology; in addition, the calibration and validation of this model also exemplifies a rigorous methodology that will hopefully become standard in this field.

Decision letter after peer review:

Thank you for submitting your article "Development, calibration, and validation of a novel human ventricular myocyte model in health, disease, and drug block" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by José D. Faraldo-Gómez as Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Thomas Hund (Reviewer #1); Molly Maleckar (Reviewer #3).

Although it is customary for eLife to condense reviewers' reports into a concise decision letter, in this case the Reviewing Editor believes it would be best to enclose these reports as originally submitted. Based on these reports, we would like to invite you to submit a revised version of your manuscript that addresses the questions and concerns raised.

Reviewer #1:

This paper presents a modified model of the human ventricular action potential based on a published model from the Rudy group (O'hara Rudy – ORd model). Changes were made to improve the ability of the model to reproduce different aspects of the action potential – especially the plateau potential and APD accommodation. To achieve this goal, Tomek et al. modified the L-Type calcium channel, as well as replacing the formulation of the sodium channel and rapid delayed rectifier channel. The L-Type channel was modified by re-deriving the ionic activity, and treating it as variable in subspaces and time. The L-Type was then also refit using the activation curve normalized to the GHK driving force, rather than the Nerst driving force as was done previously. Additionally, the formulation of the sodium channel was replaced with a version from Grandi et al., 2010, and IKr was replaced with a version from Lu et al., 2001. The changes were than fit to data from the original O'Hara Rudy paper and elsewhere. Finally, the model was validated against APD accommodation from O'Hara, 2011, drug safety predictions, and more, including ECG results from whole heart simulations. This model introduces several notable improvements to the O'Hara Rudy model that will be of interest to mathematical modeling researchers.

1) Chloride current is added to the model without fitting or showing how it affects the model. Additionally, it would be helpful to have a justification of why these currents were added, as well as validated.

2) In Figure 2, inclusion of the other main dataset used by O'Hara to fit the L-Type channel would help in the comparison of the new L-Type formulation to the old formulation. (Fulop et al., 2004).

3) In Figure 5, the fit of the fifth drug, BaCl2, would still be interesting to see as it was used in both O'Hara and Dutta et al., 2017, despite BaCl2 having off-target effects.

4) Please review all equations for typos.

Reviewer #2:

Tomek et al. have put a tremendous amount of effort into improving the O'Hara et al. mathematical model of the human ventricular myocyte. The correspondence of the new model with experimental data is quite impressive, and the authors have done a laudable job of separating the calibration and validation steps in model development. Because these steps have often been combined and/or blurred in previous work in this field, the study provides additional rigor by separating the two steps. Moreover, given the central importance of the O'Hara et al. model in the field, there is a need for improvements, and this work most likely represents a major step in the right direction. These are all reasons to like the paper.

All of that being said, there are certain aspects of the manuscript that are rather confusing and need to be improved. Although the comments below may seem excessive to the authors, it did in fact take multiple readings and considerable additional thinking for this reviewer to fully comprehend some of what the authors had done. It can be a difficult goal to achieve, but the authors should aim for a paper that can be readily understood, even by non-experts, after a single reading. The manuscript doesn't meet that standard at present.

1) One of the most interesting aspects of the manuscript is the discussion of activity coefficients, ICaL current-voltage plots, and the extraction of activation curves (subsection “In-depth revision of the L-type calcium current”). The reviewer absolutely concurs that because many formulations have been inherited from previous models, often without rigorous examination of these formulations, it is entirely appropriate to examine these assumptions and re-formulate currents if necessary. However, this discussion is ultimately unconvincing, and the presentation needs to be modified for this section to be fully understood.

1a) The discussion of the activity coefficients is interesting and will be informative to readers unfamiliar with this primary literature. However, although the authors make a compelling case that different activity coefficients, i.e. closer to 0.6, should be used, the manuscript leaves out the most important question, namely: how do these changes affect the I-V curves?

1b) Speaking of I-V curves, examination of Figure 1D makes a convincing case that the new model has a different shape and matches the experimental data better. However, it's not clear why this occurs – what allows this better fit? Is this due to the changes in activity coefficients? Is it just from the better activation curve shown in Figure 1C? Another fact that can affect this curve is the relative permeability of the channel to Na and K compared with Ca. It's odd that this is never addressed in the manuscript. Did the authors modify this to try to fit the curves better, or were these numbers considered fixed based on original data?

1c) The term "driving force" is used in the manuscript in a way that is inconsistent with prior literature. One of the appeals of Ohmic formulations is that driving force is expressed in units of volts, and conductance can be derived from current plots by simple division. But with a GHK formulation, things are not so simple. The term called "driving force" here does not appear to be in units of volts, so what exactly is this term representing?

1d) Finally, on this same topic, the Discussion states: "Activation curve of the current in previous cardiac models was based on the use of Nernst driving force in experimental studies, but the models then used Goldman-Hodgkin-Katz driving force to compute the current." Again, it's not completely clear how the authors derive one set of numbers (i.e. activation at defined voltages) from a different set of numbers (i.e. current at those same voltages). As I have been writing this, it has occurred to me that perhaps the units of driving force are less relevant, as long as one set of numbers can be multiplied by a different set of numbers to ultimately produce current. However, the fact that I've had to think so hard about this demonstrates that the manuscript needs to do better. Because the ICaL formulation is claimed in the Discussion as "the greatest theoretical contribution of this work," the explanations here need to be crystal clear. Perhaps the supplement should contain flow charts of the conventional method for extracting ICaL activation versus how the new approach improves this, as well as plots showing how the changes to the activity coefficients influence the IV curves.

2) The discussion of Na current blockade and inotropy is relatively weak. Perhaps the authors need to reproduce some original experimental data, or, at the very least, provide some numbers extracted from the earlier studies. The description of Figure 3 discusses the "negative inotropy" previously reported with Na channel blockers, but with no numbers provided. The change in Ca transient amplitude shown in Figure 3C is very small, probably undetectable experimentally. If experiments have reported a 50% decrease in contraction strength, I would say that neither model is consistent, although ToR-ORd is slightly better. Obviously the heatmaps in 3E and 3F provide additional information, but in general here the correspondence with data can be discussed in a more quantitative way. In the Discussion, the phrase "good response of the ToR-ORd model to sodium blockade" sticks out as rather vague.

2a) Again on the Na channel block-inotropy issue. The authors have an opportunity to obtain new mechanistic insight here given that the response of the two models is different. My suspicion is that it might have less to do with the AP morphology, as speculated in the Discussion, and more to do with intracellular [Na] regulation. However, since mechanisms are not explored, we don't know which idea is correct. It might be considered beyond the scope of this study to obtain this mechanistic insight, but it's an interesting question, and the new model provides a means for addressing it.

3) The description of hyperkalemia simulation in Figure 8 should be improved. First, the text claims that Figure 8A shows a "progressive" increase in resting potential and slowing of upstroke velocity. But since the figure only shows 2 examples, it's hard to see that this is progressive. Second, PRR is used in this description but has not been previously defined. It took a few seconds to figure out what the authors meant. Is it really necessary to have an abbreviation for a term that's only used once in the manuscript?

4) The last paragraph of the Discussion, discussing future directions, should be modified. This paragraph states: "Similarly to most existing cardiac models, the equations governing the release depend directly on the L-type calcium current, rather than on the calcium concentration adjacent to the ryanodine receptors, which is the case in cardiomyocytes. Future development of the ryanodine receptor model and calcium handling will extend the applicability of the model.…"

The first sentence is correct, the second is not. The challenge is not to improve the representation of the ryanodine receptor. This will not fix the problems; the problems arise from the fact that Ca release in cells is controlled locally rather than globally – this is why whole cell models, that use a single variable to describe ryanodine receptor gating, need to use shortcuts such as making release directly dependent on ICaL. This general problem was rigorously analyzed by Stern way back in 1992 (PMID: 1330031). For more discussion, see also PMIDs: 15465866, 20346962, 21586292.

It's great to discuss potential future improvements to the EC coupling part of the model, but these discussions should acknowledge that the issue is not just improving the RyR model, but that stochastic triggering of locally-controlled Ca sparks will need to be described.

Reviewer #3:

Mature models and simulation techniques in human cardiac electrophysiology can now be exploited to accelerate therapeutic development and validation e.g. devices, drug development/cardiotoxicity. The authors identify key weaknesses in a model of the human ventricular action potential (ORd, which has been chosen previously by an expert-led initiative to represent the human ventricular AP in validation studies incorporating models and simulation), and present an updated (novel) model of the human AP, the ToR-ORd, to address these.

Overall, the work addresses an important need: in order to effectively translate value from models and simulations in the hoped-for context of human ventricular electrophysiology, the primary model's weaknesses must absolutely be addressed for utility, and so I would consider this work far beyond incremental and a very useful contribution in terms of model to the field at this juncture. The work also nicely leverages a plethora of prior experimental work using direct electrophysiological measurements for calibration and validation. In general, the work is very well organized and well-written.

Comments:

- Cogent, well-motivated Introduction. Weaknesses of ORd (AP plateau potential, APD adaptation and response to sodium current block) and solutions (L-type calcium, excitation contraction coupling and hERG current re-assessment and reformulations) clear.

- Overall goal to design, develop, calibrate and validate the novel ToR-ORd model, with aim of reproducing all key depolarization, repolarization and calcium dynamics properties in healthy human ventricular cells and when these are under drug block, as well as in diseased conditions e.g. hyperkalemia and hypertrophic cardiomyopathy is both timely and useful.

- Importantly, calibration and validation processes are independent, using independent datasets

- "The ICaL current was deeply revisited, particularly with respect to its driving force, based on biophysical principles." – well-motivated, needed, seldom done, valuable to other models. "This allows accurate representation of the driving force when ionic concentrations are disturbed,"

- Really encouraging to see disease-based, multi-scale validation of this nature. Impact for translational work made abundantly clear.

Concerns/areas to address:

1) Given the journal's wide appeal, there is a need to better introduce the strategy and process going into the Materials and methods section, from "We initially performed the evaluation of the ORd model (O'Hara et al., 2011) against calibration criteria…". While I appreciated the simplicity of explanation in general, this guiding summary can be improved to clarify what was initially done and why and how the strategy developed

2) It's also not immediately clear what the calibration criteria actually are (Table 1) – I assume that, in addition to the listed references, that these exist in a supplement somewhere and it would be great to point the reader to this

3) "Simulations with the existing versions of the ORd model failed to fulfil key criteria such as AP morphology, calcium transient duration, several properties of the L-type calcium current, negative inotropic effect of sodium blockers, or the depolarising effect of IK1 block" – where is this shown? Is there a supplementary figure?

4) In-depth revisions based on fundamental physical principles is a much-needed process. Some motivation and/or discussion of the state of the art in this particular field (i.e. how some attention to the underlying biophysics was laid by the wayside in model redevelopment, experimental assimilation, and subsequent versioning, and conjectures as to why e.g. computational tools like versioning tools did not exist, would be appropriate

5) Given the progressive, savvy lean of this work, it seems reasonable to ask why authors did not consider making the code available in other formats, e.g. python as well, or at least justify/mention the relevance of language and tools for reuse/reproducibility/versioning. Similarly, reference to other recent forays into systematic model improvement, e.g. functional curation and web lab, seems warranted

6) Results: "This [ToR-ORd model yields negative ICaL values in such conditions] is a direct consequence of the updates to the extracellular/intracellular calcium activity coefficients, which supports its credibility and it is important for cases of elevated ICaL, such as under ß-adrenergic stimulation." – while this is likely true, it also seems likely a throwaway – were any simulations run using the model to demonstrate the importance in this vein? Important how?

7) Results/Figure 3: Besides noting that the ToR-ORd is consistent with observed negative inotropy of sodium blockers, it is unclear from text how updated model compares in terms of available experimental data, i.e. "A mild increase in inotropy may be achieved only under near-exclusive INa block." – or whether this comparison is available at all.

8) Figure 5A, B, C – the slope of the APD90 dependence on BCL for the ToR-ORd differs consistently from that of the data for BCLs > 1s – any musings as to mechanism? Either briefly in main text or supplement.

9) Figure 6C: would strengthen the case for the ToR-ORd further to compare restitution for ORd in a fibre under same protocol?

10) Seems like suitability of ToR-ORd for drug safety testing is clear – and discussion around this is adequate and encouraging. However, there still does not seem to be a marked improvement in the example given over the ORd (Figure 7), particularly in terms of false negatives. Authors note "further improvement to the score is likely with development of a population optimised towards drug safety assessment" – so it will be interesting to see results there.

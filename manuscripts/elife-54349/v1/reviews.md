# Peer review - Round 1

Editors:
- Tamar R Makin, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54349.sa1](https://doi.org/10.7554/eLife.54349.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides a transparent and balanced communication of the opportunities and disadvantages afforded by spinal cord stimulation for sensory restoration. We are excited about the opportunities offered to the community by the sensations reporting tool, which is of particular value considering the overly descriptive and non-uniform reporting standards in the community. This tool will provide a much needed means for quantitative comparison of results across studies and interventions.

Decision letter after peer review:

Thank you for sending your article entitled "Sensory restoration by epidural stimulation of dorsal spinal cord in upper-limb amputees" for peer review at eLife. Your article has been evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation is being overseen by Richard Ivry as the Senior Editor.

The reviewers and editors agreed that your manuscript provides an interesting approach for sensory restoration that needs to be documented, and appreciated the efforts to characterize the feasibility of this procedure. However, they also agreed that there are too many serious issues in the manuscript that presently preclude the translational impact of the study. To give three examples:

1) Very limited sample size, combined with inherent inter-subject variability deems the interpretation of the findings very challenging.

2) Locality: How focal is the stimulation, and is it useful for the purpose of touch localisation? And how can one deal with the double sensations (on the residual limb)?

3) Action: What are the consequences of the stimulation on motor control and vice versus

Considering the limited translational or neuroscience impact presently afforded by the manuscript, the main innovation the paper provides is methodological. And here we do see considerable value in the study. A key strength of the paper is that it reveals the challenges of the technique, as well as the opportunities.

As such, we would welcome a revision that is restructured as a submission under eLife's Tools and Resources category. https://elifesciences.org/articles/07083. Note that this will require that you revise some parts of the manuscript to better reflect some methodological aspects (for example, what challenging decisions they needed to make during surgical insertion, what worked and didn't work for the stimulation, etc) and/or share some of their code (e.g. the tool they developed to capture the sensory percepts). A revision for the Tools and Resources category would also provide an opportunity to provide a more balanced account of the feasibility of this technique for sensory substitution. This perspective could be worked more explicitly into the manuscript (the reviewers made multiple suggestions to help guide the revisions).

Reviewer #1:

The authors demonstrate that epidural spinal cord stimulation in amputees evokes sensations that are perceived as emanating from the missing limb, and hand in particular, providing an interesting candidate procedure for restoring the sense of touch for prosthesis usage. While previous studies have reported that SCS evokes sensations, this is the first study to meticulously characterise the feasibility of this procedure for sensory restoration in upper limb amputees. The authors demonstrate that by manipulating the stimulation attributes they are able to linearly modulate the resulting sensations, with relatively high predictability of perceptual outcomes. While other techniques are currently available to surgically restore tactile sensations, the current approach provides unique advantages, both in terms of surgical practicality and with respect to amputees with proximal injuries. The authors did a commendable job in characterising stimulus-response profiles, which is no small task considering the massive parameter space and difficulty of measuring subjective reports. Although preliminary, I believe this effort will provide an important first point of reference for considering further the feasibility of this approach.

While there was a lot to like in this study, there were also some major limitations that need to be considered. First, the spatial stability of the stimuli over weeks was pretty disappointing. Is it true that this is comparable with the current state of the art for peripheral stimulation techniques? Second, as emphasised in the manuscript, the inter-individual differences are massive. Because the study only involves 4 subjects, it’s hard to determine what is driving the differences between the subjects, which might be very important for considering the translational power of this technique (e.g. specificity of stimulation site). Third, while this approach is designed for improving prosthesis usage, the current design/results do not seem to take into consideration the practical considerations of prosthesis usage (e.g. active movements, spatiotemporal profile of tactile feedback). For all these reasons, based on the evidence presented here, I'm not convinced that this approach is entirely feasible/promising for tactile restoration of touch. This is not to say that the manuscript should not be published – this is conceptually a very appealing idea and it’s important to set the record clear on the advantages and limitations that it entails. But the manuscript, and Abstract and Discussion in particular, should be changed to reflect these limitations better, to produce a more balanced perspective on the presented results.

1) Beyond the translational significance of this manuscript, it offer modest innovation for basic neuroscience (e.g. the observation on the somatotopy across dermatomes). So it might suit better the methodological format Tools and resources? Note that this will require the authors to share some of their code (e.g. for capturing the sensory percepts).

2) Practically, for the purpose of tactile feedback for prosthesis usage, is this procedure producing sufficient spatial resolution? In other words, are the percepts focal enough, and spatially synchronised sufficiently? Are these percept impacted when the subject is mobile?

3) The authors show very impressive performance with the bayesian classifier for predicting the categorical description, but could this be put into better spatio-temporal context, relating to the other key attributes of the percept? Also, could they correctly classify the sensations across sessions/weeks?

4) The statistical analysis requires further details. What were the parameters used for the GLM? How were they modelled (e.g. repeated model, fixed, etc)? authors should be weary of collapsing data across electrodes and participants (fixed effect, e.g. Figure 3D), as there could be dependencies across same-subject electrodes. How was the classifier trained? When running multiple tests, did the authors account for multiple comparisons?

Reviewer #2:

Chandrasekaran and Nanivadekar et al. present the first clinical results demonstrating the efficacy of epidural spinal cord stimulation to restore targeted somatosensation in amputees. While other groups are pursuing similar goals using technologies such as intraneural stim, the authors' approach has a lot of promise, in my opinion, because it is minimally invasive and employs clinically-available technology with well-established surgical protocols.

I think this is a nice study that highlights both the promise and challenges of pushing this technology towards clinical adoption. It works well as a proof of concept to show that this minimally-invasive technology can be leveraged for sensation, and that. With only four subjects, and with considerable inter-subject differences, the authors are limited in their ability to show how reliably they can target specific sensations. However, it points the way towards a wide range of follow-up studies to continue to explore the potential of this technology.

1) Overall, I appreciated the depth of the data presented, though occasionally the text could read like a "data dump". While this approach is preferable to the overselling that has come to dominate scientific literature, of course, there were some times where I was not sure why the analysis or experiment was performed and how it helped the case for applying epidural stimulation to amputee patients. This minor criticism could be addressed with a small number of additional clarifications to better guide the reader towards the authors' interpretation of the results (I suggest a couple of specific places below).

2) The authors could make better use of the available figures. I certainly don't advocate that a paper must unnecessarily swell to fill the limits on figures, but there were times where interesting analyses were merely described in text with no visually presented data (for example, the GLM model showing the effect of stimulation amplitude), or where supplementary figures were referenced with no corresponding main figure component (for example the linear relationship between centroid stability and time).

3) Lastly, were there ever motor consequences from the stimulation? The work by Capogrosso and colleagues highlight how epidural activation of sensory afferents can be used to drive movements. This level of interaction could complicate the design of protocols meant to simply restore sensation.

Reviewer #3:

"Sensory restoration by epidural stimulation of dorsal spinal cord in upper-limb amputees" is about the sensory feedback restoration to amputees through the epidural Spinal Cord stimulation. Authors describe a human testing with four volunteers is presented in the study.

It is a reasonable study, within the field of sensory substitution/restoration. Yet some aspects should be clarified.

– Regarding the modulation of the perceived sensation: "Increasing the stimulus amplitude increased the perceived intensity of the sensation in all subjects." "For every unit increase in the normalized amplitude, there was a 16% increase in area (p<0.01) and a 110% increase in intensity (p<0.01) across all subjects. This indicates that while percept area is not entirely independent of stimulation amplitude, the unit change in intensity is almost an order of magnitude larger than the unit change in area with respect to stimulation amplitude."

This is somehow misleading, and should be placed in the functional context: it means that in order to modulate the VAS sensation from 1 to 2 the area is increasing the 16% (and what is it on the hand representation spatially)? And therefore, to arrive to the sensation level 2 the area would be 32% bigger? If we consider Figure 2. And subject 2 or 3, it means that the sensory percept already almost whole hand, would then go over the resting part of it? In conclusion it means that it is possible to modulate rather "whole hand" sensation only?

– It is very important to understand the types and percentages of the evoked percepts. Supplementary Figure 3 is meant to do this: why authors do not use some scientific and meaningful representation? E.g. pie chart or something similar with representative percentages? Present figure is disabling the full understanding of sensations variety evoked and their numbers.

– Supplementary Figure 4 is potentially very important since dealing with the stability. Yet the way of presentation of A and B) is really unclear, and not helping in the interpretation of the results. "B, each point represents the change in area of the evoked percept when compared to the median area for a given electrode, expressed as a fraction of the total area of the hand."

Figures should be helpful and easy to interpret, but here I struggle to understand even the meaning of it. It would be important to present it in some more intuitive fashion.

– " suggesting the approach is amenable to a diverse population of amputees."

this is clearly an overstatement: any except very proximal amputees would use other available approaches that deliver more stable, selective, natural and repeatable sensations as extensively reported. Please moderate the statements, from Abstract and within the manuscript.

– Subject 4 is very different w.r.t. other 3-what is the reason? Different surgery?

– Were any types of placebo-s executed? For instance under-threshold stimulation, or any type of possible falsifying strategies (e.g. short pulse supra-threshold and then longer part of pulse under threshold)?

– Clinically, why do you believe that high amputees, e.g. shoulder disarticulation (which are clearly the unique targetable category) would prefer this w.r.t. targeted reinnervation for instance?

– Authors state: "In Subjects 2 and 3, most percepts were accompanied by a sensation on the residual limb… At threshold, paired sensations (perceived in the hand and residual limb) occurred in 0%, 92%, 98% and 8% of all reported sensations for Subjects 1-4 respectively."

So it means that in 2 users the vast majority of all sensations elicited where always accompanied by (at least) a second referred sensation Such a situation can clearly affect the eventual usability of these sensations for the reliable bidirectional control. What is the idea of authors to overcame this?

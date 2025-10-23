# Peer review - Round 1

Editors:
- Richard S Lewis, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66170.sa1](https://doi.org/10.7554/eLife.66170.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper applies intravital 2-photon microscopy to describe the intracellular calcium signals that drive fluid secretion from salivary gland cells in vivo. Secretion of saliva depends on calcium-dependent chloride and potassium channels, and based on studies of isolated salivary gland cells in vitro, these were previously thought to reside in different regions of the cell and require a propagating calcium wave for their activation. This study reveals a much more localized pattern of calcium signals in the intact organ, providing the first view of how calcium is coupled to secretion in vivo and new insights into how ion channel activity is coordinated to optimize secretion.

Decision letter after peer review:

Thank you for submitting your article "The characteristics of intracellular Ca2+ signals in vivo necessitate a new model for salivary fluid secretion" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen Kenton Swartz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Peter Thorn (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The major significance of this work rests on the novel pattern of Ca2+ signals associated with secretion in vivo and demonstrating a consequent need for a revised model of apical K channel activation to maintain the driving force for Cl-efflux across the apical membrane and fluid secretion.

1. Is a new model needed to describe secretion in vivo? The argument for a new model in which Ca2+ activates KCa channels in the apical membrane is based on the observation of low levels of secretion (<5 Hz stimulation) associated with apically localized Ca oscillations. However, these signals are not strictly localized to the apical membrane and would likely activate KCa channels in the basolateral membrane that are close to the tight junctions. In addition, a large increase in secretion is seen for stimuli (5-10 Hz) that propagate Ca to the basal pole, consistent with previous models incorporating activation of basal KCa channels. The contribution of KCa channels in the apical membrane needs to be demonstrated experimentally. This could be addressed by applying blockers to the apical surface, although this may be difficult. Overall, to justify the model, a need for apical KCa channels or evidence of their contribution to secretion, needs to be shown.

2. The apical Ca signals are ascribed solely to release through IP3R, but Orai1 channels, known to be expressed in these cells, are likely to contribute as well. Preferably, Orai1 inhibitors applied systemically (as was done for the cholinesterase inhibitor) should be tested for effects on Ca2+ signals and secretion. At the least the contributions of Orai1 channels should be discussed, taking into account previously published work.

3. The computational model does not adequately reproduce the main features of the Ca2+ response. It shows a large initial spike upon stimulation (Figure 11B) that is not seen experimentally (Figure 9). It also oscillates at a much lower frequency (<0.2 Hz, similar to in vitro) than measured in vivo (0.5-1 Hz). In addition, the model needs to be tested under more conditions to confirm that it can account for the experimental data; e.g., does it predict the intracellular [Ca2+]i gradients, and how increasing stimulation frequency changes the Ca2+ response? More data are needed to justify the choice of model parameter values.

4. The absence of local apical Ca2+ signals in vitro is not the case for all exocrine acinar cells. The authors should acknowledge that local apical responses have been seen in other acinar cells (e.g. pancreatic acinar cells) in vitro, upon stimulation with physiological concentrations of hormones, low concentrations of neurotransmitter, or directly by IP3.

5. The current data do not allow a fair comparison of the spatiotemporal aspects of Ca2+ signaling in vivo and in vitro. While the use of GCaMP6f is a good way to rule out effects of different indicators (e.g., fura-2), other factors are likely to contribute and can be easily tested:

(a) The in vivo experiments were conducted at 37 deg C while the in vitro imaging seems to have been done at room temperature (temperature was not indicated in the Methods). Cooler temperature is likely to affect oscillation frequency as well as the rate of pumping or sequestration which could affect propagation.

(b) The concentrations of ACh used in vitro may not relate to the neural stimulation frequencies in vivo. The 100 nM response in vitro is quite large, so it may not be fair to compare this with low- frequency stimulation in vivo where signals are confined to the apical pole. Perhaps more localized signals would result from lower ACh concentrations.

6. The method for standard deviation (SD) image processing should be described. This approach highlights areas that oscillate, but may de-emphasize areas of tonic elevation which would also be expected to drive secretion. At 5 Hz stimulation it shows that oscillations are confined mostly to the apical region (Figure 7C), but at 10 Hz the cells don't seem to oscillate (Figure 8), so it is not clear why SD images are presented here. It would be more informative to plot a cross-section of GCaMP6 signal from apical to basal before and during stimulation.

Reviewer #1:

This work offers a new look at the calcium signals that drive secretion in salivary gland cells. Based on studies of isolated cells in vitro, the common view was that calcium signals originating in the apical pole of the cell propagate to the basal pole, so that chloride channels allow chloride ions to exit across the apical membrane while K channels in the basal membrane are opened to maintain the electrical driving force for chloride exit. Through an elegant use of 2-photon microscopy to monitor the spatial spread of calcium signals in intact glands in vivo, the authors describe a different pattern, in which the signals do not propagate but are much more confined to the apical pole of the cell, and they show that secretion occurs even without significant spread of calcium to the basal pole. These results are significant as they challenge current mechanistic models for secretion, and they imply a functional role for K channels in the apical membrane, which until now have been commonly considered to only function in the basolateral membrane.

However, the paper has several shortcomings that need to be addressed to better support a need for revising the current secretion model. It is not clear whether KCa channels in proximal regions of the basolateral membrane are activated by the apically confined Ca2+ and therefore are sufficient to support secretion. A modified computational model intended to support the need for apical KCa channels does not offer strong support, as it does not faithfully reproduce several of the experimentally observed Ca2+ responses. Finally, the differences between the spatiotemporal aspects of Ca2+ signaling in vivo and in vitro are difficult to assess as critical conditions such as temperature and agonist concentration were not matched in the two experimental scenarios.

Reviewer #2:

In this study Dr. Yule and his colleagues describe very impressive and painstaking work in which they have monitored for the first time Ca2+ signals and salivary secretion in vivo in a mouse model which expressed the Ca2+ indicator protein, GCamp6F, in salivary glands. Previously reported studies measured fluid secretion in vivo by injecting the animals with pilocarpine and collecting the oral secretion or by using protocols where the gland is perfused. However, cytosolic [Ca2+] changes, which are correlated with, and required for, salivary fluid secretion have been predominantly measured in isolated acinar or cell cluster preparations and some in tissue slices. By using intravital multiphoton (MP) microscopy together with stimulation of the neural input to the gland, the authors were able to measure the spatiotemporal properties of Ca2+ signals within the acinar cells and collect saliva that is secreted into the oral cavity. Thus, this study is an important breakthrough in this field as it reveals the exact [Ca2+] changes associated with salivary gland fluid secretion.

This study shows that major spatiotemporal properties of the Ca2+ signals detected in vivo are markedly different from those previously reported using isolated acinar cells (by this group and others) which demonstrated that Ca2+ signals are initiated apically but propagate as a wave globally across the cell without generation of Ca2+ gradients. The present findings show that following moderate stimulation, apically localized oscillatory Ca2+ signals are generated that do not propagate globally and cause minimal secretion. However, at stimulation intensities optimum for secretion, there is a spread of Ca2+ across the cell although with an apical-basal standing Ca2+ gradient. Based on these differences the authors have proposed a revised model which suggests that the apical region contains all the machinery needed for saliva secretion and that Ca2+ released predominately in the apical region, via IP3R, can regulate the function of locally situated ion channels without requirement for a propagated wave of increased [Ca2+] across the cell. As I have noted above the data described in this manuscript provide new understanding of the physiological response of salivary gland to neuronal stimulation and how fine-tuning of the spatiotemporal properties of the Ca2+ signals regulate fluid secretion.

The main question I have is regarding stimulus strengths that induce optimal levels of secretion (10 and 30Hz) where there is propagation of Ca2+ across the cell and almost 3-fold higher secretion relative to that at 5Hz. While increase in % responding cells at higher stimulus strengths could result in higher total secretion, possible contribution of Ca2+ influx pathways in the spread of Ca2+ in individual acinar cells, e.g. via Orai1 that is localized in the apical region of the cell, cannot be ruled out. Also not clear is whether the spread enhances secretion. Thus, when stimulus is low, secretion is minimal and supported only by release and oscillatory apical [Ca2+]. At higher stimulus strengths there might be an additional Ca2+ influx component which is activated very early after stimulation, likely during IP3-mediated Ca2+ release. Since the basolateral membrane extends all the way to the tight junction, is it possible that several components shown basally localized in the model could actually be quite close to the apical membrane region, near the tight junctions.

Thus, it is important to distinguish between initial stimulation of secretion vs regulation of sustained secretion. For example; the last sentence in the abstract clearly, and correctly, states "salivary secretion can be efficiently stimulated by apically localized Ca2+ signals".

Reviewer #3:

This paper describes a nice set of experiments where the authors have measured calcium responses in salivary acinar cells from living animals and, importantly, correlated these with measures of salivary secretion. The work is very well performed and the data interesting and definitely an advance in the field. I cannot think of another study that combines, so well, cellular calcium responses with genuine physiological output.

Strengths

Intravital images are very good and the combination with fluid secretion gives a nice correlation between calcium responses and physiological output – something which is impossible in vitro.

Good initial analysis of the images and convincing data where the calcium responses are further analysed.

The conclusions that local calcium responses can drive physiological responses is interesting in the context of salivary glands.

Weaknesses

The authors claim that local responses are not seen in vitro is dependent on taking a very narrow view of exocrine cells. Local responses are readily seen in other exocrine cells, like pancreatic acinar cells. These local responses can be driven directly by IP3, low concentrations of neurotransmitter, or physiological concentrations of hormones. Furthermore, these responses drive enzyme secretion. Therefore, although these local responses have not been measured intravitally, it is highly likely that they are the native response in the pancreas.

The new model put forward is conjecture. It is built entirely around the observations of localised calcium responses but has no supporting data on changes in membrane potential or activation of specific channels.

The in vitro GCaMP data is not convincing. GCaMP and Fura have different affinities for calcium and so this is a serious potential confounder in their experiments. For the in vitro work, the isolated cells are clearly fragmented and the cell chosen is at the edge of the cell cluster. It would be expected that the cells will completely lose their polarisation and structural factors that might limit the calcium response.

While I like the analysis, I think that much of it is unnecessary. The authors, for example, show that regions that respond well at low stimulation also respond well at high levels of stimulation. That's fine, but the authors then do not explore what the basis of these differences are.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The characteristics of intracellular Ca2+ signals in vivo necessitate a new model for salivary fluid secretion" for further consideration by eLife. Your revised article has been evaluated by Kenton Swartz (Senior Editor) and a Reviewing Editor.

Thank you for the revised manuscript with the additional data and clarifications. Your responses have addressed most of the major concerns of the reviewers. The only remaining issue is whether KCa channels in the apical membrane are required for secretion. I think this is central to the significance of the paper. The study shows beautifully how Ca signals are mostly apical and do not propagate to the basal membrane in vivo, but the most interesting implication is that it necessitates having KCa channels near or in the apical membrane. To broaden the appeal of your paper to more than exocrine gland physiologists it will be important to establish this point clearly.

We understand that an experimental approach (luminal application of blockers) to establish the role of apical KCa channels is not feasible. Thus, the model offers the best opportunity to test this idea. The model needs a fuller description, not including all the details and equations, but rather a description of the salient features that will allow the reader to grasp how it works, and what assumptions it makes. The comments below summarize the uncertainties in the model's operation that need to be addressed:

1. How are apical, cytoplasmic, and basal regions defined in the model, and how do they correspond to the same regions in the experimental data? Throughout the paper there are references to "apical PM" or "apical region." The apical PM is the membrane bounded by tight junctions, but what does "apical region" mean – does this include lateral membrane between the apical PM and the nucleus? The model cartoon in Figure 13 does not explain the distinction between apical and basolateral. Likewise, on p. 12: "We emphasise that, in the model, KCa channels and Na/K- ATPases are also present in the basal membrane, and thus the secretory machinery is not restricted to the apical membrane." Is "basal" here referring to lateral membrane as well? I imagine that some of this vagueness is because the anatomy is complex and the localization of channels is not precisely known, but this needs to be clarified, particularly for non-expert readers.

2. How is the KCa current simulated? This is a crucial part of the model, but it is not clear how this was done. The only description is (p. 25) "The apical/basal K+ current ratio was determined by the apical/basal surface area ratio." After Ca2+ is released from the ER, is it assumed to diffuse to the lateral membrane where it activates KCa channels? (lateral membrane is defined here as basolateral membrane between the tight junction and the nucleus, corresponding to the "cytoplasmic" region in the experimental Ca measurements.) Or is only the basal Ca2+ signal being used to determine KCa current? The data in Figure 10 show that there is significant Ca2+ elevation in the cytoplasmic region below the apical membrane even at low stimulation frequencies, which could activate channels in the lateral membrane. What spatial distribution of KCa channels is assumed in the model? These things need to be clearly and simply explained.

3. The model shows that with no apical KCa channels (but the same total number) you still get ~80% of the maximal response (Figure 14F). This is almost maximal and implies only a modest effect of true apical PM channels. Figure 14F Y axis should be plotted from 0 rather than 60, in order to give a truer impression of the effect of KCa channel localization. There is also some confusion here: Figure 14B shows only 50% of max response if you remove apical KCa channels – but I assume that this is because the total number of channels was not constant in this case, resulting in fewer KCa channels than in Figure 14F. If so, that is not a fair comparison.

4. On p. 17 there is a reference to Supp. Figure 4, but that figure was not included.

5. I would suggest some rewording of the title, as it seems too focused on what was done, rather than the most significant result. Perhaps you can revise it to focus on localized calcium signaling that engages apical K channels in vivo.

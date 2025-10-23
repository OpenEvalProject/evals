# Peer review - Round 1

Editors:
- Joshua Johansen, RIKEN Center for Brain Science Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57148.sa1](https://doi.org/10.7554/eLife.57148.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study includes a particularly intriguing use of calcium imaging to monitor single neuron activity deep in the brain during behavior to demonstrate that ventromedial hypothalamic (VMH) cells respond during socially threatening experiences. The most compelling aspect of the results was the finding that VMH cells come to encode contextual features of the defeat environment or respond in the safety of the home cage following social defeat experiences. These findings show how aversive social experiences reconfigure hypothalamic circuits to drive learned adaptive behaviors.

Decision letter after peer review:

Thank you for submitting your article "Dynamic encoding of social threat and spatial context in the hypothalamus" for consideration by eLife. Your article has been reviewed by three peer reviewers and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses and data are required before a final decision can be reached, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this manuscript, using newly designed behavioral paradigms and microendoscopic calcium imaging of deep brain area, Krzywkowski et al. reported that past social experience reshaped activity patterns of social threat and spatial context neurons in the VMHvl. They first designed a new behavioral paradigm for performing rodent social defeat in far chamber, resident-intruder test in home chamber, and approach-avoidance behaviors without manual interference. Next, they applied in vivo microendoscopy to image calcium response of VMHvl neurons at single-cell level in free-moving mice subjected to social defeat. Using these approaches the authors revealed that neurons in the ventrolateral subregion of the VMH (VMHvl) are activated by social threat as well as the context in which that social threat occurred. Furthermore, using the resident-intruder test in home chamber, the authors found that the VMHvl neurons showed an overlapping encoding of social defense and aggression. Moreover, the authors found that social defeat experience altered neurons in the VMHvl such that subsequent optogenetic activation of VMHvl could elicit avoidance of the defeat context. Collectively, these findings reveal a novel, dynamic role for the VMHvl in mediating both social threat and the contextual factors which control these threats.

Overall, this interesting set of data represents a conceptual advance in understanding the role of the VMHvl in aggressive behavior and contextual coding and the reviewers are generally enthusiastic about the work. However, there are a number of important analytic concerns and key behavioral measures are missing. In addition, tracking single cells across days during calcium imaging experiments is not trivial and the authors need a more rigorous assessment of this. Though no new experiments are required, the addition of new analyses, existing data and textual revisions is therefore necessary before a decision can be reached.

Essential revisions:

1) The authors wrote that "Many neurons (100/246, 40%, Social+) showed an increase in activity during close social interaction that returned to baseline levels during the subsequent approach-avoidance phase". It is unclear whether "close social interaction" means the whole period in the far chamber or every social interaction epoch with the aggressor. Please clarify. In Figure 1F, G, H, the authors only showed overall calcium activities in and out of the far chamber. It should be possible to align the signal to every social interaction epoch as shown in Figure 1I, J, K, which will provide more information on the timing of Ca signals. In addition, since the VMHvl also responded to contexts as shown in Figure 2, a control experiment should be performed for Figure 1L, with no aggressor in the far chamber to exclude the context-coding neurons from Social+/- neurons.

2) The definition of Flight- neurons and calculation of their auROC are confusing. An auROC value smaller than 0.5 means that the neuron has a higher tendency to fire not during the event. However, in the bottom trace of Figure 1O, the activity of the example Flight- neuron is elevated right before the flight behavior and declined during the flight, but still above the baseline. According to this pattern, its auROC value should be bigger than 0.5, contradicting to its definition (auROC < 0.35) as indicated in Figure 1Q.

3) The authors concluded that "defeat has a unique capacity to alter the encoding of social cues in VMHvl. Notably, this change was found only when defeats preceded, but not when they followed aggression experiences". Interesting result, but it is not clear whether this difference in VMHvl neural coding is a consequence or a cause of different behavioral performance owing to different sequential order of defeat and aggression. The authors seem to implicate the behaviors are the same with the statement that "The experimental animals showed similar frequencies of behaviors across the two days of social defeat (Figure 4—figure supplement 1A)". However, they mixed behavioral results of all mice tested with different sequential orders. Please separate the two groups with defeat before or after aggression and quantify the behaviors again.

4) For Figure 1, no behavioral data is shown or described at all in the main text or supplement in relation to Figure 1. Do all the mice experience defeat? Is the degree to which a mouse is "defeated" (i.e. number of attacks, etc.), related at all to neuronal activity patterns? How much time on average do mice spend avoiding or approaching the defeater? The authors should display and describe their behavior data for this initial Results section.

5) In the subsection “Encoding of social threat”, Social- neurons are described as showing either no change during defeat/social investigation and an increase in activity during the approach/avoidance phase or a reduction during the defeat phase coupled with an increase in the approach/avoidance phase. However, the data for these two options is pooled under the "Social-" category, where really, they should be pooled under an Avoidance+ category. This pooling seems to ignore the potential differences between the 3 types of neurons the authors identify: 1) Social+/Avoidance- cells, 2) Social no change/Avoidance+ cells, and 3) Social-/Avoidance+ cells. The reviewer understands that separating the data further would increase the complexity of these data and introduce additional factors to consider, however, perhaps a supplementary figure breaking down these groups could be included, or at the least, a revision to the text explaining why neuron classes 2 and 3 are being merged.

6) The authors say that they use a cutoff of >0.65 and <0.35 to classify cells as being responsive to a given behavior, but also say they use a shuffling procedure and a significance cutoff of >/= 3SD from the mean. It is not clear when these different criteria were used. For example, this leads to some confusion when examining Figure 1. For Figure 1H, K, N and Q frequency histograms, there are colored portions of lines below 0.65 and above 0.35. Are the cells counted here assessed using the 3 SD criterion? Relatedly, for cell counts in the Venn diagram in Figure 1T, which criterion was used to classify them? This same confusion applies to all imaging figures.

7) Similar to point 4, the authors show no behavioral data for Figure 2. How much time do mice spend in each of the chambers during the test phase? Is it related to the degree to which they were defeated the prior day? These should be data that the authors already have and can put figures together for without running any extra experiments.

8) Figure 3A-D. There is usually a small percentage of resident animals in a resident intruder assay that fail to exhibit any fighting (as seen in papers cited by the authors throughout the text). Did the authors see aggression in all of their residents? This is important as it speaks to the degree of overlap observed in this experiment (for instance, perhaps the degree of overlap seen is due to the animal(s) that didn't fight?).

9) The authors wrote "Defeat+ and Assessment+ cells showed a high degree of overlap (32% vs. chance 20%, P > 0.1)". How can the conclusion of overlap be made based on a non-significant p value?

10) The cluster distance statistical measure/comparison used for the contextual coding and effects of repeated defeat on population activity should also be used for the analysis of the effects of repeated defeat on ESR1+ cells (related to data in Figure 4K-L).

11) The authors concluded that "VMHvl neurons promote aggression and defense" based on data from Figure 5. Yet only defensive behavior, no aggression, was analyzed in Figure 5.

12) Is the "social interaction" behavior in Figure 5 the same as "close social interaction" defined in Figure 1? If yes, please explain the discrepancy between optogenetic manipulation (activation of VMHvl Esr1+ neurons decreased social interaction, Figure 5) and endoscope recording (more Social+ neurons than Social- neurons found in VMHvl, Figure 1).

13) Are the mice used for the data presented in Figure 5E the same as 5D or are these separate cohorts of mice? If the former, could the repeated optogenetic activation explain some of the effects observed? Please explain/clarify in text.

14) Given that the endoscopic imaging lasted for ~1 week (as shown in Figure 1—figure supplement 1A-C) and several comparisons were conducted across days, it is critically important to verify the stability of imaging across different recording days. Please show maps of spatial filters of all cells from each day of imaging and the overlaid filters (see Extended Data Figure 7 in Remedios et al.'s paper (Remedios et al., 2017) for reference). In addition, the authors should think about using a more quantitative measure of ROI stability potentially using an existing algorithm for aligning ROIs across days (such as Sheintuch, L….Ziv, Y. Cell Reports 21(4) pg. 1102, 2017).

15) In the optogenetic experiments the authors say they use a YFP alone control (subsection “Functional remodeling of Esr1+ neurons by social defeat”), but don't show the data. This data should be shown.

16) Please ensure you include full statistical reporting including F, t statistic, degrees of freedom, exact p value, etc.

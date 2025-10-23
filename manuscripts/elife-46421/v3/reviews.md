# Peer review - Round 1

Editors:
- Leslie C Griffith, Brandeis University United States

Reviewers:
- Leslie C Griffith, Brandeis University United States
- Paul Taghert, Washington University Medical School United States

## Review text

DOI: [10.7554/eLife.46421.sa1](https://doi.org/10.7554/eLife.46421.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Imaging neuropeptide release at synapses with a genetically engineered reporter" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Leslie C Griffith as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Eve Marder as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal their identity: Paul Taghert (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper develops a new set of tools for looking at release of peptides in real time. The idea is a good one and there is a need in the field for such tools. The authors describe a genetically encoded reporter system for dense core vesicle (DCV) fusion in Drosophila. They generate a host of fusions of GCaMP6 to ANF and DTK neuropeptides and identify a specific fusion event that localizes well to DCVs by both immunocytochemistry and immuno-EM. The authors show the sensor can respond to strong stimulation and compare the response to cytosolic GCaMP6 as a read-out of intra-terminal calcium changes. Overall, it's a potentially useful tool for the field, but the study could add a bit more quantification to demonstrate how well the sensor is actually working.

Essential revisions:

1) The major issue the reviewers had with the feasibility of this approach for dissecting DCV release is the conditions needed to trigger these changes – 70 Hz stimulation for 18 secs. These motor neurons would never experience such extreme stimulation in vivo. Peptidergic neurons typically fire in the 1-5 Hz range and while motor neurons fire at higher rates, natural stimulation is not of the duration used here. The signal-to-noise ratio (δ F changes) of this DCV sensor (compared to GCaMP alone which appears to be at least 5-10x more sensitive) is also rather poor. As such, it would be informative to have more information on the dynamics of their new reporter.

a) Provide a dose response curve to demonstrate both the required stimulation frequency (only 70 Hz is reported), the required length of stimulation (only 18 seconds is reported) and the calcium response curve. What does 1 Hz look like? Or 5 Hz?

b) The authors only report changes in the Type 3 terminals. What did the authors see in the Type 1 terminals that have fewer DCVs? Was DCV release detectable in these neurons, as has been reported in the field for the classical ANF-GFP DCV sensor? These data may be more useful than Type III data for investigators contemplating using this tool in neurons that do not have huge numbers of DCVs.

c) It would be helpful to use a benchmark to compare the methodology described here to that currently used in the field – the loss of ANF-GFP signal following stimulation. Is the current system actually an upgrade over that? There is unique value here in the potential to endogenously target specific neuropeptides for this technique, but if the sensitivity is far below that of ANF-GFP, the older system might still be the one of choice for dissecting the biology of DCV fusion overall. Without these data it is hard to claim an advance.

2) It would be helpful for the authors to further clarify in discussion what they actually think the sensor is reporting over time. It was not clear to reviewers exactly what the rise/falling/undershoot/recovery phases actually represent. The recovery phase is especially mysterious since the soma is gone so it cannot be replenishment via transport. DCVs are known to only release part of their cargo during stimulation, so presumably many of these DCVs still contain GCaMP-tether neuropeptide within them. Do the DCVs that have fused become less acidic and take up come extracellular calcium and thus activate the remaining GCaMP within them? Or do the authors think that the DCVs release all their content, or not take up calcium or lose their acidity during partial fusion events? This seems a potential confound – the authors are measuring a transient rise in calcium influx and pH change within the lumen of the DCV, not the actual release of the neuropeptide-GCaMP.

While the reviewers did not feel that it was required that this point be addressed with new experiments, it would be incredibly informative to assay their sensor in animals concurrently expressing an ANF-mCherry, ANF-mOrange (or other red-shifted tagged neuropeptide) where loss of the neuropeptide is directly reported in addition to the neuropeptide-GCaMP signal. That would really help clarify what is likely to be happening with their sensor during these phases of DCV release or partial fusion.

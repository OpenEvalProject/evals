# Peer review - Round 1

Editors:
- Richard Amasino, University of Wisconsin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31700.033](https://doi.org/10.7554/eLife.31700.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Coordination of robust single cell rhythms in the Arabidopsis circadian clock via spatial waves of gene expression" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Richard Amasino as the Reviewing Editor and Christian Hardtke as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Andrew Millar.

The Reviewing Editor has drafted the comments below, which are based on the reviews, to help you prepare a revised submission.

Two papers from Tokitaka Oyama (Okada et al. 2017 and Muranaka and Oyama, 2016) have done fairly significant scale of single-cell imaging, both in terms of number of cells and of time series duration. Although these were using Lemna fronds, and this Arabidopsis work addresses considerably greater organ complexity, these two papers ought to be cited.

The authors argue that damping in individual cells is small relative to cell desynchrony, largely it seems by inspection of Figure 1—figure supplement 5. That argument is reasonable – the conclusions of the present paper depend more on the clear differences among tissues than the more subtle differences among cells within a tissue. Future work will require a more objective method to score damping in individual traces, which should be possible from individual peak/trough data.

The model result in Figure 3K achieves a qualitative match to the spatial pattern of phases along the root, driven simply by period differences of 1.5 to 3h among root sections. One difficulty inherent in the modelling is that these period differences are estimated from intact plants, so the measured periods include effects of coupling. This is unavoidable, as there is currently no reliable means to measure the rhythmic properties of physiologically-representative plant cells in physical isolation, and this issue needs to be clearly noted in the paper.

"waves cause the most desynchronisation." Averaging over the waves of mean phase along the y axis is one factor that contributes to damped rhythms in the root as a whole. The other factor is the more variable period among cells at each y position in the root (e.g. Figure 3H), compared to the hypocotyl or cotyledon, which the authors attribute to weaker coupling. These two sources of desynchrony were not quantitatively compared, and preferably they should be. Alternatively, the authors could qualify the claim that averaging of the mean phase along the root has a greater effect than desynchrony at a single location.

To convey the scale of the rhythmic patterns and the difference among locations, from the data analysis here, can the authors estimate a characteristic separation distance where clocks have similar phases, compared to more distant clocks?

Absence of radial (z-axis) patterning in the root (Results, fifth paragraph) is a new and interesting result, suggesting that rhythmic properties are not cell-type specific in the bulk of the root. This is the first dataset with both the spatial resolution and temporal duration to address this issue for any plant organ. However, only one dataset is shown with z-axis resolution. Does the same result hold in the repeat seedlings?

Data and code availability:

It is good to release the numerical data on BioDare, but BioDare hosts many public datasets. The authors should give specific identifiers for each experiment, data set or script in the paper, perhaps as a table, to relate specific figures to the relevant, underlying data. BioDare Experiment IDs are unique, stable identifiers for this specific purpose. Will the fluorescence image stacks also be available? Preferably, however, the data ought to be deposited at Dryad (http://datadryad.org/) because this site is likely to be more stable long-term.

The periods of the clock in the model were faster in the shoot and root tip thanthe rest of the root. Might this be related to patterns of somite rhythms (Benfey lab papers) that are associated with lateral root emergence. If the plant clock drives auxin rhythms, are these causal to developmental outcomes at the single-cell level? Although outside the scope of this work, maybe a sentence of speculation in the Discussion might be helpful to a general audience?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Coordination of robust single cell rhythms in the Arabidopsis circadian clock via spatial waves of gene expression" for further consideration at eLife. Your revised article has been favorably evaluated by Christian Hardtke as the Senior Editor, Richard Amasino as the Reviewing Editor, and one reviewer.

It has long been observed that plant rhythms damp over time. This has been attributed to desynchronizing of oscillators in individual cells, but there has been little experimental support for this hypothesis. Your work provides such experimental evidence. It also describes waves of clock gene expression running from shoot to root and from the root tip up the root which strongly supports coupling among clocks in different cells. This work is likely to stimulate and inform the next rounds of experiments and models. The manuscript has been improved but there are some remaining major points that must be addressed:

Introduction, third paragraph. Figure 1C is described as showing individual cells losing rhythmicity, but doesn't it actually show all individual cells losing amplitude, which is different. If individual cells lose rhythmicity would you not have some cells remaining rhythmic (with or without a loss in amplitude) while other cells cease cycling and instead display either constant expression or randomly varying expression levels?

Results, third paragraph. The authors state that "most" cells display circadian rhythms. Can this be quantified? Is most 51% or 90%? Although this would be somewhat arbitrary, based on the cutoffs chosen, it is important to provide the reader with an estimate in the text.

Results, fourth paragraph. How was it determined that the single cell rhythms in the hypocotyl and cotyledons are more robust than a system size of 100 and are closer to a system size of 1000? Was this by visual inspection? Can this be quantified? Perhaps through a comparison of the variances of estimates of period and phase? Similarly, is the greater variability of root phases than phases in the rest of the plant (Results, fifth paragraph) by inspection? Could this be quantified?

Results, last paragraph. Cell density is greater in the root tip than elsewhere, which may contribute to increased coupling. Another tissue with increased cell density is the Shoot Apical Meristem. Given the suggestion of Takahashi et al. that the SAM is important for the maintenance of root rhythms, it would be interesting to look at rhythmicity in the SAM. Although an examination of the SAM is not necessary for this manuscript, the authors may want to consider this and mention it in the paper.

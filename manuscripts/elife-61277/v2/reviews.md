# Peer review - Round 1

Editors:
- Martin Vinck, Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61277.sa1](https://doi.org/10.7554/eLife.61277.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

General value assessment: The brain is a hierarchically organized system. Is information in higher brain areas integrated over different time-scales than in lower brain areas? Gao et al. analyze intracranial recordings in humans across a large part of the neocortex using several new analytical techniques. They find that higher brain areas have longer neuronal time-scales. Neuronal time-scales are correlated with specific gene expression patterns, and are correlated with working memory performance.

Decision letter after peer review:

Thank you for submitting your article "Neuronal timescales are functionally dynamic and shaped by cortical microarchitecture" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Thilo Womelsdorf (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Gao et al. analyze how brain-wide timescales of ECoG signals vary across the cortical hierarchy and relate these timescales to several other aspects of structure, behavior and function. They report the following main findings: 1) Timescales increase with the cortical hierarchy. 2) Time-scales, after regressing out the hierarchical T1w/T2w structure variable, correlate significantly with several genes related to synaptic receptors and ion channels. 3) Time-scales increase with working memory task vs. baseline, and predict working memory performance across subjects. 4) Time-scales decrease with aging, in a region-specific way. These findings are a significant advance in comparison to previous work by considering brain-wide hierarchy at a high spatial and temporal resolution and relating them to behaviour and genetics.

All four reviewers agreed the study is of substantial interest. The study was found of high quality.

Essential revisions:

1) Definition and comparison of timescales:

i) The comparison shown in Figure 2 between spiking time-scale and ECOG time-scale might be problematic, in the sense that the spiking time-scales were taken from the Murray et al., 2014 paper where they were quantified with a different technique. A possible solution would be to quantify time-scales in the same manner as Murray, or maybe there is a convincing argument why this is not a problem.

ii) For the non-specialist reader, the concept of neuronal timescales that is central to the paper should be defined more explicitly in the Introduction ('neuronal timescales' appear in paragraph three, while it gets defined in paragraphs one and two).

iii) Fast and slow responding to sensory versus cue related information may reflect a circular definition of timescales.

iv) The Results text says that the aperiodic components is interpreted as time scale but not how the inference is made, i.e. what quantity is interpreted as time scale.

v) It is difficult to keep track of which timescales are referred to when in the text, e.g. the authors start referring to neuronal timescales after having discussed ECOG based time scales and spike timescales. It seems important for cleanly separating the source of the timescale to denote them with a unique label depending on the source data that give rise to them. Why not using a subscript for spike, epiduralECoG, subduralECoG, intracranialLFP,.… ?

2) Timescales and hierarchy:

i) The correlations shown between transcriptomics and timescales need to be carefully considered. While the authors regress out T1w/T2w residuals, these might just be one structural factor that changes with cortical hierarchy and assumes that the underlying relationships are linear. Hence, it is possible that timescales and gene profiles are correlated with structure but that there is no causal relationship between these genes and timescales. In this sense, the correlation of genes with hierarchy might also yield similar genetic profiles. It would be important to show the correlation of hierarchy with genetic profiles, to see whether this looks different from the correlations that are obtained with timescale.

ii) The authors use T1W/T2W as the measure for cortical hierarchy. This is a gradient-based perspective on cortical hierarchy. However, there are other perspectives on hierarchy that are not gradient-based, but are based on anatomical connectivity, e.g. as pursued by Kennedy and Van Essen (Vezoli et al., 2020). This needs to be discussed.

iii) The manuscript addresses two distinct aspects of neuronal timescales: their relationship to local microarchitecture and their dynamics as a function of task or age. Although there is obviously a strong inter-relationship between these two aspects, this deserves a more extensive discussion. For example, in relation with the previous point, if local microstructural properties predict neuronal timescales, why is it that timescale changes during the delay seem to be ubiquitous (or are they)? And why should such changes (that are overall in the same range) correlate with subject performance in the PFC but not in the other areas? How does this relate to the aging observations? Although this discussion is bound to be speculative. It is important in order to strengthen the link between these two independent avenues of the paper, and to enrich the discussion about the functional role of these dynamic changes in neuronal timescales.

iv) The paper does not consider oscillations, which is fine, but the reader is left wondering how oscillations affect these time-scales. Discussion on this aspect would be useful.

4) Comments on figures, statistics and clarification:

i) Are the rho correlation values corrected for the expected value of the surrogate distribution? That is are they significantly overestimated due to the dependent samples issue? In this case it is recommended to report the corrected correlation values, rather than the raw correlation values.

ii) The correlation performed in Figure 4D is a bit unclear. Are the different dots+lines participants, or is this a binned correlation? If it is a binned correlation, does that represent a problem for the correlation analysis?

iii) It would be useful in Figure 1/2 to show some examples of ECOG time-scales related to the actual underlying signals and PSDs, rather than just illustrating the technique on simulated data, so that the validity of the technique can be judged.

iv) In general it would be useful to report carefully the N's and the dataset that is used for each analysis, because it is easy to get lost in what is what as the authors analyze a huge number of datasets.

v) The technique of removing spatial autocorrelations that influence the p-value appears to be sophisticated and well done. If the authors need another validation, one way of doing this would be to use a cross-validation prediction approach where a subset of subjects is used for training and the other subjects are used for testing.

vi) What are "these" limitations in the subsection “Neuronal timescale can be inferred from frequency domain”?

vii) Figure 1E: how is r2=1 when the dots do not fall on the line?

viii) The description of the methods needs be improved. For example, "we can estimate neuronal timescale from the 'characteristic frequency'" which implies a peak in the spectrum. Yet in the next sentence they write that they extract timescale from aperiodic components.

ix) Subsection “Synaptic and ion channel genes shape timescales of neuronal dynamics”: Are these markers also correlated with cell packing density? If so, it's possible that denser neural networks have longer timescales.

x) Relatedly, how strongly inter-correlated are these genetic markers across the cortex? The authors mostly take a mass-univariate approach except for showing gene-PC1 in Figure 3A. There isn't enough information shown to evaluate whether the top PC is suitable, or whether this PC comprises many/all gene contributions or is driven by a small number, etc.

xi) The modeling results seem to be missing. They appear as a schematic in Figure 1 and are mentioned in the Materials and methods section. Was this model actually used somewhere?

xii) In Figure 2B, some T1w/T2w values are above values of 2, which is not standard. Likewise, several outliers can be observed. This might have impacted the estimation of the regression slope. This slope currently matches the one from Burt et al., 2018, although the data point distribution is different.

xiii) Figure 4B is contradicting Figure 2C as the evidenced timescale hierarchy is different (comparing PC, PFC and OFC). Please explain.

xiv) Figure 4B and C, please show actual data points and justify parametric tests.

xv) Figure 4C: how consistent is the increase in delay period timescales across areas within each subject. In other words, is this a general property of the brain, task-related effects resulting in a non-specific adjustment in neuronal timescales or are there regional differences in the reported increase (you might want to exclude the PFC from the analysis to remove task related effects).

xvi) Given the described age-related effect, did the authors check that the different databases they used sampled from subjects with the same age distribution?

xvii) Legend of Figure 1 is not self-explanatory and a lot of the symbols and information plotted in the figures are not explained. Unfortunately, this information is also missing from the Results section.

5) General dense writing style and clarity:

The manuscript is written to be dense yet terse, which makes it harder to read, particularly given the complexity of the analyses. It feels like it was written for a journal with extreme word limitations. The manuscript would be overall improved if the authors would "loosen their belt" and explain the findings and methods in more detail. Figure legends should be more self-explanatory. Quite often, figure detail description and contextual information are missing both from the text and the figures. This also applies to the supplementary figures.

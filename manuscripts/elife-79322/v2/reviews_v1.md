# Peer review - Round 1

Editors:
- Martin Vinck, https://ror.org/00ygt2y02 Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79322.sa0](https://doi.org/10.7554/eLife.79322.sa0)

This is an important paper which shows how high-density neurophysiological recordings in non-human-primates can be used to identify inter-neuronal interactions based on cross-correlations. This provides valuable insights such as the dependence of correlations on vertical distance and orientation tuning. Overall the techniques used here are compelling and set a standard for recordings in non-human-primates. The paper is of interest for a broad audience of neuroscientists that performs electrophysiological recordings or is interested in functional interactions among neuron pairs.


---

# Peer review - Round 1

Editors:
- Martin Vinck, https://ror.org/00ygt2y02 Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79322.sa1](https://doi.org/10.7554/eLife.79322.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Functional Connections Among Neurons within Single Columns of Macaque V1" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jens Kremkow (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Although the paper does provide rich information on interactions within local cortical circuits, the main weakness of the paper is using the term "functional connection" in an imprecise manner. Cross-correlograms (CCG) of spike trains of pairs of neurons show different shapes depending on the underlying connectivity and not all significant peaks in CCGs reflect functionally connected neuron pairs. For example, CCGs of synaptically connected neuron pairs show a transient peak that is offset from the 0-ms lag due to the synaptic delay. CCGs with this shape thus reflect "functionally connected neuron pairs". In contrast, common inputs to pairs of neurons can induce significant peaks in CCGs, despite the fact that these neurons are only correlated but not functionally connected (e.g. Ostojic et al. 2009). Therefore, taking the shape of significant CCGs into account is important when discussing "functionally connected neuron pairs". While the authors mention this point in the paper, the term "functional connection" is nonetheless used irrespective of the CCG shapes which can be confusing to the reader. Moreover, the authors claim that the method allows identifying "1000s of functionally connected neuronal pairs". This statement is likely not fully supported by the data, evident by the fact that CCGs with the shape of mono-synaptic connections (transient and non-zero lag peak) are not among the distinct classes of CCGs shown in Figure 4.

The term "functionally connection" implies a synaptic connection between a pair of neurons. However, the majority of CCGs shown in the paper likely reflect correlated activity at fast timescales rather than true functionally connections. Because this can be confusing to readers I recommend defining the terminology more precisely and also using the term "functionally connected neuron pairs" only in cases where this is justified. This is particularly important because one claim of the paper is that Neuropixels probes allow identifying "1000s of functionally connected neuronal pairs". Please either show that indeed this large number of synaptically connected neurons is in the dataset, or change the title/abstract to match the results.

2. Likewise, it is surprising that CCGs that reflect mono-synaptic connections are not among the distinct classes shown in Figure 4? Why is that? Given the large number of tested interactions, and the claims of the paper, we would have expected that mono-synaptic connections form one of the distinct classes. It could be interesting and useful to specifically identify and study mono-synaptic connections, e.g. by employing methods reported in Liew et al. 2021 JNP, or by other approaches.

3. It is well established that fast-spiking neurons in the cortex receive stronger inputs from neurons in the local circuitry as compared to regular spiking neurons. Because fast-spiking and regular spiking neurons can be distinguished based on their spike waveform in extracellular recordings it could be interesting, but not required, to see whether this cell-type dependent connection strength is also evident in this dataset. This could add to the significance of the work and provide another angle to investigate circuit interactions. Again, this is only a suggestion.

4. It would be useful to show the CCGs in Figure 1e in a higher temporal resolution around the peak such that the lag of the peak is visible.

5. It seems odd to treat the forward and reverse correlation functions as two distinct types since the labeling is arbitrary. That is, swapping the label for the reference neuron and its partner would flip the correlation function from one category to the other. Since the choice of the reference neuron is arbitrary, it is not clear why there are two categories. Please provide justification.

6. Separate from this issue, the labeling looks erroneous to the best of our knowledge. That is, 'forward' correlation functions have more mass at negative lags. This is opposite to the conventional definition. Mass at negative lags means the partner neuron tends to fire before the reference neuron, which is not a forward connection (reference driving partner) but the opposite. Please clarify.

7. Please provide the species used.

8. Page 10: It was not obvious that the regression coefficients could be directly compared since the covariates (pair distance and r_ori) have very different magnitudes. Please clarify.

9. Please provide an explanation of how the spike sorting was done. One concern about the sharp correlation peaks is that they are artifactual, resulting from issues in Kilosort (https://github.com/MouseLand/Kilosort/issues/29). In brief, Kilosort can match the same spike waveform to two different templates, one template capturing most of the waveform shape and the second capturing the residual. This issue is discussed on the Github Kilosort page. Are the authors sure that this does not contribute to/drive the sharp peak phenomenology? One way to provide reassurance would be to provide more information on the shape and width of the sharp peaks. If they are ~1 ms wide, it seems more likely to be artifactual than biological.

10. Please provide the proportion of simple and complex neurons in the data set.

11. Discussion: The authors do a good job of discussing the limitations of correlation analysis for identifying synaptic connections. However, they refer to their R and F shapes (9% of cases) as potentially capturing such connections. Traditionally (e.g. Reid and Alonso), correlation function consistent with synaptic connections must pass a more stringent description than a simple asymmetry with respect to zero time lag. Namely, they need to have a sharp peak clearly offset from zero. This difference in stringency should be incorporated into the Discussion if the authors wish to propose that R and F types are related to connectivity.

12. Line 635: The definition of the correlation function seems different from previous work. The correlation function appears normalized by a quantity that depends on the time lag of one neuron and not the other (the denominator). Please clarify the notation.

13. Figure 2B: There is an oscillation in the marginal histogram of peak delays. This is also evident in Figure 3C. Please clarify.

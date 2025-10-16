# Peer review - Round 1

Editors:
- Sachin Deshmukh, Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51972.sa1](https://doi.org/10.7554/eLife.51972.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Spatiotemporal patterns of neocortical activity around hippocampal sharp-wave ripples" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor.

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This paper combines wide field optical recording techniques with electrophysiology to study cortico-hippocampal interactions surrounding the hippocampal sharp wave-ripple (SWR). The timing of activation and deactivation of cortex appears continuously distributed with a bias for cortical activation before SWR. Within the cortex, activation appears to propagate from medial to lateral/sensory regions. Interestingly, the propensity to have SWRs within a short window ("bundles") is correlated with the hippocampus activation before cortical activation.

The reviewers agree that this work uses a novel and potentially powerful experimental approach to address important questions of hippocampal-cortical communication. The manuscript is clearly written and reflects a substantial scientific work. However, the reviewers also raise several substantial concerns about the quantitative statistics used and interpretation of the observed results, which must be addressed. The reviewers also suggest new analyses that will significantly increase the relevance and appeal of the present study.

Essential revisions:

1) The findings of hippocampal MUA activity before and after SWRs correlating with neocortical activation is very sensitive to the accuracy of SWR detection. If SWR power is elevated before/after a detected SWR but doesn't pass the detection threshold, the observed MUA may simply reflect hippocampal SWR-related firing. In this case cortical activity coordinated in time would be expected. This could influence the results of both Figure 5 and Figure 6. The authors should analyze their data to show that this is not the case or reinterpret the findings.

2) There are a number of cases where it seems like inappropriate statistical tests were performed in a way that could strongly influence the results. For example, in Figures 2ciii, 2dii, 3cii. It seems like one-sided paired t-tests were conducted between a chosen subset of the groups. This is faulty for a number of independent reasons: pairwise instead of a group test, selective choosing of the groups without a-priori strong reasons to do so, inexplicable use of one-tail test even to make claims explicitly not permitted by the use of one-sided tests (e.g. claiming that "visual (activation is) followed by the medial (activation)" using medial vs visual one-sided test showing no statistical significance), no correction for multiple comparisons, small sample size for a t-test. Repeated-Measures ANOVA or other appropriate tests should be used throughout. Later in the paper the authors switch to non-parametric tests, but it is unclear why.

3) The idea of a loop-like interaction between neocortex and hippocampus during SWS ripples is not new. For example, it has been similarly expressed by Rothschild et al., 2017 and 2018, and recently summarized by Klinzing et al., 2019. This literature needs to be more elaborately integrated. It would be of great interest here to actually demonstrate this loop in the data (i.e., to see if cortical activation that triggers ripples also triggers delayed cortical activations). Ideally, this analysis should be separate for naturally sleeping animals (which optimally were exposed to a novel environment before imaging) and anesthetized animals.

4) The authors could greatly enhance the impact of their work by adding an analysis of the neocortical slow oscillation (SO). Ripples are well known to more likely occur in the down-to-up transition of the SO, and the SO down-state is often considered a global frame resetting activity also in hippocampal networks. Indeed, the authors on several occasions discuss the possibility that the decreases and increases in MUA they observe around ripples represent down and up states of the SO. Why don't they add the respective data and analyses?

5) A key finding in this manuscript is that changes in neocortical activity often precede hippocampal SWRs and the potential interpretation that this may support cortical biasing of hippocampal reactivation. While the data seems to support this proposal, the authors downplay important previous studies that have described such findings (in some cases with neural population data with single-cell resolution) and models. Sirota et al., 2003, reported somatosensory cortical firing preceded SWRs and suggested a cortical influence on hippocampal reactivation; Wang and Ikemoto, 2016, found a similar pattern in ACC; Rothschild et al., 2017, identified a cortical-hippocampal-cortical loop of communication around SWRs and proposed a related model (Rothschild, 2018); Recent human studies found a similar pattern of communication (Norman et al., 2019, Viet-Ngo et al., 2019, Helfrich et al., 2019). These previous reports of this phenomenon should be highlighted.

6) The functional significance of a key result in the paper- the enhanced SWR-related activity in RSC as compared to other cortical regions- is unclear. On the one hand, we know that RSC receives direct input from hippocampus whereas other regions do not. On the other hand, degree of fluorescence does not necessarily tell us much about the functional role of the communication. So what do we learn from this finding beyond a reflection of known anatomy?

7) Given that the important physiological signatures differ across the groups (Figure 2—figure supplement 1), the reviewers questioned the appropriateness of grouping highly different experimental groups/conditions, such as in VSD/glutamate imaging and natural sleep/anesthesia. Do the authors have more data that can enable them to separately analyze these groups? If not, they must provide appropriate justification for the grouping and demonstrate that the different groups pooled together did not perform differently from each other in specific analyses.

8) Figure 1—figure supplement 1 shows recording electrode at the CA1/subiculum boundary, and not unambiguously in CA1 as claimed by the authors. Authors need to show the distribution of all LFP recording electrodes. On a related note, was there any functional mapping performed to demarcate the boundaries between different cortical regions, or are the boundaries based on the atlas?

9) A number of methodological restrictions need to be clearly discussed. First, wide field imaging did not cover prefrontal cortex. In particular, medial prefrontal cortex is an area most strongly connected to the hippocampus and there are a number of previous studies showing particular temporal "peri-ripple" relationships of activity between mPFC and hippocampus. The retrosplenial cortex being the more important hub for sleep dependent consolidation (than mPFC) very much fits with some of the human fMRI literature (e.g., Darsaud et al., 2011, J Cogn Neurosci), although such conclusions unfortunately cannot be made based on the present data. While cortical activity is assessed over rather large areas, hippocampal ripples are recorded from just one electrode site. Considering the local (and travelling) nature of ripples, the temporal relationship of ripples to neocortical activity might essentially depend on where in the hippocampus they are generated/recorded. A related conceptual issue (to be discussed) is that local memory replay mainly occurs during the ripple, and not before or after.

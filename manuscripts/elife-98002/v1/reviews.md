# Peer review - Round 1

Editors:
- Brice Bathellier, Centre National de la Recherche Scientifique France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98002.3.sa0](https://doi.org/10.7554/eLife.98002.3.sa0)

This study compiles a wide range of results on the connectivity, stimulus selectivity, and potential role of the claustrum in sensory behavior. While most of the connectivity results confirm earlier studies, this valuable work provides incomplete evidence that the claustrum responds to multimodal stimuli and that local connectivity is reduced across cells that have similar long-range connectivity. The conclusions drawn from the behavioral results are weakened by the animals' poor performance on the designed task. This study has the potential to be of interest to neuroscientists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98002.3.sa1](https://doi.org/10.7554/eLife.98002.3.sa1)

Summary:

The paper by Shelton et al investigates some of the anatomical and physiological properties of the mouse claustrum. First, they characterize the intrinsic properties of claustrum excitatory and inhibitory neurons and determine how these different claustrum neurons receive input from different cortical regions. Next, they perform in vitro patch clamp recordings to determine the extent of intraclaustrum connectivity between excitatory neurons. Following these experiments, in vivo axon imaging was performed to determine how claustrum-retrosplenial cortex neurons are modulated by different combinations of auditory, visual, and somatosensory input. Finally, the authors perform claustrum lesions to determine if claustrum neurons are required for performance on a multisensory discrimination task

Strengths:

An important potential contribution the authors provide is the demonstration of intra-claustrum excitation. In addition, this paper does provide the first experimental data where two cortical inputs are independently stimulated in the same experiment (using 2 different opsins). Overall, the in vitro patch clamp experiments and anatomical data provide confirmation that claustrum neurons receive convergent inputs from areas of frontal cortex. These experiments were conducted with rigor and are of high quality.

Weaknesses:

The title of the paper states that claustrum neurons integrate information from different cortical sources. However, the authors did not actually test or measure integration in the manuscript. They do show physiological convergence of inputs on claustrum neurons in the slice work. Testing integration through simultaneous activation of inputs was not performed. The convergence of cortical input has been recently shown by several other papers (Chia et al), and the current paper largely supports these previous conclusions. The in vivo work did test for integration, because simultaneous sensory stimulations were performed. However, integration was not measured at the single cell (axon) level because it was unclear how activity in a single claustrum ROI changes in response to (for example) visual, tactile, and visual-tactile stimulations. Reading the discussion, I also see the authors speculate that the sensory responses in the claustrum could arise from attentional or salience related inputs from an upstream source such as the PFC. In this case, claustrum cells would not integrate anything (but instead respond to PFC inputs).

The different experiments in different figures often do not inform each other. For example, the authors show in Figure 3 that claustrum-RSP cells (CTB cells) do not receive input from the auditory cortex. But then, in Figure 6 auditory stimuli are used. Not surprisingly, claustrum ROIs respond very little to auditory stimuli (the weakest of all sensory modalities). Then, in Figure 7 the authors use auditory stimuli in the multisensory task. It seems that these experiments were done independently and were not used to inform each other.

One novel aspect of the manuscript is the focus on intraclaustrum connectivity between excitatory cells (Figure 2). The authors used wide-field optogenetics to investigate connectivity. However, the use paired patch clamp recordings remains the ground truth technique for determining the rate of connectivity between cell types, and paired recordings were not performed here. It is difficult to understand and gain appreciation for intraclaustrum connectivity when only wide-field optogenetics is used.

In Figure 2, CLA-rsp cells express Chrimson, and the authors removed cells from the analysis with short latency responses (which reflect opsin expression). But wouldn't this also remove cells that express opsin and receive monosynaptic inputs from other opsin expressing cells, therefore underestimating the connectivity between these CLA-rsp neurons? I think this needs to be addressed.

In Figure 5J the lack of difference in the EPSC-IPSC timing in the RSP is likely due to 1 outlier EPSC at 30ms which is most likely reflecting polysynaptic communication. Therefore, I do not feel the argument being made here with differences in physiology is particularly striking.

In the text describing Figure 5, the authors state "These experiments point to a complex interaction ....likely influenced by cell type of CLA projection and intraclaustral modules in which they participate". How does this slice experiment stimulating axons from one input relate to different CLA cell types or intra-claustrum circuits? I don't follow this argument.

In Figure 6G and H the blank condition yields a result similar to many of the sensory stimulus conditions. This blank condition (when no stimulus was presented) serves as a nice reference to compare the rest of the conditions. However, the remainder of the stimulation conditions were not adjusted relative to what would be expected by chance. For example, the response of each cell could be compared to a distribution of shuffled data, where time-series data are shuffled in time by randomly assigned intervals and a surrogate distribution of responses generated. This procedure is repeated 200-1000x to generate a distribution of shuffled responses. Then the original stimulus triggered response (1s post) could be compared to shuffled data. Currently, the authors just compare pre/post mean data using a Mann Whitney test from the mean overall response, which could be biased by a small number of trials. Therefore, I think a more conservative and statistically rigorous approach is warranted here, before making the claim of a 20% response probability or 50% overall response rate.

Regarding Figure 6, a more conventional way to show sensory responses is to display a heatmap of the z-scored responses across all ROIs, sorted by their post-stimulus response. This enables the reader to better visualize and understand the claims being made here, rather than relying on the overall mean which could be influenced by a few highly responsive ROIs.

For Figure 6 it would also help to display some raw data showing responses at the single ROI level and the population level. If these sensory stimulations are modulating claustrum neurons, then this will be observable on the mean population vector (averaged df/f across all ROIs as a function of time) within a given experiment and would add support to the conclusions being made.

As noted by the authors, there is substantial evidence in the literature showing that motor activity arises in mice during these types of sensory stimulation experiments. It is foreseeable that at least some of the responses measured here arise from motor activity. It would be important to identify to what extent this is the case.

All claims in the results for Figure 6 such as "the proportion of responsive axons tended to be highest when stimuli were combined" should be supported by statistics.

For Figure 7, the authors state that mice learned the structure of the task. How is this the case, when the number of misses are 5-6x greater than the number of hits on audiovisual trials (S Fig 19). I don't get the impression that mice perform this task correctly. As shown in Figure 7I, the hit rate is exceptionally low on the audiovisual port in controls. I just can't see how control and lesion mice can have the same hit rate and false alarm rate yet have different d'. Indeed, I might be missing something in the analysis. However, given that both groups of mice are not performing the task as designed, I fail to see how the authors claim regarding multisensory integration by the claustrum is supported. Even if there is some difference in the d' measure, what does that matter when the hits are the least likely trial outcome here for both groups.

In the discussion, it is stated that "While axons responded inconsistently to individual stimulus presentations, their responsivity remained consistent between stimuli and through time on average...". I do not understand this part of the sentence. Does this mean axons are consistently inconsistent?

In the discussion the authors state their axon imaging results contrast with recent studies in mice. Why not actually do the same analysis that Ollerenshaw did, so this statement is supported by fact? As pointed out above, the criteria used to classify an axon as responsive to stimuli was very liberal in this current manuscript.

I find the discussion wildly speculative and broad. For example, "the integrative properties of the CLA could act as a substrate for transforming the information content of its inputs (e.g. reducing trial to trial variability of responses to conjunctive stimuli...)". How would a claustrum neuron responding with a 10% reliability to a stimuli (or set of stimuli) provide any role in reducing trial to trial variability of sensory activity in the cortex?

Comments on the latest version: The authors have revised the manuscript, by adding 1 new supplementary figure, and some minor changes to the text. Overall, my comments regarding the manuscript were not sufficiently addressed. Here is one example:

The authors don't seem to be taking the comments regarding the statistical significance of the sensory responses seriously. If there is a response in 10% of the axons in the blank condition, and a 11 % response in the auditory stimulation, then that means that it is more accurate to say that 1% of axons actually respond to auditory stimulation. "leaving to reader to make their own decisions" as the authors suggest, but then having authors read text such as "All modalities could evoke responses in at least some claustrum neurons", is misleading because no attempt was made to correct for a chance level of detection that is clearly observed in the blank condition. Another interpretation of the authors data would be that in the case of the auditory/visual/somatosensory combined stimuli resulted in 21%(observed) - 10% (blank) = 11% of axons. Therefore, a conclusion that more accurately reflects the data would be that 89% of claustrum axons do not respond, even when the mouse received multisensory stimuli. I tried to get the authors to run some basic stats to more accurately test the true degree of responsiveness, but these changes did not appear in the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98002.3.sa2](https://doi.org/10.7554/eLife.98002.3.sa2)

Summary:

In this manuscript, Shelton et al. explore the organization of the Claustrum. To do so, they focus on a specific claustrum population, the one projecting to the retrosplenial cortex (CLA-RSP neurons). Using elegant technical approach, they first described electrophysiological properties of claustrum neurons, including the CLA-RSP ones. Further, they showed that CLA-RSP neurons (1) directly excite other CLA neurons, in a 'projection-specific' pattern, i.e. CLA-RSP neurons mainly excite claustrum neurons not projecting to the RSP and (2) received excitatory inputs from multiple cortical territories (mainly frontal ones). In an effort to confirm the 'integrative' property of claustrum networks, they then imaged claustrum axons in the cortex during single- or multi-sensory stimulations. Finally, they investigated the effect of CLA-RSP lesion on performance in a sensory detection task.

Strengths:

Overall, this is a really good study, using state of the art technical approaches to probe the local/global organization of the Claustrum. The in-vitro part is impressive, and the results are compelling.

Weaknesses:

One noteworthy concern arises from the terminology used throughout the study. The authors claimed that the claustrum is an integrative structure. Yet, integration has a specific meaning, i.e. the production of a specific response by a single neuron (or network) in response to a specific combination of several input signals. In this study, the authors showed compelling results in favor of convergence rather than integration. On a lighter note, the in-vivo data are less convincing, and do not entirely support the claim of "integration" made by the authors.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98002.3.sa3](https://doi.org/10.7554/eLife.98002.3.sa3)

Public review:

The claustrum is one of the most enigmatic regions of the cerebral cortex, with a potential role in consciousness and integrating multisensory information. Despite extensive connections with almost all cortical areas, its functions and mechanisms are not well understood. In an attempt to unravel these complexities, Shelton et al. employed advanced circuit mapping technologies to examine specific neurons within the claustrum. They focused on how these neurons integrate incoming information and manage the output. Their findings suggest that claustrum neurons selectively communicate based on cortical projection targets and that their responsiveness to cortical inputs varies by cell type.

Imaging studies demonstrated that claustrum axons respond to both single and multiple sensory stimuli. Extended inhibition of the claustrum significantly reduced animals' responsiveness to multisensory stimuli, highlighting its critical role as an integrative hub in the cortex.

However, the study's conclusions at times rely on assumptions that may undermine their validity. For instance, the comparison between RSC projecting and non-RSC projecting neurons is problematic due to potential false negatives in the cell labeling process, which might not capture the entire neuron population projecting to a brain area. This issue casts doubt on the findings related to neuron interconnectivity and projections, suggesting that the results should be interpreted with caution. The study's approach to defining neuron types based on projection could benefit from a more critical evaluation or a broader methodological perspective.

Nevertheless, the study sets the stage for many promising future research directions. Future work could particularly focus on exploring the functional and molecular differences between E1 and E2 neurons and further assess the implications of the distinct responses of excitatory and inhibitory claustrum neurons for internal computations. Additionally, adopting a different behavioral paradigm that more directly tests the integration of sensory information for purposeful behavior could also prove valuable.

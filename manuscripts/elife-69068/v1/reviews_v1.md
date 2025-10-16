# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69068.sa1](https://doi.org/10.7554/eLife.69068.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper addresses the important topic of comparing the data obtained from standard electrophysiology recordings to calcium imaging in a controlled experimental set up [it does ephys and 2p in different mice, perhaps not ideal but very useful for real comparisons of different datasets]. Previously, most comparisons have been performed at the level of single cells with simultaneous ephys and imaging, and these comparisons have not addressed the topics discussed here, which are highly relevant to the field. The discussion and analysis of pros and cons to each method are fair and valuable, in particular as the shortcomings of electrophysiology are sometimes not discussed in the literature.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Reconciling functional differences in populations of neurons recorded with two-photon imaging and electrophysiology" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing/Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While all the reviewers saw great merit in the approach, there are several flaws large and small that require a thorough reworking of the paper and significant new analyses that could substantially change the main conclusions. Such a thoroughly reworked paper taking into account all the reviewer comments could be submitted as a new submission to eLife.

Reviewer #1:

In this manuscript, Siegle, Ledochowitsch et al. compare two large datasets of neurons recorded by electrophysiology and two-photon calcium imaging respectively. They start by showing that there are substantial differences in the responsiveness and selectivity of the neurons, but those differences mostly go away after taking into account the details of these methods. This work is very useful information for anyone using ephys or ophys to record neurons from brains, which includes a lot of labs. It can become a priceless reference for everyone worried about what their data actually represents, and there is a lot of concern going around these days, especially as the recording methods are being scaled up very rapidly.

The paper and the analysis are very well written and convey all the information we need. I have almost no minor or major comments, but I do have one very serious concern. The paper is not really comparing ephys to ophys, but comparing ephys to L0-deconvolution of calcium imaging data. While I believe deconvoluton is absolutely crucial for interpreting 2p data correctly, the method chosen by the authors – L0 deconvolution – is problematic because it will result in exactly the kind of selectivity and responsiveness effects reported here. This is not merely a possibility, but a guaranteed consequence of L0-deconvolution because this method by design returns a very large fraction of zeros, effectively only picking up the "top of the iceberg" from the calcium traces.

The solution to this problem is clear: adjust the regularization constant in the L0 deconvolution all the way down to 0 and see how your results change. The Jewell et al. method will probably stop working correctly before you get to 0, in which case please use un-penalized OASIS, which is deconvolution with no regularization. Suite2p provides wrappers to do this with everything turned off (no parameter estimation and no regularization), and there are papers out there showing that the optimal value of the regularization constant is actually 0 for some ground truth data.

I would be extremely surprised if the results don't change substantially, and I am very curious to know exactly how they change.

Reviewer #2:

This paper addresses the important topic of comparing the data obtained from standard electrophysiology recordings to calcium imaging in a controlled experimental set up. Previously, most comparisons have been performed at the level of single cells with simultaneous ephys and imaging, and these comparisons have not addressed the topics discussed here, which are highly relevant to the field. Overall the paper and results are well presented. The conclusions and interpretations follow from the data presented. The discussion and analysis of pros and cons to each method are fair and valuable, in particular as the shortcomings of electrophysiology are sometimes not discussed in the literature. I therefore think this paper will be a valuable addition to the field. However, there are some shortcomings that need to be noted clearly and some potential extensions that could further enhance the impact of the work.

1. The major shortcoming of the paper is that it is focused on only a single labeling strategy for calcium imaging, namely using transgenic mice with the GCaMP6f indicator. The labeling strategy and indicator likely have very major impacts on the data obtained from calcium imaging. Specifically, expression levels can vary depending on the labeling approach, such as between viral methods and transgenic methods, which can affect the signal-to-noise ratio and the ability to detect single action potentials. Also, different indicators will have different detection thresholds. Here GCaMP6f was used, which is relatively insensitive, whereas a choice of GCaMP6s would have resulted in more detection of single action potentials. It is well known among experimenters in the field that viral labeling generally gives substantially higher signal-to-noise ratio compared to transgenic methods, including the transgenic methods used in this paper. This can be seen in some of the single-spike detection rates shown in the original GCaMP6 paper compared to subsequent efforts from the Allen Institute and others using transgenic mice. The same is true for GCaMP6s vs. GCaMP6f as was shown clearly in the original GCaMP6 paper. It is therefore the case that the differences between ephys and imaging could be different if viral methods were used and if GCaMP6s or GCaMP7 variants were used for the experiments. This is really important and currently the paper does not put emphasis on this point. The danger is that readers will think these results generalize to all calcium imaging studies, which I think is unlikely to be true, at least in the details, but perhaps in the general findings too. Obviously it is too much work to repeat all the experiments with a different indicator and/or labeling strategy. But, this is a critical point that must be addressed and presented very clearly. The authors must mention in the abstract that they used GCaMP6f and transgenic mice because these details are critical to the specifics of their findings. Furthermore, they should provide a detailed section in the discussion that points out that the results could vary substantially if different labeling methods and/or indicators are used. These issues raise another level of details regarding comparing studies, and it is critical that the authors discuss them thoroughly.

2. I very much liked the forward model to transform spikes to calcium events. I think it would also be useful to try deconvolution to transform calcium to spikes as well. I agree with the authors that this is an under-constrained problem without an ideal solution. However, there are common methods in the field that are frequently applied in calcium imaging papers. I suggest the authors use a common deconvolution approach and compare how this impacts the comparison between ephys and calcium imaging. I suggest this because most calcium imaging studies now analyze deconvolved data instead of the calcium events.

3. One of the very important findings is that the distribution of tuning preferences look to be similar between methods, for example for temporal frequency in Figure 2G. I think this point should be emphasized even more to point out the things that are similar between methods. I would also like to see these same distributions for other tuning parameters, such as spatial frequency, orientation, direction, and so on. It was not clear why the authors only showed temporal frequency.

4. It would be helpful to see additional metrics for selectivity beyond lifetime sparseness. I like the lifetime sparseness metric, but there are others that are more commonly used in the field and might help the reader to see. As one possibility, it might be helpful to see an orientation selectivity index as a comparison between ephys and calcium imaging data. I understand that this is not a general metric, but it is common in the field and thus potentially helpful.

5. The responsiveness measure seems reasonable, but it is based on a seemingly arbitrary threshold of 25% of trials with responses above 95% of the baseline period. What happens if this 25% threshold is varied? In addition, other measures of response reliability might be helpful. For example, trial-to-trial variability might be an interesting and important parameter to quantify, such as using the coefficient of variation or other metrics.

6. My understanding is that the calcium imaging data were segmented into cells using morphology based methods. This is not the current standard in the field. Most papers now use correlations in the fluorescence timeseries to help with segmentation. Is the segmentation obtained by the authors consistent with the segmentation obtained with more standard methods in the field, such as the cells obtained with Suite2P or CNMF? It might also be helpful for the authors to discuss how cell segmentation with calcium imaging, including neuropil contamination/subtraction, could impact the metrics they studied. The analysis of potential spike sorting artifacts or biases was informative, and something analogous could be, at the least, discussed for calcium imaging segmentation.

7. I do not like the introduction of the term 'ophys'. To me, this just adds another term to the field and likely results in more confusion rather than sticking with normal nomenclature in the field. I do not see what it adds over referring to the data as calcium imaging or two photon calcium imaging. If anything 'ophys' seems less precise because it could include voltage imaging too.

Reviewer #3:

This paper makes a step towards addressing a need in the community: understanding if measurements made with electrophysiology (ephys) and 2-photon imaging (2p) give the same result, and if not, in which way they differ and why. The best way to compare the two would be to do ephys and 2p at the same time (e.g. Wei,.… Druckmann, bioRxiv 2019). Next best would be to do them at different times but in the same neurons (which could be done here, because many of the ephys mice express GCaMP6f). This paper uses the third best approach: it does ephys and 2p in different mice. Not ideal but a useful exercise given the remarkably vast datasets.

The paper however contains some flawed analyses and meanders away from the main focus. It could be refocused e.g. by keeping the top half of Figure 1; a revised Figure 2; Figure 4; the top half of Figure 5, and a panel similar to Figure 4E, showing that once biases in cell selection are taken care of, the fraction of responsive neurons to different stimuli becomes the same. The current Figures 2 and 7 show analyses that are simply not ok, as explained below.

(1) The paper starts by making a flawed comparison between 2p and ephys data (Figure 2). One can't directly compare the output of ephys, i.e. spike trains that are sequences of 1s and 0s, with the deconvolved output of 2p, i.e. firing rates that range over 4 orders of magnitude. To compare those two measures of activity they must have the same units: either compute firing rates with common bin size (by binning the spike trains and resampling the deconvolved firing rates) or convolve the spike trains with a filter to match the GCaMP timecourse (as in Figure 4).

(2) Based on Figure 2, the paper finds two discrepancies: the 2p dataset has neurons with higher stimulus selectivity (Figure 2H) but a lower fraction of responsive neurons (Figure 2F). The first discrepancy disappears once the spikes measured with ephys are convolved with a reasonable filter that models the impulse response of GCaMP (Figure 4I). The second discrepancy remains (Figure 4E) but it disappears (does it? this is not fully shown) if one considers that the ephys data is biased towards neurons that fire more.

(3) The analysis of cell selection bias takes 3 long figures (Figure 5,6, and 7) without delivering the desired result: we need to see a figure with the same format as Figure 1F and Figure 4I, showing a match between the two techniques -- if such a match can be obtained.

(4) To address sampling bias introduced by the 2p processing pipeline, the paper explores the effect of setting a threshold at a given firing rate (p 13). However, the sampling bias may be more closely related to the procedures used to identify neurons in the 2p images. It seems that ROIs here are based on morphological properties without further manual curation (de Vries et al., 2020). This wide net will increase the total number of neurons, and thus likely decrease the fraction of responsive neurons, as pointed out by the same group (Mesa et al., bioRxiv). Subsampling using event rate reduces rather than increases overall selectivity, but in the Mesa et al. preprint, subsampling using a higher threshold for coefficient of variation (CV) increases selectivity with fewer neurons. So, at the very least, consider subsampling using CV to see whether this increases similarity between recording methods.

(5) Another reason for high sparseness/selectivity in the 2p data could be the deconvolution algorithm. Indeed L0 deconvolution, and L0 regularization in general, are intended to sparsify (e.g. as described in Pachitariu et al., 2018 J Neurosci). This could be dealt with by re-analyzing the dataset with different deconvolution algorithms, or vary the parameter λ governing the L0/L1 trade-off. Or perhaps better, one could make synthetic 2p data by convolving the ephys data and then deconvolve it to estimate firing rates. If they become sparser, there is a problem.

(6) The statistical test of Jensen-Shannon distance seems to find significant differences also where there barely are any. In some analyses (e.g. Figure 4I) the distributions look highly similar, yet are still judged to be statistically distinct. Is there an instance (e.g. within the same modality) where the Jensen-Shannon distance would ever be small enough to fail to reject the null? For example, by taking two sets of ephys data obtained from the same population in two different days.

(7) Figure 7 shows an unconvincing attempt at clustering neurons. It rests on a clustering process that seems dubious (t-SNE is geared to show data as clusters) and would require a whole paper to be convincing. It hinges on the existence and robustness of clusters of cells based on responses to a variety of stimuli. If there are clusters of that kind, that's a major discovery and it should get its own paper. But showing it convincingly would likely require long recordings (e.g. across days). It is not the kind of thing one shows at the end of a paper on a different topic. What we want at the end of this paper is to know whether the correction for selection bias explains the discrepancy shown in the simple analysis of Figure 4.

(8) The separate analysis of different visual areas adds complexity without delivering benefits. There is little reason to think that the relationship between spikes and calcium is different in neighboring cortical areas. If it is, then it's an interesting finding, but one that will require substantial burden of proof (as in simultaneous recordings). Otherwise it seems more logical to pool the neurons, greatly simplifying the paper. (This said, it does seem somewhat useful to separate the visual areas in Figure 4G, as they do have some differences in selectivity).

(9) The paper would be much stronger if it included an analysis of GCaMP6s data in addition to GCaMP6f. Are the same findings made with those mice?

(10) Are there consistent differences in reliability of the responses (repeatability across trials of same stimuli) in the two measures, and if so, does the convolution and selection biases explain these differences.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Reconciling functional differences in populations of neurons recorded with two-photon imaging and electrophysiology" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese as the Senior and Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers found the paper much improved but there is still some concern that the message is somewhat muddled and that readers are not being given the guidance they need to treat their data appropriately. In particular, please make sure readers come away with guidance on what to do with their data; please discuss this more and clarify this issue throughout the text. Recommendations for the Authors of Reviewer #1 will be helpful.

Reviewer #1:

My earlier review had suggested ways to make this paper briefer and more incisive so that it would have a clearer message. To summarize my opinion, the message would have been clearer if the paper started by listing the differences between the two methods (using an apples-to-apples comparison from the get-go) and then introduced the forward model and step by step indicated what one needs to do to make the differences go away. I would not introduce in the last figure a new result/analysis (the clusters of cell types) and use that one to illustrate the success of the forward model. I would drop that figure because it's a dubious (potentially interesting) result that would need its own paper to be convincing. By the time we arrive at that figure we should have established how we will judge a model's capabilities, rather than throw more data at the reader. This said, there are certainly many ways to write a paper, and it should be ok to ignore one reviewer's opinion on how to arrange an argument.

My main suggestion is to give the paper another look and try to convey a clearer message. For instance, take this sentence in abstract: "However, the forward model could not reconcile differences in responsiveness without sub-selecting neurons based on event rate or level of signal contamination." If one took out the double negative (not/without) one would end up with a positive result: the forward model can indeed reconcile those differences, provided that one focuses on neurons with low contamination and sets a threshold for event rate. Writing things this way would actually honor the goal stated in the title: "Reconciling functional differences…". Overall, it would be good if readers could come out with a clearer understanding of what they should do to their 2p data to make it more similar to ephys data, and what aspects they can trust and what aspects they cannot.

Reviewer #2:

Looks great to me, thanks for doing the extra analyses from Figure 3!

Reviewer #3:

I support publication of this paper and think it will be a nice addition to the field and of interest to a large number of readers. The paper is clearly written and presented. The addition of Figure 3 and new discussion points is helpful. I do not have remaining concerns or comments.

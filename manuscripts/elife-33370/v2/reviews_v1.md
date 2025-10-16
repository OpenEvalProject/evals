# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33370.014](https://doi.org/10.7554/eLife.33370.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Large-scale two-photon imaging revealed super-sparse population codes in V1 superficial layer of awake monkeys" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David Van Essen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Anna Wang (Reviewer #2); Stanley Klein (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, Tang and colleagues use two-photon calcium imaging in awake monkeys to investigate the sparseness of responses in V1. All reviewers were enthusiastic about the manuscript, noting that it was technically novel and conceptually important for delineating how V1 encodes the visual world. For instance, 5 important advances were pointed out: (1) No previous study has provided a direct data-based quantitative measure of sparseness in terms of number of cells in the population (<0.5%). This finding demonstrates that very few cells, for a large number of stimulus types (from simple to complex), are needed to encode each stimulus. This is a conclusion that, due to limitations of sampling, could not be arrived at by existing single unit neurophysiology approaches. (2) The study presents a large number of different stimuli, both simple and complex, to a large dense population of single cells, all observed simultaneously in monkey cortex. This is an innovative way to track how all cells within a single locus of cortex respond under a large number of different conditions. (3) This study invites reconsideration of V1 as an area that encodes simple features of visual stimuli. (4) This study opens up new ideas about what a hypercolumn is. (5) Technically, this is a high quality, tour-de-force study of monkey visual cortex that few in the world can achieve.

The reviewers also pointed out several areas where the manuscript requires improvement, most notably (1) discussing the possibility that GCaMP is missing lower firing rate neurons; (2) improving the clarity and justification of the analysis methods, as well as possible alternate interpretations of current findings; (3) improving the discussion of why these findings are novel, and what are the implications for the role of V1 in visual processing, as well as for the meaning of a hypercolumn; and (5) making the figures more clear. Specific comments and suggestions follow.

Essential revisions:

1) Concerns about GCaMP5.

1a) The authors point to the linearity of GCaMP5 as an advantage of the current study. While this is correct for large enough firing rates, it fails to mention the significant iceberg effect of GCaMP5, which is clearly demonstrated in the authors previous work (only spike rates larger than 10Hz evoke detectable fluorescence changes). In the current paper, the iceberg effect is only acknowledged in passing in the Materials and methods section. This iceberg effect is a serious issue for the current study. This paper reports average firing rates between 15 and 30 Hz, which would suggest that a detection threshold of 10Hz for the calcium imaging indeed will result in an overestimation of sparseness by failing to detect weaker responses. Most of the chronic calcium indicators currently available (including GCaMP6) have this problem, so there is currently no suitable alternative. However, the shortcomings of the chosen indicator, and the resulting potential for overestimating sparseness, should be addressed much more clearly than is currently the case. In its current form the paper is misleading, because it does not acknowledge the confounds of the GCaMP nonlinearities on the sparseness measurements.

1b) One fix for this problem could be to include actual measurements of spike rates for a population of V1 neurons. While those data would suffer from sampling biases not present in the two-photon data, they would still be the strongest possible complement to this data set. Without spike data, it is basically impossible to assess how much of a problem the iceberg effect could be.

1c) Perhaps a sensitivity analysis could be performed to test different assumptions about the response distributions below the Ca signal threshold. For instance, what happens if each "non-responsive" neuron is assigned a random response between 0 and 10 spikes/s? How would the sparseness results change in that case? That type of statistical analysis could be useful to estimate or provide bounds to the error in the sparseness measurement caused by the iceberg effect.

1d) The statement that the linearity of GCaMP5 makes the sensor more suitable than GCaMP6 (which potentially saturates at higher rates) is incorrect. Determining sparseness across a population requires a determination of how many neurons are 'on' during a particular stimulus presentation, not accurate measurements of tuning functions. The same holds for determining the life-time sparseness of a neuron, which also only requires a determination of how many stimuli drive a neuron over a baseline level, not the precise tuning function.

2) Concerns about statistical/analysis methods

2a) Sparseness measures. The authors use the half-height bandwidth as a measure for sparseness. This choice is rather arbitrary and should be further justified. It would seem more plausible to count all stimuli that evoke responses that are significantly larger than the baseline. At a minimum, the authors should explore how their assessment of sparseness changes if the criterion threshold is changed (how many stimuli evoke responses that are 10%, 20% etc. of the maximum response). In general, any such measure is problematic because of the iceberg effect of GCaMP mentioned above. This also needs to be discussed more explicitly.

2b) Comparison to traditional sparseness measures. The authors assert that sparseness measures used previously (as the one by Rolls and Tovee) are not applicable here because they are sensitive to changes in baseline level. However, these previous studies used baseline subtracted firing rates to calculate sparseness. The sensitivity of the traditional measures to changes in baseline levels therefore requires further explanation.

2c) Decoding. The 2 analysis parts of the paper are somewhat disconnected. One emphasizes single cell selectivity, whereas the other emphasizes population sparseness. It might be useful to set up the idea that single cell selectivity does or does not predict population sparseness. It seems two concepts are correlated, but I could imagine that this need not be so.

The first part assesses sparseness by thresholding responses on a per neuron basis. The second part assesses decoding based on groups of neurons by thresholding the population. What happens to the decoding if the response matrix is computed with the thresholding of part 1 applied (i.e., setting all responses below the half maximum for a neuron to 0)?

Furthermore, the discussion of the decoding results should be improved. Currently, it seems to imply a rather arbitrary threshold of around 20% that is considered 'good decoding' (e.g., in the comparison of the decoding results from the top 0.5% – which are around 20-30%, and the decoding results from the bottom 0.5% – which are around 15%). Both are far from the chance level, so these statements need to be further justified.

Finally, the authors conclude that the comparison of decoding performance for top and bottom responses demonstrates that strong responses are both necessary and sufficient to transfer relevant information. This is incorrect. The sufficiency is indeed demonstrated (accepting the assertion that decoding performance above some threshold constitutes successful decoding). However, to demonstrate necessity, they would have to demonstrate that successful decoding always implies the occurrence of strong responses. This is not the same as demonstrating that weak responses do not allow 'successful' decoding.

2d) It would be interesting to compare the sparseness of responses evoked by natural images to that evoked by gratings (which in other studies have been shown to drive a large percentage of superficial V1 neurons). This would also allow a better assessment of how many neurons could potentially respond, further alleviating concerns about cell health or other properties of the imaging region (although this concern is largely addressed by the fact that most neurons respond to at least some of the images in the natural image set).

2e) A famous paper by Quiroga, Reddy, Kreiman, Koch and Fried (2005) illustrated extremely high sparsity in cells that responded to images of Jennifer Aniston and Halle Berry. I'm actually surprised that there was no mention in the present paper of that finding by Quiroga. Although a direct comparison may not be appropriate given the differences in areas, it may still be informative to ask whether the V1 cells have greater sparseness than the Jennifer Aniston cell.

Another reason for connecting to the Quiroga paper is that they also do ROC analyses, but their ROC curves look very different than those of the present paper (see point 5e below). The comparison may provide further evidence that the sparseness calculations, including the ROC calculations, were done properly.

3) Clarification of experimental methods employed.

3a) Cell count. The overall number of cells per imaging region is crucial for estimating sparseness. The ROI-definition procedure adopted by the authors appears reasonable and well justified. However, a few additional details would be useful:

- Additional images of identified cells so that the accuracy of the chosen approach can be assessed.

- How does the imaging region from monkey 2 look like?

- Which manual steps are involved in the procedure (presumably, somebody checks the identified ROIs)?

- Were all data collected on the same day? If not, how are data and cell counts combined across days? How many cells were stable across those days?

- How many of these cells are filled in versus have a ring-like label? This will help to assess how many of the included neurons are presumably healthy and should exhibit normal responses.

3b) Visual stimuli. Only the size of the stimuli are given. What are the other characteristics of the natural image set? Are they in color? Are they isoluminant with the background? What spatial frequencies and colors do they span? How different is their content? Are they part of one of the standard sets of natural images used in other studies?

The claim that single neurons respond to similar features of stimuli is not well supported and premature [“neuron 653 of monkey A was most excited when its receptive field (0.8o in diameter) covered the lower rim of the cat's 1 eye'. 'neuron 949 of Monkey A was found to be selective to an opposite curvature embedded in its preferred natural stimulus set”].

4) Points for further discussion/elaboration.

4a) The Discussion is focused on issues of sparseness. However, there are two issues that are also worth mentioning. First, this study thus provides a fresh view of what V1 is doing, one that shifts the emphasis from simple orientation selectivity to complex natural stimuli, and which gives novel perspective on how the brain encodes natural stimuli. And second, the results show that, within the span of a single hypercolumn, all stimuli presented could be largely decoded. This supports Hubel and Wiesel's original concept that a hypercolumn contains all the machinery to encode everything at a single point in space, except that the manner of encoding may be distinct from (or more complex than) the original concept of selection from amongst an array of systematically organized ocular dominance, orientation, and color columns.

4b) A very important item that should be made very clear is the last sentence of the Abstract where the authors correctly claim that this is the first paper that shows sparseness of neuronal population responses in V1 in primates. They need to point out that papers like Frouderakis et al. (2014) were in mice and papers like Quiroga, et al. (2005) were in humans but not in V1. The statement at the end of the tenth paragraph of the Results and Discussion needs to make that clear. It is such an important point that it needs to be pointed out in the Introduction and the Conclusion. Other researchers would then become aware of the power of two-photon imaging.

5) Clarification of data/analyses in the figures.

5a) I find Figure 1F and G vs. L and M description very confusing. I think this is the interpretation: For population sparseness, one expects the distribution to show that for most images only few cells respond. For single cell selectivity, one expects each cell to respond to only a few images. Somehow the description of these graphs seems garbled. [E.g. then for each picture only 0.5% of cells responded means: in Monkey A, for 250 pictures 1 cell responded; for ~200 pictures 6 cells responded; for 5 pictures 20 cells responded. Alternative interpretation of graph: 1 cell responded to 250 pictures; 6 cells responded to ~200 pictures; 20 cells responded to 5 pictures? I would not use 'half-height bandwidths'. Use 'number of cells'. Why is stimulus specificity called 'life-time sparseness'? F-G, L-M should be described better to distinguish what each is saying (single cell selectivity vs. population sparseness/redundancy). Maybe partly it is the terminology that is used.]

5b) Figure 1: Why are there points below zero in D and E?

5c) Figure 1: 'Cells 653 and 949 are colored red respectively.' Don't see this.

5d) Figure 2: 0.5% contributes 50% of information and 5% contributes to 80% of information, what are remaining cells doing?

5e) Figure 1—figure supplement 2: Item C shows ROC curves for 99 shuffled trials. The part that wasn't at all clear to me was why did you compare the results to a shuffled version of the results. And why did the shuffled data have such a high hit rate at zero false alarms. I would have thought that the shuffling would greatly reduce the hit rate. That is quite different from Quiroga's (2005) paper, which shows more normal curves with the false positive rate close to zero. If the authors are unable to use the Quiroga method then they should explain why, and why they end up with the very unusual shape for the ROC curves.

5f) Perhaps it would be helpful to the reader to have Figure 1 broken up into multiple figures. By doing that the figures would be larger with details more visible. One improvement that would be helpful for Figures1D, E would be to have the x-axis be a log axis so that the cell rank of the first 20 or so neurons would be more visible. I believe this is the plot that best demonstrates sparseness so it needs to be very clear.

I would suggest also spending substantially more effort clarifying F and F0 on which panels D and E are based. Another question is what is the role of noise for the one second intervals where the stimulus is shown? There is expected to be more noise in that interval than in the interval without the stimulus. How is that noise estimated?

5g) In connection with Figure 1—figure supplement 2 it would be useful to show A and B as histograms in addition to the way they are presently shown.

5h) I suspect Figure 2 is an important figure. However it wasn't at all clear to me how it was calculated. I did figure out that the small inset was a continuation of the large plot that stopped at 10%. I wonder of the inset could be removed if log axes were used for the x-axis and the data would go from say 0.1% to 100%. But more important is to clarify how the red and blue data were calculated.

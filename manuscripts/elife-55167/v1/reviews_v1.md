# Peer review - Round 1

Editors:
- Markus Meister, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55167.sa1](https://doi.org/10.7554/eLife.55167.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper introduces an online web site focused on evaluating different methods of spike sorting: the computational process that extracts the spiking of single neurons from a raw electrical recording of brain signals. The authors set themselves three goals: to aid scientists in selecting a spike sorter; to spur improvements to sorting algorithms; and to provide easy-to-use software packages. In an area that has been crying out for standardization this web site promises to be an invaluable resource.

Decision letter after peer review:

Thank you for submitting your article "SpikeForest: reproducible web-facing ground-truth validation of automated neural spike sorters" for consideration by eLife. Your article has been reviewed by three peer reviewers including Markus Meister as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper introduces an online resource focused on evaluating different methods of spike sorting. Spike sorting is an indispensable step in analyzing extracellularly recorded neuronal data, and there have been large advances in the software that performs this task over the past few years. The result is a large number of algorithms and no general consensus as to which of these algorithms works best in each circumstance. Add to that the large number of different recording configurations and brain regions, and the result is substantial uncertainty about which sorter to use in any given situation. The SpikeForest website and comparison framework presented here represents a major step toward addressing that problem. The site maintains data from many extracellular recordings that include ground truth spike times of single units. And it implements about a dozen different spike sorting algorithms that can be applied to the same data sets. The results are analyzed by various quality metrics and compared across spike sorters and data sets in tabular form. The site also offers a dive into the results down to the waveforms of individual sorted units. It is live and extensible both with regards to new data sets and new sorters.

The authors set themselves three goals: to aid scientists in selecting a spike sorter; to spur improvements to sorting algorithms; and to provide easy-to-use software packages. Based on experience in our research groups and some polling of some colleagues, these goals have been achieved already. The paper is very well written and offers an indispensable complement to the website. Here is the consensus review:

Essential revisions:

The paper offers little guidance for how to interpret the output of each sorter. Each of these sorters will produce a number of clusters which do not correspond to single units. Some set of quality metrics must be applied when the user decides how to interpret the sorter's output, and the authors have the opportunity to provide some guidance on that critical topic. This is mentioned as the first future direction, and we would encourage the authors to make a first effort at this in the current manuscript.

The Introduction is quite long and reads more like a review article. Please distil this section down to the key facts that a reader needs to know and move other material to Results section or Discussion section. The first figure, for example, would be better placed at the beginning of the Results section.

All of the ground truth datasets are quite short (~10 min), but standard recordings from neuronal populations can span hours. It seems likely that the number of spikes from a given ground truth unit and the number of spikes from other units has an effect on sorting accuracy. Can this impact be quantified for each sorter? Please comment on whether the results will generalize to longer data sets.

Figure 2: Given that there is space for figures, it would be helpful to show not just the overall accuracy metric, but also the false positive and negatives for each sorter. Of course, this is available on the website, but readers may want this information right away. The caption should explain the meaning of empty cells in the table.

Please add some guidance for why one might choose one performance metric versus another. False positives, for example, can be particularly problematic when assessing correlations between units, while false negatives lead to underestimates of firing rates.

The process whereby a user might take advantage of the containerized sorters could be explained more clearly. This is not the main thrust of the manuscript, but creation of these standard software environments greatly furthers the goal of reproducibility.

Results section, Discussion section and elsewhere: Which of the spike sorters have been optimized on these specific test data? This is mentioned in context of IronClust and SpyKING CIRCUS. Maybe spell out in Table 2 for each sorter how the parameters were chosen and whether they were adapted to the test sets.

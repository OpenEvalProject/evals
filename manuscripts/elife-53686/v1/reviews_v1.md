# Peer review - Round 1

Editors:
- María Isabel Geli, Institut de Biología Molecular de Barcelona (IBMB) Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53686.sa1](https://doi.org/10.7554/eLife.53686.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

You have now added an excellent discussion on the issues requested. In particular, you clearly summarize how well DASC can scale and translate across systems and most importantly, you nicely discuss key issues regarding the definition of ACs versus CCPs and the possible molecular mechanisms involved, which will certainly be useful to the community working in clathrin-mediated endocytosis. Therefore, we are pleased to inform you that your article, "DASC, a sensitive classifier for measuring discrete early stages in clathrin-mediated endocytosis", is now ready for publication in eLife.

Decision letter after peer review:

Thank you for submitting your article "DASC, a sensitive classifier for measuring discrete early stages in clathrin-mediated endocytosis" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Suzanne Pfeffer as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript by Wang and co-workers describes a new methodology to discriminate between bona fide productive Clathrin Coated Pits (CCPs) and Abortive Clathrin Coats (ACs), which the authors refer as DASC (Disassembly Asymmetry Score Classification). The assignment to CCPs and ACs is mostly based on 3 criteria: 1. the dynamics of individual clathrin structures extracted from the presumably CCP and AC populations, which follow those previously described for the corresponding structures; 2. the observation that the predicted CCP population very significantly diminishes in an AP2 mutant unable to bind PIn(4,5)P2, which was previously shown to prevent maturation of clathrin coats; and 3. the observation that the DASC-predicted CCPs acquire curvature, whereas those extracted from the AC population do not.

This method seems to reliably discriminate between productive CCPs and ACs on single color TIRF videos. Since these structures significantly overlap in terms of their maximum intensity and life span, methods that merely use these parameters on single color videos cannot automatically assign the nature of the clathrin structures. On the other hand, the experimental settings to more directly follow the recruitment of late endocytic proteins or vesicle fission itself in two color videos, are significantly more complex. Therefore, all reviewers agreed that DASC could be a useful metric to facilitate studies on the mechanisms driving maturation of clathrin structures.

As a resource paper though, a few considerations regarding the validation of the approach and the statistical treatment of the data need to be taken into account before publication:

Two reviewers indicated that further experimental validation using a more direct measurement of maturation would strongly reinforce the work. The authors use acquisition of curvature as a read-out for maturation, but a subset of ACs seem to acquire curvature anyway (Figure 3F). Preferably cargo loading, but alternatively, either acquisition of late endocytic proteins or fission itself, could be valid parameters. The authors could use already published data from their laboratory or others, if available.

Also, it will be important to clarify a number of experimental settings as well as some of the statistical treatment of the data to better define the limits of the approach:

1) The authors do a good job of characterizing d1, d2, and d3, their prominent output measures from DASC. But the authors need to convince readers of the generalizability of this metric on 2 fronts:

a) Within-condition variability. The permutations testing for differences between% CCPs in cells from the same condition in Figure 2F-G is excellent, but only captures a small component of the potential variability between cells. Figure 4B-D shows clear differences in the siControl group for each experiment, suggesting variability in the downstream output measures. What is the source of this variability? The day of the experiment? The batch of transfection? The quality of recorded images? As this is an exacting quantitative measure, understanding the sources of variability is necessary. Perhaps the authors could replicate the permutation test, but comparing across days or across transfections? Because the authors want to make this a resource, understanding variability would help to set the limits on how experiments within a dataset could be compared by future users of the resource.

b) Stability of Output Metric Distributions. The distributions for d1-3 shown in Figure 1D-F show striking differences between the proposed classes. But what do these distributions look like between cells? Are the distributions shown in this figure summaries for a single cell? Averaged across a population? Calculating CI on these distributions, or at least showing examples from different cells, would go a long way to demonstrate the variability that future experimenters using this metric should expect to see.

2) Perhaps even more important is the threshold used in the k-medoids clustering. While the OT population appears easily separable, the AC vs. CCP populations have clear overlap. Because of how clustering works, you'll always get 3 populations if you tell the algorithm to return 3 populations, regardless of how well separated these populations are. It is very clear that the peaks of these populations are well separated (as demonstrated in Figure 2D), but what of the events that lie at the boundary between the two distributions? Since differentiating ACs from CCPs is an essential task DASC will be used for, it would be very useful to see:

a) How do events at the edge of the two clusters look? Plotted in intensity per time space seems the most useful representation. Are these events at the edge discernible as AC or CCPs from one another based on an additional metric beyond d1-3 that the authors could incorporate into the clustering parameter space?

b) How robust are k-medoid thresholds for these two groups between experiments? All the clustering is done on centered and scaled data, but once scaled can we easily compared those data across conditions? This is important for understanding how to compare data between different experimental groups in the same paper, and also comparing new data gathered with this tool in the future to previously collected results.

# Peer review - Round 1

Editors:
- Lucina Q Uddin, University of Miami University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64694.sa1](https://doi.org/10.7554/eLife.64694.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript describes a longitudinal study of the adolescent structural connectome. The authors find strong effects of expansion of structural connectomes in transmodal brain regions during adolescence. They also report findings centered on the caudate and thalamus, and supplement the structural connectivity analyses with transcriptome association analyses revealing genes enriched in specific brain regions. Finally, intelligence measures are predicted from baseline structural measures. These findings help to bridge large-scale brain network configurations, microscale processes, and cognition in adolescent development.

Decision letter after peer review:

Thank you for submitting your article "An expanding manifold characterizes adolescent reconfigurations of structural connectome organization" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ben Fulcher (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This manuscript describes a longitudinal study of the adolescent structural connectome. Park et al. report on an analysis of existing semi-longitudinal NSPN 2400 data to learn how the projections of high-dimensional structural connectivity patterns onto a three-dimensional subspace change with age during adolescence. They employ a non-linear manifold learning algorithm (diffusion embedding), thereby linking the maturation of global structural connectivity patterns to an emerging approach in understanding brain organization through spatial gradient representations. The authors find strong effects of expansion of structural connectomes in transmodal brain regions during adolescence. They also report findings centered on the caudate and thalamus, and supplement the structural connectivity analyses with transcriptome association analyses revealing gens enriched in specific brain regions. Finally, intelligence measures are predicted from baseline structural measures.

This is an interesting and comprehensive set of analyses on an important topic. Overall, the figures are lovely. The sensitivity analyses are particularly commendable.

The paper is well written, the data are fantastic, and the analyses are interesting. Some suggestions and points for clarification (both theoretical and methodological) are below.

Essential revisions:

– There is not much in the introduction about why co-localized gene sets are of interest to explore. What is already known about brain development using this approach, and how does the current work fill a gap in our knowledge?

– Similarly, the introduction states that the study aims to "predict future measures of cognitive function". What cognitive functions specifically were of interest in this study, and why? No rationale or background is provided for conducting these analyses.

– The authors claim that their study examines "the entire adolescent time period", however some would argue that age 14 does not represent the earliest age at which adolescence onsets. I think it would be more accurate to say the study covers the mid to late adolescent period.

– In the results it is stated that three eigenvector explained approximately 50% of the variance in the template affinity matrix. Here it would be helpful to report exactly how much of the variance was explained by each (E1, E2, E3).

– Pubertal development occurs across the age range investigated, and affects brain structure and function. Was information on pubertal stage of participants available? Did some participants undergo changes in pubertal status from timepoint 1 to timepoint 2?

– The introduction does not mention cortical thickness much, therefore these analyses come as a bit of surprise in the results.

– As in the introduction, there is not much interpretation of the transcriptome findings in the discussion.

– For constructing the structural connectome, the Schaefer 7-network atlas was utilized. Can the authors comment on why a functional atlas (rather than a structural atlas) was used here?

– While this work touches on an important topic, ties nicely with the increasing body of papers on global brain gradients, and its overall conclusions are warranted, I am not (yet) convinced that it offers fundamentally new insights that could not have been gleaned from previous work (after all, manifold learning simply displays a shadow of the underlying patterns; if the patterns change, so does their shadow). I am also not convinced by the rationale for employing diffusion embedding: the authors state that the ensuing gradients are heritable, conserved across species, capture functional activation patterns during task states, and provide a coordinate system to interrogate brain structure and function, but that would be true for any method that adequately captures biologically meaningful variance in the structural connectivity patterns.

– The authors show that the maturational change of the manifold features predict intelligence at follow-up but did not show that intelligence itself exhibited changes that exceeded the error bounds of the regression line. Why not predict IQ change?

– The slight improvements in prediction accuracy observed after adding maturational change and subcortical features to the features at baseline will necessarily happen by adding more regression parameters and may not be meaningful.

– Interpretability and Lack of Comparison

The authors claim repeatedly that they are "capitalizing on advanced manifold learning techniques".

One could imagine an infinite number of papers that take a dataset, use a technique to extract a metric, X (e.g., eccentricity), and then write about the changes in X with some property of interest, Y (e.g., age). Given this set of papers (and the non-independence between the set of possible Xs), the reader ought to be most interested in those Xs that provide the best performance and simplest interpretation, with other papers being redundant.

Thus, a nuanced approach to presenting a paper like this is to demonstrate that the metric used represents an advance over alternative, simpler-to-compute, or clearer-to-interpret metrics that already exist.

In this paper, however, the authors do not demonstrate the benefits of their particular choice of applying a specific nonlinear dimensionality reduction method using 3 dimensions alignment to a template manifold and then computing an eccentricity metric. For example:

i. Is the nonlinearity required (e.g., does it outperform PCA or MDS)?

ii. Is there something special about picking 3 dimensions to do the eccentricity calculation? Is dimensionality reduction required at all (e.g., would you get similar results by computing eccentricity in the full-dimensional space?)

iii. Does it outperform basic connectome measures (e.g., the simple ones the authors compute)?

There is a clear down-side of how opaque the approach is (and thus difficult to interpret relative to, say, connectivity degree), so one would hope for a correspondingly strong boost in performance. The authors could also do more to develop some intuition for the idea of a low-dimensional connection-pattern-similarity-space, and how to interpret taking Euclidean distances within such a space.

– Developmental Enrichment Analysis

Both in the main text and in the Materials and methods, this is described as "genes were fed into a developmental enrichment analysis". Can some explanation be provided as to what happens between the "feeding in" and what comes out? Without clearly described methods, it is impossible to interpret or critique this component of the paper. If the methodological details are opaque, then the significance of the results could be tested numerically relative to some randomized null inputs being 'fed in' to demonstrate specificity of the tested phenotype.

– IQ prediction

The predictions seem to be very poor (equality lines, y = x, should be drawn in Figure 5, to show what perfect predictions would look like; linear regressions are not helpful for a prediction task, and are deceptive of the appropriate MAE computation). The authors do not perform any comparisons in this section (even to a real baseline model like `predicted_IQ = mean(training_set_IQ)`). They also do not perform statistical tests (or quote p-values), but nevertheless make a range of claims, including of "significant prediction" or "prediction accuracy was improved", "reemphasize the benefits of incorporating subcortical nodes", etc. All of these claims should be tested relative to rigorous statistics, and comparisons to appropriate baseline/benchmark approaches.

– Group Connectome

Given how much the paper relies on estimating a group structural connectome, it should be visualized and characterized. For example, a basic analysis of the distribution of edge weights and degree, especially as edge weights can vary over orders of magnitude and high weights (more likely to be short distances) may therefore unduly dominate some of the low-dimensional components. The authors may also consider testing robustness performed to alternative ways of estimating the connectome [e.g., Oldham et al. NeuroImage 222, 117252 (2020)] and its group-level summary [e.g., Roberts et al. NeuroImage 145, 1-42 (2016)].

– Individual Alignment

The paper relies on individuals being successfully aligned to the template manifold. Accordingly, some analysis should be performed quantifying how well individuals could be mapped. Presumably some subjects fit very well onto the template, whereas others do not. Is there something interesting about the poorly aligned subjects? Do your results improve when excluding them?

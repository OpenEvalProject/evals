# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Edinburgh , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11351.017](https://doi.org/10.7554/eLife.11351.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled "On the difficulty of predicting neuronal output from underlying electrophysiological parameters" for consideration at eLife. Your full submission has been evaluated by Eve Marder (Senior editor) and three peer reviewers, and the decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

It has taken us a little time to put together some sort of consensus decision about your manuscript because each person who looks at it seems to see (and not see) somewhat different strengths and weaknesses. I believe that this is a measure of the fact that it is an ambitious undertaking and only partially successful in its present form. Consequently, we are forced to reject this version of the manuscript. Nonetheless, if you find the criticisms, comments here and below helpful, and you feel that you can produce a different version of this work that takes into consideration these reviews, eLife would be willing to consider a new version, which we would consider as a new submission. That manuscript might be evaluated by the same or different reviewers, and there is no assurance that it would be successful in review.

Major Strength:

We are all impressed that you have made a serious effort to collect as many measures as possible from each of a large number of neurons in the frog tectum. In principle, this should constitute an important data set, and could be used to answer a number of interesting questions. And one of the reviewers was, and remains positive about the paper, precisely for this reason. Clearly, the attempt to connect the intrinsic properties and electrophysiological behaviors of the neurons to their underlying component processes is deeply important. But, the devil is in the details, and that is where other reviewers had serious reservations, some of which are expressed in the original reviews and others that surfaced during an extensive set of discussions among the reviewers.

Weaknesses/Limitations:

1) The reviewers were unclear about whether your starting assumption was that all of the recorded neurons were of the same cell type: principal neurons of that tectal region? You made it clear that you were excluding neurons that should have been of a different type, but what evidence is there that all of these neurons should be considered similar? In other words, was it your goal to cluster neurons into reliably different subtypes, or was it your goal to study the range of properties in one type of neuron? The manuscript seems to slide back and forth between these two positions.

2) Having 33 attributes sounds impressive, but the question is how many of these attributes are independent, and how many are derived properties? To be more specific, we would all agree that the Na and K conductance densities are independent attributes. But, spike frequency and interspike interval are two measures of the same property. Obviously, this latter case is trivial, but there are instances in which two attributes that on first glance may appear to be independent are not. So for example, membrane capacitance and synaptic current might together give you the envelope of the synaptic events? If so, then is it fair to use all three as independent attributes? It is not clear how many truly independent measurements there are among the 33?

3) We understand that there is an inherent problem when one is trying to measure many properties from the same neurons, and that it may not be possible to make all measurements perfectly. That said, we don't fully understand why particular choices were made. For example, you do not report the resting potential. And we understand why you made some measurements after bringing all the neurons to -65mV. But that by itself was a decision to not measure the voltage difference between the resting potential and threshold. There are a number of choices of this sort which were not adequately justified in the manuscript, but which might change significantly the take-home messages? You report the number of spikes in response to cosine drive, but from -65mV. These data might look totally different if you had started at the neurons' resting potential (which also has its difficulties of course).

4) A relatively minor consideration that however influences how people approach the paper: the title promises more than the paper delivers and sets it up for criticism.

The full individual reviews are below.

Reviewer #1:

In the present article, Ciarleglio and colleagues investigate the changes in electrical phenotype of neurons of the optic tectum of Xenopus laevis tadpole occurring during development and after imposed sensory stimulation. One of the specificities of the current article is that the authors use different types of multi-dimensional analyses (mostly PCA) to analyze variations in electrical phenotype defined by 33 intrinsic electrophysiological parameters (passive properties, spiking response, and measurements of specific voltage-dependent ion currents). The main conclusion drawn from this analysis is that a high degree of degeneracy underlies the electrical phenotype of tectal neurons, as neurons with similar spiking can display strikingly different underlying electrophysiological properties and neurons with similar underlying electrophysiological properties may display strikingly different electrical phenotype. Moreover, the authors suggest that the differences in electrophysiological properties found between visually-stimulated and early stages of development for similar spiking profiles also demonstrate degeneracy of electrical phenotype. Although the approach is interesting, I have several concerns about the measurements, the analysis and the conclusions drawn from the results.

1) My main concern is about the poor representativeness of the total variance of the observations by the two principal components used for the PCA (presented in Figure 4, Figure 5, Figure 6, and Figure 7). As the authors mention, the 2 principal components account for 23% of the variance of the observations (15% for PC1 and 8% for PC2). This means that the main part of the variance in the observations (77%) is unaccounted for in this analysis. The choice of analyzing neuronal output by measuring a large number of electrophysiological parameters, and using dimensionality-reduction techniques such as PCA to visualize it is a valid approach if dimensionality reduction preserves most of the information contained in the original measurements. In the present case, 77% of the variance (most likely including variance in parameters that are essential for defining neuronal output) is lost in the analysis. This problem may arise from several different sources: i) the high number of parameters used as an input for the PCA (33) ii) the fact that a linear model such as PCA might not be adequate to describe the variance of the parameters analyzed here. Independent of the source of confusion, this means that PCA may not be the adequate model to use in the present study to draw conclusions on the relationships between neuronal output and underlying parameters. In particular, the concept of degeneracy requires that both the target phenotype (here neuronal output) and the underlying parameters are accurately measured (see main point 2) and defined, and that they have relevant relationships. The fact that PCA accounts for only 23% of the variance in "electrical phenotype" is a real concern that hinders the purpose and the conclusions of this study.

2) My second main concern is about the relevance of some of the electrophysiological parameters measured: some of the parameters are flawed with measurements errors, whilst others lack obvious physiological relevance. The thresholds of the 3 ion currents (Na, KT, and KS) are not measured properly as they are contaminated by reversal potential variations (Na, KT) or are based on a non-sigmoidal fragment of the IV curve (KS). Ion current "thresholds" are usually characterized by precisely defining the half-activation voltages based on conductance vs voltage curves. The measurements of action potential properties in these cells seem to be strongly influenced by variations in the remote location of the spike initiation site (as indicated by the small amplitude of the action potential, around 15–20 mV). In this context, it is difficult to understand whether variations in the kinetics and amplitude of the action potential are mainly attributable to variations in Na and K currents, or variations in the passive properties (i.e. rather related to Cm and Rm) of the compartment located in between the recording site and the spike initiation site. I do not understand the monosynapticity factor.

3) Because of the first two main concerns, it is difficult to really trust the conclusion about the degeneracy of neuronal output in these neurons. Although there is no doubt that biological systems are "degenerate", demonstrating degeneracy first requires to demonstrate that the variable parameters have a strong influence on the output of the system. As an example, action potential shape is degenerate if i) it relies on variable sodium current density and ii) sodium current density has been demonstrated to have a causal influence on action potential shape. The degeneracy argument is irrelevant when the second condition is not fulfilled: as an example, the fact that synaptic transmission at axon terminals located far away from the soma tolerates large variations in soma size does not tell us anything about the degeneracy of synaptic transmission, until we prove that soma size has a significant influence on synaptic transmission.

Reviewer #2:

Ciarleglio, Khakalin et al. have analyzed input-output tuning (spiking) and the underlying electrophysiological properties of neurons in the optic tectum of Xenopus tadpoles over a series of stages of development and following visual stimulation at a single stage. Principal component analysis identified properties of spikiness and robustness. Some properties were found to change during development, while others changed with stimulation. Neuronal properties were observed to become more diverse with age. The authors observes substantial degeneracy in that multiple combinations of electrophysiological properties lead to similar spiking behavior so that electrical properties cannot predict spiking activity.

The project is very well conceptualized and executed. The paper is clearly and very well written and ties to the figures nicely. The figures in turn are very well assembled and easy to follow. Figure 7 is particularly informative.

My only suggestion is to change the title to something more positive. Perhaps something like Quantitative analysis of the relation of spiking output to electrophysiological properties reveals substantial degeneracy. I think this will motivate more readers to dip into it.

The authors have addressed an important question about structure (component) – function relationships in the vertebrate brain.

Reviewer #2 (Additional data files and statistical comments (optional)):

The data files and statistical analyses seem appropriate.

Reviewer #3:

The authors have provided a substantial data set of electrophysiological properties of tectal neurons of Xenopus tadpoles, towards a goal of better understanding the changes in spiking properties of these neurons over development. An additional, and perhaps more striking, point of the paper is the apparent variability of properties that underlie "similar" spiking patterns. In its current form, I'm not sure it has accomplished these goals. There is also a much richer literature in which to root these ideas, particularly in computational arenas, which are largely overlooked.

There is inherent value in large electrophysiology data sets, and the authors provide a substantial amount of data in this regard. Ultimately this paper is about analysis choices within this data set. I have comments about some of these analysis choices, organized by figures:

Figure 2: The authors seem to have chosen to combine a large dataset of heterogeneous cell types and then perform post-hoc correlation analyses. The rationale for this is unclear, and potentially confounding. The value of the "network" style plot in Figure 2A is minimal. This kind of diagram could potentially be valuable for comparing correlation patterns across groups, but as a standalone, it is difficult to follow any one pair of parameters that the reader would be interested in. The thickness of the lines has no interpretive value without a scale associated. For example, R-values that range from 0.1 to 0.3 would still have a threefold range of thickness, but show minimal correlation regardless.

Figure 5: Using a PCA, despite the difficulties inherent in not all data being present for all cell types, can be a powerful approach. However, while one can somewhat impute characterizing "spikiness", a meaningful definition of "robustness" is not provided. The authors then go on to make the point that the PCA cloud is moving across developmental "space", predominantly in the "spikiness" domain. This is seemingly a bit of an overwrought analysis, when a much more direct measure of "spikiness" (i.e. the spiking of the cells) is provided in Figure 3 and demonstrates in much less convoluted terms that spiking propensity does indeed change in these groups.

Figure 7: This is a major thrust of the paper, in support of the notion that cells that are grouped by similar output have variable physiological parameters. This crucial aspect of the manuscript is not well justified. The criterion for determining cells of similar output is only mentioned in passing with a reference to work of Victor and Purpura without enough detail to evaluate. Since then, many computational studies have been published with highly effective means of identifying cells with highly convergent output. This is underscored by the fact that in Figure 7B, the representative traces from these cells are too small to really get a proper feel for this, but the case could easily be made counter to the authors assertion that "spiking outputs are… closely matched within each group". In other words, they don't look that similar to me. If this is based simply on spike number, then it is ignoring the pattern of firing and seems to arbitrarily decide that 2-3 and 4-7 are different groups (why not 2-4 and 5-7?). A much more thorough analysis and justification for "similar outputs" would greatly strengthen the argument of the authors. As this figure is potentially a centerpiece of the study, this is one of the most critical aspects to address.

Reviewer #3 (Additional data files and statistical comments (optional)): I do have comments about statistical approaches for this paper, as the manuscript is highly dependent on the analyses for its interpretation.

Figure 2: A rationale for Pearson analysis, which is wedded to a linear relationship, as opposed to Spearman or Kendall Tau, would be appreciated (Pearson does not require normality, because most of the data set is non-normally distributed and rank-based correlation may be more appropriate). The panels in Figure 2B reveal the susceptibility of correlation analysis to outliers and nonlinear relationships. In particular, "Wave decay vs. N spikes (steps)" is a highly suspect correlation, yet is presented as one of the strongest. The power of large sample sizes and the logic of correlation allows for an analysis pathway that can avoid these problems. Specifically, with this level of sample size the authors could remove the tails of the data distribution (perhaps below the 5th and above the 95th percentiles), reanalyze, and see if correlations remain. If a true correlation exists, it will persist among any reasonable subset of the data points.

Figure 3: Nonparametric analyses are performed on these data, but the data are represented with parametric variance. It is unclear what the shaded area represents, or its statistical derivation or value.

Figure 5: If I understand correctly, the authors are making the conclusion that the PCA space changes across developmental time by doing statistics on statistics (an ANOVA of Principal Components). I'm wondering if there are other examples of this approach and whether this derived level of analysis is appropriate. Citations would be appreciated.

Figure 6: It is not clear what the origins of the shaded parts of Figure 6E are? Are these a result of a statistical measure?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your work entitled "Multivariate analysis of electrophysiological diversity of Xenopus visual neurons during development and plasticity" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom has agreed to reveal his identity: Nicolas Spitzer. The evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

Ciarleglio et al. have followed the changes in an exhaustive list of electrophysiological properties of visual neurons in Xenopus during development. This reveals that properties typically diverge over development, but also that visual stimulation can reduce variability.

Essential revisions:

The consensus reached was this is a valuable study well worth publishing, and it was strongly felt that the data set is an important part of the study and should be made public.

There are various options for this. If the data are subject specific then we strongly recommend that the data be deposited in the appropriate location. There is a nice list here: http://www.nature.com/sdata/data-policies/repositories. If the data are heterogeneous and not well suited to a specific repository then one can work with datacite, zenodo, imeji or figshare.

We can of course assist you in this process.

Reviewer #1:

Ciarlegio and colleagues have gone to a lot of trouble to record as many physiological properties as they can from many neurons in a population of Xenopus tectum neurons. They compare datasets across developmental periods and a stimulation condition. There appear to be three main conclusions. First, some neural properties change during development and with stimulation, becoming more diverse. Second, that neural properties are highly variable, to the extent that it is hard to predict physiological behavior from 'low level' properties. Third, stimulation appears to decrease variability in the sense that certain features become more correlated.

The first conclusion agrees with a large body of existing data, but does not say anything specific about the possible function of such diversification. For example, do the properties that change make sense from the perspective of how the circuit might function? This kind of question is not really addressed in the manuscript, which instead attempts a more data-driven/assumption free approach. Such an approach needs to have a very transparent analysis and should steer clear of jumping to conclusions. Unfortunately, I found the analysis relied heavily on quite opaque methods that in one case reported clustering (Figure 6A) with minute p-values even though no clustering is evident when all the data are plotted together. This reliance on very complicated analysis methods to find patterns in the data made it hard to interpret the findings and assess their veracity.

Another concern which is common to all experimental data that show high variability is the possibility that measurement error and the experimental procedure itself corrupt the readings. The authors chose quite a punishing experimental protocol, and a substantial fraction of cells did not survive. Those that did presumably had stable properties but the only criterion I could find for including a set of recordings was "as long as the nearest IV-curve recording from these cells was stable". This is unacceptably vague – how, for instance, would someone repeat this study using the same criterion? This makes me worry about the quality of the dataset, quite independently of whether it has been over-analyzed. If the dataset (i.e. raw recordings) were to be made available this would help a lot.

Reviewer #1 (Additional data files and statistical comments):

I think the dataset should be made available (raw recordings) and a qualified statistician should look at the manuscript.

Reviewer #2:

The authors have made significant improvements to the manuscript. They have provided better justifications for their conclusions that a population of neurons becomes electrophysiologically more variable during development, that similar spiking behaviors are generated by different constellations of membrane properties and that sensory input reduces electrophysiological diversity.

They have justified their data analysis more fully, in particular checking the main PCA analysis with two standard methods. The case for retaining all the variables makes sense to me. The variance that can be accounted by PCA is now validated through several procedures. The Methods provides a better justification and explanation of the analysis.

They strike a fair balance between clustering neurons into different subtypes and investigating the range of properties of a single type of neurons: the distinction cannot be drawn from the available data. Choosing between the two would be assisted but not resolved by knowing transcriptomes since there is more to differentiation than RNA synthesis, but this is an issue for another day.

Overall the paper is clearer on both experimental and analytical procedures and is more accessible. I am enthusiastic about publication.

Reviewer #3:The authors have done a fairly thorough and convincing job of re-packaging these results into a more tractable and consistent narrative, and this has greatly enhanced the paper. There is substantial value in a large and thorough electrophysiological parameter investigation in a vertebrate system, as this is a rare contribution to the literature. In particular what has emerged is an interesting story not so much about degeneracy in mechanisms of output of a single cell type (I believe a flaw in the initial conception of the original manuscript), but rather a thorough and convincing revelation of a continuum of output as revealed by shifting relations among electrophysiological parameters.

A majority of the rebuttal deals with the analysis, and I will admit that I do not have the depth of experience with PCA to contribute much more to this discussion. It seems well conceived and justified to my non-expert eye. The remaining concerns are appropriately addressed.

While the sum total content and conclusion of the paper lacks that clear and concise punchline, in some ways this adds to the charm of the paper. Biology is messy, and in some ways this paper helps to quantify this "messiness" and put it into multiple appropriate and interesting contexts.

I think this study makes a contribution to this area that is worthy of publication.

Reviewer #4:

The authors have taken the reviewers’ comment into account, and have modified the manuscript and added significant analysis accordingly. I have no further comments.

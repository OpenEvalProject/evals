# Peer review - Round 1

Editors:
- Manuel Zimmer, University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64988.sa1](https://doi.org/10.7554/eLife.64988.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper is interesting to psychologists, ethologists, and neuroscientists. It uses fruit flies as a model system and a sophisticated high-throughput experimental pipeline that captures a large space of behavioral metrics over long timescales, while keeping the identity of individual animals. Using innovative computational tools, the authors identify structure in form of covariations in this behavioral parameter space. They find that behavioral covariates appear rather sparse and high-dimensional. Hence, there are no stereotyped groups of individuality-types found in the population of flies. The work further shows that variability in behavior can be predicted in part by gene expression, and makes first attempts in targeting neuronal circuits that potentially contribute to behavioral variability.

Decision letter after peer review:

Thank you for submitting your article "The structure of behavioral variation within a genotype" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please go over the reviewers detailed comments below which we believe most of them can be addressed by additional analyses, text revisions and clarifications. The authors should revise the manuscript accordingly and prepare a point-by-point response.

2) The authors should provide a more thorough analysis showing which behaviours show persistent idiosyncrasies in individual animals as opposed to trial-trial variability (see reviewer #1). Based on this, perhaps the analyses can be repeated only on those behavioural metrics.

3) One concern is that the two decathlon data are not reproducible which undermines many of the conclusions and the subsequent comparisons to outbred fly lines. See reviewer #1 (1-2) and discussion with reviewer #3. Can the authors justify better their conclusions in the face of these concerns?

4) The reviewers agree that the results in Figure 3 are very weak. Besides the finding that behavioural covariates can change with temperature in the iso line, there is little that can be learn from the circuit interrogation lines. We wonder whether the paper would be stronger without these data included.

Reviewer #1:

The definition of individuality and its neurogenetic basis is a fundamental problem in ethology and neuroscience. Individuals might fall into discrete groups of personality types; alternatively, individuals might be better described by a broader spectrum of independent traits. An unbiased and quantitative analysis of behavioural traits that make up an individual's personality is a prerequisite of investigating the neuronal and genetic basis of individuality. Given the technical challenges in systematically measuring many behavioural traits across sufficiently large and genetically defined populations and over long time-scales, these questions remain unanswered. This manuscript represents a tour-de-force trying to shed more light in these directions. Werkhoven and colleagues aim at characterizing structure in correlations among a large set of quantitative behavioural measures obtained from the model organism Drosophila melanogaster. The authors performed a large number of high throughput behavioural experiments that cover behavioural paradigms ranging from locomotion to perceptual decision-making. Data were acquired from an inbred, hence isogenic fly line, an outbred line, and various neuronal circuit manipulations. In addition, gene expression data were obtained from individuals. In this way, the authors were able to capture hundreds of behavioural metrics from hundreds of flies, while keeping their individual identities over the course of 13 days. They developed a computational analysis pipeline that quantifies the correlation matrix computed from these metrics. In a 2-step procedure, they condense this matrix into a "distilled" matrix, the entries of which contain all remaining behavioural covariates that were not a priori expected by the authors.

A central claim in this paper is that any structure in this distilled matrix should reveal the principal axes along which individuality should be described. Based on these measurements and analyses flies could not be categorized into discrete types. Moreover, behavioral covariates appear rather sparse and derive from a high-dimensional behavioral space. This would mean that each individual fly is better described by a large combinatorial set of parameters. The same qualitative finding was made between inbred and outbred flies, leading the authors to a conclusion that larger genetic diversity does not change the principal organization of behaviour. The authors perform a set of neuronal-circuit manipulations and claim in conclusion that specific neuronal activity patterns underly structure in behavioural correlations. Some correlations between gene expression and behavioral metrics were discovered, for example gene expression of metabolic pathways

can predict some variability found in the behaviour of flies. The behavioural pipeline is sophisticated and presents a great leap forward in enabling researchers to capture a large set of behavioural measures from large fly population, keeping the identity of individuals. The work is also presenting an innovative and interesting analysis pipeline.

Although we applaud these ambitious experimental paradigms and computational techniques used, we have several major reservations about this work. Reading through the manuscript multiple times, one is left confused whether the major finding is that no structure whatsoever can be found in these data and to what extent the remaining sparse correlations are of biological / ethological relevance. Another major concern arises from the high level of trial-trial variability that is found in the data, which seems to preclude identification of persistent idiosyncrasies in the behavioural traits of individuals and impedes the reproducibility of the data matrices in two repetitions of the main experiment. We feel that most of the authors' conclusions and claims are confounded by these caveats.

(1) Distinguishing persistent idiosyncrasies from trial-to-trial variability and reproducibility of decathlon data.

A major challenge in measuring personality traits or individuality is to distinguish between persistent idiosyncrasies and trial-to-trial variation; the latter could result from inherent stochastic properties of behaviors, environmental or measurement noise. To identify an idiosyncratic behavioral trait in an animal one needs to show that individuals exhibit a distinct distribution in a behavioral metric that cannot be explained by trial-to-trial variability. Such a distinction cannot be made if a behavioral metric is measured just once or during a short period, but requires repeated measures over longer time-scales from a sufficiently large population of animals. Unfortunately, in this study many measures have been taken during just one 1-2hs episode per individual of a decathlon. For other measures that were taken repeatedly (circadian assays, unsupervised video acquisition) no efforts have been undertaken by the authors to make the above distinction. Hence, the authors' conclusion that there are no "types" of flies seems premature. In Figure S1 we are surprised to see how low most behavioral measures auto-correlate when recorded on two subsequent days; most auto-correlations further drop to meaningless values when compared over time-periods that correspond to the different epochs of a decathlon. This indicates that trial-to-trial variability dominates the data. In our view it makes little sense to ask whether two behavioral metrics are correlated or not, if their autocorrelations measured over the same time-scale are already extremely low. Moreover, Figure S5B shows that the two decathlons generate largely different data matrices (correlation ~0.25), raising concerns that the results are not reproducible. We wonder whether any structure in behavioral correlations was masked by various sources of noise in this study.

Related to above, there should be error bars and number of flies for the plots in Figure S1. This figure undermines the starting point of the paper claiming persistent idiosyncratic behaviors.

(2) Given the concerns above, it is not surprising that the outbred fly line delivers another set of covariates which lack otherwise any further structure. If experiments with >100 inbred flies cannot deliver reproducible results, it cannot be expected that a similarly sized population of outbred flies would. Perhaps the needed population size must be orders of magnitudes larger in this case.

(3) Figure 3. It is intriguing to observe how the relationship between switchiness and clumpiness is perturbed upon temperature shifts. But, it seems rather uncorrelated at the restrictive temperature in the Iso line, with a slightly positive value. However, the switchiness-clumpiness correlation is not reproducible in both perturbation types at permissive temperatures. Note, that at both temperatures the Shi and Trp datasets show no – or very low correlations: the Trp lines produce correlations from approx. -0.2 (permissive T) to 0.1 (restrictive T); the Shi lines 0, 0.1 respectively. Figure 3D is very misleading in showing the best fits to the combined datasets. We are not convinced that there is a robust sign-inversion in any of these correlation. The authors' major conclusion that " thermogenetic manipulation and specific neuronal activity patterns underlie the structure of behavioral variation" is not supported by these data. The effect of temperature in the control line, although interesting, is a major caveat for interpreting the results from the Shi and Trp results.

(4) The authors measure a large set of low- and high-level behavioral metrics, e.g. walking speed and choices in Y-mazes respectively. A fundamental problem is that many of these metrics potentially have common underlying but trivial causes, e.g. covariation between speeds measured in various conditions is expected. Therefore, the authors condense their original correlation matrix (Figure 1E) into a distilled matrix (1G) by making such judgements. In the present form, it is impossible to evaluate how systematic or arbitrarily these choices were. In many cases, where the same measure was recorded repeatedly (e.g. circadian bout length) or across different conditions (e.g. mean speed) it is obvious, but for other cases it is not obvious at all for the non-expert: for example, why are circadian-bout-length and LED-Y-maze-choice-number lumped into one block of expected behavioral covariates? The current manuscript lacks detailed explanations how the authors systematically created the distilled matrix. Can the sparseness of the distilled matrix be a consequence of too generous pre-allocations? See also point (6). The bulk of the analysis in this paper is done on the "distilled matrices" which are produced by removing correlations within previously defined groups of behavioral metrics. This is said to cleanly reveal unexpected correlations, leading to a main result of the paper, the correlations between "Switchiness" and "Clumpiness". However, if the a priori categories were defined differently, then in the extreme case this correlation would have been completely removed. How sensitive is this correlation to the choice of categories, especially given that many of the Switchiness and Clumpiness metrics are from similar assays (Figure S8)?

(5) For the second pipeline that uses t-SNE and watershed (Figure 2 and S3C), a previous publication from some of the authors [1] appears to show low repeatability of this analysis. Thus, the repeatability and noise levels of the pipeline must be investigated further. These were 3x 1h recordings per decathlon. Related to comments (1-2), the authors need to show that the differences across flies (Figure 2C,D) are not expected from the level of trial-to-trial variability. Perhaps more data from individual flies need to be recorded?

(6) 1G: To our understanding, within-block entries to the distilled matrix should indicate zero correlations, because these are correlations between PCA-projections. But we see many nonzero entries. Given the information provided in the methods it is unclear why this is the case; this requires further explanation.

In any case, within-block correlations are expected to be at least very low. Hence, we expect the distilled matrix to be relatively sparse given how it was calculated. Of interest are then the across-block correlations, the authors should make this pointy more clear top the readers.

(7) Some of the author's claims are related to the spectral dimensionality description technique described in Figure S9. However, none of the real data shown in the main paper figures look qualitatively similar to the toy data. Indeed, the histograms from the main figures are on a log scale, and are thus not comparable to the toy data results. Although the technique might be well suited for certain classes of data, one interpretation of the main paper figures seems to be that no structure is revealed whatsoever. More work should be done to exclude this as a possible interpretation, at least by generating toy data that look like the real Datasets; also with respect to point (6) above.

(8) Throughout the paper, the authors use the term "independence" for orthogonal / uncorrelated datasets. Correlation/uncorrelation – dependence/independence are not interchangeable terms. To my understanding PCA decomposes into independent variables only under certain circumstances (multivariate normal distributed data). Have the authors tested for independence?

[1] Todd, J.G., Kain, J.S. and de Bivort, B.L., 2017.

Systematic exploration of unsupervised methods for mapping behavior. Physical biology, 14(1), p.015002.

The authors should be more rigorous in identifying persistent idiosyncrasies.

The authors could repeat their analysis on the behavioral parameters that show consistent auto-correlations only.

Data/results related to Figure 3 could be removed from the paper.

Reviewer #2:

In this paper, Werkhoven and colleagues describe a large-scale effort, using Drosophila, to study variation in behavior among individuals with identical genotypes, and raised in very similar environmental conditions. This addresses the important and basic question of how much behavioral variability exists under such conditions, e.g. due to stochastic processes during development. By looking across many different behaviors, the authors are able also to investigate the nature of this variability. The key conclusion of the paper is that this intragenotypic variability is high dimensional, and cannot be explained by a small set of behavioral syndromes. They find that this observation is robust to the method they use to quantify behavior, and also holds to different degrees in data sets acquired from outbred flies, or files subjected to genetic perturbations of neural activity. Furthermore, they have generated a data set that allows correlation of behavioral biases in individual animals with transcriptomic data. Altogether, this is an impressive study that, beyond its important conclusions, opens up the possibilities for many further explorations in this area, and should be interesting to a broad audience. The experiments are well designed and overall the paper is very nicely written and clear to understand.

I have a few small questions or points that were unclear to me that the authors might like to address.

1) I missed a description of the distribution across individuals of the different behavioral measures that were used for the correlation analysis. E.g. were they generally Gaussian, heavy-tailed etc?

2) One complication in their data set is that there are quite a lot of points with missing data, because a particular variable could not be measured in a particular fly. The authors deal with this by filling in the missing data using an approach which they validate using synthetic data, where they have randomly deleted a subset of points. However it appears that the missing points in their datasets are not distributed randomly (Figure S3A) but have quite a marked structure. Perhaps the authors could apply similarly structured perturbations in their toy data to strengthen the argument for the methods they use for infilling.

3) A recent preprint from the Berman lab (Hernández et al., 2020. https://arxiv.org/abs/2007.09689) ascribes some aspects of interindividual variability to temporary differences in occupancy of longer time-scale behavioral states, and they make some attempts to normalize for this in their analysis. Perhaps the authors could discuss the possible implications, if any, for interpretation of their data set.

4) In the introduction the authors cite Pantoja et al., 2016 in the context of studying intragenotypic variability, but I don't think this paper looked at individuals with identical genotypes.

5) The data presented in Figure 3 seems less convincing than the rest of the paper. First, it appears to focus on only one particular behavioral coupling so that it is difficult to make a general conclusion from this that the Decathlon experiments tend to identify behaviorally meaningful couplings. I am also confused by Figure 3D, which appears to show, in the 95% confidence interval, a very wide range of possible slopes in the control data, which overlap considerably with the result at the higher temperature. Maybe the authors can help clarify this?

Reviewer #3:

In this paper Werkhoven et al., ask a fundamental question in behavioral neuroscience – what is the structure of co-varying behaviors among individuals within populations. While questions in the context of inter-individual behavioral differences have been studied across organisms, this work represents a highly novel and comprehensive analysis of the behavioral structure of inter-individual variation in the fly, and the underlying biological mechanism that may shape this structure of covariation. In particular, for their experiments they combined a set of behavioral tests (some of them were explored in previous studies) to a 13-day long behavioral paradigm that tested single individuals in a highly controlled and precise way. Through clever analysis the authors interestingly showed strong correlations only between a small set of behaviors, indicating that most of the behaviors that they tested do not co-vary, exhibiting many dimensions of inter-individual variation in the data. They further used perturbations of neuronal circuits and showed that temperature and circuit perturbations can change dependencies among sets of behaviors. In a different set of experiments where they integrated gene-expression data (from the brains of single individuals), they showed that some of the genes are correlated with individual-specific parameters of behaviors. Interestingly, through comparison of inbred and outbred population they demonstrated that also outbred populations are showing relatively low covariance of behaviors across individuals.

Overall, the data in the paper indicate that surprisingly, even for a 'simple' organism, there are many dimensions of inter-individual variation, e.g. many specific characters that can change among individuals in a non-depended way. The ability of the authors to precisely measure such dependencies in such a highly robust and precise way allowed their investigation of the underlying processes that may generate this variation. The results in this study are highly interesting and novel. They uncover a general picture of the structure of behavioral variation among individuals and open many avenues for further analyses of the underlying neuronal and molecular mechanisms that control variation in sets of behaviors. Furthermore, the methods that were developed in this paper can be of great use by other researches in the field.

However, while the key claims of the manuscript are well supported by the data and analyses methods, some aspects of data analysis need to be clarified or extended.

– It is not clear what is the motivation for using the 'Effective dimensionality spectrum' analysis presented in the paper and how it significantly adds to existing methods of clustering that are relying directly on the correlation/distance matrix (some of them were used in this study).

– While it is clear that the distilled behavioral covariation matrix has many independent dimensions (as the authors indicated, most of the a-priori PCs are not strongly correlated), the number of 'significant' Pcs was not calculated directly for the distilled matrix, and t-SNE analysis is presented only for the original covariation matrix (1L).

– It is possible that some if the behaviors that covary across individuals in the high temporal resolution assay and also tend to be associated over time within an individual, may indicate sequences of behavior on longer time-scales (than the timescales in which parameters are quantified).

– Further analyses are needed for extending the detection of correlations between variation in gene-expression data and the independent behavioral measures in the covariation matrix.

The results in the study by Werkhoven et al., are highly novel and important. They provide a compelling evidence for many independent dimensions of inter-individual variation within populations. Furthermore, using their careful and accurate measurements, as well as their clever analyses, they authors interestingly demonstrated that the structure of behavioral covariation among individuals may change under specific environmental/circuit manipulations and can be predicted from gene-expression differences. For their experiments they examined ~120 different behavioral parameters (across ten behavioral paradigms) in hundreds of individuals. Their robust and precise measurements allowed them to construct a covariation matrix that represents covarying behavioral parameters across individuals, thus defining characters of individuals in a more complex way. Analyses of these data detected many dimensions of variation, uncovering a complex behavioral covariation space. They further extended their experiments to (1) perturb co-variation structure by neuronal manipulation (2) find association between gene-expression and behavioral variation (3) show that both inbred and outbred populations have many dimensions of behavioral variation (4) run their analysis pipeline on available datasets.

Overall, this is an important study that will greatly impact many areas of behavioral neuroscience. The data in the paper indicate that surprisingly, even for a 'simple' organism, there are many dimensions of inter-individual variation, e.g. many specific characters that can change among individuals in a non-dependent way. The ability of the authors to precisely measure such dependencies allowed their investigation of the underlying processes that may generate this variation. This work uncovers a more global picture of the structure of behavioral variation among individuals and open many avenues for further analyses of the underlying neuronal and molecular mechanisms that control variation in sets of behaviors. Furthermore, the methods that were developed in this paper can be of use by other researches in the field.

However, while the key claims of the manuscript are well supported by the data and analyses methods, some aspects of data analysis need to be clarified or extended.

– It is not clear what is the motivation for using the 'Effective dimensionality spectrum' analysis presented in the paper and how it significantly adds to existing methods of clustering/network analysis that are relying directly on the correlation/distance matrix (some of them were used in this study). This analysis seems more of analysis of group structure of the covariation data and not a direct dimensionality assessment such as by using PCA. Also, a possibly more direct description of X axis in Figure 1J is 'number of connected components.

– It is not clear what is the number of 'significant' Pcs in the distilled matrix (Figure 1I), using the same shuffling methods that the authors used for the original matrix. It will be interesting to include t-SNE analysis for the distilled covariation matrix (such as in 1L).

– Figure 2 – why only the second Decathlon was used (p. 6)?

– Not clear how the probability matrix in Figure 2H was generated. What are the defined/measured parameters? Not in methods.

– Temporal correlations in Figure 2H may indicate sequences of behavior on longer time-scales that can change in intensity among individuals. In this case they may covary across individuals because they are part of the same temporal sequence

– It will be interesting to correlate the 'high resolution' movement parameters (Figure 2) with the rest of the behavioral parameters (Figure 1), although there is a clear separation in timescales between behavioral parameters.

– Figure 3: "colored hash marks" – do not appear in the figure.

– Figure 4 – it will be informative to correlate gene-expression data with measures of the distilled behavioral covariation matrix (PCs), given that genes are probably correlated in the same way with behavioral parameters from the same a-priori group.

– Figure 7- Analysis of other datasets indicate that in some of the cases there are stronger correlations among behavioral parameters. It will be interesting to discuss potential sources of differences in structure between the datasets.

Figure S9 Dashed line not explained in figure caption.

Comment by reviewer #3 that arouse during the discussion, in response to reviewer #1, point (1):

The reproducibility of the two experiments- the correlations in the distilled matrix (S5B) are lower than in the original matrix (S5A). I assume that the low correlation values in the distilled matrix makes the correaltion comparison more noisy. Actually, it is hard to learn a lot by computing correlation on correlations. I would ask the authors to plot the correlations of D1, D2 (one against the other) to directly show reproducibility.

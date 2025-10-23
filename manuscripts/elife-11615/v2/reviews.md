# Peer review - Round 1

Editors:
- Duncan T Odom, University of Cambridge / Cancer Research UK , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11615.061](https://doi.org/10.7554/eLife.11615.061)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Evidence for a common evolutionary rate in metazoan transcriptional networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors (Duncan Odom). The evaluation has been overseen by Naama Barkai as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This was unanimously evaluated as an important analytical contribution to regulatory evolution, and will help rectify a number of discordant results currently in the literature. Carvunis et al. confirm that the rate of gene expression evolution is comparatively stable in both fruit flies and mammalian clades, and newly show that using a uniform analysis approach strongly suggests that underlying TF binding evolution also appears to occur at a comparable rate. They provide some evidence towards the hypothesis that this rate is mediated by the different rates of change found in euchromatic versus heterochromatic components of the mammalian genome.

Essential revisions:

1) The methods should be more carefully documented and the main text and supporting materials sections better cross-referenced (Reviewer #1).

2) The Discussion should be somewhat increased, and the major points brought up by all three reviewers addressed.

3) A few of the results should be revisited with new analysis (see Reviewer #3).

Reviewer #1:

This is an extremely important manuscript in regulatory evolution that, in essence, harmonizes apparently contradictory results from a number of previously published studies by using a carefully designed and uniform analysis methodology. There has been considerable debate around how rapidly transcription and transcriptional regulation evolve between species. In particular, fruit flies and mammals have been reported to have surprisingly different tempos of gene-specific TF binding divergence. Carvunis et al. extract the raw data from a number of studies, and then apply rigorously a combination of analysis protocols with many combinations of widely used tools. They reveal that when analyzed together, gene expression and TF binding evolve similarly in drosophila and mammals. Finally and importantly, Carvunis et al. reveal that a likely culprit for the disconnect between rapid sequence evolution of mammals and the slower SPTF binding and gene expression evolution is the rapid divergence of chromatin inaccessible DNA in mammals. This last point is the key intellectual (as opposed to technical/analytical) insight within this paper.

Aside from more clearly outlined computational handling and a few minor revisions I suggest for consideration below, this straightforward and timely paper will be an excellent contribution to the ongoing discussion of evolutionary genetics.

Major considerations:

1) Materials and methods. Starting from paragraph two of the Results, the authors should direct the reader to the Methods section, and write a concise, but carefully laid out, description of how each step was performed. For instance from paragraph two of the Results, the inter-species normalization of gene expression is a notoriously tricky bit of analysis, per the Brawand et al. Nature 2011 study. I think this really must be carefully walked through. Similarly for all the other sections later.

2) Points not mentioned in this version that could be additionally dissected in the Discussion include:

The impact of effective breeding sizes on how chromatin accessible and inaccessible DNA is handled.

How the breeding rate and absolute time (MY) could interplay in driving evolution (in other words, 40 MY for flies is a LOT more generations than for mice).

Reviewer #2:

This study draws on published datasets to study the evolution of transcriptional regulation in three clades (mammals, birds, and diptera). The basic finding is that rates of evolutionary divergence in transcript abundance, transcription factor binding site occupancy, open chromatin sequence evolution, and transcription factor motif sequences are similar in the three clades. This result is unexpected, as previous studies have reported rather different rates of evolution for some of these features. The authors use this observation to argue that only a small fraction of the genome is involved in transcriptional regulation.

A notable strength of this study is that the authors applied uniform methods of analysis to similar kinds of data, demonstrating that the differences in evolutionary rates reported in the earlier publications are at least in part an artifact of the different methods of analysis that they used. (The impact of different technology platforms, which is also likely a contributing factor, was not addressed.) These results provide an important cautionary lesson, namely that it is essential to work with closely comparable data and to apply uniform methods of analysis before drawing conclusions about biological differences or similarities based on functional genomic datasets. The study is valuable for this reason alone.

Where it is less successful is in providing new insights:

1) The plots showing similar overall rates of evolution (Figure 3, Figure 4, Figure 5) are striking and I'm convinced that the rates are similar among the three clades. But I have no idea what this tells us about the evolution of transcription. I couldn't find any mention in the Results or Discussion sections about how to interpret the observation of rate constancy.

2) The only conclusion presented in the Discussion concerns the fraction of the genome that regulates transcription. Unfortunately, the bulk of the evolutionary comparisons have no bearing on this conclusion. The only one that does is the rate of sequence evolution within chromatin-accessible regions of the genome after removing core promoters. This comparison is relevant, but not because of the rate constancy among clades. It is relevant because the rate in this fraction of the genome is notably slower than the genome as a whole, and specifically within mammals, which have the greatest proportion of noncoding sequences among the three clades. Thus, most of the rate comparisons among the three clades contribute little or nothing to the conclusion that a small fraction of the genome regulates gene expression.

3) The observation that regulatory sequences evolve more slowly than other noncoding sequences is by no means a novel observation. This has been noted previously not just in Sundaram et al. (2014) (as the authors point out), but in several others, including Yue et al. (2014) and papers from Odom's group and Crawford's group. So the basic conclusion of the study was already apparent. Indeed, this is the logic that Graur et al. (2013) used to argue that the ENCODE team overestimated the fraction of noncoding sequences that are functional.

4) The argument that sequence conservation implies that a small fraction of sites regulate transcription is not as straightforward as implied in the Discussion. The ENCODE team wrote a thoughtful rebuttal of the Graur et al. paper (Kellis et al. 2014 PNAS 111:6131) that should be cited in this regard. Beyond the narrow debate about the ENCODE claims, it has been clear for quite some time that some enhancers and transcription factor binding sites turn over quite rapidly in evolution even though they are known to play a role in transcriptional regulation. See Yue et al. (2014) for a recent example, but there are many others. It is clear that negative selection is not the only evolutionary mechanism that operates on regulatory sequences. Using conservation as a criterion for function will thus overlook some functional sites.

Reviewer #3:

Carvunis et al. present an interesting analysis comparing evolutionary rate of genomic sequences and transcriptional regulation, by examining gene expression, transcription factor binding, and open chromatin marks across multiple species of mammals, birds, and drosophila. The authors' analyses recapitulate previous results that sequence gain and loss are much more prominent in mammals than in birds and insects, while rates of gene expression level changes are similar. The authors show that the rates of regulatory changes, such as gain and loss of orthologous TF binding and open chromatin events, are indistinguishable between lineages, providing an answer to conflicting reports on the different rates of evolution for genomic sequences and transcription regulation.

This is a well-written study with important insights. The authors draw a significant conclusion. However, the study has several limitations in their results, reducing their supports to a rather strong conclusion. The authors should either be very clear with the assumptions they made, or presenting stronger and more comprehensive evidence. But I am very excited about this work.

First, the authors use fraction of ortholog sequence retained as a metric to measure rate of genomic sequence evolution. However, the study should consider sequence evolution in the context of rate of substitution, in addition to what the authors already provide. Retained sequences can evolve at different rate, which is directly related to the arguments the authors make.

Second, the authors choose to use the exponential decay model to fit this data. While this is a useful model for evolutionary analysis, this is not the only one. Would their conclusion be solid if they fit the data with a different model?

Third, the species chosen for the study does not provide enough coverage across the 100myrs span. For mammals, there was one data point at 20myrs, and many more data points at either >5myrs, or more than 90myrs. This is a serious concern, because the skewed distribution could potentially bias any model fitting. This is reflected by the TF data for the 20myr comparison. The datapoints at 20myrs were consistently below the fitted curve, often appears quite significantly deviated from the curve.

Lastly, the number of TFs included in the study is too small to support a quite general and significant conclusion. I don't expect many TF data will become available for the study, so perhaps tuning down some of the claims would be a good response.

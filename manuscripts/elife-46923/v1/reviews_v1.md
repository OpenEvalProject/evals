# Peer review - Round 1

Editors:
- Peter Turnbaugh, University of California, San Francisco United States

Reviewers:
- Peter Turnbaugh, University of California, San Francisco United States
- Christopher Quince, University of Warwick United Kingdom
- Sean Gibbons

## Review text

DOI: [10.7554/eLife.46923.026](https://doi.org/10.7554/eLife.46923.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Consistent and correctable bias in metagenomic sequencing experiments" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Peter Turnbaugh as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individuals involved in review of your submission have also agreed to reveal their identity: Christopher Quince (Reviewer #2); Sean Gibbons (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The independent replication of microbiome research can produce very different results due to biases inherent in different protocols for studying complex microbial communities. Here, McLaren, Willis, and Callahan focus on multiplicative biases in microbiome experiments and quantify their effect on distorting the resulting abundance distributions. The authors formulate a rigorous framework in treating multiplicative biases based on individual protocol steps and derive a correction of that bias. Application of their correction methods to two mock community data sets validates their findings and provides improved estimates of microbial abundances. Together, this work provides an important framework to begin to more robustly compare data across experiments and research groups. This work is incredibly timely and provides a significant advance in our understanding of biases in microbiome data and a framework that will be built on to address them in the future.

Essential revisions:

1) The github repository is great but might not be enough of a tutorial for inexperienced users. I'd recommend writing a step by step tutorial (a la http://qiime.org/tutorials/).

Also, are there any plans in place to update this code as new approaches become available? It may also help to name the package/tool.

2) More discussion is needed regarding the propagation of noise or errors across multiplicative factors as opposed to bias. For instance, is noise in the extraction protocol more important than PCR because it occurs earlier? Or are the errors simply multiplicative too so that there is no purpose in trying to reduce noise in the earlier steps? In any case noise is perhaps more important than bias as it cannot be corrected so in their Tables 1 and 2 it would be good to have an estimate of the average error associated with each protocol. In some cases, a more biased but reproducible protocol could be preferable.

3) Both data sets used by the authors are derived from mock communities with known ground truth. The authors argue that their methods can be used even in the absence of a ground truth by using relative efficiencies. I feel that this is an important use case for real-world data sets. Standard communities, including all/most of the detected taxa across a set of real-world samples, are usually not available for any given microbiome study. Here, one could still estimate relative efficiencies by using technical replicates (samples co-processed across batches – how many samples need to be co-processed across batches for this approach to be useful?). However, that particular use case is discussed only briefly and there is no quantitative study with any data set that is not a mock data set. I feel that inclusion of a non-mock data set with technical replicates may be more informative here since that is closer to most published microbiome data sets. Based on that the authors could formulate a protocol that can be proposed for future microbiome experiments and that would allow systematic elimination of multiplicative biases. One challenge I foresee is that relative efficiencies will be very difficult to estimate for low-abundance taxa that are often unique to a small number of samples, unless every sample is processed across all batches.

4) The authors start by arguing that major biases should be multiplicative. Even though they provide a wide array of references describing the existence of bias in microbiome assays, there is no reference that supports the assumption that the strongest bias has to be multiplicative. This is addressed later in the manuscript by showing that multiplicative bias captures the error in mock communities well and by stating this multiplicative limitation in the Discussion. I would have liked a more systematic study of the potential magnitudes of multiplicative vs. additive/other biases.

a) For instance, what is the amount of variance explained by multiplicative bias vs. potentially additive biases (e.g. saturating effects, contamination from external sources, or well-to-well contamination)? I would expect that additive biases, like well-to-well contamination, to be more important in low-biomass samples. Further discussion of this point would be useful.

b) In the two data sets analyzed in this study the authors removed contamination manually. However, this approach likely won't be possible for non-mock data.

c) All bias estimates reported in the text are usually reported without dispersion measures, even though the formulated point estimate should induce an appropriate dispersion measure as well. It would be interesting to see how much uncertainty there is regarding the bias as a function of samples used for correction. This could aid in determining how many samples should be used to estimate the bias.

5) It would be worthwhile to discuss the observed bias structure with other data transformations (not only the ones from compositional data analysis). For instance, Equation 7 essentially makes fold changes of the same taxon across samples invariant to the bias. This would mean that the established transformation from RNA-seq analysis would also be applicable here (log-transformation and comparison by log-fold change rather than absolute difference).

6) I feel that some further investigation into correlations of the identified biases with taxonomy may be helpful to gain mechanistic insight into the sources of bias. For instance, does the bias correlate with the abundance of the taxon, or do phylogenetically similar taxa show similar biases? This could help to formulate strategies for estimating bias for taxa that are undetected in the batch replicates. The authors also argue that summarization of taxa into higher phylogenetic ranks may introduce additional errors, but they do not state which rank is permissible here (species, genus, family?).

The reviewers were all enthusiastic about publication and realize that all of these points may be difficult to accomplish within the next couple months. We would encourage the authors to use their best judgement in deciding what can be addressed in a substantive way and which points would be best addressed with additional discussion.

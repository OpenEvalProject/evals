# Peer review - Round 1

Editors:
- Christian R Landry, Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57347.sa1](https://doi.org/10.7554/eLife.57347.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors present a comprehensive analysis of the composition of protein domains across millions of years of evolution to examine whether evolution is directing proteins towards specific regions of the available sequence space. One key finding is a reduction with time of hydrophobic clustering in proteins, consistent with evolution to reduce aggregation propensity as proteins age. The results presented show that although natural selection can change some protein features rapidly, other changes may be more difficult to achieve and can thus continue to be improved over long-term evolution.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Universal and taxon-specific trends in protein sequences as a function of age" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Taraneh Zarin (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Although the questions addressed in the manuscript are of potential interest to a broad community, the organization of the manuscript and some of the method descriptions make it difficult to know what are the specific questions being asked (Introduction) and how the data is compiled and analyzed (results). Some of the results appear to be significant but with very small effect sizes, which may require a more careful examination and interpretation. Since the study is focusing on protein domains, it would also be useful to define in the introduction what kind of protein domains are being analyzed. For many people, a protein domain has a tertiary structure, which means that by definition it is ordered. It is therefore not sure what a disorder predictor is predicting for such domains.

Reviewer #1:

Prior phylostratigraphic studies have reported correlations between various properties and gene age, where gene age is estimated from the last common ancestor of the species that harbor homologs of that gene. Failure to identify distant homologs is a source of error in gene age estimates. The prevalence of such errors, whether the error introduces systematic bias, and the impact of errors on phylostratigraphic inference is currently a subject of debate. This manuscript seeks to address these issues through the use of Pfam Hidden Markov models, instead of blastp searches, for homolog detection. The manuscript presents results that are relevant to two lines of inquiry:

– Does the use of Pfam HMMs reduce error in gene age estimates via greater sensitivity? Do the age estimates obtained with Pfam HMMs exhibit evidence of systematic bias that could lead to erroneous conclusions?

– What do gene age estimates obtained using Pfam HMMs tell us about the forces that govern the evolution of amino acid composition in proteins of different ages?

Both questions are important. However, there are substantial difficulties with the analysis and interpretation, as presented here, that must be addressed before is possible to assess the quality of the evidence and how well it supports the conclusions with respect to either question.

I) Lack of a formal hypothesis testing framework: In its current form, this manuscript does not address either of the above questions with sufficient formality and rigor to make a convincing case that the evidence supports a particular set of conclusions. To address this, the introduction should (1) summarize prior work, discuss open questions and unresolved controversies; (2) specifically state which hypotheses will be tested in the current study, with a discussion of the testable predictions that flow from these hypotheses; (3) describe how these predictions will be tested; and (4) what steps will be taken to eliminate confounding factors and rule out alternate hypotheses.

For the first question (mitigation of error due to more accurate homology identification), steps 1 and 2 are handled reasonably well. However, testable predictions are mentioned haphazardly in the results and confounding factors are not adequately addressed. The second question (what forces act on the amino acid composition encoded by genes as they age) is not formally stated as a target of inquiry, but introduced almost in passing in the middle of the manuscript.

II) Prior art: This manuscript states that "A key innovation is to use Pfam domains rather than BLASTp as our unit of homology". However, Pfam HMM models have been brought to bear on the question of homology detection and gene age estimates in a prior work that is not cited or discussed in the current manuscript: Jain et al., 2019. The authors will wish to read that article to determine to what extent it duplicates, contradicts or is complementary to the results in the current manuscript. In addition, they may find that the Jain et al. article offers useful ideas for methodological refinements and/or casts new light on how the results of the current manuscript should be interpreted. In particular, Jain et al., deal explicitly with lineage- and family-specific differences in evolutionary rates, topics that are not explored in depth in the current manuscript.

III) Methodology: The methodology in the current manuscript is not sufficiently well described to allow a reviewer to fully assess the results or another scientist to reproduce them. Technical terms are used without definition. Descriptions of how various quantities are actually calculated are lacking. Attention is given to statistical significance (p-values), but not to effect sizes. The presentation relies heavily on summary statistics and derived data, in ways that may obscure trends in the underlying raw data. Insufficient information is given about the data used, and it is not clear what data and supplementary information will be made available to the reader, other than the eight supplementary figures. Specific examples of these problems are given in the detailed comments below, but this is not an exhaustive list.

IV) Demonstrating that the evidence supports the conclusions: The manuscript contains a number of strongly word assertions without sufficient demonstration that these conclusions are in fact supported by the evidence. The logic underlying the assertions is not spelled out and alternate explanations are not ruled out or even discussed. The manuscript tends to conflate the description of an observation with the interpretation of what that observation means.

– In one example of these issues, the manuscript concludes that the use of Pfam HMMs resulted in improved detection accuracy. While this is highly plausible, the evidence for this conclusion is not rigorously demonstrated. The main evidence presented is that phylostratigraphy slopes for mouse genes are steeper when Pfam HMMs are used for homology detection, compared to blastp. However, the manuscript does not demonstrate that steeper slopes are incontrovertible evidence of more accurate homology detection. A comparison of the gene sets obtained using the two methods would provide a more convincing and direct assessment. Is there a decrease in false negatives without an increase in false positives? The properties of sequences in the two sets should also be examined for evidence of systematic bias.

The discussion of this issue exemplifies the tendency to confuse cause and effect. In the Results section, the statement "Our improved methodology increased the steepness of the relationship between gene ISD and gene age…" does not make a clear distinction between the observation (steeper slopes) and the inference (that steeper slopes are due to the new methodology and that the new methodology is an improvement). The inference must be demonstrated, not simply stated.

– In a second example, the argument is made that the observed relationships between amino acid composition and age are unaffected by systematic error in homology detection because different trends are observed in plant and animal protein domains and "homology detection bias is expected to create similar patterns for all taxa". No argument is presented to support the statement that "homology detection bias is expected to create similar patterns for all taxa." While this might hold under some conditions, it is not clear to me why this should be true in taxonomic lineages that differ substantially in GC content or evolutionary rates.

Even assuming that the "similar patterns for all taxa" prediction is valid, only one taxonomic comparison, plants versus animals, is offered as evidence. If subsets of animal species are compared, for example, are dissimilar patterns also observed? Further, could the different patterns in plants and animals be due to issues with the underlying data? The Materials and methods section describes a substantial effort to obtain high quality genomes. (This is one of the strongest sections in the Materials and methods.) Despite, and perhaps because of, this effort, the number of animal genomes exceeds the number of plant genomes by almost a factor of four. Domain discovery, modeling, and annotation in plant genomes lags substantially behind animal genomes, in part because of the relative dearth of proteomic data in plants. The fact that the slope for recent plant domains is positive and not statistically significant (p=0.1), as well as the large variance in plant slopes shown in Figure 1B, all suggest that there may be problems with the plant data that could be responsible for different trends.

The manuscript contains other, similar problems with interpretation of evidence, in addition to the two examples given above.

Reviewer #2:

James et al., comprehensively outline the challenges in phylostratigraphy and homology detection while carefully applying these methods to detect age-dependent trends in protein sequences. Their method improves signal for previously reported trends such as decreased hydrophobicity and increased hydrophobic clustering in young protein sequences. Interestingly, the authors find increased intrinsic structural disorder (ISD) in young animal domains, but not young plant domains. Their method also allows them to gain insights into changes in amino acid frequency with gene age. These results would be of general interest to eLife readers. The following could help clarify the scope of these results:

1) The authors should elaborate on the diversity of the taxa that are included. Although there are an impressive 435 species included in the analysis, there are only 5 non-plant and non-animal species, all of which are fungi. This is understandably due to quality control for data that are included in the analysis, but it's not clear if it's fair to use the term "universal" for the trends observed throughout the paper if they are based (mostly) on plants and animals.

2) The authors should comment on whether or not there are systematic differences in the plant vs. animal species that are included, and how that could affect the results of the study. For example, is the GC content of the included plant genomes a concern? There seem to be some reported differences in GC content of different plant species (monocots vs. dicots) [Kawabe and Miyashita, 2003; Li and Du, 2014, Šmarda et al., 2014] - are these species broadly sampled in this study? If not, this should be clearly stated.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for sending your article entitled "Universal and taxon-specific trends in protein sequences as a function of age" for peer review at eLife. Your article is being evaluated by Diethard Tautz as the Senior Editor, a Reviewing Editor, and two reviewers.

As you will see, the first reviewer was overall satisfied with the revisions, although some issues remained. The second reviewer raised important points, many of which are still valid for the latest version of the manuscript and concern some of the main conclusions.

Reviewer #2:

Having gone through the appeal letter and the current/revised version of the manuscript, I feel that the authors have addressed the reviewers' concerns, where possible and within the scope of the paper. The overall goals of the study are now more clearly defined, and the elaboration on the methods, data, and alternative explanations that could underlie the observations is helpful.

Reviewer #3:

Trends in summary statistics of proteins between plants and animals based on grouping age of origin show that bias in detecting homologous proteins is accounted for and not the strongest effect in results. Authors convincingly show (1) there are minor differences in degree of clustering of hydrophobic residues between proteins with ancient origins and more recent animal proteins; (2) animal and plant proteins with more recent origins have different degrees of predicted disorder; (3) Amino acid frequency trends are surprisingly consistent between ancient transmembrane and non-transmembrane domains, less surprisingly ancients assessed in plants and animal. Other claims are not convincing.

1) A main claim of the manuscript, that "events during the earliest stages of life continue to have an impact on the composition of ancient sequences" is not supported. The research, as described in the "general assessment" above, is focused on amino acid composition and other protein summary statistics compared among age of origin classes. Even if most of the analysis is accepted as correct, this data can only be interpreted as evidence for change if you assume the starting composition of the proteins in these age classes is the same.

2) No evidence was provided that differences in summary statistics were driven by selection, as opposed to slow relaxation to equilibrium. This should not be implied in the Discussion section. Further, there is no evidence that anything has reached any kind of "optimum". These unfounded claims, for me, detract from the overall analysis.

3) The difference in plant and animal recent disorder prediction measures is a good point to refute some previous analyses, but it contradicts the idea that disorder is necessarily a selection-drive property of new proteins.

4) The slope in excess clustering of hydrophobic amino acids is framed as being consistent, but this is an unconventional way of putting it given that the plant variation is so high, and the mean is in the opposite direction. Further, the ancient proteins are in the same direction, but barely so (just into apparent significance based on direction).

5) The effect size of the change in excess clustering among these groups is not big compared to the magnitude of the excess clustering overall. It was not clear to me that this is enough to matter, particularly over short time periods such as a few hundred million years. It would be good to demonstrate that this average magnitude effect would have a large impact on disorder or stickiness.

6) Because the clustering effect size is so small, I was not convinced that it would be difficult to alter the amino acid composition to this degree if required by selection. That is, my sense is that protein composition is moderately malleable to allow a steady state to be achieved fairly quickly (eg millions of years) such that the effect of origin age would not be detected on this time scale.

7) While the correlation in composition between transmembrane and non-transmembrane AA usage frequencies is impressive, three amino acids, G, A, and V, are strong outliers. These are the simplest three amino acids, and while they were possibly recruited early into the genetic code, the cited inference is fairly speculative, and was itself a prediction based largely on the amino acid simplicity. The "order of recruitment" correlation with slope (Figure 4) consists of 17 amino acids with little correlation, and these early three that have a large positive slope. This does not convince that age of recruitment continues to affect frequencies. There are many possible amino acid property vectors, and clarity on what has driven these differences is lacking.

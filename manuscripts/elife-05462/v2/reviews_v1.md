# Peer review - Round 1

Editors:
- Duncan T Odom, Cancer Research UK Cambridge Institute , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05462.018](https://doi.org/10.7554/eLife.05462.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Dosage compensation buffers copy-number variation in wild yeast” for consideration at eLife. Your article has been favorably evaluated by Stylianos Antonarakis (Senior editor), Duncan Odom (Reviewing editor), and three reviewers. The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The consensus was that the demonstration that wild yeast strains exhibit gene expression compensation in the face of aneuploidy was of potentially high interest to a broad community. Some substantial criticisms were raised, in particular by Reviewers 1 and 2, which you must carefully address before this can be published in eLife.

The essential revision requirements are: (1) repeat the chromosome titrations you did for Chr12 in strain YPS1009 using the Chr8 strains derived from NCYC110, and this new analysis must include spike-in controls for RNA-seq; (2) much better annotation of the strains used both in main text and in the supplemental.

Like the three reviewers have done, the Reviewing Editor, Duncan Odom, has gone over your manuscript both editorially and graphic design-wise, and we have made suggestions below that should help improve your clarity and presentation. One extremely important point: you must re-tool your figures with an eye towards red–green color blindness.

Reviewer #1:

This is a very interesting paper looking at aneuploidy in non-lab strains of yeast. They conclude that natural isolates are more tolerant of aneuploidy than the lab strain W303 and they suggest that this is related to an apparent dosage compensation of gene expression from the amplified chromosome.

I think this is important work, and it is getting to the heart of several key conundrums in the aneuploidy field. Because it's such an important problem, I think the paper should do more to convincingly show the results and how they contrast with the lab strain results. I suspect, as the authors find in one of the RNAseq experiments, that their results are not actually as different as it first seems.

1) The first set of RNAseq experiments are problematic for a few reasons. First, they are not performed with isogenic strains that only differ by presence/absence of a CNV. The additional variation in gene expression introduced by all the other genetic differences going on could be partly responsible for the observed differences. I think it is crucial to also show at least a few paired euploid samples of similar relatedness to demonstrate the degree of expression difference expected in the absence of any CNVs. The reason this is important can be best explained by imagining that the base expression really does change proportional to the copy number. Now imagine additional genetic differences cause many genes to change in expression by, say 1.5-fold up or down, a result that has frequently been observed in comparisons between natural isolates. In the simplest possible additive model of expression, many genes in the CNV would now show greater or less than expected changes in expression, but not due to dosage compensation.

Also, I think the data from these experiments would be much easier to interpret if displayed as histograms (e.g. something like Figure 2 in the recent eLife paper from Amon and Torres) in addition to the scatter plot view. Furthermore, the analysis would be much more compelling if compared directly to data from at least the W303 gene expression series, and preferably additional aneuploid lab strains (for example, the Hughes et al. deletion collection strains that are aneuploid, or some of the aneuploids isolated from experimental evolution). Though on average genes in the CNV change proportionately with copy number in these lab strain experiments, that is certainly not universally true, nor should it be: the W303 experiments, for example, have the same problem as described above, that is, the layering of multiple expression signatures, in this case the stress and/or growth rate response coupled with the copy number driven expression. Evolved strains and deletion strains have additional mutations as well that may affect expression on top of the perturbation from the CNV. Direct comparison to these data would be very convincing if there really is a big difference here. It certainly wouldn't be the first time that lab strains are outliers in behavior, so I am inclined to believe there is something to see, but it should be shown explicitly.

2) Some of the concerns about the first set of experiments are mitigated by the dosage series generated for the second batch of RNAseq. Here, we have both isogenic lines carrying different numbers of chromosomes, and a direct comparison with the lab strain. The fact that the apparent dosage compensation is present in the W303 3N strain in this experiment is one thing that makes me suspect these results are not as different as initially posited (and see the paragraph above for ways of demonstrating that I'm wrong). Also, that the 4N W303 strain is the aberrant one, and grows most poorly, hints again at the issue with confounding additional gene expression signatures.

Additionally, I really wish that chromosome 12 had not been the core element of this part of the paper. The rDNA array is on chromosome 12, and differences in repeat number can change the size of the chromosome by up to a megabase. In the W303 experiments, chromosome 12 disomy causes a growth defect that I definitely would agree fits the definition of “extreme.” Also problematic, different strains carry polymorphisms in the rDNA that cause all sorts of potentially confounding phenotypes, such as issues with replication (see Kwan et al. 2013 PLoS Genetics), a problem that might be particularly important for aneuploids. I think the experiments are still interesting, of course, but they are difficult to interpret without some indication that the rDNA is similar in sequence and copy number in the different strain backgrounds. A chromosome 8 series in W303 (or at least one other matched set) would also be helpful in addressing the generalizability of the observations with 12.

3) The remaining parts of the paper are nice follow-up experiments, including the analysis over other strains of genes that are found in CNVs more or less frequently, and the plasmid expression experiments. I have no major comments about these analyses and appreciated their inclusion.

Reviewer #2:

The Hose et al. manuscript examines the extent of dosage compensation within wild yeast strains. The work examines RNA-seq data and uses a new model (mixture of linear regression) to identify distinct classes of dosage compensation. They nicely use existing publicly available data to the level of dosage compensation constraint (Vg/Vm) and CNV buffering. In the data leading up to these sections, however, there are some major concerns.

In general differential expression studies using RNA-seq (subsection headed “A common aneuploidy response recapitulates a Down syndrome signature”; and edgeR as described here) assume that most things are not changing, an assumption that could very well be violated by whole chromosome amplifications. Normalization to a closely related euploid would not alleviate this issue. Spike in controls are necessary in this case. Redoing all their RNA-seq studies is unnecessary if spike in normalization for one strain relative to its closely related euploid shows largely identical results.

In the subsection headed “Many amplified genes display lower-than-expected expression”, it is noted that strains are “isogenic aside of the aneuploidy” yet this assertion is made without proof. In particular, the construction of the aneuploid isogenic panel for NCYC110 required passaging for 427 generations. At the known yeast mutation rate, this would result in roughly 2-3 mutations pre haploid genome content (or as many as 12 mutations in their strain as it is tetraploid). As anueploidy tolerating mutations are known to arise quickly (Torres et al. Cell 2010), it is unclear whether the observed differences arise from changes in aneuploidy or mutations. Given the diploid arose quickly after the triploid (17 generations), is the triploid strain unstable?

Given ambiguity in Figure 1A and the strain table, it is unclear if these were strains they already genome sequenced (in which case this would be a bioinformatic exercise) or whether genome sequencing is necessary.

In general the base ploidy and nature of the aneuploidy within various Figures is unclear. Given the broad range of comparisons made within this paper (strain backgrounds, aneuploidies, ploidies, etc), it is imperative for interpretation that these be more clearly labeled and identified. Likewise, their strain table should indicate for which strains genome sequence and RNA-seq are available from this study. It is unclear how “closely related euploids as paired controls” was determined. How do you know a particular strain is closely related: by genome sequence, by lineage, other?

Reviewer #3:

The authors observed no difference in growth rates or doubling times in WT induced aneuploidy strains, suggesting no deleterious effects are derived from this. Moreover, aneuploidy was stable throughout generations, strengthening the hypothesis that WT strains tolerate aneuploidy.

The authors elegantly generated aneuploidy strains from euploid parents, which give strength to their conclusions and showed dosage compensation is one mechanisms involved in such tolerability generating less than expected gene expression in some of the amplified genes that are under higher evolutionary constrain due to their toxic effects if overexpressed.

Comments:

The observation of downregulation of respiration-related genes is very interesting, yet to conclude that induced aneuploidy in WT strains recapitulates a Down syndrome signature is not sustained by the data shown in this manuscript. I would leave this assumption/interesting correlation for discussion and only highlight mitochondrial ribosomal proteins and respiration genes signature.

Do the authors have a hypothesis on how this signature is involved in the observed permissive aneuploidy?

Is Figure 4 showing the overall number of lower and higher than expected regulated genes in all aneuploid cells versus their euploid? How many of those are common amongst all strains tested? How would this graph look for each individual strain aneuploidy/euploid comparison?

Duncan Odom, Reviewing editor:

My comments are focused on presentational and editorial issues.

The Title should read: “Dosage compensation can buffer copy-number variation in wild yeast”.

The Abstract should be carefully re-edited, as it has a few awkward sentences.

In the Introduction, what criteria were used in order to pair up your yeast samples was not at all clear. This is mentioned in the major comments numbered above, but this section will need heavy and careful revision.

In the Results section, the use of these seemingly arbitrary classes is confusing to the reader. Consider how else this section could be more clearly presented. Related: the number of genes in each class should be listed clearly in the text.

In the Discussion, the term 'Balance Hypothesis' requires both careful explanation (I have no idea what this is, for instance) and a few accessible references or reviews.

In the Discussion, you state: “while the expression of these genes is controlled…” Which genes? This is a very ambiguous and poorly structured statement.

Figures: In general, please consider re-tooling all figures using the principles outlined in Visual Display of Quantitative Information by Edward Tufte. However, below I highlight specific examples that should be corrected.

The use of colors in the figures is poorly considered throughout. Random color choices appear to occur in their bar charts. There is excessive use of bar charts, which reduce interest.

Required: Figure 2A and Figure 2B must not use red-green, as this is impossible for the 6-8% of male readers to see who are colorblind. Replace with yellow-blue instead. See:http://www.nature.com/nmeth/journal/v8/n6/full/nmeth.1618.html

Figure 4 is poorly presented, and the axes are not understandable. Consider breaking into two separate and better annotated scatterplots.

Figure 6. D panel is not informative. What is this trying to say?

Figure 7. RNA abundance used blue in A/B and red in C/D. Why?

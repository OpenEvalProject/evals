# Peer review - Round 1

Editors:
- Joerg Bohlmann, University of British Columbia Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32110.040](https://doi.org/10.7554/eLife.32110.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Functional genomics of lipid metabolism in the oleaginous yeast Rhodosporidium toruloides" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

Both reviewers were generally positive about the paper. They have also discussed the reviews with one another and agreed that the paper requires some substantial revisions as detailed in their reports.

Reviewer #1:

In this manuscript the authors adapted random barcoded random transposon insertion methods to the oleaginous yeast Rhodosporidium toruloides, enabling the functional inference into 100s - 1000s of genes. Insert density was high (1 insert per 100bp) and fairly even across the genome, though there were some biases (regions of low insertion rates). The authors were convincing in the power of this method, and inferred the function of 1337 putatively essential genes, including 150 genes affecting lipid accumulation, of which 35 were validated through targeted deletion assays. The research appears to have been conducted with rigor and the manuscript is well written, figures are appropriate, etc.

I found this research quite exciting and do not see any flaws or major issues with this research. The only suggestions I have would be to shorten the text (Discussion is six pages, for instance), as it is quite long and in some places repetitive. Also, there are many advantages to working with yeast. The authors should discuss how well this approach would transfer to non-yeast fungi, which account for the vast diversity of Fungi and differ in biology, genome size and intron distribution. While the authors were able to dissect the lipid metabolism and importance of different processes (e.g. autophagy) and pathways for accumulation, I would have liked to have seen the use of this information to increase the size and abundance of lipid droplets, and yields in Rhodosporidium, obvious next steps.

Reviewer #2:

The paper entitled "Functional genomics lipid metabolism in the oleaginous yeast" represents a comprehensive random insertion mutagenesis effort in a relatively uncharacterized basidiomycete yeast. The successful construct of this library allows high resolution parallel genomic fitness analysis, whereby relative changes in mutant strain abundance in response to perturbation provide insight into gene function. Oleaginous yeast are of high interest as they are an attractive host for the production of sustainable chemicals and diesel-like fuels. In addition, understanding the unique accumulation of triacylglycerides (TAG) observed in this organism may be of relevance to lipid storage disorders in human. Here, re-annotation of the R. toruloides genome, combined with a molecular twist on the now classic insertional mutagenesis approach pioneered in Saccharomyces cerevisiae is deployed to address two important biological questions; the identification of genes that are i) essential for growth (in the conditions tested) and ii) involved in the unusual lipid metabolism of this organism.

Before embarking on creating a random insertional mutation library, the authors first greatly improved the existing genome assembly using standard approaches including long read scaffolds and paired-end sequencing of messenger RNA to guide gene annotation. By modifying bar-coded transposon sequencing methodologies, a library of insertional mutations was constructed by taking advantage of established methods of Agrobacterium tumefasciens T-DNA mediated transformation to overcome the low transformation efficiency of R. toruloides. All random mutagenesis techniques used for library construction suffer from insertional biases that can confound interpretation. T-DNA insertions exhibit a preference for intergenic regions, can include multiple insertion events, and have been shown to cause local mutations and inversions among others. Despite these issues, through careful tracking and detailed characterization of T-DNA biases, the authors successfully mapped 293,163 barcodes (from a total of ~2 million) to useable T-DNA insertions that were well-dispersed throughout the genome. These mutants represented >90% of nuclear encoded genes for use in parallel downstream fitness assays. In practice however, barcodes were sequenced on average to a depth of ~20 million counts per fitness assay. This precluded detection of ~40,000 mapped barcodes due to low counts and combined with constraining fitness measurements only to insertions that landed in central regions of the coding sequence. These constraints reduced the number of insertions that could be accurately assessed for fitness to 68,021; representing 6,588 genes and ~20% of the original total mapped barcodes. Counts per barcode ranged from 1 to 1000, with a mode of ~10.

The authors then turned to applying their insertion library to identify genes required for fitness in various conditions. As a proof of principle, synthetic minimal media (YNB) was supplemented with arginine and, in a different experiment, methionine was used and at least in one case compared to YNB alone. This is an ideal feasibility test, as any gene required for biosynthesis of these amino acids cannot grow in YNB alone, and therefore exhibit a maximum decrease in fitness. Though the authors did not address this issue, this experiment would be useful in defining the dynamic range and establishing the sensitivity of the assay. When fitness differences were striking when YNB was compared to YNB + the required amino acid the results were striking. Nearly all members required for arginine and methionine were identified, although there were a handful of exceptions. It seems that further study of the specific reason for these false negatives was a missed opportunity to learn about unforeseen issues inherent to the methodology. It is also noteworthy that the results were much less striking when the different fitness conditions were compared to the standard T0 control, the metric of fitness that the authors argued as being the preferred method for accurate quantification of changes in fitness. For this reason, why this analysis method was chosen over the other was not specifically addressed, a general finding echoed in other fitness experiments is throughout the manuscript. This concern is addressed more fully in the specific comments.

Additional fitness tests included growth on three fatty acids as the sole carbon source; 129 genes were identified with significant fitness defect scores that included genes involved in fatty acid oxidation, gluconeogenesis and mitochondrial amino acid metabolism. Many of these genes were consistent with those known to be required for fatty acid oxidation in other species. Importantly, these findings were validated by constructing targeted deletion mutants in ~10 of these genes and measuring growth on the various carbon sources.

To identify genes involved in lipid accumulation, the library was fractionated using two measures of lipid content – buoyancy separation and neutral-lipid staining. In this case, instead of using the initial library as the reference, genes involved in lipid accumulation were identified by comparing the abundance of each mutant in high and low lipid fraction and looking for strains that had the biggest differences measured in the two conditions compared to the control. Subsequent clustering of the data reveal enrichment in biological functions. Select strains were again validated; in this case finding a greater number of inconsistencies between the two assays as well as a greater number of false positives. The authors therefore defined more stringent criteria to correct this; requiring gene mutations identified as exhibiting increased or decreased lipid content to be consistent between both the buoyancy and staining lipid content assays. The rationale behind using their genomic toolset to understand lipid metabolism and biogenesis in this particular fungus is clear, but the results need to be put in context of what has been observed in similar assays in the published literature i.e. the large amount of information regarding particular pathways available from yeasts such as Saccharomyces, Schizosaccharomyces, Candida and Coccidioides. For example, the role of Sulphur metabolism in lipid biosynthesis and biogenesis would seem to be well served by a more extensive comparison to the data that has been collected and published with these other model systems. Indeed, it is unclear what, if anything, was specifically novel to R. toruloides.

Nonetheless, the morphological phenotypes observed were fascinating and would benefit from a more thorough treatment and a more in-depth comparison between these observations. Indeed, one of the key contributions represented by this thorough study is the power that it provides to compare and contrast these findings with findings observed in these other systems or by other methods.

In summary, the resource and library provided by this study will be extremely useful in further defining and characterizing the genetics and metabolic pathways unique to R. toruloides. Importantly, the study supports other work suggesting that existence mitochondrial beta-oxidation is widespread in fungi. The involvement of both peroxisomal and mitochondrial beta-oxidation has been shown to be important in gluconeogenesis in mammalian cells and has also been linked to altered metabolism in cancer.

Specific comments:

Overall paper is well written and represents a significant contribution to the genomic analysis of another emerging model fungus. However, there were several issues with the statistical analysis that must be addressed.

First, the issue of sufficient coverage in counts per gene needs to be included and discussed as necessary. As mentioned, the author's state fitness was measured fore 68,021 representing 6558 genes. After accounting for constraints including low reads, ~4.6 million counts were available to measure these ~70k mutations, leaving 50 counts per gene. If the counts were evenly distributed, this should be sufficient for fitness measures. We know that this is clearly not the case for sequencing reads as they are typically modeled using a noisy Poisson distribution or by a negative binomial. In the manuscript presented, neither the initial counts nor the final counts per gene are reported, not even including an example. This is a glaring omission: the authors state that the range of counts per gene varied broadly, with a mode of 10. Naively, this would imply that many mutations with significant fitness effects would be identified by ~10 counts. This seems too low for adequate gene coverage, particularly as the variance increases dramatically in this low count range, making significant fitness changes difficult to detect and accurately quantify.

Though the methodology used for the analysis was referenced (PMID: 25968644), the assumptions made in this analysis were not discussed here. Because the authors suggest that the use of the T0 sample strengthens quantitative fitness measurements, yet the results in the supplementary files do not seem to reflect this, the analysis section needs to include this discussion.

Overall, I found the statistical analysis difficult to follow and thinly presented – including details such as how the cells were grown. As manuscripts become increasingly packed with massive amounts of data, these sections of the manuscript are critical in order for the reviewer to evaluate the data quality and robustness.

In the supplementary text, fitness scores are described as:

"For each barcoded T-DNA insertion, we calculate the log2 ratio of abundance before and after competitive growth in the experimental condition. F is the average of those ratios (weighted by sequence depth) for all the insertions disrupting a given gene. T is a modified student's T-statistic, a measure of statistical significance of F that incorporates consistency between individual insertions across biological replicate cultures."

The authors need to include at least one example of how a gene is modeled by averaging the log2(T0 /Tafter) from different insertional mutants and include a figure that demonstrates the consistency across biological replicates.

The supplementary data mentions several different metrics and it is difficult to know which is being used in the main text, or why they are all included to begin with. For example in the auxotrophy experiments the results are presented in several different ways, the columns described by:

1) Fitness Scores (averaged between replicates), included 5 comparisons to T0

YPD

YNB + DOC

YNB + Arginine

YNB + Methionine

YNB + No Supplement

2) T-like Statistics versus T0; T-like test statistics for fitness/enrichment scores above

YPD

YNB + DOC

YNB + Arginine

YNB + Methionine

YNB + No Supplement

3) Fitness differences vs. Control Conditions (averaged between replicates)

DOC vs. No Supplement

Methionine vs. No Supplement

Arginine vs. No Supplement

YPD vs. No Supplement

3) T-like Statistics vs. Control Conditions

DOC vs. No Supplement

Methionine vs. No Supplement

Arginine vs. No Supplement

YPD vs. No Supplement

4) Wilcoxon Signed Rank Tests Multiple Hypothesis Adjusted; Wilcoxon signed rank test between condition and T0

No Supplement vs. T0

DOC vs. T0

Methionine vs. T0

Arginine vs, T0

DOC vs. No Supplement

Methionine vs. No Supplement

Arginine vs. No Supplement

YPD vs. T0

YPD vs. No Supplement

It is not clear which method of analysis was used on which dataset – every experiment should be annotated as such.

This presentation of the data is especially confusing because fitness scores are weighted averages by sequencing depth across all insertions and then averaged to obtain a single score. I can imagine all kinds of scenarios where this could be problematic. For example, for a single gene averaging the log2(T0 /Tafter) would seem to be vulnerable to over or underestimating the actual fitness – for example when different insertions for the same gene are conflicting in magnitude or even sign. Problems when measuring the relative importance of different genes to each other may also arise for example, if shorter genes are penalized due to having fewer insertions, or may introduce bias due to unequal numbers of insertions associated with each gene and possibly influenced by variance as well. To avoid these issues it would seem necessary to use a metric that corrects or normalizes for these issues.

An additional concern as has already been mentioned is the higher confidence in measuring fitness relative to the T0 condition; presumably due to the depth of sequencing and the ability to obtain associated 't-like' statistics. However, there seems to be some logic missing here. For example, in the condition YNB + Arginine, a decrease in fitness compared to T0 may be due to 1) slow growth of the strain in any condition 2) slow growth only in YNB 3) slow growth only in arginine.

Although there is an accompanying website, it is clearly in its early stages and no key is provided for explanation of the metrics used in these files.

In Supplementary file 2 multiple scores reported for each gene in each experiment. However, each gene described as a weighted average of all of the insertions for a given gene. The number of independent insertions is not given except to say that there were around 10 inserts/kb for most genes. This raises the possibility that the assumption that genes with fewer than 2 inserts are essential – a key conclusion only briefly discussed – maybe misleading. This section needs to mention the logic and statistics behind this as well as to acknowledge previous work (e.g. PMID: 28481201 which used saturation transposition to identify essential genes). Another point that requires attention is why the variance and confidence in the counts is not addressed (as it is in RNA seq) prior to scoring log ratios by the average weighted counts for the insertions associated with each gene.

This paper relies on an advance (more barcodes) on the well-established barcoded Tn-Seq methodology pioneered by Adam Deutschbauer. It seems unnecessary and not helpful to rebrand the technique with another acronym/abbreviation. The authors need to acknowledge the many Tn-Seq papers in many other model systems that have been successful in characterization of new genomes. Along these same lines, the authors mention that co-fitness analysis will accelerate annotation of new genomes. This is likely correct, but the previously published concept of co-fitness should be elaborated upon and cited.

Returning to the insertional mutagenesis technique and unanswered questions:

Overall, the main difficulties in insertional mutagenesis in comparison to targeted gene deletions are that saturation is difficult as some regions are hotspots, while others are immune. Other problems include the fact, as in this study, that each gene is covered ~10x, yet the nature of the mutation is unknown. This can be partially controlled by limiting insertion sites to those that interrupt coding regions.

If a gene-specific model is the intent for measuring fitness defects by relying on deep sequencing of the time zero sample, several specific issues need to be explained:

How many sequence reads are required for time zero? Shouldn't replicates of time zero be included? What is the supporting statistical test? What is the range of ratios and variance for F?

To end on a more positive note, I do not doubt that the fundamental conclusions of the manuscript are correct. Many if not most of the issues can be addressed by providing all of the data to the reader, preferably in a user-friendly format. However, the conclusions themselves did not obviously follow from presentation of the results, neither for the methodology or the biology. If the intent was instead to focus on novel biological findings using the technology, the biological findings seemed to rely heavily on homology and the presentation of complex model pathways was inappropriate without making clear in the model what is and is not known in other model organisms, or distinguishing what findings were novel and unique to R. toruloides.

# Peer review - Round 1

Editors:
- Joseph S Takahashi, Howard Hughes Medical Institute, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35618.041](https://doi.org/10.7554/eLife.35618.041)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Diversity and circadian cycling of alternative splicing in the transcriptomes of isolated Drosophila neuron populations" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript from Wang et al., the authors re-analyzed previously published RNA-seq datasets for alternative splicing (AS) patterns comparing three neuronal populations in Drosophila melanogaster that are critical for circadian rhythms (DN1, LNd, and LNv) with a control group of TH neurons. They have also analyzed these same populations over the course of two days. Overall, this is a coherent paper, applying sophisticated analytical method to high throughput RNA-seq data to uncover the novel findings.

Using the comprehensive computational method JUM (Junction Usage model) to analyze splicing patterns revealed a striking number of AS junctions in the aforementioned neurons absent from the more standard Drosophila head RNA preparation. A significant portion (~15%) of these were exclusive to the individual neuron types and almost entirely were previously unannotated (~95%). Each neuron type was also shown to contain a broad range of unique AS junctions when compared to the TH group, and that these genes could impact neuronal function (ex. N-syb, Shab). GO analysis on the AS genes from the circadian neurons showed globally that these patterns are more prominent in potassium channels, ion exchange pumps (sodium-potassium ATPases), and, more importantly, functions such as vesicle exocytosis that are critical for circadian function. Finally, the authors conducted a 2-day time course dissection of these same neurons every 4 hours and analyzed AS splicing again using JUM. This experiment found unique AS junctions in all circadian neurons that cycled through the day/night; however, the overall level of mRNA from most of these genes did not change, demonstrating that the control of gene function is most likely due to AS rather than transcriptional control.

There are interesting insights from these experiments into the much greater role of alternative splicing in circadian rhythms, however, there is too much emphasis on JUM, which has already been described elsewhere, in Wang and Rio, 2017. Considering this, the extensive description of the tool, nomenclature, and usage is not necessary and detracts from the biological aspect of the manuscript. That is not to say that JUM is not worth a good amount of emphasis – it is impressive, but a revision is needed to achieve a better balance. Substantial portions of the Results section and relevant Figures (Figure 1A in particular) could be removed.

Essential revisions:

1) The authors indicate that they have generated RNA-seq data from individual neuronal populations as described in Abruzzi et al., 2017 but it is not clear if the flies were maintained in 12:12 light:dark or constant darkness during the experiment. This distinction could impact the interpretation of circadian analyses since under 12:12 light:dark many gene expression changes and AS events may be driven by light sensing as opposed to an intrinsic clock.

2) The authors consistently refer only to the number of AS junction sites, without providing the number of affected genes. While the number of events is of interest because it gives a sense of how pervasive alternative splicing is, it how many genes are affected is necessary to get a sense of the scope and selectivity of this phenomenon. For example, in the Results section the authors explain the AS junctions in two genes, Cry and CG10483, but do not provide a perspective – how many of the genes with these AS structures have functions relevant to the different neurons in this study and of neuronal populations over other cell types?

3) There were only 10 AS events found in all three groups of neurons (Figure 3B). Was any further analysis done on these? These might be genes that are particularly important as well.

4) The authors could point out the use of other algorithms to identify AS changes – why rely only on JUM?

5) A critical point of this study is the identification of "novel" AS junctions. Therefore, it will be important to have some quality control metrics to show the identified junctions are real rather than technical artifacts or alignment errors. It will be helpful to clearly describe parameters related to accuracy of exon junction identification (e.g., size of overlap on each side of the junction), and if possible provide an estimate of accuracy (e.g. using simulated synthetic exon junction reads by swapping 5' and 3' parts).

6) Related to the point above, it is also important to clearly state the criteria used to define a "novel" AS junction in the main text. As of now, the authors stated in the method section that "The novelty of each AS junction was compared against the library of annotated junctions in the UCSC genome browser transcriptome annotation (genome 422 version: FB2017_05)." It is unclear what type of annotations was used here (e.g., which gene models, does that include EST sequences?)

7) In subsection “Circadian neurons present specific alternative pre-mRNA splicing patterns”, the authors identified AS junctions differentially spliced in each type of circadian neurons compared to TH neurons. They then examined the overlap of the lists to claim most of these junctions are specifically spliced in one subtype. To be more rigorous, one should perform differential splicing analysis between different types of circadian neurons, as the limited overlap could also be due to limited statistical power.

Similar issue for comparison of cycling exons in Figure 6B.

8) While cell type- and time of day-dependent AS patterns are artfully presented here, a major weakness in this manuscript is that the underlying mechanisms driving AS or their consequences on protein expression are not studied. Regarding upstream mechanism, it would help to know if expression of any RNA binding proteins correlate with the observed AS events across cell types or times of day. Regarding the relative impact of AS on neuronal identity and function, a first pass analysis could be to compare the relative numbers and enriched ontologies between mRNA expression and AS differences between cell types and in the circadian data. A more compelling experiment would be to specifically inhibit an AS event within one of the neuronal populations to test its effect on cell function.

9) One potential concern is the technical/biological variation between replicates, which is expected from the small number of cells used to generate RNA-seq libraries and visible from the examples shown in the figures. It will be helpful to have some data to show the reliability/reproducibility of observed differential splicing (e.g., correlation of splicing pattern of replicates, or even independent RT-PCR validation if possible).

10) The observation of alternative exons that are differentially spliced in specific types of neurons or time-of-the-day during the circadian clock is very interesting. Is there any indication of corresponding changes in splicing factors that potentially regulate these AS events?

11) It will be helpful to provide additional functional analysis of identified AS events with differential splicing, in addition to GO. This reviewer understands that detailed functional dissection of specific events might be beyond the scope of this manuscript, but it should be feasible to perform statistical analysis of cross-species conservation, preservation of reading frame, exon size, etc., which is frequently distinct for exons with cell type specific splicing.

12) In Figure 4B, although the authors claim, "in TH and LNd neurons the Shab transcripts preferentially utilize an alternative terminal exon, […] while in LNv and DN1 neurons, the long Shab isoform that encodes all transmembrane regions is dominant", it is not intuitively showing that by looking at the Sashimi plots. The authors should order the samples similarly to Figure 4A, and also may better prove their point by grouping the LNv and DN1 samples or highlighting the relevant differences in the figure read numbers.

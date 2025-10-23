# Peer review - Round 1

Editors:
- Antonis Rokas, https://ror.org/02vm5rt34 Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81406.sa0](https://doi.org/10.7554/eLife.81406.sa0)

The valuable study by Dumeaux et al. examines the transcriptional response to antifungal treatment in the major opportunistic human fungal pathogen Candida albicans. Using solid methodology, including a novel droplet-based single cell transcriptomics platform, the authors report that fungal cells exhibit heterogeneity in their transcriptional response to antifungal drug treatment. The ability to study the trajectories of individual cells in a high-throughput manner provides a novel perspective on studying the emergence of drug tolerance and resistance in fungal pathogens.


---

# Peer review - Round 1

Editors:
- Antonis Rokas, https://ror.org/02vm5rt34 Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81406.sa1](https://doi.org/10.7554/eLife.81406.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Candida albicans exhibits heterogeneous and adaptive cytoprotective responses to anti-fungal compounds" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David Shore (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you will see from the reviewers' individual reports, there was consensus that the manuscript and work reported are interesting but also had concerns about presentation and some of the controls used in the study. Thus, the manuscript will require revision, including potentially additional experiments, and one more round of review.

1) There is concern that there is significant overlap (and lack of clarity) with respect to data previously published (Battauer et al. 2020) and data that are new to this study. It will be imperative to clearly explain where the data in this new manuscript are coming from.

2) There was consensus among reviewers for a revised Introduction section that better sets up the rationale for this study (e.g., Reviewer #2, point #2 and Reviewer #3, point #1).

3) There was concern about the use of different time-points associated with controls vs. treatments (e.g., Reviewer #2, point #4) – addressing this point might necessitate collection of additional data.

Reviewer #1 (Recommendations for the authors):

Since the underlying biology here will be of most interest to researchers who are unlikely to be versed in the experimental and analytical methods used throughout, I think that the authors should make a better effort to help the reader begin to understand the bases of their analytical methods and their potential pitfalls. For example, they don't even define the ubiquitously applied "UMAP" method, much less explain in general how it works, what it reveals, and what its limits might be (though it is defined in the McInnes et al. reference title). I suspect that most readers will be unfamiliar with the details of single-cell transcriptomic analysis, which is complex and relatively recent. Μore science-related comments are as follows:

1. The significance of the dozen or so small "comet" clusters is unclear. On line 525 they are referred to as possible "trimeras" (What does that mean? Should it read "trisomes") "…with unstable genomes previously identified after FCZ treatment…which might have arisen as a response to amino-acid starvation." This latter point might be testable by increasing amino acid concentrations in the medium, which might then abolish the formation of some clusters.

2. In the Discussion the authors describe "bulk DNA-level profiling" of untreated cells and four FCZ treated populations (days 2, 3, 6, and 12). They state that attempts to assign the aberrations they observe to either the α or β response were inconclusive, but it's unclear how this would have even been possible to do. Please clarify. It is also stated in the text that variation levels peak at day 3, but it would seem to me to be day 2. Furthermore, on day 2 there would appear to be a nearly uniform increase in signal for all chromosomes shown, suggesting that there might be widespread trisomy. These points all need to be addressed and clarified.

3. The significance of the so-called "trajectory" in Figure 4A (black line) is unclear to me. From the text, it would appear to me that clusters 3 and 4 represent β-like cells on days 6 and 3, respectively. But what are the expression differences between these two groups? A similar question arises for clusters 1 and 2, which are said to be α-like cells. Does the black "trajectory" line imply a strict mode of transition between these 4 states? Why do α-like cells seem to be predominant when longer times are stated elsewhere to favor the β-like state?

4. The authors should state clearly how fast the cultures are growing (bulk measurement) at the time points they examine, and whether they have any way of knowing the growth rate as a function of transcriptome state and time of drug exposure. Related to this, do the authors imagine that α-like cells predominate early simply because they derive from those cells that had the highest levels of RP and ribosome biogenesis gene expression prior to treatment and thus might have been faster growing and/or more capable of escaping the early effects of drug treatment?

5. What is the actual evidence that β cells are derived from α cells through induction of RASTR in the latter population of cells? Related to his, could it be shown that α cells display a higher level of protein aggregation than β cells, perhaps by looking at RP fusions to GFP, versus HSP70-GFP?

6. Can the authors compare in more detail the transcription states of their β cells to the profile of RASTR cells (S. cerevisiae) described by Albert et al.? For example, are the targets of Hsf1 known in detail in Candida albicans, and if so, how well do they match with the up-regulated genes observed in β cells? Does Hsf1 also target genes encoding components of the proteasome (as in S. cerevisiae)?

7. Furthermore, can the authors show that Ifh1 is "condensed" in β cells, as seen clearly using Ifh1-GFP fusions in S. cerevisiae? In addition, what is known about Ifh1 targets in C. albicans (are they mostly RP genes?), and how well does this group overlap with the profiles of down-regulated genes in β cells? Perhaps the datasets are not robust enough to give this sort of information, but the issues should at least be addressed in the text by the authors.

8. The idea that a kind of persistent RASTR response promotes tolerance is very interesting. Perhaps the authors could test this idea further by asking whether inducing RASTR prior to drug treatment (with diazaborin or an RNA Pol I inhibitor) might strongly increase the fraction of tolerant cells.

9. Line 591: what is meant by "reinitiate translational machinery" with respect to the α cells? And how is this related to their persistence over time?

Reviewer #2 (Recommendations for the authors):

1. This manuscript emphasizes the lack of single-cell transcriptomics in C. albicans (and fungi broadly), although there does appear to be other work published in this area (Dohn et al. 2021 – which also includes antifungal treatment). Relationship to other work in this area should be more clearly addressed, and differences in findings with regards to antifungal treatment should also be addressed.

2. The introduction to this manuscript is framed around antifungal drug tolerance, and throughout this research, antifungal tolerance is highlighted as a central research question. However, it is not clear how the experimental design of this work addresses antifungal tolerance in any way. Cells are treated with antifungal drugs and subjected to transcriptomic analysis, but this does not represent a distinct 'tolerant' population of fungi that are being analyzed. This either needs to be much more clearly explained and justified, or more likely, the framing of this work needs to be substantially re-assessed.

3. The authors make reference to another study of theirs (Battauer et al. 2020) and suggest that the transcriptomic profiles reported in this work combine profiles from their previous work. This needs to be much more clearly explained. Have parts of this work already been previously published? How is this analysis unique and novel? The title of the previous manuscript seems very similar to that of this manuscript suggesting there might be a substantial overlap between these works.

4. The major analysis in this work compares untreated cells in log phase, to antifungal drug treated cells grown for 2-3 days in antifungals. It is not clear why untreated cells were not grown for the same duration of time as drug-treated cells, which would certainly alter the findings and analysis. It is thus unclear if the transcriptomic responses described in this manuscript truly represent the consequence of drug treatment itself, or are also influenced by the growth state of the cells (which are in stationary phase after 2-3 days of drug treatment). A comparison to untreated cells in stationary phase would be a more appropriate comparison.

5. The work describes the identification of 184 transcripts on average in each cell, which seems like an incredibly small number. Is this in line with other similar single-cell transcriptomic analysis? Does this number of transcripts enable robust conclusions to be drawn on the transcriptional profile of individual cells?

6. While the paper is generally well written, it is written in an extremely technical manner with much methodological detail (as well as discussion) incorporated throughout the main Results section. Major Results sections also lack clear and concise conclusions to help readers understand and interpret the major findings. This diminishes the clarity of the work and makes the manuscript at times quite dense and difficult to fully interpret.

7. It is unclear why stress response pathways are being assessed in untreated cells without any stress exposure. Should this be analyzed in the drug-treated cells instead?

8. In the growth curves in Figure 3 Supp 1a, it seems that both untreated and drug-treated cells take 2-3 days to reach stationary phase. This seems very unusual for cells that replicate quite rapidly under many growth conditions. Is this due to a nutrient-limited media or some other explanation?

9. It seems surprising that extremely different antifungals (cidal vs. static, different cell targets) elicit a very similar transcriptional response based on this analysis (line 345-348). Can this be explained?

10. Section 8-9 on expanding the analysis to day 6 was difficult to interpret in terms of the rationale for the experimental design and how the findings can be interpreted. It is also unclear how solid agar media-based tolerance assays can be extrapolated to liquid media growth assays with drugs, as these are very different conditions. It is also unclear if there is a day 6 untreated control that is being assessed.

a. The microscopy in associated Figure 4 K is very difficult to see and lacks scale bars.

Reviewer #3 (Recommendations for the authors):

Below I provide a few suggestions for how the authors may improve the manuscript, but overall I found it well done.

1. First, it is my understanding that tolerance is defined as survival, but not growth, after exposure above the MIC for drugs that normally would kill most of the population of cells (for non-static drugs). This is the definition put forward in Balaban et al. ("Definitions and guidelines for research on antibiotic persistence"; Nat Rev Microbiol; 2019). I would have called what the authors describe as phenotypic resistance, i.e., a sub-population of cells that can continue to grow after exposure above the MIC, and a non-genetically heritable state (i.e., readily reversible). This is a known phenomenon for some antimicrobials/species combinations, as the authors describe. I think it would be good to standardize usage of the word tolerance through the manuscript, or the authors can better explain how the phenomenon they observe is consistent with Balaban et al.'s definition of tolerance. This is an important semantics issue. Second, the drug concentrations used were at or well-below their MICs. This raises the question of whether the authors are studying the clinical phenomenon that they describe as tolerance (i.e., above the MIC) when the experiment was conducted below the MIC. While I understand their reasoning for using low drug concentrations, and I think there is still something to be learned at these concentrations, I think the authors should better contextualize the clinical relevance of their findings with the caveat that the experimental results were probably collected at sub-clinical concentrations. Admittedly, drug concentration is dynamic during treatment, so at some point the concentration in vivo likely passes through the author's choice of in vitro concentrations. It would be interesting to know how much their results are invariant to the drug concentration chosen.

2. The author's interpretation of the "comets" is questionable. On L244 they say, "This pattern suggests that the small set of cells from each comet have strong transcriptional similarity but each such comet is transcriptionally distinct from the other comets." I do not see how the cells within comets share "strong" transcriptional similarity because they are still spread out. Rather, the comet tails could be interpreted as lineages of descent, wherein each cell becomes more distinct (along some transcriptional axis) than its ancestor. This pattern is commonly observed in genetic data plotted with PCA, which is somewhat related to what is being shown here. Therefore, an alternative interpretation is that some lineages are moving toward a transcriptionally distinct state and leaving behind progeny along their trajectory, especially given that the experimental setup may not quickly remove ancestral cells in the two day exposure. Another explanation is that the comets are composed of a different (minority) morphology, such as filamentous growth. Another (less?) plausible interpretation is that these are noise clusters due to the inherent stochasticity involved in single-cell analyses. I see no reason why these explanations aren't equally reasonable to the author's explanation. Perhaps the authors can incorporate these alternative into their interpretations, but (at a minimum) there needs to be more justification given for the claim of "strong" intra-cluster transcriptional similarity.

3. L434: I am skeptical of the author's interpretation here about the relative fitness of α and β states. It could also suggest switching rates between phenotypic states are different between α and β populations. Also in this paragraph (L439), the authors use OD600 to show a higher growth rate for β over untreated. However, β also reaches a higher yield, which is unexplained. Having done many growth rate experiments with OD600 data, I am always skeptical of drawing large inferences about fitness from OD600. A better test of fitness is a competition experiment. I suggest the authors remove or downplay their conclusions about relative fitness here. Also, why isn't OD600 plotted in log-space (log(OD600)) if the goal is to see the difference in growth rate?

4. The authors did not seem to analyze feature importance in Leiden clustering, preferring to look at cluster associations (z-scores) instead. Leiden clustering is not guaranteed to be optimal, so some understanding of cluster stability would have been useful. That is, if inputs changed somewhat (e.g., subsampling or resampling), would the identified clusters have been similar? This is particularly important given that the UMAP1 versus UMAP2 clusters look like blobs that are split along arbitrary axes. It seems doubtful these clusters are stable, yet the whole manuscript analyzes them as though the blobs are discretized correctly.

5. I have some concerns about the comparison between untreated and treated at the same (or similar) time points. If the transcript profile changes over time, as presumably it would, then it is reasonable to expect that the treated and untreated cells are at different equivalent times because their growth rates are different. I have a similar concern with comparing different time points (days 3 versus 6) because fresh medium (YPD) was used in this experiment. How much are transcript abundances static over time? This should minimally be discussed further in the manuscript. Also, the conclusions in L472-475 and L579-592 may need this caveat mentioned.

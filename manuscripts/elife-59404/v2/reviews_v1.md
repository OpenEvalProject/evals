# Peer review - Round 1

Editors:
- Job Dekker, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59404.sa1](https://doi.org/10.7554/eLife.59404.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript describes a method, named SAMOSA, to identify nucleosome positions along chromatin segments that can be over 10 Kb in size. The approach employs EcoGII-modulated m6dA deposition on accessible non-nucleosomal DNA (inkers, nucleosome free regions) released from nuclear after mild MNase cleavage. The DNA modification is then read-out using PacBio sequencing. Mapping nucleosome positions along longer DNA stretches can provide information on variation in nucleosomal arrays, and how that relates to chromatin state and factor binding etc. The assay is validated using a reconstitute chromatin template and then applied to K562 cells, revealing significant variation in nucleosome positioning and nucleosome repeat lengths at transcription factor binding sites, and throughout domains with various histone modifications.

Decision letter after peer review:

Thank you for submitting your article "Massively multiplex single-molecule oligonucleosome footprinting" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Job Dekker as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Naama Barkai as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript describes a method, named SAMOSA, to identify nucleosome positions along chromatin segments that can be over 10 Kb in size. The approach employs EcoGII-modulated m6dA deposition on accessible non-nucleosomal DNA (inkers, nucleosome free regions) released from nuclear after mild MNase cleavage. The DNA modification is then read-out using PacBio sequencing. Mapping nucleosome positions along longer DNA stretches can provide information on variation in nucleosomal arrays, and how that relates to chromatin state and factor binding etc. The assay is validated using a reconstitute chromatin template and then applied to K562 cells, revealing significant variation in nucleosome positioning and nucleosome repeat lengths at transcription factor binding sites, and throughout domains with various histone modifications.

Essential revisions:

Overall the approach works well and promises to address important questions, but the current work does not yet take full advantage of the single molecule nature of the assay and as such falls a bit short compared to very related methods that have recently been published (the works cited in the manuscript, and recently published work from the Stamatoyannopoulos lab). Can the authors acquire sufficient read coverage so that specific sites, e.g. specific CTCF sites are analyzed multiple times so that variation in the cell population at defined sites can be explored?

Many of the claims made about the potential of the method are insufficiently supported by the data provided. It appears that additional data is required to support the conclusions made from SAMOSA with respect to existing chromatin information, such as signal differences as a function of transcription factor binding (see below). The authors need to fully address these points in order for this manuscript to be considered for publication.

1) The authors should make an attempt to investigate where sequence bias influences a methylation call in their datasets. Clearly the pattern on the in vitro chromatinized template suggests that on average their methylated calls are correct. However, there appear to be clear positions in their chromatinized template datasets where this is not the case, i.e. lines in Figure 1—figure supplement 6A representing methylation calls in unmethylated template DNA and unmethylated calls on fully methylated template DNA. Upon close examination, this also seems the case in the chromatinized template, with certain positions inflexibly methylated/unmethylated and at odds with the surrounding linker/nucleosome patterning (Figure 1D). The authors should use K-mer analysis of methylated A's genome-wide to detect sequence bias in either the methyltransferase or sequencing platform.

2) It seems reasonable that the clustered data by NRL estimate (Figure 3) should correlate with existing measurements (i.e. MNase-seq). The authors should identify regions of the genome with strong enrichment for the seven clusters and compare this to nucleosome repeat length as can be estimated using conventional MNase measurements, i.e. the average distance between 5' mapping read positions across the genome (Valouev et al., 2011, Teif et al., 2012). Some agreement (for at least a few of these clusters with very regular nucleosomes) would strengthen the conclusions made by this approach, especially where there are irregular positioning patterns. Additionally, for these clusters the authors should display raw read alignment/methylation calls for SAMOSA at a few representative loci, where a sense of the raw data can be gleaned.

3) The comparisons of SAMOSA at different TF bound regions is likely influenced by the fraction of actually TF-bound molecules present in the original cellular sample. For example, CTCF is known to occupy it's strong motifs in the majority of cells, while few other factors have such regular binding/residency (Kelly et al., 2012 NomeSeq data at CTCF sites). It seems reasonable that some cluster fractions should scale with the enrichment for the factor (for at least CTCF and REST, the strong binding/nucleosome positioners), especially those associated with chromatin accessibility at the motif (i.e. A-accessible, HA-hyper-accessible). The authors should try to illustrate this, as well as representative read alignments/methylation calls at a few loci where these signals are prevalent.

4) The meta-plotted data seems noisy for most TFs profiled (Figure 4A-L) and the authors should show that their replicates agree with each other in terms of the relative size of clusters and at the metaplot level. Similarly, the data shown in Figure 5 should be broken into replicates. It is difficult to know to what extent the differences quoted are quantifiable/reproducible. For example, in panel A the reported deviation seems quite large around the median to make strong claims: e.g. "In specific cases, we observed small effect shifts in the estimated median NRLs for specific domains-for example, a shift of ~5 bp (180 bp vs. 185 bp) in H3K9me3 chromatin with respect to random molecules.…". This should also apply to the analysis done in Figure 5B and C, where it is difficult to get a sense of reproducibility from cluster size and the heatmap of Odds ratio and q-values.

The use of mild MNase is presented as an advantage, but is it really necessary? Adding EcoGII to isolated nuclei may work as well as shown in the recent Stamatoyannopoulos paper in Science.

In Figure 5, controls are randomly chosen nucleosomes, but it would be interesting to see what unmarked nucleosomes show. For example, unmarked alpha-satellite should be dominated by highly regular arrays with a 171-bp repeat length present in higher-order repeats corresponding to active centromeres, which consist of nucleosomal complexes that lack Histone H3 (CENP-A instead). The authors speculate that satellite irregularity might result from dynamic restructuring by HP1, and this predicts that other (H3-containing) unmarked satellites that lack H3K9me3 and presumably lack HP1 will be in regular arrays.

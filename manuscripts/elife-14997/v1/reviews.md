# Peer review - Round 1

Editors:
- Eve Marder, Brandeis University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.14997.027](https://doi.org/10.7554/eLife.14997.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Hipposeq: a comprehensive RNA-seq database of gene expression in hippocampal principal neurons" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

1) Please note that the most important issue that arose during the review is that the reviewers did not have access to the web site with the actual data nor to the analysis code. As you know, eLife will expect you to make both of these public, and it seems reasonable that the reviewers should have access to these in order to make their final judgments of the work. Consequently, along with preparing a revision to be responsive to the issues raised below, please ensure that these are available to us at the next submission. One of the reviewers requested that you use GitHub (or equivalent) rather than FigShare.

Summary:

This manuscript describes gene expression datasets for several classes of excitatory hippocampal neuron: CA1 (dorsal and ventral), CA2 (dorsal) and CA3 pyramidal cells (dorsal and ventral), DG granule cells (dorsal and ventral) and DG mossy cells (dorsal). The datasets appear to have been carefully generated and analysed, and the results and methods are clearly described. It is likely the datasets will be useful as a "ground truth" of population level gene expression profiles of each of the investigated cell types.

Points for revision:

1) The study claims to have characterised gene expression for every excitatory neuronal class in the hippocampus. While we agree the major classes have been characterised, there are additional excitatory cell classes that were not investigated, e.g. semilunar granule cells in the dentate gyrus (Williams et al., J. Neurosci. 2007; Larimer and Strowbridge, Nature Neuroscience 2010), radiatum giant cells in CA1 (Gulyas et al., Eur. J. Neurosci. 1998; Bullis et al., J. Physiol. 2007), and CA3 granule cells (Szabadics et al., J. Neurosci. 2010). These classes have distinct morphology and biophysical properties. It would not be surprising if their gene expression profiles are also distinct. Given the good evidence for these additional excitatory cell classes, the claims for completeness should be qualified and the excitatory cell classes not characterised should be acknowledged.

2) The replicate correlation score is much lower for granule cells. Is there a known reason for this? Were granule cells sampled from upper or lower blade of the DG? Or both? Is there a difference?

3) Mapping of reads used TopHat. For many applications this has been superseded by STAR (Dobin et al., Bioinformatics 2013) which has been suggested to map more accurately. It might be worth checking whether this gives improvements sufficient to reveal any additional differentially expressed genes.

4) The Hipposeq resource is referred to multiple times in the manuscript, but is not accessible so it is not possible to comment on the "resource" aspect of the manuscript. It's also not clear what the resource provides that could not be achieved by downloading the data via GEO and using standard analysis tools. Ease of use? Novel analyses?

5) Materials and methods. '12-hour light/dark cycle'. At what time were the animals sacrificed? If the time differed between animals, does this contribute to any variance in the data?

6) In the last paragraph of the subsection “Generating a cell- and region-specific RNA-seq database for the hippocampus”. How many cells (mean ± SD)? I think this is in the Methods, but would be helpful to make clear in the Results section.

7) In the first paragraph of the subsection “Manual sorting, library preparation, and sequencing”. Which C57bl/6 strain? If not generated on this background, for how many generations are the lines back-crossed?

8) How was the integrity of the RNA assessed? E.g. was there a threshold RIN value?

9) There is increasing evidence for diversity of CA1 along the radial (deep vs. superficial) axis. Please consider.

10) The figure legends are a bit sparse and could benefit from adding a more detailed description of the data.

11) Figure 1—figure supplement 1. Please label the various panels with the identity of the transgenic line.

12) Although some mouse lines do show fairly specific expression limited to specific subregions, other lines show very broad patterns of expression, particularly for CA2 (Figure 1—figure supplement 1). How did the authors manage to get a CA2-specific population to examine?

13) Did the authors look for inhibitory specific cell markers (e.g. GAD65,67) to judge the level of contamination from inhibitory neurons?

14) Please give a better description of the bar graphs in Figure 2B, 4C, etc. Is the x-axis the cell type? If so, it would be helpful to indicate this on the panels and in the legend. Also, what is the y-axis? FPKM? Please define. The normalized color plots of FPKM are hard to understand, and the description in the Methods are obscure for a non-expert. What is the being normalized? The bar-graph quantification much more useful than the normalized color plots. Perhaps the authors may wish to include a table in the supplemental material listing actual fold differences in expression of various genes?

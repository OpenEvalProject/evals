# Author response - Round 1

Authors:
- Toshiharu Ichinose ([ORCID: 0000-0002-6845-9403](https://orcid.org/0000-0002-6845-9403))
- Shu Kondo ([ORCID: 0000-0002-4625-8379](https://orcid.org/0000-0002-4625-8379))
- Mai Kanno
- Yuichi Shichino ([ORCID: 0000-0002-0093-1185](https://orcid.org/0000-0002-0093-1185))
- Mari Mito
- Shintaro Iwasaki ([ORCID: 0000-0001-7724-3754](https://orcid.org/0000-0001-7724-3754))
- Hiromu Tanimoto ([ORCID: 0000-0001-5880-6064](https://orcid.org/0000-0001-5880-6064))

## Response text

DOI: [10.7554/eLife.90713.3.sa3](https://doi.org/10.7554/eLife.90713.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer 3:

Response to authors' revisions:

This reviewer is not convinced that the authors have done enough to satisfactorily address either of the major issues described in the original public review, above.

They're still not providing a quantification of Fig. 5D (originally 5C).

Their response regarding the expression pattern of Rh1 is particularly concerning, as it represents a misinterpretation of previously published data.

The gene encoding Rh1, ninaE, is expressed at such high levels in R1-6 PRs that any RNA-seq data (bulk or single-cell) generated from the optic lobes, no matter what cell-type, will display some ninaE transcripts that are present in the background, as they leak from R1-6 during dissociation steps. This phenomenon has been well described, for instance in Davis et al., 2020, eLife, and in fact led to the development of computational tools to abate such artifacts. In other words: no, rh1 is not expressed in glia, or any other neuron besides PRs for that matter. Therefore, I remain deeply suspicious about the functional relevance of the regulatory mechanisms described in this paper.

We thank the reviewer for her or his critical comments.

We quantified the cell-type differences in translation of the reporter with Tub-GAL4 and now show the results in Figure 5F. Consistent with other results, this analysis revealed that the glia-to-neuron ratio of the reporter protein expression is significantly lower when it contains the UTR sequences of rh1.

We removed the mRNA counts (former Figure 5A and Figure 5 - figure supplement 1A), as we agree that these may well be contaminated by the very high rh1 expression in R1-6. We also amended the graph showing the ribosome distribution on the rh1 mRNA (Figure 5B) to better compare the translational efficiency (footprints normalized with mRNA, in a similar manner to Figure 3C). Now it clearly highlights the cell-type differences of footprint distributions; ribosomes are much more enriched on the CDS (being translated) in neurons, while the fraction of ribosomes on the 5ʹ leader (being stalled) is much higher in glia. We summarized this differential ribosome distribution in a new graph (now Figure 5C).

We apologize for the misleading description of the reporter experiments. Despite the high level of mRNA expression in the R1-6, we chose the 5ʹ leader of rh1 for the translation reporter, as it contains clear uORFs and differential ribosome accumulation thereon (Figure 5B). This biased ribosome distribution and differential translation are the consistent features for many neuronal genes (Figure 3). We revised the text to clarify this point (Line 195-203).

In summary, we provide more rigorous analysis and extensive revision, which we hope clarified the concern.

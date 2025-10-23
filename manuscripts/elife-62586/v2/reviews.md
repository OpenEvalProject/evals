# Peer review - Round 1

Editors:
- Melanie M Brinkmann, Technische Universität Braunschweig Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62586.sa1](https://doi.org/10.7554/eLife.62586.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Single-cell characterization of transcriptomic heterogeneity in lymphoblastoid cell lines" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Erik K Flemington (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers clearly appreciated your work which, by including five LCL cell lines from different donors and two different virus strains, generates a valuable resource to understand the dynamics between latent and lytic infection in EBV-infected B cells and B cell differentiation versus activation. However, the results and conclusions were not really validated and the work remains quite descriptive. We came to the conclusion, especially taking into regard the comments of reviewer #3, that this work in its current state is not of profound general interest to the readers in the non-EBV field and therefore not suited for publication in eLife.

Reviewer #1:

The authors report single cell RNA sequencing of five LCL lines. Three of them are recently derived, two with the B95-8 and one with the M81 EBV, and two have been in culture for prolonged periods of time. Two LCLs are from the same donor, one B95-8 and one M81 transformed. Three are predominated by IgG switched memory, one by IgA switched memory and only one by IgM, originating from naïve or unswitched memory B cells. Interestingly, B cell activation and NF-kappaB expression correlates inversely with both antibody isotype class switching and plasma cell differentiation. Lytic EBV gene expression can only be observed in a small subset, primarily in the LCLs from the same donor transformed with B95-8 and M81 viruses but is not higher in the M81 transformed LCL. Finally, the authors model how heterogenous LCL composition might evolve, but the GM12878 cell line demonstrates that this does not necessarily drive to clonality in all instances. The authors suggest that LCLs go through a founder bottleneck that renders possibly every LCL different and that this should be taken into account in using these cellular models.

The study described the comprehensive analysis of five LCLs and generates a valuable resource to understand the dynamics in EBV infected B cells between latent and lytic infection and B cell differentiation versus activation. However, some more information on the correlation of LCL proliferation with gene expression, latent EBV gene expression and antibody isotype composition from uninfected to LCL to lytic reactivation should be provided.

1) The gene expression analysis suggests inverse correlation of B cell activation and differentiation. Is this reflected by LCL proliferation in vitro? Do the LCLs with higher frequencies of differentiated LCLs proliferate slower than for example LCL777 B95-8.

2) The authors report lytic EBV gene expression, but presumably latent transcripts were rarely sequenced due to their low transcript number per cell. Nevertheless, it would be interesting if LMP1 expression frequency is elevated in LCLs with higher frequencies of activated cells and diminished in IgA or IgG expressing cells. The authors should attempt to address these questions by alternative means like flow cytometry or immune fluorescence microscopy.

3) Does lytic EBV reactivation occur in all antibody isotype carrying subpopulations similarly, or is it enriched in XBP1 positive IgG and IgA carrying B cells? Is there any preference between IgA and IgG expressing differentiated B cells?

4) Do the LCLs reflect peripheral B cell composition of the donors at all? Does for example donor 777 have a higher percentage of IgA positive B cells in the peripheral blood than 461.

5) GM12878 might argue that LCL composition could be stable over time in some LCLs and not necessarily drift towards monoclonality. Do the authors have any longitudinal information on BCR isotype composition in their investigated LCLs?

Reviewer #2:

This paper demonstrates fairly wide diversity of cell transcriptomes within EBV derived LCL populations. This intra-cell population diversity extends even to cell lines that have been in culture for many years. This likely speaks to the principles driving transcriptional activation which derives from chance intermolecular interactions that are albeit favored or disfavored based on changes in chromatin and chromatin domain structures. The relevance is that the certain level of randomness of these principles can lead to dynamic changes in entire transcription and differentiation programs even within a single cell population. While there is already evidence for these kinds of issues in cell populations, this work brings out these principles in the context of LCLs/EBV (particularly striking are the findings of the presence of plasma blast-like populations and marker-less subpopulations. Overall, this paper provides important insights into the transcriptional and phenotypic diversity that exists in what might have previously been perceived as mostly uniform cell populations of tissue culture LCLs.

The authors have also been able to identify unique transcriptome signatures for reactivating cells which is potentially interesting from the standpoint of informing us on the nature of apparently stochastic events that trigger this transition to the EBV lytic phase. Nevertheless, given the lack of detection of BZLF1 (and possibly other lytic transcripts?), it would be helpful if the authors could provide additional evidence that these are true lytic cells vs abortive lytic cells (the latter of which would itself would be an interesting finding). It would be helpful if the authors could plot distributions of the percentage of viral lytic transcript reads to cell transcript reads in these populations of cells (this is hard to gauge from Figure 3C). Since herpesviral lytic infection typically results in a substantial proportion of lytic transcripts (minimum of 10% of all reads), this would help determine whether most of these cells are truly lytic or abortive lytic (perhaps through some epigenetic changes that lead to a higher level of transcriptional bursting of the EBV genome).

Reviewer #3:

Summary: Lymphoblastoid Cell Lines (LCLs) are induced by infecting primary B cells with Epstein-Barr Virus (EBV) and constitute a widely used cell line model in molecular biology, oncology and immunology. Understanding the intra- and inter-heterogeneity of these cell lines using single-cell analysis is key to design research and interpret experimental results. The authors induced three cell lines using two EBV strains and they performed single cell RNA-seq using the 10x platform and conducted a very classical analysis using Seurat. They added two datasets from the literature (Osorio et al., 2019). They describe that each cell line has a certain level of intra-heterogeneity with different Ig expression patterns, different maturation stages (Figure 1 and 2), as well as exhibit different viral lytic/latent stages (Figure 3) and mitochondrial gene expression (Figure 4).

General comments: This study is needed and interesting as a resource for the community of scientists using these cell lines but I see major problems in the design of the study and the analysis. Beyond doing scRNA-seq and displaying clustering analysis, the final aim and the novelty of the study are not clear to me. It is neither clear how one can use such analysis to guide his research. As presented, the data analysis is very preliminary (Figure 1—figure supplement 15-19 and Figure 4—figure supplement 1-4) and the study needs substantial improvements before publication in a top-tier journal such as eLife. No functional analysis is provided to indeed demonstrate that intra- and inter-variability has implications in study design.

1) Design of the experiments: the overall scope of the study is very limited with only five different donors and it is not clear what is the contribution of the different viral strains. The rational of the study design is not outlined. The authors have chosen to look at the transcriptome only; we would have expected to have more -omics for a resource paper such as ATAC-seq and methylome to document the underlying heterogeneity of the cells.

2) The description of the variability of LCLs is not novel. Ozgyin et al., 2019 have already provided a genotype-independent functional genomic variability of the LCLs. This study is not quoted.

3) The variability between the five LCLs is not clearly delineated. Each cell line is heterogenous (Figure 1 to 4) but the authors have studied the cell lines independently without attempting to merge the data. The inter-heterogeneity is very poorly documented. The data analysis to perform a merge would require substantial computational work that goes beyond the scope of a two-month revision. It would be very important to explain the contribution of the inter-individual genomic variability between donors.

4) The authors claim in the Abstract that "This heterogeneity is likely attributable to intrinsic variance in primary B cells and host-pathogen dynamics." In a publication in a top journal such as eLife, we expect that such a claim is documented with experiments. The authors claim that "primary cell heterogeneity, random sampling, time in culture, and even mild differences in phenotype-specific fitness" can contribute to such heterogeneity. These are very general claims that do not help and are not supported with experiments.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Single-cell characterization of transcriptomic heterogeneity in lymphoblastoid cell lines" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Päivi Ojala as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Erik K Flemington (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Lymphoblastoid Cell Lines (LCLs) are induced when primary B cells are infected with the human herpesvirus Epstein-Barr Virus (EBV) and are a widely used model in molecular biology, oncology, and immunology. The authors have used single cell transcriptomics to demonstrate substantial phenotypic heterogeneity within and across LCLs. Hence, this work is important for researchers working with LCLs for the design and interpretation of experiments.

Revisions:

Please include in your discussion the points raised by reviewers #1 and #3 about the limitations of this study:

Reviewer #1: Due to lack of donor material prior to transformation by EBV the authors could not assess if the heterogeneity of their cell lines was donor dependent. Furthermore, they could not provide any information on the longitudinal stability of the reported heterogeneity.

Reviewer #3: It remains to uncover the origin of this variability using other layers of -omics and longitudinal sampling of the cells along the transformation process.

# Peer review - Round 1

Editors:
- Chris Q Doe, https://ror.org/0293rh119 Howard Hughes Medical Institute, University of Oregon United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86127.sa0](https://doi.org/10.7554/eLife.86127.sa0)

This is an important study that defines the role of the FruC transcription factor in key developmental decisions during neurogenesis in Drosophila. The authors combine genetics and genomic profiling to provide convincing evidence that FruC-regulated gene expression is correlated with changes in repressive histone marks. This study will be of wide general interest to the developmental biology field.


---

# Peer review - Round 1

Editors:
- Chris Q Doe, https://ror.org/0293rh119 Howard Hughes Medical Institute, University of Oregon United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86127.sa1](https://doi.org/10.7554/eLife.86127.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Low-level repressive histone marks fine-tune stemness gene transcription in neural stem cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Chris Doe, as Reviewing Editor and Marianne Bronner as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Irwin Davidson (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Add statistical analysis to Figures 5, 6, and S4. Alternatively, explain why this is not possible.

2) Provide a more direct measure of gene expression e.g. rt-qPCR, RNA-seq, or nascent RNA-seq. Alternatively, explain why this is not possible, and temper quantitative claims accordingly.

Reviewer #1 (Recommendations for the authors):

Comments:

1) The authors indicate that FruC is the predominant Fru isoform, but don't show the data for A and B, the other isoforms they examine. This data should be included to support their conclusion.

2) The authors use an Engrailed Repressor Domain (ERD) fusion with the FruC DNA binding domain to argue that FruC normally has a repressive function. The authors do not provide references or any support that the ERD is functional in type II neuroblasts and/or in their chimeric protein.

3) The authors argue in several places in their study that they validate antibodies by performing staining in the brat-null genotype. How does this validate the antibody? Is their independent data to support that is the expected expression pattern? Did the authors examine loss-of-function tissues?

4) The genotype of animals used in the study is often not clear. What is the Fru allele used other than the FruC allele? How were clones generated? Additionally, some of the shorthand is not clear in the figures. The FruSat allele they mention early on appears to be a large deletion. Could the loss of other genes be an issue in their study?

5) In the UMAP plots, the authors do not indicate what the colors show. For example, what is orange vs black in Figure 1F? Please check all figures.

6) Figure S1 B-The lower panel appears to be incorrect. The text said it shows the percentage of mitochondrial genes. This error also makes it difficult to determine the quality of the scRNA-seq data.

7) The microscopy images often point to small changes that are not obvious, but the authors use these to make conclusions. The authors should consider how to better show the regions to support their claims.

8) How were the data randomized in Figure 3A? How were enriched genes defined in D. Why are only the genes in parenthesis shown over the UMAP?

9) The way the authors indicate significant differences in some of the graphs is unclear. For example, in Figure 4E what does the ** indicate is different? The two lower rows of microscopy images do not appear different by eye. What are the arrows pointing to?

10) The authors should provide their code and data sets in a public repository. The authors should provide all the gene lists from the single cell and cut-and-run analyses. They should also have the statistical criteria used for their identification in a supplemental table.

11) How were the larvae genotyped? Was this using molecular techniques or phenotypic markers?

12) How were microscopy images quantified? Was the observer blind to genotype?

13) Have the authors considered finding genes with bivalent modification--those with both activating and repressive histone modifications. These genes are thought to be cell fate identity genes.

Reviewer #2 (Recommendations for the authors):

In the first section of the results, the authors use scRNA-seq to characterize the neural populations. As an alternative to the candidate approaches that the authors have used to identify key regulators can they also use unbiased computational regulome approaches (for example SCENIC) to predict other potential regulators that may be involved in key developmental decisions?

On page 9 and many other times throughout the text the authors state that Fru 'fine tunes' the expression of Notch effector genes. While the basis for this conclusion comes from the elegant genetic analyses, at no point do the authors directly measure gene expression in any of the genetic backgrounds. The authors should perform RT-qPCR analyses of the expression changes of key regulatory genes (or better still RNA-seq or even better nascent RNA-seq). It is important to do this to have some type of precise measure of transcriptional changes as the authors' model is based on subtle changes in H3K27me3. It would be important to quantify and correlate both processes more precisely.

A key aspect of the author's model is the changes in H3K27me3 levels at key target gene loci. However, the data illustrated in Figure 5 are rather confusing. First, the levels of H3K27ac are reduced upon Fru deletion as are the levels of H3K27me3. This issue is that the regions labelled by H3K27ac and H3K27me3 do not overlap. As regions with H3K27ac correspond to active enhancers it is clearly not these regions that are being targeted by H3K27me3. What is the evidence that the regions showing altered H3K27me3 are actually relevant for regulating target gene expression? Can the authors make a more global comparison of regions marked by K27ac and K27me3? In addition, the authors state that Fru promotes 'low levels' of K27me3 at its bound loci throughout the genome. How do the authors define 'low levels' low compared to what? What are the cut-off criteria that they use to define low versus high levels of HK27me3?

While the experiments in this paper are well carried out, the conclusions drawn should be carefully considered. The authors state 'Our data indicate that FruC likely functions together with PRC2 to dampen the expression of specific genes in mitotic neuroblasts by promoting low levels of H3K27me3 enrichment at their enhancers and promoters (Figure 7). We propose that local low-level enrichment of repressive histone marks can act to fine-tune gene expression.' As mentioned above there are no direct measurements of gene expression and in fact, what the data show is that changes in H3K27me3 correlate with altered gene expression. There is no direct molecular mechanism described. The above suggested that nascent RNA-seq would be useful to directly demonstrate that Fru directly affects transcription, but the authors could also perform Cut&Run for Pol II to ask which stages of transcription Pol II recruitment and PIC formation or pausing/elongation are targeted by Fru. For the moment, there is only a correlation with changes in histone modification. Either the authors should tone down the conclusions or perform additional experiments that do actually address a molecular mechanism by which Fru alters gene transcription. Either way, it is essential that changes in gene expression be directly assessed.

The authors should be careful with the figure annotation as lettering for panels is often missing.

Reviewer #3 (Recommendations for the authors):

The overall results of the work are compelling and experiments were performed thoroughly.

1) In the description of the results presented in Figure 1, it would be of relevance to clearly state the drivers used.

2) Figure 1 F – it would be easier to represent the expression of the different markers in the format of a dot plot so that colocalization of expression is easier to assess. If the authors choose to leave it as is a legend the colors should be added.

3) Figure 1 F – why these markers were used (TTFs) should be included as well as corresponding references.

4) Figure S1B -These plots could benefit from some more explanation.

5) In Figure 2 it would be of high relevance to include results for other fruitless isoforms, just as presented for fruc in Figure 2C.

6) In Figure 2 – The expression of markers is not easy to assess. For instance, in 2F only one Dpn+Ase- can be visualized and the Dpn staining is very dim and does not seem nuclear. If possible, include more representative images.

7) Quantifications should be presented for Figure 2D, E.

8) In Figure 2L: include values above the graph and not in the middle.

9) In Figure 2M-O it is barely possible to distinguish any Asense or Prospero staining. Possibly select better representative images, maybe include fewer arrows.

10) In this same section, where it is said "This result indicates that Fruc overexpression is sufficient to restore differentiation in brat-null brains" should read instead "is sufficient to partially restore (…)".

11) In figure 3G, what would be the expected random overlap, considering the big difference in peak numbers between the different datasets? (9301 peaks for Fru and 305 peaks for Su(H)).

12) In Figure 4, representative images of the quantifications would be relevant;

13) In FigS4 and Figure 5 it would be important to include the number of significant events in the volcano plots (which can be included in the figure itself);

14) One concern, and according to the Materials and methods, fruc::myc, which you used for the genome-wide studies, is a UAS/Gal4 system. Hence, this might mean that there is an overrepresentation of fruc binding sites that might be more subtle in biological situations. Did the authors perform any CUT&RUN experiments using the fruitless common antibody in a wild-type background?

15) Do the authors know what happens to PRC2-bound peaks in the absence of fruc? Or, in contrast, what happens to fruc-bound peaks when PRC2 subunits are absent?

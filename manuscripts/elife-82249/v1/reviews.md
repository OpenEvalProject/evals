# Peer review - Round 1

Editors:
- Filippo Del Bene, https://ror.org/000zhpw23 Institut de la Vision France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82249.sa0](https://doi.org/10.7554/eLife.82249.sa0)

The study describes the discovery of two related micro-peptides that regulate zebrafish behavior by affecting chromatin accessibility in the embryonic brain. Zebrafish mutants lacking these micro-peptides show altered gene regulatory networks that preferentially affect oligodendrocytes and cerebellar cells in the embryonic brain. The data presented in the study is solid and presents convincing additional evidence for versatile functions of micro-peptides.


---

# Peer review - Round 1

Editors:
- Filippo Del Bene, https://ror.org/000zhpw23 Institut de la Vision France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82249.sa1](https://doi.org/10.7554/eLife.82249.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "linc-mipep and linc-wrb encode micropeptides that regulate chromatin accessibility in vertebrate-specific neural cells" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by and Marianne Bronner as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The evolutionary analysis should be expanded significantly which will increase the scope of the results. What happens in other fish species (teleosts but also coelacanth/gar)? Do they also have both proteins? What happens in frogs/birds/reptiles? A multiple-alignment showing the proteins from different representative species of HMGN1 and the new proteins will be particularly informative.

2) In the initial screen, it is not clear how the candidates for testing were selected and what kind of mutations were introduced in the F0, and what was the efficiency of the editing. As the paper is presented at least in part as an innovative screening effort, it is important to provide these details and outline them in the Results section.

3) A ChIP-seq experiment of the new proteins appears to be very interesting, but it is basically not described at all. How many peaks were found? Do they resemble each other? How reproducible was the data? A motif-based analysis appears to be very superficial given how instrumental these data (if solid) can be.

4) The authors should show ribosome profiling data together with the gene structure of examined transcript (ideally, supported by RNA-seq) to visualize the position of ribosome-protected regions within the transcripts (Extended data Figure 1a and Figure 1d). The sequence analyses reveal the similarity between linc-mipep and linc-wrb and should be presented as it is an important finding. The authors should indicate the (expected/predicted) size of both peptides; it was not mentioned in the manuscript.

5) The different genetic alleles generated for linc-mipep and linc-wrb should be confirmed by DNA sequencing chromatographs; the expression of the linc-mipep and linc-wrb transcripts in the mutants should be confirmed by qRT-PCR as sometimes even small deletions can lead to destabilization or overexpression of the remaining transcripts. This is particularly important for the mutants that show behavioral deviations from wt animals.

6) In an elegant rescue experiment, the authors demonstrate that CDS of linc-miprep can rescue zebrafish locomotion hyperactivity phenotype. A control experiment with a construct expressing a frameshifted peptide should be included. From the presentation in Figure 2a, the peptide was tagged with FLAG-HA. Can the expression of the peptide be detected by Western blot/immunostaining? Have the authors tried to rescue the phenotype with human HMGN1?

7) One of the main conclusions from this study is that both micropeptides act together/somewhat redundantly, which would explain why knocking out both peptides has a stronger phenotype than knocking out either peptide individually. While this is a possibility (that they act redundantly, targeting the same regions in the genome), other scenarios are possible, e.g. that they have distinct or only partially overlapping chromatin targets and thus regulate different genes/pathways, which in the end converge on the same behavioral phenotype.

To resolve this, the rescue with linc-mipep should be attempted for the double mutant and also the single linc-wrb mutant (since it is a ubiquitous overexpression line, it may rescue both). Similarly, a rescue by linc-wrb (which is not shown, also not for the single mutant) would be important to support the conclusion that the phenotype is due to the loss of this peptide, and that it acts redundantly with linc-mipep. Moreover, it will also be important to quantify and provide statistics for the overexpression effect of the rescue construct in the WT background

Please also address the other points raised by the reviewers to improve the clarity and readability of the manuscript.

Reviewer #1 (Recommendations for the authors):

In my opinion, the main weakness of the paper is the very limited ability of the molecular phenotypic characterization of the mutants to explain the behavioral and neuropharmacological phenotype. This weakness is partially evident also by the lack of this point in the discussion that focuses on the evolutionary implications and the chromatin remodeling defects observed in the mutants. This is in my opinion an important point that should be better explained and investigated.

I would have also liked to have some validation of the protein localization in the cell types identified as most sensitive to the loss of linc-mipep and linc-wrb. Custom antibodies for these peptides were generated and staining is presented in extended fig2m showing only the larval forebrain. This analysis should be extended to OPC and cerebellar granule cells.

In the discussion of the putative evolutionary origin of linc-mipep and linc-wrb the authors mention the lancelet defining it simply as "invertebrate". This polyphyletic group is insufficient here and the authors should explain better its relevance in this context as basal chordate.

Reviewer #2 (Recommendations for the authors):

1. In the initial screen, it is not clear how the candidates for testing were selected and what kind of mutations were introduced in the F0, and what was the efficiency of the editing. As the paper is presented at least in part as an innovative screening effort, it is important to provide these details and outline them in the Results section.

2. The evolutionary analysis can be expanded significantly which will increase the scope of the results. What happens in other fish species (teleosts but also coelacanth/gar)? Do they also have both proteins? What happens in frogs/birds/reptiles? A multiple-alignment showing the proteins from different representative species of HMGN1 and the new proteins will be particularly informative.

3. Locomotor activity graphs: the number of tested fish should be added to all graphs. In some cases, the authors added a dot plot graph with P values, and this should be done for all the locomotor activity experiments.

4. The rescue experiments were performed using zebrafish linc-mipep CDS. It would be interesting to test whether a homolog for a different species (i.e., HMGN1) will also rescue the behavioral phenotypes.

5. ATAC-seq analysis: the analysis focuses on the comparison of peaks detected or not detected in the different datasets. A more common and more robust approach is to identify a single set of peaks using all the data together, and then test (e.g., using DESeq2) which peaks have differential accessibility between the different genotypes/samples.

6. A ChIP-seq experiment of the new proteins appears to be very interesting, but it is basically not described at all. How many peaks were found? Do they resemble each other? How reproducible was the data? A motif-based analysis appears to be very superficial given how instrumental these data (if solid) can be.

7. There's a mistake in c-fos In situ hybridization experiment location, which is in extended data Figure 4E, and not in Figure 3f (where it is written now).

8. In figure 2d – is the phenotype of linc-mipep-/- vs. linc-mipep+/+ fish (1st vs. 3rd) here significant? If yes – show the p-value. If not – how is this explained?

9. The statement that genes with ribosome-protected fragments are likely encoding functional proteins is not always correct and this part should be explained in more detail.

10. In the description of the single-cell datasets, please indicate fold-changes in differences of representation (e.g., for reduction of olig2+ oligodendrocyte progenitor cells across the brain)

Reviewer #3 (Recommendations for the authors):

1. The authors should show ribosome profiling data together with the gene structure of examined transcript (ideally, supported by RNA-seq) to visualize the position of ribosome-protected regions within the transcripts (Extended data Figure 1a and Figure 1d). The sequence analyses reveal the similarity between linc-mipep and linc-wrb and should be presented as it is an important finding. The authors should indicate the (expected/predicted) size of both peptides; it was not mentioned in the manuscript.

2. The authors should elaborate on the expression of the examined transcripts/peptides during embryogenesis (i.e., are they expressed at 5dpf only or earlier/later) and in adult tissues.

3. The different genetic alleles generated for linc-mipep and linc-wrb should be confirmed by DNA sequencing chromatographs; the expression of the linc-mipep and linc-wrb transcripts in the mutants should be confirmed by qRT-PCR as sometimes even small deletions can lead to destabilization or overexpression of the remaining transcripts. This is particularly important for the mutants that show behavioral deviations from wt animals.

4. In an elegant rescue experiment, the authors demonstrate that CDS of linc-miprep can rescue zebrafish locomotion hyperactivity phenotype. A control experiment with a construct expressing a frameshifted peptide should be included. From the presentation in Figure 2a, the peptide was tagged with FLAG-HA. Can the expression of the peptide be detected by Western blot/immunostaining? Have the authors tried to rescue the phenotype with human HMGN1?

5. A question related to the comment above: is it possible to detect native, untagged peptides by mass spectrometry? Have the authors tried to do it?

6. The manuscript would gain on clarity if a more detailed description of the behavioral assays used as a functional read-out was included in the main text. In general, the manuscript is partially hard to follow due to the insufficient data presentation, peptide size, peptide sequences, etc.

7. The authors should elaborate on why they used a single linc-mipep mutant for the drug experiments but a double mutant for omni-ATAC experiments.

8. The authors should clearly state in the discussion that the molecular mechanisms of action of both studied peptides remain completely unknown. For example, how do they affect chromatin accessibility? What are their interaction partners if any? etc

Reviewer #4 (Recommendations for the authors):

The manuscript can be significantly improved by addressing the following concerns:

Concerns and suggestions:

One of the main conclusions from this study is that both micropeptides act together/somewhat redundantly, which would explain why knocking out both peptides has a stronger phenotype than knocking out either peptide individually. While this is a possibility (that they act redundantly, targeting the same regions in the genome), other scenarios are possible, e.g. that they have distinct or only partially overlapping chromatin targets and thus regulate different genes/pathways, which in the end converge on the same behavioral phenotype.

To reconcile this, the rescue with linc-mipep should be attempted for the double mutant and also the single linc-wrb mutant (since it is a ubiquitous overexpression line, it may rescue both). Similarly, a rescue by linc-wrb (which is not shown, also not for the single mutant) would be important to support the conclusion that the phenotype is due to loss of this peptide, and that it acts redundantly with linc-mipep. Moreover, it will also be important to quantify and provide statistics for the overexpression effect of the rescue construct in the WT background – is there a significant activity decrease by linc-mipep OE? Overall, the authors mention the dosage-sensitivity of HMGN1 proteins, but with the current analyses fail to provide convincing evidence of a clear dosage effect of the two peptides since they could potentially target different, only in part redundant, genes or have different effects in different cell types. To this end, the use of either the single linc-mipep vs double linc-mipep/linc-wrb mutant is inconsistent in the second half of the manuscript: global ATAC-Seq data is only provided from the double mutant while single-cell-analyses are only provided from the single linc-mipep mutant. Moreover, the ChIP-seq analyses provided are only summarized for both proteins combined in the main Figure, but used individual antibodies, leaving it unclear how the individual profiles look (the authors should follow the standard convention on how to show the quality of ChIP-seq data, e.g. provide ChIP-seq tracks at least for some example genes since the quality of the data remains unclear, and differences between the two Abs cannot be assessed; the Suppl Table 8 also only provides a combined list of 37 genes for which ChIP seq peaks were identified though it would be important to show it individually for each AB; also the number of genes bound appears really really small? Are these ALL genes with a ChIP-seq peak?).

The second major concern relates to the unclear link between the different phenotypes observed: how can the behavioral phenotypes be reconciled with the molecular phenotypes (chromatin accessibility in specific neurons or precursors), and how can the chromatin accessibility differences in WT vs mutant be reconciled with the measured transcriptional/gene expression differences? Is there any evidence for NMDA being downstream of linc-mipep/wrb regulation? I applaud the authors on generating all these interesting data sets and analyses, but without connecting them together (here the focus for example on just the single linc-mipep mutant would be helpful, but the global brain ATAC-Seq data is only shown for the double mutant; and vice-versa, the single-cell ATAC-Seq data with the chromatin accessibility changes detected in specific cell types is not linked back to the ChIP-seq profiles of the peptides). Do glial progenitors and OPCs of the mutant(s) have altered expression of the underlying loci with altered accessibility? In Figure 4c, e, f, h, and Extended 6c-e, how does the chromatin accessibility translate to rna level in Purkinje cells and radial glia cells? How many sites lose accessibility in OPCs? Is "broad loss" a fair assessment of the observation?

Without addressing the two major concern points, the statement that linc-mipep and linc-wrb 'broadly regulate the chromatin state of neural cell types, most impacting OPCs and cerebellar granule cell gene expression networks and cell states in a basal vertebrate' appears overstated and would need to phrased differently/softened.

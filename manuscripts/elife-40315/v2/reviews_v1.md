# Peer review - Round 1

Editors:
- Shahragim Tajbakhsh, Institut Pasteur France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40315.037](https://doi.org/10.7554/eLife.40315.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Sonic hedgehog signaling patterns the oral-aboral axis of the mandibular arch" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Shahragim Tajbakhsh as guest Reviewing Editor, and the evaluation has been overseen by Didier Stainier as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ramkumar Sambasivan (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study reports on the role of Hedgehog signalling in the patterning of the oral-aboral axis in the mouse developing jaw. The authors use scRNAseq and identify genes in distinct cell populations in the mandibular arch and map these subsets in the embryo using in situ hybridisation. Using several genetically modified mouse models, the authors propose that hedgehog signaling antagonizes Bmp signalling in the presumptive osteogenic domain, which is critical for cell survival in the distal mandibular arch. The work complements the current understanding of FGF8 / BMP4 antagonism in patterning the proximo-distal axis of jaw, the experiments are well-designed and the extensive phenotypic data represents a significant advance in the field.

Essential revisions:

1) The presentation of scRNAseq data is not well integrated and the analysis appears preliminary. Additional analysis would enable the authors to support their conclusions, and would make the article more accessible to a wider readership.

2) Are the subdivisions of the mandibular arch sharply defined or extremes of expression gradients? In the in situ hybridizations, many genes show graded expression, and the authors also mention the presence of nested spatial expression patterns (subsection “Single-cell RNA-seq analysis of the E10.5 mouse mandibular arch”, third paragraph). It is not clear why the authors choose to represent the complex 3D organization of the mandibular arch with a simple 2D tSNE projection, and why they look for distinct clusters instead of analyzing expression gradients. Indeed, the genes shown in Figure 2 do match the four clusters shown in Figure 1B only in some cases. Some of the genes demarcate parts of these clusters (e.g. pou3f3, foxf2) or span subparts of multiple clusters (e.g. lhx8, covering part of cluster 0 and 3). Moreover, it is not evident why 3 stands as its own cluster: the heatmap in Figure 1C does not show genes specific of this cluster.

The dataset seems rich enough to characterise and display more clearly the three major spatial axes of the developing mandibular arch: oral-aboral, proximo-distal and rostro-caudal. The authors could explore computational methods better suited for this, for example PCA, ICA or diffusion maps. In this way the three axes might show up as separate components in PCA, ICA and/or diffusion map space. This would enable the authors to study the cells along "pseudospace" trajectories, and to plot more clearly the expression of genes with graded and nested expression along these axes. They should also identify in an unbiased way the gene families overrepresented along these axes (e.g. by GO-enrichment), and leverage their data further to support the main conclusions (e.g., are there genes involved in ossification vs. muscle differentiation activated at the two opposite extremes?).

3) The increased apoptosis found in the distal region of mandibular arch at E10.5 in Hand2Cre;Smoc/c may be responsible for the lack of distal mandibular skeletal structure at newborn stage. It would be helpful to discuss or speculate on the potential cellular mechanism that resulted in the ectopic dentary bone formation in Smo mutant mice.

4) The authors attribute the NC3 population from the single cell RNA-seq to a population of neural crest cells which underwent an incomplete lysis of their nucleus, thus clustering out of the NC1 and NC2 clusters. However it is considered that nuclear transcripts represent a small fraction of cellular transcripts, and that nuclear mRNA is a good substitute for cellular mRNA in scRNAseq cell type identification (Lake et al., Sci Rep, 2017). Could the lack of nuclear transcripts alone account for the clustering of this population ? Among the nuclear lncRNA, Sox11 seems to be highly differentially expressed in NC3 compared with NC1/2. Sox11 is known to be expressed in the palate 3 days later, as well as in nerves. Could this population come from a proximal contamination from a domain shared with the maxillary prominence or neurogenic cells in the mandible ?

5) The authors present a model of an oral endodermal Shh expression, leading to an activation of Foxf1/2 in the adjacent mesenchyme and inhibition of BMP4 signalling, controlling the expansion of the Msx1 domain.

- Importantly, do the authors observe an expansion of p-SMAD1/5/9 in the Wnt1-Cre; Foxf1/2 cKO?

- If so, can the authors speculate on the possible targets of Foxf1/2, leading to the inhibition of Smads?

6) The authors describe tongue agenesis in Wnt1-Cre;Smo cKO, Hand2-Cre; Smo cKO and Wnt1-Cre; Foxf1/2 cKO, but show only rostral frontal sections.

- Is tongue agenesis observed all along the oral rostro-caudal axis in the different cKO specimens?

- Do the authors have available data at E10.5 showing altered hypoglossal cord formation in cKO specimens?

- From the data collected in this study, the authors should discuss more extensively the role of the neural crest-derived population during tongue morphogenesis as previously proposed and reviewed in Parada and Chai (2015).

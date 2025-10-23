# Peer review - Round 1

Editors:
- Asifa Akhtar, Max Planck Institute for Immunobiology and Epigenetics Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35684.065](https://doi.org/10.7554/eLife.35684.065)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Evolution of gene dosage on the Z-chromosome of schistosome parasites: a snapshot of Ohno's hypothesis" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Vicoso and colleagues analyse dosage compensation status of the Z chromosome in ZW females and ZZ males in three schistosome species and propose that the Z-linked genes are upregulated in both sexes in addition to reduced expression of Z-linked genes in females indicating that their results are consistent with Ohno's original hypothesis. Reviewers agreed that studying evolution of sex chromosome is an important topic and that authors provide interesting evidence for dosage compensation regulation in schistosome. However, a number of concerns were raised regarding the analysis of the genomewide data set for scoring dosage compensation status. These points need to be addressed in a thoroughly revised version before we make a final decision on the manuscript.

We would like you to especially address the following concerns.

Reviewers discussed that authors should pay close attention to, and describe in detail, how they calculate X:A ratios. They should take into consideration the expression of house-keeping genes and sex bias expression. This is an important point to address as it could significantly change the interpretations regarding the status of dosage compensation in schistosomes.

This primary concern is described in more detail in the reviewers' original comments, so their full reviews are appended below.

Reviewer #1:

Here, Picard et al. examine the gene content and dosage compensation status of the Z chromosome in ZW female and ZZ male African and Asian schistosomes. Dosage compensation is assayed by comparing Z expression between the sexes (F:M ratio) and by calculating Z versus autosomal expression within each sex (Z:AA ratio). Both ratios are expected to = 1.0 if dosage compensation is "complete". They find that the F:M ratio falls below 1.0, suggesting greater Z expression in males than females. Z:AA ratios in females fall between 0.5 and 1.0, while in males they exceed 1.0. The conclusion is that some degree of Z-upregulation, or "incomplete" dosage compensation, occurs in both sexes, consistent with the first evolutionary step as proposed by Ohno. Analysis of microarray and proteomic data reveals concordance between RNA and protein levels, suggesting that post-transcriptional mechanisms do not kick in to provide "full" Z dosage compensation.

This manuscript addresses an important biological question. However, I'm not sure the analyses currently support the proposed Z dosage compensation status in schistosomes.

Studying Z/X upregulation is complex, and several previous studies are flawed because they have not paid attention to several important factors. In the current submission the authors have considered most of these factors: they have set an appropriate lower cut-off for gene expression (RPKM >1), and have compared expression of extant with ancestral Z-genes. However, the issue of dosage-sensitive housekeeping genes is not considered. As proposed by Birchler and demonstrated by Pessia (cited in the first paragraph of the subsection “The relevance of the Ohno’s hypothesis in the high-throughput sequencing era”), upregulation preferentially affects this specific class of genes. Pessia et al. showed that when all expressed genes are included in X:AA calculations, X:AA ratios in XY males fall between 0.5 and 1.0, suggesting that X-upregulation is "incomplete". However, when only housekeeping genes are considered, X:AA ratios equal 1.0, showing that X-upregulation is actually "complete". A similar approach by Sangrithi et al. (2017) (not cited here) validated and refined this approach, identifying housekeeping genes by virtue of ubiquitous expression. Thus, the status of upregulation will vary depending on which genes are assayed. Also related to this point is whether the authors are studying the same expressed genes across different sexes and tissues. This is the most appropriate comparison.

To address the effect of post-transcriptional regulation on Z dosage compensation, the authors then compare microarray and proteomics data on schistosome heads and gonads. It's not clear to me why the tissues used for this analysis are distinct from those in the RNA-seq analysis; this makes the manuscript a bit awkward. However, setting this aside, the issue of gene choice once again becomes important. Many studies have shown that the mammalian X chromosome is enriched in genes with CNS functions and gonadal functions; the presence of these highly expressed genes artificially elevates X:AA ratios. Is there evidence for such gonadal and neural specialisation of schistosome Z chromosomes? Related to this point, the authors should address whether Z:AA ratios are influenced by imposition of upper expression cut-offs. Such cut-offs affect X:AA ratios in the CNS and gonads (see Sangrithi et al. and studies from Disteche).

Reviewer #2:

The authors use depth of coverage from whole genome sequencing to identify Z-linked genes in three schistosome species (one from Asia and two from Africa). Although the Z chromosome is homologous across all three species, there are differences in the evolutionary strata between species from different continents, suggesting that the lineages differ is some pseudoautosomal regions. When looking at gene expression, several patterns emerge: (i) the Z has lower expression than the autosomes in females, (ii) the Z has higher expression than the autosomes in males, (iii) the Z has strongly male-biased expression. The authors interpret these results as being in agreement with the early stage of Ohno's classic model for the evolution of dosage compensation in which the Z is upregulated in both sexes in order to compensate for its reduced dosage in females. Similar patterns are seen at the level of protein abundance, suggesting that post-transcriptional regulation does not play a major role in the evolution of dosage compensation in these species.

This paper is very well-written and the figures do a good job of illustrating the main results. The authors have made a convincing case and have gone an extra step beyond most previous studies of this type by including proteomic data. I think that this work makes an important contribution to the field. I don't see any major flaws.

Reviewer #3:

The genomics of sex chromosome function and evolution has been under intense study for the last 15 years. These studies, along with work that augments the genetics of dosage compensation, have enriched our understanding of selective pressures and evolution of sex chromosomes. Having additional models is always useful. The current work examines a lineage which allows a comparison of expression sex chromosome linked genes in various stages of being made hemizygous in a ZW system. As the authors note, X0/XY and ZW systems appear to follow different rules for sex chromosomes dosage compensation. The current work confirms these differences in a well written, but under-detailed manuscript.

1) The ortholog mapping and projection of scaffolds onto the Z chromosomes appears robust. This will provide a valuable map for future use of these species in sex chromosome studies as well as for other uses in the genomic parasitology field. It would be useful if these mappings were available. I understand that the TPA has rigorous steps for getting such information into a public repository, but maybe there are other options, such as adding a table in the supplement.

2) There are many confounding factors in using median expression in females and males to measure dosage compensation, none of which appear to be taken into consideration. The sexes of schistosoma are highly dimorphic and are enriched in gonad compared to most organisms that have been examined for sex chromosome dosage compensation. This creates analytical complexities. For example, extensive sex-biased expression, differences in the distribution of genes showing sex-biased expression, differences in cell-type composition between the sexes, or MSCI could all complicate the analysis. Looking at the sexually undifferentiated stages may take care of some of these concerns, but the authors do not explain any of the complexities and workarounds to the reader, whom might not be well acquainted with the field. I would very much like to see the sex-bias profiles, some attempt to examine the expression of more housekeeping genes, and a generally deeper look at the data.

3) That there is not a highly robust translational compensation response is a nice addition to the literature. However, it is important to demonstrate that the proteomics has the sensitivity to make any claims about the contribution of post-transcriptional control to dosage compensation (or lack thereof). The correlations with expression data are positive, but it seems imprudent to extend too far from the primary data showing that F/M ratio for proteins encoded by Z-linked genes is reduced.

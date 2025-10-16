# Peer review - Round 1

Editors:
- Andrew P Morris, University of Liverpool United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39595.032](https://doi.org/10.7554/eLife.39595.032)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that minor issues remain unresolved.]

Acceptance letter:

The Reviewing Editor's assessment is that a minor issue (the appropriateness of the term "fine-mapping") remains unresolved.

Decision letter after peer review:

Thank you for submitting your article "Fine-mapping cis-regulatory variants in diverse human populations" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

Summary:

The authors describe a novel approach for the identification of chromatin accessibility QTLs (caQTLs) on the basis of ATAC-seq data obtained from pooled sequencing in LCLs from thousands of individuals across 10 population groups. The results of these analyses are used to assess allelic effects on chromatin across populations, and demonstrate that chromatin accessibility is associated with transcription factor binding, long-range chromatin interactions and gene expression. The authors then propose the use of variants with shared allelic effects on chromatin across populations as an approach to prioritise causal variants for complex traits at loci identified through GWAS. Both reviewers highlighted the novelty and importance of the study in understanding how genetic variation impacts on complex traits via chromatin accessibility across population groups.

Major concerns:

The reviewers expressed concerns over the interpretation of the results of the fine-mapping analyses. To comprehensively fine-map a GWAS locus, the effect of all (or most) variants on a trait are assessed, but the approach can only consider variants with sufficient ATAC-seq read depth. It is also assumed that causal variants will have shared allelic effects on chromatin across populations. This does not allow for potential allele frequency differences between populations which might impact on power to detect allelic imbalance in each population. Whilst the approach can be used to prioritise potential causal variants, it is not "fine-mapping" in the traditional sense, and the authors should consider these limitations in the interpretation of their results.

The reviewers also felt that some further discussion of the potential limitations of the approach, and the impact on the interpretation of their findings, would be warranted, including the ability to only detect caQTLs that affect their own read counts, the reliability of estimation of pre-ATAC/ChIP allele frequencies and potential mapping bias of Hi-C reads.

Separate reviews (please respond to each point):

Reviewer #1:

The manuscript by Tehranchi et al. describes the generation of ATAC-seq data in LCLs from a thousand individuals across 10 populations using a pooled approach and then mapping allelic effects in pooled data from each population. The authors then use these results to describe relationships in allelic effects on chromatin across populations, identify variants with shared effects across populations, compare allelic effects to other molecular trait data, and use these variants to prioritize fine-mapped GWAS variants. In total this study and findings are both an important resource and provide a conceptual advance in our understanding of how population genetic variation affects chromatin accessibility and role in complex traits and disease.

The authors describe their approach of prioritizing variants with significant allelic effects across populations as fine-mapping causal variants, which I think is not entirely accurate. The premise of fine-mapping is that most/all variants on in a region are evaluated for their effects on a trait; given that the authors are only able to map the subset of variants with sufficient ATAC-seq read depth there may be causal variants that, for example, map in a different site and affect chromatin accessibility across an entire region, map in the same site but on the edge and have low read depth, or map outside of a site entirely. While presumably the majority of variants with shared allelic effects are likely directly responsible for their imbalance, there are likely also variants where this isn't the case.

Furthermore, assuming that only variants with shared effects across populations are causal for a trait also does not consider that (a) some trait/disease signals have population-specific effects and (b) allele frequency differences across populations might prohibit mapping allelic imbalance in all populations and lead to the assumption that the effects are population-specific. In terms of mapping causal variants at disease signals then, this approach would work well if the signal is shared across populations with consistent frequency, but if it is population-specific or has allelic heterogeneity then this approach might not be as applicable.

It would help the study for the authors to be more explicit about these limitations, and re-frame the description of the results to clarify that they aren't fine-mapping causal variants in a classic sense but rather identifying a specific set of variants with shared effects across populations that are extremely useful in interpreting fine-mapped disease signals which are shared across populations.

For the GWAS examples it would be extremely useful to readers I think to see plots of the regions including the data described for each example, which I couldn't find (maybe I missed them). For the second example, it would be useful to further see the LD patterns across populations to demonstrate that rs479844 is associated with Europeans but not in other populations presumably due to differences in LD with rs10791824.

Minor Comments:

1) When comparing the percentage of variants with allelic effects shared across populations, presumably they considered a variant shared across two populations if it had significant effects in both? If so it would be informative to estimate how many variants were also likely shared but didn't reach significance for example by estimating concordance in effects.

2) It would be interesting to determine whether variants with shared allelic effects tended to have higher causal probabilities from genetic fine-mapping than other classes of variants to provide further support for their causality.

3) The statement "An alternative to increasing sample size within a single population is trans-ethnic fine-mapping, in which a GWAS is performed across multiple populations" is confusing and could be clarified.

4) I think purists might quibble with the use of QTL to describe allelic imbalance mapping, and could also potentially cause confusion to readers not overly familiar with this field.

Reviewer #2:

In Tehranchi et al., 2018, the authors present a novel use of pooled sequencing applied to the identification of QTLs altering chromatin accesibility (caQTLs) by ATAC-seq. They demonstrate convincingly that their pooled approach can identify QTLs more efficiently than standard approaches, that CA is causally associated with transcription factor binding, long-distance chromatin interactions, and gene expression, and that chromatin accessibility is a likely molecular trait underlying GWAS variants. However, there are several concerns:

1) caQTLs can only be detected if they affect their own read counts. Is this a major limitation of the method given the findings of previous studies? This should be addressed in the text.

2) Do caQTLs show different allele frequencies across genomic annotations (e.g. active TSS vs enhancers vs repressed regions, etc)? Does this contradict or support hypotheses of negative selection on caQTLs?

3) Have the authors validated, in this or previous work, that they are able to reliably estimate the pre-ATAC/ChIP allele frequencies using their regression approach?

4) For the "Long-range interaction analysis," is potential mapping-bias of Hi-C reads taken into account by the authors?

Minor Comments:

1) Introduction section: while most GWAS variants are not in LD with coding variants or may be in LD with variants in regulatory regions, most genome-wide significant variants from GWAS aren't actually in regulatory regions.

2) In "Characterizing fine-mapped eQTLs," the source data of the chromatin states (Ernst and Kellis, 2012) is present in the figure legend but is absent in the text and methods; adding a citation to one of these would be helpful

3) As a minor stylistic concern, chromHMM tracks have a standard color palette (e.g. red corresponds to promoter/TSS, orange/yellow to enhancer, green to transcribed regions, etc.) and this reviewer would prefer its use for Figure 3.

4) It is not clear how read density was controlled for in subsection “Characterizing fine-mapped caQTLs”.

5) The final paragraph of subsection “Characterizing fine-mapped caQTLs” references "trinucleotide" dependencies of CA variants but these are not mentioned in the text or Materials and methods section.

6) The figure legend for Figure 4 mentions using "allele-specific 3D chromosomal interaction" data; does this mean only heterozygous sites were considered? This should be described in more detail in the text and/or methods.

7) Having the principal equations of the regression approach in the Materials and methods section would be helpful to readers.

8) The subsection "Effects of caQTLs on DNA shape" in the Supplementary Text includes analysis related to chromatin shape, which is not present in the main text.

Additional data files and statistical comments:

The provided data files, in addition to read data placed on public databases, should be sufficient.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting a revised version of your article "Fine-mapping cis-regulatory variants in diverse human populations" for consideration by eLife. Your article has been reviewed by the original referees and the evaluation has been overseen by Andrew Morris as the Reviewing Editor and Patricia Wittkopp as the Senior Editor.

The manuscript has been improved, but the reviewers remain concerned about the use of the term "fine-mapping" in the manuscript. Traditional fine-mapping, in the GWAS field for example, interrogates all (or the majority) of variants in a region, and assesses their relative evidence for causality based on association with a trait and relevant annotation. However, in your investigation, only a limited subset of variants in a region are considered, and the reviewers do not feel that "fine-mapping" is an appropriate description of the approach taken. The reviewers have suggested the following changes be made.

1) Remove the term "fine-mapping" from the title of the manuscript – this could be replaced by "determining" or "localising".

2) Please provide further discussion of the limitation of the approach to localising causal variants. In particular, please include discussion to address the following comment from the initial review of your manuscript:

"The authors describe their approach of prioritizing variants with significant allelic effects across populations as fine-mapping causal variants, which I think is not entirely accurate. The premise of fine-mapping is that most/all variants on in a region are evaluated for their effects on a trait; given that the authors are only able to map the subset of variants with sufficient ATAC-seq read depth there may be causal variants that, for example, map in a different site and affect chromatin accessibility across an entire region, map in the same site but on the edge and have low read depth, or map outside of a site entirely. While presumably the majority of variants with shared allelic effects are likely directly responsible for their imbalance, there are likely also variants where this isn't the case."

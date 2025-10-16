# Peer review - Round 1

Reviewers:
- Cynthia Wolberger, Johns Hopkins University , United States

## Review text

DOI: [10.7554/eLife.18919.035](https://doi.org/10.7554/eLife.18919.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Direct screening for chromatin status on DNA barcodes in yeast delineates the regulome of H3K79 methylation by Dot1" for consideration by eLife. Your article has been favorably evaluated by Jessica Tyler (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors describe a new strategy for carrying out an unbiased screen for genes that regulate chromatin modifications. The Epi-ID method allows pools of individual mutants, each carrying a specific integrated barcode, to be probed by ChIP. Deep sequencing of the barcodes in the precipitated samples allows quantitative assessment of the effects of a given mutation on the chromatin parameter, in this case H3K79me1 and H3K79me3. In addition to the genes previously known to regulate H3K79 methylation, either directly or indirectly, the authors identify novel genes including the Gcn5 acetyltransferase, N-terminal acetyltransferases, genes that regulate replication fork recovery, and enzymes involved in S-adenosyl methionine (SAM) and SAH biosynthesis. The manuscript also makes a strong case that there is no H3K79 demethylase, with the caveat that essential strains were not tested. Overall, the reviewers found the Epi-ID method to have strong potential for identifying novel genes impacting methylation that could be readily extended to other chromatin modifications for which the appropriate antibodies are available. However, a more thorough exploration of some of the hits would make a stronger case of the utility of the approach.

Essential revisions:

1) The interpretation of Figure 4 is speculative, and the results on the leukemia cell lines do not clarify the conclusions. The adenosine kinase inhibitors could be influencing cell viability through a mechanism quite unrelated to Dot1L or H3K79me. What do the H3K79me levels look like in the treated cells? In their current form, these tissue culture experiments weaken the paper and should be omitted unless further pursued.

2) The finding that deletion of ADO1 impacts histone methylation is presented as a discovery, whereas it seems to fall in the category of a confirmation of the validity of the screen rather than new information. Since ADO1 was already reported to regulate SAM levels (Kanai 2013), it is not surprising that altering levels of the methyl donor would impact histone methylation. It was initially puzzling that deletion of ADO1 had opposing effects on Dot1 versus Set1 and Set2. However, the explanation that the authors suggest, namely that these enzymes respond differently to restriction of SAM and SAH is, in fact, consistent with the cited paper (Sadhu et al., 2013), which reported differential effects on H3K79 versus H3 K4 methylation in response to nutritional limitation. The lengthy discussion of this gene does not seem warranted in light of what was previously known. Instead, this could be cast differently, namely as support for the Epi-ID method.

3) One of the more intriguing findings is the observed impact of acetyltransferase mutations on H3K79 methylation via an effect on H2B ubiquitination, which is required for methylation by Dot1. A deletion or catalytic mutant of the Gcn5 acetyltransferase increased methylation via an impact on H2B ubiquitination, whereas mutations in the N-terminal acetyltransferase proteins, Nat1 and Ard1, caused a decrease in H2B ubiquitination. However, these results are not pursued adequately, leaving open the question of whether these genes directly regulate H2B ubiquitination or have indirect effects. At minimum, the authors should show whether any of the acetyltransferase mutants affect levels of proteins known to be involved in H2B ubiquitination, Bre1, Rad6 and Lge1, or deubiquitination, Ubp8 and Ubp10. Potential effects on protein levels should be explored for any other mutants discussed, as was done for Slx5/8.

4) Do the HAT mutations also affect H3K4 methylation?

5) The western blot in Figure 4A for Ado1 effects is not particularly convincing. H3K4me3 and H3K36me3 levels also seem to be decreased.

6) What do H2Bub levels look like in the ado1 mutant?

7) Conclusions drawn from Figure 1 (even in regards to controls) should be qualified in regards to effects of deletions on growth rates which affect K79me3 (as the authors address in Figure 2).

8) How do the authors ensure that the time points in Figure 2A represent log phase growth? While the growth rates for two independent experiments were determined and then averaged, can the same conclusions about K79me3 and growth rate be derived independently from each experiment? Assuming this is the case, this should be stated (although it may be buried in Figure 2B legend). It would also be helpful to make clear in the main text that the strains were separately grown, as opposed to grown as a pool.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Direct screening for chromatin status on DNA barcodes in yeast delineates the regulome of H3K79 methylation by Dot1" for further consideration at eLife. Your revised article has been favorably evaluated by Jessica Tyler (Senior editor), a Reviewing editor, and 1 reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The revised manuscript appropriately addresses almost all previous concerns. The addition of controls in which protein levels were measured in the various mutant strains improved the manuscript and helped clarify interpretations. The reduced emphasis on Ado1, along with a discussion of these results in the context of published studies, also improved the paper. Finally, the removal of the cell line experiments, which were incomplete, solidified the manuscript.

One remaining issue in the revised manuscript is that Gcn5, and Gcn5 catalytic activity, are described as regulators of Ubp8 activity. However, Ubp8 protein levels are reduced in the gcn5 deletion strain, indicating that the defect in H2B deubiquitylation is a consequence of the loss of the SAGA subunit, Ubp8, rather than regulation of its catalytic activity. The authors show that a mutant of Gcn5, F221A, has a phenotype comparable to the deletion; however, F221 forms hydrophobic interactions with multiple buried residues, which raises the possibility that the strong effect of the F221A mutation results from destabilization of Gcn5, which would be predicted to lead to loss of Ubp8. To demonstrate that Gcn5 indeed regulates Ubp8 activity, as opposed to stabilizing its incorporation into SAGA, the authors should provide evidence that the levels of both Gcn5 and Ubp8 are unchanged when Gcn5 bears the F221A substitution. Without this result, the authors should soften their conclusions here. Should the authors wish to generate a bona fide Gcn5 catalytic mutant, substitution of the conserved catalytic E122 would be a better choice.

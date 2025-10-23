# Peer review - Round 1

Editors:
- Xavier Darzacq, University of California, Berkeley United States

Reviewers:
- Mathias Francois, The University of Queensland Australia
- Ciara Metcalfe, Genentech United States

## Review text

DOI: [10.7554/eLife.48876.sa1](https://doi.org/10.7554/eLife.48876.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Both reviewers and myself judge the work to be important and timely for this field. Whether a DBD can be drugged is a burning question, and here you provide a very clear example of how drugs can be developed in this space. The work clearly warrants publication in eLife and as a result of the review process the added discussion and data on specificity is essential as drugging protein DNA interfaces is a major challenge in general for the community.

Decision letter after peer review:

Thank you for submitting your article "Modulating FOXO3 transcriptional activity by small, DBD-binding molecules" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Eisen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mathias Francois (Reviewer #1); Ciara Metcalfe (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Both reviewers and myself judge the work to be important and timely for this field. Whether a DBD can be drugged is a burning question, and here you provide a very clear example of how drugs can be developed in this space. The work clearly warrants publication in eLife, but it is also essential that you establish the specificity of the compound. Both reviewers and myself noted that the provided data do not unambiguously establish specificity. indeed, as noted by reviewer 2, "the NMR data (Figure 2—figure supplement 2) suggest an overlap in residues impacted by S9OX in FOXO1 and FOXO3, with distinct regions of the protein impacted in FOXO4" – suggesting that the DBD of all these family members may bind to S9OX, to some degree. These data do not support the statement that the NMR data "suggest selectivity of S9 and S9OX within the FOXO-family of transcription factors." It is therefore essential to explore the specificity in more detail. Exploring new chemical spaces to gain in specificity would likely be beyond the scope of this paper, though a great subject to discuss in this paper. However, a solid characterisation of the current 76 compound would establish a benchmark for future studies in this field.

Essential revisions:

I consider all the points raised by reviewers essential, with the exception of developing new variants of S9 that I consider super interesting but out of the scope of this paper. following is a summary of the concerns to address.

1) Selectivity issue: following is a list of the points raised by the two reviewers. I would like this point to be clarified in a revised work. Achieving selectivity is not important for publication but the selectivity must be known and documented.

2) Use of 4 OHT and doses of S9: several critical issues need to be documented here with identical doses of the compound and synergistic effects must be explored.

3) Cellular source of FOXO3: overexpression of FOXO3 is a problem and one would want to see some other approach. Reviewer 2 in her point 3 suggest a great possibility that would offer an orthogonal system to perform this study.

Reviewer #1:

This work by Psenakova and colleagues is really exciting and will directly contribute to the emerging and expanding field of drugging transcription. The molecular strategy chosen by the author is to target the DNA binding domain of FOXO3 transcription factor, using a pipeline that relies on: 1) an in silico-based approach (docking FOX/DNA to identify hot spot- generate 76 hits for in vitro testing via virtual screening using 2 chemical databases). 2) modelling of protein DNA interface to identify putative residues involved in small compound interaction. 3) combination of in vitro homogenous assay (FP) and in vitro cell-based assay with transcriptomics and tumour sphere assay as a readout for FOXO3 activity to validate inhibitor activity in living cells.

Overall the quality of the data is high and the manuscript clearly written. There is no doubt that the identified compound (S9) has some biological effects, at least in part mediated by FOXO3 inhibition, however the on-target engagement on FOXO3 lack some experimental evidences. With the current data set as it stands one cannot definitely come to the conclusion that S9 mostly acts via FOXO3 inhibition and interference of DNA binding.

Key experimental evidences missing to support the claims:

1) The rationale is to target the DNA binding activity of FOXO3. Aside from the FP data there is no evidence that S9 acts with this mode of action in cells to interfere with gene transcription. To address this the authors would need to perform ChiPSeq for FOXO3 in presence or absence of the compound and show that genome wide binding locations are interfered with by S9. At least the author should be able to provide some evidence on a subset of known FOXO3 direct target genes that FOXO3 binding is altered at known binding sites – This can be done by ChIP-qPCR analysis.

2) It would be helpful to perform thermal stability assay in presence of FOXO3 or a FOXO3 mutant (Arg 211, His 212, Ser215 amino acid thought to be involved with S9 interaction) with and without S9. This to further support the modelling data for compound/protein interaction.

3) It is difficult to understand how S9 achieve such a high level of selectivity to FOXO3 at least in FP while targeting such a highly conserved region as the DNA binding domain of FOX protein. Of note the FP experiments run for FOXO3 and other FOXO protein use different concentrations of S9 molecules (250nM for FOXOs vs. 500nM for FOXO3). To be able to compare selectivity it is necessary to perform the same dose response of S9 across all the FOXO protein.

4) The work rely solely on the use of 1 compound, it is therefore difficult to assess the level of selectivity of this molecular space. How are other compounds closely related (with a similar pharmacophore) but with no predicted DNA binding activity behave (at least in FP). Can S9 affect FOXM1 DNA binding activity? These data would help to assess specificity and efficacy of S9 as a protein/DNA disruptor.

5) It Is possible that S9 and 4-OHT have a synergic or additive effect on FOXO3 gene regulatory network. The analysis of the RNAseq data set should revised and include an analysis of DEseq for -4OHT with -4OHT+S9. This would be useful to assess the effect of the inhibitor on endogenous FOXO3 activity.

6) The authors highlight that the SH-EP neuroblastoma cell line used in this work has some level of FOXO3 activity. In the tumour sphere assay there is no effect of S9 in condition without 4OHT. It seems that S9 only works in over-expression condition- if there is endogenous FOXO3 expression in SHEP cells why is there no effect of S9?

Reviewer #2:

Hagenbuchner et al. describe inhibition of the transcription factor FOXO3 by small molecule targeting of its DNA-binding domain. Therapeutic targeting of transcription factors is highly desirable, but remains a significant challenge. Practical advancements in this area are thus potentially impactful, and the topic of this study is thus relevant for publication in eLife. However, there are some key elements of the work where improvements are warranted:

1) – Given that a major concern of small molecule perturbation of DNA-binding is the specificity of this approach, it is important to clearly establish selectivity of S9/S9OX, across the FOXO family and beyond. While the fluorescence polarization assay measuring binding of FOXO-DBD to labelled oligo provides some evidence of potential selectivity (though the result for FOXO4 is borderline), the NMR data (Figure 2—figure supplement 2) suggests an overlap in residues impacted by S9OX in FOXO1 and FOXO3, with distinct regions of the protein impacted in FOXO4 – suggesting that the DBD of all these family members may bind to S9OX, to some degree. These data do not support the statement that the NMR data "suggests selectivity of S9 and S9OX within the FOXO-family of transcription factors."

2) – Given the above, it would be useful to see the primary biochemical validation data (i.e. fluorescence polarization assay) for the 76 virtual hits that were experimentally tested, to understand the dynamic range, sensitivity and specificity of the in vitro screening assay e.g. what did an unconfirmed hit look like, vs. S9? Ideally, a secondary screen would have been performed against an unrelated DBD – was this done?

3) – The mRNA expression data showing attenuation of 4OHT-induced transcription by S9(OX), and the CHIP data showing a prevention of 4OHT-induced DNA binding of FOXO3 are highly encouraging. However, a limitation is that much of the functional data is in the context of exogenously expressed, ER-tagged, mutant FOXO3. Activity states of endogenous FOXO3 can be "toggled" using PI3K/AKT inhibitors (e.g. Santo et al., Cancer Research, 2013). An assessment of how S9(OX) impacts endogenous FOXO3-mediated transcription and DNA-binding under these conditions would provide more compelling support for S9 mechanism.

4) – For the viability experiments on the NB15 cells, the S9 dose is dropped to 5µM, while the FOXO3-specific pathway assessments were conducted at 50µM – it would be worthwhile to show a dose response of both the transcriptional and physiological effects to demonstrate that the physiological consequences of S9-treatment are due to an on-target effect on transcription i.e. the transcriptional and physiological phenotypes should occur/arise at similar drug concentrations.

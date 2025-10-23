# Peer review - Round 1

Editors:
- Stephen CJ Parker, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76500.sa0](https://doi.org/10.7554/eLife.76500.sa0)

Here, the authors used multiple F1 crosses and the resulting embryonic fibroblasts to perform molecular profiling with ATAC-seq and a combination of ChIP-seq, Hi-ChIP, and CUT&RUN on multiple modified histones and transcription factors proteins. These important results are a convincing resource for quantifying allelic bias in protein-DNA binding and chromatin accessibility.


---

# Peer review - Round 1

Editors:
- Stephen CJ Parker, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76500.sa1](https://doi.org/10.7554/eLife.76500.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Characterization of sequence determinants of enhancer function using natural genetic variation" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We all thought the data are quite strong. We have included the full review from both reviewers below and have summarized the essential three items for revision here:

1) The authors claim "Our findings provide new insight into how enhancer function is encoded within DNA sequences…" but it was hard to see the new insights that were provided. We suggest hardening up the abstract to clarify precisely what the authors have discovered, and considering reorganizing the text to consolidate and focus the introductory material on what is relevant to these key claims.

2) The overall data set is strong, but they are not utilized to the fullest extent for analyses. For example, no population genetics data were considered. Can the authors examine allele frequency and effect size relationships? Basic population genetics tells us that rare SNPs are more likely to be deleterious. So, in situations where C57BL/6J has the rare allele -- is accessibility and TF binding more likely to be reduced? There are several analyses that could address this general question.

3) Data sharing through GEO must be complete.

Reviewer #1 (Recommendations for the authors):

The authors claim "Our findings provide new insight into how enhancer function is encoded within DNA sequences…" but I had trouble seeing the new insights that were provided here.

Several claims were made about enhancer priming, selection, and other chromatin kinetics. But to really understand this, I think one needs time series data, which is not part of the present study.

In the Allele-specific CUT&RUN peak calling section, what does it mean to recenter a CUT&RUN peak onto an ATAC-seq summit? Are you shifting the coordinates of the CUT&RUN peak so the middle occurs where the ATAC summit is located? Does this make sense to do? Given that a modified histone should not occur at the same place as an open chromatin summit, I'm not sure why this was done. Perhaps there are missing details that should be here.

It looks like there are issues with the GEO upload and these should be resolved before the manuscript is finalized.

The abstract claim of "impact of sequence variation on enhancer function" seems a little broad.

Sometimes, the figures should be labeled more clearly. For example, Figure 6A-B has two different line colors but these are not explained with a color key in the figure.

Figure 2H-J and every panel in Figure 5 have typos on the x-axis. -100 is incorrectly plotted as -10.

The acronym CRE is used extensively throughout the paper, beginning in the second sentence of the introduction, but is never defined.

Reviewer #2 (Recommendations for the authors):

1) The abstract is pretty general and did not help me figure out what the main claims of the paper were. I had difficulty triangulating the claim I found most interesting with its description in the narrative and the data in the figures. For example, the abstract claims "our data…reveal a hierarchical relationship between AP-1 and TEAD TF binding at enhancers" (lines 38-39), which is too vague. The relevant section begins on page 21, but includes two paragraphs of introduction before arriving at the new claim. I would suggest hardening up the abstract to clarify precisely what the authors have discovered, and considering reorganizing the text to consolidate and focus the introductory material on what is relevant to these key claims.

2) I found the use of the term "k-mer" confusing. It appears that the authors use this as shorthand for "TF recognition sequence" or "motif match", but sometimes as meaning TF consensus/motif (e.g. the AP1 consensus in line 666). The gk-SVM uses another definition, where k-mers are used as SVM features. I eventually gathered that the first use follows from the KMAC (Guo et al. 2018) tool. I would suggest clarifying this terminology to refer more generally to TF recognition sequences where appropriate.

3) The manuscript would benefit from a supplemental table describing the details of the sequencing data generated, including basic experimental metadata, sequencing QC statistics (read counts, duplicate rates, enrichment, etc.), and identification of replicates.

4) The authors say that the data have been submitted to GEO but the accession was not available upon submission. The GEO record would need to be verified as providing the sequencing data underlying the manuscript in a well-organized fashion.

5) Several figures include data and trend lines which are not clearly described in the legends (e.g. the lines vs. the bars in Figure 2H-J, Figure 5, and Figure 6).

6) The authors mention that experiments were performed in both serum-starved and stimulated cells. There are occasional references to differences between these conditions (e.g. line 393, line 702), but it appears the authors generally decided to lump data from both conditions together. The authors should provide an assessment of the similarity of the two conditions, and clearly describe and justify in the narrative how they handled this variable.

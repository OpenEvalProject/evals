# Peer review - Round 1

Editors:
- David Baulcombe, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47891.036](https://doi.org/10.7554/eLife.47891.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A positive feedback loop that establishes heterochromatin predisposes transcribed genes to stable epimutations" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript aims at understanding the mechanism of CG gene body methylation (gbM) by expressing the Arabidopsis CMT3 gene in Eutrema salsugineum, a species that is lacking a CMT3 ortholog and is devoid of gbM. The authors generated several transgenic lines in Eutrema expressing the Arabidopsis CMT3 gene, and followed the establishment of CHG methylation in two independent lines over six generations. They found de novo CHG methylation on repeat sequences, intergenic sequences and on some genes that share common features with genes targeted by gbM in Arabidopsis thaliana. Interestingly, these genes were not marked by H3K9me2, a modification that is usually associated with CMT3 activity. Finally, it is shown that CMT3 silencing led to a fast decrease of CHG and CHH methylation and to a slow decrease of CG methylation. It is proposed that transient deposition of H3K9me2 on genes may recruit CMT3, which in turn methylates DNA in CHG context, leading to CG methylation by an unknown mechanism.

Essential revisions:

1) The main shortcoming of the manuscript is the failure to point to a mechanism through which CHG methylation mediates CG methylation. The main data to support the assumption that CHG methylation leads to gbM are those in Figure 6, showing that loss of CMT3 expression (after transgene silencing) causes a slower decline of CG methylation compared to CHG and CHH methylation. The authors made use of the fact that CMT3 became silenced in the fifth generation in the AtCMT3-L2 line to test the effect of CMT3 loss on DNA methylation. Since it is unclear if the silencing is triggered by the transgene itself or by other factors, and how quickly silencing occurred, the results in Figure 6 are not completely conclusive. Moreover, the data are based on a single line and one individual per generation.

To address this point we request the analysis of at least one other non-silenced transgenic line, as well as the analysis of transgene-free progeny instead of the apparently silenced line.

2) Plants expressing CMT3 show body CHG methylation, but not body H3K9me2. The authors seem to interpret this observation as H3K9me2 recruiting CMT3 but H3K9me2 being removed by IBM1. An alternative interpretation of the results could be that H3K9me1, rather than H3K9me2, recruits CMT3. CMT3 binds not only to H3K9me2 but also to H3K9me1, even though CMT2 does not bind to H3K9me1 (Stroud et al., 2014, Figure 2D). Therefore, it seems possible that preexisting H3K9me1 guides CMT3, but not CMT2, to introduce CHG methylation in gene bodies.

To address this point we request the comparison of H3K9me1 in transgenic and non-transgenic control plants.

3) In Figure 5A, the authors compared CHG methylation gain and expression change in each gene in the T4 plant with body CHG methylation. Their interpretation of the results is that "genic CHG methylation in AtCMT3-expressing lines is uncoupled from heterochromatin formation and transcriptional silencing, similar to gbM." A possible complication can be that transcriptome should reflect both primary effects of the body CHG methylation and indirect effects from those primary effects. The indirect effects would not correlate with CHG methylation.

Furthermore, the proportion of CHG methylated genes in downregulated genes (X<-2) seems significantly higher than those in upregulated genes (2<X) and control genes (-2<X<2). The results look consistent with transcriptome analyses in ibm1 mutants in Arabidopsis (Inagaki et al., 2017). According to that literature, genes downregulated in ibm1 mutants have significant levels of CHG methylation, while upregulated genes do not. In addition, GO analyses of upregulated genes suggest their link to immune responses. The interpretation by Inagaki et al. was that CHG methylation induces downregulation for a subset of genes, and that the upregulation of many genes reflects indirect effects, likely due to primary changes in expression of some key factor involved in immune responses.

As the results in Figure 5A seem consistent with the transcriptome of ibm1 mutants (downregulation as primary effects and upregulation as indirect effects), we suggest GO analysis of upregulated genes, and statistical test for the overrepresentation of CHG gain in downregulated genes. If GO analysis of upregulated genes show some tendency, even if not immune response, that would suggest indirect effects involved.

More generally, the question is if body CHG methylation affects gene expression. That could be clarified by examining other plants without the gain of CHG methylation, such as other transgenic lines or other generations of plants in the same line, as controls (in addition to the non-transgenic wild-type plants). Especially interesting controls might be T6 plants of the line that lost body CHG methylation while keeping body CG methylation, because that might disentangle effects of body CG and CHG methylation.

Other points:

Please address the following additional points raised by the three reviewers as much as possible.

Reviewer #1:

4) The manuscript suggests that an increase of CMT3 expression leads to an increase of CHG methylation (subsection “Expression of AtCMT3 in E. salsugineum results in increased CHG methylation”, third paragraph). It is surprising why the authors did not use the AtCMT3-L3 for their analysis, as CMT3 is higher expressed in this line than in AtCMT3-L1 (Supplementary file 4). If the model is correct, AtCMT3-L3 should exhibit a higher methylation level than lines -L1 or -L2. As the authors have generated the methylome of this line (Figure 1—figure supplement 1), they should analyze gbM in this line. In fact, it would be advisable to include also the data for the other lines, since based on Figure 1—figure supplement 1 the authors produced methylome data for all lines until the second generation.

5) Figure 4: The choice of the generations used in the analysis requires justification; why analyzing generations 1, 2, 4, 5, 8, 11 for Col-0 and generations 5, 13 for suv4/5/6 ? At least they should include the 13th Col-0 generation in the analysis, since the DNA methylation pattern can be significantly affected after few generations (Figure 1, AtCMT3-L2). It is also advisable to include additional explanations to this paragraph to allow the reader to follow what has been analyzed.

6) It is unclear how the RNA seq data were analyzed (subsection “RNA sequencing mapping and analyses”).

7) For the ChIP-seq analysis, input seems to have been retrieved (subsection “Chromatin immunoprecipitation and sequencing (ChIP-seq)”) but apparently was not used for the normalization, neither have H3 data been used to normalize (subsection “ChIP-sequencing mapping and analyses”). The analysis has to be described in more detail or repeated.

Reviewer #2:

8) In regard to the ways of presentation of the ChIP-seq results, they showed metaplot and browser view for H3K9me2. It might also be informative to see scatter plot, comparing H3K9me2 level between the T4 and non-transgenic plants, to see if the signal increases in a subset of genes or TE genes.

9) Based on results in Figure 4, authors discussed that gain of CG methylation rate was significantly lower in Arabidopsis suvh4/5/6 mutant than in WT, but loss of CG methylation was not significantly different. The background statistics was not clear to me.

Reviewer #3:

10) The manuscript often refers to "targeting" of CMT3 to genes, which to me implies an active process. But the authors reach the conclusion (Discussion, last paragraph) that gbm is likely a passive byproduct of having a functional CMT3 enzyme. It's not that CMT3 is specifically targeted to genes, but that CMT3 acts in non-heterchromatic regions with some low frequency. It is suggested that the authors reconsider their use of the word targeting.

11) One of the results that most strongly supports the authors' model is that CG methylation is retained (and CHG and CHH methylation is lost) in CHGhyper genes after CMT3 is silenced in line L2 (Figure 6A and 6B). This led me to wonder why Eutrema lacks all gbm – presumably the loss of CMT3 occurred relatively recently in its evolutionarily history since its closest relatives retain CMT3 and gbm. Shouldn't some CG methylation still be present? Can the authors date the loss of CMT3 in Eutrema and does the total absence of gbm in this species fit with the timing of that loss and what we know about rates of mCG gain and loss in gene bodies over time?

12) Based on analysis of repeat methylation, the authors suggest that AtCMT3 preferentially targets heterochromatin over genes. There are alternative interpretations for these data. DNA methylation was reduced in all contexts in L2T6 in heterochromatin (Figure 6C), although it remained higher than in genes (Figure 6B). But the remaining methylation could be due to other maintenance and de novo pathways also being more active in those regions (MET1, RdDM, CMT2), rather than any residual CMT3 activity preferentially being directed to heterochromatin.

13) The portion of the manuscript about epimutations rates in suvh4/5/6 in Arabidopsis was a distraction from the main message. The effects on CG methylation gain, while statistically significant, do not appear particularly strong. I recommend removing this section from the paper.

14) The right panel of Figure 1—figure supplement 5 does not support the conclusion that higher levels of CMT3 expression are correlated with increased global CHG methylation. The R2 value of 0.59 is driven by two points and many samples have high CHG methylation but relatively low CMT3 expression. This doesn't seem like a key conclusion of the paper, and the authors should be more cautious in their interpretation.

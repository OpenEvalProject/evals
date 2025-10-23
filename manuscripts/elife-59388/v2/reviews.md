# Peer review - Round 1

Editors:
- Jie Xiao, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59388.sa1](https://doi.org/10.7554/eLife.59388.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work investigates an interesting question in gene regulation: when two independent transcription induction signals on one gene are combined, will it result in an additive or multiplicative gene expression level? Using genomic approaches to assay both mRNA expression and chromatin accessibility, the work finds that while there is a large range of responses, most genes favor either additive or multiplicative outcome. This work connects the phenomenological description of gene expression with a mechanistic insight of how two independent transcription signals could work together to regulate one gene.

Decision letter after peer review:

Thank you for submitting your article "Gene regulation gravitates towards either addition or multiplication when combining the effects of two signals" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hernan Garcia (Reviewer #1); Angela H DePace (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without substantial additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below mainly address clarity and presentation, with a few minor experiments if possible.

Summary:

In this work the authors used a genomic approach to investigate the way cells interpret two combined signals versus two individual signals. The authors used RNA-seq to examine the gene expression outputs from thousands of genes in response to two signal inputs, TGF-β and retinoic acid, either individually or in combination. The authors found that when stimulated with both signals, most cells exhibited additive or multiplicative responses. The authors further used paired chromatin accessibility by ATAC-seq to relate such responses to putative transcription factory binding patterns in these genes. Surprisingly, ATAC-seq revealed that most genes prefer addition to combine two signals as chromatin accessibility is largely additive, although some super-additive accessibility may respond to multiplicative gene expression.

This work provides a platform to quantitatively assess combinatorial transcription regulation both at the level of DNA accessibility and transcriptional output. Although the concept of additive vs. multiplicative transcriptional response is phenomenological, it may be used to clarify and constrain certain biophysical models of transcriptional regulation and set the stage for a better understanding of the molecular relation between combinatorial transcription factor binding and corresponding gene activity.

While the work is written in a clear and concise language, there are places that require further clarification and better presentations.

Essential revisions:

1) Presentations of the logic and data: it is hard to follow the math in the absence of equations:

a) Please show the equations featured in Figure 1A in the main text together with some derivation or explanation that can build intuition.

b) The simulations results shown in Figure 1 and Figure 2 are a key part of the argument. Yet, their details are buried in the SI, making it hard to follow their justification (which could also benefit from schematics). Please explain these simulations in the context of the main text.

c) "For each dosage of the combination treatment, we classified a gene as sub-additive if the additive and multiplicative predictions were higher than the 80% confidence interval, additive if only the additive prediction laid in the confidence interval, multiplicative if only the multiplicative prediction laid in the interval, super-multiplicative if both additive and multiplicative predictions were below the confidence interval, and ambiguous if both the additive and the multiplicative prediction laid within the interval." Please show this graphically and/or with an equation.

2) Clarifications of experimental conditions and results:

a) The authors treat the cells for 72h. This is a very long time where secondary effects may be dominating the results. The choice of this time point should, at the very least, be justified and discussed. For example, previous studies that quantitatively characterized distinct temporal dynamics in SMAD signaling after TGF-β treatment showed a transient, dose dependent SMAD response in the first 4 h after TGF-β treatment, with a strong early peak in the nuclear/cytoplasmic ratio of SMAD2/4 (Clarke and Liu, 2008; Schmierer et al., 2008; Zi et al., 2011; Zi et al., 2012; Strasen et al., 2018). In addition, TGF-β signaling has been suggested to depend on cell density and cell cycle stage (Zieba et al., 2012), which may also affect the results. Also it would be helpful to have a quantitative measure of the corresponding nuclear TF levels at the selected time-point after 72h (e.g. for main affected TFs such as pSMAD2 and RARA levels).

b) MCF7 cells were treated with three different doses of TGF-β (1.25, 5, and 10 ng/mL) and RA (50, 200 and 400 nM). As it seems that the selected doses are higher than what has been used in previous studies, the authors should comment on their choice.

c) The authors state that "We defined a master set of 1,398 upregulated genes by selecting the set of genes that were differentially expressed in any dose of the combination treatment (log FC {greater than or equal to} 0.5 and padj {less than or equal to} 0.05) and that had increased expression in each dose of each individual signal." It is unclear how this gene set relates to the top-right Venn diagram in Figure 1B, in which only 303 genes are shown as being upregulated in all three treatments and the total according to the numbers in the diagram are >1398.

d) Figure 1B shows that a large proportion of genes were differentially expressed in response to both signals, but not to either of the signals individually. Their responses are presumably more non-additive than the responses of genes upregulated in response to all three treatments. Restricting analysis to the latter group therefore introduces a bias for certain modes of combinatorial regulation. The justification for this choice should be discussed.

e) The authors frame the work on the basis of simple models of gene regulation by pairs of transcription factors that predict either addition or multiplication. However, they are activating two signaling pathways that could interact also at the level of signal transduction (and need not be directly regulating the genes in question, as noted in point 1). How justifiable is it to make inferences about the nature of combinatorial transcriptional regulation from this kind of experimental set up? These issues should be made clearer from the beginning and should be taken into account when interpreting the data.

f) Related to the point above, the authors use chromatin accessibility as a proxy for TF binding. However, this does not need to be the case, especially if the accessibility data are considered quantitatively. For example, TFs may bind and recruit remodeling factors that affect accessibility differentially across the genome, obscuring the relationship between TF binding and accessibility. This is especially pertinent at longer time scales after perturbation. We suggest presenting the data on accessibility as just that, instead of presenting it as data that directly reports on TF binding. The relationship to TF binding can and should still be explored in the analyses, but with clarification for how accessibility data is limited in this case. The following are instances where accessibility data is described as directly reporting on TF binding that we recommend revising (the list is not exhaustive):

– the title of section two

– Figure 2E

– the link between models of TF control and the relationship between peaks and expression, such as the reference to the thermodynamic model at the end of section 3.

– remove the implicit assumption between cooperativity of TF binding and super-additive peaks in section 3 and section 4. This may help explain more naturally the lack of dual-motif finding in section 4.

3) Title: The authors suggest a bimodal distribution for the observed c values, with peaks at 0 and 1. The authors write that "Our simulated c value distributions bear a moderate resemblance to our observed c value distributions". This conclusion is central to the paper's claim that "Gene regulation gravitates towards either addition or multiplication when combining the effects of two signals" (title) and that "the combined responses exhibited a range of behaviors, but clearly favored both additive and multiplicative combined transcriptional responses" (Abstract). However, the additional peak at c=1 is not obvious from the data in Figure 1E. Stronger evidence (i.e. statistical analysis of the observed distributions) would be needed to demonstrate overrepresentation of c values ~1. Alternatively, the title and Abstract could be revised to better reflect the strength of the findings.

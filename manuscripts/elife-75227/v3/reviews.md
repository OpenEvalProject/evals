# Peer review - Round 1

Editors:
- Gene W Yeo, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75227.sa1](https://doi.org/10.7554/eLife.75227.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Proteogenomic analysis of aneuploidy reveals divergent types of gene expression regulation across cellular pathways" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Matthias Selbach (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors show that SCNAs are often significantly compensated at the protein level in most tumor types. This compensation is also normally stronger than RNA level compensation. A technical issue about this finding that needs to be addressed is that this is mainly based on proteomics data that used TMT for quantification. TMT-based quantifications, although quite precise, are not always the most accurate measurements in the sense of capturing the true amplitude of changes. This is due to the so-called ratio compression of TMT mass spec data. The authors need to account for that in order to exclude that this technical limitation of TMT-based proteomics measurements is a main contributor to the protein level compensation seen. Do the authors also have some proteomics data where label-free quantification of SILAC quantification was used? Do the same conclusions hold true when such data sets are used?

2) Many of the statistically significant differences seen – e.g complexed proteins versus non-complexed proteins, highly conserved proteins versus less conserved proteins – have actually a relatively small effect size. Rather than a bootstrapping strategy, it would be useful to also evaluate the differences using a Mann-Whitney U test.

Reviewer #1 (Recommendations for the authors):

– Figure 3A legend: for group 2 it should say "High RNA-protein correlation" instead of "Low RNA-protein correlation", shouldn't it?

– In Methods section lines 681 to 699. The data sets used should be described in more detail and not just by giving direct links to them. E.g. what is the quantification method for proteomics data used, etc.? This is important to evaluate the analysis for potential technical artifacts due to data collection in the different data sets.

– In the "Methods" section at line 732 – "random sampling the CS" – how big was the sample each time? This is not just here but throughout the analysis part where bootstrapping is used.

– In the "Methods" section lines 765 to 772 – to be honest I do not fully understand what the authors did here. Could you maybe rephrase this section?

– In the "Methods" section line 891 – the peptides were TMT labeled. Therefore, I do not think DIA measurements were done but rather DDA – should that maybe mean "(DDA)" instead of "DIA"?

– In the "Methods" section line 915 – it indicates that in MaxQuant the "Match between the runs" feature was on. What is the benefit of that if TMT samples were measured as an MS2 spectrum anyway needs to be recorded to get quantitative information? Did the authors use another program in addition, like Dart-ID?

Reviewer #2 (Recommendations for the authors):

1. Ribosomal proteins make up a significant fraction of proteins that are overproduced and show protein-level compensation in aneuploid cells. Did the authors check how (i) ribosomal proteins look like as a group and (ii) how the data changes if ribosomal proteins are excluded from the analyses? This is to assess whether the findings are dominated by this specific subset of proteins.

2. One technical limitation of the TMT multiplexes proteomic data is ratio compression. Due to this effect, the observed absolute log2FC tends to be smaller than true log2FCs. This technical artifact might be mist-interpreted as protein-level compensation. Please mention and discuss this potential limitation.

3. Line 123: "Dosage compensation is a process by which cells modulate gene expression to buffer against changes in DNA copy number" – I think dosage compensation is defined in the context of sex chromosomes – a mechanism to ensure that the homogametic sex does not have too much or the heterogametic sex too little of the gene products. I do not think the term should be used in the context of aneuploidy.

4. Line 138: "For each gene of each cancer type, we defined the samples that did not have DNA copy number changes (log2 copy number ratio between -0.2 to 0.2) as the neutral group." How are these DNA copy number changes normalized? How did the authors deal with possible whole genome doubling in cancer? This question is relevant because it affects the size of relative changes: For example, going from 2 copies (diploid cancer) to 3 copies (for amplified regions) is a larger relative gain than from 4 copies (cancer with whole genome doubling) to 5.

5. Line 554: "The protein compensation for complex genes of DNA gains is thought to occur through protein degradation of the overabundant subunits (McShane et al., 2016). However, this model cannot easily explain how protein compensation happens after DNA losses and why the compensation is stronger for protein complex genes." I disagree with this point: The model can (to some extent) also explain compensation after DNA loss. The key point is that overproduction of proteins does not only occur during aneuploidy but is a widespread feature even in euploid cells: Many subunits of multiprotein complexes are overproduced (and rapidly degraded) in diploid cells. This baseline overproduction buffers proteins against gene copy number losses: Loss of one copy for such will result in reduced protein overproduction (and reduced degradation). But as long as the overproduction (at baseline) is greater than the reduction due to the DNA-level loss there should be full compensation. One way to assess this would be to look at how the protein compensation upon DNA loss correlates with the degree of protein overproduction in diploid cells. Specifically, the fraction of protein overproduction (and rapid degradation) in diploid RPE-1 cells can be easily computed from the Markov-chain based model for non-exponential protein degradation (see Figure 2 plus legend in Taggart et al., 2020 for the formula and Table S4 from McShane et al., 2016 for model parameters). Assuming this overproduction is to some extent similar in different cells, I would expect that protein compensation upon DNA loss correlates with "baseline" protein overproduction in diploid cells.

6. Line 586 and following: This is the Discussion section, and the authors are of course free to speculate about the biological meaning of their findings. Having said this, I have different opinions on a number of points they may want to consider. First, I do not think that energy conservation can explain RNA-level regulation in a satisfying way: The energy cost to synthesise and degrade mRNAs is negligible relative to the cost to synthesise and degrade proteins (see for example figure S12C in Schwanhausser et al., Nature, 2011). Second, I do not think that the faster speed of regulation can explain mRNA level regulation: In contrast to the statement made in the discussion, regulation at the protein level (translation or protein degradation) enables faster changes in protein levels than changes at the mRNA level (see DOI: 10.1002/bies.201300017, for example). In contrast to these explanations, I think it is helpful to see protein-level regulation as a consequence of the missing mRNA-level regulation: Some genes may be gene-specific regulatory feedback mechanisms regulating mRNA levels. These genes do not have much protein-level control because copy number changes are already buffered at the mRNA level. For example, as nicely pointed out by the authors, protein-level control is difficult for secreted proteins, which means that there is evolutionary pressure to evolve mRNA-level feedback mechanisms. In contrast, genes w/o such mRNA level buffering are buffered at the protein level. The degradation of orphan protein complex subunits provides a mechanistic explanation of how this could be achieved. I think it is also helpful to think about how regulation can mechanistically occur, given that there is no known universal mechanism that "measures" mRNA or protein levels and adjusts transcription and translation accordingly. In my opinion, RNA-level regulation evolved because (i) this regulation is functionally important (like for genes encoding secreted proteins) and (ii) because regulatory feedback is mechanistically feasible (like transcription factors regulating their own transcription, RNA-binding proteins regulating stability of their own RNA). Other genes which did not have gene-specific regulatory feedback loops remain unbuffered or are buffered at the protein level (where the degradation of orphan subunits via ligases like UBE2O provides a universal mechanism for protein-level buffering). Some of these points are also discussed in a recent review (see below).

7. The authors may want to add these two relevant recent papers – Senger G, Schaefer MH. 2021. Protein Complex Organization Imposes Constraints on Proteome Dysregulation in Cancer. Frontiers in Bioinformatics. 1:33- Buccitelli C, Selbach M. 2020. mRNAs, proteins and the emerging principles of gene expression control. Nat Rev Genet. 630-644.


---

# Peer review - Round 1

Editors:
- Gene W Yeo, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75227.sa0](https://doi.org/10.7554/eLife.75227.sa0)

The manuscript is of broad interest to researchers in the field of gene expression regulation and especially gene expression regulation in cancer cells. Gene expression can be regulated at several levels – in particular, the RNA and protein level. How each regulatory layer contributes to the final gene expression level is a central question in molecular biology. The authors tackle this fundamental question by asking how copy number variations at the level of DNA impact the other expression layers of RNA and protein. They do so mainly in a huge cohort of cancer samples, but also show that their findings extend to untransformed cells, and they find that there is rarely compensatory regulation at the RNA and protein level together, but that depending on the gene, expression is either compensated at the RNA level or protein level. This is an extensive meta-analysis of a huge set of samples that will be of interest to a broad readership.

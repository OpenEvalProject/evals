# Peer review - Round 1

Editors:
- Asifa Akhtar, Max Planck Institute for Immunobiology and Epigenetics , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16970.038](https://doi.org/10.7554/eLife.16970.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Nucleosome positions and alternative chromatin states revealed by computation approach leveraging digestion variability" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai as the Senior Editor, Asifa Akhtar as Reviewing Editor, and two reviewers, including Juan Vaquerizas (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this study, Zhou et al. introduce a computational method to determine nucleosome positioning from MNase-seq data at a base-pair resolution. Due to digestion variability, it has been a problem comparing nucleosome positioning maps between samples from different MNase-seq experiments. It is also impossible to separate biological variations in nucleosome positioning from technical variations in MNase digestion. The computational method proposed by the authors looks quite promising to solve these problems.

Overall the study is interesting and the method will be of use to the genomics community, since it is currently not straightforward to determine nucleosome positioning with high accuracy.

1) There are currently a number of other methods to determine nucleosome positioning. The manuscript will greatly benefit from performing a comparison with those, so the readers can easily assess the performance of the method.

2) The method describing how to use the software to generate the digestion variability template is too simplified, and the GitHub site is also poorly organized with no documentations, making it very hard to apply the authors' method to other MNase-seq experiments. It limits the usefulness of the authors' approach for the wide audience of eLife. This aspect should be improved upon revision.

3) The authors propose there are alternative positioning of nucleosomes near TSSs. Why are these alternative positioning nucleosomes not apparent in the chemical approach (Brogaard et al. 2012)? What will be the overlap between author's approach and the Brogaard approach if you only consider the alternative positioned nucleosomes?

4) The authors suggest that distal nucleosomes might work by providing a boundary for the assembly of the PIC (subsection “Alternative chromatin states and transcription initiation”, third paragraph). However, the authors do not provide enough evidence to be able to make this statement since the distal positioning of the nucleosomes might just reflect the binding of the PIC, and therefore might just be a consequence of the transcriptional process, rather than the provision of a boundary.

5) The authors report a link between the presence of uniquely positioned nucleosomes in highly expressed genes. It would be interesting to stratify genes according to gene expression (for examples using quintiles) and to evaluate whether there are specific enrichments of unique vs alternative nucleosomes across the stratified dataset. This would allow the authors to discern whether the unique vs. alternative nucleosome observation could be explained by the overall level of gene expression or whether the two groups have functional implications. This is important in the context of the subsequent sequence analysis since the authors argue that unique nucleosomes have specific sequence features, which suggest functional implications.

6) In order to assess the functional implications, the manuscript will improve considerably if the unique vs. alternative classification analysis and subsequent gene expression and sequence analyses would be repeated using the human dataset in Figure 4.

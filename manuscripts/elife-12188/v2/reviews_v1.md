# Peer review - Round 1

Editors:
- Sarah A Teichmann, EMBL-European Bioinformatics Institute & Wellcome Trust Sanger Institute , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12188.034](https://doi.org/10.7554/eLife.12188.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Inference of gene regulation functions from dynamic transcriptome data" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. One of the two reviewers has agreed to reveal his identity: Hernan Garcia.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission

Summary:

Gene regulatory functions (GRFs) are the fundamental unit of any quantitative description of transcriptional programs. These functions describe the output level of gene expression as a function of the input concentrations of activators and repressors and of the binding site arrangement of these molecules on regulatory DNA. The measurement of these GRFs has been demonstrated repeatedly in the context of synthetic constructs, where DNA regulatory architecture and input transcription factor concentration can be precisely controlled. However, the field is missing technology to go beyond synthetic circuits and systematically expand these dissections to endogenous gene regulatory circuits. Only with the combined ability to assay synthetic and endogenous gene circuits can we develop a predictive understanding of the gene regulatory code underlying cellular decision programs.

In this manuscript, Hillenbrand et al. develop a computational approach to infer GRF from endogenous RNA-Seq data sets. They use mRNA data of oscillatory genes in order to infer the protein concentration of input transcription factors. This inferred protein dynamic is combined with the output mRNA dynamics of target genes in order to obtain GRFs. These GRFs are put in the context of the underlying DNA regulatory architecture using theoretical models based on equilibrium statistical mechanics. Finally, they show how this approach can go beyond the quantification of GRFs to also provide a means to map gene regulatory networks and their quantitative parameters.

Essential revisions:

For acceptance at eLife, as rigorous as possible validation of the model is required. This can include checking resulting parameters against published values, as well as against published or novel experimental data confirming any of the parameters, such as through knockout or knockdown or overexpression experiments.

Indeed, an intriguing consequence of plots such as those shown in Figure 3 is that the authors make quantitative predictions about the GRF at input concentration values that are not present in the calibration data set. For example, most 3D plots in the paper extrapolate gene expression beyond the input levels observed in the wild-type. The authors could propose the experiments necessary to test these predictions. Perhaps there are already such datasets publicly available. If not, the authors could generate some to support the model.

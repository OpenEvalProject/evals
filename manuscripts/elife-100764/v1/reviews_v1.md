# Peer review - Round 1

Editors:
- Irwin Davidson, Institut de Génétique et de Biologie Moléculaire et Cellulaire France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100764.3.sa0](https://doi.org/10.7554/eLife.100764.3.sa0)

This valuable study compares ChIP-seq and ChEC-seq2 techniques to investigate RNA polymerase II (RNAPII) binding patterns in yeast, revealing that ChEC-seq2 captures distinct regulatory events associated with active transcription missed by ChIP-seq. The authors use ChEC-seq2 data to build a stochastic model of RNAPII kinetics, providing convincing new insights into transcription regulation and the role of the nuclear pore complex. The paper highlights the importance of careful methodological comparisons in understanding RNAPII dynamics.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100764.3.sa1](https://doi.org/10.7554/eLife.100764.3.sa1)

Summary:

In this study, the authors use ChEC-seq, an MNase based method to map yeast RNA pol II. Part of the reasoning for this study is that earlier biochemical work suggested pol II initiation and termination should involve slow steps at the UAS/promoter and termination regions that are not well visualized by formaldehyde-based ChIP methods. Here the authors find that pol II ChIP and ChEC give complementary patterns. Pol II ChIP signals are strongest in the coding region (where ChIP signal correlates well with transcription (rho = 0.62)). In contrast, pol II ChEC signals are strongest at promoters (rho = 0.52) and terminator regions. Weaker upstream ChEC signals are also observed at the STM class genes where biochemical studies have suggested a form of Pol (and maybe other general factors) is recruited to UAS sites. ChEC of TFIIA and TFIIE give promoter-specific ChEC signals as expected. Extending this work to elongation factors Ctk1 and Spt5 unexpectedly give strong signals near the PIC location and little signals over the coding region. This, and mapping CTD S2 and S5 phosphorylation by ChEC suggests to me that, for some reason, ChEC isn't optimal for detecting components of the elongation complex over coding regions.

Examples are also presented where perturbations of transcription can be measured by ChEC. Modeling studies are shown where adjustment of kinetic parameters agree well with ChEC data and that these models can be used to estimate which steps in transcription are affected by various perturbations. However, no tests were performed to see if the predictions could be validated by other means. Finally, the role of nuclear pore binding by Gcn4 is explored, although the effects are small and this proposal should be explored more completely in future studies. Overall, the authors show that pol II ChEC is a valuable and complementary method for investigating transcription mechanisms and slow steps at the initiation and termination regions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100764.3.sa2](https://doi.org/10.7554/eLife.100764.3.sa2)

Summary:

The study by VanBalzen et. al. compares chromatin immunoprecipitation (ChIP-seq) and chromatin endogenous cleavage sequencing (ChEC-seq2) to examine RNA polymerase II (RNAPII) binding patterns in yeast. While ChIP-seq shows RNAPII enrichment mainly over transcribed regions, ChEC-seq2 highlights RNAPII binding at promoters and upstream activating sequences (UASs), suggesting it captures distinct RNAPII populations that the authors speculate are linked more tightly to active transcription. The authors develop a stochastic model for RNAPII kinetics using ChEC-seq2 data, revealing insights into transcription regulation and the role of the nuclear pore complex in stabilizing promoter-associated RNAPII. The study suggests that ChEC-seq2 identifies regulatory events that ChIP-seq may overlook.

Strengths:

(1) This is a carefully crafted study that adds significantly to existing literature in this area. Transgenic MNase fusions with endogenous Rpb1 and Rpb3 subunits were carefully performed, and complemented by fusions with several additional proteins that help the authors to dissect the transcription cycle. Both the S. cerevisiae lines and the sequencing data are likely to be of significant use to the community

(2) The validation of ChEC-seq2 and its comparison with ChIP-seq is highly valuable technical information for the community.

(3) The kinetic modeling appears to be thoughtfully done.

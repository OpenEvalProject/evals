# Peer review - Round 1

Editors:
- James M Berger, Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67236.sa1](https://doi.org/10.7554/eLife.67236.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

DNA supercoiling plays a key role in the regulation of DNA replication and transcription. Both processes affect DNA supercoiling locally; thus, the precise distribution of DNA superhelicity is expected to be highly dynamic and change depending on cellular status. Whether there exist chromosomal regions that display preferential supercoiling levels has been unknown due to a paucity of technologies for measuring supercoiling throughout the genome. The generation and removal of topologically stressed DNA is required for cell viability but, when mishandled, can lead to molecular pathologies. The work described in the present manuscript uses GapR, a protein that preferentially binds overwound DNA, to map genomic regions of positive supercoiling in bacteria and yeast. Such insights are needed to understand how supercoiling is partitioned and controlled at chromosome-wide level.

Decision letter after peer review:

Thank you for submitting your article "High-resolution, genome-wide mapping of positive supercoiling in chromosomes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please see the request for revisions as detailed below.

Reviewer #1:

In this study, the authors present a new method that is claimed to measure (+) supercoiling levels in vivo.

The topology of chromosomal DNA in bacteria is known to be highly dynamic and to change from cell to cell. The method proposed by the authors would thus detect regions with 'persistent' or 'preferential' levels of (+) DNA supercoiling. Such a measurement would be relevant to understanding bacterial transcription, replication and DNA segregation.

In a previous study, the authors show that GapR binds positively supercoiled DNA in vivo using biochemical methods (Guo. et al., Cell 2018). In the present study they further investigate the mechanism of (+) supercoiled DNA binding using magnetic tweezers.

Their first experiment shows that, in the presence of GapR, introduction of (+) supercoiling reduces the extension of the DNA molecule but to a lower degree than in absence of GapR. The authors conclude that GapR precludes the conversion of (+) supercoiling to (+) writhe. It is not clear though where is the excess (+) supercoiling going. Does GapR favour conversion of the added (+) supercoiling into (+) twist? Is there any clue of this in their crystallographic data? What is their model for how GapR is constraining the added (+) supercoiling? The scheme in Figure 1G is very confusing in this regard.

The authors then monitor changes in DNA extension over time in absence and presence of GapR for (+) and (-) supercoiled DNA substrates. They conclude that GapR dynamically binds and diffuses along (-) supercoiled DNA but stably binds to (+) supercoiled DNA. I do not see the evidence for the former claim (dynamic binding and diffusion/sliding). I do not fully agree with the evidence shown for the second conclusion: 1 μm is a pretty high concentration for magnetic tweezers experiments. What is the binding affinity of GapR? Their moderate effect of GapR at lower concentrations (100nM) suggests that the binding affinity is likely in the hundreds of micromolars. In this range, the residence time of a protein on its substrate is short (sec) thus I am confused as to why the authors say GapR binds stably to (+) supercoiled DNA.

All in all, magnetic tweezers experiments are interesting, but do not clearly demonstrate binding of GapR to (+) supercoiling DNA, do not provide further mechanistic insight or strong support for their model of how GapR binds to (+)/(-) supercoiled DNA. Perhaps a higher resolution assay (e.g rotor bead) could shed more light into the mechanism of binding of GapR.

Next, the authors use ChIP-seq on GapR and a fusion of GapR to 3xFLAG. They see that these proteins bind to AT-rich regions located downstream from a ribosomal operon, and their binding is reduced when transcription is inhibited. In the example shown, there are several highly transcribed ribosomal genes in the operon. I would have expected to see binding of GapR throughout the operon or at least at the 3' ends of these genes, as RNApol2 is producing (+) supercoils throughout the entire operon. However, binding of GapR appears only at the 3' end of the operon. Do these experiments really show that GapR binds to (+) supercoils in E. coli as claimed by the authors?

The authors then used mutants of GapR to determine if binding of GapR to DNA was due to chromosome accessibility or to DNA topology. For this they used a deletion mutant of GapR that binds DNA but does not encircle it. They show that this mutant binds (+) supercoiled DNA in a biochemical topological assay. However, it would be more consistent to use the magnetic tweezers assay of Figure 1. Does this mutant also suppress accumulation of (+) writhe? how are the dynamics of binding to (-), (+) DNA affected? These experiments could provide insight and support for their model of binding of GapR to (+) supercoiled DNA (see above).

Next, they used ChIP-seq to show that the deletion mutant fails to bind to AT-rich regions at the 3' ends of highly expressed operons. From this, they conclude that binding to (+) supercoiled regions requires tetramerization. I am not convinced that the data supports this conclusion. If the tetramerization domain was required to increase the affinity of DNA binding of GapR dimers, then one would also expect a loss in specific binding in absence of the tetramerization domain. If this domain was needed for interactions with other proteins present at 3'-ends of highly transcribed genes, then one would also expect a similar result.

Reviewer #2:

This work claims to provide a new tool that specifically detects positive DNA supercoiling, genome-wide. The research question asked in the manuscript is quite important. The tool is based on the ability of bacterial protein GapR to bind preferentially with over-twisted DNA. The manuscript is divided into two parts: first, a demonstration that bacterial protein GapR binds preferentially with over-twisted DNA, both in single-molecule assays and in vivo at sites of already predicted to be positively supercoiled, and then a genome-wide search for positive supercoiling at the key genomic positions. There are several promising results in the second part of the manuscript, but they are all based on the first part where the presented evidence/data are not sufficient to draw decisive conclusions. Many additional experiments, much more data and further controls are required to prove that GapR could be used as a probe for positive DNA supercoiling.

1) The authors in their previous work used analysis of the DNA supercoiling induced by plasmid-GapR interaction to suggest that the protein likely binds over-twisted DNA. In the current manuscript, Guo et al., perform again this analysis (Figure 3A, S3E). The weak point in their DNA supercoiling assay is that DNA topology does not change up to 2.5 μM GapR, and then an abrupt change is observed as the concentration is increased. This is not the expected pattern if GapR binding increases incrementally as it introduces or stabilizes a small amount of positive twist in the DNA (see Clark and Leblanc, Methods Mol Biol. 2015 for a recent review of this method). The distribution of topoisomers in the assay should gradually shift from the relaxed state to the new supercoiled position until binding is saturated. One of the simplest explanations of the observed unusual pattern is a synergy threshold: for example, the GapR-mediated DNA bridging which is reported in the literature (see Lourenço et al., mBio. 2020) might give this result. To confirm their suggestion, the authors use single-molecule assays. Based on the pattern of DNA "rotation-extension curve" generated by this assay, the authors state that GapR stably interacts with positively supercoiled DNA while the interaction with negatively supercoiled DNA is unstable. However, as admitted in the manuscript this curve is highly unusual and cannot be explained solely by the constraining of positive supercoils. The high fluctuations of DNA length on the negative-supercoiling side of the curve once again suggests that some kind of cooperative binding-unbinding of GapR affects the shape of the DNA.

2) The authors imply that the GapR-binding method might be superior to psoralen-crosslinking methods for the detection of positive supercoiling but there is no actual comparison. Psoralen assays have been calibrated both in vitro and in vivo (see Bermúdez et al., Nucleic Acids Res. 2010, and Kouzine et al., Nat Struct Mol Biol. 2008). Similar calibration is required for GapR study. In the current manuscript, the authors detected GapR binding at sites expected to be positive supercoiling (Figure 2, 3, and 4) which is not sufficient to support the key claims in the manuscript – GapR is binding at positively supercoiled sites. Based on the known topological plasticity of chromatin to the DNA over-twisting, one might expect that GapR is able to differentiate between difference positive torsional stress stored in twist with that in the writhe of the 3-D shape of DNA in the E. coli genome or in yeast chromatin. Although exciting, the full characterization of DNA-GapR interaction is required.

3) The strength of the manuscript is the technically impressive analysis of the GapR localization in the genome reported in the second part of the manuscript. The authors find that this protein does recognize the strategic regions of the genome (Figure 6 and 7). With proper analysis of DNA-GapR interaction in the first part of the manuscript, these data will indicate that GapR is an important probe for DNA conformation in the context of key genomic processes.

1) The quality of the 2D gels should be improved and accurate titration with broader range of protein concentrations should be performed. The explanation of the topoisomers' distribution should minimize pre-assumptions. The ability of the protein (protein preparation) to induce DNA double-stranded breaks and nicks should be explained.

2) The DNA topology electrophoresis and single-molecular assays were performed at different protein concentrations. What is the reason for choosing different concentrations? What would we see if single-molecular assay would be performed at higher protein concentration? All anomalies on the extension curve should be explained (might be added to the Supplementary section). What is the reason for the high fluctuation on the negative side of the curve? I do not think it can be explained by single binding-unbinding-diffusing event. Why is naked, relaxed DNA is shorter than the same DNA in the presence of the protein? One might expect the opposite if GapR constrains ower-twisted DNA.

3) Preferential binding of GapR to positively supercoiling DNA over negatively supercoiled DNA was not proven as the single-molecular assay did not give a definitive answer. The study should be supplemented by competition assay between different DNA conformations. Could you efficiently fish out positively supercoiled plasmid from the mixture of genomic DNA circles/plasmids wound to different degrees? What happens if you compare normal plasmids (able to form supercoils) with DNA minicircles (unable to form supercoils)?

4) In the omics study, GapR binding should be compared with psoralen-based maps. The assumption that psoralen-based studies infer the presence of positive supercoils by the absence of crosslinking is wrong. In the classical approach, the presence of supercoiling is inferred from the changes of psoralen intercalation after fast nicking and relaxation of the DNA inside the cells (Sinden's studies). In addition, it is incorrect to say that "psoralen-based studies are still limited in resolution". With developing of high throughput sequencing methods, the resolution of supercoiling is close to the DNA persistence length (Henikoff's studies).

5) All discussion of the positive supercoiling in yeast should be supplemented with the introduction of known torsional plasticity of chromatin to DNA over-twisting. The current consensus in the field is that chromatin fiber is torsionally soft with respect to positive supercoiling – twisting of chromatin results in the reorganization of nucleosomal template without introducing DNA over-twisting. How do you align this expected topological plasticity with the proposed ability of GapR to sense twist rather than writhe?

6) There is very little discussion on consequences of the prolonged expression of GapR protein. So, one caveat is that the expression of GapR over time does not perturb the DNA topology or chromatin conformation in cells. There may be quick and more general approaches for this method than building strains and cell-lines to express GapR. For example, the authors could make yeast spheroplasts, treat with saponin/digitonin, in the presence of GapR, fix with formalin and then perform ChIP-seq, (this is the sort manipulation that is used in native ChIP) and then compare these results with in vivo expression of GapR. This would potentially eliminate artefacts of prolonged in vivo expression and greatly expand the general utility of the method as it could be than used on any cell line without transgenic or knock-in expression.

7) The sentence "Genomic DNA can become supercoiled when the DNA duplex winds about its own axis forming a right-handed superhelix (positive supercoiling) or a left-handed superhelix (negative supercoiling)" is misleading. In the plectonemic form of unconstrained supercoiling, a right-handed superhelix is assigned a negative number (negative supercoiling) and a left-handed superhelix is assigned a positive number (positive supercoiling). Opposite for solenoid/toriodal form of constrained supercoiling.

8) Moderate binding is detected to 5' ends of weakly expressed genes but not to highly expressed gene. It would be good to check if this is due to an upstream co-directional transcript that pumps positive supercoils into the promoter of the weakly expressed genes making the promoter harder to melt and transcribe.

9) DNase likes G-C rich DNA better than A-T-rich, GapR likes the opposite. Does the base composition partly explain separation of GapR and DNaseI sites?

10) The idea of involvement of positive supercoiling in R-loop genesis should be discussed together with recent work from Chedin' lab (Stolz et al., Proc Natl Acad Sci U S A. 2019).

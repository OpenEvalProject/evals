# Peer review - Round 1

Editors:
- Robert H Singer, Albert Einstein College of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12175.020](https://doi.org/10.7554/eLife.12175.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Single-cell analysis of transcription kinetics across the cell cycle" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Rob Singer (Reviewing Editor) and Aviv Regev as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you can see below, the reviewers were enthusiastic about the manuscript and felt it was of high quality. The need for revision centers on some items where they felt the presentation required more extensive discussion, for instance in the dosage compensation discussion and the modeling approach. We look forward to the revised manuscript soon.

Reviewer #1:

In the lovely paper "Single-cell analysis of transcription kinetics across the cell cycle" by Skinner et al., the authors investigate how transcriptional parameters of Nanog and Oct4 affect the cell-to-cell variability of these genes and how these parameters change during the cell cycle. Using single-molecule FISH measurement to precisely quantify nascent and mature RNA, and by determining the transcriptional kinetic parameters the authors show that the difference in variability between the two genes can be explained by the slower ON/OFF switching by Nanog.

I think this study is very timely, as there has been increased interest these days in the connections between global regulation of transcriptional processes and transcriptional bursts-in this case, the demonstration that there is dosage compensation upon DNA replication. The authors also have wisely chosen to study Nanog and Oct4, which has been the topic of much recent debate. One of the highlights is the authors showing that the kinetics of Nanog are what leads to the oft-described variability in Nanog transcript levels. It is also methodologically rigorous, including the RNA quantification, the modelling of the kinetic parameters the analysis, as well as the extensive documentation of the methods used.

1) The more familiar usage of the term dosage compensation comes from the case of sex chromosome dosage compensation (e.g., to balance out X chromosome dosage differences between male and female mice). I think what the authors are observing is rightly called dosage compensation, but it's probably worth mentioning the more traditional context in which the term is used and explicitly pointing out the similarities and differences.

2) The paper was exceptional in its depth of methods documentation, yet regarding the cell cycle modelling and the transcriptional kinetic parameters, the paper would benefit if the authors described some of the modeling more in the main text. For example, it would be useful to better clarify the difference between the "rough" and detailed cell-cycle analysis, possibly in a sentence at the beginning of the section. Similarly, it would be helpful if a brief explanation of the ergodic rate analysis could also be found in the main text. Along these lines: Would be helpful to define the term "cell cycle age". Also, in Figure 3C, there is no indication as to what the start and end point for "Time in cell cycle" is, and thus how the 10 time windows relate to G1, S, G2 phase.

3) One of the results I found most interesting was that the reporter did not show any dosage compensation effect. I was hoping the authors could speculate on this a bit more. In the case of Padovan-Merhar et al., they show that whatever the cause is for the dosage compensation, it's occurring in cis to the DNA, like a histone modification or something that gets diluted upon replication. It's possible that the reporter gene is not fully chromatinized, which is why it doesn't show the dosage compensation effect. Anyway, I thought it was a cool result that the authors may want to highlight more.

Reviewer #2:

Cell cycle phase is one of the most important extrinsic factors determining differences within populations of actively dividing cells. In this study Golding and colleagues combine high-quality single molecule FISH of mature and nascent mRNA and computational approaches to infer cell cycle phase and study its effect on changes in promoter burst parameters. They demonstrate their approach by identifying a dosage compensation mechanism entailing a decline in the burst frequency of the genes Nanog and Oct4. The power of this work is in the rigorous and elegant theoretical formulation of the problem of inferring burst parameters in cycling cells, and the clear description of the algorithm for extracting these parameters. I believe the methodology developed here will be instrumental to many future works related to gene expression variability in the context of the cell cycle.

The paper could be improved by addressing, at least in the text, the following points:

1) The authors should elaborate on the comparison between their results and those of Raj and colleagues (Padovan-Merhar et al., 2015). Specifically in the Padovan-Merhar paper a dosage compensation very similar to the one identified here was detected (decreased "burst frequency" upon replication), however, upon growth of cellular volume (occurring predominantly at G2) there was a global increase in number of nascent mRNA per transcription site (compensatory increase in "burst size"). The present study did not identify a difference in the burst size between G1 and G2. These discrepancies between the two works could be related to the differences in the cell lines and genes studied (specifically the shorter cell cycle time of ES cells compared to fibroblasts).

2) The deterministic model of nascent and mature mRNA kinetics (section 9) and the associated Figure 3—figure supplement 1 nicely demonstrate that the mature mRNA is not at steady state. More importantly, it shows that the mature mRNA in G2 is less than twice the levels in G1(as also shown in Figure 3C). This would mean that upon division the levels of mature mRNA at the start of G1 phase of the next round would be smaller than in the current round, and that mRNA will exponentially decline to zero with additional cycles. This naturally cannot be the case and there must be some compensatory dosage compensation somewhere along the cell cycle. While identifying this additional dosage compensation mechanism is beyond the scope of the current work it is important to note this issue in the text.

3) Section 6.1 “Quantification of DNA content”: the authors should provide the cell cycle periods for the ES cells studied, inferred by their cell cycle phase inference algorithm.

4) The authors consider a change in Kon upon replication, rather than Koff. One could imagine the dosage compensation would entail higher Koff rather than lower Kon. Would there be a potential identifiability problem in discerning between models that allow changes in both Kon and Koff?

5) The model applied assumes fixed times of replication and division, how would results change if these parameters were allowed to vary (that is if they were sampled from some normal distribution)?

6) "The number of nascent mRNA at each active transcription site was quantified in the exon-channel by dividing the integrated intensity by the integrated intensity of a single-mRNA molecule (Materials and methods 5.1)". This approach may introduce some bias that depends on the probe library design. If all probes target the first part of the gene then any RNA polymerase will have a nascent mRNA attached to it that includes the full complement of probes and thus has intensity equal to a full mature mRNA. If, however, probes are equally spread along the gene, the average RNA polymerase will have an mRNA with half of the library probes yielding a 'dimmer' dot. Correction for this effect is described in Bahar Halpern et al. 2015 and is worth considering.

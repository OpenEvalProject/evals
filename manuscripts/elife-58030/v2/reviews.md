# Peer review - Round 1

Editors:
- Christine Clayton, DKFZ-ZMBH Alliance Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58030.sa1](https://doi.org/10.7554/eLife.58030.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Previously, by counting marker copy numbers, only a single putative origin of replication had been found for each Leishmania chromosome. The problem with this conclusion is that there might not be time to replicate the longer chromosomes. In this paper, the authors confirm that acetylated histone H3 (AcH3), base J and a kinetochore factor co-localise at these previously-mapped loci, which also show G/T skew and G4 patterns. However, they also find indications of additional DNA synthesis that is less strongly cell-cycle regulated, and initiates near the telomeres in regions marked only by AcH3. This may explain how replication of the longer chromosomes can be completed.

Decision letter after peer review:

Thank you for submitting your article "Genome duplication in Leishmaniamajor relies on unconventional subtelomeric DNA replication" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Christine Clayton as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Dominique Soldati-Favre as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Peter Myler (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript includes novel insights into genome replication in Leishmania, which suggest various initiation zones are present. The authors performed deep-sequencing analyses of cells sorted by DNA content in different phases of the cell cycle and normalized the read-depth with that obtained from cells stalled at the stationary phase. This unveiled a replication initiation zone close to the telomeres that is more prominent during the G1 and G2 phases of the cell cycle. This initiation zone is altered in replicative stress conditions, what make it distinct to the early S centromere-proximal initiation zone they have previously identified.

Essential revisions:

The reviewers agreed that the results were interesting and that no further experiments are needed, and the Leishmania expert said that the manuscript is clearly written, although densely packed at times. However, the two experts on the method agreed that the use of Z-scores was misleading and that you over-interpret the data. It is therefore essential that you follow their recommendations and re-analyse your data without using Z-scores.

Condensed version of their conclusions:

The authors considered two other papers reporting multiple replication initiation sites per chromosome, suggesting that either the SNS technique picks up every initiation site although very infrequent or that the fiber stretching technique is measuring the replication at the kinetoplast circles. However, the MFA is likely measuring replication timing, not replication initiation sites, which would be compatible with the above mentioned works. The alternate possibility is that replication in Leishmania starts from multiple inefficient origins that are activated in clusters; one centromere-proximal and another telomere-proximal. The fact that the authors use Z-scores to analyse their MFA data masks non-clustered initiation sites, leading them to interpret their findings of an early initiation zone as an unique early initiation site. Reanalysing the data and moderating their claims will still make their finding of the telomeric-proximal initiation zone interesting for better understanding the biology of these organisms.

Reviewer 3: Lombrana et al., 2016 and Stanojcic et al., 2016, using more precise origin identification methods (Short Nascent Strand analysis and DNA combing) provided strong evidence that origins are much more frequent than this (origin spacing ~180 kb). Although each method of origin mapping has its limitations, marker frequency analysis is relatively imprecise in its ability to map individual origins, and is better suited to analysis of replication timing. It therefore cannot be right for the current paper to ignore the very plausible data obtained by other techniques. This reviewer thus feels that you cannot conclude, from the single MFA-seq peak, that "the majority of DNA replication initiates from a single locus."

Detail from reviewer 2:

1) My main question is about the usage of MFA Z-scores for all the subsequent analysis. I understand that Z-scores are needed when comparing between different strains. Why applying Z-scores when analyzing DNA amounts in cell cycle sorted cells? Normalizing the read depths relative to those of stationary cells would be good enough if the same strain is used; aneuploidies will be corrected and the resolution will be higher, potentially allowing better comparisons with the more sensitive SNS-seq technique, as the authors argue in the Introduction and show in Figure 1—figure supplement 3Ci-ii. Besides, Z-scores magnify relative enrichments what could lead to information loss and to a different interpretation of the data. I would suggest the authors to reanalyze their MFA data without using Z-scores. It might well be that by doing this a different picture will emerge, like DNA replication initiating in two main zones in Leishmania chromosomes: one centromere-proximal and another telomere-proximal, but not necessarily from a single origin site in either case.

2) Building on that, looking at the raw data presented in Figure 1—figure supplement 3A it seems that the increased chromosome-central read density is already observed in STA cells (similarly to EXP cells). What happen if STA data are represented as Z-scores in Figure 1—figure supplement 3B? Would the authors interpreted that as DNA replication of some non-stalled cells in the STA population? Or could that be due to other reasons, like amplification of the centromeric regions? Although likely out of the scope of the current work, an important control for all MFA experiments would have been to perform EdU-IP in sorted cells and test if they get similar observations using nascent DNA.

3) Figure 1—figure supplement 3Ci and Cii data suggest to me a replication timing program starting from chromosome ends in G1 and from a centromere-proximal zone in early S, that merge and it is completed in late-S and G2. Could this be related to the transcriptional wave along the cell cycle? If there are not data available on this, at least the authors should comment that possibility in the Discussion. Similarly, such a replication timing scenario could be compatible with a 3D genome architecture in which centromeres and/or telomeres are tethered together in 3D as seen in other unicellular parasites (Bunnik et al., 2019). Replication would initiate from those clustered chromosomal points and then extended to the rest of the genome. This interpretation will be consistent with shorter chromosomes replicating earlier in S-phase (Figure 2). The authors also should discuss this possibility.

4) In conditions of replicative stress or RAD9 deficiency, the authors nicely show that the most telomere-proximal signals are reduced, but more interior ones are not altered or even increased. How do the authors interpret this? These data would fit with the above 3D architecture, where replication origins are activated from telomere-ends even in conditions in which the very distal initiation sites (that might be replicated in a different fashion) are not activated.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for re-submitting your article "Genome duplication in Leishmaniamajor relies on unconventional subtelomeric DNA replication" for consideration by eLife. Your article has been re-reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Dominique Soldati-Favre as the Senior Editor. The reviewers have opted to remain anonymous.

In conclusion: The data are interesting but neither expert is convinced by your interpretation. It is therefore absolutely essential that you tone down the claims. In particular, please remove the claim that there is a "single origin", neither reviewer thinks that the data support it. The claims about "unconventional replication" or "non-origin directed replication" must also be removed from their title and Abstract. It is possible that there is a strong origin region, and multiple less strong origins in other regions – but they are still origins. It is also important to try a bit more to reconcile your data with the fibre data. I've included the reviews verbatim because I think the detailed arguments are important.

Reviewer #2:

The authors have answered my main concern by presenting the MFA data as read-depth rations instead of Z-scores. As they point out, the overall interpretation of the data is not profoundly altered relative to the previous version of the manuscript. On the contrary, the use of read-depth ratios makes clearer that the resolution of the MFA technique is too low to ascribe the mid-chromosomal initiation zone as a single initiation site and, therefore, to further build their claims on the unique G4 patterns and GC-skew at the center of these large early replicating regions as a footprint of replication origins. So, I insist that they should moderate the tone even further on this before publication. Still, I consider the manuscript, and their novel finding of very early subtelomeric replication, of interest for better understanding kinetoplastids biology and support publication in eLife. I recommend the authors again to be cautious when interpreting subtelomeric DNA replication as not origin-directed or unconventional. As they also point out in their response to the reviewer's comments, there are no evidences so far on ORC-binding at Leishmania chromosomes, so we still don’t know how replication origins are specified in this organism.

Reviewer #3:

I still find the way the results are interpreted quite misleading. Marker Frequency Analysis (MFA) is not a reliable technique for mapping replication origins, though it can reveal the replication timing programme by which different regions of the genome are replicated at different stages of S phase. The results are interpreted as though MFA is giving reliable information about individual origins, and that there is only a single origin driving the bulk of DNA synthesis, which I believe goes against both experimental data (the more reliable fibre analysis) and theoretical considerations of the number of origins required for reliable completion of replication. I would note that base composition bias, although providing some evidence that initiation occurs in a region, is poor evidence that only a single origin is used, and instead is only consistent with most DNA replication being bidirectional around this site.

For example:

“…whereas a single putative origin in each L. major chromosome is activated early in S-phase, predicted subtelomeric DNA replication can be detected in all enriched stages of the L. major cell cycle.”

“These data are consistent with bidirectional progression of replication forks from a single putative origin in each chromosome”

– “These data may be explained by DNA replication in L. major following a programme in which synthesis of a new chromosome initiates at a defined locus in the interior of each chromosome…”

“Since a single major MFA-seq peak was seen in each chromosome in ES cells, the majority of DNA replication is predicted to initiate from a single locus in each case.”

“These data suggest that the simultaneous presence of these three genome factors is a local driver for coordinated DNA replication initiation at a single locus in each chromosome…”

“These data provide clear evidence for base composition bias, consistent with DNA replication initiation, at a single central locus in each of the 36 L. major chromosomes.”

“…but their relationship with DNA replication initiation sites mapped by MFA-seq…”

The authors suggest that DNA replication is occurring at cell cycle stages other than S phase, but this runs the danger of being rather circular: how would they define G1 and G2 if not by a lack of DNA synthesis?

The Abstract introduces the concept that telomeric DNA is replicated in a way that is distinct from “origin-directed replication”. I don't understand what this means, and isn't clear to me how this relates to the experimental results and how they are interpreted in the Discussion.

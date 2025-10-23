# Peer review - Round 1

Editors:
- Guangxia Gao, Institute of Biophysics, Chinese Academy of Sciences China

Reviewers:
- Nara Lee

## Review text

DOI: [10.7554/eLife.47261.056](https://doi.org/10.7554/eLife.47261.056)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The Tudor SND1 protein is a m6A RNA reader essential for KSHV replication" for consideration by eLife. Your article has been reviewed by Päivi Ojala as the Senior Editor, a Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Nara Lee (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting investigation into the landscape of m6A modification of KSHV transcripts and the readers of the modified RNAs. Seven members of the "Royal family" of TUDOR domain containing proteins were identified as new putative m6A readers, including SND1. SND1 associates with the KSHV ORF50 transcript in a manner dependent on the m6A modification and SND1 depletion leads to a global impairment of KSHV gene expression. Identification of members of the 'Royal family' as new m6A-readers greatly increases their epigenetic functions beyond protein methylation.

Essential revisions:

1) Reviewers 1 and 3 suggested the authors to map the SND1 binding sites by CLIP-seq rather than RNA-IP.

2) Reviewer 2 suggested the authors to perform a ChIP-seq analysis of the viral genome to exclude the possibility that SND1 binds and activates the ORF50 promoter.

The full reviews are listed below, in the hope that the comments can help to improve the quality of the paper.

Reviewer #1:

More evidence is needed to improve the quality of the manuscript.

Essential revisions:

1) I have several concerns for the gel shift assay and the data interpretation:

(A) The components of the 1x binding buffer of the gel shift assay (subsection “Electrophoretic mobility shift assays (EMSAs)”) looked different from that is stated in the manual of the LightShift Chemiluminescent EMSA Kit from ThermoScientific in terms of salt concentrations. This could affect the secondary structure of the probes used in the assay. Also, it is not clear whether the authors used non-specific Poly (dI•dC) as instructed by the kit. Considering the function of SND1 as a transcriptional factor, does the presence of non-specific DNA affect the RNA binding of SND1 in gel shift assay?

(B) In Figure 2, Figure 3—figure supplement 6 and Figure 3—figure supplement 7, the biotin signals from the probe were always overwhelming compared to the shifted probes, making it hard to calculate the ratio of free probe to bound probe and estimate the binding affinity (Kd). Why is this the case? Any way to optimize the imaging condition? Maybe fluorescent dye labelled probe could help.

2) The authors saved the input sample of the RIP-seq saved before crosslinking the cells. Normally people process the input and RIP samples in parallel until before IP. The authors claimed the reason is that the sonicated input gave lower quality sequencing libraries maybe due to overshearing (subsection “RIP-seq”). I still believe that the input sample should be saved after sonication, otherwise it is hard to estimate artifacts introduced by the sonication step. And "overshearing" itself may already be a concern for high-quality RIP assays. Instead of "formaldehyde-crosslinked RIP-seq", the authors may consider performing "CLIP-seq" as a validation which also gives high-resolution binding sites of protein on RNA based on crosslinking-induced mutations in cDNA libraries.

3) "SND1 binds symmetrically demethylated arginines (sDMA)" via its Tudor domain, as described on subsection “RNA affinity identifies putative m6A readers which belong to the Tudor domain ‘Royal family’”. I am wondering if the authors have tested affinity of the protein towards N6, N6-dimethyladenosine. It may worth checking if known ribosomal RNA N6, N6-dimethyladenosine sites were enriched in their SND1 RIP-seq data.

Reviewer #2:

The authors cannot demonstrate the final consequences of SND1 binding to the ORF50 RNA. Here the manuscript reveals conceptual deficits. Also, the work of another laboratory with similar findings is not discussed sufficiently.

Essential revisions:

1) Abstract: The authors provide interesting structural data, but the claim that all identified proteins recognize m6A in a structural-dependent manner is an overstatement (see also below). To verify this more mutants are necessary. The critical claim of the manuscript is that SND1 stabilizes the ORF50 RNA. However, the single data figure given in Figure 6 does not clarify this point (see below). The following sentence mentions a global impairment of KSHV gene expression, which is no surprise if the master switch of reactivation is blocked. This claim has to be toned down to "inhibits KSHV early gene expression".

2) Subsection “Royal domains bind m6A-modified RNA hairpins in a RNA secondary structure-dependent manner”, Figure 2, Figure 3—figure supplement 4 and Figure 3—figure supplement 4: First, these data nicely show that SND1 binds the ORF50-1 sequence. However, the interpretation of the cORF50-1 shortened stem and the sORF50-1 mutant is not straightforward. To state "in structural-dependent manner" the authors need to increase the stability of the stem by erasing the bulges only. Also, the cORF50-1 sequence may be just too short to form the correct stem. The authors should extend the stem of cORF50-1 mutant by unrelated bases to provide more insights on the structural features needed by SND1.

3) Subsection “SND1 is a m6A reader in KSHV-infected cells”, Figure 3: The authors should compare their obtained m6A frequency in the high-confidence SND1 targets to ratios available for other m6A reader proteins such as the YTHDF family members. Is there a similar correlation or do these readers contains even more m6A modified target sequences in their high-confidence interval? These data should be available from public resources.

4) Subsection “SND1 is a m6A reader in KSHV-infected cells”: how SND1 recognizes its RNA target sequences is pure speculation and should be removed from the result section. In addition, the motif provided in Figure 4—figure supplement 3D looks like 3' splice site and may argue for SND1's role in splicing.

5) Subsection “SND1 stabilises ORF50 RNA and is essential for KSHV replication” and Figure 5: The authors provide an interesting discrepancy between the TREx BCBL-1 cells and naturally infected BCBL-1 cells. Their argument reads as follows: in naturally, unmodified BCBL-1 cells, the ORF50 RNA is decreased during SND1 knockdown. This effect is masked in the TREx BCBL-1 cells since they contain a chromosomally integrated doxycycline-inducible ORF50 gene. However, the authors fail short in the interpretation of their results. An alternative explanation would be that the DNA-binding and promoter-modifying capacity of SND1 comes into play. The major difference between the two ORF50 versions is the nature of the promoter driving their expression. The dox version harbors 6 to 7 tetracyclin-operators and a minimal CMV promoter. In the virus the ORF50 promoter is the sensor of the cellular status and is highly regulated to induced lytic reactivation only under certain conditions. To clarify the role of SND1 the authors need to perform a ChIP-seq analysis of the viral genome to exclude the possibility that SND1 binds and activates the ORF50 promoter. Thus, a lack of SND1 may cause an inhibition of ORF50 transcription and may explain all downstream effects. If this is the case the derived claims such as "SND1 stabilizes the ORF50 transcript" may not be corrected. In addition, the impairment of viral lytic gene expression could also be explained in a similar manner. The authors themselves mention this possibility indirectly in the Discussion section stating that SND1 functions as co-activator of the EBV protein EBNA-2.

6) Figure 5D and G: The authors should include lytic markers such as K8.1 and ORF59.

7) Figure 6B: Here, the authors need to provide the raw data. In addition, to an accelerated decay the SND1 knockdown may already reduce the amount ORF50 transcript. See also argument provided above. Also, the authors should distinguish between the decay of spliced vs. unspliced ORF50 RNA if possible.

8) Supplementary Figure S11: I agree with the authors that a METTL3 knockdown might be difficult in BCBL-1 cells. Even though the increase in ORF50 RNA is not significant I am wondering if the authors here observe the same effect as the Glaunsinger laboratory (Hesser et al., 2018). These authors were able to reduce the amount of METTL3 in BCBL-1 cells sufficiently and observed an increase in ORF50 protein, but not RNA. These findings are not discussed in the current manuscript! If METTL3 knockdown is too difficult, the authors should use the DAA treatment presented in Figure 6C,D to assess ORF50 RNA levels in the absence of m6A modifications.

Reviewer #3:

The most exciting part of this manuscript is the identification of novel m6A reader proteins, which were originally thought to bind methylated proteins only. While I am convinced of the specificity of SND1 towards m6A, my main criticism is directed towards the authors' choice of experimental approach to map SND1 binding sites on RNA. As detailed below, RNA-IP in this particular instance appears inappropriate to locate SND1 binding sites.

Essential revisions:

While different experimental approaches can be applied to identify RNA-protein interactions, such as RNA-IP or CLIP-based techniques, in the case of SND1 the use of RNA-IP appears inappropriate. As mentioned in subsection “SND1 is a m6A reader in KSHV-infected cells” and shown in Figure 4—figure supplement 1, the vast majority of RNA fragments was sheared to <200 nt (not "bp"), yet the enriched fragments were of considerably greater size, which the authors suggest may be due to the anti-SND1 antibody having higher affinity for longer fragments. This statement is not very plausible. On the other hand, given the affinity of SND1 for methylated arginines, it is possible that chromatin-associated nascent RNAs were indirectly precipitated through SND1 binding to other chromatin-associated factors (e.g. histones or spliceosomal proteins). These complexed RNAs would greatly resist shearing by sonication as compared to free RNAs. According to Materials and methods section, no DNase treatment was included prior to IP and hence indirect RNA IP cannot be excluded. While bona fide SND1 targets may certainly be present within the deep sequenced RNAs, this cohort may be largely polluted by non-specific transcripts.

Rather than RNA-IP, eCLIP or iCLIP would have the advantage that the crosslinked sites can be identified unambiguously, which would be particularly useful in overlapping m6A sites on RNA with SND1 binding sites.

# Peer review - Round 1

Editors:
- Ivan P Moskowitz, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56697.sa1](https://doi.org/10.7554/eLife.56697.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript presents an integrated approach for investigating genetic variation identified by GWAS, traveling from human genetics through informatics and genomic analysis to validation in a mouse model. This approach may be broadly applicable. Equally interesting are the specific findings concerning gene regulation at the TBX3 locus, including the identification of several enhancers, at least one of which is shown to be required in vivo.

Decision letter after peer review:

Thank you for submitting your article "Trait-associated noncoding variant regions affect TBX3 regulation and cardiac conduction" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ivan P Moskowitz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Didier Stainier as the Senior Editor The following individual involved in review of your submission has agreed to reveal their identity: Tony Firulli (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Hendrik van Weerd et. al is a very good manuscript detailing a functional genomics approach to understanding regulation of the TBX3 gene and investigating GWAS variants for cardiac rhythm traits at the TBX3 locus. The paper includes an interrogation of common non-coding genomic variants upstream and in cis with the T-box transcription factor TBX3 associated with changes in cardiac conduction velocity.

The paper excels in several ways. First, it provides a comprehensive approach to travel from trait-associated variants to functional investigation of the gene regulatory consequences of specific variants, attempting to link them to phenotypic consequences. Second, it advances our understanding of the cis-regulatory landscape at TBX3 and reveals a likely molecular mechanism for GWAS signals at the TBX3 locus – specifically, variation of cis-regulatory element function affecting TBX3 expression in conduction tissues. Third, it considers and tackles some basic difficulties in understanding cardiac conduction system GWAS – the lack of human expression data for cardiac conduction tissues and therefore the lack of eQTL data for such tissues implicated in cardiac rhythm control. The mouse – human pipeline presented provides a potential roadmap for future studies in the CCS or in other tissues that lack human expression data.

Revisions:

The specific comments are meant to clarify the manuscript. The generation of new data is not necessary for the revision. The following issues should to be clarified in a revision manuscript, either by analysis of current data or by clarification of the text and/or figures:

1) In-vivo functional analysis is not of SNPs themselves but of a much larger enhancer deletion. This caveat should be discussed with regards to the molecular mechanism underlying the GWAS association caused by SNPs.

2) Some of the observed molecular and functional effects of SNPs or enhancer knockouts are unexpected and are left without a mechanistic explanation. For example, analysis of the in-vivo effects of removal of VR2 generated results for Tbx3 expression and for functional conduction measures that are opposite of expectations. Tbx3, a repressor of fast conduction channels, was upregulated in conduction tissues, generating the expectation that conduction would be slowed in affected regions. However, a decreased PR interval, indicative of more rapid conduction speed, was observed. Can the authors explain why this is the case? At the very least the authors should discuss the unexpected nature of this observation and offer a plausible explanation.

3) The Motif data presented in a few of the figures may not be accurate. It is clear that the VR2 is functional and published DNA occupancy data shows associated DNA binding from defined TFs within the RE's; however, the sequence consensus shown for the bHLH factors (sans MyoD) do not contain E-boxes, SOX9 and SMAD Motifs reported also appear non-canonical. Discussing this at some level is warranted.

4) ATAC-seq was performed in embryonic hearts and traits were from adult humans. This comparison may underestimate the overlap were ATAC to be done on adult AVC cells. This caveat should be discussed.

5) The authors interrogated the human TBX3 locus for TAD structure and the location of SNPs associated with conduction traits; they identified candidate REs in the AVC by performing AVC ATAC-seq, which should provide an excellent resource for the field.

How were the 67 candidate REs at the Tbx3 locus defined relative to the entire dataset?

How specific are the identified elements for the AVC as opposed to non-AVC myocardium?

The authors show but do not discuss the comparison between the AVC versus ventricular ATAC across the Tbx3 locus. How many are AVC-specific? It looks like many are shared.

Did the author's attempt a differential ATAC analysis across the locus?

6) The STARR analysis was performed in COS cells to identify regions that activate transcription based on specific TFs previously defined as important for AVC gene expression. As the authors indicate, there is no AVC cell line, requiring use of an unrelated line. None-the-less, the use of COS cells is a significant caveat, and should be discussed clearly in the Discussion. The TF enrichment in this context is a therefore a self-fulfilling prophecy.

The number of human and mouse STARR identified candidates, as well as their overlap, should be described up front.

7) The description of mouse/human homology for VR1 and VR2 should be described in more detail.

8) RE candidate selection is described in Fg3a using a hierarchical approach in schematic form.

It should be possible to use the actual locus, display the individual datasets, and overlay them to present a more accurate description of the chosen REs at the locus.

Figure 3B appears to display data already published. Were any other candidates tested in-vivo?

9) Several of the candidate risk alleles, examined in luciferase activity in Figure 4C and d, show discordant effects on basal activity and TF-stimulated activity. This should be described and considered. Do the variants alter TF binding sites of known activator or repressor TFs that would help explain this discordance? Do any of the analyzed variants alter TF binding sites of the TF analyzed, which may explain their altered regulatory response to TF expression?

10) In Figure 6, the schematic shows the location of the TALEN cuts. The authors should delineate VR1 and VR2, as in Figure 5.

11) Figure 1C do the authors have insight as to why the Motif consensus for HAND2, TCF3, and TCF4 do not contain a clear E-box motif such as shown for MyoD? The SOX9 Motif also seems out of place with the canonical consensus: CCTTGAG. SMAD 3&4 likewise are reported to bind CAGAC, CAGCC as well as the 5-bp consensus sequence GGC(GC)|(CG). What is shown in the motif is very different and some discussion of this is warranted there is not confidence that the aforementioned transcription factors would bind these sequences robustly. There is simply low confidence that the algorithm is pulling accurate motif data and the authors should try to address this in the text.

12) Figure 2 same issue with consensus data in 2G (note the motif name and the motif do not line up correctly).

13) Figure 3 some clarity in the narration would be helpful. Paragraph one of subsection “Identification of variant REs within VR1 and VR2” discuss 9 candidate REs in VR1 and 13 in VR2. Are these regions supposed to be identifiable in Figure 3A (as is the assumption)? The figure shows 6 candidate REs which resolve to 3 with SNP overlaps comparing the figure to the narration is confusing.

14) Figure 6C shows only Tbx3 expression Tbx5 and Med13l expression narrated as being in Figure 6C. Panel G would benefit from slightly enlarged images.

15) The criteria and datasets used to define the EMERGE regions is not found in this paper nor is there any citation listing where these regions came from. Please clarify.

16) What was the criteria used to identify the 9 and 13 (as listed in the text) candidate regulatory elements in VR1/2? Supplementary Table 4 lists only 20 candidate regulatory elements (7 and 13). What happened to hRE1 and hRE2 to exclude them from downstream analysis and inclusion in the table? Were other sites excluded as well? It is also unclear from Figures 2H-K and Figure 3A, and Supplementary Tables 3 and 4 what was used to define the candidate regulatory elements examined in greater detail in Figures 4, Figure 3—figure supplement 1 and Figure 4—figure supplement 1. For example, hRE13 was not examined in Figures 4C/D or Figure 4—figure supplement 1. Overall, I really like the multi-factor approach to defining candidates; however, the key filtering steps taken to get the final list of candidates needs to be more clearly defined.

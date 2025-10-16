# Peer review - Round 1

Editors:
- Michael R Green, Howard Hughes Medical Institute, University of Massachusetts Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19272.030](https://doi.org/10.7554/eLife.19272.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Combinatorial bZIP dimers define complex DNA-binding specificity landscapes" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Michael Green who is a member of our Board of Reviewing Editors, and Kevin Struhl (who is not responsible for the references to previous work in the reviews) as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting manuscript on the DNA binding specificity of dimers in the human bZIP family. bZIP proteins are known to play critical regulatory roles in many cellular processes, and different members of this family are known to form both homo- and heterodimers (sometimes with more than one partner). Prior to the work described in this manuscript, it was unclear how dimerization influences DNA specificity. The authors used SELEX-seq experiments to characterize the binding specificities of 80 heterodimers and 22 homodimers, and used proper control experiments to ensure that the data is interpreted correctly (e.g. they tested that the choice of which bZIP monomer is biotinylated does not affect results).

This rich data set has the potential to change the way we analyze genomic binding of bZIP proteins, especially in terms of assessing the potential impact of SNPs on bZIP-DNA binding. However, in its current form, the manuscript is not ready for publication. Several sections are unclear and hard to read, and there are many incorrect references to figures or supplementary material. Please see specific comments and questions below.

Essential revisions:

1) The identification of "emergent sites" for some bZIP dimers is one of the major insights gained from the authors' large compendium of bZIP specificities. According to the authors, such sites cannot be predicted from the specificities of the homodimers. However, the section presenting this result, "Conjoined, Variably-spaced and Emergent cognate sites bound by heterodimers" is very hard to read.

The supplementary files are not numbered correctly: "[…] the homodimer DNA specificity (e.g., ATF4 vs. ATF4•CEBPA, r = 0.1; Figure 1—figure supplement 3)." I could not find this figure.

In Figure 1C, please annotate in the figure itself which motifs are "conjoined" vs. "variably-spaced" vs. "emergent". Arranging the motifs into these categories would make the manuscript easier to follow. For the motifs that are compared to one another, the authors should display them together and aligned them. Otherwise it is very hard to follow what the authors are trying to convey (see subsection “Conjoined, Variably-spaced and Emergent cognate sites bound by heterodimers” paragraph two). A direct comparison of FOS-CABPG and FOS-CABPE should be shown in a figure.

Related to the same paragraph and Figure 1, it is interesting that BATF3 as a homodimer binds TGACGTCA, but as heterodimers with CEBPA, ATF3, ATF5, and NFIL3, BATF proteins bind GTGG (a CRE-L half-site). Could it be that as homodimers BATF proteins can bind both CRE and CRE-L sites, but these two different sites cannot be captured by a single motif? Certain bZIP subfamilies have been known for many years to bind more than 1 type of motif. For example, see early work from Kevin Struhl's lab on Ap-1 versus ATF/CREB bZIP domains: Ap-1 proteins recognize overlapping TGAC half-sites TGA(C|G)TCA, while ATF/CREB proteins recognize adjacent half-sites TGACGTCA; however, "AP-1 proteins prefer to bind AP-1 sites, but they also bind ATF/CREB sites with only slightly lower affinity" (PMID: 7630732). Given that the authors use single motifs to represent the specificity of homo and heterodimers, such preferences for more than one arrangement of half-sites is not illustrated in the paper.

2) From the manuscript it seems clear that if we take only the top motif for each dimer, then "emergent" motifs cannot be predicted from the motifs of the individual homodimers. But if for each homodimer we consider all the motifs they recognize (sometimes with different affinities, other times with very similar affinity), can we then predict some of the "emergent" motifs?

On a related note: The authors mention that "Nine out of the 80 heterodimers (11%) enriched two motifs (Supplementary file 2). For example, BATF•CEBPG enriched both CRE-CAAT and CRE-L-CAAT motifs." But what about homodimers? Some homodimers might also bind two motifs.

The authors tried to address this issue by using "specificity and energy landscapes" (SEL). While I understand that these landscapes contain a lot more information than the motifs, they are not intuitive to interpret and it is not clear to me how one would immediately extract information about multiple half-site arrangements from SELs. A much simpler representation would be by using several motifs for each homo/hetero-dimer that binds more than 1 half-site arrangement.

3) Comparing SELs is also difficult. When two dimers have a site in common, how can we see that from the SELs? Unless the seed is exactly the same, the SELs are hard to compare.

The authors interpret some SELs in subsection “Specificity and Energy Landscapes (SELs) reveal the entire spectrum of cognate sites bound by heterodimers”, but couldn't the same insights be gained by simply deriving more than 1 motif from each data set?

Maybe one possibility for presenting the data is to generate a set of motifs representing all the half-site combinations observed in the data, and then for each dimer plot its affinities for sites matching each motif.

4) Few studies of heterodimers binding to DNA carefully dissect the binding of hetero- versus homodimers. The authors did this using EMSA-FRET assays, and for a large number of heterodimers (67).

Although this data is very valuable, the way it is presented is not clear – see Figure 3 and associated text. I would recommend using a single color for PPIs, and a single color for PDIs (with intensity proportional to affinity of the interactions). Or even have separate plots for PPIs versus PDIs. Alternatively, the authors could show the data as barplots with PDI strength above the x-axis (i.e. as positive numbers) and PPIs underneath the x-axis (i.e. as negative numbers). Another option would be to use circles where the size reflects PDI strength and the color intensity reflects PDI strength. In subsection “EMSA-FRET analysis to validate heterodimer binding to different cognate sites” the authors say: "It is readily evident that neither the JUN nor the ATF3 homodimers associate with the emergent site identified by SELs for JUN•ATF3 (Figure 3C and Figure 3—figure supplement 1)." To this reviewer it was not evident, and it took quite a lot of time to extract this information from SELs and the figures in the manuscript.

5) The case study of ATF3's specificity being influenced by partner TFs is clear and interesting.

6) Regarding the in vivo ATF3 analysis: the authors found that the motifs of different ATF3 dimes are best at explaining the ATF3 ChIP-seq data in different cell lines. Did the authors verify that the partners identified by their analysis are actually expressed, at high enough levels, in those cell lines?

Also, are the reported differences in AUC-ROC values between different motifs (Figure 5B) significant? What is the magnitude of differences observed for motifs trained on replicate SELEX-seq experiments? The AUC-ROC values are generally not robust to small changes in the motifs. The analysis shown in Figure 5C-D, based on the SELEX-seq data, better reflects the cell-type specific differences in ATF3 heterodimer binding.

7) The analysis in the last section of Results (Figure 7) is very interesting. However, the "noise factor" used in the analyses of SNP data seems ad-hoc. What is the rationale for the formula used to calculate the noise factor?

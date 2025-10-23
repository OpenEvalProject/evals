# Peer review - Round 1

Editors:
- John Calarco, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97682.3.sa0](https://doi.org/10.7554/eLife.97682.3.sa0)

This valuable study combines massively parallel reporter assays and regression analysis to identify sequence features in untranslated regions contributing to the stability of in vitro transcribed mRNA delivered to cells. The strength of evidence presented is solid, although some points about half-life measurements and the relevance of identified sequence features to native transcript stability will inform future discussion surrounding the present study. Taken together, the work will be of interest to a broad swath of colleagues studying post-transcriptional gene regulation and especially to those using massively parallel reporter assays.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97682.3.sa1](https://doi.org/10.7554/eLife.97682.3.sa1)

In the manuscript by Su et al., the authors present a massively parallel reporter assay (MPRA) measuring the stability of in vitro transcribed mRNAs carrying wild-type or mutant 5' or 3' UTRs transfected into two different human cell lines. The goal presented at the beginning of the manuscript was to screen for effects of disease-associated point mutations on the stability of the reporter RNAs carrying partial human 5' or 3' UTRs. However, the majority of the manuscript is dedicated to identifying sequence components underlying the differential stability of reporter constructs. This analysis showed that UA dinucleotides are the most predictive feature of RNA stability in both cell lines and both UTRs.

The effect of AU rich elements (AREs) on RNA stability is well established in multiple systems, and the present study confirms this general trend, but points out variability in the consequence of seemingly similar motifs on RNA stability. For example, the authors report that a long stretch of Us has extreme opposite effects on RNA stability depending on whether it is preceded by an A (strongly destabilizing) or followed by an A (strongly stabilizing). While the authors interpretation of a context-dependence of the effect is certainly well-founded, it seems counterintuitive that the preceding or following A would be the (only) determining factor. This points to a generally reductionist approach taken by the authors in the analysis of the data and in their attempt to dissect the contribution of "AU rich sequences" to RNA stability, with a general tendency to reduce the size and complexity of the features (e.g. to dinucleotides). While this certainly increases the statistical power of the analysis due to the number of occurrences of these motifs, it limits the interpretability of the results. How do UA dinucleotides per se contribute to destabilizing the RNA, both in 5' and 3' UTRs, but (according to limited data presented) not in coding sequences? What is the mechanism? RBPs binding to UA dinucleotide containing sequences are suggested to "mask" the destabilizing effect, thereby leading to a more stable RNA. Gain of UA dinucleotides is reported to have a destabilizing effect, but again no hypothesis is provided as to the underlying molecular mechanism. In addition to reducing the motif length to dinucleotides, the notion of "context dependence" is used in a very narrow sense.

The present MPRA measures the effect of UTR sequences in one specific reporter context and using one experimental approach (following the decay of in vitro transcribed and transfected RNAs). While this method certainly has its merits compared to other approaches, it also comes with some caveats: RNA is delivered naked, without bound RBPs and no nuclear history, e.g. of splicing (no EJCs), editing and modifications. Therefore, it remains to be seen whether UA dinucleotide frequency is a substantial factor in determining the half-lives of endogenous mRNAs.

The authors conclude their study with a meta-analysis of genes with increased UA dinucleotides in 5' and 3'UTRs, showing that specific functional groups are overrepresented among these genes. In addition, they provide evidence for an effect of disease-associated UTR mutations on endogenous RNA stability. While these elements link back to the original motivation of the study (screening for effects of point mutations in 5' and 3' UTRs), they provide only a limited amount of additional insights.

In summary, this manuscript presents an interesting addition to the long-standing attempts at dissecting the sequence basis of RNA stability in human cells. The analysis is in general comprehensive and sound; however, it remains unclear to what extent the findings can be generalized beyond the method and the experimental system used here.

Comments on revisions:

Parts of my original comments have been adequately addressed by the reviewers.

After reading the revised manuscript and the rebuttal, my main concern is related to the figure comparing the half-lives as measured in the two different cell lines that was included in the response to reviewer 2, but not in the revised manuscript. The complete lack of correlation between the half-lives of the 3'UTR library measured in the two cell lines is concerning. While variability and cell type-specific effects can be expected, some principles should be the same (such as the effect of UA dinucleotides that the authors report), leading to at least some correlation.

In addition, it is unclear to me why the half-lives measured for the two libraries in HEK cells are shifted (median ln(t 1/2)=6-7 for the 5'UTR library and ln(t 1/2)=4-4.5 for the 3'UTR library), but not in SH.

I feel that this figure contains important information that should be included in the final manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97682.3.sa2](https://doi.org/10.7554/eLife.97682.3.sa2)

Summary of goals:

Untranslated regions are key cis-regulatory elements that control mRNA stability, translation, and translocation. Through interactions with small RNAs and RNA binding proteins, UTRs form complex transcriptional circuitry that allows cells to fine-tune gene expression. Functional annotation of UTR variants has been very limited, and improvements could offer insights into disease relevant regulatory mechanisms. The goals were to advance our understanding of the determinants of UTR regulatory elements and characterize the effects of a set of "disease-relevant" UTR variants.

Strengths:

The use of a massively parallel reporter assay allowed for analysis of a substantial set (6,555 pairs) of 5' and 3' UTR fragments compiled from known disease associated variants. Two cell types were used.

The findings confirm previous work about the importance of AREs, which helps show validity and adds some detailed comparisons of specific AU-rich motif effects in these two cell types.

Using a Lasso regression, TA-dinucleotide content is identified as a strong regulator of RNA stability in a context dependent manner based on GC content and presence of RNA binding protein binding motifs. The findings have potential importance, drawing attention to a UTR feature that is not well characterized.

The use of complementary datasets, including from half-life analyses of RNAs and from random sequence library MRPA's, is a useful addition and supports several important findings. The finding the TA dinucleotides have explanatory power separate from (and in some cases interacting with) GC content is valuable.

The functional enrichment analysis suggests some new ideas about how UTRs may contribute to regulation of certain classes of genes.

Weaknesses:

In this section, original reviewer comments about the initial submission and the responses of the authors are listed together with new reviewer responses to the authors:

Reviewer original comment 1: It is difficult to understand how the calculations for half-life were performed. The sequencing approach measures the relative frequency of each sequence at each time point (less stable sequences become relatively less frequent after time 0, whereas more stable sequences become relatively more frequent after time 0). Since there is no discussion of whether the abundance of the transfected RNA population is referenced to some external standard (e.g., housekeeping RNAs), it is not clear how absolute (rather than relative) half-lives were determined.

Author response: [The authors showed the equations used to calculate half lives based on read counts.] They stated that "The absolute abundance was not required for the half-life calculation."

Reviewer response to authors: The methods section states that DESeq2 was used to normalize read counts. DESeq2 normalization assumes that levels of most RNAs are not different between samples. That assumption is not valid here, since RNAs in the library are introduced into cells at time 0 and all RNAs decrease over time. If DESeq2 is applied without modification to normalize across timepoints, normalized reads from less stable RNAs will decrease over time (as expected) but normalized reads from more stable RNAs will increase. Can the authors please clarify in the methods how the read counts were normalized to account for this issue?

Reviewer original comment 2: Fig. S1A and B are used to assess reproducibility. They show that read counts at a given time point correlate well across replicate experiments. However, this is not a good way to assess reproducibility or accuracy of the measurements of t1/2 are. (The major source of variability in read counts in these plots - especially at early time points - is likely starting abundance of each RNA sequence, not stability.) This creates concerns about how well the method is measuring t1/2. Also creating concern is the observation that many RNAs are associated with half-lives that are much longer than the time points analyzed in the study. For example, based upon Figure S1 and Table S1 correctly, the median t1/2 for the 5' UTR library in HEK cells appears to be >700 minutes. Given that RNA was collected at 30, 75, and 120 minutes, accurate measurements of RNAs with such long half lives would seem to be very difficult.

Author response: ... The calculation of the half-life involves first determining the decay constant λ, which represents a constant rate of decay. Since λ is a constant, it is possible to accurately calculate it without needing data over the entire decay range. Our experimental design considers this by selecting appropriate time points to ensure a reliable estimation of λ, and thus, the half-life. To determine the most suitable time points, we conducted preliminary experiments using RT-PCR. These experiments indicated that 30, 75, and 120 minutes provided an effective range for capturing the decay dynamics of the transcripts.

Reviewer response to author comments: Based on Fig. S1D, for 3' UTRs in both cell types and for 5' UTRs in SH-SY5Y cells, median t1/2 is in the range of ~30 to 90 minutes (corresponding to ln t1/2 = 3.5 to 4.5). Measuring RNAs at 30, 75, and 120 minutes would therefore be a good choice for these cases, However, median t1/2 in HEK cells appears to be ~600 minutes (corresponding to ln t1/2 ~6.4) for HEK cells. For t1/2 of 600 minutes, RNA levels at the final time point (120 minutes) would be 90% of the those at the first time point (30 minutes), which illustrates why the method would need to be able to reliably capture very small changes in RNA abundance to accurately measure t1/2 for transcripts with half-lives much longer than 120 minutes. As suggested in our original review, this concern could be addressed by showing the correlation of half-lives across replicates for the 5' and 3' UTR libraries in both cell types. Alternatively, the authors could show other measures of reproducibility for the half-life measurements across replicates. This requires no additional experimentation and can be done using the data from replicate runs shown in Fig. S1A and B. We remain concerned that for sequences with very long half-lives, extrapolating the half-life from small changes between 30 and 120 minutes will lead to imprecise measurements.

Reviewer original comment 3: There is no direct comparison of t1/2 between the two cell types studied for the full set of sequences studied. This would be helpful in understanding whether the regulatory effects of UTRs are generally similar across cell lines (as has been shown in some previous studies) or whether there are fundamental differences. The distribution of t1/2's is clearly quite different in the two cell lines, but it is important to know if this reflects generally slow RNA turnover in HEK cells or whether there are a large number of sequence-specific effects on stability between cell lines. A related issue is that it is not clear whether the relatively small number of significant variant effects detected in HEK cells versus SH-SY5Y cells is attributable to real biological differences between cell types or to technical issues (many fewer read counts and much longer half lives in HEK cells).

Author response: For both cell lines, we selected oligonucleotides with R2 > 0.5 and mean squared error (MSE) < 1 for analysis when estimating half-life (λ) by linear regression. This selection criterion was implemented to minimize the effect of experimental noise. After quality control, we selected common UTRs and compared the RNA half-lives of the two cell lines using a scatter plot. The figure below shows that RNA half-lives are quite different between the cell lines, with a moderate similarity observed in the 5' UTRs (R = 0.21), while the correlation in the 3' UTRs is non-significant. Despite the low correlation of mRNA half-life between the two cell lines, UA-dinucleotide and UA-rich sequences consistently emerge as the most significant destabilizing features, suggesting a shared regulatory mechanism across diverse cellular environments.

Reviewer response to author comments: We appreciate that the authors shared this additional analysis of the data. We believe that this is an important finding and that the additional figure showing correlations of half-lives across cell types should be included in the manuscript or supplement. Discussion of this result in the manuscript would also be useful for readers. This result is surprising to us since we would have expected that widely expressed RNA-binding proteins would have led to more similar effects between the two cell types, as previously found using other approaches (e.g., studies of 3' UTR effects in MPRAs). It would also be appropriate to discuss that differences seen between the two cell types indicate that caution is warranted when trying to generalize the results of this study to other cell types.

Reviewer original comment 4 has been addressed adequately in the revised manuscript.

Appraisal and impact:

Reviewer original comment 1: The work adds to existing studies that previously identified sequence features, including AREs and other RNA binding protein motifs, that regulate stability and puts a new emphasis on the role of "TA" (better "UA") dinucleotides. It is not clear how potential problems with the RNA stability measurements discussed above might influence the overall conclusions, which may limit the impact unless these can be addressed.

It is difficult to understand whether the importance of TA dinucleotides is best explained by their occurrence in a related set of longer RBP binding motifs (see Fig 5J, these motifs may be encompassed by the "WWWWWW cluster") or whether some other explanation applies. Further discussion of this would be helpful. Does the LASSO method tend to collapse a more diverse set of longer motifs that are each relatively rare compared to the dinucleotide? It remains unclear whether TA dinucleotides are associated with less stability independent of the presence of the known larger WWWWWWW motif. As noted above, the importance of TA dinucleotides in the HEK experiments appears to be less than is implied in the text.

Author response: To ensure the representativeness of the features entered into the LASSO model, we pre-selected those with an occurrence greater than 10% among all UTRs. There is no evidence to support a preference for dinucleotides by LASSO. To address whether the destabilizing effect of UA dinucleotides is part of the broader WWWWWW motif, we divided UA dinucleotides into two groups: those within the WWWWWW motif and those outside of it. Specifically, we divided UTRs into two categories: 'at least one UA within a WWWWWW motif' and 'no UA within a WWWWWW motif,' and visualized the results using a boxplot. As shown in [figures provided to the reviewers], the destabilizing trend still remains for UA dinucleotides outside of the WWWWWW motif, although the effect appears to be more pronounced when UA is within the WWWWWW motif. This suggests that while UA dinucleotides have a destabilizing effect independently, their impact is amplified when they are part of the broader WWWWWW motif.

Reviewer response to authors: These are useful additional analyses, and we suggest that the additional figure and discussion should be included in the manuscript/supplement so that readers can benefit from them.

Reviewer original comment 2: The inclusion of more than a single cell type is an acknowledgement of the importance of evaluating cell type-specific effects. The work suggests a number of cell type-specific differences, but due to technical issues (especially with the HEK data, as outlined above) and the use of only two cell lines, it is difficult to understand cell type effects from the work.

The inclusion of both 3' and 5' UTR sequences distinguishes this work from most prior studies in the field. Contrasting the effects of these regions on stability is of interest, although the role of these UTRs (especially the 5' UTR) in translational regulation is not assessed here.

Author response: We examined the role of UTR and UTR variants in translation regulation using polysome profiling. By both univariate analysis and an elastic regression model, we identified motifs of short repeated sequences, including SRSF2 binding sites, as mutation hotspots that lead to aberrant translation. Furthermore, these polysome-shifting mutations had a considerable impact on RNA secondary structures, particularly in upstream AUG-containing 5' UTRs. Integrating these features, our model achieved high accuracy (AUROC > 0.8) in predicting polysome-shifting mutations in the test dataset. Additionally, metagene analysis indicated that pathogenic variants were enriched at the upstream open reading frame (uORF) translation start site, suggesting changes in uORF usage underlie the translation deficiencies caused by these mutations. Illustrating this, we demonstrated that a pathogenic mutation in the IRF6 5' UTR suppresses translation of the primary open reading frame by creating a uORF. Remarkably, site-directed ADAR editing of the mutant mRNA rescued this translation deficiency. Because the regulation of translation and stability does not converge, we illustrate these two mechanisms in two separate manuscripts (this one and doi.org/10.1101/2024.04.11.589132).

Reviewer response to authors: This is useful context. No further comment.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97682.3.sa3](https://doi.org/10.7554/eLife.97682.3.sa3)

Summary:

In their manuscript titled "Multiplexed Assays of Human Disease‐relevant Mutations Reveal UTR Dinucleotide Composition as a Major Determinant of RNA Stability" the authors aim to investigate the effect of sequence variations in 3'UTR and 5'UTRs on the stability of mRNAs in two different human cell lines.

To do so, the authors use a massively parallel reporter assay (MPRA). They transfect cells with a set of mRNA reporters that contain sequence variants in their 3' or 5' UTRs, which were previously reported in human diseases. They follow their clearance from cells over time relative to the matching non-variant sequence. To analyze their results, they define a set of factors (RBP and miRNA binding sites, sequence features, secondary structure etc.) and test their association with differences in mRNA stability. For features with a significant association, they use clustering to select a subset of factors for LASSO regression and identify factors that affect mRNA stability.

They conclude that the TA dinucleotide content of UTRs is the strongest destabilizing sequence feature. Within that context, elevated GC content and protein binding can protect susceptible mRNAs from degradation. They also show that TA dinucleotide content of UTRs affects native mRNA stability and that it is associated with specific functional groups. Finally, they link disease associated sequence variants with differences in mRNA stability of reporters.

Strengths:

(1) This work introduces a different MPRA approach to analyze the effect of genetic variants. While previous works in tissue culture use DNA transfections that require normalization for transcription efficiency, here the mRNA is directly introduced into cells at fixed amounts, allowing a more direct view of the mRNA regulation.

(2) The authors also introduce a unique analysis approach, which takes into account multiple factors that might affect mRNA stability. This approach allows them to identify general sequence features that affect mRNA stability beyond specific genetic variants, and reach important insights on mRNA stability regulation. Indeed, while the conclusions to genetic variants identified in this work are interesting, the main strength of the work involves general effect of sequence features rather than specific variants.

(3) The authors provide adequate support for their claims and validate their analysis using both their reporter data and native genes. For the main feature identified, TA di-nucleotides, they perform follow-up experiments with modified reporters that further strengthen their claims, and also validate the effect on native cellular transcripts (beyond reporters), demonstrating its validity also within native scenarios.

(4) The work provides a broad analysis of mRNA stability, across two mRNA regulatory segments (3'UTR and 5'UTR) and is performed in two separate cell-types. Comparison between two different cell-types is adequate, and the results demonstrate, as expected, the dependence of mRNA stability on the cellular context. Analysis of 3'UTR and 5'UTR regulatory effects also shows interesting differences and similarities between these two regulatory regions.

Weaknesses:

In their revised manuscripts, the authors successfully address many of the weaknesses raised in the original review, including the effect of possible confounding effects, and additional methodology details. Notably, two of the issues raised in the original report, have only been partially addressed in the revision.

(1) The analysis and regression models built in this work are not thoroughly investigated relative to native genes within cells.

While using MPRAs indeed allows to isolate regulatory effects that are less influential in-vivo, the resulting effects still provide some regulatory function in-vivo. The goal of such an analysis would not be to demonstrate the predictive power of the models, or to make any claims regarding using these models to fully explain or predict the stability of native transcripts. Clearly, additional more prominent factors could function in controlling endogenous RNA stability.

Instead, the goal of such an investigation is to simply assess the fraction of in-vivo regulation that the factors identified in this work contribute in native contexts, and what is the relative contribution of the phenomena captured by the well-controlled MPRA study.

This reviewer believes that even if the effects identified by the current MPRA study only contribute a small fraction of in-vivo variation, an analysis that aim to estimate what this fraction is, will be very relevant to this study for several reasons. First, in order to appreciate the results of this study within their in-vivo context. Second, in light of the questions raised as motivation for this study, and particularly the need to identify the effect of disease-associated 3'UTR variants, which clearly have an in-vivo effect.

(2) Methodology validation can be performed with simulated data (generated in-silico by the authors) to provide an independent support for the ability of the current methodology to correctly extract regulatory effects from the data.

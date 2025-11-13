# Measuring the sequence-affinity landscape of antibodies with massively parallel titration curves

## Authors

- Rhys M Adams<sup>1</sup>
- Thierry Mora<sup>3</sup> ([ORCID: 0000-0002-5456-9361](https://orcid.org/0000-0002-5456-9361)) †
- Aleksandra M Walczak<sup>1</sup> ([ORCID: 0000-0002-2686-5702](https://orcid.org/0000-0002-2686-5702)) †
- Justin B Kinney<sup>2</sup> ([ORCID: 0000-0003-1897-3778](https://orcid.org/0000-0003-1897-3778)) †

### Affiliations

1. Laboratoire de Physique Théorique, UMR8549, CNRS, École Normale Supérieure Paris France
2. Simons Center for Quantitative Biology Cold Spring Harbor Laboratory Cold Spring Harbor United States
3. Laboratoire de Physique Statistique, UMR8550, CNRS, École Normale Supérieure Paris France

† Corresponding author

## Abstract

Despite the central role that antibodies play in the adaptive immune system and in biotechnology, much remains unknown about the quantitative relationship between an antibody’s amino acid sequence and its antigen binding affinity. Here we describe a new experimental approach, called Tite-Seq, that is capable of measuring binding titration curves and corresponding affinities for thousands of variant antibodies in parallel. The measurement of titration curves eliminates the confounding effects of antibody expression and stability that arise in standard deep mutational scanning assays. We demonstrate Tite-Seq on the CDR1H and CDR3H regions of a well-studied scFv antibody. Our data shed light on the structural basis for antigen binding affinity and suggests a role for secondary CDR loops in establishing antibody stability. Tite-Seq fills a large gap in the ability to measure critical aspects of the adaptive immune system, and can be readily used for studying sequence-affinity landscapes in other protein systems.

## Introduction

During an infection, the immune system must recognize and neutralize invading pathogens. B-cells contribute to immune defense by producing antibodies, proteins that bind specifically to foreign antigens. The astonishing capability of antibodies to recognize virtually any foreign molecule has been repurposed by scientists in a wide variety of experimental techniques (immunofluorescence, western blots, ELISA, ChIP-Seq, etc.). Antibody-based therapeutic drugs have also been developed for treating many different diseases, including cancer (Chan and Carter, 2010).

Much is known about the qualitative mechanisms of antibody generation and function (Murphy et al., 2008). The antigenic specificity of antibodies in humans, mice, and most jawed vertebrates is primarily governed by six complementarity determining regions (CDRs), each roughly 10 amino acids (aa) long. Three CDRs (denoted CDR1H, CDR2H, and CDR3H) are located on the antibody heavy chain, and three are on the light chain. During B-cell differentiation, these six sequences are randomized through V(D)J recombination, then selected for functionality as well as against the ability to recognize host antigens. Upon participation in an immune response, CDR regions can further undergo somatic hypermutation and selection, yielding higher-affinity antibodies for specific antigens. Among the CDRs, CDR3H is the most highly variable and typically contributes the most to antigen specificity; less clear are the functional roles of the other CDRs, which often do not interact with the target antigen directly.

Many high-throughput techniques, including phage display (Smith, 1985; Vaughan et al., 1996; Schirrmann et al., 2011), ribosome display (Fujino et al., 2012), yeast display (Boder and Wittrup, 1997; Gai and Wittrup, 2007), and mammalian cell display (Forsyth et al., 2013), have been developed for optimizing antibodies ex vivo. Advances in DNA sequencing technology have also made it possible to effectively monitor both antibody and T-cell receptor diversity within immune repertoires, e.g. in healthy individuals (Boyd et al., 2009; Weinstein et al., 2009; Robins et al., 2009, 2010; Mora et al., 2010; Venturi et al., 2011; Murugan et al., 2012; Zvyagin et al., 2014; Elhanati et al., 2014; Qi et al., 2014; Thomas et al., 2014; Elhanati et al., 2015), in specific tissues (Madi et al., 2014), in individuals with diseases (Parameswaran et al., 2013) or following vaccination (Jiang et al., 2013; Vollmers et al., 2013; Laserson et al., 2014; Galson et al., 2014; Wang et al., 2015). Yet many questions remain about basic aspects of the quantitative relationship between antibody sequence and antigen binding affinity. How many different antibodies will bind a given antigen with specified affinity? How large of a role do epistatic interactions between amino acid positions within the CDRs have on antigen binding affinity? How is this sequence-affinity landscape navigated by the V(D)J recombination process, or by somatic hypermutation? Answering these and related questions is likely to prove critical for developing a systems-level understanding of the adaptive immune system, as well as for using antibody repertoire sequencing to diagnose and monitor disease.

Recently developed ‘deep mutational scanning’ (DMS) assays (Fowler and Fields, 2014) provide one potential method for measuring binding affinities with high enough throughput to effectively explore antibody sequence-affinity landscapes. In DMS experiments, one begins with a library of variants of a specific protein. Proteins that have high levels of a particular activity of interest are then enriched via one or more rounds of selection, which can be carried out in a variety of ways. The set of enriched sequences is then compared to the initial library, and protein sequences (or mutations within these sequences) are scored according to how much this enrichment procedure increases their prevalence.

Multiple DMS assays have been described for investigating protein-ligand binding affinity. But no DMS assay has yet been shown to provide absolute quantitative binding affinity measurements, i.e., dissociation constants in molar units. For example, one of the first DMS experiments (Fowler et al., 2010) used phage display technology to measure how mutations in a WW domain affect the affinity of this domain for its peptide ligand. These data were sufficient to compute enrichment ratios and corresponding sequence logos, but they did not yield quantitative affinities. Analogous experiments have since been performed on antibodies using yeast display (Reich et al., 2015; Kowalsky et al., 2015) and mammalian cell display (Forsyth et al., 2013). Yeast-display-based DMS assays have also proven particularly useful for mapping protein epitopes that are targeted by specific antibodies of interest (Kowalsky et al., 2015; Doolan and Colby, 2015; Van Blarcom et al., 2015). Still, none of these approaches provides quantitative affinity values. SORTCERY (Reich et al., 2015, ), a DMS assay that combines yeast display and quantitative modeling, has been shown to provide approximate rank-order values for the affinity of a specific protein for short unstructured peptides of varying sequence. Determining quantitative affinities from SORTCERY data, however, requires separate low-throughput calibration measurements (Reich et al., 2014). Moreover, it is unclear how well SORTCERY, if applied to a library of folded proteins rather than unstructured peptides, can distinguish sequence-dependence effects on affinity from sequence-dependent effects on protein expression and stability. Other recent work has described a DMS assay, again based on yeast display, for measuring fold-changes in affinity relative to a reference protein (Kowalsky and Whitehead, 2016). This method, however, does not provide absolute values for dissociation constants, is vulnerable to the confounding effects of sequence-dependent expression and protein stability, and was observed to have only a 10-fold dynamic range.

To enable massively parallel measurements of absolute binding affinities for antibodies and other structured proteins, we have developed an assay called ‘Tite-Seq.’ Tite-Seq, like SORTCERY, builds on the capabilities of Sort-Seq, an experimental strategy that was first developed for studying transcriptional regulatory sequences in bacteria (Kinney et al., 2010). Sort-Seq combines fluorescence-activated cell sorting (FACS) with high-throughput sequencing to provide massively parallel measurements of cellular fluorescence. In the Tite-Seq assay, Sort-Seq is applied to antibodies displayed on the surface of yeast cells and incubated with antigen at a wide range of concentrations. From the resulting sequence data, thousands of antibody-antigen binding titration curves and their corresponding absolute dissociation constants (here denoted $K_{D}$) can be inferred. By assaying full binding curves, Tite-Seq is able to measure affinities over many orders of magnitude (We note that Kowalsky et al. (2015) have described yeast display DMS experiments performed at multiple concentrations. These data, however, were not used to reconstruct titration curves or infer quantitative $K_{D}$ values). Moreover, the resulting affinity values provided by Tite-Seq are not confounded by the (rather substantial) effect that sequence variation can have on either (a) the amount of protein expressed on the surface of cells or (b) the specific activity of displayed proteins (i.e., the fraction of protein molecules that are functional).

We demonstrated Tite-Seq on a protein library derived from a well-studied single-chain variable fragment (scFv) antibody specific to the small molecule fluorescein (Boder and Wittrup, 1997; Boder et al., 2000). Mutations were restricted to CDR1H and CDR3H regions, which are known to play an important role in the antigen recognition of this scFv (Boder et al., 2000; Midelfort et al., 2004). The resulting affinity measurements were validated with binding curves for a handful of clones measured using standard low-throughput flow cytometry. Our Tite-Seq measurements reveal both expected and unexpected differences between the effects of mutations in CDR1H and CDR3H. These data also shed light on structural aspects of antigen recognition that are independent of effects on antibody stability.

## Results

### Overview of Tite-Seq

Our general strategy is illustrated in Figure 1. First, a library of variant antibodies is displayed on the surface of yeast cells (Figure 1A). The composition of this library is such that each cell displays a single antibody variant, and each variant is expressed on the surface of multiple cells. Cells are then incubated with the antigen of interest, bound antigen is fluorescently labeled, and fluorescence-activated cell sorting (FACS) is used to sort cells one-by-one into multiple ‘bins’ based on this fluorescent readout (Figure 1B). Deep sequencing is then used to survey the antibody variants present in each bin. Because each variant antibody is sorted multiple times, it will be associated with a histogram of counts spread across one or more bins (Figure 1C). The spread in each histogram is due to cell-to-cell variability in antibody expression, and to the inherent noisiness of flow cytometry measurements. Finally, the histogram corresponding to each antibody variant is used to compute an ‘average bin number’ (Figure 1C, dots), which serves as a proxy measurement for the average amount of bound antigen per cell.

![Figure 1.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig1-v3.jpg)

**Figure 1.:** (A) A library of variant antibodies (various colors) are displayed on the surface of yeast cells (tan). (B) The library is exposed to antigen (green triangles) at a defined concentration, cell-bound antigen is fluorescently labeled, and FACS is used to sort cells into bins according to measured fluorescence. (C) The antibody variants in each bin are sequenced and the distribution of each variant across bins is computed (histograms; colors correspond to specific variants). The mean bin number (dot) is then used to quantify the typical amount of bound antigen per cell. (D) Binding titration curves (solid lines) and corresponding $K_{D}$ values (vertical lines) can be inferred for individual antibody sequences by using the mean fluorescence values (dots) obtained from flow cytometry experiments performed on clonal populations of antibody-displaying yeast. (E) Tite-Seq consists of performing the Sort-Seq experiment in panels A–C at multiple antigen concentrations, then inferring binding curves using mean bin number as a proxy for mean cellular fluorescence. This enables $K_{D}$ measurements for thousands of variant antibodies in parallel. We note that the Tite-Seq results illustrated in panel E were simulated using three bins under idealized experimental conditions, as described in Appendix 1. The inference of binding curves from real Tite-Seq data is more involved than this panel might suggest, due to the multiple sources of experimental noise that must be accounted for.

It has previously been shown that $K_{D}$ values can be accurately measured using yeast-displayed antibodies by taking binding titration curves, i.e., by measuring the average amount of bound antigen as a function of antigen concentration (VanAntwerp and Wittrup, 2000; Gai and Wittrup, 2007). The median fluorescence $f$ of labeled cells is expected to be related to antigen concentration via

$$
f=A⁢\frac{c}{c+K_{D}}+B
$$

where $A$ is proportional to the number of functional antibodies displayed on the cell surface, $B$ accounts for background fluorescence, and $c$ is the concentration of free antigen in solution. Figure 1D illustrates the shape of curves having this form. By using flow cytometry to measure $f$ on clonal populations of yeast at different antigen concentrations $c$, one can infer curves having the sigmoidal form shown in Equation 1 and thereby learn $K_{D}$. Such measurements, however, can only be performed in a low-throughput manner.

Tite-Seq allows thousands of binding titration curves to be measured in parallel. The Sort-Seq procedure illustrated in Figure 1A–C is performed at multiple antigen concentrations, and the resulting average bin number for each variant antibody is plotted against concentration. Sigmoidal curves are then fit to these proxy measurements, enabling $K_{D}$ values to be inferred for each variant.

We emphasize that $K_{D}$ values cannot, in general, be accurately inferred from Sort-Seq experiments performed at a single antigen concentration. Because the relationship between binding and $K_{D}$ is sigmoidal, the amount of bound antigen provides a quantitative readout of $K_{D}$ only when the concentration of antigen used in the labeling procedure is comparable in magnitude to $K_{D}$. However, single mutations within a protein binding domain often change $K_{D}$ by multiple orders of magnitude. Sort-Seq experiments used to measure sequence-affinity landscapes must therefore be carried out over a range of concentrations large enough to encompass this variation.

Furthermore, as illustrated in Figure 1C and D, different antibody variants often lead to different levels of functional antibody expression on the yeast cell surface. If one performs Sort-Seq at a single antigen concentration, high affinity (low $K_{D}$) variants with low expression (blue variant) may bind less antigen than low affinity (high $K_{D}$) variants with high expression (orange variant). Only by measuring full titration curves can the effect that sequence has on affinity be deconvolved from sequence-dependent effects on functional protein expression.

### Proof-of-principle Tite-Seq experiments

To test the feasibility of Tite-Seq, we used a well-characterized antibody-antigen system: the 4-4-20 single chain variable fragment (scFv) antibody (Boder and Wittrup, 1997), which binds the small molecule fluorescein with KD=1.2 nM (Gai and Wittrup, 2007). This system was used in early work to establish the capabilities of yeast display (Boder and Wittrup, 1997), and a high resolution co-crystal structure of the 4-4-20 antibody bound to fluorescein, shown in Figure 2A, has been determined (Whitlow et al., 1995). An ultra-high-affinity (KD=270 fM) variant of this scFv, called 4m5.3, has also been found (Boder et al., 2000). In what follows, we refer to the 4-4-20 scFv from Boder and Wittrup (1997) as WT, and the 4m5.3 variant from Boder et al. (2000) as OPT.

![Figure 2.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig2-v3.jpg)

**Figure 2.:** (A) Co-crystal structure of the 4-4-20 (WT) antibody from Whitlow et al. (1995) (PDB code 1FLR). The CDR1H and CDR3H regions are colored blue and red, respectively. (B) The yeast display scFv construct from Boder and Wittrup (1997) that was used in this study. Antibody-bound antigen (fluorescein) was visualized using PE dye. The amount of surface-expressed protein was separately visualized using BV dye. Approximate location of the CDR1H (blue) and CDR3H (red) regions within the scFv are illustrated. (C) The gene coding for this scFv construct, with the six CDR regions indicated. The WT sequence of the two 10 aa variable regions are also shown. (D) The number of 1-, 2-, and 3-codon variants present in the 1H and 3H scFv libraries. Figure 2—figure supplement 1 shows the cloning vector used to construct the CDR1H and CDR3H libraries, as well as the form of the resulting expression plasmids.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (A) The iRA11 amplicon library, which was prepared from microarray-synthesized oligos containing variant CDR1H or variant CDR3H regions. This amplicon is flanked by inward-facing BsaI restriction sites. (B) The pRA10 cloning vector, which contains the ccdB selection gene within a cassette flanked by outward-facing BsmBI restriction sites. (C) The pRA11 plasmid library, which was cloned by ligating BsaI-digested iRA11 amplicons and BsmBI-digest pRA10 vector. (D) The sequencing amplicon that was amplified from sorted cells after Tite-Seq and Sort-Seq experiments and submitted for ultra-high-throughput DNA sequencing. Appendix 3 provides more details about iRA11 amplicons, the pRA10 vector, and the pRA11 plasmid library. Appendix 4 provides more information about the creation of sequencing amplicons.

The scFv was expressed on the surface of yeast as part of the multi-domain construct illustrated in Figure 2B and previously described in Boder and Wittrup (1997). Following (Boder et al., 2000), we used fluorescein-biotin as the antigen and labeled scFv-bound antigen with streptavidin-RPE (PE). The amount of surface-expressed protein was separately quantified by labeling the C-terminal c-Myc tag using anti-c-Myc primary antibodies, followed by secondary antibodies conjugated to Brilliant Violet 421 (BV). See Appendix 2 for details on this labeling procedure.

Two different scFv libraries were assayed simultaneously. In the ‘1H’ library, a 10 aa region encompasing the CDR1H region of the WT scFv (see Figure 2C) was mutagenized using microarray-synthesized oligos (see Appendix 3 for details). The resulting 1H library consisted of all 600 single-codon variants of this 10 aa region, 1100 randomly chosen 2-codon variants, and 150 random 3-codon variants (Figure 2D). An analogous ‘3H’ library was generated for a 10 aa region containing the CDR3H region of this scFv. In all of the Tite-Seq experiments described below, these two libraries were pooled together and supplemented with WT and OPT scFvs, as well with a nonfunctional scFv referred to as $Δ$.

Tite-Seq was carried out as follows. Yeast cells expressing scFv from the mixed library were incubated with fluorescein-biotin at one of eleven concentrations: 0 M, 10-9.5 M, 10-9 M, 10-8.5 M, 10-8 M, 10-7.5 M, 10-7 M, 10-6.5 M, 10-6 M, 10-5.5 M, and 10-5 M. After subsequent PE labeling of bound antigen, cells were sorted into four bins using FACS (Figure 3A). Separately, BV-labeled cells were sorted according to measured scFv expression levels (Figure 3B). The number of cells sorted into each bin is shown in Figure 3C. Each bin of cells was regrown and bulk DNA was extracted. The 1H and 3H variable regions were then PCR amplified and sequenced using paired-end Illumina sequencing, as described in Appendix 4. The final data set consisted of an average of 2.6×106 sequences per bin across all 48 bins (Figure 3D). Three independent replicates of this experiment were performed on three different days.

![Figure 3.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig3-v3.jpg)

**Figure 3.:** (A) Gates used to sort cells based on PE fluorescence, which provides a readout of bound antigen. Cells were labeled at the eleven different antigen concentrations. Shades of red indicate the four fluorescence gates used to sort cells; these correspond to bins 0, 1, 2, and 3 (from left to right). (B) Gates, indicated in shades of purple, used to sort cells based on BV fluorescence, which provides a readout of antibody expression. (C) The number of cells sorted into each bin. (D) The number of Illumina reads obtained from each bin of sorted cells after quality control measures were applied. The data shown in this figure corresponds to a single Tite-Seq experiment. Figure 3—figure supplement 1 and Figure 3—figure supplement 2 show data for two independent replicates of this experiment.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Analog of Figure 3 in the main text, but for the replicate 2 Tite-Seq experiment.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** Analog of Figure 3 in the main text, but for the replicate 3 Tite-Seq experiment.

For each variant scFv gene, a KD value was inferred by fitting a binding curve to the resulting Tite-Seq data, with separate curves independently fit to data from each Tite-Seq experiment (Figure 4A). As illustrated in Figure 1E, this fitting procedure uses the sigmoidal function in Equation 1 to model mean bin number as a function of antigen concentration. However, the need to account for multiple sources of noise in the Tite-Seq experiment necessitates a more complex procedure than Figure 1E might suggest; the details of this inference procedure are described in Appendix 5.

![Figure 4.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-v3.jpg)

**Figure 4.:** (A) Binding curves and $K_{D}$ measurements inferred from Tite-Seq data. (B) Mean fluorescence values (dots) and corresponding inferred binding curves (lines) obtained by flow cytometry measurements for five selected scFvs (WT, OPT, C5, C45, and C107). In (A,B), values corresponding to 0 M fluorescein are plotted on the left-most edge of the plot, dotted lines show the upper ($10^{-5}$ M) and lower ($10^{-9.5}$ M) limits on $K_{D}$ sensitivity, vertical lines show inferred $K_{D}$ values, and different shades correspond to different replicate experiments. (C) Comparison of the Tite-Seq-measured and flow-cytometry-measured $K_{D}$ values for all clones tested. Colors indicate different scFv protein sequences as follows: WT (purple), OPT (green), $Δ$ (black), 1H clones (blue), and 3H clones (red). Each $K_{D}$ value indicates the mean $log_{10}⁡K_{D}$ value obtained across all replicates, with error bars indicating standard error. Clones with $K_{D}$ outside of the affinity range are drawn on the boundaries of this range, which are indicated with dotted lines. The coefficient of determination ($R^{2}$) between log Tite-Seq values and log flow $K_{D}$values includes clones outside of the affinity range; in such cases, the corresponding boundary value ($10^{-9.5}$ M or $10^{-5.0}$ M) has been used. The amino acid sequences and measured $K_{D}$ values for all clones tested are provided in Table 1. Figure 4—figure supplement 1 provides plots, analogous to panels A and B, for all of the assayed clones. Figure 4—figure supplement 2 compares $K_{D}$ and $E$ values obtained across all three Tite-Seq replicates. Figure 4—figure supplement 3 quantifies measurement error using synonymous mutants. Figure 4—figure supplement 4 provides information about library composition. Figure 4—figure supplement 5 illustrates the poor correlation between scFv enrichment and Tite-seq measured $K_{D}$ values. Figure 4—figure supplement 6 shows a 2-fold difference in the specific activities of OPT and WT scFvs. Figure 4—figure supplement 7 illustrates the simulations we used in Figure 4—figure supplement 8 to validate the ability of our analysis to infer correct $K_{D}$ values.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Binding curves, measured using (A) Tite-Seq or (B) flow cytometry, for all clones analyzed in this paper and described in Table 1. Plots are drawn as in Figure 4, panels A and B.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Density plots of (A) Tite-Seq-measured $K_{D}$ values and (B) Sort-Seq-measured $E$ values between all pairs of replicate experiments. Measurements for these quantities that were judged to be of low precision due to low sequence counts are not plotted. $f$ indicates the percentage of total assayed sequences plotted; $r$ is the Pearson correlation and includes clonal measurements outside the boundaries of our measurable ranges ($10^{-9.5}-10^{-5}$ M for $K_{D}$, 0–2 for expression). Clones outside of these ranges were given values at the closest boundary.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp3-v3.jpg)

**Figure 4—figure supplement 3.:** Density plots for (A) Tite-Seq-measured log$_{10}K_{D}$ standard deviation and average log$_{10}K_{D}$ and (B) Sort-Seq-measured $E$ standard deviation and average $E$ are shown for each scFv sequence with more than one synonymous mutant for each of the replicate experiments. The $K_{D}$ error peaked between $10^{-7}-10^{-6}$ M. The expression error peaked at or above WT expression (i.e. 1) levels.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp4-v3.jpg)

**Figure 4—figure supplement 4.:** (A) Comparison of library composition between all pairs of replicate experiments. (B) Zipf plots showing the library composition in each replicate experiment. In both panels, the prevalence of each scFv sequence in each replicate experiment was determined as part of the Tite-Seq curve fitting procedure, as described in Appendix 5.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp5-v3.jpg)

**Figure 4—figure supplement 5.:** To assess how well simple enrichment calculations might reproduce the $K_{D}$ values measured by Tite-Seq, we did the following calculation. For each of the two libraries (1 H and 3 H), we partitioned scFvs into seven groups based on their measured $K_{D}$s (columns). For each group at each antigen concentration (rows), we then computed the enrichment of each scFv in the high PE bins (bins 2,3) relative to the low PE bins (bins 0,1). In these enrichment calculations, the number of counts in each bin was re-weighted to accurately reflect the fraction of library cells falling within the fluorescence range of that bin. This figure shows the resulting Spearman rank correlation $(ρ)$ between enrichment and log $K_{D}$ values computed for each scFv group at each antigen concentration. In both libraries, we see that correlation values above background (which can be assessed from the values in the 0 M fluorescein row) only occur close to the diagonal, i.e., when $K_{D}$ is close to the fluorescein concentration used.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp6-v3.jpg)

**Figure 4—figure supplement 6.:** 2D flow cytometry histograms showing both OPT- and WT-expressing cells labeled with PE and BV after incubation at 2 $\mu$M fluorescein. At this fluorescein concentration, nearly all functional WT and OPT scFvs are bound. Regression lines (fixed to have slope 1) were fit to data points with BV signal between $10^{4.5}$ and $10^{5}$. The vertical shift of the OPT data relative to the WT data indicates a factor of $2.03\pm0.07$ difference (computed from four replicate experiments) in the amount labeled antigen. This difference is not due to a difference in the number of surface-displayed scFvs, as this would cause the OPT and WT clouds to lie along the same diagonal. Rather, this difference between WT and OPT is due to variation in specific activity.

![Figure 4—figure supplement 7.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp7-v3.jpg)

**Figure 4—figure supplement 7.:** Realistic Tite-Seq data were simulated separately for each distinct pair of affinity ($K_{D}$) and amplitude ($A$) values, as described in Appendix 7. This figure shows simulated data, akin to the data displayed in Figure 4—figure supplement 6, for WT values of $K_{D}$ and $A$.

![Figure 4—figure supplement 8.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig4-figsupp8-v3.jpg)

**Figure 4—figure supplement 8.:** $K_{D}$ values were inferred for Tite-Seq data simulated using (green) the same number of cells, (light green) $10^{-3}$ times as many cells, or (black) $10^{4}$ times as many sorted cells as in our experiments. Areas indicate approximately plus or minus one standard deviation in the fitted $K_{D}$ values obtained for each true $K_{D}$ value.

**Table 1.**
 Clones measured using flow cytometry and Tite-Seq. List of scFv clones, ordered by their flow-cytometry-measured $K_{D}$ values. With the exception of OPT and $Δ$, these clones differed from WT only in their 1H and 3H variable regions. WT amino acids within these regions are capitalized; variant amino acids are shown in lower case. No sequence is shown for $Δ$ because this clone contained a large deletion, making identification of the 1H and 3H variable regions meaningless. $K_{D}$ values saturating our lower detection limit of $10^{-9.5}$ M or upper detection limit of $10^{-5.0}$M are written with a $≲$ or $≳$ sign to emphasize the uncertainty in these measurements. Tite-Seq $K_{D}$ values indicate mean and standard errors computed across the three replicate Tite-Seq experiments; they are not averaged across synonymous variants.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>1H variable region</th>
      <th>3H variable region</th>
      <th>No. replicates (flow)</th>
      <th>KD [M] (flow)</th>
      <th>KD [M] (Tite-Seq)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>OPT</td>
      <td>TFghYWMNWV</td>
      <td>GasYGMeYlG</td>
      <td>3</td>
      <td>≲10−9.5</td>
      <td>≲10−9.5</td>
    </tr>
    <tr>
      <td>C107</td>
      <td>TFSDYWMNWV</td>
      <td>GaYYGMDYWG</td>
      <td>3</td>
      <td>10−9.28±0.04</td>
      <td>10−9.18±0.11</td>
    </tr>
    <tr>
      <td>C112</td>
      <td>TFSDYWMNWV</td>
      <td>GSYYGMDYcG</td>
      <td>3</td>
      <td>10−8.95±0.07</td>
      <td>10−9.19±0.14</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>TFSDYWMNWV</td>
      <td>GSYYGMDYWG</td>
      <td>10</td>
      <td>10−8.61±0.07</td>
      <td>10−8.92±0.10</td>
    </tr>
    <tr>
      <td>C144</td>
      <td>vFSDYWMNWV</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>10−8.57±0.03</td>
      <td>10−8.86±0.04</td>
    </tr>
    <tr>
      <td>C133</td>
      <td>aFSDYWMNWV</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>10−8.55±0.06</td>
      <td>10−8.62±0.09</td>
    </tr>
    <tr>
      <td>C132</td>
      <td>TFmDYWlNWV</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>10−8.48±0.08</td>
      <td>10−8.38±0.29</td>
    </tr>
    <tr>
      <td>C94</td>
      <td>TFSDYWMNWV</td>
      <td>GSYYGMDsWG</td>
      <td>3</td>
      <td>10−8.46±0.06</td>
      <td>10−8.50±0.04</td>
    </tr>
    <tr>
      <td>C5</td>
      <td>TFSDYWiNWV</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>10−8.34±0.10</td>
      <td>10−8.55±0.09</td>
    </tr>
    <tr>
      <td>C93</td>
      <td>TFSDYWMNWV</td>
      <td>GSYrGMDYWG</td>
      <td>3</td>
      <td>10−7.35±0.08</td>
      <td>10−7.60±0.70</td>
    </tr>
    <tr>
      <td>C39</td>
      <td>TFSDYWMNWV</td>
      <td>GSYYGMDYWa</td>
      <td>3</td>
      <td>10−7.08±0.20</td>
      <td>10−7.28±0.17</td>
    </tr>
    <tr>
      <td>C102</td>
      <td>TFSDYWMNWV</td>
      <td>sSkYGMDYWG</td>
      <td>3</td>
      <td>10−5.76±0.16</td>
      <td>10−7.25±0.60</td>
    </tr>
    <tr>
      <td>C22</td>
      <td>ssSDYWMNWV</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>10−5.69±0.31</td>
      <td>10−7.53±0.07</td>
    </tr>
    <tr>
      <td>C7</td>
      <td>hFSDYWMNWl</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>10−5.53±0.18</td>
      <td>10−5.39±0.18</td>
    </tr>
    <tr>
      <td>C45</td>
      <td>TFSDYWMNWV</td>
      <td>GSYdGnDYWG</td>
      <td>3</td>
      <td>10−5.40±0.24</td>
      <td>≳10−5.0</td>
    </tr>
    <tr>
      <td>C103</td>
      <td>TFSDYWMNWV</td>
      <td>GSYYGMDlWG</td>
      <td>3</td>
      <td>10−5.15±0.47</td>
      <td>10−5.44±0.55</td>
    </tr>
    <tr>
      <td>C3</td>
      <td>TFSDYWMsWV</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>≳10−5.0</td>
      <td>≳10−5.0</td>
    </tr>
    <tr>
      <td>C18</td>
      <td>TFSDYsMNWV</td>
      <td>GSYYGMDYWG</td>
      <td>3</td>
      <td>≳10−5.0</td>
      <td>≳10−5.0</td>
    </tr>
    <tr>
      <td>Δ</td>
      <td>–</td>
      <td>–</td>
      <td>12</td>
      <td>≳10−5.0</td>
      <td>≳10−5.0</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Primers. Oligonucleotide sequences are written 5$^{′}$ to 3$^{′}$. Bold sequences indicate variable regions. The ‘1H library’ and ‘3H library’ primers respectively contained the 1H and 3H variable regions (bold) analyzed in this paper. These primer libraries were synthesized by LC Biosciences using microarray-based DNA synthesis. All other primers were ordered from Integrated DNA Technologies. The ‘[XX]’ portion of L1AF_XX and L1AR_XX indicates the location of each of 64 different barcodes (i.e., XX = 01, 02, $…$, 64), which ranged in length from 7 bp to 10 bp and which differed from each other by at least two substitution mutations.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Sequence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1H library</td>
      <td>GTGTTGCCTCTGGATTCACTTTTAGTGACTACTGGATGAACTGGGTCCGCCAGTCTCCAGA</td>
    </tr>
    <tr>
      <td>3H library</td>
      <td>GTGACTGAGGTTCCTTGACCCCAGTAGTCCATACCATAGTAAGAACCCGTACAGTAATAGATACCCAT</td>
    </tr>
    <tr>
      <td>oRAL10</td>
      <td>TTCTGAGGAGACGGTGACTGAGGTTCCTTG</td>
    </tr>
    <tr>
      <td>oRAR10</td>
      <td>TGAAGACATGGGTATCTATTACTGTACG</td>
    </tr>
    <tr>
      <td>oRAL11</td>
      <td>CAGTCCTTTCTCTGGAGACTGGCG</td>
    </tr>
    <tr>
      <td>oRAR11</td>
      <td>ATGAAACTCTCCTGTGTTGCCTCTGGATTC</td>
    </tr>
    <tr>
      <td>3H1F</td>
      <td>TTCTGAGGAGACGGTGACT</td>
    </tr>
    <tr>
      <td>3H2R</td>
      <td>TGAAGACATGGGTATCTATTACTGTAC</td>
    </tr>
    <tr>
      <td>1H2F</td>
      <td>CAGTCCTTTCTCTGGAGACTG</td>
    </tr>
    <tr>
      <td>1H1R</td>
      <td>ATGAAACTCTCCTGTGTTGCCT</td>
    </tr>
    <tr>
      <td>oRA10</td>
      <td>GCATATCTAAGGTCTCGTTCTGAGGAGACGGTGAC</td>
    </tr>
    <tr>
      <td>oRA11</td>
      <td>GCCGATTGTTGGTCTCCATGAAACTCTCCTGTGTTGC</td>
    </tr>
    <tr>
      <td>PE1v3ext</td>
      <td>AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACG</td>
    </tr>
    <tr>
      <td>PE2v3</td>
      <td>AAGCAGAAGACGGCATACGAGATCGGTCTCGGCATTCCTGCT</td>
    </tr>
    <tr>
      <td>L1AF_XX</td>
      <td>ACACTCTTTCCCTACACGACGCTCTTCCGATCT[XX]AGTCTTCTTCAGAAATAAGC</td>
    </tr>
    <tr>
      <td>L1AR_XX</td>
      <td>CTCGGCATTCCTGCTGAACCGCTCTTCCGATCT[XX]GCTTGGTGCAACCTG</td>
    </tr>
  </tbody>
</table>

Separately, the Sort-Seq data obtained by sorting the BV-labeled libraries were used to determine the expression level of each scFv. Specifically, we use $E$ to denote (for each scFv in the library) the mean bin number that results from this expression-based sorting; this $E$ value provides a measurement of the surface expression level of that scFv. All $E$ values have been scaled so that the mean of such measurements for all synonymous WT scFv gene variants is 1.0.

### Low-throughput validation experiments

To judge the accuracy of Tite-Seq, we separately measured binding curves for individual scFv clones as described for Figure 1D. In addition to the WT, OPT, and $Δ$ scFvs, we assayed eight clones from the 1H library (named C3, C5, C7, C18, C22, C132, C133 and C144) and eight clones from the 3H library (C39, C45, C93, C94, C102, C103, C107, C112). Each clone underwent the same labeling procedure as in the Tite-Seq experiment, after which median fluorescence values were measured using standard flow cytometry. $K_{D}$ values were then inferred by fitting binding curves of the form in Equation 1 using the procedure described in Appendix 6. These curves, which can be directly compared to Tite-Seq measurements (Figure 4A), are plotted in Figure 4B; at least three replicate binding curves were measured for each clone. See Figure 4—figure supplement 1 for the titration curves of all the tested clones.

### Tite-Seq can measure dissociation constants

Figure 4C reveals a strong correspondence between the $K_{D}$ values measured by Tite-Seq and those measured using low-throughput flow cytometry. The robustness of Tite-Seq is further illustrated by the consistency of $K_{D}$ values measured for the WT scFv. Using Tite-Seq, and averaging the results from the 33 synonymous variants and over all three replicates, we determined $K_{D}=10^{-8.87\pm0.02}$ M for the WT scFv. These measurements are largely consistent with the measurement of $K_{D}=10^{-8.61\pm0.07}$ M obtained by averaging low-throughput flow cytometry measurements across 10 replicates, and coincides with the previously measured value of $1.2$ nM $=10^{-8.9}$ M reported in (Gai and Wittrup, 2007). The three independent replicate Tite-Seq experiments give reproducible results as measured by direct comparison (Figure 4—figure supplement 2), from synonymous mutant variation (Figure 4—figure supplement 3) and library composition Figure 4—figure supplement 4) with Pearson coefficients ranging from $r=0.82$ to $r=0.89$ for all the measured $K_{D}$ values between replicates; note that $K_{D}$ values outside of the sensitivity range are included in the calculation of these Pearson coefficients as described in the Figure 4 caption.

The error bars for $K_{D}$ values in Figure 4C calculated from the variability of the fits to different replicates therefore support the reproducibility of the experiment. The main discrepancy in these error bar calculations occurred for clones c22 and c102 (see also Figure 4—figure supplement 1). The reason for this discrepancy is currently unclear. We note that Tite-Seq-measured $K_{D}$ values for these two clones are close to $10^{-7}$ M, and that the analysis of synonymous variants (Figure 4—figure supplement 3) found that Tite-Seq-measured $K_{D}$s in this region exhibited the largest variations.

The necessity of performing $K_{D}$ measurements over a wide range of antigen concentrations is illustrated in Figure 4—figure supplement 5. At each antigen concentration used in our Tite-Seq experiments, the enrichment of scFvs in the high-PE bins correlated poorly with the $K_{D}$ values inferred from full titration curves. Moreover, at each antigen concentration used, a detectable correlation between $K_{D}$ and enrichment was found only for scFvs with $K_{D}$ values close to that concentration.

Figure 4—figure supplement 6 suggests a possible reason for the weak correlation between $K_{D}$ values and enrichment in high-PE bins. We found that, at saturating concentrations of fluorescein ($2⁢\mu$M), cells expressing the OPT scFv bound twice as much fluorescein as cells expressing the WT scFv. This difference was not due to variation in the total amount of displayed scFv, which one might control for by labeling the c-Myc epitope as in Reich et al. (2015). Rather, this difference in binding reflects a difference in the specific activity of displayed scFvs. Yeast display experiments performed at a single antigen concentration cannot distinguish such differences in specific activity from differences in scFv affinity.

To further test the capability of Tite-Seq to infer dissociation constants from sequencing data over a wide range of values, as well as to validate our analysis procedures, we simulated Tite-Seq data in silico and analyzed the results using the same analysis pipeline that we used for our experiments. Details about the simulations are given in Appendix 7. The simulated data is illustrated in Figure 4—figure supplement 7. $K_{D}$ values inferred from these simulated data agreed to high accuracy with the $K_{D}$ used in the simulation (Figure 4—figure supplement 8), thus validating our analysis pipeline.

### Properties of the affinity and expression landscapes

Figure 5 shows the effect that every single-amino-acid substitution mutation within the 1H and 3H variable regions has on affinity and on expression; histograms of these effects are provided in Figure 5—figure supplement 1. In both regions, the large majority of mutations weaken antigen binding (1H: 88%; 3H: 93%), with many mutations increasing KD above our detection threshold of 10-5 M (1H: 36%; 3H: 52%). Far fewer mutations reduced KD (1H: 12%; 3H: 7%), and very few dropped KD below our detection limit of 10-9.5 M (1H: 0%; 3H: 3%). Histograms of the effect of two or three amino acid changes relative to WT, shown in Figure 5—figure supplement 2A, reveal that multiple random mutations tend to further reduce affinity. We also observed that mutations within the 3H variable region have a larger effect on affinity than do mutations in the 1H variable region. Specifically, single amino acid mutations in 3H were seen to increased KD more than mutations in 1H (1H median KD=10-6.84; 3H median KD≳10-5.0P=4.7×10-4; P=4.7×10−4, one-sided Mann-Whitney U test). This result suggests that binding affinity is more sensitive to variation in CDR3H than to variation in CDR1H, a finding that is consistent with the conventional understanding of these antibody CDR regions (Xu and Davis, 2000; Liberman et al., 2013).

![Figure 5.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig5-v3.jpg)

**Figure 5.:** Heatmaps show the measured effects on affinity (A,B) and expression (C,D) of all single amino acid substitutions within the variables regions of the 1H (A,C) and 3H (B,D) libraries. Purple dots indicate residues of the WT scFv. Green dots indicate non-WT residues in the OPT scFv. Figure 5—figure supplement 1 provides histograms of the non-WT values displayed in panels A–D. Figure 5—figure supplement 2 compares the effects on $K_{D}$ of both single-point and multi-point mutations.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A,B) Histogram showing the $K_{D}$ values measured for all substitution mutations in the 1 H (A) and 3 H (B) libraries. Note that these are the values plotted in panels A and B of Figure 5, except that the WT $K_{D}$ value is not included. Dashed lines indicate the $K_{D}$ of the WT scFv; dotted lines indicate thresholds just within our detection boundaries, $10^{-9.49}$ M and $10^{-5.01}$ M, while the colored bars outside this interval indicate the number of substitution mutations with $K_{D}$ above (blue) and below (red) this range. (C,D) Histogram of $E$ values for all single-substitution variants in the 1 H (C) or 3 H (D) libraries. These values, save those of the WT scFv, are plotted in panels C and D of Figure 5. Dashed lines indicate the WT expression level of $E=1.0$.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** The effect of 1, 2, or three mutations on (A) Tite-Seq-measured $K_{D}$ values or (B) Sort-Seq-measured $E$ values. Plots show the relative probability density (over 30 bins along the $K_{D}$ or $E$ axes) observed for variants in each class.

Our observations are thus fully consistent with the hypothesis that the amino acid sequences of the CDR1H and CDR3H regions of the WT scFv have been selected for high affinity binding to fluorescein. We know this to be true, of course; still, this result provides an important validation of our Tite-Seq measurements.

To further validate our Tite-Seq affinity measurements, we examined positions in the high affinity OPT scFv (from [Boder et al., 2000]) that differ from WT and that lie within the 1H and 3H variable regions. As illustrated in Figure 5A and B, five of the six OPT-specific mutations reduce $K_{D}$ or are nearly neutral. Previous structural analysis (Midelfort et al., 2004) has suggested that D106E, the only OPT mutation that we find significantly increases $K_{D}$, may indeed disrupt antigen binding on its own while still increasing affinity in the presence of the S101A mutation.

Next, we used our measurements to build a ‘matrix model’ (also known as a ‘position-specific affinity matrix,’ or PSAM [Foat et al., 2006]) describing the sequence-affinity landscape of these two regions. Our model assumed that the $log_{10}⁡K_{D}$ value for an arbitrary amino acid sequence could be computed from the $log_{10}⁡K_{D}$ value of the WT scFv, plus the measured change in $log_{10}⁡K_{D}$ produced by each amino acid substitution away from WT. We evaluated our matrix models on the 1H and 3H variable regions of OPT, finding an affinity of $10^{-9.16}$ M. Our simple model for the sequence affinity landscape of this scFv therefore correctly predicts that OPT has higher affinity than WT. The quantitative affinity predicted by our model does not match the known affinity of the OPT scFv ($K_{D}=10^{-12.6}$ M), but this is unsurprising for three reasons. First the OPT scFv differs from WT in 14 residues, only 6 of which are inside the 1H and 3H variable regions assayed here. Second, one of the OPT mutations (W108L) reduces $K_{D}$ below our detection threshold of $10^{-9.5}$ M; in building our matrix model, we set this value equal to $10^{-9.5}$, knowing it would likely underestimate the affinity-increasing effect of the mutation. Third, our additive model ignores potential epistatic interactions. Still, we thought it worth asking how likely it it would be for six random mutations within the 1H and 3H variable regions to reduce affinity as much as our model predicts for OPT. We therefore simulated a large number ($10^{7}$) of variants having a total of 6 substitution mutations randomly scattered across the 1H and 3H variable regions. The fraction of these random sequences that had an affinity at or below our predicted affinity for OPT was $4.7\times10^{-5}$. This finding is fully consistent with the fact that the mutations in OPT relative to WT were selected for increased affinity, an additional confirmation of the validity of our Tite-Seq measurements.

The sequence-expression landscape measured in our separate Sort-Seq experiment yielded qualitatively different results (Figure 5C and D). We observed no significant difference in the median effect that mutations in the variable regions of 1H (median $E=0.826$) versus 3H (median $E=0.822$) have on expression ($P=0.96$, two-sided Mann-Whitney U test); see also Figure 5—figure supplement 1. The variance in these effects, however, was larger in 3H than in 1H ($P=9.9\times10^{-16}$, Levene’s test). These results suggest two things. First, the 3H variable region appears to have a larger effect on scFv expression than the 1H variable region has. At the same time, since we observe fewer beneficial mutations in 1H (Figure 5C) than in 3H (Figure 5D), the WT sequence appears to be more highly optimized for expression in CDR1H than in CDR3H. The effect of double or triple mutations further reduced expression in both CDRs (Figure 5—figure supplement 2B), similar to what was observed for affinity.

### Structural correlates of the sequence-affinity landscape

We asked if the sensitivity of the antibody to mutations could be understood from a structural perspective. To quantify sensitivity of affinity and expression at each position $i$, we computed two quantities:

$$
(2)S_{K}^{i}=\sqrt{⟨(log_{10}⁡K_{D}^{ia}−log_{10}⁡K_{D}^{WT})^{2}⟩_{a|i}},(3)S_{E}^{i}=\sqrt{⟨(E^{ia}−E^{WT})^{2}⟩_{a|i}}.
$$

Here, $K_{D}^{WT}$ and $E^{WT}$ respectively denote the dissociation constant and expression level measured for the WT scFv, $K_{D}^{i⁢a}$ and $E^{i⁢a}$ denote analogous quantities for the scFv with a single substitution mutation of amino acid $a$ at position $i$, and $⟨⋅⟩_{a|i}$ denotes an average computed over the 19 non-WT amino acids at that position.

Figure 6A shows the known structure (Whitlow et al., 1995) of the 1H and 3H variable regions of the WT scFv in complex with fluorescein. Each residue is colored according to the SK and SE values computed for its position. To get a better understanding of what aspects of the structure might govern affinity, we plotted SK values against two other quantities: the number of amino acid contacts made by the WT residue within the antibody structure (Figure 6B), and the distance between the WT residue and the antigen (Figure 6C). We found a strong correlation between SK and the number of contacts, but no significant correlation between SK and distance to antigen. By contrast, SE did not correlate significantly with either of these structural quantities (Figure 6D and E).

![Figure 6.](https://cdn.elifesciences.org/articles/23156/elife-23156-fig6-v3.jpg)

**Figure 6.:** (A) Crystal structure (Whitlow et al., 1995) of the CDR1H and CDR3H variable regions of the WT scFv in complex with fluorescein (green). Each residue (CDR1H: positions 28–37; CDR3H: positions 100–109) is colored according to the $S_{K}$ and $S_{E}$ values computed for that position. These variables, $S_{K}$ and $S_{E}$, respectively quantify the sensitivity of $K_{D}$ and $E$ to amino acid substitutions at each position, with larger values corresponding to greater sensitivity; see Equations 2 and 3 for definitions of these quantities. (B,C) For each position in the CDR1H and CDR3H variable regions, $S_{K}$ is plotted against either (B) the number of contacts the WT residue makes within the protein structure, or (C) the distance of the WT residue to the fluorescein molecule. (D,E) Similarly, $S_{E}$ is plotted against either (D) the number of contacts or (E) the distance to the antigen. $R^{2}$ is the coefficient of determination.

## Discussion

We have described a massively parallel assay, called Tite-Seq, for measuring the sequence-affinity landscape of antibodies. The range of affinities measured in our Tite-Seq experiments ($10^{-9.5}$ M to $10^{-5.0}$ M) includes a large fraction of the physiological range relevant to affinity maturation ($10^{-10}$ M to ~10−6 M) (Batista and Neuberger, 1998; Foote and Eisen, 1995; Roost et al., 1995). Expanding the measured range of affinities below $10^{-9.5}$ M might require larger volume labeling reactions, but would be straight-forward. Tite-Seq therefore provides a potentially powerful method for mapping the sequence-affinity trajectories of antibodies during the affinity maturation process, as well as for studying other aspects of the adaptive immune response.

The details of our Tite-Seq experiments (e.g., 11 antigen concentrations, four sorting bins per concentration, etc.) were chosen largely for experimental convenience. The effects of varying these parameters have not been systematically explored, and a future investigation of these effects might be valuable. Figure 4—figure supplement 8 does illustrate, via simulation, the effect of read depth on the precision of measured $K_{D}$ values. These simulations, along with an analysis of synonymous variants (Figure 4—figure supplement 3), suggest that the primary source of noise in our experiments came not from a lack of sorted cells or Illumina reads, but rather from the inefficient post-sort recovery of antibody sequences. We therefore suggest that improvements to our post-sort DNA recovery protocol might substantially improve the resolution of Tite-Seq.

Tite-Seq fundamentally differs from prior DMS experiments in that full binding titration curves, not two-bin enrichment statistics, are used to determine binding affinities. The measurement of binding curves provides three major advantages. First, binding curves provide absolute $K_{D}$ values in molar units, not just rank-order affinities, like those provided by SORTCERY (Reich et al., 2015), or relative affinity ratios, like those provided by the method of Kowalsky and Whitehead (2016). Second, because ligand binding is a sigmoidal function of affinity, DMS experiments performed at a single ligand concentration (e.g., [Kowalsky and Whitehead, 2016]) are insensitive to receptor $K_{D}$s that differ substantially from this ligand concentration. Binding curves, by contrast, integrate measurements over a wide range of concentrations and are therefore sensitive to a wide range of $K_{D}$s.

The third advantage of measuring binding curves pertains to the fact that protein sequence determines not just ligand-binding affinity, but also the quantity and specific activity of surface-displayed proteins. Our data (Figure 4—figure supplement 5 and Figure 4—figure supplement 6) suggest that these confounding effects can be large and that they can distort yeast display affinity measurements computed from enrichment statistics gathered at a single antigen concentration. Strong sequence-dependent effects on both the expression and specific activity of yeast-displayed proteins has been reported by other groups as well (e.g., [Burns et al., 2014]), although the absence of such effects has also been reported (e.g., [Kowalsky and Whitehead, 2016]). Ultimately, the magnitude of these effects is likely to vary substantially from protein to protein. It should also be noted that many DMS studies using yeast display (e.g., epitope mapping studies [Kowalsky et al., 2015; Doolan and Colby, 2015; Van Blarcom et al., 2015]) might not suffer from these potentially confounding effects, and in such cases it probably makes sense to employ a simpler experimental design than is required for Tite-Seq. Nevertheless, either Tite-Seq or other experimental methods that assay full binding curves are probably essential if one wants to quantitatively and reliably measure $K_{D}$ values in a massively parallel fashion.

We wish to emphasize, more generally, that changing a protein’s amino acid sequence can be expected to change multiple biochemical properties of that protein. Our work illustrates the importance of designing massively parallel assays that can disentangle these effects. Tite-Seq provides a general solution to this problem for massively parallel studies of protein-ligand binding. Indeed, the Tite-Seq procedure described here can be readily applied to any protein binding assay that is compatible with yeast display and FACS. Many such assays have been developed (Liu, 2015). We expect that Tite-Seq can also be readily adapted for use with other expression platforms, such as mammalian cell display (Forsyth et al., 2013).

Our Tite-Seq measurements reveal interesting distinctions between the effects of mutations in the CDR1H and CDR3H regions of the anti-fluorescein scFv antibody studied here. As expected, we found that variation in and around CDR3H had a larger effect on affinity than did variation in and around CDR1H. We also found that CDR1H is more optimized for protein expression than is CDR3H, an unexpected finding that appears to be novel. Yeast display expression levels are known to correlate with thermostability (Shusta et al., 1999). Our data is limited in scope, and we remain cautious about generalizing our observations to arbitrary antibody-antigen interactions. Still, this finding suggests the possibility that secondary CDR regions (such as CDR1H) might be evolutionarily optimized to help ensure antibody stability, thereby freeing up CDR3H to encode antigen specificity. If this hypothesis holds, it could provide a biochemical rationale for why CDR3H is more likely than CDR1H to be mutated in functioning receptors (Liberman et al., 2013) and why variation in CDR3H is often sufficient to establish antigen specificity (Xu and Davis, 2000).

Tite-Seq can also potentially shed light on the structural basis for antibody-antigen recognition. By comparing the effects of mutations with the known antibody-fluorescein co-crystal structure (Whitlow et al., 1995), we identified a strong correlation between the effect that a position has on affinity and the number of molecular contacts that the residue at that position makes within the antibody. By contrast, no such correlation of expression with this number of contacts is observed. Again, we are cautious about generalizing from observations made on a single antibody. If our observation were to hold for other antibodies, however, it would suggest that the functional geometry of paratopes might be governed by networks of residues whose positions and orientations are strongly interdependent.

## Materials and methods

Tite-Seq was performed as follows. Variant 3H and 1H regions were generated using microarray-synthesized oligos (LC Biosciences, Houston TX. USA). These were inserted into the 4-4-20 scFv of (Boder and Wittrup, 1997) using cassette-replacement restriction cloning as in (Kinney et al., 2010); see Appendix 3. Yeast display experiments were performed as previously described (Boder et al., 2000) with modifications; see Appendix 2. Sorted cells were regrown and bulk DNA was extracted using standard techniques, and amplicons containing the 1H and 3H variable regions were amplified using PCR and sequenced using the Illumina NextSeq platform; see Appendix 4. Three replicate experiments were performed on different days. Raw sequencing data has been posted on the Sequence Read Archive under BioProject ID PRJNA344711. Low-throughput flow cytometry measurements were performed on clones randomly picked from the Tite-Seq library. Sequence data and flow cytometry data were analyzed using custom Python scripts, as described in Appendices 5 and 6. Processed data and analysis scripts are available at github.com/jbkinney/16_titeseq.

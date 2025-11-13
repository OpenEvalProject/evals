# CDK9-dependent RNA polymerase II pausing controls transcription initiation

## Authors

- Saskia Gressel<sup>1</sup> ([ORCID: 0000-0003-0261-675X](https://orcid.org/0000-0003-0261-675X))
- Björn Schwalb<sup>1</sup> ([ORCID: 0000-0003-2987-2622](https://orcid.org/0000-0003-2987-2622)) †
- Tim Michael Decker<sup>2</sup>
- Weihua Qin<sup>3</sup>
- Heinrich Leonhardt<sup>3</sup>
- Dirk Eick<sup>2</sup> †
- Patrick Cramer<sup>1</sup> ([ORCID: 0000-0001-5454-7755](https://orcid.org/0000-0001-5454-7755)) †

### Affiliations

1. Department of Molecular Biology Max-Planck-Institute for Biophysical Chemistry Göttingen Germany
2. Department of Molecular Epigenetics Helmholtz Center Munich, Center of Integrated Protein Science Munich Germany
3. Department of Biology II Ludwig-Maximilians-Universität München, Center of Integrated Protein Science Martinsried Germany

† Corresponding author

## Abstract

Gene transcription can be activated by decreasing the duration of RNA polymerase II pausing in the promoter-proximal region, but how this is achieved remains unclear. Here we use a ‘multi-omics’ approach to demonstrate that the duration of polymerase pausing generally limits the productive frequency of transcription initiation in human cells (‘pause-initiation limit’). We further engineer a human cell line to allow for specific and rapid inhibition of the P-TEFb kinase CDK9, which is implicated in polymerase pause release. CDK9 activity decreases the pause duration but also increases the productive initiation frequency. This shows that CDK9 stimulates release of paused polymerase and activates transcription by increasing the number of transcribing polymerases and thus the amount of mRNA synthesized per time. CDK9 activity is also associated with long-range chromatin interactions, suggesting that enhancers can influence the pause-initiation limit to regulate transcription.

## Introduction

Transcription in metazoan cells is often regulated at the level of promoter-proximal pausing (Core et al., 2008; Day et al., 2016; Henriques et al., 2013; Nechaev et al., 2010; Rougvie and Lis, 1988; Strobl and Eick, 1992), which can be detected by measuring the occupancy with paused Pol II by ChIP-seq (Johnson et al., 2007), GRO-seq (Core et al., 2008), (m)NET-seq (Mayer et al., 2015; Nojima et al., 2015), or PRO-seq (Kwak et al., 2013). Genes with paused Pol II are conserved across mammalian cell types and states (Day et al., 2016). The mechanisms underlying how Pol II pausing can regulate RNA transcript synthesis remain unclear.

Transcription of a human protein-coding gene of average length takes at least half an hour to be completed. The duration of pausing however lies in the range of minutes (Jonkers et al., 2014) and does not considerably change the overall time it takes to complete a transcript. Thus, how can changes in the pause duration lead to synthesis of a different number of RNA transcripts per time? It has been suggested that a decreased pause duration goes along with a higher initiation frequency, because occupancy peaks for promoter-proximal Pol II can increase upon gene activation (Boehm et al., 2003) or can remain high even when pausing is impaired (Henriques et al., 2013).

The height of Pol II occupancy peaks however cannot directly inform on initiation frequency or pause duration because it depends not only on the number of polymerases that pass the pause site but also on their residence time (Ehrensberger et al., 2013). A kinetic model of transcription predicted that pause duration delimits the initiation frequency and suggested that paused Pol II sterically interferes with initiation (Ehrensberger et al., 2013). Indeed, modeling reveals that a paused polymerase positioned up to around 50 bp downstream of the TSS could sterically interfere with formation of the Pol II initiation complex (Figure 1—figure supplement 1). Even if a paused polymerase is located further downstream, it may still interfere with initiation if one or more additional elongating polymerases line up behind it.

The critical relationship between pausing and initiation could thus far not be tested experimentally, as no methods were available to measure initiation frequencies. A recently developed method, transient transcriptome sequencing (TT-seq) (Schwalb et al., 2016), now allows to unveil the flow of polymerases as it measures local RNA synthesis rates genome-wide at nucleotide resolution.

Here we investigate whether changes in pause duration alter initiation frequency in living cells. We specifically inhibit the kinase CDK9, which facilitates Pol II pause release (Laitem et al., 2015; Marshall and Price, 1992; Peterlin and Price, 2006), and monitor RNA synthesis and initiation frequencies by TT-seq. A combination of TT-seq data with mNET-seq data allows us to derive pause durations for active genes. We conclude that the duration of pausing can control transcription initiation at human genes, and derived determinants for CDK9-dependent pause release and initiation activation.

## Results

### CRISPR-Cas9-engineered mutation allows for specific CDK9 inhibition

To specifically inhibit CDK9, we used a chemical biology approach (Lopez et al., 2014) that circumvents off-target effects of standard CDK9 inhibitors (Morales and Giordano, 2016). We introduced a CDK9 analog sensitive mutation (CDK9as) into human Raji B cells by CRISPR-Cas9 (Materials and methods, Figure 1—figure supplement 2A–B). This allows for rapid and highly specific CDK9 inhibition with the adenine analog 1-NA-PP1 (Lopez et al., 2014), which does not have any effect on wild type cells (Figure 1—figure supplement 2C). CDK9 protein levels were unchanged in CDK9as mutant cells compared to wild type cells (Figure 1—figure supplement 2D). After 72 hr of incubation with 1-NA-PP1, growth of CDK9as cells ceased, whereas wild type cells grew normally (Figure 1—figure supplement 2E).

### TT-seq monitors immediate response to CDK9 inhibition

We treated CDK9as cells with 5 μM of 1-NA-PP1 for 10 min and monitored changes in RNA synthesis by TT-seq (Schwalb et al., 2016), using a RNA labeling time of 5 min (Figure 1A). TT-seq data were highly reproducible (Spearman correlation coefficient 1) and monitored transcription activity before and after CDK9 inhibition (Figure 1B). CDK9 inhibition resulted in reduced TT-seq signals at the beginning of genes, indicating that less Pol II was released into gene bodies (Figure 1B, Figure 2—figure supplement 1A–B). This gave rise to a ‘response window’ revealing the distance traveled by Pol II during 10 min inhibitor treatment (Figure 1C). Downstream of the response window, the TT-seq signal was largely unchanged, indicating continued RNA synthesis from Pol II elongation complexes that had been released before CDK9 inhibition.

![Figure 1.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig1-v2.jpg)

**Figure 1.:** (A) Experimental design. TT-seq was carried out with CDK9as cells after treatment with solvent DMSO (control) or 1-NA-PP1 (CDK9as inhibited). (B) TT-seq signal before (black) and after (red) CDK9 inhibition at the ABHD17C gene locus (75,937 [bp]) on chromosome 15. Two biological replicates were averaged. The grey box depicts the transcript body from the transcription start site (TSS, black arrow) to the polyA site (pA). (C) Schematic representation of changes in TT-seq signal showing the definition of the response window. Colors are as in (B). (D) Metagene analysis comparing the average TT-seq signal before and after CDK9 inhibition. The TT-seq coverage was averaged for 954 out of 2538 investigated TUs that exceed 50 [kbp] in length (Materials and methods). TUs were aligned with their TSS. Shaded areas around the average signal (solid lines) indicate confidential intervals (Materials and methods). (E) Violin plot showing the relative response to CDK9 inhibition for 2538 investigated TUs defined as 1 - (CDK9as inhibited/Control)$∙$100 for a window from the TSS to 10 [kbp] downstream, excluding the first 200 [bp] (C). A red line indicates the median response (58%).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Modeling shows that paused Pol II (silver, right) positioned 50 bp downstream of the transcription start site (TSS) allows for formation of the Pol II initiation complex (different colors, left). Shorter distances between the active sites of paused and initiating Pol II are predicted to lead to steric clashes. Modeling is based on the latest structural information (Mediator EMD-8307 [Robinson et al., 2016], TFIID EMD-3305 [Louder et al., 2016], TFIIH EMD EMD-3307 [He et al., 2016], closed complex PDB-code 5FZ5 [Plaschka et al., 2016], EC PDB-code 1WCM [Kettenberger et al., 2004]).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) BstUI restriction enzyme recognition site used for screening is indicated in the HDR template sequence (highlighted in red). Agarose gels of screening PCRs followed by restriction digest with BstUI of wild type (wt) and CDK9as (as) Raji B cell line. (B) Validation of CDK9as Raji B cell line by sequencing. (C) Log fold change upon 1-NA-PP1 treatment (5 µM for 15 min) versus the normalized mean read count across replicates and conditions for wild type Raji B cells (left panel) and CDK9as Raji B cells (right panel). Significantly up- or downregulated TUs (adjusted p-value<0.01) are marked in red. (D) Wild type and CDK9as Raji B cells were treated with 10 µM of 1-NA-PP1 for 15 min or 2 hr. DMSO was used as control. Stable CDK9 protein levels were detected by Western blotting (Materials and methods). α-Tubulin was used as loading control. (E) Cell proliferation at increasing 1-NA-PP1 inhibitor concentrations (log scale) was determined using a colorimetric assay based on MTS metabolization (Materials and methods). Cell proliferation of CDK9as Raji B cells was dramatically reduced by >50% when 1-NA-PP1 concentrations of 5 µM (indicated with dashed red line) or higher were used, whereas wild type Raji B cells were largely unaffected. Error bars indicate the standard deviation (n = 4).

To determine the relative response of genes to CDK9 inhibition, we calculated response ratios for those transcribed units (TUs, Materials and methods) that synthesized RNA, harbored a single TSS, and exceeded 10 kbp in length (2,538 TUs). The response ratio of TUs varied between 0% to 100% (fully responding TUs) with a median of 58% (Figure 1C–E). A remaining TT-seq signal in the response window likely reflects the proportion of polymerases that move to productive elongation without CDK9 kinase activity, but we cannot exclude that it stems from incomplete CDK9 inhibition. However, based on the assumption that the inhibitor is evenly distributed across cells and within, the portion of CDK9 that has not been fully inhibited must be very low.

### Pol II elongation velocity is gene-specific

The width of the response window differs between TUs (Figure 1D) and informs on Pol II elongation velocity (Materials and methods). The average width of the response window was 23 kbp, and thus the average elongation velocity was 2.3 kbp/min (Figure 2A–B), which agrees with previous estimates (Fuchs et al., 2014; Jonkers et al., 2014; Saponaro et al., 2014; Veloso et al., 2014). Gene-specific elongation velocities (Figure 2C, Figure 2—figure supplement 1A–B) were significantly higher in TUs with longer first introns (Figure 2D, Wilcoxon rank sum test, p-value<1.916·10−11), consistent with faster transcription of introns (Jonkers et al., 2014). Elongation velocity correlated positively with nucleosome density, and negatively with the stability of the DNA-RNA hybrid, CpG density and topoisomerase occupancy (Figure 2—figure supplement 1C).

![Figure 2.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig2-v2.jpg)

**Figure 2.:** (A) Schematic representation of observed response window of TT-seq signal with CDK9as inhibitor (red) or control (black) for TUs of three different length classes (short TUs < 25 [kbp], medium-length TUs 25–50 [kbp] and long TUs > 100 [kbp]). (B) Scatter plot of the ratio of transcribed bases (CDK9as inhibited/control) (Materials and methods) against the length of the TUs in nucleotides [kbp] revealed that the schematic representation in (A) holds true for 2443 investigated TUs (Materials and methods). Modeling of the observed relation allows estimation of a robust average elongation velocity of 2.3 [kbp/min] (solid black line, Materials and methods). (C) Distribution of gene-wise elongation velocity depicted as a histogram (mean 2.7 [kbp/min], median 2.4 [kbp/min]). (D) Distributions of elongation velocity [kbp/min] depicted for 513 TUs with short first intron (<50% quantile, left) and 514 TUs with long first intron (>50% quantile, right).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) YWHAQ gene locus (47,042 [bp]) on chromosome 2. The upper panel shows TT-seq signal with CDK9as inhibitor (red) and control (black). Grey box depicts transcript body from transcription start site (TSS, black arrow) to polyA site (pA). Lower panel shows the difference of TT-seq signal (control – CDK9as inhibited in blue). Black rectangle depicts the estimated response window according to elongation velocity estimate (Materials and methods). (B) HEATR3 gene locus (40,446 [bp]) on chromosome 16 depicted as in (A). (C) Color encoded Spearman correlation coefficients (color encoded, −0.45 in blue to 0.21 in red) of elongation velocity [kbp/min] against genomic features and measures of transcriptional context (Materials and methods, Supplementary file 1).

### Promoter-proximal pausing occurs at sequences that give rise to weak DNA-RNA hybrids

To study the kinetics of CDK9-dependent Pol II pause release, we generated mNET-seq data that map the RNA 3’-end of engaged Pol II and extracted the position of paused polymerases (Materials and methods). mNET-seq data were highly reproducible (Spearman correlation coefficient 0.93). Of the above TUs, 2135 (84 %) showed mNET-seq signal peaks above background (Materials and methods). The called pause sites were distributed around a maximum located ~84 bp downstream of the TSS (Figure 3A, Figure 3—figure supplement 1A). At these sites we detected an enrichment for G/C-C/G dinucleotides (Figure 3—figure supplement 1B) with a strongly conserved cytosine at the RNA 3’-end (Figure 3B). We also observed a minimum of the predicted melting temperature of the DNA-RNA hybrid (Materials and methods) immediately downstream of the pause site (Figure 3C). A weak DNA-RNA hybrid in the active center of Pol II is known to destabilize the elongation complex (Kireeva et al., 2000), and could be a major determinant for establishing the paused state.

![Figure 3.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig3-v2.jpg)

**Figure 3.:** (A) Distribution of pause site distance from the TSS for 2135 investigated TUs depicted as a histogram (mean 128 [bp], median 112 [bp], mode 84 [bp]). Two biological replicates were averaged. (B) Position weight matrix (PWM) logo representation of bases at positions –10 to +10 [bp] around the pause site (position 0). (C) Mean melting temperature of the DNA-RNA and DNA-DNA hybrid aligned at the TSS and the pause site (signal between the TSS and the pause site is scaled to common length of 100 [bp]). Shaded areas around the average signal (solid lines) indicate confidence intervals.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Distributions of pause site depicted as densities for TUs with a response ratio >75% quantile (574 TUs, red) and TUs with a response ratio <25% quantile (469 TUs, black). (B) Plot showing the top 5 enriched 2-mers found by comparing the frequency of all possible 2-mers in a window of ±10 bp around the estimated pause site for fixed positions. Testing was done via Fisher’s exact test against the (background) frequency of the respective 2-mer obtained from a window of the same size shifted 500 bp downstream. The respective p-values and odd-ratios are given in the left and right panel.

### Multi-omics analysis provides pause duration d and initiation frequency I

To quantify pausing, we defined the pause duration d as the time a polymerase needs to pass through a 200 bp ‘pause window’ located ±100 bp around the pause site. The pause duration d can now be derived from a combination of mNET-seq and TT-seq data. In particular, the mNET-seq signal corresponds to the number of polymerases in the pause window, which is determined by d and by the initiation frequency I (Figure 4A) (Ehrensberger et al., 2013). Thus, d is proportional to the ratio of the mNET-seq signal over I. To calculate I we integrated TT-seq signals over exons, excluding the first exon (Materials and methods). This provides the ‘productive initiation frequency’, that is the number of polymerases that initiate and successfully exit from the pause window. We use the term ‘productive’ because we do not know whether there is a small fraction of polymerases terminating within the pause window. Finally, to derive absolute values of d, we scaled the reciprocal of d (the elongation velocity in the pause window) according to the elongation velocity obtained from CDK9 inhibition (Materials and methods).

![Figure 4.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig4-v2.jpg)

**Figure 4.:** (A) Schematic representation of polymerase flow in the promoter-proximal region. The mNET-seq signal (top) is the ratio of the initiation frequency I over the elongation velocity v. The TT-seq signal (bottom) corresponds to initiation frequency I. Thus, v can be derived from the ratio of the TT-seq over the mNET-seq signal, and the reciprocal of v in the pause window corresponds to the pause duration d. (B) Distributions of gene-wise pause duration d [min] for TUs with a CDK9 response ratio >75% quantile (574 TUs) and TUs with a response ratio <25% quantile (469 TUs). (C) Distributions of gene-wise initiation frequency I [cell−1min−1] for TUs with a CDK9 response ratio >75% quantile (635 TUs) and TUs with a response ratio <25% quantile (635 TUs). (D) Scatter plot between the initiation frequency I [cell−1min−1] and the pause duration d [min] for 2135 common TUs with color-coded density estimation. The grey shaded area depicts impossible combinations of I and d according to published kinetic theory (Ehrensberger et al., 2013) and assuming that steric hindrance occurs below a distance of 50 [bp] between the active sites of the initiating Pol II and the paused Pol II.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Simulation of labeled RNA fragments synthesized in 5 min labeling duration (TT-seq fragments depicted for polymerases with a distance corresponding to 40 s of elongation, middle panel) for a pause site 80 bp downstream of the TSS with a given elongation velocity profile [bp min−1] comprising a pause duration of 1 min (upper panel) and a initiation frequency of 0.5 [cell−1min−1]. Lower panel shows the resulting TT-seq coverage. Shorter fragments have a higher probability to escape labeled RNA purification and can not be recovered fully. (B) Simulation of labeled RNA fragments as in (A) with two times the initiation frequency (1 [cell−1min−1]) and a promoter-proximal termination of every second polymerase. The resulting TT-seq coverage (lower panel) shows less effect (higher coverage) upstream of the pause site. For reasons of simplicity the promoter-proximal termination of every second polymerase is modeled by overlaying two simulation instances with an initiation frequency of 0.5 [cell−1min−1]. One as in (A) and one with a constantly terminating polymerase. Note that polymerases that terminate in the pause window do not contribute signal to the region downstream of the pause site. (C) Simulation of labeled RNA fragments as in (A) with a pause duration of 2 min (upper panel) leading to a greater shortage of labeled RNA in the region between the TSS and the pause site. (D) Schematic representation of coverage ratio calculation for real TT-seq coverage. (E) Distributions of gene-wise uridine content in the region between the TSS and the pause site for TUs with a response ratio >75% quantile (603 TUs) and TUs with a response ratio <25% quantile (527 TUs). (F) Distributions of gene-wise mean real TT-seq signal in the region between the TSS and the pause site normalized to initiation frequency for subsets as in (E).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Scatter plot comparing the initiation frequency [cell−1min−1] against the pause duration [min] for 2135 common TUs with color encoding according to mNETseq signal strength (weak in white to strong in blue). The grey shaded area depicts impossible combinations of I and d according to published kinetic theory (Ehrensberger et al., 2013) and assuming that steric hindrance occurs below a distance of 50 bp between the active sites of the initiating Pol II and the paused Pol II. (B) Schematic representation of polymerase flow in the promoter-proximal region. The number of polymerases in a region of interest (mNET-seq signal, top) corresponds to the average elongation velocity v in that region. The width of the response window (TT-seq signal, bottom) informs on Pol II elongation velocity v. The pause duration $d^$ can be derived (without the initiation frequency I) as the reciprocal of v in the pause window. The elongation velocity v in the pause window relates directly to v in the response window which can be adjusted to the elongation velocity obtained from CDK9 inhibition (Materials and methods). (C) Scatter plot revealing an anti-correlation between the initiation frequency I [cell−1min−1] and the pause duration $d^$ [min] for 974 common TUs with color-coded density estimation (Spearman correlation coefficient −0.3). The grey shaded area depicts impossible combinations of I and $d^$ according to published kinetic theory (Ehrensberger et al., 2013). (D) Density showing the spearman correlation coefficient of pause duration $d^$ and initiation frequency I for repeated randomly shuffled mNET-seq signal assignment to TUs. Original spearman correlation coefficient is indicated with a red line. (E) Distributions of gene-wise pause duration $d^$ [min] for TUs with a CDK9 response ratio >75% quantile (155 TUs) and TUs with a response ratio <25% quantile (271 TUs). (F) Density showing the number of impossible combinations of pause duration $d^$ and initiation frequency I (above pause-initiation limit) for repeated randomly shuffled mNET-seq signal assignment to TUs. Original observation is indicated with a red line.

We obtained a mean productive initiation frequency of 2.7 polymerases cell−1min−1, and pause durations in the range of minutes, with strong variations between TUs. The pause durations are generally consistent with reported half-lives of paused Pol II in mouse (Jonkers et al., 2014) and Drosophila cells (Buckley et al., 2014; Henriques et al., 2013) but slightly shorter. Pause durations were also consistent with kinetic modeling of TT-seq data alone. At TUs with long pause durations we observed less labeled RNA in the short region between the TSS and the pause site (Figure 4—figure supplement 1). This confirms that indeed initiation frequencies are altered. It also indicates that the fraction of Pol II enzymes that terminate within the pause window is low, in agreement with previous findings (Henriques et al., 2013). For strongly CDK9-responding TUs, we obtained a significantly longer pause duration (Wilcoxon rank sum test, p-value<10−12) and lower initiation frequencies (Figure 4B–C).

### Human genes have a ‘pause-initiation limit’

These results prompted us to ask whether the pause duration is generally related to the initiation frequency. We indeed found a robust anti-correlation between I and d in normally growing cells, and an upper boundary for combinations of I and d which we call ‘pause-initiation limit’. (Figure 4D, Figure 4—figure supplement 2A). Thus, genes with shorter pausing show higher initiation frequencies and more RNA synthesis. This fundamental relationship can be verified by calculating the pause duration $d$ without the initiation frequency I, $d^$ (Materials and methods, Figure 4—figure supplement 2B–C,E). Repeated random shuffling of mNET-seq signal assignment to TUs abolishes the correlation between $d^$ and I (Figure 4—figure supplement 2D). It also shows that the observation of impossible combinations of pause duration $d^$ and initiation frequency I (points above ‘pause-initiation limit’) are minimal (Figure 4—figure supplement 2F). In conclusion, independent mNET-seq and TT-seq data led to independent measures of pause duration and productive initiation frequency for each gene, which were then observed to be globally anti-correlated.

These findings now allowed us to test directly whether longer pause durations lead to lower initiation frequencies, by analyzing TT-seq data after CDK9 inhibition. CDK9 inhibition resulted in significantly reduced labeled RNA in the short region between the TSS and the pause site (Wilcoxon rank sum test, p-value<10−16) (Figure 5A–B). Productive initiation frequencies were significantly downregulated after CDK9 inhibition (Wilcoxon rank sum test, p-value<10−16) (Figure 5C). Because CDK9 specifically targets paused Pol II, and not initiating polymerase, these results show that pausing limits initiation, and not the other way around. Thus, human genes have a ‘pause-initiation limit’.

![Figure 5.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig5-v2.jpg)

**Figure 5.:** (A) Schematic representation of observed decrease in TT-seq signal upon CDK9 inhibition, upstream and downstream of the pause site. (B) Distributions of gene-wise mean TT-seq signals in the region between the TSS and the pause site, before (control) and after CDK9 inhibition, normalized to the initiation frequency before CDK9 inhibition. (C) Distributions of gene-wise initiation frequencies before (control) and after CDK9 inhibition.

To monitor the occupancy of engaged Pol II we generated mNET-seq data before and after CDK9 inhibition (Materials and methods). CDK9 inhibition resulted in increased mNET-seq signal at the beginning of genes and decreased signal in the gene body, indicating that less Pol II was released from the pause site (Figure 6A). Indeed, calculation of pause durations from mNET-seq and TT-seq data after CDK9 inhibition showed that Pol II resides significantly longer at the pause site after CDK9 inhibition (Wilcoxon rank sum test, p-value<10−16) (Figure 6B). Taken together, CDK9 inhibition increases the pause duration and decreases the initiation frequency at human genes (Figure 6C–D).

![Figure 6.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig6-v2.jpg)

**Figure 6.:** (A) Metagene analysis comparing the average mNET-seq signal before and after CDK9 inhibition. Two biological replicates were averaged. The mNET-seq coverage was averaged for 2538 investigated TUs (Materials and methods). TUs were aligned with their TSS. Shaded areas around the average signal (solid lines) indicate confidentiality intervals (Materials and methods). (B) Distributions of gene-wise pause duration d [min] before (control) and after CDK9 inhibition. (C) Scatter plot between the initiation frequency I [cell−1min−1] and the pause duration d [min] after CDK9 inhibition for 2135 common TUs with color-coded density estimation. The grey shaded area depicts impossible combinations of I and d (Ehrensberger et al., 2013) assuming that steric hindrance occurs below a distance of 50 [bp] between the active sites of the initiating Pol II and the paused Pol II. (D) Schematic of changes in pause duration (Δd) and initiation frequency (ΔI) upon CDK9 inhibition. As a consequence, data points in panel (D) are moved to the left and upwards.

### Determinants of promoter-proximal pausing

To investigate possible reasons for polymerase pausing and its consequences, we compared different properties of TUs with long and short pause durations. For the 5’-region of TUs with longer pause durations, the transcript adopts more RNA secondary structure in vivo and in silico (Wilcoxon rank sum test, p-value<10−16) (Figure 7A, Figure 7—figure supplement 1A) (Rouskin et al., 2014). TUs with longer pause durations were also enriched for hyper-methylated CpG islands (ENCODE Project Consortium, 2012) upstream of the pause site (Figure 7B), consistent with a previous report (Hendrix et al., 2008). Comparison of strongly and weakly CDK9-responding TUs around the pause site showed that TUs that responded strongly to CDK9 inhibition showed a higher tendency to establish long-range chromatin interactions (Figure 7C) as observed by Hi-C (Ma et al., 2015). This is consistent with the idea that interactions of an enhancer with its target promoter can stimulate Pol II pause release (Ghavi-Helm et al., 2014; Rahl et al., 2010). This tendency however seems to be independent of the pause duration as comparing TUs with long and short pause durations leads to no observable difference in Hi-C signal.

![Figure 7.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig7-v2.jpg)

**Figure 7.:** (A) Distribution of gene-wise mean in vivo DMS-seq signals (detecting RNA secondary structure) for a window between −65 and −15 [bp] upstream of the pause site for TUs with long pause durations (pause duration >75% quantile, 534 TUs) and with short pause durations (pause duration <25% quantile, 534 TUs) normalized to denatured DMS-seq coverage (Materials and methods). (B) Metagene analysis comparing the average Bisulfite-seq signal (detecting methylated DNA) for subsets as in (A) aligned at the pause site (red, long pause duration, and black, short pause duration). Shaded areas around the average signal (solid lines) indicate confidence intervals. (C) Metagene analysis comparing the average Hi-C signal (detecting long-range chromatin interactions) for strongly CDK9-responding TUs (red, response ratio >75% quantile, 552 TUs) and weakly CDK9-responding TUs (black, response ratio <25% quantile, 440 TUs) aligned at the pause site. Shaded areas around the average signal (solid lines) indicate confidence intervals (Materials and methods, Supplementary file 1).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/29736/elife-29736-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Distributions of gene-wise mean minimum free energy (Materials and methods) for a window of [−15,–65] bp upstream of the pause site for TUs with long pause durations (pause duration >75% quantile, 534 TUs) and TUs with short pause durations (pause duration <25% quantile, 534 TUs). (B) Heatmap showing the pairwise Spearman correlation (color encoded, −0.12 in blue to 0.15 in red) using ChIP measurements of Pol II phospho-isoforms S2P, S5P, S7P and T1P in the pause window against the pause duration in three different variants: ChIP measurements normalized to productive initiation rate (initiation rate), normalized to total Pol II (Pol II), raw signal (raw). (C) Heatmap as in (B) using ChIP measurements of CDK9, NELFe and Brd4 (color encoded, −0.19 in blue to 0.22 in red) (Supplementary file 1).

Finally, we investigated which factors preferentially occupy pause windows with longer pause durations. This is now possible because ChIP-seq signals can be normalized with the productive initiation frequency. Without such normalization, ChIP-seq derived factor occupancies are artificially high in pause windows with long pause durations (Ehrensberger et al., 2013). Correlation of such normalized ChIP-seq signals in the pause window with pause durations (Figure 7—figure supplement 1B–C) resulted in a positive correlation for Pol II phosphorylation at sites that are associated with elongation, and also for NELF-E, CDK9, and Brd4, which are all factors involved in Pol II pausing and release.

## Discussion

Taken together, our results show that Pol II pausing can control transcription initiation and demonstrate the central role of CDK9 in controlling pause duration and thereby the productive initiation frequency. Our results have implications for understanding gene regulation. Genes that show initiation frequencies below the pause-initiation limit may be activated by increasing the initiation frequency without changing pause duration. However, activation of genes that are transcribed at the pause-initiation limit requires a decrease in pause duration, that is stimulation of pause release, to enable higher initiation frequencies. We suggest that pause-controlled initiation evolved because mutations in the promoter-proximal region can change pause duration, and thereby limit initiation, but do not compromise a high initiation capacity of the core promoter around the TSS. This may have enabled the evolution of genes that remain highly inducible but can be efficiently downregulated.

After our work had been completed, a publication appeared that concluded that polymerase pausing inhibits new transcription initiation (Shao and Zeitlinger, 2017). The conclusion in this paper is consistent with our general finding of an interdependency of Pol II pausing and transcription initiation, but the two studies differ in three aspects. First, we used human cells whereas the published work was conducted in Drosophila cells. Second, our work uses a multi-omics approach to enable a kinetic description, whereas the published work is based on changes in factor occupancy. Third, we selectively inhibited CDK9 using CRISPR-Cas9-based engineering and chemical biology, whereas the published work used small molecule inhibitors that may target multiple kinases. Despite these differences, the general conclusion that promoter-proximal pausing of Pol II sets a limit to the frequency of transcription initiation holds for both human and Drosophila cells and is likely a general feature of metazoan gene regulation.

## Materials and methods

### Key resources table

<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cell line (Homo sapiens; male)</td>
      <td>Raji B lymphocyte cells (wild type)</td>
      <td>DSMZ</td>
      <td>DSMZ Cat# ACC-319; RRID:CVCL_0511</td>
      <td></td>
    </tr>
    <tr>
      <td>cell line (Homo sapiens; male)</td>
      <td>Raji B lymphocyte cells (CDK9as)</td>
      <td>This paper</td>
      <td></td>
      <td>Raji B cells were obtained from DSMZ Cat# ACC-319, RRID:CVCL_0511. Homozygous mutation of F103 at the CDK9 gene loci in Raji B cells was performed using the CRISPR-Cas9 system.</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>anti-CDK9</td>
      <td>Santa Cruz, Dallas, TX USA</td>
      <td>sc-484</td>
      <td></td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>anti-alpha-tubulin</td>
      <td>Sigma-Aldrich, St. Louis, MO USA</td>
      <td>DM1A</td>
      <td></td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>anti-Pol II (total, unphos + phos)</td>
      <td>BIOZOL, Eching, Germany</td>
      <td>MABI0601</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>CellTiter 96 AQueous One Solution Cell Proliferation Assay (MTS)</td>
      <td>Promega, Madison, WI USA</td>
      <td>G3582</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>Plasmo Test Mycoplasma Detection Kit</td>
      <td>InvivoGen, San Diego, CA USA</td>
      <td>rep-pt1</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>Ovation Universal RNA-Seq System</td>
      <td>NuGEN, Leek, The Netherlands</td>
      <td>0343–32</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>TruSeq Small RNA Library Prep Kit</td>
      <td>Illumina, Massachusetts USA</td>
      <td>RS-200–0012</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>CDK9as inhibitor; 1-NA-PP1</td>
      <td>Calbiochem, EMD Millipore, Danvers, MA USA</td>
      <td>529579</td>
      <td>CAS 221243-82-9</td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>Solvent control; DMSO</td>
      <td>Sigma-Aldrich, St. Louis, MO USA</td>
      <td>D8418</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>4-thiouracil (4sU)</td>
      <td>Sigma-Aldrich, St. Louis, MO USA</td>
      <td>T4509</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>empigen BB detergent</td>
      <td>Sigma-Aldrich, St. Louis, MO USA</td>
      <td>30326</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cell lines and cell culture

Raji B cells were obtained from DSMZ (DSMZ no.: ACC 319; RRID:CVCL_0511). CDK9as Raji B cells were generated in this study by CRISPR-Cas9-based engineering of Raji B cells obtained from DSMZ (DSMZ no.: ACC 319; RRID:CVCL_0511). Raji B cells and CDK9as Raji B cells were grown in RPMI 1640 medium (Thermo Fisher Scientific, Waltham, MA USA) supplemented with 10% foetal calf serum (bio-sell, Nürnberg, Germany), 100 U/mL penicillin and 100 µg/mL streptomycin (Thermo Fisher Scientific, Waltham, MA USA), and 2 mM L-glutamine (Thermo Fisher Scientific, Waltham, MA USA) at 37°C and 5% CO2. Cells were verified to be free of mycoplasma contamination using Plasmo Test Mycoplasma Detection Kit (InvivoGen, San Diego, CA USA).

### Generation of human CDK9asRaji B cell line

CDK9as contains a point mutation of the so-called gatekeeper residue that enables the kinase active site to accept bulky ATP analogs (1-NA-PP1) (4-Amino-1-tert-butyl-3-(1ʹ-naphthyl)pyrazolo[3,4-d]pyrimidine). To identify the gatekeeper residue (Lopez et al., 2014), the amino acid sequence of the human CDK9 kinase (UniProt, P50750-1) was aligned with sequences of previously characterized kinases carrying analog sensitive mutations. Multiple sequence alignment was performed with the web tool Clustal Omega 1.2.4 (Sievers et al., 2011). For the canonical isoform of CDK9, phenylalanine (F) 103 was identified as the gatekeeper residue and selected for mutation to alanine (A). Mutation of F103 at the CDK9 gene loci in Raji B cells was performed using the CRISPR-Cas9 system (Doudna and Charpentier, 2014; Hsu et al., 2014) as described (Mulholland et al., 2015) with minor modifications. Briefly, the single guide RNA (sgRNA) for editing CDK9 was designed by using the web tool Optimized CRISPR design (http://crispr.mit.edu/), and was incorporated to pSpCas9(BB)−2A-GFP (PX458) vector by BpiI restriction sites (Addgene plasmid # 48138) (Ran et al., 2013). For nucleotide replacement (gttc to cgcg), 200 nt single-stranded DNA oligonucleotides (ssODNs) were synthesized by Integrated DNA Technologies (IDT, Leuven, Belgium) and used as homology-directed repair (HDR) template. A BstUI cutting site was incorporated into the HDR template for screening. The vector and HDR template were introduced into human Raji B cells using Amaxa Mouse ES Cell Nucleofector Kit (Lonza, Basel, Switzerland) according to the manufacturer’s instructions. Two days after transfection, GFP positive cells were single cell sorted into 96 well plates using FACS Aria II instrument (Becton Dickinson, Franklin Lakes, NJ USA). After two weeks, individual colonies were expanded for genomic DNA isolation. The mutant lines were validated by PCR using respective primers, BstUI digestion (Figure 1—figure supplement 2A) and DNA sequencing (Figure 1—figure supplement 2B).

HDR template (A103 is underlined, BstUI cutting site in small letters):

AAAGTGTGTTGGGTGTGGTTTTCTTGACTTTTTCTTCTTTCTATTCCTGCCTCAGCTTCCCCCTATAACCGCTGCAAGGGTAGTATATACCTGGTcgcgGACTTCTGCGAGCATGACCTTGCTGGGCTGTTGAGCAATGTTTTGGTCAAGTTCACGCTGTCTGAGATCAAGAGGGTGATGCAGATGCTGCTTAACGGCCT

Primers for sgRNA generation and screening:

CDK9-sgRNA-F: 5’-CACCGGCTCGCAGAAGTCGAACACC-3’

CDK9-sgRNA-R: 5’-AAACGGTGTTCGACTTCTGCGAGCC-3’

CDK9-screen-F: 5’-CCCCGTAGCTGGTGCTTCCTCG-3’

CDK9-screen-R: 5’-CCCCAGCAGCCTTCATGTCCCTAT-3’

### Antibodies and western blot analysis

Proteins equivalent to 1 × 105 Raji B cells were loaded in Laemmli buffer and subjected to SDS-PAGE before transfer to nitrocellulose. Unspecific binding of antibodies was blocked by incubation of the membrane with 5% milk in Tris-buffered saline containing 1% Tween. Primary antibodies were anti-CDK9 (sc-484) (Santa Cruz, Dallas, TX USA) and anti-α-tubulin (DM1A) (Sigma-Aldrich, St. Louis, MO USA). Fluorophore-coupled secondary antibodies (Rockland Immunochemicals Inc., Pottstown, PA USA) were used and blots were visualized using the Odyssey system (LI-COR, Lincoln, NE USA).

### MTS assay

Cell proliferation at increasing 1-NA-PP1 inhibitor concentrations was measured in four biological replicates using the CellTiter 96 AQueous One Solution Cell Proliferation Assay System (Promega, Madison, WI USA). Cells were seeded in a 96-well plate and increasing concentrations of 1-NA-PP1 (Calbiochem, EMD Millipore, Danvers, MA USA) or DMSO (Sigma-Aldrich, St. Louis, MO USA) were added. After 72 hr, MTS tetrazolium compound was added to each well for one hour. Subsequently, the quantity of the MTS formazan product was measured as absorbance at 490 nm with a Sunrise photometer (TECAN, Männedorf, Switzerland) that was operated using the Magellan data analysis software (v7.2, TECAN, Männedorf, Switzerland). Relative signals for each concentration were calculated by dividing the signals of the CDK9as inhibitor treated cells by the corresponding signals of the control.

### TT-seq

Two biological replicates of reactions including RNA spike-ins were performed essentially as described (Schwalb et al., 2016). Briefly, 3.3 × 107 Raji B (CDK9as or wild type) cells were treated for 15 min with solvent DMSO (control) or 5 µM of 1-NA-PP1 (CDK9as inhibitor). After 10 min of treatment, labeling was performed by adding 500 µM of 4-thiouracil (4sU) (Sigma-Aldrich, St. Louis, MO, USA) for 5 min at 37°C and 5% CO2. Cells were harvested by centrifugation at 3000 x g for 2 min. Total RNA was extracted using QIAzol according to the manufacturer’s instructions. RNAs were sonicated to generate fragments of <1.5 kbp using AFAmicro tubes in a S220 Focused-ultrasonicator (Covaris Inc., Woburn, MA USA). 4sU-labeled RNA was purified from 150 µg total fragmented RNA. Separation of labeled RNA was achieved with streptavidin beads (Miltenyi Biotec, Bergisch Gladbach, Germany) as described in (Schwalb et al., 2016). Prior to library preparation, 4sU-labeled RNA was purified and quantified. Enrichment of 4sU-labeled RNA was analyzed by RT-qPCR as described (Schwalb et al., 2016). Input RNA was treated with HL-dsDNase (ArcticZymes, Tromsø, Norway) and used for strand-specific library preparation according to the Ovation Universal RNA-Seq System (NuGEN, Leek, The Netherlands). The size-selected and pre-amplified fragments were analyzed on a Fragment Analyzer before clustering and sequencing on the Illumina HiSeq 1500.

### TT-seq data preprocessing and global normalization

Paired-end 50 base reads with additional 6 base reads of barcodes were obtained for each of the samples, that is two TT-seq replicates with 1-NA-PP1 (CDK9as inhibitor) and two TT-Seq replicates with DMSO (control) treatment. Reads were demultiplexed and mapped with STAR 2.3.0 (Dobin and Gingeras, 2015) to the hg20/hg38 (GRCh38) genome assembly (Human Genome Reference Consortium). Samtools (Li et al., 2009) was used to quality filter SAM files, whereby alignments with MAPQ smaller than 7 (-q 7) were skipped and only proper pairs (-f2) were selected. Further data processing was carried out using the R/Bioconductor environment. We used a spike-in (RNAs) normalization strategy essentially as described (Schwalb et al., 2016) to allow observation of global shifts and antisense bias determination (ratio of spurious reads originating from the opposite strand introduced by the RT reactions). Read counts for spike-ins were calculated using HTSeq (Anders et al., 2015). Sequencing depth calculations did not detect global differences. Antisense bias ratios were calculated for each sample j according to

$$
c_{j}=mediani⁡\frac{k_{ij}^{antisense}}{k_{ij}^{sense}}
$$

for all available spike-ins i.

### Definition of transcription units (TUs)

For each annotated gene, transcription units (TUs) were defined as the union of all existing inherent transcript isoforms (UCSC RefSeq GRCh38). Read counts for all features were calculated using HTSeq (Anders et al., 2015) and corrected for antisense bias using antisense bias ratios $c_{j}$ calculated as described above. The real number of read counts sij for transcribed unit i in sample j was calculated as

$$
s_{ij}=\frac{S_{ij}-c_{j}A_{ij}}{1-c_{j}^{2}}
$$

where Sij and Aij are the observed number of read counts on the sense and antisense strand. Read counts per kilobase (RPK) were calculated upon bias corrected read counts falling into the region of a transcribed unit divided by it’s length in kilobases. Based on the antisense bias corrected RPKs a subgroup of expressed TUs was defined to comprise all TUs with an RPK of 100 or higher in two summarized replicates of TT-seq without inhibitor treatment. An RPK of 100 corresponds to approximately a coverage of 10 per sample due to an average fragment size of 200. This subset was used throughout the analysis unless stated otherwise.

### Calculation of the number of transcribed bases

Aligned duplicated fragments were discarded for each sample. Of the resulting unique fragment isoforms only those were kept that exhibited a positive inner mate distance. The number of transcribed bases (tbj) for all samples was calculated as the sum of the coverage of evident (sequenced) fragment parts (read pairs only) for all fragments smaller than 500 bases in length and with an inner mate interval not entirely overlapping a Refseq annotated intron (UCSC RefSeq GRCh38, ~96% of all fragments) in addition to the sum of the coverage of non-evident fragment parts (entire fragment).

### Size factor normalization

We first checked that no significant global shifts were detected in a comparison of two TT-seq replicates with 1-NA-PP1 (CDK9as inhibitor) treatment against two TT-seq replicates with DMSO treatment (control) in the above described spike-ins normalization strategy. Then all samples were subjected to an alternative, more robust normalization procedure. For each sample j the antisense bias corrected number of transcribed bases tbj was calculated on all expressed TUs i exceeding 125 kbp in length. 50 kbp were truncated from each side of the selected TUs to avoid influence of the response to CDK9as inhibition (Laitem et al., 2015). On the resulting intervals, size factors for each sample j were determined as

$$
\sigma_{j}=mediani⁡\frac{tb_{ij}}{\prod_{v=1}^{m}tb_{ij}^{1/m}}
$$

where m denotes the number of samples. This formula has been adapted (Anders and Huber, 2010) and was used to correct for library size and sequencing depth variations.

### Calculation of response ratios

For each condition j (control or CDK9as inhibited) the antisense bias corrected number of transcribed bases $tb_{i}^{j}$ was calculated on all expressed TUs i exceeding 10 kbp in length. Of all remaining TUs only those were kept harboring one unique TSS given all Refseq annotated isoforms (UCSC RefSeq GRCh38). Response ratios were calculated for a window from the TSS to 10 kbp downstream (excluding the first 200 bp) for each TU i as

$$
r_{i}=1-tb_{i_{[0.2,10kbp]}}^{CDK9^{as}inhibited}/tb_{i_{[0.2,10kbp]}}^{Control}
$$

where negative values were set to 0.

### Estimation of robust common elongation velocity

For each condition j (control or CDK9as inhibited) the antisense bias corrected number of transcribed bases $tb_{i}^{j}$ was calculated on all expressed TUs i with a given response ratio $r_{i}$, excluding the first 200 bp. All TUs were truncated by 5 kbp in length from the 3’ end prior to calculation to avoid influence of some alterations in signal around the pA site after CDK9as inhibition (Laitem et al., 2015). A robust common elongation velocity estimate was calculated by finding an optimal fit for all TUs i between 25 to 200 kbp in length Li, that is minimizing the function

$$
loss=mediani(|1−\frac{tb_{i}^{CDK9^{as}inhibited}}{tb_{i}^{Control}}−\frac{r_{i}v(t^{∗}−t)}{L_{i}}|)
$$

on the interval [0,10000] with inhibitor treatment duration t*=15 [min] and labeling duration t = 5 [min], given that

$$
tb_{i}^{CDK9^{as}inhibited}-tb_{i}^{Control}=r_{i}\frac{tb_{i}^{Control}}{L_{i}}v_{i}t^{*}-t
$$

that is the difference of transcribed bases obtained by the CDK9as inhibitor treatment equals the number of transcribed bases per nucleotide $tb_{i}^{Control}/L_{i}$ times the number of nucleotides traveled $v_{i}t^{*}-t$ in $t^{*}-t$ minutes corrected by the amount of the response $r_{i}$.

### Estimation of gene-wise elongation velocity

For each condition j (control or CDK9as inhibited) the antisense bias corrected number of transcribed bases $tb_{i}^{j}$ was calculated on all expressed TUs i exceeding 35 kbp in length, excluding the first 200 bp. All TUs were truncated by 5 kbp in length from the 3’ end prior to calculation to avoid influence of some alterations in signal around the pA site after CDK9as inhibition (Laitem et al., 2015). Of all remaining TUs only those were kept harboring one unique TSS given all Refseq annotated isoforms (UCSC RefSeq GRCh38). For each TU i with $r_{i}>0.25$ the elongation velocity vi [kbp/min] was calculated as

$$
v_{i}=\frac{tb_{i}^{Control}-tb_{i}^{CDK9^{as}inhibited}}{tb_{i}^{Control}∙\frac{r_{i}}{L_{i}}t^{*}-t}
$$

with inhibitor treatment duration t*=15 [min] and labeling duration t = 5 [min].

### mNET-seq

Two biological replicates of reactions including empigen BB detergent treatment during immunoprecipitation (IP) were performed essentially as described (Nojima et al., 2016; Schlackow et al., 2017), with minor modifications. Briefly, 1.6 × 108 Raji B (CDK9as) cells were treated for 15 min with solvent DMSO (control) or 5 µM of 1-NA-PP1 (CDK9as inhibitor). Cell fractionation was performed as described (Conrad and Ørom, 2017). Isolated chromatin was digested with micrococcal nuclease (MNase) (NEB, Ipswich, MA USA) at 37°C and 1,400 rpm for 90 s. To inactivate MNase, EGTA was added to a final concentration of 25 mM. Digested chromatin was collected by centrifugation at 4°C and 13,000 rpm for 5 min. The supernatant was diluted tenfold with IP buffer containing 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05% (vol/vol) NP-40, and 1% (vol/vol) empigen BB (Sigma-Aldrich, St. Louis, MO USA). For each IP, 50 µg of Pol II antibody clone MABI0601 (BIOZOL, Eching, Germany) was conjugated to Dynabeads M-280 Sheep Anti-Mouse IgG (Thermo Fisher Scientific, Waltham, MA USA). Pol II antibody-conjugated beads were added to diluted sample. IP was performed on a rotating wheel at 4°C for 1 hr. The beads were washed six times with IP buffer (50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05 % NP-40, and 1% empigen BB) and once with 500 µL of PNKT buffer containing 1 x T4 polynucleotide kinase (PNK) buffer (NEB, Ipswich, MA USA) and 0.1% (vol/vol) Tween-20 (Sigma-Aldrich, St. Louis, MO USA). Beads were incubated in 100 µL of PNK reaction mix containing 1 x PNK buffer, 0.1% (vol/vol) Tween-20, 1 mM ATP, and T4 PNK, 3’ phosphatase minus (NEB, Ipswich, MA USA) at 37°C for 10 min. Beads were washed once with IP buffer. RNA was extracted with TRIzol reagent. RNA was precipitated with GlycoBlue co-precipitant (Thermo Fisher Scientific, Waltham, MA USA) and resolved on 6% denaturing acrylamide containing 7 M urea (PanReac AppliChem, Darmstadt, Germany) gel for size purification. Fragments of 35–100 nt were eluted from the gel using elution buffer containing 1 M NaOAc, 1 mM EDTA, and precipitated in ethanol. RNA libraries were prepared according to the TruSeq Small RNA Library Kit (Illumina, Massachusetts USA) and as described (Nojima et al., 2016). The size-selected and pre-amplified fragments were analyzed on a Fragment Analyzer before clustering and sequencing on an Illumina HiSeq 2500 sequencer.

### mNET-seq data preprocessing and normalization

Paired-end 50 base reads with additional 6 base reads of barcodes were obtained for each of the samples, that is mNET-seq samples with 1-NA-PP1 (CDK9as inhibitor) and with DMSO (control) treatment. Reads were demultiplexed and mapped with STAR 2.3.0 (Dobin and Gingeras, 2015) to the hg20/hg38 (GRCh38) genome assembly (Human Genome Reference Consortium). Samtools (Li et al., 2009) was used to quality filter SAM files, whereby alignments with MAPQ smaller than 7 (-q 7) were skipped and only proper pairs (-f2) were selected. Further data processing was carried out using the R/Bioconductor environment. Antisense bias (ratio of spurious reads originating from the opposite strand introduced by the RT reactions) was determined using positions in regions without antisense annotation with a coverage of at least 100 according to Refseq annotated genes (UCSC RefSeq GRCh38). mNET-seq coverage tracks were size factor normalized on 260 TUs that showed a response of less than 5% ($r_{i}<0.05$) in the TT-seq signal upon 1-NA-PP1 (CDK9as inhibitor) treatment. The response ratio $r_{i}$ was determined as described above including also TUs with multiple TSS to extend the number of TUs for normalization. Note that variation of the response ratio cutoff and thereby the number of TUs available for normalization does virtually not change the normalization parameters. Coverage tracks for further analysis were restricted to the last nucleotide incorporated by the polymerase in the aligned mNET-seq reads.

### Detection of pause sites

For all expressed TUs i exceeding 10 kbp in length with one unique TSS given all Refseq annotated isoforms (UCSC RefSeq GRCh38) the pause site m* was calculated for all bases m in a window from the TSS to the end of the first exon (excluding the last 5 bases) via maximizing the function

$$
ρ_{i}=maxmp_{im}
$$

where $ρ_{i}$ needed to exceed 5 times the median of the signal strength $p_{im}$ for all non-negative antisense bias corrected mNET-seq coverage values (Nojima et al., 2015). Note that all provided coverage tracks were used.

### DNA-RNA and DNA-DNA melting temperature calculation

The gene-wise mean melting temperature of the DNA-RNA and DNA-DNA hybrid was calculated from subsequent melting temperature estimates of 8-base pair DNA-RNA and DNA-DNA duplexes tiling the respective area according to (SantaLucia, 1998; Sugimoto et al., 1995).

### Molecular weight conversions

The known sequence and mixture of the utilized spike-ins allows to calculate a conversion factor to RNA amount per cell [cell−1] given their molecular weight assuming perfect RNA extraction. The number of spike-in molecules per cell N [cell−1] was calculated as

$$
N=\frac{m}{Mn}N_{A}
$$

with the number of spike-ins m 25.10−9 [g], the number of cells n 3.27.107, the Avogadro constant NA 6.02214085774.1023 [mol−1] and molar-mass (molecular weight) of the spike-ins M [g mol−1] calculated as

$$
M = A_{n}⋅329.2 + (1−\tau)⋅U_{n}⋅306.2 + C_{n}⋅305.2 + G_{n}⋅345.2 + \tau⋅4sU_{n}⋅322.26 + 159
$$

where An, Un, Cn, Gn and 4sUn are the number of each respective nucleotide within each spike-in polynucleotide. $\tau$ is set to 0.1 in case of a labeled spike-in and 0 otherwise. The addition of 159 to the molecular weight takes into account the molecular weight of a 5' triphosphate. Provided the above the conversion factor to RNA amount per cell $κ$ [cell−1] can be calculated as

$$
κ=mean (mediani(\frac{tb_{i}}{L_{i}⋅N}))
$$

for all labeled spike-in species i with length Li. Note that imperfect RNA extraction efficiency would lead to an underestimation of cellular labeled RNA in comparison to the amount of added spike-ins and thus to an underestimation of initiation frequencies. In case of a strong underestimation however the real initiation frequencies would lie above the pause-initiation limit, which is theoretically impossible. Thus we assume this effect to be insignificant.

### Estimation of initiation frequency I

The antisense bias corrected number of transcribed bases $tb_{i}^{Control}$ was calculated on all expressed TUs i exceeding 10 kbp in length. Of all remaining TUs only those were kept harboring one unique TSS given all Refseq annotated isoforms (UCSC RefSeq GRCh38). For each TU i the productive initiation frequency Ii [cell−1min−1], which corresponds to the pause release rate, was calculated as

$$
I_{i}=\frac{1}{κ}∙\frac{tb_{i}^{Control}}{t∙L_{i}}
$$

with labeling duration t = 5 [min] and length Li. Note that $tb_{i}^{Control}$ and Li were restricted to regions of non-first constitutive exons (exonic bases common to all isoforms).

### Estimation of pause duration d

For all expressed TUs i exceeding 10 kbp in length with one unique TSS given all Refseq annotated isoforms (UCSC RefSeq GRCh38) the pause duration di [min] was calculated as the residing time of the polymerase in a window ±100 bases m around the pause site (see above) as

$$
d_{i}=\frac{\sum_{+/−100}p_{im}}{I_{i}}.mediani(\frac{v_{i}}{I_{i}v_{i}(t^{∗}−t)/\sum_{response window}p_{im}})
$$

with pause release rate $I_{i}$ and the number of polymerases $p_{im}$ (antisense bias corrected mNET-seq coverage values [Nojima et al., 2015]) in a window ±100 bases around the pause site. For pause sites below 100 bp downstream of the TSS the first 200 bp of the TU were considered. Note that the right part of the formula is restricted to mNETseq instances above the 50% quantile for robustness and adjusts di to an absolute scale by comparing the CDK9 derived elongation velocities$v_{i}$ with those derived from combining mNET-seq and TT-seq data in the response window $200,v_{i}t^{*}-t$.

### Pause-initiation limit

The previously derived inequality from (Ehrensberger et al., 2013)

$$
\frac{v}{I}\geq50[bp]
$$

states that new initiation events into productive elongation are limited by the velocity of the polymerase in the promoter-proximal region and that steric hindrance occurs below a distance of 50 bp between the active sites of the initiating Pol II and the paused Pol II. Given the calculations of pause duration $d$ and (productive) initiation frequency $I$ above, we can reformulate this inequality to

$$
\frac{200[bp]}{d∙I}\geq50[bp]
$$

with 200 [bp] being the above defined pause window.

### Simulation of TT-seq data based on elongation velocity profiles

Based on the following model we simulated TT-seq coverage values by providing elongation velocity profiles $vt$, a labeling duration $t^{lab}$ and a uracil content dependent labeling bias

$$
l_{f}=1−(1−p^{lab})^{#u_{f}}
$$

$p^{lab}$ denotes the labeling probability (set to 0.05) and $#u_{f}$ the number of uracil residues of a given fragment $f$ (set to 0.28 times fragment length). The elongation velocity profile $vt$ can be used to calculate the number of elongated positions of the polymerase $\taut$ at timepoint $t$ as

$$
\taut=\int_{0}^{t}vtdt
$$

Given the transcription start site $\tau0$ the number of elongated positions $\taut$ can be used to determine the end of an emerging nascent fragment $f$. Based on that we determined the start position of a fragment as $\tau(max(t−t^{lab},0))$ for each labeling duration $t^{lab}$ as the position of the polymerase at the beginning of the labeling process. Subsequently, we used the number of uracil residues present in the RNA fragment $#u_{f}$ to weight the amount of coverage contributed by this fragment as $l_{f}$. Additionally, we applied a size selection similar to that in the original protocol for fragments below 80 bp in length with a sigmoidal curve that mimics a typical size selection spread. Given a pause position of 80 bp downstream of the TSS and pause duration of 1 or 2 min we adjusted the elongation velocity profile to simulate polymerase pausing. Note that neither reasonable changes in labeling probability, size selection probability nor changes in uracil residue content change the general observation that longer pause durations induce a greater shortage of TT-seq coverage in the region between the TSS and the pause site.

### Estimation of gene-wise elongation velocity (without of response ratio)

For each condition j (control or CDK9as inhibited) the antisense bias corrected number of transcribed bases $tb_{i}^{j}$ was calculated on all expressed TUs i exceeding 35 kbp in length, excluding the first 200 bp. All TUs were truncated by 5 kb in length from the 3’ end prior to calculation to avoid influence of some alterations in signal around the pA site after CDK9as inhibition (Laitem et al., 2015). Of all remaining TUs only those were kept harboring one unique TSS given all Refseq annotated isoforms (UCSC RefSeq GRCh38). For each TU i with $r_{i}>0.25$ the cumulative sums of the difference of the number of transcribed bases $tb_{i}^{j}$ for each base k was calculated as

$$
S_{0}=0S_{n}=S_{n-1}+tb_{i}^{Control}-tb_{i}^{CDK9^{as}inhibited}
$$

starting at the unique TSS (position 0) to $n=L_{i}$ the length of the TU. A elongation length estimate $L_{i}^{responsewindow}$ was then calculated by finding an optimal fit for n between 0 to $L_{i}$, that is maximizing the function

$$
gain=nmax(\frac{S_{n}⋅L_{i}}{maxn=1..L_{i}S_{n}}−n+1)
$$

on the interval [0, $L_{i}$]. In words, finding the maximum of the cumulative sums of difference in coverage rotated 45 degrees clockwise. The elongation velocity $v^_{i}$ [kbp/min] was subsequently calculated as

$$
v^_{i}=\frac{L_{i}^{response window}}{(t^{∗}−t)}
$$

with inhibitor treatment duration t*=15 [min] and labeling duration t = 5 [min].

### Estimation of pause duration d^ (without of initiation frequency).

For all expressed TUs i exceeding 10 kb in length with one unique TSS given all Refseq annotated isoforms (UCSC RefSeq GRCh38) the pause duration $d^_{i}$ [min] was calculated as the residing time of the polymerase in a window ±100 bases m around the pause site (see above) as

$$
d_{i}^=\frac{\sum_{+/−100}p_{im}.L_{i}^{response window}}{\sum_{response window}p_{im}.v^_{i}}
$$

with elongation length estimate $L_{i}^{responsewindow}$ and the number of polymerases $p_{im}$ (antisense bias corrected mNET-seq coverage values) in a window ±100 bases around the pause site. For pause sites below 100 bp downstream of the TSS the first 200 bp of the TU were considered. Note that $d^_{i}$ was adjusted to the height as $d_{i}$ by a single proportionality factor for visualization purposes.

### In vivo RNA secondary structure (DMS-seq [Rouskin et al., 2014])

The gene-wise DMS-seq coverage (300 μl in vivo) for a window of [−15,–65] bp upstream of the pause site was normalized by subtraction from the respective DMS-seq coverage (denatured) allowing for maximal 5% negative values which were set to 0 (sequencing depth adjustment). The gene-wise mean values were subsequently normalized by dividing with the initiation frequency. Note that the latter normalization has an insignificant effect.

### Prediction of RNA secondary structure

The gene-wise mean minimum free energy for a window of [−15,–65] bp upstream of the pause site was calculated from subsequent minimum free energy estimates of 13-base pair RNA fragments tiling the respective area using RNAfold from the ViennaRNA package (Lorenz et al., 2011).

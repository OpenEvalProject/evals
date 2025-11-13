# HUWE1 controls tristetraprolin proteasomal degradation by regulating its phosphorylation

## Authors

- Sara Scinicariello<sup>1</sup>
- Adrian Soderholm<sup>1</sup>
- Markus Schäfer<sup>3</sup>
- Alexandra Shulkina<sup>1</sup>
- Irene Schwartz<sup>1</sup>
- Kathrin Hacker<sup>1</sup>
- Rebeca Gogova<sup>2</sup>
- Robert Kalis<sup>2</sup> ([ORCID: 0000-0001-7553-4806](https://orcid.org/0000-0001-7553-4806))
- Kimon Froussios<sup>3</sup> ([ORCID: 0000-0003-2812-0525](https://orcid.org/0000-0003-2812-0525))
- Valentina Budroni<sup>1</sup>
- Annika Bestehorn<sup>1</sup>
- Tim Clausen<sup>3</sup> ([ORCID: 0000-0003-1582-6924](https://orcid.org/0000-0003-1582-6924))
- Pavel Kovarik<sup>1</sup>
- Johannes Zuber<sup>3</sup> ([ORCID: 0000-0001-8810-6835](https://orcid.org/0000-0001-8810-6835))
- Gijs A Versteeg<sup>1</sup> ([ORCID: 0000-0002-6150-2165](https://orcid.org/0000-0002-6150-2165)) †

### Affiliations

1. Department of Microbiology, Immunobiology and Genetics, Max Perutz Labs, University of Vienna, Vienna BioCenter (VBC) Vienna Austria ([ROR:03prydq77](https://ror.org/03prydq77))
2. Vienna BioCenter PhD Program, Doctoral School of the University of Vienna and Medical University of Vienna, Vienna BioCenter (VBC) Vienna Austria ([ROR:03prydq77](https://ror.org/03prydq77))
3. Research Institute of Molecular Pathology (IMP), Vienna BioCenter (VBC) Vienna Austria ([ROR:04khwmr87](https://ror.org/04khwmr87))
4. Medical University of Vienna, Vienna BioCenter (VBC) Vienna Austria ([ROR:04khwmr87](https://ror.org/04khwmr87))

† Corresponding author

## Abstract

Tristetraprolin (TTP) is a critical negative immune regulator. It binds AU-rich elements in the untranslated-regions of many mRNAs encoding pro-inflammatory mediators, thereby accelerating their decay. A key but poorly understood mechanism of TTP regulation is its timely proteolytic removal: TTP is degraded by the proteasome through yet unidentified phosphorylation-controlled drivers. In this study, we set out to identify factors controlling TTP stability. Cellular assays showed that TTP is strongly lysine-ubiquitinated, which is required for its turnover. A genetic screen identified the ubiquitin E3 ligase HUWE1 as a strong regulator of TTP proteasomal degradation, which we found to control TTP stability indirectly by regulating its phosphorylation. Pharmacological assessment of multiple kinases revealed that HUWE1-regulated TTP phosphorylation and stability was independent of the previously characterized effects of MAPK-mediated S52/S178 phosphorylation. HUWE1 function was dependent on phosphatase and E3 ligase binding sites identified in the TTP C-terminus. Our findings indicate that while phosphorylation of S52/S178 is critical for TTP stabilization at earlier times after pro-inflammatory stimulation, phosphorylation of the TTP C-terminus controls its stability at later stages.

## Introduction

Dynamic regulation of the immune system is essential to mount a defense against pathogens upon infection, yet shut-off the response at the appropriate time during resolution. Since most cytokines and other pro-inflammatory mediators are transcriptionally induced during infection, an essential aspect of returning to homeostatic conditions is the timely removal of their mRNAs during resolution.

Tristetraprolin (TTP; also known as ZFP36 or TIS11A) is an RNA-binding protein that interacts with AU-rich elements (ARE) present in the 3’-untranslated-regions (UTR) of many mRNAs encoding pro-inflammatory mediators (Galloway et al., 2016; Lai et al., 1999; Sedlyarov et al., 2016). Subsequently, TTP recruits the CCR4-NOT decapping and deadenylation complex to target mRNAs, resulting in their destabilization and removal from the cell (Fabian et al., 2013; Lai et al., 2003; Lykke-Andersen and Wagner, 2005; Sandler et al., 2011; Tiedje et al., 2016). TTP binds to the AREs of a multitude of mRNAs encoding cytokines and other immune-related factors, yet not all of them are destabilized (Moore et al., 2018; Sedlyarov et al., 2016; Tiedje et al., 2016; Zhang et al., 2017). This has suggested that additional -hitherto unknown- regulatory mechanisms are at play controlling TTP-dependent mRNA degradation, which may differ in various cell types.

The biological importance of TTP for proper dampening of the inflammatory response is underpinned by the observation that Zfp36 (the gene encoding TTP)-deficient mice develop systemic inflammation characterized by arthritis, dermatitis, conjunctivitis, and cachexia, which has been coined TTP deficiency syndrome (Taylor et al., 1996). One of the main deregulated ARE-containing mRNAs driving the inflammatory phenotype in Zfp36-deficient mice is Tnf (Carballo et al., 1998; Taylor et al., 1996), although additionally Il1a/b, Il23, and Ccl3 have been implicated as well (Kang et al., 2011; Molle et al., 2013; Sneezum et al., 2020).

TTP itself is regulated at the transcriptional, post-transcriptional, and post-translational levels. Most cell types express low levels of Zfp36 mRNA in unstimulated conditions, the transcription of which is robustly induced by proinflammatory stimuli including the Toll-like receptor 4 (TLR4) agonist lipopolysaccharide (LPS) in myeloid cells such as macrophages (Carballo et al., 1998; Lai et al., 1995; Sauer et al., 2006; Schaljo et al., 2009; Suzuki et al., 2003). At the post-translational level, TTP is phosphorylated at over 30 residues by inflammation-activated stress kinases (Brook et al., 2006; Clark and Dean, 2016; Hitti et al., 2006; Ronkina et al., 2019).

The biological relevance of most TTP phospho-sites and the identity of the involved kinases remain unknown (Clark and Dean, 2016; Ronkina et al., 2019). Most characterized are phosphorylation events at residues S52 and S178 in murine TTP that are mediated by the inflammation-activated kinase MK2, which acts down-stream of p38 mitogen-activated protein kinase (MAPK; Brook et al., 2006; Hitti et al., 2006). In mice, TTP mutants lacking these phosphorylation sites are highly unstable and rapidly degraded, yet highly biologically active (Ross et al., 2015).

This has given rise to a model in which TTP is predominantly unphosphorylated and rapidly degraded in unstimulated cells, whereas pro-inflammatory cell signaling not only increases Zfp36 transcription, but also TTP S52/S178 phosphorylation and stabilization through interaction with 14-3-3 proteins (Kratochvill et al., 2011; Sedlyarov et al., 2016). However, in this S52/S178 phosphorylated state, TTP is thought to be inactive, whereas during dephosphorylation of these residues at later times in the inflammatory response, TTP actively mediates mRNA degradation (Kratochvill et al., 2011; Sedlyarov et al., 2016). Nevertheless, the impact of the other 30+ phosphorylated residues on TTP stability and activity has remained largely elusive.

Proteasomes are the main degradation machines of cells for homeostatic protein turn-over (Bard et al., 2018). 20S core particles contain catalytic activity, yet lack receptors for ubiquitin and ATPase activity for unfolding and translocation of proteins into the catalytic chamber. Association of 19S regulatory particles containing ubiquitin receptors and AAA+ ATPase activity assembles 26S proteasomes, which are considered the main degradative entities for poly-ubiquitinated proteins (Bard et al., 2018).

TTP protein is degraded through the proteasome, as previous studies showed that 20S proteasome inhibition stabilizes TTP. Moreover, a previous study suggested that TTP may be directly degraded by 20S proteasomes in a ubiquitin-independent manner. In this context, important destabilizing intrinsically disordered regions in the N and C termini of TTP were identified and have been suggested to putatively allow direct degradation by 20S proteasomes (Brook et al., 2006; Ngoc et al., 2014). Yet, other regulators of intracellular TTP protein abundance have remained elusive. In this study, we set out to identify and characterize novel factors that control TTP turn-over, thereby affecting pro-inflammatory output.

Through genetic loss-of-function screening, we identified several novel determinants of TTP abundance, including the giant ubiquitin E3 ligase HUWE1. Our data indicate that TTP is strongly poly-ubiquitinated on lysines in its zinc finger domain, and degraded by the proteasome in a ubiquitin-dependent manner. Moreover, we identified a novel role for the E3 ligase HUWE1 in indirectly controlling TTP turn-over through mediating its phosphorylation via multiple stress kinases, and reduced dephosphorylation.

## Results

### TTP is degraded in a ubiquitin-dependent manner

Pro-inflammatory stimuli such as LPS drive both transcription of Zfp36 (the gene encoding TTP), and phosphorylation of the TTP protein. To study how TTP protein levels are regulated, we established a macrophage cell line expressing exogenous TTP from a constitutively active promoter, uncoupling Zfp36 transcription from regulatory effects on TTP protein stability in the absence or presence of pro-inflammatory signals.

Consistent with previous studies, endogenous TTP protein was rapidly induced by LPS (Carballo et al., 1998; Lai et al., 1995; Sauer et al., 2006; Schaljo et al., 2009; Suzuki et al., 2003), and in the absence of de novo protein synthesis, rapidly degraded (Figure 1A; Brook et al., 2006; Ngoc et al., 2014). Treatment with proteasome inhibitor MG132 almost completely prevented TTP degradation, indicating that its degradation is predominantly through the proteasome. Under these conditions, a high-MW form of TTP accumulated, suggesting that phosphorylation is important for regulation of its stability.

![Figure 1.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig1-v1.jpg)

**Figure 1.:** (A) RAW264.7 murine macrophages were stimulated with LPS and incubated with the translation inhibitor cycloheximide (CHX) and the proteasome inhibitor MG132 for the indicated times (h), after which TTP levels were analyzed by western blot. (B) 3xHA-TTP-expressing RAW264.7 cells were incubated with LPS or left unstimulated. Cells were then treated with E1 enzyme inhibitor (TAK-234) or the proteasome inhibitor Epoxomicin (Epx). Protein levels were assessed by western blot. (C) RAW264.7 cells stably expressing 3xHA-tagged TTP protein were treated with Epx for 5 hr, after which TTP was immunoprecipitated, and its ubiquination analyzed by western blot. (D) Schematic representation of the TTP stability reporter construct. Constitutively expressed myc-tagged mCherry-TTP fusion protein and enhanced blue fluorescent protein (eBFP2) are translated at equimolar levels through a P2A site. (E–F) RAW264.7-Dox-Cas9-mCherry-TTP cells were stimulated with LPS for the indicated times. Subsequently, cell lysates were treated with Calf Intestinal Phosphatase (CIP) for 2 hr at 37 °C, and TTP levels analyzed by western blot. Non-saturated western blot signals for mCherry-TTP and endogenous TTP protein were quantified, normalized to ACTIN levels, and plotted. (G) RAW264.7-Dox-Cas9-mCherry-TTP cells were treated with LPS for 2 hr, after which PP1/2 inhibitor okadaic acid (OA) was added to the culture medium for 2 hr. TTP electrophoretic mobility was assessed by western blot.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) 3xHA-TTP-expressing RAW264.7 cells were incubated with LPS or left unstimulated. Cells were then treated with E1 enzyme inhibitor (TAK-234) or the proteasome inhibitor Epoxomicin (Epx). Ubiquitin levels were assessed by western blot. (B) RAW264.7 cells were incubated with LPS for 2 hr, subsequently treated with the indicated inhibitors for 6 hr, and endogenous TTP quantified by Western blot. Bar graphs represent mean and s.d.; n=2 biological replicates analyzed by unpaired t-test. (C) HEK-293T cells were transiently transfected with plasmids encoding 3xHA-tagged wild-type TTP, a TTP KtoR mutant, or an empty vector. Cells were incubated with the translation inhibitor cycloheximide (CHX) and Epx for 5 hr. Immunoprecipitation was carried out using HA antibody, and TTP ubiquination was analyzed by western blot. (D) RAW264.7 cells were treated with LPS for 2 hr, subsequently incubated with CHX and Epx for 5 hr, and analyzed by IP of endogenous TTP, and subsequent WB for ubiquitin. (E) HEK-293T cells were transiently transfected with plasmids encoding 3xHA-tagged wild-type TTP, or a TTP KtoR mutant, incubated with CHX for the indicated times, and quantified by WB. Single-phase decay curves represent means and s.d. from n=3 biological replicates. (F) HEK-293T cells were transiently transfected with plasmids encoding 3xHA-tagged HA-TTP KtoR mutants, and quantified by WB. Bar graphs represent means and s.d. of n=3 biological replicates, analyzed by one-way ANOVA. (G) HEK-293T cells expressing FLAG-TTP and HA-ubiquitin were incubated for 5 hr with Epx, followed by IP for FLAG-TTP, and WB analysis using K48- or K63-specific ubiquitin antibodies. In vitro produced K48- and K63-linked ubiquitin chains were included as positive controls. (H) RAW264.7-Dox-Cas9-mCherry-TTP cells were either left unstimulated or treated with LPS for 5 hr. Subsequently, cells were incubated with CHX for 10 hr. and analyzed for mCherry-TTP protein levels by flow cytometry. (I) RAW264.7-Dox-Cas9 cells were stimulated with LPS for the indicated time. Immunoprecipitation was carried out using antibodies for TTP or an IgG control. Immunoprecipitated complexes were analysed by western blot. (J) Volcano plots representing TTP-interactome in RAW264.7 cells. RAW264.7 cells stably expressing a Dox-inducible TurboID-TTP fusion protein were treated with LPS or Epx for 4 hr., followed by 15 min. of biotin labeling in the cell medium. TurboID without fusion was used as a control. Biotinylated proteins were immunoprecipitated and submitted for nLC-MS/MS. TTP interactome is highlighted and known TTP interactors are shown adjusted p-value ≤0.05 and Fold Change (Log2) ≥1; with n=3 biological replicates.

To investigate whether pro-inflammatory stimuli are exclusively stabilizing TTP, or also provide degradation signals, a macrophage cell line stably expressing HA-tagged TTP was established (Figure 1B). Under non-stimulated conditions, HA-TTP was detected as medium-range MW species migrating at and above its predicted MW of 36.7 kDa, consistent with it being partially phosphorylated under non-stimulated conditions. Stimulation with LPS resulted in rapid TTP stabilization after 30 min, followed by a reduction of its protein levels at 3 hr and 7 hr post-treatment (Figure 1B; lanes 2–3). This suggested that pro-inflammatory stimuli may also provide the signaling required for TTP turn-over at longer stimulation times, possibly through regulating its phosphorylation.

To determine whether TTP proteasomal degradation was mediated by ubiquitination, cells were treated with the ubiquitin E1 inhibitor TAK-243, which inhibits de novo ubiquitination (Figure 1B and Figure 1—figure supplement 1A–B). This stabilized endogenous and exogenously expressed TTP under baseline and LPS-stimulated conditions (Figure 1B, and Figure 1—figure supplement 1A–B), demonstrating that TTP is degraded in a ubiquitination-dependent manner. Consistent with this notion, exogenous HA-TTP and endogenous TTP was detected to be ubiquitinated in denaturing lysates from these cells (Figure 1C, and Figure 1—figure supplement 1C-D).

Moreover, a TTP mutant in which all of its five lysine residues in the TTP zinc finger domain were mutated to arginines (KtoR), accumulated at high steady-state levels, and was substantially less ubiquitinated (Figure 1—figure supplement 1C). Consistent with its strongly reduced ubiquitination, the KtoR TTP mutant was stabilized (Figure 1—figure supplement 1E). Mutation of individual lysines had no significant effects on TTP accumulation (Figure 1—figure supplement 1F), suggesting that multiple lysine residues in TTP may be functionally redundant for its ubiquitination and degradation. A TTP mutant with simultaneous mutation of four residues (K97/115/133/135 R) did significantly accumulate, albeit to a lesser extent than a mutant in which all five lysines were mutated (Figure 1—figure supplement 1F). In line with lysine poly-ubiquitination playing an important role in TTP degradation, degradative K48-linked poly-ubiquitin chains were detected on TTP, whereas non-degradative K63-linked chains were not (Figure 1—figure supplement 1G). Collectively, these results indicate that TTP is covalently poly-ubiquitinated in its TTP zinc finger domain, and that all five lysines are functionally important for TTP degradation.

To enable identification of TTP abundance regulators by genetic screening, a macrophage cell line stably expressing unstable mCherry-TTP and stable BFP was established (Figure 1D). The stable BFP served as an internal control, as it is translated in equimolar amounts from the same transcript through a P2A ribosomal skip site. mCherry-TTP accumulated in cells as a stable protein under non-stimulated conditions (Figure 1E; top panel). In contrast, LPS stimulation initially further stabilized mCherry-TTP, yet subsequently facilitated its degradation, phenocopying its endogenous TTP counterpart (Figure 1E; bottom panel, and Figure 1—figure supplement 1H). Treatment of lysates from these cells with alkaline phosphatase collapsed higher migrating endogenous and exogenous TTP species (Figure 1F), whereas inhibition of the phosphatases PP1 and PP2 by okadaic acid (OA) increased them (Figure 1G), indicating that mCherry-TTP is phosphorylated in a similar fashion as endogenous TTP.

Together, these data show that LPS-stimulation initially stabilizes TTP, whereas at later time points its induced cell signaling events direct TTP degradation.

### The E3 ligase HUWE1 is a major determinant of cellular TTP protein abundance

Next, we set out to identify cellular factors regulating TTP protein abundance. To this end, a RAW264.7 mouse macrophage cell line with Dox-inducible Cas9 was established, which in addition expresses mCherry-TTP (Figure 1D and Figure 2A). To enable identification of essential genes, a cell line was established which only functionally edits in the presence of doxycycline (Dox), but not in its absence (Figure 2—source data 4).

![Figure 2.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig2-v1.jpg)

**Figure 2.:** (A) Overview of FACS-based CRISPR-Cas9 knockout screening procedure using the RAW264.7-Dox-Cas9-mCherry-TTP cell line. Cells expressing high and low levels of mCherry-TTP protein were sorted, and their integrated sgRNA coding sequences determined by next generation sequencing. (B) Read counts per million in the mCherry-TTPhigh cells at 3 days after Cas9 induction were compared to those in unsorted cells from the same day, sgRNA enrichment calculated by MAGeCK analysis, and log2-fold change and adjusted p-value plotted. Genes enriched in the sorted populations that met the following criteria are indicated in red: a log2 fold-change of <1.8 (mCherry-TTPlow) or >1.8 (mCherry-TTPhigh), adjusted p-value <0.05, not enriched in the matching eBFP2low or eBFP2high sorted cells. (C) Cas9 was induced with Dox for 5 days in RAW264.7-Dox-Cas9-mCherry-TTP cells expressing either sgROSA or sgHuwe1. Subsequently, cells were treated with LPS for 16 hr, and TTP protein levels were assessed by western blot. HUWE1, mCherry-TTP and endogenous TTP abundance was quantified and plotted. The TTP and ACTIN panels are the left four lanes from the blot presented in Figure 2—figure supplement 1B. (D) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Then, cells were incubated with LPS for 16 hr or left unstimulated, and endogenous TTP protein levels analyzed by intracellular staining, followed by flow cytometry. (E) sgROSA- or sgHuwe1-targeted RAW264.7-Dox-Cas9 cells were treated with LPS for the indicated times (h), and TTP levels were analyzed by flow cytometry. Normalized mean fluorescence intensity (MFI) was plotted. Data represent the mean and s.d.; n=3 biological replicates. ****p ≤0.0001. (F) Bone marrow-derived macrophages (BMDMs) isolated from Cas9-expressing knock-in mice were stably transduced with sgROSA or sgHuwe1. Cells were incubated with LPS for 16 hr or left unstimulated. Endogenous TTP protein levels were determined by western blot. Quantified TTP levels normalized to VINCULIN are plotted. (G) sgROSA- or sgHuwe1-RAW264.7-Dox-Cas9 cells were treated for 2 hr with LPS, followed by CHX chase in the continued presence of LPS. Protein lysates were harvested at the indicated time points (h). Endogenous TTP levels were measured by WB, quantified, plotted, and TTP half-life calculated. Data represent means and s.d.; n=3 biological replicates.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Read counts per million in the mCherry-TTPhigh cells at 6 days after Cas9 induction were compared to those in unsorted cells from the same day, sgRNA enrichment calculated by MAGeCK analysis, and log2-fold change and adjusted p-value plotted. Genes enriched in the sorted populations that met the following criteria are indicated in red: a log2 fold-change of <1.8 (mCherry-TTPlow) or >1.8 (mCherry-TTPhigh), adjusted P-value <0.05, not enriched in the matching eBFP2low or eBFP2high sorted cells. (B) RAW264.7-Dox-Cas9 cells were transduced with lentiviral vectors encoding the indicated sgRNAs. Cas9 was induced for 5 days with Dox. Subsequently, cells were treated with LPS for 16 hr, and TTP protein levels were analyzed by western blot. (C) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were incubated with LPS for the indicated time points (h). Zfp36 mRNA levels were measured by RT-qPCR and normalized to Gapdh. Data represent the mean and s.d.; n=3 biological replicates. Two-way ANOVA was performed. (D) RAW264.7-Dox-Cas9 cells expressing mCherry-IκBα were either left unstimulated or treated with LPS for 2 hr, and mCherry- IκBα protein levels analyzed by flow cytometry. (E) RAW264.7-Dox-Cas9 cells stably expressing mCherry-TTP or mCherry-IκBα fusion proteins were transduced with lentiviral expression constructs encoding sgROSA or sgHuwe1. Knock-out was induced for 3 days by the addition of Dox. Cells were stimulated with LPS for 2 hr. (mCherry-IκBα) or 16 hr. (mCherry-TTP), after which mCherry and eBFP levels were determined by flow cytometry. (F) RAW264.7-Dox-Cas9 expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were pre-treated with Epx for 60 min. or left unstimulated. Subsequently, cells were incubated with LPS for the indicated times and endogenous IκBα phosphorylation and degradation was analyzed by western blot. (G) RKO-Dox-Cas9 cells expressing sgAAVS1 or sgHUWE1 were stimulated with Dox for 6 days, after which TTP protein levels were determined by western blot. (H) sgROSA- or sgHuwe1-RAW264.7-Dox-Cas9 cells stably expressing 3xHA-TTP were treated for 6 hr. with LPS, followed by CHX. Protein lysates were harvested at the indicated time points (h). TTP levels were measured by western blot, quantified, plotted, and TTP half-life calculated. n=2 biological replicates, *p≤0.05.

A genome-wide lentiviral sgRNA library was transduced into these cells, ensuring one integration per cell. Knock-outs were induced by treatment with Dox for three and six days to identify regulators irrespective of essential gene functions and different protein half-lives. Subsequently, TTP was destabilized by LPS treatment, cells with high and low mCherry-TTP content were sorted, and their integrated sgRNA coding sequences quantified by next-generation sequencing (Figure 2A, and Figure 2—source data 5). In parallel, sorted cells with high or low levels of the stable BFP control (Figure 1D, and Figure 2—source data 5) were likewise processed, and used for identifying non-specific factors.

As anticipated, factors previously reported to be important for stabilizing TTP (e.g. Mapkapk2 (Mk2), Ywhag (14-3-3γ), Mapk14 (p38)) were significantly enriched in the mCherry-TTPlow cell pool (Figure 2—source data 6, Figure 2B and Figure 2—figure supplement 1A; left and top panels, respectively). Consistent with mCherry-TTP proteasomal degradation being LPS-dependent (Figure 1E), key factors for TLR4-signaling (Tlr4, Ly96 (Md2)), and components of the proteasome (Psma5, Psmb7) were significantly enriched in mCherry-TTPhigh sorted cells (Figure 2B and Figure 2—figure supplement 1A; right and bottom panels, respectively). Moreover, various additional new candidates controlling cellular TTP abundance were identified, including the giant ubiquitin E3 ligase Huwe1 (Figure 2B and Figure 2—figure supplement 1A, right and top panels, respectively). Individual targeting of these candidates increased endogenous TTP and exogenous mCherry-TTP protein levels by western blot (Figure 2—figure supplement 1B), attesting to the validity and predictive quality of our screen.

In particular, HUWE1 was identified as a strong determinant of endogenous and exogenous TTP protein abundance by western blot (Figure 2C and Figure 2—figure supplement 1B; compare LPS-treated samples), and flow cytometry (Figure 2D), without affecting Zfp36 mRNA levels (Figure 2—figure supplement 1C). Consistent with an increase in protein stability, inducible Huwe1 knock-out significantly increased endogenous TTP protein levels at later time points post-LPS stimulation (Figure 2E). Given that after initial stabilization, LPS mediates TTP degradation (Figure 1E), we tested whether Huwe1 knock-out affected TLR4 signaling. To this end, the effect of Huwe1 loss on IκBα, which is degraded in a proteasome-dependent manner upon LPS stimulation (Figure 2—figure supplement 1D), was measured. Huwe1 knock-out increased TTP protein levels (Figure 2—figure supplement 1E; top panel), but did neither affect LPS-induced degradation of mCherry-IκBα by flow cytometry (Figure 2—figure supplement 1E; bottom panel), nor endogenous IκBα by western blot (Figure 2—figure supplement 1F). This shows that the Huwe1 knock-out does not affect cell signaling between TLR4 and IκBα, and this does not contribute to TTP stabilization in Huwe1-deficient cells.

Next, we determined whether the HUWE1-dependent control of TTP abundance in the RAW264.7 mouse macrophage cell line was conserved across species and cell types. To this end, HUWE1 was targeted in the human colon carcinoma cell line RKO, which -unlike most myeloid cells- have low detectable levels of TTP in the absence of any stimulation (Figure 2—figure supplement 1G). Similar to the phenotype in RAW264.7 cells, HUWE1 knock-out in RKO cells strongly increased TTP protein levels (Figure 2—figure supplement 1G), indicating that HUWE1 has a similar role in human, non-myeloid cells independent of the TLR4 axis. Moreover, targeting of Huwe1 in mouse bone marrow derived macrophages (BMDMs), likewise strongly increased high and low molecular weight species of endogenous TTP (Figure 2F), indicating that the biological importance of Huwe1 for TTP abundance is relevant in primary cells.

Lastly, we measured whether Huwe1 ablation affected TTP protein half-life. To this end, sgROSA and sgHuwe1 RAW264.7-Dox-Cas9 cells were continuously stimulated with LPS, chased in the presence of translation inhibitor cycloheximide (CHX), analyzed by western blot, and single-step exponential decay curves plotted. Endogenous TTP was stabilized ≥5-fold in the absence of Huwe1 (estimated half-life of ~20 hr), compared to sgROSA cells in which TTP half-life was measured to be 3.7 hr (Figure 2G). In similar stability assessments with exogenously expressed TTP in the absence of LPS, Huwe1 knock-out increased HA-TTP protein half-life by 83% from 35 min to 55 min (Figure 2—figure supplement 1H). Together, these data demonstrate that loss of Huwe1 increases TTP protein half-life, and positioned HUWE1 as a strong, conserved regulator of TTP protein stability.

### Loss of Huwe1 decreases the half-life of pro-inflammatory mRNAs controlled by TTP

TTP is essential for the degradation of transcripts with AU-rich elements in their 3’-UTR, encoding pro-inflammatory cytokines such as TNF and IL6. Phosphorylation of S52 and S178 stabilizes TTP, yet reduces its degradation of mRNAs. In contrast, the effect of phosphorylation on other sites has remained elusive. Therefore, we reasoned that increased TTP protein levels upon Huwe1 ablation could (i) either result in increased intracellular TTP protein concentrations, and consequently diminished levels of transcripts encoding pro-inflammatory cytokines, or -as a consequence of increased TTP phosphorylation- (ii) decrease the bio-active pool of TTP, resulting in equal or increased mRNA levels in Huwe1 knock-out cells.

To investigate whether increased TTP levels upon Huwe1 loss are biologically relevant, we measured Tnf and Il6 mRNA levels in Huwe1-targeted BMDMs and RAW264.7 cells. Consistent with the fact that non-stimulated cells have very low levels of TTP, Huwe1 knock-out did not alter baseline Tnf (Figure 3A, and Figure 3—figure supplement 1A), or Il6 (Figure 3—figure supplement 1B/C) mRNA levels.

![Figure 3.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig3-v1.jpg)

**Figure 3.:** RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were incubated with LPS for the indicated time points (h). (A) Mature Tnf mRNA levels, and (B) Tnf pre-mRNA levels were measured by RT-qPCR and normalized to Gapdh. Data represent the mean and s.d.; n=3 biological replicates. ****p ≤0.0001. Two-way ANOVA was performed. (C) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were incubated with LPS for 3 hr, after which Actinomycin D (ActD) was added for the indicated times (min), and Tnf mRNA levels were determined by RT-qPCR. Data represent the mean and s.d.; n=3 biological replicates. **p ≤ 0.01. Unpaired t-tests were performed for the 40 min and 60 min time points.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were incubated with LPS for the indicated time points (h). (A) Tnf or (B) Il6 mRNA levels were measured by RT-qPCR and normalized to Gapdh. Data represent the mean and s.d.; n=3 biological replicates. *p ≤ 0.05; **p ≤ 0.01; ***p≤0.001; ****p ≤0.0001. Two-way ANOVA was performed. (C) sgROSA- or sgHuwe1-expressing BMDMs were treated with LPS as indicated. Gapdh-normalized Il6 mRNA levels were measured by RT-qPCR. Data represent the mean and s.d.; with n=2 biological replicates. ****p ≤0.0001. Two-way ANOVA was performed. (D) Differentiation of sgROSA- or sgHuwe1-expressing BMDMs after 7 days of M-CSF treatment was analyzed by F4/80 staining and analysis by flow cytometry. (E) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 single sgRNA vectors, or sgROSA-sgTTP or sgHuwe1-sgTTP double sgRNA vectors were incubated with LPS for the indicated times. Tnf mRNA expression was determined by RT-qPCR. Data represent the mean and s.d.; n=3 biological replicates. ****p ≤0.0001. Two-way ANOVA was performed. (F) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with LPS for the indicated times. During the last 2 hr, Brefeldin A was added to block cytokine secretion. Intracellular TNF protein levels were analyzed by flow-cytometry. Data represent the mean and s.d.; n=3 biological replicates. **p ≤ 0.01. Two-way ANOVA was performed.

LPS stimulation transcriptionally induces Tnf and Il6, and in parallel influences TTP protein stability. Loss of Huwe1 resulted in significantly decreased concentrations of Tnf and Il6 transcripts at 3–16 hr post-stimulation (Figure 3A, and Figure 3—figure supplement 1A–C), consistent with increased TTP protein levels in Huwe1 knock-out cells (Figure 2C). In line with TTP-dependent post-transcriptional effects, Huwe1-loss only altered mature Tnf mRNA concentrations, whereas its pre-mRNA levels remained unaffected (Figure 3B), indicating that Tnf transcription was likely unaffected. Neither did any differences stem from altered macrophage differentiation from bone marrow, as no differences in F4/80 surface expression were measured between sgROSA and sgHuwe1 BMDMs (Figure 3—figure supplement 1D). Instead, Actinomycin D mRNA chase experiments indicated that the decreased levels of pro-inflammatory mRNAs are consistent with a 57% decrease in Tnf mRNA stability (Figure 3C). Moreover, targeting of Zfp36 in Huwe1-deficient cells partially rescued Tnf mRNA concentrations (Figure 3—figure supplement 1E), indicating that the effects of Huwe1 loss on Tnf mRNA levels are at least in part TTP-dependent. Lastly, measurements of intracellular cytokines by flow-cytometry showed that the decreased Tnf mRNA levels in Huwe1 KO cells, were matched by significantly decreased intracellular TNF protein (Figure 3—figure supplement 1F).

Taken together, these data show that loss of Huwe1 increases the bio-active pool of cellular TTP, resulting in enhanced turn-over of TTP target mRNAs encoding pro-inflammatory mediators.

### HUWE1 regulates TTP phosphorylation and its increase is responsible for increased TTP stability

Since HUWE1 is a ubiquitin E3 ligase and was identified as a regulator of TTP protein stability by genetic means, we reasoned that the effects from its ablation on TTP could be direct through complex formation and ubiquitination of TTP, or indirect by influencing the activity or abundance of proteins that regulate TTP. Neither co-IP, nor TurboID proximity labeling assays identified complex formation between TTP and HUWE1 in cells (Figure 1—figure supplement 1I/J).

This suggested that the effects of HUWE1 on TTP may be indirect, although direct ubiquitination of TTP by HUWE1 cannot be ruled out as their interaction may have been too transient to detect in our assays. Attempts to address direct TTP ubiquitination by HUWE1, or any of the other E3 ligases identified in the genetic screen (Figure 2B and Figure 2—figure supplement 1A–B; VHL, UBE3C, and the Cullin adapters Elongin B/C) were hindered by the inability to purify sufficient amounts of recombinant TTP protein.

Since TTP stability is regulated for an important part through phosphorylation by the stress kinase p38-MK2 axis and to a lesser extent ERK (Brook et al., 2006; Deleault et al., 2008; Ronkina et al., 2019), we set out to determine whether Huwe1 ablation would alter TTP levels indirectly by affecting the cellular concentrations or activity of these kinases. Data from Huwe1 knock-out cells indicated that the effect of Huwe1 loss on TTP stability was predominantly at time points after the initial two hours of LPS stimulation (Figure 2E) during which TTP dephosphorylation of S52/S178 happens, resulting in its degradation (Kratochvill et al., 2011; Sedlyarov et al., 2016). Consistent with this finding, Huwe1 ablation did not significantly alter the total protein levels or change the early phosphorylation/activation kinetics of stress kinases p38, MK2, ERK, and JNK between 0 and 60 min post-LPS treatment (Figure 4—figure supplement 1A–D).

In contrast, ablation of Huwe1 strongly increased endogenous TTP levels upon its induction by LPS at all measured later time points from 2 to 16 hr post-stimulation (Figures 2E and 4A). In the same lysates, total and activated/phosphorylated levels of p38, MK2, ERK, and JNK were determined.

![Figure 4.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig4-v1.jpg)

**Figure 4.:** (A–D) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were incubated with LPS for the indicated time points (h). Phosphorylation of (A) p38, (B) MK2, (C) ERK, and (D) JNK was determined by western blot. (E) sgROSA- or sgHuwe1-RAW264.7-Dox-Cas9 cells were treated with LPS or left untreated. After 2 h of LPS treatment, cells were incubated with p38i, MK2i, ERKi, JNKi, or PP1/2 inhibitor Calyculin A (CalycA). TTP levels were analyzed by flow cytometry and normalized MFI plotted. Data represent the mean and s.d.; n=3 biological replicates. **p ≤ 0.01; ***p≤ 0.001; ****p ≤0.0001. Two-way ANOVA was performed. Dotted horizontal line indicates TTP abundance in the DMSO control at 6 hr post-LPS treatment. (F) sgROSA- or sgHuwe1-RAW264.7-Dox-Cas9 cells were treated with LPS for the indicated times. During the last 4 hr of LPS stimulation, the indicated inhibitors were added, after which endogenous TTP levels were analyzed by WB.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A–D) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were incubated with LPS for the indicated time points (min). Phosphorylation of (A) p38, (B) MK2, (C) ERK, and (D) JNK was determined by western blot. Total and phosphorylated kinase levels were quantified from non-saturated western blot signals and normalized to ACTIN. The ratio of the phosphorylated protein signals to their respective total protein signals was plotted. Data represent the mean and s.d.; n=3 biological replicates. Two-way ANOVA was performed. (E) RAW264.7-Dox-Cas9 cells expressing sgROSA or sgHuwe1 were treated with Dox for 5 days to induce Cas9. Cells were incubated with LPS for the indicated time points (h). Phosphorylation of p53 was assessed by western blot. As a control for the induction of p-p53, RAW264.7-Dox-Cas9 were treated with DNA damage inducer Etoposide for 6 hr.

The total levels of all four kinases varied slightly between the different time points post-LPS stimulation, yet these differences were independent of the targeted locus (ROSA or Huwe1). In contrast, Huwe1-targeting consistently increased the activated phosphorylated forms of all kinases at 2 hr post-stimulation (Figure 4A–D). While activated p38 and ERK levels in Huwe1-targeted cells were comparable to the ROSA-targeted control, or even lower, at later time points (Figure 4A–C), MK2 and JNK activation was increased for prolonged times, up to 6 hr post-stimulation (Figure 4B–D). Importantly, in the absence of LPS stimulation, Huwe1 knock-out did not affect, or even decreased, baseline phosphorylated levels of all kinases (Figure 4A–D). Moreover, Huwe1 ablation in the presence of LPS did not induce unrelated stress responses, such as p53 activation (Figure 4—figure supplement 1E), indicating that loss of Huwe1 does not induce a general stress response in the cell, but is specific for pro-inflammatory cellular conditions mediated by LPS. Together, these data indicated that in the absence of Huwe1, multiple stress kinases may be activated more, and for prolonged times.

Based on the increased levels of phosphorylated TTP (Figure 2C) and stress kinase activation in Huwe1 knock-out cells, we hypothesized that increased phosphorylation of TTP by some or all of the four deregulated kinases could be responsible for the elevated TTP protein stability. In particular, p38 and its downstream target MK2 were prime candidates, given their importance in LPS-induced TTP stabilization through phosphorylation of S52 and S178.

We reasoned that if HUWE1-dependent stability effects on TTP occured through altering TTP phosphorylation, that either preventing TTP phosphorylation by kinase inhibition, or saturating TTP phosphorylation by phosphatase inhibition would negate TTP stabilization in Huwe1 KO cells. To investigate whether the increased activity of the four individual kinases in Huwe1-targeted cells was causative for the increased TTP stability, a mixed genetic/inhibitor epistasis experiment was performed. To this end, endogenous TTP levels were assessed by intra-cellular staining in ROSA- or Huwe1-targeted cells, which were additionally treated with individual inhibitors of p38, MK2, ERK, JNK, or a combination of all four inhibitors (Figure 4E).

Consistent with our other results, Huwe1 knock-out increased TTP protein levels in 6 hr LPS-treated DMSO control cells (Figure 4E; sample set 3). In line with previous reports that the p38-MK2 axis is an important determinant of TTP stability, treatment of sgROSA-targeted cells with p38 or MK2 inhibitors significantly decreased TTP levels (Figure 4E; sample sets 4 and 5). However, simultaneous Huwe1 knock-out still elevated TTP levels in the presence of these individual inhibitors, indicating that either HUWE1 does not affect TTP through the p38-MK2 axis, or that there are compensatory mechanisms affecting TTP stability in the absence of p38-MK2 kinase activity.

Consistent with previous findings of a minor effect of ERK activity, and no effect of JNK on TTP stabilization (Deleault et al., 2008), ERK or JNK inhibition did not influence TTP levels (Figure 4E; sample sets 6 and 7). Moreover, the levels of TTP in the presence of either ERK or JNK inhibitors were still increased upon Huwe1 knock-out, indicating that the activity of neither of these individual kinases alone is required for the HUWE1-dependent effect on TTP.

We hypothesized that the deregulated increase in activity of multiple of these four stress kinases could in a partially functionally compensatory manner contribute to elevated TTP phosphorylation (Figure 4A–D) and stability. Indeed, inhibition of all four kinases (4i) simultaneously rendered TTP highly unstable as expected, yet in contrast to the single kinase inhibitors, this was no longer affected by Huwe1 knock-out (Figure 4E; sample set 8, and Figure 2F). From these data, we concluded that the HUWE1 effect on TTP stability is dependent on the activity of multiple stress kinases. Together, these results indicate that HUWE1 is important for curtailing TTP phosphorylation, thereby indirectly influencing TTP stability. We reasoned that the increased TTP phosphorylation in Huwe1 knock-out cells could stem from either increased phosphorylation by the stress kinases, and/or decreased dephosphorylation.

Since MK2/p38, ERK, and JNK are activated/phosphorylated through independent cellular pathways, yet inactivated/dephosphorylated by the same phosphatases as TTP itself (PP1/2) (Kruse et al., 2020; Nguyen and Shiozaki, 1999; Takekawa et al., 1998; Takekawa et al., 2000; Warmka et al., 2001), we reasoned that it was most likely that HUWE1 may be important to regulate PP1/2 activity or its cellular concentrations. Therefore, we hypothesized that decreased PP1/2 output in Huwe1 knock-out cells could prolong TTP phosphorylation by: (i) diminishing direct TTP dephosphorylation by PP1/2, and (ii) indirectly prolonging stress kinases activation as a consequence of their diminished dephosphorylation by PP1/2.

To test this hypothesis, sgROSA or sgHuwe1 cells were treated with LPS for 6 hr, and from 2 hr onward, co-incubated with PP1/2 inhibitor Calyculin A (Figure 4E–F). As expected, preventing dephosphorylation by this inhibitor stabilized TTP, and prevented TTP degradation by 6 hr of LPS treatment (Figure 4E; compare sgROSA 6 hr LPS with sgROSA 6 hr LPS +CalycA; sample set 9, and Figure 2F). In contrast to sgHuwe1 samples treated for 6 hr with LPS (in which TTP protein levels were increased), Huwe1 knock-out no longer increased TTP protein concentrations in the presence of Calyculin A (Figure 4E; compare sgHuwe1 6 hr LPS with sgHuwe1 6 hr LPS +CalycA, and Figure 2F).

From these results, we conclude that in the absence of HUWE1, decreased cellular output of PP1/2 may prolong stress kinase activation. Increased kinase activity and decreased dephosposphorylation of TTP by PP1/2 consequently increases TTP phosphorylation, thereby stabilizing it.

### HUWE1 controls only a small fraction of proteasome targets, and regulates the abundance of TTP paralog ZFP36L1

HUWE1 has been shown to associate with proteasomes (Besche et al., 2009), the biological significance of which has remained elusive. We reasoned that HUWE1 might be important for proteasome activity, and its ablation could cause a general impaired degradation of proteasome targets such as TTP. To investigate whether this was the case, we compared the proteomes of LPS-stimulated RAW264.7-Dox-Cas9 cells in which we targeted either Huwe1 or proteasome core particle component Psmb7 by label-free mass-spectrometry.

As expected, Psmb7 targeting altered the abundance of a large number of proteins, many of which are known targets of proteasomal degradation (Figure 5—figure supplement 1A and Figure 5—source data 2). In contrast, Huwe1 ablation significantly changed the concentrations of only a select number of proteins (Figure 5A and Figure 5—figure supplement 1B). In line with expectations of an E3 ligase, HUWE1 targets showed a trend of also being increased in Psmb7 knock-out cells, and vice versa (Figure 5A and Figure 5—figure supplement 1A/B). However, there was no clear correlation between the most affected proteins in the two genotypes, indicating that HUWE1 is likely not essential for proteasome function in cells, and that the increase of TTP in Huwe1 knock-out cells is unlikely to have resulted from diminished overall proteasome activity. Among the differentially regulated proteins were factors previously identified as HUWE1 targets (Cassidy et al., 2020; Thompson et al., 2014; Xu et al., 2016), including GRB2, CHEK1, and CDC34 (Figure 5—figure supplement 1C).

![Figure 5.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig5-v1.jpg)

**Figure 5.:** (A) RAW264.7-Dox-Cas9 expressing sgROSA, sgHuwe1 or sgPsmb7 were treated with Dox for 3 days to induce Cas9. Proteome changes were assessed by quantitative mass spectrometry. Proteins classified as HUWE1 targets are highlighted in red. Shared HUWE1 and proteasome targets are labelled in the Psmb7 knock-out volcano plot. (adjusted p-value ≤0.05 and Fold Change (Log2) ≥0.5; n=3 biological replicates). (B) Venn diagram showing the overlap between proteome changes of Huwe1-targeted RAW264.7, A375, and SW620 cell lines. Shared targets are listed (adjusted p-value ≤0.05 and Fold Change (Log2) ≥0.5; n=3 biological replicates). (C) Volcano plots representing proteome changes of Huwe1- and AAVS1/ROSA-targeted A375 human melanoma cells and RAW264.7-Dox-Cas9 cells (adjusted p-value ≤0.05 and Fold Change (Log2) ≥0.5; n=3 biological replicates). The shared HUWE1 target ZFP36L1 is highlighted. (D) sgROSA or sgHuwe1 knockout RAW264.7-Dox-Cas9 cells were treated with Dox for 5 days to induce Cas9, followed by LPS treatment for the indicated times (h). Endogenous ZFP36L1 protein levels were determined by western blot.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Proteome changes in RAW264.7-Dox-Cas9 cells expressing sgPsmb7 by quantitative mass-spectrometry. Proteins classified as PSMB7 targets are highlighted in orange and displayed in the Huwe1 knock-out volcano plot. (adjusted p-value ≤0.05 and Fold Change (Log2) ≥0.5; n=3 biological replicates) (B) Venn diagram showing the overlap in proteome changes of Psmb7- and Huwe1-targeted RAW264.7-Dox-Cas9 cells. Shared targets are listed. Twenty-nine proteins were identified as common targets (adjusted p-value ≤0.05 and Fold Change (Log2) ≥0.5; n=3 biological replicates). (C) Volcano plot representing proteome changes of Huwe1- and ROSA- targeted RAW264.7-Dox-Cas9 cells. Known HUWE1 targets are highlighted in orange (adjusted p-value ≤0.05 and Fold Change (Log2) ≥0.5; n=3 biological replicates). (D–E) Proteome changes of Huwe1-targeted RAW264.7, A375, and SW620 cell lines are plotted. PP1/2 protein components in (D), and MAPK proteins in (E), are highlighted as solid dots. Only significantly enriched proteins are labelled (adjusted p-value ≤0.05 and Fold Change (Log2) ≥0.5; n=3 biological replicates).

Our data so far indicated that HUWE1 is important for proper regulation of TTP phosphorylation, and that in its absence the equilibrium shifted to a hyper-phosphorylated state (Figure 4), dependent on a decrease in phosphatase activity, and an increase in stress kinase activity, without major effects on their protein levels.

To further assess in an unbiased manner whether Huwe1 deficiency would affect MAPK or PP1/2 protein levels, we extended our proteome mass-spectrometry for two additional human cell lines (A375 and SW620). Consistent with our previous findings (Figure 4), Huwe1 ablation did not substantially or consistently affect the protein levels of detected MAPK or PP1/2 subunits in the three cell lines (Figure 5—figure supplement 1D/E). In line with the data presented above (Figure 4), this suggests that the hyper-phosphorylated TTP state in Huwe1-targeted cells does not result from changes in MAPK or PP1/A protein levels.

Previous studies have indicated that HUWE1 can target broader classes of cellular substrates (Grabarczyk et al., 2021; Hunkeler et al., 2021), but that the targeted proteins may be cell type specific to some degree. Analysis of proteome changes in the three different cell lines identified seven proteins that were consistently increased in all Huwe1-targeted cell lines (Figure 5B). Moreover, the protein concentration of other proteins was changed in only two of the three cell lines, whereas it was not detected in the third (Figure 5B).

We reasoned that any of these common deregulated proteins in Huwe1 knock-out cells could contribute to the TTP hyper-phosphorylation/stabilization phenotype. However, analysis of overlap between factors that regulate TTP abundance identified in the genetic screen (Figure 2B and Figure 2—figure supplement 1A), and proteins deregulated by Huwe1-ablation did not identify any overlap, suggesting that these Huwe1-regulated proteins are unlikely to drive the effect on TTP protein stability.

Importantly, proteome measurements by mass-spectrometry are limited to detection of only reasonably abundant proteins. Even after LPS stimulation, no TTP peptides were identified in any of the three analyzed cell lines (Figure 5B), indicating that its absolute intra-cellular concentrations in these cells are too low to be detected by this method. In contrast, peptides of its paralog ZFP36L1 were readily identified in RAW264.7 and A375 cells and among the most increased proteins identified in Huwe1-targeted cells (Figure 5C). In line with this observation, independent western blot analysis of ZFP36L1 in cell lysates from Huwe1-deficient RAW264.7 cells showed that ZFP36L1 protein levels were increased in Huwe1 knock-out cells (Figure 5D).

Collectively, these findings indicate that Huwe1 ablation does not alter MAPK or PP1/2 protein levels, but that rather their differential activation alters TTP phosphorylation and stability. Moreover, ZFP36L1 abundance is regulated by HUWE1, akin to its closest related family member -TTP-, indicating that they could be regulated by HUWE1 in a conserved manner.

### Residues in the TTP 234-278 region are important for its stability

Lysines are exclusively located in the TTP zinc finger domain, and our data indicate that this is the site of poly-ubiquitination (Figure 1—figure supplement 1C–G). In line with this notion, upon mutation of the five lysine residues in its zinc finger domain (KtoR), TTP accumulated as a stable, phosphorylated species (Figure 6A–B and Figure 6—figure supplement 1A–B). Moreover, this mutant was no longer affected by HUWE1 loss, indicating that the effects of HUWE1 on TTP stability are dependent on ubiquitination in the zinc finger domain.

![Figure 6.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig6-v1.jpg)

**Figure 6.:** (A) Schematic representation of 3xHA-TTP mutants. Colors denote amino acid substitutions. ZF indicates the zinc finger domain, and the three tetraprolin motifs are presented as dark grey boxes. (B–E) sgAAVS1- and sgHUWE1-depleted HEK-293T-Cas9 cells were transfected with the indicated mutants, and 3xHA-TTP stability was determined by western blot. mCherry is expressed as a stable internal control through a P2A site.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) Alignment of mouse and human TTP and ZFP36L1 orthologs. (B) TTP protein levels from Figure 6B were quantified from non-saturated western blot signals, normalized to the internal control mCherry, and plotted. Data represent the mean and s.d.; n=2 biological replicates. (C) HEK-293T-Cas9 cells expressing sgAAVS1 or sgHUWE1 were transfected with plasmids encoding HA-tagged wtTTP or its S52/178 A mutant. HA-TTP protein levels were analyzed by WB. n=6 biological replicates, analyzed by unpaired t-test. (D) TTP protein levels from Figure 6C were quantified from non-saturated western blot signals, normalized to the internal control mCherry, and plotted. Data represent the mean and s.d.; n=2 biological replicates. (E) HEK-293T-Cas9 cells expressing sgAAVS1 or sgHUWE1 were transfected with plasmids encoding the HA-tagged TTP-Δ4 mutant. HA-TTP protein levels were quantified by WB. n=2 biological replicates, analyzed by unpaired t-test. (F–G) TTP protein levels from Figure 6D–E were quantified from non-saturated western blot signals, normalized to the internal control mCherry, and plotted. Data represent the mean and s.d.; n=2 biological replicates.

We reasoned that the E3 ligase ubiquitinating TTP at that site could bind TTP in its folded zinc finger domain, or that the mRNA-engaged TTP pool could be the predominant HUWE1-dependent target. Therefore, we addressed whether a TTP mutant with a disrupted zinc finger domain (C116R, C139R; Lai et al., 2018; Ming et al., 2001) would be stabilized. Zinc finger domain disruption did not accumulate at higher steady-state levels than its wtTTP counter-part, and was still increased upon HUWE1 loss (Figure 6B and Figure 6—figure supplement 1B), demonstrating that neither recognition of the folded zinc finger domain structure by an E3 ligase, nor TTP functionality are required for the HUWE1 effects.

Our data support a role of HUWE1 in determining TTP phosphorylation, and thereby its stability. Therefore, we next analyzed whether phosphorylation of the two best-characterized TTP residues in this context (S52, S178) are important for HUWE1 effects. As for the zinc finger domain mutant, a S52A/S178A TTP mutant was still stabilized by HUWE1 loss (Figure 6B and Figure 6—figure supplement 1B/C). This indicated that while phosphorylation of these residues importantly controls TTP stability, HUWE1 effects are likely independent of these phospho-residues.

Together, these data from full-length TTP point mutants suggest that an unknown E3 ligase likely binds TTP outside of its zinc finger domain, but ubiquitinates it on lysines inside the zinc finger domain. Moreover, we concluded that HUWE1 regulation of TTP stability and phosphorylation is independent of the MK2-stabilized S52/S178 residues. This is consistent with the finding that TTP levels were still increased in Huwe1 knock-out cells treated with inhibitors of the p38 and MK2 kinases phosphorylating these two sites (Figure 4E; subsets 4–5). Lastly, these data indicate that TTP does not require an intact zinc finger domain for stability, suggesting that TTP engagement with target mRNAs is likely not a prerequisite for HUWE1-dependent stability regulation.

Next, we set out to determine which part of TTP regulates its HUWE1-dependent phosphorylation and stability. To this end, progressive N- and C-terminal TTP deletion mutants (Figure 6A) were analyzed in cells for their steady-state concentrations, phosphorylation, and sensitivity to HUWE1 ablation. Since TTP is predicted to be mostly disordered outside of its zinc finger domain (https://alphafold.ebi.ac.uk/entry/P22893), we reasoned that the effects of the truncations on overall protein structure would be limited.

N-terminal deletions did neither affect TTP protein levels, its phosphorylation, nor the effect of HUWE1 loss (Figure 6C and Figure 6—figure supplement 1D–E; deletions ΔN1-4), indicating that HUWE1 does not influence TTP stability through residues N-terminal of the zinc finger domain. Likewise, the two most C-terminal deletions did also not affect TTP stability (Figure 6D and Figure 6—figure supplement 1F; ΔC1-2). In contrast, further truncation of the C-terminus rendered mutant ΔC3 (259–278 region) less sensitive to HUWE1 loss, yet retained its heterogeneous size distribution for phosphorylated species. Further deletion of the 234–258 region in the ΔC4 mutant strongly stabilized TTP at a homogeneously phosphorylated size, and rendered it insensitive to HUWE1 knock-out (Figure 6D and Figure 6—figure supplement 1F). Likewise, the ΔC5 and ΔC6 mutants were insensitive to HUWE1 knock-out, but accumulated as unphosphorylated TTP species. Together, these data indicate that the 234–278 region (Figure 6D and Figure 6—figure supplement 1F) is important for HUWE1-dependent regulation of TTP stability, and its phosphorylation status.

Since the TTP-ΔC3 mutant was stabilized in a HUWE1-insensitive manner (Figure 6D and Figure 6—figure supplement 1F), we reasoned that this region (259-278) could be important for proteasomal targeting (e.g. an E3 ligase binding site). In contrast, the TTP-ΔC4 mutant accumulated as a lower MW homogenously phosphorylated TTP species (Figure 6D and Figure 6—figure supplement 1F), suggesting that the 234–258 region regulates TTP stability by affecting its phosphorylation status (e.g. a phosphatase binding site).

To test these possibilities, we analyzed mutants in which either only the 259–278 or 234–258 regions were deleted, while retaining the rest of the protein (Figure 6A). Consistent with the data from Figure 6D, a TTP mutant only lacking the 259–278 region was strongly stabilized, accumulated predominantly as a relatively homogeneous phosphorylated species, and was insensitive to HUWE1 knock-out (Figure 6E and Figure 6—figure supplement 1G). Moreover, deletion of the 234–258 region resulted in TTP hyper-phosphorylation (Figure 6E and Figure 6—figure supplement 1G), consistent with the idea of it being important for phosphatase binding.

Together, these data indicate that the TTP ΔC3-specific region (259-278) is consistent with a possible binding site for an E3 ligase, whereas the ΔC4-specific region (234-258) is a likely interaction site of a phosphatase (Figure 7A). Importantly, the ΔC5- and ΔC6-mutants were stabilized, yet not hyperphosphorylated (Figure 6B). This suggests that the phosphorylated residues contributing to TTP stabilization in HUWE1 knock-out cells are likely in the possible E3 ligase binding site in the TTP ΔC3-specific region (259-278) (Figure 7A).

![Figure 7.](https://cdn.elifesciences.org/articles/83159/elife-83159-fig7-v1.jpg)

**Figure 7.:** (A) Model indicating the TTP regions in its C-terminus speculated to recruit PP1/2 and an unknown E3 ligase that ubiquitinates the zinc finger domain. (B) Model of TTP stability regulation through phosphorylation in wild-type cells and Huwe1-deficient cells.

In summary, we provide evidence for ubiquitin-dependent proteasomal degradation as a key regulatory mechanism for TTP protein abundance in cells. A genetic screen identified HUWE1 as a strong regulator of TTP proteasomal turn-over. In the absence of Huwe1, TTP is heavily phosphorylated and stabilized, which is dependent on multiple ubiquitination sites in the TTP zinc finger domain, and phosphorylation in the 259–278 region. We propose that this region in its unphosphorylated form is also a likely binding site for an E3 ligase directing TTP ubiquitination and degradation (Figure 7A). Moreover, the adjacent 234–258 region is consistent with an interaction site for the main TTP phosphatases (PP1/2) (Figure 7A).

We propose a model in which HUWE1 under physiological conditions curtails stress kinase activation, thereby limiting their stabilizing effects on TTP (Figure 7B). However, in the absence of Huwe1, the collective activity increase of these stress kinases results in TTP hyper-phosphorylation in the 259–278 region, increased TTP stability, and decreased pro-inflammatory output. Since we found that TTP phosphorylation is inversely correlated with ubiquitination and degradation, we speculate that phosphorylation in this region could prevent E3 ligase binding (Figure 7A).

## Discussion

Previous studies have predicted that TTP is disordered outside of its zinc finger domain, and showed that these unstructured regions contribute to its rapid proteasomal turn-over (Ngoc et al., 2014; Ross et al., 2015). Protein disorder is often associated with proteasomal turn-over, as these regions often contain degrons, accessible ubiquitination sites, or provide an initiation side for threading into the proteasome and initiating unfolding and translocation into the catalytic chamber (Aufderheide et al., 2015; van der Lee et al., 2014). However, previous work did not identify TTP poly-ubiquitination, and showed that incubation of TTP with purified 20S proteasomes -which lack the Ub-receptor containing 19 S regulatory particle-, were sufficient to degrade TTP (Ngoc et al., 2014).

Work from Ngoc et al. showed that fusion to GFP of either the N-terminal TTP part, or the TTP C-terminal part (aa 214–436), destabilized GFP in cells (Ngoc et al., 2014). Thus, the GFP destabilization was seemingly indiscriminate, and possibly caused by the disordered nature of the fusion construct per se. Since the C-terminal TTP part fused to GFP included aa 214–436, we cannot rule out that part of this effect was HUWE1-dependent. However, the discrepancy with our finding that the TTP N-terminus does not contribute to HUWE1-dependent TTP regulation, may suggest that the GFP fusions by Ngoc et al. were destabilized by more general protein principles, rather than HUWE1-specific effects.

It has been reported that oxidized, unfolded proteins could be directly degraded by 20S proteasomes (Davies, 2001; Inai and Nishikimi, 2002). However, the prevailing notion is that association of a regulatory particle is critical to open access to the catalytic chamber (Coux et al., 1996; Davies, 2001; Driscoll and Goldberg, 1990; Eytan et al., 1989), and efficient substrate degradation in cells. Here, we demonstrate robust poly-ubiquitination of TTP in denaturing RAW264.7 lysates, indicating that these poly-ubiquitin chains are covalently attached to TTP, and do not interact through a putative ubiquitin-interaction domain. Moreover, we show that mutation of lysines in the zinc finger domain stabilized TTP, and that an inhibitor preventing de novo ubiquitination in cells, stabilized TTP. These data demonstrate that poly-ubiquitination of TTP is essential for its degradation, which is likely mediated by 26S proteasomes.

In contrast to other published work (Ngoc et al., 2014), non-degrative TRAF2-driven K63-linked poly-ubiquitination of TTP has been previously reported to mediate the balance between NFκB and JNK-dependent signaling using transfected HEK-293T cells (Schichl et al., 2011). Consistent with TTP being rapidly proteasomally turned-over, we readily detected K48-linked poly-ubiquitination of TTP in the same cell system, yet failed to detect substantial K63-linked poly-ubiquitination. This dissimilarity could stem from differences in expression levels, lack of co-expression of TRAF2, or insufficicient sensitivity of the K63-specific antibody in our assays. As TNF and TLR activation activate NFκB and stress kinases -including JNK- in parallel, it will be of interest to further dissect in future studies the interplay between HUWE1-dependent phospo-regulation of TTP, and its K63-ubiquitination in stimulated myeloid cells.

Most proteins with disordered regions will eventually be degraded in in vitro reactions containing high concentrations of 20S proteasomes (Liu et al., 2003; Lu et al., 2015). This could explain the previous finding of ubiquitin-independent TTP degradation in vitro (Ngoc et al., 2014). Future comparisons of TTP degradation kinetics of ubiquitinated and non-ubiquitinated forms in the presence of 26S proteasomes will be important to further address this issue.

Several E3 ligases to putatively poly-ubiquitinate TTP were identified in our genetic screen (Figure 2): HUWE1, VHL, UBE3C, and the Cullin adapters Elongin B/C. Huwe1 ablation most robustly stabilized TTP, based on which we hypothesized that HUWE1 may directly poly-ubiquitinate TTP. However, multiple independent techniques, including TurboID proximity labeling and co-IPs, failed to identify an interaction between TTP and HUWE1, which suggested that it may instead indirectly influence TTP stability.

At this point, we cannot rule out that HUWE1 directly poly-ubiquitinates TTP, resulting in its proteasomal degradation. Alternatively, one or more of the other identified E3 ligases could contribute to direct TTP ubiquitination. If indeed the other E3 ligases contribute to TTP ubiquitination, the fact that their knock-out phenotype is substantially less than that of Huwe1 loss (Figure 2—figure supplement 1B) may suggest that multiple of them could be functionally redundant. Irrespective of potential direct TTP ubiquitination by HUWE1, multiple lines of evidence point towards a strong contribution of HUWE1-dependent differential TTP phosphorylation as an indirect means to control TTP stability and functional activity. This is consistent with our finding that TTP phosphorylation and ubiquitination appear to be inversely correlated, as the TTP KtoR mutant accumulates as a hyper-phosphorylated species (Figure 6B).

Published data support a model in which TTP upon translation is initially phosphorylated by the p38/MK2 kinase axis on residues S52 and S178 (mTTP numbering), resulting in its stabilization, yet repressing TTP function (Deleault et al., 2008; Hitti et al., 2006; Kratochvill et al., 2011; Ross et al., 2015). At later stages, diminishing p38/MK2 kinase activity is thought to shift the equilibrium to dephosphorylation of TTP at these residues, rendering it active, but unstable. Under these conditions, TTP is rapidly turned over by the proteasome (Deleault et al., 2008; Ross et al., 2015).

Consistent with these data, we also found that an S52A/S178A mutant is unstable in the absence and presence of LPS stimulation (Figure 6B, and Figure 6—figure supplement 1C). Importantly, this mutant was still stabilized in the absence of Huwe1, indicating that the stabilizing effects of phosphorylation on S52/S178 are independent of HUWE1. Moreover, it indicates that HUWE1-dependent effects on TTP stability target other sites in TTP. Thus, S52/S178 phosphorylation seems predominantly relevant for TTP stabilization at the early (2–3 hr) time points post-LPS-stimulation (Ross et al., 2015), whereas HUWE1-dependent effects occur later (between 3–16 hr) post-LPS stimulation. In contrast to S52/178, TTP phosphorylation in its C-terminal 259–278 region and its associated stabilization in the absence of Huwe1, is paralleled by decreased concentrations of known TTP mRNA targets, which suggests that phosphorylation in this region may not inhibit TTP functional output.

To uncouple LPS-induced Zfp36 transcription from PTMs influencing TTP protein stability, we complemented experiments using endogenous TTP with exogenously expressed counterparts. In the absence of LPS stimulation, Huwe1 loss did increase exogenous TTP, albeit rather mildly (Figure 2C and Figure 2—figure supplement 1B). In contrast, upon LPS stimulation and stress kinase activation, the effect of Huwe1 knock-out was much stronger, resulting in strong TTP protein accumulation, which included a substantial fraction of phosphorylated forms (Figure 2C and F, and Figure 2—figure supplement 1B). These results suggest that there may be low baseline levels of activated stress kinases in the cell that affect TTP stability in the absence of LPS. However, in contrast to these mild phenotypes, the predominant effects of Huwe1 loss on TTP protein stability and phosphorylation occur after LPS stimulation, in line with the notion that HUWE1 regulates TTP stability through influencing stress kinase-dependent TTP phosphorylation (Figures 5 and 6).

Huwe1 loss increased the activity of multiple stress kinases (Figure 4A–D) without affecting their total protein levels. The previous findings that (i) the phosphorylation and activation of these kinases is controlled by PP2A (Kruse et al., 2020; Nguyen and Shiozaki, 1999; Takekawa et al., 1998), and (ii) the observation that combined inhibition of the stress kinases, or inhibition of PP1/2 activity with Calyculin A, rescued Huwe1 knock-out effects on TTP (Figure 4E–F), suggest that HUWE1 may be important for PP1/2 activity. In line with this notion, decreased PP1/2 activity in Huwe1 knock-out cells could affect TTP phosphorylation and stability by directly affecting its dephosphorylation, and in parallel maintain high stress kinase activity, which increases TTP phosphorylation even more.

This functional interaction between HUWE1 and the activity of PP1/2 and stress kinases has not been described previously, although it should be noted that HUWE1 has been reported to control the abundance and activity of other kinases and phosphatases (Cassidy et al., 2020; Jang et al., 2014; Su et al., 2021). Our findings broaden the understanding of how HUWE1 may indirectly influence numerous cellular proteins beyond direct recognition as ubiquitination substrates.

Taken together, our data support a model in which HUWE1 is important to maintain PP1/2 cellular output, and curtail stress kinase activation. This in turn limits phosphorylation in the TTP region spanning residues 259–278, allowing for recruitment of HUWE1 itself or another -yet unidentified- E3 ligase to that same region, subsequent poly-ubiquitination on lysine residues in the zinc finger domain, and ultimately proteasomal degradation. Phosphorylation in this region could prevent E3 ligase binding. Although the HUWE1-dependent phosphorylation effect appears to be dependent on the putative E3 ligase binding site (259-278), phosphatase recruitment to the 234–258 region in TTP seemingly controls dephosphorylation of most or all phospho-sites on TTP (Figure 6C). Since ZFP36L1 abundance is also strongly regulated by HUWE1, this suggests that its C-terminal region is orthologous to TTP 234–278 and how it controls HUWE1-dependent degradation could be conserved across these family members.

## Materials and methods

### Vectors

The lentiviral mouse genome-wide sgRNA library (six sgRNAs/gene) has been described previously (Michlits et al., 2020). Lentiviral vectors driving the expression of a single sgRNA or a dual sgRNA from a U6 promoter, and either eBFP2 or iRFP from a PGK promoter have been described previously (de Almeida et al., 2021). Single sgRNA CDSs were cloned in pLentiCRISPRv2 (Addgene plasmid 52961) to perform stable knock-outs in HEK293T cells. A Dox-inducible Cas9 lentiviral vector was modified from LT3GEPIR (Addgene plasmid 111177): T3G-GFP-(miR-E)-PGK-Puro-IRES-rtTA3, in which the GFP-mirE cassette was replaced by Cas9-P2A-GFP from pLentiCRISPRv2. The TTP stability reporter (pLX-SFFV-mCherry-TTP-P2A-BFP) was constructed by cloning the open-reading frame (ORF) of murine TTP into a modified pLX303 vector (Addgene plasmid 25897). Lentiviral N-terminally HA-tagged-TTP deletions or point mutant variants were obtained by cloning the indicated variants of murine TTP ORF into a modified pLX303 vector. For this purpose, cDNAs encoding mTTP mutants were purchased from Twist Bioscience. All 3xHA-TTP constructs co-expressed mCherry through a P2A site to monitor protein expression and protein stability. All plasmids and sgRNAs used in this study are listed in Table 1 and Table 2.

**Table 1.**
 Vectors.


<table>
  <thead>
    <tr>
      <th>Plasmid</th>
      <th>Purpose</th>
      <th>Reference or source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pRRL-TRE3G-Cas9-P2A-GFP-PGK-IRES-rtTA3</td>
      <td>Dox inducible Cas9</td>
      <td>Johannes Zuber, IMP</td>
    </tr>
    <tr>
      <td>pLX303-mCherry.TTP-P2A-BFP</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔC1</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔC2</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔC3</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔC4</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔC5</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔC6</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔN1</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔN2</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔN3</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔN4</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP Δ259–278</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ΔC234-258</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP Δ206–233</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP KtoR</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP S52A S178A</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP ZNF C116R C139R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K97R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K115R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K133R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K135R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K141R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K97R/K115R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K97R/K115R/K133R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K97R/K115R/K133R/K135R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K135R/K141R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K133R/K135R/K141R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pLX303-MYC-mCherry-P2A-3xHA.TTP K115R/K133R/K135R/K141R</td>
      <td>TTP reporter</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>CMV-Flag-TTP</td>
      <td>TTP reporter</td>
      <td>Pavel Kovarik, Max Perutz Labs</td>
    </tr>
    <tr>
      <td>DualCRISPR-hU6-sgRNA-mU6-sgRNA-EF1as-BFP</td>
      <td>Dual sgRNA</td>
      <td>de Almeida M, Hinterndorfer M et al, 2021</td>
    </tr>
    <tr>
      <td>pLentiv2-U6-PGK-iRFP670-P2A-Neo</td>
      <td>Single sgRNA</td>
      <td>de Almeida M, Hinterndorfer M et al, 2022</td>
    </tr>
    <tr>
      <td>pLentiv2-U6-PGK-BFP-P2A-Neo</td>
      <td>Single sgRNA</td>
      <td>de Almeida M, Hinterndorfer M et al, 2023</td>
    </tr>
    <tr>
      <td>PRRL-PBS-U6-sgRNA-EF1as-Thy1-P2A-NeoR (sgETN)</td>
      <td>Library sgRNA</td>
      <td>Johannes Zuber, IMP</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 sgRNA coding sequences.


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>Species</th>
      <th>Sequence (5' to 3')</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ROSA_1 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>AGATGGGCGGGAGTCTTC</td>
    </tr>
    <tr>
      <td>ROSA_2 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>TTTAGATGGGCGGGAGTCTTCGTTTA</td>
    </tr>
    <tr>
      <td>Huwe1_1 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GATTTGCTGCAGTTCCAAG</td>
    </tr>
    <tr>
      <td>Huwe1_2 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>ATAAAATTCAAAGTGTAGTG</td>
    </tr>
    <tr>
      <td>Psmb7_1 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GCTGTAACAACTCTCGGG</td>
    </tr>
    <tr>
      <td>Psmb7_2 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GAAAACTGGCACTACCATCG</td>
    </tr>
    <tr>
      <td>Vcpip1 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GACGTGCTCTGGTTCGATG</td>
    </tr>
    <tr>
      <td>Ppil4 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GTGTTTGGTGAAGTGACAGA</td>
    </tr>
    <tr>
      <td>Tceb1 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GCTGAGAATGAAACCAACG</td>
    </tr>
    <tr>
      <td>Ube3c (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GAGAGTCAAAGTTCAAAA</td>
    </tr>
    <tr>
      <td>Ddx23 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GGATGGAGCGGGAGACCAA</td>
    </tr>
    <tr>
      <td>Cnot10 (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GATTTCACAGGGTAGCGG</td>
    </tr>
    <tr>
      <td>Ttp (RAW264.7 &amp; BMDMs)</td>
      <td>mouse</td>
      <td>GAAGCGGGCGTTGTCGCTACG</td>
    </tr>
    <tr>
      <td>AAVS1_1 (RKO &amp; HEK-293T)</td>
      <td>human</td>
      <td>CTGTGCCCCGATGCACAC</td>
    </tr>
    <tr>
      <td>AAVS1_2 (RKO &amp; HEK-293T)</td>
      <td>human</td>
      <td>GCTGTGCCCCGATGCACAC</td>
    </tr>
    <tr>
      <td>HUWE1_1 (RKO &amp; HEK-293T)</td>
      <td>human</td>
      <td>GTGCGAGTTATATCACTGGG</td>
    </tr>
    <tr>
      <td>HUWE1_2 (RKO &amp; HEK-293T)</td>
      <td>human</td>
      <td>GTGCGAGTTATATCACTGGGTGG</td>
    </tr>
    <tr>
      <td>AAVS1_3 (A375 &amp; SW620)</td>
      <td>human</td>
      <td>GCTGTGCCCCGATGCACAC</td>
    </tr>
    <tr>
      <td>AAVS1_4 (A375 &amp; SW620)</td>
      <td>human</td>
      <td>GCTTGGCAAACTCACTCTT</td>
    </tr>
    <tr>
      <td>HUWE1_3 (A375 &amp; SW620)</td>
      <td>human</td>
      <td>GTGCGAGTTATATCACTGGG</td>
    </tr>
    <tr>
      <td>HUWE1_4 (A375 &amp; SW620)</td>
      <td>human</td>
      <td>GACAGTGGAGAATATGTCA</td>
    </tr>
  </tbody>
</table>

### Cell culture and reagents

All experiments in this study have been reproduced at least twice in independent experiments. Cell lines were tested negative for mycoplasma contamination. All cell lines used in this study and their applications are listed in Table 3. None of the used cell lines are on the current list of commonly misidentified cell lines (v12). Parental cell lines were obtained from ATCC: A375 (CRL-1619), RKO (CRL-2577), SW620 (CCL-227), and authenticated by short tandem repeat analysis. These cell lines were used to generate dox-inducible Cas9 derivatives as indicated in Table 3. RAW264.7 Dox-Cas9 cells were generated by transducing RAW264.7 cells with pRRL-TRE3G-Cas9-P2A-GFP-PGK-IRES-rtTA3 lentiviral vector. Cas9 expression was induced with 500 ng/ml of Docycycline hyclate (Dox, Sigma-Aldrich, D9891) and single cells were sorted by FACS into 96-well plates using a FACSAria III cell sorter (BD Biosciences) to obtain single-cell-derived clones. Cas9 function and leakiness of the TRE3G promoter in the absence of Dox was tested in competitive proliferation assays. For mCherry-TTP reporter cells, pLX303-SFFV-mCherry-TTP-P2A-BFP was transduced into RAW264.7-Dox-Cas9 cells, and cells co-expressing mCherry and BFP were sorted by FACSAria III cell sorter into 96-well plates to obtain single-cell-derived clones. To obtain 3xHA-TTP expressing cells, pLX303-SFFV-mCherry-P2A-3xHA-TTP was transduced into RAW264.7-Dox-Cas9 cells, and cells expressing mCherry were bulk sorted using a FACSAria III. Bone marrow-derived macrophages (BMDMs) were differentiated from bone marrow isolated from femurs and tibias of 8-to-12-week-old mice from Cas9 knock-in mice of both sexes (Platt et al., 2014). Femur and tibia marrow was centrifuged and cells were resuspended in DMEM. Cells were differentiated in DMEM (Sigma-Aldrich, D6429) containing recombinant M-CSF for 10 days. All cells were cultured at 37 °C and 5% CO2 in a humidified incubator. All animals were maintained in the pathogen-free animal facility of the Research Institute of Molecular Pathology, and all procedures were carried out according to an ethical animal license that is approved and regularly controlled by the Austrian Veterinary Authorities (License Number: GZ: 516079/2017/14). All reagents used in this study are listed in the Table 4. All antibodies used in this study are listed in Table 5.

**Table 3.**
 Cells and culture conditions.


<table>
  <thead>
    <tr>
      <th>Cell lines and primary cells</th>
      <th>Type</th>
      <th>Reference or source</th>
      <th>Purpose</th>
      <th>Media</th>
      <th>Supplements</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RAW264.7</td>
      <td>Murine macrophages</td>
      <td>ATCC TIB-71</td>
      <td>parental cell line</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>RAW264.7-Dox-Cas9</td>
      <td>Murine macrophages</td>
      <td>This study</td>
      <td>Dox-inducible Cas9</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>RAW264.7-Dox-Cas9 mCherry-TTP-P2A-BFP</td>
      <td>Murine macrophages</td>
      <td>This study</td>
      <td>mCherry-TTP reporter</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>RAW264.7-Dox-Cas9 mCherry-IkBα-P2A-BFP</td>
      <td>Murine macrophages</td>
      <td>This study</td>
      <td>mCherry-IkBα reporter</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>RAW264.7-Dox-Cas9 3xHA-TTP</td>
      <td>Murine macrophages</td>
      <td>This study</td>
      <td>3xHA-TTP reporter</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>Bone Marrow Derived Macrophages, BMDMs</td>
      <td>Murine macrophages</td>
      <td>This study</td>
      <td>constitutive Cas9 expression</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>HEK293T</td>
      <td>Human kidney neural tissue</td>
      <td>CRL-3216</td>
      <td>3xHA-TTP mutants</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>Lenti-X 293T</td>
      <td>Human kidney neural tissue</td>
      <td>Takara, Cat# 632180</td>
      <td>VLP production</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>RKO</td>
      <td>human colon carcinoma</td>
      <td>de Almeida M, Hinterndorfer M et al, 2021</td>
      <td>Dox-inducible Cas9</td>
      <td>RPMI 1640 (Thermo Fisher Scientific, 21875)</td>
      <td>10% FBS (Sigma-Aldrich, F7524), L-glutamine (4  mM, Gibco), sodium pyruvate (1  mM, Sigma-Aldrich), and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>A375</td>
      <td>human melanoma</td>
      <td>This study</td>
      <td>Dox-inducible Cas9</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524), L-glutamine (4  mM, Gibco) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
    <tr>
      <td>SW620</td>
      <td>human colon carcinoma</td>
      <td>This study</td>
      <td>Dox-inducible Cas9</td>
      <td>Dulbecco’s modified Eagle’s medium (DMEM; Sigma-Aldrich, D6429)</td>
      <td>10% FBS (Sigma-Aldrich, F7524), L-glutamine (4  mM, Gibco) and 1% penicillin/streptomycin (Sigma-Aldrich, P4333)</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 reagents.


<table>
  <thead>
    <tr>
      <th>Description</th>
      <th>Abbreviation</th>
      <th>Application</th>
      <th>Dilution/concentration</th>
      <th>Manufacturer</th>
      <th>Catalogue number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lipopolysaccharides from Escherichia coli O55:B5</td>
      <td>LPS</td>
      <td>Cell culture</td>
      <td>10 ng/ml</td>
      <td>Sigma-Aldrich</td>
      <td>L2637</td>
    </tr>
    <tr>
      <td>Cycloheximide</td>
      <td>CHX</td>
      <td>Cell culture</td>
      <td>40 μg/m</td>
      <td>Sigma-Aldrich</td>
      <td>C1988</td>
    </tr>
    <tr>
      <td>MG132</td>
      <td>MG132</td>
      <td>Cell culture</td>
      <td>10 μM</td>
      <td>Sigma-Aldrich</td>
      <td>M7449</td>
    </tr>
    <tr>
      <td>Epoxomicin</td>
      <td>EPX</td>
      <td>Cell culture</td>
      <td>10 μM</td>
      <td>Gentaur Molecular Products</td>
      <td>607-A2606</td>
    </tr>
    <tr>
      <td>TAK-243</td>
      <td></td>
      <td>Cell culture</td>
      <td>0.5 μM</td>
      <td>ChemScence</td>
      <td>CS-0019384</td>
    </tr>
    <tr>
      <td>Doxycycline hyclate</td>
      <td>DOX</td>
      <td>Cell culture</td>
      <td>500 ng/ml</td>
      <td>Sigma-Aldrich</td>
      <td>D9891</td>
    </tr>
    <tr>
      <td>G418 disulfate salt</td>
      <td>G418</td>
      <td>Cell culture</td>
      <td>0.5–1 mg/ml</td>
      <td>Sigma-Aldrich</td>
      <td>A1720</td>
    </tr>
    <tr>
      <td>PH-797804, p38 inhibitor</td>
      <td>p38i</td>
      <td>Cell culture</td>
      <td>1 μM</td>
      <td>Selleckchem</td>
      <td>S2726</td>
    </tr>
    <tr>
      <td>JNK Inhibitor II, JNK inhibitor</td>
      <td>JNKi</td>
      <td>Cell culture</td>
      <td>20 μM</td>
      <td>Sigma-Aldrich</td>
      <td>420119</td>
    </tr>
    <tr>
      <td>PF-3644022, MK2 inhibitor</td>
      <td>MK2i</td>
      <td>Cell culture</td>
      <td>10 μM</td>
      <td>Sigma-Aldrich</td>
      <td>PZ0188</td>
    </tr>
    <tr>
      <td>U0126, MEKi inhibitor</td>
      <td>ERKi</td>
      <td>Cell culture</td>
      <td>250 nM</td>
      <td>Cell Signaling Technology</td>
      <td>9903</td>
    </tr>
    <tr>
      <td>Okadaic Acid</td>
      <td>OA</td>
      <td>Cell culture</td>
      <td>1 μM</td>
      <td>Cell Signaling Technology</td>
      <td>5934</td>
    </tr>
    <tr>
      <td>Calyculin A</td>
      <td>CalycA</td>
      <td>Cell culture</td>
      <td>50 nM</td>
      <td>Cell Signaling Technology</td>
      <td>9902</td>
    </tr>
    <tr>
      <td>Etoposide</td>
      <td></td>
      <td>Cell culture</td>
      <td>5 μM</td>
      <td>Sigma-Aldrich</td>
      <td>E1383</td>
    </tr>
    <tr>
      <td>Brefeldin A</td>
      <td></td>
      <td>Cell culture</td>
      <td>10 ug/ml</td>
      <td>Sigma-Aldrich</td>
      <td>B7651</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 antibodies.


<table>
  <thead>
    <tr>
      <th>Target</th>
      <th>Application</th>
      <th>Dilution</th>
      <th>Conjugate</th>
      <th>Manufacturer</th>
      <th>Catalogue number</th>
      <th>Name</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TTP</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>71632</td>
      <td>D1I3T</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>Myc Tag</td>
      <td>Western blot</td>
      <td>1:5000</td>
      <td></td>
      <td>Sigma-Aldrich</td>
      <td>05–724</td>
      <td>4A6</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>HA tag</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>3724</td>
      <td>C29F4</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>HECTH9</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>5695</td>
      <td>AX8D1</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>Lasu1/Ureb1</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Bethyl</td>
      <td>A300-486A</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>Vinculin</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Sigma-Aldrich</td>
      <td>V9131</td>
      <td>V9131</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>phospho-p38 MAPK, Thr180/Tyr182</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>9211</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>p38 MAPK</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>9212</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>phospho-SAPK/JNK, Thr183/Tyr185</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>9251</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>SAPK/JNK</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>9252</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>phospho-p44/42 MAPK (Erk1/2), Thr202/Tyr204</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>9101</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>p44/42 MAPK (Erk1/2)</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>4695</td>
      <td>137F5</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>p-MK2 (Thr334)</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>3007</td>
      <td>27B7</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>MK2</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>3042</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>p-p53, Ser15</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>9284</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>p-p53</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>2524</td>
      <td>1C12</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>ZFP36L1/2</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Proteintech</td>
      <td>12306–1-AP</td>
      <td>12306–1-AP</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>Ubiquitin</td>
      <td>Western blot</td>
      <td>1:1000</td>
      <td></td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-8017</td>
      <td>P4D1</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>HRP-β-actin</td>
      <td>Western blot</td>
      <td>1:20000</td>
      <td>HRP</td>
      <td>Abcam</td>
      <td>ab49900</td>
      <td>AC-15</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>HRP anti-rabbit IgG</td>
      <td>Western blot</td>
      <td>1:3500</td>
      <td>HRP</td>
      <td>Cell Signaling Technology</td>
      <td>7074</td>
      <td></td>
      <td>Secondary</td>
    </tr>
    <tr>
      <td>HRP anti-mouse IgG</td>
      <td>Western blot</td>
      <td>1:3500</td>
      <td>HRP</td>
      <td>Cell Signaling Technology</td>
      <td>7076</td>
      <td></td>
      <td>Secondary</td>
    </tr>
    <tr>
      <td>TTP</td>
      <td>FACS</td>
      <td>1:100</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>71632</td>
      <td>D1I3T</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>HECTH9</td>
      <td>FACS</td>
      <td>1:100</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>5695</td>
      <td>AX8D1</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>TNF alpha</td>
      <td>FACS</td>
      <td>1:100</td>
      <td>APC</td>
      <td>eBioscience</td>
      <td>17-7321-82</td>
      <td>MP6-XT22</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>Rat IgG1 kappa Isotype Control</td>
      <td>FACS</td>
      <td>1:500</td>
      <td>APC</td>
      <td>eBioscience</td>
      <td>17-4301-82</td>
      <td>eBRG1</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>APC anti-CD90.1/Thy1.1</td>
      <td>FACS</td>
      <td>1:500</td>
      <td>APC</td>
      <td>BioLegend</td>
      <td>202526</td>
      <td></td>
      <td>Secondary</td>
    </tr>
    <tr>
      <td>Alexa Fluor Plus 594 anti-Mouse IgG</td>
      <td>FACS</td>
      <td>1:500</td>
      <td>Alexa Fluor 594</td>
      <td>Thermo Fisher Scientific</td>
      <td>A-21201</td>
      <td></td>
      <td>Secondary</td>
    </tr>
    <tr>
      <td>Alexa Fluor Plus 680 anti-Rabbit IgG</td>
      <td>FACS</td>
      <td>1:500</td>
      <td>Alexa Fluor 680</td>
      <td>Thermo Fisher Scientific</td>
      <td>A-21076</td>
      <td></td>
      <td>Secondary</td>
    </tr>
    <tr>
      <td>APC anti-F4/80</td>
      <td>FACS</td>
      <td>1:100</td>
      <td>APC</td>
      <td>Thermo Fisher Scientific</td>
      <td>17-4801-82</td>
      <td>BM8</td>
      <td>Secondary</td>
    </tr>
    <tr>
      <td>TruStain FcX mouse Fc Receptor CD16/32</td>
      <td>FACS</td>
      <td>1:100</td>
      <td></td>
      <td>BioLegend</td>
      <td>101319</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>IgG Isotype Control</td>
      <td>IP</td>
      <td>1:300</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>2729</td>
      <td></td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>TTP</td>
      <td>IP</td>
      <td>1:100</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>71632</td>
      <td>D1I3T</td>
      <td>Primary</td>
    </tr>
    <tr>
      <td>HA tag</td>
      <td>IP</td>
      <td>1:100</td>
      <td></td>
      <td>Cell Signaling Technology</td>
      <td>3724</td>
      <td>C29F4</td>
      <td>Primary</td>
    </tr>
  </tbody>
</table>

### Transfections

All transfections were perfomed by mixing DNA and polyethylenimine (PEI, Polysciences, 23966) in a 1:3 ratio (μg DNA/μg PEI) in DMEM (Sigma-Aldrich, D6429) without supplements. Transfection was performed using 500 ng of total DNA. The day before transfection, 2×105 HEK293T cells were seeded in six-well clusters in fully supplemented media. Cells were harvested 48 hr after transfection, washed with ice cold PBS and stored at −80 °C until further processing.

### Western blot

Cells were lysed in Frackelton lysis buffer (10  mM Tris-HCl pH 7.4, 50  mM NaCl, 30  mM Na4P2O7, 50  mM NaF, 2  mM EDTA, 1% Triton X-100, 1  mM DTT, 0.1  mM PMSF, and 1 X protease inhibitor cocktail). Cells were incubated for 5  min on ice and then centrifuged at 18,500 x g for 10  min at 4  °C. The supernatant was transferred to a new tube and protein concentration was determined using Pierce BCA Protein Assay Kit (Thermo Fisher Scientific, 23225). Between 20 and 40 micrograms of protein were mixed with Laemmli sample buffer supplemented with β-mercaptoethanol and boiled for 10 min. Proteins were loaded on SDS polyacrylamide gels. The percentage of the gel was chosen based on the MW of the proteins of interest. Proteins were blotted on a PVDF or on a nitrocellulose membrane at 4  °C for 16  hr at 200 mA and then for 2  hr at 400 mA in Towbin buffer (25 mM Tris-HCl pH 8.3, 192 mM glycine, and 20% ethanol) or in carbonate transfer buffer (3  mM Na2CO3, 10  mM NaHCO3, and 20% ethanol). The membrane was blocked in 5% BSA in PBS-T for 1  hr at room temperature and then incubated with the primary antibody overnight at 4  °C while shaking. The next day, the membrane was washed three times with PBS-T and incubated with HRP-coupled secondary antibody for 1  hr at room temperature and imaged with the ChemiDoc Imaging System from Bio-Rad. Relative protein levels were quantified using Image Lab (BioRad).

### Immunoprecipitation

Cells were lysed in 1  ml of RIPA lysis buffer (50  mM Tris-HCl pH 7.4, 150  mM NaCl, 1% SDS, 0.5% Sodium deoxycholate, 1% Triton X-100) supplemented with 40 mM NEM, 40 mM iodoacetamide, 25 U/ml Benzonase, 0.1  mM PMSF, and 1 X protease inhibitor. Cells were incubated on a rotating wheel at 4 °C for 30 min, and centrifuged at 20,000 x g at 4 °C for 30 min. The supernatant was transferred to a new tube and 50 µl (20% of the lysate used for the IP) were collected as input. A total of 500 µg of lysates were incubated overnight at 4  °C on a rotating wheel with an IgG Isotype control (Cell Signaling Technology, 1:300), anti-HA antibody (Cell Signaling Technology, 1:100), or anti-TTP antibody (Cell Signaling Technology, 1:100). The next day, magnetic beads (Pierce Protein A/G Magnetic Beads, Thermo Fisher Scientific, 88803) were blocked by rotation in 3% BSA in RIPA Buffer for 1 hr at 4 °C. Twenty-five µl of beads were added to 500 micrograms of lysates and rotated for 2 hr at 4 °C. Then, the beads were washed five times with 1  ml of RIPA buffer supplemented with 300 mM NaCl, and proteins were eluted in 2 X disruption buffer (2.1  M Urea, 667  mM β-mercaptoethanol and 1.4% SDS).

### Protein half-life determination

To estimate HA-TTP protein half-life, RAW264.7 Dox-Cas9 cells expressing sgHuwe1 or sgROSA were treated with Dox for 5 days before translational elongation was inhibited using 40 μg/ml of cycloheximide (CHX, Sigma-Aldrich, C1988). At indicated time points, whole cell lysates were prepared, analysed by western blot, quantified, and normalized to ACTIN levels and to time point 0 as indicated. Single exponential decay curves were determined using GraphPad Prism (v9), from which protein half-lives were calculated.

### RNA isolation, cDNA synthesis, and qPCR

Total RNA was extracted from mouse bone-marrow-derived macrophages and RAW264.7 Dox-Cas9 cells harboring non-targeting ROSA or Huwe1-targeting sgRNAs. 0.5×106 cells were lysed using Trizol reagent (Thermo-Fisher Scientific, 5596–018) and total RNA was isolated as recommended, and treated with 0.2 U/μl Turbo DNase (Thermo Fisher Scientific, AM2238). cDNA was prepared using Oligo (dT18) Primer (Thermo Fisher Scientific, S0132) or random hexamer primers (Thermo Fisher Scientific, S0142) and RevertAid Reverse Transcriptase (Thermo-Fisher Scientific, EP0441). Real-time PCR experiments were run on a Mastercycler (Biorad), using SYBR Green (Thermo-Fisher Scientific, S7567). Primers for qPCR are listed in Table 6.

**Table 6.**
 qPCR primers.


<table>
  <thead>
    <tr>
      <th>Target</th>
      <th>Primer</th>
      <th>Sequence (5' to 3')</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Il6</td>
      <td>FWD</td>
      <td>CCAGAAACCGCTATGAAGTTCC</td>
    </tr>
    <tr>
      <td>REV</td>
      <td>TTGTCACCAGCATCAGTCCC</td>
    </tr>
    <tr>
      <td rowspan="2">Zfp36</td>
      <td>FWD</td>
      <td>CTCTGCCATCTACGAGAGCC</td>
    </tr>
    <tr>
      <td>REV</td>
      <td>GATGGAGTCCGAGTTTATGTTCC</td>
    </tr>
    <tr>
      <td rowspan="2">Tnf</td>
      <td>FWD</td>
      <td>GATCGGTCCCCAAAGGGATG</td>
    </tr>
    <tr>
      <td>REV</td>
      <td>CACTTGGTGGTTTGCTACGAC</td>
    </tr>
    <tr>
      <td rowspan="2">pre-Tnf</td>
      <td>FWD</td>
      <td>GGCAAAGAGGAACTGTAAG</td>
    </tr>
    <tr>
      <td>REV</td>
      <td>CCATAGAACTGATGAGAGG</td>
    </tr>
    <tr>
      <td rowspan="2">Gapdh</td>
      <td>FWD</td>
      <td>ATGGTGAAGGTCGGTGTGA</td>
    </tr>
    <tr>
      <td>REV</td>
      <td>TGAAGGGGTCGTTGATGG</td>
    </tr>
  </tbody>
</table>

### Lentivirus production and transduction

Semiconfluent Lenti-X cells were transfected with mixes containing lentiviral transfer plasmids of interest, pCRV1-Gag-Pol (Hatziioannou et al., 2004) and pHCMV-VSV-G (Yee et al., 1994) using polyethylenimine (PEI, Polysciences, 23966) in a ratio of 1:3 (μg DNA/μg PEI) in DMEM without any supplements. Virus containing supernatant was clarified of cellular debris by filtration through a 0.45 μm filter. Virus-like particles were directly used after harvesting or kept at 4 °C for short-term storage. Target cells were infected in the presence of 6 μg/ml of polybrene (Sigma-Aldrich, TR1003G).

### Intracellular staining for flow cytometry

For staining of intracellular proteins, cells were collected and washed twice with PBS and subsequently fixed with 2% PFA for 15 min.at room temperature (RT). After PBS washes, cells were resuspended in ice-cold MeOH for permeabilization. At this point, fixed cells were stored in MeOH at −20 °C for a maximum of 2 days. On the day of the intracellular staining, cells were washed with PBS, and incubated for 10 min.at RT in TruStain FcX mouse Fc Receptor CD16/32 block to inhibit non-specific antibody binding. Cells were then incubated with the primary antibody or left unstained for 1 hr at RT. Following three PBS washes, cells were incubated with the secondary antibody for 15 min at 4 °C. Cells were washed two times and resuspended in FACS buffer for flow cytometric analysis on an LSRFortessa (BD Biosciences) operated by BD FACSDiva software (v8.0). FACS data were analysed in FlowJo (v10.8). Median fluorescence intensities were normalized to the control.

### FACS-based CRISPR–Cas9 screens

The genome-wide Vienna sgRNA library was was lentivirally packaged in semiconfluent Lenti-X cells (Takara) via PEI transfection. Following double harvest, the collected supernatant was cleared of cellular debris by filtration through a 0.45 μm PES filter and stored a+4 °C. The obtained virus was used to transduce RAW264.7 Dox-Cas9 cells at a multiplicity of infection (MOI) of less than 0.2 TU/cell, and 600–1000-fold library representation. The percentage of library-positive cells was determined after 4 days of transduction by immunostaining of the Thy1.1 surface marker, and subsequent flow cytometric analysis. Library-positive cells were selected with G418 (1 mg/ml, Sigma-Aldrich, A1720) and expanded. Genome editing was induced with Dox (500 ng/ml, Sigma-Aldrich, D9891) and Cas9-GFP expression was monitored by FACS. Prior to Cas9 induction with Dox (Day 0), as well as before each FACS sort, an unsorted reference sample was collected. For this, a number of cells corresponding to at least 1000-fold library representation was collected and stored at −80 °C until further processing. After 3 days and 6 days of Cas9 induction, cells were sorted at FACS. Cells were harvested, washed with PBS and stained with Fixable Viability Dye eFluor (1:1,000, eBioscience, 65-0865-14) for 30 min. Subsequently, cells were washed three times with PBS, strained through a 35 µm nylon mesh and sorted in DMEM using the FACSAria II or FACSAria III cell sorters operated by BD FACSDiva software (v8.0). For the sort the following gating strategy was used: debris, doublets, dead (Viability Dye positive), Cas9-negative (GFP), mCherry- and BFP-negative cells were excluded. 5% of cells with the lowest and 1% of cells with the highest mCherry-TTP signal were sorted into PBS; same for the BFP internal control. At least 3×106 (mCherrylow and BFPlow) and 5×105 (mCherryhigh and BFPhigh) cells were collected for each time point. Sorted samples were re-analysed for purity, pelleted and stored at −80 °C until further processing. The gating strategy for flow cytometric cell sorting is shown in Figure 2—source data 5.

### Generation of next-generation sequencing libraries

Next-generation sequencing (NGS) libraries of sorted and unsorted control samples were processed as previously described (de Almeida et al., 2021). Isolated genomic DNA was subjected to two-step PCR. The first PCR allowed the amplification of the integrated sgRNA cassette, the second PCR introduced the Illumina adapters. Purified PCR products size distribution and concentration was measured using a fragment analyzer (Advanced Analytical Technologies). Equimolar ratios of the obtained libraries were pooled and sequenced on a HiSeq 2500 platform (Illumina). Primers used for library amplification are listed in Table 7. In primer sequences, NNNNNN denotes random nucleotides, XXXX denotes sample-specific barcodes.

**Table 7.**
 NGS library primers.


<table>
  <thead>
    <tr>
      <th>PCR 1</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Primer_name</td>
      <td>Direction</td>
      <td>Sequence</td>
      <td>Comments</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNCTCATTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNTCGATTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNCCTATTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNGAACTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNATCCTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNACTCTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNCTTCTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNCAAGTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNTGAGTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNTTCGTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNTAGGTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>sgDeepSeq_rev_XXXX</td>
      <td>Rv</td>
      <td>CTCTTTCCCTACACGACGCTCTTCCGATCTNNNNNNTCTGTTCCAGCATAGCTCTTAAAC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td>Fwd1_hybrid_P7_Nras</td>
      <td>Fwd</td>
      <td>GCATACGAGATAGCTAGCCACC</td>
      <td>Library preparation 1st PCR</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>PCR 2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Primer_name</td>
      <td>Direction</td>
      <td>Sequence</td>
      <td>Comments</td>
    </tr>
    <tr>
      <td>Rev2_p5_sgDeepSeq</td>
      <td>Rv</td>
      <td>AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCT</td>
      <td>Library preparation 2nd PCR</td>
    </tr>
    <tr>
      <td>Fwd2_p7_sgDeepSeq</td>
      <td>Fwd</td>
      <td>CAAGCAGAAGACGGCATACGAGATAGCTAGCCACC</td>
      <td>Library preparation 2nd PCR</td>
    </tr>
  </tbody>
</table>

### Analysis of pooled CRISPR screens

The analysis of the CRISPR–Cas9 screen was carried out as previously described (de Almeida et al., 2021). sgRNAs enriched in day 3 and day 6 sorted samples were calculated against the unsorted population control harvested on the respective day of sorting. In addition, the dropout over time of sgRNAs was calculated by comparing the unsorted populations to the initial day 0 population.

### Quantitative proteomics

To systematically assess protein changes after Huwe1 or Psmb7 knockout, in RAW264.7-Dox-Cas9 cells ROSA-, Huwe1- and Psmb7-KO was induced for 2 days. Cells where incubated with LPS for the indicated times, after which 5×105 cells were washed with PBS, pelleted and snap-frozen and stored at –80 °C. Sample protein concentration was measured using standard Pierce Protein Assay Kit (Thermo Fisher Scientific, 23225), after which 40 µg of protein were processed using the iST PreOmics Sample Preparation kit 8 x (P.O. 00001) according to the manufacturer’s instructions.

Peptides were separated on an Ultimate 3000 RSLC nano-flow chromatography system (Thermo Fisher Scientific), using a pre-column for sample loading (Acclaim PepMap C18, 2 cm ×0.1 mm, 5 μm, Thermo Fisher Scientific), and a C18 analytical column (Acclaim PepMap C18, 50 cm ×0.75 mm, 2 μm, Thermo Fisher Scientific), applying a segmented linear gradient from 2% to 35% and finally 80% solvent B (80% acetonitrile, 0.1% formic acid; solvent A 0.1% formic acid) at a flow rate of 230 nL/min over 120 min. Eluting peptides were analyzed on an Exploris 480 Orbitrap mass spectrometer (Thermo Fisher Scientific), which was coupled to the column with a FAIMS pro ion-source (Thermo Fisher Scientific) using coated emitter tips (PepSep, MSWil). The mass spectrometer was operated in DIA mode with the FAIMS CV set to –45, the survey scans were obtained in a mass range of 400–900 m/z, at a resolution of 120 k at 200 m/z and a normalized AGC target at 300%. 31 MS/MS spectra with variable isolation width between 13 and 24 m/z covering 399.5–899.5 m/z range including 1 m/z windows overlap, were acquired in the HCD cell at 30% collision energy at a normalized AGC target of 1000% and a resolution of 30 k. The max. injection time was set to auto.

Raw data were processed using Spectronaut software (version 15.4.210913.50606, https://biognosys.com/software/spectronaut/) with the DirectDIA workflow. The Uniprot mouse reference proteome (version 2021.03, https://www.uniprot.org), as well as a database of most common contaminants were used. The searches were performed with full trypsin specificity and a maximum of 2 missed cleavages at a protein and peptide spectrum match false discovery rate of 1%. Carbamidomethylation of cysteine residues were set as fixed, oxidation of methionine and N-terminal acetylation as variable modifications. The global normalization and imputation were done in Spectronaut - all other parameters were left at default. Spectronaut output tables were further processed using Cassiopeia_LFQ in R (https://github.com/moritzmadern/Cassiopeia_LFQ; Madern, 2021). Contaminant proteins, protein groups identified only by one peptide and protein groups with less than two quantitative values in one experimental group, were removed for further analysis. Differences between groups were statistically evaluated using the LIMMA package (Ritchie et al., 2015) in Cassiopeia_LFQ at 5% FDR (Benjamini-Hochberg).

To generate A375 AAVS1- and HUWE1-KO cells, inducible Cas9 clones of both cell lines were transduced with an sgRNA construct targeting the respective gene by lentiviral delivery. Cells were antibiotic selected for genomic integration and expanded. A375 samples were further FACS sorted for sgRNA + cells to obtain purity of >99%. Cells were harvested 72 hr after Cas9 induction with Dox at final concentration of 0.2 µg/µl. A total number of 3×106 SW620 or 2.5×106 A375 cells were harvested, washed with PBS, pelleted, snap-frozen, and stored at –70 °C. Protein concentrations were measured using standard BCA assay and normalized to 50 micrograms. The protein samples were prepared with iST preOmics Sample Preparation kit 96 x (P.O. 00027) according to the manufacturer’s protocol.

The nano HPLC system (UltiMate 3000 RSLC nano system, Thermo Fisher Scientific) was coupled to an Orbitrap Eclipse Tribrid mass spectrometer equipped with a FAIMS pro interfaces and a Nanospray Flex ion source (all parts Thermo Fisher Scientific). Peptides were loaded onto a trap column (PepMap Acclaim C18, 5 mm ×300 μm ID, 5 μm particles, 100 Å pore size, Thermo Fisher Scientific) at a flow rate of 25 μl/min. using 0.1% TFA as mobile phase. After 10 minutes, the trap column was switched in line with the analytical column (PepMap Acclaim C18, 500 mm ×75 μm ID, 2 μm, 100 Å, Thermo Fisher Scientific) operated at 30 °C. Peptides were eluted using a flow rate of 230 nl/min, starting with the mobile phases 98% A (0.1% formic acid in water) and 2% B (80% acetonitrile, 0.1% formic acid) and linearly increasing to 35% B over the next 180 minutes. The Eclipse was operated in data-dependent mode, performing a full scan (m/z range 350–1500, resolution 120,000, target value 1E6) at 4 different compensation voltages (CV-45,–55, −65,–75), followed each by MS/MS scans of the most abundant ions for a cycle time of 0.75 sec per CV. MS/MS spectra were acquired using an isolation width of 1.2 m/z, target value of 3E4 and intensity threshold of 5E4, maximum injection time 20ms, HCD with a collision energy of 30, using the Iontrap for detection in the rapid scan mode. Precursor ions selected for fragmentation (include charge state 2–6) were excluded for 60 s. The monoisotopic precursor selection filter and exclude isotopes feature were enabled.

For peptide identification, the RAW-files were loaded into Proteome Discoverer (version 2.5.0.400, Thermo Fisher Scientific). All MS/MS spectra were searched using MSAmanda v2.0.0.16129 (Dorfer et al., 2014). The peptide mass tolerance was set to ±10 ppm, the fragment mass tolerance to ±400 mmu, the maximal number of missed cleavages was set to 2, using tryptic enzymatic specificity without proline restriction. Peptide and protein identification were performed in two steps. For an initial search, the RAW-files were searched against the database human_uniprot_reference_2021-06-30.fasta (20,531 sequences; 11,395,157 residues), supplemented with common contaminants, using the following search parameters: alkylation of cysteine by C6H11NO was set as a fixed modification, oxidation of methionine as variable modification. The result was filtered to 1% FDR on protein level using the Percolator algorithm (Käll et al., 2007) integrated in Proteome Discoverer. A sub-database of proteins identified in this search was generated for further processing. For the second search, the RAW-files were searched against the created sub-database using the same settings as above plus considering additional variable modifications: phosphorylation on serine, threonine and tyrosine, deamidation on asparagine and glutamine, and glutamine to pyro-glutamate conversion at peptide N-terminal glutamine, acetylation on protein N-terminus were set as variable modifications. The localization of the post-translational modification sites within the peptides was performed with the tool ptmRS, based on the tool phosphoRS (Taus et al., 2011). Identifications were filtered again to 1% FDR on protein and PSM level, additionally an Amanda score cut-off of at least 70 was applied. Peptides were subjected to label-free quantification using IMP-apQuant (Doblmann et al., 2019). Proteins were quantified by summing unique and razor peptides and applying intensity-based absolute quantification (iBAQ; Schwanhäusser et al., 2011) with subsequent normalisation based on the MaxLFQ algorithm (Cox et al., 2014). Proteins were filtered to be identified by a minimum of 3 quantified in at least 1 sample. Protein-abundance-normalization was done using sum normalization. Statistical significance of differentially expressed proteins was determined using limma (Smyth, 2004).

# Large-scale phenotypic drug screen identifies neuroprotectants in zebrafish and mouse models of retinitis pigmentosa

## Authors

- Liyun Zhang<sup>1</sup>
- Conan Chen<sup>1</sup>
- Jie Fu<sup>2</sup>
- Brendan Lilley<sup>1</sup>
- Cynthia Berlinicke<sup>1</sup>
- Baranda Hansen<sup>1</sup>
- Ding Ding<sup>3</sup>
- Guohua Wang<sup>1</sup>
- Tao Wang<sup>2</sup>
- Daniel Shou<sup>2</sup>
- Ying Ye<sup>2</sup>
- Timothy Mulligan<sup>1</sup>
- Kevin Emmerich<sup>1</sup>
- Meera T Saxena<sup>1</sup>
- Kelsi R Hall<sup>7</sup>
- Abigail V Sharrock<sup>3</sup>
- Carlene Brandon<sup>8</sup>
- Hyejin Park<sup>9</sup>
- Tae-In Kam<sup>9</sup>
- Valina L Dawson<sup>9</sup> ([ORCID: 0000-0002-2915-3970](https://orcid.org/0000-0002-2915-3970))
- Ted M Dawson<sup>9</sup> ([ORCID: 0000-0002-6459-0893](https://orcid.org/0000-0002-6459-0893))
- Joong Sup Shim<sup>13</sup>
- Justin Hanes<sup>1</sup>
- Hongkai Ji<sup>3</sup>
- Jun O Liu<sup>11</sup> ([ORCID: 0000-0003-3842-9841](https://orcid.org/0000-0003-3842-9841))
- Jiang Qian<sup>1</sup>
- David F Ackerley<sup>7</sup> ([ORCID: 0000-0002-6188-9902](https://orcid.org/0000-0002-6188-9902))
- Baerbel Rohrer<sup>8</sup>
- Donald J Zack<sup>1</sup>
- Jeff S Mumm<sup>1</sup> ([ORCID: 0000-0002-2575-287X](https://orcid.org/0000-0002-2575-287X)) †

### Affiliations

1. Department of Ophthalmology, Wilmer Eye Institute, Johns Hopkins University Baltimore United States
2. The Center for Nanomedicine, Wilmer Eye Institute, Johns Hopkins University Baltimore United States
3. Department of Biostatistics, Johns Hopkins University Baltimore United States
4. School of Chemistry, Xuzhou College of Industrial Technology Xuzhou China
5. College of Light Industry and Food Engineering, Nanjing Forestry University Nanjing China
6. Department of Genetic Medicine, Johns Hopkins University Baltimore United States
7. School of Biological Sciences, Victoria University of Wellington Wellington New Zealand
8. Department of Ophthalmology, Medical University of South Carolina Charleston United States
9. Department of Neurology, Johns Hopkins University Baltimore United States
10. Institute for Cell Engineering, Johns Hopkins University Baltimore United States
11. Department of Pharmacology and Molecular Sciences, Johns Hopkins University Baltimore United States
12. Solomon H. Snyder Department of Neuroscience, Johns Hopkins University Baltimore United States
13. Faculty of Health Sciences, University of Macau, Taipa Macau China
14. Department of Oncology, Johns Hopkins University Baltimore United States
15. Department of Molecular Biology and Genetics, Johns Hopkins University Baltimore United States

† Corresponding author

## Abstract

Retinitis pigmentosa (RP) and associated inherited retinal diseases (IRDs) are caused by rod photoreceptor degeneration, necessitating therapeutics promoting rod photoreceptor survival. To address this, we tested compounds for neuroprotective effects in multiple zebrafish and mouse RP models, reasoning drugs effective across species and/or independent of disease mutation may translate better clinically. We first performed a large-scale phenotypic drug screen for compounds promoting rod cell survival in a larval zebrafish model of inducible RP. We tested 2934 compounds, mostly human-approved drugs, across six concentrations, resulting in 113 compounds being identified as hits. Secondary tests of 42 high-priority hits confirmed eleven lead candidates. Leads were then evaluated in a series of mouse RP models in an effort to identify compounds effective across species and RP models, that is, potential pan-disease therapeutics. Nine of 11 leads exhibited neuroprotective effects in mouse primary photoreceptor cultures, and three promoted photoreceptor survival in mouse rd1 retinal explants. Both shared and complementary mechanisms of action were implicated across leads. Shared target tests implicated parp1-dependent cell death in our zebrafish RP model. Complementation tests revealed enhanced and additive/synergistic neuroprotective effects of paired drug combinations in mouse photoreceptor cultures and zebrafish, respectively. These results highlight the value of cross-species/multi-model phenotypic drug discovery and suggest combinatorial drug therapies may provide enhanced therapeutic benefits for RP patients.

## Introduction

Inherited retinal diseases (IRDs) encompass a group of genetically linked retinopathies characterized by progressive photoreceptor death (Duncan et al., 2018). IRDs lead to irreversible vision loss, for which treatment strategies are limited. Retinitis pigmentosa (RP), the most common IRD with approximately 1.5–2.5 million RP patients a worldwide (Dias et al., 2018; Hartong et al., 2006; Verbakel et al., 2018), is characterized by early onset night blindness, gradual loss of visual field, and eventual loss of central vision (Ferrari et al., 2011; Hamel, 2006). The initial pathological feature of RP is selective rod photoreceptor cell death causing night blindness, which is then followed by loss of cone photoreceptors and eventual full blindness (Léveillard et al., 2014). Mutations in more than 70 genes have been linked to RP (Dias et al., 2018; https://sph.uth.edu/retnet/). How these mutations affect gene function or initiate aberrant photoreceptor cell loss is largely unknown. Given the genetic diversity, pan-disease therapeutics are highly desirable. Accordingly, the purpose of our study was to identify compounds capable of promoting rod cell survival in multiple RP models and across species.

As RP progression is relatively protracted, and even small numbers of surviving rod photoreceptors can preserve cone photoreceptor function (Guadagni et al., 2015; Hartong et al., 2006; Punzo et al., 2012), pharmacological interventions aimed at slowing rod photoreceptor death are sought (Duncan et al., 2018; Wubben et al., 2019). However, currently there are no effective therapies for promoting rod photoreceptor survival. As a means of discovering new pharmacological treatments, target-directed high-throughput screening (HTS) approaches have been highly successful in identifying compounds that bind to and/or modulate disease-implicated molecules. However, many promising leads fail during late-stage animal model testing or clinical trials (Munos, 2009; Sams-Dodd, 2013; Scannell et al., 2012). This trend has renewed interest in phenotypic drug discovery (PDD), a complementary approach where drug effects are evaluated in cells or living disease models (Bickle, 2010; Lee et al., 2012; Swinney, 2013). A number of first-in-class drugs were recently discovered using PDD (Eder et al., 2014; Swinney and Anthony, 2011; Swinney, 2013). To expand opportunity on this front, we developed a PDD platform enabling quantitative HTS (qHTS; Inglese et al., 2006) in zebrafish (Walker et al., 2012; Wang et al., 2015a; White et al., 2016).

Zebrafish offer several distinct advantages as a retinal disease modeling system (Angueyra and Kindt, 2018; Richardson et al., 2017). First, the structure of the zebrafish retina is similar to the other vertebrates (Angueyra and Kindt, 2018; Richardson et al., 2017; Schmitt and Dowling, 1999). In particular, the zebrafish retina is ‘cone rich’ like the human retina. Second, about 70% of human genes have at least one ortholog in zebrafish (Howe et al., 2013). Moreover, all RP-associated genes listed in RetNet (https://sph.uth.edu/retnet/) have conserved zebrafish orthologs. Third, the zebrafish retinal system develops quickly being fairly mature by day five of development (Brockerhoff et al., 1995; Moyano et al., 2013; Schmitt and Dowling, 1999). Fourth, zebrafish are amendable to large-scale chemical screening due to their high fecundity rate, small size, and ease of visualizing and quantifying a variety of phenotypes (Mathias et al., 2012; Zon and Peterson, 2005). To streamline such screens, we developed a high-throughput plate reader-based method for quantifying reporter gene expression in vivo (‘ARQiv’; Walker et al., 2012). Recently, we adapted the ARQiv system to human stem-cell-derived retinal organoids (Vergara et al., 2017) to enable cross-species PDD. To realize full throughput potential, ARQiv was combined with robotics-based automation to create ‘ARQiv-HTS’ (Wang et al., 2015b; White et al., 2016).

Here, to identify neuroprotective compounds promoting rod photoreceptor survival, ARQiv-HTS was used to perform a large-scale chemical screen in a transgenic zebrafish model enabling inducible rod photoreceptor cell death (Walker et al., 2012; White et al., 2017). In these fish, YFP-NTR (a yellow fluorescent protein-nitroreductase bacterial enzyme fusion protein) is selectively expressed in rod photoreceptors. NTR expression enables inducible ablation of rod cells upon exposure to prodrug substrates, such as metronidazole (Mtz), which are thought to cause apoptosis through activated metabolites that cause DNA damage (Curado et al., 2007; White and Mumm, 2013). Close to 3000 largely human-approved drugs were tested across six concentrations (i.e. using qHTS principles, Inglese et al., 2006) in more than 350,000 zebrafish larvae. Statistically, 113 hits were identified as hits and 42 of the top performing compounds advanced through confirmation and orthogonal assays. Eleven compounds passed all secondary tests and moved forward as lead drug candidates. Validation tests in an orthogonal series of mouse RP models followed, reasoning that drugs effective across species and/or independent of disease mutation may translate better clinically. All leads were screened in primary mouse photoreceptor cell cultures and a subset of leads was evaluated in retinal explants from the retinal degeneration 1 (Pde6brd1, hereafter rd1) mutant mouse model of RP. Finally, one of three top-performing leads was tested in retinal degeneration 10 mutant retinas in vivo (Pde6brd10, hereafter rd10).

An analysis of potential mechanisms of action (MOA) suggested both shared and complementary targets/pathways. The role of Poly (ADP-ribose) polymerase (PARP), the most common shared target, was evaluated using chemical inhibition, genetic targeting, and western blot analysis. The results implicated PARP as a key mediator of NTR/Mtz-mediated rod cell ablation, and PARP1 inhibition as a shared MOA for a subset of leads. As PARP-dependent cell death pathways are implicated in the etiology of Parkinson’s disease (Kam et al., 2018), RP (Power et al., 2020), and other neurodegenerative disorders (Fan et al., 2017; Fatokun et al., 2014), NTR/Mtz-mediated cell ablation may serve as an inducible and titratable methodology for modeling neurodegenerative disease. To interrogate complementary MOA, lead compounds were tested in pairs in mouse photoreceptor cell culture assays and in zebrafish. Intriguingly, enhanced survival effects were common in mouse photoreceptor cell cultures, while additive and even synergistic effects were evident in zebrafish for the majority of pairs tested. Taken together, our results suggest drugs providing neuroprotective effects across diverse RP models, between species, and/or through complementary MOA, will provide promising new therapeutic opportunities for IRD/RP patients.

## Results

### Establishing a large-scale reporter-assisted neuroprotectant screen in zebrafish larvae

We initiated our study using a robotics-automated large-scale in vivo screening system to identify compounds that promoted rod photoreceptor survival in a transgenic zebrafish line enabling targeted ablation of rod photoreceptors, Tg(rho:YFP-Eco.NfsB)gmc500, hereafter, rho:YFP-NTR (Walker et al., 2012; White et al., 2017). In this line, a 3.7 kb rhodopsin (rho) promoter fragment (Hamaoka et al., 2002) drives transgene expression exclusively in rod photoreceptor cells (Figure 1A). The transgene is a fusion protein linking a yellow fluorescent protein (YFP) reporter to a nitroreductase prodrug converting enzyme (NTR, encoded by the nfsB gene from Escherichia coli). NTR expression enables pro-drug inducible targeted cell ablation (Curado et al., 2007; Pisharath et al., 2007). Exposing rho:YFP-NTR fish to the prodrug metronidazole (Mtz) leads to the selective death of rod photoreceptors and concomitant loss of YFP (Figure 1A–C), physiologically mimicking the onset of RP (Hamel, 2006). An immunohistological analysis of rod and cone photoreceptor markers was performed on 7 days post-fertilization (dpf) zebrafish retinal sections to test if Mtz-induced ablation was specific to rod cells. In non-ablated controls, rod outer segment labeling was well correlated with YFP expression (Figure 1—figure supplement 1A,B; -Mtz, arrows). In Mtz-treated retinas, rod outer segment labeling and YFP expression were markedly diminished (Figure 1—figure supplement 1A,B; +Mtz). Cone photoreceptor labeling showed no overlap with YFP expression, and cone cell labeling appeared similar in non-ablated and Mtz-treated retinas (Figure 1—figure supplement 1C), suggesting cone cells were not affected by Mtz exposure or by acute rod cell loss.

![Figure 1.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig1-v4.jpg)

**Figure 1.:** (A–C) Prodrug (Metronidazole, Mtz) inducible ablation of rod photoreceptors in rho:YFP-NTR larvae. (A) In vivo confocal images of a rho:YFP-NTR larvae showing transgene expression specificity and whole retinas before and after Mtz-induced ablation of rod photoreceptors; schematic shows proposed neuroprotective effect of screened compounds. (B) Optimization of Mtz treatment regimen for large-scale screen: at five dpf, rho:YFP-NTR larvae were exposed to 10, 5, 2.5, 1.25, or 0.625 mM Mtz and YFP levels assessed daily by fluorescence microplate reader from 5 to 8 dpf (sample size: 56 larvae per group, two experimental repeats). The average YFP signal (±sem) for each Mtz treatment group is plotted as the percentage relative to non-ablated (0 mM Mtz) control signals per day. The 10, 5, and 2.5 mM Mtz-treated groups produced minimal YFP signal intensities (<20%) at 7 dpf (Supplementary file 1a; Figure 1B—source data 1). A 2.5 mM Mtz treatment over two days (5–7 dpf), the minimal Mtz concentration achieving maximal ablation, was therefore chosen for the large-scale primary screen. (C) Time series in vivo confocal images of representative non-ablated (-Mtz control, upper panel) and 2.5 mM Mtz-treated (+Mtz control, lower panel) retinas at 5 dpf (pre-Mtz) and 7 dpf (post-Mtz). By 7 dpf, only a limited number of YFP-positive cells are detectable in the +Mtz retina, mainly concentrated in a ventral band of high rod cell density. (D) Schematic of primary drug screening process: (1) At 0 dpf, large numbers of embryos were collected. (2) At 16 hpf, PTU was added to suppress melanization. (3) At 4 dpf, individual drugs were dispensed and titrated in 96-well plates using robotic liquid handlers; 16 wells per concentration (two columns) and six concentrations per drug. (4) At 5 dpf, the COPAS was used to dispense individual larvae into single wells of the drug titration 96-well plates. (5) After a 4 hr pre-exposure to drugs, larvae were treated with 2.5 mM Mtz to induce rod cell ablation. (6) At 7 dpf, YFP signals were quantified by fluorescence microplate reader assay. (7) Same day data analysis using a custom R code (https://github.com/mummlab/ARQiv2; Ding and Zhang, 2021) was used to plot signal to background ratios, SSMD plot, microplate heat map, and SSMD score table. (8) Drug plates producing SSMD scores of ≥1 were visually inspected using fluorescence stereomicroscopy to exclude autofluorescent and lethal compounds.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig1-figsupp1-v4.jpg)

**Figure 1—figure supplement 1.:** (A–C) Immunohistological analysis of rod and cone photoreceptor markers in seven dpf rho:YFP-NTR larvae retinas treated ± 2.5 mM Mtz from 5 to 7 dpf. Representative whole retina and zoomed images of boxed regions are shown for two rod cells markers (A–B) and a cone cell marker (C) in non-ablated controls (-Mtz) and rod cell ablated retinas (+Mtz). (A) Anti-rhodopsin (α-Rho, 1d1 antibody) labeling of rod outer segments (Rod OS, magenta), YFP-expressing rods (rho:YFP-NTR, green) and/or nuclei (DAPI, blue). Arrows denote co-labeling with α-Rho and YFP. (B) Rod photoreceptor-specific antibody (4C12, uncharacterized antigen) labeling of rod outer segments (Rod OS, magenta), YFP-expressing rods (rho:YFP-NTR, green) and/or nuclei (DAPI, blue). Arrows denote co-labeling with α-Rho and YFP. (C) Anti-arrestin3a (α-Arr3a, zpr-1 antibody) labeling of cone cells (Cones, magenta), YFP-expressing rods (rho:YFP, green) and/or nuclei (DAPI, blue). Scale bars: 50 and 100 µm.

Prior studies suggest NTR/Mtz-mediated ablation occurs by apoptosis (Chang et al., 1993; Doonan et al., 2003; Portera-Cailliau et al., 1994; Zeiss et al., 2004) and loss of rods in RP has also been linked to apoptosis (Chang et al., 1993; Doonan et al., 2003; Portera-Cailliau et al., 1994; Zeiss et al., 2004). Thus, we reasoned rho:YFP-NTR fish could be used to identify compounds that protected rods from apoptosis. To identify neuroprotective compounds with this model (i.e. drugs that sustain YFP expression after Mtz exposure), we used our established plate reader-based ARQiv-HTS assay (Figure 1D; Walker et al., 2012; White et al., 2016).

We first determined optimal conditions for inducing rod cell loss while maintaining larval health in a 96-well plate format. Major aspects of retinal cytogenesis are largely complete by five dpf in zebrafish (Schmitt and Dowling, 1999; Stenkamp, 2011). Reporter expression in rho:YFP-NTR larvae has also stabilized by this time point (Unal Eroglu et al., 2018), consistent with rho expression (Raymond et al., 1995). We therefore chose 5 dpf to initiate Mtz-induced rod cell ablation. We previously determined that rod cell loss reached a nadir at 7 dpf following a 24 hr pulse of 10 mM Mtz at 5 dpf (Walker et al., 2012). We reasoned that a 48 hr Mtz exposure initiating at 5 dpf would maximize the signal window to test for neuroprotective effects. Concluding the experiment by 7 dpf also avoids challenges associated with feeding, as zebrafish can subsist on their yolk sac up to that time point (Hernandez et al., 2018; Jardine and Litvak, 2003). However, 10 mM Mtz treatments extending beyond 24 hr become increasingly toxic (Mathias et al., 2014) and removing Mtz from microtiter plates after a 24 hr pulse could not be easily automated. We therefore sought a 48 hr Mtz treatment regimen sufficient for inducing maximal rod cell loss by 7 dpf that showed no evidence of general toxicity.

Five concentrations of Mtz were tested across a twofold dilution series from 10 mM to 625 μM. YFP reporter signals were quantified daily from 5 to 8 dpf using ARQiv. Changes in YFP levels were calculated as percentages normalized to non-ablated YFP controls. The data showed concentration-dependent reductions in YFP with maximal loss observed at 7 dpf (Figure 1B). Mtz exposures at 0.625, 1.25, 2.5, 5, and 10 mM led to a 55, 79, 87, 87, and 83% decrease in YFP detection, respectively (Supplementary file 1a). Although no lethality was observed for any condition, signs of distress were evident for 10 mM Mtz exposures (i.e. reduced motility). At ≤5 mM Mtz, however, no signs of stress were observed. As 2.5 mM Mtz was the lowest concentration producing maximal loss of YFP detection, and confocal imaging verified YFP loss following a 2-day (5–7 dpf) 2.5 mM Mtz treatment (Figure 1C), this condition was selected as the treatment regimen for the large-scale screen.

Previously established power analysis methods using ablated and non-ablated controls (White et al., 2016) determined that a sample size of nine larvae was sufficient to detect a 50% neuroprotective effect. For ease of dispensing, microtiter plate formatting, and to account for larval dispensing errors, we increased the sample size to 16 larvae per condition for the primary screen. We also reasoned that this would also allow us to detect subtler neuroprotective effects. The strictly standardized mean difference quality control (SSMD QC) score was 1.67, indicating the assay was of sufficient quality to justify a large-scale screening effort (Zhang, 2011).

To establish a positive control, we tested 17 compounds and one compound ‘cocktail’ previously implicated as neuroprotectants in mammalian RP models (Supplementary file 2a). Unfortunately, none sustained YFP expression at the concentrations tested (4 μM to 125 nM). However, none have proven effective in RP patients either, suggesting a lack of conservation of neuroprotective effects across species. Our screen was designed to address this issue by testing for neuroprotective effects of these compounds across species and between different RP models. Fortunately, a compound identified as a retinal cell neuroprotectant by the Zack lab (manuscript in preparation) did show-dose-dependent effects on YFP levels. This compound was therefore used as a positive control (POS) for assay performance throughout the large-scale screen.

### Primary screen

The Johns Hopkins Drug Library (JHDL) was chosen for the large-scale screen. The JHDL is comprised of nearly 3000 compounds, most being human-approved drugs (Shim and Liu, 2014). To minimize false discovery rates, all compounds were tested using qHTS principles (Inglese et al., 2006) – that is, across six concentrations (4 μM - 125 nM) using a twofold dilution series. The screen largely followed published ARQiv-HTS methodologies (Wang et al., 2015b; White et al., 2016), with additional assay-specific details (Figure 1D, steps 1–8). In all, 2934 compounds were screened and more than 350,000 transgenic zebrafish larvae evaluated. Real-time data analysis was performed as previously detailed (White et al., 2016) to generate: (1) a plot of YFP signal levels, (2) a plot of SSMD scores across all tested concentrations, (3) a signal intensity heat map of each plate, and (4) an SSMD score table (Figure 1D, step 7). Compounds producing SSMD scores of ≥one were considered potential hits and flagged for visual inspection to assess fluorescence and general morphology using a stereo fluorescence microscope. This step facilitated elimination of false-positive compounds producing aberrant fluorescence due to larval toxicity (six drugs) or compound autofluorescence (27 drugs; Figure 1C, step 8; Supplementary file 2b). Additionally, this allowed visual confirmation of sustained YFP expression within the retina. At the conclusion of the primary screen, 113 compounds were identified as hits (Supplementary file 2c). Hit compounds were classified according to the highest SSMD score achieved across all concentrations tested, and whether concentration-dependent effects were observed. SSMD scores suggested one drug produced a strong effect (SSMD of 2–3); three had semi-strong effects (1.645–2), 21 showed moderate effects (1.28–1.645), and 88 had fairly moderate effects (1–1.28) (Supplementary file 2c). Forty-two drugs showed concentration-dependent effects, while 71 exhibited discontinuous or singular concentration effects. ‘On label’ mechanism of action (MOA) information available for the 113 hits implicated more than 50 targets/pathways in rod cell neuroprotection (Supplementary file 2d).

### Confirmation test

We next performed a series of confirmatory and orthogonal assays to evaluate a subset of 42 hit compounds prioritized by SSMD score, dose-response profile, and/or implicated MOA (Supplementary file 2c, highlighted compounds). Having extensive MOA data is a key advantage of testing human-approved compounds which we leveraged in a previous large-scale zebrafish PDD screen (Wang et al., 2015b). Similarly here, as studies have suggested inflammation plays a key role in retinal degeneration and regeneration (Hollyfield et al., 2008; Mitchell et al., 2018; White et al., 2017; Yoshida et al., 2013), hits implicated as modulators of inflammatory signaling were included as part of the prioritization scheme. In addition, several compounds that did not produce concentration-dependent effects were selected to test whether this criterion was useful in predicting reproducibility. All compounds were obtained from new sources to ensure reagent authenticity. To confirm survival promoting effects, three repeats of the primary screening assay (Figure 2A) were conducted, but using a wider concentration range to account for differences in reagent quality (from 100 μM to 1.28 nM, fivefold dilution series). If toxicity was observed at higher concentrations, dilution series were initiated at 10 µM or 1 µM. Using this strategy, 11 of the 42 prioritized hit compounds were confirmed as lead candidates (26%). Estimated effects on rod cell survival – that is, YFP signal levels relative to +Mtz/0.1% DMSO controls – ranged from 38 to 9% (Figure 2B; lead drug candidate names, abbreviations, PubChem CID, and chemical structures are provided in Table 1).

![Figure 2.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig2-v4.jpg)

**Figure 2.:** (A) Diagram of confirmation assay protocol (see Figure 1D for further details). (B) Box plots of rod cell survival effects of eleven confirmed lead compounds (arrayed by level of neuroprotection) and the positive control compound (POS). YFP signal intensities were normalized to the signal window defined by setting ablated controls (+Mtz) at 0% and non-ablated controls (-Mtz) at 100% to account for: (1) individual variation in reporter expression between fish and, (2) fluctuations in signal window across assays, thus allowing data from identical conditions to be pooled across experimental repeats. Survival effects (normalized YFP %), 95% confidence intervals, p-values, and sample sizes (N) for each condition are shown in the table below. Student’s t-test was used to calculate p-values for each condition relative non-ablated controls (0 mM Mtz). Bonferroni correction for multiple comparisons resulted in an adjusted significance level of 0.004 (α=0.004). A minimum of three experimental replicates was performed for each condition (Figure 2—source data 1). No statistical differences in larval survival were observed for lead compounds relative to their respective +Mtz controls, except for DHA (86%) and CHL (87%; Fisher’s exact test, p<0.05). Common names, IUPAC names, abbreviations, PubChem CID, and chemical structures of lead compounds are listed in Table 1. Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone; POS, positive control. Other abbreviations: CI, confidence interval; Mtz, Metronidazole; PTU, N-phenylthiourea.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig2-figsupp1-v4.jpg)

**Figure 2—figure supplement 1.:** (A) Box plots of NTR inhibition activity (relative to NTR alone control, set at 100%) of lead compounds tested at 300 or 50 μM (see B) using an in vitro assay of CB1954 prodrug reduction kinetics. Compounds that resulted in ≤75% NTR activity (red line, WAR, CPO, CAL, and SUL) were considered potential NTR inhibitors. (B) Relative NTR activity levels and standard deviations (SD) for all leads, as well as IC50 values for CB1954 and Mtz reduction kinetics assays for three potential NTR inhibitors (WAR, CPO, and CAL). All kinetic assays were conducted in triplicate with a single purified batch of NfsB_Ec protein (Figure 2—figure supplement 1—source data 1). Lead compound abbreviations: WAR, Warfarin; MIC, Miconazole; CLO, Cloxyquin; CPO, Ciclopirox olamine; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig2-figsupp2-v4.jpg)

**Figure 2—figure supplement 2.:** (A) Diagram of rod cell neogenesis assay protocol. Transgenic rho:YFP-NTR larvae were treated with individual lead compounds from 5 to 7 dpf to test for effects on rod photoreceptor neogenesis; retinoic acid (RA) served as the positive control. YFP signals were quantified by microplate reader assay and normalized to DMSO-treated controls (CTL, set at 100%). (B) Box plots of lead compound and positive control (RA) effects on rod cell neogenesis. Effects on rod cell neogenesis (normalized % YFP), 95% confidence intervals, p values, and sample sizes (N) for each condition are shown in the table below. Student’s t test was used to calculate p values for each condition relative non-ablated controls. Bonferroni correction for multiple comparisons resulted in an adjusted alpha level of 0.004 (α=0.004 adjusted significance level). A minimum of three biological replicates was performed for each condition and data pooled across replicates (Figure 2—figure supplement 2—source data 1). No statistical differences in larval survival were observed for lead compounds relative to their respective +Mtz controls, except for CPO (74%; Fisher’s exact test, p<0.05). Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone. Other abbreviations: CI, confidence interval; Mtz, Metronidazole; PTU, N-phenylthiourea; RA, retinoic acid (positive control).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig2-figsupp3-v4.jpg)

**Figure 2—figure supplement 3.:** (A) Diagram of rod cell regeneration assay protocol. Transgenic rho:YFP-NTR were exposed to 10 mM Mtz from 5 to 6 dpf, then treated with individual lead compounds from 6 to 9 dpf. YFP signals were quantified by microplate reader assay and normalized to +Mtz controls (set at 0%). Data from at least two experimental repeats were pooled. (B) Box plots of lead compounds and positive control (DEX) effects on rod cell regeneration. Regenerative effects (normalized % YFP), 95% confidence intervals, p values, and sample sizes (N) for each condition are shown in the table below. Student’s t-test was used to calculate p values for each condition relative +Mtz ablated controls. Bonferroni correction for multiple comparisons resulted in an adjusted alpha level of 0.004 (α=0.004 adjusted significance level). A minimum of three biological replicates was performed for each condition (Figure 2—figure supplement 3—source data 1). No statistical differences in larval survival were observed for lead compounds relative to their respective +Mtz controls, except for CIC (76%), DHA (72%), CHL (56%) and COR (48%; Fisher’s exact test, p<0.05). Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone. Other abbreviations: CI, confidence interval; DEX, dexamethasone (positive control); Mtz, Metronidazole; PTU, N-phenylthiourea.

**Table 1.**
 Eleven confirmed lead compounds.Common names, IUPAC names, abbreviations, PubChem CID, and chemical structures of confirmed lead compounds listed in order of efficacy.


<table>
  <thead>
    <tr>
      <th>Common and IUPAC names</th>
      <th>Abbr.</th>
      <th>PubChem CID</th>
      <th>Structure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Warfarin 4-hydroxy-3-(3-oxo-1-phenylbutyl)chromen-2-one</td>
      <td>WAR</td>
      <td>54678486</td>
      <td></td>
    </tr>
    <tr>
      <td>Cloxyquin 5-Chloro-8-hydroxyquinoline</td>
      <td>CLO</td>
      <td>2817</td>
      <td></td>
    </tr>
    <tr>
      <td>Ciclopirox olamine 2-aminoethanol;6-cyclohexyl-1-hydroxy-4-methylpyridin-2-one</td>
      <td>CPO</td>
      <td>38911</td>
      <td></td>
    </tr>
    <tr>
      <td>Miconazole 1-[2-(2,4-dichlorophenyl)−2-[(2,4-dichlorophenyl)methoxy]ethyl]imidazole</td>
      <td>MIC</td>
      <td>4189</td>
      <td></td>
    </tr>
    <tr>
      <td>Zinc pyrithione zinc;1-oxidopyridin-1-ium-2-thiolate</td>
      <td>ZPT</td>
      <td>26041</td>
      <td></td>
    </tr>
    <tr>
      <td>Dihydroartemisinin (4S,5R,9R,10S,12R,13R)−1,5,9-trimethyl-11,14,15,16-tetraoxatetracyclo[10.3.1.04,13.08,13]hexadecan-10-ol</td>
      <td>DHA</td>
      <td>456410</td>
      <td></td>
    </tr>
    <tr>
      <td>Chloroxine 5,7-dichloroquinolin-8-ol</td>
      <td>CHL</td>
      <td>2722</td>
      <td></td>
    </tr>
    <tr>
      <td>Calcimycin 5-(methylamino)−2-[[(2S,3R,5R,8S,9S)−3,5,9-trimethyl-2-[1-oxo-1-(1H-pyrrol-2-yl)propan-2-yl]−1,7-dioxaspiro[5.5]undecan-8-yl]methyl]−1,3-benzoxazole-4-carboxylic acid</td>
      <td>CAL</td>
      <td>40486</td>
      <td></td>
    </tr>
    <tr>
      <td>Sulindac 2-[(3Z)−6-fluoro-2-methyl-3-[(4-methylsulfinylphenyl)methylidene]inden-1-yl]acetic acid</td>
      <td>SUL</td>
      <td>1548887</td>
      <td></td>
    </tr>
    <tr>
      <td>Artemesinin (1R,4S,5R,8S,9R,12S,13R)−1,5,9-trimethyl-11,14,15,16-tetraoxatetracyclo[10.3.1.04,13.08,13]hexadecan-10-one</td>
      <td>ART</td>
      <td>68827</td>
      <td></td>
    </tr>
    <tr>
      <td>Cortexolone (8R,9S,10R,13S,14S,17R)−17-hydroxy-17-(2-hydroxyacetyl)−10,13-dimethyl-2,6,7,8,9,11,12,14,15,16-decahydro-1H-cyclopenta[a]phenanthren-3-one</td>
      <td>COR</td>
      <td>440707</td>
      <td></td>
    </tr>
  </tbody>
</table>

We next asked whether there was a correlation between SSMD scores and/or concentration-dependent effects and confirmation rates. Among 19 selected hit compounds with higher SSMD scores (≥1.3), seven (37%) were confirmed; among 23 with lower SSMD scores (1–1.28), four (17%) were confirmed. Of 27 selected hit compounds with a concentration-dependent trend, eight (30%) were confirmed. Conversely, of 15 compounds that did not show a concentration-dependent trend, 3 (20%) were confirmed. Among the 11 confirmed leads, 8 (73%) showed dose-dependent effects and 7 (64%) had higher SSMD scores (>1.28). These results suggest that prioritizing hit compounds by both relative SSMD scores and dose-dependent trends provides predictive value for confirming activity, consistent with qHTS principles (Inglese et al., 2006).

### Zebrafish model validation I: NTR inhibition

As rod cell death is induced by NTR-mediated reduction of the prodrug Mtz in our model, it is possible that some lead compounds simply suppressed NTR enzymatic activity. To test this, NTR activity was evaluated in the presence of each lead compound by assaying the reduction kinetics of the prodrug CB1954 in vitro (Prosser et al., 2010). To ensure any potential for NTR inhibition was accounted for, all compounds were tested at 300 μM (except MIC and CHL which precipitated at higher concentrations and were tested at 50 µM) that is, ~100-fold greater than neuroprotective concentrations. Compounds were deemed potential inhibitors if NTR activity was less than 75% of the NTR alone control. Seven compounds showed no evidence of NTR inhibition by this criterion, but four did: warfarin (WAR), ciclopirox olamine (CPO), calcimycin (CAL), and sulindac (SUL; Figure 2—figure supplement 1A,B). However, IC50 measures ranged from 150 µM (for CPO) to 350 µM (for SUL, Figure 2—figure supplement 1B), approximately one to two orders of magnitude higher than observed neuroprotective concentrations (i.e. 0.4–20 µM). When NTR reduction of Mtz was tested for WAR, CPO, and CAL at 300 μM, similarly weak inhibitory effects were observed (Figure 2—figure supplement 1B). The differences in concentrations between neuroprotective and NTR inhibitory activities diminish the likelihood that these leads act directly on NTR. To test this further, lead compounds were assayed for neuroprotective effects in NTR-independent mouse RP models (see below).

### Zebrafish model validation II: rod photoreceptor development

To control for the possibility that lead candidates promoted rod photoreceptor development, rather than neuroprotection, YFP levels were quantified in rho:YFP-NTR larvae exposed solely to lead drugs from 5 to 7 dpf (Figure 2—figure supplement 2A). Retinoic acid (RA, 1.25 μM) was used as a positive control as it promotes rod fates during development in zebrafish (Hyatt et al., 1996). RA-treated fish displayed statistically significant increases in YFP levels compared to untreated controls (Figure 2—figure supplement 2B). In contrast, none of the retinas treated with lead compounds exhibited increased YFP expression, suggesting they do not promote rod photoreceptor cell fate. In fact, three lead compounds cloxyquin (CLO), cortexolone (COR) and CPO reduced YFP signals relative to the untreated control (Figure 2—figure supplement 2B, asterisks), suggesting negative effects on rod cell development.

### Zebrafish model validation III: Regeneration

It is well known that the zebrafish retina regenerates (Gorsuch and Hyde, 2014; Lenkowski and Raymond, 2014; Wan and Goldman, 2016). Therefore, to determine whether lead compounds acted by stimulating regeneration, we used a previously described ARQiv assay designed to detect changes in rod cell replacement kinetics (Walker et al., 2012; White et al., 2017). Briefly, rho:YFP-NTR larvae were first treated with 10 mM Mtz at 5 dpf for 24 hr to induce rod cell loss. At 6 dpf, Mtz was washed out and larvae were treated with lead compounds at concentrations corresponding to maximal neuroprotective effects and YFP levels quantified at 9 dpf (Figure 2—figure supplement 3A). Dexamethasone, which accelerates rod cell regeneration kinetics (White et al., 2017), was used as a positive control. The results showed that none of the compounds increased rod cell regeneration rates (Figure 2—figure supplement 3B), while four compounds, dihydroartemisinin (DHA), CLO, CPO and MIC inhibited regeneration. These data suggest that lead compounds do not increase YFP levels by promoting rod cell regeneration.

### Zebrafish model validation IV: Confocal intravital microscopy

To test if lead compounds simply increased YFP signal intensity, rather than promoted rod cell survival, intravital microscopy was used to image Mtz-treated retinas ±lead compounds and non-ablated (-Mtz) controls. Mtz-treated retinas had reduced numbers of YFP-NTR-expressing rods (Figure 3, +Mtz). Conversely, rods in control retinas displayed robust YFP signal throughout the retina and elongated morphologies suggestive of healthy outer segments (Figure 3, -Mtz). In retinas exposed to Mtz and lead compounds, YFP signal loss was attenuated and rods typically displayed elongated morphologies (Figure 3). However, for some compounds, cells appeared rounded, suggesting degeneration was not fully inhibited (e.g. miconazole, MIC; Figure 3). To confirm lead compounds increased rod cell survival, confocal stacks of YFP-expressing rods were 3D-rendered and fluorescence volume quantified using Imaris software-based automated image analysis (White et al., 2017). The data showed a statistically significant increase in YFP volumes for all drug-treated groups (Figure 3—figure supplement 1), confirming that lead compounds promoted increased rod cell numbers and/or preserved outer segment morphology.

![Figure 3.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig3-v4.jpg)

**Figure 3.:** Representative 7 dpf in vivo confocal images of YFP-expressing rod cells in an ablated control (+Mtz), non-ablated control (-Mtz), and in Mtz-exposed retinas treated with lead compounds from 5 to 7 dpf. Whole retina 3D image stacks (~150 micron depth) show loss or preservation of YFP-expressing rod cells throughout the retina, zoomed images of a more limited stack in the dorsal-nasal quadrant (~12 micron depth) provide rod cell morphological detail. Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone; POS, positive control. Other abbreviations: CI, confidence interval; Mtz, Metronidazole; PTU, N-phenylthiourea.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig3-figsupp1-v4.jpg)

**Figure 3—figure supplement 1.:** Box plots of lead compound effects on YFP volumes per image stack across conditions. All conditions resulted in a statistically significant increase in YFP volume relative to Mtz-ablated controls. Lead compound effects on YFP volume (normalized % relative to controls), 95% confidence intervals, adjusted p-values, and sample sizes (N) for each condition are shown in the table below (Figure 3―figure supplement 1—source data 1). Adjusted p values were calculated by performing Mann-Whitney U tests followed by false discovery rate (FDR) correction for multiple comparisons (significance level, α=0.05). Lead compound abbreviations: WAR, Warfarin; MIC, Miconazole; CLO, Cloxyquin; CPO, Ciclopirox olamine; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; Other abbreviations: CI, confidence interval; Mtz, Metronidazole.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig3-figsupp2-v4.jpg)

**Figure 3—figure supplement 2.:** (A) Representative 7 dpf in vivo confocal images of YFP-expressing rod cells in an ablated control (+Mtz), non-ablated control (-Mtz), and in Mtz-exposed rho: YFP-NTR2.0 retinas treated with lead compounds from 5 to 7 dpf. Confocal image stacks from the dorsal-nasal quadrant (~12 micron depth) provide rod cell outer segment morphological detail. (B) Box plots of lead compound effects on rod cell volumes (total YFP volume divided by the number of cells per image stack) across conditions. Conditions resulting in a statistically significant increase in average rod cell volume relative to Mtz-ablated controls are marked with an asterisk. The table below shows average effects on YFP volume per cell (normalized % relative to controls), 95% confidence intervals, adjusted p-values, and sample sizes (N) for each condition (Figure 3―figure supplement 2—source data 1). Adjusted p values were calculated by performing Mann-Whitney U tests followed by false discovery rate (FDR) correction for multiple comparisons. Lead compound abbreviations: ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; WAR, Warfarin; CPO, Ciclopirox olamine; CLO, Cloxyquin; MIC, Miconazole; CHL, Chloroxine; Other abbreviations: CI, confidence interval; Mtz, Metronidazole.

To further investigate if lead compounds preserved rod outer segments, we used a newly developed zebrafish transgenic line, Tg(rho:GAP-YFP-2A-nfsB_Vv F70A/F108Y)jh405 (hereafter rho:YFP-NTR2.0). In this line, rods co-express membrane-tagged YFP and an improved NTR (‘NTR 2.0’). The membrane-tagged YFP facilitates improved imaging of rod outer segments, while NTR 2.0 enables cell ablation at a reduced concentration of Mtz (e.g. 10 µM versus 2.5 mM; Sharrock et al., 2020). To assess if lead compounds preserved outer segment morphologies, intravital confocal imaging was performed as above but using the rho:YFP-NTR2.0 line and 10 µM Mtz treatments. Qualitative image analysis suggested the majority, six of seven tested lead compounds, preserved rod outer segments (Figure 3—figure supplement 2A). Reasoning that preservation of outer segments would equate to increased rod cell size, relative to rounded morphologies of dead or stressed cells, average rod cell sizes were calculated as the total YFP volume divided by the number of rod cells per each 3D confocal stack (i.e. average YFP volume per cell). Compared to rod ablated controls, five of seven lead compounds tested promoted statistically significant increases in rod cell volumes (Figure 3—figure supplement 2B). These data suggest some lead compounds were able to maintain rod outer segment morphology, thus potentially maintaining rod cell function.

### Mouse model validation I: primary photoreceptor cells treated with stressor compounds

To identify new therapeutics for RP patients, we reasoned compounds producing neuroprotective effects across fish and mammalian RP models would likely target conserved mechanisms, and thus be more likely to translate successfully in the clinic. We therefore tested the efficacy of lead compounds in a series of mouse models of retinal photoreceptor degeneration.

First, we tested compounds for the capacity to protect mouse primary photoreceptor cells from stressor-induced cell death in culture. Photoreceptors were isolated from postnatal day four (P4) QRX mice, a transgenic line in which GFP expression is restricted to photoreceptors (Wang et al., 2004), and grown as previously described (Fuller et al., 2014). To induce photoreceptor cell death, thapsigargin (0.25 µM) or tunicamycin (0.6 µg/mL) were added. These ‘stressor’ compounds deplete endoplasmic reticulum (ER) calcium levels (Thastrup et al., 1990) and inhibit protein glycosylation (Fliesler et al., 1984), respectively (Lai et al., 2007b). In turn, they elicit an unfolded protein response (UPR) (Wang et al., 2015b) and related ER stress (Oslowski and Urano, 2011; Zhang et al., 2014), both implicated in the etiology of RP (Griciuc et al., 2011; Rana et al., 2014). To test for survival effects, all eleven lead compounds were screened at seven concentrations across a threefold dilution series (from 30 µM to 40 nM). After 48 hr in stressor ± lead compounds, cells were imaged using an automated high-content screening system. Photoreceptor survival was assessed by automated quantification of GFP-expressing cells (Figure 4A). Nine of 11 lead compounds, proved protective in the thapsigargin-induced cell death assay (Figure 4B). MIC, CLO and SUL also protected photoreceptors from tunicamycin-induced cell death (Figure 4—figure supplement 1). Thus, nine of 11 lead compounds promoted the survival of mouse primary photoreceptor cells in at least one stressor-induced cell death assay, and three were neuroprotective in both assays.

![Figure 4.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig4-v4.jpg)

**Figure 4.:** (A) Primary photoreceptor survival assay protocol. (B) Box plots of photoreceptor survival effects of lead compounds and the positive control compound (POS). Statistically significant survival effects are marked with an asterisk. Survival effects, adjusted p-values, and sample sizes (N) for each condition are shown in the table below. Adjusted p-values were calculated by performing Mann-Whitney U tests followed by false discovery rate (FDR) correction for multiple comparisons. Each assay consisted of six biological replicates per condition and a minimum of two experimental repeats was performed across all conditions (Figure 4—source data 1). (C) Representative images from each condition. Lead compound abbreviations: as in prior figures. Others: EthD, Ethidium homodimer; GFP, green fluorescent protein.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig4-figsupp1-v4.jpg)

**Figure 4—figure supplement 1.:** A) Diagram of primary photoreceptor survival assay protocol. Primary retinal cells were isolated from QRX mice and cultured for 2 days in tunicamycin (an ER stressor that induces cell death) and lead compounds or DMSO (control). After 48 hr, cells were stained with Hoescht and ethidium homodimer followed by high-content imaging and automated cell counting to assess the survival effects of lead compounds on GFP-expressing photoreceptor cells. Cell counts for each condition were normalized to the DMSO controls on the same plate. (B) Box plots of photoreceptor survival effects of lead compounds and the positive control compound. Conditions resulting in statistically significant survival effects are marked with an asterisk. The table below shows survival effects (normalized % GFP-expressing cells), adjusted p values, and total sample sizes (N) for each condition. Each assay consisted of six biological replicates per condition and a minimum of two experimental repeats was performed across all conditions (Figure 4—figure supplement 1—source data 1). Adjusted p values were calculated by performing Mann-Whitney U tests followed by false discovery rate (FDR) correction for multiple comparisons. Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone. Other abbreviations: CI, confidence interval; DMSO, dimethylsulfoxide; POS (positive control).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig4-figsupp2-v4.jpg)

**Figure 4—figure supplement 2.:** (A–B) Lead compounds were tested individually and in pairs for survival effects in primary photoreceptor cells isolated from QRX mice as per Figure 4. Box plots and summary tables (below plots) show relative survival effects in thapsigargin-treated (A) and tunicamycin-treated (B) cultures across all conditions. (C–D) Tables summarize survival effects of individual compounds (outlined boxes on diagonal) and paired compounds for thapsigargin-treated (C) and tunicamycin-treated (D) cultures, trend toward enhanced survival effects are indicated by bolded numbers, gray boxes (median effects). Mann-Whitney U tests followed by Bonferroni correction for multiple comparison (α=0.0006 adjusted significance level) showed that enhanced effects of paired conditions were not statistically significant relative to individual compound controls. (Figure 4—figure supplement 2—source data 1). Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone. Other abbreviations: DMSO, dimethylsulfoxide; POS (positive control).

### Mouse validation II: rd1 mutant retinal explants

We next tested lead compounds for survival effects in rd1 mouse retinal explant cultures. The rd1 mouse model of RP exhibits early onset rod cell degeneration caused by a mutation in the Pde6b gene (Danciger et al., 1990; Pittler and Baehr, 1991; Sidman and Green, 1965), which is an ortholog of the human RP-associated PDE6B (Khramtsov et al., 1993; McLaughlin et al., 1993). In rd1 mice, photoreceptor degeneration begins around P10 and progresses rapidly. By P21, only a single row of photoreceptor cells remain in the outer nuclear layer (ONL; Tansley, 1951) making it an excellent system for screening potential neuroprotectants (Beeson et al., 2016). Here, retinal explants from P10 rd1 mice were isolated and cultured ex vivo (Bandyopadhyay and Rohrer, 2010). Eight lead compounds, all but CAL, SUL, and Zinc pyrithione (ZPT), were tested for survival effects at three concentrations across a fivefold dilution series centered on the concentration most effective in fish RP models. After 11 days in culture, explants were fixed, stained and the number of photoreceptor rows counted (Figure 5A). Neuroprotective effects were defined as a concentration-dependent increase in the number of photoreceptor rows remaining in the ONL relative to untreated controls (p≤0.05). An average of 1.2 ±0.19 rows of photoreceptors remained in the ONL of control explants. Three lead drugs, CPO, DHA, and ART, increased the number of surviving photoreceptor layers (Figure 5B). Representative images of control (DMSO and POS) and lead-treated explants demonstrate photoreceptor layer protection (Figure 5C). CPO, DHA, and ART thus promoted rod cell survival in the fish RP model and two mouse cell culture RP models. However, high concentration CPO treatments (15 µM) led to disruption of retinal histology due to induction of proliferation in the inner nuclear layer (INL) and ONL. Therefore, as DHA is the active metabolite of ART-related compounds, we proceeded with testing DHA in an in vivo mouse RP model.

![Figure 5.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig5-v4.jpg)

**Figure 5.:** (A) Diagram of rd1 explant photoreceptor survival assay protocol. Retinal explants were isolated at postnatal day 10 (P10) and cultured for eleven days in lead compounds at three different concentrations or DMSO. The number of surviving photoreceptor rows was then quantified. (B) Maximally effective dosage of ciclopirox olamine (CPO), artemisinin (ART), and dihydroartemisinin (DHA). Repeated measures ANOVA followed by Bonferroni/Dunn posthoc correction was used to assess statistical significance. (C) Represented images of retinal explants under conditions listed. INL, inner nuclear layer; ONL, outer nuclear layer; RGC, retinal ganglion cell layer; RPE, retinal pigment epithelium.

### Mouse validation III: rd10 mutant model of RP

To test the potential of DHA as a ‘pan-disease’ therapeutic, that is, whether it was effective across multiple genetic RP models, it was tested for photoreceptor survival effects in the rd10 mouse model of RP (Pde6brd10). The rd10 line was selected for in vivo experiments due to its slower rate of photoreceptor degeneration relative to other rd mutants, thus allowing a prolonged window for pharmacological intervention. DHA was selected based on its superior performance in rd1 retinal explant assays (Figure 5) and because it is the active metabolite of a second lead drug candidate, ART, recently shown to protect photoreceptors from light damage (Lu and Xie, 2019). To create a long-release formulation, DHA was encapsulated in PLGA polymers (Poly(D,L-lactide-co-glycolide)). Release kinetics assays in PBS/0.1% DMSO in vitro suggested DHA would reach maximal concentrations after 30 days, and remain stable for at least 20 days thereafter (Figure 6A). We noted that release was minimal in the absence of DMSO, but were reluctant to include DMSO for injections due to the potential for deleterious effects on the retina (Tsai et al., 2009). PLGA-DHA was injected into the vitreous of one eye of rd10 mice at P14, with the contralateral eye serving as a vehicle injection control. At P32, 18 days after injection, and when DHA levels were predicted to reach 80% of maximal concentration based on in vitro releases kinetics, rd10 mouse eyes were processed for immunohistochemistry (Figure 6B) and ONL thickness quantified (Figure 6C). Despite initial promising results in pilot assays, no reproducible neuroprotective effects were observed. It is possible that in the absence of DMSO release kinetics may have been limiting in vivo. We plan to address this possibility in future studies.

![Figure 6.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig6-v4.jpg)

**Figure 6.:** (A) In vitro release kinetics of a long-release DHA formulation (DHA encapsulated in PLGA polymer microparticles, PLGA-DHA) in phosphate buffered saline containing 0.1% DMSO (pH 7.4) at 37°C (Figure 6—source data 1). (B) Representative images of DAPI-stained retinal sections from one female and one male rd10 retina injected with vehicle control (CTL) or PLGA-DHA (DHA; scale bar = 25 µm). (C) Quantification of ONL thickness of control and PLGA-DHA-treated retinas, no statistically significant differences were observed (p=0.5898, two-way ANOVA). The total sample size was 17 mice across three experimental replicates. Abbreviations: CTL, control; DHA, Dihydroartemisinin; ONL: outer nuclear layer; INL: inner nuclear layer; GCL: ganglion cell layer.

### Molecular mechanism of action

Previously, we used ‘on label’ information to explore MOA of hit compounds identified during an in vivo phenotypic screen of the JHDL (Wang et al., 2015b). Recently, we have become interested in additional advantages afforded by HTS-based MOA data and whole-organism phenotypic screening, such as polypharmacology (Dar et al., 2012; Rennekamp and Peterson, 2015; Rihel et al., 2010). Accordingly, we applied a target-agnostic MOA analysis process by evaluating lead compound performance in HTS and ultra-HTS studies archived on PubChem (https://pubchem.ncbi.nlm.nih.gov/). Many lead compounds exhibited shared target/pathway activities, suggesting in-common MOA (Table 2). Among shared targets, Tyrosyl-DNA Phosphodiesterase 1 (TDP1), a DNA repair enzyme, was the most popular (eight leads). To test whether TDP1 inhibition promoted rod photoreceptor survival, we tested three TDP1 inhibitors in rod:YFP-NTR fish: paromomycin (PM), thiostrepton (ThS), and methyl-3,4-dephostatin (MD) (Huang et al., 2011; Liao et al., 2006). Both PM and ThS showed neuroprotective effects (Table 3, Figure 7).

![Figure 7.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig7-v4.jpg)

**Figure 7.:** Box plots of rod cell survival effects of eight PARP inhibitors (green), a necroptosis inhibitor (blue), four apoptosis inhibitors (magenta), and three Tdp1 inhibitors (orange) in Mtz-treated rho:YFP-NTR zebrafish larvae (targets are listed above for each category). Assays performed as per confirmation tests (see Figure 2A) with all inhibitors tested across 10 concentrations using a twofold dilution series (see Methods for highest concentration tested per compound). Conditions resulting in a statistically significant increase in survival effects relative to +Mtz controls are marked with an asterisk. Survival effects (normalized YFP %), 95% confidence intervals, p-values, and sample sizes (N) for each condition are shown in the table below. Student’s t-test was used to calculate p-values for each condition relative non-ablated controls (0 mM Mtz). Bonferroni correction for multiple comparisons resulted in an adjusted significance level of 0.003 (α=0.003). A minimum of two experimental repeats was performed for each condition (Figure 7—source data 1). No statistical differences in larval survival were observed for tested compounds relative to their respective +Mtz controls, except for PM (67%; Fisher’s exact test, p<0.05). Target abbreviations: Parp, Poly (ADP)-ribose polymerase; Ripk1, Receptor-interacting serine/threonine-protein kinase (1); Tdp1, Tyrosyl-DNA phosphodiesterase 1; Mtz, metronidazole. Inhibitor abbreviations: AG, AG-14361; NMS, NMS-P118; BMN, talazoparib; ABT, veliparib; OLA, olaparib; MK, niraparib; RUC, rucaparib; NEC, necrostatin-1; AC, Ac-DEVD-CHO; CASI, caspase3/7 inhibitor I; CASVII, caspase three inhibitor VII; PM, paromomycin; ThS, thiostrepton; MD, methyl-3,4-dephostatin. Other abbreviations: CI, confidence interval; Mtz, Metronidazole.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig7-figsupp1-v4.jpg)

**Figure 7—figure supplement 1.:** Box plots of rod cell survival effects of BMN (PARP inhibitor) and NEC (necroptosis inhibitor) tested alone and in pairs at three different concentrations in rho:YFP-NTR zebrafish larvae (assays performed as per confirmation tests, see Figure 2A). Seven of nine pairs promoted a statistically significant increase in survival relative to both individual compound controls (++), while one pair performed better than a single compound control (+). Survival effects (normalized YFP %), 95% confidence intervals, p-values, and sample sizes (N) for each condition are shown in the table below. For comparison, the survival effect of each pair (Effect %) and the summed effect of the respective individual compound controls (Sum %) are provided. Additive effects were defined as any pair that promoted survival at equal to or greater than the sum of the corresponding individual compound effects ±10%. By this criterion, eight pairs produced additive effects (bolded). A minimum of two experimental repeats were performed for each condition and data polled across replicates (Figure 7—figure supplement 1—source data 1). See also Supplementary file 1b for Student’s t-test calculated p-values for paired conditions relative to ablated controls (+Mtz) and to respective individual compound controls. Inhibitor abbreviations: BMN, talazoparib; NEC, necrostatin-1. Other abbreviations: CI, confidence interval; Mtz, Metronidazole; NA, not applicable.

**Table 2.**
 Summary of PubChem HTS and uHTS target-based screens of lead compound bioactivity.Results of 13 target-based HTS screens, with '+' indicating inhibitory activity of lead compounds. Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone; POS, positive control. Other abbreviations: CI, confidence interval; Mtz, Metronidazole; PTU, N-phenylthiourea. Target abbreviations: Tdp1, Tyrosyl-DNA phosphodiesterase 1; Rorc, RAR-related orphan receptor gamma; AR, androgen receptor signaling pathway; TR, thyroid receptor signaling pathway; VDR, vitamin D receptor; ER, estrogen receptor alpha; AhR, aryl hydrocarbon receptor; GR, glucocorticoid receptor; Dopa, dopamine related; HIF1, Hypoxia-inducible factor 1-alpha; SHH, Sonic hedgehog; COX, cyclooxygenase.


<table>
  <thead>
    <tr>
      <th>Drug\path</th>
      <th>Tdp1</th>
      <th>Rorc</th>
      <th>AR</th>
      <th>TR</th>
      <th>VDR</th>
      <th>ER</th>
      <th>AhR</th>
      <th>GR</th>
      <th>P53</th>
      <th>Dopa</th>
      <th>HIF1</th>
      <th>SHH</th>
      <th>COX</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WAR</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>MIC</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CLO</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CPO</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ZPT</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>DHA</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CHL</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CAL</td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
    </tr>
    <tr>
      <td>SUL</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
    </tr>
    <tr>
      <td>ART</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>COR</td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Chemical inhibitors of lead implicated targets and cell death pathways.List of eight PARP inhibitors, one necroptosis inhibitor, three apoptosis inhibitors, and three TDP1 inhibitors tested for neuroprotective effects in rho:YFP-NTR larvae (see Figure 4 and Figure 4—source data 1). Target(s) and relative inhibitory activity against related targets in each cell death pathway are as reported by manufacturer, references provided by manufacturer, or references herein. Concentrations producing maximal survival effects and the percent increase in YFP levels are listed for each compound. Abbreviations: Parp (Poly (ADP)-ribose Polymerase), Ripk1 (Receptor-interacting serine/threonine-protein kinase 1), Tdp1 (Tyrosyl-DNA phosphodiesterase 1).


<table>
  <thead>
    <tr>
      <th>Cell death Pathway</th>
      <th>Compound name (abbrv.)</th>
      <th>Target(s) and Relative Activity (+)</th>
      <th>Conc. [µM]</th>
      <th>Effect (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">Parp-dependent (Parthantos or cGMP-dependent)</td>
      <td>AG-14361 (AG)</td>
      <td>Parp1+++</td>
      <td>64</td>
      <td>9</td>
    </tr>
    <tr>
      <td>NMS-P118 (NMS)</td>
      <td>Parp1++</td>
      <td>8</td>
      <td>16</td>
    </tr>
    <tr>
      <td>Talazoparib (BMN)</td>
      <td>Parp1 ++++</td>
      <td>0.5</td>
      <td>14</td>
    </tr>
    <tr>
      <td>Veliparib (ABT)</td>
      <td>Parp1+++, 2+++</td>
      <td>64</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Olaparib (Ola)</td>
      <td>Parp1+++, 2++++</td>
      <td>32</td>
      <td>9</td>
    </tr>
    <tr>
      <td>E7449</td>
      <td>Parp1++++, 2++++</td>
      <td>1</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Niraparib (MK)</td>
      <td>Parp1+++, 2+++</td>
      <td>32</td>
      <td>11</td>
    </tr>
    <tr>
      <td>Rucaparib (RUC)</td>
      <td>pan-Parp++++</td>
      <td>32</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Necroptosis</td>
      <td>Necrostatin-1 (NEC)</td>
      <td>Rip1k++</td>
      <td>64</td>
      <td>17</td>
    </tr>
    <tr>
      <td rowspan="3">Apoptosis</td>
      <td>Ac-DEVD-CHO (AC)</td>
      <td>Caspase 1+++, 2+, 3++++, 4++, 5++, 6+++, 7+++, 8++++, 9++, 10+++</td>
      <td>0.5</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Caspase3/7 inhibitor I (CASI)</td>
      <td>Caspase 3++, 7++, 9+</td>
      <td>0.5</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Caspase three inhibitor VII (CASVII)</td>
      <td>Caspase 3+++</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <td rowspan="3">Tdp1 (DNA repair)</td>
      <td>Paromomycin (PM)</td>
      <td>Tdp1+</td>
      <td>20</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Thiostrepton (ThS)</td>
      <td>Tdp1+</td>
      <td>100</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Methyl-3,4-dephostatin (MD)</td>
      <td>Tdp1++</td>
      <td>0.16</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

This result was surprising given that NTR reduction of Mtz is thought to cause DNA damage-induced cell death (Curado et al., 2007). Thus, inhibition of a DNA repair enzyme would be expected to enhance, not inhibit, NTR/Mtz-mediated cell death. However, an alternative means of disrupting TDP1 activity is by inhibiting Poly (ADP-ribose) Polymerases (PARPs). Indeed, in a comprehensive 400,000 compound qHTS assay designed to identify TDP1 inhibitors, all five hits turned out to be PARP inhibitors (Murai et al., 2014). PARPs also mediate DNA repair but, interestingly, hyperactivation of PARP1 leads to a specific form of DNA damage-induced cell death, termed parthanatos (Fatokun et al., 2014; Wang et al., 2016). PARP is also involved in a cGMP-dependent cell death pathway implicated in RP (Power et al., 2020).

We therefore assayed PARP inhibitors for the capacity to promote rod cell survival in rod:YFP-NTR fish. All eight PARP inhibitors tested had neuroprotective activity, ranging from 9% to 20% (Figure 7). To account for other cell death mechanisms implicated in neurodegeneration, we tested an inhibitor of necroptosis (necrostatin-1; NEC), and three inhibitors of apoptosis (Ac-DEVD-CHO, CASI, and CASVII, Table 3). Surprisingly, NEC promoted rod cell survival, while the apoptosis inhibitors did not (Figure 7, Table 3). Interestingly, paired testing of PARP and necroptosis inhibitors resulted in additive effects (Figure 7—figure supplement 1, Supplementary file 1b), suggesting either differential responses to NTR/Mtz-induced DNA damage among rod cells, or that inhibiting both pathways keeps cells from activating the other mechanism of cell death when only one pathway is blocked.

To further dissect cell death pathways mediating NTR/Mtz-induced rod cell ablation, we used a ‘redundant’ CRISPR/Cas9 gene targeting approach (i.e. four guide RNA targeting), which enables phenotyping in injected zebrafish embryos/larvae (Wu et al., 2018). Key factors for apoptosis (casp3a and casp3b), PARP-dependent cell death pathways parthanatos and/or cGMP-dependent cell death (parp1), and necroptosis (ripk1l) were targeted. In addition, tdp1 was targeted as a DNA repair control. For each targeted gene, four gRNAs and Cas9 protein were co-injected into one-cell stage embryos. Injected and uninjected (control) larvae were treated ±2.5 mM Mtz at five dpf and rod-YFP levels quantified at six dpf by ARQiv. For Mtz-ablated larvae, knockdown of parp1 markedly increased rod cell survival (39% compared to 20% in the uninjected control, p=4E-12), and ripk1l knockdown modestly protected rods (26% compared to 22% in the uninjected control, p=0.05). However, no improvement in survival was observed for either casp3a/b or tdp1 knockdown (Figure 8A). In no Mtz controls, knockdown of parp1, ripk1l or tdp1 had no effect on rod cell numbers. Conversely, casp3a/3b double knockdown increased rod cell numbers (Figure 8B) suggesting inhibition of developmental apoptosis and confirming efficacy of casp3a/3b knockdown. Confocal imaging confirmed parp1 knockdown effects on rod cell survival and casp3a/3b knockdown effects on rod cell development (Figure 8—figure supplement 1A). Reduced gene expression was verified by qPCR (Figure 8—figure supplement 1B, Supplementary file 3). These results are consistent with the NTR/Mtz system eliciting DNA damage-associated cell death mediated by parp1, that is, parthanatos, in rod cells.

![Figure 8.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig8-v4.jpg)

**Figure 8.:** (A) Box plots of rod cell survival effects of CRISPR/Cas9-based knockdown of key cell death pathway genes: parp1 (parthanatos), ripk1l (necroptosis), casp3a and casp3b (apoptosis), as well as tdp1 (as a DNA repair pathway control) in Mtz-treated rho:YFP-NTR zebrafish larvae. Cas9 protein and four gRNAs (for parp1, ripk1l and tdp1) or eight gRNAs (for casp3a with casp3b) were co-injected at the one-cell stage. Larvae were raised to 5 dpf and treated with Mtz (2.5 mM) to induce rod cell death. Rod cell survival was quantified at 6 dpf by fluorescence microplate reader assay. Conditions resulting in a statistically significant increase in survival effects relative to non-injected controls are marked with an asterisk. Sample sizes (N), survival effects (YFP % relative to non-ablated control) and p-values are provided in the table below. A minimum of three experimental repeats was performed and data pooled across replicates (Figure 8—source data 1). (B) Box plots of effects on rod cell development in non-ablated rho:YFP-NTR zebrafish larvae (-Mtz) following knockdown of the same genes as in (A). Rod cell numbers were estimated at 6 dpf by microplate reader-based quantification of YFP. Only casp3a/3b knockdown resulted in a statistically significant increase (22%) in rod cell numbers during development. Sample sizes (N), normalized survival effects (% relative to non-injected control) and p-values are provided in the table below. A minimum of three experimental repeats was performed and data pooled across replicates. Abbreviations: parp1, poly (ADP-ribose) polymerase 1; ripk1l, receptor (TNFRSF)-interacting serine-threonine kinase 1, like; casp3a: caspase 3, apoptosis-related cysteine peptidase a; casp3b: caspase 3, apoptosis-related cysteine peptidase b; tdp1, tyrosyl-DNA phosphodiesterase 1; CTL, control; KD, knockdown; PAR, Poly (ADP-ribose).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig8-figsupp1-v4.jpg)

**Figure 8—figure supplement 1.:** (A) Representative intravital whole retina confocal image stacks of gene knockdown effects on YFP-expressing rod cell numbers in Mtz-treated fish (+Mtz, i.e. effects on NTR/Mtz-mediated cell death) and non-ablated controls (-Mtz, i.e. developmental effects) zebrafish at 6 dpf. (B) Quantification of CRISPR-based gene knockdown, 16–24 larvae (7 dpf) per condition were pooled as one sample for RNA extraction. qPCR results confirmed suppression of gene expression for each target (ranging from 22% to 50% of control). Data from 3 to 4 experimental repeats were pooled (Figure 8—figure supplement 1—source data 1). (C) Western blot of PAR accumulation in rho:YFP-NTR zebrafish larvae following 2.5 mM Mtz treatment at five dpf. Protein samples were collected from approximately 30 fish at 3, 6, 12, 24, and 48 hr post-Mtz treatment (hpt). PAR polymer detection with an anti-PAR antibody suggest increases in accumulation in Mtz-treated larvae at 24 and 48 hpt. (D) Quantification of PAR polymer bands showed a statistically significant increase at 24 hpt (p = 0.04, Student’s t test; Figure 8—figure supplement 1—source data 1). Abbreviations: parp1, poly (ADP-ribose) polymerase 1; ripk1l, receptor (TNFRSF)-interacting serine-threonine kinase 1, like; casp3a: caspase 3, apoptosis-related cysteine peptidase a; casp3b: caspase 3, apoptosis-related cysteine peptidase b; tdp1, tyrosyl-DNA phosphodiesterase 1; CTL, control; KD, knockdown; PAR, Poly (ADP-ribose).

To further test for activation of PARP signaling during NTR/Mtz-induced rod cell death, accumulation of polymerized poly (ADP-ribose) (PAR), a downstream effector of PARP1 activation (Kam et al., 2018), was analyzed by western blot. five dpf rho:YFP-NTR larvae were treated ±2.5 mM Mtz and protein samples collected from ~30 fish at 3, 6, 12, 24, and 48 hr post-Mtz treatment initiation. Western blots showed clear accumulation of PAR in Mtz-treated fish at 24 and 48 hr post-Mtz (Figure 8—figure supplement 1C) which was verified quantitatively (Figure 8—figure supplement 1D). Collectively, results of cell death pathway analyses are concordant across chemical inhibition, genetic knockdown, and biochemical assays, strongly suggesting NTR/Mtz-induced cell ablation is mediated by PARP-dependent cell death (e.g. parthanatos, cGMP-dependent cell death), a target/pathway implicated across multiple mammalian models of RP (Arango-Gonzalez et al., 2014).

To determine if lead compound effects were mediated by inhibition of PARP signaling, parp1 expression was knocked down prior to testing for effects on rod cell survival in rho:YFP-NTR larvae. Four leads predicted to be PARP inhibitors (MIC, CLO, CPO, DHA), one predicted to be a non-PARP inhibitor (WAR), and a known PARP inhibitor control (BMN) were tested. Two lead compounds, MIC and DHA and BMN (the PARP inhibitor control) produced no statistically significant enhanced neuroprotective effects over parp1 knockdown. Conversely, WAR, CLO and CPO increased rod cell survival in parp1 knockdown fish (Figure 9A). qPCR confirmed mRNA knockdown (Figure 9B) and controls showed no effects of parp1 knockdown on rod cell development (Figure 9C, -Mtz) and enhanced rod cell survival upon Mtz treatment (Figure 9C, +Mtz). These data confirm that PARP inhibition mediates the neuroprotective effects of some lead compounds (e.g. MIC and DHA) while others are PARP-independent. The latter result suggests lead compounds may act via complementary neuroprotective mechanisms. Combined, these findings are consistent with rod cell loss in our fish RP model occurring, at least partially, by PARP-dependent cell death.

![Figure 9.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig9-v4.jpg)

**Figure 9.:** (A) Box plots of rod cell survival effects of five lead compounds and a PARP inhibitor control (BMN) in Mtz-treated rho:YFP-NTR zebrafish larvae in which parp1 expression was knocked down, assays performed as per confirmation tests (see Figure 2A). Larvae subjected to CRISPR-based knockdown of parp1 were raised to 5 dpf, exposed to lead compounds at the indicated concentrations, and treated with 2.5 mM Mtz to induce rod cell death. Rod cell survival was quantified at six dpf by fluorescence microplate reader assay. Conditions that promoted a statistically significant increase in rod cell survival are marked with an asterisk. Survival effects (normalized YFP %), 95% confidence intervals, p-values, and sample sizes (N) for each condition are shown in the table below. Student’s t-test was used to calculate p-values for each condition relative to ablated controls (+Mtz). Bonferroni correction for multiple comparisons resulted in an adjusted significance level of 0.006 (α=0.006). A minimum of three experimental repeats were performed for each condition and data polled across replicates (Figure 9—source data 1). (B) Quantification of CRISPR-based parp1 knockdown, 16–24 larvae per condition (seven dpf) were pooled as one sample for RNA extraction. qPCR results confirmed suppression of parp1 expression (ranging from 14% to 23% of uninjected controls). (C) Box plots of parp1 knockdown effects on rod cell neogenesis and rod cell survival, that is, -Mtz and +Mtz controls, respectively, for these experiments. Sample sizes (N), survival effects (normalized YFP %) and p-values are shown in the table below. Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; DHA, Dihydroartemisinin; Other abbreviations: BMN, talazoparib (parp1-dependent control);, CI, confidence interval; Mtz, Metronidazole; parp, poly (ADP-ribose) polymerase 1.

### Combinatorial assay

PubChem data also suggested potential complementary MOA, that is, multiple independent targets across lead compounds (Table 2). We therefore hypothesized that combining lead compounds may produce enhanced, additive, or even synergistic effects. To investigate this, combinatorial lead drug treatments were tested in primary mouse photoreceptor cell cultures. As above, photoreceptors were isolated from QRX mouse retinas and used in stressor-treated primary cell culture assays. All 11 lead compounds were tested at a selected concentration individually and in pairs and the survival of GFP-labeled photoreceptors analyzed by high-content imaging and automated cell counting. The results showed no wholly additive effects, that is, survival percentages equaling or excelling the summed effect of individual compound assays. However, enhanced effects – i.e., better median survival than for either compound alone – were observed for 30 of 55 pairs in thapsigargin-treated cultures and for 20 of 55 pairs in tunicamycin-treated cultures (Figure 4—figure supplement 2). Finally, seven lead compounds were tested alone and in pairs in rho:YFP-NTR zebrafish using optimal effective concentrations. Pairs producing survival effects equal to or greater than the sum of their individual values (±10%) were considered additive. By this criterion, 10 of 19 viable pairs (two pairs proved lethal) exhibited additive effects (Figure 10, bolded; Supplementary file 1c) and three pairs produced supra-additive effects (i.e. ≥25% greater than summed effects) suggesting possible synergy (Figure 10, asterisks). The maximal average rod cell survival effect was 58% (WAR + CPO). Several compounds showed broadly additive effects, for example, WAR was additive with all six drugs and COR with four of five pairs (one pair proving lethal). Additive effects suggest multiple signaling pathways are involved in NTR/Mtz-induced photoreceptor degeneration, thus that combinatorial drug regimens may be required to achieve maximal therapeutic benefits for RP patients.

![Figure 10.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig10-v4.jpg)

**Figure 10.:** Box plots of rod cell survival effects of seven lead compounds tested alone and in pairs in rho:YFP-NTR zebrafish larvae (assays performed as per confirmation tests, see Figure 2A). To test for enhanced survival, all compounds were tested at maximal effective dosages. Eleven pairs promoted a statistically significant increase in survival relative to both individual compound controls (++), while five pairs performed better than a single compound control (+). Survival effects (normalized YFP %), 95% confidence intervals, p-values, and sample sizes (N) for each condition are shown in the table below. For comparison, the survival effect of each pair (Effect %) and the summed effect of the respective individual compound controls (Sum %) are provided. Additive effects were defined as any pair that promoted survival at equal to or greater than the sum of the corresponding individual compound effects ±10%. By this criterion, 10 pairs produced additive effects (bolded values). Three pairs produced effects greater than 25% above the summed effect and were considered potentially synergistic (asterisks). A minimum of three experimental repeats were performed for each condition and data pooled across replicates (Figure 10—source data 1). No statistical differences in larval survival were observed for lead compounds or compound pairs relative to their respective +Mtz controls, except for DHA (73%), WAR+DHA (73%), CIC+DHA (89%), ZPT+DHA (91%), ZPT+COR (90%) and CAL+COR (79%; Fisher’s exact test, p<0.05). Two pairs, DHA+CAL and DHA+COR resulted in total lethality and are not plotted. See Supplementary file 1c for survival effects (normalized YFP %), 95% confidence intervals and p-values relative to ablated controls (+Mtz) and to respective individual compound controls, and sample sizes (N) for all conditions. Lead compound abbreviations: WAR, Warfarin; CLO, Cloxyquin; CPO, Ciclopirox olamine; MIC, Miconazole; ZPT, Zinc pyrithione; DHA, Dihydroartemisinin; CHL, Chloroxine; CAL, Calcimycin; SUL, Sulindac; ART, Artemisinin; COR, Cortexolone; POS, positive control. Other abbreviations: CI, confidence interval; Mtz, Metronidazole.

## Discussion

Identifying effective neuroprotective therapies for RP and other IRDs stands as a critical unmet need for the field (Duncan et al., 2018; Wubben et al., 2019). Although, neurotrophic factors, anti-apoptotic agents, nutritional supplements, and antioxidants have shown neuroprotective effects in animal models of RP (Dias et al., 2018). Unfortunately, these reagents have produced, at best, only limited benefits for patients to date and, for some, mild improvements are offset by adverse side effects associated with long-term use (Dias et al., 2018). For example, ciliary neurotrophic factor (CNTF) was shown to be effective in protecting photoreceptors in mouse (Cayouette et al., 1998), dog (Tao et al., 2002), and chicken (Fuhrmann et al., 2003) models of retinal degeneration. However, CNTF failed to improve either visual acuity or field sensitivity in short- and long-term RP clinical trials (Birch et al., 2016; Ciliary Neurotrophic Factor Retinitis Pigmentosa Study Groups et al., 2013; Argus II Study Group et al., 2015). Clinical trials of Vitamin A in combination with Vitamin E (Berson et al., 1993), docosahexaenoic acid (Berson et al., 2004), lutein (Berson et al., 2010), or valproic acid (Birch et al., 2018) were reported to produce some benefits for RP patients, but only in subpopulations, and some of these studies have been controversial (Massof and Finkelstein, 1993).

Our strategy for addressing this challenge was to: (1) scale up the number of compounds tested directly in complex living disease models and (2) perform a cross-species screening cascade that starts with small animal models amenable to HTS and proceeds to mammalian models. We hypothesize that compounds producing beneficial outcomes across evolutionarily diverse species will target conserved MOA and thus stand a higher chance of successful translation. As a generalized strategy, large-scale drug discovery screens using small animal models are showing increasing promise across multiple disease paradigms (Cagan et al., 2019; Cully, 2019; Kitcher et al., 2019; MacRae and Peterson, 2015).

Here, using a large-scale in vivo drug screening platform (Figure 1), we tested 2934 largely human-approved compounds for neuroprotective effects across six concentrations in >350,000 larval zebrafish models of RP. The primary screen implicated 113 compounds as neuroprotectants (Supplementary file 2c). Confirmatory repeats and a series of four orthogonal assays validated 11 of 42 prioritized hit compounds in protecting zebrafish rod photoreceptors from cell death (Figures 2 and 3, Figure 2—figure supplements 1–3, Figure 3—figure supplement 1 and Table 1). Importantly, investigations of lead compound MOA, led to the discovery that NTR/Mtz-mediated rod cell death appears to proceed through alternative cell death pathways (Figure 8) recently linked to photoreceptor degeneration in mammalian models of RP (Arango-Gonzalez et al., 2014; Paquet-Durand et al., 2007; Power et al., 2020; Sancho-Pelluz et al., 2008; Tolone et al., 2019). A summary schematic of the entire screening cascade is provided in Figure 11.

![Figure 11.](https://cdn.elifesciences.org/articles/57245/elife-57245-fig11-v4.jpg)

**Figure 11.:** (A) Flow chart of cross-species phenotypic drug discovery process showing results of the primary drug screen, secondary confirmation, orthogonal assays, mouse model tests, shared MOA and complementary MOA assays (i.e. paired drug tests). (B) Summary of survival effects of lead drug candidates across model systems. (C) Summary of survival effects of paired lead drug tests in the zebrafish-inducible RP model showing effects of single drug controls (blue boxes) and paired drug tests that resulted in no additive effects (gray boxes), additive effects (orange boxes) and synergistic effects (red boxes); mathematically summed effect of each pair of lead compounds (italics) are shown for comparison. Abbreviations: as in prior figures.

Confirmatory tests showed survival effects of lead compounds varied from 9 to 38% (Figure 2), which might suggest limited therapeutic potential. However, even small numbers of surviving rod cells can have a significant impact on cone photoreceptor survival (Guadagni et al., 2015; Hartong et al., 2006; Punzo et al., 2012). This effect is mediated by the rod-derived cone viability factor (RdCVF) (Léveillard et al., 2004) which stimulates glucose metabolism to promote cone survival (Aït-Ali et al., 2015). Therefore, as cone cells provide high-acuity daytime vision, protecting small numbers of rod cell has significant therapeutic potential for RP patients. To test this further, lead compounds will need to be tested for the ability to prolong cone survival and function in rod-cone degeneration models.

Visualization by in vivo confocal imaging showed variations in surviving cell morphologies across lead compounds (Figure 3 and Figure 3—figure supplement 2), suggesting.

variations in the extent of rod cell protection that could impact function. In particular, maintenance of the outer segment, a specialized primary cilium in which phototransduction occurs, is necessary for photoreceptor function. Volumetric quantification of surviving rod cells further suggested lead compounds differ in their capacity to maintain outer segments. Visual function tests will need to be performed to test this possibility and thus to prioritize lead compounds for in vivo testing in mammalian RP models.

To test conservation of neuroprotective effects across species, lead compounds were evaluated in three mouse IRD/RP models. Nine of 11 leads were confirmed as neuroprotectants in primary photoreceptor cell cultures (Figure 4). Three of eight leads assayed using rd1 retinal explant cultures were also validated (Figure 5); two being active in both paradigms, DHA and ART. We chose the rd10 RP model for in vivo testing because it undergoes a slower rate of rod cell loss than rd1; spanning from approximately P16 to P35 (Chang et al., 2007; Gargini et al., 2007). DHA was the most promising compound for these tests as it had shown strong effects across assays and was amenable to a long-term release formulation designed to sustain drug action over weeks to months (PLGA-DHA, Figure 6A). In addition, DHA is the active metabolite of artemisinin, another of our cross-species confirmed leads that was shown to have neuroprotective activity in rat models of stress-induced neuronal damage and light-induced photoreceptor degeneration (Yan et al., 2017). Unfortunately, we did not observe increased photoreceptor survival in rd10 retinas injected with PLGA encapsulated DHA. A potential issue that needs to be resolved is the release kinetics of encapsulated DHA in vivo. DHA has poor water solubility, therefore in vitro release kinetics were obtained in the presence of 0.1% DMSO. However, because intravitreal injection of DMSO can have deleterious effects (Tsai et al., 2009) we avoided this potential complication. To assess DHA release in vivo, pharmacokinetic assays such as high-performance liquid chromatography (Ayalasomayajula and Kompella, 2004; Shen et al., 2014) will be used to quantify lead compound concentrations in the retina for future tests. Another possible explanation is that rd1 and rd10 models have differential responses to DHA. This has been reported for the histone-deacetylase inhibitor valproic acid, which shows opposing effects in rd1 (neuroprotective) and rd10 (deleterious) mice (Mitton et al., 2014) and across four different frog models of RP (Vent-Schmidt et al., 2017). In addition valproic acid has produced inconsistent results in clinical trials with RP patients (Chen et al., 2019; Todd and Zelinka, 2017; Totan et al., 2017). These results emphasize the need for a more thorough understanding of IRD and RP disease mechanisms and downstream cell pathways to support the development of both personalized and pan-disease therapeutics.

Numerous IRD/RP-linked mutations have been identified (Dias et al., 2018; https://sph.uth.edu/retnet/) implicating an array of disease mechanisms (Dharmat et al., 2020). However, cell death pathways common across different IRD/RP patient subpopulations may provide pan-disease targets for neuroprotective therapies. Apoptosis has long been thought to be the mechanism by which rod photoreceptors die in IRD/RP (Chang et al., 1993; Doonan et al., 2003; Portera-Cailliau et al., 1994; Zeiss et al., 2004). However, these reports relied on terminal deoxynucleotidyl transferase dUTP nick end labeling (TUNEL), which does not distinguish apoptosis from other types of cell death (Ansari et al., 1993; Charriaut-Marlangue and Ben-Ari, 1995; Grasl-Kraupp et al., 1995; Dmitrieva and Burg, 2007; Kanoh et al., 1999; Nishiyama et al., 1996). More recent evaluations of multiple apoptosis-related markers (e.g. BAX, cytochrome c, caspase-9, cleaved caspase-3) suggest apoptosis occurs in only a minority of RP models (Arango-Gonzalez et al., 2014; Sancho-Pelluz et al., 2008). Moreover, inhibition of apoptosis does not block cell death in many mouse photoreceptor degeneration models (Hamann et al., 2009; Yoshizawa et al., 2002), suggesting other pathways may mediate rod and/or cone cell death in retinal degenerative disease.

Recently, non-apoptotic cell death mechanisms have been implicated in IRD/RP. In a comprehensive biochemical analysis of 10 mammalian RP models—involving mutations in cnga3, cngb1, pde6a, pde6b, pde6c, prph2, rho, and rpe65—non-apoptotic cell death signatures were found to be common across all models tested (Arango-Gonzalez et al., 2014). Conversely, definitive apoptotic markers were found only for the S334ter (rho) rat model. Shared features included activation of poly (ADP-ribose) polymerase (PARP), histone deacetylase (HDAC), and calpain, as well as accumulation of cyclic guanosine monophosphate (cGMP) and poly (ADP-ribose) (PAR). For PARP, chemical inhibitors and a knock out line provided further confirmation (Jiao et al., 2016; Paquet-Durand et al., 2007; Sahaboglu et al., 2017; Sahaboglu et al., 2016; Sahaboglu et al., 2010). Prior reports had suggested the NTR/Mtz system elicits caspase-3 activation and apoptotic cell death (Chen et al., 2011). Initially, we had used this as a rationale for pursuing a neuroprotective screen with the rho:YFP-NTR line- however, the recent reports outlined above suggested apoptosis may have limited relevance to IRD/RP. Interestingly, when we tested cell death processes implicated in photoreceptor degeneration directly, an inhibitor of apoptosis (BEL) did not promote rod cell survival, whereas inhibition of necroptosis (NEC) and PARP were neuroprotective in our fish RP model (Figure 7, Table 3). Serendipitously, an exploration of shared lead compound MOA helped to clarify cell death mechanism(s) mediating NTR/Mtz-induced rod cell ablation.

To explore molecular MOA of our lead compounds, we searched bioactivity data from prior HTS and ultra HTS assays (PubChem). The results suggested both shared and independent MOA. The most common shared target was TDP1 (eight of 11 lead compounds; Table 2). An initial test confirmed two of three TDP1 inhibitors tested, though neuroprotective activity was relatively weak (~10% survival; Figure 7). TDP1 is a DNA repair enzyme that repairs topoisomerase I-induced DNA damage (Dexheimer et al., 2008; El-Khamisy, 2011). Interestingly, a qHTS cell-based screen of 400,000 compounds for inhibitors of human TDP1 found that all five confirmed compounds actually inhibited PARP activity not TDP1 (Murai et al., 2014). This is consistent with findings showing that TDP1 acts in conjunction with PARP1 (Das et al., 2014; Lebedeva et al., 2015), thus PARP inhibition can indirectly affect TDP1 activity. Combined with the results discussed above, we were motivated to test whether PARP inhibition was protective against NTR/Mtz-induced rod cell death.

All eight PARP inhibitors tested promoted rod cell survival in our fish RP model (Figure 7 and Table 3). CRISPR/Cas9-based knockdown of parp1 resulted in a statistically significant reduction of Mtz-induced rod cell death (Figure 8A). Moreover, PAR polymer, an indicator of PARP activation, accumulated in Mtz-treated fish (Figure 8—figure supplement 1C–D). Collectively, these results suggest PARP activation plays an important role in NTR/Mtz-induced rod cell death. PARP1 overactivation initiates a caspase-independent form of DNA damage-induced cell death, termed parthanatos (Fan et al., 2017). Parthanatos has been strongly implicated in the etiology of Parkinson’s disease (Kam et al., 2018) and in a variety of neurodegenerative conditions as well (Fan et al., 2017; Fatokun et al., 2014), including RP/IRDs (Power et al., 2020). Importantly, PARP is also a key component of the cGMP-dependent cell death pathway which has been linked to photoreceptor degeneration (Iribarne and Masai, 2017; Tolone et al., 2019; Power et al., 2020). Thus, the NTR/Mtz-mediated cell ablation system may provide a novel approach for modeling neurodegenerative diseases associated with PARP-dependent cell death that is both inducible and titratable.

To investigate cell death more broadly, we also explored the roles of necroptosis, apoptosis and tdp1 signaling in the zebrafish-inducible RP model. Interestingly, inhibiting necroptosis but not apoptosis promoted rod cell survival in rho:YFP-NTR fish (Figure 7 and Table 3). Consistent with this, CRISPR/Cas9-based knockdown of ripk1l protected rods, but casp3a/3b knockdown did not (Figure 8). Necroptosis is primarily associated with secondary cone cell death in RP models (Murakami et al., 2015; Murakami et al., 2012; Yang et al., 2017) but has also been implicated in rod cell death in IRBP mutant RP models (Sato et al., 2013) and/or may damage photoreceptors indirectly via necroptotic microglia signaling (Huang et al., 2018). Combined, these results suggest that necroptosis, PARP1-dependent parthanatos, and/or c-GMP-dependent cell death mediate NTR/Mtz-induced rod cell ablation. The potential relevance of these alternative cell death pathways to heritable photoreceptor degeneration may explain the relatively high rate of validation we observed in cross-species tests of lead compounds.

To evaluate whether lead compound effects were mediated by inhibition of PARP signaling, a subset of lead compounds and a PARP inhibitor control (BMN) were analyzed for survival effects in parp1 knockdown fish. Among four leads tested that were implicated as parp1 inhibitors, two (MIC and DHA) were no longer protective when parp1 expression was suppressed (Figure 9), suggesting parp1 inhibition mediated their neuroprotective effects. PARP1 has also been shown to have a role in stem cell reprogramming (Chiou et al., 2013; Doege et al., 2012; Weber et al., 2013). PARP inhibition might therefore block Müller glia dedifferentiation, diverting injury-induced activity from a regenerative to neuroprotective program (Bringmann et al., 2009).

Finally, MOA analyses also implicated additional, potentially complementary, lead targets (Table 2). Compounds acting through independent targets/pathways have the potential to produce additive or even synergistic effects. This possibility was confirmed for 10 of 19 paired lead compounds tested in rho:YFP-NTR fish (Figure 9, Supplementary file 1c). Analogous tests in mouse photoreceptor cell cultures showed a trend toward enhanced survival effects of paired leads but no fully additive effects (Figure 4—figure supplement 2). This discrepancy could be due to cell culture assays lacking in vivo complexity, such as signals requiring intact tissue or interactions between cell types or with other tissues. This result highlights a potential advantage of whole organism phenotypic drug screening: the ability to identify compounds/conditions that would be missed in more simplified assay systems. That combinatorial assays could be performed efficiently and rapidly also exemplifies key advantages the zebrafish system affords phenotypic drug discovery, for example, versatility and low cost.

In summary, we identified 11 lead compounds promoting rod cell survival in an inducible zebrafish RP model using a large-scale in vivo phenotypic drug discovery platform. Nine lead compounds were also effective as neuroprotectants in primary mouse photoreceptor cell cultures and three promoted photoreceptor survival in rd1 mouse retinal explants. MOA studies indicated a subset of lead compounds may protect rod cells by inhibiting PARP-dependent cell death pathways and/or necroptosis. Combinatorial assays in fish showed additive and even synergistic effects, suggesting some lead compounds target independent neuroprotective pathways (summarized in Figure 11). We hypothesize that compounds producing beneficial outcomes across diverse animal disease models likely target highly conserved MOA and may therefore stand an increased likelihood of successfully translating to the clinic. Further, our data suggest polypharmacological targeting of complementary neuroprotective mechanisms has the potential to maximize therapeutic benefits for IRD/RP patients.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Transgenic zebrafish, Danio rerio (AB; roy)</td>
      <td>Tg(rho:YFP-Eco.NfsB)gmc500; mpv17a9 (rho:YFP-NTR)</td>
      <td>RRID # #:ZFIN_ZDB-GENO-190617–10</td>
    </tr>
    <tr>
      <td>Transgenic zebrafish Danio rerio (AB; roy)</td>
      <td>Tg(rho:GAP-YFP-2A-nfsB_Vv F70A/F108Y)jh405; mpv17a9 (rho:YFP-NTR2.0)</td>
      <td>ZFIN ID pending; Mumm lab</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>BL21(DE3) Competent Cells</td>
      <td>emdmillipore.com: 69450</td>
    </tr>
    <tr>
      <td>Mutant mouse Mus musculus</td>
      <td>Pde6brd1 (rd1)</td>
      <td>RRID #:MGI:5902961</td>
    </tr>
    <tr>
      <td>Mutant mouse Mus musculus (C57BL/6J)</td>
      <td>Pde6brd10 (rd10)</td>
      <td>RRID # #:IMSR_JAX:004297</td>
    </tr>
    <tr>
      <td>Transgenic mouse Mus musculus (SJL/J)</td>
      <td>QRX-IRES-EGFP</td>
      <td>Zack lab</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Arrestin3a (α-Arr3a; zpr-1) Mouse monoclonal (1:200 dilution)</td>
      <td>RRID #:AB_10013803</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Rhodopsin (α-Rho; 1d1) Mouse monoclonal - 1:100 dilution</td>
      <td>ZDB-ATB-081229–13</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Ab-4C12 (aka, 4C12) Mouse monoclonal - 1:50: dilution</td>
      <td>ZDB-ATB-090506–2</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Mouse IgG (H+L), Alexa 647 Goat polyclonal - 1:1000 dilution</td>
      <td>RRID #:AB_2338902</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Cone Arrestin (mouse) Rabbit polyclonal - 1:1000 dilution</td>
      <td>RRID #:AB_1163387</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Retinal S antigen (S128) Mouse monoclonal - 1:1000 dilution</td>
      <td>RRID #:AB_2747776</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-PAR (human) Recombinant Antibody - 1:2000 dilution</td>
      <td>PMID:30385548</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Human IgG (Fab')2 (HRP) Goat polyclonal - 1:10000 dilution</td>
      <td>RRID #:AB_1951105</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-beta-Actin-HRP Mouse monoclonal - 1:20000 dilution</td>
      <td>RRID #:AB_262011</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>17-(Allylamino)−17-demethoxygeldanamycin (17-AAG)</td>
      <td>CAS #: 75747-14-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>17β-Estradiol</td>
      <td>CAS #: 50-28-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>3-Hydroxybenzylhydrazine dihydrochloride</td>
      <td>CAS #: 81012-99-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>6,7-Dihydroxyflavone</td>
      <td>CAS #: 38183-04-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Acacetin</td>
      <td>CAS #: 480-44-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Ac-DEVD-CHO (AC)</td>
      <td>CAS #: 169332-60-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>AG-14361</td>
      <td>CAS #: 328543-09-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Alpha-lipoic acid</td>
      <td>CAS #: 1077-28-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Alpha-tochopherol</td>
      <td>CAS #: 10191-41-0</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Aluminum chloride hexahydrate</td>
      <td>CAS #: 7784-13-6</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Artemisinin (ART)</td>
      <td>CAS #: 63968-64-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Ascorbic acid</td>
      <td>CAS #: 50-81-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Calcimycin (CAL)</td>
      <td>CAS #: 52665-69-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Calpastatin peptide</td>
      <td>sigmaaldrich.com: SCP0063</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Calpeptin</td>
      <td>CAS #: 117591-20-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Caspase-3 Inhibitor VII (CASVII)</td>
      <td>CAS #: 745046-84-8</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Caspase-3/7 Inhibitor I (CASI)</td>
      <td>CAS #: 1110670-49-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Chloroxine (CHL)</td>
      <td>CAS #: 773-76-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Ciclopirox olamine (CPO)</td>
      <td>CAS #: 41621-49-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Clonidine</td>
      <td>CAS #: 4205-90-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Clopidogrel sulfate</td>
      <td>CAS #: 120202-66-6</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Cloxyquine (CLO)</td>
      <td>CAS #: 130-16-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Compactin</td>
      <td>CAS #: 73573-88-3</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Cortexolone (COR)</td>
      <td>CAS #: 152-58-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>D-(-)-Norgestrel</td>
      <td>CAS #: 797-63-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Danthron</td>
      <td>CAS #: 117-10-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>DAPI dihydrochloride</td>
      <td>CAS #: 28718-90-3</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Deltaline</td>
      <td>CAS #: 6836-11-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Dexamethasone</td>
      <td>CAS #: 50-02-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Diazepam</td>
      <td>CAS #: 439-14-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Digoxin</td>
      <td>CAS #: 20830-75-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Dihydroartemisinin</td>
      <td>CAS #: 71939-50-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>E7449</td>
      <td>CAS #: 1140964-99-3</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Entinostat</td>
      <td>CAS #: 209783-80-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Escitalopram oxalate</td>
      <td>CAS #: 219861-08-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Eupatorin</td>
      <td>CAS #: 855-96-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Hoechst 33342</td>
      <td>CAS #: 23491-52-3</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Hydroquinone</td>
      <td>CAS #: 123-31-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Indomethacin</td>
      <td>CAS #: 53-86-1</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Isopropamide Iodide</td>
      <td>CAS #: 71-81-8</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Isoxsuprine hydrochloride</td>
      <td>CAS #: 579-56-6</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lactulose</td>
      <td>CAS #: 4618-18-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Leucovorin Calcium</td>
      <td>CAS #: 1492-18-8</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Levobetaxolol</td>
      <td>CAS #: 93221-48-8</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lobeline sulfate</td>
      <td>CAS #: 134-64-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Lovastatin</td>
      <td>CAS #: 75330-75-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Magnesium gluconate</td>
      <td>CAS #: 3632-91-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Menadione</td>
      <td>CAS #: 58-27-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Mercaptamine hydrochloride</td>
      <td>CAS #: 156-57-0</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Methyl-3,4-dephostatin (MD)</td>
      <td>PubChem SID #: 24278575</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Metronidazole (MTZ)</td>
      <td>CAS #: 443-48-1</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Miconazole (MIC)</td>
      <td>CAS #: 22916-47-8</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>MnTBAP</td>
      <td>CAS #: 55266-18-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Myriocin</td>
      <td>CAS #: 35891-70-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Myrrh oil</td>
      <td>UPC #: 640791683602</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>N-Acetyl-L-cysteine (NAC)</td>
      <td>CAS #: 616-91-1</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Nalidixic acid</td>
      <td>CAS #: 389-08-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>NCS-382</td>
      <td>CAS #: 520505-01-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Necrostatin-1 (NET)</td>
      <td>CAS #: 4311-88-0</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Niraparib (MK)</td>
      <td>CAS #: 1038915-60-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>NMS-P118</td>
      <td>CAS #: 1262417-51-5</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>N-tert-Butyl-α-(2-sulfophenyl)nitrone</td>
      <td>CAS #: 73475-11-3</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Olaparib (OLA)</td>
      <td>CAS #: 763113-22-0</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Panobinostat</td>
      <td>CAS #: 404950-80-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Paromomycin (PM)</td>
      <td>CAS #: 1263-89-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>PLGA</td>
      <td>CAS #: 26780-50-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Pseudoephedrine, (1S,2S)-(+)-</td>
      <td>CAS #: 90-82-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Retinoic acid (RA)</td>
      <td>CAS #: 302-79-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Rofecoxib</td>
      <td>CAS #: 162011-90-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Romidepsin</td>
      <td>CAS #: 128517-07-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Rosiglitazone</td>
      <td>CAS #: 122320-73-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Rucaparib (RUC)</td>
      <td>CAS #: 283173-50-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Streptomycin sulfate</td>
      <td>CAS #: 3810-74-0</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Sulindac (SUL)</td>
      <td>CAS #: 38194-50-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Sunitinib</td>
      <td>CAS #: 557795-19-4</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Talazoparib (BMN)</td>
      <td>CAS #: 1207456-01-6</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>thapsigargin</td>
      <td>CAS #: 67526-95-8</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Thiostrepton (ThS)</td>
      <td>CAS #: 1393-48-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>tunicamycin</td>
      <td>CAS #: 11089-65-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Veliparib (ABT)</td>
      <td>CAS #: 912444-00-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Vorinostat</td>
      <td>CAS #: 149647-78-9</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Warfarin (WAR)</td>
      <td>CAS #: 81-81-2</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Xanthurenic acid</td>
      <td>CAS #: 59-00-7</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Zinc pyrithione (ZPT)</td>
      <td>CAS #: 13463-41-7</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Software for large-scale in vivo screen data processing (R v3.3.1, R Studio v0.99.903, and the ARQiv2 package)</td>
      <td>https://github.com/mummlab/ARQiv2</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Thermo Scientific HCS Studio Cell Analysis Software</td>
      <td>Customized for this project</td>
    </tr>
    <tr>
      <td>Database</td>
      <td>CRISPRScan</td>
      <td>https://www.crisprscan.org/</td>
    </tr>
  </tbody>
</table>

### Animal care and use

All animal studies described herein were performed in accordance with both the Association for Research in Vision and Ophthalmology (ARVO) statement on the ‘Use of Animals in Ophthalmic and Vision Research’ and the National Institutes of Health (NIH) Office of Laboratory Animal Welfare (OLAW) policies regarding studies conducted in vertebrate species. Animal protocols were approved by the Animal Care and Use Committees of the Johns Hopkins University School of Medicine (protocol # FI19M489 and #MO20M253) and Medical University of South Carolina (protocol #2018–00399).

### Fish maintenance and husbandry

Zebrafish were maintained using established temperature and light cycle conditions (28.5°C, 14 hr of light/10 hr of dark). A previously generated zebrafish transgenic line, Tg(rho:YFP-Eco.NfsB)gmc500 (hereafter, rho:YFP-NTR) expresses a fusion protein of enhanced yellow fluorescent protein (YFP) and a bacterial nitroreductase (NTR) enzyme (encoded by the E. coli nfsB gene) selectively in rod photoreceptors (Walker et al., 2012). When rho:YFP-NTR fish are exposed to the prodrug metronidazole (Mtz), NTR reduces Mtz to a DNA damage-inducing cytotoxic derivative, resulting in the death of NTR-expressing cells (Chen et al., 2011; Curado et al., 2007). A newly generated transgenic line, Tg(rho:GAP-YFP-2A-nfsB_Vv F70A/F108Y)jh405 (hereafter rho:YFP-NTR2.0) expresses a membrane tagged YFP and an improved version of NTR which enables induction of cell death at much lower concentrations of Mtz (Sharrock et al., 2020). These lines were propagated in a pigmentation mutant with reduced iridophore numbers, roya9 (roy), to facilitate YFP reporter signal detection in vivo. Non-transgenic roy fish were used to define reporter signal cutoff values for fluorescent microplate reader assays. For each large-scale drug screening assays, 6000–12,000 eggs were collected by group breeding ~300 adult rho:YFP-NTR fish (White et al., 2016).

### Immunostaining

rho:YFP-NTR larvae were treated with 2.5 mM Mtz or 0.1% DMSO at 5 dpf for 2 days (10 fish per condition), and collected at 7 dpf for immunostaining using previously reported methods (Unal Eroglu et al., 2018). Briefly, larvae were fixed in 4% PFA at 4°C overnight, infiltrated with 30% sucrose, and embedded in OCT. Cryosections of 10 µm thickness were made for immunofluorescence staining. Each section was blocked with 1x PBS containing 0.5% Triton X-100% and 5% goat serum for one hour followed by primary antibody staining overnight. The next day, each section was washed and stained with the secondary antibody for 2 hr. All slides were mounted and underwent confocal imaging. The primary antibodies used in this study were zpr-1 (anti-Arrestin3a; 1:200 dilution; from ZIRC), 1d1 (anti-Rhodopsin; 1:50; gift from Dr. James M. Fadool) and 4C12 (uncharacterized rod cell antigen, 1:100 dilution; gift from Dr. James M. Fadool). The secondary antibody used was goat anti-mouse Alexa 647 (1:1000; Invitrogen).

### Optimization of Mtz treatment for rod cell ablation - rho:YFP-NTR zebrafish

rho:YFP-NTR larvae were separated into six groups of ~23 larvae per group. Each group was treated with varying Mtz concentrations (10, 5, 2.5, 1.25, 0.625, 0 mM), from 5 to 8 days post-fertilization (dpf). YFP signals were quantified daily by fluorescence microplate reader (TECAN Infinite M1000 PRO; excitation 514 nm, bandwidth 5 nm; emission 538 nm, bandwidth 10 nm) to track changes in rod photoreceptor cell numbers relative to Mtz concentration (Walker et al., 2012; White et al., 2016). Two technical repeats were performed and results aggregated across experiments by normalizing to non-ablated controls.

### Sample size estimation

To calculate sample size (N) and evaluate assay quality, two 96-well plates of larvae were treated with 2.5 mM Mtz/0.1% DMSO (ablated ‘+Mtz’ control) or 0.1% DMSO only (non-ablated ‘-Mtz’ control) from 5 to 7 dpf (196 fish per condition). YFP signals were then quantified at seven dpf (due to the large sample size, a single technical replicate was performed). Power calculations were used to determine sample sizes across a range of error rates and effect sizes (White et al., 2016). This analysis suggested a sample size of nine per condition tested would sufficiently minimize false-discoveries (i.e. type I and type II error rates of 0.05 and 0.05, respectively) and account for drug effects reaching 50% of signal window of the positive (non-ablated) control. However, to account for plating errors and other confounding variables, we chose to increase the sample size to 16.

### Primary drug screening assay - rho:YFP-NTR zebrafish

A schematic of the primary screening process is presented in Figure 1C. For the primary screen, 2934 compounds from John Hopkins Drug Library (JHDL) were screened across six concentrations (4 μM-125 nM using a twofold dilution series). The JHDL consists of ~2200 drugs approved for use in humans (e.g. FDA approved) with the remainder approved for clinical trials (Chong et al., 2006). The ARQiv screening process has been detailed previously (White et al., 2016) and was adapted here for large-scale quantification of YFP-expressing rod photoreceptors (Walker et al., 2012; White et al., 2016). rho:YFP-NTR embryos were collected and raised in zebrafish E3 embryo media (5 mM NaCl; 0.17 mM KCl; 0.33 mM CaCl; 0.33 mM MgSO4). At 16 hr post fertilization (hpf), N-phenylthiourea (PTU) was added to E3 media (E3/PTU) at a final concentration of 0.2 mM to promote ocular transparency by inhibiting melanosome maturation in the retinal pigment epithelium. At 4 dpf, visual screens were performed to remove larvae with abnormal morphology or low YFP expression levels. Stock drug and DMSO (negative control) solutions were automatically dispensed and diluted across a 96-well plate containing E3/PTU using a robotic liquid handling system (Hudson Robotics). At 5 dpf, a COPAS-XL (Complex Object Parametric Analyzer and Sorter, Union Biometrica) was used to dispense single larvae into individual wells containing either drug or DMSO; the final DMSO concentration was 0.1% across all conditions. After a 4 hr pre-exposure to test drugs or DMSO alone, larvae were treated with 2.5 mM Mtz to induce rod photoreceptor death. Larvae were maintained under these conditions for 2 days until 7n dpf and then anesthetized with clove oil (50 ppm final concentration); YFP signals were measured as described above. Larvae exposed to 2.5 mM Mtz/0.1% DMSO without any tested drug served as controls (‘+Mtz’) for maximal rod cell ablation. Larvae treated solely with 0.1% DMSO served as non-ablated controls (‘-Mtz’) to calculate maximal YFP signal levels. Non-transgenic larvae were used to establish a signal cutoff value, as previously described (White et al., 2016). A customized R code program was applied for real-time data analysis of compound performance relative to controls, including dose-response curves and strictly standardized mean difference (SSMD) scores (https://github.com/mummlab/ARQiv2; Ding and Zhang, 2021). Compound concentrations producing a SSMD score ≥1 were considered potential ‘hits’ and evaluated visually using fluorescence microscopy to eliminate non-specific fluorescence; e.g., dead larvae or autofluorescent compounds.

### Secondary confirmation assay - rho:YFP-NTR zebrafish

After the initial screen, 42 top-performing ‘hit’ compounds were selected for confirmatory and orthogonal assays. Hit drugs were obtained from new sources and tested across a wider range of concentrations (fivefold dilution series, eight total concentrations, n=30 fish/condition). Based on the toxicity profile of each drug, the starting concentration was either 100, 10, or 1 μM. For validation assays, YFP signals were measured by fluorescence microplate reader with at least three experimental repeats conducted and SSMD scores calculated. All experimental results were normalized and pooled to calculate effect sizes, confidence intervals, sample sizes (N) and p-values. p Values were calculated using Student’s t-test followed by Bonferroni correction for multiple comparisons resulting in an adjusted significance level of 0.005 (α=0.005).

### Confocal imaging - rho:YFP-NTR and rho:YFP-NTR2.0 zebrafish

For in vivo confocal imaging assays, five dpf rho:YFP-NTR larvae were treated with drug plus 2.5 mM Mtz/0.1% DMSO (ablated +Mtz controls), or 0.1% DMSO (non-ablated -Mtz controls) for 48 hr and processed for intravital imaging at 7 dpf. Similar treatment strategy was applied to five dpf rho:YFP-NTR2.0 larvae except the Mtz treatment was reduced to 10 μM. All compounds were tested at the maximal effective concentration in 0.1% DMSO. Larvae from each group were anesthetized in 0.016% tricaine and embedded on their sides in 1% low melt agarose gel. An Olympus Fluoview FV1000 confocal microscope with a 20x water immersion objective (0.95 NA) was used to collect 30–40 z-stack images of YFP-expressing rod cells across the whole retina at 4 μm intervals. These image slices were stacked into a single maximal intensity projection image using Image J. To provide greater detail of rod photoreceptor morphology, a region in the dorsal-nasal quadrant was imaged using a 60× water immersion objective (1.10 NA) at 4.18 μm intervals. Three contiguous image slices were then stacked into a single maximal intensity projection image using Image J. As a means of assessing rod photoreceptor survival, intravital confocal retinal images were collected of YFP-expressing rod cells per condition and processed for volumetric quantification of YFP signal volume using automated image analysis software (Imaris 3.9.1; see White et al., 2017). Briefly, YFP-expressing rod cells volumes were automatically rendered using the same parameters across all treatment groups with the sum of all volumes used to estimate rod photoreceptor numbers per each retina. For images from rho:YFP-NTR2.0 larvae, the sum of rod cell YFP volumes in each retina was normalized to the number of YFP-expressing cells to estimate the average rod photoreceptor cell size per each condition. The average number of cells quantified per retina was 18.52, with sample sizes ranging from 9 to 19 fish per condition.

### In vitro nitroreductase inhibition assay

The eleven lead compounds were tested to eliminate false-positives that directly inhibited E. coli NTR enzymatic activity (from the nfsB_Ec gene) using an established anticancer prodrug (CB1954) reduction assay (Prosser et al., 2010). The highest soluble concentration of the test drug (up to 300 μM maximum) or 0.1% DMSO (rate control) was added to a master mix of 250 μM CB1954/1 μM NTR/250 μM NADPH/10 mM Tris (pH 7.0) to determine any inhibitory effect of the compounds on NTR-mediated reduction of CB1954. Reactions were conducted in 100 μl volume in a 96-well plate format. CB1954 reduction kinetics were assayed at 420 nm unless the test compound exhibited confounding absorbance at 420 nm, in which case NADPH depletion was monitored at 340 nm. The reaction rates for CB1954 reduction in the presence of tested compounds were compared to the DMSO control. Compounds with NTR activity <75% of controls were deemed potentially inhibitory and IC50 values (the concentration required to restrict NTR activity to 50% of the DMSO control) determined.

Compounds were also evaluated for the ability to inhibit NTR-mediated reduction of Mtz. For this assay, the highest soluble concentration of the test drug (up to 300 μM maximum) or DMSO (rate control) was added to a master mix of 500 μM Mtz/17 μM NTR/100 μM NADPH/0.55 μM glucose dehydrogenase/5 mM glucose/50 mM sodium phosphate buffer (pH 7.0; the glucose dehydrogenase used for cofactor regeneration, maintaining a steady-state of NADPH to allow Mtz reduction to be monitored directly at 340 nm without interference from NADPH oxidation). Reactions were conducted in 100 μl volume and assayed at 340 nm using 1 mm quartz cuvettes (Rich et al., 2018). IC50 values for potentially inhibitory compounds were measured as with CB1954. All kinetic assays were conducted in triplicate with a single purified batch of NfsB_Ec protein.

### Rod photoreceptor Neogenesis assay - rho:YFP-NTR zebrafish

To evaluate whether lead compounds promoted rod photoreceptor development, rho:YFP-NTR larvae were handled as described for the primary screen with the following exceptions: at five dpf, larvae were exposed solely to test compounds; larvae were not treated with Mtz. YFP reporter signals were quantified by fluorescence microplate reader at 7 dpf and compared to non-ablated ‘-Mtz’ controls treated only with 0.1% DMSO. Sample sizes ranged from 58 to 88 across at least two experimental repeats.

### Rod photoreceptor regeneration assay - rho:YFP-NTR zebrafish

To determine whether lead compounds stimulated retinal regeneration, rho:YFP-NTR larvae were handled as described for the primary screen with the following exceptions: at 5 dpf, larvae were incubated with either 10 mM Mtz or 0.1% DMSO for 24 hr. At 6 dpf, larvae were then placed in new 0.1% DMSO/E3/PTU media containing test compounds (or DMSO alone) for 3 days. YFP signal intensity was measured at 9 dpf. Sample sizes ranged from 31 to 83 across at least two experimental repeats.

### Primary mouse retinal photoreceptor cell culture assays

A transgenic mouse line with an IRES-GFP cassette integrated at the QRX locus (QRX-IRES-EGFP) has GFP reporter expression restricted to retinal photoreceptors, and was used here to isolate primary photoreceptor cells. Mice were housed with 12 hr light/12 hr dark cycles, at 22°C, 30–70% relative humidity and food/water ad libitum. Primary mouse retinal photoreceptor cells were isolated and prepared for culture as previously described (Fuller et al., 2014). Briefly, murine retinas were isolated at postnatal day four (P4). Retinal tissue was dissociated into a single-cell suspension by incubating whole tissue in activated papain in Hibernate-E without Calcium (BrainBits) for 15 min at 37°C. Cells were resuspended in culture media (Neurobasal, 2% B-27, 0.5 mM L-Glutamine and 1x final Penicillin/streptomycin; all Life Technologies) and seeded onto poly-D-lysine coated 384 well tissue culture plates. To test lead compounds for survival effects, thapsigargin and tunicamycin (Sigma) and were used as stressor compounds to induce photoreceptor cell death. Stressors and test compounds were added at the time of primary cell seeding. Eleven lead compounds were tested at seven concentrations across a threefold dilution series (from 30 µM to 40 nM). For paired tests, each compound was applied at a single concentration, WAR (3.33 µM), CPO (0.04 µM), DHA (1.11 µM), ART (10 µM), ZPT (0.12 µM), CAL (0.04 µM), COR (3.33 µM), CHL (3.33 µM), SUL (3.33 µM), MIC (10 µM), and CLO (1.11 µM). After a 48 hr treatment, cells were stained with Hoescht and ethidium homodimer; nine field images were acquired via an automated imager (Cellomics Vti; ThermoFisher) using a 20x objective and images analyzed. Photoreceptor number and the percent of photoreceptor to retinal cell population per well was determined by automated quantification of the number of live Hoechst 33342-stained, GFP-expressing cells using a custom algorithm (Neuronal Profiling software package; ThermoFisher). A minimum of two experimental repeats was performed for each test with individual assays consisting of six biological replicates per condition tested.

### Retinal explant assay - Pde6brd1 (rd1) mouse

Mice were generated from retinal degeneration 1 (Pde6brd1, hereafter rd1) breeding pairs (gift from Dr. Debora Farber; UCLA) and housed under a 12:12 light:dark cycle with access to food and water ad libitum. All chemicals used for organ cultures were tissue culture grade and purchased from Invitrogen unless otherwise noted. Cultures of retina with attached retinal pigment epithelium (RPE) were grown according to published protocols (Ogilvie et al., 1999; Pinzón-Duarte et al., 2000; Rohrer and Ogilvie, 2003) with modifications (Bandyopadhyay and Rohrer, 2010). P10 pups were decapitated and heads were rinsed in 70% ethanol; whole eyes were dissected and placed in ice-cold Hanks balanced salt solution plus glucose (6.5 g/L). Eyes were first incubated in 1 mL of high-glucose Hanks balanced salt solution/0.5 mg/ml proteinase K (37°C, 7 min) and then in Neurobasal medium (Life Technologies) plus 10% fetal calf serum to stop enzymatic activity. The retina with attached RPE was dissected free from the choroid and sclera after removing the anterior chamber, lens and vitreous. Relaxing cuts were made to flatten the tissue prior to transfer to the upper compartment of a Costar Transwell chamber (RPE layer faced-down) using a drop of Neurobasal medium. Neurobasal media with B-27 supplement (Life Technologies) was placed in the lower compartment. For each of the cohorts, three to fourindividual P10 retina/RPE explants were placed in culture. The cultures were kept in an incubator (5% CO2, balanced air, 100% humidity, 37°C) and the lower compartment media changed every 2 days (neither antimitotics nor antibiotics were required). Test compounds were added to the culture media and refreshed every 2 days for 11 days. At completion, explants were fixed in 4% PFA, sectioned 14 µm thick, and stained with toluidine blue (Bandyopadhyay and Rohrer, 2010). For each culture, 10 counts of rows of photoreceptors were performed in the center of the explant; the average of this cell counts provides the mean for each retina, with the average of all retinas providing the mean ± SEM per culture condition. Cell counts were compared by repeated measure ANOVA to assess dose-response treatment effects followed by a Bonferroni posthoc analysis to determine if differences between control and lead compounds compared across the entire dose range were statistically significant. An ANOVA across groups but within a particular dose, using a Bonferroni/Dunn test to reduce type I errors, was used to determine if lead compounds promoted a statistically significantly increase in cell numbers compared to control media at low, middle, and/or high concentrations.

### Long-release formulation of DHA

PLGA-DHA microparticles were prepared using a single emulsion solvent evaporation method. Briefly, 200 mg PLGA (Resomer RG 502 hr, Poly(D),L-lactide-co-glycolide; Evonik Corporation) was dissolved in 1 mL of dichloromethane (DCM, Sigma-Aldrich), and mixing with 40 mg DHA (TCI, Tokyo, Japan) dissolved in 0.125 ml dimethyl sulfoxide (DMSO, Sigma-Aldrich). The mixture was homogenized (L4RT, Silverson Machines) at 7000 RPM for 1 min. The homogenized mixture was then poured into a solution containing 1% polyvinyl alcohol (25 kDa, 88% hydrolys, Polysciences, Warrington, PA) in water under continuous stirring. Particles were hardened by allowing solvent to evaporate while stirring at room temperature for 2 hr. Particles were collected via centrifugation (International Equipment Co) at 1000 x g for 5 min, and washed three times with HyPure cell culture grade water (endotoxin-free, HyClone, Logan, UT) and re-collected by centrifugation three times. The washed particles were then lyophilized and stored frozen until use. Microparticles were resuspended at the desired concentration prior to injection in a sodium hyaluronate solution (Healon) diluted fivefold with endotoxin-free HyPure water at the desired concentration prior to injection.

### Characterization of PLGA-DHA microparticles

Particle size distribution was determined using a Coulter Multisizer 4 (Beckman Coulter, Inc, Miami, FL). Particles were resuspended in double distilled water and added dropwise to 100 ml of ISOTON II solution until the coincidence of the particles was between 8% and 10%. At least 100,000 particles were sized for each batch of particles to determine the mean particle size and size distribution. To determine the drug loading, microparticles were dissolved in DMSO and the total drug content was calculated by measuring the UV absorbance at 289 nm after react with NaOH in triplicate (C.-S. Lai et al., 2007a). The average microparticle size was 14.2 ± 1.9 µm and the DHA loading was 20.3% ± 0.7 (w/w) across three experimental replicates.

### PLGA-DHA release kinetics in vitro

Release kinetics were obtained by resuspending microparticles in 1 ml phosphate buffered saline (PBS containing 0.1% DMSO, pH 7.4) and incubating at 37°C on a platform shaker (140 RPM). Supernatant was collected at predetermined intervals by centrifugation at 2000 x g for 5 min. Drug-containing supernatant was collected and particles were resuspended in 1 ml of fresh 1xPBS containing 0.1% DMSO. DHA concentration in the collected supernatant was assayed via absorbance at 289 nm in triplicate for each sample (Figure 4—figure supplement 1).

### In vivo mouse retinal assay - Pde6brd10 (rd10) mouse model

B6.CXB1-Pde6brd10/J animals (Jackson Laboratories stock #004297) were maintained as homozygotes. On P14, animals were anesthetized with ketamine/xylazine (115 mg/kg and 5 mg/kg, respectively), and placed on a heating pad to maintain body temperature throughout injection and recovery. Glass needles were pulled and a bore size of approximately 75 µm was made to allow for the movement of the microspheres into and out of the needle. A PLI-100 picospritzer (Harvard Apparatus) was used for intravitreal injections with settings of 350 ms injection time at 30 psi, which yielded the injection of approximately 500 nL. One eye was randomly selected for injection with vehicle and the other was used for microsphere injections. Following injection, GenTeal gel (Novartis) was applied to the eyes to prevent corneal drying. Animals were monitored until they were awake and moving normally. A total of 17 mice was used across three technical repeats.

Eighteen days post-injection, animals were anesthetized with isoflurane and decapitated; the eyes were removed and placed in 4% PFA for 30 min. After removing the cornea and lens, the eye cups were placed back into fixative for 2 hr on ice. After thorough washing with 1× PBS, eyecups were soaked in 15% sucrose (w/v) in 1× PBS for 3 hr, then incubated in 30% sucrose (w/v)/1× PBS overnight. Samples were embedded in OCT compound (TissueTek) and frozen on dry ice. Cryosections of 12–14 µm thickness were cut on a Leica CM3050S cryostat and were mounted on Superfrost Plus slides (Fisher Scientific). Slides were rehydrated with 1× PBS and then incubated in blocking buffer (10% Normal donkey serum/ 0.3% Triton X-100/1× PBS) for 2 hr, and were then incubated for 30 hr at 4°C with primary antibodies diluted in blocking buffer. Sections were washed in 1× PBS and incubated for 2 hr at room temperature with secondary antibodies diluted in blocking buffer. Following additional washes, sections were incubated with DAPI and mounted with FluoroGel (Electron Microscopy Sciences).

Sections were examined using a Zeiss Axioplan two epifluorescence microscope fitted with an Axioscope camera. Following acquisition with a 40× air objective, images were analyzed in ImageJ using the measure tool to examine Outer Nuclear Layer (ONL) thickness. Four to 5 measurements were taken at 75 µm intervals for 200–500 µm both superior and inferior from the optic nerve head. The measured values from multiple sections were averaged for each eye. Data were analyzed and statistical tests were performed in GraphPad Prism 7. An Olympus FV1000 confocal microscope was also used to image sections stained with multiple dyes.

### Shared MOA and cell death pathway inhibitor assays – rho:YFP-NTR zebrafish

To evaluate tdp1 and parp1 as a potential shared target across multiple leads, as well as cell death pathways implicated in photoreceptor degeneration, eight PARP inhibitors, one necroptosis inhibitor, three apoptosis inhibitors, and three Tdp1 inhibitors were selected for testing using the confirmation screening protocol (Figure 2A). Based on the toxicity profile of each inhibitor, upper concentrations were adjusted to 64, 32, or 8 µM and a twofold dilution series was used to test a total of 10 concentrations for rod cell survival effects in rho:YFP-NTR larvae. Sample sizes varied from 27 to 173 across two to six experimental replicates for each tested compound. YFP signal levels were measured by fluorescence microplate reader (i.e. ARQiv assay). Results across conditions were normalized to non-ablated controls and pooled across experimental repeats to calculate effect sizes, confidence intervals, and p-values. P values were calculated by performing Student’s t-tests. Bonferroni correction for multiple comparisons resulted in an adjusted significance level of 0.003 (α=0.003). Note: assessments of TDP1 inhibitors followed the fivefold dilution series protocol used for secondary confirmation assays described above. For paired inhibitor tests, three concentrations of BMN (parp inhibitor) and three concentrations of NEC (necroptosis inhibitor) were combined. YFP quantification and statistical analysis of rod cell survival in Mtz-treated rho:YFP-NTR fish were performed as above.

### CRISPR/Cas9-based gene knockdown

Five genes, parp1, ripk1l, casp3a, casp3b, tdp1, were selected for CRISPR/Cas9-based knockdown in rho:YFP-NTR zebrafish using an established ‘redundant targeting’ methodology (Wu et al., 2018). Four sgRNAs were designed to target each gene. The oligonucleotide for generating each sgRNA was either those suggested by Wu et al., 2018, Table S2 or designed using CRISPRscan (https://www.crisprscan.org, Supplementary file 3; Moreno-Mateos et al., 2015). Preparation of sgRNAs followed the published method (Wu et al., 2018). Briefly, four sgRNAs of each gene were in vitro transcribed using the HiScribe T7 High Yield RNA Synthesis kit (New England BioLabs) and purified using the NEB Monarch RNA Cleanup kit. A mixture of four sgRNAs (1 ng in total) and Cas9 protein (2.5 µM, IDT) was injected into rho:YFP-NTR embryos at the one-cell stage for targeting parp1, ripk1l and tdp1. Four sgRNAs each for casp3a and casp3b were pooled to co-target both genes. Injected and uninjected embryos were treated ±Mtz (2.5 mM) at 5 dpf. Rod cell survival was evaluated by fluorescence microplate reader-based quantification of YFP at 6 dpf. Student’s t-test was used to compare rod survival between injected and uninjected (control) fish. Each gene knockdown experiment was conducted in triplicate or quadruplicate. A subset of lead compounds (and a PARP inhibitor control, BMN) was also tested in parp1 knockdown fish to determine if Parp1 inhibition was required for survival effects. Leads were applied to larvae one hour before Mtz administration and YFP quantification performed as above. Each drug test was conducted in duplicate or triplicate. To calculate p-values relative to +Mtz controls, Student’s t-tests were performed. Bonferroni correction for multiple comparisons resulted in an adjusted significance level of 0.006 (α=0.006).

### Quantitative PCR

To quantify gene expression levels in rho:YFP-NTR larvae ±CRISPR/Cas9-based gene knockdown, 16–24 larvae from each condition were pooled for mRNA extraction at six dpf. RNA was purified using NEB Monarch RNA Cleanup kit and reverse transcribed to cDNA using qScript cDNA synthesis kit (QuantaBio) according to the instruction from the manufacturer. Quantitative PCR was conducted using designed primers (Supplementary file 3) and PowerUp SYBR Green Master Mix (ABI) in QuantaStudio (ABI). Delta delta CT analysis was performed to calculate relative fold change in gene expression levels between knockdown larvae and controls. Each experiment was performed in triplicate or quadruplicate.

### Western blot

To further evaluate Parp-dependent signaling downstream of Mtz treatments in rho:YFP-NTR larvae, PAR accumulation, a vetted measure of Parp activity, was quantified by western blot following the published method (Kam et al., 2018). Briefly, ~30 rho:YFP-NTR fish were treated ±2.5 mM Mtz at five dpf were collected at 3, 6, 12, 24, 48 hr post treatment (hpt). Larvae were homogenized and lysed using RIPA buffer (Sigma) supplemented with protease inhibitors (Roche). Protein concentrations were quantified using Pierce BCA kit (ThermoScientific) following the manufacturer’s instruction. Protein samples were separated on Tris-Glycine gel and then transferred onto nitrocellulose membranes. The membrane was blocked with 5% non-fat milk in TBST (Tris-buffered saline with 0.1% Tween 20) at room temperature for 1 hr and then blotted with the primary antibody, anti-human-PAR (1:2000, Dowson lab reagent), at 4°C overnight. After rinsing in TBST for three times, the secondary antibody, anti-Human IgG-HRP (1:10,000, Abcam) was applied for 1 hr at room temperature. Anti-beta-actin-HRP antibody (1:20,000) was used as a loading control. Immunolabeled bands were visualized by ECL substrate and quantified in Fiji. 24 hr post-Mtz PAR accumulation assays were performed in triplicate. Mann-Whitney U test was performed and a p-value of ≤0.05 used to indicate statistical significance.

### Paired drug testing in zebrafish

To test for additive neuroprotective effects in zebrafish, seven lead compounds were tested at optimal concentrations either individually or in pairs using the primary screen protocol. All experimental results were normalized to controls and pooled per compound tested to calculate effect sizes, confidence intervals, and p-values using Student’s t-test. Bonferroni correction for multiple comparisons resulted in an adjusted significance level of 0.002 (α=0.002). Sample sizes for each paired condition varied from 86 to 160 across at least four experimental replicates.

### Data analysis and statistics

For the primary screening, under the R environment, a customized ARQiv data analysis package was used to calculate sample size (n), quality control strictly standardized mean difference (SSMD) and SSMD scores as previously described (White et al., 2016). The following results of each drug were derived: (1) a plot of signal to background ratio at all tested concentrations, (2) a plot and a table of SSMD scores, and (3) a signal intensity heat map of each drug plate (96-well plate view). To combine and analyze the data from different experiments, data normalization was conducted by (Si -$X-$neg)/($X-$ Pos -$X-$neg). Si is the signal of ith reading, $X-$Pos is mean of positive controls, and $X-$Neg is mean of negative controls. To compare between experimental conditions and controls, Student’s t-tests were performed followed by Bonferroni correction for multiple comparisons (α/n). Relative effects, 95% confidence intervals and p-values were calculated. For mouse photoreceptor cell culture assays and volumetric confocal image analyses, adjusted p-values were calculated by performing Mann-Whitney U tests followed by false discovery rate correction for multiple comparisons.

# Frequent exchange of the DNA polymerase during bacterial chromosome replication

## Authors

- Thomas R Beattie<sup>1</sup>
- Nitin Kapadia<sup>1</sup> ([ORCID: 0000-0003-4514-7631](https://orcid.org/0000-0003-4514-7631))
- Emilien Nicolas<sup>2</sup>
- Stephan Uphoff<sup>2</sup>
- Adam JM Wollman<sup>3</sup>
- Mark C Leake<sup>3</sup>
- Rodrigo Reyes-Lamothe<sup>1</sup> ([ORCID: 0000-0002-5330-3481](https://orcid.org/0000-0002-5330-3481)) †

### Affiliations

1. Department of Biology McGill University Montreal Canada
2. Department of Biochemistry University of Oxford Oxford United Kingdom
3. Biological Physical Sciences Institute, Departments of Physics and Biology University of York Heslington United Kingdom

† Corresponding author

## Abstract

The replisome is a multiprotein machine that carries out DNA replication. In Escherichia coli, a single pair of replisomes is responsible for duplicating the entire 4.6 Mbp circular chromosome. In vitro studies of reconstituted E. coli replisomes have attributed this remarkable processivity to the high stability of the replisome once assembled on DNA. By examining replisomes in live E. coli with fluorescence microscopy, we found that the Pol III* subassembly frequently disengages from the replisome during DNA synthesis and exchanges with free copies from solution. In contrast, the DnaB helicase associates stably with the replication fork, providing the molecular basis for how the E. coli replisome can maintain high processivity and yet possess the flexibility to bypass obstructions in template DNA. Our data challenges the widely-accepted semi-discontinuous model of chromosomal replication, instead supporting a fully discontinuous mechanism in which synthesis of both leading and lagging strands is frequently interrupted.

## Introduction

DNA replication is carried out by a multifunctional machine, the replisome (Beattie and Reyes-Lamothe, 2015). The E. coli replisome has been characterized in vitro and in vivo and is composed of more than 12 different proteins (Kurth and O'Donnell, 2013; Reyes-Lamothe et al., 2010). DNA synthesis is performed by the Pol III polymerase (αεθ). Three copies of Pol III are incorporated into the replisome through an interaction with the τ subunit of the pentameric clamp loader complex (τ3δδ’). Together, these constitute the Pol III* subassembly ((αεθ)3-τ3δδ’). The clamp loader is also responsible for loading the β clamp dimer onto DNA, which is required for processive synthesis by Pol III. Addition of β clamp to Pol III* forms the Pol III holoenzyme. At the core of the E. coli replisome is the replicative helicase, DnaB, which encircles the lagging strand template and unwinds parental DNA. The Pol III holoenzyme associates with DnaB through the τ subunit of the clamp loader (Figure 1A). In addition, the DnaB helicase recruits the primase, DnaG, which synthesizes RNA primers. Due to the antiparallel nature of DNA, synthesis of one the strands – the leading strand – occurs co-directionally with progression of the replication fork, while the second strand – the lagging strand – is synthesized by repeated cycles of primer synthesis and DNA extension.

![Figure 1.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig1-v2.jpg)

**Figure 1.:** (A) Model illustrating the architecture of a replisome at the E. coli replication fork. (B) Representative fluorescence images of FRAP experiments for the Pol III α subunit and the DnaB helicase. Cell boundaries shown as white lines, red circle shows the location of the bleached focus. (C) Representative examples of the FRAP curves for Pol III α subunit (N = 48) and DnaB (N = 96). Red line shows a reaction-diffusion model fit to the data, dashed grey lines show SE for the model. Dashed blue line represents the estimated maximum possible fluorescence recovery after correcting for photobleaching. (D) Analysis summary of the replisome by FRAP. Bars represent average bound-times. Red squares represent level of recovery normalised to the intensity before bleaching. Dashed blue line represents maximum possible fluorescence recovery. It was not possible to estimate the bound-time for DnaB. Error bars represent SE.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Representative images of non-treated (M9-Gly) or cells treated with 40 µg/ml of cephalexin (M9 Gly + Cephalexin) are shown. The position of the ori1 locus (mapped at 3908 kb in the chromosome), labelled by TetR-mCerulean bound to a tetO array, is shown in red, while the position of the replisome component SSB labelled with YPet is shown in green. Top panels do not show the phase contrast. Scale bar represents 2 µm. A table summarizes analysis of this data, showing the number of ori1 and SSB foci per cell, and the ratio between them. (B) Distribution of the total intensity of DAPI signal against cell length in cells untreated (blue dots) and treated with cephalexin for one hour (red dots). Ethanol fixation was used to ensure homogenous permeability to the dye. Fitting to a linear model is shown in the respective colours. The inset shows the distribution of mean intensities per pixel for both conditions. (C) Distribution of the total intensity of ε-YPet signal against cell length in cells untreated (blue dots) and treated with cephalexin for one hour (red dots). Fitting to a linear model is shown in the respective colours. The inset shows the distribution of mean intensities per pixel for both conditions.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Representative fluorescence images of a cell carrying a tetO operator array and expressing TetR-YPet. Cells were fixed with formaldehyde to avoid protein exchange. Cell boundaries are represented with a white line. The point of localized bleaching is shown with a red circle. (B) Average distribution of fluorescence recovery after photobleaching of 49 cells. Note that intensity increase after bleaching is minimal (<5% of the total intensity), consistent with stochastic fluctuations and experimental measurement error. Error bars represent SE.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Growth curve of AB1157 in M9-Glycerol at 22°C is shown. Samples were taken every hour for 7 hr. (B) Distribution of the number of spots per cell of a strain carrying ε-YPet grown in M9-Glycerol at 22°C (N = 1403 cells). We estimated the replication time by taking into account the generation time and the number of cells with spots. We made the assumption that initiation of DNA replication occurs at cell birth to account for the uneven distribution of cell ages in the population. (C) Representative images obtained from a time-lapse experiment of a strain carrying SSB-YPet grown on a 1% agarose pad in M9-Glycerol at 22°C. Pictures were taken at 10 min intervals. Replication time was determined from the time point of first appearance of SSB-YPet spot to its subsequent disappearance (N = 56 cells). The average of the two methods (150 min) is reported in the main text.

Replication of the circular chromosome of E. coli proceeds bidirectionally from a single, defined locus: oriC. Multiple mechanisms tightly restrict DnaB loading, and therefore replisome assembly, to the oriC locus during initiation, with a single initiation event per cell cycle (Costa et al., 2013). Two sister replisomes are assembled at oriC during initiation, and each is responsible for replicating half of the ~4.6 Mbp chromosome. At 37°C, it takes 40–60 min of continuous DNA synthesis to complete chromosomal replication, at rates of 600–1000 bp s−1.

Given the extent of DNA synthesis required, it has been assumed that the replisome is a stable protein complex capable of replicating large fragments of the chromosome without disassembling. This is supported by in vitro data showing that a single purified replisome, once assembled on DNA, is capable of synthesizing DNA with an average length of 70 kbp without requiring replacement of the Pol III* subassembly or DnaB (Tanner et al., 2011; Yao et al., 2009). Even greater stability has been inferred from in vivo experiments that suggest infrequent replication fork collapse during chromosome replication in E. coli (Maisnier-Patin et al., 2001).

Chromosomal DNA presents multiple potential obstacles to replisome progression. DNA lesions can result in the stalling of the replisome due to Pol III’s inability to use damaged DNA as a template (Moore et al., 1981). In addition, the replisome frequently encounters DNA-bound proteins, potentially resulting in disassembly or pausing (Mettrick and Grainge, 2016; Gupta et al., 2013). Multiple mechanisms have been proposed that allow replisome integrity to be maintained during bypass of such obstacles (Heller and Marians, 2006a; Yeeles and Marians, 2011; Pomerantz and O'Donnell, 2008) and that remove bound proteins from DNA (Gupta et al., 2013). In cases where these strategies are insufficient, the cell also has mechanisms to mediate the reassembly of the replisome at specific DNA structures that arise following replisome collapse (Heller and Marians, 2006b). The frequency at which replisomes encounter these obstacles and the efficiency of the bypass mechanisms are still unclear. It is also uncertain in which way the architecture and stability of replisome play a role during these events.

The replisome is likely to be affected by multiple factors present inside cells which have not been accounted for in reconstituted systems. However, a direct measurement of the stability of the replisome has not been undertaken in vivo. Here we measure the binding kinetics of replisome subunits during DNA replication using two independent fluorescence-based methods in living cells. Our results show that the entire Pol III* subassembly is replaced within the replisome at a frequency equivalent to a few cycles of Okazaki fragment synthesis. This leads us to conclude that DNA replication is a discontinuous process on both strands. We also find that the DnaB helicase remains bound to DNA for tens of minutes, preventing disassembly of the replisome likely by serving as a dock during Pol III* subassembly turnover. We propose that this dynamic stability provides the replisome with flexibility to bypass frequent obstacles on DNA while maintaining the necessary processivity for chromosomal replication.

## Results

### Fluorescence recovery after photobleaching reveals frequent exchange of subunits in active replisomes

To assess the stability of the E. coli replisome when replicating chromosomal DNA in vivo, we first measured the binding kinetics of replisome subunits using fluorescence recovery after photobleaching (FRAP) in strains possessing fluorescent YPet derivatives of key replisome components (Reyes-Lamothe et al., 2010, 2008). Using actively replicating cells in growth conditions that permit a single replication event per cell cycle, we bleached individual foci of fluorescent replisome subunits using a focused laser pulse and measured their recovery over time (Figure 1B). The dimensions of E. coli – in our conditions typically ~0.7 µm diameter and few microns in length – and the low number of replisome subunit molecules per cell – a few hundred for most subunits (Reyes-Lamothe et al., 2010) – increased the difficulty of selectively bleaching replisome foci without affecting the remaining fluorescent pool. To minimize photobleaching of the diffusing pool of fluorescent proteins we increased cell volume by treatment with cephalexin; this did not affect DNA replication (Figure 1—figure supplement 1).

To our surprise, we found that the initial focus fluorescence recovered in a few seconds for Pol III and clamp loader components (Figure 1B). Fluorescence recovery is not explained by the photophysical properties of YPet, like photoblinking, and instead it represents protein exchange (Figure 1—figure supplement 2). We used a reaction-diffusion model in a reaction-limited regime to fit the average fluorescence recovery curve of individual subunits, and calculated a time constant for binding (bound-time) which represents the average time that a molecule is bound to the replisome before exchanging. The bound-time was 4 ± 2 and 6 ± 2 s (mean ± SE) for the α and ε subunits of Pol III, respectively. Similarly, the τ, δ and χ subunits of the clamp loader had bound times of 6 ± 3, 3 ± 2 and 6 ± 4 s, respectively (Figure 1C–D). Molecules of the β clamp exchanged at a slower rate, remaining associated for an average of 36 ± 21 s, consistent with its binding to newly-synthesized DNA behind the replisome (Moolman et al., 2014; Su'etsugu and Errington, 2011). The timescale of Pol III holoenzyme exchange is in striking contrast to the ~150 min required for two replisomes to complete chromosomal replication under our microscopy conditions (Figure 1—figure supplement 3).

### sptPALM demonstrates fast turnover of the Pol III* subassembly

To confirm these results, we used single-particle tracking Photoactivated Localization Microscopy (sptPALM) (Manley et al., 2008) to determine the bound-times of replisome subunits (Uphoff et al., 2013). We constructed E. coli strains with functional fusions of replisome subunits and the photoconvertible fluorescent protein, mMaple (McEvoy et al., 2012) (Figure 2—figure supplement 1). We used a single low intensity pulse of 405 nm-laser activation per experiment to switch, on average, a single molecule per cell into a red fluorescence state. Long (500 ms) camera exposure times – to motion-blur fast diffusing molecules – were used, spaced by 1 s or 5 s intervals, to track non-diffusing replisome-associated molecules as foci (Figure 2A). This illumination protocol did not perturb cell growth (Figure 2—figure supplement 2). Track duration distributions for labelled replisome subunits were calculated from the number of frames individual molecules appeared as foci (Figure 2B–C). Bound times were calculated by correcting for the disappearance of foci due to photobleaching, which was characterized using a strain carrying the transcriptional repressor LacI fused to mMaple and a chromosomal array of lacO binding sites. We also assessed the effect photoblinking using this same strain (Figure 2—figure supplement 3A–C). We expect that in the timescale of our experiments, the lifetime of LacI-mMaple foci will be dictated by photobleaching, with dissociation from DNA being negligible (Hammar et al., 2014).

![Figure 2.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig2-v2.jpg)

**Figure 2.:** (A) Diagram illustrating the sptPALM experimental design used to measure bound-times. (B) Representative example of the focus life span for the Pol III ε subunit. (C) Representative examples of the distribution of fluorescent foci life-spans (blue bars) for Pol III ε subunit and DnaB, showing fitting of a single-exponential decay model (red line), the estimated bleaching rate in the same conditions (blue line) and the corrected estimated bound-time (purple line). Note that to improve accuracy in single-molecule detection tracks shorter than four localizations were removed in the case of ε but corrected during curve fitting, hence the lower bar near 0 s time point. ε data was collected using 500 ms exposure time and 1 s intervals (N = 143), DnaB data was collected using 2 s exposure time and 10 s intervals (N = 86). The plot for DnaB shows binned data for presentation purposes. (D) Summary of estimated average bound-times. Errors in the table represent SE.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Plot showing growth curves of the AB1157 and derivative strains carrying mMaple fusions to replisome components. Experiment was done in M9-Glycerol at 37°C. Average and standard deviation of three experiments are shown. (B) Table that summarizes the results from the growth curve experiments.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Images obtained from an sptPALM experiment of a strain carrying mMaple-DnaB using 2 s exposure times of the 561 nm laser and 2 min intervals (time in minutes). Note the growth of cells despite exposure to a single event of 405 nm wavelength activation and multiple exposures to 561 nm wavelength light. Scale bar = 2 µm. (B) Plot showing lengths of cells over time for eight different cells. The average of doubling-time is similar to the generation time of AB1157 at 22°C.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Frequency of detected short gaps, likely representing photoblinking, during the tracking of a population of LacI-mMaple molecules using 500 ms capture rates. We applied a cut-off threshold at 2.6 s for the maximum duration of photoblinking based on previous characterisation of mMaple (Durisic et al., 2014). More than 75% of the molecules did not show photoblinking (N = 148 molecules). (B) Distribution of gap times between subsequent localizations at the same location of the field of view. Note that most events lasted for only one frame. N = 60 events. (C) We fitted the distribution of gap times to a single exponential function using a truncated form of MLE. This was done to account for the fraction of events shorter than 500 ms, which would be missed in our experiments. Using a 1-frame memory parameter we estimate that our analysis will prematurely terminate less than 7.5%, 3% and 0.0001% of the tracks due to blinking when using a 1 s, 2 s, and 5 s intervals, respectively. (D) Semi-log plots of the data presented in Figure 2C for ε and DnaB. The plots show a relatively linear relation between number of cases and time, which is indicative of a single regime of binding for both subunits. Further support of a single binding behaviour is presented in Supplementary file 1C. (E) Plots showing the PDF curves of bound, bleaching, and tracking times for representative results from a single experiment of ε imaged with 500 ms (left) (N = 143) and 2 s exposure (right) (N = 415). The bound-time was 7.44 s (SE ±1.07 s) and 12.34 s (SE ±1.36 s) for 500 ms and 2 s, respectively. The plot for the 500 ms example is presented to facilitate comparison and is identical to that in Figure 2C.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A–F) Analysis from PALM experiments of ε-mMaple and mMaple-DnaB using a 21 ms capture rate. (A) Calculated MSDs for the two proteins. In both cases, curves plateau at around 600 nm in agreement with the dimension of the short axis of the cell. (B) Comparison of step lengths in the tracks of diffusing molecules analysed. (C–D) Examples of detected tracks for ε and DnaB. Lines of different colours are used to facilitate the observation of individual tracks. A red line was only used to show the position of tracks representing immobile tracks where the apparent diffusion coefficient is close to 0. The outline of the cell is shown in grey. (E–F) Distribution of the apparent diffusion coefficients calculated. 2344 tracks obtained from 77 cells and 2467 tracks obtained from 90 cells were used for ε and DnaB, respectively. (G) Distribution of mean PSFs for the x-axis for tracks of ε-mMaple or mMaple-DnaB obtained from experiments done with 500 ms capture rates. In the case of ε, a clear peak close to 100 nm shows the PSF dimensions of immobile molecules, while a second peak close to 200 nm represents diffusing molecules. In contrast, the dimensions of the PSFs from immobile and diffusive molecules is less clear for DnaB. The dashed line shows the threshold used to assign immobile and diffusing molecules in our analysis.

The single-molecule results are consistent with our FRAP data. Pol III subunit and clamp loader components indeed exchanged rapidly, with ε, τ and δ remaining replisome-associated for only 10 ± 0.7, 10 ± 0.7 and 12 ± 0.9 s (mean ± SE), respectively (Figure 2B and D). We found no strong evidence for multiple binding behaviors of individual subunits (Figure 2—figure supplement 3D and Supplementary file 1C), suggesting that both leading and lagging strand polymerases behave similarly. As with FRAP, we observed similar bound-times for all subunits of both the DNA polymerase III and clamp loader complexes despite a difference in stoichiometry – δ, τ and ε are present in 1, 3 and 3 copies per replisome, respectively (Figure 1A). As such, exchange of individual subunits independently from one another, although still possible, does not easily explain our results. We therefore propose that the unit of exchange of Pol III and clamp loader subunits is the Pol III* subassembly ((αεθ)3-τ3δδ’). This idea is supported by in vitro data that shows that exchange of Pol III at the replication fork requires it to be part of the Pol III* subassembly (Yuan et al., 2016). Cells have an excess of free Pol III that does not interact with the clamp loader (Maki and Kornberg, 1985). Consistent with the notion that only Pol III subunits found within a Pol III* subassembly are competent for exchange, we observed re-binding of single molecules of ε, often to a different replisome, at a much higher frequency than would be predicted if all of the ~270 molecules of ε in the cell were in direct competition (Reyes-Lamothe et al., 2010) (Figure 3A and Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig3-v2.jpg)

**Figure 3.:** (A) Representative example of a cell where a single activate copy of ε-mMaple shows multiple cycles of binding and unbinding (time in seconds). Obtained from an experiment using 2 s intervals between consecutive images. Frame average shows the cellular location of two replisomes. (B) Example of a cell where a single activated mMaple-DnaB molecule remains localized as a focus for several minutes (time in minutes). Obtained from an experiment using 10 s intervals between consecutive images. Boundaries of the cells at the beginning of the experiment are shown as white outlines.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Plot showing the number of rebinding events during a single experiment. (B) Distribution of gap times, calculated from data obtained using 2 s exposure time. Rebinding analysis was done similarly to the track linkage analysis, except no frame threshold was applied. Time between re-binding events was obtained by determining the time interval between the end of a single-molecule track and the beginning of a new track at the same position in the cell. Note that in reality the frequency of binding will likely be higher, since molecules have a similar probability of binding to a different replisome between consecutive events. We manually analysed cells with two replisome spots and estimated that 52% of consecutive spot reappearance events occur at a different position in cells with two replisomes (N = 30 cells; 199 re-binding events).

The β clamp again showed a longer bound-time of 47 ± 3 s in sptPALM. Our estimate is broadly consistent with a previous estimate from E. coli, although ~4 times shorter (Moolman et al., 2014). Assuming similar numbers of DNA-bound β as in that earlier report, we estimate from our results that a new β dimer is loaded at each replication fork every ~2 s. Considering an average rate of fork progression of ~260 bp s−1 – calculated from the duration of replication in the conditions used (Figure 1—figure supplement 3) – we find an average Okazaki fragment length of 520 bp, in close agreement with an in vitro measurement of 650 bp at room temperature (Yao et al., 2009). In contrast, we estimate from FRAP and sptPALM an average replication fork progression of 1–3 kbp prior to Pol III exchange, which would allow completion of multiple Okazaki cycles. We therefore think it unlikely that subunit exchange within the replisome is exclusively linked to the dynamics on the lagging strand.

### DnaB may act as a stable platform upon which the Pol III* subassembly exchanges

The DnaB helicase displayed very different dynamics to other replisome subunits when assessed by FRAP. Crucially, we never observed full fluorescence recovery of DnaB over 5 min of measurement (Figure 1B–D), indicating that it is stably associated with the replisome on this timescale. Our analysis showed an initial recovery of fluorescence with a 7 ± 4 s time constant, which we attribute to the signal from diffusing molecules moving into the bleached area. However, we did not observe a significant increase in the intensity after this initial time point, preventing us from accurately estimating a bound-time for DnaB (Figure 1C). We conclude that in contrast to Pol III holoenzyme subunits, replisome-associated DnaB does not exchange frequently, and is instead a stable component of the replisome.

Analysis of DnaB by sptPALM confirmed that it is the most stable subunit in the replisome. To eliminate incorrect assignment of DnaB fluorescence by our software we used even longer (2 s) exposure times, thus further blurring slow-diffusing molecules (Figure 2—figure supplement 4). Control experiments with ε under the same conditions had no significant effect on calculated bound-times (Figure 2—figure supplement 3E). Crucially, we estimate that single molecules of DnaB remained bound to the replisome for 913 ± 508 s, significantly longer than any other component (Figure 2B–D). The width on the distribution for this estimate is inherently large due to a close similarity between DnaB foci lifetimes and the bleaching time of mMaple (Figure 2C). However, our long bound-time estimate is supported by frequent examples of DnaB fluorescent foci that last for tens of minutes (Figure 3B). Currently we cannot assess the extent at which the turnover detected represents PriABC mediated re-loading of helicase (Heller and Marians, 2006b). Altogether, our data supports a role for DnaB as the primary determinant of replisome integrity.

### Active synthesis is only partially responsible for turnover

To determine if subunit exchange occurs as a consequence of active DNA synthesis, we measured bound-times by FRAP and sptPALM in cells treated with the DNA polymerase inhibitor hydroxyurea (HU) (Sinha and Snustad, 1972). Components of the Pol III* subassembly and the β-clamp showed bound-times two- to six fold higher than in untreated cells (Figure 4A–B). HU had no apparent effect on DnaB FRAP estimates (Figure 4A). We conclude that the exchange of replisome components is at least partially dependent on active DNA synthesis. Remaining turnover may reflect residual DNA synthesis after HU treatment. In addition, it may indicate that the replisome is intrinsically dynamic as a multiprotein complex, with DNA synthesis further increasing subunit exchange.

![Figure 4.](https://cdn.elifesciences.org/articles/21763/elife-21763-fig4-v2.jpg)

**Figure 4.:** (A) Summary of the average bound-times in cells treated with HU, estimated by FRAP. The results for untreated (blue bars) and treated cells (green bars) is shown. Data for the untreated condition is presented to facilitate comparison and is identical to that in Figure 1D. Red squares represent the normalised level of fluorescence recovery. Dashed blue line shows estimated maximum possible recovery. It was not possible to estimate the bound-time for DnaB. (B) Summary of bound-times estimated by sptPALM (weighted average). Results for the untreated (blue bars) and treated cells (green bars) is shown. Data obtained using cells treated with the RNA Polymerase inhibitor Rifampicin is also shown for cells carrying ε-mMaple (purple bars). Data for the untreated condition is presented to facilitate comparison and is identical to that in Figure 2D. Error bars represent SE.

**Table 1.**
 Strains used for this study.


<table>
  <thead>
    <tr>
      <th>Strain</th>
      <th>Relevant genotype</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AB1157</td>
      <td>thr-1, araC14, leuB6(Am), DE(gpt-proA)62, lacY1, tsx-33, qsr'-0, glnV44(AS), galK2(Oc), LAM-, Rac-0, hisG4(Oc), rfbC1, mgl-51, rpoS396(Am),  rpsL31(strR), kdgK51, xylA5, mtl-1, argE3(Oc), thi-1</td>
      <td>Dewitt and Adelberg, 1962</td>
    </tr>
    <tr>
      <td>RRL27</td>
      <td>holC-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL30</td>
      <td>holE-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL32</td>
      <td>ssb-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL33</td>
      <td>holA-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL34</td>
      <td>holD-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL35</td>
      <td>dnaE-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL36</td>
      <td>dnaQ-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL51</td>
      <td>dnaX-ypet kan</td>
      <td>Reyes-Lamothe et al. (2008)</td>
    </tr>
    <tr>
      <td>RRL196</td>
      <td>frt ypet-dnaN</td>
      <td>Reyes-Lamothe et al. (2010)</td>
    </tr>
    <tr>
      <td>RRL368</td>
      <td>frt-ypet-dnaB</td>
      <td>Reyes-Lamothe et al. (2010)</td>
    </tr>
    <tr>
      <td>RRL537</td>
      <td>dnaQ-mMaple kan</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>RRL538</td>
      <td>holA-mMaple kan</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>RRL541</td>
      <td>tetR-ypet kan, [tetO240-gm]852</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>RRL553</td>
      <td>dnaX-mMaple kan</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>RRL557</td>
      <td>frt mMaple-dnaB</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>RRL558</td>
      <td>frt mMaple-dnaN</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>TB44</td>
      <td>dnaB-mMaple kan</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>TB54</td>
      <td>lacI-mMaple kan, [lacO240-hyg]2735::ΔpheA</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>Plasmid</td>
      <td>Features</td>
      <td>Source</td>
    </tr>
    <tr>
      <td>pKD46</td>
      <td>Expression of lambda red genes</td>
      <td>Datsenko and Wanner, 2000</td>
    </tr>
    <tr>
      <td>pCP20</td>
      <td>Expression of Flp recombinase</td>
      <td>Datsenko and Wanner, 2000</td>
    </tr>
    <tr>
      <td>pROD61</td>
      <td>mYPet Kan R6K gamma ori. For C-ter insertions</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pROD83</td>
      <td>YPet Kan R6K gamma ori. For N-ter insertions</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pROD93</td>
      <td>mMaple Kan R6K gamma ori. For C-ter insertions</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>pROD160</td>
      <td>mMaple Kan R6K gamma ori. For N-ter insertions</td>
      <td>This study</td>
    </tr>
  </tbody>
</table>

## Discussion

### A dynamic replisome may help to minimize delays in replication fork progression in the presence of roadblocks

Obstructions in template DNA, particularly protein-DNA complexes, have been shown to cause frequent pausing of the E. coli replisome in vivo (Gupta et al., 2013). In vitro studies have demonstrated that the E. coli replisome is capable of bypassing such obstacles by interrupting leading strand synthesis and resuming extension downstream of the obstruction from a leading strand primer deposited by DnaG or an mRNA synthesized by RNA polymerase (Heller and Marians, 2006a; Yeeles and Marians, 2011; Pomerantz and O'Donnell, 2008). Our data is entirely consistent with this mechanism, whereby bypass could be achieved through detachment of the stalled Pol III* subassembly from DnaB and its replacement downstream of the obstacle with another Pol III* from solution. Because DnaB translocates on the lagging strand, small lesions and large protein blockages on the leading strand can both be bypassed by Pol III* exchange. Note however that we did not observe any apparent effect on the dynamics of Pol III after inhibiting transcription, suggesting that this process is not the main cause of exchange (Figure 4B). On the lagging strand, small template lesions capable of passing through the central pore of DnaB may also be bypassed through Pol III* exchange. In contrast, obstacles on the lagging strand that destabilize DnaB, such as proteins stably bound to DNA or strand discontinuities, would likely result in the disassembly of the replisome. We propose that obstacle bypass along template DNA may be the primary selection pressure that has driven the evolution of a dynamic replisome.

In addition to the model above, we acknowledge that other processes may also exert selective pressure for the generation of the observed replisome binding kinetics. First, unbinding of Pol III* subassembly may result from build-up of helical torsion in the template DNA generated by the coupled synthesis of both DNA strands (Kurth et al., 2013). This is consistent with longer binding times when synthesis was inhibited by HU. Unbinding of a single polymerase from DNA or release of the whole Pol III* subassembly would have the same effect on stress relief. Second, the dynamics observed may be a byproduct of the highly regulated interaction between Pol III and β-clamp. Even though Pol III tightly binds the β-clamp to ensure highly processive synthesis, these two proteins rapidly unbind from each other upon completion of the duplex DNA. The strength of this protein-protein interaction is modulated by the OB domain in the α subunit of Pol III, which binds to ssDNA ahead of the catalytic domain, and the C-terminus of the τ subunit of the clamp loader (Georgescu et al., 2009, Leu et al., 2003). Premature activation of such a switch in both leading and lagging strand polymerases would weaken the grip of the Pol III* subassembly on the replication fork and potentially result in its displacement. This idea is consistent with the presence of ssDNA gaps in the lagging strand (Li and Marians, 2000), which may be explained by a premature loss of Pol III processivity.

Presumably, exchange of Pol III* subassembly within the replisome occurs rapidly enough to minimize potentially deleterious ssDNA gaps between fragments of nascent DNA on the leading strand. However, the rate of DNA unwinding by DnaB decreases by more than 10-fold when DnaB is detached from the τ subunit of the clamp loader (Kim et al., 1996a), providing a potential safety mechanism to limit DNA unwinding and exposure of ssDNA during Pol III* subassembly exchange. It remains to be determined if a newly associated copy of Pol III uses the existing 3’ end at the leading strand or requires the activity of primase to resume synthesis.

### Protein excess in cells is a key factor in the regulation of replisome subunit turnover

Our data apparently contradict in vitro studies which have demonstrated that a single reconstituted E. coli replisome can operate without subunit exchange in synthesizing an average of ~80 kbp (Tanner et al., 2011; Yao et al., 2009). Measurements in those reports were performed by removing all diffusing Pol III* subassembly and DnaB subunits from the reaction. In contrast, in the cell there is a permanent excess of diffusing replisome subunits. We believe this explains the differences observed with our in vivo data. Competition for binding sites between DNA-bound and diffusing molecules has been shown to change the DNA-binding kinetics of proteins such as Fis, HU and NHP6A (Graham et al., 2011), EcoRI (Sidorova et al., 2013), RPA (Gibb et al., 2014) and the transcription factor CueR (Chen et al., 2015). Furthermore, mathematical modelling has shown that it is theoretically possible for a replisome to be stable under conditions in which no extra subunits are present, as in vitro, and yet undergo frequent subunit exchange in the presence of extra subunits, as in vivo, due to subunit competition (Åberg et al., 2016). We think that active synthesis may enhance exchange with the diffusing pool, consistent with our results using HU.

Frequent exchange of DNA polymerases in the presence of extra subunits has been observed in the replisomes of bacteriophages T4 and T7 in vitro (Yang et al., 2004; Johnson et al., 2007). In T7, this occurs through a mechanism in which extra DNA polymerases associate with the bacteriophage DNA helicase and exchange with the active DNA polymerase through competition for DNA binding (Geertsema et al., 2014; Loparo et al., 2011). It will be interesting in the future to determine the mechanisms that exist in E. coli to ensure efficient capture and exchange of the low-abundance Pol III* subassembly.

### DNA synthesis of both leading and lagging strands is discontinuous in E. coli

One predicted consequence of the Pol III* subassembly exchanging as a single unit is that synthesis of both leading and lagging strands will be frequently interrupted, resulting in discontinuities on both strands. This contrasts the widely-accepted semi-discontinuous model of DNA replication. However, while this model is strongly supported by in vitro experiments (Wu et al., 1992), the mechanism that operates in vivo has long been unclear (Yeeles, 2014; Wang, 2005). Okazaki and colleagues’ original characterization of replication intermediates demonstrated that all DNA is initially synthesized as short fragments, supporting fully discontinuous DNA replication (Okazaki et al., 1968). More recent in vivo experiments performed in the absence of DNA ligase support the idea that discontinuities are produced on both leading and lagging strands during DNA replication in E. coli (Amado and Kuzminov, 2013, 2006). Our data provide a mechanistic explanation for these observations, and supports a discontinuous model of DNA synthesis in E. coli.

## Materials and methods

### Strains and growth conditions

All strains used are derivatives of AB1157. Cells were routinely grown in LB or in M9 minimal media. M9 was supplemented with glycerol (final concentration 0.2%); 100 µg/ml of amino acids threonine, leucine, proline, histidine and arginine; and thiamine (0.5 µg/ml). When required, antibiotics were added at the following concentrations: ampicillin (100 µg/ml), kanamycin (30 µg/ml), chloramphenicol (25 µg/ml), cephalexin (40 µg/ml), rifampicin (Rif) (300 µg/ml) and hydroxyurea (HU) (60–100 mM). For microscopy, cells were spotted on a 1% agarose pad in M9-Glycerol. DAPI was used at a working concentration of 300 nM as recommended by manufacturer. Ethanol fixation was done using 70% ethanol in water, followed by two washes with PBS. For TetR-YPet strain, fixation was done using 4% formaldehyde and incubating 15 min at room temperature, 15 min on ice, followed by two washes with PBS.

Chromosomal replacement of replisome genes by fluorescent derivatives was done by lambda red (Reyes-Lamothe et al., 2008; Datsenko and Wanner, 2000). In short, we used plasmids carrying a copy of ypet (Reyes-Lamothe et al., 2008; Nguyen and Daugherty, 2005) or mMaple (McEvoy et al., 2012) followed or preceded by a kanamycin resistance cassette flanked by frt sites as PCR templates. Flexible peptides with sequences SAGSAAGSGEF (YPet C-ter fusions), SAGSAAGSGAV (mMaple C-ter fusions) or SAGSAAGSGSA (YPet and mMaple N-ter fusions) were used as a linker between the fluorescent protein (FP) and the protein targeted. Primers carrying 40-50nt tails with identical sequence to the chromosomal locus for insertion were used to amplify the linker-FP-kanR (or kanR-FP-linker in the case of N-terminal fusions) from template plasmids. The resulting PCR product was transformed by electroporation into a strain carrying the lambda red-expressing plasmid pKD46. Colonies were selected by kanamycin resistance and ampicillin sensitivity, screened by PCR using primers annealing to regions flanking the insertion, and sequenced. In the case of N-terminal fusions, in order to minimize the effect of the insertion on the expression levels of the gene we removed the kanamycin cassette by expressing the Flp recombinase from plasmid pCP20(Datsenko and Wanner, 2000). Gene fusions did not have any apparent detrimental effect on cell growth (Figure 2—figure supplement 1).

LacI-mMaple was generated through lambda red using the strain MG1655. The gene fusion was then transduced, using P1 phage, into an AB1157 derivative carrying a 256-lacO array replacing the pheA gene (chromosomal position 2735 kb)(Wang et al., 2006). Similarly, a TetR-YPet fusion expressed from a lac promoter (Reyes-Lamothe et al., 2014) was transduced into a strain carrying a 256-tetO operator array at R3 (chromosomal position 852 kb) (Wang et al., 2006).

### Fluorescence recovery after photobleaching (FRAP)

Cells were grown in M9-Glycerol at 30°C, treated with cephalexin for 2 hr, harvested at early log-phase (OD6000.1–0.2), concentrated and spotted onto a pad of 1% agarose in M9-Glycerol, contained in a gene frame (Thermo Scientific). Treatment with hydroxyurea was done on the agarose pad by mixing HU with media and agarose. Cells were incubated on the slides for 10 min before imaging.

Most FRAP experiments, except for the TetR-YPet control, were performed using a spinning disk imaging system (PerkinElmer) with a 100x NA1.35 oil objective and an ImagEM EMCCD camera (Hamamatsu Photonics). Images were acquired using Volocity imaging software. An image was acquired in the brightfield channel at the beginning of the experiment to serve as a reference. FRAP was performed by pulse-bleaching using a 488 nm laser for 10–15 ms and 30–50% laser intensity (radius of the spot was diffraction limited at ~300 nm). Two pre-bleach images were captured, the bleach spot was centered on one replisome focus and recovery of the bleached region was recorded at different intervals after bleaching. Image capture was done at a 300 ms frame rate (4–6% 515 nm laser) for most replisome components except for DnaB helicase, for which 500 ms capture rate was used (2% 515 nm laser). For α, ε, τ, δ and χ, we used intervals between pictures of 2 s, 5 s and 10 s. For DnaB and β, we used intervals between pictures of 5 s, 10 s and 20 s. Experiments were done at room temperature.

FRAP to control for photoblinking was done using an epifluorescence system, Leica DMi8, with a 100x oil objective (Leica 100x/NA 1.47 HL PL APO) and an iXon Ultra 897 EMCCD camera (Andor). FRAP was performed using an iLas2 unit (Roper Scientific) using an ILE laser combiner (Andor) and a 150 mW 488 nm laser. Both bleaching and excitation of YPet were done using the 488 nm laser. Acquisition was done using 100 ms exposure at 5 s intervals.

### FRAP analysis

Initial position of spots was manually selected using the coordinates for localized bleaching in the image recorded by the acquisition software. Tracking was then done automatically using a previously developed custom program in MATLAB (Mathworks), ADEMS code (Miller et al., 2015) (freely available at https://sourceforge.net/projects/york-biophysics/). Most experiments analyzed had a pixel size of 100 nm, for which we used a search window with a radius of 5 pixels and an initial guess for the PSF of 3 pixels when fitting candidate spots. For a minority of the experiments, with pixel size of 140 nm, analysis was done using 4-pixel search window and a 2-pixel radius for initial fitting.

Intensity traces were filtered to retain only those where clear bleaching was observed. We removed any trace where the intensity at any of the pre-bleach time points was below the value of the ROI immediately after bleaching (0 s time point). In addition, the intensity at the 0 s time point had to be below 40% of the mean pre-bleach intensity. FRAP data were then normalized by the average intensity of the pre-bleached data points.

To estimate the maximum possible fluorescence recovery (Max recovery), we used the corresponding brightfield image to draw a polygon in ImageJ (Schneider et al., 2012) around cells containing a bleached spot. We used these ROIs to obtain the intensities across the experiment in the fluorescence channel. Max recovery was calculated by dividing the intensity of the cell at 0 s time point by the average intensity before bleaching. An average Max recovery value was obtained from all the bleached cells in the experiment.

To correct for photobleaching during the experiment, a different set of spots was manually selected in cells not exposed to localized bleaching, so they could serve as a baseline control. An average bleaching curve was produced using the intensity traces from these fluorescent foci. All data used to generate the bleaching curve were obtained in the same day using the same strain, excitation settings and interval between pictures as for the FRAP experiment. The average curve was fitted to an exponential decay function. FRAP intensity traces were corrected by dividing each time point by the corresponding normalized value in the fitted bleaching curve.

Data from the same set of experiments were averaged. Data from experiments performed the same day, but having different intervals between pictures, were collated into a single recovery curve. Data were then fitted by an exponential solution of the reaction-diffusion equation in a reaction-limited regime (equation 1) using MATLAB:

$$
y=c−ae^{−bt}
$$

where c is the asymptote for recovery, a the amplitude of recovery, and b the rate of unbinding (i.e. koff). Bound-times are the reciprocal of koff.

Upper boundary for c during fitting was set to the Max recovery (see above), plus ten percent of this value to account for measurement error. In addition to R squared, which is not recommended for non-linear models, goodness of fit was assessed using the Kolmogorov-Smirnov test by measuring the normality in the distribution of residuals (Andrae et al., 2010). Standard errors and 95% confidence intervals (CI) on the parameter estimates were calculated using the variable values previously obtained, as initial estimates, and bootstrap sampling was performed over 10,000 samples (Supplementary file 1A). The values reported in the figures are weighted averages of all the experiments done for the same subunit.

We expect that co-localization of sister replisome will have no effect on the rates calculated since the intensity of every spot is normalized against itself in FRAP, and the average rate of recovery is the same at every replisome. Similarly, in sptPALM binding time of individual molecules should not be influenced by a nearby replisome, resulting only a minimal increase in the probability of re-binding to the same place.

### sptPALM

Cells were harvested from early log-phase cultures in M9-Glycerol (OD6000.1–0.2), concentrated and spotted onto a pad of 1% agarose in M9-Glycerol, contained in a gene frame. Coverslips cleaned with versa-clean, acetone and methanol were used to minimize fluorescent background. Treatment with hydroxyurea was done on the agarose pad, by mixing HU with media and agarose.

Imaging was performed at room temperature on an inverted Olympus IX83 microscope using a 60x oil objective lens (Olympus Plan Apo 60X NA 1.42 oil) or 100x oil objective lens (Olympus Plan Apo 100X NA 1.40 oil). Images were captured using a Hamamatsu Orca-Flash 4.0 sCMOS camera. Excitation was done from an iChrome Multi-Laser Engine from Toptica Photonics. Laser triggering was done through a real-time controller U-RTCE (Olympus). Experiments were done using HiLo illumination setup (Tokunaga et al., 2008) from a single-line cell^TIRF illuminator (Olympus). Olympus CellSens 2.1 imaging software was used to control the microscope and lasers.

For experiments with replisome subunits fused to mMaple, a single 405 nm wavelength activation event, typically lasting less than 20 ms, was followed by multiple 561 nm wavelength excitation events with camera captures of 500 ms spaced by 1 s or 5 s intervals, or camera captures of 2s with continuous excitation (2 s rates) or 10 s intervals. Low levels of exposure to violet-blue light were used to minimize photoxicity and allow cells to continue growing during the experiments (Figure 1—figure supplement 3). To image LacI, we used continuous illumination of 561 nm wavelength after a single 405 nm wavelength activation event at capture rates and intervals of 500 ms or 2 s. We also used 2s capture with 10 s intervals to characterize LacI bleaching in long experiments. Rifampicin experiments were done in a similar manner except Rifampicin was added to the M9-Gly agarose pad, and imaging was done after a 20 min incubation on the agarose pad. We noticed that fewer spots were detected, consistent with inhibition of replication initiation through Rifampicin.

### sptPALM analysis

Images were first segmented in order to remove out-of-cell noise coming from contaminants on the coverslip. Binary masks were created using ImageJ, either from the differential interference contrast (DIC) channel or the green fluorescent channel of mMaple. For DIC, alignment was done by first obtaining a maximum-intensity projection of the PALM timelapse, and subsequently aligning it to the reference DIC, using ImageJ. Each slice of the PALM timelapse was then multiplied by the binary mask, to retain intensities within cells only. An average value of the out-of-cell background was added to regions outside of the ROIs to minimize incorrect assignment by the detection program due to sharp intensity increases.

PALM tracking was performed using previously developed software (Uphoff et al., 2013), based on the DAOSTORM (Holden et al., 2011) localization algorithm. An intensity threshold was used to find candidate molecules. The positions of the candidate molecules were then used as initial guesses for a 2D-elliptical Gaussian fit. The fitted parameters were: x-position, y-position, x-standard deviation, y-standard deviation, intensity, brightness, elliptical rotation angle, and background. Tracking was done based on a widely used algorithm (Crocker and Grier, 1996). Localizations were linked if they appeared within a 300 nm radius between consecutive frames, using a memory parameter of one frame to account for blinking or missed localizations (i.e. the molecule can go missing for one frame and still be linked).

Further refinement of the recorded tracks was done to analyze only those that represented immobile single-molecules. To remove slow-diffusing molecules, we plotted a histogram of the PSFs in x and y for all localizations, and performed a two-component Gaussian mixture fit using Maximum Likelihood Estimation. The component with the smaller mean PSF likely represents bound molecules, whereas the other component represents unbound molecules. The two-component Gaussian mixture model has the following form:

$$
p(\frac{1}{\sigma_{1}\sqrt{2\pi}})e^{\frac{−(x−\mu_{1})^{2}}{2(\sigma_{1})^{2}}}+(1− p)(\frac{1}{\sigma_{2}\sqrt{2\pi}})e^{\frac{−(x−\mu_{2})^{2}}{2(\sigma_{2})^{2}}}
$$

Where p is the mixture probability, σ1 and µ1 are the standard deviation and mean of normal distribution 1, respectively. Likewise, σ2 and µ2 are the standard deviation and mean of normal distribution 2, respectively. From the fit, we identified the mean and standard deviation of the component representing bound molecules. We then took 2 standard deviations above the mean to obtain an initial estimation of the threshold. We assessed the accuracy of tracking by manually comparing the tracking results for a subset of fluorescent spots with their lifetime in the original images. Using this method we determined that a threshold of x ≤ 170 and y ≤ 215, placed on the mean PSF over the track, helped to eliminate most of the unbound molecules from subsequent analysis.

In addition, we varied the threshold on the number of localizations for track acceptance across different time-intervals of capture. Our reasoning was that the probability that a track represents a genuinely bound molecule becomes higher as the time interval used increases (Mazza et al., 2012). Therefore, the thresholds for removing tracks were <4, <3, <2, and <2 localizations for interval times of 1 s, 2 s, 5 s, and 10 s, respectively. The thresholds were selected by comparing the raw image by eye to the tracks found by the tracking software. Technically no tracks were removed for 5 s and 10 s since tracks with 1 localization cannot be used to calculate track durations.

To quantify only single-molecule tracks, we plotted a histogram of the mean intensity of a track and fit using a Gaussian Mixture Model (GMM), utilizing the Expectation-Maximization (EM) algorithm. The intensity values were clustered based on membership probabilities (i.e. the probability of belonging to a particular Gaussian component). We used a 2 component GMM fit for most cases and isolated the cluster having the lowest mean, as the intensity values from this cluster likely represent single molecules. We used a 3 component GMM fit in some cases where a significant portion of the molecules seemed out of focus, resulting in a sharp spike of low intensity values in the histogram. In such cases, we isolated the cluster with the second lowest mean. This was especially important when studying proteins with long bound-times, where track fragmentation has a greater relative effect in underestimating the real track duration. We also performed a Bayesian Information Criterion (BIC) test to confirm that the 3 component GMM fit better than the 2 component model. We used only track durations with single molecule intensity values for subsequent analysis.

To avoid track fragmentation in the analysis of proteins with long bound-times, as in LacI and DnaB, caused by fluctuations in intensity or the molecule moving transiently out-of-focus, we determined the typical length of time that the localization software misses spot detection during long tracks (gap time). We did this by manually comparing the outcome of the analysis to the lifetime of a subset of spots in the original images. We found that on average, the gap was ~4 frames. Therefore, we linked tracks based on the criteria that their mean positions were ≤300 nm apart and gap time between them was <= 4 frames. For these data sets, we performed the GMM fit for isolation of single-molecule tracks after track linkage.

The track durations of multiple samples taken on the same day and time-interval were amalgamated into one data set. In order to get the average track duration, we fitted the track durations using MLE. The reason for our choice of MLE over the more commonly used Least Squares-Estimation (LSE) method is that it is invariant to the bin size (i.e. the parameter estimate is the same regardless of how we bin the data) and it allows us to infer what the population parameter is. Essentially, we use information from our sample data (track duration times and track acceptance threshold) as input into MLE, in order to find the population probability density function (PDF), that makes our data the most likely. The fitted lines represent this PDF (Myung, 2003; Woody et al., 2016).

Histograms were binned based on the square-root rule, where the number of bins is equal to the square root of the sample size. We binned our data for presentation purposes only, in order to reduce noise associated with a finite sample size and reveal our sample distribution more clearly.

The PDF of the track durations is related to bleaching and unbinding as follows:

$$
k_{track}e^{−k_{track}t}=(k_{off}+k_{bleach})e^{−(k_{off}+k_{bleach})t}
$$

Where ktrack is the rate of track durations ending, koff is the rate of unbinding, and kbleach is the rate of bleaching. The model PDF we used for fitting was a left-truncated exponential distribution. This was used to compensate for the fact that we removed short duration tracks from analysis. The general form of this PDF is:

$$
(\frac{1}{\tau})e^{\frac{−(x−L)}{\tau}}
$$

where τ is the mean time, and L is the truncation point/origin of exponential distribution (Balakrishnan and Basu, 1995). Note that the equation has the same form as expected for a translated exponential distribution and so we used this form for all data sets.

To correct for photobleaching, we used LacI tagged with mMaple. LacI is expected to have a binding time significantly longer than the bleaching time of mMaple in our experimental conditions (Hammar et al., 2014). Therefore, since the koff term is much smaller than the kbleach term, the average track duration is equivalent to the average bleach time for mMaple. Note that previous estimates of LacI bound-time at the lacO operator were determined using a single copy of the operator, while we used an array composed of 256 copies of lacO. This should result in even longer apparent binding of the repressor protein and increase the likelihood that focus disappearance is solely due to bleaching. We obtained a constant exposure bleaching curve, which we used for the 1 s, and 5 s intervals (500 ms exposure data). We scaled the average bleach time from the constant exposure bleaching data, in order to use it for different time intervals. The constant exposure bleaching time is related to the average bleaching time as follows:

$$
T_{bleach}=(\frac{t_{interval}}{t_{exp}})T_{constant}
$$

Where $t_{interval}$ is the interval time, $t_{exp}$ is the exposure time, and $T_{constant}$ is the constant exposure bleaching time.

We then calculated the average bound time using the following equation:

$$
T_{bound}=\frac{T_{track}T_{bleach}}{T_{bleach}−T_{track}}
$$

In order to calculate the SE and 95% CI on the parameter estimates, we used the right-hand side of Equation 3. We used the bleaching times and bound times calculated previously, as initial estimates, and then performed bootstrap sampling over 10,000 samples, in order to calculate the standard errors and confidence intervals on the bound time estimates. We used the ‘bias and accelerated percentile method’ (BCA) algorithm when calculating CI, in order to compensate for any bias or skewness in the bootstrap distribution.

Previous characterization of photoblinking of mMaple found 49% probability of blinking and an average of 3.4 blinking events per molecule (Durisic et al., 2014). This same study set a cutoff time of 2.6 s to account for over 99% of the blinking events. We expected to detect fewer blinking events since the shorter ones will be recorded only as intensity fluctuations, and not discontinuities in the track, due to the use of longer capture rates, 500 ms instead of 100 ms. In addition, lower exposure intensity would likely contribute to a decrease rate of blinking (Garcia-Parajo et al., 2000). To estimate the effect of blinking in our analysis, we used the data of LacI using 500 ms capture-times. We analysed the data as previously except that we did not apply the one-frame memory parameter during tracking. We then determined the number of frames between two consecutive tracks at the same position of the field of view. We used a 2.6 s cutoff in our data since longer gap times likely represent new binding events instead of blinking.

For DnaB, since 500 ms capture-times were not efficient at preventing diffusing molecules from being detected, even after the PSF threshold was applied (Figure 2—figure supplement 4G), we used exposure times of 2 s and spaced capture by intervals of 2 s and 10 s. We used Pol III ε subunit as a control to ensure that increasing the exposure time does not significantly alter the bound time estimates (Figure 2—figure supplement 3).

Since the track durations of DnaB are similar to those of LacI, we determined a weighted average of the track duration times obtained and for each data set of DnaB performed a constrained fit (i.e. fitting with bounds placed on the estimates). We calculated a bound time from the weighted average in order to generate an initial estimate of the bound time, which was then used for the constrained fit. We allowed for 20% variation in the bleaching time in order to determine physically reasonable estimates. The lower and upper bounds for the DnaB bound time were 1 s and 90 min, respectively.

For the fitting procedure, we calculated the negative log-likelihood function of the two parameter (bleach time, bound time) left-truncated exponential distribution, as well as the gradients. We then used the MATLAB minimization function, fmincon, in order to find the parameters that minimize the negative log-likelihood function. This was done to improve the convergence to the correct solution, especially if the initial estimates were far from the actual solution, and to simplify the estimation procedure. We subsequently performed bootstrap sampling as discussed before to calculate standard errors and confidence intervals (Supplementary file 1B).

The final estimates for bound times were calculated by doing a weighted average of data taken on multiple days and with different time intervals.

We performed a chi-square goodness of fit test under the null hypothesis that our data is sampled from a single-exponential distribution, and the alternative hypothesis that it does not. It is possible however that even if the fit is good, that a different model fits the data better (e.g. two exponential model). We wanted to determine the best model for the data and we performed two tests in this regard: (1) Log-Likelihood Ratio(LLR) test and (2) Bayesian Information Criterion (BIC) test.

Log-Likelihood Ratio Test- The LLR test tries to test if an unconstrained model statistically significantly fits the data better than the constrained model, by comparing the likelihood values obtained from the unconstrained versus the constrained. In our case, the unconstrained model is the two-exponential model while the one-exponential model is the constrained model, as shown below:

$$
p(\frac{1}{\tau_{1}})e^{\frac{−(x−L)}{\tau_{1}}}+(1−p)(\frac{1}{\tau_{2}})e^{\frac{−(x−L)}{\tau_{2}}}
$$

where τ1=(Tbleach+Tboundα)/Tbleach*Tboundα, τ2=(Tbleach+Tboundβ)/Tbleach*Tboundβ, p is the mixture probability, and L is the truncation point.

Note that if we constrain p=1, we recover the single-exponential model.

Bayesian Information Criterion (BIC) test- The BIC test determines which model fits the data better, but penalizes for greater complexity (i.e. more parameters), to prevent over-fitting the data. The lowest number obtained through the test indicates the model that fits the data the best with the least complexity.

When calculating the MLE estimates and log-likelihood values for the two-exponential model, the lower and upper bounds for the two timescales were 0.1 and 5400 s, respectively. The bounds for the bleaching constant were placed such that it allowed for 20% variation in the estimate.

The criterion we used to judge if the two-exponential model was the better model, was if the BIC test gave the lowest value for the two-exponential model and the LLR test gave a p<0.01. Also, the estimates obtained from the two-exponential should be sensible, and especially, they should not give us simply the values of the bounds, as that indicates that no estimates were found.

We found a few cases where the dataset passed the criterion. The timescales estimated were not consistent however, and upon further examination we realized that it was due to a few noticeable outliers in the dataset, possibly from noise due to dirt still on the coverslip. When we removed the outliers, it resulted in these datasets not passing the criterion, but without significantly changing the bound times previously obtained in the single-exponential fits.

### Blinking analysis of mMaple for sptPALM

We used LacI data collected with 500 ms exposure as fast as possible (~500 ms interval time), to characterize mMaple under our acquisition settings. The mean positions of single-molecule tracks initiating at the first frame were used as ROIs around which a 7 × 7 pixel window was drawn to extract intensity-time traces. Fluorescence from a bound molecule was identified as being 2 standard deviations above the mean cellular background, and the signal had to be above this threshold for >3 localizations (similar to track acceptance threshold previously described). Gap durations were calculated as the number of frames between bound fluorescence signals. Fits to the gap durations were done through MLE using a truncated exponential model. The resulting fit was used to calculate the probability of a gap duration lasting greater than a specified value, through integration.

### Estimation of β-clamp loading rate

To estimate the effective loading rate we followed the following equation described elsewhere (Moolman et al., 2014):

$$
\frac{1}{T_{eff_load}}=\frac{\beta_{2bound}}{T_{unload}}
$$

where $T_{eff_load}$ represents the loading rate, $\beta_{2bound}$ represents the number of copies of β clamp at the fork and $T_{unload}$ represents the bound-time of a β clamp. In our estimations we assume that there are 23 β dimers per fork as previously estimated (Moolman et al., 2014).

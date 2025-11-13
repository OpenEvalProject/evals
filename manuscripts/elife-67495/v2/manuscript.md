# Two different cell-cycle processes determine the timing of cell division in Escherichia coli

## Authors

- Alexandra Colin<sup>1</sup> ([ORCID: 0000-0002-9144-3282](https://orcid.org/0000-0002-9144-3282))
- Gabriele Micali<sup>2</sup>
- Louis Faure<sup>1</sup> ([ORCID: 0000-0003-4621-586X](https://orcid.org/0000-0003-4621-586X))
- Marco Cosentino Lagomarsino<sup>4</sup> ([ORCID: 0000-0003-0235-0445](https://orcid.org/0000-0003-0235-0445)) †
- Sven van Teeffelen<sup>1</sup> ([ORCID: 0000-0002-0877-1294](https://orcid.org/0000-0002-0877-1294)) †

### Affiliations

1. Microbial Morphogenesis and Growth Laboratory, Institut Pasteur Paris France
2. Department of Environmental Microbiology Dübendorf Switzerland
3. Department of Environmental Systems Science, ETH Zürich Zürich Switzerland
4. IFOM, FIRC Institute of Molecular Oncology Milan Italy
5. Physics Department, University of Milan, and INFN Milan Italy
6. Département de Microbiologie, Infectiologie et Immunologie, Université de Montréal Montréal Canada

† Corresponding author

## Abstract

Cells must control the cell cycle to ensure that key processes are brought to completion. In Escherichia coli, it is controversial whether cell division is tied to chromosome replication or to a replication-independent inter-division process. A recent model suggests instead that both processes may limit cell division with comparable odds in single cells. Here, we tested this possibility experimentally by monitoring single-cell division and replication over multiple generations at slow growth. We then perturbed cell width, causing an increase of the time between replication termination and division. As a consequence, replication became decreasingly limiting for cell division, while correlations between birth and division and between subsequent replication-initiation events were maintained. Our experiments support the hypothesis that both chromosome replication and a replication-independent inter-division process can limit cell division: the two processes have balanced contributions in non-perturbed cells, while our width perturbations increase the odds of the replication-independent process being limiting.

## Introduction

Temporal regulation of cell division is essential for cellular proliferation in all organisms. Timing of cell division determines average cell size in a population of growing cells and guarantees that every daughter cell receives one complete copy of chromosomal DNA. Despite its importance, the process remains not understood even in the best-studied model system Escherichia coli.

Three conceptually different classes of models have been proposed to explain division control in E. coli (Figure 1B and C).

![Figure 1.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig1-v2.jpg)

**Figure 1.:** (A) Cartoon of the cell cycle and definition of C, D and I periods. The C period is the time between initiation and termination of chromosome replication, the D period is the time between replication termination and division, and the I period is the time between subsequent initiations. (B) Models of cell-division control based on a single limiting process. According to the first set of models cell division is controlled by DNA replication and subsequent segregation (Witz et al., 2019; Ho and Amir, 2015; Sompayrac and Maaloe, 1973). According to the second set of models, cell division is controlled by a chromosome-independent inter-division process between birth and division (Si et al., 2017; Si et al., 2019; Harris and Theriot, 2016; Harris and Theriot, 2018). (C) Scheme of the concurrent-processes model. According to this model, the time of cell division is set by the slowest of two process, an inter-division process and chromosome replication/segregation. When both processes are completed, the cell can go through division (analogous to an AND gate).

According to the first class of models, DNA replication and segregation are regarded as limiting for cell division, while division has no influence on replication. At the single-cell level, different couplings between DNA replication and cell division have been suggested: a 'constant' (size-uncoupled) duration since the time of DNA replication initiation (C+D period in Figure 1A; Ho and Amir, 2015; Wallden et al., 2016), or the addition of a 'constant' (size-uncoupled) size between replication initiation and division (Witz et al., 2019).

A second class of models suggests that DNA replication has no direct influence on the timing of cell division under unperturbed growth conditions (Harris and Theriot, 2016; Harris and Theriot, 2018; Si et al., 2019; Ojkic et al., 2019; Zheng et al., 2020; Ghusinga et al., 2016; Figure 1B). Instead, a different, chromosome-independent process, the accumulation of a molecule or protein, is thought to trigger cell division, once copy number reaches a threshold. Evidence comes from the observation that the size added by cells between birth and division is independent of their size at birth (Campos et al., 2014; Taheri-Araghi et al., 2015; Amir, 2014). Further evidence comes from experiments that demonstrate the independence of this 'adder' behavior from perturbations of DNA replication (Si et al., 2019). Different 'accumulator' molecules have been suggested – notably cell-wall precursor molecules (Harris and Theriot, 2016), components of the divisome or septum (Zheng et al., 2020), or, more specifically, FtsZ proteins (Si et al., 2019; Ojkic et al., 2019; Serbanescu et al., 2020). However, whether cells effectively measure a constant size increase, whether the adder behavior emerges through the accumulation of a single molecule, and/or whether chromosome replication/segregation have a direct influence on cell division remains controversial (Witz et al., 2019; Si et al., 2019; Zheng et al., 2020).

A third model developed by some of us proposes that two processes limit cell division, DNA replication/segregation and a second 'inter-division' process that relates cell size at division to cell size at birth, independently of DNA replication or segregation (Micali et al., 2018b; Figure 1C). The inter-division process could be the accumulation of a molecule produced since birth, as summarized above. According to this 'concurrent-cycles' model, the slowest process sets the timing of cell division at the single-cell level. Based on recent experimental evidence (Si et al., 2019; Witz et al., 2019), DNA-replication initiation is controlled through an adder-like process between subsequent initiation events, which could also stem from a molecule accumulating during replication events (Ho and Amir, 2015; Sompayrac and Maaloe, 1973).

Micali et al. showed that single-cycle models proposed (Wallden et al., 2016; Ho and Amir, 2015; Harris and Theriot, 2016) fail to explain experimental data on the B and C+D subperiods in single cells, while the concurrent-cycles model is able to fit the previously available experimental datasets (Micali et al., 2018b). However, the model makes assumptions about the nature of the underlying processes and has more fit parameters than any of the more simple previous models. In this situation, relevant perturbations could help us validate competing scenarios that are not simple to discern from single cells growing and dividing in standard conditions.

To test single- vs concurrent-processes models of division control, we aimed to force one of the two potentially limiting processes, the replication-independent inter-division process, to be more likely limiting for division control. Zheng et al., 2016 showed that increasing cell width through titration of the MreB-actin cytoskeleton causes an increase of the period between replication termination and cell division (D period) without affecting the average duration of DNA replication (C period) or cell-cycle duration (see also Si et al., 2017). We hypothesized, that an increased D period might correspond to a decreasingly limiting role of DNA replication and an increasingly limiting role of the inter-division process for cell division.

Similar to Zheng et al., 2016, we thus systematically increased cell width through perturbations of the MreB actin cytoskeleton. We then followed single-cell division and DNA replication in microfluidic devices during steady-state growth conditions in minimal media, similar to previous work (Wallden et al., 2016; Si et al., 2019; Witz et al., 2019).

Indeed, upon increasing D period, cell size at division showed continuously decreasing correlations with cell size at initiation of DNA replication. Without any modeling, these findings already suggest that cell division is controlled by a process different from DNA replication but dependent on cell size at birth. On the contrary, in non-perturbed cells, DNA replication appears to have an important limiting role, as supported by the high correlations between division size and size at replication initiation also observed previously (Witz et al., 2019). By testing two recently proposed single-process models (Si et al., 2019; Witz et al., 2019) and the concurrent-process model from Micali et al., we found that only the concurrent-process model is able to describe the experimental data in both perturbed and unperturbed conditions.

In summary, our work suggests that cell division is controlled by at least two concurrent processes that link cell division to DNA replication and cell birth, respectively.

## Results

### Tracking DNA replication during steady-state growth in microfluidic channels

To investigate division control in the model organism E. coli, we measured cell division and DNA replication at the single-cell level using a modified wildtype strain (NCM3722, λ::P127-mcherry, dnaN::Ypet-dnaN), which contains a cytoplasmic mCherry marker for accurate measurements of cell dimensions and a functional fluorescent-protein fusion to the beta-clamp of the DNA-replication machinery (YPet-DnaN), introduced at the native dnaN locus (Reyes-Lamothe et al., 2010). The YPet-DnaN fusion forms foci at the replication fork during DNA replication but is diffuse otherwise (Figure 2A; Reyes-Lamothe et al., 2010; Moolman et al., 2014). To investigate cells during exponential, steady-state growth conditions, we grew cells in microfluidic devices commonly referred to as ’mother machines’ (Figure 2A, Figure 2—video 1), similar to previous experiments (Wang et al., 2010; Long et al., 2013; Long et al., 2014; Si et al., 2019; Witz et al., 2019). To reliably distinguish subsequent rounds of DNA replication, we grew cells in minimal medium (M9+NH4Cl+glycerol), such that subsequent replication rounds do not overlap.

![Figure 2.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig2-v2.jpg)

**Figure 2.:** (A) Top: Snapshots of a single mother-machine channel. Interval between images is 12 min. Red: cytoplasmic mCherry, yellow: YPet-DnaN. The contours show a cell growing for two consecutive cell cycles. Bottom: Cell length (gray line), the position of YPet-DnaN foci along the long axis of the cell (black dots), initiation and termination times (red and yellow dashed lines, respectively) in the same cells shown in A. Scale bar: 2 μm. (B) Top: Snapshots of E. coli S233 (NCM3722, λ::P-mcherry, dnaN::Ypet-dnaN) treated with sublethal amounts of A22 (concentrations in μg.mL-1). Scale bar: 2 μm. Bottom: Effect of A22 treatment on average dimensions of cells grown in liquid or in mother machine for at least 6 hr of exponential growth. For cell-to-cell variations see Figure (C) Duration of inter-division time, I, C, and D periods as a function of average cell width measured in mother machines. Blue and gray squares represent unperturbed conditions and A22-treatment, respectively. Each symbol represents an independent biological replicate. (D) Conditional probability density of the occurrence of YPet-DnaN foci $p⁢(y|t)$ as a function of cell length (y-axis) for different time points before subsequent cell division (x-axis) for different A22 concentrations as indicated on top of the maps. Maps are duplicated for better visualization of the replication process. Vertical lines indicate the beginning and end of the probability peaks that correspond to replication initiation and termination, respectively. Note that these times do not strictly agree with average replication/termination times.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Conditional probability density of the occurrence of YPet-DnaN foci as a function of cell length ($y$-axis) $p⁢(y|t)⁢d⁢y$ as a function of time before subsequent cell division ($x$-axis) for untreated cells. Red and yellow squares represent the windows in which we are looking for initiation and termination respectively. (B, C) The DNA replication cycle can be detected based on the number of spots detected inside the cell, or, as chosen for this paper, based on the intensity distribution of the YPet-DnaN signal (see Materials and methods for details).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Coefficient of variation of cell width as a function of mean cell with obtained at different A22 concentrations. Squares and triangles represent measurements performed on cells grown in mother machine or in liquid culture, respectively. Blue color represent wild-type cells. Gray color represent cells treated with different A22 concentrations.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Effect of A22 treatment on growth rate measured in liquid culture and in mother machine. (B) Example of growth curves obtained in liquid culture. The star indicates the time at which the snapshots (Figure 2A) were taken. Dashed lines represent exponential fits. (C) Growth rate (left column) and doubling time (right column) remains approximately constant over time in the mother-machine experiments upon treatment with different A22 concentrations (with $<15%$ variations during the observation window).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Coefficient of variation of growth rate as a function of average growth rate. (B) Cell-to-cell variations (coefficient of variation) of inter-division time, I, C, and D period do not increase with increasing average cell width. Each point represents one biological replicate generated in mother machine.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Mean initiation volume is computed from individual lengths and mean width at the time of replication initiation, assuming spherocylindrical cells.

We segmented single cells using the Oufti cell-segmentation tool (Paintdakhi et al., 2016) and constructed cell lineages using the Schnitzcells package (Young et al., 2012). We then used the YPet-DnaN signal to measure periods of DNA replication (Figure 2—figure supplement 1). In unperturbed cells, we found an average C period of $51\pm1$ min and a D period of $22\pm4$ min (Supplementary file 1), in agreement with previous bulk measurements (Michelsen et al., 2003). Since DnaN stays bound to DNA for about 5 min after replication termination (Moolman et al., 2014), we likely overestimate the average C period and underestimate the D period by this amount. However, this absolute change of period durations does not affect our investigations of cell-cycle regulation, which are based on the combined C+D period.

### A systematic increase of cell width through the MreB-polymerization inhibitor A22 causes an increased D period

The concurrent-cycles model (Micali et al., 2018b) suggests that DNA replication and a replication-independent inter-division process are equally likely to limit the timing of cell division under unperturbed conditions. To test the model, and more generally the presence of two concurrent cycles, we aimed to make one of the two processes more limiting. Specifically, we speculated that the inter-division process might become the sole limiting process if the average duration between replication termination and division (D period) could be increased. Based on previous work by Zheng et al., 2016, we therefore systematically increased cell width by perturbing the MreB-actin cytoskeleton (Figure 2B). Instead of titrating MreB levels (Zheng et al., 2016), we treated cells with sub-inhibitory concentrations of the MreB-polymerization inhibitor A22 (Bean et al., 2009), similar to previous studies (Tropini et al., 2014).

Increasing A22 concentration leads to increasing steady-state cell width both in batch culture and in the mother machine (Figure 2B), without affecting cell-to-cell width fluctuations (Figure 2—figure supplement 2), and without affecting doubling time (Figure 2C) or single-cell growth rate (Figure 2—figure supplement 3). Furthermore, growth-rate fluctuations remain constant (Figure 2—figure supplement 4A) and similar to previous measurements (Kennard et al., 2016; Grilli et al., 2018).

In line with the results of Zheng et al., 2016, the increase of cell width leads to an increase in the average D period (Figure 2C) as hypothesized. At the same time, the average C period (Figure 2C) and the average cell volume at the time of replication initiation remain unperturbed (Figure 2—figure supplement 5), as previously reported (Zheng et al., 2016). Cell-to-cell fluctuations in the duration of sub-periods remain constant (I, C, and interdivision periods) or decrease mildly (D period) (Figure 2—figure supplement 4B). While sub-periods are extracted from single-cell lineages, the shift of replication to earlier times is also observed in the probability distributions of replicase positions (Figure 2D), where periods of both early and late replication appear as marked foci. Vertical lines that indicate the beginning or end of peaks in Figure 2D are guides to the eye and should not be interpreted as average times of initiation or termination.

### Increasing D period through A22 leads to decreasing correlations between DNA replication and cell division

In view of the previously suggested concurrent-cycles model (Micali et al., 2018b), we speculated that DNA replication might not be limiting for cell division if the D period was increased, while a replication-independent inter-division process might become the sole limiting process for cell division. Alternatively, as previously suggested (Zheng et al., 2016), replication could still be the limiting process determining the timing of cell division, for example through a width-dependent added size between replication initiation and subsequent cell division (Witz et al., 2019).

The coupling between cell size and cell growth over different cell-cycle subperiods can be quantified in different ways (Jun and Taheri-Araghi, 2015; Osella et al., 2017; Cadart et al., 2019). For convenience, and following Jun and Taheri-Araghi, 2015; Micali et al., 2018b; Si et al., 2019; Ho and Amir, 2015, we quantified behavior during different sub-periods using ’adder plots’, which display the added size during the period versus the initial size, both normalized by their means (see Materials and methods for a discussion of the use of length instead of volume as a proxy for size). We refer to the slope of these plots as 'coupling constants' $ζ_{X}$, where $X$ denotes the respective sub-period. A coupling constant of 0 corresponds to adder behavior. A coupling constant of 1 corresponds to a 'timer' process, that is a process that runs for a constant duration on average, independently of cell size at the beginning of the period, and a coupling constant of -1 corresponds to a process where the final size is independent of the size at the beginning of the period (see Materials and methods).

First, we measured the added size between birth and division. In agreement with previous results (Campos et al., 2014; Taheri-Araghi et al., 2015), untreated cells showed 'adder behavior', that is, the added size between birth and division is independent of birth size L0, with a coupling constant (or slope) of $ζ_{G}=-0.046\pm0.085$ (Figure 3A). Here, the uncertainty denotes the standard deviation between biological replicates (Supplementary file 1). With increasing D period duration (through increasing A22 concentration), cells continued to show near-adder behavior with a weak trend towards sizer behavior (Figure 3B). For single-cell point clouds of intermediate A22 concentrations see Figure 3—figure supplement 1. Similarly, cells also show adder behavior between subsequent rounds of replication initiation (Figure 3C). More specifically, cells add a constant size per origin of replication between subsequent rounds of initiation, independently of initial initiation size ($ζ_{I}=-0.013\pm0.098$). This behavior is robust with respect to variations of average growth rate using a poorer growth medium (Figure 3—figure supplement 3). For unperturbed cells, this behavior was previously proposed theoretically (Ho and Amir, 2015; Sompayrac and Maaloe, 1973) and demonstrated experimentally (Si et al., 2019; Witz et al., 2019). Ho and Amir, 2015 previously demonstrated that the average size per origin and average added size per origin are equal to one another during steady-state growth. The scaling of average cell size at initiation with the number of replication origins initially deduced by Donachie, 1968 and later confirmed for different growth rates (Wallden et al., 2016) and for different cell widths (Zheng et al., 2020) is therefore also a strong motivation to consider the added size per origin (rather than the non-normalized added size) in our and previous single-cell studies (Si et al., 2019; Witz et al., 2019).

![Figure 3.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig3-v2.jpg)

**Figure 3.:** (A,C,E) Added size between birth and division (A), between subsequent events of replication initiation (C), and during the C+D period (E), for untreated cells (left) and cells treated with 1 μg.mL-1 A22 (right). Points represent single cells. Dashed lines represent robust linear fits. All lengths are indicated in units of μm. (B,D,F) Slopes of the added sizes corresponding to A, C, E, respectively, as a function of the D period as obtained through sub-lethal A22 treatment (0–1 μg.mL-1). A slope of 0 represents adder behavior, while a slope of -1 represents independence on the size at the beginning of the sub-period (sizer behavior). Blue and gray squares represent unperturbed conditions and A22-treatment, respectively. Each symbol represents an independent biological replicate. (G,H) Division size $L_{d}$ as a function of initiation size per ori $L_{B}/n_{Ori}$ (G) and corresponding slopes (H) in analogy to panels A, B, respectively. The decreasing slope in H demonstrates decreasing dependency of division on DNA replication.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The slopes $ζ_{G}$, $ζ_{I}$, and $ζ_{CD}$ for different A22 concentrations are obtained from robust fits (black lines). Each cloud represents one of three biological replicates.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Points are color-coded according to whether initiation happened in the mother (blue) or in the mother (black), respectively. Dashed lines represent the slopes of each cloud according to linear regression.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) Lengths and widths obtained for cells grown in two different growth media: M9 Glycerol NH4Cl (blue squares) or M9 Glycerol Proline (red squares). Symbols represent independent biological replicates. (B) Duration of inter-division time, I period, C period, and D period as a function of average growth rate measured in mother machines. (C, D, E) Left: Example of division, inter-initiation and C+D adder plots for cells grown at slower growth rate (M9 Proline Gycerol). Right: Slope of division, inter-initiation and C+D adder as a function of average growth rate for cells grown in the two different growth media (M9 Proline Glycerol and M9 NH4Cl Glycerol).

We found that $ζ_{I}$ is constant, independently of A22 treatment (Figure 3D). Together with the constancy of the average initiation volume (Figure 2—figure supplement 5, Ho and Amir, 2015; Si et al., 2017; Zheng et al., 2016) this suggests that the process of replication initiation is not affected by the A22-induced cell widening.

In contrast to the weak dependency of $ζ_{G}$ and $ζ_{I}$ on drug treatment, correlations between initiation size and corresponding cell division systematically change as a function of average D period (Figure 3G–H). While unperturbed cells effectively show adder behavior ($ζ_{CD}=-0.10\pm0.11$, Figure 3E), in agreement with the analysis of previous experimental data (Micali et al., 2018b; Witz et al., 2019), $ζ_{CD}$ continuously changes toward a value of -1 with increasing average D period (Figure 3F). Note that the negative value of $ζ_{CD}$ corresponds to a lack of correlation between division size and size at initiation (Figure 3G), typically predicted by the models where replication is never limiting for cell division Micali et al., 2018b; Si et al., 2019. This lack of correlations can also be illustrated differently: Division size is decreasingly dependent of the size at initiation with increasing D period (Figure 3H).

With increasing average D period, replication is increasingly likely to happen in the mother cell (Figure 2D). To test whether this behavior might be responsible for a change of the slopes of the point clouds observed in Figure 3E–F, we separated the single-cell measurements of untreated cells or cells treated with a low A22 concentration (0.25 µg/ml) into separate clouds, depending on whether initiation happened in the mother or in the daughter cell, respectively (Figure 3—figure supplement 2). We did not observe a separation of point clouds nor differences between their slopes, suggesting that the spread of the C period over a division event does not affect correlations between initiation and division or between subsequent initiation events.

From these observations, we conclude that with increasing average D period a process different from DNA replication is likely increasingly responsible for division control.

### A replication-independent adder-like process is increasingly likely the bottleneck process for cell division

As described in the introduction, a range of different single-process models were proposed in the past to explain correlations between DNA replication and cell division (Si et al., 2019; Harris and Theriot, 2016; Witz et al., 2019; Wallden et al., 2016; Ho and Amir, 2015). Some of us recently argued that existing single-process models are incapable to reconcile correlations observed in previous experimental datasets (Micali et al., 2018b), which led us to propose the concurrent cycle scheme illustrated in Figure 4A. The model assumes two processes that must both finish for cell division to occur, one replication/segregation process related to the size at replication initiation and one inter-division process related to the size at birth. The model contains three control parameters: $ζ_{CD^{′}}$ controls the replication/segregation process and $ζ_{H}$ controls the inter-division process. A third parameter, $ζ_{I}$ controls the inter-initiation process that relates replication initiation to the cell size at the previous initiation. The slopes of the inter-division period ($ζ_{G}$) and of the C+D period ($ζ_{CD}$) emerge from the competition of the two cycles and are predictions of the model.

![Figure 4.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig4-v2.jpg)

**Figure 4.:** (A) Cartoon: Two independent inter-division and timer-like replication/segregation must be completed before division occurs. The inter-division process is assumed to exhibit adder-like behavior with control parameter $ζ_{H}=0$, while the replication/segregation is a timer (see Materials and methods for details on the estimation). The adder-like inter-initiation processes with control parameter $ζ_{I}=0$ determines size at initiation. (B) Model-fitting to experimental data reveals the probability $p_{H}$ of the inter-division process to control cell division as a function of increasing D period (with increasing A22 concentration), assuming constant control parameters $ζ_{H}=0$ and $ζ_{I}=0$. (C) Slopes of adder plots $ζ_{G}$ as a function $ζ_{CD}$. Blue diamond: prediction in Si et al., 2019. Dotted lines: Prediction of pure adder models. Green: Prediction from a general class of single-process chromosome-limited models ('ICD' models, see Supplementary Notes) (Micali et al., 2018b), where cells divide after completion of the replication/segregation process with variable $ζ_{CD}$. Purple: Prediction of the concurrent cycles model. Shaded areas represent the ranges of predictions using the maximum and minimum experimentally measured input parameters (ratio of variance of size at initiation over size at birth; ratio of mean size at division over size at birth). (B, C) Blue and gray squares represent unperturbed conditions and A22-treatment, respectively. Each symbol represents an independent biological replicate.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Predictions of the concurrent cycles model if $ζ_{H}$ is left as a free parameter.(A, B) Probability for the cell division process to be limiting ($p_{H}$) (A) and strength of the inter-division control parameter ($ζ_{H}$) (B) for experimental data generated in this study (red circles and grey squares for untreated cells and cells treated with A22). Both $p_{H}$ and $ζ_{H}$ are allowed to vary and the values are estimated solving Equation (S20) for $p_{H}$ and $ζ_{H}$. The linear fit for the different results is shown as red dashed line. (C) $ζ_{G}$ (division adder slope) as a function of $ζ_{CD}$ (C+D adder slope) for data generated in this study (gray circles). Prediction of the replication-independent model by Si et al., 2019 (blue diamond), and of ICD model (green area). Two predictions of the concurrent cycles model are also plotted: light purple: prediction of concurrent cycles model assuming $ζ_{H}=0$ (see Figure 4). Dark purple: prediction of concurrent cycles model leaving $ζ_{H}$ as a free parameter of the fit (see (A,B)). The shaded areas represent the range of predictions using the maximum and minimum of experimentally measured ratio of variance of size at initiation over size at birth (both for ICD and concurrent cycles) and of the experimentally measured ratio of mean size at division over size at birth (concurrent cycles). The maximum and minimum values are taken over the experimental data reported in this picture, that is treated and untreated data acquired for this work.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Witz and coworkers (Witz et al., 2019) proposed an ICD model (see methods) with an adder between consecutive initiations ($ζ_{I}=0$) and in the C+D period ($ζ_{C⁢D}=0$), and asymmetric division, which we tested with our data. (A) The level of asymmetry at birth from our data is about 5%. The asymmetry is computed as $|\frac{(L_{0}^{c⁢e⁢l⁢l⁢1}-L_{0}^{c⁢e⁢l⁢l⁢2})}{(L_{0}^{c⁢e⁢l⁢l⁢1}+L_{0}^{c⁢e⁢l⁢l⁢2})}|$ (where cell 1 and cell 2 are two daughter cells) and averaged for each dataset. (B) Simulations of the Witz et al. 'double adder' ICD model as a function of the asymmetry in division (α). (Parameter set as in untreated conditions: $⟨\mu⟩=0.0088⁢min^{-1}$, $\sigma_{\mu}=0.001⁢min^{-1}$, $⟨Δ_{I}⟩=0.875⁢um^{3}$, $\sigma_{Δ_{I}}=0.19⁢\mu⁢m^{3}$, $⟨Δ_{C⁢D}⟩=1.39⁢um^{3}$, $\sigma_{Δ_{C⁢D}}=0.16⁢um^{3}$). For increasing asymmetry, the model recapitulates the near-adder behavior between divisions ($ζ_{G}≃0$). (C) $ζ_{G}$ (division adder slope) as a function of the C+D adder slope $ζ_{CD}$ for simulations at $\alpha=0$ (bright yellow diamond), $\alpha=0.05$ (bright yellow), and $\alpha=0.1$ (dark yellow diamond). In our own experimental study find the division asymmetry to be about 5% ($\alpha=0.05$), consistent with previous reports . Blue diamond: prediction from the Si et al. model. Green shaded area: Prediction of the ICD model with no asymmetry in division. Purple shaded area: Prediction of the concurrent cycles model with the hypothesis that $ζ_{H}=0$. The shaded areas represent the range of predictions using the maximum and minimum experimentally measured ratio of variance of size at initiation over size at birth (both for ICD and concurrent cycles models) and the experimentally measured ratio of mean size at division over size at birth (for the concurrent cycles model). The maximum and minimum values are taken over the untreated conditions acquired for this work as well as the published data from Si et al., 2019 and Witz et al., 2019.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Inter-division adder slope ($ζ_{G}$) plotted as a function of inter-initiation slope ($ζ_{I}$). Gray circles: data generated in M9(NH4Cl) Glycerol medium. Gray triangles: data generated in M9(Proline) Glycerol medium (slow growth rate). Green triangle: data generated by Witz et al., 2019. Yellow square: data generated by Si et al., 2019. (B) Division adder slope ($ζ_{G}$) as a function of the C+D adder slope ($ζ_{CD}$). Same symbols as in (A) correspond to the same data. Additionally, we also display predictions from different models as in Figure 4—figure supplement 2. (C) Estimation of $p_{H}$ as a function of doubling time for data generated in this study, Witz et al., 2019 and Si et al., 2019.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (A) The plot shows the slope of the inter-division adder plot $ζ_{G}$ as a function of the slope of the adder plot in the $C+D$ period $ζ_{C⁢D}$ for both the concurrent cycles model (blue and red) and for the ICD model (green), respectively. Theoretical predictions in the small-noise approximation (dashed lines) agree with simulations (symbols). For concurrent cycles, simulation parameters are chosen to maintain noise levels comparable to untreated experimental conditions and to remain on average in the regime of no overlapping rounds (blue diamonds) or a single overlapping round (red circles), while varying $p_{H}$. For ICD (green triangles), $Δ_{C⁢D}$ varies in conditions without overlapping rounds. The ratio $⟨\tau_{C+D}⟩/⟨\tau⟩$ ranges from 0.5 to 1.5. (B, C) The analytical predictions are robust with increasing noise levels. The plots show the difference between the analytical (small-noise) predictions and direct simulations of the size homeostasis parameter ζ (slope of the adder plot) for the inter-division cycle (B) and for the $C+D$ period (C) in the concurrent cycles model, as a function of the maximal relative noise level. Simulation parameters are set to explore the limits of the small noise approximation while maintaining constant $p_{H}$ and $Q_{C⁢D}$. The gray region indicates the regime of noise levels obtained from our experiments. The $Q_{C⁢D}=1.5$ regime correspond to $⟨\tau_{C+D}⟩/⟨\tau⟩≈0.6$ (blue + crosses), $Q_{C⁢D}=2.3$ regime correspond to $⟨\tau_{C+D}⟩/⟨\tau⟩≈1.2$ (red x crosses).

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/67495/elife-67495-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** (A) Comparison of inter-initation adder slope ($ζ_{I}$) calculated in two different ways, either by assuming symmetric cell division ($y$-axis, obtained from $L_{B}^{cell}/n_{cell}-L_{B}^{mother}/n_{mother}$, where $n_{X}$ is the number of origins at the time of replication initiation in the mother or cell), or by taking asymmetry into account ($x$-axis, obtained through correction as indicated in Materials and methods). (B) $ζ_{I}$ as a function of the average D period, assuming symmetric division. C:$ζ_{I}^{asym}$ as a function of the average D period, correcting for asymmetric division. (D-E) Comparison of the adder slopes during the C+D period generated while ignoring or considering division asymmetry. Panels are analogous to panels (A–C). Circles (red) and squares (gray) represent unperturbed conditions and A22-treatment, respectively. Each symbol represents an independent biological replicate.

To fit the concurrent-cycles model to our experimental data, we set the inter-initiation process to be an adder ($ζ_{I}=0$), based on our experimental results (Figure 3C), in agreement with previous observations in unperturbed cells (Si et al., 2019; Witz et al., 2019). Furthermore, we assumed that replication segregation (the C+D’ perid) is a timer process ($ζ_{CD^{′}}=1$) that requires a minimum time to be completed, which is independent of size at the time of initiation, and does not vary in A22 perturbations. Note that neither the minimum completion time C+D’ nor the coupling parameter $ζ_{CD^{′}}$ can be measured experimentally, or bypassed in the model. In principle these parameters could change under A22 perturbations, since MreB affects the activity of topoisomerase IV (Madabhushi and Marians, 2009; Kruse et al., 2003), an enzyme that mediates the dimerization of sister chromosomes. However, constancy of $ζ_{C⁢D^{′}}$ is supported by the constancy of the C period, and the minimum D’ period cannot increase too strongly with width in the model, because otherwise it would render replication/segregation limiting for division under A22 perturbations, contrary to our experimental observation. Hence, for simplicity, we assumed $ζ_{C⁢D^{′}}$ and the D’ period to stay constant. For the inter-division process we assumed that $ζ_{H}=0$ (adder). This assumption is supported by previous experiments in filamentous cells, transiently inhibited for division (Wehrens et al., 2018). Those cells divide following a cell-cycle adder and therefore divide much more frequently than non-filamentous cells, likely because DNA replication is never limiting. The adder hypothesis is also compatible with the accumulation models of FtsZ or other divisome/septum components for this sub-period, as recently hypothesized Si et al., 2019; Zheng et al., 2020; Ojkic et al., 2019.

Compared to a single-process model, this framework outputs the extra parameter $p_{H}$, which quantifies the probability that the inter-division process is limiting. Figure 4B shows how by fitting the model to our data, increasing D period duration leads to an increase of $p_{H}$. The model therefore predicts that the two independent processes, DNA replication and a replication-independent inter-division process, are almost equally likely to limit cell division under unperturbed conditions (Micali et al., 2018b). However, with increasing average D period through perturbation by A22, the replication-independent inter-division process is increasingly likely limiting for cell division.

In a generalized framework, we also allowed the inter-division control parameter $ζ_{H}$ to vary, fitting $ζ_{H}$ and $p_{H}$ simultaneously, at the cost of an extra parameter. We found that $ζ_{H}$ decreases mildly from an adder-like behavior toward a sizer with increasing average D period (Figure 4—figure supplement 1B). $p_{H}$ increases with the D period regardless of the fitting strategy (Figure 4—figure supplement 1A).

Two recent studies have proposed single-process models based on new experimental data: First, a chromosome-limited model that links replication and subsequent division through an adder process (Witz et al., 2019), which is the best-fitting model of a whole class of models where replication is limiting and initiation is set by an adder ('ICD' models, see Supplementary Notes) and second, a chromosome-agnostic model that considers replication and division processes as independent of one another (Si et al., 2019). We therefore tested the performance of both of these models on our experimental data of unperturbed cells, by jointly comparing the predicted couplings of the inter-division period and the C+D period. We found that both frameworks appear to be incompatible with our data (Figure 4C).

We also verified that the concurrent-cycles scenario generally shows better agreement with recently published data (Si et al., 2019; Witz et al., 2019) than single-process models (Figure 4—figure supplement 3). Interestingly, when fitting our model to all datasets including our own, we found that $p_{H}≈0.5$ at slow growth (if the average doubling time is smaller than 1.4 hr), while $p_{H}$ increases with decreasing doubling time. This trend is in qualitative agreement with recent work from Tiruvadi-Krishnan et al., 2021, who propose that DNA replication limits division at slow growth but not at fast growth (see also Discussion). However, we note that part of this increase might also be caused by decreasing accuracy of detecting replication initiation during overlapping rounds of replication, which would artificially decrease correlations between replication and division.

Witz et al., 2019 argued that their single-process model could reconcile adder behavior based on asymmetric cell division (see also their recent comment in Julou et al., 2020). For simplicity and analytical tractability, we did not include asymmetric division in the general models shown in Figure 4C, but we analyzed its role separately in Figure 4—figure supplement 2. We also observed that in the model proposed by Witz et al., 2019, asymmetric division drives the inter-division control $ζ_{G}$ toward an adder-like process, reaching adder behavior for division asymmetries that are similar to experimentally observed values (Figure 4—figure supplement 2). However, this model does not allow $ζ_{C⁢D}$ to deviate from an adder, thus resulting in a poor agreement upon perturbation of cell width (Figure 4—figure supplement 5).

The predictions of Figure 4C rely on analytical calculations performed in the limit of small noise. To verify that the levels of cell-to-cell variability would not affect the results, we tested the predictions of our model with simulations at the experimentally observed levels of noise, and as a function of noise levels. Figure 4—figure supplement 4 shows by direct model simulation that the predictions are robust.

## Discussion

In conclusion, our study suggests that cells control the timing of cell division based on at least two processes in slow-growth conditions: genome replication/segregation and an inter-division process, which relates cell division to size at birth. Accordingly, experimental data obtained in this study and in previous studies are well described by the concurrent-cycles model, while the available single-process models fail to describe our experimental data in unperturbed and perturbed conditions.

Our conclusions are based on the following observations: First, cell size at division and cell size at initiation of DNA replication are correlated in unperturbed cells ($ζ_{CD}=0$, Figure 3), as already observed previously (Micali et al., 2018b; Witz et al., 2019). Thus, division and replication cannot proceed fully independently of one another, as previously suggested (Si et al., 2019). But why can DNA replication alone not account for division control as suggested by Witz et al., 2019, in form of an adder between replication initiation and division? When increasing cell width and the average D period with A22, we observed decreasing correlations between DNA replication and division (a decrease of $ζ_{CD}$ towards -1) (Figure 3), which suggests that division becomes decreasingly dependent of replication. At the same time, two other key cell-cycle couplings remained nearly unchanged ($ζ_{G}≈0$, $ζ_{I}≈0$). Our data are in line with the idea that a replication-independent process related to size at birth contributes to division control, and that this process is dominant upon width perturbations. Thus, cell division is apparently affected by both cell size at birth and DNA replication.

What is the process that links cell division to size at birth? The concurrent-cycles model suggests that the inter-division process is an adder-like process ($ζ_{H}≈0$), which shows a mild trend toward sizer with increasing perturbation. The adder-like nature of this process is also supported by experiments with dividing filamentous cells, where DNA replication is likely never limiting cell division (Wehrens et al., 2018). Recently, multiple studies suggested that cells divide independently of DNA replication, based on a licensing molecule that accumulates since birth and reaches a critical threshold in copy number at the time of cell septation or division (Si et al., 2019; Zheng et al., 2020; Ojkic et al., 2019; Harris and Theriot, 2016; Panlilio et al., 2021). The licensing molecules were suggested to be cell-wall precursor molecules (Harris and Theriot, 2016), FtsZ or other division-ring components (Si et al., 2019; Ojkic et al., 2019; Serbanescu et al., 2020), or other unknown molecules (Zheng et al., 2020). The peptidoglycan accumulation model is based on the assumption that peptidoglycan accumulates in proportion to cell volume, while cell-wall insertion occurs in proportion to cell-surface growth. However, some of us recently demonstrated that cell surface area grows in proportion to biomass (Oldewurtel et al., 2021), which makes it more likely that peptidoglycan synthesis and cell-wall insertion happen at equal rates. FtsZ or a different septum component are possible candidates for the inter-division mechanism. Cell size at z-ring formation correlates with total FtsZ abundance (rather than FtsZ concentration) (Männik et al., 2018). Furthermore, controlled repression or over-expression of FtsZ delay or accelerate subsequent cell division (Si et al., 2019). However, at the same time, the expression of FtsZ is cell-cycle dependent (Männik et al., 2018). Whether the accumulation of FtsZ or other divisome components are responsible for an adder-like inter-division process thus requires further investigation.

Si et al., 2019 recently conducted periodic expression/repression experiments of FtsZ, the mentioned septum component, and DnaA, the major replication-initiation protein, which led them to conclude that replication and division were independent of each other. While their experiments are suggestive of a role of cell size at birth for subsequent cell division, their data do not rule out an additional limiting role of DNA replication for division, which is supported by the adder-like correlations observed between replication initiation and division (Figure 3; Witz et al., 2019).

How is cell division mechanistically coupled to DNA replication? Z-ring formation and DNA segregation are coupled through the processes of nucleoid occlusion, which inhibits Z-ring formation on top of nucleoids, and ter linkage, a process that links the Z-ring to the terminal region of the segregated chromosomes (Dewachter et al., 2018). Another link in slow-growth conditions comes from FtsZ expression: FtsZ-protein expression increases in a step-wise manner during the cell cycle (Männik et al., 2018), and Z-ring formation happens predominantly after the increase of production (Männik et al., 2018). However, which of these or other processes is coupling the timing of replication to division remains to be determined.

Based on the concurrent-cycles model, we predict that inter-division and DNA replication/segregation processes are equally likely limiting cell division ($p_{H}≈0.5$) in two different minimal growth media (Figure 4—figure supplement 3), and we previously reported the same balance (Micali et al., 2018b) for previous experiments at slow growth (Adiciptaningrum et al., 2016; Wallden et al., 2016). However, at fast growth, $p_{H}$ seems to increase, based on fitting our model to data from Si et al., 2019 (Figure 4—figure supplement 3). While it is increasingly challenging to detect the time of initiation accurately in this regime, which could account for part of the increase of $p_{H}$, support of this trend also comes from a recent study by Tiruvadi-Krishnan et al., 2021. They demonstrate that temporal correlations between replication termination and z-ring constriction are high at slow growth, which supports a limiting role of DNA replication for cell division, but correlations decrease at fast growth, which then requires a different process to control cell division, in qualitative agreement with the concurrent-cycles model (Figure 4—figure supplement 3).

The balance between the replication/segregation and inter-division processes at slow growth, over a broad regime of growth rates, is surprising, as it requires that both processes terminate, on average, at the same cell volume $2⟨V_{0}⟩$. Under balanced conditions, average cell size after completion of the inter-division and replication/segregation processes are given by $⟨V_{0}+Δ_{H}⟩≈2⟨Δ_{H}⟩$ and $2⁢Δ_{I}⁢2^{(C+D^{′})/\tau}$ (Ho and Amir, 2015), respectively. With $Δ_{I}$ constant, $Δ_{H}$ must therefore scale in proportion to $2^{[(C+D^{′})/\tau]}≈2^{[(C+D)/\tau]}$.

Zheng et al., 2020 recently re-investigated average cell size and the duration of the C+D period as a function of nutrient-dependent growth rate. While it was previously thought that cell size increases exponentially with growth rate (Schaechter et al., 1958), Zheng et al., 2020 identified a linear relationship. Similarly, they found that the average C+D period shows a Michaelis-Menten-like relationship ($C+D=\mu/(a⁢\mu+b)$) with average growth rate μ. Based on these experimental findings, they suggested an accumulator model (equivalent to our H-process) that could reconcile the growth-rate dependent increase of average cell size, as long as the threshold molecule was produced at a rate proportional to $1/(C+D)$ on average. Recent theoretical work supports this relationship (Serbanescu et al., 2020) based on the assumption of constitutive divisor expression. The same assumption also finds some experimental validation from nutrient-shift data (Panlilio et al., 2021). Constitutive divisor-protein expression could provide an explanation for the maintenance of $p_{H}$ over different unperturbed conditions. However, as soon as only one of the two processes is modulated, for example through width perturbations (Figure 4), their balance is broken.

A qualitatively different behavior at slow growth was recently suggested in the already mentioned work by Tiruvadi-Krishnan et al., 2021. While they do not put forward a complete cell-cycle model, they suggest that a checkpoint temporally close to DNA replication solely limits the timing of z-ring constriction and therefore cell division at slow growth but not at fast growth. In the future, it will thus be interesting to re-investigate the balance between two different processes by implementing a variant of the concurrent-cycles model that considers an ’and’ gate between replication termination and z-ring constriction.

The concurrent-cycles framework assumes that replication initiation is independent of cell division or cell size at birth, based on the robust measurements of adder behavior between subsequent initiations (Figure 3C). However, we note that this is not the only possibility, and DNA replication may not be entirely independent of cell division. A complementary hypothesis (Kleckner et al., 2018) posits a possible (additional or complementary) connection of initiation to the preceding division event. To test this hypothesis, one could perturb specific division processes by titrating components involved in Z-ring assembly (e.g. titrating FtsZ Zheng et al., 2016).

In conclusion, cell-cycle regulation remains to be understood mechanistically. However, from our work it appears that in standard conditions both DNA replication and cell growth since birth play important roles for division timing.

## Materials and methods

**Key resources table**


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
      <td>Strain, strain background (E. coli)</td>
      <td>S233</td>
      <td>This work</td>
      <td>NCM3722, λ::P127-mcherry, dnaN::Ypet-dnaN</td>
      <td>Strain construction</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>A22</td>
      <td>Cayman Chemicals</td>
      <td>22816-60-0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>The MathWorks, Inc.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Oufti</td>
      <td>Paintdakhi et al., 2016</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Schnitzcells</td>
      <td>Young et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Strain construction

All experiments were carried out with E. coli strain S233 (NCM7322, λ::P-mcherry, dnaN::Ypet-dnaN). The strain was obtained by a two-step phage transduction into the K-12 strain NCM3722 (wildtype) (Brown and Jun, 2015; Soupene et al., 2003). First, we introduced mCherry from MG1655(λ::P127-mcherry,int,kan) (Vigouroux et al., 2018) via P1 phage tansduction, then removed integrase and kanamycin-resistance cassette using the pE-FLP system (St-Pierre et al., 2013). The resulting strain was transduced with P1 phages lysate of strain S227 (dnaN::Ypet-dnaN,kan) (Reyes-Lamothe et al., 2010), a kind gift from Rodrigo Reyes-Lamothe. Finally, we removed the kanamycin-resistance cassette using pE-FLP.

### Chemicals

Unless otherwise indicated, all chemicals used in this study were purchased from Sigma-Aldrich. MreB perturbing compound A22 was purchased from Cayman Chemicals and was dissolved in DMSO at a final concentration of 5 mg.mL-1. This solution was made every month and stored in small aliquots not defrosted more than two times. An intermediate solution was freshly prepared for each new experiment in the corresponding growth medium.

### Microfluidic chip fabrication

Cell growth was monitored in a microfluidic device for many generations. The device is an adaptation of the mother machine device (Wang et al., 2010) with the difference that channels are opened at both ends (Long et al., 2013; Long et al., 2014). The design of the device was kindly provided by Pietro Cicuta’s lab. The chips were replicated from epoxy molds by pouring PDMS (Sylgard 184 with 1:10 w/w ratio of curing agent) and by curing it overnight at 60°C. After cutting the chip and punching inlets (with either a 0.75 mm or 1.5 mm biopsy punch in diameter), the chip was cleaned with scotch tape and bonded to a cleaned glass coverslip (#1.5 24x60 mm). Glass coverslips were cleaned by one hour heated sonication in 2% Helmanex soap, rinsing with water, and then one hour heated sonication in 100% ethanol. The slides were kept in 100% ethanol until used and dried with compressed air just before use. For PDMS bonding to the coverslip, coverslips and PDMS chips were plasma cleaned (Plasma System Cute, Femtoscience), and the assembled chips were baked at 60°C for at least one hour.

Before loading cells, the device’s surface was passivated with Pluronic F-127 (P2443, Sigma) at 0.085% final concentration (dissolved in sterile PBS) for 5–30 min at room temperature. The device was then rinsed with growth medium. Loading of the cells was done with no prior centrifugation and with a 5 µm filter attached to the syringe, in order to avoid cells aggregates to clog the channels. All other reagents and media were filtered with a 0.22 µm filter prior to injection in the microfluidic chip. Growth medium flowing in the chip was supplemented with BSA (A9418 Sigma, 10 mg.mL-1 final concentration, dissolved in filtered sterile water).

### Growth media

All microscopy experiments were done in M9 minimal medium (Miller, 1972) supplemented with 1 mM of MgSO4 (Sigma, M2773) and glycerol (0.2%) as carbon source. If not otherwise indicated we used NH4Cl (19 mM) as nitrogen source. Alternatively, for slower growth, we used Proline (Acros, AC157620250) (10 mM). The composition of M9 minimal medium is: Disodium Hydrogenophosphate (Na2HPO4, S7907, Sigma) (42 mM); Potassium Dihydrogen phosphate (KH2PO4, P0662, Sigma) (22 mM); Sodium Chloride (NaCl 31434, Sigma) (8.6 mM).

### Growth conditions

Bacteria were grown at 37°C. For mother machine experiments, a preculture in the selected M9 growth medium was prepared from a single colony on a LB agar plate after streaking from a glycerol freezer stock. After overnight growth, the culture was back-diluted by a factor 1/50 to 1/100 for growth of 1 to 4 hr at 37°C. The culture was then injected into the mother machine device for population of the channels during one hour without flow. Subsequently, flow with M9 medium (supplemented with A22 if indicated) was started using a syringe pump (Harvard Apparatus). A movie was started at least one hour after starting the flow. We made sure that cells were growing at steady state in terms of growth rate/interdivision time/length/width for at least 6 hr. Any of those quantities were not varying more than 15% during the time course of the experiment (see Figure 2—figure supplement 3B for the constancy of growth rate).

For growth rate measurement in liquid culture and snapshots to measure cell dimensions, a preculture was made in the chosen minimal medium from a glycerol stock streak and grown overnight at 37°C, as above. In the morning, the culture was back-diluted to an OD of 0.005 and treatment with A22 was started. Cells were grown for 1–2 hr at 37°C before growth rate measurements were started. Snapshots were taken after 7 hr of A22 treatment.

### Microscopy

Microscopy was performed on an inverted DeltaVision Elite microscope (GE Healthcare) equipped with a 100X oil immersion phase contrast objective (UPlanSApo 100X NA = 1.4, Olympus). We used a laser-based auto-focusing system to maintain focus on the cells throughout the whole course of the experiment. For fluorescence measurements, we used a Fluorescence light source (Lumencor), a multi-band dichroic beamsplitter (DAPI-FITC-mCherry-Cy5), FITC filter (excitation: 475/28, emission: 525/48) and mCherry filter (excitation: 575/25, emission: 625/45). Parameters for excitation were 10% of light intensity for mCherry, with exposure time of 300 ms and 32% of intensity for YPet, with exposure time of 300 ms. Images were acquired through a sCMOS camera (DV Elite, PCO-Edge 5.5) with an effective pixel size of 65 nm was used, with a frame interval of 6 min for cells grown in M9(NH4Cl, Glycerol) medium and 8 min for cells grown in M9(Proline, Glycerol) medium. Imaging was done at 37°C in a controlled chamber. Microfluidic flow was controlled with a syringe pump (Harvard Apparatus).

### Image analysis

Image analysis was based on published or custom Matlab scripts. Cells were segmented using the Oufti package (Paintdakhi et al., 2016). Dimensions of cells grown in liquid culture and imaged on agarose pads were extracted using Oufti. For cells grown in mother machine channels, we considered all channels that contained cells growing for the whole duration of the experiment. As the cells are trapped in channels and their long axis is aligned with the channel direction, we computed cell length as the distance between the two extreme points of the cell contour (obtained with Oufti) along the channel axis. We subsequently reconstructed cell lineages using the Schnitzcells software (Young et al., 2012), and we considered only cells with at least four ancestors for further analysis.

Single-cell growth rate was calculated from an exponential fit to cell length as a function of time. Only cells with positive growth rates and exponential fits with $R^{2}$ above 0.8 were kept for analysis.

For our statistical analysis of replication-division coupling, we considered triplets of cells (a cell associated with its mother and its grandmother). This allowed us to follow two subsequent replication cycles and the corresponding events of cell division (a C+D period after initiation), even if replication initiation started more than one generation time before division.

To obtain average time points of replication initiation and termination, we generated probability-density maps $p⁢(z/L,t-t_{d})$ of finding a DnaN-Ypet spot at a position $z$ along the cell axis (normalized by cell length $L$) at a time $t-t_{d}$ before cell division (Figure 2C). To that end we identified fluorescent spots of Ypet-DnaN: First, a bandpass filter was applied to the YPet fluorescence image (Matlab function bpass with 0.8 px and 20 px for the characteristic length scales of noise and objects, respectively). We then considered all local intensity maxima (Matlab function regionprops) inside cell contours with peak intensity above a manually defined threshold. We then obtained the average time points of initiation/termination as as inflection points along the x-axis in probability density maps (see Figure 2C).

For the detection of DNA-replication initiation and termination in single cells, we did not consider spots but took advantage of the heterogeneous Ypet signal during replication (as illustrated in Figure 2—figure supplement 1). After bandpass filtering of the YPet image, we subtracted the median intensity $I_{med}$ for every pixel and took the sum: $I_{tot}=\sum_{i}(I_{i}-I_{med})$, where $i$ runs over all pixels inside the cell contour. We divided triplets of cells into two mother-daughter pairs. In each pair, we aimed to identify a complete round of replication that is most recently terminated before before the division of the respective daughter cell. Prior to single-cell analysis, limits for initiation frame and termination frame were obtained from the probability density maps (Figure 2C, Figure 2—figure supplement 1). Replication/termination was allowed to happen up to 11 time frames (of 6 or 8 min, depending on growth medium) before or after the average time of replication/termination. In each mother-daughter pair, we then identified regions with $I_{tot}>0$ of a duration of at least 25 min as potential rounds of replication. We then identified the largest region with both initial and final time points within the respective time windows defined above (Figure 2—figure supplement 1). We allowed the D period to be equal to zero if no replication is detected in the two first frames of the two daughter cells. Following this protocol, we identified replication periods in almost all cells (see Supplementary file 1).

### Estimation of adder slopes

To measure the added length per ori between subsequent replication initiation events and between replication initiation and subsequent division, respectively, we first calculated an ori-normalized length $L^{⋆}$. To that end, we divided the length of the mother and grandmother cells by two and four respectively. The added length per ori between initiations is then obtained as $Δ_{I}=L^{⋆}⁢(t_{B}^{cell})-L^{⋆}⁢(t_{B}^{mother})$, irrespectively of whether initiation events happen in cell, mother, or grandmother. Similarly, the added length between replication and subsequent division is obtained as $Δ_{C+D}=L^{⋆}⁢(t_{d}^{cell})-L^{⋆}⁢(t_{B}^{cell})$. Here, we implicitly assumed symmetric cell division, since division asymmetry is small (5%) in all our experiments (Figure 4—figure supplement 2). To test for the influence of division asymmetry on the adder slopes, we corrected the added lengths for the asymmetries of grandmother-mother and mother-cell division events. For example, to correct for the asymmetry in the calculation of the inter-initiation added length, if subsequent initiations happen in mother and daughter cell, we obtain $Δ_{I}^{asym}=Δ_{I}+(1-\alpha)⁢L_{d}^{⋆}$, where $L_{d}^{⋆}$ is the ori-normalized length of the mother cell at division, and where $\alpha=(L_{0}^{sibling}-L_{0})/(L_{0}^{sibling}+L_{0})$ is the division asymmetry between the daughter cell with birth length L0 and its sibling with birth length $L_{0}^{sibling}$. Comparing the simple and the more accurate calculation revealed no significant difference for both I and C+D periods, respectively (Figure 4—figure supplement 2).

Adder slopes were estimated from a robust fit on the cloud of points using iteratively re-weighted least squares (Matlab, robustfit function) to avoid the contribution of occasional outliers. Detailed sample sizes for each experiment are listed in Supplementary file 1.

### The use of length fluctuations as a proxy for size fluctuations

For our statistical analysis of cell-cycle progression (Figure 3), we used single-cell length fluctuations as a proxy for size fluctuations (rather than fluctuations in volume), for the following reasons:

First, it would be most desirably to measure fluctuations in single-cell mass. Whether fluctuations in surface area or volume are better proxies for mass fluctuations remains to be studied in detail. However, in favor of surface area being a potentially better proxy, we recently showed that the ratio of surface area to mass remains constant during the cell cycle while dry-mass density, the ratio between mass and volume, varies systematically with length (Oldewurtel et al., 2021). Cell length, in turn, is directly proportional to surface area $S$ ($S=\piLW$), independently of polar caps or septum formation, while length and volume show a septum-dependent and non-linear relationship.

Second, in our data, both surface-area and volume calculations are subject to substantial measurement noise in width, so that (within conditions) the best available proxy for mass is actually length. Specifically, relative width variations to be about 10% in the mother machine, but physical cell-to-cell variations are likely about 5% – see our measurements on agarose pads in Figure 2—figure supplement 2 and (Oldewurtel et al., 2021). Hence, while absolute uncertainty in width and length measurements are likely very similar, measurement noise in width leads to much higher uncertainty in volume (by about sixfold in our conditions).

Since cell-to-cell fluctuations in width do not increase with increasing drug concentrations (Figure 2—figure supplement 2), we reasoned that the observed decrease of correlations between initiation size and division size (with increasing A22 concentration; Figure 3H) is not a consequence of width fluctuations. We also note that our conclusions on size correlations are based on size fluctuations around their respective means, and thus they are not affected by mean-width changes across conditions.

### Mathematical linear-response formalism for adder coupling constants of cell-cycle subperiods

In this section, we present the mathematical framework used in this work to quantify the size control during different cell-cycle subperiods, and to compare experimental results with predictions from different theoretical models. Specifically, this framework provides us with relationships between the slopes of the different adder plots (Figure 3) that must be met by experimental data to support a given model. Thus, the relationships provide a powerful validation/falsification tool for the different models available.

The original formalism presented in Micali et al., 2018a is based on the so-called ‘size-growth plots’ (Turner et al., 2012; Chandler-Brown et al., 2017; Grilli et al., 2018), whose slope (λ) quantifies the correlation between (logarithmic) size and (logarithmic) multiplicative growth. Here, we adopt an equivalent variant of the formalism based on the slope (ζ) of ‘adder plots’, which relate the added size over a subperiod to initial size (size at the beginning of the subperiod) (Jun and Taheri-Araghi, 2015).

At fast growth, E. coli starts DNA replication already in the mother or grandmother, depending on the C+D period and on the generation time ($⟨\tau_{C+D}⟩>⟨\tau⟩$). Our framework can take into account such situations for single-process models. However, for the concurrent-cycles model our theory is restricted to non-overlapping rounds of replication/segregation (that is $⟨\tau_{C+D}⟩>⟨\tau⟩$). However, we found empirically that the theory also works for overlapping rounds within the range of $⟨\tau_{C+D}⟩/⟨\tau⟩$ values observed in our experiments (Figure 4—figure supplement 4). For all models, analytical predictions only apply to the limit of small noise and for symmetric division. For comparison with data with overlapping rounds, analysis of the role of noise, and of division asymmetry, we used direct numerical simulations of the models (see the figure supplements to Figure 4).

#### Standard linear-response formalism based on the slopes of size-growth plots

We recapitulate here the linear-response formalism used in Micali et al., 2018a, based on size-growth plots (see also Amir, 2014; Grilli et al., 2018). This formalism assumes that a genealogy of single cells, whose cell cycles are indexed by $i$, grow exponentially, $V^{i}⁢(t)=V_{0}^{i}⁢e^{\mu^{i}⁢(t-t_{0})}$, where $V_{0}^{i}$ and t0 are the cell volume and time at birth, respectively. $V^{i}⁢(t)$ is the volume of cell cycle $i$ at time $t$, and $\mu^{i}$ is its growth rate. During a cell cycle, the cell reaches a final size $V_{f}^{i}$ in a period of time $\tau^{i}=t_{f}-t_{0}$ (inter-division time), before dividing symmetrically, $V_{f}^{i}=2⁢V_{0}^{i+1}$.

Since single cells show exponential growth $V_{f}^{i}(t)=V_{0}^{i}e^{\mu^{i}\tau^{i}}$, we decided to expand the logarithmic growth $G_{G}^{i}:=\mu^{i}⁢\tau^{i}$ about its average value ($⟨G_{G}⟩≃log⁡2$) in terms of variations around the logarithmic size at birth $q_{0}^{i}:=log⁡V_{0}^{i}$. In this way, the size of the newborn cells can be written as

$$
2V_{0}^{i+1}=V_{0}^{i}e^{⟨G_{G}⟩−\lambda_{G}\deltaq_{0}^{i}+η_{0}^{i}},
$$

where $\deltaq_{0}^{i}=log⁡V_{0}^{i}−⟨log⁡V_{0}⟩≃log⁡V_{0}^{i}−log⁡⟨V_{0}^{i}⟩$ and $\lambda_{G}$ is the slope of the size-growth plot, which quantifies size homeostasis. Finally, $η_{0}^{i}$ is assumed to be Gaussian noise with mean zero and standard deviation $\sigma_{q_{0}}$. This formalism is described in detail in Amir, 2014; Grilli et al., 2018, and amounts to treating the initial size fluctuations as a linear response problem.

By taking the logarithm of Equation (S1), the variation in logarithmic size of the newborn cell can be expressed as function of the variation of the logarithmic size of the mother cell at birth,

$$
q_{0}^{i+1}+log⁡2=q_{0}^{i}+⟨G_{G}⟩−\lambda_{G}\deltaq_{0}+η_{0}^{i}q_{0}^{i+1}+log⁡2−⟨q_{0}⟩=q_{0}^{i}+⟨G_{G}⟩−\lambda_{G}\deltaq_{0}−⟨q_{0}⟩+η_{0}^{i}\deltaq_{0}^{i+1}+log⁡2=\deltaq_{0}^{i}+⟨G_{G}⟩−\lambda_{G}\deltaq_{0}+η_{0}^{i}\deltaq_{0}^{i+1}=(1−\lambda_{G})\deltaq_{0}^{i}+η_{0}^{i}
$$

Note that $\lambda_{G}=1$ corresponds to a sizer since the fluctuation in logarithmic initial size of cell $i+1$ do not depend on the fluctuations in logarithmic size at birth of cell $i$ ($\delta⁢q_{0}^{i+1}=η_{0}^{i}$). On the other extreme, $\lambda_{G}=0$ corresponds to a timer, in which fluctuation in logarithmic size of cell $i+1$ fully explained by fluctuation in the logarithmic size of the mother cell $i$ ($\delta⁢q_{0}^{i+1}=\delta⁢q_{0}^{i}+η_{0}^{i}$). $\lambda_{G}$ can take any intermediate value with $\lambda_{G}=0.5$ corresponding to an adder. Multiplying both sides of Equation (S2) by the fluctuation in initial logarithmic size $\delta⁢q_{0}^{i}$ and taking the average gives us an expression to directly measure the strength of control as a linear-response from data coefficient (Grilli et al., 2018),

$$
(1−\lambda_{G})=\frac{⟨\deltaq_{0}^{i+1}\deltaq_{0}^{i}⟩}{\sigma_{q_{0}}^{2}} .
$$

The same formalism can be used to estimate the strength of size control over subperiods (notably, the C+D period) and between consecutive initiation events (I period) (Micali et al., 2018a). Hereafter, the quantities $q_{X}^{i}$ refer to the logarithmic volume at cell cycle progression stage $X$ of the cycle $i$. We consider for instance the size-growth coupling during the $C+D$ period in the simple case in which initiation and termination both happen in the cell $i$, and we write the following expressions to relate size fluctuations before and after this subperiod 

$$
q_{0}^{i+1}+log⁡2=q_{B}^{i}+⟨G_{C+D}⟩−\lambda_{C+D}\deltaq_{B}+η_{B}^{i}q_{0}^{i+1}+log⁡2−⟨q_{0}⟩+⟨q_{0}⟩=q_{B}^{i}+⟨G_{C+D}⟩−\lambda_{C+D}\deltaq_{B}−⟨q_{B}⟩+⟨q_{B}⟩+η_{B}^{i}\deltaq_{0}^{i+1}=\deltaq_{B}^{i}−\lambda_{G}\deltaq_{0}+⟨G_{C+D}⟩−log⁡2−⟨q_{0}⟩+⟨q_{B}⟩+η_{B}^{i}\deltaq_{0}^{i+1}=(1−\lambda_{C+D})\deltaq_{B}^{i}+η_{B}^{i},
$$

where the log-size fluctuation at initiation is $\deltaq_{B}^{i}:=q_{B}^{i}−⟨q_{B}⟩≈log⁡(V_{B}^{i}/⟨V_{B}⟩)$, with $V_{B}$ size at initiation, and $η_{B}^{i}$ Gaussian noise with mean zero and standard deviation $\sigma_{q_{B}}$. In the case in which DNA replication starts in the mother (cycle $i$) and terminates in a subsequent cell cycle (in daughters: $n=2$, in granddaughters: $n=3$), Equation (S4) becomes $\delta⁢q_{0}^{i+n}=(1-\lambda_{C+D})⁢\delta⁢q_{B}^{i}+η_{B}^{i}$. In the same way, one can represent the control strength for the $I$ and $B$ period (Micali et al., 2018a) by the following expressions linking logarithmic cell size fluctuations before and after the subperiods,

$$
\delta⁢q_{B}^{i+1}=(1-\lambda_{I})⁢\delta⁢q_{B}^{i}+η_{B}^{i}.
$$



$$
\delta⁢q_{B}^{i}=(1-\lambda_{B})⁢\delta⁢q_{0}^{i}+η_{0}^{i}.
$$

#### From size-growth plots to adder plots

As for $\lambda_{G}$, the control parameters $\lambda_{X}$ calculated from logarithmic volumes quantify size homeostasis. For small size fluctuations, they are in 1:1 relation with the slopes of the corresponding adder plots Grilli et al., 2017. Here, we translate the λ-formalism to the slopes of adder plots $ζ_{X}$(Jun and Taheri-Araghi, 2015). Equation (S1) can be rewritten as

$$
2V_{0}^{i+1}=Q_{G}(V_{0}^{i})^{1−\lambda_{G}}⟨V_{0}⟩^{\lambda_{G}}+ν_{0}^{i} ,
$$

where $Q_{G}=e^{⟨G_{G}⟩}=exp⁡⟨log⁡V_{f}/V_{0}⟩$, and $ν_{0}^{i}$ is the Gaussian noise with mean zero and standard deviation $\sigma_{V_{0}}$. Equation (S7) was first introduced in Amir, 2014. Following this study, expanding around the average size, for small fluctuations (Amir, 2014; Grilli et al., 2017) we obtain a mapping between added size and slope of the size-growth plot,

$$
2V_{0}^{i+1}=Q_{G}⟨V_{0}⟩+(1−\lambda_{G})Q_{G}\deltaV_{0}^{i}+ν_{0}^{i}2V_{0}^{i+1}−V_{0}^{i}−⟨V_{0}⟩=Q_{G}⟨V_{0}⟩+[(1−\lambda_{G})Q_{G}−1]\deltaV_{0}^{i}−2⟨V_{0}⟩+ν_{0}^{i}\deltaΔ_{G}^{i}=+[(1−\lambda_{G})Q_{G}−1]\deltaV_{0}^{i}+ν_{0}^{i}.
$$

Here $Δ_{G}^{i}=V_{f}^{i}-V_{0}^{i}$ is the added size during a cell cycle, and $\deltaΔ_{G}^{i}=Δ_{G}^{i}−⟨Δ_{G}^{i}⟩$ is its fluctuation. Hence, by definition, the term in square brackets must be the slope of the adder plot

$$
ζ_{G}:=(1-\lambda_{G})⁢Q_{G}-1.
$$

Solving the equation for $\lambda_{G}$, we get

$$
(1-\lambda_{G})=\frac{(ζ_{G}+1)}{Q_{G}},
$$

which can be used (assuming small fluctuations Grilli et al., 2017) to convert the slope $ζ_{G}$ of the adder plot into the slope of the size-growth plot $\lambda_{G}$, and vice versa.

It is straightforward to extend the relationship to cell-cycle subperiods and to the inter-initiation period, leading to the following relationships

$$
ζ_{C+D}:=(1-\lambda_{C+D})⁢Q_{C+D}-1
$$



$$
ζ_{B}:=(1-\lambda_{B})⁢Q_{B}-1
$$



$$
ζ_{I}:=(1-\lambda_{I})⁢Q_{I}-1,
$$

where $Q_{C+D}=exp⁡⟨log⁡2^{n} V_{0}/V_{B}⟩$, $Q_{B}=exp⁡⟨log⁡V_{B}/(n V_{0})⟩$, $Q_{I}=exp⁡⟨log⁡n V_{B}^{i+1}/V_{B}^{i}⟩$ and $n=⌊\tau_{C+D}/\tau⌋+1$.

It is important to notice that for inter-division and inter-initiation events in symmetrically dividing cells $Q_{G,I}≃2$. For these subperiods, adder behavior is equivalent to $ζ_{G,I}=0$. However, the same equivalence does not hold for other subperiods, and in particular of the $B$ and $C+D$ period, of interest here, since $Q_{B,C+D}\neq2$.

#### Adder coupling constants for single-process ICD models

We call here 'ICD' models all single-process models that assume a cell-size-independent mechanism in control of the inter-initiation process (I period) and a mechanism that couples cell division to the size of DNA replication initiation (C+D period). We already generalized the approach of Ho and Amir, 2015; Witz et al., 2019 to arbitrary coupling constants for the $C+D$ period (Micali et al., 2018a). In this class of models, DNA replication is the limiting process setting subsequent division and initiation events. This section presents the generalized relationships for ICD models in the formalism of adder coupling constants, for non-overlapping and overlapping replication rounds, used in Figure 4 of the main text and its supplements.

From Equation (S8) and the equivalent equations for $C+D$, $B$ and $I$, we can derive the following relationships

$$
\delta⁢V_{0}^{i+1}=\frac{(1-\lambda_{G})⁢Q_{G}}{2}⁢\delta⁢V_{0}^{i}+ν_{0}^{i}=\frac{(ζ_{G}+1)}{2}⁢\delta⁢V_{0}^{i}+ν_{0}^{i}
$$



$$
\delta⁢V_{B}^{i+1}=\frac{(1-\lambda_{I})⁢Q_{I}}{2}⁢\delta⁢V_{B}^{i}+ν_{B}^{i}=\frac{(ζ_{I}+1)}{2}⁢\delta⁢V_{B}^{i}+ν_{B}^{i}
$$



$$
\delta⁢V_{B}^{i}=(1-\lambda_{B})⁢Q_{B}⁢\delta⁢V_{0}^{i}+ν_{0}^{i}=(ζ_{B}+1)⁢\delta⁢V_{0}^{i}+ν_{0}^{i}
$$



$$
\delta⁢V_{0}^{i+n}=\frac{(1-\lambda_{C+D})⁢Q_{C+D}}{2⁢n}⁢\delta⁢V_{B}^{i}+ν_{B}^{i}=\frac{(ζ_{C+D}+1)}{2⁢n}⁢\delta⁢V_{B}^{i}+ν_{B}^{i},
$$

where $i+n$ generalizes to the case in which the size at birth of cell $i+n$ by replication initiation in cell $i$.

In ICD models, the coupling constants $ζ_{I}$ and $ζ_{C+D}$ are treated as input control parameters, while $ζ_{G}$ and $ζ_{B}$ are outcomes of the model, measured as observable correlations. The predicted correlations for ICD models are (see Micali et al., 2018a),

$$
{(ζ_{G}+1)=\frac{1}{(2⁢n)^{2}}⁢(ζ_{C+D}+1)^{2}⁢(ζ_{I}+1)⁢\frac{\sigma_{V_{B}}^{2}}{\sigma_{V_{0}}^{2}}(ζ_{B}+1)=\frac{1}{2^{(n+1)}⁢n}⁢(ζ_{C+D}+1)⁢(ζ_{I}+1)^{n}⁢\frac{\sigma_{V_{B}}^{2}}{\sigma_{V_{0}}^{2}}
$$

The model by Witz and coworkers presented in Witz et al., 2019 falls in this broad category, with the assumption that $ζ_{I,C+D}=0$, i.e. the coupling constants impose perfect adders both between initiation events and during the C+D period. The predicted correlation patterns for this model are

$$
{(ζ_{G}+1)=\frac{1}{(2⁢n)^{2}}⁢\frac{\sigma_{V_{B}}^{2}}{\sigma_{V_{0}}^{2}}(ζ_{B}+1)=\frac{1}{2^{(n+1)}⁢n}⁢\frac{\sigma_{V_{B}}^{2}}{\sigma_{V_{0}}^{2}}.
$$

Note that although the model presented in Witz et al., 2019 falls in the broad category of ICD models, the authors of this study extend the model with an additional parameter, accounting for asymmetric division. This additional ingredient allows their theory to deviate from the predictions of Equation (S19). Figure 4—figure supplement 2 illustrates this point. As discussed in the main text, asymmetric division can drive $ζ_{G}$ toward adder behavior. However, in our hands this requires unrealistically high values of asymmetry. Furthermore, this model fails to reproduce the results of the A22 perturbation presented in this work, since the specific $C+D$ control pattern is postulated in the model, while it changes with the perturbation in the experiments (Figure 4C in the main text).

#### Concurrent cycles

This section presents the predicted correlation patterns for the concurrent cycles framework in terms of adder coupling constants. In this model (Micali et al., 2018a), two cycles are in competition for setting cell division. According to the size-growth framework, a cycle ‘$H$’ starts from cell division, and has control strength $\lambda_{H}$ over the next division event. In addition, a cycle ‘$C+D^{′}$’ starts from initiation of DNA replication and has control strength $\lambda_{C+D^{′}}$ over the the division event following termination of DNA replication and segregation. At the single-cell level, the slowest process set division, and the parameter $p_{H}$ encodes the average probability of the cycle $H$ to set division.

In the concurrent cycles model, the control strength of the inter-division process ($H$), of the inter-initiation process ($I$), and of the replication-segregation processes set by initiation ($C+D^{′}$) are inputs of the model. Following Micali et al., 2018a, the latter is assumed to be a pure timer, i.e. $\lambda_{C+D^{′}}=0$. In contrast, the slopes resulting from the competition of the two concurrent cycles, that is the inter-division ($G$) slope and the slopes over the $C+D$ period are outcomes of the model, that is, predictions that can be validated using experimental data.

Following a similar approach to Micali et al., 2018a and using Equations S14-S17, we obtain

$$
⟨\deltaV_{0}^{i+1}\deltaV_{0}^{i}⟩=\frac{(ζ_{G}+1)}{2}\sigma_{V_{0}}^{2}=p_{H}\frac{(ζ_{H}+1)}{2}\sigma_{V_{0}}^{2}+(1−p_{H})\frac{Q_{C+D^{′}}}{2}(ζ_{B}+1)\sigma_{V_{0}}^{2},⟨\deltaV_{B}^{i}\deltaV_{0}^{i}⟩=(ζ_{B}+1)\sigma_{V_{0}}^{2}=\frac{(ζ_{C+D}+1)}{2}\frac{(ζ_{I}+1)}{2}\sigma_{V_{B}}^{2},⟨\deltaV_{0}^{i+1}\deltaV_{B}^{i}⟩=\frac{(ζ_{C+D}+1)}{2}\sigma_{V_{B}}^{2}=p_{H}\frac{(ζ_{H}+1)}{2}(ζ_{B}+1)\sigma_{V_{0}}^{2}+(1−p_{H})\frac{Q_{C+D^{′}}}{2}\sigma_{V_{B}}^{2},
$$

where the effective parameter $p_{H}$ quantifies the probability that the inter-division process is limiting, and is a function of basic parameters that are fixed in a given condition, such as mean size at initiation and noises (see Micali et al., 2018a).

The above equations can be recast into the following relationships involving adder coupling constants:

$$
{(ζ_{G}+1)=p_{H}⁢(ζ_{H}+1)+(1-p_{H})⁢Q_{C+D^{′}}⁢(ζ_{B}+1)(ζ_{B}+1)=(ζ_{C+D}+1)⁢(ζ_{I}+1)⁢\frac{\sigma_{V_{B}}^{2}}{4⁢\sigma_{V_{0}}^{2}}(ζ_{C+D}+1)=\frac{(1-p_{H})⁢Q_{C+D^{′}}}{(1-p_{H}⁢\frac{(ζ_{H}+1)⁢(ζ_{I}+1)}{4})}.
$$

Finally, for the specific case of the adder-adder model in which both the inter-initiation and the $H$ processes are adders ($ζ_{I}=0$ and $ζ_{H}=0$), the same relationships simplify into the following scheme,

$$
{(ζ_{G}+1)=p_{H}+(1-p_{H})⁢Q_{C+D^{′}}⁢(ζ_{B}+1)(ζ_{B}+1)=\frac{(1-p_{H})}{(1-\frac{p_{H}}{4})}⁢\frac{Q_{C+D}⁢\sigma_{V_{B}}^{2}}{4⁢\sigma_{V_{0}}^{2}}(ζ_{C+D}+1)=\frac{(1-p_{H})⁢Q_{C+D^{′}}}{(1-\frac{p_{H}}{4})}.
$$

Note that Equations (S20)-(S21) are valid for $n=1$, that is for initiation and termination that happen in the same cell cycle. As discussed in Micali et al., 2018a simulations are used to extend the results to $n>1$.

The latter model involving adders over $I$ and $H$ is used for the comparison in Figure 4 of the main text, while a more general model fixing $ζ_{I}=0$ but allowing $ζ_{H}$ to vary is used for the fit in Figure 4—figure supplement 1. Note that in the above expressions $Q_{C+D^{′}}$ is the growth during the $C+D^{′}$ period and is not measurable directly. To bypass this problem, we approximate it by $Q_{C+D^{′}}=1.8$, which is the average measured $Q_{C+D}$ in unperturbed conditions. $Q_{C+D^{′}}$ is equal to $Q_{C+D}$ for $p_{H}=0$. In unperturbed conditions, where $p_{H}≃0.5$, $Q_{C+D^{′}}\leqQ_{C+D}$, and the two values are similar, since they differ only by the low-CV noise of the inter-division process. For the A22 perturbations, we assumed that the value of $Q_{C+D^{′}}$ remains constant, as the $C+D^{′}$ period should be unperturbed by A22 increasing concentrations (as supported by Figure 2C, since the measurable $C$ period is on average constant). We also note that this approximation is equivalent to the reasonable assumption that $Q_{H}≃2$ used in Micali et al., 2018a.

### Brief description of simulations

In this manuscript, we used stochastic simulations for two reasons: (i) to explore the role of asymmetric division in ICD models (Figure 4—figure supplement 2), as suggested by Witz et al., 2019, (ii) to validate the analytical predictions for $ζ_{G}$ and $ζ_{C⁢D}$ for the concurrent cycles model and in particular the robustness of the small noise approximation and to quantitative extend concurrent cycle predictions for $⟨\tau_{C+D}⟩/⟨\tau⟩>1$ (Figure 4—figure supplement 4).

For simulations in Figure 4—figure supplement 2 that account for asymmetric division, we were inspired by the model in Witz et al., 2019. Briefly, for each initiation event $V_{B}^{i}$, the number of origins noris is duplicated and two random added lengths are chosen from log-normal distributions for the I-period ($Δ_{I}^{i}$) and the C+D-period ($Δ_{C⁢D}^{i}$), respectively. Note that both means ($⟨Δ_{I}⟩$ and $⟨Δ_{CD}⟩$) and standard deviation ($\sigma_{I}$ and $\sigma_{C⁢D}$) of the distributions are parameters inferred from data. $Δ_{C⁢D}^{i}$ sets the division event: $V_{d}^{i}=V_{B}^{i}+Δ_{CD}^{i}$, if $n_{oris}=1$, if $n_{oris}=2$. Events with $n_{oris}>2$ are rare in the conditions used in Figure 4—figure supplement 2. However, the simulations can account for those events correcting for asymmetries in the multiple divisions and ensuring an added size between $V_{B}^{i}/2^{n_{oris}-1}$ and the triggered division event equal to $Δ_{C⁢D}^{i}$. The number or origins is divided by two at each division event. To account of asymmetric division, the newborn cell has volume $V_{0}^{i+1}$ set by a Gaussian random variable with mean $V_{d}^{i}/2$ and standard deviation $\alpha⁢V_{d}^{i}/2$. Typical values of α from our experimental data are 0.05 (see Figure 4—figure supplement 2). The next initiation event is set by $Δ_{I}^{i}$ if the next initiation event is in the same cell cycles, $V_{B}^{i+1}=\frac{V_{B}^{i}}{2}+n_{oris}⁢Δ_{I}^{i}-(\frac{V_{d}^{i}}{2}-V_{0}^{i+1})$ if the next initiation event is in the following cell cycle. More complicated scenarios in which the next initiation event is in further cell cycles accounts for the multiple asymmetric division events and calculate the actual added size. In the conditions used in Figure 4—figure supplement 2 these events are rare.

For simulations in Figure 4—figure supplement 4 of the concurrent-cycles model with perfectly symmetric division, we refer the reader to Micali et al., 2018b.

### Description of the analysis of data from the literature

To compare our findings with data available in the literature, we downloaded data of untreated conditions from Si et al., 2019 (downloaded at https://www.sciencedirect.com/science/article/pii/ S0960982219304919) and Witz et al., 2019 (downloaded at https://zenodo.org/record/3149097#. X7PKA9NKhBx). Excel files are imported in MATLAB using the function readtable and all the subsequent analysis has been performed with MATLAB. Since this manuscript is focused on slow-growth conditions, we restrict our comparision with (Si et al., 2019) to their slow-growth conditions (MG1655 acetate and NCM3722 MOPS arginine) (see Figure 4—figure supplement 3).

Note that Si et al., 2019 report the initiation size per origin without specifying the number of origins and without providing the added size during C+D. For this reason, we assume the number of origins by plotting the size at initiation vs the size of newborn cells. Cells in which the initiation per origins is smaller than the size at birth are considered to terminate DNA replication in the daughter cell. In this case, the added size during C+D is estimated from ( division size (micron) - initiation size per ori (micron)/ 2 + division size (micron) daughter - newborn size (micron) daughter. Cells in which the initiation per origins is larger than the size at birth are considered to terminate DNA replication in the same cycle as initiation started. Hence, the added size during C+D is division size (micron) - initiation size per ori (micron). The added size between division events is estimated from division size (micron) - newborn size (micron). The added size during two consecutive initiation events is estimated from ( division size (micron)-initiation size per ori (micron) ) / 2 +initiation size per ori (micron) daughter - newborn size (micron) daughter). The slopes $ζ_{G}$, $ζ_{I}$ and $ζ_{C⁢D}$ were calculated by applying the robustfit function in MATLAB to the clouds of points of the inter division, inter initiation and C+D adder plots, respectively.

The data from Witz et al., 2019 are in a different format which provides the inter-division, inter-initiation and $C+D$ added size as well as size at birth and size at initiation. For this reason, we were able to calculate the $ζ_{G}$, $ζ_{I}$, and $ζ_{C⁢D}$ directly using the added quantities and the robustfit function in MATLAB.

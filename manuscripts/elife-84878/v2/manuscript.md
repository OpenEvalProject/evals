# An optimal regulation of fluxes dictates microbial growth in and out of steady state

## Authors

- Griffin Chure<sup>1</sup> ([ORCID: 0000-0002-2216-2057](https://orcid.org/0000-0002-2216-2057)) †
- Jonas Cremer<sup>1</sup> ([ORCID: 0000-0003-2328-5152](https://orcid.org/0000-0003-2328-5152)) †

### Affiliations

1. Department of Biology, Stanford University Stanford United States ([ROR:00f54p054](https://ror.org/00f54p054))

† Corresponding author

## Abstract

Effective coordination of cellular processes is critical to ensure the competitive growth of microbial organisms. Pivotal to this coordination is the appropriate partitioning of cellular resources between protein synthesis via translation and the metabolism needed to sustain it. Here, we extend a low-dimensional allocation model to describe the dynamic regulation of this resource partitioning. At the core of this regulation is the optimal coordination of metabolic and translational fluxes, mechanistically achieved via the perception of charged- and uncharged-tRNA turnover. An extensive comparison with ≈ 60 data sets from Escherichia coli establishes this regulatory mechanism’s biological veracity and demonstrates that a remarkably wide range of growth phenomena in and out of steady state can be predicted with quantitative accuracy. This predictive power, achieved with only a few biological parameters, cements the preeminent importance of optimal flux regulation across conditions and establishes low-dimensional allocation models as an ideal physiological framework to interrogate the dynamics of growth, competition, and adaptation in complex and ever-changing environments.

## Introduction

Growth and reproduction is central to life. This is particularly true of microbial organisms where the ability to quickly accumulate biomass is critical for competition in ecologically diverse habitats. Understanding which cellular processes are key in defining growth has thus become a fundamental goal in the field of microbiology. Pioneering physiological and metabolic studies throughout the 20th century laid the groundwork needed to answer this question (Monod, 1935; Monod, 1937; Monod, 1941; Monod, 1947; Monod, 1966; Campbell, 1957; Schaechter et al., 1958; Kjeldgaard et al., 1958; Cooper and Helmstetter, 1968; Donachie et al., 1976; Jun et al., 2018), with the extensive characterization of cellular composition across growth conditions at both the elemental (Heldal et al., 1985; Loferer-Krößbacher et al., 1998; Lawford and Rousseau, 1996) and molecular (Schaechter et al., 1958; Kjeldgaard et al., 1958; Watson, 1976; Britten and Mcclure, 1962) levels showing that the dry mass of microbial cells is primarily composed of proteins and RNA. Seminal studies further revealed that the cellular RNA content is strongly correlated with the growth rate (Schaechter et al., 1958; Kjeldgaard et al., 1958; Gausing, 1977), an observation which has held for many microbial species (Karpinets et al., 2006). As the majority of RNAs are ribosomal, these observations suggested that protein synthesis via ribosomes is a major determinant of biomass accumulation in nutrient replete conditions (Koch, 1988; Hernandez and Bremer, 1993; Magasanik et al., 1959). Given that the cellular processes involved in biosynthesis, particularly those of protein synthesis, are well conserved between species and domains (Doris et al., 2015; Davidovich et al., 2009; Bruell et al., 2008), these findings have inspired hope that fundamental principles of microbial growth can be found despite the enormous diversity of microbial species and the variety of habitats they occupy.

The past decade has seen a flurry of experimental studies further establishing the importance of protein synthesis in defining growth. Approaches include modern ‘-omics’ techniques with molecular-level resolution (Taniguchi et al., 2010; Bennett et al., 2009; Schmidt et al., 2016; Valgepea et al., 2013; Peebo et al., 2015; Li et al., 2014; Balakrishnan et al., 2021b; Mori et al., 2021; Belliveau et al., 2021; Metzl-Raz et al., 2017; Paulo et al., 2015; Paulo et al., 2016; Xia et al., 2021; Jahn et al., 2018), measurements of many core physiological processes and their coordination (Dai et al., 2016; Basan et al., 2015; You et al., 2013; Wu et al., 2022; Di Bartolomeo et al., 2020; Li et al., 2018; Jahn et al., 2018; Zavřel et al., 2019; Parker et al., 2020), and the perturbation of major cellular processes like translation (Scott et al., 2010; Hui et al., 2015; Dai et al., 2016; Towbin et al., 2017). Together, these studies advanced a more thorough description of how cells allocate their ribosomes to the synthesis of different proteins depending on their metabolic state and the environmental conditions they encounter, called ribosomal allocation. Tied to the experimental studies, different theoretical ribosomal allocation models have further been formulated to dissect how ribosomal allocation influences growth (Molenaar et al., 2009; Karr et al., 2012; Scott et al., 2014; Weiße et al., 2015; Maitra and Dill, 2015; Giordano et al., 2016; Mori et al., 2017; Erickson et al., 2017; Towbin et al., 2017; Mori et al., 2017; Korem Kohanim et al., 2018; Macklin et al., 2020; Hu et al., 2020; Dourado and Lercher, 2020; Roy et al., 2021; Mori et al., 2021; Serbanescu et al., 2020; Balakrishnan et al., 2021a; Balakrishnan et al., 2021b). For example, high-dimensional models have been formulated which simulate hundreds to thousands of biological reactions (Karr et al., 2012; Macklin et al., 2020) providing a detailed view of the emergence of distinct internal physiological states and the underlying processes which sustain them. Alternatively, other theoretical considerations follow coarse-grained approaches of moderate dimensionality which group different classes metabolic reactions together and mathematizicing their dynamics (Roy et al., 2021; Hu et al., 2020). Distinct from these is an array of extremely low-dimensional models, pioneered by Molenaar et al., 2009, which have been developed to describe growth phenomena in varied conditions and physiological limits that rely on only a few parameters (Molenaar et al., 2009; Scott et al., 2014; Bosdriesz et al., 2015; Giordano et al., 2016; Towbin et al., 2017; Korem Kohanim et al., 2018; Erickson et al., 2017; Mairet et al., 2021; Balakrishnan et al., 2021a) (a more detailed overview of the different modeling approaches is provided in Appendix 1 - Allocation models to study microbial growth).

In this work, we build on low-dimensional allocation models (Scott et al., 2014; Giordano et al., 2016; Bosdriesz et al., 2015; Dourado and Lercher, 2020; Hu et al., 2020) and the results from dozens of experimental studies to synthesize a self-consistent and quantitatively predictive description of resource allocation and growth. At the core of our model is the dynamic reallocation of resources between the translational and metabolic machinery, which is sensitive to the metabolic state of the cell. We demonstrate how ‘optimal allocation’—meaning an allocation towards ribosomes which contextually maximizes the steady-state growth rate—emerges when the flux of amino acids through translation to generate new proteins and the flux of uncharged-tRNA through metabolism to provide charged-tRNA required for translation are mutually maximized, given the environmental conditions and corresponding physiological constraints. This regulatory scheme, which we term flux-parity regulation, can be mechanistically achieved by a global regulator (e.g., guanosine tetraphosphate, ppGpp, in bacteria) capable of simultaneously measuring the turnover of charged- and uncharged-tRNA pools and routing protein synthesis. The explanatory power of the flux-parity regulation circuit is confirmed by extensive comparison of model predictions with ≈ 60 data sets from Escherichia coli, spanning more than half a century of studies using varied methodologies. This comparison demonstrates that a simple argument of flux-sensitive regulation is sufficient to predict bacterial growth phenomena in and out of steady state and across diverse physiological perturbations. The accuracy of the predictions, coupled with the minimalism of the model, establishes the optimal regulation and cements the centrality of protein synthesis in defining microbial growth. The mechanistic nature of the theory—predicated on a minimal set of biologically meaningful parameters—provides a low-dimensional framework that can be used to explore complex phenomena at the intersection of physiology, ecology, and evolution without requiring extensive characterization of the myriad biochemical processes which drive them.

### A simple allocation model describes translation-limited growth

We begin by formulating a simplified model of growth which follows the flow of mass from nutrients in the environment to biomass by building upon and extending the general logic of low-dimensional resource allocation models (Molenaar et al., 2009; Scott et al., 2010; Scott et al., 2014; Dai et al., 2016; Giordano et al., 2016). Specifically, we focus on the accumulation of protein biomass, as protein constitutes the majority of microbial dry mass (Churchward et al., 1982; Feijó Delgado et al., 2013) and peptide bond formation commonly accounts for ≈80% of the cellular energy budget (Stouthamer, 1973; Belliveau et al., 2021). Furthermore, low-dimensional allocation models utilize a simplified representation of the proteome where proteins can be categorized into only a few functional classes (Molenaar et al., 2009; Scott et al., 2014; Hui et al., 2015; Maitra and Dill, 2015; Dourado and Lercher, 2020). In this work, we consider proteins to be either ribosomal (i.e., a structural component of the ribosome, excluding ternary complex members like EF-Tu), metabolic (i.e., enzymes catalyzing synthesis of charged-tRNA molecules from environmental nutrients), or being involved in all other biological processes (e.g., lipid synthesis, DNA replication, energy generation, and chemotaxis) Molenaar et al., 2009; Scott et al., 2010; Scott et al., 2014; Hui et al., 2015; Figure 1—figure supplement 1; in Appendix 1 What makes the fraction of ‘other’ proteins?, we outline in more detail how individual protein species are partitioned between the ‘metabolic’ and ‘other’ sectors depending on their functional annotations. Simple allocation models further do not distinguish between different cells but only consider the overall turnover of nutrients and biomass. To this end, we explicitly consider a well-mixed batch culture growth as reference scenario where the nutrients are considered to be in abundance. This low-dimensional view of living matter may at first seem like an unfair approximation, ignoring the decades of work interrogating the multitudinous biochemical and biophysical processes of cell-homeostasis and growth (Macklin et al., 2020; Karr et al., 2012; Hui et al., 2015; Grigaitis et al., 2021; Noree et al., 2019). However, at least in nutrient replete conditions, many of these processes appear not to impose a fundamental limit on the rate of growth in the manner that protein synthesis does (Belliveau et al., 2021). In Appendix 1 The major simplifications of low-dimensional allocation models and why they might work we discuss this along with other simplifications in more detail.

To understand protein synthesis and biomass growth within the low-dimensional allocation framework, consider the flux diagram (Figure 1A, Molenaar et al., 2009; Giordano et al., 2016; Belliveau et al., 2021; Balakrishnan et al., 2021b; Scott et al., 2014) showing the masses of the three protein classes, precursors which are required for protein synthesis (including charged-tRNA molecules, free amino acids, cofactors, etc.), nutrients which are required for the synthesis of precursors, and the corresponding fluxes through the key biochemical processes (arrows). This diagram emphasizes that growth is autocatalytic in that the synthesis of ribosomes is undertaken by ribosomes which imposes a strict speed limit on growth (Dill et al., 2011; Belliveau et al., 2021; Kafri et al., 2016). While this may imply that the rate of growth monotonically increases with increasing ribosome abundance, it is important to remember that metabolic proteins are needed to supply the ribosomes with the precursors needed to form peptide bonds. Herein lies the crux of ribosomal allocation models: the abundance of ribosomes is constrained by the need to synthesize other proteins and growth is a result of how new protein synthesis is partitioned between ribosomal, metabolic, and other proteins. How is this partitioning determined, and how does it affect growth?

![Figure 1.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig1-v2.jpg)

**Figure 1.:** (A) The flow of mass through the self-replicating system. Biomolecules and biosynthetic processes are shown as gray and white boxes, respectively. Nutrients in the environment passed through cellular metabolism to produce ‘precursor’ molecules which are then consumed through the process of translation to produce new protein biomass, either as metabolic proteins (purple arrow), ribosomal proteins (gold arrow), or ‘other’ proteins (gray arrow). (B) Annotated equations of the model with key parameters highlighted in blue. An interactive figure where these equations can be numerically integrated is provided on paper website (cremerlab.github.io/flux_parity). (C) Key model parameters, their units, typical values in E. coli, and their appropriate references. This is also provided as Supplementary file 1. The steady-state values of (D) the growth rate $\lambda$ and (E) the relative translation rate $\gamma⁢(c_{p⁢c}^{*})/\gamma_{m⁢a⁢x}$, are plotted as functions of the allocation towards ribosomes for different metabolic rates (colored lines). (F) Analytical solutions for candidate scenarios for regulation of ribosomal allocation with fixed allocation, allocation to prioritize translation rate, and allocation to optimal growth rate highlighted in gray, green, and blue respectively. (G) A list of collated data sets of E. coli ribosomal allocation and translation speed measurements spanning 55 years of research. Details regarding these sources and method of data collation is provided in Supplementary file 2. A comparison of the observations with predicted growth-rate dependence of ribosomal allocation (H) and translation speeds (I) for the three allocation strategies. An interactive version of the panels allowing the free adjustment of parameters is available on the associated paper website (cremerlab.github.io/flux_parity).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Low-dimensional allocation models consider in their simplest form growth of a clonal population within a well-mixed environment. Biomass is described in a highly simplified manner focusing in the simplest case on protein synthesis alone (Molenaar et al., 2009, Scott et al., 2014), with different protein species jointly considered by a few different protein classes. Here, metabolic proteins (purple), ribosomal proteins (gold), or ‘other’ proteins (gray). Sectors areas are displayed as being approximately equivalent to those found in rapidly growing E. coli.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** In general, the environmental conditions microbes encounter changes rapidly and nutrient availability commonly limits growth. Growing batch cultures, for example, run out of nutrients eventually and growth stops. The allocation modeling framework can account such a dynamics by including metabolic rates which depend on the nutrient concentrations in the environment. In the simplest case, one nutrient source is considered (concentration $c_{nt}$) with the metabolic rate $ν(c_{nt})$ depending on the concentration in a Michaelis–Menten manner with a maximal metabolic rate being reached only at high nutrient concentrations (Ai). The dynamics of precursors is given by a balance of synthesis, consumption, and dilution (Aii), replacing the corresponding equation of the simple model in (Figure 1Biv). The modeling of growth further requires the explicit modeling of nutrient concentrations. This dynamics depends on the specifics of the environment and, depending on the environment, can become very complex with multiple sources and sinks affecting the nutrient concentration. Here, we consider a typical batch culture scenario in which cells grow under well-mixed conditions. Nutrients are provided only initially and nutrient concentrations are falling because of consumption (Aiii). (B) Model parameters, dimensions, values, and relevant reference for including nutrient dynamics. (C–E) Resulting temporal variation of nutrient concentrations (C), biomass accumulation (D), and precursor concentration (E) when integrating the model equations and using a parameter set descriptive of E. coli growing in a glucose-minimal medium with a growth rate ≈1 hr-1 and a starting glucose concentration of 10 mM. As experimentally observed, initially abundant nutrients are consumed and biomass accumulates (exponential phase) until nutrients are exhausted and growth stops (saturation phase) (C, D). Importantly, precursor concentrations (E) quickly reach a constant plateau which lasts until nutrients become scarce ($c_{n⁢t}≫K_{M}^{c_{n⁢t}}$ and $ν⁢(c_{n⁢t})≈ν_{m⁢a⁢x}$). During this transient period (shaded regions), the synthesis of precursors matches the consumption by protein synthesis and dilution, meaning $\frac{d⁢c_{p⁢c}}{d⁢t}=0$. Given a constant precursor concentration $c_{p⁢c}^{*}$, the translation rate $\gamma⁢(c_{p⁢c}^{*})$ is also constant. As a consequence, the protein pool approaches a steady composition dictated by the allocation parameters ($\frac{M_{R⁢b}}{M}=ϕ_{R⁢b}$, $\frac{M_{M⁢b}}{M}=ϕ_{M⁢b}$ and $\frac{M_{O}}{M}=ϕ_{O}$). With precursor concentrations and protein composition remaining constant, the system is in a steady state and biomass accumulates exponentially over time, $\frac{d⁢M}{d⁢t}=\gamma⁢(c_{p⁢c}^{*})⁢ϕ_{R⁢b}⁢M≡\lambda⁢M$. This is the steady-state regime we focus on in the main text. Note that the steady state growth regime readily emerges when we consider dilution (see Appendix 1 - Precursor concentrations and the importance of dilution by cell growth). Model parameters are provided in Supplementary file 1. Biomass units are converted to optical density assuming at $O⁢D_{600⁢n⁢m}=1$, there are 109 cells per ml and 109 amino acids per cell. An interactive version of these dynamics can be found on the paper website (cremerlab.github.io/flux_parity).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Variation of the precursor concentration with varying allocation parameters ($ϕ_{Rb}$) and maximal metabolic rate ($ν_{m⁢a⁢x}$). (B, C) Corresponding trends of translation and growth rate as also shown in Figure 1C and D. Corresponding boxes show the analytical expression describing the steady-state precursor concentration, translation speed, and growth rate with details of the derivation provided in 'Methods.' Model parameters used are provided in Supplementary file 1. Colors indicate different metabolic rates $ν_{m⁢a⁢x}$ = 0.2–12.5 hr-1.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** The variation of precursor concentration (A), translation rate (B), and growth rate (C) with changing metabolic rate is shown for the three allocation scenarios introduced in the main text; fixed allocation (scenario I, black lines), prioritizing fast translation (scenario II, green lines), and growth-optimal allocation (scenario III, blue lines). Plotted are the analytical solutions provided in Figure 1F and derived in 'Methods.' The resulting relations between growth rate and translation as well as growth rate and ribosome content are shown in Figure 1H andI. We here discuss the consequence of these allocation scenarios in more detail. Scenario I—fixed allocation: In this scenario, allocation is fixed and does not vary with conditions. Locking in the ribosome allocation to $ϕ_{Rb}=0.20$ (A, black line), for example, carries strong consequences for translation and growth rates (B and C, black lines). When conditions are poor ($ν_{m⁢a⁢x}$ is small), the translation rate is significantly lower than the maximal rate as there are too many ribosomes competing for a small pool of precursors (B). The translation and growth rates increase with the metabolic rate $ν_{m⁢a⁢x}$ until the influx of precursors is sufficiently high such that all ribosomes are translating close to their maximum and growth rate is at its optimal value. Further increasing the metabolic rate does not increase the growth rate (plateau of black curve in B) as all ribosomes are already translating close to their maximum rate. Scenario II—prioritizing fast translation: In this scenario, allocation is adjusted such that translation rates are maintained at a high value. This is achieved by tuning the allocation between ribosomes and metabolic proteins such that a constant precursor concentration $c_{p⁢c}^{*}≫K_{M}^{c_{p⁢c}}$ is maintained. For example, at higher metabolic rates, the metabolic proteins can sustain a higher influx of precursors allowing a larger allocation towards ribosomal proteins $ϕ_{Rb}$ (green lines). Scenario III—optimizing growth: In this scenario, allocation is tuned to optimize growth rate across conditions, meaning that the fastest growth rate is achieved given a set metabolic rate and other model parameters. For example, the allocation towards ribosomes $ϕ_{R⁢b}$ is adjusted with the metabolic rate such that the growth rate rests at the peak of the curves shown in Figure 1D (blue lines). Accordingly, the growth rate continues to increase with higher metabolic rates always exceeding the growth rate of scenarios I and II (C, green line). Model parameters follow the reference set for E. coli (Supplementary file 1). Black lines correspond to a constant allocation $ϕ_{R⁢b}^{(I)}=0.20$ and green lines correspond to a constant precursor concentration $c_{p⁢c}^{*}≈10⁢K_{M}^{c_{p⁢c}}$, yielding a constant translation rate of $\gamma⁢(c_{p⁢c}^{*})≈0.9⁢\gamma_{m⁢a⁢x}$. An interactive version of these figure panels is available on the paper website (cremerlab.github.io/flux_parity).

To answer these questions, we must understand how these different fluxes interact at a quantitative level and thus must mathematize the biology underlying the boxes and arrows in Figure 1A. Taking inspiration from previous models of allocation (Molenaar et al., 2009; Scott et al., 2010; Scott et al., 2014; Giordano et al., 2016; Dourado and Lercher, 2020), we enumerate a minimal set of coupled differential equations which captures the flow of mass through metabolism and translation (Figure 1B, with the dimensions and value ranges of the parameters listed in Figure 1C and Supplementary file 1). While we present a step-by-step introduction of this model in ‘Methods,’ we here focus on a summary of the underlying biological intuition and implications of the approach.

We begin by codifying the assertion that protein synthesis is key in determining growth. The synthesis of new total protein mass $M$ depends on the total proteinaceous mass of ribosomes $M_{R⁢b}$ present in the system and their corresponding average translation rate $\gamma$ (Figure 1Bi). As ribosomes rely on precursors to work, it is reasonable to assert that this translation rate must be dependent on the concentration of precursors $c_{p⁢c}$ such that $\gamma≡\gamma⁢(c_{p⁢c})$ (Scott et al., 2014; Giordano et al., 2016), for which a simple Michaelis–Menten relation is biochemically well motivated (Figure 1Bii). With changing precursor concentrations, the translation rate $\gamma$ varies between a maximum value $\gamma_{m⁢a⁢x}$, representing rapid synthesis, and a minimum value $\gamma_{m⁢i⁢n}$, representing the slowest achievable translation rate. In our model, this minimum rate $\gamma_{m⁢i⁢n}$ is zero and corresponds to the condition where there are no available precursors to support translation. The standing precursor concentration $c_{p⁢c}$ is set by a combination of processes (Figure 1Biii), namely the production of new precursors through metabolism (synthesis), their degradation through translation (consumption), and their dilution as the total cell volume grows. The synthesis is driven by the abundance of metabolic proteins $M_{M⁢b}$ in the system and the speed by which they convert nutrients into novel precursors. As the metabolic networks at play are complex, low-dimensional allocation models describe the process of metabolism using an average metabolic rate $ν$ in lieu of mathematicizing the network’s individual components. As such, the metabolic rate is difficult to directly measure but generally depends on the quality and concentration of nutrients in the environment (see below, Figure 1—figure supplement 2 and ‘Methods’). In the following, we focus on a growth regime in which nutrient concentrations are saturating. In such a scenario, metabolism operates at a nutrient-specific maximal metabolic rate $ν≡ν_{m⁢a⁢x}$. Finally, the relative magnitude of the ribosomal, metabolic, and ‘other’ protein masses is dictated by $ϕ_{R⁢b}$, $ϕ_{M⁢b}$, and $ϕ_{O}$, three allocation parameters which range between zero and one to describe the fraction of ribosomes being utilized in synthesizing the corresponding protein pools. Importantly, as ribosomes only translate one protein at a time, the allocation parameters follow the constraint $ϕ_{R⁢b}+ϕ_{M⁢b}+ϕ_{O}=1$ (Figure 1Biv). For readers familiar with allocation models, we emphasize that we here use $ϕ_{X}$ to denote allocation parameters rather than mass fractions, $M_{X}/M$; both quantities are only equivalent in the steady-state regime. Together, the introduced equations provide a full mathematicization of the mass flow diagram shown in Figure 1A.

For constant allocation parameters ($ϕ_{R⁢b}^{*},ϕ_{M⁢b}^{*}$), a steady-state regime emerges from this system of differential equation. Particularly, the precursor concentration is stationary in time ($c_{p⁢c}=c_{p⁢c}^{*}$), meaning the rate of synthesis is exactly equal to the rate of consumption and dilution. Furthermore, the translation rate $\gamma⁢(c_{p⁢c}^{*})$ is constant during steady-state growth and the mass abundances of ribosomes and metabolic proteins are equivalent to the corresponding allocation parameters, e.g. $\frac{M_{R⁢b}}{M}≡ϕ_{R⁢b}^{*}$. As a consequence, biomass is increasing exponentially $\frac{d⁢M}{d⁢t}=\lambda⁢M$, with the growth rate $\lambda=\gamma⁢(c_{p⁢c}^{*})⁢ϕ_{R⁢b}^{*}$. The emergence of a steady state and analytical solutions describing steady growth are further discussed in Figure 1—figure supplement 2 and Figure 1—figure supplement 3. Notably, dilution is important to obtain a steady state as has been highlighted previously by Giordano et al., 2016 and Dourado and Lercher, 2020 but is often neglected (Appendix Precursors concentrations and the importance of dilution by cell growth).

Figure 1D and E show how the steady-state growth rate $\lambda$ and translation rate $\gamma⁢(c_{p⁢c}^{*})$ are dependent on the allocation towards ribosomes $ϕ_{R⁢b}^{*}$. The figures also show the dependence on the metabolic rate $ν_{m⁢a⁢x}$ which we here assert to be a proxy for the ‘quality’ of the nutrients in the environment (with increasing $ν_{m⁢a⁢x}$, less metabolic proteins are required to obtain the same synthesis of precursors). The non-monotonic dependence of the steady-state growth rate on the ribosome allocation and the metabolic rate poses a critical question: What biological mechanisms determine the allocation towards ribosomes in a particular environment and what criteria must be met for the allocation to ensure efficient growth?

### Different strategies for regulation of allocation predicts different phenomenological behavior

While cells might employ many different ways to regulate allocation, we here consider three specific allocation scenarios to illustrate the importance of allocation on growth. These candidate scenarios either strictly maintain the total ribosomal content (scenario I), maintain a high rate of translation (scenario II), or optimize the steady-state growth rate (scenario III). We derive analytical solutions for these scenarios (as has been previously performed for scenario III; Giordano et al., 2016; Dourado and Lercher, 2020; Figure 1F and ‘Methods’), and ultimately compare these predictions to observations with E. coli to show this organisms’ optimal allocation of resources.

The simplest and perhaps most näive regulatory scenario is one in which the allocation towards ribosomes is completely fixed and independent of the environmental conditions. This strategy (scenario I in Figure 1F, gray) represents a locked-in physiological state where a specific constant fraction of all proteins is ribosomal. This imposes a strict speed limit for growth when all ribosomes are translating close to their maximal rate, $\gamma⁢(c_{p⁢c}^{*})≈\gamma_{m⁢a⁢x}$. If the fixed allocation is low (e.g., $ϕ_{R⁢b}^{(I)}=0.2$), then this speed limit could be reached at moderate metabolic rates.

A more complex regulatory scenario is one in which the allocation towards ribosomes is adjusted to prioritize the translation rate. This strategy (scenario II in Figure 1F, green) requires that the ribosomal allocation is adjusted such that a constant internal concentration of precursors $c_{p⁢c}^{*}$ is maintained across environmental conditions, irrespective of the metabolic rate. In the case where this standing precursor concentration is large ($c_{p⁢c}^{*}≫K_{M}^{c_{p⁢c}}$), all ribosomes will be translating close to their maximal rate.

The third and final regulatory scenario is one in which the allocation towards ribosomes is adjusted such that the steady-state growth rate is maximized. The analytical solution which describes this scenario (scenario III in Figure 1F) resembles previous analytical solutions by Giordano et al., 2016; Dourado and Lercher, 2020. More illustratively, the strategy can be thought of as one in which the allocation towards ribosomes is tuned across conditions such that the observed growth rate rests at the peak of the curves in Figure 1D. Notably, this does not imply that the translation rate is constantly high across conditions (as in scenario II). Rather, the translation rate is also adjusted and approaches its maximal value $\gamma_{m⁢a⁢x}$ only in very rich conditions (high metabolic rates). All allocation scenarios and their consequence on growth are discussed in further detail in Figure 1—figure supplement 4 and the corresponding interactive figure on the paper website (cremerlab.github.io/flux_parity).

### E. coli regulates its ribosome content to optimize growth

Thus far, our modeling of microbial growth has remained ‘organism agnostic’ without pinning parameters to the specifics of any one microbe’s physiology. To probe the predictive power of this simple allocation model and test the plausibility of the three different strategies for regulation of ribosomal allocation, we performed a systematic and comprehensive survey of data from a vast array quantitative studies of the well-characterized bacterium E. coli. This analysis, consisting of 26 studies spanning 55 years of research (listed in Supplementary file 2 and as Figure 1—source data 1 and Figure 1—source data 2) using varied experimental methods, goes well beyond previous attempts to compare allocation models to data (Scott et al., 2010; Hui et al., 2015; Erickson et al., 2017; Giordano et al., 2016; Bosdriesz et al., 2015; Hu et al., 2020; Dourado and Lercher, 2020; Serbanescu et al., 2020; Hu et al., 2020; Roy et al., 2021; Maitra and Dill, 2015; Weiße et al., 2015).

These data, shown in Figure 1H and I (markers), present a highly consistent view of E. coli physiology where the allocation towards ribosomes (equivalent to ribosomal mass fraction in steady-state balanced growth) and the translation rate demonstrate a strong dependence on the steady-state growth rate in different carbon sources. The pronounced correlation between the allocation towards ribosomes and the steady-state growth rate immediately rules out scenario I, where allocation is constant, as a plausible regulatory strategy used by E. coli, regardless of its precise value. Similarly, the presence of a dependence of the translation speed on the growth rate rules out scenario II, where the translation rate is prioritized across growth rates and maintained at a constant value. The observed phenomenology for both the ribosomal allocation and the translation speed is only consistent with the logic of regulatory scenario III where the allocation towards ribosomes is tuned to optimize growth rate.

This logic is quantitatively confirmed when we compute the predicted dependencies of these quantities on the steady-state growth rate for the three scenarios diagrammed in Figure 1F based on literature values for key parameters (outlined in Supplementary file 1). Deviations from the prediction for scenario III are only evident for the ribosomal content at very slow steady growth ($\lambda\leq0.5$ hr-1), which are hardly observed in any ecologically relevant conditions and can be attributed to additional biological and experimental factors, including protein degradation (Calabrese et al., 2021) and cultures which have not yet reached steady state, factors we discuss in Appendix 1 – Additional considerations relevant at slow growth. The inactivation of ribosomes is another such explanation, though a growth rate-independent inactive fraction is not sufficient to explain the observations, Appendix 1 —Inactive ribosomes.

Importantly, the agreement between theory and observations works with a minimal number of parameters and does not require the inclusion of fitting parameters. All fixed model parameters such as the maximum translation rate $\gamma_{m⁢a⁢x}$ and the Michaelis–Menten constant for translation $K_{M}^{c_{p⁢c}}$ have distinct biological meaning and can be either directly measured or inferred from data (Supplementary file 1). Furthermore, we discuss the necessity of other parameters such as the ‘other protein sector’ $ϕ_{O}$ (Appendix 1— What makes the fraction of 'other' proteins?), its degeneracy with the maximum metabolic rate $ν_{m⁢a⁢x}$, and inclusion of ribosome inactivation and minimal ribosome content (Appendix 1— Inactive ribosomes). We, furthermore, provide an interactive figure on the paper website (cremerlab.github.io/flux_parity) where the parametric sensitivity of these regulatory scenarios and the agreement/disagreement with data can be directly explored. Notably there is no combination of parameter values that would allow scenario I or II to adequately describe both the ribosomal allocation and the translation speed as a function of growth rate. These findings are in line with a recent higher-dimensional modeling study (Hu et al., 2020), which, based on the optimization of a reaction network with >200 components, rationalized the variation in translation speed with growth as a manifestation of efficient protein synthesis. Together, these results confirm that scenario III can accurately describe observations over a very broad range of conditions, in strong support of the popular but often questioned presumption that E. coli optimally tunes its ribosomal content to promote fast growth (Giordano et al., 2016; Bosdriesz et al., 2015; Towbin et al., 2017).

In Appendix 1 – Application of the model to Saccharomyces cerevisiae, we present a similar analysis for yeast, which, in line with previous studies (Metzl-Raz et al., 2017; Xia et al., 2021; Paulo et al., 2015; Paulo et al., 2016; Kostinski and Reuveni, 2021), suggests that this eukaryote likely follows a similar optimal allocation strategy, although data for ribosomal content and the translation rate is scarce. The strong correlation between ribosome content and growth rate has further been reported for other microbial organisms in line with an optimal allocation (Karpinets et al., 2006; Jahn et al., 2018; Zavřel et al., 2019; Jahn et al., 2021), though the absence of translation rate measurements precludes confirmation. An interesting exception is the methanogenic archaeon Methanococcus maripaludis, which appears to maintain constant allocation, in agreement with scenario I (Müller et al., 2021). The presented analysis thus suggests that E. coli and possibly many other microbes closely follow an optimal ribosome allocation behavior to support efficient growth. Moreover, the good agreement between experiments and data establishes that a simple low-dimensional allocation model can describe growth with notable quantitative accuracy. However, this begs the question: how do cells coordinate their complex machinery to ensure optimal allocation?

### Optimal allocation results from a mutual maximization of translational and metabolic flux

To optimize the steady-state growth rate, cells must have some means of coordinating the flow of mass through metabolism and protein synthesis. In the ribosomal allocation model, this reduces to a regulatory mechanism in which the allocation parameters ($ϕ_{R⁢b}$ and $ϕ_{M⁢b}$) are dynamically adjusted such that the metabolic flux to provide new precursors ($ν⁢(c_{n⁢t})⁢ϕ_{M⁢b}$) and translational flux to make new proteins ($\gamma⁢(c_{p⁢c}^{*})⁢ϕ_{R⁢b}$, equivalent to the steady-state growth rate $\lambda$) are not only equal, but are mutually maximized. Such regulation therefore requires a mechanism by which both the metabolic and translational flux can be simultaneously sensed.

Thus far, we have referred to the end product of metabolism as ambiguous ‘precursors’ which are used by ribosomes to create new proteins. In reality, these precursors are tRNAs charged with their cognate amino acids. One can think of metabolism as a two-step process where (i) an amino acid is synthesized from environmental nutrients and (ii) an amino acid is attached to the appropriate uncharged-tRNA. As we assume that nutrients are in excess in the environment, we make the approximation that nutrients in the environment are saturating such that $c_{n⁢t}≫K_{M}^{c_{n⁢t}}$ and the metabolic rate $ν$ now depends solely on the concentration of uncharged-tRNAs $ν⁢(tRNA^{u})$. This enforces some level of regulation of metabolism; if the uncharged tRNA concentration is too low, the rate of metabolism slows and does not add to the already large pool of charged tRNA. But when charged-tRNA is available, translation occurs at a rate $\gamma⁢(tRNA^{c})$, forming new protein biomass and converting a charged-tRNA back to an uncharged state. This process is shown by gray arrows in Figure 2A.

![Figure 2.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig2-v2.jpg)

**Figure 2.:** (A) A circuit diagram of interactions between metabolic and translational fluxes with flux-parity regulatory connections highlighted in red. The fluxes are connected via a positive feedback loop through the generation of mutual starting materials (uncharged- or charged-tRNAs, respectively). The rates of each flux exhibit semi-autoregulatory behavior in that flux through each process reduces the standing pool of tRNAs. (B) The governing dynamics of the flux-parity regulatory circuit with key parameters highlighted in blue and flux-parity regulatory components highlighted in red. (C) Parameters, dimensions, values, and references for each component of the flux-parity regulatory circuit. (D) The steady-state meabolic (purple) and translational (gold) fluxes plotted as a function of the ribosomal allocation under the simple allocation model. Vertical red line indicates the steady-state solution of the flux-parity model under physiological parameter regimes. (E) The difference in allocation towards ribosomes in steady state between the flux-parity model and optimal allocation ($ϕ_{R⁢b}^{*(f⁢l⁢u⁢x-p⁢a⁢r⁢i⁢t⁢y)}-ϕ_{R⁢b}^{(I⁢I⁢I)}$) plotted as a function of the maximal metabolic rate, $ν_{m⁢a⁢x}$.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Black lines represent the steady-state growth rate as a function of the allocation towards ribosomes $ϕ_{R⁢b}$. Dashed gold and purple lines correspond to the translational and metabolic fluxes, with their intersection indicating the steady state. The different panels consider from left to right three scenarios with a too low, optimal, and too high allocation towards ribosomes. An interactive version of this figure is available on the paper website (cremerlab.github.io/flux_parity).

To describe the state-dependent adjustment of the allocation parameters ($ϕ_{R⁢b}$ and $ϕ_{M⁢b}$), we further include in this feedback loop a regulatory system we term a ‘flux-parity regulator’ (Figure 2A, red), which controls the allocation parameters in response to relative changes in the concentrations of the two tRNA species. Together, the arrows in Figure 2 represent a more fine-grained view of a proteinaceous self replicating system, yet maintains much of the structural minimalism of the simple ribosomal allocation model without requiring explicit consideration of different types of amino acids (Bosdriesz et al., 2015), inclusion of their myriad synthesis pathways (Hu et al., 2020), or reliance on observed phenomenology (Wu et al., 2022).

The boxes and arrows of Figure 2A can be mathematized to arrive at a handful of ordinary differential equations (Figure 2B) structurally similar to those in Figure 1B. At the center of this model is the ansatz that the ribosomal allocation $ϕ_{R⁢b}$ is dependent on the ratio of charged- and uncharged-tRNA pools and has the form

$$
ϕ_{R⁢b}⁢(\frac{tRNA^{c}}{tRNA^{u}})=(1-ϕ_{O})⁢\frac{\frac{tRNA^{c}}{tRNA^{u}}}{\frac{tRNA^{c}}{tRNA^{u}}+\tau},
$$

where the ratio $\frac{tRNA^{c}}{tRNA^{u}}$ represents the ‘charging balance’ of the tRNA and $\tau$ is a dimensionless sensitivity parameter which defines the charging balance at which the allocation towards ribosomes is half-maximal. Additionally, we make the assertion that the synthesis rate of new uncharged-tRNA via transcription $κ$ is coregulated with ribosomal proteins (Skjold et al., 1973; Dong et al., 1996) and has a similar form of

$$
κ⁢(\frac{tRNA^{c}}{tRNA^{u}})=κ_{m⁢a⁢x}⁢\frac{\frac{tRNA^{c}}{tRNA^{u}}}{\frac{tRNA^{c}}{tRNA^{u}}+\tau},
$$

where $κ_{m⁢a⁢x}$ represents the maximal rate of tRNA transcription relative to the total biomass.

Numerical integration of this system of equations reveals that the flux-parity regulation is capable of optimizing the allocation towards ribosomes, $ϕ_{R⁢b}$, such that the metabolic and translation fluxes are mutually maximized (Figure 2D), thus achieving optimal allocation. Importantly, the optimal behavior inherent to this regulatory mechanism can be attained across a wide range of parameter values for the charging sensitivity $\tau$ and the transcription rate $κ_{m⁢a⁢x}$, the two key parameters of flux-parity regulation (Figure 2C). Moreover, the emergent optimal behavior of this regulatory scheme occurs across conditions without the need for any fine-tuning between the flux-parity parameters and other parameters. For example, the control of allocation via flux-parity regulation matches the optimal allocation (scenario III above) when varying the metabolic rate $ν_{m⁢a⁢x}$ (Figure 2E and Appendix 1 – Parameter dependence of the flux-parity model).

The theoretical analysis presented in Figure 2 suggests that a flux-parity regulatory mechanism may be a simple way to ensure optimal ribosomal allocation that is robust to variation in the key model parameters. To test if such a scheme may be implemented in E. coli, we compared the behavior of the steady-state flux-parity regulatory circuit within physiological parameter regimes to steady-state measurements of ribosomal allocation and the translation rate as a function of the growth rate (Figure 3A and B). Remarkably, the predicted steady-state behavior of the flux-parity regulatory circuit describes the observed data with the same quantitative accuracy as the optimal behavior defined by scenario III, as indicated by the overlapping red and blue lines, respectively.

![Figure 3.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig3-v2.jpg)

**Figure 3.:** Measurements of the (A) ribosomal allocation and the (B) translation rate are plotted alongside the steady-state behavior of the flux-parity regulatory circuit (red dashed line) and the optimal behavior of scenario III (solid blue line). Points and markers are the same as those shown in Figure 1G. (C) Measurements of intracellular ppGpp concentrations relative to a reference condition ($\lambda_{0}≈1$ hr-1) are plotted as a function of growth rate alongside the prediction emergent from the flux-parity regulatory circuit (red dashed line). (D–F) Inhibition of ribosome activity via antibiotic modeled repression of translational flux. Plots show comparison with data for different media (red shades) with the flux-parity model predictions (dashed lines). (G–I) Inhibition of metabolic and translational fluxes through excess gene expression. (H) shows data where β-galactosidase is expressed at different levels. Different shades of red correspond to different growth media. Right-hand panel shows collapse of the growth rates of overexpression of β-galactosidase (squares), β-lactamase (inverted triangles), and EF-Tu (diamonds) relative to the wild-type growth rate in different media conditions. The same set of model parameters listed in Supplementary file 2 has been used to generate the predictions.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Measurements are shown for ribosomal content, translation rate, and relative ppGpp concentration from left to right, respectively. Markers are the same as those in Figure 3 of the main text. Solid blue line shows predicted steady-state behavior assuming a simple ansatz of ribosome-tRNA binding probabilities (Equation 41). Dashed red line denotes predicted behavior using the ansatz that ppGpp concentration is dependent on the charging balance.

While the flux-parity regulation scheme appears to accurately describe the behavior of E. coli, how are metabolic and translational fluxes sensed at a mechanistic level? Many bacteria, including E. coli, utilize the small molecule guanosine tetraphosphate (ppGpp) as a molecular indicator of amino acid limitation and has been experimentally shown to regulate ribosomal, metabolic, and tRNA genes through many routes, including directly binding RNA polymerase (Magnusson et al., 2005; Anderson et al., 2021; Potrykus and Cashel, 2008; Potrykus et al., 2011; Imholz et al., 2020) and plays an important role in other cellular processes, including cell size control (Büke et al., 2022). Mechanistically, ppGpp levels are enzymatically controlled depending on the metabolic state of the cell, with synthesis being triggered upon binding of an uncharged-tRNA into an actively translating ribosome. While many molecular details of this regulation remain unclear (Magnusson et al., 2005; Anderson et al., 2021; Potrykus and Cashel, 2008; Wu et al., 2022), the behavior of ppGpp meets all of the criteria of a flux-parity regulator. Rather than explicitly mathematicizing the biochemical dynamics of ppGpp synthesis and degradation, as has been undertaken previously (Bosdriesz et al., 2015; Giordano et al., 2016; Wu et al., 2022), we model the concentration of ppGpp being inversely proportional to the charging balance,

$$
[ppGpp]∝\frac{tRNA^{u}}{tRNA^{c}},
$$

encompassing the fact that processes beyond allocation use ppGpp as an effector molecule. This ratio, mathematically equivalent to the odds of a ribosome binding an uncharged-tRNA relative to binding a charged-tRNA, is one example of a biochemically motivated ansatz that can be considered (‘Methods’) and provides a relative measure of the metabolic and translational fluxes.

With this approach, the amount of ppGpp present at low growth rates, and therefore low ribosomal allocation, should be significantly larger than at fast growth rates where ribosomal allocation is larger and charged-tRNA are in abundant supply. While our model cannot make predictions of the absolute ppGpp concentration, we can compute the relative ppGpp concentration to a reference state [ppGpp]0 as

$$
\frac{[ppGpp]}{[ppGpp]_{0}}=\frac{(tRNA^{u}/tRNA^{c})}{(tRNA_{0}^{u}/tRNA_{0}^{c})}.
$$

To test this, we compiled and rescaled ppGpp measurements of E. coli across a range of growth rates from various literature sources (Figure 3C and Figure 3—source data 1). The quantitative agreement between the scaling predicted by Equation 4 and the experimental measurements strongly suggests that ppGpp assumes the role of a flux sensor and enforces optimal allocation through the discussed flux-parity mechanism.

### The flux-parity allocation model predicts E. coli growth behavior in and out of steady state

We find that the flux-parity allocation model is extremely versatile and allows us to quantitatively describe aspects of microbial growth in and out of steady state and under various physiological stresses and external perturbations with the same core set of parameters. Here, we demonstrate this versatility by comparing predictions to data for four particular examples using the same self-consistent set of parameters we have used thus far (Supplementary file 1). First, we examine the influence of translation-targeting antibiotics like chloramphenicol (Figure 3D) on steady-state growth in different growth media (Scott et al., 2010; Dai et al., 2016). By incorporating a mathematical description of ribosome inactivation via binding to chloramphenicol (described in ‘Methods’), we find that the flux-parity allocation model quantitatively predicts the change in steady-state growth and ribosomal content with increasing chloramphenicol concentration (Figure 3E, red shades). Furthermore, the effect on the translation speed is qualitatively captured (Figure 3F, red shades). The ability of the flux-parity allocation model to describe these effects without readjustment of the model and its core parameters is notable and provides a mechanistic rationale for previously established phenomenological relations (Scott et al., 2010; Dai et al., 2016).

As a second perturbation, we consider the burden of excess protein synthesis by examining the expression of synthetic genes (Figure 3G). A decrease in growth rate results when cells are forced to synthesize different amounts of the lactose cleaving enzyme $\beta$-galactosidase in different media lacking lactose (Figure 3H, red shades). The flux-parity allocation model (dashed lines) quantitatively predicts the change in growth rate with the measured fraction of $\beta$-galactosidase without further fitting (‘Methods’). The trends for different media (red shades) quantitatively collapse onto a single line (Figure 3I and Figure 3—source data 2) when comparing changes in relative growth rates, a relation which is also captured by the model (dashed black line) and is independent of the overexpressed protein (symbols). This collapse, whose functional form is derived in ‘Methods,’ demonstrates that the flux-parity allocation model is able to describe excess protein synthesis in general, rather than at molecule- or media-specific level.

As the flux-parity regulatory circuit responds to changes in the metabolic and translational fluxes, it can be used to explore behavior in changing conditions. Consider a configuration where the starting conditions of a culture are tuned such that the ribosomal allocation $ϕ_{R⁢b}$, the tRNA charging balance $tRNA^{c}/tRNA^{u}$, and the ribosome content $M_{R⁢b}/M$ are set to be above or below the appropriate level for steady-state growth in the environment (Figure 4A). As the culture grows, the observed ribosomal content $M_{R⁢b}/M$ is steadily adjusted until the steady-state level is met where it directly matches the optimal allocation (Figure 4B). This adaptation of the ribosomal content is controlled by dynamic adjustment of the allocation parameters via the flux-parity regulatory circuit (Figure 4C). To further test the flux-parity allocation model, we examine how accurately this system can predict growth behavior under nutritional shifts (Figure 4D–F) and the entry to starvation (Figure 4G–I).

![Figure 4.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig4-v2.jpg)

**Figure 4.:** (A) Hypothetical initial configurations of model parameters and variables before begining numerical integration. (B) The equilibration of the ribosomal protein content ($M_{R⁢b}/M$). (C) Dynamic adjustment of the ribosomal allocation parameter in response to the new environment. Green and purple colored lines correspond to the initial conditions of the culture from well above to well below the steady-state values, respectively. Dashed red line indicates the steady-state solution. (D, E) Nutrient upshifts with increased metabolic flux. (E) The instantaneous growth rate $\lambda_{i}$ for shifts from succinate to gluconate (bright red), xylose (dark red), or arabinose (black) (Erickson et al., 2017). (F) Collapse of instantaneous growth rate measurements immediately after the shift (relative to the preshift-growth rate) as a function of the total shift magnitude. (G–I) Exhaustion of nutrients in the environment yields a decrease in the metabolic flux, promoting expression of more metabolic proteins. (H) Growth curve measurements in media with different starting concentrations of glucose (0.22 mM, 0.44 mM, and 1.1 mM glucose from light to dark, respectively) overlaid with flux-parity predictions. (I) The change in total metabolic protein synthesis in the flux-parity model (dashed lines) overlaid with the change in expression of a fluorescent reporter from a PtsG promoter (solid lines).

We first consider a nutrient shift where externally supplied low-quality nutrients are instantaneously exchanged with rich nutrients. Figure 4E shows three examples of such nutritional upshifts (markers), all of which are well described by the flux-parity allocation theory (dashed lines). The precise values of the growth rates before, during, and after the shift will depend on the specific carbon sources involved. However, by relating the growth rates before and immediately after the shift to the total shift magnitude (as shown in Korem Kohanim et al., 2018), one can collapse a large collection of data onto a single curve (Figure 4F, markers). The collapse emerges naturally from the model (dashed line) when decomposing the metabolic sector into needed and non-needed components (‘Methods’), demonstrating that the flux-parity allocation model is able to quantitatively describe nutritional upshifts at a fundamental level.

Finally, we consider the growth dynamics during the onset of starvation, another non-steady-state phenomenon (Figure 4G–I). Figure 4H shows the growth of batch cultures where glucose is provided as the sole carbon source in different limiting concentrations (Bren et al., 2013) (markers). The cessation of growth coincides with a rapid, ppGpp-mediated increase in expression of metabolic proteins (Magnusson et al., 2005; Dennis et al., 2004). Bren et al., 2013 demonstrated that expression from a glucose-specific metabolic promoter (PtsG) rapidly, yet temporarily, increases with the peak occurring at the moment where growth abruptly stops (Figure 4I, solid gray lines). The flux-parity allocation model again predicts this behavior (Figure 4I, red lines) without additional fitting (‘Methods’), cementing the ability of the model to describe growth far from steady state.

## Discussion

Microbial growth results from the orchestration of an astoundingly diverse set of biochemical reactions mediated by thousands of protein species. Despite this enormous complexity, experimental and theoretical studies alike have shown that many growth phenotypes can be captured by relatively simple correlations and models which incorporate only a handful of parameters (Schaechter et al., 1958; Molenaar et al., 2009; Scott et al., 2010; Scott et al., 2014; Erickson et al., 2017; Korem Kohanim et al., 2018; Bosdriesz et al., 2015; Giordano et al., 2016; Dai et al., 2016). Through re-examination of these works, we relax commonly invoked approximations and assumptions, include a generalized description of global regulation, and integrate an extensive comparison with data to establish a self-consistent, low-dimensional model of protein synthesis that is capable of quantitatively describing complex growth behaviors in and out of steady state.

Growth emerges as in previous allocation models (Molenaar et al., 2009; Scott et al., 2010; Giordano et al., 2016) as a consequence of protein synthesis and the allocation of ribosome activity towards (i) making new ribosomes, (ii) making the metabolic proteins which sustain the precursors ribosomes require to translate, and (iii) making other proteins cells require to operate. An optimal allocation which yields the fastest growth in a given condition is reached when the synthesis of precursors (metabolic flux) and the consumption of precursors (translational flux) are mutually maximized, a process we term flux-parity regulation. We analyze how such regulation can be mechanistically achieved by the relative sensing of charged- and uncharged-tRNA via the abundance of a global regulator (such as ppGpp) which diametrically affects the expression of ribosomal and metabolic genes. Through extensive comparison with 61 data sets from 46 studies, we show that the flux-parity model predicts the fundamental growth behavior of E. coli with quantitative accuracy. Beyond describing the growth-rate dependent ribosomal content and translation speed for steady growth across various carbon sources, the flux-parity model quantitatively captures phenomena out of steady state (including nutrient upshifts and response to starvation) and under externally applied physiological perturbations (such as antibiotic stress or expression of synthetic genes). Notably, the broad agreement across data sets is obtained using a single core parameter set which does not require any adjustment from one scenario to the next. As such, the flux-parity model predicts the microbial ‘growth laws,’ providing a mechanistic explanation for previous phenomenological models formulated to understand them (Scott et al., 2010; Scott et al., 2014; Molenaar et al., 2009). The finding that these predictions hold so well despite the overwhelmingly complex nature of the cell further highlights that biological systems are not irreducibly complex but can be distilled to a small number of fundamental components sufficient to capture the core behavior of the system.

As proteins commonly account for the majority of biomass in microbial organisms and the core processes of protein synthesis are universally conserved among them, it is likely that protein synthesis is a fundamental growth constraint across many organisms. Accordingly, flux-parity regulation may be a very general scheme which ensures the efficient coordination of metabolic and translational fluxes across many microbial organisms. And as our modeling approach is organism agnostic, it should be transferable to a variety of microbes growing in nutrient-replete conditions. Indeed, other organisms including S. cerevisiae exhibit a strict interdependence between growth rate and ribosome content (Karpinets et al., 2006; Metzl-Raz et al., 2017), as is predicted by the flux-parity model. However, more quantitative data on ribosomal content, translation speeds, upshift dynamics, and more need to be acquired to fully examine the commonality of flux-parity regulation in the microbial world.

A common interpretation of previous allocation models is that cells maximize their growth rate in whatever conditions they encounter (Bosdriesz et al., 2015; Towbin et al., 2017). Rather, we believe flux-parity regulation only ensures optimal coordination between metabolic and translational fluxes. It does not imply that the growth rate itself is maximized or directly sensed. In particular, the flux-parity model does not assume that the pool of metabolic proteins is tailored to maximize the metabolic flux and thus growth in the encountered conditions. This is in agreement with an expanding body of evidence which shows that microbes frequently synthesize metabolic and other proteins which are not directly needed in the encountered condition and thus impede growth. E. coli, for example, synthesizes a plethora of different transport proteins when exposed to poor growth conditions even if the corresponding substrates are not available, collectively occupying a significant portion of the proteome (Belliveau et al., 2021; Schmidt et al., 2016; Hui et al., 2015; Balakrishnan et al., 2021a). Accordingly, it has been observed that cells stop synthesizing these proteins when evolving over many generations in the absence of those sugars (Leiby and Marx, 2014; Favate et al., 2021).

But why, then, do we observe an optimal allocation between metabolic and ribosomal proteins when the pool of metabolic proteins itself shows this apparent non-optimal behavior? We posit here that both behaviors emerge from the adaptation to fluctuating conditions: in contrast to the well-defined static conditions of laboratory experiments, the continuous ebb and flow of nutrients in natural environments precludes any sense of stability. Accordingly, the machinery of the cell should be predominantly adapted to best cope with the fluctuating conditions microbial organisms encounter in their natural habitats (Koch, 1971). A complex regulation of metabolic proteins is thus expected, including, for example, the diverse expression of nutrient transporters which promote growth in anticipated conditions, rather than synthesizing only those specific to nutrients that are present in the moment (Balakrishnan et al., 2021a).

However, in those fluctuating conditions, flux-parity regulation promotes rapid growth. To illustrate this point, we consider again a nutrient upshift in which there is an instantaneous improvement in the nutrient conditions. We compare the predicted response via flux-parity (Figure 5A, red box) with that predicted by a simpler step-wise regulation where the allocation solely depends on the environmental condition (and not the internal fluxes) and immediately adjusts to the new steady value at the moment of the shift (Figure 5A, blue box). The dynamic reallocation by flux-parity facilitates a sharp increase in the allocation towards ribosomes (Figure 5B), resulting in a rapid increase in instantaneous growth rate compared to the step-wise reallocation mechanism (Figure 5C), suggesting that flux-parity is advantageous in fluctuating environments. As its regulation solely depends on the internal state of the cell (particularly, the relative abundance of charged- to uncharged-tRNA), it holds independently of the encountered conditions. This stands in contrast to the regulation of metabolic proteins, where both the external and internal states dictate what genes are expressed. As a result, optimal coordination between metabolic and translational fluxes occurs ubiquitously across conditions and not only in those that occur in natural habitats and drive adaptation. These broader conditions include steady-state growth within the laboratory, with the ‘growth laws’ observed under those conditions emerging as a serendipitous consequence.

![Figure 5.](https://cdn.elifesciences.org/articles/84878/elife-84878-fig5-v2.jpg)

**Figure 5.:** (A) Ribosome reallocation strategies upon a nutrient upshift. After a nutrient upshift, cells either dynamically reallocate their ribosomes given flux-parity regulation (top, red) or they undergo stepwise reallocation from one steady-state value to the next (bottom, blue). (B) The allocation dynamics for both strategies in response to a nutrient upshift. (C) The instantaneous growth rate for both strategies over the course of the shift. Dashed red and solid blue lines correspond to model predictions for optimal allocation and flux-parity regulation, respectively. (D) Cellular decision making in fluctuating environments. Upon sensing features of the environment, cells undergo a two-component decision making protocol defining what metabolic genes should be expressed (top) and how the allocation towards ribosomes should be adjusted to maintain flux-parity. The combination of these processes yield an increase of biomass at a given characteristic growth rate.

In summary, we view the process of cellular decision making as having two major components (Figure 5D): (i) determining what metabolic genes should be expressed given the environmental and physiological state and (ii) determining how ribosomes should be allocated given the metabolic and translational fluxes. Flux-parity regulation can explain the latter but many details of the former remain enigmatic. Additional studies are thus required to understand how the regulation of metabolic genes depends on encountered conditions and how it is shaped by adaptation to specific habitats. However, the ability of this theory to predict complex phenotypes across scales suggests that it can also act as a basis to answer these questions, and thereby galvanize an integrative understanding of microbial life connecting physiology, ecology, and evolution.

## Methods

### Formulating the allocation model

Here we present a step-by-step derivation of the low-dimensional allocation model we use to describe bacterial growth. We provide additional biological motivation for its construction and highlight the different assumptions and simplifications invoked. To maintain consistency with the literature, we largely follow the notational scheme introduced by Scott et al., 2014 and define each symbol as it is introduced.

### Synthesis of proteins

The rate of protein synthesis is determined by two quantities: the total number of ribosomes $N_{R⁢b}$ and the speed $v_{t⁢l}$ at which they are translating. The latter depends on the concentration of precursors needed for peptide bond formation, such as tRNAs, free amino acids, and energy sources like ATP and GTP. Taking the speed $v_{t⁢l}$ as a function of the concentration of the collective precursor pool $c_{p⁢c}$, the increase in protein biomass $M$ follows as

$$
\frac{d⁢M}{d⁢t}=v_{t⁢l}⁢(c_{p⁢c})⁢N_{R⁢b}.
$$

There exists a maximal speed at which ribosomes can operate, $v_{t⁢l}^{m⁢a⁢x}$, that is reached under optimal conditions when precursors are highly abundant, in E. coli approximately 20 amino acids (AA)/second (s) (Forchhammer and Lindahl, 1971). Conversely, the translation speed falls when precursor concentrations $c_{p⁢c}$ get sufficiently small. Simple biochemical considerations support a Michaelis–Menten relation (Ehrenberg and Kurland, 1984; Klumpp et al., 2013; Belliveau et al., 2021) as good approximation of this behavior with the specific form

$$
v_{t⁢l}⁢(c_{p⁢c})=v_{t⁢l}^{m⁢a⁢x}⁢(\frac{c_{p⁢c}}{c_{p⁢c}+K_{M}^{c_{p⁢c}}}),
$$

where $K_{M}^{c_{p⁢c}}$ is a Michaelis–Menten constant with the maximum speed $v_{t⁢l}^{m⁢a⁢x}$ only observed for $c_{p⁢c}≫K_{M}^{c_{p⁢c}}$. The number of ribosomes $N_{R⁢b}$ can be approximated given knowledge of the total mass of ribosomal proteins $M_{R⁢b}$ and the proteinaceous mass of a single ribosome $m_{R⁢b}$ via $N_{R⁢b}≈M_{R⁢b}/m_{R⁢b}$ (more details in Appendix 1 Estimating the number of ribosomes within the cell). The increase in protein biomass (Equation 5) is thus

$$
\frac{d⁢M}{d⁢t}=v_{t⁢l}⁢(c_{p⁢c})⁢\frac{M_{R⁢b}}{m_{R⁢b}}≡\gamma⁢(c_{p⁢c})⁢M_{R⁢b}.
$$

The translation rate$\gamma⁢(c_{p⁢c})≡v_{t⁢l}⁢(c_{p⁢c})/m_{R⁢b}$ describes the rate at which ribosomes generate new protein.

The maximal translation rate $\gamma_{m⁢a⁢x}≡v_{t⁢l}^{m⁢a⁢x}/m_{R⁢b}$ imposes a firm upper limit (Dill et al., 2011; Belliveau et al., 2021; Kafri et al., 2016) of how rapidly biomass can accumulate, unrealistically assuming the system would consist of only ribosomes translating at maximum rate. Notably, however, this upper limit is not much faster than the fastest growth observed, highlighting the importance of protein synthesis in defining the timescale of growth. For example, the maximal translation rate for E. coli is ≈ 10 hr-1 and thus only ≈4 times higher than the growth rates in rich LB media ($\lambda≈2.5$ hr-1). Including the synthesis of rRNA, another major component of the cellular dry mass, lowers this theoretical limit only marginally (Kostinski and Reuveni, 2020), further supporting our sole consideration of protein synthesis in defining growth. The difference between measured growth rates and the theoretical limits can be mostly attributed to the synthesis of metabolic proteins which generate the precursors required for protein synthesis, which we consider next.

### Synthesis of precursors

Microbial cells are generally capable of synthesizing precursors from nutrients available in the environment, such as sugars or organic acids. This synthesis is undertaken by a diverse array of metabolic proteins ranging from those which transport nutrients across the cell membrane, to the enzymes involved in energy generation (such as those of fermentation or respiration), and the enzymes providing the building blocks for protein synthesis (such as those involved in the synthesis of amino acids). While these enzymes vary in their abundance and kinetics, we group them all into single set of metabolic proteins with a mass $M_{M⁢b}$ which cooperate to synthesize the collective pool of precursors from nutrients required for protein synthesis. We make the approximation that these metabolic proteins generate precursors at an effective metabolic rate $ν$. In general, this rate depends on the concentration of nutrients $c_{n⁢t}$ in the environment. This relation is canonically described by a Monod (Michaelis–Menten) relation

$$
ν⁢(c_{n⁢t})=ν^{m⁢a⁢x}⁢(\frac{c_{n⁢t}}{c_{n⁢t}+K_{M}^{c_{n⁢t}}}),
$$

where $ν_{m⁢a⁢x}$ is the maximum metabolic rate describing how fast the metabolic proteins can synthesize precursors, and $K_{M}^{c_{n⁢t}}$ is the Monod constant describing the concentration below which nutrient utilization slows (Monod, 1949). Novel precursors are thus supplied with a total rate of $ν⁢(c_{n⁢t})⁢M_{M⁢b}$ and consumed via protein synthesis at a rate $\gamma⁢(c_{p⁢c})⁢M_{R⁢b}$. Translation relies on precursors and, as introduced above, the translation rate $\gamma⁢(c_{p⁢c})⁢M_{R⁢b}$ thus depends on the concentration of precursors in the cell, $c_{p⁢c}$. As we do not explicitly model cell division, we here approximate this cellular concentration as the relative mass abundance of precursors to total protein biomass. This approximation is justified by the observation that cellular mass density and total protein content is approximately constant across a wide range of conditions (Belliveau et al., 2021; Martínez-Salas et al., 1981; Kubitschek et al., 1983). The dynamics of precursor concentration follows from the balance of synthesis, consumption, and dilution as the total biomass grows:

$$
\frac{dc_{pc}}{dt}=\frac{ν(c_{nt})M_{Mb}}{M}⏞production via metabolism−\frac{\gamma(c_{pc})M_{Rb}}{M}⏟consumption via protein synthesis−\frac{c_{pc}\gamma(c_{pc})M_{Rb}}{M}⏞dilution via growth.
$$

While the dilution term is often assumed to be negligible, this term is critical to describe growth and derive analytical expressions. Furthermore, we note that the precursor concentration is defined such that the consumption of one precursor yields the addition of one amino acid to the biomass $M$. As we measure proteins in units of amino acids, there is thus no conversion factor needed when describing the consumption of precursors by protein synthesis.

### Simplification of saturating nutrients

The introduced dynamics simplifies when the nutrient concentration in the environment $c_{n⁢t}$ well exceeds the Monod constant $K_{M}^{c_{n⁢t}}$ as $ν⁢(c_{n⁢t})$ simplifies to $ν_{m⁢a⁢x}$. Steady growth for which biomass increases exponentially readily emerges. This is the scenario we focus on in in the first half of this work. It should be noted, however, that biologically such a scenario can only be realized temporarily as the nutrient supply required by the exponentially growing biomass can only be sustained by the environment for a limited amount of time. In general, the nutrient levels vary.

### Consumption of nutrients in batch culture growth

The synthesis of novel precursors relies on the availability of nutrients which changes depending on the environment. In Figure 1—figure supplement 2, we consider specifically a ‘batch culture’ scenario in which nutrients are provided only at the beginning of growth and are never replenished. Therefore, growth of the culture continues until all of the nutrients have been consumed. The concentration of nutrients in the environment is thus given as

$$
\frac{d⁢c_{n⁢t}}{d⁢t}=-\frac{ν⁢(c_{n⁢t})⁢M_{M⁢b}}{Y},
$$

where $Y$ is the yield coefficient which describes how many nutrient molecules are needed to produce one unit of precursors.

### Ribosomal allocation of protein synthesis

As final step of the model definition, we must describe how cells direct their protein synthesis towards making ribosomes, metabolic proteins, or all other proteins that make up the cell (colored arrows in Figure 1A). We do so by introducing three allocation parameters $ϕ_{R⁢b}$, $ϕ_{M⁢b}$, and $ϕ_{O}$ (such that $ϕ_{R⁢b}+ϕ_{M⁢b}+ϕ_{O}=1$) which define how novel protein synthesis is partitioned among these categories:

$$
\frac{dM_{Rb}}{dt}=ϕ_{Rb}\frac{dM}{dt};\frac{dM_{Mb}}{dt}=ϕ_{Mb}\frac{dM}{dt};\frac{dM_{O}}{dt}=ϕ_{O}\frac{dM}{dt}.
$$

These equations are summarized in Figure 1B and Figure 1, Figure 1—figure supplement 2 and define the accumulation of biomass, from nutrient uptake to protein synthesis.

### Approximating concentration via relative abundance

In addition to maintaining the total macromolecular densities, cells also maintain an approximately constant protein density (Bremer and Dennis, 2008). This observation allows for a major simplification when formulating the allocation model, namely the approximation of concentrations as relative mass abundances. The rate $\gamma$ at which ribosomes can synthesize protein is dependent on the abundance of precursors, $c_{p⁢c}$, in the cell. To compute the concentration and/or density in typical units (e.g. µM, or mass/volume), we would require some measure of the total cellular volume, $V_{c⁢e⁢l⁢l}$, such that the concentration follows

$$
c_{p⁢c}=\frac{M_{p⁢c}}{V_{c⁢e⁢l⁢l}},
$$

with $M_{p⁢c}$ denoting the total mass of the precursor pool. By making the experimentally supported assertion that the protein density $ρ$ is constant, we can say that

$$
ρ=\frac{M}{V_{c⁢e⁢l⁢l}}=Constant,
$$

where $M$ is the total protein biomass. Thus, the total cellular volume $V_{c⁢e⁢l⁢l}$ can be computed as

$$
V_{c⁢e⁢l⁢l}=\frac{M}{ρ}.
$$

Plugging this result into Equation 12, we arrive at the approximation

$$
c_{p⁢c}=ρ⁢\frac{M_{p⁢c}}{M}≈\frac{M_{p⁢c}}{M}.
$$

In this work, we neglect $ρ$ as a multiplicative constant and treat $c_{p⁢c}$ as being dimensionless. We direct the reader to Scott et al., 2010 and Milo, 2013 for a further discussion of the conversion between concentration and relative abundance.

### Derivation of analytical expressions

In the first section of this work, we present several analytical relations pertinent to steady-state growth. These relations follow from the simple allocation model and describe (i) how the growth rate depends on model parameters (Figure 1C) and (ii) how ribosome content depends on other model parameters for the three different regulation scenarios we discuss (Figure 1F). Here, we introduce a step-by-step derivation of these expressions.

### Deriving the steady-state growth rate

We begin with deriving an expression for the steady-state growth rate $\lambda$ which is similar to previous approaches taken by Giordano et al., 2016 and Dourado and Lercher, 2020. As discussed in Figure 1—figure supplement 2, steady-state conditions are satisfied when two conditions are met. First, the dynamics of the precursor concentration is constant (i.e., $\frac{d⁢c_{p⁢c}}{d⁢t}=0$) and the composition of the proteome matches the allocation parameters (i.e., $\frac{M_{R⁢b}^{*}}{M^{*}}=ϕ_{R⁢b}^{*}$ and $\frac{M_{M⁢b}^{*}}{M^{*}}=ϕ_{M⁢b}^{*}$). Furthermore, we assume that in steady-state growth, the concentration of nutrients in the environment is saturating ($c_{n⁢t}≫K_{M}^{c_{n⁢t}}$), meaning that $ν⁢(c_{n⁢t})≈ν_{m⁢a⁢x}$. With these conditions satisfied, we can rewrite Equation 9 as

$$
\frac{d⁢c_{p⁢c}}{d⁢t}=ν_{m⁢a⁢x}⁢ϕ_{M⁢b}-\gamma⁢(c_{p⁢c}^{*})⁢ϕ_{R⁢b}-c_{p⁢c}⁢\gamma⁢(c_{p⁢c}^{*})⁢ϕ_{R⁢b}=0,
$$

where $c_{p⁢c}^{*}$ is the steady-state precursor concentration.

Noting that in steady-state conditions the total biomass increases exponentially at a rate $\lambda≡\gamma⁢(c_{p⁢c})⁢ϕ_{R⁢b}^{*}$, Equation 16 can be simplified to

$$
\frac{d⁢c_{p⁢c}}{d⁢t}=ν_{m⁢a⁢x}⁢ϕ_{M⁢b}^{*}-\lambda⁢(1+c_{p⁢c})=0.
$$

We can therefore solve for the steady-state precursor concentration $c_{p⁢c}^{*}$ to yield

$$
c_{p⁢c}^{*}=\frac{ν_{m⁢a⁢x}⁢ϕ_{M⁢b}^{*}}{\lambda}-1.
$$

Assuming a Michaelis–Menten form for the translation rate $\gamma⁢(c_{p⁢c}^{*})$, we can now define it as a function of the growth rate $\lambda$ as

$$
\gamma⁢(c_{p⁢c}^{*})=\frac{\gamma_{m⁢a⁢x}}{1+\frac{K_{M}^{c_{p⁢c}}}{c_{p⁢c}}}=\frac{\gamma_{m⁢a⁢x}}{1+\frac{K_{M}^{c_{p⁢c}}⁢\lambda}{ν_{m⁢a⁢x}⁢ϕ_{M⁢b}^{*}-\lambda}}.
$$

Knowing that the growth rate $\lambda≡\gamma⁢(c_{p⁢c^{*}})⁢ϕ_{R⁢b}^{*}$, and $ϕ_{M⁢b}^{*}=1-ϕ_{R⁢b}^{*}-ϕ_{O}^{*}$, we say that

$$
\lambda=\frac{\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}}{1+\frac{K_{M}^{c_{p⁢c}}⁢\lambda}{ν_{m⁢a⁢x}⁢(1-ϕ_{R⁢b}^{*}-ϕ_{O}^{*})-\lambda}}.
$$

This can be algebraically manipulated to yield a quadratic equation of the form

$$
\lambda^{2}⁢(1-K_{M}^{c_{p⁢c}})+\lambda⁢(ν_{m⁢a⁢x}⁢(1-ϕ_{R⁢b}^{*}-ϕ_{O}^{*})+\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*})-\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}⁢ν_{m⁢a⁢x}⁢(1-ϕ_{R⁢b}^{*}-ϕ_{M⁢b}^{*})=0,
$$

which has one positive root of

$$
\lambda=\frac{ν_{m⁢a⁢x}⁢(1-ϕ_{R⁢b}^{*}-ϕ_{O}^{*})+\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}-\sqrt{(ν_{m⁢a⁢x}⁢(1-ϕ_{R⁢b}^{*}-ϕ_{O}^{*})+\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*})^{2}-4⁢(1-K_{M}^{c_{p⁢c}})⁢\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}⁢ν_{m⁢a⁢x}⁢(1-ϕ_{R⁢b}^{*}-ϕ_{O}^{*})}}{2⁢(1-K_{M}^{c_{p⁢c}})}.
$$

For notational simplicity, we can define the maximum metabolic output and the maximum translational output as $N=ν_{max}(1−ϕ_{Rb}−ϕ_{O})$ and $Γ=\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}$, respectively, and substitute them into Equation 22 to generate

$$
\lambda=\frac{N+Γ−\sqrt{(N+Γ)^{2}−4(1−K_{M}^{c_{pc}})NΓ}}{2(1−K_{M}^{c_{pc}})},
$$

#### Defining ϕR⁢b for scenarios II and III

In Figure 1F, we provide a description of three plausible regulatory scenarios microbes may employ to regulate their ribosomal content. Scenario I assumes just a constant, arbitrary allocation parameter $ϕ_{R⁢b}\in[0,1-ϕ_{O}]$. Here, we provide a short derivation for the more complicated relations describing ribosomal content under scenarios II and III.

#### Scenario II: Constant translation rate

The second regulatory scenario assumes that the ribosomal content is adjusted to maintain a specific standing concentration of precursors, which we denote as $c_{p⁢c}^{*}$. Noting that the growth rate $\lambda≡\gamma⁢(c_{p⁢c}^{*})⁢ϕ_{R⁢b}^{*}$, we can restate Equation 18 in the form

$$
c_{p⁢c}^{*}=\frac{ν_{m⁢a⁢x}⁢(1-ϕ_{O}^{*}-ϕ_{R⁢b}^{*})⁢(c_{p⁢c}^{*}+K_{M}^{c_{p⁢c}})}{c_{p⁢c}^{*}⁢\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}}.
$$

Some algebraic rearrangement allows us to solve for $ϕ_{R⁢b}^{*}$, yielding

$$
ϕ_{R⁢b}=\frac{(1-ϕ_{O}^{*})⁢ν_{m⁢a⁢x}⁢(c_{p⁢c}^{*}+K_{M}^{c_{p⁢c}})}{ν_{m⁢a⁢x}⁢(c_{p⁢c}^{*}+K_{M}^{c_{p⁢c}})+\gamma_{m⁢a⁢x}⁢c_{p⁢c}^{*}⁢(c_{p⁢c}^{*}+1)}.
$$

This expression is equivalent to that shown for scenario II in Figure 1F. In evaluating this scenario, we considered the regime in which precursors were in abundance, meaning $c_{p⁢c}^{*}≫K_{M}^{c_{p⁢c}^{*}}$. Under this regime, Equation 25 simplifies further to

$$
ϕ_{R⁢b}^{*}≈\frac{(1-ϕ_{O}^{*})⁢ν_{m⁢a⁢x}}{\gamma_{m⁢a⁢x}⁢(c_{p⁢c}^{*}+1)+ν_{m⁢a⁢x}}.
$$

This represents a strategy where the cell adjusts $ϕ_{R⁢b}^{*}$ to maintain a translation rate very close to $\gamma_{m⁢a⁢x}$.

#### Scenario III: Optimal allocation

In this work, we define the optimal allocation of ribosomes $ϕ_{R⁢b}^{*}$ to be that which maximizes the growth rate in a given environment and at a given metabolic state. To determine the optimal $ϕ_{R⁢b}^{*}$, we can differentiate Equation 22 with respect to $ϕ_{R⁢b}^{*}$ to yield the cumbersome expression

$$
\frac{\partial⁡\lambda}{\partial⁡ϕ_{R⁢b}^{*}}=\frac{1}{2⁢(1+K_{M}^{c_{p⁢c}})}\times
$$



$$
[\gamma_{m⁢a⁢x}-ν_{m⁢a⁢x}-\frac{2⁢\gamma_{m⁢a⁢x}⁢ν_{m⁢a⁢x}⁢(1-K_{M}^{c_{p⁢c}})⁢(2⁢ϕ_{R⁢b}^{*}+ϕ_{O}^{*}-1)+(\gamma_{m⁢a⁢x}-ν_{m⁢a⁢x})⁢(\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}+ν_{m⁢a⁢x}⁢(1-ϕ_{O}^{*}-ϕ_{R⁢b}^{*}))}{\sqrt{(\gamma_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}+ν_{m⁢a⁢x}⁢(1-ϕ_{O}^{*}-ϕ_{R⁢b}^{*}))^{2}-4⁢(1-K_{M}^{c_{p⁢c}})⁢\gamma_{m⁢a⁢x}⁢ν_{m⁢a⁢x}⁢ϕ_{R⁢b}^{*}⁢(1-ϕ_{O}^{*}-ϕ_{R⁢b}^{*})}}].
$$

Setting this expression equal to zero and solving for $ϕ_{R⁢b}$ results in

$$
ϕ_{R⁢b}=\frac{(1-ϕ_{O}^{*})⁢(\gamma_{m⁢a⁢x}⁢ν_{m⁢a⁢x}⁢(1-2⁢K_{M}^{c_{p⁢c}})+ν_{m⁢a⁢x}^{2}+\sqrt{K_{M}^{c_{p⁢c}}⁢\gamma_{m⁢a⁢x}⁢ν_{m⁢a⁢x}}⁢(\gamma_{m⁢a⁢x}-ν_{m⁢a⁢x}))}{(\gamma_{m⁢a⁢x}+ν_{m⁢a⁢x})^{2}-4⁢K_{M}^{c_{p⁢c}}⁢\gamma_{m⁢a⁢x}⁢ν_{m⁢a⁢x}}
$$

which is the optimal allocation towards ribosomes as presented in Figure 1F.

### Implementing flux-parity regulation via ppGpp

Here we expand upon and derive the equations defining the flux-parity allocation model shown schematically in Figure 2A and explore its dependence on parameter values.

#### Formulation of model

To include ppGpp signaling into the ribosomal allocation model, we must perform two tasks. First, we must explicitly model the dynamics of both charged- and uncharged-tRNAs. Secondly, we must tie the relative abundances of these tRNAs to the allocation parameters such that when charged-tRNAs are limiting and uncharged-tRNAs in abundance, the system reacts by adjusting the allocation parameters towards ribosomal proteins and away from metabolic proteins ($ϕ_{R⁢b}$ and $ϕ_{M⁢b}$).

We consider there to be two pools of tRNAs: those charged with an amino acid (denoted as $t⁢R⁢N⁢A^{c}$) and those that are uncharged ($t⁢R⁢N⁢A^{u}$). Rather than keeping track of the copy numbers of these tRNAs, we instead model their concentration as relative mass abundances (relative to the total protein biomass $M$), treating each tRNA to have an effective mass of one amino acid as each tRNA can in principle be charged. Much as for consideration of precursors in the simpler model we can model the concentration dynamics of these pools of tRNAs by considering three processes: the generation of the tRNAs, the consumption of the tRNAs, and the effect of dilution as the biomass grows.

We begin first with modeling the dynamics of the charged-tRNA pool, $t⁢R⁢N⁢A^{c}$. Here, we consider that charged-tRNAs are synthesized from one free amino acid and one uncharged-tRNA and further assume that the pool of free amino acids is abundant enough such that the tRNA pool is the rate limiting component. Making this assumption allows us to state that the conversion of one uncharged-tRNA to one charged-tRNA via the metabolic machinery proceeds at a rate $ν⁢(t⁢R⁢N⁢A^{u})$, itself dependent on the uncharged-$tRNA^{u}$ concentration. Likewise, we consider that the conversion of one charged-tRNA to an uncharged-tRNA is only possible via protein synthesis, which proceeds at a rate $\gamma⁢(t⁢R⁢N⁢A^{c})$ that is dependent on the charged-$tRNA$ concentration. Finally, we must also consider how the mere fact of growing biomass effectively dilutes the charged-tRNA concentration. Together, these processes can be combined to enumerate the dynamics of the charged-tRNA pool as

$$
\frac{dtRNA^{c}}{dt}=\frac{ν(tRNA^{u})M_{Mb}}{M}⏞generation via metabolism−\frac{\gamma(tRNA^{c})M_{Rb}}{M}⏟consumption via protein synthesis−\frac{tRNA^{c}\gamma(tRNA^{c})M_{Rb}}{M}⏞reduction via dilution.
$$

The dynamics for the pool of uncharged-tRNAs can be constructed in a similar manner, with the caveat that the generation of new uncharged-tRNAs occurs from both protein synthesis (converting one charged-tRNA into one uncharged-$t⁢R⁢N⁢A^{u}$) and from transcription of the individual tRNA genes. We consider the latter to occur at a rate $κ$, which has dimensions of concentration per unit time. Using the same logic of mapping the productive and consumptive processes, we can enumerate the dynamics of the uncharged-tRNA pool as

$$
\frac{dtRNA^{u}}{dt}=κ⏞production via transcription+\frac{\gamma(tRNA^{c})M_{Rb}}{M}⏟occurance via protein synthesis−\frac{ν(tRNA^{u})M_{Mb}}{M}⏞consumption via metabolism−\frac{tRNA\gamma(tRNA^{c})M_{Rb}}{M}⏟reduction via dilution.
$$

These expressions comprehensively define the dynamics of the tRNA pool, from generation via transcription to their recycling between charged and uncharged states through metabolic and translational fluxes, respectively. As in the main text, we posit that the dynamics of the ribosomal $M_{R⁢b}$, metabolic $M_{M⁢b}$, and ‘other’ $M_{O}$ protein masses follow via the allocation parameters $ϕ_{R⁢b}$, $ϕ_{M⁢b}$, and $ϕ_{O}$ respectively. However, in this treatment of the model, we consider these parameters, with the exception of $ϕ_{O}$, to be dynamic and depending on the intracellular concentration of ppGpp. Mathematically, we state this as

$$
\frac{d⁢M_{R⁢b}}{d⁢t}=ϕ_{R⁢b}⁢(ppGpp)⁢\frac{d⁢M}{d⁢t};\frac{d⁢M_{M⁢b}}{d⁢t}=[1-ϕ_{O}-ϕ_{R⁢b}⁢(ppGpp)]⁢\frac{d⁢M}{d⁢t};\frac{d⁢M_{O}}{d⁢t}=ϕ_{O}⁢\frac{d⁢M}{d⁢t}.
$$

We are now tasked with (i) enumerating the dynamics of ppGpp and (ii) assigning a specific functional form to $ϕ_{R⁢b}⁢(ppGpp)$. The biochemistry of ppGpp synthesis, degradation, and binding to the transcription machinery has been studied in E. coli among other prokaryotes, revealing the enzyme(s) important for this process, In E. coli RelA and SpoT. Many molecular details revealing how those enzymes control ppGpp levels in response to the abundance of tRNA levels are known but important details also remain puzzling (Magnusson et al., 2005; Anderson et al., 2021). Thus, while previous works have consider the dynamics of these specific proteins in more detail (Bosdriesz et al., 2015; Giordano et al., 2016), we here take a more coarse-grained view. Specifically, we first make the ansatz that the dynamics of ppGpp synthesis and degradation are sufficiently fast compared to the timescale of protein synthesis such that it can be treated as being in steady-state instantaneously. Secondly, we take the concentration of ppGpp to be inversely proportional to the relative abundance of charged- to uncharged-tRNAs,

$$
ppGpp∝\frac{1}{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}}.
$$

This is a well-motivated starting point as in E. coli, ppGpp is primarily synthesized via RelA when an uncharged-tRNA enters the A-site of a translating ribosome, forming a stalled complex. As binding of a charged-tRNA or an uncharged-tRNA is a competitive process, the probability of one or the other being bound is dependent on their relative concentrations, rather than the absolute concentrations of either species. However, other processes which affect ppGpp levels, including the synthesis and degradation by SpoT in relation to ribosome activity, are less well understood (Srivatsan and Wang, 2008). Accordingly, we consider our approach to describe ppGpp as inversely proportional to the relative abundance of charged- to uncharged-tRNAs as a motivated ansatz rather than a fully established biochemical relation. And we furthermore show below that this ansatz works much better for describing the experimental observations as a few different ones we probed.

Given the relation between ppGpp and tRNA charging ratio, Equation 33, we can now define the allocation towards ribosomes to be a function of the tRNA charging ratio, $ϕ_{R⁢b}⁢(\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}})$. To assign a specific functional form to this relation, we assume that the expression of ribosomal genes is in first order described by a simple binding kinetics of ppGpp to the transcriptional machinery and the allocation towards ribosomes follows a form similar to that of a Michaelis–Menten relation,

$$
ϕ_{R⁢b}⁢(\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}})=(1-ϕ_{O})⁢\frac{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}}{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}+\tau}.
$$

Here, the parameter $\tau$ represents the value of the charged- to uncharged-tRNA ratio where $ϕ_{R⁢b}$ is at its half-maximal value. The maximal value itself depends on the magnitude of $ϕ_{O}$, the allocation towards other proteins, which we are considering to be independent of ppGpp; $ϕ_{R⁢b}^{(m⁢a⁢x)}=1-ϕ_{O}$.

The transcription of tRNA genes towards novel tRNA synthesis has also been shown to be regulated with ppGpp, appearing to closely match the regulatory behavior of ribosomal proteins (Jinks-Robertson et al., 1983). We therefore model that the tRNA synthesis rate $κ$ (introduced in Equation 31) is similarly modulated by the charged- to uncharged-tRNA ratio,

$$
κ⁢(\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}})=κ_{max}⁢\frac{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}}{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}+\tau}.
$$

Here, $κ_{m⁢a⁢x}$ is the rate of tRNA transcription when all tRNA genes are fully saturated with RNA polymerase in rich growth conditions where gene dosage is high. Finally, we must establish functional forms for the tRNA dependencies on the metabolic and translation rate. Simple biochemical assumptions permit a formulation of a Michaelis–Menten function for each rate. Noting that the translation rate $\gamma$ is defined as $\gamma≡\frac{v_{t⁢l}}{m_{R⁢b}}$, where $v_{t⁢l}$ is the translation speed and $m_{R⁢b}$ is the proteinaceous mass of a single ribosome, we take $\gamma⁢(t⁢R⁢N⁢A^{c})$ to be of the form

$$
\gamma⁢(t⁢R⁢N⁢A^{c})=\frac{v_{t⁢l}^{(m⁢a⁢x)}}{m_{R⁢b}}⁢\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{c}+K_{M}^{(t⁢R⁢N⁢A^{c})}},
$$

where $v_{t⁢l}^{(m⁢a⁢x)}$ is the maximum translation speed and $K_{M}^{(t⁢R⁢N⁢A^{c})}$ is the Michaelis–Menten constant. A similar argument can be made for the dependence of the metabolic rate $ν$ on the uncharged-tRNA concentration,

$$
ν⁢(t⁢R⁢N⁢A^{u})=ν_{m⁢a⁢x}⁢\frac{t⁢R⁢N⁢A^{u}}{t⁢R⁢N⁢A^{u}+K_{M}^{(t⁢R⁢N⁢A^{u})}},
$$

with $K_{M}^{(t⁢R⁢N⁢A^{u})}$ being another Michaelis–Menten constant. Together, Equations 30–37 mathematically describe a model for ppGpp-dependent regulation of translational and metabolic fluxes.

In principle, an analytical solution for this system of ODEs can be found, though it precludes evaluation by hand and is computationally intensive. While we do not solve this system of ODEs analytically here, we can numerically integrate them to sufficiently approximate the steady-state behavior. Depending on the choice of parameter values, such an approach can yield an allocation scenario nearly indistinguishable from that of the optimal allocation scenario (scenario III) of the simple model (Figure 1H and I).

#### Optimal allocation emerges from flux-parity regulation

While the previous section lays out the mathematics of the flux-parity model, we now discuss how this regulation scheme can lead to an optimal allocation. Towards this goal, we first discuss in more detail what we mean when we say ’flux-parity.’ As described in the main text, we define flux-parity as a balance and mutual maximization of (i) the flux of uncharged-tRNAs through metabolism (termed the metabolic flux$J_{M⁢b}$) and (ii) the flux of charged-tRNAs through protein synthesis (termed the translational flux$J_{T⁢l}$). To demonstrate this point, assume that we can decouple the dependence of the allocation parameter $ϕ_{R⁢b}$ from the ratio of charged- to uncharged-tRNAs. Mathematically speaking, we can define the metabolic flux as the collective action of metabolic proteins,

$$
J_{M⁢b}=ν⁢(t⁢R⁢N⁢A^{u})⁢ϕ_{M⁢b}=\frac{ν_{m⁢a⁢x}⁢t⁢R⁢N⁢A⁢(1-ϕ_{O}-ϕ_{R⁢b})}{t⁢R⁢N⁢A^{u}+K_{M}^{t⁢R⁢N⁢A^{u}}}.
$$

Similarly, we can state that the translational flux is the collective action of ribosomal proteins,

$$
J_{T⁢l}=\frac{\gamma_{m⁢a⁢x}⁢t⁢R⁢N⁢A^{c}⁢ϕ_{R⁢b}}{t⁢R⁢N⁢A^{c}+K_{M}^{t⁢R⁢N⁢A^{c}}}
$$

So long as these fluxes are equivalent, a steady-state is satisfied. However, this steady-state is not necessarily the optimal value. This is illustrated in Figure 2, Figure 2—figure supplement 1. For example, if we consider that $ϕ_{R⁢b}$ is too large for the given condition (Figure 2—figure supplement 1, left), a specific steady-state is realized (black point). If $ϕ_{R⁢b}$ is further increased, the value of both the metabolic and translational fluxes (dashed lines) must decrease to reach a new steady state and growth rate thus declines. However, if $ϕ_{R⁢b}$ is decreased, the value of both fluxes increase and growth-rate thus also increases as well. At optimum allocation (where growth is locally maximized, Figure 2—figure supplement 1, middle), any perturbation to $ϕ_{R⁢b}$ will necessarily result in a decrease in the fluxes, indicating that at the optimal allocation the fluxes are mutually maximized.

As the concentrations of both tRNA species (Equations 30 and 31) are dependent on the allocation towards ribosomes $ϕ_{R⁢b}$ in inverse ways, the ratio of their concentrations acts as an effective sensor of the magnitude of either flux. A large charged- to uncharged-tRNA ratio indicates that there is an abundance of charged-tRNAs, suggesting that the translational flux is too low. Conversely, a small charged- to uncharged-tRNA ratio indicates a translational flux that is too large, diminishing the metabolic flux. By tying the allocation towards ribosomes $ϕ_{R⁢b}$ to this ratio, an allocation can emerge that optimizes the fluxes and thus growth.

### Assessing different assumptions of ϕR⁢b dependence on ppGpp

In Equation 33, we made the assumption that the concentration of ppGpp was inversely proportional to the charging balance of the tRNA pools. We put this forward as an ansatz with the motivation that the degree of tRNA charging should be related to the amount of ppGpp synthesized. However, there are other ansatzes that could be made relating the amount of ppGpp to the individual concentrations of the tRNAs, or other ratiometric definitions.

To test how sensitive our findings are to the particular ansatz used, we considered other ways in which the ppGpp concentration could be related to the tRNA pools. There is strong biochemical evidence that a primary route of ppGpp synthsesis is via the enzyme RelA, which becomes active when associated to a ‘stalled’ ribosome—one that is bound to an uncharged tRNA—though some details remain enigmatic. In manner similar to other works (Giordano et al., 2016; Wu et al., 2022; Bosdriesz et al., 2015), we can assert that the amount of ppGpp is proportional to the abundance of stalled ribosomes. Mathematically, we can define the ppGpp concentration as being proportional to the probability of a ribosome binding an uncharged tRNA. Assuming that the tRNA concentration (of both charged and uncharged forms) is sufficiently high that all ribosomes are complexed with a tRNA, this equates to

$$
[p⁢p⁢G⁢p⁢p]∝P_{bound}^{(uncharged)}≈\frac{t⁢R⁢N⁢A^{u}}{t⁢R⁢N⁢A^{c}+t⁢R⁢N⁢A^{u}},
$$

where $t⁢R⁢N⁢A^{c}$ and $t⁢R⁢N⁢A^{u}$ represent the absolute concentrations of charged and uncharged species, respectively. If the ppGpp concentration is inversely proportional to the allocation towards ribosomes, we can similarly make the argument that the ribosomal allocation $ϕ_{R⁢b}$ will be proportional to the probability of a ribosome being bound to a charged-tRNA,

$$
ϕ_{R⁢b}=(1-ϕ_{O})⁢P_{bound}^{(charged)}=(1-ϕ_{O})⁢\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}+t⁢R⁢N⁢A^{c}}.
$$

This equation mechanistically operates in a similar way as Equation 34—the allocation towards ribosomes depends on the relative amounts of charged- and uncharged-tRNAs. In the extreme limit where the total concentration of tRNA is fixed (for which there is conflicting evidence; Dong et al., 1996; Skjold et al., 1973; Bremer and Dennis, 2008; Bosdriesz et al., 2015; Giordano et al., 2016), Equation 41 and Equation 34 are mathematically equivalent. However, the predicted scaling dependence of ppGpp takes a different form.

In the main text, we noted that the concentration of ppGpp relative to a reference growth rate $\frac{[p⁢p⁢G⁢p⁢p]}{[p⁢p⁢G⁢p⁢p]_{0}}$ is equivalent to the inverse ratio of the charging balances. Under the ansatz that the ppGpp concentration is depending on the uncharged-tRNA binding probability, this relation takes the form

$$
\frac{[p⁢p⁢G⁢p⁢p]}{[p⁢p⁢G⁢p⁢p]_{0}}=\frac{P_{bound}^{(uncharged)}}{P_{bound_{0}}^{(uncharged)}}=\frac{1+\frac{t⁢R⁢N⁢A_{0}^{c}}{t⁢R⁢N⁢A_{0}}}{1+\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}},
$$

where the subscript 0 denotes the reference state value. This distinction, coupled with experimental measurements of the relative ppGpp concentrations, allows us to test the validity of the two assumed forms for $ϕ_{R⁢b}$.

Figure 3—figure supplement 1 shows the predictive capacity of these two ansatzes with the simple binding (Equation 41) and ratiometric (Equation 33) predictions shown in solid-blue and dashed-red lines, respectively. While both of these assumptions are capable of predicting the scaling of the ribosome content and translation speed with quantitative equivalence, there is a distinct difference in the predicted behavior of the relative ppGpp concentrations. The simple binding ansatz predicts a significantly shallower dependence on the growth rate than is observed in the data and in the ratiometric prediction. Thus, it appears that relating [ppGpp] to the ratio of uncharged- to charged-tRNA concentrations accurately captures the behavior of E. coli, though there remain gaps in our understanding of this relationship at a biochemical level.

#### Incorporating effects of ribosome-targeting antibiotics

To extend the flux-parity allocation model and incorporate the effects of antibiotic treatment, we must consider the mechanism of action of the antibiotic, specifically chloramphenicol. Chloramphenicol is a bacteriostatic antibiotic with tightly, but reversibly, binds to the ribosome. Once bound, the ribosome is unable to resume translation until chloramphenicol dissociates. Thus, we can model the effect of this drug by enumerating the probability that chloramphenicol is bound to a ribosome $P_{bound}$ at a given concentration $c_{c⁢m}$. Mathematically, this can be stated as

$$
P_{bound}=\frac{c_{c⁢m}}{c_{c⁢m}+K_{D}^{c⁢m}},
$$

where $K_{D}^{c⁢m}$ is an effective dissociation constant of chloramphenicol to a unit of ribosomal mass accounting for kinetics transport and ribosome binding. We can then say that the probability of a ribosome being active is equal to the probability of a ribosome being unbound,

$$
P_{active}=1-P_{bound}=1-\frac{c_{c⁢m}}{c_{c⁢m}+K_{D}^{c⁢m}}.
$$

As only active ribosomes will contribute to the accumulation of biomass, we must rewrite the dynamics as

$$
\frac{d⁢M}{d⁢t}=\gamma⁢(t⁢R⁢N⁢A^{c})⁢M_{R⁢b}^{active}=\gamma⁢(t⁢R⁢N⁢A^{c})⁢P_{active}⁢M_{R⁢b}.
$$

To make the predictions shown in Figure 3E and F, we assumed that the chloramphenicol concentration in the growth medium is equal to the intracellular concentration and take $K_{D}^{c⁢m}≈0.5$ nM.

#### Incorporating effects of excess protein stress

We consider that the excess protein synthesis can be modeled as the introduction of a new protein class, which we consider to have a total mass of $M_{X}$. Following the allocation parameters of the flux-parity model as defined in Equation 32, we can introduce a new allocation parameter $ϕ_{X}$ such that

$$
\frac{d⁢M_{X}}{d⁢t}=ϕ_{X}⁢\frac{d⁢M}{d⁢t};ϕ_{O}+ϕ_{M⁢b}+ϕ_{R⁢b}+ϕ_{X}=1.
$$

In Figure 3 I, we show that a collection of data can be collapsed onto a single line that relates the relative change in growth rate as a function of the excess protein that is synthesized. While we cannot fully solve the flux-parity model analytically, we can derive an analytical expression of this relation. Specifically, we note that the steady-state growth rate in the absence of excess expression $\lambda$ follows the simple relation

$$
\lambda=\gamma⁢(t⁢R⁢N⁢A^{c})⁢ϕ_{R⁢b}⁢(\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}})=\gamma_{m⁢a⁢x}⁢(1-ϕ_{O})⁢\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{c}+K_{M}^{t⁢R⁢N⁢A^{c}}}⁢\frac{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}}{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}+\tau}.
$$

This can be easily extended to compute the growth rate under excess protein synthesis $\lambda_{X}$ as

$$
\lambda_{x}=\gamma⁢(t⁢R⁢N⁢A^{c})⁢ϕ_{R⁢b}⁢(\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}})=\gamma_{m⁢a⁢x}⁢(1-ϕ_{O}-ϕ_{X})⁢\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{c}+K_{M}^{t⁢R⁢N⁢A^{c}}}⁢\frac{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}}{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}+\tau}.
$$

We can take the ratio of these growth rates to yield an expression for the collapse function

$$
\frac{\lambda_{X}}{\lambda}=\frac{\gamma_{m⁢a⁢x}⁢(1-ϕ_{O}-ϕ_{X})⁢\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{c}+K_{M}^{t⁢R⁢N⁢A^{c}}}⁢\frac{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}}{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}+\tau}}{\gamma_{m⁢a⁢x}⁢(1-ϕ_{O})⁢\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{c}+K_{M}^{t⁢R⁢N⁢A^{c}}}⁢\frac{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}}{\frac{t⁢R⁢N⁢A^{c}}{t⁢R⁢N⁢A^{u}}+\tau}}.
$$

If we assume that the excess protein synthesis affects only $ϕ_{X}$, leaving all other parameters untouched, Equation 49 reduces to the concise form

$$
\frac{\lambda_{X}}{\lambda}=\frac{1-ϕ_{O}-ϕ_{X}}{1-ϕ_{O}},
$$

which is the linear relation plotted in Figure 3I.

Aside from the collapse, we also show how the flux-parity model quantitatively predicts the growth rate as a function of excess protein for three different media (Figure 3H). In this case, we require some knowledge of what the metabolic rate $ν_{m⁢a⁢x}$ is for those specific conditions. As the metabolic rate is an efficient rate incorporating the action of different metabolic reactions and serving as a proxy of the nutrient quality, it is not possible to make an a priori estimate of its value. To nevertheless estimate $ν_{m⁢a⁢x}$ for each condition, we determined its value by using the simple allocation model as encoded in ‘Derivation of analytical expressions,’ assuming the growth rate $\lambda$ and the ribosomal content describes the allocation towards ribosomes $ϕ_{R⁢b}$. Under the simple allocation model, we note that an expression for the metabolic rate can be solved from the steady-state precursor concentration $c_{p⁢c}^{*}$ (Equation 18) to yield

$$
ν_{m⁢a⁢x}=\frac{\lambda⁢(c_{p⁢c}+1)}{1-ϕ_{O}-ϕ_{R⁢b}}.
$$

The steady-state precursor concentration $c_{p⁢c}^{*}$ can be solved from the definition of the steady-state growth rate and has the form

$$
c_{p⁢c}^{*}=\frac{K_{D}^{c_{p⁢c}}⁢\lambda}{ϕ_{R⁢b}⁢\gamma_{m⁢a⁢x}⁢(1-\frac{\lambda}{ϕ_{R⁢b}})}.
$$

Combining Equations 51 and 52 yields an expression for the maximal metabolic rate $ν_{m⁢a⁢x}$,

$$
ν_{m⁢a⁢x}=\frac{\lambda}{1-ϕ_{O}-ϕ_{R⁢b}}⁢(\frac{K_{D}^{c_{p⁢c}}⁢\lambda}{ϕ_{R⁢b}⁢\gamma_{m⁢a⁢x}⁢(1-\frac{\lambda}{ϕ_{R⁢b}})}+1).
$$

Thus, given knowledge of the steady-state growth rate $\lambda$ and the allocation towards ribosomes $ϕ_{R⁢b}$ (which are both measured quantities), the value of $ν_{m⁢a⁢x}$ can be derived.

#### Incorporating effects of nutrient upshifts

To model the dynamics of growth in fluctuating conditions, we asserted that a nutritional upshift is equivalent to an instantaneous change in the metabolic rate such that $ν_{max}^{preshift}<ν_{max}^{postshift}$. However, this is not completely sufficient to capture the phenomenology that is observed. It is becoming exceedingly clear that bacterial cells are non-optimal in what genes they express, with many proteins that are synthesized are ultimately useless in the specific condition (Balakrishnan et al., 2021a). This can have very important effects on the growth rate as any amount of conditionally useless protein that is synthesized consumes resources that could otherwise be partitioned to the proteins that need to be synthesized. To incorporate this effect, we introduce another protein class with an allocation parameter $ϕ_{ø}$. As the degree of conditionally useless expression is significantly more pronounced in slow rather than fast conditions (Balakrishnan et al., 2021a; Belliveau et al., 2021; Schmidt et al., 2016), we further asserted that the magnitude of this sector also changed in response to the nutritional upshift such that $ϕ^{preshift}>ϕ^{postshift}$. The precise value of this sector is less important than the difference in the pre- and post-shift condition and can be considered as an additional rescaling factor as described in Appendix 1 Neglecting the other proteins. Thus, for all nutritional shifts in this work, we considered that $ϕ_{ø}^{p⁢o⁢s⁢t⁢s⁢h⁢i⁢f⁢t}=0$ and the value of $ϕ_{ø}^{p⁢r⁢e⁢s⁢h⁢i⁢f⁢t}$ to be linearly proportional to the difference in the growth rates between the pre- and post-shift conditions.

#### Incorporating effects of nutrient depletion

Up to this point, we have explored the flux-parity model under the assumption that the nutrients in the environment were saturating, such that $ν⁢(c_{n⁢t})≈ν_{m⁢a⁢x}$. However, a dependence on the environmental nutrient concentration $c_{n⁢t}$ can be easily included in the definition of the metabolic rate $ν$ as

$$
ν⁢(t⁢R⁢N⁢A,c_{n⁢t})=ν_{m⁢a⁢x}⁢(\frac{t⁢R⁢N⁢A^{u}}{t⁢R⁢N⁢A^{u}+K_{M}^{t⁢R⁢N⁢A^{u}}})⁢(\frac{c_{n⁢t}}{c_{n⁢t}+K_{M}^{c_{n⁢t}}}),
$$

where $K_{M}^{c_{n⁢t}}$ is the Michaelis–Menten constant. We can then model the dynamics of the nutrient concentration $c_{n⁢t}$ in a batch-culture system as

$$
\frac{d⁢c_{n⁢t}}{d⁢t}=-\frac{ν⁢(t⁢R⁢N⁢A,c_{n⁢t})⁢M_{M⁢b}}{Y},
$$

where $Y$ is the yield coefficient.

### Data sets

This work leverages a large collection of data, primarily from E. coli, to evaluate the accuracy of our model in describing biological phenomena. These data come from a range of studies spanning around 50 years of measurements from different groups and different geographical locations. Collecting and curating this large data set required the manual transcribing of data from papers as well as various standardization steps to ensure that measurements were truly comparable between studies, as is outlined in Supplementary file 2.

For proper referencing and attribution, we list the data sources here as follows: Albertson and Nyström, 1994; Baracchini and Bremer, 1988; Basan et al., 2015; Bentley et al., 1990; Bremer and Dennis, 2008; Bren et al., 2013; Brunschede et al., 1977; Büke et al., 2022; Buckstein et al., 2008; Coffman et al., 1971; Dai et al., 2016; Dalbow and Young, 1975 ; Dong et al., 1995; Erickson et al., 2017; Forchhammer and Lindahl, 1971; Gausing, 1972; Hernandez and Bremer, 1990; Hernandez and Bremer, 1993; Imholz et al., 2020; Kepes and Beguin, 1966; Korem Kohanim et al., 2018; Lacroute and Stent, 1968; Lazzarini et al., 1971; Li et al., 2014; Li et al., 2018;; Mori et al., 2017; Morris and Hansen, 1973; Oldewurtel et al., 2021; Panlilio et al., 2020; Pedersen, 1984; Ryals et al., 1982; Sarubbi et al., 1988; Schmidt et al., 2016; Schleif, 1967; Schleif et al., 1973; Scott et al., 2010; Si et al., 2017; Skjold et al., 1973Sloan and Urban, 1976; Sokawa et al., 1975; Wu et al., 2022; You et al., 2013; Young and Bremer, 1976; Zhu and Dai, 2019; Bonven and Gulløv, 1979; Lacroute, 1973; Metzl-Raz et al., 2017; Paulo et al., 2015; Paulo et al., 2016; Riba et al., 2019; Siwiak and Zielenkiewicz, 2010; Waldron and Lacroute, 1975; Xia et al., 2021; Rohatgi, 2021.

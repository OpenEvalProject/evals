# Robust, coherent, and synchronized circadian clock-controlled oscillations along Anabaena filaments

## Authors

- Rinat Arbel-Goren<sup>1</sup> ([ORCID: 0000-0002-7253-2036](https://orcid.org/0000-0002-7253-2036))
- Valentina Buonfiglio<sup>2</sup> ([ORCID: 0000-0003-1528-2955](https://orcid.org/0000-0003-1528-2955))
- Francesca Di Patti<sup>3</sup> ([ORCID: 0000-0003-1288-0079](https://orcid.org/0000-0003-1288-0079))
- Sergio Camargo<sup>1</sup> ([ORCID: 0000-0002-5688-3215](https://orcid.org/0000-0002-5688-3215))
- Anna Zhitnitsky<sup>1</sup> ([ORCID: 0000-0001-9598-4812](https://orcid.org/0000-0001-9598-4812))
- Ana Valladares<sup>4</sup> ([ORCID: 0000-0002-6683-1355](https://orcid.org/0000-0002-6683-1355))
- Enrique Flores<sup>4</sup> ([ORCID: 0000-0001-7605-7343](https://orcid.org/0000-0001-7605-7343))
- Antonia Herrero<sup>4</sup> ([ORCID: 0000-0003-1071-6590](https://orcid.org/0000-0003-1071-6590))
- Duccio Fanelli<sup>2</sup> ([ORCID: 0000-0001-8545-9424](https://orcid.org/0000-0001-8545-9424))
- Joel Stavans<sup>1</sup> ([ORCID: 0000-0003-0396-7797](https://orcid.org/0000-0003-0396-7797)) †

### Affiliations

1. Department of Physics of Complex Systems, Weizmann Institute of Science Rehovot Israel
2. Dipartimento di Fisica e Astronomia, Università di Firenze, INFN and CSDC Sesto Fiorentino Italy
3. Consiglio Nazionale delle Ricerche, Istituto dei Sistemi Complessi Sesto Fiorentino Italy
4. Instituto de Bioquímica Vegetal y Fotosíntesis, CSIC and Universidad de Sevilla Sevilla Spain

† Corresponding author

## Abstract

Circadian clocks display remarkable reliability despite significant stochasticity in biomolecular reactions. We study the dynamics of a circadian clock-controlled gene at the individual cell level in Anabaena sp. PCC 7120, a multicellular filamentous cyanobacterium. We found significant synchronization and spatial coherence along filaments, clock coupling due to cell-cell communication, and gating of the cell cycle. Furthermore, we observed low-amplitude circadian oscillatory transcription of kai genes encoding the post-transcriptional core oscillatory circuit and high-amplitude oscillations of rpaA coding for the master regulator transducing the core clock output. Transcriptional oscillations of rpaA suggest an additional level of regulation. A stochastic one-dimensional toy model of coupled clock cores and their phosphorylation states shows that demographic noise can seed stochastic oscillations outside the region where deterministic limit cycles with circadian periods occur. The model reproduces the observed spatio-temporal coherence along filaments and provides a robust description of coupled circadian clocks in a multicellular organism.

## Introduction

Endogenous circadian clocks allow the alignment of cellular physiology with diurnal light/darkness cycles on Earth, endowing organisms, from unicellular cyanobacteria to multicellular plants and mammals, with a selective fitness advantage (Cohen and Golden, 2015). Significant progress has been achieved in understanding circadian clock architectures and function in cyanobacteria, which are arguably the simplest organisms exhibiting self-sustained oscillations (Hasty et al., 2010; Rust et al., 2007; Lambert et al., 2016; Dong et al., 2010; Teng et al., 2013; Gan and O'Shea, 2017). The molecular mechanisms behind autonomous circadian clocks have been elucidated primarily in the unicellular Synechococcus elongatus. These investigations have shown that the core of the circadian clock consists of three proteins, KaiA, KaiB, and KaiC (Ishiura et al., 1998), whose oscillating behavior can be reconstituted in vitro (Nakajima et al., 2005). The basic mechanism behind the clock is based on the stimulation of KaiC autophosphorylation by the binding of KaiA and the autodephosphorylation that ensues when KaiB binds to KaiC, blocking KaiA’s stimulatory function. A salient feature of the circadian clock in Synechococcus is the high temporal precision it can exhibit, despite the fact that biochemical reactions in a cell are stochastic events and that clock components may be subject to variations in molecular copy numbers between cells, variations known as demographic noise (Tsimring, 2014). Many studies have addressed the robustness of circadian rhythms to demographic noise in Kai proteins (Mihalcescu et al., 2004; Chabot et al., 2007; Teng et al., 2013; Pittayakanchit et al., 2018; Chew et al., 2018), but copy number variations in KaiC phosphoforms, which impact directly on clock function, have not been previously considered.

The multicellular character of higher organisms and of some cyanobacterial species (Herrero et al., 2016) naturally prompts the question of how do ensembles of noisy circadian clocks perform in a multicellular organismal setting. Theoretical considerations have motivated the notion that reliable collective oscillations may result from the coupling of ‘sloppy’, noisy clocks (Enright, 1980). It has been suggested that coupling of circadian clocks in unicellular organisms by quorum sensing interactions may result in emergent synchronization (Garcia-Ojalvo et al., 2004), and experimental evidence in support of this notion has been reported in a synthetic system (Danino et al., 2010).

Anabaena sp. strain PCC 7120 (henceforth Anabaena) is a multicellular cyanobacterium in which cells are arranged in a one-dimensional configuration, with local, nearest-neighbor cell-cell coupling through septal junctions (Herrero et al., 2016). Evidence of coupling of metabolic pathways along a filament due to cell-cell communication has been reported (Mullineaux et al., 2008). In contrast to Synechococcus, information about the mechanism of the circadian clock of Anabaena is scant. Sequence BLAST analysis has shown that Anabaena contains homologs of the kaiA, kaiB, and kaiC genes of Synechococcus, and structural studies indicate that the interactions between the respective proteins are similar (Garces et al., 2004). Furthermore, Anabaena also contains factors coupling the Kai post-transcriptional oscillator to input signals and to output factors such as RpaA, CikA, and SasA that couple the clock to the genes it regulates (Schmelling et al., 2017). The roles of these genes in Anabaena remain to be elucidated. A first characterization of the circadian rhythms in bulk cultures of Anabaena has shown that the clock is autonomous, running freely under constant light conditions following exposure to two 12 hr light-dark cycles, similarly to Synechococcus (Kushige et al., 2013). However, this study also showed that, in contrast to Synechococcus, none of the kai genes are expressed with a large amplitude. Nonetheless, about 80 kai-controlled genes that exhibit high-amplitude circadian oscillations were identified using DNA microarray analysis, a behavior that was abolished in a kaiABC deletion mutant.

Here, we present an experimental and theoretical study of circadian clocks in multicellular Anabaena. Its one-dimensional character allowed us to follow clocks in each and every cell along a filament, and shed light on the interplay between demographic noise and cell-cell communication in setting synchrony and spatial coherence along filaments. In our experiments, we followed in vivo the output of clocks in individual cells by monitoring the expression from the promoter of pecB, a clock-controlled gene of high-amplitude oscillations (Kushige et al., 2013). This gene is part of the pecBACEF operon and codes for the beta subunits of phycoerythrocyanin, a structural component of the phycobilisome rod that plays a major role in light harvesting for photosynthesis (Swanson et al., 1992). On the theoretical side, we first incorporated the effects of demographic noise into a three-component model of a single clock describing the phosphorylation states of KaiC, as in Synechococcus. Next, we extended this single-cell stochastic model to describe a one-dimensional array of coupled clocks, as in multicellular Anabaena, allowing us also to analyze the spatio-temporal coherence properties of noisy oscillations in Anabaena filaments.

## Results

### Circadian clocks of individual cells in growing filaments are highly synchronized

We followed circadian oscillations in Anabaena from a chromosomal gfp fusion to the N-terminus of the clock-controlled protein, PecB, here denoted as $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ at the level of individual cells along filaments. Prior to and during the experiments, filaments were grown under constant light conditions. Typical images of wild-type (WT) filaments at different time points are shown in Figure 1A (see also Figure 1, Video 1). One salient feature in the images is significant synchrony, that is, cellular oscillations progressed in individual cells along filaments together and with a similar period. The images in Figure 1A correspond to successive maxima and minima of the mean cell fluorescence intensity, µ, as a function of time, which we plot in Figure 2A. Similar experiments with a strain in which the kaiABC genes were deleted ($Δ$kaiABC) resulted in a low-level, non-oscillatory signal (Figure 2A), confirming the regulation of pecB expression by the circadian clock genes. As a control, we monitored expression from the promoter of hetR, a gene coding for the master regulator of development in Anabaena. The expression from the hetR promoter $P_{h⁢e⁢t⁢R-g⁢f⁢p}$ did not exhibit an oscillatory behavior (Figure 2A), a result consistent with previous microarray experiments (Kushige et al., 2013). This does not preclude a possible interaction between the circadian clock and differentiation. On the other hand, the autofluorescence from photosynthetic pigments did not display oscillatory behavior (see Figure 1B, Figure 2A).

![Figure 1.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig1-v2.jpg)

**Figure 1.:** (A) GFP fluorescence in a filament of an Anabaena strain bearing a $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ promoter fusion, growing under nitrogen-replete conditions. The snapshots were chosen near maxima and minima of the circadian oscillations. (B) Autofluorescence as a function of time in Anabaena. Snapshots correspond to those in (A), and time 0 corresponds to the time at which filaments were placed in a device for microscope observation (for details, see Materials and methods). For a time-lapse movie, see Video 1 (taken over 6 days).

![Figure 2.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig2-v2.jpg)

**Figure 2.:** (A) Average cell fluorescence intensity from $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ in a filament as a function of time for a wild-type genetic background (full black circles) and for a $Δ$kaiABC background (empty black circles); intensity of autofluorescence as a function of time (blue circles); average cell fluorescence intensity from $P_{h⁢e⁢t⁢R-g⁢f⁢p}$ (cyan line); and temporal dependence of the cell-cell variability $C⁢V^{2}$ in expression of $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ (red line). Data were taken from at least 50 contiguous cells along a filament. (B) Average fluorescence intensity as a function of time of filaments in different fields of view from the same experimental run. Each trace was obtained from at least 50 contiguous cells along each filament. (C) Expression from a $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ fusion in the lineages of two contiguous cells as a function of time. (D) Average spatial autocorrelation function of $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ expression along filaments of wild-type (blue), $Δ$sepJ/$Δ$fraCD (green), and $Δ$kaiABC (orange) genetic backgrounds. Error bars represent standard errors. Magenta line: contribution to the spatial autocorrelation function of fluctuations from the wild-type data set, induced by binomial partitioning of molecules between daughter cells, following each of three consecutive cell divisions. Prior to divisions, the cell order in each filament was reshuffled. (E) Histogram of the phase of cell-division events along the circadian cycles, with 0 and $2⁢\pi$ denoting two consecutive minima, from two independent experiments. For additional data similar to (A) and (C), corresponding to filaments of the sepJ/fraCD genetic background, see Figure 2—figure supplement 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig2-figsupp1-v2.jpg)

![Video 1.](https://cdn.elifesciences.org/articles/64348/elife-64348-video1.mp4.jpg)

To characterize quantitatively the degree of synchronization between cellular clocks along a filament, we used the synchronization index $R$ (Garcia-Ojalvo et al., 2004) (Materials and methods), which can be readily calculated from the measured fluorescence intensity in each cell and which varies between 0 (no synchronization) and 1 (full synchronization). To compute $R$, several cells along a filament were selected, and their fluorescence intensity was followed over a full period of oscillation. Contiguous cells, which include sister cells from the same mother, are highly synchronized, as shown by the large value of $R$ ($0.89\pm0.04$) (Table 1). The value of $R$ for cells initially separated by intervals of 10 other cells – chosen in an attempt to avoid initial correlations between their clocks – was significantly indistinguishable from that computed for contiguous cells, underscoring the large degree of synchronization of clocks along a filament.

**Table 1.**
 Synchronization of expression of a clock-controlled gene in cells within and between Anabaena filaments.The synchronization index $R$ for strains with the indicated genotypes (Materials and methods) was measured from the fluorescence intensities of $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ expression in the same cells followed over a full circadian period in a filament, either in clusters of contiguous cells (contiguous) or for cells separated by intervals of 10 cells (separate). To measure synchronization between filaments, $R$ was computed from about 10 cells, each belonging to a different filament. For each genetic background, the mean and standard error of the mean (SEM) of $R$ was determined from a number of independent repeats (Rust et al., 2007; Lambert et al., 2016; Dong et al., 2010; Teng et al., 2013), carried out in $n$ different experimental runs. Significance (p-value) in interstrain comparisons was established by the Mann–Whitney U-test, and * represents rejection of the null hypothesis that samples come from distributions with equal medians. WT: wild type.


<table>
  <thead>
    <tr>
      <th>Genotype</th>
      <th>Cell cluster</th>
      <th>R (mean ± SEM)</th>
      <th>n</th>
      <th>Comparison with strain</th>
      <th>p-Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WT</td>
      <td>Contiguous</td>
      <td>0.89 ± 0.04</td>
      <td>3</td>
      <td>WT (separate)</td>
      <td>0.117</td>
    </tr>
    <tr>
      <td>WT</td>
      <td>Separate</td>
      <td>0.85 ± 0.01</td>
      <td>2</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>WT</td>
      <td>Different filaments</td>
      <td>0.75 ± 0.04</td>
      <td>2</td>
      <td>WT (separate)</td>
      <td>0.026*</td>
    </tr>
    <tr>
      <td>Δ⁢s⁢e⁢p⁢J⁢Δ⁢f⁢r⁢a⁢C⁢D</td>
      <td>Contiguous</td>
      <td>0.73 ± 0.05</td>
      <td>4</td>
      <td>WT (contiguous)</td>
      <td>0.001*</td>
    </tr>
    <tr>
      <td>Δ⁢k⁢a⁢i⁢A⁢B⁢C</td>
      <td>Contiguous</td>
      <td>0.71 ± 0.03</td>
      <td>3</td>
      <td>WT</td>
      <td>0.001*</td>
    </tr>
  </tbody>
</table>

To test the extent to which different filaments are synchronized under the same conditions, we measured the average fluorescence intensity per cell in different filaments as a function of time (Figure 2B). The expression from $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ in different filaments oscillated nearly in phase mainly during the first oscillations. To evaluate quantitatively the degree of phase synchronization between filaments, we calculated $R$ by choosing one cell per filament in a number of filaments measured simultaneously (Materials and methods). We obtained $R=0.75\pm0.04$, a value that is significantly smaller than that obtained for cells within the same filament (Figure 2C, Table 1). We surmise that initial synchronization may be due to phase resetting following the change in conditions, for example, illumination, upon transfer of cells from bulk culture to the microscope for real-time measurements. This change also could account for the decay in fluorescence intensity observed during the first circa 24 hr of our experiments (Figure 2A, B). Furthermore, this decay is $P_{p⁢e⁢c⁢B-g⁢f⁢p}$-specific, but clock-independent, as it was also observed in filaments of the $Δ⁢k⁢a⁢i⁢A⁢B⁢C$ background (Figure 2A).

### Circadian clocks along filaments are coupled by cell-cell communication

Another salient feature in the snapshots of Figure 1A is the high spatial coherence of the expression from $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ along filaments, that is, all cells have nearly the same phase along their circadian cycle. To quantify the extent to which clocks are actually correlated, we calculated the spatial autocorrelation function of fluorescence intensity $g$ as a function of distance along a filament (see Materials and methods). We found that $g$ decays to zero for separations of five cells or more (Figure 2D).

To evaluate the contribution of phase inheritance following cell division to the observed autocorrelation, a simulated filament was generated from each measured filament by dividing each cell into two for three generations, partitioning the fluorescence of a mother cell binomially between the two daughters, and then multiplying the results by two, in order to conserve the average fluorescence per cell. The autocorrelation functions of these simulated filaments were then computed and averaged. The resulting mean autocorrelation (Figure 2D, magenta line) decreased to zero already at the second neighbor, suggesting that another factor, for example, cell-cell communication, contributes significantly to the coupling of fluctuations of pecB expression along a filament. To support this notion further, we calculated the spatial autocorrelation function of $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ expression in filaments of a $Δ$sepJ/$Δ$fraCD strain in which genes coding for three septal proteins SepJ, FraC, and FraD involved in cell-cell communication were deleted (Nürnberg et al., 2015). Circadian oscillations in expression from $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ in filaments of this strain were observed (Figure 2—figure supplement 1A). The resulting spatial autocorrelation function decreased over significantly shorter lengthscales (about two cells) than the WT (Figure 2D). Therefore, we calculated the synchronization index between contiguous cells in this genetic background and found that $R$ was significantly smaller than that measured for contiguous cells within filaments of the WT background, but comparable to that obtained for cells in different filaments (Table 1). Consistently with this smaller value of R, traces of individual cells and their respective lineages were considerably more noisy (see Figure 2—figure supplement 1B) than lineages in WT filaments (Figure 2C). These findings indicate that the correlation in $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ expression is due primarily to significant coupling between the clocks in neighboring cells due to cell-cell communication. Of note, the value of $R$ calculated for a $Δ⁢k⁢a⁢i⁢A⁢B⁢C$ background, in which $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ expression is clock-independent, was similar to that for $Δ$sepJ/$Δ$fraCD, in which cell-cell communication is impaired (Table 1).

### Cell-cell variability oscillates out of phase with the circadian rhythm

Variations in gene expression between cells along a filament may limit both synchrony and spatial coherence. These variations are evident in Figure 1A even though their amplitude is small relative to the clock-modulated activity of $P_{p⁢e⁢c⁢B-g⁢f⁢p}$. To quantify these variations, we calculated the square of the coefficient of variation $C⁢V=\sigma/\mu$, where $\sigma$ denotes the standard deviation of the fluorescence intensity of contiguous cells along a filament. A plot of $C⁢V^{2}$ as a function of time showed that the cell-cell variability itself displays oscillatory behavior, attaining maxima approximately in the middle of periods during which the mean fluorescence intensity increases (Figure 2A).

### Coupling between cell cycle and clocks

In a cellular setting, circadian and cell cycle oscillations take place concurrently. In a variety of organisms, from prokaryotes to mammals, the circadian clock has been observed to gate cell division, enabling cell division to take place at some phases of the circadian cycle but inhibiting at others (Mori, 2009; Yang et al., 2010). To test whether the cell cycle and circadian clocks are coupled in Anabaena cells, we monitored the time at which cell division takes place along the circadian cycle in individual cell traces, under conditions of constant illumination. The fluorescence intensity traces of two contiguous ancestor cells bearing the $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ fusion and their respective lineage are shown in Figure 2C. In Figure 2E, we show a histogram of the timing of cell division events as a function of the phase at which they occur along the circadian clock, obtained from traces similar to those in Figure 2C. Far from being equiprobable along the circadian cycle, cell division events showed a marked tendency to occur near the beginning or the end of a circadian cycle (minima in µ) as for Synechococcus (Yang et al., 2010). Figure 2C also shows that the clock phase was faithfully inherited by any two daughters following cell division.

### Transcriptional oscillations of kai genes and the master transducer regulator rpaA

Previous northern blot measurements and microarray analysis of kai genes showed no reliable, high-amplitude oscillatory expression of any of the kai genes in Anabaena. To study with higher sensitivity the expression of kai genes, we carried out real-time quantitative polymerase chain reaction (RT-qPCR) measurements of WT and ΔkaiABC strains in bulk cultures. Since the value of the $R$ index was smaller between filaments than within (Table 1), the experiments were carried out under constant light conditions following two 12 hr/12 hr light-dark cycles, to enhance synchronization (see Materials and methods). The relative expression of the three kai genes indeed showed noisy, low-amplitude temporal modulations (Figure 3A). The oscillations were largely in phase, and transcription occurred mainly during subjective day. To assess quantitatively the extent of coordination, we calculated the synchronization index $R$ for the different pairs and obtained $R_{A,B}=0.85\pm0.05$, $R_{A,C}=0.79\pm0.09$, and $R_{B,C}=0.87\pm0.06$. Error bars were obtained by bootstrap methods (Materials and methods). Since the differences between these values are not significant, we conclude that transcription of the three genes is coordinated. In fact, the value of $R$ evaluated for the three genes was 0.78 ± 0.08.

![Figure 3.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig3-v2.jpg)

**Figure 3.:** (A) Relative expression of kaiA (green), kaiB (red), and kaiC (blue) as a function of time measured by RT-qPCR (Materials and methods). A persistence homology analysis of these data is presented in Figure 3—figure supplement 1. (B, C) Relative expression levels of rpaA and pecB, respectively, in wild-type (full circles) and $Δ$kaiABC strains (empty circles). Curves have been normalized by their temporal mean. Error bars represent the standard error of the mean of three independent experiments (see Materials and methods). Gray shades represent periods of subjective night. For additional information about regulatory sequences of the kaiABC, rpaA, pecB promoter regions and RpaA binding sites in Anabaena, see (C) (Figure 3—figure supplement 2).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig3-figsupp2-v2.jpg)

To expose an underlying oscillatory behavior in the kai genes data and support the notion that the oscillations are circadian, we applied persistent homology methods (Pereira and de Mello, 2015; Otter et al., 2017) to two-dimensional phase portraits of their respective time series (see Appendix 1 – supplemental methods). The delay $\tau$ for each phase portrait corresponds to the first minimum of the auto-mutual information of the time series (Fraser and Swinney, 1986), and for a periodic, nearly sinusoidal signal, corresponds to a quarter of the signal's period (Kennedy et al., 2018). We obtained $\tau=7.1\pm1.2$ hr, $\tau=6.7\pm1.2$ hr, and $\tau=7.3\pm1.1$ ($n\geq3$) hr for kaiA, kaiB, and kaiC, respectively, all consistent with a circadian period of oscillation (Appendix 1). A Vietoris–Rips filtration of the clouds of points in the phase portraits (Appendix 1) indeed showed evidence for a persistent cycle in the transcription of each of the kai genes (Figure 3—figure supplement 1).

To shed light on how the state of the clock is relayed to the genes it controls, for example, pecB, we measured the relative expression of rpaA in WT and $Δ⁢k⁢a⁢i⁢A⁢B⁢C$ strains by RT-qPCR. RpaA has been shown to transduce the phosphorylation state of KaiC to clock-controlled genes in other cyanobacteria (Markson et al., 2013; Iijima et al., 2015) and is highly conserved (Schmelling et al., 2017). The role RpaA plays in the circadian oscillations of Anabaena is unknown. We found that the relative expression of rpaA displays high-amplitude oscillatory behavior (Figure 3B). Furthermore, pecB displays oscillatory behavior, with similar amplitude and phase. The oscillatory behavior of both genes was abolished in the $Δ$kaiABC mutant (Figure 3B, C). Note that the expression of both rpaA and pecB peaks during subjective night.

### Incorporating demographic noise into a model of a single clock

In order to develop a model of an array of coupled noisy clocks as in Anabaena, we first characterized the spectral properties of uncoupled clocks in individual cells of Synechococcus. We carried out experiments following the expression of YFP from the kaiBC promoter in single cells of Synechococcus growing within patterned gels (Figure 4A). Circadian oscillations in the lineages of two sister cells are shown in Figure 4B (see also Figure 5B for the associated power spectrum). Expression from the kaiBC promoter exhibited circadian oscillations with a period of about 25 hr, similar to those observed previously (Teng et al., 2013). Our next goal was to generalize a deterministic model for individual clocks in Synechococcus (Rust et al., 2007) to include the effects of demographic stochasticity. We followed the interaction network depicted in Figure 5A (adapted from Rust et al., 2007). Our mathematical model takes into account the dynamics of three forms of KaiC, namely, the single-phosphorylated forms S-KaiC (phosphorylated at serine 431), T-KaiC (phosphorylated at threonine 432), and the double-phosphorylated form D-KaiC, while the unphosphorylated U-KaiC can be deduced from the conservation of the total number of molecules of KaiC. Crucial for the appearance of oscillations is the negative feedback mediated by S-KaiC through inactivation of KaiA via KaiB function. Furthermore, the condition on the active KaiA monomers (see Equation S4 in Rust et al., 2007) is modeled here by a continuous function (Appendix 1 – Equation 6) that makes analytical progress possible. The parameter $\gamma$ in our nonlinear phosphorylation and dephosphorylation rates $k_{X⁢Y}$ for $X,Y={U,T,D,S}$ sets the steepness of the inverted sigmoidal dependence of the rates on KaiA (Figure 5—figure supplement 1). The dynamics of the stochastic model is described by a master equation accounting for discrete variations in molecular copy numbers of phosphoforms instead of deterministic, ordinary differential equations (Rust et al., 2007; Brettschneider et al., 2010). We then use the van Kampen system-size expansion to carry out a linear noise approximation that yields, to leading order, an extended set of ordinary differential equations for the concentrations of S ($ϕ_{S}=[S-KaiC]$), T ($ϕ_{T}=[T-KaiC]$), and D ($ϕ_{D}=[D-KaiC]$). The analysis of these equations allows us to determine the region in parameter space within which the model exhibits sustained deterministic oscillations (Figure 5C). The parameters of the model have been set to the values determined in vitro in Rust et al., 2007 and reported in Appendix 1—table 1, except for $\gamma$ and [KaiA], which were allowed to change freely. Note that deterministic oscillations with a circadian period were limited only to a small strip near the stability boundary. At the next-to-leading order, the expansion allows to evaluate the effects of demographic noise and calculate the power spectrum of fluctuations for each species’ abundance due to finite size effects (see Appendix 1). A fit of the theoretical power spectrum to the experimentally measured one provides an adequate interpolation upon adjusting the two fitting parameters, $\gamma$ and [KaiA] (see Figure 5B). In drawing the comparison between theory and experiments, we assumed that the fluorescence intensity is an immediate proxy of the phosphoform T-KaiC (Teng et al., 2013). The fitted parameters position the system outside the region of deterministic oscillations (circle in Figure 5C), suggesting that circadian rhythms can be a manifestation of noise-driven oscillations (Figure 5D). Remarkably, the fitted value for $[KaiA]=1.308$ µM matches the concentration reported previously ($[KaiA]=1.3$ µM; see Rust et al., 2007).

![Figure 4.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig4-v2.jpg)

**Figure 4.:** (A) Growth and lineage of a cell in patterned agarose, expressing YFP from the kaiBC promoter. The snapshots were chosen near maxima and minima of the circadian oscillations. (B) Fluorescence intensity of YFP of individual cells obtained from two independent cell lineages (red and blue).

![Figure 5.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig5-v2.jpg)

**Figure 5.:** (A) Schematic representation of interconversion between KaiC phosphoforms modulated by the activity of KaiA in an individual clock. The different phosphoform states of KaiC are denoted by U (unphosphorylated, U-KaiC), T (phosphorylated at threonine, T-KaiC), S (phosphorylated at serine, S-KaiC), and D (phosphorylated at both sites). Arrows denote transitions between the different phosphoforms $X,Y$ with the indicated rates $k_{x⁢y}$. KaiB mediates the inactivation of KaiA by S, as described by the continuous function $f$ (see Figure 5—figure supplement 1). (B) Average power spectrum of single-cell fluorescence (red symbols) fit to the data with the prediction from the stochastic model (blue line). (C) $\gamma$-[KaiA] plane where deterministic limit cycle oscillations in individual clocks occur. The color corresponds to the period of oscillations (in hours). The boundary of the colored region corresponds to a Hopf bifurcation. Note that deterministic oscillations with a circadian period are limited only to a small strip near the stability boundary at the bottom right. The circle identifies the values of $\gamma$ and KaiA that we obtain by fitting experimental power spectra in (B). The diamond stands for best fit parameters obtained for Anabaena (Figure 6C). (D) Comparison between damped deterministic oscillations (blue line) and quasi-cycles, both at the circle point outside the region of the deterministic oscillations in (C).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig5-figsupp1-v2.jpg)

### Theoretical model of arrays of coupled noisy clocks

Next, we generalized the single-clock model above to an array of coupled circadian clocks as in Anabaena, which is endowed with cell-cell communication via septal proteins (Herrero et al., 2016; Figure 6A). We postulate that the intercellular transfer of factors such as sugars (Mullineaux et al., 2008; Nürnberg et al., 2015) may affect the behavior of neighboring clocks, yielding an effective long-ranged coupling between clock inputs across the filament. The interaction is here modeled by an exponential kernel that extends over a few cells. We assumed that the core clock mechanisms of Synechococcus and Anabaena are similar (Kushige et al., 2013; Schmelling et al., 2017; Garces et al., 2004) and followed the interaction network depicted in Figure 5A. We further assumed that the rates of interconversion between KaiC phosphoforms for Anabaena are similar to those measured previously (Rust et al., 2007) in a reconstituted in vitro system consisting of KaiA, KaiB, and KaiC of Synechococcus (Appendix 1—table 2). This is supported by the fact that individual cells in both organisms exhibit oscillations with circadian periods (Figure 2C, Figure 4B) that in the case of Synechococcus are rather insensitive to changes in KaiC concentrations (Chew et al., 2018), constraining the values of these rates. Furthermore, KaiA of Anabaena, which is about two-thirds shorter than KaiA of Synechococcus, is similarly able to dimerize and enhance the phosphorylation of KaiC of other cyanobacteria in vitro, as well as elicit oscillations when its gene is transferred to Synechococcus cells, despite the evolutionary divergence between both organisms (Uzumaki et al., 2004). Individual cells can therefore display self-sustained oscillations only if the parameters $\gamma$ and [KaiA] take values inside the colored region of Figure 5C. These oscillations are characterized by a circadian period only within a narrow strip near the stability boundary. The fluorescence intensity is assumed to reflect the output of the clock, with a phase difference as shown previously (Kushige et al., 2013). We hence calculated the power spectrum of the fluorescence signal on every cell along the filament and averaged together the results. The experimentally computed power spectrum shows a clear peak, which is nicely interpolated by the theoretically predicted curve (Figure 6C) upon adjusting the two fitting parameters, $\gamma$ and [KaiA]. Again, the fitted values position the system (diamond in Figure 5C) outside the region of deterministic order, suggesting that demographic noise could trigger the observed oscillations. To test the robustness of the fit, we have implemented a bootstrap procedure (see Materials and methods) by perturbing each kinetic parameter with respect to the values reported in Rust et al., 2007. The imposed perturbation was about 10% for each individual kinetic parameter. The obtained best fit estimates for [KaiA] and $\gamma$ were found to display a degree of variability of approximately 20%, with reference to averaged values reported in Figure 5C. The bifurcation line that sets the separation between the deterministic limit cycle and the stationary stable fixed point became modulated depending on the set of assigned kinetic constants. Each pair of fitted $\gamma$ and [KaiA] falls by definition in the domain where the deterministic oscillations are impeded and the stochastic finite size corrections drive the emergence of the resonant quasi-cycles.

![Figure 6.](https://cdn.elifesciences.org/articles/64348/elife-64348-fig6-v2.jpg)

**Figure 6.:** (A) Schematic representation of the Anabaena filament showing coupling of circadian clocks via cell-cell communication (red arrows). (B) Gillespie simulations of quasi-cycles of T-KaiC in a continuous stretch of 10 cells along a filament. The reaction parameters correspond to the diamond plotted in Figure 5C. The total amount of KaiC phosphoforms was set to 5000, and the number of steps of the Gillespie algorithm was $1.6\times10^{7}$. (C) Average power spectrum of single-cell fluorescence intensity along filaments (red symbols) fit to the data with the prediction from the stochastic model (blue line). The best fit values correspond to the diamond shown in Figure 5C. (D) Complex coherence function measuring the correlation expression from $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ in 35 cell segments at the frequency of temporal oscillations. Red full circles correspond to experimental data, blue squares represent the fit to the experimental data with the prediction of the stochastic model, and empty red circles represent the coherence function of the experimental data in which cells have been reshuffled. Lines between symbols are a guide to the eye. The fit was carried out by adjusting two parameters, the strength of the imposed spatial coupling and the characteristic scale of the exponential kernel, see Appendix 1. Remarkably, the range of the interaction as obtained from the fit is compatible with that estimated from the spatial autocorrelation depicted in Figure 2D. The intercell coupling was obtained from the fit in (C).

In Anabaena, the oscillations displayed by different cells along a filament are synchronized, most likely by cell-cell communication. To support further the notion of clock coupling, we studied the spatial coherence of noisy oscillations along an Anabaena filament. We assume that $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ expression reports faithfully the output of the clock, albeit with a delay due to the transduction of KaiC’s phosphorylation state up to activation of the promoter, probably by phosphorylated RpaA. To study spatial coherence, we calculated the complex coherence function (Marple, 1987), whose magnitude measures the degree of correlation between cells within a filament at different distances. As shown in Figure 6D, the coherence at the characteristic frequency of oscillations was a monotonically decaying function of distance, an observation that points to the existence of non-local interactions by cell-cell communication along the filament. As complementary evidence, we notice that the magnitude of the coherence function took a constant value when spatial correlations were broken by randomly reshuffling the position of the cells along the filament. Remarkably, the prediction of the stochastic model captures the experimental behavior, as shown in Figure 6C. The range of interaction of the exponential kernel is self-consistently quantified by the fitting strategy and yields a result that agrees with that obtained from the spatial autocorrelation analysis (Figure 2D). More specifically, this conclusion is consistent with the reduction of spatial autocorrelation in the expression of a clock-regulated gene when either cell-cell communication is perturbed or clock genes are deleted, and with the notion that inheritance following cell division alone cannot account for all the spatial variation of expression along filaments (Figure 2D). In Figure 6C, quasi-cycles recorded on different cells of the stochastic Anabaena model are depicted showing a remarkable degree of synchronization. In Appendix 1, the analysis is extended so as to account for both a constant and a decaying power-law kernel of interaction.

## Discussion

Anabaena, a model organism in which each cell has a well-defined number of neighbors with which it communicates, has enabled us to study one-dimensional arrays of circadian clocks in a multicellular organism in space and time by interrogating each cell individually. Remarkably, our experiments using a fluorescence reporter fused to the N-terminus of a clock-controlled protein show that filaments display large-amplitude oscillations, consistently with previous studies carried out in bulk cultures (Kushige et al., 2013). These oscillations, which run freely under constant light conditions and are therefore autonomous, are characterized by high spatial coherence and synchrony. In addition to inheritance following cell division as in unicellular Synechococcus (Amdaoud et al., 2007), the behaviors of both the spatial autocorrelation (Figure 2D) and the complex coherence function (Figure 6D) represent strong evidence that these two characteristics result from local coupling between clocks of neighboring cells due to cell-cell communication via septal junctions. It is unlikely that this coupling results from the direct cell-to-cell transfer of KaiA, KaiB, or KaiC clock components as septal junctions in Anabaena are known to serve as conduits of only small molecules including metabolites, nutrients, and small peptides (e.g., PatS-derived peptides involved in lateral inhibition during developmental pattern formation, mediated by SepJ; Corrales-Guerrero et al., 2015). We postulate that metabolic factors such as sugars, which are transferred between cells via FraC and FraD proteins (Mullineaux et al., 2008; Nürnberg et al., 2015), may affect the behavior of neighboring clocks, yielding an effective long-ranged coupling between clock inputs (e.g., redox state, glycogen abundance, and ATP/ADP ratio) across the filament (Cohen and Golden, 2015; Golden, 2020). This is consistent with the shorter decay of the spatial autocorrelation function of $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ fluorescence intensity, and with the reduced value of the synchronization index, measured in filaments of a strain in which the transport of sugars and/or other coupling factors is impaired ($Δ$sepJ/$Δ$fraCD). Of note, the value of the synchronization index in this strain is similar to that obtained for cells from different filaments. Thus, we have found that cells within a filament behave coordinately, whereas different filaments appear to be in different oscillatory phases. Nonetheless, coherent oscillations at the whole culture level were observed after light/darkness training of the cultures, showing that input signals can coordinate the circadian rhythm in cells from different filaments.

The high synchrony and spatial coherence observed in our experiments further suggest that circadian rhythms in Anabaena are not centrally coordinated as in higher multicellular organisms (Bell-Pedersen et al., 2005). In mammals, for instance, clocks in peripheral tissues are centrally coordinated from a central pacemaker in the brain, the suprachiasmatic nucleus (Reppert and Weaver, 2002). In plants such as Arabidopsis, recent studies revealed the existence of waves of gene expression across the whole plant and the response of cells to positional information (Gould et al., 2018), consistent with weak coupling between cells and supporting a more decentralized model of clock coordination in plants (Endo, 2016). High synchrony and spatial coherence may be viewed as a necessary adaptation following the transition from a unicellular to a multicellular lifestyle (Masuda et al., 2017), while preserving key architectural features, gating of the cell cycle by the circadian clock and robust response to stresses, supporting the notion that a filament represents the organismic unit in Anabaena.

Our single-cell measurements of gene expression from $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ indicated that the cell-cell variability along filaments as measured by $C⁢V^{2}$ is oscillating, achieving maxima approximately half-way during periods of increase of the fluorescence intensity. The phase difference between the oscillation in fluorescence intensity and its cell-cell variability is consistent with the phase of rpaA transcriptional oscillations observed in our RT-qPCR measurements. The oscillatory nature of $C⁢V^{2}$ in $P_{p⁢e⁢c⁢B-g⁢f⁢p}$ expression may be due to the relay of the signal of the core clock by the transcriptional oscillations of a transcription factor, here RpaA (Heltberg et al., 2019).

Our experiments, carried out under constant light conditions, that is, non-varying external cues, provide clear evidence of gating of the cell cycle by the circadian clock, as for Synechococcus and many other organisms (Mori, 2009). In Synechococcus, cell doubling times vary considerably with light intensity (Teng et al., 2013), and the cell cycle has no effect on the circadian clock, irrespective of the cell cycle rate (Mori et al., 1996; Mori and Johnson, 2001). Furthermore, as for Synechococcus (Mihalcescu et al., 2004; Mori et al., 1996; Yang et al., 2010), clock phase is faithfully inherited by any two daughters following cell division as illustrated in Figure 2C. In fact, the post-transcriptional design of cyanobacterial circadian circuits has been suggested to provide insulation from effects due to variable cell division rates (Paijmans et al., 2016). Cell doubling times in Anabaena can also vary significantly with light intensity (Zhao et al., 2007). The mechanism of how the circadian clock controls the timing of cell division has been studied in Synechococcus as well as in Synechocystis, and it has been suggested that phosphorylated RpaA regulates the bacterial tubulin-analog FtsZ, inhibiting the formation of the cytokinetic ring (Dong et al., 2010; Kizawa and Osanai, 2020). While the precise genetic and biochemical differences between the circadian clocks of Anabaena and Synechococcus remain to be elucidated, the presence of homologs of core clock components, output coupling factors such as RpaA (Schmelling et al., 2017), and cell division promoters such as FtsZ in Anabaena (Corrales-Guerrero et al., 2018) suggests that the mechanisms for gating in these two organisms may be similar. Note that ftsZ has an upstream putative RpaA binding site motif (see Figure 3—figure supplement 2). Interestingly, nitrogen-fixing cells – heterocysts – that are formed under nitrogen deprivation in Anabaena lose the ability to divide, and yet, the heterocyst-enriched fraction in bulk experiments has been shown to exhibit clear circadian oscillations (Kushige et al., 2013). This supports the notion that cell division does not affect the circadian clock in Anabaena as in Synechococcus.

The RT-qPCR results and their analysis provide conclusive and quantitative evidence for circadian oscillations in the expression of kai genes in Anabaena. The calculation of the synchronization index $R$ for different pairs of kai genes yields large and similar values, suggesting that the expression of the three genes is highly coordinated, consistent with their possible expression as an operon. Furthermore, a persistent homology analysis of the time series of the three genes yields clear evidence of oscillatory behavior, consistent with a circadian period. In agreement with microarray measurements (Kushige et al., 2013), the oscillations we detect are of small amplitude, similar to those of Synechocystis (Kucho et al., 2005; Beck et al., 2014), but unlike those of Synechococcus. Given that the oscillations in the expression of kai genes are small, but that of pecB and many other targets are large (Kushige et al., 2013), we reasoned that a possible way of transducing the core clock signal to clock-controlled genes may be furnished by the downstream transcription factor RpaA. The kai-dependent transcriptional oscillations of rpaA we observed in Anabaena suggest an additional level of regulation of clock-controlled genes, which differs from the post-translational mechanism observed in Synechococcus. In particular, the oscillations in kai genes are consistent with the existence of a transcription-translation feedback loop via RpaA (Markson et al., 2013). Indeed, a well-defined candidate binding site motif of RpaA is located upstream of the kai genes (Figure 3—figure supplement 2). Additional candidate binding site motifs of RpaA are found upstream of the rpaA locus itself as well as the pecBACEF operon. The mechanism behind the large-amplitude oscillatory behavior of rpaA transcription we observed remains to be elucidated.

In order to describe theoretically circadian oscillations in individual Anabaena filaments, we started by incorporating demographic noise into a deterministic model of a single clock that includes only the kai genes as a core, such as the one describing oscillations in Synechococcus, and then extended the model to one describing a one-dimensional array of coupled noisy clocks as in Anabaena. The stochastic models capture well the peaks of finite width in the power spectra of fluctuations observed in our experiments (Figure 5B, Figure 6C). Importantly, the parameters we obtain from the fits to the experimental power spectra lie well outside the region in parameter space where deterministic oscillations occur, and in particular, the smaller region corresponding to oscillations characterized by circadian periods. This strongly suggests that the oscillatory behavior may correspond to noise-seeded oscillations as observed in other systems (McKane and Newman, 2005), without the need of training by light-dark cycles. The noise-seeded enlargement of the range of biological parameters over which circadian oscillatory behavior can be observed may confer robustness to clocks, a decisive biological advantage. Robustness may enable proper circadian clock function of Anabaena under a variety of stresses, including those involved in metabolic rewiring and the ensuing differentiation in response to combined nitrogen deprivation (Herrero et al., 2016; Di Patti et al., 2018). In this context, note that Anabaena filaments display circadian oscillations under nitrogen-deprived conditions, as shown previously (Kushige et al., 2013). Lastly, the model also reproduces the spatial coherence of oscillations in filaments, providing independent evidence of clock coupling through cell-cell communication.

In spite of the fact that Kai protein copy numbers run in the thousands in Synechococcus, phase fluctuations between cells are readily visible both in our experiments and in previous ones (Chew et al., 2018; Chabot et al., 2007). Stochastic modeling indicates that these numbers may be needed to compensate for noise amplification introduced by the post-translational feedback loop provided by KaiA, and reducing the numbers of Kai proteins leads to lower clock precision (Chew et al., 2018). We point out that demographic noise may be more significant than the copy numbers of Kai proteins may suggest: the functional form of KaiC is hexameric, which further partitions into its different phosphoforms (Chew et al., 2018). In addition, it has been shown that KaiB spends most of its time in an inactive tetrameric state, preventing its interaction with other Kai proteins, and that KaiA also oscillates between active and inactive states by binding to KaiB (Tseng et al., 2017). Together, these regulatory contributions might reduce active KaiC-effective numbers, thereby increasing fluctuations.

While the copy numbers of Kai proteins in Anabaena have not been measured, it is likely that they are significantly smaller than in Synechococcus, given the low transcriptional levels observed in our RT-qPCR experiments, as well as in DNA microarrays (Kushige et al., 2013). The expression of kai genes in Synechocystis is weak (Kucho et al., 2005), and protein copy numbers are correspondingly small (Zavřel et al., 2019). Thus, demographic noise effects may be indeed at least as important in Anabaena as they are for Synechococcus. One may hypothesize that cell-cell communication and the resulting coupling of clocks compensate for the smaller number of Kai proteins, setting the high synchrony and spatial coherence we observe in Anabaena. The picture that emerges may be more general and applicable to other multicellular organisms (Gould et al., 2018).

The transition from unicellular to multicellular organisms demanded coordination between physiological processes in different cells in order to enhance organismal fitness and adaptation to stresses. This is true in particular of circadian clocks and the genes they regulate. By analyzing filaments at the individual cell level, we found concrete evidence supporting coordination mediated by cell-cell communication, allowing clocks in different cells to be coupled. Furthermore, the high synchrony and spatial coherence of cell clocks along filaments observed in the experiments suggest that cell-cell communication contributes significantly to these two properties. Our theoretical model of single core clocks and arrays thereof shows that far from being detrimental demographic noise may seed oscillations that can be synchronized by clock coupling. This provides a robust description of circadian oscillations in a multicellular organism such as Anabaena.

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
      <td>Strain, strain background (Anabaena)</td>
      <td>PpecB−gfp, WT</td>
      <td>This paper</td>
      <td></td>
      <td>Anabaena PCC 7120 WT, bearing a pecB promoter fusion to gfp</td>
    </tr>
    <tr>
      <td>Strain, strain background (Anabaena)</td>
      <td>PpecB−gfp, Δ⁢k⁢a⁢i⁢A⁢B⁢C</td>
      <td>This paper</td>
      <td></td>
      <td>Anabaena PCC 7120 deletion mutant of the k⁢a⁢i⁢A⁢B⁢C genes, bearing a pecB promoter fusion to gfp</td>
    </tr>
    <tr>
      <td>Strain, strain background (Anabaena)</td>
      <td>PhetR−gfp</td>
      <td>doi: 10.1371/journal.pgen.1005031</td>
      <td>CSL64</td>
      <td>Anabaena PCC 7120 WT, bearing a hetR promoter fusion to gfp</td>
    </tr>
    <tr>
      <td>Strain, strain background (Anabaena)</td>
      <td>PpecB−gfp, Δ⁢s⁢e⁢p⁢J/Δ⁢f⁢r⁢a⁢C/Δ⁢f⁢r⁢a⁢D</td>
      <td>This paper</td>
      <td></td>
      <td>Anabaena PCC 7120 deletion mutant of the s⁢e⁢p⁢J, f⁢r⁢a⁢C, f⁢r⁢a⁢D genes (CSVM141), bearing a pecB promoter fusion to gfp</td>
    </tr>
    <tr>
      <td>Strain, strain background (Synechococcus elongatus)</td>
      <td>YFP-SsrA</td>
      <td>This paper</td>
      <td>PCC 7942</td>
      <td>Synechococcus elongatus PCC 7942 (wild-type) expressing YFP- SsrA</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>EB2316 (plasmid)</td>
      <td>Addgene plasmid</td>
      <td>87753</td>
      <td>http://n2t.net/addgene: 87753</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSpark (plasmid)</td>
      <td>Canvax</td>
      <td>C0001</td>
      <td>https://lifescience.canvaxbiotech.com/wpcontent/uploads/sites/2/2015/08pSpark-DNA-Cloning.pdf</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCSRO s⁢a⁢c⁢B- containing cloning vector</td>
      <td>doi: 10.1128/JB.00181-13</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Fast SYBR Green Master Mix</td>
      <td>Applied Biosystems</td>
      <td>4385612</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QuantiTect Reverse Transcription kit</td>
      <td>QIAGEN</td>
      <td>205311</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Strains

Strains bearing a chromosomally encoded $P_{p⁢e⁢c⁢B-g⁢f⁢p}$, were obtained by conjugation with the following backgrounds: WT Anabaena sp. (also known as Nostoc sp.) strain PCC 7120; $Δ$sepJ/$Δ$fraCD, strain CSVM141 in which sepJ, fraC, and fraD were deleted (Nürnberg et al., 2015); $Δ$kaiABC in which the kaiABC genes were deleted (for details, see Appendix 1 – Supplemental methods), as recipients. Strain CSL64 bearing a chromosomally encoded $P_{h⁢e⁢t⁢R-g⁢f⁢p}$ transcriptional fusion in a WT background has been reported previously (Corrales-Guerrero et al., 2015). The S. elongatus strain containing the gene encoding a YFP-SsrA reporter whose expression is driven by the kaiBC promoter at neutral site II was constructed by transforming Synechococcus sp. PCC 7942 with plasmid EB2316 (Addgene plasmid # 87753; http://n2t.net/addgene:87753; RRID: Addgene 87753).

### Culture conditions

Strains and derived strains were grown photoautotrophically in BG11 medium containing NaNO3, supplemented with 20 mM HEPES (pH 7.5) with shaking at 180 rpm, at 30°C, as described previously (Corrales-Guerrero et al., 2013; Di Patti et al., 2018). Growth took place under constant illumination (10 µmol of photons [spectrum centered at 450 nm]) from a cool-white LED array. When required, streptomycin sulfate (Sm) and spectinomycin dihydrochloride pentahydrate (Sp) were added to the media at final concentrations of 2 µg/mL for liquid and 5 µg/mL for solid media (1% Difco agar). The densities of the cultures were adjusted so as to have a chlorophyll content of 2–4 µg/mL 24 hr prior to the experiment, following published procedures (Di Patti et al., 2018). For time-lapse measurements, filaments in cultures were harvested and concentrated 50-fold. Synechococcus cultures were grown as above, and when required, 7.5 µg chloramphenicol (Cm) was added.

### Samples for time-lapse microscopy

Strains were grown as described previously (Di Patti et al., 2018). When required, antibiotics, Sm and Sp were added to the media at final concentrations of 2 µg/mL for liquid and 5 µg/mL for solid media. The densities of the cultures, grown under an external LED array (15 µmol for about 5 days), were adjusted so as to have a chlorophyll a content of 2–4 µg/mL, 24 hr prior to the experiment following published procedures (Di Patti et al., 2018). For time-lapse, single-cell measurements of Anabaena, 5 µL of culture concentrated 100-fold were pipetted onto an agarose low-melting gel pad (1.5%) in BG11 medium containing NaNO3 and 10 mM NaHCO3, which was placed on a microscope slide. The pad with the cells was then covered with a #0 mm coverslip and then placed on the microscope at 30°C. The cells grew under light from both an external LED array (15 µmol) and tungsten halogen light (10 µmol, 3000K color). Under these illumination conditions, the doubling time of cells is similar to that in bulk cultures (Di Patti et al., 2018). The change in illumination conditions when transferring cells from bulk cultures to the microscope results in high synchronization within filaments. Images of about 10 different fields of view were taken every 30 min on a Nikon Eclipse Ti-E microscope controlled by the NIS-Elements software using a 60 N.A. 1.40 oil immersion phase contrast objective lens (Nikon plan-apochromat 60 1.40) and an Andor iXon X3 EMCCD camera. Focus was maintained throughout the experiment using a Perfect Focus System (Nikon). All the filters used are from Chroma. The filters used were ET480/40X for excitation, T510 as dichroic mirror, ET535/50M for emission (GFP set), ET500/20x for excitation, T515lp as dichroic mirror, and ET535/30m for emission (EYFP set), and ET430/24x for excitation, 505dcxt as dichroic mirror, and HQ600lp for emission (chlorophyll set). Samples were excited with a pE-2 fluorescence LED illumination system (CoolLED).

For measurements of Synechococcus, the cultures were grown as above to a OD750 of 0.3–0.4. Samples were then entrained by two light-dark cycles (12 hr–12 hr) before measurements commenced. The cultures were then diluted to a OD750 of 0.1 using BG11 medium, and 2 µL of the culture was pipetted onto a glass-bottom culture dish. A patterned pad prepared as above but solidified on an optical grating (Hadizadeh Yazdi et al., 2012) was placed atop the cell suspension. Then, 1.5% agarose melted in BG11, cooled to 37°C, was poured on top of the well to cover the pad. After solidifying this last layer, 5 mL of BG11 was added to the culture dishes to maintain the moisture level of the agarose pad during the experiment. This device was placed in the microscope, and time-lapse measurements were carried out as for Anabaena.

### RT-qPCR measurements

For RT-qPCR measurements, strains were grown under the same conditions as described above. When the cultures reached the beginning of their exponential phase, about 1.8 µg/mL of chlorophyll a content, they were entrained by two light-dark cycles (12 hr–12 hr) and then grown under constant light. Then, measurements were started 24 hr after, and total RNA was extracted from the PCC 7120 and $Δ$kaiABC cultures in two biological replicates, every 4 hr. For each sample, 20 mL of cells were collected by filtration and washed with buffer TE50 (50 mM Tris-HCl at pH 8.0, 100 mM EDTA). Cells were resuspended in 2 mL TE50 buffer, and then they were centrifuged at 11,500 g for 2 min at 4°C. Supernatant was then removed and cell pellets were flash-frozen in nitrogen liquid for storage at 80°C. Total RNA was isolated by using hot phenol as described (Mohamed and Jansson, 1989) with modifications. All samples were treated with DNase I, and RNA quantity and purity were assessed with a NanoDrop One spectrophotometer as well as by agarose gel electrophoresis.

For cDNA synthesis, 600 ng of total RNA of each sample were used for reverse transcription with the QuantiTect Reverse Transcription kit (QIAGEN). Then, PCR amplification of 17.4 ng of each cDNA was carried out using Fast SYBR Green Master Mix (Applied Biosystems) that includes an internal reference based on the ROX dye and specific primers (Appendix 1—table 2). The amplification protocol was one cycle at 95°C for 10 min, 40 cycles of 95°C for 15 s, and 60°C for 60 s. RT-qPCR was carried out using an Applied Biosystems StepOnePlus instrument equipped with the StepOne Software v2.3. After the amplification was completed, a melting point calculation protocol was carried out in order to check that only the correct product was amplified in each reaction. Reactions were run in triplicate in 3–4 independent experiments from two biological replicates. The transcript levels of kaiA (alr2884), kaiB (alr2885), kaiC (alr2886), pecB (alr0523), and rpaA (all0129) were normalized to the transcript levels of the housekeeping genes rnpB and all5167 (ispD) to obtain the Δct value. Relative gene expression was calculated as $2^{-Δ⁢Δ⁢c⁢t}$ (Pfaffl, 2001).

### Image segmentation

All image processing and data analysis were carried out using MATLAB (MathWorks). Filament and individual cell recognition was performed on phase contrast images using an algorithm developed in our laboratory. The program’s segmentation was checked in all experiments and corrected manually for errors in recognition. The total fluorescence from GFP (for Anabaena) and chlorophyll (autofluorescence) channels of each cell, as well as the cell area, was obtained as output for further statistical analysis.

### Analysis of synchronization and spatial correlations along filaments

Synchronization was measured by the order parameter proposed by Garcia-Ojalvo et al., 2004:

$$
R=\frac{⟨\mu^{2}⟩−⟨\mu⟩^{2}}{⟨f_{i}^{2}⟩−⟨f_{i}⟩^{2}¯}
$$

where $⟨⋅⟩$ denotes a time average, $.¯$ indicates an average over all cells, and µ denotes the average of the fluorescence intensity of each cell fi. Hence, $R$ is defined as the ratio of the standard deviation of $\mu⁢(t)$ to the standard deviation of fi, averaged over all cells. For the measurement of synchronization within the same filament, groups of 8–11 cells were chosen, whether separated or contiguous (sharing a common ancestor as determined from a lineage analysis). For evaluation of inter-filament synchronization, one cell per filament was chosen randomly in different fields of view. $R$ was then calculated, and this procedure was repeated for different choices of cells, at least three times for each experiment. All the evaluations of $R$ were carried out over a full period of oscillation in either one of the first two oscillations, except for the $Δ⁢k⁢a⁢i⁢A⁢B⁢C$ background, for which $R$ was calculated for an interval of 24 hr, during which other strains display the first full oscillation. The final result comprises the mean of at least three independent repeats in at least two independent experiments. Errors in the quoted values of $R$ therefore represent standard errors (SEM). Statistical analyses were performed in MATLAB using Mann–Whitney U-test.

The spatial autocorrelation function of fluorescence intensities along filaments was calculated using the autocorr MATLAB command with 30 lags from at least 25 filaments of 50 cells each and at least two independent experiments. For WT and $Δ$sepJ/$Δ$fraCD backgrounds, autocorrelation functions of individual filaments were calculated at maxima and minima of circadian oscillations and the results were averaged. For filaments of the $Δ⁢k⁢a⁢i⁢A⁢B⁢C$ background, autocorrelation functions were calculated at about 30 and 50 hr, corresponding to the first minimum and maximum of oscillations observed in filaments of WT background. The spatial autocorrelation function was calculated from the formula

$$
g_{k}=\frac{c_{k}}{c_{0}}
$$

where

$$
c_{k}=\frac{1}{N}\sumi=1N−k(f_{i}−f¯) (f_{i+k}−f¯)
$$

where fi denotes the fluorescence intensity in cell $i$ in a filament of $N$ cells.

### Robustness of Anabaena dataset fit to the Synechococcus parameters

Each kinetic parameter ($k$) was randomly selected from a Gaussian distribution centered at the nominal value ($k¯$) estimated by Rust et al., 2007 using the normrnd MATLAB function. The standard deviation is assigned as $\sigma=k¯/10$. For every complete set of (randomly selected) kinetic constants, we proceeded with the fit of $\gamma$ and [KaiA] to interpolate the experimental power spectrum. Each pair of fitted values was stored to eventually compute averaged estimates, together with the error, as quantified by the associated standard deviation. By averaging over 200 independent realizations of the implemented procedure yields $\gamma=7.2\pm1.4$ and [KaiA] $=1.3\pm0.24$ (mean ± SD).

# Rapid regulation of vesicle priming explains synaptic facilitation despite heterogeneous vesicle:Ca2+ channel distances

## Authors

- Janus RL Kobbersmed<sup>1</sup> ([ORCID: 0000-0003-0313-6205](https://orcid.org/0000-0003-0313-6205))
- Andreas T Grasskamp<sup>3</sup> ([ORCID: 0000-0002-5895-6529](https://orcid.org/0000-0002-5895-6529))
- Meida Jusyte<sup>3</sup> ([ORCID: 0000-0001-9948-871X](https://orcid.org/0000-0001-9948-871X))
- Mathias A Böhme<sup>3</sup> ([ORCID: 0000-0002-0947-9172](https://orcid.org/0000-0002-0947-9172))
- Susanne Ditlevsen<sup>1</sup> ([ORCID: 0000-0002-1998-2783](https://orcid.org/0000-0002-1998-2783))
- Jakob Balslev Sørensen<sup>2</sup> ([ORCID: 0000-0001-5465-3769](https://orcid.org/0000-0001-5465-3769)) †
- Alexander M Walter<sup>3</sup> ([ORCID: 0000-0001-5646-4750](https://orcid.org/0000-0001-5646-4750)) †

### Affiliations

1. Department of Mathematical Sciences, University of Copenhagen København Denmark
2. Department of Neuroscience, University of Copenhagen København Denmark
3. Molecular and Theoretical Neuroscience, Leibniz-Forschungsinstitut für Molekulare Pharmakologie, FMP im CharitéCrossOver Berlin Germany
4. Einstein Center for Neuroscience Berlin Germany

† Corresponding author

## Abstract

Chemical synaptic transmission relies on the Ca2+-induced fusion of transmitter-laden vesicles whose coupling distance to Ca2+ channels determines synaptic release probability and short-term plasticity, the facilitation or depression of repetitive responses. Here, using electron- and super-resolution microscopy at the Drosophila neuromuscular junction we quantitatively map vesicle:Ca2+ channel coupling distances. These are very heterogeneous, resulting in a broad spectrum of vesicular release probabilities within synapses. Stochastic simulations of transmitter release from vesicles placed according to this distribution revealed strong constraints on short-term plasticity; particularly facilitation was difficult to achieve. We show that postulated facilitation mechanisms operating via activity-dependent changes of vesicular release probability (e.g. by a facilitation fusion sensor) generate too little facilitation and too much variance. In contrast, Ca2+-dependent mechanisms rapidly increasing the number of releasable vesicles reliably reproduce short-term plasticity and variance of synaptic responses. We propose activity-dependent inhibition of vesicle un-priming or release site activation as novel facilitation mechanisms.

## Introduction

At chemical synapses, neurotransmitters (NTs) are released from presynaptic neurons and subsequently activate postsynaptic receptors to transfer information. At the presynapse, incoming action potentials (APs) trigger the opening of voltage gated Ca2+ channels, leading to Ca2+ influx. This local Ca2+ signal induces the rapid fusion of NT-containing synaptic vesicles (SVs) at active zones (AZs) (Südhof, 2012). In preparation for fusion, SVs localize (dock) to the AZ plasma membrane and undergo functional maturation (priming) into a readily releasable pool (RRP) (Kaeser and Regehr, 2017; Verhage and Sørensen, 2008). These reactions are mediated by an evolutionarily highly conserved machinery. The SV protein VAMP2/Synaptobrevin and the plasma membrane proteins Syntaxin-1 and SNAP25 are essential for docking and priming and the assembly of these proteins into the ternary SNARE complex provides the energy for SV fusion (Jahn and Fasshauer, 2012). The SNARE interacting proteins (M)Unc18s and (M)Unc13s (where ‘M’ indicates mammalian) are also essential for SV docking, priming and NT release (Rizo and Südhof, 2012; Südhof and Rothman, 2009), while Ca2+ triggering of SV fusion depends on vesicular Ca2+ sensors of the Synaptotagmin family (Littleton and Bellen, 1995; Südhof, 2013; Walter et al., 2011; Yoshihara et al., 2003). Cooperative binding of multiple Ca2+ ions to the SV fusion machinery increases the probability of SV fusion (pVr) in a non-linear manner (Bollmann et al., 2000; Dodge and Rahamimoff, 1967; Schneggenburger and Neher, 2000).

A distinguishing feature of synapses is their activity profile upon repeated AP activation, where responses deviate between successive stimuli, resulting in either short-term facilitation (STF) or short-term depression (STD). This short-term plasticity (STP) fulfils essential temporal computational tasks (Abbott and Regehr, 2004). Postsynaptic STP mechanisms can involve altered responsiveness of receptors to NT binding, while presynaptic mechanisms can involve alterations in Ca2+ signalling and –sensitivity of SV fusion (von Gersdorff and Borst, 2002; Zucker and Regehr, 2002). Presynaptic STD is often attributed to high pVr synapses, where a single AP causes significant depletion of the RRP. In contrast, presynaptic STF has often been attributed to synapses with low initial pVr and a rapid pVr increase during successive APs. This was often linked to changes in Ca2+ signalling, for instance by rapid regulation of Ca2+ channels (Borst and Sakmann, 1998; Nanou and Catterall, 2018), saturation of local Ca2+ buffers (Eggermann et al., 2012; Felmy et al., 2003; Matveev et al., 2004), or the accumulation of intracellular Ca2+ which may increase pVr either directly or via ‘facilitation sensors’ (Jackman and Regehr, 2017; Katz and Miledi, 1968). Alternatively, fast mechanisms increasing the RRP were proposed (Fioravante and Regehr, 2011; Gustafsson et al., 2019; Pan and Zucker, 2009; Pulido and Marty, 2017).

The coupling distance between Ca2+ channels and primed SVs is an important factor governing pVr (Böhme et al., 2018; Eggermann et al., 2012; Stanley, 2016). Previous mathematical models describing SV fusion rates from simulated intracellular Ca2+ transients have in many cases relied on the assumption of uniform (or near uniform) distances between SV release sites surrounding a cluster of Ca2+ channels and such conditions were shown to generate STF (Böhme et al., 2016; Meinrenken et al., 2002; Nakamura et al., 2015; Vyleta and Jonas, 2014). However, alternative SV release site:Ca2+ channel topologies have been proposed, including two distinct perimeter distances, tight, one-to-one connections of SVs and channels, or random placement of either the channels, the SVs, or both (He et al., 2019; Böhme et al., 2016; Chen et al., 2015; Guerrier and Holcman, 2018; Keller et al., 2015; Shahrezaei et al., 2006; Stanley, 2016; Wong et al., 2014). So far, the precise relationship between SV release sites and voltage gated Ca2+ channels on the nanometre scale is unknown for most synapses, primarily owing to technical difficulties to reliably map their precise spatial distribution. However, (M)Unc13 proteins were recently identified as a molecular marker of SV release sites (Reddy-Alla et al., 2017; Sakamoto et al., 2018) and super-resolution (STED) microscopy revealed that these sites surround a cluster of voltage gated Ca2+ channels in the center of AZs of the glutamatergic Drosophila melanogaster neuromuscular junction (NMJ) (Böhme et al., 2016; Böhme et al., 2019).

Here, by relying on the unique advantage of being able to precisely map SV release site:Ca2+ channel topology we study its consequence for short-term plasticity at the Drosophila NMJ. Topologies were measured using electron microscopy (EM) following high pressure freeze fixation (HPF) or STED microscopy of Unc13 which both revealed a broad distribution of Ca2+ channel coupling distances. Stochastic simulations were key to identify facilitation mechanisms in the light of heterogenous SV release site:Ca2+ channel distances. Contrasting these simulations to physiological data revealed that models explaining STF through gradual increase in pVr (from now on called ‘pVr-based models’) are inconsistent with the experiment while models of activity-dependent regulation of the RRP account for STP profiles and synaptic variance.

## Results

### Distances between docked SVs and Ca2+ channels are broadly distributed

We first set out to quantify the SV release site:Ca2+ channel topology. For this we analysed EM micrographs of AZ cross-sections and quantified the distance between docked SVs (i.e. SVs touching the plasma membrane) and the centre of electron dense ‘T-bars’ (where the voltage gated Ca2+ channels are located Fouquet et al. (2009); Kawasaki et al. (2004); Figure 1A). In wildtype animals, this leads to a broad distribution of distances (‘EM dataset wildtype’, Figure 1—figure supplement 1A; Böhme et al., 2016; Bruckner et al., 2017). At the Drosophila NMJ, the two isoforms Unc13A and –B confer SV docking and priming, but the vast majority (~95%) of neurotransmitter release and docking of SVs with short coupling distances is mediated by Unc13A (Böhme et al., 2016). We therefore investigated the docked SV distribution in flies expressing only the dominant Unc13A isoform (Unc13A rescue, see Materials and methods for exact genotypes) which showed a very similar, broad distribution of distances as wildtype animals (‘EM-dataset Unc13A rescue’) (Reddy-Alla et al., 2017; Figure 1A,B). In both cases, distance distributions were well described by a Rayleigh distribution (Figure 1B, Figure 1—figure supplement 1A, solid green lines). The EM micrographs studied here are a cut cross-section of a three-dimensional synapse. To derive the relevant coupling distance distribution for all release sites (including the ones outside the cross-section), the Rayleigh distribution was integrated around a circle (Figure 1C), resulting in the following probability density function (pdf, see Materials and methods for derivation):

$$
gx=\frac{\sqrt{2}}{\sqrt{\pi}⋅\sigma^{3}}⋅x^{2}⋅e^{-x^{2}/(2\sigma^{2})}
$$

![Figure 1.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig1-v2.jpg)

**Figure 1.:** (A) Example EM image of an NMJ active zone (AZ) obtained from a 3rd instar Drosophila larva expressing the dominant Unc13A isoform after high pressure freeze fixation (Unc13A rescue: elav-GAL4/+;;UAS-Unc13A-GFP/+;P84200/P84200). The image captures a T-bar cross section. For clarity, the T-bar is colored in light blue, SVs are indicated with circles, the outline of the presynaptic plasma membrane is shown (magenta). Docked SVs are marked with black circles (non-docked in magenta). Black scale bar: 50 nm. (B) Histogram of the distances of docked SVs to the T-bar center obtained from EM micrographs 19 SVs observed in n = 10 EM cross-sections/cells from at least two animals, the same distance measurements had previously been used for the analysis depicted in Figure 5 of Reddy-Alla et al. (2017). The solid green line is the fitted Rayleigh distribution (σ = 76.5154 nm, mean is 95.9 nm, standard deviation, SD is 50.1 nm). (C) The one-dimensional Rayleigh distribution (green line) is integrated in order to estimate the docked SV distance distribution in the whole presynapse. (D) The integrated Rayleigh distribution is more symmetric, and the mean increases to 122.1 nm. SD is 51.5 nm. (E) The three left example images show wildtype (w[1118]) AZs stained against Unc13A and imaged on a STED microscope. The right hand image shows the average fluorescence signal for 524 individual centered AZ images from 16 different NMJs and more than three different animals (see Materials and methods for details). White scale bars: 100 nm. (F) Histogram of fluorescence intensities against distance from the AZ center, as derived from the average STED image plotted together with the integrated Rayleigh distribution derived from the EM analysis (replotted from panel D), showing a close agreement between the two approaches. Additional EM analysis of wildtype flies and the analysis of an independent STED experiment are compared to the data depicted here in Figure 1—figure supplement 1. Used genotype: Unc13A rescue (panel A, B), w[1118] (panel E, F). Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all genotypes. Raw data corresponding to the depicted histograms can be found in the accompanying source data file (Figure 1—source data 1). Scripts used for analysis of average STED image and plotting of histograms in 1B and 1F can be found in accompanying source data zip file (Figure 1—source data 2).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Histogram (blue) of the distances of docked SVs to the T-bar center obtained from EM micrographs of Wild-type (w[1118]) animals (‘EM dataset 1’) plotted with a fitted Rayleigh distribution green, N = 5 animals, n = 11 AZs, mean of Rayleigh distibution = 92.83 nm, SD is 48.5 nm; the same distance measurements had been used for the analysis depicted in Figure 6 of Böhme et al. (2016). (B) Integrated distributions of ‘EM dataset 2’ (Figure 1B, Unc13A rescue, black) with a mean of 122.1 nm and SD of 51.5 nm and of ‘EM dataset 1’ with a mean of 118.9 nm (blue) and SD of 49.9 nm. (C) Average images of ‘STED dataset 1’ (replotted from Figure 1E, green box) (N = 3 animals, n = 524 AZs) and ‘STED dataset 2’ (red box) (N = 3 animals, n = 586 AZs). (D) Overlay of the distance distributions derived from all four (two EM and two STED) datasets. Used genotypes: w[1118] (‘EM dataset 2’, panel A-D), Unc13A rescue: elav-GAL4/+;;UAS-Unc13A-GFP/+;P84200/P84200 (‘EM dataset 1’, panel B, D). Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all exact genotypes.

These pdfs were more symmetrical than the ones from the cross-sections and peaked at larger distances (as expected from the increase in AZ area with increasing radius) (Figure 1D). The estimation of this pdf was very robust, resulting in near identical curves for the two EM datasets (Figure 1—figure supplement 1B).

We also used an independent approach to investigate the distribution of docked SV:Ca2+ channel coupling distances without relying on the integration of docked SV observations from cross-sections: since (M)Unc13 was recently described as a molecular marker of SV release sites (Reddy-Alla et al., 2017; Sakamoto et al., 2018) we investigated AZ images of wildtype NMJs stained against Unc13A (Böhme et al., 2019). Hundreds of individual AZ STED images (lateral resolution of approx. 40 nm) were aligned and averaged to obtain an average image of the AZ (Figure 1E), which revealed a ring-like distribution of the Unc13A fluorescence. In previous works we had established that the voltage gated Ca2+ channels reside in the center of this ring (Böhme et al., 2016). As this average image already reflects the distribution throughout the AZ area (unlike for the EM data above where an integration was necessary) the distribution of coupling distances can directly be computed based on pixel intensities and their distance to the AZ centre. Two independent datasets where analysed, resulting in very similar average images and distance distributions (‘wildtype STED dataset 1 and 2’, Figure 1—figure supplement 1).

Remarkably, although the two approaches (EM and STED microscopy) were completely independent, the distributions of coupling distances quantified by either method coincided very well (Figure 1F, Figure 1—figure supplement 1D; note that the integrated Rayleigh distributions were determined from EM micrographs and integration; they were NOT fit to the Unc13A distribution), supporting the accuracy of this realistic release site topology. The compliance between SV docking positions and Unc13A distribution further indicates that SVs dock to the plasma membrane where priming proteins are available, and therefore the entire distribution of docked SVs is potentially available for synaptic release (Imig et al., 2014).

### Physiological assessment of short-term facilitation and depression at the Drosophila NMJ

Having identified the high degree of heterogeneity in the docked SV:Ca2+ channel coupling distances, we became interested in how this affected synaptic function. We therefore characterized synaptic transmission at control NMJs (Ok6-GAL4 crossed to w[1118]) in two electrode voltage clamp experiments. A common method to quantitatively evaluate synaptic responses and their STP behaviour is to vary the Ca2+ concentration of the extracellular solution which affects AP-induced Ca2+ influx (see below). We used this approach and investigated responses evoked by repetitive (paired-pulse) AP stimulations (10 ms interval). In line with classical studies (Dodge and Rahamimoff, 1967), our results display an increase of the evoked Excitatory Junctional Current (eEJC) responses to the first AP (eEJC1 amplitudes) with increasing extracellular Ca2+ (Figure 2A,B). STP was assessed by determining the paired-pulse ratio (PPR): the amplitude of the second response divided by first. The eEJC2-amplitude was determined taking the decay of eEJC1 into account (see insert in Figure 2C, Figure 2—figure supplement 1A). At low extracellular Ca2+ (0.75 mM), we observed strong STF (with an average PPR value of 1.80), which shifted towards depression (PPR < 1) with increasing Ca2+ concentrations (Figure 2C,D). Thus, the same NMJ displays both facilitation and depression depending on the extracellular Ca2+ concentration, making this a suitable model synapse to investigate STP behaviour.

![Figure 2.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig2-v2.jpg)

**Figure 2.:** Two-electrode voltage clamp recordings of AP-evoked synaptic transmission in muscle 6 NMJs (genotype: Ok6-GAL4/+ (Ok6-Gal4/II crossed to w[1118])). Left panel (A, C, E) shows example traces from one cell. Right panel (B, D, F) shows quantification across cells. (A) Representative eEJC traces from a single cell measured at different Ca2+ concentrations (0.75–10 mM). (B) Average eEJC1 amplitudes and SD from six animals as a function of extracellular Ca2+ concentration. (C) Representative eEJC traces of paired pulse paradigm (10 ms inter-stimulus interval, normalized to eEJC1) from single cell measured at different Ca2+ concentrations (0.75–10 mM). While STF can be seen at the two lowest extracellular Ca2+ concentrations (0.75 and 1.5 mM), the cell exhibits STD for extracellular Ca2+ concentrations of 3 mM or more. Insert (gray background) shows calculation of eEJC2. An exponential function was fitted to the decay to estimate the baseline for the second response (see Figure 1—figure supplement 1 and Materials and methods for details). (D) Mean and SD of PPR values (6 cells from six animals) at different Ca2+ concentrations. (E) Experiment to assess variance of repeated synaptic responses in a single cell. eEJC1 traces in response to nine consecutive AP stimulations (10 s interval) are shown (orange lines) together with the mean eEJC1 response (black line) at different extracellular Ca2+ concentrations (0.75–10 mM, see Materials and methods). (F) Plot of mean eEJC1 variance as a function of the mean eEJC1 amplitude across 6 cells from six animals for each indicated Ca2+ concentration. The curve shows best fitted parabola with intercept forced at (0,0) (Var = −0.0061*<eEJC1>2+0.6375 nA*<eEJC1>, corresponding to nsites = 164 and q = 0.64 nA when assuming a classical binomial model (Clements and Silver, 2000), see Materials and methods). For the variance-mean relationship of the single cell depicted in Figure 2E , please refer to Figure 2—figure supplement 2. Experiments were performed in Ok6-Gal4/+ 3rd instar larvae, often used as a control genotype for experiments using cell-specific driver lines. Separate experiments were performed to ensure that this genotype showed similar synaptic responses and STP behavior as wildtype animals (Figure 2—figure supplement 3). Used genotype: Ok6-Gal4/II crossed to w[1118]. Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all exact genotypes. Data points depict means, error bars are SDs across cells except in (F), where error bars show SEM. Raw data corresponding to the depicted graphs can be found in the accompanying source data file (Figure 2—source data 1). Scripts for analysis of recorded traces are found in accompanying source data zip file (Figure 2—source data 2). Raw traces from paired-pulse experiments summarized in Figure 2 and Figure 2—figure supplements 2 and 3 can be found in Figure 2—source data 2; Figure 2—figure supplement 1—source data 1; Figure 2—figure supplement 3—source data 1. Estimation of eEJC2 amplitudes and fitting of a smooth mEJC function (used in simulations, see Materials and methods) are illustrated in Figure 2—figure supplement 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Analysis of eEJCs. The eEJC1 amplitude is determined as the first minimum within 10 ms of the stimulus. The eEJC2 amplitude is determined from the baseline found by exponential extrapolation of the eEJC1 decay. (B) The mean mEJC from experimental recordings and the best fit used for convolution (see Materials and methods). Used genotype: Ok6-Gal4/II crossed to w[1118]. Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all exact genotypes.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Example traces showing nine individual stimulation sweeps (orange) per Ca2+ concentration (0.75–10 mM). Averages of single sweeps are shown in black. (B) Quantification of eEJC amplitudes of single sweeps (orange) at different Ca2+ concentrations. Scattering of these values illustrates the variance of eEJC amplitudes between individual sweeps. Average eEJC amplitudes per Ca2+ concentration are indicated in black, error bars show SDs. Average amplitudes (and their variance) shown here were used in C. (C) Variances of eEJC amplitudes in this cell (from nine repetitions per Ca2+ concentration, indicated in blue) plotted as a function of the mean eEJC amplitude. A parabola can be fitted to the data points (forced through (0,0) intercept, see Materials and methods for futher information and exact genoytpes). Used genotype: Ok6-Gal4/II crossed to w[1118]. Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all exact genotypes.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Electrophysiological recordings of muscle 6 NMJs upon a paired-pulse stimulation (10 ms inter-stimulus interval) at 0.75 mM (A-D) and 1.5 mM Ca2+(E-H). (A) Representative example traces for eEJC1 from single cells in +/+ or Ok6-Gal4/+. (B) Quantification of eEJC1 amplitudes in +/+ (n = 6 cells from three animals) and Ok6-Gal4/+ (n = 8 cells from four animals), averages and SDs across cells are indicated. (C) Representative normalized eEJC example traces of paired pulse (10 ms inter-stimulus interval) responses in representative cells of +/+ and Ok6-Gal4/+ animals. (D) Quantification of paired pulse ratios (PPRs) in +/+ (n = 6 cells from three animals) and Ok6-Gal4/+ (n = 8 cells from four animals), averages across cells and SDs are indicated. (E) Representative example traces for eEJC1 from single cells of +/+ or Ok6-Gal4/+ animals. (F) Quantification of eEJC1 amplitudes in +/+ (n = 5 cells from three animals) and Ok6-Gal4/+ (n = 5 cells from three animals), averages and SDs across cells are indicated. (G) Normalized eEJC example traces of paired pulse (10 ms inter-stimulus interval) from single cells in +/+ and Ok6-Gal4/+ animals. (G) Quantification of PPRs in +/+ (n = 5 cells from three animals) and Ok6-Gal4/+ (n = 5 cells from three animals), averages across cells and STDs are indicated. Used genotypes: Ok6-GAL4/+ (Ok6-Gal4/II crossed to w[1118]) and +/+: w[1118]. Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all exact genotypes.

In panels B and D the mean eEJC1 amplitudes and PPRs from six animals are shown and the error bars indicate standard deviation, SD (across all animals). We also examined the variation of repeated AP-evoked responses at the same NMJ between trials (10 s apart) at different extracellular Ca2+ concentrations (Figure 2E,F). At low concentrations (0.75 mM), the probability of transmitter release is low, resulting in a low mean eEJC1 amplitude with little variation (Figure 2E,F, Figure 2—figure supplement 2 ). With increasing extracellular Ca2+, the likelihood of SV fusion increased and initially so did the variance (e.g. at 1.5 mM extracellular Ca2+). However, further increase in extracellular Ca2+ (3 mM, 6 mM, 10 mM) led to a drop in variance (Figure 2E, Figure 2—figure supplement 2). Figure 2F depicts this average ‘variance-mean’ relationship from 6 cells (means of cell means and means of cell variances, error bars indicate SEM). When assuming a binomial model, this approach has often been used to estimate the number of release sites nsites and the size of the postsynaptic response elicited by a single SV (q) (Clements and Silver, 2000). In agreement with previous studies of the NMJ this relationship was well described by a parabola with forced intercept at y = 0 and nsites = 164 and q = 0.64 nA (Figure 2F, Figure 2—figure supplement 2; Matkovic et al., 2013; Müller et al., 2012; Weyhersmüller et al., 2011).

### Simulation of AP-induced Ca2+ signals

Having determined the distribution of coupling distances (Figure 1) and the physiological properties of the NMJ synapse (Figure 2), we next sought to compare how the one affected the other. There are two things two consider here. First of all, the SV release probability steeply depends on the 4th to 5th power of the local Ca2+ concentration (Neher and Sakaba, 2008). Secondly, because of the strong buffering of Ca2+ signals at the synapse, the magnitude of the AP-evoked Ca2+ transients dramatically declines with distance from the Ca2+ channel (Böhme et al., 2018; Eggermann et al., 2012). These two phenomena together make the vesicular release probability extremely sensitive to the coupling distance to the Ca2+ channels. Because we find that this distance is highly heterogeneous among SVs within the same NMJ, the question arises how these two properties (heterogeneity of distances combined with a strong distance dependence of pVr) functionally impact on synaptic transmission. Indeed, approaches by several labs to map the activity of individual NMJ AZs revealed highly heterogeneous activity profiles (Akbergenova et al., 2018; Gratz et al., 2019; Muhammad et al., 2015; Peled and Isacoff, 2011).

To quantitatively investigate the functional impact of heterogeneous SV placement, we wanted to use mathematical modelling to predict AP-induced fusion events of docked SVs placed according to the found distribution. A prerequisite for this is to first faithfully simulate local, AP-induced Ca2+ signals throughout the AZ (such that the local transients at each docking site are known). We first determined the relevant AZ dimensions at the Drosophila NMJ, which, similarly to the murine Calyx of Held, is characterized by many AZs operating in parallel. We therefore followed previous suggestions from the Calyx using a box with reflective boundaries containing a cluster of Ca2+ channels in the base centre (Meinrenken et al., 2002). The base dimensions (length = width) were determined as the mean inter-AZ distance of all AZs to their four closest neighbours (because of the 4-fold symmetry) from NMJs stained against the AZ-marker BRP (Kittel et al., 2006; Wagh et al., 2006; Figure 3A). To save computation time, we further simplified to a cylindrical simulation (where the distance to the Ca2+ channel is the only relevant parameter) covering the same AZ area (Figure 3B, Table 1).

**Table 1.**
 Parameters of Ca2+ and buffer dynamics.


<table>
  <thead>
    <tr>
      <th>Simulation volume</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>r</td>
      <td>Radius of cylindric simulation volume</td>
      <td>623.99 nm</td>
    </tr>
    <tr>
      <td>h</td>
      <td>Height of cylindric simulation volume</td>
      <td>1 µm</td>
    </tr>
    <tr>
      <td>ngrid</td>
      <td>Spatial grid points in CalC simulation</td>
      <td>71 × 101 (radius x height)</td>
    </tr>
    <tr>
      <td colspan="3">Ca2+</td>
    </tr>
    <tr>
      <td>Qmax</td>
      <td>Scaling of the total amount of Ca2+ charge influx</td>
      <td>Fitted (all models), see Table 2</td>
    </tr>
    <tr>
      <td>DCa</td>
      <td>Diffusion coefficient of Ca2+ (Allbritton et al., 1992)</td>
      <td>0.223 µm2/ms</td>
    </tr>
    <tr>
      <td>[Ca]bgr</td>
      <td>Background Ca2+</td>
      <td>[Ca2+]ext[Ca2+]ext+KM,current⋅190 nM</td>
    </tr>
    <tr>
      <td>KM,current</td>
      <td>Set to the same value as KM,fluo determined in GCaMP6 experiments</td>
      <td>2.679 mM</td>
    </tr>
    <tr>
      <td>Ca2+ uptake</td>
      <td>Volume-distributed uptake (Helmchen et al., 1997)</td>
      <td>0.4 ms−1</td>
    </tr>
    <tr>
      <td colspan="3">Buffer Bm (‘fixed’ buffer)</td>
    </tr>
    <tr>
      <td>DBm</td>
      <td>Diffusion coefficient</td>
      <td>0.001 µm2/ms</td>
    </tr>
    <tr>
      <td>KD,Bm</td>
      <td>Equilibrium dissociation constant (Xu et al., 1997)</td>
      <td>100 µM</td>
    </tr>
    <tr>
      <td>K+,Bm</td>
      <td>Ca2+ binding rate (Xu et al., 1997)</td>
      <td>0.1 (µM⋅ms)−1</td>
    </tr>
    <tr>
      <td>K-,Bm</td>
      <td>Ca2+ unbinding rate: KD,Bm⋅K+,Bm</td>
      <td>1 ms−1</td>
    </tr>
    <tr>
      <td>Total Bm</td>
      <td>Total concentration (bound+unbound) (Xu et al., 1997)</td>
      <td>4000 µM</td>
    </tr>
    <tr>
      <td colspan="3">Buffer ATP</td>
    </tr>
    <tr>
      <td>DATP</td>
      <td>Diffusion coefficient (Chen et al., 2015)</td>
      <td>0.22 µm2/ms</td>
    </tr>
    <tr>
      <td>KD,ATP</td>
      <td>Equilibrium dissociation constant (Chen et al., 2015)</td>
      <td>200 µM</td>
    </tr>
    <tr>
      <td>K+,ATP</td>
      <td>Ca2+ binding rate (Chen et al., 2015)</td>
      <td>0.5 (µM⋅ms)−1</td>
    </tr>
    <tr>
      <td>K-,ATP</td>
      <td>Ca2+ unbinding rate: KD,ATP⋅K+,ATP</td>
      <td>100 ms−1</td>
    </tr>
    <tr>
      <td>Total ATP</td>
      <td>Total concentration (bound+unbound) (Chen et al., 2015)</td>
      <td>650 µM</td>
    </tr>
    <tr>
      <td colspan="3">Resting Ca2+</td>
    </tr>
    <tr>
      <td>KM,current</td>
      <td>Michaelis Menten-constant of resting Ca2+ (same as KM,current of Ca2+ influx)</td>
      <td>2.679 mM</td>
    </tr>
    <tr>
      <td>[Ca2+]max</td>
      <td>Asymptotic max value of resting Ca2+</td>
      <td>190 nM</td>
    </tr>
  </tbody>
</table>

![Figure 3.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig3-v2.jpg)

**Figure 3.:** (A) Estimation of the simulation volume and Ca2+ simulations. The left hand image shows a confocal scan of a 3rd instar larval NMJ stained against the AZ marker Bruchpilot (BRP) (genotype: w[1118]; P{w[+mC]=Mhc-SynapGCaMP6f}3–5 (Bloomington Stock No. 67739). The right hand image shows a higher magnification of the indicated region. To determine the dimensions of the simulation volume, the average distance of each AZ to its closest four neighboring AZs (k-NND = kth nearest neighbor distance) was determined. The average inter-AZ distance to each of the closest four neighboring AZs (1- through 4-NND) is depicted on the left. Average and SEM of inter-AZ distances (1-4-NND) are depicted on the right. White scale bars: Left: 5 µm; right: 1 µm. (B) Example illustration of the Ca2+ simulation. The simulation volume is a cylinder whose base area (radius 624 nm) is the same as a square with side length of the mean 1–4-NND. The local Ca2+ concentration is shown at different time points following an AP-induced Gaussian Ca2+ current (the area/height is a free parameter, see Table 2, the FWHM is 0.36 ms). The simulation started at t=0 ms, Ca2+ influx was initiated at t=0.5 ms and peaked at t=2 ms. The Ca2+ (point) source is located in the AZ center (black dot) and the Ca2+ concentration is determined at 10 nm height from the plasma membrane. (C) Example simulation of the local Ca2+ concentration profile in response to stimulation with a pair of APs (current was initiated at 0.5 and 10.5 ms and peaked at 2 and 12 ms). Simulations were performed using the best fit parameters of the single sensor model described below (see Figure 4, Table 2). Top left: Ca2+ transients in response to the first AP at two distances: 95.9 nm and 122.1 nm (the mean of Rayleigh/integrated Rayleigh). Top right: AP-induced Ca2+ transient at 122.1 nm for all experimental extracellular Ca2+ concentrations. Bottom left: Semi-logarithmic plot of Ca2+ decays toward baseline after the 2nd transient (residual Ca2+) at different extracellular Ca2+ concentrations ([Ca2+]ext). Time constant of decay is τ = 111 ms. Bottom right: Residual Ca2+ levels at 122.1 nm after 10.5 ms of simulation as a function of extracellular Ca2+ concentrations. Data depicted in panel A were collected from 17 different animals. Used genotype: w[1118]; P{w[+mC]=Mhc-SynapGCaMP6f}3–5 (Bloomington Stock No. 67739, panel A). Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all exact genotypes. Values used for graphs can be found in the accompanying source data file (Figure 3—source data 1). GCaMP6m experiment is summarized in Figure 3—figure supplement 1. Ca2+ signals for all optimised models (below) are summarised in Figure 3—figure supplement 2.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Example frame of maximum fluorescence during recording of presynaptic GCaMP6m at 6 mM extracellular Ca2+. Red dotted line indicates the ROI used for read-out of the fluorescence signal. (B) 10 s fluorescence trace of experiment shown in A. At the 5 s mark, 20 APs are given over 1 s. Subtracting the fluorescence at 4.75 s from the maximum fluorescence gives the value dF plotted in panel D. (C) Baseline-subtracted fluorescence (see Materials and methods for details) traces of 5 different animals over the whole range of extracellular Ca2+ concentrations. 8.3 mM EGTA was added at the end to quench Ca2+ influx. (D) Quantification of dF (see panel B) per cell and Ca2+ concentration. The nonlinear fit with hill coefficient, m, of 2.43 (as previously determined for GCaMP6m Barnett et al., 2017) is indicated as a dashed black line, see Materials and methods for details. Mean is shown as black bars ± SEM. Used genotype: w[1118]; P{y[+t7.7] w[+mC]=20XUAS-IVS-GCaMP6m}attP40 crossed to Ok6-GAL4. Materials and methods section ‘Fly husbandry, genotypes and handling’ lists all exact genotypes. Data summary as well as best fit Hill curve corresponding to the depicted graph can be found in the accompanying source data file (Figure 3—source data 1).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Left: Both transients at 1.5 mM extracellular Ca2+ concentration at 95.9 nm and 122.1 nm. Middle: For all experimental extracellular Ca2+ concentrations an AP induced Ca2+ transient at a distance of 122.1 nm distance from the Ca2+ source is shown. Right: Semilogarithmic plot of Ca2+ decays at the different extracellular Ca2+ concentration. Time constant of decay is τ = 111 ms in all models. Plots of Ca2+ in the single-sensor model are the same as Figure 3C. Parameters can be found in Tables 1,2.

To simulate the electrophysiological experiments above, where the extracellular Ca2+ concentration was varied (Figure 2), it was important to establish how the extracellular Ca2+ concentration influenced AP-induced Ca2+ influx. In particular, it is known that Ca2+ currents saturate at high extracellular Ca2+ concentrations (Church and Stanley, 1996). Unlike other systems, the presynaptic NMJ terminals are not accessible to electrophysiological recordings, so we could not measure the currents directly. We therefore used a fluorescence-based approach as a proxy. AP-evoked Ca2+ influx was assessed in flies presynaptically expressing the Ca2+-dependent fluorescence reporter GCaMP6m (;P{y[+t7.7] w[+mC]=20XUAS-IVS-GCaMP6m}attP40/Ok6-GAL4). Fluorescence increase was monitored upon stimulation with 20 APs (at 20 Hz) while varying the extracellular Ca2+ concentration and showed saturation behaviour for high concentrations (Figure 3—figure supplement 1). This is consistent with a previously described Michaelis-Menten type saturation of fluorescence responses of a Ca2+-sensitive dye upon single AP stimulation at varying extracellular Ca2+ concentrations at the Calyx of Held, where half-maximal Ca2+ influx was observed at 2.6 mM extracellular Ca2+ (Schneggenburger et al., 1999). This relationship was successfully used in the past to predict Ca2+ influx in modeling approaches Trommershäuser et al. (2003). In our measurements, we determined a half maximal fluorescence response at a very similar concentration of 2.68 mM extracellular Ca2+ and therefore used this value as KM,current in a Michaelis-Menten equation (Materials and methods, Equation 5) to calculate AP-induced presynaptic Ca2+ influx. The second parameter of the Michaelis-Menten equation, (the maximal Ca2+ current charge, Qmax) was optimized for each model (Figure 3—figure supplement 2, for parameter explanations and best fit parameters see Table 2). We furthermore assumed that basal, intracellular Ca2+ concentrations at rest were also slightly dependent on the extracellular Ca2+ levels in a Michaelis-Menten relationship with the same dependency (KM,current) and a maximal resting Ca2+ concentration of 190 nM (resulting in 68 nM presynaptic basal Ca2+ concentration at 1.5 mM external Ca2+). With these and further parameters taken from the literature on Ca2+ diffusion and buffering (see Table 1) the temporal profile of Ca2+ signals in response to paired AP stimulation (10 ms interval) could be calculated at all AZ locations using the software CalC (Matveev et al., 2002; Figure 3C, Figure 3—figure supplement 2). This enabled us to perform simulations of NT release from vesicles placed according to the distribution described above.

**Table 2.**
 Best fit parameters of all models.


<table>
  <thead>
    <tr>
      <th colspan="4">Models presented in main figures</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Single-sensor model (Figure 4)</td>
      <td>Dual fusion-sensor model, cooperativity 2 (Figure 6)</td>
      <td>Unpriming model, cooperativity 5 (Figure 7)</td>
    </tr>
    <tr>
      <td>Qmax</td>
      <td>8.42 fC</td>
      <td>4.51 fC</td>
      <td>13.77 fC</td>
    </tr>
    <tr>
      <td>krep</td>
      <td>165.53 s−1</td>
      <td>159.30 s−1</td>
      <td>134.85 s−1</td>
    </tr>
    <tr>
      <td>nsites</td>
      <td>216</td>
      <td>211</td>
      <td>180</td>
    </tr>
    <tr>
      <td>k2</td>
      <td></td>
      <td>4.10e7 M−1s−1</td>
      <td></td>
    </tr>
    <tr>
      <td>s</td>
      <td></td>
      <td>510.26</td>
      <td></td>
    </tr>
    <tr>
      <td>u</td>
      <td></td>
      <td></td>
      <td>236.82 s−1</td>
    </tr>
    <tr>
      <td>kM,prim</td>
      <td></td>
      <td></td>
      <td>55.21 nM−1</td>
    </tr>
    <tr>
      <td>Cost value (see Materials and methods)</td>
      <td>9.689</td>
      <td>4.129</td>
      <td>0.340</td>
    </tr>
    <tr>
      <td colspan="4">Models presented in figure supplements</td>
    </tr>
    <tr>
      <td></td>
      <td>Dual fusion-sensor model, cooperativity 5 (Figure 6—figure supplement 1)</td>
      <td>Unpriming model, cooperativity 2 (Figure 7—figure supplement 1)</td>
      <td>Site activation model (Figure 7—figure supplement 3)</td>
    </tr>
    <tr>
      <td>Qmax</td>
      <td>8.10 fC</td>
      <td>13.49 fC</td>
      <td>12.59 fC</td>
    </tr>
    <tr>
      <td>krep</td>
      <td>492.56 s−1</td>
      <td>106.59 s−1</td>
      <td>141.20 s−1</td>
    </tr>
    <tr>
      <td>nsites</td>
      <td>112</td>
      <td>203</td>
      <td>189</td>
    </tr>
    <tr>
      <td>k2</td>
      <td>5.41e6 M−1s−1</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>s</td>
      <td>261.07</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>u</td>
      <td></td>
      <td>5207.70 s−1</td>
      <td></td>
    </tr>
    <tr>
      <td>kM,prim</td>
      <td></td>
      <td>7.61 nM−1</td>
      <td></td>
    </tr>
    <tr>
      <td>β</td>
      <td></td>
      <td></td>
      <td>0.09 s−1</td>
    </tr>
    <tr>
      <td>γ</td>
      <td></td>
      <td></td>
      <td>194.77 s−1</td>
    </tr>
    <tr>
      <td>δ</td>
      <td></td>
      <td></td>
      <td>10.70 s−1</td>
    </tr>
    <tr>
      <td>Cost value (see Materials and methods)</td>
      <td>2.941</td>
      <td>0.642</td>
      <td>1.57</td>
    </tr>
  </tbody>
</table>

### Stochastic simulations and fitting of release models

In the past, we and others have often relied on deterministic simulations based on numerical integration of kinetic reaction schemes (ordinary differential equations, ODEs). These are computationally effective and fully reproducible, making them well-behaved and ideal for the optimisation of parameters (a property that was also used here for initial parameter searches, see Materials and methods). However, NT release is quantal and relies on only a few (hundred) SVs, indicating that stochasticity plays a large role (Gillespie, 2007). Moreover, deterministic simulations always predict identical output making it impossible to analyse the synaptic variance between successive stimulations, which is a fundamental hallmark of synaptic transmission and an important physiological parameter (Figure 2F; Scheuss and Neher, 2001; Vere-Jones, 1966; Zucker, 1973). Stochastic simulations allow a prediction of variance which can help identify adequate models that will not only capture the mean of the data, but also its variance. To compare this, data points are now shown with error bars indicating the square root of the average variance between stimulations within a cell (Figure 4C, E, 6E, G and 7E, G). This is the relevant parameter since the model is designed to resemble an ‘average’ NMJ’ and therefore cannot predict inter-animal variance. Finally, as we show here deterministic simulations cannot be compared to experimentally determined PPR values because of Jensen’s inequality (full proof in Materials and methods, see Figure 4—figure supplement 1). Thus, stochastic simulations are necessary to account for SV pool sizes, realistic release site distributions, synaptic variance and STP. We thus implemented stochastic models of SV positions (drawn randomly from the distribution above) and SV Ca2+ binding states based on inhomogeneous, continuous time Markov models with transition rates governing reaction probabilities (see Materials and methods for details).

![Figure 4.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig4-v2.jpg)

**Figure 4.:** (A) Diagram of the single-sensor model. Consecutive binding of up to 5 Ca2+ ions to a vesicular Ca2+ sensor increases the probability of SV fusion (transition to state F) indicated by the color of the state. Primed SVs can be replenished from an infinite Vesicle pool. (B) Experimental eEJC traces averaged over all cells (black) together with average simulated traces (red). (C) eEJC1 amplitudes of experiment (black) and simulation (red). Error bars and colored bands show the standard deviations of data (see text) and simulations, respectively. Simulations reproduce eEJC1 amplitudes well. (D) Average (over all cells), normalized eEJC traces of experiment (black) and simulation (red). Simulations obtained with this model lack facilitation, as indicated by the red symbols. (E) PPR values of experiment (gray) and best fit simulation (blue). Green curve show simulations with replenishment 100x slower than the fitted value illustrating the effect of replenishment on the PPR. Error bars and colored bands show standard deviation. Best fit simulations do not reproduce the facilitation observed in the experiment at low extracellular Ca2+ concentrations. (F) Average simulated traces (red) and examples of different outcomes of the stochastic simulation (colors). (G) Plot of the mean synaptic variance vs. the mean eEJC1 amplitudes, both from the experiment (black) and the simulations (red). The curves show the best fitted parabolas with forced intercept at (0,0) (simulation: Var = −0.0041*<eEJC1>2+0.5669 nA*<eEJC1>, corresponding to nsites = 244 and q = 0.57 nA when assuming a classical binomial model (Clements and Silver, 2000), see Materials and methods). Simulations reveal too much variance in this model. Experimental data (example traces and means) depicted in panels B-E,G are replotted from Figure 2A–D,F. All parameters used for simulation can be found in Tables 1–3. Simulation scripts can be found in Source code 1. Results from simulations (means and SDs) can be found in the accompanying source data file (Figure 4—source data 1). Exploration of the difference between PPR estimations in deterministic and stochastic simulations are illustrated in Figure 4—figure supplement 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** PPR values from stochastic (bullets) and deterministic (curves) simulations of the single-sensor model (Figure 4) at varying amounts of Ca2+ influx. Simulations are performed with (blue) and without (red) replenishment. Decreasing Ca2+ influx increases the PPR values due to less SV depletion. Stochastic simulations generally yield higher PPR estimations than the deterministic simulations. The effect is most significant at the lower Ca2+ influx. Parameters used for simulation can be found in Tables 1–3. Simulation scripts can be found in Source code 1. Results from simulations (means) can be found in the accompanying source data file (Figure 4—source data 1).

We also needed to consider where new SVs would (re)dock once SVs had fused and implemented the simplest scenario of re-docking in the same positions. This ensures a stable distribution over time and agrees with the notion that vesicles prime into pre-defined release sites, which are stable over much longer time than a single priming/unpriming event (Reddy-Alla et al., 2017).

### A single-sensor model fails to induce sufficient facilitation and produces excessive variance

The first model we tested was the single-sensor model proposed by Lou et al. (2005), where an SV binds up to 5 Ca2+ ions, with each ion increasing its fusion rate or probability (Figure 4A, Table 3). Release sites were placed according to the distance distribution in Figure 1D and all sites were occupied by a primed SV prior to stimulation (i.e. the number of release sites equals the number of vesicles in the RRP). Sites becoming available following SV fusion were replenished from an unlimited vesicle pool, making the model identical to the one described by Wölfel et al. (2007). Ca2+ (un)binding kinetics were taken from Wölfel et al. (2007) Table 3, the values of the maximal Ca2+ current charge (Qmax), the SV replenishment rate (krep) and the number of release sites (nsites) were free parameters optimized to match the experimental data (see Materials and methods for details, best fit parameters in Table 2).

**Table 3.**
 Parameters of exocytosis simulation.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Explanation and reference</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Common parameters</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>nsites</td>
      <td>Number of release sites (=maximal number of SVs)</td>
      <td>Fitted (all models), see Table 2</td>
    </tr>
    <tr>
      <td>L+</td>
      <td>Basal fusion rate constant (Kochubey and Schneggenburger, 2011)</td>
      <td>3.5⋅10−4 s−1</td>
    </tr>
    <tr>
      <td>q</td>
      <td>Amplitude of the mEJC. Estimated from variance-mean of data (see Figure 2F)</td>
      <td>0.6 nA</td>
    </tr>
    <tr>
      <td>Fast sensor (all models)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>nmax</td>
      <td>Cooperativity, fast sensor (Lou et al., 2005; Schneggenburger and Neher, 2000; Wölfel et al., 2007)</td>
      <td>5</td>
    </tr>
    <tr>
      <td>k1</td>
      <td>Ca2+ binding rate, first sensor (Wölfel et al., 2007)</td>
      <td>1.4⋅108 M−1s−1</td>
    </tr>
    <tr>
      <td>k-1</td>
      <td>Ca2+ unbinding rate, first sensor (Wölfel et al., 2007)</td>
      <td>4000 s−1</td>
    </tr>
    <tr>
      <td>bf</td>
      <td>Cooperativity factor, first sensor (Lou et al., 2005; Wölfel et al., 2007)</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>kf</td>
      <td>Fusion rate constant of R(5,0) (fast sensor fully activated). (Lou et al., 2005; Schneggenburger and Neher, 2000; Wölfel et al., 2007)</td>
      <td>6000 s−1</td>
    </tr>
    <tr>
      <td>f</td>
      <td>⟮kfL+⟯15</td>
      <td>27.978</td>
    </tr>
    <tr>
      <td>Replenishment (all models)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>krep</td>
      <td>Replenishment rate constant</td>
      <td>Fitted (all models), see Table 2</td>
    </tr>
    <tr>
      <td>Slow sensor (dual fusion-sensor model)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>mmax</td>
      <td>Cooperativity, second fusion sensor</td>
      <td>2 (5 in figure supplement)</td>
    </tr>
    <tr>
      <td>KD</td>
      <td>Dissociation constant, second fusion sensor (Brandt et al., 2012)</td>
      <td>1.5 µM</td>
    </tr>
    <tr>
      <td>k2</td>
      <td>Ca2+ binding rate, second fusion sensor</td>
      <td>Fitted (dual fusion-sensor model), see Table 2</td>
    </tr>
    <tr>
      <td>k-2</td>
      <td>Ca2+ unbinding rate, second fusion sensor</td>
      <td>kD⋅k2</td>
    </tr>
    <tr>
      <td>bs</td>
      <td>Cooperativity factor, second fusion sensor (=bf)</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>s</td>
      <td>Second fusion sensor analogue of f: factor on the fusion rate</td>
      <td>Fitted (dual fusion-sensor model), see Table 2</td>
    </tr>
    <tr>
      <td>Unpriming (unpriming model)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>n</td>
      <td>Cooperativity (exponent in unpriming rate equation)</td>
      <td>5 (2 in figure supplement)</td>
    </tr>
    <tr>
      <td>u</td>
      <td>Rate constant of unpriming</td>
      <td>Fitted (unpriming model), see Table 2</td>
    </tr>
    <tr>
      <td>KM,prim</td>
      <td>Michaelis-Menten constant in expression of r</td>
      <td>Fitted (unpriming model), see Table 2</td>
    </tr>
    <tr>
      <td>Site activation (site activation model)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>n</td>
      <td>Cooperativity (exponent on [Ca2+]</td>
      <td>5</td>
    </tr>
    <tr>
      <td>α</td>
      <td>Rate constant [I] to [D]</td>
      <td>1e6 s-1</td>
    </tr>
    <tr>
      <td>β</td>
      <td>Rate constant [D] to [I]</td>
      <td>Fitted (site activation model), see Table 2</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>Rate constant [D] to [A]</td>
      <td>Fitted (site activation model), see Table 2</td>
    </tr>
    <tr>
      <td>δ</td>
      <td>Rate constant [A] to [D]</td>
      <td>Fitted (site activation model), see Table 2</td>
    </tr>
  </tbody>
</table>

To be able to compare the output of this and all subsequent models to experimental data as depicted in Figure 2 (postsynaptic eEJC measurements), the predicted fusion events were convolved with a typical postsynaptic response to the fusion of a single SV (mEJC, Figure 2—figure supplement 1B, see Materials and methods for more details). From the stochastic simulations (1000 runs each), we calculated the mean and variance of eEJC1 amplitudes, and the mean and variance of PPRs at various extracellular Ca2+ concentrations and contrasted these with the experimental data.

This single-sensor model was able to reproduce the eEJC1 values (Figure 4B,C). Moreover, the model accounted for the STD typically observed at high extracellular Ca2+ concentrations in the presence of rapid replenishment (Hallermann et al., 2010; Miki et al., 2016) (our best fit yielded τ ≈ 6 ms and reducing this rate led to unnaturally strong depression, Figure 4E, green curve+area). However, even despite rapid replenishment this model failed to reproduce the STF observed at low extracellular Ca2+ (Figure 4D,E) and the variances predicted by this model were much larger than found experimentally (Figure 4F,G). The observation that eEJC1 amplitudes were well accounted for, but STPs were not, may relate to the fact that this model was originally constructed to account for a single Ca2+-triggered release event (Lou et al., 2005). As this model lacks a specialized mechanism to induce facilitation, residual Ca2+ binding to the Ca2+ sensor is the only facilitation method which appears to be insufficient (Jackman and Regehr, 2017; Ma et al., 2015; Matveev et al., 2002). This result differs from our previous study using this model where we had placed all SVs at the same distance to Ca2+ channels which reliably produced STF (Böhme et al., 2016). So why does the same model fail to produce STF with this broad distribution of distances? To understand this we investigated the spatial distribution of SV release in simulations of the paired-pulse experiment at 0.75 mM extracellular Ca2+ (Figure 5).

![Figure 5.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig5-v2.jpg)

**Figure 5.:** (A) Two examples of docked SVs stochastically placed according to the distribution described in Figure 1D and their behavior in the PPR simulation at 0.75 mM extracellular Ca2+. For clarity, 10 SVs are shown per AZ (the actual number is likely lower) and only a central part of the AZ is shown. Top row: Prior to AP1 SVs are primed (dark gray circles) and pVr1 is indicated as numbers. The larger dashed, blue circle in the AZ center indicates pVr1 = 0.25. Second row: After AP1 some of the SVs have fused (dashed blue circles). Third row: Right before AP2 some of the SVs that had fused in response to AP1 have been replenished (orange shading), and pVr2 is indicated as a number. The larger dashed, red circle indicates pVr2 = 0.25. Bottom row: After AP2 the second release has taken place. Small dashed circles indicate release from AP1 and AP2 (blue and red, respectively). The small increase in pVr caused by Ca2+ accumulation cannot produce facilitation because of depletion of SVs. (B) The average simulation at the same time points as in (A). Histograms represent primed SVs (black and gray) as well as first and second release (blue and red) illustrating how release from AP1 and AP2 draw on the same subpopulation of SVs. The blue and red curves indicate the vesicular release probability as a function of distance during AP1 (blue) and AP2 (red). The green arrows show the repopulation of previously used sites via replenishment. AP2 draws on the same portion of the SV distribution as AP1 causing depression despite the fast replenishment mechanism. Parameters used for simulations can be found in Tables 1–3.

### In the absence of a facilitation mechanism, only part of the SV distribution is utilized

Figure 5A depicts two examples of synapses – seen from above – with SVs randomly placed according to the distance distribution in Figure 1D/5B. The synapse is shown immediately before AP1, immediately after AP1, immediately before AP2 (i.e. after refilling) and immediately after AP2 (the external Ca2+ concentration was 0.75 mM). From this analysis it becomes clear that the pVr1 caused by AP1 essentially falls to zero around the middle of the SV distribution (Figure 5B, top panel). This means that only SVs close to the synapse center fuse, and these high-pVr SVs are depleted by AP1. SV replenishment refills the majority (but not all) of those sites and thus AP2/pVr2 essentially draws on the same part of the distribution (Figure 5B, bottom panel). Because of this, and because the refilling is incomplete, this causes STD. Even with faster replenishment (which would be incompatible with the low PPR values at high extracellular Ca2+, Figure 4E) this scenario would only lead to a modest increase of the PPR to values around 1. Therefore, our analysis reveals that large variation in Ca2+ channel distances results in a specific problem to generate STF. Our analysis further indicates that with the best fit parameters of the single sensor model, the majority of SVs (those further away) is not utilized at all.

### A dual fusion-sensor model improves PPR values, but generates too little facilitation and suffers from asynchronous release and too much variance

The single-sensor model failed to reproduce the experimentally observed STF at low extracellular Ca2+ concentrations because of the dominating depletion of SVs close to Ca2+ channels, and the inability to draw on SVs further away. However, this situation may be improved by a second Ca2+ sensor optimized to enhance the pVr2 in response to AP2. Indeed, in the absence of the primary Ca2+ sensor for fusion, Ca2+ sensitivity of synaptic transmission persists, which was explained by a dual sensor model (Sun et al., 2007). It was recently suggested that syt-7 functions alongside syt-1 as a Ca2+ sensor for release (Jackman et al., 2016), and deterministic mathematical dual fusion-sensor model assuming homogeneous release probabilities (which implies homogeneous SV release site:Ca2+ channel distances) was shown to generate facilitation (Jackman and Regehr, 2017). Similarly, stochastic modelling of NT release at the frog NMJ also showed a beneficial effect of a second fusion sensor for STF (Ma et al., 2015). We therefore explored whether a dual fusion sensor model could account for synaptic facilitation from realistic release site topologies.

The central idea of this dual fusion-sensor model is that while syt-1 is optimized to detect the rapid, AP-induced Ca2+ transients (because of its fast Ca2+ (un)binding rates, but fairly low Ca2+ affinity), the cooperating Ca2+ sensor is optimized to sense the residual Ca2+ after this rapid transient (Figure 3C) (with slow Ca2+ (un)binding, but high Ca2+ affinity). The activation of this second sensor after (but not during) AP1 could then enhance the release probability of the remaining SVs for AP2 (Figure 6A,B). This is illustrated in Figure 6B, where k2 (the on-rate of Ca2+ binding to the slow sensor) is varied resulting in different time courses and amounts of Ca2+ binding to the second sensor. Increasing the release probability is equivalent to lowering the energy barrier for SV fusion (Schotten et al., 2015). In this model both sensors regulate pVr and therefore additively lower the fusion barrier with each associated Ca2+ ion (Figure 6A), resulting in multiplicative effects on the SV fusion rate. While the fast fusion reaction appears to have a 5-fold Ca2+ cooperativity (Bollmann et al., 2000; Burgalossi et al., 2010; Schneggenburger and Neher, 2000), it is less clear what the Ca2+ cooperativity of a second Ca2+ sensor may be, although the fact that the cooperativity is reduced in the absence of the fast sensor (Burgalossi et al., 2010; Kochubey and Schneggenburger, 2011; Sun et al., 2007) could be taken as evidence for a Ca2+ cooperativity < 5. We explored cooperativities 2, 3, 4, and 5 (cooperativities 2 and 5 are displayed in Figure 6 and Figure 6—figure supplement 1). It is furthermore not clear whether such a sensor would be targeted to the SV (like syt-1 /-2), or whether it is present at the plasma membrane. Both scenarios are functionally possible and it was indeed reported that syt-7 is predominantly or partly localized to the plasma membrane (Sugita et al., 2001; Weber et al., 2014). A facilitation sensor on the plasma membrane would be more effective, which our simulations confirmed (not shown), because it would not be consumed by SV fusion, allowing the sensor to remain activated. We therefore present this version of the model here. We used a second sensor with a Ca2+ affinity of KD = 1.5 μM (Brandt et al., 2012; Jackman and Regehr, 2017).

![Figure 6.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig6-v2.jpg)

**Figure 6.:** (A) Diagram of the dual fusion-sensor model (left). A second Ca2+ sensor for fusion with slower kinetics can increase pVr (indicated by color of each Ca2+ binding state). The second fusion sensor is assumed to act on the energy barrier in a similar way as the first sensor (right). The top right equation shows the relation between the fusion constant, kfuse, and energy barrier modulation with n and m being the number of Ca2+ bound to the first and second Ca2+ sensor, respectively. Ca2+ binding to the second sensor is described by similar equations as for the first sensor, but with different rate constants and impact on the energy barrier. (B) Simulation of Ca2+ binding to the fast (blue) and slow (other colors) Ca2+ sensor in simulations at 0.75 mM extracellular Ca2+ with different k2 values but with constant affinity (i.e. fixed ratio of k-2/k2). The binding is normalized to the maximal number of bound Ca2+ to each sensor (5 and 2, respectively). For illustration purposes in this graph the fusion rate was set to 0 (because otherwise the fast sensor (blue line) would be consumed by SV fusion). k2 = 4e7 M-1s-1 (red trace) illustrates the situation for the optimal performance of the model (approximately best fit value). (C) PPR values in stochastic simulations with the same parameter choices as in (B) but allowing fusion. (D) Experimental eEJC traces (black) together with average simulated traces (red). Simulations show too much asynchronous release compared to experiments. (E) eEJC1 amplitudes of experiment (black) and simulation (red). Error bars and colored bands show standard deviations of data and simulations, respectively. Simulations reproduce eEJC1 amplitudes well. (F) Average, normalized eEJC traces of experiment (black) and simulation (red). Simulations show too little facilitation compared to experiment. (G) PPR values of experiment (gray) and simulation (blue). Error bars and colored bands show standard deviation. Simulations show too little facilitation compared to experiment. (H) Average simulated traces (red) and examples of different outcomes of the stochastic simulation (colors). (I) Plot of the mean synaptic variance vs. the mean eEJC1 values, both from the experiment (black) and the simulations (red). Curves are the best fitted parabolas with forced intercept at (0,0) (simulation: Var = −0.0034*<eEJC1>2+0.5992 nA*<eEJC1>, corresponding to nsites = 294 and q = 0.60 nA when assuming a classical binomial model (Clements and Silver, 2000), see Materials and methods). Simulations lead to too much variance at the highest Ca2+ concentrations. (J) Parameter exploration of the second sensor varying the parameters Qmax, k2, and s. Each ball represents a choice of parameters and the color indicates the average PPR value in stochastic simulations with 0.75 mM extracellular Ca2+. None of the PPR values match the experiment (indicated by the black arrow). Black lines show the best fit parameters. (K) Same parameter choices as in (I). The colors indicate the number of RRP SVs in order to fit the eEJC1 amplitudes at the five different experimental Ca2+ concentrations. Black lines show the best fit parameters, and arrows show the experimental and best fit simulation values. Note that the best fit predicted more release sites than fluctuation analysis revealed in the experiment. Experimental data (example traces and means) depicted in panels D-G,I are replotted from Figure 2A–D,F. Parameters used for simulations can be found in Tables 1–3. Simulation scripts can be found in Source code 1. Results from simulations (means and SDs) can be found in the accompanying source data file (Figure 6—source data 1). Simulations of the dual fusion-sensor model with cooperativity 5 are summarized in Figure 6—figure supplement 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Average, experimental eEJC1 traces (black) together with average simulated traces (red). The higher cooperativity increases the PPR compared to cooperativity 2 (Figure 6), but introduces massive asynchronous release resulting in distorted eEJC shapes. (B) eEJC1 amplitudes of experiment (black) and simulation (red). Error bars and colored bands show standard deviation. Like with the three models described in the main text, simulations of this model reproduces eEJC1 amplitudes well, but the variance at the higher extracellular Ca2+ concentrations is too large. (C) Average, normalized eEJC traces of experiment (black) and simulation (red). Like in (A) the wrong shape of the eEJC is evident. (D) PPR values of experiment (gray) and simulation (blue). Error bars and colored bands show standard deviation. Despite the increase in PPR compared to the dual fusion-sensor model with cooperativity 2, the PPR is still too low. (E) Plot of the mean synaptic variance vs. the mean eEJC1 values, both from the experiment (black) and the simulation (red). The curves show the best fitted parabolas with forced intercept at (0,0) (simulation: Var = −0.00089*< eEJC1>2+0.6728 nA*< eEJC1>, corresponding to nsites = 1124 and q = 0.67 nA when assuming a classical binomial model (Clements and Silver, 2000), see Materials and methods). This model leads to an even larger overshoot of the variance than the dual fusion-sensor model with cooperativity 2 (Figure 6). Experimental data (example traces and means) depicted in panels A-E are replotted from Figure 2A–D,F. Parameter values used for simulations can be found in Tables 1–3. Simulation scripts can be found in Source code 1. Results from simulations (means and SDs) can be found in the accompanying source data file (Figure 6—source data 1).

Like for the single-sensor model, all release sites were occupied with releasable vesicles (nsites equals the number of RRP vesicles) and their locations determined by drawing random numbers from the pdf. When fitting this model five parameters were varied: Qmax, krep, and nsites (like in the single-sensor model) together with k2 (Ca2+ association rate constant to the second sensor) and s (the factor describing the effect of the slow sensor on the energy barrier for fusion) (see Table 2 for best fit parameters). The choice of k2 had an effect on the PPR in simulations, confirming that the second sensor was able to improve the release following AP2 (Figure 6C). Figure 6D–I show that the dual fusion-sensor model could fit the eEJC1 amplitudes and the model slightly improved the higher PPR values at the low- and the lower PPR values at high extracellular Ca2+ concentrations compared to the single sensor model (compare Figures 4E and 6G). However, the model failed to produce the STF observed experimentally (the PPR values at 0.75 mM Ca2+were ~ 1.08 in the simulation compared to ~ 1.80 in the experiments). Another problem of the dual fusion-sensor model was that release became more asynchronous than observed experimentally (Figure 6D), which was due to the triggering of SV fusion in-between APs. Finally, predicted variances were much larger than the experimental values (Figure 6I).

In addition to the optimization, we systematically investigated a large region of the parameter space (Figure 6J,K), but found no combination of parameters that would be able to generate the experimentally observed STF. Lowering the Ca2+ influx (by decreasing Qmax) yielded a modest increase in PPR values (Figure 6J), but required a large number of release sites (nsites) to match the eEJC1 amplitudes (Figure 6K). Changing s had the largest effect when k2 was close to the best fit value and moving away from this value decreased the PPRs, either by increasing the effect of the second sensor on AP1 (when increasing k2) or by decreasing the effect on AP2 (when decreasing k2), which both counteracts STF (Figure 6B,J).

Fitting the dual fusion-sensor model with a Ca2+ cooperativity of 5 did not improve the situation (Figure 6—figure supplement 1, best fit parameters in Table 2): Although slightly more facilitation was observed, this model suffered from even larger variance overshoots (Figure 6—figure supplement 1E) and excessive asynchronous release (Figure 6—figure supplement 1A,C). We explored different KD values between 0.5 and 2 μM at cooperativities 2–5 in separate optimizations, but found no satisfactory fit of the data (results not shown). Thus, a dual fusion-sensor model is unlikely to account for STF observed from the realistic SV release site topology at the Drosophila NMJ. Note that this finding does not rule out that syt-7 functions in STF, but argues against a role in cooperating alongside syt-1 in a pVr-based facilitation mechanism.

### Rapidly regulating the number of RRP vesicles accounts for eEJC1 amplitudes, STF, temporal transmission profiles and variances

Since dual fusion-sensor models and other models depending on changes in pVr (see Discussion) are unlikely to be sufficient, we next investigated mechanisms involving an activity-dependent regulation of the number of participating release sites. For this we extended the single-sensor model by a single unpriming reaction (compare Figures 4A and 7A). The consequence of reversible priming is that the initial release site occupation can be less than 100% (in which cases nsites can exceed the number of RRP vesicles). This enables an increase (‘overfilling’) of the RRP (/increase in site occupancy) during the inter-stimulus interval (consistent with reports in other systems Dinkelacker et al., 2000; Gustafsson et al., 2019; Pulido et al., 2015; Smith et al., 1998; Trigo et al., 2012). We assumed that Ca2+ would stabilize the RRP/release site occupation by slowing down unpriming (Figure 7A). This made the steady-state RRP size dependent on the resting Ca2+ concentration and the modest dependence of this on the extracellular Ca2+ resulted in RRP enlargement with increasing extracellular Ca2+ (Figure 7B), in agreement with recent findings on central synapses (Malagon et al., 2020). This model (like the dual fusion-sensor models depicted in Figure 6 and Figure 6—figure supplement 1) includes two different Ca2+ sensors, but the major difference is that these Ca2+ sensors operate to regulate two separate sequential steps (priming and fusion). Indeed, this scenario aligns with reports of a syt-7 function upstream of SV fusion (Liu et al., 2014; Schonn et al., 2008). Figure 7C shows how the number of RRP vesicles develops over time in this model during a paired-pulse experiment for low and high extracellular Ca2+ concentrations. In all cases, SV priming was in equilibrium prior to the first stimulus, indicated by the horizontal lines (0–2 ms, Figure 7C). Note that prior to AP1 priming is submaximal (~41%) for 0.75 mM extracellular Ca2+, but near complete (~99%) at 10 mM extracellular Ca2+. At low extracellular Ca2+ the elevation of Ca2+ caused by AP1 results in a sizable inhibition of unpriming, leading to an increase (‘overfilling’) of the RRP during the inter-stimulus interval. With this, more primed SVs are available for AP2, causing facilitation (green line in Figure 7C). In contrast, at high extracellular Ca2+ concentrations, the rate of unpriming is already low at steady state and the RRP close to maximal capacity (grey line in Figure 7C). At this high extracellular Ca2+ concentration, AP1 induces a larger Ca2+ current (higher pVr), resulting in strong RRP depletion, of which only a fraction recovers between APs (as in the other models, replenishment commences with a Ca2+ independent rate krep). Because Ca2+ acts in RRP stabilization, not in stimulating forward priming, this model (unlike the dual fusion-sensor models in Figure 6 and Figure 6—figure supplement 1) did not yield asynchronous release in-between APs (Figure 7D). Thus, the two most important features of this model are the submaximal site occupation and an inhibition of unpriming by intracellular Ca2+.

![Figure 7.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig7-v2.jpg)

**Figure 7.:** (A) Diagram of the unpriming model. The rate of unpriming decreases with the Ca2+ concentration. All other reactions are identical to the single-sensor model (Figure 4A). (B) Assumed basal Ca2+ concentration at different extracellular Ca2+ concentrations (red curve) together with the steady-state amount of priming (blue). Increasing basal Ca2+ concentration increases priming. (C) The average fraction of occupied release sites as a function of time in simulations with 0.75 mM (green) and 10 mM (gray) extracellular Ca2+ concentration. Release reduced the number of primed SVs. At 0.75 mM Ca2+, the Ca2+-dependent reduction of unpriming leads to ‘overfilling’ of the RRP between AP1 and AP2, thereby inducing facilitation. (D) Average experimental eEJC traces (black) together with average simulated traces (red). (E) eEJC1 amplitudes of experiment (black) and simulation (red). Error bars and colored bands show standard deviation. (F) Average, normalized eEJC traces of experiment (black) and simulation (red). (G) PPR values of experiment (gray) and simulation (blue). Error bars and colored bands show standard deviation. Simulations reproduce the experimentally observed facilitation. (H) Average simulated traces (red) and examples of different outcomes of the stochastic simulation (colors). (I) Plot of the mean synaptic variance vs. the mean eEJC1 values, both from the experiment (black) and the simulations (red). The curves show the best fitted parabolas with forced intercept at (0,0) (simulation: Var = −0.0053*<eEJC1>2+0.6090 nA*<eEJC1>, corresponding to nsites = 189 and q = 0.61 nA when assuming a classical binomial model (Clements and Silver, 2000), see Materials and methods). (J) Similar to Figure 6J. Parameter exploration of the unpriming model varying Qmax, kM,prim, and u (unpriming rate constant). Each ball represents a choice of parameters and the color indicates the PPR value. Black lines show the best fit parameters, and arrows show the experimental and best fit simulation values. (K) Same parameter choices as in (J). The colors indicate the optimal maximal number of SVs (i.e. number of release sites, nsites) in order to fit the eEJC1 amplitude at the five different Ca2+ concentrations. A large span of PPR values (shown in (J)) can be fitted with a reasonable number of release sites (shown in (K)). Experimental data (example traces and means) depicted in panels D-G,I are replotted from Figure 2A–D,F. Parameters used for simulation can be found in Tables 1–3. Simulation scripts can be found in Source code 1. Results from simulations (means and SDs) can be found in the accompanying source data file (Figure 7—source data 1). Simulations of the unpriming model with cooperativity two are summarized in Figure 7—figure supplement 1. The site activation model (described later) is introduced and results are summarized in Figure 7—figure supplement 3. Simulations of the unpriming model with various inter-stimulus intervals are summarized in Figure 7—figure supplement 2.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Average, experimental eEJC traces (black) together with average simulated traces (red). (B) eEJC1 amplitudes of experiment (black) and simulation (red). Error bars and colored bands show standard deviation. Like with the three models described in the main text, simulations of this model reproduce eEJC1 amplitudes well. (C) Average, normalized eEJC traces of experiment (black) and simulation (red). (D) PPR values of experiment (gray) and simulation (blue). Error bars and colored bands show standard deviation. Like the unpriming model with cooperativity 5 (Figure 7), this model reproduces the short-term facilitation observed in experiments. (E) Plot of the mean synaptic variance vs. the mean eEJC1 values, both from the experiment (black) and the simulation (red). The curves show the best fitted parabolas with forced intercept at (0,0)) (simulation: Var = −0.0042*< eEJC1>2+0.5648 nA*< eEJC1>, corresponding to nsites = 238 and q = 0.56 nA when assuming a classical binomial model (Clements and Silver, 2000), see Materials and methods). Like the unpriming model with cooperativity 5, variances decrease with increasing extracellular Ca2+ concentration, although the variances are slightly higher. Experimental data (example traces and means) depicted in panels A-E are replotted from Figure 2A–D,F. Parameter values used for simulations can be found in Tables 1–3. Simulation scripts can be found in Source code 1. Results from simulations (means and SDs) can be found in the accompanying source data file (Figure 7—source data 1).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (A) Diagram of the site activation mechanism. Three states are introduced: [I], inactive, [D], delay, and [A], activated. SV fusion is only allowed from sites in state [A]. The rate from [I] to [D] is increased by Ca2+, whereas the rate from [D] to [A] is slower and independent of Ca2+, thereby introducing a delay. All (in)activation reactions are assumed to be reversible. (B) Full site activation model. The Ca2+ (un)binding of the SVs follow the same equations as in the single-sensor model and occurs independently of the site (in)activation. Replenishment is allowed into empty release sites regardless of activation status. (C) Average, experimental eEJC traces (black) together with average simulated traces (red). (D) eEJC1 amplitudes of experiment (black) and simulation (red). Error bars and colored bands show standard deviation. Like with the three models described in the main text, simulations reproduce eEJC1 amplitudes well. (E) Average, normalized eEJC traces of experiment (black) and simulation (red). (F) PPR values of experiment (gray) and simulation (blue). Error bars and colored bands show standard deviation. Like the unpriming model, simulations reproduce the experimentally observed facilitation. (G) Average simulated traces (red) and examples of different outcomes of the stochastic simulation (colors). (H) Plot of the mean synaptic variance vs. the mean eEJC1 values, both from the experiment (black) and the simulation (red). The curves show the best fitted parabolas with forced intercept at (0,0) (simulation: Var = −0.0043*< eEJC1>2+0.5398 nA*< eEJC1>, corresponding to nsites = 233 and q = 0.54 nA when assuming a classical binomial model (Clements and Silver, 2000), see Materials and methods). Like in experiments, simulations lead to decreasing variance at the highest Ca2+ concentrations. (I) The number of sites in state [I] and [A] (gray and red resp.) in simulations with extracellular Ca2+ concentrations of 0.75 mM and 10 mM (solid and dashed resp.). The varying basal Ca2+ concentration yield different initial amounts of site activation. The activation of sites mainly occurs between APs because of the delay state. Experimental data (example traces and means) depicted in panels C-F,H are replotted from Figure 2A–D, F. Parameter values used for simulations can be found in Tables 1–3. Simulation scripts can be found in Source code 1. Results from simulations (means and SDs) can be found in the accompanying source data file (Figure 7—source data 1).

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** (A) Estimated PPRs for 0.75, 1.5, 3, 6 and 10 mM extracellular Ca2+ (from top to bottom) as a function of interstimulus interval (5, 10, 25, 50, 100, 250, 500 and 1000 ms). STF can be detected at low (0.75 mM) and physiological (1.5 mM) Ca2+ concentrations and decays after approximately 100 ms, no STF can be detected at high (3–10 mM) Ca2+ concentrations (starting with PPR values below 0.5 at 5 ms and increasing to PPR values around one for intervals above 25 ms). Regions of interest indicated by dashed red square are shown as a close-up in next panel. (B) Estimated paired-pulse ratio values (PPR) for Ca2+ concentrations (0.75–10 mM) 0.75, 1.5, 3, 6 and 10 mM extracellular Ca2+ (from top to bottom) as a function of their interstimulus interval (5, 10, 25, 50 ms). (C) Examples of average traces from paired-pulse simulations at different (0.75–10 mM) extracellular Ca2+ (from top to bottom) for 5 ms (blue), 10 ms (red), 25 ms (yellow) and 50 ms (purple) interstimulus intervals. Results from simulations (means and SDs) can be found in the accompanying source data file (Figure 7—source data 1).

In this model we assumed a Ca2+ cooperativity of n = 5 for the unpriming mechanism (we also explored n = 2, see Figure 7—figure supplement 1). The following parameters were optimized: Qmax, nsites and krep (like in the single- and dual fusion-sensor models), together with KM,prim, the Ca2+ affinity of the priming sensor, and u, its Ca2+ cooperativity. These values together define the Ca2+-dependent unpriming rate (see Table 2 for best fit parameters). The total number of fitted parameters (5) was the same as for the dual fusion-sensor models (Figure 6 and Figure 6—figure supplement 1). Figure 7D–I present the results. It is clear that both eEJC1 amplitudes and PPR values were described very well with this model at all extracellular Ca2+ concentrations. In addition, the variance-mean relationship of the eEJC1 was reproduced satisfactorily, except for a small variance overshoot for the highest extracellular Ca2+ concentrations (Figure 7I, see Discussion). Fitting of the unpriming model with a Ca2+ cooperativity of 2 also led to a good fit (Figure 7—figure supplement 1), although the variance overshoot was somewhat larger. We also explored the time-dependence of the facilitation by simulating PPR values for various inter-stimulus intervals at different extracellular Ca2+ concentrations which could be investigated experimentally in the future to further refine parameters (Figure 7—figure supplement 2).

Different facilitating synapses exhibit a large range of PPR values, some larger than observed at the Drosophila NMJ (Jackman et al., 2016). Therefore, if this were a general mechanism to produce facilitation, we would expect it to be flexible enough to increase the PPR much more than observed here. To investigate the model’s flexibility we systematically explored the parameter space by varying Qmax, KM,prim, and u (Figure 7J,K). Similar to Figure 6J,K, the colors of the balls represent the PPR value and the number of release sites needed to fit the eEJC1 amplitudes. Consistent with a very large dynamic range of this mechanism, PPR values ranged from 0.85 to 3.90 (Figure 7J,K) and unlike the dual fusion-sensor model, PPR values were fairly robust to changes in Ca2+ influx (note the different scales on Figure 7J,K and Figure 6J,K). Moreover, because this mechanism does not affect the Ca2+ sensitivity of SV fusion, facilitation was achieved without inducing asynchronous release (Figure 7D).

We also investigated an alternative model based on Ca2+-dependent release site activation. In this model, all sites are occupied by a vesicle, but some sites are inactive and fusion is only possible from activated sites. We assumed that site activation was Ca2+-dependent. In order to avoid site activation during AP1, which would again hinder STF and could contribute to asynchronous release, we implemented an intermediate delay state (Figure 7—figure supplement 3A–B) from which sites were activated in a Ca2+-independent reaction. This could mean that priming occurs in two-steps, with the first step being Ca2+-dependent. Similar to the unpriming model presented above, the modest increase of intracellular Ca2+ with extracellular Ca2+ yielded an RRP increase (/increase in active sites) (Figure 7—figure supplement 3I). This model agreed similarly well with the data as the unpriming model (Figure 7—figure supplement 3C–H). Thus, both mechanisms which modulate the RRP rather than pVr are fully capable of reproducing the experimentally observed Ca2+-dependent eEJC1 amplitudes, STF, release synchrony and variance. The unpriming model was preferred since it had fewer parameters and performed slightly better in optimisations than the site activation model.

### A release site facilitation mechanism utilizes a larger part of the SV distribution

Why do nsite/priming-based mechanisms (Figure 7, Figure 7—figure supplement 1, Figure 7—figure supplement 3) account for STF from the broad distribution of SV release site:Ca2+ channel coupling distances, while the pVr-based models (Figures 4 and 6, Figure 6—figure supplement 1) cannot? To gain insight into this, we analysed the spatial dependence of transmitter release in the unpriming model during the paired-pulse experiment (0.75 mM extracellular Ca2+) in greater detail (Figure 8). Panel 8A, similarly to Figure 5A, shows example stochastic simulations (at external Ca2+ concentration 0.75 mM, to illustrate facilitation). The best fit parameters of the unpriming model predicted a larger Ca2+ influx (1.64-fold and 3.05-fold larger Qmax value) than the single- and dual fusion-sensor models (Table 2). The larger Ca2+ influx compensated for the submaximal priming of SVs (reduced release site occupancy) prior to the first stimulus by expanding the region where SVs are fused (Figure 8B). Comparing to Figure 5B, a much larger part of the SV distribution is utilized during the first stimulus. Following AP1, vesicles prime into empty sites across the entire distribution, allowing AP2 to draw again from the entire distribution. During this time, the increased residual Ca2+ causes overfilling of the RRP, that is more release sites are now occupied, giving rise to more release during AP2. Notably, the AP2-induced release again draws from the entire distribution. Thus, the unpriming model not only reproduces STF and synaptic variance, but also utilizes docked SVs more efficiently from the entire distribution compared to the single- and dual fusion-sensor model.

![Figure 8.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig8-v2.jpg)

**Figure 8.:** (A) Two examples of docked SVs stochastically placed according to the distribution described in Figure 1D and their behavior in the PPR simulation at 0.75 mM extracellular Ca2+ concentration. For clarity, 10 SVs are shown per AZ and only a central part of the AZ is shown. Top row: Prior to AP1, only some release sites contain a primed SV (dark gray circles) and pVr1 is indicated as a number. Initially empty release sites are indicated by dashed black squares. The larger dashed, blue circle in the AZ center indicates pVr1 = 0.25. Second row: After AP1 some of the SVs have fused (dashed blue circles). Third row: Right before AP2 the initially empty sites as well as the sites with SV fusion in response to AP1 have been (re)populated (orange shading). pVr2 is indicated as a number. The larger dashed, red circle indicates pVr2 = 0.25. Bottom row: After AP2 the second release has taken place. Small, dashed circles indicate release from AP1 and AP2 (blue and red resp.). (B) The average simulation at the same time points as in (A). Histograms represent primed SVs (black and gray) as well as first and second release (blue and red) illustrating how release from AP1 and AP2 draw on a larger part of the SV distribution (compare to Figure 5) and how the increase in RRP size can induce facilitation. The blue and red curves indicate the vesicular release probability as a function of distance during AP1 (blue) and AP2 (red). Parameters used for simulations can be found in Tables 1–3.

## Discussion

We here described a broad distribution of SV release site:Ca2+ channel coupling distances in the Drosophila NMJ and compared physiological measurements with stochastic simulations of four different release models (single-sensor, dual fusion-sensor, Ca2+-dependent unpriming and site activation model). We showed that the two first models (single-sensor and dual fusion-sensor), where residual Ca2+ acts on the energy barrier for fusion and results in an increase in pVr, failed to reproduce facilitation. The two latter models involve a Ca2+-dependent regulation of participating release sites and reproduced release amplitudes, variances and PPRs. Therefore, the Ca2+-dependent accumulation of releasable SVs is a plausible mechanism for paired-pulse facilitation at the Drosophila NMJ, and possibly in central synapses as well. In more detail, our insights are as follows:

In our model, all primed vesicles have identical properties, and only deviate in their distance to the Ca2+ channel cluster (positional priming, Neher and Brose, 2018). Alternatively, several vesicle pools with different properties (molecular priming) could be considered, which might involve either vesicles with alternative priming machineries, or vesicles being in different transient states along the same (slow) priming pathway (Walter et al., 2013). In principle, if different primed SV states are distributed heterogenously such that more distant vesicles are more primed/releasable, such an arrangement might counteract the effects of a broad distance distribution, although this is speculative. Without such a peripheral distribution, the existence of vesicles in a highly primed/releasable state (such as the ‘super-primed’ vesicles reported at the Calyx of Held synapse), would result in pronounced STD, and counteract STF, which indeed has been observed (Lee et al., 2013; Taschenberger et al., 2016).

In this study electrophysiological recordings were performed on muscle 6 of the Drosophila larva which receives input from morphologically distinct NMJs containing big (Ib) and small (Is) synaptic boutons, which have been shown to differ in their physiological properties (Atwood et al., 1993; He et al., 2009; Newman et al., 2017). This could add another layer of functional heterogeneity in the postsynaptic responses analysed here (the EM and STED analyses shown here were focused on Ib inputs). Because our model does not distinguish between Is and Ib inputs, the estimated parameters represent a compound behaviour of all types of synaptic input to this muscle. Future investigations to isolate the contribution of the different input types (e.g. by genetically targeting Is/Ib-specific motoneurons using recently described GAL4 lines; Pérez-Moreno and O'Kane, 2019) could help distinguish between inputs and possibly further refine the model to identify parameter differences between these input types.

Figure 9 summarizes the results for the single-sensor, dual fusion-sensor and unpriming models. Facilitation in single and dual fusion-sensor models depend on the increase in release probability from the first AP to the next (compare colored rings representing 25% release probability between row 2 and 4). However, the increase is very small, even for the dual fusion-sensor model, and to nevertheless produce some facilitation, optimisation finds a small Ca2+ influx, which leads to an ineffective use of the broad vesicle distribution (and a too-high estimate of nsites). In the unpriming model a higher fitted Ca2+ influx (QMax) leads to a more effective use of the entire SV distribution, and facilitation results from the combination of incomplete occupancy of release sites before the first AP (row 1), combined with ‘overshooting’ priming into empty sites between APs (row 3).

![Figure 9.](https://cdn.elifesciences.org/articles/51032/elife-51032-fig9-v2.jpg)

**Figure 9.:** Top row: SVs primed (white ball) prior to AP1. In the single- and dual fusion-sensor models all release sites are occupied. In the unpriming model priming is in an equilibrium with unpriming and some release sites are empty. The dashed white graphs show the peak Ca2+ concentration (simulation of optimal fits for each model) during the first transient as a function of distance to the Ca2+ source. Second row: Some of the SVs fuse in response to AP1. The dashed blue graphs show the pVr1 as a function of distance. The large blue circles indicate pVr1 = 0.25. In the unpriming model the larger Ca2+ influx (according to the optimal fit) increases the area from which SVs fuse. Third row: Right before AP2 some of the empty release sites have been repopulated or newly filled by priming (orange balls). The shift in the (un)priming equilibrium in the unpriming model makes the increase in the number of primed SVs substantially larger than in the other models. The dashed white graphs show the peak Ca2+ concentration during the second transient as a function of distance to the Ca2+ source. Bottom row: SV fusion in response to AP2. The large dashed red graphs show pVr2 as a function of distance to the Ca2+ source. The blue and red circles indicate pVr1 and pVr2 of 0.25. In the dual fusion-sensor model, the second sensor increases pVr between stimuli, but the effect is small, even in the best fit of the model. These cartoons illustrate the mechanisms underlying our fitting results of the different models: The dual fusion-sensor model shows a small increase in second release compared to the single-sensor model, but only the unpriming model reproduces the experimentally observed facilitation. Parameters used for simulations can be found in Tables 1–3.

Molecularly, syt-7 was linked to STF behaviour (Jackman et al., 2016), and our data does not rule out that syt-7 is essential for STF at the Drosophila NMJ. However, we show clearly that a pVr-based facilitation mechanism (dual fusion-sensor model) cannot account for STF in synapses with heterogeneous distances between release sites and Ca2+ channels. Interestingly, syt-7 was also reported to function in vesicle priming and RRP replenishment (Liu et al., 2014; Schonn et al., 2008). Thus, future work will be necessary to investigate whether the function of syt-7 in STF might take place by Ca2+-dependent inhibition of vesicle unpriming or release site activation.

Similar suggestions that facilitation results from a build-up of primed SVs during stimulus trains were made for the crayfish NMJ and mammalian synapses (Gustafsson et al., 2019; Pan and Zucker, 2009; Pulido and Marty, 2018). This is in line with our results, with facilitation arising from modulation of the number of primed SVs rather than pVr. Our models are conceptually simple (e.g. all SVs are equally primed and distinguished only by distance to Ca2+ channels, sometimes referred to as ‘positional priming’ Neher and Sakaba, 2008), and we improved conceptually on previous work by using estimated SV release site:Ca2+ channel distributions, stochastic simulations and comparison to variance-mean relationships and we performed a systematic comparison of pVr- and priming-based models. It has not been clear whether increases in primed SVs are also required for paired-pulse facilitation, or only become relevant in the case of ‘tonic’ synapses that build up release during longer stimulus trains (frequency facilitation Neher and Brose, 2018). Paired-pulse facilitation is a more wide-spread phenomenon in synapses than frequency facilitation, and we show here for the case of Drosophila NMJ that it also seems to require priming-based mechanisms. Thus, Ca2+-dependent increases of the RRP during STP might be a general feature of chemical synapses.

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
      <td>Strain (Drosophila melanogaster)</td>
      <td>w[1118]</td>
      <td>BloomingtonDrosophilaStock Center</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Ok6-GAL4/II</td>
      <td>(Aberle et al., 2002)</td>
      <td>PMID:11856529</td>
      <td>Ok6-Gal4/II crossed to w[1118]</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>elav-Gal4/I</td>
      <td>(Lin and Goodman, 1994)</td>
      <td>PMID:7917288</td>
      <td>Used for elav-GAL4/+;;UAS-Unc13A-GFP/+;P84200/P84200</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Unc13A-GFP/III</td>
      <td>(Böhme et al., 2016)</td>
      <td>PMID:27526206</td>
      <td>Used for elav-GAL4/+;;UAS-Unc13A-GFP/+;P84200/P84200</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ry506; P{ry11}unc-13P84200 / ciD</td>
      <td>Kyoto Stock Center</td>
      <td>FlyBase: FBst0300878</td>
      <td>Used for elav-GAL4/+;;UAS-Unc13A-GFP/+;P84200/P84200</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[1118]; P{w[+mC]=Mhc-SynapGCaMP6f}3–5</td>
      <td>(Newman et al., 2017) BloomingtonDrosophilaStock Center</td>
      <td>PMID:28285823 Bloomington Stock # 67739</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[1118]; P{y[+t7.7] w[+mC]=20XUAS-IVS-665GCaMP6m}attP40/Ok6-GAL4</td>
      <td>BloomingtonDrosophilaStock Center</td>
      <td>Bloomington Stock # 42748</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Unc13A (guinea pig polyclonal)</td>
      <td>(Böhme et al., 2016)</td>
      <td>PMID:27526206</td>
      <td>Dilution: 1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti guinea pig STAR635 (goat polyclonal)</td>
      <td>(Böhme et al., 2016)</td>
      <td>PMID:27526206</td>
      <td>Dilution: 1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti Nc82 (mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Antibody Registry ID: AB_2314866</td>
      <td>Dilution: 1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse Cy5 (goat polyclonal)</td>
      <td>Jackson ImmunoResearch</td>
      <td>SKU: 115-175-072</td>
      <td>Dilution: 1:500</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LAS X software</td>
      <td>Leica Microsystems</td>
      <td>https://www.leica-microsystems.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LCS AF</td>
      <td>Leica Microsystems</td>
      <td>Leica Microsystems</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Image J</td>
      <td>NIH</td>
      <td>Version 1.48q/1.50 g; https://imagej.nih.gov/ij/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Imspector Software</td>
      <td>Max Planck Innovation</td>
      <td>Version 0.10</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>R2010b/R2016b</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clampfit</td>
      <td>Molecular Devices</td>
      <td>Version 10.3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad Software</td>
      <td>Version 5.01/6.01</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pClamp 10</td>
      <td>Molecular Devices</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CalC</td>
      <td>(Matveev et al., 2002)</td>
      <td>PMID:12202362 Version 6.8.6</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Computer grid</td>
      <td>Bioinformatics Center, University of Copenhagen</td>
      <td>https://www1.bio.ku.dk/scarb/bioinformatics-centre/</td>
      <td>Used for simulations</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>custom-built STED-microscope</td>
      <td>(Göttfert et al., 2017)</td>
      <td>PMID:23823248</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>HPF machine (HPM100)</td>
      <td>Leica Microsystems</td>
      <td>https://www.leica-microsystems.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>AFS</td>
      <td>Leica Microsystems</td>
      <td>https://www.leica-microsystems.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ultramicrotome (RMC PowerTome XL; Reichert Ultracut S)</td>
      <td>Leica Microsystems</td>
      <td>https://www.leica-microsystems.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Electrone microscope (TecnaiSpirit; FEI or Zeiss 900)</td>
      <td>FEI; Zeiss</td>
      <td>https://www.fei.com,https://www.zeiss.com</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Fly husbandry, genotypes and handling

Flies were kept under standard laboratory conditions as described previously (Sigrist et al., 2003) and reared on semi-defined medium (Bloomington recipe) at 25°C, except for GCaMP6m and synapGCaMP6f flies which were kept at room temperature, and Ok6-GAL4/+ (Figure 2, Figure 2—figure supplement 1, Figure 4 panel B-E and G, Figure 6 panel D-G and I, Figure 6—figure supplement 1, Figure 7D–G and I, Figure 7—figure supplement 1, Figure 7—figure supplement 3C–F,H) which were kept at 29°C (for detailed genotypes see below). For experiments both male and female 3rd instar larvae were used. The following genotypes were used:

Figure 7 Ok6-GAL4/+ (Ok6-Gal4/II crossed to w[1118]; panel D-G, (I). Figure 7—figure supplement 1: Ok6-GAL4/+ (Ok6-Gal4/II crossed to w[1118]). Figure 7—figure supplement 3: Ok6-GAL4/+ (Ok6-Gal4/II crossed to w[1118]; panel C-F, (H).

The following stocks were used: Ok6-GAL4/II (Aberle et al., 2002), UAS-Unc13A-GFP/III (Böhme et al., 2016), elav-Gal4/I (Lin and Goodman, 1994). The following stock were obtained from the Bloomington Drosophila Stock Center: P{w[+mC]=Mhc-SynapGCaMP6f}3–5/III (Newman et al., 2017) and w[1118]; P{y[+t7.7] w[+mC]=20XUAS-IVS-GCaMP6m}attP40. The following stock was obtained from Kyoto Stock Center: P84200/IV.

### EM data acquisition and analysis

Sample preparation, EM image acquisition and the quantification of docked SV distances to the AZ center (center of the electron dense ‘T-bar’) are described in Böhme et al. (2016); Reddy-Alla et al. (2017). The Rayleigh distributions were fit to the distances of docked SVs to the T-bar pedestal center, which had been collected in two EM datasets; analyses of these datasets were published in two previous studies, (Reddy-Alla et al., 2017) for the histogram of distances depicted in Figure 1A and (Böhme et al., 2016) for the histogram of distances depicted in Figure 1—figure supplement 1A.

### Derivation of the realistic docked SV distribution from EM measurements

The distances between Ca2+ channels and docked SVs in Drosophila NMJ obtained by EM was found to follow a Rayleigh distribution with best fit scale parameter σ = 76.51 nm (EM dataset 1) and σ = 74.07 nm (EM dataset 2). The fitting was performed with a MATLAB (MathWorks, version R2018b) function, raylfit, which uses maximum likelihood estimation. As these distances are found by EM of a cross-section of the active zone, we integrate this distribution around a circle to obtain the two-dimensional distribution of SVs in the circular space around the active zone.

The Rayleigh distribution has the following probability density function (pdf):

$$
f(x)= \frac{x}{\sigma^{2}}e^{−x^{2}/2\sigma^{2}}, x>0
$$

The pdf of the SV distribution will then be a scaling of the following function

$$
g^(x)=2\pixf(x)=2\pix\frac{x}{\sigma^{2}}e^{−x^{2}/2\sigma^{2}}
$$

In order to find the pdf of the 2D SV distribution, we integrate $g^$ to find the normalizing constant. By integration by parts we get

$$
\int_{0}^{∞}g^(x) dx=\int_{0}^{∞}2\pix\frac{1}{\sigma^{2}}xe^{−\frac{x^{2}}{2\sigma^{2}}} dx=2\pi([−xe^{−\frac{x^{2}}{2\sigma^{2}}}]_{0}^{∞}+\int_{0}^{∞}e^{−\frac{x^{2}}{2\sigma^{2}}} dx)=2\pi\int_{0}^{∞}e^{−\frac{x^{2}}{2\sigma^{2}}} dx=2\pi \frac{1}{2}\sigma\sqrt{2\pi}
$$

where the standard normal distribution was used in the last equality. Normalising (1) by this constant, we get the pdf of the distance distribution on a circular area in the active zone:

$$
gx=\frac{\sqrt{2}}{\sqrt{\pi}⋅\sigma^{3}}⋅x^{2}⋅e^{-x^{2}/2\sigma^{2}}
$$

### The SV distribution in simulations

In order to use the above SV distribution in simulations, we need to determine probabilities. g(x) is a generalized gamma distribution with $a=\sqrt{2}⋅\sigma$, $p=2$, $d=3$. The generalized gamma distribution with a>0, p>0, d>0 has the following pdf:

$$
hx;a,d,p=\frac{p}{a^{d}}⋅\frac{x^{d-1}⋅e^{-\frac{x}{a}^{p}}}{Γd/p}
$$

and cumulative density function (cdf):

$$
Hx;a,d,p=\frac{\gammad/p,x/a^{p}}{Γd/p}
$$

where $\gamma$ is the lower incomplete gamma function, and $Γ$ is the (regular) gamma function. Both of these functions are implemented in MATLAB (MathWorks, version R2018b), which easily allows us to draw numbers from them.

Thus, the SV distribution has the following cdf:

$$
 G(x)=\frac{\gamma(1.5, (x^{2}/2\sigma^{2})) }{Γ(1.5)}
$$

That is, given a uniformly distributed variable $q\in(0,1)$, we can use inbuilt MATLAB functions to sample SV distances, d:

$$
d=G^{−1}(q)=\sqrt{\gamma^{−1}(1.5,q⋅Γ(1.5))⋅2\sigma^{2}}
$$

The implementation is as follows:

Note that in MATLAB the inverse incomplete gamma function with parameter s is scaled by $Γ(s)$, which is why we input $q$ and not $q/Γ(1.5)$.

### STED data acquisition and analysis

Sample preparation, Unc13A antibody staining, STED image acquisition and the isolation of single AZ images are described in Böhme et al. (2019) and in the following. Third-instar w[1118] larvae were put on a dissection plate with both ends fixed by fine pins. Larvae were then covered by 50 µl of ice-cold hemolymph-like saline solution (HL3, pH adjusted to 7.2 [Stewart et al., 1994]: 70 mM NaCl, 5 mM KCl, 20 mM MgCl2, 10 mM NaHCO3, 5 mM Trehalose, 115 mM D-Saccharose, 5 mM HEPES). Using dissection scissors a small cut at the dorsal, posterior midline of the larva was made from where on the larvae was cut completely open along the dorsal midline until its anterior end. Subsequently, the epidermis was pinned down and slightly stretched and the internal organs and tissues removed. For the ‘STED dataset 2’ shown in Figure 1—figure supplement 1C,D, animals were then incubated in a HL3 solution containing 0.5% DMSO for 10 min (this served as a mock control for another experiment not shown in this paper using a pharmacological agent diluted in DMSO). The dissected samples were washed 3x with ice-cold HL3 and then fixed for 5 min with ice-cold methanol. After fixation, samples were briefly rinsed with HL3 and then blocked for 1 hr in 5% native goat serum (NGS; Sigma-Aldrich, MO, USA, S2007) diluted in phosphate buffered saline (Carl Roth Germany) with 0.05% Triton-X100 (PBT). Subsequently dissected samples were incubated with primary antibodies (guinea-pig Unc13A 1:500; Böhme et al., 2016) diluted in 5% NGS in PBT overnight. Afterwards samples were washed 5x for 30 min with PBT and then incubated for 4 hr with fluorescence-labeled secondary antibodies (goat anti-guinea pig STAR635 (1:100) diluted in 5% NGS in PBT. For secondary antibody production STAR635 fluorophore (Abberior, Germany) was coupled to respective IgGs (Dianova, Germany). Samples were then washed overnight in PBT and subsequently mounted in Mowiol (Max-Planck Institute for Biophysical Chemistry, Group of Stefan Hell) on high-precision glass coverslips (Roth, Germany, LH24.1). Two-color STED images were recorded on a custom-built STED-microscope (Göttfert et al., 2017), which combined two pairs of excitation laser beams of 595 nm and 635 nm with one STED fiber laser beam at 775 nm. All STED images were acquired using Imspector Software (Max Planck Innovation GmbH, Germany). STED images were processed using a linear deconvolution function integrated into Imspector Software (Max Planck Innovation GmbH, Germany). Regularization parameter was 1e−11. The point spread function (PSF for deconvolution was generated using a 2D Lorentz function with its half-width and half-length fitted to the half-width and half-length of each individual image. Single AZ images of ‘STED dataset 1’ (Figure 1E,F, Figure 1—figure supplement 1C,D) had previously been used for a different type of analysis defining AZ Unc13A cluster numbers; Wild-type in supplementary Figure 2a of Böhme et al. (2019). In this study here, we wanted to obtain the average Unc13A distribution from all AZs (no distinction of AZ types). To get an average image of the Unc13A AZ distribution, we used a set of hundreds of 51 × 51 pixel images with a pixel size of 10 × 10 nm. We identified Unc13A clusters in each image using the fluorescence peak detection procedure described in Böhme et al. (2019) using MATLAB (version 2016b). Peak detection was performed as follows: In each deconvolved 51 × 51 pixel image of an Unc13A-stained AZ, a threshold of 25 gray values was applied below which no pixels were considered. Then, local maxima values were found by finding slope changes corresponding to peaks along pixel columns using the function diff. The same was done along rows for all column positions where peaks were found. The function intersect was then used to determine all pixel positions common in both columns and rows. A minimum distance of 50 nm between neighboring peaks was used to exclude the repeated detection of the same peak, and an edge of 10 nm around the image was excluded to prevent the detection of neighboring AZs. The center of mass of all peak x,y-coordinates found in a single image was then calculated as follows:

$$
P_{x}=n^{-1}*\sum1nx_{obs}n
$$



$$
P_{y}=n^{-1}*\sum1ny_{obs}(n)
$$

Here, n is the number of detected peaks, (Px, Py) represents the center of mass (x,y)-coordinate, and xobs(n) and yobs(n) are the coordinates of the n-th detected peak. The image was then shifted such that this position (Px,Py) would fall into the center pixel of the 51 × 51 AZ image. For this, we calculated the required shift (dx and dy):

$$
d_{x}=\frac{imgsizex}{2}-P_{x}
$$



$$
d_{y}=\frac{imgsizey}{2}-P_{y}
$$

Here, imgsize(x,y) refers to the pixel dimensions of the image in both x and y dimensions. The required shift dx,y was then applied to the image using imtranslate, which directly takes these shift values as an input. All shifted images were then averaged into a single compound average image of all AZs by taking the average of each individual pixel and linearly scaling the result in a range between 0 and 255. This resulted in a circular cloudy structure depicted in Figure 1E, Figure 1—figure supplement 1C. To obtain the distribution of fluorescence as a function of distance to the AZ center in the average picture, we determined the distance between the center of the image and the center of the pixel together with the fluorescence intensity in each pixel. The fluorescence intensity in each pixel was obtained by using the inbuilt MATLAB function ‘imread’, which outputs the intensities in a matrix with indexes corresponding to the pixel location in the picture. From the indexes (xp,yp) of each pixel (of size 10 nm), the distance (in nm) to the center was calculated by the following formula:

$$
d(p)=(\sqrt{(x_{p}−26)^{2}+(y_{p}−26)^{2}})⋅10 nm
$$

We subtracted 26 from the pixel number, since the center pixel is the 26th pixel in x- and y-direction.These distances together with the intensity at each pixel provided the data for the histograms in Figure 1F and Figure 1—figure supplement 1D. The intensity values were normalized to the total amount of intensity making the y-axis of the histogram show percentage of the total amount of intensity.

### Calculation of mean distance to four nearest neighbors (1–4-NND)

Stage L3 larvae (n = 17; genotype: w[1118]; P{w[+mC]=Mhc-SynapGCaMP6f}3–5, Bloomington #67739) were fixed in ice-cold Methanol for 7 min and IHC-stained for BRP (mouse anti-Nc82, 1:1000; secondary AB: goat anti-mouse Cy5 1:500). Confocal images of the preparations were taken and processed as described in Reddy-Alla et al. (2017) for a different set of experiments not shown in this paper. Subsequently, the BRP channel was used to identify local fluorescence intensity maxima using the ImageJ-function ‘Find Maxima’ with a threshold setting between 10 and 20. The locations of maxima for each cell were then loaded into MATLAB (version 2016b) and the distances of each x,y-coordinate to all others were determined using the MATLAB function pdist2, resulting in a square matrix containing all possible inter-AZ distances. Each column of this matrix was then sorted in ascending order, and (as the distance of one AZ to itself is always 0) the mean of the 2nd to 5th smallest values across all AZs was determined and depicted as 1-NND through 4-NND in Figure 3A. The mean distance of the four nearest neighbouring AZs (1–4-NND) was calculated in each AZ (gray circles in Figure 3A bottom right) and the mean across AZs was used for quantification of the simulation volume (see below).

### Electrophysiological data acquisition and analysis

For both eEJC and mEJC (spontaneous release events,”miniature Excitatory Junctional Currents’) recordings, two electrode voltage clamp (TEVC) recordings were performed from muscle 6 NMJs of abdominal segments A2 and A3 as reported previously (Qin et al., 2005). Prior to recordings, the larvae were dissected in haemolymph-like solution without Ca2+ (HL3, pH adjusted to 7.2 Stewart et al., 1994: 70 mM NaCl, 5 mM KCl, 20 mM MgCl2, 10 mM NaHCO3, 5 mM Trehalose, 115 mM D-Saccharose, 5 mM HEPES) on Sylgard (184, Dow Corning, Midland, MI, USA) and transferred into the recording chamber containing 2 ml of HL3 with CaCl2 (concentrations used in individual experiments described below). TEVC recordings were conducted at 21°C using sharp electrodes (borosilicate glass with filament, 0.86×1.5×80 nm, Science Products, Hofheim, Germany) with pipette resistances between 20–30 MΩ, which were pulled with a P-97 micropipette puller (Sutter Instrument, CA, USA) and filled with 3 mM KCl. Signals were low-pass filtered at 5 KHz and sampled at 20 KHz. Data was obtained using a Digidata 1440A digitizer (Molecular devices, Sunnyvale, CA, USA), Clampex software (v10.6) and an Axoclamp 900A amplifier (Axon instruments, Union City, CA, USA) using Axoclamp software. Only cells with a resting membrane potential Vm below −50 mV, membrane resistances Rm above 4 MΩ and an absolute leak currents of less than 10 nA were included in the dataset.

#### eEJC recordings

eEJC recordings were conducted at a membrane holding potential of −70 mV in TEVC mode. APs were evoked by giving 300 µs short depolarizing pulses (8 V) to respective innervating motoneuron axons using a suction electrode (pulled with DMZ-Universal Puller (Zeitz-Instruments GmbH, Germany) polished with the CPM-2 microforge (ALA Scientific, NY, USA)) and a stimulator (S48, Grass Technologies, USA).

For experiments shown in Figure 2, individual cells were recorded at an initial extracellular CaCl2 concentration of 0.75 mM which was subsequently increased to 1.5 mM, 3 mM, 6 mM and 10 mM by exchanging and carefully mixing 1 ml of the bath solution with 1 ml HL3 of a higher CaCl2 concentration (total concentrations of exchange solutions: 2.25 mM, 4.5 mM, 9 mM, 14 mM), ultimately adding up to the desired CaCl2 concentration in the bath. At each titration step, cells were acclimated in the bath solution for 60 s and 10 repetitions of paired stimulating pulses (0.1 Hz, 10 ms interstimulus interval) were given. eEJC data shown in Figure 2—figure supplement 3 was obtained by recording Ok6-Gal /+ and +/+ NMJs at 0.75 mM (Figure 2—figure supplement 3A-D ) and 1.5 mM (Figure 2—figure supplement 3E-H ) Ca2+. A single test AP was given (followed by a 20 s intermission) and cells were stimulated once by two consecutive APs (10 ms inter-stimulus interval). In Figure 2—figure supplement 3B, D, E, and G, eEJC1 and PPR averages are shown ± the estimated single-cell SD .

eEJC data was analyzed with our own custom-built MATLAB script (provided with the source data file, Figure 2—source data 1). After stimulation artifact removal, the eEJC1 amplitude was determined as the minimum current value within 10 ms from the time of stimulation. To account for the decay only being partial before the second stimulus, we fitted a single exponential function to the eEJC decay from the time point of 90% of the amplitude to the time point of the second stimulus. The eEJC2 amplitude was determined as the difference between the minimum after the second stimulus and the value of the fitted exponential at the time point of the second minimum (see insert in Figure 2C and Figure 2—figure supplement 1A). For analysis shown in Figure 2, the first stimulation per Ca2+ concentration was excluded, as we noticed that the first trial often gave first eEJC responses that were higher than in the following trials. This may reflect the presence of a slow reaction by which SVs can be primed with an even higher release probability (possibly due to the ‘super-priming’ described at the murine Calyx of Held synapse Lee et al., 2013). However, as the var/mean analysis requires the existence of an equilibrium in-between stimuli which appears to have been reached between all of the succeeding stimuli, we decided to use only those for our analysis. For eEJC1 amplitudes the average over all measurements and all cells (6 cells, nine measurements each) was calculated (Figure 2B). The PPR was calculated by dividing the second amplitude by the first throughout trials and averaging over all measurements and all cells (Figure 2D). In each cell, the variance of eEJC1 and PPR was estimated (nine stimulations per Ca2+ concentration) and the average variance (averaged across cells) was calculated at each extracellular Ca2+ concentration. The error bars in Figure 2B,D are the SD (across all animals) at each extracellular Ca2+ concentration. In Figure 2F the eEJC1 averages and variances are ± SEM. A parabola with intersect y = 0 was fitted using the function polyfitZero (version 1.3.0.0 from MathWorks file exchange) in MATLAB. (Var = q*I-I2/N, q being the quantal size, I the mean eEJC1 amplitude and N number of release sites) (Clements and Silver, 2000).

#### mEJC recordings

mEJC data was obtained from a separate set of experiments where mEJCs were recorded for 60 s in TEVC mode at 1.5 mM extracellular Ca2+ and a holding potential of −80 mV for easier identification of miniature events. Because different holding potentials were used (−80 mV here compared to −70 mV for the data shown in Figure 2) it must be pointed out that these recordings were only used to determine the shape of the response for later convolution with SV fusion events predicted by the model (the mEJC amplitude was adjusted based on the variance-mean data collected at -70 mV, see below). For this, the average mEJC traces from five different cells were aligned to 50% of the rise and averaged. We then fitted the following formula to the data:

$$
I_{mini}t=A⋅1-e^{-\frac{t-t_{0}}{\tau_{r}}}⋅B⋅e^{-\frac{t-t_{0}}{\tau_{df}}}+1-B⋅e^{-\frac{t-t_{0}}{\tau_{ds}}}
$$

$t_{0}$ is the onset, $A$ is the full amplitude (if there was no decay), $B$ is the fraction of the fast decay, and $\tau_{r},\tau_{df},\tau_{ds}$ are the time constants of the rise, fast decay, and slow decay respectively.

The best fit was

$$
t_{0}≈3.0 ms, A≈7.21 \muA,B≈2.7e−9,\tau_{r}≈10.6928 s, \tau_{df}≈1.5 ms, \tau_{ds}≈2.8 ms
$$

and is plotted together with the average experimental mini trace in Figure 2—figure supplement 1B. Note that $t_{0}$ is a time delay when this mEJC is implemented in the simulation and is therefore arbitrary. B is very small making the decay close to a single exponential. The maximum of this function is ~0.7 nA. However, as mentioned above, this function was rescaled to a value of 0.6 nA to match the mEJC amplitudes of the experiments conducted with a holding potential of -70 mV, that is the size of a single quantal event, q=0.6 nA, estimated from the variance-mean analysis (see Figure 2F).

### Presynaptic GCaMP recordings and analysis

Because the presynaptic terminals of the Drosophila larval NMJ are not readily accessible to electrical recordings of Ca2+ currents, the saturation behaviour of Ca2+ influx as a function of extracellular Ca2+ concentrations was measured. We did so by engaging the fluorescent Ca2+ indicator GCaMP6m (Genotype: w[1118]; P{y[+t7.7] w[+mC]=20XUAS-IVS-GCaMP6m}attP40, Flybase ID: FBti0151346), which we expressed presynaptically using OK6-Gal4 as a motoneuron-specific driver. Third instar larvae heterozygously expressing the indicator were used in experiments as follows. Dissection took place in Ca2+-free, standard hemolymph-like solution HL-3 (in mM: NaCl 70, KCl 5, MgCl2 20, NaHCO3 10, Trehalose 5, Sucrose 115, HEPES 5, pH adjusted to 7.2) (Stewart et al., 1994). After dissection on a Sylgard-184 (Dow-Corning) block, larvae were transferred to the recording chamber containing HL-3 at varying CaCl2 concentrations (see below). The efferent motoneuron axons were sucked into a polished glass electrode containing a chlorided silver-wire, which could be controlled via a mechanical micromanipulator (Narishige NMN25) and was connected to a pipette holder (PPH-1P-BNC, NPI electronics) via a patch electrode holder (NPI electronics), and connected to an S48 stimulator (Grass Technologies). Larvae were then recorded using a white-light source (Sutter DG-4, Sutter Instruments) and a GFP filter set with a Hamamatsu OrcaFlash 4.0v2 sCMOS (Hahamatsu Photonics) with a framerate of 20 Hz (50 ms exposure) controlled by µManager software (version 1.4.20, https://micro-manager.org) on an upright microscope (Olympus BX51WI) with a 60x water-immersion objective (Olympus LUMFL 60 × 1.10 w). Muscle 4 1b NMJs in abdominal segments 2 to 4 were used for imaging. Imaging was conducted over 10 s, and at 5 s, 20 stimuli were applied to the nerve at 20 Hz in 300µs 7V depolarization steps. This procedure was begun in the lowest Ca2+ concentration (0.75 mM) and then repeated in the same larva at increasing Ca2+ concentrations (in mM 1.5, 3, 6) by exchanging the extracellular solution. To achieve a situation with no Ca2+ influx, a final recording was conducted where the bath contained HL-3 without CaCl2 and instead 8.3 mM EGTA (this solution was made by diluting 2.5 ml of a 50 mM stock solution in H2O in 12.5 ml of HL3, resulting in a pH of 8.0). Because this results in a slight dilution (16%) of the components in the HL3, the same dilution was performed for the above described Ca2+-containing solutions by adding 2.5 ml H2O to 12.5 ml of HL3 before CaCl2 was added at above mentioned concentrations.

Analysis of 5 Drosophila 3rd instar Larvae was done after automated stabilization of x,y-movement in the recordings (8-bit multipage .TIF-stacks, converted from 16 bit) as described previously (Reddy-Alla et al., 2017), manually selecting a ROI around the basal fluorescent GCaMP signal, and reading out the integrated density (the sum of all pixel grey values) of the whole region over time. Background fluorescence was measured in a region of the same size and shape outside of the NMJ and subtracted (frame-wise) from the signal, separately for each single recording. The quantification was then performed individually for each Ca2+ concentration, by subtracting the fluorescence 250 ms before the stimulation (Ft=4.75s) from the maximum fluorescence of the trace (Fmax), yielding the change in fluorescence dF:

$$
dFCa^{2+}=F_{max}-F_{t=4,75s}
$$

This was repeated for each cell and a Hill fit was performed on the individual values using Prism (version 6.07, GraphPad Software Inc):

$$
FCa^{2+}_{ext}=\frac{F_{end}*Ca^{2+}_{ext}^{m}}{K_{M,fluo}^{m}+Ca^{2+}_{ext}^{m}}+C
$$

In the above equation, Fend is the asymptotic plateau of the fluorescence increase. Furthermore, [Ca2+]ext is the extracellular Ca2+ concentration. KM,fluo (best fit value: 2.679 mM) is the concentration of extracellular Ca2+ at which fluorescence was half of Fend. The exponent m indicates a cooperative effect of the extracellular Ca2+ concentration on the fluorescence increase, which was constrained to a value of 2.43 (unitless) based on the described Ca2+ cooperativity of GCaMP6m (Barnett et al., 2017). However, constraining this value only had a modest effect on the estimate of KM,fluo as leaving it as a free parameter yielded similar values for KM,fluo (3.054 mM) and m (1.887). The constant C added at the end of Equation 3 allowed the baseline fluorescence to be different from zero. Results and best fit are summarized in (Figure 3—figure supplement 1).

### Proof that stochastic simulation of release is needed for PPR estimation

We here prove that stochastic simulations of neurotransmitter release provide a different average PPR value than the PPR value estimated in deterministic simulations. In the following, the stochastic variables A1 and A2 represent the amplitudes of the first and second release, respectively, capital ‘E’ denotes the mean of a stochastic variable (e.g. EA1), and a1 and a2 represent the amplitudes of the first and second release in the deterministic simulations. In all cases of parameter sets that we tried, the average amplitudes from the stochastic simulations with 1000 repetitions differed < 0.5 nA from the deterministically determined amplitudes. Thus, we can assume that EA1 = a1 and likewise for the second release.

In deterministic simulations, the estimate of the PPR is

$$
PPR-=\frac{a_{2}}{a_{1}}=\frac{EA_{2}}{EA_{1}}
$$

On the other hand, stochastic simulations yield a sample of different PPR values, since repetitions of the simulation routine yield release varying from trial to trial. In that case, the estimated PPR is

$$
PPR∼=E(\frac{A_{2}}{A_{1}})
$$

This resembles the way the PPR is estimated in experiments.

Using Jensen’s Inequality and the fact that the function f(x)=1/x is strictly convex, we get

$$
\frac{1}{EA_{1}}<E(\frac{1}{A_{1}})=E(A_{1}^{−1})
$$

Applying this to (4) we get

$$
PPR∼=E(\frac{A_{2}}{A_{1}})= E(A_{1}^{−1}A_{2})= Cov(A_{1}^{−1},A_{2})+E(A_{1}^{−1})E(A_{2})>Cov(A_{1}^{−1},A_{2})+ \frac{EA_{2}}{EA_{1}}=Cov(A_{1}^{−1},A_{2})+ PPR−
$$

Thus, the average stochastically simulated PPR do not necessarily converge to the deterministic estimate with increasing repetitions (note that in general it is true that the mean of a non-linear function of two random variables is not equal to the non-linear function evaluated in the means). An example is shown in Figure 4—figure supplement 1, where the single-sensor model was simulated with varying amounts of Ca2+ influx (by varying Qmax). The most left blue point, for example, is significantly higher than the deterministic estimate (p=4e-16, one-sample t-test). This motivates the use of stochastic simulations for correct estimation of the PPR.

### Simulation flow

All MATLAB procedures for simulation of the models can be found in Source code 1.

All simulations (deterministic and stochastic, see below) consisted of the same four basic steps, which we describe in detail here.

For each new set of parameters, steps 1–4 were repeated. For stochastic simulations, steps 2–4 were repeated 1000 times except for the parameter exploration in Figures 6J–K and 7J–K, where we ran 200 repetitions per parameter set. The many repetitions allowed a good estimate of both mean and variance of the models. In all cases, the mean amplitudes from the stochastic simulations with 1000 repetitions differed < 0.5 nA from the deterministically determined amplitudes.

### Ca2+ simulation

Simulation of Ca2+ signals in the presynapse was performed with the program CalC version 6.8.6 developed and maintained by Victor Matveev (Matveev et al., 2002). After this work was initiated, a bug affecting simulations of multiple Ca2+ channels in the same topology was found and a new version of CalC was released. This update had no effect on the simulations used in this study.

Intracellular Ca2+ concentrations were simulated in space and time in a cylinder-shaped volume. The cylinder allowed us to assume spatial symmetry which reduced simulation time significantly. Borders of the simulation volume were assumed to be reflective to mimic diffusion of Ca2+ from adjacent AZs (Meinrenken et al., 2002) and a volume-distributed uptake mechanism was assumed.

From measurements of the distance between an AZ and its four nearest neighbors (Figure 3A) we estimated the distance between centers of active zones to be 1.106 µm, leading to the assumption that the AZ spans a square on the membrane with area of 1.223 µm2. In order for the cylindrical simulation volume to cover an area of the same size, the radius was set to 0.624 µm. The height of the simulation volume was set to 1 µm making the simulation volume 1.223 µm3. Increasing the height further had no effect on the Ca2+ transients.

The total amount of charge flowing into the cell was assumed to relate to extracellular Ca2+ in a Michaelis-Menten-like way (as previously described by Schneggenburger et al., 1999; Trommershäuser et al., 2003) such that

$$
Q= \frac{Q_{max}⋅[Ca]_{ext}}{K_{M,current}+[Ca]_{ext}}
$$

KM,current was set to the value of 2.679 mM as determined for KM,fluo in the GCaMP6m experiments (see above). Qmax was fitted during the optimizations of the models.

We simulated a 10 ms paired pulse stimulus initiated after 0.5 ms of simulation. The Ca2+ currents for the two stimuli were simulated for 3 ms each and assumed to be Gaussian with FWHM = 360 µs and peak 1.5 ms after initiation. That is:

$$
I_{Ca}= {Q⋅\frac{1}{\sigma⋅\sqrt{2\pi}}e^{−\frac{(t−2)^{2}}{2\sigma^{2}}}, for t\in[0.5, 3.5]Q⋅\frac{1}{\sigma⋅\sqrt{2\pi}}e^{−\frac{(t−12)^{2}}{2\sigma^{2}}}, for t\in[10.5, 13.5]0, else
$$

with $\sigma= \frac{0.360}{2\sqrt{2⋅ln(2)}}= 0.153.$

The CalC simulation output were data files that contained the spatio-temporal intracellular Ca2+ profile at the height of 10 nm from the plasma membrane. In exocytosis simulations, these concentrations were interpolated at the SV distances in the x,y-plane and at time points with MATLAB’s built-in interpolate functions when computing the reaction rates of the system at a given time point.

The resting Ca2+ concentration was assumed to relate to the extracellular Ca2+ concentration in a similar way as during stimulation, such that

$$
[Ca^{2+}]_{basal}=[Ca^{2+}]_{max}⋅\frac{[Ca^{2+}]_{ext}}{K_{M,current}+[Ca^{2+}]_{ext}}
$$

with $Ca^{2+}_{max}=190nM$

For designation and value of Ca2+ parameters, see Table 1.

### SV distribution drawing

In all simulations we had to determine where to place release site. This was done by using the cdf of the SV distance distribution derived above (Equation 2).

For deterministic simulations, which were used in the fitting routine of the models (see below), the unit interval was divided into 180 bins of the form

$$
\frac{k-1}{180},\frac{k}{180},k=1,2…180.
$$

The midpoints were the percentiles giving rise to distances at which we read the Ca2+ simulation. This approach provided an approximation of the SV distribution. In accordance with our assumption that the AZs work in parallel the 180 distances gave rise to 180 independent different systems of ODEs with 1/180 of the total amount of SVs in each system. The results were then added together as a good approximation of the mean of the stochastic simulations with random SV distance drawings.

In each run of the stochastic simulations, we drew n random numbers from the unit interval, n being the number of SVs, and computed the distances based on the formula derived above.

### Rate equations of the simulated models

The models are summarized in Figures 4A, 6A and 7A, and Figure 7—figure supplement 3A,B. In the following equations the single-sensor, dual fusion-sensor, and unpriming models are all described. The site activation model is a combination of the equations for the single-sensor model and the site activation equations described below. The red text denotes terms that are unique to the dual fusion-sensor model, blue text indicates unpriming, which is unique to the unpriming model. Parameters are described below. For designation and value of parameters, see Tables 2,3.

Rate equations of the single-sensor model, dual fusion-sensor model and unpriming model:

$$
\frac{d[R(0,0)]}{dt}=k_{rep}[P0]−(r⋅u+ 5[Ca^{2+}]k_{1}+2[Ca^{2+}]k_{2}+L^{+})[R(0,0)]+k_{−1}[R(1,0)]+ k_{−2}[R(0,1)]
$$



$$
\frac{d[R(1,0)]}{dt}=−(4[Ca^{2+}]k_{1}+k_{−1}+2[Ca^{2+}]k_{2}+L^{+}f)[R(1,0)]+5[Ca^{2+}]k_{1}[R(0,0)]+ 2b_{f}k_{−1}[R(2,0)]+ k_{−2}[R(1,1)]
$$



$$
\frac{d[R(2,0)]}{dt}=−(3[Ca^{2+}]k_{1}+2b_{f}k_{−1}+2[Ca^{2+}]k_{2}+L^{+}f^{2} )[R(2,0)]+4[Ca^{2+}]k_{1}[R(1,0)]+ 3b_{f}^{2}k_{−1}⋅[R(3,0)]+k_{−2}⋅[R(2,1)]
$$



$$
\frac{d[R(3,0)]}{dt}=−(2[Ca^{2+}]k_{1}+3b_{f}^{2} k_{−1}+2[Ca^{2+}]k_{2}+L^{+}f^{3} )[R(3,0)]+3[Ca^{2+}]k_{1}[R(2,0)]+ 4b_{f}^{3}k_{−1}⋅[R(4,0)]+k_{−2}⋅[R(3,1)]
$$



$$
\frac{dR[(4,0)]}{dt}=−([Ca^{2+}]k_{1}+4b_{f}^{3}k_{−1}+2[Ca^{2+}]k_{2}+L^{+}f^{4} )[R(4,0)]+2[Ca^{2+}]k_{1}[R(3,0)]+ 5b_{f}^{4}k_{−1}⋅[R(5,0)]+k_{−2}⋅[R(4,1)]
$$



$$
\frac{d[R(5,0)]}{dt}=−(2[Ca^{2+}]k_{2}+5b_{f}^{4}k_{−1}+L^{+}f^{5} )[R(5,0)]+[Ca^{2+}]k_{1}[R(4,0)]+k_{−2}⋅[R(4,1)]
$$



$$
\frac{d[R(0,1)]}{dt}=k_{rep}[P1]−(5[Ca^{2+}]k_{1}+[Ca^{2+}]k_{2}+k_{−2}+L^{+}s)[R(0,1)]+k_{−1}⋅[R(1,1)]+2[Ca^{2+}]k_{2}[R(0,0)]+2b_{s}k_{−2}⋅[R(0,2)]
$$



$$
\frac{d[R(1,1)]}{dt}=−(4[Ca^{2+}]k_{1}+k_{−1}+[Ca^{2+}]k_{2}+k_{−2}+L^{+}fs)[R(1,1)]+5[Ca^{2+}]k_{1}[R(0,1)]+2b_{f}k_{−1}⋅[R(2,0)]+ 2[Ca^{2+}]k_{2}[R(1,0)]+ 2b_{s}k_{−2}⋅[R(1,2)]
$$



$$
\frac{d[R(2,1)]}{dt}=−(3[Ca^{2+}]k_{1}+2b_{f}k_{−1}+[Ca^{2+}]k_{2}+k_{−2}+L^{+}f^{2}s )[R(2,1)]+4[Ca^{2+}]k_{1}[R(1,1)]+3⋅b_{f}^{2}⋅k_{−1}[R(3,1)]+ 2[Ca^{2+}]k_{2}[R(2,0)]+ 2b_{s}k_{−2}⋅[R(2,2)]
$$



$$
\frac{d[R(3,1)]}{dt}=−(2[Ca^{2+}]k_{1}+3b_{f}^{2} k_{−1}+[Ca^{2+}]k_{2}+k_{−2}+L^{+}f^{3}s )[R(3,1)]+3[Ca^{2+}]k_{1}[R(2,1)]+ 4b_{f}^{3}k_{−1}⋅[R(4,1)]+ 2[Ca^{2+}]k_{2}[R(3,0)]+ 2b_{s}k_{−2}⋅[R(3,2)]
$$



$$
\frac{d[R(4,1)]}{dt}=−([Ca^{2+}]k_{1}+4b_{f}^{3}k_{−1}+[Ca^{2+}]k_{2}+k_{−2}+L^{+}f^{4}s )[R(4,1)]+2[Ca^{2+}]k_{1}[R(3,1)]+5b_{f}^{3}k_{−1}⋅[R(5,1)]+ 2[Ca^{2+}]k_{2}[R(4,0)]+ 2b_{s}k_{−2}[R(4,2)]
$$



$$
\frac{d[R(5,1)]}{dt}=−(5b_{f}^{4}k_{−1}+[Ca^{2+}]k_{2}+k_{−2}+L^{+}f^{5}s )[R(5,1)]+[Ca^{2+}]k_{1}[R(4,1)]+ 2[Ca^{2+}]k_{2}[R(5,0)]+ 2b_{s}k_{−2}⋅[R(5,2)]
$$



$$
\frac{d[R(0,2)]}{dt}=k_{rep}[P2]−(5[Ca^{2+}]k_{1}+2b_{s}k_{−2}+L^{+}s^{2})[R(0,2)]+k_{−1}[R(1,2)]+[Ca^{2+}]k_{2}[R(0,1)]
$$



$$
\frac{d[R(1,2)]}{dt}=−(4[Ca^{2+}]k_{1}+k_{−1}+2b_{s}k_{−2}+L^{+}fs^{2})[R(1,2)]+5[Ca^{2+}]k_{1}[R(0,2)]+ 2b_{f}k_{−1}[R(2,2)]+ [Ca^{2+}]k_{2}[R(1,1)]
$$



$$
\frac{d[R(2,2)]}{dt}=−(3[Ca^{2+}]k_{1}+2b_{f}k_{−1}+2b_{s}k_{−2}+L^{+}f^{2}s^{2} )[R(2,0)]+4[Ca^{2+}]k_{1}[R(1,2)]+ 3b_{f}^{2}k_{−1}[R(3,0)]+ [Ca^{2+}]k_{2}[R(2,1)]
$$



$$
\frac{d[R(3,2)]}{dt}=−(2[Ca^{2+}]k_{1}+3b_{f}^{2} k_{−1}+2b_{s}k_{−2}+[Ca^{2+}]k_{2}+L^{+}f^{3}s^{2} )[R(3,2)]+3[Ca^{2+}]k_{1}[R(2,2)]+ 4b_{f}^{3}k_{−1}⋅[R(4,2)]+ [Ca^{2+}]k_{2}[R(3,1)]
$$



$$
\frac{d[R(4,2)]}{dt}=−([Ca^{2+}]k_{1}+4b_{f}^{3}k_{−1}+2b_{s}k_{−2}+[Ca^{2+}]k_{2}+L^{+}f^{4}s^{2} )[R(4,2)]+2[Ca^{2+}]k_{1}[R(3,2)]+ 5b_{f}^{3}k_{−1}⋅[R(5,2)]+ [Ca^{2+}]k_{2}[R(4,1)]
$$



$$
\frac{d[R(5,2)]}{dt}=−(5b_{f}^{4}k_{−1}+2b_{s}k_{−2}+L^{+}f^{5}s^{2} )[R(5,2)]+[Ca^{2+}]k_{1}[R(4,2)]+ [Ca^{2+}]k_{2}[R(5,1)]
$$



$$
\frac{d[F]}{dt}=L^{+}([R(0,0)]+f[R(1,0)]+f_{2}[R(2,0)]+f_{3}[R(3,0)]+f_{4}[R(4,0)]+f_{5}[R(5,0)]+[sR(0,1)]+fs[R(1,1)]+f^{2}s[R(2,1)]+f^{3}s[R(3,1)]+f^{4}s[R(4,1)]+f^{5}s[R(5,1)]+[s^{2}R(0,2)]+fs^{2}[R(1,1)]+f^{2}s^{2}[R(2,1)]+f^{3}s^{2}[R(3,1)]+f^{4}s^{2}[R(4,1)]+f^{5}s^{2}[R(5,1)])
$$



$$
\frac{d[P0]}{dt}=L^{+}([R(0,0)]+ f[R(1,0)]+f^{2}[R(2,0)]+f^{3}[R(3,0)]+f^{4}[R(4,0)]+f^{5}[R(5,0)])+k_{−2}[P1]−2k_{2}[Ca^{2+}][P0]−k_{rep}[R(0,0)]+r⋅u[R(0,0)]
$$



$$
\frac{d[P1]}{dt}=L^{+}([sR(0,1)]+fs[R(1,1)]+f^{2}s[R(2,1)]+f^{3}s[R(3,1)]+f^{4}s[R(4,1)]+f^{5}s[R(5,1)])−k_{−2}[P1]+2k_{2}[Ca^{2+}][P0]+2b_{s}k_{−2}⋅[P2]−k_{rep}[R(0,1)]
$$



$$
\frac{d[P2]}{dt}=L^{+}([R(0,0)]+f[R(1,0)]+f^{2}[R(2,0)]+f^{3}[R(3,0)]+f^{4}[R(4,0)]+f^{5}[R(5,0)]+[sR(0,1)]+ fs[R(1,1)]+f^{2}s[R(2,1)]+f^{3}s[R(3,1)]+f^{4}s[R(4,1)]+f^{5}s[R(5,1)]+[s^{2}R(0,2)]+ fs^{2}[R(1,1)]+f^{2}s^{2}[R(2,1)]+f^{3}s^{2}[R(3,1)]+f^{4}s^{2}[R(4,1)]+f^{5}s^{2}[R(5,1)])+2k_{2}[P1]−2b_{s}k_{−2}[Ca^{2+}][P2]−k_{rep}[R(0,2)]
$$



$$
r=1−\frac{[Ca^{2+}]^{n}}{[Ca^{2+}]^{n}+K_{M,unprim}^{n}}
$$

In the single-sensor and site activation models, k2 = k-2=u = 0, and s = 1. This excludes all reactions exclusive for the dual fusion-sensor and unpriming models. Similarly, u = 0 in the dual fusion-sensor model and k2 = k-2=0 and s = 1 in the unpriming model.

[R(n,m)] denotes the Ca2+ binding state of a SV with n Ca2+ ions bound to the first sensor and m Ca2+ ions bound to the second fusion sensor. Note that in the single-sensor, site activation and unpriming models, m is always zero (since there is no second fusion sensor), and the states are denoted with a single number in Figures 4A and 6A and Figure 7—figure supplement 3. [F] counts the cumulative number of fused SVs. [P0] is not shown in the figures, but are part of the equations denoting the number of empty sites. That is, in the single-sensor and unpriming models $r=1-\frac{Ca^{2+}^{n}}{Ca^{2+}^{n}+K_{M,unprim}^{n}}$ has a positive part equal to $\frac{dP0}{dt}$ and a negative part equal to the rate of replenishment. In the dual fusion-sensor model, there are three states of empty sites, [P0], [P1], [P2]. These corresponded to the different states of Ca2+ binding to the second fusion sensor of the empty sites since we assumed the second sensor to be located on the plasma membrane. Note that these equations describe the second sensor with cooperativity 2, which is described in Results. We also optimized cooperativities 3, 4, and 5. The equations can easily be extended to these cases, since the rate equations of the second fusion sensor are of the same form as for the first sensor. In the unpriming model (Figure 7A) we assumed unpriming to take place from state [R(0)] with a Ca2+-dependent rate.

For the individual reactions, we can express the rates of Ca2+ (un)binding, fusion, and replenishment of a single SV in a more general form. This is useful in the stochastic simulation method introduced later. In the following, we denote the general form of the rate for each possible reaction in the models described above.

The expressions in brackets denote the states involved in the reaction.

$$
[R(n,m)]→[R(n−1,m)]:nk_{−1}b^{n−1}[R(n,m)]→[R(n+1,m)]:(n_{max}−n)[Ca^{2+}]k_{1}[R(n,m)]→[R(n,m−1)]:mk_{−2}b^{m−1}[R(n,m)]→[R(n,m+1)]:(m_{max}−m)[Ca^{2+}]k_{2}[R(n,m)]→[F]: L^{+}s^{m}f^{n}[P0]→[R(0,0)]: k_{rep}
$$

with nmax and mmax denoting the cooperativity of the first and second fusion sensors, respectively. Equations in line 3 and 4 in (7) were only non-zero in the dual fusion-sensor model.

### Rate equation of the site activation model

In the site activation model (Figure 7—figure supplement 3), all reactions regarding Ca2+ (un)binding and replenishment was as in the one-sensor model. In addition we assumed a mechanism acting on the release sites independently of the Ca2+ binding of the SV. All sites regardless of the SV status were either activated (A state) or not (D or I states). This mechanism is proposed as a facilitation mechanism, which necessitates its primary effect to be on the second stimulus rather than the first. We were therefore forced to implement the D state, which is a temporary ‘delay’ state making sure the mechanism does not increase first release. The changing of [A] and [I] states at 0.75 and 10 mM extracellular Ca2+ are shown in (Figure 7—figure supplement 3I).

The site activation mechanism has the following rate equations:

$$
\frac{d[A]}{dt}=−\delta[A]+\gamma[D]\frac{d[D]}{dt}=−(\beta+\gamma)[D]+\alpha[Ca^{2+}]^{n}[I]+\delta[A]\frac{d[I]}{dt}=−\alpha[Ca^{2+}]^{n}[I]+\beta[D]
$$

where $\alpha, \beta, \delta, \gamma>0$ are rate parameters.

The deterministic implementation of the site activation model included 3 sets of ODEs, one for each state in the site activation model. Each set consisted of the equations of the one-sensor model as well as transitions between states of equal Ca2+ binding in the 3 sets of ODEs (e.g. from R(0,D) to R(0,A)) (Figure 7—figure supplement 3B).

In the stochastic simulations the site activation rates were included in the propensity vector like any other reaction. Whenever a site activation reaction occurred, a release site vector consisting of nsites elements was updated. For each site, the fusion rate was multiplied by 0, when the site state was I or D.

### Steady-state estimation

Prior to simulation, the Ca2+ binding states of all SVs were assumed to be in equilibrium. We can determine the steady state iteratively by setting

$$
\frac{d[I]}{dt}=-\alphaCa^{2+}^{n}I+\beta[D]
$$



$$
\alpha,\beta,\delta,\gamma>0
$$



$$
R0,0_{init}=1
$$

This can be reduced to the non-iterative expression:

$$
[R(n,m)]_{init}=\frac{(\prodi=1n(n_{max}+1−i))⋅[Ca^{2+}]^{n}⋅k_{1}^{n}}{n!⋅b^{\sumj=1n(j−1)}⋅k_{−1}^{n}}⋅\frac{(\prodi=1m(m_{max}+1−i))⋅[Ca^{2+}]^{m}⋅k_{2}^{m}}{m!⋅b^{\sumj=1m(j−1)}⋅k_{−2}^{m}}=(\frac{\frac{n_{max}!}{(n_{max}−n)!}⋅[Ca^{2+}]^{n}k_{1}^{n}}{n!⋅b^{\frac{n(n−1)}{2}}⋅k_{−1}^{n}} )⋅(\frac{\frac{m_{max}!}{(m_{max}−m)!}⋅[Ca^{2+}]^{m}k_{2}^{m}}{m!⋅b^{\frac{m(m−1)}{2}}⋅k_{−2}^{m}})
$$

Note that for n = 0, the first parenthesis is 1, while m = 0 implies that the second parenthesis is 1, making this solution valid also in the absence of a second fusion-sensor. We ignored the very small fusion rate. In the steady-state of the unpriming model, the number of SVs in [R(0,0)] must furthermore be in equilibrium with the number of empty states:

$$
Rn,m_{init}=\frac{(\prodi=1n(n_{max}+1-i))⋅[Ca^{2+}]^{n}⋅k_{1}^{n}}{n!⋅b^{\sumj=1nj-1}⋅k_{-1}^{n}}⋅\frac{(\prodi=1m(m_{max}+1-i))⋅[Ca^{2+}]^{m}⋅k_{2}^{m}}{m!⋅b^{\sumj=1mj-1}⋅k_{-2}^{m}}
$$

After finding this steady-state, the solution is scaled to match the desired number of SVs by multiplying all states with a constant, such that the sum of all [R(n,m)] and [P] equals the number of SVs. The steady-state of the site activation was determined before simulation by calculating the fraction of states being in [A], [D], or [I]. This was done by calculating

$$
=\frac{\frac{n_{max}!}{(n_{max}-n)!}⋅Ca^{2+}^{n}k_{1}^{n}}{n!⋅b^{\frac{nn-1}{2}}⋅k_{-1}^{n}}⋅\frac{\frac{m_{max}!}{(m_{max}-m)!}⋅Ca^{2+}^{m}k_{2}^{m}}{m!⋅b^{\frac{mm-1}{2}}⋅k_{-2}^{m}}
$$

and normalizing to sum to 1. This determined the steady state fraction of activation of sites. In the stochastic simulations, the SVs were randomly assigned initial states according to the probabilities of the different states in the steady-state.

### Deterministic exocytosis simulation

All deterministic exocytosis simulations of the above equations were carried out with the inbuilt MATLAB ODE solver ode15s.

### Stochastic exocytosis simulation

All stochastic exocytosis simulations as well as simulation data handling were carried out in MATLAB with custom-written scripts (included in Source code 1). For the simulation itself we used a modified version of the Gillespie Algorithm (Gillespie, 2007), which included a minimal time step since reaction rates change quickly with the changing intracellular Ca2+ concentration. The minimal step was µ = 1e-6 s. In the algorithm, the time from the current simulation time point, t, until the next reaction,τ, is determined, the reaction is carried out and the new simulation time point is set to t+τ. Whenever the simulation yielded τ>µ, the simulation time point was set to t+µ, no reaction was carried out and the propensities of the model were updated at the new time point. This is a valid method of obtaining a better estimate because the waiting time until next reaction is exponentially distributed.

The implementation of the algorithm takes advantage of the general form of the rate equations in (7). Instead of calculating matrices of states and reaction rates, we have a vector, V, of length nsites, where each element represents the status of one SV/site. The SV state of a docked SV on the kth site in state [R(n,m)] is denoted by the two-digit number

$$
P=\frac{r⋅u}{k_{rep}+r⋅u}⋅[R0,0]
$$

If the site was empty (due to initial submaximal priming or SV fusion) we assigned $V_{k}=100$.

Using Equation 7, the rates of any primed SV are

$$
r_{k}=(m⋅k_{−2}⋅b^{m−1}n⋅k_{−1}⋅b^{n−1}L^{+}f^{n}s^{m}(n_{max}−n)⋅[Ca^{2+}]⋅k_{1}(m_{max}−m)⋅[Ca^{2+}]⋅k_{2}r⋅b)
$$

The sum of these rates of all SVs yield the summed propensities of the system, a0, which is the basis of the calculation of τ, whereas the cumulative sum is used for determination of which SV undergoes a reaction (Gillespie, 2007). When a SV undergoes a reaction, we find the index of the reaction occurring, j, by using the cumulative sum of rk in the same way as in the standard implementation of the Gillespie Algorithm (Gillespie, 2007). Putting $j^=j−3$ allows us to easily update the status of the SV, since

$$
V_{k}=V_{k}+1_{(j^\neq3)}⋅sign(j^)⋅10^{|j^|−1}+1_{(j^=0)∨(j^=3)}⋅(100−V_{k})
$$

In parallel with this a vector of fusions is updated, such that at every time point, the next element in the fusion vector is set to 1 if a fusion took place, and 0 else.

### Parallel computing

Many repetitions of time consuming stochastic simulations had to be performed, and many sets of ODEs were solved for each choice of parameters. Therefore, simulations were carried out on the computer grid on The Bioinformatics Center, University of Copenhagen. This allowed running repetitions in parallel with MATLAB’s Parallel Computing toolbox using between 5 and 100 cores depending on the simulation job.

### Calculating the postsynaptic response

In order to calculate the eEJC, we needed a vector of the SV fusions at different time points. Both deterministic and stochastic simulations yielded the vectors time_outcome and fuse_outcome, which is a pair of vectors of the same length but with changing time steps. For the sampling we generated a time vector, time_sample, with a fixed time step of 1 µs. From here, the determining of the SV fusion times differ between deterministic and stochastic simulations.

In the deterministic simulations, we simulated a sample of distances, bins, as described earlier. Each bin gave rise to a set of ODEs, which could be simulated independently, and the fuse_outcome is continuously changing based on the rates. In MATLAB the interpolation for bin k was done as follows:

$$
fuse_interp_{k}=interp1(time_outcome,fuse_outcome,time_sample)
$$

fuse_interpk contained the cumulative fused SVs over time in a single bin sampled at the time points of the vector time_sample. These were summed to find the total number of fused SVs:

$$
V_{k}=V_{k}+1_{(j^\neq3)}⋅signj^⋅10^{j^-1}+1_{j^=0∨(j^=3)}⋅100-V_{k}
$$

Therefore the SVs fused per time step were be the difference between neighboring values in the fuse_interp vector:

$$
fusion_vec=[0,diff(fuse_interp)]
$$

This vector was the basis for the computation of the eEJC.

In the stochastic simulations, the fuse_outcome vector contains discrete SV fusions at certain time points. We therefore sample the SV fusions by assigning them to the nearest time points on the time_sample vector. That is, each fusion time was rounded to the nearest microsecond, thereby giving rise to the fusion_vec, which in the stochastic case contained whole numbers of SV fusions at different time points.

In both deterministic and stochastic simulations the mEJC was generated as a vector, mEJC_vec, with the same time step as the time_sample and fuse_vec. This allows us to calculate the eEJC with MATLAB’s convolve function, conv, such that

$$
eEJC=conv(fuse_vec, mEJC_vec)
$$

where fusion_vec is a vector with the same time step, each element being the number of SV fusions at each time point.

### Analysis of simulated eEJCs

The eEJC1 amplitude was determined as the minimum current of the eEJC within the time interval (0,10) ms. Similar to the analysis of experimental eEJC data, we fitted an exponential function to the decay for estimation of the base value for the second response (see Figure 2—figure supplement 1A). The eEJC2 amplitude was the difference between the second local minimum and the fitted exponential function extrapolated to the time point of the second local minimum (as described for the analysis of electrophysiology experiments).

### Fitting routine

Because deterministic simulations cannot predict PPR values (due to Jensen’s inequality, see above), but stochastic simulations cannot be fitted to data, we first ran deterministic simulations comparing the simulated first and second absolute eEJC amplitudes to the experimental amplitudes (not the PPR, see Materials and methods). Afterwards we ran stochastic simulations with the optimised parameters in order to compare PPRs and variances to experimental results. To determine the optimal parameters for the deterministic simulations at the five experimental extracellular Ca2+ concentrations, the models were fitted to the two peak amplitudes, eEJC1 and eEJC2, by minimizing the following cost value:

$$
fuse_interp=\sumk=1n_{bins}fuse_interp_{k}
$$

where we sum over the five different experimental Ca2+ concentrations. Note that in deterministic simulations, eEJC1 and eEJC2 amplitudes are precise estimates of average amplitudes in stochastic simulations allowing us to do deterministic optimizations.

When fitting the models, we used the inbuilt MATLAB function fminsearch, which uses the Nelder-Mead Simplex Search, to minimize the above cost function. The cost calculation in each iteration was a two-step process taking advantage of the fact that the total number of SVs scales the eEJC1 and eEJC2 values in the deterministic simulations. For each choice of parameters the simulation was run with 180 sites (the initial number of sites is arbitrary, but matched the number of distance bins), and the optimal number of sites were determined afterwards. Thus, a given set of parameters gave rise to amplitudes eEJC1,init and eEJC2,init from simulations with 180 sites. After that we determined $eEJC=conv(fuse_vec,mEPSC_vec)$ such that $cost(eEJC_{1,sim},eEJC_{2,sim})=\sumk=15\frac{eEJC_{1,sim,k}-eEJC_{1,exp,k}^{2}}{eEJC_{1,exp,k}}+\frac{eEJC_{2,sim,k}-eEJC_{2,exp,k}^{2}}{eEJC_{2,exp,k}}$ was minimized. The number of sites in the given iteration was therefore 180⋅csites and the cost of that particular iteration was

$$
c_{sites}\inR^{+}
$$

In this way the optimization algorithm did not have to include nsites in the parameter search algorithm, which reduced the number of iterations significantly.

In the stochastic simulations, the number of SVs was set to 180⋅csites rounded to nearest integer.

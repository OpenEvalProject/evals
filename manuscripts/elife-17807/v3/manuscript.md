# Cortical flow aligns actin filaments to form a furrow

## Authors

- Anne-Cecile Reymann<sup>1</sup> ([ORCID: 0000-0002-0517-5083](https://orcid.org/0000-0002-0517-5083))
- Fabio Staniscia<sup>3</sup>
- Anna Erzberger<sup>3</sup>
- Guillaume Salbreux<sup>3</sup> †
- Stephan W Grill<sup>1</sup> †

### Affiliations

1. Biotechnology Center Technische Universität Dresden Dresden Germany
2. Max Planck Institute of Molecular Cell Biology and Genetics Dresden Germany
3. Max Planck Institute for the Physics of Complex Systems Dresden Germany
4. The Francis Crick Institute London United Kingdom

† Corresponding author

## Abstract

Cytokinesis in eukaryotic cells is often accompanied by actomyosin cortical flow. Over 30 years ago, Borisy and White proposed that cortical flow converging upon the cell equator compresses the actomyosin network to mechanically align actin filaments. However, actin filaments also align via search-and-capture, and to what extent compression by flow or active alignment drive furrow formation remains unclear. Here, we quantify the dynamical organization of actin filaments at the onset of ring assembly in the C. elegans zygote, and provide a framework for determining emergent actomyosin material parameters by the use of active nematic gel theory. We characterize flow-alignment coupling, and verify at a quantitative level that compression by flow drives ring formation. Finally, we find that active alignment enhances but is not required for ring formation. Our work characterizes the physical mechanisms of actomyosin ring formation and highlights the role of flow as a central organizer of actomyosin network architecture.

## Introduction

Cytokinesis begins in late anaphase, triggered by regulatory pathways with feedback from the mitotic spindle that ensure appropriate positioning of the molecular machinery (reviewed in Fededa and Gerlich, 2012; Green et al., 2012). As a consequence, the small regulatory GTPase RhoA (Piekny et al., 2005; Tse et al., 2012) and the molecular motor myosin (Shelton et al., 1999; Werner and Glotzer, 2008) are enriched in an equatorial band (Piekny et al., 2005; Werner and Glotzer, 2008). Myosin can directly organize the actin network (Miller et al., 2012; Soares e Silva et al., 2011; Vavylonis et al., 2008), and if myosin-based active alignment (e.g. via search-and-capture [Vavylonis et al., 2008]) or flow-based compression as proposed by White and Borisy (White and Borisy, 1983; Rappaport, 1996) drive furrow formation and cytokinesis in eukaryotes remains unclear (Green et al., 2012; Bray and White, 1988; Levayer and Lecuit, 2012; Mendes Pinto et al., 2013; Cao and Wang, 1990; Murthy and Wadsworth, 2005; Zhou and Wang, 2008).

## Results and discussion

We set out to address this question in the one cell embryo of the nematode C. elegans which forms two constricting ingressions, first a pseudocleavage furrow during polarity establishment, and then a cytokinetic furrow during cytokinesis (Figure 1—figure supplement 1a, Video 1) (Munro and Bowerman, 2009; Rose et al., 1995). Notably, the pseudocleavage furrow is linked to cortical flow (Mayer et al., 2010; Munro et al., 2004) and lacks regulatory control from the mitotic spindle (Werner and Glotzer, 2008). We first characterized the actomyosin cortical network during pseudocleavage and cytokinesis. For this, we generated a Lifeact::mKate2 fluorescent line of C. elegans by coupling the Lifeact peptide to the far-red fluorophore mKate2 that was codon optimized for C. elegans (Redemann et al., 2011) (see Materials and methods and Video 2). This allows us to quantify cortical actin filament orientation in space and time, as well as cortical flow velocity fields by Particle Image Velocimetry (PIV, Figures 1 and 2, Figure 2—figure supplement 1) (Mayer et al., 2010). We find that actin filaments change from a randomly oriented and isotropic gel before cortical flows initiate, into a more circumferentially aligned organization at the future site of furrow ingression during both pseudocleavage and cytokinesis (Figure 1b, Figure 1—figure supplement 1 and Videos 1 and 3). We studied how pseudocleavage and cytokinesis differ in the spatial distribution of molecular regulation and contractility within the equatorial region (Figure 1). Non-muscle myosin II (NMY-2) is the essential molecular motor that drives both cortical flow and cytokinesis (Shelton et al., 1999; Guo and Kemphues, 1996), whereas the small GTPase RhoA (Piekny et al., 2005; Tse et al., 2012), when active, is responsible for its local activation. At the onset of cytokinesis, active RhoA and NMY-2 locally increase at the position of the contractile ring, while for pseudocleavage we observed no such increase (Figure 1). Instead, the equatorial region in pseudocleavage corresponds to a transition zone with a gradual decrease of RhoA and myosin between the anterior region of high and the posterior region of low contractility (Figure 1) (Mayer et al., 2010). The actin nucleator formin CYK-1 is downstream of RhoA (Piekny et al., 2005) and follows a similar pattern of localization, and actin bundling via anillin (Piekny and Glotzer, 2008) or plastin also does not appear to be increased in the equatorial region during pseudocleavage (Figure 2—figure supplement 5e–f). To conclude, the pseudocleavage furrow ingresses with a circumferential alignment of filaments in the gel, but without a local zone of RhoA activation and the corresponding local increase in myosin and formin density. Since search-and-capture like mechanisms require a localized band of myosin and actin nucleators at the equator to drive myosin-based active alignment (Vavylonis et al., 2008), this suggests that actin filaments in pseudocleavage align via flow-based compression and not via active alignment.

![Video 1.](https://cdn.elifesciences.org/articles/17807/elife-17807-media1.mp4.jpg)

**Video 1.:** Cortical and medial planes of an embryo expressing both Lifeact::mKate2 and endogenous NMY-2::GFP. Left panel, medial plane Lifeact:mKate2, center, cortical NMY-2::GFP, right panel, cortical Lifeact:mKate2 (min:s).

![Video 2.](https://cdn.elifesciences.org/articles/17807/elife-17807-media2.mp4.jpg)

**Video 2.:** The back of the embryo is dimmer due to imaging.

![Figure 1.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig1-v3.jpg)

**Figure 1.:** (a) Average active RhoA biosensor intensity profiles along the AP axis (0 represents the embryo center; N = 14 embryos for pseudocleavage and N = 7 for cytokinesis; errors represent the standard error of the mean). (b) Actomyosin cortical organization at the onset of pseudocleavage and cytokinesis in embryos expressing both Lifeact::mKate2 and NMY-2::GFP. (c–d) Average actin, myosin and ingression profiles as a function of position along the AP axis (N = 10 embryos for pseudocleavage and N = 22 for cytokinesis; errors represent the standard error of the mean). Scale bars, 10 μm. The following figure supplement is available for Figure 1:

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (a) Actomyosin gel dynamics in the C. elegans zygote. Single cortical and medial planes from a timelapse sequence of a representative embryo expressing both Lifeact::mKate2 and NMY-2::GFP. Anterior is to the left, posterior to the right. White arrows indicate the position of pseudocleavage and cytokinesis ingressions. Red arrows indicate flow directions. (b) Close up look at the filaments dynamics near the site of flow initiation. Cortical plane from a timelapse sequence of an embryo expressing both Lifeact::mKate2 and NMY-2::GFP. (c) Top: Actin network organization from an embryos expressing Lifeact::mKate2. Times rescaled to 0 at flow initiation. Green arcs indicate the smooth cleared zone during the polarization process. Red lines schematize filaments maximum vertical alignment positions. White arrows underlie pseudocleavage ingression. Bottom: color-coded representation of the orientation of filaments. (d) Example from an embryo for which the polarization process starts off centered from the physical pole of the embryo due to a mispositioning of the sperm pronucleus (dashed circle on medial plane). Alignment direction is observed to follow perpendicularly to the direction of the flow as it reorients along the long axis of the embryo (also see Appendix). Red arrows represent flow direction, red lines filaments main orientation. Scale bars, 10 μm.

![Figure 2.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig2-v3.jpg)

**Figure 2.:** (a) Filament orientation is quantified by a nematic order parameter; flow fields are obtained from Particle Image Velocimetry (PIV) analysis. (b) Gel flow, compression rate, filament orientation and cell ingression fields. Top row, schematic representations. Middle row, kymographs of the time evolution of the profiles along the AP axis of flow velocity, compression rate, nematic order parameter and outer ingression distance for pseudocleavage (N = 10). Bottom row, cytokinesis (N = 12). Orange dashed lines indicate the times where all four fields are stationary. Flow, compression and nematic order were determined from bottom-section and ingression from mid-section views of Lifeact::mKate2 labelled embryos (see Materials and methods and Appendix). (c) Spatial correlation between compression, alignment and ingression (see Materials and methods). Peak value positions (estimated by a Gaussian fitting of the 1D correlation curve) are indicated. See Figure 2—figure supplement 2 for spatiotemporal correlation functions. (d) Table of the temporal delays obtained from the correlation peak value positions using the mean values of the velocity in the 10 μm central region (mean values for pseudocleavage: $v$ = 6.16 ±1.23 μm/min; for cytokinesis: $v$ = 4.01±1.92 μm/min; mean ± SD).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (a) Example of the filaments alignment quantification (red lines) and the flow velocity field (yellow arrows), as well as nematic order parameters conventions. (b) Time evolution of flow (light green) and compression rate (dark green) as well as ingression (grey) measured at a fixed position along the AP axis (−20 μm for velocity, 0 μm or central position of the embryo for compression and 3 μm for ingression, measured from the center). Error bars represent the standard error of the mean. Bottom, fit using the error function (red line) of the time evolution of the velocity from a single embryo (blue dots) used to determine the reference time point (Time = 0). (c) Time evolution of the mean velocity and compression rate along the AP axis and nematic order parameter, all taken at fixed positions along the AP axis. Error bars represent the standard error of the mean. In orange is represented the period chosen as stationary flow phase. (d) Mean profiles along the AP axis of the velocities (vx light green and vy yellow), compression rate and nematic order parameters (Q = −Qxx in dark blue and Qxy in cyan) during the stationary flow phase. (See Appendix for further explanations.)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** Plots of the spatiotemporal correlations between the compression, alignment and ingression data sets taken during the pseudocleavage stationary phase (a) and cytokinesis onset stationary phase (b). Data is restricted to the 30 μm central region of the embryo.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** (a) Example of a simulated isotropic actin meshwork (see Appendix for details). (b) Example of a simulated actin meshwork for which the angle of the starting direction is biased toward vertical (see Appendix). (c) Cumulative distribution function (CDF) used and example of an image and its nematic order map (red lines indicate the preferential orientation inside a template or orientation vector) obtained for different values of the starting parameter B that controls the bias of the filaments orientation. B = 0 leads to an isotropic orientation. (d) Variation of the average nematic order parameter obtained for several synthetic meshworks while increasing the vertical bias of the filaments orientation. The saturation is caused by the fact that we here bias only the initial direction of growth.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig2-figsupp4-v3.jpg)

**Figure 2—figure supplement 4.:** (a) An artificial filamentous network is obtained by a random iteration process with controllable parameters in Matlab (see Appendix for more details). (b-d) We chose to maintain a vertical bias in the orientation of the filaments in all the following cases (B = 1). Red lines indicate the preferential orientation inside a template or orientation vector. A profile of the mean nematic order parameter along the x-axis as well as the angular distribution are shown in all cases. Note that as we do not measure the directionality of filaments thus we obtain values modulo π. (b) Impact of the filament density (ranging from 60 to 120 filaments per image) on the nematic order parameter quantification. The profile of nematic order is to first order independent of network density. (c) Impact of the signal to noise ratio. High signal to noise ratio leads to higher values of the nematic order parameter, low signal to noise ratio leads to a poor detection of the direction of the filaments and artificially small values of the nematic order parameter.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig2-figsupp5-v3.jpg)

**Figure 2—figure supplement 5.:** (a–c) Average AP profiles of flow velocity (light green) and nematic order parameter (blue) at the time of stationary flow during pseudocleavage of respectively 22 embryos expressing Lifeact:GFP, NMY:RFP, 9 embryos expressing Lifeact:RFP, NMY-2:GFP and 16 embryos expressing Lifeact:mKate2, NMY-2:GFP. Overlaid in red is the velocity profile of worms expressing only labeled NMY-2 (N = 5). Error bars represent the standard error of the mean. (d) Images of NMY-2:GFP in the early zygote. Left strain without Lifeact, right strain expressing Lifeact:mKate2. The density, size and dynamics are similar in both strains. Right panel, the average radial autocorrelation coefficient of the myosin intensity over a minute in early embryos gives an average myosin foci size. (e) Localization of the actin bundling protein plastin during pseudocleavage and cytokinesis. Plastin localizes in dense bundles of actin filaments and is particularly abundant in the cytokenetic ring and could act to stabilize actin bundles in these regions. (f) Localization of the actin nucleating agent formin during pseudocleavage and cytokinesis. CYK-1 is present throughout the cell cortex during pseudocleavage, with higher densities in foci regions. It is recruited to the cell equator during cytokinetic ring formation and ingression. Scale bars, 10 μm.

![Video 3.](https://cdn.elifesciences.org/articles/17807/elife-17807-media3.mp4.jpg)

**Video 3.:** Left panel, cortical NMY-2::GFP, center cortical Lifeact:mKate2 and a zoom is shown in the right panel (min:s).

We next sought to test if flow-based compression drives actin filament alignment. To this end, we developed tools for the spatiotemporal quantification of compression by flow, of filament orientation, and of cortex ingression distance within the gel both at the onset of pseudocleavage and cytokinesis (see Appendix as well as Figure 2a and Figure 2—figure supplement 1). We find that the flow compression rate along the antero-posterior direction (AP axis or x axis), given by the spatial gradient of the velocity field −∂xv  (Figure 2b), increases with time during the very early stages of pseudocleavage. The compression rate peaks in the central region of the embryo, with a maximum of ~0.4 min−1. Notably, this peak is stable for several minutes until pseudocleavage flows cease entirely (Figure 2b). For cytokinesis, we find that the early flow also proceeds in a unidirectional manner from the posterior toward the anterior (Figure 2b). Similar to pseudocleavage, the compression rate increases with time over the very early stages of cytokinesis, with the compression profile peaking at the center of the embryo with a maximum rate of ~0.7 min−1 (Figure 2b). We characterized the average actin filaments orientation by a nematic order tensor Q (Figure 2—figure supplement 1a). This analysis relies on the fact that the intensity of the Fourier transformed image encodes geometric characteristics such as its main orientation pattern (see Appendix). We find that vertical (orthogonal to the direction of flow) alignment appears coincidental in space and time with the local increase of the compression rate (Figure 2b, compare column 2 and 3). Notably, changing the direction of flow also changes the direction of alignment: off-site sperm entry leads to flows along the short axis of the egg (Goldstein et al., 1993) and actin filaments still align in the direction determined by compression (Figure 1—figure supplement 1d, Video 4 and Appendix). Finally, the ingressing furrow forms in the region where filaments are aligned (Figure 2b, column 4). Our quantifications reveal remarkable similarities between the compression rate fields, the pattern of alignment, and the ingression distance between pseudocleavage and cytokinesis (Figure 2b), suggesting common mechanisms. To conclude, actin filament alignment arises at locations of significant compression by flow.

![Video 4.](https://cdn.elifesciences.org/articles/17807/elife-17807-media4.mp4.jpg)

**Video 4.:** Actin filament alignment follows flow and compression, thus transitions from a horizontal to a vertical direction (min:s).

If flow-based compression aligns actin filaments for forming an ingression, we would expect compression to precede or to be concomitant with alignment and ingression. The 1D crosscorrelations between compression, filament alignment and ingression distance, calculated for the time that flows are essentially stationary (Figure 2b and Figure 2—figure supplement 1), show that for pseudocleavage both compression rate and alignment peak at about the same location, while the ingression field peaks ~ 3 µm further to the anterior (Figure 2c and Figure 2—figure supplement 2 for the spatiotemporal crosscorrelations). The situation is similar at cytokinesis, except that the compression field peaks furthest to the posterior. We next translated the characteristic distances between peaks in stationary flow to temporal delays between events (see Materials and methods for further explanation). We find that for pseudocleavage, filament alignment is essentially concomitant with compression, while for cytokinesis compression precedes alignment by 0.40 ± 0.16 min (Figure 2d). Furthermore, ingression arises approximately 0.5 min after compression for pseudocleavage and 0.9 min after compression for cytokinesis. To conclude, filament alignment appears to rapidly follow compression while ingression arises with a delay.

We next sought to provide a physical explanation for flow-based alignment (Salbreux et al., 2009). The cell cortex in this and other systems can be thought of as a gel that forms a thin layer underneath the plasma membrane. Recent advances in physical theory show that this gel is active and generates the forces that drive cell shape changes (Salbreux et al., 2009; Gowrishankar, 2012; Kruse et al., 2005; Turlier et al., 2014). We describe the actin cortical layer as a thin film of a nematic gel under shear and compression by flow (Salbreux et al., 2009; Kruse et al., 2005; Prost et al., 2015). In the x-direction, the time evolution of the local nematic order Q depends on advection (first term on the right hand side in Equation 1), compression in gel flow (second term), a process of relaxation to an isotropic configuration possibly via turnover (third term), and a tendency of filaments to align with each other over space (last term, see also Figure 3a)(1)∂tQ=−v∂xQ−β2∂xv−1τQ+ℓ2τ∂x2Q.

![Figure 3.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig3-v3.jpg)

**Figure 3.:** (a) Schematic representation of flow-based alignment. For full theory refer to Appendix. (b) Average AP profiles of gel flow (light green, smoothened), compression rates (dark green) and nematic order parameter (blue) at the time of stationary flow (Figure 2C) during pseudocleavage (left, N = 16) and cytokinesis onset (right, N = 32). Error bars represent the standard error of the mean. Dashed red line indicates the respective best-fit theory predictions for the nematic order parameter (blue). (c) Table of the material parameters. See also Figure 3—figure supplement 1 and Table 1, Table 2. (d) Illustration of the cortical tension related to the ingression distance. (e) Outer ingression profiles at the onset of pseudocleavage (brown) and cytokinesis (yellow). The theoretical profiles (thick dashed red lines: active tension depends on alignment and can be anisotropic; thin dashed lines: active tension is isotropic) are determined by simultaneous fitting of both the pseudocleavage and cytokinesis datasets with a single fit parameter (see Appendix) using the myosin density, flow velocity and nematic order parameter fields.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (a) Nematic order parameter profiles obtained when varying independently each of the fitting parameters $\tau$, $\beta\tau$, $ℓ$ away from their the best fit values obtained for cytokinesis. Dashed red line, best fit result ($\tau$ = 2.34 min, $\beta\tau$ = 0.654 min, $ℓ$ =1.69 μm). For each set of parameters $\tau$, $\beta\tau, ℓ$, a fit is performed for the fitting parameters C1 and C2 only (see Appendix). (b) Nematic order parameter profiles obtained when varying the fitting parameter $\tau $ while keeping $\beta\tau$, $ℓ$ fixed and equal to their best-fit values. Appropriate fits to experimental curve are obtained for all values of $\tau$ < 0.5 min. For each value of $\tau$, a fit is performed for the fitting parameters C1 and C2 only.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** (a) Average AP profiles of gel flow (light green), compression rates (dashed dark green), nematic order parameter (blue) and myosin fluorescence (magenta) at the time of stationary flow during pseudocleavage (left, N = 16) and cytokinesis onset (right, N = 32). Error bars represent the standard error of the mean. Dashed red lines indicate the best-fit theory predictions for the nematic order parameter in absence of active alignment, dashed black lines are the fits obtained while including the myosin-based active alignment, with $\lambda^{′}\tau=4.1 10^{−8}\pm0.54$ for pseudocleavage and $\lambda^{′}\tau=0.34\pm 0.45$ for cytokinesis. (b) Contribution of the individual terms from Equation 3 in the main text (red: $−\frac{\beta}{2}\tau∂_{x}v$, green: $−\tauv∂_{x}Q$, blue: $ℓ^{2} \partial_{x}^{2}Q$, magenta: $\lambda^{′}\tau c(x)/c_{0}Q$). Note that myosin-based active alignment (magenta) is insignificant for pseudocleavage and is low for cytokinesis compared to compression-based alignment (red). The theoretical alignment profile (sum of all the terms shown in black) overlays the experimental data points (dots).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** (a) Top, a representative embryo is used to visualize the time course of ingression. Bottom, Kymograph obtained from the region specified by the dashed white box in the upper pannel. The pseudocleavage and cytokinesis ingressions are visible. Yellow arrow indicates the inner ingression distance during polarizing flow phase, magenta dashed line indicates the ingressing membrane and blue arrow indicates the outer ingression. Red doted lines represent the position of the eggshell. Scale bar 10 μm. (b) Top, illustration of the cortical tension during ingression. Bottom, outer ingression profiles (grey) averaged over the time periods indicated by the thin horizontal white lines in (a, bottom) during pseudocleavage (left) and cytokinesis (right). The theoretical profiles (dashed red lines) are determined by simultaneous fitting of both the pseudocleavage and cytokinesis datasets with a single fit parameter (see Appendix) using the myosin density (magenta), flow velocity (green) and nematic order parameter (blue) fields. (c) and (d) Illustration of the coordinate and reference systems used for this theoretical description. (e) Comparison of the theoretically obtained profile of the outer ingression without the anisotropic stress induced by nematic order (dashed red, obtained by imposing p3 = 0) during pseudocleavage and cytokinesis phases with the experimental data (black).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig3-figsupp4-v3.jpg)

**Figure 3—figure supplement 4.:** Left column, plots of the cell shape (mean radius for all embryos during the stationary flow phase and eggshell reference) for pseudocleavage (a) and cytokinesis (b). Error bars, the standard error of the mean. Right column, ingression distance for several embryos and mean value (cyan) during the stationary phase of pseudocleavage and cytokinesis.

The characteristic time for relaxation to an isotropic state via turnover is determined by $\tau$, while $\beta$ is a dimensionless coefficient that describes how local compression $−\partial_{x}v$ impacts nematic ordering. Finally, $ℓ$ is a length scale that determines the distance over which actin filaments tend to point in the same direction (Salbreux et al., 2009). In our experiments, we observe a stationary phase (Figure 2b), and the profile of nematic order Q at steady-state is given by

$$
Q=−\tauv∂_{x}Q−\frac{\beta}{2}\tau∂_{x}v+ℓ^{2} ∂_{x}^{2}Q.
$$

We next determined the theoretical alignment field from the experimental flow field v and compression field ∂xv. We used nonlinear least-square fitting to evaluate parameter values for which the theoretical alignment profile best matched the experimental one. There are five unknowns (three parameters that characterize emergent material properties, τ, ℓ, and β τ, as well as two boundary values of nematic order) but three spatial fields, hence the fitting procedure is significantly constrained and the best fit parameters are uniquely defined in most cases (see Appendix and Figure 3—figure supplement 1). For cytokinesis the calculated alignment profile (dashed red lines in Figure 3b) best matches the experimentally measured one for β τ =0.64 (0.548, 0.713) min (unless otherwise noted we indicate the median value together with the standard 68% confidence interval of the distribution of the bootstrap data, see Appendix),  τ = 2.3 (1.89, 2.71) min and ℓ = 1.7 (1.37, 2.44) μm (Table 1 and Table 2). For pseudocleavage, β τ  was similar (0.6 (0.577, 0.7) min), τ was determined to be smaller than 0.5 min, and ℓ = 4.7 (3.12, 6.09) μm larger (Table 1 and Table 2). We note that in both cases, we obtain good agreement between the theoretical and experimental alignment field, allowing us to conclude that compressive gel flow can account for alignment. Further, we observe a small τ for pseudocleavage and a larger τ for cytokinesis, which is consistent with the observation that alignment appears concomitant with compression in pseudocleavage but arises with a short delay during cytokinesis (Figure 2d). We speculate that the changes in physical parameters of the actomyosin cortical layer between pseudocleavage and cytokinesis (higher τ and smaller ℓ) reflect the fact that the cell forms a strong and more pronounced ring of aligned filaments during cytokinesis. To conclude, our results are consistent with a scenario in which actin filament alignment arises in a disordered network through compression by flow (White and Borisy, 1983; Salbreux et al., 2009; Turlier et al., 2014).

**Table 1.**
 Best fit gel material parameters, bootstrapping. The median values together with the standard 68% confidence bounds of the distribution of the bootstrap data are given.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Pseudocleavage</th>
      <th>Cytokinesis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>non RNAi</td>
      <td>non RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>&lt; 0.5 (n.d.) †</td>
      <td>2.26 (1.89, 2.71)</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>0.626 (0.577, 0.7)</td>
      <td>0.646 (0.548, 0.713)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>4.72 (3.12, 6.09)</td>
      <td>1.74 (1.37, 2.44)</td>
    </tr>
    <tr>
      <td></td>
      <td>nop-1 RNAi</td>
      <td>nop-1 RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>n.d. *</td>
      <td>&lt; 0.5 (n.d.) †</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>n.d. *</td>
      <td>0.771 (0.694, 2.75)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>n.d. *</td>
      <td>2.67 (1.7, 11.5)</td>
    </tr>
    <tr>
      <td></td>
      <td>ani-1 RNAi</td>
      <td>ani-1 RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>&lt; 0.5 (n.d.) †</td>
      <td>0.989 (0.555, 1.79)</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>1.45 (0.969, 18) ‡</td>
      <td>0.724 (0.636, 0.929)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>12.3 (6.39, 58.4) ‡</td>
      <td>3.38 (2.97, 6.16)</td>
    </tr>
    <tr>
      <td></td>
      <td>mlc-4  (5–7 hr) RNAi</td>
      <td>mlc-4 (5–7 hr) RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>&lt; 0.5 (n.d.) †</td>
      <td>4.76 (3.67, 6.6)</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>0.467 (0.451, 0.503)</td>
      <td>0.637 (0.567, 0.768)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>2.75 (2.38, 4.1)</td>
      <td>6.58 (5.31, 6.85)</td>
    </tr>
    <tr>
      <td></td>
      <td>mlc-4 (7–9 hr) RNAi</td>
      <td>mlc-4 (7–9 hr) RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>n.d. *</td>
      <td>&lt; 0.5 (n.d.) †</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>n.d. *</td>
      <td>0.916 (0.82, 1.04)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>n.d. *</td>
      <td>3.12 (2.49, 4.18)</td>
    </tr>
  </tbody>
</table>

_*n.d. denotes parameters which could not be determined,†< 0.5 (n.d.) denotes parameters which could not be determined, but could be determined to be below 0.5 (see Figure 3—figure supplement 1b),‡denotes values that could be determined but that were not well constrained._

**Table 2.**
 Best fit gel material parameters, no bootstrapping. The mean values together with its 95% confidence bounds are given.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Pseudocleavage</th>
      <th>Cytokinesis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>non RNAi</td>
      <td>non RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>&lt; 0.5 (n.d.) †</td>
      <td>2.34 (1.74, 3.14)</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>0.59 (0.513, 0.806)</td>
      <td>0.652 (0.541, 0.764)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>5.38 (3.27, 8.85)</td>
      <td>1.69 (1.04, 2.75)</td>
    </tr>
    <tr>
      <td></td>
      <td>nop-1 RNAi</td>
      <td>nop-1 RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>n.d. *</td>
      <td>&lt; 0.5 (n.d.) †</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>n.d. *</td>
      <td>0.738 (0.0.614, 0.862)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>n.d. *</td>
      <td>1.79 (0.64, 5.03)</td>
    </tr>
    <tr>
      <td></td>
      <td>ani-1 RNAi</td>
      <td>ani-1 RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>&lt; 0.5 (n.d.) †</td>
      <td>1.01 (0.989, 1.03)</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>1.31 (0.428, 2.19)</td>
      <td>0.74 (0.588, 0.892)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>10.4 (4.91, 21.9) ‡</td>
      <td>4.08 (2.68, 6.2)</td>
    </tr>
    <tr>
      <td></td>
      <td>mlc-4  (5–7 hr) RNAi</td>
      <td>mlc-4 (5–7 hr) RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>&lt; 0.5 (n.d.) †**</td>
      <td>4.37 (3.08, 6.21)</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>0.454 (0.437, 0.47)</td>
      <td>0.614 (0.501, 0.727)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>2.24 (1.87, 2.67)</td>
      <td>5.81 (5.02, 6.72)</td>
    </tr>
    <tr>
      <td></td>
      <td>mlc-4 (7–9 hr) RNAi</td>
      <td>mlc-4  (7–9 hr) RNAi</td>
    </tr>
    <tr>
      <td>τ, min</td>
      <td>n.d. *</td>
      <td>&lt; 0.5 (n.d.) †</td>
    </tr>
    <tr>
      <td>β τ, min</td>
      <td>n.d. *</td>
      <td>0.97 (0.931, 1.01)</td>
    </tr>
    <tr>
      <td>ℓ, μm</td>
      <td>n.d. *</td>
      <td>2.98 (2.88, 3.08)</td>
    </tr>
  </tbody>
</table>

_*n.d. denotes parameters which could not be determined,†< 0.5(n.d.) denotes parameters which could not be determined, but could be determined to be below 0.5 (see Figure 3—figure supplement 1b),‡denotes values that could be determined but that were not well constrained. Caption for Videos 1Videos 1 to 7_

Until now, we have not considered processes of myosin-based active alignment in our theory (Vavylonis et al., 2008). This simplification is probably appropriate for pseudocleavage, but this is less clear for cytokinesis given that there is a clear band of myosin enrichment at the equator when the cell divides (Figure 1c,d). We next consider active alignment by myosin, and describe the cortical layer as a thin film of an active nematic gel. For stationary flows the profile of nematic order $Q$ is now given by

$$
Q=−\tauv∂_{x}Q−\frac{\beta}{2}\tau∂_{x}v+ℓ^{2} ∂_{x}^{2}Q+\lambdaQ,
$$

where the right-most term describes active alignment by myosin molecular motors, with $\lambda$ an alignment parameter dependent on the local myosin concentration. In our modified fitting procedure, we now evaluate the respective contributions of myosin-based active and flow-based passive alignment to the stationary Q profile, under the assumption that $\lambda$ is proportional to local myosin concentration. We find that considering active alignment does not increase the overall agreement between calculated and measured alignment profiles for both pseudocleavage and cytokinesis (Figure 3—figure supplement 2). Notably, the contribution of active alignment to pseudocleavage is insignificant, while active alignment contributes to enhancing compression-induced alignment during cytokinesis (Figure 3—figure supplement 2b; see Appendix), albeit to a small degree. We conclude that compression by flow and not myosin-based active alignment is the driving force of ring formation in both pseudocleavage and cytokinesis.

A key prediction from our model is that reducing flow speeds and compression rates should give rise to less filament alignment and a possible inhibition of pseudocleavage furrow formation. To test this prediction, we performed weak-perturbation RNAi experiments (Naganathan et al., 2014) of the regulatory myosin light chain of non-muscle myosin (mlc-4(RNAi) (Craig et al., 1983) to mildly reduce actomyosin flow speeds without significant changes in overall actomyosin organization (Figure 4—figure supplement 1). Short feeding times (5–7 hr) lead to a small reduction in gel flow and compression rates (Figure 4a), but actin filaments still aligned in the central region and the pseudocleavage furrow still formed and ingressed. Consistent with our hypothesis, longer feeding times (7–9 hr) lead to a complete abolishment of cortical flow and a loss of both actin alignment and pseudocleavage furrow (Figure 4b). Actomyosin foci are not required for compression-based alignment since anillin- depleted embryos (ani-1(RNAi), 24 hr) still show significant alignment under compression in the absence of these dense foci (Figure 4c) (Maddox et al., 2005; Piekny and Maddox, 2010; Tse et al., 2011). Reduced flow speeds and compression rates can also account for the absence of alignment and pseudocleavage in nop-1(RNAi) embryos, in which RhoA-dependent processes are affected and pseudocleavage formation abrogated (Figure 4d, Figure 4—figure supplement 1 and 2) (Tse et al., 2012; Rose et al., 1995; Zhang and Glotzer, 2015). Overall, these experiments lead us to conclude that reducing gel flow and compression rates affects alignment in a manner that is consistent with Equation 2. Finally, a complete loss of flow and compression abolishes pseudocleavage entirely (Figure 4b;d and Figure 4—figure supplement 1). Taken together, our results suggest that the pseudocleavage furrow arises as a by-product of compressive flows, mechanically aligning actin filaments into a ring even in the absence of localized RhoA activation.

![Figure 4.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig4-v3.jpg)

**Figure 4.:** (a-d) Average AP profiles of gel flow (light green, smoothened), compression rates (dark green) and nematic order parameter (blue) at the time of stationary flow during pseudocleavage onset for mlc-4 5–7 hr and 7–9 hr, nop-1 and ani-1 RNAi. Error bars represent the standard error of the mean (N = 17, 14, 10, 22 for a-d, respectively). Dashed red line indicate the respective best-fit theory predictions for the nematic order parameter (blue). For ani-1 and mlc-4 (5–7 hr), $\tau$ is small and is determined to be smaller than 0.5 min. For nop-1 and mlc-4 (7–9 hr), theory profiles were generated using the parameters obtained for the unperturbed non-RNAi pseudocleavage, since insufficient compression rates did not constrain the physical parameters. Scale bar, 10 μm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (a-d) Actin organization and myosin distribution under nop-1(RNAi), ani-1(RNAi) and mlc-4(RNAi). Inserts with fluorescence intensity profiles during pseudocleavage and cytokinesis onset are overlaid next to the corresponding images (actin in blue, myosin in magenta). Note that ANI-1 depleted embryos had more elongated and thin anterior halves, with no localized dense actin ring like structure and no clear and stable central furrow with membrane overlapping. Also note that the asymmetry in the distribution of actin (usually denser in the anterior half of the embryo) during cytokinesis was reduced for both nop-1 and long mlc-4(RNAi). Right, combined images and zoom (green Lifeact, red NMY-2). Scale bar, 10 μm (full images); 5 μm (zoom).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** (a-d) Results of nop-1(RNAi), ani-1(RNAi) and mlc-4(RNAi). Average AP profiles of gel flow (light green, smoothened), compression rates (dark green) and nematic order parameter (blue) at the time of stationary flow during cytokinesis onset. Error bars represent the standard error of the mean (for nop-1, ani-1, mlc-4 5–7 hr and 7–9 hr, N = 9, 18, 9, 13, respectively). Dashed red line indicates the respective best-fit theory predictions for the nematic order parameter (blue). For cytokinesis mlc-4 (7–9 hr) tau is small and is determined to be smaller than 0.5 min. (e-f) Overlay of the different profiles at pseudocleavage and cytokinesis onset, non-RNAi is shown in blue and compression rates in dashed lines. Note that the level of outer ingression was similar to the non-RNAi case for ani-1(RNAi) pseudocleavage, but with improper location and no membrane overlapping, thus no full pseudocleavage furrowing was obtained but a remaining initial anterior ingression was achieved in the presence of some filaments alignment.

In this context we wondered if the cortex is specifically modified to favor ring formation in cytokinesis. We used our fitting procedure to determine the parameters that characterize emergent material properties of the cortex under mlc-4(RNAi). Notably, we observe that 7–9 hr of mlc-4(RNAi) leads to a reduction of the alignment relaxation time scale $\tau$ during cytokinesis. The value obtained is similar to the alignment relaxation time scale during pseudocleavage under non-RNAi conditions (Table 1 and Table 2), leading us to speculate that an increase in myosin activity via Rho signaling is responsible for the observed increase of the characteristic relaxation time $\tau$ in cytokinesis. Importantly, increasing $\tau$ allows the cell to form a pronounced ring of aligned filaments by compressive cortical flow during cytokinesis, as predicted by theory (Figure 3—figure supplement 1).

Finally, we sought to find support from theory that aligned filaments in the equatorial region drive anisotropic stress generation (Mayer et al., 2010) to form an ingression (White and Borisy, 1983; Salbreux et al., 2009; Turlier et al., 2014). By use of a theory that connects anisotropic active stress generation in the active nematic gel to changes in cell shape (see Appendix and Figure 3d) we show that we cannot appropriately account for the observed ingression profiles unless we consider anisotropic active stress generation in an aligned gel (Figure 3e, Figure 3—figure supplement 3). This suggests that anisotropic active stress generation in a network of aligned actin filaments is important for forming an ingression.

To conclude, we find that compression by flow drives actomyosin ring formation in both pseudocleavage and cytokinesis, as originally proposed by White and Borisy (White and Borisy, 1983) (Figure 5). For this, we provide a general framework for determining emergent material parameters of the actomyosin gel. This characterizes flow-alignment coupling and allows for capturing essential aspects of the mechanics of furrow generation. Our analysis of the pseudocleavage ingression in C. elegans demonstrates that constricting rings can form in the absence of equatorial RhoA activation. This reveals that cortical flow functions as a central organizer of network architecture, mechanically aligning filaments to form a constricting furrow in the equatorial region without a localized increase of actin nucleation (Figure 2—figure supplement 5,f) and myosin contractility (Figure 1b-d). Finally, it will be interesting to investigate if a cortex that is aligned by compressive flow favors the recruitment of specific actin binding proteins such as bundling or motor proteins (Robinson et al., 2002), comprising an interesting mechanism of positive feedback for stabilizing and enhancing the ring during cytokinesis. Our work highlights that determining emergent material properties of actomyosin is important for understanding cytokinesis, and a challenge for the future is to link emergent material properties at the larger scale with molecular mechanisms (Mendes Pinto et al., 2013; Eggert et al., 2006).

## Materials and methods

### C. elegans strains

Existing reagents did not allow for detailed and long-term imaging of actin filaments in embryos, which is critical for reliably quantifying their orientation. Hence, we generated a new Lifeact transgenetic line with enhanced actin filament labeling (SWG001). A codon optimized for C. elegans far-red fluorophore, mKate2 kindly shared by Henrik Bringman (Redemann et al., 2011) (26 kDa, 588/633 nm) was added to the actin probe with a linker (66 bp) and cloned into MOSCI vector containing unc119 rescue gene (Hyman Lab) under the control of the mex-5 promoter. Stable integration was obtained by bombardment of this plasmid in DP38 strain. This strain was then backcrossed with N2. In this line, we observed within the cortical plane bright actin filament labeling with a high signal-to-noise ratio and little photobleaching. Importantly, overall cortical organization and flow dynamics appeared to not be affected by this reagent, foci lifetime, spacing, cortical flow velocities were similar to previous measurement with other fluorescent lines. A dual colored transgenic line was obtained in order to image simultaneously actin and myosin dynamics by crossing Lifeact::mKate2 strain with LP133 (NMY-2::GFP obtained by CRISPR (Dickinson et al., 2013), SWG007). The RhoA biosensor used for Figure 1 was developed by the Glotzer lab (GFP::AHPH, C. elegans strain MG617, Tse et al., 2012). This sensor consists of GFP fused to the C-terminal portion of C. elegans anillin, which contain its conserved region (AH) and pleckstrin homology (PH) domain. It lacks the N-terminal myosin and actin-binding domains but retains its RhoA-binding domain. The strains expressing CYK-1:GFP (SWG004) and PLST-1:GFP (SWG005) were obtained by the insertion of a GFP tag at the endogenous locus in their C-terminal region using CRISPR according to Dickinson et al (Dickinson et al., 2013). C. elegans worms were cultured on OP50-seeeded NGM agar plates as described (Brenner, 1974).

### Microscopy

L4 mothers were maintained overnight at 20°C before dissection in M9 buffer. For imaging, one-cell embryos were mounted on 2% agar pads, thereby slightly compressed to increase the cortical surface visible in a confocal plane. Images were acquired with spinning disk confocal microscope (Zeiss C-Apochromat, 63X/1.2 NA or 100X/1.42 NA, Yokogawa CSU-X1 scan head and Hamamatsu Orca-Flash4.0 camera) every 2 s on two or three different planes (one or two at the bottom for a cortical section, and one 12 µm above for a medial section of the embryo) . For 3D acquisitions, Z-stacks were acquired every 0.2 μm. We assume the shape to be rotationally symmetrical to the longer axis, thus the outline of one medial section of the embryo reflects faithfully cell shape changes and ingression distance.

### Gene silencing by RNA interference

RNAi experiments were performed by feeding (Timmons et al., 2001). L4 worms were grown at 20°C on feeding plate (NGM agar containing 1 mM isopropyl-β-D-thiogalactoside and 50 μg ml−1 ampicillin) for the required number of hours before imaging.

### Correlation

Spatiotemporal correlation functions were calculated for all time points during the stationary period, in the 30 μm central region of the embryo. The plot of the spatial correlation only (1D correlation function) is shown in Figure 2c between the compression, alignment and ingression data sets. Peak value positions are obtained by a Gaussian fitting procedure and allow the calculation of positional differences between the different data sets. Because the flow field appears stationary, we expect this distance between peaks of compression, alignment and ingression to arise due to temporal delays between these events in the reference frame co-moving with the cortical flows. We thus translated the characteristic distances between stationary peaks to temporal delays using the average flow velocity in the −10 μm to 0 central region (6.16 ± 1.23 µm/min for pseudocleavage and 4.01 ± 1.92 µm/min for cytokinesis) (Figure 2d).

![Figure 5.](https://cdn.elifesciences.org/articles/17807/elife-17807-fig5-v3.jpg)

**Figure 5.:** Schematic illustration of flows, cytoskeletal organization and cell shape changes during pseudocleavage and at the onset of cytokinesis.

![Video 5.](https://cdn.elifesciences.org/articles/17807/elife-17807-media5.mp4.jpg)

**Video 5.:** Cortical and medial planes of an embryo expressing both Lifeact::mKate2 and endogenous NMY-2::GFP. Left panel, medial plane Lifeact:mKate2, center, cortical NMY-2::GFP, right panel, cortical Lifeact:mKate2 (min:s).

![Video 6.](https://cdn.elifesciences.org/articles/17807/elife-17807-media6.mp4.jpg)

**Video 6.:** Cortical and medial planes of an embryo expressing both Lifeact::mKate2 and endogenous NMY-2::GFP. Left panel, medial plane Lifeact:mKate2, center, cortical NMY-2::GFP, right panel, cortical Lifeact:mKate2 (min:s).

![Video 7.](https://cdn.elifesciences.org/articles/17807/elife-17807-media7.mp4.jpg)

**Video 7.:** Cortical and medial planes of an embryo expressing both Lifeact::mKate2 and endogenous NMY-2::GFP. Left panel, medial plane Lifeact:mKate2, center, cortical NMY-2::GFP, right panel, cortical Lifeact:mKate2 (min:s).

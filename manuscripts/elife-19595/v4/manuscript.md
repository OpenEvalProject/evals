# Controlling contractile instabilities in the actomyosin cortex

## Authors

- Masatoshi Nishikawa<sup>1</sup> ([ORCID: 0000-0001-6502-7907](https://orcid.org/0000-0001-6502-7907))
- Sundar Ram Naganathan<sup>1</sup>
- Frank Jülicher<sup>2</sup> ([ORCID: 0000-0003-4731-9185](https://orcid.org/0000-0003-4731-9185))
- Stephan W Grill<sup>1</sup> ([ORCID: 0000-0002-2290-5826](https://orcid.org/0000-0002-2290-5826)) †

### Affiliations

1. Biotechnology Center Technical University Dresden Dresden Germany
2. Max Planck Institute for the Physics of Complex Systems Dresden Germany
3. Max Planck Institute of Molecular Cell Biology and Genetics Dresden Germany

† Corresponding author

## Abstract

The actomyosin cell cortex is an active contractile material for driving cell- and tissue morphogenesis. The cortex has a tendency to form a pattern of myosin foci, which is a signature of potentially unstable behavior. How a system that is prone to such instabilities can rveliably drive morphogenesis remains an outstanding question. Here, we report that in the Caenorhabditis elegans zygote, feedback between active RhoA and myosin induces a contractile instability in the cortex. We discover that an independent RhoA pacemaking oscillator controls this instability, generating a pulsatory pattern of myosin foci and preventing the collapse of cortical material into a few dynamic contracting regions. Our work reveals how contractile instabilities that are natural to occur in mechanically active media can be biochemically controlled to robustly drive morphogenetic events.

## Introduction

Alan Turing described in his seminal 1952 paper the ability of an initially homogeneous spatial system that contains diffusing and chemically interacting species to form a self-organized pattern (Turing, 1952). Turing’s original conjecture was that such processes contribute to the patterning of developing organisms. While many examples have been found that are compatible with this idea (Kondo and Asal, 1995; Müller et al., 2012; Sheth et al., 2012; Raspopovic et al., 2014), self-organized patterning in morphogenesis, however, is known to not only rely on biochemical regulation but also depend on cell-and tissue scale active mechanical processes (Turing, 1952; Howard et al., 2011). General physical mechanisms by which the interplay between regulatory and mechanical processes endows active biological materials to form self-organized spatiotemporal patterns have remained largely unexplored.

Actomyosin contractility (Bray and White, 1988; Salbreux et al., 2012) is an essential cellular mechanical process, responsible for driving many cell- and tissue scale morphogenetic events (Murrell et al., 2015; Levayer and Lecuit, 2012). The cortex consists to a large extent of actin filaments and myosin motor proteins, forming a thin layer underneath the cell membrane that can be thought of as a thin film of an active gel (Salbreux et al., 2012; Jülicher et al., 2007). Contractility by myosin motor proteins generates active tension in the gel, and gradients in active tension are known to generate cortical flows of this layer (Mayer et al., 2010). Cortical flow participates in forming the cytokinetic furrow (Bray and White, 1988; Benink et al., 2000; Yumura, 2001; Eggert et al., 2006), and drives polarization of the one-cell stage C. elegans embryo (Hird and White, 1993; Guo and Kemphues, 1996; Cheeks et al., 2004; Munro et al., 2004; Goehring et al., 2011). Highly contractile cortices, like the one driving polarization in C. elegans, tend to exhibit transient accumulations of myosin that form a pulsatile pattern. Pulsatile actomyosin patterns are ubiquitous in development (Munro et al., 2004; Martin et al., 2009; Solon et al., 2009; Rauzi et al., 2010; Roh-Johnson et al., 2012; Maître et al., 2015), and it has been suggested that they result from positive feedback and contractile instabilities (Kruse and Jülicher, 2000; Bois et al., 2011; Gowrishankar et al., 2012; Kumar et al., 2014; Munjal et al., 2015; Hannezo et al., 2015). A contractile instability causes the cortex to become inhomogeneous over space, with cortical material collapsing into contracting regions (Bois et al., 2011; Alvarado et al., 2013). Theoretical work has shown that contractile instabilities are inevitable when contractility is high enough (Bois et al., 2011), raising the question of how a system that is prone to such instabilities can reliably drive morphogenesis. Here we show that there indeed exists a contractile instability in the actomyosin cortical layer of the C. elegans zygote, and we discover that this instability is controlled by a RhoA oscillator.

## Results and discussion

In order to investigate spatiotemporal patterns in the C. elegans cortex, we first sought to see whether non-muscle myosin II (NMY-2) in the C. elegans zygote displays pulsatile dynamics (Munro et al., 2004). For this, we determined the temporal derivative of the average NMY-2 intensity (Figure 1A, averaging over a region in the posterior indicated by a white box), as a proxy of myosin foci assembly and disassembly behavior (Figure 1A–C). We also quantified the time-dependence of the average speed of cortical flow in this region as determined by Particle Image Velocimetry (PIV, see Appendix for detail) (Figure 1B,C). Notably, both quantities exhibited signs of oscillatory behavior (Figure 1C) and an auto-correlation analysis revealed periodic changes in both quantities with a time constant of approximately 30 s (Figure 1D,E). To conclude, the myosin foci pattern in the C. elegans zygote exhibits pulsatile, oscillatory dynamics.

![Figure 1.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig1-v4.jpg)

**Figure 1.:** (A) A representative image of NMY-2::GFP showing the NMY-2 foci pattern (magenta) in the C. elegans zygote. Anterior is to the left throughout, white box denotes region shown in B. (B) Myosin focus assembly and disassembly time-course from A in inverted contrast; dashed circle indicates a myosin focus. Arrows denote the velocity field determined by PIV; thick green line: velocity scale bar 0.4 $\mu⁢m/s$. (C) The temporal dynamics of NMY-2 fluorescence intensity time-rate change (magenta) and cortical flow speed (blue, obtained by PIV) for the region in (B), arrowheads indicate the time interval shown in (B). (D) Normalized autocorrelation of NMY-2 intensity change and flow speed timecourses in (C) and (E) respective oscillation periods. (F) NMY-2::RFP (magenta) and AHPH::GFP (green), a probe for active RhoA, co-localize at myosin foci. (G) COMBI analysis schematic. (H) Effective reaction terms of NMY-2 and active RhoA in the phase plane of normalized NMY-2 and active RhoA concentrations (N = 25 embryos). Arrows represent concentration changes, colors indicate the magnitude of change. Thin solid magenta (NMY-2) and green (RhoA) lines, numerically determined nullclines. Thick dashed lines, linearized nullclines (see Appendix). Scale bars; $5 \mum$.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig1-figsupp1-v4.jpg)

**Figure 1—figure supplement 1.:** (A) The temporal dynamics of AHPH (green) and NMY-2 (magenta) foci intensities (n = 16). (B) Normalized spatiotemporal cross-correlation function of AHPH and NMY2 intensities. For visualization purpose, only the contours of the cross-correlation values are plotted (n = 25 embryos). (C) A plot of the normalized cross-correlation peak value, obtained from (B) at different time offsets. Note that the peak value is highest at $\tau=0$, indicating that active RhoA and myosin tend to come together at foci at the same time. Note also that the graph is asymmetric, indicating distinct dynamics in the assembly and disassembly phase.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig1-figsupp2-v4.jpg)

**Figure 1—figure supplement 2.:** (A) Effective reaction terms of NMY-2 and active RhoA obtained by COMBI (man text Figure 1H). Arrows represent concentration changes, colors indicate the magnitude of change. Black lines indicate the integrated trajectories, the solid black line with arrows highlights a trajectory that states with high active RhoA and low myosin, and overshoots in its level of myosion prior reaching the fixpoint. (B) Trajectories (black lines) are obtained from linearized reaction kinetics shown in (C) and (D). (C,D) Linearization of (C) $R_{r}⁢(c_{r},c_{m})$ and (D) $R_{m}⁢(c_{r},c_{m})$.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig1-figsupp3-v4.jpg)

**Figure 1—figure supplement 3.:** (A) Effective reaction terms of active RhoA and actin in the phase plane of normalized active RhoA and LifeAct concentrations (N = 14 embryos). Arrows represent concentration changes, colors indicate the magnitude of change. Thin solid green (active RhoA) and blue (actin) lines, numerically determined nullclines. Thick dashed lines, linearized nullclines (see Appendix). (B) A plot of peak value of the normalized , spatiotemporal cross-correlation function between LifeAct and AHPH fluorescence. (C) A representative image of AHPH::GFP (green) and LifeAct::tagRFP-T (magenta) in the non-RNAi condition. Scale bar; $5⁢\mu⁢m$.

We next sought to understand where this oscillatory behavior comes from. One possibility is that positive feedback mediated by RhoA (RHO-1 in C. elegans) (Bement et al., 2015), a key activator of myosin (Jenkins et al., 2006; Motegi and Sugimoto, 2006; Schonegg and Hyman, 2006), plays a role in generating this pulsatile pattern (Munjal et al., 2015). We investigated the dynamics of active RhoA by use of a GFP fused anillin homology domain (AHPH) probe, to image the GTP-bound active form of RhoA (Tse et al., 2012). We find that active RhoA forms a dynamic, pulsatile pattern that is similar to that of myosin, with both active RhoA and myosin co-localizing in pulsatile foci (Figure 1F, Figure 1—figure supplement 1, and Video 1). We speculated that flow-based transport of an activator of myosin could give rise to positive feedback and a contractile instability (Bois et al., 2011), favouring the spontaneous formation of self-organized pulsatory patterns (Munjal et al., 2015). However, testing for this possibility requires knowledge of the kinetics of active RhoA mediated myosin recruitment coupled with a hydrodynamic description of active cortical mechanics, for evaluating if the full mechanochemically coupled system indeed is unstable.

![Video 1.](https://cdn.elifesciences.org/articles/19595/elife-19595-media1.mp4.jpg)

**Video 1.:** Time lapse movie shows the cortical plane of embryo that expresses both AHPH::GFP (green) and NMY-2::tagRFP-T (magenta) in non-RNAi condition. Scale bar, 5 $\mu⁢m$.

We set out to test if coupling RhoA mediated myosin recruitment to gel flow and advection results in an intrinsically unstable cortex (Figure 2A). To this end, we sought to determine the effective reaction kinetics of the regulatory interaction between active RhoA and myosin in vivo. We developed a method of measuring the kinetic diagram of active RhoA mediated myosin recruitment (CO-moving Mass Balance Imaging; COMBI): We investigated the mass balance of both species in the comoving frame of reference of the flowing cortex, under consideration of the effects of dilution/enrichment by divergent/convergent gel flow (Figure 1G) (Vallotton et al., 2004). In the frame of reference of the embryo, concentrations of myosin and active RhoA can change due to transport by flow (advective fluxes) or due to association/dissociation (chemical fluxes). The chemical fluxes Rr and Rm, where r denote active RhoA and m denotes myosin, correspond to reaction terms that capture turnover and biochemically regulated recruitment effects. They can depend on the concentrations of both species.

![Figure 2.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig2-v4.jpg)

**Figure 2.:** (A) Schematic of the full mechanochemical patterning system. (B) Stability diagram of the homogeneous state in the plane of hydrodynamic length $\lambda$ and active tension measure $\sigma¯$ (see Appendix). The homogeneous state is unstable within the red region. Blue dot represents the parameter values of the non-RNAi C. elegans cortex; error bars denote 95% confidence intervals. (C) Stability diagram for a partial model without NMY-2 recruitment by RhoA; inset: corresponding schematic. The homogeneous state is unstable within the blue region. (D) Dispersion relations of the full mechanochemical patterning system with (red) and without (blue) RhoA mediated NMY-2 recruitment. Lighter shared areas represent 95% confidence intervals. (E) let-502 RNAi suppresses RhoA mediated recruitment of NMY-2. (F) COMBI diagram for let-502 RNAi (30 hr), N = 12 embryos. Thin solid magenta (NMY-2) and green (RhoA) lines; numerically determined nullclines. Thick solid dashed lines, linearized nullclines. Light dashed lines, linearized nullclines for the non-RNAi condition (Figure 1H) for comparison. (G) Dispersion relation for let-502 RNAi, lighter blue area indicates the 95% confidence interval. (H) NMY-2 distribution under let-502 RNAi. Scale bar; $5 \mum$.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig2-figsupp1-v4.jpg)

**Figure 2—figure supplement 1.:** Dispersion relations for measured diffusion coefficients (blue) and for a ten-fold increase (red) and a ten-fold decrease (green).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig2-figsupp2-v4.jpg)

**Figure 2—figure supplement 2.:** Stability of the homogeneous state with a linear form of $f⁢(c_{m})=c_{m}$.(A) Stability diagram of the homogeneous state in the plane of hydrodynamic length $\lambda$ and active tension measure $\sigma¯$. The homogeneous state is unstable for the full system within the red region, and unstable for the partial system without myosin recruitment by active RhoA within the blue region. (B) Corresponding dispersion relations, shaded regions indicate 95% confidence.

COMBI determines the average changes of per area myosin concentration ($c_{m}$) and of active RhoA concentration ($c_{r})$ due to turnover/regulation and as a function of the concentrations of both species. This provides us with information of the reaction kinetics of RhoA $(R_{r}⁢(c_{r},c_{m}))$ and myosin $(R_{m}⁢(c_{r},c_{m}))$ in the myosin and active RhoA concentration phase space (Figure 1G). We determined $c_{m}$ and $c_{r}$ every 5 s by spinning-disk confocal microscopy (Materials and methods). Advective fluxes account for the effects of dilution/enrichment by divergent/convergent gel flow, and these were determined by measuring the velocity field of cortical flow by particle image velocimetry (PIV), an image-based crosscorrelation analysis (Mayer et al., 2010; Raffel et al., 2007) that quantifies the movement of interrogation areas between two sequential timelapse images (Materials and methods). The spatial resolution of the velocity field is determined by the spacing of the interrogation areas which we choose as $1.26 \mum$. This is sufficiently smaller than the correlation length of cortical flow (the hydrodynamic length is ∼14 μm [Mayer et al., 2010; Saha et al., 2016]), hence, COMBI can provide information on actomyosin homeostasis by determining the average reaction kinetics on a timescale of seconds and a length scale of microns.

We visualize the reaction terms determined by COMBI in a vector field that illustrates the average evolution of concentrations of both species (Figure 1H). This reveals interesting features, for example a trajectory that starts with high active RhoA and low myosin levels will overshoot in its level of myosin prior to approaching the single stable fixed point (thick black line in Figure 1—figure supplement 2A). Key aspects of these dynamics can be captured by a nullcline analysis (Izhikevich, 2007). Reaction terms are zero on a nullcline ($R_{r}=0$ for active RhoA, Figure 1H, solid green line; and $R_{m}=0$ for myosin, Figure 1H, solid magenta line), which describes the concentration that a species would achieve when the concentration of the other species is fixed. This reveals that active RhoA recruits myosin (Figure 1H, solid magenta line) (Motegi and Sugimoto, 2006; Schonegg and Hyman, 2006) while RhoA activation kinetics is essentially independent of myosin levels (Figure 1H, solid green line). The full kinetic landscape can be linearized over its entire range (Figure 1H, dashed lines; Figure 1—figure supplement 2B–D), capturing global aspects of RhoA-based myosin recruitment. To conclude, COMBI can provide insight into the cortical kinetics over a broad range of myosin and active RhoA concentrations.

Given our kinetic analysis, we next sought to test if the full mechanochemically coupled system is indeed unstable. We describe the actomyosin cortex as a thin film of an active gel (Simha and Ramaswamy, 2002; Kruse et al., 2004; Ahmadi et al., 2006; Salbreux et al., 2009), with active tension generation by myosin under control of RhoA (Figure 2A; see Appendix for details). We measured the relevant material parameters of the gel in vivo directly from laser ablation experiments (hydrodynamic length: $\lambda=14.3 \mum$, and a conversion factor from NMY-2 intensity to active tension, $ζ^{′}=24.9 \mum^{2}/s$)(Saha et al., 2016). This allowed us to perform a linear stability analysis of the homogeneous state for the full model of the mechanochemical patterning system, with the above determined and linearized reaction kinetics between active RhoA and NMY-2 (Figure 1H). Figure 2B shows the corresponding stability diagram as a function of both the hydrodynamic length of the cortex $\lambda$ and the active tension measure $\sigma¯$ (see Appendix for detail). Notably, the homogeneous state, in which all concentrations are constant in space, always becomes unstable above a critical value of the active tension. Furthermore, we find that the parameter values of the C. elegans cortex are such that the system is close to the transition line between stable and unstable, but placed within the unstable regime (Figure 2B). Hence, our analysis is consistent with the actomyosin cortex in C. elegans being unstable and poised to form a spatial pattern.

Our theory predicts that the contractile instability depends on the strength of positive feedback, and thus the amount of recruitment of myosin by active RhoA (Figure 2C,D). Hence, we asked if suppression of RhoA mediated recruitment of myosin in the C. elegans zygote prevents the instability and results in a homogeneous NMY-2 distribution. LET-502 is the Rho-associated protein kinase that phosphorylates the regulatory myosin light chain, MLC-4, to activate NMY-2 (Piekny and Mains, 2002). Hence, reducing the concentration of LET-502 by RNAi should suppress RhoA mediated recruitment of myosin to the cortex. Indeed, COMBI analysis of let-502 RNAi embryos (30 hr) revealed that RhoA mediated recruitment of NMY-2 to the cortex is reduced, since the myosin nullcline displays a significantly decreased slope as compared to the non-RNAi condition (Figure 2E,F; see Table 1). Using the non-RNAi values of λ and ζ′ and the linearized reaction kinetics between active RhoA and NMY-2 measured by COMBI in let-502 RNAi (dark dashed lines in Figure 2F), we find that the cortex is predicted to be stable because all eigenvalues are negative (Figure 2G, compare to D; see Appendix for detail). Consistent with this prediction, we observed that let-502 RNAi embryos display a homogeneous NMY-2 distribution without pulsatory myosin foci (Figure 2H, compare to Figure 1A; Video 2). We conclude that, consistent with COMBI and theory, the actomyosin cortex can be brought into a stable regime by reducing positive feedback via suppressing myosin recruitment by active RhoA.

**Table 1.**
 Parameter values.


<table>
  <thead>
    <tr>
      <th>Parameters*,†</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Determined in this study</td>
    </tr>
    <tr>
      <td></td>
      <td>Kinetic parameter for non RNAi</td>
    </tr>
    <tr>
      <td>3.96±0.21⁢[10-2/s]</td>
      <td>konr</td>
    </tr>
    <tr>
      <td>4.54±0.244⁢[10-2/s]</td>
      <td>koffr</td>
    </tr>
    <tr>
      <td>0.0576±0.0934⁢[10-2/s]</td>
      <td>konmr</td>
    </tr>
    <tr>
      <td>0.126±0.389⁢[10-2/s]</td>
      <td>konm</td>
    </tr>
    <tr>
      <td>9.94±0.435⁢[10-2/s]</td>
      <td>konrm</td>
    </tr>
    <tr>
      <td>10.1±0.269⁢[10-2/s]</td>
      <td>koffm</td>
    </tr>
    <tr>
      <td></td>
      <td>Kinetic parameter for let-502 RNAi</td>
    </tr>
    <tr>
      <td>2.87±0.105⁢[10-2/s]</td>
      <td>konr</td>
    </tr>
    <tr>
      <td>4.39±0.0979⁢[10-2/s]</td>
      <td>koffr</td>
    </tr>
    <tr>
      <td>0.178±0.178⁢[10-2/s]</td>
      <td>konmr</td>
    </tr>
    <tr>
      <td>3.56±0.165⁢[10-2/s]</td>
      <td>konm</td>
    </tr>
    <tr>
      <td>1.81±0.0938⁢[10-2/s]</td>
      <td>konrm</td>
    </tr>
    <tr>
      <td>7.49±0.106⁢[10-2/s]</td>
      <td>koffm</td>
    </tr>
    <tr>
      <td>0.01⁢[μ⁢m2/s]</td>
      <td>Dr,Dm</td>
    </tr>
    <tr>
      <td></td>
      <td>Determined in Saha et al.,</td>
    </tr>
    <tr>
      <td>14.3±2.94⁢[μ⁢m]</td>
      <td>λ</td>
    </tr>
    <tr>
      <td>24.8±8.62⁢[μ⁢m2/s]</td>
      <td>ζ/γ</td>
    </tr>
    <tr>
      <td></td>
      <td>Parameter values for complex Swift-Hohenberg equation</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>a</td>
    </tr>
    <tr>
      <td>0.0000490</td>
      <td>b</td>
    </tr>
    <tr>
      <td>1.00+0.2⁢i</td>
      <td>d1</td>
    </tr>
    <tr>
      <td>0.0297+0.00400⁢i</td>
      <td>d2</td>
    </tr>
    <tr>
      <td>0.4</td>
      <td>f0</td>
    </tr>
    <tr>
      <td>0.00247</td>
      <td>f1</td>
    </tr>
    <tr>
      <td>10.1</td>
      <td>q0</td>
    </tr>
  </tbody>
</table>

_*Parameter values are shown with 95 % confidence intervals.†Active RhoA and NMY-2 densities are normalized by their average concentrations, and reported in dimensionless units of fluorescence intensities per unit area of 1⁢[pixel]2, corresponding to 0.0110⁢μ⁢m2._

![Video 2.](https://cdn.elifesciences.org/articles/19595/elife-19595-media2.mp4.jpg)

**Video 2.:** Time lapse movies show the cortical planes of the embryo that expresses NMY-2::tagRFP-T in let-502 RNAi embryo (upper) and in non-RNAi embryo (lower). Scale bar, 5 $\mu⁢m$.

We next asked if the patterns that are formed in the unstable regime in our theory correspond to the pattern of myosin foci observed in the embryo. Earlier work that considers a cortical gel with a diffusible activator of myosin (Bois et al., 2011; Kumar et al., 2014) suggests that a contractile instability results in a myosin foci pattern with a spacing that is determined by the hydrodynamic length λ. Indeed, a numerical solution of the full mechanochemical patterning system (Figure 2A) reveals the formation of a few dynamic contracting regions which travel and are spaced about 2⁢λ apart (Figure 3—figure supplement 1, Video 3). These traveling peaks have rapid flows converging upon them (peak flow speed: 0.7 μm/s), and they persist and are not pulsatile. This pattern is different from the myosin foci pattern observed in the C. elegans zygote, which is pulsatile and exhibits a shorter spacing between foci (∼5 μm, compare to λ=14.3 μm; see Figure 3—figure supplement 1) (Munro et al., 2004; Mayer et al., 2010). This suggests that our model is missing an essential feature, which is responsible for determining the myosin pattern beyond the contractile instability.

![Video 3.](https://cdn.elifesciences.org/articles/19595/elife-19595-media3.mp4.jpg)

**Video 3.:** Time evolution of the myosin pattern, obtained by the numerical integration of the mechanochemical patterning system without an active RhoA pacemaking oscillator.

To identify the element missing in our model, we note that our theory predicts that reducing myosin recruitment by let-502 RNAi should cause both myosin and RhoA to be homogeneous and non-pulsatile (all eigenvalues are negative, see Figure 2G). However, imaging active RhoA under let-502 RNAi revealed that while the pulsatile myosin pattern is lost, the pulsatile active RhoA pattern is still present (Figure 3A,C; Video 4). Similarly, we find that 16 hr of RNAi of nmy-2 led to an almost complete loss of cortical myosin with, however, active RhoA still forming pulsatile foci (Figure 3B,D; Video 5). We conclude that, in contrast to the scenario in Drosophila germband extension (Munjal et al., 2015), active RhoA in C. elegans exhibits pulsatile foci dynamics independently of NMY-2 function. Importantly, both the characteristic spacing of the myosin-independent active RhoA pattern and its characteristic timescale were similar between nmy-2 RNAi, let-502 RNAi, and the non-RNAi condition (Figure 3E,F). Given that active RhoA in the wild-type acts to recruit myosin (Figure 1H), this raises the possibility that the myosin-independent dynamic active RhoA pattern is responsible for setting the myosin spatiotemporal pattern beyond the contractile instability. We conclude that the dynamic active RhoA pattern is generated in a manner that is independent of the myosin foci pattern, possibly through an independent RhoA spatiotemporal oscillator.

Oscillatory activities of Rho GTPases have previously been observed (Hwang et al., 2005; Miller and Bement, 2009; Das et al., 2012; Antoine-Bertrand et al., 2016). We next asked if this spatiotemporal oscillator requires ect-2, a RhoGEF, responsible in the early morphogenesis (Motegi and Sugimoto, 2006; Schonegg and Hyman, 2006). Indeed, RNAi of ect-2 leads to a complete absence of RhoA pulsation (Video 6). Furthermore, it is interesting to speculate if the myosin-independent active RhoA oscillator that we identify here is related to the RhoA/actin-based excitable oscillatory system reported previously (Bement et al., 2015; Westendorf et al., 2013). To test if the underlying mechanism to generate myosin-independent active RhoA oscillator is shared between C. elegans single-cell embryo and Xenopus embryo, we used COMBI to investigate the effective kinetic regulation between active RhoA and actin. We used LifeAct tagRFP-T as a probe for filamentous actin in the cortex (Riedl et al., 2008; Reymann et al., 2016). We determined the kinetic diagram in the active RhoA and actin concentration phase plane, to quantitatively evaluate the rate constants in the effective kinetic equations (Figure 1—figure supplement 3A). We find that the active RhoA nullcline is nearly vertical and inconsistent with actin behaving as a negative regulator of RhoA. Note that this does not exclude the general possibility of negative feedback between actin and RhoA (Robin et al., 2016), but suggests that the C. elegans cortex is normally operating in a regime where no such negative feedback is accessed. While the detailed mechanism as well as the kinetic interactions that underlie RhoA pulsation in C. elegans remain to be determined, the RhoGEF ect-2 is involved and the system appears to undergo spatiotemporal oscillations in the absence of negative feedback between actin and RhoA.

![Figure 3.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig3-v4.jpg)

**Figure 3.:** (A,B) AHPH::GFP (green) and NMY-2::RFP (magenta) in (A) a representative let-502 RNAi and (B) a representative nmy-2 RNAi embryo. (C,D) Normalized AHPH::GFP intensity change autocorrelation (C) for (A) and (D) for B, obtained within the posterior. (E,F) Characteristic (E) spacing of AHPH patterns and (F) period of AHPH intensity change in non-RNAi, nmy-2 RNAi, and let-502 RNAi embryos. Scale bars, $5 \mum$.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig3-figsupp1-v4.jpg)

**Figure 3—figure supplement 1.:** Myosin forms traveling peaks that are spaced approximately $2⁢\lambda$ apart.Space time plot of the myosin distribution obtained by numerical integration the full mechanochemical system (no active RhoA pacemaer). The system forms a single traveling peak with rapid flows impinging upon it.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig3-figsupp2-v4.jpg)

**Figure 3—figure supplement 2.:** (A,B) A representative example of a preprocessed GFP-AHPH image by (A) background subtraction and (B) contrast enhancement (contrast limited adaptive histogram equalization method, Matlab) prior to computing the spatial autocorrelation function of the intensity. Scale bar, 5 $\mu⁢m$. (C) Corresponding spatial autocorrelation function. (D) Corresponding radially averaged correlation function. The position of the first peak at $∼4⁢\mu⁢m$ indicates the characteristic spacing of AHPH foci in this embryo.

![Video 4.](https://cdn.elifesciences.org/articles/19595/elife-19595-media4.mp4.jpg)

**Video 4.:** Time lapse movie shows the cortical plane of the embryo that expresses both AHPH::GFP (green) and NMY-2::tagRFP-T (magenta) in let-502 RNAi embryo. Scale bar, 5 $\mu⁢m$.

![Video 5.](https://cdn.elifesciences.org/articles/19595/elife-19595-media5.mp4.jpg)

**Video 5.:** Time lapse movie shows the cortical plane of the embryo that expresses both AHPH::GFP (green) and NMY-2::tagRFP-T (magenta) in nmy-2 RNAi embryo. Scale bar, 5 $\mu⁢m$.

![Video 6.](https://cdn.elifesciences.org/articles/19595/elife-19595-media6.mp4.jpg)

**Video 6.:** Time lapse movies show the cortical planes of the embryos that expresses AHPH::GFP (green) in nmy-2 RNAi embryo (upper), and in ect-2 RNAi embryo (lower). Scale bar, 5 $\mu⁢m$.

We next sought to test in our theory if it is possible that an active RhoA spatiotemporal oscillator sets the myosin pattern beyond the contractile instability (Figure 4A, left). To this end, we described the dynamical behavior of an active RhoA pacemaker by use of a generic model of spatiotemporal oscillating patterns, the complex Swift-Hohenberg Equation (Figure 4—figure supplement 1A) (Sakaguchi, 1997). Importantly, coupling in our model this generic spatiotemporal oscillator (30⁢s characteristic timescale, 5 μm characteristic length scale, Figure 3E,F; see Appendix for detail) to the full mechanochemical patterning system does not destroy the active RhoA spatiotemporal oscillator pattern. Instead our model predicts that the myosin pattern (which in the absence of the generic oscillator formed a single traveling peak, see Figure 3—figure supplement 1) now follows that of the active RhoA spatiotemporal oscillator (Figure 4B left). Hence, the active RhoA oscillator can determine the myosin pattern in the unstable regime (Video 7). As a consequence, controlling the myosin pattern also results in reduced cortical flow speeds (peak flow speed: 0.17 μm/s) as compared to the case where the RhoA oscillator is absent (0.7 μm/s, see above). However, we find that the ability of the RhoA oscillator to control the myosin pattern critically depends on the level of mechanochemical feedback. We demonstrate this by reducing the hydrodynamic length in our model, which increases overall flow speeds and advection, and thereby increases the mechanochemical feedback strength. We find in our model that this change destroys the pattern of the active RhoA spatiotemporal oscillator. Both the myosin and active RhoA pattern no longer form a regular spatiotemporal oscillation (Figure 4—figure supplement 1, λ is reduced by 5 μm to 9 μm). Instead, the system displays a dynamical state that is characterized by an irregular spatiotemporal pattern of dynamic contracting regions that move rapidly (Figure 4B right; Figure 4—figure supplement 1; Video 8). In this state, the pattern of active RhoA now depends on myosin and flows and is essentially under control of the contractile instability. Finally, flow speeds are again increased and comparable to the case when the RhoA oscillator is absent (peak flow speed: 0.94 μm/s). In conclusion, theory indicates that the active RhoA oscillator can act as a pacemaker for the system, to control the contractile instability and to prevent the formation of large and irregularly moving contracting regions of myosin.

![Figure 4.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig4-v4.jpg)

**Figure 4.:** (A) Schematic of a mechanochemical patterning system under control of a RhoA pacemaker, with (left) normal conditions and (right) with increased mechanochemical feedback and with faster flows. (B) Numerically obtained space time plots of the myosin distribution, for normal conditions ($\lambda=14.3 \mum$; left) and for a weakened cortex with increased mechanochemical feedback ($\lambda=9 \mum$; right); see Appendix. (C) Kymographs of NMY-2 intensity under normal conditions (spd-5 RNAi; left) and under conditions of a weakened cortex (pfn-1 RNAi; right) obtained in mid-plane images and from the yellow region illustrated in the inset image on the right. (D,E) Representative cortical plane images of (D) NMY-2::tagRFP-T and (E) RhoA::GFP, dotted circles indicate foci. (F) Average cortical flow speed as a function of direction under conditions of a normal cortex (dark blue: non-RNAi; light blue: spd-5 RNAi) as well as for a weakened cortex (red: pfn-1 RNAi). (G) Radially averaged velocity orientation correlation function (Materials and methods) for the same three conditions, note that the pfn-1 RNAi embryo cannot drive coherent flow over large distances. Scale bars, $5 \mum$.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/19595/elife-19595-fig4-figsupp1-v4.jpg)

**Figure 4—figure supplement 1.:** (A) Spatiotemporal plot of the active RhoA pacemaker in the absence of myosin and cortical flow, by utilizing a generic spatiotemporal oscillator for active RhoA dynamics (the complex Swift-Hohenberg equation, see Appendix). (B) Spatiotemporal plot of this active RhoA pacemaker coupled of the full mechanochemical system with $\lambda=14.3 \mum$, describing the normal state the cortex (non-RNAi or spd-5 RNAi). Left (green) shows the active RhoA pattern; right (magenta) shows myosin. Compared to (A), the full mechanochemical system displays a slightly longer time-scale, and the active RhoA foci appear slighlty more ’condensed’. Note also that in our experiments, active RhoA foci appear more condensed when myosin is active (main text Figure 4E, left) as compared to when myosin function is reduced or when myosin is absent (main text Figure 3A,B). (C) Spatiotemporal plot of the active RhoA pacemaker coupled of the full mechanochemical system with reduced mechanochemical feedback and $\lambda=9 \mum$, mimicking pfn-1 RNAi. Now the dynamical pattern is characterized by irregular movements.

![Video 7.](https://cdn.elifesciences.org/articles/19595/elife-19595-media7.mp4.jpg)

**Video 7.:** Time evolution of the myosin pattern, obtained by the numerical integration of the mechanochemical patterning system, coupled with the active RhoA pacemaking oscillator.

![Video 8.](https://cdn.elifesciences.org/articles/19595/elife-19595-media8.mp4.jpg)

**Video 8.:** Time evolution of the myosin pattern, obtained by the numerical integration of the mechanochemical patterning system with the reduced hydrodynamic length by 5 $\mu⁢m$ to 9 $\mu⁢m$, and coupled with the active RhoA pacemaking oscillator.

We next sought to seek experimental evidence that the myosin pattern in the C. elegans zygote is under control of the RhoA pacemaker. To this end, we tested if increasing the level of mechanical feedback in C. elegans destroys the pattern of the active RhoA spatiotemporal oscillator as predicted from theory. For this we recorded space-time patterns of myosin in a midplane section under conditions of spd-5 RNAi. SPD-5 is a centriole constituent that is essential for centriole maturation (Hamill et al., 2002), and its RNAi leads to a delay of polarizing flows which gives us more time for an analysis of the pulsatory dynamics. To increase mechanochemical feedback we recorded space-time patterns of myosin under RNAi of the actin nucleator pfn-1 (Severson et al., 2002) for which the cortex is weakened and flow speeds are increased by a factor of three to five (Figure 4F) and for which the hydrodynamic length is decreased by 5 μm to 9 μm (Severson et al., 2002; Naganathan, unpublished). For spd-5 RNAi, we observed the ’normal’ pulsating pattern of myosin foci (Figure 4C left; Video 9 and Video 10). In contrast, for pfn-1 RNAi we observed large contracting regions of myosin that rapidly move in an irregular fashion (Figure 4C right, D right; Videos 9 and 11). Importantly, in pfn-1 RNAi active RhoA assembles in large and irregularly moving foci structures (Figure 4E right, compare to Figure 4E left and Figure 3A,C; Video 11). This suggests that the normal pattern of the active RhoA spatiotemporal oscillator is destroyed, and the distribution of active RhoA is now governed by the irregular dynamics of myosin. Note that pfn-1 RNAi does not destroy the general ability of RhoA to generate a pulsating pacemaker pattern, as revealed by double RNAi of pfn-1 and nmy-2 (Video 12). We conclude that reducing the hydrodynamic length increases mechanochemical feedback and advection. This causes the RhoA pacemaker to lose the ability to control the contractile instability. Consistent with the predictions of our theory, this destroys the RhoA pacemaker pattern and causes the system to undergo a transition to irregular behavior with large and rapidly moving contracting regions (Figure 4C–E). Interestingly, the uncontrolled gel is no longer capable to drive coherent flows of the cortex over large distances (Figure 4G), and the embryo fails to polarize (Severson et al., 2002). Taken together, our quantitative analysis is consistent with the interpretation that the spatiotemporal RhoA oscillator acts as a pacemaker in C. elegans, controlling the contractile instability of the actomyosin cortex.

![Video 9.](https://cdn.elifesciences.org/articles/19595/elife-19595-media9.mp4.jpg)

**Video 9.:** Time lapse movies show the midplane sections of the embryos that express NMY-2::GFP (magenta) in spd-5 RNAi embryo (upper) and pfn-1 RNAi embryo (lower). Scale bar, 5 $\mu⁢m$.

![Video 10.](https://cdn.elifesciences.org/articles/19595/elife-19595-media10.mp4.jpg)

**Video 10.:** Time lapse movies show the cortical planes of the embryo that expresses both AHPH::GFP (green) and NMY-2::tagRFP-T (magenta) in spd-5 RNAi embryo. Scale bar, 5 $\mu⁢m$.

![Video 11.](https://cdn.elifesciences.org/articles/19595/elife-19595-media11.mp4.jpg)

**Video 11.:** Time lapse movies show the cortical planes of the embryo that expresses both AHPH::GFP (green) and NMY-2::tagRFP-T (magenta) in pfn-1 RNAi embryo. Scale bar, 5 $\mu⁢m$.

![Video 12.](https://cdn.elifesciences.org/articles/19595/elife-19595-media12.mp4.jpg)

**Video 12.:** Time lapse movies show the cortical planes of the embryos that expresses AHPH::GFP (green) in nmy-2 RNAi embryo (upper), and in pfn-1;nmy-2 RNAi embryo (lower). Scale bar, 5 $\mu⁢m$.

We have here investigated the mechanisms of pattern formation in an active system that combines the contractile force generation and flow with regulation and advection. For this, we introduced the COMBI method to directly infer reaction kinetics without relying for example on photobleaching (Sprague et al., 2004). We determined the effective reaction kinetics of myosin and active RhoA in the actomyosin cortex with COMBI. This allowed us to build a quantitative model of mechanochemical patterning in the actomyosin layer. By use of linear stability analysis, we found that the actomyosin cortex is unstable and spontaneously forms a self-organized pattern. We speculate that during embryogenesis cells need high cortical contractility to drive morphological changes. This can lead them near or beyond contractile instabilities, leading to dynamics characterized by strong fluctuations and irregular behavior, possibly exhibiting active turbulence (Giomi, 2015). We suggest that such instabilities are inevitable in dynamic systems that are highly contractile. We discovered a spatiotemporal RhoA oscillator that determines the myosin pattern even beyond the contractile instability, thereby controlling the contractile instability. The independent biochemical RhoA oscillator endows the cell with the ability to use an intrinsically unstable active contractile medium for driving morphogenetic processes such as polarization. To conclude, our work paves the way for understanding pattern formation in active biological materials that utilize potentially unstable contractile processes.

## Materials and methods

### Worm strains, maintenance, and sample preparation

The following transgenic lines were used in this study: SWG003 (nmy-2(cp8[NMY-2::GFP + unc-119(+)]) I; unc-119(ed3) III; gesIs002[unc- 119(ed3) III; (pie-1::Lifeact ::tagRFP-T::pie-1 + unc-119(+))]) for imaging of GFP labelled NMY-2 (the images shown in Figure 1A and B and in Figure 4C). SWG012 (nmy-2(cp8[NMY-2::tagRFP-T + unc-119(+)]) I; unc-119(ed3) III; gesIs002[unc- 119(ed3) III; mgSi5[cb-UNC-119 (+) GFP::ANI-1(AH+PH)]II) for imaging of tagRFP-T labelled NMY-2 and GFP labelled AHPH for a probe of active RhoA in the cortex (the images shown in Figure 1F, in Figure 2H, and in Figure 3A and B).

Worm strains were maintained at 20°C, and shifted to 24°C for 24 hr before imaging. Embryos were dissected in M9 buffer and mounted onto agar pads (2% agarose in water) to squish the embryos gently. All experiments were performed at 23–24°C. RNA interference experiments were performed by feeding as described in Naganathan et al. (2014). Feeding times for RNAi experiments were 16–18 hr for nmy-2, 23–25 hr for spd-5, 19–21 hr for pfn-1, 19–21 hr for pfn-1;nmy-2 double knockdown and 29–31 hr for let-502. Feeding clones were obtained from the Hyman lab (MPI-CBG, Dresden, Germany).

### Imaging

One-cell stage embryos were observed under the inverted fluorescence microscope (Axio Observer Z1, Zeiss) using a Zeiss C-Apochromat 63$\times$ water immersion lens, equipped with a spinning disc confocal unit (Yokogawa, CSU-X1) and AOTF laser combiner (Andor, ALC). Fluorescence images were acquired by a sCMOS camera (Hamamatsu, ORCA flash 4.0) at 5 s time intervals for non-RNAi, let-502 RNAi, nmy-2 RNAi, and pfn-1;nmy-2 RNAi embryos. For pfn-1 RNAi embryos, images were taken every 3 s. Pixel size was 0.105 $\times$ 0.105 $\mu⁢m^{2}$, all devices were controlled through $\mu-$manager(Edelstein et al., 2014). Fluorescence images of GFP and tagRFT-T labeled proteins in the embryos were excited by 488 and 561 nm lasers, respectively.

### Image analysis

Prior to COMBI analysis, images were filtered using the nonlocal means method (Buades et al., 2005), reducing spatially uncorrelated noise while preserving finer structures. Filtering was performed by averaging fluorescence intensities on the basis of the similarity between the fluorescence intensity profile in the interrogation area and the intensity profile in the neighboring region, i.e., a searching window. We set the size of the interrogation area and the searching window, to be $5\times5$ pixels and $25\times25$ pixels, corresponding to 0.525 $\times$ 0.525 $\mu⁢m^{2}$ and 2.625 $\times$ 2.625 $\mu⁢m^{2}$, respectively. A filtering parameter, $h$, was set to be $0.1 s$ for NMY-2 images, $0.3 s$ for AHPH images, where $s$ denotes the standard deviation of the fluorescence intensity in each image. We performed the filtering using a freely available code from MATLAB central (Fast Non-Local Means 1D, 2D Color and 3D by Kroon). Note that it is important to remove spatially uncorrelated noise prior to the computation of the spatial derivatives, since differential value is affected by spatially uncorrelated noises.

To perform COMBI, we first determined the cortical flow velocity, $𝐯⁢(x,y)$, by Particle Image Velocimetry (PIV) using a freely available PIV algorithm, PIVlab 1.32 (available from http://pivlab.blogspot.de/). PIV was performed on NMY-2 images by setting the interrogation area as 24 pixels with a step of 12 pixels. Velocity vectors were then interpolated to single pixel resolution for determining $R_{r}$ and $R_{m}.$$∂_{t}C_{i}, C_{i}∇v$ and $𝐯⁢\nabla⁡C_{i}$ for both the background subtracted, active RhoA and myosin intensities (denoted by $C_{r}$ and $C_{m}$, respectively). Intensity background levels were obtained by averaging the intensity in the region outside the embryo. $R_{r}$ and $R_{m}$ were then determined for each pixel throughout the cortical plane, by the use of the mass balance equations given in Figure 1G. We obtained a kinetic diagram (Figure 1H) by averaging $R_{r}$ and $R_{m}$ in $10\times10 \mum^{2}$ boxes located in the anterior region. We determined average values for each embryo by averaging over the first 36 frames after the start of polarizing flow. For the non-RNAi case (Figure 1H), we report the average kinetic diagram from $N=25$ embryos, for let-502 RNAi (Figure 2F) we averaged over $N=12$ embryos. Note that the active RhoA and NMY-2 concentrations were normalized by the respective mean intensities of active RhoA and NMY-2 under non-RNAi conditions.

### Correlation analysis

To characterize the myosin intensity change, $Δ⁢I⁢(t)$ and the cortical flow speed $v_{r}⁢(t)$ in a box of size $10\times10 \mum^{2}$ in the posterior region, we determined the spatial average over the box. We then computed the autocorrelation function

$$
C_{t}(\tau)=\frac{⟨[f(t)^{2}−f¯][f(t+\tau)^{2}−f¯]⟩_{t}}{\sigma_{f}^{2}},
$$

where $f⁢(t)=Δ⁢I⁢(t)$ or $v_{r}⁢(t)$, $\sigma_{f}$ denote the standard deviation of $f⁢(t)$, and $f¯$ denotes the mean of $f⁢(t)$, averaged over time $t$, where $⟨⟩_{t}$ represents an average over time. $C_{t}$ is mean-subtracted and normalized by the variance of $f⁢(t)$. The period of oscillation was determined by the peak position in the autocorrelation function. For a precise detection of oscillatory behavior, we removed from our analysis embryos in which the second peak in the autocorrelation function of the time course was undetectable (12 out of 25 cases for non-RNAi embryos, 5 out of 12 cases in let-502 embryos, 4 out of 12 embryos for nmy-2 RNAi embryos, respectively).

We obtained the characteristic length of the spatial pattern of myosin and RhoA by detecting the location of the first peak in the radial spatial intensity correlation function. The spatial intensity autocorrelation function of intensity, $f⁢(x,y,t)$, was obtained by

$$
C_{sp}(ξ,η,t)=\frac{⟨[f(x,y,t)^{2}−f¯(t)][f(x+ξ,y+η,t)^{2}−f¯]⟩_{x,y}}{\sigma_{f}^{2}},
$$

where $f¯⁢(t)$ denotes the spatial average of $f⁢(x,y,t)$, see Figure 3—figure supplement 2C. This function was radially averaged, and the first peak was detected (Figure 3—figure supplement 2D) in each time point. The radii of first peak were then averaged over time in each embryo. For the determination of the spacing in AHPH foci, the contrast of the fluorescence images was enhanced using the Contrast Limited Adaptive Histogram Equalization method using Matlab (Mathworks)(see Figure 3—figure supplement 2).

To characterize the spatial coherence of the velocity field, we evaluated the spatial correlation of the normalized velocity vectors, $n(x,y,t)=v(x,y,t)/||v(x,y,t)||$. The spatial correlation function was computed by,

$$
C_{ori}(ξ,η)=⟨n(x,y,t)⋅n(x+ξ,y+η,t)⟩_{x,y,t},
$$

where $⋅$ represents scalar product, and $⟨⟩_{x,y}$ denotes the spatial average. Note that the coordinate transformation from Cartesian to polar coordinates of the orientation vectors, $𝐧⁢(x,y,t)$, provides a simpler representation of $C_{ori}⁢(ξ,η)$ as,

$$
C_{ori}(ξ,η)=⟨cos⁡[\theta(x,y,t)−\theta(x+ξ,y+η,t)]⟩,
$$

where $\theta⁢(x,y,t)$ denotes the anti-clockwise angle from x-axis of $𝐧⁢(x,y,t)$. The above expression shows that the $C_{ori}⁢(ξ,η)$ provides spatial correlation of the cosine similarity between $\theta⁢(x,y,t)$ and $\theta⁢(x+ξ,y+η,t)$. Therefore, the characteristic length of the decay of $C_{ori}⁢(ξ,η)$ represents the loss of correlation between the directions of velocity vectors, $(ξ,η)$ away. Larger characteristic length of the decay demonstrates the large-scale flow of the cortex.

For visualizing purpose, we transformed the coordinate system from $(ξ,η)$ to polar $(r,ϕ)$ and then determined the average over the angle, $ϕ$, to plot $C_{ori}$ as a function of the radius, $r$, e.g. Figure 4G.

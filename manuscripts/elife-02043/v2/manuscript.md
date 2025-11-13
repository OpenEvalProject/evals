# Systems analysis of the CO2 concentrating mechanism in cyanobacteria

## Authors

- Niall M Mangan<sup>1</sup> †
- Michael P Brenner<sup>1</sup> †

### Affiliations

1. School of Engineering and Applied Sciences and Kavli Institute for Bionano Science and Technology Harvard University Cambridge United States

† Corresponding author

## Abstract

Cyanobacteria are photosynthetic bacteria with a unique CO2 concentrating mechanism (CCM), enhancing carbon fixation. Understanding the CCM requires a systems level perspective of how molecular components work together to enhance CO2 fixation. We present a mathematical model of the cyanobacterial CCM, giving the parameter regime (expression levels, catalytic rates, permeability of carboxysome shell) for efficient carbon fixation. Efficiency requires saturating the RuBisCO reaction, staying below saturation for carbonic anhydrase, and avoiding wasteful oxygenation reactions. We find selectivity at the carboxysome shell is not necessary; there is an optimal non-specific carboxysome shell permeability. We compare the efficacy of facilitated CO2 uptake, CO2 scavenging, and HCO3− transport with varying external pH. At the optimal carboxysome permeability, contributions from CO2 scavenging at the cell membrane are small. We examine the cumulative benefits of CCM spatial organization strategies: enzyme co-localization and compartmentalization.

## Introduction

Intracellular compartments are critical for directing and protecting biochemical reactions. One of the simplest and most striking known examples of compartmentalization are the carboxysomes (Cannon et al., 2001; Yeates et al., 2008) of cyanobacteria and other autotrophic proteobacteria (Savage et al., 2010; Rosgaard et al., 2012). These small, 100–200 nm compartments separate the principal reaction of the Calvin cycle, the RuBisCO catalyzed fixation of carbon dioxide (CO2) into 3-phosphoglycerate, from the rest of the cell (Cannon et al., 1991). CO2 and oxygen (O2) competitively bind as substrates of RuBisCO, and the reaction with O2 produces phosphoglycolate, a waste product which must be recycled by the cell (Jordan & Ogren, 1981; Tcherkez et al., 2006; Savir et al., 2010). To maximize carboxylation and minimize oxygenation, the carboxysome is believed to act as a diffusion barrier to CO2 (Reinhold et al., 1989; Dou et al., 2008). There is much interest in the design and function of such compartments and whether they can be used to enhance carbon fixation in other organisms such as plants or to improve reaction rates in other metabolic systems (Ducat & Silver, 2012; Agapakis et al., 2012; Papapostolou & Howorka, 2009; Frank et al., 2013). Increased efficiency of biochemical reactions will lead to better yield in bioengineered bacterial systems, creating new possibilities for production of high-value products such as biofuels. Enhancing carbon fixation in plants or other organisms could lead to increased carbon sequestration, or crop yield.

The concentrating mechanism in cyanobacteria relies on the interaction of a number of well characterized components, as shown in Figure 1, transferring inorganic carbon from outside the cell into cytosol and carboxysomes (Allen, 1984; Badger & Price, 2003; Kaplan & Reinhold, 1999; Price et al., 2007). Due to this mechanism, inorganic carbon concentration is elevated well above 200–300 μM, the CO2 concentration required for saturating the RuBisCO. Additionally a high CO2 concentration increases the ratio of CO2 to O2 so that carboxylation dominates over oxygenation. Concentrations of 20–40 mM inorganic carbon, up to 4000-fold higher than external levels, have been observed (Kaplan & Reinhold, 1999; Woodger et al., 2005; Sultemeyer et al., 1995; Price et al., 1998). The bilipid outer and cell membranes are highly permeable to small uncharged molecules such as CO2 (Missner et al., 2008; Gutknecht et al., 1977), so instead the cell primarily accumulates the charged and less membrane soluble bicarbonate (HCO3−) (Volokita et al., 1984; Price & Badger, 1989). Active transporters, both constitutive and inducible, bring HCO3− into the cell (Price et al., 2008, 2004; Omata et al., 1999), and mechanisms exist to actively convert CO2 to HCO3− at the thylakoid and cell membrane (Price et al., 2008; Maeda et al., 2002; Shibata et al., 2001). Once it passively diffuses into the carboxysome, HCO3− is rapidly brought into equilibrium with CO2 by the enzyme carbonic anhydrase, resulting in the production of CO2 near RuBisCO. Carbonic anhydrase is known to be localized on the interior side of the carboxysome shell (Yeates et al., 2008; Cannon et al., 1991; Cot et al., 2008; Long et al., 2008). The carboxysome shell must be permeable enough to allow HCO3− and 3-phosphoglycerate to readily diffuse in and out. The function of this system and its ability to concentrate inorganic carbon depends on the interplay between these various molecular components. Without a model, flux measurements cannot determine the components relative roles in enhancing the CO2 concentration in the carboxysome. To date, it has not been possible to directly measure the partitioning of the internal carbon concentration in the cytosol and carboxysomes. We wish to characterize the distribution of internal carbon. Visualizations of the location of the carboxysomes with fluorescent microscopy in Synechococcus elongatus PCC7942 demonstrated that the carboxysomes are evenly spaced along the centerline of the cell, (Savage et al., 2010), raising the question of how spatial organization, beyond simple partitioning, changes the efficacy of the system.

![Figure 1.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig1-v2.jpg)

**Figure 1.:** Outer and cell membranes (in black), as well as, thylakoid membranes where the light reactions take place (in green) are treated together. Carboxysomes are shown as four hexagons evenly spaced along the centerline of the cell. The model treats a spherically symmetric cell, with one carboxysome at the center. Active $HCO_{3}^{−}$ transport into the cell is indicated (in light blue), as well as active conversion from CO2 to $HCO_{3}^{−}$, sometimes called ‘facilitated uptake’ or ‘scavenging’, at membranes (in orange). Both CO2 and $HCO_{3}^{−}$ can leak in and out of the cell, with CO2 leaking out much more readily. Both species passively diffuse across the carboxysome shell. Carbonic anhydrase (red) and RuBisCO (blue) are contained in the carboxysomes and facilitate reactions as shown.

The goal of this study is to further develop a mathematical model of the CCM (Reinhold et al., 1989; Fridlyand et al., 1996; Reinhold et al., 1991) that uses recent experimental progress on the CCM to untangle the relative roles of the different molecular components, and predict the region of parameter space where efficient carbon fixation occurs. We are considering conditions where CO2 is limiting (15μM external inorganic carbon) and, for the moment, ignore other biological pressures. In this context, efficient carbon fixation requires two conditions: First, the CO2 concentration must be high enough that RuBisCO is saturated, and the competitive reaction with O2 is negligible. We emphasize that for the oxygenation reaction to be negligible the CO2 concentration should be higher than needed to merely saturate RuBisCO. Secondly, the carbonic anhydrase within the carboxysome must be unsaturated, so that extra energy isn't wasted transporting unused $HCO_{3}^{−}$ into the cell.

Examination of the system performance with varying expression levels of $HCO_{3}^{−}$ transporters, carboxysome permeability, and conversion from CO2 to $HCO_{3}^{−}$, reveals a parameter window where these conditions are simultaneously satisfied. We comment on the relation of this window to measured carbon pools, carbon fixation rates, and $HCO_{3}^{−}$ transporters. We find that the $HCO_{3}^{−}$ concentration in the cytosol is constant across the cell, set by the $HCO_{3}^{−}$ transport and leakage rates, and depends very little on the carboxysome permeability. The carboxysome permeability does, however, set how the CO2 is partitioned between the carboxysome and cytosol. At optimal carboxysome permeability, $HCO_{3}^{−}$ diffusion into the carboxysome is fast enough to supply inorganic carbon for fixation, but the rate of CO2 leakage out of the carboxysome is low. We explore the fluxes from CO2 facilitated uptake and scavenging with varying ratios of external CO2 and $HCO_{3}^{−}$. Finally we discuss the proportion the carbon concentration comes from different methods of spatial organization such as co-localization, encapsulation, and spatial location of carboxysomes. Concentration of carbonic anhydrase increases the maximum rate of reaction for carbonic anhydrase per volume, causing carbonic anhydrase to saturate at a higher level of $HCO_{3}^{−}$, and achieve an order of magnitude higher local CO2 concentrations. Encapsulation of the reactions in an optimally permeable carboxysome shell achieves another order of magnitude of CO2 concentration.

### Reaction diffusion model

We present our mathematical model, which captures all aspects of the CCM as described above. This model is an expansion of previously developed models (Reinhold et al., 1989; Fridlyand et al., 1996; Reinhold et al., 1991). Our three dimensional model of the CCM solves for both the $HCO_{3}^{−}$ and CO2 concentration throughout a spherical cell. We solve this model numerically and analytically at steady state for three different spatial organizations of carbonic anhydrase and RuBisCO in the cell (See Figure 6): enzymes distributed evenly throughout the cell, enzymes localized to the center of the cell but not encapsulated (as they would be on a scaffold), enzymes encapsulated in a carboxysome. We compare the effects of these scenarios in the discussion section, and for now consider a spherical cell of radius Rb = 0.5 μm with a single spherical carboxysome of radius Rc = 50 nm containing RuBisCO and carbonic anhydrase. Numerical computations are carried out with finite difference methods in MATLAB. The details of analytic solutions are given in the Supplementary file 1.

We include the effects of diffusion, active transport and leakage through the cell membrane, and reactions with carbonic anhydrase and RuBisCO. In the carboxysome (r < Rc), the equations governing the $HCO_{3}^{−}$ and CO2, here H and C respectively, are

$$
\partial_{t}C=D\nabla^{2}C+R_{CA}−R_{Rub}
$$



$$
\partial_{t}H=D\nabla^{2}H−R_{CA^{,}}
$$

where here D is the diffusion constant, and RCA is the carbonic anhydrase reaction, and RRub is the RuBisCO reaction. The carbonic anhydrase reaction follows reversible Michaelis–Menten kinetics (Kaplan & Reinhold, 1999; Price et al., 2007),

$$
R_{CA}(H,C)=\frac{V_{ba}K_{ca}H−V_{ca}K_{ba}C}{K_{ba}K_{ca}+K_{ca}H+KL_{ba}C},
$$

where Vca and Vba are hydration and dehydration rates, proportional to the local carbonic anhydrase concentration. Kca and Kba are the concentration at which hydration and dehydration are half maximum. The RuBisCO reaction follows Michaelis–Menten kinetics with competitive binding with O2, $R_{Rub}=V_{max}C/(C+K_{m})$, where $k_{m}=k_{m}^{′}(1+O/k_{i})$. Here Vmax is the maximum rate of carbon fixation and Km is the apparent half maximum concentration value, which has been modified to include competitive binding with O2, O. Ki is the dissociation constant of O2 with the RuBisCO and $K_{m}^{′}$ is the half maximum concentration with no O2 present. RuBisCO also requires ribulose-1,5-bisphosphate, the substrate which CO2 reacts with to produce 3-phosphoglycolate. Under CO2 limiting conditions it has been shown that there is sufficient ribulose-1,5-bisphosphate to saturate all RuBisCO active sites, and the reaction rates are independent of ribulose-1,5-bisphosphate concentrations (Mayo et al., 1989; Whitehead et al., 2014).

In the cytosol there is no carbonic anhydrase or RuBisCO activity, so RCA = 0 and $R_{Rub}=0$, and there is only diffusion of CO2 and $HCO_{3}^{−}$. We do not include the natural, but slow, interconversion of CO2 and $HCO_{3}^{−}$ in the cytosol. This assumption is a good one given that the $HCO_{3}^{−}$ concentration is known to be held out of equilibrium in the cell (Volokita et al., 1984; Price & Badger, 1989). In agreement with this experimental observation, we find that all the other processes effecting the concentration of $HCO_{3}^{−}$ in the cytosol happen much faster than the natural interconversion.

Boundary conditions prescribe the inorganic carbon fluxes into the cell and the diffusion across the carboxysome boundary. We treat the inorganic carbon fluxes at cell and thylakoid membranes together. At this cell boundary, there is passive leakage of both CO2 and $HCO_{3}^{−}$: the velocity of CO2 across the cell membrane, $k_{m}^{c}$ is about 1000-fold higher than that of $HCO_{3}^{−}$, $k_{m}^{H}$, due to the lower permeability of the membrane to charged molecules. To account for active import of $HCO_{3}^{−}$, we combine the total $HCO_{3}^{−}$ flux, jc, from all $HCO_{3}^{−}$ transporters. These transporters include BCT1 (encoded by cpm), which is thought to be powered by ATP; and BicA and SbtA which are thought to be symporters between $HCO_{3}^{−}$ and Na+, driven by the highly controlled electrochemical gradient for Na+ (Price et al., 2008, 2004; Omata et al., 1999). Additionally, there are two complexes NDH-13 and NDH-14 responsible for converting CO2 to $HCO_{3}^{−}$. This conversion is thought to either decrease CO2, creating a gradient across the membranes and ‘facilitating uptake’ of CO2, or ‘scavenge’ CO2 which has escaped from the carboxysome. These are localized to the thylakoid and possibly the plasma membrane. They have been linked to the photosynthetic linear and cyclic electron transport chain (Price et al., 2008; Maeda et al., 2002; Shibata et al., 2001). It has been proposed that electron transport drives the formation of local alkaline pockets where CO2 more rapidly converts to $HCO_{3}^{−}$. We more simply describe the conversion with a maximal reaction rate α, and concentration of half maximal activity of Kα. Combining these effects, the boundary condition setting diffusive flux of $HCO_{3}^{−}$ and CO2 at the cell membrane is

$$
D\partial_{r}C=−\frac{\alphaC_{cytosol}}{K_{\alpha}+C_{cytosol}}+k_{m}^{C}(C_{out}−C_{cytosol})
$$



$$
D\partial_{r}H=j_{c}H_{out}+\frac{\alphaC_{cytosol}}{K_{\alpha}+C_{cytosol}}+k_{m}^{H}(H_{out}−H_{cytosol})
$$

where the subscript cytosol and out indicate we are taking the concentration immediately inside and outside the cell boundary respectively. The diffusion constant times partial derivatives with respect to the radial coordinate, r, define the diffusive flux at the membrane.

The carboxysome shell is composed of proteins with a radius Rc ≈ 50 nm. As of yet, there have been no direct measurements of the carboxysome permeability to small molecules. Using the carboxysome geometry, we can calculate an upper bound for the diffusive velocity across the carboxysome shell, which is directly related to the carboxysome permeability. Crystal structures (Yeates et al., 2008; Cheng et al., 2008; yeates et al., 2007) show the surface has approximately Npores = 4800 small pores with radius $r_{pore}≈0.35$ nm, and thickness l = 1.8 nm. If kc is the characteristic velocity that small molecules pass through the shell, these numbers imply the upper bound for diffusive transport $k_{c}<\frac{\pir_{pore}^{2}D}{4\piR_{c}^{2}l}(N_{pores})≈0.02\frac{cm}{s}$. This calculation is done by taking the probability that a molecule will encounter a pore on the carboxysome shell $(\frac{N_{pores}\timespore surface area}{carboxysome surface area})$ and multipling it by the speed a small molecule will diffuse through the length of the pore (D/l). Since it does not take into account any charge effects, which would add an additional energy barrier, it is an upper bound. Although there has been much speculation that the positively charged pores might enhance diffusion of negatively charged $HCO_{3}^{−}$ (Yeates et al., 2008; Dou et al., 2008; Cheng et al., 2008), here we explore the simplest assumption, that both $HCO_{3}^{−}$ and CO2 have the same permeability. Namely, the boundary conditions at the carboxysome shell are

$$
D\partial_{r}C=k_{c}(C_{cytosol}−C_{carboxysome})
$$



$$
D\partial_{r}H=k_{c}(H_{cytosol}−H_{carboxysome}).
$$

We will vary kc (henceforth called carboxysome permeability, although it is a velocity) within our model and see that there is a range of kc where the CCM is effective even with kc identical for CO2 and $HCO_{3}^{−}$.

## Results

### Analysis of model: Finding functional parameter space

Now that we have defined our model, we wish to find the range of parameters where efficient carbon fixation occurs. In what follows, we fix the enzymatic rates, cell membrane permeability, and diffusion constant as reported in the literature (Jordan & Ogren, 1981; Missner et al., 2008; Gutknecht et al., 1977; Heinhorst et al., 2006) (see Table 1 and Table 2). Note that full analytic solutions are available in Supplementary file 1 sections S3 and S4, so the effect of varying other parameters can be analyzed. We consider the efficacy of the CCM as a function of jc, the flux of HCO3− into the cell, kc, the carboxysome permeability, and the parameters (α, Kα) governing the CO2 facilitated uptake mechanism. Both α and jc can be regulated by the organism and vary depending on environmental conditions, whereas the carboxysome permeability, kc, is the parameter with the largest uncertainty and debate (Cannon et al., 2001; Yeates et al., 2008; Cheng et al., 2008).

**Table 1.**
 Parameter values chosen for main set of simulations, unless otherwise indicated


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Definition</th>
      <th>Value</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hout</td>
      <td>concentration of bicarbonate outside the cell</td>
      <td>14 μM*</td>
      <td>(Price et al., 2008)</td>
    </tr>
    <tr>
      <td>Cout</td>
      <td>concentration of carbon dioxide outside of cell</td>
      <td>0.14 μM*</td>
      <td>(Price et al., 2008)</td>
    </tr>
    <tr>
      <td>D</td>
      <td>diffusion constant of small molecules, CO2 and HCO3−</td>
      <td>10−5 cm2s</td>
      <td>(Fridlyand et al., 1996)</td>
    </tr>
    <tr>
      <td>kmc</td>
      <td>permeability of cell membrane to CO2</td>
      <td>0.3 cms</td>
      <td>(Missner et al., 2008; Gutknecht et al., 1977)</td>
    </tr>
    <tr>
      <td>kmH</td>
      <td>permeability of cell membrane to HCO3−</td>
      <td>3×10−4cms</td>
      <td>(Missner et al., 2008; Gutknecht et al., 1977)</td>
    </tr>
    <tr>
      <td>Rc</td>
      <td>radius of carboxysome</td>
      <td>5×10−6 cm</td>
      <td>(Cheng et al., 2008; Schmid et al., 2006)</td>
    </tr>
    <tr>
      <td>Rb</td>
      <td>radius of bacteria</td>
      <td>5 × 10−5 cm</td>
      <td>(Savage et al., 2010)</td>
    </tr>
    <tr>
      <td>jc</td>
      <td>HCO3− transport rate resulting in 30mM cytosolic HCO3− pool</td>
      <td>0.6 cms*</td>
      <td>calculated here</td>
    </tr>
    <tr>
      <td>kc</td>
      <td>optimal carboxysome permeability</td>
      <td>10−3 cms*</td>
      <td>calculated here</td>
    </tr>
    <tr>
      <td>Vcell</td>
      <td>cell volume</td>
      <td>5.2×10−10μL</td>
      <td>calculated</td>
    </tr>
    <tr>
      <td>SAcell</td>
      <td>cell surface area</td>
      <td>3×10−8cm2</td>
      <td>calculated</td>
    </tr>
  </tbody>
</table>

_*these parameters are varied in the text, but these values are use unless noted otherwise._

**Table 2.**
 Table comparing enzymatic rates (Woodger et al., 2005; Sultemeyer et al., 1995; Heinhorst et al., 2006)


<table>
  <thead>
    <tr>
      <th>Enzyme reaction</th>
      <th>active sites</th>
      <th>kcat [1s]</th>
      <th>Vmax in ‘cell’ [μMs]</th>
      <th>Vmax in carboxysome [μMs]</th>
      <th>K1/2 [μM]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>carbonic anhydrase hydration</td>
      <td>80</td>
      <td>8 × 104</td>
      <td>8.8 × 103</td>
      <td>1.5 × 107</td>
      <td>3.2 × 103</td>
    </tr>
    <tr>
      <td>carbonic anhydrase dehydration</td>
      <td>80</td>
      <td>4.6 × 104</td>
      <td>1.5 × 104</td>
      <td>8.8 × 106</td>
      <td>9.3 × 103</td>
    </tr>
    <tr>
      <td>RuBisCO carboxylation</td>
      <td>2160</td>
      <td>26</td>
      <td>178</td>
      <td>1.8 × 105</td>
      <td>270</td>
    </tr>
  </tbody>
</table>

_Vmax in cell and carboxysome refer to the volumetric reaction rate assuming the enzymes are distributed throughout the entire cell or only carboxysome. Vba (Vmax for carbonic anhydrase dehydration) is estimated by assuming Keq = 5 and using parameters found in (Heinhorst et al., 2006). Vca is Vmax for carbonic anhydrase hydration. Similarly, Kba, and Kca are K1/2 for dehydration and hydration respectively._

For any given pair of kc and jc, we ask whether the CO2 concentrating mechanism is effective, using the criteria of saturating RuBisCO, reducing oxidation reactions, and not increasing the HCO3− concentration beyond carbonic anhydrase saturation. Our central result is presented in Figure 2, which shows the range of kc and jc where these conditions are met, assuming that there is no facilitated uptake, α = 0. The blue shaded region shows where RuBisCO is unsaturated, and the red shaded region shows where carbonic anhydrase is saturated. There is a crescent shaped region between these regions, where the CCM is effective according to our criteria. In the white region oxygenation reactions happen at a rate of greater than 1%. In the green shaded region oxygenation reactions occur at a rate of less than 1%. Within the white and green regions the CO2 concentration in the carboxysome varies greatly.

![Figure 2.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig2-v2.jpg)

**Figure 2.:** Phase space for $HCO_{3}^{−}$ transport, jc, and carboxysome permeability kc.Plotted are the parameter values at which the CO2 concentration reaches some critical value. The left most line (dark blue) indicates for what values of jc and kc the CO2 concentration in the carboxysome would half-saturate RuBisCO (Km). The middle line (light blue) indicates the parameter values which would result in a CO2 concentration where 99% of all RuBisCO reactions are carboxylation reactions and only 1% are oxygenation reactions when O2 concentration is 260 μM. The right most (red) line indicates the parameter values which result in carbonic anyhdrase saturating. Here α = 0, so there is no CO2 scavenging or facilitated uptake. The dotted line (grey) shows the kc and jc values, where the $HCO_{3}^{−}$ concentration in the cytosol is 30 mM. The $HCO_{3}^{−}$ concentration in the cytosol does not vary appreciably with kc in this parameter regime, and reaches 30 mM at $j_{c}≈0.6\frac{cm}{s}$. All other parameters, such as reaction rates are held fixed and the value can be found in the Table 1 and Table 2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Phase space for $HCO_{3}^{−}$ transport and carboxysome permeability.Solid lines show lines of constant CO2 concentration in the carboxysome for $D_{c}=1e−5\frac{cm^{2}}{s}$, or the diffusion constant of small molecule in water. Dashed lines show the same lines of constant CO2 concentration, bur for $D_{c}=1e−7\frac{cm^{2}}{s}$, or the diffusion constant of a small molecule in a 60% sucrose solution.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Phase space for $HCO_{3}^{−}$ transport, jc, and carboxysome permeability, kc.Plotted are the parameter values at which CO2 concentration reaches some critical value. The left most line (dark blue) indicates for what values of jc and kc the CO2 concentration in the carboxysome would saturate RuBisCO. The middle line (light blue) indicates the parameter values which would result in a CO2 concentration where 99% of all RuBisCO reactions are carboxylation reactions and only 1% are oxygenation reactions when O2 concentration is 260 µM. The right most (red) line indicates the parameter values which result in carbonic anyhdrase saturating. Here $\alpha=0\frac{cm}{s}$ (solid lines) and $\alpha=0\frac{cm}{s}$ (dashed line), showing the effect of CO2 scavenging or facilitated uptake on the phase space. All other parameters, such as reaction rates are held fixed and the value can be found Table 1.

The lines dividing the regions in Figure 2 are lines of constant carboxysomal CO2 concentration in jc and kc parameter space. The dark blue line is where CO2 = Km, the CO2 concentration for half-maximum RuBisCO reactions. The light blue line indicates parameter values resulting in the CO2 concentration (C99%) where rate of oxygenation reactions is 1% for O2 concentration of 260 μM. Varying carboxysome permeability, kc values, require more or less HCO3 transport, jc, to achieve the same carboxysomal CO2 concentration.

We can calculate an amplification factor for the C99% carboxysomal CO2 concentration as $A_{c}=\frac{C_{carboxysome}}{C_{out}+H_{out}}=133$. Any combination of jc and kc which produce C = C99%, make 133 times more CO2 available in the carboxysome than there is total inorganic carbon outside the cell. Generally, increasing $HCO_{3}^{−}$ transport, below the carbonic anhydrase saturation point results in higher CO2 concentration in the carboxysome.

### Varying HCO3− transport saturates enzymes

The basic physics of the phase diagram Figure 2 follows from examining how CO2 and HCO3− in the carboxysome change as jc is varied. Figure 3 shows the response to varying jc, with kc=10−3cms (the optimal value in Figure 4).

![Figure 3.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig3-v2.jpg)

**Figure 3.:** $HCO_{3}^{−}$ transport is varied, and all other system parameters are held constant. The CO2 concentration above which RuBisCO is saturated is Km (grey dashed line). The CO2 concentration where the oxygen reaction error rate will be 1% is C99% (grey dash-dotted line). The transition between carbonic anyhdrase being unsatruated and saturated happens where the two analytic solutions meet (where the dashed and solid red lines meet). Below a critical value of transport, $j_{c}≈10^{−3}\frac{cm}{s}$ the level of transport is lower than the $HCO_{3}^{−}$ leaking through the cell membrane. A value of $k_{c}=10^{−3} cm/s$ for the carboxysome permeability was used for these calculations.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** We assume the same amount of carbonic anhydrase and RuBisCO activity for each simulation and compare the case with the enzymes evenly distributed throughout the carboxysome to the case where the carbonic anhydrase is localized to the inner carboxysome shell. The (-.-) lines are for no organization and (x) for localization with $D_{c}=10^{−5}\frac{cm^{2}}{s}$. The (…) lines are for no organization and (o) are for localization with $D_{c}=10^{−7}\frac{cm^{2}}{s}$.

![Figure 4.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig4-v2.jpg)

**Figure 4.:** Numerical solution (diamonds and circles) and analytic solutions (carbonic anhydrase unsaturated, solid lines, and saturated, dashed lines) correspond well. On all plots CO2 (red circle) < $HCO_{3}^{−}$ (blue diamond). Concentration in the cell along the radius, r, with carboxysome permeability $k_{c}=10^{−5}\frac{cm}{s}$ (B), $k_{c}=10^{−3}\frac{cm}{s}$ (C), $k_{c}=1\frac{cm}{s}$ (D). Grey dotted lines in (B), (C), (D) indicate location of the carboxysome shell boundary. The transition from low CO2 at high permeability (D) to maximum CO2 concentration at optimal permeability (C) occurs at $k_{c}^{∗}=\frac{D}{R_{c}}=2\frac{cm}{s}$. At low carboxysome permeability (B) $HCO_{3}^{−}$ diffusion into the carboxysome is slower than consumption. For all subplots $\alpha=0\frac{cm}{s}$ and $j_{c}=0.6\frac{cm}{s}$. Qualitative results remain the same with varying jc, increasing α will increase the gradient of CO2 across the cell as CO2 is converted to $HCO_{3}^{−}$ at the cell membrane.

When jc is low, the ratio of CO2 and $HCO_{3}^{−}$ is constant, set by the chemical equilibrium at a given pH. In this case the rate of the carbonic anhydrase reaction is much faster than diffusion within the carboxysome, so that $V_{ba}K_{ca}H=V_{ca}K_{ba}C$. Unlike the uncatalyzed interconversion of CO2 and $HCO_{3}^{−}$ in the cytosol, carbonic anhydrase brings the concentrations in the carboxysome to equilibrium very quickly. The chemical equilibrium is $K_{eq}=H/C=(K_{ba}V_{ca})/(K_{ca}V_{ba})≈5$, for pH around 7 [Heinhorst et al., 2006; DeVoe & Kistiakowsky, 1961)], so that $HCO_{3}^{−}$ > CO2 in the carboxysome. Increased pH would increase Keq and the proportion of $HCO_{3}^{−}$, while decreased pH would decrease Keq and the proportion of $HCO_{3}^{−}$. Such variations do not substantially effect the subsequent discussion and mechanisms, although they will change the absolute values of CO2 concentration in the carboxysome.

The Km dashed line in Figure 3 shows the CO2 level above which RuBisCO reaction is saturated: this gives the RuBisCO saturated (blue) boundary in Figure 2. We have similarly marked the concentration C99% where there is a 1% oxygen reaction error rate with a dash-doted line.

At higher levels, the CO2 concentration no longer increases with increasing jc, because the carbonic anhydrase is saturated. The saturated regime occurs in Figure 3 when $H_{carboxysome}>K_{ba}$, so that increasing $H_{carboxysome}$ (controlled directly by jc) no longer increases the rate of production of $C_{carboxysome}$. This transition from unsaturated to saturated carbonic anhydrase defines the line for the carbonic anhydrase saturated region in Figure 2.

### Carboxysome permeability has optimal value

For each line of constant concentration in Figure 2 there is an optimal permeability value, where the least $HCO_{3}^{−}$ transport is required to achieve the same CO2 concentration. The optimal permeability value shifts downward with increasing CO2 concentration (compare light and dark blue curves). For C99% the optimal permeability is $k_{c}=10^{−3}\frac{cm}{s}$, below the calculated upper bound: $k_{c}<0.02\frac{cm}{s}$ obtained above from the carboxysome structure. To further understand the effect of permeability, we examine the CO2 concentration in the carboxysome for varying carboxysome permeabilities and a fixed $HCO_{3}^{−}$ transport rate in Figure 4. Figure 4A, shows that there is a broad range of kc where the CCM has maximal efficacy. Figure 4 shows the distribution of inorganic carbon throughout the cell when the permeability is low (B), optimal (C), and high (D). At high permeability, the CO2 produced in the carboxysome rapidly leaks out of the carboxysome, and the CO2 concentration in the cytosol, shown in Figure 4D, is relatively high. When the carboxysome permeability decreases to near the optimal value, Figure 4C, the carboxysome traps CO2, and the cytosolic levels are lower, decreasing leakage out of the cell. This transition occurs when diffusion across the cell (and carboxysome) takes a shorter time than diffusion through the carboxysome shell; or the CO2 in the carboxysome is effectively partitioned from the CO2 in the cell.

If the carboxysome permeability is below optimal, diffusion of $HCO_{3}^{−}$ into the carboxysome cannot keep up with consumption from RuBisCO, Figure 4B. The existence of an optima requires RuBisCO consumption to be low enough that there is a kc where the cytosol and carboxysome are partitioned, but $HCO_{3}^{−}$ diffusion in can keep up. When such an optima exists, the carboxysome permeability can improve the CO2 concentration in the carboxysome without any special selectivity between $HCO_{3}^{−}$ and CO2. The location and concentrating power of the optimal regime, is dependent on the size of the cell and the membrane permeabilities to CO2 and $HCO_{3}^{−}$.

## Discussion

### Are the fluxes and concentrations reasonable?

While we have solved our model to describe a vast parameter space it is instructive to compare the fluxes and concentrations we find within our optimal parameter space (the green region in Figure 2) to actual numbers. At low external inorganic carbon conditions, internal inorganic carbon pools due to CCM activity are regularly measured as high as Ci = 30 mM. The inorganic carbon is predominantly in the form of HCO3−, and measurements do not distinguish between the cytosol and carboxysome (Kaplan & Reinhold, 1999; Woodger et al., 2005; Sultemeyer et al., 1995; Price et al., 1998, 2008). In our model, we find that the cytosolic HCO3− concentration is 30 mM when jc=0.6cms, over a wide range of the carboxysome permeability (indicated as the dashed grey line in Figure 2). From Figure 4 we can also see that the cytosolic HCO3− concentration is the dominate form of inorganic carbon in the cell at jc=0.6cms. We examine the fate of the HCO3− transported into the cell in terms of the HCO3− leaking out, CO2 leaking out, CO2 fixation or carboxylation, and O2 fixation or oxygenation (Table 3).

**Table 3.**
 Fate of carbon brought into the cell for jc = 0.6cm/s and kc = 10–3cm/s


<table>
  <thead>
    <tr>
      <th></th>
      <th>formula</th>
      <th>[picomoles(cell s)]</th>
      <th>% of flux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HCO3− transport</td>
      <td>jcHout</td>
      <td>3.26 × 10−4</td>
      <td></td>
    </tr>
    <tr>
      <td>HCO3− leakage</td>
      <td>kmH(Hout−Hcytosol(Rb))</td>
      <td>3.2 × 10−4</td>
      <td>98.6%</td>
    </tr>
    <tr>
      <td>CO2 leakage</td>
      <td>kmC(Cout−Ccytosol(Rb))</td>
      <td>4.5 × 10−4</td>
      <td>1.4 %</td>
    </tr>
    <tr>
      <td>carboxylation</td>
      <td>VmaxCC+Km(1+OKO)</td>
      <td>8.2 × 10−8</td>
      <td>0.03 %</td>
    </tr>
    <tr>
      <td>oxygenation</td>
      <td>VmaxOCC+KmO(1+CKC)</td>
      <td>6.7 × 10−10</td>
      <td>2 × 10−4 %</td>
    </tr>
  </tbody>
</table>

For cells grown under low inorganic carbon conditions net HCO3− fluxes (transport - leakage) are measured 105pmolmgChls, with CO2 net flux being slightly lower but the same order of magnitude (Whitehead et al., 2014; Badger et al., 1994). High external inorganic carbon conditions produce slightly higher net HCO3− rates (Tchernov et al., 1997). Assuming chlorophyll per cell volume of around 10−11mgChlcell for cells of our size we can convert this into a flux of 10−6pmol(cells) (Whitehead et al., 2014; Keren et al., 2004, 2002). The net HCO3− flux for our model cell is 6×10−6pmol(cells), so we are about an order of magnitude too high. If we choose a HCO3− transport value one order of magnitude smaller, we will get net fluxes of the same order of magnitude as the measurements at the cost of slightly lower carboxylation rates and higher oxygenation rates (Table 4). This would also mean a lower internal HCO3− pool. Alternatively, the same internal HCO3− could be reached at a lower flux rate, if the external HCO3− is higher. Since the majority of the HCO3− transport is balanced by HCO3− leakage, we can find the transport rate needed to sustain a particular amplification by the simple formula: jc=kmH(Hout−Hcytosol(Rb))/Hout.

**Table 4.**
 Fate of carbon brought into the cell for jc = 0.06 cm/s and kc = 10–3cm/s


<table>
  <thead>
    <tr>
      <th></th>
      <th>formula</th>
      <th>[picomoles(cell s)]</th>
      <th>% of flux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HCO3− transport</td>
      <td>jcHout</td>
      <td>2.8 × 10−5</td>
      <td></td>
    </tr>
    <tr>
      <td>HCO3− leakage</td>
      <td>kmH(Hout−Hcytosol(Rb))</td>
      <td>2.7 × 10−5</td>
      <td>96.6 %</td>
    </tr>
    <tr>
      <td>CO2 leakage</td>
      <td>kmC(Cout−Ccytosol(Rb))</td>
      <td>8.8 × 10−7</td>
      <td>3.2 %</td>
    </tr>
    <tr>
      <td>carboxylation</td>
      <td>VmaxCC+Km(1+OKO)</td>
      <td>5.4 × 10−8</td>
      <td>0.2 %</td>
    </tr>
    <tr>
      <td>oxygenation</td>
      <td>VmaxOCC+KmO(1+CKC)</td>
      <td>2.3 × 10−9</td>
      <td>8 × 10−3 %</td>
    </tr>
  </tbody>
</table>

While we can compare the net fluxes, we have not found direct experimental evidence for the absolute $HCO_{3}^{−}$ uptake rate. To determine whether this $HCO_{3}^{−}$ transport rate is reasonable we perform a back of the envelope calculation. Our simulated cell has a flux of 2 × 108 molecules/s. Assuming the rate of transport per transporter of $10^{3}\frac{molecules}{s}$ and our cell's surface area this requires about $10^{4}\frac{transporters}{\mum^{2}}$. This is about an order of magnitude higher than the number of ATP synthase complexes on the thylakoid membrane in spinach, $700 \frac{complexes}{\mum^{2}}$ (Miller and Staehelin, 1979).

According to our calculation only around 1 % of the carbon transported into the cell is fixed into 3-phosophoglycerate. Even in this highly CO2 concentrating regime, 5 × 104 2-phosophoglycolate produced per second. Cyanobacteria have been shown to have multiple pathways for recycling 2-phosophoglycolate (Hackenberg et al., 2009). Our system fixes CO2 at a rate of 0.14 pg/hour. Given the volume of our cell, and the fact that between 115–300 fg/μm3 of carbon are needed to produce a new cyanobacterial cell (Mahlmann et al., 2008) we need between 0.1 and 0.3 picograms of carbon per cell. At the higher flux rate (Table 3) this means that a cell could replicate every 7–21 hr and the lower flux rate (Table 4) allows replication every 11–35 hr. Both are consistent with the division times of cyanobacteria.

### Concentration profiles of CO2 and HCO3− across the cell

At $j_{c}=0.6\frac{cm}{s}$, varying the carboxysome permeability changes how the available inorganic carbon is partitioned between the carboxysome and cytosol, thereby setting the carboxysomal CO2 concentration as shown in Figure 4. Strikingly, the $HCO_{3}^{−}$ concentration is constant across the cytosol. This is because the cell membranes have low permeability to $HCO_{3}^{−}$; thus, the rate of escape is slow and $HCO_{3}^{−}$ equilibrates across the cell. A consequence of this flat $HCO_{3}^{−}$ profile is that the carboxysome experiences the same $HCO_{3}^{−}$ concentration, independent of its position in the cell. This means the incoming inorganic carbon source for the carboxysome system is invariant with the position of the carboxysome in the cell.

In contrast, there is a gradient in CO2 concentration across the cell when the carboxysome permeability is at or above the optimum (Figure 4C,D). The cell membrane is more permeable to CO2. The gradient means that the CO2 leakage out of the cell affects the CO2 leakage out of the carboxysome. Moving the carboxysome close to the cell membrane increases the leakage rate of CO2 out of the carboxysome. Notably, in S. elongatus the carboxysomes are located along the center line of the cell, away from the cell membranes (Savage et al., 2010). The spatial profiles of $HCO_{3}^{−}$ and CO2 give no hint as to why the carboxysomes are spaced apart from one another. Since the gradient in $HCO_{3}^{−}$ is flat, there is no competition between the carboxysomes for $HCO_{3}^{−}$ (the main incoming source of inorganic carbon). In fact, since the local concentration of CO2 is higher near a carboxysome, nearby carboxysomes would ‘feed’ each other CO2. As has been shown, such clumping would reduce the probability of distributing carboxysomes equitably to daughter cells, possibly counteracting any benefit (Savage et al., 2010).

The concentration across the carboxysome is basically constant, because the carboxysome is so small that diffusion across it takes very little time. A consequence of this is that the organization of the reactions in the carboxysome does not effect the CO2 concentration in the carboxysome (Figure 3—figure supplement 1). Therefore, the localization of the carbonic anhydrase to the inner carboxysome shell seems to have no effect on the CCM. It has been suggested that diffusion in the carboxysome should be slower, since the carboxysome is packed with RuBisCO. One proposed consequence of slower diffusion in the carboxysome is that it could trap CO2, making a low carboxysome permeability unnecessary. We have tested this hypothesis (Figure 2—figure supplement 1), and find that assuming the diffusion constant one would expect for small molecules in a 60% sucrose solution ($D_{c}=10^{−7}\frac{cm^{2}}{s}$), does reduce the optimal carboxysome permeability. However, for any carboxysome permeability a higher $HCO_{3}^{−}$ transport rate is needed to achieve the same carboxsomal CO2 concentration. So if the diffusion is indeed slower in the carboxysome it does not aid the CCM. Even at this slower diffusion, the CO2 concentration across the carboxysome is flat.

### Benefit of CO2 to HCO3− conversion: facilitated uptake or scavenging of CO2

We investigate the effect of CO2 to $HCO_{3}^{−}$ conversion at the thylakoid and cell membranes (combined in the model). Increasing conversion, α > 0, can facilitate uptake of CO2 from outside the cell and scavenge CO2 escaped from the carboxysome. Facilitated uptake results in saturating both carbonic anhydrase and RuBisCO at a lower level of $HCO_{3}^{−}$ transport. Scavenging broadens the range of carboxysome permeability which will effectively separate the inorganic carbon pools in the carboxysome and outside. Scavenging decreases the concentration of CO2 in the cytosol, so a more permeable carboxysome can still result in a low leakage rate of inorganic carbon out of the cell (more of the inorganic carbon in the cytosol is in the form of $HCO_{3}^{−}$ which leaks out less readily). However, neither of these effects is particularly strong in our current range of reaction rates, and cell membrane permeability (Figure 2—figure supplement 2).

The relative effect of these two mechanisms depends on the external CO2 and HCO3− concentrations. In saltwater environments the pH is near 8 and HCO3− is the predominant inorganic carbon source. While external pH is not explicitly treated in our model, we can account for changes to pH through the external inorganic carbon concentration. To be consistent with oceanic environment, thus far we have shown results for low external inorganic carbon concentrations of [CO2] = 0.1 μM and [HCO3−] = 14.9 μM. The effect of facilitated uptake, under these assumptions, is very small. In freshwater or under conditions of ocean acidification, where the pH could fall to 6 or lower, there can be a much larger proportion of CO2 (>50%). Figure 5 shows the absolute contribution of HCO3− transport, facilitated CO2 uptake, and CO2 scavenging for varying proportions of external CO2. Even though we assume the same velocity of facilitated uptake and HCO3− transport (jc=αKα=1), facilitated uptake contributes less because it is limited by CO2 diffusion across the membrane. At the same rates of transport the facilitated uptake mechanism only contributes more than active HCO3− if the CO2 concentration is greater than 80% of external inorganic carbon. This is consistent with observations that oceanic cyanobacteria such as Prochlorococcus only seem to possess gene homologs for HCO3− transport systems, while other freshwater and estuarine cyanobacteria have gene homologs for both constitutive (NDH-14) and inducible (NDH-13) CO2 uptake systems as well as inducible HCO3− transport systems (BicA, SbtA, and BCT1) (Price, 2011).

![Figure 5.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig5-v2.jpg)

**Figure 5.:** Size of the $HCO_{3}^{−}$ flux in one cell from varying sources, as the proportion of $CO_{2}$ to $HCO_{3}^{−}$ outside the cell changes changes.We show results for three carboxysome permeabilities, $k_{c}$, and only the scavenging is effected. Total external inorganic carbon is $15\muM$, $j_{c}=1\frac{cm}{s}$ and $\frac{\alpha}{K_{\alpha}}=1\frac{cm}{s}$. Scavenging is negligibly small for all values of $k_{c}$ shown. Unless there is very little $HCO_{3}^{−}$ in the environment, $HCO_{3}^{−}$ transport seems to be more efficient than $CO_{2}$ facilitated uptake.

Scavenging is negligibly small for all values of $k_{c}$ shown. There is very little $CO_{2}$ in the cytosol, so there is very little $CO_{2}$ to scavenge, Figure 5. The effect of scavenging is dependent on the cell membrane permeability to $CO_{2}$ and $HCO_{3}^{−}$.

Given that scavenging has no obvious affect on $HCO_{3}^{−}$ concentrations, it is reasonable to wonder why this mechanism exists at all. One might assume that scavenging prevents leakage, but if the energy to bring a ‘new’ $HCO_{3}^{−}$ molecule from outside the cell is the same as the energy required to save an ‘old’ CO2 molecule from leaking out, there is no obvious advantage of preventing the leakage. It is possible that since the scavenging mechanism is associated with the electron transport chain of the light reactions of photosynthesis scavenging can be ramped up more easily when there is excess light energy. If this were the case, a comparison of $j_{c}=1\frac{cm}{s}$ and $\frac{\alpha}{k_{\alpha}}=1\frac{cm}{s}$ is deceiving and $\frac{\alpha}{K_{\alpha}}$ could be much larger. Indeed it has been suggested that the cell uses this mechanism as a way to dissipate excess light energy (Tchernov et al., 1997, 2003).

### Cellular organization

The most striking aspect of the CCM is the way that spatial organization is used to increase the efficacy of the reactions. Figure 6 compares the effect of different enzymatic reaction organizations. Concentrating carbonic anhydrase and RuBisCO to a small region in the center of the cell, on a scaffold for example, leads to an order of magnitude increase in the concentration of CO2. Localizing the carbonic anhydrase to a small volume concentrates it, increasing the maximum reaction rate per volume, Vca and Vba. A larger Vba increases the HCO3− concentration at which carbonic anhydrase is saturated allowing the mechanism to take advantage of a larger HCO3− flux, jc. A small increase can be gained from encapsulating the enzymes in a permeable carboxysome shell and another order of magnitude is gained at the optimal permeability. At optimal carboxysome permeability, the CO2 is effectively partitioned into the carboxysome and conversion can act only as facilitated uptake as shown in Figure 5.

![Figure 6.](https://cdn.elifesciences.org/articles/02043/elife-02043-fig6-v2.jpg)

**Figure 6.:** Concentration of CO2 achieved through various cellular organizations of enzymes, where we have selected the $HCO_{3}^{−}$ transport level such that the $HCO_{3}^{−}$ concentration in the cytosol is 30 mM.O2 concentration is 260 μM. The oxygenation error rates, as a percent of total RuBisCO reactions are indicated on the concentration bars. The cellular organizations investigated are RuBisCO and carbonic anhydrase distributed throughout the entire cytosol, co-localizing RuBisCO and carbonic anhydrase on a scaffold at the center of the cell without a carboxysome shell, RuBisCO and carbonic anhydrase encapsulated in a carboxysome with high permeability at the center of the cell, and RuBisCO and carbonic anhydrase encapsulated in a carboxysome with optimal permeability at the center of the cell.

Another advantage of localizing the enzymes in a small region at the center of the cell is separating carbonic anhydrase from the α (CO2 to $HCO_{3}^{−}$) conversion mechanism, preventing a futile cycle. The futile cycle is most detrimental when the enzymes are distributed through out the cytosol, and increases the oxygenation error rate (data not shown). Concentrating the enzymes away from the cell and thylakoid membranes, where conversion happens, removes this effect. On a scaffold the oxygenation rate is almost exactly the same with and without the α conversion mechanism. This is consistent with the previously shown detrimental effect of having active carbonic anhydrase free within the cytosol (Price & Badger, 1989). It would be impossible to keep the cytosol completely free from carbonic anhydrase enzyme, so there must be a way of activating it within the carboxysome only. Carbonic anhydrase is inactivated under reducing conditions (Peña et al., 2010). Recently it was shown that carboxysomes oxidize after assembly, providing a way to keep carbonic anhydrase inactive until fully enclosed in a carboxysome (Chen et al., 2013).

### Effects of pH

Cyanobacteria must regulate pH as almost all biochemical reactions are pH sensitive. We do not attempt to model this regulation or potential pH variation within the cell, however pH may be included implicitly in a couple ways. We have already explored the effect of varying external pH, and the effects of pH on carbonic anhydrase. Cytosolic pH would have little direct effect on the CO2 and $HCO_{3}^{−}$ levels since the non-enzymatic interconversion is very slow as previously discussed. The effect of internal pH could also be explored by varying the reaction rate of RuBisCO, which is pH sensitive. Varying the reaction rate of RuBisCO greatly could change the range where a non-specific carboxysome permeability can increase the concentration of CO2 in the carboxysome. It would be unexpected that the RuBisCO rate be much faster than we assume, as we have assumed a rate on the high end. A lower RuBisCO rate would increase the range of effective carboxysome permeabilities. As previously mentioned the CO2 facilitated uptake mechanism functions by creating local alkaline pockets. Diffusion of hydrogen ions across the cell would be very fast, so such pockets would require a massive reduction from the light reactions to maintain local alkalinity. Whether such pH gradients are possible, is certainly a subject of future interest.

### Conclusions

We have described and analyzed a model for the CO2 concentrating mechanism in cyanobacteria. There exists a broad range of $HCO_{3}^{−}$ transport and carboxysome permeability values which result in effective CO2 concentration in the carboxysome. This effective concentration parameter space is defined by CO2 levels high enough to saturate RuBisCO and produce a favorable ratio of carboxylation to oxygenation reactions, but not so high as to saturate carbonic anhydrase (after which increasing $HCO_{3}^{−}$ transport will not increase the CO2 concentration). An optimal carboxysome permeability exists, where $HCO_{3}^{−}$ diffusion into the carboxysome is not substantially inhibited, but CO2 leakage is minimal. $HCO_{3}^{−}$ concentrations across the cell are flat and are predominately set by the transport rate in, and leakage out. We quantitatively compare the transport rates and concentrations we predict in our optimal parameter space, and find them to be in good agreement with experiment. We also comment on the effects of external pH on CO2 versus $HCO_{3}^{−}$ uptake mechanisms. Finally we describe the cumulative benefits of co-localization, encapsulation, and optimal carboxysome permeability on the CCM.

Further comparison of this model to experimental flux measurements, especially to determine the quantitative contributions of different transporters under different physiological conditions would be very interesting. Current solutions are for steady state at constant external concentration, but most gas exchange measurements, by necessity, measure the fluxes as the inorganic carbon is depleted in the media. The model could be modified to solve the time dependent problem with varying external inorganic carbon. As of yet the carboxysome permeability has not been measured directly, and it would be quite interesting to see how close it is to our ‘optimal’ prediction.

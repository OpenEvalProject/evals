# Measuring protein stability in the GroEL chaperonin cage reveals massive destabilization

## Authors

- Ilia Korobko<sup>1</sup>
- Hisham Mazal<sup>2</sup> ([ORCID: 0000-0002-2071-9552](https://orcid.org/0000-0002-2071-9552))
- Gilad Haran<sup>2</sup> ([ORCID: 0000-0003-1837-9779](https://orcid.org/0000-0003-1837-9779))
- Amnon Horovitz<sup>1</sup> ([ORCID: 0000-0001-7952-6790](https://orcid.org/0000-0001-7952-6790)) †

### Affiliations

1. Departments of Structural Biology, Weizmann Institute of Science Rehovot Israel
2. Chemical and Biological Physics, Weizmann Institute of Science Rehovot Israel

† Corresponding author

## Abstract

The thermodynamics of protein folding in bulk solution have been thoroughly investigated for decades. By contrast, measurements of protein substrate stability inside the GroEL/ES chaperonin cage have not been reported. Such measurements require stable encapsulation, that is no escape of the substrate into bulk solution during experiments, and a way to perturb protein stability without affecting the chaperonin system itself. Here, by establishing such conditions, we show that protein stability in the chaperonin cage is reduced dramatically by more than 5 kcal mol−1 compared to that in bulk solution. Given that steric confinement alone is stabilizing, our results indicate that hydrophobic and/or electrostatic effects in the cavity are strongly destabilizing. Our findings are consistent with the iterative annealing mechanism of action proposed for the chaperonin GroEL.

## Introduction

The Escherichia coli GroE chaperonin system, which comprises GroEL and its co-factor GroES, assists protein folding in vivo and in vitro in an ATP-dependent manner (Thirumalai and Lorimer, 2001; Saibil et al., 2013; Hayer-Hartl et al., 2016; Gruber and Horovitz, 2016). Binding of GroES to GroEL forms a cage in which encapsulated substrate proteins can fold in isolation from bulk solution. The GroE system has been studied intensively for more than three decades, but it is still unclear and controversial whether its cavity is a ‘passive cage’ in which protein substrate aggregation is prevented but the folding pathway is unchanged or a chamber in which the folding process is altered in some manner. It is also unclear whether encapsulation in the GroE cavity is thermodynamically stabilizing, for example because of confinement, or destabilizing owing, for example, to a diminished hydrophobic effect.

The effects of encapsulation on folding kinetics have been examined in different studies but it has been difficult to generalize its impact, in part, because it may depend on the properties of the protein substrate studied such as its size and charge. According to some studies, encapsulation prevents aggregation but does not alter the protein substrate’s folding pathway and kinetics (Horst et al., 2007; Tyagi et al., 2011). In the case of rhodanese, for example, it was reported that encapsulation retards the folding of its C-terminal domain but has no effect on its N-terminal domain (Hofmann et al., 2010). By contrast, other studies have suggested more ‘active’ models according to which folding is accelerated in the GroEL cavity compared to bulk solution. Recent work showed, for example, that GroEL repairs a folding defect of a mutant of maltose-binding protein by accelerating the formation of an on-pathway intermediate (Ye et al., 2018). Accelerated folding upon encapsulation has been attributed to steric confinement and the negative charges of the cavity walls (Tang et al., 2006). It has also been attributed to substrate interactions with the cavity-protruding C-terminal tails of GroEL, which comprise Gly-Gly-Met repeats (Tang et al., 2006; Weaver and Rye, 2014; Weaver et al., 2017). In addition, GroEL-mediated folding can be affected by the cavity-confined water, which can enhance the hydrophobic effect (and thus accelerate folding) by accumulating near the cavity walls (England et al., 2008) or diminish it (and thus slow folding) by being more ordered. Finally, an even more ‘active’ mechanism has been proposed according to which encapsulated misfolded protein substrates undergo ATP-promoted forced-unfolding (Weaver and Rye, 2014), in accordance with the iterative annealing model (Todd et al., 1996), thereby giving them further opportunity to fold correctly. The iterative annealing model predicts higher folding yields but it has been suggested that annealing can also lead to accelerated folding (Tang et al., 2006; Gupta et al., 2014; Weaver and Rye, 2014; Weaver et al., 2017).

In contrast with the many and often conflicting studies on the kinetic effects of encapsulation, there have been virtually no reports on the thermodynamic effects of encapsulation. One complication in understanding the thermodynamic effects of encapsulation has been that protein substrates spend variable amounts of time folding in the cavity and in bulk solution because of GroEL-GroES cycling and the leakiness of its cavity (Motojima and Yoshida, 2010). As shown below, such leakiness is even greater in the complex of single-ring GroEL with GroES, which was used in some studies (Hofmann et al., 2010) and has been suggested to form during GroEL’s normal reaction cycle (Yan et al., 2018). Another complication has been that measuring protein stability usually involves perturbations such as temperature or solution changes, which could also affect the stability of the chaperonin itself. The goal of the work described here was, therefore, to establish a system that would allow measuring the stability of an encapsulated protein in a non-leaky and unperturbed GroE complex. An appropriate system was found to be a chimera of dihydrofolate reductase from Moritella profunda (DHFRMp) fused to eGFP, which is encapsulated in the football-shaped and non-cycling BeFx-stabilized GroEL-GroES2 complex (Figure 1). Consequently, we were able to isolate the thermodynamic effect of encapsulation from other effects associated with GroEL-GroES cycling. Our results show that protein stability in the GroEL cavity is reduced dramatically in comparison with bulk solution.

![Figure 1.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig1-v3.jpg)

**Figure 1.:** A chimera was formed by fusing dihydrofolate reductase from Moritella profunda (DHFRMp, PDB ID: 3IA4) to the C-terminus of eGFP (PDB ID: 2Y0G) via a linker. This chimera was then encapsulated in the cavity of the BeFx-stabilized football–shaped GroEL-GroES2 complex, which is depicted schematically with GroEL in purple and GroES in green. The cavity volume is about 175,000 Å3 whereas that of the chimera (which is not drawn to scale) is about 58,000 Å3 assuming 1.23 Å3 per Da.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) Freshly assembled eGFP-containing ‘football’ complexes were applied to a gel-filtration column and elution was monitored by measuring protein and eGFP absorbance at 280 and 485 nm, respectively. The inset shows SDS-PAGE analysis of a peak one fraction, which contains ‘football’ complexes with encapsulated eGFP. (B) A sample of ‘football’ complexes with encapsulated eGFP was kept at room temperature overnight and then analyzed by gel-filtration as above. Only one protein-containing fraction was observed and no free eGFP could be detected. SDS-PAGE analysis of this fraction (inset) showed that it contains GroEL, GroES and eGFP. Taken together, these results show that the GroEL-GroES2 football-shaped complexes remained intact and that eGFP did not escape outside during the overnight incubation. These experiments were repeated at least five times.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** (A) Freshly assembled eGFP-containing single-ring GroEL (SR1) complexes with GroES were applied to a gel-filtration column. The fractions were analyzed by SDS-PAGE (inset). The first peak, which was found to contain GroEL, GroES and eGFP, corresponds to eGFP-containing SR1 in complex with GroES. (B) Samples of eGFP-containing SR1 in complex with GroES were kept at overnight at room temperature and then analyzed by gel-filtration. Most of the eGFP was found in fractions (peak 3) that contain no GroEL and GroES (inset), thereby indicating that eGFP escaped from the cavity of the complex of SR1 with GroES. These experiments were repeated twice.

## Results

### Design and construction of a model protein substrate

We chose to use dihydrofolate reductase from Moritella profunda, a psychrophilic bacterium with an optimal growth temperature at 2°C, as a model substrate since it is a relatively unstable protein at room temperature Xu et al., 2003 whose folding can be monitored easily by measuring the regain in enzyme activity. DHFRMp was fused to the C-terminus of enhanced green fluorescent protein (eGFP) in order to further destabilize it as observed before for other proteins (Sokolovski et al., 2015; Dave et al., 2016). The fusion to eGFP also facilitated easy and sensitive determination of the location of the substrate, that is whether it is in the cavity or has leaked outside of it. Under our conditions, the apparent melting temperature, Tm, in bulk solution of DHFRMp alone was found to be about 41.2 (±1.8) °C whereas DHFRMp fused to eGFP was found to be strongly destabilized with a Tm of 22.8 (±1.1) °C (Figure 2). eGFP in the chimera was also found to be destabilized in bulk solution relative to eGFP alone, but to a lesser extent, with Tm values of 76.3 (±0.3) and 81.3 (±1.3) °C, respectively.

![Figure 2.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig2-v3.jpg)

**Figure 2.:** (A) DHFRMp, eGFP and a chimera of these proteins were subjected to temperature denaturation in bulk solution using a Real-Time PCR machine. Denaturation was monitored by measuring the change in fluorescence of the SYPRO Orange reagent. Each trace represents the average of at least six experiments. (B) Plots of the first derivatives of the denaturation curves as a function of temperature. Melting points were determined from these plots by using the StepOne Software v2.3.

### Identifying conditions for minimizing escape of encapsulated substrates

GroEL and GroES can form either GroEL-GroES bullet-shaped or GroEL-GroES2 football-shaped complexes. It has been reported that the GroEL-GroES2 complex is stabilized in the presence of BeFx (Taguchi et al., 2004). We, therefore, tested whether eGFP remains encapsulated in the BeFx-stabilized ‘football’ complex over a sufficiently long period of time. BeFx-stabilized and eGFP-containing ‘football’ complexes were prepared, purified by gel-filtration and then allowed to stand overnight at room temperature. The samples were then analyzed by gel-filtration in order to determine the extent, if any, of substrate escape. The results show that all the eGFP co-eluted with GroEL and GroES, thereby indicating that the complex remained intact and no escape occurred (Figure 1—figure supplement 1). Two other proteins, the p53 core domain and a chimera of the engrailed homeodomain transcription factor with eGFP with respective masses of 22.4 and 42.9 kDa, were also tested in this manner and found to not escape (data not shown). Previously, it was believed that substrates encapsulated in the cage formed by single-ring GroEL in complex with GroES cannot escape since dissociation of GroES from one ring of GroEL is triggered by ATP binding to the opposite ring (Rye et al., 1997). Experiments carried out with eGFP encapsulated in the cavity of single-ring GroEL in complex with GroES showed, however, that massive substrate leakage took place (Figure 1—figure supplement 2).

### Folding of the DHFRMp part of the chimera in the GroEL cavity

BeFx-stabilized ‘football’ complexes containing the chimera were purified and the DHFR activity of the encapsulated chimera was monitored at 23°C (i.e. near the apparent Tm of the fused DHFRMp in bulk solution) by following the change in absorbance at 340 nm, upon addition of the substrates NADPH and dihydrofolate (DHF). The data show a lag phase followed by a linear phase (Figure 3) before activity starts to diminish owing to substrate depletion. Strikingly, the lag phase is absent when the chimera is free in bulk solution (Figure 3). One possible reason for the presence of the lag phase, in the case of the encapsulated chimera, is that the added substrates (DHF and NADPH) need to diffuse into the cavity. In such a case, the rate constant associated with the lag phase should increase with increasing substrate concentrations. Alternatively, the lag phase may reflect substrate (DHF and/or NADPH)-promoted folding of the DHFRMp part of the chimera, which is destabilized in the cavity relative to bulk solution. Substrate (DHF and/or NADPH)-promoted folding of the DHFRMp part of the chimera can take place via a mechanism of conformational selection, that is the substrates bind only to the folded state, thereby shifting the equilibrium in its favor. In such a case, the rate constant associated with the lag phase should decrease with increasing substrate concentrations (Vogt and Di Cera, 2012). Alternatively, substrate-promoted folding of the DHFRMp part of the chimera can also occur via a mechanism of induced fit in which case the rate constant associated with the lag phase should increase with increasing substrate concentrations. In other words, an increase in the rate constant of the lag phase with increasing substrate concentration can be due to substrate penetration or induced fit, whereas a decrease is evidence for conformational selection. Discriminating between these mechanisms can, therefore, be achieved by measuring the substrate concentration dependence of the rate constant of the lag phase.

![Figure 3.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig3-v3.jpg)

**Figure 3.:** (A) Representative traces are shown for the DHFRMp activities of free (29 nM) and GroE-encapsulated (40 nM) chimera upon addition of 250 μM dihydrofolic acid and 300 μM NADPH. The reactions were monitored by measuring the decrease in absorbance at 340 nm as a function of time. An initial lag phase is observed in the case of the encapsulated chimera but not the free one. (B) The lag and linear phases in the data for the encapsulated chimera were fitted to Equation 1. (C) Good fits were obtained as indicated by plots of the residuals with random deviations about zero. See Materials and methods for additional details.

The change in the absorbance at 340 nm due to the enzyme activity of the encapsulated or free chimera was, therefore, monitored in the presence of different concentrations of DHF and a fixed concentration of NADPH. The data were fitted to:

$$
[P]=Vt+A(e^{−\lambdat}−1)
$$

where [P] is the product concentration (or the absorbance at 340 nm which is proportional to it), V is the slope that corresponds to the linear steady-state velocity of the reaction and A and λ are the respective amplitude and rate constant of the lag phase. Equation 1 can be derived for the reaction scheme $E_{U}⇄E_{F}⇄ES$, where EU, EF and ES designate the respective unfolded, folded and substrate-bound folded states of the protein (E), assuming that ligand binding is fast relative to the folding and unfolding steps. In such a case, the rate constant, λ, is given by Vogt and Di Cera, 2012:

$$
\lambda=k_{1}+\frac{k_{-1}k_{-2}}{k_{2}[S]+k_{-2}}=k_{1}+\frac{k_{-1}}{K_{a}[S]+1}
$$

where k1 and k-1 are the respective folding and unfolding rate constants, k2 and k-2 are the respective substrate association and dissociation rate constants and Ka = k2/k-2 is the substrate association constant. Inspection of Equation 2 shows that the value of the observed rate constant, λ, decreases with increasing substrate concentration as observed here in the case of the encapsulated chimera (Figure 4A). This finding indicates that the DHFRMp part of the chimera is significantly destabilized in the cavity, but not in bulk solution (where the lag phase is absent), and that the substrates DHF and NADPH shift its equilibrium toward the folded state via a conformational selection mechanism. In agreement with this finding, temperature melts of the chimera in bulk solution show that both DHF and NADPH stabilize its DHFRMp part (Figure 4—figure supplement 1). It should be noted that, in principle, a similar kinetic behavior would be observed for a scheme $E'⇄E_{F}⇄ES$, that is when the equilibrium is between the folded protein and a mis-folded inactive species, E’ (instead of between the folded and unfolded species). This possibility is unlikely, however, because it was found that only 20% of human DHFR mis-folds inside the cavity of the non-cycling complex of single-ring GroEL with GroES (Horst et al., 2007). In such a case, the expected lag phase due to the mis-folded population would not be observed owing to the activity of the remaining DHFR, which does not mis-fold. Moreover, according to this model, the mis-folded state is much more stable than the folded state, which is in violation of Anfinsen’s dogma that the native state is at the minimum free energy if the conditions in the cavity are assumed to favor folding.

![Figure 4.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig4-v3.jpg)

**Figure 4.:** (A) Plot of the observed folding rate constant, λ, of the DHFRMp part of the chimera inside the cavity as a function of the DHF concentration. The data were fitted to Equation 2, thereby yielding estimates of the folding and unfolding rate constants. These experiments were carried out in duplicate. (B) Reduced χ2 surfaces for the folding and unfolding rate constants k1 and k-1, respectively. The relatively steep chi-squared surfaces suggest that the extracted parameters are well defined with relatively narrow confidence intervals. (C) Plot of the initial enzyme velocity of the DHFRMp part of the chimera inside the cavity and in bulk solution, as a function of the DHF concentration. The data were fitted to the Michaelis-Menten equation. In the case of the encapsulated chimera, the initial enzyme velocities were obtained by fitting the data of decrease in absorption at 340 nm as a function of time to Equation 1. Error bars in both panels represent standard errors.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (A) The chimera (5 µM) alone or in the presence of 500 µM NADPH or DHF was subjected to temperature denaturation using a Real-Time PCR machine as described under Materials and methods. Each trace represents the average of at least six experiments. (B) Plots of the first derivatives of the denaturation curves as a function of temperature. Melting points were determined from these plots by using the StepOne Software v2.3. Under the conditions here, the melting temperature of the DHFRMp part of the chimera increases, in the presence of NADPH and DHF, by about 8°C and 31°C, respectively.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** (A) The stability of the DHFRMp part of the chimera was determined as a function of GuHCl concentration at different fixed concentrations of NADPH. Shown are representative data for denaturation in the presence of 0.05 and 2.9 µM NADPH. The data were fitted using Equation 3. (B) Plot of the free energies of unfolding, in the absence of GuHCl, as a function of the concentration of NADPH. The data were fitted using Equation 4. The m-values are essentially independent of the concentration of NADPH and were found to have an average value of 1.4 (±0.1) kcal mol−1 M−1. Error bars represent standard errors.

Values of the folding and unfolding rate constants were obtained by fitting the plot of λ as a function of substrate (DHF) concentration to Equation 2 and found to be 1.4 (±0.4) x 10−4 and 7.3 (±0.8) x 10−3 sec, respectively (Figure 4A,B). Consequently, the stability of the cavity-confined fused DHFRMp, in the absence of the substrates DHF and NADPH, is 2.4 (±0.2) kcal mol−1, that is the folded state is extremely destabilized so that it is less stable than the unfolded state. By contrast, the stability in bulk solution of fused DHFRMp, in the absence of the substrates DHF and NADPH, is −3.45 (±0.09) kcal mol−1 (Figure 4—figure supplement 2). This value was determined by measuring the stability of fused DHFRMp, in the presence of different concentrations of NADPH, in order to minimize aggregation that takes place in bulk solution, and then extrapolating to zero concentration of NADPH. Taken together, the results obtained here show that encapsulation in the GroEL cavity destabilizes the DHFRMp part of the chimera by more than five kcal mol−1 relative to bulk solution. Interestingly, analysis of the linear phase in the progress curves (e.g. in Figure 3) shows that the steady-state enzyme activity of DHFRMp is also affected by encapsulation. The Km value of the encapsulated fused DHFRMp for DHF is about 0.28 (±0.09) mM and, thus, about 10-fold higher than the value of 33 (±2) µM measured in bulk solution (Figure 4C), in agreement with a previous determination (Xu et al., 2003). The value of kcat may also be affected but these values are difficult to determine because of uncertainties regarding the active protein concentrations.

In order to test whether the destabilization of the cavity-confined fused DHFRMp is due to its interaction with the cavity walls, we carried out fluorescence anisotropy decay measurements. Fits of the decay curves for the free and caged chimeras yielded similar rotational times of 22.85 (±0.30) ns and 25.40 (±0.45) ns, respectively (Figure 5). Likewise, the fits of the decay curves for free and caged eGFPs yielded similar rotational times of 14.38 (±0.20) ns and 15.90 (±0.25) ns, respectively (Figure 5—figure supplement 1), in agreement with previous work (Striker et al., 1999). The results indicate free mobility of the chimera and eGFP inside the GroEL football complex. It is, therefore, unlikely that the cavity-induced thermodynamic destabilization of the fused DHFRMp is due to interactions with the cavity walls.

![Figure 5.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig5-v3.jpg)

**Figure 5.:** (A) Fluorescence anisotropy decay curves of free (green) and caged (red) chimeras were measured as described in the Materials and methods. Fits of the decay curves for free and caged chimera to a single exponential (green and red solid lines, respectively) yielded rotational times of 22.85 (±0.30) ns and 25.40 (±0.45) ns, respectively. The results indicate no restriction on the mobility of the chimera inside the GroEL football complex. Each experiment was carried out in duplicate. (B) Plots of the residuals for the fits in panel A.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/56511/elife-56511-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A) Fluorescence anisotropy decay curves of free (green) and GroEL-caged (red) eGFP were measured as described in the Materials and methods. Fits of the fluorescence anisotropy decay curves for free and caged eGFP to a single exponential (black and blue solid lines, respectively) yielded rotational times of 14.38 (±0.20) ns and 15.90 (±0.25) ns, respectively, in agreement with previous work (Striker et al., 1999). These results indicate no restriction mobility of eGFP inside the GroEL football complex. Each experiment was carried out in duplicate. (B) Plots of the residuals for both curves.

## Discussion

Our results show that protein stability in the chaperonin cage is reduced dramatically by more than 5 kcal mol−1 compared to that in bulk solution. Given that steric confinement alone is expected to be stabilizing, our results indicate that protein destabilization in the cavity is likely to be due to hydrophobic and/or electrostatic effects. One possibility is that water in the cavity becomes more ordered in the presence of a substrate protein, thereby leading to a diminished hydrophobic effect. All-atom molecular dynamics simulations have shown that pairwise hydrophobic interactions are destabilized in hydrophobic nanopores when they contain water at bulk density (Vaitheeswaran and Thirumalai, 2008), as indicated by some evidence in the case of the GroEL cavity (Franck et al., 2014). The cavity walls of the ‘football’ complexes in our experiments are, however, charged and the extent of destabilization would, therefore, depend on many factors including the distribution of charges on the cavity walls, the cavity geometry and the presence of regions where the water structure is disrupted. Future simulations should test how these various factors affect pairwise interactions under confinement.

Similar to man-made machines, biological machines such as GroEL cycle between states that differ in their structural and functional properties. Substrate proteins first bind to GroEL in its apo state and can become destabilized through binding to its hydrophobic cavity walls (see, for example, Libich et al., 2015). ATP binding to the GroEL-protein substrate complex, which follows, can cause further unfolding due to a stretching force applied to the substrate protein upon ATP-binding-promoted conformational changes (Weaver et al., 2017). Next, protein substrates are encapsulated in the GroES-capped cavity for 1–10 s (Bigman and Horovitz, 2019) before being discharged into bulk solution. Here, we have succeeded in isolating the effect of this key step on substrate stability and found that it can also lead to protein destabilization. It is important to point out, however, that the magnitude (and possibly direction) of the effect is likely to depend on the protein substrate’s size and other properties. Hence, future studies should employ the strategy developed here to examine other proteins.

Finally, it is important to note that our finding that the cavity environment is destabilizing supports the iterative annealing mechanism of action proposed for the chaperonin GroEL (Todd et al., 1996; Thirumalai et al., 2020). According to this mechanism, protein substrates undergo kinetic partitioning, during each reaction cycle of GroEL, between productive folding to the native state and mis-folding. The remaining fraction of mis-folded protein substrates are then rebound to GroEL and (partially) unfolded, thereby giving them new opportunity to fold correctly. Our results show that (partial) unfolding is achieved not only because of binding to the hydrophobic cavity of the apo state and ATP-promoted forced unfolding, as shown before by others, but also because it is strongly favored thermodynamically under the conditions in the GroES-capped cavity.

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
      <td>Recombinant DNA reagent</td>
      <td>Pet21d plasmid for expressing DHFRMp</td>
      <td>Gift from Prof. S. Fleishman</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Pet21a plasmid for expressing eGFP</td>
      <td>PMID:29066625</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>E. coli Rosetta cells</td>
      <td>Novagen</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>E. coli BL21 cells</td>
      <td>PMID:3537305</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>TEV site insertion -forward</td>
      <td>This work</td>
      <td>PCR primer</td>
      <td>5’-ACTCGAGCACCACCACCACCACCACTGA-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>TEV site insertion -reverse</td>
      <td>This work</td>
      <td>PCR primer</td>
      <td>5’-GCTGTATAAGGGCAACCTGTATTTTCAGGGCACTCGAGCACCACC-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DHFRMp cloning -forward</td>
      <td>This work</td>
      <td>RF cloning primer</td>
      <td>5’-CCTGTATTTTCAGGGCATGATCGTAAGCATGATTGCCGCACTGGCG-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DHFRMp cloning -reverse</td>
      <td>This work</td>
      <td>RF cloning primer</td>
      <td>5’-GGTGGTGGTGGTGCTCGAGTTCACTCGAGTTTGACTCTTTCAAGTAGAC-3’</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SYPRO Orange protein gel stain</td>
      <td>Sigma</td>
      <td>Cat#S5692</td>
      <td>Used at a dilution of 1:5000</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB 2015b</td>
      <td>MathWorks</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>HisTrap 5 ml columns</td>
      <td>GE Healthcare</td>
      <td>Cat#17-5248-02</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PD 10 desalting columns</td>
      <td>GE Healthcare</td>
      <td>Cat#17-0851-01</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Superdex 75 10/300 column</td>
      <td>GE Healthcare</td>
      <td>Cat#29-1487-21</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Superose 6 10/300 column</td>
      <td>GE Healthcare</td>
      <td>Cat#17-5172-01</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Q Sepharose column</td>
      <td>GE Healthcare</td>
      <td>Cat#17-1014-01</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Construction of the chimera of DHFRMp with eGFP

The Pet21a plasmid containing the gene for eGFP (with the mutation A206K that stabilizes its monomeric state) and an N-terminal His7-tag (Bandyopadhyay et al., 2017) was amplified by PCR using the following respective forward and reverse primers:

5’-ACTCGAGCACCACCACCACCACCACTGA-3’

5’-GCTGTATAAGGGCAACCTGTATTTTCAGGGCACTCGAGCACCACC-3’. This amplification resulted in introducing a TEV protease cleavage site at the C-terminus of eGFP. The gene coding for DHFRMp was then introduced at the 3’ end of the TEV coding sequence by restriction-free cloning using the forward and reverse primers:

5’-CCTGTATTTTCAGGGCATGATCGTAAGCATGATTGCCGCACTGGCG-3’

5’-GGTGGTGGTGGTGCTCGAGTTCACTCGAGTTTGACTCTTTCAAGTAGAC-3’, respectively. The final gene product codes for eGFP with an N-terminal His7-tag fused at its C-terminus to DHFRMp via a linker sequence containing a TEV protease cleavage site.

### Expression and purification of the chimera of DHFRMp with eGFP

E. coli BL21 cells (Studier and Moffatt, 1986) harboring the Pet21d plasmid containing the gene for the chimera were inoculated into 250 ml 2 x TY with 100 µg/ml ampicillin and grown at 37°C until an O.D. of 0.6 was reached. Expression was induced by addition of 0.5 mM IPTG and growth was continued overnight at 16°C. The cells were then spun at 11,970 g for 20 min at 4°C, resuspended in 10% sucrose solution, spun again at 3,452 g for 30 min at 4°C and the pellet was stored at −80°C until purification. The pellet was resuspended in 30 ml of 50 mM Tris-HCl buffer (pH 7.5) containing 10 mM NaCl and 1 mM DTT (buffer A) with 8 M urea to prevent proteolysis. The cells were lysed using a French press (three passes) and sonication (4 cycles of 20 s sonication at 70% intensity and 60 s intervals). The lysate was then centrifuged at room temperature for 10 min at 24,610 g and again at 38,720 g for 30 min. The supernatant was diluted with buffer A to 6 M urea and loaded on a 140 ml Q-Sepharose column pre-equilibrated with buffer A containing 6 M urea. The column was then washed with 200 ml buffer A containing 6 M urea and with 150 ml of this buffer containing also 150 mM NaCl. A 5 ml HisTrap column, which was pre-equilibrated with buffer A containing 6 M urea, was connected downstream to the Q-Sepharose column and both columns were washed with 200 ml of buffer A with 1 M NaCl. The Q-Sepharose column was then removed and the HisTrap column was washed at room temperature with 75 ml of 50 mM Tris-HCl buffer (pH 7.5) containing 100 mM NaCl, 15 mM imidazole and 1 mM DTT (buffer B) with 5 M urea. Elution was carried out with a 75 ml linear gradient of 15 to 500 mM imidazole in buffer B with 5 M urea. Fractions were analyzed with SDS-PAGE and those containing the chimera were combined and concentrated to ~8 ml. The protein was then refolded at 4°C by mixing it with buffer B at a ratio of 1.5:98.5, respectively, during loading on a HisTrap 5 ml column. After loading, the column was washed with 25 ml buffer B and the protein was eluted with a 75 ml linear gradient from 15 to 500 mM imidazole in buffer B. Fractions containing the pure chimera were identified by SDS-PAGE and pooled and the buffer was then exchanged to 20 mM Hepes (pH 8.0) containing 100 mM KCl, 50 mM MgCl2, 50 mM Na2SO4, 10 mM NaF, 1 mM BeSO4 and 1 mM DTT (working buffer) using a PD 10 desalting column at 4°C. The concentration was determined from the absorption at 280 nm using an extinction coefficient of 50435 M−1 cm−1 and the protein was aliquoted and stored at −80°C for further use.

### Expression and purification of DHFRMp

Expression and purification of DHFRMp were achieved as before (Xu et al., 2003) with the following changes. E. coli Rosetta cells harboring the Pet21d plasmid containing the DHFRMp gene were inoculated into 7 L 2 x TY medium and grown at 37°C until an O.D. of 1 was reached. IPTG (0.5 mM) was then added to induce protein expression and the cells were grown at 37°C for another 5 hr. Harvesting was carried out by spinning the cells at 11,970 g for 20 min at room temperature and then resuspending them in 100 ml buffer B containing 10 µg/ml aprotinin, 5 µg/ml antipain, 5 µg/ml pepstatin, 5 µg/ml chymostatin, 10 µg/ml leupeptin, 50 μl EDTA-free protease inhibitor cocktail (Calbiochem), 1.5 μM PMSF, 6 μg/ml RNase A, 30 µg/ml DNase and 0.22 mg/ml folate. The cells were lysed by sonication (4 cycles of 20 s sonication at 70% intensity and 60 s intervals) and one passage through a French press at 1500 atm. The lysate was centrifuged at 4°C for 30 min at 24,610 g and then for 30 min at 38,720 g. The supernatant was applied to a 5 ml His-Trap column, which was then washed with 25 ml buffer B, 25 ml buffer B containing 1 mM ATP and 50 mM MgCl2 and then with 25 ml buffer B again. DHFRMp was eluted with a 50 ml linear gradient of 15 mM to 500 mM imidazole in buffer B. Fractions were analyzed with SDS-PAGE and those containing DHFRMp were combined, concentrated and the buffer was exchanged to 50 mM Tris-HCl (pH 8.0) containing 250 mM NaCl, 5 mM EDTA, 5 mM β-mercaptoethanol (buffer C) using a PD-10 desalting column at 4°C. The protein was applied to a 5 ml methotrexate column, which was then washed with 20 ml buffer C. DHFRMp was eluted with a linear gradient of 70 ml from 0 to 1 mM folate and 0.25 to 1 M NaCl in buffer C. Fractions were analyzed with SDS-PAGE and those containing DHFRMp were combined, concentrated, mixed with 1 mM ATP and 50 mM MgCl2 and then applied to a Superdex 75 10/300 gel-filtration column equilibrated with working buffer. Fractions were analyzed by SDS-PAGE and those containing pure DHFRMp were combined, aliquoted and stored at −80°C. The protein concentration was determined using the Bradford assay and a BSA-based calibration curve.

### Measurements of melting temperatures of eGFP and DHFRMp

The melting temperatures of eGFP and DHFRMp alone and in the chimera were measured by differential scanning fluorimetry using a StepOne real-time PCR instrument (Applied Biosystems). The protein (5 µM) alone or in the presence of 500 µM NADPH or dihydrofolate was mixed with 1X SYPRO Orange reagent (Sigma) in a 20 µl reaction volume of working buffer. The sample was heated from 4°C to 94°C with a temperature increment of 0.5°C every 45 s. The fluorescence of SYPRO Orange was measured after each temperature increment by exciting at 492 nm and measuring the emission at 610 nm. Analysis of the data was carried out using the StepOne software V2.3.

### Stability measurements of the DHFRMp part of the chimera in bulk solution

The stability of the DHFRMp part of the chimera was determined by measuring the fluorescence emission at 330 nm upon excitation at 280 nm (using an ISS PC1 fluorimeter with excitation and emission bandwidths of 16 nm) as a function of GuHCl concentration at different fixed concentrations of NADPH. Measurements were made at 23°C for samples containing about 1.4 μM of the chimera in working buffer after incubation for 10 min at the same temperature. The concentration of the stock solution of GuHCl was determined by measuring the refraction index at 23°C. The data were fitted using the following equation:

$$
F=\frac{F_{U}^{0}+a[D]+(F_{N}^{0}+b[D])e^{\frac{−ΔG^{0}+m[D]}{RT}}}{1+e^{\frac{−ΔG^{0}+m[D]}{RT}}}
$$

where ΔG0 is the free energy of unfolding in the absence of denaturant, [D] is the GuHCl concentration, m is the GuHCl-concentration dependence of the free energy of unfolding ($m=\frac{∂ΔG}{∂[D]}$), T is the temperature and R is the gas constant. The fluorescence of the native (N) and denatured (U) states are expressed as linear functions of the GuHCl concentration with slopes of a and b, respectively. This analysis is based on the assumption that the melting curves reflect the denaturation of only the DHFRMp part of the chimera, which is justified since eGFP is very stable under our conditions and the fluorescence of its single tryptophan residue changes very little (and in a linear fashion) as a function of GuHCl concentration. The values of ΔG0 obtained from the fits to Equation 3 were then plotted as a function of the concentration of NADPH and the data were fitted using the following equation:

$$
ΔG=ΔG^{0}−RTln(1+[S]/K_{m})
$$

where [S] is the concentration of NADPH and Km is its Michaelis-Menten constant of 13 µM (Evans et al., 2010). Here, ΔG0 is the free energy of unfolding in the absence of both GuHCl and NADPH.

### Encapsulation of protein substrates in GroE footballs

Encapsulation of eGFP and the chimera in the GroEL-GroES2 football was performed using different methods of denaturation. In the case of eGFP, the substrate (7.5 nmol) was denatured in 200 µl of 60 mM HCl in a siliconized test-tube. The denatured eGFP was then added slowly to 20 ml of 50 mM Tris-HCl buffer (pH 7.5) containing 100 mM KCl, 50 mM MgCl2, 1 mM DTT, 0.05 µM GroEL oligomer and 0.125 µM GroES oligomer (folding buffer) and left for 40 min at room temperature with mild stirring. Football assembly was initiated by adding 2 ml containing 550 mM Na2SO4, 110 mM NaF, 11 mM BeSO4 and 11 mM ATP (activation mix) to the folding buffer. The mixture was then stirred for 15 min at room temperature, concentrated and fractionated using a Sepharose 6 (10/300) gel-filtration column in working buffer. Fractions were analyzed by SDS-PAGE and those containing GroE-encapsulated eGFP were kept for further work. In the case of the chimera, a binary complex was first formed by incubating 9 nmol of the native chimera with ~5 nmol of GroEL oligomer in 300 µl of working buffer overnight at room temperature. The mixture was then added to a 200 µl solution containing 135 mM Na2SO4, 25 mM NaF, 2.5 mM BeSO4, 2.5 mM ATP and ~10 nmol of GroES oligomer, stirred for 15 min at room temperature and applied to a Superose 6 10/300 gel-filtration column.

### DHFR activity assays

Activity assays were performed at 23°C in working buffer using an Infinite M200pro (TECA Group Ltd.) plate reader. Reactions were initiated by mixing 190 µl of the protein with 10 µl of NADPH (350 µM final concentration) and different concentrations of DHF. The reaction progress was followed by measuring the decrease in absorption at 340 nm as a function of time. The chimera concentrations were verified from measurements of the fluorescence emission at 509 nm upon excitation at 488 nm (with bandwidths of 4, 8 or 16 nm depending on the protein concentration) and using an eGFP-based calibration curve. Analysis and fitting of the data were performed using MatLab 2015b software.

### Time-resolved fluorescence anisotropy measurements

Fluorescence anisotropy decay curves of the target proteins were measured using a MicroTime200 fluorescence microscope (PicoQuant). Samples of eGFP and the chimera were diluted to 50–100 nM in the working buffer containing 0.01% TWEEN 20 and then loaded into a flow cell pre-coated with a lipid bilayer (Mazal et al., 2019). Molecules were excited with a 485 nm diode laser pulsed at a repetition rate of 20 MHz and with a power of 10 µW. Emitted photons were divided based on their polarization using a polarizing beam splitter cube, followed by filtration using band-pass filters (520/35 nm, BrightLine). Photon arrival times relative to the excitation pulse were registered with a resolution of 16 ps using two single-photon avalanche photo-diodes detectors (Excelitas SPCM-AQR-14-TR) coupled to a time-correlated single-photon counting module (HydraHarp 400, PicoQuant). The parallel and perpendicular fluorescence decays were constructed from the data and background corrected. Fluorescence anisotropy decays were then calculated using the following relation: $rt=\frac{I_{∥(t)}-GI_{⊥(t)}}{I_{∥(t)}+2GI_{⊥(t)}}$, where $I_{∥(t)}$ and $I_{⊥(t)}$ are the time-dependent fluorescence intensities of the parallel and perpendicular components, and G is the polarization sensitivity factor (whose value was determined to be 1). Fluorescence anisotropy decays were fitted to a single exponential function to obtain the rotational correlation times of the proteins.

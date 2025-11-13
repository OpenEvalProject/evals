# Environment determines evolutionary trajectory in a constrained phenotypic space

## Authors

- David T Fraebel<sup>1</sup> ([ORCID: 0000-0002-8668-3476](https://orcid.org/0000-0002-8668-3476))
- Harry Mickalide<sup>1</sup>
- Diane Schnitkey<sup>1</sup>
- Jason Merritt<sup>1</sup>
- Thomas E Kuhlman<sup>1</sup>
- Seppe Kuehn<sup>1</sup> ([ORCID: 0000-0002-4130-6845](https://orcid.org/0000-0002-4130-6845)) †

### Affiliations

1. Center for the Physics of Living Cells University of Illinois at Urbana-Champaign Urbana United States
2. Department of Physics University of Illinois at Urbana-Champaign Urbana United States
3. Center for Biophysics and Quantitative Biology University of Illinois at Urbana-Champaign Urbana United States

† Corresponding author

## Abstract

Constraints on phenotypic variation limit the capacity of organisms to adapt to the multiple selection pressures encountered in natural environments. To better understand evolutionary dynamics in this context, we select Escherichia coli for faster migration through a porous environment, a process which depends on both motility and growth. We find that a trade-off between swimming speed and growth rate constrains the evolution of faster migration. Evolving faster migration in rich medium results in slow growth and fast swimming, while evolution in minimal medium results in fast growth and slow swimming. In each condition parallel genomic evolution drives adaptation through different mutations. We show that the trade-off is mediated by antagonistic pleiotropy through mutations that affect negative regulation. A model of the evolutionary process shows that the genetic capacity of an organism to vary traits can qualitatively depend on its environment, which in turn alters its evolutionary trajectory.

## Introduction

In nature organisms adapt to complex environments where many biotic and abiotic factors affect survival. For microbes these factors include demands on metabolism (Savageau, 1983), motility (Celani and Vergassola, 2010) and antibiotic resistance (Vetsigian et al., 2011). In this context, evolution involves the simultaneous adaptation of many phenotypic traits. Organisms under complex selection pressures often cannot vary traits independently and instead exhibit trade-offs (Shoval et al., 2012).

Trade-offs constrain adaptive responses to selection. For example, phage exhibit a trade-off between fecundity and virulence which depends on the relative duration of periods of horizontal and vertical transmission (Messenger et al., 1999). Bacterial populations selected for efficient conversion of nutrients to biomass exhibit a trade-off between yield and growth rate (Bachmann et al., 2013).

Predicting evolution in complex environments requires quantifying both trade-offs and selection pressures (Lande, 1979). In wild populations of birds (Grant and Grant, 1995) and fish (Ghalambor et al., 2003), phenotypic constraints and selection pressures have been inferred from measurements of phenotypic variation. However, in wild populations of higher organisms it is challenging to observe evolution, determine selection pressures and elucidate mechanisms constraining phenotypes. To better understand the interplay between trade-offs, selection and evolution, it is necessary to study genetically tractable, rapidly evolving microbial populations in the laboratory.

However, laboratory-based experimental evolution of microbes typically selects for a single phenotype such as growth rate (Lang et al., 2013). There is evidence that metabolic trade-offs arise in these experiments from the decay of traits that are not subject to selection (Cooper and Lenski, 2000) rather than a compromise between multiple selection pressures. Other experiments explore how phenotypes restricted by trade-offs evolve under alternating selection for individual traits (Yi and Dean, 2016; Messenger et al., 1999). Less is known about evolutionary dynamics in the naturally relevant regime where selection pressures are multifaceted.

To address this, we selected Escherichia coli for faster migration through a porous environment. We showed that the evolution of faster migration is constrained by a trade-off between swimming speed and growth rate. Evolution of faster migration in rich medium is driven by faster swimming despite slower growth, while faster migration in minimal medium is achieved through faster growth despite slower swimming. Sequencing and genetic engineering showed that this trade-off is due to antagonistic pleiotropy through mutations that affect negative regulation. Finally, a model of multi-trait selection supports the hypothesis that the direction of evolution when phenotypes are constrained by a trade-off is determined by the genetic variance of each trait. Our results show that when selection acts simultaneously on two traits governed by a trade-off, the environment determines the evolutionary trajectory.

## Results

### Experimental evolution of migration rate

E. coli inoculated at the center of a low viscosity agar plate consume nutrients locally, creating a spatial nutrient gradient which drives chemotaxis through the porous agar matrix (Righetti et al., 1981; Maaloum et al., 1998) and subsequent nutrient consumption (Adler, 1966; Wolfe and Berg, 1989; Croze et al., 2011). As a result, the outermost edge of the expanding colony is driven by both growth and motility (Koster et al., 2012). The result is a three-dimensional bacterial colony that expands radially across the plate as individuals swim and divide in the porous environment. We refer to the outermost edge of an expanding colony as the migrating front. We tracked these migrating fronts using webcams and light-emitting diode (LED) illumination (Materials and methods). The front migrates at a constant speed $s$ after an initial growth phase (Adler, 1966; Wolfe and Berg, 1989).

We performed experimental evolution by repeating rounds of allowing a colony to expand for a fixed time interval, selecting a small population of cells from the migrating front and using them to inoculate a fresh low viscosity agar plate (Figure 1a). By isolating cells from the migrating front, our procedure selects both for motility and growth rate. We performed selection experiments in this way for two distinct nutrient conditions. First, we used rich medium (lysogeny broth (LB), 0.3 % w/v agar, 30°C) where all amino acids are available. In this medium the population forms concentric rings (Figure 1b) that consume amino acids sequentially. The outermost ring consumes L-serine and most of the oxygen (Adler, 1966). Second, we used minimal medium (M63, 0.18 mM galactose, 0.3 % w/v agar, 30°C) where populations migrate towards and metabolize galactose with a single migrating front.

![Figure 1.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig1-v2.jpg)

**Figure 1.:** (a) A schematic of the selection procedure. E. coli are inoculated into the center of a low viscosity (0.3 % w/v) agar plate where they form an expanding colony driven by metabolism and motility. After a fixed period of incubation, samples are taken from eight locations around the outer edge of the expanded colony, mixed, and used to inoculate a fresh plate. (b) Shows expanded colonies in rich medium (LB) plates after 12 hr of incubation over five successive rounds of selection. The color bar to the right applies to all panels in (b), with darker gray indicating higher cell density. Image intensity is assumed to be monotonic but not linear with cell density in the plate. Scale bar in the left panel is 1 cm and applies to all panels in (b). (c) Shows the rate of migration as a function of round of selection over 15 rounds for five replicate selection experiments in rich medium. No rate is reported for replicate 1 round 8 due to failure of the imaging device. Errors in measured rates of migration are smaller than the size of the markers. (d) Shows colonies (gray regions) in minimal medium (M63, 0.18 mM galactose) after 48 hr of incubation. The color bar to the right applies to all panels in (d). The scale bar in the left panel is 1 cm. (e) Shows the rate of migration as a function of round of selection over 10 rounds for five replicate selection experiments in minimal medium. Errors in migration rates were smaller than the size of markers. See Materials and methods for details of image processing in both experiments.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Selection with non-chemotactic ($Δ$cheA-Z) mutant.Front migration rates of non-chemotactic mutants in 0.3 % w/v agar at 30°C with LB (left panel) and M63 0.18 mM galactose (right panel). Errors are smaller than the size of the markers, except for the red replicate in rich medium at round 2. Red and black correspond to two independent selection experiments. Note the vertical scales. In minimal medium, zero migration rate denotes plates where density increased in the vicinity of the site of inoculation but no migration was observed. In these cases no measurable migration rate was obtained.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (left) The founder strain (Figure 1c, main text, $s=$ 0.3 $\pm$ 0.01 cm h−1) was inoculated into a turbidostat and continuously cultured in LB at 30°C for approximately 200 generations. Samples were periodically drawn from the turbidostat and used to inoculate 0.3 % w/v agar LB plates in duplicate. Migration was recorded via webcam as described in the main text. Error bars are standard errors from regression of radius with time. Note the scale on the y-axis. (right) Identical experiment in minimal medium conditions. Founding strain was grown in a single chemostat (doubling time 5.7 hr) in minimal medium for 120 generations. Plates were inoculated from samples drawn from the chemostat, two plates at each time point for the first four time points and then one plate at each time point. The last four time points (where the rate appears to saturate) exhibit a slower migration rate than the round 10 migration rates in Figure 1e ($p=0.02$).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Migration rate as a function of the round of selection. Colored traces are reproduced from Figure 1 in the main text. Black circles and squares are two replicate selection experiments where populations are sampled halfway between the center of the colony and the outer edge after each round of selection.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Single-cell swimming in rich medium: (left) Run duration distributions identical to those shown in Figure 3a–b of the main text. 77 RP437 individuals were tracked from a culture at the same optical density as founder and round 15 (replicate 1). A total of 9218 run events were recorded. The average $\pm$ standard deviation in run duration for RP437 is 0.76 $\pm$ 0.82 s. (right) Comparison of run speeds for the same three strains. RP437 has an average $\pm$ standard deviation in run speed of 18.6 $\pm$ 6.4 μm s−1. The average run duration for RP437 exceeds that of round 15 ($p<10^{−4}$), and the average run speed is smaller than that of round 15 ($p<10^{−4}$). For the RP437 strain in rich medium, we measure a migration rate of 0.15 $\pm$ 0.01 cm h−1 and a liquid culture growth rate of 1.1 $\pm$ 0.02 h−1.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** A strain isolated after 15 rounds of selection in rich medium (Figure 1c, replicate 1, main text, $s=$ 0.6 cm h−1) was inoculated into a turbidostat and continuously cultured in LB at 30°C for approximately 140 generations. The number of generations was estimated assuming a constant generation time of 36 min. Samples were periodically drawn from the turbidostat and used to inoculate 0.3 % w/v agar LB plates. Migration was recorded via webcam as as described in the main text. Error bars are standard errors from regression of radius with time.

In rich medium, colonies of wild-type bacteria (MG1655-motile, founding strain) expand with a front migration speed $s≈$ 0.3 cm h−1 and cells were sampled from the front after 12 hr (Figure 1b). A portion of this sample was used to immediately inoculate a fresh plate while the remainder was preserved cryogenically. The process was repeated every 12 hr for 15 rounds. We observed a nearly 50% increase in $s$ over the course of the first 5 rounds of selection. The increase in $s$ was largely reproducible across five independent selection experiments (Figure 1c). We estimate that plate-to-plate variation in agar concentration due to evaporative loss could change the migration rate by up to 0.06 cm h−1 in later rounds (Appendix 1). However, independent replicate selection experiments exhibit fluctuations in migration rate that exceed this estimate. For example, replicate 4 declines in later rounds of selection, and this decline may reflect the unique low abundance mutation that appears in this replicate by round 15 (Figure 5a). In addition, replicate 3 exhibits substantially faster migration than replicates 1, 2 and 4 in round 7, and this may reflect the distinct mutations observed in this replicate at round 5 (Figure 5a). So, while migration rates increased in all replicates, the magnitude of the increase differed between replicates.

To check whether chemotaxis was necessary for increasing $s$, we performed selection experiments using a motile but non-chemotactic mutant ($Δ$cheA-Z, Materials and methods). Motility in this strain was confirmed by single-cell imaging in liquid media. As observed previously (Wolfe and Berg, 1989), the non-chemotactic strain formed dense colonies in low viscosity agar that remained localized near the site of inoculation and expanded $∼$1 cm in a 24 hr period: a rate 10-fold slower than the wild-type. To allow sufficient time for colony expansion, we performed selection experiments using this strain with 24 hr incubation times and observed an increase in $s$ from approximately 0.03 cm h−1 to 0.04 cm h−1 (Figure 1—figure supplement 1). We did not observe fast migrating spontaneous mutants which have been reported previously in multiple species (Wolfe and Berg, 1989; Mohari et al., 2015), likely because our plates were incubated for a shorter period of time.

To determine the number of generations transpiring in our selection experiments, we measured the number of cells in the inoculum and the number of cells in the colony after 12 hr of growth and expansion (Materials and methods). We estimated that 10 to 12 generations occurred in each round of selection. We then tested whether prolonged growth in well mixed liquid medium for a similar number of generations could lead to faster migration by growing the founding strain for 200 generations in continuous liquid culture and periodically inoculating a low viscosity agar plate (Figure 1—figure supplement 2). We observed only a 3.5% increase in the rate of migration, demonstrating that selection performed on spatially structured populations results in more rapid adaptation for fast migration than growth in well mixed conditions.

We then performed selection experiments in a minimal medium where growth and migration are substantially slower than in rich medium (Figure 1d). In this condition we allowed 48 hr for each round of expansion and took precautions to limit evaporative loss in the plates over this longer timescale (Materials and methods). In the first round, the population formed small $∼$1.5 cm diameter colonies without a well defined front. Populations formed well defined fronts in subsequent rounds of selection (Figure 1d), reflecting a transition from growth and diffusion dominated transport to chemotaxis dominated migration (Croze et al., 2011). We observed an approximately 3-fold increase in $s$ over the course of 10 rounds of selection. Variation across replicate experiments was substantial, and exceeded our estimate of systematic error due evaporative losses changing the agar concentration (Appendix 1). So while all replicates increased their migration rate, the magnitude of the increase in migration rate varied substantially. This variation may be due to the different mutations present across replicates (Figure 5b).

When we performed selection in minimal medium using the non-chemotactic mutant ($Δ$cheA-Z), we found little or no migration and only a very small increase in the migration rate over 10 rounds of selection (Figure 1—figure supplement 1). We concluded that chemotaxis is also necessary for increasing $s$ in this medium.

Using the same technique described for rich medium, we estimated the number of generations per round of selection in minimal medium to be <10. We tested whether approximately 120 generations of growth in liquid was sufficient to evolve faster migration in minimal medium. Here we found that prolonged growth in well mixed conditions resulted in $∼$2-fold faster front migration. Despite the increase in migration rate, selection in well mixed conditions resulted in slower migration than selection in low viscosity agar plates for a similar number of generations (Figure 1—figure supplement 2).

### Increasing swimming speed and growth rate increase migration rate

To characterize the adaptation we observed in Figure 1c,e, we studied a reaction-diffusion model of migrating bacterial fronts of the type pioneered by Keller and Segel (1971) and reviewed in Tindall et al. (2008). We model the bacterial density $ρ⁢(𝐫,t)$ and a single chemo-attractant that also permits growth $c⁢(𝐫,t)$. Our model includes only a single nutrient since the growth and chemotaxis of the outermost ring in rich media is driven by L-serine (Adler, 1966) and our minimal media conditions contain only a single carbon source/attractant. The dynamics of $ρ⁢(𝐫,t)$ and $c⁢(𝐫,t)$ are governed by

$$
\frac{∂ρ}{∂t}=D_{b}∇^{2}ρ−∇⋅(\frac{k_{0}K_{D}}{(K_{D}+c)^{2}}ρ∇c)+g(ρ,c)
$$

and

$$
\frac{∂c}{∂t}=D_{c}∇^{2}c−f(ρ,c),
$$

where the spatial and temporal dependence of ρ and c have been suppressed for clarity. The three terms on the right hand side of Equation 1 describe diffusion, chemotaxis and growth respectively. Db is the bacterial diffusion constant, which describes the rate of diffusion of bacteria due to random, undirected motility. k0 is the chemotactic coefficient, which captures the strength of chemotaxis in response to gradients in attractant. KD is the equilibrium binding constant between the attractant and its associated receptor (Brown and Berg, 1974). Growth is modeled using the Monod equation g(ρ,c)=kgρcKg+c , where kg is the maximum growth rate and is the concentration of nutrient allowing half-maximal growth. f(ρ,c) describes the nutrient consumption and has an identical form to g(ρ,c) since we assume the yield (Y, cells mL-1mM-1) is a constant. Dc is the diffusion constant of small molecules in water. The physiological parameters describing growth and attractant-receptor binding (kg, Kg, Y and KD) were either measured here or have been reported in the literature and can be applied directly in our simulation of migration in both nutrient conditions. Table 1 describes each parameter used in this study.

**Table 1.**
 Reaction-diffusion model parameters: Columns indicate parameter, explanation of parameter, units, value used in simulation of founder strain in rich medium, and the value used in simulation of founder strain in minimal medium. Parameters marked with an $^{m}$ were measured in this study. $D_{b}$, $k_{0}$ and $D_{c}$ in rich medium were estimated as described in Appendix 1 using the methods of Croze et al (2011). $D_{c}$ is assumed to be the same in minimal medium as rich medium. Identical $k_{0}$ and $D_{b}$ were used in rich and minimal media since Ford and Lauffenburger (1992) find nearly identical values for galactose as Ahmed and Stocker (2008) do for serine. $K_{D}$ for both nutrient conditions was taken from Hazelbauer Adler et al., 1973. For minimal medium $K_{g}$ and $Y$ were taken from Lendenmann et al., 1999. The values cited for $s$ were measured from numerical simulation of the reaction-diffusion model as outlined in Materials and methods.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Explanation</th>
      <th>Units</th>
      <th>Founder value RM</th>
      <th>Founder value MM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">Single-cell swimming (this study)</td>
    </tr>
    <tr>
      <td>τr</td>
      <td>run duration</td>
      <td>s</td>
      <td>0.67m</td>
      <td>0.47m</td>
    </tr>
    <tr>
      <td>τt</td>
      <td>tumble duration</td>
      <td>s</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>|vr|</td>
      <td>run speed</td>
      <td>μm s−1</td>
      <td>18.7m</td>
      <td>22.2m</td>
    </tr>
    <tr>
      <td colspan="5">Reaction-diffusion model</td>
    </tr>
    <tr>
      <td>ρ⁢(𝐫,t)</td>
      <td>cell density</td>
      <td>m−3</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>c⁢(𝐫,t)</td>
      <td>nutrient density</td>
      <td>mM</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>c0</td>
      <td>nutrient concentration in medium</td>
      <td>mM</td>
      <td>1m</td>
      <td>0.18m</td>
    </tr>
    <tr>
      <td>Db</td>
      <td>bacterial diffusion constant</td>
      <td>cm2h−1</td>
      <td>0.0576</td>
      <td>0.0576</td>
    </tr>
    <tr>
      <td>Dc</td>
      <td>nutrient diffusion constant</td>
      <td>cm2h−1</td>
      <td>0.036</td>
      <td>0.036</td>
    </tr>
    <tr>
      <td>k0</td>
      <td>chemotactic coefficient in liquid</td>
      <td>cm2h−1</td>
      <td>6.12</td>
      <td>6.12</td>
    </tr>
    <tr>
      <td>KD</td>
      <td>receptor-nutrient binding constant</td>
      <td>mM</td>
      <td>2</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>kg</td>
      <td>maximum growth rate</td>
      <td>h−1</td>
      <td>1.23m</td>
      <td>0.125m</td>
    </tr>
    <tr>
      <td>Kg</td>
      <td>c concentration for half-maximum growth rate</td>
      <td>mM</td>
      <td>0.1</td>
      <td>3P &lt;10-4</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>yield biomass per unit nutrients</td>
      <td>cells mL-1mM-1</td>
      <td>5×107m</td>
      <td>3×108</td>
    </tr>
    <tr>
      <td>C</td>
      <td>agar concentration</td>
      <td>% (w/v)</td>
      <td>0.3m</td>
      <td>0.3m</td>
    </tr>
    <tr>
      <td>s</td>
      <td>front migration rate</td>
      <td>cm h−1</td>
      <td>0.61</td>
      <td>0.09</td>
    </tr>
  </tbody>
</table>

The bacterial diffusion constant and the chemotactic coefficient depend on motility and the physical structure of the agar matrix. Motility in E. coli consists of runs, segments of nearly straight swimming $∼$0.5 to 1 s long at $∼$20 μm s-1, and tumbles that rapidly reorient the cell over a period of $∼$0.1 s (Berg and Brown, 1972). Rivero et al. showed how the reaction-diffusion parameters $D_{b}$ and $k_{0}$ depend on run speed and duration (Rivero et al., 1989). Croze et al. (2011) modified these results to account for the presence of the agar matrix. The approach treats interactions between cells and agar as scattering events where the cell is forced to tumble.

We estimated $D_{b}$ and $k_{0}$ using the method developed by Croze et al. for our conditions. With these parameters we simulated the model in Equations 1 and 2 with parameters appropriate for rich media (chemotaxis towards L-serine) and minimal media (chemotaxis towards galactose). For the founder strain, these simulations predicted a migration rate of 0.61 cm h−1 for rich media and 0.08 cm h−1 for minimal media compared to measured rates of 0.30 $\pm$ 0.01 cm h−1 and 0.0163 $\pm$ 0.0038 cm h−1 respectively. We note that this comparison involves no free parameters.

In rich medium our model describes the dynamics of a single metabolite/attractant (L-serine), and therefore fails to account for secondary fronts behind the outermost front, which arise from the metabolism of other amino acids (Adler, 1966) (Figure 1b, Figure 2—figure supplement 2). This is a reasonable approximation since we select cells only from the outermost front of the colony. In minimal medium, where only a single nutrient is available, we observe only a single migrating front as our model predicts (Figure 2—figure supplement 2). Other limitations of this model include the fact that it does not describe the process of adaptation by chemoattractant receptors (Berg and Tedesco, 1975), nor does it describe stochastic processes at the single-cell level such as trapping in the agar matrix and cell-to-cell variability. The discrepancy between predicted migration rate and our observed migration rate most likely arises from the fact that cells are transiently trapped in the agar matrix (Wolfe and Berg, 1989) rather than simply being scattered. While more sophisticated models have been developed to include these processes (Vladimirov et al., 2008; Frankel et al., 2014), the model in Equations 1, 2 captures the essential features of bacterial front migration with fewer adjustable parameters. See Appendix 1 for further discussion.

To understand how changes in motility and growth could contribute to the evolution of migration, we studied how the migration rate (s) varied with the parameters of our model through numerical simulation (Appendix 1). We found that increases in run speed (|vr|) and growth rate (kg) had the largest impact on s (Figure 2). Consistent with previous reports, our model indicates that only small gains in migration rate can be achieved through increases in tumble frequency (Wolfe and Berg, 1989) (∼10%, Figure 2—figure supplement 3).

![Figure 2.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig2-v2.jpg)

**Figure 2.:** (a) Front migration rate (heatmap) as a function of run speed ($|v_{r}|$) and maximum growth rate ($k_{g}$) simulated using the reaction-diffusion model discussed in the text with parameters appropriate for rich medium conditions (Table 1). Model parameters were estimated using the method developed by Croze et al (Appendix 1). Black square shows the run speed and growth rates measured for the founding strain in rich medium (Figure 3). Standard error in $|v_{r}|$ is smaller than the size of the marker; error bar in $k_{g}$ is the standard deviation across three replicate measurements. (b) Identical to panel (a) except for minimal medium. The abrupt change in migration rate around $k_{g}=$0.2 h−1 corresponds to a transition from diffusion dominated front migration to a traveling wave (Appendix 1). The founding strain’s phenotype is shown as a black circle, error bars are constructed identically to those in (a).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Results from numerical simulations of the reaction-diffusion model in the main text. Simulations for founding strain in rich medium (a), founding strain in minimal medium (b), and round 5 strain in minimal medium (c) are shown. Three snapshots of $ρ(r,t)$ for each simulation are shown as greyscale heatmaps (note independent color maps). The panel on the right in (a–c) shows the location of the front in time (black trace) and the time points corresponding to the three snapshots are labeled by the colored points. The parameters for each simulation are given in Table 1. The founding strain in minimal medium exhibits diffusive transport due to slow growth, this is also observed experimentally (Figure 1, main text). Scale bars on the left of each panel are 1 cm.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Upper four panels show front density profiles from simulation and experiment for the rich medium condition. Left column shows founder and right column round 15. Simulation profiles are taken from time points after a constant rate of expansion has been attained. Experimental front profiles are taken at the end of colony expansion (12 hr). In the experimental front profiles, the high-density regions arise from metabolism of amino acids other than serine. The lower four panels are identical to the upper four but are taken from minimal medium simulations and experiments.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Using the formalism of Croze et al., migration rate as a function of tumble frequency (Appendix 1) was computed using the reaction-diffusion model presented in the main text. Panels show migration rate ($s$) as a function of tumble frequency ($\alpha_{0}$) for rich medium and minimal medium conditions. Red dots indicate measured tumble frequency for founder in each condition (Figure 3, main text). Error bars in the left panel are smaller than the size of the markers. Error bars in the right panel are standard errors from a linear regression on the front location in time. The non-monotonic variation of migration rate with tumble frequency in minimal medium results from the slight curvature in the front location as a function of time in these conditions (Figure 2—figure supplement 1 [right panel]).

Figure 2 shows how the front migration rate (heatmap) varies with run speed and growth rate for both nutrient conditions studied in Figure 1. Our model predicts that the fastest migrating strain should be the one that increases both its run speed and growth rate relative to the founder. Therefore, in the absence of any constraints on accessible phenotypes, we expect both run speed and growth rate to increase with selection.

### A trade-off constrains the evolution of faster migration

To test the predictions of the reaction-diffusion model, we experimentally interrogated how the motility and growth phenotypes of our populations evolved over the course of selection. We performed single-cell tracking experiments using a microfluidic method similar to one described previously (Jordan et al., 2013). This method permitted us to acquire 5 min swimming trajectories from hundreds of individuals from strains isolated prior to selection (founder) and after 5, 10 and 15 rounds of selection in rich media (replicate 1, Figure 1c) and for the founder and strains isolated after 5 and 10 rounds of selection in minimal media (replicate 1, Figure 1e). For tracking, cells were grown in the medium in which they were selected. This technique permitted us to capture more than 280,000 run-tumble events from approximately 1500 individuals. Tracking code is available (Mickalide et al., 2017).

We identified run and tumble events for all individuals (Berg and Brown, 1972; Taute et al., 2015) (Materials and methods). Figure 3a–b shows that run durations declined over the course of selection in both rich and minimal media. We show the complementary cumulative distribution function (c⁢(τr)) of run durations (τr) aggregated across all run events detected for the founding or evolved strains (c⁢(τr)=1-∫-∞τrd⁢τr′⁢P⁢(τr′), where P⁢(τr′) is the distribution of run durations). c⁢(τr) quantifies the fraction of all runs longer than a time τr. These distributions show that the evolved strains exhibited a reduction in the probability of executing long runs. We observed opposite trends for tumble duration, with decreasing tumble duration in rich medium and increasing duration in minimal medium (Figure 3—figure supplement 2). To summarize these changes in run-tumble statistics, we computed the tumble bias (fraction of time spent tumbling) and the tumble frequency (tumbles per second, Figure 3c–d). In both conditions, we observe an increase in the tumble frequency. This is expected since previous studies showed that mutants with increased tumble frequencies have faster migration rates through agar, likely due to tumbles freeing cells from being trapped in the agar (Wolfe and Berg, 1989). In rich medium we observed a decline in tumble bias, while selection in minimal medium increased the tumble bias. Tumble bias and frequency are reported in Table 2 for all tracked strains.

**Table 2.**
 Tumble bias and frequency for additional strains.


<table>
  <thead>
    <tr>
      <th colspan="3">Tumble bias and frequencies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>strain</td>
      <td>Tumble bias</td>
      <td>Tumble frequency [Hz]</td>
    </tr>
    <tr>
      <td>Rich medium</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>founder</td>
      <td>0.197 ± 0.006</td>
      <td>0.59 ± 0.02</td>
    </tr>
    <tr>
      <td>15(r3)</td>
      <td>0.174 ± 0.006</td>
      <td>0.78 ± 0.02</td>
    </tr>
    <tr>
      <td>15(r4)</td>
      <td>0.2 ± 0.01</td>
      <td>0.79 ± 0.01</td>
    </tr>
    <tr>
      <td>clpXE185*</td>
      <td>0.19 ± 0.01</td>
      <td>0.66 ± 0.02</td>
    </tr>
    <tr>
      <td>Minimal medium</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>founder</td>
      <td>0.29 ± 0.01</td>
      <td>0.41 ± 0.03</td>
    </tr>
    <tr>
      <td>10(r2)</td>
      <td>0.25 ± 0.02</td>
      <td>0.44 ± 0.03</td>
    </tr>
    <tr>
      <td>galSL22R</td>
      <td>0.3 ± 0.02</td>
      <td>0.44 ± 0.05</td>
    </tr>
  </tbody>
</table>

![Figure 3.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig3-v2.jpg)

**Figure 3.:** (a–f) Show single-cell swimming phenotypes (run duration ($\tau_{r}$), run speed ($|v_{r}|$), tumble bias and tumble frequency, see Materials and methods). Tracking was performed for founding strain (140 cells, 19,597 run events), strains isolated after 5 (79 cells, 12,217 run events), 10 (97 cells, 18,505 run events) and 15 (96 cells, 15,928 run events) rounds in rich media and in minimal media for the founding strain (72 cells, 7556 run events), round 5 (45 cells, 9724 run events) and round 10 (25 cells, 4892 run events). (a) Shows the fraction of runs longer than a given $\tau_{r}$ for strains evolved in rich media (95% confidence intervals from bootstrapping). The mean and standard deviation in run duration for founder is 0.66 $\pm$ 0.78 s, for round 5: 0.63 $\pm$ 0.61 s, for round 10: 0.58 $\pm$ 0.50 s and for round 15: 0.65 $\pm$ 0.57 s. Round 5, 10 and 15 strains exhibit shorter average run durations than founder (p<0.05). (b) Shows the same distribution for strains in minimal medium with founder exhibiting average run duration 0.49 $\pm$ 0.52 s, round 5: 0.44 $\pm$ 0.48 s and round 10: 0.33 $\pm$ 0.28 s. Rounds 5 and 10 exhibit shorter average run durations than founder ($p<10^{−8}$). (c–d) Show average fraction of time spent tumbling (tumble bias) and tumble frequency (tumbles per second) for rich medium and minimal medium respectively. Note the two vertical axes. In rich medium only the round 15 tumble bias is significantly different from founder (p<0.001), but the tumble frequency is higher than founder for both rounds 10 and 15 (p<0.001). In minimal medium all tumble biases and frequencies are significantly different from founder for all strains (p<0.001). (e) Shows run speed distributions for strains evolved in rich medium, legend in (a) applies. The average $\pm$ standard deviation run speeds are, for founder: 18.7 $\pm$ 7.1 μm s−1, round 5: 24.9 $\pm$ 7.1 μm s−1, round 10: 27.6 $\pm$ 7.0 μm s−1, and for round 15: 28.7 $\pm$ 6.8 μm s−1. Average run speeds for rounds 5, 10 and 15 are greater than founder (f) Shows the same distributions for strains evolved in minimal medium, average run speed for founder: 20.7 $\pm$ 10.8 μm s−1, for round 5: 11.2 $\pm$ 4.8 μm s−1 and for round 10: 13.3 $\pm$ 4.4 μm s−1. Both rounds 5 and 10 exhibit slower average run speeds than founder, the legend in (b) applies. (g–h) Show growth rates in well mixed liquid culture for all strains studied in panels (a–f) in the medium in which the strains were selected. (g) Shows triplicate measurements from each of the four strains isolated in rich medium. Rounds 5, 10 and 15 exhibit slower growth than founder (p<0.01). (h) Shows growth rates for strains isolated from minimal medium selection experiment. Four replicate measurements were made for founder and round 10 and three replicate measurements for round 5. Squares and circles demarcate measurements made on separate days. Rounds 5 and 10 have higher growth rates than founder (p<10-5).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (left) Bright-field image at 20$\times$ magnification of the PDMS microfluidic chamber used to trap single bacteria.The boundary of the chamber can be seen as the high contrast circle. Scale bar is 50 μm. (right) A segmented trajectory of a single cell in a chamber like the one shown on the left. Dots indicate locations of the centroid. Black portions indicate running events and red portions tumbles. Image processing and run-tumble detection are described in the Materials and methods section of the main text.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Tumble durations ($\tau_{t}$) and run lengths ($l_{r}$) for single-cell tracking shown in Figure 3 of the main text. (a) Shows the complementary cumulative distribution of tumble durations for rich media evolved strains. Shaded regions are 95% confidence intervals from bootstrapping. Averages and standard deviations are: 0.18 $\pm$ 0.20 s, 0.17 $\pm$ 0.16 s, 0.14 $\pm$ 0.13 s, 0.14 $\pm$ 0.12 s for founder, round 5, 10 and 15 respectively. (b) Identical to (a) except constructed for run lengths. The run length is found by computing the arc-length between tumble events for each run. The averages and standard deviations are 13.5 $\pm$ 17.7 μm, 16.5 $\pm$ 17.4 μm, 16.5 $\pm$ 16.0 μm, 19 $\pm$ 17.8 μm respectively. (c) and (d) are identical to (a) and (b) for minimal medium evolved strains (replicate 1, Figure 1e). The tumble durations are 0.17 $\pm$ 0.17 s, 0.25 $\pm$ 0.28 s, 0.20 $\pm$ 0.21 s for founder, round 5 and 10. The respective run lengths are 10.0 $\pm$ 13.0 μm, 5.0 $\pm$ 7.5 μm and 4.6 $\pm$ 4.6 μm.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Single-cell tracking and growth rate measurements were performed on independently selected strains in rich medium (15 rounds, (a–c)) and minimal medium (10 rounds, (d–f)). Panels show run durations (a,d), run speeds (b,e) and growth rates (c,f). The founder population is shown in black in all panels. Single-cell tracking experiments were performed on two additional round 15 strains from the rich medium experiment (replicates 3 and 4, Figure 1c main text). For replicates 1, 3 and 4– 96, 85 and 98 individuals were tracked for a total of 15,928, 16,639 and 18,171 run events respectively. (a) shows the run duration distributions for these three strains with mean $\pm$ standard deviations: 0.65 $\pm$ 0.57 s, 0.60 $\pm$ 0.53 s, 0.57 $\pm$ 0.49 s respectively. (b) Run speed ($|v_{r}|$) distributions for the same three strains with means 28.7 μm s−1, 26.2 μm s−1 and 26.7 μm s−1 respectively. (c) maximum growth rates ($k_{g}$) for the same two independently evolved strains (with 15(3) denoting replicate 3 and 15(4) denoting replicate 4). The decline in growth rate relative to founder is significant for both replicate 3 ($p<10^{−3}$) and replicate 4 ($p<10^{−3}$). (d–f) show swimming statistics and growth rates for independently evolved strains in minimal medium, replicate 1 and 2 correspond to Figure 1e in the main text. (d) Run duration distributions for constructed for 25 individuals from replicate 1 and 80 individuals from replicate 2 corresponding to 4892 and 9357 run events respectively. The mean $\pm$ standard deviations are: 0.33 $\pm$ 0.26 s and 0.65 $\pm$ 0.87 s. (e) Run speed distributions for independently evolved minimal medium strains. Means for replicates 1 and 2 are 13.3 μm s−1 and 15.25 μm s−1 respectively. (f) Growth rates for founder, rounds 5 and 10 reproduced from Figure 1e, main text (circles) along with growth rate measurements for strain isolated from round 5 of replicate 2 (dark red triangles) and round 10 of replicate 2 (light red triangles). Means are 0.3h-1and 0.24h-1 Round 5 growth rates do not differ significantly ($p=0.24$) while round 10 growth rates do ($p<0.02$). Both replicate 2 strains from rounds 5 and 10 exhibit growth rates larger than founder ($p<0.001$).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (a–d) Show swimming statistics ($\tau_{r}$, $\sigma_{\tau_{r}}$, $\tau_{t}$ and $|v_{r}|$) as a function of culture optical density for rich medium founding (black) and evolved (green, round 15, replicate 1). Each point corresponds to a single individual tracked for up to 5 min. 141 individuals were tracked from founder and 96 individuals were tracked from round 15. Trend lines are from non-parametric kernel regressions and shaded regions represent 95% confidence intervals from bootstrapping. The shorter run duration in round 15 is apparent in the reduced $\sigma_{\tau_{r}}$ relative to founder. (e–h) Show identical plots for minimal medium founding (black) strain (38 cells) and evolved (green, 64 cells, round 10 replicate 1).

Figure 3e–f show the probability distributions of run speeds for founding and selected strains in both nutrient conditions. In rich medium we observed a nearly 50% increase in the run speed ($|v_{r}|$) between founder and rounds 10 to 15. Tracking strains isolated after 15 rounds from independent selection experiments (replicates 3 and 4, Figure 1c) showed that this increase in run speed was reproducible across independent evolution experiments (Figure 3—figure supplement 3). Finally, to check that the phenotype we observed after 15 rounds of selection in rich medium was distinct from standard laboratory strains used in chemotaxis studies, we tracked RP437 and found that its swimming speed was slower than the round 15 strain (Figure 1—figure supplement 4).

Surprisingly, when we performed single-cell tracking for strains evolved in minimal media we observed the opposite trend. In these conditions we observed a 50% reduction in run speed (Figure 3f). Again, we found that this result was reproducible across independently evolved strains (Figure 3—figure supplement 3).

While the overall trend in minimal medium was towards reduced run duration, one replicate showed an increase in run duration (Figure 3—figure supplement 3). The strain where we observed long runs after 10 rounds of selection (replicate 2, Figure 1e) also exhibited a slower migration rate than the strain isolated from replicate 1, and the long run durations may be responsible for this difference.

We then measured the growth rates of founding and evolved strains from both selection conditions in well mixed liquid corresponding to the medium used for selection (Appendix 1). We observed a decline of about 10% in the maximum growth rate with selection in rich medium and a three-fold increase in the maximum growth rate after 10 rounds of selection in minimal medium (Figure 3g-h). We found that these changes in growth rate are reproducible across independently evolved strains in both environmental conditions (Figure 3—figure supplement 3).

Since motility is known to depend on the growth history of the population (Staropoli and Alon, 2000), we checked whether the phenotypic differences between founding and evolved strains shown in Figure 3 remained valid when we tracked cells over a range of optical densities during population growth. We performed these measurements for the founding strain in both rich and minimal media, and for a round 15 strain in rich medium and a round 10 strain in minimal medium (Figure 3—figure supplement 4). For both rich and minimal media, we found that the differences in run speed ($|v_{r}|$) between founding and selected strains were retained across the growth curve (Figure 3—figure supplement 4d). Likewise, in minimal medium, the average run duration was shorter for the selected strain than for the founder across the growth curve. For rich medium, average run durations for the round 15 strain were not consistently shorter than founder, but the round 15 strain exhibited smaller variability in run duration (Figure 3—figure supplement 4b).

Combining growth rate measurements with single-cell motility measurements allowed us to predict the front migration rate for strains in rich and minimal media using the reaction-diffusion model described above. We found that the model qualitatively recapitulated the increase in front migration rate that we observed experimentally (Tables 3,4, Figure 4—figure supplement 1).

**Table 3.**
 Reaction-diffusion model parameters estimated from measurements of tumble frequency ($\alpha_{0}$) and run speed ($|v_{r}|$) for rich medium evolved strains in $C=$ 0.3% agar.


<table>
  <thead>
    <tr>
      <th colspan="5">Evolution of population level migration parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>strain</td>
      <td>α0 [s−1]</td>
      <td>|vr| [ μm s−1]</td>
      <td>Db [ cm2h−1]</td>
      <td>k0 [ cm2h−1]</td>
    </tr>
    <tr>
      <td>founder</td>
      <td>1.45</td>
      <td>18.7</td>
      <td>0.02</td>
      <td>0.65</td>
    </tr>
    <tr>
      <td>round 5</td>
      <td>1.56</td>
      <td>24.9</td>
      <td>0.027</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>round 10</td>
      <td>1.72</td>
      <td>27.6</td>
      <td>0.029</td>
      <td>1.04</td>
    </tr>
    <tr>
      <td>round 15</td>
      <td>1.54</td>
      <td>28.7</td>
      <td>0.031</td>
      <td>1.04</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Reaction-diffusion model parameters estimated from measurements of tumble frequency ($\alpha_{0}$) and run speed ($|v_{r}|$) for minimal medium evolved strains in $C=$0.3% agar.


<table>
  <thead>
    <tr>
      <th colspan="5">Evolution of population level migration parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>strain</td>
      <td>α0 [s−1]</td>
      <td>|vr| [ μm s−1]</td>
      <td>Db [ cm2h−1]</td>
      <td>k0 [ cm2h−1]</td>
    </tr>
    <tr>
      <td>founder</td>
      <td>2</td>
      <td>20.7</td>
      <td>0.021</td>
      <td>0.66</td>
    </tr>
    <tr>
      <td>round 5</td>
      <td>2.5</td>
      <td>11.2</td>
      <td>0.011</td>
      <td>0.39</td>
    </tr>
    <tr>
      <td>round 10</td>
      <td>3</td>
      <td>13.3</td>
      <td>0.011</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>

We conclude that there is a trade-off between run speed and growth rate in E. coli which constrains the evolution of faster migration through low viscosity agar. Figure 4, which summarizes this trade-off for both conditions, shows the measured growth rates and swimming speeds for all strains presented in Figure 3 overlaid on the predicted migration rates from our reaction-diffusion model. The curves in Figure 4a–b show that the evolved phenotypes lie near a Pareto frontier in the phenotypic space of run speed and growth rate.

![Figure 4.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig4-v2.jpg)

**Figure 4.:** (a) Shows run speeds and growth rates for strains evolving faster migration in rich medium overlaid on a heatmap of the prediction for front migration rate from the reaction-diffusion model (Figure 2). Phenotypes for strains from Figure 3 are shown along with two independently evolved strains (replicates 3 (15(r3)) and 4 (15(r4)), Figure 1c). In addition, the red ‘x’ marks the phenotype for the mutation clpXE185* in the founding strain background (Figure 5). (b) Shows run speeds and growth rates for strains evolved in minimal medium overlaid on the predicted from migration rate from the reaction-diffusion model. Growth rate and run speed for an independently evolved round 10 strain is shown (10(r2), Figure 1e) as well as the phenotype for the galSL22R mutation in the founder background (black ‘x’). Predicted front migration rates assume no change in run duration.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Using the reaction-diffusion model (Main text), we simulated colony expansion using the parameters shown in Table 1 of the main text.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Run durations ($\tau_{r}$) and speeds ($|v_{r}|$), growth rates ($k_{g}$) and migration rates ($s$) for four mutations reconstructed in the founder background (see Main Text). Three mutants were studied in rich medium (a,c,e,g) - clpXE185, a single base pair deletion at position 523,086 ($Δ$1bp) and the double mutant (clpX$+Δ$ 1 bp). One mutant was studied in minimal medium: galSL22R. In all panels, phenotypes of mutants are compared to founder and the population isolated after the final round of selection in the appropriate environment. (a) shows $c⁢(\tau_{r})$ in rich medium, means and standard deviations are: 0.63 $\pm$ 0.60 s, 0.66 $\pm$ 0.91 s and 0.59 $\pm$ 0.55 s for clpX, $Δ$1 bp and clpX$+Δ$1bp respectively. clpX and clpX$+Δ$1bp have shorter average run durations than founder ($p<10^{−4}$). (b) $c⁢(\tau_{r})$ in minimal medium, where galSL22R exhibits longer runs than founder with 0.55 $\pm$ 0.75 s ($p<10^{−5}$). (c) gives $P⁢(|v_{r}|)$ in rich medium. Means $\pm$ standard deviations are 24.2 $\pm$ 7.8 μm s−1, 18.2 $\pm$ 7.3 μm s−1 and 23.4 $\pm$ 7.6 μm s−1 for clpX, $Δ$1 bp and clpX$+Δ$1bp respectively. All mutants except $Δ$1 bp exhibit faster runs on average ($p<10^{−5}$). (d) gives $P⁢(|v_{r}|)$ in minimal medium. galSL22R has a mean of 17.6 $\pm$ 8.7 μm s−1, which is lower than founder ($p<10^{−5}$). (e) Growth rates for rich medium mutants. clpX and clpX$+Δ$1bp have lower growth rates than founder ($p=0.0087$ and $p=0.0069$). The $Δ$1 bp mutation alone does not have a statistically significant difference in growth rate from founder ($p=0.53$). (f) shows growth rate for the galS mutant relative to founder and round 10. The mutant growth rate is larger than founder ($p<0.001$). (g) shows colony migration rates for mutants in rich medium. clpX and clpX$+Δ$1bp differ significantly from the migration rate of founder ($p=0.0021$ and $p=0.0017$). $Δ$1bp does not have a statistically significant change in migration rate. Comparisons are made between duplicate measurements for each genotype and the migration rates of all five replicate experiments in Figure 1 of the main text. (f) Shows migration rate measurements for the galS mutant in minimal medium compared to founder and round 10 in minimal medium. The mutant is faster than the founding strain ($p<10^{−3}$).

### Parallel genomic evolution drives a trade-off through antagonistic pleiotropy

To investigate the mechanism of the phenotypic evolution and trade-off we observed, we performed whole genome sequencing of populations for the founding strain as well as strains isolated after rounds 5, 10 and 15 in rich medium for four of five selection experiments and rounds 5 and 10 in minimal medium for four of five selection experiments (Materials and methods). Figure 5 shows de novo mutations observed in each strain sequenced. Since we sequenced populations, we report the frequency of each mutation observed (see legend, Figure 5a, middle panel).

![Figure 5.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig5-v2.jpg)

**Figure 5.:** (a) De novo mutations observed in strains isolated after 5, 10 and 15 rounds of selection in rich medium. Abscissa denotes position along the genome. Colors of the markers indicate independently evolved replicates and correspond to traces in Figure 1c. Circles denote single nucleotide polymorphisms (SNP) in coding regions, squares denote intergenic SNPs, and triangles denote larger insertions or deletions. The size of the marker is proportional to the frequency of the mutation in the population. Only mutations with a frequency above 0.2 in the population are shown. Genes of interest are labeled. The operons coding for motility and chemotaxis are near flhD. (b) Identical to (a) but shows de novo mutations for strains evolved in minimal medium. The marker near icd corresponds to multiple SNPs in close proximity to each other. See Tables 5–12 for a list of all mutations observed and details of the sequencing.

In the rich medium experiment we observed parallel evolution across replicate selection experiments, with a mutation in clpX (E185*) and an intergenic single base pair deletion both rising to fixation within approximately 5 rounds of selection. In this condition we observed transient mutations in genes regulating chemotaxis or motility (near flhD, Figure 5a) in two of four replicates.

A previous study showed that mutations in clpX alter flhDC expression and motility (Girgis et al., 2007). We therefore focused attention on the mutation in clpX, which converted position 185 from glutamic acid to a stop codon in the 424 residue ClpX protein. ClpX is the specificity subunit of the ClpX-ClpP serine protease. ClpX forms a homohexamer that consumes ATP to unfold and translocate target proteins to the ClpP peptidase (Baker and Sauer, 2012). The ClpXP protease has many targets in the cell including FlhDC, the master regulator of flagellar biosynthesis (Tomoyasu et al., 2003). We found that this mutation in clpX was at high abundance ($>$70%) in all populations after 5 rounds of selection and fixed by round 10 in all four replicates (Figure 5a).

To determine the phenotypic effects of clpXE185*, we used scarless recombineering to reconstruct this mutation in founding strain genetic background (Kuhlman and Cox, 2010) (Materials and methods). We then performed migration rate, single-cell tracking and growth rate measurements on this strain. We observed a statistically significant increase in migration speed for the clpXE185* mutant (0.39 $\pm$ 0.01 cm h−1, mean and standard error) relative to founder (0.30 $\pm$ 0.01 cm h−1, $p=$0.002). We also found that clpXE185* resulted in a statistically significant increase in run speed relative to founder (24.2 μm s−1 compared to 18.7 μm s−1, p< 10-10). Finally, in well mixed batch culture in rich medium, the clpXE185* mutant exhibited a maximum growth rate $k_{g}=$ 1.19 $\pm$ 0.009 h−1 (standard error for triplicate measurements) with founder exhibiting a maximum growth rate of 1.23 $\pm$ 0.01 h−1 ($p=0.0174$, Figure 4—figure supplement 2). Knocking out clpX from founder resulted in very slow front migration ($s=$ 0.0036 $\pm$ 0.001 cm h-1), suggesting that the stop codon mutation we observe has a more subtle effect on the enzyme’s function than a simple loss of function. Finally, we reconstructed the intergenic single base pair deletion which fixed in all four replicate selection experiments but observed no phenotypic effects of this mutation when placed in the founder or clpXE185* background (Figure 4—figure supplement 2). These results suggest that this intergenic mutation is neutral.

We conclude that the clpX mutation observed in all four replicate experiments drives faster front migration through increasing run speed, despite decreasing growth rate. Since the mutant exhibits both faster swimming and slower growth rate relative to founder we conclude that the trade-off between growth rate and swimming speed is driven by antagonistic pleiotropy (Cooper and Lenski, 2000).

Figure 5b shows the mutations observed in rounds 5 and 10 for four of five replicate selection experiments in minimal medium. In all experiments, we observed mutations in the transcriptional regulator galS which fixed in just five rounds. In one of four experiments, we observed a mutation in the gene encoding the motor protein FliG, otherwise the observed mutations appear to be metabolic in nature. In minimal medium we also observed a substantial number of synonymous mutations rising to fixation (see Table 5–8). The role of these synonymous mutations is not known, but may be due to tRNA pool matching (Stoletzki and Eyre-Walker, 2007).

**Table 5.**
 Minimal medium replicate 1: All mutations detected in rounds 5 and 10 of minimal medium replicate 1. The galSL22R mutation in rounds 5 and 10 was confirmed by Sanger sequencing. See Table 9 caption.


<table>
  <thead>
    <tr>
      <th colspan="3">Minimal medium replicate 1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5, (71×)</td>
      <td>10, (214×)</td>
      <td>round, (coverage)</td>
    </tr>
    <tr>
      <td>1196220, icd H366H,78.4%, 46</td>
      <td>1196220, icd H366H, 100%, 141</td>
      <td rowspan="2">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td>1196232, icd T370T, 71.1%, 34</td>
      <td>1196232, icd T370T, 100%, 101</td>
    </tr>
    <tr>
      <td>1196247, icd L375L, 72.0%, 25</td>
      <td>1196247, icd L375L, 100%, 75</td>
      <td></td>
    </tr>
    <tr>
      <td>1196277, icd N385N, 47.1%, 17</td>
      <td>2015871, fliG V331D, 100%, 111</td>
      <td></td>
    </tr>
    <tr>
      <td>1196280, icd A386A, 47.1%, 17</td>
      <td>2241604, galS L22R, 100%, 184</td>
      <td></td>
    </tr>
    <tr>
      <td>1196283, icd K387K, 47.2%, 17</td>
      <td>2685013, glyA H165H, 100%, 197</td>
      <td></td>
    </tr>
    <tr>
      <td>1196292, icd T390T, 46.2%, 13</td>
      <td>3815859, rph Δ82 bp, 100%, 260</td>
      <td></td>
    </tr>
    <tr>
      <td>1196304, icd E394E, 46.2%, 13</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2015871, fliG V331D, 70.0%, 60</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2241604, galS L22R, 100%, 45</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2685013, glyA H165H, 100%, 62</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Minimal medium replicate 2: All mutations detected in rounds 5 and 10 of minimal medium replicate 2. The galSL22R mutation in rounds 5 and 10 was confirmed by Sanger sequencing. See Table 9 caption.


<table>
  <thead>
    <tr>
      <th colspan="3">Minimal medium replicate 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5, (67×)</td>
      <td>10, (64×)</td>
      <td>round, (coverage)</td>
    </tr>
    <tr>
      <td>2241604, galS L22R, 100%, 70</td>
      <td>1757419, IG +17 bp insertion, 94.9%, 37</td>
      <td rowspan="2">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td>2685013, glyA H165H, 100%, 65</td>
      <td>2241604, galS L22R, 100%, 47</td>
    </tr>
    <tr>
      <td></td>
      <td>2685013, glyA H165H, 100%, 79</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>3815828, IG T→G, 43.5%, 62</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 7.**
 Minimal medium replicate 3: All mutations detected in rounds 5 and 10 of minimal medium replicate 3. See Table 9 caption.


<table>
  <thead>
    <tr>
      <th colspan="3">Minimal medium replicate 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5, (208×)</td>
      <td>10, (229×)</td>
      <td>round, (coverage)</td>
    </tr>
    <tr>
      <td>1291079, rssB A280T, 29.7%, 54</td>
      <td>2241595, galS Δ1bp, 100%, 218</td>
      <td rowspan="2">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td>2241595, galS Δ1bp, 64.7%, 102</td>
      <td>3277264, prlF +CATTCAA insertion, 93.6%, 109</td>
    </tr>
    <tr>
      <td>3762200, rhsA A6A, 23.5%, 181</td>
      <td>3350529, IG T→C, 100%, 117</td>
      <td></td>
    </tr>
    <tr>
      <td>3762212, rhsA G10G, 23.1%, 164</td>
      <td>3762200, rhsA A6A, 45.8%, 320</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>3762212, rhsA G10G, 42.0%, 292</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 8.**
 Minimal medium replicate 4: All mutations detected in rounds 5 and 10 of minimal medium replicate 4. See Table 9 caption.


<table>
  <thead>
    <tr>
      <th colspan="3">Minimal medium replicate 4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5, (256×)</td>
      <td>10, (230×)</td>
      <td>round, (coverage)</td>
    </tr>
    <tr>
      <td>2241232, galS R146L, 72.4%, 274</td>
      <td>2020519, fliM E145K, 100%, 205</td>
      <td rowspan="2">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td></td>
      <td>2241665, galS I2L, 100%, 304</td>
    </tr>
  </tbody>
</table>

To understand how these mutations drive phenotypic evolution, we focused on the galSL22R mutation. galS encodes the transcriptional repressor of the gal regulon. The coding mutation we observe occurs in the highly conserved N-terminal helix-turn-helix DNA binding region of this protein, we therefore expect that this mutation alters the expression of the gal regulon (Weickert and Adhya, 1992). To assay the phenotypic effects of this mutation, we reconstructed it in the genetic background of the founder.

The migration rate of the galSL22R mutant showed a statistically significant increase relative to founder ($s=$ 0.039 $\pm$ 0.001 cm h−1 for galSL22R and 0.0163 $\pm$ 0.0038 cm h−1 for founder, p < 10−3). We found that the growth rate of the mutant was approximately 2.5-fold larger than founder in minimal medium (0.23 $\pm$ 0.005 h−1 for galSL22R and 0.089 $\pm$ 0.03 h−1 for founder, $p=$4×<10−4). Further, this mutation reduced the mean swimming speed relative to founder by approximately 15% (Figure 4b, Figure 4—figure supplement 2). However, when we knock out the galS gene from founder we do not observe a significant increase in the migration rate ($Δ$galS $s=$ 0.0165 $\pm$ 0.002 cm h−1, $p=0.92$).

Therefore, as shown in Figure 4b, we conclude that galSL22R alone drives faster growth and slower swimming. As with the rich medium condition, this trade-off is governed by antagonistic pleiotropy.

### Genetic covariance determines direction of phenotypic evolution

To understand why we observe divergent phenotypic trajectories in the rich and minimal medium conditions (Figure 4a–b), we studied a simple model of the evolution of correlated traits (Lande, 1979; Mezey and Houle, 2005). We consider a vector of the two phenotypes of interest, run speed and maximum growth rate, normalized to the values of the founder (Hansen and Houle, 2008), $ϕ→=[|v~_{r}|,k~_{g}]^{T}$ ($|v~_{r}|=⟨|v_{r}|⟩/⟨|v_{r}|^{f}⟩$, $k~_{g}=⟨k_{g}⟩/⟨k_{g}^{f}⟩$, where $⟨⟩$ denotes an average across the population). The model describes the evolution of the mean phenotype ($ϕ→$) under selection by

$$
ϕ→=G\beta→+ϕ→_{0}
$$

where $G$, the genetic covariance matrix, describes the genetically driven phenotypic covariation in the population, which is assumed to be normally distributed ($𝒩⁢(ϕ→,G)$). $\beta→$ is the selection gradient which captures the change in migration rate with respect to phenotype since we are selecting for faster migration. The matrix $G$ is given by

$$
G=[\sigma_{|v~_{r}|}^{2}ρ⁢\sigma_{|v~_{r}|}⁢\sigma_{k~_{g}}ρ⁢\sigma_{|v~_{r}|}⁢\sigma_{k~_{g}}\sigma_{k~_{g}}^{2}],
$$

where $\sigma_{*~}^{2}$ describes the (fractional) variance in the phenotype due to genetic variation and captures the correlation between the two traits. Therefore, the diagonal elements of $G$ describe the capacity for mutations to vary each trait while the off-diagonal elements describe the capacity for mutations to vary both traits. In our experiment we do not have a direct measurement of $G$. However, we do observe how $ϕ→$ changes over the course of selection, our data suggest that $ρ<0$ and our reaction-diffusion model permits us to estimate how migration rate depends on the two traits of interest. In particular, $\beta→=[\frac{∂log⁡(s)}{∂(|υ_{r}|)},\frac{∂log⁡(s)}{∂k_{g}}]^{T}$.

We approximate $\beta→$ in both rich and minimal media by fitting a plane to the heatmap shown in Figure 2a–b (Appendix 1). The resulting selection gradient is shown in Figure 6—figure supplement 1 for both conditions. Using this formalism, we asked what values of $\sigma_{k~_{g}}$ and $\sigma_{|v~_{r}|}$ would result in the directions of phenotypic evolution we observed experimentally in rich and minimal media.

We found that the direction of phenotypic evolution in rich medium agreed well with our experimental observations so long as σ|υ~r|/σkg~≥1 for ρ<−0.1. This implies that our observed phenotypic evolution is consistent with a genetic variance in run speed that is no smaller than the genetic variance in growth rate (Figure 6—figure supplement 2). In contrast, in minimal medium the model predicts the direction of observed phenotypic evolution only if σ|υ~r|/σkg~≲0.3 for ρ<−0.1. This result indicates that our observed phenotypic evolution is consistent with at least three-fold larger propensity for mutations to alter growth rate compared to run speed in minimal medium (Figure 6—figure supplement 2). Figure 6 shows these geometric relationships between selection, genetic covariance and phenotypic evolution.

![Figure 6.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig6-v2.jpg)

**Figure 6.:** The evolutionary model describes the change in phenotype relative to the founder ($ϕ→=[|v~_{r}|,k~_{g}]^{T}$) under selection described by $\beta→$. Panels show unit vectors in the direction of observed phenotypic evolution ($ϕ^$) and the direction of selection inferred from the reaction-diffusion model ($\beta^$). Ellipses show quartiles for a normal distribution of phenotypes with covariance matrix $G$ that is consistent with $ϕ→$ and $\beta→$. In both panels, we set the correlation coefficient between $k~_{g}$ and $|v~_{r}|$ is $ρ=−0.75$ but our conclusions hold for $ρ<−0.1$. In rich medium (a) $\sigma_{|v~_{r}|}/\sigma_{k~_{g}}=1$ and in minimal medium $\sigma_{|v~_{r}|}/\sigma_{k~_{g}}=0.3$. In rich medium $\beta^_{R⁢M}=[0.78,0.61]$ and in minimal medium $\beta^_{M⁢M}=[0.87,0.49]$.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Determining $\beta→$ from reaction-diffusion model.Reaction-diffusion model (main text) was used to simulate migration rates. Panels (a) and (b) plot the normalized (to the founder) predicted migration rate ($s~$) for both rich medium (a) and minimal medium (b). (a–b) are surface plots of the heatmaps shown in Figures 2,4 of the main text. To infer the selection pressure $(\beta→)$ we fit a plane (black circles) to the surfaces shown in (a) and (b). The residuals of this fit are shown in (c) and (d) respectively. The fit for rich medium is good, while the residual is large in minimal medium.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Direction of phenotypic evolution with $\sigma_{|v~_{r}|}$ and $\sigma_{k~_{g}}$.The dot product $ϕ^_{o⁢b⁢s}⋅ϕ^_{p⁢r⁢e⁢d}$ is plotted as a heatmap as a function of genetic variances in growth rate and run speed. Each row corresponds to a different value of the correlation coefficient ($ρ$) between run speed and growth rate as labeled. The left column is for rich medium and the right column for minimal medium. When $ϕ^_{o⁢b⁢s}⋅ϕ^_{p⁢r⁢e⁢d}→1$ (dark red) this indicates regions where the predicted direction of evolution ($ϕ^_{p⁢r⁢e⁢d}$) coincides with the observed direction of evolution ($ϕ^_{o⁢b⁢s}$). Note our qualitative conclusions are robust to large variation in $ρ$.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/24669/elife-24669-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Stochastic simulations of phenotypic evolution in minimal medium. Simulations were carried out as described above. For all simulations $\sigma_{|v~_{r}|}=0.1$. Each colored line represents a single simulation which initiates at $[1,1]$. Each point is the mean phenotype for a round of selection. Colors represent different values of $\sigma_{k~_{g}}$ as shown in the legends. The green-yellow heatmap is the ‘fitness landscape’ interpolated from the heatmap shown in Figure 2b of the main text. Each panel shows a simulation for different, fixed, values of the trait correlation coefficient $ρ$. The red line and circles show the observed phenotypic evolution in minimal medium (Figure 4b, main text).

This suggests that the capacity of mutations to alter run speed or growth rate relative to founder depends on the nutrient conditions and that changes in this capacity qualitatively alter the direction of evolution along a Pareto frontier (Shoval et al., 2012). This result captures the intuition that mutations that can increase growth rate in rich medium are few while in minimal medium the propensity for mutations increasing growth rate is substantially larger. The model presented here relies on a linear approximation to $\beta→$ , which is a good assumption for rich medium but not for minimal medium, where the dependence of $s$ on $|υ_{r}|$ and $k_{g}$ is strongly nonlinear. Using simulations of the evolutionary process described by Equation 3 , we relaxed the assumption of linearity in the selection coefficient and found that our qualitative conclusions were not altered (Figure 6—figure supplement 3).

We note that the structure of $G$ inferred above reflects the capacity for mutations to change phenotypes at the outset of the experiment. As evolution proceeds in rich medium, we observe a saturation in both run speed and growth rate (Figure 4a), suggesting that further variation is constrained, either genetically or through biophysical constraints on swimming speed. Similarly, in minimal medium, saturation in the growth rate occurs after 5 rounds of selection, suggesting that mutations to further improve growth rate are either not available or fundamental constraints on growth inhibit further increases (Scott et al., 2010).

## Discussion

The most striking observation of our study is the divergent trajectories of phenotypic evolution shown in Figure 4a–b. This observation shows that the evolution of faster migration results in environmentally dependent phenotypic outcomes. This result has important implications for interpreting phenotypic variation in natural populations.

When trade-offs are observed in wild populations, it is sometimes proposed that phenotypes at the extrema of a Pareto frontier reflect the outcome of selection for a specific task (Shoval et al., 2012). Our study shows that when selection pressures place demands on multiple traits simultaneously, evolution along the frontier can reflect differing genetic capacity for adaptation of each phenotype rather than simply the fitness benefit of improving each trait. This result suggests a cautious approach to interpreting phenotypes in nature, where selection pressures and mechanisms constraining phenotypes are often not known (Gould and Lewontin, 1979).

Our results point to the potential predictive power of determining the directions in phenotype space in which genetic variation can most readily change phenotypes – so called, ‘genetic lines of least resistance’ (Schluter, 1996). These directions may be related to genetic regulatory architecture. The mutations we observe in both rich and minimal media alter negative regulators (a protease in the case of clpX and a transcriptional repressor in the case of galS). This supports the hypothesis that microevolution is dominated by the disruption of negative regulation (Lind et al., 2015) and suggests that the direction of phenotypic evolution can be predicted by determining where negative regulatory elements reside in genetic and proteomic networks. The mutations we examined appear to be more subtle than simple loss of function, since knockout mutants for both clpX and galS do not exhibit fast migration, therefore a detailed understanding of how mutations disrupt negative regulation will be essential.

Previous experimental evolution studies have revealed a similar trade-off to the one presented here. Comparing the results of these studies to our own demonstrates the impact of how selection is performed on the phenotypic outcomes. For example, Yi and Dean, 2016 selected E. coli alternately for growth in well mixed conditions and chemotaxis using a capillary assay and observed a trade-off between growth rate and swimming speed which was circumvented by phenotypic plasticity. We observe no evolution beyond the Pareto frontier in our study, possibly because our conditions simultaneously select for growth and motility rather than alternating between selection pressures. This suggests that evolutionarily persistent trade-offs may reflect selection pressures that occur simultaneously in nature. In addition, van Ditmarsch et al. (2013) and Deforet et al. (2014) select Pseudomonas aeruginosa for a hyperswarming phenotype on hard agar. Rather than sampling from the population at a specific location in a swarming colony, they allow the population to swarm for a fixed time interval, remove the entire colony from the plate and inoculate a second plate from a mixed sample of the entire colony. This procedure likely selects both for swarming speed and for growth in the bulk of the colony. Phenotypically, hyperswarmers selected in this way exhibit a decline in growth rate and swimming speed in liquid and a deficit in biofilm formation (van Ditmarsch et al., 2013; Deforet et al., 2014). In light of our study, these results suggest that evolved phenotypes can depend on whether selection occurs at well defined spatial locations in a structured population (e.g. migrating fronts) or through periodic removal of spatial structure. A more precise understanding of the selection pressure applied by van Ditmarsch et al. might emerge from the application of Lande’s (Lande, 1979) formalism to the observed genetic and phenotypic variation.

Interestingly, both Yi and Dean (2016) and van Ditmarsch et al. (2013) observe mutations that alter regulation of motility and chemotaxis genes. None of the mutations observed in our experiment were found by Yi and Dean, despite evolution along similar Pareto frontiers. This suggests that determining the allowed directions of phenotypic variation may be a more powerful approach to predicting evolution than cataloging mutations alone.

The mechanism of the trade-off between growth rate and swimming speed has, to our knowledge, not been determined. However, over-expression of motility operons could drive the reductions in growth rate we observe in rich medium. Subsequent increases in speed could then arise passively from reductions in cell size which reduce hydrodynamic drag (Taheri-Araghi et al., 2015). Similarly, increases in growth rate in minimal medium should increase cell size and hydrodynamic drag. Using the data of Taheri-Araghi et al. (2015), we estimated changes in cell size due to measured changes in growth rate for populations evolved in rich and minimal medium. We could not account for the large change in swimming speed we observe through growth rate mediated changes in cell size alone (Appendix 1). Since we have not measured cell size directly, we cannot conclusively rule out this mechanism. To definitively characterize the mechanism of this trade-off will require measurements of cell size, gene expression, flagellar length and proton motive force.

Our study shows how evolutionary dynamics are defined by the complex interplay between genetic architecture, phenotypic constraints and the environment. Our hope is that a general approach to predicting evolution can emerge from a more complete understanding of this interplay.

## Materials and methods

### Motility selection

#### Rich medium

10 μL of motile E. coli (strain MG1655-motile, Coli Genetic Stock Center (CGSC) #8237) from an overnight LB culture was injected at the center of a 0.3 % w/v agar 15 cm diameter plate containing LB. Images were acquired every minute via webcams (Logitech HD Pro Webcam C920, Logitech, Lausanne, Switzerland) in a dark box using pulsed illumination provided by an LED light strip (part number: COM-12021, Sparkfun Inc, Nilwot, CO). Only the Red and Green LEDs of the RGB strip were used in order to avoid blue light response known to occur in E. coli (Taylor and Koshland, 1975). After 12 hr, 50 μL of cells was removed from each of eight points around the outermost ring. This sample was briefly vortexed and 10 μL ($≈10^{6}$ cells) was injected into a fresh plate from the same batch. Remaining bacteria were preserved at −80°C in 25% glycerol. Selection was performed by repeating this sampling and growth over 15 rounds. Automated image processing then yielded quantitative data about front speed. All experiments were performed at 30°C in an environmental chamber (Darwin Chambers, St. Louis, MO). Plates were allowed to equilibrate for 12 hr at 30°C in the environmental chamber before use. All plates for a single selection replicate were poured from a single media bottle. Plates were allowed to cool, parafilmed and stored at 4°C until use.

To estimate the number of generations that occur during each round of selection, we inoculated an agar plate from a culture of the founding strain. We then measured the cell density of the inoculum by serial dilution and plating. We permitted the colony to expand for 12 hr. To measure the total population on the plate after growth, we mixed the entire contents of the plate in a beaker and measured the density by serial dilution and plating again. From this we extracted an estimate of the number of generations that occurred. The range reflects errors due to serial dilution and plating and the difference in colony size during selection.

#### Minimal medium

Selection experiment was performed identically to rich medium experiment with the following modifications. Plates were made with M63 0.18 mM galactose. Cultures used to initiate selection were grown in M63 30 mM galactose for 24 to 48 hr prior to initiating selection. During each 48 hr round of migration and imaging, plates were housed in a plexiglass box with a beaker of water to prevent evaporative losses from the plate. Images were acquired every 2 min. We estimated the number of generations per round as described above. Reliable plate counts were only obtained for plates of round 10 strains where we estimate 10 generations per round. We therefore take this as an upper bound and conclude that the 10 round selection experiment includes <100 generations. Plates were thermalized for 24 hr before use.

The $Δ$cheA-Z mutant was constructed via P1 transduction from a strain provided by the group of Chris Rao and the mutation was confirmed by PCR. This mutant lacks the receptors tar and tap and the chemotaxis genes cheAWRBYZ.

We selected the motile MG1655 wild-type strain for these experiments rather than the more commonly used RP437 strain since the latter is auxotrophic for several amino acids. Minimal medium experiments were therefore performed without additional amino acids which could confound results.

### Image analysis

Webcam acquired images of migrating fronts were analyzed by custom written software (Matlab, Mathworks, Natick, MA). A background image was constructed by median projecting six images from the beginning of the acquisition before significant growth had occurred. This image was subtracted from all subsequent images prior to further analysis. The location of the center of the colony was determined by first finding the edges of the colony using a Canny edge detection algorithm. A circular Hough transform (Hough, 1959) was applied to the resulting binary image to locate the center. In rich medium, where signal to background was $>10$, radial profiles of image intensity were measured from this center location and were not averaged azimuthally due to small departures from circularity in the colony. The location of the front was determined by finding the outermost peak in radial intensity profiles. Migration rate was determined by linear regression on the front location in time. Imaging was calibrated by imaging a test target to determine the number of pixels per centimeter. The results of the calibration did not depend on the location of the test target in the field of view. In minimal medium, where the signal to background is reduced due to low cell densities, background subtraction was employed as described above but radial density profiles were not always reliable for locating the front. Instead, a circular Hough transform was applied to each image to locate the front at each point in time.

### Single-cell tracking

Single-layer microfluidic devices were constructed from polydimethyl-siloxane (PDMS) using standard soft-lithography techniques, (Quake and Scherer, 2000) following a design similar to the one used previously (Jordan et al., 2013), and were bonded to coverslips by oxygen plasma treatment (Harrick plasma bonder, Harrick Plasma, Ithaca, NY). Bonded devices formed a circular chamber of diameter 200 μm and depth 10 μm (Figure 3—figure supplement 1). Devices were soaked in the medium used for tracking (LB for rich medium strains, M63 0.18 mM galactose for minimal medium strains) with 1% Bovine Serum Albumin (BSA) for at least 1 hr before cells were loaded. Bacteria were inoculated directly from frozen stocks into medium containing 0.1% BSA in a custom continuous culture device. BSA was necessary to minimize cells adhering to the glass cover slip. For rich medium tracking experiments, cells grew to a target optical density and the continuous culture device was run as a turbidostat. In minimal medium experiments the device was run as a chemostat at an optical density of $∼$0.15. The culture was stirred by a magnetic stir bar at 775 RPM and the temperature was maintained at 29.75°C by feedback.

To perform single-cell tracking, cells were sampled from the continuous-culture device and diluted appropriately (to trap one cell in the chamber at a time) before being pumped into the microfluidic chamber. Video was acquired at 30 frames per second with a Point Grey model FL3-U3-32S2M-CS camera (Point Grey, Richmond, Canada) and a bright-field microscope (Omano OM900-T inverted) at 20x magnification. Movies were recorded for 5 min before a new cell was loaded into the chamber. An example movie is available at https://doi.org/10.13012/B2IDB-4912922_V2. Two microscopes were operated in parallel. The stock microscope light source was replaced by a high-brightness white LED (07040-PW740-L, LED Supply, Randolf, VT) to avoid 60 Hz flickering that was observed with the stock halogen light source. All experiments were performed in an environmental chamber maintained at 30°C.

Movies were segmented and tracked with custom written Matlab routines described previously (Jordan et al., 2013; Jaqaman et al., 2008). Code is available at https://github.com/dfraebel/CellTracking (Mickalide et al., 2017; copy archived at https://github.com/elifesciences-publications/CellTracking). At times when two individuals are present in the chamber, ambiguous crossing events can lead to loss of individual identities. All crossing events were inspected manually to prevent this. To identify runs and tumbles, we utilized a method based on reference (Taute et al., 2015) which was modified from the approach used by Berg and Brown (1972). Briefly, for each cell the segmentation routine results in a matrix of spatial locations $x→⁢(t)$. We compute the velocity by the method of central differences resulting in $v→⁢(t)$ from which we compute an angular velocity between adjacent velocity vectors ($\omega⁢(t)$). We then define $\alpha$, a threshold on $\omega$. Tumbles are initiated if $\omega⁢(t)$ & $\omega(t+1)>\alpha$ or if $\omega⁢(t)>\alpha$ and the angle defined between the vectors $x→⁢(t-2)-x→⁢(t)$ and $x→(t)−x→(t+2)$ is greater than $\alpha$. The latter condition detects tumbles that occur on the timescale of the imaging (0.033 s). Runs are initiated only when $\omega⁢(t)$ & $\omega(t+1)$& $\omega(t+2)<\alpha$. As a result, tumbles can be instantaneous and runs are a minimum of four frames. $\alpha$ was determined dynamically for each individual by initializing $\alpha_{0}$ and then detecting all runs for a cell. A new $\alpha_{i}=c\timesmedian(\omega_{runs})$ was computed with $c$ a constant and $\omega_{r⁢u⁢n⁢s}$ is the angular velocity during runs. The process was iterated ten times but typically converged to a final $\alpha_{f}$ in less than five iterations. $c=5$ was determined by visual inspection of resulting classified trajectories. Approximately, 1% of cells exhibited sustained tumbling and had average tumble durations greater than 0.4 s and were excluded from further analysis.

We only considered run events that were in the bulk of the chamber and were not interrupted by interactions with the circular boundary of the chamber. We computed tumble bias by measuring the total time spent tumbling when the cell was not interacting with the chamber boundaries. Tumble frequency was computed by counting the number of tumble events that occurred in the bulk of the chamber and dividing by the total time the cells spent swimming in the bulk. Tumble bias and frequency were computed for each individual over the duration tracked. Averages across individuals are reported in Figure 3c–d.

Due to interactions with the chamber floor and ceiling (boundaries perpendicular to the optical axis), we intermittently observed cells circling. We developed a method to detect this behavior automatically and found that our results are unchanged when we consider individuals that are not interacting with the chamber boundaries (Appendix 1). Data presented in the main text excludes cells determined to be circling.

### Whole genome sequencing and analysis

Whole genome sequencing was performed using the Illumina platform with slight variations between four independent runs. For all sequencing, cultures were grown by inoculating fresh medium from frozen stocks isolated during the course of selection and growing to saturation at 30°C. For sequencing of rich medium strains from replicate 1, DNA was extracted and purified using a Bioo Scientific NEXTprep-Bacteria DNA Isolation Kit. Libraries were prepared from these strains with the Kapa HyperLibrary Preparation kit (Kapa Biosystems, Wilmington MA), pooled and quantified by qPCR and sequenced for 101 cycles from each of the fragments on a HiSeq 2500 (Illumina, San Diego, CA). This HiSeq run was performed by the Biotechnology Core Facility at the University of Illinois at Urbana-Champaign and included additional strains not presented here. All other sequencing was performed on a locally operated and maintained Illumina MiSeq system.

For MiSeq runs which generated data for all minimal medium evolved strains and replicates 2 to 4 of the rich medium selection experiments, DNA was extracted with either the Bioo Scientific NEXTprep kit or the MoBio Ultraclean Microbial DNA isolation kit. Different isolation kits were used due to the discontinuation of the Bioo Scientific kit. DNA was quantified by Qubit and Bioanalyzer and libraries were prepared using the NexteraXT kit from Illumina.

Sequencing adapters for the HiSeq generated data were trimmed using flexbar (http://sourceforge.net/projects/flexbar/). MiSeq runs were demultiplexed and trimmed using the onboard Illumina software. Analysis was performed using the breseq platform http://barricklab.org/twiki/bin/view/Lab/ToolsBacterialGenomeResequencing in polymorphism mode. Breseq uses an empirical error model and a Bayesian variant caller to predict polymorphisms at the nucleotide level. The algorithm uses a threshold on the empirical error estimate (E-value) to call variants (Barrick and Lenski, 2009). The value for this threshold used here was 0.01, and at this threshold, with the sequencing coverage for our samples, we report all variants present in the population at a frequency of 0.2 or above (Barrick and Lenski, 2009). All other parameters were set to their default values. Reads were aligned to the MG1655 genome (INSDC U00096.3). We note that breseq is not well suited to predicting large structural variation. Since we sequence populations at different points during selection, observation of the same mutations at different points in time significantly reduces the probability of false positives (Lang et al., 2013).

The founder strain was sequenced at an average depth of 553× when aggregating reads from four separate sequencing reactions. Any mutations observed in this strain were excluded from further analysis. Tables 5–12 document mutations, important mutations were confirmed by Sanger sequencing as noted in the captions to these tables. Since these genomes were sequenced at very high depth, we did not confirm every mutation by Sanger sequencing. All mutation calls made by breseq were inspected manually and found to be robust or they were excluded. We also manually inspected the founder strain reads aligned to regions where frequent mutations were observed in the evolved strains (clpX E185*, the Δ1 bp mutation at position 523086 and galS L22R) to confirm that those mutations were not present in the founder. Sequencing data are available at https://doi.org/10.13012/B2IDB-3958294_V1.

**Table 9.**
 Rich medium replicate 1: All mutations detected above a frequency of 0.2 in rounds 5, 10 and 15 of rich medium selection replicate 1. The first number in each cell denotes the distance in base pairs from ori (location). The second entry (mutation) identifies the mutations with ‘IG’ denoting an intergenic mutation. The third entry (fraction) is the fraction of the population carrying this mutation (as inferred by breseq in polymorphism mode). The fourth entry (coverage) is the number of reads that aligned to this location. In the round 15 strain, the clpX SNP and $Δ$1 bp deletion at position 523,086 were confirmed by Sanger sequencing.


<table>
  <thead>
    <tr>
      <th colspan="4">Rich medium replicate 1</th>
    </tr>
    <tr>
      <th>Round, (coverage)</th>
      <th>5, (172×)</th>
      <th>10, (213×)</th>
      <th>15, (180×)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>457978, clpX E185*, 75.2%, 179</td>
      <td>457978, clpX E185*, 100%, 199</td>
      <td>457978, clpX E185*, 100%, 164</td>
      <td rowspan="2">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td>523086, IG Δ1 bp, 100%, 194</td>
      <td>523086, IG Δ1 bp, 100%, 266</td>
      <td>523086, IG Δ1 bp, 100%, 168</td>
    </tr>
    <tr>
      <td>950518, pflA T188I, 22.2%, 144</td>
      <td>990379, IG A→C, 100%, 201</td>
      <td>663115, dacA Δ1 bp, 100%, 150</td>
      <td></td>
    </tr>
    <tr>
      <td>1978458, IG G→T, 21.2%, 156</td>
      <td></td>
      <td>990379, IG A→C, 100%, 156</td>
      <td></td>
    </tr>
    <tr>
      <td>3618863, nikR H92H, 20.7%, 189</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 10.**
 Rich medium replicate 2: All mutations detected in rounds 5, 10 and 15 of rich medium replicate 2. See Table 9 caption. Note low coverage on $Δ$1 bp mutation at 523086 noted in bold.


<table>
  <thead>
    <tr>
      <th colspan="4">Rich medium replicate 2</th>
    </tr>
    <tr>
      <th>Round, (coverage)</th>
      <th>5, (218×)</th>
      <th>10, (100×)</th>
      <th>15, (166×)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>457978, clpX E185*, 100%, 220</td>
      <td>457978, clpX E185*, 100%, 109</td>
      <td>457978, clpX E185*, 100%, 184</td>
      <td rowspan="2">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td>950518, pflA T188I, 27.2%, 210</td>
      <td>523086, IG Δ1 bp, 100%, 16</td>
      <td>523086, IG Δ1 bp, 100%, 24</td>
    </tr>
    <tr>
      <td>523086, IG Δ1 bp, 100%, 10/18</td>
      <td></td>
      <td>667259, mrdA R320H, 39.5%, 159</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>794472, modE L58*, 42.4%, 136</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 11.**
 Rich medium replicate 3: All mutations detected in rounds 5, 10 and 15 of rich medium replicate 3. See Table 9 caption. Note low coverage on $Δ$1 bp mutation at 523086 noted in bold.


<table>
  <thead>
    <tr>
      <th colspan="4">Rich medium replicate 3</th>
    </tr>
    <tr>
      <th>Round, (coverage)</th>
      <th>5, (291×)</th>
      <th>10, (45×)</th>
      <th>15, (186×)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>457978, clpX E185*, 100%, 300</td>
      <td>457978, clpX E185*, 100%, 43</td>
      <td>457978, clpX E185*, 100%, 185</td>
      <td rowspan="2">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td>523086, IG Δ1 bp, 50%, 38</td>
      <td>523086, IG Δ1 bp, 100%, 8</td>
      <td>523086, IG Δ1 bp, 100%, 16</td>
    </tr>
    <tr>
      <td>950518, pflA T188I, 26.3%, 332</td>
      <td>950518, pflA T188I, 53.3%, 53</td>
      <td>950518, pflA T188I, 30.6%, 190</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>321263, IG T→C, 25%, 16</td>
      <td>1968653, cheR Q238K, 29.6%, 190</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>382794, yaiX +9bp insertion, 64%, NA</td>
      <td>382794, yaiX +9bp insertion, 25.8%, NA</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4161562, fabR Δ⁢17bp, 46.2%, 67</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 12.**
 Rich medium replicate 4: All mutations detected in rounds 5, 10 and 15 of rich medium replicate 4. See Table 9 caption. Note low coverage on $Δ$1 bp mutation at 523086 noted in bold.


<table>
  <thead>
    <tr>
      <th colspan="4">Rich medium replicate 4</th>
    </tr>
    <tr>
      <th>Round, (coverage)</th>
      <th>5, (384×)</th>
      <th>10, (555×)</th>
      <th>15, (333×)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>457978, clpX E185*, 100%, 370</td>
      <td>457978, clpX E185*, 100%, 559</td>
      <td>457978, clpX E185*, 100%, 339</td>
      <td rowspan="3">Mutation (loc., mut., frac., cov.)</td>
    </tr>
    <tr>
      <td>523086, IG Δ1 bp, 50%, 72</td>
      <td>523086, IG Δ1 bp, 100%, 34/83</td>
      <td>523086, IG Δ1 bp, 100%, 19/33</td>
    </tr>
    <tr>
      <td>950518, pflA T188I, 31.7%, 446</td>
      <td></td>
      <td>3619915, rhsB W242G, 24.9%, 20</td>
    </tr>
  </tbody>
</table>

### Mutant reconstruction

Knockout mutants ($Δ$clpX, $Δ$galS) were constructed by P1 transduction from KEIO collection mutants (Baba et al., 2006). Mutations were confirmed by PCR. Antibiotic markers were not removed prior to phenotyping.

Three commonly observed single nucleotide polymorphisms (SNPs) observed across evolution experiments were reconstructed in the chromosome of the ancestral background (founder) using a recombineering method presented previously (Kuhlman and Cox, 2010; Tas et al., 2015). These mutations were the clpXE185* mutation, the single base pair deletion between ybbP and rhsD (which we refer to as ‘$Δ⁢1$bp’) and galSL22R. For full details of the recombineering we performed see Appendix 1. Briefly, recombineering proficient cells were prepared by electroporation of the helper plasmid pTKRED (Kuhlman and Cox, 2010) and selection on spectinomycin. A linear ‘landing pad’ fragment consisting of tetA flanked by I-SceI restriction sites and homologies to the desired target site was synthesized from the template plasmid pTKLP-tetA and site specific primers. The landing pad was inserted by electroporation into recombineering proficient cells and transformants were selected by growth on tetracycline. Successful transformants were confirmed by PCR. A second transformation was then performed using a 70 bp oligo containing the desired mutation near the center and flanked by homologies to target the landing pad. Counterselection for successful transformants was performed with NiCl$_{2}$ (6 mM for the ClpX and GalS mutations, 6.5 mM for $Δ$1 bp). Successful recombination at this step resulted in removal of the landing pad and integration of the 70 bp oligo containing the desired mutation. The helper plasmid pTKRED was cured by growth at 42°C and confirmed by verifying spectinomycin susceptibility. The presence of desired mutations in the final constructs was confirmed by Sanger sequencing.

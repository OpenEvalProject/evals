# Mapping transiently formed and sparsely populated conformations on a complex energy landscape

## Authors

- Yong Wang<sup>1</sup> ([ORCID: 0000-0001-9156-0377](https://orcid.org/0000-0001-9156-0377))
- Elena Papaleo<sup>1</sup> ([ORCID: 0000-0002-7376-5894](https://orcid.org/0000-0002-7376-5894))
- Kresten Lindorff-Larsen<sup>1</sup> ([ORCID: 0000-0002-4750-6039](https://orcid.org/0000-0002-4750-6039)) †

### Affiliations

1. Structural Biology and NMR Laboratory, Linderstrøm-Lang Centre for Protein Science, Department of Biology University of Copenhagen Copenhagen Denmark

† Corresponding author

## Abstract

Determining the structures, kinetics, thermodynamics and mechanisms that underlie conformational exchange processes in proteins remains extremely difficult. Only in favourable cases is it possible to provide atomic-level descriptions of sparsely populated and transiently formed alternative conformations. Here we benchmark the ability of enhanced-sampling molecular dynamics simulations to determine the free energy landscape of the L99A cavity mutant of T4 lysozyme. We find that the simulations capture key properties previously measured by NMR relaxation dispersion methods including the structure of a minor conformation, the kinetics and thermodynamics of conformational exchange, and the effect of mutations. We discover a new tunnel that involves the transient exposure towards the solvent of an internal cavity, and show it to be relevant for ligand escape. Together, our results provide a comprehensive view of the structural landscape of a protein, and point forward to studies of conformational exchange in systems that are less characterized experimentally.

## Introduction

Proteins are dynamical entities whose ability to change shape often plays essential roles in their function. From an experimental point of view, intra-basin dynamics is often described via conformational ensembles whereas larger scale (and often slower) motions are characterized as a conformational exchange between distinct conformational states. The latter are often simplified as a two-site exchange process, $G⇌E$, between a highly populated ground (G) state, and a transiently populated minor (or ‘excited’, E) state. While the structure of the ground state may often be determined by conventional structural biology tools, it is very difficult to obtain atomic-level insight into minor conformations due to their transient nature and low populations. As these minor conformations may, however, be critical to protein functions, including protein folding, ligand binding, enzyme catalysis, and signal transduction (Mulder et al., 2001; Tang et al., 2007; Baldwin and Kay, 2009) it is important to be able to characterize them in detail. While it may in certain cases be possible to capture sparsely populated conformations in crystals under perturbed experimental conditions, or to examine their structures by analysis of electron density maps (Fraser et al., 2009), NMR spectroscopy provides unique opportunities to study the dynamical equilibrium between major and minor conformations (Baldwin and Kay, 2009; Sekhar and Kay, 2013) via e.g. chemical-exchange saturation transfer (Vallurupalli et al., 2012), Carr-Purcell-Meiboom-Gill (CPMG) relaxation dispersion (Hansen et al., 2008), or indirectly via paramagnetic relaxation enhancement (Tang et al., 2007) or residual dipolar coupling (Lukin et al., 2003) experiments. In favourable cases such experiments can provide not only thermodynamic and kinetic information (i.e. the population of G and E states and the rate of exchange between them), but also structural information in the form of chemical shifts (CS), that can be used to determine the structure of the transiently populated state (Sekhar and Kay, 2013).

Despite the important developments in NMR described above, it remains very difficult to obtain structural models of minor conformations, and a substantial amount of experiments are required. Further, it is generally not possible to use such experiments to infer the mechanisms of interconversion, and to provide a more global description of the multi-state free energy landscape (Zhuravlev and Papoian, 2010; Wang et al., 2012). In the language of energy landscape theory (Onuchic et al., 1997), free energy basins and their depths control the population and stability of functionally distinct states, while the relative positions of basins and the inter-basin barrier heights determine the kinetics and mechanism of conformational exchange. As a complement to experiments, such functional landscapes can be explored by in silico techniques, such as molecular dynamics (MD) simulations, that may both be used to help interpret experimental data and provide new hypotheses for testing (Karplus and Lavery, 2014; Eaton and Muñoz, 2014). Nevertheless, the general applicability of simulation methods may be limited by both the accuracy of the physical models (i.e. force fields) used to describe the free energy landscape and our ability to sample these efficiently by computation. We therefore set out to benchmark the ability of simulations to determine conformational free energy landscapes.

The L99A variant of lysozyme from the T4 bacteriophage (T4L) has proven an excellent model system to understand protein structure and dynamics. Originally designed a ‘cavity creating’ variant to probe protein stability (Eriksson et al., 1992b) it was also demonstrated that the large (150 Å3) internal cavity can bind hydrophobic ligands such as benzene (Eriksson et al., 1992a; Liu et al., 2009). It was early established that the cavity is inaccessible to solvent in the ground state, but that ligand binding is rapid (Feher et al., 1996), suggesting protein dynamics to play a potential role in the binding process. This posts a long-standing question of how the ligands gain access to the buried cavity (Mulder et al., 2000; López et al., 2013; Merski et al., 2015; Miao et al., 2015).

NMR relaxation dispersion measurements of L99A T4L demonstrated that this variant, but not the wild type protein, displayed conformational exchange on the millisecond timescale between the ground state and a minor state populated at around 3% (at room temperature) (Mulder et al., 2001). Such small populations generally lead only to minimal perturbations of ensemble-averaged experimental quantities making structural studies difficult, and hence it was difficult to probe whether the exchange process indeed allowed for ligand access to the cavity. A series of additional relaxation dispersion experiments, however, made it possible to obtain backbone and side chain CSs of the minor E state of L99A (Mulder et al., 2002; Bouvignies et al., 2011). The backbone CS data were subsequently used as input to a CS-based structure refinement protocol (CS-ROSETTA) to produce a structural model of the E state (ER⁢O⁢S⁢E⁢T⁢T⁢A; Figure 1) of the L99A mutant (Bouvignies et al., 2011). This model was based in part on the crystal structure of the ground state of L99A (referred to in what follows as GX⁢r⁢a⁢y), but perturbing the structure in regions that the experiments demonstrated to undergo conformational change in a way so that the final model (ER⁢O⁢S⁢E⁢T⁢T⁢A) agrees with experiments. The structure was further validated by creating and solving the structure of a triple mutant variant that inverts the populations of the G and E states. The ER⁢O⁢S⁢E⁢T⁢T⁢A structure revealed substantial local rearrangements in T4L L99A, in particular near the cavity which gets filled by the side chain of a phenylalanine at position 114 (F114). Because the cavity is filled and solvent inaccessible in the E-state, the structure did, however, not reveal how ligands might access the cavity.

![Figure 1.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig1-v2.jpg)

**Figure 1.:** The X-ray structure of the G state ($G_{X⁢r⁢a⁢y}$; PDB ID code 3DMV) has a large internal cavity within the core of the C-terminal domain that is able to bind hydrophobic ligands. The structure of the E state ($E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$; PDB ID code 2LC9) was previously determined by CS-ROSETTA using chemical shifts. The G and E states are overall similar, apart from the region surrounding the internal cavity. Comparison of the two structures revealed two remarkable conformational changes from G to E: helix F (denoted as $H_{F}$) rotates and fuses with helix G ($H_{G}$) into a longer helix, and the side chain of phenylalanine at position 114 ($F_{114}$) rotates so as to occupy part of the cavity. As the cavity is inaccessible in both the $G_{X⁢r⁢a⁢y}$ and $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ structures it has been hypothesized that ligand entry occurs via a third ‘cavity open’ state (Merski et al., 2015).

In an attempt to benchmark the ability of simulations to map conformational free energy landscapes, we have here employed a series of in silico experiments designed to probe the structure and dynamics of L99A T4L and have compared the results to NMR measurements. We used enhanced-sampling MD simulations in explicit solvent and with state-of-the-art force fields to map the free-energy landscape including the exchange between the major and minor conformations of the protein. We used a series of recently developed metadynamics methods (Laio and Parrinello, 2002) to sample the conformational exchange process and associated structure and thermodynamics, as well as to determine the kinetics and mechanisms of exchange. We obtained additional insight into the structural dynamics of the E state using simulations that employed the experimental CSs as replica-averaged restraints. Our results provide a coherent picture of the conformational dynamics in L99A and extend the insights obtained from recent simulations of a triple mutant of T4L (Vallurupalli et al., 2016), by providing new information about the mechanisms of exchange and the transient exposure of the internal cavity. Together with previous results for Cyclophilin A (Papaleo et al., 2014) the results described here reiterate how simulation methods have now reached a stage where they can be used to study slow, conformational exchange processes such as those probed by NMR relaxation dispersion even in cases where less information is available from experiments.

## Results and discussion

### Mapping the free-energy landscape

As the average lifetime of the G and E states are on the order of 20–50 ms and 1 ms, respectively (Mulder et al., 2001, 2002; Bouvignies et al., 2011), direct and reversible sampling of the G-E transition at equilibrium would be extremely demanding computationally. Indeed, a recent set of simulations of a triple mutant of T4L, which has a substantially faster kinetics, was able only to observe spontaneous transitions in one direction (Vallurupalli et al., 2016). We therefore resorted to a set of flexible and efficient enhanced sampling methods, collectively known as ‘metadynamics’ (Laio and Parrinello, 2002), that have previously been used in a wide range of applications. In metadynamics simulations, a time-dependent bias is continuously added to the energy surface along a small number of user-defined collective variables (CVs). In this way, sampling is enhanced to reach new regions of conformational space and at the same time allows one to reconstruct the (Boltzmann) free-energy surface. The success of the approach hinges on the ability to find a set of CVs that together describe the slowly varying degrees of freedom and map the important regions of the conformational landscape.

We first performed a set of metadynamics simulations in the well-tempered ensemble (Barducci et al., 2008) using so-called path CVs ($S_{p⁢a⁢t⁢h}$ and $Z_{p⁢a⁢t⁢h}$) (Branduardi et al., 2007; Saladino et al., 2012) with the aid of recently developed adaptive hills to aid in the convergence of the sampling (Branduardi et al., 2012; Dama et al., 2014) (see details in Appendix and Appendix 1—table 1). In short, the $S_{p⁢a⁢t⁢h}$ variable describes the progress of the conformational transition between the $G_{X⁢r⁢a⁢y}$ and $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ structures with additional ‘interpolation’ using an optimal ‘reference’ path in a simplified model (see details in Appendix and Figure 2—figure supplement 1), while $Z_{p⁢a⁢t⁢h}$ measures the distance to this reference path. In this way, the two-dimensional free energy landscape along $S_{p⁢a⁢t⁢h}$ and $Z_{p⁢a⁢t⁢h}$ provides a useful description on conformational exchange between ground and excited states that does not assume that the initial reference path describes perfectly the actual path(s) taken.

Projecting the sampled free energy landscape along Sp⁢a⁢t⁢h (upper panel of Figure 2) reveals a deep, narrow free energy basin around Sp⁢a⁢t⁢h=0.2 (labeled by red sphere and corresponding to the G state), and a broader, shallow free energy basin with Sp⁢a⁢t⁢h ranging from 0.6 to 0.8 (labeled by blue sphere and corresponding to the E state). Additional information is obtained from the two-dimensional landscape (shown as a negative free energy landscape, -F(Sp⁢a⁢t⁢h, Zp⁢a⁢t⁢h), in the lower panel of Figure 2) which reveals a complex and rough landscape with multiple free energy minima (corresponding to mountains in the negative free energy landscape). Subsequently, structural inspection of these minima identified that the conformations in the basins around Sp⁢a⁢t⁢h=0.2 and Sp⁢a⁢t⁢h=0.75 correspond to the structures of GX⁢r⁢a⁢y and ER⁢O⁢S⁢E⁢T⁢T⁢A, respectively.

![Figure 2.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig2-v2.jpg)

**Figure 2.:** In the upper panel, we show the projection of the free energy along $S_{p⁢a⁢t⁢h}$, representing the Boltzmann distribution of the force field employed along the reference path. Differently colored lines represent the free energy profiles obtained at different stages of the simulation, whose total length was 667ns. As the simulation progressed, we rapidly found two distinct free energy basins, and the free energy profile was essentially constant during the last 100 ns of the simulation. Free energy basins around $S_{p⁢a⁢t⁢h}=0.2$ and $S_{p⁢a⁢t⁢h}=0.75$ correspond to the previously determined structures of the G- and E-state, respectively (labelled by red and blue dots, respectively). As discussed further below, the E-state is relatively broad and is here indicated by the thick, dark line with $S_{p⁢a⁢t⁢h}$ ranging from 0.55 to 0.83. In the lower panel, we show the three-dimensional negative free energy landscape, -F($S_{p⁢a⁢t⁢h}$, $Z_{p⁢a⁢t⁢h}$), that reveals a more complex and rough landscape with multiple free energy minima, corresponding to mountains in the negative free energy landscape. An intermediate-state basin around $S_{p⁢a⁢t⁢h}=0.36$ and $Z_{path}=0.05$ nm2, which we denote $I_{0.36}$, is labeled by a yellow dot.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The plot reveals a ‘gullwing’ shape of the matrix of pairwise RMSDs of the frames of the reference path, indicating that frames along the reference path are approximately equidistant. We used 31 structures to discretize the path.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) The two-dimensional free energy surface F($S_{p⁢a⁢t⁢h}$,$Z_{p⁢a⁢t⁢h}$) of L99A sampled by a 667 ns PathMetaD simulation. (B) The two-dimensional free energy surface F($S_{p⁢a⁢t⁢h}$,$Z_{p⁢a⁢t⁢h}$) of the triple mutant sampled by a 961 ns PathMetaD simulation. (C) The free energy profiles as a function of $S_{p⁢a⁢t⁢h}$ of both L99A (black) and the triple mutant (blue).

The broad nature of the free energy landscape in the region of the minor state is consistent with the observation that our MD simulations initiated from $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ display significant conformational fluctuations (RUN20 and RUN22 in Appendix 1—table 1). Furthermore, our metadynamics simulations revealed multiple local free energy minima adjacent to the $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ basin, together composing a wider basin (highlighted by the black curve in Figure 2). Thus, these simulations suggest that the E state displays substantial conformational dynamics, a result corroborated by simulations that have been biased by the experimental data (see section ‘Simulations of the minor state using chemical shift restraints’).

In addition to free-energy minima corresponding to the $G$ and $E$ states, we also found a free energy minimum around $S_{p⁢a⁢t⁢h}=0.36$ and $Z_{path}=0.05$ nm2 (denoted as $I_{0.36}$ and labeled by a yellow sphere in Figure 2) that is located between the G and E states on the one-dimensional free-energy surface. We note, however, that it is difficult to infer dominant reaction pathways from such free energy surfaces, and so from this data alone, we cannot determine whether $I_{0.36}$ occurs as an intermediate in G-E conformational transitions. Indeed, it appears from the two-dimensional surface that there exist multiple possible pathways between G and E, as illustrated by white lines along the mountain ridges of the negative free energy landscape in the lower panel of Figure 2. (We also explored the mechanism of exchange by reconnaissance metadynamics simulations (Tribello et al., 2011), the results of which are described and discussed further below.)

### Effect of mutations on the free energy landscape

Based on the encouraging results above for L99A T4L, we examined whether simulations could also capture the effect of mutations on the free energy landscape. Using Rosetta energy calculations on the $G_{X⁢r⁢a⁢y}$ and $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ structures it was previously demonstrated that two additional mutations, G113A and R119P, when introduced into the L99A background, cause an inversion in the populations of the two states (Bouvignies et al., 2011; Vallurupalli et al., 2016). Indeed, NMR data demonstrated that the triple mutant roughly inverts the populations of the two states so that the minor state structure (of L99A) now dominates (with a 96% population) the triple mutant. We repeated the calculations described above for L99A also for the triple mutant. Remarkably, the free energy profile of the triple mutant obtained using metadynamics simulations reveals a free energy landscape with a dominant minimum around $S_{p⁢a⁢t⁢h}$=0.7 and a higher energy conformation around $S_{p⁢a⁢t⁢h}$=0.15 (Figure 2—figure supplement 2). Thus, like our previous observations for a ‘state-inverting mutation’ in Cyclophilin A (Papaleo et al., 2014), we find here that the force field and the sampling method are sufficiently accurate to capture the effect of point mutations on the free energy landscape. Further, we note that the barrier height for the conformational exchange in the triple mutant is very similar to the value recently estimated using a completely orthogonal approach (Vallurupalli et al., 2016). Finally, we attempted to determine the free energy landscape of the L99A,G113A double mutant, which has roughly equal populations of the two states (Bouvignies et al., 2011), but this simulation did not converge on the simulation timescales at which the two other variants converged.

### Calculating conformational free energies

With a free-energy surface in hand and a method to distinguish G- and E-state conformations, we calculated the free energy difference, Δ⁢G, between the two conformational states, and compared with the experimental values. We divided the global conformational space into two coarse-grained states by defining the separatrix at Sp⁢a⁢t⁢h=0.46 which corresponds to a saddle point on the free energy surface, on the basis of the observations above that the E state is relatively broad. Although a stricter definition of how to divide the reaction coordinate certainly helps the precise calculation, here we just used this simple definition to make an approximate estimation of the free energy difference. Further, since the barrier region is sparsely populated, the exact point of division has only a modest effect on the results. By summing the populations on the two sides of the barrier we calculated Δ⁢G as a function of the simulation time (Figure 3). Initially during the simulations the free energy profile varies substantially (Figure 2) and the free energy difference equally fluctuates. As the simulations converge, however, the free energy difference between the two states stabilize to a value at approximately Δ⁢G=3.5 kcal mol−1 (Figure 3, black line). This value can be compared to the value of 2.1 kcal mol−1 obtained from NMR relaxation dispersion experiments (Mulder et al., 2001), revealing reasonably good, albeit not exact, agreement with the experiments.

![Figure 3.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig3-v2.jpg)

**Figure 3.:** We divided the global conformational space into two coarse-grained states by defining the separatrix at $S_{p⁢a⁢t⁢h}=0.46$ (0.48 for the triple mutant) in the free energy profile (Figure 2—figure supplement 2) which corresponds to a saddle point of the free energy surface, and then estimated the free energy differences between the two states ($Δ⁢G$) from their populations. The time evolution of $Δ⁢G$ of L99A (upper time axis) and the triple mutant (lower axis) are shown as black and blue curves, respectively. The experimentally determined values (2.1 kcal mol−1 for L99A and −1.9 kcal mol−1 for the triple mutant) are shown as yellow lines.

Similar calculations using the simulations of the triple mutant also converge, in this case to about −1.6 kcal mol−1 (Figure 3, blue line), in excellent agreement with the experimental measurement (−1.9 kcal mol−1) (Bouvignies et al., 2011). Combining these two free energy differences we find that the G113A, R119P mutations cause a shift in the G-E free energy of 5.1 kcal mol−1 in simulations compared to 4.0 kcal mol−1 obtained by experiments. Thus, we find that the simulations with reasonably high accuracy are able to capture the thermodynamics of the conformational exchange between the two states. While the generality of such observations will need to be established by additional studies, we note here that comparably good agreement was obtained when estimating the effect of the S99T mutations in Cyclophilin A (Papaleo et al., 2014).

In our previous work on Cyclophilin A (Papaleo et al., 2014) we sampled the conformational exchange using parallel-tempering metadynamics simulations (Bonomi and Parrinello, 2010) using four CVs that we chose to describe the structural differences between the G and E states in that protein. We note here that we also tried a similar approach here but unfortunately failed to observe a complete G-to-E transition, even in a relatively long trajectory of about 1 μs per replica (CVs summarized in Appendix 1—table 2, parameters shown in Appendix 1—table 1). This negative result is likely due to the CVs chosen did not fully capture the relevant, slowly changing degrees of freedom, thus giving rise to insufficient sampling even with the use of a parallel tempering scheme.

### Calculating the rates of conformational exchange

Enhanced-sampling simulations such as those described above provide an effective means of mapping the free-energy landscape and hence the structural and thermodynamic aspects of conformational exchange. While the same free-energy landscape also determines the kinetics and mechanisms of exchange it may be more difficult to extract this information from e.g. path-CV-based metadynamics (PathMetaD) simulations. To examine how well simulations can also be used to determine the rates of the G-to-E transitions, quantities that can also be measured by NMR, we used the recently developed ‘infrequent metadynamics’ method (InMetaD, see details in Appendix) (Tiwary and Parrinello, 2013; Salvalaglio et al., 2014; Tiwary et al., 2015a; 2015b). Briefly described, the approach calculates first-passage times for the conformational change in the presence of a slowly-added bias along a few CVs, here chosen as the path CVs also used to map the landscape. By adding the bias slowly (and with lower amplitude) we aim to avoid biasing the transition-state region and hence to increase the rate only by lowering the barrier height; in this way it is possible to correct the first-passage times for the bias introduced.

Using this approach on L99A T4L we collected 42 and 36 independent trajectories with state-to-state transition starting from either the G state or E state, respectively (Appendix 1—figure 1 and Appendix 1—figure 2 ). The (unbiased) rates that we calculated (Table 1 and Appendix 1—figure 3) are in good agreement with the experimental rates (Mulder et al., 2001; Bouvignies et al., 2011) (within a factor of 10), corresponding to an average error of the barrier height of ∼1 kcal mol−1. We also performed similar calculations for the ‘population-inverting’ triple mutant, where we collected 30 transitions (15 for each direction) using InMetaD simulations. As for L99A, we also here find similarly good agreement with experimental measurements (Vallurupalli et al., 2016) (Table 1 and Appendix 1—figure 4). We estimated the reliability of this computational approach using a Kolmogorov-Smirnov test to examine whether the first-passage times conform to the expected Poisson distribution (Salvalaglio et al., 2014), and indeed the results of this analysis suggest good agreement (Table 1, Appendix 1—figure 5 and Appendix 1—figure 6).

**Table 1.**
 Free energy differences and rates of conformational exchange.


<table>
  <thead>
    <tr>
      <th></th>
      <th>τG→E (ms)</th>
      <th>τE→G (ms)</th>
      <th>Δ⁢G (kcal mol−1)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">L99A</td>
    </tr>
    <tr>
      <td>NMR</td>
      <td>20</td>
      <td>0.7</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td>InMetaD</td>
      <td>175 ± 56</td>
      <td>1.4 ± 0.6</td>
      <td>2.9 ± 0.5</td>
    </tr>
    <tr>
      <td>PathMetaD</td>
      <td></td>
      <td></td>
      <td>3.5</td>
    </tr>
    <tr>
      <td colspan="4">L99A/G113A/R119P</td>
    </tr>
    <tr>
      <td>NMR</td>
      <td>0.2</td>
      <td>4</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <td>InMetaD</td>
      <td>2.0 ± 1.7</td>
      <td>14.3 ± 8.3</td>
      <td>-1.2 ± 1.1</td>
    </tr>
    <tr>
      <td>PathMetaD</td>
      <td></td>
      <td></td>
      <td>-1.6</td>
    </tr>
  </tbody>
</table>

The ability to calculate forward and backward rates between $G$ and $E$ provided us with an alternative and independent means to estimate the free energy difference between the two states (Table 1), and to test the two-state assumption used in the analysis of the experimental NMR data. We therefore calculated the free energy difference from the ratio of the forward and backward reaction rates. The values obtained (2.9$± $0.5 kcal mol−1 and −1.2$± $1.1 kcal mol−1 for L99A and the triple mutant, respectively) are close both to the values obtained above from the equilibrium free energy landscape (3.5 kcal mol−1 and −1.6 kcal mol−1) and experiment (2.1 kcal mol−1 and −1.9 kcal mol−1). In particular, the relatively close agreement between the two independent computational estimates lends credibility both to the free energy landscape and the approach used to estimate the kinetics. The observation that both values for L99A are slightly larger than the experimental number suggests that this discrepancy (ca. 1 kcal mol−1) can likely be explained by remaining force field deficiencies rather than lack of convergence or the computational approach used.

### Simulations of the minor state using chemical shift restraints

While the simulations described above used available structural information of G and E states to guide and enhance conformational sampling, the resulting free energy surfaces represent the Boltzmann distributions of the force field and are not otherwise biased by experimental data. To further refine the structural model of the E state we used the relaxation-dispersion derived CSs that were used to determine of $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ [BMRB (Ulrich et al., 2008) entry 17604] as input to restrained MD simulations. In these simulations, we used the experimental data as a system-specific force field correction to derive an ensemble of conformations that is compatible both with the force field and the CSs. Such replica-averaged simulations use the experimental data in a minimally-biased way that is consistent with the Principle of Maximum Entropy (Pitera and Chodera, 2012; Roux and Weare, 2013; Cavalli et al., 2013; Boomsma et al., 2014).

We performed CS-restrained MD simulations of the $E$ state of L99A averaging the CSs over four replicas. Although the number of replicas is a free parameter, which should in principle be chosen as large as possible, it has been demonstrated that four replicas are sufficient to reproduce the structural heterogeneity accurately (Camilloni et al., 2013) without excessive computational requirements. The agreement between calculated and experimental CSs was quantified by the root-mean-square deviation between the two (Figure 4—figure supplement 1). In particular, it is important not to bias the agreement beyond what can be expected based on the inherent accuracy of the CS prediction methods (we assumed that the error in the experimental CS measurement, even for the $E$ state, is negligible in comparison). Thus, we compared the experimental CS values of the minor state with the values calculated using the $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ structure as input to CamShift (Kohlhoff et al., 2009), Sparta+ (Shen and Bax, 2010) and ShiftX (Neal et al., 2003) (Figure 4—figure supplement 2). The average RMSDs for five measured nuclei ($H_{\alpha}$, $H_{N}$, $N$, $C^{′}$ and $C_{\alpha}$) are 0.2, 0.4, 2.0, 0.8 and 1.1ppm, respectively (Appendix 1—table 1), which are close to the inherent uncertainty of the CS back-calculation, indicating that the level of agreement enforced is reasonable.

To compare the results of these experimentally-biased simulations with the experimentally-unbiased simulations described above, we projected the CS-restrained MD trajectories onto either one (Figure 4) or both (Figure 4—figure supplement 3) of the Sp⁢a⁢t⁢h and Zp⁢a⁢t⁢h variables used in the path-variable-driven simulations (PathMetaD). The distribution of conformations obtained using the E-state CSs as restraints is in good agreement with the broad free energy profile of the E-state obtained in the metadynamics simulations that did not include any experimental restraints. To ensure that this observation is not merely an artifact of both simulations using the same force field (CHARMM22*), we repeated the biased simulations using the Amber ff99SB*-ILDN force field and obtained comparable results. We also verified that the conclusions obtained are reasonably robust to other variables such as the number of replicas and the strength of restraints (Figure 4—figure supplement 4).

![Figure 4.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig4-v2.jpg)

**Figure 4.:** We determined an ensemble of conformations corresponding to the E-state of L99A T4L using replica-averaged CSs as a bias term in our simulations. The distribution of conformations was projected onto the $S_{p⁢a⁢t⁢h}$ variable (orange) and is compared to the free energy profile obtained above from the metadynamics simulations without experimental biases (black line). To ensure that the similar distribution of conformations is not an artifact of using the same force field (CHARMM22*) in both simulations, we repeated the CS-biased simulations using also the Amber ff99SB*-ILDN force field (magenta) and obtained similar results. Finally, we used the ground state CSs of a triple mutant of T4L, which was designed to sample the minor conformation (of L99A) as its major conformation, and also obtained a similar distribution along the $S_{p⁢a⁢t⁢h}$ variable (cyan).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** We calculated the RMSD between the experimental CSs and the values back-calculated by CamShift (Kohlhoff et al., 2009) as implemented in ALMOST (Fu et al., 2014). We projected a 250 ns MD trajectory sampled using the CHARMM22* force field (RUN3 in Appendix 1—table 1) onto the RMSDs. The average RMSDs for the five measured nuclei ($H_{\alpha}$, $H_{N}$, $N$, $C^{′}$ and $C_{\alpha}$) are 0.23 ppm, 0.38 ppm, 1.97 ppm, 0.83 ppm and 1.06 ppm, respectively (Appendix 1—table 2), which are close to the inherent uncertainty of the chemical shift calculation (Figure 4—figure supplement 2). This indicates the simulation yielded an ensemble in good agreement with experiments.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Using $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ as the reference structure, we calculated the chemical shifts using different algorithms and compared the correlation coefficients and RMSD between them.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** The chemical shifts of the E state of L99A (BMRB 17604) were used. (A) The simulation with CHARMM22* force field. (B) The simulation with Amber ff99SB*-ILDN force field.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (A) N = 4, $ϵ_{CS}=24$ KJ · mol−1. (B) N = 2, $ϵ_{CS}=24$ KJ · mol−1. (C) N = 2, $ϵ_{CS}=12$ KJ · mol−1. N refers to the number of replicas that the CS values are averaged over. The CHARMM22* force field was used in these simulations. The results also support the conclusion that the conformational space of the minor (E) state covers a relatively wide set of structures including the $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ structure.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** Chemical shift restraints were from BMRB 17,603 and CHARMM22* force field was used.

As a final and independent test of the structural ensemble of the minor conformation of L99A we used the ground state CSs of the triple mutant (BMRB entry 17603), which corresponds structurally to the E state of L99A, as restraints in replica-averaged CS-biased simulations (Figure 4—figure supplement 5). Although not fully converged, these simulations also cover roughly the same region of conformational space when projected along $S_{p⁢a⁢t⁢h}$ (Figure 4).

Thus, together our different simulations, which employ different force fields, are either unbiased or biased by experimental data, and use either dispersion-derived (L99A) or directly obtained (triple mutant) CS all provide a consistent view of the minor E-state conformation of L99A. We also note that the CS-derived ensembles of the E-state support the way we divided the G- and E-states when calculating conformational free energy differences between the two states.

### Mechanisms of conformational exchange

Having validated that our simulations can provide a relatively accurate description of the structure, thermodynamics and kinetics of conformational exchange we proceeded to explore the molecular mechanism of the G-to-E transitions. We used the recently developed reconnaissance metadynamics approach (Tribello et al., 2010), that was specifically designed to enhance sampling of complicated conformational transitions and has been employed to explore the conformational dynamics of complex systems (Tribello et al., 2011; Söderhjelm et al., 2012).

We performed three independent reconnaissance metadynamics simulations of L99A starting from the G state (summarized in Appendix 1—table 1) using the same geometry-based CVs that we also used in the parallel-tempering simulations described above. We observed complete conformational transitions from the G to E state in the reconnaissance simulations in as little as tens of nanoseconds of simulations (Figure 5—figure supplement 1)— at least 1–2 orders of magnitude faster than standard metadynamics. These G-to-E and E-to-G transitions, although biased by the CVs, provide insight into the potential mechanisms of exchange. To ease comparison with the equilibrium sampling of the free energy landscape we projected these transitions onto the free energy surface F(Sp⁢a⁢t⁢h,Zp⁢a⁢t⁢h) (Figure 5). The results reveal multiple possible routes connecting the G and E states, consistent with the multiple gullies found on the free energy surface (Figure 2). The trajectories also suggested that the G-to-E interconversion can either take place directly without passing the I0.36 state or indirectly via it.

![Figure 5.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig5-v2.jpg)

**Figure 5.:** Trajectories labeled as Trj1 (magenta), Trj2 (blue) and Trj3 (green and orange) are from the simulations RUN10, RUN11 and RUN12 (Appendix 1—table 1), respectively. There are multiple routes connecting the G and E states, whose interconversions can take place directly without passing the $I_{0.36}$ state or indirectly via it.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The state-specific fraction of contacts (Wang et al., 2012), and , were employed to monitor the conformational transitions to G and E state, respectively. Trajectories Trj1, Trj2 and Trj3 are from the simulations RUN10, RUN11 and RUN12 (Appendix 1—table 1), respectively.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Trajectories Trj1 (magenta), Trj2 (blue) and Trj3 (green and orange) are from the simulations RUN10, RUN11 and RUN12 (Appendix 1—table 2), respectively. The steepest descent path (SDP, black) used to define the initial path in PathMetaD is also shown as a reference. To measure the distance between helix F and helix I, and between F144 and helix D, we employed order parameters $R_{H⁢F-H⁢I}$ and $R_{F⁢114-H⁢D}$. is defined as the $C_{\alpha}$ distance between E108 and R137, while $R_{F⁢114-H⁢D}$ is defined as the distance between the $C_{\delta⁢4}$ atom of F114 and the $C_{\alpha}$ atom of Y88.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** The figure suggests in the direct $G⇋E$ transitions (Trj1 and first half of Trj3) F114 can rotate its side chain inside the protein core. In contrast, in the $G⇋I_{0.36}⇋E$ route (Trj2 and second half of Trj3) the side chain of F114, which occupies the cavity in the E state, gets transiently exposed to solvent during the transition.

In the context of coarse-grained kinetic models the results above would suggest at least two possible mechanisms operate in parallel: G⇌E or G⇌I0.36⇌E. Further inspection of the structures along these different kinetics routes (see the trajectories of other order parameters in Figure 5—figure supplement 2 and Videos 1–4) suggested an interesting distinction between the two. In the G⇌I0.36⇌E route the side chain of F114, which occupies the cavity in the E state, gets transiently exposed to solvent during the transition, whereas in the direct G⇌E transitions F114 can rotate its side chain inside the protein core (see also the solvent accessible surface area calculation of F114 in Figure 5—figure supplement 3).

![Video 1.](https://cdn.elifesciences.org/articles/17505/elife-17505-media1.mp4.jpg)

**Video 1.:** The backbone of L99A is represented by white ribbons, Helices E, F and G are highlighted in blue, while F114 is represented by red spheres.

![Video 2.](https://cdn.elifesciences.org/articles/17505/elife-17505-media2.mp4.jpg)

**Video 2.:** The backbone of L99A is represented by white ribbons, Helices E, F and G are highlighted in blue, while F114 is represented by red spheres.

![Video 3.](https://cdn.elifesciences.org/articles/17505/elife-17505-media3.mp4.jpg)

**Video 3.:** The backbone of L99A is represented by white ribbons, Helices E, F and G are highlighted in blue, while F114 is represented by red spheres.

![Video 4.](https://cdn.elifesciences.org/articles/17505/elife-17505-media4.mp4.jpg)

**Video 4.:** The backbone of L99A is represented by white ribbons, Helices E, F and G are highlighted in blue, while F114 is represented by red spheres.

### A potential pathway for ligand binding and escape

As the internal cavity in L99A T4L remains buried in both the G and E states (and indeed occupied by F114 in the E state) it remains unclear how ligands access this internal cavity and how rapid binding and release is achieved. Visual inspection of our trajectories and solvent-accessible surface area analysis revealed structures with transient exposure of the internal cavity towards the solvent. The structures were mostly found in a region of conformational space that mapped onto the I0.36 basin (Figure 2), and the events of that basin mostly took place between 430 ns and 447 ns (see Video 5). Thus, we mapped these structures to the free energy surface (Figure 6—figure supplement 1) and analysed them. Overall, the structure is more similar to the G- than E-state, though is more loosely packed. The similarity to the G-state is compatible with rapid binding and position of F114 in this state.

![Video 5.](https://cdn.elifesciences.org/articles/17505/elife-17505-media5.mp4.jpg)

**Video 5.:** The figure shows the time evolution of the free energy surface as a function of $S_{p⁢a⁢t⁢h}$ and $Z_{p⁢a⁢t⁢h}$ sampled in a 667 ns PathMetaD simulation of L99A.

We used CAVER3 (Chovancova et al., 2012) (see parameters in Appendix 1—table 4) to analyse the structures and found multiple tunnels connecting the cavity with protein surface (Figure 6—figure supplement 1 and 2). The tunnels are relatively narrow with the typical radius of the bottleneck (defined as the narrowest part of a given tunnel) between ∼1 Å − ∼2 Å. We used CAVER Analyst1.0 (Kozlikova et al., 2014) (see details in Appendix and parameters in Appendix 1—table 4) to separate the tunnels into different clusters (Figure 6—figure supplement 3 and Appendix 1—table 5) with the dominant cluster (denoted tunnel#⁢1) having a entrance located at the groove between HF and HI. A typical representative structure of I0.36 is shown in Figure 6A. The radii along the structures in cluster #⁢1 vary, but share an overall shape (Figure 6—figure supplement 1), and we find that the maximal bottleneck radius is ∼2.5 Å, the average bottleneck radius is ∼1.3 Å, and the average length ∼11.2 Å.

![Figure 6.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig6-v2.jpg)

**Figure 6.:** (A) We here highlight the most populated tunnel structure (tunnel$#⁢1$), that has an entrance located at the groove between helix F ($H_{F}$) and helix I ($H_{I}$). Helices E, F and G (blue) and F114 (red) are highlighted. (B) The panel shows a typical path of benzene (magenta) escaping from the cavity of L99A, as seen in ABMD simulations, via a tunnel formed in the same region as tunnel #1 (see also Video 6).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** A transiently formed tunnel from the solvent to the cavity forms in the $I_{0.36}$ state.(A) Typical structures from the $I_{0.36}$ state sampled in the simulation (between 430 ns and 447 ns) are mapped onto the free energy surface, and represented by yellow points. (B) The cavity-related regions (helix E, F and G) are coloured in blue, while F114 is coloured in red. F114 tends to be partially solvent exposed in $I_{0.36}$, resulting in the internal cavity to be open. The tunnel$#⁢1$ connecting the internal cavity and protein surface is coloured in yellow, and has a peanut-shell like shape. (C) shows the radius along the tunnel of structures belong to the cluster of tunnel$#⁢1$. Lines in different colours represent different structures. Grey dotted line represents the average tunnel radius.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Representative structures of the cavity region in the $I_{0.36}$ state.The figure shows six representative structures of the cavity region revealing multiple tunnels that connect the cavity with the protein surface. The different colours correspond to different tunnels observed, and a structure can have different tunnels with different widths present at the same time. The colours represent the relative size with yellow, purple and green corresponding to tunnels of decreasing width.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Tunnel clustering analysis on $I_{0.36}$ state.The clustering of tunnels was performed using the CAVER Analyst software (Kozlikova et al., 2014) and the average-link hierarchical algorithm based on the calculated matrix of pairwise tunnel distances. We found that the most weighted tunnel (denoted as tunnel$#⁢1$) populates $27%$ of the $I_{0.36}$ basin. The second and third tunnels populate 20% and 15%, respectively, but their maximal bottleneck radii are 1.4 and 1.3 Å, in contrast to the maximal bottleneck radius of tunnel#1 of 2.5 Å. (A) Heat map visualization of the tunnel profile of tunnel$#⁢1$. The colour map represents the radius of the tunnel$#⁢1$ along the tunnel length. (B) Average tunnel radius and minimal tunnel radius of individual structures belonging to tunnel$#⁢1$ cluster. Note that the gaps indicate these snapshots do not have tunnels. (C) The tunnel radius as a function of the tunnel index which is ranked by the average radius (R). The second widest tunnel (tunnel$#⁢1$) has the highest population and is highlighted in yellow. (D) A typical structure of $I_{0.36}$ with an open tunnel$#⁢1$. HE, $H_{F}$ and $H_{G}$ are coloured in blue, F114 is coloured in red, and tunnel$#⁢1$ is coloured in yellow. (E) The figure shows the location of an alkylbenzene (magenta) in a crystal structure of L99A T4L (PDB ID: 4W59). The figure further shows (in yellow) the tunnel induced in the structure by the alkyl chain, as revealed by CAVER3 when applied to the structure after removing the ligand. Because the tunnel overlaps with the alkyl chain of the ligand, only the phenyl moiety of the ligand is visible.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/17505/elife-17505-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** The figure shows how ABMD simulations allow us to observe the ligand benzene escape from the internal binding site. We performed two sets of 20 simulations using two different force constants for the ABMD (upper: 50 KJ · mol−1 · nm−2; lower: 20 KJ · mol−1 · nm−2); note also the different time scales on the two plots. The simulations used the RMSD of the ligand to the bound state as the reaction coordinate, but are here shown projected onto the distance between the benzene molecule and the side chain of F114. The three structures in the bottom panel provide representative structures.

Interestingly, a series of structures of L99A were recently described, in which the internal cavity where filled with eight congeneric ligands of increasing size to eventually open the structure size (Merski et al., 2015). We performed a comparable tunnel analysis on those eight ligand-bound structures (PDB ID codes: 4W52 – 4W59), revealing the maximal bottleneck radius of 1.8 Å (bound with n-hexylbenzene, 4W59). Although the size of the tunnel in these X-ray structures is slightly smaller than that in $I_{0.36}$ structures, the location of the tunnel exit is consistent with the dominant tunnel$#⁢1$ in $I_{0.36}$ (Figure 6—figure supplement 3). We note, however, that the tunnels observed in our simulation and in the ligand-induced cavity-open X-ray structure (4W59), are too narrow to allow for unhindered passage of e.g. benzene with its a van der Waals’ width of 3.5 Å (Eriksson et al., 1992a). Thus, we speculate that the transient exposure in $I_{0.36}$ might serve as a possible starting point for ligand (un)binding, which would induce (Koshland, 1958; López et al., 2013; Wang et al., 2012) further the opening of the tunnel.

As an initial step towards characterizing the mechanism of ligand binding and escape we used adiabatic biased molecular dynamics (ABMD) simulations (Marchi and Ballone, 1999; Paci and Karplus, 1999) to study the mechanism of how benzene escapes the internal cavity (see Appendix for details). In ABMD the system is perturbed by a ‘ratcheting potential’, which acts to ‘select’ spontaneous fluctuations towards the ligand-free state. In particular, the biasing potential is zero when the reaction coordinate (here chosen to be the RMSD of the ligand to the cavity-bound state) increases, but provides a penalty for fluctuations that brings the ligand closer to the cavity. In this way, we were able to observe multiple unbinding events in simulations despite the long lifetime (1.2 ms) of the ligand in the cavity. Most of trajectories (15 of the 20 events observed) reveal that benzene escapes from the cavity by following tunnel #⁢1 (Figure 6—figure supplement 4 and Appendix 1—table 6). A typical unbinding path is shown in the right panel of Figure 6 (see also Video 6). Because the ABMD introduces a bias to speed up ligand escape, we ensured that the observed pathway was the same at two different values of the biasing force constants (Figure 6—figure supplement 4 and Appendix 1—table 6). Future work will be aimed to perform a more quantitative analysis of the ligand binding and unbinding kinetics.

![Video 6.](https://cdn.elifesciences.org/articles/17505/elife-17505-media6.mp4.jpg)

**Video 6.:** The backbone of L99A is represented by white ribbons, Helices E, F and G are highlighted in blue, while F114 and benzene are represented by spheres in red and magenta, respectively.

### Conclusions

The ability to change shape is an essential part of the function of many proteins, but it remains difficult to characterize alternative conformations that are only transiently and sparsely populated. We have studied the L99A variant of T4L as a model system that displays a complicated set of dynamical processes which have been characterized in substantial detail. Our results show that modern simulation methods are able to provide insight into such processes, paving the way for future studies for systems that are more difficult to study experimentally.

Using a novel method for defining an initial reference path between two conformations, we were able to sample the free energy landscape described by an accurate molecular force field. In accordance with experiments, the simulations revealed two distinct free energy basins that correspond to the major and minor states found by NMR. Quantification of the free energy difference between the two states demonstrated that the force field is able to describe conformational free energies to an accuracy of about 1 kcal mol−1. This high accuracy is corroborated by previous studies of a different protein, Cyclophilin A, where we also calculated conformational free energies and compared to relaxation dispersion experiments and found very good agreement. For both proteins we were also able to capture and quantify the effect that point mutations have on the equilibrium between the two states, and also here found good agreement with experiments. We note, however, that comparable simulations of the L99A/G113A mutant did not reach convergence.

Moving a step further, we here also calculated the kinetics of conformational exchange using a recently developed metadynamics method. For both the L99A variant and a population-inverting triple mutant we find that the calculated reaction rates are in remarkably good agreement with experiments. The ability to calculate both forward and backward rates provided us with the opportunity to obtain an independent estimate the calculated free energy difference. The finding that the free energy differences estimated in this way (for both L99A and the triple mutant) are close to those estimated from the free energy landscape provides an important validation of both approaches, and we suggest that, when possible, such calculations could be used to supplement conventional free energy estimates.

The free-energy landscape suggested that the E state is relatively broad and contains a wider range of conformations. To validate this observation, we used the same chemical shift information as was used as input to Rosetta and performed replica-averaged CS-restrained simulations. The resulting ensemble demonstrates that the experiments and force field, when used jointly, indeed are compatible with a broader E state. Thus, we suggest that the $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ structure and CS-restrained ensemble jointly describe the structure and dynamics of the E state.

While NMR experiments, in favourable cases, can be used to determine the structure, thermodynamics and kinetics of conformational exchange, a detailed description mechanism of interconversion remains very difficult to probe by experiments. We explored potential mechanisms of conformational exchange between the two states, finding at least two distinct routes. One route involved a direct transition with the central F114 entering the cavity within the protein, whereas a different possible mechanism involves transient partial-loosening of the protein. In both cases, the mechanism differs from the reference path that we used as a guide to map the free energy landscape, demonstrating that high accuracy of the initial guess for a pathway is not absolutely required in the metadynamics simulations, suggesting also the more general applicability of the approach.

Finally, we observed a set of conformations with a transiently opened tunnel that leads from the exterior of the protein to the internal cavity, that is similar to a recently discovered path that is exposed when the cavity is filled by ligands of increasing size. The fact that such a tunnel can be explored even in the absence of ligands suggests that intrinsic protein motions may play an important role in ligand binding, and indeed we observed this path to be dominant in simulations of ligand unbinding.

In total, we present a global view of the many, sometimes coupled, dynamical processes present in a protein. Comparison with a range of experimental observations suggests that the simulations provide a relatively accurate description of the protein, demonstrating how NMR experiments can be used to benchmark quantitatively the ability of simulations to study conformational exchange. We envisage that future studies of this kind, also when less is known about the structure of the alternative states, will help pave the way for using simulations to study the structural dynamics of proteins and how this relates to function.

## Materials and methods

### System preparation

Our simulations were initiated in the experimentally determined structures of the ground state of L99A ($G_{X⁢r⁢a⁢y}$; PDB ID code 3DMV) or minor, E state ($E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$; 2LCB). The structure of the ground state of the L99A, G113A, R119P triple mutant, corresponding to the E state of L99A was taken from PDB entry 2LC9 ($G_{R⁢O⁢S⁢E⁢T⁢T⁢A}^{T⁢r⁢i⁢p⁢l⁢e}$). Details can be found in the Appendix.

### Initial reaction path

Taking $G_{X⁢r⁢a⁢y}$ and $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ as the models of the initial and final structures, we calculated an initial reaction path between them with the MOIL software (Elber et al., 1995), which has been used to explore the mechanism of conformational change of proteins (Wang et al., 2011). Further details can be found in the Appendix and in refs. (Majek et al., 2008; Wang et al., 2011).

### Path CV driven metadynamics simulations with adaptive hills

The adaptive-hill version of metadynamics updates the Gaussian width on the fly according to the local properties of the underlying free-energy surface on the basis of local diffusivity of the CVs or the local geometrical properties. Here, we used the former strategy. Simulation were performed using Gromacs4.6 (Pronk et al., 2013) with the PLUMED2.1 plugin (Tribello et al., 2014). See parameter details in Appendix 1—table 1.

### Replica-averaged CS-restrained simulations

We performed replica-averaged CS restrained MD simulations by using GPU version of Gromacs5 with the PLUMED2.1 and ALMOST2.1 (Fu et al., 2014) plugins. Equilibrated structures of $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ and $G_{R⁢O⁢S⁢E⁢T⁢T⁢A}^{T⁢r⁢i⁢p⁢l⁢e}$ were used as the starting conformations. CS data of $E_{R⁢O⁢S⁢E⁢T⁢T⁢A}$ and $G_{R⁢O⁢S⁢E⁢T⁢T⁢A}^{T⁢r⁢i⁢p⁢l⁢e}$ were obtained from the BMRB database (Ulrich et al., 2008) as entries 17604 and 17603, respectively.

### Reconnaissance metadynamics simulations

Reconnaissance metadynamics (Tribello et al., 2010) uses a combination of a machine learning technique to automatically identify the locations of free energy minima by periodically clustering the trajectory and a dimensional reduction technique that can reduce the landscape complexity. We performed several reconnaissance metadynamics simulations with different combinations of CVs starting from $G_{X⁢r⁢a⁢y}$ using Gromacs4.5.5 with PLUMED1.3 plugin. See parameter details in Appendix 1—table 1.

### Calculating kinetics using infrequent metadynamics

The key idea of infrequent metadynamics is to bias the system with a frequency slower than the barrier crossing time but faster than the slow intra-basin relaxation time, so that the transition state region has a low risk of being substantially biased. As the first transition times should obey Poisson statistics, the reliability of the kinetics estimated from InMetaD can be assessed by a statistical analysis based on the Kolmogorov-Smirnov (KS) test (Salvalaglio et al., 2014). See parameter details on Appendix and Appendix 1—table 1.

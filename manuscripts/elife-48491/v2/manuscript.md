# Efficient conversion of chemical energy into mechanical work by Hsp70 chaperones

## Authors

- Salvatore Assenza<sup>1</sup> ([ORCID: 0000-0001-9983-8927](https://orcid.org/0000-0001-9983-8927))
- Alberto Stefano Sassi<sup>3</sup> ([ORCID: 0000-0002-1269-4746](https://orcid.org/0000-0002-1269-4746))
- Ruth Kellner<sup>5</sup>
- Benjamin Schuler<sup>5</sup> ([ORCID: 0000-0002-5970-4251](https://orcid.org/0000-0002-5970-4251))
- Paolo De Los Rios<sup>3</sup> ([ORCID: 0000-0002-5394-5062](https://orcid.org/0000-0002-5394-5062))
- Alessandro Barducci<sup>8</sup> ([ORCID: 0000-0002-1911-8039](https://orcid.org/0000-0002-1911-8039)) †

### Affiliations

1. Laboratory of Food and Soft Materials ETH Zürich Zürich Switzerland
2. Departmento de Física Teórica de la Materia Condensada Universidad Autónoma de Madrid Madrid Spain
3. Institute of Physics, School of Basic Sciences École Polytechnique Fédérale de Lausanne (EPFL) Lausanne Switzerland
4. IBM TJ Watson Research Center Yorktown Heights New York United States
5. Department of Biochemistry University of Zurich Zurich Switzerland
6. Department of Physics University of Zurich Zurich Switzerland
7. Institute of Bioengineering, School of Life Sciences Ecole Polytechnique Fédérale de Lausanne (EPFL) Lausanne Switzerland
8. Centre de Biochimie Structurale (CBS) INSERM, CNRS, Université de Montpellier Montpellier France

† Corresponding author

## Abstract

Hsp70 molecular chaperones are abundant ATP-dependent nanomachines that actively reshape non-native, misfolded proteins and assist a wide variety of essential cellular processes. Here, we combine complementary theoretical approaches to elucidate the structural and thermodynamic details of the chaperone-induced expansion of a substrate protein, with a particular emphasis on the critical role played by ATP hydrolysis. We first determine the conformational free-energy cost of the substrate expansion due to the binding of multiple chaperones using coarse-grained molecular simulations. We then exploit this result to implement a non-equilibrium rate model which estimates the degree of expansion as a function of the free energy provided by ATP hydrolysis. Our results are in quantitative agreement with recent single-molecule FRET experiments and highlight the stark non-equilibrium nature of the process, showing that Hsp70s are optimized to effectively convert chemical energy into mechanical work close to physiological conditions.

## Introduction

Even though in vitro most proteins can reach their native structure spontaneously (Anfinsen, 1973), this is not always the case in cellular conditions and proteins can populate misfolded states which can form cytotoxic aggregates (Dobson, 2003). In order to counteract misfolding and aggregation, cells employ specialized proteins, called molecular chaperones, which act on non-native protein substrates by processes that stringently depend on ATP hydrolysis for most chaperone families (Hartl, 1996). Among them, the ubiquitous 70 kDa heat-shock proteins (Hsp70s) play a special role because they assist a plethora of fundamental cellular processes beyond prevention of aggregation (Clerico et al., 2019; Rosenzweig et al., 2019).

Decades of biochemical and structural studies have clarified the core elements of the Hsp70 functional cycle at the molecular level (Mayer, 2013). Hsp70s consist of two domains: the substrate binding domain (SBD) interacts with disparate substrate proteins, whereas the nucleotide binding domain (NBD) is responsible for the binding and hydrolysis of ATP. The two domains are allosterically coupled, and the nature of the nucleotide bound to the NBD affects the structure of the SBD and as a consequence the affinity for the substrate and its association/dissociation rates. More precisely, when the chaperone is in the ATP-bound state, the SBD is open and easily accessible to the substrate, whereas the SBD is closed when ADP is bound. These structural differences result in substrate binding and unbinding rates when ATP is bound that are orders of magnitude faster than when ADP is bound (Mayer et al., 2000). Furthermore, the coupling is bidirectional: the substrate, together with a co-localized J-domain protein (JDP) that serves as cochaperone (Kampinga and Craig, 2010; Kampinga et al., 2019), greatly accelerates the hydrolysis of ATP. Substrate binding thus benefits from the fast association rate of the ATP-bound state and the slow dissociation rate of the ADP-bound state, resulting in a non-equilibrium affinity (ultra-affinity) that can be enhanced beyond the maximum limit allowed by thermodynamic equilibrium, namely the affinity of the ADP-bound state (De Los Rios and Barducci, 2014; Barducci and De Los Rios, 2015).

More recently, the consequences of Hsp70 binding on the conformational ensembles of its substrates have also been investigated. Several lines of evidence indicate that the binding of Hsp70s to a polypeptide induces its expansion. Biochemical assays revealed that binding of Hsp70 increases the sensitivity of misfolded Luciferase to proteolysis and decreases its propensity to bind Thioflavin-T, strongly suggesting a loss of compactness (Sharma et al., 2010). Nuclear Magnetic Resonance (NMR) measurements have shown that Hsp70s destabilize the tertiary structure of several different substrates (Lee et al., 2015; Sekhar et al., 2015). Moreover, a single-molecule study based on Förster resonance energy transfer (FRET) spectroscopy quantified the considerable expansion of unfolded rhodanese in native conditions upon binding of multiple Hsp70 chaperones. In particular, this study revealed that the expansion is stringently ATP-dependent, because upon ATP exhaustion the system relaxes to the expansion values observed in the absence of chaperones (Kellner et al., 2014).

Despite these advances in the characterization of Hsp70 functioning, the mechanistic understanding of how the energy of ATP hydrolysis is used to expand a substrate has lagged behind. Our goal here is precisely to fill this gap between the molecular and functional characterization of Hsp70. To this aim, we first explore the structural and energetic features of Hsp70-bound rhodanese using Molecular Dynamics (MD) simulations. We next integrate this molecular information into a rate model that explicitly includes the Hsp70-rhodanese interactions and the chaperone ATPase cycle, thus elucidating how Hsp70s convert the chemical energy of ATP into mechanical work necessary to expand their substrates.

## Results

### Structural and thermodynamic characterization of chaperone-substrate complexes

To characterize the main features of chaperone-induced expansion, we performed MD simulations of the Hsp70/rhodanese complexes. We relied on a one-bead-per-residue Coarse Grained (CG) force field (Smith et al., 2014), which has been tailored to match experimental FRET data of intrinsically disordered proteins and satisfactorily reproduces the compactness of unfolded rhodanese in native conditions without any further tuning (see Materials and methods). Hsp70 chaperones were modeled with a structure-based potential to account for their excluded volume and they were artificially restrained to binding sites on the substrate. We identified six binding sites on the rhodanese sequence using two distinct bioinformatic algorithms (Rüdiger et al., 1997; Van Durme et al., 2009). Considering that each binding site could be either free or bound to a Hsp70 protein, we thus took into account a total of 26 = 64 distinct chaperone/substrate complexes, which were exhaustively simulated. In Figure 1, we report the distributions of the substrate potential energy and of the radius of gyration ($R_{g}$) for three representative complexes with one (left), three (center) and six (right) bound chaperones. Consistently with FRET results (Kellner et al., 2014), chaperone binding leads to larger radii of gyration and higher potential energies, implying that the excluded-volume interactions due to the large Hsp70s progressively expand the complex and disrupt the attractive intra-chain interactions in rhodanese.

![Figure 1.](https://cdn.elifesciences.org/articles/48491/elife-48491-fig1-v2.jpg)

**Figure 1.:** Probability density maps of substrate potential energy and radius of gyration for representative Hsp70/rhodanese complexes with one (left), three (center) and six (right) bound chaperones. The different Hsp70 chaperones have been represented with different colors to ease their discernibility.

We then calculated the conformational free energy of all the possible chaperone/rhodanese complexes to obtain a quantitative picture of the energy landscape governing the chaperone-induced expansion. To this aim, we performed extensive sets of non-equilibrium steering MD trajectories for each complex, and measured the work needed to steer it to a completely extended reference structure ($R_{g}>260$ Å), whose conformational free energy is not affected by chaperone binding. Equilibrium free-energy differences with respect to this reference state were then estimated from non-equilibrium work distributions via the Jarzynski equality (Jarzynski, 1997), thus allowing the determination of the conformational free energy $Δ⁢G$ of each distinct chaperone/substrate complex (see Figure 2—figure supplement 1 and Materials and methods).

In Figure 2 (main), we report $Δ⁢G$ for each complex as a function of its mean radius of gyration using different colors for different stoichiometries. The conformational free energy increased with the swelling of the substrate due to the progressive binding of the chaperones. The increase in substrate potential energy due to the loss of intra-chain interactions upon Hsp70 binding is therefore only marginally compensated by the gain in conformational entropy. Notably, the conformational free energy is not uniquely determined by the stoichiometry, and is significantly affected by the specific binding pattern. The conformational free-energy cost $Δ⁢Δ⁢G$ of adding a single chaperone (inset in Figure 2) is positive for all complexes, but it varies from 2 kcal/mol up to 7 kcal/mol depending on the stoichiometry of the complex and on the particular choice of the binding sites. The increase of $Δ⁢G$ as a function of $R_{g}$ is quantitatively captured by Sanchez (1979) theory for the coil-to-globule collapse transition in polymers (see Figure 2 and Materials and methods). Remarkably, the excellent agreement is not the outcome of a fitting procedure since all the parameters were extracted from experiments (see Appendix 2). This result further reinforces the reliability of our simulations as well as the general applicability of the present setup beyond the particular system considered in this work.

![Figure 2.](https://cdn.elifesciences.org/articles/48491/elife-48491-fig2-v2.jpg)

**Figure 2.:** Conformational free-energy differences $Δ⁢G$ of the Hsp70/rhodanese complexes with respect to the unbound substrate (n = 0) plotted as a function of the corresponding radius of gyration $R_{g}$. Each point represents one of the 64 possible binding configurations with color code indicating the number of bound chaperones. The black curve was obtained using the model in Sanchez (1979) (see Appendix 2). (inset) Distribution of $Δ⁢Δ⁢G$ corresponding to the free-energy cost for binding an additional Hsp70 to a chaperone/substrate complex.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/48491/elife-48491-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Top: representative chaperone/rhodanese complex in the fully-stretched conformation. Bottom: Free-energy difference $\delta⁢G$ between equilibrium conformations and the fully-stretched state for rhodanese (red line) and two representative chaperone/rhodanese complexes. The double arrows indicate the final value of $Δ⁢G$ for the corresponding complex.

### ATP hydrolysis promotes multiple chaperone binding

The structural and thermodynamic characterization obtained by molecular simulations can be profitably complemented by a kinetic model encompassing relevant biochemical processes in order to determine the probability of each chaperone/substrate complex as a function of the chemical conditions. Notably, a model of the Hsp70 biochemical cycle based on experimental rates was previously used to illustrate how ATP-hydrolysis may result into non-equilibrium ultra-affinity for peptide substrates (De Los Rios and Barducci, 2014). Here, we extend this result to the more complex case of Hsp70-induced expansion by taking into account multiple chaperone binding events and their consequences on the conformational free energy of the substrate.

In our model, each state corresponds to a single configuration of the chaperone/substrate complex, which is defined by the occupation state of the six Hsp70 binding sites on rhodanese. Each site can be either free or occupied by an ADP- or ATP-bound chaperone for a total of 36 = 729 different states. All the relevant molecular processes corresponding to transitions between these states are explicitly modeled, including chaperone binding/unbinding, nucleotide exchange and ATP hydrolysis (see Figure 3). We took advantage of available biochemical data for determining the rate constants associated to all the relevant reactions (see Materials and methods). Importantly, kinetic rates for Hsp70 binding were modulated by the conformational free energies determined by CG MD simulations. Indeed, the unbinding rates of Hsp70 from large-sized protein substrates were observed to be similar to the ones from small peptides, whereas the binding rates can be up to two orders of magnitude smaller (Schmid et al., 1994; Mayer et al., 2000; Kellner et al., 2014). This evidence was further corroborated by a recent NMR study (Sekhar et al., 2018) suggesting a conformational selection scenario where the energetic cost due to substrate expansion mostly affects the Hsp70/rhodanese binding rate. Accordingly, we thus considered a substrate-independent unbinding rate constant $k_{o⁢f⁢f}$, while we expressed the binding rate constant as

$$
k_{o⁢n,i⁢j}=k_{o⁢n}^{0}⁢exp⁡[-\beta⁢Δ⁢Δ⁢G_{i⁢j}],
$$

where $\beta=1/k_{B}T$, $k_{B}$ is the Boltzmann constant, T is the absolute temperature, $k_{o⁢n}^{0}$ is the binding rate measured for a peptide substrate, and $Δ⁢Δ⁢G_{i⁢j}$ is the conformational free-energy cost of Hsp70 binding, which depends on the specific initial and final binding patterns $i$ and $j$ in the rhodanese/chaperone complex (see Figure 2, inset). The interactions with JDP cochaperones were not explicitly modeled but the cochaperones were assumed to be colocalized with the substrate, so that their effect was implicitly taken into account in the choice of the rate constants for ATP hydrolysis (Kampinga and Craig, 2010; Hu et al., 2006).

![Figure 3.](https://cdn.elifesciences.org/articles/48491/elife-48491-fig3-v2.jpg)

**Figure 3.:** Each chaperone binding site on rhodanese (black dots) can be either free or occupied by an Hsp70 (yellow), which in turn can be either ADP- or ATP-bound. We depict here for the sake of clarity only a representative portion of the full model, which takes into account six binding sites. The reaction cycle is governed by the rates for chaperone binding/unbinding to the substrate ($k_{o⁢n}^{A⁢T⁢P},k_{o⁢n}^{A⁢D⁢P},k_{o⁢f⁢f}^{A⁢T⁢P},k_{o⁢f⁢f}^{A⁢D⁢P}$) and for hydrolysis ($k_{h}^{s}$), synthesis ($k_{s}^{s}$) and exchange ($k_{e⁢x,D⁢T}^{e⁢f⁢f},k_{e⁢x,T⁢D}^{e⁢f⁢f})$ of nucleotides bound to the chaperones (see Materials and methods for further details). Importantly, the binding rate constants, $k_{o⁢n}^{A⁢T⁢P}$ and $k_{o⁢n}^{A⁢D⁢P}$, take into account the conformational free energies, according to Equation (1).

The analytical solution of the model provides the steady-state probability of each binding configuration and allows the exploration of their dependence on external conditions. It is particularly instructive to investigate the system behavior as a function of the ratio between the concentrations of ATP and ADP, which is intimately connected to the energy released by ATP hydrolysis. At thermodynamic equilibrium, the $[A⁢T⁢P]/[A⁢D⁢P]$ ratio is greatly tilted in favor of ADP ($[A⁢T⁢P]_{e⁢q}/[A⁢D⁢P]_{e⁢q}≃10^{-9}-10^{-8}$; Alberty, 2005), whereas in the cell ATP is maintained in excess over ADP by energy-consuming chemostats ($[A⁢T⁢P]/[A⁢D⁢P]>1$; Milo and Phillips, 2015). The $[A⁢T⁢P]/[A⁢D⁢P]$ ratio hence determines how far the system is from equilibrium, thus representing a natural control parameter for the non-equilibrium biochemical cycle. We thus report in Figure 4 (top panel) the compound probabilities for complexes with the same stoichiometry $n$ as a function of this nucleotide ratio. In conditions close to equilibrium (very low values of $[A⁢T⁢P]/[A⁢D⁢P]$), the vast majority of the substrate proteins are free and only about 10% of them are bound to a single chaperone. The population of equimolar complexes increases for $[A⁢T⁢P]/[A⁢D⁢P]$ between 10−2 and 10−1 and gives way to larger complexes with multiple chaperones for higher values of the nucleotide ratio. For $[A⁢T⁢P]/[A⁢D⁢P]>1$, most substrates are bound to at least 4 chaperones, with an average stoichiometry $⟨n⟩∼4.9$ (solid line in Figure 4), bottom panel). Further increase of the nucleotide ratio does not significantly change this scenario indicating an almost constant behaviour in large excess of ATP $([A⁢T⁢P]/[A⁢D⁢P]>10)$. It is important here to underscore that the binding of the chaperones in these conditions is a non-equilibrium effect, driven by the Hsp70-induced hydrolysis of ATP, and it is not a mere consequence of the excess of ATP over ADP or of the large difference between the substrate association rates to the ATP- and ADP-bound chaperones. Indeed, if we neglect Hsp70 ATPase activity ($k_{h}^{h},k_{s}^{h}=0$) without changing any of the other model parameters, efficient chaperone binding is abolished ($⟨n⟩≪1$, as shown in the bottom panel of Figure 4, dashed line). As a matter of fact, in such equilibrium scenario an excess of ATP over ADP actually slightly disfavors chaperone binding, because the Hsp70 affinity for the substrate is slightly lower in the ATP-bound state than in the ADP-bound state ($k_{o⁢f⁢f}^{A⁢T⁢P}/k_{o⁢n}^{A⁢T⁢P}>k_{o⁢f⁢f}^{A⁢D⁢P}/k_{o⁢n}^{A⁢D⁢P}$, see De Los Rios and Barducci, 2014 for further discussion.)

![Figure 4.](https://cdn.elifesciences.org/articles/48491/elife-48491-fig4-v2.jpg)

**Figure 4.:** (Top) compound probabilities for Hsp70/substrate complexes with given number of bound chaperones $n$ as a function of [ATP]/[ADP]. (Bottom) Mean value $⟨n⟩$ as a function of [ATP]/[ADP] with (solid line) and without (dashed line) ATP hydrolysis.

Combining the steady-state probabilities derived from the rate model with the results of the MD simulations, we can now exhaustively characterize the structural properties of the system. This provides the opportunity to directly compare our model with the results from FRET experiments both in equilibrium and non-equilibrium conditions. To this aim, we first focused on the average radius of gyration of the system at thermodynamic equilibrium ($[A⁢T⁢P]≪[A⁢D⁢P]$) or in non-equilibrium conditions with ATP in large excess over ADP ($[A⁢T⁢P]/[A⁢D⁢P]>10$). In order to probe the robustness of our results with respect to inaccuracies in the molecular model, we also took into account normally distributed errors on the conformational free energies $Δ⁢G_{i}$.

The results are reported as histograms in Figure 5 and they suggest that at equilibrium the average radius of gyration is extremely close to what would be measured in the case of free substrate (dashed line). This is in agreement with the experimental observation that the formation of rhodanese–DnaK complexes is strictly dependent on the hydrolysis of ATP and that ADP cannot trigger the expansion of the substrate (Kellner et al., 2014). Conversely, in large excess of ATP we observe a substantial swelling of the substrate ($75<R_{g}<95$ Å) due to the ultra-affine binding of Hsp70s. This finding is fully compatible with the size of DnaK/DnaJ/rhodanese complexes determined by single-molecule FRET experiments in excess of ATP (Kellner et al., 2014). In this regime, the limited effects of cochaperone binding on substrate conformations, which are not explicitly included in the model, play a minor role in determining the global expansion of the complex.

![Figure 5.](https://cdn.elifesciences.org/articles/48491/elife-48491-fig5-v2.jpg)

**Figure 5.:** Histograms of the radius of gyration for equilibrium (blue) and non equilibrium (red) values of [ATP]. The black dashed line indicates the average radius of unbound rhodanese. (inset) FRET transfer efficiencies as a function of the sequence separation between the fluorescent dyes. The black circles correspond to the experimental values (Kellner et al., 2014). Calculated efficiencies taking into account uncertainties are reported as blue (equilibrium conditions) and red circles (ATP excess).

A more quantitative comparison between the model and the FRET results can be achieved by back-calculating the transfer efficiencies that were experimentally measured for five distinct pairs of fluorescent dyes (Kellner et al., 2014). In equilibrium conditions, namely when $[ATP]/[ADP]≪1$, the calculated FRET efficiency is ~0.8 for all considered pairs of fluorescent dyes (inset of Figure 5, blue circles) and it matches the experimental results for the compact unbound rhodanese (∼0.8). A dramatic difference is instead observed in excess of ATP (red circles), where the expansion of the substrate leads to a significant decrease of the calculated efficiency , in excellent agreement with the experimental values measured in similar conditions (black circles). Remarkably, the results correctly captured the non-monotonic behaviour of FRET efficiency as a function of the sequence separation between the dyes, which was not reproduced in previous calculations (Kellner et al., 2014). This agreement corroborates the prediction of the DnaK binding sites on the rhodanese sequence and the overall reliability of our model.

### Energy balance and thermodynamic efficiency

Molecular chaperones consume energy via ATP hydrolysis in order to expand rhodanese. It is hence important to determine how effective they are as molecular machines, as well as to assess how favorable the physiological conditions are to perform their biological task.

To this aim, we calculated the global increase in the overall conformational free energy of the substrate with respect to equilibrium conditions, $Δ⁢G_{S⁢w⁢e⁢l⁢l}$ (Figure 6, top). This quantity measures the excess probability of each complex with respect to equilibrium conditions weighted by its corresponding conformational free energy $Δ⁢G_{i}$.

$$
Δ⁢G_{S⁢w⁢e⁢l⁢l}=\sumi[p_{i}⁢(\frac{[A⁢T⁢P]}{[A⁢D⁢P]})-p_{i}^{e⁢q}]⁢Δ⁢G_{i},
$$

where $p_{i}⁢(\frac{[A⁢T⁢P]}{[A⁢D⁢P]})$ is the probability of complex $i$ for a given value of $[A⁢T⁢P]/[A⁢D⁢P]$ and $p_{i}^{e⁢q}$ is the same quantity computed at equilibrium conditions. In order to investigate the conversion of chemical energy into mechanical work, it is instructive to focus on the ratio between $Δ⁢G_{S⁢w⁢e⁢l⁢l}$ and the free energy of hydrolysis of ATP $Δ⁢G_{h}$,

$$
ΔG_{h}=k_{B}T[ln⁡(\frac{[ATP]}{[ADP]})−ln⁡(\frac{[ATP]_{eq}}{[ADP]_{eq}})].
$$

The ratio $Δ⁢G_{S⁢w⁢e⁢l⁢l}/Δ⁢G_{h}$ reports on the effectiveness of the transduction process. We plot in Figure 6 (top) this quantity as a function of the $[A⁢T⁢P]/[A⁢D⁢P]$ ratio considering the estimated inaccuracies of the model as previously done for the gyration radius. Not surprisingly, all these curves exhibit a maximum because the probabilities of the different states, and thus also $Δ⁢G_{S⁢w⁢e⁢l⁢l}$, attain plateaus for $[A⁢T⁢P]≫[A⁢D⁢P]$ (see 4, top panel), whereas $Δ⁢G_{h}$ increases monotonically with the nucleotide ratio. The regime where transduction is maximally efficient intriguingly corresponds to values of $[A⁢T⁢P]/[A⁢D⁢P]$ that are typical of cellular conditions (grey area).

![Figure 6.](https://cdn.elifesciences.org/articles/48491/elife-48491-fig6-v2.jpg)

**Figure 6.:** (Top) Ratio between the conformational free energy and the free energy of ATP hydrolysis, as a function of [ATP]/[ADP]. Dark green curve results from data from molecular simulations and light green curves takes into account normally-distributed uncertainties on calculated $Δ⁢G_{i}$. (Bottom) Effective dissociation constant in the case of a single binding site normalized with respect to the corresponding value in equilibrium, as a function of [ATP]/[ADP] (solid black line). Ratio between the non-equilibrium excess of binding free energy $Δ⁢G_{b}$ and the free energy of ATP hydrolysis $Δ⁢G_{h}$, as a function of [ATP]/[ADP] (dashed red line). The gray region indicates the interval corresponding to physiological conditions.

We highlight that in our model Hsp70 functioning encompasses two distinct yet intertwined processes: the ATP-dependent binding of the chaperones to the substrate, and its consequent expansion. In this two-step mechanism, the amount of energy available for the mechanical expansion is limited by that provided by non-equilibrium Hsp70 binding, which does not explicitly depend on the overall conformational properties of the substrate. To further dissect the energetic determinants of Hsp70 functioning and obtain more general conclusions, we thus analyzed the energy balance of chaperone binding to a model substrate, such as a peptide with a single binding site. To this aim, we focused on a simplified reaction cycle, which essentially corresponds to a single triangle within the overall scheme in Figure 3 and does not imply any conformational free-energy variation upon Hsp70 binding. We report in Figure 6 (bottom panel, black solid line) the non-equilibrium dissociation constant, $K_{d}^{n⁢e⁢q}$, normalized with respect to its equilibrium value $K_{d}^{e⁢q}$, as a function of [ATP]/[ADP]. When the ratio between the concentrations of ATP and ADP approaches the physiological regime, the dissociation constant drops significantly until it settles at a value that is two orders of magnitude lower than its equilibrium counterpart, as already discussed in De Los Rios and Barducci (2014). Here, we convert the dissociation constant into a binding free-energy excess with respect to equilibrium

$$
Δ⁢G_{b}=-k_{B}⁢T⁢ln⁡[\frac{K_{d}^{n⁢e⁢q}}{K_{d}^{e⁢q}}]
$$

that we can compare to the free energy of ATP hydrolysis, $Δ⁢G_{h}$, as previously done in the case of $Δ⁢G_{S⁢w⁢e⁢l⁢l}$. Interestingly, also in this case the energy ratio is maximal in cellular conditions (red dashed line in Figure 6, bottom panel), suggesting that the optimality of the overall expansion process does not depend on specific features of the substrate but it is a direct consequence of the intrinsic kinetic parameters of Hsp70 chaperones.

## Discussion

Integrating molecular simulations, polymer theory, single-molecule experimental data and non-equilibrium rate models, we have developed a comprehensive framework that provides a quantitative picture of Hsp70-induced expansion of substrate proteins and offers a broad insight into the cellular functioning of this versatile chaperone machine.

We relied on molecular simulations for characterizing the structural and thermodynamic features of the complexes formed by the bacterial chaperone DnaK and its unfolded substrate rhodanese. Notably, we investigated a large variety of possible chaperone-substrate complexes for determining their conformational free energy as a function of stoichiometry and chaperone binding patterns. This computational strategy based on an enhanced-sampling protocol confirmed that excluded-volume interactions upon chaperone binding can greatly perturb the conformational ensemble of the unfolded substrate leading to its expansion. Remarkably, simulation results were found to be in excellent agreement with the predictions of Sanchez theory for globule to coil transition, thus providing another example of how polymer theory can be successfully used to decipher the behaviour of disordered proteins (Sherman and Haran, 2006; Hofmann et al., 2012; Schuler et al., 2016). We then combined conformational free energies with available biochemical data to develop an analytical rate model of the chaperone/substrate reaction cycle, which included both chaperone binding/unbinding and nucleotide hydrolysis/exchange processes.

This model fully takes into account non-equilibrium effects due to ATP hydrolysis and represents a natural extension of the ultra-affinity framework originally developed for peptide substrates with a single Hsp70 binding site (De Los Rios and Barducci, 2014). We could thus investigate the population of each complex and the average structural properties of the system as a function of the ATP/ADP nucleotide ratio, which measures how far the system is from thermodynamic equilibrium. The reliability of the model was corroborated by a quantitative comparison with recent single-molecule FRET data, indicating that our non-equilibrium framework accurately captures the salient features of the ATP-dependent expansion. We then used this unprecedented access to the thermodynamics details of this complex molecular process to compare the free-energy cost associated with substrate swelling with the chemical energy released by ATP-hydrolysis. Remarkably, this analysis revealed that energy transduction is maximally efficient for ATP/ADP values in cellular conditions. This result hints at the possibility that Hsp70 chaperones have been tuned by evolution to optimize the conversion of chemical energy into mechanical work for substrate expansion. Further analysis indicated that this optimality is likely inherited from the intrinsic properties of Hsp70 chaperones, which can convert up to 20% of the ATP chemical energy into non-equilibrium, excess binding energy at physiological conditions (Figure 6, bottom panel).

From a broader perspective, the ATP-driven action of Hsp70s induces a non-equilibrium redistribution of their protein-substrates over their structural ensemble. In particular, thanks to the fine-tuning of the process by co-chaperones (J-domain proteins and Nucleotide Exchange Factors), the expansion process highlighted here, followed by substrate release, may result in the enhancement of the native state population beyond the predictions of thermodynamic equilibrium, as recently observed even under otherwise denaturing conditions (Goloubinoff et al., 2018). Consistently, Zhao and coworkers have recently observed that Hsp70 chaperones crucially contribute in vivo to the solubility and functionality of a sizeable fraction of the E. coli proteome that, in their absence, would instead spontaneously misfold and aggregate (Zhao et al., 2019). Remarkably, a similar effect has been observed in vitro for the GroEL chaperonin (Chakrabarti et al., 2017; Goloubinoff et al., 2018), hinting at the possibility that multiple chaperone families might reshape the equilibrium conformational distribution of proteins through energy-consuming processes. These considerations might have important consequences for our ability to translate results from in vitro experiments to the active cellular context (Bershtein et al., 2013). Likewise, they raise fundamental questions about the evolution of protein sequences: indeed, since chaperones are ubiquitous and very much conserved across the different kingdoms of life, their ability to favor native states might have partially relieved the selection pressure for strong equilibrium thermodynamic stability, thus allowing evolution to proceed faster and to be more tolerant for slightly destabilizing mutations, as suggested in Rutherford and Lindquist (1998); Tokuriki and Tawfik (2009).

Besides the unfolding of non-native substrates discussed in this work, Hsp70s are highly versatile machines that play a fundamental role in a variety of diverse cellular functions such as protein translocation, protein translation, and disassembly of protein complexes. All these processes share basic analogies from the mechanistic point of view: in all these cases, Hsp70 binding to flexible substrates in constrained environments requires the energy of ATP hydrolysis (ultra-affinity) and results in the generation of effective forces due to excluded volume effects (entropic pulling), which ultimately drive protein translocation into mitochondria (De Los Rios et al., 2006; Assenza et al., 2015), clathrin cage disassembly (Sousa et al., 2016) and/or prevention of ribosome stalling (Liu et al., 2013). Here, by detailing how energy flows from ATP hydrolysis to mechanical work due to entropic pulling, we have elucidated a general force-generating mechanism of Hsp70 chaperones. This mechanism does not rely on any power-stroke conformational change but it rather depends on the efficient conversion of ATP chemical energy into ultra-affinity.

## Materials and methods

### Molecular model

In all the simulations, rhodanese and Hsp70 were coarse grained at the single-residue level as collections of beads centered on the $C_{\alpha}$ atom of each amino acid. The unfolded state of bovine rhodanese (PDB:2RHS) was modeled according to the force field for disordered proteins from Smith et al. (2014). Two- and three-body bonded interactions along the substrate backbone were included via harmonic potentials, namely $V_{bond}=k_{l}\sumb(r_{b}−l)^{2}/2$ and $V_{bend}=\frac{1}{2}k_{\theta}\sum\alpha(\theta_{\alpha}−\theta_{0})^{2}$, respectively. In the previous formulas, $r_{b}$ denotes bond lengths; $\theta_{\alpha}$ the bend angles; $l=3.9$ Å; $(k_{l}/k_{B}T)^{−1/2}=0.046$ Å; $\theta_{0}=2.12$ rad; $(k_{\theta}/k_{B}⁢T)^{-\frac{1}{2}}=0.26$; and $k_{B}⁢T$ is the thermal energy. Four-body bonded interactions were implemented as Fourier terms, $V_{dihed}=k_{B}T\sumd\sums=14[A_{s}cos⁡(sϕ_{d})+B_{s}sin⁡(sϕ_{d})]$, where $ϕ_{d}$ is the torsion angle and $A_{1}=0.705$, $A_{2}=-0.313$, $A_{3}=-0.079$, $A_{4}=0.041$, $B_{1}=-0.175$, $B_{2}=-0.093$, $B_{3}=0.030$, $B_{4}=0.030$. The steric repulsion was implemented through a Weeks-Chandler-Andersen potential, $V_{W⁢C⁢A}=\sum_{i⁢j}V_{r}$, where

$$
V_{r}={4k_{B}T[(\frac{\sigma}{r_{ij}})^{12}−(\frac{\sigma}{r_{ij}})^{6}]+k_{B}Tif r_{ij}\leq2^{\frac{1}{6}}\sigma0otherwise.
$$

In the previous formula, $r_{i⁢j}$ is the distance between beads $i$ and $j$, while $\sigma=4.8$ Å. The hydrophobic part of the potential is specific to the interacting residues and is modeled as the attractive part of the Lennard-Jones potential, $V_{hydro}=ϵ_{h}\sumijV_{h}$, where

$$
V_{h}={4ϵ_{ij}[(\frac{\sigma}{r_{ij}})^{12}−(\frac{\sigma}{r_{ij}})^{6}]if r_{ij}\geq2^{\frac{1}{6}}\sigma−ϵ_{ij}otherwise.
$$

In the previous formula, $ϵ_{h}=0.7722⁢k_{B}⁢T$ sets the overall strength of the hydrophobic interactions, while $ϵ_{i⁢j}$ depends on the residues $i$ and $j$ involved in the interaction, and is defined as the geometric mean of their hydrophobicities, $ϵ_{i⁢j}≡\sqrt{ϵ_{i}⁢ϵ_{j}}$. The values of the hydrophobicities considered are based on a shifted and normalized Monera hydrophobicity scale (Smith et al., 2014). Electrostatic interactions were neglected based on control FRET experiments (see section 5.3). Without further tuning, this force field gives a radius of gyration of unbound rhodanese equal to $R_{g}=(23.3\pm0.1)$ Å, which is in good agreement with the experimental value $R_{g}=(20.1\pm0.8)$ Å (Kellner et al., 2014; Hofmann et al., 2014).

We modeled Hsp70 by means of a simple structure-based potential (Assenza et al., 2015) built on the conformation of ADP-bound Hsp70 (Bertelsen et al., 2009, PDB:2KHO). We described both the NBD (residues 4–680) and the SBD (residues 690–603) as rigid bodies whereas the interdomain linker (residues 681–689) was modeled according to the potential for flexible proteins described above. Importantly, non-bonded interactions of Hsp70 residues were limited to excluded volume effects and described by WCA potential (see Equation (5)). Electrostatic interactions were not explicitly included due to their marginal role in Hsp70/rhodanese complexes evidenced by FRET experiments (Appendix 1).

The binding sites for DnaK on the substrate were identified by applying the algorithms by Rüdiger et al. (1997) and Van Durme et al., 2009 on rhodanese and selecting only fragments for which at least partial consensus between the two predictions was obtained. Following this procedure, we identified six binding sites roughly centered on residues 10, 118, 131, 162, 188, 260 of the rhodanese sequence. The residues of the binding site were aligned to a SBD-bound peptide reported in the literature (PDB:1DKX Zhu et al., 1996) and constrained to move rigidly with the corresponding SBD, thus ensuring that each chaperone was irreversibly bound to the substrate. Following this procedure, 26 = 64 different chaperone/substrate complexes were built depending on the occupancy of each binding site.

### Simulation protocols

All the simulations were performed with a version of LAMMPS (Plimpton, 1995) patched with the open-source, community-developed PLUMED library (Bonomi et al., 2019), version 2.1 (Tribello et al., 2014). The temperature $T=293⁢K$ was controlled through a Langevin thermostat with damping parameter 16 ns-1. The time step was set equal to 1 fs, and each residue had a mass equal to 1 Da.

In order to obtain conformational properties, for each of the 64 chaperone/rhodanese complexes we performed at least 10 independent simulations of 2 · 107 timesteps. To ensure that full equilibration was achieved, only the last 107 timesteps of the obtained trajectories were considered for analysis. Statistical errors on the computed quantities were estimated as standard errors of the mean computed across independent realizations and are smaller than the size of symbols reported in the figures. The FRET efficiency E for a given couple of dyes was computed starting from the distance $r$ separating the corresponding amino acids as

$$
E=\frac{1}{1+(\frac{r}{r_{0}})^{6}},
$$

where r0 = 54 Å, as in Kellner et al. (2014). For each realization, the time average of E was computed. The final values employed to compute the results reported in the inset of Figure 5 in the main text were obtained as the average between independent realizations.

The conformational free energies were computed by means of steered simulations, where for each complex rhodanese was pulled from equilibrium until an elongated conformation was obtained (Figure 2—figure supplement 1, top panel). Due to the large intermolecular distances, the effect of chaperones on the conformational properties of fully-stretched rhodanese is negligible, so that this state can be used as a reference to compute the free-energy differences between different chaperone/rhodanese complexes. The pulling was implemented by adding a harmonic potential acting on the radius of gyration $R_{g}$ of rhodanese. The equilibrium position of the harmonic trap was increased at a constant pulling speed v = 10-5Å/fs from the equilibrium value up to $R_{g}=R_{g}^{fin}$. For each chaperone/substrate complex, 100 independent pulling simulations were performed, starting from uncorrelated initial snapshots extracted from the equilibrium distribution. For each realization, the work $W$ performed by the bias potential during the steering process was measured. The free-energy difference $\delta⁢G$ between the equilibrium starting point and the reference state (corresponding to $R_{g}^{fin}$) was then computed via the Jarzynski (1997) equality:

$$
e^{-\frac{\delta⁢G}{k_{B}⁢T}}=⟨e^{-\frac{W}{k_{B}⁢T}}⟩,
$$

where $⟨…⟩$ denotes statistical average. The error on $\delta⁢G$ was estimated according to the bootstrap method. The quantity $Δ⁢G$ considered in the main text was finally computed as $Δ⁢G=\delta⁢G_{0}-\delta⁢G$, where $\delta⁢G_{0}$ corresponds to the case of rhodanese alone (Figure 2—figure supplement 1, bottom panel). The uncertainty on $Δ⁢G$ was estimated by propagating the error bars on $\delta⁢G$ and is always smaller than the size of symbols. In order to enhance the robustness of the results, the final values reported in the main text were obtained as a further average over the values of $R_{g}^{fin}$ within the range 260 Å ≤ $R_{g}^{fin}$ ≤ 290 Å.

### Rate model

For the kinetic model we consider a system in which each of the six binding sites can either be occupied by a chaperone in the ATP or ADP state, or it can be free, so that in total there are 36 = 729 possible configurations. The concentration $c_{i}$ of each state evolves in time according to a system of rate equations

$$
\frac{d⁢c_{i}}{d⁢t}=\sumjk_{j⁢i}⁢c_{j}-\sumjk_{i⁢j}⁢c_{i}
$$

where $k_{i⁢j}$ is the transition rate from state $i$ to state $j$. The first term in the right hand side (r.h.s.) of Equation (9) represents the total flux of molecules from the other states toward state $i$, while the second term in the r.h.s. of Equation (9) accounts for the flux of molecules from state $i$ to any other state. We focused on the steady-state, when the concentrations of the various states do not change over time, which is defined by

$$
\frac{d⁢c_{i}}{d⁢t}=0
$$

Here, we provide a list of the relevant reactions that must be taken into account and of their corresponding rates. Each configuration is labelled by means of six symbols: 0 for empty sites, $T$ for sites occupied by an ATP-bound chaperone and $D$ for sites occupied by an ADP-bound chaperone (e.g. $(0,T,0,D,0,0)$, where the first, third, fifth and sixth Hsp70 binding sites are unoccupied, the second binding site is associated to a chaperone in the ATP-bound state while the fourth binding site is associated with a chaperone in the ADP-bound state). With this notation, the rates corresponding to every reaction are easily determined. Examples of the reactions that need to be considered are

$$
(0,T,0,0,0,0)⇌k_{off}^{adp}[Hsp70⋅ADP]k_{on}^{adp}e^{−\betaΔΔG}(0,T,0,D,0,0)(0,T,0,0,0,0)⇌k_{off}^{atp}[Hsp70⋅ADP]k_{on}^{atp}e^{−\betaΔΔG}(0,T,0,T,0,0)
$$

$$
(0,T,0,T,0,0)⇌k_{s}^{s}k_{h}^{s}(0,T,0,D,0,0)
$$

$$
(0,T,0,D,0,0)⇌k_{ex,TD}^{eff}k_{ex,DT}^{eff}(0,T,0,T,0,0).
$$

We further provide, as an example, the equation for a precise configuration, say $(0,T,0,D,0,0)$ (here the label stands for the concentration of the configuration). The two binding sites that are occupied can undergo chaperone unbinding, ATP hydrolysis/synthesis or nucleotide exchange. The remaining unoccupied binding sites can bind either an ATP- or an ADP-bound chaperone. We thus have

$$
\frac{d}{dt}(0,T,0,D,0,0)=−(0,T,0,D,0,0)∗(k_{ex,DT}^{eff}+k_{s}^{s}+k_{ex,TD}^{eff}+k_{h}^{s}+k_{off}^{atp}+k_{off}^{adp})++(0,0,0,D,0,0)[Hsp70⋅ATP]k_{on}^{atp}e^{−\betaΔΔG}++(0,T,0,0,0,0)[Hsp70⋅ADP]k_{on}^{adp}e^{−\betaΔΔG}++(T,T,0,D,0,0)k_{off}^{atp}++(D,T,0,D,0,0)k_{off}^{adp}++(0,T,T,D,0,0)k_{off}^{atp}++(0,T,D,D,0,0)k_{off}^{adp}++(0,T,0,D,T,0)k_{off}^{atp}++(0,T,0,D,D,0)k_{off}^{adp}++(0,T,0,D,0,T)k_{off}^{atp}++(0,T,0,D,0,D)k_{off}^{adp}.
$$

Below we further detail the rates of our model.

It is possible to move from an ATP-state to an ADP-state either via hydrolysis/synthesis or via nucleotide exchange. In the case of exchange, effective constants are used, which take into account the unbinding of one nucleotide species and the binding of the different one. The effective exchange rates are thus a function of the ratio [ATP]/[ADP] (see also De Los Rios and Barducci, 2014):

$$
k_{ex,DT}^{eff}=\frac{k_{−D}k_{+T}\frac{[ATP]}{[ADP]}}{k_{+D}+k_{+T}\frac{[ATP]}{[ADP]}}
$$



$$
k_{ex,TD}^{eff}=\frac{k_{−T}k_{+D}}{k_{+D}+k_{+T}\frac{[ATP]}{[ADP]}},
$$

where $k_{+D}$, $k_{+T}$, $k_{-D}$ and $k_{-T}$ are the binding and unbinding rates for ADP and ATP respectively.

The rates of binding between the chaperone and single peptides have been previously determined experimentally (Mayer et al., 2000), and they were corrected in order to take into account the conformational change of the full polypeptide substrate upon binding, as we illustrated in the main text.

Substrate binding enhances the chaperone ATPase activity. Furthermore, the stimulation of ATP hydrolysis always takes place in cooperation with JDP co-chaperones. In our model, we did not consider them explicitly but their contribution was implicitly included through the choice of the rate constants.

In particular, the hydrolysis rate in the absence of the substrate, $k_{h}$, is much smaller than the same rate in the presence of the substrate, $k_{h}^{s}$ ($k_{h}≪k_{h}^{s}$). We assumed that the ratio between the rate of hydrolysis $k_{h}$ and the rate of synthesis $k_{s}$ is not altered by the substrate:

$$
\frac{k_{h}}{k_{s}}=\frac{k_{h}^{s}}{k_{s}^{s}}.
$$

The substrate binding/unbinding rates, the rates of nucleotide exchange and the hydrolysis and synthesis rates are collectively constrained by thermodynamic relations. Indeed, when the ratio between the concentrations of ATP and ADP is equal its equilibrium value (when the spontaneous hydrolysis and synthesis reactions are at steady state and compensate each other), detailed balance must be satisfied (Ge et al., 2012). As a consequence, for every closed cycle in the reaction network the product of the rates in one direction must be equal to the product of the rates in the opposite direction. Therefore, if $k_{o⁢n}^{a⁢t⁢p}$, $k_{o⁢n}^{a⁢d⁢p}$, $k_{o⁢f⁢f}^{a⁢t⁢p}$ and $k_{o⁢f⁢f}^{a⁢d⁢p}$ are the rate of substrate binding and unbinding from a chaperone in the ATP and ADP states, we must have

$$
\frac{k_{o⁢n}^{a⁢t⁢p}⁢k_{h}^{s}⁢k_{o⁢f⁢f}^{a⁢d⁢p}⁢k_{s}}{k_{o⁢n}^{a⁢d⁢p}⁢k_{s}^{s}⁢k_{o⁢f⁢f}^{a⁢t⁢p}⁢k_{h}}=\frac{k_{o⁢n}^{a⁢t⁢p}⁢k_{o⁢f⁢f}^{a⁢d⁢p}}{k_{o⁢n}^{a⁢d⁢p}⁢k_{o⁢f⁢f}^{a⁢t⁢p}}=1.
$$

Remarkably, taking the rates as provided in Mayer et al. (2000); Hu et al. (2006); Kellner et al. (2014), this relation is not satisfied, and we had thus to modify them. We thus calculated the product in the formula above and then corrected the rates in the following way:

$$
\frac{k_{on}^{atp}k_{off}^{adp}}{k_{on}^{adp}k_{off}^{atp}}=r
$$



$$
k_{on}^{atp},k_{off}^{adp}→k_{on}^{atp}/r^{1/4},k_{off}^{adp}/r^{1/4}
$$



$$
k_{on}^{adp},k_{off}^{atp}→k_{on}^{adp}∗r^{1/4},k_{off}^{atp}∗r^{1/4}.
$$

The concentration of free chaperones in the ATP and in the ADP states was obtained, at the leading order, by solving a three-state system whose reactions have the form

$$
Hsp70+ADP⇌Hsp70⋅ADP⇌Hsp70⋅ATP⇌Hsp70+ATP.
$$

Since we worked in the assumption of excess of chaperones in the system, once these concentrations were obtained, they remained fixed once for all, without being considered as a variable of the biochemical network.

We report in the following table the rates used in the model.

<table>
  <thead>
    <tr>
      <th colspan="2">Parameters of the model (Mayer et al., 2000; Hu et al., 2006; Kellner et al., 2014)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ko⁢f⁢fa⁢t⁢p  2.31⁢s-1</td>
      <td>ko⁢f⁢fa⁢d⁢p  2*10-3⁢s-1</td>
    </tr>
    <tr>
      <td>k-T  1.33*10-4⁢s-1</td>
      <td>k-D  0.022⁢s-1</td>
    </tr>
    <tr>
      <td>ko⁢na⁢t⁢p  1.28*106⁢M-1⁢s-1</td>
      <td>ko⁢na⁢d⁢p  103⁢M-1⁢s-1</td>
    </tr>
    <tr>
      <td>k+T  1.3*105⁢M-1⁢s-1</td>
      <td>k+D  2.67*105⁢M-1⁢s-1</td>
    </tr>
    <tr>
      <td>kh  6*10-4⁢s-1</td>
      <td>khs  1.8⁢s-1</td>
    </tr>
  </tbody>
</table>

To test the robustness of the model for the radius of gyration, the average FRET efficiency and the free-energy $Δ⁢G_{s⁢w⁢e⁢l⁢l}$, 100 realizations were implemented, taking each time the values $Δ⁢G_{i}$ from a Gaussian distribution with $\sigma=0.3$ kcal/mol and mean equal to the value obtained with the MD simulations.

### Molecular graphics

Molecular graphics in Figures 1 and 6 have been generated with UCSF Chimera, developed by the Resource for Biocomputing, Visualization, and Informatics at the University of California, San Francisco, with support from NIH P41-GM103311 (Pettersen et al., 2004).

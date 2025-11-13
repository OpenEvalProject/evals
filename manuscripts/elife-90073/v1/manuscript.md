# Explicit ion modeling predicts physicochemical interactions for chromatin organization

## Authors

- Xingcheng Lin<sup>1</sup> ([ORCID: 0000-0002-9378-6174](https://orcid.org/0000-0002-9378-6174))
- Bin Zhang<sup>1</sup> ([ORCID: 0000-0002-3685-7503](https://orcid.org/0000-0002-3685-7503)) †

### Affiliations

1. Department of Chemistry, Massachusetts Institute of Technology Cambridge United States ([ROR:042nb2s44](https://ror.org/042nb2s44))

† Corresponding author

## Abstract

Molecular mechanisms that dictate chromatin organization in vivo are under active investigation, and the extent to which intrinsic interactions contribute to this process remains debatable. A central quantity for evaluating their contribution is the strength of nucleosome-nucleosome binding, which previous experiments have estimated to range from 2 to 14 kBT. We introduce an explicit ion model to dramatically enhance the accuracy of residue-level coarse-grained modeling approaches across a wide range of ionic concentrations. This model allows for de novo predictions of chromatin organization and remains computationally efficient, enabling large-scale conformational sampling for free energy calculations. It reproduces the energetics of protein-DNA binding and unwinding of single nucleosomal DNA, and resolves the differential impact of mono- and divalent ions on chromatin conformations. Moreover, we showed that the model can reconcile various experiments on quantifying nucleosomal interactions, providing an explanation for the large discrepancy between existing estimations. We predict the interaction strength at physiological conditions to be 9 kBT, a value that is nonetheless sensitive to DNA linker length and the presence of linker histones. Our study strongly supports the contribution of physicochemical interactions to the phase behavior of chromatin aggregates and chromatin organization inside the nucleus.

## Introduction

Three-dimensional genome organization plays essential roles in numerous DNA-templated processes (Dekker et al., 2013; Bonev and Cavalli, 2016; Finn and Misteli, 2019; Misteli, 2020; Lin et al., 2021b). Understanding the molecular mechanisms for its establishment could improve our understanding of these processes and facilitate genome engineering. Advancements in high-throughput sequencing and microscopic imaging have enabled genome-wide structural characterization, revealing a striking compartmentalization of chromatin at large scales (Lieberman-Aiden et al., 2009; Quinodoz et al., 2018; Su et al., 2020; Takei et al., 2021). For example, A compartments are enriched with euchromatin and activating post-translational modifications to histone proteins. They are often spatially segregated from B compartments that enclose heterochromatin with silencing histone marks (Gibcus and Dekker, 2013; Finn and Misteli, 2019; Misteli, 2020; Mirny and Dekker, 2022; Xie and Zhang, 2019).

Compartmentalization has been proposed to arise from the microphase separation of different chromatin types as in block copolymer systems (Fujishiro and Sasai, 2022; Jost et al., 2014; Falk et al., 2019; Bajpai et al., 2021; Laghmach et al., 2020; Hu et al., 2013; Lesne et al., 2014; Di Pierro et al., 2016; Xie et al., 2017; Yildirim and Feig, 2018; MacPherson et al., 2018; Shi and Thirumalai, 2021; Brahmachari et al., 2022). However, the molecular mechanisms that drive the microphase separation are not yet fully understood. Protein molecules that recognize specific histone modifications have frequently been found to undergo liquid-liquid phase separation (Larson et al., 2017; Kent et al., 2020; Xie et al., 2022; Leicher et al., 2022; Latham and Zhang, 2021; Lin et al., 2021a; MacPherson et al., 2018), potentially contributing to chromatin demixing. Demixing can also arise from interactions between chromatin and various nuclear landmarks such as nuclear lamina and speckles (Brahmachari et al., 2022; Falk et al., 2019; Mirny and Dekker, 2022; Kamat et al., 2023), as well as active transcriptional processes (Hilbert et al., 2021; Jiang et al., 2022; Brahmachari et al., 2023; Goychuk et al., 2023). Furthermore, recent studies have revealed that nucleosome arrays alone can undergo spontaneous phase separation (Gibson et al., 2019; Strickfaden et al., 2020; Zhang et al., 2022), indicating that compartmentalization may be an intrinsic property of chromatin driven by nucleosome-nucleosome interactions.

The relevance of physicochemical interactions between nucleosomes to chromatin organization in vivo has been constantly debated, partly due to the uncertainty in their strength (Kruithof et al., 2009; Cui and Bustamante, 2000; Kaczmarczyk et al., 2020; Funke et al., 2016). Examining the interactions between native nucleosomes poses challenges due to the intricate chemical modifications that histone proteins undergo within the nucleus and the variations in their underlying DNA sequences (Fenley et al., 2010; Fenley et al., 2018). Many in vitro experiments have opted for reconstituted nucleosomes that lack histone modifications and feature well-positioned 601-sequence DNA (Lowary and Widom, 1998) to simplify the chemical complexity. These experiments aim to establish a fundamental reference point, a baseline for understanding the strength of interactions within native nucleosomes. Nevertheless, even with reconstituted nucleosomes, a consensus regarding the significance of their interactions remains elusive. For example, using force-measuring magnetic tweezers, Kruithof et al. estimated the inter-nucleosome binding energy to be ∼14 kBT (Kruithof et al., 2009). On the other hand, Funke et al. introduced a DNA-origami-based force spectrometer to directly probe the interaction between a pair of nucleosomes (Funke et al., 2016), circumventing any potential complications from interpretations of single-molecule traces of nucleosome arrays. Their measurement reported a much weaker binding free energy of approximately 2 kBT. This large discrepancy in the reported reference values complicates a further assessment of the interactions between native nucleosomes and their contribution to chromatin organization in vivo.

Computational modeling is well suited for reconciling the discrepancy across experiments and determining the strength of inter-nucleosome interactions. The high computational cost of atomistic simulations (Winogradoff et al., 2015; Woods et al., 2021; Li et al., 2023) has inspired several groups to calculate the nucleosome binding free energy with coarse-grained models (Moller et al., 2019; Farr et al., 2021). However, the complex distribution of charged amino acids and nucleotides at nucleosome interfaces places a high demand on force field accuracy. In particular, most existing models adopt a mean-field approximation with the Debye-Hückel theory (Phillips, 2012) to describe electrostatic interactions in an implicit-solvent environment (Izadi et al., 2016; Bascom and Schlick, 2018; Moller et al., 2019; Farr et al., 2021), preventing an accurate treatment of the complex salt conditions explored in experiments. Further force field development is needed to improve the accuracy of coarse-grained modeling across different experimental settings (Freeman et al., 2011; Hinckley and de Pablo, 2015; Sun et al., 2022; Hayes et al., 2015).

We introduce a residue-level coarse-grained explicit ion model for simulating chromatin conformations and quantifying inter-nucleosome interactions. We validate our model’s accuracy through extensive simulations, demonstrating that it reproduces the binding affinities of protein-DNA complexes (Privalov et al., 2011) and energetic cost of nucleosomal DNA unwinding (Hall et al., 2009). Further simulations of chromatin at various salt concentrations reproduce experimentally measured sedimentation coefficients (Correll et al., 2012). We also reveal extensive close contacts between histone proteins and DNA across nucleosomes, the perturbation of which explains the discrepancy among various experimental studies. Finally, we determined the binding free energy between a pair of nucleosomes under physiological salt concentrations as ∼9 kBT. While longer linker DNA would reduce this binding energy, linker histones can more than compensate this reduction to mediate inter-nucleosome interactions with disordered, charged terminal tails. Our study supports the importance of intrinsic physicochemical interactions in chromatin organization in vivo.

## Results

### Counterion condensation accommodates nucleosomal DNA unwrapping

Various single-molecule studies have been carried out to probe the stability of nucleosomes and the interactions between histone proteins and DNA (Bennink et al., 2001; Cui and Bustamante, 2000; Pope et al., 2005; Bancaud et al., 2007; Hall et al., 2009). The DNA-unzipping experiment performed by Hall et al., 2009, is particularly relevant since the measured forces can be converted into a free energy profile of DNA unwinding at a base-pair resolution, as shown by Forties et al. with a continuous-time Markov model (Forties et al., 2011). The high-resolution quantification of nucleosome energetics is valuable for benchmarking the accuracy of computational models.

We introduce a coarse-grained explicit ion model for chromatin simulations (Figure 1). The model represents each amino acid with one coarse-grained bead and three beads per nucleotide. It resolves the differences among various chemical groups to accurately describe biomolecular interactions with physical chemistry potentials. Our explicit representation of monovalent and divalent ions enables a faithful description of counterion condensation and its impact on electrostatic interactions between protein and DNA molecules. Additional model details are provided in the Materials and methods and Appendix.

![Figure 1.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig1-v1.jpg)

**Figure 1.:** The left panel presents a snapshot for the simulation box of a 147 bp nucleosome in a solution of 100 mM NaCl and 0.5 mM MgCl2. The nucleosomal DNA and histone proteins are colored in red and white, respectively. The zoom-in on the right highlights the condensation of ions around the nucleosome, with Na+ in cyan and Mg2+ in yellow. Negative residues of the histone proteins are colored in pink.

We performed umbrella simulations (Torrie and Valleau, 1977) to determine the free energy profile of nucleosomal DNA unwinding. The experimental buffer condition of 0.10 M NaCl and 0.5 mM MgCl2 (Hall et al., 2009) was adopted in simulations for direct comparison. As shown in Figure 2B, the simulated values match well with experimental results over a wide range. Furthermore, we computed the binding free energy for a diverse set of protein-DNA complexes and the simulated values again match well with experimental data (Figure 2—figure supplement 1), supporting the model’s accuracy.

![Figure 2.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig2-v1.jpg)

**Figure 2.:** (A) Illustration of the umbrella simulation setup using the end-to-end distance between two DNA termini as the collective variable. The same color scheme as in Figure 1 is adopted. Only ions close to the nucleosomes are shown for clarity. (B) Comparison between simulated (black) and experimental (red) free energy profile as a function of the unwrapped DNA base pairs. Error bars were computed as the standard deviation of three independent estimates. (C) The average number of Na+ ions within 10 Å of the nucleosomal DNA (top) and Cl−ions within 10 Å of histone proteins (bottom) are shown as a function of the unwrapped DNA base pairs. Error bars were computed as the standard deviation of three independent estimates.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Experimental and simulated binding free energies are compared for nine protein-DNA complexes (Privalov et al., 2011), with a Pearson correlation coefficient of 0.6. The PDB ID for each complex is indicated in red, and the diagonal line is drawn in blue. The significant correlation between simulated and experimental values supports the accuracy of the model. To further enhance the agreement between the two, it will be necessary to implement specific non-bonded interactions that can resolve differences among amino acids and nucleotides beyond simple electrostatics. Such modifications will be interesting avenues for future research. See text section ‘Binding free energy of protein-DNA complexes’ for simulation details.

Counterions are often released upon protein-DNA binding to make room for close contacts at the interface, contributing favorably to the binding free energy in the form of entropic gains (Schiessel, 2003). However, previous studies have shown that the histone-DNA interface in a fully wrapped nucleosome configuration is not tightly sealed but instead permeated with water molecules and mobile ions (Davey et al., 2002; Materese et al., 2009). Given their presence in the bound form, how these counterions contribute to nucleosomal DNA unwrapping remains to be shown. We calculated the number of DNA-bound cations and protein-bound anions as DNA unwraps. Our results, shown in Figure 2C, indicate that only a modest amount of extra Na+ and Cl− ions becomes associated with the nucleosome as the outer DNA layer unwraps. However, significantly more ions become bound when the inner layer starts to unwrap (after 73 bp). These findings suggest that counterion release may contribute more significantly to the inner layer wrapping, potentially caused by a tighter protein-DNA interface.

### Charge neutralization with Mg2+ compacts chromatin

In addition to contributing to the stability of individual nucleosomes, counterions can also impact higher-order chromatin organization. Numerous groups have characterized the structures of nucleosome arrays (Widom, 1986; Schwarz et al., 1996; Engelhardt, 2004; Correll et al., 2012; Grigoryev et al., 2009; Allahverdi et al., 2015), revealing a strong dependence of chromatin folding on the concentration and valence of cations.

To further understand the role of counterions in chromatin organization, we studied a 12-mer with 20-bp-long linker DNA under different salt conditions. We followed the experiment setup by Correll et al., 2012, that immerses chromatin in solutions with 5 mM NaCl, 150 mM NaCl, 0.6 mM MgCl2, or 1 mM MgCl2. To facilitate conformational sampling, we carried out umbrella simulations with a collective variable that quantifies the similarity between a given configuration and a reference two-start helical structure. Simulation details and the precise definition of the collective variable are provided in the Materials and methods and Appendix. Data from different umbrella windows were combined together with proper reweighting (Kumar et al., 1992) for analysis.

As shown in Figure 3A, the average sedimentation coefficients determined from our simulations match well with experimental values. Specifically, the simulations reproduce the strong contrast in chromatin size between the two systems with different NaCl concentrations. Chromatin under 5 mM NaCl features an extended configuration with minimal stacking between one and three nucleosomes (Figure 3B). On the other hand, the compaction is evident at 150 mM NaCl. Notably, in agreement with previous studies (Ding et al., 2021; Liu et al., 2022; Cai et al., 2018; Dombrowski et al., 2022), we observe tri-nucleosome configurations as chromatin extends. Finally, the simulations also support that divalent ions are more effective in packaging chromatin than NaCl. Even in the presence of 0.6 mM MgCl2, the chromatin sedimentation coefficient is comparable to that obtained at 150 mM of NaCl.

![Figure 3.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig3-v1.jpg)

**Figure 3.:** (A) Top: Comparison of simulated and experimental (Correll et al., 2012) sedimentation coefficients of chromatin at different salt concentrations. Bottom: Number of DNA charges neutralized by bound cations (yellow, left y-axis label) and the fraction of ions bound to DNA (red, right y-axis label) at different salt concentrations. The error bars were estimated from the standard deviation of simulated probability distributions (Figure 3—figure supplement 1). (B) Representative chromatin structures with sedimentation coefficients around the mean values at different salt concentrations.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Probability distribution of sedimentation coefficients calculated from the simulation with Na+ ions. (B) Probability distribution of sedimentation coefficients calculated from the simulation with Mg2+ ions. (C) Probability distribution of neutralized charges calculated from the simulation with Na+ ions. (D) Probability distribution of neutralized charges calculated from the simulation with Mg2+ ions. (E) Probability distribution of the fraction of bound ions calculated from the simulation with Na+ ions. (F) Probability distribution of the fraction of bound ions calculated from the simulation with Mg2+ ions.

We further characterized ions that are in close contact with DNA to understand their impact on chromatin organization. Our simulations support the condensation of cations, especially for divalent ions (Figure 3A, bottom) as predicted by the Manning theory (Manning, 1978; Clark and Kimura, 1990). Ion condensation weakens the repulsion among DNA segments that prevents chromatin from collapsing. Notably, the fraction of bound Mg2+ is much higher than Na+. Correspondingly, the amount of neutralized negative charges is always greater in systems with divalent ions, despite the significantly lower salt concentrations. The difference between the two types of ions arises from the more favorable interactions between Mg2+ and phosphate groups that more effectively offset the entropy loss due to ion condensation (Clark and Kimura, 1990). While higher concentrations of NaCl do not dramatically neutralize more charges, the excess ions provide additional screening to weaken the repulsion among DNA segments, stabilizing chromatin compaction.

### Close contacts drive nucleosome binding free energy

Encouraged by the explicit ion model’s accuracy in reproducing experimental measurements of single-nucleosomes and nucleosome arrays, we moved to directly quantify the strength of inter-nucleosomes interactions. We once again focus on reconstituted nucleosomes for a direct comparison with in vitro experiments. These experiments have yielded a wide range of values, ranging from 2 to 14 kBT (Funke et al., 2016; Cui and Bustamante, 2000; Kruithof et al., 2009). Accurate quantification will offer a reference value for conceptualizing the significance of physicochemical interactions among native nucleosomes in chromatin organization in vivo.

To reconcile the discrepancy among various experimental estimations, we directly calculated the binding free energy between a pair of nucleosomes with umbrella simulations. We adopted the same ionic concentrations as in the experiment performed by Funke et al., 2016, with 35 mM NaCl and 11 mM MgCl2. We focus on this study since the experiment directly measured the inter-nucleosomal interactions, allowing straightforward comparison with simulation results. Furthermore, the reported value for nucleosome binding free energy deviates the most from other studies. In one set of umbrella simulations, we closely mimicked the DNA-origami device employed by Funke et al. to move nucleosomes along a predefined path for disassociation (Figure 4A, A1 to A3). For example, neither nucleosome can freely rotate (Figure 4—figure supplement 1); the first nucleosome is restricted to the initial position, and the second nucleosome can only move within the Y-Z plane along the arc 15 nm away from the origin. For comparison, we performed a second set of independent simulations without imposing any restrictions on nucleosome orientations. Additional simulation details can be found in Materials and methods and Appendix.

![Figure 4.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig4-v1.jpg)

**Figure 4.:** (A) Illustration of the simulation protocol employed to mimic the nucleosome unbinding pathway dictated by the DNA-origami device (Funke et al., 2016). The three configurations, A1, A2, and A3, corresponding to the three cyan dots in part B at distances 62.7, 80.2, and 96.3 Å. For comparison, a tightly bound configuration uncovered in simulations without any restraints of nucleosome movement is shown as A1’. The number of contacts formed by histone tails and DNA (Htail-DNA) and by histone core and DNA (Hcore-DNA) from different nucleosomes is shown for A1 and A1’. (B) Free energy profile as a function of the distance between the geometric centers of the two nucleosomes, computed from unrestrained (black) and DNA-origami-restrained simulations (red). Error bars were computed as the standard deviation of three independent estimates. (C) Average inter-nucleosomal contacts between DNA and histone tail (orange) and core (blue) residues, computed from unrestrained and DNA-origami-restrained simulations. Error bars were computed as the standard deviation of three independent estimates.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Schematics of the DNA-origami-based force spectrometer, reproduced from Figure 1 of Funke et al., 2016. (B) Schematics for the spatial restraints imposed on nucleosomes in our simulations to mimic the DNA-origami setup. The vertex angle between two arms of the DNA-origami system is denoted by $Φ$. The two cartoons on the side illustrate the angle between two nucleosome dyad axes and the angle between two nucleosome planes. To define the coordinate system and other notations, please refer to section ‘Simulations at high salt concentrations’ and the accompanying text.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Comparison between the simulated (black) and experimental (red) free energy profile as a function of the inter-nucleosome distance. Error bars were computed as the standard deviation of three independent estimates. The barrier observed between 60 Å and 80 Å arises from the unwinding of nucleosomal DNA when the two nucleosomes are in close proximity, as highlighted in the orange circle. (B) Comparison between the simulated (black) and experimental (red) free energy profile as a function of the vertex angle. Error bars were computed as the standard deviation of three independent estimates. (C) Illustration of the vertex angle $Φ$ used in panel (B).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** The average number of inter-nucleosome contacts between DNA and histone tails (A) or histone cores (B) is plotted as a function of the distance $r$. The error bars were estimated as the standard deviation of three equal partitions of the simulations.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** The unrestricted simulations favor a smaller angle $\theta$ between two nucleosomal planes compared to the DNA-origami-restrained simulations, related to Figure 4 of the main text.(A) Illustration of the collective variables used in the umbrella-sampling simulation. $\theta$ is the angle between two nucleosomal planes, and $r$ is the distance between the geometric centers of two nucleosomes. $w_{1}→$ and $w_{2}→$ represent the vectors perpendicular to the nucleosome planes. See text section ‘Simulations at high salt concentrations’ for further definitions of the collective variables. (B) 2D free energy landscape for nucleosome interactions under 35 mM NaCl and 11 mM MgCl2 salt, plotted as a function of $r$ and $\theta$. (C) The average value of $\theta$ as a function of the distance $r$ for the unrestricted (red) and the DNA-origami-restrained (black) simulations. The error bars were estimated as the standard deviation of three equal partitions of the simulations.

Strikingly, the two sets of simulations produced dramatically different binding free energies. Restricting nucleosome orientations produced a binding free energy of ∼2 kBT, reproducing the experimental value (Figure 4B, Figure 4—figure supplement 2). On the other hand, the binding free energy increased to 15 kBT upon removing the constraints.

Further examination of inter-nucleosomal contacts revealed the origin of the dramatic difference in nucleosome binding free energies. As shown in Figure 4C, the average number of contacts formed between histone tails and DNA from different nucleosomes is around 150 and 10 in the two sets of simulations. A similar trend is observed for histone core-DNA contacts across nucleosomes. The differences are most dramatic at small distances (Figure 4B, Figure 4—figure supplement 3) and are clearly visible in the most stable configurations. For example, from the unrestricted simulations, the most stable binding mode corresponds to a configuration in which the two nucleosomes are almost parallel to each other (see configuration A1’ in Figure 4A), with the angle between the two nucleosome planes close to zero (Figure 4B, Figure 4—figure supplement 4). However, the inherent design of the DNA-origami device renders this binding mode inaccessible, and the smallest angle between the two nucleosome planes is around 23° (see configuration A1 in Figure 4A). Therefore, a significant loss of inter-nucleosomal contacts caused the small binding free energy seen experimentally.

### Modulation of nucleosome binding free energy by in vivo factors

The predicted strength for unrestricted inter-nucleosome interactions supports their significant contribution to chromatin organization in vivo. However, the salt concentration studied above and in the DNA-origami experiment is much higher than the physiological value (Kaczmarczyk et al., 2020). To further evaluate the in vivo significance of inter-nucleosome interactions, we computed the binding free energy at the physiological salt concentration of 150 mM NaCl and 2 mM of MgCl2.

We observe a strong dependence of nucleosome orientations on the inter-nucleosome distance. A collective variable, $\theta$, was introduced to quantify the angle between the two nucleosomal planes (Figure 5A). As shown in two-dimensional binding free energy landscape of inter-nucleosome distance, $r$, and $\theta$ (Figure 5B), at small distances (∼60 Å), the two nucleosomes prefer a face-to-face binding mode with small $\theta$ values. As the distance increases, the nucleosomes will almost undergo a 90° rotation to adopt perpendicular positions. Such orientations allow the nucleosomes to remain in contact and is more energetically favorable. The orientation preference gradually diminishes at large distances once the two nucleosomes are completely detached. Importantly, we observed a strong inter-nucleosomal interaction with two nucleosomes wrapped by 147 bp 601-sequence DNA (∼9 kBT).

![Figure 5.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig5-v1.jpg)

**Figure 5.:** (A) Illustration of the collective variable, $\theta$, defined as the angle between two nucleosomal planes, and $r$ defined as the distance between the nucleosome geometric centers. $w_{1}→$ and $w_{2}→$ represent the axes perpendicular to the nucleosomal planes. (B) The 2D binding free energy profile as a function of $\theta$ and $r$ at the physiological salt condition (150 mM NaCl and 2 mM MgCl2) for nucleosomes with the 601 sequence. (C) Dependence of nucleosome binding free energy on nucleosome repeat length (NRL) and linker histone H1.0. Error bars were computed as the standard deviation of three independent estimates. (D) Representative structure showing linker histones (red and blue) mediating inter-nucleosomal contacts.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** See text section ‘Simulations at the physiological salt concentration’ for further discussions on simulation details. (A) Illustration of the collective variables used in umbrella-sampling simulations. $\theta$ is the angle between two nucleosomal planes, and $r$ is the distance between the geometric centers of two nucleosomes. $w_{1}→$ and $w_{2}→$ represent the vectors perpendicular to the nucleosome planes. (B) The free energy profile as a function of the distance $r$ between the geometric centers of two nucleosomes with 601, poly-dA:dT, and poly-dG:dC sequences. Error bars were computed as the standard deviation of three independent estimates. (C) The 2D free energy profiles as a function of $\theta$ and $r$. The simulations used nucleosomes with 601, poly-dA:dT, and poly-dG:dC sequences.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) The average number of inter-nucleosome contacts between histone proteins and nucleosomal DNA is plotted as a function of the distance $r$ between the geometric centers of two nucleosomes. The error bars were estimated as the standard deviation of three equal partitions of the simulations. (B) Representative structures from simulations with poly-dA:dT (left) and poly-dG:dC (right) nucleosomes. Noticeable DNA unwrapping can be seen in poly-dA:dT nucleosomes, contributing to the increased cross-nucleosome contacts.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/90073/elife-90073-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** See text section ‘Simulations at the physiological salt concentration’ for further discussions on simulation details. (A) Illustration of the collective variables used in the umbrella-sampling simulations. $\theta$ is the angle between two nucleosome planes, and $r$ is the distance between the geometric centers of two nucleosomes. $w_{1}→$ and $w_{2}→$ represent the vectors perpendicular to the nucleosome planes. (B) 2D free energy profiles as a function of $\theta$ and $r$ for the three systems indicated in the titles.

Furthermore, we found that the nucleosome binding free energy is minimally impacted by the precise DNA sequence. For example, when the 601 sequence is replaced with poly-dA:dT or poly-dG:dC, the free energy only varied by ∼2 kBT (Figure 5—figure supplement 1). However, the poly-dA:dT sequence produced stronger binding while poly-dG:dC weakened the interactions. The sequence specific effects are potentially due to the increased stiffness of poly-dA:dT DNA (Ortiz and de Pablo, 2011), which causes the DNA to unwrap more frequently, increasing cross-nucleosome contacts at larger distances (Figure 5—figure supplement 2).

In addition to variations in DNA sequences, in vivo nucleosomes also feature different linker lengths. We performed simulations that extend the 601 sequence with 10 extra base pairs of poly-dA:dT sequence at each end, reaching a nucleosome repeat length (NRL) of 167 bp. Consistent with previous studies (Mangenot et al., 2002; Correll et al., 2012; Huang et al., 2018), increasing the NRL weakened inter-nucleosomal interactions (Figure 5C and Figure 5—figure supplement 3), reducing the binding free energy to ∼6 kBT.

Importantly, we found that the weakened interactions upon extending linker DNA can be more than compensated for by the presence of histone H1 proteins. This is demonstrated in Figure 5C and Figure 5—figure supplement 3, where the free energy cost for tearing apart two nucleosomes with 167 bp DNA in the presence of linker histones (blue) is significantly higher than the curve for bare nucleosomes (red). Notably, at larger inter-nucleosome distances, the values even exceed those for 147 bp nucleosomes (black). A closer examination of the simulation configurations suggests that the disordered C-terminal tail of linker histones can extend and bind the DNA from the second nucleosome, thereby stabilizing the inter-nucleosomal contacts (as shown in Figure 5D). Our results are consistent with prior studies that underscore the importance of linker histones in chromatin compaction (Finch and Klug, 1976; Zhou et al., 2021), particularly in eukaryotic cells with longer linker DNA (Routh et al., 2008; Dombrowski et al., 2022).

## Discussion

We introduced a residue-level coarse-grained model with explicit ions to accurately account for electrostatic contributions to chromatin organization. The model achieves quantitative accuracy in reproducing experimental values for the binding affinity of protein-DNA complexes, the energetics of nucleosomal DNA unwinding, nucleosome binding free energy, and the sedimentation coefficients of nucleosome arrays. It captures the counterion atmosphere around the nucleosome core particle as seen in all-atom simulations (Materese et al., 2009) and highlights the contribution of counterions to nucleosome stability. The coarse-grained model also succeeds in resolving the difference between monovalent and divalent ions, supporting the efficacy of divalent ions in neutralizing negative charges and offsetting repulsive interactions among DNA segments.

One significant finding from our study is the predicted strong inter-nucleosome interactions under the physiological salt environment, reaching approximately 9 $k_{B}T$. We showed that the much lower value reported in a previous DNA-origami experiment is due to the restricted nucleosomal orientation inherent to the device design. Unrestricted nucleosomes allow more close contacts to stabilize binding. A significant nucleosome binding free energy also agrees with the high forces found in single-molecule pulling experiments that are needed for chromatin unfolding (Kruithof et al., 2009; Meng et al., 2015; Kaczmarczyk et al., 2020). We also demonstrate that this strong inter-nucleosomal interaction is largely preserved at longer NRL in the presence of linker histone proteins. While post-translational modifications of histone proteins may influence inter-nucleosomal interactions, their effects are limited, as indicated by Ding et al. (Ding et al., 2021), and are unlikely to completely abolish the significant interactions reported here. Therefore, we anticipate that, in addition to molecular motors, chromatin regulators, and other molecules inside the nucleus, intrinsic inter-nucleosome interactions are important players in chromatin organization in vivo.

We focused our study on single chromatin chains. Strong inter-nucleosome interactions support the compaction and stacking of chromatin, promoting the formation of fibril-like structures. However, as shown in many studies (Maeshima et al., 2016; Ricci et al., 2015; Ou et al., 2017; Zhang et al., 2022), such fibril configurations can hardly be detected in vivo. It is worth emphasizing that this lack of fibril configurations does not contradict our conclusion on the significance of inter-nucleosome interactions. In a prior paper, we found that many in vivo factors, most notably crowding, could disrupt fibril configurations in favor of inter-chain contacts (Liu et al., 2022). The inter-chain contacts can indeed be driven by favorable inter-nucleosome interactions.

Several aspects of the coarse-grained model presented here can be further improved. For instance, the introduction of specific protein-DNA interactions could help address the differences in non-bonded interactions between amino acids and nucleotides beyond electrostatics (Lin et al., 2021a). Such a modification would enhance the model’s accuracy in predicting interactions between chromatin and chromatin proteins. Additionally, the single-bead-per-amino-acid representation used in this study encounters challenges when attempting to capture the influence of histone modifications, which are known to be prevalent in native nucleosomes. Multiscale simulation approaches may be necessary (Collepardo-Guevara et al., 2015). One could first assess the impact of these modifications on the conformation of disordered histone tails using atomistic simulations. By incorporating these conformational changes into the coarse-grained model, systematic investigations of histone modifications on nucleosome interactions and chromatin organization can be conducted. Such a strategy may eventually enable the direct quantification of interactions among native nucleosomes and even the prediction of chromatin organization in vivo.

## Materials and methods

### Coarse-grained modeling of chromatin

The large system size of chromatin and the slow timescale for its conformational relaxation necessitates coarse-grained modeling. Following previous studies (Leicher et al., 2020; Ding et al., 2021; Lin et al., 2021a; Lin et al., 2021b; Liu et al., 2022), we adopted a residue-level coarse-grained model for efficient simulations of chromatin. The structure-based model (Clementi et al., 2000; Noel et al., 2016) was applied to represent the histone proteins with one bead per amino acid and to preserve the tertiary structure of the folded regions. The disordered histone tails were kept flexible without tertiary structure biases. A sequence-specific potential, in the form of the Lennard-Jones (LJ) potential and with the strength determined from the Miyazwa-Jernigan (MJ) potential (Miyazawa and Jernigan, 1985), was added to describe the interactions between amino acids. The 3SPN.2C model was adopted to represent each nucleotide with three beads and interactions among DNA beads follow the potential outlined in Freeman et al., 2014, except that the charge of each phosphate site was switched from –0.6 to –1.0 to account for the presence of explicit ions. The Coulombic potential was applied between charged protein and DNA particles. In addition, a weak, non-specific LJ potential was used to account for the excluded volume effect among all protein-DNA beads. Detail expressions for protein-protein and protein-DNA interaction potentials can be found in Ding et al., 2021, and the Appendix section ‘Coarse-grained protein-DNA model’.

We observe that residue-level coarse-grained models have been extensively utilized in prior studies to examine the free energy penalty associated with nucleosomal DNA unwinding (Lequieu et al., 2016; Parsons and Zhang, 2019; Zhang et al., 2016), sequence-dependent nucleosome sliding (Lequieu et al., 2017; Brandani et al., 2018), binding free energy between two nucleosomes (Moller et al., 2019), chromatin folding (Ding et al., 2021; Liu et al., 2022), the impact of histone modifications on tri-nucleosome structures (Chang and Takada, 2016), and protein-chromatin interactions (Watanabe et al., 2018; Leicher et al., 2020). The frequent quantitative agreement between simulation and experimental results supports the utility of such models in chromatin studies. Our introduction of explicit ions, as detailed in Appendix section ‘Coarse-grained explicit ion model’, further extends the applicability of these models to explore the dependence of chromatin conformations on salt concentrations.

### Coarse-grained modeling of counterions

Explicit particle-based representations for monovalent and divalent ions are needed to accurately account for electrostatic interactions (Freeman et al., 2011; Hinckley and de Pablo, 2015; Hayes et al., 2015; Denesyuk and Thirumalai, 2015; Denesyuk et al., 2018; Wang et al., 2022; Sun et al., 2022). We followed Freeman et al., 2011, to introduce explicit ions (see Figure 1) and adopted their potentials to describe the interactions between ions and nucleotide particles, with detailed expressions provided in the Appendix section ‘Coarse-grained explicit ion model’. Parameters in these potentials were tuned by Freeman et al., 2011, to reproduce the radial distribution functions and the potential of mean force between ion pairs determined from all-atom simulations.

This explicit ion model was originally introduced for nucleic acid simulations. We generalized the model for protein simulations by approximating the interactions between charged amino acids and ions with parameters tuned for phosphate sites. Parameter values for ion-amino acid interactions are provided in Table 1 and Table 2.

**Table 1.**
 Summary of parameters used to describe interactions between ions and charged particles.See text section ‘Coarse-grained explicit ion model’ for definitions of various parameters.


<table>
  <thead>
    <tr>
      <th>Coarse-grained pair</th>
      <th>ϵ(kcal/mol)</th>
      <th>σ(Å)</th>
      <th>rmϵ(Å)</th>
      <th>σϵ(Å)</th>
      <th>H1(kcal/mol)</th>
      <th>rmh1(Å)</th>
      <th>σh1(Å)</th>
      <th>H2(kcal/mol)</th>
      <th>rmh2(Å)</th>
      <th>σh2(Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>P-P</td>
      <td>0.18379</td>
      <td>6.86</td>
      <td>6.86</td>
      <td>0.5</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Na+-P</td>
      <td>0.02510</td>
      <td>4.14</td>
      <td>3.44</td>
      <td>1.25</td>
      <td>3.15488</td>
      <td>4.1</td>
      <td>0.57</td>
      <td>0.47801</td>
      <td>6.5</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>Na+-AA+*</td>
      <td>0.239</td>
      <td>4.065</td>
      <td>3.44</td>
      <td>1.25</td>
      <td>3.15488</td>
      <td>4.1</td>
      <td>0.57</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Na+-AA−†</td>
      <td>0.239</td>
      <td>4.065</td>
      <td>3.44</td>
      <td>1.25</td>
      <td>3.15488</td>
      <td>4.1</td>
      <td>0.57</td>
      <td>0.47801</td>
      <td>6.5</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>Mg2+-P</td>
      <td>0.1195</td>
      <td>4.87</td>
      <td>3.75</td>
      <td>1.0</td>
      <td>1.29063</td>
      <td>6.1</td>
      <td>0.5</td>
      <td>0.97992</td>
      <td>8.3</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>Mg2+-AA+</td>
      <td>0.239</td>
      <td>3.556</td>
      <td>3.75</td>
      <td>1.0</td>
      <td>1.29063</td>
      <td>6.1</td>
      <td>0.5</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Mg2+-AA−</td>
      <td>0.239</td>
      <td>3.556</td>
      <td>3.75</td>
      <td>1.0</td>
      <td>1.29063</td>
      <td>6.1</td>
      <td>0.5</td>
      <td>0.97992</td>
      <td>8.3</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>Cl−-P</td>
      <td>0.08121</td>
      <td>5.5425</td>
      <td>4.2</td>
      <td>0.5</td>
      <td>0.83652</td>
      <td>6.7</td>
      <td>1.5</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Cl−-AA+</td>
      <td>0.239</td>
      <td>4.8725</td>
      <td>4.2</td>
      <td>0.5</td>
      <td>0.83652</td>
      <td>6.7</td>
      <td>1.5</td>
      <td>0.47801</td>
      <td>5.6</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>Cl−-AA−</td>
      <td>0.239</td>
      <td>4.8725</td>
      <td>4.2</td>
      <td>0.5</td>
      <td>0.83652</td>
      <td>6.7</td>
      <td>1.5</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Na+-Na+</td>
      <td>0.01121</td>
      <td>2.43</td>
      <td>2.7</td>
      <td>0.57</td>
      <td>0.17925</td>
      <td>5.8</td>
      <td>0.57</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Na+-Mg2+</td>
      <td>0.04971</td>
      <td>2.37</td>
      <td>2.37</td>
      <td>0.5</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Na+-Cl−</td>
      <td>0.08387</td>
      <td>3.1352</td>
      <td>3.9</td>
      <td>2.06</td>
      <td>5.49713</td>
      <td>3.3</td>
      <td>0.57</td>
      <td>0.47801</td>
      <td>5.6</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>Mg2+-Mg2+</td>
      <td>0.89460</td>
      <td>1.412</td>
      <td>1.412</td>
      <td>0.5</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Mg2+-Cl−</td>
      <td>0.49737</td>
      <td>4.74</td>
      <td>4.48</td>
      <td>0.57</td>
      <td>1.09943</td>
      <td>5.48</td>
      <td>0.44</td>
      <td>0.05975</td>
      <td>8.16</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>Cl−-Cl−</td>
      <td>0.03585</td>
      <td>4.045</td>
      <td>4.2</td>
      <td>0.56</td>
      <td>0.23901</td>
      <td>6.2</td>
      <td>0.5</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_*Positive amino acids.†Negative amino acids._

**Table 2.**
 Summary of parameters used to describe the WCA interactions between ions and neutral particles.See text section ‘Coarse-grained explicit ion model’ for definitions of various parameters.


<table>
  <thead>
    <tr>
      <th>Coarse-grained pair</th>
      <th>ϵ(kcal/mol)</th>
      <th>σ(Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Na+-S*</td>
      <td>0.239</td>
      <td>4.315</td>
    </tr>
    <tr>
      <td>Na+-A†</td>
      <td>0.239</td>
      <td>3.915</td>
    </tr>
    <tr>
      <td>Na+-T‡</td>
      <td>0.239</td>
      <td>4.765</td>
    </tr>
    <tr>
      <td>Na+-G§</td>
      <td>0.239</td>
      <td>3.665</td>
    </tr>
    <tr>
      <td>Na+-C¶</td>
      <td>0.239</td>
      <td>4.415</td>
    </tr>
    <tr>
      <td>Na+-AA**</td>
      <td>0.239</td>
      <td>4.065</td>
    </tr>
    <tr>
      <td>Mg2+-S</td>
      <td>0.239</td>
      <td>3.806</td>
    </tr>
    <tr>
      <td>Mg2+-A</td>
      <td>0.239</td>
      <td>3.406</td>
    </tr>
    <tr>
      <td>Mg2+-T</td>
      <td>0.239</td>
      <td>4.256</td>
    </tr>
    <tr>
      <td>Mg2+-G</td>
      <td>0.239</td>
      <td>3.156</td>
    </tr>
    <tr>
      <td>Mg2+-C</td>
      <td>0.239</td>
      <td>3.906</td>
    </tr>
    <tr>
      <td>Mg2+-AA**</td>
      <td>0.239</td>
      <td>3.556</td>
    </tr>
    <tr>
      <td>Cl−-S</td>
      <td>0.239</td>
      <td>5.1225</td>
    </tr>
    <tr>
      <td>Cl−-A</td>
      <td>0.239</td>
      <td>4.7225</td>
    </tr>
    <tr>
      <td>Cl−-T</td>
      <td>0.239</td>
      <td>5.5725</td>
    </tr>
    <tr>
      <td>Cl−-G</td>
      <td>0.239</td>
      <td>4.4725</td>
    </tr>
    <tr>
      <td>Cl−-C</td>
      <td>0.239</td>
      <td>5.2225</td>
    </tr>
    <tr>
      <td>Cl−-AA**</td>
      <td>0.239</td>
      <td>4.8725</td>
    </tr>
  </tbody>
</table>

_*Sugar.†Adenine base.‡Thymine base.§Guanine base.¶Cytosine base.**Non-charged amino acids._

### Details of molecular dynamics simulations

We simulated various chromatin systems, including a single-nucleosome, two-nucleosomes, and a 12-mer nucleosome array. The initial configurations for the molecular dynamics simulations were constructed based on the crystal structure of a single nucleosome with PDB ID: 1KX5 (Davey et al., 2002) and 3LZ1 (Vasudevan et al., 2010), or a tetranucleosome with PDB ID: 1ZBB (Schalch et al., 2005). We used the 3DNA software (Lu and Olson, 2003) to add additional DNA, connect and align nucleosomes, and extend the chain length as necessary. Further details on constructing the initial configurations are provided in the Appendix section ‘Ionic dependence of the conformation for a 12-mer nucleosomal array’. Chromatin was positioned at the center of a cubic box with a length selected to avoid interactions between nucleosomes and their periodic images. Counterions were added on a uniformly spaced grid to achieve the desired salt concentrations and neutralize the system. The number of ions and the size of simulation boxes are provided in Table 3.

**Table 3.**
 Summary of simulation setups used in this study.Additional simulation details can be found in text section ‘Molecular dynamics simulation details’.


<table>
  <thead>
    <tr>
      <th>Studies</th>
      <th>Box size (nm3)</th>
      <th>Number of Na+</th>
      <th>Number of Mg2+</th>
      <th>Number of Cl−</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Single nucleosome 100 mM NaCl+0.5 mM MgCl2</td>
      <td>216,000</td>
      <td>13,017</td>
      <td>65</td>
      <td>13,003</td>
    </tr>
    <tr>
      <td>Twelve nucleosomes 5 mM NaCl</td>
      <td>1,331,000</td>
      <td>6196</td>
      <td>0</td>
      <td>4006</td>
    </tr>
    <tr>
      <td>Twelve nucleosomes 150 mM NaCl</td>
      <td>216,000</td>
      <td>21,695</td>
      <td>0</td>
      <td>19,505</td>
    </tr>
    <tr>
      <td>Twelve nucleosomes 0.6 mM MgCl2</td>
      <td>3,375,000</td>
      <td>0</td>
      <td>2314</td>
      <td>2438</td>
    </tr>
    <tr>
      <td>Twelve nucleosomes 1 mM MgCl2</td>
      <td>3,375,000</td>
      <td>0</td>
      <td>3127</td>
      <td>4064</td>
    </tr>
    <tr>
      <td>Two 147 bp 601-seq nucleosomes 35 mM NaCl+11 mM MgCl2</td>
      <td>125,000</td>
      <td>2922</td>
      <td>828</td>
      <td>4290</td>
    </tr>
    <tr>
      <td>Two 147 bp 601-seq nucleosomes 150 mM NaCl+2 mM MgCl2</td>
      <td>216,000</td>
      <td>19,505</td>
      <td>260</td>
      <td>19,737</td>
    </tr>
    <tr>
      <td>Two 147 bp poly-dA:dT nucleosomes 150 mM NaCl+2 mM MgCl2</td>
      <td>216,000</td>
      <td>19,505</td>
      <td>260</td>
      <td>19,737</td>
    </tr>
    <tr>
      <td>Two 147 bp poly-dG:dC nucleosomes 150 mM NaCl+2 mM MgCl2</td>
      <td>216,000</td>
      <td>19,505</td>
      <td>260</td>
      <td>19,737</td>
    </tr>
    <tr>
      <td>Two 167 bp 601-seq nucleosomes 150 mM NaCl+2 mM MgCl2</td>
      <td>216,000</td>
      <td>19,505</td>
      <td>260</td>
      <td>19,657</td>
    </tr>
    <tr>
      <td>Two 167 bp 601-seq nucleosomes with H1.0 150 mM NaCl+2 mM MgCl2</td>
      <td>216,000</td>
      <td>19,505</td>
      <td>260</td>
      <td>19,763</td>
    </tr>
  </tbody>
</table>

All simulations were performed at constant temperature and constant volume (NVT) using the software package LAMMPS (Plimpton, 1995). The electrostatic interactions were implemented with the particle-particle particle-mesh solver, with the relative root-mean-square error in per-atom force set to 0.0001 (Hockney and Eastwood, 2021). A Nosé-Hoover style algorithm (Shinoda et al., 2004) was used to maintain the system temperature at 300 K with a damping parameter of 1 ps. We further modeled the histone core and the inner layer of the nucleosomal DNA together as a rigid body to improve computational efficiency. This approximation does not affect the thermodynamic properties of chromatin (Ding et al., 2021; Liu et al., 2022). Umbrella simulations were used to enhance the sampling of the conformational space (Torrie and Valleau, 1977), and details of the collective variables employed in these simulations are provided in the Appendix section ‘Molecular dynamics simulation details’. All the results presented in the main text are reweighted from the biased simulations by the weighted histogram algorithm (Kumar et al., 1992).

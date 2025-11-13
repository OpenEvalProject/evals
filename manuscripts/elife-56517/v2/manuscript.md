# Inherent regulatory asymmetry emanating from network architecture in a prevalent autoregulatory motif

## Authors

- Md Zulfikar Ali<sup>1</sup> ([ORCID: 0000-0002-7054-0059](https://orcid.org/0000-0002-7054-0059))
- Vinuselvi Parisutham<sup>1</sup> ([ORCID: 0000-0002-0349-4072](https://orcid.org/0000-0002-0349-4072))
- Sandeep Choubey<sup>3</sup> ([ORCID: 0000-0002-7387-6148](https://orcid.org/0000-0002-7387-6148))
- Robert C Brewster<sup>1</sup> ([ORCID: 0000-0002-7656-4086](https://orcid.org/0000-0002-7656-4086)) †

### Affiliations

1. Program in Systems Biology, University of Massachusetts Medical School Worcester United States
2. Department of Microbiology and Physiological Systems, University of Massachusetts Medical School Worcester United States
3. Max Planck Institute for the Physics of Complex Systems Dresden Germany

† Corresponding author

## Abstract

Predicting gene expression from DNA sequence remains a major goal in the field of gene regulation. A challenge to this goal is the connectivity of the network, whose role in altering gene expression remains unclear. Here, we study a common autoregulatory network motif, the negative single-input module, to explore the regulatory properties inherited from the motif. Using stochastic simulations and a synthetic biology approach in E. coli, we find that the TF gene and its target genes have inherent asymmetry in regulation, even when their promoters are identical; the TF gene being more repressed than its targets. The magnitude of asymmetry depends on network features such as network size and TF-binding affinities. Intriguingly, asymmetry disappears when the growth rate is too fast or too slow and is most significant for typical growth conditions. These results highlight the importance of accounting for network architecture in quantitative models of gene expression.

## Introduction

The genomics revolution has enabled biology with the ability to read, write and assemble DNA at the genome scale with single base pair resolution. These advancements have provided an important tool for the field of gene regulation that aims to predict gene expression from the regulatory code, inscribed in DNA (Carey et al., 2013; Kosuri et al., 2013; Sharon et al., 2012). This approach relies on quantitative measurements of gene expression as the regulatory DNA is systematically designed to induce regulation by various transcription factors (TFs) at specific positions or with differing affinities. However, success in predicting expression levels of natural genes from sequence alone has been relatively modest. One obvious complication is that genes are not isolated but rather exist in dense, interconnected networks. The concept of network motifs, defined as overrepresented patterns of connections between genes and TFs in the network, helps to digest these large networks into smaller subgraphs with specific properties; each of these motifs can be interpreted as performing a particular 'information processing' function that is determined by the connectivity and regulatory role of the genes in the motif (Alon, 2006; Alon, 2007; Davidson, 2006; Mangan and Alon, 2003; Tkacik et al., 2008). In this study, we dissect a prevalent gene regulation motif, the single-input module (SIM), to demonstrate the influence of network size and connectivity on the regulation of a network motif.

The SIM is a network motif where a single TF regulates the expression of a set of genes, including itself (Figure 1A). In E. coli, this motif is prevalent; the majority of TFs are autoregulated and have multiple targets (Santos-Zavaleta et al., 2019). Typically, this group of genes have related functions and the purpose of this motif is to coordinate, in both time and magnitude, expression of these related genes (Alon, 2006). There are mounting examples, from diverse topics that range from metabolism (Figure 1B, Zaslaver et al., 2004), stress response (Figure 1C, Friedman et al., 2005; Ronen et al., 2002), development (Arnone, 2002; Gaudet and Mango, 2002; Kalir et al., 2001), and cancer (Lorenzin et al., 2016), where temporal ordering of gene expression in the motif naturally follows the functional order of the genes in the physiological pathway. Mechanistically, it is thought that this ordering is set through differential affinity for the TF amongst the various target genes in the motif (Alon, 2006), although in some experiments temporal ordering was not observed implying a dependence on physiology or another experimental detail that is yet unrecognized (Gerosa et al., 2013; Schmidt et al., 2016). Due to the broad importance of these motifs, a quantitative understanding of how SIM motifs can be encoded, designed and optimized, will be instrumental in gaining a deep and fundamental understanding of the spatial and temporal features of a diverse set of cellular phenomena.

![Figure 1.](https://cdn.elifesciences.org/articles/56517/elife-56517-fig1-v2.jpg)

**Figure 1.:** (A) Schematic of a canonical SIM motif: A single TF regulates itself and several other genes. (B and C) Examples of SIM motifs in E. coli. (B) ArgR is a transcriptional regulator of arginine biosynthesis. It auto-regulates itself and genes involved in different steps of arginine biosynthesis with precision in expression starting from the first enzyme of the pathway down to the last. This precise ordering is thought to originate from a corresponding ordering in TF-binding affinities of the target genes. (C) LexA is the master regulator of SOS pathway and is actively degraded in response to DNA damage. LexA auto-represses itself and represses a set of other genes involved in DNA repair. In this case, the early response genes have low affinity for the repressor while the late acting genes have high affinity, enabling temporal ordering of the response. (D) Histogram showing the number of known regulated genes for every TF in E. coli. Inset shows different modes of regulation of the TF genes. 62% of the TF genes are autoregulated with 42% negatively autoregulated and 20% positively auotregulated. (E) Schematic of the experimental model of a SIM motif used in this study. Here, LacI-mCherry is the model TF and YFP is the protein product of the target gene. Decoys sites are used to control the network size by simulating the demand of other target genes in the SIM motif. (F) Representation of the tunable parameter space detailed in this study. We can systematically tune the TF unbinding rate, number of decoys and protein degradation rate in the experimental system and adjust these parameters accordingly in simulations.

To quantitatively explore the input-output relationship of the SIM motif, we use a synthetic biology approach that boils the motif down to its most basic components: an autoregulated TF gene, a sample target gene, and competing binding sites. Using E. coli as a model organism, we build this motif in vivo. We use non-functional ‘decoy’ binding sites to exert competition for the TF and mimic the demand of the other genes in the motif (which will depend on the size of the network, Figure 1D; Gillespie, 1977; Shen-Orr et al., 2002). However, the demand for the TF could also stem from a litany of sources such as random non-functional sites in the genome (Bakk and Metzler, 2004; Kemme et al., 2016; Lee and Maheshri, 2012; Mirny, 2010) or non-DNA-based obstruction or localization effects that transiently interfere with a TFs ability to bind DNA. Because of the design, our results do not depend on the nature of the TF competition. SIM TFs typically exert the same regulatory role on all targets of the motif (Shen-Orr et al., 2002). As such, in this work, we will focus on a TF that is a negative regulator of its target genes and itself; this is the most common regulation strategy in Escherichia coli where roughly 60% of TF genes are autoregulated and almost 70% of those TFs negatively regulate their own expression (inset Figure 1D, Shen-Orr et al., 2002).

We use stochastic simulations of kinetic models (Gillespie, 1977; Gillespie, 2007; Kaern et al., 2005; Shahrezaei and Swain, 2008), to predict how the overall level of gene expression depends on parameters characterizing cellular environment such as TF-binding affinities and the number of competing binding sites. To test these predictions in vivo, we built a synthetic system with LacI as a model TF, and individually tune each of these parameters. Past work with LacI has demonstrated the ability to control with precision the regulatory function, binding affinity and TF copy number through basic sequence level manipulations (Brewster et al., 2014; Choi et al., 2008; Garcia and Phillips, 2011; Jones et al., 2014; Kuhlman et al., 2007; Oehler et al., 1990; Razo-Mejia et al., 2018); Here, we use that detailed knowledge to inform our simulations which then guide our experiments (and vice versa).

Our approach reveals that the presence of competing TF-binding sites can have counterintuitive effects on the mean expression levels of the TF and its target genes due to the opposing relationship between free TFs and total TFs (total TF is the sum of free TF and TF bound to promoters and decoy binding sites). Furthermore, we find that the TF and target gene experience quantitatively different levels of regulation in the same cell, and with the same regulatory sequence. We show that this regulatory asymmetry is sensitive to features such as the degradation rate, TF-binding affinity and the number of competing binding sites for the TF. The stochastic simulation makes accurate predictions of the asymmetry and its dependence on the parameters of the model that we confirm through in vivo measurements. Interestingly, regulatory asymmetry is not captured by a simple deterministic model which is based on translating the stochastic reactions to kinetic rates through mass action equilibrium kinetics (which have been shown to accurately predict target gene expression in other studies [Brewster et al., 2014; Garcia and Phillips, 2011; Garcia et al., 2012; Jones et al., 2014; Razo-Mejia et al., 2018]). In fact, this deterministic model fails to accurately predict expression of either gene. A revised deterministic model, which explicitly allows for different microenvironments in each ‘regulatory state’, predicts asymmetry, although it still does not recover quantitative agreement with stochastic simulations.

## Results

### Matching molecular biology with simulation methodology

We use a combination of theory and experimental in vivo measurements on engineered E. coli strains to study the interplay between TF gene, target gene, and additional binding sites of a negative autoregulatory SIM network motif. The basic regulatory system is outlined in Figure 1E. We use a stochastic model of the SIM motif to explore how the expression of the TF gene and one target gene depends on parameters such as TF-binding affinity and number of other binding sites in the network (here modeled and controlled through competing, non-regulatory decoy sites [Burger et al., 2010]). In this model, the TF gene and target gene can be independently bound by a free TF to shut off gene expression until the TF unbinds. The two genes (TF-encoding and target) compete with decoy binding sites which can also bind free TFs. Each free TF can bind any open operator site with equal probability (set by the binding rate). The unbinding rate can be set individually for the TF gene, target gene and decoy sites and is related to the specific base pair identity of the bound operator site (Kinney et al., 2010; Maerkl and Quake, 2007; Stormo, 2000; Weirauch et al., 2013). We employ stochastic simulations to make specific predictions for how the expression level of the TF and target genes depend on the various parameters of the model. Furthermore, we translate these stochastic processes into a deterministic ODE model using equilibrium mass action kinetics (see Appendix 6: Deterministic solution). A thorough discussion on how we chose the kinetic parameters of our model is presented in the Materials and methods section.

In experiments, the corresponding system is constructed with an integrated copy of both the TF (LacI-mCherry) and target gene (YFP) with expression of both genes controlled by identical promoters with a single LacI-binding site centered at +11 relative to their transcription start sites (Brewster et al., 2014; Garcia and Phillips, 2011). As demonstrated in Figure 1F, decoy binding sites are added by introducing a plasmid with an array of TF-binding sites (between 0 to 5 sites per plasmid) enabling control of up to roughly 300 binding sites per cell (for average plasmid copy number measured by qPCR, see Materials and methods and Appendix 3—figure 1). TF unbinding rate is controlled by changing the sequence identity of the operator sites; the binding sequence assessed in this study include (in order of increasing affinity) O2, O1 and Oid. The decoy binding site arrays are constructed using the Oid operator site. We quantify regulation through measurements of fold-change (FC) in expression which is defined as the expression level of a gene in a given condition (typically a specific number of decoy binding sites) divided by the expression of that gene when it is unregulated. For the target gene, we can always measure unregulated expression simply by measuring expression in a LacI knockout strain. However, it is challenging to measure unregulated expression for the autoregulated gene. For autoregulation, this unregulated expression can be measured by exchanging the TF-binding site with a mutated non-binding version of the site. For O1 there is a mutated sequence (NoO1v1, Oehler et al., 1994) that we have shown relieves repression of the target gene comparable to a strain expressing no TF (see Appendix 4—figure 1A), which allows us to calculate fold-change even for the autorepressed gene. Despite testing many different mutated sites and strategies, we could not find a corresponding sequence for O2 and Oid so we focus primarily on studying a TF gene regulated by O1 (see Appendix 4: Constitutive values for autoregulatory gene, for more discussion).

### Decoy sites increase expression of the auto-repressed gene and its targets

We first investigate the negatively regulated SIM motif where the TF and target gene have identical promoters and TF binding sites (O1) and the number of (identical) competing binding sites are varied systematically (schematically shown in Figure 1E,F). Simulation and experimental data for Fold-change of the TF gene as a function of number of decoys is shown in Figure 2A as red lines (simulation) and red points (experiments). We find that increasing the number of decoy sites increases the expression of the auto-repressed TF gene monotonically. To interpret why the TF level increases, in Figure 2B we plot the number of ‘free’ TFs in our simulation (defined as TFs not bound to an operator site) as a function of decoy site number. The solid line demonstrates that on average, despite the increased average number of TFs in the cell, the number of unbound TFs decreases as the number of competing binding sites increases (Nevozhay et al., 2009). Therefore, because the number of available repressors decreases, the overall level of repression also decreases and thus the mean expression of the TF gene rises.

![Figure 2.](https://cdn.elifesciences.org/articles/56517/elife-56517-fig2-v2.jpg)

**Figure 2.:** (A) Fold-change in the expression level of both the autoregulated gene (red) and the TF's target gene (blue) as a function of the number of competing binding sites present. Simulation data is shown as solid curves. Different symbols represent independent biological replicates. Each data point in y-axis is the bootstrapped mean of individual decoy strains and the error bars represent the standard deviation of bootstrapped mean. Each data point in x-axis is the mean of three technical replicates and the error bar is the corresponding standard deviation. (B) Increasing the number of competing binding sites increases the expression of both the TF (red line) and target genes by lowering the overall number of free TFs (black line). (C) Simple kinetic model describing the SIM motif using mass action equilibrium kinetics. For compactness of the figure, the reactions involving the decoy binding sites, dimerization/dedimerization of TF monomers, and transcription steps are not shown. Full reactions of the model are described in Appendix 6.

Now we consider the effect of competition on the expression of SIM target genes. We measure our system with O1 as the regulatory binding site for both TF and target genes. In Figure 2A, the expression of the target gene is shown as blue points (experiments) and blue lines (simulation) for the SIM motif with different numbers of decoy TF-binding sites (from 0 sites up to five per plasmid). Just as in the case of the TF gene, we once again see that the expression of the target gene increases as more decoy binding sites are added even though the total number of TFs is also increasing (red points and line). Qualitatively, we expected this result since the free TF number is expected to decrease (Figure 2B) and, in turn, the expression of any gene targeted by the autoregulated repressing TF will increase. While the mechanism is more obvious in this controlled system, it is important to note that this is a case where more repressors correlate with more expression of the repressed gene. It is easy to see how this relationship could be misinterpreted as activation in more complex in vivo system if the competition level of the TF is (advertently or otherwise) altered in experiments.

### Asymmetry in gene regulation between TF and target genes

Quantitative inspection of Figure 2A reveals an interesting detail: Even when the regulatory region of the auto-repressed gene and the target gene are identical, we find that the expression (fold-change or FC) is higher for the target gene, raising the question of how two genes with identical promoters and regulatory binding sites in the same cell can have different regulation levels. In this data, both the TF gene and target gene are regulated by a single repressor-binding site (O1) immediately downstream of the promoter. This regulatory scheme is often referred to as 'simple repression' (Bintu et al., 2005; Garcia and Phillips, 2011; Phillips et al., 2013). Drawing our intuition from a simple deterministic model of regulation based on translating the stochastic reactions to kinetic rate equations (Figure 2C and Appendix 6: Deterministic solution), we find that regardless of the network architecture (autoregulation, constitutive TF production, number of competing sites, etc.), the fold-change of any gene is expected to follow a simple scaling relation,

$$
Fold−change=\frac{1}{1+R^{∗}},R^{∗}=R_{free}\frac{k_{on}}{k_{off}+\gamma}.
$$

where, $R_{free}$ is the number of free (unbound) TFs and $k_{on}/(k_{off}+\gamma)$ represents the affinity of the specific TF binding site in the thermodynamic framework (Rydenfelt et al., 2014). This calculation is applicable for both the TF and the target gene and would predict a ‘symmetric’ response for identical regulatory regions. This model performs well for this same promoter in a related system where the TF is induced or constitutively expressed and predicts the fold-change for a wide range of perturbations such as promoter strength, TF-binding site, induction condition and TF competition levels are tuned (data accumulated in Figure 3A, adapted from Phillips et al., 2019). However, it has been shown that the regulation of an autorepressed gene can diverge from this prediction (Hahl and Kremling, 2016; Hornos et al., 2005; Milias-Argeitis et al., 2015). In Figure 3, we show simulation data for the fold-change versus number of scaled-free TFs ($R^{*}$) for the autoregulatory gene (red line) and its target gene (blue line) with O1 (Figure 3C) or O2 (Figure 3B) binding sites, where we are changing the number of free TFs by tuning the number of competing-binding sites. In each plot, we also show simulations for the fold-change of a single target gene with a TF undergoing constitutive (constant in time) expression where the TF is controlled by either changing the expression level of the TF (purple stars) or adding competing-binding sites while maintaining a set constitutive expression level (purple circles). In both cases, where TFs are made constitutively, the simulation data agrees well with the deterministic model predictions. However, for the autoregulatory circuits, we find that for strong binding sites (O1) neither the target nor the TF gene follow the deterministic solution (black dashed line). In this case, the asymmetry occurs with the TF gene being more repressed and the target gene less repressed than expected.

![Figure 3.](https://cdn.elifesciences.org/articles/56517/elife-56517-fig3-v2.jpg)

**Figure 3.:** (A) Fold-change vs scaled free TF in the thermodynamic model for a collection of simple repression data (open circles) where free TF is controlled through a diverse range of mechanisms. The data collapse to the deterministic model predictions (dashed curve). (B–C) Fold-change vs scaled free TF in simulations using the actual free TF obtained from simulation. The data for a constitutive expressed TF where free TF is varied by changing TF production rate (purple circles) or number of decoy sites (purple stars) collapses to the deterministic solution, however, the regulation of genes in the SIM motif (target: red line, TF gene: blue line) both diverge from the deterministic solution in opposing ways, giving rise not only to asymmetry but also a disagreement with deterministic modeling for both genes. (D) Fold-change in the target gene versus fold-change in the TF gene. Each data point is the bootstrapped mean of fold-change in TF and target expression across hundreds of cells with a given number of competing binding sites and error bars represent the standard deviation of the bootstrapped mean. Different symbols represent independent biological replicates. In all cases, the TF gene is regulated by an O1 binding sites, whereas the target is regulated by (in order of weakest binding to strongest binding): O2 (purple), O1 (yellow) or Oid (blue). Simulation data is shown as solid curves.

Since ‘free TF concentration’ is not readily available in experiments, we demonstrate asymmetry in experimental results explicitly in , where we plot the fold-change of the target gene against fold-change of the TF gene. In this figure, the data points are derived from measurements made in six different competition levels (from 0 to 5 decoy binding sites per plasmid). Each data point represents the average expression level of each gene for a given number of competing binding sites. The lines represent results from the stochastic simulations where we systematically vary competition levels by introducing decoy binding sites and the fold-change of both the TF and target gene are calculated. The simple deterministic model prediction that identical promoters (yellow data, Figure 3D) should experience identical levels of regulation (see Appendix 6—figure 1C, Sanchez et al., 2011) would cause the data to fall on the black dashed one-to-one line. However, for both simulations and experiments of this system the TF gene is clearly more strongly regulated than the target gene subject to identical regulatory sequences.

To examine the extent of asymmetry in this system, we adjust the target binding site to be of higher affinity (Oid, blue lines and data points in Figure 3D) or weaker (O2, purple lines and data points in Figure 3D). Clearly, this should change the symmetry of the regulation, after all the TF-binding sites on the promoters are now different and symmetry is no longer to be expected. The experiments and simulations once again agree well. However, when Oid regulates the target gene and O1 regulates the TF gene, the regulation is now roughly symmetric despite the target gene having a much stronger binding site; in this case, the size of the inherent regulatory asymmetry effect is on par with altering the binding site to a stronger operator resulting in symmetric overall regulation of the genes.

### Mechanism of asymmetric gene regulation

The difference in expression between the TF and its target can be understood by studying the TF-operator occupancy for each gene, drawn schematically in Figure 4A. This cartoon shows the four possible promoter occupancy states of the system: (1) both genes unbound by TF, (2) target gene bound by TF, TF gene unbound, (3) TF gene bound by TF, target gene unbound, and (4) both genes bound by TF. It should be clear that state 1 and state 4 cannot be the cause of asymmetry; both genes are either fully on (state 1) or fully off (state 4). As such, the asymmetry must originate from differences in states 2 and 3. In state 2, the TF gene is ‘on’ while the target gene is fully repressed and in state 3 the opposite is true. Since we know that the asymmetry appears as more regulation of the TF gene than the target gene, then it must be the case that the system spends less time in state 2 than in state 3. There are two paths to exit either of these states: unbinding of the TF from the bound operator or binding of the TF to the free operator. Since unbinding rate of a TF is identical for both promoters in our model, the asymmetry must originate from differences in binding of free TF in state 2 and in state 3; specifically state 2 must have an (on average) higher concentration of TF than state 3. This makes sense since the system is still making TF in state 2, while production of TF is shut off in state 3. Figure 4B validates this interpretation as we can see that state 2 has on average more free TFs than state 3, and as a result, the system spends less time in state 2 than in state 3 in our simulations. As such, the asymmetry comes from the fact that the two genes, despite being in the same cell and experiencing the same average intracellular TF concentrations, are exposed to systematically different concentrations of TF when the TF and target gene are in their respective ‘active’ states. To quantify regulatory asymmetry, we define asymmetry as the difference in fold-change of the target and the fold-change of the TF gene (asymmetry =$FC_{target}-FC_{TF}$). Using the chemical master equation (CME) approach, we find that the asymmetry is exactly equal to the difference in time spent in state 3 and state 2, for any condition or parameter choice (Figure 4C and Appendix 9 Equation A9-9: CME for minimal model). Furthermore, the asymmetry can be written as the difference of TF concentration in state 2 and state 3 and is given by

$$
Asymmetry=\frac{k_{on}}{k_{off}+\gamma}⁢(n_{2}-n_{3}),
$$

where, n2 and n3 are the TF concentrations in state 2 and state 3, respectively. In Figure 4D, we show that the asymmetry obtained using the difference in TF concentration precisely match with the asymmetry calculated from the fold-change expression. However, it is important to note that this is not a complete analytic solution for asymmetry because n2 and n3 are unsolved functions of the model parameters.

![Figure 4.](https://cdn.elifesciences.org/articles/56517/elife-56517-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of the TF-operator occupancy with their corresponding transition rates. The $k_{on}$ for transition from state 1 to state 2 or state 3 will be identical and hence cannot account for the asymmetry. State 2 and state 3 on the other hand, will encounter a difference in the free TF concentration and hence the $k_{on}$ for transition from one of these states to state 4 will be different; thus, accounting for the asymmetry in expression between the TF and the target. (B) Plot showing the average number of free TFs in different states and fraction of time cells spends in each of the given state in the simulation. (C) Plot showing asymmetry as a function of fractional time difference between state 2 and state 3. (D) Plot showing asymmetry as a function of difference in free TF concentration between state 3 and state 2. (E) Heat map showing the phase space of maximum asymmetry as a function of binding affinity for the TF and its half-life. (F) Tuning the TF degradation rate influences the extent of asymmetry observed in the SIM module. Yellow points corresponds to the system with no degradation tags; Blue points corresponds to degradation by a ‘weak’ or ‘slow’ tag (DAS tag with a rate of 0.00063 per min per enzyme); Green points corresponds to a slightly faster tag (DAS + 4 with a rate of 0.0011 per min per enzyme ); Red points corresponds to a very fast tag (LAA tag with a rate of 0.21 per min per enzyme ). Different symbols represent independent biological replicates.

The asymmetry in the expression of TF and target genes stems from systematically differential TF concentration in the states when the TF gene is occupied (and target gene is expressing) and when the target gene is occupied (and the TF gene is expressing). The general approach of ODEs outlined above (Figure 2C) does not account for this differential TF concentration and hence shows no asymmetry. Armed with the knowledge that individual states have this systematic TF difference, we can rewrite the basic deterministic model where we instead keep track individually of each state and the specific TF concentration of that state using the same equilibrium mass action kinetic approach (details in Appendix 10: Modified ODEs for the minimal model). Like the stochastic CMEs, the modified ODEs predict that the asymmetry arises from the difference in the TF concentrations in different states and solely depends on the difference in time spent in state 3 (only target gene occupied) and state 2 (only TF gene occupied). Although we find the modified deterministic model can predict asymmetry, it still does not quantitatively agree with the results of stochastic modeling due to the deterministic model not accounting for variability in TF number in each state (see Appendix 10: Modified ODEs for the minimal model). As a result, in the following sections, we will compare our experiments to stochastic simulations based on the full CME formalism.

### Dependence of regulatory asymmetry on TF degradation and binding affinity

According to the above-proposed mechanism, the regulatory asymmetry stems from differences in the cellular TF concentration when the TF is bound to the target versus when it is bound to the autoregulatory gene, as such we expect that binding affinity will play a central role in setting asymmetry levels. This is also evident from Figure 3B,C where we find that the deviation of the expression of both TF and target gene is more prominent for a strong binding site (Oid or O1) compared to a weaker binding site (O2). Furthermore, there are many parameters associated with the production and decay of TF and target mRNA and protein which could also influence the asymmetry. To reveal which (if any) of these parameters is important to asymmetry, we calculate the maximum asymmetry (the maximum value of asymmetry found as competing site number is controlled, Appendix 7—figure 1A) using simulation as these production and degradation parameters are tuned. First, we find that tuning the rates of target gene production and decay has no effect on asymmetry (Appendix 7—figure 1B and Appendix 11—figure 1B). On the other hand, for TF production and decay each parameter has some effect on asymmetry. However, we find that the biggest driver of asymmetry in this set of parameters is the protein degradation rate (Appendix 7—figure 1B). As such, we focus on two crucial parameters that control the asymmetry: TF-binding affinity and TF degradation rate. In Figure 4E, we show a heat map of the maximum asymmetry as a function of the rate of protein degradation and binding affinity of the TF. We see from this figure that strong binding produces enhanced asymmetry, but the degradation rate displays an interesting intermediate maximum in asymmetry â€“ degradation that is too fast, or too slow will not show asymmetry, but a maximum asymmetry is expected for TF lifetimes between 10 and 100 min. Crucially, this maximum coincides with typical doubling time of E. coli (which sets the TF half-life [Marr, 1991; Neidhardt and Curtiss, 1996]) and thus regulatory asymmetry in this motif is most relevant in common physiological conditions.

The non-monotonic behavior of asymmetry with degradation rate of TF can be explained by the TF-promoter occupancy (alternatively, residence time) of the TF and the target gene. Analytically, the asymmetry is given by the difference of occupancy of state 2 and state 3 (Appendix 9 Equation A9-7: CME for minimal model). For slow degradation, the number of TFs in a cell is high, favoring the transition to state 4 very quickly, thereby reducing the residence times of both state 2 and 3. On the other extreme, when degradation is fast, the TF number is too low for the cell to be in the state 2 or 3; the cell spends most of the time in state 1. In both the cases, the difference of residence times between state 2 and state 3 is low and hence the asymmetry is small. In the intermediate regime of degradation, the number of TFs is optimum to maximize the difference between residence times in state 2 and 3, which leads to maximum asymmetry.

To experimentally test the theory predictions for the role of TF degradation in setting regulatory asymmetry, we introduced several ssrA degradation tags to the LacI in our experiments (McGinness et al., 2006). The data, shown in Figure 4F includes degradation by a ‘weak’ or ‘slow’ tag (DAS with a rate of 0.00063 per minute per enzyme [McGinness et al., 2007], blue points), a slightly faster tag (DAS + 4 with a rate of 0.0011 per minute per enzyme [McGinness et al., 2007], green points) and a very fast tag (LAA tag with a rate of 0.21 per minute per enzyme [McGinness et al., 2007], red points) . In addition, the data without a tag is shown as yellow points. Here, we see that the slowest tag (blue points) introduces strong asymmetry. However, for the next fastest tag (green points) we see a significant decrease in asymmetry and the level of regulatory asymmetry is similar to what is seen in the absence of tags (yellow points). Finally, the fastest tag (red points) shows no asymmetry at all. It is worth pointing out that the qualitative order of degradation rates in these experiments can be inferred from how far the data ‘reaches’, faster degradation will lead to higher overall fold-changes for a given competition level. Importantly, controlling the protein degradation rate through this synthetic tool agrees with our model predictions, although the actual in vivo protein degradation rates are difficult to estimate from tag sequence alone, the asymmetry follows the expected trends based on the known (and observed) effectiveness of each tag (see schematic inset Figure 4F).

In the absence of targeted degradation, the degradation rate of most protein in E. coli, is naturally set by the growth rate. According to the model predictions in Figure 4E, the asymmetry should be highest for fast growing cells (roughly 20 min division rate for our growth conditions which is well below the degradation rate for peak asymmetry ∼10 min, Figure 4F) and decrease (or vanish) for very slow growing cells. To test this, we take the system with O1 regulatory binding sites on both the target and the TF promoter (yellow data in Figure 3D grown in M9 + glucose, 55 min doubling time) and grow in a range of doubling times between 22 min (rich defined media) up to 215 min (M9 + acetate) (see Appendix 2—figure 1A). Importantly, when we change the growth rate, other rates such as the transcription and translation rates will also be impacted (Bremer and Dennis, 2008; Klumpp et al., 2009), while these parameters will change the quantitative values of the asymmetry curve, the qualitative ordering and features of the asymmetry are not expected to be impacted (see Appendix 11—figure 1C). The data for these growth conditions is shown in Figure 5A. As predicted, faster growing cells show more regulatory asymmetry and slower growing cells show little-to-no regulatory asymmetry. We also test the role of growth rate in asymmetric regulation when O2 (a lower affinity site) and Oid (a higher affinity site) are used as the regulatory-binding sites instead of O1. This data is shown in Figure 5B (O2) and 5C (Oid). As discussed above, we could not find a suitable mutant for O2 and Oid that both relieved regulation from LacI and completely restored the expression of target gene (see Appendix 4: Constitutive values for autoregulatory gene.). This means we cannot explicitly measure the 1–1 correlation between the two axes in our data when using O2 or Oid for the TF gene. To this end, we find this correspondence by fitting the glucose data to our simulation of the same system and use that value to normalize all other growth rates for that operator. Despite this complication, it is clear that O2 regulation is symmetric at all studied growth rates while Oid regulation is asymmetric for all growth rates with faster growth rates appearing more asymmetric.

![Figure 5.](https://cdn.elifesciences.org/articles/56517/elife-56517-fig5-v2.jpg)

**Figure 5.:** Measurement of asymmetry in different media as a function of TF binding energy: O1 (A), O2 (B), Oid (C). The division time (τ) is varied between 22 min up to 215 min. (A) For O1, the asymmetry decreases with slower division rates and agrees well with the simulation predictions. (B) For the weak O2 site, no asymmetry is seen at any growth rate. (C) For the strongest site, Oid asymmetry is present at every growth rate although the magnitude of asymmetry still orders roughly by growth rate. Different symbols represent independent biological replicates and simulation data are shown as solid curves. (D) Histograms of single-cell asymmetry in expression of the TF and target gene regulated by O1 binding site in these four growth rates. Solid lines represent the interpolated distributions for better visualization of the histograms. Panels from top to bottom represent increasing the level of competition for the TF.

Importantly, the regulatory asymmetry is not due to a small population of outliers, bimodality or any other ‘rare’ phenotype. In Figure 5D, we show a histogram of single cell asymmetry values (defined as asymmetry = $FC_{Target}-FC_{TF})$ for each condition. As can be seen, expression in each media condition are roughly symmetric for most cells at the lowest competition levels (top panel). However, as competition levels are increased, the fast-growing conditions shift to higher asymmetry levels; strikingly at the highest growth rate almost every single cell is expressing target at a higher level than TF (bottom panel).

## Discussion

The single-input module (SIM) is a prevalent regulation strategy in both bacteria (Ma et al., 2004; Shen-Orr et al., 2002) and higher organisms (Lee et al., 2002; Segal et al., 2003; Yu et al., 2003). While the role of TF autoregulation (positive and negative) has been extensively studied (Acar et al., 2008; Assaf et al., 2011; Becskei and Serrano, 2000; Ochab-Marcinek et al., 2017; Rodrigo et al., 2016; Rosenfeld et al., 2002; Savageau, 1975; Semsey et al., 2009), the focus here is on the combined influence of an autoregulated TF and its target genes and how the shared need for that TF influences the quantitative features of its regulatory behaviors. We find that there is a fundamental asymmetry in gene regulation that can occur in the SIM regulatory motif. This asymmetry is not related to distinctions in the biological processes or an unexpected difference in our in vivo experiment, but rather an inherent asymmetry originating from the way the motif itself is wired. Although two identical promoters are in the same cell with the same average protein concentrations, they experience distinct regulatory environments. This is particularly relevant for the SIM motif because the primary function of the motif, organizing and coordinating gene expression patterns, operates on the premise of differential affinities amongst target genes; here we have shown that the TF gene has an inherent ‘affinity advantage’ due to being exposed to systematically higher TF concentrations than its target genes. This implies that the TF gene will respond 'earlier' than expected based on the raw affinity of its binding site and may necessitate weaker sites on autoregulating TF genes in order to achieve similar timing in expression compared to its targets. This may also shed light on the discrepancies in Arg pathway timing between different experiments which have used plasmid reporters (essentially changing network size) or different physiological growth conditions; the asymmetry is critically sensitive to both of these features. Although, here we are using E. coli as a model organism where it is easy to build and manipulate these regulatory motifs, we expect this phenomenon to apply broadly to other regulatory systems.

Regulatory asymmetry is intrinsic to the negative SIM motif even in the absence of decoys, but it can be greatly exacerbated by competing TF-binding sites. Due to the promiscuous nature of TF binding, this highlights the importance of considering not just the ‘closed’ system of a TF and a given target but also the impact of other binding sites (or inactivating interactions) for the TF in predicting regulation as well as the regulatory motif at play in the system. In our system, the magnitude of the asymmetry is enough to compensate for swapping the wild-type proximal O1 LacI binding site on the target gene with the ‘ideal’ operator Oid.

The cause of this asymmetry is a systematic difference in the TF concentration when the TF gene is active compared to when the target gene is active. As such, asymmetry is magnified by anything that enhances this concentration difference. Here, we have identified TF-binding affinity and TF degradation rate (controlled both directly and through modulating growth rate) as primary drivers of asymmetry in this motif. Although the relationship between growth rate and expression levels is well established (Bremer and Dennis, 2008; Klumpp and Hwa, 2008; Klumpp et al., 2009; Scott et al., 2010; Volkmer and Heinemann, 2011), effects such as this add a layer of complexity to this relationship.

In studies of quantitative gene regulation, the typical goal is to predict the output of a gene based on the regulatory composition of that gene's promoter and the number and identity of regulatory proteins. This work clearly presents a challenge for the drive to ‘read’ and predict regulation levels from the promoter DNA alone, in this case the regulatory motif is responsible for altering the observed regulation and must be considered as well. It has previously been demonstrated that features of a transcript can impact its regulation by effects such as targeted degradation, stabilization or posttranslational modification and regulation (Schikora-Tamarit et al., 2018), it is important to point out that regulatory asymmetry in this motif is a distinct phenomenon that does not operate through an enzymatic processes but rather is a fundamental feature of the network.

Finally, here we demonstrate regulatory asymmetry using a specific (but common) regulatory motif. The more general problem of quantifying the role of asymmetry in other network motifs may be an important step in expanding the predictive power of models based on single genes. The broader point that specific genes can be exposed to systematically different levels of regulatory TFs even in the absence of specific cellular mechanisms such as cytoplasmic compartmentalization, protein localization or DNA accessibility is likely more generally relevant. Understanding and quantifying these mechanisms can be an important piece towards improving our ability to predict and design gene regulatory circuits.

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
      <td>Gene (E. coli)</td>
      <td>ybcN&lt;&gt;25XX+11-lacI-mcherry</td>
      <td>GeneBank</td>
      <td>MT726947</td>
      <td>TF gene; XX can be O1, O2 or Oid operator</td>
    </tr>
    <tr>
      <td>Gene(E. coli)</td>
      <td>galK&lt;&gt;3*5XX+11-yfp</td>
      <td>GeneBank</td>
      <td>MT726948</td>
      <td>Target gene; XX can be O1,O2 or Oid operator</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>E. coli MG1655</td>
      <td>Lab stock</td>
      <td>CGSC#6300</td>
      <td>Wild type</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>HG105</td>
      <td>Garcia and Phillips, 2011</td>
      <td></td>
      <td>E. coli MG1655 with lac operon deleted</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>HG105 Δ⁢s⁢s⁢p⁢B</td>
      <td>This study</td>
      <td></td>
      <td>E. coli HG105 with s⁢s⁢p⁢B gene deleted</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>M9 minimal media</td>
      <td>BDDiagnostics</td>
      <td>DF0485-17</td>
      <td>Commercial media</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Rich defined media</td>
      <td>Teknova</td>
      <td>#M2105</td>
      <td>Commercial media</td>
    </tr>
    <tr>
      <td>Software,algorithm</td>
      <td>Matlab code</td>
      <td>Schnitzcells Rosenfeld et al., 2005</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>C code for simulations</td>
      <td>GitHub link This study</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Bacterial strains

All strains used in this study are constructed from the parent strain E. coli HG105 which is MG1655 with the lac operon deleted (MG1655 $Δ⁢l⁢a⁢c⁢I⁢Z⁢Y⁢A$). Auto-regulated TF (lacI-mCherry) is expressed from the ybcN locus and the TF-repressed target (yfp) is expressed from the galK locus with identical promoter sequence for both the TF and the target. Decoys are introduced on the pZE plasmid. In order to tune the degradation rate of the TF, three different ssrA tags were added to the C-terminus of the LacI-mCherry fusion protein. The tags used in this study are wild-type LAA tag (AANDENYALAA), DAS tag (AANDENYADAS) and DAS + 4 tag (AANDENYSENYADAS) (McGinness et al., 2006). For protein degradation tag experiments with LacI-mCherry fusion protein, HG105 with ΔsspB knockout is used as a parent strain to substantially moderate the protein degradation rate. It is also noteworthy that deletion of sspB gene did not affect the growth rate in any of the strains tested. Primers used in this study are listed in Table 1.

**Table 1.**
 Primers used in this study are listed below.Primers for the chromosomal integration of TF and the target are the same as described in Brewster et al., 2014. Primers to mutate the binding sites from O1 to Oid, O2 or NoO1V1 is listed below with the binding sites in blue. Primers to introduce the degradation tags to LacI mCherry fusion protein is listed below with tag sequence in red.


<table>
  <thead>
    <tr>
      <th colspan="2">Mutagenesis primer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Oid⁢_⁢mutagenesis⁢_⁢FP</td>
      <td>CCGGCTCGTATAATGTGTGGAATTGTGAGCGCTCACAATTGAATTCATTAAAGAG</td>
    </tr>
    <tr>
      <td>Oid⁢_⁢mutagenesis⁢_⁢RP</td>
      <td>CTCTTTAATGAATTCAATTGTGAGCGCTCACAATTCCACACATTATACGAGCCGG</td>
    </tr>
    <tr>
      <td>O2⁢_⁢mutagenesis⁢_⁢FP</td>
      <td>GTGAGCGAGTAACAACCGAATTCATTAAAGAGGAGAAAGGTAC</td>
    </tr>
    <tr>
      <td>O2⁢_⁢mutagenesis⁢_⁢RP</td>
      <td>TTGTTACTCGCTCACATTTCCACACATTATACGAGCC</td>
    </tr>
    <tr>
      <td>NoO1V1⁢_⁢mutagenesis⁢_⁢FP</td>
      <td>GATTGTTAGCGGAGAAGAATTGAATTCATTAAAGAGGAGAAAGGTACC</td>
    </tr>
    <tr>
      <td>NoO1V1⁢_⁢mutagenesis⁢_⁢RP</td>
      <td>AATTCTTCTCCGCTAACAATCCCACACATTATACGAGCCGGAAG</td>
    </tr>
    <tr>
      <td colspan="2">Primers to introduce tags</td>
    </tr>
    <tr>
      <td>ssrA⁢_⁢WT⁢_⁢FP</td>
      <td>GCAGCAAACGACGAAAACTACGCTTTAGCAGCTTAAGCTTAATTAGCTGAGTCTAGAGGC</td>
    </tr>
    <tr>
      <td>ssrA⁢_⁢WT⁢_⁢RP</td>
      <td>AGCTGCTAAAGCGTAGTTTTCGTCGTTTGCTGCTTTGTACAGCTCATCCATGC</td>
    </tr>
    <tr>
      <td>DAS⁢_⁢FP</td>
      <td>CAGCAAACGACGAAAACTACGCTGATGCATCTTAAGCTTAATTAGCTGAGTCTAGAGGC</td>
    </tr>
    <tr>
      <td>DAS⁢_⁢RP</td>
      <td>AGATGCATCAGCGTAGTTTTCGTCGTTTGCTGCTTTGTACAGCTCATCCATGCAGCTCATCCATGC</td>
    </tr>
    <tr>
      <td>DASplus4⁢_⁢FP</td>
      <td>GCAGCAAACGACGAAAACTACTCTGAAAATTATGCTGATGCATCTTAAGCTTAATTAGCTGAGTCTAGAGGC</td>
    </tr>
    <tr>
      <td>DASplus4⁢_⁢RP</td>
      <td>AGATGCATCAGCATAATTTTCAGAGTAGTTTTCGTCGTTTGCTGCTTTGTACAGCTCATCCATGC</td>
    </tr>
    <tr>
      <td colspan="2">qPCR primers</td>
    </tr>
    <tr>
      <td>qPCR⁢_⁢FP</td>
      <td>GCATTTATCAGGGTTATTGTCTCAT</td>
    </tr>
    <tr>
      <td>qPCR⁢_⁢RP</td>
      <td>GGGAAATGTGCGCGGAAC</td>
    </tr>
  </tbody>
</table>

### Microscopy

Bacterial cultures are grown overnight in 1 mL of LB in a 37°C incubator shaking at 250 rpm. Unless otherwise stated cultures grown overnight are diluted 2.5 × 103 fold to an initial OD of 0.002 into 1 mL of fresh M9 minimal media supplemented with 0.5% of one of the three different carbon sources (Glucose, Glycerol or Acetate) or in Rich Defined Media (RDM, Teknova #M2105), allowed to grow at 37°C until they reach an OD600 of 0.2 to 0.4 (0.1 for acetate) and harvested for microscopy. Cells are diluted 1:3 in 1X PBS (in order to obtain isolated cells in microscope images) and 1L is spotted on a 2% low melting agarose pad (Invitrogen #16520050) made with 1X PBS. Cells grown in RDM are cross-linked with paraformaldehyde before imaging to prevent shrinkage and osmotic shock to the cells. An automated fluorescent microscope (Nikon TI-E) with a heating chamber set at 37°C is used to record multiple fields per sample (between 8 and 12 unique fields of view) resulting in roughly 500 to 1000 individual cells per sample.

### qPCR measurements for average plasmid copy number

We performed qPCR measurements in order to quantify the average copy number of the pZE plasmid. Cells are grown as described for microscopic analysis and diluted 1:200 in Qiagen P1 lysis buffer and allowed to sit on ice. Meanwhile, cells are plated at 10–5 dilutions on fresh LB plates in order to determine the colony-forming units per mL (CFU/mL). 25 L of the lysate is diluted with 25 L of 1X PBS and allowed to sit for 5 min. The cells are then diluted 1:100 into 1X cut smart buffer from NEB. 20L of the mixture is incubated with 0.5 L of HindIII restriction enzyme for 30 min at 37°C followed by heat inactivation at 80°C for 20 min. The mixture is further diluted 1:10 and 4.2 L is used as a template in a 20 L qPCR reaction mixture. The pZE-1XOid plasmid is purified using the Qiagen Plasmid Medi Prep kit and quantified using the Qubit dsDNA assay kit. A standard curve is then prepared by diluting pZE-1XOid plasmid from 108 copies down to 10 copies. The average copy number of the decoy plasmid per cell is computed by comparing the cT of the sample to the standard curve and dividing by the number of cells in the sample.

### Simulation methodology

To model the experiments and study the effect of decoy sites on the expression of a target gene regulated by a negatively autoregulated TF gene, we develop a simple model of the experimental system. In our model, the auto-regulatory gene produces a protein (X) which forms a TF dimer (R). We explicitly modeled TF as a dimer to incorporate the fact that LacI acts as a dimer in our experimental system (the LacI-mCherry construct lacks the tetramerization domain [Kipper et al., 2018]). Dimerization and de-dimerization steps occur at the rate $k_{p}$ and $k_{m}$, respectively. The TF binds to its own promoter ($P_{TF}$), to the promoter of the target gene ($P_{target}$), and to the decoy sites (N) with a constant rate $k_{on}$ per free TF per unit time. The off rate of the bound TF ($k_{off}$, the unbinding rate) depends on the sequence identity and can be different for different promoters. A bound TF unbinds from the promoters of the TF and target, and from the decoy sites at a rate $k_{off,TF}$, $k_{off,target}$, and $k_{off,decoy}$ per unit time, respectively. A TF-free promoter produces an mRNA at the rate β which is then translated into a protein at a rate α. The mRNA and the proteins are degraded at the rate $\gamma_{m}$ and γ, respectively. We assume that all proteins (free protein, TF bound to promoter and TF bound to decoy sites) degrades with the same rate. Typically, the proteins in E. coli are very stable with protein half-life greater than the cell cycle and the dominant contribution to degradation comes from the dilution due to cell division. The degradation rate is thus given by $\gamma=l⁢n⁢(2)/\tau_{1}+l⁢n⁢(2)/\tau_{2}$, where $\tau_{1}$ and $\tau_{2}$ are protein half-life and cell division time, respectively. The set of reactions describing the model above are listed in Appendix 6—figure 2A.

We implement the simulations for stochastic reaction systems using Gillespie's algorithm (Gillespie, 1977) in C programming. Each simulation is run for sufficiently long time (∼106 s) to reach a steady state. Typically, for the rates used in this paper the steady state is achieved in 105 s or less (see Appendix 6—figure 1 for a sample time trace). Data for steady state distributions (TF and target protein) are then recorded by sampling over time with a time interval ($T_{S}$) long enough for the slowest reaction to occur 20 times on average ($T_{S}$ = 20 over rate for slowest reaction). Mean protein numbers in steady state for fold-change are calculated using at least 105 data points for each single run.

### Kinetic parameter estimation

To compare the results from experiments with our simulations, we are required to find values for the kinetic on and off rate of LacI for different operator sites (Oid, O1 and O2), the transcription and translation rates, mRNA degradation rate, and the growth rates in different media. We directly measure growth rate for different media in our experiment (see Appendix 2). The on and off rates are related to the binding energy ($Δ⁢ϵ$) through,

$$
\frac{k_{on}}{k_{off}+\gamma}=\frac{e⁢x⁢p⁢(-Δ⁢ϵ)}{N_{ns}},
$$

where $N_{ns} ∼5\times10^{6}$ bps is the number of non-specific binding sites in the genome (which we take as the total number of bases) (Phillips et al., 2013), $k_{on}$ is the binding rate per free TF per unit time, $k_{off}$ is the unbinding rate per unit time and γ is the decay rate of the TF. Experimental measurements of $Δ⁢ϵ$ have been reported in many repeated experiments (Brewster et al., 2014; Garcia and Phillips, 2011; Razo-Mejia et al., 2018) and thus we constrain our choice of $k_{on}$ and $k_{off}$ such that we obtain affinities consistent with these measurements. Taking one data set (O1 regulated TF and O1 regulated target grown in glucose), we use maximum likelihood analysis to obtain the rates by varying $k_{on}$ in a range 0.0015–0.003 $s^{-1}$ (which sets the corresponding value of $k_{off}$ to give $Δ⁢ϵ_{O1}=15.3⁢k_{B}⁢T$) (Elf et al., 2007; Bremer and Dennis, 2008), $\gamma_{m}^{-1}$ in a range of 30–90 s (Yu et al., 2006; Bremer and Dennis, 2008), β in a range of 0.1–0.3 $s^{-1}$ (Kennell and Riezman, 1977), and choosing α (Cai et al., 2006) such that the constitutive number for the TF protein is in the range of 1000–2600; this parameter largely sets the ‘range’ of our fold-change vs fold-change curves and this range of α reproduces the experimental range we see in those curves for this data set.

We then use this same on rate to derive the relevant off rates for O2 and Oid using their binding energies ($Δ⁢ϵ_{O2}=13.9⁢k_{B}⁢T$, $Δ⁢ϵ_{Oid}=16.3⁢k_{B}⁢T$ ) and Equation 1. Interestingly, the binding affinity we measure for Oid is 0.7 $k_{B}⁢T$ weaker than has been previously reported but is consistent with measurements of Oid binding affinity in our lab. Using this method, we find the $k_{on}$ to be 0.0015 per TF per second, which yields $k_{off}$ to be, O1 = 0.0015 $s^{-1}$, O2 = 0.0167 $s^{-1}$ and Oid = 0.0004 $s^{-1}$, consistent with previous findings (Elf et al., 2007; Hammar et al., 2014; Jones et al., 2014; Razo-Mejia et al., 2018). All other rates are listed in Table 2. Importantly, this process is not meant to precisely determine the exact quantitative parameters of LacI binding, and it is not a formal fit, but rather an estimate that provides us with realistic prediction of regulation from our simulations using molecular parameters that are consistent with available direct kinetic measurements (Chen et al., 2015; Elf et al., 2007; Sanchez et al., 2011; Yu et al., 2006).

**Table 2.**
 Kinetic rates used in the simulations.


<table>
  <thead>
    <tr>
      <th>Rates</th>
      <th>Symbols</th>
      <th>Value</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Growth rate</td>
      <td>ln2/γ</td>
      <td>25 min (RDM)</td>
      <td>Measured experimentally</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>55 min (Glucose)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>125 min (Glycerol)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>225 min (Acetate)</td>
      <td></td>
    </tr>
    <tr>
      <td>Binding of TF</td>
      <td>kon</td>
      <td>0.0015 TF-1⁢s-1</td>
      <td>Obtained from fit</td>
    </tr>
    <tr>
      <td>Unbinding of TF</td>
      <td>koff</td>
      <td>0.00042 s-1 (Oid)</td>
      <td>Equation 1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.00149 s-1 (O1)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.0167 s-1 (O2)</td>
      <td></td>
    </tr>
    <tr>
      <td>mRNA degradation</td>
      <td>γm</td>
      <td>0.033 s-1</td>
      <td>Obtained from fit</td>
    </tr>
    <tr>
      <td>mRNA production</td>
      <td>β</td>
      <td>0.1 s-1</td>
      <td>Obtained from fit</td>
    </tr>
    <tr>
      <td>Translation rate</td>
      <td>α</td>
      <td>0.03–0.2 s-1</td>
      <td>Obtained from fit</td>
    </tr>
    <tr>
      <td>Dimerization</td>
      <td>kp</td>
      <td>1.38⁢s-1</td>
      <td>Stamatakis and Zygourakis, 2011</td>
    </tr>
    <tr>
      <td>Monomerization</td>
      <td>km</td>
      <td>0.000002⁢s-1</td>
      <td>Stamatakis and Zygourakis, 2011</td>
    </tr>
  </tbody>
</table>

### Data analysis

Data analysis is performed using a modified version of the Matlab code Schnitzcells (Rosenfeld et al., 2005). We use this code to segment the phase images of each sample to identify single cells. Mean pixel intensities of YFP and mCherry signals are extracted from the segmented phase mask for each individual cell using regionprops, an inbuilt function in matlab. The background fluorescence is calculated by averaging the mean intensity of the inverse phase mask upon eroding the regions around the segmented cell masks. The background fluorescence value of a particular frame was subtracted from the mean pixel intensity of cells in the same frame (see Appendix 1). Finally, the autofluorescence value were calculated using the same procedure for cells that do not express either YFP or mCherry and the average autofluorescence value of these cells is subtracted from each measured YFP or mCherry value. Resulting mean pixel intensity of mCherry signal was corrected for the crosstalk from YFP signal. Crosstalk between different channels can be measured by determining the difference between the autofluorescence of a strain without a given fluorophore in the presence of the other fluorophore (highly expressed). We find that under our microscope 0.25% ($\gamma_{cross}=0.0025$) of YFP signals can be seen in the mCherry channel whereas mCherry channel has no crosstalk in the YFP channel. Hence, we correct for this crosstalk by subtracting the mean pixel intensity of YFP signal times the $\gamma_{cross}$ from the mean pixel intensity of mCherry signal. The per-pixel fluorescence values of mCherry and YFP of each cell is then multiplied by the area of the cell to account for the total fluorescence. Fold-change in expression of the mCherry and YFP is calculated by dividing the corresponding values of the constitutive strains (discussed in Appendix 4). At least 500 individual cells were analyzed per sample and binned according to the mCherry values. Any bin with less than 50 data points is excluded. Unless otherwise stated, each data point represents the bootstrapped mean of all data points in a given bin and the error bar represents the standard deviation of the bootstrapped mean.

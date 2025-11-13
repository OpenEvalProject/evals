# Non-equilibrium strategies enabling ligand specificity by signaling receptors

## Authors

- Andrew Goetz<sup>1</sup> †
- Jeremy Barrios<sup>2</sup>
- Ralitsa Radostinova Madsen<sup>3</sup> ([ORCID: 0000-0001-8844-5167](https://orcid.org/0000-0001-8844-5167))
- Purushottam D Dixit<sup>1</sup> ([ORCID: 0000-0003-3282-0866](https://orcid.org/0000-0003-3282-0866)) †

### Affiliations

1. Department of Biomedical Engineering, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
2. Department of Physics, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
3. MRC Protein Phosphorylation and Ubiquitylation Unit, University of Dundee Dundee United Kingdom ([ROR:01zg1tt02](https://ror.org/01zg1tt02))
4. Systems Biology Institute, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))

† Corresponding author

## Abstract

Signaling receptors often encounter multiple ligands and have been shown to respond selectively to generate appropriate, context-specific outcomes. At thermal equilibrium, ligand specificity is limited by the relative affinities of ligands for their receptors. Here, we present a non-equilibrium model in which receptors overcome thermodynamic constraints to preferentially signal from specific ligands while suppressing others. In our model, multi-site phosphorylation and active receptor degradation act in concert to regulate ligand specificity, with receptor degradation, a common motif in eukaryotes, providing a previously under-appreciated layer of control. Here, ligand-bound receptors undergo sequential phosphorylation, with progression restarted by ligand unbinding or receptor turnover. High-affinity complexes are kinetically sorted toward degradation-prone states, while low-affinity complexes are sorted toward inactivated states, both limiting signaling. As a result, network activity is maximized for ligands with intermediate affinities. This mechanism explains paradoxical experimental observations in receptor tyrosine kinase signaling, including non-monotonic dependence of signaling output on ligand affinity and kinase activity. Given the ubiquity of multi-site phosphorylation and ligand-induced degradation across signaling receptors, we propose that kinetic sorting may be a general non-equilibrium ligand-discrimination strategy used by multiple signaling receptors.

## Introduction

Signaling receptors routinely encounter a wide variety of extracellular ligands and decode their identity with remarkable precision to generate context-specific responses. This selective processing of environmental cues is essential for regulating diverse biological processes, including development, immune surveillance, and tissue homeostasis (Cantley et al., 2014). Failures in ligand discrimination underlie many diseases, including diabetes and cancer (Madsen et al., 2025; Madsen and Vanhaesebroeck, 2020).

A key determinant of ligand specificity in biochemical networks is the thermodynamic stability of molecular complexes, such as ligand–receptor or substrate–enzyme pairs. At thermal equilibrium, the abundance of complexes is determined by their equilibrium binding constants. This imposes a fundamental limit on specificity: high-affinity ligands are inevitably favored over lower-affinity competitors, with complex abundances scaling in proportion to their association constants.

Notably, many biochemical networks display paradoxical behaviors that cannot be explained by equilibrium affinity alone (Clark et al., 1999; Coombs et al., 2002; Freed et al., 2017; Madsen et al., 2025; Myers et al., 2023). For example, signaling receptors such as receptor tyrosine kinases (RTKs) and T cell receptors can produce stronger signaling outputs (phosphorylation levels) in response to intermediate-affinity ligands compared to low- and high-affinity ligands (Coombs et al., 2002; Lever et al., 2014; Freed et al., 2017; Madsen et al., 2025; Myers et al., 2023). Additionally, RTKs also exhibit a non-monotonic dependence between receptor activity and kinase activity (Kiyatkin et al., 2020; Kleiman et al., 2011). These observations raise a fundamental question: how do signaling receptors overcome thermodynamic constraints to achieve robust, ligand-specific responses?

A classic scheme to bypass limitations imposed by equilibrium thermodynamics is kinetic proofreading (KPR), a mechanism first proposed by Hopfield, 1974 and Ninio, 1975. KPR enhances specificity of high-affinity ligands by introducing energy-consuming, irreversible steps, such as phosphorylation/dephosphorylation cycles, that amplify differences between competing ligands. KPR has been invoked in diverse systems, including DNA replication (Hopfield, 1980), mRNA surveillance (Hilleren and Parker, 1999), protein folding (Gulukota and Wolynes, 1994), and immune receptor signaling (McKeithan, 1995; Huang et al., 2019; Lever et al., 2014). Notably, while most KPR models prefer ligands with the highest affinity, it is also known that embedding KPR schemes in larger biochemical networks may allow non-monotonic dependence between ligand affinity and network activity (Lever et al., 2014; Murugan et al., 2014). However, as we will show below, these models do not capture the non-monotonic dependence between network output and kinase activity.

In this work, we present a novel non-equilibrium mechanism to achieve ligand specificity at the receptor level that relies on biologically ubiquitous signaling motifs: sequential multi-site phosphorylation and active receptor degradation. These two motifs are found in many major receptor systems, including RTKs (Furdui et al., 2006; Sorkin and Goh, 2009), G protein-coupled receptors (GPCRs) (Koenig and Edwardson, 1997; Tobin, 2008), T cell receptors (McKeithan, 1995; Charpentier and King, 2021), and interleukin receptors (Kollewe et al., 2004; Cendrowski et al., 2016). Notably, the combined role of these motifs in conferring networks with ligand and kinase specificity has not been explored.

In our model, high-affinity ligand–receptor complexes are sorted toward degradation-prone states, while low-affinity complexes repeatedly dissociate the ligand, resulting in maximal signaling output only from intermediate-affinity ligands. Notably, this ligand specificity can be tuned by varying easily controllable cellular parameters, for example, enzyme abundances. This non-equilibrium kinetic sorting mechanism explains the paradoxical non-monotonic dependence of signaling activity on ligand affinity and phosphorylation rate observed in RTKs. More broadly, given the ubiquity of the signaling motifs involved, we propose that kinetic sorting provides a general strategy for achieving ligand discrimination that is likely to be broadly used across diverse signaling networks.

## Results

### Classic KPR favors high-affinity ligands

KPR is the standard model for non-equilibrium ligand discrimination. To set the stage, we first revisited the classic KPR model originally proposed by McKeithan to explain how T cell receptors avoid activation downstream of weak ligands (McKeithan, 1995; Figure 1a; see ‘Materials and methods’ for equations).

![Figure 1.](https://cdn.elifesciences.org/articles/107524/elife-107524-fig1-v1.jpg)

**Figure 1.:** Chemical species and rate constants are shown in the figure. R denotes ligand-free receptors, B denotes ligand-bound inactive receptors, and $P_{n},n\in[1,N]$ are phosphorylated receptors. The ultimate phosphorylated species PN (marked red) is assumed to be signaling competent. (a) shows the traditional model first proposed by McKeithan, 1995. (b, c) show the sustained signaling model and the limited signaling model (Lever et al., 2014) which introduce additional receptor states, $P_{N}^{0}$ and I respectively, directly following receptor activation.

In this model, ligand-bound receptors undergo a series of phosphorylation steps, with the final state PN representing the active, signaling-competent form. Importantly, ligand unbinding at any phosphorylation stage returns the receptor to the unbound state R. We parameterized the model using dimensionless quantities: the ligand dissociation rate $𝛿=𝑘_{𝑑}𝜏$, phosphorylation rate $𝜔=𝑘_{𝑝}𝜏$, and ligand concentration $u=L/K_{D}$, where $K_{D}=k_{d}/k_{on}$. Assuming saturating ligand ($𝑢→∞$), the steady-state abundance of the active state is

$$
P_{N}=\frac{\omega^{N}}{(\omega+\delta)^{N}}.
$$

As expected, increasing the phosphorylation cascade length N amplifies the preference for low-dissociation (high-affinity) ligands (Figure 2a), reflecting the classical KPR outcome.

![Figure 2.](https://cdn.elifesciences.org/articles/107524/elife-107524-fig2-v1.jpg)

**Figure 2.:** (a) Activity $P_{N}$ plotted as a function of non-dimensional ligand dissociation rate $𝛿$ for the traditional KPR scheme (Figure 1a). (b) Activity $P_{N}$ plotted as a function of non-dimensional ligand dissociation rate $𝛿$ for the limited signaling model (Figure 1b). (c) The dependence of the activity on the dimensionless phosphorylation rate ω for the limited signaling model. All figures plotted for a sequence of N = 1, 5, and 10 phosphorylation sites.

### Modified KPR schemes do not explain paradoxical RTK behavior

Before introducing our model, we briefly review two previously proposed extensions of receptor-level KPR that exhibit non-monotonic ligand discrimination: the sustained signaling model and the limited signaling model (Lever et al., 2014; Figure 1b and c). Both models introduce an additional state to Mckeithan’s KPR scheme. The sustained signaling model adds an active but ligand-free state $P_{N}^{0}$, while the limited signaling model introduces an inactivated state $𝐼$ downstream of $P_{N}$.

While both models show non-monotonic dependence of signaling activity on ligand affinity (Lever et al., 2014), only the limited signaling model retains this non-monotonic dependence at saturating ligand concentrations (Lever et al., 2014; Figure 2b), consistent with some paradoxical features observed in RTKs (Freed et al., 2017; Madsen et al., 2025; Myers et al., 2023). However, the limited signaling model fails to reproduce a second key observation in RTKs: receptor activity in this model increases monotonically with kinase activity, whereas RTK experiments show that partial kinase inhibition can paradoxically increase receptor activity (Kiyatkin et al., 2020; Kleiman et al., 2011; Figure 2c). Thus, these models are insufficient to explain RTK signaling dynamics.

Notably, these models neglect a key feature of many receptor signaling pathways: preferential degradation of activated receptors (Sorkin and Goh, 2009; Koenig and Edwardson, 1997; Charpentier and King, 2021; Cendrowski et al., 2016). Below, we incorporate preferential degradation in our model to investigate how it governs receptor activity.

### A kinetic sorting model integrates active receptor degradation

We build a model to study the effect of two widespread signaling motifs: sequential multi-site phosphorylation and ligand-induced receptor degradation (Figure 3) on ligand discrimination. In our model, receptors are delivered to the surface at a constant rate, internalized at a basal rate $𝑘_{𝑖𝑛𝑡}$, and degraded more rapidly when highly phosphorylated ($k_{int}^{∗}>k_{int}$). Ligand-bound receptors undergo irreversible phosphorylation and dephosphorylation through distinct irreversible mechanisms. We note that both kinase and phosphatase are irreversible reactions carried out by separate enzymes. While their effect on the coarse-grained model of the receptor may appear reversible, it is important to note that receptor phosphorylation via ATP hydrolysis and removal of the phosphate group from the receptor corresponds to a futile cycle that does not recharge the ADP molecule to an ATP molecule. In addition to the previously defined dimensionless parameters, we define the dimensionless active receptor degradation rate, $\beta=k_{int}^{∗}/k_{int}$, and the relative rate of dephosphorylation, $ρ=k_{dp}/k_{p}$. A key feature of our model is that all phosphorylated species are signaling competent. Indeed, in many signaling pathways all phosphorylation sites on the receptor Schulze et al., 2005; Tobin, 2008; Kollewe et al., 2004; Lemmon and Schlessinger, 2010; Latorraca et al., 2020 have downstream effects. Therefore, we define the net activity $𝐴_{𝑛}$ of phosphorylation site $𝑛$ as all receptor states where the site $𝑛$ is phosphorylated: $A_{n}=\summ\geqnP_{m}$.

![Figure 3.](https://cdn.elifesciences.org/articles/107524/elife-107524-fig3-v1.jpg)

**Figure 3.:** Chemical species and rate constants are shown in the figure. $𝑅$ denotes ligand-free receptors, $𝐵$ denotes ligand-bound inactive receptors, and $P_{n},n\in[1,N]$ are phosphorylated receptors. $𝜙$ represents an implicit source and sink, corresponding to receptor delivery and internalization, respectively. It does not denote a physical chemical species.

#### Parameter ranges

To ensure that the phenomena captured by our model are relevant to real signaling networks, we selected ranges for the dimensionless parameters based on direct experimental measurements and model fits. Importantly, many of these kinetic processes have comparable rates across diverse receptor systems (Koenig and Edwardson, 1997; Subtil et al., 1994; Liu et al., 2000). Specifically, basal receptor internalization occurs at rates of $k_{int}≈10^{−4}$–$10^{−3},s^{−1}$ (Wiley, 2003), while active receptor internalization is typically faster, at $k_{int}^{∗}≈10^{−3}$–$10^{−2},s^{−1}$ (Wiley, 2003; Lyashenko et al., 2020). Ligand dissociation rates typically fall in the range $k_{d}≈10^{−2}$–$10^{−1},s^{−1}$ (Chen et al., 2009; Lyashenko et al., 2020), and receptor phosphorylation ($k_{p}$) and dephosphorylation ($k_{dp}$) occur at $∼10^{−1}$–$10^{0},s^{−1}$ (Kleiman et al., 2011; Chen et al., 2009; Lyashenko et al., 2020). For EGFR, equilibrium dissociation constants range from $∼0.1,nM$ for the high-affinity ligand Betacellulin to $∼25,nM$ for the low-affinity ligand AREG (Hu et al., 2022; Macdonald-Obermann and Pike, 2014). Based on these values, we set the following ranges for dimensionless parameters: $\beta=k_{int}^{∗}/k_{int}\in[1,100]$, $ρ=k_{dp}/k_{p}\in[0.01,100]$, $\omega=k_{dp}/k_{int}\in[1,1000]$, and $\delta=k_{d}/k_{int}\in[1,1000]$. Finally, the number of phosphorylation sites with known functional roles typically ranges from 5 to 25 (Schulze et al., 2005). These broad ranges comfortably encompass experimentally measured estimates. Unless otherwise specified, our default parameter values are $\delta=20$, $\omega=200$, $ρ=0.01$, $\beta=50$, and $N=10$.

Before examining how phosphorylation levels depend on model parameters, we illustrate the mechanism of kinetic sorting of receptor states, which tunes ligand specificity beyond pure thermodynamic preference, using a simple example. To that end, we consider a signaling network with $N=5$ phosphorylation sites interacting with three ligands of distinct affinities—high, medium, and low. We assume the dissociation rates for these ligands are $\delta_{H}=20$, $\delta_{M}=200$, and $\delta_{L}=1000$, respectively. In order to compare our model with the aforementioned paradoxical experimental observations which have been performed at saturating ligand concentration, we take the limit $u→∞$.

Figure 4 shows that low-affinity ligands ($\delta_{L}=1000$) predominantly sort receptors toward the inactive state $𝐵$ and early phosphorylation states $P_{n},n∼1$ as frequent ligand unbinding prevents progression to later phosphorylation states. This behavior resembles the traditional KPR mechanism described by McKeithan, 1995. In contrast, receptors bound to high-affinity ligands are sorted toward later phosphorylation states, which mark them for enhanced degradation. Here, similar to traditional KPR, the fraction of receptors reaching the final phosphorylation state is highest for high-affinity ligands. Yet, the overall receptor pool is reduced due to ligand-induced degradation, lowering net phosphorylation activity. Strikingly, receptors bound to intermediate-affinity ligands ($\delta_{M}=200$) are sorted toward intermediate phosphorylation states, resulting in maximal phosphorylation output. Below, we show how kinetic parameters govern the ability of the network to overcome thermodynamic preference and acquire ligand specificity.

![Figure 4.](https://cdn.elifesciences.org/articles/107524/elife-107524-fig4-v1.jpg)

**Figure 4.:** Abundances of network species $𝐵$ (ligand bound inactive receptor) and $P_{n},n\in[1,5]$ for a signaling receptor with $N=5$ phosphorylation sites. Abundances are shown for ligands of three different affinities. The inset shows the activity of the first phosphorylation site $𝐴_{1}$. Species abundances below $10^{−3}$ are not shown.

#### Early phosphorylation sites show ligand specificity

Figure 5a illustrates how total phosphorylation activity at each site, $A_{n},n\in[1,N]$ varies with ligand dissociation rate $𝛿$. We note that the activity of the $𝑛^{𝑡ℎ}$ site is given by the total concentration of all species that have the $𝑛^{𝑡ℎ}$ site phosphorylated; $A_{n}=\sumi=nNP_{n}$. We find that early phosphorylation sites ($n∼1$) exhibit maximal activity at intermediate values of $𝛿$ while both high- and low-affinity ligands suppress net receptor phosphorylation. Our model predicts that this ligand specificity diminishes for later sites, where outputs increasingly resemble traditional KPR, which favors high-affinity ligands.

![Figure 5.](https://cdn.elifesciences.org/articles/107524/elife-107524-fig5-v1.jpg)

**Figure 5.:** (a) The activity $A_{n}$ of the $𝑛^{𝑡ℎ}$ phosphorylation site as a function of dimensionless dissociation rate $𝛿$. The activity is normalized to the maximum activity. The maximum $𝐴_{𝑛}$ as a function of $𝑛$ is shown in the inset. (b) Activity of the first phosphorylation site $A_{1}$ plotted as a function of the dissociation rate $\delta$ for different values of the phosphorylation rate $\omega$. (c, d) Activity of the first phosphorylation site $A_{1}$ plotted as a function of phosphorylation rate $𝜔$ (dephosphorylation rate $ρ$ in panel d) for different values of the dissociation rate $𝛿$.

To examine how model parameters shape ligand specificity, we focused on the activity at the first phosphorylation site, $𝐴_{1}$, which exhibits the strongest discriminatory behavior (Figure 5a). As shown in Figure 5b, achieving ligand specificity at high dissociation rates $𝛿$ requires sufficiently high phosphorylation rates $𝜔$. Notably, our model captures a puzzling observation from EGFR signaling: the high-affinity ligand EGF produces lower/comparable steady-state phosphorylation compared to lower-affinity ligands such as Epigen and Epiregulin (Freed et al., 2017; Myers et al., 2023; Madsen et al., 2025). Experimental estimates place the basal EGFR internalization rate at $k_{int}≈1.3\times10^{−3},s^{−1}$ (Chen et al., 2009), the EGF dissociation rate at $k_{d}≈3\times10^{−2},s^{−1}$ (Chen et al., 2009), and the phosphorylation rate at $k_{p}≈10^{−1}−10^{0},s^{−1}$, yielding $\delta_{EGF}≈10−20$ and $\omega_{EGFR}≈100−1000$. Low-affinity ligands such as Epigen (EPGN) and Epiregulin (EREG) have equilibrium dissociation constants about 10-fold higher than EGF (Hu et al., 2022), corresponding to $\delta_{EPGN}≈\delta_{EREG}≈100−200$. The effective degradation rate of fully activated receptors is estimated to be 10–50 times higher than that of inactive receptors (Lyashenko et al., 2020), implying $\beta=50$. Under these conditions, our model predicts a switch in phosphorylation levels: as $𝛿$ increases from $\delta_{EGF}$ to $\delta_{EPGN}$, receptor phosphorylation increases—reversing the expectation based purely on thermodynamic affinity. This effect arises because EGF-bound receptors are efficiently sorted toward degradation-prone states compared to those bound to lower-affinity ligands.

Our model also explains another paradox in EGFR signaling. Experimental studies have shown that EGF-stimulated receptors exhibit higher steady-state phosphorylation when kinase activity is partially inhibited (Kiyatkin et al., 2020; Kleiman et al., 2011). As shown in Figure 5c, at low $𝛿$ values (e.g., $𝛿=16$), decreasing the phosphorylation rate $𝜔$ from levels typical of EGFR ($\omega_{EGFR}≈100−1000$) paradoxically increases overall receptor phosphorylation. A similar effect is observed when receptor dephosphorylation is enhanced (Figure 5d). Importantly, our model makes a testable prediction: the reversal of thermodynamic preference observed between EGF and EPGN/EREG will disappear when kinase activity is mildly suppressed (see, e.g., the curves for $\omega=256$ and $\omega=16$ over $\delta\in[10,100]$), such as by treatment with low doses of the kinase inhibitor gefitinib (Herbst et al., 2004). This non-monotonic trend may help prevent cells with abnormally high kinase activity from becoming constitutively active, thereby preserving their sensitivity to extracellular cues.

#### Multi-site phosphorylation and ligand-induced degradation are both essential for ligand specificity

To assess the importance of sequential multi-site phosphorylation on ligand specificity, we analyzed $𝐴_{1}^{𝑁}$, the phosphorylation of the first site for signaling networks with $𝑁$ phosphorylation sites. Figure 6a shows that multi-site phosphorylation is essential to endow signaling networks with ligand specificity and ligand-induced receptor degradation alone is not sufficient. This is because the non-monotonic preference for intermediate affinity ligands arises only when the receptors can be sorted among multiple phosphorylation sites: earlier ones for low-affinity ligands and later ones for high-affinity ligands.

![Figure 6.](https://cdn.elifesciences.org/articles/107524/elife-107524-fig6-v1.jpg)

**Figure 6.:** (a) Activity of the first phosphorylation site, $𝐴_{1}$, as a function of the dissociation rate $𝛿$ for signaling networks with different number of phosphorylation sites. (b) The optimal dissociation rate $𝛿_{𝑜𝑝𝑡}$ that leads to maximum phosphorylation activity as a function of dimensionless degradation rate $𝛽$ for different values of $𝜔$. $𝛿_{𝑜𝑝𝑡}$ is shown only if $\delta_{opt}\in[1,1000]$. (c) The relative activity of a ligand with dissociation rate that differs by $k_{B}T$ compared to $𝛿_{𝑜𝑝𝑡}$ plotted as a function of $𝛽$ for different values of $𝜔$ (see inset). Of the two ligands that differ in stability by $k_{B}T$, the ligand exhibiting maximum activity is considered.

To assess how receptor degradation shapes ligand specificity for a multi-site phosphorylation network, we examined how altering receptor turnover influences model behavior. As shown in Figure 6b, the optimal dissociation rate $\delta_{opt}$, which maximizes receptor phosphorylation levels, increases with ligand-induced degradation rate $𝛽$. Crucially, this optimal $\delta_{opt}$ emerges only when receptor degradation is strong ($\beta≫1$). These predictions can be tested by blocking receptor degradation, for example, via mutation of ubiquitination sites (Gerritsen et al., 2023).

To quantify ligand specificity, we computed receptor phosphorylation in response to ligands differing by at least one $k_{B}T$ in binding free energy from the optimal ligand. Figure 6c shows that as $𝛽$ increases, phosphorylation downstream of suboptimal ligands (red line in inset) declines relative to the optimal ligand. This enhanced specificity is further amplified by increasing kinase activity $𝜔$.

These results show that both multi-site phosphorylation and ligand-induced degradation are key features controlling ligand specificity in our kinetic sorting mechanism.

## Discussion

Cells face the formidable task of decoding multiple chemically distinct extracellular signals to generate appropriate, context-specific responses. This challenge is especially acute for cell surface receptors like RTKs, GPCRs, and interleukin receptors, which bind multiple cognate ligands and yet elicit distinct downstream outcomes. While equilibrium affinity provides a baseline expectation for ligand specificity, it cannot fully explain the rich and often counterintuitive behaviors observed in many signaling systems.

Here, we show that a non-equilibrium mechanism of kinetic sorting which operates through multi-site phosphorylation and active receptor degradation can explain how signaling networks achieve ligand specificity beyond equilibrium limits. In kinetic sorting, high-affinity ligand–receptor complexes are sorted toward degradation-prone states, low-affinity complexes are sorted toward inactivated states, and intermediate-affinity ligands strike the optimal balance between progression and degradation to maximize signaling. This framework explains paradoxical features observed in RTK systems, including the non-monotonic dependence of phosphorylation on ligand affinity and kinase activity. Importantly, our model predicts that early phosphorylation sites show the strongest ligand discrimination, consistent with recent experimental observations. It also makes the testable prediction that impairing receptor degradation should reduce specificity by eliminating the kinetic sorting effect. Given the ubiquity of the essential motifs of our mechanism, that is, multi-site phosphorylation and receptor degradation, we believe that kinetic sorting may be a common mechanism to modulate ligand specificity at the receptor level, potentially in addition to other mechanisms that endow signaling networks with ligand specificity, both at the receptor level (Lever et al., 2014) as well as in downstream signaling pathways (Singh and Nemenman, 2017).

In contrast to what has been shown previously for KPR models (Coombs et al., 2002; Lever et al., 2014), the kinetic sorting model also captures the non-monotonic relationship between signaling output and kinase/phosphatase activity observed in RTK systems such as EGFR (Kleiman et al., 2011; Kiyatkin et al., 2020). In these systems, partial inhibition of kinase activity paradoxically increases steady-state receptor phosphorylation, a behavior not accounted for by equilibrium models (see ‘Materials and methods’) or by prior non-equilibrium schemes such as the limited signaling model (Lever et al., 2014). This type of protective filtering can ensure that downstream signaling remains contingent on extracellular cues and is not constitutively active, thereby preventing persistent, cue-independent activation. Such regulation could help maintain control in pathways such as those governing growth, where deregulated activity can have severe consequences. The potential benefit of this regulatory pattern suggests it could be advantageous in other signaling contexts. Consistent with this idea, non-monotonic regulation by kinase or phosphatase activity is found in other systems through distinct mechanisms (e.g., the non-monotonic effects of the phosphatase CD45 in T-cell receptor signaling, Courtney et al., 2019). This indicates that selective filtering based on enzymatic activity is a strategy employed in diverse biological settings. While direct evidence for the kinetic sorting mechanism remains limited to RTKs, similar filtering behavior emerges in theoretical analyses of phosphorylation–dephosphorylation cycles in more general settings (Martins and Swain, 2013), suggesting it may represent a broader principle of enzymatic signaling networks.

Our findings complement prior studies on mechanisms of ligand specificity that operate at thermal equilibrium, such as those described in the Bone Morphogenetic Protein (BMP) pathway (Antebi et al., 2017; Su et al., 2022; Parres-Gold et al., 2025). BMP signaling relies on promiscuous ligand–receptor interactions, with specificity emerging from differences in receptor abundance, binding affinity, and complex activity. In contrast, our work shows that non-equilibrium mechanisms—such as phosphorylation cycles and ligand-induced receptor degradation—can achieve ligand discrimination even for a single receptor type. Given that ligand–receptor promiscuity, multi-site phosphorylation, and receptor turnover are common features across signaling systems (e.g., in the EGFR/ErbB family; Linggi and Carpenter, 2006), it is likely that biological networks integrate both equilibrium and non-equilibrium strategies to achieve robust and tunable ligand specificity.

In recent years, there has been growing interest in engineering synthetic physical and chemical circuits capable of carrying out complex computational tasks, including input discrimination, classification, prediction, and the generation of multiple stable cell states (Shakiba et al., 2021; Ma et al., 2022; Benzinger et al., 2022; Zhu et al., 2022; Floyd et al., 2024; Parres-Gold et al., 2025; Aoki et al., 2019). Some of these synthetic strategies rely on equilibrium thermodynamics (Parres-Gold et al., 2025), while others exploit non-equilibrium steady states (Floyd et al., 2024). We propose that non-equilibrium kinetic sorting, which harnesses receptor synthesis and degradation, could provide synthetic biologists with a powerful framework for achieving precise control over molecular abundances and dynamic system behavior.

Finally, we address a major concern in non-equilibrium signaling circuits: the energetic cost of operation. Previous theoretical work has shown that free energy dissipation places fundamental constraints on the performance of signaling networks (Bryant and Machta, 2023; Govern and ten Wolde, 2014; Lan et al., 2012; Mehta and Schwab, 2012; Qian and Reluga, 2005; Cao et al., 2015; Azeloglu and Iyengar, 2015; Floyd et al., 2024; Mahdavi et al., 2024). These studies typically focus on futile cycles of reversible modifications such as phosphorylation or methylation. In contrast, ligand-induced receptor degradation—a central feature of many signaling networks—is a far more energy-intensive process. For example, MCF10A cells maintain approximately 105 EGFR molecules on the surface (each 1,210 amino acids in length) (Shi et al., 2016), with a synthesis rate of about 15 receptors per second (Lyashenko et al., 2020), corresponding to an energetic cost of roughly ~8 × 104 ATP/s (assuming 4.5 ATP per peptide bond; Milo et al., 2010). By comparison, EGFR dephosphorylation occurs over ~15 s (Kleiman et al., 2011), and only 5–10% of receptors are phosphorylated at steady state (Shi et al., 2016; Feng et al., 2023), resulting in a much lower energetic cost of ~6 × 102ATP/s for dephosphorylation. Thus, the energetic burden of receptor turnover can exceed that of reversible modification cycles by up to two orders of magnitude. These estimates suggest that, at least in eukaryotic cells where signaling proteins may turnover multiple times within cellular lifetime (Milo et al., 2010), non-equilibrium modification cycles are unlikely to pose a fundamental energetic limitation on the functionality of signaling networks. Here, the energetic demands of signaling networks must account for protein turnover in addition to non-equilibrium modification cycles.

## Materials and methods

### Equations for proofreading models

The equations describing species abundances in the traditional KPR model similar to that of McKeithan, 1995 are as follows:

$$
\frac{dR}{dt}=−k_{on}LR+k_{d}B+k_{d}\sumi=1NP_{i}
$$



$$
\frac{dB}{dt}=+k_{on}LR−k_{d}B−k_{p}B
$$



$$
\frac{dP_{1}}{dt}=k_{p}B−k_{p}P_{1}−k_{d}P_{1}
$$



$$
\frac{dP_{i}}{dt}=k_{p}P_{i−1}−k_{p}P_{i}−k_{d}P_{i}∀ i\in[2,N−1]
$$



$$
\frac{dP_{N}}{dt}=k_{p}P_{N−1}−k_{d}P_{N}
$$

For the limited signaling model, the dynamics of $𝐵$, and $𝑃_{𝑖},𝑖∈[1,𝑁−1]$ are identical to the traditional KPR model. The dynamics of $𝑅$ and $𝑃_{𝑁}$ are modified as follows:

$$
\frac{dR}{dt}=−k_{on}LR+k_{d}B+k_{d}\sumi=1NP_{i}+k_{d}I
$$



$$
\frac{dP_{N}}{dt}=k_{p}P_{N−1}−k_{d}P_{N}−k_{in}P_{N}
$$



$$
\frac{dI}{dt}=k_{in}P_{N}−k_{d}P_{I}
$$

### Equations for the model with receptor degradation

Signaling receptors participate in a variety of complex regulatory processes, including non-linear ligand binding dynamics (Limbird et al., 1975; Macdonald and Pike, 2008), receptor oligomerization (Mudumbi et al., 2024; Huang et al., 2016), context-specific interactions with adapter proteins (Madsen and Vanhaesebroeck, 2020; Feng et al., 2023), and trafficking between cellular compartments leading to degradation (Sorkin and Goh, 2009; Wiley, 2003; Irannejad and von Zastrow, 2014).

While computational models that incorporate these mechanistic details are powerful tools for hypothesis generation (Chen et al., 2010; Qiao et al., 2025), they often require large-scale datasets for accurate parameterization (Feng et al., 2023). As an alternative, simplified models that intentionally omit certain mechanistic details can still yield deep qualitative insights, even if they cannot quantitatively reproduce experimental data.

In this study, we present such a simplified model aimed at explaining two paradoxical features of RTK signaling: (1) the non-monotonic relationship between ligand-receptor affinity and steady-state receptor phosphorylation (Freed et al., 2017; Madsen et al., 2025; Myers et al., 2023), and (2) the counterintuitive increase in receptor phosphorylation following mild kinase inhibition (Kleiman et al., 2011; Kiyatkin et al., 2020).

To keep the model simple and tractable, we neglect receptor recycling and oligomerization. Previously, we showed that the combined effects of endocytosis, recycling, and degradation can be captured by a single effective dimensionless parameter, $𝛽$ in this study, which reflects the degradation bias of fully phosphorylated receptors compared to partially phosphorylated receptors (Lyashenko et al., 2020). Similarly, receptor dimerization and negative cooperativity can be abstracted into a Hill coefficient $𝜂<1$ (Lyashenko et al., 2020). For the phenomena explored here, including oligomerization would modify the shape of the response curves but not their qualitative behavior.

Under these assumptions, the governing equations for the model are given by

$$
\frac{dR}{dt}=k_{delivery}−k_{on}LR+k_{d}B+k_{d}\sumi=1NP_{i}−k_{int}R
$$



$$
\frac{dB}{dt}=k_{on}LR−k_{d}B−k_{p}B−k_{int}B
$$



$$
\frac{dP_{1}}{dt}=k_{p}B−k_{p}P_{1}−k_{d}P_{1}−k_{int}P_{1}
$$



$$
\frac{dP_{i}}{dt}=k_{p}P_{i−1}−k_{p}P_{i}−k_{d}P_{i}−k_{int}P_{i},∀ i\in[2,N−1]
$$



$$
\frac{dP_{N}}{dt}=k_{p}P_{N−1}−k_{d}P_{N}−k_{int}^{∗}P_{N}
$$

All equations are solved at steady state and in the limit $𝑢→∞$. All codes required to generate the figures in the manuscript can be found at https://github.com/BarriosJer0/KineticSorting (copy archived at Barrios, 2025).

### Equations for a model at thermal equilibrium

To confirm the role of non-equilibrium thermodynamics on ligand specificity, we consider the closest equivalent equilibrium model. The strongest requirement of an equilibrium model is that all reactions must be bidirectional. Another requirement is that microscopic reversibility or detailed balance. Specifically, ratios of rate constants around loops must equal to unity for all loops. The first requirement implies that unidirectional reactions: synthesis and degradation of receptors and the irreversible loss of activity due to ligand dissociation cannot exist in a reaction network that operates at equilibrium. The simplest equilibrium model closest to the kinetic sorting scheme is governed by the following equations:

$$
\frac{dR}{dt}=−k_{on}LR+k_{d}B
$$



$$
\frac{dB}{dt}=k_{on}LR−k_{d}B−k_{p}B+k_{dp}P_{1}
$$



$$
\frac{dP_{i}}{dt}=k_{p}P_{i−1}−k_{dp}P_{i}−k_{p}P_{i}+k_{dp}P_{i+1}∀ i\in[1,N−1]
$$



$$
\frac{dP_{N}}{dt}=k_{p}P_{N−1}−k_{dp}P_{N}
$$

In the above equations, we use the notation $P_{0}≡B$.

We note that phosphorylation/dephosphorylation reactions are unidirectional non-equilibrium reactions carried out by different enzymes: phosphorylation hydrolyzes ATP to ADP and attaches a phosphate group to the receptor. In contrast, while dephosphorylation removes a phosphate group from the receptor, it does not recharge an ADP molecule back to ATP. Notably, however, this non-equilibrium nature of the phosphorylation/dephosphorylation cycle is not apparent in our coarse-grained kinetic scheme where ATP and ADP are not explicitly considered. We retain this part of the non-equilibrium model since a corresponding equilibrium model can be imagined where different sites on the receptor change conformation between an inactive and an active state and that these changes occur in a sequential manner.

Solving these equations at steady state and taking the limit $u=Lk_{on}/k_{d}→∞$, we have

$$
p_{i}=\frac{P_{i}}{R_{T}}=\frac{ρ^{N−i}}{\sumi=0Nρ^{i}}
$$

where $𝑅_{𝑇}$ is the total number of receptors and $ρ=k_{dp}/k_{p}$. Note that as expected, this equilibrium model has no dependence on ligand dissociation rate $k_{d}$ at saturation, further confirming that non-equilibrium reactions are needed to endow cells with ligand specificity.

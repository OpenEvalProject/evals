# Proofreading through spatial gradients

## Authors

- Vahe Galstyan<sup>1</sup> ([ORCID: 0000-0001-7073-9175](https://orcid.org/0000-0001-7073-9175))
- Kabir Husain<sup>2</sup>
- Fangzhou Xiao<sup>3</sup>
- Arvind Murugan<sup>2</sup> ([ORCID: 0000-0001-5464-917X](https://orcid.org/0000-0001-5464-917X)) †
- Rob Phillips<sup>3</sup> ([ORCID: 0000-0003-3082-2809](https://orcid.org/0000-0003-3082-2809)) †

### Affiliations

1. Biochemistry and Molecular Biophysics Option, California Institute of Technology Pasadena United States
2. Department of Physics and the James Franck Institute, University of Chicago Chicago United States
3. Division of Biology and Biological Engineering, California Institute of Technology Pasadena United States
4. Department of Physics, California Institute of Technology Pasadena United States

† Corresponding author

## Abstract

Key enzymatic processes use the nonequilibrium error correction mechanism called kinetic proofreading to enhance their specificity. The applicability of traditional proofreading schemes, however, is limited because they typically require dedicated structural features in the enzyme, such as a nucleotide hydrolysis site or multiple intermediate conformations. Here, we explore an alternative conceptual mechanism that achieves error correction by having substrate binding and subsequent product formation occur at distinct physical locations. The time taken by the enzyme–substrate complex to diffuse from one location to another is leveraged to discard wrong substrates. This mechanism does not have the typical structural requirements, making it easier to overlook in experiments. We discuss how the length scales of molecular gradients dictate proofreading performance, and quantify the limitations imposed by realistic diffusion and reaction rates. Our work broadens the applicability of kinetic proofreading and sets the stage for studying spatial gradients as a possible route to specificity.

## Introduction

The nonequilibrium mechanism called kinetic proofreading (Hopfield, 1974; Ninio, 1975) is used for reducing the error rates of many biochemical processes important for cell function (e.g. DNA replication [Kunkel, 2004], transcription [Sydow and Cramer, 2009], translation [Rodnina and Wintermeyer, 2001; Ieong et al., 2016], signal transduction [Swain and Siggia, 2002], or pathogen recognition [McKeithan, 1995; Goldstein et al., 2004; Cui and Mehta, 2018]). Proofreading mechanisms operate by inducing a delay between substrate binding and product formation via intermediate states for the enzyme–substrate complex. Such a delay gives the enzyme multiple chances to release the wrong substrate after initial binding, allowing far lower error rates than what one would expect solely from the binding energy difference between right and wrong substrates.

Traditional proofreading schemes require dedicated molecular features such as an exonuclease pocket in DNA polymerases (Kunkel, 2004) or multiple phosphorylation sites on T-cell receptors (McKeithan, 1995; Goldstein et al., 2004); such features create intermediate states that delay product formation (Figure 1a) and thus allow proofreading. Additionally, since proofreading is an active nonequilibrium process often involving near–irreversible reactions, the enzyme typically needs to have an ATP or GTP hydrolysis site to enable the use of energy supplies of the cell (Yamane and Hopfield, 1977; Rodnina and Wintermeyer, 2001). Due to such stringent structural requirements, the number of confirmed proofreading enzymes is relatively small. Furthermore, generic enzymes without such dedicated features are assumed to not have active error correction available to them.

![Figure 1.](https://cdn.elifesciences.org/articles/60415/elife-60415-fig1-v2.jpg)

**Figure 1.:** (a) The traditional proofreading scheme with multiple biochemically distinct intermediates, transitions between which are typically accompanied by energy–consuming reactions. The T-cell activation mechanism with successive phosphorylation events is used for demonstration (McKeithan, 1995; Cui and Mehta, 2018). (b) The spatial proofreading scheme where the delay between binding and catalysis is created by constraining these events to distinct physical locations. The wavy arrows stand for the diffusive motion of the complex. Binding events primarily take place on the length scale $\lambda_{_{S}}$ of substrate localization.

In this work, we propose an alternative scheme where the delay between initial substrate binding and product formation steps is achieved by separating these events in space. If substrates are spatially localized and product formation is favorable only in a region of low substrate concentration where an activating effector is present then the time taken by the enzyme–substrate complex to travel from one location to the other can be used to discard the wrong substrates, which are assumed to unbind from the enzyme more readily than the right substrates (Figure 1b). When this delay is longer than substrate unbinding time scales, very low error rates of product formation can be achieved, allowing this spatial proofreading scheme to outperform biochemical mechanisms with a finite number of proofreading steps.

In contrast to traditional proofreading, the nonequilibrium mechanism here does not require any direct energy consumption by the enzyme or substrate itself (e.g. through ATP hydrolysis). This liberates the enzyme from any proofreading-specific molecular features; indeed, any ‘equilibrium’ enzyme with a localized effector can proofread using our scheme if appropriate concentration gradients of the substrates or enzymes are set up. In this way, the energetic and structural requirements of proofreading can be outsourced from the enzyme and substrate to the gradient maintaining mechanism. It also means that spatial proofreading is easy to overlook in experiments, and that the fidelity of reconstituted reactions in vitro could be lower than the fidelity in vivo.

The lack of reliance on structure makes spatial proofreading more adaptable. We study how tuning the length scale of concentration gradients can trade off error rate against speed and energy consumption on the fly. In contrast, traditional proofreading schemes rely on nucleotide chemical potentials, for example, the out of equilibrium [ATP]/[ADP] ratio in the cell, and cannot modulate their operation without broader physiological disruptions.

Our proposed scheme can be leveraged for specificity if appropriate concentration gradients are set. Such gradients arise in multiple cellular contexts (e.g. near the nucleus, the plasma membrane, the Golgi apparatus, the endoplasmic reticulum [ER], kinetochores, microtubules [Bivona et al., 2003; Caudron et al., 2005; Kholodenko, 2006]) and several gradient-forming mechanisms have been discussed in the literature (Wu et al., 2018; Kholodenko, 2006; Kholodenko, 2003). We conclude our analysis of spatial proofreading by quantifying its limitations as set by realistic reaction rates and gradient formation mechanisms, and discuss examples from the literature, including the localization of mRNAs in polarised cells, and the non-vesicular transport of lipids in eukaryotic cells, in which this mechanism might be in play. Our work motivates a detailed investigation of spatial structures and compartmentalization in living cells as possible delay mechanisms for proofreading enzymatic reactions.

## Results

### Slow transport of enzymatic complex enables proofreading

Our proposed scheme is based on spatially separating substrate binding and product formation events for the enzyme (Figure 1b). Such a setting arises naturally if substrates are spatially localized by having concentration gradients in a cellular compartment. Similarly, an effector needed for product formation (e.g. through allosteric activation) may have a spatial concentration gradient localized elsewhere in that compartment. To keep our model simple, we assume that the right (R) and wrong (W) substrates have identical concentration gradients of length scale $\lambda_{_{S}}$ but that the effector is entirely localized to one end of the compartment, for example via membrane tethering. In Appendix 4, we extend our study of model performance to the scenario where the two substrates have different localization length scales.

We model our system using coupled reaction–diffusion equations for the substrate-bound (‘ES’ with $S=R,W$) and free (‘E’) enzyme densities, namely,

$$
\frac{∂ρ_{_{ER}}}{∂t}=D\frac{∂^{2}ρ_{_{ER}}}{∂x^{2}}−k_{off}^{R}ρ_{_{ER}}+k_{on}ρ_{_{R}}ρ_{_{E}},
$$



$$
\frac{∂ρ_{_{EW}}}{∂t}=D\frac{∂^{2}ρ_{_{EW}}}{∂x^{2}}−k_{off}^{W}ρ_{_{EW}}+k_{on}ρ_{_{W}}ρ_{_{E}},
$$



$$
\frac{∂ρ_{_{E}}}{∂t}=D\frac{∂^{2}ρ_{_{E}}}{∂x^{2}}+\sumS=R,Wk_{off}^{S}ρ_{_{ES}}−\sumS=R,Wk_{on}ρ_{_{S}}ρ_{_{E}}.
$$

Here, D is the enzyme diffusion constant, $k_{on}$ and $k_{off}^{S}$ (with $k_{off}^{W}>k_{off}^{R}$) are the substrate binding and unbinding rates, respectively, and $ρ_{_{S}}⁢(x)∼e^{-x/\lambda_{_{S}}}$ is the spatially localized substrate concentration profile which we take to be exponentially decaying, which is often the case for profiles created by cellular gradient formation mechanisms (Driever and Nüsslein-Volhard, 1988; Brown and Kholodenko, 1999). We limit our discussion to this one-dimensional setting of the system, though our treatment can be generalized to two and three dimensions in a straightforward way.

The above model does not explicitly account for several effects relevant to living cells, such as depletion of substrates or distinct diffusion rates for the free and substrate-bound enzymes. More importantly, it does not account for the mechanism of substrate gradient formation. We analyze a biochemically detailed model with this latter feature and experimentally constrained parameters later in the paper. Here, we proceed with the minimal model above for explanatory purposes. To identify the key determinants of the model’s performance, we assume throughout our analysis that the amount of substrates is sufficiently low that the enzymes are mostly free with a roughly uniform profile (i.e. $ρ_{_{E}}≈constant$). This assumption makes Equations (1-3) linear and allows us to solve them analytically at steady state. We demonstrate in Appendix 5 that proofreading is, in fact, most effective under this assumption and discuss the consequences of having high substrate amounts on the performance of the scheme.

In our simplified picture, enzyme activation and catalysis take place upon reaching the right boundary at a rate r that is identical for both substrates. Therefore, the density of substrate–bound enzymes at the right boundary can be taken as a proxy for the rate of product formation $v_{S}$, since 

$$
v_{S}=r⁢ρ_{_{ES}}⁢(L),
$$

where L is the size of the compartment. In order to keep the analytical results concise and intuitive, we perform our main analyses under the assumption that catalysis is slow, mirroring the study of traditional proofreading schemes (Hopfield, 1974). In Appendix 3, we derive the precise conditions under which this treatment is valid, and generalize our analysis to arbitrary catalysis rates.

To demonstrate the proofreading capacity of the model, we first analyze the limiting case where substrates are localized to the left end of the compartment ($\lambda_{_{S}}→0$). In this limit, the fidelity $η$, defined as the number of right products formed per single wrong product, becomes

$$
η=\frac{v_{R}}{v_{W}}=\sqrt{η_{eq}}⁢\frac{sinh⁡(\sqrt{\tau_{D}⁢k_{off}^{W}})}{sinh⁡(\sqrt{\tau_{D}⁢k_{off}^{R}})},
$$

where $η_{eq}=k_{off}^{W}/k_{off}^{R}$ is the equilibrium fidelity, and $\tau_{D}=L^{2}/D$ is the characteristic time scale of diffusion across the compartment (see Appendix 1 for the derivation).

Equation 5 is plotted in Figure 2 for a family of different parameter values. As can be seen, when diffusion is fast (small $\tau_{D}$), fidelity converges to its equilibrium value and proofreading is lost ($η≈\sqrt{η_{eq}}\times\sqrt{\tau_{D}k_{off}^{W}/\tau_{D}k_{off}^{R}}=η_{eq}$). Conversely, when diffusion is slow (large $\tau_{D}$), the enzyme undergoes multiple rounds of binding a substrate at the left end and unbinding midway until it manages to diffuse across the whole compartment as a complex and form a product. These rounds serve as ‘futile cycles’ that endow the system with proofreading. In this regime, fidelity scales as

$$
η∼e^{(\sqrt{k_{off}^{W}}-\sqrt{k_{off}^{R}})⁢\sqrt{\tau_{D}}}.
$$

![Figure 2.](https://cdn.elifesciences.org/articles/60415/elife-60415-fig2-v2.jpg)

**Figure 2.:** Individual curves were made for different choices of $k_{off}^{W}$ (varied in the $[10-100]⁢k_{off}^{R}$ range). $\tau_{off}^{R}=1/k_{off}^{R}$ is the unbinding time scale of right substrates, kept fixed in the study. Fidelity values corresponding to integer degrees of proofreading in a traditional sense ($η/η_{eq}=η_{eq}^{n}$, $n=1,2,3,…$) are marked as circles. Dominant processes in the two limiting regimes are highlighted in red in the schematics shown as insets.

To get further insights, we introduce an effective number of extra biochemical intermediates (n) that a traditional proofreading scheme would need to have in order to yield the same fidelity, that is $η/η_{eq}=η_{eq}^{n}$. We calculate this number as (see Appendix 1)

$$
n≈\frac{\sqrt{\tau_{D}⁢k_{off}^{W}}}{ln⁡η_{eq}}.
$$

Notably, since $\tau_{D}∼L^{2}$, the result above suggests a linear relationship between the effective number of proofreading realizations and the compartment size ($n∼L$). In addition, because the right-hand side of Equation 7 is an increasing function of $k_{off}^{W}$, the proofreading efficiency of the scheme rises with larger differences in substrate off-rates (Figure 2) – a feature that ‘hard–wired’ traditional proofreading schemes with a fixed number of proofreading steps lack.

### Navigating the speed–fidelity trade-off

As is inherent to all proofreading schemes, the fidelity enhancement described earlier comes at a cost of reduced product formation speed. This reduction, in our case, happens because of increased delays in diffusive transport. Here, we explore the resulting speed–fidelity trade-off and its different regimes by varying two of the model parameters: diffusion time scale $\tau_{D}$ and the substrate localization length scale $\lambda_{_{S}}$.

Speed and fidelity for different sampled values of $\tau_{D}$ and $\lambda_{_{S}}$ are depicted in Figure 3a. As can be seen, for a fixed $\tau_{D}$, the reduction of $\lambda_{_{S}}$ can trade off fidelity against speed. This trade-off is intuitive; with tighter substrate localization, the complexes are formed closer to the left boundary. Hence, a smaller fraction of complexes reach the activation region, reducing reaction speed. The Pareto-optimal front of the trade-off over the whole parameter space, shown as a red curve on the plot, is reached in the limit of ideal substrate localization ($\lambda_{_{S}}→0$). Varying the diffusion time scale allows one to navigate this optimal trade-off curve and access different performance regimes.

![Figure 3.](https://cdn.elifesciences.org/articles/60415/elife-60415-fig3-v2.jpg)

**Figure 3.:** (a) Speed and fidelity evaluated for sampled values of the diffusion time scale ($\tau_{D}$) and substrate localization length scale ($\lambda_{_{S}}$). Here, $v_{eq}∼1/k_{off}^{R}$ is the speed in the equilibrium limit of a uniform substrate profile ($\lambda_{_{S}}→∞$). The red line corresponds to the Pareto-optimal front and is reached in the high substrate localization limit. The example speed–fidelity trade-off illustrated through the black dotted curve is obtained for $\tau_{D}≈20⁢\tau_{off}^{R}$. (b) Density profiles of wrong (EW) and right (ER) complexes in three qualitatively different performance regimes. The normalization factor $ρ_{_{ES}}^{eq}$ corresponds to the equilibrium complex densities. (c) Fidelity as a function of diffusion time scale for different choices of $\lambda_{_{S}}$ (varied in the $[0.04,0.4]⁢L$ range). The dashed line corresponds to the ideal substrate localization limit ($\lambda_{_{S}}→0$). Inset: Fidelity as a function of $L/\lambda_{_{S}}$ for a fixed $\tau_{D}$. Shaded area indicates the range where the bulk of fidelity enhancement takes place. Equilibrium fidelity $η_{eq}=10$ was used in generating all the panels.

Specifically, if the diffusion time scale is fast compared with the time scales of substrate unbinding (i.e. $\tau_{D}≪1/k_{off}^{R},1/k_{off}^{W}$), then both right and wrong complexes that form near the left boundary arrive at the activation region with high probability, resulting in high speeds, although at the expense of error–prone product formation (Figure 3b, top). In the opposite limit of slow diffusion, both types of complexes have exponentially low densities at the activation region, but due to the difference in substrate off-rates, production is highly accurate (Figure 3b, bottom). There also exists an intermediate regime where a significant fraction of right complexes reach the activation region while the vast majority of wrong complexes do not (Figure 3b, middle). As a result, an advantageous trade-off is achieved where a moderate decrease in the production rate yields high fidelity enhancement – a feature that was also identified in multi-step traditional proofreading models (Murugan et al., 2012).

In Appendix 3, we also study this trade-off caused by varying the catalysis rate $r$. Briefly, we find that when all other parameters are fixed, increasing $r$ trades off fidelity against speed in a linear fashion, with the ratio of highest and lowest fidelity values falling in the $[\sqrt{η_{eq}},η_{eq}]$ range. The Pareto–optimal front of the trade-off, however, monotonically shifts toward the higher speed region, suggesting that faster catalysis is, in fact, more favorable if the diffusion time scale $\tau_{D}$ can be adjusted accordingly (see Appendix 3 for details).

We saw in Figure 3a that in the case of ideal substrate localization, the slowdown of diffusive transport necessarily reduced the production rate and increased the fidelity. The latter part of this statement, however, breaks down when substrate gradients are weak. Indeed, fidelity exhibits a non-monotonic response to tuning $\tau_{D}$ when the substrate gradient length scale $\lambda_{_{S}}$ is non-zero (Figure 3c). The reason for the eventual decay in fidelity is the fact that with slower diffusion (larger $\tau_{D}$), substrate binding and unbinding events take place more locally and therefore, the right and wrong complex profiles start to resemble the substrate profile itself, which does not discriminate between the two substrate kinds. We show in Appendix 1 that the optimal diffusion time scale can be roughly approximated as $\tau_{D}^{*}/\tau_{off}^{R}≈η_{eq}^{-1}⁢(L/\lambda_{_{S}})^{2}$, which increases monotonically with $L/\lambda_{_{S}}$, consistent with the shifting peaks in Figure 3c.

Not surprisingly, the error–correcting capacity of the scheme improves with better substrate localization (lower $\lambda_{_{S}}$). For a fixed $\tau_{D}$, the bulk of this improvement takes place when $L/\lambda_{_{S}}$ is tuned in a range set by the two key dimensionless numbers of the model, namely, $\sqrt{\tau_{D}⁢k_{off}^{R}}$ and $\sqrt{\tau_{D}⁢k_{off}^{W}}$ (Figure 3c, inset). In Appendix 1, we provide an analytical justification for this result. Taken together, these parametric studies uncover the operational principles of the spatial proofreading scheme and demonstrate how the speed–fidelity trade-off could be dynamically navigated as needed by tuning the key time and length scales of the model.

### Energy dissipation and limits of proofreading performance

A hallmark signature of proofreading is that it is a nonequilibrium mechanism with an associated free energy cost. In our scheme, the enzyme itself is not directly involved in any energy-consuming reactions, such as hydrolysis. Instead, the free energy cost comes from maintaining the spatial gradient of substrates, which the enzymatic reaction tends to homogenize by releasing bound substrates in regions of low substrate concentration. As the activating effectors are assumed to be tethered at $x=L$, they do not require dissipation to remain localized.

While mechanisms of substrate gradient maintenance may differ in their energetic efficiency, there exists a thermodynamically dictated minimum energy that any such mechanism must dissipate per unit time. We calculate this minimum power P as

$$
P=\sumS = {R,W}\int_{0}^{L}j_{_{S}}⁢(x)⁢\mu⁢(x)⁢dx.
$$

Here $j_{_{S}}⁢(x)=k_{on}⁢ρ_{_{S}}⁢(x)⁢ρ_{_{E}}-k_{off}^{S}⁢ρ_{_{ES}}⁢(x)$ is the net local binding flux of substrate ‘S’, and $\mu⁢(x)$ is the local chemical potential (see Appendix 2.1 for details). For substrates with an exponentially decaying profile considered here, the chemical potential is given by

$$
\mu⁢(x)=\mu⁢(0)+k_{B}⁢T⁢ln⁡\frac{ρ_{_{S}}⁢(x)}{ρ_{_{S}}⁢(0)}=\mu⁢(0)-k_{B}⁢T⁢\frac{x}{\lambda_{_{S}}},
$$

where $k_{B}⁢T$ is the thermal energy scale. Notably, the chemical potential difference across the compartment, which serves as an effective driving force for the scheme, is set by the inverse of the nondimensionalized substrate localization length scale, namely,

$$
\beta⁢Δ⁢\mu=\frac{L}{\lambda_{_{S}}},
$$

where $\beta^{-1}=k_{B}⁢T$. This driving force is zero for a uniform substrate profile ($\lambda_{_{S}}→∞$) and increases with tighter localization (lower $\lambda_{_{S}}$), as intuitively expected.

We used Equation 8 to study the relationship between dissipation and fidelity enhancement as we tuned $Δ⁢\mu$ for different choices of the diffusion time scale $\tau_{D}$. As can be seen in Figure 4, power rises with increasing fidelity, diverging when fidelity reaches its asymptotic maximum given by Equation 5 in the large $Δ⁢\mu$ limit. For the bulk of each curve, power scales as the logarithm of fidelity, suggesting that a linear increase in dissipation can yield an exponential reduction in error. Notably, such a scaling relationship has also been calculated in the context of E. coli chemoreceptor adaptation (Lan et al., 2012). In particular, it was shown that the adaptation error decreases exponentially with energy dissipated through multiple methylation–demethylation cycles which are used to stabilize the activity state of the receptor. Analogies in the cost-performance trade-off across these functionally distinct mechanisms contribute to the search for overarching thermodynamic themes underlying cellular information processing (Lan et al., 2012; Lan and Tu, 2013; Horowitz et al., 2017; Sartori and Pigolotti, 2015).

![Figure 4.](https://cdn.elifesciences.org/articles/60415/elife-60415-fig4-v2.jpg)

**Figure 4.:** Power–fidelity relationship when tuning the effective driving force $Δ⁢\mu$ for different choices of the diffusion time scale $\tau_{D}$.$J_{bind}=k_{on}ρ_{E}\intρ_{S}(x)dx$ is the integrated rate of substrate binding. The red line indicates the large dissipation limit of fidelity given by Equation 5. The circles indicate the $Δ⁢\mu$ range specified in Equation 11 for different $\tau_{D}$ choices. For sufficiently large $\tau_{D}$ values, the cost per binding event approaches $\beta⁢\sqrt{η_{eq}}$ at the end of this range (see Appendix 2.1 for details). In making this plot, $η_{eq}=10$ was used.

The logarithmic scaling is achieved in our model when the driving force is in a range where most of the fidelity enhancement takes place, namely,

$$
\beta⁢Δ⁢\mu\in[\sqrt{\tau_{D}⁢k_{off}^{R}},\sqrt{\tau_{D}⁢k_{off}^{W}}].
$$

At the end of this range, the cost per substrate binding event approaches $\sqrt{η_{eq}}$ in $k_{B}⁢T$ units (see Appendix 2.1 for details). And beyond the range, additional error correction is attained at an increasingly higher cost.

Note that the power computed here does not include the baseline cost of creating the substrate gradient, which, for instance, would depend on the substrate diffusion constant. We only account for the additional cost to be paid due to the operation of the proofreading scheme which works to homogenize this substrate gradient. The baseline cost in our case is analogous to the work that ATP synthase needs to perform to maintain a nonequilibrium [ATP]/[ADP] ratio in the cell, whereas our calculated power is analogous to the rate of ATP hydrolysis by a traditional proofreading enzyme. We discuss these two classes of dissipation in greater detail in Appendix 2.3.

Just as the cellular chemical potential of ATP or GTP imposes a thermodynamic upper bound on the fidelity enhancement by any proofreading mechanism (Qian, 2006), the effective driving force $Δ⁢\mu$ imposes a similar constraint for the spatial proofreading model. This thermodynamic limit depends only on the available chemical potential and is equal to $e^{\beta⁢Δ⁢\mu}$. This limit can be approached very closely by our model, which for $Δ⁢\mu≳1$ achieves the exponential enhancement with an additional linear prefactor, namely, $(η/η_{eq})^{max}≈e^{\beta⁢Δ⁢\mu}/\beta⁢Δ⁢\mu$ (see Appendix 2.2). Such scaling behavior was theoretically accessible only to infinite-state traditional proofreading schemes (Qian, 2006; Ehrenberg and Blomberg, 1980). This offers a view of spatial proofreading as a procession of the enzyme through an infinite series of spatial filters and suggests that, from the perspective of peak error reduction capacity, our model outperforms the finite-state schemes.

### Proofreading by biochemically plausible intracellular gradients

Our discussion of the minimal model thus far was not aimed at a particular biochemical system and thus did not involve the use of realistic reaction rates and diffusion constants typically seen in living cells. Furthermore, we did not account for the possibility of substrate diffusion, as well as for the homogenization of substrate concentration gradients due to enzymatic reactions, and have thereby abstracted away the gradient maintaining mechanism. The quantitative inspection of such mechanisms is important for understanding the constraints on spatial proofreading in realistic settings.

Here, we investigate proofreading based on a widely applicable mechanism for creating gradients by the spatial separation of two opposing enzymes (Stelling and Kholodenko, 2009; Bivona et al., 2003; Brown and Kholodenko, 1999). Consider a protein $S$ that in its free state is phosphorylated by a membrane-bound kinase and dephosphorylated by a delocalized cytoplasmic phosphatase, as shown in Figure 5a. This setup will naturally create a gradient of the active form of protein ($S^{*}$), with the gradient length scale controlled by the rate of phosphatase activity $k_{p}$ ($S^{*}→k_{p}S$). Such mechanisms are known to create gradients of the active forms of MEK and ERK (Kholodenko, 2006), of GTPases such as Ran (with GEF and GAP [Kalab et al., 2002] playing the role of kinase and phosphatase, respectively), of cAMP (Kholodenko, 2006) and of stathmin oncoprotein 18 (Op18) (Bastiaens et al., 2006; Niethammer et al., 2004) near the plasma membrane, the Golgi apparatus, the ER, kinetochores and other places.

![Figure 5.](https://cdn.elifesciences.org/articles/60415/elife-60415-fig5-v2.jpg)

**Figure 5.:** (a) The active form $S^{*}$ of many proteins exhibits gradients because kinases that phosphorylate $S$ are anchored to a membrane while phosphatases can diffuse in the cytoplasm (Kholodenko, 2006). An enzyme can exploit the resulting spatial gradient for proofreading. (b) At low enzyme activity (i.e. low $k_{on}⁢ρ_{_{E}}$), the gradient of $S^{*}$ is successfully maintained, allowing for proofreading. The upper dashed line corresponds to the peak fidelity when the substrate profile is exponential. At high enzyme activity (large $k_{on}⁢ρ_{_{E}}$), the dephosphorylation with rate $k_{p}=5$ s-1 is no longer sufficient to maintain the gradient and proofreading is lost. (c) Profiles of right substrates for different choices of enzyme activity. Numbers indicate $k_{on}⁢ρ_{_{E}}$ in s-1 units. The black line shows an exponential substrate profile with a length scale $\lambda_{_{S}}=\sqrt{D/k_{p}}∼0.5$ μm.

We test the proofreading power of such gradients, assuming experimentally constrained biophysical parameters for the gradient forming mechanism. Specifically, we consider an enzyme $E$ that acts on the active forms of cognate ($R^{*}$) and non-cognate ($W^{*}$) substrates which have off-rates 0.1 s-1 and 1 s-1, respectively (hence, $η_{eq}=10$). These off-rates are consistent with typical values for substrates proofread by cellular signaling systems (Cui and Mehta, 2018; Gascoigne et al., 2001). The kinases and phosphatases in our setup act identically on right and wrong substrates. We consider a dephosphorylation rate constant $k_{p}=5$ s-1 that falls in the range 0.1−100 s-1 reported for different phosphatases (Brown and Kholodenko, 1999; Kholodenko et al., 2000; Todd et al., 1999), and a cytosolic diffusion constant $D=1$ μm2/s for all proteins in this model. With this setup, exponential gradients of length scale ∼0.5 μm are formed for $R^{*}$ and $W^{*}$. We evaluate the proofreading and energetic performance of the model in a compartment of size $L=10$ μm – a typical length scale in eukaryotic cells (see Appendix 6 for details).

Although not cost-efficient, this setup achieves proofreading in a wide range of regimes. Specifically, it is most effective when the enzyme–substrate binding is slow, in which case the exponential substrate profile is maintained and the system attains the fidelity predicted by our earlier explanatory model (Figure 5b). The system’s proofreading capacity is retained if the first–order on-rate is raised up to $k_{on}ρ_{_{E}}∼10$ s-1, where around 10-fold increase in fidelity is still possible. If the binding rate constant ($k_{on}$) or the enzyme’s expression level ($ρ_{_{E}}$) is any higher, then enzymatic reactions overwhelm the ability of the kinase/phosphatase system to keep the active forms of substrates sufficiently localized (Figure 5c) and proofreading is lost. Overall, this model suggests that enzymes can work at reasonable binding rates and still proofread, when accounting for an experimentally characterized gradient maintaining mechanism.

## Discussion

We have outlined a way for enzymatic reactions to proofread and improve specificity by exploiting spatial concentration gradients of substrates. Like the classic model, our proposed spatial proofreading scheme is based on a time delay; but unlike the classic model, here the delay is due to spatial transport rather than transitions through biochemical intermediates. Consequently, the enzyme is liberated from the stringent structural requirements imposed by traditional proofreading, such as multiple intermediate conformations and hydrolysis sites for energy coupling. Instead, our scheme exploits the free energy supplied by active mechanisms that maintain spatial structures.

The decoupling of the two crucial features of proofreading – time delay and free energy dissipation – allows the cell to tune proofreading on the fly. For instance, all proofreading schemes offer fidelity at the expense of reaction speed and energy. For traditional schemes, navigating this trade-off is not always feasible, as it needs to involve structural changes via mutations or modulation of the [ATP]/[ADP] ratio which can cause collateral effects on the rest of the cell. In contrast, the spatial proofreading scheme is more adaptable to the changing conditions and needs of the cell. The scheme can prioritize speed in one context, and fidelity in another, simply by tuning the length scale of intracellular gradients (e.g. through the regulation of the phosphotase or free enzyme concentration in the scheme discussed earlier).

On the other hand, this modular decoupling can complicate the experimental identification of proofreading enzymes and the interpretation of their fidelity. Here, the enzymes need not be endowed with the structural and biochemical properties typically sought for in a proofreading enzyme. At the same time, any attempt to reconstitute enzymatic activity in a well-mixed, in vitro assay, will show poor fidelity compared to in vivo measurements, even when all necessary molecular players are present in vitro. Therefore, more care is required in studies of cellular information processing mechanisms that hijack a distant source of free energy compared to the case where the relevant energy consumption is local and easier to link causally to function.

While we focused on spatially localized substrates and delocalized enzymes, our framework would apply equally well to other scenarios, like one with a spatially localized enzyme (or its active form [Kalab et al., 2002; Nalbant et al., 2004]) and effector with delocalized substrates, an example of which would be an alternative version of the scheme in Figure 5a where the target of the kinase/phosphatase activity is changed from substrates to enzymes. Our framework can also be extended to signaling cascades, where slightly different phosphatase activities can result in magnified concentration ratios of two competing signaling molecules at the spatial location of the next cascade step (Roy and Cyert, 2009; Bauman and Scott, 2002; Kholodenko, 2006).

The spatial gradients needed for the operation of our model can be created and maintained through multiple mechanisms in the cell, ranging from the kinase/phosphatase system modeled here, to the passive diffusion of substrates/ligands combined with active degradation (e.g. Bicoid and other developmental morphogens), to active transport processes combined with diffusion. A particularly simple implementation of our scheme is via compartmentalization – substrates and effectors are localized in two spatially separated compartments with the enzyme–substrate complex having to travel from one to another to complete the reaction.

Many molecular localization pathways involving the naturally compartmentalized parts of the cell require high substrate selectivity and are therefore potential candidates for the implementation of spatial proofreading. For example, in polarized, asymmetric cells (e.g. budding yeast or neuronal cells) gene expression often needs to be spatially regulated (Parton et al., 2014; Martin and Ephrussi, 2009). Such regulation is achieved with designated ribonucleoproteins that bind specific mRNAs near the cell nucleus, perform a biased random walk to the mRNA localization site and deliver them for translation. During transport, mRNAs are protected from ribosome binding and when they unbind, they are subject to degradation which would prevent rebinding events at intermediate locations. Another example process is the non-vesicular transport of lipids between the membrane–bound domains of the cells (e.g. the ER, mitochondria, the Golgi apparatus, or the plasma membrane). This transport mechanism is mediated by lipid-transfer proteins that bind lipids on the donor membrane, diffuse to the acceptor membrane and upon interacting with it, undergo a conformational change, delivering the ‘cargo’ (Lev, 2010). Although the higher proximity of the two membranes is thought to enhance the transport efficiency, it would be interesting to study the optimality of the inter-membrane distance in the context of fidelity–transport efficiency trade-off, given the fact that some of the lipid-transfer proteins are known to exhibit specificity for their cognate substrates.

Our scheme may also be applicable as a quality control mechanism in protein secretion pathways (Ellgaard and Helenius, 2003; Arvan et al., 2002), in high-fidelity targeting of membrane proteins mediated by signal recognition particles (Rao et al., 2016; Chio et al., 2017), as well as in selective glycosylation reactions in the Golgi apparatus (Jaiman and Thattai, 2020). Lastly, considering the recent advances in generating synthetic morphogen patterns in multicellular organisms (Toda et al., 2020; Stapornwongkul et al., 2020), spatial proofreading could also be employed in pathways acting on engineered protein gradients. Experimental investigations of these processes in light of our work will reveal the extent to which spatial transport promotes specificity.

In conclusion, we have analyzed the role played by spatial structures in endowing enzymatic reactions with kinetic proofreading. Simply by spatially segregating substrate binding from catalysis, enzymes can enhance their specificity. This suggests that enzymatic reactions may acquire de novo proofreading capabilities by coupling to pre-existing spatial gradients in the cell.

## Materials and methods

Detailed derivations of the analytical results presented in the main text along with additional studies on our model are included in the Appendices. In addition, Python scripts and Jupyter notebooks used to generate all the plots in the main text and Appendices are included as Supplementary files.

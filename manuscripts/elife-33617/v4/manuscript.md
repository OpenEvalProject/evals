# Signaling pathways as linear transmitters

## Authors

- Harry Nunns<sup>1</sup> ([ORCID: 0000-0002-9669-0039](https://orcid.org/0000-0002-9669-0039)) †
- Lea Goentoro<sup>1</sup> ([ORCID: 0000-0002-3904-0195](https://orcid.org/0000-0002-3904-0195)) †

### Affiliations

1. Division of Biology and Biological Engineering California Institute of Technology Pasadena United States

† Corresponding author

## Abstract

One challenge in biology is to make sense of the complexity of biological networks. A good system to approach this is signaling pathways, whose well-characterized molecular details allow us to relate the internal processes of each pathway to their input-output behavior. In this study, we analyzed mathematical models of three metazoan signaling pathways: the canonical Wnt, MAPK/ERK, and Tgfβ pathways. We find an unexpected convergence: the three pathways behave in some physiological contexts as linear signal transmitters. Testing the results experimentally, we present direct measurements of linear input-output behavior in the Wnt and ERK pathways. Analytics from each model further reveal that linearity arises through different means in each pathway, which we tested experimentally in the Wnt and ERK pathways. Linearity is a desired property in engineering where it facilitates fidelity and superposition in signal transmission. Our findings illustrate how cells tune different complex networks to converge on the same behavior.

## Introduction

Cells must continually sense, interpret, and respond to their environment. This is orchestrated by signaling pathways: networks of multiple proteins that transmit signals and initiate cellular response. Signaling pathways are critical to animal development and physiology, and yet there are fewer than 20 classes of metazoan signaling pathways (Gerhart, 1999). These signaling pathways evolved prior to the Cambrian and remain highly conserved across animal phyla (Gerhart, 1999; Pires-daSilva and Sommer, 2003). Each signaling pathway, therefore, governs a wide range of cellular events, both within and across organisms.

Insights into the versatility of signaling pathways may be gleaned from pathway architectures. Indeed, distinct architectural features define each pathway. Studies over the past several decades have revealed distinct signaling capabilities that arise from pathway architecture, for example, all-or-none response in the MAPK/ERK pathway (Huang and Ferrell, 1996; Ferrell and Machleder, 1998), oscillations in the NFκB pathway (Hoffmann et al., 2002), or asymmetrical cell signaling in the Notch/Delta pathway (Sprinzak et al., 2010). Alternatively, analysis of pathway architectures may also reveal shared signaling capabilities that emerge from the distinct architectures, pointing to a fundamental property that pathways have converged upon despite their separate evolutionary trajectories. In this study, we sought to identify shared properties between conserved signaling pathways.

To this end, we examined three signaling pathways, the canonical Wnt, ERK and Tgfβ pathways. These pathways are activated by an extracellular ligand binding to a membrane receptor (Figure 1A). The ligand-receptor activation initiates a series of biochemical reactions within the cell, culminating in a buildup of transcriptional regulator, which regulates transcription of broad gene targets. Since the ligand-receptor module is relatively plastic across organisms (e.g. flies have one EGF receptor whereas humans have four [Citri et al., 2003]), we focused on the conserved core pathway (Figure 1A). We define the input to the core pathway as the ligand-receptor activation, and the output as the level of transcriptional regulator.

![Figure 1.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig1-v4.jpg)

**Figure 1.:** (A) Signaling pathways transmit inputs from ligand-receptor interaction to a change in output, the level of transcriptional regulator (white circle). (B-D) The core pathway for each metazoan signaling pathway is defined by distinct architectural features. In the Wnt pathway (B), the output is regulated by a futile cycle of continual synthesis and rapid degradation. In the ERK pathway (C), the output is regulated by a kinase cascade coupled to negative feedback. In the Tgfβ pathway (D), the output is regulated through continual nucleocytoplasmic shuttling.

The Wnt, ERK, and Tgfβ pathways transmit input using different core transmission architecture (Figure 1B–D). In the Wnt pathway, signal transmission is characterized by a futile cycle of synthesis and rapid degradation (Kimelman and Xu, 2006; Saito-Diaz et al., 2013; Hoppler and Moon, 2014). We use the term futile cycle to highlight that β-catenin is continually synthesized only to be quickly targeted for degradation and kept at low concentration, as opposed to, for instance, being synthesized only as needed. Ligand-receptor input diminishes the degradation arm of this cycle, leading to accumulation of β-catenin output (Kimelman and Xu, 2006; Stamos and Weis, 2013; Nusse and Clevers, 2017). In the ERK pathway, signal transmission is characterized by a cascade of phosphorylation events coupled to feedbacks, leading to an increase in phosphorylated ERK output (Kolch, 2005; Yoon and Seger, 2006; Avraham and Yarden, 2011; Lake et al., 2016). Finally, signal transmission in the Tgfβ pathway is characterized by continual nucleocytoplasmic protein shuttling (Inman et al., 2002; Nicolás et al., 2004; Xu and Massagué, 2004; Schmierer and Hill, 2005; Massagué et al., 2005). Ligand-receptor input effectively increases the rate of nuclear import, leading to an increase in output, the nuclear Smad complex (Schmierer et al., 2008).

Importantly for our approach, the architectures of the three pathways are captured by mathematical models that have been refined by years of experiments. Although by no means complete, the mathematical models have track records of success in predicting systems-level behaviors across multiple biological systems. For instance, the Wnt model (Lee et al., 2003) captures the dynamics of destruction complex well enough as to enable prediction of robustness in fold-change response (Goentoro and Kirschner, 2009) and the differential roles of the two scaffolds in the pathway (Lee et al., 2003); the ERK model (Huang and Ferrell, 1996; Ferrell and Bhatt, 1997; Schoeberl et al., 2002; Sturm et al., 2010) captures the ultrasensitivity in the phosphorylation cascade (Huang and Ferrell, 1996); and the Tgfβ model (Schmierer et al., 2008) reveals the roles of nucleocytoplasmic shuttling in transducing the duration and intensity of ligand stimulation (Schmierer et al., 2008).

We studied these mathematical models to identify what, if any, behaviors converge across pathways. The Wnt (Lee et al., 2003), ERK (Sturm et al., 2010), and Tgfβ (Schmierer et al., 2008) models consist of 7, 26, and 10 coupled, nonlinear ODEs, respectively, with 22, 46, and 13 parameters. Because of their large sizes, they are typically solved numerically to simulate experimental observations and generate new predictions. However, for the questions posed here, we found that numerical simulations are not sufficient. Rather, we needed analytics to uncover exactly how the pathway behaviors depend on the underlying biochemical processes. While we previously derived an analytical solution to the Wnt pathway (Goentoro and Kirschner, 2009), analytical treatment of the Tgfβ and ERK pathways has not been attempted due to the complex, nonlinear equations involved. To address this problem, we employed various analytical techniques, including graph theory-based variable elimination and dimensional analysis, to derive analytical or semi-analytical solutions to the steady-state output of each pathway. Our analysis, along with subsequent experimental verification, reveals a striking convergence across the Wnt, Tgfβ, and ERK pathways: cells operate in the parameter regime where the complex, nonlinear interactions in each pathway give rise to linear signal transmission.

## Results

### Mathematical analysis identifies the Wnt, ERK, and Tgfβ pathway as linear transmitters

We began our analysis using established models of the Wnt (Lee et al., 2003), ERK (Sturm et al., 2010), and Tgfβ (Schmierer et al., 2008) pathways. These models capture the salient features of each pathway, and include biochemical details such as synthesis, degradation, binding, dissociation and post-translational modifications. In all the models, biochemical parameters have been directly measured or fitted to kinetic measurements from cell, embryo or extract systems. Numerical simulation of each model has predicted a wide range of pathway behaviors over the years (e.g. Wnt refs. [Lee et al., 2003; Goentoro and Kirschner, 2009; Hernández et al., 2012]; ERK refs. [Huang and Ferrell, 1996; Ferrell and Machleder, 1998; Schoeberl et al., 2002; Sturm et al., 2010; Fritsche-Guenther et al., 2011]; Tgfβ refs. [Schmierer et al., 2008; González-Pérez et al., 2011; Andrieux et al., 2012; Vizán et al., 2013; Wang et al., 2014]). Below, we describe our analysis of each pathway and the unifying behavior that emerges from all three pathways.

### Canonical Wnt pathway

In this pathway, cells sense ligand-receptor input by monitoring β-catenin protein (Kimelman and Xu, 2006; Stamos and Weis, 2013; Nusse and Clevers, 2017; MacDonald et al., 2009; Clevers and Nusse, 2012). β-catenin is continually synthesized and rapidly degraded by a large destruction complex, comprised of multiple proteins including APC, Axin, and GSK3β. The destruction complex binds and phosphorylates β-catenin, tagging it for degradation by the ubiquitin/proteosome machinery (Kimelman and Xu, 2006; Stamos and Weis, 2013). Wnt ligands, through binding to Frizzled and LRP receptors, inhibit the destruction complex, leading to accumulation of β-catenin. β-catenin then regulates the expression of broad target genes (Stamos and Weis, 2013; Nusse and Clevers, 2017).

The model of the Wnt pathway (Figure 2A) was published in 2003 by a collaboration between the Kirschner and Heinrich labs (Lee et al., 2003). The Wnt model consists of seven nonlinear differential equations and 22 parameters. Applying dimensional analysis, we previously derived the analytical solution to β-catenin concentration at steady-state (Goentoro and Kirschner, 2009):

$$
[\betacat]_{ss}=K_{17}⋅\frac{1−\gamma+\frac{\alpha}{u}}{2}(\sqrt{1+\frac{4\gamma}{(1−\gamma+\frac{\alpha}{u}^{2})}}−1)
$$



$$
\alpha=\frac{k_{4}k_{6}k_{9}v_{14}⋅GSK3_{tot}⋅APC_{tot}}{k_{5}k__{6}K_{7}K_{8}k_{13}k_{15}}
$$



$$
\gamma=\frac{v_{12}}{k_{13}K_{17}}
$$

![Figure 2.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-v4.jpg)

**Figure 2.:** (A-C) Network diagrams of the signaling pathways. The Tgfβ diagram is modified from Schmierer et al. (2008). In the network diagram in A, DC refers to the β-catenin destruction complex. Below the network diagrams: the parameter groups and linearity equations we analytically derived in this study. Parameter groups and input functions are color-coded to the corresponding reactions in the network diagrams. Parameters that do not appear in the parameter groups either drop out due to irreversible reaction steps (such as k10 and k11 in the Wnt pathway) or negligible (as indicated by ellipses). (D-F) Our analysis reveals that in physiologically relevant parameter values, these pathways generate a linear input-output relationship. The outputs are β-catenin, dpERK, and nuclear Smad complex for the Wnt, ERK, and Tgfβ pathway, respectively. The input functions $u$ describe the effect of ligand-receptor interactions on the core pathway. Specifically: $u(Wnt)$ is the rate by which Dishevelled/Dvl inhibits the destruction complex upon Wnt ligand activation, where $k_{3}$ and $k_{−6}$ are defined in the figure and [Dvl]a is the concentration Wnt-activated Dishevelled (see Equations A15); u(EGF) is concentration of EGF-activated Ras (Ras-GTP); and u(Tgfβ) is the fraction of Tgfβ -activated receptors. Red and blue lines, respectively: analytical and numerical solutions with measured parameters (plotted against the left y-axis). Grey line: examples of numerical solutions outside measured parameters (plotted against the right y-axis).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-figsupp1-v4.jpg)

**Figure 2—figure supplement 1.:** (A) Parameter groups in the ERK model are constant to within 10%, over the physiologically relevant range of u considered here, justifying the inclusion of variables into the parameter groups. (B–C) The dpERK output is an ultrasensitive function of both free and total phosphorylated Raf. The values $E_{s}$ and $R_{s}$ are illustrated in (B), and are defined in Appendix 1. (D–F) Numerical simulation of pulsatile response in the ERK pathway. (D) A pulse of input, RasGTP, is generated by EGF addition in an ERK model that includes details of receptor desensitization (Schoeberl et al., 2002). Basal activity of Ras is included to ensure constitutive negative feedback (Fritsche-Guenther et al., 2011). (E) dpERK output also exhibits a pulsatile response, peaking within 10 min. (F) We plot the peak dpERK output against peak input for a range of physiologically relevant u(EGF) doses, and find that it matches our steady-state predictions for linear input-output behavior. (G) Five-fold Raf overexpression does not break the linear input-output behavior.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-figsupp2-v4.jpg)

**Figure 2—figure supplement 2.:** (A–B) Numerical simulation of the ERK and Tgfβ models. (A) The ERK model shows linear input-output relationship up to 93% of dpERK activation. (B) The Tgfβ pathway shows linear input-output relationship throughout the entire input range (from 0 to 1). Linearity was analyzed using the L1-norm or least absolute deviation (see Materials and methods). The blue range indicates where L1-norm was computed.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-figsupp3-v4.jpg)

**Figure 2—figure supplement 3.:** (A) Nuclear Smad4 concentration is constant to within 2%, over a physiologically relevant range of u(Tgfβ) considered here, justifying its inclusion into parameter group $\alpha$. (B–D) Numerical simulation of pulsatile response in the Tgfβ pathway. (B) A pulse of input, active Tgfβ receptor, is generated by Tgfβ addition in a model that includes details of receptor desensitization (Vizán et al., 2013). (C) S24n output also exhibits a pulsatile response. (D) We plot the peak S24n output against peak input, and find that it matches our steady-state predictions for linear input-output behavior.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-figsupp4-v4.jpg)

**Figure 2—figure supplement 4.:** We include the role of GSK3β in phosphorylating LRP5/6 into the input function u(Wnt), such that u(Wnt) is a function of GSK3β and the phosphorylation rate k9 (for simplicity, the same rate as GSK3β phosphorylation of β-catenin), and the reverse rate kr. In both models, β-catenin increases in response to GSK3β inhibition (e.g., by CHIR99021). However, only the model with the dual function of GSK3β shows a decrease in input range that we observed experimentally.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-figsupp5-v4.jpg)

**Figure 2—figure supplement 5.:** In each plot, we varied S, defined in the equation shown on the x-axis, and simulated the input-output curve over the dynamic range of the model. The parameters in the equations are as defined in the main text. For the ERK and Tgfβ pathway, $\alpha$ and γ are linked in such a way that they could not easily be varied independently. Linearity was assessed using the L-1 norm, which ranges from 0 to 0.5, with L-1 norm < 0.1 indicating linearity. L1-norm analysis was performed over the full dynamic range of the system, i.e., u(Wnt) = 1- 6, u(ERK) = 0 to 110,000 molecules of Ras-GTP, which gave 90% activation of [dpERK] in unperturbed cells, and u(Tgfβ) = 0 to 1.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-figsupp6-v4.jpg)

**Figure 2—figure supplement 6.:** In this analysis, the parameter groups in each model were varied as indicated e.g., 3x is three-fold increase, 0.3x is three-fold decrease. 1x corresponds to the measured parameters. Plotted in each box is the input-output relationship, numerically simulated over the full dynamic range of the models, i.e., 1-6 for u(Wnt), 0-105 for u(EGF), and 0-1 for u(Tgfβ). For simplicity, all outputs are normalized from 0 to 1. Grey shade: the unperturbed state. Purple shade: linear input-output response, as defined by L-1 norm < 0.1.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig2-figsupp7-v4.jpg)

**Figure 2—figure supplement 7.:** We used the model first built by Hoffman et al. in 2002 (Hoffmann et al., 2002) and later revised by Ashall et al. in 2009 (Ashall et al., 2009). The parameters in the model have been measured or fitted to single-cell dynamics in multiple cell types (Hoffmann et al., 2002; Ashall et al., 2009). We simulated the model here over a physiologically observed dynamic range, i.e., Lee et al. (2014) observed in HeLa cells that at saturating ligand dose (10 ng/mL TNFα, set to one in the model),~25% of NF-κB pool is nuclear. Linearity is assessed using the L1-norm, where L1-norm < 0.1 indicates linear relationship (see Materials and methods).

where the input function $u=u(Wnt)$ is the rate of inhibition of the destruction complex (DC) via Dishevelled/Dvl, a function of ligand-receptor activation. As illustrated in Figure 2A, Ki’s are equilibrium dissociation constants, ki’s are rate constants, and vi’s are synthesis rates. $\alpha$ and $\gamma$ in Equation 1 are dimensionless parameter groups defined in Equations 2 and 3: $\alpha$ characterizes β-catenin degradation by the destruction complex, and $\gamma$ characterizes the extent to which β-catenin binds to APC independently of the destruction complex.

Equation 1 demonstrates that, in general, β-catenin concentration is a nonlinear function of the input $u$. Many parameters of the model were directly measured in Xenopus extracts, and the remaining calculated from measurements in the same system (Appendix 1—table 1). In this study, we examined how the analytical solution (Equation 1) behaves with these measured parameters. The measured parameters (Appendix 1—table 1) indicate that $\alpha~66$, $\gamma~1.4$, and for maximal stimulation, $u~6.0$. The large $\alpha$ reflects how β-catenin stability is primarily dictated by the destruction complex, that is, $\alpha/u≫1$ means that non-Axin-dependent degradation is minimal, and $\alpha/u≫\gamma$ means that the positive feedback from sequestration by APC is minimal. Indeed, the rapid action of the destruction complex in the Wnt pathway is a recurring observation across biological systems (Kimelman and Xu, 2006; Saito-Diaz et al., 2013; Hoppler and Moon, 2014). With $\alpha/u≫1+\gamma$, Equation 1 simplifies to

$$
[\betacat]_{ss}≈K_{17}\frac{\gamma}{\alpha}u
$$

with detailed derivations presented in Appendix 1. Therefore, within physiologically relevant parameter values, the steady-state β-catenin concentration becomes a linear function of the input $u$ (red line, Figure 2D). The linear input-output relationship holds for the entire dynamic range of the model, until the system saturates at maximal stimulation ($u∼6.0$). We confirmed that the numerical solution of the full model matches the analytical solution in Equation 4 (blue line, Figure 2D), and that the response becomes nonlinear when $\alpha$ is decreased, breaking the requirement $\alpha/u≫1+\gamma$ (grey line, Figure 2D).

Source codes for the numerical simulations in Figure 2D–F (grey and black lines) are available in Figure 2—source code 1.

### ERK pathway

The unexpected linearity that emerges from the model of the Wnt pathway prompted us to wonder if such simplicity may be found in other pathways. Strikingly, we observed the same linearity in the ERK and Tgfβ pathways. In the ERK pathway (Figure 2B), ligand-receptor input is transmitted via a cascade of protein phosphorylation (Kolch, 2005; Yoon and Seger, 2006). In particular, ligand-receptor interactions activate Ras, which leads to membrane recruitment and phosphorylation of Raf. Phosphorylated Raf subsequently doubly phosphorylates MEK, which in turn doubly phosphorylates ERK (Kolch, 2005). Doubly-phosphorylated ERK (dpERK) is a transcriptional regulator that affects a broad array of genes (Yoon and Seger, 2006). The multi-step topology of the kinase cascade, combined with distributive phosphorylation of each kinase, gives rise to ultrasensitivity – first demonstrated in the seminal work by the Ferrell lab (Huang and Ferrell, 1996; Ferrell and Machleder, 1998). In other contexts, the pathway also exhibits a graded response (Whitehurst et al., 2004; Mackeigan et al., 2005; Cohen-Saidon et al., 2009; Ahmed et al., 2014) that is thought to arise from the incorporation of negative feedbacks (Lake et al., 2016), one of which is the inhibition of Raf by dpERK through hyper-phosphorylation of serine residues (Sturm et al., 2010; Dougherty et al., 2005; Hekman et al., 2005).

The ERK model (Sturm et al., 2010) is the product of more than two decades of refinement (Huang and Ferrell, 1996; Ferrell and Machleder, 1998; Schoeberl et al., 2002; Sturm et al., 2010; Fritsche-Guenther et al., 2011). The model, which captures ultrasensitivity and Raf feedback, consists of 26 differential equations and 46 parameters. To derive an analytical expression for the ERK pathway, we used a variable elimination technique developed for networks of mass action kinetics (Feliu and Wiuf, 2012). The technique utilizes an algebraic framework, linear elimination of variables, and mass conservation laws to parameterize steady-state in terms of core variables (described in Appendix 1). We derived an analytical relationship between the steady-state output of the pathway $[dpERK]_{ss}$ and the input to the phosphorylation cascade $u$:

$$
[dpERK]_{ss}=\frac{\alpha}{\beta}⋅(\frac{Raf_{tot}}{[pRaf]_{ss}})−1−\frac{\gamma}{\alpha}⋅u−\frac{\delta}{\beta}
$$



$$
\alpha=\frac{k_{3}⋅(k_{8}+k_{b7})}{k_{7}⋅[P1]_{ss}⋅k_{8}}+⋅⋅⋅
$$



$$
\beta=\frac{k_{25}⋅(k_{30}+k_{b29}+k_{29}⋅[P4]_{ss})}{k_{29}⋅[P4]_{ss}⋅k_{30}}+⋅⋅⋅
$$



$$
\gamma=\frac{k_{3}⋅(k_{8}+k_{b7})⋅k_{9}⋅[MEK]_{ss}}{k_{7}⋅[P1]_{ss}⋅k_{8}⋅k_{10}}+⋅⋅⋅
$$



$$
\delta=\frac{k_{26}+k_{b25}}{k_{26}}+…
$$

Detailed derivations of Equation 5 are presented in Appendix 1. The input $u=u(EGF)$ in Equation 5 is the concentration of active Ras, which is activated via GTP loading at the ligand-receptor complex (Kolch, 2005). The parameter groups $\alpha$, $\beta$, $\gamma$, and $\delta$ in Equation 5 are defined in Equations 6–9, where the ellipses indicate additional small terms (expanded in Appendix 1). The relative magnitudes of $\alpha$, $\beta$, $\gamma$, and $\delta$ indicate how the Raf pool partitions during signaling (Equations A21, A29–A31). The dimensionless group $\alpha⋅u$ relates to the amount of free, phosphorylated Raf ($\alpha$, blue-shaded in Figure 2B), $\beta⋅[dpERK]_{ss}$ describes the amount of Raf inhibited through negative feedback by dpERK ($\beta$, red-shaded in Figure 2B), $\delta$ relates to the amount of unphosphorylated ($\delta$, blue-shaded in Figure 2B), and $\gamma⋅u$ relates to the amount of phosphorylated Raf bound to other proteins (e.g. to MEK, brown-shaded in Figure 2B). Equation 5 is not a closed solution, as it includes the term $pRaf_{ss}$, and there are variables included in parameter groups $\alpha$, $\beta$, $\gamma$. We confirmed that the parameter groups remain constant over the course of signaling (within 10%, Figure 2—figure supplement 1), justifying treating the latter variables as parameters.

Next, we considered how the analytical expression (Equation 5) behaves within a specific parameter regime observed in experiments. First, experiments in several mammalian cell systems have shown that feedback is strong, such that a significant fraction of the Raf pool is inhibited (Fritsche-Guenther et al., 2011; Dougherty et al., 2005). This means that $\beta⋅dpERK_{ss}~\alpha+\gamma⋅u+\delta$. Second, as has been observed in multiple contexts ([Huang and Ferrell, 1996; Ferrell and Machleder, 1998; Schoeberl et al., 2002; Sturm et al., 2010] Appendix 1—table 2), ERK phosphorylation is ultrasensitive to the amount of pRaf (the ultrasensitive cascade is shaded green in Figure 2B). Denoting $K$ as the relative change of $dpERK_{ss}$ with respect to $pRaf_{ss}$, ultrasensitivity entails that $K≫1$. In this range, small changes in pRaf level have very large effects on dpERK level (e.g., in model simulations, a 30% change in pRaf level results in a 900% change in dpERK level, Figure 2—figure supplement 1). We find analytically that in the parameter regime where $\beta⋅dpERK_{ss}~\alpha+\gamma⋅u+\delta$ and $K≫1$, the negative feedback holds the level of pRaf constant ($pRaf_{ss}≈R_{s}$, details in Appendix 1). With these two features, strong negative feedback and ultrasensitivity, dpERK becomes a linear function of the input $u$:

$$
[dpERK]_{ss}≈\frac{\alpha}{\beta}⋅\frac{Raf_{tot}}{R_{s}}⋅u−\frac{\delta}{\beta}
$$

The full derivation is given in Appendix 1, and includes a toy model to illustrate the intuition for how ultrasensitivity combines with negative feedback to produce linearity. Equation 10 is plotted in Figure 2E (red line). We confirmed that the numerical solution of the full model matches the analytics in Equation 10, and becomes nonlinear when the negative feedback is weakened (grey line, Figure 2E). Although the analytical expression describes up until 50% of ERK activation, we verified numerically that the predicted linearity extends to 93% of ERK activation (Figure 2—figure supplement 2).

The linearity derived here applies across different dynamic ERK responses. The model we analyzed gives a sustained dpERK response. In some contexts, however, the ERK pathway shows a pulsatile response, which has been attributed to receptor desensitization (Schoeberl et al., 2002). Using a larger model that includes details of receptor desensitization (Schoeberl et al., 2002), we numerically verified that the linearity holds for pulsatile responses - that is, the peak level of dpERK increases linearly with the peak level of $u$ (Figure 2—figure supplement 1).

### Tgfβ pathway

Finally, we examined signal transduction within the Tgfβ pathway (Figure 2C). In the Tgfβ pathway, input from ligand-receptor interactions is transmitted by the Smad proteins. There are several classes of Smad proteins, including the receptor-regulated Smads (R-Smads) and the common Smad (co-Smad or Smad4) (Massagué et al., 2005). Ligand-activated receptors phosphorylate R-Smads. Phosphorylated R-Smads bind to the co-Smad, and shuttle into the nucleus and regulate broad target genes. In the nucleus, the Smad complex dissociates and R-Smads are constitutively de-phosphorylated and shuttled out to the cytoplasm, where the cycle of phosphorylation and complex formation begins again (Schmierer et al., 2008). This dynamic translocation in and out of the nucleus forms a continual nucleocytoplasmic shuttling of Smads, a known integral feature of the Tgfβ pathway (Inman et al., 2002; Nicolás et al., 2004; Xu and Massagué, 2004; Schmierer and Hill, 2005).

The Tgfβ model (Schmierer et al., 2008) was published in 2008 by the Hill lab, and consists of 10 differential equations and 13 parameters. Even though the model was fitted to R-Smad2 data, the general architecture of signal transmission is conserved across all five R-Smads (Massagué et al., 2005; Schmierer et al., 2008). Using the variable elimination technique described before (Feliu and Wiuf, 2012), we derived an analytical expression of the steady-state concentration of Smad complex in the nucleus:

$$
[S24n]_{ss}=a⋅\frac{\alpha⋅u}{(\alpha+\gamma)⋅u+\beta}S2_{tot}
$$



$$
\alpha=\frac{a⋅(k_{on}[S4n]_{ss}+a⋅k_{ex2})}{k_{off}}+⋅⋅⋅
$$



$$
\beta=\frac{PPase⋅k_{dephos}}{k_{phos}⋅R_{tot}⋅\frac{k_{ex2}}{a⋅k_{ex2}+k_{in2}}}+⋅⋅⋅
$$



$$
\gamma=a⋅(a⋅k_{ex2}+PPase⋅k_{dephos})(\frac{1}{a⋅k_{ex2}}+\frac{1}{CIF⋅k_{in2}})+⋅⋅⋅
$$

In Equation 11, the input function $u=u(Tgf\beta)$ is the active fraction of Tgfβ receptors. The parameter $a$ is the nucleocytoplasmic volume ratio. The dimensionless parameter groups $\alpha$, $\beta$, and $\gamma$ in Equation 11 are defined in Equations 12–14, where the ellipses indicate additional small terms (expanded in Appendix 1). $\alpha$, $\beta$, and $\gamma$ describe how the Smad2 pool partitions during signaling (Equations A44, A50, A51): $\alpha⋅u$ relates to the amount of nuclear Smad complex ($\alpha$, blue-shaded in Figure 2C, captures the parameters related to complex formation and translocation to the nucleus), $\beta$ relates to the amount of free, unphosphorylated Smad2 ($\beta$, red-shaded in Figure 2C, captures the parameters related to complex dissociation and translocation to the cytoplasm), and $\gamma⋅u$ loosely relates to the remaining Smad2 pool ($\gamma$ is brown-shaded in Figure 2C). Phosphorylated Smad2 quickly forms complex (Lagna et al., 1996), so $\beta$ essentially corresponds to total monomeric Smad2. Finally, Equation 11 is not a closed solution, since variable $S4n_{ss}$ appears in $\alpha$. We numerically tested that it is constant within 2% for non-saturating inputs (Figure 2—figure supplement 3), justifying treating it as a parameter.

As in the Wnt and ERK pathway, the analytical expression for nuclear Smad complex (Equation 11) allows us to see that the behavior dramatically simplifies with parameters observed in experiment. We consider the case for non-saturating inputs ($u∼0.1$). Protein concentrations in the Tgfβ model were measured in human keratinocyte cells and the rate constants fitted to kinetic data measured in the cells (Schmierer et al., 2008). With the measured parameters (Appendix 1—table 3), we find that $\beta~46$, $\alpha⋅u~1.5$, and $\gamma⋅u~0.7$. In this parameter regime, once Smad2 is imported to the nucleus, it is rapidly dephosphorylated and exported. Dynamic Smad2 translocation maintains monomeric Smad2 in excess to Smad complex ($\beta≫\alpha+\gamma⋅u$). and forms the continual nucleocytoplasmic shuttling that is characteristic of the Tgfβ pathway. Even under maximal Tgfβ stimulation, it has been estimated that phosphorylated Smad2 comprises only 36% of the Smad2 pool (Schmierer and Hill, 2005; Gao et al., 2009). With $\beta≫\alpha+\gamma⋅u$, the first term in the denominator of Equation 11 is small, and concentration of nuclear Smad complex becomes a linear function of input:

$$
[S24n]_{ss}≈a⋅\frac{\alpha⋅S2_{tot}}{\beta}⋅u
$$

Equation 15 is plotted in Figure 2F (red line), and we confirmed that numerical simulations recapitulates Equation 15 (blue line, Figure 2F). Although the analytical solution is valid only for small values of u, we numerically verified that the predicted linearity holds for the entire range of input u (from 0 to 1, Figure 2—figure supplement 2). We confirmed that the pathway becomes nonlinear when the R-Smad phosphatase is inhibited such that $\beta~\alpha+\gamma⋅u$ (grey line, Figure 2F). While the model analyzed here gives a sustained Smad response, we verified numerically that the linearity holds for a larger model that includes receptor desensitization and gives a pulsatile Smad response (Figure 2—figure supplement 3) (Vizán et al., 2013).

### Linearity in the Wnt and ERK pathways was observed experimentally

Analytical expressions for the Wnt, ERK, and Tgfβ pathways reveal that the three pathways behave as linear signal transmitters within parameter regimes measured in cells. To confirm the linearity, we directly measured the input-output relationships in human cell lines. We focused our efforts on the Wnt and ERK pathways, since we are limited by available antibodies in the Tgfβ pathway.

To analyze the canonical Wnt pathway, we performed quantitative Western blot measurements in RKO cells, a model system for Wnt signaling. To track the input, we measured the level of phosphorylated LRP5/6 receptors (on Ser1490), which increases within minutes of ligand-receptor complex formation (Tamai et al., 2004). To track the output, we measured the level of β-catenin. We confirmed that the level of phosphorylated LRP5/6 and β-catenin increase upon Wnt simulation and reach steady-state within 6 hr (Figure 3—figure supplement 1). Accordingly, all subsequent measurements were done at 6 hr after Wnt stimulation.

To measure the input-output relationship in the Wnt pathway, we treated RKO cells with varying doses of purified Wnt3A and measured how β-catenin (output) correlates with phosphorylated LRP (input). As shown in Figure 3A, the level of β-catenin increases linearly with the level of phosphorylated LRP. The linearity persists until saturation of the input, defined as 90% of maximal phosphorylated LRP response (blue circles, Figure 3A; Figure 3—figure supplement 2). Notably, at high doses of Wnt3A, β-catenin continues to show incremental activation, despite saturation in phosphorylation of LRP (grey circles, Figure 3A). This can be explained within some findings that, while Frizzled/LRP complex is the primary receptor input in β-catenin activation, β-catenin can be activated independently of LRP (e.g. Rotherham and El Haj, 2015).

![Figure 3.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-v4.jpg)

**Figure 3.:** (A) Measurements of the input-output relationship in the Wnt pathway. In these experiments, RKO cells were stimulated with 0–1280 ng/mL purified Wnt3A ligand, harvested at 6 hr after ligand stimulation, and lysed for Western blot analyses. Shown on top is a representative Western blot. The data plotted come from seven independent experiments (total N = 66). Each circle indicate the mean intensities of the phospho-LRP5/6 (x-axis) and β-catenin (y-axis) bands for all Western blot biological replicates, and error bars indicate the standard error of the mean. For each gel, we normalize the unstimulated sample (i.e. 0 ng/mL of Wnt3A) to one, and scale the magnitude of the dose response to the average of all gels (described in Materials and methods). The grey line is a least squares regression line, and ρ is the Pearson’s coefficient, where ρ = 1 is a perfect positive linear correlation. (B) Measurements of the input-output relationship in the ERK pathway. In these experiments, H1299 cells were stimulated with 0–50 ng/mL purified EGF ligand, harvested at 5 min after ligand stimulation, and lysed for Western blot analyses. Shown on top is a representative Western blot. The data plotted here come from five independent experiments (total N = 30). Each circle indicates the mean intensities of dpERK1/2 bands across Western blot biological replicates, and the error bars indicate standard error of the mean. Single replicates are plotted without error bars. All data is plotted relative to unstimulated sample. The grey line is a least squares regression line, and r2 is the coefficient of correlation where r2 = 1 is a perfect linear correlation. (C) As in (A), except that cells were treated with 1 μM CHIR99021 (detailed in Materials and methods). The data plotted here come from five independent experiments (total N = 59). The grey line is a least squares regression, and ρ is the Pearson’s coefficient, where ρ = 1 is a perfect positive linear correlation. Shown in the subplot are the same least squares regression line (solid line), overlaid with the model prediction (dashed line). (D) As in (B), but measurements were performed in H1299 cells expressing mutant Raf S289/296/301A. The data plotted here come from three independent experiments (total N = 15). The grey line is a fit using the ERK model. We first fitted the gain of the model to the data (i.e. the y-range), and afterward, varied the strength of dpERK feedback (k25) to find the best fit. We used the weighted Akaike Information Criterion, w(AICc), to verify that the nonlinear fit from the ERK model outperforms a linear least squares fit (see Materials and methods). 0 < w(AICc) < 1, with higher w(AICc) indicates better performance by the non-linear fit. In all figures, linearity was additionally assessed using the least absolute deviations, L1-norm (see Methods). L1-norm can range from 0 to 0.5, with L1-norm < 0.1 indicate a linear relationship. Blue vs grey circles in each figure are explained in the main text. Source files of all Western blot gel images and numerical quantitation data are available in Figure 3—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp1-v4.jpg)

**Figure 3—figure supplement 1.:** RKO cells were treated with 160 ng/mL Wnt3A for the specified times, and then assayed for phospho-LRP5/6 and β-catenin level by Western blot. Error bars are standard error of the mean from 2 to 4 biological replicates. Data are plotted relative to the sample at time zero, and normalized to the average maximal activation across experiments. The grey lines connect the mean of each time point.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp2-v4.jpg)

**Figure 3—figure supplement 2.:** RKO cells were treated with the specified dose of Wnt3A for six hours, and then assayed for phospho-LRP5/6 and β-catenin by quantitative Western blot. Data are plotted relative to unstimulated samples. (A–B) In wt cells, phospho-LRP5/6 (A) shows > 90% of maximal response at 200 ng/mL Wnt3A, while β-catenin (B) shows 70% of maximal response at 200 ng/mL, and subsequently incremental response until 640 ng/mL Wnt3A. (C–D) In cells pre-treated with 1 µM CHIR99021, phospho-LRP5/6 (C) shows > 90% of maximal response at 80 ng/mL Wnt3A, while β-catenin (D) shows 70% of maximal response at 80 ng/mL and continues incremental activation at higher doses. (E). Cells were treated with 160 ng/mL Wnt3A and assayed for phospho-LRP5/6. Cells pre-treated with 1 µM CHIR99021 (N = 3) exhibited 50% the level of phospho-LRP5/6 as untreated cells (N = 3). The grey lines simply connect the means of data.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp3-v4.jpg)

**Figure 3—figure supplement 3.:** H1299 cells were treated with 1 ng/mL EGF for the specified times, and then assayed for dpERK1/2 by Western blot. Data is plotted relative to the samples at time zero, with at least three biological replicates per time point.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp4-v4.jpg)

**Figure 3—figure supplement 4.:** In these experiments, H1299 cells were treated with varying doses of EGF for 5 min, and then fixed and analyzed for immunofluorescence against doubly phosphorylated ERK (dpERK).(A) Representative images of cells treated with the indicated doses of EGF. (B) The intensity of nuclear level of dpERK staining across individual cells. Cell nuclei were delineated using DAPI staining (for EGF doses 0, 0.3, 1.3, and 2.0 ng/mL, N = 453, 381, 373, and 413 cells, respectively).

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp5-v4.jpg)

**Figure 3—figure supplement 5.:** H1299 cells over-expressing Raf-1 were treated with the indicated dose of EGF for 5 min, and then assayed for dpERK1/2 by Western blot. The grey line is a fit from a linear model with r2 = 0.99. Data is plotted relative to unstimulated samples, with total N = 9.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp6-v4.jpg)

**Figure 3—figure supplement 6.:** H1299 cells expressing the Raf mutant Raf S29/289/296/301/642 were treated with the indicated dose of EGF for 5 min, and then assayed for dpERK1/2 by Western blot. Data is plotted relative to unstimulated samples, with total N = 5.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp7-v4.jpg)

**Figure 3—figure supplement 7.:** (A) The level of β-catenin and phosphorylated LRP, measured across different lanes. (B) Ligand-stimulated change in β-catenin and phophorylated LRP level, measured in six independent Western blots. CV is coefficient of variation, defined as standard deviation/mean.

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp8-v4.jpg)

**Figure 3—figure supplement 8.:** In these two independent experiments, RKO cells were stimulated with a range of Wnt3A dose (0-160 ng/mL), the cells lysed after 6 hr, and analyzed for Western blot against β-catenin and phosphorylated LRP5/6 (pLRP5/6).Top row: In each experiment, GAPDH intensity varies with <10% CV across samples. Bottom row: Raw β-catenin and LRP intensity data without normalization with GAPDH loading control. The measurements are plotted relative to unstimulated cells. Grey lines are least squares regression lines, and $ρ$ is the Pearson correlation coefficient.

![Figure 3—figure supplement 9.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig3-figsupp9-v4.jpg)

**Figure 3—figure supplement 9.:** (A) In these two independent experiments, RKO cells were stimulated with a range of Wnt3A doses, lysed after 6 hr, and analyzed for Western blot against β-catenin and phospho-LRP5/6. (B) In these four independent experiments, H1299 cells were stimulated with a range of EGF doses, lysed after 5 min, and analyzed for Western blot against doubly-phosphorylated ERK. All measurements are plotted relative to unstimulated cells. Grey lines are least squares regression, ρ is Pearson correlation coefficient, and r2 is correlation coefficient.

Consistent with the mathematical analysis, we observed in RKO cells that the Wnt pathway behaves as a linear transmitter throughout the dynamic range of the input. As a control that is expected from the Michaelis-Menten kinetics that describe ligand binding in the model, we confirmed that the linearity does not extend upstream to Wnt dose: both phospho-LRP5/6 and β-catenin show nonlinear response to Wnt dose (Figure 3—figure supplement 2). Therefore, in the Wnt pathway, a nonlinear ligand-receptor processing step is followed by linear signal transmission through the core intracellular pathway.

Next, to measure the input-output relationship in the ERK pathway, we performed quantitative Western blots in H1299 cells, one of the model systems used in the field. Linearity in the ERK pathway has been suggested in different parts of the pathway, e.g. Knauer et al. (1984) used experimental and modeling analyses to infer linearity between receptor occupancy and the downstream cellular proliferation; Oyarzún et al. (2014) suggests linearity in ligand-receptor processing. Here, we specifically probe linearity in the core transmission step of the pathway. Detecting the input level, EGF-activated Ras GTP, requires a pull down step that makes it less quantifiable. Therefore, motivated by Oyarzún et al. (2014), we tested EGF ligand itself as the input. To track the output, we measured the level of doubly-phosphorylated ERK1/2 (on Thr202/Tyr204), dpERK. We first characterized the kinetics of response: dpERK peaks 5 min after EGF stimulation (Figure 3—figure supplement 3), and saturates at 4 ng/ml EGF (grey circles, Figure 3B). Accordingly, all subsequent measurements were performed at 5 min after EGF stimulation, and linearity was assessed over the input range of 0–4 ng/mL EGF (blue circles, Figure 3B).

We observed linearity in the input-output relationship of the ERK pathway, with the level of dpERK increasing linearly with EGF dose (Figure 3B). The linearity holds throughout the dynamic range of the system, over at least 12-fold activation of dpERK. As the ERK pathway is sometime observed to show bimodal response that would be masked by bulk measurements, we confirmed that the H1299 cells indeed show to graded dpERK response in single-cell level (Figure 3—figure supplement 4), in agreement with a previous single-cell, live imaging study (Cohen-Saidon et al., 2009). Therefore, as in the Wnt pathway, signals are transmitted linearly in the ERK pathway throughout the dynamic range of the cell. Moreover, the linearity in the ERK pathway is more extensive than in the Wnt pathway, as linearity extends all the way upstream, such that the level of dpERK directly reflects the dose of extracellular EGF ligand.

### Linearity in the Wnt and ERK pathways is modulated by perturbation to parameters

Finally, the analytical expressions we derived in this study not only reveal linear signal transmission, but also the mechanisms by which it arises. In the model of the Wnt pathway, linear transmission occurs due to the futile cycle of β-catenin, in the parameter regime where β-catenin is continually synthesized and rapidly degraded (i.e. $\alpha/u≫1+\gamma$). This regime is not infinite: for instance, a ten-fold decrease in $\alpha$ (e.g. by inhibiting the destruction complex) will break the futile cycle (grey line, Figure 2D).

To test if the futile cycle is indeed required for linear signal transmission, we inhibited the destruction complex using CHIR99021, an inhibitor of GSK3β kinase. As before, we measured the input-output relationship, β-catenin vs. phospho-LRP5/6 level, up to 90% of maximal phospho-LRP5/6 input (blue circles, Figure 3C). As expected, we found that inhibiting the destruction complex (decreasing $\alpha$ in the model) reduced the range of linearity. The non-treated cells (blue circles, Figure 3A) exhibit a linear input-output relationship over a 4.4-fold range of LRP input, whereas the CHIR-treated cells show a linear input-output relationship over only a 2.8-fold range of LRP input (blue circles, Figure 3C).

Further, our measurements also reveal an unexpected feature of the Wnt pathway. In the model, inhibiting GSK3β causes β-catenin response to become nonlinear for larger inputs (dashed line, Figure 3C subplot). In CHIR-treated RKO cells, however, this nonlinearity cannot be reached, as the maximal amount of phosphorylated LRP (input) is reduced by 50% (grey circles, Figure 3; Figure 3—figure supplement 2), consistent with the dual-function of GSK3β identified by Zeng et al. (2005); Zeng et al. (2008) in phosphorylating β-catenin for degradation as well as phosphorylation LRP for activation. Incorporating this dual-role of GSK3β into the model, we found that this expanded model can indeed recapitulate the data (Figure 2—figure supplement 4). Therefore, our data indicate two findings: first, that inhibiting GSK3β reduces the range of linear input-output behavior in the Wnt pathway, as predicted by our analytics, and second, that GSK3β co-regulation of β-catenin and LRP unexpectedly constrains the system within the linear regime.

Next, we examine the requirements for linearity in the ERK pathway. Equation 10 reveals that linearity in the ERK pathway depends upon the coupling of strong nonlinearities – ultrasensitivity and negative feedback. As in the Wnt pathway, this regime is not infinite, for example, decreasing the strength of feedback $\beta$ enables the system to exit the ultrasensitive regime, and therefore reduces linearity (grey line, Figure 2E).

To test this requirement, we examined the effects of weakening the negative feedback. We created a stable H1299 cell line expressing Raf S289/296/301A, a Raf-1 mutant in which three serine residues that are phosphorylated by dpERK are mutated to alanine (Dougherty et al., 2005; Hekman et al., 2005). Assessing the dynamic range of the input as before (0–4 ng/mL EGF), we now found that dpERK responds nonlinearly to EGF dose (blue circles, Figure 3D), consistent with model predictions (grey line, Figure 3D). As a control, we found that overexpressing WT Raf-1 to a similar level does not perturb linearity (experiments, Figure 3—figure supplement 5; modeling, Figure 2—figure supplement 1). Lastly, mutating all five direct ERK feedback sites on Raf-1 to alanine had a similar effect to Raf S289/296/301A (Figure 3—figure supplement 6). Our results support the model requirement that strong negative feedback is critical to linear signal transmission in the ERK pathway.

## Discussion

Our study suggests that the canonical Wnt pathway, the ERK pathway, and the Tgfβ pathway have converged upon a shared strategy of linear signal transmission. Our mathematical analysis reveals that, despite their distinct architectures, the three signaling pathways behave in some physiological contexts as linear transmitters. Not only is linearity is predicted within measured parameter regimes, the analysis shows that linearity is a property of the systems that occurs through a considerable range of parameters (Figure 2—figure supplements 5 and 6). We then showed direct measurements of the linear input-output relationship in the canonical Wnt and ERK pathway.

It would be interesting to further probe the generality of linear signal transmission. Linear behavior requires that single cells responds to ligand in a graded manner. Although there are reports of oscillatory or bimodality in signaling pathways, there are also multiple observations across biological contexts of single cells responding to ligand in a graded manner (Appendix 1—table 4). Besides the systems analyzed here, NF-κB is another signaling pathway that has been modeled rigorously (Hoffmann et al., 2002; Ashall et al., 2009; Lee et al., 2014). Numerical simulations of a well-established NF-κB model (Ashall et al., 2009) over the range of nuclear NF-κB translocation observed in human epithelial cells (Lee et al., 2014) reveal that the peak of the nuclear NF-κB pulse correlates linearly with ligand concentration (Figure 2—figure supplement 7). Finally, linearity extends beyond metazoan signaling pathways. In the yeast pheromone sensing pathway, a homolog of the ERK cascade, transcriptional output correlates linearly with receptor occupancy (Yu et al., 2008). The linearity is mediated by negative feedback by Fus3 acting on Sst2, a feedback that is not conserved in the mammalian ERK system. These further argue for linear signal transmission as a convergent property across independently evolving signaling pathways, as well as between conserved pathways that diverged 1.5 billion years ago.

What are potential advantages to linear signal transmission? Linearity is a feature of many engineering systems, where it serves several practical purposes. In particular, linear signal transmission enables the superposition of multiple signals, where the output of two simultaneous inputs is equal to the sum of the outputs for each input separately. Superposition enables multiple, dynamic signals to be faithfully transmitted and processed independently. Thus, for instance, linearity enables people to listen to a phone call and interpret speech amongst background noise, and allows a car radio to tune into one station out of multiple broadcasting on separate carrier frequencies. Notably, linearity is also a desired goal in synthetic biology, where it is often implemented using negative feedback (Nevozhay et al., 2009; Del Vecchio et al., 2016). Analogous to engineered circuits, linearity in biological signaling pathways may facilitate multiplexing inputs into a single pathway (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/33617/elife-33617-fig4-v4.jpg)

**Figure 4.:** (A) Linearity enables multiplexing of inputs to a signaling pathway. Multiplexed signals can be independently decoded downstream, and therefore regulate distinct transcriptional events. (B) Illustration for how linearity between the receptor occupancy and downstream outputs gives rise to dose-response alignment (Andrews et al., 2016). (C) Linearity can produce fold-changes in output that are robust to variation in cellular parameters. To illustrate this, we added lognormal noise (0.1 CV) to all parameters of the Wnt model, and simulated the level of β-catenin before and after Wnt stimulation (blue circles). As long as the model operates in the regime of linear signal transmission (i.e. $Y=a⋅u$, where $Y$ is output, $u$ is input, and $a$ is a scalar that is a function of parameters), variation in parameters affects stimulated and basal level of β-catenin equally, and we get a constant fold change in β-catenin (i.e. red line, where $FC=Y_{stimulated}/Y_{basal}$ is independent of parameter variations).

A second benefit is that linearity might underlie two phenomena that are increasingly found across signaling pathways. First, a linear transmitter naturally gives rise to dose-response alignment (Andrews et al., 2016), where one or more downstream responses of a pathway closely follows the fraction of occupied receptor (Figure 4B). Dose response alignment appears in many biological systems and is thought to improve the fidelity of information transfer through signaling pathways (Oyarzún et al., 2014; Yu et al., 2008; Andrews et al., 2016; Becker et al., 2010). Second, linearity facilitates fold change detection, where cells sense fold changes in signal, rather than absolute level, to buffer cellular noise (Goentoro and Kirschner, 2009; Cohen-Saidon et al., 2009; Lee et al., 2014; Thurley et al., 2014; Frick et al., 2017). In linear input-output systems, the stimulated output correlates linearly to the basal output; thus, the fold-change in output is robust to variations in cellular parameters (Figure 4C). Indeed, for the signaling pathways studied here, it has been shown experimentally that the robust outcome of ligand stimulation is the fold-change in the level of transcriptional regulator (Goentoro and Kirschner, 2009; Cohen-Saidon et al., 2009; Lee et al., 2014; Frick et al., 2017). Therefore, selecting for linearity may naturally confer the benefits of superposition, dose-response alignment, and a robust fold-change in output.

Interestingly, unlike synthetic circuits whose linearity is often designed to extend across multiple orders of magnitude (Nevozhay et al., 2009; Nevozhay et al., 2013), the linearity we observed in the three natural pathways extends only one order of magnitude, which is also the dynamic range of the pathways. However, we know that natural pathways can convey inputs varying across multiple orders of magnitude, for example, vision. Thus, an advantage of linearity in natural pathways may be that, in conjunction with fold-change detection at the receptor-level (Olsman and Goentoro, 2016), the system as a whole can continually adapt to a given input, hence maintaining sensitivity to future signals.

Why evolve complexity in signaling pathways only to produce seemingly simple behavior? We offer two thoughts. First, complexity of each pathway might afford tunability, in the sense that parameters can be tuned to produce different behaviors in different contexts. For instance, the ERK pathway produces digital, all-or-none response in some contexts (Huang and Ferrell, 1996), and analog response in others (Whitehurst et al., 2004; Mackeigan et al., 2005). Second - to take an example from engineering - in order to utilize physical processes that are not naturally linear, engineers must implement complex design features to approximate linearity. Similarly, many biochemical processes are inherently nonlinear, meaning that linearity does not arise from a reduction in complexity. Indeed, in each pathway we analyzed here, linearity emerges from complex interactions: a futile cycle in the Wnt pathway, ultrasensitivity coupled to feedback in the ERK pathway, and continual nucleocytoplasmic shuttling in the Tgfβ pathway. Therefore, analogous to engineered systems, complexity in the biochemical pathways we analyzed here might have evolved in part to produce linearity.

## Materials and methods

### Expression constructs

pBABEpuro-CRAF that contains the wt human Raf-1 clone was a gift from Matthew Meyerson (Addgene plasmid # 51124). Mutant Raf (S289/296/301A) and (S29/289/296/301/642A) were generated using the Q5 site-directed mutagenesis kit (New England Biolabs, E0554S). The mutant and wt Raf-1 were then placed downstream of a CMV promoter.

### Cell lines and cell culture

RKO cells (ATCC, CRL-2577) and H1299 cells (ATCC, CRL-5803) were authenticated by STR profiling and supplied by ATCC. RKO cells were cultured at 37°C and 5% (vol/vol) CO2 in DMEM (ThermoFisher Scientific; 11995) supplemented with 10% (vol/vol) FBS (Invitrogen; A13622DJ), 100 U/mL penicillin, 100 μg/mL streptomycin, 0.25 μg/mL amphotericin, and 2 mML-glutamine (Invitrogen). H1299 cells were cultured at 37C and 5% (vol/vol) CO2 in RPMI (ThermoFisher Scientific; 11875) supplemented with 10% (vol/vol) FBS (Invitrogen; A13622DJ), 100 U/mL penicillin, 100 μg/mL streptomycin, 0.25 μg/mL amphotericin, and 2 mML-glutamine (Invitrogen). Both cell lines tested negative for mycoplasma contamination.

### Transfection of Raf-1 constructs

H1299 cells were transfected with the mutant and wt Raf-1 constructs using Lipofectamine 3000 (ThermoFisher Scientific, L3000). Stable expression was selected using puromycin at a concentration of 1.5 μg/mL for 2 weeks.

### Reagents and antibodies

The following antibodies were purchased from Cell Signaling Technologies: anti-Phospho-p44/42 MAPK (Erk1/2) (Thr202/Tyr204) (E10) Mouse mAb #9106, anti-histone H3 (D1H2) XP Rabbit mAb #4499, anti-c-Raf Antibody #9422, anti-phospho-LRP6 (Ser1490) Antibody #2568, anti-GAPDH (D4C6R) Mouse mAb #97166. Anti-Beta-catenin mouse mAb was purchased from BD Transduction Laboratories (#610153) and anti-GAPDH rabbit antibody was purchased from Abcam (ab9485). The following fluorescent secondary antibodies were purchased from Fisher Scientific: IRDye 800CW Goat anti-Mouse IgG (926–32210) and IRDye 680LT Goat anti-Rabbit IgG (926-68021).

Recombinant human Wnt3A was purchased from Fisher Scientific (5036WN), and recombinant human EGF was purchased from Sigma (E9644). CHIR99021 was purchased from Sigma (SML1046). Halt Protease and Phosphatase Inhibitor Cocktail (100X) was purchased from Fisher Scientific (78440).

### CHIR99021 treatment

RKO cells were pre-treated with 1 μM CHIR99021 for 24 hr before adding replacement media containing 1 μM CHIR99021 and Wnt3A for 6 hr.

### Cell lysis

RKO cells at 70% confluency were scraped in PBS, pelleted, and snap-frozen, and then thawed in NP-40 lysis buffer containing Halt inhibitor cocktail. Samples were spun down, and the supernatants were transferred to Laemmli sample buffer and boiled. The samples were then run onto a Bolt 4–12% Bis-Tris Plus Gel (Thermofisher, NW04120BOX). H1299 cells at 70% confluence were scraped in NP-40 lysis buffer containing Halt inhibitor cocktail, and further lysed in Laemmli sample buffer. Samples were spun down, and the supernatants were boiled. The samples were then run onto a Novex 4–20% Tris-Glycine Mini Gel (ThermoFisher, XP04200BOX).

### Quantitative Western blots

Proteins were transferred onto nitrocellulose membranes, blocked for one hour at room temperature (RT) with blocking buffer (Odyssey Blocking Buffer (TBS) (927–50000) or 5% milk powder in TBS) and stained overnight at 4°C with primary antibody diluted in blocking buffer. The membranes were then stained with fluorescent IR secondary antibodies diluted in blocking buffer for one hour at RT. The fluorescent signal was then imaged using the LiCOR Odyssey Imager and quantified using Odyssey Application software version 3.0. The background-subtracted intensity of the protein bands were normalized to the loading control, GAPDH and/or Histone H3 (for RKO) or Histone H3 (for H1299). These values were then normalized to the reference lanes within each gel, to allow comparison across gels. For β-catenin and phospho-LRP5/6, variation in the fold-activation from experiment to experiment could artificially stretch the data along the x- and y-axis, and introduce artifacts into the relationship between phospho-LRP5/6 and β-catenin. Therefore, for Wnt3A dose responses, the data from each gel was scaled such that the mean of 80 ng/mL and 160 ng/mL samples was equal to the mean across all gels. Finally, for each antibody used in the study, we did careful characterization of the linear range, and verified that our measurement conditions were within the linear range of the antibody. Technical variability of Western blot quantitation. To confirm the effects reported, we verified that quantitation of the same sample loaded in multiple lanes in a gel gives CV < 10%, and quantitation of the same sample across multiple independent gels gives CV < 10% (Figure 3—figure supplement 7). As further control, we verified that normalization with loading control did not produce artificial distortion of the input-output relationship: linearity was observed without normalization in cases where loading was already uniform (Figure 3—figure supplement 8).

### L-1 and L2-norm analysis

L1-norm analysis was performed as described in Nevozhay et al. (2013). Briefly, the data is fitted with a cubic Hermite polynomial, and rescaled along the x and y axis to [0, 1]. The L1-norm is computed as the area between the polynomial fit and the diagonal. Linearity is defined in this context as L1-norm < 0.1. L2-norm analysis for Wnt pathway data was performed using a Pearson’s coefficient, and L2-norm analysis for ERK pathway data was performed using the coefficient of correlation, $r^{2}$.

### Akaike information criterion

To score the validity of nonlinear model fits for Figure 3D, we used the bias-corrected Akaike Information Criterion as described in ref. (Spiess and Neumeyer, 2010), which assesses goodness-of-fit and model parsimony. The weighted Aikaike $w(AIC)$ provides a comparison of all considered models, which in our case is the nonlinear ERK pathway model fit and a linear fit, with the higher score indicating a more valid model.

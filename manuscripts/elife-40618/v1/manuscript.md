# Measuring cis-regulatory energetics in living cells using allelic manifolds

## Authors

- Talitha L Forcier<sup>1</sup>
- Andalus Ayaz<sup>1</sup>
- Manraj S Gill<sup>1</sup>
- Daniel Jones<sup>1</sup>
- Rob Phillips<sup>2</sup> ([ORCID: 0000-0003-3082-2809](https://orcid.org/0000-0003-3082-2809))
- Justin B Kinney<sup>1</sup> ([ORCID: 0000-0003-1897-3778](https://orcid.org/0000-0003-1897-3778)) †

### Affiliations

1. Simons Center for Quantitative Biology Cold Spring Harbor Laboratory Cold Spring Harbor United States
2. Department of Applied Physics California Institute of Technology Pasadena United States

† Corresponding author

## Abstract

Gene expression in all organisms is controlled by cooperative interactions between DNA-bound transcription factors (TFs), but quantitatively measuring TF-DNA and TF-TF interactions remains difficult. Here we introduce a strategy for precisely measuring the Gibbs free energy of such interactions in living cells. This strategy centers on the measurement and modeling of ‘allelic manifolds’, a multidimensional generalization of the classical genetics concept of allelic series. Allelic manifolds are measured using reporter assays performed on strategically designed cis-regulatory sequences. Quantitative biophysical models are then fit to the resulting data. We used this strategy to study regulation by two Escherichia coli TFs, CRP and σ70 RNA polymerase. Doing so, we consistently obtained energetic measurements precise to ∼0.1 kcal/mol. We also obtained multiple results that deviate from the prior literature. Our strategy is compatible with massively parallel reporter assays in both prokaryotes and eukaryotes, and should therefore be highly scalable and broadly applicable.Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that minor issues remain unresolved (see decision letter).

## Introduction

Cells regulate the expression of their genes in response to biological and environmental cues. A major mechanism of gene regulation in all organisms is the binding of transcription factor (TF) proteins to cis-regulatory elements encoded within genomic DNA. DNA-bound TFs interact with one another, either directly or indirectly, forming cis-regulatory complexes that modulate the rate at which nearby genes are transcribed (Ptashne and Gann, 2002; Courey, 2008). Different arrangements of TF binding sites within cis-regulatory sequences can lead to different regulatory programs, but the rules that govern which arrangements lead to which regulatory programs remain largely unknown. Understanding these rules, which are often referred to as ‘cis-regulatory grammar’ (Spitz and Furlong, 2012), is a major challenge in modern biology.

Measuring the quantitative strength of interactions among DNA-bound TFs is critical for elucidating cis-regulatory grammar. In particular, knowing the Gibbs free energy of TF-DNA and TF-TF interactions is essential for building biophysical models that can quantitatively explain gene regulation in terms of simple protein-DNA and protein-protein interactions (Shea and Ackers, 1985; Bintu et al., 2005; Sherman and Cohen, 2012). Biophysical models have proven remarkably successful at quantitatively explaining regulation by a small number of well-studied cis-regulatory sequences. Arguably, the biggest successes have been achieved in the bacterium Escherichia coli, particularly in the context of the lac promoter (Vilar and Leibler, 2003; Kuhlman et al., 2007; Kinney et al., 2010; Garcia and Phillips, 2011; Brewster et al., 2014) and the O$_{R}$/O$_{L}$ control region of the $\lambda$ phage lysogen (Ackers et al., 1982; Shea and Ackers, 1985; Cui et al., 2013). But in both cases, this quantitative understanding has required decades of focused study. New approaches for dissecting cis-regulatory energetics, approaches that are both systematic and scalable, will be needed before a general quantitative understanding of cis-regulatory grammar can be developed.

Here we address this need by describing a systematic experimental/modeling strategy for dissecting the biophysical mechanisms of transcriptional regulation in living cells. Our strategy centers on the concept of an ‘allelic manifold’. Allelic manifolds generalize the classical genetics concept of allelic series to multiple dimensions. An allelic series is a set of sequence variants that affect the same phenotype (or phenotypes) but differ in their quantitative strength. Here we construct allelic manifolds by measuring, in multiple experimental contexts, the phenotypic strength of each variant in an allelic series. Each variant thus corresponds to a data point in a multi-dimensional ‘measurement space’. If the measurement space is of high enough dimension, and if one’s measurements are sufficiently precise, these data should collapse to a lower-dimension manifold that represents the inherent phenotypic dimensionality of the allelic series. These data can then be used to infer quantitative biophysical models that describe the shape of the allelic manifold, as well as the location of each allelic variant within that manifold. As we show here, such inference allows one to determine in vivo values for important biophysical quantities with remarkable precision.

We demonstrate this strategy on a regulatory paradigm in E. coli: activation of the $\sigma^{70}$ RNA polymerase holoenzyme (RNAP) by the cAMP receptor protein (CRP, also called CAP). CRP activates transcription when bound to DNA at positions upstream of RNAP (Busby and Ebright, 1999), and the strength of these interactions is known to depend strongly on the precise nucleotide spacing between CRP and RNAP binding sites (Gaston et al., 1990; Ushida and Aiba, 1990). However, the Gibbs free energies of these interactions are still largely unknown. To our knowledge, only the CRP-RNAP interaction at the lac promoter has previously been quantitatively measured (Kuhlman et al., 2007; Kinney et al., 2010). By measuring and modeling allelic manifolds, we systematically determined the in vivo Gibbs free energy ($Δ⁢G$) of CRP-RNAP interactions that occur at a variety of different binding site spacings. These $Δ⁢G$ values were consistently measured to an estimated precision of ~ 0.1 kcal/mol. We also obtained $Δ⁢G$ values for in vivo CRP-DNA and RNAP-DNA interactions, again with similar estimated precision.

The Results section that follows is organized into three Parts, each of which describes a different use for allelic manifolds. Part 1 focuses on measuring TF-DNA interactions, Part 2 focuses on TF-TF interactions, and Part 3 shows how to distinguish different possible mechanisms of transcriptional activation. Each Part consists of three subsections: Strategy, Demonstration, and Aside. Strategy covers the theoretical basis for the proposed use of allelic manifolds. Demonstration describes how we applied this strategy to better understand regulation by CRP and RNAP. Aside describes related findings that are interesting but somewhat tangential.

## Results

### Part 1. Strategy: Measuring TF-DNA interactions

We begin by showing how allelic manifolds can be used to measure the in vivo strength of TF binding to a specific DNA binding site. This measurement is accomplished by using the TF of interest as a transcriptional repressor. We place the TF binding site directly downstream of the RNAP binding site in a bacterial promoter so that the TF, when bound to DNA, sterically occludes the binding of RNAP. We then measure the rate of transcription from a few dozen variant RNAP binding sites. Transcription from each variant site is assayed in both the presence and in the absence of the TF.

Figure 1A illustrates a thermodynamic model (Shea and Ackers, 1985; Bintu et al., 2005; Sherman and Cohen, 2012) for this type of simple repression. In this model, promoter DNA can be in one of three states: unbound, bound by the TF, or bound by RNAP. Each of these three states is assumed to occur with a frequency that is consistent with thermal equilibrium, that is with a probability proportional to its Boltzmann weight.

![Figure 1.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig1-v1.jpg)

**Figure 1.:** (A) A thermodynamic model of simple repression. Here, promoter DNA can transition between three possible states: unbound, bound by a TF, or bound by RNAP. Each state has an associated Boltzmann weight and rate of transcript initiation. $F$ is the TF binding factor and $P$ is the RNAP binding factor; see text for a description of how these dimensionless binding factors relate to binding affinity and binding energy. $t_{sat}$ is the rate of specific transcript initiation from a promoter fully occupied by RNAP. (B) Transcription is measured in the presence ($t_{+}$) and absence ($t_{-}$) of the TF. Measurements are made for an allelic series of RNAP binding sites that differ in their binding strengths (blue-yellow gradient). (C) If the model in panel A is correct, plotting $t_{+}$ vs. $t_{-}$ for the promoters in panel B (colored dots) will trace out a 1D allelic manifold. Mathematically, this manifold reflects Equation 1 and Equation 2 computed over all possible values of the RNAP binding factor $P$ while the other parameters ($F$, $t_{sat}$) are held fixed. Note that these equations include a background transcription term $t_{bg}$; it is assumed throughout that $t_{bg}≪t_{sat}$ and that $t_{bg}$ is independent of RNAP binding site sequence. The resulting manifold exhibits five distinct regimes (circled numbers), corresponding to different ranges for the value of $P$ that allow the mathematical expressions in Equations 1 and 2 to be approximated by simplified expressions. In regime 3, for instance, $t_{+}≈t_{-}/(1+F)$, and thus the manifold approximately follows a line parallel (on a log-log plot) to the diagonal but offset below it by a factor of $1+F$ (dashed line). Data points in this regime can therefore be used to determine the value of $F$. (D) The five regimes of the allelic manifold, including approximate expressions for $t_{+}$ and $t_{-}$ in each regime, as well as the range of validity for $P$.

The energetics of protein-DNA binding determine the Boltzmann weight for each state. By convention we set the weight of the unbound state equal to 1. The weight of the TF-bound state is then given by $F=[TF]⁢K_{F}$ where $[TF]$ is the concentration of the TF and $K_{F}$ is the affinity constant in inverse molar units. Similarly, the weight of the RNAP-bound state is $P=[RNAP]⁢K_{P}$. In what follows we refer to $F$ and $P$ as the ‘binding factors’ of the TF-DNA and RNAP-DNA interactions, respectively. We note that these binding factors can also be written as $F=e^{-Δ⁢G_{F}/k_{B}⁢T}$ and $P=e^{-Δ⁢G_{P}/k_{B}⁢T}$ where $k_{B}$ is Boltzmann’s constant, $T$ is temperature, and $Δ⁢G_{F}$ and $Δ⁢G_{P}$ respectively denote the Gibbs free energy of binding for the TF and RNAP. Note that each Gibbs free energy accounts for the entropic cost of pulling each protein out of solution. In what follows, we report $Δ⁢G$ values in units of kcal/mol; note that 1 kcal/mol = $1.62⁢k_{B}⁢T$ at 37 °C.

The overall rate of transcription is computed by summing the amount of transcription produced by each state, weighting each state by the probability with which it occurs. In this case we assume the RNAP-bound state initiates at a rate of $t_{sat}$, and that the other states produce no transcripts. We also add a term, $t_{bg}$, to account for background transcription (e.g., from an unidentified promoter further upstream). The rate of transcription in the presence of the TF is thus given by 

$$
t_{+}=t_{sat}⁢\frac{P}{1+F+P}+t_{bg}.
$$

In the absence of the TF ($F=0$), the rate of transcription becomes 

$$
t_{-}=t_{sat}⁢\frac{P}{1+P}+t_{bg}.
$$

Our goal is to measure the TF-DNA binding factor $F$. To do this, we create a set of promoter sequences where the RNAP binding site is varied (thus generating an allelic series) but the TF binding site is kept fixed. We then measure transcription from these promoters in both the presence and absence of the TF, respectively denoting the resulting quantities by $t_{+}$ and $t_{-}$ (Figure 1B). Our rationale for doing this is that changing the RNAP binding site sequence should, according to our model, affect only the RNAP-DNA binding factor $P$. All of our measurements are therefore expected to lie along a one-dimensional allelic manifold residing within the two-dimensional space of ($t_{-}$, $t_{+}$) values. Moreover, this allelic manifold should follow the specific mathematical form implied by Equations 1 and 2 when $P$ is varied and the other parameters ($t_{sat}$, $t_{bg}$, $F$) are held fixed; see Figure 1C.

The geometry of this allelic manifold is nontrivial. Assuming $F≫1$ and $t_{bg}≪t_{sat}$, there are five different regimes corresponding to different values of the RNAP binding factor $P$. These regimes are listed in Figure 1D and derived in Appendix 4. In regime 1, $P$ is so small that both $t_{+}$ and $t_{-}$ are dominated by background transcription, that is $t_{+}≈t_{−}≈t_{bg}.$ $P$ is somewhat larger in regime 2, causing $t_{-}$ to be proportional to $P$ while $t_{+}$ remains dominated by background. In regime 3, both $t_{+}$ and $t_{-}$ are proportional to $P$ with $t_{+}/t_{-}≈1/(1+F)$. In regime 4, $t_{-}$ saturates at $t_{sat}$ while $t_{+}$ remains proportional to $P$. Regime five occurs when both $t_{+}$ and $t_{-}$ are saturated, that is $t_{+}≈t_{-}≈t_{sat}$.

### Part 1. Demonstration: Measuring CRP-DNA binding

The placement of CRP immediately downstream of RNAP is known to repress transcription (Morita et al., 1988). We therefore reasoned that placing a DNA binding site for CRP downstream of RNAP would allow us to measure the binding factor of that site. Figure 2 illustrates measurements of the allelic manifold used to characterize the strength of CRP binding to the 22 bp site GAATGTGACCTAGATCACATTT. This site contains the well-known consensus site, which comprises two palindromic pentamers (underlined) separated by a 6 bp spacer (Gunasekera et al., 1992). We performed measurements using this CRP site centered at two different locations relative to the transcription start site (TSS): +0.5 bp and +4.5 bp. Note that the first transcribed base is, in this paper, assigned position 0 instead of the more conventional +1, and half-integer positions indicate centering between neighboring nucleotides. To avoid influencing CRP binding strength, the −10 region of the RNAP site was kept fixed in the promoters we assayed while the −35 region of the RNAP binding site was varied (Figure 2A). Promoter DNA sequences are shown in Appendix 1—figure 1.

![Figure 2.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig2-v1.jpg)

**Figure 2.:** (A) Expression measurements were performed on promoters for which CRP represses transcription by occluding RNAP. Each promoter assayed contained a near-consensus CRP binding site centered at either +0.5 bp or +4.5 bp, as well as an RNAP binding site with a partially mutagenized −35 region (gradient). $t_{+}$ (or $t_{-}$) denotes measurements made using E. coli strain JK10 grown in the presence (or absence) of the small molecule cAMP. (B) Dots indicate measurements for 41 such promoters. A best-fit allelic manifold (black) was inferred from $n=39$ of these data points after the exclusion of 2 outliers (gray ‘X’s). Gray lines indicate 100 plausible allelic manifolds fit to bootstrap-resampled data points. The parameters of these manifolds were used to determine the CRP-DNA binding factor $F$ and thus the Gibbs free energy $Δ⁢G_{F}=-k_{B}⁢T⁢log⁡F$. Error bars indicate 68% confidence intervals determined by bootstrap resampling. See Appendix 3 for more information about our manifold fitting procedure.

We obtained $t_{-}$ and $t_{+}$ measurements for these constructs using a modified version of the colorimetric $\beta$-galactosidase assay of Lederberg (1950) and Miller (1972); see Appendix 2 for details. Our measurements are largely consistent with an allelic manifold having the expected mathematical form (Figure 2B). Moreover, the measurements for promoters with CRP sites at two different positions (+0.5 bp and +4.5 bp) appear consistent with each other, although the measurements for +4.5 bp promoters appear to have lower values for $P$ overall. A small number of data points do deviate substantially from this manifold, but the presence of such outliers is not surprising from a biological perspective (see Discussion). Fortunately, outliers appear at a rate small enough for us to identify them by inspection.

We quantitatively modeled the allelic manifold in Figure 2B by fitting $n+3$ parameters to our $2⁢n$ measurements, where $n=39$ is the number of non-outlier promoters. The $n+3$ parameters were $t_{sat}$, $t_{bg}$, $F$, and $P_{1}$, $P_{2}$, …, $P_{n}$, where each $P_{i}$ is the RNAP binding factor of promoter $i$. Nonlinear least squares optimization was used to infer values for these parameters. Uncertainties in $t_{sat}$, $t_{bg}$, and $F$ were quantified by repeating this procedure on bootstrap-resampled data points. See Appendix 3 for details.

These results yielded highly uncertain values for $t_{sat}$ because none of our measurements appear to fall within regime 4 or 5 of the allelic manifold. A reasonably precise value for $t_{bg}$ was obtained, but substantial scatter about our model predictions in regime 1 and 2 remain. This scatter likely reflects some variation in $t_{bg}$ from promoter to promoter, variation that is to be expected since the source of background transcription is not known and the appearance of even very weak promoters could lead to such fluctuations.

These data do, however, determine a highly precise value for the strength of CRP-DNA binding: $F=23.9_{-2.5}^{+3.1}$ or, equivalently, $Δ⁢G_{F}=-1.96\pm0.07$ kcal/mol. This allelic manifold approach is thus able to measure the strength of TF-DNA binding with a precision of ~ 0.1 kcal/mol. For comparison, the typical strength of a hydrogen bond in liquid water is −1.9 kcal/mol (Markovitch and Agmon, 2007).

We note that CRP forms approximately 38 hydrogen bonds with DNA when it binds to a consensus DNA site (Parkinson et al., 1996). Our result indicates that, in living cells, the enthalpy resulting from these and other interactions is almost exactly canceled by entropic factors. We also note that our in vivo value for $F$ is far smaller than expected from experiments in aqueous solution. The consensus CRP binding site has been measured in vitro to have an affinity constant of $K_{F}∼10^{11}⁢M^{-1}$ (Ebright et al., 1989). There are probably about 103 CRP dimers per cell (Schmidt et al., 2016), giving a concentration $[CRP]∼10^{−6} M$. Putting these numbers together gives a binding factor of $F∼10^{5}$. The nonspecific binding of CRP to genomic DNA and other molecules in the cell, and perhaps limited DNA accessibility as well, might be responsible for this ~ 105-fold disagreement with our in vivo measurements.

### Part 1. Aside: Measuring changes in the concentration of active CRP

Varying cAMP concentrations in growth media changes the in vivo concentration of active CRP in the E. coli strain we assayed (JK10). Such variation is therefore expected to alter the CRP-DNA binding factor $F$. We tested whether this was indeed the case by measuring multiple allelic manifolds, each using a different concentration of $[cAMP]$$[cAMP]$[cAMP] when measuring $t_{+}$. These measurements were performed on promoters with CRP binding sites at +0.5 bp (Figure 3A). The resulting data are shown in Figure 3B. To these data, we fit allelic manifolds having variable values for $F$, but fixed values for both $t_{bg}$ and $t_{sat}$ ($t_{bg}=2.30\times10^{-3}$ a.u. was inferred in the prior analysis for Figure 2B; $t_{sat}=15.1$ a.u. was inferred in the subsequent analysis for Figure 5C).

![Figure 3.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig3-v1.jpg)

**Figure 3.:** (A) Allelic manifolds were measured for the +0.5 bp occlusion promoter architecture using seven different concentrations of cAMP (ranging from 2.5 µM to 250 µM) when assaying $t_{+}$. (B) As expected, these data follow allelic manifolds that have cAMP-dependent values for the CRP binding factor $F$. (C) Values for $F$ inferred from the data in panel B exhibit a nontrivial power law dependence on [cAMP]. Error bars indicate 68% confidence intervals determined by bootstrap resampling.

This procedure allowed us to quantitatively measure changes in the RNAP binding factor $F$, and thus changes in the in vivo concentration of active CRP. Our results, shown in Figure 3C, suggest a nontrivial power law relationship between $F$ and [cAMP]. To quantify this relationship, we performed least squares regression ($log⁡F$ against $log⁡[cAMP]$) using data for the four largest cAMP concentrations; measurements of $F$ for the three other cAMP concentrations have large asymmetric uncertainties and were therefore excluded. We found that $F∝[cAMP]^{1.41\pm0.18}$, with error bars representing a 95% confidence interval. We emphasize, however that our data do not rule out a more complex relationship between [cAMP] and $F$.

There are multiple potential explanations for this deviation from proportionality. One possibility is cooperative binding of cAMP to the two binding sites within each CRP dimer. Such cooperativity could, for instance, result from allosteric effects like those described in Einav et al., 2018. Alternatively, this power law behavior might reflect unknown aspects of how cAMP is imported and exported from E. coli cells. It is worth comparing and contrasting this result to those reported in Kuhlman et al. (2007). JK10, the E. coli strain used in our experiments, is derived from strain TK310, which was developed in Kuhlman et al. (2007). In that work, the authors concluded that $F∝[cAMP]$, whereas our data leads us to reject this hypothesis. This illustrates one way in which using allelic manifolds to measure how in vivo TF concentrations vary with growth conditions can be useful.

### Part 2. Strategy: Measuring TF-RNAP interactions

Next we discuss how to measure an activating interaction between a DNA-bound TF and DNA-bound RNAP. A common mechanism of transcriptional activation is ‘stabilization’ (also called ‘recruitment’; see Ptashne, 2003). This occurs when a DNA-bound TF stabilizes the RNAP-DNA closed complex. Stabilization effectively increases the RNAP-DNA binding affinity $K_{P}$, and thus the binding factor $P$. It does not affect $t_{sat}$, the rate of transcript initiation from RNAP-DNA closed complexes.

A thermodynamic model for activation by stabilization is illustrated in Figure 4A. Here promoter DNA can be in four states: unbound, TF-bound, RNAP-bound, or doubly bound. In the doubly bound state, a ‘cooperativity factor’ $\alpha$ contributes to the Boltzmann weight. This cooperativity factor is related to the TF-RNAP Gibbs free energy of interaction, $Δ⁢G_{\alpha}$, via $\alpha=e^{-Δ⁢G_{\alpha}/k_{B}⁢T}$. Activation occurs when $\alpha>1$ (i.e., $ΔG_{\alpha}<0$). The resulting activated transcription rate is given by

![Figure 4.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig4-v1.jpg)

**Figure 4.:** (A) A thermodynamic model of simple activation. Here, promoter DNA can transition between four different states: unbound, bound by the TF, bound by RNAP, or doubly bound. As in Figure 1, $F$ is the TF binding factor, $P$ is the RNAP binding factor, and $t_{sat}$ is the rate of transcript initiation from an RNAP-saturated promoter. The cooperativity factor $\alpha$ quantifies the strength of the interaction between DNA-bound TF and RNAP molecules; see text for more information on this quantity. (B) As in Figure 1, expression is measured in the presence ($t_{+}$) and absence ($t_{-}$) of the TF for promoters that have an allelic series of RNAP binding sites (blue-yellow gradient). (C) If the model in panel A is correct, plotting $t_{+}$ vs. $t_{-}$ (colored dots) will reveal a 1D allelic manifold that corresponds to Equation 4 (for $t_{+}$) and Equation 2 (for $t_{-}$) evaluated over all possible values of $P$. Circled numbers indicate the five regimes of this manifold. In regime 3, $t_{+}≈\alpha^{′}⁢t_{-}$ where $\alpha^{′}$ is the renormalized cooperativity factor given in Equation 5; data in this regime can thus be used to measure $\alpha^{′}$. Separate measurements of $F$, using the strategy in Figure 1, then allow one to compute $\alpha$ from knowledge of $\alpha^{′}$. (D) The five regimes of the allelic manifold in panel C. Note that these regimes differ from those in Figure 1D.

$$
t_{+}=t_{sat}⁢\frac{P+\alpha⁢F⁢P}{1+F+P+\alpha⁢F⁢P}+t_{bg}.
$$

This can be rewritten as

$$
t_{+}=t_{sat}⁢\frac{\alpha^{′}⁢P}{1+\alpha^{′}⁢P}+t_{bg},
$$

where

$$
\alpha^{′}=\frac{1+\alpha⁢F}{1+F}
$$

is a renormalized cooperativity that accounts for the strength of TF-DNA binding. As before, $t_{-}$ is given by Equation 2. Note that $\alpha^{′}\leq\alpha$ and that $\alpha^{′}≈\alpha$ when $F≫1$ and $\alpha≫1/F$.

As before, we measure both $t_{+}$ and $t_{-}$ for an allelic series of RNAP binding sites (Figure 4B). These measurements will, according to our model, lie along an allelic manifold resembling the one shown in Figure 4C. This allelic manifold exhibits five distinct regimes (when $t_{sat}/t_{bg}≫\alpha^{′}≫1$), which are listed in Figure 4D.

### Part 2. Demonstration: Measuring class I CRP-RNAP interactions

CRP activates transcription at the lac promoter and at other promoters by binding to a 22 bp site centered at −61.5 bp relative to the TSS. This is an example of class I activation, which is mediated by an interaction between CRP and the C-terminal domain of one of the two RNAP $\alpha$ subunits (the $\alpha$CTDs) (Busby and Ebright, 1999). In vitro experiments have shown this class I CRP-RNAP interaction to activate transcription by stabilizing the RNAP-DNA closed complex.

We measured $t_{+}$ and $t_{-}$ for 47 variants of the lac* promoter (see Appendix 1—figure 1 for sequences). These promoters have the same CRP binding site assayed for Figure 2, but positioned at −61.5 bp relative to the TSS (Figure 5A). They differ from one another in the −10 or −35 regions of their RNAP binding sites. Figure 5B shows the resulting measurements. With the exception of 3 outlier points, these measurements appear consistent with stabilizing activation via a Gibbs free energy of $Δ⁢G_{\alpha}=-4.05\pm0.08$ kcal/mol, corresponding to a cooperativity of $\alpha=712_{-83}^{+102}$. We note that, with $F=23.9$ determined in Figure 2B, $\alpha^{′}=\alpha$ to 4% accuracy.

![Figure 5.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig5-v1.jpg)

**Figure 5.:** (A) $t_{+}$ and $t_{-}$ were measured for promoters containing a CRP binding site centered at −61.5 bp. The RNAP sites of these promoters were mutagenized in either their −10 or −35 regions (gradient), generating two allelic series. As in Figure 2, $t_{+}$ and $t_{-}$ correspond to expression measurements respectively made in the presence and absence of cAMP. (B) Data obtained for 47 variant promoters having the architecture shown in panel A. Three data points designated as outliers are indicated by ‘X’s. The allelic manifold that best fits the $n=44$ non-outlier points is shown in black; 100 plausible manifolds, estimated from bootstrap-resampled data points, are shown in gray. The resulting values for $\alpha$ and $Δ⁢G_{\alpha}=-k_{B}⁢T⁢log⁡\alpha$ are also shown, with 68% confidence intervals indicated. (C) Allelic manifolds obtained for promoters with CRP binding sites centered at a variety of class I positions. (D) Inferred values for the cooperativity factor $\alpha$ and corresponding Gibbs free energy $Δ⁢G_{\alpha}$ for the 12 different promoter architectures assayed in panel C. Error bars indicate 68% confidence intervals. Numerical values for $\alpha$ and $Δ⁢G_{\alpha}$ at all of these class I positions are provided in Table 1.

This observed cooperativity is substantially stronger than suggested by previous work. Early in vivo experiments suggested a much lower cooperativity value, for example 50-fold (Beckwith et al., 1972), 20-fold (Ushida and Aiba, 1990), or even 10-fold (Gaston et al., 1990). These previous studies, however, only measured the ratio $t_{+}/t_{-}$ for a specific choice of RNAP binding site. This ratio is (by Equation 4) always less than $\alpha$ and the differences between these quantities can be substantial. However, even studies that have used explicit biophysical modeling have determined lower cooperativity values: Kuhlman et al. (2007) reported a cooperativity of $\alpha≈240$ ($Δ⁢G_{\alpha}≈-3.4$ kcal/mol), while Kinney et al. (2010) reported $\alpha≈220$ ($Δ⁢G_{\alpha}≈-3.3$ kcal/mol). Both of these studies, however, relied on the inference of complex biophysical models with many parameters. The allelic manifold in Figure 4, by contrast, is characterized by only three parameters ($t_{sat}$, $t_{bg}$, $\alpha^{′}$), all of which can be approximately determined by visual inspection.

To test the generality of this approach, we measured allelic manifolds for 11 other potential class I promoter architectures. At every one of these positions we clearly observed the collapse of data to a 1D allelic manifold of the expected shape (Figure 5C). We then modeled these data using values of $\alpha$ and $t_{bg}$ that depend on CRP binding site location, as well as a single overall value for $t_{sat}$. The resulting values for $\alpha$ (and equivalently $Δ⁢G_{\alpha}$) are shown in Figure 5D and reported in Table 1. As first shown by Gaston et al. (1990) and Ushida and Aiba (1990), $\alpha$ depends strongly on the spacing between the CRP and RNAP binding sites. In particular, $\alpha$ exhibits a strong ~ 10.5 bp periodicity reflecting the helical twist of DNA. However, as with the measurement in Figure 5B, the $\alpha$ values we measure are far larger than the $t_{+}/t_{-}$ ratios previously reported by Gaston et al. (1990) and Ushida and Aiba (1990); see Table 1. We also find $t_{sat}=15.1_{-0.5}^{+0.6}$ a.u. The single-cell observations of So et al. (2011) suggest that this corresponds to $13.8\pm6.6$ transcripts per minute. By pure coincidence, the ‘arbitrary unit’ (a.u.) units we use in this paper correspond very closely to ‘transcripts per minute’.

### Part 2. Aside: Difficulties predicting binding affinity from DNA sequence

The measurement and modeling of allelic manifolds sidesteps the need to parametrically model how protein-DNA binding affinity depends on DNA sequence. In modeling the allelic manifolds in Figure 5C, we obtained values for the RNAP binding factor, $P=[RNAP]⁢K_{P}$, for each variant RNAP binding site from the position of the corresponding data point along the length of the manifold.

RNAP has a very well established sequence motif (McClure et al., 1983). Indeed, its DNA binding requirements were among the first characterized for any DNA-binding protein (Pribnow, 1975). More recently, a high-resolution model for RNAP-DNA binding energy was determined using data from a massively parallel reporter assay called Sort-Seq (Kinney et al., 2010). This position-specific affinity matrix (PSAM) assumes that the nucleotide at each position contributes additively to the overall binding energy (Figure 6A). This model is consistent with previously described RNAP binding motifs but, unlike those motifs, it can predict binding energy in physically meaningful energy units (i.e., kcal/mol). In what follows we denote these binding energies as $Δ⁢Δ⁢G_{P}$, because they describe differences in the Gibbs free energy of binding between two DNA sites.

![Figure 6.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig6-v1.jpg)

**Figure 6.:** (A) The PSAM for RNAP-DNA binding inferred by Kinney et al. (2010). This model assumes that the DNA base pair at each position in the RNAP binding site contributes independently to $Δ⁢G_{P}$. Shown are the $Δ⁢Δ⁢G_{P}$ values assigned by this model to mutations away from the lac* RNAP site. The sequence of the lac* RNAP site is indicated by gray vertical bars; see also Appendix 1—figure 1. A sequence logo representation for this PSAM is provided for reference. (B) PSAM predictions plotted against the values $ΔG_{P}=−k_{B}Tlog⁡P$ inferred by fitting the allelic manifolds in Figure 5C. Error bars on these measurements represent 68% confidence intervals. Note that measured $Δ⁢G_{P}$ values are absolute, whereas the $Δ⁢Δ⁢G_{P}$ predictions of the PSAM are relative to the lac* RNAP site, which thus corresponds to $Δ⁢Δ⁢G_{P}=0$ kcal/mol. The dashed line, provided for reference, has slope 1 and passes through this lac* data point.

There is good reason to believe this PSAM to be the most accurate current model of RNAP-DNA binding. However, subsequent work has suggested that the predictions of this model might still have substantial inaccuracies (Brewster et al., 2012). To investigate this possibility, we compared our measured values for the Gibbs free energy of RNAP-DNA binding ($Δ⁢G_{P}=-k_{B}⁢T⁢log⁡P$) to binding energies ($ΔΔG_{P}$) predicted using the PSAM from Kinney et al. (2010). These values are plotted against one another in Figure 6B. Although there is a strong correlation between the predictions of the model and our measurements, deviations of 1 kcal/mol or larger (corresponding to variations in $P$ of 5-fold or greater) are not uncommon. Model predictions also systematically deviate from the diagonal, suggesting inaccuracy in the overall scale of the PSAM.

This finding is sobering: even for one of the best understood DNA-binding proteins in biology, our best sequence-based predictions of in vivo protein-DNA binding affinity are still quite crude. When used in conjunction with thermodynamic models, as in Kinney et al. (2010), the inaccuracies of these models can have major effects on predicted transcription rates. The measurement and modeling of allelic manifolds sidesteps the need to parametrically model such binding energies, enabling the direct inference of Gibbs free energy values for each assayed RNAP binding site.

### Part 3. Strategy: Distinguishing mechanisms of transcriptional activation

E. coli TFs can regulate multiple different steps in the transcript initiation pathway (Lee et al., 2012; Browning and Busby, 2016). For example, instead of stabilizing RNAP binding to DNA, TFs can activate transcription by increasing the rate at which DNA-bound RNAP initiates transcription (Roy et al., 1998), a process we refer to as ‘acceleration’. CRP, in particular, has previously been reported to activate transcription in part by acceleration when positioned appropriately with respect to RNAP (Niu et al., 1996; Rhodius et al., 1997).

We investigated whether allelic manifolds might be used to distinguish activation by acceleration from activation by stabilization. First we generalized the thermodynamic model in Figure 4A to accommodate both $\alpha$-fold stabilization and $\beta$-fold acceleration (Figure 7A). This is accomplished by using the same set of states and Boltzmann weights as in the model for stabilization, but assigning a transcription rate $\beta⁢t_{sat}$ (rather than just $t_{sat}$) to the TF-RNAP-DNA ternary complex. The resulting activated rate of transcription is given by

![Figure 7.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig7-v1.jpg)

**Figure 7.:** (A) A TF can activate transcription in two ways: by stabilizing the RNAP-DNA complex or by accelerating the rate at which this complex initiates transcripts. (B) A thermodynamic model for the dual mechanism of transcriptional activation illustrated in panel A. Note that $\alpha$ multiplies the Boltzmann weight of the doubly bound complex, whereas $\beta$ multiplies the transcript initiation rate of this complex. (C) Data points measured as in Figure 4C will lie along a 1D allelic manifold having the form shown here. This manifold is computed using $t_{+}$ values from Equation 7 and $t_{-}$ values from Equation 2. Note that regime five occurs at a point positioned $\beta^{′}$-fold above the diagonal, where $\beta^{′}$ is related to $\beta$ through Equation 8. Measurements in or near the strong promoter regime ($P≳1$) can thus be used to determine the value of $\beta^{′}$ and, consequently, the value of $\beta$. (D) The five regimes of this allelic manifold are listed.

$$
t_{+}=t_{sat}⁢\frac{P}{1+F+P+\alpha⁢F⁢P}+\beta⁢t_{sat}⁢\frac{\alpha⁢F⁢P}{1+F+P+\alpha⁢F⁢P}+t_{bg}.
$$

This simplifies to

$$
t_{+}=\beta^{′}t_{sat}\frac{\alpha^{′}P}{1+\alpha^{′}P}+t_{bg},
$$

where $\alpha^{′}$ is the same as in Equation 5 and

$$
\beta^{′}=\frac{1+\alpha⁢\beta⁢F}{1+\alpha⁢F}
$$

is a renormalized version of the acceleration rate $\beta$. The resulting allelic manifold is illustrated in Figure 7C. Like the allelic manifold for stabilization, this manifold has up to five distinct regimes corresponding to different values of $P$ (Figure 7D). Unlike the stabilization manifold however, $t_{+}\neqt_{-}$ in the strong RNAP binding regime (regime 5); rather, $t_{+}≈\beta^{′}⁢t_{sat}$ while $t_{-}≈t_{sat}$.

### Part 3. Demonstration: Mechanisms of class I activation by CRP

We asked whether class I activation by CRP has an acceleration component. Previous in vitro work had suggested that the answer is ‘no’ (Malan et al., 1984; Busby and Ebright, 1999), but our allelic manifold approach allows us to address this question in vivo. We proceeded by assaying promoters containing variant alleles of the consensus RNAP binding site (Figure 8A). Note that the consensus RNAP site is 1 bp shorter than the lac* RNAP site (Appendix 1—figure 1, panel C versus panel B). We therefore positioned the CRP binding site at −60.5 bp in order to realize the same spacing between CRP and the −35 element of the RNAP binding site that was realized in −61.5 bp non-consensus promoters.

![Figure 8.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig8-v1.jpg)

**Figure 8.:** (A) $t_{+}$ and $t_{-}$ were measured for promoters containing variants of the consensus RNAP binding site as well as a CRP binding site centered at −60.5 bp. Because the consensus RNAP site is 1 bp shorter than the RNAP site of the lac* promoter, CRP at −60.5 bp here corresponds to CRP at −61.5 bp in Figure 5. (B) $n=18$ data points obtained for the constructs in panel A, overlaid on the measurements from Figure 5B (gray). The value $t_{sat}=15.1$ a.u., inferred for Figure 5C, is indicated by dashed lines. (C) Values for $\beta$ inferred using the data in Figure 5 for the 10 CRP positions that exhibited greater than 2-fold inducibility; $\beta$ values at the two other CRP positions (−66.5 bp and −76.5 bp) were highly uncertain and are not shown. Error bars indicate 68% confidence intervals.

The resulting data (Figure 8B) are seen to largely fall along the previously measured all-stabilization allelic manifold in Figure 5B. In particular, many of these data points lie at the intersection of this manifold with the $t_{+}=t_{-}$ diagonal. We thus find that $\beta≈1$ for CRP at −61.5 bp. To further quantify possible $\beta$ values, we fit the acceleration model in Figure 7 to each dataset shown in Figure 5B, assuming a fixed value of $t_{sat}=15.1$ a.u. The resulting inferred values for $\beta$, shown in Figure 8C, indicate little if any deviation from $\beta=1$. Our high-precision in vivo results therefore substantiate the previous in vitro results of Malan et al. (1984) regarding the mechanism of class I activation.

### Part 3. Aside: Surprises in class II regulation by CRP

Many E. coli TFs participate in what is referred to as class II activation (Browning and Busby, 2016). This type of activation occurs when the TF binds to a site that overlaps the −35 element (often completely replacing it) and interacts directly with the main body of RNAP. CRP is known to participate in class II activation at many promoters (Keseler et al., 2011; Salgado et al., 2013), including the galP1 promoter, where it binds to a site centered at position −41.5 bp (Adhya, 1996). In vitro studies have shown CRP to activate transcription at −41.5 bp relative to the TSS through a combination of stabilization and acceleration (Niu et al., 1996; Rhodius et al., 1997).

We sought to reproduce this finding in vivo by measuring allelic manifolds. We therefore placed a consensus CRP site at −41.5 bp, replacing much of the −35 element in the process, and partially mutated the −10 element of the RNAP binding site (Figure 9A). Surprisingly, we observed that the resulting allelic manifold saturates at the same $t_{sat}$ value shared by all class I promoters. Thus, CRP appears to activate transcription in vivo solely through stabilization, and not at all through acceleration, when located at −41.5 bp relative to the TSS (Figure 9B).

![Figure 9.](https://cdn.elifesciences.org/articles/40618/elife-40618-fig9-v1.jpg)

**Figure 9.:** (A) Regulation by CRP centered at −41.5 bp was assayed using an allelic series of RNAP binding sites that have variant −10 elements (gradient). (B) The observed allelic manifold plateaus at the value of $t_{sat}=15.1$ a.u. (dashed lines) determined for Figure 5B, thus indicating no detectable acceleration by CRP. This lack of acceleration is at odds with prior in vitro studies (Niu et al., 1996; Rhodius et al., 1997). (C) Regulation by CRP centered at −40.5 bp was assayed in an analogous manner. (D) Unexpectedly, data from the promoters in panel C do not collapse to a 1D allelic manifold. This finding falsifies the biophysical models in Figures 4A and 7B and indicates that CRP can either activate or repress transcription from this position, depending on as-yet-unidentified features of the RNAP binding site. Error bars in panel D indicate 95% confidence intervals estimated from replicate experiments.

**Table 1.**
 Summary of results for class I activation by CRP.The $\alpha$ and $Δ⁢G_{\alpha}$ values listed here correspond to the values plotted in Figure 5D. The corresponding value inferred for the saturated transcription rate is $t_{sat}=15.1_{-0.5}^{+0.6}$ a.u. Error bars indicate 68% confidence intervals; see Appendix 3 for details. $n$ is the number of data points used to infer these values, while ‘outliers’ is the number of data points excluded in this analysis. For comparison we show the fold-activation measurements (i.e., $t_{+}/t_{-}$) reported in Gaston et al. (1990) and Ushida and Aiba (1990); ‘-’ indicates that no measurement was reported for that position.


<table>
  <thead>
    <tr>
      <th>Position (bp)</th>
      <th>n</th>
      <th>Outliers</th>
      <th>Δ⁢Gα (kcal/mol)</th>
      <th>α</th>
      <th>t+/t- (Gaston)</th>
      <th>t+/t- (Ushida)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>−60.5</td>
      <td>21</td>
      <td>0</td>
      <td>-2.09±0.08</td>
      <td>29.6-3.5+4.7</td>
      <td>3.85</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−61.5</td>
      <td>44</td>
      <td>3</td>
      <td>-4.10±0.08</td>
      <td>763-84+113</td>
      <td>9.05</td>
      <td>20.6</td>
    </tr>
    <tr>
      <td>−62.5</td>
      <td>23</td>
      <td>0</td>
      <td>-2.43±0.11</td>
      <td>51.4-8.5+9.0</td>
      <td>4.22</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−63.5</td>
      <td>20</td>
      <td>1</td>
      <td>-0.88±0.05</td>
      <td>4.15-0.37+0.30</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−64.5</td>
      <td>17</td>
      <td>0</td>
      <td>-1.08±0.08</td>
      <td>5.80-0.67+0.89</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−65.5</td>
      <td>17</td>
      <td>0</td>
      <td>-0.48±0.03</td>
      <td>2.16-0.11+0.10</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−66.5</td>
      <td>19</td>
      <td>1</td>
      <td>0.00±0.04</td>
      <td>0.99-0.07+0.07</td>
      <td>0.78</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>−71.5</td>
      <td>35</td>
      <td>1</td>
      <td>-2.88±0.04</td>
      <td>105-7+7</td>
      <td>2.50</td>
      <td>16.4</td>
    </tr>
    <tr>
      <td>−72.5</td>
      <td>20</td>
      <td>0</td>
      <td>-2.73±0.04</td>
      <td>83.0-5.8+5.2</td>
      <td>3.49</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−76.5</td>
      <td>16</td>
      <td>0</td>
      <td>-0.15±0.04</td>
      <td>1.27-0.06+0.09</td>
      <td>0.54</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−81.5</td>
      <td>32</td>
      <td>0</td>
      <td>-1.53±0.03</td>
      <td>11.9-0.8+0.4</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>−82.5</td>
      <td>20</td>
      <td>0</td>
      <td>-1.82±0.05</td>
      <td>19.0-1.8+1.3</td>
      <td>-</td>
      <td>6.99</td>
    </tr>
  </tbody>
</table>

The genome-wide distribution of CRP binding sites suggests that CRP also participates in class II activation when centered at −40.5 bp (Keseler et al., 2011; Salgado et al., 2013). When assaying this promoter architecture, however, we obtained a 2D scatter of points that did not collapse to any discernible 1D allelic manifold (Figure 9D). Some of these promoters exhibit activation, some exhibit repression, and some exhibit no regulation by CRP.

These observations complicate the current understanding of class II regulation by CRP. Our in vivo measurements of CRP at −41.5 bp call into question the mechanism of activation previously discerned using in vitro techniques. The scatter observed when CRP is positioned at −40.5 bp suggests that, at this position, the −10 region of the RNAP binding site influences the values of at least two relevant biophysical parameters (not just $P$, as our model predicts). A potential explanation for both observations is that, because CRP and RNAP are so intimately positioned at class II promoters, even minor changes in their relative orientation caused by differences between in vivo and in vitro conditions or by changes in RNAP site sequence could have a major effect on CRP-RNAP interactions. Such sensitivity would not be expected to occur in class I activation, due to the flexibility with which the RNAP $\alpha$CTDs are tethered to the core complex of RNAP.

## Discussion

We have shown how the measurement and quantitative modeling of allelic manifolds can be used to dissect cis-regulatory biophysics in living cells. This approach was demonstrated in E. coli in the context of transcriptional regulation by two well-characterized TFs: RNAP and CRP. Here we summarize our primary findings. We then address some caveats and limitations of the work reported here. Finally, we elaborate on how future studies might be able to scale up this approach using massively parallel reporter assays (MPRAs), including for studies in eukaryotic systems.

### Summary

In each of our experiments, we quantitatively measured transcription from an allelic series of variant RNAP binding sites, each site embedded in a fixed promoter architecture. Two expression measurements were made for each variant promoter: $t_{+}$ was measured in the presence of the active form of CRP, while $t_{-}$ was measured in the absence of active CRP. This yielded a data point, $(t_{-},t_{+})$, in a two-dimensional measurement space. We had expected the data points thus obtained for each allelic series to collapse to a 1D curve (the allelic manifold), with different positions along this manifold corresponding to different values of RNAP-DNA binding affinity. Such collapse was indeed observed in all but one of the promoter architectures we studied. By fitting the parameters of quantitative biophysical models to these data, we obtained in vivo values for the Gibbs free energy ($Δ⁢G$) of a variety of TF-DNA and TF-TF interactions.

In Part 1, we showed how measuring allelic manifolds for promoters in which a DNA-bound TF occludes RNAP can allow one to precisely measure the $Δ⁢G$ of TF-DNA binding. We demonstrated this strategy on promoters where CRP occludes RNAP, thereby obtaining the $Δ⁢G$ for a CRP binding site that was used in subsequent experiments. As an aside, we demonstrated how performing such measurements in different concentrations of the small molecule cAMP allowed us to quantitatively measure in vivo changes in active CRP concentration.

In Part 2, we showed how allelic manifolds can be used to measure the $Δ⁢G$ of TF-RNAP interactions. We used this strategy to measure the stabilizing interactions by which CRP up-regulates transcription at a variety of class I promoter architectures. Our strategy consistently yielded $Δ⁢G$ values with an estimated precision of $∼0.1$ kcal/mol. As an aside, we showed how $Δ⁢G$ values for RNAP-DNA binding could also be obtained from these data. Notably, these $Δ⁢G$ measurements for RNAP-DNA binding were seen to deviate substantially from sequence-based predictions using an established position-specific affinity matrix (PSAM) for RNAP. This highlights just how difficult it can be to accurately predict TF-DNA binding affinity from DNA sequence.

In Part 3, we showed how allelic manifolds can allow one to distinguish between two potential mechanisms of transcriptional activation: ‘stabilization’ (a.k.a. ‘recruitment’) and ‘acceleration’. Applying this approach to the data from Part 2, we confirmed (as expected) that class I activation by CRP does indeed occur through stabilization and not acceleration. As an aside, we pursued this approach at two class II promoters. In contrast to prior in vitro studies (Niu et al., 1996; Rhodius et al., 1997), no acceleration was observed when CRP was positioned at −41.5 bp relative to the TSS. Even more unexpectedly, no 1D allelic manifold was observed at all when CRP was positioned at −40.5 bp. This last finding indicates that the variant RNAP binding sites we assayed control at least one functionally important biophysical quantity in addition to RNAP-DNA binding affinity.

### Caveats and limitations

An important caveat is that our $Δ⁢G$ measurements assume that the true transcription rates (of which we obtain only noisy measurements) exactly fall along a 1D allelic manifold of the hypothesized mathematical form. These assumptions are well-motivated by the data collapse that we observed for all except one promoter architecture. But for some promoter architectures, there were a small number of ‘outlier’ data points that we judged (by eye) to deviate substantially from the inferred allelic manifold. The presence of a few outliers makes sense biologically: the random mutations we introduced into variant RNAP binding sites will, with some nonzero probability, either shift the position of the RNAP site or create a new binding site for some other TF. However, even for promoters that exhibit clear clustering of 2D data around a 1D curve, the deviations of individual non-outlier data points from our inferred allelic manifold were often substantially larger than the experimental noise that we estimated from replicates. It may be that the biological cause of outliers is not qualitatively different from what causes these smaller but still detectable deviations from our assumed model.

The low-throughput experimental approach we pursued here also has important limitations. Each of the 448 variant promoters for which we report data was individually catalogued, sequenced, and assayed for both $t_{+}$ and $t_{-}$ in at least three replicate experiments. We opted to use a low-throughput colorimetric assay of $\beta$-galactosidase activity (Lederberg, 1950; Miller, 1972) because this approach is well established in E. coli to produce a quantitative measure of transcription with high precision and high dynamic range. Such assays have also been used by other groups to develop sophisticated biophysical models of transcriptional regulation (Kuhlman et al., 2007; Cui et al., 2013). However, this low-throughput approach has limited utility because it cannot be readily scaled up.

Our reliance on cAMP as a small molecule effector of CRP presents a second limitation. In our experiments, we controlled the in vivo activity of CRP by growing a specially designed strain of E. coli in either the presence (for $t_{+}$) or absence ($t_{-}$) of cAMP. This mirrors the strategy used by Kuhlman et al. (2007), and the validity of this approach is attested to by the calibration data shown in Appendix 2—figure 1. However, controlling in vivo TF activity using small molecules has many limitations. Most TFs cannot be quantitatively controlled with small molecules, and those that can often require special host strains (e.g., see Kuhlman et al., 2007). Moreover, varying the in vivo concentration of a TF can affect cellular physiology in ways that can confound quantitative measurements.

### Outlook

MPRAs performed on array-synthesized promoter libraries should be able to overcome both of these experimental limitations. Current MPRA technology is able to quantitatively measure gene expression for $≳$104 transcriptional regulatory sequences in parallel. We estimate that this would enable the simultaneous measurement of ~ 102 highly resolved allelic manifolds, each manifold representing a different promoter architecture. Moreover, by using array-synthesized promoters in conjunction with MPRAs, one can measure $t_{+}$ and $t_{-}$ by systematically altering the DNA sequence of TF binding sites, rather than relying on small molecule effectors of each TF. This capability would, among other things, enable biophysical studies of promoters that have multiple binding sites for the same TF; in such cases it might make sense to use measurement spaces having more than two dimensions.

Will allelic manifolds be useful for understanding transcriptional regulation in eukaryotes? Both Sort-Seq MPRAs (Sharon et al., 2012; Weingarten-Gabbay et al., 2017) and RNA-Seq MPRAs (Melnikov et al., 2012; Kwasnieski et al., 2012; Patwardhan et al., 2012) are well established in eukaryotes so, on a technical level, experiments analogous to those described here should be feasible. The bigger question, we believe, is whether the results of such experiments would be interpretable. Eukaryotic transcriptional regulation is far more complex than transcriptional regulation in bacteria. Still, we believe that pursuing the measurement and modeling of allelic manifolds in this context is worthwhile. Despite the underlying complexities, simple ‘effective’ biophysical models might work surprisingly well. Similar approaches might also be useful for studying other eukaryotic regulatory processes that are compatible with MPRAs, such as alternative splicing (Wong et al., 2018).

Based on these results, we advocate a very different approach to dissecting cis-regulatory grammar than has been pursued by other groups. Rather than attempting to identify a single quantitative model that can explain regulation by many different arrangements of TF binding sites (Gertz et al., 2009; Sharon et al., 2012; Mogno et al., 2013; Smith et al., 2013; Levo and Segal, 2014; White et al., 2016), we suggest focused studies of the biophysical interactions that result from specific TF binding site arrangements. The measurement and modeling of allelic manifolds provides a systematic and stereotyped way of doing this. By coupling this approach with MPRAs, it should be possible to perform such studies on hundreds of systematically varied regulatory sequence architectures in parallel. General rules governing cis-regulatory grammar might then be identified empirically. We suspect that this bottom-up strategy to studying cis-regulatory grammar is likely to reveal regulatory mechanisms that would be hard to anticipate in top-down studies.

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
      <td>Genetic reagent (E. coli)</td>
      <td>JK10</td>
      <td>this paper</td>
      <td>none</td>
      <td>genotype: ∆cyaA ∆cpdA ∆lacY ∆lacZ ∆dksA</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pJK47.419</td>
      <td>this paper</td>
      <td>none</td>
      <td>cloning vector with BsmBI cut sites, ccdB cassette, lacZ reporter gene, kanamycin resistance, pSC101 origin</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pJK48 and variants</td>
      <td>this paper</td>
      <td>none</td>
      <td>reporter plasmids cloned from pJK47.419</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>cAMP</td>
      <td>Sigma-Aldrich</td>
      <td>A9501-1G</td>
      <td>Adenosine 3’,5’-cyclic monophosphate, 1 gram</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>IPTG</td>
      <td>Sigma-Aldrich</td>
      <td>I5502-1G</td>
      <td>Isopropyl β-D-1- thiogalactopyranoside, 1 gram</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>ONPG</td>
      <td>Sigma-Aldrich</td>
      <td>N1127-5G</td>
      <td>2-Nitrophenyl β-D-galactopyranoside, 5 gram</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PureLink Genomic DNA Mini Kit</td>
      <td>ThermoFisher</td>
      <td>K182001</td>
      <td>none</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Nextera XT DNA Library Preparation Kit</td>
      <td>Illumina</td>
      <td>FC-131–1024</td>
      <td>24 samples</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>RDM</td>
      <td>Teknova</td>
      <td>M2105</td>
      <td>growth media: MOPS EZ Rich Defined Medium Kit, 5 liter</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PopCulture Reagent</td>
      <td>MilliporeSigma</td>
      <td>71092–4</td>
      <td>75 milliliters</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Breathe-Easier film</td>
      <td>USA Scientific</td>
      <td>9123–6100</td>
      <td>sterile, 100 per box</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Epoch 2 Microplate Spectrophotometer</td>
      <td>BioTek</td>
      <td>EPOCH2C</td>
      <td>none</td>
    </tr>
    <tr>
      <td>Software</td>
      <td>analysis scripts</td>
      <td>this paper</td>
      <td>none</td>
      <td>Available at https://github.com/jbkinney/17_inducibility (copy archived at https://github.com/elifesciences-publications/17_inducibility)</td>
    </tr>
  </tbody>
</table>

Appendix 1 describes the media, strains, plasmids, and promoters assayed in this work. Appendix 2 describes the colorimetric $\beta$-galactosidase activity assay, adapted from Lederberg (1950) and Miller (1972), that was used to measure expression levels. Appendix 3 provides details about how quantitative models were fit to these measurements, as well as how uncertainties in estimated parameters were computed. Supplementary file 1 is an Excel spreadsheet containing the DNA sequences of all assayed promoters, all $t_{+}$ and $t_{-}$ measurements used in this work, and all of the parameter values fit to these data, both with and without bootstrap resampling.

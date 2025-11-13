# Cellular compartmentalisation and receptor promiscuity as a strategy for accurate and robust inference of position during morphogenesis

## Authors

- Krishnan S Iyer<sup>1</sup> ([ORCID: 0000-0002-0930-5164](https://orcid.org/0000-0002-0930-5164))
- Chaitra Prabhakara<sup>2</sup>
- Satyajit Mayor<sup>2</sup> ([ORCID: 0000-0001-9842-6963](https://orcid.org/0000-0001-9842-6963)) †
- Madan Rao<sup>1</sup> ([ORCID: 0000-0001-6210-6386](https://orcid.org/0000-0001-6210-6386)) †

### Affiliations

1. Simons Center for the Study of Living Machines, National Center for Biological Sciences - TIFR Bangalore India ([ROR:03ht1xw27](https://ror.org/03ht1xw27))
2. National Center for Biological Sciences - TIFR Bangalore India ([ROR:03ht1xw27](https://ror.org/03ht1xw27))

† Corresponding author

## Abstract

Precise spatial patterning of cell fate during morphogenesis requires accurate inference of cellular position. In making such inferences from morphogen profiles, cells must contend with inherent stochasticity in morphogen production, transport, sensing and signalling. Motivated by the multitude of signalling mechanisms in various developmental contexts, we show how cells may utilise multiple tiers of processing (compartmentalisation) and parallel branches (multiple receptor types), together with feedback control, to bring about fidelity in morphogenetic decoding of their positions within a developing tissue. By simultaneously deploying specific and nonspecific receptors, cells achieve a more accurate and robust inference. We explore these ideas in the patterning of Drosophila melanogaster wing imaginal disc by Wingless morphogen signalling, where multiple endocytic pathways participate in decoding the morphogen gradient. The geometry of the inference landscape in the high dimensional space of parameters provides a measure for robustness and delineates stiff and sloppy directions. This distributed information processing at the scale of the cell highlights how local cell autonomous control facilitates global tissue scale design.

## Introduction

Precise positioning of cell fates and cell fate boundaries in a developing tissue is of vital importance in ensuring a correct developmental path (reviewed in Tkačik and Gregor, 2021; Wolpert, 2016). The required positional information is often conveyed by concentration gradients of secreted signalling molecules, or morphogens (reviewed in Tabata and Takei, 2004; Briscoe and Small, 2015). Typically, a spatially varying input morphogen profile is translated into developmentally meaningful transcriptional outputs. Morphogen profile measurements, across several signalling contexts, show that the gradients are inherently noisy Houchmandzadeh et al., 2002; Gregor et al., 2007a; Kicheva et al., 2007; Bollenbach et al., 2008; Zagorski et al., 2017. However, precision of the signalling output should be robust to inherent genetic or environmental fluctuations in the concentrations of the ligands and receptors engaged in translating the positional information. For example, the noisy profile of the morphogen Bicoid (Bcd) that activates hunchback (hb) in the early Drosophila embryo Gregor et al., 2007a; Gregor et al., 2007b , and the expression of gap genes that activate pair-rule genes Dubuis et al., 2013; Petkova et al., 2019 result in cell fate boundaries that are positioned to a remarkable accuracy of about one cell’s width. This points to a local, cell autonomous morphogenetic decoding that is precise and robust to various sources of noise Kerszberg and Wolpert, 2007; Kerszberg, 2004; Jaeger et al., 2004.

Cell autonomous decoding of noisy morphogen profiles includes reading of morphogen concentration, followed by cellular processing, finally leading to inference in the form of transcriptional readout. Several strategies have been proposed to ensure precision in output (reviewed in Barkai and Shilo, 2009; Lander et al., 2009): feedbacks such as self-enhanced morphogen degradation Eldar et al., 2002; Eldar et al., 2003, spatial and temporal averaging Gregor et al., 2007a, use of two opposing gradients McHale et al., 2006, pre-steady state patterning Bergmann et al., 2007 and serial transcytosis Bollenbach et al., 2007.

Most cell signalling systems have regulatory mechanisms that fine-tune signalling by controlling ligand-specific receptor interactions Rogers and Schier, 2011. Ligands such as TGF $\beta$/BMP Mueller and Nickel, 2012, Jiang and Cong, 2016, D’Souza et al., 2008, show promiscuous interactions with different receptors. Chen and Schier, 2002; Sick et al., 2006 or sequestering components within the extracellular matrix Marjoram and Wright, 2011 or interactions with binding receptors such as heparin sulphate proteoglycans (HSPGs) Baeg et al., 2001; Baeg et al., 2004; Yan and Lin, 2009 can control availability of the ligand. Additionally, the multiple endocytic pathways that operate at the plasma membrane can control the extent of signalling Bökel and Brand, 2014; Di Fiore and von Zastrow, 2014. These examples argue for distributed information processing within the cell.

In this paper, we show how cellular compartmentalisation, a defining feature of multicellularity, provides a compelling realisation of such distributed cellular inference. We show that compartmentalisation together with multiple receptors, receptor promiscuity and feedback control, ensure precision and robustness in positional inference from noisy morphogen profiles during development. Compartments associated with specific chemical (e.g. lipids, proteins/enzymes) and physical (e.g. pH) environments, have been invoked as regulators of biochemical reactions during cellular signalling and development Ellisdon and Halls, 2016; Omerovic et al., 2007; Omerovic and Prior, 2009; Shilo and Schejter, 2011; Bökel and Brand, 2014. Deploying promiscuous receptors against a morphogen, in addition to its specific receptor, is a strategy to buffer variations in morphogen levels. These observations provide the motivation for a general conceptual framework for morphogenetic decoding based on a multi-tiered, multi-branched information channel. While our framework has broader applicability, we will, for clarity, use the terminology of Wingless signalling in Drosophila wing imaginal disc Hemalatha et al., 2016.

### Conceptual framework and quantitative models

We pose the task of morphogenetic decoding as a problem in local, cell autonomous inference of position from a morphogen input (Figure 1), where each cell acts as an information/inference channel with the following information flow:

![Figure 1.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig1-v1.jpg)

**Figure 1.:** (a) A morphogen is produced by a specific set of cells (blue), and secreted into the lumen surrounding the tissue. Due to stochasticity of the production and transport processes, the morphogen concentration received by the rest of the cells is contaminated by extrinsic noise, which defines a distribution of morphogen concentration along the $y$-direction at any position $x$. (b) The route from morphogens to a developmental outcome requires each cell to read, process and infer its position. This task is further complicated by the stochasticity of the reading and processing steps themselves, that lead to intrinsic noise. (c) The problem of robust inference of position can be considered in a channel framework. The positional information is noisily encoded in the local morphogen (ligand) concentrations, $p⁢(L|x)$. The cells receive this as input and process it into a less noisy output to ensure robustness in inferred positions.

At a phenomenological level, reading of the morphogen input is associated with the binding of the morphogen ligand to various receptors with varying degree of specificity, leading to the notion that the information channel describing positional inference must possess multiple branches. Furthermore, the multiple processing steps associated with compartmentalisation of cellular biochemistry and/or signal transduction modules, for example phosphorylation states, provide the motivation for invoking multiple tiers in the channel architecture. At an abstract level, one may think of the branch-tier architecture of the cellular processing as a bipartite Markovian network/graph Hartich et al., 2014, with a fast direction (involving multiple branches) consisting of ligand-bound and unbound states along with chemical state changes, and a slower direction (involving multiple tiers) consisting of intracellular transport, fission and fusion, characterised by energy-utilising processes or a flux imbalance. A general developmental context with multiple morphogens may involve several such bipartite Markov networks/graphs with different receptors (or branches) in parallel. Some of these receptors could be shared between different morphogens. We refer to signalling receptors as those which transduce a signal upon binding to their specific morphogen ligand and non-signalling receptors as those that participate in the signalling pathway without directly eliciting a signalling response. At the end of processing, each individual cell may pool information from the various branches for the final inference of position, i.e. a transcriptional readout (Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig2-v1.jpg)

**Figure 2.:** Branches correspond to different receptor types and tiers denote the layers of compartmentalisation used in cellular processing. Cellular processing associated with each receptor type (here, branches 1 and 2) is depicted by a generic Markov network. The gray and brown planes depict the tiers in the two branches respectively (here, tiers 1, 2, and 3 in each branch). The bi-directional in-plane purple arrows correspond to faster transitions between receptor states, e.g. bound/unbound, and the green bi-directional arrows depict slower transitions involving intracellular transport driven by flux-imbalanced processes. There may exist several feedback control loops (red ━┥ arrows) in the network. Ligand concentration $L$ drives one or several reaction rates in such Markov networks as in Harvey et al., 2020. The output $\theta$ is a collection $f$ of several signalling states (purple nodes) from one or many branches. The statistics of the output $\theta$ then enables inference of position.

The task of achieving a precise inference is complicated by the noise in morphogen input arising from both production and transport processes, and by the stochasticity of the reading and processing steps; thus the inference must be robust to the extrinsic and intrinsic sources of noise. The use of feedback control mechanisms is a common strategy to bring about robustness in the context of morphogen gradient formation and sensing Averbukh et al., 2017. Motivated by this, in Section ‘Quantitative models for cellular reading and processing’ we consider different feedback controls in conjunction with the tiers and branches. With these three elements to the channel architecture, the task of morphogenetic decoding can be summarised in the following objective.

<table>
  <tbody>
    <tr>
      <td>Objective:</td>
    </tr>
    <tr>
      <td>Given a noisy ligand input distribution at position x, i.e. p⁢(L|x), what are the requirements on the reading (number of receptor types and receptor concentrations) and processing steps (number of tiers and feedback type) such that the positional inference is precise and robust to extrinsic and intrinsic noise?</td>
    </tr>
  </tbody>
</table>

### Mathematical framework

Figure 1 describes information processing during development across a two dimensional tissue of nx, ny cells in $x$ and $y$ directions, respectively. The direction of morphogen gradient is taken to be along $x$, with the morphogen source to the left of $x=0$. Each cell is endowed with a chemical reaction network (CRN) with the same multi-tiered, multi-branched architecture with feedbacks described previously, that reads a noisy input $L⁢(x,y)$ (morphogen concentration) and produces an ‘output’ (biochemical ‘signal’) $\theta⁢(x,y)$ that is also noisy. Here, we choose to construct the noisy morphogen profile in the following manner: for a given position $x\in[0,1]$, cells along the $y$-direction see different amounts of ligand coming from the same input distribution$p⁢(L|x)$,

$$
p(L|x)=\frac{2}{\sqrt{2\pi\sigma_{L}^{2}(x)}}Exp[−\frac{(L−\mu_{L}(x))^{2}}{2\sigma_{L}^{2}(x)}](1+Erf[\frac{\mu_{L}(x)}{\sqrt{2}\sigma_{L}(x)}])^{−1}.
$$

characterised parametrically by a mean $\mu_{L}⁢(x)$ and standard deviation $\sigma_{L}⁢(x)$. Experimental data can be fit to this distribution Equation 1 (or another distribution suitable for the specific experimental system) to obtain the parameters. Here, we consider an exponentially decaying mean $\mu_{L}$ and standard deviation $\sigma_{L}$.

$$
\mu_{L}(x)=Ae^{−x/\lambda}
$$



$$
\sigma_{L}(x)=\sqrt{\mu_{L}(x)}
$$

Alternatively, one could choose a different parametrisation consistent with experimental observations for a morphogen profile with a monotonically decaying mean. The values of $A,\lambda$ chosen for our analysis are listed in Table 1. The corresponding output distribution $p⁢(\theta|x)$ can be used to infer the cell’s position. Since we do not know the precise functional relationship between the output and inferred position, we invoke Bayes rule MacKay and Mac Kay, 2003, as in previous work Tkačik et al., 2015, to infer the cell’s position,

$$
p(x|\theta)=\frac{p(\theta|x)p(x)}{p(\theta)}
$$

where $p⁢(\theta)=\int_{0}^{1}dx⁢p⁢(\theta|x)⁢p⁢(x)$ and $p⁢(x)$ is the prior distribution which we take to be uniform over a tissue of unit length, $p⁢(x)=1$. We quantify precision in the inference by the local inference error, $\sigma_{X}⁢(x)$. For each position $x$, the inferred position $x^{∗}$ of cells along the $y$-direction is taken to be the maximum a posteriori estimate,

$$
x^{∗}(x,y)=argmaxx~p(x~|\theta(x,y))
$$

where we use $x~$ to differentiate from the true position $x$. From this, the local and average inference error can be computed.

$$
\sigma_{X}^{2}(x)=⟨(x^{∗}−x)^{2}⟩_{y}
$$



$$
\sigma¯_{X}=\int_{0}^{1}\sigma_{X}(x)p(x)dx
$$

where the average in Equation 6 is over cells in the $y$-direction. The logic behind this definition of the inference error is that development of the tissue relies on the precision in the inference of cells’ positions throughout the tissue. However, there may be tissue developmental contexts, where only the positions of certain regions or cell fate boundaries need to be specified with any precision (as in the case of short-range morphogen gradients like Nodal Liu et al., 2022). The definition of inference error may be readily extended to incorporate such specifications (see Section ‘Choice of objective function’).

**Table 1.**
 Parameters associated with rates, feedback and receptor profiles along with their range of values.The chemical rate values used in numerical analysis are scaled by the unbinding rate $r_{u},κ_{u}$ taken to be 1. The corresponding experimental values have been taken from Lauffenburger and Linderman, 1996 where available.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Numerical values</th>
      <th>Experimental values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chemical rates</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Signalling branch</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Unbinding rate</td>
      <td>ru</td>
      <td>1</td>
      <td>0.34 min-1</td>
    </tr>
    <tr>
      <td>Binding rate</td>
      <td>rb</td>
      <td>0.1–1 nM-1</td>
      <td>0.072 nM-1⁢min-1</td>
    </tr>
    <tr>
      <td>Degradation rate</td>
      <td>rd</td>
      <td>0.001–0.01</td>
      <td>0.0022 min-1</td>
    </tr>
    <tr>
      <td>Internalisation rate</td>
      <td>rI</td>
      <td>0.1–1</td>
      <td>0.03–0.3 min-1</td>
    </tr>
    <tr>
      <td>Recycling rate</td>
      <td>rR</td>
      <td>0.1–1</td>
      <td>0.058 min-1</td>
    </tr>
    <tr>
      <td>Non-signalling branch</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Unbinding rate</td>
      <td>κu</td>
      <td>1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Binding rate</td>
      <td>κb</td>
      <td>0.1–1 nM-1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Degradation rate</td>
      <td>κd</td>
      <td>0.001–0.01</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Internalisation rate</td>
      <td>κI</td>
      <td>0.1–1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Recycling rate</td>
      <td>κR</td>
      <td>0.1–1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Conjugation rate</td>
      <td>κC</td>
      <td>0.1–1 nM-1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Splitting rate</td>
      <td>κS</td>
      <td>0.1–1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Feedback control</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Amplification</td>
      <td>α</td>
      <td>0.1-10</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Feedback Sensitivity</td>
      <td>γ</td>
      <td>0-1 nM-1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Feedback strength</td>
      <td>n</td>
      <td>0-5</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Receptor control</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Signalling receptors</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hill coefficient</td>
      <td>a</td>
      <td>0-5</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Minimum concentration</td>
      <td>A0</td>
      <td>50-250 nM</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Maximum concentration</td>
      <td>A0+A1</td>
      <td>50-500 nM</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Position of half-maximum</td>
      <td>A2</td>
      <td>0.01-1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Non-signalling receptors</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hill coefficient</td>
      <td>b</td>
      <td>0-5</td>
      <td></td>
    </tr>
    <tr>
      <td>Minimum concentration</td>
      <td>B0</td>
      <td>50-250 nM</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Maximum concentration</td>
      <td>B0+B1</td>
      <td>50-500 nM</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Position of half-maximum</td>
      <td>B2</td>
      <td>0.01-1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Ligand input</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Maximum concentration</td>
      <td>A</td>
      <td>30 nM</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Decay length</td>
      <td>λ</td>
      <td>0.2-0.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Number of cells along x-direction</td>
      <td>nx</td>
      <td>101</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Number of cells along y-direction</td>
      <td>ny</td>
      <td>101</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

We have been motivated to use the maximum a posteriori (MAP) estimate in Equation 5 by its successful use in previous studies in Drosophila embryo Dubuis et al., 2013; Petkova et al., 2019; Tkačik et al., 2015 and, more importantly, that it is a local estimate not requiring the computation of $p(\theta)$ (which is independent of $x$). We have checked that a different definition of the inference error, which does not use the MAP estimate and takes into account the entire distribution $p(x^{∗}|x)$,

$$
\sigma_{x}^{2}(x)=\int_{0}^{1}dx(x^{∗}−x)^{2}p(x^{∗}|x)
$$

leads to the same qualitative results.

### Quantitative models for cellular reading and processing

In order to calculate the probability of the inferred position given the output $p⁢(x^{∗}|\theta)$ and hence the inference error $\sigma¯_{X}$, one needs to know the prior $p⁢(x)$ and the input-output relation giving rise to the output distribution $p⁢(\theta|x)$ in Equation 4. While a uniform prior may be justified by a homogeneous distribution of cells in the developing tissue at the stage considered, the input-output relation needs to be developed using a specific model based on the general channel design principles described previously. Thus, we will take each cell to be equipped with a chemical reaction network (CRN) that has up to two receptor types both of which bind the ligand on the cell surface but only one is signalling competent Hemalatha et al., 2016; Tabata and Takei, 2004. This latter aspect breaks the symmetry between the receptor types and hence the branches, a point that we will revisit in Section ‘Asymmetry in branched architecture: promiscuity of non-signalling receptors’. In multi-tier architectures, the bound states of both the receptors are internalised and shuttled through several compartments. The last compartment allows for a conjugation reaction between the two receptors (as in the case of Wingless and Dpp Hemalatha et al., 2016; Zhu et al., 2020). The signalling states, defined by all the bound states of the signalling receptor, contribute to the output. Within this schema, we consider control mechanisms on the surface receptor concentrations and in the chemical reactions downstream to binding on the surface (i.e. on internalisation, shuttling, conjugation, etc). We formulate the control on processing steps as a feedback/feedforward regulation from one of the signalling species in the CRN. On the other hand, the control of surface receptors is considered in the form of an open-loop control by allowing receptor profiles to vary within certain bounds, as described below. The key parameters are chemical rate parameters describing the rates of various reactions in the CRN, receptor parameters describing the receptor concentration profiles, feedback topology in the CRN that is a combination of actuator and rate under regulation, control parameters describing the strength and sensitivity of the feedback/feedforward. With these parameters specified, an input-output relation, calculated as a tier-wise weighted sum of all signalling states, can then be used to infer the cell’s position by Equation 4.

#### Cellular Reading via surface receptors

In the framework described previously, we consider the morphogen ligand as an external input to the receiving cells, outside the cellular information processing channel. The signal and noise of this external input are captured by the distribution Equation 1. This implicitly assumes that there is no feedback control from the output to the ligand input, that is no ‘sculpting’ of the morphogen ligand profile. We revisit this point in the Discussion. Given a distribution of the morphogen input, we address the local, cell autonomous morphogenetic decoding that allows the cells to tune their reading dynamically.

We subject the local, cellular reading to an open-loop control on total (ligand bound plus unbound) surface availability of the signalling $ψ$ and non-signalling $ϕ$ receptors. This implies that for each evaluation of inference error within the optimisation routine (see Section ‘Performance of the Channel Architectures’), the local surface receptor levels are held constant in time through a chemostat (see Appendix 1). In our analysis, we consider a family of monotonic (increasing or decreasing in $x$ and independent of $y$) receptor profiles, which for convenience we take to be of the Hill form (Figure 3), that is either

$$
Monotonically increasing in x:f_{A}(x)=A_{0}+\frac{A_{1}x^{a}}{A_{2}^{a}+x^{a}}or
$$



$$
Monotonically decreasing in x:f_{B}(x)=B_{0}+\frac{B_{1}}{1+(x/B_{2})^{b}}
$$

The range of values for these parameters considered in the numerical analysis are listed in Table 1. Therefore, when considering $ψ⁢(x)$ to be monotonically increasing in $x$, we parametrise it with $f_{A}$. It follows that in a one-branch channel, there are two possibilities: $ψ\in{f_{A},f_{B}}$ while in a two-branch channel, there are a total of four possibilities: $(ψ,ϕ)\in{f_{A},f_{B}}\times{f_{A},f_{B}}$. This allows us to simulate the ‘reading’ step performed by the cells (see Figure 1b).

![Figure 3.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig3-v1.jpg)

**Figure 3.:** Family of receptor profiles $f_{A}$ (monotonically increasing in $x$) and $f_{B}$ (monotonically decreasing in $x$) with an interpretation of function parameters (Equations 8; 9).The total surface concentrations of both signalling and non-signalling receptors are taken from these families of receptor profiles.

Note that we are not fixing a receptor profile but taking it from a class of monotonic profiles (including a uniform profile), over which we vary to determine the optimal inference (see Section ‘Performance of the Channel Architectures’ below). Further, in the optimisation scheme (Section ‘Performance of the Channel Architectures’), we allow the receptor concentrations to vary over the space of all monotonically increasing, decreasing or flat profiles, and do not encode the positional information in the receptor profiles. Monotonicity implicitly assumes a spatial correlation in the receptor concentrations across cells – we return to this point in the Discussion.

#### Dynamics of processing in a single-tier channel

In a single tier channel, all processing is restricted to the cell surface. We represent the bound state of the signalling receptor as $R^{(1)}$ and that of the non-signalling receptor as $S^{(1)}$. The conjugated state is represented by $Q^{(1)}$. The CRN for such a system with one and two branches is shown in Figure 4a. Rates associated with these reactions are listed in Table 1. The differential equations that describe the binding, unbinding, conjugation, splitting and degradation reactions of the receptors are given by

$$
∂_{t}R^{(1)}=r_{b}L(ψ(x)−R^{(1)})−(r_{u}+r_{d})R^{(1)}−κ_{C}R^{(1)}S^{(1)}+κ_{S}Q^{(1)}
$$



$$
∂_{t}S^{(1)}=κ_{b}L(ϕ(x)−S^{(1)})−(κ_{u}+κ_{d})S^{(1)}−κ_{C}R^{(1)}S^{(1)}+κ_{S}Q^{(1)}
$$



$$
∂_{t}Q^{(1)}=κ_{C}R^{(1)}S^{(1)}−κ_{S}Q^{(1)}
$$

The steady-state output $\theta$, defined as the sum of all the ligand-bound signalling states, is given by $\theta=R^{(1)}+Q^{(1)}$. Note that to describe the 1-branch system, we simply set all rates $κ$ to zero.

![Figure 4.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig4-v1.jpg)

**Figure 4.:** Signalling receptors in the bound state (colour purple) from each of the tiers contribute to the cellular output. The interpretation of the arrows is shown in the legend.

#### Dynamics of processing in a multi-tier channel

In a multi-tiered channel, the receptors go through additional steps of processing before generating an output. We represent the bound state of a receptor in $k$-th tier of the first branch as $R^{(k)}$, that of the second branch as $S^{(k)}$, and the conjugate species that forms in the last $n_{T}$-th tier as $Q^{(n_{T})}$. The CRN for such a system with $n_{T}$ tiers is shown in Figure 4b. Rates associated with these reactions are listed in Table 1. The differential equations that describe the binding, unbinding, trafficking, recycling, conjugation, splitting and degradation reactions of the receptors are given by

$$
∂_{t}R^{(1)}=r_{b}L(ψ(x)−R^{(1)})−(r_{u}+r_{d}+r_{I})R^{(1)}+r_{R}R^{(2)}
$$



$$
∂_{t}S^{(1)}=κ_{b}L(ϕ(x)−S^{(1)})−(κ_{u}+κ_{d}+κ_{I})S^{(1)}+κ_{R}S^{(2)}
$$



$$
∂_{t}R^{(n_{T})}=r_{I}R^{(n_{T}−1)}−(r_{R}+r_{d})R^{(n_{T})}−κ_{C}R^{(n_{T})}S^{(n_{T})}+κ_{S}Q^{(n_{T})}
$$



$$
∂_{t}S^{(n_{T})}=κ_{I}S^{(n_{T}−1)}−(κ_{R}+κ_{d})S^{(n_{T})}−κ_{C}R^{(n_{T})}S^{(n_{T})}+κ_{S}Q^{(n_{T})}
$$



$$
∂_{t}Q^{(n_{T})}=κ_{C}R^{(n_{T})}S^{(n_{T})}−κ_{S}Q^{(n_{T})}
$$

The output, realised from all the ligand-bound signalling states, now becomes $\theta=w_{n_{T}}⁢Q^{(n_{T})}+\sum_{k=1}^{n_{T}}w_{k}⁢R^{(k)}$ at steady state with wk, such that $\sum_{k}w_{k}=1$, representing the weight allotted to the tier (according to the mean residence time in the tier, for instance). For details regarding the setup of Equations 10–17 refer to Appendix 1. These differential equations for single-tiered and multi-tiered systems are to be augmented by stochastic contributions from both extrinsic and intrinsic sources. Extrinsic noise is a consequence of stochasticity of the ligand concentration presented to the cell, $L∼p⁢(L|x)$, and enters the equations as a source term. On the other hand, intrinsic noise is a consequence of copy-number fluctuations in the CRNs that characterise the channel, and are treated using chemical master equations (CMEs) Sengupta, 2008.

#### Feedback Control

We consider all rates in the CRN, except the ligand binding and unbinding rates, as potentially under feedback regulation. Any chemical rate $r\in{r_{I},κ_{I},κ_{C},….}$ that is under feedback control actuated by the node $R\in{R^{(1)},S^{(1)},….}$ is modelled as.

$$
r_{+}=r_{0}(1+\frac{\alphaR^{n}}{\gamma^{−n}+R^{n}})if under positive feedback
$$



$$
r_{−}=\frac{r_{0}}{1+(\gammaR)^{n}}if under negative feedback
$$

with r0 as the reference value of the chemical rate in the absence of feedback. The range of values for amplification $\alpha$, feedback sensitivity $\gamma$ and feedback strength $n$ are listed in Table 1. Figure 5 shows the different categories of possible feedback controls. We discuss the heuristics underlying the feedback controls in Appendix 2.

![Figure 5.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig5-v1.jpg)

**Figure 5.:** (A) In a one-branch channel, feedbacks are considered on internalisation rates or degradation rates. (B) A second branch in the channel opens up the possibilities of (a) intra-branch and (b) inter-branch, (i) intra-tier and (ii) inter-tier feedbacks.

### Performance of the channel architectures

With the model in place, we address the Objective discussed previously, by studying the performance of different channel architectures, i.e. number of tiers and branches, and feedback topology. We define a vector $v→$ belonging to a parameter space $V$ of the channel parameters related to chemical rates, receptor profiles and feedback (see Table 1). While the chemical rates and feedback parameters are the same in all cells, the receptor profile parameters help define the receptor concentrations at each cell position $x,y$. For a given morphogen input distribution $p⁢(L|x)$ and a channel architecture under consideration, the optimisation can be stated as

$$
\sigma¯_{X}^{opt}=minv→\inV\sigma¯_{X}(v→;p(L|x))
$$

and implemented by the following algorithm, the details of which are presented in Appendix 3.

<table>
  <thead>
    <tr>
      <th>Optimisation scheme</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fix a morphogen input distribution for each position, p⁢(L|x) using Equation 1.Define the channel architecture hierarchically, i.e. first declare the number of tiers and branches in the channel, and then choose a feedback topology (as in Figure 5).Optimise the average inference error Equation 20 w.r.t. to the channel parameters v→∈V within the bounds provided in Table 1. We use a gradient independent method viz. Pattern Search algorithm for this step (implemented in MATLAB). For every poll (iteration) of the Pattern Search, we evaluate the average inference error σ¯X using the steady-state outputs of the equations corresponding to the CRN under optimisation that is Equations 10–17. The steady state solution is obtained analytically when possible or solved using ODE15s (MATLAB) algorithm.Repeat Step 3 until all feedback topologies under consideration are exhausted.Repeat Steps 2 and 3 until all channel architectures are scanned.</td>
    </tr>
  </tbody>
</table>

## Results

As discussed previously, cells of a developing tissue face both extrinsic as well as intrinsic sources of noise. We first look at the issue of extrinsic noise in the morphogen input (described by Equation 1). The output then is a deterministic function of the morphogen input and parameters of the channel i.e. receptor concentrations, feedback topology, chemical rates and feedback parameters. The range of values considered for these parameters is listed in Table 1, consistent with the timescale separation between the rates of chemical reactions and transport as discussed in Section ‘Conceptual framework and quantitative models’. We apply the numerical analysis and the optimisation algorithm outlined in Section ‘Performance of the Channel Architectures’ to determine the design characteristics of ‘reading’ (receptor profiles) and ‘processing’ (tiers and feedback control) steps. Later, we check how channels, optimised in the reading and processing steps to deal with extrinsic noise, respond to intrinsic noise and what roles the elements of channel architecture play there. All the essential results are presented in this section and the reader may look up the appendices for further details.

### Branched architecture with multiple receptors provides accuracy and robustness to extrinsic noise

We begin with architectures comprising single-tiered channels with one and two branches. Such architectures are similar in design to the classic picture of ligand-receptor kinetics Lauffenburger and Linderman, 1996; Alberts et al., 2017, but also to the self-enhanced degradation models for robustness of morphogen gradients Eldar et al., 2003. Before we proceed, it helps to recall a simple heuristic regarding signal discrimination. Appendix 4—figure 1 illustrates that precision in positional inference requires both that the output variance at a given position be small and that the mean output at two neighbouring positions be sufficiently different.

Let us first consider a minimal architecture of a one-tier one-branch channel without feedback control on any of the reaction rates. The output of this channel, here $R^{(1)}$, is a monotonic, saturating function of the input, with the surface receptor concentration setting the asymptote. As in Appendix 5—figure 1a, if the receptor concentrations decrease with mean ligand input, i.e. increases with distance from source ($f_{A}$ in Figure 3a; ), the outputs for different input ranges overlap significantly. On the other hand, if the receptor concentrations increase with mean input ($f_{B}$ in Figure 3b), the outputs overlap to a lesser degree (see Appendix 5—figure 1b). Thus within this minimal architecture, the inference error is optimised when the receptor concentrations increase with the mean input.

Introducing a feedback in this one-tier one-branch architecture, either on receptor levels or degradation rate, only partially reduces the inference errors (Figure 6a, c). As seen in Figure 6d, this is because the surface receptor concentration $ψ$ sets both the asymptote and the steepness of the input-output functions, resulting in significant overlaps between outputs at neighbouring positions. The receptor control introduces a competition between robustness of the output to input noise and sensitivity to systematic changes in the mean input (see Appendix 4).

![Figure 6.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig6-v1.jpg)

**Figure 6.:** The optimised channel shows a moderately strong positive feedback on the degradation rate. (b) The optimal output is obtained when (b, inset) the total (bound plus unbound) signalling receptor concentration profile decreases away from the source. (c) Local inference errors in this optimised channel show a reduction compared to the expected inference errors from ligand with no cellular processing (i.e. reading directly from the free ligand). The minimum average inference error in this channel is $\sigma¯_{X}∼8%$, which corresponds to 8 cells’ width. The dashed line denotes a local inference error of one cell’s width $∼1/n_{x}$. (d) The input-output relations in this channel are monotonically increasing sigmoid functions saturating at only large values of input. The solid lines correspond to the input-output relations at selected positions $x=0.25,0.5,0.75$, shaded with the same colour as the position-markers in (b inset, coloured rectangles). The signalling $ψ⁢(x)$ receptor concentration is mentioned in the legend. For a fixed distribution of ligand input (Equation 1), the range of input values recorded by the receptors at the selected positions gives rise to a range of outputs (circles). It is clear that neighbouring positions have significant overlaps in their outputs. The optimised parameter values for the plots in (b–d) can be found in Table 2 under the column corresponding to $n_{T}=1,n_{B}=1,r_{+}=r_{d}^{(1)}$.

Including a non-signalling receptor $ϕ$ via an additional branch in the channel architecture opens up several new possibilities of feedback controls, in addition to providing an extra tuning variable. Now, as opposed to the one-tier one-branch case, an inter-branch feedback control (Figure 7a) results in an input-output relation with a sharp rise followed by a saturation (Figure 7d). By appropriately placing the receptors at spatial locations that receive different input, as shown by black arrow in Figure 7d, one can cleanly separate out the cellular outputs in neighbouring positions. For a detailed description see Appendix 6. This mitigates the above-mentioned tension between robustness to input noise and sensitivity to systematic changes in the mean input to a considerable extent (see Appendix 4—figure 2).

![Figure 7.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig7-v1.jpg)

**Figure 7.:** (b) The output profile (with standard error in shaded region) corresponding to the (inset) optimised signalling (blue) and non-signalling (red) receptor profiles. The optimal signalling receptor now increases away from the source as opposed to the situation in the optimal one-tier one-branch channel (Figure 6). On the other hand, the optimal non-signalling receptor decreases away from the source. (c) The local inference error $\sigma_{X}⁢(x)$ is reduced throughout the tissue, when compared to the expected inference errors from ligand with no processing. (d) The input-output relations at selected positions $x=0.25,0.5,0.75$ (in the direction of the black arrow) are shown as solid lines, shaded with the same colour as the position-markers in (b inset, coloured rectangles). The signalling $ψ⁢(x)$ and non-signalling $ϕ$ receptor concentrations are mentioned in the legend. For a fixed distribution of ligand input (Equation 1), the range of input values recorded by the receptors at the selected positions gives rise to a range of outputs (circles). Tuning of input-output relations through receptor concentrations reduces output variance and minimises overlaps in the outputs of neighbouring cell cohorts. The optimised parameter values for the plots in (b–d) can be found in Table 2 under the column corresponding to $n_{T}=1,n_{B}=2,r_{-}=κ_{C}$.

As seen in Figure 7c, the two-branch architecture with inter-branch feedback leads to a dramatic reduction in the inference errors, to reach one cell’s width precision at most spatial locations in the tissue.

We would like to highlight two unexpected features of the optimised two-branch architecture. (i) The signalling and non-signalling receptors present opposing optimal profiles – a consequence of the negative inter-branch feedback. (ii) The optimal non-signalling receptor decreases away from the source, indicating that the non-signalling receptor ‘reads’ the ligand input, while the signalling receptor increases away from the source, buffering the noise in the output (Figure 7). A heuristic understanding of the opposing optimal receptor profiles is provided in Appendix 7. In contrast, in the one-branch architectures, it is the signalling receptor that does the reading and buffering.

**Table 2.**
 Values of rates, feedback and receptor control parameters obtained after optimising the different channel architectures with $n_{T}$ tiers and $n_{B}$ branches.The optimised values of the chemical rates quoted below are scaled by the unbinding rate ru, $κ_{u}$ taken to be 1. The symbols $r_{-}$ and $r_{+}$ denote positive and negative feedbacks, respectively, on the rates following the equals sign; ${}$ implies absence of feedback.


<table>
  <thead>
    <tr>
      <th rowspan="3">Parameter (Symbol)</th>
      <th colspan="5">Value obtained in the optimised channel (nT,nB)</th>
    </tr>
    <tr>
      <th>(1,1)</th>
      <th>(1,2)</th>
      <th>(2,2)</th>
      <th>(2,2)</th>
      <th>(2,2)</th>
    </tr>
    <tr>
      <th>r+=rd(1)</th>
      <th>r-=κC</th>
      <th>r-=κI</th>
      <th>r-=κC</th>
      <th>r-={}</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chemical rates</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Signalling branch</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Binding rate (rb,nM-1)</td>
      <td>0.0898</td>
      <td>0.0949</td>
      <td>0.0932</td>
      <td>0.0893</td>
      <td>0.0787</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 1 (rd(1))</td>
      <td>0.0013</td>
      <td>0.0081</td>
      <td>0.0086</td>
      <td>0.0098</td>
      <td>0.0038</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 2 (rd(2))</td>
      <td>-</td>
      <td>-</td>
      <td>0.0066</td>
      <td>0.0087</td>
      <td>0.0016</td>
    </tr>
    <tr>
      <td>Internalisation rate (rI)</td>
      <td>-</td>
      <td>-</td>
      <td>0.0531</td>
      <td>0.0784</td>
      <td>0.0363</td>
    </tr>
    <tr>
      <td>Recycling rate (rR)</td>
      <td>-</td>
      <td>-</td>
      <td>0.0681</td>
      <td>0.0359</td>
      <td>0.0758</td>
    </tr>
    <tr>
      <td>Non-signalling branch</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Binding rate (κb,nM-1)</td>
      <td>-</td>
      <td>0.0590</td>
      <td>0.0954</td>
      <td>0.0835</td>
      <td>0.0288</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 1 (κd(1))</td>
      <td>-</td>
      <td>0.0086</td>
      <td>0.001</td>
      <td>0.0043</td>
      <td>0.0068</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 2 (κd(2))</td>
      <td>-</td>
      <td>-</td>
      <td>0.0037</td>
      <td>0.0031</td>
      <td>0.0033</td>
    </tr>
    <tr>
      <td>Internalisation rate (κI)</td>
      <td>-</td>
      <td>-</td>
      <td>0.0741</td>
      <td>0.0846</td>
      <td>0.0559</td>
    </tr>
    <tr>
      <td>Recycling rate (κR)</td>
      <td>-</td>
      <td>-</td>
      <td>0.0123</td>
      <td>0.0134</td>
      <td>0.0998</td>
    </tr>
    <tr>
      <td>Conjugation rate (κC,nM-1)</td>
      <td>-</td>
      <td>0.9926</td>
      <td>0.9823</td>
      <td>0.9722</td>
      <td>0.6019</td>
    </tr>
    <tr>
      <td>Splitting rate (κS)</td>
      <td>-</td>
      <td>0.1285</td>
      <td>0.1545</td>
      <td>0.1350</td>
      <td>0.7512</td>
    </tr>
    <tr>
      <td>Feedback control</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Amplification (α)</td>
      <td>3.2085</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Feedback Sensitivity (γ)</td>
      <td>0.2491</td>
      <td>0.1831</td>
      <td>0.5535</td>
      <td>0.8259</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Feedback strength (n)</td>
      <td>2.6825</td>
      <td>2.3683</td>
      <td>2.0953</td>
      <td>2.1880</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Tier-wise weights</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>weight of tier 1 (w1)</td>
      <td>1</td>
      <td>1</td>
      <td>0.0018</td>
      <td>0.1232</td>
      <td>0.9259</td>
    </tr>
    <tr>
      <td>weight of tier 2 (w2)</td>
      <td>-</td>
      <td>-</td>
      <td>0.9982</td>
      <td>0.8768</td>
      <td>0.0741</td>
    </tr>
    <tr>
      <td>Receptor control</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Signalling receptors</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hill coefficient (a)</td>
      <td>4.9231</td>
      <td>1.9974</td>
      <td>3.8363</td>
      <td>3.5251</td>
      <td>3.3835</td>
    </tr>
    <tr>
      <td>Minimum concentration (A0,nM)</td>
      <td>51.8130</td>
      <td>51.0960</td>
      <td>69.6940</td>
      <td>51.9770</td>
      <td>51.2</td>
    </tr>
    <tr>
      <td>Maximum concentration (A0+A1,nM)</td>
      <td>298.283</td>
      <td>290.356</td>
      <td>304.114</td>
      <td>134</td>
      <td>301</td>
    </tr>
    <tr>
      <td>Position of half-maximum (A2)</td>
      <td>0.4752</td>
      <td>0.7818</td>
      <td>0.9405</td>
      <td>0.8344</td>
      <td>0.4091</td>
    </tr>
    <tr>
      <td>Non-signalling receptors</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hill coefficient (b)</td>
      <td>-</td>
      <td>4.8951</td>
      <td>1.0802</td>
      <td>1.7472</td>
      <td>3.1821</td>
    </tr>
    <tr>
      <td>Minimum concentration (B0,nM)</td>
      <td>-</td>
      <td>192.32</td>
      <td>248.69</td>
      <td>192.4</td>
      <td>94.1850</td>
    </tr>
    <tr>
      <td>Maximum concentration (B0+B1,nM)</td>
      <td>-</td>
      <td>442</td>
      <td>489.77</td>
      <td>441.67</td>
      <td>305</td>
    </tr>
    <tr>
      <td>Position of half-maximum (B2)</td>
      <td>-</td>
      <td>0.7428</td>
      <td>0.5177</td>
      <td>0.3196</td>
      <td>0.0902</td>
    </tr>
  </tbody>
</table>

### Tiered architecture with compartmentalisation adds robustness to intrinsic noise

We next investigate the effects of addition of tiers (compartments) on the inference errors. Our optimisation shows there are two distinct optimised two-tier two-branch architectures, one with inter-branch feedback on the internalisation rate of the non-signalling receptors $κ_{I}$ and the other on the conjugation rate $κ_{C}$, that have comparable inference errors (Figure 8b, c). Both the receptor profiles and the input-output relations of these two optimised two-tier two-branch channels are qualitatively similar (Appendix 8—figure 1).

![Figure 8.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig8-v1.jpg)

**Figure 8.:** (a) Minimum average inference error $\sigma¯_{X}$ in two-branch architectures with increasing number of tiers $n_{T}$. The dashed line corresponds to a local inference error of one cell’s width $∼1/n_{x}$. (b,c) Results of optimisation of two-tier two-branch channels with inter-branch feedback. These two architectures perform equally well: local inference errors in both the channels (blue dots) are low throughout the tissue (with average inference errors $∼1.6%$ and $∼1.7%$) as compared to a case with no processing of ligand prior to inference (black dots). Note that the local inference errors in the optimised channels increase towards the end of the tissue due to lower ligand concentrations. The dashed line corresponds to a local inference error of one cell’s width $∼1/n_{x}$. The optimised parameter values for the plots in (b–c) can be found in Table 2 under the column corresponding to $n_{T}=2,n_{B}=2,r_{-}=κ_{I}$ and $n_{T}=2,n_{B}=2,r_{-}=κ_{C}$, respectively.

It would seem that addition of further tiers, that is more than two, would lead to further improvement in the inference. However, in both these optimised architectures, addition of tiers leads only to a marginal reduction of inference errors (Figure 8a) while invoking a cellular cost. Of course, extensions of our model that involve modification of the desired output could favour the addition of more tiers. For instance, additional tiers could facilitate signal amplification or improvement in robustness to input noise through an increase in signal-to-noise ratio (SNR) Stoeger et al., 2016. Further, by making the output $\theta$ a multi-variate function of the tier index (compartment identity) one can multitask the various cellular outcomes (as in Ras/MAPK signalling Fehrenbacher et al., 2009 or with GPCR compartmentalisation Ellisdon and Halls, 2016).

So far, we have only considered noise due to fluctuations in the morphogen profile, that is extrinsic noise. Given that we are considering a distributed channel, intrinsic noise due to low copy numbers of the reacting species in the CRN will have a significant influence on the inference. As discussed in Section ‘Conceptual framework and quantitative models’ and Appendix 3, we solve the stochastic chemical master equations (CMEs) to compute the output distributions and the positional inference. It is here that we find that the addition of tiers contribute significantly to reducing inference errors. A comparison of the one-tier two-branch and two-tier two-branch channel architectures (Figure 9a and b) optimised for extrinsic noise, shows that in the presence of intrinsic noise, additional tiers lead to significantly lower inference errors (Figure 9c). The large inference errors seen in the one-tier one-branch channel in the presence of intrinsic noise, can be traced to the instabilities of steady-state trajectories of the two signalling species $R^{(1)}$ and $Q^{(1)}$ driven by the non-linear feedback (Figure 9d–f). This effect is more prominent for larger values of ligand concentrations, that is closer to the source at $x=0$. On the other hand, we find that in the two-tier two-branch architecture (Figure 9g–i), the fluctuations in the signalling species are more tempered, the inter-branch feedback leads to a mutual damping of the fluctuations of the signalling species from the two branches. Details of this heuristic argument appear in Appendix 9.

![Figure 9.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig9-v1.jpg)

**Figure 9.:** (c) A comparison of local inference errors due to intrinsic noise shows consistently better performance in the case of a two-tier two-branch channel (red dots). (d-f) Sample steady-state trajectories of the signalling species $R^{(1)}$ (blue) and $Q^{(1)}$ (red) of a one-tier two-branch channel (purple nodes in (a)) at positions $x=0.1,0.4,0.7$, respectively. (g–i) Sample steady-state trajectories of the signalling species $R^{(2)}$ (blue) and $Q^{(2)}$ (red) of a two-tier two-branch channel (purple nodes in (b)) at positions $x=0.1,0.4,0.7$, respectively. The optimised parameter values for the plots in (c,d–f,g–i) can be found in Table 2 under the column corresponding to $n_{T}=1,n_{B}=2,r_{-}=κ_{C}$ and $n_{T}=2,n_{B}=2,r_{-}=κ_{C}$, respectively.

In summary, we find that the nature of the channel architectures play a significant role in robustness of morphogenetic decoding to both extrinsic and intrinsic sources of noise. Of the three elements to the channel architecture - branches, tiers, and feedback control, we find that a branched architecture can significantly reduce inference errors by employing an inter-branch feedback and a control on its local receptor concentrations. For this, the receptor concentration profiles required to minimise inference errors are such that the concentration of signalling (non-signalling) receptor should decrease (increase) with mean morphogen input. Crucially, in the absence of feedback, performance of the channel diminishes and the optimised receptor profiles both decrease away from the source (Appendix 10—figure 1). Further, we show in Appendix 11—figure 1 that having uniform profiles for the signalling and non-signalling receptors, with or without uncorrelated noise, fares poorly in terms of inference capability. This provides a posteriori justification for the monotonicity in receptor profiles. Addition of tiers can help in further bringing down inference errors due to extrinsic noise, but with diminishing returns. An additional tier, however, does provide a buffering role for feedback when dealing with intrinsic noise. We note that these qualitative conclusions remain unaltered for different morphogen input characteristics, that is input noise and morphogen decay lengths (see Appendix 12).

### Asymmetry in branched architecture: promiscuity of non-signalling receptors

Before comparing the theoretical results with experiments, we comment on the implications for the cellular control of the signalling $ψ$ and non-signalling $ϕ$ receptors. In the two-branch architecture, the symmetry between the signalling and non-signalling receptors is broken by the inter-branch feedback and the definition of output $\theta$, the latter taken to be a function only of the signalling states $R^{(k)}$ and $Q^{(k)}$ (Section ‘Conceptual framework and quantitative models’, purple nodes in Figure 7a and Figure 8b and c). What are the phenotypic implications of this asymmetry? In Appendix 13—figure 1, we plot the contours of average inference errors $\sigma¯_{X}$ in the $ψ-ϕ$ plane around the optimal point. We compute the eigenvalues of the local curvature of $\sigma¯_{X}⁢(Δ⁢ψ,Δ⁢ϕ)$ around the optimal point ($Δ⁢ψ=Δ⁢ϕ=0$). The difference in the magnitudes of these eigenvalues, as discussed in Appendix 13, immediately describes stiff and sloppy directions Transtrum et al., 2015 along the $ψ$ and $ϕ$ axes, respectively. This implies that while the signalling receptor is under tight cellular control, the control on the non-signalling receptor is allowed to be sloppy. A similar feature is observed in the contour plots for the robustness measure $χ$ (defined as the ratio of coefficients of variation in the output to that in the input). Appendix 4—figure 3 shows that for any given input distribution, reduction in output variance requires a stricter control on $ψ$, while the control on $ϕ$ can be lax.

This sloppiness in the levels of non-signalling receptor would manifest at a phenotypic level in the context of multiple morphogen inputs as in the case of Drosophila imaginal disc Tabata and Takei, 2004. Participation of the same non-signalling receptor in the different signalling networks would imply its promiscuous interactions with all ligands. The signalling receptors, therefore, are specific for the various ligands while the non-signalling receptor, being promiscuous, is non-specific. This, as we see below, is the case with the Heparan sulfate proteoglycans (HSPGs) such as Dally and Dally-like protein (Dlp) that participate in the Wingless (Wg) and Decapentaplegic (Dpp) signalling networks Lin and Perrimon, 2000; Romanova-Michaelides et al., 2021.

### Geometry of fidelity landscape

The above section and Appendix 13 motivate us to study the changes in the inference error upon perturbations of all the channel parameters. We therefore discuss the nature of optima in terms of the local geometry of the fidelity landscape around the optimum, and the geometry of the low inference error states. We work with the case of the optimised one-tier two-branch channel (shown in Figure 7a with optimum channel parameters listed in Table 2, Table 3) in presence of extrinsic noise.

**Table 3.**
 Values of chemical rates and feedback parameters obtained after optimising the two-tier two-branch channel with inter-branch feedback on the internalisation rate $κ_{I}$ of the non-signalling branch, keeping the receptor profiles spatially uniform, with and without uncorrelated noise.The optimised values of the chemical rates quoted below are scaled by the unbinding rate ru, $κ_{u}$ taken to be 1.


<table>
  <thead>
    <tr>
      <th rowspan="2">Parameter (Symbol)</th>
      <th colspan="2">Optimised value</th>
    </tr>
    <tr>
      <th>uniform receptor profiles</th>
      <th>uniform receptor profiles with uncorrelated noise</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chemical rates</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Signalling branch</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Binding rate (rb,nM-1)</td>
      <td>0.0922</td>
      <td>0.0782</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 1 (rd(1))</td>
      <td>0.0089</td>
      <td>0.0041</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 2 (rd(2))</td>
      <td>0.0092</td>
      <td>0.0095</td>
    </tr>
    <tr>
      <td>Internalisation rate (rI)</td>
      <td>0.0225</td>
      <td>0.0611</td>
    </tr>
    <tr>
      <td>Recycling rate (rR)</td>
      <td>0.0403</td>
      <td>0.0971</td>
    </tr>
    <tr>
      <td>Non-signalling branch</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Binding rate (κb,nM-1)</td>
      <td>0.0464</td>
      <td>0.0265</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 1 (κd(1))</td>
      <td>0.0035</td>
      <td>0.0045</td>
    </tr>
    <tr>
      <td>Degradation rate in tier 2 (κd(2))</td>
      <td>0.0071</td>
      <td>0.0068</td>
    </tr>
    <tr>
      <td>Internalisation rate (κI)</td>
      <td>0.02</td>
      <td>0.0513</td>
    </tr>
    <tr>
      <td>Recycling rate (κR)</td>
      <td>0.0989</td>
      <td>0.0770</td>
    </tr>
    <tr>
      <td>Conjugation rate (κC,nM-1)</td>
      <td>0.7605</td>
      <td>0.7579</td>
    </tr>
    <tr>
      <td>Splitting rate (κS)</td>
      <td>0.7038</td>
      <td>0.3036</td>
    </tr>
    <tr>
      <td>Feedback control</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Amplification (α)</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Feedback Sensitivity (γ)</td>
      <td>0.0939</td>
      <td>0.1946</td>
    </tr>
    <tr>
      <td>Feedback strength (n)</td>
      <td>4.6310</td>
      <td>0.6202</td>
    </tr>
    <tr>
      <td>Tier-wise weights</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>weight of tier 1 (w1)</td>
      <td>0.0046</td>
      <td>0.2875</td>
    </tr>
    <tr>
      <td>weight of tier 2 (w2)</td>
      <td>0.9954</td>
      <td>0.7125</td>
    </tr>
  </tbody>
</table>

To address the geometry of the local fidelity landscape around the optimum, we compute (i) percent changes in inference error $\sigma¯_{X}$ due to perturbations in channel parameters (Figure 10a), and (ii) the eigenspectrum of the Fisher information metric (FIM, Figure 10b). The FIM $g_{\mu⁢ν}$ is evaluated in the log-parameter space as Transtrum et al., 2015.

$$
g_{\muν}=\sumx_{i}\sumy_{j}\frac{∂x^{∗}(M(x_{i},y_{j}),v→)}{∂ln⁡v^{\mu}}\frac{∂x^{∗}(M(x_{i},y_{j}),v→)}{∂ln⁡v^{ν}}
$$

where, $v→\inV$ is the channel parameter vector, and $x_{i},y_{j}$ are the indices of cells that run along the $x$- and $y$-directions. As shown in Figure 10a, we see that the inference error does not change significantly (up to 20% change with most parameters), that is it remains within $\sigma¯_{X}\leq2.2%$. Varying the feedback strength $n$, however, drives a much stronger deviation from the minimum. Similarly, as seen from the heat map (Figure 10b), eigenvectors with the larger eigenvalues (index 1–6) have an appreciable component of the feedback parameters $\gamma,n$. This implies that variation of the feedback parameters from the optimum would result in significant changes in the inferred positions. Perturbing conjugation $κ_{C}$ and splitting $κ_{S}$ rates simultaneously (see eigenvector 16) does not produce any notable change to the inferred positions (eigenvalue $∼10^{-13}$). Further, perturbations to channel parameters other than the feedback parameters (eigenvectors 7–16) produce marginal changes in inferred positions.

![Figure 10.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig10-v1.jpg)

**Figure 10.:** (a) Percent changes in the inference error upon perturbations in the channel parameters (as described in Table 1) around the optimum for one-tier two-branch channel (optimised $\sigma¯_{X}=1.9%$). For most perturbations, the inference error deviates by up to 20% of the optimum i.e. the inference error $\sigma¯_{X}$ remains below 2.2%. (b) Left: eigen spectrum of the Fisher information metric (FIM, see Equation 21) around the global minimum of $\sigma¯_{X}$, Right: weight of the different channel parameters in the eigenvectors of FIM, obtained from projecting each eigenvector along the channel parameter axes. The index 1 corresponds to the eigenvector with the largest eigenvalue and the index 16 corresponds to the eigenvector with the smallest eigenvalue.

Moving now from a local to global analysis of the fidelity landscape, we run the optimisation algorithm (Section ‘Performance of the Channel Architectures’) on the one-tier two-branch channel architecture with 216 space-filling initial points in the 16-dimensional parameter space of this architecture. We then define the low inference error states as those channel parameters $v→^{opt}$ that yield $\sigma¯_{X}\leq2%$. This cutoff, which equals $⌈\frac{\sigma¯_{X}}{0.01}⌉$, corresponds to declaring as equivalent all the inference errors $\sigma¯_{X}$ that lie between one and two cells’ widths. Consistent with the local analyses, we find that the frequency distribution of optimal feedback parameters $\gamma,n$ is narrowly distributed about the global optimum (Figure 11a). As shown in Figure 11a, the parameters corresponding to forward and backward rates are skewed towards the upper and lower bounds of the allowed parameter range, respectively. We see that the optimal binding rates in the non-signalling branch (Figure 11a) are more broadly distributed across the permissible range than the optimal binding rates in the signalling branch, which are concentrated towards the upper bound of the permissible range. This again reflects the promiscuity of the non-signalling receptors as described in Section ‘Asymmetry in branched architecture: promiscuity of non-signalling receptors’. All other optimal parameters corresponding to degradation rates, minimum and maximum receptor values and steepness of the receptor profiles, show a very broad spread over this range (Appendix 14—figure 1). To explore the topography of the low inference error landscape, we evaluate the components of the ‘position vectors’ of these minima $v→^{opt}$ in the parameter space $V$ along the eigenvectors of the Hessian of $\sigma¯_{X}$, defined as

$$
h_{\muν}=\frac{∂^{2}\sigma¯_{X}(M,v→)}{∂v^{\mu}∂v^{ν}}
$$

where $M$ stands for the entire morphogen profile and we have assumed a Euclidean metric. As shown in Figure 11b and c, components of the ‘position vector’ of the minima $v→^{opt}\inV$ lie predominantly along the sloppy directions of the Hessian that is along the eigenvectors with small eigenvalues. This suggests that geometry of the low inference error landscape resembles a deep valley, which is shallow along the several sloppy directions and steep along the few stiff directions.

![Figure 11.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig11-v1.jpg)

**Figure 11.:** Geometry of the low inference error landscape defined by channels within a band $\sigma¯_{X}\leq2%$ about the global minimum.(a) Frequency distributions of optimised channel parameters in the low inference error landscape. Here we show the ligand binding rates of the signalling and non-signalling receptors, conjugation and splitting rates, and feedback sensitivity and feedback strength parameters. The distributions of the other optimised channel parameters are shown in Appendix 14. (b) Eigenvalues of the Hessian $h_{\mu⁢ν}$ (see Equation 22) of $\sigma¯_{X}$ around the global minimum. (c) Components of the normalised ‘position vectors’ of the minima $v→^{opt}\inV$ along the eigenvectors of the Hessian $h_{\mu⁢ν}$, obtained from projecting each position vector along the eigenvector of the Hessian. Here, position vectors in the parameter space $V$ are defined by the usual Euclidean metric.

### Choice of objective function

The objective function as defined in Equation 7 gave equal weight to inference errors at all positions $x$ along the tissue, driving the inference error to reduce at all positions simultaneously. In certain developmental contexts, the objective could be to partition the tissue into cell identity segments (reviewed in Briscoe and Small, 2015). In such a case, the partition boundaries would need to be sharp Gregor et al., 2007a that is only the errors at the segment boundaries would need to be minimised. We show that even with this choice of objective function, the qualitative results for the optimal channel architectures remain unaltered. We define the inference error for a tissue with $N_{p}$ segmented cell identities as.

$$
\sigma_{X}^{2}(x)=⟨(1−\delta_{g(x),g(x^{∗})})(x^{∗}−x)^{2}⟩_{y}whereg(x)=1+\sumi=1N_{p}Θ(x−ξ_{i})
$$

where $\delta$ and $Θ$ denote the Kronecker-delta and Heaviside-theta functions respectively, $ξ_{i}$ is the position of the boundary between the i-th and (i+1)-th segments, and $g$ is a function that maps position (actual or inferred) to a segment, that is $g:[0,1]→{1,2,…,N_{p}}$ with $N_{p}$ as the total number of segments.

We optimise one-tier one-branch, one-tier two-branch and two-tier two-branch channel architectures for the inference error as defined in Equation 23 with $N_{p}=4$ and equally spaced boundaries located at positions $ξ_{1}=0.25,ξ_{2}=0.5,ξ_{3}=0.75$ along the $x$-axis. As before, this optimisation suggests that an additional branch aids in reducing the inference errors due to extrinsic noise (compare Figure 12b and d), with similar opposing receptor profiles as in Section ‘Branched architecture with multiple receptors provides accuracy and robustness to extrinsic noise’. Tiers play only a moderate role in reducing the inference errors further in a two-branch channel (compare Figure 12d and f). However, just as with the previous objective function, an additional tier provides substantial robustness to intrinsic noise as shown in Figure 13c.

![Figure 12.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig12-v1.jpg)

**Figure 12.:** (a) Profile of the signalling receptor for (a, inset) the optimised one-tier one-branch channel. (b) Corresponding inference errors due to extrinsic noise in the optimised one-tier one-branch channel. (c) Profiles of the signalling (blue) and non-signalling (red) receptor for (c, inset) the optimised one-tier two-branch channel. (d) Corresponding inference errors due to extrinsic noise in the optimised one-tier two-branch channel. Errors are predominantly located around the segment boundaries at $x=0.25,0.5,0.75$ and still increase in the direction of reducing morphogen concentrations. (e) Profiles of the signalling (blue) and non-signalling (red) receptor for (e, inset) the optimised two-tier two-branch channel. (f) Corresponding inference errors due to extrinsic noise in the optimised two-tier two-branch channel. Note that the errors here are predominantly around the segment boundaries ($x=0.25,0.5,0.75$) and diminished compared to the one-tier two-branch channel in (d).

![Figure 13.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig13-v1.jpg)

**Figure 13.:** (c) A comparison of local inference errors of the two optimised channels in (a,b) in presence of intrinsic noise. Even for this choice of objective function, the two-tier channel shows consistently better performance.

### Experimental verification in the Drosophila Wg signalling system

The phenomenology of the morphogen reading and processing of Wg in the wing imaginal disc of Drosophila melanogaster Hemalatha et al., 2016 suggests a one-to-one mapping to the two-tier two-branch channel defined above, thus providing an ideal experimental system for a realisation of the ideas presented here (Figure 14a, b).

![Figure 14.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig14-v1.jpg)

**Figure 14.:** (a) Schematic of the cellular processes involved in Wg signalling, showing the two endocytic routes for the receptors (see text for further description). (b) Two-tier two-branch channel architecture corresponding to the Wg signalling system. (c) Schematic describing the XY view of wing disc. The vertical brown stripe marks the Wg producing cells. Horizontal green stripes mark the regions in wing disc used for analysis. See Experimental Methods (Appendix 15) for more information. (d) Coefficient of variation (CV) of CAAX-GFP intensity profiles, expressed in wing discs, as a function of (normalized) distance from producing cells (n=4). (e) Coefficient of variation in the output of the optimised two-tier two-branch channel (blue), and upon perturbation (orange) via removal of the non-signalling branch, implemented by setting all rates in the non-signalling branch $κ$ to zero. The optimised parameter values for the plot can be found in Table 2 under the column corresponding to $n_{T}=2,n_{B}=2,r_{-}=κ_{C}$. (f) CV of intensity profiles of endocytosed Wg in control wing discs (C5GAL4Xw1118; blue; n=4) and discs where CLIC/GEEC endocytic pathway is removed using UAS-myr-garz-DN (C5GAL4XUAS-myr-garz-DN; orange; n=5).

![Figure 14—figure supplement 1.](https://cdn.elifesciences.org/articles/79257/elife-79257-fig14-figsupp1-v1.jpg)

**Figure 14—figure supplement 1.:** Fluorescence intensity profiles of: (a) GFP-Myr-Garz-DN and control. Endocytosed Wg profiles in (b) control wing discs (n=4) and (c) discs where CLIC/GEEC endocytic pathway is removed using UAS-myr-Garz-DN (n=5). Figure 14—figure supplement 1—source data 1.Fluorescence intensity measurements for a-c. Mean and standard error of mean (SEM) for b,c. Figure 14—source data 1.CV of intensity measurements of CAAX GFP and endocytosed Wg, in control and myr-Garz-DN, as a function of distance from producing cells in individual samples of wing imaginal discs.

Wingless (Wg) is secreted by a line of cells (1–3 cells) at the dorso-ventral boundary and forms a concentration gradient across the receiving cells Neumann and Cohen, 1997. Receiving cells closer to the production domain show higher Wg signalling while those farther away have lower Wg signalling Neumann and Cohen, 1997. Several cell autonomous factors influence reading and processing of the morphogen Wg in the receiving cells. Binding of Wg to its signalling receptor, Frizzled-2 (DFz2), initiates signal transduction pathway and nuclear translocation of $\beta$-catenin which further results in activation of Wg target genes (reviewed in Clevers and Nusse, 2012). In addition to the signalling receptor, binding receptors such as Heparin Sulphate Proteoglycans (HSPGs) – Dally and Dlp also contribute to Wg signalling Baeg et al., 2001; Franch-Marro et al., 2005. Further, the two receptors follow distinct endocytic pathways Hemalatha et al., 2016: while, DFz2 enters cells via the Clathrin Mediated Endocytic pathway (CME), Wg also enters cells independent of DFz2, possibly by binding to HSPGs, through CLIC/GEEC (CG) endocytic pathway. The two types of vesicles, containing Wg bound to different receptors, merge in common early endosomes Hemalatha et al., 2016. However, only DFz2 receptors in their Wg-bound state, both at the cell surface and early endosomes, are capable of generating a downstream signal leading to positional inference through a transcriptional readout Tsuda et al., 1999. This phenomenology is faithfully recapitulated in our two-tier two-branch channel architecture (Figure 14b) in which DFz2 and HSPG receptors play the role of the two branches. The conjugated state ‘Q’ represents a combination of the readings from the two branches, possibly realised by the co-receptors HSPGs that bind Kirkpatrick et al., 2006; Capurro et al., 2008 and present Hemalatha et al., 2016 diffusible ligands to signalling receptors (either on the cell surface or within endosomes).

Since an experimental measurement of positional inference error poses difficulties, we measure the cell-to-cell variation in the signalling output for a given position $x$ as a proxy for inference error (Appendix 4—figure 3). Larger the variation, higher is the inference error. This is calculated as coefficient of variation (CV, Appendix 15) in the output across cells in the $y$-direction (Figure 14c).

Let us first discuss the results from the theoretical analysis. The optimised two-tier two-branch channel (Figure 14b) shows that the magnitude and the fluctuations in the coefficients of variation are small, with a slight increase with position (blue, Figure 14f). This is consistent with the low inference error associated with the optimised channel (Figure 8b). Upon perturbing this channel via removal of the non-signalling branch, the magnitude and fluctuations in the signalling output variation increases significantly (orange, Figure 14e). This qualitative feature of the coefficient of variation in the optimised two -tier two-branch channel is replicated in the Wg measurements of wild type cells.

In the experiments, we first established the method by determining the CV of a uniformly distributed signal, CAAX-GFP (expressed using ubiquitin promoter), and observed that the CV of CAAX-GFP is relatively uniform in $x$, the distance from Wg producing cells (Figure 14d). In order to study the steady state distribution of Wg within a cell and within the endosomes, we performed a long endocytic pulse (1 hr) with fluorescently labelled antibody against Wg Hemalatha et al., 2016; Prabhakara et al., 2022. Following this, we estimated the CV of the Wg endocytic profile as a function of $x$ (Figure 14f, and Figure 14—figure supplement 1).

We assessed the CV of endocytosed Wg under two conditions: one, where the endocytic pulse of Wg is captured by the two branches and two tiers (control condition), and another, where we disengage one of the tiers by inhibiting the second endocytic pathway using a genetically expressed dominant negative mutant of Garz, a key player in the CG endocytic pathway Gupta et al., 2009. This perturbation has little or no effect on the functioning of the CME or the levels of the surface receptors that are responsible for Wg endocytosis (Hemalatha et al., 2016; Prabhakara et al., 2022). As predicted by the theory (Figure 14e), CV in the control shows a slight increase with position (Figure 14f) with fluctuations about the mean profile being small. In the perturbed condition, with the CG endocytic pathway disengaged, we find the CV shows a steeper increase with $x$ and has larger fluctuations about the mean profile.

In principle, the coefficient of variation of the output is affected by all the microscopic stochastic processes that intersect with Wg signalling network in the wing imaginal disc and in the ligand input. Therefore, one has to be careful about interpreting the changes in the coefficient of variation of the output, based on the such perturbation experiments. Notwithstanding, this qualitative agreement between theory and experiment is encouraging.

## Discussion

In this paper, we have posed the problem of spatial patterning of cell fates in a developing tissue as a local, cell autonomous morphogenetic decoding that ensures precise inference of position, that is robust to extrinsic and intrinsic noise. We treat the cells as inference channels capable of reading and processing the morphogen input. We describe the architecture of the inference channels in terms of three elements: branches (number of receptor types), tiers (number of compartments) and feedbacks. We ask for properties of the inference channel architectures that allow for precision and robustness in the task of morphogenetic decoding of cellular position.

### Key results

Taking an information theoretic and systems biology approach, we have addressed the issue of accurate and robust morphogenetic decoding of position. For convenience, we summarise our key results in a point-wise manner:

Our theoretical predictions are compared with experimental observations from Wg morphogen system of Drosophila wing imaginal disc. We first show that Wg signalling in the experimental system is equivalent to a two-tier two-branch channel. In the experiments, we use signal-to-noise ratio (SNR) of the output as a proxy for robustness of inference. Perturbation of the architecture, i.e. removal of the non-signalling branch, results in reduction of SNR. In a forthcoming manuscript, we will provide a detailed verification of the predicted opposing receptor profiles.

### Geometry of the inference error landscape: implications for control

We have explored the local geometry of the fidelity landscape around the optimum, and the global geometry of the low inference error states, by perturbing channel parameters and concentration profiles of the receptors.

The local geometry of the fidelity landscape is studied using the Fisher information metric. This shows that steepest variation in the inference error comes from moving along the feedback parameters while perturbations to other channel parameters produces only marginal changes. Further, we explore the global geometry using the spectrum of the Hessian of the inference error. We find that the topography of the low inference error landscape resembles a ravine or a deep valley, which is shallow along the several sloppy directions and steep along the few stiff directions, the latter being predominantly along the feedback parameters. This dimensional reduction appears to be a recurring feature of such high-dimensional optimisation Transtrum et al., 2015; Yadav et al., 2022.

Such a geometrical approach also provides insight on the differences between the signalling and the non-signalling receptors, which shows up in the extent to which they influence inference errors in the neighbourhood of the optimum. Slight changes in the signalling receptor away from the optimum lead to a sharp increase in inference error while similar changes in the non-signalling receptor do not affect the inference errors significantly. This gives rise to the notion of stiff and sloppy directions of control - with non-signalling receptor placed under sloppy control. In a context with multiple morphogen ligands setting up the different coordinate axes (e.g. Wg, Dpp and Hh in imaginal discs Lin, 2004; Lin and Perrimon, 2000), the non-specific receptor can potentially facilitate cross-talks between them. A sloppy control on non-specific receptor would allow for accommodation of robustness in the outcomes of the different morphogens. This could potentially be tested in experiments.

### Future directions

We end our discussion with a list of tasks that we would like to take up in the future. First, the information processing framework established here is very general. Obvious extensions of our models, such as adding more branches, tiers and chemical states, will not lead to qualitatively new features. However, one may alter the objective function – for instance, in the case of short range morphogens like Nodal Liu et al., 2022, only the positions of certain regions (closer to the morphogen source) or cell fate boundaries need to be specified with any precision. To this end, we have analysed another objective function which partitions the tissue into cell identity segments. The qualitative features of the optimised channel architectures remain unaltered. Depending on the developmental context, one might explore other objective functions. This would be a task for a future investigation.

Next, our optimisation study ignores cellular costs due to compartmentalisation, additional receptors and implementation of feedback controls, and thus possible trade-offs between cellular economy and precision in inference. Nevertheless, the observation that addition of extra tiers beyond two provides only marginal improvements to inference, already suggests a balance between precision and cellular costs.

Third, our theoretical result that the optimised surface receptor profiles are either monotonically increasing or decreasing from the morphogen source, suggests that the surface receptor concentrations are spatially correlated across cells. Such correlations could have a mechanochemical basis, either via cell surface tension that could in turn affect internalisation rates Thottacherry et al., 2018 or inter-cellular communication through cell junction proteins Garcia et al., 2018 or from adaptive feedback mechanisms between the output and receptor concentrations Barkai and Leibler, 1997. We emphasize that in the current optimisation scheme, we have allowed the receptor concentrations to vary over the space of all monotonically increasing, decreasing or flat profiles, and have not encoded the positional information in the receptor profiles.

Finally, we have considered the morphogen ligand as an external input to the receiving cells, outside the cellular information processing channel. There is no feedback from the output to the receptors and thus no ‘sculpting’ of the morphogen ligand profile. Morphogen ligand profiles (e.g. Dpp Romanova-Michaelides et al., 2021) are set by the dynamics of morphogen production at the source, diffusion via transcytosis and luminal transport, and degradation via internalisation. These cellular processes are common to both the reading and processing modules in our channel architecture. This would suggest a dynamical coupling and feedback between reading and ligand internalisation, which naturally introduces closed-loop controls on the surface receptors and a concomitant sculpting of the morphogen profile.

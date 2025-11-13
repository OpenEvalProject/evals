# First-principles model of optimal translation factors stoichiometry

## Authors

- Jean-Benoît Lalanne<sup>1</sup> ([ORCID: 0000-0001-8753-0669](https://orcid.org/0000-0001-8753-0669))
- Gene-Wei Li<sup>1</sup> ([ORCID: 0000-0001-7036-8511](https://orcid.org/0000-0001-7036-8511)) †

### Affiliations

1. Department of Biology, Massachusetts Institute of Technology Cambridge United States
2. Department of Physics, Massachusetts Institute of Technology Cambridge United States

† Corresponding author

## Abstract

Enzymatic pathways have evolved uniquely preferred protein expression stoichiometry in living cells, but our ability to predict the optimal abundances from basic properties remains underdeveloped. Here, we report a biophysical, first-principles model of growth optimization for core mRNA translation, a multi-enzyme system that involves proteins with a broadly conserved stoichiometry spanning two orders of magnitude. We show that predictions from maximization of ribosome usage in a parsimonious flux model constrained by proteome allocation agree with the conserved ratios of translation factors. The analytical solutions, without free parameters, provide an interpretable framework for the observed hierarchy of expression levels based on simple biophysical properties, such as diffusion constants and protein sizes. Our results provide an intuitive and quantitative understanding for the construction of a central process of life, as well as a path toward rational design of pathway-specific enzyme expression stoichiometry.

## Introduction

A universal challenge faced by both evolution and synthetic pathway creation is to optimize the cellular abundance of proteins. This abundance optimization problem is not only multidimensional – often involving several proteins participating in the same pathway – but also under systems-wide constraints, such as limited physical space (Klumpp et al., 2013) and finite nutrient inputs (You et al., 2013). The complexity of this problem has prevented rational design of protein expression for pathway engineering (Jeschek et al., 2017). Fundamentally, being able to predict the optimal and observed cellular protein abundances from their individual properties would reflect an ultimate understanding of molecular and systems biology.

Evolutionary comparison of gene expression across microorganisms suggests that basic principles governing the optimization problem may exist. We recently reported broad conservation of relative protein synthesis rates within individual pathways, even under circumstances in which the relative transcription and translation rates for the homologous enzymes have dramatically diverged across species (Lalanne et al., 2018). Moreover, distinct proteins that evolved convergently toward the same biological function also displayed the same stoichiometry of protein synthesis in their respective species. These results suggest that the determinants of optimal in-pathway protein stoichiometry are likely modular and independent of detailed biochemical or physiological properties that differ across clades. However, the precise nature of such determinants remains unknown.

Translation of mRNA into proteins is a central pathway required for cell growth and therefore serves as an entry point for establishing a quantitative model of growth-optimized in-pathway stoichiometry. As a group, the total amount of translation-related proteins per cell mass linearly increases with growth rate in most conditions (Scott et al., 2010; Dai et al., 2016; Schaechter et al., 1958), a relationship considered a bacterial ‘growth law’. In addition to ribosomes which have well-coordinated synthesis of subunits (Nomura et al., 1984), the translation pathway is comprised of nearly 100 protein factors involved in facilitating ribosome assembly, translation initiation, elongation, and termination (Marintchev and Wagner, 2004; Dever and Green, 2012; Rodnina, 2018). The intracellular abundances of these factors vary over 100-fold (Pedersen et al., 1978; Li et al., 2014), and their ratios are often maintained in different growth conditions and across different species (Lalanne et al., 2018). What dictates the observed stoichiometry among translation factors is less understood. Early studies predicted expression of the highly expressed elongation factor Tu (EF-Tu) relative to the ribosome (Klumpp et al., 2013; Ehrenberg and Kurland, 1984) by maximizing translational flux per unit proteome. More recently, expression of several other components involved in the elongation step (ribosomes, tRNA, mRNA, EF-Tu, and EF-Ts) was predicted by minimizing the total mass of the components at a fixed translational flux (Hu et al., 2020). The selective pressure on expression levels remains to be determined for most members of the translation machinery, including initiation and termination factors that are much more lowly expressed and often assumed to be non-limiting.

Here, we sought to derive an intuitive model to understand the quantitative abundance hierarchy (Figure 1B) among the core translation factors (tlFs), which have well-characterized functions (Table 1, schematic in Figure 1A). Our goal is not to exhaustively model the heterogeneous movement of ribosomes on the transcriptome (Shaw et al., 2003; Reuveni et al., 2011; Subramaniam et al., 2014; Dykeman, 2020) or to include as many details of the underlying molecular steps as possible (Hu et al., 2020; Vieira et al., 2016). Instead, we coarse-grained global translation into a cycle that consists of sequential steps with interconnected fluxes that depend on core tlFs concentrations. At steady-state cell growth, all individual fluxes are matched and the overall rate of ribosomes completing the full translation cycle is proportional to cell growth. By solving for the maximum flux under proteome allocation constraints, we obtained analytical solutions for the optimal factor concentrations, which agree well with the observed values. The ratios of optimal concentrations depend only on simple biophysical parameters that are broadly conserved across species. For instance, elongation factor EF-G is predicted to be more abundant than initiation and termination tlFs by a multiplicative factor of $≈\sqrt{average number of codons per protein}≈14$, whereas EF-Tu is predicted to be more abundant than EF-G by a factor of $≈\sqrt{number of different amino acids}≈4$. These results, arising from the optimization procedure and generic properties of the translation cycle, provide rationales for the order-of-magnitude expression of these important enzymes.

![Figure 1.](https://cdn.elifesciences.org/articles/69222/elife-69222-fig1-v2.jpg)

**Figure 1.:** (A) Multiscale model relating translation factor expression to growth rate. The growth rate λ is directly proportional to the active ribosome content ($ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}$) in the cell and inversely proportional to the average time to complete the translation cycle $\tau_{t⁢l}$, consisting of the sum of the initiation ($\tau_{i⁢n⁢i}$), elongation ($\tau_{e⁢l}$), and termination ($\tau_{t⁢e⁢r}$) times. Each of these reaction times are determined by the translation factor abundances. On average, the elongation step is repeated around $⟨ℓ⟩≈200\times$ to complete a full protein, compared to 1 × for initiation and termination. Our framework of flux optimization under proteome allocation constraint addresses what ribosome and translation factor abundances maximize growth rate. (B) Measured expression hierarchy of bacterial mRNA translation factors, conserved across evolution. Horizontal bars mark the proteome synthesis fractions as measured by ribosome profiling (Lalanne et al., 2018) (equal to the proteome fraction by weight for a stable proteome) for key mRNA translation factors in B. subtilis (Bsub), E. coli (Ecol), and V. natriegens (Vnat) and are color-coded according to the protein (or group of proteins) specified. Triangles (◂) on the right indicate the mean synthesis fraction of the protein in the three species. See Table 1 for a short description of the translation factors considered. Synthesis fractions in (B) can be found in Supplementary file 1.

**Table 1.**
 Brief description of the function of core translation factors considered.For reviews of mRNA translation, see Rodnina, 2018; Chen et al., 2016.


<table>
  <thead>
    <tr>
      <th>Step</th>
      <th>Factor</th>
      <th>Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Initiation</td>
      <td>IF1</td>
      <td>Initiation factor 1: binds to 30S ribosome subunits to facilitate initiator tRNA binding (Laursen et al., 2005; Gualerzi and Pon, 2015).</td>
    </tr>
    <tr>
      <td>Initiation</td>
      <td>IF2</td>
      <td>Initiation factor 2: ribosome-dependent GTPase interacting with 30 ribosome subunits, ensures correct binding of initiator tRNAs (Laursen et al., 2005; Gualerzi and Pon, 2015).</td>
    </tr>
    <tr>
      <td>Initiation</td>
      <td>IF3</td>
      <td>Initiation factor 3: prevents premature docking of 50S ribosomal subunits (Laursen et al., 2005; Gualerzi and Pon, 2015).</td>
    </tr>
    <tr>
      <td>Elongation</td>
      <td>EF-Tu</td>
      <td>Elongation factor Tu: binds to charged tRNAs to form ternary complexes, brings charged tRNAs to empty ribosome A sites. (Weijland et al., 1992; Agirrezabala and Frank, 2009; Andersen et al., 2003)</td>
    </tr>
    <tr>
      <td>Elongation</td>
      <td>aaRS</td>
      <td>tRNA synthetases: charge tRNAs with cognate amino acids (Ibba and Soll, 2000; Pang et al., 2014).</td>
    </tr>
    <tr>
      <td>Elongation</td>
      <td>EF-G</td>
      <td>Elongation factor G: catalyzes translocation steps of the ribosome after peptide bond formation (Andersen et al., 2003; Agirrezabala and Frank, 2009).</td>
    </tr>
    <tr>
      <td>Elongation</td>
      <td>EF-Ts</td>
      <td>Elongation factor Ts: nucleotide exchange factor for EF-Tu (Agirrezabala and Frank, 2009; Andersen et al., 2003).</td>
    </tr>
    <tr>
      <td>Termination</td>
      <td>RF1/RF2</td>
      <td>Peptide chain release factors 1 and 2: recognize stop codon and hydrolyze the completed protein. RF1 recognizes UAA, UAG, and RF2 UAA, UGA (Bertram et al., 2001).</td>
    </tr>
    <tr>
      <td>Termination</td>
      <td>RF4</td>
      <td>Ribosome recycling factor: catalyzes the dissociation of ribosome subunits following peptide chain release in translation termination (Bertram et al., 2001).</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Compilation of predicted optimal abundances for translation factors.The optimal abundance is the sum of the terms in each row. Columns correspond to contributions of different nature (diffusion of factor itself, diffusion of other factors involved in the factor’s cycle, catalytic term). Terms must be multiplied by the common factors indicated in each column’s header (∝). For RF1+RF2, $\delta:=2⁢\sqrt{f_{U⁢A⁢G}⁢f_{U⁢G⁢A}}$ (see section Optimal abundances for RF1/RF2).


<table>
  <thead>
    <tr>
      <th>Factor</th>
      <th>Diffusion (direct) ∝λ*P</th>
      <th>Diffusion (other) ∝λ*P</th>
      <th>Catalytic sequestration ∝λ*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IF1</td>
      <td>ℓr⁢i⁢b⁢o⁢ℓI⁢F⁢1⟨ℓ⟩⁢k^o⁢nI⁢F⁢1⁢[1+ℓI⁢F⁢2+ℓI⁢F⁢3ℓr⁢i⁢b⁢o]</td>
      <td>ℓI⁢F⁢1⟨ℓ⟩⁢⟨ℓ⟩k^o⁢n50⁢S</td>
      <td>ℓI⁢F⁢1⟨ℓ⟩⁢(1kR⁢N⁢A+1kc⁢a⁢ti⁢n⁢i)</td>
    </tr>
    <tr>
      <td>IF2</td>
      <td>34⁢ℓr⁢i⁢b⁢o⁢ℓI⁢F⁢2⟨ℓ⟩⁢k^o⁢nI⁢F⁢2</td>
      <td>ℓI⁢F⁢2⟨ℓ⟩⁢(ℓr⁢i⁢b⁢o⁢ℓI⁢F⁢1⟨ℓ⟩⁢k^o⁢nI⁢F⁢1+⟨ℓ⟩k^o⁢n50⁢S)</td>
      <td>ℓI⁢F⁢2⟨ℓ⟩⁢(1kR⁢N⁢A+1kc⁢a⁢ti⁢n⁢i)</td>
    </tr>
    <tr>
      <td>IF3</td>
      <td>34⁢ℓr⁢i⁢b⁢o⁢ℓI⁢F⁢3⟨ℓ⟩⁢k^o⁢nI⁢F⁢3</td>
      <td>ℓI⁢F⁢3⟨ℓ⟩⁢(ℓr⁢i⁢b⁢o⁢ℓI⁢F⁢1⟨ℓ⟩⁢k^o⁢nI⁢F⁢1+⟨ℓ⟩k^o⁢n50⁢S)</td>
      <td>ℓI⁢F⁢3⟨ℓ⟩⁢(1kR⁢N⁢A+1kc⁢a⁢ti⁢n⁢i)</td>
    </tr>
    <tr>
      <td>EF-G</td>
      <td>ℓr⁢i⁢b⁢o⁢ℓGk^o⁢nG</td>
      <td></td>
      <td>ℓGkc⁢a⁢tG</td>
    </tr>
    <tr>
      <td>EF-Ts</td>
      <td>ℓT⁢u⁢ℓT⁢sk^o⁢nT⁢s</td>
      <td></td>
      <td>ℓT⁢skc⁢a⁢tT⁢s</td>
    </tr>
    <tr>
      <td>EF-Tu</td>
      <td>ℓr⁢i⁢b⁢o⁢ℓT⁢u⁢na⁢ak^o⁢nT⁢C</td>
      <td>ℓT⁢u⁢ℓT⁢sk^o⁢nT⁢s</td>
      <td>ℓT⁢u⁢(1kc⁢a⁢tT⁢C+1kc⁢a⁢tT⁢s)</td>
    </tr>
    <tr>
      <td>RF1+RF2</td>
      <td>ℓr⁢i⁢b⁢o⁢ℓR⁢F⁢I⁢(1+δ)⟨ℓ⟩⁢k^o⁢nR⁢F⁢I</td>
      <td></td>
      <td>ℓR⁢F⁢I⟨ℓ⟩⁢kc⁢a⁢tR⁢F⁢I</td>
    </tr>
    <tr>
      <td>RF4</td>
      <td>ℓr⁢i⁢b⁢o⁢ℓR⁢F⁢4⟨ℓ⟩⁢k^o⁢nR⁢F⁢4</td>
      <td></td>
      <td>ℓR⁢F⁢4⟨ℓ⟩⁢kc⁢a⁢tR⁢F⁢4</td>
    </tr>
  </tbody>
</table>

## Results

### Problem statement and model formulation

Our overall goal is to determine the growth-optimizing proteome allocation for the core translation factors. Conceptually, varying tlF concentrations has two opposing effects on cell proliferation. At the biochemical level, high tlF expression can facilitate growth by allowing more efficient usage of ribosomes. At the systems level, increased tlF expression can nonetheless limit growth by reducing the number of ribosomes and other proteins that can be produced. The tradeoffs between various tlFs and ribosomes create a multidimensional optimization problem.

We solve this multidimensional problem by treating translation as a dynamical system, in which ribosomes cycle through initiation, elongation, and termination. The resulting flux drives cell growth. During steady-state growth, every interlocked step of the translation cycle must have the same ribosome flux that is specified by the growth rate. We show that at the growth optimum, concentrations for distinct tlFs can be solved independently. The resulting analytical solutions can be expressed in terms of the growth rate and simple biophysical parameters.

### Cell growth driven by tlF-dependent ribosome flux

To describe the biochemical effects of tlF concentrations on cell growth, we first introduce a coarse-grained translation cycle time $\tau_{t⁢l}$, or the time it takes for a ribosome to complete a typical cycle of protein synthesis (Figure 1A), which consists of three sequential steps: initiation ('$i⁢n⁢i$'), elongation ('$e⁢l$'), and termination ('$t⁢e⁢r$'). Each of these steps is catalyzed by multiple tlFs. The full translation cycle time is then sum of ribosome transit times at the three steps ($\tau_{t⁢l}=\tau_{i⁢n⁢i}+\tau_{e⁢l}+\tau_{t⁢e⁢r}$), whose dependence on individual tlF concentrations can be quantitatively described through mass action kinetic schemes (schematically depicted in Figure 1A, see Appendices 2, 3, and 4 for details and examples below). We express tlF concentrations in units of proteome fractions (dry mass fraction of a specified protein to the full proteome), denoted by $ϕ$ (Scott et al., 2010) (Materials and methods, section Conversion between concentration and proteome fraction). Using this notation, the translation cycle time $\tau_{t⁢l}$ is a decreasing function of various tlFs concentrations (${ϕ_{t⁢l⁢F,i}}$).

In addition to its dependency on tlF concentrations, the translation cycle time provides a bridge between the cell growth rate and ribosome concentration. In steady-state growth (Monod, 1949; Scott et al., 2010; Dai et al., 2016), the growth rates of cells and of their protein content (total number of proteins) must be identical, denoted here as λ, as a result of the constant average cellular composition. The protein content grows at a rate determined by the flux of active ribosomes completing the translation cycle, that is $N_{r⁢i⁢b⁢o}^{a⁢c⁢t}/\tau_{t⁢l}$, where $N_{r⁢i⁢b⁢o}^{a⁢c⁢t}$ is the number of active ribosomes per cell, divided by the total number of proteins $N_{P}$ per cell: $\lambda=N_{r⁢i⁢b⁢o}^{a⁢c⁢t}/\tau_{t⁢l}⁢N_{P}$. Active ribosomes are defined as those functionally engaged in, and cycling through, the initiation, elongation, and termination reactions of peptide synthesis. Rescaling to the total mass fraction (Materials and methods, section Conversion between concentration and proteome fraction) of proteome for active ribosomes ($ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}$) yields

$$
\lambda=\frac{ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}}{\tau_{t⁢l}}⁢\frac{⟨ℓ⟩}{ℓ_{r⁢i⁢b⁢o}},
$$

where $ℓ_{r⁢i⁢b⁢o}$ is the number of amino acids in ribosomal proteins and $⟨ℓ⟩$ is the average number of codons per protein, weighted by expression levels (Materials and methods, section Average number of codons per protein: $⟨ℓ⟩$). The rescaling factor ($ℓ_{r⁢i⁢b⁢o}/⟨ℓ⟩≈7300/200=36.5$) is approximately constant across growth conditions (Matrials and methods, section Average number of codons per protein: $⟨ℓ⟩$). This equation establishes how tlF concentrations affect the growth rate biochemically via $\tau_{t⁢l}$.

We note that Equation 1 is a generalized form of the bacterial growth law that relates the mass fraction of elongating ribosomes to growth rate ($\lambda=\frac{ϕ_{r⁢i⁢b⁢o}^{e⁢l}}{\tau_{e⁢l}}⁢\frac{⟨ℓ⟩}{ℓ_{r⁢i⁢b⁢o}}=\gamma⁢ϕ_{r⁢i⁢b⁢o}^{e⁢l}$, where γ is a rescaled translation elongation rate and $ϕ_{r⁢i⁢b⁢o}^{e⁢l}$ is the proteome fraction of actively translating ribosomes [Scott et al., 2010; Dai et al., 2016; Scott et al., 2014]). This classic growth law was derived by considering the steady-state flux of peptide bond formation by elongating ribosomes, whereas our model focuses on the flux of ribosomes that traverse the entire translation cycle, thereby allowing us to consider the effects of translation factors and ribosomes engaged in additional steps (initiation, elongation, and termination). For each step, Equation 1 can be extended to show that the growth rate is similarly proportional to the mass fraction of the corresponding ribosomes divided by the transit time at that step (Materials and methods, section Equality of ribosome flux in steady-state).

Steady-state growth thus imposes the requirement that the growth rate be inversely proportional to the translation cycle time and proportional to the number of active ribosomes engaged in the translation cycle (Equation 1). Inactive ribosomes, comprised of assembly intermediates, hibernating ribosomes, or otherwise non-functional ribosomes, have been found to constitute a small fraction (≈5%) of the total ribosome pool for fast growth (Lindahl, 1975; Dai et al., 2016). Based on Equation 1, both increasing ribosome concentration and increasing tlF concentrations (which decreases $\tau_{tl}$) can accelerate growth. However, production of ribosomes and tlFs is subject to competition under a limited proteomic space, which we consider next.

### Optimization under proteome allocation constraint

To model the production cost tradeoff between tlFs and ribosomes, we integrate the flux-based formulation above with a proteomic constraint. Assuming that components of the translation machinery together accounts for a fixed fraction of proteome, that is, the ‘translation sector’ $ϕ_{t⁢l}$ (denoted $ϕ_{R}$ in the context of growth laws [Scott et al., 2010]), the proteome fraction for active ribosomes is related to the proteome fraction for translation factors via

$$
ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}=ϕ_{t⁢l}-ϕ_{r⁢i⁢b⁢o}^{i⁢n⁢a⁢c⁢t}-\sumiϕ_{t⁢l⁢F,i}.
$$

Equations 1 and 2, together with to the kinetic schemes for each step of the translation cycle, constitute the core of our model. Combining the biochemical effects (Equation 1) and the systems-level constraints (Equation 2) on tlFs, we arrive at a self-contained relationship between growth and tlF concentrations:

$$
\lambda=\frac{ϕ_{t⁢l}-ϕ_{r⁢i⁢b⁢o}^{i⁢n⁢a⁢c⁢t}-\sum_{i}ϕ_{t⁢l⁢F,i}}{\tau_{t⁢l}⁢({ϕ_{t⁢l⁢F,i}})}⁢\frac{⟨ℓ⟩}{ℓ_{r⁢i⁢b⁢o}},
$$

where we explicitly express $\tau_{t⁢l}$ as a function of $ϕ_{t⁢l⁢F,i}$ to reflect the dependence of ribosome transit times on translation factor abundances. The above relationship (Equation 3) allows us to ask: what is the stoichiometry of tlFs, or partitioning of the translation sector, that maximizes the growth rate (Figure 1A)?

The condition for the optimal TF abundances, that is, the set of $ϕ_{t⁢l⁢F,i}$ that satisfies $(\partial⁡\lambda/\partial⁡ϕ_{t⁢l⁢F,i})^{*}=0$, can be obtained by considering the $ϕ_{t⁢l⁢F,i}$ as independent variables and taking the derivative of Equation 3 with respect to a specified tlF abundance. Under the assumptions that the translation sector ($ϕ_{t⁢l}$) and the proteome fraction for inactive ribosomes ($ϕ_{r⁢i⁢b⁢o}^{i⁢n⁢a⁢c⁢t}$) are both fixed in a given external nutrient condition, this yields

$$
(\frac{\partial⁡\tau_{t⁢l}}{\partial⁡ϕ_{t⁢l⁢F,i}})^{*}=-\frac{⟨ℓ⟩}{ℓ_{r⁢i⁢b⁢o}}⁢\frac{1}{\lambda^{*}},
$$

where the asterisk refers to the growth optimum within our model, that is, $(\partial⁡\lambda/\partial⁡ϕ_{t⁢l⁢F,i})^{*}=0$. Hence, under this framework, the tlF abundances are growth-optimized when the sensitivity of the translation cycle time to changing the considered tlF abundance ($\partial⁡\tau_{t⁢l}/\partial⁡ϕ_{t⁢l⁢F,i}$) reaches a value determined solely by the growth rate and protein size factors. We emphasize that the derivative above corresponds to a perturbation scenario in which the tlF abundance is changed while maintaining fixed the total proteomic resources to the translation sector, as prescribed by our optimization procedure. As such, it does not correspond an actual perturbation easily realizable experimentally.

Although Equation 3 and the resulting optimization conditions (Equation 4, one for every tlF) corresponds to a coupled nonlinear system of multiple $ϕ_{t⁢l⁢F,i}$, substantial decoupling occurs at the optimal growth rate. In this situation, most $ϕ_{t⁢l⁢F,i}$ are only connected through the resulting growth rate. The optimization problem is then further simplified by the fact that the translation cycle consists of sequential and largely independent steps. The translation cycle time $\tau_{t⁢l}$ corresponds to the sum of the coarse-grained initiation, elongation, and termination times, that is, $\tau_{t⁢l}=\tau_{i⁢n⁢i}+\tau_{e⁢l}+\tau_{t⁢e⁢r}$. Given that each tlF is involved in a specific molecular step, the sensitivity matrix of these times to tlF concentration is sparse: $(\partial⁡\tau_{j}/\partial⁡ϕ_{t⁢l⁢F,i})^{*}=0$ for most combinations of $\tau_{j}$ and $ϕ_{t⁢l⁢F,i}$. This lack of ‘cross-reactivity’ expresses that, for example, the initiation time $\tau_{i⁢n⁢i}$ is unaffected by the tRNA synthetase concentration. This sparsity only occurs at the optimal expression levels, as the transit times typically depend on the growth rate (see an example in section Non binding-limited regime [one stop codon]) and $\partial⁡\lambda/\partial⁡ϕ_{t⁢l⁢F,i}\neq0$ away from the optimum. The optimum condition for factor $i$ then simplifies to:

$$
(\frac{\partial⁡\tau_{j}}{\partial⁡ϕ_{t⁢l⁢F,i}})^{*}=-\frac{⟨ℓ⟩}{ℓ_{r⁢i⁢b⁢o}}⁢\frac{1}{\lambda^{*}},
$$

where $j$ above denotes the translation step(s) that tlFi participates in. This leads to simplifications that allow the system to be solved analytically in most cases: instead of solving the full system at once, individual reactions within the translation cycle can be considered in isolation. The resulting optimal concentrations are connected via the growth rate $\lambda^{*}$. Interestingly, the optimal stoichiometry among most tlFs is independent of $\lambda^{*}$ if the reactions are in the binding-limited regime, as we show below.

### Case study: Translation termination

We first illustrate the process of solving for the optimal tlF concentration for the relatively simple case of translation termination. The principles used here and the form of solutions provide conceptual guideposts for solving other steps of the translation cycle.

In bacteria, translation termination (Bertram et al., 2001) consists of two distinct, sequential steps: (1) stop codon recognition and peptidyl-tRNA hydrolysis catalyzed by class I peptide chain release factors RF1 and RF2, followed by (2) dissociation of ribosomal subunits from the mRNA, that is, ribosome recycling, catalyzed by RF4. We do not explicitly consider the additional factors (e.g. RF3 and EF-G) due to their lack of conservation or because they are non-limiting for this specific step (Appendix 2, section Omitted molecular details). RF1 and RF2 have the same molecular functions but recognize different stop codons (Scolnick et al., 1968): RF1 recognizes stops UAA and UAG, whereas RF2 recognizes UAA and UGA. For simplicity, we describe here a scenario where RF1 and RF2 have no specificity towards the three stop codons, which allows us to combine them in a single factor (denoted RFI). The model is readily generalized, with similar results, to the case of the two RFs with their specificity towards the three stop codons (Appendix 2, section Full three stop codons model).

Under a coarse-grained description, the total ribosome transit time at termination $\tau_{t⁢e⁢r}$ can be decomposed into a sum of peptide release time and ribosome recycling time. In the treatment below, we consider a regime of binding-limited reactions for simplicity (rapid catalytic rate). A full model with catalytic components can also be solved analytically (Appendix 2, section Non binding-limited regime (one stop codon), Figure 2A). In the binding-limited regime ($k_{c⁢a⁢t}→∞$), the peptide release time and ribosome recycling time are inversely proportional to the corresponding tlF concentrations:

$$
\tau_{t⁢e⁢r}=\frac{1}{k_{o⁢n}^{R⁢F⁢I}⁢ϕ_{R⁢F⁢I}}+\frac{1}{k_{o⁢n}^{R⁢F⁢4}⁢ϕ_{R⁢F⁢4}},
$$

where the association rate constants $k_{o⁢n}^{i}$ are rescaled by the factor’s sizes in proteome fraction units (Materials and methods, section Conversion between concentration and proteome fraction). The above expression constitutes the solution of the mass action scheme for termination, connecting factor abundances to termination time.

![Figure 2.](https://cdn.elifesciences.org/articles/69222/elife-69222-fig2-v2.jpg)

**Figure 2.:** (A) Coarse-grained translation termination scheme. (B) Illustration of the minimization of effective proteome fraction corresponding to peptide chain release factors, leading to the equipartition principle.

The termination time (Equation 6) can then be directly substituted into the optimality condition (Equation 5) and solved in terms of $\lambda^{*}$:

$$
ϕ_{R⁢F⁢I}^{*}=\sqrt{\frac{ℓ_{r⁢i⁢b⁢o}⁢\lambda^{*}}{⟨ℓ⟩⁢k_{o⁢n}^{R⁢F⁢I}}},ϕ_{R⁢F⁢4}^{*}=\sqrt{\frac{ℓ_{r⁢i⁢b⁢o}⁢\lambda^{*}}{⟨ℓ⟩⁢k_{o⁢n}^{R⁢F⁢4}}}.
$$

If the reactions are not binding-limited, an additional catalytic term $∝\lambda^{*}/k_{c⁢a⁢t}$ is added to the minimally required levels above (Appendix 2, section Non binding-limited regime [one stop codon]). The square-root dependence in the optimal RF concentrations emerges from the $ϕ_{i}^{-1}$ dependence of $\tau_{i}$, for example, for ribosome recycling $\tau_{r⁢e⁢c⁢y⁢c}∝ϕ_{R⁢F⁢4}^{-1}$, which becomes $(ϕ_{i}^{*})^{-2}$ upon taking the derivative in the optimality condition (Equation 5). The square root is then obtained by solving for $ϕ_{i}^{*}$. A similar square-root dependence has been noted in optimization of the ternary complex and tRNA abundances (Ehrenberg and Kurland, 1984; Berg and Kurland, 1997). Analysis of tlF expression across slower growth conditions supports the derived square root dependence (Figure 4—figure supplement 2). As a result of the square-root, the optimal RF concentrations are weakly affected by biophysical properties such as the association rate constants and protein sizes. In the binding-limited regime above, the ratio of the optimal concentrations between RFI and RF4 is independent of the growth rate and only depends on the kinetics of binding.

As a side note, the expression for termination time $\tau_{t⁢e⁢r}$ in Equation 6 must be modified in a regime where ribosomes are frequently queued upstream of stop codons. This would occur if the termination rate were slow and approached initiation rates on mRNAs (Bergmann and Lodish, 1979; Lalanne et al., 2021). In this regime, queues of ribosomes at stop codons would incur an additional time to terminate. In a general description, the resulting additional termination time can be absorbed in a queuing factor $𝒬:\tau_{ter}^{full}:=\tau_{ter} 𝒬(\tau_{ter})$ (Appendix 1 for derivation and discussion). The resulting nonlinearity would forbid the decoupling in the optimization procedure between RFI and RF4. Although absolute rates of termination are difficult to measure in vivo, translation on mRNAs is generally thought to be limited at the initiation step (Laursen et al., 2005), and consistently, ribosome queuing at stop codons in bacteria is not usually observed (except under severe perturbations, e.g. Kavčič et al., 2020; Baggett et al., 2017; Mangano et al., 2020; Saito et al., 2020; Lalanne et al., 2021). In the physiological regime of fast termination, the queuing factor converges to 1, yielding simple solutions that depend only on biophysical parameters (Equations 7).

### Equipartition between tlF and corresponding ribosomes

The optimal tlF concentrations (e.g. Equation 7) can also be intuitively derived from another viewpoint. For each reaction in the translation cycle, we can define an effective proteome fraction allocated to that process, combining the proteome fractions of the corresponding tlF and the ribosomes waiting at that specific step. As an example, for the case of peptide chain release factor (RFI) just treated, the effective proteome fraction includes the release factors and ribosomes with completed peptides waiting at stop codons (dashed box in Figure 2A), that is, $ϕ_{R⁢F⁢I}^{e⁢f⁢f}:=ϕ_{R⁢F⁢I}+ϕ_{r⁢i⁢b⁢o}^{s⁢t⁢o⁢p}$. This effective proteome fraction corresponds to the total proteomic space associated to a tlF in the context of the translation cycle.

During steady-state growth, the concentration of ribosomes waiting at any specific step of the translation cycle is equal to the total active ribosome concentration multiplied by the ratio of the transit time of that step to the full cycle: for example, here $ϕ_{r⁢i⁢b⁢o}^{s⁢t⁢o⁢p}=\frac{\tau_{s⁢t⁢o⁢p}}{\tau_{t⁢l}}⁢ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}$, where $\tau_{s⁢t⁢o⁢p}=1/(k_{o⁢n}^{R⁢F⁢I}⁢ϕ_{R⁢F⁢I})$ is the time to arrival of RFI. Using Equation 1 for $ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}$, the effective proteome fraction satisfies:

$$
ϕ_{RFI}^{eff}:=ϕ_{RFI}+ϕ_{ribo}^{stop}=ϕ_{RFI}+\frac{1}{ϕ_{RFI}}\frac{\lambda}{k_{on}^{RFI}}\frac{ℓ_{ribo}}{⟨ℓ⟩}\geq2\sqrt{\frac{\lambda}{k_{on}^{RFI}}\frac{ℓ_{ribo}}{⟨ℓ⟩}}.
$$

In the last line, we used the inequality of arithmetic and geometric means ($a+b\geq2⁢\sqrt{a⁢b}$) to obtain the minimum of the effective proteome fraction. The equality holds when the two proteome fractions are equal ($ϕ_{R⁢F⁢I}=ϕ_{r⁢i⁢b⁢o}^{s⁢t⁢o⁢p}$), which provides the solution for optimal $ϕ_{R⁢F⁢I}$:

$$
ϕ_{R⁢F⁢I}^{*}=\sqrt{\frac{ℓ_{r⁢i⁢b⁢o}⁢\lambda^{*}}{⟨ℓ⟩⁢k_{o⁢n}^{R⁢F⁢I}}},
$$

Hence, we recover Equation 7 by minimizing the effective proteome fraction allocated to a given process in the translation cycle (the above argument applies to the optimal free concentration in the non-binding limited regime, see Appendix 2, section Non binding-limited regime (one stop codon) for an example). From this perspective, optimization of the translation apparatus balances the production cost of the enzyme of interest with the improved efficiency of a having less ribosomes idle at that step, Figure 2B. The optimal abundance in our model corresponds to a point of equipartition: the proteome fraction of free cognate factors equals the proteome fraction of ribosomes waiting at the corresponding step (Figure 2B).

### Case study: Ternary complex and tRNA cycle (EF-Tu and aaRS)

We next consider a more complex step of the translation cycle – elongation – and demonstrate that the optimality criterion (Equation 5) can similarly provide simple analytical solutions in the physiologically relevant regime. Translation elongation involves multiple interlocked cycles (one for each chemical species) and enzymes (EF-Tu, EF-G, EF-Ts, aminoacyl-tRNA synthetases (aaRS), and more). Our simplified kinetic scheme for translation elongation is shown in Figure 3A: charged tRNAs are brought to ribosomes through a ternary complex (TC), corresponding to a bound tRNA and EF-Tu. Following tRNA delivery and GTP hydrolysis, EF-Tu is released from the ribosome, and nucleotide exchange factor EF-Ts recycles EF-Tu back into the active pool, after which EF-Tu can bind a charged tRNA again and form another TC. At the ribosome, translocation to the next codon is catalyzed by EF-G, followed by release of uncharged tRNAs. Aminoacyl-tRNA synthetases then charge tRNAs to complete the elongation cycle.

![Figure 3.](https://cdn.elifesciences.org/articles/69222/elife-69222-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of the translation elongation scheme, with the tRNA cycle, involving aminoacyl-tRNA synthetases (aaRS) and EF-Tu. Reactions with a # have their association rate constants rescaled by a factor of $n_{a⁢a}^{-1}≈1/20$ through our coarse-graining to a single codon model. Greyed out cycles (EF-Ts and EF-G) can be solved in isolation (Appendix 3, sections Optimal EF-Ts abundance and Optimal EF-G abundance). (B) Exploration of the aaRS/EF-Tu expression space from numerical solution of the elongation model (Appendix 3, section Optimal EF-Tu and aaRS abundances). The transition line (orange) marks the boundary between the EF-Tu limited and aaRS limited regimes. Left panel shows the ternary complex concentration (which is closely related to the elongation rate, Equation 10). The ternary complex concentration is scaled by the dissociation constant $K_{T⁢C}$ to the ribosome A site (see Equation 39). Middle panel shows the free charged tRNA fraction. Right panel shows the free EF-Tu fraction ($ϕ_{T⁢u^{G⁢T⁢P}}$ denotes the proteome fraction of EF-Tu GTP that can bind to charged tRNAs to form the ternary complex). The star marks the optimal solution, as described in the text.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/69222/elife-69222-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Geometrical interpretation of the sharpness of the separation of the aaRS limited and EF-Tu limited regimes. Each graph corresponds to a different combination of aaRS and EF-Tu abundance. The solution for $ϕ_{T⁢C}$ (yellow circle) corresponds to the intersection of the full (tRNA budget minus TC concentration and ribosome bound tRNAs) and dashed (all remaining tRNA contributions) black lines. Red and pink lines correspond to the free uncharged and charged tRNAs respectively. Because of the rapid divergence of the free charged tRNA term (red) at $ϕ_{T⁢C}=ϕ_{T⁢u}$, the system shifts from being limited by aaRS-limited (pink line intersecting full black line) to being EF-Tu limited (red line intersect full black line) over a very narrow range in aaRS or EF-Tu expression change. The central graph corresponds to the abundance of EF-Tu and aaRS matched (no unbound charged tRNAs or EF-Tu), and falls on the transition line of Figure 3.

To reduce the complexity due to different tRNA isoacceptors and aaRSs, we self-consistently coarse-grained the translation elongation cycle to have a single codon (derived in Appendix 3, section Coarse-grained one-codon model). The resulting model harbors a single effective species for tRNA, aaRSs, and TCs, respectively. A rescaling factor ($1/n_{a⁢a}≈1/20$, estimated in section Estimation of coarse-grained rates) arises in the procedure to decrease the rates of codon specific reactions and can be attached to either the respective rate constants or chemical species concentrations. In our formulation, we choose to rescale the association rate constants such that the coarse-grained abundance for each effective species corresponds to the sum over all individual codon-specific components. For example, $ϕ_{a⁢a⁢R⁢S}$ in our coarse-grained model corresponds to the summed proteome fraction of all aaRSs in the cell, and its association rate constant with the total tRNAs is rescaled by a factor of $1/n_{a⁢a}$.

As a result of this choice of rescaling within our coarse-grained model, there are two classes of reactions in the elongation cycle that are distinguished by different kinetics: those that were codon specific (scaled by $1/n_{a⁢a}$) and those that are not. Codon-specific reactions, for example, aaRS binding to cognate tRNAs and TC binding to cognate codons, are coarse-grained into one-codon reactions with reduced association rate constants (marked by # in Figure 3A). By contrast, codon-agnostic reactions do not incur such a rescaling and are thus much faster. We refer to this as a separation of timescale between the two classes of reactions (codon-specific vs. codon-agnostic), and note that this is not a reflection of slower underlying microscopic bimolecular reaction rates, but rather a result of our choice of variable in the coarse-graining.

Similar to translation termination, the factor-dependent ribosome transit time through a single codon ($\tau_{a⁢a}$) is comprised of two steps, corresponding to binding of the TC and EF-G, respectively (formal derivation and non binding-limited regime in Appendix 3, section Coarse-grained translation elongation time):

$$
\tau_{a⁢a}=\frac{1}{\frac{k_{o⁢n}^{T⁢C}}{n_{a⁢a}}⁢ϕ_{T⁢C}}+\frac{1}{k_{o⁢n}^{G}⁢ϕ_{G}}.
$$

The coarse-grained factor-dependent portion of the total translation elongation time in our model is then given by the single codon time above multiplied by the average number of codons per protein, that is, $⟨ℓ⟩⁢\tau_{a⁢a}$. As discussed above, the rescaling of the TC association rate constant by $n_{a⁢a}^{-1}$ arises as a result of our coarse-graining to a one-codon model (Appendix C, section C.1 Coarse-grained one-codon model). Note that the ternary complex concentration, $ϕ_{T⁢C}$, is a nonlinear function of the concentrations of all elongation factors (including $ϕ_{G}$).

Despite the complexity of $\tau_{a⁢a}$ as a function of the $ϕ_{t⁢l⁢F,i}$, the fact that all fluxes are equal in steady-state allows several steps to be isolated and solved separately (EF-Ts and EF-G, greyed out in Figure 3A, respectively solved in Appendix C, sections C.3.3 Optimal EF-Ts abundance and C.3.4 Optimal EF-G abundance). For example, the approximate binding-limited solution for optimal EF-G concentration parallels that for termination factors:

$$
ϕ_{G}^{*}≈\sqrt{\frac{ℓ_{r⁢i⁢b⁢o}⁢\lambda^{*}}{k_{o⁢n}^{G}}}.
$$

Importantly, the optimum for EF-G is larger than the optimum for RFs by a factor $\sqrt{⟨ℓ⟩}$, reflecting that the typical translation cycle to produce a protein requires $⟨ℓ⟩$ steps catalyzed by EF-G and only one step for RFs (i.e. $⟨ℓ⟩⁢\tau_{a⁢a}$ enters the optimality condition, Equation 5, in contrast to $\tau_{t⁢e⁢r}$ which is not multiplied by a scaling factor). The square root dependence arises here for the same reason as in the case of translation termination (derivative of $ϕ^{-1}$).

In contrast to EF-G and EF-Ts, EF-Tu and aaRS cannot a priori be treated in isolation because the TC is composed of both EF-Tu and charged tRNAs. Still, the separation of timescales within our coarse-grained model (see Appendix C, section Interpretation of the sharp separation between aaRS and EF-Tu limited regimes) simplifies the solution considerably. Indeed, rapid binding of charged tRNAs to EF-Tu leads to either component being limiting for ternary complex concentration in most of the aaRS/EF-Tu expression space, leading to two clearly delineated regimes (Figure 3B). In one regime, charged tRNAs are limiting (low aaRS), whereas EF-Tu is limiting in the other (low EF-Tu). These regimes are separated by a narrow transition region, whose sharpness is a reflection of the smallness of the rate rescaling parameter $n_{a⁢a}^{-1}$ (see Appendix 3, section Interpretation of the sharp separation between aaRS and EF-Tu limited regimes). We term the focal region separating the two regimes in the aaRS/EF-Tu expression space the 'transition line’ (see 1 for derivation and additional details).

The transition line corresponds to conditions in which EF-Tu and aaRS are co-limiting for TC concentration. In the EF-Tu limited region, increasing aaRS abundance does not increase ternary complex concentration: since all EF-Tu proteins are already bound to charged tRNAs, increasing tRNA charging cannot further increase TC concentration. Conversely, in the aatRNA limited region, increasing EF-Tu abundance does not increase TC concentration: since all charged tRNAs are already bound by EF-Tu, increasing EF-Tu concentration does not alleviate the requirement for more charged tRNAs. Given that the optimality condition requires non-zero increase in ternary complex concentration with increasing factor abundance (Equation 5 using $\tau_{a⁢a}$ from Equation 10), the optimal EF-Tu and aaRS abundances must be on the transition line.

Which point on the transition line corresponds to the optimum? Note that inside the EF-Tu limited region, the ternary complex concentration is entirely set by the total EF-Tu concentration: $ϕ_{T⁢C}≈ϕ_{T⁢u}$ (since most EF-Tu proteins are bound by charged tRNAs, Figure 3—figure supplement 1). As an approximation resulting from the narrow range of transition region (Figure 3 and Figure 3—figure supplement 1), we assume that the EF-Tu limited regime solution $ϕ_{T⁢C}≈ϕ_{T⁢u}$ holds up to very close to the transition line. Replacing $ϕ_{T⁢C}$ by $ϕ_{T⁢u}$ in the elongation time Equation 10 and substituting in the optimality condition (Equation 5), the approximate optimal abundance for EF-Tu (the full solution includes additional terms from the EF-Ts cycle, section Optimal EF-Tu and aaRS abundances) can then be obtained in the same way as for translation termination factors:

$$
ϕ_{T⁢u}^{*}≈\sqrt{\frac{ℓ_{r⁢i⁢b⁢o}⁢n_{a⁢a}⁢\lambda^{*}}{k_{o⁢n}^{T⁢C}}}.
$$

Importantly, compared to the solution for EF-G, the above is multiplied by an additional factor of $\sqrt{n_{a⁢a}}$. This contribution arises from the rescaling of the association rate for the ternary complex to the ribosome in our coarse-grained one-codon model, increasing the requirement on EF-Tu abundance.

From the necessity for the combined EF-Tu and aaRS solution to fall on the transition line, the approximate solution for the optimal aminoacyl-tRNA synthetase abundance is then the intersection (yellow star in Figure 3B) of the transition line with the EF-Tu-only solution described above (dashed blue line in Figure 3B, derivation of solution in Box 1).

For the above derivation to be valid, the total number of tRNAs in the cell must be sufficient to accommodate all ribosomes (about two per ribosome, A- and P-sites) and binding to all EF-Tu (about gt4 per ribosome based on endogenous expression stoichiometry [Li et al., 2014; Lalanne et al., 2018]). The number of tRNAs per ribosomes in the cell should thus be at least 6×. Remarkably, estimates of this ratio in the cell suggest that this is barely the case (between 6 and 7 tRNAs/ribosome at fast growth [Dong et al., 1996]). Although our model treats the total tRNA abundance as a measured parameter and omits its selective pressure (see Hu et al., 2020 which includes RNA mass in their optimization procedure), the abundance of three core components of the tRNA cycle appear to be at the special point where the transition line plateau, that is set by total tRNA abundance, just crosses the EF-Tu-only optimum (blue line in Figure 3B). At this point, all three components are co-limiting.

### Optimal stoichiometry of mRNA translation factors

Analogous to the case studies above, optimal concentrations for all core translation factors can be solved using the optimality condition (Equation 5) and their respective kinetics schemes (the case of translation initiation is solved in Appendix 4). The analytical forms of the optimal solutions are shown in Table 1. In the binding-limited regime, the ratios of growth-optimized tlF concentrations are independent of the growth rate (except for aaRS), and are dependent only on basic biophysical parameters, such as protein sizes and diffusion constants.

To obtain the numerical values of association rate constants needed for calculating the optimal tlF stoichiometry (Table 1), we used the measured $k^_{o⁢n}^{T⁢C}$ in vivo and estimated all other association rate constants using a biophysically motivated scaling ($k^$ denotes the raw association rate constant in units µM−1s−1, which is different from the rescaled $k$, see section Conversion between concentration and proteome fraction). To our knowledge, the binding between TC and ribosomes, $k^_{on}^{TC}=6.4$ µM−1s−1 (Dai et al., 2016), is the only measured association rate constant for any tlFs in a physiological context. We estimate the association rate constants for other reactions by scaling $k^_{o⁢n}^{T⁢C}$ by the respective diffusion coefficients of the chemical species, that is for reaction involving species $A$ and $B: k^_{on}^{AB}/k^_{on}^{TC}=(D_{A}+D_{B})/(D_{TC}+D_{ribo})$, where $D_{i}$ is the diffusion constant for the molecular species $i$ (see Appendix 5—table 2). Diffusion constants for several tlFs have been measured experimentally (Bakshi et al., 2012; Sanamrad et al., 2014; Plochowietz et al., 2017; Volkov et al., 2018), and uncharacterized ones can be estimated using the cubic-root scaling with number of codons per protein from the Stokes-Einstein relation (Nenninger et al., 2010) (see Appendix 5—table 1). For simplicity, this approach assumes that reactive radii and orientational constraints are similar for the different reactions (see 3 Discussion for additional assumptions). These strong assumptions are necessary given the lack of in vivo biochemical parameter measurements, and can be relaxed as refined empirical determination for more physiological association rates become available in the future. Nonetheless, we note that the square-root dependence on these parameters (Table 1) for our predictions makes the numerical values less sensitive to possible tlF-specific effects.

The estimated optimal tlF concentrations show concordance with the observed ones, both in terms of the absolute levels and the stoichiometry among tlFs (Figure 4 for fast growth, see Supplementary file 1 for data and Figure 4—figure supplement 1 for additional growth conditions). A hierarchy of expression levels emerges such that the factors involved in elongation are more abundant compared to initiation and termination factors. The separation of these two classes is driven by the scaling factor $\sqrt{⟨ℓ⟩}≈14$ in our analytical solutions, which reflects the fact that the flux for elongation factors is $⟨ℓ⟩≈200$ times higher than that for initiation and termination factors. Within each class, the finer hierarchy of expression levels can also be further explained by simple parameters. For example, EF-Tu is predicted to be more abundant than EF-G by a factor of $\sqrt{n_{a⁢a}⁢ℓ_{T⁢u}/ℓ_{G}}≈3.3$ (observed $ϕ_{T⁢u}/ϕ_{G}$: E. coli 3.9, B. subtilis 2.7, V. natriegens 3.3). A higher abundance is required for EF-Tu because it is bound to the different tRNAs, which effectively decreases the concentration by a factor of $n_{a⁢a}≈20$ (see section Estimation of coarse-grained rates for derivation and discussion of why the factor is not equal to the number of different tRNAs). Taken together, our model offers straightforward explanations for the observed tlF stoichiometry.

![Figure 4.](https://cdn.elifesciences.org/articles/69222/elife-69222-fig4-v2.jpg)

**Figure 4.:** Predicted optimal abundance (no catalytic contribution, $k_{c⁢a⁢t}→∞$) versus observed abundance.Measured proteome fractions are the average of E. coli, B. subtilis, V. natriegens (Lalanne et al., 2018). We note that given the sensitivity of the optimal aaRS abundance on the total tRNA/ribosome ratio (visually: yellow star’s position in Figure 3B moves rapidly along x-axis upon changes in plateau of transition line), the prediction for aaRS should be interpreted with caution. Data and predicted values can be found in Supplementary file 1 and 2.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/69222/elife-69222-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Measured (ribosome profiling) and predicted (diffusion-limited estimates) proteome fraction for core translation factors in individual conditions corresponding to different ribosome profiling datasets included in our analysis (see Supplementary files 1–4). Doubling time for each condition is indicated. (A) Individual fast growing species (see Figure 4 for the average). (B) Slower growth conditions in E. coli. (C) C. crescentus datasets. Predictions of aaRS in species other than E. coli are marked by # to indicate that we used E. coli tRNA abundance measurements from Dong et al., 1996 to make prediction for this tlF these other species.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/69222/elife-69222-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Expression stoichiometry of core translation factors in different species and at different growth rates. (A) Comparison of measured (ribosome profiling) proteome fraction for core translation factors across different species and growth conditions (same conditions as Figure 4—figure supplement 1). All conditions are compared to the E. coli RDM dataset (reference: $r⁢e⁢f$, condition of interest: $i$). Dotted line correspond to $ϕ_{i}=ϕ_{r⁢e⁢f}$, dashed line to $ϕ_{i}=(\lambda_{i}/\lambda_{r⁢e⁢f})⁢ϕ_{r⁢e⁢f}$ and full black line to $ϕ_{i}=\sqrt{\lambda_{i}/\lambda_{r⁢e⁢f}}⁢ϕ_{r⁢e⁢f}$ (the parameter free prediction from the binding-limited regime of the model, optimal abundance $∝\sqrt{\lambda}$). Orange line corresponds to the one parameter fit $log⁡ϕ_{i}=\alpha_{i}+log⁡ϕ_{r⁢e⁢f}$ (excluding aaRS, not expected to follow the square root scaling, and ribosomes), corresponding to the scaling of all factor’s abundance. (B) Best one-parameter fit $\alpha_{i}$ (scale factor) from (A) as a function of the growth rate ratio $\lambda_{i}/\lambda_{r⁢e⁢f}$. Square root scaling: full line. Linear scaling: dashed line. Uncertainties on the growth ratio are propagated from uncertainties of the respective growth rates. Uncertainties in $\alpha_{i}$ are 95% confidence interval from the linear fits in (A).

For a few tlFs, the observed concentrations are two- to fivefold higher than the predicted optimal levels (e.g. EF-Ts, RF4, and IF1 in Figure 4). A potential explanation is that the corresponding reactions may not be binding or diffusion-limited, which would lead to a non-negligible fraction of tlFs sequestered at the catalytic step and thereby require higher total concentrations. Indeed, recent detailed modeling of the EF-Ts (Hu et al., 2020) cycle estimated only a small fraction (6% to 48%) of its abundance was in the free form in the cell, consistent with the large deviation we observe for this factor from our diffusion only prediction. Our optimization model can also be solved analytically in the non-binding-limited regime (Table 1), with the finite catalytic rate leading to an additional contribution of the form $∝ℓ⁢\lambda^{*}/k_{c⁢a⁢t}$. However, the numerical values for these solutions are in general difficult to obtain because the estimates for catalytic rates are sparse and often inconsistent with estimates of kinetics in live cells. As an example, median estimated aaRS catalytic rates (Jeske et al., 2019) measured in vitro is ≈3 s−1, well below the minimal value of 15 s−1, required to sustain translation flux at the measured value (Appendix 5), suggesting substantial deviation between in vitro and in vivo kinetics. While technically demanding, the fraction of free vs. bound factors can in principle be determined through live cell microscopy of tagged factors by partitioning the diffusive states of the tagged enzyme. Using that approach, Volkov et al., 2018 estimated that EF-Tu was in its bound state <10% of the time (consistent with our diffusion-limited prediction closed to the observed value for this factor).

Another potential explanation for the observed deviations from our predictions is that the selective pressure for these tlFs may be lower compared to the more highly expressed tlFs. This explanation is unlikely both because their stoichiometry are observed to be conserved (Figure 1B, Figure 4—figure supplement 2) and given that the expression of other lowly expressed tlFs (e.g. RF1, RF2, and individual aaRSs) has been shown to acutely affect cell growth (Lalanne et al., 2021; Parker et al., 2020). Nevertheless, the deviations from the predicted optimal levels suggest that a more refined model may be required than our first-principles derivation.

## Discussion

Despite the comprehensive characterization of their molecular mechanisms, the ‘mixology’ for the protein synthesis machineries inside living cells has remained elusive. Here, we establish a first-principles framework to provide analytical solutions for the growth-optimizing concentrations of translation factors. We find reasonable agreements between our parameter-free parsimonious predictions and the observed tlF stoichiometry (Figure 4). These results provide simple rationales for the hierarchy of expression levels, as well as insights into several construction principles for biological pathways.

An important implication from the agreement between observed stoichiometries and our predictions is that most tlFs are co-limiting for growth. Previous models have focused on expression optimization for the full translation sector, ribosomes (Scott et al., 2010; Belliveau et al., 2021), and the abundant elongation factors EF-Tu (Ehrenberg and Kurland, 1984; Klumpp et al., 2013). In a recent study, Hu and colleagues considered additional RNA components and EF-Ts in their optimization procedure (Hu et al., 2020). In line with the conclusions of these previous studies, our results demonstrate that multiple components of the translation machinery, regardless of their observed expression level, are simultaneously co-limiting for cell growth. By virtue of the interlocked translation cycles at steady state, the flux through every cycle must be matched. In our model, the optimality occurs when there are just enough tlFs to support the required flux in every cycle, such that the proteome fraction of free factors equals that of waiting ribosomes at that step (equipartition). If the concentration of any one tlF falls below the optimal point, it becomes the limiting factor for protein synthesis and growth. This result is supported by experimental evidence that slight knockdowns of individual RFs and aaRSs are detrimental to growth (Parker et al., 2020; Lalanne et al., 2021). Figuratively, the translation apparatus is analogous to a vulnerable supply chain, in which slowdown in any of the steps affects the full output.

In the binding-limited regime, the optimal tlF stoichiometry is independent of the specific growth rate (except for aaRS). This is consistent with the observation that relative tlF expression remains unchanged in E. coli in conditions with doubling times ranging from 20 min to 2 hr (Lalanne et al., 2018; Li et al., 2014; Figure 4—figure supplement 2A).

Our results are also consistent with the maintenance of the relative tlF expression across large phylogenetic distances even though the underlying regulation and cellular physiology has diverged (Lalanne et al., 2018; Figure 1B, and additional comparison to slow growing C. crescentus in Figure 4—figure supplement 2A). Under the assumption of diffusion-limited association to estimate parameters, the optimal tlF stoichiometry depends only on simple biophysical parameters, including protein sizes and diffusion constants, that are likely conserved in distant species. It remains to be determined if similar biophysical principles apply to the other pathways that also exhibit conserved enzyme expression stoichiometry.

In principle, our model can also make predictions on the growth defects at suboptimal tlF concentrations. However, experimentally testing these predictions will be difficult due to secondary effects of gene regulation that are not considered in our model near optimality. For example, we have recently shown that small changes in RF levels lead to idiosyncratic induction of the general stress response in B. subtilis due to a single ultrasensitive stop codon (Lalanne et al., 2021). As a result, the growth defect not only arises from reduced translation flux, but is in fact dictated by spurious regulatory connections that are normally not activated when tlF expression is at the optimum. We propose that tlF expression may be set at the optimal levels as our first-principles model suggests but entrenched by connections in the regulatory network. To predict the full expression-to-fitness landscape away from the optimum, a more comprehensive model may be required to take into account all the molecular interactions in the cell (Karr et al., 2012; Macklin et al., 2020).

Our coarse-graining approach has several limitations in its connection to detailed biochemical parameters. Foremost, coarse-grained association rate constants remain difficult to numerically estimate, and possibly neglect important features. In particular, given the sparsity of available in vivo rate constants, we estimate $k^_{o⁢n}$ for all tlFs reactions by scaling the measured TC association rate constant ($k^_{o⁢n}^{T⁢C}$) by the respective diffusion coefficients. This approach generates more plausible values than the unrealistic overestimate from Smoluchowski theory (diffusion-limited rate for perfectly absorbing spheres, see Appendix 5). However, the simplifying assumptions that certain molecular properties of modeled reactions are similar (e.g. the size of the reactive surfaces, orientational constraints of the bimolecular interaction, and possible non-cognate binding events) may have to be modified for more detailed models. We also do not explicitly consider off-rates in our model. Instead, our parameters correspond to effective rate constants that account for possible sequential binding and unbinding events, that is, $k~_{o⁢n}=k_{o⁢n}/n_{b⁢i⁢n⁢d}$, with $n_{b⁢i⁢n⁢d}=k_{c⁢a⁢t}/(k_{c⁢a⁢t}+k_{o⁢f⁢f})$. The effective association rate constants in our model thus contain information about catalytic and possible proofreading steps, which could be tlF-specific and are challenging to estimate. All these effects may contribute to the discrepancy between our predicted and observed tlF concentrations. As more physiological and molecular data become available, these tlF-specific features could be used to individually refine our estimate for the association rates constants and our predictions. For example, elaborate calculations from structural data could account for rotational constraints (Schlosshauer and Baker, 2004), but are beyond the scope of the present work. Overall, we expect these tlF-specific corrections to be of limited influence on the final predictions due to the square-root dependence of the optimal expression (Table 2). We further note that a number of conclusions from our model, such as the factor of $\sqrt{⟨ℓ⟩}$ separating the optimal abundances of elongation from initiation/termination tlFs, are generic and do not depend on the specific association rates.

Taken together, our model provides the biophysical basis for the stoichiometry of translation factors in living cells. The first-principles approach complements more comprehensive models that include many biochemical parameters (Hu et al., 2020; Vieira et al., 2016), while providing intuitive rationales for the expression hierarchy. We anticipate that our approach will be generalizable to elucidate or design enzyme stoichiometry of other biological pathways, especially those whose activities are required for cell growth.

## Materials and methods

### Average number of codons per protein: ⟨ℓ⟩

We calculate the average number of codons per protein, weighted by expression, as

$$
⟨ℓ⟩:=\frac{\sum_{i}e_{i}⁢ℓ_{i}}{\sum_{i}e_{i}},
$$

where $ℓ_{i}$ is the number of codon for the protein product of gene $i$, and ei is the protein synthesis rate (as estimated from ribosome profiling [Li et al., 2014; Lalanne et al., 2018]) for gene $i$. For a stable proteome (in fast growing bacteria, the cell doubling time is shorter than the active degradation of most proteins [Larrabee et al., 1980]), the protein synthesis rate equals to the proteome mass fraction (Li et al., 2014). Changes in the expression of genes across growth conditions do not lead to substantial changes in $⟨ℓ⟩$. In E. coli, across growth conditions spanning ≈20 min doubling time to ≈120 min, $⟨ℓ⟩$ changes by about 20%. Specifically, we find $⟨ℓ⟩=$ 196, 210, and 240 in respectively MOPS complete (≈20 min doubling time [Li et al., 2014]), MOPS minimal (≈56 min doubling time [Li et al., 2014]), and NQ1390 forced glucose limitation (≈120 min doubling time [Mori et al., 2021]), based on ribosome profiling data. Here for simplicity, we take $⟨ℓ⟩≈200$ throughout.

### Conversion between concentration and proteome fraction

Throughout, we use both units of concentration (molar), denoted as for example, $[A]$ for protein $A$, and proteome fraction, denoted by $ϕ_{A}$ (Scott et al., 2010). The correspondence between the two is $ϕ_{A}=[A]⁢ℓ_{A}/P$, where $ℓ_{A}$ is the number of amino acid in protein $A$, and $P$ is the in-protein amino acid concentration in the cell. $P≈2.6\times10^{6}$ µM, and has a value approximately independent of growth rate (Klumpp et al., 2013; Bremer and Dennis, 2008). This change in units also relates to how association constants are defined in units of proteome fraction: $k^_{o⁢n}⁢[A]:=k_{o⁢n}⁢ϕ_{A}$, where the hat $⋅^$ refers to the association constant in usual units of µM−1 s−1 (used to connect to empirical data). Hence, $k_{o⁢n}:=k^_{o⁢n}⁢P⁢ℓ^{-1}$ is the rescaled association rate in units of proteome fraction.

### Equality of ribosome flux in steady-state

In steady-state exponential growth, the ribosome flux in and out of each intermediate state is equal to the total flux. This results from the fact that no ribosome can accumulate in any intermediate state. Since the flux out of state $i$ is given by $ϕ_{r⁢i⁢b⁢o}^{i}/\tau_{i}$, we must have:

$$
\frac{\lambda⁢ℓ_{r⁢i⁢b⁢o}}{⟨ℓ⟩}=\frac{ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}}{\tau_{t⁢r⁢l}}=\frac{ϕ_{r⁢i⁢b⁢o}^{i⁢n⁢i}}{\tau_{i⁢n⁢i}}=\frac{ϕ_{r⁢i⁢b⁢o}^{e⁢l}}{\tau_{e⁢l}}=\frac{ϕ_{r⁢i⁢b⁢o}^{t⁢e⁢r}}{\tau_{t⁢e⁢r}}.
$$

As a consequence, the proportion of ribosome in each state is equal to the proportion of time spent at that given step, for example for translation initiation:

$$
\frac{ϕ_{r⁢i⁢b⁢o}^{i⁢n⁢i}}{ϕ_{r⁢i⁢b⁢o}^{a⁢c⁢t}}=\frac{\tau_{i⁢n⁢i}}{\tau_{i⁢n⁢i}+\tau_{e⁢l}+\tau_{t⁢e⁢r}}.
$$

### Protein production flux and growth rate

In order to write the mass action kinetic scheme for more complex models, it is useful to recast our framework in terms of the protein number production flux $J$, defined as the number of full length proteins produced per cell volume per unit time. The production of each protein requires a ribosome to go through the full synthesis cycle, and as such $J$ provides a convenient quantity in mass action schemes formulated in molar units.

In steady-state of exponential growth (Monod, 1949; Scott et al., 2010; Dai et al., 2016), there is a direct relationship between the growth rate λ (defined through $d⁢N/d⁢t=\lambda⁢N$, where $N$ is the number of cells per unit volume of culture) and the protein production flux $J$. Explicitly, the protein mass accumulation rate is $\lambda⁢M$, where $M$ is the total protein mass per unit volume of culture. If $V$ is the mean cell volume, then $\lambda⁢M/V=N⁢m_{a⁢a}⁢⟨ℓ⟩⁢J$, where $m_{a⁢a}$ is the mean amino acid mass. Defining $P:=M/(m_{a⁢a}⁢N⁢V)$, the in-protein amino acid concentration per cell (Materials and methods, section Conversion between concentration and proteome fraction), the connection between protein production flux $J$ and growth rate λ is then $J=\frac{P⁢\lambda}{⟨ℓ⟩}$. This relationship will be used to convert between molar and proteome fraction in some equations below.

### Summary of optimal solutions

Solutions for the factor predicted optimal abundances as a function of effective biochemical parameters and the growth rate at the optimum, are presented in Table 1. The table breaks down terms in each solution by categories: direct diffusion term (arising from diffusive search time), catalytic sequestration, and delay incurred by the diffusion of other proteins in part of the cycle of the factor of interest. Solutions are listed in terms of on-rate $k^_{o⁢n}$ (units of µM−1s−1). The aaRS solution follows a different form:

$$
ϕ_{aaRS}^{∗}=\frac{n_{aa}ℓ_{aaRS}\lambda^{∗}}{k^_{on}^{aaRS}PΔ_{tRNA}^{∗}}+\frac{ℓ_{aaRS}\lambda^{∗}}{k_{cat}^{aaRS}},with Δ_{tRNA}^{∗}:=\frac{tRNA_{tot}}{P}−\frac{\lambda^{∗}}{k_{on}^{TC}ϕ_{TC}^{∗}}−\frac{2\lambda^{∗}}{k_{el}^{max}}−\frac{ϕ_{TC}^{∗}}{ℓ_{Tu}}−\frac{\lambda^{∗}}{k_{cat}^{aaRS}},  and  ϕ_{TC}^{∗}:=\sqrt{\frac{n_{aa}ℓ_{ribo}ℓ_{Tu}\lambda^{∗}}{k^_{on}^{TC}P}}.
$$

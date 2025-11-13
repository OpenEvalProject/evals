# Probable nature of higher-dimensional symmetries underlying mammalian grid-cell activity patterns

## Authors

- Alexander Mathis<sup>1</sup> ([ORCID: 0000-0002-3777-2202](https://orcid.org/0000-0002-3777-2202)) †
- Martin B Stemmler<sup>3</sup>
- Andreas VM Herz<sup>3</sup>

### Affiliations

1. Department of Molecular and Cellular Biology Harvard University Cambridge United States
2. Center for Brain Science Harvard University Cambridge United States
3. Bernstein Center for Computational Neuroscience Munich Germany
4. Fakultät für Biologie Ludwig-Maximilians-Universität München Munich Germany

† Corresponding author

## Abstract

Lattices abound in nature—from the crystal structure of minerals to the honey-comb organization of ommatidia in the compound eye of insects. These arrangements provide solutions for optimal packings, efficient resource distribution, and cryptographic protocols. Do lattices also play a role in how the brain represents information? We focus on higher-dimensional stimulus domains, with particular emphasis on neural representations of physical space, and derive which neuronal lattice codes maximize spatial resolution. For mammals navigating on a surface, we show that the hexagonal activity patterns of grid cells are optimal. For species that move freely in three dimensions, a face-centered cubic lattice is best. This prediction could be tested experimentally in flying bats, arboreal monkeys, or marine mammals. More generally, our theory suggests that the brain encodes higher-dimensional sensory or cognitive variables with populations of grid-cell-like neurons whose activity patterns exhibit lattice structures at multiple, nested scales.

## Introduction

In mammals, the neural representation of space rests on at least two classes of neurons. ‘Place cells’ discharge when an animal is near one particular location in its environment (O'Keefe and Dostrovsky, 1971). ‘Grid cells’ are active at multiple locations that span an imaginary hexagonal lattice covering the environment (Hafting et al., 2005) and have been found in rats, mice, crawling bats, and human beings (Hafting et al., 2005; Fyhn et al., 2008; Yartsev et al., 2011; Jacobs et al., 2013). These cells are believed to build a metric for space.

In these experiments, locomotion occurs on a horizontal plane. Theoretical and numerical studies suggest that the hexagonal lattice structure is best suited for representing such a two-dimensional (2D) space (Guanella and Verschure, 2007; Mathis, 2012; Wei et al., 2013). In general, however, animals move in three dimensions (3D); this is particularly true for birds, tree dwellers, and fish. Their neuronal representation of 3D space may consist of a mosaic of lower-dimensional patches (Jeffery et al., 2013), as evidenced by recordings from climbing rats (Hayman et al., 2011). Place cells in flying bats, on the other hand, represent 3D space in a uniform and nearly isotropic manner (Yartsev and Ulanovsky, 2013).

As mammalian grid cells might represent space differently in 3D than in 2D, we study grid-cell representations in arbitrarily high-dimensional spaces and measure the accuracy of such representations in a population of neurons with periodic tuning curves. We measure the accuracy by the Fisher information (FI). Even though the firing fields between cells overlap, so as to ensure uniform coverage of space, we show how resolving the population's FI can be mapped onto the problem of packing non-overlapping spheres, which also plays an important role in other coding problems and cryptography (Shannon, 1948; Conway and Sloane, 1992; Gray and Neuhoff, 1998). The optimal lattices are thus the ones with the highest packing ratio—the densest lattices represent space most accurately. This remarkably simple and straightforward answer implies that hexagonal lattices are optimal for representing 2D space. In 3D, our theory makes the experimentally testable prediction that grid cells will have firing fields positioned on a face-centered-cubic lattice or its equally dense non-lattice variant—a hexagonal close packing structure.

Unimodal tuning curves with a single preferred stimulus, which are characteristic for place cells or orientation-selective neurons in visual cortex, have been extensively studied (Paradiso, 1988; Seung and Sompolinsky, 1993; Pouget et al., 1999; Zhang and Sejnowski, 1999; Bethge et al., 2002; Eurich and Wilke, 2000; Brown and Bäcker, 2006). This is also true for multimodal tuning curves that are periodic along orthogonal stimulus axes and generate repeating hypercubic (or hyper-rectangular) activation patterns (Montemurro and Panzeri, 2006; Fiete et al., 2008; Mathis et al., 2012). Our results extend these studies by taking more general stimulus symmetries into account and lead us to hypothesize that optimal lattices not only underlie the neural representation of physical space, but will also be found in the representation of other high-dimensional sensory or cognitive spaces.

### Model

#### Population coding model for space

We consider the D-dimensional space $ℝ^{D}$ in which spatial location is denoted by coordinates $x=(x_{1},…,x_{D})\inℝ^{D}$. The animal's position in this space is encoded by N neurons. The dependence of the mean firing rate of each neuron i on x is called the neuron's tuning curve and will be denoted by Ωi(x). To account for the trial-to-trial variability in neuronal firing, spikes are generated stochastically according to a probability $P_{i}(k_{i}|\tau Ω_{i}(x))$ for neuron i to fire ki spikes within a fixed time window τ. While two neurons can have correlated tuning curves Ωi(x), we assume that the trial-to-trial variability of any two neurons is independent of each other. Thus, the conditional probability of the N statistically independent neurons to fire (k1,…,kN) spikes at position x summarizes the encoding model:

$$
P((k_{1},…,k_{N})|x)=\prodi=1NP_{i}(k_{i}|\tau Ω_{i}(x)).
$$

Decoding relies on inverting this conditional probability by asking: given a spike count vector K = (k1,…,kN), where is the animal? Such a position estimate will be written as $x^(K)$. How precisely the decoding can be done is assessed by calculating the average mean square error of the decoder. The average distance between the real position of the animal x and the estimate $x^(K)$ is

$$
\epsilon(x^|x)=E_{P(K|x)}(∥x−x^(K)∥),
$$

given the population coding model $P(K|x)$. This error is called the resolution (Seung and Sompolinsky, 1993; Lehmann, 1998), whereby the term $∥.∥$ denotes Euclidean distance, $∥x∥=\sqrt{\sum\alpha x_{\alpha}^{2}}$. More generally, the covariance matrix $\sum(x^|x)$ with coefficients $\sum(x^|x)_{\alpha,\beta}=E_{P(K|x)}((x_{\alpha}−x_{\alpha}^(K))⋅(x_{\beta}−x_{\beta}^(K)))$ for spatial dimensions $\alpha,\beta\in{1,…,D}$, measures the covariance of the different error components, so that the sum of the diagonal elements of ∑ is just the resolution $\epsilon(x^|x)$. In principle, the resolution depends on both the specific decoder and the population coding model. However, for unbiased estimators, that is, estimators that on average decode the location x as this location $E_{P(K|x)}(x^(K))=x$, the FI provides an analytical measure to assess the highest possible resolution of any such decoder (Lehmann, 1998).

#### Resolution and Fisher Information

Given a response of K = (k1,…,kN) spikes across the population, we ask how accurately an ideal observer can decode the stimulus x. The FI measures how well one can discriminate nearby stimuli and depends on how P(x, K) changes with x. The greater the FI, the higher the resolution, and the lower the error $\epsilon(x^|x)$, as these two quantities are inversely related. More precisely, the inverse of the FI matrix J(x),

$$
J_{\alpha\beta}(x)=\int^{​}(\frac{\partial ln P(K,x)}{\partialx_{\alpha}})(\frac{\partial ln P(K,x)}{\partialx_{\beta}})P(K,x) dK,
$$

bounds the covariance matrix $\sum(x^|x)$ of the estimated coordinates x = (x1,…,xD)

$$
\sum(x^|x)\geqJ(x)^{−1}.
$$

The resolution of any unbiased estimator of the encoded stimulus can achieve cannot be greater than J(x)−1. This is known as the Cramér-Rao bound (Lehmann, 1998). Based on this bound, we will consider the FI as a measure for the resolution of the population code. In particular, we are interested in isotropic and homogeneous representations of space. These two conditions assure that the population has the same resolution at any location and along any spatial axis. Isotropy does not entail that the (global) spatial tuning of an individual neuron, Ωi(x), has to be radially symmetric, but merely that the errors are (locally) distributed according to a radially symmetric distribution. For instance, the tuning curve of a grid cell with hexagonal tuning is not radially symmetric around the center of a field (it has three axes), but the posterior is radially symmetric around any given location for a module of such grid cells. Homogeneity requires that the FI J(x) be asymptotically independent of x (as the number of neurons N becomes large); spatial isotropy implies that all diagonal entries in the FI matrix J(x) are equal.

#### Periodic tuning curves

Grid cells have periodic tuning curves—they are active at multiple locations, called firing fields, and these firing fields are hexagonally arranged in the environment (Hafting et al., 2005). Their periodic structure is given by a hexagonal lattice. The periodic structure of the tuning curve Ωi(x) reflects its symmetries, that is, the set of vectors that map the tuning curve onto itself. Since we want to understand how the periodic structure affects the resolution of the population code, we generalize the notion of a grid cell to allow different periodic structures other than just hexagonal. Mathematically, the symmetries of a periodic structure can be described by a lattice L, which is constructed as follows: take a set of independent vectors (vα)1≤α≤D in D-dimensional space ℝD, and consider all possible combinations of these vectors and their integer multiples—each such vector combination points to a node of the lattice, such that the union of these represents the lattice itself. For instance, the square lattice (Figure 1A, bottom) is given by basis vectors v1 = (1, 0) and v2 = (0, 1). Mathematically, the lattice L⊂ℝD is(5)L=∑α=1Dkαvαforkα∈ℤ, vα∈ℝD,for which (vα)1≤α≤D is a basis of ℝD. We will not consider degenerate lattices. In this work, we follow the nomenclature from Conway and Sloane (1992). Applied fields might differ slightly in their terminology, especially regarding naming conventions for packings, which are generalizations of lattices (Whittaker, 1981; Nelson, 2002). We will address these generalizations of lattices below.

![Figure 1.](https://cdn.elifesciences.org/articles/05979/elife-05979-fig1-v2.jpg)

**Figure 1.:** (A) Construction of a grid cell: Given a tuning shape Ω and a lattice $L$, here a square lattice generated by v1 and v2 with φ = π/2, one periodifies Ω with respect to $L$. One defines the value of $Ω^{L}(x)$ in the fundamental domain L as the value of Ω(r) applied to the distance from zero and then repeats this map over $ℝ^{2}$ like $L$ tiles the space. This construction can be used for lattices $L$ of arbitrary dimensions (Equation 7). (B) Grid module: The firing rates of three grid cells (orange, green, and blue) are indicated by color intensity. The cells' tuning is identical (Ω and $L$ are the same), yet they differ in their spatial phases ci. Together, such identically tuned cells with different spatial phases define a grid module.

Based on such a lattice $L$, we construct periodic tuning curves as illustrated in Figure 1A. We start with a lattice $L$ and a tuning shape $Ω:ℝ^{+}→[0,1]$ that decays from unity to zero; Ω(r) describes the firing rate of the periodified tuning curve at distance r from any lattice point and should be at least twice continuously differentiable. Each lattice point $p\inL$ has a domain $V_{p}⊂ℝ^{D}$ called the Voronoi region, which is defined as

$$
V_{p}={x\inℝ^{D} | ∥x−p∥<∥x−q∥ ∀q\inL ∧ p\neqq},
$$

that contains all points x that are closer to p than to any other lattice point q. Note that Vp ∩ Vq = ϕ if p ≠ q and that for all $p,q\inL$ there exists a unique vector $v\inL$ with Vp = Vq + v.

The domain that contains the null (0) vector is called the fundamental domain and is denoted by L:= V0. For each $x\inℝ^{D}$ there is a unique lattice point $p\inL$ that maps x into the fundamental domain: $x−p\inL$. Let us call this mapping $\pi_{L}$. With this notation one can periodify Ω onto $L$ by defining a grid cell's tuning curve as $Ω^{L}$:

$$
Ω^{L}(x):ℝ^{D}→ℝ^{+}, x↦f_{max}⋅Ω(∥\pi_{L}(x)∥^{2}),
$$

where fmax is the peak firing rate of the neuron. Note that throughout the paper we set fmax = τ = 1, for simplicity. As illustrated in Figure 1A, within the fundamental domain L, the tuning curve $Ω^{L}$ defined above is radially symmetric. This pattern is repeated along the nodes of $L$, akin to ceramic tiling.

A grid module is defined as an ensemble of M grid cells $Ω_{i}^{L}$, $i\in{1,…,M}$ with identical, but spatially shifted tuning curves, that is, $Ω_{i}^{L}(x)=Ω^{L+c_{i}}(x)$ and spatial phases $c_{i}\inL$ (see Figure 1B). The various phases within a module can be summarized by their phase density $ρ(c)=\sum^{​}_{i=1}^{M} \delta(c−c_{i})$. This definition is motivated by the observation of spatially shifted hexagonally tuned grid cells in the entorhinal cortex of rats (Hafting et al., 2005; Stensola et al., 2012).

Any grid module is uniquely characterized by its signature $(Ω,ρ,L)$. To investigate the role of different periodic structures, we can fix the tuning shape Ω and density ρ and solely vary the lattice $L$ to find the lattice that yields the highest FI.

## Results

To determine how the resolution of a grid module depends on the periodic structure L, we compute the population FI Jς(x) for a module of grid cells with signature ς=(Ω,ρ,L), which describes the tuning shape, the density of firing fields, and the lattice. By fixing the tuning shape Ω and the number |ρ|=M of spatial phases, we can compare the resolution for different periodic structures. (Table 1 contains a glossary of the variables.)

**Table 1.**
 List of acronyms, variables, and terms


<table>
  <tbody>
    <tr>
      <td>D</td>
      <td>Dimension of the stimulus space ℝD</td>
    </tr>
    <tr>
      <td>FI</td>
      <td>Fisher information, usually denoted by J (Equation 3)</td>
    </tr>
    <tr>
      <td>L</td>
      <td>Non-degenerate point lattice describing periodic structure (Equation 5)</td>
    </tr>
    <tr>
      <td>L</td>
      <td>Fundamental domain of L, which is the Voronoi cell containing 0 (Equation 6)</td>
    </tr>
    <tr>
      <td>Ω</td>
      <td>Tuning shape</td>
    </tr>
    <tr>
      <td>supp(Ω)</td>
      <td>Support of Ω, that is, the subset where Ω does not vanish</td>
    </tr>
    <tr>
      <td>ΩL</td>
      <td>Periodified tuning curve on ℝD, where L is a D-dimensional lattice and Ω a tuning curve. Simply referred to as a ‘grid cell’ (Equation 7)</td>
    </tr>
    <tr>
      <td>ρ</td>
      <td>Phase density of grid cells' phases ci within a module ρ(c)=∑​i=1Mδ(c−ci)</td>
    </tr>
    <tr>
      <td>M</td>
      <td>Number of phases in grid module ∫Lρ=M</td>
    </tr>
    <tr>
      <td>ς=(Ω,ρ,L)</td>
      <td>Signature defining a grid module, which is an ensemble of grid cells differing in spatial phases ci, defined by ρ and tuning curves given by ΩL</td>
    </tr>
    <tr>
      <td>det(L)</td>
      <td>Determinant of lattice L (equal to volume of L)</td>
    </tr>
    <tr>
      <td>BR(0)</td>
      <td>Subset of ℝD containing all points with distance less than R from 0</td>
    </tr>
    <tr>
      <td>Δ(L)</td>
      <td>Packing ratio of a lattice, that is, the volume of the largest BR(0) that fits inside L divided by det(L) (Equation 15)</td>
    </tr>
    <tr>
      <td>H, Q</td>
      <td>Hexagonal and square planar lattice of unit node-to-node distance (Figure 2)</td>
    </tr>
    <tr>
      <td>FCC, BCC, C</td>
      <td>Face-centered, body-centered, and cubic lattice of unit node-to-node distance, respectively (Figure 4).</td>
    </tr>
    <tr>
      <td>trJ</td>
      <td>Trace of the FI, that is, the sum of diagonal elements</td>
    </tr>
    <tr>
      <td>Jς</td>
      <td>Population FI of grid module with signature ς</td>
    </tr>
    <tr>
      <td>trJL, trJQ, trJH</td>
      <td>Trace of FI per neuron for lattice L (Q and H, respectively) with fixed bump-like Ω defined in Equation 26</td>
    </tr>
    <tr>
      <td>trJLM</td>
      <td>Trace of FI for lattice L for M randomly distributed phases in L for the same bump function</td>
    </tr>
  </tbody>
</table>

### Scaling of lattices and nested grid codes

Our grid-cell construction has one obvious degree of freedom, the length scale or grid size of the lattice $L$, that is, the width of the fundamental domain L. For a module with signature $ς=(Ω,ρ,L)$ and for arbitrary scaling factor λ > 0, the rescaled construction $\lambdaς:=(Ω(\lambdar),ρ(\lambdax),\lambda⋅L)$ is a grid module too. The corresponding tuning curve satisfies $(Ω∘\lambda)_{\lambdaL}(x)=Ω_{L}(\lambdax)$ and is thus merely a scaled version of the former. Indeed, as we show in the ‘Material and methods’ section, the FI of the rescaled module is λ−2 Jς(0). The Cramér-Rao bound (Equation 4) implies that the local resolution of an unbiased estimator could thus rapidly improve with a finer grid size, that is, decreasing λ.

However, for any grid module $ς=(Ω,ρ,L)$ the posterior probability, that is, the likelihood of possible positions given a particular spike count vector K = (k1,…,kN), is also periodic. This follows from Bayes rule:

$$
P(x|K)=\frac{P(K|x)⋅P(x)}{P(K)}∝P(x)\prodi=1NP_{i}(k_{i}|\tau Ω_{i}^{L}(x)).
$$

Since the right hand side is invariant under operations of $L$ on x, so is the left hand side of this equation. Thus, the multiple firing fields of a grid cell cannot be distinguished by a decoder, so that for λ → 0 the global resolution approaches the a priori uncertainty (Mathis et al., 2012a, 2012b). By combining multiple grid modules with different spatial periods one can overcome this fundamental limitation, counteracting the ambiguity caused by periodicity and still preserving the highest resolution at the smallest scale. Thus, one arrives at nested populations of grid modules, whose spatial periods range from coarse to fine. The FI for an individual module at one scale determines the optimal length scale of the next module (Mathis et al., 2012a, 2012b). The larger the FI per module, the greater the refinement at subsequent scales can be (Mathis et al., 2012a, 2012b). This result emphasizes the importance of finding the lattice that endows a grid module with maximal FI, but also highlights that the specific scale of the lattices can be fixed for this study.

### FI of a grid module with lattice L

We now calculate the FI for a grid module with signature $ς=(Ω,ρ,L)$. For cells whose firing is statistically independent (Equation 1), the joint probability factorizes; therefore, the population FI is just the sum over the individual FI contributions by each neuron, $J_{ς}(x)=\sum^{​}_{i=1}^{M} J_{Ω_{i}^{L}}(x)$. The individual neurons only differ by their spatial phase ci, thus $J_{Ω_{i}^{L}}(x)=J_{Ω^{L}}(x−c_{i})$. Consequently, $J_{ς}(x)=\sum^{​}_{i=1}^{M} J_{Ω^{L}}(x−c_{i})$, depends only on the function $J_{Ω^{L}}(r)$ and the deviations x − ci, where ci is the closest lattice point of $c_{i}+L$ to x. If the grid-cell density ρ is uniform across $L$, then for all $x\inℝ^{D}$: Jς(x) ≈ Jς(0). It therefore suffices to only consider the FI at the origin, which can be written as:

$$
J_{ς}(0)=\sumi=1MJ_{Ω^{L}}(c_{i})=\int_{L} J_{Ω^{L}}(c)ρ(c)dc.
$$

For uniformly distributed spatial phases ci and increasing number of neurons M, the law of large numbers implies

$$
limM→∞|\frac{det(L)}{M}J_{ς}(0)−\int_{L} J_{Ω^{L}}(c) dc|=0.
$$

Here, $det(L)$ denotes the volume of the fundamental domain. Thus, for large numbers of neurons $M=\int_{L} ρ(c)dc$ we obtain

$$
J_{ς}(0)≈\frac{M}{det(L)}\int_{L} J_{Ω^{L}}(c)dc.
$$

This means that the population FI at 0 is approximately given by the average FI within the fundamental domain L times the number of neurons M. Let us now assume that supp(Ω) = [0, R] for some positive radius R. Outside of this radius, the tuning shape is zero and the firing rate vanishes. So the spatial phases of grid cells that contribute to the FI at x = 0 lie within the ball BR(0). If we now also assume that this ball is contained in the fundamental domain, $B_{R}(0)⊂L$, we get

$$
\int_{L} J_{Ω^{L}}(c)dc=\int_{B_{R}(0)}J_{Ω^{L}}(c)dc.
$$

This result implies that any grid code $ς=(Ω,ρ,L)$, with large M, supp(Ω) = [0, R], and $B_{R}(0)⊂L$, satisfies

$$
J_{ς}(0)≈\frac{M}{det(L)}\int_{B_{R}(0)} J_{Ω^{L}}(c)dc.
$$

The FI at the origin is therefore approximately equal to the product of the mean FI contribution of cells within a R-ball around 0 and the number of neurons M, weighted by the ratio of the volume of the R-ball to the area of the fundamental domain L. Due to the radial symmetry of $Ω^{L}$, the FI matrix $J_{Ω^{L}}(c)$ is diagonal with identical entries, guaranteeing the spatial resolution's isotropy. The error for each coordinate axis is bounded by the same value, that is, the inverse of the diagonal element 1/Jς(0)ii, for such a population. Instead of considering the FI matrix Jς(0), we can therefore consider the trace of Jς(0), which is the sum over the diagonal of Jς(0). According to Equation 4, 1/trJς(0) bounds the mean square error summed across all dimensions $\epsilon(x^|x)$.

For two lattices $L_{1}$,$L_{2}$, with BR(0) ⊂ L1∩​L2 we consequently obtain

$$
\frac{trJ_{Ω^{L_{1}}}}{trJ_{Ω^{L_{2}}}}=\frac{det(L_{2})}{det(L_{1})},
$$

which signifies that the resolution of the grid module is inversely proportional to the volumes of their fundamental domains. The periodic structure $L$ thus has a direct impact on the resolution of the grid module. This result implies that finding the maximum FI translates directly into finding the lattice with the highest packing ratio.

### Packing ratio of lattices

The sphere packing problem is of general interest in mathematics (Conway and Sloane, 1992) and has wide-ranging applications from crystallography to information theory (Barlow, 1883; Shannon, 1948; Whittaker, 1981; Gray and Neuhoff, 1998; Gruber, 2004). When packing R-balls BR in ℝD in a non-overlapping fashion, the density of the packing is defined as the fraction of the space covered by balls. For a lattice L, it is given by(15)vol(BR(0))det(L),which is known as the packing ratio Δ(L) of the lattice. For a given lattice, this ratio is maximized by choosing the largest possible R, known as the packing radius, which is defined as the in-radius of a Voronoi region containing the origin (Conway and Sloane, 1992). Figure 2 depicts the disks with the largest in-radius for the hexagonal and the square lattice in blue and illustrates the packing ratio.

![Figure 2.](https://cdn.elifesciences.org/articles/05979/elife-05979-fig2-v2.jpg)

**Figure 2.:** Periodified grid-cell tuning curve $Ω^{L}$ for two planar lattices, (A) the hexagonal (equilateral triangle) lattice $H$ and (B) the square lattice $Q$, together with the basis vectors v1 and v2.These are π/3 apart for the hexagonal lattice and π/2 for the square lattice. The fundamental domain, that is, the Voronoi cell around 0, is shown in gray. A few other domains that have been generated according to the lattice symmetries are marked by dashed lines. The blue disk shows the disk with maximal radius R that can be inscribed in the two fundamental domains. For equal and unitary node-to-node distances, that is, $|v_{1}|=|v_{2}|=1$, the maximal radius equals 1/2 for both lattices. The packing ratio Δ is $Δ(H)=\pi/\sqrt{12}$ for the hexagonal and $Δ(Q)=\pi/4$ for the square lattice; the hexagonal lattice is approximately 15.5% denser than the square lattice.

### FI and packing ratio

We now come to the main finding of this study: among grid modules with different lattices, the lattice with the highest packing ratio leads to the highest spatial resolution.

To derive this result, let us fix a tuning shape Ω with supp(Ω) = [0, R], lattices $L_{j}$ such that BR(0) ⊂ Lj for 1 ≤ j ≤ K, and uniform densities ρ for each fundamental domain of equal cardinality M. Any linear order on the packing ratios,

$$
Δ(L_{1})\leq…\leqΔ(L_{j})\leq…\leqΔ(L_{K}) ,
$$

is translated by Equation 14 into the same order for the traces of the FI

$$
trJ_{Ω^{L_{1}}}\leq…\leqtrJ_{Ω^{L_{j}}}\leq…\leqtrJ_{Ω^{L_{K}}},
$$

and thus the resolution of these modules: the higher the packing ratio, the higher the FI of a grid module.

The condition supp(Ω) = [0, R] with BR(0) ⊂ L, although restrictive, is consistent with experimental observations that grid cells tend to stop firing between grid fields and that the typical ratio between field radius and spatial period is well below 1/2 (Hafting et al., 2005; Brun et al., 2008; Giocomo et al., 2011). Generally, the tuning width that maximizes the FI does not necessarily satisfy this condition; see Figures 3, 4, in which the optimal support radius of the tuning curve θ2 is greater than the in-radius R = 1/2 of L. The same observation will hold in higher dimensions (D > 2), consistent with the finding that the optimal tuning width for Gaussian tuning curves increases with the number of spatial dimensions, whether space is infinite (Zhang and Sejnowski, 1999) or finite (Brown and Bäcker, 2006). When the radius R of the support of the tuning curve exceeds the in-radius, the optimal lattice can be different from the densest one as we will show numerically for specific tuning curves and Poisson noise. However, with well separated fields, like those observed experimentally, the densest lattice provides the highest resolution for any tuning shape Ω, as we just demonstrated.

![Figure 3.](https://cdn.elifesciences.org/articles/05979/elife-05979-fig3-v2.jpg)

**Figure 3.:** (A) Top: Periodified bump-function Ω and square lattice $L$, for various parameter combinations θ1 and θ2. Here, θ1 modulates the decay and θ2 the support. Middle: Average trace $trJ_{L}$ of the Fisher information (FI) for uniformly distributed grid cells $Ω^{L}$. Hexagonal ($H$) and square ($Q$) lattices are considered for different θ1 and θ2 values. The FI of the hexagonal grid cells outperforms the quadratic grid when support is fully within the fundamental domain (θ2 < 0.5, see main text). Bottom: Ratio $trJ_{H}/trJ_{Q}$ as a function of the tuning parameter θ2. For θ2 < 0.5, the hexagonal population offers 3/2 times the resolution of the square population, as predicted by the respective packing ratios. (B) Average $trJ_{L}$ for grid cells distributed uniformly in lattices generated by basis vectors separated by an angle φ (basis depicted above graph). $trJ_{L}$ behaves like 1/sin(φ) and has its maximum at π/3. (C) Distribution of 5000 realizations of $trJ_{L}^{M}/M$ at 0 for a population of M = 200 randomly distributed neurons. For both the hexagonal and square lattice, parameters are θ1 = 1/4 and θ2 = 0.4. The means closely match the average values in (A). However, due to the finite neuron number the FI varies strongly for different realizations, and in about 20% of the cases a square lattice module outperforms a hexagonal lattice.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/05979/elife-05979-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Upper left panel: Tuning shape Ω(r) with parameters θ2 = 0.5 and varying θ1. Lower left panel: Corresponding Fisher information (FI) integrand $ℱ(r)$. Upper right panel: Tuning shape Ω(r) with parameters θ1 = 0.25 and varying θ2. Lower right panel: Corresponding FI integrand $ℱ(r)$.

![Figure 4.](https://cdn.elifesciences.org/articles/05979/elife-05979-fig4-v2.jpg)

**Figure 4.:** (A) The three lattices considered: face-centered cubic ($FCC$), body-centered cubic ($BCC$), and cubic ($C$). (B) $trJ_{L}$ for the periodified bump-function Ω for the three lattices and various parameter combinations θ1 and θ2. The Fisher information (FI) of the $FCC$ grid cells outperforms the other lattices when the support is fully within the fundamental domain (θ2 < 0.5, see main text). For larger θ2 the best lattice depends on the relation between the Voronoi cell's boundary and the tuning curve. (C) Ratio $trJ_{L}/trJ_{C}$ as a function of θ2 for $L\in{FCC,BCC,C}$. For θ2 < 0.5, the hexagonal population has 3/2 times the resolution of the square population, as predicted by the packing ratios. (D) Average $trJ_{L_{\phi,ψ}}$ for uniformly distributed grid cells within a lattice $L_{\phi,ψ}$ generated by basis vectors separated by angles φ and ψ (as shown above; θ1 = θ2 = 1/4). $trJ_{L_{\phi,ψ}}$ behaves like 1/(sinφ⋅sinψ) and has its maximum for the lattice with the smallest volume. (E) Distribution of 5000 realizations of $trJ_{L}^{M}/M$ at 0 for a population of M = 200 randomly distributed neurons. Parameters: θ1 = 1/4, θ2 = 0.4. The means closely match the averages in (B). Due to the finite neuron number, the FI varies strongly for different realizations.

The optimal packing ratio of lattices for low-dimensional space is well known. Having established our main result, we can now draw on a rich body of literature, in particular Conway and Sloane (1992), to discuss the expected firing-field structure of grid cells in 2D and 3D environments.

### Optimal 2D grid cells

With a packing ratio of $\pi/\sqrt{12}$, the hexagonal lattice is the densest lattice in the plane (Lagrange, 1773). According to Equation 14, the hexagonal lattice is the optimal arrangement for grid-cell firing fields on the plane. For example, it outperforms the quadratic lattice, which has a density of π/4, by about 15.5% (see Figure 2). Consequently, the FI of a grid module periodified along a hexagonal lattice outperforms one periodified along a square lattice by the same factor.

To provide a tangible example, we calculated the trace of the average FI per neuron $trJ_{ς}/\int_{L} ρ$ for signature $ς=(Ω,ρ,L)$ and chose the lattice $L$ to either be the hexagonal lattice $H$ or the quadratic lattice $Q$. We denote the trace of the average FI per neuron as: $trJ_{L}$ = $trJ_{ς}/\int_{L} ρ$; $trJ_{H}$ and $trJ_{Q}$ are similarly defined. We considered Poisson spike statistics and used a bump-like tuning shape Ω (Equation 26, ‘Materials and methods’ section). The tuning shape Ω depends on two parameters θ1 and θ2, where θ1 controls the slope of the flank in Ω and θ2 defines the support radius. The periodified tuning curve $Ω^{Q}$ is illustrated for different parameters in the top of Figure 3A and in Figure 3—figure supplement 1.

Figure 3A depicts $trJ_{H}$ and $trJ_{Q}$ for various values of θ1 and θ2. Quite generally, the FI is larger for grid modules with broad tuning (large θ2) and steep tuning slopes (small θ1). Figure 3A also demonstrates that as long as θ2 ≤ 1/2, $trJ_{H}$ consistently outperforms $trJ_{Q}$. But how large is this effect? As predicted by our theory, the grid module with the hexagonal lattice outperforms the square lattice by the relation of packing ratios $\sqrt{3}/2$, as long as the support radius θ2 is within the fundamental domain of the hexagonal and the square lattice of unit length, that is, θ2 ≤ 1/2 (bottom of Figure 3A). As the support radius becomes larger, the FI of the hexagonal lattice is no longer necessarily greater than that of the square lattice; the specific interplay of tuning curve and boundary shape determines which lattice is better: for θ1 = 1/4, $trJ_{H}/trJ_{Q}$ drops quickly beyond θ2 = 0.5, even though, for θ1 = 1, the ratio stays constant up to θ2 = 0.6.

Next we calculated the FI per neuron for a larger family of planar lattices generated by two unitary basis vectors with angle φ. Figure 3B displays $trJ_{L}$ for φ ∈ [π/3, π/2], slope parameter θ1 = 1/4, and different support radii θ2. For the lattice to have unitary length, the value φ cannot go below π/3. The $trJ_{L}$ decays with increasing angle φ. Indeed, according to Equation 13, the FI falls like $1/det L=1/sin(\phi)$ so that the maximum is achieved for the hexagonal lattice with π/3.

The FIs $trJ_{L}$ are averages over all phases, under the assumption that the density of phases tends to a constant; but are these values also indicative for small neural populations? To answer this question, we calculated the FI for populations with 200 neurons, as some putative grid cells are found in patches of this size (Ray et al., 2014). For M = 200 randomly chosen phases (Figure 3C), the mean of the normalized FI $trJ_{L}^{M}/M$ over 5000 realizations is well captured by the FI per neuron calculated in Figure 3A. Because of fluctuations in the FI, however, the square lattice is better than the hexagonal lattice in about 20% of the cases.

Our theory implies that for radially symmetric tuning curves the hexagonal lattice provides the best resolution among all planar lattices. This conclusion agrees with earlier findings: Wei et al. considered a notion of resolution defined as the range of the population code per smallest distinguishable scale and then demonstrated that a population of nested grid cells with hexagonal tuning is optimal for a winner-take-all and Bayesian maximum likelihood decoders (Wei et al., 2013). Guanella and Verschure numerically compared hexagonal to other regular lattices based on maximum likelihood decoding (Guanella and Verschure, 2007).

### Optimal lattices for 3D grid cells

Gauss proved that the packing ratio of any cubic lattice is bounded by $\pi/(3\sqrt{2})$ and that this value is attained for the face-centered cubic ($FCC$) lattice (Gauss, 1831) illustrated in Figure 4A. This implies that the optimal 3D grid-cell tuning is given by the $FCC$ lattice. For comparison, we also calculated the average population FI for two other important 3D lattices: the cubic lattice ($C$) and the body-centered cubic lattice ($BCC$), both shown in Figure 4A.

Keeping the bump-like tuning shape Ω and independent Poisson noise, we compared the resolution of grid modules with such lattices (Figure 4B). Their averaged trace of FI is denoted by $trJ_{FCC}$, $trJ_{BCC}$, and $trJ_{C}$, respectively. As long as the support θ2 of Ω is smaller than 1/2, the support is a subset of the fundamental domain of all three lattices. Hence, the trace of the population FI of the $FCC$ outperforms both the $BCC$ and $C$ lattices. As the ratios of the trace of the population FI scales with the packing ratio (Figure 4C), $FCC$-grid cells provide roughly 41% more resolution for the same number of neurons than do $C$-grid cells. Similarly, $FCC$-grid cells provide 8.8% more FI than $BCC$-grid cells.

Next we calculated the FI per neuron for a large family of cubic lattices $L_{\phi,ψ}$ generated by three unitary basis vectors with spanning angles φ and ψ. Figure 4D displays $trJ_{L_{\phi,ψ}}$ for θ1 = θ2 = 1/4 and various φ and ψ. The resolution $trJ_{L}$ decays with increasing angles and has its maximum for the lattice with the smallest volume as predicted by Equation 13.

To study finite-size effects, we simulated 5000 populations of 200 grid cells with random spatial phases. Qualitatively, the results (Figure 4E) match those in 2D (Figure 3C). Despite the small module size, $FCC$ outperformed the cubic lattice $C$ in all simulated realizations.

### Equally optimal non-lattice solutions for grid-cell tuning

Fruit is often arranged in an FCC formation (Figure 5A). One arrives at this lattice by starting from a layer of hexagonally placed spheres. This requires two basis vectors to be specified and is the densest packing in 2D. To maximize the packing ratio in 3D, the next layer of hexagonally arranged spheres has to be stacked as tightly as possible. There are two choices for the third and final basis vector achieve this packing, denoted as γ1 and γ2 in Figure 5B (modulo hexagonal symmetry). If one chooses γ1, then two layers below there is no sphere with its center at location γ1, but instead there is one at γ2 (and vice versa). This stacking of layers is shown in Figure 5C and generates the FCC lattice.

![Figure 5.](https://cdn.elifesciences.org/articles/05979/elife-05979-fig5-v2.jpg)

**Figure 5.:** (A) Stacking of spheres as in an $FCC$ lattice. In this densest lattice in 3D, each sphere touches 12 other spheres and there are four different planar hexagonal lattices through each node. (B) Over a layer of hexagonally arranged spheres centered at γ0 (in black) one can put another hexagonal layer by starting from one of six locations, two of which are highlighted, γ1 and γ2. (C) If one arranges the hexagonal layers according to the sequence (…,γ1, γ0, γ2,…) one obtains the $FCC$. Note that spheres in layer I are not aligned with those in layer III. (D) Arranging the hexagonal layers following the sequence (…,γ0, γ1, γ0,…) leads to the hexagonal close packing $HCP$. Again, each sphere touches 12 other spheres. However, there is only one plane through each node for which the arrangement of the centers of the spheres is a regular hexagonal lattice. This packing has the same packing ratio as the $FCC$, but is not a lattice. (E) $trJ_{L}$ for bump-function Ω with $L=FCC$ and $HCP$ for various parameter combinations θ1 and θ2; θ1 modulates the decay and θ2 the support. The two packings have the same packing ratio and for this tuning curve also provide identical spatial resolution. FI: Fisher information.

One could achieve the same density by choosing γ1 for both the top layer and the layer below the basis layer. Yet as this arrangement, called hexagonal close packing ($HCP$), cannot be described by three vectors, it does not define a lattice (see Figure 5D), even though it is as tightly packed as the $FCC$. Such packings, defined as an arrangement of equal non-overlapping balls (Conway and Sloane, 1992; Hales, 2012), generalize lattices.

While one can define a grid module for any lattice, as we showed above, one cannot define a grid module in a meaningful way for an arbitrary packing, due to the lack of symmetry. But for any given packing $P$ of $ℝ^{D}$ by balls $B_{1}$ of radius 1, one can define a ‘grid cell’ by generalizing the definition given for lattices (Equation 7). To this end, consider the Voronoi partition of $ℝ^{D}$ by $P$. For each location $x\inℝ^{D}$ there is a unique Voronoi cell Vp with node $p\inP$. One defines the grid cell's tuning curve $Ω^{P}(x)$ by assigning the firing rate according to $Ω(∥p−x∥^{2})$ for tuning shape Ω and distance $∥p−x∥$. Depending on the specific packing, this tuning curve $Ω^{P}$ may or may not be periodic. Because a packing $P$ often has fewer symmetries than a lattice $L$, the ‘grid cells’ in an arbitrary $P$ cannot generally be used to define a ‘grid module’. To explain why, consider an arbitrary packing and the unique Voronoi cell V0 that contains the point 0. Choose M uniformly distributed phases c1,…,cM within V0. Locations within V0 will then be uniformly covered by shifted tuning curves $Ω_{i}(x):=Ω^{P}(x−c_{i})$. However, typically the different Voronoi cells will neither be congruent, nor have similar volumes. Thus, the Ωi will typically not cover each Voronoi cell with the same density and will therefore fail to define a proper grid module. This problem does not exist for lattices. Here, the equivalence classes $c_{i}+L$ cover each cell with the same density.

Highly symmetric packings, on the other hand, do permit the definition of grid modules. For example, the hexagonal close packing $HCP$ can be used to define a grid cell $Ω^{HCP}(x)$. Using the same symmetry argument from Equations 9–11, implies for the FI:

$$
J_{(Ω,ρ,HCP)}(x)≈J_{(Ω,ρ,HCP)}(0)≈\frac{M}{vol(V_{0})}\int_{V_{0}} J_{Ω^{HCP}}(c)dc.
$$

The maximal in-radius R for the $HCP$ with grid size λ = 1 is equal to 1/2. Like for lattices, we assume that supp(Ω) = [0, R] and BR(0) ⊂ V0. Then the integrand vanishes for distances larger than 1/2 from 0. Hence, we obtain:

$$
J_{(Ω,ρ,HCP)}(0)≈\frac{M}{vol(V_{0})}\int_{B_{1/2}(0)} J_{Ω^{HCP}}(c)dc.
$$

Considering the same tuning shape Ω and number of phases M for an $FCC$ lattice, which also has maximal in-radius 1/2, Equation 13 gives us the following expression for the $FCC$ lattice:

$$
J_{(Ω,ρ,FCC)}(0)≈\frac{M}{det(FCC)}\int_{B_{1/2}(0)} J_{Ω^{FCC}}(c)dc.
$$

Since both fundamental domains have the same volumes, that is, $det(FCC)=vol(V_{0})$, and the integrands restricted to these balls are identical, that is, $J_{Ω^{FCC}}|_{B_{1/2}(0)}=J_{Ω^{HCP}}|_{B_{1/2}(0)}$, we can conclude that grid modules comprising $FCC$ or $HCP$-like symmetries have the same FI. We also numerically calculate the trace of the average FI for a module of $HCP$ grid cells and compare it to the $FCC$ case. For bump-like tuning curves Ω, both FIs are identical (Figure 5E) as expected from the radial symmetry of Ω. As a consequence, grid cells defined by either $HCP$ or $FCC$ symmetries provide optimal resolution.

Figure 5D,E shows that the cyclic sequences (γ0, γ1) and (γ1, γ0, γ2) lead to $HCP$ and $FCC$, respectively. The centers γ0, γ1, and γ2 can also be used to make a final point on packings: there are infinitely many distinct packings with the same density $\pi/(3\sqrt{2})$. They can be constructed by inequivalent words, generated by finitewalks through the triangle with letters γ0, γ1, and γ2 (Hales, 2012), with each letter representing one of three orientations for the layers. For instance, (γ0, γ1, γ0, γ2) describes another packing with the same density. All packings share one feature: around each sphere there are exactly 12 spheres, arranged in either $HCP$ or $FCC$ lattice fashion (Hales, 2012). These packings can also be used to define a grid module, because the density of phases will be uniform in all cells. Furthermore, as in the calculation of the FI for the $HCP$ and $FCC$ (Equation 18–20) only local integration was necessary, such mixed packings will have equally large, uniform FI as the pure $HCP$ or $FCC$ packings.

Only in recent years has it been proven that no other arrangement has a higher packing ratio than the $FCC$, a problem known as Kepler's conjecture (Hales, 2005, 2012). Based on these results and our comparison of $trJ_{HCP}$ and $trJ_{FCC}$ (Figure 5E), we predict that 3D grid cells will correspond to one of these packings. While there are equally dense packings as the densest lattice in 3D, this is not the case in 2D. Thue proved that the hexagonal lattice is unique in being the densest amongst all planar packings (Thue, 1910); grid cells in 2D should possess a hexagonal lattice structure.

## Discussion

Grid cells are active when an animal is near one of any number of multiple locations that correspond to the vertices of a planar hexagonal lattice (Hafting et al., 2005). We generalize the notion of a grid cell to arbitrary dimensions, such that a grid cell's stochastic activity is modulated in a spatially periodic manner within $ℝ^{D}$. The periodicity is captured by the symmetry group of the underlying lattice $L$. A grid module consists of multiple cells with equal spatial period but different spatial phases. Using information theory, we then asked which lattice offers the highest spatial resolution.

We find that the resolution of a grid module is related to the packing ratio of $L$—the lattice with highest packing ratio corresponds to the grid module with highest resolution. Well-known results from mathematics (Lagrange, 1773; Gauss, 1831; Conway and Sloane, 1992) then show that the hexagonal lattice is optimal for representing 2D, whereas the $FCC$ lattice is optimal for 3D. In 3D, but not in 2D, there are also non-lattice packings with the same resolution as the densest lattice (Thue, 1910; Hales, 2012). A common feature of these highly symmetric optimal solutions in 3D is that each grid field is surrounded by 12 other grid fields, arranged in either $FCC$ lattice or hexagonal close packing fashion. These solutions emerge from the set of all possible packings simply by maximizing the resolution, as we showed. However, resolution alone, as measured by the FI, does not distinguish between optimal packing solutions with different symmetries. Whether a realistic neuronal decoder, such as one based on population vector averages, favors one particular solution is an interesting open question.

As we have demonstrated, using the FI makes finding the optimal $L$ analytically tractable for all dimensions D and singles out densest lattices as optimal tuning shapes under assumptions that are restrictive, but are consistent with experimental measurements (Hafting et al., 2005; Brun et al., 2008; Giocomo et al., 2011). The assumption that the tuning curves must have finite support within the fundamental domain of the lattice corresponds to grid cells being silent outside of the firing field. Indeed, our numerical simulations also showed that for broader tuning curves, grid modules with quadratic lattices can provide more FI than the hexagonal lattice (Figure 3A, θ2 ≈ 0.6 and θ1 = 1/4) and that grid cells with a $C$ or $BCC$ lattice can provide more FI than the $FCC$ (Figure 4B, θ2 > 0.65 and θ1 = 1/4). For the planar case, Guanella and Verschure (2007) show numerically that triangular tessellations yield lower reconstruction errors under maximum-likelihood decoding than equivalently scaled square grids. Complementing this numerical analysis, Wei et al. (2013) provide a mathematical argument that hexagonal grids are optimal. To do so, they define the spatial resolution of a single module representing 2D space as the ratio R = (λ/l)2, where λ is the grid scale and l is the diameter of the circle in which one can determine the animal's location with certainty. For a fixed resolution R, the number of neurons required is N = d sin(φ) R in their analysis, where d is the number of tuning curves covering each point in space. As φ ∈ [π/3, π/2] for the lattice to have unitary length (Figure 3B), minimizing N for a fixed resolution R yields φ = π/3; thus, hexagonal lattices should be optimal. Furthermore, Wei et al. show that this result also holds when considering a Bayesian decoder (Wei et al., 2013). While Wei et al. minimize N for fixed l, we minimize l (in their notation). Like Wei et al., we assume that the tuning curve Ω is isotropic (notwithstanding the fact that the lattice has preferred directions); unlike these authors, we show that there are conditions under which the firing fields should be arranged in a square lattice, and not hexagonally.

Using the FI gives a theoretical bound for the local resolution of any unbiased estimator (Lehmann, 1998). In particular, this local resolution does not take into account the ambiguity introduced by the periodic nature of the lattice. Our analysis is restricted to resolving the animal's position within the fundamental domain. For large neuron numbers N and expected peak spike counts fmaxτ the resolution of asymptotically efficient decoders, like the maximum likelihood decoder, or the minimum mean square estimator, can indeed attain the resolution bound given by the FI (Seung and Sompolinsky, 1993; Bethge et al., 2002; Mathis et al., 2013). Thus, for these decoders and conditions the results hold. In contrast, for small neuron numbers and peak spike counts, the optimal codes could be different, just as it has been shown in the past that the optimal tuning width in these cases cannot be predicted by the FI (Bethge et al., 2002; Yaeli et al., 2010; Berens et al., 2011; Mathis et al., 2012).

Maximizing the resolution explains the observed hexagonal patterns of grid cells in 2D, and predicts an $FCC$ lattice (or equivalent packing) for grid-cell tuning curves of mammals that can freely explore the 3D nature of their environment. Quantitatively, we demonstrated that these optimal populations provide 15.5% (2D) and about 41% (3D) more resolution than grid codes with quadratic or cubic grid cells for the same number of neurons. Although better, this might not seem substantial, at least not at the level of a single grid module. However, as medial entorhinal cortex harbors a nested grid code with at least 5 and potentially 10 or more modules (Stensola et al., 2012), this translates into a much larger gain of $1.155^{5 … 10}≈2.1 … 4.2$ and $\sqrt{2}^{5 … 10}≈5.7 … 32$, respectively (Mathis et al., 2012a, 2012b). Because aligned grid-cell lattices with perfectly periodic tuning curves imply that the posterior is periodic too (compare Equation 8), information from different scales would have to be combined to yield an unambiguous read-out. Whether the nested scales are indeed read out in this way in the brain remains to be seen (Mathis et al., 2012a, 2012b; Wei et al., 2013). An alternative hypothesis, as first suggested by Hafting et al., is that the slight, but apparently persistent irregularities in the firing fields across space (Hafting et al., 2005; Krupic et al., 2015; Stensola et al., 2015) are being used. Future experiments should tackle this key question.

We considered perfectly periodic structures (lattices) and asked which ones provide most resolution. However, the first recordings of grid cells already showed that the fields are not exactly hexagonally arranged and that different fields might have different peak firing rates (Hafting et al., 2005). More recently, deviations from hexagonal symmetry have gained considerable attention (Derdikman et al., 2009; Krupic et al., 2013, 2015; Stensola et al., 2015). Such ‘defects’ modulate the periodicity of the tuning and consequently affect the symmetry of the likelihood function. This might imply that a potential decoder might be able to distinguish different unit cells even given a single module, which is not possible for perfectly periodic tuning curves (compare Equation 8). The local resolution, on the other hand, is robust to small, incoherent variations as the FI is a statistical average over many tuning curves with different spatial phases. At a given location, Equation 9 becomes

$$
J_{ς}(x)=\sumi=1MJ_{Ω_{i}^{L}}(x−c_{i})≈\int_{x−L}J_{Ω^{L}¯}(c)ρ(c)dc,
$$

where $Ω^{L}¯$ is the average of the variable tuning curves $Ω_{i}^{L}$. Small variations in the peak rate and grid fields will therefore average out, unless these variations are coherent across grid cells. Thus, resolution bounded by the FI is robust with respect to minor differences in peak firing rates and hexagonality. Similar arguments hold in higher dimensions.

In this study, we focused on optimizing grid modules for an isotropic and homogeneous space, which means that the resolution should be equal everywhere and in each direction of space. From a mathematical point of view, this is the most general setting, but it is certainly not the only imaginable scenario; future studies should shed light on other geometries. Indeed, the topology of natural habitats, such as burrows or caves, can be highly complicated. Higher resolution might be required at spatial locations of behavioral relevance. Neural representations of 3D space may also be composed of multiple 1D and 2D patches (Jeffery et al., 2013). However, the mere fact that these habitats involve complicated low-dimensional geometries does not imply that an animal cannot acquire a general map for the environment. Poincaré already suggested that an isotropic and homogeneous representation for space can emerge out of non-Euclidean perceptual spaces, as one can move through physical space by learning the motion group (Poincaré, 1913). An isotropic and homogeneous representation of 3D space facilitates (mental) rotations in 3D and yields local coordinates that are independent of the environment's topology. On the other hand, the efficient-coding hypothesis (Barlow, 1959; Atick, 1992; Simoncelli and Olshausen, 2001) would argue that surface-bound animals might not need to dedicate their limited neuronal resources to acquiring a full representation of space, as flying animals might have to do, so that representations of 3D space will be species-specific (Las and Ulanovsky, 2014). Desert ants represent space only as a projection to flat space (Wohlgemuth et al., 2001; Grah et al., 2007). Likewise, experimental evidence suggests that rats do not encode 3D space in an isotropic manner (Hayman et al., 2011), but this might be a consequence of the specific anisotropic spatial navigation tasks these rats had to perform. Data from flying bats, on the other hand, demonstrate that, at least in this species, place cells represent 3D space in a uniform and nearly isotropic manner (Yartsev and Ulanovsky, 2013). The 3D, toroidal head-direction system in bats also suggests that they have access to the full motion group (Finkelstein et al., 2014). Our theoretical analysis assumes that the same is true for bat grid cells and that they have radially symmetric firing fields. From these assumptions, we showed the grid cells' firing fields should be arranged on an $FCC$ lattice or packed as $HCP$. Interestingly, such solutions also evolve dynamically in a self-organizing network model for 3D (Stella et al., 2013; Stella and Treves, 2015) that extends a previous 2D system which exhibits hexagonal grid patterns (Kropff and Treves, 2008). Experimentally, the effect of the arena's geometry on grid cells' tuning and anchoring has also been a question of great interest (Derdikman et al., 2009; Krupic et al., 2013, 2015; Stensola et al., 2015). First, let us note that even though the environment might be finite, the grid-cell representation need not be constrained by it. In particular, the firing fields are not required to be contained within the confines of the four walls of a box—experimental observations show that walls can intersect the firing fields (so that one measures only a part of the firing field). On the other hand, the borders clearly distort the hexagonal arrangement of nearby firing fields in 2D environments (Stensola et al., 2015), whereas central fields are more perfectly arranged. Deviations are also observed when only a few fields are present in the arena (Krupic et al., 2015). One might expect similar deviations in 3D, such as for bats flying in a confined space. Our mathematical results rely on symmetry arguments that do not cover non-periodic tuning curves. Given that the resolution is related to the packing ratio of a lattice, extensions of the theory to general packings might allow one to draw on the rich field of optimal finite packings (Böröczky, 2004; Toth et al., 2004), thereby providing new hypotheses to test.

Many spatially modulated cells in rat medial entorhinal cortex have hexagonal tuning curves, but some have firing fields that are spatially periodic bands (Krupic et al., 2012). The orientation of these bands tends to coincide with one of the lattice vectors of the grid cells (as the lattices for different grid cells share a common orientation), so band cells might be a layout ‘defect’. In this context, we should point out that the lattice solutions are not globally optimal. For instance, in 2D, a higher resolution can result from two systems of nested 1D grid codes, which are aligned to the x and y axis, respectively, than from a lattice solution with the same number of neurons. The 1D cells would behave like band cells (Krupic et al., 2012). Similar counterexamples can be given in higher dimensions too. The anisotropy of the spatial tuning in grid cells of climbing rats when encoding 3D space (Hayman et al., 2011) might capitalize on this gain (Jeffery et al., 2013). Radial symmetry of the tuning curve may also be non-optimal. For example, two sets of elliptically tuned 2D unimodal cells, with orthogonal short axes, typically outperform unimodal cells with radially symmetric tuning curves (Wilke and Eurich, 2002). Why experimentally observed place fields and other tuning curves seem to be isotropically tuned is an open question (O'Keefe and Dostrovsky, 1971; Yartsev and Ulanovsky, 2013).

Grid cells which represent the position of an animal (Hafting et al., 2005) have been discovered only recently. By comparison, in technical systems, it has been known since the 1950s that the optimal quantizers for 2D signals rely on hexagonal lattices (Gray and Neuhoff, 1998). In this context, we note that lattice codes are also ideally suited to cover spaces that involve sensory or cognitive variables other than location. In higher-dimensional feature spaces, the potential gain could be enormous. For instance, the optimal eight-dimensional (8D) lattice is about 16 times denser than the orthogonal 8D lattice (Conway and Sloane, 1992) and would, therefore, dramatically increase the resolution of the corresponding population code. Advances in experimental techniques, which allow one to simultaneously record from large numbers of neurons (Ahrens et al., 2013; Deisseroth and Schnitzer, 2013) and to automate stimulus delivery for dense parametric mapping (Brincat and Connor, 2004), now pave the way to search for such representations in cortex. For instance, by parameterizing 19 metric features of cartoon faces, such as hair length, iris size, or eye size, Freiwald et al. showed that face-selective cells are broadly tuned to multiple feature dimensions (Freiwald et al., 2009). Especially in higher cortical areas, such joint feature spaces should be the norm rather than the exception (Rigotti et al., 2013). While no evidence for lattice codes was found in the specific case of face-selective cells, data sets like this one will be the test-bed for checking the hypothesis that other nested grid-like neural representations exist in cortex.

## Materials and methods

We study population codes of neurons encoding the D-dimensional space by considering the FI J as a measure for their resolution. The population coding model, the construction to periodify a tuning shape Ω onto a lattice $L$ with center density ρ, as well as the definition of the FI, are given in the main text. In this section we give further background on the methods.

### Scaling of grid cells and the effect on Jς

How is the resolution of a grid module affected by dilations? Let us assume we have a grid module with signature $ς=(Ω,ρ,L)$, as defined in the main text, and that λ > 0 is a scaling factor. Then $\lambdaς:=(Ω(\lambdar),ρ(\lambdax),\lambda⋅L)$ is a grid module too, and the corresponding tuning curve $(Ω∘\lambda)_{\lambdaL}$ satisfies:

$$
(Ω∘\lambda)_{\lambdaL}(x)=Ω_{L}(\lambdax).
$$

Thus, the tuning curve $(Ω∘\lambda)_{\lambdaL}$ is a scaled version of $Ω_{L}$. What is the relation between the FI of the initial grid module and the rescaled version? Let us fix the notation: $ρ(c)=\sum^{​}_{i}^{N}\delta(c−c_{i})$. From the definition of the population information (Equation 9), we calculate

$$
J_{\lambdaς}(0)=\sumi=1MJ_{(Ω∘\lambda)_{\lambdaL}}(\lambdac_{i})=\sumi=1MJ_{Ω_{L}}(c_{i})⋅\frac{1}{\lambda^{2}}=\frac{1}{\lambda^{2}}J_{ς}(0),
$$

where in the second step we used the re-parameterization formula of the FI (Lehmann, 1998). This shows that the FI of a grid module scaled by a factor λ is the same as the FI of the initial grid module times 1/λ2.

### Population FI for Poisson noise with radially symmetric tuning

In the ‘Results’ section, we give a concrete example for Poisson noise and the bump function. Here we give the necessary background. Equation 13 states that

$$
J_{ς}(0)≈\frac{M}{det(L)}\int_{B_{R}(0)}J_{Ω^{L}}(c)dc.
$$

One would like to know $\int_{B_{R}(0)} J_{Ω^{L}}(c)dc$ for various tuning shapes Ω with supp(Ω) ≤ R.

Consider x ∈ L and α ∈ {1,…,D}. Then:

$$
\frac{\partiallnP(K|x)}{\partialx_{\alpha}}=\frac{\partiallnP(K,s)}{\partials}|_{s=Ω^{L}(x)}⋅Ω′(∥x∥^{2}) f_{max}\tau 2x_{\alpha}.
$$

Together with the definition of the FI Equation 13, this yields

$$
J_{Ω^{L}}(x)_{\alpha\beta}=4x_{\alpha}x_{\beta}f_{max}^{2}\tau^{2}Ω′(∥x∥^{2})^{2}. \sumK(\frac{\partial}{\partials}lnP(K,s)|_{s=Ω^{L}(x)})^{2}⋅P(K,Ω^{L}(x))︸=:N(∥x∥^{2}).
$$

Note that for α ≠ β this function is odd in x. Thus, when averaging these individual contributions over a symmetric fundamental domain L: $\int_{L} J_{Ω^{L}}(c)_{\alpha\beta}dc=0$ for α ≠ β. Thus, the diagonal entries are all identical. This also holds for any fundamental domain L when BR(0) ⊂ L, because BR(0) is symmetric.

For Poisson spiking $N(∥c∥^{2})$ has a particularly simple form, namely $N(∥c∥^{2})=1/(f_{max}\tau Ω(∥c∥^{2}))$. The trace of the FI matrix becomes

$$
trJ_{ς}(0)=4f_{max}\tau\int_{B_{R}(0)}∥c∥^{2}\frac{Ω′(∥c∥^{2})^{2}}{Ω(∥c∥^{2})}︸=:F(c)dc.
$$

Thus, the trace only depends on the tuning shape Ω and its first derivative. In the main text, we use the following specific tuning shape:

$$
Ω(r)={exp(\frac{\theta_{1}}{\theta_{2}^{2}}−\frac{\theta_{1}}{\theta_{2}^{2}−r^{2}})if |r| <\theta_{2}0otherwise.
$$

This type of function is often called ‘bump function’ in topology, as it has a compact support but is everywhere smooth (i.e., infinitely times continuously differentiable). In particular, the support of this function is [0, θ2), and is therefore controlled by the parameter θ2. The other parameter θ1 controls the slope of the bump's flanks (see upper panels of Figure 3—figure supplement 1).

For the bump-function Ω and radius $r=\sqrt{\sum^{​}_{\alpha}^{D}x_{\alpha}^{2}}$ the integrand for the FI is given by

$$
F(r)={\frac{4\theta_{1}^{2}r^{2}}{(\theta_{2}^{2}−r^{2})^{4}}  exp  (\frac{\theta_{1}}{\theta_{2}^{2}}−\frac{\theta_{1}}{\theta_{2}^{2}−r^{2}})if |r| <\theta_{2}0otherwise.
$$

The lower panels of Figure 3—figure supplement 1 depict the integrand of Equation 25, defined as $F(r)$. This function shows how much FI a cell at a particular distance contribute to the location 0. By integrating the FI over the fundamental domain L for a lattice $L$ one gets Jς(0), that is, the average FI contributions from all neurons (as shown in Figures 3, 4, 5E).

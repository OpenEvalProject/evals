# Expansion and contraction of resource allocation in sensory bottlenecks

## Authors

- Laura R Edmondson<sup>1</sup> ([ORCID: 0000-0001-9886-1121](https://orcid.org/0000-0001-9886-1121))
- Alejandro Jiménez Rodríguez<sup>2</sup>
- Hannes P Saal<sup>1</sup> ([ORCID: 0000-0002-7544-0196](https://orcid.org/0000-0002-7544-0196)) †

### Affiliations

1. Active Touch Laboratory, Department of Psychology, University of Sheffield Sheffield United Kingdom ([ROR:05krs5044](https://ror.org/05krs5044))
2. Sheffield Robotics, University of Sheffield Sheffield United Kingdom ([ROR:05krs5044](https://ror.org/05krs5044))
3. Department of Computer Science, University of Sheffield Sheffield United Kingdom ([ROR:05krs5044](https://ror.org/05krs5044))

† Corresponding author

## Abstract

Topographic sensory representations often do not scale proportionally to the size of their input regions, with some expanded and others contracted. In vision, the foveal representation is magnified cortically, as are the fingertips in touch. What principles drive this allocation, and how should receptor density, for example, the high innervation of the fovea or the fingertips, and stimulus statistics, for example, the higher contact frequencies on the fingertips, contribute? Building on work in efficient coding, we address this problem using linear models that optimally decorrelate the sensory signals. We introduce a sensory bottleneck to impose constraints on resource allocation and derive the optimal neural allocation. We find that bottleneck width is a crucial factor in resource allocation, inducing either expansion or contraction. Both receptor density and stimulus statistics affect allocation and jointly determine convergence for wider bottlenecks. Furthermore, we show a close match between the predicted and empirical cortical allocations in a well-studied model system, the star-nosed mole. Overall, our results suggest that the strength of cortical magnification depends on resource limits.

## Introduction

In many sensory systems, receptors are arranged spatially on a sensory sheet. The distribution of receptors is typically not uniform, but instead, densities can vary considerably. For example, in vision, cones are an order of magnitude more dense in the fovea than in the periphery (Goodchild et al., 1996; Wells-Gray et al., 2016). In the somatosensory system, mechanoreceptors are denser in the fingertips than the rest of the hand (Johansson and Vallbo, 1979). Alongside the density of receptors, the statistics of the input stimuli can also vary. For example, the fingertips are much more likely to make contact with objects than the palm (Gonzalez et al., 2014). Subsequent sensory areas are typically arranged topographically, such that neighbouring neurons map to nearby sensory input regions, for example, retinotopy in vision and somatotopy in touch. However, the size of individual cortical regions is often not proportional to the true physical size of the respective sensory input regions and, instead, representations might expand (often called magnification) or contract. For example, both the fovea and the fingertips exhibit expanded representations in early visual and somatosensory cortices, respectively, compared to their physical size (Azzopardi and Cowey, 1993; Engel et al., 1997; Sereno et al., 1995; Martuzzi et al., 2014). What determines this cortical magnification? For somatotopy, it has been proposed that cortical topography might directly reflect the density of sensory receptors (Catani, 2017). On the other hand, receptor density alone is a poor predictor of magnification (Corniani and Saal, 2020) and work on plasticity has established that cortical regions can expand and contract dynamically depending on their usage, suggesting that expansion and contraction might be driven by the statistics of the sensory stimuli themselves (Coq and Xerri, 1998; Merzenich and Jenkins, 1993; Xerri et al., 1996).

Here, we tackle this problem from a normative viewpoint, employing efficient coding theory, which has been widely used to model and predict sensory processing. Efficient coding theory includes a number of different approaches such as sparse coding, redundancy reduction and predictive coding, depending on the constraints of the proposed problem (Chalk et al., 2018). Here, we focus on efficient coding via redundancy reduction (Barlow, 1961), which suggests that neural populations are tuned to maximize the information present in the sensory input signals by removing redundant information (Atick, 1992; Atick and Redlich, 1990; Attneave, 1954; Graham and Field, 2009; Chechik et al., 2006). Efficient coding models have been most prominent in vision (Kersten, 1987; Karklin and Simoncelli, 2011; Atick, 1992; Atick and Redlich, 1990; Doi et al., 2012; Olshausen and Field, 1996; Olshausen and Field, 1997; Olshausen and Field, 2004; Bell and Sejnowski, 1997) and audition (Smith and Lewicki, 2006; Lewicki, 2002). This prior work has mostly focused on predicting the response properties and receptive field structure of individual neurons. In contrast, here we ask how receptive fields—independent of their precise structure—should tile the sensory sheet when the receptors themselves differ in density and activation levels.

Some aspects of magnification in topographic representations have been qualitatively reproduced using self-organizing maps (Ritter et al., 1992). However, these models generally lack a clear cost function and the magnification factor can be determined exactly only in rare cases, while a general expression is lacking (Ritter and Schulten, 1986). Assuming a uniform density of output neurons, cortical maps may be optimizing for the spread of incoming information to be equally distributed over these neurons (Plumbley, 1999).

In contrast to receptor density, there has been some work on how populations of neurons should encode non-uniform stimulus statistics using Fisher information (Ganguli and Simoncelli, 2010; Ganguli and Simoncelli, 2014; Ganguli and Simoncelli, 2016; Yerxa et al., 2020). This approach aims to approximate mutual information and is used to calculate optimal encoding in a neural population (Yarrow et al., 2012) however, its use is restricted to specific conditions and assumptions (Berens et al., 2011; Bethge et al., 2002). Rather than receptive fields uniformly tiling the input space, the optimal population should be heterogeneous, with receptive fields placed more densely over high-probability inputs, at detriment to low-probability regions (Ganguli and Simoncelli, 2014). Our approach differs from this prior work: rather than maximizing information between the neural population and the stimulus itself, we instead consider information between the neural population and an initial population of receptor neurons. This places a limit on the total amount of information that can be represented.

The need for information maximization is often motivated by resource constraints. These can take the form of an explicit bottleneck, where the number of receptor neurons is greater than the number of output neurons. This is the case in the early visual system, where photoreceptors in the retina are much more numerous than the retinal ganglion cells to which they project (Wells-Gray et al., 2016; Goodchild et al., 1996). Other sensory systems might lack such explicit bottlenecks, but still place limits on the amount of information that is represented at a higher-order processing stage.

How then should resource allocation change for different-sized bottlenecks, given varying densities of receptors and different stimulus statistics? Here, we derive optimal neural allocations for different bottlenecks, while systematically varying receptor density and stimulus statistics. A preliminary version of these results restricted to the effects of receptor density in a 1D space was previously presented as a conference paper (Edmondson et al., 2019).

## Results

We restrict ourselves to linear models and only consider second-order statistics of the sensory signals, such that redundancy reduction simplifies to decorrelation (for examples from the visual literature, see Hancock et al., 1992; Simoncelli and Olshausen, 2001; Doi and Lewicki, 2005). We also introduce a sensory bottleneck, such that the number of output neurons is smaller than the number of receptors. Specifically, $r=Wx$, where $r$ is the $m$-dimensional output vector, $x$ is the $n$-dimensional input vector (with $n>m$) containing sensory receptor responses, and $W$ contains the receptive field. Assuming a low-noise regime, optimal decorrelation can be achieved if $W$ takes the following form:

$$
W=Λ^{−\frac{1}{2}}Φ^{T},
$$

where $Λ$ and $Φ$ contain the (top $m$) eigenvalues and eigenvectors, respectively, of the covariance matrix $Σ=X^{T}X$.

In the specific setup we consider here, receptors are placed in non-uniform densities across the sensory sheet, with some regions having a higher density than others. For example, in Figure 1B, the digit tip is tiled more densely than the rest of the finger. The covariance of receptor activation decreases with distance (see Figure 1C). Thus, directly neighbouring units in denser regions covary more strongly than those from less dense regions. The activation level of receptors can also vary between regions, which is modelled through scaling the covariance function (see Appendix 1 for further details). We initially focus on negative exponential covariance functions, for which the eigenvalues and the resulting allocation can be calculated analytically. The covariance between receptors xi and xj for two regions R1 and R2, differing in density and activation, can thus be expressed as

$$
Σ_{ij}^{(R1)}=e^{−\gamma|x_{i}−x_{j}|}andΣ_{ij}^{(R2)}=ae^{−d\gamma|x_{i}−x_{j}|},
$$

![Figure 1.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig1-v2.jpg)

**Figure 1.:** (A) Abstract problem setup. When two regions vary in their receptor densities and activation, how should a shared resource be allocated between them when that resource is limited, as in a sensory ‘bottleneck’? The allocation between the two regions may vary depending on the width of the bottleneck, for example, for narrow bottlenecks it might be most efficient to allocate all resources to the higher density region 2. (B) Application of the problem to the tactile system. The density of touch receptors differs across regions of the hand (e.g. fingertip, shown in orange, versus finger phalanx, yellow). Different finger regions make contact with objects at different rates (dark blue versus light blue shading, darker colours indicating higher contact rates). (C) Sensory inputs are correlated according to a covariance function that decays with distance between receptors on the sensory sheet. This function is evaluated at different receptor distances depending on the density of sensory receptors (orange versus yellow dots at the bottom). Regions with higher probability of activation exhibit greater variance (dark versus light blue curves). (D) Decorrelation of sensory inputs in the presence of a bottleneck is achieved by calculating and retaining the eigenvectors and eigenvalues of the receptor covariance matrix. Here, this matrix is approximated as a block matrix, which allows calculating the eigenvalues for each region individually (dark blue versus light blue box). (E) The combined set of eigenvalues from all regions is then sorted; the region where each successive eigenvalue in the combined sorted set originates from determines where that output neuron’s receptive field will fall. (F) Counting which input regions successive eigenvalues belong to results in the allocation breakdown for different bottlenecks. For certain forms of the covariance function, this allocation can be calculated analytically.

where $a$ denotes the receptor activation ratio and $d$ the receptor density ratio between both regions. It can be seen that changing the density affects the decay of the covariance function and thereby ‘stretches’ the space, while changing the activation scales the function.

We approximate the regions as separate, such that no receptors are activated from both regions simultaneously. The covariance matrix across all receptors then forms a block matrix, where the covariance between separate regions is zero (Figure 1D):

$$
Σ=[Σ^{(R1)}00Σ^{(R2)}]
$$

Thus, eigenvalues can be calculated separately from the covariance matrices of each region (inset panels in Figure 1D), and for negative exponential covariance functions, this can be done analytically (see ‘Methods’ for mathematical derivations):

$$
R_{1}:\lambda_{l,m}^{(R1)}=\frac{2\gamma}{\pi^{2}L^{−2}(l^{2}+m^{2})+\gamma^{2}}andR_{2}:\lambda_{n,o}^{(R2)}=\frac{2\gammaa\sqrt{d}}{\pi^{2}L^{−2}(n^{2}+o^{2})+\gamma^{2}}
$$

Finally, the resulting eigenvalues are ordered by magnitude for both regions combined (grey line in Figure 1E). A bottleneck is introduced by restricting the total number of output neurons. This is done by selecting from the combined set of ordered eigenvalues until the limit is reached. The proportion of eigenvalues originating from each input region determines its allocation for the chosen bottleneck width (see red dashed line in Figure 1E and F).

In the following, we will present results for the common case of 2D sensory sheets, while results for 1D receptor arrangements are summarized in Appendix 6. For ease of analysis, all cases discussed will assume two sensory input regions of equal size, which are differing in receptor density, input statistics, or both. In all our examples, receptors in the low-density (baseline) region are always spaced on a grid with a distance of 1.

### Resource limits determine the amount of magnification

First, we investigated resource allocation in bottlenecks for heterogeneous density of receptors and heterogeneous stimulus statistics separately, whilst keeping the other factor uniform across the input regions.

#### Heterogeneous density

For two regions with different receptor densities, we found that the higher density region could either expand or contract relative to its input density, depending on the width of the bottleneck. Specifically, for narrow bottlenecks (smaller than approximately 10% of input neurons), the higher density region is either exclusively represented or its representation is expanded compared to a proportional density allocation (see example in Figure 2A). Mathematically, this can be explained by a multiplicative scaling of the eigenvalue function for the higher density region (see illustration in Figure 2—figure supplement 3A). In contrast, for intermediate bottlenecks, low-density regions expand their representation, beyond what is expected for a proportional mapping (see dashed red line in Figure 2A denoting proportional allocation), leading to a contraction of the high-density region. For negative exponential covariance functions, this allocation converges to a fixed ratio at wider bottlenecks of $1/(1+\sqrt{d})$, where $d$ is the density ratio between both regions (dashed yellow line in Figure 2A; see ‘Methods’ for derivation), as neurons are allocated to either region at a fixed ratio (see inset in Figure 2—figure supplement 3A). Finally, for wide bottlenecks, all information arising from the low-density region has now been captured, and any additional output neurons will therefore be allocated to the high-density region only. The over-representation of the low-density region thus decays back to the original density ratio. The overall nonlinear effect of bottleneck width is present regardless of the ratio between the densities (see Figure 2B). The spatial extent of the correlations over the sensory sheet (controlled by the decay constant γ in the covariance function, see ‘Methods’) determines allocation at narrow bottlenecks, and how fast the allocation converges, but does not affect the convergence limit itself (Figure 2C). As γ increases, and therefore spatial correlations decrease, the convergence limit is approached only at increasingly wider bottlenecks. The extent of magnification thus heavily depends on the correlational structure of the stimuli for narrower bottlenecks, while receptor densities are more important for wider bottlenecks.

![Figure 2.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig2-v2.jpg)

**Figure 2.:** (A) Illustration of resource allocation for heterogeneous receptor density but homogeneous stimulus statistics over all bottleneck sizes. Orange denotes the lower density region and blue the higher density region, with a ratio of 1:3. Dotted lines show proportional representation according to receptor numbers (red) and convergence of the optimal allocation in the limit (yellow). Arrows indicate contraction (up) and expansion (down) of the higher density region representation. Inset demonstrates change in density between the regions. (B) Bottleneck allocation boundaries for different density ratios (given as low:high). The area below each line corresponds to the low-density representation, while the area above corresponds to the high-density representation, as in (A). (C) Effect of changing the extent of the spatial correlations (parameterized by the decay value γ, see ‘Methods’ for details and Figure 2—figure supplement 1 for an illustration of the covariance function for different values of γ). Density ratio is set at 1:3 for all γ. Increasing γ leads to expansion of the higher density region for a larger initial portion of the bottleneck. (D–F) Same as in row above but for homogeneous density and heterogeneous receptor activation ratios. (D) Illustrative example with the blue region having higher receptor activation. Note that the representation of the higher activation region is expanded for all bottleneck widths. Inset demonstrates difference in activation between the regions. Larger, brighter coloured points indicate higher activation for that region compared to the other. (E) Allocation boundaries for different activation ratios. The representation of the higher activation regions is expanded for all bottlenecks. As activation ratio increases, the highly active region allocation is expanded for wider bottlenecks. (F) Changing the extent of spatial correlations (γ) has larger effects when the activation ratio is heterogeneous (set at 1:3 for all γ) compared to heterogeneous density (C). See Figure 2—figure supplement 2 for an equivalent figure considering 1D receptor arrangements.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Smaller γ leads to a slower decay and therefore a larger extent of spatial correlations. When the sigma is large, receptors have less similar responses to their neighbours, and therefore co-vary less. Orange points denote the baseline spacing of receptors along one dimension. When receptor density is varied, the other region will have higher density (e.g. 1:3, indicated by blue dots).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Examples of allocation for two input regions with differing receptor densities and activation (see insets) for different bottleneck widths, demonstrating complex trade-offs in resource allocation. Here, ratio for low:high density = 1:3, γ=1. Dotted lines show representation proportional to receptor density (red) and convergence in the limit (yellow). Arrows indicate expansion (down) and contraction (up) of the higher density (blue) region. Both expansion and contraction of the higher density region are seen, similar to the 2D case. (B). Allocation boundaries for different density ratios. Ratios are given as low:high density. (C) Effect of changing the decay γ parameter. Density ratio is set at 1:3 for all sigmas. (D–F), same as above but for density constant across the two regions and receptor activation manipulated. Activation ratio is set at 1:3 in (D, F). Note that in (D) the representation of the higher activation (blue) region is expanded for all bottlenecks.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Main panels: eigenvalues for heterogeneous density (A), heterogeneous activation (B), or combined (C). For each, the manipulated ratio is set as 1:2. For simplicity, the example considers 1D regions. Orange markers show eigenvalues from the baseline region, which is identical for all panels. Blue markers show eigenvalues from the second region with higher density, activation, or both, respectively. Markers connected by the grey line show the combined set of sorted eigenvalues from both regions. Insets: cumulative allocation for the set of eigenvalues marked by the red ellipse in the main panel. Horizontal orange lines indicate eigenvalues from and therefore allocation to the orange region, whilst vertical blue lines indicate allocation to the blue region. (A) Heterogeneous density. Increased receptor density in the blue region causes higher spatial correlations between neighbouring receptors and therefore larger eigenvalues, leading to a scaling of the eigenvalue curve. Increased density also leads to a larger number of receptors in the blue region, increasing the number of eigenvalues from this region and the total number of eigenvalues considered. (B) Heterogeneous activation. Increased variance in the blue region leads to a scaling of the eigenvalue curve. However, the number of receptors in the blue region is not affected, explaining differences observed compared to (A). (C) Heterogeneous density and activation. Effects from (A) and (B) are combined, leading to a double scaling of the eigenvalue curve, plus an increase in the total number of eigenvalues.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Resource allocations where the bottleneck is expressed as variance explained. Because eigenvalues decrease dramatically in size, this re-expression results in a ’squashing’ of the allocation curve towards higher bottleneck sizes as the initial eigenvalues in the sorted set explain a much larger amount of the variance. (A) Examples with heterogeneous density. (B) Examples with heterogeneous activation. (C) Examples with heterogeneous density and activation. Dashed red line in each denotes allocation proportional to density.

#### Heterogeneous statistics

Aside from receptor densities, the stimulus statistics can also vary over the input space, leading to differences in receptor activation levels between the regions and their associated response variance. Overall, allocations for heterogeneous receptor activation are similar to those found with heterogeneous density. However, while the allocations are again a nonlinear function of bottleneck width, the representations are solely expanded for the higher activation region for all bottleneck widths (see example in Figure 2D). The extent of this expansion depends on the width of the bottleneck and is again more extreme for narrower bottlenecks (see Figure 2E). The convergence limit is $1/(1+a)$, where $a$ is the activation ratio, implying that the level of expansion and contraction in intermediate bottlenecks is more extreme than in the heterogeneous density case (see difference between red and yellow dashed lines in Figure 2A and D). Finally, the effect of spatial correlations is also more pronounced (Figure 2F).

In the cases described above, the bottleneck was constrained by the number of output neurons. Alternatively, the limiting factor might be set as the amount of information (total variance) captured. Doing so results in allocation curves that retain the nonlinear behaviour described here (see Figure 2—figure supplement 4 for illustrations). An additional consideration is the robustness of the results regarding small perturbations of the calculated eigenvalues. As allocation depends on the ranks of the eigenvalues only, low levels of noise are unlikely to affect the outcome for narrow bottlenecks, especially since eigenvalues are decaying rather steeply in this regime. On the other hand, allocation in wider bottlenecks is determined from small tail eigenvalues which are much more sensitive to noise (which is also evident when comparing the analytical solution to numerical ones). Allocation can therefore be expected to be somewhat less robust in those regimes.

In summary, we find that representations of different input regions can contract or expand, depending on the bottleneck width. This effect plays out similarly for differences in receptor density and receptor activation, however, with some crucial differences. Finally, for narrow bottlenecks, the spatial extent of the correlations across the sensory sheet becomes an important driver.

### Interplay between stimulus statistics and receptor density

In sensory systems, such as in touch, both the density and input statistics vary across regions and will therefore jointly determine the resulting allocation. As a consequence, the convergence for intermediate bottlenecks will depend on both density and activation ratios, and can be calculated as $\frac{1}{(1+a⁢\sqrt{d})}$, where $a$ is the activation and $d$ is the density ratio (see ‘Methods’ for derivation).

At narrow bottlenecks, the spread of possible allocations is much wider for varying the activation ratio (see left panel of Figure 3A) compared to varying the density ratio. Thus, for 2D sensory sheets, the activation ratio more strongly determines the possible allocation than does the density ratio. Specifically, this means that the allocation regime, that is, whether the allocation expands, contracts, or exhibits both behaviours across all bottleneck widths, is more dependent on relative receptor activation than densities (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig3-v2.jpg)

**Figure 3.:** (A) Allocations with both heterogeneous density and activation ratios. Expansion and contraction for a baseline region where relative density and activation is varied over the other region. All ratios given are baseline:other region. Left: fixed density ratio of 1:2, while activation ratio is varied between 7:1 and 1:7 (see colourbar). Purple dashed line indicates allocation proportional to density ratio. Right: fixed activation ratio of 1:2, while density ratio is varied between 7:1 and 1:7. The coloured markers indicate whether the baseline region is expanded (dark blue squares), contracted (white circles), or both (light blue stars) across all bottlenecks. (B) Possible expansion/contraction regimes for the baseline region based on combinations of density and activation ratios. Colours as shown by the markers in (A). Grey dashed lines show all possible allocation regimes for an example with either fixed density ratio (horizontal, corresponding plot in A, left) or activation ratio (vertical, A, right). When activation is fixed and density is varied, the allocations can be either expanded/both or contracted/both across the full bottleneck width. In contrast, when the density ratio is fixed and activation is varied, the allocation of a region could be any of the three regimes. The green ellipse highlights parameter combinations where activation and density ratios are correlated. See Figure 3—figure supplement 1 for a comparison of how receptor density and activation interact between 1D and 2D receptor arrangements.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Effect of changing both the density and activation ratios, and possible resource allocations for two regions. Plots show the same density ratio, 1:5, considering 1D (left) and 2D (right) regions. Allocation % is for baseline region (region 1). Each line denotes the variance ratios between region 1:region 2 (see colourbar). Solid lines denote contraction of baseline region representation, whilst dotted lines are expansion. The horizontal red dashed line shows the proportional density representation. Across both 1D and 2D, different patterns of expansion and contraction occur. The baseline region is more likely to either be fully expanded or contracted for the whole bottleneck in 2D, whereas in 1D both expansion and contraction occur (denoted by light blue star, which covers three activation ratios in 1D, but only 1:1 in 2D as indicated by the markers). In 1D, the same activation and density ratio leads to convergence at the proportional density, whereas for 2D, the convergence is always lower. (B) Comparison of the possible allocation schemes between 1D (left) and 2D (right). Dotted grey line denotes density ratio from (A). In 2D, the likelihood of both expansion and contraction (light blue region) of the representations decreases.

Finally, it is likely that regions with higher receptor densities will also show greater activation than lower density regions. For example, in touch, the regions on the hand with the highest receptor densities also are the most likely to make contact with objects (Gonzalez et al., 2014). In these cases, both effects reinforce each other and drive the resulting allocation further from proportional allocation (see orange lines in Figure 3A and green ellipse in Figure 3B).

### Resource limits determine the strength of plasticity under changes in stimulus statistics

Over most of the lifetime of an organism, the resources available for processing sensory information and the density of sensory receptors should be relatively constant. The stimulus statistics, on the other hand, can and will change, for example, when encountering a new environment or learning new skills. These changes in stimulus statistics should then affect sensory representations, mediated by a variety of plasticity mechanisms. For example, increased stimulation of a digit will lead to an expansion of that digit’s representation in somatosensory cortex (Jenkins et al., 1990).

We asked how representations should adapt under the efficient coding framework and whether resource limits would affect the resulting changes. To answer this question, we calculated optimal allocations for different bottleneck widths, receptor densities, and stimulus statistics. We then introduced a change in stimulus statistics and re-calculated the resulting allocations (see illustration in Figure 4A). As expected, we found that when increasing the receptor activation over a region (e.g. by increasing stimulation of the region), more neurons would be allocated to this region than to the other. Interestingly, however, this effect was dependent on the width of the bottleneck. The largest effects are seen for smaller bottlenecks and then diminish as the bottleneck size increases. Figure 4B demonstrates such allocation changes for three different bottleneck widths for a range of receptor densities and activation ratios. This suggests that plasticity should be relatively stronger under extreme resource constraints than in cases where limits on the information are generous.

![Figure 4.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig4-v2.jpg)

**Figure 4.:** (A) Top left: illustration of problem setup. Increased stimulation is applied to the middle digit (yellow symbols), leading to changes in optimal allocations. Top right: optimal allocations for baseline (blue) and stimulation (yellow) conditions across all bottleneck widths. Stimulation of the middle finger increases its representation, but the relative magnitude of the effect depends on the bottleneck width. Bottom: changes in allocation of the middle digit for two bottleneck widths (indicated by dashed lines above). The increase is proportionally larger for the narrow compared to the wide bottleneck. (B) Change in allocation when receptor activation for an input region increases (left half) or decreases (right half). Drastic changes in cortical allocation are observed for narrow bottlenecks (green lines), while wider bottlenecks (red and purple lines) induce only moderate change. Solid lines denote equal receptor density across both regions, while dashed lines show examples with varying density.

### Generalization to other covariance functions

The results above relate to negative exponential covariance functions, where allocations can be solved analytically and it is unclear whether these findings generalize to other monotonically decreasing covariance functions and are therefore robust. Specifically, negative exponential covariances are relatively ‘rough’ and allocations might conceivably depend on the smoothness of the covariance function. To test directly how optimal allocations depend systematically on the smoothness of the covariance function, we numerically calculated allocations for three covariance functions of the Matérn class, whose smoothness depends on a single parameter ν. The negative exponential considered so far is a special case of the Matérn class when $ν=1/2$ and we also considered $ν=3/2$ and $ν=5/2$ (see ‘Methods’). As ν increases, the decay function becomes smoother, yielding larger correlations at short distances and smaller ones at farther distances (see Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig5-v2.jpg)

**Figure 5.:** (A) Three covariance functions of different smoothness taken from the Matérn class, differing in the parameter ν (see ‘Methods’). (B) Examples of numerically determined allocation for the covariance functions shown in (A) for two scenarios. Left: density ratio 1:2, equal activation. Right: density ratio 1:6, activation ratio 1:3. The red dashed line shows the analytic solution for the negative exponential covariance ($ν=1/2$). (C) Estimated allocations at convergence for different density ratios (horizontal axis) and a fixed activation ratio of 1:2. Solid lines denote numerical convergence, and dashed lines refer to fitted functions (see main text).

We numerically calculated allocations for different density and activation ratios in 1D (Figure 5B). We focused on smaller bottleneck widths, where solutions are numerically stable, and observed a close match between the numerical and analytical solutions for the negative exponential covariance function (see dashed lines in Figure 5B).

This analysis yielded two main findings. First, allocation curves are qualitatively similar across all tested covariance functions in that regions with higher density, activation, or both are systematically over-represented. Furthermore, this effect is more extreme at smaller bottleneck widths. Second, the resulting allocations depend systematically on the smoothness of the covariance function, such that smoother covariances yield less extreme differences in allocation. This effect is most obvious when considering the convergence points at larger bottlenecks: smoother covariance functions induce a more uniform allocation (closer to a 50:50 split) than does the negative exponential (Figure 5C). We also noticed that the convergence points appeared to follow a simple function, namely, $\frac{1}{1+\sqrt[6]{a⁢d}}$ for $ν=5/2$, $\frac{1}{1+\sqrt[4]{a⁢d}}$ for $ν=3/2$ (see dashed lines in Figure 5C), and $\frac{1}{1+\sqrt{a⁢d}}$ for $ν=1/2$ (which is the result obtained analytically, see Appendix 6).

In summary, monotonically decreasing covariance functions result in qualitatively similar allocations to the negative exponential studied earlier. However, precise allocations and convergence are determined by the correlational structure: smoother covariance functions lead to less extreme differences in allocation.

### Predicting cortical magnification in the star-nosed mole

Finally, we investigated to what extent the procedure outlined in the previous sections might predict actual resource allocation in the brain. While our model is relatively simple (see ‘Discussion’), decorrelation has been found to be a strong driver in early sensory processing, including in vision (Atick and Redlich, 1992; Graham et al., 2006; Vinje and Gallant, 2000), audition (Clemens et al., 2011; Smith and Lewicki, 2006), and touch (Ly et al., 2012), and one might therefore expect the approach to at least yield qualitatively valid predictions. As currently available empirical data makes it difficult to test the impact of different bottleneck widths on the resulting allocation directly (see ‘Discussion’), we instead focused on another predicted outcome of the proposed model: the precise interaction between receptor density and receptor activation in driving resource allocation that we presented earlier. We picked the star-nosed mole as our model system because stimulus statistics, receptor densities, and cortical allocations have been precisely quantified. Moreover, the star-nosed mole displays considerable variation in all these parameters, presenting a good opportunity to put the model to the test.

The star-nosed mole is a mostly underground dwelling creature relying on active tactile sensing while foraging for prey (Catania and Kaas, 1997; Catania, 2020). This process is facilitated by two sets of 11 appendages arranged in a star-like pattern that make up the mole’s nose (Figure 6A). Individual rays are tiled with tactile receptors known as Eimer’s organs that detect prey, which is then funnelled towards the mouth (Catania and Kaas, 1997; Sawyer and Catania, 2016). The density of fibres innervating the Eimer’s organs differs across the rays, with rays closer to the mouth exhibiting higher densities (Figure 6B). The rays also vary in size and location with respect to the mouth. This affects their usage as the rays closest to the mouth encounter tactile stimuli much more frequently than other rays (Figure 6C). In the cortex, a clear topographic representation of the rays can be found (Catania and Kaas, 1997). However, the extent of the cortical ray representations is not proportional to the physical size of the rays. Ray 11, which sits closest to the mouth, is cortically magnified several fold and is considered the tactile equivalent of the visual fovea (Catania and Remple, 2004).

![Figure 6.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig6-v2.jpg)

**Figure 6.:** (A) Star-nosed moles have two sets of 11 tactile rays used for detecting and capturing prey. (B) Fibre innervation densities for each ray. (C) Typical usage percentages for each ray during foraging. Higher usage corresponds to greater average activation of receptors located on the corresponding ray. Typically prey is funnelled from distal rays towards ray 11, which is located next to the mouth. Ray outlines adapted from Catania et al., 2011. (D) Left: explained variance ($R^{2}$) between model predictions and cortical allocation for three different models: restricted to receptor density only (purple), restricted to receptor activation only (green), and a full model (pink) that incorporates accurate values for both factors. Results confirm previous findings that ray usage is a better predictor of cortical allocation than receptor densities alone. Additionally, we show that including both of these factors provides a marginal improvement to the fit, with the highest $R^{2}$ (86%). Right: predicted versus empirical cortical allocations for all rays. When including both density and activation parameters, the model provides a good fit to empirical measurements. Scatter plots for all models are available in Figure 6—figure supplement 1B. (A) Reproduced from Figure 1C in Catania et al., 2011, copyright Kenneth Catania.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/70777/elife-70777-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Fits across all bottleneck sizes for each model. Lowest root-mean-square error (RMSE) is indicated for each model. Dashed line indicates lowest RMSE (excluded for densities-only model as RMSE is fairly constant across bottlenecks, see C). (B) Corresponding fits at each selected bottleneck size compared to cortical data. (C) RMSE values over all bottleneck sizes for each model. (D) Can any values be fit given the range of bottleneck sizes? Here, we test whether a good fit can be obtained for a series of ‘random models’, where the random values are selected for each ray’s density and variance within the range of parameters. The same fitting process is then applied, where the lowest RMSE fit to the cortical data is selected based on the range of possible bottlenecks. Note that $R^{2}$ values are calculated with fixed intercept, resulting in some negative values. Most random models perform poorly, suggesting that the model cannot be fit successfully without using the precise parameter values from the empirical star-nosed mole data.

Previous work by Catania and Kaas, 1997 found that cortical sizes are correlated more strongly with the different patterns of activation across the rays, rather than their innervation densities. Using the empirical data quantifying receptor densities and stimulus statistics from this study, we investigated whether the efficient coding model could predict typical cortical representation sizes for each ray (see ‘Methods’ for details) and whether innervation densities or usage would lead to more accurate allocation predictions. As the bottleneck size between periphery and cortex is unknown for the star-nosed mole, we calculated the optimal allocations over all possible bottleneck sizes. Using the model described above, we calculated allocations considering three different scenarios. The first, ‘density only’, included accurate afferent densities, but with activations set to the mean over all rays. The second model, ‘usage only’, included accurate activation ratios but mean receptor densities. Finally, the ‘full model’ included accurate values for both factors. We found that the empirical cortical representation sizes are most accurately predicted by the models that include receptor activation—the ‘receptor usage only’ and ‘full models’ (Figure 6D)—suggesting the star-nosed mole could be employing an efficient coding strategy based on decorrelation in the neural representation of somatosensory inputs.

## Discussion

We examined efficient population coding under limited numbers of output neurons in cases of non-uniform input receptor densities and stimulus statistics. Instead of focusing on the precise structure of the receptive field, we asked which coarse region of the sensory sheet the receptive field would fall on. We showed that the resulting allocations are nonlinear and depend crucially on the width of the bottleneck, rather than being proportional to the receptor densities or statistics. Specifically, narrow bottlenecks tend to favour expansion of a single region, whereas for larger bottlenecks, allocations converge to a constant ratio between the regions that is closer to a proportional representation. Whether, across all possible bottlenecks, allocations are always expanded, contracted, or show both expansion and contraction depends on the relative density and activation ratios, but receptor activation plays a bigger role. When allocation changes due to novel stimulus statistics, a larger fraction of output neurons will switch their receptive field to another region for narrow compared to wide bottlenecks. Finally, we demonstrated that in the star-nosed mole a model that includes both accurate innervation densities and contact statistics provides a better fit to the sizes of somatosensory cortical regions than considering each of these factors alone.

### Comparison with previous approaches

A key feature of efficient coding population models is the non-uniform allocation of output neurons, whereby stimuli occurring at higher probabilities are represented by a greater number of neurons. A common approach is to use Fisher Information as a proxy for mutual information, enabling the calculation of optimal output neuron density and tuning curve placement given a distribution of sensory stimuli (Ganguli and Simoncelli, 2010; Ganguli and Simoncelli, 2014; Ganguli and Simoncelli, 2016; Yerxa et al., 2020). However, these approaches maximize information between the output population and the stimulus distribution itself, such that allocating additional neurons to a given region of the input space will always lead to an increase in the overall amount of information represented. In contrast, our approach assumes a finite number of input receptors in each region. We are thus asking a different question than previous research: once information about a sensory stimulus has been captured in a limited population of receptors, what is the most efficient way of representing this information? This framing implies that once all information from a given region has been fully captured in the output population, our method does not allocate further neurons to that region. Therefore, this also places a limit on the total size of the output population as this cannot exceed the total number of input receptors.

There has also been prior work on how bottlenecks affect sensory representations, though mostly focused on how different levels of compression affect receptive field structure. For example, Doi and Lewicki, 2014 predicted receptive fields of retinal ganglion cells at different eccentricities of the retina, which are subject to different convergence ratios. More recently, such direct effects on representations have also been studied in deep neural networks (Lindsey et al., 2019). Finally, some approaches employ a different cost function than the mean-squared reconstruction error inherent to the principal component analysis (PCA) method used here. For example, the Information Bottleneck method (Tishby et al., 2000; Tishby and Zaslavsky, 2015) aims to find a low-dimensional representation that preserves information about a specific output variable, while compressing information available in the input. It is quite likely that the choice of cost function would affect the resulting allocations, a question that future research should pursue.

### Implications for sensory processing

The quantitative comparison of the model results with the cortical somatosensory representation in the star-nosed mole provided limited evidence that one of the model predictions—namely, that receptor density and activation statistics should jointly determine cortical organization—is borne out in a biological model system. Further direct tests of the theory are hampered by the lack of reliable quantitative empirical data. Nevertheless, the model makes a number of qualitative predictions that can be directly compared to available data or tested in future experiments.

First, there is additional evidence that both receptor density and stimulus statistics drive allocation in neural populations. Similar to the star-nosed model, the primate somatosensory system also exhibits non-uniform distributions of both stimulus statistics and receptor density. Both of these factors are also broadly correlated, for example, receptor densities are higher on the fingertips, which are also more likely to be in contact with objects (Gonzalez et al., 2014). Importantly, while receptor densities alone can explain some of the magnification observed in the cortical somatosensory homunculus, they cannot account for this effect fully (Corniani and Saal, 2020). Indeed, evidence from non-human primates shows that cortical magnification also critically depends on experience (Xerri et al., 1996; Xerri et al., 1999). Similar results have recently been obtained from the brainstem in mice (Lehnert et al., 2021). Empirically reported differences in sizes of receptive fields between the digit tips and the palm have also been recreated from typical contact across the hand during grasping (Bhand et al., 2011), suggesting an influence of statistics of hand use. Both mechanoreceptor densities (e.g. Verendeev et al., 2015) and hand use statistics (Fragaszy and Crast, 2016) differ across primates, forming the basis for a potential cross-species study. The model presented here demonstrates how both effects can be treated within a single framework driven by information maximization.

Second, it appears that allocation in sensory systems with severely constrained resources is qualitatively in agreement with model predictions. As our results demonstrated, magnification should be more extreme the tighter the bottleneck. The best characterized and most clearly established bottleneck in sensory processing is likely the optical nerve in vision. Given that the optic nerve serves as a narrow bottleneck (approximately 12–27%; assuming 0.71–1.54 million retinal ganglion cells with 80% Midget cells [Curcio and Allen, 1990; Perry et al., 1984] and 4.6 million cones [Curcio et al., 1990]), and that the fovea contains a much higher density of cone receptors than the periphery (Wells-Gray et al., 2016; Curcio et al., 1990), the model would predict a large over-representation of the fovea, agreeing with experimental observations (see Edmondson et al., 2019, for further qualitative evidence). In order to further test the proposed model, comparisons could be made between individuals to study variations within a population. Specifically, it would be expected that optic nerves containing a high number of fibres would devote proportionally fewer of them to the fovea than optic nerves containing smaller numbers of fibres (assuming equal receptor densities and numbers in the retina). These comparisons could be extended across species, taking advantage of the fact that photoreceptor densities and optic nerve fibre counts differ across many primate species (Finlay et al., 2008). Along these lines, recent computational work has shown that the amount of neural resources allocated to the optic nerve can be expected to affect the structure of the receptive field itself (Lindsey et al., 2019). Finally, the extent of cortical areas can be controlled by experimental interventions in animals (Huffman et al., 1999), which would constitute a direct manipulation of the bottleneck.

#### Re-allocation during development, learning, and ageing

Changing receptor densities, stimulus statistics, or resource limits over the life span of an organism should lead to a dynamic re-allocation of the available resources. The most common case will be changes in stimulus statistics as both receptor densities and resources should be relatively stable. In such cases, representations should adapt to the new statistics. For example in touch, changing the nature of tactile inputs affects cortical representations (Coq and Xerri, 1998; Merzenich and Jenkins, 1993; Xerri et al., 1996). Increasing statistics of contact over a region typically leads to expansion of that region in the cortex. Our method suggests that the precise level of expansion would be dependent on the bottleneck width with larger effects observed for narrower bottleneck sizes.

For the other cases, changes in fibre numbers during development and ageing might be interpreted as a change in resources. For example, the optic nerve undergoes a period of rapid fibre loss early during development (Sefton et al., 1985; Provis et al., 1985). Similarly, fibre counts in the optic nerve decrease during ageing (Dolman et al., 1980; Jonas et al., 1990; Sandell and Peters, 2001). In this case, the model would predict a decrease in the size of peripheral representation in the bottleneck compared to the fovea. It is also possible that the receptor densities themselves may change. In touch, ageing leads to reductions in the densities of receptors in older adults (García-Piqueras et al., 2019). In such cases, we have effectively increased the bottleneck width relative to our receptor population, which again should lead to the re-allocation of resources.

#### Expansion and contraction along the sensory hierarchy

Magnification of specific sensory input regions can be observed throughout the sensory hierarchy, from the brainstem and thalamus up to cortical sensory areas. Often, the amount of expansion and contraction differs between areas. For example, the magnification of the fovea increases along the visual pathway from V1 to V4 (Harvey and Dumoulin, 2006). Which of these representations might be best addressed by the model presented here? The main component of the model is decorrelation, which has been shown to be a driving principle for efficient coding in settings where noise is low (Chalk et al., 2018). This is generally the case in low-level sensory processing, for example, in touch (Goodwin and Wheat, 2004). Our results might therefore best match early sensory processing up to perhaps low-level cortical representations. Beyond this, it is likely that noise will be much higher (Shadlen and Newsome, 1998) and for efficient codes to shift away from decorrelation (Hermundstad et al., 2014). Furthermore, while distinct bottlenecks, whether on the number of neurons or the amount of information, are common in low-level processing, it is less clear whether such restrictions constrain cortical processing. Whether and how such different regimes should affect neural allocations remains an open question.

#### Perceptual consequences

Does the allocation of output neurons lead to testable perceptual consequences? While we do not model neurons’ receptive fields directly, allocating more neurons to a given region would increase perceptual spatial acuity for that region. Indeed, cortical magnification and perceptual acuity are correlated in both vision (Duncan and Boynton, 2003) and touch (Duncan and Boynton, 2007). At the same time, the absolute limits on spatial acuity are determined by the density of receptors in each input region. A naive allocation scheme that assigns output neurons proportional to the density of receptors would therefore result in perceptual spatial acuity proportional to receptor distance. Instead, as our results have shown, the allocation should not be proportional in most cases. Specifically, for narrow bottlenecks we would expect relatively higher spatial acuity for regions with high receptor density than might be expected from a proportional allocation. Conversely, for wider bottlenecks this relationship should be reversed and spatial acuity should be better than expected for lower density regions. In agreement with these results, it has been found that in vision spatial resolution declines faster than expected with increasing eccentricity, suggesting a narrow bottleneck in the optic nerve (Anderson et al., 1991).

A second consequence is that spatial acuity should be better in regions with higher activation probability even when receptor densities are equal. Indeed, spatial discrimination in touch improves with training or even just passive stimulation (Van Boven et al., 2000; Godde et al., 2000), up to a limit that is presumably related to receptor density (Wong et al., 2013; Peters et al., 2009). Assuming a fixed resource limit, training may offer improvements to some digits to the detriment of others. Whether this is indeed the case has to our knowledge not yet been empirically tested.

Finally, previous work has shown that non-uniform tuning curves across a population will lead to characteristic biases in perceptual tasks (Wei and Stocker, 2015). While the original formulation assumed that this heterogeneous allocation of output neurons was driven by stimulus statistics alone, we have shown here that it can also be a consequence of receptor densities. Thus, perceptual biases might also be expected to arise from neural populations that efficiently represent sensory inputs sampled by non-uniform receptor populations.

### Limitations and future work

We considered simple linear models based on decorrelation and demonstrated that even such seemingly straightforward models exhibit surprising complexity in how they manage trade-offs in resource allocation under constraints. Specifically, we found that output neurons were not generally allocated proportionally to input neurons or according to some other fixed rule. It therefore stands to reason that similarly complex trade-offs would manifest in more complex models, even though the precise allocations might differ. Nevertheless, since PCA is widely employed for decorrelation and dimensionality reduction, and therefore incorporated into many other algorithms, our results immediately generalize to several other methods. For example, it is straightforward to extend the model with additional constraints (e.g. response sparsity or power constraints) that would not affect the resulting allocations (see ‘Methods’ for details), and therefore the model presented here already covers a number of related models. This includes independent component analysis, which considers higher-order rather than second-order statistics, but relies on a whitened signal, which in the undercomplete (bottleneck) case is obtained via PCA (Hyvärinen and Oja, 2000). Similarly, some models that do incorporate sensory noise and maximize reconstruction accuracy also use an undercomplete set of principal components to reduce the dimensionality of the sensory signal (Doi and Lewicki, 2014). In both of these examples, the resulting receptive field structure will differ, but their allocation—where on the sensory sheet they will fall—will be governed by the same principles described earlier. However, we did not consider nonlinear models and previous work has demonstrated that response nonlinearities can make important contributions to decorrelation (Pitkow and Meister, 2012). Additionally, the precise structure and origin of noise in nonlinear models have been demonstrated to affect efficient coding strategies (Brinkman et al., 2016) and might therefore also influence the resulting allocations. Future work should explore resource allocation in such complex models.

We considered allocations for monotonically decreasing covariance functions. Choosing a negative exponential function and assuming that activations are uncorrelated across different input regions allowed us to derive an analytical solution. How justified are these assumptions? Many sensory systems will likely obey the intuitive notion that receptor correlations decrease with distance; however, there are notable exceptions, for example, in the auditory system (Terashima and Okada, 2012). In touch, the sensory system we are mainly concerned with here, contact might often be made with several fingers (for humans) or rays (for the star-nosed mole) simultaneously, which would induce far-ranging non-monotonic correlations. Unfortunately there is little quantified evidence on the strength of these correlations, rendering their importance unclear. At least for the star-nosed mole, their prey is often small compared to the size of the rays, which move mostly independently, so cross-ray correlations might be low. Furthermore, the receptive fields of neurons in early somatosensory cortex of both humans and star-nosed moles are strongly localized to a single appendage and lie within cortical sub-regions that are clearly delineated from others (Sur et al., 1980; Nelson et al., 1980; Catania and Kaas, 1995). If long-range non-monotonic correlations were strong, we would expect to find many multi-appendage receptive fields and blurry region boundaries. As this is not the case, it therefore stands to reason that either these correlations are not very strong or that there is some other process, perhaps during development, that prevents these correlations affecting the final allocation. Either way, our assumption of monotonically decreasing covariance functions appears to be a good first-order match. Still, the question of how to arrive at robust allocations for more complex covariance functions is an important one that should be considered in future research. While it is possible in principle to solve the allocation problem numerically for arbitrary covariance functions, in practice we noticed that the presence of small numerical errors can affect the sorting process and caution is therefore warranted, especially when considering non-monotonic functions.

## Methods

Our main goal was to derive a method for efficiently allocating output neurons to one of several input regions with different correlational response structure in the presence of constraints on the number of output neurons or amount of information being transmitted. In the following, we focus on the main rationale and equations, while specific proofs can be found in Appendix 1–6. First, we outline the framework for combined whitening and dimensionality reduction that is employed. Next, we demonstrate how this framework can be applied to multiple input regions with different statistics and densities of receptors, and how calculation of the eigenvalues of region-specific covariance matrices solves the problem of resource allocation. Finally, we demonstrate how the problem can be solved analytically for a certain choice of covariance function. The Python code implementing the equations that can be used to recreate the figures in this article is available on GitHub (Edmondson, 2021).

### Combined whitening and dimensionality reduction

We assume that receptors are arranged on a 2D sensory sheet. Correlations in the inputs occur as receptors that are nearby in space have more similar responses. Restricting ourselves to such second-order statistics and assuming that noise is negligible, information is maximized in such a setup by decorrelating the sensory inputs. Here, we decorrelate using a simple linear model. To model the bottleneck, we restrict the number of outputs to $m$ < $n$, where $n$ is the total number of receptors.

If the inputs are represented as a matrix $X$ of dimensions $n\timesz$ (where $z$ is the number of sensory input patterns), then our goal is to find an $m\timesn$ dimensional matrix $W$ such that $W⁢X$ is uncorrelated:

$$
X^{T}W^{T}WX=I.
$$

This is achieved by setting $W=Σ^{−\frac{1}{2}}$, where $Σ=X^{T}X$. Solutions can then be expressed in terms of the diagonal matrix of eigenvalues, $Λ$, and eigenvectors, $Φ$, of the covariance matrix $Σ$:

$$
W=PΛ^{−\frac{1}{2}}Φ^{T}.
$$

Whitening filters are not uniquely determined and optimal decorrelation is obtained with any orthogonal matrix $P$. Setting $P=I$ (plain whitening/PCA) leads to the form shown in the main results section (Equation 1). Localized receptive fields are obtained by setting $P=Φ$, which is known as zero-phase component analysis. In cases with a bottleneck, the solution involves solving an Orthogonal Procrustes problem (Doi and Lewicki, 2014) to find $P^{*}$, an $m$-dimensional orthogonal matrix (where $m$ is the size of the bottleneck) which minimizes the reconstruction error of the inputs and a set of ideal local receptive fields $W_{o⁢p⁢t}$:

$$
P^{∗}=minP‖W_{opt}−PΛ^{−\frac{1}{2}}Φ^{T}‖_{F}^{2},
$$

where $∥⋅∥_{F}$ denotes the Frobenius norm, and $Λ$ and $Φ$ are as above but retaining only those components with the $m$ largest eigenvalues. As the optimally whitened solution is independent of $P$, additional constraints on the solution can be enforced. For example, power constraints are often added, which either limit the total variance or equalize the variance across output neurons, and additional sparsity constraints can be placed on the output neuron’s activity or their receptive field weights (Doi et al., 2012; Doi and Lewicki, 2014). For example, to optimize the sparsity of the weight matrix, one would define an appropriate cost function (such as the $L^{1}$ norm of the weight matrix), then iteratively calculate the gradient with respect to $W$, take an update step to arrive at a new $W_{o⁢p⁢t}$, and determine $P$ as described in Equation 7 (see Doi and Lewicki, 2014, for further details). Importantly for our problem, such additional constraints will affect the precise receptive field structure (through $P$), but not the eigenvalues and eigenvectors included in $Λ$ and $Φ$, respectively. As we will see in the following section, our solution relies on the eigenvalues only, and we can therefore solve the allocation problem irrespective of the precise receptive field structure or additional constraints on the solution.

### Extension to multiple input regions

For our specific problem, we are interested in the case of multiple input regions with different correlational structure (i.e. due to differing receptor density or activation). To simplify the derivations, we approximate different input regions as independent, such that the overall covariance matrix will be a block diagonal matrix. The covariance $Σ$ for two input regions, R1 and R2, can then be expressed as follows:

$$
Σ=[Σ^{(R1)}00Σ^{(R2)}]
$$

This assumption turns out to be a reasonable approximation when region sizes are relatively big and correlations typically do not extend far across the sensory sheet (see Edmondson et al., 2019, for a comparison between block and non-block region covariance matrices in 1D). Furthermore, in many sensory systems, the borders between regions of differing density tend to be relatively narrow. For example, in touch, the digits of the hand are spatially separated, and regions of differing densities, for example, between the digit tips and proximal phalanges, neighbour along the short rather than long axis of the digit. In the star-nosed mole, rays of different innervation densities are separated and neighbour only along their connection to the rest of the nose. However, the block matrix approximation might be problematic in cases with many very small adjacent regions with strong, far-ranging correlations.

The eigenvalues and eigenvectors of a block diagonal covariance matrix also follow the block diagonal form and can be calculated from the individual region covariances alone by a simple application of the Cauchy interlacing theorem. Thus, the corresponding eigenvalues and eigenvectors are

$$
Λ=[Λ^{(R1)}00Λ^{(R2)}]andΦ=[Φ^{(R1)}00Φ^{(R2)}].
$$

Due to the imposed bottleneck, only the $m$ largest eigenvalues from the combined set $Λ$ will be retained. If receptive fields are localized such that they are constrained to fall within a single input region, then an eigenvalue selected from $Λ^{(R1)}$ indicates that the receptive field of the corresponding output neuron will fall onto region R1, and analogously for R2. This fact holds independent of the structure of $P$ that is chosen in Equation 7 because in order to preserve decorrelation a given region cannot contain more output neurons than eigenvalues retained from this region. In the following, we show how the eigenvalues can be calculated analytically for certain covariance functions.

### Calculation of eigenvalues for negative exponential covariance functions

We model the covariance between receptors as a negative exponential function. The covariance matrix is then calculated as a function of distance between pairs of receptors (see Figure 1C). We will first go through the calculation of eigenvalues for the baseline region R1, and then continue with the derivation for R2, which exhibits different receptor density, receptor activation, or both.

For region R1 the covariance between receptors is calculated as

$$
Σ_{ij}^{(R1)}=e^{−\gamma|x_{i}−x_{j}|},
$$

where xi and xj are the locations of the ith and jth receptors, and γ is the decay constant.

The corresponding eigenvalues for an exponential covariance function in the continuous domain can be calculated analytically. The eigenvalue–eigenvector problem is expressed as an integral homogeneous equation, such that for R1 we get

$$
\lambda_{k}⁢ϕ_{k}⁢(x)=\int_{0}^{L}e^{-\gamma⁢|x-y|}⁢ϕ_{k}⁢(y)⁢dy,
$$

where $ϕ_{k}⁢(x)$ is the kth eigenfunction and $\lambda_{k}$ its corresponding eigenvalue. The domain length $L$ is the input region size for one of the dimensions.

It can be shown that solutions to this problem can be related to the Laplacian operator (see Appendix 2 and Appendix 3 for proofs), such that

$$
\lambda_{k}=\frac{2⁢\gamma}{\mu_{k}+\gamma^{2}},
$$

where $\mu_{k}$ are the eigenvalues of the Laplacian operator.

The general solution for the Laplacian eigenvalue problem for a 2D rectangle with Dirichlet boundary conditions is (Strauss, 2007)

$$
\mu_{k}=\mu_{l,m}=\frac{l^{2}⁢\pi^{2}}{L_{1}^{2}}+\frac{m^{2}⁢\pi^{2}}{L_{2}^{2}},l,m=1,2,…,
$$

where L1 and L2 are the sizes of the domain for each dimension.

To calculate the covariance for R2, we need to take into account the potentially different receptor density and response variance for this region. Denoting the ratio of the response variances between both regions by $a$, and the ratio of receptor densities by $d$, the covariance for R2 can be expressed as

$$
Σ_{ij}^{(R2)}=ae^{−d\gamma|x_{i}−x_{j}|}.
$$

It can be seen that $a$ scales the overall covariance matrix (see also Figure 1C), while $d$ changes the spatial extent of the correlations and thereby implicitly accounts for the different receptor density.

The calculation of the eigenvalues for R2 proceeds analogously. The eigenvalue–eigenvector problem is given as

$$
\lambda_{k}⁢ϕ_{k}⁢(x)=\int_{0}^{L⁢\sqrt{d}}a⁢e^{-d⁢\gamma⁢|x-y|}⁢ϕ_{k}⁢(y)⁢dy
$$

Since the receptor density ratio $d$ causes an implicit stretching of the space for the higher density region, the region length $L$ needs to be adjusted in order to keep the effective size of the region constant. In 2D, each axis is therefore scaled by $\sqrt{d}$, resulting in an upper integration limit of $L⁢\sqrt{d}$.

### Allocation in the bottleneck

Given a sensory system with limited representational capacity, different regions may be allocated different amounts of resources. Here, we calculate the allocations over different bottleneck widths for two regions, while the extension to multiple regions is given in Appendix 5. In the following, we assume 2D square regions of equal size for ease of analysis (see Appendix 6 for the equivalent solution in 1D). A single variable $L$ is therefore used to denote the lengths of the squares. Following Equation 12, the eigenvalues for regions R1 and R2 can now be calculated as

$$
R_{1}:\lambda_{l,m}^{(R⁢1)}=\frac{2⁢\gamma}{\pi^{2}⁢L^{-2}⁢(l^{2}+m^{2})+\gamma^{2}}
$$



$$
R_{2}:\lambda_{n,o}^{(R⁢2)}=\frac{2⁢\gamma⁢a⁢\sqrt{d}}{\pi^{2}⁢L^{-2}⁢(n^{2}+o^{2})+\gamma^{2}}
$$

where $l,m$ and $n,o\inN$ enumerate different eigenvalues for regions R1 and R2, respectively.

In order to calculate how many output neurons are allocated to R1 and R2 for different bottleneck widths, we will need to establish an ordering of the eigenvalues, such that for each pair $(l,m)$ we can determine the sorted rank of the eigenvalues. In contrast to the 1D case (see Appendix 6), there is no natural ordering of the eigenvalues in two dimensions; however, a close approximation can be obtained by calculating the number of lattice points enclosed by a quarter circle with radius $p=l^{2}+m^{2}$ (see Appendix 4 for full details). Denoting this function as $N⁢(p)$ and setting $p^{(R⁢1)}=l^{2}+m^{2}$ and $p^{(R⁢2)}=n^{2}+o^{2}$, we can then calculate the number of eigenvalues allocated to R1 as a function of the number of neurons allocated to R2, by setting $\lambda^{(R⁢1)}=\lambda^{(R⁢2)}$ and solving for $p^{(R⁢2)}$. This yields

$$
p^{(R⁢2)}=a⁢\sqrt{d}⁢p^{(R⁢1)}+\frac{L^{2}⁢\gamma^{2}⁢a⁢\sqrt{d}-L^{2}⁢\gamma^{2}}{\pi^{2}}.
$$

As we allocate more neurons to region R1, the ratio $\frac{N(p^{(R1))}}{N⁢(p^{(R⁢2)})}$ simplifies to $lim_{R_{1}→∞}⁡\frac{N⁢(p^{(R⁢1)})}{N⁢(p^{(R⁢2)})}=a⁢\sqrt{d}$. The fraction of neurons allocated to each region therefore depends on the size of the bottleneck and converges to $\frac{1}{1+a⁢\sqrt{d}}$ and $\frac{a⁢\sqrt{d}}{1+a⁢\sqrt{d}}$ for R1 and R2, respectively.

### Alternative covariance functions

To test generalization to other covariance functions that decrease monotonically with receptor distance, we tested a number of functions from the Matérn class, in which the parameter ν controls the smoothness of the function. The negative exponential covariance function we employed in previous sections is equivalent to a Matérn function with $ν=1/2$. Larger values of ν lead to progressively higher correlations for smaller distances and lower correlations for larger distances. Specifically, we tested a Matérn function with $ν=3/2$:

$$
Σ_{ij}^{ν=3/2}=(1+\gamma\sqrt{3}|x_{i}−x_{j}|)e^{−\gamma\sqrt{3}|x_{i}−x_{j}|},
$$

and with $ν=5/2$:

$$
Σ_{ij}^{ν=5/2}=(1+\gamma\sqrt{5}|x_{i}−x_{j}|+\frac{\gamma^{2}5|x_{i}−x_{j}|^{2}}{3})e^{−\gamma\sqrt{5}|x_{i}−x_{j}|}
$$

For simplicity and to obtain numerically stable solutions, all calculations were performed for 1D regions only. For all cases tests, the baseline region contained 500 receptors, while the number of receptors for the other region was determined by the density ratio. Eigenvalues were calculated from the covariance matrix using the eigh method of the numpy Python package (Harris et al., 2006). Comparing the numerically obtained allocation for the negative exponential covariance function with its analytical solutions showed a close match for most bottleneck widths. However, numerical errors increased for wider bottlenecks, where eigenvalues became very small and their decay flattened out, affecting the sorting process. For the analyses here, we therefore restricted ourselves to bottleneck widths where a close match between the numerical and analytical solutions could be obtained. This range was sufficient to demonstrate allocation at narrow bottlenecks and estimate the convergence point for larger ones.

### Calculations for star-nosed mole

The 11 rays were approximated as 2D square regions with areas set to their reported sizes (Sawyer and Catania, 2016). Receptor densities for each ray were calculated as the sensory fibre innervation per mm2 (Catania and Kaas, 1997). Approximations of receptor activation on each ray were calculated from empirical data of prey foraging interactions recorded by Catania and Kaas, 1997. Contact statistics were converted to receptor activation probabilities with receptors following a Bernoulli distribution. Finally, activation variance was calculated as the variance of the Bernoulli distribution (see Appendix 1). The decay rate γ of the negative exponential covariance function was determined for each ray using a model of the typical extent of receptor activation during interaction with prey stimuli of varying sizes. Each ray interacts with varying prey sizes at different frequencies. For example, ray 11 is typically contacted by smaller stimuli more often than other rays. A 2D model of the rays was used to simulate average responses to each stimulus size. Each model ray was tiled with receptors, and circular stimuli of different sizes were then randomly placed over the ray. The radii and frequencies of each stimulus size were based on the prey model (Catania and Kaas, 1997). A ray receptor was marked as active if its coordinate position was within the bounds of the stimuli. Response covariance between receptors was then calculated and an exponential function was fit to find the γ decay parameter. See Table 1 for the full set of parameters. The code implementing the receptor model is available on GitHub (Edmondson, 2021). To determine allocations, eigenvalues associated with each ray were calculated analytically, resulting in allocations for each ray at all bottleneck widths. Three models were compared: first, a ‘density-only’ model, which includes accurate receptor density ratios, but receptor activation ratio remains uniform across all rays; second, an ‘activation-only’ model, which includes heterogeneous receptor activation ratios, but uniform receptor density ratios across all rays; finally, the ‘full model’ combines both accurate densities and receptor activation ratios. Model allocations for each ray were compared to the cortical allocation empirical data from Catania and Kaas, 1997. As the bottleneck size for the star-nosed mole is unknown, the root-mean-square error (RMSE) was calculated for each model at all bottleneck widths. The bottleneck resulting in the lowest error was then selected for each. Allocations for rays at each bottleneck can be found in Figure 6—figure supplement 1A. For the ‘activation-only’ and ‘full’ models, the lowest RMSE values were for bottleneck widths of between 37 and 45%; for the ‘density-only’ model, the RMSE was similar over all bottlenecks widths (see Figure 6—figure supplement 1C). We also tested a ‘baseline model’ where densities and activation were randomly selected for each ray within the possible range of parameters. The aim was to determine how much explained variance within the cortical allocations was due to the selection of the best-fitting bottleneck and how much was due to the specific density and activation parameters. A total of 20 random models were run, and the average $R^{2}$ was –0.09 (see Figure 6—figure supplement 1D).

**Table 1.**
 Model parameters for the star-nosed mole.


<table>
  <thead>
    <tr>
      <th>Ray</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Size</td>
      <td>1.14</td>
      <td>1.21</td>
      <td>1.21</td>
      <td>1.17</td>
      <td>1.08</td>
      <td>1.02</td>
      <td>1.00</td>
      <td>1.13</td>
      <td>1.05</td>
      <td>0.87</td>
      <td>1.10</td>
    </tr>
    <tr>
      <td>Density</td>
      <td>45.78</td>
      <td>47.14</td>
      <td>45.82</td>
      <td>45.69</td>
      <td>45.2</td>
      <td>46.91</td>
      <td>43.3</td>
      <td>44.01</td>
      <td>44.26</td>
      <td>47.92</td>
      <td>50.46</td>
    </tr>
    <tr>
      <td>Activation</td>
      <td>0.03</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.08</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>0.99</td>
      <td>1.00</td>
      <td>1.02</td>
      <td>1.01</td>
      <td>1.00</td>
      <td>1.01</td>
      <td>0.99</td>
      <td>1.04</td>
      <td>1.10</td>
      <td>1.16</td>
      <td>1.27</td>
    </tr>
  </tbody>
</table>

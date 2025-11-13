# Swimming eukaryotic microorganisms exhibit a universal speed distribution

## Authors

- Maciej Lisicki<sup>1</sup> ([ORCID: 0000-0002-6976-0281](https://orcid.org/0000-0002-6976-0281)) †
- Marcos F Velho Rodrigues<sup>1</sup> ([ORCID: 0000-0002-8744-6966](https://orcid.org/0000-0002-8744-6966))
- Raymond E Goldstein<sup>1</sup> ([ORCID: 0000-0003-2645-0598](https://orcid.org/0000-0003-2645-0598))
- Eric Lauga<sup>1</sup> ([ORCID: 0000-0002-8916-2545](https://orcid.org/0000-0002-8916-2545)) †

### Affiliations

1. Department of Applied Mathematics and Theoretical Physics University of Cambridge Cambridge United Kingdom
2. Institute of Theoretical Physics, Faculty of Physics University of Warsaw Warsaw Poland

† Corresponding author

## Abstract

One approach to quantifying biological diversity consists of characterizing the statistical distribution of specific properties of a taxonomic group or habitat. Microorganisms living in fluid environments, and for whom motility is key, exploit propulsion resulting from a rich variety of shapes, forms, and swimming strategies. Here, we explore the variability of swimming speed for unicellular eukaryotes based on published data. The data naturally partitions into that from flagellates (with a small number of flagella) and from ciliates (with tens or more). Despite the morphological and size differences between these groups, each of the two probability distributions of swimming speed are accurately represented by log-normal distributions, with good agreement holding even to fourth moments. Scaling of the distributions by a characteristic speed for each data set leads to a collapse onto an apparently universal distribution. These results suggest a universal way for ecological niches to be populated by abundant microorganisms.

## Introduction

Unicellular eukaryotes comprise a vast, diverse group of organisms that covers virtually all environments and habitats, displaying a menagerie of shapes and forms. Hundreds of species of the ciliate genus Paramecium (Wichterman, 1986) or flagellated Euglena (Buetow, 2011) are found in marine, brackish, and freshwater reservoirs; the green algae Chlamydomonas is distributed in soil and fresh water world-wide (Harris et al., 2009); parasites from the genus Giardia colonize intestines of several vertebrates (Adam, 2001). One of the shared features of these organisms is their motility, crucial for nutrient acquisition and avoidance of danger (Bray, 2001). In the process of evolution, single-celled organisms have developed in a variety of directions, and thus their rich morphology results in a large spectrum of swimming modes (Cappuccinelli, 1980).

Many swimming eukaryotes actuate tail-like appendages called flagella or cilia in order to generate the required thrust (Sleigh, 1975). This is achieved by actively generating deformations along the flagellum, giving rise to a complex waveform. The flagellar axoneme itself is a bundle of nine pairs of microtubule doublets surrounding two central microtubules, termed the '9 + 2' structure (Nicastro et al., 2005), and cross-linking dynein motors, powered by ATP hydrolysis, perform mechanical work by promoting the relative sliding of filaments, resulting in bending deformations.

Although eukaryotic flagella exhibit a diversity of forms and functions (Moran et al., 2014), two large families, ‘flagellates’ and ‘ciliates’, can be distinguished by the shape and beating pattern of their flagella. Flagellates typically have a small number of long flagella distributed along the bodies, and they actuate them to generate thrust. The set of observed movement sequences includes planar undulatory waves and traveling helical waves, either from the base to the tip, or in the opposite direction (Jahn and Votta, 1972; Brennen and Winet, 1977). Flagella attached to the same body might follow different beating patterns, leading to a complex locomotion strategy that often relies also on the resistance the cell body poses to the fluid. In contrast, propulsion of ciliates derives from the motion of a layer of densely-packed and collectively-moving cilia, which are short hair-like flagella covering their bodies. The seminal review paper of Brennen and Winet (1977) lists a few examples from both groups, highlighting their shape, beat form, geometric characteristics and swimming properties. Cilia may also be used for transport of the surrounding fluid, and their cooperativity can lead to directed flow generation. In higher organisms this can be crucial for internal transport processes, as in cytoplasmic streaming within plant cells (Allen and Allen, 1978), or the transport of ova from the ovary to the uterus in female mammals (Lyons et al., 2006).

Here, we turn our attention to these two morphologically different groups of swimmers to explore the variability of their propulsion dynamics within broad taxonomic groups. To this end, we have collected swimming speed data from literature for flagellated eukaryotes and ciliates and analyze them separately (we do not include spermatozoa since they lack (ironically) the capability to reproduce and are thus not living organisms; their swimming characteristics have been studied by Tam and Hosoi, 2011). A careful examination of the statistical properties of the speed distributions for flagellates and ciliates shows that they are not only both captured by log-normal distributions but that, upon rescaling the data by a characteristic swimming speed for each data set, the speed distributions in both types of organisms are essentially identical.

## Results and discussion

We have collected swimming data on 189 unicellular eukaryotic microorganisms ($N_{fl}=112$ flagellates and $N_{cil}=77$ ciliates) (see Appendix 1 and Source data 1). Figure 1 shows a tree encompassing the phyla of organisms studied and sketches of a representative organism from each phylum. A large morphological variation is clearly visible. In addition, we delineate the branches involving aquatic organisms and parasitic species living within hosts. Both groups include ciliates and flagellates.

![Figure 1.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig1-v1.jpg)

**Figure 1.:** Aquatic organisms (living in marine, brackish, or freshwater environments) have their branches drawn in blue while parasitic organisms have their branches drawn in red. Ciliates are indicated by an asterisk after their names. For each phylum marked in bold font, a representative organism has been sketched next to its name. Phylogenetic data from Hinchliff et al. (2015).

Due to the morphological and size differences between ciliates and flagellates, we investigate separately the statistical properties of each. Figure 2 shows the two swimming speed histograms superimposed, based on the raw distributions shown in Figure 2—figure supplement 1, where bin widths have been adjusted to their respective samples using the Freedman-Diaconis rule (see Materials and methods). Ciliates span a much larger range of speeds, up to 7 mm/s, whereas generally smaller flagellates remain in the sub-mm/s range. The inset shows that the number of flagella in both groups leads to a clear division. To compare the two groups further, we have also collected information on the characteristic sizes of swimmers from the available literature, which we list in Appendix 1. The average cell size differs fourfold between the populations (31 µm for flagellates and 132 µm for ciliates) and the distributions, plotted in Figure 2—figure supplement 2, are biased towards the low-size end but they are quantitatively different. In order to explore the physical conditions, we used the data on sizes and speeds to compute the Reynolds number $Re=U⁢L/ν$ for each organism, where $ν=η/ρ$ is the kinematic viscosity of water, with $η$ the viscosity and $ρ$ the density. Since almost no data was available for the viscosity of the fluid in swimming speed measurements, we assumed the standard value $ν=10^{−6}m^{2}/s$ for water for all organisms. The distribution of Reynolds numbers (Figure 2—figure supplement 3), shows that ciliates and flagellates operate in different ranges of $Re$, although for both groups $Re<1$, imposing on them the same limitations of inertia-less Stokes flow (Purcell, 1977; Lauga and Powers, 2009).

![Figure 2.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig2-v1.jpg)

**Figure 2.:** Data points represent the mean and standard deviation of the data in each bin; horizontal error bars represent variability within each bin, vertical error bars show the standard deviation of the count. Inset: number of flagella displayed, where available, for each organism exhibits a clear morphological division between ciliates and flagellates.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Symbols have been randomly placed vertically to avoid overlap.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Each histogram has been rescaled by the average cell size for each group. Although both distributions exhibit a qualitatively similar shape biased toward the low limit, no quantitative similarity is found.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Source data for the characteristic size $L$ and swimming speeds $U$ are listed in Appendix 1.

Furthermore, studies of green algae (Short et al., 2006; Goldstein, 2015) show that an important distinction between the smaller, flagellated species and the largest multicellular ones involves the relative importance of advection and diffusion, as captured by the Péclet number $P⁢e=U⁢L/D$, where $L$ is a typical organism size and $D$ is the diffusion constant of a relevant molecular species. Using the average size $L$ of the cell body in each group of the present study ($L_{fl}=31 \mum$, $L_{cil}=132\mum$) and the median swimming speeds ($U_{fl}=127m/s$, $U_{cil}=784m/s$), and taking $D=10^{3}(\mum)^{2}/s$, we find $P⁢e_{fl}∼3.9$ and $P⁢e_{cil}∼103$, which further justifies analyzing the groups separately; they live in different physical regimes.

Examination of the mean, variance, kurtosis, and higher moments of the data sets suggest that the probabilities $P⁢(U)$ of the swimming speed are well-described by log-normal distributions,

$$
P⁢(U)=\frac{1}{U⁢\sigma⁢\sqrt{2⁢\pi}}⁢exp⁡(-\frac{(ln⁡U-\mu)^{2}}{2⁢\sigma^{2}}),
$$

normalized as $\int_{0}^{∞}𝑑U⁢P⁢(U)=1$, where $\mu$ and $\sigma$ are the mean and the standard deviation of $ln⁡U$. The median $M$ of the distribution is $e^{\mu}$, with units of speed. Log-normal distributions are widely observed across nature in areas such as ecology, physiology, geology and climate science, serving as an empirical model for complex processes shaping a system with many potentially interacting elements (Limpert et al., 2001), particularly when the underlying processes involve proportionate fluctuations or multiplicative noise (Koch, 1966).

The results of fitting (see Materials and methods) are plotted in Figure 3, where the best fits are presented as solid curves, with the shaded areas representing 95% confidence intervals. For flagellates, we find the $M_{fl}=127m/s$ and $\sigma_{fl}=0.978$ while for ciliates, we obtain $M_{cil}=784m/s$ and $\sigma_{cil}=0.936$. Log-normal distributions are known to emerge from an (imperfect) analogy to the Gaussian central limit theorem (see Materials and methods). Since the data are accurately described by this distribution, we conclude that the published literature includes a sufficiently large amount of unbiased data to be able to see the whole distribution.

![Figure 3.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig3-v1.jpg)

**Figure 3.:** Data points represent uncertainties as in Figure 2. Despite the markedly different scales of the distributions, they have similar shapes.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The algebraic moments $ℳ_{n}$ are defined in Equation (4). Error bars representing 95% confidence intervals for fitted parameters, are obscured by markers.

We next compare the statistical variability within groups by examining rescaled distributions (Goldstein, 2018). As each has a characteristic speed $M$, we align the peaks by plotting the distributions versus the variable $U/M$ for each group. Since $P$ has units of 1/speed, we are thus led to the form $P⁢(U,M)=M^{-1}⁢F⁢(U/M)$ for some function $F$. For the log-normal distribution, with $M$ the median, we find

$$
F(ξ)=\frac{1}{ξ\sigma\sqrt{2\pi}}exp⁡(−\frac{ln^{2}⁡ξ}{2\sigma^{2}}),
$$

which now depends on the single parameter $\sigma$ and has a median of unity by construction. To study the similarity of the two distributions we plot the functions $F=M⁢P⁢(U/M)$ for each. As seen in Figure 4, the rescaled distributions are essentially indistinguishable, and this can be traced back to the near identical values of the variances $\sigma$, which are within 5% of each other. The fitting uncertainties shown shaded in Figure 4 suggest a very similar range of variability of the fitted distributions. Furthermore, both the integrated absolute difference between the distributions (0.028) and the Kullback-Leibler divergence (0.0016) are very small (see Materials and methods), demonstrating the close similarity of the two distributions. This similarity is robust to the choice of characteristic speed, as shown in Figure 4—figure supplement 1, where the arithmetic mean $U^{*}$ is used in place of the median.

![Figure 4.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig4-v1.jpg)

**Figure 4.:** Shown are the two fitted log-normal curves for flagellates and ciliates, each multiplied by the distribution median $M$, plotted versus speed normalized by $M$. The distributions for show remarkable similarity and uncertainty of estimation.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/44907/elife-44907-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Data collapse as in the main figure, but using the mean speeds $U^{*}$ instead of the median $M$.A similar quality of data collapse is seen.

In living cells, the sources for intrinsic variability within organisms are well characterized on the molecular and cellular level (Kirkwood et al., 2005) but less is known about variability within taxonomic groups. By dividing unicellular eukaryotes into two major groups on the basis of their difference in morphology, size and swimming strategy, we were able to capture in this paper the log-normal variability within each subset. Using a statistical analysis of the distributions as functions of the median swimming speed for each population we further found an almost identical distribution of swimming speeds for both types of organisms. Our results suggest that the observed log-normal randomness captures a universal way for ecological niches to be populated by abundant microorganisms with similar propulsion characteristics. We note, however, that the distributions of swimming speeds among species do not necessarily reflect the distributions of swimming speeds among individuals, for which we have no available data.

## Materials and methods

### Data collection

Data for ciliates were sourced from 26 research articles, while that for flagellates were extracted from 48 papers (see Appendix 1). Notably, swimming speeds reported in the various studies have been measured under different physiological and environmental conditions, including temperature, viscosity, salinity, oxygenation, pH and light. Therefore we consider the data not as representative of a uniform environment, but instead as arising from a random sampling of a wide range of environmental conditions. In cases where no explicit figure was given for $U$ in a paper, estimates were made using other available data where possible. Size of swimmers has also been included as a characteristic length for each organism. This, however, does not reflect the spread and diversity of sizes within populations of individual but is rather an indication of a typical size, as in the considered studies these data were not available. Information on anisotropy (different width/length) is also not included.

No explicit criteria were imposed for the inclusion in the analyses, apart from the biological classification (i.e. whether the organisms were unicellular eukaryotic ciliates/flagellates). We have used all the data found in literature for these organisms over the course of an extensive search. Since no selection was made, we believe that the observed statistical properties are representative for these groups.

### Data processing and fitting the log-normal distribution

Bin widths in histograms in Figure 2 and Figure 3 have been chosen separately for ciliates and flagellated eukaryotes according to the Freedman-Diaconis rule (Freedman and Diaconis, 1981) taking into account the respective sample sizes and the spread of distributions. The bin width $b$ is then given by the number of observations $N$ and the interquartile range of the data $IQR$ as

$$
b=2⁢\frac{IQR}{N^{1/3}}.
$$

Within each bin in Figure 3, we calculate the mean and the standard deviation for the binned data, which constitute the horizontal error bars. The vertical error bars reflect the uncertainty in the number of counts $N_{j}$ in bin $j$. This is estimated to be Poissonian, and thus the absolute error amounts to $\sqrt{N_{j}}$. Notably, the relative error decays with the number of counts as $1/\sqrt{N_{j}}$.

In fitting the data, we employ the log-normal distribution Equation (1). In general, from from data comprising $N$ measurements, labelled $x_{i}$ ($i=1,…,N$), the $n$-th arithmetic moment $ℳ_{n}$ is the expectation $𝔼⁢(X^{n})$, or

$$
ℳ_{n}=\frac{1}{N}⁢\sumi=1Nx_{i}^{n}
$$

Medians of the data were found by sorting the list of values and picking the middlemost value. For a log-normal distribution, the arithmetic moments are given solely by $\mu$ and $\sigma$ of the associated normal distribution as

$$
ℳ_{n}=M^{n}⁢Σ^{n^{2}},
$$

where we have defined $M=exp⁡(\mu)$ and $Σ=exp⁡(\sigma^{2}/2)$, and note that $M$ is the median of the distribution. Thus, the mean is $M⁢Σ$ and the variance is $M^{2}⁢Σ^{2}⁢(Σ^{2}-1)$. From the first and second moments, we estimate

$$
\mu=ln⁡(\frac{ℳ_{1}^{2}}{\sqrt{ℳ_{2}}}) and \sigma^{2}=ln⁡(\frac{ℳ_{2}}{ℳ_{1}^{2}}).
$$

Having estimated $\mu$ and $\sigma$, we can compute the higher order moments from Equation (5) and compare to those calculated directly from the data, as shown in Figure 3—figure supplement 1.

To fit the data, we have used both the MATLAB fitting routines and the Python scipy.stats module. From these fits we estimated the shape and scale parameters and the 95% confidence intervals in Figure 3 and Figure 4. We emphasize that the fitting procedures use the raw data via the maximum likelihood estimation method, and not the processed histograms, hence the estimated parameters are insensitive to the binning procedure.

For rescaled distributions, the average velocity for each group of organisms was calculated as $U^{∗}=\frac{1}{N_{i}}⁢\sum_{i=1}^{N_{i}}U_{i}$, with $i\in{cil,fl}$. Then, data in each subset have been rescaled by the area under the fitted curve to ensure that the resulting probability density functions $p_{i}$ are normalized as

$$
\int_{0}^{∞}p_{i}⁢(x)⁢dx=1.
$$

In characterizations of biological or ecological diversity, it is often assumed that the examined variables are Gaussian, and thus the distribution of many uncorrelated variables attains the normal distribution by virtue of the Central Limit Theorem (CLT). In the case when random variables in question are positive and have a log-normal distribution, no analogous explicit analytic result is available. Despite that, there is general agreement that a sum of independent log-normal random variables can be well approximated by another log-normal random variable. It has been proven by Szyszkowicz and Yanikome (2009) that the sum of identically distributed equally and positively correlated joint log-normal distributions converges to a log-normal distribution of known characteristics but for uncorrelated variables only estimations are available (Beaulieu et al., 1995). We use these results to conclude that our distributions contain enough data to be unbiased and seen in full.

### Comparisons of distributions

In order to quantify the differences between the fitted distributions, we define the integrated absolute difference $Δ$ between two probability distributions $p⁢(x)$ and $q⁢(x)$ ($x>0$) as

$$
Δ=\int_{0}^{∞}|p⁢(x)-q⁢(x)|⁢dx.
$$

As the probability distributions are normalized, this is a measure of their relative ’distance’. As a second measure, we use the Kullback-Leibler divergence (Kullback and Leibler, 1951),

$$
D⁢(p,q)=\int_{0}^{∞}p⁢(x)⁢ln⁡(\frac{p⁢(x)}{q⁢(x)})⁢dx.
$$

Note that $D⁢(p,q)\neqD⁢(q,p)$ and therefore $D$ is not a distance metric in the space of probability distributions.

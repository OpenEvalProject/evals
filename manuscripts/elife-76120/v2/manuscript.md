# Binary and analog variation of synapses between cortical pyramidal neurons

## Authors

- Sven Dorkenwald<sup>1</sup> ([ORCID: 0000-0003-2352-319X](https://orcid.org/0000-0003-2352-319X)) †
- Nicholas L Turner<sup>1</sup>
- Thomas Macrina<sup>1</sup>
- Kisuk Lee<sup>1</sup>
- Ran Lu<sup>1</sup>
- Jingpeng Wu<sup>1</sup>
- Agnes L Bodor<sup>4</sup>
- Adam A Bleckert<sup>4</sup>
- Derrick Brittain<sup>4</sup>
- Nico Kemnitz<sup>1</sup>
- William M Silversmith<sup>1</sup>
- Dodam Ih<sup>1</sup>
- Jonathan Zung<sup>1</sup>
- Aleksandar Zlateski<sup>1</sup>
- Ignacio Tartavull<sup>1</sup>
- Szi-Chieh Yu<sup>1</sup>
- Sergiy Popovych<sup>1</sup>
- William Wong<sup>1</sup>
- Manuel Castro<sup>1</sup>
- Chris S Jordan<sup>1</sup>
- Alyssa M Wilson<sup>1</sup>
- Emmanouil Froudarakis<sup>5</sup> ([ORCID: 0000-0002-3249-3845](https://orcid.org/0000-0002-3249-3845))
- JoAnn Buchanan<sup>4</sup>
- Marc M Takeno<sup>4</sup> ([ORCID: 0000-0002-8384-7500](https://orcid.org/0000-0002-8384-7500))
- Russel Torres<sup>4</sup> ([ORCID: 0000-0002-2876-4382](https://orcid.org/0000-0002-2876-4382))
- Gayathri Mahalingam<sup>4</sup>
- Forrest Collman<sup>4</sup> ([ORCID: 0000-0002-0280-7022](https://orcid.org/0000-0002-0280-7022))
- Casey M Schneider-Mizell<sup>4</sup> ([ORCID: 0000-0001-9477-3853](https://orcid.org/0000-0001-9477-3853))
- Daniel J Bumbarger<sup>4</sup>
- Yang Li<sup>4</sup>
- Lynne Becker<sup>4</sup>
- Shelby Suckow<sup>4</sup>
- Jacob Reimer<sup>5</sup>
- Andreas S Tolias<sup>5</sup>
- Nuno Macarico da Costa<sup>4</sup> ([ORCID: 0000-0003-2001-4568](https://orcid.org/0000-0003-2001-4568))
- R Clay Reid<sup>4</sup> ([ORCID: 0000-0002-8697-6797](https://orcid.org/0000-0002-8697-6797))
- H Sebastian Seung<sup>1</sup> †

### Affiliations

1. Princeton Neuroscience Institute, Princeton University Princeton United States ([ROR:00hx57361](https://ror.org/00hx57361))
2. Computer Science Department, Princeton University Princeton United States ([ROR:00hx57361](https://ror.org/00hx57361))
3. Brain & Cognitive Sciences Department, Massachusetts Institute of Technology Cambridge United States ([ROR:042nb2s44](https://ror.org/042nb2s44))
4. Allen Institute for Brain Science Seattle United States ([ROR:00dcv1019](https://ror.org/00dcv1019))
5. Department of Neuroscience, Baylor College of Medicine Houston United States ([ROR:02pttbw34](https://ror.org/02pttbw34))
6. Center for Neuroscience and Artificial Intelligence, Baylor College of Medicine Houston United States ([ROR:02pttbw34](https://ror.org/02pttbw34))
7. Department of Electrical and Computer Engineering, Rice University Houston United States ([ROR:008zs3103](https://ror.org/008zs3103))

† Corresponding author

## Abstract

Learning from experience depends at least in part on changes in neuronal connections. We present the largest map of connectivity to date between cortical neurons of a defined type (layer 2/3 [L2/3] pyramidal cells in mouse primary visual cortex), which was enabled by automated analysis of serial section electron microscopy images with improved handling of image defects (250 × 140 × 90 μm3 volume). We used the map to identify constraints on the learning algorithms employed by the cortex. Previous cortical studies modeled a continuum of synapse sizes by a log-normal distribution. A continuum is consistent with most neural network models of learning, in which synaptic strength is a continuously graded analog variable. Here, we show that synapse size, when restricted to synapses between L2/3 pyramidal cells, is well modeled by the sum of a binary variable and an analog variable drawn from a log-normal distribution. Two synapses sharing the same presynaptic and postsynaptic cells are known to be correlated in size. We show that the binary variables of the two synapses are highly correlated, while the analog variables are not. Binary variation could be the outcome of a Hebbian or other synaptic plasticity rule depending on activity signals that are relatively uniform across neuronal arbors, while analog variation may be dominated by other influences such as spontaneous dynamical fluctuations. We discuss the implications for the longstanding hypothesis that activity-dependent plasticity switches synapses between bistable states.

## Introduction

Synapses between excitatory neurons in the cortex and hippocampus are typically made onto spines, tiny thorn-like protrusions from dendrites (Yuste, 2010). In the 2000s, long-term in vivo microscopy studies showed that dendritic spines change in shape and size, and can appear and disappear (Bhatt et al., 2009; Holtmaat and Svoboda, 2009). Spine dynamics were interpreted as synaptic plasticity, because spine volume is well correlated with physiological strength of a synapse (Matsuzaki et al., 2001; Noguchi et al., 2011; Holler et al., 2021). The plasticity was thought to be in part activity-dependent, because spine volume increases with long-term potentiation (Matsuzaki et al., 2004; Kopec et al., 2006; Noguchi et al., 2019). Given that the sizes of other synaptic structures (postsynaptic density, presynaptic active zone, and so on) are well correlated with spine volume and with each other (Harris and Stevens, 1989), we use the catch-all term ‘synapse size’ to refer to the size of any synaptic structure, and ‘synapse strength’ as a synonym.

In the 2000s, some hypothesized the existence of ‘learning spines’ and ‘memory spines’, appearing to define two discrete categories that are structurally and functionally different (Kasai et al., 2003; Bourne and Harris, 2007). Quantitative studies of cortical synapses, however, found no evidence for discreteness (Harris and Stevens, 1989; Arellano, 2007; Loewenstein et al., 2011; Loewenstein et al., 2015; de Vivo et al., 2017; Santuy et al., 2018; Kasai et al., 2021). Whether in theoretical neuroscience or artificial intelligence, it is common for the synaptic strengths in a neural network model to be continuously variable, enabling learning to proceed by the accumulation of arbitrarily small synaptic changes over time.

Here, we reexamine the discrete versus continuous dichotomy using a wiring diagram between 334 layer 2/3 pyramidal cells (L2/3 PyCs) reconstructed from serial section electron microscopy (ssEM) images of mouse primary visual cortex. We show that synapses between L2/3 PyCs are well modeled as a binary mixture of log-normal distributions. If we further restrict consideration to dual connections, two synapses sharing the same presynaptic and postsynaptic cells, the binary mixture exhibits a statistically significant bimodality. It is therefore plausible that the binary mixture reflects two underlying structural states, and is more than merely an improvement in curve fitting.

According to our best fitting mixture model, synapse size is the sum of a binary variable and a log-normal continuous variable. To probe whether these variables are modified by synaptic plasticity, we examined dual connections. Previous analyses of dual connections examined pairs of synapses between the same axon and same dendrite branches (SASD) (Sorra and Harris, 1993; Koester and Johnston, 2005; Bartol et al., 2015; Kasthuri et al., 2015; Dvorkin and Ziv, 2016; Bloss et al., 2018; Motta et al., 2019). They found that such synapse pairs are correlated in size, and the correlations have been attributed to activity-dependent plasticity. In contrast, our population of synapse pairs includes distant synapses made on different branches and is constrained to one cell type (L2/3 PyC). We find that the binary variables are highly correlated, while the continuous variables are not. If we expand the analysis to include a broader population of cortical synapses, bimodality is no longer observed.

The specificity of our synaptic population was made possible because each of the 334 neurons taking part in the 1735 connections in our cortical wiring diagram could be identified as an L2/3 PyC based on a soma and sufficient dendrite and axon contained in the ssEM volume. The closest precedents for wiring diagrams between cortical neurons of a defined type had 29 connections between 43 L2/3 PyCs in mouse visual cortex (Lee et al., 2016), 63 connections between 22 L2 excitatory neurons in mouse medial entorhinal cortex (Schmidt et al., 2017), and 32 connections between 89 L4 neurons in mouse somatosensory cortex (Motta et al., 2019).

Our cortical reconstruction has been made publicly available and used concurrently in other studies (https://www.microns-explorer.org/phase1)(Schneider-Mizell et al., 2021; Turner et al., 2022). The code that generated the reconstruction is already freely available.

## Results

### Handling of ssEM image defects

We acquired a 250 × 140 × 90 μm3 ssEM dataset (Figure 1—figure supplement 1) from L2/3 primary visual cortex of a P36 male mouse at 3.58 × 3.58 × 40 nm3 resolution. When we aligned a pilot subvolume and applied state-of-the-art convolutional nets, we found many reconstruction errors, mainly due to misaligned images and damaged or incompletely imaged sections. This was disappointing given reports that convolutional nets can approach human-level performance on one benchmark ssEM image dataset (Beier et al., 2017; Zeng et al., 2017). The high error rate could be explained by the fact that image defects are difficult to escape in large volumes, though they may be rare in small (<1000 μm3) benchmark datasets.

Indeed, ssEM images were historically considered problematic for automated analysis (Briggman and Bock, 2012; Lee et al., 2019) because they were difficult to align, contained defects caused by lost or damaged serial sections, and had inferior axial resolution (Knott et al., 2008). These difficulties were the motivation for developing block face electron microscopy (bfEM) as an alternative to ssEM (Denk and Horstmann, 2004). Most large-scale ssEM reconstructions have been completely manual, while many large-scale bfEM reconstructions have been semi-automated (19/20 and 5/10 in Table 1 of Kornfeld and Denk, 2018). On the other hand, the higher imaging throughput of ssEM (Nickell and Zeidler, 2019; Yin et al., 2019) makes it suitable for scaling up to volumes that are large enough to encompass the arbors of mammalian neurons.

We supplemented existing algorithms for aligning ssEM images (Saalfeld et al., 2012) with human-in-the-loop capabilities. After manual intervention by a human expert, large misalignments were resolved but small ones still remained near damaged locations and near the borders of the volume. Therefore, we augmented the training data for our convolutional net with simulated misalignments and missing sections (Figure 1a, Figure 1—figure supplement 2). The resulting net was better able to trace neurites through such image defects (Figure 1b, quantification in Figure 1—figure supplement 3). Other methods for handling ssEM image defects are being proposed (Li, 2019), and we can look forward to further gains in automated reconstruction accuracy in the future.

![Figure 1.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig1-v2.jpg)

**Figure 1.:** (a) Ideally, imaging serial sections followed by computational alignment would create an image stack that reflects the original state of the tissue (left). In practice, image stacks end up with missing sections (blue) and misalignments (green). Both kinds of defects are easily simulated when training a convolutional net to detect neuronal boundaries. Small subvolumes are depicted rather than the entire stack, and image defects are typically local rather than extending over an entire section. (b) The resulting net can trace more accurately, even in images not previously seen during training. Here, a series of five sections contains a missing section (blue frame) and a misalignment (green). The net ‘imagines’ the neurites through the missing section, and traces correctly in spite of the misalignment. (c) 3D reconstructions of the neurites exhibit discontinuities at the misalignment, but are correctly traced. (d) All 362 pyramidal cells with somas in the volume (gray), cut away to reveal a few examples (colors). (e) Layer 2/3 (L2/3) pyramidal cell reconstructed from ssEM images of mouse visual cortex. Scale bars: 300 nm (b).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** 250×140×90 µm3 3D image stack from L2/3 of mouse primary visual cortex.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (a) Illustration of a possible pair of neurites that pass through both missing section (cyan) and misalignment (orange) defects. (b) Illustration of a naive segmentation of the pair in (a). (c) Same examples as in Figure 1, accompanied by affinity map. Scale bar: 300 nm. (d) Near a larger misalignment, the displacement is larger than the width of a thin neurite, and the convolutional net is unable to trace through the misalignment. Scale bar 300 nm. (e) A proofread neuron (gray) with segments merged during proofreading (colored). Scale bar: 10 μm. (f) The same proofread neuron in (e) with pieces split during proofreading (colored).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Robustness of three boundary detectors trained with no data augmentation (‘baseline’, blue), simulated missing section (‘missing section’, red), and simulated misalignment (‘misalignment’, yellow) to (a) increasingly large displacement of simulated misalignment and (b) increasing number of simulated consecutive missing sections.

### Wiring diagram between cells in L2/3

After alignment and automatic segmentation (Materials and methods), we semi-automatically identified 417 PyCs and 34 inhibitory cells with somas in the volume based on morphological characteristics and automated nucleus detection (Figure 1d and e, Materials and methods). We then chose a subset of 362 PyCs and 34 inhibitory cells with sufficient neurite length within the volume for proofreading. Remaining errors in the segmentation of these cells were corrected using an interactive system that enabled human experts to split and merge objects.

We estimate that the PyC reconstructions were corrected through ~1300 hr of human proofreading to yield 670 mm cable length (axon: 100 mm, dendrite: 520 mm, perisomatic: 40 mm, Figure 1—figure supplement 2). We examined 12 randomly sampled axons and conservatively estimated that 0.28 merge errors per millimeter remain after proofreading (see Materials and methods for other estimates). The dendrites of the PyCs receive more than one-quarter of the 3.2 million synapses that were automatically detected in the volume (Materials and methods, Turner et al., 2020). However, the synapses onto PyC dendrites are almost all from ‘orphan’ axons, defined as those axonal fragments that belong to somas of unknown location outside the volume. Using these automatically detected synapses as a starting point, we mapped all connections between this set of PyCs and inhibitory cells (Materials and methods). The end result was a wiring diagram of 6210 synapses from 3347 connections in the dataset. The subgraph of PyCs contained 1960 synapses from 1735 connections between 334 L2/3 PyCs (Figure 2a). Note that some connections are multisynaptic, that is, they are mediated by multiple synapses sharing the same presynaptic and postsynaptic cells (Figure 2b, Figure 2—figure supplement 1, see Table 1 for a tabular overview of these statistics).

![Figure 2.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig2-v2.jpg)

**Figure 2.:** (a) Wiring diagram of 362 proofread layer 2/3 (L2/3) pyramidal cells (PyCs) as a directed graph. Two orthogonal views with nodes at 3D locations of cell bodies. Single (gray), dual (blue), and triple, quadruple, quintuple (red) connections. (b) Dual connection from a presynaptic cell (orange) to a postsynaptic cell (gray). Ultrastructure of both synapses can be seen in closeups from the electron microscopy (EM) images. The Euclidean distance between the synapses is 64.3 μm. (c) Normalized distributions of synapses sizes for L2/3 PyCs synapses separated by postsynaptic cell type. (d) Same as (c) for inhibitory cells in layer 2/3. (e) Cumulative distributions of the number of synapses per connection for different pre- and postsynaptic cell types. (f) Distribution of Euclidean distances between synapse pairs of dual connections. Median distance is 46.5 μm. Scale bars: 10 μm (a), 500 nm (b).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Dendritic spines (yellow) and synaptic clefts (red) are rendered in 3D. Most are dual connections (160), but there are also triples (24), quadruples (3), and quintuples (2).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Scale bar: 500nm. In each pair of images, the left shows one section through a synapse, and the right adds the automatically detected cleft as an overlay. Note here that the clefts are associated with postsynaptic densities.

**Table 1.**
 Overview of number of data points obtained in this study.


<table>
  <tbody>
    <tr>
      <td>Number of L2/3 PyCs in dataset</td>
      <td>417</td>
    </tr>
    <tr>
      <td>Number of L2/3 PyCs selected for proofreading</td>
      <td>362</td>
    </tr>
    <tr>
      <td>Number of proofread L2/3 PyCs connecting to any other L2/3 PyCs</td>
      <td>334</td>
    </tr>
    <tr>
      <td>Number of inhibitory cells in dataset</td>
      <td>34</td>
    </tr>
    <tr>
      <td>Number of synapses (automated) in the dataset</td>
      <td>3,239,275</td>
    </tr>
    <tr>
      <td>Number of outgoing synapses (automated) in the dataset from proofread L2/3 PyCs</td>
      <td>10,788</td>
    </tr>
    <tr>
      <td>Number of synapses between L2/3 PyCs</td>
      <td>1960</td>
    </tr>
    <tr>
      <td>Number of connections between L2/3 PyCs</td>
      <td>1735</td>
    </tr>
    <tr>
      <td>Number of connections between L2/3 PyCs with one synapse</td>
      <td>1546</td>
    </tr>
    <tr>
      <td>Number of connections between L2/3 PyCs with two synapses</td>
      <td>160</td>
    </tr>
    <tr>
      <td>Number of connections between L2/3 PyCs with three synapses</td>
      <td>24</td>
    </tr>
    <tr>
      <td>Number of connections between L2/3 PyCs with four synapses</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Number of connections between L2/3 PyCs with five synapses</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

For clarity, we emphasize that our usage of the term ‘multisynaptic’ refers to multiple synapses between a single cell pair. A connection between two PyCs usually (89.1%) contains one synapse, but can contain up to five synapses (2: 9.22%, 3: 1.38%, 4: 0.17%, 5: 0.12%, Figure 2c) (these numbers should be taken with the caveat that the observed number of synapses for a connection is a lower bound for the true number of synapses, because two PyCs with cell bodies in our EM volume could synapse with each other outside the bounds of the volume.). In comparison, only 60.3% of connections from PyCs on inhibitory cells were monosynaptic. Similarly, 62.1% connections made by inhibitory neurons were monosynaptic when targeting other inhibitory neurons, which reduces to only 42.6% when targeting PyCs. While the number of synapses per PyC-PyC connection varies least compared to the other three categories, we observed the highest variance in synapse sizes for these connections (Figure 2d and e). Here, we quantified synaptic cleft size as the number of voxels labeled by the output of our automated cleft detector (Figure 2—figure supplement 2). The dimensions of our reconstructions allowed us to observe dual connections with two synapses more than 100 μm apart (Figure 2b and f), involving different axonal and dendritic branches. Previous analyses reporting correlations between synapses from dual synaptic connections only included synapses that were close to another and were between the SASD.

### Binary latent states

Previous studies of cortical synapses have found a continuum of synapse sizes (Arellano, 2007) that is approximated by a log-normal distribution (Loewenstein et al., 2011; de Vivo et al., 2017; Santuy et al., 2018; Kasai et al., 2021). Even researchers who report bimodally distributed synapse size on a log-scale in hippocampus (Spano et al., 2019) still find log-normally distributed synapse size in neocortex (de Vivo et al., 2017) by the same methods.

We quantified the size of each synapse by the volume of the spine head (Figures 2b and 3a) (spine head volume excludes the spine neck, which is at most only weakly correlated in size with other synaptic structures [Arellano, 2007]). In the following, ‘spine volume’ will serve as a synonym for spine head volume. Spine volumes spanned over two orders of magnitude, though 75% of spines lie within a single order of magnitude. The distribution of spine volumes is highly skewed, with a long tail of large spines (Figure 3b) as observed before (Loewenstein et al., 2011; Santuy et al., 2018; Kasai et al., 2021). Because of the skew, it is helpful to visualize the distribution using a logarithmic scale for spine volume (Loewenstein et al., 2011; Bartol et al., 2015). We were surprised to find that the distribution deviated from normality, due to a ‘knee’ on the right side of the histogram (Figure 3c) (multiple researchers have proposed dynamical models of spine size that are consistent with approximately log-normal stationary distributions [Kasai et al., 2021]). A mixture of two normal distributions was a better fit than a single normal distribution when accounting for the number of free parameters (likelihood ratio test: p<1e-39, n=1960, Materials and methods).

![Figure 3.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-v2.jpg)

**Figure 3.:** (a) Dendritic spine heads (yellow) and clefts (red) of dual connections between layer 2/3 pyramidal cells (L2/3) PyCs. The associated electron microscopy (EM) cutout shows a 2D slice through the synapse. The synapses are centered in the EM images. (b) Skewed histogram of spine volume for all 1960 recurrent synapses between L2/3 PyCs, with a long tail of large spines. (c) Histogram of the spine volumes in (b), logarithmic scale. A mixture (red, solid) of two log-normal distributions (red, dashed) fits better (likelihood ratio test, p<1e-39, n=1960) than a single normal (blue). (d) Spine volumes belonging to dual connections between L2/3 PyCs, modeled by a mixture (red, solid) of two log-normal distributions (red, dashed). (e) Dual connections between L2/3 PyCs, each summarized by the geometric mean of two spine volumes, modeled by a mixture (red, solid) of two log-normal distributions (red, dashed). (f) Mixture of two normal distributions as a probabilistic latent variable model. Each synapse is described by a latent state H that takes on values ‘S’ and ‘L’ according to the toss of a biased coin. Spine volume V is drawn from a log-normal distribution with mean and variance determined by latent state. The curves shown here represent the best fit to the data in (d). Heights are scaled by the probability distribution of the biased coin, known as the mixture weights. (g) Comparison of spine volumes for single (black) and dual (red) connections. (h) Probability of the ‘L’ state (mixture weight) versus number of synapses in the connection. Error bars are standard deviations estimated by bootstrap sampling. Scale bar: 500nm (a). Error bars are $\pm\sqrt{n}$ of the model fit (c, d, e) and standard deviation from bootstrapping (h).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a) Spine volumes belonging to dual connections between layer 2/3 pyramidal cells (L2/3 PyCs). (b) Dual connections between L2/3 PyCs, each summarized by the geometric mean of two spine volumes.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (a) Dual connections between layer 2/3 pyramidal cells (L2/3 PyCs), each summarized by the arithmetic mean of two spine volumes, modeled by a mixture (red, solid) of two normal distributions (red, dashed). (b) Dual connections between L2/3 PyCs, each summarized by the arithmetic mean of two cleft sizes, modeled by a mixture (red, solid) of two normal distributions (red, dashed). Error bars are $\pm\sqrt{n}$ of the model fit.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Plots are analogous to Figure 3 and Figure 3—figure supplement 2. (a) Histogram of same spine volumes, logarithmic scale. A mixture (red, solid) of two log-normal distributions (red, dashed) is shown. (b) Spine volumes belonging to dual connections between layer 2/3 pyramidal cells (L2/3 PyCs), modeled by a mixture (red, solid) of two log-normal distributions (red, dashed). (c) Dual connections between L2/3 PyCs, each summarized by the geometric mean of two spine volumes, modeled by a mixture (red, solid) of two log-normal distributions (red, dashed). (d) Dual connections between L2/3 PyCs, each summarized by the arithmetic mean of two spine volumes, modeled by a mixture (red, solid) of two log-normal distributions (red, dashed).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (a) Spine volumes belonging to dual connections between layer 2/3 (L2/3) pyramidal cells. A bimodal mixture (red, solid) of two normal distributions (red, dashed) is a better fit than a unimodal mixture (blue, solid) of two normal distributions (blue, dashed) (see Holzmann and Vollmer, 2008; p=0.0425, n=320). The bimodal mixture weights are 60:40. (b) Dual connections between L2/3 pyramidal cells, each summarized by the geometric mean of spine volumes. A bimodal mixture (red, solid) of two normal distributions (red, dashed) is a better fit than a unimodal mixture (blue, solid) of two normal distributions (blue, dashed) (likelihood ratio test, p=0.0059, n=160). Error bars are $\pm\sqrt{n}$ of the model fit.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** (a) Spine volume versus cleft size for all layer 2/3 pyramidal cell (L2/3 PyC)-L2/3 PyC synapses. (b) Histogram of same spine volumes, logarithmic scale. A mixture (red, solid) of two normal distributions (red, dashed) fits better (likelihood ratio test, p<1e-63, n=1960) than a single normal (blue). (c) Cleft sizes belonging to dual connections between L2/3 PyCs, modeled by a mixture (red, solid) of two normal distributions (red, dashed, likelihood ratio test, p=0.02, n=320). (d) Dual connections between L2/3 PyCs, each summarized by the geometric mean of two cleft sizes, modeled by a mixture (red, solid) of two normal distributions (red, dashed, likelihood ratio test, p=0.037, n=160). (e) Comparison of cleft sizes for single (black) and dual (red) connections. (f) Probability of the ‘L’ state (mixture weight) versus number of synapses in the connection. Error bars are $\pm\sqrt{n}$ of the model fit.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** (a) Bottom: Spine head volume distribution for single connections (gray) along with synapses for all connections (black). Top: parameter estimates for the component means of single connections, as well as dual connections (red), and triple connections (cyan) and all connections (black). Gray line indicates 90% bootstrap interval over the single connection synapses (1000 samples). Points jittered for clarity. (b) Parameter estimates for component means of the same populations in (a). Box indicates interquartile range across bootstrap samples. Whiskers show 90% bootstrap interval. (c) Parameter estimates for component standard deviations of the same populations in (a). (d) Second component mean estimate from GMM fits on samples of the full dataset model. Full dataset model used for sampling had component weights taken from single connection model, dual connection model, or triple connection model. Points show parameter estimate from the original GMM fit for that connection type. (e) Spine head volume by the number of synapses in a connection.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** (a) Examples of spine apparatus (SA) in electron microscopy (EM) images. Scale bar: 300 nm. (b) Spine volume distributions of synapses with no endoplasmic reticulum (ER) (blue), smooth ER (yellow), and SA (red). (c) Likelihood of SA (red) and ‘L’ state (black) conditioned on spine volume. (d) Spine volume distribution conditioned on SA (red) compared with size distribution conditioned on ‘L’ state (black). Inset: Joint probability distribution of SA within dual connections. Error bars are $\pm\sqrt{n}$ of the model fit.

We next restricted our consideration to the 320 synapses belonging to 160 dual connections between the PyCs. Again, a binary mixture of normal distributions was a better fit (Figure 3d, see Figure 3—figure supplement 1 for linear plots) than a single normal distribution (normal fit not shown, likelihood ratio test: p<1e-7, n=320). Next, we made use of the fact that synapses from dual connections are paired. For each pair, we computed the geometric mean (i.e., mean in log-space) of spine volumes and found that this quantity is also well modeled by a binary mixture of normal distributions (Figure 3e, see Figure 3—figure supplement 2 for the arithmetic mean, Figure 3—figure supplement 3 for histograms without model fits and Table 2 for fit results).

**Table 2.**
 Overview of results from log-normal mixture fits for different synapse subpopulations.


<table>
  <thead>
    <tr>
      <th rowspan="2">Subset of L2/3 L2/3 PyC synapses</th>
      <th colspan="3">S</th>
      <th colspan="3">L</th>
      <th rowspan="2">N</th>
    </tr>
    <tr>
      <th>Mean(log10 µm3)</th>
      <th>Std(log10 µm3)</th>
      <th>Weight</th>
      <th>Mean (log10 µm3)</th>
      <th>Std(log10 µm3)</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>All synapses</td>
      <td>–1.42</td>
      <td>0.24</td>
      <td>0.77</td>
      <td>–0.77</td>
      <td>0.22</td>
      <td>0.23</td>
      <td>1960</td>
    </tr>
    <tr>
      <td>Single synapses</td>
      <td>–1.41</td>
      <td>0.24</td>
      <td>0.81</td>
      <td>–0.76</td>
      <td>0.21</td>
      <td>0.19</td>
      <td>1546</td>
    </tr>
    <tr>
      <td>Dual synapses</td>
      <td>–1.44</td>
      <td>0.23</td>
      <td>0.64</td>
      <td>–0.77</td>
      <td>0.21</td>
      <td>0.36</td>
      <td>320</td>
    </tr>
    <tr>
      <td>Triple synapses</td>
      <td>–1.49</td>
      <td>0.17</td>
      <td>0.36</td>
      <td>–0.86</td>
      <td>0.30</td>
      <td>0.64</td>
      <td>72</td>
    </tr>
    <tr>
      <td>All synapses with weights refitted to single synapses</td>
      <td>(–1.42)</td>
      <td>(0.24)</td>
      <td>0.80</td>
      <td>(–0.77)</td>
      <td>(0.248)</td>
      <td>0.20</td>
      <td>1960 and 1546</td>
    </tr>
    <tr>
      <td>All synapses with weights refitted to dual synapses</td>
      <td>(–1.42)</td>
      <td>(0.24)</td>
      <td>0.66</td>
      <td>(–0.77)</td>
      <td>(0.248)</td>
      <td>0.34</td>
      <td>1960 and 320</td>
    </tr>
    <tr>
      <td>All synapses with weights refitted to triple synapses</td>
      <td>(–1.42)</td>
      <td>(0.24)</td>
      <td>0.52</td>
      <td>(–0.77)</td>
      <td>(0.248)</td>
      <td>0.48</td>
      <td>1960 and 72</td>
    </tr>
    <tr>
      <td>Geometric mean of dual synapses</td>
      <td>–1.44</td>
      <td>0.16</td>
      <td>0.58</td>
      <td>–0.87</td>
      <td>0.18</td>
      <td>0.42</td>
      <td>160</td>
    </tr>
    <tr>
      <td>Arithmetic mean of dual synapses</td>
      <td>–1.43</td>
      <td>0.16</td>
      <td>0.53</td>
      <td>–0.85</td>
      <td>0.18</td>
      <td>0.47</td>
      <td>160</td>
    </tr>
  </tbody>
</table>

A binary mixture model might merely be a convenient way of approximating deviations from normality. We would like to know whether the components of our binary mixture could correspond to two structural states of synapses. A mixture of two normal distributions can be unimodal or bimodal, depending on the model parameters (for example, if the two normal distributions have the same weight and standard deviation, then the mixture is unimodal if and only if the separation between the means is at most twice the standard deviation) (Robertson and Fryer, 1969). When comparing best fit unimodal and bimodal mixtures we found that a bimodal model yields a significantly superior fit for spine volume and geometric mean of spine volume (p=0.0425, n=320; Figure 3—figure supplement 4, see Holzmann and Vollmer, 2008, for statistical methods).

A binary mixture model can be interpreted in terms of a binary latent variable. According to such an interpretation, synapses are drawn from two latent states (Figure 3f). In ‘S’ and ‘L’ states, spine volumes are drawn from log-normal distributions with small and large means, respectively. It should be noted that there is some overlap between mixture components (Figure 3f), so that an S synapse can be larger than an L synapse.

To validate this finding with a different measurement of synapse size, the number of voxels labeled by the output of our automated cleft detector. We found a close relationship between spine volume and cleft size in our data (Figure 3—figure supplement 5a), in accord with previous studies (Harris and Stevens, 1989; Arellano, 2007; Bartol et al., 2015). When spine volume is replaced by cleft size in the preceding analysis, we obtain similar results (Figure 3—figure supplement 5).

According to our two-state model, the parameters of the mixture components should stay roughly constant for the distribution of any subset of synapses between L2/3 PyCs. To probe model dependence on the number of synapses per connection, we individually fit a Gaussian mixture to the population of synapses from single, dual, and triple connections and found that their mixture components were not significantly different. Parameter estimates for these fits lie within sampling error of the single connection dataset (Figure 3—figure supplement 6). When comparing these distributions we observed an overrepresentation of large synapses for dual connections compared to single connections (Figure 3g). We wondered if the previously reported mean spine volume increase with the number of synapses per connection (Figure 3—figure supplement 6, Bloss et al., 2018) could be explained with a synapse redistribution between the latent states. This time, we only fit the component weights to single, dual, triple connections while keeping the Gaussian components constant (see Materials and methods). We found a linear increase in fraction of synapses in the ‘L’ state with the number of synapses per connection (Figure 3h). (This relationship was found for the observed number of synapses. On average, this number is expected to increase with the true number of synapses. Therefore, mean spine volume is also expected to increase with the true number of synapses per connection)

Large spines have been reported to contain an intracellular organelle called a spine apparatus (SA), which is a specialized form of smooth endoplasmic reticulum (ER) (Peters and Kaiserman-Abramof, 1970; Spacek, 1985; Harris and Stevens, 1989). We manually annotated SA in all dendritic spines of all synapses between L2/3 PyCs, and confirmed quantitatively that the probability of an SA increases with spine volume (Figure 3—figure supplement 7, Materials and methods).

### Correlations at dual connections

Positive correlation between synapse sizes at dual connections has been reported previously in hippocampus (Sorra and Harris, 1993; Bartol et al., 2015; Bloss et al., 2018) and neocortex (Kasthuri et al., 2015; Motta et al., 2019) for synapse pairs formed by the same axonal and dendritic branches. According to our binary mixture model, synapse size is the sum of a binary variable and a log-normal continuous variable. We decided to quantify the contributions of these variables to synapse size correlations.

The dendritic spines for all dual connections between L2/3 PyCs are rendered in Figure 2—figure supplement 1. A positive correlation between the two spine volumes of each dual connection is evident in a scatter plot of the spine volume pairs (Figure 4a, see Figure 4—figure supplement 1 for an unoccluded plot; Pearson’s r=0.418). We fit the joint distribution of the spine volumes by a mixture model like Figure 3f, while allowing the latent states to be correlated (Figure 4a and f, see Table 3 for fit results, Figure 4—figure supplement 2 for the same analysis for synaptic cleft sizes). In the best-fitting model, SS occurs roughly half the time, LL one-third of the time, and the mixed states (SL, LS) occur more rarely (Figure 4e). The low probability of the mixed states can be seen directly in the scarcity of points in the upper left and lower right corners of the scatter plot (Figure 4a). Pearson’s phi coefficient, the specialization of Pearson’s correlation coefficient to binary variables, is 0.637.

![Figure 4.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig4-v2.jpg)

**Figure 4.:** (a) Scatter plot of spine volumes (black, lexicographic ordering) for dual connections. Data points are mirrored across the diagonal (gray). The joint distribution is fit by a mixture model (orange) like that of Figure 3f, but with latent states correlated as in (e). (b) Projecting the points onto the vertical axis yields a histogram of spine volumes for dual connections (Figure 3d). Model is derived from the joint distribution. (c) Projecting onto the x=y diagonal yields a histogram of the geometric mean of spine volumes (Figure 3e). Model is derived from the joint distribution. (d) Projecting onto the x=−y diagonal yields a histogram of the ratio of spine volumes. (e) The latent states of synapses in a dual connection (H1 and H2) are more likely to be the same (SS or LL) than different (SL/LS), as shown by the joint probability distribution. (f) When conditioned on the latent states, the spine volumes (V1 and V2) are statistically independent, as shown in this dependency diagram of the model. (g), (h) Sampling synapse pairs to SS and LL states according to their state probabilities. The top shows a kernel density estimation of multiple iterations of sampling. The bottom shows the distribution of Pearson’s r correlations across many sampling rounds (N=10,000). Error bars are $\pm\sqrt{n}$ of the model fit.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Plots are analogous to Figure 4 and Figure 4—figure supplement 4. (a) Synapse pairs from all dual connections. (b) Dual connections of synapse pairs less than the median distance apart. (c) Dual connections of synapse pairs more than the median distance apart.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (a) The latent states of synapses in a dual connection are positively correlated with each other. The latent states are more likely to be the same (SS or LL) rather than different (SL or LS), as shown by the joint probability distribution. (b) Scatter plot of cleft sizes (black, lexicographic ordering) for dual connections between layer 2/3 (L2/3) pyramidal cells. Scatter plot points are mirrored across the diagonal (gray). The joint distribution is fit by a mixture model (orange) like that of Figure 3f, but with latent states that are correlated as described below. (c) Projecting the points onto the vertical axis yields a histogram of cleft sizes for dual connections, the same as in Figure 3d. Model is derived from the joint distribution. (d) Projecting the points onto the x=y diagonal yields a histogram of the geometric mean of cleft sizes for dual connections, the same as in Figure 3e. Model is derived from the joint distribution. (e) Projecting the points onto the x=−y diagonal yields a histogram of the ratio of cleft sizes for dual connections. Error bars are $\pm\sqrt{n}$ of the model fit.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** We assigned the synapse pairs from the 160 dual synaptic connections to their most likely state (SS, SL, LS, LL) and subtracted the mean of the binary components. (a) shows the residual components. (b) shows the residual components when restricting assignments to SS and LL states.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Spine volumes (left) and cleft sizes (right). (a) Dual connections of synapse pairs less than 46.5 μm apart (phi = 0.534). (b) Dual connections of synapse pairs more than 46.5 μm apart (phi = 0.745). (c) Mixture component means of model fits as a function of the minimum distance separating synapse pairs. (d) Mixture component means of model fits as a function of the maximum distance separating synapse pairs. Error bars are $\pm\sqrt{n}$ of the model fit.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** Synapses are shuffled between dual connections to measure the correlations between synapses that have the same axon (red) or the same dendrite (blue) against a fully random baseline (black). Shuffled synapses are not allowed to be paired with other synapses within their original connection. Each shuffling procedure was performed on a subset of data where at least one valid shuffling exists for each synapse (e.g. where each dendrite receives at least two dual connections). (a–c) Joint distributions of spine head volumes in the dual connections used for shuffling. Slope of linear fit shows Pearson’s r value. (a) Subset of data used for random shuffling (all 160 synapse pairs). r=0.42. (b) Subset of data used for axon-preserved shuffling (141 pairs). r=0.45. (c) Subset of data used for dendrite-preserved shuffling (89 pairs). r=0.51. (d) Example shuffle of data in (a). r=0.00. (e) Example shuffle of data in (b). r=–0.08. (f) Example shuffle of data in (c). r=–0.11. (g) Diagram of a possible shuffle of two dual synaptic connections onto the same dendrite. (h) Distribution of Pearson’s r correlation for paired spine head volumes after shuffling (100,000 shuffles each). Dashed lines indicate correlation value for the unshuffled subset. (i) Distribution of Pearson’s phi correlation for paired spine head volumes after shuffling.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/76120/elife-76120-fig4-figsupp6-v2.jpg)

**Figure 4—figure supplement 6.:** Spine volumes (top) and cleft sizes (bottom). (a) Distribution of synapse sizes in dual connections received by layer 2/3 (L2/3) pyramidal cells, including those from orphan axons (566 synapses). (b) Distribution of geometric means of synapse sizes in same dual connections as in (a) (283 pairs). (c) Joint distribution of synapse sizes in dual connections received by L2/3 pyramidal cells, including those from orphan axons (283 pairs). (d) Distribution of synapse sizes for excitatory synapses received by L2/3 pyramidal cells, including those from orphan axons (700 synapses).

**Table 3.**
 Overview of results from hidden Markov model (HMM) log-normal component fits for different dual synaptic connection subpopulations.


<table>
  <thead>
    <tr>
      <th rowspan="2">Subset of L2/3 L2/3 PyC dual synaptic connections</th>
      <th colspan="2">S</th>
      <th colspan="2">L</th>
      <th colspan="3">Weights</th>
      <th rowspan="2">Pearson’s phi</th>
      <th rowspan="2">N</th>
    </tr>
    <tr>
      <th>Mean(log10 µm3)</th>
      <th>Std(log10 µm3)</th>
      <th>Mean (log10 µm3)</th>
      <th>Std(log10 µm3)</th>
      <th>SS</th>
      <th>SL+LS</th>
      <th>LL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>All connections</td>
      <td>–1.470</td>
      <td>0.216</td>
      <td>–0.833</td>
      <td>0.244</td>
      <td>0.490</td>
      <td>0.177</td>
      <td>0.333</td>
      <td>0.637</td>
      <td>160</td>
    </tr>
    <tr>
      <td>Dist &lt;median dist</td>
      <td>–1.506</td>
      <td>0.212</td>
      <td>–0.861</td>
      <td>0.243</td>
      <td>0.427</td>
      <td>0.232</td>
      <td>0.342</td>
      <td>0.534</td>
      <td>80</td>
    </tr>
    <tr>
      <td>Dist &gt;median dist</td>
      <td>–1.449</td>
      <td>0.207</td>
      <td>–0.818</td>
      <td>0.251</td>
      <td>0.529</td>
      <td>0.123</td>
      <td>0.348</td>
      <td>0.745</td>
      <td>80</td>
    </tr>
  </tbody>
</table>

Our mixture model assumes that the spine volumes are independent when conditioned on the latent states. To visualize whether this assumption is justified by the data, Figure 4 shows 1D projections of the joint distribution onto different axes. The projection onto the vertical axis (Figure 4b) is the marginal distribution, the overall size distribution for all synapses that belong to dual connections (same as Figure 3d). The projection onto the x=y diagonal (Figure 4c) is the distribution of the geometric mean of spine volume for each dual connection (same as Figure 3e). The projection onto the x=−y diagonal (Figure 4d) is the distribution of the ratio of spine volumes for each dual connection. For all three projections, the good fit suggests that the data are consistent with the mixture model’s assumption of isotropic normal distributions for the LL and SS states. (The x=y and vertical histograms look bimodal because they are different projections of the same two ‘bumps’ in the joint distribution. If the probability of the mixed state (LS/SL) were high, there would be two additional off-diagonal bumps in the joint distribution, and the x=y diagonal histogram would acquire another peak in the middle. In reality the probability of the mixed state is low, so the x=y diagonal histogram is well modeled by two mixture components. The widths of the bumps are the same in both projections, but the distance between the bumps is longer in the x=y diagonal histogram by a factor of root two. This explains why the mixture components are better separated in the distribution of geometric means (Figure 3e) than in the marginal distribution (Figure 3d), and hence why the statistical significance of bimodality is stronger for the geometric means.)

For a quantitative test of the isotropy assumption, we resampled observed spine volume pairs with weightings computed from the posterior probabilities of the SS and LL states (Figure 4g and h). If the model were consistent with the data, the resampled data would obey an isotropic normal distribution. Indeed, Pearson’s correlation for the resampled data is not significantly greater than zero (Figure 4g and h). Therefore, the spine volumes in a dual connection are approximately uncorrelated when conditioned on the latent states. We validated this result by examining the residual synapse sizes after subtracting the binary components and found no remaining correlation between then synapse pairs (Figure 4—figure supplement 3).

### Specificity of latent state correlations

Could the observed correlations between synapses in dual connections be caused by crosstalk between plasticity of neighboring synapses (<10 μm separation), which has been reported previously (Harvey and Svoboda, 2007; Harvey et al., 2008)? We looked for dependence of latent state correlations on separation by splitting dual connections into two groups, those with synapses nearer or farther than the median Euclidean distance in the volume of 46.5 μm. Both groups were fit by mixture models with positive correlations between latent variables (near: φ = 0.53, far: φ = 0.75, see Materials and methods, Figure 4—figure supplement 4). In other words, for dual connections involving pairs of distant synapses, the latent state correlations are still strong.

We also considered the possibility of correlations in pairs of synapses sharing the same presynaptic cell but not the same postsynaptic cell, or pairs of synapses sharing the same postsynaptic cell but not the same presynaptic cell (Bartol et al., 2015; Kasthuri et al., 2015; Dvorkin and Ziv, 2016; Bloss et al., 2018; Motta et al., 2019). We randomly drew such synapse pairs from the set of synapses that belong to dual connections (and hence belong to PyCs that participate in dual connections). Correlations in the latent state or synapse size were negligible (same axon: φ = −0.11±0.08 SD, r = −0.06±0.06 SD; same dendrite: φ = −0.06±0.06 SD, r = −0.13±0.05 SD; Figure 4—figure supplement 5), similar to previous findings (Bloss et al., 2018; Motta et al., 2019).

## Discussion

Our synapse size correlations are specific to pairs of synapses that share both the same presynaptic and postsynaptic L2/3 PyCs, similar to previous findings (Sorra and Harris, 1993; Koester and Johnston, 2005; Bartol et al., 2015; Kasthuri et al., 2015; Dvorkin and Ziv, 2016; Bloss et al., 2018; Motta et al., 2019). We have further demonstrated that the correlations exist even for large spatial separations between synapses. More importantly, we have shown the correlations are confined to the binary latent variables in our synapse size model; the log-normal analog variables exhibit little or no correlation.

The correlations in the binary variables could arise from a Hebbian or other synaptic plasticity rule driven by presynaptic and postsynaptic activity signals that are relatively uniform across neuronal arbors. Such signals are shared by synapses in a multisynaptic connection (Sorra and Harris, 1993; Koester and Johnston, 2005; Bartol et al., 2015; Kasthuri et al., 2015; Dvorkin and Ziv, 2016; Bloss et al., 2018; Motta et al., 2019).

We speculate that much of the analog variation arises from the spontaneous dynamical fluctuations that have been observed at single dendritic spines through time-lapse imaging. Computational models of this temporal variance suggest that it can account for much of the population variance (Yasumatsu et al., 2008; Loewenstein et al., 2011; Statman et al., 2014). Experiments have shown that large dynamical fluctuations persist even after activity is pharmacologically blocked (Yasumatsu et al., 2008; Statman et al., 2014; Sando et al., 2017; Sigler, 2017). Another possibility is that the analog variation arises from plasticity driven by activity-related signals that are local to neighborhoods within neuronal arbors.

It remains unclear whether the binary latent variable in our model reflects some underlying bistable mechanism or is merely a convenient statistical description. Our latent variable model is consistent with the scenario in which synapses behave like binary switches that are flipped by activity-dependent plasticity. Switch-like behavior could arise from bistable networks of molecular interactions at synapses (Lisman, 1985), has been observed in physiology experiments on synaptic plasticity (Petersen et al., 1998; O’Connor et al., 2005), and has been the basis of a number of computational models of memory (Tsodyks, 1990; Amit and Fusi, 1994; Fusi et al., 2005). In this scenario, synapses only appear volatile due to fluctuations in the analog variable (Loewenstein et al., 2011), which obscures an underlying bistability.

In a second scenario, the bimodality of synapse size does not reflect an underlying bistability. For example, models of activity-dependent plasticity can cause synapses to partition into two clusters located at upper and lower bounds for synaptic size (Song et al., 2000; van Rossum et al., 2000; Rubin et al., 2001). In this scenario, synapses are intrinsically volatile, and bimodality arises because learning drives them to extremes.

We would like to suggest that the first scenario of binary switches is somewhat more plausible, for two reasons. First, it is unclear how the second scenario could lead to strong correlations in the binary variable. Second, it is unclear how the second scenario could be consistent with the little or no correlation that remains in our data once the contribution from the binary latent variables is removed. This argument is tentative; more experimental and theoretical studies are needed to draw firmer conclusions.

Bimodality and strong correlations were found for a restricted ensemble of synapses, those belonging to dual connections between L2/3 PyCs. However, bimodality is not observed for the ensemble of all excitatory synapses onto L2/3 PyCs, including those from orphan axons (Figure 4—figure supplement 6). This ensemble is similar to ones studied previously, that is, synapses onto L2/3 PyCs (Arellano, 2007), L4 neurons (Motta et al., 2019), or L5 PyCs (Loewenstein et al., 2011). Bimodality and strong correlations are also not observed for the ensemble of all dual connections received by L2/3 PyCs, including those from orphan axons (Figure 4—figure supplement 6). Because our findings are based on a highly specific population of synapses, they are not inconsistent with previous studies that failed to find evidence for discreteness of cortical synapses (Harris and Stevens, 1989; Arellano, 2007; Loewenstein et al., 2011; Loewenstein et al., 2015; de Vivo et al., 2017; Santuy et al., 2018).

Why does the bimodality disappear when one includes dual connections with orphan axons? In our view, the simplest explanation is that this is due to the fact that orphan axons come from a mixed population of cell types, each one with its different distribution of synapse sizes. While each cell type to cell type connection might have its unique properties, they are lost to the observer when combining connections between different cell types together.

Bimodality and correlations may turn out to be heterogeneous across classes of neocortical synapses. Heterogeneity in the hippocampus has been demonstrated by the finding that dual connections onto granule cell dendrites in the middle molecular layer of dentate gyrus (Bromer et al., 2018) do not exhibit the correlations that are found in stratum radiatum of CA1 (Bartol et al., 2015; Bloss et al., 2018).

Since the physiological strength of a multisynaptic connection can be approximately predicted from the sum of synaptic sizes (Holler-Rickauer et al., 2019), our S and L latent states and their correlations have implications for the debate over whether infrequent strong connections play a disproportionate role in cortical computation (Song et al., 2005; Cossell et al., 2015; Scholl, 2019).

## Materials and methods

### Mouse

All procedures were in accordance with the Institutional Animal Care and Use Committees at the Baylor College of Medicine and the Allen Institute for Brain Science. Same sex littermates were housed together in individual cages with one to four mice per cage. Mice were maintained on a regular diurnal lighting cycle (12:12 light:dark) with ad libitum access to food and water and nesting material for environmental enrichment. Mice were housed in the Taub Mouse Facility of Baylor College of Medicine, accredited by AAALAC (The Association for Assessment and Accreditation of Laboratory Animal Care International). The animal used for this experiment was healthy and not involved in any previous procedure or experiment.

### Mouse line

Functional imaging was performed in a transgenic mouse expressing fluorescent GCaMP6f. For this dataset, the mouse we used was a triple heterozygote for the following three genes: (1) Cre driver: CamKIIa-Cre (Jax: 005359 https://www.jax.org/strain/005359), (2) tTA driver: B6;CBA-Tg(Camk2a-tTA)1Mmay/J (Jax: 003010 https://www.jax.org/strain/003010), (3) GCaMP6f Reporter: Ai93 (Allen Institute).

### Cranial window surgery

Anesthesia was induced with 3% isoflurane and maintained with 1.5–2% isoflurane during the surgical procedure. Mice were injected with 5–10 mg/kg ketoprofen subcutaneously at the start of the surgery. Anesthetized mice were placed in a stereotaxic head holder (Kopf Instruments) and their body temperature was maintained at 37°C throughout the surgery using a homeothermic blanket system (Harvard Instruments). After shaving the scalp, bupivicane (0.05 cc, 0.5%, Marcaine) was applied subcutaneously, and after 10–20 min an approximately 1 cm2 area of skin was removed above the skull and the underlying fascia was scraped and removed. The wound margins were sealed with a thin layer of surgical glue (VetBond, 3 M), and a 13 mm stainless-steel washer clamped in the headbar was attached with dental cement (Dentsply Grip Cement). At this point, the mouse was removed from the stereotax and the skull was held stationary on a small platform by means of the newly attached headbar. Using a surgical drill and HP 1/2 burr, a 3 mm craniotomy was made centered on the primary visual cortex (V1; 2.7 mm lateral of the midline, contacting the lambda suture), and the exposed cortex was washed with ACSF (125 mM NaCl, 5 mM KCl, 10 mM glucose, 10 mM HEPES, 2 mM CaCl2, 2 mM MgSO4). The cortical window was then sealed with a 3 mm coverslip (Warner Instruments), using cyanoacrylate glue (VetBond). The mouse was allowed to recover for 1–2 hr prior to the imaging session. After imaging, the washer was released from the headbar and the mouse was returned to the home cage.

### Widefield imaging

Prior to two-photon imaging, we acquired a low-magnification image of the 3 mm craniotomy under standard illumination.

### Two-photon imaging

Imaging for candidate mice was performed in V1, in a 400 × 400 × 200 µm3 volume with the superficial surface of the volume at the border of L1 and L2/3, approximately 100 µm below the pia. Laser excitation was at 920 nm at 25–45 mW depending on depth. The objective used was a 25× Nikon objective with a numerical aperture of 1.1, and the imaging point spread function was measured with 500 nm beads and was approximately 0.5 × 0.5 × 3 µm3 in x, y, and z. Pixel dimensions of each imaging frame were 256×256.

### Tissue preparation and staining

The protocol of Hua et al., 2015, was combined with the protocol of Tapia et al., 2012, to accommodate a smaller tissue size and to improve TEM contrast. Mice were transcardially perfused with 2.5% paraformaldehyde and 1.25% glutaraldehyde. After dissection, 200 μm thick coronal slices were cut with a vibratome and post-fixed for 12–48 hr. Following several washes in CB (0.1 M cacodylate buffer pH 7.4), the slices were fixed with 2% osmium tetroxide in CB for 90 min, immersed in 2.5% potassium ferricyanide in CB for 90 min, washed with deionized (DI) water for 2× 30 min, and treated with freshly made and filtered 1% aqueous thiocarbohydrazide at 40°C for 10 min. The slices were washed 2× 30 min with DI water and treated again with 2% osmium tetroxide in water for 30 min. Double washes in DI water for 30 min each were followed by immersion in 1% aqueous uranyl acetate overnight at 4°C. The next morning, the slices in the same solution were placed in a heat block to raise the temperature to 50°C for 2 hr. The slices were washed twice in DI water for 30 min each, and then incubated in Walton’s lead aspartate pH 5.0 for 2 hr at 50°C in the heat block. After another double wash in DI water for 30 min each, the slices were dehydrated in an ascending ethanol series (50%, 70%, 90%, 100%×3) 10 min each and two transition fluid steps of 100% acetonitrile for 20 min each. Infiltration with acetonitrile:resin dilutions (2p:1p, 1p:1p and 2p:1p) were performed on a gyratory shaker overnight for 4 days. Slices were placed in 100% resin for 24 hr followed by embedding in Hard Plus resin (EMS, Hatfield, PA). Slices were cured in a 60°C oven for 96 hr. The best slice based on tissue quality and overlap with the 2p region was selected.

### Sectioning and collection

A Leica EM UC7 ultramicrotome and a Diatome 35-degree diamond ultra-knife were used for sectioning at a speed of 0.3 mm/s. Eight to ten serial sections were cut at 40 nm thickness to form a ribbon, after which the microtome thickness setting was set to 0 in order to release the ribbon from the knife. Using an eyelash probe, pairs of ribbons were collected onto copper grids covered by 50 nm thick LUXEL film.

### Transmission electron microscopy

We made several custom modifications to a JEOL-1200EXII 120 kV transmission electron microscope (Yin et al., 2019). A column extension and scintillator magnified the nominal field of view by 10-fold with negligible loss of resolution. A high-resolution, large-format camera allowed fields of view as large as (13 µm)2 at 3.58 nm resolution. Magnification reduced the electron density at the phosphor, so a high-sensitivity sCMOS camera was selected and the scintillator composition tuned to generate high-quality EM images with exposure times of 90–200 ms. Sections were acquired as a grid of 3840 × 3840 px images (‘tiles’) with 15% overlap.

### Alignment in two blocks

The dataset was divided by sections into two blocks (1216 and 970 sections), with the first block containing substantially more folds. Initial alignment and reconstruction tests proceeded on the second block of the dataset. After achieving satisfactory results, the first block was added, and the whole dataset was further aligned to produce the final 3D image. The alignment process included stitching (assembling all tiles into a single image per section), rough alignment (aligning the set of section images with one affine per section), coarse alignment (nonlinear alignment on lower resolution data), and fine alignment (nonlinear alignment on higher resolution data).

### Alignment, block one

The tiles of the first block were stitched into one montaged image per section and rough aligned using a set of customized and automated modules based on the ‘TrakEM2’ (Cardona et al., 2012) and ‘Render’ (Zheng et al., 2018) software packages.

#### Stitching

After acquisition, a multiplicative intensity correction based on average pixel intensity was applied to the images followed by a lens distortion of individual tiles using nonlinear transformations (Kaynig et al., 2010). Once these corrections were applied, correspondences between tiles within a section were computed using SIFT features, and each tile was modeled with a rigid transform.

#### Rough alignment

Using 20× downsampled stitched images, neighboring sections were roughly aligned (Saalfeld et al., 2012). Correspondences were again computed using SIFT features, and each section was modeled with a regularized affine transform (90% affine+10% rigid), and all correspondences and constraints were used to generate the final model of one affine transform per tile. These models were used to render the final stitched section image into rough alignment with block two.

### Alignment, block two

The second block was stitched and aligned using the methods of Saalfeld et al., 2012, as implemented in Alembic (Macrina and Ih, 2019).

#### Stitching

For each section, tiles containing tissue without clear image defects were contrast normalized by centering the intensities at the same location in each tile, stretching the overall distribution between the 5th and 95th intensity percentiles. During imaging, a 20× downsampled overview image of the section was also acquired. Each tile was first placed according to stage coordinates, approximately translated based on normalized cross-correlation (NCC) with the overview image, and then finely translated based on NCC with neighboring tiles. Block matching was performed in the regions of overlap between tiles using NCC with 140 px block radius, 400 px search radius, and a spacing of 200 px. Matches were manually inspected with 1× coverage, setting per-tile-pair thresholds for peak of match correlogram, distance between first and second peaks of match correlograms, and correlogram covariance, and less frequently, targeted match removal. A graphical user interface was developed to allow the operator to fine-tune parameters on a section-by-section basis, so that a skilled operator completed inspection in 40 hr. Each tile was modeled as a spring mesh, with nodes located at the center of each blockmatch operation, spring constants 1/100th of the constant for the between-tile springs, and the energy of all spring meshes within a section were minimized to a fractional tolerance of 10–8 using nonlinear conjugate gradient. The final render used a piecewise affine model defined by the mesh before and after relaxation, and maximum intensity blending.

#### Rough alignment

Using 20× downsampled images, block matching between neighboring sections proceeded using NCC with 50 px block radius, 125 px search radius, and 250 px spacing. Matches were computed between nearest neighbor section pairs, then filtered manually in 8 hr. Correspondences were used to develop a regularized affine model per section (90% affine+10% rigid), which was rendered at full image resolution.

#### Coarse alignment

Using 4× downsampled images, NCC-based block matching proceeded 300 px block radius, 200 px search radius, and 500 px spacing. Matches were computed between nearest and next-nearest section pairs, then manually filtered by a skilled operator in 24 hr. Each section was modeled as a spring mesh with spring constants 1/10th of the constant for the between-section springs, and the energy of all spring meshes within the block were minimized to a fractional tolerance of 10–8 using nonlinear conjugate gradient. The final render used a piecewise affine model defined by the mesh.

#### Fine alignment

Using 2× downsampled images, NCC-based block matching proceeded 200 px block radius, 113 px search radius, and 100 px spacing. Matches were computed between nearest and next-nearest section pairs, then manually filtered by a skilled operator in 24 hr. Modeling and rendering proceeded as with coarse alignment, using spring constants were 1/20th of the constant for the between-section springs.

### Alignment, whole dataset

Blank sections were inserted manually between sections where the cutting thickness appeared larger than normal (11). The alignment of the whole dataset was further refined using the methods of Saalfeld et al., 2012, as implemented in Alembic (Macrina and Ih, 2019).

#### Coarse alignment

Using 64× downsampled images, NCC-based block matching proceeded 128 px block radius, 512 px search radius, and 128 px spacing. Matches were computed between neighboring and next-nearest neighboring sections, as well as 24 manually identified section pairs with greater separation, then manually inspected in 70 hr. Section spring meshes had spring constants 1/20th of the constant for the between-section springs. Mesh relaxation was completed in blocks of 15 sections, 5 of which were overlapping with the previous block (2 sections fixed), each block relaxing to a fractional tolerance of 10–8. Rendering proceeded similarly as before.

#### Fine alignment

Using 4× downsampled images, NCC-based block matching proceeded 128 px block radius, 512 px search radius, and 128 px spacing. Matches were computed between the same section pairs as in coarse alignment. Matches were excluded only by heuristics. Modeling and rendering proceeded similar to coarse alignment, with spring constants 1/100th the constant for the between-section springs. Rendered image intensities were linearly rescaled in each section based on the 5th and 95th percentile pixel values.

### Image volume estimation

The imaged tissue has a trapezoidal shape in the sectioning plane. Landmark points were placed in the aligned images to measure this shape. We report cuboid dimensions for simplicity and comparison using the trapezoid midsegment length. The original trapezoid has a short base length of 216.9 μm, long base length of 286.2 μm, and height 138.3 μm. The imaged data has 2176 sections, which measures 87.04 μm with a 40 nm slice thickness.

### Image defect handling

Cracks, folds, and contaminants were manually annotated as binary masks on 256× downsampled images, dilated by 2 px, then inverted to form a defect mask. A tissue mask was created using nonzero pixels in the 256× downsampled image, then eroded by 2 px to exclude misalignments at the edge of the image. The image mask is the union of the tissue and defect masks, and it was upsampled and applied during the final render to set pixels not included in the mask to zero. We created a segmentation mask by excluding voxels that had been excluded by the image mask for three consecutive sections. The segmentation mask was applied after affinity prediction to set affinities not included in the mask to zero.

### Affinity prediction

Human experts used VAST (Berger et al., 2018) to manually segment multiple subvolumes from the current dataset and a similar dataset from mouse V1. Annotated voxels totaled 1.29 billion at full image resolution.

We trained a 3D convolutional network to generate 3 nearest neighbor (Turaga et al., 2010) and 13 long-range affinity maps (Lee, 2017). Each long-range affinity map was constructed by comparing an equivalence relation (Jain et al., 2010) of pairs of voxels spanned by an ‘offset’ edge (to preceding voxels at distances of 4, 8, 12, and 16 in x and y, and 2, 3, 4 in z). Only the nearest neighbor affinities were used beyond inference time; long-range affinities were used solely for training. The network architecture was modified from the ‘Residual Symmetric U-Net’ of Lee, 2017. We trained on input patches of size 128 × 128 × 20 at 7.16 × 7.16 × 40 nm3 resolution. The prediction during training was bilinearly upsampled to full image resolution before calculating the loss.

Training utilized synchronous gradient updates computed by four Nvidia Titan X Pascal GPUs each with a different input patch. We used the AMSGrad variant (Reddi et al., 2019) of the Adam optimizer (Kingma and Ba, 2014), with PyTorch’s default settings except step size parameter α=0.001. We used the binary cross-entropy loss with ‘inverse margin’ of 0.1 Huang and Jain, 2013; patch-wise class rebalancing (Lee, 2017) to compensate for the lower frequency of boundary voxels; training data augmentation including flip/rotate by 90 degrees, brightness and contrast perturbations, warping distortions, misalignment/missing section simulation, and out-of-focus simulation (Lee, 2017); and lastly several new types of data augmentation including the simulation of lost section and co-occurrence of misalignment/missing/lost section.

Distributed computation of affinity maps used chunkflow (Wu et al., 2019). The computation was done with images at 7.16 × 7.16 × 40 nm3 resolution. The whole volume was divided into 1280 × 1280 × 140 chunks overlapping by 128 × 128 × 10, and each chunk was processed as a task. The tasks were injected into a queue (Amazon Web Service Simple Queue Service). For 2.5 days, 1000 workers (Google Cloud n1-highmem-4 with 4 vCPUs and 26 GB RAM, deployed in Docker image using Kubernetes) fetched and executed tasks from the queue as follows. The worker read the corresponding chunk from Google Cloud Storage using CloudVolume (Silversmith et al., 2021), and applied previously computed masks to black out regions with image defects. The chunk was divided into 256 × 256 × 20 patches with 50% overlap. Each patch was processed to yield an affinity map using PZNet, a CPU inference framework (Popovych, 2020). The overlapping output patches were multiplied by a bump function, which weights the voxels according to the distance from patch center, for smooth blending and then summed. The result was cropped to 1024 × 1024 × 120 vx and then previously computed segmentation masks were applied (see Image defect handling above).

### Watershed and size-dependent single linkage clustering

The affinity map was divided into 514 × 514 × 130 chunks that overlapped by 2 voxels in each direction. For each chunk we ran a watershed and clustering algorithm (Zlateski and Seung, 2015) with special handling of chunk boundaries. If the descending flow of watershed terminated prematurely at a chunk boundary, the voxels around the boundary were saved to disk so that domain construction could be completed later on. Decisions about merging boundary domains were delayed, and information was written to disk so decisions could be made later. After the chunks were individually processed, they were stitched together in a hierarchical fashion. Each level of the hierarchy processed the previously delayed domain construction and clustering decisions in chunk interiors. Upon reaching the top of the hierarchy, the chunk encompassed the entire volume, and all previously delayed decisions were completed.

### Mean affinity agglomeration

The watershed supervoxels and affinity map were divided into 513 × 513 × 129 chunks that overlapped by 1 in each direction. Each chunk was processed using mean affinity agglomeration (Lee, 2017; Funke et al., 2019). Agglomeration decisions at chunk boundaries were delayed, and information about the decisions was saved to disk. After the chunks were individually processed, they were combined in a hierarchical fashion similar to the watershed process.

### Training with data augmentations

We performed preliminary experiments on the effect of training data augmentation by simulating image defects on the publicly available SNEMI3D challenge dataset (http://brainiac2.mit.edu/SNEMI3D). We partitioned the SNEMI3D training volume of 1024 × 1024 × 100 voxels into the center crop of 512 × 512 × 100 voxels for validation, and the rest for training. Then we trained three convolutional nets to detect neuronal boundaries, one without any data augmentation (‘baseline’), and the other two with simulated missing section (‘missing section’) and simulated misalignment (‘misalignment’) data augmentation, respectively. After training the three nets, we measured the robustness of each net to varying degrees of simulated image defects on the validation set (Figure 1—figure supplement 3). In the first measurement, we simulated a misalignment at the middle of the validation volume with varying numbers of pixel displacement. In the second measurement, we introduced varying numbers of consecutive missing sections at the middle of the validation volume. For each configuration of simulation, we ran an inference pipeline with the three nets to produce respective segmentations, and computed the variation of information error metric to measure the quality of the segmentations. For the measurement against simulated misalignment, we applied connected components to recompute the ground truth segmentation after introducing a misalignment, such that we separated a single object into two distinct objects if the object is completely broken by the misalignment (e.g. the displacement of misalignment larger than the diameter of neurite).

### Synaptic cleft detection

Synaptic clefts were annotated by human annotators within a 310.7 μm3 volume, which was split into 203.2 μm3 training, 53.7 μm3 validation, and 53.7 μm3 test sets. We trained a version of the Residual Symmetric U-Net (Lee, 2017) with 3 downsampling levels instead of 4, 90 feature maps at the third downsampling instead of 64, and ‘resize’ upsampling rather than strided transposed convolution. Images and labels were downsampled to 7.16 × 7.16 × 40 nm3 image resolution. To augment the training data, input patches were transformed by (1) introducing misalignments of up to 17 pixels, (2) blacking out up to five sections, (3) blurring up to five sections, (4) warping, (5) varying brightness and contrast, and (6) flipping and rotating by multiples of 90 degrees. Training used PyTorch (Paszke et al., 2017) and the Adam optimizer (Kingma and Ba, 2014). The learning rate started from 10−3, and was manually annealed three times (505k training updates), before adding 67.2 μm3 of extra training data for another 670k updates. The extra training data focused on false positive examples from the network’s predictions at 505k training updates, mostly around blood vessels. The trained network achieved 93.0% precision and 90.9% recall in detecting clefts of the test set. This network was applied to the entire dataset using the same distributed inference setup as affinity map inference. Connected components of the thresholded network output that were at least 50 voxels at 7.16 × 7.16 × 40 nm3 resolution were retained as predicted synaptic clefts.

### Synaptic partner assignment

Presynaptic and postsynaptic partners were annotated for 387 clefts, which were split into 196, 100, and 91 examples for training, validation, and test sets. A network was trained to perform synaptic partner assignment via a voxel association task (Turner et al., 2020). Architecture and augmentations were the same as for the synaptic cleft detector. Test set accuracy was 98.9% after 710k training iterations. The volume was separated into non-overlapping chunks of size 7.33 × 7.33 × 42.7 μm3 (1024 × 1024 × 1068 voxels), and the net was applied to each cleft in each chunk. This yielded a single prediction for interior clefts. For a cleft that crossed at least one boundary, we chose the prediction from the chunk which contained the most voxels of that cleft. Cleft predictions were merged if they connected the same synaptic partners and their centers-of-mass were within 1 μm. This resulted in 3,556,643 final cleft predictions.

### PyC proofreading

The mean affinity graph of watershed supervoxels was stored in our PyChunkedGraph backend, which uses an octree to provide spatial embedding for fast updates of the connected component sets from local edits. We modified the Neuroglancer frontend (Maitin-Shepard et al., 2019) to interface with this backend so users directly edit the agglomerations by adding and removing edges in the supervoxel graph (merge and split agglomerations). Connected components of this graph are meshed in chunks of supervoxels, and chunks affected by edits are updated in real time so users can always see a 3D representation of the current segmentation. Using a keypoint for each object (e.g. soma centroid), objects are assigned the unique ID of the connected component for the supervoxel which contains that location. This provides a means to update the object’s ID as edits are made.

Cell bodies in the EM volume were semi-automatically identified. PyCs were identified by morphological features, including density of dendritic spines, presence of apical and basal dendrites, direction of main axon trunk, and cell body shape. We selected a subset of the 417 PyCs for proofreading based on the amount of visible neurite within the volume. A team of annotators used the meshes to detect errors in dendritic trunks and axonal arbors, then to correct those errors with 50,000 manual edits in 1044 person-hours. After these edits, PyCs were skeletonized, and both the branch and end points of these skeletons were identified automatically (with false negative rates of 1.7% and 1.4%, as estimated by annotators). Human annotators reviewed each point to ensure no merge errors and extend split errors where possible (210 person-hours). Putative broken spines targeted by PyCs were identified by selecting objects that received one or two synapses. Annotators reviewed, and attached these with 174 edits in 24 person-hours. Some difficult mergers came from small axonal boutons merged to dendrites. We identified these cases by inspecting any predicted presynaptic site that resided within 7.5 μm of a postsynaptic site of the same cell, and corrected them with 50 person-hours.

### Estimation of final error rates

After proofreading was complete, a single annotator inspected 12 PyCs and spent 18 hr to identify all remaining errors in dendritic trunks and axonal arbors. The PyC proofreading protocol was designed to correct all merge errors, though not necessarily correct split errors caused by a masked segmentation. So this error estimation includes all merge errors identified and only split errors caused by less than three consecutive sections of masked segmentation. For 18.7 mm of dendritic path length inspected, three false splits (falsely excluding 160 synapses) and three false merges (falsely including 117 synapses) were identified (99% precision and 99% recall for incoming synapses). For 3.6 mm of axonal path length inspected, two false splits (falsely excluding four synapses) and one false merge (falsely including nine synapses) were identified (98% precision and 99% recall for outgoing synapses). We also sampled four dendritic branches with a collective 0.7 mm of path length, and identified 126 false negative and 0 false positive spines (88% recall of spines).

### PyC-PyC synapse proofreading

Synapses between PyC were extracted from the automatically detected and assigned synapses. We reviewed these synapses manually with 2× redundancy (1972 correct synapses out of 2433 putative synapses). Two predicted synapses out of these were ‘merged’ with other synaptic clefts. These cases were excluded from further analysis. One synapse was incorrectly assigned to a PyC and removed from the analysis. One other synapse was ‘split’ into two predictions, and these predictions were merged for analysis. We were not able to calculate spine head volumes for 8 out of these 1968 synapses and they were excluded from the analysis. This left 1960 synapses admitted into the analysis.

### Synapses from other excitatory axons

We randomly sampled synapses onto the PyCs and evaluated whether they are excitatory or inhibitory based on their shape, appearance, and targeted compartment (n=881 single excitatory synapses). We randomly sampled connections of two synapses onto PyCs and evaluated whether their presynaptic axon is excitatory or inhibitory and checked for reconstruction errors. Here, we manually checked that the automatically reconstructed path between the two synapses along the 3D mesh of the axon was error free (n=446 pairs of excitatory synapses). Those axons were allowed to contain errors elsewhere and we did not proofread any axons to obtain these pairs.

### Dendritic spine heads

We extracted a 7.33 × 7.33 × 4 μm3 cutout around the centroid of each synapse. The postsynaptic segment within that cutout was skeletonized using kimimaro (https://github.com/seung-lab/kimimaro; Silversmith and Wu, 2022), yielding a set of paths traveling from a root node to each leaf. The root node was defined as the node furthest from the synapse coordinate. Skeleton nodes participating in fewer than three paths were labeled as ‘spine’ while others were labeled as ‘shaft’. The shaft labels were dilated along the skeleton until either (1) the distance to the segment boundary of the next node was more than 50 nm less than that of the closest (shaft) branch point, or (2) dilation went 200 nodes beyond the branch point. Each synapse was associated with its closest skeleton node, and a contiguous set of ‘spine’ labeled nodes. We finally separated spine head from neck by analyzing the distance to the segment boundary (DB) moving from the root of the spine to the tip. After segmenting the spine from the rest of the segment, we chose two anchor points: (1) the point with minimum DB value across the half of the spine toward the dendritic shaft and (2) the point with maximum DB value across the other half. A cut point was defined as the first skeleton node moving from anchor 1 to anchor 2 whose DB value was greater than ⅓ DBanchor1 + ⅔ DBanchor2. Accounting for slight fluctuations in the DB value, we started the scan for the cut point at the closest node to anchor 2 that had DB value less than ⅕ DBanchor1 + ⅘ DBanchor2. The skeleton of the spine head was defined as the nodes beyond this cut point to a leaf node, and the spine head mesh was defined as all spine mesh vertices which were closest to the spine head skeleton. The mesh of each head was identified as the subset of the postsynaptic segment mesh whose closest skeleton node was contained within the nodes labeled as spine head. We then estimated the volume of this spine head by computationally sealing this mesh and computing its volume.

We identified poor extractions by computing the distance between each synapse centroid and the nearest node of its inferred spine head mesh. We inspected each inferred spine head for which this distance was greater than 35 nm, and corrected the mesh estimates of mistakes by relabeling mesh vertices using a 3D voronoi tessellation of points placed by a human annotator.

### Endoplasmic reticulum

We manually evaluated all spine heads between PyCs admitted to the analysis for whether they contained an SA, ER that is not an SA (ER), or none (no ER). We required the presence of at least two (usually parallel) membrane saccules for SA. Dense plate/region (synaptopodin and actin) in-between membrane saccules was an indicator. We found SA in spine heads and spine necks. We considered single lumens of organelles connecting to the ER network in the shaft as ER. We required that every ER could be traced back to the ER network in the dendritic shaft.

### Mixture models

Spine volumes and synapse sizes were log10-transformed before statistical modeling. Maximum likelihood estimation for a binary mixture of normal distributions used the expectation-maximization algorithm as implemented by Pomegranate (Schreiber, 2017). The algorithm was initialized using the k-means algorithm with the number of clusters set to equal the number of mixture components. For cleft size, the normal distributions were truncated at a lower bound of log10(50) voxels, the same cutoff used in cleft detection. The truncation was implemented by modifications to the source code of Pomegranate. In this mixture model, each fitted distribution is parameterized with a mean, standard deviation, and weight per mixture component. In the case of two components we also refer to the weights as S and L state fractions. We used the square root of the estimated counts as errors on the fitted distributions (Figure 3c, d and e). To estimate errors on the state weights, we bootstrapped the population of synapses and reported the standard deviation of the fitted weights.

### Hidden Markov models

The joint distribution at dual connections was fitted by hidden Markov models (HMMs) with two latent states and emission probabilities given by normal distributions as described in the previous section. In total this resulted in four state probabilities (SS, SL, LS, LL). HMMs are trained on ordered pairs. Because there is no inherent order of the synapse pair from dual connections, we included each synapse pair twice in the dataset, one for each order.

### Correlation analysis

We assigned state probabilities to each dual synaptic pair using the best fit HMM. The following was done for SS and LL states independently. In each sampling iteration (n=10,000) we assigned individual synapse pairs to the state in question based on independent biased coin flips weighted by their respective state probability. For every such obtained sample we computed the Pearson’s correlation of the sampled population of synapses (Figure 4g and h). For visualization in Figure 4g and h we applied a kernel density estimation (bw = 0.15 in log10-space).

### Parametric test for bimodality

For binary mixtures of normal distributions, the parameter regimes for bimodal and unimodal behaviors are known (Robertson and Fryer, 1969). The likelihood ratio of the best-fitting bimodal and unimodal models can be used for model selection (Holzmann and Vollmer, 2008). Mixture models were fit using Sequential Least Squares Programming using constraints on the parameter regimes for unimodal fits. We computed p-values using Chernoff’s extension to boundary points of hypothesis sets (Chernoff, 1954) of Wilks’ theorem governing asymptotics of the likelihood ratio (Wilks, 1938).

### Skeletonization

We developed a skeletonization algorithm similar to Sato et al., 2000, that operates on meshes. For each connected component of the mesh graph, we identify a root and find the shortest path to the farthest node. This procedure is repeated after invalidating all mesh nodes within the proximity of the visited nodes until no nodes are left to visit. We make our implementation available through our package MeshParty (https://github.com/sdorkenw/MeshParty; Dorkenwald et al., 2020).

### Estimation of path lengths

We skeletonized all PyCs and labeled their first branch points close to the soma according to the compartment type of the downstream branches (axon, dendrite, ambiguous). If no branch point existed in close proximity a point at similar distance was placed. All skeleton nodes downstream from these nodes seen from the soma were labeled according to these labels. This allowed us to estimate path lengths for each compartment with the path up to the first branch point labeled as perisomatic (axon: 100 mm, dendrite: 520 mm, perisomatic: 40 mm, ambiguous: 10 mm). We estimated that our skeletons were overestimated by 11% due to following the mesh edges and corrected all reported pathlengths accordingly.

### Code availability

All software is open source and available at http://github.com/seung-lab if not otherwise mentioned.

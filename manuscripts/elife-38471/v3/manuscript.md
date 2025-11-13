# Unsupervised discovery of temporal sequences in high-dimensional datasets, with applications to neuroscience

## Authors

- Emily L Mackevicius<sup>1</sup> ([ORCID: 0000-0001-6593-4398](https://orcid.org/0000-0001-6593-4398))
- Andrew H Bahle<sup>1</sup> ([ORCID: 0000-0003-0567-7195](https://orcid.org/0000-0003-0567-7195))
- Alex H Williams<sup>2</sup> ([ORCID: 0000-0001-5853-103X](https://orcid.org/0000-0001-5853-103X))
- Shijie Gu<sup>1</sup> ([ORCID: 0000-0001-6257-5756](https://orcid.org/0000-0001-6257-5756))
- Natalia I Denisenko<sup>1</sup>
- Mark S Goldman<sup>4</sup> ([ORCID: 0000-0002-8257-2314](https://orcid.org/0000-0002-8257-2314)) †
- Michale S Fee<sup>1</sup> ([ORCID: 0000-0001-7539-1745](https://orcid.org/0000-0001-7539-1745)) †

### Affiliations

1. McGovern Institute for Brain Research, Department of Brain and Cognitive Sciences Massachusetts Institute of Technology Cambridge United States
2. Neurosciences Program Stanford University Stanford United States
3. School of Life Sciences and Technology ShanghaiTech University Shanghai China
4. Center for Neuroscience, Department of Neurobiology, Physiology and Behavior University of California, Davis Davis United States
5. Department of Ophthamology and Vision Science University of California, Davis Davis United States

† Corresponding author

## Abstract

Identifying low-dimensional features that describe large-scale neural recordings is a major challenge in neuroscience. Repeated temporal patterns (sequences) are thought to be a salient feature of neural dynamics, but are not succinctly captured by traditional dimensionality reduction techniques. Here, we describe a software toolbox—called seqNMF—with new methods for extracting informative, non-redundant, sequences from high-dimensional neural data, testing the significance of these extracted patterns, and assessing the prevalence of sequential structure in data. We test these methods on simulated data under multiple noise conditions, and on several real neural and behavioral data sets. In hippocampal data, seqNMF identifies neural sequences that match those calculated manually by reference to behavioral events. In songbird data, seqNMF discovers neural sequences in untutored birds that lack stereotyped songs. Thus, by identifying temporal structure directly from neural data, seqNMF enables dissection of complex neural circuits without relying on temporal references from stimuli or behavioral outputs.

## Introduction

The ability to detect and analyze temporal sequences embedded in a complex sensory stream is an essential cognitive function, and as such is a necessary capability of neuronal circuits in the brain (Clegg et al., 1998; Janata and Grafton, 2003; Bapi et al., 2005; Hawkins and Ahmad, 2016), as well as artificial intelligence systems (Cui et al., 2016; Sutskever et al., 2014). The detection and characterization of temporal structure in signals is also useful for the analysis of many forms of physical and biological data. In neuroscience, recent advances in technology for electrophysiological and optical measurements of neural activity have enabled the simultaneous recording of hundreds or thousands of neurons (Chen et al., 2013; Kim et al., 2016; Scholvin et al., 2016; Jun et al., 2017), in which neuronal dynamics are often structured in sparse sequences (Hahnloser et al., 2002; Harvey et al., 2012; MacDonald et al., 2011; Okubo et al., 2015; Fujisawa et al., 2008; Pastalkova et al., 2008). Such sequences can be identified by averaging across multiple trials, but only in cases where an animal receives a temporally precise sensory stimulus, or executes a sufficiently stereotyped behavioral task.

Neural sequences have been hypothesized to play crucial roles over a much broader range of natural settings, including during learning, sleep, or diseased states (Mackevicius and Fee, 2018). In these applications, it may not be possible to use external timing references, either because behaviors are not stereotyped or are entirely absent. Thus, sequences must be extracted directly from the neuronal data using unsupervised learning methods. Commonly used methods of this type, such as principal component analysis (PCA) or clustering methods, do not efficiently extract sequences, because they typically only model synchronous patterns of activity, rather than extended spatio-temporal motifs of firing.

Existing approaches that search for repeating neural patterns require computationally intensive or statistically challenging analyses (Brody, 1999; Mokeichev et al., 2007; Quaglio et al., 2018; Brunton et al., 2016). While progress has been made in analyzing non-synchronous sequential patterns using statistical models that capture cross-correlations between pairs of neurons (Russo and Durstewitz, 2017; Gerstein et al., 2012; Schrader et al., 2008; Torre et al., 2016; Grossberger et al., 2018; van der Meij and Voytek, 2018), such methods may not have statistical power to scale to patterns that include many (more than a few dozen) neurons, may require long periods (≥105 timebins) of stationary data, and may have challenges in dealing with (non-sequential) background activity. For a review highlighting features and limitations of these methods see (Quaglio et al., 2018).

Here, we explore a complementary approach, which uses matrix factorization to reconstruct neural dynamics using a small set of exemplar sequences. In particular, we build on convolutional non-negative matrix factorization (convNMF) (Smaragdis, 2004; Smaragdis, 2007) (Figure 1B), which has been previously applied to identify recurring motifs in audio signals such as speech (O’Grady and Pearlmutter, 2006; Smaragdis, 2007; Vaz et al., 2016), as well as neural signals (Peter et al., 2017). ConvNMF identifies exemplar patterns (factors) in conjunction with the times and amplitudes of pattern occurrences. This strategy eliminates the need to average activity aligned to any external behavioral references.

![Figure 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig1-v3.jpg)

**Figure 1.:** (A) NMF (non-negative matrix factorization) approximates a data matrix describing the activity of $N$ neurons at $T$ timepoints as a sum of $K$ rank-one matrices. Each matrix is generated as the outer product of two nonnegative vectors: $𝐰_{k}$ of length $N$, which stores a neural ensemble, and $𝐡_{k}$ of length $T$, which holds the times at which the neural ensemble is active, and the relative amplitudes of this activity. (B) Convolutional NMF also approximates an $N\timesT$ data matrix as a sum of $K$ matrices. Each matrix is generated as the convolution of two components: a non-negative matrix $𝐰_{k}$ of dimension $N\timesL$ that stores a sequential pattern of the $N$ neurons at $L$ lags, and a vector of temporal loadings, $𝐡_{k}$, which holds the times at which each factor pattern is active in the data, and the relative amplitudes of this activity. (C) Three types of inefficiencies present in unregularized convNMF: Type 1, in which two factors are used to reconstruct the same instance of a sequence; Type 2, in which two factors reconstruct a sequence in a piece-wise manner; and Type 3, in which two factors are used to reconstruct different instances of the same sequence. For each case, the factors ($𝐖$ and $𝐇$) are shown, as well as the reconstruction ($𝐗~=𝐖⊛𝐇=𝐰_{1}⊛𝐡_{1}+𝐰_{2}⊛𝐡_{2}+⋯$).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) Example factorizations of a synthetic dataset for convolutional NMF, and for convolutional NMF with three different penalties designed to eliminate correlations in $𝐇$ or in both $𝐇$ and $𝐖$. Notice that different penalties lead to different types of redundancies in the corresponding factorizations. (B) Quantification of correlations in $𝐇$ and $𝐖$ for each different penalty. H correlations are measured using $∥𝐇𝐒𝐇^{⊤}∥_{1,i\neqj}$ and W correlations are measured using $∥𝐖_{f⁢l⁢a⁢t}⁢𝐖_{f⁢l⁢a⁢t}^{⊤}∥_{1,i\neqj}$, where $𝐖_{f⁢l⁢a⁢t}=\sum_{ℓ}(𝐖_{⋅⁣⋅ℓ})$.

While convNMF may produce excellent reconstructions of the data, it does not automatically produce the minimal number of factors required. Indeed, if the number of factors in the convNMF model is greater than the true number of sequences, the algorithm returns overly complex and redundant factorizations. Moreover, in these cases, the sequences extracted by convNMF will often be inconsistent across optimization runs from different initial conditions, complicating scientific interpretations of the results (Peter et al., 2017; Wu et al., 2016).

To address these concerns, we developed a toolbox of methods, called seqNMF, which includes two different strategies to resolve the problem of redundant factorizations described above. In addition, the toolbox includes methods for promoting potentially desirable features such as orthogonality or sparsity of the spatial and temporal structure of extracted factors, and methods for analyzing the statistical significance and prevalence of the identified sequential structure. To assess these tools, we characterize their performance on synthetic data under a variety of noise conditions and also show that they are able to find sequences in neural data collected from two different animal species using different behavioral protocols and recording technologies. Applied to extracellular recordings from rat hippocampus, seqNMF identifies neural sequences that were previously found by trial-averaging. Applied to functional calcium imaging data recorded in vocal/motor cortex of untutored songbirds, seqNMF robustly identifies neural sequences active in a biologically atypical and overlapping fashion. This finding highlights the utility of our approach to extract sequences without reference to external landmarks; untutored bird songs are so variable that aligning neural activity to song syllables would be difficult and highly subjective.

## Results

### Matrix factorization framework for unsupervised discovery of features in neural data

Matrix factorization underlies many well-known unsupervised learning algorithms, including PCA (Pearson, 1901), non-negative matrix factorization (NMF) (Lee and Seung, 1999), dictionary learning, and k-means clustering (see Udell et al., 2016 for a review). We start with a data matrix, $𝐗$, containing the activity of $N$ neurons at $T$ timepoints. If the neurons exhibit a single repeated pattern of synchronous activity, the entire data matrix can be reconstructed using a column vector $𝐰$ representing the neural pattern, and a row vector $𝐡$ representing the times and amplitudes at which that pattern occurs (temporal loadings). In this case, the data matrix $𝐗$ is mathematically reconstructed as the outer product of $𝐰$ and $𝐡$. If multiple component patterns are present in the data, then each pattern can be reconstructed by a separate outer product, where the reconstructions are summed to approximate the entire data matrix (Figure 1A) as follows:

$$
𝐗_{n⁢t}≈𝐗~_{n⁢t}=\sumk=1K𝐖_{n⁢k}⁢𝐇_{k⁢t}=(𝐖𝐇)_{n⁢t}
$$

where $𝐗_{n⁢t}$ is the $(n⁢t)^{t⁢h}$ element of matrix $𝐗$, that is, the activity of neuron $n$ at time $t$. Here, in order to store $K$ different patterns, $𝐖$ is a $N\timesK$ matrix containing the $K$ exemplar patterns, and $𝐇$ is a $K\timesT$ matrix containing the $K$ timecourses:

$$
W=[|||w_{1}w_{2}⋯w_{K}|||] H=[−h_{1}−−h_{2}−⋮−h_{K}−]
$$

Given a data matrix with unknown patterns, the goal of matrix factorization is to discover a small set of patterns, $𝐖$, and a corresponding set of temporal loading vectors, $𝐇$, that approximate the data. In the case that the number of patterns, $K$, is sufficiently small (less than $N$ and $T$), this corresponds to a dimensionality reduction, whereby the data is expressed in more compact form. PCA additionally requires that the columns of $𝐖$ and the rows of $𝐇$ are orthogonal. NMF instead requires that the elements of $𝐖$ and $𝐇$ are nonnegative. The discovery of unknown factors is often accomplished by minimizing the following cost function, which measures the element-by-element sum of all squared errors between a reconstruction $𝐗~=𝐖𝐇$ and the original data matrix $𝐗$ using the Frobenius norm, $∥𝐌∥_{F}=\sqrt{\sum_{i⁢j}𝐌_{i⁢j}^{2}}$:

$$
(W^{∗},H^{∗})=arg minW,H‖X~−X‖_{F}^{2}
$$

(Note that other loss functions may be substituted if desired, for example to better reflect the noise statistics; see (Udell et al., 2016) for a review). The factors $𝐖^{*}$ and $𝐇^{*}$ that minimize this cost function produce an optimal reconstruction $𝐗~^{*}=𝐖^{*}⁢𝐇^{*}$. Iterative optimization methods such as gradient descent can be used to search for global minima of the cost function; however, it is often possible for these methods to get caught in local minima. Thus, as described below, it is important to run multiple rounds of optimization to assess the stability/consistency of each model.

While this general strategy works well for extracting synchronous activity, it is unsuitable for discovering temporally extended patterns—first, because each element in a sequence must be represented by a different factor, and second, because NMF assumes that the columns of the data matrix are independent ‘samples’ of the data, so permutations in time have no effect on the factorization of a given data. It is therefore necessary to adopt a different strategy for temporally extended features.

### Convolutional matrix factorization

Convolutional nonnegative matrix factorization (convNMF) (Smaragdis, 2004; Smaragdis, 2007) extends NMF to provide a framework for extracting temporal patterns, including sequences, from data. While in classical NMF each factor $𝐖$ is represented by a single vector (Figure 1A), the factors $𝐖$ in convNMF represent patterns of neural activity over a brief period of time. Each pattern is stored as an $N\timesL$ matrix, $𝐰_{𝐤}$, where each column (indexed by $ℓ=1$ to $L$) indicates the activity of neurons at different timelags within the pattern (Figure 1B). The times at which this pattern/sequence occurs are encoded in the row vector $𝐡_{𝟏}$, as for NMF. The reconstruction is produced by convolving the $N\timesL$ pattern with the time series $𝐡_{𝟏}$ (Figure 1B).

If the data contains multiple patterns, each pattern is captured by a different $N\timesL$ matrix and a different associated time series vector $𝐡$. A collection of $K$ different patterns can be compiled together into an $N\timesK\timesL$ array (also known as a tensor), $𝐖$ and a corresponding $K\timesT$ time series matrix $𝐇$. Analogous to NMF, convNMF generates a reconstruction of the data as a sum of $K$ convolutions between each neural activity pattern ($𝐖$), and its corresponding temporal loadings ($𝐇$):

$$
X_{nt}≈X~_{nt}=\sumk=1K\sumℓ=0L−1W_{nkℓ}H_{k(t−ℓ)}≡(W⊛H)_{nt}
$$

The tensor/matrix convolution operator $⊛$ (notation summary, Table 1) reduces to matrix multiplication in the $L=1$ case, which is equivalent to standard NMF. The quality of this reconstruction can be measured using the same cost function shown in Equation 3, and $𝐖$ and $𝐇$ may be found iteratively using similar multiplicative gradient descent updates to standard NMF (Lee and Seung, 1999; Smaragdis, 2004; Smaragdis, 2007).

**Table 1.**
 Notation for convolutional matrix factorization


<table>
  <tbody>
    <tr>
      <td>Shift operator</td>
    </tr>
    <tr>
      <td>The operator (H)ℓ→ shifts a matrix 𝐇 in the → direction by ℓ timebins: (H)ℓ→⋅t=H⋅(t−l) and likewise (H)←ℓ⋅t=H⋅(t+ℓ) where ⋅ indicates all elements along the respective matrix dimension.The shift operator inserts zeros when (t−ℓ)&lt;0 or (t+ℓ)&gt;T</td>
    </tr>
    <tr>
      <td>Tensor convolution operator</td>
    </tr>
    <tr>
      <td>Convolutive matrix factorization reconstructs a data matrix 𝐗 using a N×K×L tensor 𝐖 and a K×T matrix 𝐇: 𝐗~=𝐖⊛𝐇=∑ℓ𝐖⋅⁣⋅ℓ⁢𝐇ℓ→Note that each neuron n is reconstructed as the sum of k convolutions: 𝐗~n⁢t=∑k∑ℓ𝐖n⁢k⁢ℓ⁢𝐇k⁢(t-ℓ)≡(𝐖⊛𝐇)n⁢t</td>
    </tr>
    <tr>
      <td>Transpose tensor convolution operator</td>
    </tr>
    <tr>
      <td>The following quantity is useful in several contexts: 𝐖⁢⊛⊤⁢𝐗=∑ℓ(𝐖⋅⁣⋅ℓ)⊤⁢𝐗←ℓNote that each element (𝐖⁢⊛⊤⁢𝐗)k⁢t=∑l(𝐖⋅k⁢ℓ)⊤⁢𝐗⋅(t+ℓ)=∑l∑n𝐖n⁢k⁢ℓ⁢𝐗n⁢(t+ℓ) measures the overlap (correlation) of factor k with the data at time t</td>
    </tr>
    <tr>
      <td>convNMF reconstruction</td>
    </tr>
    <tr>
      <td>𝐗≈𝐗~=∑k𝐖⋅k⁣⋅⊛𝐇k⁣⋅=𝐖⊛𝐇Note that NMF is a special case of convNMF, where L=1</td>
    </tr>
    <tr>
      <td>L⁢1 entrywise norm excluding diagonal elements</td>
    </tr>
    <tr>
      <td>For any K×K matrix 𝐂, ∥𝐂∥1,i≠j≡∑k∑j≠k𝐂j⁢k</td>
    </tr>
    <tr>
      <td>Special matrices</td>
    </tr>
    <tr>
      <td>𝟏 is a K×K matrix of ones𝐈 is the K×K identity matrix𝐒 is a T×T smoothing matrix: 𝐒i⁢j=1 when |i−j|&lt;L and otherwise 𝐒i⁢j=0</td>
    </tr>
  </tbody>
</table>

While convNMF can perform extremely well at reconstructing sequential structure, it can be challenging to use when the number of sequences in the data is not known (Peter et al., 2017). In this case, a reasonable strategy would be to choose $K$ at least as large as the number of sequences that one might expect in the data. However, if $K$ is greater than the actual number of sequences, convNMF often identifies more significant factors than are minimally required. This is because each sequence in the data may be approximated equally well by a single sequential pattern or by a linear combination of multiple partial patterns. A related problem is that running convNMF from different random initial conditions produces inconsistent results, finding different combinations of partial patterns on each run (Peter et al., 2017). These inconsistency errors fall into three main categories (Figure 1C):

Together, these inconsistency errors manifest as strong correlations between different redundant factors, as seen in the similarity of their temporal loadings ($𝐇$) and/or their exemplar activity patterns ($𝐖$).

We next describe two strategies for overcoming the redundancy errors described above. Both strategies build on previous work that reduces correlations between factors in NMF. The first strategy is based on regularization, a common technique in optimization that allows the incorporation of constraints or additional information with the goal of improving generalization performance or simplifying solutions to resolve degeneracies (Hastie et al., 2009). A second strategy directly estimates the number of underlying sequences by minimizing a measure of correlations between factors (stability NMF; Wu et al., 2016).

### Optimization penalties to reduce redundant factors

To reduce the occurrence of redundant factors (and inconsistent factorizations) in convNMF, we sought a principled way of penalizing the correlations between factors by introducing a penalty term, $ℛ$, into the convNMF cost function:

$$
(W^{∗},H^{∗})=arg minW,H(‖X~−X‖_{F}^{2}+ℛ)
$$

Regularization has previously been used in NMF to address the problem of duplicated factors, which, similar to Type 1 errors above, present as correlations between the $𝐇$’s (Choi, 2008; Chen and Cichocki, 2004). Such correlations are measured by computing the correlation matrix $𝐇𝐇^{⊤}$, which contains the correlations between the temporal loadings of every pair of factors. The regularization may be implemented using the penalty term $ℛ=\lambda⁢∥𝐇𝐇^{⊤}∥_{1,i\neqj}$, where the seminorm $∥⋅∥_{1,i\neqj}$ sums the absolute value of every matrix entry except those along the diagonal (notation summary, Table 1) so that correlations between different factors are penalized, while the correlation of each factor with itself is not. Thus, during the minimization process, similar factors compete, and a larger amplitude factor drives down the temporal loading of a correlated smaller factor. The parameter $\lambda$ controls the magnitude of the penalty term $ℛ$.

In convNMF, a penalty term based on $𝐇𝐇^{⊤}$ yields an effective method to prevent errors of Type 1, because it penalizes the associated zero lag correlations. However, it does not prevent errors of the other types, which exhibit different types of correlations. For example, Type 2 errors result in correlated temporal loadings that have a small temporal offset and thus are not detected by $𝐇𝐇^{⊤}$. One simple way to address this problem is to smooth the $𝐇$’s in the penalty term with a square window of length $2⁢L-1$ using the smoothing matrix $𝐒$ ($𝐒_{i⁢j}=1$ when $|i-j|<L$ and otherwise $𝐒_{i⁢j}=0$). The resulting penalty, $ℛ=\lambda⁢∥𝐇𝐒𝐇^{⊤}∥$, allows factors with small temporal offsets to compete, effectively preventing errors of Types 1 and 2.

This penalty does not prevent errors of Type 3, in which redundant factors with highly similar patterns in $𝐖$ are used to explain different instances of the same sequence. Such factors have temporal loadings that are segregated in time, and thus have low correlations, to which the cost term $∥𝐇𝐒𝐇^{⊤}∥$ is insensitive. One way to resolve errors of Type 3 might be to include an additional cost term that penalizes the similarity of the factor patterns in $𝐖$. This has the disadvantage of requiring an extra parameter, namely the $\lambda$ associated with this cost.

Instead we chose an alternative approach to resolve errors of Type 3 that simultaneously detects correlations in $𝐖$ and $𝐇$ using a single cross-orthogonality cost term. We note that, for Type 3 errors, redundant $𝐖$ patterns have a high degree of overlap with the data at the same times, even though their temporal loadings are segregated at different times. To introduce competition between these factors, we first compute, for each pattern in $𝐖$, its overlap with the data at time $t$. This quantity is captured in symbolic form by $𝐖⁢⊛⊤⁢𝐗$ (see Table 1). We then compute the pairwise correlation between the temporal loading of each factor and the overlap of every other factor with the data. This cross-orthogonality penalty term, which we refer to as 'x-ortho’, sums up these correlations across all pairs of factors, implemented as follows:

$$
ℛ=\lambda⁢∥(𝐖⁢⊛⊤⁢𝐗)⁢𝐒𝐇^{⊤}∥_{1,i\neqj}
$$

When incorporated into the update rules, this causes any factor that has a high overlap with the data to suppress the temporal loadings ($𝐇$) of any other factors that have high overlap with the data at that time (Further analysis, Appendix 2). Thus, factors compete to explain each feature of the data, favoring solutions that use a minimal set of factors to give a good reconstruction. The resulting global cost function is:

$$
(W^{∗},H^{∗})=arg minW,H(‖X~−X‖_{F}^{2}+\lambda‖(W⊛⊤X)SH^{⊤}‖_{1,i\neqj})
$$

The update rules for $𝐖$ and $𝐇$ are based on the derivatives of this global cost function, leading to a simple modification of the standard multiplicative update rules used for NMF and convNMF (Lee and Seung, 1999; Smaragdis, 2004; Smaragdis, 2007) (Table 2). Note that the addition of this cross-orthogonality term does not formally constitute regularization, because it also includes a contribution from the data matrix $𝐗$, rather than just the model variables $𝐖$ and $𝐇$. However, at least for the case that the data is well reconstructed by the sum of all factors, the x-ortho penalty can be shown to be approximated by a formal regularization (Appendix 2). This formal regularization contains both a term corresponding to a weighted smoothed orthogonality penalty on $𝐖$ and a term corresponding to a weighted smoothed) orthogonality penalty on $𝐇$, consistent with the observation that the x-ortho penalty simultaneously punishes factor correlations in $𝐖$ and $𝐇$.

**Table 2.**
 Regularized NMF and convNMF: cost functions and algorithms


<table>
  <tbody>
    <tr>
      <td>NMF</td>
      <td></td>
    </tr>
    <tr>
      <td>ℒ=12⁢||𝐗~-𝐗||22+ℛ 𝐗~=𝐖𝐇</td>
      <td>W←W×XH⊤X~H⊤+∂ℛ∂W H←H×W⊤XW⊤X~+∂ℛ∂H</td>
    </tr>
    <tr>
      <td>convNMF</td>
      <td></td>
    </tr>
    <tr>
      <td>ℒ=12⁢||𝐗~-𝐗||22+ℛ 𝐗~=𝐖⊛𝐇</td>
      <td>W⋅⋅ℓ←W⋅⋅ℓ×X Hℓ→⊤X~ Hℓ→⊤+∂ℛ∂W⋅⋅ℓ H←H×W⊛⊤XW⊛⊤X~+∂ℛ∂H</td>
    </tr>
    <tr>
      <td>L⁢1 regularization for 𝐇 ( L⁢1 for 𝐖 is analogous)</td>
      <td></td>
    </tr>
    <tr>
      <td>ℛ=λ⁢||𝐇||1</td>
      <td>∂⁡ℛ∂⁡𝐖⋅⁣⋅ℓ=0 ∂⁡ℛ∂⁡𝐇=λ⁢𝟏</td>
    </tr>
    <tr>
      <td>Orthogonality cost for 𝐇</td>
      <td></td>
    </tr>
    <tr>
      <td>ℛ=λ2⁢||𝐇𝐇⊤||1,i≠j</td>
      <td>∂⁡ℛ∂⁡𝐖⋅⁣⋅ℓ=0 ∂⁡ℛ∂⁡𝐇=λ⁢(𝟏-𝐈)⁢𝐇</td>
    </tr>
    <tr>
      <td>Smoothed orthogonality cost for 𝐇 (favors ‘events-based’)</td>
      <td></td>
    </tr>
    <tr>
      <td>ℛ=λ2⁢||𝐇𝐒𝐇⊤||1,i≠j</td>
      <td>∂⁡ℛ∂⁡𝐖⋅⁣⋅ℓ=0 ∂⁡ℛ∂⁡𝐇=λ⁢(𝟏-𝐈)⁢𝐇𝐒</td>
    </tr>
    <tr>
      <td>Smoothed orthogonality cost for 𝐖 (favors ‘parts-based’)</td>
      <td></td>
    </tr>
    <tr>
      <td>ℛ=λ2⁢||𝐖f⁢l⁢a⁢t⊤⁢𝐖f⁢l⁢a⁢t||1,i≠j  where (𝐖f⁢l⁢a⁢t)n⁢k=∑ℓ𝐖n⁢k⁢ℓ</td>
      <td>∂⁡ℛ∂⁡𝐖⋅⁣⋅ℓ=λ⁢𝐖f⁢l⁢a⁢t⁢(𝟏-𝐈) ∂⁡ℛ∂⁡𝐇=0</td>
    </tr>
    <tr>
      <td>Smoothed cross-factor orthogonality (x-ortho penalty)</td>
      <td></td>
    </tr>
    <tr>
      <td>ℛ=λ⁢||(𝐖⁢⊛⊤⁢𝐗)⁢𝐒𝐇⊤||1,i≠j</td>
      <td>∂⁡ℛ∂⁡𝐖⋅⁣⋅ℓ=λ⁢𝐗←ℓ⁢𝐒𝐇⊤⁢(𝟏-𝐈) ∂⁡ℛ∂⁡𝐇=λ⁢(𝟏-𝐈)⁢𝐖⁢⊛⊤⁢𝐗𝐒</td>
    </tr>
  </tbody>
</table>

There is an interesting relation between our method for penalizing correlations and other methods for constraining optimization, namely sparsity. Because of the non-negativity constraint imposed in NMF, correlations can also be reduced by increasing the sparsity of the representation. Previous efforts have been made to minimize redundant factors using sparsity constraints; however, this approach may require penalties on both $𝐖$ and $𝐇$, necessitating the selection of two hyper-parameters ($\lambda_{w}$ and $\lambda_{h}$) (Peter et al., 2017). Since the use of multiple penalty terms increases the complexity of model fitting and selection of parameters, one goal of our work was to design a simple, single penalty function that could regularize both $𝐖$ and $𝐇$ simultaneously. The x-ortho penalty described above serves this purpose (Equation 6). As we will describe below, the application of sparsity penalties can be very useful for shaping the factors produced by convNMF, and our code includes options for applying sparsity penalties on both $𝐖$ and $𝐇$.

#### Extracting ground-truth sequences with the x-ortho penalty when the number of sequences is not known

We next examined the effect of the x-ortho penalty on factorizations of sequences in simulated data, with a focus on convergence, consistency of factorizations, the ability of the algorithm to discover the correct number of sequences in the data, and robustness to noise (Figure 2A). We first assessed the model’s ability to extract three ground-truth sequences lasting 30 timesteps and containing 10 neurons in the absence of noise (Figure 2A). The resulting data matrix had a total duration of 15,000 timesteps and contained on average 60±6 instances of each sequence. Neural activation events were represented with an exponential kernel to simulate calcium imaging data. The algorithm was run with the x-ortho penalty for 1000 iterations andit reliably converged to a root-mean-squared-error (RMSE) close to zero (Figure 2B). RMSE reached a level within 10% of the asymptotic value in approximately 100 iterations.

![Figure 2.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig2-v3.jpg)

**Figure 2.:** (A) A simulated dataset with three sequences. Also shown is a factorization with x-ortho penalty ($K=20$, $L=50$, $\lambda=0.003$). Each significant factor is shown in a different color. At left are the exemplar patterns ($𝐖$) and on top are the timecourses ($𝐇$). (B) Reconstruction error as a function of iteration number. Factorizations were run on a simulated dataset with three sequences and 15,000 timebins ($≈$ 60 instances of each sequence). Twenty independent runs are shown. Here, the algorithm converges to within 10% of the asymptotic error value within $≈$ 100 iterations. (C) The x-ortho penalty produces more consistent factorizations than unregularized convNMF across 400 independent fits ($K=20$, $L=50$, $\lambda=0.003$). (D) The number of statistically significant factors (Figure 2—figure supplement 1) vs. the number of ground-truth sequences for factorizations with and without the x-ortho penalty. Shown for each condition is a vertical histogram representing the number of significant factors over 20 runs ($K=20$, $L=50$, $\lambda=0.003$). (E) Factorization with x-ortho penalty of two simulated neural sequences with shared neurons that participate at the same latency. (F) Same as E but for two simulated neural sequences with shared neurons that participate at different latencies.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (A) Distribution of overlap values between an extracted factor and the held-out data. (B) A null factor was constructed by randomly circularly shifting each row of a factor independently. Many null factors were constructed and the distribution of overlap values ($𝐖⁢⊛⊤⁢𝐗$) was measured between each null factor and the held-out data. (C) A comparison of the skewness values for each null factor and the skewness of the overlaps of the original extracted factor. A factor is deemed significant if its skewness is significantly greater than the distribution of skewness values for the null factor overlaps.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** Number of significant factors as a function of $\lambda$ for datasets containing between 1 and 10 sequences.The number of significant factors obtained by fitting data containing between 1 and 10 ground truth sequences using the x-ortho penalty ($K=20$, $L=50$) for a large range of values of $\lambda$. For each value of $\lambda$, 20 fits are shown and the mean is shown as a solid line. Each color corresponds to a ground-truth dataset containing a different number of sequences and no added noise. Values of $\lambda$ ranging between $0.001$ and $0.1$ tended to return the correct number of significant sequences at least 90% of the time.

While similar RMSE values were achieved using convNMF with and without the x-ortho penalty; the addition of this penalty allowed three ground-truth sequences to be robustly extracted into three separate factors ($𝐰_{1}$, $𝐰_{2}$, and $𝐰_{3}$ in Figure 2A) so long as $K$ was chosen to be larger than the true number of sequences. In contrast, convNMF with no penalty converged to inconsistent factorizations from different random initializations when $K$ was chosen to be too large, due to the ambiguities described in Figure 1. We quantified the consistency of each model (see Materials and methods), and found that factorizations using the x-ortho penalty demonstrated near perfect consistency across different optimization runs (Figure 2C).

We next evaluated the performance of convNMF with and without the x-ortho penalty on datasets with a larger number of sequences. In particular, we set out to observe the effect of the x-ortho penalty on the number of statistically significant factors extracted. Statistical significance was determined based on the overlap of each extracted factor with held out data (see Materials and methods and code package). With the penalty term, the number of significant sequences closely matched the number of ground-truth sequences. Without the penalty, all 20 extracted sequences were significant by our test (Figure 2D).

We next considered how the x-ortho penalty performs on sequences with more complex structure than the sparse uniform sequences of activity ediscussed above. We further examined the case in which a population of neurons is active in multiple different sequences. Such neurons that are shared across different sequences have been observed in several neuronal datasets (Okubo et al., 2015; Pastalkova et al., 2008; Harvey et al., 2012). For one test, we constructed two sequences in which shared neurons were active at a common pattern of latencies in both sequences; in another test, shared neurons were active in a different pattern of latencies in each sequence. In both tests, factorizations using the x-ortho penalty achieved near-perfect reconstruction error, and consistency was similar to the case with no shared neurons (Figure 2E,F). We also examined other types of complex structure and have found that the x-ortho penalty performs well in data with large gaps between activity or with large overlaps of activity between neurons in the sequence. This approach also worked well in cases in which the duration of the activity or the interval between the activity of neurons varied across the sequence (Figure 3—figure supplement 3).

![Figure 3.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig3-v3.jpg)

**Figure 3.:** Performance of the x-ortho penalty was tested under four different noise conditions: (A) probabilistic participation, (B) additive noise, (C) temporal jitter, and (D) sequence warping. For each noise type, we show: (top) examples of synthetic data at three different noise levels; (middle) similarity of extracted factors to ground-truth patterns across a range of noise levels (20 fits for each level); and (bottom) examples of extracted factors $𝐖$’s for one of the ground-truth patterns. Examples are shown at the same three noise levels illustrated in the top row. In these examples, the algorithm was run with $K=20$, $L=50$ and $\lambda$ = $2⁢\lambda_{0}$ (via the procedure described in Figure 4). For C, jitter displacements were draw from a discrete guassian distribution with the standard deviation in timesteps shown above For D, timewarp conditions 1–10 indicate: 0, 66, 133, 200, 266, 333, 400, 466, 533 and 600 max % stretching respectively. For results at different values of $\lambda$, see Figure 3—figure supplement 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Robustness to noise at different values of $\lambda$.Performance of the x-ortho penalty was tested under four different noise conditions, at different values of $\lambda$ than in Figure 3 (where $\lambda=2⁢\lambda_{0}$): (A) probabilistic participation, $\lambda=5⁢\lambda_{0}$, (B) additive noise, $\lambda=\lambda_{0}$ (C) timing jitter, $\lambda=5⁢\lambda_{0}$ and (D) sequence warping, $\lambda=5⁢\lambda_{0}$. For each noise type, we show: (top) examples of synthetic data at three different noise levels; (middle) similarity of x-ortho factors to ground-truth factors across a range of noise levels (20 fits for each level); and (bottom) example of one of the $𝐖$’s extracted at three different noise levels (same conditions as data shown above). The algorithm was run with $K=20$, $L=50$.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** (A) A short (400 timestep) dataset containing one example each of three ground-truth sequences, as well as additive noise. (B) As a function of dataset size, similarity of extracted factors to noiseless, ground-truth factors. At each dataset size, 20 independent fits of penalized convNMF are shown. Median shown in red. Three examples of each sequence were sufficient to acheive similiarty scores within 10% of asymptotic performance. (C) Example factors fit on data containing 2, 3, 4 or 20 examples of each sequence. Extracted factors were significant on held-out data compared to null (shuffled) factors even when training and test datasets each contained only 2 examples of each sequence.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** Characterization of the x-ortho penalty for additional types of noise. (A) An example of a factorization for a sequence with large gaps between members of the sequence. (B–D) Example factorizations of sequences with neuronal activations that are highly overlapped in time. (B) An example of an x-ortho penalized factorization that reconstructs the data using complex patterns in $𝐖$ and $𝐇$. (C) An example of an x-ortho penalized factorization with the addition of an L1 penalty on $𝐇$ models the data as an overlapping pattern with sparse activations. (D) An example of an x-ortho penalized factorization with the addition of an L1 penalty on $𝐖$ models the data as a non-overlapping pattern with dense activations. (E) An example of an x-ortho penalized factorization for data in which neurons have varying durations of activation which form two patterns. (F) An example of an x-ortho penalized factorization for data in which neurons have varying durations of activation which are random. (G–I) Examples factorizations of sequences with statistics that vary systematically. (G) An example of an x-ortho penalized factorization for data in which neurons have systematically varying changes in duration of activity. (H) An example of an x-ortho penalized factorization for data in which neurons have systematically varying changes in the gaps between members of the sequence. (I) An example of an x-ortho penalized factorization for data in which neurons have systematically varying changes in the amount of jitter.

![Figure 4.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig4-v3.jpg)

**Figure 4.:** Procedure for choosing $\lambda$ for a new dataset based on finding a balance between reconstruction cost and x-ortho cost.(A) Simulated data containing three sequences in the presence of participation noise (50% participation probability). This noise condition is used for the tests in (B–F). (B) Normalized reconstruction cost ($||𝐗~-𝐗||_{F}^{2}$) and cross-orthogonality cost ($||(𝐖⁢⊛⊤⁢𝐗)⁢𝐒𝐇^{⊤}||_{1,i\neqj}$) as a function of $\lambda$ for 20 fits of these data. The cross-over point $\lambda_{0}$ is marked with a black circle. Note that in this plot the reconstruction cost and cross-orthogonality cost are normalized to vary between 0 and 1. (C) The number of significant factors obtained as a function of $\lambda$; 20 fits, mean plotted in orange. Red arrow at left indicates the correct number of sequences (three). (D) Fraction of fits returning the correct number of significant factors as a function of $\lambda$. (E) Similarity of extracted factors to ground-truth sequences as a function of $\lambda$. (F) Composite performance, as the product of the curves in (D) and (E) (smoothed using a three sample boxcar, plotted in orange with a circle marking the peak). Shaded region indicates the range of $\lambda$ that works well ($\pm$ half height of composite performance). (G–L) same as (A–F) but for simulated data containing three noiseless sequences. (M) Summary plot showing the range of values of $\lambda$ (vertical bars), relative to the cross-over point $\lambda_{0}$, that work well for each noise condition ($\pm$ half height points of composite performance). Circles indicate the value of $\lambda$ at the peak of the smoothed composite performance. For each noise type, results for all noise levels from Figure 3 are shown (increasing color saturation at high noise levels; Green, participation: 90, 80, 70, 60, 50, 40, 30, and 20%; Orange, additive noise 0.5, 1, 2, 2.5, 3, 3.5, and 4%; Purple, jitter: SD of the distribution of random jitter: 5, 10, 15, 20, 25, 30, 35, 40, and 45 timesteps; Grey, timewarp: 66, 133, 200, 266, 333, 400, 466, 533, 600, and 666 max % stretching. Asterisk (*) indicates the noise type and level used in panels (A–F). Gray band indicates a range between $2⁢\lambda_{0}$ and $5⁢\lambda_{0}$, a range that tended to perform well across the different noise conditions. In real data, it may be useful to explore a wider range of $\lambda$.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Analysis of the best range of $\lambda$.Here, we quantify the full width at the half maximum for the composite performance scores in different noise conditions. For each condition, a box and whisker plot quantifies the number of orders of magnitude over which a good factorization is returned (median denoted by a white circle). Next to each box plot individual points are shown, corresponding to different noise level. Color saturation reflects noise level as in Figure 4.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Procedure for choosing $\lambda$ applied to data with shared neurons.(A) Simulated data containing two patterns which share 50% of their neurons, in the presence of participation noise (70% participation probability). (B) Normalized reconstruction cost ($||𝐗~-𝐗||_{F}^{2}$) and cross-orthogonality cost ($||(𝐖⁢⊛⊤⁢𝐗)⁢𝐒𝐇^{⊤}||_{1,i\neqj}$) as a function of $\lambda$ for these data. The cross-over point $\lambda_{0}$ is marked with a black circle. (C) The number of significant factors obtained from 20 fits of these data as a function of $\lambda$ (mean number plotted in orange). The correct number of factors (two) is marked by a red triangle. (D) The fraction of fits returning the correct number of significant factors as a function of $\lambda$. (E) Similarity of the top two factors to ground-truth (noiseless) factors as a function of $\lambda$. (F) Composite performance measured as the product of the curves shown in (D) and (E), (smoothed curve plotted in orange with a circle marking the peak). Shaded region indicates the range of $\lambda$ that works well ($\pm$ half height of composite performance). For this dataset, the best performance occurs at $\lambda=5⁢\lambda_{0}$, while a range of $\lambda$ between 2 $\lambda_{0}$ and 10 $\lambda_{0}$ performs well.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig4-figsupp3-v3.jpg)

**Figure 4—figure supplement 3.:** Using cross-validation on held-out (masked) data to choose $\lambda$.A method for choosing a reasonable value of $\lambda$ based on cross validation is shown for five different noise types (each column shows a different noise type; from left to right: (I) participation noise, (II) additive noise, (III) jitter, (IV) temporal warping), and (V) a lower level of participation noise. The cross-validated test error is calculated by fitting x-ortho penalized factorizations while randomly holding out 10% of the elements in the data matrix as a test set (Wold, 1978; Bro et al., 2008). In many of our test datasets, there was a minimum or a divergence point in the difference between the test and training error, that agreed with the procedure described in Figure 4, based on $\lambda_{0}$. (A) Examples of each dataset. (B) Test error (blue) and training error (red) as a function of $\lambda$ for each of the different noise conditions. (C) The difference between the test error and training error values shown above. (D) Normalized reconstruction cost ($||𝐗~-𝐗||_{F}^{2}$) and cross-orthogonality cost ($||(𝐖⁢⊛⊤⁢𝐗)⁢𝐒𝐇^{⊤}||_{1,i\neqj}$) as a function of $\lambda$ for each of the different noise conditions. (E) Composite performance as a function of $\lambda$. Panels D and E are identical to those in Figure 4, and are included here for comparison. (V) These data have a lower amount of participation noise than (I). Note that in low-noise conditions, test error may not exhibit a minima within the range of $\lambda$ that produces the ground truth number of factors.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig4-figsupp4-v3.jpg)

**Figure 4—figure supplement 4.:** Quantifying the effect of L1 sparsity penalties on $𝐖$ and $𝐇$.(A) An example window of simulated data with three sequences and 40% dropout. (B) The fraction of fits to data with the noise level in (A) that yielded three significant factors, as a function of two L1 sparsity regularization parameters on $𝐖$ and $𝐇$. Each bin represents 20 fits of sparsity penalized convNMF with K = 20 and L = 50. (C) The mean similarity to ground-truth for the same 20 factorizations as in (B). (D–F) same as panels A-C but with additional noise events in 2.5% of the bins. (H–J) same as panels A-C but with a jitter standard deviation of 20 bins. (K–M) same as panels A-C but for warping noise with a maximum of 260% warping.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig4-figsupp5-v3.jpg)

**Figure 4—figure supplement 5.:** (A) The fraction of 20 x-ortho penalized fits which had the same number of significant factors as the ground-truth for all noise conditions shown in Figure 3 at the $\lambda$ with the best performance. (B) The similarity to ground-truth for 20 x-ortho penalized fits to all noise conditions shown in Figure 3 at the $\lambda$ with the best performance. (C) The number of significant factors for 100 fits with an x-ortho penalty (black) and with sparsity penalties on $𝐖$ and $𝐇$ (Red) of four different noise conditions at the level indicated in (A) and (B). Penalty parameters used in (C–E) were selected by performing a parameter sweep and selecting the parameters which gave the maximum composite score as described above. (D) The fraction of 20 x-ortho or sparsity penalized fits with the ground truth number of significant sequences. Noise conditions are the same as in (C). Values for $\lambda$ were selected as those that give the highest composite performance (see Figure 4F). (E) Similarity to ground-truth for the fits shown in (C–D). Median is shown with black dot and bottom and top edges of boxes indicate the 25th and 75th percentiles.

#### Robustness to noisy data

The cross-orthogonality penalty performed well in the presence of types of noise commonly found in neural data. In particular, we considered: participation noise, in which individual neurons participate probabilistically in instances of a sequence; additive noise, in which neuronal events occur randomly outside of normal sequence patterns; temporal jitter, in which the timing of individual neurons is shifted relative to their typical time in a sequence; and finally, temporal warping, in which each instance of the sequence occurs at a different randomly selected speed. To test the robustness of the algorithm with the x-ortho penalty to each of these noise conditions, we factorized data containing three neural sequences at a variety of noise levels (Figure 3, top row). The value of $\lambda$ was chosen using methods described in the next section. Factorizations with the x-ortho penalty proved relatively robust to all four noise types, with a high probability of returning the correct numbers of significant factors (Figure 4—figure supplement 5). Furthermore, under low-noise conditions, the algorithm produced factors that were highly similar to ground-truth, and this similarity declined gracefully at higher noise levels (Figure 3). Visualization of the extracted factors revealed a good qualitative match to ground-truth sequences even in the presence of high noise except for the case of temporal jitter (Figure 3). We also found that the x-ortho penalty allows reliable extraction of sequences in which the duration of each neuron’s activity exhibits substantial random variation across different renditions of the sequence, and in which the temporal jitter of neural activity exhibits systematic variation at different points in the sequences (Figure 3—figure supplement 3).

Finally, we wondered how our approach with the x-ortho penalty performs on datasets with only a small number of instances of each sequence. We generated data containing different numbers of repetitions ranging from 1 to 20, of each underlying ground-truth sequence. For intermediate levels of additive noise, we found that three repetitions of each sequence were sufficient to correctly extract factors with similarity scores close to those obtained with much larger numbers of repetitions (Figure 3—figure supplement 2).

#### Methods for choosing an appropriate value of λ

The x-ortho penalty performs best when the strength of the regularization term (determined by the hyperparameter $\lambda$) is chosen appropriately. For $\lambda$ too small, the behavior of the algorithm approaches that of convNMF, producing a large number of redundant factors with high x-ortho cost. For $\lambda$ too large, all but one of the factors are suppressed to zero amplitude, resulting in a factorization with near-zero x-ortho cost, but with large reconstruction error if multiple sequences are present in the data. Between these extremes, there exists a region in which increasing $\lambda$ produces a rapidly increasing reconstruction error and a rapidly decreasing x-ortho cost. Thus, there is a single point, which we term $\lambda_{0}$, at which changes in reconstruction cost and changes in x-ortho cost are balanced (Figure 4A). We hypothesized that the optimal choice of $\lambda$ (i.e. the one producing the correct number of ground-truth factors) would lie near this point.

To test this intuition, we examined the performance of the x-ortho penalty as a function of$\lambda$ in noisy synthetic data consisting of three non-overlapping sequences (Figure 4A). Our analysis revealed that, overall, values of $\lambda$ between 2$\lambda_{0}$ and 5$\lambda_{0}$ performed well for these data across all noise types and levels (Figure 4B,C). In general, near-optimal performance was observed over an order of magnitude range of $\lambda$ (Figure 1). However, there were systematic variations depending on noise type: for additive noise, performance was better when $\lambda$ was closer to $\lambda_{0}$, while with other noise types, performance was better at somewhat higher values of $\lambda$s ($≈10⁢\lambda_{0}$).

Similar ranges of $\lambda$ appeared to work for datasets with different numbers of ground-truth sequences—for the datasets used in Figure 2D, a range of $\lambda$ between 0.001 and 0.01 returned the correct number of sequences at least 90% of the time for datasets containing between 1 and 10 sequences (Figure 2—figure supplement 2). Furthermore, this method for choosing $\lambda$ also worked on datasets containing sequences with shared neurons (Figure 4—figure supplement 2).

The value of $\lambda$ may also be determined by cross-validation (see Materials and methods). Indeed, the $\lambda$ chosen with the heuristic described above coincided with a minimum or distinctive feature in the cross-validated test error for all the cases we examined (Figure 4—figure supplement 3). The seqNMF code package accompanying this paper provides functions to determine $\lambda$ both by cross-validation or in reference to $\lambda_{0}$.

#### Sparsity constraints to reduce redundant factors

One of the advantages of the x-ortho penalty is that it includes only a single term to penalize correlations between different factors, and thus requires only a single hyperparameter $\lambda$. This contrasts with the approach of incorporating a sparsity constraint on $𝐖$ and $𝐇$ of the form $\lambda_{w}⁢∥𝐖∥_{1}+\lambda_{h}⁢∥𝐇∥_{1}$ (Peter et al., 2017). We have found that the performance of the sparsity approach depends on the correct choice of both hyperparameters $\lambda_{w}$ and $\lambda_{h}$ (Figure 4—figure supplement 4). Given the optimal choice of these parameters, the L1 sparsity constraint yields an overall performance approximately as good as the x-ortho penalty (Figure 4—figure supplement 4). However, there are some consistent differences in the performance of the sparsity and x-ortho approaches depending on noise type; an analysis at moderately high noise levels reveals that the x-ortho penalty performs slightly better with warping and participation noise, while the L1 sparsity penalty performs slightly better on data with jitter and additive noise (Figure 4—figure supplement 5). However, given the added complexity of choosing two hyperparameters for L1 sparsity, we prefer the x-ortho approach.

### Direct selection of K to reduce redundant factors

An alternative strategy to minimizing redundant factorizations is to estimate the number of underlying sequences and to select the appropriate value of $K$. An approach for choosing the number of factors in regular NMF is to run the algorithm many times with different initial conditions, at different values of $K$, and choose the case with the most consistent and uncorrelated factors. This strategy is called stability NMF (Wu et al., 2016) and is similar to other stability-based metrics that have been used in clustering models (von Luxburg, 2010). The stability NMF score, diss, is measured between two factorizations, $𝐅^{1}={𝐖^{1},𝐇^{1}}$ and $𝐅^{2}={𝐖^{2},𝐇^{2}}$, run from different initial conditions:

$$
diss(F^{1},F^{2})=\frac{1}{2K}(2K−\sumj=1Kmax1\leqk\leqKC_{jk}−\sumk=1Kmax1\leqj\leqKC_{jk})
$$

where $𝐂$ is the cross-correlation matrix between the columns of the matrix $𝐖^{1}$ and the the columns of the matrix $𝐖^{2}$. Note that diss is low when there is a one-to-one mapping between factors in $𝐅^{1}$ and $𝐅^{2}$, which tends to occur at the correct K in NMF (Wu et al., 2016; Ubaru et al., 2017). NMF is run many times and the diss metric is calculated for all unique pairs. The best value of K is chosen as that which yields the lowest average diss metric.

To use this approach for convNMF, we needed to slightly modify the stability NMF diss metric. Unlike in NMF, convNMF factors have a temporal degeneracy; that is, one can shift the elements of $𝐡_{k}$ by one time step while shifting the elements of $𝐰_{k}$ by one step in the opposite direction with little change to the model reconstruction. Thus, rather than computing correlations from the factor patterns $𝐖$ or loadings $𝐇$, we computed the diss metric using correlations between factor reconstructions ($𝐗~_{k}=𝐰_{𝐤}⊛𝐡_{𝐤}$).

$$
𝐂_{i⁢j}=\frac{Tr⁢[𝐗~_{i}^{T}⁢𝐗~_{j}]}{∥𝐗~_{i}∥_{F}⁢∥𝐗~_{j}∥_{F}}
$$

where $Tr⁢[⋅]$ denotes the trace operator, $Tr⁢[𝐌]=\sum_{i}𝐌_{i⁢i}$. That is, $𝐂_{i⁢j}$ measures the correlation between the reconstruction of factor i in $𝐅^{1}$ and the reconstruction of factor j in $𝐅^{2}$. Here, as for stability NMF, the approach is to run convNMF many times with different numbers of factors ($K$) and choose the $K$ which minimizes the diss metric.

We evaluated the robustness of this approach in synthetic data with the four noise conditions examined earlier. Synthetic data were constructed with three ground-truth sequences and 20 convNMF factorizations were carried out for each K ranging from 1 to 10. For each K the average diss metric was computed over all 20 factorizations. In many cases, the average diss metric exhibited a minimum at the ground-truth $K$ (Figure 5—figure supplement 1). As shown below, this method also appears to be useful for identifying the number of sequences in real neural data.

Not only does the diss metric identify factorizations that are highly similar to the ground truth and have the correct number of underlying factors, it also yields factorizations that minimize reconstruction error in held out data (Figure 5, Figure 5—figure supplement 2), as shown using the same cross-validation procedure described above (Figure 5—figure supplement 2). For simulated datasets with participation noise, additive noise, and temporal jitter, there is a clear minimum in the test error at the K given by diss metric. In other cases, there is a distinguishing feature such as a kink or a plateau in the test error at this K (Figure 5—figure supplement 2).

![Figure 5.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig5-v3.jpg)

**Figure 5.:** Panels show the distribution of diss as a function of K for several different noise conditions. Lower values of diss indicate greater consistency or stability of the factorizations, an indication of low factor redundancy. (A) probabilistic participation (60%), (B) additive noise (2.5% bins), (C) timing jitter (SD = 20 bins), and (D) sequence warping (max warping = 266%). For each noise type, we show: (top) examples of synthetic data; (bottom) the diss metric for 20 fits of convNMF for K from 1 to 10; the black line shows the median of the diss metric and the dotted red line shows the true number of factors.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A) Participation noise, (B) additive noise, (C) jitter and (D) warping. For each panel, the top shows an example of data with three sequences and each noise type. The bottom panel shows the dissimilarity of factorizations in different levels of noise, as a function of K. A condition with no noise is shown in blue and dark red represents the highest noise condition with the color gradient spanning the levels between. Noise levels are the same as in Figure 3 and Figure 4. Notice that there is often either a minimum or a distinct feature at K = 3, corresponding to the ground-truth number of sequences in the data.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** (A) Reconstruction error (RMSE) for test data (red) and training data (blue) plotted as a function of the number of components (K) used in convNMF. Twenty independent convNMF fits are shown for each value of K. This panel shows results for 10% participation noise. For synthetic data fits, 10% of the data was held out as the test set. For neural data 5% of the data was held out. Other noise conditions are shown as follows: (B) jitter noise (10 timestep SD); (C) warping (13%); (D) higher additive noise (2.5%); (E) higher jitter noise (25 timestep SD); (F) higher warping (33%) (G) Reconstruction error vs. K for neuronal data collected from premotor cortex (area HVC) of a singing bird (Figure 9) and (H) hippocampus of rat 2 performing a left-right alternation task (Figure 8).

### Strategies for dealing with ambiguous sequence structure

Some sequences can be interpreted in multiple ways, and these interpretations will correspond to different factorizations. A common example arises when neurons are shared between different sequences, as is shown in Figure 6A and B. In this case, there are two ensembles of neurons (1 and 2), that participate in two different types of events. In one event type, ensemble one is active alone, while in the other event type, ensemble one is coactive with ensemble 2. There are two different reasonable factorizations of these data. In one factorization, the two different ensembles are separated into two different factors, while in the other factorization the two different event types are separated into two different factors. We refer to these as ’parts-based’ and ’events-based’ respectively. Note that these different factorizations may correspond to different intuitions about underlying mechanisms. ‘Parts-based’ factorizations will be particularly useful for clustering neurons into ensembles, and ‘events-based’ factorizations will be particularly useful for correlating neural events with behavior.

![Figure 6.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig6-v3.jpg)

**Figure 6.:** Datasets that have neurons shared between multiple sequences can be factorized in different ways, emphasizing discrete temporal events (events-based) or component neuronal ensembles (parts-based), by using orthogonality penalties on $𝐇$ or $𝐖$ to penalize factor correlations (see Table 2). (Left) A dataset with two different ensembles of neurons that participate in two different types of events, with (A) events-based factorization obtained using an orthogonality penalty on $𝐇$ and (B) parts-based factorizations obtained using an orthogonality penalty on $𝐖$. (Right) A dataset with six different ensembles of neurons that participate in three different types of events, with (C) events-based and (D) parts-based factorizations obtained as in (A) and (B).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** Biasing factorizations between sparsity in $𝐖$ or $𝐇$.Two different factorizations of the same simulated data, where a sequence is always repeated precisely three times. Both yield perfect reconstructions, and no cross-factor correlations. The factorizations differ in the amount of features placed in $𝐖$ versus $𝐇$. Both use $K=3$ and $\lambda=0.001$. (A) Factorization achieved using a sparsity penalty on $𝐇$, with $\lambda_{L⁢1⁢𝐇}=1$. (B) Factorization achieved using a sparsity penalty on $𝐖$, with $\lambda_{L⁢1⁢𝐖}=1$.

Here, we show that the addition of penalties on either $𝐖$ or $𝐇$ correlations can be used to shape the factorizations of convNMF, with or without the x-ortho penalty, to produce ‘parts-based’ or ‘events-based’ factorization. Without this additional control, factorizations may be either ‘parts-based’, or ‘events-based’ depending on initial conditions and the structure of shared neurons activities. This approach works because, in ‘events-based’ factorization, the $𝐇$’s are orthogonal (uncorrelated) while the $𝐖$’s have high overlap; conversely, in the ‘parts-based’ factorization, the $𝐖$’s are orthogonal while the $𝐇$’s are strongly correlated. Note that these correlations in $𝐖$ or $𝐇$ are unavoidable in the presence of shared neurons and such correlations do not indicate a redundant factorization. Update rules to implement penalties on correlations in $𝐖$ or $𝐇$ are provided in Table 2 with derivations in Appendix 1. Figure 9—figure supplement 2 shows examples of using these penalties on the songbird dataset described in Figure 9.

$L⁢1$ regularization is a widely used strategy for achieving sparse model parameters (Zhang et al., 2016), and has been incorporated into convNMF in the past (O’Grady and Pearlmutter, 2006; Ramanarayanan et al., 2013). In some of our datasets, we found it useful to include $L⁢1$ regularization for sparsity. The multiplicative update rules in the presence of $L⁢1$ regularization are included in Table 2, and as part of our code package. Sparsity on the matrices $𝐖$ and $𝐇$ may be particularly useful in cases when sequences are repeated rhythmically (Figure 6—figure supplement 1A). For example, the addition of a sparsity regularizer on the $𝐖$ update will bias the $𝐖$ exemplars to include only a single repetition of the repeated sequence, while the addition of a sparsity regularizer on $𝐇$ will bias the $𝐖$ exemplars to include multiple repetitions of the repeated sequence. Like the ambiguities described above, these are both valid interpretations of the data, but each may be more useful in different contexts.

### Quantifying the prevalence of sequential structure in a dataset

While sequences may be found in a variety of neural datasets, their importance and prevalence is still a matter of debate and investigation. To address this, we developed a metric to assess how much of the explanatory power of a seqNMF factorization was due to synchronous vs. asynchronous neural firing events. Since convNMF can fit both synchronous and sequential events in a dataset, reconstruction error is not, by itself, diagnostic of the ‘sequenciness’ of neural activity. Our approach is guided by the observation that in a data matrix with only synchronous temporal structure (i.e. patterns of rank 1), the columns can be permuted without sacrificing convNMF reconstruction error. In contrast, permuting the columns eliminates the ability of convNMF to model data that contains sparse temporal sequences (i.e. high rank patterns) but no synchronous structure. We thus compute a ‘sequenciness’ metric, ranging from 0 to 1, that compares the performance of convNMF on column-shuffled versus non-shuffled data matrices (see Materials and methods), and quantify the performance of this metric in simulated datasets containing synchronous and sequential events with varying prevalence (Figure 7C). We found that this metric varies approximately linearly with the degree to which sequences are present in a dataset. Below, we apply this method to real experimental data and obtain high ‘sequenciness’ scores, suggesting that convolutional matrix factorization is a well-suited tool for summarizing neural dynamics in these datasets.

![Figure 7.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig7-v3.jpg)

**Figure 7.:** (A) Example simulated datasets. Each dataset contains 10 neurons, with varying amounts of additive noise, and varying proportions of synchronous events versus asynchronous sequences. For the purposes of this figure, 'sequence' refers to a sequential pattern with no synchrony between different neurons in the pattern. The duration of each dataset used below is 3000 times, and here 300 timebins are shown. (B) Median percent power explained by convNMF (L = 12; K = 2; $\lambda$=0) for each type of dataset (100 examples of each dataset type). Different colors indicate the three different levels of additive noise shown in A. Solid lines and filled circles indicate results on unshuffled datasets. Note that performance is flat for each noise level, regardless of the probability of sequences vs synchronous events. Dotted lines and open circles indicate results on column-shuffled datasets. When no sequences are present, convNMF performs the same on column-shuffled data. However, when sequences are present, convNMF performs worse on column-shuffled data. (C) For datasets with patterns ranging from exclusively synchronous events to exclusively asynchronous sequences, convNMF was used to generate a ‘Sequenciness’ score. Colors correspond to different noise levels shown in A. Asterisks denote cases where the power explained exceeds the Bonferroni-corrected significance threshold generated from column-shuffled datasets. Open circles denote cases that do not achieve significance. Note that this significance test is fairly sensitive, detecting even relatively low presence of sequences, and that the ‘Sequenciness’ score distinguishes between cases where more or less of the dataset consists of sequences.

### Application of seqNMF to hippocampal sequences

To test the ability of seqNMF to discover patterns in electrophysiological data, we analyzed multielectrode recordings from rat hippocampus (https://crcns.org/data-sets/hc), which were previously shown to contain sequential patterns of neural firing (Pastalkova et al., 2015). Specifically, rats were trained to alternate between left and right turns in a T-maze to earn a water reward. Between alternations, the rats ran on a running wheel during an imposed delay period lasting either 10 or 20 seconds. By averaging spiking activity during the delay period, the authors reported long temporal sequences of neural activity spanning the delay. In some rats, the same sequence occurred on left and right trials, while in other rats, different sequences were active in the delay period during each trial types.

Without reference to the behavioral landmarks, seqNMF was able to extract sequences in both datasets. In Rat 1, seqNMF extracted a single factor, corresponding to a sequence active throughout the running wheel delay period and immediately after, when the rat ran up the stem of the maze (Figure 8A); for 10 fits of K ranging from 1 to 10, the average diss metric reached a minimum at 1 and with $\lambda=2⁢\lambda_{0}$, most runs using the x-ortho penalty extracted a single significant factor (Figure 8C–E). Factorizations of thes data with one factor captured 40.8% of the power in the dataset on average, and had a ‘sequenciness’ score of 0.49. Some runs using the x-ortho penalty extracted two factors (Figure 8E), splitting the delay period sequence and the maze stem sequence; this is a reasonable interpretation of the data, and likely results from variability in the relative timing of running wheel and maze stem traversal. At somewhat lower values of $\lambda$, factorizations more often split these sequences into two factors. At even lower values of $\lambda$, factorizations had even more significant factors. Such higher granularity factorizations may correspond to real variants of the sequences, as they generalize to held-out data or may reflect time warping in the data (Figure 5—figure supplement 2J). However, a single sequence may be a better description of the data because the diss metric displayed a clear minimum at $K=1$ (Figure 8C). In Rat 2, seqNMF typically identified three factors (Figure 8B). The first two correspond to distinct sequences active for the duration of the delay period on alternating left and right trials. A third sequence was active immediately following each of the alternating sequences, corresponding to the time at which the animal exits the wheel and runs up the stem of the maze. For 10 fits of K ranging from 1 to 10, the average diss metric reached a minimum at three and with $\lambda=1.5⁢\lambda_{0}$, most runs with the x-ortho penalty extracted between 2 and 4 factors (Figure 8F–H). Factorizations of these data with three factors captured 52.6% of the power in the dataset on average, and had a pattern ‘sequenciness’ score of 0.85. Taken together, these results suggest that seqNMF can detect multiple neural sequences without the use of behavioral landmarks.

![Figure 8.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig8-v3.jpg)

**Figure 8.:** (A) Firing rates of 110 neurons recorded in the hippocampus of Rat 1 during an alternating left-right task with a delay period (Pastalkova et al., 2015). The single significant extracted x-ortho penalized factor. Both an x-ortho penalized reconstruction of each factor (left) and raw data (right) are shown. Neurons are sorted according to the latency of their peak activation within the factor. The red line shows the onset and offset of the forced delay periods, during which the animal ran on a treadmill. (B) Firing rates of 43 hippocampal neurons recorded in Rat 2 during the same task (Mizuseki et al., 2013). Neurons are sorted according to the latency of their peak activation within each of the three significant extracted sequences. The first two factors correspond to left and right trials, and the third corresponds to running along the stem of the maze. (C) The diss metric as a function of K for Rat 1. Black line represents the median of the black points. Notice the minimum at K = 1. (D) (Left) Reconstruction (red) and correlation (blue) costs as a function of $\lambda$ for Rat 1. Arrow indicates $\lambda=8\times10^{−5}$, used for the x-ortho penalized factorization shown in (A). (E) Histogram of the number of significant factors across 30 runs of x-ortho penalized convNMF. (D) The diss metric as a function of K for Rat 2. Notice the minimum at K = 3. (G–H) Same as in (D–E) but for Rat 2. Arrow indicates $\lambda=8\times10^{−5}$, used for the factorization shown in (B).

### Application of seqNMF to abnormal sequence development in avian motor cortex

We applied seqNMF methods to analyze functional calcium imaging data recorded in the songbird premotor cortical nucleus HVC during singing. Normal adult birds sing a highly stereotyped song, making it possible to detect sequences by averaging neural activity aligned to the song. Using this approach, it has been shown that HVC neurons generate precisely timed sequences that tile each song syllable (Hahnloser et al., 2002; Picardo et al., 2016; Lynch et al., 2016). Songbirds learn their song by imitation and must hear a tutor to develop normal adult vocalizations. Birds isolated from a tutor sing highly variable and abnormal songs as adults (Fehér et al., 2009). Such ‘isolate’ birds provide an opportunity to study how the absence of normal auditory experience leads to pathological vocal/motor development. However, the high variability of pathological ‘isolate’ song makes it difficult to identify neural sequences using the standard approach of aligning neural activity to vocal output.

Using seqNMF, we were able to identify repeating neural sequences in isolate songbirds (Figure 9A). At the chosen $\lambda$ (Figure 9B), x-ortho penalized factorizations typically extracted three significant sequences (Figure 9C). Similarly, the diss measure has a local minimum at $K=3$ (Figure 9—figure supplement 1B). The three-sequence factorization explained 41% of the total power in the dataset, with a sequenciness score of 0.7 andhe extracted sequences included sequences deployed during syllables of abnormally long and variable durations (Figure 9D–F, Figure 9—figure supplement 1A).

![Figure 9.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig9-v3.jpg)

**Figure 9.:** (A) Functional calcium signals recorded from 75 neurons, unsorted, in a singing isolate bird. (B) Reconstruction and cross-orthogonality cost as a function of $\lambda$. The arrow at $\lambda=0.005$ indicates the value selected for the rest of the analysis. (C) Number of significant factors for 100 runs with the x-ortho penalty with $K=10$, $\lambda=0.005$. Arrow indicates three is the most common number of significant factors. (D) X-ortho factor exemplars ($𝐖$’s). Neurons are grouped according to the factor in which they have peak activation, and within each group neurons are sorted by the latency of their peak activation within the factor. (E) The same data shown in (A), after sorting neurons by their latency within each factor as in (D). A spectrogram of the bird’s song is shown at top, with a purple ‘*’ denoting syllable variants correlated with $𝐰_{2}$. (F) Same as (E), but showing reconstructed data rather than calcium signals. Shown at top are the temporal loadings ($𝐇$) of each factor.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig9-figsupp1-v3.jpg)

**Figure 9—figure supplement 1.:** (A) For each of the three extracted sequences, examples of song spectrograms triggered at moments where there is a peak in H. Different examples are separated by a red line. Note that each sequence factor corresponds to a particular syllable type. (B) As a function of $K$, diss measure across all combinations of 10 fits of convNMF. Note the local minima at K = 3. (C) Percent power explained (for convNMF with K = 3 and $\lambda=0$) as a function of L. Note the bend that truncates at approximately 0.25 s, corresponding to a typical syllable duration.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig9-figsupp2-v3.jpg)

**Figure 9—figure supplement 2.:** Illustration of a trade-off between parts-based ($𝐖$ is more strictly orthogonal) and events-based ($𝐇$ is more strictly orthogonal) factorizations in a dataset where some neurons are shared between different sequences. The same data as in Figure 9 is factorized with an orthogonality cost just on $𝐇$ (A, events-based), or just on $𝐖$ (B, parts-based). Below each motivating cartoon factorization, we show x-ortho penalized convNMF fits ($𝐖$ and $𝐇$ together with the reconstruction) of the data in Figure 9. The right panels contain the raw data sorted according to these factorizations. Favoring events-based or parts-based factorizations is a matter of preference. Parts-based factorizations are particularly useful for separating neurons into ensembles. Events-based factorizations are particularly useful for identifying what neural events occur when.

In addition, the extracted sequences exhibit properties not observed in normal adult birds. We see an example of two distinct sequences that sometimes, but not always, co-occur (Figure 9). We observe that a shorter sequence (green) occurs alone on some syllable renditions while a second, longer sequence (purple) occurs simultaneously on other syllable renditions. We found that biasing x-ortho penalized convNMF towards ’parts-based’ or ’events-based’ factorizations gives a useful tool to visualize this feature of the data (Figure 9—figure supplement 2). This probabilistic overlap of different sequences is highly atypical in normal adult birds (Hahnloser et al., 2002; Long et al., 2010; Picardo et al., 2016; Lynch et al., 2016) and is associated with abnormal variations in syllable structure—in this case resulting in a longer variant of the syllable when both sequences co-occur. This acoustic variation is a characteristic pathology of isolate song (Fehér et al., 2009).

Thus, even though we observe HVC generating sequences in the absence of a tutor, it appears that these sequences are deployed in a highly abnormal fashion.

### Application of seqNMF to a behavioral dataset: song spectrograms

Although we have focused on the application of seqNMF to neural activity data, these methods naturally extend to other types of high-dimensional datasets, including behavioral data with applications to neuroscience. The neural mechanisms underlying song production and learning in songbirds is an area of active research. However, the identification and labeling of song syllables in acoustic recordings is challenging, particularly in young birds in which song syllables are highly variable. Because automatic segmentation and clustering often fail, song syllables are still routinely labelled by hand (Okubo et al., 2015). We tested whether seqNMF, applied to a spectrographic representation of zebra finch vocalizations, is able to extract meaningful features in behavioral data. Using the x-ortho penalty, factorizations correctly identified repeated acoustic patterns in juvenile songs, placing each distinct syllable type into a different factor (Figure 10). The resulting classifications agree with previously published hand-labeled syllable types (Okubo et al., 2015). A similar approach could be applied to other behavioral data, for example movement data or human speech, and could facilitate the study of neural mechanisms underlying even earlier and more variable stages of learning. Indeed, convNMF was originally developed for application to spectrograms (Smaragdis, 2004); notably it has been suggested that auditory cortex may use similar computations to represent and parse natural statistics (Młynarski and McDermott, 2018).

![Figure 10.](https://cdn.elifesciences.org/articles/38471/elife-38471-fig10-v3.jpg)

**Figure 10.:** (A) Spectrogram of juvenile song, with hand-labeled syllable types (Okubo et al., 2015). (B) Reconstruction cost and x-ortho cost for these data as a function of $\lambda$. Arrow denotes $\lambda=0.0003$, which was used to run convNMF with the x-ortho penalty (C) $𝐖$’s for this song, fit with $K=8$, $L=200⁢m⁢s$, $\lambda=0.0003$. Note that there are three non-empty factors, corresponding to the three hand-labeled syllables a, b, and c. (D) X-ortho penalized $𝐇$’s (for the three non-empty factors) and reconstruction of the song shown in (A) using these factors.

## Discussion

As neuroscientists strive to record larger datasets, there is a need for rigorous tools to reveal underlying structure in high-dimensional data (Gao and Ganguli, 2015; Sejnowski et al., 2014; Churchland and Abbott, 2016; Bzdok and Yeo, 2017). In particular, sequential structure is increasingly regarded as a fundamental property of neuronal circuits (Hahnloser et al., 2002; Harvey et al., 2012; Okubo et al., 2015; Pastalkova et al., 2008), but standardized statistical approaches for extracting such structure have not been widely adopted or agreed upon. Extracting sequences is particularly challenging when animal behaviors are variable (e.g. during learning) or absent entirely (e.g. during sleep).

Here, we explored a simple matrix factorization-based approach to identify neural sequences without reference to animal behavior. The convNMF model elegantly captures sequential structure in an unsupervised manner (Smaragdis, 2004; Smaragdis, 2007; Peter et al., 2017). However, in datasets where the number of sequences is not known, convNMF may return inefficient and inconsistent factorizations. To address these challenges, we introduced a new regularization term to penalize correlated factorizations, and developed a new dissimilarity measure to assess model stability. Both proposed methods can be used to infer the number of sequences in neural data and are highly robust to noise. For example, even when (synthetic) neurons participate probabilistically in sequences at a rate of 50%, the model typically identifies factors with greater than 80% similarity to the ground truth (Figure 3A). Additionally, these methods perform well even with very limited amounts of data: for example successfully extracting sequences that only appear a handful of times in a noisy data stream (Figure 3—figure supplement 2).

The x-ortho penalty developed in this paper may represent a useful improvement over traditional orthogonality regularizations or suggest how traditional regularization penalties may be usefully modified. First, it simultaneously provides a penalty on correlations in both $𝐖$ and $𝐇$, thus simplifying analyses by having only one penalty term. Second, although the x-ortho penalty does not formally constitute regularization due to its inclusion of the data $𝐗$, we have described how the penalty can be approximated by a data-free regularization with potentially useful properties (Appendix 2). Specifically, the data-free regularization contains terms corresponding to weighted orthogonality in (smoothed) $𝐇$ and $𝐖$, where the weights focus the orthogonality penalty preferentially on those factors that contribute the most power to the reconstruction. This concept of using power-weighted regularization penalties may be applicable more generally to matrix factorization techniques.

As in many data analysis scenarios, a variety of statistical approaches may be brought to bear on finding sequences in neural data. A classic method is to construct cross-correlogram plots, showing spike time correlations between pairs of neurons at various time lags. However, other forms of spike rate covariation, such as trial-to-trial gain modulation, can produce spurious peaks in this measure (Brody, 1999); recent work has developed statistical corrections for these effects (Russo and Durstewitz, 2017). After significant pairwise correlations are identified, one can heuristically piece together pairs of neurons with significant interactions into a sequence. This bottom-up approach may be better than seqNMF at detecting sequences involving small numbers of neurons, since seqNMF specifically targets sequences that explain large amounts of variance in the data. On the other hand, bottom-up approaches to sequence extraction may fail to identify long sequences with high participation noise or jitter in each neuron (Quaglio et al., 2018). One can think of seqNMF as a complementary top-down approach, which performs very well in the high-noise regime since it learns a template sequence at the level of the full population that is robust to noise at the level of individual units.

Statistical models with a dynamical component, such as Hidden Markov Models (HMMs) (Maboudi et al., 2018), linear dynamical systems (Kao et al., 2015), and models with switching dynamics (Linderman et al., 2017), can also capture sequential firing patterns. These methods will typically require many hidden states or latent dimensions to capture sequences, similar to PCA and NMF which require many components to recover sequences. Nevertheless, visualizing the transition matrix of an HMM can provide insight into the order in which hidden states of the model are visited, mapping onto different sequences that manifest in population activity (Maboudi et al., 2018). One advantage of this approach is that it can model sequences that occasionally end prematurely, while convNMF will always reconstruct the full sequence. On the other hand, this pattern completion property makes convNMF robust to participation noise and jitter. In contrast, a standard HMM must pass through each hidden state to model a sequence, and therefore may have trouble if many of these states are skipped. Thus, we expect HMMs and related models to exhibit complementary strengths and weaknesses when compared to convNMF.

Another strength of convNMF is its ability to accommodate sequences with shared neurons, as has been observed during song learning (Okubo et al., 2015). Sequences with shared neurons can be interpreted either in terms of ‘parts-based’ or ‘events-based’ factorizations (Figure 9—figure supplement 2). This capacity for a combinatorial description of overlapping sequences distinguishes convNMF from many other methods, which assume that neural patterns/sequences do not co-occur in time. For example, a vanilla HMM can only model each time step with a single hidden state and thus cannot express parts-based representations of neural sequences. Likewise, simple clustering models would assign each time interval to a single cluster label. Adding hierarchical and factorial structure to these models could allow them to test for overlapping neural sequences (see e.g. Ghahramani and Jordan, 1997); however, we believe seqNMF provides a simpler and more direct framework to explore this possibility.

Finally, as demonstrated by our development of new regularization terms and stability measures, convolutional matrix factorization is a flexible and extensible framework for sequence extraction. For example, one can tune the overall sparsity in the model by introducing additional L1 regularization terms. The loss function may also be modified, for example substituting in KL divergence or more general $\beta$-divergence (Villasana et al., 2018). Both L1 regularization and $\beta$-divergence losses are included in the seqNMF code package so that the model can be tuned to the particular needs of future analyses. Future development could incorporate outlier detection into the objective function (Netrapalli et al., 2014), or online optimization methods for large datasets (Wang et al., 2013). Other extensions to NMF, for example, Union of Intersections NMF Cluster (Ubaru et al., 2017), have yielded increased robustness and consistency of NMF factorizations, and could potentially also be modified for application to convNMF. Thus, adding convolutional structure to factorization-based models of neural data represents a rich opportunity for statistical neuroscience.

Despite limiting ourselves to a relatively simple model for the purposes of this paper, we extracted biological insights that would have been difficult to otherwise achieve. For example, we identified neural sequences in isolated songbirds without aligning to song syllables, enabling new research into songbird learning on two fronts. First, since isolated and juvenile birds sing highly variable songs that are not easily segmented into stereotyped syllables, it is difficult and highly subjective to identify sequences by aligning to human-labeled syllables. SeqNMF enables the discovery and future characterization of neural sequences in these cases. Second, while behaviorally aligned sequences exist in tutored birds, it is that possible many neural sequences—for example, in different brain areas or stages of development—are not closely locked to song syllables. Thus, even in cases where stereotyped song syllables exist, behavioral alignment may overlook relevant sequences and structure in the data. These lessons apply broadly to many neural systems, and demonstrate the importance of general-purpose methods that extract sequences without reference to behavior. Our results show that convolutional matrix factorization models are an attractive framework to meet this need.

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
      <td>Software, algorithm</td>
      <td>seqNMF</td>
      <td>this paper</td>
      <td>https://github.com/FeeLab/seqNMF</td>
      <td>start with demo.m</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>convNMF</td>
      <td>Smaragdis, 2004; Smaragdis, 2007</td>
      <td>https://github.com/colinvaz/nmf-toolbox</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>sparse convNMF</td>
      <td>O’Grady and Pearlmutter, 2006; Ramanarayanan et al., 2013</td>
      <td>https://github.com/colinvaz/nmf-toolbox</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NMF orthogonality penalties</td>
      <td>Choi, 2008; Chen and Cichocki, 2004</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>other NMF extensions</td>
      <td>Cichocki et al., 2009</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NMF</td>
      <td>Lee and Seung, 1999</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CNMF_E (cell extraction)</td>
      <td>Zhou et al., 2018</td>
      <td>https://github.com/zhoupc/CNMF_E</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>www.mathworks.com, RRID:SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (adeno-associated virus)</td>
      <td>AAV9.CAG.GCaMP6f. WPRE.SV40</td>
      <td>Chen et al., 2013</td>
      <td>Addgene viral prep # 100836-AAV9, http://n2t.net/addgene:100836, RRID:Addgene_100836</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Miniature microscope</td>
      <td>Inscopix</td>
      <td>https://www.inscopix.com/nvista</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Contact for resource sharing

Further requests should be directed to Michale Fee (fee@mit.edu).

### Software and data availability

The seqNMF MATLAB code is publicly available as a github repository, which also includes our songbird data (Figure 9) for demonstration (Mackevicius et al., 2018; copy archived at https://github.com/elifesciences-publications/seqNMF).

The repository includes the seqNMF function, as well as helper functions for selecting $\lambda$, testing the significance of factors, plotting, and other functions. It also includes a demo script with an example of how to select $\lambda$ for a new dataset, test for significance of factors, plot the seqNMF factorization, switch between parts-based and events-based factorizations, and calculate cross-validated performance on a masked test set.

### Generating simulated data

We simulated neural sequences containing between 1 and 10 distinct neural sequences in the presence of various noise conditions. Each neural sequence was made up of 10 consecutively active neurons, each separated by three timebins. The binary activity matrix was convolved with an exponential kernel ($\tau=10$ timebins) to resemble neural calcium imaging activity.

### SeqNMF algorithm details

The x-ortho penalized convNMF algorithm is a direct extension of the multiplicative update convNMF algorithm (Smaragdis, 2004), and draws on previous work regularizing NMF to encourage factor orthogonality (Chen and Cichocki, 2004).

The uniqueness and consistency of traditional NMF has been better studied than convNMF. In special cases, NMF has a unique solution comprised of sparse, ‘parts-based’ features that can be consistently identified by known algorithms (Donoho and Stodden, 2004; Arora et al., 2011). However, this ideal scenario does not hold in many practical settings. In these cases, NMF is sensitive to initialization, resulting in potentially inconsistent features. This problem can be addressed by introducing additional constraints or regularization terms that encourage the model to extract particular, e.g. sparse or approximately orthogonal features (Huang et al., 2014; Kim and Park, 2008). Both theoretical work and empirical observations suggest that these modifications result in more consistently identified features (Theis et al., 2005; Kim and Park, 2008).

For x-ortho penalized seqNMF, we added to the convNMF cost function a term that promotes competition between overlapping factors, resulting in the following cost function:

$$
(W~,H~)=arg minW,H(||X~−X||_{F}^{2}+\lambda||(W⊛⊤X)SH^{⊤}||_{1,i\neqj})
$$

We derived the following multiplicative update rules for $𝐖$ and $𝐇$ (Appendix 1):

$$
W_{⋅⋅ℓ}←W_{⋅⋅ℓ}\times\frac{X(Hℓ→)^{⊤}}{X~(Hℓ→)^{⊤}+\lambdaX←ℓSH^{⊤}(1−I)}
$$



$$
H←H\times\frac{W⊛⊤X}{W⊛⊤X~+\lambda(1−I)(W⊛⊤XS)}
$$

where the division and $\times$ are element-wise. The operator $(⋅)ℓ→$ shifts a matrix in the $→$ direction by $ℓ$ timebins, that is a delay by $ℓ$ timebins, and $(⋅)←ℓ$ shifts a matrix in the $←$ direction by $ℓ$ timebins (notation summary, Table 1). Note that multiplication with the $K\timesK$ matrix $(𝟏-𝐈)$ effectively implements factor competition because it places in the $k$th row a sum across all other factors. These update rules are derived in Appendix 1 by taking the derivative of the cost function in Equation 8 and choosing an appropriate learning rate for each element.

In addition to the multiplicative updates outlined in Table 2, we also renormalize so rows of $𝐇$ have unit norm; shift factors to be centered in time such that the center of mass of each $𝐖$ pattern occurs in the middle; and in the final iteration run one additional step of unregularized convNMF to prioritize the cost of reconstruction error over the regularization (Algorithm 1). This final step is done to correct a minor suppression in the amplitude of some peaks in $𝐇$ that may occur within $2⁢L$ timebins of neighboring sequences.

#### Testing the significance of each factor on held-out data

In order to test whether a factor is significantly present in held-out data, we measured the distribution across timebins of the overlaps of the factor with the held-out data, and compared the skewness of this distribution to the null case (Figure 1). Overlap with the data is measured as $𝐖⁢⊛⊤⁢𝐗$, a quantity which will be high at timepoints when the sequence occurs, producing a distribution of $𝐖⁢⊛⊤⁢𝐗$ with high skew. In contrast, a distribution of overlaps exhibiting low skew indicates a sequence is not present in the data, since there are few timepoints of particularly high overlap. We estimated what skew levels would appear by chance by constructing null factors where temporal relationships between neurons have been eliminated. To create such null factors, we start from the real factors then circularly shift the timecourse of each neuron by a random amount between 0 and $L$. We measure the skew of the overlap distributions for each null factor, and ask whether the skew we measured for the real factor is significant at p-value $\alpha$, that is, if it exceeds the Bonferroni corrected $((1-\frac{\alpha}{K})\times100)^{t⁢h}$ percentile of the null skews (see Figure 2—figure supplement 1).

<table>
  <thead>
    <tr>
      <th>Algorithm 1: SeqNMF (x-ortho algorithm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Input: Data matrix 𝐗, number of factors K, factor duration L, regularization                   strength λ    Output: Factor exemplars 𝐖, factor timecourses 𝐇1 Initialize 𝐖 and 𝐇 randomly 2 Iter = 1 3 While (Iter &lt; maxIter) and (Δ cost &gt; tolerance) do4       Update 𝐇 using multiplicative update from Table 2 5       Shift 𝐖 and 𝐇 to center 𝐖’s in time 6       Renormalize 𝐖 and 𝐇 so rows of 𝐇 have unit norm 7       Update 𝐖 using multiplicative update from Table 2 8       Iter = Iter + 19 Do one final unregularized convNMF update of 𝐖 and 𝐇10 return</td>
    </tr>
  </tbody>
</table>

Note that if $\lambda$ is set too small, seqNMF will produce multiple redundant factors to explain one sequence in the data. In this case, each redundant candidate sequence will pass the significance test outlined here. We will address below a procedure for choosing $\lambda$ and methods for determining the number of sequences.

#### Calculating the percent power explained by a factorization

In assessing the relevance of sequences in a dataset, it can be useful to calculate what percentage of the total power in the dataset is explained by the factorization ($𝐗~$). The total power in the data is $\sum𝐗^{2}$ (abbreviating $\sum_{n=1}^{N}\sum_{t=1}^{T}x_{n⁢t}^{2}$ to $\sumX^{2}$). The power unexplained by the factorization is $\sum(X−X~)^{2}$. Thus, the percent of the total power explained by the factorization is:

$$
\frac{\sum𝐗^{2}-\sum(𝐗-𝐗~)^{2}}{\sum𝐗^{2}}=\frac{\sum2⁢𝐗⁢𝐗~-𝐗~^{2}}{\sum𝐗^{2}}
$$

#### ‘Sequenciness’ score

The ‘sequenciness’ score was developed to distinguish between datasets with exclusively synchronous patterns, and datasets with temporally extended sequential patterns. This score relies on the observation that synchronous patterns are not disrupted by shuffling the columns of the data matrix. The ‘sequenciness’ score is calculated by first computing the difference between the power explained by seqNMF in the actual and column-shuffled data. This quantity is then divided by the power explained in the actual data minus the power explained in data where each neuron is time-shuffled by a different random permutation.

#### Choosing appropriate parameters for a new dataset

The choice of appropriate parameters ($\lambda$, $K$ and $L$) will depend on the data type (sequence length, number, and density; amount of noise; etc.).

In practice, we found that results were relatively robust to the choice of parameters. When $K$ or $L$ is set larger than necessary, seqNMF tends to simply leave the unnecessary factors or times empty. For choosing $\lambda$, the goal is to find the ‘sweet spot’ (Figure 4) to explain as much data as possible while still producing sensible factorizations, that is, minimally correlated factors, with low values of $||(𝐖⁢⊛⊤⁢𝐗)⁢𝐒𝐇^{⊤}||_{1,i\neqj}$. Our software package includes demo code for determining the best parameters for a new type of data, using the following strategy:

In some applications, achieving the desired accuracy may depend on choosing a $\lambda$ that allows some inconsistency. It is possible to deal with this remaining inconsistency by comparing factors produced by different random initializations, and only considering factors that arise from several different initializations, a strategy that has been previously applied to standard convNMF on neural data (Peter et al., 2017).

During validation of our procedure for choosing $\lambda$, we compared factorizations to ground truth sequences as shown in Figure 4. To find the optimal value of $\lambda$, we used the product of two curves. The first curve was obtained by calculating the fraction of fits in which the true number of sequences was recovered as a function of $\lambda$. The second curve was obtained by calculating similarity to ground truth as a function of $\lambda$ (see Materials and methods section ‘Measuring performance on noisy fits by comparing seqNMF sequence to ground-truth sequences’). The product of these two curves was smoothed using a three-sample boxcar sliding window, and the width was found as the values of $\lambda$ on either side of the peak value that correspond most closely to the half-maximum points of the curve.

#### Preprocessing

While seqNMF is generally quite robust to noisy data, and different types of sequential patterns, proper preprocessing of the data can be important to obtaining reasonable factorizations on real neural data. A key principle is that, in minimizing the reconstruction error, seqNMF is most strongly influenced by parts of the data that exhibit high variance. This can be problematic if the regions of interest in the data have relatively low amplitude. For example, high firing rate neurons may be prioritized over those with lower firing rate. As an alternative to subtracting the mean firing rate of each neuron, which would introduce negative values, neurons could be normalized divisively or by subtracting off a NMF reconstruction fit using a method that forces a non-negative residual (Kim and Smaragdis, 2014). Additionally, variations in behavioral state may lead to seqNMF factorizations that prioritize regions of the data with high variance and neglect other regions. It may be possible to mitigate these effects by normalizing data, or by restricting analysis to particular subsets of the data, either by time or by neuron.

#### Measuring performance on noisy data by comparing seqNMF sequences to ground-truth sequences

We wanted to measure the ability of seqNMF to recover ground-truth sequences even when the sequences are obstructed by noise. Our noisy data consisted of three ground-truth sequences, obstructed by a variety of noise types. For each ground-truth sequence, we found its best match among the seqNMF factors. This was performed in a greedy manner. Specifically, we first computed a reconstruction for one of the ground-truth factors. We then measured the correlation between this reconstruction and reconstructions generated from each of the extracted factors, and chose the best match (highest correlation). Next, we matched a second ground-truth sequence with its best match (highest correlation between reconstructions) among the remaining seqNMF factors, and finally we found the best match for the third ground-truth sequence. The mean of these three correlations was used as a measure of similarity between the seqNMF factorization and the ground-truth (noiseless) sequences.

#### Testing generalization of factorization to randomly held-out (masked) data entries

The data matrix $𝐗$ was divided into training data and test data by randomly selecting 5 or 10% of matrix entries to hold out. Specifically, the objective function (Equation 5, in the Results section) was modified to:

$$
(12)arg minW,H||M\times(W⊛H−X)||_{F}^{2}+ℛ
$$

where $\times$ indicates elementwise multiplication (Hadamard product) and $𝐌$ is a binary matrix with 5 or 10% of the entries randomly selected to be zero (held-out test set) and the remaining 95 or 90% set to one (training set). To search for a solution, we reformulate this optimization problem as:

$$
arg minW,H,Z||W⊛H−Z||_{F}^{2}+ℛsubjecttoM\timesZ=M\timesX
$$

where we have introduced a new optimization variable $𝐙$, which can be thought of as a surrogate dataset that is equal to the ground truth data only on the training set. The goal is now to minimize the difference between the model estimate, $𝐗~=𝐖⊛𝐇$, and the surrogate, $𝐙$, while constraining $𝐙$ to equal $𝐗$ at unmasked elements (where $m_{i⁢j}=1$) and allowing $𝐙$ to be freely chosen at masked elements (where $m_{i⁢j}=0$). Clearly, at masked elements, the best choice is to make $𝐙$ equal to the current model estimate $𝐗~$ as this minimizes the cost function without violating the constraint. This leads to the following update rules which are applied cyclically to update $𝐙$, $𝐖$, and $𝐇$.

$$
Z_{nt}←{X_{nt}ifM_{nt}=1(W⊛H)_{nt}ifM_{nt}=0
$$



$$
W_{⋅⋅ℓ}←W_{⋅⋅ℓ}\times\frac{Z(Hℓ→)^{⊤}}{X~(Hℓ→)^{⊤}+\lambdaZ←ℓSH^{⊤}(1−I)}
$$



$$
H←H\times\frac{W⊛⊤Z}{W⊛⊤X~+\lambda(1−I)(W⊛⊤ZS)}
$$

The measure used for testing generalization performance was root mean squared error (RMSE). For the testing phase, RMSE was computed from the difference between $𝐗~$ and the data matrix $𝐗$ only for held-out entries.

### Hippocampus data

The hippocampal data was collected in the Buzsaki lab (Pastalkova et al., 2015; Mizuseki et al., 2013), and is publicly available on the Collaborative Research in Computational Neuroscience (CRCNS) Data sharing website. The dataset we refer to as ‘Rat 1’ is in the hc-5 dataset, and the dataset we refer to as ‘Rat 2’ is in the hc-3 dataset. Before running seqNMF, we processed the data by convolving the raw spike trains with a gaussian kernel of standard deviation 100 ms.

### Animal care and use

We used male zebra finches (Taeniopygia guttata) from the MIT zebra finch breeding facility (Cambridge, MA). Animal care and experiments were carried out in accordance with NIH guidelines, and reviewed and approved by the Massachusetts Institute of Technology Committee on Animal Care (protocol 0715-071-18).

In order to prevent exposure to a tutor song, birds were foster-raised by female birds, which do not sing, starting on or before post-hatch day 15. For experiments, birds were housed singly in custom-made sound isolation chambers.

### Data acquisition and preprocessing

The calcium indicator GCaMP6f was expressed in HVC by intracranial injection of the viral vector AAV9.CAG.GCaMP6f.WPRE.SV40 (Chen et al., 2013) into HVC. In the same surgery, a cranial window was made using a GRIN (gradient index) lens (1 mm diamenter, 4 mm length, Inscopix). After at least one week, in order to allow for sufficient viral expression, recordings were made using the Inscopix nVista miniature fluorescent microscope.

Neuronal activity traces were extracted from raw fluorescence movies using the CNMF_E algorithm, a constrained non-negative matrix factorization algorithm specialized for microendoscope data by including a local background model to remove activity from out-of-focus cells (Zhou et al., 2018).

We performed several preprocessing steps before applying seqNMF to functional calcium traces extracted by CNMF_E. First, we estimated burst times from the raw traces by deconvolving the traces using an AR-2 process. The deconvolution parameters (time constants and noise floor) were estimated for each neuron using the CNMF_E code package (Zhou et al., 2018). Some neurons exhibited larger peaks than others, likely due to different expression levels of the calcium indicator. Since seqNMF would prioritize the neurons with the most power, we renormalized by dividing the signal from each neuron by the sum of the maximum value of that row and the $95^{t⁢h}$ percentile of the signal across all neurons. In this way, neurons with larger peaks were given some priority, but not much more than that of neurons with weaker signals.

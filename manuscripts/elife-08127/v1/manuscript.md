# The number of olfactory stimuli that humans can discriminate is still unknown

## Authors

- Richard C Gerkin<sup>1</sup> †
- Jason B Castro<sup>2</sup>

### Affiliations

1. School of Life Sciences Arizona State University Tempe United States
2. Department of Psychology Bates College Lewiston United States
3. Program in Neuroscience Bates College Lewiston United States

† Corresponding author

## Abstract

It was recently proposed (Bushdid et al., 2014) that humans can discriminate between at least a trillion olfactory stimuli. Here we show that this claim is the result of a fragile estimation framework capable of producing nearly any result from the reported data, including values tens of orders of magnitude larger or smaller than the one originally reported in (Bushdid et al., 2014). Additionally, the formula used to derive this estimate is well-known to provide an upper bound, not a lower bound as reported. That is to say, the actual claim supported by the calculation is in fact that humans can discriminate at most one trillion olfactory stimuli. We conclude that there is no evidence for the original claim.

## Introduction

A recent paper (Bushdid et al., 2014) proposed that humans can discriminate between at least a trillion olfactory stimuli. Using that paper's methods to reanalyze the data it presented, we show that this estimate is problematically fragile. Specifically, it varies systematically and sensitively (over tens of orders of magnitude, in both directions), for very modest changes in incidental experimental and analysis parameters against which a result ought to be robust. Had the experiment enlisted ∼ 100 additional subjects similar to the original ones, the same analysis would have concluded that all possible stimuli are discriminable (i.e., that each of the more than 1029 olfactory stimuli possible in their framework are mutually discriminable). By contrast, if the same experimental data were analyzed using moderately more conservative statistical criteria, it would have concluded that there are fewer than 5000 discriminable olfactory stimuli—no larger than the folk wisdom value that the new estimate purports to replace.

Therefore, under this framework, data describing the same underlying perceptual abilities admit a wide range of extremely disparate (varying over 25 orders of magnitude), yet unobjectionable alternative conclusions (including both the largest and smallest possible estimates allowed by the analysis framework). We conclude that the framework is unsound: there may be trillions of discriminable olfactory stimuli, or more, or fewer, but the framework does not provide the means for settling this question. Here we first demonstrate the framework's fragility, and then explain the sources of that fragility. For most of this paper, we remain agnostic about whether the framework is conceptually sound, to highlight the fact that it has strictly methodological problems of a statistical origin that do not depend on the validity of a competing set of assumptions.

We also show that the formula used to derive the estimated number of discriminable stimuli, given an estimated perceptual limen, yields an upper bound, not a lower bound, meaning that any estimate derived here or in (Bushdid et al., 2014), under any assumptions, is a maximum and not a minimum. In other words, the original paper in fact supports the conclusion that humans can discriminate at most one trillion olfactory stimuli (or more or fewer, due to the problem described above), a rather uninspiring claim. In a concluding section, we explore possibilities for improving the estimate.

### Problems with the estimate

The first main concern is that the estimated number of discriminable stimuli depends steeply, systematically, and non-asymptotically on choices of arbitrary experimental parameters, among them the number of subjects enrolled, the number of discrimination tests performed, and the threshold for statistical significance. We show below that the order of magnitude claim of ‘one trillion olfactory stimuli’ requires that those parameters assume a very narrow set of values. Certainly, the precise value of an estimate may change as additional data are collected, but the estimate should not change in expectation; it should not be possible to make an estimate arbitrarily large (or small), simply by collecting more (or less) data. Similarly, the estimate itself should not become arbitrarily small or large with adjustment of a significance criterion. Estimates that scale systematically with such incidental parameter choices are considered statistically inconsistent (Figure 1). It is the inconsistency of the present estimate that produces a tremendously large space of extremely different, yet unobjectionable alternative conclusions that can be reached about the number of discriminable olfactory stimuli.

![Figure 1.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig1-v1.jpg)

**Figure 1.:** An estimator is consistent if the resulting estimate asymptotically converges (in expectation) as sample size increases (black line). Uncertainty in the estimate (gray area) may shrink with sample size, but the estimate itself should not systematically change with sample size, and should converge on the truth. Estimators without this property are termed inconsistent (the blue line is a relevant example), and are considered unreliable, as the resulting estimate can be heavily biased by the sample size. If the estimate has a minimum and maximum allowed value (see Equation 1), an especially inconsistent estimator can even produce any estimate within that range.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** For each possible value of the number of tests T conducted per mixture class, there is a cumulative distribution of the fraction f of those tests that will be correctly discriminated, under the null hypothesis of chance $(\frac{1}{3})$ responding. The choice of significance threshold α determines the fraction correct required to reject the null hypothesis, and thus count as ‘significantly discriminating’ in the framework. For a given value of α (0.05 shown here, and used in [Bushdid et al., 2014]), the fraction correctly discriminated required to reach this threshold varies greatly with T. Rejecting the null hypothesis can thus be very easy or very hard depending on T (or the number of subjects S, not shown), or on α.

To illustrate that we can correctly recapitulate the analysis undertaken in (Bushdid et al., 2014), Figure 2 shows our reproduction (using raw supplementary data from [Bushdid et al., 2014]) of two critical figures from that paper (Bushdid et al., 2014), from which its main conclusion was drawn. See Table 1 for definitions of parameters used here and in (Bushdid et al., 2014). Figure 3 and Table 2 quantify the fragility of this conclusion, by generating estimates using the same framework under trivial alternative scenarios in which different numbers of subjects (or mixtures) were used, or different choices of statistical threshold (α) were used for assessing discriminability. Thus, we produced all values shown here by analyzing the data from (Bushdid et al., 2014), using the methods described therein, and varying only parameters. Code to reproduce these and all subsequent analyses is available at http://github.com/rgerkin/trillion, documented at http://nbviewer.ipython.org/github/rgerkin/trillion/blob/master/journal.ipynb.

![Figure 2.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig2-v1.jpg)

**Figure 2.:** Compare to Figures 3, 4 in that publication. (A): Discriminability vs mixture overlap, expressed as a percentage of the mixture size N. From this analysis, (Bushdid et al., 2014) derives $\frac{d−N}{N}∼51%$ (vertical dashed line) as the critical value of mixture overlap at which 50% of mixtures achieve ‘significant discriminability’. (B): Estimated number of discriminable mixtures z vs mixture overlap (expressed as a percentage of N) allowing discrimination. The plot is obtained by regression and interpolation of results in A combined with Equation 1, with colors corresponding to values of N as shown in A. For a value of $∼51%$as derived in A, one obtains the ‘trillions’ figure reported in (Bushdid et al., 2014).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** This reproduces Figure 2B from (Bushdid et al., 2014), and can be subsequently used to reproduce Figure 3A and ultimately Figure 3C from (Bushdid et al., 2014). Similar reconstructions, using alternative parameter choices, were used as basis for the findings presented in Figure 3A here. Analogous reconstructions of Figures 2C, 3B,D from (Bushdid et al., 2014) (not shown) were used to generate Figure 3B here.

**Table 1.**
 Definitions of parameters


<table>
  <tbody>
    <tr>
      <td>z</td>
      <td>Estimated number of discriminable olfactory stimuli</td>
    </tr>
    <tr>
      <td>C</td>
      <td>Number of distinct compounds available to make mixtures</td>
    </tr>
    <tr>
      <td>N</td>
      <td>Number of distinct compounds in a mixture</td>
    </tr>
    <tr>
      <td>O</td>
      <td>Number of distinct compounds shared by a mixture pair</td>
    </tr>
    <tr>
      <td>D</td>
      <td>Number of distinct compounds in one mixture of a pair that are not shared by the other. (D=N−O)</td>
    </tr>
    <tr>
      <td>class</td>
      <td>All mixture pairs with the same value of N and D.</td>
    </tr>
    <tr>
      <td>d</td>
      <td>The value of D for which mixture pairs of a given N are more likely than not to be discriminable at a rate significantly above chance.</td>
    </tr>
  </tbody>
</table>

![Figure 3.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig3-v1.jpg)

**Figure 3.:** (A): Heat map showing alternative conclusions reached for different choices of T, the number of mixture pairs per class to test, and application of alternative significance threshold α for discriminability, with the data from (Bushdid et al., 2014). Asterisks (*) show the parameter regime (T = 20 mixtures, $\alpha=0.05$) used in (Bushdid et al., 2014). Other values on each axis are chosen in a geometric progression around those parameters. The contour in the lower right labeled ‘All’ demarcates a regime in which one will conclude that the largest possible number of mixture stimuli (i.e., all $z(d=0)=(12830)>10^{29}$ of them) are discriminable (see Equation 1). The contour in the upper left labeled ‘smallest possible’ demarcates a regime in which one will conclude that the smallest possible number of stimuli are discriminable, that is, only $z(d=N=30)<5000$ of them. The contour labeled ‘colors’ demarcates a regime in which one concludes that the number of discriminable olfactory stimuli is the same order of magnitude as the number of discriminable colors. (B): Heat map similar to left, only with number of subjects on the vertical axis. A choice of $\alpha=0.025$ is necessary to obtain the estimate that (Bushdid et al., 2014) reports for this analysis. (C): Colorscale for A and B, with reference landmarks.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Dependence of the estimate (for mixtures of N = 30) on sample size. Black shows dependence on the number of subjects S enrolled in the study, Red shows dependence on the number of mixtures T tested per mixture class. Once the number of mixtures or subjects tested is $∼150$ (by no means an unusually large sample size), the conclusion that all possible $(CN)$ mixtures are discriminable is guaranteed, in contradiction with experimental results. (B) Dependence of the estimate on the significance threshold α with (red) and without (black) a correction for multiple comparisons. (Bushdid et al., 2014) did not correct for multiple comparisons.

**Table 2.**
 Estimates of z, the number of discriminable olfactory stimuli, for different possible parameters values, for the C = 128, N = 30 case used in (Bushdid et al., 2014)


<table>
  <thead>
    <tr>
      <th colspan="3">A</th>
    </tr>
    <tr>
      <th># Discriminable stimuli (z)</th>
      <th>Significance threshold (α)</th>
      <th># Tests per class (T)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2.02×1012</td>
      <td>0.05*</td>
      <td>20*</td>
    </tr>
    <tr>
      <td>4.56×103†</td>
      <td>0.05*</td>
      <td>5</td>
    </tr>
    <tr>
      <td>1.54×1029‡</td>
      <td>0.05*</td>
      <td>185</td>
    </tr>
    <tr>
      <td>8.94×103</td>
      <td>0.001</td>
      <td>20*</td>
    </tr>
    <tr>
      <td>1.79×104</td>
      <td>0.01</td>
      <td>15</td>
    </tr>
  </tbody>
</table>

_This recapitulates selected points from Figure 3.* Indicates that the parameter value was used in (Bushdid et al., 2014). We assume here that new subjects perform similarly to the original subjects.Note that 4.56×103 (†) and 1.54×1029 (‡) are the smallest and largest possible values allowed by the framework from (Bushdid et al., 2014)._

In Bushdid et al., 2014's experimental framework, there are three sets of experiments, varying in the number of distinct molecular components N per mixture tested. We consider the N = 30 case (without loss of generality) for which there are $∼10^{29}$ possible olfactory stimuli, and for which the smallest possible number of discriminable stimuli is $∼4500$ (see Equation 1 below). Figure 3 and Table 2 thus demonstrate that (1) there is a regime of reasonable parameter choices for which one concludes that all possible olfactory stimuli (i.e., all $∼10^{29}$ of them) are discriminable; and (2) there is another regime of reasonable parameter choices for which one concludes that the smallest possible number of stimuli (i.e., only $∼4500$) are discriminable. The only assumption required to obtain these estimates is that performance in new subjects is similar to performance in the original subjects.

The fragility of the conclusion results from the claim in (Bushdid et al., 2014) that a modest (if very interesting) correlation—between the discriminability of a pair of mixtures and the overlap (fraction of shared components) of those mixtures—is evidence that a particular degree of mixture overlap defines a boundary that partitions the discriminable from the indiscriminable in a very high-dimensional space. Below, we explore the consequences of this decision, and its implications for calculating the number of discriminable olfactory stimuli.

### Explanation of the problems with the estimate

#### Recap of the basic framework

The framework's logic is built on an analogy to color vision, where estimating the number of discriminable colors requires knowing only two numbers: the size of the stimulus space (that is, the range of visible wavelengths), and the minimally discriminable distance between a typical pair of stimuli (Figure 4). Dividing the first number by the second amounts to asking how many discriminable intervals can be ‘packed’ into the stimulus space, with that number providing an estimate of the number of discriminable color stimuli.

![Figure 4.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig4-v1.jpg)

**Figure 4.:** (A): Hypothetical example showing a range of visible wavelengths. Relative to a reference stimulus (thick vertical tick mark), extremely distant stimuli (green circle) in this space are easy to discriminate, whereas extremely close stimuli (red circle) may be impossible to discriminate, as they are beyond the resolution of color vision. At some critical inter-stimulus distance, d, stimuli will be ‘just discriminable’ (black circle). A typical stimulus pair on the space, separated by distance D, will tend to be discriminable if $D>d$, and indiscriminable if $D<d$. (B): This partitioning into discriminable and indiscriminable sets is captured in the sigmoidal shape of the psychometric curve plotting discriminability vs distance. Knowing that an interval of length d on the space will tend to span ‘just discriminable’ stimuli, one can calculate how many such intervals, z, can be ‘packed’ onto the space to estimate the number of discriminable colors.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A): Left, A sharply sigmoidal relationship in which discriminability changes dramatically and categorically at a critical inter-stimulus distance, d. In all panels, d is the value of the inter-stimulus distance D at which a threshold fraction of stimulus pairs are discriminable. In the left panels, this threshold is set at 0.5. Right, The resulting value of d is nearly invariant to the choice of threshold. (B): Same as above, only for a less sharply sigmoidal data set. There is still a narrow regime in which d is largely invariant to choice of threshold. (C): Same as above, only for a weakly sigmoidal data set. Here, there is no principled means for choosing the d that is characteristic of discriminability relationships for stimuli. The data in C do not support an interpretation in which there is defensible characteristic ‘length scale’ for inter-stimulus distances.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A): To explore this possibility, the fraction discriminated vs percent mixture overlap is plotted here. This is analogous to Figure 2, except plotting fraction discriminated directly (as in Figure 4—figure supplement 1), instead of fraction significantly discriminable. The threshold (50%) and the procedure for computing mixture overlap at that threshold are as in Figure 2A. Derived from data in (Bushdid et al., 2014) as for Figure 2. (B): The thick red line shows the critical distance d that would result from the data in (Bushdid et al., 2014) for a range of ‘fraction discriminated’ thresholds between 100% (perfect discrimination), and 33.3% (chance discrimination). The curve was obtained by regression on plots like that in Figure 4—figure supplement 2, by analogy to Figure 2 and (Bushdid et al., 2014). Note that d exhibits a nearly constant-slope relationship with threshold, meaning the data are not defined by a characteristic length scale, much like in Figure 4—figure supplement 1C. The thick black curve shows the relationship between z and the chosen threshold. This relationship was obtained directly from d, using Equation 1, as in (Bushdid et al., 2014). The thin red lines correspond to the same calculation for d but using data for only a single subject (one per line), showing similar sensitivity to the choice of threshold. The absence of a robust d for any individual subject argues that the group data are not simply explained by averaging across a population with well-defined, but diverse values of d. Note that very modest and reasonable alternative choices for the threshold result in extremely disparate estimates. The vertical axis is bounded by the smallest and largest possible number of discriminable stimuli allowed by the framework. The dashed lines are a visual guide to specific (threshold, z) pairs. (C): Box and whisker plots showing the median and inter-quartile range for z when restricting the analysis to individual subjects. Note that the worst performing subjects under one threshold can discriminate many more stimuli than the best performing subjects under a slightly more liberal threshold (compare best subject using a 60% threshold vs worst subject using a 40% threshold). Therefore, it is impossible to report with any confidence the number of discriminable stimuli using this approach. In the main text, we show that the actual framework used in (Bushdid et al., 2014) is nominally employed to make a more principled choice of threshold; however it merely cloaks the arbitrariness of the threshold choice, but does not eliminate it.

Because olfactory stimuli do not have obvious physical dimensions analogous to wavelength, olfaction is not amenable to an identical calculation. Instead, (Bushdid et al., 2014) established a theoretical framework that yielded a similar calculation based upon the same underlying idea. (Bushdid et al., 2014) proposed to divide the size of a investigator-determined olfactory stimulus space by a data-determined variable representing resolution in this space. Instead of being continuous, one dimensional, and defined by some intrinsic stimulus variable like wavelength, the olfactory stimulus space was defined to be the discrete, high-dimensional space spanned by all mixtures containing N = 30 different components (molecules) that could be assembled from a library of C = 128 molecules; (Bushdid et al., 2014) also considers the N = 10 and N = 20 cases, which we ignore in this section with no loss of generality. This space of possible mixture stimuli is astronomically large $(CN)$, owing to the proverbial ‘combinatorial explosion’, and each point in the space corresponds to a specific multi-component mixture.

One definition of distance between stimuli in this space is the number of components D by which the stimuli differ. For example, nearest neighbors would be stimuli sharing all components but one $(D=1)$, and the most distant points in this space would be stimuli differing in all components $(D=N)$.

(Bushdid et al., 2014) showed that discriminability of a stimulus pair tends to increase with the distance D between the stimuli in that pair (Figure 2A), and then argued for the existence of a special distance d corresponding to the D at which stimuli are ‘just discriminable’. In other words, for $D>d$ stimuli should more often than not be considered discriminable and for $D<d$ they should more often than not be considered indiscriminable. By calculating d, one could in turn readily calculate the number of stimuli within a distance $D\leqd$ of a typical point in the stimulus space using the provided formulas. Geometrically, the set of stimuli with distance $D\leqd$ from a reference stimulus corresponds to a filled ‘ball’ of stimuli indiscriminable from the reference stimulus at its center. Conversely, the reference stimulus should be discriminable from stimuli outside the ball. We could thus count the number z of non-overlapping balls that can be packed into the stimulus space, as proposed in (Bushdid et al., 2014), by analogy to the example for color vision:

$$
z(d)=\frac{(CN)}{ball(d/2)}
$$

where ‘ball’ is defined as:

$$
ball(r)=\sumx=0r(Nx)(C−Nx)
$$

Equation 1 produces the final estimate z of the number of discriminable stimuli. Note that while this has been interpreted as ‘the answer’ to the sphere packing problem in high dimensions, it is in fact only a best-case scenario (an upper bound). The exact number of d-spanning spheres that can be packed in a discrete space defined by a particular C and N has in fact only been computed for a few specific, modest cases of these values. In general, it is only possible to report bounds for these values. This is discussed at more length in the section. ‘An upper or a lower bound?’, below, as well in the supplemental materials.

C and N are fixed by experimenter choices, and d—the resolution-like term—is the only quantity derived from data that is related to measured psychophysical performance. Note that for C = 128, N = 30, as used in (Bushdid et al., 2014), the largest and smallest possible values this equation can produce are $∼1.5\times10^{29}$ (for d = 0) and $∼4500$ (for d = N), respectively. Assuming this framework is conceptually unproblematic (but see Meister, 2015), the only question becomes: How do we derive d from the data?

### Derivation of the critical parameter d

#### Thresholding the fraction discriminated

A classic psychometric curve (Figure 4B), showing discriminability as a function of inter-stimulus distance D, admits a few plausible ways to derive d. The simplest is to use a discriminability threshold, such that d corresponds to the distance D at which the ‘fraction correct’ reaches a certain value. In (Bushdid et al., 2014)'s three-alternative forced-choice experiments, chance responding would produce a fraction correct of $\frac{1}{3}$, so the appropriate threshold would be somewhere between $\frac{1}{3}$ and 1. This threshold choice would be arbitrary—we might say that a fraction correct of $\frac{1}{2}$ reflects discriminability, or alternatively we might choose $\frac{2}{3}$ or any other value between $\frac{1}{3}$ and 1.

If the psychometric curve is sufficiently steep near some value of D (Figure 4—figure supplement 1A represents an ideal case) then the derived d will vary minimally over a wide range of choices for the threshold. In this scenario, we might be confident that the d we derive is a truly meaningful measure of resolution—it would be robust. If not (Figure 4—figure supplement 1C), it will be very fragile. We explored this approach (Figure 4—figure supplement 2), and concluded that it does not suffice for deriving a robust d.

### Thresholding the fraction significantly discriminable

The approach actually used in (Bushdid et al., 2014) is instead to apply a threshold not to the fraction discriminated (explored in Figure 4—figure supplement 2), but to the fraction significantly discriminable. In other words, determine for which subjects (or alternatively, for which classes of mixtures) the fraction discriminated is significantly greater than $\frac{1}{3}$, i.e., for which subjects the null hypothesis of chance discrimination can be rejected. To facilitate visualization of this step, (Bushdid et al., 2014) re-plotted the summary data (fraction correctly discriminated) as fraction significantly discriminable (Figure 2A). This view of the data provides a linear relationship between distance D and the fraction significantly discriminable, which holds across all the values of N tested. The relationship is much steeper than for fraction discriminable (compare Figure 2 and Figure 4—figure supplement 2) because this hypothesis-testing step acts as a strong non-linear threshold that exaggerates otherwise small differences in the data. An arbitrary choice of threshold is required; (Bushdid et al., 2014) chose a threshold of 50% significantly discriminable, and computed d from the fraction significantly discriminable using linear regression and interpolation.

Varying the threshold (i.e., 50%) itself (not shown), would change the computed d (and consequently z), but this is not the largest issue. By introducing a hypothesis-testing step, the d derived from Figure 2 now varies systematically with the number of subjects enrolled in the study (and the number of mixtures tested), and with the choice of significance criterion α. This is because each data point used to compute d becomes the binary result of a hypothesis test, each of which depends critically on sample size and test specificity. Because d is then fed into an expression (Equation 1) that explodes geometrically, the result is a recipe for producing any of a range of estimates for z that one might choose. If one enlists more subjects or slackens the significance criterion, a very large (even the largest possible) number will be obtained. If one enlists fewer subjects or makes the significance criterion more strict, a very small (even the smallest possible) number will be obtained. Figure 3—figure supplement 1 shows the explicit dependence of the estimate on each of these quantities alone. Naturally, these can be varied in tandem too, with even more dramatic consequences, as described above (Figure 3 and Table 2).

A hypothesis test is meant to assess the strength of evidence for or against a hypothesis (often against a null hypothesis), not to make a point estimate. However, it may not be uncommon for researchers to use hypothesis testing in the manner done in (Bushdid et al., 2014)—to count the number or fraction of data points exhibiting a certain property. In many cases this may amount to a venial statistical sin with (hopefully) benign consequences. But that is unfortunately not the case in (Bushdid et al., 2014), due in part to the extremely steep dependence of z on d guaranteed by Equation 1.

If one claims that an estimate is meaningful, it is fair to ask how vigorously would one have to defend a specific choice of arbitrary experimental parameters to defend a particular order-of-magnitude range around that estimate. Unfortunately, the systematic sensitivities exhibited here severely undermine the plausibility and relevance of the estimate reported in (Bushdid et al., 2014). Due to these sensitivities, one could pick almost any number of discriminable stimuli in advance, and affirm this number using these or similar data. Ultimately, the absence of a robust d to characterize the data is an insurmountable obstacle for the framework.

## Building the stimulus space

### The structure of the stimulus space

One might ask: what is the right way to calculate d in order to obtain a robust estimate of the number of discriminable stimuli? Before heading down this road and devising alternative statistical approaches, it is worth first clearly articulating the assumptions of a framework in which a single variable plays such a special role. Under what conditions is it sensible to expect that plugging a single data-derived number (d) into Equation 1 will produce a meaningful estimate of the number of discriminable olfactory stimuli?

To gain some intuition into this, we can ask the analogous question in the simplified visual system example (Figure 4) that was used as the principal motivation for the procedure. The ‘sphere packing’ calculation in this case naturally involves measuring the resolution of perception in terms of the stimulus, but its validity is not a consequence of this measurement alone. Rather, the procedure in Figure 4 is sensible because the thing we are calling an independent stimulus dimension (wavelength) is respected as such by perception: we encounter monotonically changing, non-redundant percepts as we move from one extreme of the stimulus space to the other. If we didn't—say, if the same percept ‘blue’ were experienced for several non-overlapping disjoint intervals—the sphere packing formulation would fall apart. We might observe that on average discriminability improves with distance, but this would not be evidence of a characteristic length scale that partitions stimulus pairs into discriminable vs indiscriminable sets.

Thus the sphere-packing framework is valid only if the underlying geometry of stimulus space (that the investigator has designed) aligns with the geometry of perceptual space (as implemented in neural circuitry). Formally, the map from stimulus space to perceptual space needs to be homeomorphic, or nearly so. See (Meister, 2015) for further insight on this issue.

### Redundancy in the stimulus space

Instead of providing evidence for this homeomorphism, it was assumed in (Bushdid et al., 2014) for the purposes of calculation that each component of the molecular library (of size C = 128 in [Bushdid et al., 2014]) spanned an informative additional dimension for perception to explore: each molecule in the library is treated as an olfactory primary that is independent of all the others. This is the assumption, codified in the numerator of Equation 1, that allows for a massive space of potential discriminable stimuli. Indeed, the guaranteed runaway growth of the numerator as molecules are added to the C-sized library was offered in (Bushdid et al., 2014) as an argument for why the reported ‘trillion’ figure is an underestimate—after all, C could always be higher.

It is worthwhile to quantify the behavior of the estimate as C changes. First, the estimate depends geometrically on C, with a power law exponent of ∼30 (Figure 5, blue line). In other words, if the chemical library were doubled, the estimate z would increase by a factor of 230 under constant performance. If the component library were increased to the size of a standard flavor and fragrance catalog (∼2000 chemicals), the estimate would increase to z∼1041, implying a unique olfactory percept for each carbon atom on earth.

![Figure 5.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig5-v1.jpg)

**Figure 5.:** The number of possible stimuli z that can be assembled by choosing N = 30distinct molecules from a library of size C increases geometrically with C (black line). If a library of a different size had been used, and similar subject performance resulted, the estimated number of discriminable stimuli z would grow along a similar trajectory (blue line). Even if performance deteriorated as C increased, the estimate could never fall below the red line, which represents worst-case performance (d = N). This results from the combinatorial explosion inherent in Equation 1.

Subjects' performance could become worse when mixtures are drawn from this larger, more complete library, and we acknowledge that we cannot know in advance what the newly calculated resolution d would be on the new stimulus space. In other words, as the numerator of Equation 1 increased, its denominator (given by Equation 2) might conveniently grow proportionally. Let us therefore assume that with a library of sufficient size, so many mixtures become indiscriminable that the resolution becomes as poor as the framework allows, with d = N. Even in this edge case, if only mixtures differing in all components were ‘just discriminable’, we would still calculate $10^{21}$ discriminable stimuli. If C is increased to $10^{6}$, the smallest possible number of discriminable percepts (under the assumption of worst measurable performance, as above) is $10^{61}$, or 10 million trillion unique olfactory percepts for every carbon atom on earth (Figure 5, red line). One may object that the inflation of C here is an unfair critique, as the perceptual redundancy of molecules must at some point provide an important constraint on the size of the artificially constructed stimulus space. Indeed, it has been reported that as few as thirty components are required to imbue most mixtures with a common smell, even when there is no component overlap between the mixtures (Weiss et al., 2012). But this is the essence of the problem with Equation 1: where does that point lie, and why wasn't the constraint important to consider for the original C = 128 molecular library?

### An upper or a lower bound?

Even if one takes the estimate of d to be unimpeachable, the formula used to derive z does not provide a lower bound as reported in (Bushdid et al., 2014). This much is suggested by the worst-case behavior of Equation 1 as C grows. After all, worst case behavior should correspond to z = 1. If one cannot discriminate anything (maximal d), then there is only one percept. Examining Equation 1 more closely, we see that it is a variant of the so-called Hamming bound for constant weight codes (MacWilliams and Sloane, 1977). which is well-known to be an upper bound for an identically formulated problem in the theory of error-correcting codes. It is, as suggested in (Bushdid et al., 2014), an estimate derived from a hypothetical sphere-packing approach to filling the stimulus space, but it is the largest possible value for the correct answer, not the smallest. Hence, according to the Hamming bound, for $d=N=30$ the upper bound on the number of discriminable stimuli is 4561, and we know the correct answer to be 1 (or 4, depending on conventions, see the Supplemental Materials). Since the upper bound exceeds the correct answer, Equation 1, while not particularly tight as an upper bound, is nonetheless not wrong, so long as we acknowledge that it is an upper and not a lower bound. The same applies for all other values of d, including the one derived from the data in (Bushdid et al., 2014).

Thus Equation 1, as used in (Bushdid et al., 2014), provides no insight into the lower bound for z, with a lower bound being required to overturn conventional wisdom about the number of discriminable stimuli. Instead, to obtain a lower bound one must dispense with the factor of 2 in Equation 1, yielding Levenshtein's constant weight version of the so-called Gilbert-Varshamov bound for error-correcting codes ([Levenshtein, 1971; MacWilliams and Sloane, 1977; Jiang and Vardy, 2004],see Supplemental Materials). A plot of the lower bound obtained in this manner is shown in Figure 6B, along with the reconstructed upper bounds from (Bushdid et al., 2014) a, showing the true bounded interval for z. Intuitively, this corrected lower bound reaches z = 1 for worst-case d, implying sensibly that anosmics cannot discriminate any stimuli. In contrast, the upper bound (reported as a lower bound in 1) is on the order of several thousand for worst case d, showing that it cannot be a lower bound d; this can also be confirmed in Figure 4 of (Bushdid et al., 2014).

![Figure 6.](https://cdn.elifesciences.org/articles/08127/elife-08127-fig6-v1.jpg)

**Figure 6.:** (A): Number of discriminable olfactory stimuli as a function of the estimated difference limen (the fractional mixture overlap allowing discrimination). This is simply the behavior of Equation 1 as a function of d, for the three values of N used in (Bushdid et al., 2014); the red dot (in both A and C) corresponds to the value reported in (Bushdid et al., 2014). The smallest possible estimate (thousands of stimuli) is indicated by the dotted line running the length of the abscissa (note also the y-intercept). As described in the text and in the supplement, this graph in fact shows the behavior of the upper bound (the so-called Hamming bound) for the mathematical problem of sphere packing. Compare with Figure 3D in (Bushdid et al., 2014). (B): Same plot as in A, only using the lower-bound for the same calculation. (C): Upper and lower bounds of the sphere packing problem for the N = 30case (green lines from A and B, respectively. The dark gray bar shows the range of defensible estimates under the sphere-packing framework, using the d calculated in (Bushdid et al., 2014). Using that d, the number of discriminable stimuli may be as small as ∼10,000, and is guaranteed to be no larger than ∼1 trillion. Since the estimate of d is also fragile (Figure 3), the data may in fact support any value in the shaded gray area.

### Avenues for improving the estimate

If one is seeking a conservative estimate of the number of discriminable stimuli in a perceptual space whose organization and intrinsic dimensionality are poorly understood, it is arguably more appropriate to use a model that accounts for the data with the smallest number of dimensions. The massive estimates possible in the framework of (Bushdid et al., 2014) are an immediate consequence of a definition of dimensionality driven by experimenter designation, not data.

We therefore propose an alternative framework: use experimental data to create a working map of the perceptual space, and then apply the sphere-packing framework to that map, rather than to a map of the stimulus space. In cognitive science, psychometrics, and marketing, subject responses to stimuli are used to create maps of the underlying perceptual (or conceptual) representations of those stimuli. These maps are characterized by the attribute that pairs of items which are considered intuitively to be perceptually near (rated similar or difficult to discriminate) are nearer to one another on the map than pairs of items which are perceptually more distant (rated dissimilar or easy to discriminate). There are many algorithms for generating such maps, many of which have been used before in olfaction, including variants of PCA (Zarzo and Stanton, 2006; Khan et al., 2007; Koulakov et al., 2011), non-negative matrix factorization (NMF, [Castro et al., 2013]), and multi-dimensional scaling (Mamlouk et al., 2003). While there are open questions in the generation of these maps (e.g., how many dimensions should they have?), they all have the virtue that their accuracy can be checked (e.g., by examining the correlation between subjects' indications of item pair dissimilarity and the distance between that pair on the map), and thus the maps can be improved. Developing these maps may also have the collateral benefit of revealing stimulus dimensions intrinsic to olfaction (if any), which could constrain the experimental choice of a resolution to measure.

Unfortunately, it is difficult if not impossible to create these maps from the data discussed here, because each mixture of a tested pair is used only once in (Bushdid et al., 2014), in that pair alone, and never in any other pairs. Thus, there are no serial comparisons of the same mixture that could be used to anchor a stimulus on the map relative to a stimulus against which it was not directly compared experimentally. Thus, there is no way to compute distances between stimuli that do not appear together in a tested pair. In other words, the structure of the perceptual space is severely under-determined by the data. In future experiments such serial repetition of already-tested mixtures would be required to build up a data set to which the proposed method could be applied.

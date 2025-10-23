# Author response - Round 1

Authors:
- Joshua B Burt ([ORCID: 0000-0002-5605-2091](https://orcid.org/0000-0002-5605-2091))
- Katrin H Preller ([ORCID: 0000-0003-0413-7672](https://orcid.org/0000-0003-0413-7672))
- Murat Demirtas
- Jie Lisa Ji ([ORCID: 0000-0002-6280-9070](https://orcid.org/0000-0002-6280-9070))
- John H Krystal
- Franz X Vollenweider ([ORCID: 0000-0001-9053-6164](https://orcid.org/0000-0001-9053-6164))
- Alan Anticevic ([ORCID: 0000-0002-4324-0536](https://orcid.org/0000-0002-4324-0536))
- John D Murray ([ORCID: 0000-0003-4115-8181](https://orcid.org/0000-0003-4115-8181))

## Response text

DOI: [10.7554/eLife.69320.sa2](https://doi.org/10.7554/eLife.69320.sa2)

Reviewer #1 (Recommendations for the authors):

P4 – perhaps better to state that GBC 'can be interpreted' as a measure of functional integration.

We now state: “…global brain connectivity (GBC), which is a graph-theoretic statistic that can be interpreted as a measure of functional integration.”

P4 – I realise it is passe to ask for citations of one's own work, however the authors may wish to cite a recent review on the use of neural mass models linking structure and function (Shine et al., 2021 in Nature Neuroscience), as the topic of the review is strongly-aligned with the authors approach.

This new review is now cited.

P6 – is it realistic to model gain as a continually increasing function? There is a natural ceiling to how high the firing rate of a neuron can be, which suggests that a sigmoid transfer function might be a more sensible function. The authors could mitigate this concern by confirming that the firing rate of their neural populations is bounded within reasonable limits by other features of their model (e.g., EI balance).

We now state in the Methods: “Note that while this function is unbounded and therefore does not saturate, we confirmed that the node-averaged firing rates in the gain-modulated model (which do not exceed ∼15Hz throughout the parameter sweep in Figure 2A) remain in a neurobiologically plausible firing-rate regime where this approximation of the F-I curve does not break down.”

P7 – are the off-diagonal elements of the FC matrix normalized separately for 5HT2A vs. placebo conditions? If so, did the authors first check to determine whether there were systematic differences between 5HT2A and placebo that may have been diminished through normalisation?

We now include this clarification: “The location of this regime suggests that neural gain is preferentially modulated on excitatory pyramidal neurons, which nonetheless remain in a specific ratio with inhibitory interneurons.”

P8 – the authors conclude that the model fits reflect the fact that "neural gain is preferentially modulated on excitatory pyramidal neurons", however I wonder whether a more parsimonious description would be that "neural gain is preferentially modulated on excitatory pyramidal neurons, which nonetheless remain in a specific ratio with inhibitory interneurons". Note that this result is further expanded in Figure 2B, but I worry that the interim conclusion may mislead from the final result.

P8 – I really liked the utilisation of other 5HT and DA receptor maps and permutation testing.

Reviewer #2 (Recommendations for the authors):

It would be informative to include some discussion of the connectivity normalization choice. The connectivity matrix diagonals are set to zero and each row is re-scaled to unity, which is equivalent to using the Laplacian. The result of this is that every brain region receives an identical total level of input from other regions in the network. This is particularly interesting given the principal metric of interest is (changes in) global brain connectivity (row/column averages of the FC matrix). The equivalent maps for the anatomical connectivity will be uniform, for the reasons detailed above. Could the authors please discuss: what, if any, is the neurobiological, and/or mathematical rationale for this normalization choice, and what are their thoughts on the above considerations.

We now state in the Methods: “Diagonal elements of the SC matrix were set identically to zero, as the dynamical model (described below) explicitly includes self-coupling terms. Moreover, the SC matrix was row-wise normalized such that the total long-range inputs to each node were normalized. This normalization procedure instantiates the assumption that each local microcircuit receives a balance of local and long-range inputs.”

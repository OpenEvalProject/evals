# Author response - Round 1

Authors:
- Cristina Parigini
- Philip Greulich ([ORCID: 0000-0001-5247-6738](https://orcid.org/0000-0001-5247-6738))

## Response text

DOI: [10.7554/eLife.56532.sa2](https://doi.org/10.7554/eLife.56532.sa2)

Reviewer #1:

[…] The main criticism I have about the work is that the manuscript may misguide the readers to think that the GIA and GPA models are the only models that have been discussed in explaining the clonal statistics. As one of the authors showed in their previous paper (Greulich and Simons, 2016), the basic statistics such as the clone size distribution will change when adding spatial regulation to the voter model class, which is distinct from what is obtained by GIA or GPA. In fact, for all the tissues that have been studied so far, including the gut (10.1016/j.cell.2010.09.016, Lopez-Garcia et al., 2010), seminiferous tubule (Klein et al., 2010, Hara et al., 2014, and 10.1016/j.stem.2018.11.013), and the skin (10.1016/j.stem.2018.09.005), experiments suggest that the spatial correlation between the fates are non-negligible and therefore the asymptotic statistics should follow the voter model. I would assume that there needs to be at least a justification in only studying the cases without spatial interactions here, especially if the authors do not know any specific example that nicely corresponds to their model.

We thank the reviewer for this remark. The reviewer notes correctly that in most tissues cell-extrinsic regelation via cell-cell signalling determines fate choices. This can indeed be represented by a (multi-type) voter model – a lattice model where lost cells are compensated by dividing neighbours. However, it has been shown that a voter model in any dimension larger than one has the same asymptotic rescaled clone size distribution as the corresponding branching process without interaction, which is the type of model we use (shown rigorously by Bramson and Griffeath, 1980, and discussed in the context of cell fate dynamics by Klein and Simons, 2011). For mean clone sizes as function of time t, there is no difference for dimensions larger than two (in the two dimensional scenario merely a logarithmic prefactor distinguishes the mean clone size in both models; since this factor is nearly constant for large t, it often cannot be distinguished by experimental data (Klein and Simons, 2011)).

Therefore, while a voter model may be a more realistic depiction of a tissue with spatial cell-cell interaction, the asymptotic rescaled clone size distribution of such a model is the same as for a corresponding model without spatial regulation, if considering tissues with cell arrangements of dimensions larger than one. Hence, our results would not be different for a corresponding voter model where spatial regulation is included, for two- or three-dimensional tissues such as epithelial sheets and volumnar tissues (e.g. liver or stroma). Yet, we agree that for quasi one-dimensional arrangements of stem cells, as found in seminiferous tubules and intestinal crypts, the clone size distribution differs, and these are indeed not covered by our model.

In the original version of the manuscript we expressed those limitations after the model definition: "This model is a general multi-type branching process, which is suitable to describe cell population dynamics in any dimension larger than one, even under cell-extrinsic regulation (Klein and Simons, 2011; Bramson and Griffeath, 1980)", but we acknowledge that this point warrants a clearer explanation. We therefore now include at this point a paragraph that clarifies the validity range of results to be expected from our model. Furthermore, we now discuss this in the Discussion section.

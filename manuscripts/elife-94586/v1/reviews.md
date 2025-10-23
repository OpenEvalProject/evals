# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure - PSL France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94586.4.sa0](https://doi.org/10.7554/eLife.94586.4.sa0)

This valuable study tackles the well-established overflow metabolism issue by applying a coarse-grained metabolic flux model to predict how individual cells execute various energy strategies, such as respiration versus fermentation. The model's population average is convincing enough to align with experimental observations on overflow metabolism. The potential source of metabolic or proteomic heterogeneity of individual cells remains an open question to be studied. How individual cells adjust their metabolic strategies also requires future study of the underlying mechanisms. Overall, this work provides a key aspect on cell-to-cell variability on general metabolic response.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94586.4.sa1](https://doi.org/10.7554/eLife.94586.4.sa1)

Summary:

Cell metabolism exhibits a well-known behavior in fast-growing cells, which employ seemingly wasteful fermentation to generate energy even in the presence of sufficient environmental oxygen. This phenomenon is known as Overflow Metabolism or the Warburg effect in cancer. It is present in a wide range of organisms, from bacteria and fungi to mammalian cells.

In this work, starting with a metabolic network for Escherichia coli based on sets of carbon sources, and using a corresponding coarse-grained model, the author applies some well-based approximations from the literature and algebraic manipulations. These are used to successfully explain the origins of Overflow Metabolism, both qualitatively and quantitatively, by comparing the results with E. coli experimental data.

By modeling the proteome energy efficiencies for respiration and fermentation, the study shows that these parameters are dependent on the carbon source quality constants K_i (p.115 and 116). It is demonstrated that as the environment becomes richer, the optimal solution for proteome energy efficiency shifts from respiration to fermentation. This shift occurs at a critical parameter value K_A(C).

This counterintuitive result qualitatively explains Overflow Metabolism.

Quantitative agreement is achieved through the analysis of the heterogeneity of the metabolic status within a cell population. By introducing heterogeneity, the critical growth rate is assumed to follow a Gaussian distribution over the cell population, resulting in accordance with experimental data for E. coli. Overflow metabolism is explained by considering optimal protein allocation and cell heterogeneity.

The obtained model is extensively tested through perturbations: (1) Introduction of overexpression of useless proteins; (2) Studying energy dissipation; (3) Analysis of the impact of translation inhibition with different sub-lethal doses of chloramphenicol on Escherichia coli; (4) Alteration of nutrient categories of carbon sources using pyruvate. All model perturbations results are corroborated by E. coli experimental results.

Strengths:

In this work, the author effectively uses modeling techniques typical of Physics to address complex problems in Biology, demonstrating the potential of interdisciplinary approaches to yield novel insights. The use of Escherichia coli as a model organism ensures that the assumptions and approximations are well-supported in existing literature. The model is convincingly constructed and aligns well with experimental data, lending credibility to the findings. In this version, the extension of results from bacteria to yeast and cancer is substantiated by a literature base, suggesting that these findings may have broad implications for understanding diverse biological systems.

Weaknesses:

The author explores the generalization of their results from bacteria to cancer cells and yeast, adapting the metabolic network and coarse-grained model accordingly. In the previous version this generalization was not completely supported by references and data from the literature. This drawback, however, has been treated in this current version, where the authors discuss in much more detail and give references supporting this generalization.

Comments on revisions:

I have no specific comments for the authors. My previous comments were all addressed, discussed and explained.

# Author response - Round 1

Authors:
- Yusuke Himeoka ([ORCID: 0000-0001-8545-1625](https://orcid.org/0000-0001-8545-1625))
- Chikara Furusawa

## Response text

DOI: [10.7554/eLife.98800.4.sa3](https://doi.org/10.7554/eLife.98800.4.sa3)

The following is the authors’ response to the previous reviews

Reply to the comments of the second referee

We sincerely appreciate the positive evaluation and the useful suggestions on our manuscript.

(1) The authors identified key metabolites affecting responses to perturbations in two ways: (i) by fixing a metabolite's value and (ii) by performing a sensitivity analysis. It would be helpful for the modeling community to understand better the differences and similarities in the obtained results. Do both methods identify substrate-level regulators? Is freezing a metabolite's dynamics dramatically changing the metabolic response (and if yes, which ones are so different in the two cases)? Does the scope of the network affect these differences and similarities?

Thank you for these suggestions. We compared the Sobolʼ total sensitivity index with the absolute values of the change in the response coefficient (Figure S6 in the revised manuscript). There is no clear relationship between the two quantities. The Sobolʼ sensitivity analysis quantifies how a perturbation on the concentration of a metabolite X contributes to the overall dynamics. On the other hand, the analysis in which metabolitesʼ concentrations are fixed measures how strongly metabolite X helps propagate the perturbations on the other metabolites throughout the metabolic network. In other words, in the Sobolʼ analysis, we evaluate the outcome when the perturbation is applied directly to metabolite X, whereas in the fixing-metabolites analysis, we consider perturbations applied to other metabolites and assess how X influences those perturbations. We believe this conceptual difference explains why the two quantities do not correlate. We suspect that this lack of correlation is independent of the networkʼs scope, because each method evaluates a different aspect of the system. We would say that both methods identify the effect of the metabolite dynamics on the overall dynamics whatever the form is, i.e. the methods do not distinguish the perturbation on the metabolite affecting the overall dynamics by whether the stoichiometric (reactant) way or, the substrate-level regulations. Thus, identifying the substrate-level regulation by utilizing the methods would be challenging.

(2) Regarding the issues the authors encountered when performing the sensitivity analysis, they can be approached in two ways. First, the authors can check the methods for computing conserved moieties nicely explained by Sauro's group (doi:10.1093/bioinformatics/bti800) and compute them for large-scale networks (but beware of metabolites that belong to several conserved pools). Otherwise, the conserved pools of metabolites can be considered as variables in the sensitivity analysis-grouping multiple parameters is a common approach in sensitivity analysis.

Thank you for this helpful suggestion. Following the method described in the reference, we have computed the Sobolʼ sensitivity index of NADH, NADPH, and Q8H2 (with their counterparts algebraically solved and treated as dependent variables). We have updated Figure S5 accordingly.

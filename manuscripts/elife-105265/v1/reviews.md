# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105265.3.sa0](https://doi.org/10.7554/eLife.105265.3.sa0)

The paper addresses the question of gene epistasis and asks what is the correct null model for which we should declare no epistasis. By reanalyzing synthetic gene array datasets regarding single and double-knockout yeast mutants, and considering two theoretical models of cell growth, the authors reach the valuable conclusion that the product function is a good null model. While the justification of some assumptions is incomplete, the results have the potential to be of value to the field of gene epistasis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105265.3.sa1](https://doi.org/10.7554/eLife.105265.3.sa1)

Summary

Detecting unexpected epistatic interactions between multiple mutations requires a robust null expectation-or neutral function-that predicts the combined effects of multiple mutations on phenotype based on the individual effects of single mutations. This study evaluated the relevance of the product neutrality function, where double-mutant fitness is represented as a multiplicative combination of single-mutant fitness in the absence of epistatic interactions. The authors used a recent large dataset on fitness, specifically yeast colony size, to analyze epistatic interactions.

The study confirmed that the product function outperformed other neutral functions in predicting double-mutant fitness, showing no bias between negative and positive epistatic interactions. Additionally, in the theoretical portion of the study, the authors employed a previously established theoretical model of bacterial cell growth to simulate growth rates of both single- and double-mutants under multiple parameters. The simulations similarly demonstrated that the product function was superior to other functions in predicting the fitness of hypothetical double-mutants. Based on these findings, the authors concluded that the product function is a robust tool for analyzing epistatic interactions in growth fitness and effectively reflects how growth rates depend on the combination of multiple biochemical pathways.

Strength

By leveraging a previously published large dataset of yeast colony sizes for single- and double-knockout mutants, this study validated the relevance of the product function, which has frequently been used in genetics to analyze epistatic interactions. The confirmation that the product function provides a more reliable prediction of double-mutant fitness compared to other neutral functions is valuable for researchers analyzing epistatic interactions, particularly those working with the same dataset.

Notably, this dataset has been previously used in studies exploring epistatic interactions with the product neutrality function. This study's findings affirm the validity of using the product function, which could enhance confidence in the conclusions drawn by those earlier studies. Consequently, both researchers utilizing this dataset and readers of prior research will benefit from the confirmation provided by this study.

Weakness

This study contains several serious problems, primarily stemming from the following issues: ignoring the substantial differences in the mechanisms regulating cell growth between prokaryotes and eukaryotes and adopting an overly specific and unrealistic set of assumptions in the mutation model. Below, the details are discussed.

(1) Misapplication of prokaryotic growth models

The mechanistic origin of the multiplicative model observed in yeast colony fitness is explained using a bacterial cell growth model. However, there is no valid justification for linking these two systems. The bacterial growth model, the Scott-Hwa model, heavily rely on specific molecular mechanisms, such as ppGpp-mediated regulation, which adjusts ribosome expression and activity during translation. In particular, this mechanism is critical to ensure growth-dependency of the fraction of ribosome in proteome in the Scott-Hwa model [https://doi.org/10.1111/j.1462-2920.2010.02357.x; https://doi.org/10.1073/pnas.2201585119]. Yeast cells lack this regulatory mechanism, making it inappropriate to directly apply bacterial growth models to yeast.

The Weiße model is based on a larger set of underlying equations and involves more parameters than the Scott-Hwa model. In the original paper by Weiße et al. (PNAS, 2015), however, the model parameters were fitted solely to experimental data from E. coli, and the model's applicability to yeast was never assessed. In summary, for neither the Scott-Hwa model nor the Weiße model has it been demonstrated that the entire model quantitatively fits experimental data from yeast. A positive correlation between growth rate and RNA/protein ratio, often observed in yeast, supports only a limited portion of either model, and does not constitute validation of the models as a whole.

(2) Overly specific assumptions in the theoretical model

The theoretical model assumes that two mutations affect only independent parameters of specific biochemical processes. However, this overly restrictive assumption weakens the model's validity in explaining the general occurrence of the multiplicative model in mutations. Furthermore, experimental evidence suggests limitations of this approach. For example, in most viable yeast deletion mutants with reduced growth rates, the expression of ribosomal proteins remained largely unchanged, contrary to the predictions of the Scott-Hwa model [https://doi.org/10.7554/eLife.28034]. This discrepancy highlights that the Scott-Hwa model and its derivatives cannot reliably explain mutants' growth rates based on current experimental evidence.

(3) Limited reliability of the mechanistic origin of the multiplicative model

The authors seem to regard growth-optimizing feedback as the mechanistic origin of the multiplicative model. However, the importance of growth-optimizing feedback in explaining product neutrality heavily depends on the very specific framework of the Scott-Hwa model. As I pointed out above, the Scott-Hwa model is a bacterial growth model that considers only a narrowly defined set of biochemical reactions. Using such a narrow model to explore the mechanistic origin of product neutrality observed on a genome-wide scale appears to be inappropriate. Arguments based on either the Scott-Hwa model or the Weiße model fail to account for the generality of product neutrality across diverse genetic perturbations. These models, in their current form, do not explain the broader patterns of product neutrality observed experimentally.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105265.3.sa2](https://doi.org/10.7554/eLife.105265.3.sa2)

The paper deals with the important question of gene epistasis, focusing on asking what is the correct null model for which we should declare no epistasis.

In the first part, they use the Synthetic Genetic Array dataset to claim that the effects of a double mutation on growth rate is well predicted by the product of the individual effects (much more than e.g. the additive model). The second (main) part shows this is also the prediction of two simple, coarse-grained models for cell growth.

I find the topic interesting, the paper well written, and the approach innovative.

Comments on revisions:

The authors have adequately addressed the comments raised in the review below, and I find that the paper has improved.

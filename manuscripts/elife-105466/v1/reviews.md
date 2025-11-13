# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105466.3.sa0](https://doi.org/10.7554/eLife.105466.3.sa0)

In this important quantitative study of HIV-1 evolution in humans and rhesus macaques, selection coefficients are inferred at scale over the HIV genome. Selection coefficients are similar in humans and macaques, providing compelling evidence that these coefficients are representative of the fitness landscapes of these viruses within hosts. This work will be of interest to the community working on quantitative evolution and fitness landscape inference, and the finding that rapid fitness gains in the HIV population predict bNAb emergence has significant implications for HIV vaccine design.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105466.3.sa1](https://doi.org/10.7554/eLife.105466.3.sa1)

Summary:

The present work studies the coevolution of HIV-1 and the immune response in clinical patient data. Using the Marginal Path Likelihood (MPL) framework, they infer selection coefficients for HIV mutations from time-series data of virus sequences as they evolve in a given patient.

Strengths:

The authors analyze data from two human patients, consisting of HIV population sequence samples at various points in time during the infection. They inferred selection coefficients from the observed changes in sequence abundance using MPL. Most beneficial mutations appear in viral envelop proteins. The authors also analyze SHIV samples in rhesus macaques, and find selection coefficients that are compatible with those found in the corresponding human samples.

The manuscript is well written and organized.

Comments on revisions:

In their revised version the authors have addressed most of these points satisfactorily.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105466.3.sa2](https://doi.org/10.7554/eLife.105466.3.sa2)

This paper combines a biological topic of interest with the demonstration of important theoretical/methodological advances. Fitness inference is the foundation of the quantitative analysis of adapting systems. It is a hard and important problem and this paper highlights a compelling approach (MPL) first presented in (1) and refined in (2), roughly summarized in equation 3.

The authors find that positive selection shapes the variable regions of env in shared patterns across two patient donors. The patterns of positive selection are interesting in and of themselves, they confirm the intuition that hyper-variation in env is the result of immune evasion rather than a broadly neutral landscape (flatness). They show that the immune evasion patterns due to CD8 T and naive B-cell selection are shared across patients. Furthermore, they suggest that a particular evolutionary history (larger flux to high fitness states) is associated with bNAb emergence. Mimicking this evolutionary pattern in vaccine design may help us elicit bNAbs in patients in the future.

The fitness landscape of env in multiple hosts is immensely valuable especially because of how often SHIV has used as proxy for HIV. The strength of reversion-to-consensus selection is a known pattern of HIV post-infection populations but they are nicely quantified here. Agreement between SHIV and HIV evolution is shown. They find selection is larger for autologous antibodies than the bNAbs themselves (perhaps bNAbs are just too small a component of the host response to drive the bulk of selection?), and that big fitness increases precede antibody breadth in rhesus-macaques, suggesting that this fitness increase is the immune challenge required to draw forth a bNAb. All of high interest to HIV researchers.

(1) Sohail, M. S., Louie, R. H., McKay, M. R. & Barton, J. P. Mpl resolves genetic linkage in fitness inference from complex evolutionary histories. Nature biotechnology 39, 472-479 (2021).

(2) Shimagaki, K. & Barton, J. P. Bézier interpolation improves the inference of dynamical models from data. Physical Review E 107, 024116 (2023).

Strength of evidence:

Equation 3 is a beautiful and intuitive tool that accounts for linkage and can be solved precisely even in the presence of detailed mutational and selection models. They have addressed my earlier concerns the effects of incomplete observations of the frequency bias fitness inference on rare sites.

Whether the fact that fitness increases occured before or after the presence of the bnab remains incompletely known. bNAb detection is different from bNAb presence and the possibility that fitness increases occurred after the bNAbs appeared remains. Still, their conclusion is plausible and fits in with the other observations which form a coherent and compelling picture.

Overall this is a convincing paper. It is a valuable introduction to a practical method of fitness inference at the scale of the entire env gene and how this information can be leveraged to learn some interesting biology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105466.3.sa3](https://doi.org/10.7554/eLife.105466.3.sa3)

Summary:

Shimagaki et al. investigate the virus-antibody coevolutionary processes that drive the development of broadly neutralizing antibodies (bnAbs). The study's primary goal is to characterize the evolutionary dynamics of HIV-1 within hosts that accompany the emergence of bnAbs, with a particular focus on inferring the landscape of selective pressures shaping viral evolution. To assess the generality of these evolutionary patterns, the study extends its analysis to rhesus macaques (RMs) infected with simian-human immunodeficiency viruses (SHIV) incorporating HIV-1 Env proteins derived from two human individuals.

Strengths:

A key strength of the study is its rigorous assessment of the similarity in evolutionary trajectories between humans and macaques. This cross-species comparison is particularly compelling, as it quantitatively establishes a shared pattern of viral evolution using a sophisticated inference method. The finding that similar selective pressures operate in both species adds robustness to the study's conclusions and suggests broader biological relevance. In the revised version, the Authors included a simple but clear explanation of the statistical method for inferring the model's parameters in the main text. Moreover, I find the potential implications of the methodology absent in the original submission very interesting.

Conclusions:

Overall, the study presents a compelling analysis of HIV-1 evolution and its parallels in SHIV-infected macaques.

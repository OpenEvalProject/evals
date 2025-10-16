# Peer review - Round 1

Editors:
- Jie Xiao, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73395.sa0](https://doi.org/10.7554/eLife.73395.sa0)

The work by Kim et al., used synthetic constructs in Drosophila to examine the relationship between regulators and transcription initiation. By measuring regulator concentrations and the corresponding RNA polymerase initiation rates in different synthetic constructs and using a thermodynamic model, the authors concluded that higher-order cooperativities between the repressor on adjacent binding sites, and that between the repressor and RNA polymerase are needed to explain the observed response curves in RNA polymerase loading rate. This work targets a challenging question in eukaryotic transcription regulation, where higher-order cooperativity between different molecular components, in addition to simple transcription factor binding and unbinding, is often necessary to account for observed promoter behaviors when multiple elements (repressors, mediators, activators) exist.


---

# Peer review - Round 1

Editors:
- Jie Xiao, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73395.sa1](https://doi.org/10.7554/eLife.73395.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Predictive modeling reveals that higher-order cooperativity drives transcriptional repression in a synthetic developmental enhancer" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. While the work is potentially important, the uniqueness of the model and experimental verification of model predictions need to be further justified.

The essential revisions are:

1. Modeling: Please provide a better articulation/construction of the model regarding the fitting parameters (which to keep constant and which to vary, the number of parameters to use, error bars in the experimental data), whether an alternative model should be considered, whether the provided model can indeed account quantitatively observed data (not just to demonstrate that previous models do not work), and whether statistically the model fits experimental data adequately (not by overfitting, examine using Akaike Information Criterion AIC or Bayesian Information Criterion BIC). See reviewers #1 pt 1, #2 pt 1-5, and #3's overall review, and pt1.

2. Experiments: please provide experimental measurement for a few conditions where the outcome of transcription regulation by Runt is measured by smFISH or protein concentrations to demonstrate that the measured promoter activity using RNAP loading rate is equivalent or better (without complications in mRNA/protein degradation).

Reviewer #1 (Recommendations for the authors):

1. Modeling: I would like to see a better articulation of what the alternative is to a 'thermodynamic model.' I understand the authors meaning to be equilibrium models arrived at through partition functions. But kinetic models based on detailed balance are also thermodynamic. I don't want to get twisted around in the language, but the over-emphasis on the ideological purity of thermodynamics was distracting and seems to refer to an ongoing dialog / conversation which is likely lost on the general reader.

a. One example is when they assume that the Runt dissociation constant remains unchanged with different positions (Kr) because the sequence is the same. The problem stems from their previous section where they found that there was an unsuspected relationship between the position of the Runt Binding sites and the parameter "p=[RNAP]/Kp" --- the point being that the sequence is the same in each construct, and therefore, based on their model Kp is changing. So why is it preferrable to assume that Kr is constant with position, but Kp changes?

b. Expanding on the previous point, they then proceed to state that an unchanging Kr is supported by the fact that by only varying the wrp they were able to fit their data. Considering the similar role of Kr with wrp within the equation, I wonder if one could reach the same result varying the Kr and holding wrp constant? Furthermore, who's to say that both don't vary between the constructs? Could the authors address this concern by varying Kr and further discussing this possibility and what it means for the interpretations of the model? In summary, the authors have a model which explains their data. Great. I'm not sure this agreement can be used as an argument for the propriety of the 'thermodynamic approach.'

2. A simple plot showing mRNA/cell as a function of repressor concentration for the different configurations in Figure 6 would be much appreciated. Perhaps I missed the inference, but the ultimate goal of an input/output understanding is to map concentration of a regulator to expression level of the target gene.

Reviewer #2 (Recommendations for the authors):

The manuscript has several issues as noted below.

1) For MCMC fitting of experimental data, the absolute error or relative error of all the results should be given. One would like to know the confidence degree of the fitting results.

2) Formula (5) in the main text is used to fit the data, and the results are shown in figure6. However, the number of the parameters in the fitting formula is almost the same as the amount of the experimental data, and the formula is too complicated. The corresponding parameter space is quite large. Therefore, it is necessary to further analyze the accuracy of the fitting and the necessity of adding the cooperativity.

3) What is source of error bar of the initial RNAP loading rate? Need to give detailed explanation. If the source of error bar is from the data of multiple traces, why not fit multiple trajectories separately?

4) The fitting equations (1), (2) and (5), are all the fitting function for the experimental data. Are the parameter b, p and r the fitting parameters? If they are the fitting parameters, the fitting result needs to be given. These parameters are related to the weights of different binding states in your model, which need to be listed in detail, and compared the differences of fitting results under variant conditions.

5) In this paper, a variety of data is shown, which are Runt binding to different sites such as [001][010],[011] and so on. Please elaborate on how Runt is experimentally controlled or determined to bind to the specified sites.

6) The fluorescence of nucleus and cytoplasm is quantitatively analyzed, how to distinguish nucleus and cytoplasm? Please give the process and corresponding results.

7) It is shown in Fiugre6b that if the cooperativity is not included, a good fitting result cannot be obtained. Has the fitting covered a large enough parameter space search? The fitting results in figure 6 are quite different from the experiment results regardless of the cooperativity. If so, does it mean that the cooperativity plays a major role in the fitting, or even that the individual interaction between Runt and binding sites can be ignored? Could you separate out the part of cooperativity in the fitting results so as to confirm that the cooperativity plays a key role in the experiment?

Reviewer #3 (Recommendations for the authors):

1) Results of Figure 5 should be accompanied by reports of fitting alternative models and suitable model comparisons performed. Also, a baseline model with constant KR and \omegaRP (same for all three constructs) should be evaluated and compared to. Such comparison should ideally involve model comparison techniques such as likelihood ratio and AIC/BIC.

2) Results of Figure 6 should be accompanied by statistical assessment of improvements due to higher-order cooperativity parameters.

3) The fact that fitting of more complex models typically relied on setting different values for the additional parameters for each construct (rather than the same values for all tested constructs of that category) should be examined more closely. How well can the data be modeled without this flexibility?

4) The authors should address the concern that alternative model structures different from that used in the thermodynamics-based models here might have explained the data without requiring higher-order cooperativity.

Other suggestions:

One of the first experimental tests reported is that of predicted expression profile in the hunchback promoter with one Runt binding site. Figure 3J is supposed to be a qualitative match to the predictions in Figure 3F. Could the authors elaborate on what reasonable regimes of the model parameters would provide predictions that do not qualitatively match the observation? It seems like with an activator (Bicoid) progressively decreasing and a repressor (Runt) progressively increasing from anterior to posterior, the enhancer expression will obviously decrease in some form. Perhaps the authors might wish to make it clear that their goal here was to establish some basic parameter estimates to be used in the remaining analyses, and perhaps also to assess the uncertainties associated with those model parameters.

The results presented in Figure 4 are puzzling. Figure 4D suggests that the differences among the constructs arises purely from differences in the p and R parameters, and not from the bicoid or bicoid-RNAP related parameters. Could the authors add a possible mechanistic speculation here regarding how making changes solely in the enhancer sequence might result in biochemical changes solely in the behavior of RNAP at the promoter (without any change in the protein-DNA interactions at the enhancer itself)?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Predictive modeling reveals that higher-order cooperativity drives transcriptional repression in a synthetic developmental enhancer" for further consideration by eLife. Your revised article has been evaluated by Naama Barkai (Senior Editor) and a Reviewing Editor.

The manuscript has been significantly improved but please further address one issue on the validation of transcription rate measurement, the reviewers asked to use an orthogonal method such as smFISH to validate the measurement using MS2, which was not done in the revision. Please provide at least a thorough comparison and contrast of the current method with other orthogonal methods in the Discussion to equip readers with a full context of the quantifications that are central to the work.

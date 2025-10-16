# Peer review - Round 1

Editors:
- Tatyana O Sharpee, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61942.sa1](https://doi.org/10.7554/eLife.61942.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The relationship between evoked and spontaneous activity in neural development is an important unresolved issue and this study adds a new and interesting perspective to the existing literature. The results demonstrate that as the zebrafish develop, the spontaneous and evoked activity in the optic tectum become more dissimilar.

Decision letter after peer review:

Thank you for submitting your article "Spontaneous and evoked activity patterns diverge over development" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Emre Yaksi (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This manuscript investigates the relationship between spontaneous activity and evoked activity patterns in zebrafish tectum across development. The authors show that the correlation between spontaneous and evoked activity is getting weaker as animals develop. This is contrast to some of the recent findings and provide an important observation for the field. The presented data and its analysis is of high quality, and the manuscript is particularly well written an easy to read. Some of the analysis and the figures can be further improved for making the manuscript easier to read for a general audience. Reviewers also pointed out a number of methodological and statistical clarifications that need to be made as described below.

Essential revisions:

1. The part explaining the method used in figure 3 E-G should be expanded to ensure the readers can replicate the method. Specifically, it is unclear how many dimensions are necessary to describe the hyperplane H. How many basis vectors were used for the projection? Using many dimensions for the projections could bias the results towards larger angles between patterns and the hyperplane. The authors refer to [23] as the basis of their method. However, the method used in [23] is different from the method described here and puts an emphasis on finding shared dimensions between spontaneous and evoked activity subspaces.

2. The effect in figure 3E, F is weak and the data do not fully support the conclusion. Specifically, there seems to be no significant difference between 4dpf and 15dpf in 3E. It is unclear, whether correction for multiple comparisons was used. An alternative presentation would be a matrix wise representation of p-values between all pairs of days.

3. The reported number of components required to explain 80% of the variance for EA (Figure 3C) is high (and increases with age?) compared to the number of stimuli and assemblies found (2C). How can it be reconciled that the number of assemblies is roughly 6, while the number of PC required to explain 80% of the variance is about 40? Also, there is a possible concern here that this number shows a positive bias due to the inclusion of components representing noise. If this high number of components is used to describe the hyperplanes in Figure 3E-G, a concern for bias arises.

4. In Figure 1F, despite a visible trend, the authors report no significant change in the Hamming distance of binarized correlation matrices for SA and TEA. However, it is unclear whether a Hamming distance is the most appropriate measure here (as opposed to e.g. second-order correlation between correlation matrices).

5. Visual system develops earlier than other sensory systems in zebrafish. Therefore, it is likely that major rearrangements to be observed during early development are already established at 4dpf animals. Are there evidence that such features of spontaneous and evoked activity are different in younger animals (2,5dpf) that are just hatched? It is likely that this 2,5dpf represents a stage closer to earlier developmental stage of mammalian visual system.

6. SA and TEA seem to have very different spatial distribution (SA covering larger spaces). If this is true this is rather interesting feature, as evoked activity might change such spatial features of ensembles. Can this be something interesting to analyze, is this a general feature that is stable across development?

7. Is it possible that the evoked patterns appear to get more dissimilar to spontaneous patterns on average, because the spontaneous patterns become noisier over development, as new neurons are added to the network? Is there a way to evaluate the impact of changing noise levels (both recording noise, but also neural noise) in these comparisons?

8. Also is it possible that simply by imaging only a short period of time, spontaneous activity patterns do not really capture all possible combinations of ensembles, whereas as of now the evoked activity recordings are substantially longer then spontaneous activity recordings. How much the recording duration influence such comparisons ensembles during evoked and spontaneous period. To what extent the numbers of captured ensembles depends on the recording duration ?

9. I am surprised that the authors did not discuss some of their results in the context of the findings from a recent paper on the spontaneous and evoked activity in developing zebrafish habenula (doi: https://doi.org/10.1126/sciadv.aaz3173 ), which is another brain region that exhibit both spontaneous and sensory driven activity (DOI: 10.1016/j.cub.2014.01.015 ). In this study the authors showed that at the animals develop spontaneous activity changes with higher correlations between neurons and altered temporal features. Interestingly this study also shows that the spontaneous activity is a good predictor of sensory responses of neurons, and this gets better over development, which in line with the hypothesis that the spontaneous activity might indeed be a prior to evoked responses, at least for some brain regions. I think that authors should at least consider comparing their results and discuss this relationship with these earlier works in zebrafish habenula, in addition to their description of ferret visual cortex work.

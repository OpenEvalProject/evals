# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77373.sa0](https://doi.org/10.7554/eLife.77373.sa0)

The authors introduce a machine learning based classifier for M1 and M2 polarised macrophages based on autofluorescence lifetime parameters excited by two-photon excitation in the NAD(P)H emission band following during uncoupling of oxidative phosphorylation. They have identified a promising direction for use of metabolic imaging for macrophage classification.


---

# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77373.sa1](https://doi.org/10.7554/eLife.77373.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Non-Invasive classification of macrophage polarisation by 2P-FLIM and machine learning" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Michael L Dustin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Sergi Padilla-Parra (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please, produce more data utilising the Phasor plot.

2) Produce 2D graphs clearly showing the number of photons (per pixel) vs lifetime.

3) Show all pictures of your cells with the different parameters.

4) If photons are limited leading to artifacts, increase the resolution of all your images (utilise a higher magnification/higher NA objective) and collect more photons per cell.

5) Figure 2 – Please indicate n number. Is this data from all 6 donors?

6) Figure 3 – In D, E and F, please indicate what each bar or point represents. Is this single-cell, an imaging field or200 cells? Please indicate for each panel.

7) The authors should make clear if the ROC AUC value of 0.944 is for single cells or a population? If not signal cell, how many cells are needed to reach this level?

8) The authors cite Kröger et al.'s 2021 preprint that uses lifetime parameters to classify human macrophages in vivo. Are the results here consistent with this kind of accuracy without the application of metabolic inhibitors? In this case, does in vivo environment likely serve as a discriminative condition that might separate the cells by FLIM better than the excess of oxygen in the in vitro setting?

9) The study could be strengthened further by looking at the phenotypic markers of polarisation at the single-cell level, for example, by immunofluorescence in a manner that could be correlated with the FLIM measurements. This might reveal how much the accuracy of the methods is related to some failure of macrophages to polarise in a population, rather than a true error in classification. This could be discussed as a future effort.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting the paper entitled "Non-Invasive classification of macrophage polarisation by 2P-FLIM and machine learning" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor. We are sorry to say that we have decided that this submission will not be considered further for publication by eLife.

While the revisions were appreciated, they reinforced concerns about S/N. Your response related to importance of machine learning the classification led to a deeper analysis of this machine learning approach, which also suggests several weaknesses. We hope both sets of comments will be helpful in going forward with development of a robust approach to this important and interesting problem.

Reviewer #1 (Recommendations for the authors):

Comments on machine learning approach-

Doing large grid sweeps when cross-validating is not exactly best practice as you will be optimising for performance on the test set. Data should instead be split into train-test-val: grid sweeps should be evaluated on the test set, but final performance should be evaluated on a validation set. Otherwise, these parameters may have been overfitted to test set and may not generalise to other validation sets.

line 110 – t-SNE cannot be used for dimension reduction as it doesn’t learn a function that can be re-applied.

Given there only appear to be 6 variables used, PCA will likely be useful and faster than UMAP, and the principal components will be highly interpretable. The main utility of UMAP over PCA is that it is a non-linear transformation. PCA should still be explored to see what features make up the principal components.

139 – ROC-AUC is a bit subjective based on the number of cases: true positive, false positive, true negative and false negative should be reported too.

In figure 3: is 3F a reapplication of the UMAP learned in E, or is it a new UMAP?

Figure 4B does not at all look convincing: the M1 and M2 groups do not appear to be separated. Furthermore, was the UMAP used in this figure re-trained on this patient's data, or was it pre-trained on a different dataset? It is not clear.

There's a lot going on in figure 4: Was a new model trained for each patient, or was each patient tested on the same model? In either case, A variability of 0.937 ROC-AUC to 0.650 ROC-AUC, does not suggest that this classification model is robust.

Perhaps most importantly, It is not apparent where this score of 0.944 comes from – is this the max of cross-validation or the mean? is it on a dataset that collates all the data, or only on a subset? In particular, there is no link to the findings shown in figure 4.

This could be extended by doing ‘cross-validation’ when one of the patients is held out each time and generalisation performance is evaluated on the held-out patient.

Line 235: 'it is noticeable that single-cell classification performance is affected by donor variability during the FCCP 236 treatment' – this should be emphasised in the abstract – it is a weakness of the paper.

In Table 1 it looks like mtry and ntree are the wrong way around – having only 2-5 trees in a random forest is in no way stable, and given there are 6 features, mtry can not be more than 6 (instead of the reported range of 100 to 300).

If the researchers are doing cross-validation they should report the mean and standard deviation/S.E. for their ROC-AUC scores along with their TP/TN/FP/FN. It's not apparent if they've picked the highest ROC-AUC score they got in the cross-validations or the mean

their analysis of feature importance is fairly ad-hoc: a method like SHAP should be explored.

It appears that in the fluorescence some features are combinations of other features.

Line 486: if SVMs and logistic regressions have been done these must be reported along with their confidence intervals. Logistic regressions will also be highly interpretable. It does not appear cross-validation has been done on this data, however.

Reviewer #2 (Recommendations for the authors):

The authors have performed a number of analysis to try to respond to my questions. They have produced the Phasor plot for some of the data and have also presented pixel by pixel images and the photon histograms which is really valuable to understand how reliable is the data.

I have to say that after examining these data I am not convinced that the signal to noise and the limited photon collections is not affecting the results:

Figure 3 supplement 1 all figures are the same!!! There is no difference in pixel by pixel values for all conditions! The same can be seen in Figure 3 supplement 2. All figures regardless treatment conditions look the same to me. In the case of the phasor plot the differences might come from S/N as the shift in the plot is minimal and might be equivalent to your error (a few ps). In Figure 3 Supplement 4, the average lifetime clearly shows that for lower number of photons you have a shift in the lifetime which suggests that your changes in lifetime are affected by your poor signal. If you are considering the average lifetime as the mean value from a double exponential, still this shows that your calculations are affected by poor photon collection. You might consider non-fitting approach at all (for instance photon arrival time) and the number of photons would still be important. This would be better shown in a graph in which you do not bin the average lifetimes to a particular lifetime value (histograms) but instead you plot directly each photon value versus its corresponding lifetime value (dispersion plot). If you do this pixel by pixel instead of averaging your results per cell you will get a bid distribution of lifetimes that are pretty much affected by poor photon collection and you will have to determine which is the minimal amount of photons that gives a reliable lifetime.

I am sorry to say that this vision is strengthened when examining the pixel by pixel images provided with different treatments. No differences at all can be seen when taking a look at the different treatments (i.e. Olygomycin, FCCP…). Even when comparing IL-4-M2 macrophages vs IFNγ-M1 macrophages I could not see any significant difference.

Overall, I do appreciate the effort in producing all these data and I understand that there might be some differences in lifetimes that are quantified. However, the impact of the S/N and the difficulties to deconvolve background noise from real signal as shown in the histograms and also the images puts in doubt the main hypothesis of the paper.

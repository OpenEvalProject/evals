# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72819.sa0](https://doi.org/10.7554/eLife.72819.sa0)

The authors have used measurements of endogenous fluorescence lifetimes in the two-photon stimulated NAD(P)H excitation-emission range to build an in vivo classifying for macrophage differentiation status in human dermis. The training data was derived from in vitro and ex vivo analysis of M1 and M2 polarised macrophages from peripheral blood, isolated from tissue or studies ex vivo in frozen sections with marker based validation. A machine learning approach for in vivo classification is presented and an approach to detect phagocytes in vivo is suggested.


---

# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72819.sa1](https://doi.org/10.7554/eLife.72819.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Label-free imaging of macrophage phenotypes and phagocytic activity in the human dermis in vivo using two-photon excited FLIM" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Michael L Dustin as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

There are a number of positive aspects of your study including:

Using optical methods to non-invasively detect cells has significant interest for clinical and basic studies, and the impact of this study is considered high.

Identification of different FLIM signatures for macrophages polarized towards different phenotypes in vitro, and were able to compare these signatures to those of other cell types and macrophages in the skin.

They identified a few cells in the skin that expressed markers associated with macrophage polarization, and also exhibited the FLIM signatures that were established from the in vitro polarization studies.

At the same time, there are limitations of the study that can be addressed through the following Essential Revisions:

1) The description of M1 and M2 macrophages in the skin (in the introduction) is overly simplistic and the use of single markers (in Figure 3) to establish correlations is also simplistic. This should be updated and mixed phenotypes acknowledged.

2) It would be very useful to see how the classification tree fails ~10% of the time in relation to the plots in Figure S5. It's striking that the FLIM parameters generate a near perfect classification of M1 and M2 so it almost seems that adding information like cell shape may make it less accurate. Can the authors indicate in S5 which cells were mis-identified by the decision tree and if the reason is clear? If the FLIM parameters alone are fully discriminative it's not clear why the other parameters are helpful. Is there an "F-test" that can be done to assess the statistical value of each parameter that is added to the tree and if the improvement is greater then just adding another degree of freedom. Eventually this seems destined for some kind of experimental medicine application and this information would help determine where we are in terms of feasibility toward these near term goals. It would be important to report the number of in vivo tomograms that were done for each subject, the volume analyzed and amount of time to collect the tomograms.

3) Additional phenotype markers and evaluation of many more cells seems required to test the classifier. It's possible that the current 90% reliability is not actually statistically significant due to the low numbers. There are some significant technical concerns given that macrophages are a highly heterogeneous population of cells, particularly in vivo during an activation event such as injury. The few cells analyzed in Figure 3 are not sufficient given the heterogeneity of macrophages in vivo. Mixed phenotypes are common in vivo, and it is unclear how the FLIM signatures would change in response to such mixed signatures.

4) Visualizing a single phagocytosing cell in Figure 5 is also not sufficient to conclude that the method is capable of detecting phagocytosis events. Experiments in vitro treating macrophages with phagocytic targets need to be performed. An experiment in vivo would also strengthen the study, where phagocytic targets are applied to a skin wound. Controls without targets should be examined, along with quantitation across many cells. You may wish to focus on the classification task and perhaps only bring up phagocytosis as a possible confounder in this class-action process, but demonstrating the ability to detect phagocytosis in vivo may be another paper.

5) Is the lifetime signature stable over time? Can a single cell be imaged over time. This seems possible as macrophages are generally sessile. The study would be strengthened with further analysis that correlates FLIM signatures with metabolic state (free vs. bound NADPH). Could the lifetime relate to metabolic cycles in the issues that could change with time? This is a fundamental question that should be addressed in a first paper on this topic.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Label-free imaging of M1 and M2 macrophage phenotypes in the human dermis in vivo using two-photon excited FLIM" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

This is a very interesting study that uses a label free method to classify macrophages in human dermis using two photon imaging. Additional data analysis and reporting is requested to fully document the very important work.

1. Justify your fitting model and include the decays pixel by pixel and also the fit profiles together with the goodness of the fit for all cases.

2. Compare with the Phasor plot, all your data.

3. Present all images with the corresponding number of photons acquired per pixel and plot these versus your mean lifetimes.

4. Calculate the true mean lifetime according to the canonical formula.

5. Present all your data in a pixel by pixel format.

Reviewer #1 (Recommendations for the authors):

Thank you for your clear response to the reviewer's concerns. You have addressed the issue of mixed phenotypes in healthy skin and your in vitro analysis of both in vitro differentiated and freshly isolated M1 and M2 like cells from skin show consistent two photon film signatures. You have provided information about the time involved in the measurements for each subject, the volume scanned and the number of cells found. You have also addressed the temporal stability in vivo consistent with the observation that the isolate cells maintain the flim phenotype even after isolation. The reporting on phagocytosis is now qualified and the limitations of the study are now appropriately acknowledged. I have no further recommendations.

Reviewer #3 (Recommendations for the authors):

In general the approach and validation of the technique is appropriate. I would be interested though to check the relative number of photons collected per pixel versus the different lifetimes to make sure that all lifetimes collected and analyzed are independent on the intensity/number of photons.

Also, some of the lifetimes recovered were very short and close to the resolution of the instrument response function (IRF); which by the way seems not to be recovered experimentally but rather produced by the SPCI software. Please, clarify and also if it was not recovered experimentally produce these data.

This brings me to my next point. The authors employ a double exponential approach and present both the average lifetime (calculated based on tau1 and tau2 and not with the appropriate formula, see Padilla-Parra et al., 2008 Biophys J). The authors do not show the fluorescence decays for each cell, together with the double exponential fits nor the goodness of these fits or the Χ2 (chi square). This data is fundamental to understanding if all FLIM data recovered can be fitted to the double exponential model. Also, the authors assume a double exponential approach but they do not justify their choice. Which are the two populations you are assuming to co-exist in the cells/dermis? Are you always measuring NADPH/NADP? In this case, have you shown the value of these two lifetimes in vitro, and then you should fix these two lifetimes and recover different proportions, right? The model to fit your data should be discussed and justified. I assume that if you use a triple exponential most of your stats will be better. Please discuss this also in the context of the number of photons.

Also, all the parameters recovered from the fit should be also shown pixel by pixel so that we can understand how these data vary as a function of the number of photons, or the error (Chi Square).

In Figure 4 the authors decide to show the phasor plot (Digman et al., 2008 Biophys J). This is a nice approach that does not necessitate the assumption of a model. You should present all data comparing this approach and the fitting approach utilizing a double exponential and also discuss how your data varies depending on the number of photons. It is possible that some lifetime distributions arise from the fact that in some cells the high intensity values give longer lifetimes and in others where there is a lower signal to noise, lower lifetimes are observed. When plotting your lifetimes versus the number of photons pixel by pixel no dependence should be observed. This will help to validate your data.

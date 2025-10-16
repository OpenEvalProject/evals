# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/012pb6c26 National Heart, Lung and Blood Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82593.sa0](https://doi.org/10.7554/eLife.82593.sa0)

This is a valuable study of broad potential impact in structural biology, which will interest readers in various fields, including molecular biomedicine, molecular evolution, and protein engineering.


---

# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/012pb6c26 National Heart, Lung and Blood Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82593.sa1](https://doi.org/10.7554/eLife.82593.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Rapid protein stability prediction using deep learning representations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. Two of the reviewers agreed to reveal their identity, namely Nir Ben-Tal (Reviewer #1) and Julian Echave (Reviewer #2).

As you will see below, the reviewers conclude the manuscript is not suitable for publication for eLife in its current form, but they make specific recommendations to resolve their concerns. I recognize some of these revisions are substantial and will require considerable effort – nevertheless, I encourage you to take the time required to address these concerns convincingly, and then submit a revised version.

Reviewer #1 (Recommendations for the authors):

(1) Authors should compare the results to existing alternatives. For example, here is a recent method, also based on deep learning: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008291. And there are many studies using 'simple' machine learning methods. The prediction quality here is similar to what these "shallow learning" methods give, albeit on other datasets, so perhaps irrelevant comparison. Anyway, all these methods show prediction quality that is very close to the natural upper bound given how noisy the data is (PMID: 30329016; a paper that I co-authored). So it is not clear whether the deep learning helped at all.

(2) Why was ROSETTA used as gold standard? Clearly ROSETTA is very far from perfect. In fact it's not even clear that it outperforms FoldX.

(3) Estimating ddG based on model structures: Now that AlphaFold models are available essentially to all proteins, it is possible to do much more than only 3 proteins. The authors should take advantage of this and examine the dependence of the ddG prediction quality on model RMSD to experimental structure, and more importantly, the dependence on AlphaFold's estimated model accuracy.

(4) Figure 4A. Both disease-causing and benign mutations appear to destabilize proteins. Authors claim that, on average, disease-causing mutations are more destabilizing. The calculated ddG values ~0.5 vs. ~1.4 kcal/mol are not that different. Is the difference really significant? More importantly, that the benign mutations appear to be destabilizing suggests that there might be systematic error towards destabilization. Could the authors test that? Do experimental ddG data show a similar behavior?

Reviewer #2 (Recommendations for the authors):

## Suggestions for improved or additional experiments data or analyses

1. More thorough assessment of accuracy against experiment, as compared not only with Rosetta, but also with other current methods. I think this work is much more likely to have an impact if a more thorough assessment of RaSP is made. In particular, I suggest that RaSP is more thoroughly tested against experimental mutational stability changes. In addition, to help position RaSP in the landscape of current methods, I suggest the RaSP-vs-experiment performance is compared not only to Rosetta, but also to other current methods. Such extra work does not necessarily mean that other methods need to be run. For instance, running RaSP on the same datasets used by recent assessments it would probably be possible to compare RaSP with other methods by getting the accuracy of other methods from the literature (see e.g. [https://doi.org/10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555) for a recent thorough comparison of several methods).

2. Assess whether the method satisfies the antisymmetry condition. I think it would be important to complement Pearson's correlation and MAE with other measures of accuracy. Of particular importance is how well RaSP satisfies the thermodynamic condition that the reverse stability change satisfies ΔΔG(B->A) = – ΔΔG(A->B). Violation of this condition is a well-known issue with most ΔΔG-prediction methods (and experimental values!) and it would be very interesting to know whether RaSP suffers from this problem.

3. Compare the accuracy of the method for different sites. In the paper, there is an interesting analysis of the relative performance of RaSP for different types of amino-acid substitution. Another issue the authors might want to consider is how performance depends on whether sites are buried or exposed.

4. Compare the speed of the method to that of other methods. A strength of this work is that it presents a rapid method. From the present manuscript, it is clear that it is much more rapid than Rosetta. However, it is not clear how the speed of RaSP compares with other currently available methods. If the authors could perform such a comparison, at least for a limited dataset of proteins, I think this may go a long way towards making this work more influential.

## Recommendations for improving the writing and presentation

In general, I think the paper is very well written. However, some of what I perceived to be weaknesses could probably be dealt with by revising the manuscript.

When considering these recommendations, please take into account that my take on this work is that it is about a new rapid and accurate ΔΔG-prediction method. Therefore, I think everything in the manuscript should serve the purpose of bolstering this point. For instance, from this perspective, the calculations performed on the dataset of human proteins should be included only because it serves the purpose of demonstrating the usefulness of this approach, not because the obtained results are interesting in themselves. Therefore, I make a few recommendations that tend toward giving less weight to this application and more weight to the method and its assessment.

1. Make the application to the human dataset more clearly support the main point: the method. I think what's interesting about the large-scale application is not that common variants tend to be more stable, rare and/or disease variants unstable, etc, which we already know (you and others have demonstrated this already in previous work), but that it can be done by RaSP in a very short time because RaSP is fast. Also, the fact that it confirms previous findings shows that its accuracy is enough to draw these important conclusions. I think this is pretty clear from the paper. However, it can be made even more clear. For instance, almost half the abstract talks about the conclusions of the application, rather than the method itself. Also, it is not perfectly clear, from the Abstract, whether the method was developed as a mere tool to perform these calculations, or the calculations were performed to further assess and illustrate the method's usefulness. I think some minor carefully thought-out revisions in the abstract, results, and Discussion sections may make the method more of a protagonist and give the application, in the present paper, a supporting role.

2. Improve the method's description. From the perspective that the method is the point of the paper, I think the description may be much improved. Figure 1 may be much more detailed, for example. To understand the method I had to read the 2017 Paper by Boomsa and Frellsen, which is very nice. It would be great if some versions of Figure 3 and Figure 5 of that paper can be added to Figure 1. Also, I don't think it says anywhere in the present manuscript what sort of grid was used in the 3D-CNN part of the mode (which of the 3 grids used in the 2017 paper was used here?)

3. Highlight comparison with experiment. To support that the method is "accurate", comparison with experimental data is paramount, in my view. As I said before, I suggest you do a more thorough comparison. However, even if you decide not to, I suggest that you highlight the assessment that you have performed, by moving Table S1 and Figures S2 and S3 into the main document (If there are any limitations to the number of figures, I would rather get rid of Figure 4 than have Table S1 and Figures S2 and S3 as supplementary). Perhaps you could merge all data in Figures S2, Figures S3, and Table S1 into a single multi-panel figure that deals with all the comparison-with-experiment data.

4. Position the method in the landscape of current methods. As I said before, I think this work will be much more impactful if RaSP is positioned in the context of current methods. I suggested above that you do this by running some extra analyses and leveraging recent thorough method comparisons from the literature. If you decide not to do so, I think you could add a more detailed discussion of how you expect RaSP to compare with other methods regarding accuracy and computation speed.

5. Improve the Discussion. The Discussion, (and the Abstract) may be improved with little changes that make clearer that the point is the method, its accuracy, and speed and that the application is an example that supports that the method is useful, accurate, and fast. Also, depending on whether or not extra analyses are run, some discussion may be added to put this method in relation to other current methods.

Reviewer #3 (Recommendations for the authors):

[1] The main advantage of the method the authors claim is the speed. But they don't really take advantage of this. For example, I think the impact of this work would be much greater if they were to provide ddG predictions for all substitutions in all human proteins and to make these predictions available through a website and downloadable table. I don't see any reason not to do this, given it is not much work.

[2] The comparison to existing methods is rather anecdotal. How does the performance and run time compare to foldX? To MuteCompute? To other methods? How well do state of the art protein language models predict ddGS? How well do variant effect predictors such as CADD or Eve with good performance on the task of distinguishing pathological variants perform for predicting ddGs?

[3] How well does RASP perform for discriminating pathological from benign variants? The authors approach this problem but don't actually present the predictive performance nor do they compare it to other methods.

[4] The reality is that none of the methods for predicting ddGs perform particularly well and in places the text overstates the utility of computational methods. I would suggest the authors are more critical in their evaluation of the current state of the field. The real challenge – which is not addressed here – still remains, which is how to improve the predictive performance beyond the ok/reasonable but not that useful for many tasks predictions of Rosetta etc.

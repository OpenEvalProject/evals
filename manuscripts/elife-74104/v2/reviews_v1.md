# Peer review - Round 1

Editors:
- Nir Ben-Tal, https://ror.org/04mhzgx49 Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74104.sa0](https://doi.org/10.7554/eLife.74104.sa0)

Since the inception of comparative genomics, mining phyletic patterns has been a powerful approach for the discovery of previously unknown biological interactions. The authors use a combination of singular value decomposition of the phyletic pattern matrix and random forests classification method to uncover potential protein-protein interactions. The work illustrates the utility of such methods, which are finding increasing application in addressing various computational biological problems, such as predicting protein-protein interactions from genomic information.


---

# Peer review - Round 1

Editors:
- Nir Ben-Tal, https://ror.org/04mhzgx49 Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74104.sa1](https://doi.org/10.7554/eLife.74104.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Defining hierarchical protein interaction networks from spectral analysis of bacterial proteomes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The basic predictive power of their MIWSC approach is demonstrated in Figure 2C. However, we were surprised by the extremely low recall shown in the right panel. A recall of 10e-5 is very low indeed, and would preclude this method from having much practical value. We went ahead and recomputed both panels in Figure 2C, based on the author's raw prediction data that we downloaded for E. coli from their 'scales' website (14429 predictions). We could by-and-large confirm the left panel, but for the right panel we got recall values in the 10e-02 range, which is about 1000 times higher. Is this perhaps a mislabeled axis in the plot, or a misunderstanding on our part?

2) Also related to Figure 2C: this panel demonstrates specificity and sensitivity, but only for the author's prediction class of "direct" associations. The authors, however, also predict "indirect" associations … these in fact outnumber their "direct" predictions. Is it possible to also show specificity and sensitivity for those, similar to Figure 2C, for the same set of organisms? This could be done by taking KEGG-pathway membership or GO terms as the benchmark; in our own testing we found that the overall prediction power of their "indirect MIWSC" class is less impressive – more in line with previous efforts, which might be of interest to the reader.

3) Bacteria tree is not uniformly sequenced. There is an overrepresentation of certain lineages, e.g., of gammaproteobacteria and terrabacteria (Bacillus group) in the starting matrix. This could potentially bias the quality of the correlations that are obtained in the ``mid-range' SVD components.

4) The actual biological inferences drawn for the role of the tested gene in twitching mobility might be over-interpreted. Briefly, the authors recover 4 uncharacterized proteins (Q9I5G6, Q9I5R2, Q9I0G2, Q9I0G1) as part of their T4 pilus sub-graph and infer a general function for them in the twitching mobility. They chose Q9I5G6 because it was the only one with a supposed domain of unknown function (DUF4845). However, it should be noted that Q9I5R2 also contains another such domain DUF805 along with a Zn-ribbon domain. Further, Q9I0G2 is a T2SS secretion platform protein and Q9I0G1i is the ATPase engine for the pilus. Genomic neighborhood analysis by this referee revealed that DUF4845 likely functions with the signal peptidase in secretion. Thus, given the role of the pilus in secretion and mobility, the best one could infer is a role for DUF4845 in pilus function perhaps with a greater intersection with secretion. This could even indirectly affect the mobility function which the authors' experiments are said to support. However, the authors state right in the abstract they have uncovered a twitching mobility effector. At best they could say they have uncovered a potential component that might be functionally linked to the T4 pilus which might affect secretion or twitching mobility. Indeed, the phyletic pattern of DUF4845 does not immediately suggest that all organisms with it also possess definitive twitching mobility.

5) The authors found 4 proteins of unknown function associated with pilus motility in P. aeruginosa. Only one shows positive experimental results. It would be nice to have some idea how general this is, i.e. how many times proteins get associated by the approach, even if they have biologically known but totally distinct functions.

6) The authors might experiment with using a matrix that removes closely related gammaproteobacterial, actinobacterial and terrabacterial lineages to see its effects on their training and predictions.

7) When the manuscript speaks of scales of protein interactions represented in the spectrum, is this visible in the singular vectors? We would imagine that large-scale properties should correspond to distributed vectors (and not only large singular values), while local scales should intuitively correspond to localised vectors.

8) It is quite evident that the first singular vectors are related to phylogeny, which is known to be a major source of variability between orthologs (at the end SVD achieves spectral clustering, and phylogeny reconstruction hierarchical clustering, which are expected to show some level of coherence). What is more interesting is the crossover from phylogenetic to functional information.

9) The MI is not really well defined, it would be hard to reproduce on the basis of what is written in the Methods section.

10) We have some doubts concerning the gold standard. If non-interacting pairs are randomly chosen, and fractions of interacting and non-interacting pairs are given in their approximate true proportions, the non-interacting set should contain about the same number of actually interacting pairs as given in the positive examples. The choice of so many random pairs to represent non-interacting pairs is therefore dangerous and potentially misleading. It remains also unclear how the extreme bias towards non-interacting pairs in the dataset is handled (most machine-learning algorithms run into problems in this case). When partitioning into training and validation sets, is this done independently for each class, or for the entire dataset? In the latter case, the number of positive examples might fluctuate a lot in the training set.

11) The comparison with Cong et al., might be potentially spectacular, but it is hard to understand it from the little paragraph. This should be explained better. One should also keep in mind that Cong et al., use an unsupervised approach as compared to the supervised in the present manuscript.

12) The notation in Materials and methods requires revision. To give an example (beyond the MI part already mentioned), n is the number of proteomes in the first paragraph, and the number of OGGs in the second. Please use consistent notations!

13) Is Figure 1S2B really showing normalized columns? They appear optically to have very different variances, even if they all should be normalized to variance 1.

14) The code should be made available.

Presentation:

1) The paper is very hard to read and to understand. It is written in a semi-technical jargon mixing spectral analysis, machine learning and information theory. Even having expertise in these fields, we had to continuously jump between the main text, the methods and the figure (including the supplementary figures – a total of 86 pages) to follow the argumentation of the paper. This style is not suitable for a journal with a broad and interdisciplinary readership. The authors should make a serious effort to clean up their presentation, such that the main messages become accessible. Currently, even for disciplinary journals in computational biology or bioinformatics, the presentation would require simplifications.

2) The general reader would benefit from an opening figure that clearly lays out the steps in the workflow starting with SVD (giving some general background) to random forest training. It can augment what is shown in the current figure 1 and one of the supplements to figure 2.

3) The abstract repeats 8 times the word "hierarchy" or "hierarchical". Avoid such excessive repetitions.

4) The introduction was a bit short in giving credit to previous efforts in this area. Yes, the founding papers from the 90s are cited, but there have been quite a number of studies in the meantime, including the use of SVD, reviewed for example here: Nagy et al., NAR 2020, https://doi.org/10.1093/nar/gkz1241 or Moi et al., PLoS computational biology 2020, 16 (7), e1007553

5) The results on motility are really nice. We suggest placing them much earlier in the paper, and do the more technical stuff with random forest etc. later. It could come directly after Figure 1C has been explained.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Defining hierarchical protein interaction networks from spectral analysis of bacterial proteomes" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

General Summary:

While the authors have made clearly visible efforts to improve the presentation of their manuscript, the major problem remains: while the results are very interesting, the presentation of the technical details is cumbersome, and reading the paper without massive reference to the huge number of supplementary figures is hardly possible. I think another round of simplification is unavoidable.

Detailed report:

I am still convinced that this paper has very interesting results, which fully merit publication. But in particular, the initial part of the paper is hard to read. In a nutshell, the method is quite simple: (a) extract a large matrix of phylogenetic profiles (here many proteomes annotated via OGGs), (b) perform a standard SVD, and represent OGGs via their projection to the singular vectors, (c) extract proteins having correlated projections in small spectral windows. The innovative part of the paper is a clever use of these spectral windows going from the singular values/vectors describing the large-scale organisation of the data, to smaller and smaller singular values, far beyond the few typically used in PCA, showing that these deep parts of the spectrum contain finer and finer information – here going from large functional categories via pathways to PPI. It should be possible to present this in a simple way.

I would like to make a number of more specific points:

1. The reading is impossible without the massive use of supplementary figures. To give one example (out of many), the singular vectors in UOGG and VOGG are used in methods but introduced only in Figure 1 Supp. 1. In addition, the left and right singular values are denoted equally as |n>, which is a bit confusing (even more since as mentioned, the matrices are not defined in the text). In general, the authors should revise the paper such that the supplement gives supplementary information, and the paper can be read without having ~50 pages of supplement in your hands.

2. The method heavily relies on subjective hyperparameters and thresholds: For the number of singular values considered, for the bin size in the MI calculation, for the size of the spectral window, for the used cutoffs of the spectral depth. Together with the somewhat anecdotal results (concentration mostly on motility), this gives the impression that the biological system and parameters are hand selected to show nicely interpretable results. I sincerely hope this is not the case, but if the authors would, e.g., show the tree generated by changing spectral depth from largest to smallest values, the different levels of organisation could become more evident (in case well-separated levels exist).

3. In some cases, it is hard to understand if the results are significant. If one considers Figure 1E, even a uniform MI distribution would have a similar shape as the blue curves, since the cumulative would be linear, and represented with a log-scale of the spectral position.

4. In some places, results imposed by the analysis are presented as astonishing findings. The most evident case is the hierarchical structure when changing spectral depth. Since spectral depth is defined as the depth where correlations are for the first time non-significant, the edge set of the graphs at higher spectral depth is necessarily proper subsets of those at lower spectral depth, and thus connected components are proper subsets, too. If all statistically significant correlations in each spectral window would have been taken into account, edges between proteins might disappear at some depth, and reappear at a deeper one, making the network potentially non-hierarchical.

5. Heavy but somewhat random statements like "Understanding the molecular basis of a phenotype requires (i) defining interactions that create units of collective function at different biological scales and (ii) relating these scales to create a hierarchical model of emergent phenotype." should be avoided.

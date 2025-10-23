# Peer review - Round 1

Editors:
- Yousin Suh, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61138.sa1](https://doi.org/10.7554/eLife.61138.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript provides a comprehensive characterization of the trajectory of murine muscle aging and correlates that to the ability of Klotho to exert beneficial effects on muscle health. The novel entropy-based modeling defines the trajectory of murine muscle aging, which will certainly be of interest to the community of researchers studying the biology of aging.

Decision letter after peer review:

Thank you for submitting your article "The biphasic and age-dependent impact of Klotho on hallmarks of aging and skeletal muscle function" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Daniel Remondini (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The manuscript by Pius et al. seeks to comprehensively characterize the trajectory of murine muscle aging and to correlate that to the ability of Klotho to exert beneficial effects on muscle health. The authors present a comprehensive profiling of skeletal muscle aging at the histological, functional, and transcriptomic levels across the lifespan (young, middle, old, oldest old age) and network entropy as a measure of molecular dysfunction during aging. The authors identify a network entropy inflection point and find it correlate with the ability of Klotho delivery to attenuate age-related changes. Interestingly, network entropy does not further increase from old to oldest old and Klotho in oldest old fails to exert a benefit at that age. The study presents a large amount of work, particularly in compiling the various datasets and developing a novel entropy-based modeling to define the trajectory of murine muscle aging, which will certainly be of interest to the community of researchers studying the biology of aging. All four reviewers agreed that the study provides interesting insights into aging. However, as detailed below, various concerns were also raised, relating in large part to insufficient clarity in the current version with respect to the authors' methods and the limitations of their approach and data.

Essential revisions:

1. As the transcriptomes and network entropy analysis are the cornerstone of the authors' approach, it is essential that they provide clear and complete details regarding the experimental strategies and rationale underlying each analysis. In particular, detailed answers to the following key questions must be available in the present manuscript:

2. There were mixed reviews on the validity and advantage of the entropy network method: two positive and two negative reviews. The entropy network model was built on protein-protein interaction (PPI) networks. Given that the authors used transcriptomes as input data, provide the validity of the methodology and discuss the limitation of the approach. For example, numerous reports show that the lack of positive linear correlation between protein levels and the amount of mRNA, e.g. Cell 165: 535-550; Molecular and Cellular Proteomics 1: 304-313, Scientific Reports Article number: 3272.

3. The authors should provide justification as to why the entropy change from 522 to 528 (only 1.1%, p=0.07) in Figure 3D is deemed meaningful and important.

4. pg 7 line 123-130 and Figure 3. From the figure it emerges that the first component of PCA seems to characterize aging progression: which are the genes mostly associated to this component? Further analysis (e.g. gene selection based on loadings, possibly after Factor Analysis) could help to emphasize these aspects and identify the key genes associated to aging progression. Moreover, if biologically relevant, these gene set could be characterized throughout the study in relation to aging progression and to the effects of Klotho. Further: did authors try other dimensionality reduction methods such as t-SNE, that in principle could identify other peculiar aspects within the data?

5. Methods section: more details about the analyzed network are required, e.g. which is the size of the networks used to estimate network entropy? Which are the main global features (e.g. link density, presence of disconnected components,.…). Moreover, there appears to be more than one network that has been analyzed (genes associated to hallmarks of aging in line 146, global PPI network on line 155). A clear description is needed, in the Methods or in Supplementary material. Further: in Figure1D and supplementary Figure S1 the Network entropy values appear with a "confidence interval" (in light blue). In the paper there are no references about how this uncertainty was estimated: is it standard deviation or standard deviation of mean? It is a 95% confidence interval or something else? Also for this point a clear description is requested.

6. In Figure 3, the gene perturbation data presentation is a bit odd; what would be much more helpful would be heat maps showing the progression of gene changes from young to old to oldest-old, and which of these are counter-regulated by Klotho over-expression, in particular, for the pathways shown to be linearly regulated with age, but counter-regulated by Klotho in the old. Figure 3G is redundant. Remove 3G and instead indicate the DEG numbers in each pie chart in Figure 3F. Figure 6C is also redundant. As in the Figure 3D, 3E and 3F, in Supplemental Figure 2B Old vs Young should be compared to Oldest-old vs Young age group, instead of comparing Oldest-old vs Old. For oldest-old it would be interesting to see what Klotho does. The authors get at this in figure 6D but it would important to show the actual degree of perturbation connected to the pathways shown.

7. It seems like the oldest-old Klotho vs oldest-old pathways go in the opposite direct as Old Klotho vs Old. Is that true of every pathway? it would be helpful to connect the gene expression changes to a mechanism.

8. There is a substantial literature on the skeletal muscle transcriptional studies throughout the lifespan. An example in mice (https://doi.org/10.1016/j.biocel.2014.04.025), a very recent example in rats (https://doi.org/10.1016/j.celrep.2019.08.043) and in humans (https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.0020115). Refer to the previous work, which are missing in the current manuscript.

9. The idea that "molecular disorder" underpins age-related muscle dysfunction is clever. Assuming the validity of the approach, an obvious question is whether the "entropy" approach used in this manuscript can be applied to the available datasets to validate the work and to compare differences across species. This translational component and general applicability is important to show and will increase the impact of this work.

10. There is no reference about repository of the RNA-seq data, which is mandatory for eLife. Otherwise authors should justify their decision about why not to make data accessible.

11. Would it be possible to generate an interactive online website tool to probe this dataset (and perhaps the others above), which includes the "entropy" analysis of molecular disorderliness performed here? This could be very useful to the scientific community and reduces the concern that the authors are under-utilizing their novel approach to gene expression analysis.

12. The baseline characterizations of aging are well-done and consistent with prior studies. Likewise, the experiments involving the over-expression of Klotho do not appear novel. Detailed answers to the following key questions must be available in the present manuscript to provide a novelty of the study:

13. The progressive underexpression of Klotho (as shown in Figure 4A) is much smoother than the growth in FGF23 (Figure 4B) that in the paper is claimed to be the major interactor of Klotho: is there any explanation for that? Maybe the group of direct (or second neighbor) interactors of Klotho (and of FGF23 if it is relevant) should be studied specifically, to characterize the surrounding environment of these genes and provide a deeper view of the possible processes associated to aging and to Klotho response. Moreover, it is shown a large difference between growth of FGF23 in oldest-old female as compared to male of the same age group (in female mice the growth starts earlier): can the authors try to explain why? (Maybe FGF23 interactome could provide further insight?)

14. More information on the effectiveness of the AAV is needed. What organs are being affected by this? How much over-expression of Klotho is there with AAV-Kl, and specifically how much in muscle? Explain why the AAV approach was used instead of Klotho protein supplementation, which seems to have been effective in the past and is a safer and more translatable approach.

15. The effects of Klotho are interesting; what would have been helpful would be some pharmacodynamic/pathway studies. Are the effects seen happening as a result of increased FGFR signaling? FGF23 levels go up with age, while Klotho levels go down. This may be a reaction to low FGFR signaling. When Klotho is given back, which are the key pathways that are noted to change? In other words, it would be helpful to connect the gene expression changes to a mechanism.

16. As a comment in the final discussion, since the results about mice treated with Klotho are stated as general, but transcriptomics profiling was performed only on female samples, it should be emphasized that these results could not be generalized independently of sex, since many differences have been observed between the two genders.

17. Following relevant issues emerge that require further analysis, that should not alter the overall results of the paper but in my opinion could reinforce them. Detailed answers to the following key issues must be provided, including justification as to why suggested experiments cannot be done:

18. Page 10 line 215; AAV-KL treatment rather decreased force in oldest-old group (Figure 5F and 5G). Given that Klotho over-expression in the oldest-old is perhaps detrimental, experiments should be undertaken to explore how increasing Klotho earlier in life influences regenerative and transcriptional responses later in life. If the positive attributes of Klotho, when applied to an "unhealthy" oldest-old environment, then become a negative stress, it is an idea that should be explored further. It would also be welcome to see how Klotho influences more translatable outcomes such as adaptability to exercise training, since the link between regenerative potential and age-associated sarcopenia is unclear.

19. For the mouse muscle IHC phenotyping, it is warranted to show other measures such as fiber type-specific CSA, quantification of ECM (via Sirius Red or Masson's), markers of denervation, as well as intramuscular adipose tissue infiltration (IMAT). Extending the analysis to a more oxidative/slow-twitch muscle such as the soleus would also be welcome, given that the TA mostly contains muscle fibers that aren't present in humans (Type IIB).

20. Further characterization of the AAV-Klotho regeneration experiments is warranted. Why is there less fibrosis in AAV-Kl? Are there fewer FAP/fibrogenic cells? Are there more satellite cells? Presenting collagen 4 intensity (Figure 4H) seems unorthodox. Please show Sirius Red or Masson's and normalized to area. In the aged AAV-Kl experiments, why is there less lipid accumulation, which appears to be specifically within (and not between) the muscle fibers? Was lipid accumulation between muscle fibers (IMAT) different? An Oil Red O analysis is warranted.

21. Serum levels of cholesterol and insulin of young mice (3-6 month) is necessary in Figure 4D to compare with those of old mice overexpressing Klotho.

22. As previously reported by the authors in Nature communication (2018), it would be interesting to compare the Klotho's function in the mitochondria of muscle progenitor cell, with the Klotho's function here identified.

23. To verify the author's suggestion in Discussion section, it is important to examine whether F2 or Kng2 plays a bifurcation role in old and oldest muscles.

24. The key experiment that seems to be missing is the manipulation of Klotho earlier in life to try and prevent the onset of "molecular disorder" later in life, especially since acute Klotho over-expression in the oldest old seemed to have the opposite effect.

25. A summary figure that highlight the main findings of this manuscript would be a welcome addition.

26. Abstract has no conclusions and does not properly reflect contents of the results.

# Peer review - Round 1

Editors:
- Janice L Robertson, https://ror.org/01yc7t268 Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75751.sa0](https://doi.org/10.7554/eLife.75751.sa0)

del Alamo and colleagues illustrate that restricting the depth of the input multiple sequence alignment allows AlphaFold2 to predict diverse conformational ensembles of transporters and receptors, as opposed to single static models reflecting individual states. Although they are limited to a small number of test cases of membrane proteins, the examples are of interest to members of the community. This work presents a validation of a simple approach that may be applicable to all proteins and is thus an exciting advance that is expected to be of broad interest.


---

# Peer review - Round 1

Editors:
- Janice L Robertson, https://ror.org/01yc7t268 Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75751.sa1](https://doi.org/10.7554/eLife.75751.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Sampling the conformational landscapes of transporters and receptors with AlphaFold2" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Janice L Robertson as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Kenton Swartz as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In general, the reviewers were enthusiastic about your finding that reducing the size of the sequence alignments input into AlphaFold2 increases conformational diversity for predictions of transporter membrane protein folds. While the test set is small, the validation provided is convincing, and the results are likely to be broadly useful to many who study protein conformational changes. However, it was found that many details were lacking about the methods, which will limit the ability for others to reproduce these findings or advance this approach further. With that, the following revisions are required in order to describe the methods in appropriate detail and increase the quantitative presentation of the analysis. In addition, it is important to temper general claims made throughout the paper to acknowledge these findings are based on a small test set of proteins. Since these essential revisions focus mainly on writing with some minor additions to the analysis, we expect that these changes will be tractable within a reasonable time frame.

Essential revisions:

1) Elaboration of the methods used. Additional details are needed in order to be able to evaluate the validity and reproducibility of the approach. Specifically,

– Include a brief description of the AF2 protocol and each point at which variability is introduced, i.e. by sequence alignment, template choice or recycling.

– The alignments used to develop the models should be provided. Specific details on how the visual inspection of the alignments guided their refinement should also be included. What is padding of the MSAs? How were the MSAs trimmed from 5120 to 32? What was the distribution of lengths of the sequences included? What were the sequences that ended up being included and what was the sequence diversity in the sets used?

– Earlier in the paper, it is stated that loops were removed from the sequence alignments. However, they are later discussed as being generated in the models. Provide more details about when the loops were included in the structure prediction.

– For some of the targets, the template-based modeling clearly improved sampling of various conformations and for others it didn't. How were the template selected for the template-based modeling?

– What are the PDBs used in the structural analysis? These should be listed explicitly in the pertinent figure and in the methods.

– Define pLDDT.

– What does "eliminating postprocessing with OpenMM" constitute?

– How were misfolded models identified? Providing a reference is not sufficient here.

– To address the predictive power of this approach please clarify which models were used for the PCA. Were the principal components computed from low-MSA AlphaFold2 predictions only, rather than from the large-MSA AF2 predictions, which would make the point moot since the PC reflect the range of conformational changes observed in multiple models, not a subset. Previous studies (Bahar and colleagues) suggested that PCA allows for prediction, but that PC1 is not always the useful component and so the question arises of how to select the correct PC to make the prediction?

2) Additional analysis:

– Analysis of the model accuracy with alignment quality. How do the current results depend on alignment quality and diversity? Which sequences are included in the 32, and how do your findings depend on this selection?

– Analysis of the model accuracy with sequence length. While sequence information is examined, the authors say that no general pattern was apparent regarding the ideal MSA depth. Yet, a more common strategy, namely, to compare sequence sets using a factor related to the length (L) of the protein (or perhaps the core of the protein being modeled) may reveal more. Indeed, by reducing the dataset to 32 sequences, only the longest proteins were starting to include misfolded examples. Overall, it would be more straightforward to compare models built with, e.g. L*2, L/2 and L/5 sequences. While this requires building additional models it would also provide a clearer outcome and strategy that future users could follow. A bonus may be that it would reduce the chances of misfolded models that need to be filtered out. At the minimum, the authors should reframe the data they have as a function of each protein's length.

– Analysis of template usage. What were the templates used? Was the performance of AF2 dependent on the sequence similarity between the template(s) and the target?

– Quantification of conformations. There are many occasions where the discussion of structural similarities/differences are qualitative, e.g. “virtually every transporter model superimposed nearly perfectly with the training set conformation, and none resembled the alternative conformation”. This statement should be accompanied by quantitative data. Furthermore, the different known conformational states, i.e. IF, OF and occluded, require a quantitative definition to support statements like “One target, MCT1, was exclusively modeled by AF2 in either IF or fully occluded conformations regardless of MSA depth. Notably, these results closely parallel those reported by DeepMind during their attempt to model multiple conformations of LmrP in CASP14.”.

– Along these lines, it is reported that conformational variability is not obtained by the targets that were included in the AF2 training set, and yet the extent of conformational diversity appears similar to that analysis presented in Figure 1. For example, MurJ appears to show the same degree of conformational sampling with 32 sequences as for ASCT2. A more objective analysis of the conformational sampling is required to define the dynamic range explored by the structural conformations, especially since some of the endpoint structures are quite similar to each other.

3) Please respond to and address the additional recommendations provided by the reviewers.

Reviewer #1 (Recommendations for the authors):

1. The conformational ensemble from AF2 appears to move along certain structural paths in the different analyses. How does this compare to a linear interpolation between the endpoint structures?

2. In Figure 1, it is recommended that the axes of Figure 1B be scaled similarly to the format used in Figure S3 since the experimental TM-score differences are quite different between the different proteins. Aside from ASCT2, and potentially MCT1 with templates, the dynamic range of the conformational change appears to be minimal, but this may just be difficult to see due to the current plot format. In addition, move Figure S1 into this main figure to allow the reader to discern the structural and conformational variability in this test set. Finally, please add all of the pdbs used for the experimental comparison structures, both in this figure, and in the methods.

3. Is the term “ground truth structures” referring to the crystal structures or other experimental structures? Please change this term as experimental structures do not correspond to a “truth” but is a physically accessible conformational state of the protein under those experimental conditions.

Reviewer #2 (Recommendations for the authors):

1. First, I would disagree with the title of Figure S5 and the beginning of the corresponding title, which seem to be categorical about the lack of exploration of alternate conformations for these examples, but then somewhat contradict the rest of the paragraph, where it is explained that some cases (MurJ and CCR5) behave differently from the others. These discrepancies should be resolved.

2. Second, I think it would be of value for the readership to mention that no function is included to describe the membrane in these modelling processes – even when the lipids themselves may be critical to shift these conformational equilibria. This observation actually makes the authors’ findings all the more remarkable, but also perhaps harder to interpret.

Reviewer #3 (Recommendations for the authors):

1. Change Lat1 -> LAT1

2. The following statement is unclear and should be elaborated. “Several preprints have provided evidence that AF2, despite its accuracy, likely does not learn the energy landscapes underpinning protein folding and function39,53,54. We believe that our results bolster these conclusions and highlight the need for further development of artificial intelligence methods capable of learning the conformational flexibility intrinsic to protein structures.”

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Sampling the conformational landscapes of transporters and receptors with AlphaFold2” for further consideration by eLife. Your revised article has been evaluated by Kenton Swartz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The reviewers found that the current title may lead the reader to misinterpretation. An alternate title “Sampling alternative conformational states of transporters and receptors with AlphaFold2” is more appropriate and should be adopted.

2. The findings in Figure 1 Suppl2, that the number of sequences isn’t correlated with an increase in conformational homogeneity, and displays erratic dependence for some proteins (especially ASCT2, Lat1 and STP10), are surprising. Consequently, it seems necessary to alter some statements in the manuscript, accordingly. For example, in the abstract: “reducing the depth of the input MSAs is conducive to the generation of accurate models in multiple conformations by AF2”.

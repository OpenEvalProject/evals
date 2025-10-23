# Peer review - Round 1

Editors:
- Nir Friedman, The Hebrew University of Jerusalem , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06397.029](https://doi.org/10.7554/eLife.06397.029)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled "Building accurate sequence-to-affinity models from high-throughput in vitro protein-DNA binding data using FeatureREDUCE" for consideration at eLife. Your article has been favorably evaluated by Aviv Regev (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The main concerns raised by the reviewers were:

1) Lack of details about the methods, and in particular how dinucleotide interactions are incorporated and their impact on the quality of predictions, and the use of robust regression.

2) More thorough and detailed evaluation of the performance of the method compared to others (the reviews provide specific suggestions).

Reviewer #1:

During recent years there has been a wealth of information gathered about the DNA-binding specificity of proteins using microarrays and sequencing methods. A challenge posed by this data is how to generalize from experimental results to a model of the DNA-binding preferences (or affinities) of the protein. The authors describe a computational tool (FeatureREDUCE) for dealing with these challenges. They evaluate their tool on a few in vitro and in vivo datasets and compare it to recent state of the art tools.

I agree with the authors’ description of a shift in the field from data-poor regime (where only a few binding sets per protein were known) to a data-rich regime where high-throughput methods assigning affinity/preference of the protein to thousands sequences. Yet, the methodology for representing these affinities has been lagging behind the experimental advances. I also agree with their goal of finding such a representation to generalize (i.e., extrapolate) from the results of PBMs (which list affinity value for all possible 8-mers).

To the best of my understanding the new contributions here involve the following:

1) The use of feature-based "free-energy" based method combined with specific robust estimation methods. These extend previous methods of the authors by using published methods.

2) Estimating position-bias in PBM data in parallel to estimating sequence preferences.

3) The use of Poisson regression for SELEX-seq data.

The authors evaluate their claims by using existing datasets to evaluate the results of their method compared to few recent ones in the literature.

I list comments on these aspects of the paper, especially the first, below. These describe what I view as major problems in the current manuscript, but I believe they are all addressable.

The manuscript is, above all, a methods paper. It seems to be carefully designed method to solve a well-established and important problem and it definitely would be suitable for a specialized journal. For a wider audience, I would have expected a much more significant innovation that provided new and useful insights about the general computational problem and the underlying biological reality.

Major concerns:

The authors discuss at length the importance of their free-energy view of the problem. Frankly, the discussion relating free energy representation that defines a Gibbs distribution and probabilistic models (especially exponential models) has been hashed thoroughly in multiple venues and communities. In terms of representation, there is no difference between the representational powers of position-specific Affinity and position specific Probability matrix. I agree that affinities allow an elegant way to adjust the probability due to changes in protein concentration (if you believe the system is in equilibrium). However, this is a much more minute difference than the authors' presentation makes it seem. I would tone down the "sale pitch" on this view. It is a useful one to have (and has been discussed since early days, e.g., Berg and von Hippel, 1987), but it is not inherently superior.

Similarly, the introduction of feature-based representations of free-energy differences (ΔΔG) is mathematically similar or identical to previous methods (e.g., Sharon, Lubliner and Segal, 2008).

There is a great discrepancy between the main text and figures and the Materials and methods regarding the use of features (one of the novelties of the current manuscript). The discussion in the Materials and methods mentions only position-specific mutation and do not mention any higher-order feature, which ones are searched, and how. From Figure 3 I assume these are strings of mutations. However, the way the method generates candidate features (all the ones I see in the figure involve pairs of adjacent positions) or search/decide among them is not specified.

Another discrepancy between the main text and the Materials and methods is the issue of robust estimation. The authors view the use of robust estimation as one of their main contributions (reference in the Abstract, dedicated supplemental figures, etc.). Yet, the Methods are vague about the details. The main text provides a reference for a book about robust statistics, which while surely a useful text, is not helpful for the reader who attempts to understand what actually happens in the estimation procedure.

Much of the evaluation of the method is based on its performance in a published comparison of many computational methods. It is surprising that one of the best performing methods in that comparison has been unpublished in the two years since the comparison was performed (the program has been available for download apparently).

The evaluation carried out in this manuscript is limited for cases where there is external information to compare against. I found the evaluation of GO enrichment p-value of Figure 3 as a very indirect (and inaccurate) indicator of quality (the difference between p-value of 10-8 to 10-7 are not that dramatic and can be driven by changes in the status of few genes). Similarly, the differences in RMSE in Figure 4 are not convincing me that the model is substantially different or better. First of all, ChIP signal (enrichment over background) is often not a reliable quantitative signal. Second, it is unclear how differences in low affinity sequences change actual predictions made with these models. I would expect an evaluation to provide the reader with a sense as to when the precise details do matter. I suspect they do, but the current presentation is focused on various summaries that are not transparent nor reflect actual differences in predictions.

Reviewer #2:

The manuscript describes FeatureREDUCE, a successor to the very successful MatrixREDUCE method for inferring TF binding preferences/(relative affinity) from in vitro binding data. FeatureREDUCE adds robust regression, dinucleotide affinity models, and various features specific for recent large-scale in vitro assays of TF binding (location models for PBMs, Poisson regression for sequencing-based approaches, etc.). Results are presented on a handful of TFs, so these examples simply illustrate the advantages of the new features rather than to extensively test them.

Although it seems iterative, and the validation is limited, this is very important work. The software package would be immediately useful to a large group of researchers. Despite the abundance of work in this area, there's really nothing as comprehensive (and correct) as the described software available. BEEML and BEEML-PBM come close but the manuscript nicely illustrates the advantages of FeatureREDUCE. The fact that this software works well was already illustrated in a previous study (Weirauch et al.) and all the important conceptual and engineering advances over the past few years are implemented in this package. I think eLife would be a great spot for this manuscript to end up.

A few things need to be fixed though. First, there are a number of missing details about the methodology that need to be filled in. Also, the manuscript is a little grandiose and needs to be toned down. Finally, and very importantly, the software needs to be open source and freely available. The value of this manuscript is the associated software; if that software isn't freely available, then there's no point in publishing this manuscript.

Major concerns:

1) It looks like in Figure 4 that you didn't permit BEEML to fit a protein concentration parameter as well, so this isn't a fair comparison. To make it fair, you could i) not fit a protein concentration parameter for FeatureREDUCE or ii) fit one for BEEML. Actually, you should do both, just to be sure.

2) Please provide more details in the "Robust Regression" about the MM-estimator. This technique will be new to most readers. How was it implemented? Are there any other free parameters besides the number of trimmed probes?

3) From Equation 11, it looks like BiasREDUCE requires non-linear regression. If so, then Figure 1 caption #3 is wrong.

4) How do you go from a seed k-mer to an initial PSAM? Presumably, you can't start with any zeros in the PSAM or you will get zero partial derivatives.

5) What is your tolerance for the L1-norm for the palindromes?

6) You need to provide more details about the multi-PSAM mode and experiments. Do you fit an initial PSAM and then fit a second one to the residuals using the entire pipeline (starting with #1)? Do you then re-fit the first PSAM? How do you decide whether or not a second PSAM is necessary?

Reviewer #3:

Riley and colleagues describe the development and application of a computational regression algorithm (FeatureREDUCE) to build more accurate affinity models from PBM or SELEX-seq datasets. This new method relies on iterative regression steps and the incorporation of dinucleotide dependencies to train improved affinity models for transcription factor binding. The utility of these affinity models is demonstrated on transcription factors with simple and complex binding modes.

Overall, this computational approach appears to display improved performance over other existing methods for building affinity models, and consequently will be of value to the broader scientific community. However, the current manuscript does not describe for the end-user the type of models that are generated for use in other applications – in particular how weights for the dinucleotide dependencies in the FSAM can be represented and readily displayed for interpretation. One subset of dinucleotide dependencies is displayed in Figure 3A, where surprisingly (if this reviewer is interpreting the data correctly) the strongest dinucleotide contributions to the model are substantial penalties against the consensus sequence. To this reviewer, this result is counter-intuitive, and deserves comment, as it does not mesh with a simplistic view of dinucleotide effects in protein-DNA recognition (e.g. a single amino acid simultaneously and synergistically contacting neighboring base pairs in the preferred binding site). Moreover, since the authors are claiming the demonstration of the existence of dinucleotide dependencies based on their analysis, which has been a contentious point in the field, further explanation is warranted.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Building accurate sequence-to-affinity models from high-throughput in vitro protein-DNA binding data using FeatureREDUCE" for further consideration at eLife. Your revised article has been favorably evaluated by Aviv Regev (Senior editor), a Reviewing editor, and two reviewers.

The authors responded to the issues raised. However, the reviewers’ opinion was that this response is too terse/unsatisfactory in places. We strongly recommend that the authors attempt to provide a clear understandable description of the methods, to the extent that someone with reasonable knowledge in the field but not in this project can understand what is being done in each step.

Essential revisions:

1) The software must be deposited to a public repository (GitHub or similar). Or at the very least, the open source version of FeatureREDUCE used in this manuscript should be made available through the supplement for this journal article. Published software should have an additional guarantee of availability though the journal and/or an outside authority like GitHub (or BitBucket, or similar; we do not wish to proscribe the channel for release).

2) Clarify the methods description of discrimination from reference sequence. Reviewer comment (following the authors' response):

Again, if this reviewer is interpreting the data correctly from Figure 3A, there is a penalty against CG dinucleotides at positions -1 and 1. (Likewise CA at -3,-2 and TG at 2,3) Based on the description in the Methods:

"FeatureREDUCE models the binding free energy for sequence S as a sum of coefficients associated with all the "features" that discriminate S from the reference sequence Sref (usually the DNA sequence with the highest affinity). In this study, we considered single-nucleotide features ("A at position 1") and adjacent dinucleotide features ("CG at positions 3 and 4")."

The authors describe the utilization of these features to discriminate S from Sref. The strongest (negative) dinucleotide features in Figure 3A are for dinucleotides that are in Sref, as presumably the highest affinity sequence is the reference sequence. Again, this reviewer may be missing some critical understanding of the algorithm, but based on the methods description the result does not fit with expectation. (Why would dinucleotide dependencies be discovered that apply to Sref?) Consequently, a more adequate description is required in the Materials and methods.

3) “Feature-based modeling of intensities”. This paragraph is hard to make sense of, and uses too many ill-defined terms. Please include what the features are, the coefficient (what are "columns of features"?), and how are defined (as you did for position-specific case).

4) The "Seed detection" paragraph is similarly obscure.

5) Probe-position effects – what is α? Are the γ coefficients shared among all probes? When/how are they estimated?

6) The authors use rlm (from MASS package) to estimate the "parameters in Equation 11". Up to now the authors discussed coefficients (are these parameters?). As far as I can tell, these do not appear in a linear form in Equation 11. How do you resolve that?

# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60321.sa1](https://doi.org/10.7554/eLife.60321.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Linking individual neurons to their anatomical names remains a vexing problem that limits efforts to determine patterns of gene expression and neuronal activity at the single-neuron level in C. elegans. This paper presents a computational method for solving this problem and, as such, has the potential to advance neurobiology in C. elegans. The approach could, in principle, be adapted to any nervous system from which a computational atlas could be derived following the pipeline laid out in this manuscript. The generality of the approach and its ability to incorporate additional datasets in composing the computational atlas, may lend itself to performance improvements by crowd-sourcing datasets.

Decision letter after peer review:

Thank you for submitting your article "Graphical Model Framework for Automated Annotation of Cell Identities in Dense Cellular Images" for consideration by eLife. Your article has been reviewed by Ronald Calabrese as the Senior Editor a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Whole brain imaging in C. elegans allows monitoring the activities of a large fraction of worm neurons during behaviors. However, the identity of each cell in the nerve ring remains largely unknown, prohibiting further analysis that integrates structural and functional information of the worm circuit. This problem has been partially amended by manual annotation from experts. However, this is a time-consuming and error-prone solution when one is dealing with a large dataset. Thus, the reviewers were enthusiastic about this manuscript because the authors take one important step towards automated annotation of neuronal identities. Methods in this work are innovative and attractive. By minimizing energy functions imposed by absolute coordinate differences (unary potential) between images and atlases, as well as differences of the pairwise relationship between neurons, the authors show that their CRF_ID model outperforms SOTA registration model in accuracy, speed, and robustness.

Essential revisions:

There were several concerns that necessitate serious revision and clarification. Ultimate acceptance by eLife will depend upon how the concerns can be addressed and whether the methodology will be practically useful to others in the field after further clarification. The original reviews are appended, and all concerns should be addressed. Chief among the concerns that emerged on the reviewer consultation were:

1) The authors were not clear about whether any data were held out in developing the data-driven atlas and how this choice will impact the ultimate utility of the method. Moreover, they were not clear about how this atlas was built – the motivation for building it.

2) The authors must be clear when synthetic data is being used and which strain is being used for the biological data.

3) The reviewers found the text inadequate and essentially reviewed the Appendix. For ultimate publication the authors must make the methodology clear to general readers in the main text.

4) The prediction accuracies of the model vary from case to case and was quite low in the scenario of missing neurons. The authors must state clearly, under the worst scenario such as whole brain imaging without colors, the prediction accuracy of their methods. The prediction accuracies of the CRF model, contingent upon different datasets and different noise levels, should be in a self-contained main figure, not in the supplements.

5) A key element of these reagents/strains and the annotation is that, strictly speaking, it annotates nuclei (not neurons). The authors need to explicitly tackle the question of whether the method would work with cytoplasmic markers and to properly annotate the strains they did create as using nuclear localization signals.

6) Important elements of the metrics presented to evaluate the annotation method are poorly described in the manuscript, and it is unclear from the manuscript or from the materials in the code repo the form of the results. By this we mean not the file format, but rather does the algorithm return a single assignment or a ranked list for each cell or something else?

7) Concerning the spatial location of the neurons used in the ground truth datasets. From inspecting the authors' GitHub repo, it seems that the neurons in the hand-annotated ground-truth Neuropal datasets are not evenly sampled throughout the head. Rather they are enriched in easy-to-label locations, like the anterior of the head, with less coverage in the more difficult locations (e.g. few neurons are labeled in the lateral ganglia or retrovisicular ganglia). The authors should explicitly recognize this bias in the hand-annotated ground-truth dataset.

Reviewer #1:

The application of conditional random fields to neuron registration in C. elegans represents a significant advance that will impact the field. I have major concerns about the interpretation of the method's performance: some technical, for example test sets were seemingly not held out from the data-driven atlas; and others more related to confusing or potentially misleading presentation. It was often unclear which dataset, method, reagent or performance metric (for example Top 1 vs Top 5) was being discussed. I also have concerns about giving appropriate credit for work and reagents from other groups.

1) Test sets used to assess performance do not seem to have been held out from the data-driven atlas, which raises doubts about the interpretation of Figure 2A and Figure 6E and C. This could artificially inflate performance compared to tests with a held-out animal, which would reduce the utility of the method. This could also explain the dramatic difference in performance observed fr om synthetic data with experimentally derived noise (35% accuracy) Figure 2—figure supplement 4A, and real experimental data matched to the data-driven atlas (>75% accuracy Figure 2A).

2) Lack of clarity could falsely give readers the impression of higher performance:

a) It is often ambiguous as to whether Top 1 or Top 5 performance is being plotted. Example: in Figure 3B the caption makes no mention, so one would assume Top 1 accuracy; but subsection “Cell annotation in gene expression pattern analysis” suggests Top 5. This is a crucial distinction and needs clarity in every subpanel.

b) It is also unclear when synthetic data is being used. Example: subsection “Identity assignment using intrinsic features in CRF_ID outperforms other methods” states that the algorithm "maintains high accuracy even when up to 75 % of cells in atlas were missing for data" but from the figures I gather this is synthetic data with unnaturally low position noise, so this could give the reader the wrong impression.

c) Similarly, it is often unclear from the figures which strain is being used. For example the strain in Figure 4A-C is not labeled, but it appears to be the same as Figure 3A,B. But if that's the case its unclear why performance would be so much higher in Figure 4B than Figure 3B. Please label which strain is used in which figure subpanel throughout the manuscript, or provide a table.

d) Related: Figure 4A prominently displays "calcium imaging," when this is in fact a GFP strain. This misleads the reader

3) The work critically relies on reagents from other groups but could do a better job acknowledging those contributions:

a) The Neuropal strain is crucial to the manuscript and provides the majority of the ground-truth data starting with the Results and Figure 2, but Neuropal is first mentioned only towards the very end of the Results section and even then only in the context of Figure 6.

b) The strain list should reference publications for strains and alleles used.

c) Subsection “Cell annotation in gene expression pattern analysis” misleadingly states that "a reporter strain was crossed with pan neuronal red fluorescent protein" but this cross was not performed by the authors, it was performed by another group, published and is publicly available on CGC. This should be fixed.

4) More details are needed about the ground truth datasets, including the number of neurons hand-annotated in each of the 9 individuals and their spatial location. (Manual annotation of Neuropal is easiest at the periphery and hardest in center of the ganglia, and so it would be important to know coverage).

Reviewer #2:

Whole brain imaging in C. elegans allows us to monitor the activities of a large fraction of worm neurons during behaviors. However, the identity of each cell in the nerve ring remains largely unknown, prohibiting further analysis that integrates structural and functional information of the worm circuit. This problem has been partially amended by manual annotation from experts. However, this is a time-consuming and error-prone solution when one is dealing with a large dataset. We are enthusiastic about this manuscript because the authors take one important step towards automated annotation of neuronal identities. Methods in this work are innovative and attractive. By minimizing energy functions imposed by absolute coordinate differences (unary potential) between images and atlases, as well as differences of the pairwise relationship between neurons, the authors show that their CRF_ID model outperforms SOTA registration model in accuracy, speed, and robustness.

We would like to raise several main issues of this manuscript.

1) Writing. The main text of the manuscript is brief, dense, technical, and very difficult to understand. I skipped the main text and went directly to the Appendix. This arrangement is not wise for a general audience, especially biologists. In future revisions, please embed the figures in the text, which would save us a lot of time. Here are some specific suggestions:

a) The CRF framework can be better explained by building upon physical intuition. The mathematical notations sometimes only cause confusion. For example, is it necessary to introduce clique? I thought that every neuron in their graph model is adjacent to every other neuron. If this is not the case, please describe how the graph model is constructed. You find the note on maximum entropy model is out of the blue (subsection “Structured prediction framework”). If you want to make a deep connection with statistical physics, you better explain it well in the text!!

b) The motivation to build and how to build the data-driven atlases are dismissive in the main text. It is briefly mentioned in subsection “Identity assignment using intrinsic features in CRF_ID outperforms other methods”. But these sentences are extremely difficult to understand without reading the Appendix. The Appendix -- extended methods S1.7, however, needs to be revised and better explained. For example, the equations are not quite consistent, such as in Equations 6 and 25, and the notations are quite confusing. Linking some examples like Figure 2B to S1.7 will help understand the concept.

c) The prediction accuracies of the model vary from case to case. It was quite low in the scenario of missing neurons. The authors need to state clearly in their paper, under the worst scenario such as whole brain imaging without colors, the prediction accuracy of their methods. This information is now buried somewhere that is hard to find. The prediction accuracies of the CRF model, contingent upon different datasets and different noise levels, would better be a self-contained main figure, not in the supplements. To follow the logic flow of the text, the figure panels that compared CRF with other registration methods would better be introduced later.

2) Notations. As mentioned above, the symbol consistency is a problem. In the formulation of the model, λ's, trainable parameters in original CRF, have been abused. For the λ appearing in Equations 2/3/4/6/7/8/9/10/32/34/37/46, the author might consider making a clear statement that which of them are trainable and which are hyperparameters. If they are hyperparameters, the setting and tuning strategies need to be disclosed. Also, the keywords "identification" and "annotation" should be considered unified.

3) Loop Belief Algorithms, speed, and stability. The authors should provide details on the computational complexity and the stability of their algorithms and compare it to other registration methods. In their current graph model, does each trial converge and do they all converge to the same solution starting from different initial conditions? If not, how do the authors deal with the discrepancies? Likewise, the authors may want to comment on the memory usage for constructing the data-driven atlases to see if it can be another innovation point comparing to the registration methods.

4) Other missing information and explanations:

a) The authors should post the exact name and its settings of the registration models used for comparison.

b) In Appendix S1.2.1 Unary potentials – Positions along AP axis, as x-y is a 2D plane, we do not see why AP's is always better than LR's and DV's.

c) Following the explanation of generating synthetic data (subsection “Generating synthetic data for framework tuning and comparison 464 against other methods”) is a bit hard. The reason for changing the low bound to zero might need further illustrations. Could you please comment on why the prediction accuracy is much lower in synthetic data (Figure 2A)?

d) For subsection “Whole-brain data analysis”, the author might consider linking the paragraph to Figure 5, making 0.1Hz a reasonable choice.

e) For subsection “Whole-brain data analysis”, "[0.05, 0.05]" seems to be a mistake.

f) Subscripts in Equation 13 are wrong.

g) Providing more annotations and explanations on the meaning of the colors on some worm images (e.g., Figure 4D) would be helpful.

5) Codes on GitHub may need to be slimmed down.

Reviewer #3:

Linking individual neurons to their anatomical names is a vexing problem that limits efforts to determine patterns of gene expression and neuronal activity at the single-neuron level. Given the landmark Mind of the Worm paper (White et al., 1986) and subsequent analyses of its connectome, many imagine that annotating individual neurons in C. elegans is a solved problem. Unfortunately, it is not. This paper presents a computational method for solving this problem and, as such, has the potential to advance neurobiology in C. elegans. The approach could, in principle, be adapted to any nervous system from which a computational atlas could be derived following the pipeline laid out in this manuscript. There is much to recommend this study and many opportunities for improvement regarding the presentation of the computational method, its limitations and expectations for application, and for considerations of generalization to other nervous systems.

1) Explanation of the computational method

The computational strategy is difficult to follow in the main text, unless one reviews the appendices. We suggest elaborating the process using more generic terms in the main text. The following specific elements need clarification or additional support

- The mixed approach of considering intrinsic and extrinsic similarities between image and atlas is described in a manner that assumes readers are already familiar with this computational strategy. Given the breadth of the eLife readership, the authors would increase the accessibility and impact of the paper by providing readers with examples of what features are intrinsic and which are extrinsic in this case.

- The difference between this approach and previous strategies based on image registration is communicated clearly in the Appendix, but not in the main text.

- Much is made of the computational efficiency of the CRF_ID approach, but little is provided in the way of data or analysis supporting this claim. The authors could, for example, compare the computational energy/time needed for this approach compared to prior image matching approaches. They could discuss the nature of this computational framework compared to others with respect to computational efficiency.

Generality of the method

To better support the authors claim that this method is easily adaptable for any nervous system, please apply the framework to estimate the optimal number (and/or density) of landmarks as a fraction of the total number of nuclei or density in 3D. This would assist others in applying the framework to other simple nervous systems (e.g. Aplysia, leech, hydra). Additionally, it is not clear if the image stacks used to derive data-driven atlases are distinct from the data analyzed for prediction or whether the same data is used iteratively to build atlases and improve prediction accuracy.

Application of the method to C. elegans

Specifying the AP/DV/LR axes from raw data is not completely automatic but rather appears to require some user input based on prior knowledge. This is not stated clearly in the text. In addition, it is also not clear how the algorithm handles data from partially twisted worms (non-rigid rotation around the AP-axis). This problem is more likely to be encountered if the images capture the whole worm. Is it possible to allow rotation of the DV and LR axes at different points along the AP axis?

Specific suggestions for improvement are collected below.

(1) The method depends on the tidy segmentation of nuclei, but the segmentation strategy is not discussed nor is whether or not nuclear localization of landmarks or unknown markers is essential for accurate annotation.

(2) The authors need to explicitly inform readers that the markers in the NeuroPal strains (OH15495, OH15500) and the GT strains are localized to neuronal nuclei. Additionally, the authors need to address (1) whether or not nuclear localization is required for the annotation framework to succeed, and (2) discuss whether or not a cytoplasmic marker would be sufficient, and (3) provide more information on the segmentation algorithm used and recommended for use with the computational framework discuss.

(3) The authors use the AML5 strain as a proxy for GCaMP-labeled strains (subsection “Cell annotation in multi-cell functional imaging experiments”) to demonstrate the utility of the annotation tool for identifying cells used for calcium imaging. This strain differs from the NeuroPal strain expressing GCaMP is several respects that are not discussed by the authors, leaving readers to wonder about the utility of AML5 as a proxy and to question whether or not the success of cell identification in this strain is truly generalizable. Two main differences exist: (1) In AML5, GFP is expressed in both the nucleus and cytoplasm but in in OH15500 GCaMP6s is tagged with an NLS; (2) The basal fluorescence of GCaMP6s, but not GFP depends on basal calcium concentrations-this fact may introduce additional detection noise/variance into the annotation problem. The authors need to discuss how these differences affect (or don't) the ability to generalize from success with the proxy strain to success with NLS::GCaMP6s expression.

(4) Please clarify the nature of the output from the code that implements the framework. In other words, a reader should learn from the paper what kind of output file they might receive if they attempted to apply the tool to their own images (annotated image with top prediction candidate, data structure with all predictions and respective probabilities, etc).

(5) Terminology – There are a number of general computational terms and specific terms relevant to this problem that are not defined for the reader (listed below). Providing readers with implicit or explicit definitions of these terms will improve clarity.

5(a) "count noises" – used to represent variation in the number of nuclei detected in a given image stack, but not defined at first use. Please provide conditions under which the number of nuclei detected might vary along with defining this term. Additionally, this is a singular concept and should be written as "count noise" not "count noises" (by analogy to "shot noise").

5(b) There several other instances in which "noises" is used where "noise" is meant.

5(c) "intrinsic similarity" – which seems to represent pairwise positions in 3D in the image and the atlas.

5(d) "extrinsic similarity" – not clear.

(6) (Subsection “Identity assignment using intrinsic features in CRF_ID outperforms other methods”) "More importantly, automated annotation is unbiased and several orders of magnitude faster than manual annotation by researchers with no prior experience."

(a) Unbiased – It is a common misconception that computational strategies are unbiased. For this claim to be rigorously accurate, the authors would need to demonstrate that each and every nucleus was equally likely to be identified correctly by the automated annotation algorithm. For instance, it is easy to imagine that some nuclei, such as those closer to a landmark, are more likely to identified correctly and with less uncertainty than those further away. If this were true, then automated annotation has a systematic bias in favor of nuclei closer to landmarks and a systematic bias against nuclei further away from landmarks. And would, therefore be biased – even though no human supervision is involved. The authors should back this claim up with data or clarify that what they mean is that automated annotation is an improvement over (biased and subjective) human annotation.

(b) Faster -The authors are free to speculate about the relative speed of automated vs. manual annotation by an inexperienced researchers in the discussion. By writing this as a result, however, data are needed to back it up.

(7) (Materials and methods) From the description of how GT290 and GT298 were made, it seems that both constructs include 2x NLS fragments, but the genotype description under reagents lacks that annotation and most, if not all other references to this strain neglect to mention the NLS.

Presentation concerns that need attention: There are three instances of undisclosed data re-use among the figures that need to be addressed. (1) The image in Figure 4A is identical to the green channel of the image shown in Figure 3A; (2) Some of the data shown in Figure 2—figure supplement 4A – Part of the data shown here is also shown in Figure 2C; (3) Figure 4C – Please indicate if the same number of cells were removed in each run. Also, it appears that this data also may have been used in Figure 4—figure supplement 1. If so, please disclose data re-use.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Graphical-Model Framework for Automated Annotation of Cell Identities in Dense Cellular Images" for consideration by eLife. Your article has been reviewed by Ronald Calabrese as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

(1) The authors performed additional computational experiments by holding out some of the data used to create atlases – an important and general strategy for computational solutions that depend on real-world data. The authors present a comparison of this approach for reviewers, but not for explicitly for readers. These analyses and plots must be included in the final version main text.

(2) The authors should state clearly the computational speed of their algorithms and compare it with the registration methods. The inference and subsampling procedures (~ 1000 times?) on the data-driven atlas are time-consuming and computationally expensive.

Reviewer #2:

Main Text

(1) Thanks for sending us a much better written manuscript. The authors should consider replotting some of their figures, which can be difficult to read.

(a) The neuron names in Figure 2F and Figure 2—figure supplement 6C are difficult to read. Is there a new way to plot? When I wanted to zoom in to have a better understanding, they caused my Preview crashed multiple times…

(b) The meaning of the error bars throughout the manuscript are not well explained.

(2) The authors should state clearly the computational speed of their algorithms and compare it with the registration methods. The inference and subsampling procedures (~ 1000 times?) on the data-driven atlas are time-consuming and computationally expensive.

(3) Is there a way to make the data-driven atlas publicly available in addition to the raw annotated datasets (n=9)?

Rebuttal

(1) Pipeline (Major Point#6):

I do not quite understand the necessity of single or multi-run, which can be combined into one inference process. Consider the following scenario in a freely behaving animal. At one time, the region to be annotated consists of N neurons. At a different time, a new neuron (now N+1) is squeezed into the region. It is probably always true that the number of neurons in the data is different from that in the atlas.

(2) Color and Robustness and Evaluation Metrics (Essential revisions #1, #4, #6):

It seems that the leverage of color information for annotation is quite limited in the revised manuscript. The procedures for properly normalizing the color distribution are also complicated. I also found that the following sentence was incorrect. "Further, when leave-one-out atlases are used for both positional relationship and color (Author response image 2), the accuracy achieved by top labels is marginally greater than the accuracy achieved by using leave-one-out positional relationship only (Author response image 1)". It was actually significantly lower if I read the figures correctly. This leaves the question how we shall correctly assemble the data-driven atlas efficiently.

Reviewer #3:

The revision is very responsive to the summary and specific reviewers' critiques.

There remain some awkward phrasing and missing details to address. These are noted in order to make the text accessible to a broader audience and to increase the impact of the study both within and beyond the community of C. elegans researchers. These include:

(1). The use of the plural "noises" when the authors probably mean either "noise" in the singular e.g. ” Prediction accuracy is bound by position and count 316 noise in data”, replace "amount of various noises" with "amount of noise contributed from various sources". This latter example combines both the concept of the magnitude of noise and the diverse types of noise.

(2) Shorthand terms or jargon. For example, when the text reads "the position of cells AIBL" what is meant is "the position of the cell bodies of AIBL". Similarly, replace "neurons" with "neuronal cell body" or "neuronal somata".

(3) C. elegans strains – in response to critiques of the initial submission, the authors have clarified the origin of the transgenic strains used in the study. Thank you! Please also correct the reference to AML70 which is not included in the table of strains. Based on context, it looks like the authors are referring to AML32. Please ensure that this is corrected.

(4) Figure 5, panel E. Please refer to Figure 5—figure supplement 1 panel C noting the cells with non-zero weights in SPC1, SPC2, SPC3

(5) Figure 5 panel H: Indicate the origin of the motion trace shown. It appears to belong to one of the posterior cells shown in Panel F. Please provide a rationale for this choice – since the traces in Panel F certainly indicate that motion signals differ among cells.

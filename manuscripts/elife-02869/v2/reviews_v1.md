# Peer review - Round 1

Editors:
- Emmanouil T Dermitzakis, University of Geneva Medical School , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02869.022](https://doi.org/10.7554/eLife.02869.022)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Tumor Evolutionary Directed Graphs and the History of Chronic Lymphocytic Leukemia” for consideration at eLife. Your article has been favorably evaluated by Chris Ponting (Senior editor), a Reviewing editor, and 2 reviewers. The Reviewing editor has assembled the following comments to help you prepare a revised submission.

Overall, the reviewers found the work interesting but raised a number of concerns that need to be addressed regarding the analysis of the data as well as clarifications on the design and presentation of the work.

Major comments:

1) Relative timing of mutations: It is not entirely clear in the Materials and methods or main text exactly how the temporal order of mutations is inferred. At one point, mutations are described as 'present' or 'absent' on the basis of allele fraction >5% and compared across time points. Really, the only true method for inferring temporal ordering is through reconstruction of phylogenetic trees; this can be difficult from bulk sequencing data, but there are methods emerging to do this.

2) Copy-number adjusted allele fractions: On a similar note, it is not clear that the fraction of cells carrying a point mutation has been adjusted for the copy number at that locus. This is especially important for the TP53 point mutations when the other allele has undergone LOH. Also, how are double hits in a given gene dealt with in the graph method?

3) Rate of increase: The argument that later mutations show more rapid increase than earlier mutations is difficult to sustain on the basis of these data. The initiating lesion, by definition, will be present in all the tumor cells, and therefore cannot increase at the same magnitude as later mutations. Given that it is a prerequisite for entry into the study that the patient be diagnosed with CLL, one would imagine that, at that diagnostic time point, all the earliest mutations might already be clonal, and therefore will not change over time.

4) A question for another type of inference approach is: How do we know ground truth? The only way to know is if there were a set of samples from which there was frequent sampling, and if there were within clinical defined groups. Robustness of the network is dependent on how good the data is going in. While they do mention that they selected 70 samples for TEDG for which there were at least two sequential samples, in all likelihood, 2 samples are inadequate for defining the hierarchical relationships. There needs to be some table that provides information on the distribution of sequential samples per patient, and what types of time intervals between sequential samples. While a figure about the samples is provided as Figure 3–figure supplement 1, this is very hard to digest. This is a very very heterogeneous dataset, with 10 of 70 proceeding to Richters, more than half with treatment. A question is whether or not there are enough samples, by the time that one breaks down the patients into discrete clinical groups, to understand the hierarchical relationships.

Related to this, the numbers of samples are very confusing. This is what the reviewer understood: it seems that they start out with 202 patients, but only 70 had known highly recurrent drivers. 10 of the 70 had Richters Transformation, and how many have been excluded? By the time we get to Figure 4, there are 32 samples, but there is no discussion how this number came about. In general, in what percentage of sample was a polyclonal tumor population or a subclonal driver identified at the time of diagnosis?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Tumor Evolutionary Directed Graphs and the History of Chronic Lymphocytic Leukemia” for further consideration at eLife. Your revised article has been favorably evaluated by Chris Ponting (Senior editor), a member of the Board of Reviewing Editors, and the original two reviewers. The manuscript has been improved but there are two remaining major issues that will need to be addressed before acceptance, as outlined below. We have copied the exact wording of the reviewer to facilitate the response.

Major issues:

1) A major revision has been the addition of the concept of MCF. This was done to address the concern of adjusting for local copy number changes that could affect estimation of the clone size with a gene alteration. Unfortunately, the approach taken by the authors to calculate MCF seems not well defined. This reviewer is concerned that sampling error in VAF values might fluctuate above or below 0.5 in ways that have a large influence on the inferred MCF. No convincing data is presented by the authors to justify their novel and elaborate seeming approach. Several approaches for correcting mutation VAF values for tumor purity and somatic copy number changes have been described (e.g. Carter et al., 2012, Nat Biotech; Landau et al., 2013, Cell; Fischer et al., 2014, Cell Reports). Notably, these methods rely on analysis of germline heterozygous SNPs at the mutant locus to infer CN-LOH, which is a much more robust approach. Could the authors simply use one of these established (and principled) approaches? This would leverage their exome data more fully.

2) They rely on FISH analysis for estimations of trisomy 12 and deletions of various chromosomal regions. This is not accurate, as it is not possible to correct for purity when using FISH data. In addition, copy neutral LOH cannot be inferred from FISH.

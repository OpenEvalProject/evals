# Peer review - Round 1

Editors:
- William C Hahn, Dana-Farber Cancer Institue United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61082.sa1](https://doi.org/10.7554/eLife.61082.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The approach described in this manuscript provides a new method to analyze sequencing data, which will be of general use to the scientific community. In addition, this work identifies hypotheses concerning the etiology of certain cancers.

Decision letter after peer review:

Thank you for submitting your article "Supervised mutational signatures for obesity and other tissue-specific etiological factors in cancer" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Peter J Campbell (Reviewer #2); Elaine Mardis (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript by Tomasetti and colleagues describes a conceptually novel approach to derive somatic mutational signatures (SuperSigs) from whole exome tumor sequencing data using supervised machine-learning techniques. A large and growing number of mutational signatures have been described using non-negative matrix factorization (NMF), an unsupervised method. These signatures are widely used to describe the mutational processes operant in individual tumors and have spawned many studies examining environmental exposures and intrinsic genetic mechanisms that underlie these patterns. However, when accompanying clinical data are available, supervised learning may produce more informative signatures that correlate more strongly with environmental exposures, as well as enable the discovery of signatures associated with previously unappreciated factors. This work describes one such effort and using these methods, identify differences in penetrance of such signatures in a tissue restricted manner.

Essential revisions:

1) One weakness is the reliance on one dataset, and a highly curated, highly polished one at that. The authors used the TCGA data with random splits to training and test sets via a cross-validation design. The vast majority of the data studied was exome data, with only AML and ovarian cancers using whole genome data. A specific challenge of supervised machine learning techniques is that any hidden confounding factor in the dataset (say, hospital of origin, sequencing centre, variant calling) can be extracted as apparent signal for the variable of interest (say age, obesity) – a random test / training split on one dataset will still be subject to this confounding, since it operates at the level of the combined patients. The best way to avoid this (although it is not failsafe either) is to validate signal on external datasets.

We therefore recommend testing predictors trained on TCGA data but tested on external data. There is plenty of non-TCGA exome data available and accessible, and even reasonable amounts of whole genome data, with basic clinical variables (smoking, age, sex for sure; obesity more patchy) – this would give much greater confidence in the signals extracted.

2) The authors make reference to "partially-supervised signatures" in Figure 2A and in the text, claiming that they are "superior to" unsupervised signatures when clinically annotations are not available. This is confusing because SuperSigs is motivated by the advantage of supervised methods specifically for when clinical data are available. Moreover, I don't see any data presented in the Results to support the claim that partially-supervised signatures are better. While there is a detailed description in Materials and methods, more description and evidence should be included in the text, or else the paper should focus only on the scenario when clinical data are used.

3) The figures are generally unclear and need to be improved. For instance, Figure 2B attempts to show examples of randomly generated single peak signatures, but I am confused why there are multiple colored dots for each trinucleotide if there is only one signature per color. I believe the trinucleotide sequences are also incorrect, as the right half of the plots in 2B should have a T at the center of each trinucleotide, not C. Additionally, it is unclear in Figure 3 (panel B) which tumor types were chosen for the characterization of smoking signatures, and why. I also can't understand why smoking is shown again in panel c or why age is shown in panel d when the legend describes it as "all etiologic factors other than age".

4) The Introduction mentions a critique of unsupervised NMF signatures that they don't incorporate knowledge of exposures or their intensity (e.g., cigarettes packs/day). But it is not clear that SuperSigs explicitly models the intensity either. Samples are divided into two categories: "unexposed" and "exposed". Is the intensity of smoking exposure reflected in the smoking signatures from different tissues?

5) How many tumor types have a detectable smoking signature? How many tumor types were examined for a smoking signature? Figure 4 displays smoking signatures for pancreatic adenocarcinoma and bladder urothelial carcinoma, which are surprising given that these tissues do not have nearly as much direct exposure to the carcinogens in cigarette smoke as lung cancer, head and neck cancer, and esophageal cancer.

6) The authors fail to address the potential for overfitting. A strong test against overfitting would be to shuffle the labels and then re-run their entire framework from feature selection to test prediction. A clear sign the model is overfitting would be obtaining similar AUCs on the shuffled dataset to that of their unshuffled dataset.

7) AUCs as a metric for model performance can be deceiving; an H-measure would be more informative here see David J. Hands paper 2009 Machine Learning for more details.

8) The addition of performance metrics such as speed benchmarks for exome and WGS data sets is needed to assess the feasibility of implementation for end users. This is especially true considering the large number of bootstraps needs for feature engineering.

9) How does the novel feature engineering technique compare to state-of-the-art methods like sigLASSO? Does it take into account the transcript strand bias of genes?

10) Supervised learning depends on the quality of the data annotations, which as noted above are quite variable for different TCGA projects. In most instances, there are not quantitative information available to establish what age ranges were considered “young” vs. “old”, nor were there specifics around environmental exposures such as pack-years for smoking, ranges of BMI for obesity, etc. Could these please be specified and also some reference as to how these were selected, and were they selected prior to or after cross-validation was performed for the different categories?

11) The conclusions about SuperSigs algorithm performance compared to NMF seem to be based on core NMF rather than the improved versions from Alexandrov. The authors claim that it is not possible to use Alexandrov's implementation, however, offer no reason as to why. Please specify the NMF approach used in the Materials and methods so it is clear to readers.

12) The authors provide a strong rationale for the greater flexibility for mutational signatures beyond a three nucleotide fixed size improves their models' performance, but don't provide statistical analysis to support this.

13) Context of this publication with previous work. The aging signature is based on mutation counts, rather than rates. Does this not vary according to the tissue, based on the prior work published by this group? Is this another basic principle that could be addressed by comparing to SuperSigs analysis of pediatric cancer data?

14) The conclusions around obesity and tissue variance are overstated with respect to causality. Since these studies are observational, the authors cannot conclude evidence of causality.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your revised article "Supervised mutational signatures for obesity and other tissue-specific etiological factors in cancer" for consideration by eLife. Your revised article has been re-reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your revised submission has agreed to reveal their identity: Elaine Mardis (Reviewer #4).

As for the original submission, the reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

In this manuscript, the authors describe a new approach to identify patterns of genetic alterations in tumors that reflect biological processes that affect DNA. This approach does not use prior information and uses more sequence information to look for evidence of mutational processes. Among many interesting observations is the finding that certain mutational processes occasionally have different signatures across tissue types.

Essential Revisions:

1) The authors should revise the description of the methods to provide greater detail. One example of this is the last paragraph in subsection “Do mutational signatures add to prior knowledge about etiologic factors?”, where "information" is used extensively throughout, without ever really defining what type of information is being provided by SuperSigs.

2) Please provide a weblink for the TCGA Genomics Data Commons.

3) In subsection “Do mutational signatures add to prior knowledge about etiologic factors?” (and throughout), resist using "significantly" unless you have a p value that substantiates the term, and the test used to derive the p value.

4) In the Discussion, it is mentioned that SuperSigs associated with BRCA2 vary with tissue type (ostensibly meaning breast and ovarian) but only SuperSigs for breast cancer associated with BRCA2 is shown in Figure 4.

5) Discussion paragraph two is the first mention of inflammation, which is known to be linked to obesity yet is not specifically called out here.

6) In the same paragraph, both signature 4 and signature 6 are mentioned in terms of liver cancer but only signature 6 is explained as being “rare in liver cancers”. is it also the case that smoking is not associated with liver cancer, or…? Please edit this sentence so the reader understands why you are also mentioning the smoking signature result.

Reviewer #3:

This manuscript describes a conceptually novel approach to derive somatic mutational signatures (SuperSigs) from whole exome tumor sequencing data using supervised machine-learning techniques. A large and growing number of mutational signatures have been described (initially by Alexandrov et al) using non-negative matrix factorization (NMF), an unsupervised method. These signatures are widely used to describe the mutational processes operant in individual tumors and have spawned many studies examining environmental exposures and intrinsic genetic mechanisms that underlie these patterns. However, when accompanying clinical data are available, supervised learning may produce more informative signatures that correlate more strongly with environmental exposures, as well as enable the discovery of signatures associated with previously unappreciated factors.

This study is innovative, clearly written, and logically presents the benefits of supervised learning methods to identify signatures more strongly associated with meaningful clinical factors. The conceptual advantages of SuperSigs as an alternative to NMF-based signatures are compelling. Among many interesting observations is the finding that certain mutational processes occasionally have different signatures across tissue types. Given the ubiquity of mutational signatures in cancer genomics research and the challenge in connecting many signatures to their underlying cause, I think this study and the associated algorithm will be of broad interest.

Recommendations for the authors:

I am satisfied that the authors have sufficiently addressed the concerns raised in my original review.

Reviewer #4:

This manuscript describes an approach to uncovering mutational signatures and their associated causative factors, using a new approach that does not rely on NMF/unsupervised methods, which are in widespread use yet often yield complex or indeterminate underlying causes. The work takes advantage of publicly available TCGA genomic data and associated clinical data for 30 different cancer types, and utilizes the ICGC data to test their supervised approach to mutational signatures, or SuperSigs. Important results obtained by this approach include the observation that signatures of aging differ between different tissue types, perhaps linked to the underlying cell division rate differences that are well known to exist. Another important result is the derivation of two signatures related to obesity, which is emerging as the key contributor to cancer susceptibility in first world economies. Another major strength of this approach is that by first removing known etiological signatures such as smoking with SuperSigs, more refined signatures of underlying or associated etiologic factors may be revealed by a secondary NMF-based approach. This partially supervised method achieves higher concordance than by NMF only for all known etiologies (genetic and environmental) recorded in TCGA clinical data. Of necessity, this approach was tested with a large data set that left out the nuances of different tumor types. For example, breast cancers are well characterized into different subtypes, especially with respect to underlying factors such as BRCA1/2 mutation status (germline) that associate with the different subtypes (e.g. triple negative disease). As such, it remains to be seen whether this method may be more specifically applied to large genomic data sets across different subtypes and in the context of underlying genetic predispositions to further understand the susceptibility-based etiology of a specific tissue type. However, as a general method, SuperSigs provides a new and well-tested method for deriving mutational signatures from cancer genomic data that likely will have a significant impact on the field of cancer research and, ultimately in areas of cancer prevention as well as revealing new cancer etiologies.

Recommendations for the authors:

In general, the authors responded well to the critiques raised, including the ones I contributed. I was pleased they were able to utilize the ICGC data and to show the method transferred well to the analysis of these data. It would be a good idea for the figure they produced in the response to reviewers to be included as a supplementary figure in the revised manuscript, if possible.

The figures are all quite improved, although the use of colors to help differentiate different tumor types and different etiologies sometimes is challenging to decode. This will likely be helped by preparation for publication. My only remaining critique is the language used to quantify the SuperSigs improvements over NMF are sometimes poorly quantitative. One great example of this is the last paragraph in subsection “Do mutational signatures add to prior knowledge about etiologic factors?”, where "information" is used extensively throughout, without ever really defining what type of information is being provided by SuperSigs. This needs to be edited accordingly. Please provide a weblink for the TCGA Genomics Data Commons. In subsection “Do mutational signatures add to prior knowledge about etiologic factors?” (and throughout), resist using "significantly" unless you have a p value that substantiates the term, and the test used to derive the p value. This is standard. In the Discussion section, there are two areas of confusion for me. In the Discussion, it is mentioned that SuperSigs associated with BRCA2 vary with tissue type (ostensibly meaning breast and ovarian) but I only found a SuperSigs for breast cancer associated with BRCA2 in Figure 4. This is a very important observation, so please be certain it is presented for both tissues in an accessible way in the main text. Discussion paragraph two is the first mention of inflammation, which is known to be linked to obesity yet is not specifically called out here. If this is indeed the inference being made, please be more explicit so the reader understands the importance of this conclusion! In the same paragraph, both signature 4 and signature 6 are mentioned in terms of liver cancer but only signature 6 is explained as being “rare in liver cancers”. is it also the case that smoking is not associated with liver cancer, or…? Please edit this sentence so the reader understands why you are also mentioning the smoking signature result.

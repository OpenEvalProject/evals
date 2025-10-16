# Peer review - Round 1

Editors:
- Matthew Stephens, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75600.sa0](https://doi.org/10.7554/eLife.75600.sa0)

The paper describes a novel neural-network-based strategy for imputing unmeasured genotypes, which is a standard part of most association testing pipelines. The method is computationally intensive to train, but once training is complete the imputation is fast and accurate and does not require further access to a reference panel. It has the potential to be a practically-appealing alternative to existing methods. although further work (eg training of models) is required before this new approach can be applied genome-wide.


---

# Peer review - Round 1

Editors:
- Matthew Stephens, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75600.sa1](https://doi.org/10.7554/eLife.75600.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Rapid, Reference-Free Human Genotype Imputation with Denoising Autoencoders" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Molly Przeworski as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) More precise technical details need to be provided about the method. Code used to train the method should be made available.

2) Accuracy assessments should be made on a new dataset not used at any point in the training.

3) Comparison with HMM should use a more diverse reference panel and with standard quality controls in place, with separate comparisons for rare vs common variants.

4) The reason for the surprisingly low average accuracy of all methods, compared with

previous studies, needs to be identified and, probably, corrected. (Reported imputation accuracies in previous studies are typically R2>0.8, whereas in this paper reported R2 is mostly in range 0.2-0.6).

5) Software for applying the pre-trained network to impute genotypes needs to be publicly available.

Reviewer #1 (Recommendations for the authors):

Supplemental Figures 12 and 13 – I appreciate the authors using various metrics for comparing imputation accuracies, but I think these figures are a bit confusing because it shows that SNPs with smaller MAF somehow have better imputation accuracy.

Reviewer #2 (Recommendations for the authors):

Two particular concerns for the authors:

1) The code is not yet available. Once it is made available I'll be able to more thoroughly evaluate what the authors have done.

2) As mentioned above, there is a bit of work to do on cleaning up the run time performance evaluations.

Reviewer #3 (Recommendations for the authors):

Besides the points mentioned in the public review, I have the following comments/suggestions:

– While I am somewhat familiar with autoencoders, I found it quite hard to follow the description of "denoising" autoencoders. Part of the problem was that I did not appreciate that these are different from a regular autoencoder until I did a bit more reading. I'm not quite sure how to make the description more accessible to the audience who are not familiar with denoising autoencoders, but I think it would have helped me to have an equation giving the training objective function that is being optimized to supplement Figure 1.

– The description of the HMM methods on p3 is inaccurate. For example, the hidden states are not the "to-be-imputed" variants (a better high-level description would be that the hidden states represent the haplotype in the reference panel that is most closely related to the haplotype being imputed, although different HMMs may have slightly different interpretations for the hidden states) and the genotyped variants are not the "observed states" (they are observed, but they are not the HMM states). In any case it needs rewriting.

– p4 the analogy with single-cell "dropout" is misleading because the zeros in single cell data are not "missing data" in the same sense as the missing genotypes in genotype imputation. (See https://www.nature.com/articles/s41588-021-00873-4 for example).

– p6: although ultimately performance is what matters, the genotype encoding seems a bit weird to me: specifically the way that 0 is used for both missing data and absence of the allele (which are different things!) Is this standard in the denoising autoencoder literature? Also, can you clarify what you mean by "scaled outputs can also be regarded as probabilities" and "This representation maintains the interdepencies among classes". Indeed, I don't see why this last is true: for example, the "true" genotype can never be (0,0), so if one of the pair is 0 the other must be 1, and this interdependency does not seem to be captured by the encoding.

Reviewer #4 (Recommendations for the authors):

Specific comments are given below.

1. The authors trained their models using HRC reference panel, which consists of predominantly European ancestry individuals. They didn't mention the reference panel used in HMM-based imputations, and I assume it was also HRC. As we know, performance of HMM-based imputation depends on the reference panels. There are larger and more diverse reference panels publicly available (e.g. TOPMed freeze 8 reference panel through the TOPMed imputation server). Does AE still have values (whatever training datasets they are using) over the TOPMed imputation server? Evaluations with diverse reference panel is particularly important for at least two reasons: (1) diverse panels are widely used (if not the most widely used); (2) AE relies more on pretrained model that no longer retains individual haplotype level information than HMM-based methods, which is conceptually susceptible to heterogeneity in reference panel. The authors may not have access to individual-level TOPMed data for training their AE models. In that case, they should at least evaluate the performance with the 1000 Genomes Project as reference.

2. The authors didn't mention any post-imputation QC steps, thus it's not clear to me which variants are included in their evaluations/comparisons. As we know, not all markers attempted (that is, markers in the reference panel) can be well imputed. It is essential to have post-imputation QC to filter out poorly imputed markers. The manuscript does not touch this important topic at all, rendering the method practically not useful. Also rather puzzlingly, the R2 showed in all the figures are largely in the range 0.2-0.6, which is inconsistent from what's reported in the literature. For common variants, HMM-based imputation methods have been reported to attain R2 > 0.8 (if not even much higher); and for rare variants, the mode is close to zero. The expected bimodal distribution is not observed. Please clarify. For similar reason, quality assessment should be performed for common and rare variants separately.

3. Have the authors evaluated the computationally identified hotspots? Are they largely consistent with the "true" recombination hotspots? Based on Figure 1E, these hotspots are calculated according to LD. What if the reference panel contains diverse populations? The LD calculated based on heterogeneous individuals would be meaningless.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rapid, Reference-Free Human Genotype Imputation with Denoising Autoencoders" for further consideration by eLife. Your revised article has been evaluated by two of the original Reviewers, Molly Przeworski (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. You need to clearly report the (very considerable) training time required for the autoencoder. This relates to comments from both Reviewers which I repeat here:

Reviewer 2: "I don't think the authors are dealing enough with performance issues and the need to share training times for tuning. First, in the revision the authors have edited/added Figure 6 which shows a runtime comparison, however, the methods section description (lines 308-315) does not mention how only prediction time was taken into account, as the authors seem to be explaining in the Response to Reviews document. More importantly, given that software release is mostly a proof of principle- pre-trained models are available for chr22 only -further, genome-wide inference a user would have to (as I understand it): download a reference set, train tiled auto-encoders for the genome on their own hardware, and then do inference on their data of interest. Surely then it's important to profile the performance of this bit of the pipeline for the user."

Reviewer 4. That "the training process is going to take approximately one year to finish." would severely limit the application of the method. If the authors, as developers, do not release pre-trained models, we would be relying on extremely motivated and computationally savvy users to perform the pre-training. Along the line, reporting only the inference speed (i.e., computing time needed to APPLY the pre-trained models) becomes insufficient since the users would need to pre-train the models for all other chromosomes before they can apply the models to their target data.

2. You need to address the original request to compare against HMMs from a diverse reference. This request was made in the original decision, but the response instead focussed on the diversity of the target samples, which is a different issue. (It seems that running the autoencoder with a new diverse reference sample would require considerable new computation, but running the HMMs with a more diverse reference should be relatively straightforward; this does seem to highlight a disadvantage of the long training time of autoencoders if they are to be retrained when new larger reference samples become available.)

This relates to the following comment from Reviewer 4:

For major comment 1, I was not referring to a diverse target but referred to a diverse reference. I know that HRC includes the samples from the 1000 Genomes Project but the aggressive variant filtering and the predominant European ancestry individuals (~30,000 versus ~2,000 non-European from the 1000 Genomes Project) make it a lousy example as a diverse reference.

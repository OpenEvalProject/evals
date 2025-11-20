# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.106818.3.sa0](https://doi.org/10.7554/eLife.106818.3.sa0)

This useful study attempts to place an ancient maize sample from Bolivia, dated to the end of the Incan empire, in genetic and geographical context. The analyses show that this sample is most closely related to ancient Peruvian maize, but the data remain inadequate to determine the direction of dispersal and the extent of Inca influence over the genetic make up of the analyzed sample. There are additional deficiencies in the statistical analyses and selection inferences. The topic of the study would appeal to researchers studying maize dispersal and adaptation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106818.3.sa1](https://doi.org/10.7554/eLife.106818.3.sa1)

Summary:

In this manuscript, authors describe a good quality ancient maize genome from 15th century Boliva and try to link the genome characteristics to Inca influence. Overall, the revised manuscript is still below the standard in the field. While dating of the sample and the authentication of ancient DNA has been evidenced robustly, the downstream genetic analyses do not support the conclusion that genomic changes can be attributed to Inca influence. There is more story telling than story testing in this manuscript, analyses are not robust and possibly of very narrow interest.

Strengths:

Technical data related to the maize sample are robust. Radiocarbon dating strongly evidenced sample age, estimated to around 1474 AD. Authentication of ancient DNA has been done robustly. Spontaneous C-to-T substations which are present in all ancient DNA are visible in reported sample with the expected pattern. Despite low fraction of C-to-T at the 1st base, this number could be consistent with cool and dry climate in which the sample was preserved. The distribution of DNA fragment sizes is consistent with expectations for sample of this age.

Weaknesses:

(1) The geographic placement of the sample based on genetic data is not robust. To make use of the method correctly, it would be necessary to validate that genetic samples in this region follow the assumption of the 'isolation-by-distance' with dense sampling, which has not been done. Without this important information, we do not know if genetic similarity is influenced by demographic events and/or selection. The analysis is not a robust evidence of sample connectivity.

(2) The conclusion that Ancient Andean maize is genetically similar to European varieties and hence share similar evolutionary history is not well supported. PCA plot in Fig. 4 merely represents sample similarity based on two components (jointly responsible for about 20% of variation explained). Contrary to authors' conclusion, the direct test of similarity using outgroup f3 statistic does not support that European varieties are particularly closely related to ancient Andean maize. These levels of shared drift could be due ancient Andean maize relationship with other related groups, such as ancient or modern Brazil. A relationship test between multiple populations would be necessary to show significant direct relationship between ancient Andean maize and European maize.

(3) The conclusion that selection detected in aBM sample is due to Inca influence has no support. Firstly, selection signature can be due to environmental or any other factors. To disentangle those, authors would need to generate the data for a large number of samples from similar cultural context and from a wide-ranging environmental context followed by a formal statistical test. Secondly, allele frequency increase can be attributed to selection or demographic processes, and alone is not a sufficient evidence for selection. Presented XP-EHH method seems unsuitable for single individual. Overall, methods used in this paper raise some concerns: (i) how accurate are allele-frequency tests of selection when only single individual is used as a proxy for a whole population, (ii) the significance threshold has been arbitrary fixed to an absolute number based on other studies, but the standard is to use, for example, top fifth percentile.

In sum, this manuscript presents new data that seem to be of high quality, but the analyses are frequently inappropriate and/or over-interpreted.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106818.3.sa2](https://doi.org/10.7554/eLife.106818.3.sa2)

I am glad to see a revised version of the manuscript. The authors have successfully handled some of my comments, but others require additional attention. In particular, the dataset seems quite robust and valuable to publish, and the descriptive analysis of its position relative to other modern and ancient genomes is generally sound. The selection analyses remain unsupported, and should be removed from the paper. In addition, I agree with the other reviewers and reiterate my comment that the Locator analysis is not robust.

As I said in my original review, the XP-EHH method is not applicable to pseudohaploid variant calls in a single individual. This method is simply not appropriate to apply to the data at hand, as the method relies on knowledge of diploid genotypes, usually phased, and the results from this test are not robust. It is possible that the XP-EHH method could be extended to this data type or genotype likelihoods with extensive validation and conditioning on a large reference panel, but in general haplotype-based approaches have not been extensible to low-coverage pseudohaplotype datasets. At any rate, any off-the-shelf implementation is inappropriate and unsupported. I am sorry to be this negative about this analysis, but it cannot be used as presented, the results from using it in this way would be spurious by definition.

In addition, identifying GO terms without statistical assessment of enrichment is not a robust analysis, nor is selecting genes with a high proportion of rare alleles without extensive additional contextualization based on the expectations of neutrality and deviations potentially tied to selection. For this reason, the two genes linked with height traits have no support here as genuinely being targets of selection. It is a frustrating reality for us in the ancient DNA field that small numbers of highly degraded genomes offer extremely limited scope for selection analyses, but that's the unfortunate state of play, and is the situation here.

My other major critique remains the application of the Locator method. As Reviewer 1 notes, this method must be built on a densely sampled dataset with strong isolation by distance, which is not done here. The authors explained their approach with more detail in their response, but it is fundamentally inappropriate for this dataset. It does not add anything more than the f3 analysis, and creates a falsely precise inference of genetic-geographic origins that is not supported.

Per authors' response to my previous recommendation 6, it is not advisable to re-map the reads after damage masking, and doing this with a conservative hard-masking approach will lead to a high mismatch rate and significant loss of reads in BWA. This could also exacerbate reference sequence bias which is already a major challenge for ancient DNA (see Gunther et al 2019 PLoS Genet). The correct approach is to map reads, mask or rescale for damage, and then proceed with the modified alignment file. In response to Reviewer 3's comment 3, the authors also refer to a "0 mismatch alignment" strategy. This is not concordant with the damage analysis, and if they truly do not allow mismatches this would be very inadvisable, as it would allow an extreme reference sequence bias.

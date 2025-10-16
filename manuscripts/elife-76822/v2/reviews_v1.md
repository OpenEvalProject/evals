# Peer review - Round 1

Editors:
- Deborah Bourc'his, https://ror.org/04t0gwh46 Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76822.sa0](https://doi.org/10.7554/eLife.76822.sa0)

Retrotransposons undergo massive reprogramming of their methylation states during germ cell development, but some elements are immune to this remodeling. This manuscript explores the contribution of binding motifs for KRAB-Zinc Finger Proteins (KZFPs) and position towards genes to explain the variable methylation dynamics of different retrotransposon families, namely L1, SVA and LTR12, as well as potential inter-individual variation during male germ cell development in humans, using an integrative analyses of available sequencing datasets. By bringing insights into the complex regulation of retrotransposons, it could be of particular interest to the epigenetics community.


---

# Peer review - Round 1

Editors:
- Deborah Bourc'his, https://ror.org/04t0gwh46 Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76822.sa1](https://doi.org/10.7554/eLife.76822.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Transcriptional states of retroelement-inserted regions and specific KRAB zinc finger protein association are correlated with DNA methylation of retroelements in human male germ cells" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Michael Imbeault (Reviewer #1); Geoffrey Faulkner (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers agreed the study was well conducted and although was initially done on a limited number of available samples, the important observation regarding the inter-individual variability of SVA methylation in sperm was replicated in an additional dataset with more donors and further confirmed by targeted amplicon sequencing. The conclusions regarding the DNA methylation dependency towards specific KZFPs is not novel, although it was extended here to the context of primordial germ cells. The most intriguing conclusion is certainly the description of inter-individual differences in SVA methylation in the sperm of different donors. A link with being positioned inside a highly transcribed gene and in reverse orientation towards the host gene was drawn regarding the propensity of being methylated for an SVA, but the explanation for this is very uncertain. Results appear as preliminary on this matter.

Please address the following points in a revised version of your manuscript, and answer the individual comments and questions raised by the reviewers in a detailed rebuttal letter, with possible corrections and additional figures to be included in the manuscript.

1 – Integrate all the KZFP datasets that are available in GSE120539 (but that were not published) in your analysis

2 – Is it know whether interindividual differences in SVA methylation are also found in somatic tissues, or is it a specific feature of sperm DNA? If this has not been described, please analyze available WGBS datasets focusing on one tissue of several donors, or use your amplicon sequencing strategy. This would be an important addition to the biological meaning of such differences, whether this variability also occurs during embryonic reprogramming, not only germ cell reprogramming.

3 – Provide more information as to the methodology for full length retroelement analysis and ages of sperm donors

4 – Please show screen shots of individual loci that follow the stated correlation of DNA methylation and KZFP binding

5 – Review all sentences with over statements, as outlined by reviewer #1.

Additionally, please correct the following points:

– Line 304: "… subsequently, MIWI2-interacting protein SPOCD1 recruits the chromatin remodeling complex DNMT3A and DNMT3L to…". This sentence is wrong twice: (1) DNMT3A-DNMT3L does not have chromatin remodeling ability per se, it is a de novo DNA methylation complex, and (2) DNMT3C methylates piRNA-targeted retroelements in mice, not DNMT3A (see Barau et al., 2016). Please correct as you are referring here to the process that has been described in mice.

– The link between intragenic position of SVAs and their ability to undergo methylation by transcriptional readthrough/H3K36 methylation is interesting, as it means it would happen in a piRNA-independent manner. However, it does not explain why only the SVA elements with a reverse orientation to the host gene would be affected. Please report this.

Reviewer #1 (Recommendations for the authors):

I am a researcher active in the field of KRAB zinc finger proteins for about 12 years. In my opinion, the science in this manuscript is high quality and the findings as novel as they are interesting.

I have a few small recommendations to improve some sections of the manuscript and would appreciate if they can be implemented before publication.

Early in the manuscript it is stated that "we focused on full-length copies of retroelements to analyze 85 DNA methylation for at least 30 copies.". What did you consider as 'full-length', especially for LTR-containing retroviruses? Did you analyze only copies containing the internal part, discarding solo-LTRs? I could not find details describing this in the methods section. Also, this decision is probably biasing the analysis toward younger elements – not a problem in itself, but it should be stated clearly.

With very young elements (L1Hs) the mappability is probably not very good with 100bp non-paired end reads. Could you provide a supplemental table with average mappability per family of transposons, or as a supplemental figure as a violinplot of mappability per family.

There's more data of KZFP that is available that was not included – notably at GEO accession GSE120539 from the Trono lab – these are from the same experimental series as the ones published initially but didn't make it through analysis before publication – it would be great if you can include them.

For figure 2, I would like to see statistics of enrichment (p-value) for overlaps with specific KZFPs / families of transposons and DNA methylation categories.

Figure 2A – a heatmap is not the best visualization here – it could be a simple sorted barchart of hits zoomed in on the first few members with the highest scores. Same comment for figure 3H.

Review all sentences that are related to conclusions to avoid overly strong wording, considering that most findings of this manuscript are purely correlative and causation has not been demonstrated. As an example (out of many): "Therefore, SVAs are methylated during spermatogenesis if these are inserted into actively transcribed genes." – this is too strong, you might want to add 'suggest, might, potentially'.

Please discuss somewhere in the manuscript the potential for multiple KZFPs binding the same elements having a concerted effect on the elements.

Finally, I would like to see the age distribution of the sperm donors, and some analysis to see if variability is correlating with age in any way.

Reviewer #2 (Recommendations for the authors):

My two major reservations are the claims around inter-individual variability being difficult to distinguish from technical variablity, which I don't have a reasonable suggestion for how to address, and the first specific point above, namely that uniquely mapped WGBS reads are unlikely to measure methylation in the core VNTR region of an SVA (or the L1HS 5'UTR CpG island). The authors could address this point by showing a composite profile of WGBS coverage and methylation levels compared to L1/SVA consensus sequences, showing the inner parts of L1 and SVA. They could also show examples of individual loci that follow the stated patterns of DNA methylation and ZFP binding that supports a correlation between the two. Another option would be to do nanopore long-read sequencing, which obviously would take time and substantial resources, but would provide a comprehensive picture of the situation. Note that this issue affects some of the more high profile mouse retrotransposons, such as IAP, to a much lesser degree because their LTRs are more accessible to WGBS.

I think the figure legends for Figure 2E and Figure 2F are swapped.

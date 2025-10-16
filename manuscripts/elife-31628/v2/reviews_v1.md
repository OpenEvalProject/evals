# Peer review - Round 1

Editors:
- David Baulcombe, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31628.040](https://doi.org/10.7554/eLife.31628.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The genome of Trichoplusia ni, an agricultural pest and novel model for small RNA biology" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Diethard Tautz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Julius Brennecke (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper presents a draft assembly of the genome of the destructive lepidopteran insect pest, Trichoplusia ni, and it derives a number of interesting and important features of both the coding and non-coding parts of the genome.

There is a relatively (to the second part of the paper) brief description of gene orthology based on a comparison with an Arthropoda dataset with reference to the opsin gene family, genes associated with sex determination and an analysis of Z chromosome dosage compensation associated with sex determination. There is novelty in the W chromosome sequence that is not available for other Lepidoptera although its enrichment for repeats and gene depletion is apparently similar in other members of that order.

The structural features of the genome (telomeres, absence of well-defined centromeres, heterochromatin) are well documented as are the transposons and repeats.

Added to this standard genome analysis there is a lengthy description of the small RNAome including the miRNAs, viral and other siRNAs (that are surprisingly not 2'-O methylated and piRNAs and the piRNA proteins. The T. ni pathway is revealed as a variation on other piRNA pathways including the presence of both dual and uni-strand piRNA clusters, a large cluster accounting for most if not all of the W chromosome. This description is coupled to a lengthy description of the expression pattern of the various piRNA-producing regions, including suppression of splicing. There is also a description of genome editing coupled to single cloning of mutant cultured cells in the Pi pathway ciwi gene and a transient assay system showing that the piRNA pathway protein Vasa is in perinuclear nuages, as in Drosphila.

Required Revisions:

1) Figure 1, Table1 and Supplementary file 1 genome assembly statistics, are the numbers of reads and fold coverage relating to the sequencing from mainly Hi5 cells genomic DNA, or do they also include sequencing reads from the male and female pupae? The authors note the very fragmented assemblies and short N50 from the pupae genomic DNA, and the impression received is that these reads were mainly useful in determining which of the scaffolds correspond to W, Z sex chromosomes versus the autosomes. Although the vast majority of the pupae reads map to the T. ni genome assembly, were they sufficient to confirm that the higher-level scaffold order within the de-novo assembled chromosomes in the Hi5 cell genome is the same as in T. ni pupae? We think this distinction is important, and the text and paper title should clarify that this high-quality genome assembly is mainly based off the T. ni Hi5 cell genome. It would be useful to comment on whether the Hi5 cell for the genome assembly was derived from expansion of a single clone, and if not, how does their pipeline handle the tetraploidy/karyotype variability from a mixed cell population?

2) Can the authors comment on whether T. ni miRNAs vs. siRNAs also partition into which of the two Ago/Dcr proteins like in Drosophila? When T. ni Ago2/Dcr2 are compared to Drosophila Ago2/Dcr2, are there differences in the alignment that would yield insight into lack of 2OMe in the siRNAs, perhaps differences in the Ago2 PAZ domain?

3) The authors claim that the 'Entire' W chromosome is a giant piRNA cluster, but is every base on W truly covered by sequenced piRNAs? Are all the few protein-coding genes on W also generating piRNAs? Since many miRNA loci were also mapped to W, are these loci also generating piRNAs at the same time? If not, then perhaps revise as "nearly the entire W chromosome".

4) How thorough is the CRISPR knockout of ciwi – do the modified/selected Hi5 cells show piRNA depletion despite the presence of the remaining unmodified genomic copy in Figure 7D? How stable is this modification in subsequent propagation of the Ciwi-modified hi5 cells? The image of the mCherry-tagged Ciwi in Figure 7—figure supplement 1 is very fuzzy and unlike the sharper images of the eGFP-tagged Vasa cells. Have the authors confirmed by genomic PCR and sequencing that the mCherry is inserted into the Ciwi locus like their data showing eGFP inserted into the Vasa locus? The concern stems from the literature describing efficient DNA repair/recombination mechanisms in lepidopteran cells like BmN4, and this may lend to challenges in genome editing. Could the tetraploidy of Hi5 cells cause issues in achieving complete knock out of genes with Cas9 and single-cell cloning? Can RNAi be performed to knockdown gene expression in Hi5 cells like BmN4 cells, which the Kirano and Siomi labs can do with a prolonged and repeated dsRNA treatment protocol?

5) The authors nicely show TNCL virus-mapping siRNAs, but are there also TNCL piRNAs, such as virus-derived piRNAs observed in mosquito cells? Are there piRNA clusters that map to the 3'UTR of protein-coding genes as seen in other animals?

6) We understand the nomenclature history for Piwi genes using animal colloquial names (mouse miwi, human hiwi, chicken chiwi) but one may worry that ciwi cabbage looper piwi will be confused with cat piwi, cow piwi, and camel piwi. We suggest TnPiwi, the more scalable naming convention that the authors used for TnAgo3 (like BmAgo3, DmAgo3).

7) In the second paragraph of the Introduction and in the second paragraph of the subsection “Genome-editing and single-cell cloning of Hi5 cells”, the authors state BmN4 cells are difficult to grow, but I believe this statement is incorrect because many labs have used these cells, and the Tomari lab can grow sufficient BmN4 cells to purify Siwi for piRNA biochemical studies, so I would presume these cells are straightforward to grow. Please comment.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The genome of the Hi5 germ cell line from Trichoplusia ni, an agricultural pest and novel model for small RNA biology" for further consideration at eLife. Your revised article has been favorably evaluated by Diethard Tautz (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) This revision still includes this Figure 7—figure supplement 1 and text in the fifth paragraph of the subsection “Genome-editing and single-cell cloning of Hi5 cells”. The mCherry data is also tied to the text describing single-cell cloning and Figure 8A. If the authors remove the mCherry data, how will this impact the description of single-cell cloning, and the manuscript revision is still unclear if the EGFP-HA-vasa cells were isolated via this single-cell cloning? The text says EGFP-positive cells are detected one week after Cas9/sgRNA/ssDNA transfection, but single cell sorting/growth requires at least 2 weeks, and there is no detail on whether EGFP-HA-Vasa required this 3-week regimen?

2) From author rebuttal: "We have demonstrated that we can make genomic deletions, we have not yet knocked out all four copies of a gene. The most likely explanation for this is that in the absence of all Ago3 or Ciwi, Hi5 cells are inviable. We are actively working to develop protocols to knockout all four copies of a gene, but these methods will take time to test."

This explanation would be valuable to include in the manuscript itself, either in Results or in the Discussion, to clarify why the WT band remains in the δ lane of Figure 7B. Also in Figure 7A and 7C, the prime characters in 5' and 3' are not rendering correctly in this revision PDF or print?

3) Citations are still missing in the first paragraph of the Introduction [cauliflower, prolonged culture] and in the first paragraph of the subsection “Genome sequencing and assembly” [tetraploid]. Also, additional EndNote formatting issues in the subsection “piRNA pathway proteins”, #77489?

4) We are glad the authors agree to using TnPiwi, and with regards to the rebuttal, we also note the challenge of pronouncing "ciwi" differently from Bombyx Siwi (not /k/iwi?). Nevertheless, this raises another question as to why in Supplementary file 2B TnPiwi is ascribed to the Drosophila homolog Aubergine rather than Piwi, if the authors note they do not know if TnPiwi functions more like Aub or Piwi? Is Supplementary file 2B reflecting more closely related protein sequence between TnPiwi and Aub versus Piwi? TnAub?

# Peer review - Round 1

Editors:
- Martha L Bulyk, Dana-Farber Cancer Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54919.sa1](https://doi.org/10.7554/eLife.54919.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your revised manuscript addresses the reviewers' prior concerns. We anticipate your new TRACE-Seq method will be of interest to readers as an efficient, lower cost alternative to traditional library construction methods for RNA-Seq.

Decision letter after peer review:

Thank you for sending your article entitled "Transposase assisted tagmentation of RNA/DNA hybrid duplexes" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor.

As noted in our prior communications about the competing study that has now been published in PNAS, please be sure to mention that published study appropriately in your revised manuscript and to cite it in the main text.

Also, with regard to the name of your method, I agree with reviewer #1 that ATRAC-Seq does not make sense as an abbreviation and may be confused with ATAC-Seq, and recommend naming it something else.

Reviewer #1:

In Lu et al. the authors describe a strategy for producing RNA-seq libraries by the direct tagmentation of RNA-DNA hybrids. This method "ATRAC-seq" is very similar to "SHERRY" recently published in PNAS ("RNA sequencing by direct tagmentation of RNA/DNA hybrids") relying on what appears to be transposition activity of the Tn5 transposase into RNA/DNA hybrids. Overall the paper does a good job characterizing the RNA-seq libraries; however, like the PNAS publication, the authors do not have any experiments that explicitly test the RNA/DNA transposition efficiency. Neither the published work or the manuscript presented here take into account the various efficiencies of RT enzymes / mixes to produce dsDNA, varying based on the RNase H efficiency. It is worth noting that this is irrelevant for producing a simplified assay – it does not matter if the Tn5 is inserting into dsDNA product after the first strand synthesis or to the RNA/DNA hybrids, as both produce a simplified workflow for producing RNA-seq libraries. The issue is that any publication claiming this phenomenon without direct evidence in a controlled setting could result in misguided assumptions to the field. A properly controlled test would eliminate the RT component and directly assess hybrid constructs where no dsDNA is possible. It may be that the efficiency is high, which drives this result and not the dsDNA after RT; however, it needs to be directly demonstrated.

Other than the RNA-DNA transposition assumptions, the rest of the manuscript is a test of the RNA-seq libraries that were generated when compared to standard techniques, which are fairly standard and properly assessed.

Reviewer #2:

The manuscript "Transposase assisted tagmentation of RNA/DNA hybrid duplexes" by Lu et al. describes a new approach involving direct tagmentation of RNA/DNA heteroduplexes for a "one tube" mRNA-seq library preparation protocol called ATRAC-seq. Involving fewer steps, this workflow is allowing the generation of transcriptomics data with a seemingly similar quality as a conventional RNA-seq workflow and is reportedly faster and cheaper.

Indeed, as a novel approach, direct tagmentation of RNA/DNA hybrids looks very interesting and can potentially provide new grounds for improving a number of existing RNA-seq protocols allowing to bypass the second strand synthesis step.

The major concern, however, is the novelty of this work. A paper describing very similar results and a comparable transcriptomics approach have just been published recently as a peer-review article (Da et al., PNAS) and last November 2019 as a preprint. Importantly, some authors from the current Lu et al. work seem to be affiliated with the same departments as the co-authors on Da et al., namely the Tsinghua-Peking Center for Life Sciences and College of Chemistry and Molecular Engineering, Peking University. This might be considered as merely an unlucky coincidence, but the overall similarity of the two works is truly puzzling and thus suggests this might not be the case. It involves obvious parallels in the overall flow of the manuscript and its structure: 1) rationale for attempting the tagmentation of hybrids with Tn5; 2) experimental approach; 3) workflow for mRNA-seq benchmarking; 4) figure layouts look (i.e. Figure 1 in both works show protein domain structure similarity between RNAse H superfamily members). The actual RNA-seq method ATRAC-seq described by the authors is apparently identical to SHERRY from Da et al., with slight variations such as the enzyme (Superscript II vs Superscript IV; Bst2 vs Bst3) and tagmentation buffer composition (9% PEG8000 vs 8% PEG8000). In brief, one may think that a number of merely esthetical changes were introduced in the work of Lu et al. to make it appear distinct from Da et al., 2020. That being said, the work of Da et al. also provides more details and mechanistic insights concerning tagmentation of hybrids.

Finally, the benchmarking is rather meager, as at a minimum, differential gene expression should be included as well as other parameters as for example detailed in Levin et al., Nat Meth, 2010; Alpern et al., Genome Biology, 2019; Pallares et al., 2020.

Other comments:

• How does the 256-fold increase in number of amplifiable fragments after tagmentation with active Tn5 vs inactive with RNA/DNA hybrids compare when dsDNA is used as a substrate? In this regard, what the authors may have addressed is the basis of tagmentation efficiency of RNA/DNA hybrids and dsDNA. It would be interesting to know what drives the preference of the Tn5 for tagmenting one substrate over another.

• The RNA samples might be contaminated with gDNA, which will presumable serve as a better substrate for Tn5, did the authors check this possibility experimentally or by checking the resulting sequencing reads?

• What was the reason of using Bst polymerase? Have the authors compared this to the results obtained with the conventional tagmentation protocol involving PCR amplification as described in the protocol of Picceli et al., 2014? This also relates to the shallow benchmarking already mentioned above.

Reviewer #3:

General Assessment:

This manuscript presents a new method termed "ATRAC-seq," which uses Tn5 to fragment RNA/cDNA hybrids to streamline RNA-Seq library construction. This is an interesting advancement, though the standard methods are not that difficult or time-consuming (contrary to the authors' statements). For this method to be widely adopted, the authors would need to show more data about quality and address issues such as Tn5 sequence specificity and 3' coverage bias. Note that essentially the same method has been published on January 27, 2020 as "SHERRY" -- https://www.pnas.org/content/early/2020/01/24/1919800117.

Numbered summary of any substantive concerns.

1) One key problem with the manuscript is that the authors do not use a standard sample for which the expression values are known, so that the comparison with the NEBNext Ultra II RNA library prep kit is inconclusive. It's not possible to know whether there is "comparable performance" as written about Figure 2E without a known standard or another control. The authors should add a new series of experiments with standard samples, such as "the well-characterized reference RNA samples A (Universal Human Reference RNA) and B (Human Brain Reference RNA) from the MAQC consortium, adding spike-ins of synthetic RNA from the External RNA Control Consortium (ERCC)" as published by the SEQC/MAQC-III Consortium in Nature Biotechnology 32:903-914 (2014). In that paper, the authors compare to qRT-PCR data as well as RNA-Seq. Moreover, Figure 2E shows R=0.6970 between the NEB and ATRAC-seq libraries – that is not particularly good correlation.

2) In addition, it would be interesting to see a comparison to Smart-seq2, which is a similar method in its use of oligo(dT) primed cDNA synthesis and Tn5 tagmentation. This method is much closer to ATRAC-seq than the NEB kit.

3) The authors need to more explicitly address 3' end bias (as shown in Figure 2F), as it relates to sequence coverage of genes based on their length. Analysis could be presented as in Figure 1 of Ramsköld et al. Nature Biotechnology 30:777-782 (2012). The 3' end bias was also observed in Di et al. PNAS (Figure S11 and page 7). How will this affect expression level measurements and downstream analysis? One possible solution is to use rRNA depletion together with random-primed cDNA synthesis?

4) Other analyses that should be considered are evenness of coverage along a transcript (coefficient of variation) and the ability to identify differentially expressed genes (Figure 3B in Di et al.).

5) The authors should explain further the "per-position" analysis (Figure 1—figure supplement 1F) as it is not clear what is being shown or how it was calculated.

6) There are experimental and computational details missing from this manuscript. The authors should add the following:

a) Were the ATRAC-seq and NEB libraries prepared from the same RNA?

b) What was the RIN score of RNA used in each experiment?

c) How was the NEB library constructed? This is not mentioned in the Materials and methods section.

d) How is the annealing done for Tn5 oligos (concentration, time, temperature, buffers)?

e) What is the full name and catalog # for the Tn5 purchased from Vazyme?

f) How many reads are there for each library? Analyses should be done with the same number of raw reads per library by down-sampling.

g) Accession #'s for human rRNA should be listed.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Transposase assisted tagmentation of RNA/DNA hybrid duplexes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Bart Deplancke (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The revisions have addressed most of the concerns raised previously by the reviewers. Some additional revisions need to be carried out before the manuscript is acceptable for publication.

Revisions expected in follow-up work:

1) See comment by reviewer #1 regarding a missing positive control and comparisons of efficiency for DNA/RNA hybrids versus dsDNA.

2) A number of concerns made by reviewer #3 regarding the presentation in the manuscript. None of these concerns require additional experiments.

Reviewer #1:

I appreciate that the authors went to a good deal of work to test the synthetic constructs that they describe. They note Ct values of 24 (active Tn5), 28 (inactivated Tn5), and 29 (negative control); however, they neglect to include a positive control. I am surprised, as this would be an easy addition – annealing a ssDNA to the other ssDNA template as opposed to RNA. As it stands, the ct of 24 seems very late for transposed product. Comparing to dsDNA will give a sense of the difference in efficiency between DNA/RNA hybrids and dsDNA. The other edits are fine, this is the last component I believe needs to be addressed.

Reviewer #2:

The authors have adequately addressed our major concerns. No further comments.

Reviewer #3:

General Assessment:

The revised manuscript is much improved. It was good to see the addition of the Smart-seq2 and rRNA depletion with TRACE-seq experiments. It is understandable that the authors could not add an experiment with a standard reference sample or spike-ins due to the COVID-19 outbreak. There are still issues remaining with respect to analysis, presentation, and conclusions.

Numbered summary of any substantive concerns.

1) The authors' use of housekeeping genes to assess correlation in gene expression measurements between different methods is acceptable, but these issues should be addressed.

a) The use of a set of housekeeping genes should be clearly identified in the Results section and the figure legends

b) The actual names of the housekeeping genes used should be listed in a Supplementary table rather than "list from Eisenberg and Levanon, 2013)" as in the Materials and methods section.

c) They should also present the analysis with all the genes – noting that one example is shown in the authors' response to reviewers' comments.

2) In several places, the authors minimize the underperformance of their TRACE-seq method. In each place, the authors should modify the text and include the actual numbers for the readers in the text. Finally, the text should be modified from "are comparable", "demonstrates comparable performance", and "shows comparable performance" to something more measured that lists the advantages and disadvantages.

a) Coefficient of Variation is actually much worse (Figure 2—figure supplement 1D) not "slightly higher coefficient of variation".

b) 5' to 3' bias. This issue is not apparent here because of the use of high quality RNA (RIN 9.5), but with lower quality "real world" samples, the bias becomes more of an issue and the gene expression measurements will be affected. This should be noted in relation to the statement "In spite of the gene body coverage bias, the gene expression measurement (Figure 2E).… [is] unnoticeably affected."

c) rRNA-aligned reads is actually ~100x worse for 200ng total RNA than for 10ng mRNA. That is not "slightly higher but acceptable". It is probably acceptable, but that's a judgement for the reader to make.

d) Strandedness. The authors now do mention this, but this is actually a significant drawback for RNA-Seq experiments.

3) The authors' explanation of the "per-position" analysis (Figure 2—figure supplement 2I) as still not clear about what is being shown or how it was calculated.

4) The cost comparison between NEBnext and TRACE-seq is good, but the Smart-seq2 should be included and it is likely less expensive than either method ($10-15/library).

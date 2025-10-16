# Peer review - Round 1

Editors:
- Kristin Scott, University of California, Berkeley, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21476.034](https://doi.org/10.7554/eLife.21476.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Variation in olfactory neuron repertoires is genetically controlled and environmentally modulated" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors performed a comprehensive analysis for expression levels of over 100 odorant receptors (ORs) in different mouse strains. They use the large data sets to explore individual- and strain-specific variation in OR expression, the putative role of cis-regulatory elements in choice probability, and the influence of long-term environmental exposure to odors on the OR repertoire. The comprehensiveness is the appealing point of this paper, and the study is thorough and well done. Thus, the major advancement in this paper is to expand data that had been available only from a limited number of ORs in previous studies.

Essential revisions:

1) The authors show that OR gene counts may be used as a proxy for OSN number within a single genetic background and infer that this holds for other strains. To make the case that cell number changes (rather than expression levels per cell) vary between strains, the authors need to validate more OR genes by in situ hybridizations in the different strains. Alternatively, single cell RNAseq could be used to demonstrate the variability in expression for neurons expressing the same OR within and across strains. The conclusions of the manuscript are significantly weakened without a more convincing validation that across-species DE can be used to infer species-specific OSN numbers.

2) A major claim of this paper derives from the observation that each allele of F1 hybrids expresses ORs at levels similar to that expressed by the parental strains. This leads to the claim that "choice" requires regulation in cis but not in trans. There are three reasons why this claim is not supported by the evidence. First, although Figure 4F seems more or less linear, there is substantial diversity (in log space) about the equality line, and no r-squared or equivalent metric is calculated. In addition to remediating the statistical deficits in this key figure, the deviation from unity is important and not commented upon; indeed it is unclear how the authors might interpret this deviation conceptually (i.e., how much deviation would "disprove" their hypothesis that regulation is in cis). Second, the broad (and nearly wholly unexplained) influence of an OR sequence on the expression of 10% of the OR repertoire means that there is no way to disambiguate OR sequence effects from enhancer/promoter effects (particularly since many points on 4F fall off the unity line). Third, even accepting that the data show a clear influence of cis elements on choice frequency (which is likely but not definitively shown given the data), these experiments do not afford any insight regarding the potential role for trans-interactions in choice per se; they only show that choice frequency is determined in cis (and leave open the possibility that trans-interactions are permissive for choice and therefore are critical for the singularity of gene expression), which was the prevailing model even before these data were generated. Indeed the authors repeatedly invoke trans-interactions in the paper as a possible explanation for various aspects of the data, despite strong claims that trans-interactions are not important for "choice". Constraining the interpretation of these data (largely through clarifying the language throughout to make clear that by "choice" what is meant is "choice probability") will more fairly contextualize this result. Note, also, that the definitive experiment here is one that was not performed: swapping the cis-elements between species (rather than two OR cDNAs within a species) to show that polymorphisms in cis-elements determine choice frequency.

3) The relevance of odor exposure experiments in Figure 5 and 6 is unclear, as we really don't know how the odor exposures differed from the perspective of the animal nor do we understand the perceptual consequences of these gene expression changes. Furthermore, the interpretation of these experiments is also incomplete – the receptors seem to be bidirectionally modulated (in equal measure), and only a fraction of these receptors are associated with pS6 signals.

4) In Figure 4E, the coding sequence swap of Olfr1507 with that of Olfr2 significantly changed the expression of ~10% of OR genes. This broad change in the expression of the OR repertoire due to swapping single OR gene apparently contradicts to the main claim of this paper, cis-elements determine the OR choice frequency. Is it possible that the odd gene expression effects of the CRISPR experiment reflect off-target indel formation in the OR repertoire? Was any targeted genomic sequencing done to address this concern? Is genomic architecture altered in these animals, consistent with a fundamental rearrangement of trans-interactions (which would be very interesting)?; this could be assessed by chromosome conformation capture experiments (4C against Olfr1507 promoter or enhancer or Hi-C), but performing these experiments would be only important if the authors decided to make this the focus of a revised manuscript.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Variation in olfactory neuron repertoires is genetically controlled and environmentally modulated" for further consideration at eLife. Your revised article has been favorably evaluated by Patricia Wittkopp (Senior editor), a Reviewing editor and one reviewer.

The manuscript has been greatly improved but there are minor textual changes requested to discuss the potential role of coding and non-coding sequences (see below). These text revisions should be straightforward to complete and I do not anticipate that they will cause a significant time delay.

Reviewer #2:

The paper entitled "Variation in olfactory neuron repertoires is genetically controlled and environmentally modulated" is a resubmission from Logan et al. that uses RNASeq and genetics to probe the diversity of OR expression in the olfactory epithelium. This manuscript is substantially improved from the previous submission, and in particular now appropriately characterizes what is learned from the paper. The improved statistical analyses are also very helpful. However, there are a couple small points that are worth revisiting through text revisions before publication of this very nice paper.

Major point:

The authors seem at pains to argue that the primary sequence of each OR does not contribute to the pattern of expression of that OR, but I'm still having trouble seeing the argument clearly. Just to be transparent about my point of view here, I think the authors have done a very nice job of showing that sequences that are linked to the OR are instructive for choice frequency. I just don't see any evidence that rules out OR primary sequences in this process, and indeed see some evidence that it may play a role, for the following reasons:

a) the fact that similar protein sequences are differentially regulated across strains (the main argument leveled here) doesn't rule out the converse – that distinct protein sequences might contribute to differential regulation.b) The attempt to call the differences in OR expression in the receptor swap experiment "subtle" and therefore not important ("the extensive variance…is independent of the coding sequence […] of the OR […]") is really a qualitative judgment rather than a quantitative argument, especially given that in the same manuscript similar effect sizes are argued to be relevant in the context of odor exposures, and given the argument in the discussion that fold changes in OR expression have perceptual meaning.c) Most importantly, unless I really am missing something, the F1 analysis doesn't distinguish coding from non-coding effects, as these are linked in the intercross.

I think some additional circumspection is merited here. The authors have the benefit that the model they favor – that cis elements are instructive and that protein sequences don't matter that much if at all – is likely to be right. It is just that given the data assembled here this argument seems less definitive than the authors seek to make it.

# Peer review - Round 1

Editors:
- Chris P Ponting, University of Edinburgh United Kingdom

Reviewers:
- Chris P Ponting, University of Edinburgh United Kingdom
- Igor Ulitsky, The Weizmann Institute of Science Israel

## Review text

DOI: [10.7554/eLife.42650.032](https://doi.org/10.7554/eLife.42650.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "PUMILIO hyperactivity drives premature aging of Norad-deficient mice" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Chris P Ponting as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by James Manley as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Igor Ulitsky (Reviewer #2). A further reviewer remains anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this manuscript, Mendell and colleagues describe the generation and characterization of Norad-/- mice. NORAD was previously described as an abundant and conserved lncRNA, whose disruption in human cells results in genome instability through either increase in activity of Pumilio proteins in the cytoplasm or disruption of protein complex formation involving RBMX in the nucleus. In this new work, Norad-/- mice were generated, and shown to have a severe aging phenotype, which is accompanied by genome instability and mitochondrial defects, along with some changes in gene expression, which can be attributed in part to hyperactivity of the Pumilio proteins. Convincingly, mice with mild inducible transgenic over-expression of Pum2 are shown to recapitulate the Norad-/- phenotype, strongly arguing that Pumilio hyperreactivity is indeed responsible for the Norad loss-of-function phenotype.

Essential Revisions:

1) CLIP experiments.

A) Arguably the weakest part of the results is the changes observed in gene expression in the mouse brain, particularly Figure 3E, which shows deviations in both up-regulated and down-regulated genes, contrary to the expectation for mostly up-regulation of Pumilio targets. This is possibly because the authors select Pum targets based on CLIP data, which has the advantage of yielding "experimentally defined" targets, but biases towards more abundantly expressed genes (as those are likely to have more reads/clusters in CLIP data). What does Figure 3E look like if the authors define the targets based on presence of PREs in 3'UTRs (e.g., requiring at least 2 PREs)? An alternative would be to sample non-targets that have the same expression level distribution (and 3' UTR lengths) as the CLIP-defined targets and repeat the analysis. In any case, it is worth discussing how the changes observed in gene expression, at least in bulk tissue are very small (~5%) and occur in both directions. This is consistent with the studies in human cells, but still worth dwelling on in the Discussion section.

B) Another molecular phenotype the authors observe is increase in Pumilio target clusters based on eCLIP data. This analysis has two caveats – first, differences in quality of eCLIP libraries can result in differences in numbers of clusters etc. Can the authors show that the replicates of eCLIP from the same genotype (if performed) are similar to each other more than Norad+/+ samples to Norad-/- samples? Alternatively – is the PRE motif recovered equally strongly from Norad+/+ and Norad-/- libraries?

C) The other caveat with the eCLIP analysis is that the authors normalize the total number of eCLIP reads, and then compare the eCLIP/FPKM ratios between genes. This makes it difficult to interpret Figure 3D. To me, it shows that the reads become redistributed to clusters in the more abundant genes, rather than that target occupancy globally is indeed increased (it’s not clear to me that the latter can be shown with just eCLIP data, which have to be normalized somehow). First, why don't both curves reach 1 at the y-axis? Also, since the total number of reads is normalized, is this evidence sufficient to say that "target occupancy was significantly increased"? The authors should explain more thoroughly why this analysis is valid (I could be missing something), and how it supports the conclusion in the main text.

D) Related to (A) above. Is a PRE-dependent signature of Pum target repression evident in the MEF data (Figure 4)? If it is – it's worth showing in supplement. If not – worth discussing.

2) NORAD/RBMX.

Analysis of two other protein binding partners have been published for Norad/NORAD: SAM68 and RBMX. In particular, the interaction of NORAD with RBMX and its influence on the topoisomerase complex (Munschauer et al., 2018) is very convincing and accounts for the genome instability resulting from NORAD loss. Moreover, the topoisomerase complex is also implicated in mtDNA maintenance, similar to what the authors show in their work here. The authors briefly mention the NORAD/RBMX study in the Introduction, but curiously state that the role of this interaction for genome stability is unknown. The role of topoisomerases in genome stability is thus known and the authors need to discuss the NORAD/RBMX study in light of their own findings. There are, however, some discrepancies between these studies. Lee et al., and Tichon et al., found NORAD to be predominantly localized in the cytoplasm, while the NORAD/RBMX study find that NORAD is evenly distributed (smFISH and fractionation) between the nucleus and the cytoplasm. RNA-FISH data, if available, would resolve this issue.

3) PUM2 level in FLAG-tag experiment.

There is a surprising lack of PUM2 protein level change for the FLAG-tag PUM2 mouse experiment. This means that the authors' model is not definitive and they need to be more circumspect in their conclusions. (subsection “Enforced PUM2 expression phenocopies Norad loss of function”) The authors need to define how PUM2 is deregulated, if it is not overtly overexpressed. Otherwise, the models cannot be defined as such. One alternative hypothesis is that deregulated PUM2 RNA, but not protein, is required for the phenotype to be manifested. Do the authors have evidence that this is, or is not, the case? If not then they need to discuss alternative explanations, remove the word "accordingly" (Abstract), and insert further caveats to their conclusion that (subsection “Enforced PUM2 expression phenocopies Norad loss of function” and elsewhere) "PUMILIO hyperactivity in Norad-deficient animals results in.…" etc. The rare cell specificity of effect (Discussion section) is an attractive one but is not supported by evidence in the submission. Subsection “Enforced PUM2 expression phenocopies Norad loss of function”: The lack of alteration of PUM2 protein levels in these 7 tissues (even with the negative feedback mechanism) cannot be reconciled with the PUMILIO "hyperactivity" of the title.

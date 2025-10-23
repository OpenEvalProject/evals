# Peer review - Round 1

Editors:
- Asifa Akhtar, Max Planck Institute for Immunobiology and Epigenetics , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07378.031](https://doi.org/10.7554/eLife.07378.031)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Mitotic fidelity requires transgenerational action of a testis-restricted HP1” for consideration at eLife. Your article has been favorably evaluated by K VijayRaghavan (Senior editor), a Reviewing editor, and three reviewers.

The following individuals responsible for the peer review of your submission have agreed to reveal their identity: Asifa Akhtar (Reviewing editor), William Theurkauf and Daniel Barbash (peer reviewers). A further reviewer remains anonymous.

Summary:

The reviewers have provided their individual assessments and also discussed in detail the findings presented in your manuscript. The reviewers are of the opinion that it is an interesting story with elegant genetics to describe the role of HPIE as a paternal effect mutation required for segregation of paternally-derived chromosomes. However, additional work is required to strengthen your claims so that the manuscript is a strong candidate for publication in eLife.

Essential revisions:

Detailed reviewers’ comments are included below, but the consensus among the reviewers was there are at least two major points we would like you to address upon revision.

1) The authors need to strengthen their claim about the “heterochromatin function” of HP1E. RNA seq is interesting but more direct evidence would be needed. Ideally ChIP-seq from this particular stage will be desirable however, if this is not feasible then at least ChIP-qPCR for a selected gene set will be important to provide more direct evidence for HPIE action on heterochromatin.

2) The authors also need a better characterization of the mis-segregation phenotype. As pointed out in one of the reviewer's comments, it will be very helpful if the authors used additional probes such as rDNA and a few euchromatic loci and centromeres and compared their phenotype with other reported work at later stages.

Reviewer #1:

Only a few minor comments.

1) Related to the data that show narrow expression window, yet causing derepression of heterochromatin genes in mutant: What kind of chromatin state do the authors think HP1E is conferring to sperm chromatin that both explains derepression of heterochromatin genes during spermatogenesis AND defective chromatin decondensation and segregation of paternal chromosomes in zygotes?

2) Related to their conclusion that HP1E is depleted from mature sperm chromatin, any discussion on the possibly very low amount of it marking certain genomic location, similar to a finding that histone is not completely removed from mammalian sperm chromatin? (http://www.ncbi.nlm.nih.gov/pubmed/19525931)

Reviewer #2:

This report shows that knock down and chromosomal mutations that disrupt the Drosophila testes specific HP1, HP1E, lead to defects in remodeling of the male pronucleus and segregation of the sex chromosomes during the early cleavage stage embryonic divisions. Western blotting and IF data indicate that HP1E protein localizes to nuclei during spermatogenesis, but is not incorporated into mature sperm or transferred to the embryo. The authors also show that maternal expression of HP1E does not rescue the PEL phenotype, and use a very elegant genetic experiment to show that the embryonic mitotic defects are specifically due to failure to segregate the paternal chromosomes. Based on these observations, the authors propose that HP1E establishes an epigenetic mark that is essential to reorganization of the male pronucleus. The data are consistent with this model, but HP1E mutations alter expression of over 700 genes, and it is also possible that one or more of these genes establish an inherited modification or encode a chromatin protein that is required for reorganization and segregation of the male pronucleus. While directly testing this hypothesis is difficult, this possibility needs to be considered /discussed. Nonetheless, the experiments are well executed, clearly presented, and genetically define a novel paternal function in pronuclear reorganization. The additional experiments suggested below are not essential, but would strengthen the story and could provide mechanistic insights:

1) HP1E depletion leads to mis-regulation of heterochromatin genes and segregation defects predominantly for sex chromosomes during embryonic mitosis in next generation. Does HP1E preferentially associate with the sex chromosomes during spermatogenesis? ChIP sequencing would be the best way to test this. Is this technically challenging in fly testes? If not, the authors appear to have the reagents needed to perform the experiment, and it could provide important insight into HP1E function.

2) HP1E is likely to bind H3K9-me3, and co-localization of HP1E and K9-me3 would indirectly test this. HP1A recruits the methyl transferase that generates this binding site, leading to heterochromatin spreading. HP1E may have a similar function. It would be interesting to determine if H3K9me3 localization is altered in HP1E mutants. This could be done by IF, but ChIPseq would be better.

3) As noted above, the RNAseq data show that many genes change their expression in HP1E mutants. Do any these genes encode chromatin modifying proteins, or proteins that directly associate with chromatin?

Reviewer #3:

Levine et al. have characterized the gene HP1E, discovering that it is a paternal effect mutation required for segregation of paternally-derived chromosomes. The combination of the FISH, anti-AcH4, and sesame mutant experiments are particularly strong with regards to HP1E's requirement for paternal chromosome segregation in the first embryonic mitosis. The authors further establish that HP1E is present and thus likely active only in developing sperm, with a mechanistic understanding of its role in chromosome segregation awaiting further study. The authors suggest that HP1E is a heterochromatin factor but this is based on mostly indirect evidence.

Major points:

1) I'm not very familiar with the spermatid stage being studied but take the authors' point from cited refs that heterochromatin cannot be identified with HP1A, H3MeK9, etc. at that stage. So the inability to directly examine HP1E chromatin localization is an acceptable limitation of the system. Localization in other tissue types upon ectopic expression obviously has caveats but would be useful to show if available.

The RNA-seq analysis is presented as an indirect alternative to determine whether HP1E is a heterochromatin protein, but more could potentially be gained from this, and the analyses clarified. How are heterochromatin genes defined in this study? What proportion of them are misregulated—all misregulated may be upregulated, but out of what total? Are they equally affected on all chromosome arms—this might give some insight into the apparent specificity of the segregation defect? How do such results compare to euchromatic genes? Chromosome 4 would be of particular interest due to its unusual heterochromatic state.

Analysis of repetitive sequences could also be informative for addressing whether HP1E is a general or specific chromatin regulator. There's little doubt that satellite sequences are not proportionally represented in Illumina data, especially RNA-Seq, but we have had some success with Hmr and Lhr in mapping reads to satellites, with the results partially correlating with cytological data.

2) Relating to the issue of whether HP1E is a heterochromatin protein, and its degree of specificity, the mis-segregation phenotypes in Figure 7 look very different from what we've seen in Ferree's work at later embryonic stages, where mis-segregating sequences like 359 go all the way across the anaphase bridges. Here with HP1E mutant the probes are forming clusters that don't look any more stretched out compared to normal segregation, e.g., when comparing the presumed maternal and paternal X's in the female embryo. So most of the stretched material in the bridge is unidentified. It would be informative to look at additional probes such as rDNA and a few euchromatic loci. Were centromeres looked at (may have missed)? Figure 7 (and others) are also lacking wild type controls. Here they are really essential in order to interpret the mutant phenotypes.

3) HP1E is firmly established here as a paternal effect mutant. “Transgenerational” is widely understood to refer to mutant phenotypes that are transmitted across generations, and does not apply here.

# Peer review - Round 1

Editors:
- Brian D Slaughter, Stowers Institute for Medical Research United States

Reviewers:
- Susan Strome, University of California, Santa Cruz United States
- Barbara Panning, University of California, San Francisco United States
- Brian D Slaughter, Stowers Institute for Medical Research United States

## Review text

DOI: [10.7554/eLife.42823.029](https://doi.org/10.7554/eLife.42823.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A Multiplexed DNA FISH strategy for Assessing Genome Architecture in C. elegans" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Brian D Slaughter as the Reviewing Editor and Reviewer #4, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Susan Strome (Reviewer #1); Barbara Panning (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript details the adaptation of DNA chromosome Oligopaints for use in Caenorhabditis elegans. By altering the hybridization strategy from other DNA oligo-paint protocols, the authors have come up with a bridge oligo method that allows for improved flexibility in the labeling of the FISH oligo pools. Fields et al. designed a set of ~170,000 C. elegans oligos arrayed on two 90,000-oligo chips. Each has a unique 42 bp primary oligo plus 3 barcodes, 1 for that oligo's chromosome, 1 for that oligo's 3 MB location, and 1 for that oligo's 0.5 MB location. Using the library of composite oligos in combination with bridge oligos and detection oligos conjugated to 1 of 3 fluorophores, the investigators can perform DNA FISH with up to 6 combinations to image whole chromosomes and/or 0.5-3 MB regions of chromosomes.

Having established the effectiveness and versatility of the method, the authors then use this method to assess chromosome organization during aging. They show that chromosomal territories become less distinct (enlarged and disorganized) with more overlap (suggesting that chromosomal territories are not maintained) and that this disorganization is age and not time related. Finally, they identify one molecular player, mes-3, knockdown of which phenocopies age-related chromosome disorganization.

This manuscript will be of broad interest – the FISH method will be useful for the C. elegans community and the finding that chromosome organization is altered with age will be intriguing to the aging community. Overall, the manuscript is a nice methods paper that will provide a useful resource for broad use within the C. elegans community to address key questions about how genome architecture influences multiple processes and cell types within a developing and aging organism. The reviewers shared enthusiasm for the paper, and would be supportive of publication given that the concerns below are addressed.

Essential revisions:

In Figure 2, more work should be given to demonstrate the specificity of the Oligopaint approach. To demonstrate specificity, Oligopaint could be done on animals in which oocytes carry a fusion of two chromosomes – painting one of the chromosomes of the fusion should paint only half of the long fused chromosome. Probably easier would be to paint the X chromosomes in him-8 mutant oocytes, in which the X chromosomes exist as univalents instead of a bivalent.

STORM data:

Subsection “Using OligoSTORM to super resolve C. elegans chromosomes within whole animals”: The authors need to be cautious using FISH and STORM to quantify particle density. First, there is no way to know if all the probes are getting activated since STORM is a stochastic method. Thus, an unknown percent of the probes could remain in the dark state and never be activated; or probes might not be deactivated and sent back to the dark state. Second, there is no way to know if all of the probes have hybridized, thus it is dangerous to assume that the probes are still equally distributed once they have been hybridized in the worm. The authors should address both of these in the manuscript.

Subsection “C. elegans Oligopaint library design: The authors mention that the oligos are "evenly spaced" with about 2 probes per kilobase of genomic DNA. Is this true all the way across the chromosome? In other organisms the probes are on average evenly spaced, but there are some regions where this can't occur because of repetitive DNA or potential crosstalk of the sequence with another chromosome. Furthermore, the authors use this equal distribution of probes to quantify the density of DNA in the STORM experiment. If regions of the genome are not evenly covered, then that needs to be mentioned and addressed in the STORM quantification.

Beyond this point, the authors should make more clear what the utility of the STORM analysis is, and what specially it adds to the manuscript. The chiasmata between homologs is easily represented with standard fluorescent microscopy. If true, the 'core' idea would be of interest. However, STORM is very sensitive to environment, and more work should be done to determine that the 'core' at the center of each chromosome IV homolog is real, and not an artifact of STORM. It needs to be verified with a further method. The size of the gradient of STORM density is on the order of a micron. It true, standard, high resolution, confocal data should be able to see this same gradient. Using one color to mark the chromosome, followed by DAPI quantification, may also see it. Is there evidence of such a 'core' density difference from Hi-C data?

If the authors can demonstrate that this core is missing from other chromosomes, or is missing in some condition such as aged C. elegans, it would also go a long way in determining that this is not an artifact of STORM.

Are the authors able to use STORM to resolve any detail on the scale (reported as 80 nm) of their improved resolution? And if so, what is the relationship between what conclusions can be made with super resolution imaging yet with relatively low probe density (2 probes per kb)? Further discussion on this point would be useful.

More thorough explanation of methods and more discussion:

Some sections of Materials and methods are quite minimal. Especially since this is a Tools and Resources article, the Materials and methods should provide protocols that are detailed enough for others to use the technology.

Specifically, the authors combined 3 colors in different combinations to come up with 6 signatures for the 6 chromosomes (Figure 3A). This is very effective in outlining the 6 chromosomes in cases where there is either separation of the chromosomes, or very discrete chromosome territories. However, in cases where there are not discrete territories, and overlap between chromosomes becomes dramatic, separation of 6 chromosomes with 3 colors becomes very difficult. The authors acknowledge this in the Figure 6 figure legend – and quantification in Figure 6B and CD was done on 3 chromosomes only because of this difficulty. This should be explained more thoroughly in the text.

The separation of chromosomes with this method, especially in circumstances of chromosome overlap, is a key, others will want to do this in mutants, aged cells etc. Part of this being considered as a tool and resource is a full description of methods not just for probe design, but data analysis. More explanation is needed on criteria for considering a region positive or negative for a color, and how the final determination of where a chromosome is, in cases of high degree of overlap, should be discussed with rigor so others can reproduce it.

In the section with the mes-3 RNAi – while the images in aging intestinal nuclei and mes-3 hypodermal nuclei look relatively similar, the quantitation of overlap was quite different. Is that a function of different cell types? Or does it reflect that different mechanisms underlie the breakdown of nuclear organization.

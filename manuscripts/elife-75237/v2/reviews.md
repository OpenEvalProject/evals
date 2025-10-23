# Peer review - Round 1

Editors:
- Antoine Claessens, https://ror.org/051escj72 University of Montpellier France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75237.sa0](https://doi.org/10.7554/eLife.75237.sa0)

The authors dissected the across-the-genome consequences of sexual recombination in Trypanosoma cruzi, a serious human pathogen. They had discovered hybrid formation in this species 20 years ago, here they went at length by culturing parental and hybrid clones for 5 years, demonstrating that tetraploid T cruzi hybrids undergo genome erosion.


---

# Peer review - Round 1

Editors:
- Antoine Claessens, https://ror.org/051escj72 University of Montpellier France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75237.sa1](https://doi.org/10.7554/eLife.75237.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Experimental microevolution of Trypanosoma cruzi reveals hybridization and clonal mechanisms driving rapid diversification of genome sequence and structure" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jos Van der Meer as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Julius Lukes (Reviewer #1); Fernán Agüero (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors should revise their methods for SNP calling. What GATK variant caller was used? UnifiedGenotyper or HaplotypeCaller? The latter is recommended. It is also unclear which filtering criteria were used to reduce the likelihood of false-positive SNPs. Simply setting the mapping quality to a minimum of 50 is not sufficient. We recommend to have a look at the methods of Schwabl et al. 2019 (https://doi.org/10.1038/s41467-019-11771-z) where rigorous analyses were done to remove false-positive SNPs. In particular, it would be helpful to mask the reference genome based on the mappability of its own reads. This is also important for later sections in the manuscript where the authors claim increased diversity in repetitive surface molecule genes.

Editor: Also, it is not clear whether Indels were analysed at all, they appear once in the Methods and not in the rest of the manuscript.

2. Figure 1e, Table 1 and corresponding main text – We are puzzled regarding the number of SNPs that are unique to each hybrid clone and that are common to all hybrids.

First, it seems to us that the authors have done SNP calling in all strains independently, which may result in genotypes being missed because of low local coverages. Joint genotyping would mitigate such biases. We would recommend to do a joint genotyping across all parental and hybrid strains, and then only retain those SNP positions for which there is no missing data.

Second, in the main text on page 7, it is argued that these SNPs would have occurred in culture during the approximately 50 generations of growth BEFORE hybrid formation. But in the last sentence of that paragraph it is stated that these SNPs appeared after the hybridisation event. How can the authors tell whether these SNPs occurred during culture before hybridization, or whether they happened just after hybridization? The setup of the experiment should be more clearly explained: how many generations happened before hybridization, how many after, when exactly was sequencing done during this process? This is also important for later sections that claim that hybridization resulted in a burst of novel mutations.

It seems like the authors are discovering the impact of tandem repeat regions (copy number variations) on SNP discovery. Most of page 10 and Figure 3 merely describes the fact that you will have more false-positive SNPs within the repeat regions. I'm not sure why this is of interest here. Such SNP's should not have been included in the first place.

3. Why was the mapping quality in surface molecules inferior to the rest? That begs for explanation. "Surface molecule genes", frequently used here, sounds somewhat weird to this reviewer. Couldn't it be rather "Surface protein-coding genes" or the like?

4. I understand the implications of trying to map short reads to repetitive regions. For example, PAINTS (see https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7912377/) removes noisy genomic regions (large gene families) before attempting to do ploidy estimations. This seems intuitive, and this is also explained in this Ms, in light of this maybe authors can save some space by omitting text and figures that are used to discuss and show these difficulties? Maybe there is not much to gain by showing that estimating ploidies in chromosomes with low numbers of housekeeping genes is difficult. Just state that and put the data into Supplementary file?

5. Based on the results presented, I don't agree that there is gradual erosion overall across all clones.

1D12 hybrid seems to have gone through an initial loss of DNA content but then its DNA content seems to have remained stable (Figure 1D). In addition, it's genome-wide somy profile remained stable at tetrasomy (Figure 4C). Also, there also seems to be an increase in DNA content after 600 generations. Finally, microsatellite alleles are only consistently lost in hybrid 2C1, at three different loci. No loss was observed in hybrid 1D12 and only one allele was lost in hybrid 1C2. This also raises the question what has caused the loss of DNA content in hybrid 1D12. Based on microsats and somy, there is no clear evidence for genomic erosion. So, what part of the genome is lost in the beginning of the experiment? The authors could do a comparative genomic analyses of the parental genomes and the hybrid genomes, to figure out what portions of the genomes are commonly/uniquely lost in the hybrids.

6. One of the conclusions from the study of accumulation of mutations, is that surface molecules may mutate faster. The reasoning for this if I read and understood correctly, is that there were many "mutations that appeared in each parental clone after culture growth". Do authors mean to say that these mutations appeared after the genetic cross experiment in Gaunt et al. 2003? Can the authors clarify how these parental clones were kept and passaged since then? How many passages did they undergo before being sequenced? The same clarification is warranted for hybrids. When the authors state that "while the parental strains were diploid, all initial hybrid clones were essentially tetraploid" (Discussion, page 15), the readership would like to know if these essential tetraploid states were observed just after the hybridization (genetic exchange) event (e.g. clones were kept in liquid nitrogen since then and only thawed for brief culture before sequencing) or if these states had some passages in culture after the genetic exchange event (how many?).

7. Data and code availability: The mentioned accession number was not found in the BioProject database. Please make code available via GitHub or other repository.

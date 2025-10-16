# Peer review - Round 1

Editors:
- Graham Coop, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66405.sa1](https://doi.org/10.7554/eLife.66405.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Drosophila species have long served as an important model system for genetics and genomics. The authors have developed an important community resource of high standard genomes for many species across the Drosophila clade. This resource will serve to empower the next generation of Drosophila research and provides an important road map for similar efforts in other groups of organisms.

Decision letter after peer review:

Thank you for submitting your article "Highly contiguous assemblies of 101 drosophilid genomes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Timothy B Sackton (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers and we appreciated the impressive community resource that has been carefully brought together and that this acts as an important road map for other clade-wide sequencing efforts.

The strong points of consensus that emerge across the reviews, and in the discussion with the reviewers, were:

1) The need for base accuracy to be incorporated into the quality metrics discussed.

2) The need to place the work into a broad context of large-scale genome efforts to expand the readership outside of Drosophila researchers and show the expanding wave of community efforts focused on high-quality reference genomes. Suggestions included the vertebrate genome project and the earth biogenome project.

3) The reviewers all noted that acknowledgement of previous work in Drosophilidae was lacking. Drosophila researches have clearly been leading this charge for a while and it would be good to place the current effort into prior work more thoroughly.

4) While annotation of these genomes is beyond the scope of the current paper, it would be good to include more of a discussion of the planned road map for annotation going forward.

These points all should be addressed in a revised version. Below we have copied each review in its entirety. The reviewers have read each other's reviews and agree that all of the points are reasonable. Please provide a point by point response to the reviews, with a focus on the above broad goals.

Reviewer #1 (Recommendations for the authors):

– Data availability. I found all (or at least most) of the raw sequencing data. I couldn't find assembly accessions.

– Guidance for future sequencing work

A back of the envelope calculation based on typical core prices for PacBio Sequel II CLR sequencing and Illumina Novaseq PE150 reads suggest a price total price of $14.50 / GB (< $2,175 / 150GB) and $9 / GB (< $6,750 / 750 GB) respectively. To sample a 150MB genome at 100-fold depth (15GB) for both platforms would seem to imply a cost of ~$350 (comparable to the price cited by the authors) or less. Accepting lower depth would lead to concomittant decreases in price / genome. The average sequencing depth for this project appears from Table S1 to be 9.8GB for long reads and 12.8GB for short reads, implying that the PacBio approach might be a bit cheaper. I don't think a detailed price analysis is necessary (or even advisable), but communicating the fact that the authors' approach is one of at least two more or less equally viable approaches would be both valuable and accurate.

– Quality control metrics: sequencing error and sample polymorphism

A description of the consensus error rate of the assemblies would be an important piece of documentation serving two purposes. It permits users to quantify the amount of error they might expect from this particular resource. Relatedly, since many of these samples are conducted on strains for which near isogenic samples are difficult to acquire, measuring and reporting the heterozygosity would help guide users as to the extent of this property of the material from which the assembly was derived, especially if such users intend to use the reference strains described here for conducting genetic work.

– Context via comparison to existing resources

Existing resources for highly contiguous assemblies (operatively, contig N50 > 1MB)

– The total number of existing assemblies is already at least 75 with N50 >= 1MB (57 from NCBI[1], 13 from Miller[2], 4 from Comeault[3], 1 from Rezvykh[4]).

– Obviously, this includes a lot of within-species samples (especially for D. melanogaster, including many assemblies of the reference strain) and many assemblies that have been subsequently improved by the authors. However, the authors are also sampling the same species multiple times (including the D. melanogaster reference strain) to their total count, so this is at least consistent with their counting.

– Importantly, this resource triples unique species possessing highly contiguous assemblies from 34 to 102 and expands species group representation from 8 to 15. Although, the quinaria group, represented by D. innubila, already existed and wasn't sampled again here, they re-sample 7 of the previous 8 species groups and add 7 more.

– As far as I can tell, until now, the most distant relative of D. melanogaster within Drosophilidae with a highly contiguous genome was Scaptodrosophila lebanonensis, which is in the tribe Colocasiomyini. The manuscript adds two additional members of this tribe, Leucophenga varia and Chymomyza costata. So, the number of distant relatives is tripled, but the actual phylogenetic breadth isn't (if my understanding of Drosophilid taxonomy is correct, and it may not be)

Scholarship

The $1,000 Nanopore genome was cited by both [2] and [5].

"Future work to improve biological and taxonomic diversity, particularly for species difficult to culture, should employ single fly sequencing and assembly workflows (Adams et al., 2020)."

An earlier long read precedent can be found in [6].

In addition to enumerating other high-quality Drosophila genomes that already exist, it would be extremely useful to users to see a comparison of the quality of the resources when they have published descriptions (in order to guide authors as to what types of contiguity, completeness, and error they can expect, especially in comparison to this work). At the least, I think the authors should put their work in the context of best previous assemblies for each species (an operative definition of contig N50 > 1 Mb seems consistent with their own thinking), particularly when that work has been published. To be consistent with their own accounting, they might even consider addressing works like [7], and species that have experienced extensive high quality sequencing effort like D. obscura, D. simulans, and D. pseudoobscura. I have attached a table with entries corresponding to every species in Table S2 as well as additional species exceeding contig N50 of 1Mb, including citations and NCBI accession numbers when they could be found.

The authors have actually cited many of these assemblies in other work [8], including genomes that have yet to be published, so it would seem that the authors are aware of them and trust the quality enough to incorporate into their own work, so improving the scholarship should be straightforward.

Typo

– In the abstract. There are 93 species represented, not 95.

Reviewer #2 (Recommendations for the authors):

While this manuscript presents a large amount of valuable new data, and is inherently important for that reason alone, I believe that some key improvements and additional analyses could greatly strengthen this manuscript and really improve the value to the community.

1) Improvements to quality metrics.

This paper reports genomes that are at the low-cost end of the cost/quality tradeoff in genome assembly. This is a extremely valuable contribution, because many other large-scale projects in genomics (most notably, the Vertebrate Genome Project) have focused on the other end of this spectrum. Yet, for many researchers, a low-cost way to produce 10 genomes from related species may be higher value than a "complete" assembly from one species. However, it remains somewhat unclear exactly how good these genomes are, beyond the observation that the gene space is largely complete, and contig N50s are generally high.

Therefore, I think the biggest and most important improvement that would increase the reach and usefulness of this manuscript is improvements to quality metrics. A recent preprint from the Vertebrate Genome Project team (Rhie et al., 2020; https://www.biorxiv.org/content/10.1101/2020.05.22.110833v1.full) provides a number of potentially useful quality metrics that may be worth considering applying here, although of course not all will be relevant to this project, and I realize the computational burden of trying to do everything could be large. Nonetheless, I think it is crucial to be able to give some sense of consensus quality, as base-level errors in assemblies has negative effects on many downstream applications. Based on Koren et al., 2019, there appears to be a large drop in likelihood of disrupting a gene due to a indel error between QV30 and QV40, and Rhie et al., 2020 has a lot more detail on various aspects of consensus quality metrics. I realize that many existing tools, e.g. Merqury (also Rhie et al., 2020, in Genome Biology) make the assumption that Illumina data is available for the same individual as the genome assembly, which is not universally true here (even in approximation, e.g. treating a strain as an individual). Still, some attempt to tackle this problem seems necessary, even if it cannot be done perfectly.

2) Assembly content

Related to the first point, basic descriptions of genome size (e.g., estimated from k-mers) would help to contextualize the resource produced, as would a definition of "near chromosome level contiguity" and validation of which of the newly reported assemblies here reach that threshold (especially as contig N50s vary by several orders of magnitude). Again, I don't think the VGP definitions are the only possible way to approach this question, but there is value in having some systematic summary of overall contiguity.

This paper does not describe the extent to which heterogametic sex chromosomes (not expected in all species based on sampling) or mitochondrial genomes are recovered. Presumably at least the presence of mt scaffolds is picked up in the NCBI screens, and is the kind of information that would be relatively straightforward to add to a table.

3) Drosophila focus.

There is a tension throughout this manuscript between describing a basically Drosophila-specific resource, and describing a more generally applicable approach to low-cost, clade-wide assembly. I think that the latter is really necessary and important, since not every community or group has the resources (in money, samples, compute) or desire (for their scientific questions) to use a "VGP-style" approach (with long reads, short reads, HiC, and optical mapping to produce as close to error-free chromosomal assemblies as possible). But the value of this manuscript as a blueprint for low-cost community genomics is somewhat limited by the Drosophila-centric nature of the results.

The most obvious Drosophila-specific assumptions are the availability of a inbred strain, and a genome size of 100-250 Mb or so, with a few exceptions. Notably, the assemblies of the larger genomes (and the ones derived from wild-caught flies) tend to be worse, with lower contig N50s and auN metrics, more contigs, and more fragmented or missing BUSCOs.

Of course it would be well beyond the scope of this manuscript to attempt to validate any of these approaches in other clades, or provide a simple recipe for how to assembly any possible genome. Nonetheless, it would certainly be possible to broaden the discussion, and be clearer in the text when certain statements are Drosophila specific (e.g., the $350 in sequencing costs assumes a genome on the order of 100-200 Mb).

4) Limitations of the existing resource and future prospects for improvement:

The genomes presented here do not include annotations, or any other form of supplemental resource such as whole genome alignments (e.g. Armstrong et al., 2020), and don't use HiC or any kind of scaffolding to obtain true chromosomal scaffolds. I think these are understandable and defensible choices, given the computational and technical requirements to extend this work in those directions. However, it may be valuable to discuss more explicitly what this resource is and is not. At a minimum, doing so could prevent the corresponding authors from receiving many emails asking where the gene annotations for species X are once this work is published.

Reviewer #3 (Recommendations for the authors):

This is really an impressive resource and has the potential to be widely used both in terms of the data itself and also the methodology. I have several suggestions that may improve the manuscript.

There are several species (willistoni, paulistorum, etc.) that are sequenced more than once without any reference to why. It might be useful to describe that somewhere (Table 1?). As a resource, it would be simpler to use if it was clear when one isolate per species vs. multiple were appropriate to use for analyses.

Lines 59-61 – a bit more detail about modifications here since you are writing methods last.

Lines 107-111 – I'm concerned about the conclusions drawn about repeat content based upon the way the data was analyzed. A comprehensive analysis of repeat content is probably beyond the scope of this manuscript, but without de novo characterization of repeat sequences, I'm worried that satellites and TEs in more distantly related species may be missed if they are lineage restricted. I believe TRF would get at this to a point, but maybe not robustly. Other software like RepeatModeler might be better. However, my suggestion is not that these genomes are individually de novo annotated for repeats. It is just that the conclusions about relationships between contiguity or genome size and repeat content are presented with more caveats.

Figure 2 – This figure is a bit difficult to intuit, so this is another place where more detail in the main text would be useful.

Figure 3 – though the authors argue that this tree is not meant as a robust measure of phylogenetic relationships, it would be nice to put some support values on the tree.

Line 336 – I think the bioawk people would appreciate a citation (though all I can find on the internet is to cite the github page).

Line 340 – Please describe the auN statistic (what is L and what are we summing over?) in more detail. The Li github page describes nicely.

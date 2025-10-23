# Author response - Round 1

Authors:
- Michael J Tisza
- Diana V Pastrana ([ORCID: 0000-0002-8084-5665](https://orcid.org/0000-0002-8084-5665))
- Nicole L Welch
- Brittany Stewart
- Alberto Peretti
- Gabriel J Starrett
- Yuk-Ying S Pang
- Siddharth R Krishnamurthy
- Patricia A Pesavento
- David H McDermott
- Philip M Murphy
- Jessica L Whited ([ORCID: 0000-0002-3709-6515](https://orcid.org/0000-0002-3709-6515))
- Bess Miller ([ORCID: 0000-0002-9868-5436](https://orcid.org/0000-0002-9868-5436))
- Jason Brenchley
- Stephan P Rosshart
- Barbara Rehermann
- John Doorbar
- Blake A Ta'ala
- Olga Pletnikova
- Juan C Troncoso
- Susan M Resnick
- Ben Bolduc
- Matthew B Sullivan
- Arvind Varsani ([ORCID: 0000-0003-4111-2415](https://orcid.org/0000-0003-4111-2415))
- Anca M Segall
- Christopher B Buck ([ORCID: 0000-0003-3165-8094](https://orcid.org/0000-0003-3165-8094))

## Response text

DOI: [10.7554/eLife.51971.sa2](https://doi.org/10.7554/eLife.51971.sa2)

Essential revisions:

1) Please include a brief discussion as to what criteria were utilized to designate a sequence assembly as a complete genome. For example, was there a minimum/maximum size? Did the genome have to be a closed circular genome? Was it explicitly required that a genome have at least one identifiable viral associated gene? Please comment on how plasmid sequences and nucleic acids packaged within vesicles were considered/ filtered out beyond the nuclease treatment of virus preparations.

Minimum sequence length was 1000 nucleotides and only closed circular sequences were determined to be complete (Results paragraph one). A specific exception was made for anelloviruses. While the circular sequences did not need to have similarity to known viral genes (see sections on "dark matter"), the sequences needed to have a high density of Met-initiated ORFs. We attempted to remove plasmid-like sequences by removing circular contigs that (1) had a best BLASTX hit to a plasmid and (2) had no virion structural genes (see Results subsection “Virion enrichment, genome sequencing, and annotation”). While we expect the pipeline to remove anything clearly non-viral, it remains possible that one or more of the circular "dark matter" groups could represent elements that package themselves in host-derived vesicles or virions co-opted from co-infecting viruses rather than viruses with self-encoded virion proteins.

2) Please add comments on what percentage of the total sequence data (both total sequence data and unique sequence data) went into the new genomes (and into previously known viral genomes). Likewise, it would also be informative to know what percentage of sequence data was removed by the sequencing filtering criteria discussed in the manuscript.

We added a figure (Figure 1—figure supplement 3) and a table (Supplementary file 5) to address this suggestion. Unsurprisingly, in most samples, most reads did not map to either the new genomes described here or to NCBI's Virus RefSeq database. Inspection of other contigs showed that many represent incomplete viral genomes. This underscores the difficultly of de novo assembly of complete genomes for the kind of high-quality references that this study set out to provide. We hope the reads we deposited in SRA will be fertile hunting grounds for other groups interested in viral sequence diversity.

3) Please include analysis of the overall abundance of cellular sequences present in the samples, using perhaps cellular housekeeping genes as proxies.

To answer this, we utilized the recently-published ViromeQC pipeline (Zolfo et al., 2019) to consider reads aligning to a set of housekeeping gene HMMs (Supplementary file 1). Typically only a small proportion of reads in our datasets aligned to these housekeeping genes, but there was variation sample-to-sample. This is likely because, after collection of fractions from the ultracentrifuged Optiprep gradients, each individual fraction was amplified by Phi29 polymerase in order to capture viruses of different buoyancy (Kauffman et al., 2018), potentially amplifying some bacterial genomes near the top of the gradient.

4) Please consider adding a table or figure that describes the distribution of the new viral genomes across the animal species sampled.

We've added a panel to Figure 1 (Figure 1C) detailing the number of viruses from each viral family that were found associated with each animal species as well as the 'strandedness' of each viral family. We thank the reviewers for suggesting this and other useful improvements.

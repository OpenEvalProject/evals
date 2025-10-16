# Peer review - Round 1

Editors:
- María Mercedes Zambrano, CorpoGen Colombia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88794.3.sa0](https://doi.org/10.7554/eLife.88794.3.sa0)

This study provides an important computational tool for analyzing and deconvoluting a pool of plasmids sequenced without barcoding using nanopore long-read sequencing. The tool, which has been convincingly validated, is readily available to scientists interested in rapid and cost-effective verification of plasmid sequences as well as in scaling up analysis by pooling samples within barcodes.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88794.3.sa1](https://doi.org/10.7554/eLife.88794.3.sa1)

This manuscript presents SAVEMONEY, a computational tool designed to enhance the utilization of Oxford Nanopore Technologies (ONT) long-read sequencing for the design and analysis of plasmid sequencing experiments. In the past few years, with the improvement in both sequencing length and accuracy, ONT sequencing is being rapidly extended to almost all omics analyses which are dominated by short-read sequencing (e.g., Illumina). However, relatively higher sequencing errors of long-read sequencing techniques including PacBio and ONT is still a major obstacle for plasmid/clone-based sequencing service that aims to achieve single base/nucleotide accuracy. This work provides a guideline for sequencing multiple plasmids together using the same ONT run without molecular barcoding, followed by data deconvolution. The whole algorithm framework is well-designed, and some real data and simulation data are utilized to support the conclusions. The tool SAVEMONEY is proposed to target users who have their own ONT sequencers and perform library preparation and sequencing by themselves, rather than relying on commercial services. As we know and discussed by the authors, in the real world, to ensure accuracy, the researchers will routinely pick up multiple colonies in the same plasmid construction and submit for Sanger sequencing. However, SAVEMONEY is not able to support the simultaneous analysis of multiple colonies in the same run, as compared to the barcoding-based approaches. This is a major limitation in the significance of this work. Encouraging computational efforts in ONT data debarcoding for mixed-plasmid or even single-cell sequencing would be more valuable in the field.

Comments on revisions:

My previous concerns have been addressed, and the revised manuscript has been significantly approved.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88794.3.sa2](https://doi.org/10.7554/eLife.88794.3.sa2)

The authors developed an algorithm that allows to deconvolute plasmid sequences from a mixture of plasmids that have been sequenced by nanopore long read technology. As library preparations and barcoding of individual samples increases sequencing costs, the algorithm bypasses this need and thus decreases time on sample prep and sequencing costs. In a first step, the tool assesses which of the plasmid constructions can be mixed in a single library preparation by calculating a distance matrix between the reference plasmid and the constructions producing sequence clusters. The user is given groups of plasmids, from different clusters, to be pooled together for sequencing. After sequencing, the algorithm deconvolutes the reads by classifying them based on alignments to the reference sequence. A Bayesian analysis approach is used to obtain a consensus sequence and quality scores.

Strengths

The authors exploit one of the main advantages of long read sequencing that is to accurately resolve regions of high complexity, as regularly found in plasmids, and developed a tool that can validate plasmid constructions by reducing sequencing costs. Multiple plasmids (up to six) can be analyzed simultaneously in a single library without the need of sample barcoding, also reducing sample preparation time. Although inserts must be different, just 2 bases difference would be enough for correct assignation. Maximizes cost-efficiency for projects that require large amounts of plasmid constructions and high-throughput validation. The algorithm also allows for linear DNA analysis offering extra flexibility.

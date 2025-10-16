# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98300.3.sa0](https://doi.org/10.7554/eLife.98300.3.sa0)

This important study shows how a combination of the latest generation of Oxford Nanopore Technology long reads with state-of-the art variant callers enables bacterial variant discovery at an accuracy that matches or exceeds the current "gold standard" with short reads. The work thus heralds a new era, in which Illumina short-read sequencing no longer rules supreme. While the inclusion of a larger number of reference genomes would have enabled an even more fine-grained analysis, the evidence as it is supports the claims of the authors convincingly. The work will be of interest to anyone performing sequencing for outbreak investigations, bacterial epidemiology, or similar studies.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98300.3.sa1](https://doi.org/10.7554/eLife.98300.3.sa1)

Summary:

Hall et al describe the superiority of ONT sequencing and deep learning-based variant callers to deliver higher SNP and Indel accuracy compared to previous gold-standard Illumina short-read sequencing. Furthermore, they provide recommendations for read sequencing depth and computational requirements when performing variant calling.

Strengths:

The study describes compelling data showing ONT superiority when using deep learning-based variant callers, such as Clair3, compared to Illumina sequencing. This challenges the paradigm that Illumina sequencing is the gold standard for variant calling in bacterial genomes. The authors provide evidence that homopolymeric regions, a systematic and problematic issue with ONT data, are no longer a concern in ONT sequencing.

Weaknesses:

The study is limited in the number of samples included, even though it covers different species with divergent genome sequences, likely covering major evolutionary changes. The methods section could be more detailed. A structural variation analysis would be an interesting next step.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98300.3.sa2](https://doi.org/10.7554/eLife.98300.3.sa2)

Hall et al. benchmarked different variant calling methods on Nanopore reads of bacterial samples and compared the performance of Nanopore to short reads produced with Illumina sequencing. To establish a common ground for comparison, the authors first generated a variant truthset for each sample and then projected this set to the reference sequence of the sample to obtain a mutated reference. Subsequently, Hall et al. called SNPs and small indels using commonly used deep learning and conventional variant callers and compared the precision and accuracy from reads produced with simplex and duplex Nanopore sequencing to Illumina data. The authors did not investigate large structural variation, which is a major limitation of the current manuscript. It will be very interesting to see a follow-up study covering this much more challenging type of variation.

In their comprehensive comparison of SNPs and small indels, the authors observed superior performance of deep learning over conventional variant callers when Nanopore reads were basecalled with the most accurate (but also computationally very expensive) model, even exceeding Illumina in some cases. Not surprisingly, Nanopore underperformed compared to Illumina when basecalled with the fastest (but computationally much less demanding) method with the lowest accuracy. The authors then investigated the surprisingly higher performance of Nanopore data in some cases and identified lower recall with Illumina short read data, particularly from repetitive regions and regions with high variant density, as the driver. Combining the most accurate Nanopore basecalling method with a deep learning variant caller resulted in low error rates in homopolymer regions, similar to Illumina data. This is remarkable, as homopolymer regions are (or, were) traditionally challenging for Nanopore sequencing.

Lastly, Hall et al. provided useful information on the required Nanopore read depth, which is surprisingly low, and the computational resources for variant calling with deep learning callers. With that, the authors established a new state-of-the-art for Nanopore-only variant calling on bacterial sequencing data. Most likely these findings will be transferred to other organisms as well or at least provide a proof-of-concept that can be built upon.

As the authors mention multiple times throughout the manuscript, Nanopore can provide sequencing data in nearly real-time and in remote regions, therefore opening up a ton of new possibilities, for example for infectious disease surveillance. In these scenarios, computational resources can be very limited. The highest-performing variant calling method, as established in this study, requires the computationally very expensive sup and/or duplex nanopore basecalling, while the least computationally demanding basecalling method underperforms. To comprehensively guide users through the computational resources required for basecalling and variant calling, the authors provide runtime benchmarks assuming GPU access.

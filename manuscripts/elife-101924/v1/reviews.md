# Peer review - Round 1

Editors:
- Bavesh D Kana, University of the Witwatersrand South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101924.3.sa0](https://doi.org/10.7554/eLife.101924.3.sa0)

This important study presents an evaluation of several tools used for detecting Identity-By-Descent (IBD) segments in highly recombining genomes, using simulated data to replicate the high recombination and low marker density of Plasmodium falciparum, the parasite responsible for malaria. The evidence presented by the authors is convincing demonstrating that users should be cautious calling IBD when SNP density is low and recombination rate is high. This study will be of interest to scientists working in the field of genome evolution and infectious diseases


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101924.3.sa1](https://doi.org/10.7554/eLife.101924.3.sa1)

Summary:

Authors benchmarked five IBD detection methods (hmmIBD, isoRelate, hap-IBD, phasedIBD, and Refined IBD) in Plasmodium falciparum using simulated and empirical data. Plasmodium falciparum has a mutation rate similar to that of humans but a much higher recombination rate and lower SNP density. Thus, the authors evaluated how recombination rate and marker density affect IBD segment detection. Next, they performed parameter optimization for Plasmodium falciparum and benchmarked the robustness of downstream analyses (selection detection and Ne inference) using IBD segments detected by each method. They also tracked the computational efficiency of these methods. The authors' work is valuable for the tested species, and the analyses presented support their claim that users should be cautious when calling IBD in contexts of low SNP density and high recombination rate.

Strengths:

The study design is convincing and well-structured. The authors chose to use P. falciparum, which presents an interesting case due to its high recombination rate and a mutation rate similar to that of humans. The authors note that despite the widespread use of IBD for genomic surveillance, comprehensive evaluation of these methods in high-recombination, low-marker-density contexts has been lacking. Furthermore, they also examined the performance of IBD detection methods developed specifically for P. falciparum, and evaluated it with phased data which broadened the applicability of the work.

Weaknesses:

The authors thoughtfully addressed our prior concerns by (1) expanding the simulations; (2) updating figures and methods for clarity; and (3) more clearly framing the broader utility of their benchmarking effort. These updates strengthen the manuscript and make the relevance of their findings beyond Plasmodium falciparum more apparent.

More specifically:

The authors added three full replicates per simulation scenario and updated figures to reflect uncertainty at relevant levels, which addresses earlier concerns about reproducibility. The limited number of replicates is due to computational intensity. In the future, broader generalizability and deeper exploration of variance in benchmarking accuracy across parameter space would further strengthen the conclusions/generalizability. The author's also emphasized that, while the study is centered on Plasmodium falciparum, the benchmarking framework, not the parameters, are broadly applicable to other sexually recombining species. Lastly, they extensively updated multiple figures to include simulation models, results from simulation replicates, and improved the figures from the previous version of the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101924.3.sa2](https://doi.org/10.7554/eLife.101924.3.sa2)

Summary:

Guo et al. benchmarked and optimized methods for detecting Identity-By-Descent (IBD) segments in Plasmodium falciparum (Pf) genomes, which are characterized by high recombination rates and low marker density. Their goal was to address the limitations of existing IBD detection tools, which were primarily developed for human genomes and do not perform well in the genomic context of highly recombinant genomes. They first analysed various existing IBD callers, such as hmmIBD, isoRelate, hap-IBD, phased-IBD, and refinedIBD. They focused on the impact of recombination on the accuracy, which was calculated based on two metrics, the false negative rate and the false positive rate. The results suggest that high recombination rates significantly reduce marker density, leading to higher false negative rates for short IBD segments. This effect compromises the reliability of IBD-based downstream analyses, such as effective population size (Ne) estimation.

They showed that the best tool for IBD detection in Pf is hmmIBD, because it has relatively low FN/FP error rates and is less biased for relatedness estimates. However, this method is less computationally efficient.

Their suggestion is to optimize human-oriented IBD methods and use hmmIBD only for the estimation of Ne.

Strengths:

Although I am not an expert on Plasmodium falciparum genetics, I believe the authors have developed a valuable benchmarking framework tailored to the unique genomic characteristics of this species. Their framework enables a thorough evaluation of various IBD detection tools for non-human data, such as high recombination rates and low marker density, addressing a key gap in the field.

This study provides a comparison of multiple IBD detection methods, including probabilistic approaches (hmmIBD, isoRelate) and IBS-based methods (hap-IBD, Refined IBD, phased IBD). This comprehensive analysis offers researchers valuable guidance on the strengths and limitations of each tool, allowing them to make informed choices based on specific use cases. I think this is important beyond the study of Pf.

The authors highlight how optimized IBD detection can help identify signals of positive selection, infer effective population size (Ne), and uncover population structure.

They demonstrate the critical importance of tailoring analytical tools to suit the unique characteristics of a species. Moreover, the authors provide practical recommendations, such as employing hmmIBD for quality-sensitive analyses and fine-tuning parameters for tools originally designed for non-P. falciparum datasets before applying them to malaria research.

Overall, this study represents a meaningful contribution to both computational biology and malaria genomics, with its findings and recommendations likely to have an impact on the field.

Weaknesses:

One weakness of the study is the lack of emphasis on the broader importance of studying Plasmodium falciparum as a critical malaria-causing organism. Malaria remains a significant global health challenge, causing hundreds of thousands of deaths annually.

While the study provides a thorough technical evaluation of IBD detection methods and their application to Pf, it does not adequately connect these findings to the broader implications for malaria research and control efforts. Additionally, the discussion on malaria and its global impact could have framed the study in a more accessible and compelling way, making the importance of these technical advances clearer to a broader audience, including researchers and policymakers in the fight against malaria. In the revised version, the authors have placed greater emphasis on this aspect, while still maintaining the methodological focus of the paper.

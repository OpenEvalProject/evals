# Peer review - Round 1

Editors:
- Howard Y Chang, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65146.sa1](https://doi.org/10.7554/eLife.65146.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors provide an improved method to detect R-loops genome-wide. The method provides improved signal-to-noise ratio and strand-specific information that are advantageous to existing methods. This method should be useful with increasing interest in R-loops in control of gene regulation and genome stability.

Decision letter after peer review:

Thank you for submitting your article "BisMapR: a strand-specific, nuclease-based method for genome-wide R-loop detection" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Howard Y Chang as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Wulfridge and Sarma describe a new approach to map R-loops genome-wide. Using sodium bisulfite conversion, the ssDNA of the R-loop is targeted and specifically the DNA hybridized to the RNA in the R loop is sequenced. The approach yields strand specific information on where R-loops form and at high resolution. While the approach might be an important advance, some results don't make sense which prompts concerns about the possibility of artifacts or strong biases.

Essential revisions:

1) Comparison of BisMapR with alternative methods to clarify the methodologic advance.

a) If strand-specific library construction kit is used in MapR the authors may achieve strand-specific detection already. Please justify why bisulfite treatment is needed.

b) The authors compare their data to another approach that maps R-loops in a strand specific manner, DRIPc-seq. The two methods give strikingly different results. The authors do not give any rationale for why this is. Could BisMapR be extremely selective? Perhaps it is only mapping the most stable R-loops, those that can form G-quadraplexes or are stabilized by another mechanism.

c) Comparison with single stranded DNA detection method like KAS-seq would be informative. Single-stranded DNA is a kind of proxy for R-loops. BisMap-R should provide richer data but may need more cells and may not be applicable to clinical tissue samples.

2) Biological insight of divergent transcription at promoters and enhancers.

Divergent transcription: The authors rightfully cite the bias of R-loops on the template strand as evidence that their approach works (Figure 2C). They also mention that they see R-loops in the region upstream of TSSs, which they reason arrive from antisense divergent transcription seen at upstream of most mammalian promoters. However, the authors see both template and non-template signal at these locations at identical levels. How is this possible? There wouldn't be template RNA before the TSS. With the purported resolution of the method, this should be resolvable.

Enhancers: The authors find that bidirectionally transcribed enhancers have an R-loop only on one strand. This is extremely striking and if true, a remarkable discovery. However, it may just reflect the propensity for BisMapR to map the most stable R-loops.

a) How does DRIPc-seq data look like at these enhancers?

b) The fact that some features are so different between group 1 and group 2 enhancers is confusing. First there are so many fewer Group 2 enhancers compared to Group 1. It suggests an asymmetry to which strand of the DNA R-loops form in, which does not seem possible. And then there is a higher GC skew for group 2 enhancers. The strand asymmetries are either clues as to what is going on or a potential computational artifact.

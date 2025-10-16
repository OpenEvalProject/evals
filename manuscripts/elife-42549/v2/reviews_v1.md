# Peer review - Round 1

Editors:
- Jonathan S Weissman, University of California, San Francisco United States

Reviewers:
- Michael R Schlabach, KSQ Therapeutics United States

## Review text

DOI: [10.7554/eLife.42549.043](https://doi.org/10.7554/eLife.42549.043)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "High-fidelity circular synthesized CRISPR/Cas gRNAs for functional interrogations in the coding and noncoding genome" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal his identity: Michael R Schlabach (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Given the nature of this contribution the editors recommend this be reconsidered as a Tools and Resources paper rather than as a Research Article.

Summary:

In this manuscript, Wegner et al. describe an innovative approach to generate pooled sgRNA or shRNA libraries. Such libraries are now ubiquitously used as part of functional genomics efforts and thus an improved method to generate them is of high significance and utility.

Essential revisions:

The paper has now been seen by three reviewers. There was broad enthusiasm about the approach for generating complex libraries. However, there were concerns about some aspects of the work and a general feeling that the paper would benefit by streamlining the presentation to focus on the most solid and novel aspects of the method.

Four areas of concern are highlighted below:

1) There was general enthusiasm for the library generation strategy and as well as the value of an alternate approaches to create high diversity complex libraries. That said there were concerns that the comparison to alternate PCR-based approaches may not fairly represent how well those approaches can work when carefully implemented. Although there were some differences on this point, it seems that the most conservative and time efficient way to respond to these concerns would be to generally emphasize the capabilities of the present strategy and avoid relative comparisons unless they are directly substantiated by side-by-side comparisons. Additionally, since this is primarily a methods paper, it was felt that a better description of the workflow, including time and reagent requirements would be important to address in revision. For example, in the text or as a table/figure, the workflow Figure 1A could be fleshed out to provide more specifics about time and yields.

2) There was concern that, while the underlying quality of the DUB screen may be high, that the analysis strategy is not well validated. The raw sequencing data output of the screen should be analyzed by one or more of the established hit-calling methods (e.g. MAGeCK) to provide a better sense of the robustness of the hits as well as the real world performance of this library.

3) There is considerable concern about the conclusions from the TGW screens. While there is an appreciation for the innovative nature of the approach, the quality of the results, both in terms of the completeness and false positive rates, is difficult to evaluate given the data presented. Short of what would likely be a major experimental and analytical effort, the authors should tone down the claims and present this as an exploratory effort. For example, limitations such as very low reproducibility and the need to allow multiple mismatches to map sgRNAs should be discussed alongside the need for extensive validation.

I also pass on a couple of the specific reviewers' comments to provide context for the above:

Regarding analysis of the DUB screen: The section on the DUB screen is a bit convoluted and would benefit from using standardized analysis methods and a more focused discussion of the screen results for example by omitting the GO term analysis, which does not add very much.

To analyze the data, the authors sum sgRNA counts overall genes, but the more established approach in the field would be to calculate phenotypes for each sgRNA and to then aggregate these into gene-level phenotypes and derive p-values using statistical tests. Standardized pipelines exist to perform these analyses, such as MAGeCK. These phenotypes should also be compared to those from negative controls, both non-targeting controls and neutral-cutting controls, in particular given that the cell line used by the authors is p53-positive.

In addition, the assessment of screen quality by read counts across replicates is not fair; this should be a comparison of sgRNA enrichments across replicates. The variation (and correlation) in read counts stems almost entirely from differences in the starting abundances of sgRNAs in the library. Finally, Figure 3—figure supplement 1G should perhaps just be a scatter plot of the two sets of phenotypes against each other; the current representation is biased by the sorting and makes the data look better than they might be.

Regarding the TGW screen: The tgw screens should be de-emphasized on results and a more frank description of the shortcomings of it as an exploratory technique, assuming they don't want to do more work to figure out what any of these guides are really doing. That was my major objection with the manuscript.

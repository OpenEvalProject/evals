# Peer review - Round 1

Editors:
- Noam Kaplan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34077.070](https://doi.org/10.7554/eLife.34077.070)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Insulation of gene expression by CTCF and cohesin-based subTAD loop structures" for peer review at eLife. Your article has been favorably evaluated by Jessica Tyler (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers overall appreciated the extensive analysis performed by the authors, and recognized the potential impact of this work upon further analysis. A major concern raised by all reviewers is that further evidence is required to better characterize the subTAD predictions made by the authors and relate these to known phenomena. The reviewers suggested using the available high-resolution Hi-C datasets by Rao et al., 2014 and Bonev et al., 2017 to comprehensively evaluate how the subTAD predictions made by the authors relate to small TADs and localized loop interactions which were found in these datasets. If successful, such an analysis will significantly strengthen the applicability of this approach as an alternative for high-resolution Hi-C. This would allow to evaluate whether loop interactions detected in Hi-C are mostly explained by convergent CTCF interaction. Together, these would significantly strengthen the paper.

In addition, the reviewers suggest restructuring the manuscript such that previously known results and anecdotal results are made less central in the manuscript (e.g. by moving these to the supplement).

Reviewer #1:

In this work the authors extend a previously-published computational method, that uses ChIP-seq data to predict chromatin loop structures, in order to identify loops within TADs. They refer to these loops as subTADs (confusing terminology, see below). Based on this method and on several published datasets, the authors analyze several aspects of the relations between TADs, subTADs, epigenetic state and gene expression. Their main biological result suggests that subTAD loop anchors are functionally similar to TAD loop anchors.

While the presented method is useful, taken together, in my view both the methodological and biological findings in this manuscript are not of sufficient novelty.

1) The authors define subTADs as intra-TAD loops which are anchored by CTCF and cohesin. This definition is very confusing, since the term TAD typically refers to a domain-like square/triangle interaction pattern in 3C-type experiments, and subTADs are typically defined as TAD-like patterns that are contained within larger TADs (e.g. Phillips-Cremins Cell 2013). It has been observed that TAD patterns often have end-to-end loop patterns (by loops I mean local peaks in Hi-C, as defined by the authors), but these phenomena are generally distinct as some TADs do not show localized looping interactions and some looping interactions appear outside TADs.

2) However, this is more than an issue of terminology, since the subTAD loops detected in this work may actually just represent small TADs. If this is the case, there may not be any reason to expect them to behave differently than other larger TADs, simply because the decision of what is called a TAD vs. subTAD is quite arbitrary in TAD-detection methods. In other words, the finding that TAD anchors are functionally similar to subTAD anchors may be of little novelty if the methodological distinction between the two is not clearly motivated.

3) In terms of methodological novelty, the method used to predict subTAD loops is novel but incremental, as its core has been published (prediction of loops based on CTCF ChIP-seq and motif directionality). The authors extend it to include cohesin occupancy and filter some loops so that they do not overlap TAD loops etc., but this extension is not a conceptual advance in the method (in fact the panel explaining the method is very similar to a panel from the previous paper describing the method).

4) Some of the analyses in the manuscript are of little novelty and are only indirectly linked to subTAD analysis (e.g. Figure 1 is a general analysis of TADs (A-E) and the association between gene expression and chromatin state (F-H); Figure 4 presents an analysis of enhancers and super enhancers, mostly unrelated to TADs or subTADs).

5) As far as I understand, "other CAC" sites will mostly be weak sites that did not pass the filters (this is supported by Figure 2F). How do we even know they are real sites? Given this observation, it may not be meaningful to compare with them.

6) The same goes for "other CTCF" sites: looking at Figure 2F, the ChIP signal shows they are mostly not actual sites.

Reviewer #2:

In the manuscript "Insulation of gene expression by CTCF and cohesin-based subTAD loop structures" Mathews and Waxman provide a detailed characterization of their CTCF and cohesin ChIP-seq on mouse liver. They focus on TADs and characterize their features with the help of published datasets. The characterization is later use as a proxy to compare TADs with identified/predicted subTADs. They use a previously published algorithm, to predict TADs, modified by the authors to predict subTADs by considering genomic and structural parameters. Furthermore, they identify enhancer, insulators and super-enhancers specific to mouse liver with the help of previously published data. They end by experimentally testing a subTAD insulation containing a super-enhancer.

I would recommend for publication in eLife with major modifications.

1) It is this reviewer's opinion that an essential part missing from this manuscript is for the authors to clearly show examples of subTADs that are not detected by Hi-C or ChIA-PET but are indeed predicted by their computational method. This will help the readers make sense of the very detailed bioinformatics analyses and bring home the relevance of the prediction of subTADs.

2) Why use 4C and not 5C, capture Hi-C or similar approach where you would be able to visualize your subTADs. I understand these approaches cost can be higher yet if not that at least the addition of extra viewpoints inside and outside the subTADs would be needed to show the insulation experimentally. Although unlikely, what is shown here can simply be explained by the 4C interaction frequency dropping exponentially from the viewpoint that is conveniently located at the center of the subTAD.

3) The extent of how the authors modified the method previously published and improved upon is largely unclear. I strongly suggest they make the code/scripts available to the community for all of their analyses otherwise their contributions most likely will remain unnoticed/unused.

4) Concerns about novelty: besides the obvious similarity from approaches published before additionally there is a paper found on bioRxiv (Predicting CTCF-mediated chromatin interactions by integrating genomic and epigenomic features. Kai et al., 2017) that predicts subTADs based on machine learning of ChIA-PET results. Might be helpful to discuss the pros/cons between methods.

Reviewer #3:

The authors build on a previous method that uses CTCF binding and orientation (and predicts nearly 60k loops of average length 61kb) to define subTADs that are strictly contained in TADs and are fewer in number than the original method that predicted 60k loops. Motivated by other recent findings they incorporated cohesin ChIP-seq data as well as TAD boundaries, TSS overlap and consistency across replicates and trained their model to come up with a target number of approximately 10k (number of contact domains identified from 1kb/5kb resolution Hi-C data) subTADs with convergent CTCF sites on their boundaries. Even though there is not much in terms of robustness and stability analysis of some selected parameters and targets, their approach is mostly justifiable by the literature and what we know about TADs.

The manuscript thoroughly characterizes the properties of these newly defined subTADs in mouse liver and compares them to TADs and several other types of "domains". Main conclusions are that subTADs are slightly weaker but smaller versions of TADs that carry all key TAD features and provide finer-scale control of gene expression.

1) My one main concern is the missing out on an opportunity to clearly distinguish these subTADs from the contact domains defined by Rao et al., 2014 paper on several different cell lines. All the data needed to perform subTAD predictions are available for most (if not all) of these cell lines and a clear, cell-type matched comparison of what subTADs are and how they overlap with contact domains (as well as the subset of loop domains). Only in Figure S4C there is an indirect comparison of contact domains from a mouse B-cell lymphoma cell line (CH12-LX) and subTADs from mouse liver. I think it is crucial for the field to understand similarities and differences of many different definitions of domains and subdomains in order to converge to a consensus. This paper could have done more towards that goal.

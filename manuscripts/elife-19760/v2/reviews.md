# Peer review - Round 1

Editors:
- Karen Adelman, Harvard Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19760.030](https://doi.org/10.7554/eLife.19760.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Compact and highly active next-generation libraries for CRISPR-mediated gene repression and activation" for consideration by eLife. Your article has been favorably evaluated by Jessica Tyler (Senior Editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Pooled CRISPR screenings have become important methodologies to quickly associate genes with their functions in a high-throughput fashion. These platforms include gene knockout screens, gene inactivation (CRISPRi) and activation (CRISPRa). For such powerful technologies, it is important to further boost their efficacy and minimize any potential off-target effect. This manuscript deals with this very issue, and describes a systematic analysis of features that enable effective short guide RNA (sgRNA) activity in CRISPRi or CRISPRa screens. The result is new, highly effective libraries containing 5 or 10 sgRNAs per gene. These new libraries are compact and will be powerful tools for discovery of gene function moving forward.

Specifically, the manuscript details the use of machine learning algorithms and other informatic approaches to determine what features render a sgRNA most effective. Key aspects involve targeting a nucleosome-depleted region and the position from the observed transcription start site (using the more accurate FANTOM positions for TSS designation). These properties, coupled with specific sequence features can be combined to predict very active sgRNAs. The authors do a great job demonstrating the effectiveness of their predictions and the new CRISPRi libraries. This clearly establishes the promise of CRISPRi as a potent methodology that avoids a number of the pitfalls that using catalytically active CRISPR/Cas9 entails.

To facilitate dissemination of this knowledge, they have made the libraries available on Addgene (in 5 or 10 sgRNA per gene varieties) that target mouse or human genes. Further, they share the sequences of the best sgRNAs in supplemental tables, additionally increasing the impact and breadth of this work.

In short, this is a nicely written story with convincing data. I have only a few changes to suggest to the text and display items. These are aimed at making the manuscript maximally helpful to people in the field who might be designing their own guides against non-coding RNAs, as well as increasing the interest for those who are just curious about how CRISPRi works.

Essential revisions:

1) Authors claimed that the next-generation libraries for CRISPR-mediated gene repression and activation have higher activity than the old version. The experimental demonstration for new version of CRISPRa is completely missing. It's therefore premature to make such statement in the title and in the context. This issue should be clarified.

2) The new version of library outperform the old version, mostly based on statistic prediction and analysis. However, one might argue that the original library is "good enough" with "sub-optimal" performance in the identification of genes' function in majority of cases. It would be much more convincing if they could show examples of genes identified from new libraries that would be missing in the old fashion way. In this case, comprehensive validation of these candidate genes are needed to make such a claim.

3) Authors said that the new CRISPRi screen has undetectable non-specific toxicity seen with CRISPR nuclease approaches. This is actually the feature of CRISPRi, not the new design of CRISPRi library. It's misleading to give such credit to the new algorithm of design.

4) Likewise, we couldn't quite get the point why the new library would have improved off-target effects. It's understandable that the new design might improve the on-target activity. As to the off-target rate, it's puzzling to understand the mechanism behind this observation.

5) Although the effects of nucleosomes (DNAse, MNase, FAIRE) on positioning of sgRNAs for CRISPRi is strong, the importance for CRISPRa seems quite modest from the data presented- with position relative to the TSS being much more important. Why might this be? I am not convinced that this means that activating guide RNAs are indifferent to nucleosomes (and the authors don't suggest this). So why the difference? It would be helpful to the community to get some comment on this. As the manuscript stands, one could interpret the findings to say that one needed to target nucleosome-depleted regions to inhibit gene expression, but that activating guides could more readily penetrate chromatin, which seems unlikely. Could the authors clarify?

One possibility is that the optimal location upstream of the TSS (which appears to be -100 to -200 upstream) is typically nucleosome depleted at most active genes and so there isn't much dynamic range in the nucleosome signal detected in this region. This would compress the information you could get out of this parameter, perhaps making it seem less important because there was less variability among genes.

6) Given the above distinction, it would be preferable to show the score contribution for 'target site position relative to TSS' and 'target site chromatin accessibility' separately for CRISPRi (Figure 1C) as well as CRISPRa (Figure 2C).

7) Can the authors comment on the very strong peak of effectiveness for CRISPRi sgRNAs just downstream of the TSS? This likely reflects something in addition to nucleosome-deprivation as being helpful for CRISPRi. I find the very sharp peak in maximal activity in Figure 1—figure supplement 1 to be really striking (even in comparison to previous work using less well-refined TSSs), and would encourage its inclusion in the final manuscript.

As the authors have noted before, CRISPRi really works best when the guide is positioned just downstream of the start site- perhaps because it is more effective to block early transcription elongation and the release from Pol2 pausing, rather than farther downstream once Pol2 is loaded with the machinery to plow through chromatin etc.?

For those working to block expression of novel or non-coding RNAs, we think it is worth getting this idea out there in a super-clear and obvious way- that the sweet spot for optimal guides is right downstream of the promoter.

8) Regarding the basic sgRNA prediction algorithms developed, will these be shared upon request? We see a github site for the tool created to assess chromatin features, but not for the broader prediction platform. Could the authors indicate in the Methods how an interested user might get help with sgRNA predictions?

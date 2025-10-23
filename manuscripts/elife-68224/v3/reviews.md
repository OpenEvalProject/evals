# Peer review - Round 1

Editors:
- Koichi Kawakami, National Institute of Genetics Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68224.sa1](https://doi.org/10.7554/eLife.68224.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "The landscape of regulatory genes in brain-wide neuronal phenotypes of a vertebrate brain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Koichi Kawakami as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers recognized the authors performed enormous amounts of works and the data presented in the manuscript should be useful resources for neurobiologists. However the reviewers indicated the following major concerns which should be addressed by the authors.

1) The validity of clustering. The reviewers think the authors need control analysis for this.

2) For "divergent" and "convergent" classes, the hypothesis presented by the authors were not proven. To experimentally prove this is a bit too much for the present paper. Instead, the reviewers request more statistical data to support these ideas.

Reviewer #1:

In this manuscript, the authors performed single cell RNA-seq analysis of ~46,000 cells from the zebrafish larval brain and identified 68 clusters and mapped them on the brain regions. They found (1) region-specific markers, (2) correlation with cell types in juvenile fish, (3) 1099 effector genes out of 1402 genes used to define the clusters, (4) and 48 neuronal clusters and 20 non-neurons including glia. Then, they analyzed scRNA-seq using vmat (monoaminergic) and vachte (cholinergic) transgenic fish and (5) identified 22 and 14 neuromodulator clusters. (6) The neuromodulator clusters were further analyzed for neurotransmitter types and they revealed coexpression patterns.

In the hierarchical classification, they identified (7) 11 "sister clusters" that have similar expression profiles for effector genes, that had the same neurotransmitter types but did not show brain region preference. Then they examined TF profiles in neurotransmitter type neurons and identified 14 TF sister clusters. They found (8) one effector gene cluster that match with a TF cluster (matched) and 10 effector gene clusters that did not match with TF clusters (convergent) (these expressed the same neurotransmitters), and also found (9) neuromodulator clusters were well matched with TF profiles (matched). (10) They found the same TF clusters can express different effector genes also (divergent).

Then they aimed to see relationship between TF and morphology. They sorted tectal glut cells and identified 11 TF clusters. Then they made Bac-gal4 for 15 TFs and performed intersection using Cre-glut. (11) They analyzed 574 tectal neurons and found that TF could mark multiple morphology.

Since (in the divergent class) TF did not correlate with effector, they analyzed RNA binding proteins. (12) RNA-binding proteins were expressed differently in different neuron clusters.

Strength: The authors performed a comprehensive analysis of brain cells by single-cell RNA-seq. The scRNA-seq data presented here will be a good reference when the neuroscientists study a certain neuronal types, for instance searching for marker genes expressed in the neuronal clusters of their interest. Also, the amount of work is enormous.

Weakness: The contents of this paper are rather descriptive and poor in mechanistic aspects (causal relationship). Also I felt difficulty in following the manuscript since experiments were not described as hypothesis-driven.

1) The authors prepared cells for sc-RNA seq in different ways and this made the manuscript a bit confusing. Please clarify the purpose and reason for the to do so.

2) I think only "positive" data is the identification of the "matched" class. For "convergent" and "divergent" classes, many other explanations will be possible since there are no mechanistic analysis. For "convergent" class, examine if any TFs with weak expression had been overlooked. For "divergent" class, examine if the authors can find specific (classes) of RBP as real candidates.

3) As for the section describing the morphology, 11 clusters identified, and the 7 morphological classes seemed irrelevant. Also, relationship between 6TFs and the 7 morphological classes did not sound although the work for construction of 15 BACs should have to be enormous. Rewrite the section for readers to be understandable.

Reviewer #2:

In this study, the authors investigated how diverse neuronal types develop in the brain by using single-cell RNA sequencing methods.

The authors performed rigorous data collections for different brain regions, monoaminergic neurons, catecholaminergic neurons, and glutamatergic neurons. Such careful data collection for different types of neurons and brain regions has not been done for larval zebrafish. Their data will be a valuable resource for the neuroscience field.

They further found that the expression patterns of transcription factors are not necessarily predictive of the expression patterns effector genes that constitute the "terminal features" of neuronal cell types. Such predictiveness depends on the cell types. In neuromodulatory neurons, TF expression is predictive of effector gene expressions. On the contrary, in "neurotransmitter" neurons, which represent glutamatergic and GABAergic neurons, this relationship is loose and diverse. This finding, if confirmed, will advance our understanding of how diverse neuronal types develop in vertebrate brains.

The major weakness of this study is the lack of statistical controls in their analyses. I raise two examples here. First, the classification of "convergent types" and "divergent types" is solely based on hierarchical clustering analysis and its distance measures which are not validated by sub-sampling or by other statistical methods. Therefore, this analysis cannot rule out the possibility that such classification arises from large variations of gene expressions within the analyzed populations and that there are no such distinct populations.

The second example is their analysis of the expression of RNA-binding proteins. They show that the RBPs have differential expression in "divergent" cluster pairs. However, they do not show whether such differential expression is more prevalent among "divergent" cluster pairs than in other neuronal cluster pairs. If this is not the case, the differential expression of RBPs may not be the reason for the differential expression of effector genes.

Although the claim of this paper may be of broad interest in the neuroscience field, the above weaknesses significantly affect the reliability of the conclusion of this paper. Therefore, I recommend a revision of this manuscript for its publication in eLife.

1) The classification of "convergent" and "divergent" types in Figure 3 needs quantitative validation to exclude the possibility that such classification arises from large variations of gene expressions. This problem is unavoidable for analyses that solely rely on hierarchical clustering methods and their distance measures. Showing expression patterns of several example genes does not reinforce the conclusion, as it is always possible to find genes that show differential expression between any given cluster pairs. The result of neuromodulatory neurons only works as a partial control, as they are different neuronal types. This study needs to reinforce the validity of the classification by cross-validation of cluster distances among samples or by using unbiased statistical methods other than clustering.

2) The analysis of differential expression of RNA-binding proteins among "divergent" neuronal clusters needs statistical control. The authors need to show that RBPs in "divergent" pairs have more divergent expression patterns than in "convergent" pairs in an unbiased, quantitative way. Again, showing the example of few genes is not enough. Otherwise, RBPs cannot explain the divergence of effector gene expression from similar TF expression profiles.

3) The coloring schemes in figures are confusing. For example, I can see many color schemes in Figure 1. We only need two types of classification: (1) brain regions and (2) cell types. Figure 1a may not need colors/numberings and only need names for some of the clusters. Also, the classification presented in Figure 1c (Glu-GABA-P-R) and the one presented in Figure 1g (I- II, III, IV, V) are redundant. I understand that these different schemes serve different purposes, but I recommend unifying these classification schemes for clarity. This unification may need reordering of figure panels.

Reviewer #3:

In this manuscript, the authors performed single-cell RNA sequencing of >60,000 cells across the whole zebrafish brain with region- and molecular- identity. Using the acquired transcriptomes, the authors tried to deduce the regulation logic of neuronal diversification by comparing sister clusters in hierarchical clustering based on effector genes and regulatory TFs. The author showed that while TF similarity in modulatory neurons largely predict the similarity of their neuromodulator types, neurotransmitter types and their TF profiles usually do not agree. Further analysis of cell-type divergence from common TF regulators revealed an interesting differential enrichment of RNA binding proteins, which are potentially involved in post-transcriptional regulation of neuronal identity.

The transcriptomic data is comprehensive and of high quality, with cells covering the entire zebrafish brain, and with close-up analysis generated by new experiments to give higher discriminatory power. The data offers a valuable resource to the developmental neurobiology community. Some patterns (e.g. phenotypic convergence) echoes the findings in invertebrate nervous systems. Difference in regulatory logic of neurotransmitter vs. neuromodulator types, as well as the identification of post-transcriptional regulator genes are novel and interesting.

However, some caveats in data analysis may affect the reliability of the conclusions. The key claims in the study heavily relied on analysis of "sister clusters", i.e. clusters of cells with most similar TF or effector gene profiles. Yet not enough justification was given to the selection of such clusters or the focus only on the direct sibling clusters, and the fact that neurotransmitter and neuromodulator data were acquired differently adds complication to the interpretation of the result. Meanwhile, although the descriptive data in this study gives a detailed account of neuronal diversity, the lack of causal evidence and/or concrete mechanistic explanation between regulatory genes and terminal effectors rendered the conclusions a bit elusive -they tend to fell into providing interesting insight while failing to account for alternative explanations.

Overall, I think the claims are supported by the data for the most part, and with the addition of certain control and additional analyses, it enhances our understanding of vertebrate neuronal diversification as a thought-provoking descriptive study: Genes involved in convergent or divergent cell types identified in this study serve as curious candidate for follow-up investigation. Regulatory logic and mechanisms, when compared with similar studies in invertebrates, can help us to gain insights on the origin and evolution of the nervous system.

1. In the first and second section of Result, clusters of the transcriptome data were treated as the "smallest unit" for subsequent analysis. However, there's a lack of justification for the clustering criteria: i.e. how distinct the clusters are, and how robust the subsequent analysis result is if cell-type clustering is performed slightly differently. This is especially problematic because even the authors themselves have shown that given cleaner quality data (e.g. modulatory neurons in FAC sorted cells vs. whole brain), clustering partition could be different. Additional control analysis would be necessary to show clustering makes sense and robust to noise level in the data.

2. The authors compared the 8dpf brain transcriptomes with juvenile brain in Raj et al., 2018 and claimed that "are likely to represent the full cellular diversity of the mature zebrafish brain". The stretch is a bit far because they partitioned the data only using variable genes expressed in both datasets, i.e. differentially expressed genes involved in subsequent diversification were not accounted for. I think at best this analysis serves as a similarity claim rather than "full" cellular diversity.

3. Result Section 3: a major weakness in the design of analysis is the focus only on "sister clusters", which can be sensitive to your cluster partition and does not necessarily represent the real diversification event. To compare the landscape of TF and effector gene expression, there are many alternative methods accounting for the full spectrum of cell types rather than just the most similar sibling clusters. I would suggest two supplementary analyses: (1) A population-level statistical analysis to show the difference in regulatory logic across all cell types regardless of clustering, even in the less similar cells. (2) A test to ensure that the disagreement between TF and effectors does not disappear as we break clusters in neurotransmitter types into smaller sub types. As stated in point #1, it is necessary for the authors to demonstrate the difference in regulatory logic between transmitter and modulator types is not a result of different noise level in the data.

4. Result Section 4: the criteria for assigning TF expression to morphology class is again relying too much on binary classification. In particular, the authors considered a TF to be a marker for the morphology class "appeared for at least 4 times". The morphology classes are very different in sizes and this is an unfair comparison. Rather more quantitative metrics and vigorous statistical tests should be used to support this conclusion.

5. Result Section 5: in addition to transcriptome data, it would be nice if the authors can demonstrate some causal links between the RBP genes and the cell type regulation, or verify experimentally that they indeed encode neurons with different identity, morphology or functions. If additional experiments to demonstrate causal links are not possible, the authors should sufficiently account for alternative explanations for cell type divergence. Besides post-transcriptional regulation, there are a lot of other factors that could affect gene diversification, including early regulators that are transiently expressed in the embryo that primed fate selection, and external signaling factors in the neuron's environment. Such information was lost as only mature neurons are sequenced with very little spatial context.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The landscape of regulatory genes in brain-wide neuronal phenotypes of a vertebrate brain" for further consideration by eLife. Your revised article has been evaluated by Didier Stainier (Senior Editor) and a Reviewing Editor.

The manuscript has been corrected but there are some remaining issues that need to be addressed, as outlined below:

The reviewers still think the data is a good resource, and the differentially expressed genes can be good candidates for future investigation. However, the reviewers think that cross-validation of their statistical measures that used to identify "matched", "convergent" and "divergent" types is necessary. They used two measures in parallel, hierarchical clustering, and population-level similarity, to identify these pairs. These measures can be made robust by repeating the sub-sampling of genes and average statistics over many sub-sampling calculations. The reviewers wonder how much of it remain true with sub-sampling test added. Or alternatively, the reviewers would suggest moving away from hierarchical clustering and instead re-identifying matched, convergent and divergent populations based on TF-based and effector-based distance measures, which is bootstrapped to ensure robustness. This will provide more interpretable, consistent results.

Reviewer #1:

I found that the authors performed Jaccard similarity index-based analysis to validate clustering and rewrote the text. However, these revealed some weakness of the manuscript. I have the following comments.

1. The paper lacks biological aspects. The authors identified sister clusters from different brain regions (p11, line 234). The authors should at least discuss the significance of the finding.

2. The authors separated IIa and IIb before classification using TF profiles. I am wondering why?

3. A paragraph (p12, lines 249-258), it is not clear how they performed the population-level statistical analysis. Explain more precisely.

4. Why did the hierarchical and population analyses make the difference? (p12) Explain. Also, I do not understand the meaning of making overlaps of these.

5. p13, line 277. I think the authors examined both the TF and effector profiles, correct?

6. p13, Again the paper lacks biological aspects. Why did the neurotransmitter-type and neuromodulator-type make difference? Explain the idea in the discussion.

7. p14, lines 287-297, on the other hand… this part seems redundant with the previous parts and, to me, was difficult to read. Please clarify.

8. p14-15. I admire their efforts to make many BACs. They mentioned this may support "divergent pattern"(p17, line 358), but the reason why they thought so is very weak. They need to show relevance between morphology and effector type somehow experimentally.

9. p16, line 340. They did not describe how they picked up 6 TFs.

10. Figure3—figure supplement 2D and 2F. Figure3—figure supplement 4B. I could not tell how to read these data. In addition, in all cases, the effector-based distances are small (between 0-0.1) and TF-based distances are large (between 0.1-0.4). I don't see much difference between these populations.

Reviewer #2:

I have to say the authors did not address my concerns at all.

My first concern was about the validity of "matched", "convergent" and "divergent" classifications from hierarchical clusterings that are based on effector genes and TF genes in Figures 3 and 5. As an answer, the authors calculated Jaccard similarity indices for clusterings using all genes in Figure 1 and Figure 2. These added analyses were completely unrelated to the clustering of "matched", "convergent" and "divergent." Therefore, I have to say the authors did not address the issue.

My second concern was about the validity of their claim about the differential expression of RBPs in "divergent cell population". They claim that the RBPs have more divergent expressions in "divergent cell pairs". However, it is hard to interpret the statistics presented in Figure 5E. The indication of the index [(number of genes that are solely divergent in group A) / (number of all genes that are divergent in group A)] is unclear.

Moreover, this analysis does not indicate any causality between the divergence of RBPs and the divergence of effector genes. In principle, the more heterologous the population is, we would see more divergence of RBPs and effector genes. These factors are not independent of each other. I was expecting to see a more careful statistical approach that takes these considerations into account. Therefore, I have to say the authors did not address the issue.

Reviewer #3:

In the revised manuscript, the authors mainly added three additional control analyses that increased the credibility of the conclusion, including:

1) Robustness analysis of the clustering result using Jaccard similarity of subsampled data.

2) Analysis of the matched/convergent/divergent patterns of the glutamatergic/GABAergic neurons based on relaxed criteria that include not only the terminal sister clusters, but also non-sibling clusters with relatively close relationships.

3) Control analysis to show the enrichment of differential RBP expression in divergent patterns.

The control analyses largely addressed my concerns to a large extent, although they made the dramatic contrast between the regulatory logic of neurotransmitter and neuromodulator data weaker. The identified convergent/divergent events are now more convincing and allow for further exploration of the phenotype in the future.

However, I cannot help but noticed many more changes have been made without being pointed out in the rebuttal letter, including (1) exclusion of the data from the cholinergic neurons altogether, and (2) slightly different analysis result with seemingly identical input data (e.g. comparing Figure 3—figure supplement 2 in the new version vs. Figure 3 in the original manuscript). The authors should explain why such changes were made and ensure there is no selective report of the data.

Finally, some suggestions/questions to help achieve a better presentation of the data.

1) The current "population-level" analysis is rather just a relaxed definition of the terminal sister clusters, but there are many other metrics to quantify the similarity between the TF-based and effector-based clustering result over the entire dataset. For hierarchical clustering this can be editing distance between the two trees, or more generally, similarity between organization of TF and effector gene distribution across all the clusters. This will not identify specific matched, convergent or divergent patterns, but would be an unbiased measurement of how TF and effector landscape agree with each other.

2) Figure 3: similar color regime was used to represent forebrain/OT/sub OT and matched/convergent/divergent patterns. This is very confusing. I would suggest weakening brain region visualization (e.g. changing it to a less pronounced representation or getting rid of it altogether -see comment #3) and focus on the regulatory logic. It is also recommended to color the pattern names in 3B accordingly.

3) Figure 3C: The number of matched patterns on the Venn diagram does not match the number shown in Figure 3F. Also, Venn diagram is not the best way to show that the conclusion in sister cluster- and population-statistics are similar. [Minor correction: the number of selection should be Combination C(39, 2) rather than Permutation A(39, 2)].

4) Throughout the manuscript, the brain region identities are shown next to the clusters in every figure, yet very little conclusion was made about the relationship between transcriptome and brain region identity. The authors are advised to summarize the major findings of data feature related to brain region identities (no correlation can also be a finding), and simplify the color use of brain region when the color does not convey meaningful information.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The landscape of regulatory genes in brain-wide neuronal phenotypes of a vertebrate brain" for further consideration by eLife. Your revised article has been evaluated by Didier Stainier (Senior Editor), a Reviewing Editor, and the original reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1) Although for neurotransmitter-type, "sister cluster analysis and the population-level statistical analysis " are carried out. However, for neuromodulator-type, only sister cluster analysis was done. It is fair to perform population-level analysis for neuromodulator-type.

2) Line 265: largely recapitulated. I do not agree with this. Rather, explain why the results were not consistent.

3) Line 226: The TF Regulatory Landscape in Whole-brain Neuronal Phenotypes

This section is a bit too long. The section should be separated, for example, for neurotransmitter-type and neuromodulator-type.

4) Line 395: results supported "divergent" and "convergent" patterns, because divergent pattern indicated the link of same TFs to different neuron phenotypes, while convergent pattern indicated the link of different TFs to similar neuron phenotypes.

This is too much speculation. The relationship between the morphology and effector gene profiles are unclear. I think it is fair to say that morphology does not directly correlate with TF profiles.

Reviewer #2:

I can say the authors addressed my concerns on statistical analyses after this round of revision, shrugging off unnecessary parts and exposing the most interesting part of this study. In addition, they included a new analysis in Figure 5 which indicates potential causality between the differential expression of RBPs and differential expression of effector genes.

There are still concerns about the validity of classification (lower 10% of gene distance compared to shuffled pairs, how do you justify the threshold?). However, this justification will not be so straightforward because it will be prone to the intrinsic statistics of TF expression, effector gene expression, and the sensitivity of the sequencing technique. It is obvious this is the best authors can do. I advise authors to acknowledge such limitations in the discussion.

Reviewer #3:

Unfortunately, the authors misunderstood my request for adding Tree Distance analysis. An important claim of the paper was that glutamatergic/GABAergic clusters show different TF and terminal profile patterns ("convergent/divergent"), whereas neuromodulator type clusters predominantly expressed the same TF profiles ("matched"). However, supplementary analysis was only shown for the glutamatergic/GABAergic types but not the modulator types, and the main figure that supports this conclusion (Figure 3E) still uses sister clusters from hierarchical clustering for classification of neuromodulator types, which I found to be an unfair comparison. Also, the gene subsampling test of the robustness of matched/divergent/convergent pairs was only performed on similar pairs defined by population-statistics. It was not clear to me why the authors still adhered to the "sister cluster" definition (or an INTERSECTION of this strategy with the population-statistics), for all subsequent conclusions. I suggested tree distance as a global measurement of whether the glutamatergic/GABAergic types and modulator types truly have different regulatory logic at the population level, rather only at the terminal sisters.

# Peer review - Round 1

Editors:
- Juan Valcárcel, Centre de Regulació Genòmica (CRG) Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69148.sa1](https://doi.org/10.7554/eLife.69148.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript provides an evolutionary perspective of tissue-specific circRNA expression across 70 million years of primate evolution. The authors find that most circRNAs are not conserved, with the exception of a subset of approx. 700 brain-specific circRNAs. Interestingly, those circRNAs are characterised by increased length of the downstream intron during evolution due to the recent insertion of transposons.

Decision letter after peer review:

Thank you for submitting your article "Evolutionary dynamics of circular RNAs in primates" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The authors analyzed circRNA expression in several tissues across 9 species representing 70 million years of primate evolution. They report that while most circRNAs are species-specific, with the exception of a subset of approx. brain-specific 700 circRNAs. Common features of these circRNAs are their high PSI values, low number of exons, unique back-splicing junction sites and, most significantly, increased lengths of their downstream introns, which is associated with the insertion of young transposons. The authors propose that increased intron length provides a longer kinetic window for back-splicing events, which favors the production of circRNAs.

These results are timely and interesting, given current controversies about the general functionality of circRNAs and our limited knowledge of their evolution and regulatory mechanisms. However in our opinion the manuscript is in need of substantial revisions in two main fronts:

a) Improved data analyses, including validation of the nature of the circRNAs detected by their pipeline (e.g. using RNaseR), filtering by gene expression, more stringent specificity controls and cross-validation by other dedicated software tools.

b) Further contextualization of the findings, including properly citing and discussing previous essential literature that reported related findings and conclusions and revising causality claims based upon correlative associations.

Essential revisions:

a) Improved data analyses,

a.1. It is essential to document some type of validation of the circRNAs detceted (e.g. by RNaseR), as many back-splicing junctions can be caused by artifacts of reverse transcription or alignment.

a.2. Filtering for gene expression. When comparing features of conserved circRNAs and species-specific circRNAs, it is important to use similarly-expressed circRNAs for comparison, as using highly-expressed conserved circRNAs to compare with relatively lowly-expressed species-specific circRNAs might lead to biased conclusions. Similarly-expressed groups of conserved circRNAs and species-specific circRNAs should be selected for analyses (Figure 3B). In the current version, the authors selected circRNAs with at least 5 reads and ≥ 5% PSI for their analysis. However, since the sequence depths of different species vary largely (supplemental table 1) from less than 20 millions of reads in some samples to more than 120 millions of reads in some other samples, this selection of circRNAs with at least 5 reads and ≥ 5% PSI is biased across species and would be problematic for cross sample comparison due to unbalanced sequencing depths.

a.3. The authors used Whippet to analyze both circRNAs and linear RNAs. However, this tool was originally developed to analyze canonical splicing events, and it is unclear how it performs on circRNA prediction. In addition, it has been suggested to combine some other tools, such as CIRCexplorer and MapSplice, together for reliable circRNA prediction (e.g. Hansen et al., Nucleic Acids Res 2016). Otherwise, the authors need to show convincingly that using Whippet alone is better than the suggested tools. In addition, the authors should carefully quantify circRNAs by considering different sequence depths across samples.

a.4. A number of publications have shown the association of long introns with circRNA expression, and more importantly, that the pairing between flanking introns of circRNAs is required for circRNA biogenesis in mouse and human. In line 42, an important reference, Zhang et al., Cell 2014, PMID: 25242744, should be cited to mention that "inverted repeat elements that promote complementarity between adjacent introns favouring circRNA formation". Similar conclusions may be reached in this study. For example, in Figure 3B, L2_flank and L1_flank can be the key features that discriminate the conserved and species-specific circRNAs, while the pairing between them in flanking introns may be more important than intron lengths for circRNA formation. In this case, it might be biased to emphasize the importance of downstream intron length for evolutionary circRNA biogenesis.

a.5. To show the significance of the downstream intron lengths for conserved circRNA formation, the authors should use lengths of upstream introns of conserved circRNAs as internal controls.

a.6. It is also not clear how to solve the problem caused by multicollinearity when predicting elements for circRNA biogenesis. It is possible a collinearity between long downstream introns with their pairing between flanking (long) upstream and downstream introns.

a.7. It has been shown that expressed circRNAs are enriched with 2-3 exons in multiple early studies. In this case, the low number of exons might not be specific for conserved circRNAs, but commonly among expressed circRNAs. The authors can compare the numbers of exons of conserved circRNAs with those of expressed (except conserved circRNAs) and all expressed circRNAs.

a.8. On page 18 the authors defined relative TPM values. However, the definitions of circRNAsRead and GeneRead are not clear.

b) Further contextualization of the findings. Relevant aspects of the authors' findings have been previously reported and should be properly cited and discussed, including

b.1. The reports by Rybak et al. (Mol Cell 2015), Veno et al. (Genome Biol. 2015) and You et al. (Nature Neuro 2015, which is not even cited) described that brain circRNAs are conserved, as well as several of the features described for these circRNAs in the manuscript.

b.2. Consider the orientation of the inserted transposons (as showed in Chen LL et al., Cell 2014)

b.3. Extension of downstream introns and inefficient cleavage and polyadenylation are well described as factors modulating exon circularization (see Liang et al. Mol Cell 2017, Ashwall et al., Mol Cell 2014).

b.4. In the abstract the authors state that "many primate genes produce non-coding circular RNAs". This statement is not precise as it is not clear how many of the circRNAs are coding and how many non-coding. The non-coding should be eliminated. Moreover, seems like the authors don't even know about the research showing that some circRNAS are translated.

b.5. In line 41, the authors stated that "Back-splicing occurs co-transcriptionally" but it has been shown that back-splicing might occur not only co-transcriptionally (Ashwall Fluss et al. Mol Cell 2014) but both co-transcriptionally and post-transcriptionally (Zhang et al., Cell Rep 2016, PMID: 27068474).

b.6. The most important model of this paper is that insertion of young transposon into downstream introns results in longer intronic regions, which delay the RNA polymerase II to the next splice site and increase the possibility of circRNA conservation. However, it has been reported that "Pol II accelerates dramatically while transcribing through genes, but slows at exons" (Jonkers et al., eLife 2014) and "back-splicing outcomes correlate with fast RNA Polymerase II elongation rate" (Zhang et al., Mol Cell 2016). In this case, longer introns might lead to fast, but not slow RNA polymerase II for circRNAs.

b.7. This manuscript mainly showed the insertion of LINE for circRNA expression and conservation. However, previous studies have suggested the importance of SINE elements, especially Alu elements of primates, in circRNA biogenesis (for example, Jeck et al., RNA 2013, PMID: 23249747; Zhang et al., Cell 2014, PMID: 25242744; Dong et al., RNA Biol 2017, PMID: 27982734). Did the authors observe that Alu is less involved in primate circRNA expression than LINE? Or, since Alu is prevalent among primates, their contribution to conserved circRNAs is less important than LINE?

b.8. In line 39, the authors cited Guo et al., Cell 2020 to show as examples of functional circular RNAs especially in the immune and nervous systems, but it has nothing to do with circular RNAs.

b.9. In line 44, Quaking was not likely to be suggested to facilitate "these (assumedly inverted repeat elements) RNA-RNA interactions", instead, ADAR (Ivanov et al., Cell Rep 2015, PMID: 25558066; Rybak-Wolf et al., Mol Cell 2015, PMID: 25921068), DHX9 (Aktaş et al., Nature 2017, PMID: 28355180), NF90/110 (Li et al., Mol Cell 2017, PMID: 28625552) were suggested to be involved in inverted repeat element RNA-RNA interactions to regulate circular RNA biogenesis.

b.10. In line 67, the authors cited Pipes et al., Nucleic Acids Res 2013 to suggest their used datasets in this study. However, many samples originally in Pipes et al., Nucleic Acids Res 2013 had only mRNA-seq, without total RNA-seq Total RNA-seq datasets for many those samples were updated in Peng et al., Nucleic Acids Res 2015, which should be referenced.

c) Revising causality claims based upon associative correlations:

c.1. In line 101 the authors state "Many orthologous genes consistently express circRNAs even of the precise back-spliced junction is not conserved implicating importance of trans-factors in controlling cirRNA formation". There is no logic in this statement, long introns and random insertion of repetitive elements in inverse orientation could explain this w/o invoking any trans-acting factor.

c.2. The authors claim that "Anaylsis of the exonic structure of conserved circRNAs, showed that conserved circRNAs contain fewer exons, and rarely overlap with other circRNAs (Figure 2G, p = 4:08. 10*64, Fisher exact test; see Methods) displaying back-splicing at unique 5´- and 3´-splice sites. This indicates that these conserved circRNAs possess unique cis- or trans-regulatory features that enable a tight control of the number of exons within a circRNA and the back-spliced junctions used." This is not necessarily like that and the 2 aspects could be concurrent/codependent on a different factor (i.e. intron length).

c.3. After looking for predictive genomic features for circRNA biosynthesis the authors conclude that: "This indicates a core set of 24 cis- and trans-regulatory features drive the conserved formation of circRNAs compared to our background set of introns" This is factually and conceptually wrong, as opredictive value does not mean causality. So likely most of these factors are co-occurring, which is still interesting but should not be overstated.

Reviewer #2:

In this manuscript entitled "Evolutionary dynamics of circular RNAs in primates", Gabriela Santos-Rodriguez et al. analyzed the circRNA expression in severl tissue samples across 9 primate species. They showed that most circRNAs are species-specifically expressed, while a subset of circRNAs were neural tissue-specifically expressed across species. These conserved circRNAs commonly had high PSI values, low number of exons and unique back-splicing junction sites. After evaluated hundreds of potential regulatory elements that might regulate circRNA biogenesis, the authors found that the insertion of young transposons, which expands the lengths of downstream introns, may up-regulate the expression of circRNAs and could be involved in conserved circRNA expression. Although obtained these interesting conclusions, there are key concerns related with their applied methods and claims. For example, the authors used Whippet to analyze both circRNAs and linear RNAs. However, this tool was originally developed to analyze canonical splicing events, and it is unclear how it performs on circRNA prediction. In addition, it has been suggested to combine some other tools, such as CIRCexplorer and MapSplice, together for reliable circRNA prediction (Hansen et al., Nucleic Acids Res 2016 and etc.).

The main and most important model of this paper is that insertion of young transposon into downstream introns results in longer intronic regions, which delay the RNA polymerase II to the next splice site and increase the possibility of circRNA conservation. However, it has been reported that "Pol II accelerates dramatically while transcribing through genes, but slows at exons" (Jonkers et al., eLife 2014) and "back-splicing outcomes correlate with fast RNA Polymerase II elongation rate" (Zhang et al., Mol Cell 2016). In this case, longer introns might lead to fast, but not slow RNA polymerase II for circRNAs.

Meanwhile, a number of published references have shown the association of long introns with circRNA expression, and more importantly, the pairing between flanking introns of circRNAs is required for circRNA biogenesis in mouse and human. Similar conclusion can be obtained in this study. For example, in Figure 3B, L2_flank and L1_flank can be the key features that discriminate the conserved and species-specific circRNAs, while the pairing between them in flanking introns may be more important than intron lengths for circRNA formation. In this case, it might be biased to emphasize the importance of downstream intron length for evolutionary circRNA biogenesis.

When cited references of Barbosa-Morais et al., Science 2012 and Merkin et al., Science 2012, the authors stated that "gene expression is highly conserved between the same tissues in different species". However, Barbosa-Morais et al. have clearly mentioned in their abstract that "Within 6 million years, the splicing profiles of physiologically equivalent organs diverged such that they are more strongly related to the identity of a species than they are to organ type". In addition, Merkin et al. also stated that "alternative splicing is well conserved in only a subset of tissues and is frequently lineage-specific". Together, these cited papers emphasized the species-specific alternative splicing, which can be extended to back-splicing, as back-splicing is a new type of alternative splicing. In this case, alternative splicing (should include back-splicing) can, at least partially, explain the heterogeneous expansion in complexity across evolution.

Comments for the authors:

Additional analyses should be performed to address the concerns listed in public review with stringent setup for prediction and comparison. In addition, many mis-cited references should be also corrected, including those listed below.

1. The authors need to use other suggested tools that are specific for circRNA prediction for their analyses. Otherwise, the authors need to show convincing results that using Whippet alone is better than the suggested tools. In addition, the authors should carefully quantify circRNAs by considering different sequence depths across samples.

2. To show the significance of the downstream intron lengths for conserved circRNA formation, the authors may want to use lengths of upstream introns of conserved circRNAs as internal controls to draw this conclusion.

3. When comparing features of conserved circRNAs and species-specific circRNAs, it is better to used similarly-expressed circRNAs for comparison. Using highly-expressed conserved circRNAs to compare with relatively lowly-expressed species-specific circRNAs might lead to biased conclusion.

4. This manuscript mainly showed the insertion of LINE for circRNA expression and conservation. However, previous studies have suggested the importance of SINE elements, especially Alu elements of primates, in circRNA biogenesis (for example, Jeck et al., RNA 2013, PMID: 23249747; Zhang et al., Cell 2014, PMID: 25242744; Dong et al., RNA Biol 2017, PMID: 27982734). Did the authors observe that Alu is less involved in primate circRNA expression than LINE? Or, since Alu is prevalent among primates, their contribution to conserved circRNAs is less important than LINE?

5. More stringent comparisons and controls are needed throughout the study. For example, similarly-expressed groups of conserved circRNAs and species-specific circRNAs should be selected for analyses (Figure 3B). In the current version, the authors selected circRNAs with at least 5 reads and ≥ 5% PSI for their analysis. However, since the sequence depths of different species vary largely (supplemental table 1) from less than 20 millions of reads in some samples to more than 120 millions of reads in some other samples, this selection of circRNAs with at least 5 reads and ≥ 5% PSI is biased across species and would be problematic for cross sample comparison due to unbalanced sequencing depths.

6. It is also not clear how to solve the problem caused by multicollinearity when predicting elements for circRNA biogenesis. It is possible a collinearity between long downstream introns with their pairing between flanking (long) upstream and downstream introns.

7. It has been shown that expressed circRNAs are enriched with 2-3 exons in multiple early studies. In this case, the low number of exons might not be specific for conserved circRNAs, but commonly among expressed circRNAs. The authors can compare the numbers of exons of conserved circRNAs with those of expressed except conserved circRNAs and all expressed circRNAs.

8. In line 39, the authors cited Guo et al., Cell 2020 to show as examples of functional circular RNAs especially in the immune and nervous systems, but it has nothing to do with circular RNAs. Other correct references should be cited here. Please cite those correct references.

9. In line 41, the authors stated that "Back-splicing occurs co-transcriptionally", but it has been shown that back-splicing might occur both co-transcriptionally and post-transcriptionally (Zhang et al., Cell Rep 2016, PMID: 27068474). Please correct.

10. In line 42, an important reference, Zhang et al., Cell 2014, PMID: 25242744, should be cited here to show "inverted repeat elements that promote complementarity between adjacent introns favouring circRNA formation".

11. In line 44, Quaking was not likely to be suggested to facilitate "these (assumedly inverted repeat elements) RNA-RNA interactions", instead, ADAR (Ivanov et al., Cell Rep 2015, PMID: 25558066; Rybak-Wolf et al., Mol Cell 2015, PMID: 25921068), DHX9 (Aktaş et al., Nature 2017, PMID: 28355180), NF90/110 (Li et al., Mol Cell 2017, PMID: 28625552) were suggested to be involved in inverted repeat element RNA-RNA interactions to regulate circular RNA biogenesis.

12. In line 67, the authors cited Pipes et al., Nucleic Acids Res 2013 to suggest their used datasets in this study. However, lots of samples originally in Pipes et al., Nucleic Acids Res 2013 had only mRNA-seq, without totally RNA-seq, and totally RNA-seq datasets for many those samples were updated in Peng et al., Nucleic Acids Res 2015. In this case, Peng et al., Nucleic Acids Res 2015 should be more appropriate to be cited for clarifying their used datasets.

13. At page 18, authors defined relative TPM values. However, the definitions of circRNAsRead and GeneRead are not clear.

Reviewer #3:

In the manuscript entitled "Evolutionary dynamics of circular RNAs in primates", Gabriela Santos Rodriguez et al., investigate the evolution of circRNAs in primates. This is indeed a very important and timely topic given the doubts about the functionality of circRNAs and the little we know about their evolution. Briefly, the authors compare tissue specific transcriptomes across 70 million years of primate evolution. They found that most circRNAs are not conserved with the exception of a subset of approx. 700 brain specific circRNAs. Interestingly, the authors found that those circRNAs are defined by an extended downstream intron that is lengthening during evolution due to the insertion of transposons. While the findings are interesting and the manuscript timely, it doesn't bring much new information and seems to ignore essential knowledge in the field.

– The main findings of the manuscript have been previously reported and seem to be ignored by the authors, that they didn't cite and/or discuss them. For example, the reports by Rybak et al. (Mol Cell 2015), Veno et al. (Genome Biol. 2015) and You et al. (Nature Neuro 2015, which is not even cited) described that brain circRNAs are conserved as well as several of the features described for them in the manuscript. A lot of the work described there has been described in these and other reports. So the manuscript doesn't bring novelty regarding to the conservation of brain specific circRNAs.

– Moreover, the data analysis seems a little superficial. First, the authors utilized total RNAseq, without any type of validation (e.g. RNAseR). Moreover, the authors don't even mention the fact that many backsplicing junctions are usually artifacts of reverse transcription or alignment. Moreover, the authors don't seem to apply any filter to gene expression of the circRNAs and some of the criteria utilized is not really justified. For example, very abundant circRNAs might have low PSI if the host gene is expressed at high levels.

– The authors ignore literature in the field regarding circRNA biogenesis. This is important as the authors should consider the orientation of the inserted transposons (as showed in Chen LL et al., Cell 2014) when postulating their model. Moreover, extension of downstream introns and inefficient cleavage and polyadenylation are well described as factors modulating exon circularization (see Liang et al. Mol Cell 2017, Ashwall et al., Mol Cell 2014). This is not minor, as suggest the authors don't know (or chose to ignore) major literature in the field that shows that some of the findings are not new/novel.

– There are a lot of logical/conceptual mistakes in the text in which correlations are stated as causal relationships. A few examples of them are listed below:

o In line 101 the authors say "Many orthologous genes consistently express circRNAs even of the precise back-spliced junction is not conserved implicating importance of trans-factors in controlling cirRNA formation". There is no logic in this statement, long introns and random insertion of repetitive elements in inverse orientation could explain this w/o invoking any trans-acting factor.

o The authors claim that "Anaylsis of the exonic structure of conserved circRNAs, showed that conserved circRNAs contain fewer exons, and rarely overlap with other circRNAs (Figure 2G, p = 4:08. 10*64, Fisher exact test; see Methods) displaying back-splicing at unique 5´- and 3´-splice sites. This indicates that these conserved circRNAs possess unique cis- or trans-regulatory features that enable a tight control of the number of exons within a circRNA and the back-spliced junctions used." This is not necessary like that and the 2 things could be concurrent/codependent on a different factor (i.e. intron length).

o After looking for predictive genomic features for circRNA biosynthesis the authors conclude that: "This indicates a core set of 24 cis- and trans-regulatory features drive the conserved formation of circRNAs compared to our background set of introns" This is factually and conceptually wrong, predictive value does not mean causality. So likely most of these factors are co-current. This is still interesting but the attempt of overstating is alarming.

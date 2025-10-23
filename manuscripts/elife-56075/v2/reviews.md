# Peer review - Round 1

Editors:
- Timothy W Nilsen, Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56075.sa1](https://doi.org/10.7554/eLife.56075.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Srsf10 and the minor spliceosome control tissue-specific and dynamic SR protein expression" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor, Timothy Nilsen, and James Manley as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

As you will see, the reviewers were quite positive about the work and reviewer 3 was very enthusiastic. The reviewing editor was also enthusiastic about the manuscript. Nevertheless, the reviewers have raised some concerns regarding the data and its interpretation. Please address these points as thoroughly as possible via revision. It is not necessary to delete the impact of Srsf10 expression on other SR proteins.

Reviewer #2:

This paper describes an unusual regulatory feedback process in the alternative splicing of the Srsf10 gene involving competition between major and minor intron splice sites. Several RNA binding proteins self-regulate their protein levels by inclusion of alternative "poison exons" that include premature stop codons. Srsf10 appears to have a poison exon 3 who's exclusion requires minor spliceosome activity. This part of the paper seems solid. They then show that there is a general correlation of the expression levels of many SR proteins including Srsf10. This has been described before and similar correlations can be seen in ribosomal protein genes indicating that they are under coordinate regulation. The authors then remove the poison exon from the Srsf10 gene and argue that the results support a key role for Srsf10 and, by extension, the minor spliceosome in controlling the mRNA levels of SR genes in general. The key results shown in Figure 4E do not, to me, support this idea. The authors speculate that alterations in mRNA levels are due to NMD. A direct demonstration would be more convincing. With the data they show, I think they should focus on the Srsf10 case alone rather than pushing for a more global mechanism.

Reviewer #3:

In this work, Meinke et al. demonstrate that alternative splicing of Srsf10 is formed via competition between the major and the minor spliceosome using different splice sites. These in turn lead to functional isoforms that skip exon 3 (minor spliceosome) or inclusion of exon 3 (major spliceosome) in a mostly non functional isoform which encodes a PTC and utilizes an alternative 3' end. The authors show that similar to other Sr proteins Srsf10 regulates its own levels via the inclusion of exon 3 and find a short site in that exon that is sufficient to achieve that regulation. They also perform rescue experiments with SRSF10 mouse variants in human HeLa cells, and a titration experiment with the different isoforms detected (Figure 1). KD of Rnpc3 of the minor spliceosome changes the splicing and expression of Srsf10 as expected (Figure 2). Expression of Srsf10 correlates well with expression of Rnpc3 across diverse mouse tissues, and as expected Rnpc3 levels correlate much better with expression of intron containing genes than matched expression levels of genes with only major introns (Figure 3). When removing exon3 control of Srsf10 levels via CRISPR the expression of Srsf10 increase by ~3.5fold but six other SR genes expression levels rises significantly, and these too correlate well with expression of Rnpc3 (Figure 4). The overall regulatory model is summarized in Figure 4—figure supplement 2.

Overall, we really liked this work. The authors should be congratulated for a thorough line of thoughtful experiments in support of their regulatory model as mentioned above. The manuscript is clearly written and we enjoyed reading it. We have few general comments/suggestions that should be addressed/clarified.

1) Are the changes in Rnpc3 observed in tissues in the same range as done in the titration experiments?

2) Expression computation and correlations: It's not clear how these were computed and whether these were done properly. The authors state TPM were derived by Whippet (Figure 3—figure supplement 1) but Whippet is designed only for splicing changes. It's not clear how Whippet would give full transcripts, and more importantly weighted gene level TPM values. Furthermore, TPM is not a proper measure to compare across many different experiments/conditions (it's not as bad as RPKM but still not great). Between sample normalization should be applied as implemented in DESeq and TMM. See for example https://haroldpimentel.wordpress.com/2014/12/08/in-rna-seq-2-2-between-sample-normalization/

3) Figure 4: We understand where these p-values come from, but we are still worried about possible artifacts in the normalization procedures that might affect the results (also see above). Another way to compute a p-value and address the above concern is to compute an empirical p-value compared to sampling a large set of similarly expressed genes and computing the correlation values for them. True, some may be bona fide targets as well, but presumably this population of targets is rather small and the Sr proteins correlations stand out.

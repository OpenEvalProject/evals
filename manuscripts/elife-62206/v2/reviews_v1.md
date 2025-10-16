# Peer review - Round 1

Editors:
- Mone Zaidi, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62206.sa1](https://doi.org/10.7554/eLife.62206.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The study is well done and is likely to significantly impact our understanding gene associations in large GWAS datasets. Review critique was thoughtfully and thoroughly addressed. Notably, statistical correction for multiple testing of GWAS data requires increasingly large sample sizes to establish potential associations. This retrospective study used chromatin accessibility and direct contact with gene promoters as biological constraints. The application of such constraints on otherwise sub-significant GWAS signals was shown to reveal potentially true-positive loci without the requirement to increase sample size.

Decision letter after peer review:

Thank you for submitting your article "Biological constraints on GWAS SNPs at suggestive significance thresholds reveals true BMI loci" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Clifford Rosen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David Meyre (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that substantial revisions are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors sought to determine whether SNP's located in chromatin that physically contacts GWAS hits provide evidence that boost test scores from suggestive to significant. If successful, this approach might obviate the need for larger, more expensive GWAS studies. The strategy is to first identify relevant open chromatin sites, focusing on genes that were suggestive in early studies. Then in parallel ask which suggestive loci in these early studies became significant in later and larger studies. They claim that positive results support the argument that epigenetic evidence would have boosted scores and precluded the need for larger and more expensive studies. The manuscript has potential, but work is needed. Critical evidence is not provided, or provided in a way that makes critical reading a challenge.

Essential revisions:

1) This is not the first study to demonstrate that biological annotations combined to more relax thresholds of statistical associations from GWAS “rescue” true associations in obesity field. As an illustration, Meyre et al., 2009, rescued a modest stage 1 GWAS association signal for extreme obesity in the NPC1 gene using a candidate gene strategy, and the association was replicated in stage 2. The GWAS obesity hit in NPC1 was recently confirmed as a genome-wide significant signal for BMI in a large meta-analysis (Turcot et al., 2018). Wang et al. (Diabetes 2019) demonstrated a strong enrichment in positive associations with BMI for SNPs located in/near syndromic obesity genes. The authors may like to discuss these and other reports in literature.

2) A strengths and limitation section would add a lot in the Discussion.

3) The biological criteria (chromatin accessibility / direct contact with gene promoters) used in this study are very original, but to be more exhaustive additional biological criteria may have been used to select more SNPs (listed in Li and Meyre, Int J Obes 2013 in the “hypothesis-driven GWAS analysis” section). This may be acknowledged as a limitation of the study.

4) Tissues targeted in the study (adipocyte and hypothalamus) are extremely relevant in the context of genetic susceptibility to obesity. However, genetic association studies have also highlighted the important role of other tissues in energy balance (e.g. beta-cells, liver, muscle, stomach… see Locke et al., 2015, and Pigeyre et al., Clin Sci 2016). Having not explored all tissues potentially relevant for obesity may be acknowledged as another limitation of the study.

5) While Speliotes et al., 2010 and Yengo et al., 2018 GWAS for BMI have been performed in populations of European ancestry, the Locke et al., 2015 study included a multi-ethnic population. Did the authors analyze the GWAS summary statistics in the European population in the Locke et al., 2015 study. If yes, they may provide more details on what they did in the Materials and methods section. If no, I think using the multi-ethnic GWAS summary statistics may add some heterogeneity, and I recommend to focus the analysis in the European population in the Locke et al., 2015 study.

6) Organization of data and analysis. Curiously, the epigenetic data, evidence and analysis of the Capture-C and ATAC-seq data is in the Materials and methods rather than the Results. The combination of methods and data are somewhat incomplete perhaps because of their unusual location in the manuscript. These are key to the overall study and should be in the Results section. As I read the manuscript, my curiosity grew about the nature of the evidence for connecting flanking and regulatory SNPs with the previously reported target SNPs – what is the source of the data, what is the nature of the evidence, – only to learn that they are in the Materials and methods, albeit incompletely. What is the evidence for open chromatin at their targets and in the sentinel genes that were suggestive in early GWAS studies?

7) Study design, analysis, and presentation. A flow chart would help readers understand the sequence of tasks and help the authors with the organization of the results.

8) Bottom-line. The key question is what is the benefit of the proposed method? What's missing – a simple statement about how many suggestive loci became significant later, and how many didn't, in the regular course of work, and in parallel how many epigenetic hits at suggestive loci become significant later, and how many didn't? That is, what's the quantitative benefit of the new assay. Remarkably they don't show the numbers for this seemingly simple and central question. Surprisingly, this point is not even in the Abstract; the 4th and 5th sentences, which address the key results, do not make these points clearly.

9) Chromatin evidence. The evidence is based on two cell lines – MSC-derived adipocytes and ESC-derived hypothalamic-like neurons. Both are relevant cell types in vivo. But beyond that functional connection, no other rationale is provided, and no discussion is provided to critically evaluate the reliability of the evidence. Chromatin states are dynamic properties of cells both in vivo and in vitro. Physiological conditions and disease state can impact these profiles. How stable are these profiles in vitro, and how consistent are these features with their in vivo counter-parts? How do these profiles vary among individuals in health or disease? What about single-cell heterogeneity? Presumably, these factors would contribute noise in the assays, creating false positives, false negatives. All of this is fine, in principle; every approach has limitations. But remarkably little consideration to these issues, either in study design or in discussion of the results and analysis. These issues need careful, thorough and critical consideration.

10) The authors should discuss how the model might work. The authors are correctly concerned about linkage disequilibrium, with an emphasis on independent evidence (subsection “Variant-to-gene mapping pipeline”). But no data are formally presented; if these SNPs are independent (no LD), what is the argument that these data can be combined rather than additive? Are positive results for this variant-to-gene mapping simply a reflection of additive effects? Or do they argue that SNP-interaction (epistasis) is involved? The text is unclear about these issues.

11) Approach. These are important questions for any proposed method:

A) The authors use a frequentist approach. Perhaps they justify that approach versus Bayes, which the logic of their approach nicely fits.

B) The authors should be able to give clear basic statistics – number/percentage of hits that validate in general, and then when applying their approach, essentially they need to give the false positive and false negative rates, i.e. how many does their approach put forward that end up being negative, and how many do they miss with their approach (presumably loci with non-epigenetic mechanisms would obviously be missed). Obviously, they need to be clear that a comparable threshold is being applied so that readers can assess the relative performance of the proposed and standard methods. Importantly, are they preserving the type I error rate with their new method, and what is their power? Unfortunately, the Abstract, Results and Discussion are not clear on these points – these are the essence of the paper.

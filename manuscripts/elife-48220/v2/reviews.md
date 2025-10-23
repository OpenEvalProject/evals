# Peer review - Round 1

Editors:
- Antonis Rokas, Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48220.028](https://doi.org/10.7554/eLife.48220.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Reciprocal requirement of Wnt signalling and SKN-1 underlies cryptic intraspecies variation in an ancient embryonic GRN" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Eisen as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This interesting manuscript by Torres-Cleuren et al. examines cryptic genetic variation among C. elegans wild isolates for the requirement of two key genes for gut specification in early embryos in the reference strain, skn-1/Nrf2 and mom-2/Wnt. When either gene is knocked down by RNAi in conditions resulting in 100% lethality, the various C. elegans natural isolates display dramatic variation in the penetrance of endoderm formation. Given possible caveats with RNAi efficency, the authors nicely provide additional support for the observed variation in penetrance in a few isolates by introgression of skn-1 and mom-2 mutations. A GWAS analysis shows association on chr IV for skn-1(RNAi) and no significant association for mom-2(RNAi). The authors go on to build Recombinant Inbred Lines between two lines (N2 and MY16; MY16 displaying a lower penetrance than N2 for both genes) and at least find QTLs on chr IV and II for skn-1(RNAi). A potentially interesting and particularly novel part of the study concerns the correlation between the phenotypes of skn-1(RNAi) versus mom-2(RNAi). The authors do not detect correlation between the two phenotypes in the wild isolates (or a marginally significant positive one) yet find a negative genetic correlation across a large part of the genome when testing windows of 50 SNPs. Given this negative correlation, the authors then present experimental data showing that mutant/RNAi variation at three loci (rict-1, mig-5, plp-1) has reciprocal effects on skn-1 and mom-2 mutant/RNAi effects. The authors suggest the existence of widespread compensatory cryptic genetic variation in the requirements for SKN-1 versus MOM-2. Cryptic genetic variation and compensatory evolution in developmental pathways are important topics in evolutionary developmental biology. The possible negative correlation between the requirement for the two genes is an important result, if confirmed.

All reviewers agreed that there are some major issues with the methods, particularly for the quantitative genetic analyses. The major concern is point 4 (correlation analysis) that conditions the title of the paper and thus requires further analyses.

Essential revisions:

1) Statements on RNAi sensitivity (e.g. third paragraph of subsection “Extensive natural cryptic variation in the requirement for SKN-1 in endoderm specification

within the C. elegans species”: "fully sensitive" to RNAi). Please make clear that sensitivity to RNAi is a quantitative trait. Although the authors place themselves in very strong RNAi conditions that result in 100% lethality (in contrast to a previous study by Paaby et al., 2015 where RNAi was weaker), they cannot conclude that RNAi efficiency is the same in all isolates or RILs. It may be that 0-5% of expression of the target gene causes 100% lethality, but a range of endoderm phenotypes. The introgression results are convincing for the tested isolates; however, it remains possible that some genetic variation for RNAi efficiency is detected. Of course, it would not explain the negative correlation between the two RNAi experiments, which may be worth to point out.

2) Comments on GWAS analyses:

– We suggest that the authors only show the EMMA results. Is there a reason to use a model that does not correct for population structure?

(NB: EMMA performs a GWAS, so do not refer to GWAS and EMMA as two different things.)

– Since the phenotypes are proportions, consider to use an arcsine transformation or best a binomial model on individual observations taking replicates into account. This may particularly help for the skewed mom-2 data.

– Where does the EMMA peak on chromosome IV with skn-1(RNAi) map? Please provide the association results in a supplementary table. Since the skn-1 gene is in this region (as far as can be judged), can you rule out that variation in RNAi efficiency due to skn-1 polymorphism underlies it?

3) Regarding RILs:

– Is there any reason to perform marker regression versus interval mapping? Just go for interval mapping.

– Please comment whether all lines show 100% lethality upon RNAi of each gene.

– Figure 6A: why were so few lines tested for mom-2(RNAi) compared to skn-1(RNAi)?

– Figure 6B: draw thresholds of significance on panel B for each QTL analysis.

– The plots in C-F do not bring much except for the direction of the effect of the peaks in B. Maybe it would be more useful to provide the direction of the QTL effect in panel B either with +/- or by using a negative scale when appropriate. As we interpret it, the QTL for mom-2(RNAi) on chr II (if significant) is transgressive.

4) Correlation

– Figure 7: as noted by the authors, Panel B cannot be interpreted because of linkage disequilibrium. So please remove this panel and correct for LD (for example using Plink to prune SNPs under LD).

–Correlation across the genome: If we understand well, the authors use the full RAD data in Andersen et al., 2012. So a large fraction of the SNPs come from QX1211 and a few other isolates. we suspect that the negative correlation may be driven by a small number of isolates contributing most SNPs. As this is a central result, please test whether it is robust to outliers, and genetic relatedness among lines, for example by bootstrapping on the lines.

The result, if true, implies a strong negative genetic correlation, which could be measured using a multivariate animal model (e.g., see R package sommer for worked examples).

5) rict-1, mig-5, plp-1 loci

The rationale for testing these three loci is unclear – they appear to be cherry-picked to find a different effect on mom-2 vs skn-1 penetrance. Are there instead known loci that would have similar effects on mom-2 vs skn-1 penetrance?

6) Subsection “Phylogenetic and geographical analyses”: examining the correlation between phenotypes and phylogeny using a Mantel test seems less accurate (e.g., https://www.ncbi.nlm.nih.gov/pubmed/20163450) than simply measuring whether the phenotypes have phylogenetic signal (this can be done by estimating Pagel's lamda or Blomberg's K). Please report the phylogenetic signal of the phenotypes and remove the Mantel test.

7) Subsection “Extensive natural cryptic variation in the requirement for SKN-1 in endoderm specification within the C. elegans species” paragraph three: The explanation for the difference in results between study by Paaby et al. and this study appear hand-wavy. The authors should modify or provide further justification of their conclusion.

8) The language / terminology, especially in the Introduction, needs to be more precise. Here are some examples:

Introduction first sentence: change "has been bequeathed to" to "is conserved in"

Introduction fourth sentence: you could delete this sentence as the question posed is rather too broad and will not be answered by a single study focused on a single GRN.

Introduction second paragraph: "in the most ancient creatures" – the animals to which you are referring are extant. Please rephrase.

Introduction paragraph five: "shows striking variation even in relatively most closely related species" – what's "striking" and what's not seems highly subjective so consider to tone down this statement (e.g., "substantial" is a lot more neutral). Also, i would prefer if you said "between species that diverged 20-40 million years ago", which is more precise than the ambiguous "closely related".

Introduction paragraph six: delete "the radiation of" – not necessary.

– replace "profoundly" with a more neutral word (e.g., "highly").

– "exceedingly rapid" – not at all clear why this is so.

– replace "during the radiation of" with "within".

9) Length of Discussion: the discussion was rather long, largely because the authors repeated their key results. Please replace the paragraphs (e.g., subsection “Multigenic variation in the requirement for SKN-1 and MOM-2” restating your key results with single sentence summaries.

10) Content of Discussion: One interesting aspect of this study that was not discussed in detail is the question whether this level of regulatory plasticity is restricted to a few, fast evolving taxa such as C. elegans and Drosophila or whether it is more widespread throughout metazoa. Please brief discuss this aspect of your results. In contrast, the data shown in this study do not provide definitive support for the hourglass hypothesis as the authors have argued for and this type of plasticity might be restricted to a few fast evolving taxa and not a defining characteristic feature of metazoan development. Please de-emphasize or altogether remove discussion of the developmental hourglass model as the data do not directly address it.

11) Figure 9 showing the simplified models should be expanded to include the additional factors rict-1, plp-1 and mig-5 so that it provides a more complete representation of the data.

12) Title: Maybe add "MOM-2"/Wnt since only mom-2 has been tested. The variation in requirement for mom-2 could in principle be due to variation in redundancy with another Wnt ligand. Also, "ancient": what is ancient? the network or only the final TF?

# Peer review - Round 1

Editors:
- Xochitl Morgan, University of Otago New Zealand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37090.035](https://doi.org/10.7554/eLife.37090.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Integrated culturing, modeling and transcriptomics uncovers emergent behavior in a synthetic gut community" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Wendy Garrett as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

D'hoe et al. use batch and continuous culture to model and quantify metabolic cross-feeding by three common human-associated taxa: B. hydrogenotrophica, F. prausnitzii, and R. intestinalis. The authors first characterized the metabolic activity of B. hydrogenotrophica, demonstrating that it was highly versatile and that lactate production varied according to growth substrate. Next, they created replicate sets of mono-, di-, and tricultures, which were used to model community growth according to Monod kinetics. They quantified cross-feeding in mixed communities and showed that complex communities could not be modeled from monocultures, but could be well-modeled with di-culture data. Finally, they use RNA seq data to quantify many additional metabolic changes (e.g. vitamin B12 synthesis) in complex communities. The findings represent a fundamental and rather interesting contribution to microbiome sciences given the detailed study of a synthetic gut community and the ever-expanding clinical interest in such communities. The paper's approach and methodology are generally well-executed and noteworthy.

Essential revisions:

1) Although only one strain of each species was used in the model, throughout the manuscript the discussion suggests this could be extrapolated to all strains of the species (and at one point, even genera ("Blautia consumes formate produced by Roseburia and Faecalibacterium")). This was not tested in these experiments, and so this generalization cannot be concluded. Therefore, several parts of the manuscript require careful re-writing to clarify strain heterogeneity. It would be helpful to put the discussion in terms of the genomes of the strains used, and the degree of openness of the genomes of representatives of the species sequenced to date. Likewise, please update Discussion to indicate whether models are expected to be robust across different strains within a species and what might happen if experiments were repeated with a different set of strains of the same species? Would strains that have been (in contrast to the culture collection isolates in this study) maintained by an individual over long periods of time and many generations of bacterial cells interact with one another differently?

2) The major conclusion of the paper is heavily based on the assumption of the existence of a single model that best fits the data. Please discuss the justification for choice of model. This could be done either by citation of literature and discussion of limits of Monod kinetics and impact of any violated model assumptions on conclusions, or alternatively by quantifying the fit of the model to a set of models using alternate variations of Monod kinetics from the literature (see Krumins and Fennell, 2014).

3) Please discuss how to interpret RMSE values in Table 1 and the basis used to deem a model well- or poorly-fitting? As RMSE is sensitive to outliers, please include an additional metric quantifying goodness of fit (such as R2 (coefficient of determination) or MAE (mean absolute error)) that is less sensitive to outliers.

4) The manuscript shows that F. prausnitzii is growth-limited by a heat-labile cofactor, possibly B12, and in tri-culture, FP's B12biosynthesis genes are downregulated. If time permits, it would improve the impact of the manuscript to show that FP is growth-limited by B12 specifically, such as with a simple batch experiment +/- B12 supplementation through a sterile filter.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Integrated culturing, modeling and transcriptomics uncovers emergent behavior in a synthetic gut community" for further consideration at eLife. Your revised article has been favorably evaluated by Wendy Garrett as the Senior Editor and the Reviewing Editor.

The manuscript has been improved. At this juncture, we have advice and suggestions that we think will improve the readability of your manuscript and clarity of the Abstract and Introduction. Please respond to these remaining issues that need to be addressed before acceptance, as outlined below:

As per eLife editorial guidelines, a study's title and Abstract should clearly indicate the model system being used for a study. Therefore:

1) Please revise your study title to make it more informative. I am including a suggestion but your suggestions are welcome.

Suggestion: Integrated fermentation culturing, modeling and transcriptomics uncovers complex interactions and emergent behavior in a three-species synthetic human gut community.

2) Please update your Abstract to indicate which three strains are included in your model community. Consider also updating Abstract to give a few key examples of the kinds of taxa behavior that are described.

3) Reviewers previously requested that authors shorten the end of Introduction in particular and authors have clearly made an effort to do so, but further reducing length of last three paragraphs by ~25%, particularly by trimming methods further, and re-ordering a little may improve readability of manuscript.

Here's a proposed revision as a suggestion for a possible way to shorten that text:

"In this study, we created a synthetic community composed of three abundant and typical members of the human gut microbiome: Faecalibacteriumprausnitzii A2-165 (Duncan, Hold et al., 2002b), Roseburiaintestinalis L1-82 (Duncan, Hold et al., 2002a) and Blautiahydrogenotrophica S5a33 (Bernalier, Willems et al., 1996). All three strains were isolated from human feces. They have well-characterized metabolism, draft genomes available, and described potential for cross-feeding. Furthermore, they are of particular medical relevance due to the ability of two of three strains (R. intestinalis L1-82 and F. prausnitzii A2-165) to produce butyrate, an beneficial short chain fatty acid that is an important energy source for gut epithelial cells (Geirnaert, Calatayud et al., 2016, Rivière et al., 2016). Butyrate producers are often depleted in dysbiotic gut microbiota relative to healthy controls (Antharam, Li et al., 2013, Rivera-Chávez, Zhang et al., 2016). Thus, high butyrate production will likely be a quality criterion for bacterial cocktails designed for therapeutic purposes.

In R. intestinalis L1-82, fermentation of carbohydrates results in production of butyrate as well as hydrogen gas and carbon dioxide (Duncan et al., 2002a, Falony, Verschaeren et al., 2009c), whereas F. prausnitzii A2-165 produces formate in addition to butyrate and requires acetate for growth (Duncan et al., 2002b, Moens et al., 2016). B. hydrogenotrophica S5a33 is able to grow on carbon dioxide and hydrogen gas, but also on glucose and fructose, in all cases generating acetate (Bernalier et al., 1996). Therefore, as Figure 2 illustrates, our community contains multiple cross-feeding and competitive interactions. For instance, all three strains compete for fructose. B. hydrogenotrophica S5a33 can use the hydrogen gas generated by R. intestinalis L1-82 as well as of the carbon dioxide and formate produced by both R. intestinalis L1-82 and F. prausnitzii A2-165. In turn, B. hydrogenotrophica S5a33 provides acetate that is beneficial to R. intestinalis L1-82 and F. prausnitzii A2-165. This system thus constitutes a rare example of two strain pairs that simultaneously compete and mutually cross-feed.

To reach our objectives, we created a synthetic model community comprised of three common gut commensal bacteria: Faecalibacterumprausnitzii, Blautiahydrogenotrophica, and Roseburiaintestinalis. These strains were grown as mono-, di-, or tricultures in 2-L laboratory fermentors in batch mode. We measured growth kinetic parameters, and quantified the dynamics of each combination. We quantified bacteria (flow cytometry, qPCR, OD600), growth substrates, and the short chain fatty acids and gases produced by fermentation. Finally, we sequenced the total RNA in selected samples. Figure 1 summarizes our approach. To our knowledge, this is the first study that investigates a synthetic gut community with a combination of mono- and co-cultures, mechanistic modeling and gene expression analysis."

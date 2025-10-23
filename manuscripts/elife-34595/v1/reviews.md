# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34595.032](https://doi.org/10.7554/eLife.34595.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Estimating the Protein Burden Limit of Yeast Cells by Measuring Expression Limits of Glycolytic Proteins" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Claus O Wilke (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Moriya et al., attempt to determine the protein expression limits of glycolytic proteins. They measure the growth rate, protein expression and copy number of glycolytic proteins using both high copy and low copy plasmids. They go on to estimate the contributions of various factors that might determine the upper limit of protein expression such as metabolic activity, codon usage, membrane localization and disulfide bond formation. The authors conclude that while metabolic activity has no role in determining the expression limit, disulfide bond formation, membrane localization and sub-optimal codon usage limit the extent of protein expression. The authors assert the ability of their pipeline to differentiate between proteins that can be overexpressed from those that will be harmful upon overexpression.

Essential revisions:

1) One of the main findings of the paper is that protein expression limits are not determined by the metabolic activity. The authors base this primarily on the lack of a difference between expression levels of proteins and their catalytic mutants (proteins with mutations in their catalytic sites). The authors need to verify that metabolism is indeed altered to unequivocally comment on the link between metabolic activity and protein expression levels. Instances that highlight the need to perform metabolic measurements in the manuscript are:

A) The authors measured metabolic activity for only one protein-mutant pair (Pfk2, Figure 4), which did not show any difference in protein expression levels (Figure 3A). The authors need to measure the metabolic levels for pairs of proteins that show a significant difference in their expression levels like Pfk1 or Tdh3 to be able to comment on the link between metabolism and protein levels.

B) In addition, there are several contradictions in the effect of these catalytic mutants on protein expression levels. Figure 3A shows that in two cases the mutant has higher expression (Pfk1 and Tdh3) but in other two cases, the wild-type has higher expression (Fba1, Eno1). How do the authors explain such differences? In addition, Tdh3 mutant has lower expression level compared to wild-type when expressed from a high copy plasmid. How do the authors explain this flip?

C) Discussion, fifth paragraph: The authors claim that one of the reasons why they don't see any association between metabolic activity and expression is that the majority of these enzymes are bidirectional. This is not true for all the enzymes as some glycolytic enzymes are unidirectional. In addition, the authors need to show a control example where unidirectional enzyme has a higher protein expression in order to make any claim between enzymatic directionality and protein expression.

2) The authors show that three mechanisms namely codon optimization, membrane localization and disulfide bond formation, determine the limit of expressions of several proteins. However, the differences observed by the authors are significant but really small. While it is likely that multiple mechanisms would contribute to determining the upper limit of protein expression, the authors need to be cautious about claiming them as the sole factors limiting expression levels (subsection “Mitochondrial localization restricting the expression limit of Adh3” and subsection “Lower expression of nonharmful glycolytic proteins explained by their codon optimality”, first paragraph). In addition, the authors claim that disulfide bonds limit the expression of Eno2 and Pgk1 by triggering aggregation. They show that addition of DTT removes the bond formation in Eno2, and changing cysteine to serine in a third protein (Tpi1) reduces its expression levels. Both these pieces of evidence are incomplete independently. Instead of performing the estimations in two different proteins, the authors need to alter cysteine to serine in Eno2 and Pgk1 and then show that the bands disappear in addition to increase in expression. Alternately, the authors need to show that Tpi1 also forms bonds which disappear upon treatment with DTT. The fact that expression of Tpi1 is independent of DTT contradicts that role of disulfide bonds in limiting expression.

3) Overall the authors play a bit fast and loose with their statistics. First, p values should be accurately reported. Don't write "p<0.05", write "p=0.032". Second, whenever p values are stated it should also be stated what test was used (see e.g. subsection “Mutations in catalytic centers not affecting expression limits of most glycolytic proteins”). Third, correlations should be reported with p values (e.g. subsection “Metabolic perturbations triggered upon overexpression of glycolytic proteins”, last paragraph).

4) While the authors describe an interesting system to estimate the limits of protein expression within a cell, there are several discrepancies between vector copy number and measured expression levels, which raises the concern the results can be reflective of the technical experimental setting instead of true limitations. In addition, the authors use GFP, an exogenous protein with a high expression, as control. Endogenous proteins, preferably unidirectional and bidirectional enzymes, that show high and low expression levels, will make for better controls to the glycolytic enzymes. The following are specific examples of such discrepancies:

A) In Figure 1B and C, why is the maximum growth rate between high and low copy number vector control so different?

B) Subsection “Measurement of expression limits of glycolytic proteins”, second paragraph: The two explanations mentioned by the authors are not mutually exclusive. The authors argue that proteins with low expression and low copy number are harmful for the cell and the ones with low expression and high copy number are repressed due to their high copy number. This is a circular argument and doesn't explain why the copy numbers are high in the first place. Finally, is the Pearson correlation of 0.3 significant? The authors have dismissed it but they need to show that it is statistically not significant.

C) The authors claim that 15 percent of the total cellular protein is the limit for overexpression of protein. However, the authors do not observe any correlation between molecular weight and protein expression levels. How do the authors explain this lack of correlation?

5) The results depend on how exactly one defines "growth defect" and how accurately one measures it. The paper does not discuss this issue. "growth defect" needs to be defined precisely, and the authors also need to argue that they can measure it with sufficient accuracy. One way by which one could get the result that there are no growth defects even at high levels of overexpression is by using a very insensitive assay.

6) A simple summary table presenting the expression limit and proposed mechanism of toxicity (or not) and the evidence for this for all 29 proteins would be very helpful. This could replace some of the information in Table 1 which could be moved to the supplement.

7) In places it is not entirely clear why the authors are only performing mechanistic experiments on a specific subset of the proteins. Again a summary table might help to better communicate what has been tested for which proteins and why.

8) 'Repression' implies an active mechanism to lower protein concentration whereas it is just that these proteins are not using optimised codons that increase translation like the other enzymes. It is better to avoid this word and simply talk about 'lower expression'.

9) The metabolic profiling is rather inconclusive. Is the conclusion simply that changes in the quantified metabolites cannot be causing the growth defect? There also doesn't seem to be much of a connection between the results of the computational simulations and the metabolic profiling, so it's not at all clear how useful the simulations are.

10) There is an obvious other source of potential growth defects that have been discussed widely in the literature but that aren't mentioned at all: Toxic effects due to protein misfolding or misinteractions. For example, Geiler-Samerotte et al. measured the effect of overexpressed, misfolded GFP on yeast growth and found an effect in proportion to the amount of misfolded protein (https://doi.org/10.1073/pnas.1017570108). Also concentration-dependent liquid demixing e.g. Bolognesi et al., 2016. Similar topics have been discussed in the literature for a long time, see e.g. this review: https://www.nature.com/articles/nrg2662. No additional work required, but discussion is needed.

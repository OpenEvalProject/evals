# Peer review - Round 1

Editors:
- Vaughn S Cooper, https://ror.org/01an3r305 University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74062.sa0](https://doi.org/10.7554/eLife.74062.sa0)

This study addresses mechanisms by which bacteria are able to survive and evade killing by antibiotics. Using fluorescent versions of antibiotics it studies whether entry/efflux of the drug itself is a significant contributor to the observed variability of antibiotic activity. This study will be of interest to microbiologists and clinicians for the design of better antibiotic therapies and improves our understanding of the relationships between drug uptake, bacterial growth, and drug efficacy.


---

# Peer review - Round 1

Editors:
- Vaughn S Cooper, https://ror.org/01an3r305 University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74062.sa1](https://doi.org/10.7554/eLife.74062.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review

Thank you for submitting your article ‘Fast bacterial growth reduces antibiotic accumulation and efficacy’ for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions

1) The authors report a predrug growth rate variability of more than an order of magnitude (Figure 5A-C), which also seems to vary drastically between experiments (compare x-axis range in Figure 5A-C with Figure 5E-F). This variation is considerably larger than what has been reported by other groups using very similar methods and conditions (e.g. Figure 2 in https://doi.org/10.1016/j.cub.2010.04.045 shows a spread of only a few percent in division time). This large spread possibly occurs because the cells have not yet reached steady state growth conditions before antibiotic addition. The 2 h growth period in LB before antibiotic addition indeed seems insufficient for reaching a new steady state of exponential growth; at the end of this period, large parts of the population are likely still in lag phase or stressed from loading into the microfluidic device. In any case, the state of the cells at drug addition and its reproducibility is not clear.

2) The authors claim that growth-dependent drug sensitivity for roxithromycin is because of growth-dependent transport rates. This conclusion seems insufficiently supported by data.

– Roxithromycin is the only drug that shows a negative correlation between growth rate and drug increase rate—and it is also the drug with the slowest net drug increase. Indeed, the changes in drug concentration are slow compared to the division time. Therefore, dilution via growth might be sufficient to explain the correlation without the need for any more detailed molecular mechanism. Importantly, does a TolC knockout reduce the growth rate in the presence of roxithromycin? If so, (how) can one distinguish a general growth rate effect from a specific TolC effect?

– If the authors can indeed clearly show that the effect is TolC-specific, it would be interesting to also measure the difference in drug uptake kinetics of an ompC mutant. OmpC can still play a role in drug uptake kinetics, even if its expression does not correlate with growth rate.

3) It is not clear why correlations of tolC and ompC expression with the growth before drug addition are analyzed (Figure 5). Since these proteins can affect drug uptake and efflux, it seems more relevant to directly test their correlation with the parameters quantifying these phenomena. To rule out various well-known non-specific effects of GFP reporters observed at different growth rates (e.g. copy number variation of the reporter gene, dependence of maturation time and other properties of GFP on the cytosolic milieu etc.), it would be important to perform controls using several unrelated promoters to corroborate the relevance of the correlations in Figure 5D-F.

Reviewer #1 (Recommendations for the authors)

There have been several studies that have visualised drug accumulation in bacteria at the single-cell level (Cinquin et al., – PMID26656111; Reuter et al., PMID32761242). However, in this study, the authors have done a more thorough job by looking at different classes of antibiotics, against both gram-negative and gram-positive bacteria. They also directly address the functional consequences of decreased accumulation and show that at least for one of the compounds survival was not linked with slower growth rates.

Overall, the study is well designed and the authors have carried out exhaustive characterisation of the different compounds. However, based on their results, what strongly comes across is that there are no unifying principles. Accumulation properties and correlations are unique to each antibiotic and behaviors cannot be generalised even across antibiotics targeting the same sub-cellular space or target. Therefore, some of the conclusions needs to be toned down accordingly.

Specific comments

– Ln 103-104. Table S1, the effect of the fluorescent tag was not neutral across different compounds, some of them exhibited a fold-shift in MIC of 3-256 fold, which are not-insignificant.

– It is clear that for the results to be comparable across different compounds, the authors used the same concentration of compound (46 ug/ml). However, this dose would represent 46x MIC for compounds such as polymyxin B and 0.23x MIC for roxithromycin. Considering that the different fold MICs have hugely differing impact on growth and cellular processes, this would probably translate to differences in accumulation properties depending upon the fold MIC for that particular compound. In Figure S9B, the authors are probably trying to address this issue by using 192 and 46 ug/ml of roxithromycin, but these would represent 1x and 0.23x MICs. It would be more relevant to use 20-40x MIC concentrations of roxithromycin or if solubility is an issue, to use Polymyxin at 1x and 46x concentrations.

– Ln 173-183. It could be useful to provide MIC values of roxithromycin-NBD and vancomycin-NBD for S. aureus and ciprofloxacin-NBD for P. aeruginosa and B. cenocepacia.

– Ln 213, – Linezolid despite being an intracellular targeting drug, seems to exhibit accumulation kinetics similar to membrane targeting compounds. Maybe the authors can discuss about this in more detail.

– Figure 2. I don’t see the value of this figure. The data shown in panels A and B are quite scattered and the correlations are not so obvious.

– Data in Figure 3C and 5A are plotting correlations of the same two parameters, but the values shown are different.

– Ln 448-451 – The authors generated a tolC reporter strain to address the link between kinetic parameter t0 and tolC expression. However, they do not show this correlation but based on positive correlations between t0 and elongation rate and between GFP and elongation rate, conclude that it is in line with their hypothesis. This is erroneous. This would need comparing of GFP levels with t0 and correlating directly. Similar logic was used for in subsequent paragraphs for panels 5E and 5F.

Reviewer #2 (Recommendations for the authors)

– To check whether the dye has an effect on the drug activity, it would be informative to compare single cell growth variability with labelled and unlabeled compounds.

– Background fluorescence is analyzed in empty channels. Another relevant control to rule out that autofluorescence affects the results is to measure fluorescence in cells that are treated with the non-fluorescent versions of the antibiotics.

– Quite a few claims and implications seem exaggerated

– Line 569: the authors claim to mechanistically understand why some drugs are more effective in biofilms than others. Whilst their Figure 4 is interesting, and seems in line with the cited references, it remains unclear why some drugs show a trend as a function of position whereas others don’t.

– Identifying the target of antibiotics via single cell drug uptake kinetic measurements seems a bit farfetched as an application. First, following the data provided by the authors, one could also classify the drugs using (more high throughput) bulk measurements. Second, the authors should compare their technique in the context of current approaches used to classify drugs to clarify its advantages and disadvantages. Lastly, in line 292 it says that this technique can help ‘phenotyping bacterial populations’. What do the authors mean here? Microfluidic techniques to rapidly phenotype drug sensitivity have already been proposed without using fluorescent antibiotics – it is not clear how much fluorescence would add here.

– Line 491 suggests that reducing heterogeneity is the main goal of any treatment. However, the more established goal is to inhibit the growth of as many cells as possible. This can be achieved by keeping the same heterogeneity but simply reducing the mean.

– In line 515 ‘needs to be’ seems exaggerated; similarly ‘major rethink’ in line 543.

– The term ‘phenotypically engineer’ is used both in the abstract and in line 581. This term is unclear for adding an extra compound.

– Figure 3a shows four exemplary curves out of a large data set. It would help to rigorously analyze the reduction in growth rate after the supposed lag time for the entire dataset.

– Line 587: The ‘biases’ mentioned here need to be explained. As is, this claim is unclear without digging into literature.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled ‘Fast bacterial growth reduces antibiotic accumulation and efficacy’ for further consideration by eLife. Your revised article has been evaluated by Gisela Storz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Specifically, the extent of heterogeneity in elongation rates disagrees significantly from prior work, and the current version still does not address prior concerns from Reviewer 2. The robustness of the findings of this study appear to hinge on these concerns, so despite our enthusiasm for the principle, the distribution of growth rates must be well accounted for.

Reviewer #1 (Recommendations for the authors)

The authors have addressed and made modifications to the revised text and have incorporated these new data in the revised manuscript.

I am satisfied with the current version of the manuscript.

Only one important edit. Figure 4D-F needs to be updated and reflect the new content being described in the text and figure legend. The correct figure was shown in the response to the reviewers letter but the figure in the main file is still the previous version.

Reviewer #2 (Recommendations for the authors)

The manuscript has certainly improved, especially due to the inclusion of new control experiments and some simulations. However, some of my concerns remain.

1. I am not convinced that the intra-experiment heterogeneity in elongation rate is similar to that reported in literature as claimed in the response. For example, the elongation rates shown in Figure 2 in Wang et al., are approximately normally distributed with almost all data falling between 0.03/min and 0.06/min; no elongation rates are anywhere near zero. Similarly, in Baltekin et al., Figure 2F (left panel) virtually all (normalised) growth rates fall between 0.5 and 1.25 with a handful of lower values and no values near zero. In both papers, the numbers of cells analyzed are orders of magnitude larger, making outliers more likely. In the preset work, while fewer cells were analyzed, the elongation rates are spread from 0 to 15 μm/h with many values near zero (Figure 4). Therefore, I cannot follow the authors' reasoning here: the variability in elongation rates they observed is clearly much greater than what has been reported in literature. This is problematic for the reasons described in my first report.

2. The authors argue that dilution via growth is unlikely to play a role because they rarely observed cell division during their experiment. However, the two fundamental timescales here are the doubling time and the drug uptake time. The authors state that the doubling time is 75 min = 4500 seconds, while uptake of roxithromycin takes more than 5000 seconds (Figure 1). Therefore, regardless of whether the experiment was performed long enough to observe cell division, drug uptake is slow compared to dilution via growth of cell volume (which happens continuously irrespective of cell divisions). This effect therefore inevitably contributes to the net drug uptake kinetics. One could try to quantitatively correct for this effect; this would be important to rule out that it largely explains the observed correlation between growth rate and net uptake.

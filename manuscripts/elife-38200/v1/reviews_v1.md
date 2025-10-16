# Peer review - Round 1

Editors:
- Gisela Storz, National Institute of Child Health and Human Development United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38200.028](https://doi.org/10.7554/eLife.38200.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Compensatory evolution drives multidrug-resistant tuberculosis in Central Asia" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gisela Storz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Merker et al. presents a detailed analysis of circulating MDR/pre-XDR/XDR strains in a region of Uzbekistan. By expanding the analyses to a previously reported dataset from Samara (Russia) the authors generalize the conclusions to "central Asia". The authors found high transmission of MDR/XDR strains and that high transmission is linked to compensatory mutations. The authors also show that population sizes of the main clade changed over time in parallel to important changes on TB control policies or political/historical events. One major conclusion is that the newly endorsed WHO regimen for MDR-TB will have very limited impact on the region given that strains circulating there are already resistant to many of the relevant antibiotics.

Overall, the manuscript is very well written and the phylodynamic approach to addressing these pertinent questions is timely in terms of both its methodology and its conclusions. We have the following suggestions to improve the manuscript.

Essential revisions:

1) Bayesian model selection

The use of Path Sampling to correctly identify the model is commendable. However, while the model used was a strict clock with a Bayesian skyline, this model was never tested. Thus, the substitution rate selected for the analyses was also not from the best model; it was part of the relaxed lognormal clock with the Bayesian skyline demographic. This may lead to mutation rate differences as outlined below. Related to this, the ESS for each model comparison is quite low. Generally, BEAST analyses should aim for an ESS > 200. For such an important foundation of the paper, the authors should test the utilised model and ensure there is sufficient sampling for higher ESS values.

It is also not stated if the authors ran the finally selected model (strict + skyline) under the prior for comparison to their posterior runs. This should be undertaken to ensure the model is not driving the output, especially in the face of a moderate time signal.

2) Mutation rate

Stemming from the above point, the estimates of the mutation rate seem odd compared to previous estimates. While the overall dating analysis is robust and root-to-tip distance is significant, it looks rather modest in terms of R2. This value indicates a weak clock-like structure and should be noted in the manuscript (e.g. see Discussion and Figure 1 in Duchêne et al. 2016). This weak signal is rightly expected for MTB though, and consequently a mutation rate with broad HPDs is inferred in the Bayesian analyses. This uncertainty surrounding the mutation rate is unfortunately ignored for subsequent analyses due to the strict clock selection. Authors should comment on how this uncertainty is accounted for and why their rate is so much faster than previous estimates, which tend to be closer to 10-8.

3) Phylogenetics and SNP alignment

The higher mutation rate above may be a result of the way the alignment was input for the phylogenetics. It is unclear if authors used SNP alignments or reconstituted whole genome alignments. If the former, the SNP alignments should be corrected for invariant site counts in their ML tree (e.g. by the Stamatakis ascertainment bias correction method) and in the BEAST analyses (e.g. using the constant sites parameter). If not, the branch lengths will likely be incorrect, potentially leading to incorrect date estimates as outlined by Leaché et al. (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4604835/). This would also lead to much higher mutation rates compared to whole genome estimates. Authors should redo the analyses with these corrections to ensure their time estimates are correct.

In line with this, while unlikely to be significant, the removal of 28 complete genes from the data is a bit odd and may affect the mutation rate. What of non-DR causing mutations in these genes? Certain genes, such as gyrA contain lineage defining SNPs and would skew SNP distances between isolates if removed (affecting transmission clusters as discussed below). Authors should comment on why this approach was chosen.

4) Transmission clusters

The rationale for the transmission success score and transmission index is not clear. With a SNP rate of 0.5/year we would expect that N SNPs would have evolved over N/0.5 years and therefore a 10 SNP threshold indicates a timeline of 20 years. Please clarify the rationale or where necessary adjust the calculations and figures accordingly for transmission. Additionally, in a setting like this where most of the strains are clustered, it would be of benefit to test if the different transmission clusters are monophyletic, so distance and phylogeny converge to the same delineated clusters.

Authors should also outline how a transmission cluster was defined (i.e. how did transmission indices group together to form delineated clusters). This is important as in the subsection “Impact of compensatory variants on transmission networks”, the authors identify an association between CAO + compensatory with higher number of DR mutations. This is not identified in non-CAO strains even with compensatory mechanisms. This may be because the numbers for CAO strains is "inflated" by including strains from the same transmission cluster.

5) Statistics

The use of statistics throughout the manuscript is very appreciated. However, the authors should justify the use of the t-test when it is unlikely that the underlying data is normally distributed. Authors should either test for normality or apply a Mann-Whitney test instead.

Also, while the CAO higher transmission potential and link to higher numbers of resistant mutations/phenotypes is very clear, the way it is calculated may not be correct. Do the authors take into account every strain in the dataset irrespective to whether they belong to the same cluster of transmission? Clustering may inflate the number of strains with resistance and thus the clades with higher transmission will be more likely to have more resistances. It may be better to choose from each transmission cluster one strain representative of each resistant profile and then re-run the analyses with those cluster representatives plus the unique cases.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Compensatory evolution drives multidrug-resistant tuberculosis in Central Asia" for further consideration at eLife. Your revised article has been favorably evaluated by Gisela Storz (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

While the authors response to reviewer point (4) Transmission clusters clarifies the 10-year timeline based on 0.5 SNPs/year this was not incorporated into the manuscript in the same way. It appears that the key assumption is that the study isolates are not the result of direct transmission and the minimum pairwise SNP difference is from a common ancestor of any two isolates. Including this assumption and indicating this distance is from a common ancestor and therefore the calculation is 0.5 SNPs/yr x 2 genomes would make it easier for readers to follow the calculation of the transmission index.

Similarly, the "transmission index" is also a little bit confusing as they do it per strain, not clade, and thus by using pairwise distances this means that the same case can contribute to the transmission index of several strains what seems at least weird. I may have been missing something, also the new sketch is not clear about whether they use the threshold per strain or per cluster although text suggests per strain.

The number and size of CAO clusters is not reported in the manuscript which would be helpful to understand how inflated some statistics may be due to a particular strain. These could be included in the appendix or where key statistics related to CAO strains are reported indicate how much is due to a specific number of clusters. For example, in the subsection “Impact of compensatory variants on transmission networks”, 56% of CAO-isolates had rpoC variants. Is this due to a single large transmission cluster over-representing rpoC mutations? Or a number of different strains?

A citation of Duchêne 2016 to support the proposed moderate temporal signal would be appreciated.

The first sentence of the subsection “MTBC population structure and transmission rates” differentiates between variants and polymorphisms; however, throughout the remainder of the manuscript it appears these terms are sometimes used interchangeably. Please clarify if there is indeed a difference and adjust terminology if necessary for consistency.

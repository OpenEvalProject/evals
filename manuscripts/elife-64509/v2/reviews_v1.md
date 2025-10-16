# Peer review - Round 1

Editors:
- Daniel B Weissman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64509.sa1](https://doi.org/10.7554/eLife.64509.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Coronavirus adaptation to immune responses is a very timely and important topic. This paper demonstrates that some of the seasonal coronavirus strains responsible for common colds have undergone substantial recent adaptation in a protein that is likely targeted by the immune system. However, they have not been adapting as quickly as similar proteins in the influenza virus, and at least one seasonal coronavirus strain has undergone very little adaptation in this protein.

Decision letter after peer review:

Congratulations, we are pleased to inform you that your article, "Evidence for adaptive evolution in the receptor-binding domain of seasonal coronaviruses", has been accepted for publication in eLife.

Please take note of the points below and we hope you will continue to support eLife. The main point that all the reviewers agreed on is that it would be helpful to compare your results to those that would be obtained with a standard dN/dS approach.

Reviewer #1:

The authors use dN/dS-based statistics to show that the S1 domain has been adapting in coronaviruses OC43 and 229E, but not in NL63. For at least OC43 and 229E, this agrees qualitatively with earlier studies. The authors should make a detailed, quantitative comparison with these earlier results.

1) I had a hard time understanding exactly what was going on in the simulations, and whether, e.g., they produced phylogenies that looked like the real ones. But perhaps the simulations should be cut or de-emphasized. From my understanding of the Bhatt et al. papers and the authors' code, their selection-detection method is entirely site-based and doesn't use the tree at all, and so should be insensitive to recombination a priori. If this is correct, the simulations are largely unnecessary (but see the next point).

2) It looks like there is substantial geographic population structure, as well as time-varying geographic biases in sampling. This seems like it could generate false signals of substitutions, where standing spatial variation appears to be temporal variation. Can the authors bound how large this contribution could be? If not, perhaps they could still say that they've found signatures of either global positive selection or local adaptation, both of which are interesting.

3) Why is synonymous divergence also much higher in OC43 S1 than it is in RDRP or S2?

4) As I mention in the general assessment above, the authors should compare their results to previous studies. This includes both overall substitution rates as well as specific sites found to have repeated substitutions. For NL63, how does the null result compare to what's known? I believe Kiyuka et al., 2018, found widespread reinfection by similar NL63 genotypes, which may be relevant.

Reviewer #2:

The paper by Kistler and Bedford explores whether adaptive evolution has led to diversification of coronaviruses responsible for the common cold in the human population. The paper is very well written and presents evidence for adaptive evolution in some strains and lack of evidence in others. I enjoyed reading the paper.

Reviewer #3:

This paper analyzing potential adaptive evolution in seasonal coronaviruses ("common colds") is highly relevant with well-supported conclusions. Its results will be widely applicable to myriad fields, including evolutionary biology, epidemiology and public health, vaccinology, immunology, and virology.

Kistler and Bedford present a timely and highly relevant analysis of adaptive evolution in seasonal "common cold" coronaviruses. Overall, I find the research compelling, well-performed, and mostly well-presented. The research contains sufficient statistical rigor with commendable computational reproducibility to be considered highly reliable. The authors conclude that at least two of the four known common cold coronaviruses have been undergoing adaptive evolution in their human hosts. These results may shed light on the emerging long-term evolutionary dynamics of SARS-CoV-2, the causative agent of COVID-19, as it continues circulating in humans, as well as informing ongoing vaccine design.

Kistler and Bedford present a timely and highly relevant analysis of adaptive evolution in seasonal "common cold" coronaviruses. Overall, I find the research compelling, well-performed, and mostly well-presented (though some organizational changes are needed). As always, the commitment to open code and data from the Bedford lab is admirable and successfully performed/communicated. In my comments below, I offer advice to improve the clarity and presentation of the paper, with a few small requested analyses or need for further explanations.

1) "We have arbitrarily labeled these lineages 'A' and 'B' (Figure 1)." The figure then shows A/B panels for different hCoV strains, which is a little confusing at first until you orient to the figure presentation. I recommend labeling the phylogeny in panel A with "A" and "B" rather than just using colors, and including that lineage information in the legend.

2) The legend for Figure 1 needs units for the clock rate. Presumably this is the codon sub rate per year, which is used elsewhere? Or is this nucleotide? Similarly, units are also needed:…

– Subsection “Rate of Adaptation in RdRp and subdomains of spike”, for the parenthetical "(or 0.45 adaptive substitutions each year)". Are the authors converting to nucleotide?

– Subsection “Phylogenetic Inference”.

3) In general, I find the references to supplementary figures in the text confusing. For example, I first read the phrase "Figure 1 Supplement 1A" to mean both Figure 1 and Supplement 1A. Writing this as, "Figure 1—figure supplement 1A" will make it more clear that Figure 1 of the main text is not being referenced.

4) Results, second paragraph – sentences are not well ordered. Should be in order: 1) Though…, 2) Because…, 3) This….

5) The last two sentences in the second paragraph of the Results seem tacked on and not immediately relevant to recombination. Please move these sentences or include a paragraph break.

6) Related to the previous comment, the Results section as a whole will benefit from improved organization, specifically by creating subsections. I highly recommend adding these to improve readability.

7) Comments for Figure 2:

– Unless it becomes too busy, small indicators (or at least in the legend to avoid figure noise) might be added to emphasize the RBD domain within S1 specifically.

– I recommend changing the color of the asterisks in panel A to match the lineage A (red) color.

8) The authors write, "from that lineage's common ancestor." It would be more precise to say the "from that lineage's most recent common ancestor."

9) Figure 3, specifically in panel A for RdRp, leaves some ambiguous interpretations: Is the line missing for OC43 lineage B because there is no RdRp data after the early 1990s (seems unlikely?), or because there were no adaptive substitutions, in which case the orange lines should remain steady at 0? This aspect of the figure should be clarified or fixed.

There is a similar situation for panel C, HKU1 lineage B, in Figure 2—figure supplement 1. In addition, the "C" for that panel is cut off at the bottom, so this figure needs to be slightly reformatted.

10) In the fifth paragraph of the Results, the authors introduce the H3N2 analysis, but the actual analysis is not really presented or described for another two pages. The H3N2 comparison is definitely not part of Figure 4, which this paragraph is introducing. I think this sentence is likely misplaced? Again, this comment shows that adding subsections to the Results section will be helpful for overall organization.

11) Results, I would like to see more details about what constitutes an “adaptive substitution” in the Bhatt method, which is not as widely used as dN/dS, within the main text itself. A couple additional sentences briefly and "birds eye view" explaining what constitutes adaptive will help orient readers. The easiest way to this – just move "Briefly,…each of these timepoints." to the Results section.

12) Jumping off of the last comment – why wasn't dN/dS done? Given that dN/dS is more commonly applied, I think a comparison of these results to standard dN/dS analysis is merited. In fact, including a dN/dS analysis may bolster the authors' overall conclusions and/or contribute to justifying using the Bhatt method, especially if dN/dS is not sufficient sensitive for this data.

13) In general, the authors should clarify their use of the terms "positive selection" and "adaptive substitutions." The former is traditionally associated with interpreting dN/dS, which isn't calculated in the manuscript, and the latter term is more mechanistically-oriented regarding effects of mutations. Therefore, what is meant by "positive selection" in the simulations, and how does this definition/implementation compare to the authors' measurements of "adaptive substitutions"?

14) Figure 7 and its associated analysis raised some concerns for me. It seems like only simulation 5 replicates were performed for each condition. Is there a reason so few simulations were performed (e.g. too computationally expensive?). Further, mean and CI bars for only 5 replicates in Figure 7 gives the impression that there are more than 5 replicates. A strip plot would be more forthcoming about the analyses conducted here, and some additional explanation about why only 5 replicates were performed per condition would help.

15) Table 1 and its associated analysis:

– CI's or some measure of statistical bounds should be included in Table 1.

– Where is OC43B in the table? Was the analysis not performed on this lineage, and if so why not?

– The authors motivate this analysis by explaining how TMRCA is meaningful for H3N2. Can the authors perform this analysis for H3N2 proteins as well to provide further context for the HCoV values, just as they did for these analyses associated with Figure 5?

16) Results, tenth paragraph. To motivate this analysis, the authors may also wish to cite this paper, co-authored by Trevor, that uses a downsampling strategy from empirical to study 2009 H1N1 dynamics, and shows time dependency in evolutionary metrics. https://bedford.io/papers/meyer-time-dependence/

– In addition, why did the authors use simulated data here? If we have HCoV sequence data since at least the 1990s, it seems possible to have used real data here. Further explanation/justification is therefore needed.

– All that said, looking at the CI's (assuming these are CI's – the legend needs to add this info) in Figure 7—figure supplement 1, the bounds across time points are often overlapping. One might expect that CIs would be wider as sample size decreases, which is not always the case. To my eye, the only panel in this figure that truly shows the authors' conclusion is the "no recombination/high positive selection" panel.

17) Please add a reference in the third paragraph of the Discussion about transmissibility/pathology correlates.

18) Subsection “Phylogenetic Inference”: IG-Tree typo should be IQ-TREE. In addition, The authors may also wish to confirm on their own end which IQ-TREE version was used – a major version 2 was released in 2020 and has a different citation. Either way, please indicate the IQ-TREE version used and make sure the citation is right for whichever was used.

19) Figure 2—figure supplement 1C – please choose different colors. Since some transparency is used for points, it's very hard to distinguish precisely light from dark purple.

20) Grammar and spelling:

– There should be a comma after 229E (as in, "…two species of HCoV, OC43 and 229E, were identified…")

– "Some human respiratory illness…" is a runon sentence. Please add a comma before ",while others,".

– Legend of Figure 1: Please add a comma at "…for each viral gene, and those…"

– Typo, "spikenand" → "spike and"

– Please add a comma before ", while the rate of adaptation…"

– Discussion, third paragraph, again a comma is needed before "while."

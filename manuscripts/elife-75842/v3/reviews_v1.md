# Peer review - Round 1

Editors:
- Daniel J Kliebenstein, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75842.sa0](https://doi.org/10.7554/eLife.75842.sa0)

Using high throughput mutagenesis, this work shows that evolutionary distance between homologous genes is not predictive of how these genes' functions will change in response to similar mutations. This suggests that the starting gene sequence will influence how the synthetic design of new protein functions can occur and also supports a role for conditionality in the natural evolution of protein functions.


---

# Peer review - Round 1

Editors:
- Daniel J Kliebenstein, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75842.sa1](https://doi.org/10.7554/eLife.75842.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Heterogeneity of the GFP fitness landscape and data-driven protein design" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. More clarity in what is and what is not new with more caution on the claims.

2. Support on the choice of a single absolute epistatic threshold for all tests.

3. How much of the total amino acid space was tested for each protein considering the median level of non-synonymous changes?

Reviewer #1 (Recommendations for the authors):

The authors compare different fluorescence proteins for their mutational spectrum to compare the differential sensitivity of the proteins. This shows that the four proteins even though structurally similar have very different mutational spectra both for additive and epistatic interactions.

The main conclusion is interesting but it has a cold absence of discussion about the host organisms and treats the four proteins as almost random samples of this protein space. However, is it possible that the natural differences in the environment of these four species may have shaped these proteins by selection to different temps, temp variability that could be influencing the results such that there is an underlying basis for why these proteins may not behave as expected?

I understand the intent of the graphical representation in Figure 1A and the presentation of sharp vs flat peaks. But is it correct to imply that the valleys in between these peaks have been sampled to ascertain if there are unoccupied peaks? Presently the conceptual representation does give an impression of an absence of any other peaks in this genetic space which I am not sure is supported. This comes from the fact that the space around peak is only sampled using 3-4 amino acid substitutions. Admittedly it is not currently possible to simply test the entire space, I'm simply asking if there is a way to show this unknown possibility within the conceptual figure.

I may have missed this but is there a way to estimate false negative rates on epistasis when comparing the four proteins? The mutational analysis is random so I would presume that there is some imbalance in sampling which could create a false negative issue when comparing between proteins. I'm presuming that this is not enough to change the pattern but would help to clarify.

Are Figure 3a and 3b swapped? In the text, 3a is about neutrality while it seems to be 3b in the figure by the y-axis label.

Reviewer #2 (Recommendations for the authors):

I have summarized some of my concerns below and hope that revising the manuscript improve readability and clarity of the work.

FACS sorting condition – Figure S2 showed their experimental conditions for the gating in FACS. I feel odd that they put horizontal gating when you see the simple tendency in diagonal. It is very common to see such diagonal line as it reflects the noise of expression (or cell size). Then putting a gate in horizontal manner essentially make some bias in sampling. It might be ok, but did the authors ensured their screening/deep mutational scanning strategy by comparing isolated variants (I don't see any figure in this paper)?

The data presentation in Figure 2. Figure 2A and 2C are very misleading as it looks like almost no variant lost fitness up to 2-3 mutations while the distribution of single mutational effects (Figure 2) clearly showed some fraction of mutations killed the protein. I am not sure why the authors decided to generate figures based on the median (figure 2a) or "representative median at least 15 available genotypes (figure 2c)". It is clearly biasing the data presentation toward what the authors want to claim "much difference in mutational robustness". Figure S3-b is far better presentation as it is transparent and actually much more understandable. They should remove Figure 2a and 2c and replaced by Figure S3-b

Related to the above, I do not understand Figure 2d either. Figure S3-b showed the accumulation of 7 mutations looks to me about 50% of variants are dead for amacGFP, while the line in Figure 2d showed more than 90% genotypes are functional. Is that they calculated from single point mutations? I am not sure why this is needed when they have the data. Even if they calculated from single point mutations, about 5% of single point mutations are dead (Table S1), so the accumulation of 7 should read to only about 70% variants are functional (0.957)? Anyway, I believe that FigS3-b showed the all information. Figures 2d seem to be just misleading figures.

I certainly appreciate the efforts that the authors put to measure various biophysical parameters, and tried to correlate them to the mutational robustness. Regardless much effort, they did not see the correlation and they have spent quite substantial arguments for the reasons why they did not see a clear correlation. This certainly reflect the complication of protein folding and measuring the effect of mutations on protein folding. A conventional theory of protein stability and mutational robustness is too simplified and people use this argument tend to ignore the fact that thermostability (of the folded state) does not reflect "folding ability" of each protein in the cell. Moreover, what the authors missed to discuss is that, as far as I understand, GFPs generates the chromophore when they are translated and folded in the cell. So the denatured GFP molecules are different from newly translated polypeptide and the biophysical and biochemical parameters obtained from refolding experiments of GFP may not even reflect the folding process in the cell. Also it is known that refolding of GFP is very slow as they showed in Figure S7 (it takes over hour in the test tube), suggesting refolding (and folding) process of GFPs are highly complicated. Thus it is not surprising at all that the authors did not see any correlation between the thermostability/refolding rate and mutational robustness.

While the authors claimed that it is surprising that the sequence distance does not correlate with the mutational robustness, I don't think it is the case anymore based on what we already know from previous literature. For example, it has been shown that (e.g., Bloom et al., PNAS 2005 PMID 15644440, similar work by Bershtein JMB 2008 PMID 18495157) single point mutation can alter the robustness to mutations of a protein. Moreover, it is general knowledge that most mutations affect protein stability (PMID: 17482644) and the accumulation of multiple mutations would expect to alter the stability (or foldability) of the protein substantially. Thus, It would be much more common to think that four distinct sequences (at least more than 40 mutations separate each other) would exhibit distinct behaviours depending on each sequence's property.

Epistasis calculation – the authors have calculated epistasis and decided '1" is the cutoff for significant and nonsignificant epistasis. What is the bases for the decision? I don't see anything in the main text and may be hidden in the methods. But the justification should be clearly described in the main text based on their experimental noise as it looks to me affecting the results (Figure S5) significantly when they use different cut-offs.

The data presented in Figure 3 is very hard to understand how the authors calculated. As their mutational design is based on error-prone mutations, they do not cover all possible mutations. Also each GFP templates exhibit different WT sequences, there must be only a handful of mutations were commonly observed among the four different experiments. It is not clear how they calculate those numbers in Figure 3, and they should provide much more detailed explanations for this. e.g., How many identical mutations are observed out of X all possible mutations? How they calculate epistasis when the wild type sequence is different? For example, in a 81% diverged pair, only 19% of the positions are calculated? How many mutations actually are observed in both templates? Then 4% out of 19% of the positions exhibit epistasis (figure a – that means only 2 positions showed epistasis)? In any case, more detailed numbers and data processing should be described in the methods as well as in the main text.

While it is interesting that ML can successfully predicted functional variants from a highly fragile GFP (cgreGFP), the authors did not provide much insights into the details. The authors mentioned that the deep mutational scanning data captured negatively epistatic pairs and ML avoided for the prediction. Is that something that the authors can dig and present as data? Currently, it is just a general interpretation and not beyond a hypothesis. In Figure S11, the authors presented epistasis between mutations, and thus they should be able to comment about the designed sequences, e.g., how ML predicted sequences are recapitulated the sequence space around each GFP. All designed sequences just eliminated negative epistatic combinations or even identified any positive epistasis that can compensate each other. Also, it was not clear to me that they only used amino acid mutations that were observed in either phylogeny or their deep mutational scanning dataset (for each GFP)? Or they went to other amino acids that they experimentally did not observe.

Reviewer #3 (Recommendations for the authors):

In Figure 3, the description of panels A and B appears to be swapped with respect to the Y axis labels.

The results shown in Figure S5A are unexpected. Taking amacGFP as an example, the graph shows that genotypes with two large-effect mutations, shown in the bottom left corner of this graph, typically show no epistasis (yellow points). According to equation 1, this indicates that the fluorescence of such genotypes should be equal to the sum of effects of the two mutations, i.e. close to -2.4 (-1.2 + -1.2). However, fluorescence = -2.4 appears to be lower than the dynamic range of fluorescence for amacGFP (see for example Figure 1C, where the fluorescence effect of all genotypes appears to be in the range from 0 to -1.5). Can you clarify this? Perhaps a non-additive model of epistasis was used in this figure?

Figure S9 legend: amacGFP:V14L should be V12L.

Figure S9: why were ddG predictions excluded for proline and glycine mutations?

It would be good to discuss the generality of these results. The fitness landscapes of GFP homologues are bimodal, with mutations tending to have either very little effect, or to cause large reduction of fluorescence. Is that a common property of fitness landscapes, or is it specific to GFP, or to the experimental technique used to measure fitness?

Can the data be used to discriminate between second and higher-order epistasis?

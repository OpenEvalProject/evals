# Author response - Round 1

Authors:
- Shahar Frechter ([ORCID: 0000-0002-0431-5849](https://orcid.org/0000-0002-0431-5849))
- Alexander Shakeel Bates ([ORCID: 0000-0002-1195-0445](https://orcid.org/0000-0002-1195-0445))
- Sina Tootoonian ([ORCID: 0000-0002-3990-8724](https://orcid.org/0000-0002-3990-8724))
- Michael-John Dolan ([ORCID: 0000-0001-9666-3682](https://orcid.org/0000-0001-9666-3682))
- James Manton ([ORCID: 0000-0001-9260-3156](https://orcid.org/0000-0001-9260-3156))
- Arian Rokkum Jamasb ([ORCID: 0000-0002-6727-7579](https://orcid.org/0000-0002-6727-7579))
- Johannes Kohl
- Davi Bock ([ORCID: 0000-0002-8218-7926](https://orcid.org/0000-0002-8218-7926))
- Gregory Jefferis ([ORCID: 0000-0002-0587-9355](https://orcid.org/0000-0002-0587-9355))

## Response text

DOI: [10.7554/eLife.44590.026](https://doi.org/10.7554/eLife.44590.026)

Major Comments:

1) Overall, this is a well written, impressive manuscript. It is obvious that much more analysis could be done in the future, and that this work will open the way for many different studies including behavior and circuit mapping. Together with its sister manuscript (Dolan et al., 2019 eLife), this work builds an extremely powerful, comprehensive, and informative package that should appear ideally back-to-back. In fact, as Aso et al., 2014 a and b, have done for the MB, these two manuscripts will provide a strong push for the LH.

We thank the reviewers for their careful and positive evaluation of this paper.

2) There are concerns regarding figures and figure legends. In the figures, most writing is too small. While we understand that this is difficult to change, we would encourage the authors to think of ways to put additional labeling (for instance of some of the axes) to just indicate what kind of more detailed information is 'hidden' in small print. Similarly, short figure legends can be great, but once again we would have greatly appreciated some more details in the legends, which could even include some of the 'take-home' messages of the particular panel or figure. Given the breadth and length of the manuscript, a reader is otherwise forced to jump back-and-forth between main text, legend, and Materials and methods constantly. And most readers are not ready to spend a lot of time to read a paper. In addition, many of the links provided by the authors did not work, please check this.

We thank the reviewers for their suggestions and hope that our manuscript is now more readable as a result of changes that we have made. These changes include:

We have split our original Figure 3 in two to allow the size of the summary figures to be increased.

We have likewise split our original Figure 8 in order to ensure legibility while adding additional panels to address reviewer point 3.

We have added some additional axis labeling (e.g. Figure 1E to show what kind of information is in the X axis) and figure titles (e.g. Figure 6).

We have added additional explanatory text to figure legends (Figure 4, 5) We have added a missing scale bar to Figure 5.

3) The authors discuss the hypothesis that the mushroom body is for odor identification while the LH is for odor evaluation/classification. This could potentially be very nicely tested with their existing data, by asking: how good is the population of LHN recordings at identifying odors? – i.e., is it worse than PNs? Possible metrics:

a) Figure 7 looks at correlations in odor response profiles between different LHON, LHLN and PN types. Could they reverse this and instead look at correlation in population responses, between different odors? Are population responses more correlated for LHNs than for PNs? (Of course, this would need similar controls as the rest of Figure 7 to ensure that any difference isn't an artifact of the number of cell types recorded).

b) Cluster analysis based on individual trials – how well separated are the clusters corresponding to each individual odor? How many errors are made when identifying which odor is a single trial? (as in Hige et al. Nature 2015 – where MBONs performed worse than KCs) (confounding factor here is that LHN responses are more reliable than PNs – but if LHNs are worse than PNs at clustering, then the confound is in the other direction)

c) ROC/AUC analysis like they do in Figure 8 for odor categories.

We thank the reviewers for this question, which has pushed us to add an interesting additional analysis to the paper. We considered all three of the metrics that they suggested (including carrying out the analysis in ​a​ and corresponding with Glenn Turner to verify the details of the analysis in ​b​). However in the end, we concluded that none of these suggestions were effective ways to address the underlying question, “How good is the LHN vs. PN population at identifying odors?” for our data.

Instead we adopted an approach similar to the one used by Bhandawat et al., 2007. We used a linear classifier (specifically a support vector classifier) to predict odour identity from neuronal population responses. We constructed a virtual population of PNs or LHONs by selecting a single cell for each cell type. We then trained the support vector classifier to predict odor identity and tested its performance using a leave one out cross-validation step. Bootstrapping the selection of different neurons gave an indication of variability in this performance. We also tested the impact of varying the number of cell types on the prediction accuracy. These results are included at the end of Figure 9 (formerly Figure 8) and described in the text (subsection “Encoding of odor categories”, fifth paragraph). Additional methodological details are provided (Materials and methods subsection “Measuring population decoding accuracy”).

The summary of these new results is that LHONs showed a consistent advantage in odour categorisation for cell populations as well as single cells. However for odor identification, LHON populations (but not single LHONs) outperform PNs, which is probably not the reviewer’s prediction. The likely reason for this is again the tuning breadth of LHONs – they respond to more odours (by integrating multiple input channels). Effectively for a given number of cell types an LHN population has more information than a PN population – indeed some of our test odours almost never produced a significant PN response, while still exciting numerous LHNs. All of this forces us to the conclusion that we mention in the text – that a better understanding of this relationship may need to await an improved understanding of the odour channels that LHONs actually integrate. Forthcoming connectomics data means that within the next 1-2 years we should have such data.

Now returning to the initial motivation. As the reviewers noted, we discussed the “hypothesis that the mushroom body is for odor identification while the LH is for odor evaluation/classification”. We do indeed favour a version of this hypothesis, concluding our discussion of this point (emphasis added):

“Nevertheless synthesizing the results in this study with other new work (Dolan et al., 2018a,b; Huoviala et al., 2018; Jeanne et al., 2018) does support the hypothesis that stereotyped integration in the LH could support genetically determined categorical odor representations, while the MB may enable ​identification of specific learned​ odors.”

However we would also note that we do not feel that it makes a strong prediction about the relative performance of PNs vs LHONs in odor identification. It does make a stronger prediction about relative odor identification performance of LHONs vs Kenyon cells, but that is not something that we can test at this point – it would odour response data for a large KC population with our stimulus conditions.

4) Can the authors calculate lifetime and population sparseness for LHLNs, LHONs, and PNs? (as an additional measure beyond just% of odors with significant responses).

We have added lifetime and population sparseness measures to the new Figure 4 (formerly the lower half of Figure 3) and reference these panels in the text (Results subsection “Odor responses of lateral horn neurons”, fourth paragraph). These results follow the anticipated trends i.e. decreasing sparseness for PNs, LHLNs, LHONs.

5) We have concerns about the calculation of LH neuropil volume. They calculate the total neuropil volume of the LH, then multiply by a factor of 2 on the basis that on average, LHNs have the same amount of arbor outside the LH as inside. This is based on light level skeleton data which I'm guessing reveals length but not volume. What if LHNs have thinner axons outside the LH than inside?

This an interesting point. We have recently measured the volume to cable length ratio of axonal and dendritic arbours for a sample of LHONs (using as yet unpublished auto-segmentation data generated by Peter Li and collaborators, available in preprint form at https://doi.org/10.1101/605634); we find that the axonal arbours have ~70% larger volume:length ratio than dendrites on average. Therefore it seems that LHN axons are thicker than their dendrites and we can reassure the reviewers that this concern does not hold.

Also, a distribution concern: What if LHNs with very short axons have a greater proportion of the axon outside the LH, while LHNs with very long axons have a smaller proportion outside the LH? Then on average LHNs would have the same amount of arbor inside as outside the LH, yet the total amount of neuropil outside the LH would be smaller than the total amount inside. Can the authors rule out these possibilities or place some confidence bounds on their estimate?

We summed the total arbour volume outside the LH for one sample flycircuit neuron for each of 167 cell types and compared it with the summed arbour volume inside the LH for the selected neurons. The particular distributional concern mentioned by the reviewers therefore does not apply, since we divided the two summed volumes rather than calculating the mean of 167 cable ratios. Of course we cannot exclude the possibility that neurons with extensive arbours outside the LH may be overrepresented in flycircuit, but we have taken a large sample and we only report our figures one figures to 1 s.f. and make it clear that this is an estimate.

We therefore think that our statement “we estimate that the total volume of LHN arbors is therefore actually 40% greater than the MB” remains a reasonable summary.

6) The authors use the Rand index of ~ 0.6 to say that their manual classification is "well-grounded" – but we don't have any intuition for whether a Rand index of 0.6 is "good". Would they also have said their classification was "well-grounded" if the Rand index was, say, 0.2? (i.e. is this basically an unfalsifiable statement) Can this be benchmarked against some examples where the reader can have some intuitive grasp?

We agree that few readers may have any intuition about what constitutes a “good” value of the adjusted Rand index. The adjusted Rand index does show that the classification accuracy is well above chance (since the adjusted Rand index would be 0 at chance performance); we have pointed this out in the text (subsection “Fine scale anatomical clustering confirms LHN classification”, second paragraph). However we now also report in the text (third paragraph of the aforementioned subsection) the final proportion correctly classified by anatomy and relate this to Figure 7E, which shows excellent agreement between the NBLAST anatomical clustering and functional cell types.

# Peer review - Round 1

Editors:
- Carlos D Brody, https://ror.org/00hx57361 Princeton University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85442.sa0](https://doi.org/10.7554/eLife.85442.sa0)

This valuable modeling study helps to elucidate the conditions under which interactions across brain regions support working memory. Convincing evidence underscores the importance of not merely the strength and density of long-range connections, but also the cell type specificity of such connections, and solid results indicate that the density of inhibitory neurons, together with placement in a cortical hierarchy, plays a role in how strongly or weakly a brain region displays persistent activity. This work will be of interest to modelers studying the neural basis of working memory, as well as to neuroscientists interested in how global brain interactions shape the patterns of brain activity observed during working memory.


---

# Peer review - Round 1

Editors:
- Carlos D Brody, https://ror.org/00hx57361 Princeton University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85442.sa1](https://doi.org/10.7554/eLife.85442.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work..

Decision letter after peer review:

Thank you for submitting your article "Predicting distributed working memory activity in a large-scale mouse brain: the importance of the cell type-specific connectome" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Overall, the reviewers found the manuscript interesting, but its major claim regarding PV density gradient was incompletely supported by the evidence shown, and the novelty of some of the other important findings was questioned. As a result, the manuscript would likely have to be significantly strengthened upon revision in order to be acceptable for publication in eLife (under eLife's old review model, which is how this manuscript was submitted).

1) The manuscript presents at least 3 potential contributing factors to a spatial gradient of persistent activity: hierarchical pattern of connections; PV cell density gradient; counter-stream inhibitory bias (CIB). A principal claim in the manuscript is that the PV cell density gradient is a key factor. But this was not directly demonstrated. The manuscript would be much stronger if the authors directly tested which factor, or which combination of factors, are necessary for a spatial gradient of persistent activity: that is, are hierarchical connections alone, without PV gradient or CIB, sufficient? Are hierarchical connections plus PV gradient, without CIB, sufficient? Are hierarchical connections plus CIB, without PV gradient, sufficient? Etc. It seems the authors could relatively easily test these and directly demonstrate which are the critical ones (including directly testing whether the presence or absence of the PV density gradient is necessary). As pointed out in reviewer 2's Major point 3, how the loop strength results depend on these various factors should also be tested (e.g., are hierarchical organization and CIB sufficient for the results.).

Furthermore, it is essential that the authors look across multiple sensory input modalities before drawing any general conclusions (for example, supplementary data has a version of the task in which sensory inputs are auditory, but then the key analyses upon which the hierarchy claims are based were omitted for this auditory version).

2) A clarification of the graph theoretic measure proposed here should be made. The abstract should make it clear that it simply involves taking into account sign, not only strength, of connections, so readers know what is meant by it, and the word "novel" should be removed – taking into account sign is not a novel concept.

3) The third major point described as a finding in the discussion, that when local recurrent connections are insufficient to support WM, then long-range recurrent interactions between regions are needed, should not be described as a finding of the model, since it seems a logical necessity.

4) Given doubts about several of the critical findings, one aspect that could strengthen the paper enough to be acceptable for eLife (old model) would be a substantial strengthening of the mouse-monkey comparison, which would be of interest to many readers and which this group is uniquely qualified to make. Clarification of what is/is not needed to explain the difference in results across the two species would be useful in trying to compare the two. Can the authors use modeling to demonstrate which specific feature(s) are critical for explaining the differences between the two species? Generally speaking, for the discussion: what do the authors see as the prominent similarities or differences across the two species that would be useful to highlight to the community when comparing studies across them?

5) Please describe and discuss in more detail the areas identified as core areas and those identified as readout areas. i.e. why is gustatory part of the core area for visual WM, and why MOs is not a core area but a readout area? If the task used in the model is a visual delayed response task, the difference in task demands cannot explain the discrepancy between the model results and what is concluded from the ALM literature.

6) How redundancy across regions involved in supporting WM interacts with the definition of core vs readout regions. should be discussed. (See major point 2 from reviewer 1)

Reviewer #1 (Recommendations for the authors):

Reframing the conclusions around hierarchical position (and the excitatory and inhibitory patterns of connectivity related to the hierarchy that are assumed in the model), and clarifying what is conceptually novel about taking into account sign of connections or stating that long-range connections are needed if short-range connections are insufficient would be very helpful.

Reviewer #2 (Recommendations for the authors):

Given that the main results do not seem particularly strong in the current manuscript, it seems like the authors should consider other directions that might be of more interest. For example, I was intrigued by the Discussion about whether ALM is a readout area rather than a core area, and how that might influence the prominent previous work about the role of this area in working memory (although I'm somewhat concerned that, more generally, lesioning one area alone might have minimal effect, and lesioning a different area alone might also have minimal effect, but lesioning both together might lead to a big effect; with respect to the ALM work, it seemed that something like this might be going on with unilateral versus bilateral lesions and I'm not sure if the current model takes that into account). Separately, I'm not sure if there are significant results to put greater emphasis on about multiple areas being involved in working memory, if this differs from what is found in the monkey mesoscale connectome models, or if there are other enough other novel differences between mouse and monkey that could be emphasized.

Clarification points:

1) Fonts on brain areas are tiny/unreadable, as well as on figure insets and axis labels throughout the paper, including the supplemental. The yellow color on the white background is very hard to read.

2) It is confusing to try to distinguish in the text when the PV cell fraction is/is not normalized. This should be clarified throughout the main text and figure captions, as well as justifying when it is appropriate to use the normalized measure.

3) Figure 1 – Supplement 1C. Would be helpful to plot this in the same order as panel B.

Reviewer #3 (Recommendations for the authors):

1. The potential significance of the results is at times hindered by the lack of details/clarity in the methods/results description. For example, important concepts such as cortical hierarchy are only explained in the Method section, but not in the Results section. Other rather complex concepts, such as counterstream inhibitory bias (lines 112-114), can also be more clearly described, even if it has already been covered by previous papers.

2. Figure 5 can be better annotated. For example, it is difficult to confirm (from legend) whether Figure 5B is related to sensory-period inhibition or delay-period inhibition. There should be a more explicit color code for the different categories in Figure 5D, which I only now realise matches the color code in Figure 5A.

3. Some of the results from Figure 5 are very loosely alluded to in the main text (e.g., in lines 250-251, which did not name the readout regions).

4. Although the thalamic-cortical model is quite interesting, it does feel rather separate from the rest of the study. Does this part really belong to this paper? Maybe the authors could link it better with the other main results.

5. In general, the paper could be strengthened with more clear writing and more coherent organization. As an experimentalist, I find it difficult to understand the technical details of this paper. Mejias and Wang, 2022 are a good example of very similar work suitable for a more general audience.

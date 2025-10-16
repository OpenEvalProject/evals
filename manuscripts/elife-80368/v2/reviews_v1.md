# Peer review - Round 1

Editors:
- Muireann Irish, https://ror.org/0384j8v12 University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80368.sa0](https://doi.org/10.7554/eLife.80368.sa0)

This work provides important new insights into how semantic association strength influences the function and relationships across brain regions along a topographical structure of cerebral cortex. A principal gradient with the separation of default mode network from sensory-motor systems represents a hallmark of the retrieval of strong conceptual links. This study will be of interest to cognitive neuroscientists, especially those who are interested in semantic cognition.


---

# Peer review - Round 1

Editors:
- Muireann Irish, https://ror.org/0384j8v12 University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80368.sa1](https://doi.org/10.7554/eLife.80368.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Flexing the principal gradient of the cerebral cortex to suit changing semantic task demands" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Xi-Nian Zuo (Reviewer #1); Wei Wu (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The level of analysis is not explained. For instance, for the cortical gradient analysis: are the gradients computed subject by subject and then averaged? Or is it the parcel-by-parcel matrices that are averaged? Or is it a fixed-effect analysis without considering the participant random factor? There are no error bars in Figure S1, so I assume the PCA is performed on the group average. It should be clearly stated and explained, not only for the gradient analysis but also for the dimensionality analysis and the RSA.

2. The performed statistical tests are not sufficiently explained. For example, what are the confidence intervals of their results? What is Pspin? What statistical test was performed to confirm the mediation analysis (if any)? What are the error bars in Figures 2 and 3?

3. Justification is needed for the selection of the time window for the analyses (TRs 4-6 in the semantic task and 9-10 in the chevron task). The authors indicate that the semantic trials are separated by an easy chevron task for 6 s (Line 619), but in Figure 1A this control task lasts for 4.5 s, which is a bit confusing. Also, the authors suggest 10 chevrons were presented one after another in each trial (Line 621). I wonder if 6 s was long enough for participants to look at so many chevrons and make judgements.

4. I wonder if the authors could provide more explanation about why they chose to exclude abstract nouns and pairs of items drawn from the same taxonomic category (Line 609).

5. How do response times vary according to the strength of association? How are response times taken into account in the analysis? For example, if trials with low association strength are longer, how is it taken into account?

6. How was the sample size (N=36) determined? Please clarify. Please provide statistical power, effect size, confidence interval, and corrections if multiple comparisons done for all the reports of statistics.

7. As a major manipulation in the experiment, it is not very clear how the authors split/define their stimuli into strong and weak semantic association conditions. If I understood correctly, word2vec was used to measure the association strength in each pair of words. Then the authors grouped the top 1/3 association strength trials as a "strong association" condition and the bottom 1/3 as "weak association" (Line 689), and all analyses comparing the effect of "strong vs. weak association" were conducted with data from these two subsets of stimuli. However, in multiple places, the authors indicate the association strength of their stimuli ranges from completely unrelated to weakly related to highly related (Line 612, Line 147, Line 690, and the examples in Figure 1B). This makes me wonder if the trials with bottom 1/3 association strength (i.e., those were used in the current study) are actually "unrelated/no association" trials (more like a baseline condition), instead of "weak association" trials as the authors claimed. These two situations could be different regarding how they engage semantic knowledge and control processing. Besides, I am very interested in what will the authors find if they compare all three conditions (i.e., unrelated vs. weak association vs. strong association).

8. Because the comparison between weak vs. strong association conditions is the key to the current study, I feel it might be better to introduce more about the stimuli in these two conditions. Specifically, the authors only suggested the word pairs fell in these two conditions varied in their association strength, but how about other psycholinguistic properties that could potentially confound their manipulation? For example, words with higher frequency and concreteness may engage more automatic/richer long-term semantic information and words with lower frequency and concreteness need more semantic control. I feel there may be a possibility that the effect of semantic association was partly driven by the differences in these measures in different conditions.

9. Behavior: Correlating the mean response and word2vec distance is not very informative (except for confirming that word2vec distance is meaningful for the mean population). Is this correlation accurate at the group level? i.e., if we compute the correlation coefficient per individual and then test the mean of the coefficient at the group level, is it significant?

10. I wonder if the uniqueness of response (Line 627) could be used to calculate a more straightforward measure of association strength for word pairs than word2vec. That is, for each trial, the more participants link the two words in the same way, the stronger the link is. And the fewer participants link the words in the same way, the weaker and more sparse the association is.

11. Some correlation coefficients are puzzlingly high (e.g., 0.84 in Figure 1C). Please discuss.

12. One strength of the gradient method is its continuous spatial variation in regard to the brain divisions, thus a spatially continuous brain parcellation. Thus, it would be more taking such advantage by using a voxel/vertex analysis than the 400-parcel analysis. What is the tenet for the current work to use the large-parcel gradient analysis? Is this something due to the limitation of the computational resource? If so, please clarify, and if not, please discuss.

13. It seems different cortical surface models are used for rendering the spatial maps (e.g., Figure 2ABC vs Figure 2E vs Figure 3A). Please use an identical surface model for better direct comparisons across different visualizations.

14. It might be good practice to add labels (e.g., t value, r value etc.) next to the colour bars in the activation maps, which could make the figures easier to understand.

15. The dimensionality analysis in the current study is novel and interesting. In this section, the authors linked decreasing dimensionality with more abstract and less variable representations. However, most results here were built based on the comparison between the dimensionality effects for strong and weak association conditions. I wonder if these conclusions can be generalised to results within each condition and across different regions (i.e., regions having lower dimensionality are doing more abstract and cross-modal processing). If so, I am curious why the ATL (a semantic "hub") in Figure 3A has higher dimensionality than the sensory-motor cortices (quite experiences related) and AG (another semantic "hub").

16. A more extensive discussion should be accompanied by the revision to highlight the implications and values of the present work for brain-mind development from a lifespan perspective.

17. Why do the authors use a binary separation of the distance while it is a continuous measure? If this is an actual modulation, the intermediary bin (intermediate values not included in the analyses) should present an intermediary profile.

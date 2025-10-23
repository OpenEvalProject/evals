# Peer review - Round 1

Editors:
- Joseph G Gleeson, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56257.sa0](https://doi.org/10.7554/eLife.56257.sa0)

The authors examine autism subtypes using functional connectivity data derived from magnetic resonance imaging. Autism spectrum disorder is notoriously heterogeneous, so the clustering approach to decompose this heterogeneity is attractive, however, the robustness of this approach and the generalization of groupings is unknown. The authors find that functional connectivity subtypes correspond to clinical autism diagnostic groupings and generalize using independent replication data. Functional connectivity patterns are robust, but the discrete assignment of individuals to a group is moderate and suggests that the findings may reflect compression of the primary gradient of functional brain organization.


---

# Peer review - Round 1

Editors:
- Joseph G Gleeson, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56257.sa1](https://doi.org/10.7554/eLife.56257.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Subtypes of functional connectivity associate robustly with ASD diagnosis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ralph-Axel Müller (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study examines how to subtype individuals with/without an ASD diagnosis using functional connectivity (FC) data. ASD is notoriously heterogenous. As such, a clustering approach to decompose this heterogeneity is attractive but the robustness of this approach and the generalizability of the identified groups is unknown. Urchs et al., find that FC subtypes correspond to ASD diagnosis and generalize using independent replication data. They show that FC patterns are robust, but discrete assignment of individuals to a group are moderate. The study finds that FC patterns for some ROIs are moderately linked with ASD diagnostic status. Particular strengths of the study lie in the great length it goes to achieve replication and reliability (using multiple separate datasets), and to protect from confounds. Reviewers also appreciated the clear conceptual distinction in this study between discrete and continuous heterogeneity within the ASD population, which is often not explicitly addressed in studies testing for "subtypes" or "clusters". Other interesting aspects of the study are the support for 'dense sampling' (i.e., low reliability of datasets with only a single short fMRI scan per participant). Overall, the manuscript presents a relevant and well thought out piece of work. However, as written the analyses are difficult to follow, there was confusion from Reviewers as to the terminology and biological relevance of 'subtypes'. As currently presented, the paper emphasizes evaluation of the reproducibility of the subtypes identified, but the neurobiological validity, clinical utility and potential new leads into functional brain architecture in ASD are unclear. Please see specific comments below.

Essential revisions:

1. It may be possible that the dissimilarity matrices are not optimally modelled in terms of discrete clusters. Testing should be undertaken to determine whether discrete clusters are indeed present in the data, to ensure that the clustering algorithm is not simply forcing clusters onto variation that is truly continuous. Given that the continuous assignment provided better replicability, it is possible that a continuous representation of the subtypes also provides a better characterization.

2. The protective and risk subtypes appear to parse out topographic patterns of global above- and below-average functional connectivity respectively (Figure 3). This would suggest that the subtypes are tapping into a basic FC property, such as the global fMRI signal or whole-brain averaged connectivity. Authors should characterize the topography of the subtypes, to rule out global effects. The major concern in this regard is that the topography of the subtypes are not discussed in any detail, and the abbreviations in Figure 3 are not defined. The methodological approach seems a bit peculiar. FC maps were created for 18 seeds, but justification is not sufficient. Selection of ROIs and how networks likely impact patterns of findings, so the rationale for this choice, as opposed to more common parcellation schemes (e.g., Power, Gordon, Glasser, Schaefer), needs better justification.

3. The "FC subtypes" were determined for each of the 18 seeds separately, resulting in a plethora of "subtypes". The authors later note that the subtypes for some seeds show similarities. Of course, this would be expected because they may actually reflect the same network patterns, being captured via different seeds from the catalogue of 18. Seed selection adds a potentially arbitrary step early in the pipeline that may weaken the study in comparison to data-driven approaches (e.g., ICA).

Generally, the use of the term "subtype" may be misleading, as readers may expect more evidence of ASD "subtypes". The paper has at least one important message about these: They are probably not discrete, but there is continuity between different variants of the disorder, as far as fcMRI patterns go. But the "subtypes" described in the paper are not subtypes of the disorder, and may only be rather indirectly related to them.

4. There is a big methodological step from the detection of 87 "FC subtypes" to the focus on only 11 that show significant association with ASD. Significance thresholds are ultimately arbitrary statistical lines in the sand that may not adequately reflect underlying biology. Readers will want to know more about this vast majority of 76 "subtypes" that are discarded from further analysis. It is extremely likely that these have some informative value for diagnostic classification, even if each of their singular "FC subtypes" does not 'significantly' link up with diagnostic status.

5. Could the no-added effect of symptom severity (on top of diagnosis) be attributable to there being a much greater effect from ASD vs. NTC? What do these results look like if you only include ASD individuals in your analysis? Are 'different' communities identified that do have an association with symptom severity in this approach? Essentially, are your community assignments dominated by ASD vs. control and can you find more subtle ASD symptom relevant communities when you leave out NTC individuals?

6. Authors choose ADOS which is limited to ASD individuals – why not look at SRS which is available from many NTC individuals? Wouldn't this behavior metric be more relevant to the present analysis since this study focused on NTC vs. ASD? It would be interesting to look at association with ADOS repeating the analyses with ASD individuals only, and to look at SRS scores when NTC and ASD individuals are included.

7. When comparing across multiple sessions, are the individuals 'in question' left out of the community group mean? Individuals are identifiable by their connectivity data. Thus, is having an individual's scan included in the community mean biasing the result of that individual being most similar to the 'right' community?

8. It is likely, as authors point out, that more data is driving their results (Figure 1 right). However, more sessions, states sampled, could also be contributing. This can be explicitly tested by holding the total amount of data constant and looking at improvement collapsing across more sessions. The authors are in a good position to comment on this debate using the data they have.

9. The stunning correlation depicted in Figure 2d is misleading. A bimodal distribution of datapoints is enforced as only 11 of 87 FC subtypes in the two tails (significant association with diagnostic status, either ASD or TD) are included. The high Pearson correlation for discovery vs. replication datasets is an artifact of that. Test for all 87 subtypes, or for TD vs. ASD associated subtypes separately, and the correlation will be more realistic. No big deal anyway because authors admit the diagnostic association and its replication are moderate. But authors should remove or edit the corresponding passage in the Discussion (l.292)

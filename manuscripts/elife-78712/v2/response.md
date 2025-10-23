# Author response - Round 1

Authors:
- Raymond Doudlah ([ORCID: 0000-0003-3631-5947](https://orcid.org/0000-0003-3631-5947))
- Ting-Yu Chang ([ORCID: 0000-0003-3964-0905](https://orcid.org/0000-0003-3964-0905))
- Lowell W Thompson
- Byounghoon Kim ([ORCID: 0000-0001-7159-5134](https://orcid.org/0000-0001-7159-5134))
- Adhira Sunkara
- Ari Rosenberg ([ORCID: 0000-0002-8606-2987](https://orcid.org/0000-0002-8606-2987))

## Response text

DOI: [10.7554/eLife.78712.sa2](https://doi.org/10.7554/eLife.78712.sa2)

Essential revisions:

1) R1: The manuscript should provide more information and analysis of behavioral performance in V3A and CIP sessions, to address the possibility that any differences in neuronal results observed between areas can be explained based on the performance of the animals.

This is an excellent point that was not addressed in the first submission. We updated the analysis to test for a difference in performance between the V3A and CIP sessions. The analysis confirmed that there was no significant difference in performance between these sessions (lines: 143-149).

(2) R1: The methods should be expanded to include additional information about the sequence and timing of V3A and CIP experimental sessions. For example, were all CIP sessions conducted first followed by V3A sessions, or were they interleaved?

As suggested, we now report the sequence of the V3A and CIP recording sessions (lines: 898-901). Briefly, we first performed 41 V3A sessions (Monkeys L and F), then all 53 CIP sessions (Monkeys L and F), and then 50 additional V3A sessions (Monkeys L, F, and W).

(3) R1: The overall presentation of the results would be improved by adding information about the animal to animal variability in the results, and clarifying whether examples are shown from different animals (e.g. Figures 1, 2, 3)

We completely agree. For all main analyses, we added statistics for each animal to complement the population results. Where relevant, we now discuss between-animal variability (which was minimal). Analyses that distinguished whether neurons carried choice-related activity were performed at the population-level only because some of the individual sample sizes became rather small (see lines: 399-402). We now indicate from which animal each example neuron came (lines: 192-193).

4) R1: The presentation of results and rationale for pooling data between animals can be improved as described by point #4 from reviewer 1.

We agree that this was not clear in the first submission. To clarify, we ran behavioral analyses as well as comparisons between the behavioral and neuronal responses separately for each animal. The neuronal analyses were run at the population level. As indicated in our response to comment #3, the resubmission includes neuronal analyses for the individual animals as well as pooled across animals.

(5) R1: Regarding the analysis of presaccadic activity in V3A, it would be good to show that the results are robust to the assumptions and parameters of the analysis and justify the use of ANOVA as the statistical test.

We thank the reviewer for bringing up this point. In the first submission, we did not clearly indicate that the onset time was defined as the first time point at which the time courses significantly diverge (ANOVA, p < 0.05) for at least 30 consecutive ms. The 30 ms criterion is widely used when calculating latencies because it makes the estimates more conservative and eliminates false positives. We have clarified this in the Materials and methods section (lines: 937-940 and 994-995).

We further verified the robustness of the results in two ways. First, we recalculated the onset of choice- and saccade-related activity using an ANOVA with more conservative parameters (significance values of 0.01, 0.001, and 0.0001). As expected, the onsets shifted to later times, but always by roughly equal amounts in V3A and CIP. In all cases the cross-area latency difference was within 2 ms of the reported difference, and the conclusions regarding the cross-area differences never changed. Second, we recalculated the onset of choice- and saccade-related activity using a Kruskal-Wallis test (nonparametric). In all cases, the onset times were within 3 ms of the times calculated using an ANOVA, and the conclusions regarding the cross-area differences did not change.

We also used an ANOVA to test if the responses of individual neurons depended on the saccade direction, which allowed for a direct comparison with previous work. Using a Kruskal-Wallis test (nonparametric), the classification (tuned vs. not tuned) was the same for 1053/1129 (93%) of the neurons. Additionally, we note that the saccade direction tuning curves of neurons with significant tuning were well described by von Mises functions (mean r = 0.92 ± 0.47x10-3 SEM), which would not be expected if they were not accurately classified using the ANOVA.

6. R2 questions using the visually guided saccade to dissociate visual and saccade-related responses. The approach should be clarified regarding how "CIP time courses approximately coalesced".

This is an important point which should have been addressed more thoroughly in the first submission. In the resubmission, we discuss that the current study cannot unambiguously distinguish the contributions of visual and presaccadic activity to the observed saccade-related activity (lines: 733-734). To be more agnostic about the possibility of presaccadic activity and to match the terminology used in Chang et al. (2020b), we now use the term “saccade-related activity”. We also added a supplemental figure which shows that the saccade-related activity follows a distinct time course from the visual flash responses measured during receptive field mapping (Figure 8―figure supplement 1). In the Discussion, we additionally highlight that several of the findings suggest that the observed saccade-related activity cannot be attributed to visual responses, and that future experiments will be required to thoroughly dissociate the contributions of visual and presaccadic activity in V3A/CIP (lines: 735-745).

In the Results section (lines: 565-566), we added additional pointers to the Materials and methods section (lines: 1003-1007) where we describe how we calculated the coalescent points for both the V3A and CIP time courses. At the same locations, we reference Chang et al. (2020b) which also used this method.

7. R2: The discrimination index should be described more clearly, including understanding what kind of index values are expected under different conditions.

As suggested, we expanded the description of the discrimination index (DI) to clarify its interpretation and how the mean and variance of the neuronal responses together determine the value (lines: 256-257 and 949-951).

8. R2 suggests clarifying the section entitled, "Hierarchical refinement of 3D pose representation."

We thank the reviewer for this suggestion. We have clarified that the two analyses in this section are complementary to one another in that they provide an assessment of how the overall shape of the orientation tuning curve depends on distance (Tolerance) and how the preferred orientation (independent of tuning bandwidth) depends on distance (lines: 312-334). Together, they provide convergent evidence of a transformation from lower-level visual feature selectivity in V3A to higher-level 3D object representations in CIP.

9. R2 suggests refining and clarifying the analysis of choice-related activity by assessing the amount of behavioral bias in the monkeys' choices.

This is an excellent point that we did not address in the first submission. We now report that each of the monkeys chose all targets in every session and provide summary statistics which show that the choice distributions were very broad. We further report that the session-by-session mean choices of the monkeys and the preferred choice directions of the neurons were not significantly correlated for any monkey, suggesting that their choices were not associated with the neuronal choice preferences (lines: 980-985).

(10) It is suggested by R3 to temper claims that the results are strong evidence for a hierarchical relationship between the two brain areas, and to place more emphasis on the novel results of pre-saccadic activity in V3A.

This is a great point. As suggested, we tempered our interpretation of the differences in saccade-related activity between V3A and CIP as evidence of a hierarchy and focus more on the novel result of saccade-related activity in V3A.

(11) R3 recommends dropping statements regarding the conflict between anatomical and functional data, as it is not judged to be critical for the current study.

We agree that this point is secondary to the goals of the study and removed all such statements.

(12) R3: Clarify whether the difference in timing of the onset of choice activity is significantly different between CIP and V3A.

To statistically compare the V3A and CIP onsets of choice- and saccade-related activity at the population level, it was necessary to perform permutation tests based on bootstrapped values. These individual statistics were not significant, but the latency differences were highly consistent across all domains, supporting the proposed hierarchy. We now highlight in the Discussion that V3A activity preceded CIP activity by a similar amount in every domain: visual onset (6 ms; lines: 710-712), choice-related activity onset (11 ms; lines: 793-794), saccade-related activity onset aligned to the saccade initiation (6 ms; lines: 717-719), and inflection point in the time course of the saccade-related activity aligned to the target onset (7 ms; lines: 737-739). Notably, these analyses were performed using different neuronal subpopulations and experimental trials, providing convergent evidence of a V3A to CIP hierarchy.

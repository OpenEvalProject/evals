# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70450.sa0](https://doi.org/10.7554/eLife.70450.sa0)

This manuscript aims to address an important issue in the study of concussion: both the brain damage caused by concussion, as well as the behavioral symptoms that result vary widely across individuals. The study uses novel and interesting methods to relate multi-variate diffusion MRI data with multi-variate symptom-related data. The methods of analysis are sophisticated and well-executed and the results are quite interesting. The methods developed here could have a broad impact in their application to the many other neurological diseases that have heterogeneous outcomes.


---

# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70450.sa1](https://doi.org/10.7554/eLife.70450.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Multi-tract multi-symptom relationships in pediatric concussion" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Drs. Shackman (Reviewing Editor) and Büchel (Senior Editor). The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

While the Reviewers highlighted several strengths of the manuscript, they also raised some potentially important concerns about the manuscript in its present form.

Essential revisions:

1. The need to quantitatively investigate heterogeneity

– One weakness of the study stems from a possible, and understandable confusion between heterogeneity and complexity. The study successfully targets the potential complexity of links between observed symptoms and underlying neurobiological mechanisms. Authors use a method that can identify multi-tract multi-symptom relationships, elaborating the inter-relatedness of different brain network features as well as the network of symptoms. Nevertheless, there is no analysis in the manuscript that explicitly studies heterogeneity, such as analyses on inter-subject variability (possibly comparing this to the variability within a healthy sample) or the grouping of subjects and variability of symptom/track profiles assigned to the groups. The manuscript would benefit greatly from such analyses.

– The only analysis that is related to the heterogeneity is Figure 2, which is a qualitative analysis. The black dots did not constitute a clear cluster and extended over a large portion of the scatter plot(s). I would appreciate a more quantitative analysis.

Better integration of goals and methods in the Results

Before reading the methods, I had a hard time understanding the results

– If authors want to keep the same structure, they should include short explanations within the results, describing briefly "what and how is done" in each section. For example, the section "Combined measures of white matter tract microstructure" starts with "The PCA yielded two biologically-interpretable components…", and it is not clear what features PCA was applied to and why. Similarly, it is not clear what PLSc stands for, or how and why it was used

– Comparisons between univariate and multivariate approaches should be explained better in the results. I had to read it twice and then go to the Methods section to understand what was done there. The explanation in the Methods section is much better and cleaner than what is given in the Results section.

2. The need to address potentially spurious connections

– There are concerns that some of the connections represented in the 76x76 connectivity matrix used here are spurious connections due to limitations of tractography that cannot be resolved with current methods, especially as the streamlines derived in tractography come close to cortex. These limitations can affect results even when using the state of the art tractography algorithm that was used here, (as demonstrated in Girard et al., 2020, Neuroimage, 221: 117201).

– The computational tractography arsenal includes several additional ways that could have been used to somewhat mitigate these concerns, including post-processing of the streamlines (e.g., with SIFT or LiFE), using surface-enhanced tractography methods (these may have been used here, but not mentioned) to increase the quality of tractography, and/or focusing on well-defined anatomical structures in the core of the white matter that can be well-detected using bundle recognition algorithms, and where tractography uncertainty due to the indeterminacy of the signal is of less concern. These issues seem particularly important given the substantial difference in the results between the 95% threshold and 100% threshold requirement for inclusion of an edge in the analysis

– Regarding my comments about tractography methods, I think that improvements to the tractography methods would improve the confidence in the results that are presented here. At the very least, one way to deal with these concerns is to discuss them, and to acknowledge that the estimation procedures used here produce not "tracts" but rather the edges of a connectivity graph, and that these may or may not represent anatomical units.

3. Concerns with the analytic approach and stability across feature selection

– Data were collected at multiple sites, and site differences should be considered. Authors say the scanner variable was regressed out from the connectivity data, which is fine, but it would be nice to see the site differences and the effect of regressing it out in a more systematic way.

– With the bootstrap analysis, how is it guaranteed that you get the same pairs each time? Please clarify.

– I wonder whether the procedure used to assess the statistical significance of the multi-tract multi-symptom pairs (lines 463-467) doesn't unfairly favor the ones in the unshuffled data. Shouldn't this procedure also include the preliminary feature selection step (lines 427-430) also in the shuffled data? It seems like it should, because some of the correlation in the PLSc is due to these univariate correlations, which could arise by chance in high-dimensional data.

– Uni vs multivariate 1 of 2. Is it any surprising or even interesting that the correlations between multi-tract and multi-symptom features were higher than all univariate correlations? With PLSc, latent modes are constructed (i.e., coefficients of tracts and symptoms are determined) to maximize the correlations. Thus, it is an expected outcome that those correlations would be higher than univariate correlations. Unless I am missing something, which is possible, I don't think this fact can be reported as a finding. Authors need to clarify this point, or revise the way in which these analyses and results are framed and interpreted.

– Uni vs multivariate 2 of 2. I also have a few questions regarding comparisons of univariate and mulivariate correlations: Line 122 – 124 makes a statement comparing these values, but doesn't provide quantitative information. Also, I might be misunderstanding, but don't the highest PLSc values have to be at least as high as the highest bi-variate correlation by construction? Are the differences between these values higher than would be expected by chance? In Figure 3, the two univariate brain graphs (red and blue) look very similar to each other. Are they as similar as they seem there? Are the multi-tracts implicated by PLSc1 also similar to the multi-tracts implicated in PLSc2?

– Why 200 features? Would the results change substantially if you use 100? Is there some way to select a reasonably small number of features empirically (e.g., based on a scree plot?).

4. Concerns with the approach to psychopathology

– One reviewer noted that: It is not the best practice to combine all possible psychiatric conditions within a single group and call it "adverse psychiatric outcome". This adversely affects the interpretability of findings. Knowing that one of the multi-tract features correlates with the adverse psychiatric outcome is not much informative and clinically valuable. Authors need to devise a more appropriate approach. At minimum, they need to provide a compelling motivation for the current approach.

– While the other reviewer noted that: Some comments regarding the participants that were classified as having psychopathology (marked in black in the scatter plots in Figure 2). It is not clear why these participants were selected based on the CBCL scores, which are indirect measures of psychopathology, rather than the more direct KSADS psychopathology scores? If there are 55% with psychopathological KSADS score, that should provide more than 28 participants marked here. I am also not sure that I agree with the statement that the 28 individuals highlighted in black would be grouped together in clinical studies, given their psychopathology probably varies widely. It is not clear to me whether the paragraph on lines 125 – 131 claims that these participants are different from the other participants in terms of their multi-tract/multi-symptom scores or are not different from the other participants. It seems to me that they might be different based on the first multi-tract/multi-symptom scores (which are both slightly higher in this group), but there might also not be enough subjects to demonstrate this difference statistically. I think that this would also be consistent with the subsequently-described overlap between this score and the univariate scores (lines 132-141).

5. Concerns with claims of replication

– The presentation of the results doesn't make it clear whether the structure that was identified in the discovery dataset does in fact replicate in the replication set. Similarly, it hard to judge what to make of the differences in the results of the logistic regression between the samples. If I understand correctly, the logistic regression in the discovery sample indicates as predictive of psychopathology features that are different than the feature that was indicated in the discovery set. But this might lead us to wonder: How should we interpret this? For example, if I had a measurement from a new child that has had a concussion, which of the two models would I use to predict whether they might develop a psychopathology? The one derived in the discovery set or the one remaining feature that was indicated in the discovery set? Authors need to clearly explain the logic and evidence that supports their claim.

– Regarding my comments about the comparison to the replication set, I think that a few direct comparisons might help. For example, how much of the covariance in the discovery set is explained by the same multi-tract/multi-symptom pair that explained more than 40% of the covariance in the microstructural complexity PLSc in the discovery set? Or, possibly even more rigorous: if you ran a PLSc on the discovery set how similar would the feature sets be? I realize that this might not be possible, given the smaller sample size and the choice of 200 features in the feature-selection phase.

6. The need for a more sober and precise Discussion

– Authors say in the discussion that "these results recapitulated well-known findings from the concussion literature and revealed new insights…". Yet it is not clear what those well-known findings are and what new insights were revealed

– Overall, the narrative in the Results section would benefit from a better organization

– Authors should consider reporting more quantitative results, including tables to summarize findings, and precise comparisons of their results with published work.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Multi-tract multi-symptom relationships in pediatric concussion" for further consideration by eLife. Your revised article has been evaluated by Drs. Shackman (Reviewing Editor) and Büchel (Senior Editor), in close consultation with the 2 expert Reviewers.

Both Reviewers expressed some enthusiasm for the revision, noting that

"I think the authors did a great job of reorganizing the manuscript and addressing almost all issues raised by reviewers," and

"The authors have made substantial changes to the manuscript in their revision and extensive additional analysis has been added in response to the comments made on the previous version. I believe that many of these changes help improve the article, and could provide some more clarity about the robustness of the method proposed and its application. In particular, new analyses that describe the robustness of the approach, and new comparisons with the replication sample could help establish confidence in the conclusions."

Nevertheless, there was consensus that additional major revisions are required, as detailed below

Abstract

– In the abstract, results are limited to findings in ADHD and the replication set, but both are rather secondary/supporting results. There is virtually nothing about the main findings. How do certain combinations of symptoms relate to certain combinations of tracts? I would give specific results in the abstract with the highest importance, possibly mentioning specific symptom-tract couples, rather than sharing very generic comments, such as "These clinically-informative, cross demographic multi-tract multi-symptom relationships recapitulated well-known findings…" Such text is more suitable for the Conclusions.

– The current Conclusions in the abstract is again extremely generic and does not fit well the findings. The manuscript does not include much on "stratification strategies" or "predictive biomarkers". It would be better to discuss how specific findings of the current study would fuel future studies.

Abstract/Introduction/Results/Discussion

– Overall, the main goal (not methodological but rather scientific) of the study should be clearer, both in the abstract and other sections (especially, Results). It should be clear for the reader what they learn new about concussion/TBI and how those findings can be used in practice (e.g., in research, in clinics, …).

– The new focus on ADHD is reasonable, but I would have liked to see more treatment in the manuscript of the relationship between ADHD and concussion and what we learn from the current analysis (if at all) about this relationship. As it is right now, the choice to analyze ADHD is not strongly motivated by the Introduction, and the interpretation of the results does not clearly help us understand what we learned here, beyond the fact that manifestations of concussion in participants with ADHD are heterogeneous.

Results/Discussion

– The text in the introduction (page 3, lines 87-96), nicely summarizes the main contribution: "… display a common symptom but will have overall different symptom profiles and different white matter damage profiles… a variety of white matter structure alterations ("multi-tract") may be related to a variety of symptoms ("multi-symptoms") in different ways." This is very clear and interesting. What is missing is that results do not demonstrate this interesting phenomenon clearly. There is one example in Discussions (page 21, lines 600-6004), but it is limited to ADHD symptoms. It would be great if more results/discussions were included about specific symptoms and how they are associated with specific tracts. If possible, talk more about symptom-tract pairs; specifically showing how same/similar symptoms might be related to different tracts. Or how different combinations of symptoms are linked to different tract combinations. This is the most important part of the manuscript, and the results should reflect this fact.

– The inclusion of new control analysis that uses COMMIT to identify spurious connections is great. I think that the added text on lines 666 – 690 raise important caveats and future directions, which will give the readers not as familiar with the details of dMRI research important context to understand the work. On the other hand, it is very hard to judge the similarity between the results in Appendix 1 Figure 4 and Appendix 1 Figure 14. In particular, there seem to be no black stars in Figure 14 (despite the caption mentioning them). Does this mean that no MCF symptom features are significant in this analysis when COMMIT is used? That would be a real problem for the robustness of this approach to issues related to tractography that are mentioned in this part of the discussion.

– Figure 3 (and the comparison between univariate and multivariate measures) is still hard to understand.

A) The authors stated in the response to the reviews that "Figure 3 has been modified, illustrating now two univariate brain graphs (contrasting PC1 and PC2 scores as a function of ADHD diagnosis), and three multivariate brain graphs (PLSc1 – pair 1, PLSc2 – pair 3, and PLSc1 – pair 7)." I see the latter, but not the former. Figure 3 also has two correlation coefficients inset in each plot, (e.g., "r=0.38" and "r=0.26" in the right-hand side of the first row). What do these coefficients refer to?

B) Relatedly, the methods say (starting on line 279) that "Using threshold of p<0.05, we computed univariate comparisons of connectivity (PC scores) between individuals with and those without a diagnosis of ADHD thus identifying putative "ADHD-related" univariate connectivity features." This sounds reasonable, but I don't see the conclusion from this analysis in the Results section. Is there a univariate difference between the PC scores of individuals diagnosed with ADHD and those that were not? Was this comparison conducted only within the group that had a psychopathological KSADS scores? In other words, on line 273 in the phrase "We divided the sample", does the word "sample" here refer only to (how many?) participants who had any psychopathology? Is only their data presented in Figure 3? Or is that all 214 of the discovery set participants?

C) Furthermore, I am still struggling to understand whether I should interpret Figure 3 as indicating a difference between the subjects marked in black (now subjects diagnosed with ADHD) and the other subjects in the multivariate analysis. As far as I can tell, these individuals (black dots in the scatter plots) are not different in any discernible way from the other participants in these plots (colored dots) -- certainly not in pair 3 (the middle line), where the black dots and colored dots seem completely intermingled. Is there some way to evaluate the difference between the groups across all of the multi-symptom/multi-tract features?

D) In the same section, what is the statistical test that supports the statement "Further, we computed correlations between the expression of these multivariate features and clinical subgroup membership, and found weak, albeit significant correlations"? It would be good to apply such a statistical test to all of the multi-tract multi-symptom features, and report the results of this test as part of this section, just as it would be good to report the results of a direct test of the "univariate" PCA differences. I believe that this would provide a stronger assessment of multivariate vs. univariate approaches.

– This might just be a wording issue, but I don't understand the following statement (L413- 416): "Despite forming a clinical subgroup based on a gold-standard measure of psychiatric pathology, these individuals were differentiable by their expression of multi-tract and multi-symptom features". Maybe the problem is the word "differentiable"? If this is really what you meant, may I suggest something a bit more direct, such as "…, these individuals were heterogeneous in their expression of multi-tract and multi-symptom features"?

– The analysis on the replication set is much improved in the revision, but questions still remain here as well. First, are 12% and 33% of the covariance that were explained in the replication set, using MCF1 in both PLSc analysis more than would be expected by chance? I think that this could be established through a permutation test in the replication set or some other statistical test. Another question that arises from the comparison is that it looks as though the first set of symptom weights obtained in the PLSc for microstructural complexity in the replication set (Y_1 in Appendix 1, Figure 11) is completely inverted relative to the set of weights in this PLSc conducted on the discovery set. Is this anti-correlation somehow trivial? Or is it significant (either statistically or conceptually)? What do we learn from the fact that the features selected in the discovery and replication sets are quite different? Does performing the COMMIT analysis in both the discovery and replication set improve the situation? Surely the feature selection step is affected by the 35% of connections that COMMIT finds to be spurious in the discovery set? Why not remove them with COMMIT and proceed from there? I realize that you can't try all the different permutations of analysis pipelines, but using COMMIT seems like a principled way to improve the robustness specifically of this part of the pipeline. I also think that the probe for correlation between expression of the multi-symptom multi-tract features and dataset is clever, but some of the explanations that now appear in the response to the reviews (and particularly about this point) should probably appear in the Discussion section, to help readers understand what the point of this analysis is. In general, I wonder whether, now that lines 618 – 626 have been removed, the authors could discuss the implications of the analysis of the replication set in the Discussion. I think that having a replication set analysis is a real strength of the paper.

Discussion

– While it is discussed in Discussions how a multivariate approach better captured ADHD-related symptoms than a univariate approach, this is not clear in Results. When I first read it in the discussions, I was surprised but then remembered the parts in the results (scattered all around) that supported this claim. I would make this comparison clearer under the "Results / Multivariate vs Univariate Approaches" section.

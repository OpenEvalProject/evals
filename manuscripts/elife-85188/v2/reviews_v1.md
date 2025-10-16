# Peer review - Round 1

Editors:
- Camilla L Nord, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85188.sa0](https://doi.org/10.7554/eLife.85188.sa0)

This important work extensively quantifies changes in cortical hierarchical organization induced by different types of social cognitive training. The evidence supporting this is compelling: the authors employ rigorous and complementary multi-modal neuroimaging assessments in a very large sample, measuring longitudinal changes in functional and structural metrics of cortical hierarchical organization. This work has broad applicability to basic neuroscience, illuminating the link between anatomical and functional hierarchies in the brain and social skills, and is also of interest to clinical psychology audiences due to its relevance to interventions such as mindfulness-based therapies.


---

# Peer review - Round 1

Editors:
- Camilla L Nord, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85188.sa1](https://doi.org/10.7554/eLife.85188.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Changing the social brain: plasticity along macro-scale axes of functional connectivity following social mental training" for consideration by eLife. Your article has been reviewed by 3 expert peer reviewers, and the evaluation has been overseen by Drs. Shackman (Reviewing Editor) and Makin (Senior Editor).

I am sorry to say that---after consultation with the reviewers---we have collectively decided that this work will not be considered further for publication by eLife. In brief, while there was a lot to like about your study (as we highlight in the public summary below), upon consultation the reviewers agreed that the conceptual and practical significance of the work is incremental.

Reviewer #1:

Valk et al. report a thorough, causal assessment of the brain systems involved in human social behavior. Behavioral and neuroscience research has shown that social cognition is supported by multiple distinct socio-affective, socio-cognitive, and attentional components. Prior human neuroimaging studies have demonstrated that these components are associated with activity in distributed cortical systems, including portions of the default mode, ventral attention, and multiple demand networks. The present work uses behavioral training over 9 months to causally test the relationship between component processes and large-scale cortical systems involved in social cognition. The authors find that socio-cognitive training increased functional integration of default and multiple demand regions whereas attention-mindfulness resulted in functional segregation. They further adopt a machine learning framework to show that changes in functional organization modestly predict changes in behavioral performance during training. These data provide one of the most thorough evaluations of brain systems involved in social cognition to date.

Although the main conclusions of the paper are generally supported by the data, aspects of the analysis and reporting weaken the manuscript:

– A related paper from this group (Valk, S. L., et al. 2017. Science Advances) reported changes in structural plasticity (cortical thickness) following behavioral training in the same cohort. It appears that several areas in the temporal lobe show both structural changes and functional network reorganization following training. It is not clear how the functional changes identified in the present report relate to the previously identified structural alterations.

– Many of the results appear to focus on the statistical significance of simple effects for the individual training modules (e.g., reporting t-statistics and associated p-values for changes in the eccentricity of brain region/networks following a single module). If the reported results do reflect contrasts between training modules (as much is stated in the methods), it is not clear to what extent the modules (and the active control) differ from one another because descriptive statistics and effect sizes are not reported. This does not appear to be a critical issue for some of the main results (where the same networks/regions have opposite effects), but it makes it difficult to evaluate the strength of the findings as a whole.

– Although potentially quite interesting, it is not clear that the connectivity-based prediction of behavioral changes is very robust. Effect sizes are small to medium, the methods used for these analyses are prone to data leakage (and steps to protect against these problems are not described), effect size estimates are based on cross-validation alone (as opposed to out-of-sample tests), and there are many experimenter degrees of freedom.

Additional specific recommendations:

– In addition to reporting t-statistics and p values, report descriptive statistics (mean, standard deviation, and confidence intervals) for key comparisons.

– Assess (or control for) the effect of cortical thickness on functional network reorganization. Based on the authors' past work, it appears that they expect these measures to be related, but they are not evaluated or even discussed in the present paper.

– Improve the description of the machine learning approach. Was dimension reduction performed? Based on the main text it appears PCA may have been performed, but this is not discussed in the methods. If so, how was the number of components selected? Was this done on each cross-validation fold? In the absence of these details, the reader is left to assume that the reported effects could be the result of overfitting.

– Because that cross-validation can lead to overly optimistic performance estimates, it would be helpful to perform permutation-based inference against "chance" levels of performance. Multi-level block permutation is recommended given the hierarchical nature of this dataset (see Winkler, A. M., Webster, M. A., Vidaurre, D., Nichols, T. E., & Smith, S. M. (2015). Multi-level block permutation. Neuroimage, 123, 253-268.)

– The word 'module' is used to describe the different behavioral training regimens that participants completed. As the authors are likely aware, this word is also commonly used to describe network structure. This makes phrases such as "module-specific behavioral change" and "behavioral changes across modules" difficult to parse. The authors may want to consider revising their use of the term module.

Reviewer #2:

The study has several strengths:

– Capitalizes on an extensive training program (across 9 months) in a sample of participants that has good size.

– Leverages several advanced analysis methods to characterize how large-scale organization of functional connectivity is altered by training.

– Results show that changes are observed along major axes of functional connectivity organization. Notably, these changes were correlated with behavioral changes, although the associations were rather modest in size.

The study also has several weaknesses that undermine significance:

– The paper has a large number of analyses and results. However, it not entirely clear how the study advances knowledge except in a general fashion that "functional connectivity" changes.

– The central goal of the study is unclear. If the objective was to, as stated in some places, determine changes in integration/segregation of networks, the approach seems too indirect. A direct approach would evaluate these properties with graph theory. The authors do provide some results in that direction, but it is not clear why the results are secondary and mainly used to lend support to their gradients approach. Observing a correlation of r>0.5 is provided as supporting evidence but only in a very general analysis, not specific instances.

– The paper has a large number of analyses and several processing choices were made. While many appear reasonable, several choices are potentially problematic. For example, participants with gradients that correlated less than 0.5 with the average were discarded. The corrections for multiple comparisons were not clearly justified. In one case, clusters were accepted if p less than 0.005 and in another 0.01. More generally, if the correction was applied, why not adopt 0.05?

– Several analyses were performed but almost completely relegated to supplementary material. It is unclear how the Neurosynth and genetic analyses contribute to the study. Their inclusion contributes to the impression that the authors decided to try several analyses and see what relationships would be observed.

Additional specific recommendations:

– The way the paper is presented, it appears that the authors wanted to analyze the data in terms of the "gradients" approach and use that to investigate questions that would be better addressed with other techniques. If this impression is wrong, the authors would be encouraged to try to motivate the study more clearly.

– The paper is extremely dense and difficult to follow. I would recommend an extensive rewrite.

Reviewer #3:

This is a comprehensive and well powered study demonstrating that Presence-training results in increased eccentricity of bilateral temporal and right superior parietal areas, Perspective-training resulted in decreased eccentricity of right temporal regions and insular cortex, and there was no effect of Affect-training. These findings were significant following on family-wise error correction. Whether or not GSR was run, did not significantly affect the results. The sample size is excellent with two training groups (N=80 and N=81), a matched test-retest control cohort (N=90), and a separate single training set (N=81). Subjects were imaged at baseline and across 3 sessions x 3 monthly intervals (4 sessions total).

Specific recommendations

– Taking the eigenvectors of connectivity gradients (G1, G2, G3) the authors calculated the distance from the center of this coordinate system calling this the eccentricity. This measure is presumed to capture the vertex-wise intrinsic functional integration (low eccentricity) and segregation (high eccentricity).

– The section on task-based networks is not all that clearly written (page 8, line 7 onwards). Task-based networks were defined based on task-based fMRI and then these networks were used as input to the spatial gradient calculations. There should be some transition language after describing how each of the task-based networks was calculated, before immediately discussing how the dimensionality of the resting state connectomes was reduced. I had to go back and forth between methods, this section and the supplementary section to figure out if the connectivity matrix was based on the 400 node parcellation (used later for graph theory) or the networks defined by the tasks. It's not explicitly stated.

– While care is taken in the prediction section to randomize and then in other sections to look at the effect of GSR, there is no consideration given to the sensitivity of these results to various thresholding steps. In particular, the task defined networks are arbitrarily thresholded – and it is unclear how sensitive the results are to this threshold.

– Sensitivity of the gradient calculations to how the task-based thresholds were applied to define the networks should be provided. If the task-based maps are simply changing with practice effects then wouldn't this change the gradient calculations because of different inputs or defined networks. I initially assumed task-based networks were defined at each time point – but now I realize perhaps they are only defined once. Were the paradigms for functional localization only run once or were they run each time (before and after training)? We know that task-based modules change with practice effects (and presumably with task-relevant training). So how would changes at the level of these functional subunits influence these results? Is it appropriate to measure these only once and assume they are appropriate for each time point? If the nodes change with training across time would that account for the differences in eccentricity observed? Some supplementary data showing how the task activation maps change with training intervention might be helpful – if the tasks were run more than once.

– Does overall eccentricity predict behavior? It's unclear when it is stated that G1-G3 combined could predict compassion and ToM, if this is the same as using eccentricity to predict these behaviors. Is using the first three components the same as using the single eccentricity measure? If so then why not call it that since the previous section is all focused on eccentricity.

– In the prediction work it's not clear what exact behavioral measures were tested. There is a description on page 19 under behavioral markers starting on line 33, but it would be helpful if this was described earlier (maybe this is a journal formatting problem). However, in this section there is a description of how the measure for compassion and ToM were obtained but no description of the attention score.

– It wasn't clear to me if the specific networks tested did better at predicting the related tasks or if cross-network-task predictions were investigated. For example, you measured the extent to whether G1-G3 in the attention network predicted attention scores. Did these same G1-G3 values predict socio-affective or ToM scores? Did the socio-affective network predict socio-cognitive skills better than attention and ToM? In other words what happened if you mixed and matched these across networks – how critical are the specific network definitions to the prediction?

– Was any consideration given to the robustness of results to the parameter α which controls the influence of the density of sampling points on the manifold and also later the 10% sparsity threshold? How sensitive are these results to those decisions?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Functional and microstructural plasticity following social and interoceptive mental training." for further consideration by eLife. Your revised article has been evaluated by Tamar Makin (Senior Editor) and a Reviewing Editor (Camilla Nord).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers generally feel your manuscript is significant to the wider field, and with clarification and editing, would be of interest to a broad audience. They highlight several strengths, including the longitudinal approach and sample size. They suggest several key changes that could be made, in particular, two reviewers suggest strengthening the clarity of your central argument (i.e. what was the main goal of the study?), two reviewers suggest tests of the robustness/specificity of your predictive approach (e.g. "does G1-G3 in the attention network predict socio-affective or ToM scores?"), and there are a number of helpful minor clarifications suggested, including adding some of the analytical detail currently included only in the previous/referenced publications to the manuscript itself. We agree these changes would be useful for the clarity and completeness of the manuscript.

Reviewer #1 (Recommendations for the authors):

This study has a number of strengths, including sample size, longitudinal experimental design, and MRI methods. The connections between depth-specific qT1 and resting state network features, as well as their combined ability to predict performance after cognitive training are particularly interesting. Overall, the study provides a thorough examination of training-related functional and structural changes in social-cognitive related brain networks. While the authors' individual claims are supported by their data, the main conclusion of the manuscript seems diluted as the many findings and interpretations presented are not tightly connected.

There are a few areas in which the methodology/rationale is unclear as described and could benefit from further refinement. These are detailed below.

1. The manuscript presents a set of interesting observations but seems to be missing a main argument. There can be several potential candidates for it, including (1) social cognitive training leading to changes in resting-state connectivity and depth-dependent qT1, indicating functional and microstructural plasticity, or (2) affect, presence, and perspective training leading to differential changes in network integration/segregation, supporting the global workspace theory of cognition, or (3) training-induced functional and intracortical microstructural changes are related depending on the cortical depth and specific training task, and so on. This is a very information-heavy study, so I would recommend distilling a more specific main idea and tailoring your results/discussion to it.

2. The data are analyzed and presented on multiple levels of granularity, which is very impressive but in the meantime makes the Results section hard to follow. For example, the findings for longitudinal connectivity changes are discussed in terms of (1) eccentricity of the whole brain, (2) each of the three gradients, (3) a priori functional networks, and combinations of the above (e.g., changes along gradient 3 of the a priori attention network). I would recommend the authors trim any redundant analyses or clarify the distinction between these analytical levels and the significance of including all.

3. Following the previous comment, it would be helpful to briefly introduce the importance of extracting and examining three gradients, especially G3, which in my experience is less seen in the literature.

4. Please provide more details for statistical analysis in the methods section. For example, in the comparison of presence vs. perspective, is it overall changes after presence training vs. after perspective training, or changes in the selective group that had perspective training after presence?

5. 12 cortical layers were sampled from the qT1 map acquired at 1mm isotropic resolution. Given that many changes were observed near the pial surface, such as Figure 3A-ii. Please discuss if and how the effects of partial volume averaging were accounted for. Were all qT1-related analyses controlled for cortical thickness?

6. I must admit that I'm a bit confused about the qT1 layer results, especially those in Figure 3B. The colored lines seem to indicate across-depth qT1 changes in each functional region. Then why would there be four lines for all networks? For example, why is there a green line, indicating perspective network, in the plot for attention network results? More details in the figure caption would be helpful.

Reviewer #2 (Recommendations for the authors):

In the manuscript entitled "Functional and microstructural plasticity following social and interoceptive mental training" by Valk et al., the authors present an analysis of the ReSource study data wherein they examine how gradients of functional connectivity and microstructure change following mindfulness and cognitive training. Their findings indicate that individuals' functional connectivity and cortical microstructure change longitudinally in response to these interventions, providing compelling evidence that interventions such as mindfulness change the brain's structure. Additionally, the authors used these changes to predict measures of attention, compassion, and perspective taking.

I was invited to review this manuscript after an initial round of revisions. However, I was not provided a manuscript with changes tracked, which meant I could not review the paper before and after the authors' changes. Additionally, the authors provided only a summary of their changes to the original reviewers, rather than a point-by-point response. This made it unclear which of the original reviewers' comments were addressed and which were not. As such, instead of offering new comments, I have chosen to go through the original reviewers' comments and pick out ones that I (i) think are important and (ii) do not believe have been addressed by the authors.

"The word 'module' is used to describe the different behavioral training regimens that participants completed. As the authors are likely aware, this word is also commonly used to describe network structure. This makes phrases such as "module-specific behavioral change" and "behavioral changes across modules" difficult to parse. The authors may want to consider revising their use of the term module."

I agree with R1 here. The use of the term 'module' conflicts with the broader fields typical use of the term (referring to modules within graph topology). Could the authors consider rephrasing to 'training module' or TM?

"The central goal of the study is unclear. If the objective was to, as stated in some places, determine changes in integration/segregation of networks, the approach seems too indirect. A direct approach would evaluate these properties with graph theory. The authors do provide some results in that direction, but it is not clear why the results are secondary and mainly used to lend support to their gradients approach."

I agree with R2 here. In general, I found the link between the authors measure of eccentricity and the twin pillars of functional integration and segregation to be unclear. The authors state:

"we calculated region-wise distances to the center of a coordinate system formed by the first three gradients G1, G2, and G3 for each individual [based on the Schaefer 400 parcellation (67)]. Such a gradient eccentricity measures captures intrinsic functional integration (low eccentricity) vs segregation (high eccentricity) in a single scalar value (68)."

I understand that this statement includes a relevant citation, but I think there is room for more intuition building here. What does high eccentricity correspond to in this distance calculation? Is it high distance from the center of a coordinate system? If so, why does high distance from center correspond to a segregated brain? Why does low distance from center correspond to an integrated brain? Like R2, I found it difficult to reconcile this gradient-distance based metric with my graph topology understanding of segregation and integration.

Prediction analyses:

R1 stated:

"Although potentially quite interesting, it is not clear that the connectivity-based prediction of behavioral changes is very robust. Effect sizes are small to medium, the methods used for these analyses are prone to data leakage (and steps to protect against these problems are not described), effect size estimates are based on cross-validation alone (as opposed to out-of-sample tests), and there are many experimenter degrees of freedom."

R3 stated:

"In the prediction work it's not clear what exact behavioral measures were tested. There is a description on page 19 under behavioral markers starting on line 33, but it would be helpful if this was described earlier (maybe this is a journal formatting problem). However, in this section there is a description of how the measure for compassion and ToM were obtained but no description of the attention score."

And

"It wasn't clear to me if the specific networks tested did better at predicting the related tasks or if cross-network-task predictions were investigated. For example, you measured the extent to whether G1-G3 in the attention network predicted attention scores. Did these same G1-G3 values predict socio-affective or ToM scores? Did the socio-affective network predict socio- cognitive skills better than attention and ToM? In other words what happened if you mixed and matched these across networks – how critical are the specific network definitions to the prediction?"

Presently, I do not think these comments about the authors' prediction analyses have been addressed. Moreover, I too have concerns about the authors' approach. For example, the authors state "Before running our model, we regressed out age and sex from the brain markers." Here, it's unclear whether this nuisance regression was done in a leakage resistant way or not. This sentence implies that age and sex were regressed out of all the data in a single step prior to running the prediction model. If this is the case, this approach will cause leakage and spuriously boost prediction performance. To avoid this, the authors should consider incorporating nuisance regression into their cross-validation model, wherein nuisance models are fit to the training data and applied to the test data.

Reviewer #3 (Recommendations for the authors):

The study by Valk and colleagues investigated the impact of various forms of social mental training on resting-state functional connectivity and myeloarchitecture using a large-scale longitudinal multimodal dataset. The examination of these changes in combination is particularly noteworthy.

However, a few key points should be addressed to further improve the study.

[Line 140] The use of task-based networks to summarize changes across the cortex may be problematic, as the metrics averaged within each network may be influenced by small clusters, rather than reflecting the entire network. The FDR-survived changes in Attention and Interoception networks may be due to overlap in vertices, rather than network properties. To avoid this, it may be beneficial to consider alternative methods for summarizing whole-cortex changes.

[Line 217] The motivation for the selective analysis is clear, but the overall effects of the training were unclear until later in the manuscript (Line 234 and Supplementary Figure 6). It may be beneficial to describe the overall effects of training upfront.

[Line 268] The predictive performance of the models was not explicitly tested to determine if it was above the chance level. For a nonparametric test, it may be useful to calculate the null distribution of chance level performance through the use of permuted pairs of predictors and targets.

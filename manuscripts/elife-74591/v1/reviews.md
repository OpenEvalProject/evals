# Peer review - Round 1

Editors:
- Timothy Verstynen, https://ror.org/05x2bcf33 Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74591.sa0](https://doi.org/10.7554/eLife.74591.sa0)

This manuscript describes a fascinating experiment looking at gross network dynamics across cognitive and motor circuits and across different stages of learning, during an adaptive visuomotor learning experiment in the MRI environment. The finding of reliable "excursions" from low-dimensional network states that are associated with learning, primarily in cognitive networks, and that this excursion metric is a reliable indicator of differences in learning has strong implications for our understanding of the way macroscopic brain networks learn new skills.


---

# Peer review - Round 1

Editors:
- Timothy Verstynen, https://ror.org/05x2bcf33 Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74591.sa1](https://doi.org/10.7554/eLife.74591.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Neural Excursions from Low-Dimensional Manifold Structure Explain Intersubject Variation in Human Motor Learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Chris Baker as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

This manuscript describes a fascinating experiment looking at gross network dynamics across cognitive and motor circuits and across different stages of learning, during an adaptive visuomotor learning experiment in the MRI environment. The authors found that there were reliable "excursions" from low-dimensional network states that are associated with learning, primarily in cognitive networks, and that this excursion metric is a reliable indicator of differences in learning.

All three reviewers thought this was a very well designed study, with sophisticated analyses designed to ask deep questions about the nature of brain network interactions during motor skill learning. This is reflected in the reviews (shown below). There are a few points of clarification, however, that need to be resolved before publication.

Here I provide a singular consolidated review, along 3 major themes, for guidance with your revisions. You can feel free to organize your replies around the consolidated review.

General concerns

1. Manuscript logic

Reviewer 1 felt that the manuscript describes essentially 2 phases of inquiry: (1) do excursions of network states, during the task, from resting-state baselines, associate with learning? and (2) if so what are the characteristics of these network changes in motor and cognitive networks? Yet the logic of first identifying an effect and then characterizing it is reversed in the manuscript. The authors start by carefully explaining how cognitive and motor subnetworks vary across learning, with cognitive networks having more consistent shifts across groups, and ‘then’ highlight how deviations from resting states correlates with learning and distinguishes learning groups. This seems to put the cart before the horse.

Reviewer 2 also wondered about the restriction to motor and cognitive subnetworks, wondering at times how other networks that might be involved in the task (e.g., visual regions for the perception of the stimuli; or endogenous attentional regions that might have otherwise impacted the performance, and hence would need to be inhibited in order to promote effective performance) may have been associated with the task. Have the authors analysed data outside of the selected ROIs? And do these regions conform to expectation?

2. Groups

Reviewer 1 thought that the stratification of the three learning groups, based on behavioral performance, feels a little post hoc, particularly given the sample size of the study. It is particularly odd given how the excursion metrics are calculated on a per-subject basis, which would be perfect for a true individual differences analysis. Was a subject-wise association analysis performed and failed? If the goal is to look at individual differences in learning driven by excursions from a resting null state, it seems like a subject-by-subject comparison is more intuitive. Of course, if the sample size is too small for such analysis and stratification based on learning style increases sensitivity, then that is fine (it happens with pesky imaging studies). The authors should, at a minimum, address why this was not done.

This was mirrored in Reviewer 3's concerns as well. The reviewer points out that this manuscript sets out to address how brain dynamics underlie individual differences in learning, but these remain addressed largely as two separate questions: (1) what are the differences amongst participants (with compelling finding of distinct subgroups)? (2) what is the underlying brain dynamics. While the latter question is analysed by splitting individuals into subgroups, the results do not present compelling evidence of group differences. Most of the metrics show no differences amongst the groups or very subtle differences (e.g. differences in cognitive network embedding in Figure 3g), which are commonly only descriptive and not backed up with the necessary statistics. This may be because of a relatively small sample size (N=32) which is likely insufficient to address the question of intersubject variation with sufficient power. It is therefore difficult to say if the presented findings are evidence of absence of group differences or absence of evidence for intersubject variation. In light of this, the title of the manuscript seems misleading, as the manuscript does not present convincing evidence of how 'neural excursions from low-dimensional manifold structure explain intersubject variation in human motor learning'. Therefore, the link between intersubject differences and network dynamics should be made stronger to reflect the abstract, title and interpretation, or the two questions (on behavioural differences and network dynamics) should be addressed separately.

3. Analysis

Reviewer 1 felt that the manifold analysis is incredibly interesting and appears to yield fascinating learning dynamics (particularly the mfPCA results in Figure 6). However, a careful read of the methods leads to many questions. For example, it is not intuitively clear how the authors get to the form of the tangent vector in Eq. 1. Also, it is not clear if the weight graphs (Figures 3 & 4) are derived from the tangent vectors (T) or the projection into the covariance matrices (S)? What is "x_t" in the excursion calculations? Is P^{on} just a norm on the PCA components? Why use a mixture of linear and non-linear methods to find low dimensional subspaces? Given the novelty of the approach, understanding these steps is crucial for the reader to interpret the results.

This was echoed in Reviewer 2's concern as to why the authors chose to use UMAP (a non-linear dimensionality reduction technique) to demonstrate the utility of their mean-centering approach (which the reviewer found to be well-justified), but then later used a functional variant of PCA on the actual data themselves.

Along the same lines, Reviewer 1 felt that the resting state is used as the baseline by which deviances are estimated. Wouldn't the Baseline period during the task be a more appropriate baseline for looking at learning related changes? It seems like using rest, without the same sensory or motor engagement, would be the wrong way to isolate excursions from the manifold from learning alone.

This was echoed in Reviewer 3's comments as well. The network embedding analyses are performed by defining regions of interest (across cognitive and sensorimotor networks), followed by calculating the covariance matrix across defined regions in each learning stage, and contrasting the obtained matrices to the group average resting state. The authors justify well why centering to the group average resting state is necessary to remove subject-specific differences and focus on the learning-related changes. Yet, their subsequent assessment across the baseline/early/late stages allows for interpretations of only how the relative differences in the strength of (task)-components differs across learning compared to the resting state. Given the nature of the visuomotor rotation task, wouldn't the initial 'baseline' stage provide a more natural starting point to assess changes that occur with learning? This would also enable a more direct assessment of whether there is a reconfiguration of network dynamics after the onset of rotation, and how it unfolds during subsequent learning.

Reviewer 2 also wondered whether the increase in the diffuse cognitive component, in which covariance was relatively wide-spread across the cortical regions, may have been associated with a decrease in the BOLD signal as a function of improved performance? To this end, it could be useful for the authors to plot the raw BOLD (or β weights following a GLM) collapsed across the loadings of each of the eigenvectors. This would give the reader a sense of how the covariance related to recruitment, as covariance will increase regardless of whether pairs of regions both went up or both went down.

Reviewer 3 had similar concerns with the interpretation of the manifold analyses. The presented analyses on network dynamics are rigorous and justified, yet interpreting some of the presented results is not straightforward. For instance, in Figure 3e, it seems that the mean component effect for embedding of cognitive networks shows an effect where the network landscape initially moves away from 'baseline' to 'early' stage, and then reverses for 'late' stage such that late stage is more similar to baseline than to early stage on component 1. In the manuscript, only a comparison across the groups is interpreted (FF and SF groups showing more similar trajectories), but how does one interpret changes in the trajectories themselves? Could it be that the changes in relative connectivity within this component (the dorsoattentional network and between dorsoattentional and frontoparietal networks) reflects increases in error rate, or differences in reaction time? There is potential to link these network metrics to subject performance which would help in interpreting the findings as well as relate them more closely to variation in performance.

Reviewer #1 (Recommendations for the authors):

This manuscript describes a fascinating experiment looking at gross network dynamics across cognitive and motor circuits and across different stages of learning, during an adaptive visuomotor learning experiment in the MRI environment. The authors found that there were reliable "excursions" of network states associated with learning, primarily in cognitive networks, and that this excursion metric is a reliable indicator of differences in learning.

Overall, this is a very well designed study, with sophisticated analyses designed to ask deep questions about the nature of brain network interactions during motor skill learning. There are many strengths here. My critique focuses only on the aspects of the study and manuscript that require clarity.

1. Manuscript logic

The manuscript describes essentially 2 phases of inquiry: (1) do excursions of network states, during the task, from resting-state baselines, associate with learning? and (2) if so what are the characteristics of these network changes in motor and cognitive networks? Yet the logic of first identifying an effect and then characterizing it is reversed in the manuscript. The authors start by carefully explaining how cognitive and motor subnetworks vary across learning, with cognitive networks having more consistent shifts across groups, and *then* highlight how deviations from resting states correlates with learning and distinguishes learning groups. This seems to put the cart before the horse.

2. Groups

The stratification of the three learning groups, based on behavioral performance, feels a little post hoc, particularly given the sample size of the study. It is particularly odd given how the excursion metrics are calculated on a per-subject basis, which would be perfect for a true individual differences analysis. Was a subjectwise association analysis performed and failed? If the goal is to look at individual differences in learning driven by excursions from a resting null state, it seems like a subject-by-subject comparison is more intuitive. Of course, if the sample size is too small for such analysis and stratification based on learning style increases sensitivity, then that is fine (it happens with pesky imaging studies). The authors should, at a minimum, address why this was not done.

3. Analysis

The manifold analysis is incredibly interesting and appears to yield fascinating learning dynamics (particularly the mfPCA results in Figure 6). However, a careful read of the methods leads to many questions. For example, it is not intuitively clear how the authors get to the form of the tangent vector in Eq. 1. Also, it is not clear if the weight graphs (Figures 3 & 4) are derived from the tangent vectors (T) or the projection into the covariance matrices (S)? What is "x_t" in the excursion calculations? Is P^{on} just a norm on the PCA components? Why use a mixture of linear and non-linear methods to find low dimensional subspaces? Given the novelty of the approach, understanding these steps is crucial for the reader to interpret the results.

Along the same lines, resting state is used as the baseline by which deviances are estimated. Wouldn't the Baseline period during the task be a more appropriate baseline for looking at learning related changes? It seems like using rest, without the same sensory or motor engagement, would be the wrong way to isolate excursions from the manifold from learning alone.

Reviewer #2 (Recommendations for the authors):

The authors use a set of dimensionality reduction techniques to analyse fMRI data collected while participants performed a sensorimotor adaptation task. They find evidence to suggest that the capacity for participants to learn the sensorimotor contingencies was associated with deviation from low-dimensional manifolds estimated from the data.

The manuscript was clearly presented, and the methodological choices were well-justified. There was a thorough review of the existing literature, focussing on how low-dimensional signatures estimated from neuroimaging data might relate to the capacity to learn sensorimotor contingencies in a research setting. The aims of the project were spelled out clearly, and the methods aligned well with the proposed goals of their study.

One aspect of the study that I enjoyed was the appreciation of the individual differences in learning rates. -While the group mean appeared to show a gradual increase in performance across the cohort, clustering of the trajectories revealed separable patterns of performance improvement which, if analysed en masse, may have led to erroneous conclusions regarding the neurobiological substrates of these effects. One side-effect of this approach is that it did render the Results quite complex, however the authors did a nice job of regularly referring back to the main point of the manuscript when relaying each set of results.

I was a little confused as to why the authors chose to use UMAP (a non-linear dimensionality reduction technique) to demonstrate the utility of their mean-centering approach (which I found to be well-justified), but then later used a functional variant of PCA on the actual data themselves.

I expect that this manuscript will have a positive effect on the field, as it links exciting dimensionality techniques to data recorded across the performance of an interesting cognitive task.

I did find myself wondering at times how other networks that might be involved in the task (e.g., visual regions for the perception of the stimuli; or endogenous attentional regions that might have otherwise impacted the performance, and hence would need to be inhibited in order to promote effective performance) may have been associated with the task. Have the authors analysed data outside of the selected ROIs? And do these regions conform to expectation?

I found myself wondering whether the increase in the diffuse cognitive component, in which covariance was relatively wide-spread across the cortical regions, may have been associated with a decrease in the BOLD signal as a function of improved performance? To this end, it could be useful for the authors to plot the raw BOLD (or β weights following a GLM) collapsed across the loadings of each of the eigenvectors. This would give the reader a sense of how the covariance related to recruitment, as covariance will increase regardless of whether pairs of regions both went up or both went down.

Reviewer #3 (Recommendations for the authors):

The present investigation aimed at investigating changes in brain dynamics that underlie motor learning, and how this relates to intersubject differences in learning.

The manuscript presents a learning fMRI study, employing the visuomotor rotation paradigm, which participants performed on two consecutive days. To assess differences in learning ability amongst participants, participants' performance is clustered based on behavioural measures of error and savings, which results in three distinct subgroups of learners. Then, the brain dynamics is assessed by estimating the covariance networks from cognitive and sensorimotor regions across different learning epochs. Several metrics are derived to explain how network dynamics changes with learning, finding especially differences within the 'cognitive' network. These metrics are also separately inspected across the three distinct subgroups with the aim to relate network dynamics to intersubject variation in learning ability.

Strengths:

The question on how brain dynamics change during learning is an important one, of potential interest to a broad audience. The authors utilize advanced and rigorous techniques to address this question. This has in the domain of motor learning, specifically on visuomotor rotation not been done and is therefore an important advancement of the field. Also dividing brain regions into 'motor' and 'cognitive' networks is relevant as several motor learning studies have demonstrated recently that 'motor' learning might be underpinned by substantial changes in regions traditionally regarded as 'cognitive'. Finally, the clustering of participants into distinct groups based on their learning ability is justified and a valid approach, especially for small sample sizes, to aim at investigating differences in learning ability across individuals. Despite many strengths of the manuscript, there are some outstanding concerns, especially pertaining to the interpretation of the link between brain dynamics and individual differences in learning.

Weaknesses:

1) First, this manuscript sets out to address how brain dynamics underlie individual differences in learning, but these remain addressed largely as two separate questions: 1) what are the differences amongst participants (with compelling finding of distinct subgroups), 2) what is the underlying brain dynamics. While the latter question is analysed by splitting individuals into subgroups, the results do not present compelling evidence of group differences. Most of the metrics show no differences amongst the groups or very subtle differences (e.g. differences in cognitive network embedding in Figure 3g), which are commonly only descriptive and not backed up with the necessary statistics. This may be because of a relatively small sample size (N=32) which is likely insufficient to address the question of intersubject variation with sufficient power. It is therefore difficult to say if the presented findings are evidence of absence of group differences or absence of evidence for intersubject variation. In light of this, the title of the manuscript seems misleading, as the manuscript does not present convincing evidence of how 'neural excursions from low-dimensional manifold structure explain intersubject variation in human motor learning'. Therefore, the link between intersubject differences and network dynamics should be made stronger to reflect the abstract, title and interpretation, or the two questions (on behavioural differences and network dynamics) should be addressed separately.

2) The presented analyses on network dynamics are rigorous and justified, yet interpreting some of the presented results is not straightforward. For instance, in Figure 3e, it seems that the mean component effect for embedding of cognitive networks shows an effect where the network landscape initially moves away from 'baseline' to 'early' stage, and then reverses for 'late' stage such that late stage is more similar to baseline than to early stage on component 1. In the manuscript, only a comparison across the groups is interpreted (FF and SF groups showing more similar trajectories), but how does one interpret changes in the trajectories themselves? Could it be that the changes in relative connectivity within this component (the dorsoattentional network and between dorsoattentional and frontoparietal networks) reflects increases in error rate, or differences in reaction time? There is potential to link these network metrics to subject performance which would help in interpreting the findings as well as relate them more closely to variation in performance.

3) The network embedding analyses are performed by defining regions of interest (across cognitive and sensorimotor networks), followed by calculating the covariance matrix across defined regions in each learning stage, and contrasting the obtained matrices to the group average resting state. The authors justify well why centering to the group average resting state is necessary to remove subject-specific differences and focus on the learning-related changes. Yet, their subsequent assessment across the baseline/early/late stages allows for interpretations of only how the relative differences in the strength of (task)-components differs across learning compared to the resting state. Given the nature of the visuomotor rotation task, wouldn't the initial 'baseline' stage provide a more natural starting point to assess changes that occur with learning? This would also enable a more direct assessment of whether there is a reconfiguration of network dynamics after the onset of rotation, and how it unfolds during subsequent learning.

It would be useful if the performed analyses / metrics were better justified or interpreted. For instance, in the functional PCA analysis (Figure 6) what is the interpretation of having a sinusoidal component? Is this in any way linked to the onset of rotation? If not, what would be the rationale of having such a component in the brain dynamics? What could this reflect?

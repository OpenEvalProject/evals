# Author response - Round 1

Authors:
- André Ferreira Castro ([ORCID: 0000-0002-6841-1952](https://orcid.org/0000-0002-6841-1952))
- Lothar Baltruschat
- Tomke Stürner ([ORCID: 0000-0003-4054-0784](https://orcid.org/0000-0003-4054-0784))
- Amirhoushang Bahrami ([ORCID: 0000-0001-5841-2516](https://orcid.org/0000-0001-5841-2516))
- Peter Jedlicka ([ORCID: 0000-0001-6571-5742](https://orcid.org/0000-0001-6571-5742))
- Gaia Tavosanis ([ORCID: 0000-0002-8679-5515](https://orcid.org/0000-0002-8679-5515))
- Hermann Cuntz ([ORCID: 0000-0001-5445-0507](https://orcid.org/0000-0001-5445-0507))

## Response text

DOI: [10.7554/eLife.60920.sa2](https://doi.org/10.7554/eLife.60920.sa2)

The reviewers raised several points that the authors should address in a revision of the paper. These are summarised here; the full reviewer comments are included below for reference and need not be addressed point-by-point. The reviewers agreed that no further experiments are necessary.

1) Check/provide evidence that the sampling rate of the time lapse imaging doesn't alias the measurements of dendritic growth and/or present a problem for relating data to the model.

Using the tools and resources available to us at this point, a higher temporal resolution analysis would not be feasible. This would require hundreds of additional reconstructions and their registration for the time-lapse analysis. The analysis is therefore bound to the resolution that we used and we agree with reviewer #2 (major comment #1) that higher frequency dynamics will elude our analysis. However, we would like to note that we used the same temporal resolution in the time-lapse experiments and in the random retraction growth model. The focus of this data-driven model was to replicate the growth behaviour of c1vpda neurons at this temporal scale. The agreement between simulated data and experiments validates the interpretation of the data. Higher resolution analyses will surely be useful in the future to better understand the fine details of the dynamics of dendrite growth in these cells. Nevertheless, the aim of our study was to connect the function of c1vpda neurons to dendrite differentiation across embryonic and larval stages. After the submission of the present manuscript, a complementary pre-print focusing on the molecular basis of embryonic c1vpda neurons development was submitted to bioRxiv (Palavalli et al., 2020). Since this study focused in a much smaller developmental timewindow of analysis, they used higher temporal resolution imaging to provide a link between Dscam1 molecule and branch dynamics. This level of specificity comes with the cost of not capturing the overall functional assembly of c1vpda neurons (see as well major comment #2 from reviewer #2). Finally, in line with the suggestion of the reviewer, in the revised paper (both in Results and Discussion), we put emphasis on the potential differences in growth-retraction branch dynamics that may arise due to different temporal resolutions of imaging:

”Note that the results are the net value of branch tip position between observation points at time intervals of 1hr. Even though the interpretation of this analysis is valid for the selected time interval, higher temporal resolution will no doubt uncover higher frequency dynamics that are not captured here, a common problem of any time-lapse analysis and indeed of any type of image processing (Helmstaedter, 2013; Peng et al., 2017). However, the net changes within 1hr intervals are a stable result and provide for a phenomenological description and quantification of the branch reorganisation throughout the retraction phase.”;

”Due to the lack of high-throughput automatic digital tracing algorithms for neuronal morphologies the chosen temporal resolution for imaging (see Materials and methods) was determined as a trade-off between capturing c1vpda dendrite dynamics throughout embryonic and larval stages and tracing speed (Helmstaedter, 2013).”;

and

”The accordance between data and model further validates the chosen temporal resolution of imaging. In the future, as more sophisticated tracing algorithms develop more detailed datasets will become available for analysis and modelling (Peng et al., 2017).”.

Furthermore, we will make all the raw image-stacks available upon publication. This way, by providing all data at temporal resolution of 5min intervals, readers interested in this topic can trace the image-stacks and analyse the data in more detail.

2) Small variations in the model were identified – how are these justified (Figure 6B vs 2D)?

Thank you for highlighting this point. To improve clarity we added new text in the Results section and Figure 6 legend with further details about the differences between the models. Please see below some points that clarify this comment:

1) The model in Figure 2D/Figure 6B (MST model – represented as a dashed line in those figures) is a reconstruction model. Reconstruction algorithms are the simplest of dendrite patterning computational models. They do not capture the evolution of the developmental processes and simply reconstruct dendrites at a particular point in time. These algorithms are designed to generate morphologies that replicate the shape of real cells at a static developmental time point. First, from a given dendritic tree different morphometrics are quantified, e.g. branch points, length, surface area. Then, the modeller makes assumptions about how these variables relate between each other. Particularly in the MST model used in our study, it is assumed that wiring minimisation is a key principle of dendrite wiring. Based on these assumptions, the algorithm then proceeds to generate morphologies by sampling from the distributions of real data.

2) The newly developed random retraction growth model (Computational dendrite growth model with stochastic retraction – in Materials and methods) seeks to explain the spatiotemporal differentiation of dendritogenesis. Such developmental algorithms need to specify how distinct morphometrics evolve through time, in order to make predictions about the growth process, as showed in Figure 6C and 6D. To properly constrain this model we needed dynamical morphometrics from the time-lapse data to specify how the distributions of the parameters change over time: such as elongation, branching and retraction rate of dendritic branches.

3) In Figure 2D, we first used the simpler static MST model as a first approach to test if the real data followed wiring minimisation principles. For each c1vpda morphology a MST counterpart with similar morphometrics was generated for comparison. After we developed the new random retraction growth model we used it to generated synthetic morphologies. Then, to validate random retraction growth model we wished to verify if the new synthetic dataset followed the same trends as the real data. As a first step, in Figure 6B, we compared the synthetic trees generated by the random retraction growth model with the MST model used in Figure 2D. The very good agreement between synthetic data generated by the random retraction growth model and the MST dashed line provided a first quality control for the data produced by our newly developed model. From Figure 2D/6B we gained the insight that real data and synthetic trees generated by the random retraction growth model behave similarly in respect with wiring optimisation.

3) The authors should consider balancing their citations toward invertebrate quantitative neuroanatomy and existing quantitative/computational development studies.

Thank you for the comments. We followed the suggestion of the reviewer and added new references to the Introduction. Particularly, we added references to recent studies in quantitative neuroanatomy during development. Additionally, we added references on the impact of dendritic morphology on computation in insects.

We reorganised the references in the Introduction to better highlight the importance of neuroanatomical studies in invertebrates. Note that the field of quantitative neuroanatomy is experiencing a revolution at the moment and citing all the published work and pre-prints available would be more suitable for a review paper. Finally, we added references to the Discussion section of the manuscript that focus on neuronal cell fate specification.

4) Additional data for Figure 5A (as a figure supplement) would aid intuition.

Thank you for your comment. The different simulations in the paper have different goals and address different questions. In Figure 5A (now Figure 5—figure supplement 1), we provide a first attempt at disentangling the morphological implications of the retraction phase by simulating the most extreme cases of branch retraction. It is not the point of the analysis performed in this figure to fully reproduce the different morphometric distributions in great detail. It was done only to provide insights for the next round of in-depth investigations presented in Figure 6. Therefore we restricted our statistical tests to mean comparison between key morphometrics. To avoid confusion for the reader we opted to move Figure 5A to Figure 5—figure supplement 1 that supports Figure 5 in the main text.

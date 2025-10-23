# Peer review - Round 1

Editors:
- Jerry L Workman, Stowers Institute for Medical Research , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17667.067](https://doi.org/10.7554/eLife.17667.067)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Live-Cell Single-Molecule Tracking Reveals Co-recognition of H3K27me3 and DNA Targets Polycomb Cbx7-PRC1 to Chromatin" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Jerry Workman is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tae-Hee Lee (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The Polycomp group proteins are essential for normal embryonic development. Furthermore, the members of Polycomb group are frequently overexpressed or mutated in cancer. Hence, understanding Polycomb action is crucial in health and disease. The Cbx proteins, part of the Polycomb complex, are thought to bind to H3K27me3 modification thereby recruiting the Polycomb protein PRC1 to the chromatin. Although the Cbx-PRC1 recruitment to chromatin is the established model, the molecular mechanisms behind this recruitment is poorly understood. Here, Zhen and colleagues have studied the action of Cbx family proteins by utilizing the new critical single-molecule imaging technique. Their study uncovers a new functional role for Cbx7 in targeting Cbx-PRC1 complex to the chromatin.

The conclusions are qualitatively supported by the data. This is a rare epigenetics paper based on real-time monitoring of nuclear protein behavior. The experiments are in general well-executed. However, significant revisions and clarifications are needed.

Essential revisions:

1) The conclusions need to be restated in a less deterministic manner. Based on my visual inspection of the movie files and the data (diffusion constant histograms), the cases analyzed with two diffusion components still contain a non-negligible chromatin-bound population. I agree with the suggested qualitative trends (i.e. increased or decreased chromatin-bound population). But I disagree with that the data supports the conclusions without uncertainty. I would recommend restating the conclusions with "contributes significantly" or something at a similar level instead of "essential" "necessary" "completely abolished" because these do not reflect the apparent uncertainty in the results.

2) As for data analysis, it is unclear to me why log of the diffusion constant values should distribute normally. According to the classical particle kinetics theory, one diffusion component in these histograms should follow an asymptotic growth (y = 1 – exp(-x/a)). Therefore, the histograms in this manuscript should be fit with three growth functions instead of three normal distributions. Or the authors could explain why log<r^2> should distribute normally. Either way, this point should be addressed before publication.

3) Another point unclear in the analysis is the criteria for a decision on fitting a histogram with two or three diffusion components. The criteria should be clearly stated. If the decisions were not based on quantitative criteria, I recommend fitting all the histograms with three components and drawing the conclusions accordingly (e.g. no convergence with three components or significantly reduced or increased chromatin-bound population, etc.).

4) The authors have shown by depleting H3K27me3 via Eed-/- cells, that chromatin binding of Cbx7 and Cbx8 require H3K27me3 (Figure 2). Cbx7 is further characterized by the authors. The authors should characterize Cbx2, -4, -6 and -8 in Ezh2-/- and Cbx8 in the Eed and Ezh2 rescue cells. This would strengthen the authors conclusions to show that Cbx7, and -8 require H3K27me3, while Cbx2, -4, -6 do not. Especially important would be to indicate that Cbx8 behaves similar to Cbx7.

5) It is not clear why the authors have further characterized Cbx7 but not Cbx8. Previous studies have shown differences in Cbx7 and Cbx8 action (Bernstein et al. 2006, Kaustov et al. 2011). In this manuscript the authors indicate that both Cbx7 and Cbx8 require H3K27me3 for chromatin binding. The authors should clarify why the authors have further characterized Cbx7 but not Cbx8.

6) The authors have measured the dwell times of individual single-molecules and determined the residence time of Cbx7 (Figure 4). Subsequently, the authors show that the residence time of Cbx7 is decreased by mutation or deletion of important Cbx7 regions. The authors state that the dwell time distribution is best fitted to a one-component exponential decay model. However, it is not shown whether the authors have examined the potential fit of their data to a two-, or multi-component exponential decay model.

Recent studies have shown (Chen et al. 2014, Morisaki et al. 2014, Swinstead et al. 2016) that transcription factor dwell times are usually fitted to a two-component exponential decay model, with fast dwell time representing non-specific binding and slow dwell time representing specific binding events at chromatin. The authors should clarify this issue.

See for example, Methods Mol Biol 833:177, 2012

"The survival distribution of bound molecules S(t) allows comparison of different experiments more easily than a traditional histogram of residence times for two reasons: First, in contrast to a traditional histogram, S(t) does not depend on arbitrary choices about the histogram binning. Second, when multiple populations of molecules with different residence times coexist, it is easier to directly visualize the fraction of molecules in each population because the cumulative histogram is fit with a multiexponential decay, with the amplitude of each exponential corresponding to the fraction size."

SMT# 1- For determination of fractional sizes of the three population of molecules, the authors acquire very rapidly (30ms exposure, no interval) and measure the diffusion coefficient of each population with the relative% . The authors discuss two different ways of doing this (Dm and Df1), but the details here are unclear.

SMT #2- For determination of residence times, the authors perform 30ms exposure and 1s interval. Then the authors estimate residence times. It is known that different intervals sample different population of molecules; thus the authors here are measuring different things between the 2 SMT experiments.

One biological contradiction that illustrates this problem is in Figure 7. The mutant Cbx7deltaCD-ATL has no CB (chromatin bound fraction, Figure 7C) according to SMT#1, but the authors are able to measure a residence time by SMT#2 for that fraction (Figure 7D).

Regarding SMT #2, there several issues in question.

- The exponential fitting of the data seems to be done on the histograms and not with the survival plots. As discussed above, the validity of this method is in question.

- The authors say that the best fit is one-component exponential. However, there is no evidence the authors attempted fitting to two exponentials, and no statistical analysis to justify their conclusion.

- Bleaching correction. Instead of using the same set of data to calculate bleaching, the authors use a fixed sample with histones. This is unacceptable because it is likely that fixed material will behave very differently than the non-fixed. Moreover, their bleaching fitting is again to a 1-exponential, but bleaching decay fits better to 2-exponential decay model. This likely contributes to the unusual residence time numbers the authors are getting. These times look to be a bit fast (~4s) considering the big intervals the authors are using (1s).

7) In the collection of single-molecule data for residence time estimation (Figure 4), the authors have used relative long dark time (Td) of 0.97s with total interval time (Tlap) of 1s. Previous studies have generally used shorter interval times of 10ms (Gebhardt et al. 2013), 20ms-100ms (Mazza et al. 2012), 200ms (Morisaki et al. 2014, Swinstead et al. 2016) and 500ms (Chen et al. 2014). Using a longer interval time will result in the capture of longer over the shorter tracks, which can result into overestimation of residence times. In addition, this could be the reason why the Cbx7 data fits to one-component rather than two-component, as transient binding is not seen due to long interval time. The authors should establish whether long interval time influences their dwell time distribution.

8) In Figure 4A, the authors show examples of bound and diffusing Cbx7 molecules. The examples are little puzzling. The bound Cbx7 molecule is stationary in their example for (at least) 70s while their dwell time histogram (Figure 4B) ends at 40s. If the authors are capturing 70s track, then it should be seen in the histogram. Furthermore, the diffusing Cbx7 molecule in their example moves within 10s. However, if the residence time of Cbx7 is ~4s, one would expect the molecule to move within 10s. These issues need to be clarified by the authors.

9) The authors show that disruption of Cbx7-PRC1 complex formation facilitates Cbx7 chromatin binding, but does not influence the residence time of Cbx7 (Figure 5). Why does the Cbx7 bind more to chromatin after disruption of complex formation? The authors should discuss this issue in greater depth because as currently presented, there is no explanation on this matter. In addition, in the text authors state that complex formation antagonizes the targeting of Cbx7 to chromatin. However, the data shows that is facilitates the targeting. This should be corrected by the authors.

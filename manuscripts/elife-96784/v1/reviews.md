# Peer review - Round 1

Editors:
- Adrien Peyrache, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96784.4.sa0](https://doi.org/10.7554/eLife.96784.4.sa0)

This valuable study provides a novel method to detect sleep cycles based on variations in the slope of the power spectrum from electroencephalography signals. The method, dispensing with time-consuming and potentially subjective manual identification of sleep cycles, is supported by solid evidence and analyses. This study will be of interest to researchers and clinicians working on sleep and brain dynamics.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96784.4.sa1](https://doi.org/10.7554/eLife.96784.4.sa1)

In this study, Rosenblum et al introduce a novel and automatic way of calculating sleep cycles from human EEG. Previous results have shown that the slope of the non-oscillatory component of the power spectrum (called the aperiodic or fractal component) changes with sleep stage. Building on this, the authors present an algorithm that extracts the continuous-time fluctuations in the fractal slope and propose that peaks in this variable can be used to identify sleep cycle limits. Cycles defined in this way are termed "fractal cycles". The main focus of the article is a comparison of "fractal" and "classical" (ie defined manually based on the hypnogram) sleep cycles in numerous datasets.

The manuscript amply illustrates through examples the strong overlap between fractal and classical cycle identification. Accordingly, a high percentage (81%) can be matched one-to-one between methods and sleep cycle duration is well correlated (around R = 0.5). Moreover, the methods track certain global changes in sleep structure in different populations: shorter cycles in children and longer cycles in patients medicated with REM-suppressing anti-depressants. Finally, a major strength of the results is that they show similar agreement between fractal and classical sleep cycle length in 5 different data sets, showing that it is robust to changes in recording settings and methods.

The match between fractal and classical cycles is not one-to-one. For example, the fractal method identifies a correlation between age and cycle duration in adults that is not apparent with the classical method.

The difference between the fractal and classical methods appear to be linked to the uncertain definition of sleep cycles since they are tied to when exactly the cycle begins/ends and whether or not to count cycles during fractured sleep architecture at sleep onset. Moreover, the discrepancies between the two are on the order of that found between classical cycles defined manually or via an automatic algorithm.

Overall the fractal cycle is an attractive method to study sleep architecture since it dispenses with time-consuming and potentially subjective manual identification of sleep cycles. However, given its difference with the classical method, it is unlikely that fractal scoring will be able to replace classical scoring directly. By providing a complementary quantification, it will likely contribute to refining the definition of sleep cycles that is currently ambiguous in certain cases. Moreover, it has the potential to be applied on animal studies which rarely deal with sleep cycle structure.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96784.4.sa2](https://doi.org/10.7554/eLife.96784.4.sa2)

Summary:

This study focused on using strictly the slope of the power spectral density (PSD) to perform automated sleep scoring and evaluation of the durations of sleep cycles. The method appears to work well because the slope of the PSD is highest during slow-wave sleep, and lowest during waking and REM sleep. Therefore, when smoothed and analyzed across time, there are cyclical variations in the slope of the PSD, fit using an IRASA (Irregularly resampled auto-spectral analysis) algorithm proposed by Wen & Liu (2016).

Strengths:

The main novelty of the study is that the non-fractal (oscillatory) components of the PSD that are more typically used during sleep scoring can be essentially ignored because the key information is already contained within the fractal (slope) component. The authors show that for the most part, results are fairly consistent between this and conventional sleep scoring, but in some cases show disagreements that may be scientifically interesting.

Weaknesses:

The previous weaknesses were well-addressed by the authors in the revised manuscript. I will note that from the fractal cycle perspective, waking and REM sleep are not very dissimilar. Combining these states underlies some of the key results of this study.

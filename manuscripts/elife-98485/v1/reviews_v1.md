# Peer review - Round 1

Editors:
- Dion K Dickman, University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98485.3.sa0](https://doi.org/10.7554/eLife.98485.3.sa0)

This paper presents miniML, an AI-based framework for the detection of synaptic events. Benchmark results presented in the paper are compelling, demonstrating the superiority of miniML over current state-of-the-art alternatives. The performance of miniML is demonstrated across various experimental paradigms, showing that miniML has the potential to become a valuable tool for the analysis of synaptic signals.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98485.3.sa1](https://doi.org/10.7554/eLife.98485.3.sa1)

O'Neill et al. have developed a software analysis application, miniML, that enables the quantification of electrophysiological events. They utilize a supervised deep learned-based method to optimize the software. miniML is able to quantify and standardize the analyses of miniature events, using both voltage and current clamp electrophysiology, as well as optically driven events using iGluSnFR3, in a variety of preparations, including in the cerebellum, calyx of held, golgi cell, human iPSC cultures, zebrafish, and Drosophila. The software appears to be flexible, in that users are able to hone and adapt the software to new preparations and events. Importantly, miniML is an open source software free for researchers to use and enables users to adapt new features using Python.

Overall this new software has the potential to become widely used in the field and an asset to researchers. Importantly, a new graphical user interface has been generated that enables more user control and a more user-friendly experience. Further, the authors demonstrate how miniML performs relative to other platforms that have been developed, and highlight areas where miniML works optimally. With these revisions, miniML should now be of considerable benefit and utility to a variety of researchers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98485.3.sa2](https://doi.org/10.7554/eLife.98485.3.sa2)

Summary:

This paper presents miniML as a supervised method for detection of spontaneous synaptic events. Recordings of such events are typically of low SNR, where state-of-the-art methods are prone to high false favourable rates. Unlike current methods, training miniML requires neither prior knowledge of the kinetics of events nor the tuning of parameters/thresholds.

The proposed method comprises four convolutional networks, followed by a bi-directional LSTM and a final fully connected layer, which outputs a decision event/no event per time window. A sliding window is used when applying miniML to a temporal signal, followed by an additional estimation of events' time stamps. miniML outperforms current methods for simulated events superimposed on real data (with no events) and presents compelling results for real data across experimental paradigms and species.

Strengths:

The authors present a pipeline for benchmarking based on simulated events superimposed on real data (with no events). Compared to five other state-of-the-art methods, miniML leads to the highest detection rates and is most robust to specific choices of threshold values for fast or slow kinetics. A major strength of miniML is the ability to use it for different datasets. For this purpose, the CNN part of the model is held fixed and the subsequent networks are trained to adapt to the new data. This Transfer Learning (TL) strategy reduces computation time significantly and more importantly, it allows for using a substantially smaller data set (compared to training a full model) which is crucial as training is supervised (i.e. uses labeled examples).

Weaknesses:

The authors do not indicate how the specific configuration of miniML was set, i.e. number of CNNs, units, LSTM, etc. Please provide further information regarding these design choices, whether they were based on similar models or if chosen based on performance.

The data for the benchmark system was augmented with equal amounts of segments with/without events. Data augmentation was undoubtedly crucial for successful training.

(1) Does a balanced dataset reflect the natural occurrence of events in real data? Could the authors provide more information regarding this matter?

(2) Please provide a more detailed description of this process as it would serve users aiming to use this method for other sub-fields.

The benchmarking pipeline is indeed valuable and the results are compelling. However, the authors do not provide comparative results for miniML for real data (figures 4-8). TL does not apply to the other methods. In my opinion, presenting the performance of other methods, trained using the smaller dataset would be convincing of the modularity and applicability of the proposed approach.

Impact:

Accurate detection of synaptic events is crucial for the study of neural function. miniML has a great potential to become a valuable tool for this purpose as it yields highly accurate detection rates, it is robust, and is relatively easily adaptable to different experimental setups.

Comments on revisions:

The revised manuscript presents a compelling framework. The performance of mini ML is thouroughly explored and compared to several benchmarks. The training process along with other technical issues are now described in a satisfactory level of detail.

I think the authors did a great job. They answered all claims and concerns raised by me and the other reviewers.

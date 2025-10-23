# Peer review - Round 1

Editors:
- Juan Alvaro Gallego, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94165.3.sa0](https://doi.org/10.7554/eLife.94165.3.sa0)

This valuable study reports on the characteristics of premotor cortical population activity during the execution and observation of a moderately complex reaching and grasping task. By using new variants of well-established techniques to analyse neural population activity, the authors provide solid evidence that while the geometry of neural population activity changes between execution and observation, their dynamics are largely preserved. Although these findings are novel and robust, pending additional controls and analyses, the authors should further clarify the functional implications of their findings.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94165.3.sa1](https://doi.org/10.7554/eLife.94165.3.sa1)

The authors investigated the similarity (or lack thereof) of neural dynamics while monkeys reached to and manipulated one of 4 objects in each trial, compared to observing similar movements performed by experimenters. They focused on mirror neurons (MNs) and rather convincingly showed that MNs dynamics are dissimilar during executing vs. observing actions. The manuscript has improved quite significantly compared to the previous version and I congratulate the authors for that. However, there are still a few points I would like to raise that I think will improve the manuscript scientifically and make it more pleasant to read.

- I appreciate the nicely compiled literature review which provides the context for the manuscript.

- Message: The takeaway message of the paper is inconsistent and changes throughout the paper. To me, the main takeaway is that observation and execution subspaces progress during the trial (Fig 4), and that they are distinct processes and rather dissimilar, as stated in #440-441, #634-635, etc. But the title of the paper implies the opposite. Some of the interpretations of the results (e.g., Fig 8) also imply similarity of dynamics.

- Readability: I have many issues with the readability/organisation of the paper. Unfortunately, I still find the quality of data presentation low. Below I list a few points:

(1) In 5 sessions out of 9, there are fewer than 20 neurons categorised as AE. This means this population is under-sampled in the data which makes applying any neural population techniques questionable. Moreover, the relevance of the AE analysis is also sometimes unclear: In Fig 4, the AE-related panels are just referred to once in the paper. Yet AE results are presented right next to the main results throughout the paper.

(2) Figures are low resolution and pixelated. There are some faded horizontal and vertical lines in Fig1B that are barely visible. Moreover, it may be my personal preference, but I think Fig1 is more confusing than helpful. Although panel A shows some planes rotating, indicating time-varying dynamics, I couldn't understand what more panel B is trying to convey. The arrow of time is counterclockwise, but the planes progress clockwise (i > ii > iii). Similarly, panel C just seems to show some points being projected to orthogonal subspaces (even though later in the paper we'll see that observation and execution subspaces are not orthogonal), and the CCA subspace illustrated in the same high-d space, which mathematically may be inaccurate, as CCA projects the data to a new space.

In Fig 2A, the objects are too small and pixelated as well. I suggest an overhaul of the figures to make the paper more accessible.

(3) Clarity of the text: The manuscript text could be more concise, to the point, avoiding repetitions, self-consistent, and simply readable. To name a few issues: Single letter acronyms were used to refer to trial epochs (I/G/M/H). M alone has been re-defined 13 different times in the text as in: ...Movement (M)..., excluding every related figure. The acronym (I) refers to the instruction epoch, the high-d space in Fig 1, and panel I of some figures. The acronym MN for Mirror Neurons was defined 4 separate times in the text yet spelled out as Mirror Neuron more than 2 dozen times. CD is defined in the caption of Fig 3 and never used, despite condition-dependent being a common term in the text. Many sentences, e.g., "In contrast, throughout..." in #265-#269, and "To summarize,..." in #270-#275, are too long with difficult wording. To get the point from these sentences, I had to read them many times, and go back and forth between them and the figure. Rewriting such sentences makes the manuscript much more accessible.

- Figure 3: It appears that the condition independent signal has been calculated by subtracting the average of the 4 neural trajectories in Fig 3A, corresponding to different objects. Whereas #133 suggests that it should be calculated by subtracting the average firing rate of different conditions. Assuming I got the methods right, dynamics being "knotted" (#234) after removing the condition independent signal could be because they are similar, so subtracting the condition independent signal leaves us with the noise component. This matters for the manuscript especially since this is the reason for performing the more sensitive instantaneous subspaces.

- Decoding results: I appreciate that the authors improved the decoding results in this version of the manuscript. Now it is much more interesting. However oddly, it appears that only data from 1 monkey is shown. #370 says the results from the other 2 are similar. The decoding data from every monkey must be shown. If the results are similar, they must be at least in Supplements. Currently, only 1 session (out of 3) in the Observation condition seems to decode the object type. This effect, if consistent across animals and session, is very interesting on its own and challenges other claims in the paper.

- Figure8: I reiterate the issue #7 in my previous review. I appreciate the authors clearing some methods, but my concern persists. As per line #839, spiking activity has been smoothed with a 50ms kernel. Thus, unless trial data is concatenated, I suspect the 100ms window used for this analysis is too short (small sample size), thus the correlation values (CCs) might be spurious. References cited in this section use a smaller smoothing kernel (30ms) and a much longer window (~450ms).

Moreover, I don't know why the authors chose to show correlation values in 3D space! Values of Fig8C-red are impossible to know. Furthermore, the manuscript insists on CC values of the Hold period being high, which is probably correct. But I wonder why the focus on the Hold period? I think the most relevant epoch for analysing the MNs is the Movement where the actual action happens. Interestingly, in the movement epoch, the CC values are visibly low. The reason why Hold results are more important and why the CCs in Movement are so low should be clarified in the text. Especially, statements like that in #661 seem particularly unjustified.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94165.3.sa2](https://doi.org/10.7554/eLife.94165.3.sa2)

In their study, Zhao et al. investigated the population activity of mirror neurons (MNs) in the premotor cortex of monkeys either executing or observing a task consisting of reaching to, grasping, and manipulating various objects. The authors proposed an innovative method for analyzing the population activity of MNs during both execution and observation trials. This method enabled to isolate the condition dependent variance in neural data and to study its temporal evolution over the course of single trials. The method proposed by the authors consists of building a time series of "instantaneous" subspaces with single time step resolution, rather than a single subspace spanning the entire task duration. As these subspaces are computed on an instant time basis, projecting neural activity from a given task time into them results in latent trajectories that capture condition-dependent variance while minimizing the condition-independent one. Authors then analyzed the time evolution of these instantaneous subspaces and revealed that a progressive shift is present in subspaces of both execution and observation trials, with slower shifts during the grasping and manipulating phases compared to the initial preparation phase. Finally, they compared the instantaneous subspaces between execution and observation trials and observed that neural population activity did not traverse the same subspaces in these two conditions. However, they showed that these distinct neural representations can be aligned with Canonical Correlation Analysis, indicating dynamic similarities of neural data when executing and observing the task. The authors speculated that such similarities might facilitate the nervous system's ability to recognize actions performed by oneself or another individual.

Unlike other areas of the brain, the analysis of neural population dynamics of premotor cortex MNs is not well established. Furthermore, analyzing population activity recorded during non-trivial motor actions, distinct from the commonly used reaching tasks, serves as a valuable contribution to computational neuroscience. This study holds particular significance as it bridges both domains, shedding light on the temporal evolution of the shift in neural states when executing and observing actions. The results are moderately robust, and the proposed analytical method could potentially be used in other neuroscience contexts.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94165.3.sa3](https://doi.org/10.7554/eLife.94165.3.sa3)

Summary:

In this study, the authors explore the neural dynamics of mirror neurons in the premotor cortex, focusing on the relationship between neural activity during action execution and observation. The study presents a rich dataset from three monkeys, with recordings from two regions per monkey. The authors use a method to analyze instantaneous neural subspaces and track their temporal evolution. Consistent with prior literature, they report that execution and observation subspaces remain largely distinct throughout the trial. However, after applying canonical correlation analysis, they observe a notable alignment between execution and observation activities, suggesting the presence of shared neural codes. The study is well-designed, and the analyses are thoroughly documented, occasionally overly so in the main text. While most findings are compelling, I find the conclusions drawn from Figure 8 less convincing. Specifically, I am skeptical about the application of CCA in this context and the subsequent interpretations regarding execution-observation similarity, which is a central claim of the manuscript.

• The authors cite Safaie et al. 2023 as a precedent for applying CCA to align neural population dynamics. However, in that study, CCA was used to align neural dynamics across different animals, a justifiable approach given that neural trajectories exist in separate neural state spaces for each animal. Here, CCA is applied to align execution and observation activities within the same neural state space of the same MNs. I find this application of CCA less well-justified, as it may overestimate execution-observation similarity.

• The control conditions presented in Figures 8C and 8D are somewhat reassuring, as they show that the similarity introduced by CCA is not universally high. However, these controls appear to be limited to the Hold epoch. It remains unclear whether the same holds true for the Go and Movement epochs.

• In Figure 5, the authors display low-dimensional representations of four objects across task epochs during execution (A) and observation (B). The diagonals of the matrices reveal clear differences between execution and observation configurations across all four epochs. The authors suggest using CCA to align these configurations; however, this alignment seems to require time-specific application of CCA for each epoch (as demonstrated in Figure 8 for the Hold epoch). The need for time-specific adjustments likely depends on the fact that execution and observation subspaces are continuously shifting over time (as authors show in Figure 4), but this approach appears to be a strained attempt to demonstrate similarity between execution and observation codes.

• The authors themselves offer an alternative hypothesis (line 730): that "PM MN population activity during action observation, rather than representing movements made by another individual similar to one's own movements, instead may represent different movements one might execute oneself in response to those made by another individual". This interpretation appears more congruent with the data presented.

• In the end, I am left with a sense of ambiguity: which analysis should be considered more reliable, the negligible correspondence between execution and observation activity depicted in Figure 7, or the considerable similarity shown in Figure 8? The authors should address this apparent contradiction and provide a clearer discussion to reconcile these findings.

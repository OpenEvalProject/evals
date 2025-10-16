# Peer review - Round 1

Editors:
- Emery N Brown, Massachusetts Institute of Technology , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09148.026](https://doi.org/10.7554/eLife.09148.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Intraneural stimulation can restore discrimination of textural features by artificial fingertips in humans" for peer review at eLife. Your submission has been favorably evaluated by Timothy Behrens (Senior editor), a Reviewing editor, and two reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper reports further on the very good pioneering work by these authors (previously reported) regarding the sensory/tactile input into the peripheral nerve. This paper extends the previous work, with some different aspects, although there is also a considerable overlap (which must be explained). Specifically, the authors study the use of NMT and TIME, in volunteer studies, in the study of a transradial amputee and in a simulation investigation as a way to restore tactile sensation.

The main result of neuromorphic stimulation, and neural response are interesting first presentations.

The strength of the paper is the very detailed experimentation, involving microneurography and the sensory input provided in an amputee. These experiments are aided by giving a biomimetic or neuromorphic input. Further, modeling shows how microneurography and TIM electrodes work comparably. This type of modeling coupled to experiments shows that this paper represents thorough research. The cortical response further validates that sensory perception is observed – this is quite interesting and novel as well. Overall, the work has enormous promise for establishing a paradigm for restoring tactile sensation to patients with limb injuries.

Essential revisions:

First, and most importantly, previous work by Raspopovic, more or less lays out the tactile stimulation. Also, the authors have published their sensors work. The new aspect seems to be the biologically plausible model. But the model selected – Izh ikevich is not a biological model of receptors – does not produce receptor-spiking activity and no transduction is built in.

In the subheading “Mechano-neuro-transduction (MNT) process”, sensor to spike output from Izhikevich is not an ideal receptor to neural activity transformation. The authors should point out this simplification – actually a limitation. The periodic rate output is also a significant simplification. The model produces bursts vs single spikes, but it's not clear it is biomimetic. This interpretation also needs some caution.

Second, the paper does not clearly and cleanly present what is novel here – and differentiate from many prior papers by the authors. What is novel – the stimulus pattern? The computational model? Comparison with 4 normal, amputee? Distinguish from the prior work by the same group. Please emphasize this point in your response letter and revised manuscript. The question of novelty will be critical in making a final decision on the publication of this work.

Third, the work presents tactile encoding – in particular coarse + geometric -> shape sensing. This is not clear. Is it only the artifact of their stimulus (grating) or is this the result of perception by the subjects – having tested many stimuli. i.e. is the perceptual output of the given microneurographic access to nerves and penetrating electrodes' access to the fascicles? If so, how specific and representative is it?

Fourth, the statistical analysis of the data should be improved. The text and Figure 1 discuss the results of the study in terms of the overall success rate. Figure 3 shows the breakdown of the responses by subject. There is a conspicuous lack of analysis of the data. The data should be analyzed not by lumping together all of the subjects and reporting an aggregate successful discrimination rate, but rather by individual subject as a function of stimulus type. The coarser the stimulus, the greater the discriminatory power and the weaker the stimulus the less the discriminatory power. There should be an analysis showing that the performance by individual is greater than what would be expected by chance, where chance here is 0.33. If there is an approximate monotone relation among the stimuli then a logistic regression analysis could be performed. The analysis should be conducted using confidence intervals or Bayesian methods and not just simply by reporting p-values. An advantage of a Bayesian hierarchical analysis or a random effects model across subjects is that they provide a formal way of pooling information across subjects. The latter is crucial for this problem because the authors which to establish that they have been able to provide neuromorphically tactile sensation. This statement should be made with an assessment of the accuracy of the discriminatory power of the MNT technique for each subject as a function of stimulus type. It is likely that the results will reveal that more trials will be required to show that there is truly discriminatory capability.

The authors state that they observed no difference in the natural EEG activity and evoked stimulation in source topography, response timing and clustering. How were these assessments made? They involve negative results and require a power analysis to establish their validity.

Although the data are more compelling for the TIME technique applied to the transradial amputee patient, a similar analysis should be performed for these data as well.

The authors wish to establish from their simulation analyses that the response patterns under MNT and TIME are similar if not effectively the same. It is unclear where the uncertainty comes from in these analyses since they are simulation models. Therefore how can statistical assessments of uncertainty and formal statistical inferences be made? Moreover, the authors wish to infer that the stimulation responses of the two modalities do not differ. They report a p-value without a specific statement about the statistical test being used in the analysis. Because the authors wish to establish a negative result of no difference between the two stimulations modalities, they should report a power analysis stating what types and magnitudes of differences their investigations were calibrated to detect.

The authors do not have to develop an ancillary classifier model to understand the performance characteristics of the MNT and the TIME paradigms. If they build statistical models to analyze the data from the subjects that include covariates that has IBI they will get their answer with the same model being used to analyze the data. This approach would obviate the current analyses which lead to multiple comparisons corrections.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Intraneural stimulation can restore discrimination of textural features by artificial fingertips in humans" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor), a Reviewing editor, and one reviewer. The manuscript has been improved but there are a few remaining issues that need to be addressed before acceptance, as described below.

General Comments:

This paper has been revised, and more importantly, careful and thoughtful rebuttal to all the questions has been provided. Supplementary figures and additional statistical analysis are also appreciated. Overall, the paper is acceptable. The authors should note a few salient points and revise their paper accordingly (no further review is needed).

This is an outstanding piece of work. The paper has many novel aspects, now better clarified as requested, to point out the texture discrimination capability in humans, different stimuli and temporal coding, comparison with needle vs intrafascicular, etc. The cortical, neural topographic map, and source localization strengthen the paper. The claim about neuromorphic/Izhikevich is now moderated, although the authors still argue that this is representation of tactile receptors, bur arguably this is still a significant approximation based on the Izhikevich model.

The paper's distinction from the previous, Raspopovic paper is now made and is acceptable. The comments made concerning this, from texture to encoding model, are acceptable.

The novelty aspect has been responded to: a) Texture discrimination (but not "restoration" – see below);

b) Hybrid FEM model is very useful and demonstrates TIME's utility and various fiber and recruiting; c) Perceptual studies, both psychophysical and cortical, strengthen the paper.

Suggested Revisions:

1) The claim in the Abstract is still too broad: "Intraneural MNT-based stimulation restored discrimination of textural features, thus enhancing the user's tactile capabilities." The word "restore" is too strong. It implies permanent restoration/recovery. Here a texture perception has been mimicked, and performance has not been "enhanced."

2) Paragraph two, subheading “Analysis of neural coding strategies”: This information pertains to Figure 10 (e). The message that the rate (in e, worse) vs temporal code (in d, good) is getting lost in this paragraph. This is an important observation and clarification would help. The figure caption could be more explanatory too.

3) Paragraph two, subheading “Hybrid electrical-biophysical model of the median nerve for the comparison between microstimulation needle and implanted TIME”: As the fiber organization within different fascicles in the nerve is unknown, we assumed that fibers within the fascicles belong to same functionality.

Please clarify how nociceptive fibers were separated from sensory (e.g. see the comment pertaining to the model).Indeed, this issue or not being able to separate different fiber types is quite critical and must be marked as a limitation.

4) Figure 2: Traces and colors are not well explained.

5) Figure 6 caption: The X marker represents the targeted fascicle where the fiber activation per 9 different populations was calculated. What does this mean (what populations?) for different locations of microneedle and TIME? This procedure is carried out analogously for medium and small fascicles, confirming results. Please could you also clarify the procedure.

6) Figure 8: outcomes. Color-coding is not explained

7) Figure 10: This figure, slightly modified to clarify rate vs temporal, would be much clearer (and certainly this result is important).

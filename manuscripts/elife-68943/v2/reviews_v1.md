# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68943.sa1](https://doi.org/10.7554/eLife.68943.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study combines a novel behavioral task, reinforcement learning modeling, functional imaging, and neurofeedback to show that learning to focus on what information is important for predicting choice outcomes (i.e., "abstraction") is guided by value signals. Because "abstraction" is a key process underlying flexible behavior, understanding its neural and computational basis is of major importance for cognitive neuroscience.

Decision letter after peer review:

Thank you for submitting your article "Value signals guide abstraction during learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alireza Soltani (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All three reviewers agreed that your study is well-conducted and the results convincing. However, they also had specific questions and suggestions for improvement. Below is a list of 'essential' comments that we would expect you to address in a revised version of your manuscript. The reviewers also made additional comments in the individual critiques, which we would encourage you to consider when preparing your revision.

1. There were several questions about the modeling. Please add a formal model comparison (accounting for model complexity) and show how much the mixture of expert RL model improves the fit over purely abstract and/or feature RL models. In addition, please show the responsibility values for the mixture model. This information, in addition to 'mean expected value', is needed to draw conclusions on the importance of feature and abstract RL models.

2. Please add an analysis of the behavior of excluded subjects. Do they adopt a different strategy and that is why they could not learn fast/accurately enough?

3. Does VC-vmPFC coupling predict the abstraction level? This connection seems to be as important to the authors' claims as the discussed relationship between VC-vmPFC coupling and learning speed (Figure 4C).

4. Please discuss issues around efficiency and plausibility that result from running 4 models simultaneously. That is, would it not be better if the brain only implemented the most complex algorithm instead of this algorithm in addition to the 3 simpler models?

5. Could it be that participants are simply better (more correct choices) in the abstract blocks (which presumably are also the later blocks)? If so, what does that mean for the value contrast in vmPFC? DO they reflect performance or strategy?

6. Please plot performance separately for CO, CD and OD blocks as well as for 2x2 vs 3x1 blocks.

7. Please clarify how the variance over RPEs (v) was calculated.

8. Was the cross-validation done between runs? If not, if should be done between runs, if possible.

9. The specific difference between relevant and irrelevant features seems important. Please add Figure S6 into the main manuscript.

10. Please add the results of the neurofeedback experiment. Were participants successful at increasing the size of the disc? Was there a correlation between this success and subsequent performance on the association paradigm? Full results can be provided in the supplements but should be referenced in the main text.

Reviewer #1:

Overall, the question studied in this work is timely, interesting and important. More specifically, although previous modeling studies have been focused on explaining how humans and other animals can learn informative abstract representations at the behavioral level, the underlying neural mechanisms remained poorly understood. Cortese and colleagues performed modeling analyses using a mixture of experts RL that consist of abstract and feature RL models as well as behavioral analyses (analyses of choice in a learning task) to demonstrate that performance of human subjects in a multi-dimensional learning task depends on their adopted level of abstraction. Supporting their modeling and behavioral analyses, authors analyzed fMRI data to demonstrate that the connections between ventromedial prefrontal cortex (vmPFC), the brain area encoding value signals, and visual cortex (VC) can predict subjects' learning speed, which is an indicator for adoption of abstract representations. Lastly, to demonstrate the causal relationship between VC and adoption of abstract representations, authors used a multivoxel neurofeedback procedure and showed that artificially adding value to features in VC results in an increase in adoption of abstract representations.

Although provided analyses are thorough and results are convincing, further quantitative analyses could be included to strengthen the main claims of the study. More specifically, it is helpful to show that results from fitting the mixture of expert approach is fully consistent with analyses using purely Abstract and/or Feature RL models. Additionally, an analysis of excluded subjects' behavior is missing. This is important, because failure in performing the task could indicate alternative (but unsuccessful) representations adopted by some subjects.

Comments for the authors:

(1.1) Page 6-8 and Figure 2: I could have missed this, but authors don't seem to provide any formal comparison between the goodness-of-fit using the mixture of expert RL model and pure Feature RL or Abstract RL models. For example, a simple Abstract RL model with only the informative features could capture behavior of certain subjects. I asked this because, the mixture of expert RL model contains more parameters than the Feature and Abstract RL models. I wonder when accounting for the extra parameters, would the mixture of expert RL model still provide a better fit? Please clarify.

(1.2) Related to the previous point, if the mixture of expert RL model provides a better fit, how much of the captured variance is related to the Feature RL vs Abstract RL experts (e.g. Figure 3F, G)? Perhaps this could be answered by examining the weight assigned to each type of RL in this model (λ values).

(1.3) Authors don't show the values of responsibility signals in the mixture of expert model. This information, in addition to 'mean expected value', is needed to draw conclusions on the importance of Feature and Abstract RL models.

2) I feel that the decoding analysis can be further improved. For example, do authors see any changes happen as a result of experience in the task? Also, a relevant reference is a study by Oemisch et al., Nat. Comm 2019, in which the prevalence of feature encoding neurons is examined.

3) How did the excluded subjects perform the task? Do they adopt a different strategy and that is why they could not learn fast/accurately enough? For example, did they learn about the value of different features and combine these values to make decisions (as in feature-based RL in Farashahi et al., 2017 or Farashahi et al., 2020, which is different from Feature RL and closer to Abstract RL)? Please comment.

4) Does VC-vmPFC coupling predict the abstraction level? This connection seems to be as important to authors' claims as the discussed relationship between VC-vmPFC coupling and learning speed (Figure 4C).

Reviewer #2:

Cortese and colleagues report two experiments in which human subjects made choices based on cues that had three distinct visual features. Only two of the three visual features were needed to make a correct choice. Hence participants could safely ignore one feature and learn based only on the two relevant features (a process the authors call abstraction). The authors modelled how behaviour and ventromedial prefrontal cortex activity shifted from processing all features to only the two relevant features and sought to elucidate the role of feature valuation in this process. In a second experiment, the authors used a real-time neurofeedback approach to tag visual representations of features and showed how this feature valuation process shapes the feature selection described in Experiment 1.

Past research has investigated the process by which humans and other animals learn to attend relevant features during reinforcement learning (e.g., Niv et al., 2015; Leong et al., 2017). These studies have outlined how reward shapes which features we pay attention to, and how attention shapes how we process reward. While a true account of how the process of "abstraction" might occur is still outstanding in my opinion (see below), this study adds some important insights about this process. A main point is that the authors show changing representations of features directly in vmPFC, which co-occur and interact with values. They also provide insight into the unique roles vmPFC and the hippocampus might have in this process, and how vmPFC value signals interact with sensory areas.

One particularly interesting aspect is this study is the use of neurofeedback to achieve reward-tagging of visual representations. This approach is noteworthy as it does not require to pair reward with the visual features themselves, but rather with the occurrence of neural representations that reflect said features. The behavioural effects of this manipulation on later learning were impressively strong: if the task required to attend features that were tagged with reward, behaviour was guided more strongly by appropriate selective learning; if the task required to ignore the features that were previously tagged with reward, the learning process was unchanged. This suggests that the process of selecting relevant features during learning interacts with a neural mechanism that tracks the values associated with these features. This conclusion is also supported by the fact that the same brain area that tracked the expected values of the stimuli during the task, vmPFC, was modulated by participants' level of feature selection, i.e. abstraction.

One weakness of this study is that the mechanism of abstraction remains unclear. The authors use a mixture of experts architecture of 4 different RL models: one RL model that tries to learn the appropriate action as a function of all visual features of the cues, and 3 models that try to learn based on the possible subsets of only two features.

I have some concerns about this approach. One concern is that the modelling presumes that participants concurrently run all 4 RL models, and continuously decide which one is best. The whole purpose of using a lower dimensional model is that it is more efficient. Permanently using 4 models, including the highest dimensional one, seems to defy the purpose of why the search for a best model was initiated in the first place. Arguably, such a scheme would also not necessarily predict that vmPFC should come to selectively represent only the most relevant features, since the model that requires processing all features needs to be kept up to date. It also does not shed light on how participants could ever truly stop to pay attention to some features, as feature selection is only done by weighting the model with the lowest prediction errors relative to the variance most strongly in the action selection process. In other words: I am unsure if the manuscript presents a reasonable account how representations become transformed. Other models, which do not suffer from these shortcomings, such as a function approximation model, might have added important insights to this study. Ideally, the presented model could also explain another interesting observation made by the authors: that performance improves over blocks, even though the relevant features change. This probably reflects that participants might have learned something more global about the dimensionality of the relevant space, but such a learning process is not accounted for by the authors. On the positive side, while such a concurrent training of 4 models seems computationally inefficient, it is at least data efficient, as each experience is used to update all models at once. And, the mixture of experts approach may be considered a tool to investigate feature selection, rather than a cognitive model. This should be clarified in the manuscript.

Another weakness of the manuscript in my opinion is that the valuation process targeted in the neurofeedback experiment presupposes that visual features are predictive of reward. One important aspect of abstraction, however, is that they may not be, as the same feature could lead to different outcomes, for instance based on unobservable context.

Comments for the authors:

– It would be great to try to model how longer-term knowledge about rewarding features and dimensionality of the task influence performance. How does the change over blocks occur? How do biases, as introduced through the neurofeedback procedure, influence model selection in the mixture of experts approach?

– Figure 5: Could it be that participants are simply better (more correct choices) in the abstract blocks (which presumably are also the later blocks)? If so, wouldn't that mean that the contrast high-low value in vmPFC will necessarily be higher for abstract blocks, but it could reflect performance rather than strategy?

– It would be interesting to see performance separately for CO, CD and OD blocks as well as for 2x2 vs 3x1 blocks. Is there a difference between 2x2 vs 3x1 blocks?

– Please consider avoiding the word "predict" when reporting a regression analyses or other types of non-causal effects.

– I did not follow how the variance over RPEs (v) is calculated. It would be important to clarify that in the manuscript, and indicate how it changes as learning progresses.

Does a small variance imply that all models have similar RPEs? If so, I am not sure the statement that it is related to sharper model selection is the only way to view it. It seems it could also be related to more model similarity.

– Isn't the fact that the relevant AbRL has higher values and learns faster trivial, given the design of the task? Would there have been any possibility that these results would not have come out? If not, I believe all p values should be removed.

– It would be great to add the results from Figure S6 into the main manuscript. The specific different between relevant and irrelevant features seems important

– Decoding: was the cross validation done between runs? If not, if should be done between runs if possible

– Neurofeedback: can you provide more information about how good participants were, and how long the neurofeedback effect was presented in the later task blocks (did it diminish over time?).

Reviewer #3:

The authors of this study aimed to demonstrate that abstract representations occur during the course of learning and clarify the role of the vmPFC in this process. In a novel association learning paradigm it was shown that participants used abstract representations more as the experiment went on, and that these representations resulted in enhanced performance and confidence. Using decoded neurofeedback, (implicit) attention to certain features was reinforced monetarily and this led to these features being used more during the association task. They conclude that top down control (vmPFC control of sensory cortices) guides the use of abstract representations.

The strengths of this paper include an objective, model based assessment of reinforcement learning, a strong and simple experimental paradigm incorporating variable stopping criteria, and the incorporation of decoded neurofeedback to determine if these representations could be covertly reinforced and affect behavior.

The weaknesses include a small sample, the lack of subjective evaluation of strategies/learning, and the omission of neurofeedback learning results.

Overall the authors achieved their aims and the data supports their conclusions.

This work will be of significance to computational psychologists, those who study abstraction and decision making, and those interested in the role of the vmPFC. One exciting implication of this work is that the use of certain features can be reinforced via decoded neurofeedback.

Comments for the authors:

I am not an expert in computational methods, therefore my comments are largely restricted to the neurofeedback study. The neurofeedback task is well designed and the use of relevant and irrelevant features is a nice control condition. That the effects were only observed for relevant blocks and the finding of increased abstraction from the late blocks of the main experiment strengthens their conclusions regarding causality.

While this is not the main focus of the manuscript, a supplement should contain the results of the neurofeedback experiment. Were participants successful at increasing the size of the disc? Was there a correlation between this success and subsequent performance on the association paradigm?

6s of modulation seems short for neurofeedback studies, please justify this short modulation time.

Finally, I am curious as to whether subjects were interviewed regarding the strategies they were using during the association paradigm. Were they aware they were using abstraction?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Value signals guide abstraction during learning" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Please revise your paper such that a casual reader will not erroneously take away that the MoE model presents a solid account of the data. Right now, the MoE is still mentioned in the abstract and also presented prominently in one of the main figures. You can leave the model in the manuscript if you want, but please further tone down any claims related to it.

2. It would be important to mention that some of the excluded subjects had good overall performance and the distribution of strategies was different among them.

Reviewer #1:

Authors have adequately and thoroughly addressed my concerns and questions. The only remaining concern I have is related to point # 1. Based on the presented results, it seems that MoE model does not provide the best fit of data. However, authors clearly mention and discuss this limitation in the revised manuscript. I have no further comments or concerns.

Reviewer #2:

I thank the authors for their thorough response to our previous concerns. I have two main concerns left:

1. The model comparison seems to refute the MoE model. At the same time, it seems clear that neither the FeRL nor AbRL model alone can truly capture participants behavior, since participants switch from one model to the other during the course of behavior. I think this should be made very clear in the paper, and I wonder how useful including the MoE model is.

My main reason is as follows: the core benefit of the MoE model, its ability to flexibly mix the two strategies, is seemingly not implemented in a way that reflects participants behavior. Would there be any way to improve the MoE models flexibility? The fact that it provides a "proof of concept that an algorithmic solution to arbitrate between representations / strategies exists" alone does not convince me, since the arbitration itself seems to not capture behavior and the pure existence of some algorithm is hardly surprising. In addition, there are the concerns about how realistic the MoE model is, which were raised under point 4.

I am also wondering whether the bad fit of the MoE model reflects how the fits were calculated: within each block, and then averaged (if I understood correctly)? Does that mean there was a new set of parameters per block? Have the authors tried to fit over the entirety of the experiment, using one set of parameters?

Relatedly, I believe that the change between strategies over time should be presented in one of the main figures, as this is an important point (e.g. by putting the rightmost graph from the Figure shown in the point by point response in the main paper).

2. I am also not fully convinced by the explanations about exclusions. The fact that the excluded subjects showed a different distribution of strategies should not serve as a reason for exclusion, since the purpose of the paper is to elucidate, in an unbiased manner, the distribution as it exists in the general population. The reported accuracy also does not seem very low for some participants. To me it seems that including the overall high performing subjects (with e.g. avg % correct > 70%) would provide a more unbiased sample.

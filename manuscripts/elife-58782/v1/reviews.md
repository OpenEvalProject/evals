# Peer review - Round 1

Editors:
- Anna Wang Roe, Zhejiang University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58782.sa1](https://doi.org/10.7554/eLife.58782.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is an important paper for understanding functional contribution of prefrontal (PFC) and parietal areas (LIP and MIP) to sequential decision making. Using a match/non-match (M/NM) decision paradigm in a delayed match-to-category task, the authors focused on the activity during the 250 msec period following the test stimulus presentation. The results reveal that match-preferred PFC neurons exhibited integration of seen and remembered stimuli, indicating that PFC contributes to match/non-match decision process by nonlinear neural integration. Match-preferred LIP neurons contributed primarily to sensory evaluation, while MIP neurons to motor functions such as planning or initiating lever release movements. One of the novelties is the recordings are obtained from three different brain areas from the same monkeys, providing opportunity to assess performance of three areas directly in the same task periods. A second novelty is use of the RNN recurrent neural network model to demonstrate that these outcomes are predicted and to provide a broader context regarding the role of nonlinear units in sequential decision making. The results are broadly consistent with and add to the previous literature.

Decision letter after peer review:

Thank you for submitting your article "Distributed functions of prefrontal and parietal cortices during sequential categorical decisions" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Klaus Wimmer (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This is an interesting paper that addresses the differential roles of PFC, LIP, and MIP in a delayed match-to-category task (selectivity for M vs NM in 3 member categories). This task has been studied extensively in the Freedman lab and several aspects of this dataset have been published previously. Here, the authors focus on the phase of the task from the onset of the second stimulus (test) until the response (button release) approx. 250 ms later. This phase is interesting because it is when the monkeys have to make the decision whether the two stimuli belong to the same or to a different category. The authors find that match-preferred PFC neurons show significantly shorter latency in M/NM selectivity than LIP and MIP and integrate information of both sample and test categories, indicating that PFC contributes to the match/non-match decision process by nonlinear neural integration. Match-preferred LIP neurons were involved in a comparison of sample and test categories, indicating greater role in sensory evaluation, while MIP neurons mainly contribute to motor planning or initiating lever release movements. The results add to the previous literature (e.g. from Romo and Pasternak labs, (Siegel et al. 2015)) and are broadly consistent with those. Overall, this is an interesting topic and recordings in three different brain areas (from the same monkeys) are well suited to address open questions. However, what is new here, as presented, is not sufficiently novel. To bring out the novelty, the concerns, as detailed below, center on improving analyses to better highlight (1) how linear and nonlinear integration in the three brain areas contribute to M/NM decision-making in this task and (2) what kind of functional interactions between these areas leads to a correct M/NM decision. In addition, the use of recurrent neural networks is commended, but (3) needs to go beyond what already has previously been demonstrated; there is opportunity here to provide deeper insight. (4) Substantial re-organization of the manuscript and shortening of introduction and discussion would help improve clarity. We think that these revisions and additional analyses should elucidate the circuits underlying these multi-areal interactions more clearly.

Essential revisions:

Highlighting what is new:

(1) As the differential contribution of information processing of PFC, LIP, MIP has been largely established, the authors must go beyond demonstrating "the relative functions of LIP, PFC, and MIP in sensory, cognitive, and motor functions". Specifically, how do these three brain areas contribute to M/NM decision-making in the DMC task (e.g., linear or non-liner integration, how LIN, NIN, and PN contribute to decision)? and what kind of functional interactions among these brain areas lead to a correct M/NM decision? Please make novelty of this study explicit in abstract, introduction, and discussion.

Data analysis to better isolate roles of linear and non-linear integrating neurons:

(2) Relationship between M/NM effects (match/non-match) and nonlinear integrating neurons (NIN). I was confused to learn first about M/NM neurons (Figure 2) when later – by making a finer distinction – it turns out that many neurons actually respond selectively to only one particular condition (NIN neurons; Figure 7A-C). One key result of Figure 7 is that the nonlinear neurons encode the most information about M/NM. This seems counter-intuitive because a neuron such as the one shown in Figure 7B signals "non-match" only if the test stimulus is from cat 2 and its N/MN effect can't therefore be very high. Some clarifying analysis about the relationship of non-linearity (nonlinearity index, Figure 6B) and match/non-match signals (Figure 2) should be added. At the very least this could be a neuron-by-neuron scatterplot of the non-linearity index vs match/non-match signal in PFC and LIP.

(3) Related with the previous comment, the analyses of mixed selectivity are somewhat convoluted. I would suggest a more standard analysis: as done in (Lindsay et al. 2017), one could model mixed neural responses as a combination of factors (stimuli, decision, etc) and their interaction. Statistics done on the interaction term directly relate to non-linear mixed selectivity would be easier to interpret.

Modelling:

(4) RNNs: The paper shows that the activity in the trained neural network model shares some features with the experimental data but it does not provide a deeper insight into (i) how the M/NM signals are computed in PFC (presumably from NIN neurons in PFC); (ii) whether M/NM is computed in both areas or communicated from the PFC to the LIP module. Moreover, the authors claim that "we developed a novel approach to a multi-module RNN, in which the modularity and rules governing the connections between modules were inspired by neurobiological principles" but the same approach has already been used previously (Kleinman et al. 2019; Song et al. 2016) (Pinto et al. 2019). It has been shown in these previous papers that RNNs can successfully learn tasks under the constraints of a certain network topology. Thus, my question is what we can learn from the RNN here (beyond the proof of principle that the RNN can find a similar solution to the problem)? For example, can the trained RNN be used to generate some non-trivial predictions about the (feed-forward and feedback) interactions between LIP and PFC (see (Kleinman et al. 2019))? Relatedly, no justification is given why the third brain area studied experimentally (MIP) is not included in the model.

(5) Related to the previous comment: It seems that M/NM signals in the model emerge first in LIP (Figure 8C,D), in contrast to the exp. data, where they appear first in PFC. It would also be interesting to see if the model can account for other key features of the data, in particular whether the activity of NIN neurons in the model is predictive of error trials (as shown in Figure 7G for the experimental data).

Manuscript rewriting:

(6) Manuscript is rather descriptive and not well structured (for example, representation of the stimulus category is only addressed in Figure 5, after presenting M/NM selectivity). I think the paper would gain in readability by re-organizing it, by focusing on the key findings, and potentially by moving some of the less central figure panels and control or confirmatory analysis to the supplementary material (e.g. several single neuron examples as in Figure 7; similar results for FEV and decoding e.g. in Figure 4).

(7) Introduction and the discussion are lengthy. In particular, sections of "M/NM selectivity in PFC, LIP, and MIP" and "Comparing the roles of PFC, LIP, and MIP in M/NM decision" are lengthy. We suggest the author shorten and summarize these sections.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Distributed functions of prefrontal and parietal cortices during sequential categorical decisions" for further consideration by eLife. Your revised article has been reviewed by 2 peer reviewers and the evaluation has been overseen by Joshua Gold as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below: Two reviewers, one of whom was a reviewer on your previous submission, have provided feedback. It is clear that substantial work has been done to address the previous set of reviews. Both reviewers do appreciate the RNN approach. Still, they have questions regarding this model. The rationale and meaning of changes to the parameters of the simplified RNN module is not very clear. Without clarification, the choice of parameters appear arbitrary. Further detail is requested to better understand the assumptions and behavior of the model (e.g. how the loss function changes with training; the behavior of firing rates for individual hidden units in each module). Comparison of different modelling choices is requested.

Reviewer #1:

The authors have substantially improved the manuscript and they have addressed the issues raised in the first of round of reviews.

I still have some concerns about the RNN modeling approach. I agree that the new modeling results and the analyses of the model are more compelling, and that the model is overall more comparable to the empirical findings presented in the paper. What concerns me is what the authors summarize as follows in their rebuttal letter:

"we dramatically improved and simplified our multi-module RNN modeling approach, including many fewer recurrent units (100 now vs. 400 before) and imposing fewer constraints on connectivity – in particular, eliminating the restriction that units exposed to external inputs/outputs cannot project outside their own module"

What is the biological relevance of a RNN model in which the obtained results depend so dramatically on the number of neurons and on the imposed constraints? Or put another way: what is the justification for using only 10 inhibitory and 40 excitatory units in each of the 2 modules? I understand that these units are not meant to represent single neurons but small populations. The way that the results are presented in the paper suggests that the training was set up with some constraints, then 50 networks were trained and the 41 networks that learnt the task were analyzed. The provided statistics (line 415f) refer to this scenario. But this is not how this research was carried out. First, networks with 200 units were trained and the results were very different, but this is not mentioned anywhere. I think that this can be misleading because it seems that the obtained solution is a robust finding whereas in reality it seems largely to depend on rather arbitrary modeling choices (100 vs 200 units for example). I think that at the very least the old results need to be presented in the paper as well, together with a discussion of the modeling choices and parameters that yield one solution (as in the first submission) or the other solution (as in the second submission).

Reviewer #3:

In the current study, Zhou et al., analyzed data based on two previously published paper from the same lab. Although the dataset is not new, the authors have focused on a new question by analyzing choice related signals in the test period, and by comparing among the three areas simultaneously including PFC, LIP and MIP. The authors found that although sensory-categorization signals were strongest and most salient in LIP, the choice related signals are strongest and arose earliest in PFC. By contrast, MIP shows more motor related activity. Importantly, the authors found that there was a group of PFC neurons that nonlinearly integrated signals of remembered sample and visible test stimuli. Finally the authors constructed a RNN with structure based on their neurophysiological findings. Based on this, they were able to show the network hidden units produced similar properties as in the real data. Importantly, by manipulating the units and connections in this network, the authors were able to show the nonlinear PFC-like neurons really play an important causal role in perceptual categorization task. These results are interesting, and particularly with the aid of the RNN, we may get more insights into the neural circuit mechanism mediating perceptual decision making.

1) How is the activity from the remembered stimuli, as well as from the test stimuli extracted from the test 1 period, since the test stimuli were superimposed-shown during that time, and the responses observed during that period should actually be the sum of the two signals? I am not clear about this, and cannot find this clearly in the text.

2) The causal manipulation of RNN demonstrates that the nonlinear PFC is important, but as shown in the neurophysiology, the nonlinear PFC neurons tend to have stronger sensory categorization signals, as they tend to receive stronger connections from LIP neurons. So it is not the "nonlinear" that matters, but the strong sensory categorization signal (potentially from LIP) matters, correct?

3) The description of the RNN is not clear. For example, what is the task of the network (successfully categorize stimuli)? What is its loss function?

4) If all the units in the RNN are excitatory, rather than 10-20% of them are set to be inhibitory, will the model produce similar results and conclusions? The motivation of these settings are not clearly demonstrated in the text.

5) The causal manipulation of RNN demonstrates that the nonlinear PFC is important, but what about LIP? Although overall LIP shows relatively smaller proportion of nonlinear neurons compared to PFC, they still show nonlinear effects. If inactivating these LIP neurons, what would happen? Plus, the authors have emphasized PFC too much by "suppressing" LIP.

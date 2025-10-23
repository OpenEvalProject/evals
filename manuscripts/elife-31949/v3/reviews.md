# Peer review - Round 1

Editors:
- Tor Wager, 1Institute of Cognitive Science, University of Colorado Boulder United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31949.028](https://doi.org/10.7554/eLife.31949.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The Control of Tonic Pain by Active Relief Learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Zhang and colleagues investigate how different aspects of relief learning during tonic pain stimulation relate to pain perception and what the neuronal correlates of these processes are. They report that uncertainty/attention inferred from a formal model parameter called 'associability' is correlated to reductions in pain perception. This is an intriguing and novel take on the links between learning processes and pain regulation. The study addresses an important and timely question that will be of high interest to readers in various research fields, including pain, learning theory, decision-making, and motivation. They identify neural correlates of prediction error and associability and show that these parameters map onto responses in striatum and pgACC in two separate imaging studies of instrumental relief learning during tonic heat pain (effects during Pavlovian relief learning are less conclusive). The paper is well-written, analyses are appropriate, and the work builds on previous studies of tonic pain and pain-related learning from this group, as well as a growing body of work integrating pain and associative learning.

Essential revisions:

All reviewers noted that the modeling was sophisticated but not particularly accessible to a non-modeling audience. Overall, the manuscript is densely written and relies a lot on technical terms. Unpacking some of the ideas and concepts in the Introduction and Results section would help to make the manuscript more accessible to a broader audience. Given that this is a general interest journal, I hope the following suggestions will make it easier to for a broader audience to extract conclusions. At the same time there are technical concerns that need to be addressed. These comments reflect input from all three reviewers – there are many points but some of them are convergent.

1) It isn't clear why the particular models tested were chosen and what adjudicating between them tells us, in practical terms. For example, what are the implications of a model with a fixed learning rate (TD) fitting better than a model with an adaptive learning rate (hybrid TD)? Also, as it seems a central goal to demonstrate that RL models have more explanatory power than simpler models, it would be helpful to be able to understand how well each model fit and what the incremental difference between them is. The latter might be accomplished by expanding on the description of exceedance probability in “subsection “Model fitting and comparison” and mentioning it in the Results (or figure captions?). Relatedly, the behavioral choice data in Experiments 1 and 2 are best explained by a temporal-difference (TD) model without an associability term. Are decisions and actions thus independent of the associability? Do participants learn, but do not act on that knowledge? What does that imply for the conclusions drawn here?

The authors fit models to individuals' behavior, then used mean parameters to generate regressors for neuroimaging data. Individuals seem quite variable in terms of fitted parameters, particularly in Experiment 2, and this variability in learning and performance might contribute to inconsistencies in the neural data. Why did the authors not (1) use the individual model fits in the imaging analyses, (2) fit to the group, or (3) incorporate information about individual fits (e.g. learning rates in the TD model) at the subject level in analyses?

Also, regarding the modeling efforts – How reliable are the model parameters and outcomes of the model comparisons, when only 16-18 SCR data points are used for fairly complex TD or Hybrid models for each session? Are the reported exceedance probabilities for the model comparisons 'protected exceedance probabilities' (Rigoux et al., 2014) that account for the possibility that models are equally (un)likely?

2) Associability is clearly a critical construct here, but it seems to arise operationally from the models but a little muddier at the level of theory. For example, would an associability account of relief learning differ from an attentional account? Associability and attention are discussed almost interchangeably. On a more practical level, simply stating the direction of associability (e.g. high associability = higher uncertainty) clearly would make correlations more immediately interpretable. Clarifying the relationship between these concepts early on and consistently using them throughout the manuscript will increase readability.

As a more general point relating to both of the preceding issues, I think some of the difficulties in interpreting results was due to the format whereby results are presented before methods. As an example, there was more description of associability in the discussion and methods, but it would have been helpful to have some information provided in the results, given that this is read first. Perhaps the authors could be mindful of this format and provide some explanation along with the results presented?

3) Other than the fact that a reinforcement learning paradigm fits putamen responses, do we have evidence that dorsal putamen responses are involved in a learning process? Is there any correspondence between dorsal putamen findings and behavioural findings?

4) The timing of pain and relief ratings wasn't very clear. Am I correct in inferring that both pain and relief ratings were collected at three time points in each session (near beginning, near middle, near end)? How many of each rating makes up the scores reported?

5) The important event for participants is the reduction of pain when the temperature is reduced. Since pain has a continuous intensity dimension and a reduction along this dimension is driving the learning process, I wonder whether the RL models could be extended to use a continuous outcome that might offer more information?

6) Given that correspondence between the two experiments is an important feature, a figure in which activations in one experiment are overlayed on the other (to judge spatial correspondence) would be helpful.

7) It isn't very clear how imaging data were corrected for multiple comparisons. Relatedly, in some cases, searches were restricted to a priori ROIs (e.g. pgACC, posterior insula, vlPFC), but isn't clear how these were defined (e.g. anatomically? Based on previous findings?) or whether data in these analyses was corrected across the mask of all ROIs. From the tables and Results section, I conclude that the authors use a mix of Cluster-extend thresholding and peak-voxel SVC correction. The authors should choose one method and use it consistently.

Furthermore, the authors use SVC correction based on coordinates from hand-selected previous studies or selectively use Experiment 1 coordinates for SVC correction of the amygdala results in Experiment 2. With the availability of comprehensive anatomical atlases, I urge the authors to apply masks based on anatomical atlases or independent functional localizers to correct for multiple comparisons.

8) Since the conclusions of this manuscript rely primarily on the model efforts, I think presenting about absolute model fits for choices and SCR data would help in evaluating the models. In addition, presenting information on SCR data quality will help to convince the reader about the conclusions. For example, skin conductance shows spontaneous, phasic responses during acute (10-20s) or tonic pain stimuli. To which degree are the responses modeled here locked to the cue- or outcome-events? Showing raw SCR traces and/or averaged evoked responses with predicted SCR responses would help here, e.g. using eLife's figure supplements.

9) Do changes in pain perception also correlate with pgACC activity when used as a regressor in subject-level models?

10) In the Discussion section, the authors argue that lack of controllability in Pavlovian paradigms renders uncertainty hyperalgesic instead of analgesic. However, pain ratings do not differ between instrumental and Pavlovian sessions in Experiment 1, as predicted by this reasoning.

11) In subsection “Ratings” the authors argue that placebo expectation theory predicts that larger prediction errors are correlated with pain reductions. Montgomery & Kirsch, (1997) and Locher et al., (2017) have shown that a plausible instruction regarding the placebo is needed for conditioned placebo analgesia. Participants in the present study weren't given any rationale for a cue being a placebo treatment. Hence, different processes might be involved here. In addition, this test relies on the correct estimation of the prediction error, which depends on the estimated value. The value will increase (i.e. encode more expectation for relief) over repeated trials that included a relief. When the expectation for relief and thus the prediction errors are maximal, participants have just experienced a series of relief trials and the surprise or associability/uncertainty to previous trials is also maximal.

12) In both studies, pain (and relief) ratings were collected "intermittently," yet the authors make strong assumptions about effects on relief/pain based on the correlations between ratings and the time-varying measures of associability or prediction error. The authors should present complete information about rating measurement for each experiment (e.g. number of ratings) and justify why they did not incorporate ratings at the same time scale of choice, stimulus display, and SCR measurement. To determine that ratings are preferentially related to associability and not prediction error, it seems that all quantities should be measured with the same number of observations. Furthermore, this would allow direct fits to ratings, which would be the best way to determine how these learning-related parameters modulate pain and relief. Finally, if I understand correctly, Experiment 2 included pain ratings before relief outcomes were delivered. These ratings are likely to be influenced by anticipation and uncertainty, but not by relief, whereas Experiment 1's ratings were measured after outcomes. Thus, the studies differ in terms of the construct that is captured by ratings. Since pain and relief are ultimately subjective, a more thorough consideration of the self-report measures is warranted.

13) Please also explain the negative coefficients in Figure 4E – participants experienced less pain with higher associability and with longer time since relief? This seems inconsistent with previous work on uncertainty, attention, and desire for relief which should enhance pain.

14) Skin conductance was found to be best fit by associability from the hybrid model. Can the authors rule out the possibility that this is only the case because both associability and skin conductance decrease over time? Other models included an effect of time/trial to account for such habituation. Are these findings artefactual, and might SCR track value or prediction error if habituation is modeled separately?

15) The study uses a mild tonic stimulus in healthy volunteers and measures behavioral correlates of intermittent relief. While the pgACC results are cool, I find it quite inappropriate to suggest that "the results highlight the pgACC as a target for therapeutic intervention […] by invasive excitatory deep brain stimulation."

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The Control of Tonic Pain by Active Relief Learning" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #1:

The authors have largely satisfied any concerns I had about the reliability of the findings. So, I would be comfortable publishing the paper in its current form.

That said, I concur that they haven't done as much as they might have to increase the paper's accessibility to a general audience. On re-reading the paper after the authors' responses, I think the easiest way to do this might be to do some additional revision to the introduction. The Introduction (particularly before the addition of the sections on associability and reward learning) does little to set up the actual experimental paradigms and modelling techniques used, such that one ends up trying to piece together the rationale for most of what was done while reading the methods and results. The methodology and modelling would have been far clearer to me had the authors been more explicit (as they were in their reply to reviewers) about the relevance of associability for illuminating the distinction between state and action learning and how doing so relates to the broader goal of understanding relief learning in the context of tonic pain.

So, in summary, the paper is publishable, but I do think the paper could be improved in terms of accessibility without a great deal of additional work.

Reviewer #2:

The authors have addressed all my comments and questions.

Reviewer #3:

For the most part, the authors have addressed all major concerns. I was particularly impressed that results and conclusions hold (1) whether parametric modulators are based on individual versus mean fits for Experiment 2 (although I think the authors should consider including these results in Supplementary figures), and (2) when consistently defined ROIs are employed (new Tables 6 and 7). The paper is also strengthened by the addition of information clarifying rating procedures and depicting skin conductance over time.

However, I feel that a few concerns remain, which I have delineated as minor concerns in the following section. In several places (e.g. the discussions of contingency awareness, modeling the time course of temperature changes, subjectivity of ratings), I felt that the authors only superficially engaged with reviewers' collective suggestions, and that overall accessibility of the work is still somewhat limited for non-expert audiences.

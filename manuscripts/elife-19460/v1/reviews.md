# Peer review - Round 1

Editors:
- Jack L Gallant, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19460.016](https://doi.org/10.7554/eLife.19460.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Divisive suppression explains high-precision firing and contrast adaptation in retinal ganglion cells" for consideration by eLife. Please accept our apologies for the long delay in returning these reviews to you. We had a difficult time finding qualified reviewers for your paper and then one of the initial reviewers had to bow out at a late date.

Your article has been reviewed by two peer reviewers. The process was overseen by a Reviewing Editor and by Timothy Behrens, the Senior Editor. Our decision was reached after consultation between the reviewers, the Reviewing Editor and the Senior Editor.

Based on these discussions and the individual reviews below, we regret to inform you that this submission will not be considered further for publication in eLife. However, the reviewers and Editors thought that your study was interesting and worthwhile, and after discussion amongst the Editors it was decided that we would be happy to consider a revised paper, which would be considered as a new submission. Based on extensive discussions with the reviewers, the Reviewing Editor believes that a resubmission would be considered if you were to revise the paper in one of three ways: (1) undertake pharmacological studies as suggested by one reviewer, and therefore try to tie the model more closely to specific neural mechanisms; (2) use a wider range of stimuli, such as stimuli that include naturalistic slow temporal fluctuations (e.g., 1/f), and then modify the model as necessary to account for a broader range of phenomena; (3) try to get a better sense of which elements of the model are critical under what situations, but testing an even wider range of competing models and model variants. We thank you for sending your work for review and we hope you will either revise this work and resubmit it, or barring that you will wish to submit to eLife again in the future.

Reviewer #1:

This paper studies the responses of mouse α retinal ganglion cells responding to flickering white noise at two different contrast, and fits the response with a computational model. The model is an abstract model consisting of two pathways, with one influencing the other, which is one of a general class of known models with multiple pathways followed by a nonlinear static (time-independent) interaction. It is shown that the model accurately captures the response and some properties of contrast adaptation. An argument is made why the model can be interpreted to show that inhibition underlies contrast adaptation. Other aspects of the model such as the source of precise firing are discussed. Currently the claim of the role of inhibition is not well supported, and the result that a more simple model of a known type fits the data for one type of ganglion cell is interesting, but mainly to the community of people that fit models of the retina.

Major points

1) A central claim of the paper is that the model indicates that adaptation comes from inhibitory suppression. This claim is in conflict with other studies, including one from the Demb lab (Brown & Masland, Manookin & Demb 2006). The current evidence for this claim is not sufficient, and a pharmacological experiment blocking inhibition has to be done for this claim to be supported. If it turns out that blocking inhibition abolishes adaptation and changes the response of the model in the expected way, then this should be the main focus of the paper, and the model should be used to support this main claim. In doing this experiment, the primary concern will be that without inhibition, the retina is put in a different state, where adaptation does not occur, even though inhibition is not really involved. For example, without inhibition, neurons will depolarizes and synapses may be depressed even at low contrast. So care must be taken to avoid this issue. In particular, the expectation is that the excitatory direction changes little, but the suppressive direction disappears. Because the low contrast is 10% (which is still fairly strong) it may be useful to use a lower contrast.

2) The authors interpret the 'suppressive' direction to mean inhibition, but the alternative interpretation that the authors wish to argue against is that feedback at excitatory synapses produces an apparent suppression when fit with the DivS model. It is quite suspicious that the suppressive direction (temporal filter) in Figure 2B looks exactly like a delayed version of the excitatory temporal filter. This seems to imply that the suppressive direction might indeed be from negative feedback – though admittedly such negative feedback could from synaptic depression or inhibition. The results presented are consistent with the current model of synaptic depression (not inhibition) underlying adaptation, except for Figure 4, which relies on a questionable assumption (discussed below). That's why the pharmacological test is critical.

3) As the sole support of the claim that the suppressive component of the model comes from inhibition, a spatial stimulus is used in Figure 4. This brings a new level of complexity is not properly addressed. When space is considered, we know that bipolar cells have a receptive field center and surround with different temporal filters. Bipolar cells form nonlinear subunits, each with a threshold (Schwartz et al., 2012 for mouse α cells). Each of these small subunits show local adaptation (Brown & Masland, 2001) and then there is global adaptation in the ganglion cell from spike generation (Zaghloul et al. 2005). The logic the authors use is the suppressive direction should be the same as the excitatory direction if inhibition is not involved. It is not clear whether this is true when the more complex system is considered. The 'excitatory' and 'suppressive' directions are just the two directions in stimulus space that influence the response, and the suppressive direction will be influenced by feedback at bipolar cell synapses and in the ganglion cells. The surround time course is more delayed, and may match the delayed suppression from negative feedback more closely. Thus it is not clear whether the simple DivS model will mix inputs in unexpected ways. The fact that the suppressive and excitatory directions are different is not conclusive without further consideration of the known sites of nonlinearities and adaptation.

4) Because the model has no slow dynamics, it cannot capture contrast adaptation that lasts over several seconds, which has been the sole subject of some studies of contrast adaptation (Manookin & Demb, 2006). The entire 20 s stretch of recording should be shown of the data, so it can be properly evaluated what aspects of the response cannot be fit by the model. Furthermore, the claims about the accuracy of the model should be qualified in terms of the aspects of adaptation that it does not capture.

5) Class of model. If in fact there are only two stimulus directions that are important as is claimed, than the DivS model is equivalent to a model that can be created using standard Spike-Triggered Covariance (STC) analysis (Fairhall et al., 2006), which can equivalently be done with continuous currents. So it should be pointed out that this model is not a new type of model, but an example of a known type of model. In (Fairhall, 2006) there are multiple types of ganglion cells reported with different types of responses in the two-D feature space, yet contrast adaptation is widespread among ganglion cells, so it is likely that the interpretations of the current paper won't apply generally. It is ok to study one type of cell, but the fact that the model presented is one of a known class of models should be made clear.

6) The LNK model is not convex, and more detail should be given as to how this was optimized. Were the methods of (Ozuysal & Baccus, 2012) used? For example, mean squared error was not used as an error metric. If the method of fitting was suboptimal, then the interpretation of the comparison between models is not clear. Also, more detail needs to be given for the spatial LNK model. Because there are two different spatial regions, each one should have independent adaptation, and each spatial region should have a center-surround linear receptive field. This would be a new type of model, so it's not clear whether this model can be properly optimized.

7) For the spiking DivS model, does the model really take the observed spike train as an input (not just as a constraint to fit data)? Shoudn't a model that takes the response as an input be able to produce the response? (It seems like cheating.) In fact, some studies that use the spike history in the way have shown that using the spike history is either the most important predictor of the response, or that the spike history alone can be used to predict the response (Kraus et al., 2015, Figure S4; Trucculo, et al., 2010). If this is really what was done, this approach differs from other models which use a spike-history term such as a generalized linear model (GLM) (Pillow et al., 2008) but that generate its own spikes rather than taking the actual response as an input. This needs to be made more clear, and also justified as to why this is useful. This approach may be useful for understanding the source of precision as the authors do, but it doesn't seem impressive that this model can fit the data if it really takes the actual response as an input.

8) Figure 6, it is not clear where the noise comes from in the model, as there is no noise source. Is it all from the spike-history term, i.e. the actual data? It's not clear how we can evaluate different models using this approach, because the noise is not appropriate for each model. A better approach would be to model noise sources and put them in each different model, like an LNP model.

Reviewer #2:

This paper shows how a novel model can predict the retinal ganglion cell responses to full field flicker at different contrasts. Standard approaches, like LN models, fail to generalize across contrasts, while this model does generalize with a single set of parameters to predict responses to high and low contrasts.

The key novelty of this model is to include both excitatory and inhibitory subunits, that are multiplied together to predict the ganglion cell membrane potential. Further non-linear processing allows to predict the spiking response. The model has been carefully fitted to both intracellular and extracellular recordings. The agreement between the model prediction and the data is impressive.

Overall this is a very nice work. Contrast adaptation is ubiquitous in the visual system. Such a model could have a broad impact on the field of sensory systems.

Major comment:

My only concern is about novelty: as noticed by the authors, another model, the LNK by Ozuysal and Baccus, has already shown its ability to predict ganglion cell responses at different contrasts. The performance of the current model is better than the LNK, but not by much for full field stimuli. The only stimulus where there is a significant difference, if I understood well, was the one composed of a center spot and an annulus stimulating the surround. There the model performed better, but the difference is rather small (around 7%).

The model is conceptually novel, but relatively similar to previous works by Sahani and colleagues.

So I think a more thorough comparison between the LNK model and this one would be welcomed. With such a small difference, one would like to be sure that the authors gave the LNK model its best chance of success. Here the methods do not include a text about how this model was fitted. More generally, more details would be welcomed about how the two models were fitted in the case of the compound stimulus (centered spot +annulus).

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Divisive suppression explains high-precision firing and contrast adaptation in retinal ganglion cells" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance. As you will see Reviewer 1 was very positive, but Reviewer 2 had several remaining concerns. In an extensive consultation session between both reviewers and the Reviewing Editor, it was decided that the best course of action would be for us to return this to you for further revision to meet the concerns of Reviewer 2.

1) The biggest remaining issue that must be addressed in revision concerns issue #1 raised by Reviewer #2, the use of raw data in prediction. This issue was also brought up in the initial reviews. All the discussants are concerned there is a serious danger of over-fitting here, and they did not consider the responses to the initial reviews on this matter to be sufficient. Reviewer 1 makes some good suggestions about how to deal with this issue, but you might also be able to approach it another way.

2) Please try to address the slow contrast adaptation issue as suggested by Reviewer 1. If it cannot be addressed then the manuscript should be revised to make it clear that this mechanism is not covered by the model.

3) Please respond to the dynamics/LNK issue with appropriate revisions (preferably including the requested comparisons).

4) The presentation regarding the Spike Triggered Covariance model and its relationship to the DivS model needs to be clarified.

5) Please revise the text concerning divisive suppression to address Reviewer #1's concerns.

As the discussants see it, you can meet these concerns in one of two ways:

Option 1: Revise and retract some of the claims so that the claims are more consistent with what is actually shown in the existing manuscript.

Option 2: Run the model again, but using a spike history filter generated from synthetic spikes rather than using the raw data in the model prediction as was done in the most recent revision.

The discussants agreed that either of these two options would be fine and that they would leave it up to you to decide which course of action you would like to pursue.

In either case we appreciate your submitting this excellent manuscript to eLife and we hope that these remaining revisions will not be too onerous for you to accomplish quickly.

Reviewer #1:

As far as I am concerned the authors replied well to the points I raised. It is clear that this study shows a novel model that can predict better ganglion cells responses. The quantitative improvement compared to previous approaches can be small, but the framework seems a bit more general. It is also stated clearly that this model by itself does not lead to novel insights about the mechanisms behind contrast adaptation as different mechanisms can explain these results.

Reviewer #2:

The paper has improved from the previous version, but a number of issues remain that were raised in the first review. The main positive points are that it captures contrast adaptation in a particular cell type with a simple model, and that it raises a new potential mechanism for adaptation using one pathway modulating another, which is different from the accepted explanation of synaptic depression. It can be made suitable for publication, but a number of things must be done.

1) Spike history. For the spiking DivS model, the authors use the raw data as an input to the model when predicting the data. This seemed to be the case in the last review, although it was baffling to me and surprised both reviewers. Insufficient justification has been given for this procedure, and I can't conceive of any justification for it. The arguments given by the authors for this procedure are not persuasive, and as stated in the last review, this seems like cheating to get the model to predict more accurately.

Some arguments given by the authors as to why it is ok to use the data to predict the data:

“First, as detailed in the methods, we constrain the spike history term to be negative, meaning it cannot be used to predict future spikes, but rather only influences temporal patterning on short time scales due to refractoriness.”

If the spike history term is negative, thus causing silences, it helps the model predict future silences, which the same thing as changing the prediction of future spikes.

And Figure 5F shows the authors' claim that it cannot be used to predict future spikes isn't correct. With the spike history coming from the data, the beginning of bursts become more sharp, meaning the spike history is long enough for the data spikes in one burst to influence onset of spiking in the model's next burst. The decreased jitter in the statistics for the first spike in a burst confirms this.

Furthermore, the spike history goes out at least to 40 ms, and the full duration isn't shown or stated. The fact that it is small at 40 ms doesn't matter, because at long timescales the integration over multiple spikes will produce a large cumulative effect.

“Second, as we demonstrate, using a spike history term with an LN model (the LN+RP model in later figures) has poor performance in high contrast (Figure 5F), and also cannot explain contrast adaptation effects (Figure 7B), and thus the spike-history term is only effective at explaining these effects in tandem with divisive suppression in a two-stage computation, which is a major point of this work. “

This just means that this inappropriate use of the data in the model is not sufficient alone to predict the response, but it is necessary. It is nonetheless using the data to predict the data.

“In these figures, we explicitly compare the spiking DivS model with the LN+RP model (without DivS) to show that DivS is necessary, and furthermore show that the DivS-RP model (without spike history) also cannot explain the response to high precision and contrast adaptation, demonstrating that it is the interplay of spike-history effects with the DivS computation that uniquely explain the ganglion cell response and its adaptation to contrast. As described above, the use of spike history is well vetted by much published work in modeling the retina, but the DivS model goes well beyond this to show it alone is not sufficient to explain ganglion cell firing, and must be combined with computations present at the input to ganglion cells. “

The use of spike history in a feedback loop as part of the model is acceptable of course, but using the data spikes in the model's prediction is not. It is not well vetted to use this procedure to draw conclusions about the model performance, and as mentioned in the previous review references exist to show that it can greatly improve a model prediction (Kraus et al., 2015, Figure S4; Trucculo, et al., 2010), which shows why it is not an acceptable procedure.

The following statements and conclusions are currently unsupported, and need to be supported by a model using a spike history feedback filter, and not spike history from the raw data. It's fine to take these conclusions about millisecond precision and full adaptation in the spiking model out of the paper, the paper could stand without them.

Abstract. "The full model accurately predicted spike responses with unprecedented millisecond precision, and accurately described contrast adaption of the spike train."

Introduction. "Ganglion cell firing, further shaped by spike generation mechanisms, could be predicted to millisecond precision."

Figure 5–6 indicate that without the raw data (Div – RP model), predictions are no better than an LN model. Claims about precision should be removed unless a full spiking model with feedback spike history (without the raw data) is implemented.

Subsection “Contrast adaptation relies on both divisive suppression and spike refractoriness” "Therefore, the two nonlinear properties of retinal processing, contrast adaptation and temporal precision, are tightly related mechanistically and can be simultaneously explained by the divisive suppression model."

Contrast adaptation in spiking for the Div – RP model is improved over an LN model, so that claim can be kept, although full adaptation is not captured.

2) Lack of slow contrast adaptation. There is currently insufficient evidence addressing the lack of slow contrast adaptation, and in fact the authors perform an analysis that would obscure evidence of slow adaptation. Unfortunately, the authors have resisted my request to show the raw data from a 20 s segment of the recording, which would show the change to both high and low contrast and the full 10 s recording at each contrast. It's ok if there is some slow adaptation, but they have to show whether it's there or not.

Slow adaptation is revealed only in the change in the average membrane potential (Manookin & Demb, 2006). Gain and temporal filtering do not adapt slowly (Baccus & Meister, 2003), but statistics for gain and temporal filtering are the focus of the supplemental figure. The only evidence that might have been in the figure is the vertical position of the nonlinearity, which would show the change in average membrane potential. But surprisingly, in the methods it states, citing (Chander & Chichilnisky, 2001) "The resulting nonlinearities were then aligned by introducing a scaling factor for the x-axis and an offset for the y-axis." This y-axis offset would remove the evidence of slow adaptation. This offset was not used in (Chander & Chichilnisky, 2001) and should not be used here.

To be clear, three things must be done to address whether there is slow adaptation. 1) A full raw trace must be shown. 2) Nonlinearities must be shown without manipulation of the y-axis offset. 3) Because (Manookin & Demb, 2006) shows that most slow adaptation decays by 1.5 s, they should show the membrane potential averaged over trials and binned in increments of no larger than 1 s across the full 20 s.

3) LNK model. The authors are trying to claim that a model of synaptic depression can't reproduce the effect that there is greater suppression is in one spatial location than another. It is good that the authors have tried to compare the DivS model with different types of LNK models having two pathways, but in order to rule out a possibility (localized suppression from a depression model), they have to show that they have sufficiently tried to make that possibility work.

The authors resisted my previous suggestion in the first round of review to consider that bipolar cells have center-surround receptive fields and that more than one bipolar cell feeds into a ganglion cell. This implies that for two pathways, one from the center and one from an annulus, each tested pathway should have an input from both central and peripheral regions. The DivS models was allowed to have two pathways, each with a different weighting from the center and surround, but the LNK model does not have such a mixture for each pathway. A model should be tested where each of the two pathways of the LNK model have a weighting of center and surround. To be clear, one pathway should represent bipolar cells in the center, and should have a stronger weighting from the center than the annulus. The other pathway should represent bipolar cells whose receptive field center is under the annulus region, and should have a stronger weighting from the annulus than the central spot. This fits most with known circuitry, because bipolar cells have center-surround linear receptive fields. This test will probably work as the authors predict, but the current comparisons are not adequate for their claim.

The previously published LNK model used a 4-state kinetic model, the current version of the paper now shows that a 3-state model was used here. This means that the simpler model chosen here can't reproduce all of the dynamics of the previous model. This difference needs to be clearly pointed out and justified in the main text. This issue also fits with showing whether that there is not slow adaptation, because it may be that the reason that the LNK model slightly underperforms the DivS model is that they chose a model with more simplified dynamics, yet the cell has both fast and slow dynamics.

4) Comparison to Spike Triggered Covariance. There is some confusion in the presentation about what STC analysis reveals, and the relationship to the DivS model.

“We added Figure 2—figure supplement 1 to fully describe an STC analysis and added modeling data to Figure 2. As explained >above, we more clearly demonstrate a number of key differences of the DivS >model over the STC model, most notably the presence of divisive suppression. >We now make clear the caveat that other cell types could require additional >components to capture important features of the response in the Discussion.”

The following is a summary of the relationship, and it is basically in agreement with what is stated in the legend of Figure 2—figure supplement 1: STC analysis produces orthogonal vectors that define the stimulus subspace that drives the cell's response. It does not speak to the subsequent nonlinear mapping of that subspace to the response. In this case, if there is a two-dimensional subspace that defines the response, the filters of the DivS models must occupy the same subspace two STC eigenvectors. Thus this subspace can be found by a standard STC analysis not requiring a optimization procedure.

For the choice of nonlinear mapping of the subspace to the response, either there can be an n-D nonlinearity (2-D in this case), which would be the optimal solution, or a more simplified nonlinearity can be found. This is what the DivS model does, to simplify the 2-D nonlinearity to a product of 1-D nonlinear functions.

The reason I requested this detailed comparison was simply to avoid the mistaken conclusion that the DivS model is really a new class of model. It finds a reduced dimensional subspace just as STC does, and in fact such a standard technique can be used. The DivS model then does provide a set of constraints to reduce the complexity of the subsequent nonlinearity, reducing a 2-D nonlinearity to 1-D functions.

Even though the Figure 2—figure supplement 1 legend basically agrees with these statements, there are several statements and analyses in the paper that indicate a confusion:

Subsection “The nonlinear computation underlying synaptic inputs to ganglion cells”. However, the 2-D mapping between STC filter output and the synaptic current differed substantially from the same mapping for the DivS model (Figure 2—figure supplement 1).

This isn't possible if things were done correctly (and it seems to conflict with the Figure 2—figure supplement 1 legend), the STC subspace should be the same as the DivS subspace, and the 2-D nonlinearity from the STC subspace should be the same as the mapping from subspace to response for the DivS model. I think this is just a problem of how something is being stated, but it should be corrected/clarified.

There is one potential difference between a full-2D nonlinearity from an STC subspace and the DivS model, and that is that the full 2-D nonlinearity may overfit, and thus the DivS model may impose a regularization that allows a better model of a test data set. If this is true, this is an interesting point to make, and it seems to be more relevant with the spiking model, because the authors say that can't fit the 2-D nonlinearity for spiking data (they can of course, but it must not be accurate).

In the same section, Thus, despite the ability of covariance analysis to nearly match the DivS model in > terms of model performance (Figure 2E), it could not uncover the divisive interaction between > excitation and suppression (Figure 2G).

That's not the point of STC analysis, it only acts to find the relevant subspace. A second step would define the nonlinear mapping from subspace to response, either preserving the full 2-D nonlinearity, which would be the optimal solution, or simplifying the 2-D nonlinearity to a more biological combination of 1-D pathways.

It seems what the analysis of Figure 2E has done was to use the eigenvectors as filters for subsequent 1-D nonlinearities. That doesn't make any sense, the ideal 1-D nonlinearities have to lie in the 2-D subspace, but the 1-D nonlinearities don't have to be the eigenvectors, or even be orthogonal. This is not part of a standard STC analysis, and there is no reason to suspect that this would work.

The point of my request to state the relationship between the DivS model and STC analysis was not to pit STC analysis against the DivS model, because they should yield equivalent results as the stimulus subspace, and that's as far as STC analysis goes. It was so say that STC analysis will find the equivalent subspace as the DivS model, and that the DivS model provides a way to simplify the nonlinear mapping.

Discussion section, paragraph two. The presence of nonlinearities that are fit to data in the context of multiplicative >interactions distinguishes this model from multi-linear models (two linear terms multiplying) >(Ahrens et al., 2008a; Williamson et al., 2016), as well as more generalized LN models such as >those associated with spike- triggered covariance.

This isn't clear, STC only identifies the subspace, and then multiplicative interactions can be identified within that subspace.

5) Circuit mechanisms underlying divisive suppression.

It is appropriate to discuss the possibility that inhibition does play a role in adaptation, but the authors have to mention the previous literature that says that inhibition isn't needed for contrast adaptation (Brown & Masland, 2001; Manookin & Demb, 2006). This is in their favor to do so, because they point out that their model suggests an unexpected mechanism for contrast adaptation.

There is another point that the author's may wish to mention that supports their argument. As they mention, On-α cells are more linear with a high spontaneous firing rate. Depression models rely on there being a change in the average level of synapse activation with contrast. With a linear cell, the average input to the synapse doesn't change much with contrast, and thus a change in the level of depression may not occur. Thus, inhibition from a modulatory pathway may be needed to create contrast adaptation for a more linear cell.

6) Meaning of Divisive Suppression. The authors use the term divisive suppression to apply both to one pathway modulating another (the usual term), and to any change in gain as might occur from synaptic depression. This second use is strange, if that's true, then the finding of divisive suppression isn't new, they have just called gain control something else.

The potential new concept is that the effect is better modeled by one pathway modulating the other. This is actually an old concept, (Victor) and has since been replaced by one where a second pathway is not necessary, namely synaptic depression. But the new result would be that the older concept of modulation works better, especially when one considers the spatial stimulus. To make this comparison and state this conclusion, it makes more sense to restrict 'divisive suppression' to mean modulation, and thus the question becomes one of Suppression vs. Depression, rather than saying depression is one type of suppression.

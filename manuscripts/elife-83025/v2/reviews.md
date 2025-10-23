# Peer review - Round 1

Editors:
- Valentin Wyart, https://ror.org/02vjkv261 Inserm France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83025.sa0](https://doi.org/10.7554/eLife.83025.sa0)

This important work reveals a novel mechanism by which perceptual decision-making is regulated as a function of task demands. The combination of behavioral and physiological (EEG) evidence supporting the accumulation of evidence referenced to a context-dependent sensory criterion is convincing. Overall, the study makes a strong case for the importance of augmenting behavioral modeling with additional input from neural signatures of the underlying decision process.


---

# Peer review - Round 1

Editors:
- Valentin Wyart, https://ror.org/02vjkv261 Inserm France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83025.sa1](https://doi.org/10.7554/eLife.83025.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Balancing true and false detection of intermittent sensory targets by adjusting the inputs to the evidence accumulation process" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Valentin Wyart as Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Romy Frömer (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. As you will see, the two reviewers have found that your work makes a strong case as to how behavior alone can be insufficient to tease apart competing models of sequential sampling models of decision-making, and possibly lead to misattribution of observed behavioral differences. Your neurally-informed modeling approach shows how neural measures may help in such situations to arbitrate between models that are indistinguishable from behavior alone. However, both reviewers agreed that this approach relies strongly on the assumed relationship between the neural measure of interest (here, the Β amplitude signal) and the decision process, something which amounts to 'reverse' inference to some extent. It is therefore important to consider more explicitly the possibility that this assumed relationship may either be incorrect in some respect – e.g. because the neural measure reflects a mixture of components of the decision process rather than a single component. The approach is nevertheless novel, and potentially powerful, and the main text could provide all the available empirical evidence in the data that points toward the assumed relationship between Β amplitude and evidence-independent urgency.

The reviewers have agreed on the below list of essential revisions that should be addressed in a point-by-point fashion and accounted for in a revised version of your manuscript. The individual reviews of the two reviewers are also provided at the bottom of this decision letter for you to address also minor comments on the manuscript. These individual reviews do not require point-by-point responses. We hope that you will be able to address these comments and that you will choose to submit your revised manuscript to eLife.

Essential revisions:

1) The revised manuscript should give greater consideration to the possibility that the hypothesized relationship between the neural measure of interest (Β amplitude) and the decision process may not be entirely correct. The neurally-informed modeling approach is indeed quite appealing to distinguish between candidate models that are indistinguishable from behavior alone. However, it appears at times in the current manuscript to rely on a form of 'reverse' inference: assuming that the neural measure of interest is a faithful, selective correlate of a specific component of the decision process. It is almost never the case that such inferences can be made without significant doubt, especially in the case of non-invasive neural measures such as EEG-derived metrics.

A specific paragraph in the Discussion section would be very useful for readers to clarify not only the benefits of your novel approach but also its assumptions and potential caveats.

2) The neurally-informed modeling approach (Figure 3) appears to use Β amplitude as an evidence-independent urgency signal that adds to the decision variable (it is described as such in the Methods section). However, Β amplitude is clearly affected by the evidence (Figure 2A). And in the Results section, Β amplitude is described as best corresponding to a decision variable, which would include a dependence on sensory evidence. This seems conflicting: how can Β amplitude be used as an evidence-independent urgency signal in the neurally-informed modeling if it depends on sensory evidence?

To resolve this apparent discrepancy between the assumption of the neurally-informed modeling approach and the data, it would be very important to provide the key properties of the Β amplitude signal (ideally from your own dataset) that make it suitable to use as an evidence-independent urgency signal. This list should ideally be found in the Results section so as to give readers a clear idea of the several properties of this signal before using it as an evidence-independent urgency signal in the modeling. Because the interpretability of the results of these analyses depends on this assumption, it is key that the reader understands how much this modeling assumption is grounded in the available data. Nevertheless, a Discussion paragraph that explains how the neurally informed modeling approach depends on this assumption (see point 1) is very important.

3) Related to the previous point, the properties of the Β amplitude signal suggest that it reflects a mixture of processes rather than a selective component of the decision process. As noted by Reviewer 2, in the evidence criterion adjustment model, the average DV value during the ITI will be closer to the decision bound in the weaker signal condition compared to the stronger signal condition (this is how the model fits the false alarm rate differences). This should be reflected in Β amplitude if the latter reflects the DV. However, the Β-derived urgency is highest for the condition with the lowest false alarm rate and lowest for the condition with the highest false alarm rate. It would be very useful to clarify these seemingly hypothesis-inconsistent aspects of the data in the revised manuscript, which may be resolved with further details and explanations regarding what is expected of the neural signal of interest.

4) Regarding the criterion-adjustment model, could there be an alternative equivalent account that does not involve regulation of the transfer of incoming evidence? It appears highly similar to one with a constant negative drift added to the decision variable in addition to the contribution of evidence (and a lower reflecting bound).

5) Parameterization of the models. You explain clearly that one of the model parameters (e.g., noise or bound) must be fixed, but it is not clear why you didn't keep it the same parameter across all models. Couldn't you have fixed the noise parameters for all the models? Having it different across models makes it difficult to compare parameter values across the models, especially because the fitted noise term in the neurally-informed models appears dramatically reduced compared to the fixed value of noise used for the bound-adjustment model. Also regarding model parameterization, could you possibly report the leak parameter using more intuitive units? It seems to be parameterized as a fraction leak per time step, but the time step is unclear. Reporting the leak as a time constant would be immediately understandable.

6) Reviewer 2 has identified several problems with Figure 3, which should be corrected in the revised version: Figure 3 could benefit from a number of improvements. The various line types in the top panel of A are not labeled or described. The range of values of the y-axis in the top panel seems rather small compared to the overall false alarm rates. I know the latter was calculated as a proportion over 2-second intervals. I don't know the bin width for Figure 3A, but the numbers being a factor of 10 smaller seems pretty far off based on my best guess of bin width. The scaling of the bottom panel of A clips off 2 of the 3 curves at earlier times. From the methods, I believe at least one of the curves should go all the way down to 1, so half the range is cut off in the current version. In panel B, the evidence distributions are not labeled and a bit confusing. I can guess that they correspond to distributions with a strong signal, with a weak signal, and without a signal. However, the presumptive "without signal" black distribution appears shifted negative of zero, which I don't think is correct. The title of panel F says "simulated Bound-adjustment" while the text describes this as the "simulated criterion-adjustment" model. I presume this is a mistake in labeling the title, but as this is the most critical distinction for the paper's main conclusion, it's really important to get it right.

7) In Figure 3F (simulation of the criterion-adjustment model), it is indeed quite puzzling that the DV is at zero at the time of target onset. You explain that the urgency signal was removed from the simulations of this "DV", which is useful, but there should still be an influence of pre-target noise. Did the simulations not include any influence of pre-target noise? Reviewer 2 is correct that it is unclear why it is not included, and it should be explored explicitly if possible.

8) It would be useful to discuss at least some alternative models that may have not been considered in this study. Modeling studies and their comparison are always dependent on the models being included. One could maybe have thought of a different alternative to the standard model, such as the precision-weighted evidence integration mentioned by Reviewer 3. It would be useful to discuss alternative variants of the standard account of the contrast between conditions somewhere in the Discussion section.

Frömer, R., Callaway, F., Griffiths, T., & Shenhav, A. (2022, October 22). Considering what we know and what we don't know: Expectations and confidence guide value integration in value-based decision-making. Retrieved from psyarxiv.com/2sqyt

Reviewer #1 (Recommendations for the authors):

In addition to the comments in the Public Review, Figure 3 could benefit from a number of improvements. The various line types in the top panel of A are not labeled or described. The range of values of the y-axis in the top panel seems rather small compared to the overall false alarm rates. I know the latter was calculated as a proportion over 2-second intervals. I don't know the bin width for Figure 3A, but the numbers being a factor of 10 smaller seems pretty far off based on my best guess of bin width. The scaling of the bottom panel of A clips off 2 of the 3 curves at earlier times. From the methods, I believe at least one of the curves should go all the way down to 1, so half the range is cut off in the current version. In panel B, the evidence distributions are not labeled and are a bit confusing. I can guess that they correspond to distributions with a strong signal, with a weak signal, and without a signal. However, the presumptive "without signal" black distribution appears shifted negative of zero, which I don't think is correct. The title of panel F says "simulated Bound-adjustment" while the text describes this as the "simulated criterion-adjustment" model. I presume this is a mistake in labeling the title, but as this is the most critical distinction for the paper's main conclusion, it's really important to get it right. To underscore that point, if this is in fact the simulation of the criterion-adjustment model, I'm surprised that the DV is at zero at the time of target onset. I realize that the urgency signal was removed from the simulations of this "DV", but there should still be an influence of pre-target noise. For the other models, the noise-driven DV averages to zero, but with the zero floor of the criterion-adjustment model, it shouldn't peg 0 exactly during this time. I suspect that the simulations did not include any influence of pre-target noise, and I would suggest that is something that should be included.

Reviewer #2 (Recommendations for the authors):

This paper was a pleasure to read. I found it very clearly written, with a clear rationale and thorough tests of the theoretical predictions. The methods are impressive but conveyed in a way as to not scare off readers.

I would love to be helpful, but I can't see where the authors could use my advice.

Perhaps out of curiosity: Instead of a sensory criterion as implemented by the authors, could the same pattern be achieved with precision-weighted evidence integration? (cf. Frömer, R., Callaway, F., Griffiths, T., & Shenhav, A. (2022, October 22). Considering what we know and what we don't know: Expectations and confidence guide value integration in value-based decision-making. Retrieved from psyarxiv.com/2sqyt).

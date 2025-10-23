# Peer review - Round 1

Editors:
- Richard Ivry, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20047.024](https://doi.org/10.7554/eLife.20047.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Neural hysteresis in competitive attractor models predicts changes in choice bias with non-invasive brain stimulation" for consideration by eLife. Your article has been favorably evaluated by Sabine Kastner (Senior Editor) and three reviewers, one of whom, Richard Ivry (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Boris Burle (Reviewer #2).

Summary:

The reviewers find considerable merit in this study. This paper provides a nice blend of theoretical and experimental work to demonstrate the possible neural bases for one form of response bias, namely that observed from trial to trial. The authors employ a rather detailed biophysical model but the core idea here is quite simple-residual activity in the decision units will influence decisions on subsequent trials. This effect will be most pronounced on difficult decisions, mainly because easy decisions rise very quickly to threshold. The authors perform a tDCS experiment to show a similar pattern of behavior in humans, with a greater carryover effect following depolarized stimulation arrangement and reduced carryover following hyperpolarized arrangement.

All in all, this is a very solid work piece of work. The reviewers do think that the paper could push things a bit harder to probe the robustness of the model. There is little discussion about alternative models (other than variation in locus of modeled stimulation) and thus it is difficult to evaluate the goodness of their model-it is really evaluated at a qualitative level. In addition, there are some obvious opportunities here to look at predictions from the model and ask if these are supported behaviorally, either using published data or by conducting an additional experiment. We outline recommendations for revision below.

Essential revisions:

1) Simulation effect of inter-trial interval being extended. Obviously, the carryover effect should diminish with an increase in ITI. In fact, with their parameters, the effect of ITI might be quite large over a limited range (e.g., 500 ms to 5 s). We would like to see this simulated and tested in a new behavioral study (or use published data, if appropriate). No need to do tDCS here; a simple behavioral experiment will suffice. However, the current tDCS data could also be analyzed to examine this issue since you have a range of ITIs. For example, a median split into short ITI vs. long ITI. We recognize that since you kept the trial rate constant, ITI is confounded with RT. Moreover, the small ITI range will reduce sensitivity so this re-analysis is unlikely to provide a strong test.

2) The text suggests that the simulations were done with trial-by-trial stimulation whereas the tDCS conditions were blocked in the experiment. If this is correct, it is not obvious if the model would make the same predictions if the simulated stimulation was blocked. The authors should clarify this issue and, if not tested, run a blocked simulation to verify that the trial-by-trial effects persist under this condition. (Perhaps it is obvious from the model parameters that trial-to-trial effects do not persist over neighboring trials because of reset properties-if so, this should be made explicit.)

3) An alternative model could be tested by removing reciprocal inhibition between the decision units. There are accumulator models that do not make an assumption of this form (independent accumulators) and the finding of partial errors (e.g., the work of B. Burle and colleagues) suggest that there can be pronounced activation in both choices at time of response onset. Does removing the reciprocal inhibition change things in a significant way?

4) Text does not indicate if the participants made left/right decisions with two fingers of one hand (which one?) or with two fingers from different hands. While this may seem (and be) a trivial point, it also gets at a subtle issue/assumption with the model. The model assumes that both response options are affected by the stimulation. It is reasonable to assume that the level of interaction is the same for all possible response pairs? Would one expect unilateral stimulation to produce similar interactions if effectors were both contralateral to side of stimulation as when only one effector was contralateral to side of stimulation. The authors should clarify how responses were made and make explicit implications of this issue (even if to comment on why they think it isn't important or to comment on predictions to be derived from consideration of this issue).

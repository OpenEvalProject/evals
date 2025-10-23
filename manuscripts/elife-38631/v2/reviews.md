# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38631.020](https://doi.org/10.7554/eLife.38631.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A repressor-decay timer for robust temporal patterning in embryonic Drosophila neuroblast lineages" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aviv Regev as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Lea Goentoro (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We thought that the work is interesting. However, major points need to be revised and the paper needs to be decompressed. In particular, the reviewers highlight the need to better understand whether repressor decay is in theory (per Figure 2A,B) more robust than activator accumulation (as per the reviews below). We chose to provide you with the full reviews, as all the reviewers agreed those reflect the key issues to be addressed.

Reviewer #1:

In the Drosophila embryo, neural progenitors produce a sequence of neurons whose identities depend on the sequential expression of temporal transcription factors (TTF). Although this process is thought to be driven by a relay of activators, Averbukh et al. proposed that a repressor-decay timer is the main player. To evaluate the relative contribution of activator-relay and repressor-decay, they mathematically modeled the TTF timer network, and predicted that with repressor-decay, induction timing of a transcription factor was more robust (changed less) when, for example, activator synthesis rate was reduced. They reasoned that the timer had evolved to be robust, and thus, repressor-decay (which supports higher robustness) should be important. They then did more modeling to design experiments and predict experiment results. Experimental tests supported the repressor-decay mechanism in that the induction timing of Pdm and Cas expression was sensitive to the deletion of the respective repressor and much less so to the deletion of activator. The followings are NOT tested experimentally: repressor-decay timer being more robust than activator-relay timer, and robustness being the selective pressure for evolving repressor-decay timer. However, I do like how the authors use modeling in different ways to gain biological insight and to instruct experiment design. Modeling worked rather well!

The biggest problem I have with this paper is the argument of repressor-decay causing less perturbation in induction timing than activator-accumulation (Figure 2A-B). Seems that this assertion is sensitive to the line slope (the less steep a line e.g. Figure 2A, the bigger the timing perturbation). The line slope will in turn depend on parameters, and the two mechanisms can have different parameters. The argument on this point is also rather hand-wavy in the Discussion (second paragraph). This needs to be clarified.

I find Figure 3B difficult to follow. If my understanding is correct, then the lower right dot essentially says that for this particular set of parameters, deleting HB (but not Kr) causes dramatic phenotype, meaning that HB (decay timer) is important. With this set of parameters, the original "wildtype" network is robust. It took me a couple readings to get this. This needs to be explained better.

"Robustness score", a concept key to this article, had no visual aids. Even in the Materials and methods, the explanation of robustness score was not clear (e.g. "phase duration"). I recommend adding conceptual illustrations like Figure 2D.

Reviewer #2:

I find all the exercise of constraining the model with data quite interesting. I also find the experimental results interesting. That said, I am not entirely convinced by the logic of the reasoning presented. For instance, the experimental results presented in the fourth paragraph of “Timing of Pdm and Cas expression is highly sensitive to deletion of TTF repressors, but less sensitive to deletion of TTF activators” validate the idea that the system is not a relay timer. But do we really need the theoretical study on robustness to get there? In fact, to validate the repressor decay vs. the activator relay model, the only solution is to directly perform those experiments (and maybe other ones to really validate the mechanism). The paper tries very hard to argue that an elaborated theory related to robustness is needed to predict the network topology, but I am rather unconvinced. It could be that the activator relay mechanism is impossible for other reasons that have nothing to do with robustness, so such robustness arguments are in my opinion neither very illuminating nor conclusive.

The attempt to "force" the model to predict experimental results also leads to the strange third paragraph in subsection “Timing of Pdm and Cas expression is highly sensitive to deletion of TTF repressors, but less sensitive to deletion of TTF activators”, where we basically learn that, after experimental verification, all the calibration of the model related to Pdm is incorrect, but that does not matter. It seems to me that in such situation, it would be more reasonable to use this information to redo the theoretical study with the new calibration; one could well learn something new.

On top of that, I found the paper at times difficult to follow. The paper seems to have been initially written for a journal with a very compressed format, but I believe it would be much better if some details and more explanations were given in the main text (I give some suggestions below but they are not exhaustive).

Other comments (in no particular order):

1) The authors postulate a dichotomy between activator-relay and repressor decay. This seems a bit arbitrary to me. One could well imagine more complex networks, a mix of the two via genes that are not known to be implicated, etc. I understand there is a limit to what one can do on the theory side, but I feel some discussions should be added. For instance is it known that the genes studied in the model are necessary and sufficient for the entire process?

2) I found the introduction of the parameter exploration a bit too concise. It would be good to explain how the parameters were chosen and constrained. For instance are there experimental data that are constraining them like degradation rates? More generally, are the parameters found after optimization consistent with what is known or reasonable?

3) Obviously there are also predictions on the possible ranges of parameters when theory is combined with experimental data. I found this is a potentially very interesting aspect of the paper that is not explored sufficiently. For instance can we get more information on parameters from the experimental constraints shown on Figure 5 G and I?

4) I find statements in the first paragraph of subsection “A TTF circuit can be positioned in the relay-decay timer space based on TTF-deletion phenotypes” on the connections between robustness and evolution too speculative and in my opinion confusing.

Reviewer #3:

In this paper, the authors combined modeling of interactions between four Temporal Transcription Factors (TTFs) with experiments to understand the architecture of the TTF timer in neuroblasts. The authors developed a computational framework to distinguish between relay and decay timers, identified all possible circuits that can reproduce normal and perturbed neuroblast phenotypes, and then showed how delay timers are more robust to parameter variations than relay timers. Lastly, they collected high-resolution data for TTF induction time in WT and knockout fly lines, and concluded that temporal TTF activation is primarily governed by a decay-timer circuit.

The authors concluded that robustness is not only a feature of spatial patterning, but also temporal patterning in embryos. The work also provides a wonderful insight into the longstanding question of activation vs. repression in biology.

Major comments:

1) It is unclear why only production rates are being varied for the perturbation analysis, especially since the reasoning for robustness in decay timers (subsection “A repressor-decay timer is more robust than an activator-relay timer”) is based on sensitivity to thresholds Tr. Can the authors provide a rationale? What happens if other parameters are varied as well?

2) Figures 2E, 3B, and Figure 2—figure supplement 2 may appear conflicting. Figure 3B clearly demonstrates that decay timers are more robust than relay timers, with robust circuits concentrated in the bottom right of the perturbation-space. In Figure 2E however, robustness seems to be dependent on the decay interaction, while invariant to the relay-interaction. Finally, in Figure 2—figure supplement 2, robustness shows more complicated dependencies.a) It would be helpful to see Figure 2E and 5I split up into two figures, one for Pdm induction, and one for Cas induction – possibly as supplemental figures. Combining the two as they are currently in Figure 2E, raise questions if there are some patterns that are missed, especially since Figure 3B and Figure 2—figure supplement 2 look so distinct. Could it be that Pdm, but not Cas, induction is the sensitive step in the network where robustness analysis can distinguish relay vs decay?b) Additionally, the Materials and methods indicate that when estimating the significance of the decay network for Cas induction, only the Kr-Cas interaction is removed, and the Hb-Cas interaction is left intact. Can the authors discuss why the dual-repression of Cas is not needed?

3) Figure 5A-F clearly demonstrate that removing the immediate activators has no effect on Pdm and Cas induction timing, and removing the repressor clearly affects timing of Pdm induction. But we have the most trouble with Figure 5E.a) First, Cas induction is pretty modest in both at st11 and 12. Then, based on the network, Cas represses Pdm, and we see this borne out in WT, where at st12, high Cas correlates with low Pdm. However, in Kruppel mutant, Pdm remains high, which seems to signify that there isn't much Cas induction? Can the authors discuss how they see these data? Is there an independent way to confirm that Cas is induced, and induced earlier?b) For Figure 5A-F: It would be helpful to draw a line indicating the "background level" of TTFs, to allow readers to see significance more easily. It would also be helpful to immediately see in the legend the way significant induction is determined. Also, the black arrows are not defined in legend.c) Cas is also repressed by Hb. Can the authors justify why they didn't analyze Cas induction in Hb mutant?

4) It would help to have the Materials and methods be better organized. Perhaps with separate sections, so readers can easily find the relevant information. For instance, we had trouble keeping track of the different ways Δtind normalization was performed.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A repressor-decay timer for robust temporal patterning in embryonic Drosophila neuroblast lineages" for further consideration at eLife. Your revised article has been evaluated by Aviv Regev (Senior Editor), and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been greatly improved but there are some remaining issues that need to be addressed by writing changes before acceptance. In particular, the reviewers requested that certain aspects be written more explicitly and clearly, and in a manner geared toward a general audience. Furthermore, they ask that the evolution aspect should be de-emphasized given the lack of direct data, although raising all such matters in the Discussion section should address this concern.

Because some of the reviewers have been grappling in their consultation specifically around writing and presentation, we highlight below the key areas and items that need to be addressed, and the specific writing revisions we request.

1) One reviewer still found the paper rather hard to read, and was not really convinced by the articulation between theory and experiments as is. The experiments done directly show some repressions from upstream genes, so as pointed out in the first review, one does not really need a very elaborated theory to predict this since it is a direct verification. The understand the authors argument that theory helps better refining what experiments to do, but believe that the authors should explain this more clearly. The actual experiments potentially related to theory are in Figure 5: they are connected to the correlations between times on Figure 3 C-D. I found the explanations there too short and concise, and unclear. There is too much of handwaving ("as seen in") making the arguments difficult to understand. On the one hand there are many mutants, on the other hand each mutant gives essentially one point in parameter space that is then placed in the abstract sensitivity space. There are several layers of reasoning here that could be much better explained (Figure 5H is particularly obscure). The reviewer also felt there could be some intuitive or analytical explanations. The authors allude to some analytical work in their rebuttal letter, is there a simple way to interpret the tight correlations of Figure 3 (it seems the correlation simply comes from the existence of one activation)? Also it seems the only argument for the "decay" part is the point 1', but is this really a strong effect?"

To address this, the reviewers together suggest:

The paper should clarify that it presents two parallel arguments for the decay timer:

1) The robustness from modeling analysis.

2) The experiment.

(i.e. rather than a "linear" model-predicts-experiment paper). A paragraph in the Introduction to better clarify the logic of the paper could help.

2) One of the reviewers has an ongoing concern with the robustness argument presented as the core of the paper, as hypothetically, there could be many ways to have a more "robust" network to noise. The fact that a less complicated network is less robust was not fully convincing in implying that robustness is a good biological criterion to assess the evolutionary origin of the network architecture.

We suggest that the results and interpretation of the paper should stand independent of this conjecture to focus on the repressor decay mechanism as a better explanation of the experimental results (which would roughly correspond to what is done in Figure 5 and associated theory), and reduce overinterpretation of the evolutionary origin of the network structure. Overall, given that the paper does not show that robustness is the selective pressure for evolving repressor-decay timer, we prefer this emphasis be reduced, for example, by moving this point to the Discussion.

3) The Discussion should also include the responses (from the authors' rebuttal) on work that was not done.

4) Another concern from the initial reviews was the issue of predicting parameter values from the simulations, and the authors' response that they could not really see anything. If the parameters are truly completely random in the region compatible with data, we would ask to show it explicitly. It seems a bit paradoxical that, following the authors' line of thought, one could predict so carefully the existence of extra negative interactions from the study, but nothing on the actual parameters corresponding to those interactions. At the very least the negative interactions should have parameters significantly different from a "default" state where they would not contribute. This point should be clarified.

5) While we very much appreciate the extra experiment to address our most important concern about the Cas experiments, we are however, still concerned by the fact that Cas delay-relay space (Figure 2—figure supplement 2B) does not support the robustness argument (third paragraph of subsection “A repressor-decay timer is more robust than an activator-relay timer”). We do see the robustness argument with the Pdm space (Figure 2—figure supplement 2A) and when considering the combined Pdm-Cas space in Figure 2E. This concerns us because it can compromise the overall robustness argument, in several ways:a) Perhaps Figure 2E sets up expectations about the robustness of the decay circuits, only to find out in the supplement that it is more true for Pdm, but not as much for Cas.b) It could also raise doubts on the analysis. E.g., what if Cas is less pronounced because the metric "decay significance" vs. "relay significance" does not capture the effects comprehensively enough for Cas. For instance, Cas is inhibited by Hb and Kr, but one could also view Hb's inhibition of Pdm is an inhibition of Cas (which is not removed in the analysis).

In either case, we ask that this be addressed by some re-writing, e.g., for point a, state earlier the difference between Pdm and Cas analysis, so readers are not led to expect more after seeing Figure 2E.

For point b: Add more explanation to the label "significance of decay", perhaps in parentheses, with what is actually being evaluated, e.g., "removal of Pdm--|Cas interaction".

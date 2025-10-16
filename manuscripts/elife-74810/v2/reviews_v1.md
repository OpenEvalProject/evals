# Peer review - Round 1

Editors:
- Henrique von Gersdorff, https://ror.org/009avj582 Oregon Health and Science University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74810.sa0](https://doi.org/10.7554/eLife.74810.sa0)

The calcium dependence of vesicle exocytosis at synapses is a power law with an exponent n = 3 or 4, however, the molecular mechanisms that underpin this highly non-linear dependence on calcium are unclear. To shed light on this fundamental question the authors build a model where 2 calcium ions bind to the protein synaptotagmin and synaptotagmin binds to the negatively charged lipid PIP2 in the presynaptic membrane. Simulations fit best the data from the calyx of Held synapse when 3 synaptotagmin molecules each bind calcium and PIP2. This compelling model shows that each Ca-synaptotagmin-PIP2 complex reduces the energy barrier for vesicle fusion by ~5k, thus, fast exocytosis at CNS synapses may require only 3 Ca-synaptogamin-PIP2 molecules to achieve submillisecond speeds of vesicle fusion.


---

# Peer review - Round 1

Editors:
- Henrique von Gersdorff, https://ror.org/009avj582 Oregon Health and Science University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74810.sa1](https://doi.org/10.7554/eLife.74810.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Allosteric stabilization of calcium and lipid binding engages three synaptotagmins in fast exocytosis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Victor Matveev (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Lines 670-672: The main assumption of the model is that near-simultaneous binding of 2 calcium ions greatly increases the affinity of PIP2 binding. However, simultaneous binding of 2 Ca2+ ions must imply an even stronger cooperativity between the two Ca2+ binding events than the cooperativity between Ca2+ and PIP2 binding. While equilibrium properties are not affected by such an assumption, the time-dependence of the model should depend on the precise sequence of binding events. Would the release latency predictions change if both Ca2+ binding events were resolved? Of course, the stochastic simulations for a more complicated model would be costly, and extra model parameters are not desired, but one trial analytic solution for a constant Ca2+ level is probably not hard. I am not insisting that any new simulations be included in the paper, but it would help to discuss briefly whether the assumption of two simultaneous Ca2+ binding affects the release latency estimation.

2) On page 10, the Authors describe their checks to ensure that the model parameter optimization procedure is not stuck at a local minimum. However, a more straightforward common check would involve repeating the fminsearch parameter optimization algorithm multiple times, while starting at different initial values of parameters. Have the Authors performed such a check? This would essentially quantify uncertainties in inferred parameter values in Table 2.

3) In the discussion (Line 542) the authors note that their model is fundamentally different from the proposed preassembly of Syt rings at the base of a vesicle, and that this is big testable prediction. How could this be tested? And do Syts actually preassemble with slots in their model? Figure 3B shows the number of crosslinks that precede fusion, and it would be nice to see how many Syts are bound to PIP2 at rest for any given number of "slots".

4) I like Figure 2 Sup2, where the authors probe the number of crosslinks prior to fusion. Interestingly, the speed of Ca ramping affects the number of crosslinks, and a significant number of events occur after 4 crosslinks only when Ca increases at the fastest rate (0.001 s). This is still much slower than the expected rate of Ca nanodomain formation (<100 us). Why did the authors explore only extremely slow Ca ramp rates? It seems that the ramping rates of 10 us to 10 ms would more accurately affect the condition of action potential induced Ca influx.

5) It is not immediately clear to me why the model with 6 slots never predicts fusion with 5-6 crosslinks. Why does the model fail to fit well if each crosslink contributes less to lowering the energy barrier, and thus 5-6 crosslinks are required to drive fusion?

6) If a single crosslink brings the vesicle closer to the PM, this will introduce a new form of allostery by increasing the effective concentration of PIP2 sensed by Syts. Is this reflected in the model?

7) In the model, PIP2 binding is required for Syt1-driven fusion. As a result, only Syts with a "slot" can participate in fusion. However, while K325, 327A mutations that disrupt Ca-independent PIP2 binding lead to less synchronous release, synchronous release can be restored using a paired-pulse stimulation paradigm where an initial action potential drives Ca-dependent membrane attachment of vesicles to the plasma membrane. This suggests that PIP2 binding is not required for "cross linking". How might the model change if Syts without slots could also contribute to fusion in your model?

8) The evaluation of mutants in Figure 5 should be better tied to actual biology. What mutation does "Ca2+ binding", and "A-on" mimic? No citations are provided for the many studies where Syt mutants were expressed in Syt1 KO neurons. This seems like a perfect place to test the role of PIP2 binding with more complicated Ca stimuli. Could the model be adapted to explore the effect of K/A mutations described by Chang, Trimbuch and Rosenmund?

9) Recent experimental and modeling work with Synaptotagmin and SNAREs has been published (Wu et al., 2021; eLife; https://elifesciences.org/articles/68215). These authors say: "To test whether Syt1 affected fusion pores in this system, we co-reconstituted ~4 copies of recombinant full-length Syt1 together with ~4 copies of VAMP2 (per disc face) into large nanodiscs called nanolipoprotein particles…". The work seems particularly relevant to your paper. Also please take a look at another paper from this group that suggests fast exocytosis requires up to 15 SNAREs and Syt complexes (Wu et al., eLife, 2017; https://elifesciences.org/articles/22964). Please read and discuss in your paper these recent modeling studies, which seem to suggest that large numbers of Syt's and SNAREs are needed for fast exocytosis at synapses.

Reviewer #1 (Recommendations for the authors):

1) Lines 670-672: The main assumption of the model is that near-simultaneous binding of 2 calcium ions greatly increases the affinity of PIP2 binding. However, simultaneous binding of 2 Ca2+ ions must imply an even stronger cooperativity between the two Ca2+ binding events than the cooperativity between Ca2+ and PIP2 binding. While equilibrium properties are not affected by such an assumption, the time-dependence of the model should depend on the precise sequence of binding events. Would the release latency predictions change if both Ca2+ binding events were resolved? Of course, the stochastic simulations for a more complicated model would be costly, and extra model parameters are not desired, but one trial analytic solution for a constant Ca2+ level is probably not hard. I am not insisting that any new simulations be included in the paper, but it would help to discuss briefly whether the assumption of two simultaneous Ca2+ binding affects the release latency estimation.

2) On page 10, the Authors describe their checks to ensure that the model parameter optimization procedure is not stuck at a local minimum. However, a more straightforward common check would involve repeating the fminsearch parameter optimization algorithm multiple times, while starting at different initial values of parameters. Have the Authors performed such a check? This would essentially quantify uncertainties in inferred parameter values in Table 2.

3) Apart from the nice connection between the proposed model and the model of Lou, Scheuss and Schneggenburger (2005), I think the presented model can also be viewed as a more detailed and biophysically-based extension of the "excess-calcium binding site model" of S.D. Meriney and coworkers, which I would recommend citing. To my knowledge, there are 3 papers that make use of the latter model, in one form or another (but I would recommend that the Authors double-check these papers to see if all of them are relevant):

Dittrich M, Pattillo JM, King JD, Cho S, Stiles JR, Meriney SD (2013) An excess-calcium binding site model predicts neurotransmitter release at the neuromuscular junction. Biophys J 104: 2751-63

Ma J, Kelly L, Ingram J, Price TJ, Meriney SD, Dittrich M (2015) New insights into short-term synaptic facilitation at the frog neuromuscular junction. J Neurophysiol 113: 71-87

Luo F, Dittrich M, Cho S, Stiles JR, Meriney SD (2015) Transmitter release is evoked with low probability predominately by calcium flux through single channel openings at the frog neuromuscular junction. J Neurophysiol 113: 2480-9

Reviewer #2 (Recommendations for the authors):

1. The style and length of this paper resemble a thesis. The authors are encouraged to edit the manuscript to make it accessible to a wide eLife audience. Many figures have complicated subpanels that are difficult to understand, and the text is often so technical that it does not convey the essential point of each argument. This is a very nice model. The authors could do a better job of describing the important points, which they highlight most clearly at the beginning of the discussion.

2. The model depicted in Figure 1A suggests that Ca-bound C2B attaches to the vesicle, rather than the PM. However, Chang, Trimbuch and Rosenmund 2019 showed that the PIP2 binding attaches vesicles to the PM before an action potential. Do the authors want to claim that Ca-bound C2B attaches to vesicles? This is actually very important to the main point of the paper, because "crosslinks" are likely to occur in the absence of Ca, and Ca-independent PIP2 binding might position the Ca-binding pocket closer to negatively charged phospholipids, increasing the affinity of C2B for Ca.

3. In the discussion (Line 542) the authors note that their model is fundamentally different from the proposed preassembly of Syt rings at the base of a vesicle, and that this is big testable prediction. How could this be tested? And do Syts actually preassemble with slots in their model? Figure 3B shows the number of crosslinks that precede fusion, and it would be nice to see how many Syts are bound to PIP2 at rest for any given number of "slots".

4. Line 149: What (little) is known about the concentration of PIP2 at active zones? How does the concentration of PIP2 in rich patches compare to the idea that only 3 PIP2 molecules could be available beneath the space of one vesicle? I found the discussion of PIP2 concentration in Methods (Line 999) difficult to understand.

5. The model only accounts for Ca binding by the C2B domain, which as the authors note is the more important of the C2 domains. C2A is barely discussed in this paper. However, there are differences in fusion rates when the C2A domain is mutated to block Ca binding. How would the addition of C2A affect the model?

6. I like Figure 2 Sup2, where the authors probe the number of crosslinks prior to fusion. Interestingly, the speed of Ca ramping affects the number of crosslinks, and a significant number of events occur after 4 crosslinks only when Ca increases at the fastest rate (0.001 s). This is still much slower than the expected rate of Ca nanodomain formation (<100 us). Why did the authors explore only extremely slow Ca ramp rates? It seems that the ramping rates of 10 us to 10 ms would more accurately affect the condition of action potential induced Ca influx.

7. It is not immediately clear to me why the model with 6 slots never predicts fusion with 5-6 crosslinks. Why does the model fail to fit well if each crosslink contributes less to lowering the energy barrier, and thus 5-6 crosslinks are required to drive fusion?

8. If a single crosslink brings the vesicle closer to the PM, this will introduce a new form of allostery by increasing the effective concentration of PIP2 sensed by Syts. Is this reflected in the model?

9. In the model, PIP2 binding is required for Syt1-driven fusion. As a result, only Syts with a "slot" can participate in fusion. However, while K325, 327A mutations that disrupt Ca-independent PIP2 binding lead to less synchronous release, synchronous release can be restored using a paired-pulse stimulation paradigm where an initial action potential drives Ca-dependent membrane attachment of vesicles to the plasma membrane. This suggests that PIP2 binding is not required for "cross linking". How might the model change if Syts without slots could also contribute to fusion in your model?

10. The evaluation of mutants in Figure 5 should be better tied to actual biology. What mutation does "Ca2+ binding", and "A-on" mimic? No citations are provided for the many studies where Syt mutants were expressed in Syt1 KO neurons. This seems like a perfect place to test the role of PIP2 binding with more complicated Ca stimuli. Could the model be adapted to explore the effect of K/A mutations described by Chang, Trimbuch and Rosenmund?

Reviewer #3 (Recommendations for the authors):

Such kind of complex models tend to have various underlying assumptions which could significantly influence the conclusions. Three examples are provided:

1. The interaction of synaptotagmins with SNARES or other proteins could change the Ca2+ affinity but only PIP2 is considered as a potential interaction for changing the Ca2+ affinity. In other word, the premise of the paper that the Ca2+ affinity of synaptotagmin in vitro and in vivo (within the protein complex of the fusion machinery) is identical could be wrong. Therefore, the main conclusion of the strong cooperativity of Ca2+ and PIP2 could be wrong.

2. The assumption that each crosslinking synaptotagmin lowers the energy barrier for fusion by the same amount (E_syt) could be wrong. Assuming a positive or negative cooperativity in E_syt per synaptotagmin might impact the conclusions regarding the number of required synaptotagmins.

3. The distance between the individual synaptotagmin molecules and the nearest Ca2+ channels could differ significantly on the nm-scale. The assumption of an identical local Ca2+ signal for all synaptotagmins could be wrong which could complicate the model predictions of the effect of reduced synaptotagmin copy numbers (Figure 4 and 5).

In conclusion, the study provides interesting and plausible possibilities of how synaptotagmins could mediate vesicle fusion but experimental validations are required to increase the amount of reliable and novel insights.

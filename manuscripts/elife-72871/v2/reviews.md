# Peer review - Round 1

Editors:
- J Andrew Pruszynski, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72871.sa0](https://doi.org/10.7554/eLife.72871.sa0)

The present study indicates that humans cannot easily learn to control multiple motor units innervating a single muscle independently. These results suggest that common drive to motor units and the size-recruitment principle impose strong constraints on the motor system and, as such, on the use of high-resolution muscle recordings as a means of controlling brain-machine interfaces.


---

# Peer review - Round 1

Editors:
- J Andrew Pruszynski, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72871.sa1](https://doi.org/10.7554/eLife.72871.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The control and training of single motor units in isometric tasks are constrained by a common synaptic input signal" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, and the evaluation has been overseen by Andrew Pruszynski as the Reviewing Editor and Tirin Moore as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andrew Fuglevand (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The paper needs to provide clear demonstration/analysis of the spike sorting algorithm specifically showing that it can accurately differentiate the onset and offset times of pairs motor units selected from Group 1 and pairs selected from Group 2. This can be done based on the authors already-published simultaneous surface/intramuscular recordings but it should also include an analysis/estimate of accuracy when the method is applied to the data in the present paper.

2) Given the smoothing of firing rates being used, the authors need to demonstrate that the participants could have, in principle, used the visual feedback to discriminate recruitment times of motor unit pairs. One way of doing this is generating a series of videos showing the visual feedback that would have been shown to a participant in which two motor units are recruited at different times relative to one another (this would be synthetic data). That is, artificially shift the timing of an MU1 spike train to the right for a Condition III trial - a few videos with shift increments of ~250 ms seem reasonable for such an illustration.

3) The authors suggest PICs as the explanation of selective de-recruitment of lower threshold units. As described by Reviewer #2, inhibitory inputs will also be shaped by the size principle such that low threshold (i.e. high input resistance) neurons will exhibit greater hyperpolarization. This could lead to a situations where lower threshold neurons become deactivated before higher threshold ones. Please consider this and other explanations in the revised Discussion.

4) The authors should directly discuss the differences between upper and lower limbs in terms of control and thus potential deviations the size-recruitment principle.

Reviewer #1 (Recommendations for the authors):

1. (pg 2, ln 14) "These results suggest that flexible MU control based on independent synaptic inputs to single MUs is not a simple to learn control strategy" The last phrase "is not a simple to learn control strategy" seems pretty waffly. I would suggest replacing it with something like "is unlikely".

2. (pg 3, ln 26) "and faster" perhaps substitute "and with higher rates".

3. In his Handbook of Physiology Chapter (Henneman & Mendell (1981) Functional organization of motoneuron pool and its inputs) Henneman describes attempts to alter recruitment order with biofeedback that would seem relevant to the present manuscript:

"In six of the nine subjects no changes in recruitment order were observed despite two hours of training and the help of audiovisual feedback. In each experiment recordings were made from many sites, and the subject was encouraged to explore maneuvers that might lead to alteration in recruitment. At each new site at least 20-30 minutes was spent attempting to alter the normal order. In not a single instance, out of hundreds of trials, was anyone of these six subjects able to recruit two units in their usual small-to-Iarge order and then turn off unit 1 without silencing unit 2".

"The results at almost all recording sites in the three remaining subjects were similar to those just described. In each of these subjects, however, there was one site at which some variability in recruitment order was observed. Although one unit was recruited first and dropped out last in the majority of tests, the unit that was usually recruited second was occasionally the first to respond and could then be activated repetitively for some seconds without any activity in the first unit. These changes in recruitment order seemed to occur randomly. None of the subjects could, on demand, activate unit 2 at will or alternate the activity of the two units in sequence."

4. (pg, ln 29) "and appears to remain robust in various scenarios [21], [22]". There would seem to be other citations, perhaps even more relevant than [21],[22], that might be cited here. These include:

• Desmedt JE & Godaux E (1977). Ballistic contractions in man: characteristic recruitment pattern of single motor units of the tibialis anterior muscle. The Journal of Physiology 264, 673-693.

• Thomas JS, Schmidt EM & Hambrecht FT (1978). Facility of motor unit control during tasks defined directly in terms of unit behaviors. Experimental Neurology 59, 384-397

• Thomas CK, Ross BH & Stein RB (1986). Motor-unit recruitment in human first dorsal interosseous muscle for static contractions in three different directions. Journal of Neurophysiology 55, 1017-1029

• Thomas CK, Ross BH & Calancie B (1987). Human motor-unit recruitment during isometric contractions and repeated dynamic movements. Journal of Neurophysiology 57, 311-324.

• Jones KE, Lyons M, Bawa P & Lemon RN (1994). Recruitment order of motoneurons during functional tasks. Exp Brain Res 100, 503-508

5. (pg 14, ln 5) "This indicates that subjects experienced difficulties in keeping MU2 active while MU1 is inactive in order to reach TIII when their difference in recruitment threshold was large". "Large" is a relative term. Indeed, the actual difference in recruitment thresholds was quite small, on the order of only 6 – 10 % MVC. Perhaps instead state something like "when their difference in recruitment threshold was relatively large (6 – 10 % MVC)."

6. (pg 10 ln 27 ) [This is a minor point and needs to be addressed only if the authors wish to] "in 64.73% a selective MU was de-recruited at a force level below its initial recruitment threshold". One likely explanation for this is that during the decrease in force phase, subjects slightly increased activity of the antagonist muscles (De Luca CJ & Mambrito B (1987). Voluntary control of motor units in human antagonist muscles: coactivation and reciprocal activation. J Neurophysiol 58, 525-542). Even a modest degree of antagonist activity would cause the net (measured) force at derecruitment of a MU to be somewhat less, even though the muscle (TA) force might still be the same as at recruitment (Patten C & Kamen G (2000). Adaptations in motor unit discharge activity with force control training in young and older human adults. Eur J Appl Physiol 83, 128-143; Fuglevand AJ, Dutoit AP, Johns RK & Keen DA (2006). Evaluation of plateau-potential-mediated "warm up" in human motor units. The Journal of Physiology 571, 683-693)

7. (pg 19 ln 4) "An inhibitory input is needed to extinguish the impact of PICs on the MU discharge behaviour." A citation should probably be included here.

8. (pg 21, ln 1) "but also other motor behavioural changes, including alternations in postures [36], and contraction speed [15], are well known factors that impact the recruitment order." However, plenty of other studies suggest that these factors have little clear-cut effect on recruitment order (see citations under point 4 above).

9. (pg 21, ln 3) "changes in a MU pool's discharge activity imposed by such behavioural changes were recently confirmed". The word "confirmed" is far too strong. The paper cited has not undergone peer review. Moreover, the results of that manuscript are questionable for several technical reasons. Suggest change "confirmed" to "suggested".

10. (pg 21, ln 10) Paragraph beginning "A recent study in humans provided evidence for the existence of MU pool synergies" seems somewhat ancillary to the main topic of this paper and could be eliminated.

Reviewer #2 (Recommendations for the authors):

1. Because the findings depend on the reliable isolation of single MUs, the authors should provide additional characterization of this process. (A) Please show a segment of raw data (as in Figure 1, lower middle inset) with the spike times for selected MUs highlighted. (B) Provide more details on quality metrics (such as the rate of agreement with manually-curated offline decomposition, as in ref. 25) or criteria (even if these are qualitative). A sensitivity analysis to determine whether the main results are robust to more stringent isolation criteria might also be useful.

2. Ideally, readers should be able to interpret the figures with minimal reference to the text or caption. To this end, additional annotation in Figure 3A and 4 indicating that the y-axis corresponds to the higher-threshold unit would be useful. Similarly, in Figure 5A, please provide additional annotation for Conditions I-III (e.g., "low-low," "high-high," and "low-high"), as well as labels for the Y axes of the confusion matrices (e.g., "intended target" or similar). I would also recommend a uniform color scheme for the entries in the confusion matrices in Figure 5A (e.g., a monochromatic scale with limits of 0-200%), to allow an easy graphical comparison across rows, columns, and conditions.

3. Please show a scatterplot with the TIII hit rates on TIII-instructed trials vs threshold difference for all pairs.

4. A more explicit description of the decoding scheme would help. It appears that x-y cursor positions are weighted averages of MU1 / MU2 discharge rates over the previous second; this could be stated more directly, and additional filtering procedures, if any, described.

5. Figure 1: the "green arrows" indicating the electrodes in the caption do not appear to be in the panel.

Reviewer #3 (Recommendations for the authors):

None

Reviewer #4 (Recommendations for the authors):

1. Since papers in eLife are aimed toward a broad readership, the writing could be clearer at certain points. For example:

a. The acronym DR is never spelled out.

b. The term buffer is confusing.

c. Some statements were a bit vague. For example, page 3, line 12-14; page 7, line 18-19; page 21, line 27-28

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The control and training of single motor units in isometric tasks are constrained by a common synaptic input signal" for further consideration by eLife. Your revised article has been evaluated by Tirin Moore (Senior Editor) and Andrew Pruszynski (Reviewing Editor).

The manuscript has been substantially improved but there are some remaining issues that need to be addressed, as described below:

1. There remains some concern about the validation (required revision #1 in the previous review). First, it would be good to show in a scatter plot the agreement fraction during recruitment vs. derecruitment as calculated for the common MUs (instead of reporting the average epoch-specific fraction across all MUs). Such a plot could highlight any consistent bias between the two epochs. Second, it is unclear how you decide on common MUs. Is this decision related in some way to the agreement fraction? If so, this appears to be a bit of a circular argument. Please explain why it is not circular in the manuscript.

2. The title needs to be modified to accurately reflect the main findings of the study. Specifically, please remove the word synaptic as the precise mechanism is ultimately unknown in recruitment and de-recruitment. One possibility might be: "The recruitment of single motor units in a trained isometric task is constrained by a common input signal"

3. Similar to above, the end of the abstract should also be modified to ensure it accurately reflects the bounds of the paper. The last three sentences are presently:

"These strategies rarely corresponded to a volitional control of independent input signals to individual MUs. Conversely, MU activation was consistent with a common input to the MU pair, while individual activation of the MUs in the pair was predominantly achieved by alterations in de-recruitment order that could be explained with history-dependent changes in motor neuron excitability. These results suggest that flexible MU control based on independent synaptic inputs to single MUs is unlikely."

Suggestion to clarify: First sentence: "… independent input signals in individual MUs during recruitment/onset of muscle activity". Last sentence: "These results suggest that flexible MU recruitment based on independent synaptic inputs to single MUs is unlikely, although de-recruitment might reflect either varying inputs or PIC"

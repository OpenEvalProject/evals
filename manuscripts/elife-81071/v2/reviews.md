# Peer review - Round 1

Editors:
- Marco Capogna, https://ror.org/01aj84f44 University of Aarhus Denmark

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81071.sa0](https://doi.org/10.7554/eLife.81071.sa0)

This article contains fundamental findings that substantially advance understanding of an important research question, mostly using an appropriate and validated methodology in line with the current state-of-the-art, with good and convincing support for the claims. The message of the article will have a profound and lasting influence on neuroscience.


---

# Peer review - Round 1

Editors:
- Marco Capogna, https://ror.org/01aj84f44 University of Aarhus Denmark

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81071.sa1](https://doi.org/10.7554/eLife.81071.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Postsynaptic burst reactivation of hippocampal neurons enables associative plasticity of temporally discontiguous inputs" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Further discuss the relationships between burst and DA timing.

2) Acknowledge the relatively non-physiological concentration of calcium used and discuss its influence on the interpretation of the data.

3) Consider including a number of editorial changes as detailed by Reviewer 2.

4) Improvements in methods and statistical analysis, as suggested by reviewer 2.

5) Strengthen the link between the in vitro STDP data as commented by reviewer 3.

Reviewer #2 (Recommendations for the authors):

1. The so-called "Hebbian pairing protocol" (e.g., p 4) is not Hebbian. Donald Hebb famously never mentioned synaptic weakening in his books; he only spoke of synaptic strengthening. Also, his postulate also speaks of a cell A that along with a set of other presynaptic cells elicits the spiking in the postsynaptic cell B and how this leads to the strengthening of the connection between A and B. In other words, A necessarily fires before B. In spike-timing-dependent plasticity, the tLTP window is therefore consistent with what Hebb predicted, whereas the tLTD window is neither in disagreement nor agreement with his postulate. Rather, it is an extension of Hebb's postulate. Therefore, the authors should not call this "Hebbian pairing", because it is not. They could, however, call it "spike pairing", "correlated firing", "acausal spiking", or some such thing.

2. It is unclear what is supposed to drive the postsynaptic activity during reactivation, and also when. During sleep? For example, p8 "During DA, information is allocated to primed synapses without the need of further coincident pre- and postsynaptic activity, but by reactivation of the postsynaptic neuron alone." Please clarify here and elsewhere. Please generally try to elaborate on this.

3. The statistical treatment is at times unclear. For example, in Figure 8, "Permutation t-tests with Benjamini-Hochberg correction", but to what value was the false discovery rate set, and how was this value determined? Figure 8F, Stats for React in 4 done over all bins or just 4-8? If the latter, how was this selected for? Same in Figure 8-S1.

4. Electrophysiology methods are at times unclear. Why were the slice experiments carried out at 24-26 {degree sign}C? Why not a more physiological temperature, which is what most labs do? Maybe the eligibility trace decays faster at more physiological temperatures? This would reduce the biological plausibility of this candidate mechanism. P12-19 is not a very mature age. Why were the experiments not carried out in mature animals? I am concerned that these findings might be particular to juveniles. Page 19, "monopolar stimulation electrodes were placed in stratum radiatum", but how far from the recorded CA1 cells? Stimulation too close to the recorded cell is known to possibly activate neuromodulatory fibres such as DA or ACh, which could affect the outcome. Please clarify. It is not immediately clear how many bursts were used. Figures indicate only one arrow, yet the methods state "5-6 bursts" were used, but then later, it says "by somatic current pulses via the recording electrode (5x 1.8 nA, 10 ms each)", where 5x would indicate five bursts. The authors need to be clear in the figures about the precise number of bursts and how many spikes each burst carried. P20, "digitized at 5 kHz", and so filtered at 2.5kHz as per the Nyquist criterion? Please state. P21, R_s selection is unclear, "Series resistance was monitored (10-15 MΩ)", surely the R_s wasn't always <15MOhm, esp. if it could change by as much as 30%, so I am not sure what this means. What was the pipette resistance measured to?

5. Modelling could be clearer. P 22, "tau_e = 10 min is the eligibility time constant. " Where does this value come from? Please justify. P 21, "(α_intrinsic is taken as 0 unless otherwise stated)", please clarify what this means and why it would sometimes be not zero. P26, "Experimental data and code are available at https://github.com/ …" I cannot evaluate code that is not made available.

6. Why is the priming done with post-pre and not pre-post pairing? Conceptually, this part is entirely unclear to me. (related to Major Point 1) Is this choice of timing explained somewhere and I missed it?

7. I struggle with evaluating Figures6 and 7. I simply do not understand what is going on. For example, F7Aii top, Instructive Neurons, is completely blank. The same thing in Bii, Supervised neurons. Why show empty graphs? Why show things that are not talked about in the figure caption text? Figure 8 is also quite unclear.

8. Control experiments seem to be missing or are perhaps just not consistently shown. Please clarify.

– Control experiments (i.e. control pathway) are clear for Figure 1 but are they missing or just not shown elsewhere?

– In Figure 5, Stability control with just anisomycin application seems to be missing too.

– Anisomycin has been shown to result in "profound suppression of neural activity" in the hippocampus (Sharma, Nargang, Dickson, JN 2012), which can affect STDP pairing. Have the authors compared the effects of anisomycin on AP parameters, possibly with anisomycin wash-in?

– Anisomycin can also potentiate JNKs (Iordanov et al. Mol Cell Biol 1997), which are important in synaptic release (e.g. Natisco et al., Sci Rep 2015, Abrahamsson et al., Neuron 2017). It may therefore be helpful to use an alternative protein synthesis inhibitor to confirm the results.

Reviewer #3 (Recommendations for the authors):

It would be informative if the authors vary the timing between priming and dopamine application. In their previous work where they used continuous stimulation in the presence of dopamine (Brzosko et al., 2015), a successful potentiation occurs if dopamine is applied immediately after STDP pairing, whereas with a 10 min gap no change is observed. Is the timing between pairing and dopamine application critical or rather the synaptic stimulation (bursting in this case) in the presence of dopamine the point?

Since MPEP blocks presynaptic LTD, it is surprising to me that the amount of potentiation is comparable whether MPEP is present or not (figure 1F vs figure 2A). Any explanation?

Unlike the parts for electrophysiology, the calcium imaging and the navigation-reward task sections are not provided with ample details.

To have a better comparison, the average percentage of reactivated cells at any pair of locations in the maze needs to be calculated. The same analyses shown in Figure 8 need to be done for the locations without rewards.

Page 25: "… The chance level was calculated by circularly shifting the activity with regards to the actual location." Why was circularly shifted activity with a delay used instead of randomly shuffling the activity with regards to the actual location? By shifting, some information still remains in the activity.

Is the increase in the spatial information of a neuron correlated with the temporal gap between its activity during the mice approach and its reactivation at the reward location? On average, does a shorter time gap correlate with a larger activity peak in the following trials?

The reference for Csicsvari et al., has been repeated twice.

# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66225.sa1](https://doi.org/10.7554/eLife.66225.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors provide evidence that fluctuations in ionic current through the open pore of a mutant acetylcholine-receptor ion channel are correlated with current transients during pore opening/closing conformational changes. The data are of good quality, and their rigorous analysis suggests that pore gating is coupled to fluctuations of ion conduction. Although the observations must be extrapolated to wild-type channels, they will be of fundamental interest to the ion channel community.

Decision letter after peer review:

Thank you for submitting your article "Unmasking coupling between channel gating and ion permeation in the muscle nicotinic receptor" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Marcel P Goldschen-Ohm as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kenton Swartz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Fred Sigworth (Reviewer #2); Angelo Keramidas (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) Main problem: You need to correct for the effect of the Bessel filter, whose rolloff looks a lot like a Lorentzian with cutoff near its cutoff frequency. You could use a complicated measurement of the system frequency response to correct the power spectra. Alternatively, here is a very simple method: connect the series combination of a resistor and capacitor between the headstage input terminal and the Vref (not ground) terminal. Good values are R = 20 to 50 megohms and C=.01 uF. The result is that you should measure the flat spectrum of resistor noise, spectral density = 4kT/R from ~1 Hz to high frequencies. You can then compensate for high-frequency rolloff by dividing your channel noise spectrum by the rolloff of this one, which should be obvious around 10kHz. The reviewers are happy to be contacted by the authors about how to do the spectrum calibration.

Further suspicion for an artifact is because there must be a flat spectral component extending up to the megahertz range due to shot and thermal noise in the channel. Even if your second Lorentzian disappears, the high-frequency asymptote of the spectrum might be interesting to compare.

2) Figure 8 – correlation of the low frequency component with the ON and OFF transients is visually somewhat ambiguous. Please show fits with the high frequency component only for comparison. This is doubly important if the high frequency component contains any artifact from the filter as discussed above.

3) The epsilon subunit mutation (Introduction). Where is it in the channel structure? Given its large effect on conductance and open time, why don't you think it will change the relevant behavior of the channel? It would be helpful for most readers if the authors could comment on the mechanism for this mutation in the text and briefly discuss what impact if any it might have on interpretation of the data with regards to WT channels.

4) Throughout: "wild-type" is misleading, as it should be epsilon-T264P.

5) Introduction. Please include sequence alignments of a few receptors in Figure 1 to show conservation of the salt-bridge across family and generality of the study. Also, please explicitly identify the residue position number of the acidic residue on M4 in the text.

6) Statements such as "These results localize the primary effect of the salt bridge disrupting mutation…" are model dependent, and the issue is with the word "primary". Which model do the authors have in mind? In the usual sequential model the open-closed behavior at saturating agonist is indeed due only to the final opening step; but is the change sufficient to explain (at least approximately) the shifted dose-response curve? Or is a substantial change in binding constants required as well? Similarly, the charge-reversal mutation DKKD is presented as nearly equivalent to the wildtype channel, but it is in fact a partial rescue, and the completeness of its rescue might best be evaluated with a model.

7) A related issue is the existence of a new, longer open time component at high agonist concentrations that is mentioned in the Results. Please show some data to give the reader an idea of its importance. Did this affect the saturating open probability calculations?

8) Fluctuations that are so slow (~1 ms) are unlikely to be arise from the breaking of a salt bridge that (one would expect) would leave a helix flopping in the breeze on a ~1 ns timescale. So there's something complicated going on here with slow rearrangements of the protein that have only small effects on the conductance. A discussion of the relation of these timescales to potential mechanisms would be helpful for many readers.

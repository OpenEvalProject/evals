# Peer review - Round 1

Editors:
- Klaas Enno Stephan, University of Zurich and ETH Zurich , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15719.023](https://doi.org/10.7554/eLife.15719.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Uniting functional network topology and oscillations in the fronto-parietal single unit network of behaving primates" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Klaas Stephan (Reviewer #1), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Van Essen as the Senior Editor. One other reviewer has agreed to reveal his identity: Nicholas Hatsopoulos (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary of manuscript:

This paper presents the results of graph theoretical analyses of a network of single neurons distributed over three cortical areas. Neuronal activity was recorded in three Macaque monkeys while they performed a grasping task. The recording activity was used to infer directed connections amongst pairs of neurons, and the resulting connectivity matrix served as the basis for subsequent analyses. The authors find that this single neuron network is modular and has not only a small world, but also a rich-club structure. Remarkably, rich-club neurons showed oscillatory synchronisation in the beta and low frequency (< 7 Hz) range, while the remaining neurons tended to show non-oscillatory synchrony. These results imply that topological and functional properties of single neurons are related, and that oscillatory and non-oscillatory interactions assume distinct roles at the network level.

Summary of reviews:

All three reviewers were positively impressed by the paper and agreed that it contributes some very interesting findings with potentially wide-ranging implications. However, they also had a number of methodological concerns which would need to be addressed in a revision of your paper. These issues may require additional analyses of your existing data.

The policy of the journal is to provide you with a single set of comments which reflect the consensus view amongst reviewers. These comments can be found below and are divided into essential or Major Issues, which must be addressed convincingly, and Minor Issues. We hope that you will find these comments helpful to further improve the paper.

Major issues

1) The graph theoretical analysis rests on the validity of the underlying connectivity matrix. The latter consists of estimates of directed functional connectivity, obtained from analysing cross-correlation histograms (CCHs) with regard to signatures of temporal precedence, including a correction for common driving input by subtraction of surrogacy CCHs. While CCHs are not an uncommon statistic in electrophysiology, we wondered whether your specific approach to extract directed functional connectivity estimates from CCHs has been examined and validated in previous literature? If so, it would be helpful if the respective references were provided and the evidence for the validity of this approach was summarised in the paper. If not, validation analyses would be required before the graph-theoretical results can be trusted. Ideally, this would involve "ground truth" simulations in which the method is (i) challenged to recover directed functional interactions that are known (face validity) and/or (ii) compared against alternative established measures of directed functional connectivity (construct validity), such as Granger causality.

This issue is important because, as straightforward as the present method may seem, the estimation of directed connectivity is a notoriously difficult issue, and it is now widely accepted that methods of functional/effective connectivity cannot be motivated by theory along but require careful validation.

2) Following on from the previous point, your method removes effects of common stimulus- or movement-locked inputs (although it needs to be clarified what event is used for aligning in order to generate the PSTHs) because the PSTHs reflect these stimulus- or movement-locked inputs. However, the method does not seem to account for common driving input to the two neurons that is not locked to the stimulus or movement onset.

3) Given that CCHs are sensitive to oscillatory behaviour in the neurons studied, the question arises whether this could induce a bias when comparing the connectional properties (derived from the CCHs) between neuronal units that show oscillatory versus non-oscillatory synchrony? Put differently, if estimates of directed functional connectivity were affected by whether or not the neurons in question show oscillatory activity, would this not lead, by construction, to systematic differences in the connectivity patterns of neurons with oscillatory versus non-oscillatory synchrony?

4) One unresolved question is whether the oscillatory correlations are cause or consequence of the rich-club network role of the respective neurons. You might be able to address this to some degree. Several previous studies have emphasized that oscillations in frontal and motor cortices have a transient nature (e.g. Murthy & Fetz J Neurophysiol. 1996; Lundqvist, Miller, Neuron, 2016). You could analyze your LFP recordings to dissociate oscillatory from less oscillatory periods and then investigate whether the same neurons still show the same or different rich-club role.

5) In the ACHs and CCHs, the energy of a given frequency bin is distributed over all time bins, e.g. a beta rhythm leads to multiple peaks and troughs across the width of the ACH or CCH. This diminishes the sensitivity of the statistical testing for oscillatory correlations. It seems possible to improve the analysis by first performing a Fourier transform on the ACHs or CCHs and then performing statistical testing. Currently, you first statistically test ACHs and CCHs in the time domain, and only forward the correlograms with significant clusters to Fourier transformation and statistical testing in the frequency domain. This approach might miss many significant oscillatory correlations.

6) Materials and methods section: Network analysis subsection: Oscillatory synchronization with time lag can result in ambiguous CCHs, in which it is not clear which unit is leading and which is lagging. Can you essentially exclude this ambiguity in your data, e.g. because leads/lags are only a small fraction of the cycle, or because maximal peaks exceeded the next higher peaks substantially?

7) Similarly, it is difficult to understand the interpretation of a cross-correlation peak at time zero as indicative of a bidirectional connection. It seems more likely that this is due to common input from another third neuron. How can one interpret a zero time-lag peak as indicative of bidirectional interactions?

8) You analyze distance dependency by defining distance in categories like “same electrode, “same array" and “same area". In an additional analysis, distance should be defined as actual physical distance. Figure 3 shows that some electrode pairs between F5 and M1 are closer than some other pairs within M1. Physical distance has been shown before to explain a substantial fraction of the variance in neuronal correlation.

9) It would useful to know what kind of time leads/lags were observed among significant cross-correlation histograms. Given that you are looking for significant cross-correlation peaks at time leads/lags spanning +/- 200 ms, if the peaks occurred at very large time leads/lags approaching 200 ms, in what sense are the two neurons interacting physiologically?

10) Material and methods section: Frequency analyses subsection: You remove sharp peaks with small delays with the argument that they would cause distortions. However, such sharp peaks constitute important data and must not be removed, unless they are due to artifacts. If you wish to argue that the sharp peaks are artifacts, evidence needs to be provided. Otherwise, they should be included in the analysis.

# Peer review - Round 1

Editors:
- Manuel Zimmer, Research Institute of Molecular Pathology, Vienna Biocenter and University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56942.sa1](https://doi.org/10.7554/eLife.56942.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

To execute competent behaviours, animals have to select, time and orchestrate their individual actions into orderly action sequences. By studying the escape response of C. elegans, Wang and colleagues provide intriguing insights into the underlying neuronal circuit mechanisms. While excitatory electrical signalling between an interneuron and a motoneuron ensures the sequential execution of actions, mutual inhibition via chemical synapses affects variable choices and timing. Such a combined excitatory feed-forward and winner-takes-all mutual-inhibition mechanism might be a general principle by which larger organism also organise more complex action sequences.

Decision letter after peer review:

Thank you for submitting your article "Flexible Motor Sequence Generation during Stereotyped Escape Responses" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Piali Sengupta as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers were very enthusiastic about your manuscript and this decision has been arrived at following extensive consultation among them. The Reviewing Editor has drafted this decision to help you prepare a revised submission based on the detailed comments below.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments and/or analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option.

Summary:

In "Flexible Motor Sequence Generation during Stereotyped Escape Responses", Wang et al. use behavioral analysis, calcium and glutamate imaging, optogenetics and a biophysical model to investigate the circuit mechanisms that generate an action sequence, the escape response of C. elegans. First, the authors characterize the motor sequences triggered either by optogenetic activation of mechanosensory neurons ALM/AVM or via a heat stimulus. Using a biophysical model, they classify the escape response into distinct action patterns (forward-reverse-omega turn vs forward-reverse-forward). Then, the authors investigate the role of the AIB interneurons in the transition from reversal to omega turns and find evidence that gap junctions between AIB and inter/motor neuron RIV mediate this transition. The authors then investigate the role of inhibitory glutamate signaling from AIB to RIB, an interneuron upstream of RIV, in shaping the dynamics of the reverse/turn transition. Lastly, they look into the role of turning module neurons (RIV, SAA and SMB) and find some initial evidence supporting that these neurons promote reversal termination. These results strongly support a model for the generation of behavioral sequences: as opposed to a feed-forward excitatory synaptic chain mechanism, the authors propose a mechanism involving concomitant feed-forward excitation and inhibition together with feedback inhibition that enables a more flexible control of the action sequence. This model is very interesting and potentially relevant for our understanding of motor control in general.

Essential revisions:

1) Flexibility of the escape response is observed in two ways: variability in the timing of behavioral motifs, as well as the choice between transitions type I and II; these outcomes seem to be interrelated as was observed in previous work. This concept should be better introduced and made clear throughout the text.

2) The authors describe the escape response with an alternative choice between two discrete and distinct transitions (type I vs type II). Here, they rely on a cutoff at 135 degrees reorientation angle; although this cutoff was used a few times in the past literature, to date it seems largely arbitrary. Since this is a key step in their analyses convincing evidence should be provided that justifies this distinction. Is there a bimodal distributions of reorientation angles, supporting this cutoff, under the present experimental conditions?

Note, that Kaplan et al., 2020 (see Figure S5I) reported such a bimodal distribution but here the cutoff should be around 100 degrees; based on Pierce-Shimomura et al., 1999 (Figure 9) bimodality is less obvious and if at all supporting a cutoff of around 45 degrees. Moreover, Szigeti et al., 2016 makes a strong argument of a continuum in omega turns, hence no subdivision should be made at all. On the other extreme, Broekmans et al., 2016 suggest a third transition (δ turn). In the light of these different findings, the authors need to show whether under their conditions the distribution of post-reversal reorientation angles is indeed bimodal and perhaps determine a more objective cutoff to support such behavioral classification into transitions I (no turn) and II (omega turn).

3) Model: reviewer #1: The authors claim that "the statistics were better described by introducing two types of transitions and the corresponding transition rates r(t)." However, no evidence is provided that this model indeed outperforms alternative models, e.g. a single transition rate with a continuum of post reversal reorientation angles. Or a model without plasticity in inhibitory synapses. Please provide additional sophisticated analysis scrutinizing the favoured model against alternative hypotheses.

The biophysical model is largely presented as a black box throughout the main text and little guidance to the general reader is provided, so that one has to work through the supplemental note, which is very difficult for the non-modeling-expert to follow. Which components of the model were crucial to obtain good fits and does the final model really outperforms simpler/alternative models?

Reviewer #2: The model isn't well integrated into the main text. The model is referred to in the Discussion and in relation to Figure 7 but appears to have a tenuous connection at this point. Ultimately, it only provides a fit function for the time-dependent transition rate. However, the Discussion suggests that the authors want to give more weight to the model as a basis for understanding the underlying neural circuit.

There are a few issues with the model as presented in the supplementary note:

- Assumptions are stated but are not justified or tested for their impact on the conclusion. For example, the assumption of the white-noise inputs from other neurons and the ad hoc assumption that the synaptic inhibition decreases exponentially.

- In the end the function has 3 (4?) free parameters to fit a curve. We are not surprised that the fit quality is good, but from the sparse description of the model it is unclear if it adds anything that goes substantially beyond just fitting an error function to the data.

4) At present, this study provides no evidence of neuronal correlates distinguishing transitions type I vs II. Simply triggering activity to reversal starts, reversal ends, and turns has been done in previous literature. The difference in mean amplitudes of AIB activity (type I vs II) could support the continuous model equally and/or be simply a result of different reversal durations. Moreover, we are surprised that it is not shown how the activity of RIV during type I vs. II differ? How is AIB and RIV activity distributed and can one predict type I vs type II just from certain features in AIB/RIV activity?

5) The inx-1, unc-7, unc-9 triple mutant data are hard to interpret because UNC-7 and UNC-9 are broadly expressed and previous literature shows that these mutants have substantial locomotion defects, thus there could be pleiotropic and additive effects from mutating several innexins. This should also be made clear in the main text, since at present, the authors mention that "several innexin proteins including INX-1, UNC-7 and UNC-9, are reported to express in AIB and RIV inter/motor neurons" but do not mention that especially UNC-7 and UNC-9 are expressed broadly in most other neurons.

Similarly, paragraph two of subsection “Feedforward coupling between the backward and turning modules drives omega turns” read that the inx-1 mutants still execute omega turns, leading the authors to conclude that multiple innexins are at play. However, it could also be that multiple neurons are at play, this possibility cannot be ruled out at this stage. The reasoning for performing the calcium imaging of RIV during AIB activation in the triple mutants is not clear. Was this experiment performed in the inx-1 single mutants, which is more specifically expressed in AIB? If so, these data should be shown.

6) There is no consensus on what marks the end of an omega turn. Please provide the definition and justification for this study. Otherwise, Figure 3A and Figure 2—figure supplement 1B are difficult to interpret.

7) One thing that might be nice would be if they could address the issue of stochasticity a bit more in the Discussion. Do the authors have any speculation why the behaviour is not more deterministic? And does their model give any insight into turn and reversal coupling in unstimulated animals undergoing spontaneous reversals?

8) Language:

The type-I /type-II language makes the text hard to read. It would be much easier for readability if the two cases were using an abbreviation that connects to the behaviors, for example type-I could be called RF and type-II – RT. This way the reader doesn't have to remember a somewhat arbitrary assignment of I/II.

9) Introduction: “(…) but a deep connection between theories and experiments remains yet to be established”. What constitutes a “deep connection”? Text suggests the authors are claiming they are providing one, which we don't see based on how little the model is integrated in the main text.

10) Discussion: " Several mechanisms may explain the decay of the iGluSnFR sensor signal, one being a depletion of available vesicles for release at the presynaptic site, analogous to short-term synaptic depression". It would be relevant to name alternative mechanisms here.

11) Discussion: "(…) are thought to underlie several motor behaviors such as Zebra Finch singing" would benefit from more examples and citations.

12) Winner-takes all strategy:

While this aspect can be understood from the data, the winner-takes all strategy should be more explicitly connected to the data in the Results section and explained in the Discussion.

13) Materials and methods:

The extensive documentation of strains, primers, promoters is great, yet it is often unclear which method was used for each figure panel. The Materials and methods section could be improved by a finer substructure with more subsections within similar groupings of experiments, that were performed using different instruments (e.g. optogenetics).

14) For multi-color imaging the Materials and methods section should explain how camera alignment was achieved.

15) Data availability:

We found the code accessible online. The link is included in the transparent reporting form but should also be repeated in the Materials and methods. A statement that custom MATLAB scripts were used is insufficient.

16) The order of neuronal activations involved in the action sequence (forward – reversal – post-reversal turn – forward) showing concomitant activity of AIB with reversal neurons followed by activation of RIV with turning neurons SMD and then RIB was shown already for immobilized worms in Kato et al., 2015. Moreover, ramping AIB activity during reversal has been shown before in Luo et al., 2014; Kato et al., 2015; Laurent et al., 2015, all for freely moving worms. The relationships of interneuron activities with reversal starts in freely moving worms (Figure 2—figure supplement 1B) were all shown already in Kato, 2015 and multiple other studies. It would be fair to credit this work and thereby highlighting better what is really new to this present study.

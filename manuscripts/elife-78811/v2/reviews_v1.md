# Peer review - Round 1

Editors:
- Liset M de la Prida, https://ror.org/012gwbh42 Instituto Cajal Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78811.sa0](https://doi.org/10.7554/eLife.78811.sa0)

This manuscript presents a combination of in vivo recording and optogenetic experiments that together with modeling bring findings with important significance: inhibition is functionally present in the newborn frontal cortex having major effects on EEG dynamics. These important findings challenge the view on the switch in GABAergic excitation to inhibition and extend phenomenological observations to human infant EEG data. The strength of evidence is solid, with appropriate methodology used and only minor weaknesses noted regarding the human infant data.


---

# Peer review - Round 1

Editors:
- Liset M de la Prida, https://ror.org/012gwbh42 Instituto Cajal Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78811.sa1](https://doi.org/10.7554/eLife.78811.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Developmental increase of inhibition drives decorrelation of neural activity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission have agreed to reveal their identity: Sampsa Vanhatalo (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The manuscript by Chini et al., investigates emergent dynamics of neural activity during brain development, focusing on differences in the relative strength of excitatory and inhibitory neurotransmission. Using a combination of in vivo recordings and optogenetic experiments with computer modelling, the authors show that inhibition is functionally present in newborn frontal areas. They also describe how this process is dysfunctional in a mouse model of a neurodevelopmental disorder. The work challenges the simplified view of the switch in GABAergic excitation to inhibition. By phenomenologically comparing rodent and human infant EEG data, the manuscript may provide translational bridges with significant impact for clinical studies.

While there was overall consensus on the value of the study, issues arise in particular with the points listed below. We all agree that you will need to address these points specifically to warrant publication. Please, note that the next review round should reach a consensus.

(1) An issue related with EEG human data and in particular regarding how are they generated and analyzed. First, we are unclear about the real N and the type of recordings obtained from these infants. Second, we need to understand the selection of the frequency band (1-40Hz), since most data suggest that neonates have most of their signal power at <1Hz and there is very little contribution for >20Hz. We feel you should adhere to the most commonly used standards. Finally, we are surprised about the increase in slope with early maturation, which is not in agreement with earlier publications. Importantly, addressing these points is critical for your manuscript to advance to the next step. While we will be open to discuss the option of leaving human data out of the revised version, we feel they represent an important addition that increases the impact.

(2) A second concern is with optogenetic data in Figure 4. We have difficulties in understanding the number of units per mice and per group, as they refer to age. We feel the ranges of ages used should provide a consistent number of samples. We are also unclear about the statistical design, whether it is running longitudinally or not. We would like to see these parts clarified and improved and an appropriate statistical contrast for nested design implemented.

(3) We are unclear about the paradoxical effects of optogenetic activations of INs. This point will require clarification and possibly additional analysis.

(4) Finally, regarding the model we are not completely clear about the assumptions made, in particular regarding lognormal distribution of synaptic connection strengths. We feel that testing the effect of other distributions may improve the conclusion and better support the model.

Please, also go over the specific points raised in the individual reviews and address them all in your revised version and rebuttal letter.

Reviewer #1 (Recommendations for the authors):

Overall this is a nice paper which does a good job of exploring an important question using a broad range of different approaches. The focus on PFC and cross-species analysis are particularly novel and important. There are a few points which I feel could be clearer and some issues surrounding data in Figure 4 where a better picture of how the experiments were performed and analysed would be beneficial. Code is made available via GitHub in keeping with open access policy of the journal.

Abstract:

Claim that mechanism behind decorrelation of activity unknown is not strictly accurate, numerous factors have been shown to contribute, including sensory input, synaptic changes and developmental alterations in EGABA

Introduction:

Claim that SOM integrate before PV is not accurate. See, Pangratz-Fuehrer and Hestrin, 2011; Anastasiades et al., 2016; Daw et al., 2007. They make a similar claim in the discussion "Early inhibitory circuits have several peculiarities, including a predominance of inhibitory synapses by SOM+ INs". Again this is not supported by the data. SOM interneurons certainly have an important and unique role in early development. But this is not to say that PV synapses are less numerous or weaker (in fact one of the papers they cite shows that they are much stronger at P12 and have a 20% higher connection probability than SOM cells).

Results:

In the model of the local network do they include changes in GABAergic driving force (i.e reversal potential) or just the conductance? Although they provide evidence that GABA does not appear excitatory during early development, it does not mean that it may not be depolarizing and that EGABA may change across this period. This change could influence their results. Others have shown developmental changes in EGABA within the developing PFC and so this should be taken into account.

Could differences in baseline firing across P4-12 make it harder to detect inhibition at early ages due to a floor effect? Could this contribute in part to their observation?

Were any recordings made at P4 in Figure 4? If not, why not state P5-6 rather than P4-6?

In terms of the mice recorded at different ages. Were mice recorded at all ages in each time window? For example, at P11 there are 2 mice who show a very low modulation index but at P12 all the units seem to be strongly modulated, but there are only 2 data points plotted vs 4 at P11 and 7 at P10. Were only 2 mice recorded at P12, or do the data points overlap at certain ages? Overall, how many mice were recorded at each age?

In the methods for Figure 4 they state that laser power was "adjusted until it gave the desired response" how was this defined? Was there a difference in laser power across the different ages, could this account for differences in inhibition?

Figure S3B How were positive neurons quantified? Is this per slice or per animal?

Discussion:

While the strength of the inhibition exerted by INs increases throughout development, the ability of INs to control cortical inhibition does not qualitatively change with age. Already during the first postnatal week, inhibition of INs leads to a paradoxical increase in their firing rate.

This sentence could be a little clearer.

IN inhibition results in increased spike-train correlations even though, in the last portion of the optogenetic stimulation, IN display a paradoxical increase in firing rate. As could this. Is there a way that you could rephrase? Stimulation typically means to activate cells, whereas you are suppressing them. Even though there is a paradoxical increase in firing this occurs at the network level, this is not due to the direct effect of light and so the term "optogenetic stimulation" is not accurate.

Reviewer #2 (Recommendations for the authors):

1. As mentioned in the weakness, the authors should go into more details about the paradoxical effect. Why is not seen for optogenetic activations of INs, only for the optogenetic inactivations? Also, it would be good to bring in some citations of experimental and theoretical work (Sanzeni et al. eLife, Sadeh et al. J Neuro 2017).

2. The authors should really put their work in the context of other studies who have measured and analyzed spontaneous activity and discussed how it evolves over time. For e.g. the Lohmann lab proposes the existence of L and H events (low and high participation rate events observed in the primary visual cortex), see Siegel et al. 2012. In a modeling study with the Gjorgjieva lab (Wosniack et al. eLife 2021), they proposed a different mechanism that can lead to the desynchronization (or sparsification) of activity during development, where L events increase in frequency while H events increase. This should be at least discussed. In Leighton et al. (Curr Biol 2021) the Lohmann lab also talked about the role of inhibition (from SOMs) in development. Finally, an interesting study that should be discussed is Rahmati et al. (Sci Rep 2017) which also presents results on sparsification of neural activity in development and the connection to inhibition stabilization.

3. Can the authors discuss the use of lognormal weights in the model? What happens if they are constant or taken from a lognormal distribution? I don't doubt they come from a lognormal distribution in the real circuit, but it would be important for the model to point out why this is important, as many other modeling papers ignore this fact.

4. The authors should present a more extensive discussion of why decorrelation is something that the network might strive to archive and how this relates to the onset of sensory experience and the efficient processing of sensory information.

Reviewer #3 (Recommendations for the authors):

My review at this phase will only focus on the few items that I hope would help the authors strengthen the work:

(1) In your introduction, you note that E-I ratio is important in your context because it "is the hallmark of neurodevelopmental disorders, such as autism or schizophrenia". Please note that you are mixing periods in the lifespan: your work is on neonatal brain development, while those disorders are about toddler age (autism) or much much later in life (schizophrenia).

(2) The work is very strong with the case on early inhibition. I find it a bit confusing how the work starts from making a case why the slope of PSD curve (1/f exponent) should be taken as a relevant measure of E-I.

Why not move this part towards the end, just before you introduce the human data? After all, this component appears to have value mainly because it allows you to link your findings on inhibition to the human dataset.

(3) I find it a bit perplexing that you show increase in slope with early maturation. This is opposite to what has been published earlier, and what is the general finding among clinicians. The early EEG (from prematurity to the end of neonatal period) is characterized by a rapid/robust decline in the lowest frequency power ->this translates directly to a decrease of slope.

So there is something unexpected here?

(4) I would also like to understand why you select to analyse 1-40Hz while recent papers have clearly indicated that (i) neonates have most of their signal power <1hz, and (ii) there is very little to be found >20hz.

(5) The human dataset is elusive: You tell that you had N=1100 and N=42 infants (Figure 8 N=1110?`). This would be the by far largest newborn dataset ever published. BUT the papers you cite only have 71+42+40=153 EEG recordings (assuming that they are from different infants). Also, there is no information about the kind of recordings done from these infants.

So, in brief, the information about human data is virtually missing; please elaborate.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "An increase of inhibition drives the developmental decorrelation of neural activity" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

– Regarding human data: while we were overall positive, we still feel the human data may require some clarification in view of the previous concerns. We appreciated your argument that there is no change of slope caused by contribution at 20-40Hz, but they were based on mouse data only (Figure 1-FS1). If you could provide some sort of additional/control analysis on human data as supplementary material, we feel that could help. We would like to stress this is just advice that we leave to your consideration. Importantly, we feel that it would be useful to discuss your observations on changes in slope with early maturation in the context of earlier publications. Please, be sure you add text to the discussion addressing these and previously raised issues and caveats regarding human results.

– In terms of the optogenetic data in Figure 4, we feel some additional clarification is required specifically regarding the way data is represented (per trial not per mice), and potential issues of low N.

Reviewer #1 (Recommendations for the authors):

The authors seem to have addressed my previous comments on an earlier version of this manuscript. I still think their statements regarding the predominance and importance of SST cells are a little strong, and largely unnecessary given they don't study them in this paper, but I guess it is still a matter of debate within the field.

In terms of the optogenetic data in Figure 4, their explanation makes sense. It does however seem a little strange to plot 2 trials from the same animal as separate data points. Their analysis seems to account for this, but it does mean that the N is a little low for some time points. That said their new analysis accounting for only the top 50% of active units seems to show a very robust effect consistent with their observations and overall model of inhibition's role in the early network.

Reviewer #2 (Recommendations for the authors):

The authors have appropriately addressed all of my, and the other reviewers', comments. There are still a few typos which I'm sure will be fixed in the final version (e.g. line 707 in the version with tracked changes "such AS a transition in synaptic plasticity rules", line 653 the word In's should be INs (all capital)). Overall, this is a very nice paper that people in the field will enjoy reading.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "An increase of inhibition drives the developmental decorrelation of neural activity" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

As indicated in the previous decision letter, the editorial consultation on the issue regarding human data agreed to request that this would be addressed directly in the discussion. The decision letter stated "Importantly, we feel that it would be useful to discuss your observations on changes in slope with early maturation in the context of earlier publications. Please, be sure you add text to the discussion addressing these and previously raised issues and caveats regarding human results.". Please, consider this point carefully when providing a revised version. We specifically ask for the issues raised by the non-responding reviewer to be explicitly addressed in the manuscript. Please also note that eLife publishes reviews and decision letters together with manuscripts, so we prefer not to leave important issues unaddressed that were previously raised during reviews and consultation.

# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77578.sa0](https://doi.org/10.7554/eLife.77578.sa0)

In light of the ongoing emergence of volume electron microscopy connectomics, detailed morphologies at the nanometre scale for many neurons are now available, ready for functional and computational analysis. Building on these foundational resources, this work delivers compelling evidence that synaptic inputs onto the dendritic arborisations of readout neurons (MBONs) of the learning and memory system of the adult Drosophila melanogaster contribute with equal weight to the depolarization of the neuron, independently of their location on the arbor, a phenomenon known as synaptic democracy. These important findings establish the validity of computational models based on passive dendritic propagation for simulating fly brain circuits and highlight the differences between the much larger mammalian neurons that present active propagation strategies as part of their approach to synaptic democracy.


---

# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77578.sa1](https://doi.org/10.7554/eLife.77578.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The cellular architecture of memory modules in Drosophila supports stochastic input integration" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Albert Cardona (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please follow carefully the many detailed comments by the reviewers. To emphasize comments with regard to the caveats of using partially EM-reconstructed neuronal morphologies, and in the statements regarding electrotonic compactness.

Reviewer #1 (Recommendations for the authors):

Hafez and collaborators describe the construction and analysis of a computational model of a mushroom body neuron. The anatomy derives from a combination of electron microscopy reconstructions of MBON-α3 and also from light microscopy. The physiological parameters derive from publications that measured them, in addition to the author's own electrophysiological recordings with patch-clamp.

There are two main findings. First, the dendritic arbor of MBON-α3 is electrotonically compact, meaning, individual connections from Kenyon cells will similarly elicit action potentials independently as to where, spatially, the synapses lay on the arbor. Second, in simulation, exploration of changes in the strength of Kenyon cell inputs illustrate two possible ways to alter the strength of the KC-MBON physiological connection, showing that either could account for the observed synaptic depression in the establishment of associative memories. The properties of each approach differ.

Overall, the manuscript clearly describes the journey from connectomics and electrophysiology to computational modeling and exploration of the physiological properties of a circuit in simulation.

The discussion ought to be expanded to include the implications of two possible approaches to physiologically altering the KC-MBON synapse and the consequence of their combination in expanding the space of alterations induced by associative memory paradigms.

In general, the results are clear, but some details remain underdetermined and I have listed them below in the detailed comments. The introduction and discussion present some inaccuracies that can be swiftly addressed by the authors

Detailed comments:

Line 45: Language: "potential rewarding": potentially.

Line 49: Language: "cellular and circuit architecture contributes": architectures contribute.

Line 72: instead of 5%, the number of KCs active at any one time seems to be 6% as per Turner et al. 2008 and Campbell et al. 2013. What is the robustness of the analysis to this small change? Did you explore a range of possible single-digit percent KC activations?

Line 99: Aso & Rubin 2016 belongs with citations in line 95.

Line 122: "Drosophila" needs italics, throughout the manuscript.

The authors devise a computational model of an MBON using a neuronal arbor reconstructed from volume electron microscopy by Takemura et al. 2017. That paper details that only 93% of all synapses were connected to an arbor, and only 86% of the synapses had known pre- and postsynaptic arbors. For the MBON that was used for modeling, what was the fraction of terminal ends labeled as uncertain, and where these clustered or scattered across the arbor? Furthermore, the volume imaged with FIBSEM did not fully enclose the vertical lobe of the MB. Any estimate of what fraction of the chosen MBON's arbor is contained within the imaged volume? In other words, what analysis has been done here to ensure that the modeled arbor is representative of an MBON arbor in vivo, and what mitigating measures were taken to account for the potentially missing 14% or more of the arbor synapses and terminal dendrites?

The authors report using the 10XUAS-IVS-mCD8::GFP to label the MBON, so that they can then record electrophysiologically with patch-clamp. What is the effect of inserting so many mCD8 proteins (a large transmembrane protein) into the neuron's membrane on the voltage potential and action potential formation and transport? The 10XUAS is particularly strong. How does the morphology of the imaged neuron differ from that of the EM-reconstructed neuron, regarding calibers and amount of cable? For this purpose, a cytosolic GFP targeting the soma or nucleus and poorly diffusing into the arbor would have been far preferable, as the effect of inserting transmembrane proteins in neurons' membranes on resting potentials is well reported.

Line 155: average resting potential for the MBON is reported at -56.7 mV +/- 2.0 mV. In Hige et al. 2015a, cells were held at -70 or -60 mV. Nowhere does Hige et al. 2015a report on the resting potential.

Line 174: amplitude of action potentials was rather small, but in Hige et al. 2015a action potentials typically exceeded 200 pA. Is this what the authors mean by small? Just how small were the recorded action potentials?

Line 176: by small amplitudes and the explanation on the long neurite connecting the dendritic arbor with the soma, you mean that the signal is attenuated over long distances?

Line 179: how was the membrane capacitance calculated?

Table 1: 5 neurons were used. How do you know they are all MBON-α3? Has it been confirmed that the GAL4 line doesn't have stochastic expression among similar yet different sibling neurons of the same lineage? How many other MBONs innervate the tip of the α lobe and do any of them share neuroblast lineage with MBON-α3? The large differences in measured values listed in Table 1 could be explained by having measured similar yet different neurons. Did you run a battery of tests before and after the measurements to ensure the recorded neurons remained in good health throughout the measurement session? Such tests often consist in a ramp of current injections and the recording of the neuron's responses, which are then compared between before and after the experimental measurements of membrane properties (like the current step protocol of Figure 1F).

Line 184: why only 3 cells? In Drosophila, recording from e.g. 10 cells, all homologous cells across 10 individuals, gives e.g., 8 responding with excitation to a sensory stimuli with some variation and 2 responding with inhibition. There is a lot of variability in the responses. Recording from only 3 cells seems risky, statistically speaking. What justifies this low number?

Line 186: "To to further".

Line 199: when you say that the measurements are in "good agreement with prior recordings" of other neurons in Drosophila, what do you mean exactly? How similar, how far off, by what parameters?

Line 203: might as well mention that there were 948 reconstructed KCs synapting onto MBON-α3, so 5% is 50. Spare the reader remembering where the 50 was picked from. (If you correct this to 6%, would be 57 KCs). And you seem to not keep in mind that the KCs responding to a specific odor may be correlated in their synaptic connectivity strength onto MBON-α3. Data to this end may be included in Li et al. 2020 eLife where the whole mushroom body is reconstructed, including the olfactory projection neurons, so such correlations if any may be evident in that data set.

Line 210: a complete reconstruction of MBON-α3 now exists, from either the FAFB volume or the Hemibrain volume. In the methods you mention you used the Hemibrain data set for the axon.

Line 209: the 12,770 synaptic connections aren't "all", these are the ones reported from the anatomical reconstruction from volume electron microscopy. According to the source papers (Takemura et al. 2017) about 10% of all synapses are missing. An analysis of how these missing synapses impacts the structure of the arbor is absent from the paper.

In addition, sample preparation for electron microscopy with chemical fixation alters the fine anatomical details, including the length of terminal dendrites and the calibers of neurites throughout. See e.g., Korogod et al. 2015 eLife "Ultrastructural analysis of adult mouse neocortex comparing aldehyde perfusion with cryo fixation" and the follow up paper Tamada et al. 2020 eLife "Ultrastructural comparison of dendritic spine morphology preserved with cryo and chemical fixation". What measures were taken to correct or mitigate these artifactual differences with in vivo neurons?

Later, Figure 2F strongly supports the appropriateness of the model, yet, the above points merit discussion and even exploration: how much of the dendritic arbor can you miss and still get the same result? What does the response to current injection depend on, cable, number of synapses, synapse spatial location, cable calibers, tapering of cable? What cable truncations are tolerable? This is very important information towards future computational studies based on neuronal morphologies reconstructed from volume electron microscopy.

Figure 2 legend: what is the evidence that the "proximal neurite" in green in Figure 2B is the site of axon potential generation? Gouwens and Wilson 2009 pointed at a region anywhere between the root of the dendritic tree and half-way through the axon of the uniglomerular olfactory projection neuron they modeled.

Does the site of axon potential generation emerge from your model, or did you specify it in the model?

Why is the two-tailed non-parametric Spearman correlation the correct statistic to compare the modeled and the experimentally measured membrane potential in Figure 2F?

Figure 2 legend reads "see appendix" but there isn't any appendix to the manuscript?

Line 249: "the average number of synaptic contacts from a KC to this MBON is 13.47". This statement ought to be qualified: for the single MBON-α3 measured in Takemura et al. 2017, and with the caveat of ~10% of synapses potentially missing. You could just as easily apply a correction factor and say the average number is about 14.7 + 1.47 = 16.2. Would this change the outcome of your model?

Please don't use "PN" as an acronym for proximal neurite. First, eLife doesn't restrict the length of your test. Second, PN is an established acronym, universally across all neuroscience literature, for projection neuron. Plus, the "proximal neurite" (as per figure 2B) might as well be called the putative AIS (axon initial segment; pAIS for "putative") where the integration of inputs across the entire dendritic tree take place and the axon potential is initiated.

Figure 3H: in the measurement of "local dendritic section volume", did you correct for volume artifacts induced by using (in purpose!) an incorrect osmolarity of the buffers when fixing the tissue in the sample preparation protocol for electron microscopy? See Korogod et al. 2015 eLife and Tamada et al. 2020 eLife.

Line 291: "this value is in good agreement with in vivo data for MBONs". Please could you specify what this agreement is, how close, some details.

Line 293: in line with analyzing all KCs with exactly 13 synaptic inputs onto MBON-α3, what's the result of analyzing the voltage excursion from drawing random subsets of 13 synapses? (or 16 as per the correction, see above). Are the natural groups of 13 synapses different in their effect on the neuron's voltage than artificial groupings?

Line 299: inaccurate statement: "Given that ≈ 5% of the 984 KCs innervating MBON-α3 are typically activated by an odor". Instead, what is known from the literature is that, given the presence of the GABAergic neuron APL in the mushroom body which acts as the inhibitory unit of a winner-take-all configuration, only 6% (not 5%) of KCs simultaneously respond to any one odor. Plus when the APL neuron is inhibited, a huge double-digit percent of KCs are active in response to an odor.

Line 311: there is now far better evidence of stochastic odor encoding by KCs than Caron et al. 2013. See Zheng e t al. 2020 bioRxiv "Structured sampling of olfactory input by the fly mushroom body", and Li et al. 2020 eLife, and also, for larvae, Eichler et al. 2017 Nature.

Line 319: see also Baltruschat L, Prisco L, Ranft P, Lauritzen JS, Fiala A, Bock DD, Tavosanis G. Circuit reorganization in the Drosophila mushroom body calyx accompanies memory consolidation. Cell reports. 2021 Mar 16;34(11):108871.

Line 337: the differences in the somatic amplitudes may be significant statistically, but are they meaningful? In other words, the effect size looks like near zero. The real, and important difference, is in Line 345 where it is stated that "we observed some differences in the slope of the responses between the different tuning modalities (Figure 5J,K,L)."

Line 350: Scheffer et al. 2020 is not an appropriate citation for the statement "Te ability of an animal to adapt its behavior to a large spectrum of sensory information requires specialized neuronal circuit motifs". Rather, a textbook such as Kandel et al. Principles of Neural Science, or no reference at all, would be appropriate. You could also delete the sentence without loss.

Line 353: Drosophila must go in italics, it's a species name. Multiple occurrences throughout.

Line 356: through both short-term and long-term memory. A good example is Aso & Rubin 2016 eLife.

Line 359: note the olfactory system of the fly has a sort of "fovea", Zheng et al. 2020 bioRxiv.

Line 362: this sentence needs work, I am not sure what it means: "Individual flies display idiosyncratic, apparently random connectivity patterns that transmit information of specific odors to the output circuit of the MB."

Line 366: MBONs can only each be classified as approach or avoidance within specific behavioral paradigms. In different contexts, including different physiological states (e.g., hunger, satiation, others), the classification changes.

Line 381: prior work includes Tobin et al. 2017 eLife, where EM-reconstructed dendrites of olfactory projection neurons were modeled to understand the impact of dendritic arbor size on neuronal function.

Line 386: again, these numbers aren't precise. There's about 10% of missing synapses to consider, and potentially additional Kenyon cells. And some of the KCs, particularly those with low number of synaptic connections to MBON-α3, may have been connected in error.

Line 397: Strongest finding of this work: "The location of an individual synaptic input within the dendritic tree has therefore only a minor effect on the amplitude of the neuron's output, despite large variations of local dendritic potential." Would be best to surface it more.

Line 402: a comparison would be appropriate with neurons from the crayfish stomatogastric ganglion (STG) as described by Eve Marder lab's, with published findings such as neurons being electrotonically compact despite their large size in mature adult animals. For example, Otopalik et al. 2017 eLife "When complex neuronal structures may not matter", where the authors "quantify animal-to-animal variability in cable lengths (CV = 0.4) and branching patterns in the Gastric Mill (GM) neuron". And also Otopalik et al. 2019 eLife "Neuronal morphologies built for reliable physiology in a rhythmic motor circuit".

Line 406: you forgot to cite Jackie Schiller's work on cortical pyramidal cells and their tuft dendrites, some of which predates all the cited work in this statement.

Line 412: your model, as per Figure 2F, rather very closely matches the observed electrophysiological responses of the neuron under study. In what further ways could you model more closely match experimental observations? This would be very instructive to the reader.

Line 415: by ensembles of both KCS and MBONs, not just KCs, if you are including the memory part and not only the input representation part.

Line 416: for most of the paper, you quoted these papers to justify the 5% of KCs being simultaneously active in response to an odor. Now the range is shown as 3 to 9%. This discrepancy ought to be reconciled.

Line 422: again, nowhere in the manuscript so far did you detail in what way your simulation and experimental findings match those of prior experimental reports regarding neuron response and physiological properties.

Line 425: this statement is inaccurate. An individual KC does not encode for a single odor. That would almost never be the case even if a KC was single-claw, as in, exclusively integrated inputs from a single projection neuron: individual projection neurons rarely encode an odor; it's the population of projection neurons that does. Similarly, ensembles of co-active KCs together represent an odor, and do so more narrowly and accurately than the population of projection neurons that excited them.

Line 452: left unresolved remains the question of why would both mechanisms exist, as in, is the combination of altering the KC-MBON synapse and altering the PN-KC synapse better in some dimension than altering either alone? Does this relate perhaps to a possible dynamic nature of the olfactory "fovea" proposed by Zheng et al. 2020 bioRxiv as presumably static?

Line 466: what is standard fly food? Please define it. Choice of food affects very much behavioral assays, for example.

Line 476: no antigen saturation steps in the immunohistochemistry protocol? Please revise.

Line 505: what were the settings of the puller? These would be necessary to reproduce your glass capillaries. Did you grind the tips, and if so, how?

Line 534: how were the R_series, R_input and R_m determined with Igor Pro?

Line 561: why was a threshold of 600 MΩ used to exclude cells? How many cells were recorded in total, and how many were excluded?

Line 584: once again the data is the best human effort in proofreading a semiautomatic segmentation. It is not the absolute truth. Also, each individual fly is somewhat different, so this is merely one fairly complete yet partial reconstruction, and not assured to be error free, particularly of errors of omission, of a single MBON from a single individual. Would be appropriate to remark this clearly.

Did you provide the NeuroML or similar files necessary to run the model in the NEURON simulation software? These should be appended to the manuscript as supplemental data.

Line 596: if "parameters were tuned until the computed voltage excursion at the soma matched our electrophysiological recordings", what is the rationale for comparing the voltage potential of the simulation with those of the experimental observations?

Line 607: where do these ranges of physiologically plausible values come from? Citation, or measurements done in the lab and therefore a figure is needed to show them? Are these ranges from the literature listed in Table 2? Likely yes, would be appropriate to cite them here too or at least explicitly point to Table 2.

Line 616: innervation of MBONs is cholinergic because KCs are cholinergic, but that's not from Takemura et al. 2017, instead from Barnsted et al. 2016 Neuron.

Line 622: would be appropriate to include the python scripts used to configure and run the NEURON simulation as supplemental material. Likewise for the matlab scripts used to load the analyzed data and plot it. The raw data ought to be included as CSV files or similar.

Reviewer #2 (Recommendations for the authors):

"The cellular architecture of memory modules in Drosophila supports stochastic input integration" is a classical biophysical compartmental modelling study. It takes advantage of some simple current injection protocols in a massively complex mushroom body neuron called MBON–a3 and compartmental models that simulate the electrophysiological behaviour given a detailed description of the anatomical extent of its neurites.

This work is interesting in a number of ways:

– The input structure information comes from EM data (Kenyon cells) although this is not discussed much in the paper.

– The paper predicts a potentially novel normalization of the throughput of KC inputs at the level of the proximal dendrite and soma.

– It claims a new computational principle in dendrites, this didn't become very clear to me.

Problems I see:

– The current injections did not last long enough to reach steady state (e.g. Figure 1FG), and the model current injection traces have two time constants but the data only one (Figure 2DF). This does not make me very confident in the results and conclusions.

– The time constant in Table 1 is much shorter than in Figure 1FG?

– Related to this, the capacitance values are very low maybe this can be explained by the model's wrong assumption of tau?

– That latter in turn could be because of either space clamp issues in this hugely complex cell or bad model predictions due to incomplete reconstructions, bad match between morphology and electrophysiology (both are from different datasets?), or unknown ion channels that produce non–linear behaviour during the current injections.

– The PRAXIS method in NEURON seems too ad hoc. Passive properties of a neuron should probably rather be explored in parameter scans.

Questions I have:

– Computational aspects were previously addressed by e.g. Larry Abbott and Gilles Laurent (sparse coding), how do the findings here distinguish themselves from this work.

– What is valence information?

– It seems that Martin Nawrot's work would be relevant to this work.

– Compactification and democratization could be related to other work like Otopalik et al. 2017 eLife but also passive normalization. The equal efficiency in line 427 reminds me of dendritic/synaptic democracy and dendritic constancy.

– The morphology does not obviously seem compact, how unusual would it be that such a complex dendrite is so compact?

– What were the advantages of using the EM circuit?

– Isn't Figure 4E rather trivial if the cell is compact?

Overall, I am worried that the passive modelling study of the MBON–a3 does not provide enough evidence to explain the electrophysiological behaviour of the cell and to make accurate predictions of the cell's responses to a variety of stochastic KC inputs.

Reviewer #3 (Recommendations for the authors):

This manuscript presents an analysis of the cellular integration properties of a specific mushroom body output neuron, MBON-α3, using a combination of patch clamp recordings and data from electron microscopy. The study demonstrates that the neuron is electrotonically compact permitting linear integration of synaptic input from Kenyon cells that represent odor identity.

Strengths of the manuscript:

1) The study integrates morphological data about MBON-α3 along with parameters derived from electrophysiological measurements to build a detailed model.

2) The modeling provides support for existing models of how olfactory memory is related to integration at the MBON.

Weaknesses of the manuscript:

1) The study does not provide experimental validation of the results of the computational model.

2) The conclusion of the modeling analysis is that the neuron integrates synaptic inputs almost completely linearly. All the subsequent analyses are straightforward consequences of this result.

3) The manuscript does not provide much explanation or intuition as to why this linear conclusion holds.

In general, there is a clear takeaway here, which is that the dendritic tree of MBON-α3 in the lobes is highly electrotonically compact. The authors did not provide much explanation as to why this is, and the paper would benefit from a clearer conclusion. Furthermore, I found the results of Figures 4 and 5 rather straightforward given this previous observation. I am sceptical about whether the tiny variations in, e.g. Figures 3I and 5F-H, are meaningful biologically.

1) My biggest question is about the claim of extreme electrotonic compactness of this neuron. Figure 3D,E suggests that the voltage change at the proximal neurite and at the soma varies by only about 1% depending on stimulation location. Since this is supported only by simulation, it is worth asking how robust this conclusion is.

a) Given that the variability in 3I is so small in magnitude, any dependence would be swamped by other sources of heterogeneity, so the statement that this correlates with distance (line 278) is likely irrelevant.

b) Can the authors provide a confidence interval for the fit of biophysical parameters to their recordings?

c) On lines 271-274, the authors state, "This architecture with the smallest dendritic sections at the most distant sites may contribute to the compactness of the dendritic tree, ensuring that even the most distant synaptic inputs result in somatic voltage deflections comparable to the most proximal ones." Is a dependence of dendritic size on distance required for the results? It seems like the result is simply that there is no attenuation within the dendritic tree at all. In general, the authors don't actually provide an explanation for the compactness. In the discussion, it is stated that, "The compactification of the neuron is likely related to the architectural structure of its dendritic tree," which again is rather vague. The authors should strive to provide a clear explanation for this, since it is their key result.

d) Can the authors report what the electrotonic length for such a dendrite would be? How long before we expect to see a significant spread in 3E?

2) My other concern is that, once we assume this perfect integration, the subsequent analyses are all a straightforward consequence. In particular, Figures 4 and 5 just repeatedly convey that it doesn't matter which synapse is being activated, the effect on the somatic voltage is the same. I was particularly confused about the conclusions of 5F,G,H. The authors claim "small but significant differences" here, but practically speaking, I can't imagine any of the differences in these plots being meaningful.

3) Reference to the data used to constrain the model is confusing.

a) At various places in the manuscript references are made to in vivo recordings, but it appears that all of the recordings were done ex vivo.

b) On lines 389-392, the authors state: "Near-perfect agreement between experimentally observed and simulated voltage distributions in the dendritic tree shows that linear cable theory is an excellent model for information integration in this system." What recordings of the voltage distribution in the dendritic tree were performed?

4) It seems like the conclusions are different than those of Gouwens and Wilson (2009), who described their reconstructed PNs as electrotonically extensive. The authors should comment on what about MBONs and PNs is different.

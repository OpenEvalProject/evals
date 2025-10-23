# Peer review - Round 1

Editors:
- Silke Hauf, Virginia Tech United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66955.sa0](https://doi.org/10.7554/eLife.66955.sa0)

This paper will be of interest to developmental biologists and neurobiologists who study the molecular mechanisms underlying induction and maintenance of cell fate. A combination of cutting-edge molecular genetic approaches in C. elegans together with mathematical modeling suggests an interesting mechanism for life-long maintenance of neuronal identity and function.


---

# Peer review - Round 1

Editors:
- Silke Hauf, Virginia Tech United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66955.sa1](https://doi.org/10.7554/eLife.66955.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Mechanism of life-long maintenance of neuron identity despite molecular fluctuations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Attila Becskei (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) Additional experimental controls:

(1a) Age of animals needs to be controlled for

The different durations of treatment and recovery mean that animals are tested for ASE activity (using a chemotaxis assay) at different days of adulthood, ranging from two to six days after starting the experiment. Many cellular functions decline after a few days of adulthood (see for example Stein and Murphy, Frontiers in Genetics, 2012). Therefore, the author's conclusions could be influenced by a general decline in chemotaxis, and a general inability to recover CHE-1 expression in "older" adults.

It would be important to show a time course of NaCl chemotaxis through adulthood, covering the full range of ages tested in the different treatment regimes (the authors assume that CHE-1 stability and ASE function stay constant for the whole life of the worm, but this is unlikely to be the case). The authors may already have these data, but it is not very clearly presented.

In addition, if 3-4-day old adults are treated with auxin for 1-2 days, do they recover CHE-1 expression and ASE activity? If they cannot, this would rather suggest that the switch to the OFF state is a property of "old" ASEs. It is important to deconvolve the age component in these experiments.

(1b) Control for survival of ASE neurons required

In vertebrate systems (e.g. PMID: 30146154), inducible removal of a terminal selector in adult neurons often leads to cell death. It therefore seems critical to evaluate the percentage of ASE neurons that are still alive after auxin treatment and 48h recovery, in particular when there is no recovery. This control experiment will address whether the progressive decrease in the ability of CHE-1 to recover its protein levels (upon increased periods of auxin treatment) is related to ASE cell death.

(1c) Use of ethanol in controls required

Auxin is typically diluted in 0.25 % ethanol, and therefore 0.25% ethanol should be used in controls. Especially, since ethanol is known to affect animal physiology, gene expression and chemosensation. The current study seems to use "control" animals not exposed to 0.25% ethanol. The experiments shown in figures 1, 5, and 6 should include this important control. In line 133, the authors state that NaCl chemotaxis returned to wild-type levels after 24 hrs of auxin. However, based on Figure 1 and SFigure 1, NaCl chemotaxis did not quite return to wild-type levels, perhaps because the auxin-treated animals were exposed to ethanol, whereas the control animals were not.

(1d) Control for effect of the AID allele without auxin

The authors mutated the HD site in the context of the che-1::GFP::AID allele. Therefore, control che-1::GFP::AID animals with an intact binding site must be included in the analysis shown in Figure 7C, D, and E (and in Figure S5) to ensure that initiation of che-1 occurred normally in (ΔHD)p::che-1 animals. Previous studies have shown that the AID degron by itself (without addition of auxin) can generate hypomorphic effects that become severe over time (Kerk et al., 2017, PMID: 28056346). Hence, it is unclear whether the observed reduction in CHE-1::GFP::AID in (ΔHD)p::che-1 animals over time is an effect of mutating the HD site, or is caused by lowering the levels of CHE-1 due to the presence of the AID degron. If this control has been performed, it was not pointed out clearly enough.

(2) Substantiate the model or revise the conclusions:

Concerns about the current model were raised and need to be addressed. This could be through additional wet lab experiments, revisions to the model, changes in the text, or combinations of those.

Two weaknesses were pointed out in particular: (2a) that evidence for the CHE-1 reservoir is missing, and (2b) that the (direct) transcriptional autoregulation of che-1 underlying bistability is not (yet) well supported.

(2a) The evidence for the CHE-1 reservoir could, if technically possible, be strengthened by performing ChIP experiments to analyze whether CHE-1 still binds to its own promoter after induced CHE-1 depletion. Does CHE-1 relocate from the promoter of its target genes to its own promoter upon induced CHE-1 depletion? The authors state that crucial to this mechanism is that CHE-1 shows strong preferential binding to its own promoter compared to its other target genes, but this is somewhat contradictory to a previous study showing the affinity score of CHE-1 for its own promoters and its targets genes is similar (Etchberger et al., 2007). In the absence of any additional data, the conclusions should be toned down-for example in the abstract where the authors state "Fluctuations in CHE-1 level are buffered by the reservoir of CHE-bound at its target promoters".

(2b) It seems important to further clarify the mechanism of bistability:

The mathematical model describes a positive feedback through che-1 but does not take into account the highly relevant regulation by HD. A high feedback-independent (basal) expression of che-1 would preclude bistability even with marked nonlinearities ( Májer et al. 2015; Jaquet et al. 2017).

The che-1 mRNA remains fully expressed after 24 hours of auxin treatment despite the fact that che-1-GFP fluorescence disappears after 3 hours. Currently, the observations could also be explained by an alternative model in which the bistability arises in a feedback loop downstream of che-1, which would explain why the expression of target genes declines upon auxin treatment. This could be described as HD -> Che-1 -> Che-1 target genes and the latter ones generate bistability. Such a mechanism would be reminiscent of the GAL regulon in yeast (Acar et al., 2005). The Gal4 transcription factor activates the GAL target genes but the expression of Gal4 itself is not bistable. The bistability arises due to the regulators of Gal4 that feedback on the Gal4 activity.

This could be clarified by performing mRNA measurements also after a depletion lasting for 96 hours when the neuronal function (chemotaxis index) is fully lost.

If the che-1 mRNA level declines, the authors would need to update their model to separate the timescales of the che-1-dependent processes from the HD-dependent processes.

If the che-1 mRNA level does not decline even after 96 hours, there will be no evidence for a functional autoregulation of che-1 in the terminal state despite the presence of the che-1 binding site in the promoter. In this case, the mathematical model should be reduced to a minimum that would serve to explain the bistability and time series studies.

Reviewer #1:

Traets, van Zon and colleagues explore the determinants of the reversibility of neuronal cell fate determination due to the transcription factor che-1 in the worm C. elegans. For this purpose, they deplete the che-1 protein with an auxin-degron and follow the restoration of neuronal function after the discontinuation of the auxin treatment. The neuronal function, as measured by the chemotaxis index, is not restored provided the depletion period is long enough. At first glance, this experiment suggests that the autoregulation of che-1 is bistable.

Strengths:

1. The authors perform a transient depletion experiment, a quite useful method to detect bistability. The transient depletion experiment is a merit on its own since bistability is rarely detected (with appropriate methods) in the relevant literature. The transition to the off state upon the transient depletion indicates that che-1 is somehow involved in the bistability of ASE neuron cell fate determination.

2. The authors discover a new regulatory sequence the che-1 promoter targeted by the transcription factor HD, which is involved in cell fate determination.

3. They determined the values of che-1 parameters such as mRNA and protein half-lives. The methods they use are probably more reliable than the methods commonly used in the field.

Weakness:

1. The che-1 mRNA remains fully expressed even after 24 hours of auxin treatment despite the fact that che-1-GFP fluorescence disappears after 3 hours. This result suggests that there is bistability but it is not mediated through the (direct) transcriptional autoregulation of che-1 in the terminal neuronal state. However, the authors do model the direct positive feedback of the che-1 transcription factor. Bistability cannot arise in this system because of the high feedback-independent (basal) expression of che-1. The authors identify a new regulator of the che-1 promoter, the Otx-related transcription factor, which accounts for the high basal expression of the che-1 promoter in the terminal state.

All these observations could be explained by an alternative model in which the bistability arises in feedback loop downstream of the che-1, which would explain why the expression of target genes decline upon auxin treatment. Of course, it is possible that there is a bistable positive feedback through che-1 during the earlier stages of development but it becomes overshadowed by the Otx-related transcription factor (HD) in the terminal state, which is analyzed in the current experiments. Thus, the mathematical model and parts of the interpretation seem disconnected from the observations.

Reviewer #2:

In this manuscript the authors address the question of how a cell's identity is maintained even though it exists in a reversible, bi-stable state. Specifically, the ASE sensory neurons in C. elegans require sustained activity of the transcription factor CHE-1 throughout the life of the animal. CHE-1 autoregulates its own expression in a positive feedback loop, however, such positive-feedback loops can relatively easily switch between ON and OFF states. The authors show that indeed, both che-1 mRNA and CHE-1 protein have relatively short half-lives and are not present in great excess, meaning that normal fluctuations in gene expression could indeed result in spontaneous loss of CHE-1 expression. Using a CHE-1 degradation system to reduce CHE-1 for defined amounts of time, the authors show that CHE-1 expression can be subject to such bi-stability, raising the question of how this is prevented during the life of C. elegans. Using a combination of quantitative assays for mRNA and protein expression, precise genetic manipulations in vivo, as well as mathematical modeling, the authors propose a compelling explanation: even upon fluctuations that substantially reduce the level of CHE-1, the CHE-1 protein bound to its hundreds of targets provides a reservoir for continuous che-1 transcription, as CHE-1 binds preferentially to its own promoter relative to that of other targets.

The presented work is generally strong both conceptually and methodologically. The question is interesting and well-defined, the logic of the work is clear, and the methodology is of high quality. The main strength is the quantitative nature of the work, even more so considering this is all done in vivo. Overall, I think this paper provides insightful conclusions to generally interesting questions in gene regulation and cell identity. Below I raise one concern though, that requires an additional control in order to strengthen the conclusion that CHE-1 autoregulation is bi-stable.

The authors claim bi-stability of ASE identity and function by triggering degradation of CHE-1 for different lengths of time and asking whether CHE-1 and ASE activity recover, or CHE-1 switches to an OFF state. If CHE-1 is actively degraded with the auxin inducible system for one or two days, the ASE neurons lose identity and functionality; but after another day or two in the absence of auxin, both CHE-1 and ASE activity recover. However, if CHE-1 is degraded for three or four days, neither CHE-1 nor the ASE activity can be recovered, even after two days in the absence of auxin. The authors conclude that this shows that CHE-1 controls its own expression, and ASE identity, in a bi-stable manner.

There is one slight concern with these experiments and that is that according to my understanding, the different durations of treatment and recovery mean that animals are tested for ASE activity (using a chemotaxis assay) at different days of adulthood, ranging from two to six days after starting the experiment. Despite the authors often referring to C. elegans lifespan being about 2 weeks, many cellular functions decline after a few days of adulthood (see for example Stein and Murphy, Frontiers in Genetics, 2012). Therefore, the author's conclusions could be influenced by a general decline in chemotaxis, and a general inability to recover CHE-1 expression in "older" adults. The authors state that they assayed age-matched control animals, but these are not shown. A single control is shown in each panel, and it's unclear what the age of the control was.

In addition to a time-course of chemotaxis, it would be important to test whether older adults can recover CHE-1 expression (and ASE function) when faced with a shorter auxin treatment. Specifically, if 3-4-day old adults were treated with auxin for 1-2 days, could they recover CHE-1 expression and ASE activity? If they cannot, this would rather suggest that the switch to the OFF state is a property of "old" ASEs. This wouldn't invalidate the subsequent parts of the work, but would give a more accurate picture of what the contribution of the proposed mechanism is.

Reviewer #3:

This work studies how transcriptions factors control cell fate by focusing on terminal selectors – a type of transcription factors known to induce and maintain the identity of specific neuron types across species. Traditional studies have examined terminal selector function using mutant animals carrying alleles that eliminate gene activity from early development. Hence, it remains unclear how terminal selectors maintain neuronal identity in the adult animal in the context of post-mitotic neurons, which are inherently long-lived cells in all species. This paper combines cutting-edge molecular genetic approaches with mathematical modeling to study how the terminal selector CHE-1 maintains the identity of the chemosensory neuron ASE in the C. elegans nervous system. Previous studies have shown that CHE-1 is required to maintain its own expression, but the current paper examines whether such autoregulation is sufficient or additional mechanisms are involved for maintenance of ASE fate. To test this, the authors established an inducible system to deplete CHE-1 and assess effects on ASE function. They rigorously determined copy number and half-lives of che-1 mRNA and protein. Armed with this information, they performed sophisticated simulations of the CHE-1 switch to estimate its stability against stochastic fluctuations. These simulations led to the hypothesis that high stability of the ON state required that CHE-1 binds its own promoter stronger than that of its target genes ("target reservoir buffering" hypothesis), thereby making che-1 gene expression insensitive to stochastic decreases in CHE-1 protein level. Through precise genome engineering, the authors propose that an Otx-related homeodomain binding site is selectively responsible for che-1 maintenance, not initiation.

Additional analyses and controls are required to firmly test the hypothesis of "target reservoir buffering", which at present is not entirely supported by the experimental data.

Strengths:

This study employs cutting edge molecular, genetic and biophysical methods in combination with sophisticated modeling/simulations to study the molecular mechanism underlying maintenance of ASE fate.

The authors established a powerful system to deplete CHE-1 at will for different periods of time and then assess effects on ASE function, as well as on expression of che-1 itself and its target genes.

The authors go to great lengths (e.g., smFISH, FRAP) to determine copy number and half-lives of che-1 mRNA and protein.

They performed sophisticated simulations of the CHE-1 switch to estimate its stability against stochastic fluctuations. Such simulations gave rise to the interesting hypothesis of "target reservoir buffering".

One piece of data (Figure 5) strongly supports the hypothesis, albeit a single CHE-1 target gene was tested.

Elegant genome engineering identified a 130bp fragment responsible for che-1 maintenance when CHE-1 is depleted. Within this fragment, an Otx-related HD binding site is proposed to be responsible for che-1 maintenance.

Weaknesses:

The simulations do propose an interesting mechanism (target reservoir buffering), but this mechanism is only tested indirectly and for a single che-1 target gene (gcy-22). In addition, the conclusions would profit from additional controls: since in vertebrate systems inducible removal of a terminal selector in adult neurons often leads to cell death, it seems critical to evaluate the percentage of ASE neurons that are still alive after auxin treatment and recovery. In addition, control animals should be treated with the solvent for auxin, and effects of the AID-tag, independent of auxin treatment, should be tested.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for re-submitting your article "Mechanism of life-long maintenance of neuron identity despite molecular fluctuations" for consideration by eLife.

Your article is provisionally accepted. Two of the reviewers, Paschalis Kratsios (Reviewer #3) and an anonymous reviewer, were fully satisfied by your revision, but we would like you to consider the additional comments by Attial Becskei (Reviewer #1). If you agree with his comments, this would mean slightly revising your discussion and Figure 7-S2. If you do not agree, please provide a justification.

Please see the detailed comments below. We look forward to receiving your re-submission very soon.

Reviewer #1:

The authors attempted to address the divergent behavior of CHE-1 mRNA and protein. The sampling period for the FISH experiments was extended. However, the background fluorescence was reported to increase over time and mRNAs could not be distinguished from the background. Next, they used RT-qPCR. However, they were not able to detect the CHE-1 mRNA with RT-qPCR. Thus, it remains unclear whether the CHE-1 mRNA level remains high level. These experiments would have been critical to distinguish two versions of the model.

At the same time, they rely heavily on the findings of Leyva-Diaz et al., Development, 2019 who report on the autoregulatory effects of CHE-1. In turn, they modify the model and off rate (unbinding rate) of CHE-1 is decreased 1000fold due to its interaction with HD-1. Unsurprisingly, such dramatic stabilization of the TF-DNA complex leads to a relative stabilization of the expression state. Consequently, the modelled "bistability" is stochastic, strongly time dependent. Future experiments will have to confirm this hypothesis.

Most bistability models in the literature rely on a deterministic bistability, which is then converted into stochastic model, whereas the stochastic component due to the slow dissociation rate is dominant in the author's model.

Bistability is prominently discussed in this manuscript. Therefore, the reader would gain a balanced view and profit from an extension of the discussion, in which deterministic bistability is compared to stochastic bimodality (bistability). For this, they can use the previously mentioned references and/or Hermsen et al. (2011) Plos Comp biol. Whereas kinetic nonlinearities and the dynamic range (basal expression) dominate deterministic bistability, the low number of molecules and time scales (e.g. off-rates) are key determinants of stochastic stability. The distinction also matters from a formal mathematical viewpoint. While quite general proofs can be derived for the existence of deterministic bistability, this is hardly ever the case for stochastic models. Generation of a few trajectories does not prove that a stochastic model is correct or incorrect. Therefore, I suggest replacing the labels "correct / incorrect" in Figure 7S2 by some more phenomenological terms, such as congruent / incongruent.

Reviewer #2:

The authors have done a careful and thorough revision. My previous questions and concerns are resolved and I fully support this manuscript for publication.

Reviewer #3:

The revised manuscript is very much improved. The authors have done a remarkable job addressing my comments by conducting new experiments and improving the text.

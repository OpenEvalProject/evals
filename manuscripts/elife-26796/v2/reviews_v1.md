# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26796.032](https://doi.org/10.7554/eLife.26796.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Multiple sources of signaling noise in bacterial chemotaxis network" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

FRET technique is applied to study the contributions to demonstrate that variability in the methylation or cooperativity of the chemotactic receptor to contribute to signaling noise in the bacterial chemotaxis system. This extends previous studies which focused on gene-regulatory noise. To this end, the authors analyze mutants that are defective in methylation or in clustering. A theoretical framework, based on fluctuation-dissipation theorem (FDT), is used to interpret the data.

Essential revisions:

As you can see from the individual reviews, all three reviewers found the subject interesting and that the work has the potential to be of broad interest. However, some significant revisions are still required.

Please answer in detail all of the requests made by the reviewers. In particular, the following points were emphasized during the discussion:

1) Presentation should be improved in terms of motivation, schematics, and readability.

2) Additional controls are required more make sure that noise in single-cell FRET is really due to processes inside cells, e.g. by imaging background without cells (receptor-less strain not enough).

3) More rigor is needed in the theory development (best in an appendix), putting in context of previous FDT work in bacterial chemotaxis, and stressing novelty.

4) The main novelty is noise due to cooperative receptors, which is discussed only very briefly in paper. This claim would potentially require more elaboration (e.g. to separate receptor rearrangement from signaling noise). For the latter, receptor could be overexpressed or crosslinked to increase clustering. Theory is vague at best including Ising vs. MWC, 'adjustment' and 'rescaling' of data, and non-constant effective Temperature, and limits of applicability of FDT also need to be clarified.

Reviewer #1:

The aim of this paper is to experimentally demonstrate multiple sources of signaling noise in the bacterial chemotaxis pathway, as most previous works dealt with gene-regulatory noise. Using the in vivo FRET technique in the bacterium E. coli, the authors show that there are significant contributions to the noise from receptor methylation (shown previously by the Cluzel lab) as well as receptor cooperativity. For the former, the authors use receptor mutants in fixed methylation-like states without the adaptation enzymes CheR and CheB. For the latter they utilize the CheW-Χ2 mutant, where the adapter protein CheW does not lead to receptor clustering (but nevertheless signals to the downstream kinase). As a control, they also exploit cells without receptors to estimate the noise floor in absence of receptor signaling and adaptation. The results are cast in the form of the fluctuation-dissipation theorem (FDT), which, for near-equilibrium systems, says that the power spectrum of the equilibrium fluctuations equals the response to a (small) nonequilibrium perturbation. In practice, the FDT is often used to predict nonequilibrium behavior using only knowledge from equilibrium fluctuations. How this might apply to nonequilibrium systems is still subject of ongoing research. However, here the authors use the concept of an effective temperature to frame the nonequilibrium problem as an equilibrium-like problem. The negative sign of the effective temperature is interpreted as evidence for a strongly driven, nonequilibrium system. The topic of the paper is of general interest to people working in quantitative biology. However, there are a number of concerns regarding presentation of the results and derivation of the theory, which would need to be addressed thoroughly.

Major experimental issues:

Subsection “Role of receptor cooperativity in signaling noise”: The noise from receptor methylation has been investigated before [Emonet and Cluzel, 2008; Park et al., 2010], so that the main experimental novelty is the signaling noise from receptor cooperativity. What is the nature of this noise – fluctuations in the signaling state or rearrangement of receptor clusters? Is there any way to separate these? This novelty section is only 10 lines long.

Subsection “Fluctuation dissipation relation for receptor clusters” on FDT: There has been significant amount of work on FDT-like properties including [Emonet and Cluzel, 2008] and [Park et al., 2010]. In the latter, they talk about the fluctuation-response theorem. What is the difference, and how does the current work fit into the context of the previous works?

Figure 4 legend: The caption says that "adaptation deficient" cells were used to obtain response function in Figure 4A. But the response function shown in this panel overshoots and adapts. How can these be the adaptation-deficient cells?

Figure 4B, C: These panels show power spectra and response functions for both the non-adapting (B) and adapting (C) strains, but panel A only shows response function for one strain. Where is the other response function? Panel C shows three curves but legend only mentions two-line styles. What does "rescaled" in B and "adjustment" in C really mean (in plain English)? To obtain response function, a 30 μM stimulus was apparently used, but is result really independent of stimulus strength (as long as small), or does each case need to be adjusted or rescaled separately? The theory in Materials and methods seems to be developed used an oscillating stimulus. Does it matter what the stimulus looks like?

Figure 4D: For the FDT to make any sense, Teff should be constant (independent of omega), which seems to be the case when plotted as in panel D. But upon closer inspection, the blue curve changes from 2 to almost zero, so this isn't constant after all.

Major theoretical issues:

Introduction, fifth paragraph and subsection “Modeling activity fluctuations in the framework of fluctuation dissipation relation”, first two paragraphs (Materials and methods): both the Ising and the MWC model are used. Why both? Why not just use the simpler MWC model?

Subsection “Fluctuation dissipation relation for receptor clusters” on FDT: A major issue is that the theory is only described very briefly in the Materials and methods section, and that it is almost impossible to understand. Why is it not derived in detail, e.g. in the Appendix (which is currently only one page long). When looking through the literature, found paper Clausnitzer and Enders, BMC SB (2011), which also seems to derive response functions and signaling noises. How does the current work relate to their theory and predictions?

Another theory paper, [Sartori and Tu, 2015], says that the FDT breaks down or is violated in the chemotaxis pathway. Why is the FDT then used to study the chemotaxis pathway? Why do power spectra and response functions even match? Maybe the rescaling/adjustment really means that they don't match.

Reviewer #2:

This paper aims at quantifying beside the methylation/adaptive system whether receptors can contribute to the signaling noise of the chemotaxis network in E. coli. The authors use a robust technique based on the tandem FRET CheY-YFP and CheZ-CFP that has been well-established about more than 10 years ago. The technical improvement from older studies by the same group is that they now use a CCD camera to monitor fluctuations in the Fret signal at the single cell level. This single-cell approach allows them to monitor with great precision the temporal fluctuations in the levels of the signaling molecule, CheYp.

To some extent, this paper follows mainly the same plan as Korobkova et al. Nature 2004 and Park et al. Nature 2010. Although this paper could sound like an incremental contribution, in fact it is not. The main reason being that these initial Nature papers quantified the signaling noise in a very indirect way and have ignored the central role of the receptors; Colin et al. identified the cooperativity between receptors as a key source of the signaling noise. While I feel this paper should be published in eLife, I have, however, few concerns that need to be addressed to make sure that the approach is watertight and the conclusions are accurate.

1) The noise of receptorless strain still shows non-negligible noise at long time scale (Figure 1). Is the fact that the power spectrum is not flat at long timescale comes from photobleaching of the FRET pair? What is the photobleaching of the signal over the duration of the experiment? In other words what is the t1/2?

In any case it seems that it would be possible to normalize the power spectra of R(t) with the power spectrum from the receptorless cells in order to get rid of the unwanted noise due to photobleaching at long time scale. However, this procedure would change the current shape of the spectra at long time scale. How does photobleaching shape the power spectra of R(t) at long time scale?

2) Varying CheR level should change the relative importance of noise from the receptors versus methylation/adaptation. What is the expression level of Tar relative to [CheR] in this experiment? I am asking this because the adaptive pathway (methylation) becomes noisy only when CheR works at saturation in the ultrasensitive regime, as demonstrated in Korobkova et al. For example, if [CheR] is slightly larger than wildtype level the noise vanishes. It is therefore not enough to adjust the activity at half level to guarantee that CheR is within the saturation regime since several ratios of MeAsp/Tar/CheR can yield the same level activity. It is key in Figure 3 to know what are levels of Tar with respect to CheR levels if CheR works at saturation in order to draw a robust conclusion. Without this information, I don't find the main conclusion of the paper sufficiently supported: "These results demonstrate that long-term fluctuations in activity observed either with or without the receptor methylation system require cooperative interactions between receptors".

3) Overall I find the part of the paper on the FDT weaker because it does not bring pieces of information that we did not know before. Maybe part of it – if not all – should be move to the Appendix?

4) CheZ/CheYp cycle is not taken into account in the fluctuation-dissipation formula. The authors should either justify why or include it.

5) In order to apply the FDT, the authors should apply a stimulus small enough so that the response of the system is linear. But how do the authors make sure that they are in the linear regime? For example in Park et al. a small stepwise stimulus of 10nM of L-Aspartate (which corresponds to 1 microM of MeAsp), is close to the limit of the sensitivity of the system. Here the authors use a stimulus (>10 microM of MeAsp) that is an order of magnitude larger than that is expected to yield a linear regime. Similarly, in Martin et al. PNAS 2001 (ref 64), a great care is taken to be in the linear regime as well "We chose displacement amplitudes small enough to maintain the bundle in a regime of linear responsiveness". Again how did the authors demonstrate that 10 (or 30) microM of MeAsp stimulus would yield a linear response?

Reviewer #3:

The manuscript by Colin and coworkers use FRET to evaluate the dynamics of the chemotaxis system in single cells. There are several things to like about this manuscript. The authors consider one of the most interesting and well worked-out model systems in biology, and use more technically advanced imaging methods to make new discoveries. That in itself could make it of potentially broad interest. However, though I am quite familiar with stochastic analyses of bacteria, I did not find this manuscript easy to evaluate. In terms of novelty and importance I would defer to reviewers with more expertise in the specific topic. At this stage my concerns are mostly about clarification and presentation, and I do not feel comfortable recommending that the paper be accepted or rejected before these issues are explained.

First, the paper is just not written for a general audience. It jumps into the details of chemotaxis without much explanation or motivation. To make it appropriate for eLife would require much more explanations of the basic system, including cartoons, more descriptions of the mutants involved, stronger motivations of the questions, and a more clear emphasis of the importance of the findings. What were the surprises or big wins that scientists not working directly with chemotaxis should care about?

Second, I suspect the methods are solid, but that is hard to judge as a reader. The authors emphasize that there is a technical advancement because they no longer need to average out the FRET data over several cells, and show how the average of their single cells reproduces previous population results. That on its own in no way means that the assay is reliable in terms of the noise in single cells. I would like to see at least one paragraph describing the controls made to ensure that the noise is due to the biology, and not to imaging (heterogeneity in the evenness of excitation, camera noise etc.), to cell handling (that conditions are uniform in space and time etc.) or to reporter artefacts (that the FRET pair does not affect the circuit's behavior). Only once these controls are completed would it make sense to consider the biology.

Third, the FDT analysis is not clearly presented for a broad audience. The expected limitations of FDT analyses (thermodynamic equilibrium, or other special considerations that may or may not be satisfied in any particular system) are not really discussed, and the results will not be easy to understand for a broader audience (maybe not even for a specialized audience), e.g. the discussion of effective temperature. In my opinion the authors need to set up the question more clearly, explain the results in the language of biology or chemical kinetics rather than thermodynamics, and ensure that there is a clear narrative arc. The analysis currently comes across as a technical report for people already familiar with both the system and the analysis. I also found it odd that a recent paper from the Cluzel group was not discussed, since I believe that was the first paper showing that the fluctuation-dissipation approximation holds for some aspects of the chemotaxis system, despite an absence of thermodynamic equilibrium.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Multiple sources of slow activity fluctuations in bacterial chemosensory network" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai as the Senior and Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Please correct the FDT analysis, or move it to the Appendix, as suggested by the reviewer. In addition, please rewrite the Abstract accordingly.

Reviewer #1:

In this resubmission, Colin et al. have significantly improved the readability of the paper and the theory development in the new appendix, and they added further valuable experimental controls. Although entangled in the data, I particularly like that the origins of the slow activity fluctuations could be separated into receptor dynamics and amplification by extra simulations. Overall, this is a significant contribution to chemotaxis signal transduction and quantitative cell biology as signaling noise has not been treated much so far, and I recommend publication.

Reviewer #2:

The main experimental results of this work are interesting and novel, and they should be published in eLife. The authors have clarified some of the issues of presentations that I initially had. However, the section and discussion about the application of the FDT weakens the paper because it does not bring new information about the chemotaxis system itself, and most importantly because the data do not clearly support the FDT analysis. My recommendation is to either move the section about the FDT to the Appendix and then tune down the associated claim, or maybe better to remove it entirely. The rest of the analysis with the simulations associated with Figure 5 has the merit to illustrate the different sources of noise and helps with the clarity of the paper.

1) With inset of Figure 4B, the authors claim that the ratio T/Teff is ~ 1, which would imply that the system is at the thermal equilibrium. I quote: "The deviation of T/Teff from unity was within the range of estimations with measurement methods of similar precision": I think what this convoluted phrase means is that the deviation from 1 of the ratio T/Teff is not statistically significant. But then the error bars displayed in the inset do not include the unity, which should imply that the ratio is statistically different from unity. In fact, T/Teff is clearly not constant: it is about 0.5 for frequencies<10^-2 and above 1 (>1.5) at higher frequencies. Next, in inset Figure 4C the authors used a much larger scale to plot T/Teff and now claim that the deviation (<=-0.5) from 0 is statistically significant and is the signature of a negative feedback loop. To conclude, the authors do not apply the same statistical standard to these two different insets, which makes the FDT analysis questionable.

By contrast, in the cited Martin, Hudspeth and Julicher, 2001 (Figure 3C in Martin et al., PNAS 2001) the ratio T/Teff was randomly distributed above and below the straight line T/Teff=1 over an order of magnitude in frequency, and the error bars were all crossing the straight line T/Teff=1. In Martin et al., there is no doubt about the analysis and the interpretation of the data unlike this current work.

2) The FDT analysis may be more convincing if the authors could fit with a quantitative model the ratio T/Teff like it was done for example in the Martin et al. It should be doable because the authors seem to have a full model that includes the clustering of the receptors with the adaptation pathway.

3) More generally, even if the FDT analysis were more solid, as it currently stands it does not yield new and interesting insights about the biology of the chemotaxis system. We already know that the methylation/CheA system is an energetically active process and that the cooperativity of the receptors is not. Consequently, this analysis (if proven correct) is more like a control analysis and should not hinder the main experimental results of this paper.

4) Along the same lines, the Abstract should be rewritten because it does not provide the necessary background to understand what is actually novel in this paper. As it currently stands, the abstract is a little deceptive because it suggests that the authors' study is the first one to use the FDT to analyze the chemotaxis and signaling pathways in general. For example, the concluding phrase is particularly puzzling: "We propose that such fluctuation analysis could be generally applicable to cellular networks" Of course this approach is far from being new (see Bialek et al.; PNAS; Emonet et al. PNAS; Park et al. etc…).

# Peer review - Round 1

Editors:
- Oliver Hobert, Howard Hughes Medical Institute, Columbia University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19021.019](https://doi.org/10.7554/eLife.19021.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Pan-neuronal screening reveals asymmetric neuronal dynamics of AWC neurons is critical for thermal avoidance behavior" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you can see in the appended reviews below, all three reviewers value the quality and implication of your work. However, there were some substantial concerns about how this work has been framed and a number of other issues require clarification. None of these requested revisions require additional experimentation. Please address each reviewer’s point in detail. In no order of importance the requested changes are:

1) The authors lay claim to a "novel" method for neural-activity screening although the concept is obvious to those in the field and arguably has been "pioneered" – if one can call it that – previously by several other groups. This claim to a novel screening method mars an otherwise great scientific publication. The paper should instead strictly focus on the scientific findings of asymmetric roles for the AWCs in thermal nociception. Specifically, it is recommended that the authors remove the claim of novelty in developing a "pan-neuronal functional screening system" (Introduction, second paragraph) by looking at pan-neuronal calcium responses in response to stimuli. The concept is obvious but, avoiding such discussions, this "technique" was pioneered initially by Kato et al. in their 2015 Cell publication "Global Brain Dynamics Embed the Motor Command Sequence of Caenorhabditis elegans" wherein a pan-neuronal calcium signal is screened during fictive locomotory behavior and the active neurons identified through fluorescent reporters (Figure 1C of the Kato paper).

Furthermore, Venkatachalam et al. apply the very same idea to the worm thermosensory circuit in their 2015 publication "Pan-neuronal imaging in roaming Caenorhabditis elegans" uncovering 2 unnamed neurons labeled 62 and 18 (Figure supplement 3 of the Venkatachalam paper). A citation which is strikingly missing from the submitted paper despite being published in PNAS within the same issue as the Nguyen paper which Kotera et al. do cite. Further to this, Kotera and colleagues should cite the work of the Samuel's lab as it is a direct precedent to their own work and sets the stage for their newly published discoveries.

Altogether, the claim of a novel technique is a distraction from what is otherwise a great scientific paper.

2) The authors use several fluorophores that present odd choices given the availability of newer and better alternatives. This is not problematic but readers will be left to wonder why such choices were made. We recommend the authors address this upfront to direct readers to the alternatives.

Chief among these strange choices is GECO1.1. While an improvement on GCaMP3, GECO1.1 fairs poorly when compared to GCaMP6 (the new standard in the field) – please see both the original papers from Zhao et al. 2011 on GECO1.1, Chen et al. 2013 on GCaMP6, and the Neurophotonics comparison in 2015. Presumably the choice was influenced by when Kotera and colleagues began their work. Still, given the array of choices, readers should be advised of best practices.

Second, the Discosoma-derived proteins such as DsRed, DsRed2, and mCherry have long been known to have ill effects in worm and, recent yet to be published work by Monica Driscoll's lab show that neurons react poorly to these fluorescent proteins. For this reason, TagRFP is often used in place of DsRed.

Third, mNeptune has been superseded by mNeptune2.5 which provides a nearly 2-fold improvement in brightness – published in 2014 by the Lin lab at Stanford.

As stated, these are not major issues. The authors should simply address choices for best practices since readers have easy access to strains and plasmids that represent newer better alternatives to the ones used.

3) The authors discover several unreported neurons to be thermo-sensitive. They choose to focus on AWC, a neuron with multiple but conflicting publications stating its thermo-sensitivity. The readers are left to wonder why the authors forewent the more obvious choice of exploring the novel finding of unreported thermo-responsive neurons. The authors should address this choice. Perhaps another paper is forthcoming with their results for RIS. RMDV and SMDV activity (motor neurons innervating the head) are likely reflections of downstream head actions in response to thermal stimulus. This a simple loose end that can receive a quick mention.

4) The authors have developed an impressive imaging rig capable of delivering thermal stimulus. Presumably a future paper will cover this novel rig but for now, in the spirit of openness, the software should be released to the community for public use in an open source repository and not simply made available upon request. This also benefits the science by providing transparency in the algorithms used to identify neurons, resolve their activity, and the analysis used to assay neural activity and behavioral correlates.

5) The supplement should match up the reporters used in the paper with the neurons they were used to identify. As has been the case multiple times in our field, future papers may find that some of the identifications were erroneous. This will help in quick corrections to the knowledge base.

6) G/R ratio should be explicitly defined in Figure 1C, where it is first used, as opposed to Figure 2.

7) In Figure 1—figure supplement 2, the thermal stimulus should be marked on the individual graphs so as to make sense of the neural traces.

8) Figure 2—figure supplement 1 shows the poor S/N in AWC-OFF due to the G-GECO measurement against the srsx-3p::GFP reporter. The S/N vastly improves in Figure 2C. How was this accomplished? Did the authors interpolate AWC OFF and ON from their thermal responses and then measure their activity with no OFF/ON identification reporters present?

9) The AWC fates in nsy-1 and nsy-7 mutant background requires a citation (subsection “nsy-1 and nsy-7 mutations alter the functional asymmetry in AWC neurons during noxious thermal stimulation”, first paragraph).

10) The term "turn" (first mentioned in the second paragraph of the subsection “nsy-1 and nsy-7 mutations alter the functional asymmetry in AWC neurons during noxious thermal stimulation” and Figure 4) can have multiple behavioral definitions for worms. The authors should be explicit as to what they mean by "turn". Are these omega turns, short reversals that include turning behavior, simple left/right turns?

11) The type of statistical tests should be explicitly stated and justified alongside the data – not just in the Methods – so that readers can assess the implicit assumptions made when comparing measured distributions. Furthermore, claims of normal distributions should be backed by histograms or similar representations of the sampling. Worm behavior often deviates from normality and therefore non-parametric tests are often a more appropriate choice. This problem occurs in Figure 4, Figure 4—figure supplement 3, and Figure 5. The authors can switch to violin plots or similar such statistical representations to assure the readers that the sampling is indeed "normal".

12) There is no N provided for Figure 4. The sample size should be explicitly stated. Furthermore, reversal rate and pausing (Figure 4—figure supplement 1) appear to be different in a nsy-7 mutant background. Did the authors repeat the experiments with larger sample sizes to rule out a role for AWC-ON in reversal rate and pausing as a response to noxious thermal stimulus? The behavioral transition graphs in Figure 4—figure supplement 3 show a clear non-wildtype role for nsy-7 and, inferentially AWC-ON, in response to noxious heat. Yet, these findings receive only a minor mention in the Discussion. We would like some mention at the location where the data is shown as well.

13) Claims of behavioral adaptation (and lack thereof) to repeated thermal stimulus in Figure 4 should be backed by a goodness of fit regression to a linear or exponential model of adaptation – or a similar statistic. Scientific claims require stronger evidence than that presented.

14) On the figures, the error bars are labeled as 83.4% confidence level but presumably the CI is 95% and 83.4% is termed the corresponding "capture percentage". The correct term should be used.

15) Figure 5 fails to show not only the N for the variety of conditions tested but, also, the WT response to 150mA and 250mA laser stimulation. This leads to questions as to how AWC ON/OFF ablation was controlled in the statistical analysis of 150mA and 250mA laser stimulation. The authors should address this by showing the missing data and explaining how the statistical tests were performed.

16) The term "sedated" (Discussion, seventh paragraph) is inappropriate for levamisole-mediated paralysis. The worm's neurons are obviously still functional after application of levamisole. We suggest using the term "paralyzed" in place of "sedated".

17) The central claim that AWC_OFF was identified by whole brain recording is powerful, but the only data that shows whole brain recording in Figure 1 is in a regime where AWC_OFF is quiet. It would be helpful to show the whole brain recording data that actually uncovered AWC.

18) An impressive number of cells was identified. They mention using glr-1 expression patterns to help with cell identification, but a more detailed explanation of how they came to their cell identities would be useful.

19) In the text, they claim to have stable recordings for 60 minutes with this technique. This is an impressive claim, and should be supported by data.

20) Figure 5B has a typo. The data that correspond to the ablation experiments should be labeled as such.

21) The manuscript was overall quite poorly written which made it difficult to read. The rationalization about different 'hierarchies' in investigating mechanistic underpinnings of behavior was very unclear. After all, calcium imaging is hardly the best or most direct readout of neuronal activity. This was an issue in the Introduction but even more so in the Discussion. This is not the first paper in C. elegans or in any other system to infer neuronal functions from examining stimulus-evoked neuronal activity, and it is inaccurate to portray it as such and to not mention many previous similar reports (for C. elegans – for instance see work from the de Bono lab, Chalasani lab etc.).

22) The authors also do themselves a disservice by not discussing the previous pan-neuronal imaging papers in more detail. Papers from other labs reporting similar imaging methods should be introduced in more detail. In particular, the paper by Venkatachalam et al. from the Samuel lab which specifically reports pan-neuronal imaging of thermal stimuli in freely moving animals is not referenced at all.

23) Related to the above, please check references throughout. In many cases, references are missing altogether or the wrong references are included. For example, the role of AFD in thermosensation (Introduction, fourth paragraph) was first shown by Mori et al. in 1995. The Biron et al. 2008 paper is the wrong reference here as is the Kimura paper.

24) The authors indicate that the AWC transients shown in Biron et al. 2008 are similar to interneuronal imaging (Introduction, fourth paragraph). What data is this assertion based on? Please provide references.

25) The authors should reference the Zimmer paper when discussing the use of nuclear-localized GECIs (subsection “Pan-neuronal calcium imaging coupled with thermal perturbations reveals novel neural functions”, second paragraph) for pan-neuronal imaging.

26) Figure 1B – it would be useful to include in a supplemental what the identities of all imaged neurons are beyond just the few that are labeled. There are clearly neurons that appear to show temperature responses correlated with those in AFD but these are not labeled. There is also little information provided about neuronal identification beyond the description of a few markers that were used. Many of these markers are expressed in multiple cell types. How did the authors unambiguously identify neuronal nuclei? By position as well?

27) Figure 1C – it is important to clearly indicate that the scales on the Y axes are different or replot to place them on the same scale.

28) In the last paragraph of the subsection “Pan-neuronal calcium imaging coupled with thermal perturbations reveals novel neural functions”: The authors appear to be able to detect calcium transients in the AIY soma and refer to Clark et al. 2006 as having showed this before. However, Clark et al. 2006 specifically noted that AIY signals were detected only at a 'varicosity' in the AIY axons and that no signals were detected in the soma.

29) While the authors show a detailed pan-neuronal response map for stimuli in the non-noxious range in Figure 1, why isn't a similar map shown for the nociceptive stimulus which after all is the major topic of the work? This is a pretty strong stimulus – it is important to get an idea of how much of the nervous system responds to this stimulus, and whether there are more L/R asymmetries in the response.

30) Other groups have shown that sensory neuron responses can be driven by other primary responder sensory neurons. Do the authors know whether the AWC responses they observe are due to direct detection of the stimulus or whether AWC responses are being driven by other neurons, for instance AFD or even FLP?

31) Please comment why loss of both AWC neurons results in maintained reversals to 150 mA laser stimulus, but loss of just the AWC(OFF) neuron abolish it?

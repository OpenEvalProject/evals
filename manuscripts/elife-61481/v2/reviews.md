# Peer review - Round 1

Editors:
- Andrew P Carter, MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61481.sa1](https://doi.org/10.7554/eLife.61481.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Kinesin-binding protein (KBP) is an inhibitory regulator of certain kinesin family members. In this manuscript, you use cryo-EM to solve the structure of KBP on its own and in complex with the Kif15 kinesin motor domain. KBP binds and remodels the tubulin-binding interface of the kinesin, preventing interaction with the microtubule. Mutagenesis experiments validate the mechanism described by the structure, and conservation between KBP-sensitive kinesins is used to describe specificity of KBP binding.

Decision letter after peer review:

Thank you for submitting your article "The mechanism of selective kinesin inhibition by kinesin binding protein" for consideration by eLife. Your article has been reviewed by Cynthia Wolberger as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Hauke Drechsler (Reviewer #2); Hernando Sosa (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Kinesin-binding protein (KBP) is an inhibitory regulator of certain kinesin family members. In this manuscript, Atherton et al. use cryo-EM to solve the structure of KBP on its own and in complex with the Kif15 kinesin motor domain. KBP alone forms a TPR-containing α-solenoid, which unfurls to wrap around the Kif15 motor domain in the complex structure. By binding to (and remodeling) the tubulin-binding interface of the kinesin, KBP prevents any interaction between the kinesin and the microtubule, thus explaining the mechanism of inhibition. Mutagenesis experiments validate the mechanism described by the structure, and conservation between KBP-sensitive kinesins is used to describe specificity of KBP binding.

Essential revisions:

1) The claim made by the title concerning kinesin selectivity is a bit too bold. Resolving the structure allows the authors to put forward a hypothesis about the mechanism of KBP-selectivity, but this still needs to be tested/validated. Please adjust the title.

2) It is a bit odd that the authors used Cys-substituted rather than wild-type KIF15 for their study and that they do mention this fact in the Material and methods section only. The authors should disclose this properly in the text (maybe the authors could name their construct something like KIF156S (?) or similar throughout the text, to avoid any misconception) and discuss possible caveats associated with these substitutions. In particular:

A) Although, many studies of kinesin proteins have used cys-substituted constructs, at least one study (Andreasson et al., 2015) has reported functional differences between a kinesin wild type and the cys-substituted version.

B) Could the substitutions affect KBP binding? One substitution is in kinesin helix 4 which is in the middle of the KBP binding site.

C) Could the mutations facilitate the large conformational change observed in KIF15? e.g. by allowing unraveling of the loops connecting the kinesin H4 helix to the rest of the motor domain?

D) The KIF15 motor domain construct is cys-substituted but the KIF1A construct is not. Could the differences observed between the KIF1A-KBP and KIF15-KBP complexes be partially related to the mutations introduced in the KIF15 motor domain?

3) The experimental setup of data shown in Figure 5 and Figure 5—figure supplement 1 is inconsistent and not well explained (see A-D below). Experiments are not sufficiently controlled (E-H below) and data of main figure and figure supplement is at least partially contradictive (I-J below). The authors need to re-analyse existing data and provide some new data. More detail in the sub-points below.

A) Figure 5 e.g: How is "transport" defined here? Is transport = some mRFP intensity over threshold within the 5 µm from cell perimeter? Otherwise it is hard to believe that a biological system, which always shows some background activity, produces absolute '0' values in this assay. I would kindly ask the authors to provide a proper definition of "transport" to the reader here.

B) Figure 5: I assume that the assay has been performed in interphase cells. KIF15 however does not localise to microtubules in interphase cells but rather to actin stress fibres (Buster et al., 2006), presumably by interaction with myosin 2B (Feng et al., 2016). Theoretically, some of the peroxisome behaviour observed here could therefore be actin/myosin dependent as well. This is probably not the case since the myosin 2B interaction was mapped to the KIF15-tail, which is missing here and the motor domain is probably overexpressed, uncoupling it form endogenous targeting/regulation mechanisms. However, to validate the assay in the first place, it should have been tested briefly, whether the KIF15 MD localises to microtubules at all.

C) Figure 5 D/F: As far as I understand it, the authors define an intensity threshold and quantify the cell area within 7.5 or 5 µm from the cell perimeter that is 'covered' by intensity larger a certain threshold. Why 5 µm in one case and 7.5 µm in the other case? Is thresholding really a good idea here? Given a fixed total-intensity-over-threshold equally distributed along the 5 µm (center to periphery) or with a distribution highly skewed towards the periphery. The skewed distribution would indicate better transport but would cover less area. Would something like fraction from overall intensity (above threshold) in a certain distance from the cell perimeter be more accurate?

D) Please provide an explanation (e.g. in the legend or methods) for why the quantification thresholds are different for the two kinesins in Figure 5D/F. For Kif15 the periphery is defined as the outer 7.5μm of the cell, but for Kif1A it is 5μm. Does this threshold value affect the interpretation of the results?

E) Figure 5: KBP inhibits KIF15 motor domains in a 1:1 stoichiometry. The authors kind of 'control' for the KBP expression (subsection “Cell biology image analysis and quantification”: 'Images were acquired of cells that express similar levels of HA-KBP constructs based on immunostaining'), but not for the KIF15/KIF1A-MD levels. KIF15/KIF1A-MD levels might change from mutant to mutant due to different stability in vivo (and from cell to cell, transient expression). Hence, we cannot formally exclude that a drop in peroxisome transport could as well be caused by [c] KBP > [c] KIF15 MD, masking positive (i.e., disruptive) hits or that false positive hits would be created when [c] KIF15 MD > [c] KBP.

Thus, the authors should please provide a quantification of the KIF15-MD expression, allowing the reader to estimate, whether the KIF15/KBP ratios are the same throughout the experiment. Since the authors selected single cells based on the KBP signal, KIF15-MD quantification should also be done per cell.

F) Figure 5—figure supplement 1: The authors compared the binding of WT and mutant KBP variants by quantifying the amount of HA-KBP that coprecipitated together with bioGFP-KIF15-MD. The amount is given as "intensity KBP-PD/intensity KBP input" normalised to the WT KBP condition. However, it is not clear whether the PD/Input quotient has been calculated first and then been normalised to WT KBP or if the quotient has been calculated from already normalized values. First case would not be ok, as Input and PD were clearly run and quantified on different gels and are therefore obviously not directly comparable – e.g., the pull-down bands for KBP to L10m in the first panels of (b) and (c) are stronger than their corresponding input bands.

However, I did a quick quantification (ImageJ) of the blots shown in the left panel of (b) normalising each blot to WT KBP first. Still more protein was pulled down than has been put into the assay in the first place – how can this be? Also. Doing it like this, L12m would not be a positive hit any longer. While trying to quantify the other blots, I recognized that the tonal ranges for the KIF15-MD blots (b, right panel), (c, both panels) and the KBP input blot in (c, left) has massively been pushed to the higher intensities, leaving virtually no background in the lanes above and below the bands. If this happened during figure preparation – please don't do that. If this already happened due to wrong settings during data acquisition in the imager, your quantifications might not have bene accurate.

I recommend to (re-)run both input and PD sample together on the same gel (there are 26-well gels commercially available). Like this they are treated the same way during western blotting/detection – allowing a more reliable cross comparison.

G) Figure 5—figure supplement 1: comparing the PD/Input quotient only makes sense, if we assume that KIF15/ KIF1A-MD pulldown occurs from all lysates with the same efficiency and the overall KIF15/KIF1A-MD amount is not limiting KBP pulldown. This, however, is clearly not the case: in (c) lanes L14m, L16m, L18m, L12m+L14m and alphaHP4am the amount of pulled down KIF1A-MD is much less than for the other constructs, while the KBP input in comparison is even higher. Less KIF15/KIF1A-MD in the pulldown fraction might reflect a weaker KIF15/KIF1A-MD expression (mutant stability in vivo, transient transfection), less efficient biotinylation by BirA (transiently transfected as well) in vivo or less efficient pulldown by the streptavidin beads – we just can't tell from these figures. Nevertheless, if just 10% of the total KIF15/KIF1A-MD are pulled down, only 10% of total KBP should be expected to co-precipitate as well.

Hence, the authors should please show and quantify the KIF15/KIF1A-MD input as well and relate the fraction of co-precipitated KBP with the fraction of pulled down motor domain (i.e., are mutants underperforming regarding their expected pulldown efficiency?).

I would also like to encourage the authors to verify their positive hits (i.e., L12m, L14m, HP4am, HP4bm and HP5m), by co-precipitating defined amounts of recombinant KBP/KIF-MD proteins to be on the safe side. Since expression was done in bacteria and purification protocols are established this could be done in a reasonable amount of time.

H) In Figure 5—figure supplement 1C, the intensity of the bait (bioGFP-Kif1A_MDC) appears to be significantly lower for the L16m and L18m lanes compared to the other lanes. A lower level of bait could explain the weaker pulldown of HA-KBP in these lanes. The data should be re-quantified to take into account the amount of bait pulled down, or the experiment should be repeated with a consistent level of bait across all lanes (as in Figure 5—figure supplement 1). Since the authors highlight the weaker interaction between the L18m KBP and Kif1A compared to Kif15 in the text, this is an important control to include.

I) Figure 5 and Figure 5—figure supplement 1: The L10m and L16m mutation bind KIF15-MD like WT KBP, but fail to inhibit peroxisome transport. If this effect is real (see points above), the authors should please comment on these results, since they are in conflict with their simple binding = inhibition model.

J) The text doesn't address inconsistencies between the results of the peroxisome assay and the immunoprecipitation. For example, in Figure 5D/E, the mutation to loops 10 and 16 causes the peroxisomes to disperse to the periphery, which indicates that the inhibition of kinesin by KBP is relaxed. However, in Figure 5—figure supplement 1B the interaction between KBP and the kinesin does not appear to be significantly lower (and in the case of L10 is stronger than the control). These results appear to be directly contradictory. Can the authors provide an explanation for this effect?

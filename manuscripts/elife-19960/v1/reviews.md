# Peer review - Round 1

Editors:
- Nahum Sonenberg, McGill University , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19960.023](https://doi.org/10.7554/eLife.19960.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Dynamics of mTORC1 activation in response to amino acids" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tony Hunter as the Senior Editor. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers found your work of interest but were very critical about the lack of controls and incorrect interpretation of the data. If you believe that you could improve the work, we would be happy to consider the work as a new submission. However, given the extensive requirements specified by the reviewers, we would understand if you choose to submit this work elsewhere.

1) Being able to follow Raptor translocation with endogenous levels of protein could be valuable, but it appears that the Raptor-GFP fusion protein is a hypomorph, and does not fully recapitulate the function of native Raptor. For example, amino acids alone failed to activate mTORC1 in the Raptor-GFP HAP-1 cells unlike the parental HAP-1 cells, and maximal activation of mTORC1 in Raptor-GFP HAP-1 cells required both amino acids and growth factor stimulation, and even then it was not as strong as in parental HAP-1 cells. In this regard, both growth factors and amino acids are generally required for the full activation of mTORC1 in in mammalian cells, and therefore it is not clear why mTORC1 was fully activated in HAP-1 cells just by replenishing amino acids.

2) The lag in S6K phosphorylation behind Raptor recruitment to lysosomes looks real, but the authors need to demonstrate that the anti-pT389 S6K blotting signal is linear before drawing a firm conclusion (it would be ideal if they could somehow monitor S6K phosphorylation in single cells in parallel with Raptor-GFP translocation).

3) In contrast to the authors' conclusion, the immunofluorescence images in Figure 1B show overlap between LAMP-1 and mTOR at all times. The authors should repeat the experiments with a Raptor antibody.

4) Several figures: When assessing S6K, 4E-BP1 and S6 phosphorylation by immunoblotting, the authors should also blot for total levels of these proteins.

5) Figures 1A and D, 2A; Figure 1—figure supplement 1C and E; Figure 1—figure supplement 3B; Figure 5—figure supplement 5A-B; and Figure 6—figure supplement 1C–D. The authors should include a loading control.

6) Figure 2 – the authors should determine if RAPTOR-GFP is localized to the lysosomes. In Figure 3C, D the authors showed some co-localization with LAMP-1. However, this was not quantified and most of the GFP-RAPTOR is not co-localized with LAMP-1. In addition there was not much change in GFP-RAPTOR localization in starved vs. fed conditions (Figure 3A, B).

To determine the functionality of RAPTOR-GFP, the authors exclusively rely on S6K phosphorylation measurements by immunoblot. It would be informative to measure other readouts such as 4E-BP1.

7) Figure 1—figure supplement 2B. The authors should blot for total levels S6K (or HA), RHEB and RAGA in the lysate and immunoprecipitated samples. As is, they check only the phosphorylated form of S6K. Also, a negative control for the immunoprecipitation is missing.

8) The authors did not provide mechanistic explanation for the observations presented in Figures 5 and 6. Based on experiments using a fluorescent leucine methyl ester analogue, the authors seem to favor the "inside out" model of amino acid sensing in which amino acids are sensed in the lysosomal lumen. However, a recent study showed that cytoplasmic SESN2 is "almost certainly" the major leucine sensor upstream of mTORC1 (Wolfson RL et al. Science. 351:43). This recent study should be mentioned and discussed. How do the authors know that the mechanism of sensing the leucine analogue is the same as that of sensing a non-esterified leucine (based on the structure of the leucine-binding pocket in SESN2, it seems unlikely to accommodate this analogue)? The authors should determine if SESN2 depletion affects translocation of RAPTOR-GFP to lysosomes upon addition of the leucine analogue. If it does not, how do the authors reconcile their findings with those of Wolfson et al.?

Alternatively, if SESN2 depletion has an effect, how can the authors argue that accumulation in the lysosome lumen is physiologically relevant? The glutaminolysis model, which provides a sensing mechanism for leucine and glutamine in the mitochondria, should also be mentioned (Durán RV et al. Mol Cell. 2012. 47:349).

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for choosing to send your work entitled "Dynamics of mTORC1 activation in response to amino acids" for consideration at eLife. Your resubmission has been evaluated by Tony Hunter and the original Reviewing Editor who handled your submission. The editors are generally satisfied with the revisions made, but would like to ask you to address the following points.

On reading the resubmitted paper in depth, the conclusion drawn from the new data in Figure 7 is somewhat puzzling. In these experiments the authors have addressed the requirement for Sestrin2 (Sesn2), a recently reported Leu sensor, for mTORC1 stimulation by their new fluorescent Leu analogue. Based on the work from the Sabatini lab and others, the prevailing current model is that Sesn2 binds to and inhibits the GATOR2 complex, which in turn inhibits GATOR1, a complex that acts as a RagA/RagC GAP to prevent Ragulator recruitment of mTORC1 to the lysosome. Leu binding to Sesn2 causes it to dissociate from GATOR2 allowing to inhibit GATOR1, which then leads to RagA/RagC activation and mTORC1 recruitment to the lysosome where it interacts with Rheb, i.e. GATOR2 is effectively an activator of mTORC1, and not "a key negative regulator of mTORC1", as the authors state in subsection “Activation of mTORC1 by the amino acid analogue depends on Sestrin2 and on intact lysosomes”. Based on this model, the knockdown of Sesn2 and the consequent loss of its GATOR2 inhibitory activity would be expected to result in (partial) activation of mTORC1 in the absence of Leu (which is what the authors observed in HEK 293 cells). Moreover, if Sens2 were the only Leu sensor in the system, then one would expect mTORC1 activation to be insensitive to Leu in cells devoid of Sesn2.

1) The new data in Figure 7 show that partial depletion of Sesn2 increased mTORC1 stimulation by the FA Leu analogue and by amino acids, which on the face of it does not fit with the model described above. It is possible that Sesn2 is in excess over GATOR2, and that, even though Sesn2 levels have been reduced by si-Sestrin2, the remaining level of Sesn2 protein is sufficient to bind and inhibit all the GATOR2 complex, and that the lower level of Sesn2 somehow sensitizes the system to Leu (it would be better to use CRISPR technology to knock out Sesn2, but this would be beyond the scope of the paper). Other possible explanations are that Sesn1 is partially redundant with Sesn2 for Leu sensing in these cells or there is a second Leu sensor in the system that is affected by Sesn2 in some way. Ideally, what the authors should do is to re-express siRNA-resistant WT Sesn2 (this is a control for potential off target effects of si-Sestrin2 that is missing from Figure 7) and also Sesn2 L261A, which cannot bind Leu (did the authors try to model the FA Leu analogue into the Leu-binding pocket of Sesn2?) in the si-Sestrin2 treated cells, and check the response to FA Leu and amino acids.

2) It would strengthen these data if GFP-Raptor translocation to lysosomes FA Leu and amino acid-induced were monitored in the Sesn2 knock HAP1-RAPTOR-GFP cells.

In sum, please provide a response to these issues and explain the apparent paradox that cells remain responsive to Leu after removal of a Leu sensor from the system.

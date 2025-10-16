# Peer review - Round 1

Editors:
- Richard Aldrich, The University of Texas at Austin , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12088.009](https://doi.org/10.7554/eLife.12088.009)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Mechanical sensitivity of Piezo1 ion channels can be tuned by cellular membrane tension" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Richard Aldrich as the Reviewing Editor and Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, the authors provide an in-depth assessment of the nature of the mechanical stimulus that activates Piezo1 channels in heterologous cells. In brief, there are two key findings. First, Piezo1 channels respond to changes in membrane tension rather than curvature. Second, that sustained tensions even such as those present in membrane patches held at symmetric atmospheric pressures are sufficient to inactivate a proportion of the channels. This leads to activation following applications of pressures sufficient to flatten patches and may help to establish resting set points in cells. These biophysical findings were facilitated by careful measurements of membrane curvature as well as controlled application of pressure differences across membrane patches. They have important applications for how Piezo1 works in cells and for the origin of variations in the kinetics of their responses to mechanical stimulation.

Essential revisions:

1) The authors argue that the cytoskeleton is unlikely to contribute to Piezo1 channel activation on the basis of the similarity of responses observed in cell-attached and excised patch conditions. While it is reasonable to assume that the cytoskeleton is disrupted in excised patches, direct examination of this question has indicated that excised patches can retain their association with the cortical cytoskeleton. The authors should either perform additional experiments to directly address (e.g. determine how application of cytoskeleton disrupting agents like cytocholasinD affect tension-sensitivity) this inference or rephrase the discussion of this result-indicating that while their data are more consistent with the idea that the cytoskeleton is dispensable for Piezo1 activation in HEK293T cells, that they cannot exclude this possibility

2) The most novel contribution of this work is the measurement of membrane tension/curvature while recording from piezo1-containing patches. This is challenging, and perhaps a more thorough description of the imaging procedure would be helpful. For instance, it is unclear how the authors ensure that they are looking at a plane that crosses the center of the membrane patch. If this is not the case, curvature estimates might be quite inaccurate. Also, the custom-script written in Igor-Pro to measure the radius of membrane curvature should be made available, at least upon request, if not through a free source code repository (GitHub or the like).

3) The authors use a clever pre-pulse protocol to "wake up" inactivated piezo1 channels. Use of pre-pulses is not new in the study of mechanosensitive channels and it has been used to study inactivation of MscS (Akitake et al., JGP 2005) and to show that "the availability of MscS depends on both the rate of pressure application and the amplitude of prepulse pressure". It would be informative for the readers to discuss the piezo1 results in the context of prior work with pre-pulses and mechanosensitive channels.

4) The authors show control recordings obtained when using an empty vector for transfection, which is quite good. The recorded currents are mostly flat, but there seems to be some minuscule response at small positive pressures in inside-out patches (Figure 2B). This might be within the noise, but scales are all different in panels A-C, so it is difficult to appreciate the relevance of the small currents, and I do note that data presented in Figure 4 is right on the same range of pressures and currents of the signal seen for pcDNA transfected cells (Figure 2B). In addition, no controls are presented for experiments with pre-pulses, and there is the possibility (admittedly very minor) that the authors are "waking up" other channels present in HEK293t cells. Since pre-pulses are right on the range of 5 to 10 mmHg, it would be important to see a control curve with vector-only transfected cells for pre-pulse protocols. Also, please indicate if the data presented in Figure 4 and Figure 5 were obtained using inside-out patches.

5. One important point to clarify is that the authors claim that the curvature (positive or negative) of the membrane is not important for Piezo1 activation, thus concluding that membrane tension is the most important factor in activation. However, it is not clear that the local curvature around the channels (which changes in a scale of a few nanometers) can be affected by the macroscopic patch curvature (happening in a micrometer scale). It has been seen in gramicidin channels that altering the local curvature by asymmetric lipids can change the coupling to lateral tension.

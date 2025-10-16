# Peer review - Round 1

Editors:
- Jie Xiao, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32057.040](https://doi.org/10.7554/eLife.32057.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Molecular coordination of Staphylococcus aureus cell division" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to frame the key concerns we feel must be addressed before a binding decision may be made on your submission.

Overall, the referees are in agreement that the work potentially represents new insight into cell wall synthesis and division in S. aureus. However, both reviewers raised serious concerns regarding the experimental methods, quantification, and interpretations, and consequently the major claims of the work. There were also concerns regarding the necessity of some experiments. Before a decision can be made regarding the publication, we ask you to submit a revised application addressing the following comments:

Major comments:

1) Demonstrate the ability of ADA probes to label new septal cell wall synthesis.

The authors are assuming that FDAA incorporation equals PG synthesis, when it is well known that this is not the case, most especially for the ADAs, which are incorporated into the cell wall by transpeptidase reactions. The authors would be correct in stating that crosslinking occurs everywhere in the cell and throughout the septa, but this is not synthesis. Importantly it has been published by two different groups that PBP4 (a LMW transpeptidase) is responsible for the extra septal FDAA staining signal (Monteiro, 2015 doi:10.1038/ncomms9055), (Gautam, 2015 DOI: 10.1021/jacs.5b02972). These two papers reveal that a large amount of FDAA incorporation occurs via PBP4, but this is due to crosslinking of FDAA's into the existing material and does not reflect the insertion of new material.

Thus, if the authors want to claim that A) PG synthesis occurs throughout the septa, and B) there are no hotspots (or puncta) of PG synthesis in the ring, they need to Redo their FDAA labeling and STORM in PBP4 null cells at different pulse lengths, so that they can (as much as possible) remove this outside "noisy" signal, and truly focus on where synthesis occurs.

To prove this further, they should also conduct various ranges of pulses of ADA-DA (e.g., 5s, 15s, 30s, 1 min) as these are believed to be reflective of synthesis, and not simply crosslinking. These should be done in PBP4 null cells as well.

Finally, the authors went to great detail to make the HADA probe and then do not use it for any significant experiment. They also showed no evidence of incorporation of this probe into the PG (Figure 3—figure supplement 1 only has data for the ADA probe). The ADA-DA probe could be used throughout the manuscript – thereby allowing results to be accurately compared without having to worry about artifacts of the PG-probe. The HADA probe was not used in any significant experiment and could be removed without altering the conclusions of the manuscript.

2) Provide quantitative measurements specifying the localization precision and spatial resolution of PALM/STORM images.

The authors must determine (or at least estimate their precision of localization) in both XY and Z, for eYFP and Alexa 647. Many of the arguments made in figures 1 and 3 do indeed hinge on their precision of localization. They dismiss the need for this, stating – "It is challenging to determine resolution in localisation microscopy images. However, it is more important to determine which image features observed are representative of biological structures, then to determine absolute resolution." This reviewer adamantly disagrees with this statement, as the conclusions drawn from the widths of their distributions in Figures 1 and 3 rely on their precision of localization, and thus far it is not clear if they have achieved adequate precision to make claims about the widths of these distributions.

To overcome this issue, the authors have attempted to fit their data in Figure 1 with different precisions (up to 60 nm). However, several later statements made in the paper suggest that their precision may indeed not even be that accurate: First, they state their prevision for localization of 647 is <70nm. This is a troubling measure for multiple reasons, as eYFP is significantly dimmer than 647. This makes this reviewer fear they may not have enough photons even to approach 70nm, close to the fitting they used in Figure 1 to justify these measures. Second, while it appears they used flat septa in Figure 1 (in the XY plane), in later figures they used 3D-Storm, which then raises the issue that there is a much less precision in Z relative to XY. This is not raised nor acknowledged in the paper, and how it affects the data is not clear. For example, in Figures 1 and 3, what angle were these septa in that they analyzed? (This complicates their data). Were they flat in XY, which would give the best resolution or were they angled up in Z, or tilted in some combination of XYZ? This is a key issue, as the spread, noise, and asymmetry in these distributions may arise from their precisions of each different septa, and where it is in the Z plane.

So, overall, the authors must report their localization precision in XY, and Z, for both eYFP as well as 647. This is best done (amount other ways) with pure protein immobilized on coverslips, as well known. This should allow them to accurately determine the height of the peak of a single molecule and FWHM of each localization. On an NSTORM system, the precision in Z can also be easily determined, as these systems have piezo stages.

Alternatively, at the very least the authors should at minimally report the computed (localization) precision from frame by frame peak heights in their data, as detailed in doi:10.1038/nmeth.1447. While this does not account for other sources of noise (such as instrument vibrations), it will at least give an estimate. If their analyses are conducted on complexity flat rings in the XY plane, knowing the precision can help the authors gauge the accuracy of their claims. However, if they are drawing on data that involves rings that traverse the Z direction, they should do determine, or at least give a rough calculation of the loss of precision caused by the Z-direction, and use that "worse" precision estimate to determine if they can make the claims in the paper.

3) Re-examine the claim that FtsZ and EzrA are not localized in a thin ring around the division plane, but that these proteins are in much wider bands.

There are a few problems with their analysis. First, the method by which they analyzed these distributions appears to be erroneous. They stated that they looked at the localizations at distances from centers of the circles. While this would make sense if the septa were indeed perfect circles (as shown in their simulated data), but examining the examples they show it appears most of many of these septa are not perfect circles, rather they are extended ellipses. Thus, measuring the distance from the center is not a valid measure of thickness (or distance to the edge), and thus this assumption is likely distorting their conclusions. If they want to back up this claim, it would be better they fit an ellipse to the density each septal ring, and then plotted the distribution of localizations around that line around the septa.

Second, as described above, to make the claim that FtsZ and EzrA are not in a thin "ring" they must determine their localization precision (discussed more in 2 above). Currently, they attempt to get around this by estimating the spread with different localization precisions. This is not adequate, as they have not even demonstrated they have 60nm precision (the largest value they use).

Other concerns:

1) In Figure 4—figure supplement 1, septal peptidoglycan synthesis actually looks well-localized to my eyes for 15-20 minutes and even to some extent after 30-35 minutes of PC190723 treatment, well beyond the time when FtsZ and EzrA have delocalized. Do the authors have an explanation for why this might be? It seems contrary to their claim in the manuscript that gross PG synthesis follows FtsZ and EzrA localization, although this is certainly true at later time points.

2) The Slimfield analysis, while nice, adds nothing to this paper or story. All this gives them is the diffusion coefficient of EzrA. First, how is this measure pertinent to the story? That is not made clear. Second, there also appears to be an immobile fraction, but the authors report the characteristics of the diffusive form. Is this the biologically relevant form? If EzrA is treadmilling with FtsZ, it should be immobile, and the diffusive molecules not associated with FtsZ.

Furthermore, the authors should rethink their statement about EzrA moving around the cell with FtsZ – that would not be expected for molecules associate with treadmilling filaments.

3) Figure 3—figure supplement 2B and C should present the same brightness and contrast range for comparison.

4) In the last paragraph of the Discussion, it is difficult to follow how the data presented support or do not support a model of "machines moving through the cell depositing peptidoglycan." The article argues persuasively that septal PG synthesis is not confined to the inner edge of the invaginating septum in Staph, but doesn't include much detail about the molecular mechanism of insertion (which is fine, and not necessary for this article). Given that FtsZ and EzrA are colocalized with PG incorporation in this system as well, it is a question of how the authors rule out a model where these hypothetical molecular machines do exist, but are distributed across the entire septum rather than localized in one region- such a system seems consistent with the results presented here. It is also confusing that these proteins are not always physically adjacent- it seems like most of the article has been arguing the contrary, that a wider FtsZ/EzrA localization band gives rise to more broadly distributed septal PG insertion.

5) The use of the Alexa Fluor 647 NHS ester should be clarified. This reagent non-specifically labels proteins in the cell wall.

6) As unnatural amino acids are used, could the authors comment on how they think these additions could change the structure of the cell wall? Could the probes possibly effect the placement of the machines?

7) Could the authors explain what "gross peptidoglycan synthesis" is? How does this play into their model?

8) The treatment with labeled vancomycin is not standard – usually unlabeled vancomycin is added with the labeled vancomycin. It is not certain if vancomycin is capable of labeling a D-Ala-D-Ala terminus that has been labeled with a fluorophore – this is very close to the binding pocket. That could be a reason why they do not see labeling there? What do these experiments add to their conclusions?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Molecular coordination of Staphylococcus aureus cell division" for further consideration at eLife. Your revised article has been favorably evaluated by Gisela Storz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Calculation of the spatial resolution of EzrA and FtsZ imaging:

Localization precision only tells how accurately one can determine the position of one localization. It is usually much better than the actual spatial resolution one can achieve, which is compounded by the Nyquist resolution (calculated by labeling density), and experimental resolution (calculated by the spread of repeat localization). Of these two, the experimental resolution often is the limiting factor, and should be reported. The authors cited reasons for not doing the latter calculation coltharp, but this measurement can be done by using the fixed bacteria instead of purified, in-vitro samples. See Endesfelder et al., 2014, Churchman LS et al., 2006, Biophysical J, 90(2):668-671, and Coltharp et al., 2012.

2) PBP4 null experiment:

There was one image (Figure 3—figure supplement 3) qualitatively suggesting that 15s ADA-DA and ADA incorporation in the absence of PBP4 is homogeneous. Please provide enough statistics to support this conclusion, i.e., number of cells, autocorrelation function and labeling density.

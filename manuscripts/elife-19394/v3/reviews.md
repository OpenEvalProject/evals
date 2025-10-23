# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University Medical Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19394.018](https://doi.org/10.7554/eLife.19394.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Electrostatic anchoring precedes stable membrane attachment of SNARE proteins with the plasma membrane" for consideration by eLife. Your article has been favorably evaluated by Randy Schekman (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife in the current form. Although the reviewers and editors found the topic of your work of considerable interest for potential publication in eLife, serious concerns were raised that may require a substantial amount of additional experiments and computer simulations.

Reviewer #1:

This work draws attention to an aspect of SNARE proteins that has not been extensively studied. Basic residues were identified in the cys cluster of SNAP25/SNAP23 that promotes initial plasma membrane association of SNAP25/SNAP23 which precedes the stable membrane attachment mediated by palmitoylation of cysteines. The authors performed an extensive set of mutagenesis, imaging, and fractionation experiments to support this conclusion. Coarse grain MD simulations were then performed to study random collisions between the corresponding peptides and a membrane and conclude that PIP2 is essential for the membrane association of the peptide. They support this notion by a competition experiment between SNAP-25 and the PH domain of phospholipase C-δ for PIP2.

1) In Figure 1, the ratio of membrane/cytosol localization is calculated. However, comparing the absolute protein level that is associated with the membrane would also be informative, considering that high expression levels of the positively charged mutants might cause saturation of membrane binding.

2) In Figure 2, the total expression level of SNAP-25 should be provided in addition to the cellular fractions.

3) In Figure 4, images should be provided to correspond to all cases shown in the bar chart.

4) In Figure 5, a negative control should be provided that shows that the mobility of SNAP-25 is indeed affected by interaction with syntaxin, e.g., by introduction of mutations in SNAP-25 that interfere with SNARE complex formation.

5) In Figure 8, a control should be provided to show that the competition is related to the competing interaction between the PH domain and PIP2, e.g., by using a mutant of the PH domain that does not interact with PIP2.

6) The role of polybasic residues near palmitylation or myristoylation sites has been reported previously in other contexts, and would be useful to provide a brief summary in the Introduction, e.g., M. Crouthamel, et al. Cell Signal, 20 (2008), pp. 1900-1910; K.H. Pedone, J.R. Hepler. J Biol Chem, 282 (2007), pp. 25199-25212; K.A. Cadwallader, et al. Mol Cell Biol, 14 (1994), 4722-4730; Wright, L. P. & Philips, M. R. J. Lipid Res. 47, 883-891 (2006); O. Jeffries, et al. J Biol Chem, 287 (2012), 1468-1477.

7) There are a few polybasic amino acids in the C-terminal part of the of SNAP-25 linker, such as R191, R198 and K20 that may also contribute to plasma membrane localization. An experiment would be optional, but at the minimum, the authors should comment on these residues.

Reviewer #2:

This is an interesting work dealing with the determinants of membrane association and subsequent palmitoylation in SNARE proteins, with potential generality. The plasma membrane localization data and how they respond to mutation are compelling to this reviewer. The simulation methodology is not clearly specified in several key respects, and the stable association (+/1 1 peptide) of all peptide sequences tested raises questions about the simulation model and its ability to capture the desired behavior. Time until stable association is not a measure of equilibrium properties and is thus inappropriate as a metric. The equivalent metric to the experimental data is an estimate of equilibrium partition coefficient.

Since peptide secondary structure (and 3D structure also) will differ between solution and membrane-associated forms, simply constraining structure and measuring the association (or even partition) between solution and membrane-associated forms does not capture either the kinetics or equilibrium behavior of the adsorption process. Atomistic simulations of the peptides in membrane-bound and solution forms to measure structural equilibria would be required to complete this analysis.

The authors state that they used PME electrostatics with MARTINI, but they do not state whether they also used the MARTINI polarizable water model, which is required for proper usage of PME electrostatics in the model as per the original papers. This technical point is important here, as the authors are measuring electrostatic interactions between charged peptides and a membrane (and they appear to observe artifactually stable association).

In view of these issues, I would recommend that the simulations either be redone entirely or eliminated from the manuscript, as they do not provide a robust measure of the phenomena the authors are trying to predict (and indeed measure experimentally).

Reviewer #3:

SNAP25 and SNAP23 are lipid anchored to membrane by post-translational palmitoylation of cysteine residues. The authors present evidence that initial access of SNAP25 and SNAP23 onto membrane for subsequent palmitoylation is mediated by electrostatic interactions of Lys residues near the Cys quartet with acidic phospholipids.

1) The work seems preliminary in only evaluating two SNAP25 constructs, one removing 8 Lys (SN25-5) and the other adding 4 Lys (SN25+10). The largest effects were observed with the first of these so it would be of interest to test other mutants to determine proximity to Cys quartet. Many Lys residues have acidic neighbors and it is unclear whether replacement of the Asp70, Glu73,-75 and Asp80 would be equally disruptive. The work on SN25+10 is not very relevant because it does not deal with requirements in the native protein.

2) Others have suggested that hydrophobic residues are involved in targeting but this issue is not addressed or much discussed. Would replacing the same residues with hydrophobic residues preserve membrane targeting?

3) The conclusions of the article would be much stronger if an assessment of palmitoylation were conducted. The authors instead infer palmitoylation based on Cys to Gly.

4) Data are shown as SEM but there is no statistical analysis for Figures 1D, 2, 3C, 4B, 5C, 6E, 8B so it is unclear what differences are significant.

5) The results shown in Figure 8A are quite puzzling. The images shown do not seem to be reflective of the intensity differences plotted in Figure 8B. The left panels of 8A show a remarkable suppression of PLCPH by SN25 (but not by C to G) whereas histograms indicate 2X change. It is not clear which of these intensity differences is statistically significant. There is no indication that similar amounts of protein were being expressed in these studies in comparisons done in a cell line that has endogenous SN25. Lastly, it is not at all clear what the interpretation of these studies would be.

6) The images of the membrane sheets (Figure 4) are confusingly shown at different scales and cannot be compared to bar graphs. These should be shown as direct comparisons to agree with the bar graphs.

7) To eliminate expression level as an important variable in Figure 1, the authors provide Figure 1—figure supplement 1 to indicate lack of correlation. However, the ordinate scale greatly exceeds the range over which the results of Figure 1 were taken so the lack of correlation over this broad scale did not seem to be tailored to the experimental work shown.

8) Two features of Figure 5 need to be addressed. Firstly, the red and green channels exhibit very close similarity in the lower panels. Most previous studies on Syx/SN25 do not show this degree of alignment so the possibility of channel overlap should be addressed. Secondly, overexpression of Syx appeared to slow the mobility of all fluorescent objects in the lower row compared to upper row. Is the result of extreme overexpression?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Electrostatic anchoring precedes stable membrane attachment of SNAP25/SNAP23 to the plasma membrane" for further consideration at eLife. Your revised article has been favorably evaluated by Randy Schekman (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are two remaining issues that need to be addressed before acceptance, as outlined below:

1) To reinforce the notion that SN25 membrane translocation requires PIP2, the authors construct the study of Figure 8 of expressing the PH domain of PLCdelta1 and finding less SN25 on membrane sheets. However, in this study the PH domain was expressed for 48 hrs, there was less SN25 expressed (compared to PHmut), and the cells are drastically altered in their morphology. The latter suggests drastic cytoskeletal changes or apoptosis that occur in depriving a cell long term of PIP2. Either of these would undoubtedly affect SN25 trafficking through an endosomal pool and its turnover in the cells. There does not seem to be a straightforward interpretation for the results of Figure 8. In the absence of more concerted characterization, this study should be removed from the manuscript.

2) In Figure 7, in vitro protein-liposome interaction studies show that WT SN25 binding to liposomes is enhanced by inclusion of PIP2. The SN25-5 mutant exhibits some decrease in binding. This could be interpreted as PIP2 playing some role in recruiting SN25 to the membrane although the loss of in vitro binding by SN25-5 is much smaller than that claimed for cellular membrane interactions. This difference between the in vitro binding studies and the cellular studies should be discussed. Also, the results with SN25+10 do not seem to be relevant because this mutant has acquired additional MARCKS protein-like properties of PIP2 binding that may not be relevant to the WT SN25 protein.

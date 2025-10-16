# Peer review - Round 1

Editors:
- Stephen C. Harrison, Harvard Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18740.026](https://doi.org/10.7554/eLife.18740.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Advances in XFEL diffraction data processing applied to the crystal structure of the synaptotagmin-1 / SNARE complex" for consideration by eLife. Your article has been favorably evaluated by Arup Chakraborty as the Senior Editor and three reviewers, including Tom Terwilliger (Reviewer #2) and Stephen C. Harrison (Reviewer #1), who is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a Research Advance that indeed reports improvements in the software previously described in eLife (Uevirojnankoorn et al., 2015) and that comes to updated conclusions. It thus conforms appropriately to the intent of the Research Advance category and merits publication.

The authors have made some substantial changes to their approach for analyzing the still images obtained from XFEL data. The new approaches allow treatment of reflections with negative intensities and the use of pseudo-Wilson scaling to normalize not just the average intensity of each image but also the fall-off with resolution (as has been done as a matter of course previously for synchrotron data but not for XFEL data). These approaches were applied to previously analyzed data for a synaptotagmin/SNARE complex, and the resulting maps appear to show more detail than those calculated with data treated by the earlier methods. Moreover, density correlations were better for the XFEL maps than for maps from synchrotron data from similar crystals.

Essential revisions:

Attention to the suggestions (a) and (b) under (1) and to one or more of the suggestions (i), (ii), and (iii) under (2)(b) would make the paper stronger; those calculations should be straightforward and take relatively little time. Many of the other points raised here cannot be settled with the current data, but some comments on those points would be valuable.

1) Improvement from reprocessing XFEL data. The data from the reprocessing are more complete (98% vs. 88%), but a large fraction have negative intensities, and excluding the negative intensities reduces the completeness to 88%, the same as for the previous analysis. The CC1/2 is marginally better (94% vs. 93%) for the reprocessed data. The free R value for the complex was lower for the reprocessed data (33% vs. 35%). This is the most convincing evidence that the reprocessed data are more accurate, but as the models were not the same, it is not easy to tell if the change is significant.

Suggestions:

a) It would be helpful to show a detailed comparison of the previous XFEL data with the current data. For example, what is the correlation of intensities between previous and current processed data, and what is the I/σ vs. resolution for each, after selecting the data that are in common between the two?

b) It would also be helpful to refine the same model against the previous and current XFEL datasets, only adjusting parameter values, to have a more convincing comparison based on decrease in the free R.

2) Comparison with synchrotron source. The R-factor and other formal comparisons of the model refinement suggest that the model fits the synchrotron dataset more closely, even when allowing for the resolution difference. This conflict between the free R (overall agreement between model and data) and the real-space correlation (average local agreement between model and data) is unusual. Thus, there appear to be two key issues at this point, neither related to whether the software needs even more work. (a) One key issue, which the authors cannot settle with the current data – if they could, this would be a new paper, not an Advance – appears to be: what is the physical explanation for the differences in the data sets? Excluding for now potentially undiscovered aspects of the scattering physics from the intense XFEL beam, one can see at least three reasons why the data might be different: (i) differences in the way data were collected and merged; (ii) differences in crystal damage (including, of course, the possibility that there was very little in the XFEL case); (iii) differences in the crystals themselves on the two occasions, separated substantially in time. (b) The other key issue is: why does an atomic model fit one better than the other? A hypothesis that needs testing is that the 2Fo-Fc map calculated from the XFEL dataset has more model bias because of less accurate data. (The rationale behind this hypothesis is that a dataset with zero I/σ everywhere would effectively look just like the model because the 2(Fo-Fc) portion of the 2Fo-Fc map would be random and the Fo portion would look just like the model).

a) What is the physical explanation for the differences in the data sets?i) The single-crystal data came from three fixed positions, with ccd recording. Current experience shows that this regime gives less accurate intensities than the continuous motion regime made possible by direct x-ray detectors. The latter strategy yields data with more uniform B-factors (instead of a "sawtooth" dependence of B-factor on frame number) and more favorable statistics. Nonetheless, a single crystal is more likely than many crystals to have essentially identical unit-cell contents, packing, etc., from one place to another than will a large number of crystals, and perhaps it is not surprising that despite the greater "blur" (higher net B, etc.), one model fits that set better than it does a set merged from many crystals.

ii) It might be a good idea to include the "sawtooth" B-versus-frame number plot for the single crystals, to show how much damage resulted from the total exposure at each location. Did the initial frames show measurable Bragg intensities beyond 4.1 Å? If so, the right comparison of synchrotron and XFEL might have been, for the former case, to collect only as many frames from each position that showed no evident decay, if necessary using more than one crystal to complete the data (but of course getting into an issue of crystal-to-crystal variation – perhaps minimized by taking crystals from a single drop).

iii) With two molecular complexes in the asymmetric unit, there are probably more possibilities for batch-to-batch variation (let alone one year to the next variation) from many small crystals than with just a couple of much larger ones.

b) Why does an atomic model fit one better than the other? Some possible tests for model bias and related issues are suggested below.

i) Calculate a composite omit map (with refinement) instead of a 2Fo-Fc map and analyze this map. For example one could do this by: (1) adjusting the Wilson B of the synchrotron and XFEL datasets to the same value. (j2) removing anisotropy, (3) setting the cell constants of the two datasets to both be equal to the APS dataset, (4) refining the APS model against both datasets, (5) calculating the refined composite omit map, and (6) comparing the map to the model. When one of the reviewers (TT) did this, he found adjusting the cell dimensions didn't change the Rfree for the XFEL dataset very much (Rfree=0.34 compared to 0.33 using original cell parameters). He obtained very similar correlations of XFEL and APS composite omit maps to their respective refined models in the region of the models (0.75 for XFEL vs. 0.74 for APS). The correlation calculated over the entire unit cell was somewhat better for the APS data (0.62 vs. 0.59). This result would suggest that the APS data are at least as accurate as the XFEL data.

ii) Calculate a Fo(XFEL) – Fo(synchrotron) map phased with model phases (either model). This again requires the assumption of equal cell dimensions. This map should show differences between the density corresponding to the two datasets and would be expected to have peaks at positions of side chains that are radiation sensitive (or perhaps at sulfur positions). TT calculated such a map and could not see any such pattern of density in the map (it looked almost random but not quite as there were more peaks in the protein region than in the solvent). This did not provide any evidence for a systematic difference between the two datasets at positions of radiation-sensitive atoms. It is possible that the cell dimensions really are different, affecting the difference map (although the similar free R value obtained above with different cell dimensions would argue against this interpretation).

iii) Calculate correlation or R-values of data from APS data collected at lower dose or higher dose with XFEL data. This could be done by processing just early frames of APS data or just late frames of this data and comparing each to the XFEL data. If radiation damage is less in the XFEL data it might be expected to correlate better with the early APS data (though other interpretations would still be possible). See also (a)(ii), above.

The authors suggest that the XFEL dataset had less radiation damage because the correlation difference was bigger for those side chains known to be more sensitive to radiation damage. But among the 7 side chains with the largest differences, four (Gly, Lys, Ser and Gln) are not thought to be sensitive, while Glu, one of the most sensitive, is only 13th in the sorted list. Are the Cys residues involved in di-sulfide bridges? These are far more sensitive than a cysteine. Thus, it seems likely that, while radiation damage may be a contributing factor to the observed differences, it is not the whole story.

In summary, the new software is an advance, but the reviewers are not convinced by the second conclusion – which is in any case not needed to qualify for a Research Advance publication – that "XFELs can improve upon the data obtained from synchrotrons". It has clearly done so (somewhat marginally, but nonetheless properly documented here, including the local real-space correlations, etc.) for this particular synchrotron data set, but the thoughts just outlined illustrate why that data set might not have been optimal and why the comparison may to some extent be apples and oranges.

Thus, the authors should revise the text to avoid conclusions about data "quality" and rather should focus on what this Advance is really about anyway – the new algorithms and software that implements them. To the extent that comparison with synchrotron and simulated data allows them to assess the new methods, inclusion of those comparisons is excellent. But avoid comparing what cannot, at this stage, be properly compared.

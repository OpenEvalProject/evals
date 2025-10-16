# Peer review - Round 1

Editors:
- Muireann Irish, University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.45591.023](https://doi.org/10.7554/eLife.45591.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cortico-hippocampal network connections support the multidimensional quality of episodic memory" for consideration by eLife. Your article has been reviewed by Laura Colgin as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Though features within an event are thought to be integrated to form episodic memories, it is not known how the connectivity between the hippocampus and neocortical regions drive the quality of multidimensional memories. Cooper and Ritchey conducted an experiment whereby participants learned a series of objects consisting of colors, scene locations, and emotions. These features were then tested using continuous measures of memory quality. More specifically, the connectivity between neocortical representations in the posterior-medial/anterior-temporal ("PM/AT") network was examined during encoding and retrieval. Reconstruction of memories during retrieval was associated with increased hippocampal connectivity with other regions that scaled with both the number and quality of features, with dissociable regions representing the precision of individual features. These results have significant implications for our understanding of how memory networks support the retrieval of multidimensional episodic memories in high fidelity.

The authors are to be commended for conducting an extremely rigorous and innovative study, which is expected to have a significant impact on the field. The paper was found to be beautifully written and the analyses, while rigorous and detailed, were found to be presented in an extremely clear and concise manner. However, some major issues were raised that need to be addressed.

Essential revisions:

1) Each event was studied for only 6 seconds. However, during retrieval, participants seem to have much more time to think about the object, as well as to explore each scene during the reconstruction of location (12 seconds in total?). This reconstruction period thus exposes participants to more information and for a longer time than during encoding. Could it be the case that hippocampal networks demonstrate greater connectivity during retrieval because the retrieval period is actually richer in informational content than the encoding period?

2) Clarification is needed for both the calculation of precision and the stochastic dependence of precision. Was it the case that the precision score obtained from the mixture model for each participant was used for further estimates of dependence (i.e. the correlation)? Or was it the case that individual errors that exceeded the "success" criterion calculated from the mixture model were used as the estimate of dependence? The former case would not be problematic, but the latter case may be, depending on how this correlation was conducted.

For example, if many errors per participant were used to derive the measure of dependence, was it the signed or absolute error? A trial with -40 color and +40 location error is identical to a trial with +40 color and +40 location error in terms of quality because the measure wraps around a circle, however there would be no correlation due to the sign. More elaboration of how precision was operationalized is needed here.

3) Related to the above point, did the gPPI measure take into account all the errors from 0-180 along the circle? Or did this measure only account for the "success" trials?

4) More justification/elaboration was needed for the present definition of "gist". From the mixture model analyses conducted in this paper (1 – guess rate), "gist" memories can simultaneously contain low and high resolution features, features that are all high in resolution, and features that are all low in resolution. This is because the stochastic dependence measure of success does not seem to distinguish between whether a feature memory is a high resolution success versus a low resolution success.

5) Related to the above point, reviewers appreciated the inclusion of anterior/posterior HC contributions given increasing interest in functional subdivisions along the long axis of the HC. However, the authors should consider looking at the granularity of representations along the HC long axis in a dimensional way (e.g., Brunec et al., 2018) rather than an anterior/posterior subdivision, as it is likely that the manner in which the HC is subdivided influences the resultant connectivity profiles.

6) The failure to find differences along the hippocampal long axis may also reflect the particular stimuli used in this experiment, rather than the broader/richer spatial and autobiographical categories utilized in other work (e.g., Sheldon et al., 2016), or large-scale virtual reality navigation (e.g., Brunec et al., 2018). This point also relates to the definition of "gist" comment made previously.

7) In Subsection “Dissociable PMAT connections predict the precision of recalled item and spatial features”, the authors present analyses from 4 seed regions of interest. While readers can perhaps intuitively appreciate why the authors focused on these 4 seed regions, it would be helpful to present some rationale for these analyses and the choice of seed regions. For example, why did the authors choose the PHC and RSC over the PCC or ANG? Just one sentence, explaining the motivation for choosing the seed regions (over others) would be helpful.

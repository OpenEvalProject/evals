# Peer review - Round 1

Editors:
- Timothy D Griffiths, University of Newcastle United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56963.sa1](https://doi.org/10.7554/eLife.56963.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work projects cytoarchitectonic areas after the well-established Munich scheme onto the superior temporal plane defined by 7T MRI using two types of coregistration based on curvature based alignment. The authors make the case that one type, based on priors tailored to temporal lobe surface landmarks, gives a better surface map of the cytoarchitectonic areas that is more consistent across subjects. The work is a Tools and Resources report, which explains the advance well and provides a clear practical guide for readers who wish to use it to interpret functional imaging data from group or group-case-studies data.

Decision letter after peer review:

Thank you for submitting your article "Improving a probabilistic cytoarchitectonic atlas of auditory cortex using a novel method for inter-individual alignment" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Christopher I Petkov (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The work projects cytoarchitechtonic areas after the well-established Munich scheme onto the superior temporal plane defined by 7T MRI using two types of coregistration based on curvature based alignment. The authors make the case that one type, based on priors tailored to temporal lobe surface landmarks, gives a better surface map of the cytoarchitechtonic areas that is more consistent across subjects. There will never be a perfect map because the cytoarchitechtonics do not rigidly correspond to anatomical landmarks between subjects but this technique is potentially useful in studies of individuals or groups for getting an idea of localisation of activity with respect to the cytoarchitechtonic areas. And it seems to cope well with the common HG duplication. The reviewers raised the following issue that need to be addressed.

Essential revisions:

1) Clarification of the general potential advance

• The authors need to make a better case that the complex superior alignment process is 'worth it' for gaining insight into the auditory system in functional auditory studies, as opposed to informing debate about parcellation of the human auditory cortex. This is required for publication as a Tools and Resources article.

• As 7T studies have small sample sizes and often do analyze individuals' data separately, the need for and benefits of making a precise alignment between subjects as opposed to individual-level analysis needs to be clarified. In the Discussion, the authors note that the lack of a full tonotopic gradient in Te1.0 "may be the result of excessive smoothing caused by inter-subject averaging."

• The paper does not cite earlier studies that have used landmark based registration to improve human auditory cortex mapping (e.g. Kang et al., 2004). A more careful discussion of how the approach has moved on with CBA+ is warranted.

2) Clarification and quantification of the CBA+ advantage

• The paper is largely qualitative and the claim that the CBA+ is superior is not quantitatively demonstrated. This can be done in a number of different ways including some quantitative measure of the overlap maps or the distribution of overlap with the gold standard anatomical area probabilistic maps.

• Was any comparison made with techniques other than CBA?

• The authors make a point that individual subject maps may be important to show but do not actually show them.

• Since it seems the authors also have to select landmarks, it is worth knowing how reliable different raters might be in picking those landmarks and whether a specialist is needed to do so.

3) Practical implementation

• If the main contribution is the alignment technique itself, more information and perhaps resources about the technique's application could increase its impact. For example, how can other researchers go about using it? (For example, software access? How manual/involved is the use? The individual cyto-architectonic areas are made available, as are some of the other resources like the segmentation algorithm, but would a reader need to implement the CBA+ portion themselves?) Is the group-derived atlas somehow useful by itself to other researchers or was it more of a proof-of-concept? What are the applications and limitations? For example, can the parcellation be applied to 3T MRI data or is the 7T resolution necessary to benefit from CBA+?

• Because the manuscript has been submitted in the Tools and Resources category, the goal of which is to assist prospective users in deploying the technique within their own work, more could be done to guide the reader in the application of the CBA+ technique (subsection “Cortical surface alignment”). From the description, a new user might struggle to specify macro-anatomical landmarks or where to start running that portion of the analysis, which seems to be the critical advance.

• Software/scripts/tutorial steps to implement the technique on a sample dataset would be helpful (e.g. Stropahl et al., 2018).

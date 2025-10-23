# Peer review - Round 1

Editors:
- Ming Meng, https://ror.org/01kq0pv72 South China Normal University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86037.sa0](https://doi.org/10.7554/eLife.86037.sa0)

This valuable study presents a tool for hyperaligning functional brain topography between individuals, which is based on fMRI connectivity data gathered when participants watched different movies. The tool is validated through strong correlations between functional topographic maps generated from a participant's own localizer data and those derived from other participants' data based on this hyperalignment, even when the training and target participants were drawn from different datasets. The study will potentially be of interest to researchers working with a wide range of fMRI datasets.


---

# Peer review - Round 1

Editors:
- Ming Meng, https://ror.org/01kq0pv72 South China Normal University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86037.sa1](https://doi.org/10.7554/eLife.86037.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cross-movie prediction of individualized functional topography" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Ming Meng X as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Chris Baker as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Zonglei Zhen (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Add discussion of the limit of the present hyper alignment approach: for example, to what extent the present hyper alignment approach would be applicable to individuals with atypical functional brain topography such as brain lesion patients with e.g., acquired prosopagnosia? Even in typical populations, while bilateral fusiform face areas can be identified in the majority through functional localizer scans, the left fusiform face area sometimes cannot be found. Moreover, many top-down factors are known to modulate functional brain topography. Due to these factors, brain responses and functional connectivity may be different even when the same subject watched the same movie twice (e.g., Cui et al., 2021).

2) Explain how the length of movie-viewing fMRI may affect the accuracy in predicting the idiosyncratic cortical topography? Similarly, how does the number of participants in the normative database affect the prediction of the category-selective topography? This information is important for the researchers who are interested in using the approach in their studies.

3) The data show that category-selective topography can be accurately estimated using connectivity hyper alignment, regardless of whether different movies are used to calculate the connectome and regardless of other data collection parameters. However, can the functional connectome from resting state fMRI accomplish the same as the movie-watching fMRI? If yes, this would expand the approach to much broader data.

4) The authors averaged the hyper-aligned functional localizer data from all of the subjects to predict individual category-selective topographies. As there is large spatial variability in the functional areas across subjects, averaging the data from many subjects may blur the boundaries of the functional areas. A better solution might be to average those subjects who show highly similar connectome to the target subjects.

5) Add discussion to clarify relations between the present hyperalignment approach and approaches in the literature that address the same question. Specifically, as reviewer #2 pointed out, 'Saygin and her colleagues have demonstrated that structural connectivity fingerprints can predict cortical selectivity for multiple visual categories across cortex (Osher DE et al., 2016, Cerebral Cortex; Saygin et al., 2011, Nat. Neurosci). I think there's a connection between those studies and the current study. If the author can discuss the connection between them, it may help us understand why CHA work so well.' And as reviewer #3 pointed out, 'the authors do not cite a paper that has already successfully demonstrated a functional alignment method that can address exactly this need: a connectivity-based Shared Response Model (cSRM; Nastase et al., 2020, NeuroImage). It would be relevant for the authors to consider the cSRM method in relation to their enhanced CHA method in detail. In particular, both the relative predictive performance as well as associated computational costs would be useful for researchers to understand in considering enhanced CHA for their applications.'

6) Justify the particular six step, iterative approach. That is: why were six steps chosen over any other number? At present, it is not clear if there is an explicit loss function that the authors are minimizing over their iterations. The relative computational cost of six iterations is also likely significant, particularly compared to previous hyperalignment algorithms. A more detailed theoretical understanding of why six iterations are necessary-or if other researchers could adopt a variable number according to the characteristics of their data-would significantly improve the transferability of this method.

7) The existing evaluations for enhanced CHA appear to be entirely based on image-derived correlations. That is, the authors compare the predicted image from CHA with the ground-truth image using correlation. While this provides promising initial evidence, correlation-based measures are often difficult to interpret given their sensitivity to image characteristics such as smoothness. Including Cronbach's α reliability as a baseline does not address this concern, as it is similarly an image-based statistic. It would be useful to see additional predictive experiments using frameworks such as time-segment classification, inter-subject decoding, or encoding models.

8) Make available the code for implementing CHA, or justify why this could not be done at the present.

Reviewer #1 (Recommendations for the authors):

In addition to adding more discussions on the limit of the present hyperalignment approach as I mentioned in the public review section, I would suggest more direct comparisons of the current CHA results and previous RHA results. I.e., perhaps consider moving Figure S2 to the main text?

Reviewer #3 (Recommendations for the authors):

– On L336 of The Raiders Dataset, the authors note that a subset of nine of the original eleven participants are included in the current experiments; however, from the current it is not obvious why two participants were excluded.

– Please confirm the radius of the searchlights used throughout the experiments. For example, in L361 of Connectivity Hyperalignment (Step One) the searchlight is described as 13mm radius, while on L370 of the same section it is a 15mm radius.

– In Figure S2, I noted the following two typos: In section (A), The second axis description should read "Values on the x-axis stand for correlations between each target participant's own localized-based topographies and topographies from other participants in the same dataset using CHA." In section (B), "Conbach's alphas" should be "Cronbach's alphas."

– In Figure S3, the in-figure legend (e.g., F to B) does not appear to relate to the figure content and is not explained in the figure description.

– It seems that code for implementing CHA is not currently available, as the GitHub repository listed in the Data Availability (but not in-text) does not contain executable code as far as I can tell. This would be particularly useful for other author's hoping to apply this method in their own datasets!

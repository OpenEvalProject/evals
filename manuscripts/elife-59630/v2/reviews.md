# Peer review - Round 1

Editors:
- Greg Finak, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59630.sa1](https://doi.org/10.7554/eLife.59630.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work is an important contribution to the field of cytometry. It provides an objective and well thought out normalization procedure for mass cytometry and potentially even fluorescence flow cytometry.

Decision letter after peer review:

Thank you for submitting your article "CytofRUV: Removing unwanted variation to integrate multiple CyTOF datasets" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Nima Aghaeepour (Reviewer #1); Anna Belkina (Reviewer #3); Sofie Van Gassen (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The authors present a new Cytof normalization approach based on RUV III that has proven useful for other technologies including RNASeq, single-cell RNAseq and nanostring. The reviewers all agreed that this was a strong manuscript that makes an important contribution to an area of the field that remains under-served, and they unanimously recommended publication.

Essential revisions:

Several concerns arose during review that the authors should address to strengthen the results and improve the presentation.

1) Given the size of typical cytometry data sets (millions of cells and hundreds of samples), how does this approach scale? What are the limitations? The Discussion mentions large-scale studies, but how large in practice?

2) Most importantly, reviewers raised questions around the evaluation of the normalization procedures. Specifically, since the data are re-clustered after normalization, and performance of normalization was assessed against the re-clustered data (and while the reviewers agreed this made sense), they were concerned about how a negative impact of normalization could be assessed. Specifically, if normalization failed, leading to fusion of biologically relevant clusters post-normalization, how could that be detected? It was not clear that this would be captured by Sbiology (as pre- and post-normalization Sbiology measures are not compared), nor how and if the proposed figures and evaluation measures could be interpreted to detect this situation. The reviewers felt this aspect needed further exploration and discussion.

3) Finally the reviewers were looking for more guidance from the presentation around the relative ranking of the different methods. The authors should more clearly present their conclusions about the relative performance of the methods and state which methods are performing well or poorly and why, and if the results are not conclusive, this should be stated and explained.

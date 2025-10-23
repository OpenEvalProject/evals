# Peer review - Round 1

Editors:
- Stephen Tollman, Wits University , South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02020.018](https://doi.org/10.7554/eLife.02020.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Diagnostically-relevant facial gestalt information from ordinary photos” for consideration at eLife. Your article has been favorably evaluated by a Senior editor, Detlef Weigel, a Reviewing editor, and 2 reviewers, one of whom, Peter Claes, has agreed to reveal his identity.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

With genome sequencing having become cheaper and cheaper over the past few years, the bottleneck in genetics is increasingly shifting to accurate, inexpensive phenotyping. Even for Mendelian genetic disorders, misdiagnosis rates are shockingly high. A sizeable fraction of genetic disorders is associated with craniofacial abnormalities, and the approach presented in this study greatly facilitates the acquisition and analysis of craniofacial information from simple photographs, as opposed to more complex 3D scans that are not necessarily suitable for every day medical diagnostics. The reviewers felt that the work was of high quality, and they had only some minor comments that need to be addressed in the revision.

From Reviewer 1:

The simple term “Face-Space” for the new representation presented by the authors is confusing. When doing a simple search on the internet, the concept of a Face-Space is well known as a space coding for facial shape variations due to general differences like differences in identity and not necessary clinical phenotype. In face recognition and perception, the term face-space is already widely used and does not reflect the same space as presented by the authors. I suggest defining the new representation differently to avoid confusion, for example Diagnostic Face Space.

In the Introduction the advantages over current studies using 3D images is slightly exaggerated. The single most important, BUT major advantage of the proposed approach is the easy access to ordinary images in contrast to expensive 3D acquisition systems. Rare genetic diseases are hard to find and collect, and through the use of ordinary 2D images one manages to acquire a substantial amount of samples across the world (which is typically required in AI based image strategies). In 3D, pose and illumination variations do not matter as such (which is well-documented in the literature of 2D versus 3D face recognition [1]) because pose differences can be normalized and syndromic diagnosis is mainly done on shape (and not texture) only. In contrast 2D images suffer a lot from pose and illumination differences, and the use of LMNN is a clever way of reducing their effect in clustering for diagnostic purposes as proposed by the authors (as also shown by Weinberger and Saul 2009 on 2D face recognition data). The easy access to 2D images by itself is a strong argument in favor of the proposed approach.

It is intriguing to see the generalization capabilities of the “Face-Space”. Trained on only 8 syndromes, it is capable of being applied to a much wider range of syndromes.

With regards to the SVM classification on the raw feature space, it is unclear to me, why this is performed. It seems to be a 2D implementation of a syndrome classification comparable to the 3D based classification done in the work of Hammond et al. The way I can read this in the context of the remainder of the paper is: In essence a traditional classification in the raw feature space using SVM increased from 94.4%, to 99.5% in “Face-Space” using kNN classification. However, I'm not sure if this is correct or not.

What is the stability of the main axes in “Face-Space”? In other words, do the distance metrics change a lot when using 8 different syndrome classes than the ones used for training in the manuscript? Did the authors experiment along these lines or not?

Finally the clustering improvement factor is novel and seems like an interesting metric proposed by the authors. Due to its novelty it is hard to give an interpretation to the metric and a more elaborated sample computation of the metric using the database composition as presented in the manuscript would be helpful in the methods section.

From Reviewer 2:

There are a couple of areas where the authors could add to the paper: One concerns the nature of the appearance model. We know that the faces show quite significant rigid pose variations. Would the model be improved by explicit modelling of the 3D variation? Perhaps an approach similar to that adopted by Iain Matthews and collaborators, building simultaneous 2D and 3D models might be worthwhile.

The other area relates to alternatives to the LMNN transform. Did the authors consider any other transforms? Do they rely on fundamentally different features of the data? Do they have significantly different performances?

I do not believe that either of these areas require additional computation – really just a short discussion to show the reader that there are alternative techniques within this area and choices have to be made about the computational and modelling techniques.

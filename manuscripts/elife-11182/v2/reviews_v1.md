# Peer review - Round 1

Editors:
- Werner Kühlbrandt, Max Planck Institute of Biophysics , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11182.023](https://doi.org/10.7554/eLife.11182.023)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Sampling the conformational space of the catalytic subunit of human γ-secretase" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Kuriyan as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a well-written manuscript that adds a further useful step in the process of single-particle reconstruction, especially where there is significant conformation and/or compositional heterogeneity. The central idea is to mask the background in a way that also takes advantage of the knowledge of the orientation of each particle in the projection image, leading to a more accurate way to carry out localized or "focused" refinement. Nevertheless, both peer reviewers query the novelty of the approach and have a number of other concerns, some of them substantial, which would need to be addressed in a revised manuscript.

Essential revisions:

1) The central idea of the manuscript has been around for a while. It is surprising that the authors do not cite papers which have taken a similar approach to subtraction of residual signal in earlier work, especially studies of viruses by cryo-EM. See for example:

"Structural analysis of viral nucleocapsids by subtraction of partial projections", Ying Zhang, Victor A. Kostyuchenko, and Michael G. Rossmann

http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1876683/

and:

"Bacteriophage phi29 scaffolding protein gp7 before and after prohead assembly", Marc C Morais et al.

http://www.nature.com/nsmb/journal/v10/n7/full/nsb939.html

Most likely Ludtke et al. have also described something similar many years ago in the context of studying GroEL by EMAN.

2) The authors refer to their methodology as "classification", while what they clearly mean is "clustering". This makes Figure 1 confusing, as the scheme is most likely a part of the iterative refinement process. The term classification is generally applied to algorithms for the assignment of items to given templates when the templates themselves and their numbers are known. What the authors do is clearly clustering, which normally describes a procedure which explores data structure, to detect natural groupings without a priori knowledge of group templates. This confusion in the EM field is not new, but instead of continuing the tradition, the authors might consider breaking with it or at least to specify clearly what they mean.

3) The method described in this manuscript appears to be based on a fundamental misunderstanding of the original design of the "focused classification", as originally developed by Penczek, Frank and Spahn, JSB 2006 (see Figure 2 and associated text in this paper). Moreover, Bai et al. claim that Penczek and Frank overlooked a basic inconsistency of the procedure, a notion that is challenged by one reviewer.

4) The method is not tested with simulated data. Instead of using only one experimental data set, it would be better to establish the general principles by using data sets derived from a known structure.

5) Unless the authors employ a non-linear projection algorithm, four operations in the upper left corner of Figure 1 commute. In other words, it makes no difference whether projections of two structures are subtracted from each other or structures themselves are subtracted and the difference projected. Possibly the impression that the figure implies otherwise stems from an imprecise description of the design.

6) Another main concern relates to the lack of biochemical purity of the γ-secretase sample. The authors describe an extra helix in 2 of the "apo" classes which they attribute to a co-purified protein, and they were even able to biochemically identify 4 extra proteins that were present in the sample. This raises the question whether the other state they see also has an extra protein bound to the γ-secretase complex and how much these contaminating proteins are influencing the "apo" γ-secretase structure they report both in this manuscript and in their earlier Nature paper. Similarly, because the density for the ligand is so poor in the 4.2Å map, it seems possible that the density they attribute to the inhibitor is actually a piece of one of the extra proteins in their sample. The reviewers wonder if the authors tried the same focused classification procedure on the liganded state that they used on the "apo" state, and whether that would give any insight into whether the "ligand" density they see is actually from the inhibitor or from one of the extra proteins.

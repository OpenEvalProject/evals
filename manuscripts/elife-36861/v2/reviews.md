# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36861.021](https://doi.org/10.7554/eLife.36861.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Characterisation of molecular motions in cryo-EM single-particle data by multi-body refinement in RELION" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Axel Brunger as the Reviewing Editor and Andrea Musacchio as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: John L Rubinstein (Reviewer #2); Nikolaus Grigorieff (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Scheres and colleagues describe an extension – multi-body refinement – of their software, RELION, to process images of single particles displaying large continuous heterogeneity that can be represented as motion of several independent rigid subdomains (the "bodies"). Their implementation follows a strategy that was applied previously, for example, to the ribosome and the spliceosome. The new tool is user-friendly and automates the steps established in these previous projects: masking of rigid subdomains by pre-defined masks, signal subtraction of parts of the particle outside the mask, focused refinement of the remaining domain, and combination of the separately refined domains to reconstitute the complete particle. In addition, the angles and translations for the subdomains can be analyzed using principal component analysis, and reconstructions with domains in intermediate positions can be calculated to visualize the motions. The new tool is applied to two previously published datasets, of Plasmodium ribosome and yeast spliceosome. Focused refinement itself is not new, but the new automated implementation in Relion should make it much easier to use when multiple focused regions (or multiple bodies) are necessary.

The multi-body refinement addresses an important problem in single-particle cryo-EM that occurs when domains of a complex move against each other without assuming distinct positions (conformations) relative to each other. This is one type of continuous heterogeneity that occurs frequently in large macromolecular machines. The authors demonstrate that multi-body refinement is an effective tool to improve the resolution of the subdomains. As they point out, features at the interfaces between the domains will not be reconstructed correctly.

Essential revisions:

The WarpCraft approach appears to be superior in preserving details at domain interfaces. The authors should discuss situations in which their multi-body approach would be preferred.

How does the visualization of the motion by principal component analysis work when the motion is not continuous, i.e. there are only a few discrete states? What if dividing the particles into M equi-populated bins according to the chosen eigenvalue is not possible because there are not sufficient particles for some bins?

The multi-body refinement results are compared with the consensus refinement results that were obtained by refining a single class. A more interesting comparison would be with the results obtained using traditional 3D classification assuming discrete states. In the ribosome example, this may yield results similar to the multi-body approach.

Some explanation of the rationale for choice of parameters subsection “A ribosome test case”and subsection “A spliceosome test case” would be valuable.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Characterisation of molecular motions in cryo-EM single-particle data by multi-body refinement in RELION" for further consideration at eLife. Your revised article has been favorably evaluated by Andrea Musacchio (Senior Editor), a Reviewing Editor, and three reviewers.

Reviewer #1:

I am satisfied with how the authors have addressed the concerns raised by the first round of reviews.

I caught a few typos.

Reviewer #2:

I am satisfied by the changes and think the paper should be published

Reviewer #3:

I read the authors' rebuttal and am happy with their replies. I think that the manuscript is ready for publication in eLife.

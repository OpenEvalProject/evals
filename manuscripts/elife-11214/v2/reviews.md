# Peer review - Round 1

Editors:
- Fiona M Watt, King's College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11214.038](https://doi.org/10.7554/eLife.11214.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "A versatile pipeline for the multi-scale digital reconstruction and quantitative analysis of 3D tissue architecture" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Fiona Watt as the Senior Editor. One of the two reviewers has agreed to reveal his identity: Gaudenz Danuser.

The reviewers have discussed the reviews with one another and the editor has drafted this decision to help you prepare a revised submission.

The reviewers were very positive about your manuscript and would like to see it published in eLife. While the complexity of the synthetic data is appreciably lower than the experimental data, these simulations challenge the image analysis pipeline in a relevant way. Using these simulations as a test set for such algorithms is going to be helpful. We would even suggest that you make the code and parameter files available that generate these volumes for other labs to generate systematic other test data sets.

One concern we have is that the manuscript should be re-written to make it easier to follow. The main text should describe in broad strokes the necessary image analysis steps to a fairly naive audience. Currently, there is a large fluctuation in the level of detail – sometimes, unnecessary information is highlighted in the main text, whereas other, important, concepts are left out. The authors should then discuss the strengths and source of failures of the chosen approaches. For a resource article the failures are as interesting as the successes.

The authors should also avoid claims of exclusivity as much as possible. Individually, none of the image processing steps is out of the ordinary. The authors' achievement is to combine all the steps together into a working system. That said, the authors have failed to cite recent papers that address some of the same aspects. For example, it would be interesting to compare the recent work on nucleus segmentation with work published by Philip Keller's lab or Gaudenz Danuser's lab, and discuss Sean Megason's work on cell segmentation in 3D.

A second area of concern is the comparison of the new methods to other liver tissue reconstructions. The authors claim that substantial differences between the present and cited work originate in the advances of the image analysis algorithms. However, is this really the case? Could this not be due to differences in the tissue fixation or image acquisition? Some of the cited references are fairly recent. This might offer an excellent opportunity to apply the new image analysis pipeline to data that has been analyzed by other means. Such validation would be necessary to support the statement that 'in comparison with most recent previous reports, our model therefore provides a more precise estimation of the geometrical characteristics of sinusoidal and BC networks.'

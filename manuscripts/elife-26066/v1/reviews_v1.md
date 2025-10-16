# Peer review - Round 1

Editors:
- Paul G Falkowski, Rutgers University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26066.042](https://doi.org/10.7554/eLife.26066.042)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Quantitative 3D-Imaging for Cell Biology and Ecology of Environmental Microbial Eukaryotes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal her identity: Heidi Sosik (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers made a number of constructive comments, which you should carefully address. These include:

Essential Revisions:

1) At the review stage, it was extremely difficult to find, understand, and evaluate the supplementary tables and videos. In place of the links on the download page, the editorial office sent me a zip file of the tables and videos with filenames that match the designations in the main manuscript and in your supplementary information, but some of those appear to be mislabeled or to contain the wrong information. For example, the file "Figure 3D—source data 1" looks like it just contains the statistical values listed for Figure 3—figure supplement 3—source data 1; whereas that latter file contains the principal component values from the figure. These all need to be checked and their contents appropriately described.

2) Samples were fixed in a high concentration of glutaradehyde (25%) which contributes strong autofluorescence, especially in the green region of the spectrum, that may confound the specific (dye-based) fluorescent signals. Have the authors compared the current images to images of samples fixed only with paraformaldehyde? Please comment.

3) The authors extract a large number of features from each sample. Have they performed a simple principal component analysis to determine which features are most informative? I would suspect that most of the discrimination power is contained within a relatively small subset of these parameters. Please discuss.

4) The thresholding procedure ("mean + 1.5 standard deviations") is arbitrary and depends on the density of fluorescent objects in the image as well as the level of the background. How is the fidelity of the classification impacted by the threshold level? Classification results using at least one other threshold level (e.g. mean+3 standard deviations) or an automated thresholding algorithm should be presented and discussed.

5) The authors claim to have imaged the "entire extent" of each well. However, the bright-field images will be strongly degraded near the edges of the wells due to the cone of transmitted light hitting the vertical edges of the chambers and thus missing the condenser. How was this issue addressed? If this is a simple case of over-statement, then a more accurate description should be used.

6) In terms of throughput, did the authors assess the utility of simple widefield microscopy (with deconvolution) as an alternative to confocal? This will allow for much faster data acquisition. This warrants some discussion.

7) Did the authors correct for channel bleed-through in the 4-color images? This is especially the case when using DiO and AF546. This combination may introduce some cross talk, confounding the classifier.

8) Did the authors compare the static threshold of 1.5 standard deviation above average with a more robust/sophisticated algorithm such as Otsu's method?

9) Very often, classifiers are built such that 50% of the data set is used to train, while the remaining 50% is used to test. Was there a reason the training set was such a small portion of the total data? Was this limited by manually classifying the organisms?

In summary, the reviewers generally appreciated this paper and we look forward to receiving a revised manuscript.

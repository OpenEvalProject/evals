# Peer review - Round 1

Editors:
- W James Nelson, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.14334.032](https://doi.org/10.7554/eLife.14334.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "TissueMiner: a multiscale analysis toolkit to quantify how cellular processes create tissue dynamics." for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Large scale tissue imaging is becoming an everyday tool in developmental biology, but high throughput analysis methods are restricted to few laboratories. Etournay and co-workers present a software platform for segmentation and tracking of 2D epithelial monolayers. The software provides a number of geometric outputs including deformation tensors and cell connectivity. As the tools within TissueMiner appear to be identical to those used by the authors previously (2015 eLife publication), the value of TissueMiner lies not its novelty or proof-of-concept, but squarely in the likelihood of it being used by an average researcher. Both reviewers felt that the software and current tutorials, while expansive, were far from user-friendly in their current implementation, and the tutorials, while extensive, assumed far more technical background than the average user would have. Nevertheless, both reviewers felt that TissueMiner, if improved as described below, would be an important advance and could be very useful to the community.

Some of the key problems encountered were:

1) Installation of the software is not user-friendly. Between the large size of the sample datasets (2+ GB each), and tedious GitHub interactions presented as a series of code fragments rather than a single script, it took one reviewer over an hour to get the sample data downloaded, and to deal with various docker virtual machine bugs. Even pulling the demo data down caused bugs due to permission errors that were not addressed in the tutorial.

2) Once docker was running, execution of the initial data processing step resulted in a dizzying array of analysis steps with no explanation of what was happening or how much time it would take.

3) Users must already have R installed, but this is not mentioned.

4) Preparing TissueMiner to run through RStudio should not require the user to copy-paste code fragments each time. A single script that does this should be included.

5) Tissue Analyzer – the preprocessing tool made by the same group and essentially required for use with Tissue Miner – works beautifully and has a series of video tutorials. This would be a good template for TissueMiner.

6) RStudio initialization script kept crashing. Apparently additional toolboxes are required, such as devtools.

Essential revisions:

In the context of the software, the reviewers specifically recommended that you:

1) Make the sample data much smaller in size (<2GB) so that the initial docker processing takes <5 min, or at least has a remaining time clock;

2) Make the software completely scripted, including all the initial importing in RStudio (no copy-pasting, just loading an RStudio file);

3) Prepare a new "First Use" R tutorial, skipping most of the R-101 training and just getting a user up and running with something simple, like plotting cell-area.

Then:

1) Conduct user testing with testers who truly have "no programming experience". Allow them to test installation unsupervised.

2) Create more streamlined, focused tutorials rather than an enormous master guide. TissueMiner tries to do everything at one time (e.g. the initial docker processing), and it is difficult to follow. Give the user the simplest data-set you can provide, and have them perform the simplest analysis (e.g. only focus on cell area, or tracking, or divisions).

3) The authors illustrate the capabilities of the software using the case of wing vein morphogenesis, but this is not a validation. To validate the software, the authors could use computer generated images of cell monolayers with known geometry, and demonstrate that the software is able to recover the different geometric parameters of each cell in the tissue.

# Peer review - Round 1

Editors:
- Volker Dötsch, Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70576.sa1](https://doi.org/10.7554/eLife.70576.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The analysis of large data sets obtained from omics or other approaches is often the most time consuming and difficult step of a study. Deep learning and related computational approaches offer the possibility to train a software on a certain data set and then analyze large new experimental data sets. The authors describe the software architecture and demonstrate the application of the system on three different topics: prediction of phosphorylation, prediction of transactivation potential of peptides and prediction of aggregation propensity. They compare the results of their new software PARROT with other existing software tools.

Decision letter after peer review:

Thank you for submitting your article "PARROT: a flexible recurrent neural network framework for analysis of large protein datasets" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Volker Dötsch as the Senior and Reviewing Editor and Reviewer #2.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) A suggestion would be to provide a bit more information about how non-experts can validate the results from PARROT, both in the documentation and main text. Because the authors are targeting non machine learning experts--and providing many useful defaults--they should think about how a non-expert might use the tool. Would a non-expert know when to use a ROC curve versus some other metric? Obviously, the authors should not write a ML textbook here, but think carefully through ways to guide users to appropriate tests.

Two ideas:

1) Have PARROT spit out a stack of test results by default, rather than the few it defaults to now. You could put this behavior under a flag (e.g. --testsoff) so more advanced users would not get bombarded by spew, but otherwise confront the user with as many validation metrics as possible.

2) Encode some warning heuristics for common errors. For example, PARROT could warn the naive users that their training set was unbalanced.

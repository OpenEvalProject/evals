# Peer review - Round 1

Editors:
- Joseph K Pickrell, New York Genome Center & Columbia University, United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10005.010](https://doi.org/10.7554/eLife.10005.010)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Assessing ancient DNA authenticity with low-coverage data: a case study of wheat in the British Isles 8,000 years ago” for peer review at eLife. Your submission has been favorably evaluated by Mark McCarthy (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors use an approach based on testing whether C-to-T damage patterns seen in degraded DNA fits a model of exponential decay from sequence termini in order to test a recent claim of 8,000 year old wheat DNA at a submerged site in Britain (Smith et al. 2015, Science).

Essential revisions:

The reviewers identified two additional analyses that they considered essential:

1) The authors should show visually the damage patterns in the reads from Smith et al.; even if this plot is noisy, it will provide some visual sense of the data.

2) The authors should provide some analysis of whether their results are robust to the choice of aligner. BWA-MEM uses extensive soft-clipping, which distorts patterns of damage. The authors should consider BWA-ALN/samse as an alternative.

Other reviewer comments below are provided as suggestions but need not be addressed in a revision.

Reviewer #1:

In this paper, the authors critically assess a claim from Smith et al. that wheat was present in the UK 8,000 years before present. Specifically, they argue that the sequencing reads claimed to come from ancient wheat samples in this study are instead most likely to be modern contaminants based on patterns of DNA damage.

1) The Smith et al. claim is based on 152 sequencing reads, and so the authors here have little to work with. However, they claim that the expected exponential increase in C->T substitutions in these reads is not present. It would have been nice to see the patterns of DNA degradation of these reads visually, rather than it being summarized by the p-value from their test. Why do the authors not show a figure like Figure 1A, except using the 152 reads from Smith et al? This would be extremely useful for visually determining if the expected damage patterns are present (even if the plot is extremely noisy due to small numbers of reads). The authors could show the pattern from the empirical data superimposed on damage patterns in their subsampled ancient and modern libraries.

Reviewer #2:

Weiß et al. develop a pipeline to assess the authenticity of results of analyses of ancient sedimentary DNA, and use this pipeline to test recently published results. Such a pipeline is a useful tool for ancient sedimentary analyses, and is likely to be widely adopted in the field. I found the paper to be well written and straightforward. I have only one major query.

The authors choose to use BWA-MEM for alignment, which may not be the most appropriate aligner for this test and is likely to affect the results. This aligner (BWA-MEM) performs a lot of soft-clipping (unless the settings were modified from default, in which case the authors should state this), which causes two major issues. First, it makes misincorporation profiles unreliable. Second, it can cause a lot of random mapping. I strongly recommend the authors re-run these analyses using a more appropriate aligner, e.g. BWA-ALN/samse.

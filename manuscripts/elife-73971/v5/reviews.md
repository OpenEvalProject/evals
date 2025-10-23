# Peer review - Round 1

Editors:
- Naama Barkai, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73971.sa0](https://doi.org/10.7554/eLife.73971.sa0)

De Rop et al. introduce a flexible microfluidics-based single-cell genomics technology that expands and improves previously existing custom droplet-based scRNA-seq protocols (inDrops and Drop-seq) in interesting directions: better data quality, simplified workflow, high-cell recovery, and flexibility towards other single-cell applications.


---

# Peer review - Round 1

Editors:
- Naama Barkai, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73971.sa1](https://doi.org/10.7554/eLife.73971.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article “HyDrop: droplet-based single-cell ATAC-seq and single-cell RNA-seq using dissolvable hydrogel beads” for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Klaas Mulder (Reviewer #3).

The reviewers are excited about your paper, we will be happy to publish it, but please address the suggestions made below.

Reviewer #1 (Recommendations for the authors):

The paper is clearly written and it Includes enough methodological details, for example explaining the rationale behind some of the modifications benchmarked and later selected in the HyDrop protocol. Moreover, the authors exemplify the application of HyDrop to different contexts (e.g. low-input samples). For all these reasons, I think this is an outstanding candidate for publication in eLife.

Reviewer #2 (Recommendations for the authors):

Specific comments for the authors:

1) The introduction (line 38) contains the following statement "Primers carried or released by the bead allow each individual cell’s mRNA to be indexed inside the droplet".

This is indeed the case for the inDrop method, however is incorrect for Drop-seq, where the RT reaction takes place after emulsion breaking. Therefore, this sentence does not represent both methods accurately. However, this distinction is important to make as these are the main methods HyDrop is compared to.

2) Figure 1 and Figure 1—figure supplement 2. The produced hydrogel beads do not seem perfectly monodisperse and uniform in their fluorescent signal after barcode production. It might be good to mention this in the text and briefly discuss whether this will potentially impact the detection of heterogeneity in the cell population after sequencing, or not.

3) Figure 1—figure supplement 6c, the 6uM primer beads are concluded to be the best option for the HyDropRNA application. The images of these beads show some punctate intensities. Would the authors like to comment on this briefly? This could raise some questions for the readers, potentially leading to doubts about how to best adopt the method.

4) Figure 4—figure supplement 1b, please indicate in the legend what the colors encode.

5) The linear amplification method to add the barcodes to the beads (and in the scATAC workflow) is non-standard, would the authors be able to provide an estimation of the rate (or proportions) of errors introduced into the barcodes during this process? The authors state that 88% of the detected barcodes are in the ‘'whitelist’' (1 mismatch allowed). What is the distribution of mismatches in the 12% of the barcode that were discarded? Would that be of interest to estimate the error rate of the linear amplification step?

6) On the conclusion stated on line 116 on the optimal bead primer concentration: it seems that adding half the concentration of primer (6 instead of 12 uM) leads to 10x less reads. Which concentration would they in the end advice and in which context? (not mentioned clearly).

7) Line 258: This sentence is confusing. Some points they elaborate on (use og GTP/PEG for molecular crowding) others they just refer to other papers (use of LNA). Maybe cut into different sentences with explanation and referral to supplemental figure? The overall conclusion can still be linked to the main figure.

8) Figure 8c, It seems from the methods section that the filtering of the InDrop and Drop-seq data is not the same? What happens you perform the same filtering as with your HyDrop analysis?

9) Line 284: the header states HyDrop-ATAC, whereas the experiment and text are on HyDrop-RNA.

10) Line 327. Were the discussed neuronal cell populations also detected in the in-house generated Drop-seq experiments? It would be good to include a mention/discussion of this in the text.

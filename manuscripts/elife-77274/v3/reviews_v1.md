# Peer review - Round 1

Editors:
- Armita Nourmohammad, https://ror.org/00cvxb145 University of Washington Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77274.sa0](https://doi.org/10.7554/eLife.77274.sa0)

This manuscript presents a computational approach to identify T-cells that can mount an immune response against tumors. The authors examine the presence of clusters of T cells with similar sequence as a surrogate for tumor antigen-specific responses. The identification of tumor-specific responses within the background of bystander T cell infiltration is an area of great current interest. This study provides solid support that T cell sequence clustering can be used to identify tumor-specific responses in vivo and in vitro.


---

# Peer review - Round 1

Editors:
- Armita Nourmohammad, https://ror.org/00cvxb145 University of Washington Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77274.sa1](https://doi.org/10.7554/eLife.77274.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Pinpointing the tumor-specific T-cells via TCR clusters" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Satyajit Rath as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yuval Elhanati (Reviewer #1); Benny Chain (Reviewer #2); Giulio Isacchini (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Please include a description of the ALICE algorithm so the manuscript becomes self-sufficient.

2. ALICE is a powerful method since it can find reactive T cells without a background before sample. But for the scenarios in the paper, a before sample usually exists, which can help identify the reactive clusters and clones.

Are these samples used to inform ALICE? If not, it should be discussed how they can used to strengthen the analysis.

3. Please better describe the differences between different T-cell subgroups, which are sorted based on receptor such as IL2, IL21, etc. These descriptions should make the paper more accessible to the broader audience.

4. In the first result section, and in figure 1, it is shown that normalized ALICE hits increase following treatment. But it's not clear how this effect differs between responders and non-responders. This should be added as a figure or at least described in the text.

5. Melan A is a rather unusual TAA, because of the high precursor frequency of melan A specific T cells. Please include a discussion on this point in the Discussion section.

6. Please clarify the figure captions and descriptions (in the text) by thoroughly addressing all comments from reviewer #3.

7. Please clarify the online methods by thoroughly addressing the comments from reviewer #4.

Reviewer #1 (Recommendations for the authors):

– In the last paragraph of the introduction, a comma or space seems to be missing between CD8+ and CD39+PD1+, at least if indeed the CD39+PD1+ refers also to the CD4+ cells.

– Also in the same paragraph, the acronym TAA is used, but it's not defined outside of the abstract.

– ALICE is a powerful method since it can find reactive T cells without a background before sample. But for the scenarios in the paper, a before sample usually exist, that can help identify the reactive clusters and clones. Is it used in some way in ALICE? If not, it should at least be discussed how it can used to strengthen the analysis.

– Various cytokines and receptors such as IL2, IL21, CD137 and CD39 are used to separate T cells of interest, often without describing their function and role. For the wider audience in eLife, these should be described in context, so the different groups of T cells used are clear.

– In the first Results section, and in figure 1, normalized ALICE hits are shown to increase following treatment. But it's not clear how this effect changes between responders and non-responders. This should be added as a figure or at least described in the text.

– The last section in the results seems to have little relation to the main analysis method in the paper, and maybe should be omitted.

– In the methods section "Cluster analysis of TIL TCRβ repertoires", the following sentence is unclear – "we normalized the number of hits between samples based on the number of the top-frequency input clonotypes."

Reviewer #2 (Recommendations for the authors):

This study is on the whole convincing and interesting. I felt that the figures, while aesthetically pleasing, could have been explained in more detail, and were somewhat hard to follow.

1. I would like to know more about the set of matching TCRs in VDJdb – how many, against what antigens, are the annotated TCRs themselves highly clustered.

2. For example, in 1C, in the clusters, does this mean that all TCRs were also found in VDJdb? Or does this mean that there was only a tiny cluster and so one hit was close to 100%? What is the individual red dot in panel 1 d? What exactly does the y axis in f mean? Is this the proportion of TILs which fall in an ALICE cluster?

3. A bit more detail on running the ALICE pipeline would be helpful. I couldn't see anything about this in Methods.

4. A bit more explanation of the y axes in general would be helpful. What exactly is the calculation for normalised ALICE hits, etc.

5. I like the point in Figure 2 that phenotype is sometimes not enough, but needs sequencing alongside. This is an important message to the field.

6. I don't quite understand the gigantic clusters of TCRs in Figure 3, and why they all seem to be red. This comes back to point 1 I think. I don't quite understand how stimulating a population in vivo gives rise to these huge clusters, all within 2 aa of each other? Maybe I am not understanding this figure – again a bit more detail saying what exactly is being done and shown would hugely improve the impact.

7. Melan A is a rather unusual TAA, because of the high precursor frequency of melan A specific T cells. Might be worth discussing this in a bit more detail in the Discussion.

In summary, this is a very interesting and important piece of work. But more thought on clarifying what is being done, and how it is being shown would hugely improve the study and increase the number of readers.

Reviewer #3 (Recommendations for the authors):

Some more explanations (in the main text as well) on the Alice algorithm would be useful for those that are not familiar with the approach.

Moreover, also in the Online Methods some clarifications are needed:

– It is mentioned that the number of Alice hits depends on the initial variability of the repertoire: can you show it with an SI figure?

– Where does the normalization with respect to top-frequency clones comes from? Is an heuristic approach or has it a proper basis? Why does it work?

– Is the default pgen model used? Why not inferring a pgen model for each of the patients?

– The Alice algorithm should work with clusters of hamming distance one. Why visualizing clusters of hamming distance up to 2?

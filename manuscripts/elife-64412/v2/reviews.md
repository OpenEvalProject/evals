# Peer review - Round 1

Editors:
- Pierre Sens, Institut Curie, PSL Research University, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64412.sa1](https://doi.org/10.7554/eLife.64412.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The way homologous chromosomes identify one another and become paired is an intriguing phenomenon that has a long history of study, yet the molecular mechanism remains unclear. Recent studies have led to a phenomenological button model for homolog pairing, which hypothesises that pairing is initiated at discrete sites along the length of each chromosome. The authors investigate this idea rigorously using biophysical modelling and live imaging. They constructed a simple polymer model with buttons distributed along the chain that possess locus-specific interactions, and thoroughly investigated its property via stochastic simulation in 3D. Their study confirms that homolog-specific interactions are necessary for homolog pairing. The authors went on to perform live imaging of pairing dynamics at two selected loci, using the fluorescent signal from nascent mRNA at the corresponding locus, and found satisfactory agreement with the model. Their study supports a button mechanism for homolog pairing, where stable pairing is initiated by reversible random encounters that are propagated chromosome-wide. This work suggests that active processes are not necessary to explain pairing and paves the way for further investigating the molecular mechanism of such a pairing phenomenon.

Decision letter after peer review:

Thank you for submitting your article "Live imaging and biophysical modeling support a button-based mechanism of somatic homolog pairing in Drosophila" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Shou-Wen Wang (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The referees unanimously found your work to be interesting. and highly relevant to the field of somatic homolog pairing in Drosophila. There is a number of points that need to be addressed before a final decision can be made regarding publication.

1. The theoretical model here described is a close variant of a model introduced some years ago in Genetics 179, 717 (2008). As its title clearly shows ("A Thermodynamic Switch for Chromosome Colocalization"), that paper envisaged a mechanism whereby the interaction energy between specific regions on the homologs thermodynamically stabilises their random encounters, producing a transition from an unpaired to a paired state. I think that the authors should clearly acknowledge that previous paper in their manuscript as required by the best practices of the scientific community.

2. While the authors convincingly show that the button model can explain homolog pairing, their data show areas of quantitative disagreement, which might highlight the need for future improvement of the modeling and experimental design. Specifically: the model does not accurately reproduce the observed pairing probability over developmental time (Figure 4B). The author already commented on the discrepancy at time=6h. I found the discrepancy at t=0h also puzzling: while the observed pairing probability is around 0 for both loci, the model predicts a 10% pairing probability at t=0. A comment or explanation here will be very useful for the readers.

3. Similarly, in Figure 5, while the model accurately reproduced the post pairing behavior under constrained parameters, the pre-pairing dynamics are not well reproduced: the observed inter-locus distance decreases linearly with time, while the predicted decrease has a rather nonlinear pattern, speeding up as the pairing is being established. An explanation here is useful.

4. The size of buttons should be addressed – small vs. large buttons. The authors build their model around a 10 kb button size. It is not clear why they only tested this button size. In the Rowley and Alhaj Abed studies, they conducted HiC which reflects stable state pairing, where the actions of multiple buttons could drive pairing. Based on their findings, they predict "small" buttons of insulator size (2-10kb). Viets and colleagues conducted functional transgene studies that identify the sufficiency of regions to drive pairing. Their studies predict "large" buttons of ~90 kb.

The assumption of this 10kb button size in this paper imply that the drivers of pairing are a number of small elements whose percentage determines affinity. However, this assumption does not take into account the counter model that buttons are larger ~90 kb elements. Considering that the Viets study is done by testing the pairing capacity of elements, the authors should consider this "large button" hypothesis in their model.

Along these lines, the authors conclude that pairing readily occurs at roughly 70% density (Figure 2D middle), suggesting 70 kb buttons that resemble the "large" 90 kb buttons. The authors should reconcile these data and test both models.

5. The spatial correlations between distant buttons should be discusses in more depth. The extent to which local versus distant effects of buttoning events are included in the model should be clarified the potential implications of distant effects should be discussed. Related to this, the zipping process, where a paired locus facilitates the pairing at neighboring loci, is a prediction unique to the button model. This cannot be tested directly by the current experimental design. Its test requires observing the pairing dynamics of multiple neighboring loci along the same chromosome. While this goes beyond the scope of this paper, it is worth mentioning this limitation in the paper.

6. Figure 3 is confusing and would benefit from information from Figure 5-sup 1. In figure 3, C and D are not presented in a manner that is ideal for the reader:

i. Why does the unpaired control end at ~25 minutes?

ii. The color codes for the graphs are confusing. Unpaired control and paired control are from two different experimental conditions and should be in two different colors.

iii. The data from Figure 5-sup1 should be included in Figure 3. Specifically, more individual traces to represent the data (from A and B) and the average traces for each condition (as in C, but for all conditions).

7. Why is signal lost? At some points, signal is lost in their MS2 and PP7 experiments. The authors should clearly state why this occurs and what it means for their analysis. Is it because transcription is bursty and these are breaks in transcription or is it out of the plane? If it is out of the planes of imaging, how does this affect the analysis, especially as these could potentially lead to greater distances between dots.

8. A full experimental confirmation of the model could be attained by perturbing the proposed mechanism. For instance, it could be shown that if the interaction energy between the buttons is reduced below a threshold value, pairing doesn't occur anymore. That could be experimentally achieved by interfering with the molecular elements associated to the interaction between the buttons, for example, by targeted nested deletions of those genomic regions or by titrating out the related pairing factors. A discussion of such experiments in the paper would be welcome, as they appear quite feasible and would provide a clear proof of the proposed mechanism.

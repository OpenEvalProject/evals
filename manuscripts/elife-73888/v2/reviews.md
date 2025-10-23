# Peer review - Round 1

Editors:
- Jonathan P Staley, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73888.sa0](https://doi.org/10.7554/eLife.73888.sa0)

This manuscript will be of interest to biologists who study RNA structure-function relationships in a broad range of systems, splicing researchers, and RNA structure bioinformaticians. An integrative analysis of RNA structure probing, model-based RNA folding energetics, cryo-EM data, and protein binding sequence motifs serves as the basis for a comprehensive, accurate, and robust framework for predictive models of splicing dynamics in a well-studied system. The modeling is leveraged by in silico mutagenesis that reveals novel insights into the mechanisms and tradeoffs that underlie the impact of disease-associated mutations on alternative splicing.


---

# Peer review - Round 1

Editors:
- Jonathan P Staley, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73888.sa1](https://doi.org/10.7554/eLife.73888.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Quantitative prediction of variant effects on alternative splicing using endogenous pre-messenger RNA structure probing" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The figure of SSU structure could be improved with clear nucleotide information along with reactivities. The ROC shows that the sequence seems more important than DMS reactivities. It might be better to quantitatively measure how many single-stranded nucleotides have high DMS reactivities. The DMS reactivities for unpaired As and Cs are much higher than those for paired As and Cs. Is it due to protein protection? It seems unreasonable to compare the reactivity profiles between SSU and MARPT isoforms since the profile difference might be only due the different interacted proteins.

2. It is interesting that 66% of base pairs were contained within exon units. Would the percentage remain similar when performing RNA folding with sliding window? If so, this observation could be explained as co-transcriptional folding.

3. The intron is more structured than the exon. Rather than RNA structure, is it possible that it is due to the protein protection? Would it remain a similar pattern under deproteinized conditions?

4. The unfolding free energy is based on the first step of 5'SS recognition (9 nts) for U1 snRNA. It is also possible that the RNA structure only affects U5 snRNA binding? The authors could test unfolding 3nt and see whether it will be similar or no effect. Again, will the clusters remain similar if the folding windows change?

5. It is not necessary to unfold all the nucleotides at one time. At the different steps during the splicing, the RNA structure might be very dynamic and remodelled in the process.

6. For the training set, is there any reason for using 20 synonymous and intronic mutations? A detailed clarification is necessary. Why not non-synonymous mutations?

7. The prediction could be improved by taking into account RBPs. The different DMS reactivity profiles are likely due to RBP binding. See the comment above.

8. Figure 6E. The first mutation the model predicted as "No change" seems to change; the splicing ratio does change at the leftmost column, although to a lesser extent than in the other columns called as "changed".

9. I would encourage the authors to come up with an explanation/hypothesis of why some mutations are more impactful, with respect to disease, than others.

10. Throughout the text, the authors discuss RNA conformations as being "more" or "less" structured and then "structured" or "unstructured." It would be beneficial to describe what it means to be "structured" versus "non-structured" and if they are truly the extremes or another way of saying more of less structured. It is difficult to follow as the text flips between these four ways to describe the structure, and then incorporates the direct measurement of the energy of splice site unfolding.

11. It would be good to include "MAPT" in the title considering all data was collected for this gene. If the author wanted to present this framework as a general model for splicing prediction, analysis of a second exon-intron junction would be required.

12. Results, first subsection: MAPT's PSI variability was analyzed in the context of different individuals and different cell types/tissues. This is followed by a statement that this isoform ratio is consistent. It would be helpful to see some reference to similar stats for other genes commonly studied for alternative splicing to give readers an idea of a "baseline" or at least what one should expect to see for a "random" gene. As someone not too familiar with the splicing literature, the variation in Figure 1A doesn't seem that small but this is likely because I don't know what numbers to expect. I'm also not sure about the relevance of the claim regarding "the likely presence of different levels of RBPs …" since I don't think it's clear which RBPs are involved in MAPT splicing (are these well characterized?, if yes, their levels can be quantified) and perhaps their levels are also fairly consistent across samples.

13. Results, second subsection: based on a finding that "66% of base pairs spanned less than 50 nucleotides and were contained within the exon units", the authors suggest that "the mature exons function as their own structural unit". However, looking at Figure 1B, there seem to be some high-probability, adjacent base-pairing interactions (green arcs, likely a stable helix) between exons 9 and 11 in isoform 3R, and similarly, 2 stable helices between exons 9 and 10 in isoform 4R. I recommend revising this part.

14. Results, third subsection: similarly to my previous comment, I also noticed strong base-pairing interactions (2 helices) between exon 10 and intron 10 in Figure 2. It would be helpful if the authors clarified this point and why they think that base pairing was "contained within exons, independent of introns."

Also, same question as above regarding the statement "despite likely differences in RBP concentrations, …".

15. Results, third subsection: it would be good to explicitly quantify (in the main text) the reactivity difference observed between the pre-mRNA and the mature isoform junctions, similarly to how this was done in a previous subsection for SSU vs. the isoforms, as it gives an idea of the degree of these changes and how strongly they suggest/support a higher pre-mRNA structure. That said, the statistical significance of such changes should be assessed/quantified in the context of the baseline (i.e., within-condition) variabilities.

16. Figure 2B: representative structures are shown for 3 clusters, but to me, it seems like there is a fourth cluster in the middle-right part of the plot (north east of the cluster whose representative structure is depicted at the bottom right). Was this cluster also identified by k-means? If yes, what is the representative structure and how relevant is it to the findings of this study? If this is not a separate cluster, it would help to clarify that the structure shown at the bottom right also corresponds to these points, or is it the structure at the top right corner? The latter option makes more sense based on the density plot (Figure 4C) for 4R mutant, but currently, no dashed line points directly to this region/cluster.

17. Figure 2C: the gel insets are mentioned briefly in the caption but I found it difficult to understand what these mean and why they are there. A bit more detail would be helpful, or otherwise perhaps move them to Supp. material and add some detail there.

18. Results, fourth subsection: in the statement about WT "The exon-intron junction of the representative structure for this region …" – does "this region" refer to the cloud in the middle? If yes, it's unclear from the previous sentence, which says WT had "structures distributed across the entire space…"

19. Results, fourth subsection: the last sentence refers to "the two other representative structures …" and Figure 2—figure supplement 2B, where the clustering results are shown more clearly and more than 3 clusters/structures emerge. This is really confusing, and I suggest re-thinking how to present the clustering and representative structures results. I find the supp figure to be clearer than Figure 2, even though more than 3 clusters are depicted. At the least, I think it could be helpful to clarify that more than 3 clusters were found and which structures represent which points/region in the plot.

20. Results, fifth subsection: the text on the non-synonymous and compensatory mutations isn't very clear. Were these all within exon 10? By compensatory mutations, do you mean double-mutants that recover the PSI?

21. Results, fifth subsection: did the author try to predict the PSI by using combinations of unfolding free energies (from several stages)?

22. Figure 3B: from the insets, it looks like the bootstrap variation estimates vary markedly differently for exonic vs. intronic mutations. Any idea why?

23. Figure 4A: what does "Experimental Label" mean?

24. Materials and methods, calculating \deltaG^{++} of unfolding of a region of interest: I found it difficult to follow the description of this calculation, so more detail would be appreciated. I'm also not sure what "base pairs within a region of interest were removed" means – do you mean the structure in that region was converted into a single-stranded RNA? Also, my understanding is that the notation \deltaG^{++} is for this particular non-equilibrium energy, however, I don't understand why the two numbers from which it is calculated are also denoted by \deltaG^{++}.

25. I have the impression that sometimes the authors omitted crucial explanations. For example, it is important to explicitly stated that inclusion of exon 10 results in the 4R isoform and that exclusion results in 3R early in the text to avoid confusions.

26 In Figure 1A, I suggest that splicing be drawn by having lines go from the 5' splice site of exon 9 to the 3' splice site on exon 10, or to that on exon 11, to show the alternative splicing forms.

27. Figure supplement 2A-B: space missing in "Invivo".

28. The manuscript could benefit from improvements to its writing to clarify and/or better explain a few points/statements and possibly also adjust some statements to better align with the analysis findings. Different subsections of the main text sometimes feel disconnected from the rest. Including the rationale of the authors in performing each analysis together with clear conclusions would go a long way helping the readers understand the various sections. The authors explain that the consistency of the splicing ratio (1:1) across tissues suggests that primary sequences and structure regulate this event, but not RNA binding proteins. It is strange that later on the authors include SRE (and binding of RNA binding proteins) as key regulators in their framework.

29. Line 51-52, the references for pre-mRNA structure should be Sun et al., 2019 NSMB and Liu et al., 2021, Genome Biology.

30. Shannon Entropy could be added along with BPP.

31. The PCR efficiency is normally associated with the size of fragment. The size of 3R is much shorter than that of 4R. Is there any estimations on the effects while comparing the structures of 3R and 4R?

32. Will the structure and SRE in the intron upstream of exon10 also affect the PSI?

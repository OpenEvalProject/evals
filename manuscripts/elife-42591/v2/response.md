# Author response - Round 1

Authors:
- Fuad Mohammad
- Rachel Green ([ORCID: 0000-0001-9337-2003](https://orcid.org/0000-0001-9337-2003))
- Allen R Buskirk ([ORCID: 0000-0003-2720-6896](https://orcid.org/0000-0003-2720-6896))

## Response text

DOI: [10.7554/eLife.42591.038](https://doi.org/10.7554/eLife.42591.038)

[…] However, there are a few issues to be addressed.

Given that the central point of the paper is to show that the revised technique allows unbiased detection of elongation pauses, the authors are asked to examine one additional sequencing library prepared with frozen cells and MgCl2 but using RelE in place of MNase, and determine whether this improves the inverse correlation of codon pausing with CAI described in Figure 7, which is currently substantially less than reported by Weinberg et al. for yeast RPFs. It seems important to determine whether the weaker correlation reflects a real biological difference or a technical shortcoming that can be solved by using a more precise nuclease to trim the RPFs.

The authors are also asked to make the appropriate additions or changes in text to address the other comments raised by the reviewers, shown in the separate reviews below.

As pointed out by reviewer #1, we see a weaker inverse correlation between pausing and CAI than is observed in yeast. In the Discussion section (fourth paragraph) we explain our view that this is due to technical shortcomings, not real biological differences. In particular, we know that we are sampling ribosomes in different steps of the elongation cycle: some are arrested during peptidyl transfer (we can see pausing at Pro codons) and some during decoding (we also see pauses at rare codons). These subpopulations pause for different reasons, complicating the signal. In yeast, it is now possible to separate these subpopulations and sample only decoding ribosomes, but this is not yet possible in bacteria. We are working to address this issue but it is beyond the scope of this study; it took several years of optimization in yeast to solve this problem.

The reviewers asked us to use RelE (together with MNase) to generate ribosome footprints to see if this would improve the inverse correlation between pausing and CAI. The problem is that RelE cleaves mRNA at the A-site codon and has strong sequence selectivity. Since we assign ribosome positions from the 3’-end of fragments, this introduces bias at the exact position we want to study, the A-site codon. In contrast, because MNase cleaves at the 3’-boundary of the ribosome, roughly 12 nt away from the A site, the sequence selectivity of MNase creates little or no bias at the A-site codon after averaging instances of a given codon. In short, RelE is great for reading frame but bad for pausing analyses. We changed our discussion of RelE in the Results section to explain these limitations (subsection “On the sequence specificity of nucleases”, last paragraph).

As prompted by the reviewers, we prepared samples with our new methods (direct freezing, high Mg buffers), pelleted the ribosomes, resuspended them in the standard buffer (with low Mg levels), and generated footprints using MNase together with various concentrations of RelE. Even at high concentrations of RelE, 5 times what we previously reported, only a small fraction of reads (15%) were cleaved by RelE. This may be because our protocol traps ribosomes in a conformation that prevents RelE from binding in the A site. Preliminary experiments with high Mg buffers in yeast without any antibiotics yield 28 mer footprints characteristic of an occupied A site (perhaps in the hybrid/rotated state); this would be incompatible with RelE binding.

Reviewer #1:

[…] This work is significant because it should set the standard for the proper application of ribosome profiling of bacteria. However, there are a few issues to be addressed.

The authors note that even with 3' alignments of reads, the triplet periodicity of the aligned reads is not very good, and actually reflects the sequence bias of MNase cleavage of naked RNA. This leads to two comments.

– First, the way it's written one might infer that a plot of the kind shown in Figure 1A but constructed for total aligned RNA reads would look very similar to that presented here for aligned RPFs. Presumably this is not the case considering that there is no periodicity observed upstream of the AUG start codon. Perhaps they should include such a plot constructed from RNA reads to assure the reader of this point.

3 nt periodicity arises from both the sequence selectivity of MNase and the bias of the genetic code in open reading frames. There is no periodicity in untranslated regions because there is no systematic nucleotide bias with 3 nt periodicity in these regions of the genome. In the Hwang and Buskirk (2017) paper referenced here, we prepared RNA-seq libraries with MNase and observed 3 nt periodicity exclusively in ORFs. To clarify this issue in the text, we changed the wording of the second paragraph of the subsection “On the sequence specificity of nucleases”.

– Second, the authors state that "For studies where the reading frame is essential…generating RPFs… with RelE" should be done. I feel that the current study falls into this category and that the authors should examine one additional library prepared with frozen cells and MgCl2 but using RelE in place of MNase, and determine whether this improves the inverse correlation of codon pausing with CAI described in Figure 7, which is currently substantially less than observed by Weinberg et al. for yeast RPFs.

See the response regarding RelE above.

Reviewer #3:

[…] This manuscript will advance the study of bacterial translation. The data are very clear, and the manuscript links the specific technical concerns with biological misinterpretations. Many of the concerns raised here were recognized in the first bacterial ribosome profiling studies, but the solutions presented here are valuable and novel.

1) The manuscript mentions unpublished data in a few places. The yeast unpublished data is interesting but largely superfluous to the arguments presented here. The B. subtilis profiling data seems more central to the generality of results presented here – does this manuscript describe the best approach for E. coli ribosome profiling, or for bacterial ribosome profiling more generally?

The yeast data are now in press at Molecular Cell and a citation has been added to the text. We have not made libraries with our new methods in B. subtilis. Our unpublished B. subtilis data only show that using RNase I isn’t better than MNase – it doesn’t yield distinct footprint sizes like the 28 mers in yeast. We believe that harvesting cells by filtration and arresting ribosomes with chloramphenicol are generally problematic in bacteria.

2) The manuscript discusses serine deacylation induced stress at length. One aspect of filtration that is often overlooked is the potential for cold shock. Was filtration carried out at 37 ºC with a pre-warmed filtration apparatus? If so, this should be mentioned in the Materials and methods; if not, this should be discussed as a possible stressor.

This is a good question. We added a line to the seventh paragraph of the Discussion, stating that we see strong Ser and Gly pauses whether filtration is performed at room temperature or in a 37 °C room.

3) The potential for Cm-mediated distortions was recognized in the original Oh et al. (2011) manuscript. The authors here investigate "L9" and "L10" as Cm-pretreated libraries, but the same manuscript also reported SRR364370 and SRR364368 which were "harvested by rapid filtration".

We added a line to the last paragraph of the subsection “Chloramphenicol in the media induces artifacts at the gene level”, citing this paper and an associated protocol, both of which address this problem thoughtfully. We believe it is important to address these issues again because people continue to harvest cultures by adding Cm and pelleting cells by centrifugation.

4) Some of the analysis in the very recent manuscript Zhao et al. (2018) seems relevant to the discussion of footprint length and reading frame analysis.

A reference to this paper was added in the new section on nuclease and cloning bias (subsection “On the sequence specificity of nucleases”, first paragraph).

5) The pattern of pausing seen in the optimized bacterial ribosome profiling data resembles the pattern reported for mammalian ribosomes in Ingolia et al. (2011). This similarity seems remarkable.

We added a citation of this paper in this context to the fourth paragraph of the Discussion.

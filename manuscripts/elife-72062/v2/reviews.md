# Peer review - Round 1

Editors:
- Geeta J Narlikar, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72062.sa0](https://doi.org/10.7554/eLife.72062.sa0)

The authors provide compelling evidence that the repression of gene expression during quiescence of the model eukaryote yeast is achieved by heterogenous clustering of local groups of nucleosomes.


---

# Peer review - Round 1

Editors:
- Geeta J Narlikar, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72062.sa1](https://doi.org/10.7554/eLife.72062.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Local Chromatin Fiber Folding Represses Transcription and Loop Extrusion in Quiescent Cells" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Vijay Ramani (Reviewer #2).

As you will see from the reviews, the reviewers were generally enthusiastic about the work but also agreed that additional clarifications on data analysis and interpretation were required. The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this list of essential revisions to help you prepare a revised submission.

Essential revisions:

1) The authors use the words long- range and neighboring-interactions without clearly defining them. It appears that the term "long-range" applies to interactions between nucleosomes greater than N+1, but for most readers, this term would mean interactions kilobases apart. So, we ask the authors to clearly define the term "long-range". Once defined authors should discuss the changes (or lack of) in the long-range (kilobases) interactions.

2) The authors suggest that Q cells have more long-range interactions than log cells. However, in figure 1 supplement 2 B and D, there appear more distal interactions in log for Q at 1 KB resolution.

3) The authors should provide decay curves so the reader can understand better the range of interactions that are enriched or depleted.

4) The authors shift from G1 to log phase between figures. The authors need to justify these switches.

5) The tomograph image looks compelling in figure 2A but quantitation in figure 2C seems to make the difference non-existent. It is hard to believe the differences between the orange and blue bars are statistically significant. Unless the authors provide more compelling evidence for the statistical differences between Q and log cells by this analysis, the tomograph figure should be removed.

6) The conclusions from modeling are only relevant if the results are robust to small changes in the parameters. If small changes in values of the authors' parameters cause the differences between log and Q to disappear or reverse, the authors would have to justify their values for their parameters. Indeed, the robustness of the modeling to support the previous conclusions is not evident in Figure 2 supplement 1 E. The error bars are huge. Unless the authors provide more compelling evidence for the statistical differences in the model's predictions, the modeling figure should be removed. If the authors can address this concern, then the modeling paragraph will be greatly improved by a brief description of the rationale and the results of the simulation for readers that are not familiar with these mathematical models.

7) The use of non-parental nucleosomes is confusing. Non-parental usually means new nucleosomes incorporated during S phase. Are the authors are referring to cis (within a nucleosome) vs trans (between nucleosomes) interactions? Please clarify.

8) Figure 3 C should show log-phase cells for comparison to allow the reader to assess how intermediate is the change in nucleosome interactions induced by TSA.

9) The authors should provide an explanation or comment why 20% of acetylation defective cells can enter Q. Unaddressed it would imply that a significant fraction of cells can enter quiescence despite being transcriptional active. Is this an artifact reflecting their limited ability to purify Q cells?

10) Figure 4F should also have log to provide a baseline for loss of compaction in mutants

11) Line 1687: Use of the term epistatic seems incorrectly applied. It is not clear how activation masks compaction state. Do the authors mean activation is uncorrelated with the level of compaction? Please clarify.

12) Why are the stripes present in figure 6A (in the mutant R17R19A), not present in the same mutants in the previous micro-C maps at the same resolution (4d and Figure 5 figure supplement 1 d?

13) Discussion should be shortened. The paragraph on cation role in condensation has seems to not be directly related with the results presented in the paper. The connection should be made clear or the paragraph should be deleted.

14) The authors consistently refer back to the notion of 10 nm and 30 nm fibers throughout the text (e.g. the paragraph beginning on p.69; line 1583), and the intent of this seems to be to liken the compacted states observed here to the "elusive" 30 nm fiber (e.g. by noting that H4K16ac disrupts the 30 nm fiber in vitro). This represents a fundamental weakness of the paper, because while the evidence provided certainly demonstrate that a novel compacted state exists in quiescent cells, the data are also fairly convincing that this is not a 30 nm fiber (as evidenced by STEM tomogram comparisons), especially given the bulk-averaged nature of the majority of the datasets presented here. Figure 1A illustrates precisely how the Hi-C data as presented can provide a false impression: contact curves demonstrating a typical contact probability decay are positioned under an individual fiber; these Micro-C data, however, are derived from many dinucleosome ligations averaged over many fibers from a large number of haploid cells, and thus cannot really be used to make statements about the structures of individual chromatin fibers. This issue does not dramatically alter the conclusions of the study, but does require a text revision of the 30 nm comparisons used throughout the paper (and, preferably, a sentence addressing the population averaged nature of Hi-C data).

15) Generally, the paper could be improved by more rigorous quantitative analysis of the Hi-C data, as most of the data is presented qualitatively in the current manuscript. Hi-CRep is useful for measuring reproducibility of replicates, but unfortunately remains the only significant quantitative comparison made across the many information-rich Micro-C XL datasets analyzed for this paper. This would be especially important for the contact decay curves presented – as of now it is very difficult for the reader to gauge how large a quantitative effect the various perturbations presented here have across their various samples. Moreover, it seems likely that the genome-wide averages presented here end up averaging over regions where there are larger or smaller reproducible changes in contact decay. We suggest that the authors formalize a way to quantify the relative change in contact probabilities (perhaps, through a log-odds ratio), but also consider performing these analyses across loci of interest. This extends to analyses presented in e.g. Figure 6 – can the authors use aggregate peak analysis of similar to provide some quantification of the heatmaps presented in Figure 6C?

16) The DSG results are somewhat odd and run counter to what one would expect from work by the Dekker, Rando, and Tjian-Darzacq labs in both yeast and mammalian cells. Is it possible that these findings underly a technical challenge in working with quiescent cells? One could imagine that e.g. differential accessibility to the DSG crosslinker could explain how the addition of DSG has minor effects on genome-wide contact probability estimates. Aside from testing MNase digestion efficiency by targeting ~95% mononucleosomes, the authors should mention if they considered any other ways to ensure that the contact probability decay curves being observed are not partially biased by differential crosslinking (or differential in situ ligation efficiency) in quiescent cells.

17) It would be great for the authors to make their analysis code / notebooks available via GitHub. This includes both the genomic data analysis code, the mesoscale modeling code, and any scripts used for analyzing the STEM tomograms.

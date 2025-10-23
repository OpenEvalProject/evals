# Peer review - Round 1

Editors:
- Stephen Parker, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.46314.017](https://doi.org/10.7554/eLife.46314.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A streamlined protocol and analysis pipeline for CUT&RUN chromatin profiling" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The main objective of the manuscript is to introduce an improved protocol for CUT&RUN and a peak calling algorithm. The authors made optimized the pA-MNase enzyme (now pAG-MNase), for easier purification and recognition of both mouse and rabbit primary antibodies. Furthermore, the authors suggest an improved high Ca2+/low salt CUT&RUN protocol that prevents overdigestion/nonspecific digestion. The authors also find that E. coli DNA carried over in the pAG-MNase purification is still present in CUT&RUN sequencing samples and can therefore be used to normalize CUT&RUN data. Lastly, a new peak calling algorithm is proposed for calling peaks in CUT&RUN data as it typically has low read number and high signal to noise ratio. Although this manuscript does not contain any biological findings or major changes to the current CUT&RUN protocol, it does communicate important improvements to a technique that many labs are interested in using.

Essential revisions:

1) All reviewers uniformly shared major concerns about the peak calling algorithm, and we summarize these here:

a) There are several different modes and the description how they differ and when each is appropriate wasn't clear.

b) The sudden drop-off of SEACR with more data (going from 25M to 30M reads, Figure 5D) reveals a very concerning flaw in the model or a bug in the implementation. Performance should improve with more data in a downsampling experiment. The overall drop-off and poor performance present significant questions to its claim of robustness and general usability.

c) Could MACS2 and HOMER algorithms perform comparably to SEACR simply by tuning their parameters (wasn't clear how much of an effort was made to do this, and we think that is important for algorithm benchmarking)? More comparisons to other factors would be helpful.

d) SEACR does not provide any estimate of statistical significance to the assigned peaks compared to other methods. How are users to interpret confidence in peak calls?

e) Why were the target blocks defined by contiguous regions of nonzero coverage rather than tiling windows?

f) Figure 5 – label axes of (A)-(C) more clearly. These appear to be TPR vs. FPR using the encode logFDR<-10 peaks as a truth set; is that right? But should each peak caller at a given sampling depth have a summary value (auROC or auPR) rather than a point?

g) Figure 6B – SEACR is more aggressive in aggregating long peaks but this seems sort of trivial (i.e. one could do something similar by padding and merging peaks)

Overall, we felt that the other aspects of the manuscript were strong enough to warrant a path forward in the Research Advances format even if all the above items about the peak caller are not addressable.

2) A high Calcium/Low salt procedure is included that reduces diffusion of the released complex. The data to support this lower diffusion is that signal to noise appears higher. However, direct evidence for lower diffusion within the nucleus is not provided. Background seems to be lower in specific example loci (e.g. shown in Figure 1B) – this should be quantified genome-wide (e.g.,% signal in peaks). The improvement appears to be more profound in some examples (H3K27ac, Figure 2—figure supplement 1A) than others (H34Kme2, Figure 2—figure supplement 1A). Also, are inter-sample correlations the best way to show signal:noise improvement? It would be more convincing with precision and recall (or similar) vs. high-confidence peaks.

3) The authors claim that DNA carry over from E. coli in the pAG-MN preparation is a good substitute for the yeast genomic DNA spike in that is normally used. My concern about this is that this is not a well-controlled spike in, as the amount of E. coli DNA may well vary between batches of the purified PAG-MNase.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Improved CUT&RUN chromatin profiling and analysis tool" for further consideration at eLife. Your revised article has been favorably evaluated by Detlef Weigel (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

All three reviewers have examined the revised manuscript and feel that all points were addressed with the exception of the issues raised in items 1a-g regarding the peak caller. Importantly, all reviewers remain uniformly concerned about this aspect of the work and do not believe the revisions adequately addressed the points that were outlined. All reviewers believe that other aspects of this manuscript warrant publication and advocate for moving forward without the peak caller, which would expedite publication.

However, if the authors would like to make additional revisions to the peak caller sections, we will re-review those and recommend directly addressing the items we initially raised:

1b) The response to this point was to add an ad hoc "genome coverage" filter to effectively throw out reads and decrease noise. This is not a reasonable solution for a robust peak caller and only emphasizes the sensitivity of the method to read depth and noise.

1c) Insufficient parameter exploration was provided to convincingly demonstrate that the other peak callers are inferior to SEACR. For example, in addition to changing MACS2 FDR, why have the authors not attempted to change the local λ smoothing parameter, which would make MACS2 use a genome-wide Poisson threshold that is more equivalent to the single genome-wide threshold that SEACR uses? More informed parameter exploration beyond the single example provided here would make a stronger case.

1d) The authors state that statistical model based FDRs are inferior to their empirical threshold, but the performance results only support such a statement under a limited and author-selected (yellow highlights in plots) range of read depths. Further, performance on additional antibodies (TFs, histone mods, etc.) should be presented before such a strong claim is made.

1e) If "contiguous signal blocks reflect real patterns of protein protection that should be incorporated into the peak calls." then why do the authors need to implement a "genome coverage" filter at high read depths? This statement is contradictory to the performance results and methods in the manuscript.

1f) See point 1c above.

Overall, the SEACR algorithm seems very sensitive to background noise levels, which may be highly variable across diverse labs that will implement the revised CUT&RUN technique. This could be a recipe for confusion and misinterpretation across the user base. For the collective reasons outlined above, we remain skeptical about including the peak caller in this manuscript. However, we would welcome immediate forward movement if this section is removed.

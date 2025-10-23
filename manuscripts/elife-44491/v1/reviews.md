# Peer review - Round 1

Editors:
- Jeremy Nathans, Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44491.021](https://doi.org/10.7554/eLife.44491.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your manuscript "High fidelity lineage tracing in mouse pre-implantation embryos using primed conversion of photoconvertible proteins" for consideration by eLife. Your article has been reviewed by three experts and the evaluation has been overseen by a Senior and Reviewing Editor. While the reviewers found the work interesting, the number of substantive questions raised was such that we feel we must reject it. We hope that the reviewer's comments below will be useful to you in revising the manuscript for submission elsewhere. We apologize for not being able to deliver better news, and we hope that you will continue to consider eLife for future submissions.

Reviewer #1:

In their manuscript, Pantazis and colleagues demonstrate a combined optical/computational method for reducing the effects of translational and rotational drift in pre-implantation mouse embryo lineage recordings. Primed conversion is used to introduce a sparse second color (red fluorescent nuclei), which is used as a fiducial to reduce drift and an additional quality check on the derived lineages. Although the authors convincingly demonstrate that their method does reduce the effects of drift and thus computational error in their experiments, I am unconvinced that their method is either necessary or generally important for this particular biological application.

While the problem the authors address is a real one, their method does not appear a significant improvement over previous work – in particular the groundbreaking method of Lars Hufnagel and Jan Ellenberg (Strnad et al., 2016). In that manuscript, Hufnagel and Ellenberg performed similar recordings at higher spatiotemporal resolution than reported here. In particular, the temporal sampling in Hufangel and Ellenberg was performed every 5 minutes, 1.5-3x faster than the 7.5 minute and 15 minute recordings performed by Pantazis. One has to wonder if the increased temporal sampling is in fact the dominant source of error in reconstructing lineages – if Pantazis et al. had simply recorded faster, would they have encountered the same degree of drift/error? Hufnagel and Ellenberg claimed a 100% tracking accuracy in their manuscript (for the embryos they ultimately select for lineage analysis) – if this is really the case, I have to wonder why Pantazis et al. did not simply adopt the previous tracking approach. Pantazis et al. compare their computational pipeline to Bitplane Imaris, but the real state-of-the-art comparison is to Hufnagel and Ellenberg. How does the new tracking pipeline presented by Pantazis compare to the coherent point drift method described in this previous work? It is also never explicitly spelled out how many datasets the new method 'rescues', i.e. of the 5/11 embryos that exhibited severe translation/rotational drift, how many were 'recoverable' in the new method? What is the fraction of embryos that are now fully trackable? Because the authors of the current manuscript have failed to put their method into context against previous work, it is difficult to properly assess the impact of their method.

The authors also assert that their method might allow less dosing of the sample (presumably due to the worsened temporal sampling they report) and that their pipeline results in smaller datasets due to the tighter cropping that results. Neither assertion is particularly compelling – (i) I am not convinced that in fact lowering the temporal resolution is advantageous as it seems this makes the tracking problem harder; (ii) the original data sizes they report of ~5GB are hardly massive by today's standards. In summary, I am concerned that the authors' paper constitutes a kind of 'straw man', i.e. they are attacking a problem that has been satisfactorily addressed by previous work. A thorough, statistical comparison of their method to Hufnagel and Ellenberg's would go a long way to convincing me of the value of their method.

Other comments:

The authors are to be commended for comparing H2B-pr-mEosFP to H2B-pr-mEos2. However, I would like to see more evidence for their assertion that their photoconverted embryos develop normally, especially since the primed conversion operation itself intrinsically introduces additional dose. In the previous work by Hufnagel and Ellenberg, 'the tracked embryos had a division timing and number of ICM cells comparable to those of in vitro-cultured embryos… and healthy pups were born after transfer of the imaged embryos into pseudopregnant females…'. Were similar controls done here? What is the additional dose introduced by the primed conversion on the confocal microscope, relative to the light sheet illumination dose used for imaging? The authors image from 4 cell to blastocyst, yet it seems that in previous work it is possible to image from zygote onwards. Is the 4 cell stage necessary due to the increased light sensitivity at earlier stages?

Reviewer #2:

Welling et al. present a combined reverse genetic/optical and computational approach to extract developmental lineages from pre-implantation mouse embryos. The genetic trick relies on photo-convertible proteins that are converted on a confocal set-up and later imaged using light sheet. The computational pipeline extending Imaris achieves proper segmentation, image alignment and uses the total and photo-converted nuclei to improve unsupervised lineaging.

This work has potential, however, for me, it falls short of being a minimal publishable unit. The photoconversion approach has already been published by the authors. What remains is a useful technique that would however fit better into Materials and methods section of a paper focusing on the biology that can be done with this approach. I see the benefits of being able to use the rotating embryos previously excluded from similar analysis (Strnad et al.). However, that is a very niche problem and the pipeline lacks general applicability. The segmentation enhancement is completely dependent on the precise experiment described here, no new algorithm has been presented. Similarly, the re-orientation of the rotating embryos is done using very basic core functions of Imaris. The authors do show that it benefits the analysis of their specific data, however I doubt it will be generally applicable. The comparison of the performance of the Imaris tracker applied to uncorrected and corrected data is a straw man comparison. The Imaris tracker was not developed for tracking lineages in embryos that are fast rotating and therefore it, of course, fails spectacularly.

In order to make the paper work as a methods paper, it would have to be significantly expanded. On the hardware side, the photoconversion would need to happen at one microscope (something the authors clearly intend to do). On the software side, the tracker would need to be benchmarked against existing state of the art tracking solutions such as Ilastik, TrackMate and the Keller pipeline. In addition, the authors would need to show that it is also applicable to other lineaging problems.

Last but not least, the submission contains no code. There is insufficient details provided to reproduce the work, even inside such user friendly software as Imaris is. There is a mention of some MATLAB code that is stringing together the Imaris functionality. At least that needs to be put on github to make this work useful for others. In the current form, it has no impact.

Reviewer #3:

In the short paper entitled "High fidelity lineage tracing in mouse pre-implantation embryos using primed conversion of photoconvertible proteins" the authors use photoconversion of an EosFP by 'primed conversion' to follow by 3D SPIM imaging the cell lineage. In this very limited example the authors propose a potentially promising way of tracking cell fate. However I believe that it currently has a number of issues that should be addressed.

1) Novelty. The novelty here is only mediocre. The photoconversion of EosFP by a 488→730nm illumination pulse has been reported (Mohr, Argast and Pantazis, 2016). Similarly, lineage tracking has been done before (Kurotaki et al., 2007 and others). The novelty is using SPIM here for longer-term tracking, but unfortunately while the potential was there the illumination for both channels was done with the same objective (see point #2).

2) Implementation. The real power of this method should be to focally limit which cells, or region thereof, is getting photoconverted, by launching the light through objectives situated at 90 degrees. Unfortunately, the authors choose to illuminate/activate the cell through only a single objective and thus lose a potential major benefit of the technique. It would have been really neat, and more powerful, to do the activation at a later stage when it would be otherwise difficult to activate only a single cell. In my opinion, doing the activation by cross-beams and in a condition that would be impossible to achieve by a single beam is essential here, and would improve the novelty. The authors ironically discuss axial confinement of the dual activation yet fail to do so and exploit it in the experiments. This must be done.

3) Robustness of the data. It is unclear how many times this experiment was performed. Only once? To show that the technique is robust, more experiments are needed, with statistics. The authors mention that the photoconverted embryos were healthy, but from how many experiments?

4) Other reporters. The authors should show the technique for other reporters, such as in the cell cytosol, or membrane, to generalize the concept.

5) Ambiguity of assignment. It is unclear how long a single lineage can be tracked. The S/N seemed to be high at the later stages. Can the authors better quantify showing the accuracy of assignment in each stage, with statistics.

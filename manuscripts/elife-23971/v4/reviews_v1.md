# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23971.027](https://doi.org/10.7554/eLife.23971.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Nonlinear feedback drives homeostatic plasticity in H2O2 stress response" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior Editor and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this study, the authors addressed quantitatively the adaptation of S. cerevisiae cells to oxidative stress. They used single cell readouts together with microfluidics and mathematical modeling to propose how cells acquire tolerance to H2O2. They found that the induction of peroxiredoxins by the Yap1 transcription factor (AP1) is a key phenomenon during adaptation in this particular yeast.

Both reviewers appreciated the high resolution of your microluidics experiments and the combination of mathematical modeling with quantitative experiments. However, the major concern, raised by reviewer #2 and agreed by the other reviewer, is that novelty is limited as the majority of biological findings are already known. This is a major concern which you need to address.

Despite this concern, the reviewers were positive about publication, as they greatly appreciated the depth of your measurements and analysis. A major concern here, though is the lack of cell-survival information, which the reviewers believe is the correct phenotype to be monitored when considering adaptation. As an essential revision, we therefore require that you will measure cell survival in your essays relevant for Figures 1–4.

Reviewer #1:

The authors study the dynamics of the response of S. cerevisiae to changing H2O2 levels. They use of microfluidics device that allow a precise temporal control of the media. A simple toy model that includes a negative feedback, of the stress response system is presented. The response of the growth rate, Yap1-GFP and TRX1pr-sfGFPdeg to a step response of H2O2 reveal a growth rate adaptation up to a critical H2O2 value together with an overshoot in Yap1-GFP that are consistent with a simple model termed 'linear'. These dynamics depend on the initial H2O2 the cells experience ('pre-treatment') and require the addition of Michaelian terms of the internal H2O2 levels (H) to the model (to the H2O2 scavenging term and the antioxidant production term). Mutant analysis shows that peroxiredoxin genes that were previously identified to be involved in the H2O2 stress response effect the adaptation to stress ramp. It is also shown that H2O2 levels have a non-monotonic effect on replicative life span that is Yap1 and Tsa1 dependent.

One of the main novelties of this study is the use of microfluidics that allows a temporal control of H2O2. It seems that the design of the chip relies on diffusion to carry nutrients from the feeding channel to the cells. This diffusion, in particular when cells are crowded in the channel where they grow has an effect on the effective H2O2 cells are experiencing and introduce a time delay that depends on the density of cells. The authors should provide arguments that these are negligible (either by adding a die and characterizing the flow or by simulation).

The authors divide the cells into 2 'types' of cells. The correlation between the type of cells and their location on the channel should be presented to rule out the cells in the middle of the channel are buffered.

One of the toy model assumptions is that the dilution time is constant. The authors mention in the Supplementary Information that although they realize that the growth rate is far from constant (which is actually one of the main results), it will not change the results. Taking into account the time dependence of the dilution time is critical to the understating of the underlying principles as advocated by the authors. The growth pause allows a significant time for protein to accumulate. The regulator overshot can rise from it. Without showing that the negative feedback that arise from the growth rate modulation is not significant (even by simulations and not analytical solution), the generality of the conclusion is questionable.

General

This study is elegant and the use of dynamical measurements and modeling is synergistic. Using negative feedback (and comparing it to integral feedback) and its features has been heavily studied (see for example, Khammash M. BMC Biology 2016). Feedback terms without saturation seldom describe the data well in biological systems. The reader would benefit from the use of the linear model as a pedagogical example to highlight the fact that overshoot ("training") can happen without dependence on initial conditions and hysteresis ("stress tolerance) also if it appears in the Supplementary Information. The paper would benefit from comparing the Michaelian model to a model where the growth rate is not constant in time. This will provide a vivid example for the interplay between growth rate and transnational feedback.

Reviewer #2:

Overall, the experiments presented here are quite well executed and the combination between experimental studies and mathematical modeling has been useful to validate some of their initial hypothesis. However, there are aspects of the study that limit its wide interest.

The information obtained from the study is mostly not novel, in contrast of what the authors claim. It has been known for oxidative stress and other stresses, in yeast and in other organisms, that 1) different kinetics of stress exposure leads to different adaptation patterns (training), specially on those systems in which transcription is involved and 2) that the pre-exposure to stress leads to acquisition of tolerance. It is also known that the Yap1 transcription factor is a major regulator of oxidative stress defense genes and that Yap1 regulates peroxiredoxin expression (major H2O2 scavengers). Thus, albeit nicely presented and quantitatively assessed, the new knowledge generated in the study is rather limited.

The experimental set up used to study adaptation is interesting and well executed. They mostly monitor Yap1 localization as a measure of oxidative stress signaling and growth rate to assess adaptation. These measurements are correct and they provide relevant information however, they fall short to conclude on cellular adaptation. Cell survival should be monitored (at least for Figures 1–4) to be able to claim on adaptation, measuring growth rate to visualize a transient cell cycle arrest is clearly not sufficient. Actually, cells delay cell cycle in response to stress and this delay is essential to maximize cell survival. The delay per se is an adaptive response and thus it cannot be concluded that cells that delay cell cycle are those that do not adapt properly.

Ramping experiments are interesting (Figure 3) to test the initial hypothesis. However, if I understood them properly, they do not reach the same H2O2 concentration. Authors should perform the same experiments increasing H2O2 at different rates but reaching the same final concentration (with different times) and then compare adaptation. Otherwise they are comparing not only different rate of exposure but also different final concentration of H2O2.

Negative feedback is proposed to explain some of the results. The authors do not study the contribution of such feedback in the training or acquired tolerance. This could be an interesting aspect to be analyzed.

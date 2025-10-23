# Peer review - Round 1

Editors:
- Jodi Nunnari, University of California, Davis , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07464.017](https://doi.org/10.7554/eLife.07464.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for resubmitting your work entitled “Stochastic modelling, Bayesian inference, and new in vivo measurements elucidate the debated mtDNA bottleneck mechanism” for further consideration at eLife. Your revised article has been favorably evaluated by Aviv Regev (Senior editor) and a member of the Board of Reviewing Editors along with two reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance as detailed in the reviewers' comments below.

In particular, as pointed out in the previous version, claims of novelty in several areas are overstated and require the appropriate revision for accuracy. The reviewers' concerns about data variance in the experimental data also need to be addressed (especially in the 25 day old data) as well as the concern that there is a very large effect with only small alterations in mtDNA degradation.

Reviewer #1:

This is a resubmission of a pure modeling paper, with the addition of new experimental data which is presented as supporting the main conclusions of the modeling. The authors have carried out a very thorough theoretical and analytical analysis of the proposed mtDNA genetic bottleneck, and conclude that the existing stance taken by Cree and Wai model (b) is a sensible interpretation of the experimental data. As such, the current paper is reassuringly confirmatory. However, I still have concerns, in part relating to the way the paper is written, and in part relating to the new data, which raises additional questions.

Introduction. A statement is made: ‘No study yet exists combining an analytic ‘bottom-up’ physical description of the bottleneck with mtDNAs as individual, discrete elements subject to a possible variety of replication and partitioning dynamics throughout an explicitly modelled series of cell divisions’. This is not correct, and I made this point in my earlier review of the paper. Their reference (Cree et al., 2008) includes such a ‘bottom up’ model. Although the compartments did not vary in that model, assumptions were made about the partitioning which are in accordance with the conclusions of this current paper.

Likewise, the statement ‘theory describing the behaviour of mtDNA populations throughout development, as opposed to estimating an overall effect of the bottleneck, is also absent’ is also an over-statement designed to justify the current work. There are several such theories that the authors refer to in their Introduction.

For the new experimental data, they use a line previously reported in their Cell Reports publication. A key message of this publication was that different mtDNA haplotypes behave differently, that selection occurs, and that this is influenced by the nuclear genetic background. All of these effects will influence the heteroplasmy variance. Although the authors touch on selection, they do not explore this thoroughly in the context of their previous work. How will this impact on their interpretation of their bottleneck models?

For the new experimental data, the heteroplasmy measurements are reported to a remarkable degree of accuracy. Do the authors really think that they can reliably report down to 0.01% as indicated in the supplementary data?

Previous theoretical work has shown that ∼50 heteroplasmy measurements are required to reliably compute heteroplasmy variance. Several of the published datasets do not achieve this, and thus the reported variance measurements are likely to be inaccurate. The same may also apply to the new experimental dataset.

Figure 4C raises concerns. For the ∼25 day old data, 6 data points (from a total of 15) are way outside the confidence intervals predicted by the various models. This implies that the new data set is not supporting the current or previous models.

Finally, given the likely readership, it is important to keep reminding readers what is prediction, and what is actual measurement. The section on turnover illustrates this nicely. No turnover measurements have been made; indeed, they would be incredibly difficult to do.

Reviewer #2:

The authors have revised their previous submission to now include new experimental data on the mtDNA bottleneck, as requested in an earlier round of review.

There is clearly a great deal of variation in the new data for the normalized variance, but the new data does fit best with the authors' favoured birth-death-partition model. The inclusion of this extra data, at the time points which are most discriminatory with regard to the various models, is therefore helpful, though not absolutely definitive. In particular, it looks as if the spread of the normalised variance itself has interesting dynamics, starting out low, increasing to a maximum at around 25 dpc before diminishing again. Is there any way in which the BDP model can capture these dynamics? Also it was not clear to me why the BDP curve in Figure 4A differs from the HB theory mean plot in Figure 4C.

Finally, I remain concerned that a 2% alteration in mtDNA degradation can have such a large effect, see Figure 5B. The authors must address this issue.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The previous decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled “Stochastic modelling and Bayesian inference elucidate the debated mechanism of the mtDNA bottleneck” for consideration at eLife. Your full submission has been evaluated by Aviv Regev (Senior editor), a Reviewing editor and three peer reviewers, and the decision was reached after discussions between the reviewers. We regret to inform you that your work will not be considered further for publication.

Although there was enthusiasm for the quantitative approach to the mitochondrial DNA bottleneck, the reviewers felt that experiments directed at testing the predictions of the modeling are required for the manuscript to significantly advance the field. Therefore, at this stage, we are returning the manuscript to you with an encouragement to submit with experimental data. We hope the reviewers' comments are helpful.

Reviewer #1:

The manuscript from Johnston et al. is an extremely thorough and well-thought out attempt to inject rigorous, quantitative thinking into the mechanism of the mtDNA bottleneck. It would appear that prior attempts in this direction have been limited in scope and inconclusive. The strength of the authors' approach is that it is able to unify previous treatments of the phenomenon into a single theoretical framework. From this position, it is possible to assess the plausibility of the various mechanisms within a Bayesian statistical analysis. Using prior data, the authors conclude that a birth-death-partition model is most probable. This model is analytically tractable which is also advantageous. These are powerful conclusions, and it would seem absolutely certain that progress in this field is going to require an analysis of this sort, due to the inherent complexity (and stochasticity) of the problem.

I do however have some concerns. Principally, the analysis is based entirely on previously published data, which is not all internally consistent. In particular, looking at Figure 2A for the variances, there doesn't seem to be very good agreement between the different datasets (especially comparing the Jenuth data with the rest). I appreciate that the authors' statistical analysis takes into account the experimental uncertainty, but the divergence between the different experimental data sets found in the different studies suggests that the effective experimental error bars may be much bigger than estimated. The ability to distinguish between the models via Bayesian model comparison may then be diminished. This point is important, as there is relatively little difference between the models with respect to the mean values (whose experimental values are also well clustered between the various data sets). Hence it does seem that the variances are the key to distinguishing between the models. Also the statistical inference is based around a residual sum of squares difference. However, the way this was implemented (using logs of the copy number measurements, for example) seemed a bit arbitrary. Were other possibilities investigated to ensure consistency?

More generally, I am concerned that the modelling is used primarily as a tool to fit existing data and thereby determine which model is most likely on the basis of previously published data. It would be more powerful if the authors could actually test the novel predictions of their modelling in new experiments. This would elevate the study to a higher level. Their model most definitely is predictive (Table 2), it's just that they ought to consider teaming up with an experimental group and prove these predictions right!

One other issue concerns the sensitivity of the system to variations in the mtDNA degradation rate, where even a 2% change causes a huge difference in the mean and variance (Figure 4B), which is probably unlikely in vivo. This may hint at an underlying weakness of the model.

Reviewer #2:

This paper deals with a controversy in the mitochondrial inheritance field over the details of the inheritance bottleneck and the development of variability in mtDNA heteroplasmy levels across the cells of an organism. This new mathematical modeling approach is coming from a set of researchers, including one well-known mitochondrial DNA expert, who were not involved in the original set of competing papers (primarily references Cree et al. 2008, Wai et al. 2008, Wonnapinij et al. 2010, Samuels et al. 2010, Cao et al. 2007, Cao et al. 2009). These authors also use simulation and mathematical methods that are far more sophisticated than the methods used in previous papers (references Cree et al. 2008 and Chinnery et al., 1999).

The paper does a good job of summing up the results and conflicting claims of the earlier literature. Their presentation of the differences in the assumptions of the competing models seems accurate to me, and they have built simulation models that encompass the three general competing sets of assumptions. The experimental data from the previous literature is all presented in a combined manner, which is valuable in itself. Through the Beyesian methods of assessing goodness of fit of the combined set of experimental data to the three competing models, the authors present a clear conclusion concerning the model that has the best agreement with the experimental data. This is a valuable contribution to the literature, and again it is very useful that this assessment is coming from an independent set of researchers.

While the mathematical detail that comes along with these more sophisticated methods is hard to digest, even for a trained mathematician, I would argue that it is essential to have this level of detail in the publication record.

Reviewer #3:

The authors have used stochastic modelling and Bayesian inference on published data sets to explore different models of the mitochondrial DNA genetics bottleneck.

There are several statements in the manuscript that are inaccurate and misleading. The notion that organisms ameliorate somatic mutation burden through bottlenecking is a hypothesis (not fact, as written), and not all oocytes have heteroplasmy as stated. Also, the idea that no model has been presented from the ‘bottom up’, with mtDNA as discrete elements, is not correct. The authors cite examples where this was the case (i.e. where the segregating units in the model are proposed to be mtDNA molecules). I also do not accept that there are no methods to allow the comparison of different bottlenecks. One of the authors (Poulton) is a co-author on a Bayesian approach, and Samuels has published extensively on this (some of the papers cited in the current manuscript).

Some of the proposed mechanisms (which are modelled) have little or no experimental basis. For example, we do not know there is ‘turnover’ or mtDNA within germ cells, and certainly the rate is not known. We have no idea what the size of the nucleoid is in germ cells. There is no evidence that turnover is generally low during cell division to my knowledge, to name but a few. The problem is, by including all of these parameters, the potential outcomes of the modelling will increase.

Most importantly, their general conclusions are in keeping with the previous models developed by Samuels, which combine relaxed replication and random segregation contribute to the generation of heteroplasmy in the germ line (i.e. the Cree mechanism, as they describe it). In other words, their findings are confirmatory, not novel.

The theoretical manipulation of the bottleneck provides some interesting results, but these are somewhat obvious: if you reduce mtDNA content (by increasing degragadation; incidentally this is something not shown in the germ line), you will accelerate segregation and thus lead to the loss of mutations that reach high heteroplasmy levels. Likewise, it is not surprising that selective pressures influence heteroplasmy variance. Given that heteroplasmy levels are bound by 0% and 100%, any factors pushing the level in a particular direction will inevitably alter the range of values. It is also not surprising that the observed heteroplasmy variance is consistent with a range of bottleneck sizes, given the number of other parameters that can be varied in the described models.

# Peer review - Round 1

Editors:
- Frederik Graw, Heidelberg University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66014.sa1](https://doi.org/10.7554/eLife.66014.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This study is a great example of an elaborated combination of experimental and mathematical analyses to examine an intriguing, pleiotropic immunological signaling pathway. While a good number of individual aspects of this signaling pathway have been studied and reported before, the presented work puzzles together many pieces and succeeds to present a conclusive and comprehensive model of this particular cytokine system. The main conclusions are well supported by the presented data and the manuscript will be of interest and relevance for the study of many other cytokine signaling pathways, being of broad relevance for immunologists and cell biologists.

Decision letter after peer review:

Thank you for submitting your article "Competitive binding of STATs to receptor phospho-Tyr motifs accounts for altered cytokine responses in autoimmunity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Jos van der Meer as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Kevin Thurley (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

All reviewers appreciated the elaborated and thorough analyses presented in this paper. Given this exhaustive amount of work leading to this comprehensive analyses, all reviewers also noticed that the paper is very complex and extensive. To help the reader focus, they recommend to re-think if some material and text could not be shortened or shifted to the discussion or supplement.

The detailed comments below address some specific points that the reviewers noted. In particular this addresses the following main points:

1. Please reconsider the title of the manuscript, as focusing on autoimmunity does not seem to fully capture your work

2. Some aspects regarding the statistical analyses and the mathematical modeling (e.g. hypotheses considerations) need to be explained in more detail and clarified.

3. Please consider to show a full characterization of the RPE1-cells that were used (see comment Reviewer 3)

Reviewer #1 (Recommendations for authors):

– Combining the mathematical model with the experimental data, a Bayesian Model selection and parameter inference approach is used to select between two model hypothesis and, later on, perform parameter estimation. It is not totally clear to me how an upfront Bayesian model selection can be done without addressing the issue of parameter inference. Therefore, shouldn't the comparison of the two model hypotheses not also been applied to the Th1-cell dataset, and not only the RPE1?

– (Figure 2c): The measurement of IL-27 at 30 minutes for REP1 and Th1 does not seem to contain any statistical variation. This also seems to force the model to match this data point for any parameter combination. What is the reason that there is no variation within this data point? As this also seems to be a critical point for differences between the dynamics caused by the two cytokines, would model predictions change if e.g. random variation is added to this data point?

– It is indicated in the text that the parameter inference by approximate Bayesian computation revealed statistically significant differences between the binding rates of certain receptors/molecular (p.7 top). Could you comment on the statistical tests used to compare the posterior distributions of the respective parameters to make this claim? The posterior distributions nicely show a deviation of the parameter estimates from the uniform prior distributions. However, especially in case of multi-parametric and high-dimensional models as here, there can still be the problem of correlating individual parameter estimates inhibiting parameter identifiability. To which extent are individual parameter estimates correlated within the accepted parameter combinations? In addition, more details on the ABC-approach should be given algorithm/software used, required number of particles accepted, possible number of runs (i.e., updating prior distribution by found posterior).

Reviewer #3 (Recommendations for authors):I commend the authors for an exhaustive amount of work on this exciting signaling pathway. I would like to focus on a few points now that I have a slightly more critical view on.1. Most individual findings have been reported before (or at least there have been indications). Understandably, this makes defining a clear punch line difficult, but honestly, focussing on "autoimmune diseases" already in the title to me appears a bit farfetched. The SLE aspect is only touched upon in the manuscript, and it is neither very informative nor central to the story. It is good to have it in, just to illustrate natural conditions in which altered STAT levels shapes cytokine responses, but it clearly should not be the selling point.

2. An aspect that I furthermore miss in the introduction and discussion part is the fact, that basically all cytokine receptor systems appear to have a rather strong preference for certain STATs. It appears rather trivial that different receptors / receptor chains will have different affinities for the different STATs and this has been addressed in a few studies previously (e.g. STAT1, STAT3 in ref. 42), or STAT2 in IFNAR1 in PMID:8605876. The present manuscript arrived at the conclusion of differing affinities of STAT1 and STAT3 for GP130 and IL-27Ra by rather intricate modeling approaches and confirms this biochemically. This is OK, but I find it a bit disconcerting that this is sold as a fascinating new finding, while I would say it is the most expected explanation. I dint want to diminish this achievement, just strongly suggest toning this down a bit and, most importantly, add a few words on the known and suspected differential affinities of the various STATs to cytokine receptors in general.

3. In Figure 1d, GP130 was over expressed in RPE1 cells and the authors' conclusion was that GP130 levels do not contribute to sustained pSTAT1. In fact, Figure 1d does look as if pSTAT1 is sustained; particularly when you compared to the normalized plot of Th1 cells in Suppl Figure 1c, where the authors mark this difference even in red with δ signs. It would be very interesting to know if 10xGP130 cells stimulated with (Typ)IL-6 would now also show enhanced expression of IRF1 and a second wave of transcription?

4. I would recommend the authors to show a full characterization of the RPE1 cells they use (e.g. for model parameterization and most further experiments) analogously to Th1 cells in Figure 1b and c (i.e. in terms of IL-27 vs IL-6 signaling) in one comprehensive supplementary figure. Suppl. Figure 4 goes in that direction, but it would be good to have this in the beginning (before the modeling) and in an identical fashion to the Th1 experiment. Please further make sure to identify more clearly (in text and/or legends or even figure labels) which cells were used in which experiment (e.g. "RPE1-IL-27Ra" or "RPE1-IL-27-Ra/GP130").

5. In the modeling figure, Figure 2c, I assume the Y-axes labels were swapped? If not, this needs to be explained!

# Peer review - Round 1

Editors:
- Meredith C Schuman, University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55421.sa1](https://doi.org/10.7554/eLife.55421.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We find the study to be elegantly performed and well written. It tests an interesting and relatively new ecological hypothesis and investigates both function and mechanism, in both controlled and realistic environments. This is unusually comprehensive. The study system (rice, pests, biocontrol agents) is of broad general interest.

Decision letter after peer review:

Thank you for submitting your article "Caterpillar-induced rice volatiles provide enemy-free space for the offspring of the brown planthopper" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Meredith C Schuman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ian Baldwin as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

We find this study to be elegantly performed and well written. It tests an interesting and relatively new hypothesis regarding insect oviposition choices, biocontrol by parasitoids, and enemy-free space for herbivores in an economically important system. The authors include data from an important agricultural plant and a wild relative, and investigates both function and mechanism, in both controlled and realistic environments.

However, we have several concerns regarding missing information, and methods, which must be resolved before we can determine whether the study is appropriate for publication in eLife.

Therefore we invite the authors to submit a revised version of their manuscript which should fully address the following concerns.

Essential revisions:

1) The relative quantification of at least those volatiles used for bioassays needs to be done rigorously, e.g. using response factors, and the amounts of pure compounds tested in bioassays need to be compared to amounts calculated to be present in plant blends, at least based on response factors. All three reviewers agree that this is a critical point which must be resolved. Relative quantification in terms of percentage internal standard only does not support any conclusions about absolute amounts of volatiles (ng-ug emitted per plant per time) or their ratio, and thus cannot be used as a basis to select concentrations for bioassays or to interpret bioassay results.

In particular,

– The conclusions drawn by the authors depend on the relative and perhaps absolute concentration of each compound tested in their blend, and they do not have any data to indicate whether these amounts are realistic. The description of peak area as a percentage of internal standard peak area cannot provide this information without additionally calculating response factors of individual volatiles to the internal standard. (i.e., What is the ratio between [peak area internal standard/absolute amount internal standard in sample], and [peak area of volatile/absolute amount of volatile in sample], and over what range is this relationship linear; once this is established using standard curves of the volatiles of interest versus the internal standard, an equation can then be used to estimate absolute amount of volatile in sample based on the ratio of volatile peak area to internal standard peak area in each sample).

– To address this does not require absolute quantification of 50 analytes. It would be sufficient to calculate response factors for the 13 focal volatiles, for which pure standards are available. These response factors can be used to estimate amounts measured from plants and compare those to amounts tested in assays.

– It would be much easier to interpret the results of the 20 bioassays in Figure 4 if the same "low" and "high" doses had been used (not the case -- these differ by orders of magnitude), or else if these can be related to the abundance of different compounds in the measured blends, using response factors as suggested above.

2) All reviewers agree that the statistical analyses require more complete description. A statistical analysis section is missing from the methods, and tests used and replicate number n are not stated in all figure legends.

The reviewers also agree that, in several cases, the statistical analyses require revision (inappropriate tests are currently used).

Reviewer 3 provides detailed instructions. Reviewer 3 also recommends a good standard reference: Bolker et al., Trends in Ecology and Evolution, 2008.

– Figure 1: A Wilcoxon signed rank test to compare BPH settled on the two different plants is ok although more interesting approaches exist. However, Student's t-tests are not appropriate to compare number of eggs since (i) this test assumes that the dependent variable is continuous and (ii) it does not take into account the paired structure of the data. Rather use a likelihood ratio test (LR Test) or a Wald test applied on a Generalized Linear Mixed Model (GLMM, Poisson distribution error) where the tube is treated as a random factor.

– Figure 2: A chi² test is not appropriate to analyze results of olfactometer experiments (here and elsewhere). Rather use a LR Test or a Wald test applied on a GLMM (binomial distribution error) where the odor source is treated as a random factor since multiple parasitoid females were tested with the same odor source. In more detail: (subsection “Response of A. nilaparvatae wasps to insect-infested rice plants”): 'control plants' are compared to 'treated plants'. These are the two treatment groups. But for each group, 10 individual odor sources are used with 8-12 parasitoids tested for each odor source (= 80-120 parasitoids per experiment). The, data are structured by the treatment, but also by the individual odor source nested within the treatment. Both structure levels must be integrated in the analyses. Chi square tests compare the two treatment groups but do not account for the structuring by odor source. Not taking this into account results in pseudo-replication. The most proper way to deal with that is to include the individual odor source as a random factor in the analysis, i.e. using a mixed model. Since the outcome of the experiment is a binary response (i.e. choice for control or treated plants), a GLMM is appropriate. It should include the treatment group as a fixed factor, the odor source as a random factor, and a binomial distribution error. By the way, please clarify the protocol of the olfactometer experiment that lacks clarity (subsection “Response of A. nilaparvatae wasps to insect-infested rice plants).

– Figure 3: You should never conclude anything from the score plot of a PLS-DA alone, due to the fact that this analysis is prone to overfitting of the data. Any conclusion should be drawn from a dedicated significance test followed with pairwise comparisons (see e.g. Hervé, Nicolè and Lê Cao, J. Chem. Ecol. 2018). Additionally, avoid log(x+1) transformations as the constant value introduces a bias that depends on the value to which it is added (more bias for smaller values). Since zeroes occur in the data, prefer the fourth-root transformation that is not biased.

– Figures 4 and 5: Same reasoning as for Figure 2, but with filter papers rather than individual plants as odor sources.

- Figure 6: The statistical analysis is not described in the Materials and methods. It seems from the figure that Student's t-tests were used, but this is inappropriate (cf. Figure 1). Use a LR Test or Wald test applied on a GLM (Poisson distribution error) for the number of eggs, and a LR Test or Wald test applied on a GLMM (binomial distribution error) for the % of parasitized eggs (with the tube treated as a random factor).

– Figure 7: Same comment as for Figure 6, except that a GLMM should be used for both numbers of eggs and % of parasitized eggs (each time with the cage treated as a random factor).

– Figure 3—table supplement 1: Since you perform multiple testing, it is mandatory that p-values of ANOVAs are corrected (see e.g. Saccenti et al., Metabolomics 2014). I would recommend the False Discovery Rate correction.

– Figure 4—figure supplement 1: The statistical methods are not described.

In addition:

3) Please explain the addition of Shuangli Su to the author list and the re-ordering of the author list between the initial and full submission. This is fine but should be explained.

4) The field experiment was a caged choice assay using a laboratory population of parasitoids under realistic field conditions. The authors should at least comment, and if possible provide evidence or observations, regarding whether the phenomenon that SSB infestation reduces the attractiveness of rice plants to the parasitoid can be observed in the open field, given the strong learning capacity of parasitoids.

5) Reviewer 2 expressed the concern that it takes at least 5 days until the parasitized BPH eggs become red at the condition the authors set up and thus it is not clear if the parasitization rates can be reliably quantified after only 3 days. The authors should respond to this concern, if necessary with a comparison of parasitization rates calculated at 3 versus 5 days under comparable conditions.

If these five issues are addressed and the updated results can still support the authors' central claims, then we would recommend the study for publication in eLife. However, it is possible that addressing concerns 1 and 5 in particular will reveal that the authors' bioassays are inconclusive, and that must be determined before we can assess whether this study is suitable for publication in eLife.

We expect that the work required to address all five concerns can easily be completed within two months, especially if data or observations to address concern 5 are already on hand or can be cited.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Caterpillar-induced rice volatiles provide enemy-free space for the offspring of the brown planthopper" for consideration by eLife. Your article has been assessed by a Reviewing Editor and Ian Baldwin as the Senior Editor.

After reviewing your response to the previous round of review, the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The authors have fully addressed the points raised by the prior round of peer review, but their response omits some essential information which must be provided so that the submission can be accepted for publication.

Specifically, in response to the major reviewer concern regarding their calculations, the authors state that they repeated the calculations as requested, which substantially changed their data and required new behavioral assays, but did not change their conclusions. This is fine, and the results (new values, new bioassay results) are clearly presented. However the method used to perform these new calculations is not adequately described. The authors refer to an appropriate reference (Kalambet and Kozmin, 2019; note: please correct year for this citation) which describes several acceptable methods, and do not state which of these they used, nor include their calculations in supplementary material or source data. It also cannot be determined from the new dataset how the calculations were done. This information is important both for replicability, and for understanding of interested readers regarding associated uncertainties.

The authors are thus asked to complete to their methods section and to include the new calculations, including standard curves as appropriate, as supplementary material or in the source data.

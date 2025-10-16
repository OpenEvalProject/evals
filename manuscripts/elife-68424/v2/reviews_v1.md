# Peer review - Round 1

Editors:
- Mohan K Balasubramanian, University of Warwick United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68424.sa1](https://doi.org/10.7554/eLife.68424.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript will be of interest to researchers in the fields of cell size control and the cytoskeleton. A combination of modelling and experimental data show that actin cables, which extend in budding yeast cells from the bud tip and bud neck, display an average length similar to the length of the cell, likely due to progressive decrease in their extension rate up to cell length. The distinct scaling relationship with cell length rather than volume may be a new paradigm that drives new investigations in related phenomena in other organisms.

Decision letter after peer review:

Thank you for submitting your article "Scaling of subcellular structures with cell length through decelerated growth" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Arjun Raj (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The vast majority of points raised can be addressed by rewriting and reanalyzing data already generated. However, a single new experiment has been sought by one of the referees, which I agree will further sharpen the models you are trying to advance.

Essential Revisions:

1. I'm not as familiar with the details of the models, but it seems that a key assumption is that f(Lcable,Lcell) = f(Lcable/Lcell), which allows for the cells to scale length appropriately. Can the authors speculate on potential mechanisms underlying this length scaling? If there is a gradient, what could form it with such a property?

2. The effect of Smy1 KO on initial elongation rate is modest. I think it would be useful to quantify the effect size and put it in the main text. Also, does the degree of increase quantitatively match the increased cable length observed? If not, can the authors speculate on the source of the discrepancy?

3. To uncouple cell length and cell volume, the authors could use mutants with abnormal cell shape (for instance using more ellipsoid or more rounded cells). Many such mutants have been described over the years in S. cerevisiae, so this should be a technically straightforward approach to take. This would allow to probe whether actin cable length indeed correlates better with cell length than the cubic root of volume (or other shape measurements).

4. An indication of how cables were selected for tracking and their number amongst how many cells would help better explain the extension rate measurements and increase confidence in the data. Extending this comparison to other mutants with altered cell shape as suggested above would also strengthen the conclusions.

5. Measurement of cable length and steady state length. The study depends heavily on the ability to measure actin cable length. But how cable length was measured in 3D is not presented with sufficient detail. I think it is essential to show convincing 3D images of cable end identification for the majority of actin cables in a cell. I am suggesting this since cables that reach the cell back may "turn around" and/or form bundles or unbundle through interactions with other cables.

6. The extension rate of actin cables that grow from the bud neck to the cell back is shown in movies and quantified in the figures. However, it's not clear if these cables eventually *stop* elongating. For example, in Figure 4D the extension rate does not decay to zero at the longest times. That seems to me to be an essential point since I would expect that if one is able to measure the length of most actin cables in the cell, then one should be able to see most of these cables stop extending.

7. I found the contrast between the two models, "boundary-sensing" and "balance-point" was not so sharp: the difference is on whether the extension rate decays more or less abruptly with distance along the cell. I also don't see if either of these models as presented is excluded by the data. The authors convincingly show that the cable extension rate decays with cable length, as would be expected from a balance-point model. However, as mentioned in comment 1, it is not clear where the extension rate decays to zero in graphs such as Figure 1F, 3B, 4D. If cable elongation ends abruptly at the longest time in these graphs, then this would indicate a boundary-sensing mechanism (so overall a combination/intermediate model).

8. I feel that the mechanism by which the actin cable system reaches a steady state needs to be clarified. We see a few cables that start from the bud neck and grow to the whole cell. Is this typical or are these rare cases? If rare, are they still representative? Do cables disappear to allow for new cable growth? Such processes change cable length so they are linked to the central theme of cable length regulation.

9. There is a lack of discussion and experimentation of known regulators of actin assembly and disassembly. Perhaps it's ok to leave the precise mechanism providing the feedback of cable deceleration for future work, however I feel that at least some discussion should be provided. For example, cofilin might sever filaments in age-dependent manner and cofilin-decorated filaments might be prone to breaking when buckled. Myosin motors are also known to regulate the extension rate of cables.

10. The authors don't measure cables shorter than 2 microns in Figure 1G, yet such cables should exist from the movies of cable growth versus time. I wonder if their measurement was biased towards the longest cables. In Figure 1D (cdc28-13 induced) there may be several short cables in addition to the long one. Perhaps a plot of total actin cable intensity vs distance would help.

Reviewer #1:

In this manuscript, the authors evaluate models for length determination of actin cables in yeast. The problem they pose is that actin cables must scale with the length of a cell, but given that length is a one dimensional measure, it cannot use "limiting pool" or "limiting factor" mechanisms in order to achieve such scaling. They first show that actin cables do indeed scale with cell length over a variety of cell cycle stages and perturbations. They then propose two models: a boundary sensing model and a balance-point model, the latter of which they show to be more consistent with the data. In line with their model, the rate of cable extension scaled with distance scaled by total cell length.

I found this manuscript to be a really nice example of quantitative cell biology. I think the problem of scaling of various cell components is fundamental and of great interest, and this work has framed an interesting example of the 1D scaling required for a linear component (actin cables). The paper is well written, the data is very solid with strong image analysis, and the claims are well supported.

Reviewer #2:

This is an interesting manuscript examining how the length of actin cables is set in budding yeast cells. The authors show that the average length of actin cables from bud neck to the distal pole of the mother cell is very similar to the length of the cell. The cable length appears to scale linearly with cell length in cells of diverse sizes (haploid, diploid, and cells artificially enlarged by a cell-cycle block), but cable length also scales with cell volume (with a power law – roughly with the cubic root of volume). The authors then propose a couple of possible models that would account for this scaling behaviour and show data that is in agreement with the idea that either assembly or disassembly rates are dependent on cable length, leading to a balance point at length equal that of the cell. The underlying molecular mechanism of this balance-point model is not examined, except for the finding that Smy1, which the authors previously proposed serves to limit cable length in an "antenna model" (Mohapatra et al., PLoS Comput Biol 2015), is not involved.

The correlation between cable length and cell length is very intriguing and suggestive that cell length is the relevant measure used by cells to set the length of their actin cytoskeleton. However, the presented data do not exclude that the relevant measure may be cell volume, with which actin cable length scales with cell volume using a more complex hypoallometric power law. To rigorously test whether cell length rather than cell volume is the relevant parameter, it would be necessary to decouple length from volume and test how actin cables length scales with these measurements.

The authors propose a balance-point model in which cable assembly and disassembly rates are balanced when the cable has the length of the cell due to either rate being cable length-dependent. They contrast this to a boundary model in which cable growth would abruptly stop when reaching the model cell distal pole. The experimental data to discriminate between these model focuses on measured cable extension rates in WT haploids, and normal-sized and enlarged cdc28-13 mutants. These measurements of actin cable extension by fluorescence microscopy are very challenging, and the authors should be commended for attempting it. However, they also raise uncertainty. Looking at the movies and the time-lapses, there are clearly many actin cables that do not behave as a simple birth at the neck followed by extension towards the opposite cell pole. Some of the tracking is also not certain – see for instance 17 to 18 s in movie 2: it looks like a big jump to a structure that was actually already present in the first of these two timepoints. This reduces somewhat the confidence in the conclusion that rate extension deceleration scales with cell length.

In summary, the finding of linear scaling between actin cable length and cell length is interesting, but whether cell length is the relevant parameter for this scaling is not fully established. There is a significant degree of uncertainty associated with the measurements of cable extension. While the current data is in agreement with a model in which cable extension diminishes with cable length, the mechanism of how this may be coupled to cell length is unknown.

Reviewer #3:

In this paper the authors find that the length of yeast actin cables scales with cell length. Cable length is studied using haploid, diploid, and cdc28-13 cells that grow abnormally large. Cable length extension rate is found to decrease with extension distance, at a different rate depending on cell size, supporting a "balance-point" mechanism of length regulation. The ratio between the shortest and longest cables in this work is a factor of order 2 (Figure 1F). This factor is significant to make this work interesting in the context of size regulation (though one can also be somewhat skeptical if a factor of 2 is large enough to unambiguously determine scaling mechanisms, given the multitude of actin regulators in cells that can provide such a change). Overall, this is a nicely written paper. However, I have several concerns as described below.

1) Measurement of cable length and steady state length. The study depends heavily on the ability to measure actin cable length. But how cable length was measured in 3D is not presented with sufficient detail. I think it is essential to show convincing 3D images of cable end identification for the majority of actin cables in a cell. I am suggesting this since cables that reach the cell back may "turn around" and/or form bundles or unbundle through interactions with other cables.

The extension rate of actin cables that grow from the bud neck to the cell back is shown in movies and quantified in the figures. However, it's not clear if these cables eventually *stop* elongating. For example, in Figure 4D the extension rate does not decay to zero at the longest times. That seems to me to be an essential point since I would expect that if one is able to measure the length of most actin cables in the cell, then one should be able to see most of these cables stop extending.

2) I found the contrast between the two models, "boundary-sensing" and "balance-point" was not so sharp: the difference is on whether the extension rate decays more or less abruptly with distance along the cell. I also don't see if either of these models as presented is excluded by the data. The authors convincingly show that the cable extension rate decays with cable length, as would be expected from a balance-point model. However, as mentioned in comment 1, it is not clear where the extension rate decays to zero in graphs such as Figure 1F, 3B, 4D. If cable elongation ends abruptly at the longest time in these graphs, then this would indicate a boundary-sensing mechanism (so overall a combination/intermediate model).

3) I feel that the mechanism by which the actin cable system reaches a steady state needs to be clarified. We see a few cables that start from the bud neck and grow to the whole cell. Is this typical or are these rare cases? If rare, are they still representative? Do cables disappear to allow for new cable growth? Such processes change cable length so they are linked to the central theme of cable length regulation.

4) There is a lack of discussion and experimentation of known regulators of actin assembly and disassembly. Perhaps it's ok to leave the precise mechanism providing the feedback of cable deceleration for future work, however I feel that at least some discussion would need to be provided. For example, cofilin might sever filaments in age-dependent manner and cofilin-decorated filaments might be prone to breaking when buckled. Myosin motors are also known to regulate the extension rate of cables.

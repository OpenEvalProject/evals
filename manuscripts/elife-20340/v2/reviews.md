# Peer review - Round 1

Editors:
- Jeff Smith, University of Virginia , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20340.031](https://doi.org/10.7554/eLife.20340.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "An aging-independent replicative lifespan in a symmetrically dividing eukaryote" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Each reviewer thought the study was technically well done and the results showing that S. pombe does not age were convincing. However, the major issue comes down to novelty. Two of the reviewers correctly pointed out that the microfluidic assay has already been published from your lab, and another group previously showed that S. pombe does not age, but using a microcolony-based assay. Your new high-throughput system is much better, but the conclusion that S. pombe does not age was already published, making the current findings less novel. After extensive debate, we decided the story does not reach the bar for novelty to be acceptable for publication eLife. I'm sorry for the disappointing news. The individual reviewer comments are included below.

Reviewer #1:

This manuscript by Spivey et al. describes a novel high-throughput microfluidic system for tracking the replicative lifespan (RLS) of the symmetrically dividing yeast, Schizosaccharomyces pombe. There have been conflicting reports of whether S. pombe actually ages or not, probably because of the difficulty in reliably following individual cells that have divided through fission. The multiplexed fission yeast lifespan microdissector (FYLM) solves this problem by forming a trap that traps and retains one cell pole and then allows new cell poles from the fission to flow away. The authors also developed a robust image analysis software package with the clever name "FYLM Critic". An earlier, single-channel version of this microfluidic system was previously described by the authors as a proof of principal, but this one appears to be much improved. FYLM is used in this study to demonstrate that S. pombe cells do not display age-associated changes in growth or morphology, and their rate of death does change with replicative age. Rather than fitting a Gompertz model for survival that takes into account age-dependent and age-independent contributions, the S. pombe data instead fits a model of single exponential decay. These cells apparently die stochastically, without any increased risk per generation.

Sir2 overexpression and rapamycin treatment, two conditions that extend S. cerevisiae RLS and lifespan of other model eukaryotes, actually extended S. pombe RLS as well. However, the effects remained independent of aging, and instead worked through aging-independent mechanisms. Deletion of the SIR2 gene had no effect on RLS, which was somewhat surprising given the positive effect of overexpression. SIR2 mRNA levels were increased 6-fold as measured by RT-PCR. However, this does not necessarily mean that the Sir2 protein level increased that much. Sir2 is epitope tagged in this strain, so the authors should look at Sir2 protein by western blotting.

mCherry-tagged Gar2 was used to monitor rDNA locus dynamics/segregation in the live cells. There is appears to be a correlation between improper rDNA segregation and RLS. Furthermore, a very short-lived rqh1∆ helicase mutant displayed even more missegregation. The authors therefore conclude that Rqh1p promotes longevity by suppressing rDNA instability. However, the extremely short RLS of the rqh1∆ mutant could be caused by additional, more general chromosome segregation defects. Some kind of control for general chromosome segregation seems important, perhaps centromeres.

Sir2-dependent rDNA array stabilization is considered one of the key mediators of RLS regulation in S. cerevisiae. It would be interesting to test whether Sir2 overexpression or rapamycin prevents the rDNA dynamics defects in replicatively "aging" S. pombe cells. In other words, is the rDNA contributing to the aging-independent RLS extension by Sir2 overexpression or rapamycin?

Reviewer #2:

This manuscript investigates replicative lifespan (RLS) in S. pombe using a microfluidics device developed by the Finkelstein lab. This allows them to follow individual cells up to 75 divisions before more than 50% of a population of cells has died. The conclusions from the study are that S. pombe does not "age", i.e. the cells do not show the expected features commonly associated with aging, like a slower division time and larger cell volume in the last few divisions before death. Furthermore, the likelihood of death does not increase with increasing numbers of cell divisions. Also, the siblings of dead cells do not show an increased chance of death. The system is further characterized to recapitulate the fact that Sir2 overexpression and rapamycin treatment increase RLS, and that increasing rDNA recombination causes decreased lifespan.

The conclusions of this study are congruent with an earlier study from the lab of I. Tolic-Norrelykke (Coelho, Current Biology 2013), which also concluded that S. pombe does not age. The present work follows individual cells over a much longer period of divisions, whereas the Coelho study analysed microcolonies with up to eight cell divisions. Nonetheless, the conclusions are basically very similar.

This study extends the observations of Coelho by analysis of Sir2 overexpression and rapamycin, two interventions that were previously known to extend lifespan.

From all I can tell, the data collection and analysis is sound. The novelty lies in the extent of data collection and the statistics, but the findings support earlier conclusions. Hence, it will be a judgment call as to whether this constitutes enough novelty for publication in eLife.

Reviewer #3:

The authors used a microfluidic device to trap individual fission yeast cells and monitored their growth and death patterns. The main conclusion is that fission yeast does not age, in terms of growth and death rates, with respect to replicative age. While the manuscript presents interesting, solid results, the microfluidic device ("FYLM") was published by the same group previously (Spivey et al., 2014) and the conclusion that S. pombe does not age was also published by another group (Coelho et al., 2013). The major contribution of the present work is the confirmation of the latter by extending the replicative age in the experiments by 5 to 10 fold. These recent advancements are reminiscent of the development in bacterial senescence several years ago (Wang et al., 2010 and references therein).

Comments:

1) In Abstract, "Nearly all RLS studies have used budding yeast[…]" -> "Nearly all RLS studies of single-cell eukaryotes have used budding yeast[…]"

2) Also in Abstract, "Here, we describe a multiplexed fission yeast lifespan micro-dissector (FYLM); a microfluidic platform for performing high-throughput and automated single-cell micro- dissection." This sentence reads as if this is the first time the authors are reporting their microfluidic device, but it was already published in Spivey et al., 2014.

3) The puns "FYLM", "multiFYLM", "FYLM Critic" are cute, but rather disingenuous. The Figure 1 in the manuscript and the figure in the Abstract in Spivey et al., 2014 remarkably resembles Figure 1 in Wang et al., 2010 for bacteria. Why invent a new name when the basic design of the device is essentially identical to what has been already published and widely adopted?

4) Figure 2A. I suggest to plot from 0.1 to 1.0 for y-axis. Since the main result in this figure is the exponential decay of 'fraction surviving', the current range (0.01 to 1.0) puts unnecessary importance on what is less important.

5) Figure 2B and in the main text. I suggest the authors call "the hazard function" a more easily understandable and straightforward "death rate".

6) Figure 2—Figure supplement 2; Figure 5—figure supplement 2. The exponential decay and constant death rates are not as clear here. For 2B, the data is presented in a misleading manner. The range of y axis should be from 0 to 0.07. The red fit lines should not mask the data in both Figure 2A and Figure 2B.

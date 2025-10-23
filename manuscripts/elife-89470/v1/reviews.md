# Peer review - Round 1

Editors:
- Vincent Castric, University of Lille France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89470.4.sa0](https://doi.org/10.7554/eLife.89470.4.sa0)

This important study extends existing sequentially Markovian coalescent approaches to include the combined use of SNPs and hypervariable loci such as epimutations. This is an intriguing addition to infer population size history in the recent past, and the authors provide solid validation of their methods via simulation and analysis of empirical data in Arabidopsis thaliana. Given the increasing availability of such data, this work is a timely contribution and represents a foundation for further developments to explore when and where these methods will be best used.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89470.4.sa1](https://doi.org/10.7554/eLife.89470.4.sa1)

The authors developed an extension to the pairwise sequentially Markov coalescent model that allows to simultaneously analyze multiple types of polymorphism data. In this paper, they focus on SNPs and DNA methylation data. Since methylation markers mutate at a much faster rate than SNPs, this potentially gives the method better power to infer size history in the recent past. Additionally, they explored a model where there are both local and regional epimutational processes.

Integrating additional types of heritable markers into SMC is a nice idea which I like in principle. However, a major caveat to this approach seems to be a strong dependence on knowing the epimutation rate. In Fig. 6 it is seen that, when the epimutation rate is known, inferences do indeed look better; but this is not necessarily true when the rate is not known. (See also major comment #1 below about the interpretation of these plots.) A roughly similar pattern emerges in Supp. Figs. 4-7; in general, results when the rates have to be estimated don't seem that much better than when focusing on SNPs alone. This carries over to the real data analysis too: the interpretation in Fig. 7 appears to hinge on whether the rates are known or estimated, and the estimated rates differ by a large amount from earlier published ones.

Overall, this is an interesting research direction, and I think the method may hold more promise as we get more and better epigenetic data, and in particular better knowledge of the epigenetic mutational process.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89470.4.sa2](https://doi.org/10.7554/eLife.89470.4.sa2)

A limitation in using SNPs to understand recent histories of genomes is their low mutation frequency. Tellier et al. explore the possibility of adding hypermutable markers to SNP based methods for better resolution over short time frames. In particular, they hypothesize that epimutations (CG methylation and demethylation) could provide a useful marker for this purpose. Individual CGs in Arabidopsis tends to be either close to 100% methylated or close to 0%, and are inherited stably enough across generations that they can be treated as genetic markers. Small regions containing multiple CGs can also be treated as genetic markers based on their cumulative methylation level. In this manuscript, Tellier et al develop computational methods to use CG methylation as a hypermutable genetic marker and test them on theoretical and real data sets. They do this both for individual CGs and small regions. My review is limited to the simple question of whether using CG methylation for this purpose makes sense at a conceptual level, not at the level of evaluating specific details of the methods. I have a small concern in that it is not clear that CG methylation measurements are nearly as binary in other plants and other eukaryotes as they are in Arabidopsis. However, I see no reason why the concept of this work is not conceptually sound. Especially in the future as new sequencing technologies provide both base calling and methylating calling capabilities, using CG methylation in addition to SNPs could become a useful and feasible tool for population genetics in situations where SNPs are insufficient.

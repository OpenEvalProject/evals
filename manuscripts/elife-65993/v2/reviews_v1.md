# Peer review - Round 1

Editors:
- Paul B Rainey, Max Planck Institute for Evolutionary Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65993.sa1](https://doi.org/10.7554/eLife.65993.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We really enjoyed this insight into the complexities of even simply gene regulatory networks, which you show are nowhere near as simple as we thought. Indeed, We think insights into the effects of transcriptional read-through will interest many concerned with the connection between genotype and phenotype.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Local genetic context shapes the function of a gene regulatory network" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after considerable consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

It was not easy coming to this decision. All reviewers and the reviewing editor found much merit in the work. Particularly appreciated was the extensive generation of gene combinations and evidence of effects on the GRN. But the agreed position among the reviewers that more was required in order to rise about the bar necessary for publication in eLife. In particular, all felt that lack of insight into the molecular basis of the observed effects amounted to a significant shortcoming.

Recognising that this is something that could be overcome there was discussion as to whether this could be achieved within a two-month window. Of course all recognised that in the time of covid this is an unrealistic time frame, but nonetheless, it was felt that significant additional work was required. This said, we would be happy to consider a fresh resubmission at some future time if the authors were able to deliver additional information as to the effect of the GRN on transcriptional read-through.

Reviewer #1:

I flipped about with this manuscript, from mildly enthusiastic to very enthusiastic; back and forth. On balance though, I think it provides useful additional understanding of factors affecting the evolution of GRN. Like amplification, and various structural changes, those affecting the relative placement of genes can have unrecognised effects.

The work itself is thorough and clean. A very simple contrived construct is used and the various permutations of possible gene placements are comprehensively analysed. The work in chromosomal context is very nice, and especially so the work placing the three genes in separate chromosomal locations.

Where I was left hanging was with regard to the molecular mechanism. I buy the data showing that the mechanism involves transcriptional read-through, but the reader is left with no additional understanding. The obvious unaddressed question is why does transcriptional read through occur given otherwise identical terminators?

Reviewer #2:

The authors describe an issue well-known to synthetic biologist who are trying to build synthetic gene circuits in a predictive manner, namely context-dependent effects. More specifically, they are focusing on the order of the individual transcriptional units of a circuit and observe different behaviours, not only quantitatively, but also qualitatively. I like the approach of using a synthetic circuit, I think it is interesting to quantify such an effect in more detail and also to put it into an evolutionary context. However, I did not enjoy the manuscript as much as I was hoping for after reading the Abstract, due to following reasons:

1) Very little thought was put into making the figures self-explanatory. I had to go several times for and back between text, figure and figure captions to understand what is actually shown, how the experimental results compare to the expectations and how the results compare across the different systems. Some extra schemes might help here. This applies to all of the figures, but I will explain it in more detail for Figure 1 and Figure 4

Figure 1A: Explain and show in detail what phenotype is expected. Maybe use the mathematical model used later to illustrate the expression level of each involved protein under all conditions. As the networks involve a negative feedback loop, I find this non-trivial. The expected behaviour will depend on the repression strength of lacI. B. also label the prompters. C: instead of only the labels "CfLfTf" etc, add the small schemes, including labelling.

Figure 4A: Add the interactions into the scheme and the expected behaviours for each case (with/without readthrough). Also include YFP in this scheme. This might be trivial for the authors, but it is not for a reader, who has not worked years on that project

The figures would also be easier to read if you used some colours.

2) The experimental evidence for the author's conclusion that transcriptional read-through is the main factor for some of the unexpected phenotypes is rather slim. The only evidence is Figure 4. I would like to see more evidence. They say a RNAse site prevents it to detect in Western blotting. But as the system is synthetic, it is very simple to remove that site. Moreover, they should insert about 10 different terminators and use qPCR or RNAseq to quantify the read-through in order to get an idea how wide-spread this phenomenon is. It would also be easy to put multiple terminators in a row and see if that recovers the expected behaviour. The beauty of a synthetic system is that those experiment are done in few weeks. (Of course not if the lab is shut down due to COVID-19…)

We observed that it is very easy to get unwanted promoter in sequences. That is supported by literature that shows that is very easy to get promoters from random sequences. Could this be an alternative explanation? Please discuss whether and how this can be distinguished from read-through?

3) The effect in the native circuit is rather modest. Is this even significant? No statistical test was performed. Again, the read-through should be quantified by qPCR or RNAseq.

Reviewer #3:

Overall, there are some conceptual issues with the study, as presented. The study does demonstrate physical context of genes does impact outputs. However, there are some issues.

The research and findings are not well placed in the field. There are a number of notable studies that have examined physical location of genes and their impact on regulatory networks and/or physiological outputs using natural and synthetic systems. For example, phage T7 was refactored and these synthetic T7 phages have notable differences in infectivity, etc. from their WT T7 counterpart (Chan, 2005). Additionally, a study by Wu and Rao (2010) has examined the impacts of genetic arrangement on the outputs of autoregulatory circuits. There are several other similar studies, beyond the few cited in this manuscript. How this approach builds on these studies is not made very clear.

The study seems to have honed in on one particular aspect that may affect a regulatory network – transcriptional readthrough. This seems to be explanatory for this system, and is likely a direct use of using very strong promoters (P_L derivatives). Use of such strong promoters, regardless of the efficiency of a terminator, will result in significant amounts of readthrough. How transcriptional readthrough generally contributes to regulatory networks is debatable. The data presented to support the importance of readthrough (Figure 5), while possibly statistically significant, does not provide convincing evidence for strong effects. Building on this point, how frequently are transcription factors in a multicomponent network encoded in close proximity? Would transcriptional readthrough provide any explanation as to the broader patterns we see in genome structure – even for E. coli?

There is very little explanation for why readthrough into cI has such strong effects, when readthrough into lacI or tetR have smaller (or no) effects on network behavior. Are these effects on cI strongest because CI is most proximal to your output (YFP production)? Do these effects correlate in any way to DNA binding affinity of each transcription factor?

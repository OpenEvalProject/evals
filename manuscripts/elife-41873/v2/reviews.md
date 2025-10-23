# Peer review - Round 1

Editors:
- Philipp W Messer, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41873.016](https://doi.org/10.7554/eLife.41873.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A Y-chromosome shredding gene drive for controlling pest vertebrate populations" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Diethard Tautz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Prowse and colleagues demonstrate the in vitro efficiency of a CRISPR/Cas12a-mediated "Y chromosome shredder" that is proposed as a means of suppressing invasive rodent populations by reducing the availability of fertile males. The manuscript starts by demonstrating the elimination of Y-linked loci in mouse embryonic stem cells with up to 90% efficiency, and then continues by modeling the population dynamics of a Y-shredder drive under varying parameters in silico. While gene drive strategies using sex ratio distortion systems have been studied and demonstrated previously (e.g. X-shredders in mosquitoes), the approach proposed here of targeting the Y-chromosome is interesting and novel.

Essential revisions:

1) Reference to previous studies:

A main concern with the paper is that it lacks any reference to previous studies of gene drive strategies using sex ratio distortion systems. Such systems have already been studied extensively, and some of them have been demonstrated experimentally (e.g. X-shredders in insects). These omissions make the Y-shredding approach presented in this paper seem more novel than it actually is. The authors should cite some really relevant literature detailing the building of synthetic sex ratio distortion systems in other organisms – in many cases these are also predicated on the specific nuclease-mediated ablation of sex chromosomes (usually the female sex chromosome) through the targeting of repeated sequences. While in this case it is the Y chromosome that is being targeted (with drive – the shredding of Y in mice itself is not novel and was performed previously by some of these authors), the novelty aspect is somewhat diminished in view of the prior art. The authors should revise the relevant section in the manuscript to make this more clear and not overstate the novelty of their approach.

2) Extension and better description of the modeling analysis:

The modeling analysis is clearly the main thrust of this paper, given that the authors do not actually build a functioning drive system. As such, however, this analysis should be made more comprehensive and also needs to be much better described. In its present form, this study is not repeatable.

We specifically urge the authors to compare the performance of their method against X-shredders, which are not expected to suffer from some of the stated disadvantages of this approach (in particular the reliance on males become limiting).

There also seems to be no particular reason to cap F (maximum number of females that a male can mate with) at 5. Either justify it, or make a theoretical estimate based on overlapping home ranges for the mice and also probe higher value such as 10 or more to take into account initially good opportunities to search for mates when males are rare. Better yet, identify the exact level at which the different drives considered are unable to effectively suppress the populations.

In this paper as well as in Prowse et al., 2017, the demographic parameters were fixed. There should be some investigation into the sensitivity of results due to uncertainty in these values as they can vary widely across populations. This is important for reporting uncertainty on the prediction of effectiveness of the gene drive tool.

The sensitivity analyses and the actual parameters in it are somewhat unclear. It appears that Table 1 indicates the upper and lower limits of parameters (e.g. probability of Cas9 cutting, probability of NHEJ). However, it is not clear which values were tested in this range, if these varied as continuous or discrete values, and whether they were varied independently. Please explain in more detail.

The model used for homing and NHEJ is also not particularly clear. For example, were the populations modeled such that the target allele frequency is the sum of uncut + cut, where cut = homing + NHEJ? Is PN represented as the proportion of all target alleles or the proportion of target alleles that were cut? When PN>0, is each of three gRNA target sites considered independently, or does PN reflect a resistant locus (all three gRNA sites are mutated)?

The rules of polygynous mating should be described in more detail. Can there be multiple paternity, and if so what are the genetic rules for that process? If not, how might that affect results (as it is a common process in mice it seems important to discuss). Additionally, did the growth rate of systems with Fmax=1 differ from those of Fmax>1 or were r's adjusted to keep them constant across the different mating structures?

The model structure (equations/pseudocode) and code for implementation should be provided in the supplementary information. Currently, the reader has to refer to Prowse et al., 2017, to understand the general structure of the model, but this doesn't include the advancements presented here.

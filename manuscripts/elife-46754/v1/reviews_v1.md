# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- Jonathan Wells, Cornell University United States

## Review text

DOI: [10.7554/eLife.46754.037](https://doi.org/10.7554/eLife.46754.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The role of structural pleiotropy and regulatory evolution in the retention of heteromers of paralogs" for consideration by eLife. Your article has been reviewed by Patricia Wittkopp as the Senior Editor and Reviewing Editor, and two reviewers. The following individual involved in review of your submission has agreed to reveal his identity: Jonathan Wells (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a nice study that tackles an interesting question: namely, does the quaternary structure of an ancestral protein constrain the evolution of subsequent paralogs? The central hypothesis of the paper is that, in cases where the ancestral protein is homomeric, selection to maintain binding interfaces between newly duplicated paralogs will lead to a decrease in the rate of functional divergence of those genes.

In testing this hypothesis, the authors arrive at three key findings: Firstly, heteromeric paralogs of homomeric proteins are common, and are functionally more similar than paralogues of monomeric proteins. Secondly, in silico evolution suggests that negative selection acting on homomeric interfaces is sufficient to maintain heteromeric interactions between paralogs, but if selection acts only on one paralog, then the heteromeric interaction will slowly be lost. Finally, they show that diverging regulatory evolution (e.g. cell localization) can lead to relaxation of the structural constraints, thus enabling functional divergence.

Essential revisions:

1) Modeling of selection. The authors use the method previously described in Kachroo et al., 2015 to calculate the probability of fixation of new mutations; this is "an efficient implementation" of a model described by Sella and Hirsch, PNAS (2005). According to Kachroo et al., equation 3 is accurate as long as the product of the mutation rate and effective population size, N, is very small. Whilst this assumption is generally valid for wild yeast populations, in this study N is set to 1000 – several orders of magnitude lower than is realistic (Tsai et al., 2008). Using more plausible values for N, equation 3 would essentially guarantee fixation for beneficial mutations and vice versa, over-simplifying things. To address this issue, the authors should justify their choice of model and associated parameters and, ideally, demonstrate that their results are robust to changes in these parameters. It would be interesting to see if this affects the "selection on HET AB" case.

2) Analyses of age of duplication. Please clarify how the age of WGD paralogs was calculated, and whether this differs to the method used to calculate SSD ages. Are the two directly comparable? If not, then it might affect some of the conclusions (e.g. subsection “Paralogous heteromers frequently derive from ancestral homomers”). Similarly, people might take issue with the assumption that evolutionary rates are the same for SSDs vs. WGDs. A useful paper here might be Zhu et al., 2013.

3) Analysis of sequence divergence. I include one reviewer's description of this concern in its entirety, but both reviewers agreed with this concern: "In Figure 2E, fewer SSDs form HETs in general, compared to WGDs. This is probably related to the age of duplication events, as the authors note. The two groups of WGDs have the same age. But the SSDs would be from many different times. The authors mention that most SSDs are older, but it seems that some should still be relatively very young. Assuming that an ancestral gene whose protein homodimerizes undergoes a duplication event, the two duplicates should both homodimerize and heterodimerize among them. Accordingly, very young duplicates should belong mostly to group HM&HET. As time goes by, mutations and selection may separate them in two proteins that form only homodimers (group HM), or one of them still homodimerizes and the other evolves towards heterodimerization-only with the other paralogue. In Figure 2F, these two different cases of HM&HET are merged in one group.

I have major concerns about the sequence divergence analyses and their conclusions. First of all, we know that intrinsically disordered regions evolve fast, compared to well conserved domains. Also, some regions may function as flexible linkers (that also evolve fast) between domains. One protein family may evolve fast and another protein family may be very well conserved, irrespective of protein interactions. How do the authors control for this fact?

Moreover, the pleiotropic effect should be on the interaction surface or more broadly on the interaction domain that is responsible for the formation of the homomer or HTs. Usually, this is a well-defined domain or two. Usually, this interaction domain is one of the well conserved regions of the protein and many times a small part of it. I can't imagine how a sequence divergence analysis of the whole protein is meaningful. Maybe a PFAM analysis of the pairs of paralogues and inclusion only of the interacting domains instead of the whole protein? This is a problem. The crystallographic structures analysis they did in subsection “Paralogous heteromers frequently derive from ancestral homomers” is trying to address this problem, but I feel it may not be enough. Another concern is that intrinsically disordered regions are usually involved in transient interactions whereas domains are usually involved in more stable interactions, although this is not an absolute rule. Is this accounted for by the authors in their sequence divergence analyses? Probably not.

In my view, the level of sequence divergence of two paralogues is affected by their time of divergence, but also it is affected by the domain architecture of the protein and whether the interaction is transient or stable. Thus, the authors may need to control for them as well. Basically, the interaction surface/domain is under certain constraints. But other parts of the protein may evolve fast or slow for many other reasons.

Similar concerns exist for functional similarity analyses with GO, phenotypes and genetic interactions. A protein may have more than one functions that may be irrelevant with the formation of HMs and HETs. High functional similarity could only be due to short time after divergence. How do the authors control for that? In my opinion, although some statistically significant differences exist in the analyses of Figure 3, the final message is not clear and strong. "

4) In Figure 4, the positive and negative controls (panel B and C respectively) both behave as expected. However, I was surprised that selection to maintain the heteromer (D) appeared to be a stable state, as there seems to be no obvious reason why the homomers could not eventually be lost. In figures 4 and S9 it seems that the "selection on HET AB" panels seem to be noisier – is this coincidental?

5) This paper integrates data from many sources, which is a strong point. But at the same time, this makes it a lengthy paper, perhaps with too many analyses. At some points, it is easy to lose the main message of the paper and why the authors were doing a particular analysis. Please make the paper more clear and concise, possibly putting details of some analyses (or even some entire analyses) in the supplementary material.

6) Second paragraph of Results section discusses the effect of expression on detecting HMs by PCA. Since expression has an effect on detection of PPIs, is the difference of HMs among singletons, SSDs and WGDs (mentioned in subsection “Homomers and heteromers in the yeast PPI network”) due to this reason? Would it be feasible for the authors to collect subsets of singletons, SSDs and WGDs with similar magnitudes of expression (use bins) and check difference of HMs for these 3 controlled subsets?

7) Please clarify statistics in Supplementary file 2—table S5. More information should be included in that worksheet or somewhere else.

8) In Figure 2F, although there are some statistically significant differences, the various groups span similar orders of magnitude. Please comment on this observation.

9) Optional: Is it feasible for the authors to do an extra series of wet-lab experiments and experimentally test the HMs and HETs of a selected protein with crystal structure that underwent simulated evolution with the different selection scenarios? That would strengthen the paper further.

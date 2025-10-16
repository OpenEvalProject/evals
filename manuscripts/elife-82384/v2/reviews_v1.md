# Peer review - Round 1

Editors:
- Vincent Castric, https://ror.org/02kzqn938 Université de Lille France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82384.sa0](https://doi.org/10.7554/eLife.82384.sa0)

This manuscript details an important development of population genetics theory that can be used to infer past changes in the selfing rate of natural populations. The inference procedure is convincing and represents a substantial improvement upon previous methods. The work will be of broad interest to researchers studying mating system evolution and its consequences and will improve demographic inferences drawn from population genetic approaches.


---

# Peer review - Round 1

Editors:
- Vincent Castric, https://ror.org/02kzqn938 Université de Lille France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82384.sa1](https://doi.org/10.7554/eLife.82384.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Inference of evolutionary transitions to self-fertilization using whole-genome sequences" for consideration by eLife. We apologize for the uncharacteristic delay in the handling of your manuscript, which was due to the absence of an editor. Your article has now been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Takashi Tsuchimatsu (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers appreciated an important contribution to the study of mating systems transitions, and the welcome addition of promising new methods to detect ancestral changes in the rate of selfing. In spite of these promises, however, they also judged that the current manuscript did not reach its full potential and needed major revisions on two main aspects:

1. The comparison with the estimate of the time since A. thaliana has been a selfer by Bechsgaard et al. (2006) needs to be more careful and comprehensive. This includes in particular the lack of a proper test beyond the comparison of point estimates, and the use of different mutation rates. The importance of this latter point was already noted in a previous review (Shimizu and Tsuchimatsu 2015; Ann Rev Eco Evo Syst), which is missing from the current version. They also called for an evaluation of the consequences of the (arbitrary) choice of a limited number of genomic regions, and a more formal comparison of the ancestral population size estimated by their method with those available from the literature for that species.

2. Reviewer 3 noted a number of missing references that are required to better anchor the present developments in the previous theoretical literature, and made a series of precise suggestions with that regard. Along this line, the manuscript should better highlight that the « core » process upon which the estimation procedure is based (the effect of selfing on the association between segment length and TMRCA) is currently evaluated mostly through computational approximations. The theoretical treatment of this relationship is currently relegated to an appendix, the presentation of which could be improved greatly.

Reviewer #1 (Recommendations for the authors):

1) L65-71: I would suggest citing Stebbins' work because he is the pioneer who studied the frequent transition to selfing and the evolutionary dead-end.

2) Always italicize S of "S-locus".

3) L93: This would be 413,000 years instead of 430,000 years.

4) It is an important finding that population size is more accurately inferred when the outcrossing-to-selfing transition is considered. As discussed, this would be potentially important for other organisms including crops, as the domestication process often involves a shift in mating systems. In that sense, authors could discuss how the estimated population size change of Arabidopsis thaliana (Figure 5B) is (or is not) consistent with previous estimates of population size.

Reviewer #2 (Recommendations for the authors):

As the authors did not even provide page numbers, I use line numbers to indicate the start of sections.

With regard to Theme (1), equations [1] and [2] are attributed to Nordborg, but Fu (1997 Genetics) and especially Golding and Strobeck (1980 Genetics) should also be cited.

The authors use [1] and [2] to develop a sequential Markov coalescent algorithm for estimating ancestral population size and the time since a change in the level of selfing.

Once again, the writing suggests Theme (1). In the Results section (L 202), a rain of references to sequential Markov methods appears, with little discussion of their relationship to the authors' work. Such scholarly discussion might be expected to appear in the Introduction or Discussion sections, but do not. For example, Palacios et al. (2015 Genetics) are relevant to the establishment of a solid inferential framework for approaches of this kind.

The authors address teSMC in a manner that appears to relegate it to mainly theoretical interest because the age of the MRCA of a chromosomal segment (TMRCA) is not in general known. Even so, the authors detect a possibly significant trend in the course of forward simulations of the process: a change in selfing rate induces a change in the magnitude of the negative association between segment length and TMRCA. They seek to use this phenomenon as a signature of a shift in the mating system apart from a shift in population size.

With regard to Theme (2), the paper would have been improved if they had undertaken to explore the basis of this relationship theoretically. The paper only provides an opaque description:

"the probability of a recombination event is not increasing linearly with time" (L 178).

The rate of recombination (r) is in fact not changing at all, and "time" here may (or may not) mean TMRCA. The ambiguity of this sentence leaves considerable room for guessing, and the reader should not have to guess at all. It is ρ_\σ (which is proportional to the probability that the next evolutionary event back in time is a recombination event rather than a coalescence event) that is affected by selfing. Both ρ_\σ and TMRCA decline as selfing increases, but the change in selfing rate has less effect on TMRCA. Is this what L 178 means? In any case, it should surely be stated more clearly.

A few lines later, we have

"We also made the important observation that all the segments that coalesce in the outcrossing phase, trace back their ancestry to a subset of segments that do not coalesce more recently

than t_\σ…." (L 188)

Are the authors saying that segments that coalesce before t_\σ do not coalesce after t_\σ? These are just a few examples (on the same page) of what are NOT minor grammatical lapses but major barriers to communication. They give the impression of sloppiness or indifference to the reader.

The authors note (L 275)

"Unfortunately, while the lengths of TMRCA-segments are straightforward to calculate on simulated genealogies (Figures 1A, B), it is more difficult to estimate them based on genomic diversity data alone."

Unfortunate or not, observing genetic diversity and not TMRCAs is of course the relevant case. While statistical uncertainty does not appear to be addressed for teSMC, it is addressed in the authors' ABC implementation of their approach (tsABC). As this section does deal with basing inferences on observations of genetic diversity (rather than TMRCA), it has greater relevance to the analysis of real data.

Even so, the description (L 288) in the main text suggests only that results were good, but not why or even exactly what the results were. In Figure 3, the reader must glean from the caption exactly what was done and what is being shown. Exactly what is on the X-axis is unclear. The t_\σ at the far right might suggest that the X-axis represents the true time since the switch to selfing, but it isn't clear whether the units are in generations or years or some multiple of those units. Figure 3 C/D/E appears to depict support for the true t_\σ, but not support for incorrect values. Figure 3 F/G/H does speak to whether t_\σ can be inferred, but the posterior ranges shown seem to be quite wide. After all this eyeballing of the Figure, a reader might be less entirely convinced that the results are as supportive of tsABC as the text suggests.

The next section (L 316) goes off on a tangent regarding background selection. This aspect, while important, might be reserved for a separate study: one in which a rigorous exploration might be conducted. As presented, it is not entirely clear what was done. It appears that genomic data were simulated under a background selection model. What the authors refer to as "robustness" appears to correspond to obtaining similar results from teSMC or tsABC using masked or unmasked data. The term "masking" seems to suggest that only sites NOT under selection were given to teSMC or tsABC, even though those sites were subject to background selection. If this is correct, then the finding that masking versus unmasking gives about the same results does not address the question of model misspecification: both masked and unmasked data sets could give equally bad inferences.

It seems that a more appropriate test would involve simulating data with and without BGS. The question is then whether the masked BGS data give similar results to the full non-BGS data. It is difficult to ascertain whether or not this is what the authors did.

The description of the analysis of real data is confined to a single paragraph (L 349). That the method suggested that self-compatibility arose in the Arabidopsis thaliana lineage sometime between previous estimates (413 KYA and 1000 KYA) seems a rather low bar. The authors claim "remarkable" (L 413) agreement between their results and the 413 KYA figure, which was obtained from a model-based analysis of variation at the S-locus. However, the authors do not even give credible intervals for their estimates. Giving the authors the benefit of the doubt, one might guess that the X-axis in Figure 5 is in units of 10^4 years and that the 95% credible interval is perhaps (55 KYA, 60 KYA).

Does this mean that the Bechsgaard estimate of 41 KYA lies outside the authors' credible range? Note that the Bechsgaard figure assumes the rough estimate of 5 MY for the divergence of A. thaliana from its SI relatives, so that a slight revision of this figure could bring their estimate closer to (or farther from) those of the authors. That no comment or discussion about the results of real data appears bolsters the impression of Themes (1) and (3).

The Discussion begins around L 367. Once again, I am supportive of this submission as primarily theoretical, with the very short treatment of the Arabidopsis data intended only as a worked example. However, the authors seem to have (much) greater ambitions. If the authors actually wish to characterize their work as a breakthrough that opens up long-standing questions to rigorous analysis, then they need to address in detail inferences made on the basis of real data.

For the Arabidopsis analysis (the only real data application), do the authors regard their estimate as superior to the model-based estimate of Bechsgaard? How seriously should the estimates of the changes in population size (Figure 5B) be taken? If the authors wish to argue that the changes in population size are real, they might at least provide credible intervals for the estimates and explore what is known about the ecological history of Arabidopsis.

Authors concede (L 312) that their ABC implementation could not infer the ancestral selfing rate. In the Arabidopsis case, this rate is assumed to be zero, as appropriate for a functional self-incompatibility (SI) system. Does this mean, then, that the method is useful mainly for cases in which the ancestral selfing rate is somehow known? Is their method actually only applicable to Arabidopsis?

Rather than addressing such points, the Discussion appears to cast their method permitting access to a very wide range of questions, including the evolution of sex (Barton and Charlesworth 1998). Exactly what the basis for this claim is unclear, especially since the breeding system shift modeled is wholly sexual (meiotic).

Perhaps the most germane suggestion is for the authors to determine whether this submission is primarily whatever the Discussion is maintaining or a theoretical exploration with a bit of illustration using real data.

If the latter (my view), then the theory sections might be improved. They presently appear in the Appendices as dumps of notes, with little effort invested in concise exposition. With regards to Theme (2), when presented with an opportunity for theoretical exploration, the authors appear to choose to rely on computation: the lack of theoretical exploration of the trends noted in Figure 1 and resorting to ABC over a model-based approach come to mind. I suggest that taking a different tack would facilitate deeper insight.

# Peer review - Round 1

Editors:
- Graham Coop, University of California, Davis United States

Reviewers:
- Graham Coop, University of California, Davis United States
- Brian Charlesworth, University of Edinburgh United Kingdom

## Review text

DOI: [10.7554/eLife.48548.015](https://doi.org/10.7554/eLife.48548.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Asexual reproduction drives the reduction of transposable element load" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Graham Coop as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Diethard Tautz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Brian Charlesworth (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers and I appreciated the analysis and results. I have included the two reviewers' comments below.

Please respond point by point to the reviewer comments below. The major comments that definitely need addressing are:

1) Moderate the causal language concerning selection and increase in excision rate, the evidence for this is indirect at best. See reviewer 1.

2) Reviewer 2 raises a concern about how the non-independence of temporal samples from the same population replicate are dealt with. One suggestion from the reviewer/editor discussion was to just use the difference between the initial and end points. The authors more generally need to be clearer about the analysis performed, e.g. give the formulae for the linear models run.

3) Reviewer 2 raises some questions about full-length and non-reference TEs that need to be addressed.

4) The McDonald experiment is of pooled sequencing, thus you are averaging over population-frequencies of TE at each locus. While TE-calling from the short-read data, and asexuality, it might be very hard to do anything with the frequency of TEs at each locus I thought it would be helpful to more fully acknowledge that the current analysis (I think) confounds the number TE loci in the genome and the frequency of the TE at each locus.

Reviewer #2:

This paper presents an interesting analysis of the population dynamics of transposable elements (TEs) in long-term experimental populations of budding yeast, comparing sexual and asexual populations. The data are analysed in the light of simulations, which extend an earlier study by Dolgin and Charlesworth, 2007, to match more closely the properties of the yeast populations. The overall conclusion is that excisions of the LTR retrotransposons (presumably by recombination between the LTRs; this could have been investigated) cause a decline in TE copy number in the asexuals, whereas the sexuals seem to stay more or less in equilibrium.

This is one of the few studies of this type of problem, and illustrates the difficulty of making generalisations about the fates of TEs in populations with different mating systems, as the authors make clear. I have to take their bioinformatic analyses on trust, as I lack the relevant expertise, but they seem to have done a thorough job of these. Overall, this is a nice paper.

My only criticism is that they emphasis the possible role of selection for an increase in excision rate in explaining their results, but I could not see that they have presented any solid evidence that this has actually happened. In an asexual population, all kinds of hitchhiking will be going on, so any increase in frequency of a modifier of excision rate could simply be due to such an effect, although of course one would not expect consistency across replicate populations. They need to make it clearer what the evidence for such selection actually is; it's not obvious to me that there has been an increase in excision rates.

Reviewer #3:

Bast et al. address how sexual reproduction affects transposable element (TE) accumulation in paired sexual and asexual lineages of yeast. As noted in the manuscript, much of the literature surrounding the issue of the impact of sex on TE accumulation is confounded by deeper evolutionary timescales, different effective population sizes, and changes in mating system. Utilizing existing data of yeast experimental evolution lines to get around these issues, Bast et al. find that TEs are spread through sex, and driven towards extinction in asex lines. The manuscript is clearly written and easy to follow. Specific comments below.

My understanding from a brief glance at the McDonald et al., 2016 paper these data come from suggests that the data represent eight separate lineages, such that each point should be connected through the time series in Figures 1 and 2. I'm not familiar enough with the statistics involved, but if each is an independent lineage through time, does this need to be included in analyses? It also seems that some of the uncertainty in TE genotyping could be addressed using replicate lineages – if a full-length copy is 'excised,' we don't expect to see it again in later generations of that replicate.

- Main text, fifth paragraph: Throughout the manuscript, the use of the term 'excision' might confuse readers more familiar with different types of TEs. For DNA transposons (cut and paste), this refers to a complete or near complete removal via transposition. In this manuscript, 'excision' is used for solo LTR formation via unequal recombination. To avoid confusion, perhaps 'solo LTR formation' could be used as an alternative to excision.

- Main text, fifth paragraph: It would be useful to add that solo LTR formation (excision) removes the protein coding genes that allow transposition, to make it clear why we care about full-length copies.

- Main text, sixth paragraph: I am a bit confused on the numbers of full length TEs identified. The second to last sentence states only 24 of 50 full length copies can be detected, but the last sentence states asex decreases to 41 full length copies. Although identifying TEs is really difficult, I am concerned that there could be deletions or excisions in these 26 non-assayable copies that overwhelm the signal observed. Could a total count of transposition-competent copies be tracked through time by something akin to the first coverage based approach (like Figure 1—figure supplement 1), using internal protein coding regions? Or is there a way to explain what's happening with these non-assayable copies? Are they always the same copies in every individual?

Doesn't a constant number of non-reference copies through time (Figure 2B) mean that there is an increased transposition rate in asex through time? To me it feels like since both the asex full length copies (presumably the active copies) and reference copies are being removed through time, this means the per-element transposition rate is going up. Again, this could be addressed by identifying how many non-reference TEs are the same non-reference TE copies (at the same loci) through time (although maybe the low coverage of some samples precludes this?). But it's hard for me to think in residuals, so maybe this isn't impacting things, and the slightly more negative trend in asex in 2B reflects the effect of a higher excision rate on generating fewer new copies.

- Subsection “Modelling”: I need a little more information on the TE annotation. How are full length copies being defined from the RepeatMasker output? Those which contain any internal protein coding sequence? A length cutoff relative to the reference db?

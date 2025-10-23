# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70873.sa0](https://doi.org/10.7554/eLife.70873.sa0)

The manuscript by Hoehn et al., introduces a novel approach to measure evolution in B cell responses, and apply it to a wide variety of data sets. The work provides significant new insight into which stimuli induce effective immune responses, and which has the potential to improve vaccine design. This will be of interest to those interested in B cell responses, especially in the case of vaccinations that induce poor immune responses.


---

# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70873.sa1](https://doi.org/10.7554/eLife.70873.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Human B cell lineages associated with germinal centers following influenza vaccination are measurably evolving" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors should try to either show (with simulations) that the data rejects the following scenario or they should include it as an equally likely possibility:

"Suppose that B cell clones expanded and diversified through somatic hypermutation prior to the study period (that is, prior to the secondary vaccination event which is the focus of the study). It seems that preferential expansion of highly mutated subclones during the study period could bias detected sequences towards more divergent sequences, even without ongoing somatic mutation during the study period. Preferential expansion of divergent sequences would give rise to higher average divergence as the study period goes on, giving the appearance of accumulation of additional mutations, but in fact these mutations had occurred prior to the study period and are simply more readily detected in the sparsely sampled repertoire sequencing data after their expansion. Far from being simply a pathological counter-example, this scenario seems biologically plausible, given that B cells harboring more divergent, affinity-matured sequences should generally have higher affinity antibodies that allow them to better compete for limited antigen and thus provide stronger division stimulus. This model predicts that some highly divergent sequences exist at early timepoints and would occasionally be detected."

2. Do you see any evidence for positive (or negative) selection during somatic evolution? Do you see any significant statistical difference between non-synonymous and synonymous SHMs?

3. Please expand the discussion on multiple testing adjustments in the section "Measurably evolving lineages following influenza vaccination show signs of memory B cell origin". Notably, the reported percentages of measurably evolving lineages in several scenarios (7.2% for primary hepatitis B vaccination; 6.5% for allergen-specific immunotherapy; 5.9% for HIV infection) are near the false positive rate of the test (5% of lineages measurably evolving). The authors have performed this test on datasets from ~21 studies, raising a concern that multiple hypothesis testing could give rise to false positives in some of the datasets. These results are interpreted as evidence of measurable evolution, even though they could seemingly be explained by the false discovery rate combined with multiple hypothesis testing. The authors should clarify how these results can be interpreted in light of the false positive rate of their test and multiple hypothesis testing, and must consider whether more conservative conclusions are warranted in these scenarios.

4. Did non-measurably evolving lineages also contain monoclonal antibodies that bound to vaccine antigens? Is there enrichment of vaccine-binding monoclonal antibodies within measurably evolving lineages?

5. Please modify the abstract in how the following two scenarios are presented: "some lineages enter GCs and thus likely undergo SHM", and "the average SHM over all lineages doesn't increase more than some threshold". These two scenarios are not contradictory and could both be true.

6. Figure 3A is very visually striking, despite the small sample sizes. Could you explain why this figure show a much stronger correlation than Figure S7.

7. p23 l22: why is the divergence from mrca (rather than naive ancestor) the one that we want for these tests?

8. p24 l15: do you have direct evidence for how much of the polytomy prevalence is from PCR/sequencing error?

9. The distribution of p-values should be plotted for all datasets as in Figure S6. It would be instructive to look at them and compare the full distribution given the two choices of significance threshold at 1% and 5%.

Reviewer #1 (Recommendations for the authors):

I have a number of questions about how or why different steps were undertaken, but none of them seem likely to significantly affect the basic conclusions.

– Abstract: I don't think the two findings are contradictory. To my understanding, the first says "some lineages enter GCs and thus likely undergo SHM", whereas the second says "the average SHM over all lineages doesn't increase more than some threshold". Since I think the first doesn't measure what "some" is, and since flu is usually given to non-naive individuals whose responses vary greatly depending on exposure history, and since the threshold could be too small to detect some SHM that occurs, both of these results seem compatible with what I would imagine is most researchers' prior: some lineages undergo SHM in some circumstances. The (in my view quite large) contribution of the current paper is in illuminating what both of the "some"s in the previous sentence mean. I think setting it up as a conflict between two prior results that (unless I'm misunderstanding) aren't actually in conflict just confuses the reader. As it says at p11 l21: "consistent with a primarily GC-independent memory B cell response and/or rarity of antigen-specific lineages in the peripheral blood". I prefer the framing in the first sentence of Discussion: "The extent to which seasonal influenza vaccination stimulates affinity maturation…"

– p2 l10: saying that you "demonstrate measurable evolution" in some cases seems like you care only about false negatives, but not false positives. I prefer the way this is framed at end of intro, as a "survey" with "significant heterogeneity" that conforms to expectations in both directions.

– p3 l10: "at a rate orders of magnitude".

– p3 l14: "and, rarely, re-enter".

– p3 l21: same comment as abstract: not convinced they're in conflict.

– p6 l10: "and a second time after the".

– Figure 2A:

– two categories of HIV here (empty/first 60 weeks) should match those in B (early/late).

– why is hep B not broken into naive/boost here? I assume T=0 is prime, T~1.4 is boost?

– suggest "healthy children" rather than "healthy" so reader can guess whether they expect enrichment for ME.

– Figure 2B: having ~half the y axis devoted to p values and "late hiv" makes it hard to compare everything else. I think main message is e.g. flu is like hep boost, but not hep naive, which i can only really tell by parsing the tiny p values at the top.

– p11 l21: my understanding is that equating "GC-independent" with "no SHM" isn't correct, e.g. this https://pubmed.ncbi.nlm.nih.gov/33326765/ takes as settled that some shm takes place outside the GC. Also, I could be wrong but it would make more sense to me to say something like "only a small fraction of existing flu lineages are restimulated" (which as you say earlier is relatively rare) as the first alternative.

– p14 l1 I would think that "occur at low frequency in the blood" might be better than "are not enriched in the blood", since the latter (to me) sounds like the bottleneck is only on exiting GCs, rather than the other (previous) steps.

– Figure 3A is very striking/convincing (although I guess given the small sample sizes almost worrisome it's so straight?). But could you explain why just by eye it seems so much more striking (stronger correlation) than Figure S7? I realize "min GC %" and "proportion GC B cells" are different, as are "-log P" and "% ME", and one is a scatter plot with low transparency and lots of dots are on top of each other, but 3A looks like almost a perfect relationship, whereas S7 it's hard to even see a linear relationship.

– p17 l19: this paragraph is great, it's really convincing to me.

– p19 l21: couldn't there also be a lot of lineages that are condition-specific and GC-derived, but not re-stimulated by the current stimulus? I don't know a number for the frequency with which re-stimulation causes an antigen-specific lineage to re-enter GCs, but I wouldn't expect it to be very close to 1.

– p21 l1: "to cover as wide a variety of conditions as possible".

– p21 l15: does "redundancy" mean number of observed sequences? Or does it have something to do with the number of nucleotide changes you could make without affecting the AA seq? (I presume the former, i just haven't heard it used in this way). Could use "multiplicity" or "observations" if they would be equivalent.

– p23 l2: what does "manual inspection" consist of? i.e. how do you know by eye that 0.1 is correct for non-bimodal distributions?

– p23 l3: What does "masking" consist of? Does this mean that you're not inferring the D/insert portions of the naive ancestral sequence?

– p23 l22: why is the divergence from mrca (rather than naive ancestor) the one that we want for these tests? Maybe the trunk bit would maybe just cancel out? But then at p26 l6 it looks like for the AA version you do compare to naive/germline seq? From intro to Duchene 2015, it seems they used root (not mrca)?

– p24 l15: do you have direct evidence for how much of the polytomy prevalence is from PCR/sequencing error? For instance do you get fewer polytomies in data with barcodes/UMIs?

– Figure S3: why is it so much easier to detect measurable evolution when we're looking at neutral evolution, i.e. what causes the long downward tails of points in the top right plot (selection strength 1) vs the left plot (neutral)?

– Figure S5: why does it look like there's only a lower bound/quantile (no upper box) for red (Boost, Standard)?

– I would find it very interesting if you could expand on the alternative explanations in the last paragraph of the Discussion. Partly because "does not result from a complete lack of vaccine-induced B cell evolution" seems like a very low bar/unlikely null hypothesis (i don't think many people thought there was zero).

– It might be worth discussing why you don't (I think) attempt to measure selection (it's fine that you didn't). You do an amino acid-based analysis, which is related to this (but doesn't discuss selection strength), and do simulations with both neutral and strong selection, but I'm curious why you focused only on detecting SHM/evolution, and not on whether it was neutral or not.

- It would also be nice to discuss why using parsimony (very heuristic, not very accurate) was preferred over more sophisticated methods.

Reviewer #2 (Recommendations for the authors):

Congratulations on the paper! I enjoyed reading the preprint, and I only have a few comments and suggestions that I list below.

1. For more clarity, the distribution of p-values should be plotted for all datasets as in Figure S6. It would be instructive to look at them and compare the full distribution given the two choices of significance threshold at 1% and 5%. To this end, I think it would make sense to plot the cumulative function.

2. I think the section "Measurably evolving lineages following influenza vaccination show signs of memory B cell origin" could use a more extensive explanation of the multiple testing adjustment. The p-values distributions would also be important here to distinguish the standard randomization test p-values with the BH adjusted p-values. Detecting lineages using the second definition of the p-value should also be tested with synthetic datasets.

3. The initial germline divergence is quantified using the sum of branch lengths for each lineage. I suppose this depends strongly on the lineage size (and that one on the experimental protocol). Is there a way to control for this? (For instance, would it make sense to look at these distributions for subsampled lineages of equal size?)

4. In the discussion you refer to the rates of somatic hypermutation and the length of the GC cycles as given by the literature you cite. For completeness (perhaps as a supplementary figure), could you report the values of the slope fitted in the SHM number vs sample time plot for measurably evolving lineages (as in Figure 1B)? I would be curious to see how these numbers compare with independent estimations from the data and whether their distribution changes significantly between cohorts you've studied.

5. Re discussion on page 11: Even if memory B cells do not re-enter GC, one could imagine detecting the ongoing evolution of naive cells – this possibility should be discussed. Later the results suggest the evolving lineages come mainly from memory cells (page 12) but a priori both scenarios could be true.

6. Figure 1G misses the y axis label and the x axis label is somewhat confusing without reference to the main text. The fractions in boxes should be written with the "%" sign (also in other figures).

7. In Figure 2A the point corresponding to the early-childhood dataset should be distinguishable from other healthy data (I guess it's the "significant" green point).

The caption of Figure 2B should use the term "initial germline divergence" again, as in the y axis label to avoid confusion.

8. Page 5 line 3: before using "SHM/site" first, it would be better to say what it means in words.

Page 5 line 4: In evolving lineages, sequences sampled at later time points are (…).

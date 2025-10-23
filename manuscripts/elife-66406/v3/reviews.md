# Peer review - Round 1

Editors:
- Joseph T Wade, Wadsworth Center, New York State Department of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66406.sa1](https://doi.org/10.7554/eLife.66406.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The Cas12a protein from type V CRISPR-Cas systems can be used for genome editing or modulating gene expression in mammalian cells. One of the advantages of Cas12a over other CRISPR-based systems is the ability to multiplex guide RNAs in a single array. Here, the authors show that processing of RNAs from these arrays can be inhibited by RNA secondary structure, which can be reversed by introducing an artificial sequence, coined the "synSeparator", between guide RNAs. The use of synSeparators increases the activity of Cas12a in mammalian cells, and thus represents an important advance in the development of Cas12a for biotechnology applications.

Decision letter after peer review:

Thank you for submitting your article "Enhanced Cas12a multi-gene regulation using a CRISPR array separator" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Joseph T Wade as the Reviewing Editor and Reviewer #2, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Chase Beisel (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors should test more specific models for how the A/T-rich synSeparators promote crRNA activity, either by analyzing existing data with different separator variants, or experimentally testing more separator/spacer combinations to address specific models. The reviewers recommend focusing on secondary structure in the repeat sequences as a likely source of synSeparator activity.

2. To show that synSeparators are broadly useful for multiplexed Cas12a applications, the authors should test additional targeting crRNA guides, ideally with the design informed by mechanistic insight from Essential Revision #1. The authors should also test crRNAs with synSeparators in another cell line and/or with a different Cas12a protein to further show generalizability.

Reviewer #1 (Recommendations for the authors):

Some additional literature should be integrated into manuscript. Fonfara Nature 2016 showed that Cpf1 encodes a distinct domain responsible for processing the transcribed CRISPR array into individual crRNAs. Liao Nat Commun 2019 showed that the order of the spacer in a CRISPR-Cas12a array can immensely impact multiplexed targeting, where targeting by one crRNA was strongly inhibited due to its repeat pairing with the upstream spacer. McCarty Nat Commun 2020 provided a comprehensive review of multiplexing approaches with CRISPR, including the use of CRISPR arrays.

To support general claims, the authors would need to show that the same trends persist when testing different guide sequences. This would include the selected synthetic separators as well as the natural separator.

The authors also need to integrate the folding of the repeat hairpin, as improper folding likely explains the authors' results more-so than general folding of the upstream guide sequence.

References on line 40 should be replaced with the original demonstration of crRNA processing (Brouns Science 2008) and possibly include the original paper characterizing Cas12a (Zetsche Cell 2015).

Descriptions around processing should consider the fact that the spacer is also trimmed to the 20 – 24 nt guide naturally observed with Cas12a crRNAs (Zetsche Cell 2015).

L. 63 – 64: A more reasonable reason for removal of the separator in the original work was that it was seen as dispensable rather than interfering with targeting activity.

Specify somewhere early in the Results which Cas12a was used (e.g. As, Lb, Fn).

L. 301: The claim of a significant increase needs to be supported statistically. Given the smaller fold-changes and the duplicate measurements, many of these increases may not be statistically significant.

Reviewer #2 (Recommendations for the authors):

1. The data in Figure 1 correlate predicted secondary structure with crRNA activity. However, this relationship can be tested more directly. I would like to see targeted substitutions in the separator that are predicted to lead to specific changes in secondary structure at key positions around the Cas12a cleavage site.

2. The authors speculate that the separator sequences affect Cas12a processing of the crRNAs, but they rely on indirect readouts of crRNA processing. It would be informative to measure processed crRNA levels directly, especially for the experiment shown in Figure 4. crRNA processing could also be assayed in vitro using purified Cas12a.

3. The data in Figure 4 show a modest effect of introducing a short, A/T-rich separator in the CRISPR array. I think even a small improvement in crRNA activity would be an important advance, so the magnitude of the effect is not a concern. However, I would like to see more than one CRISPR array tested, and it would be informative to individually replace A/T-rich separators with G/C-rich separators. Also, does the spacer order matter? Spacer order could also affect RNA secondary structure.

Reviewer #3 (Recommendations for the authors):

1. This is not needed for the current manuscript, but in future experimentation the authors could consider performing comparative small RNA-seq to validate crRNA array processing in presence/absence of the synSeparator.

2. In Figure 4B, the black arrows could be confusing to readers. Consider showing only the green values or more explicitly stating what the black arrows denote.

3. In line 33-36, The word "coding sequence" is not appropriate. The word should be replaced with regulatory element or something similar.

4."permissive" (line 153) should be changed to "permissive".

5. Although authors have mentioned both VPR and mini-VPR (line 530), none of Results section/figures have included VPR. Was full-length VPR used?

6. In Line 202 – legend of Figure 2 there are some extra brackets around "Figure S2A".

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Enhanced Cas12a multi-gene regulation using a CRISPR array separator" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The Reviewing Editor has read through your revised manuscript and response letter. We appreciate the impressive effort you have made to respond to the comments from the previous round of review. In principle, the paper is now suitable for publication in eLife, pending a response to a few small comments ; these comments should all be addressable with changes to the text. The most important issue relates to Figure 4. The new in vitro assay is a nice addition since it suggests the effects of RNA secondary structure are directly on Cas12a. However, I am a little confused by the data presentation in Figure 4, and I think you may be overstating the magnitude of the difference in cleavage between RNAs with/without a SynSeparator. There is clearly an improvement from adding the SynSeparator, which alone is sufficient reason to include these new data. However, you should either more clearly explain/present the data, or soften your conclusions. See comment #3 below for more details.

Specific comments:

1. Lines 578-585 (Discussion). This paragraph doesn't relate to anything in the current study, so I recommend removing it.

2. The Discussion covers a lot of ground. I recommend adding section titles to improve the readability.

3. Figure 4E summarizes the data for the in vitro cleavage assay. However, to my eye at least, the data in panels B and C, and the data in the associated supplementary figure, don't match panel E. Specifically, without the SynSeparator, the largest increase in cleavage (shown in Figure 4E) occurs between 30 and 60 minutes. However, in panel B, there is almost no difference in the abundance of the 41/42 nt products between 30 and 60 minutes. Moreover, the kinetics of cleavage for the RNA without a SynSeparator are clearly delayed relative to the RNA with a SynSeparator, but cleavage appears to saturate after ~30 minutes (see also panels E and F of the supplementary figure, which to my eye are almost identical). Figure 4E suggests that only 20% of possible cleavage has occurred after 60 minutes for the RNA without a SynSeparator. If that is the case, why is it that cleavage appears to have saturated after 30 minutes? The authors need to present and describe these data more clearly, and potentially soften their conclusions.

4. The authors should use more precise language when describing changes in predicted secondary structure, making clear that these are predictions. For example, rather than saying "as these secondary structures grew tighter, CRISPRa performance gradually worsened", I suggest "as the predicted extent of base-pairing increased, CRISPRa performance gradually worsened".

5. Line 42. This is the one place where I would stick with "crRNA" rather than "gRNA". Perhaps you could mention in parentheses that the RNAs are commonly called crRNAs when expressed from their native loci.

6. Line 42. I suggest "prokaryotic" rather than "bacterial".

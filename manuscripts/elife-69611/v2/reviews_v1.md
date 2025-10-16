# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69611.sa0](https://doi.org/10.7554/eLife.69611.sa0)

This important study advances our understanding of how upstream reading frames contribute to gene expression regulation. Using innovative tools, the authors provide convincing evidence connecting the features of these sequences to protein expression. The results will be of broad interest to investigators in the field of gene expression regulation and its evolution.


---

# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69611.sa1](https://doi.org/10.7554/eLife.69611.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Unraveling the influences of sequence and position on yeast uORF activity using massively parallel reporter systems and machine learning" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The essential revisions are outlined in the referees' reports and summarized here:

(1) Estimate the extent to which the effects measured are independent of the reporter used.

(2) Strengthen the analysis of evolution of uORFs between S. cerevisiae and S. paradoxus, for instance by testing their interpretations.

(3) Show that the reporter mRNA initiates at the predicted TSS.

(4) Demonstrate experimentally that the distance from the cap causes the effects revealed from the statistical analyses.

Reviewer #1 (Recommendations for the authors):

This is a very impressive set of experiments and a timely paper.

I have two main comments. One is already explained in the public review and regards the potential dependency of the effects measured on the main ORF. I think this could be discussed but it could be also rather simple to test a subset of uORFs across the range of effects, from strongly repressive to strongly enhancing, and use a different reporter sequence to show that at least the ranking or sign of effects is preserved. Could be done by swapping mCherry and YFP for instance in the plasmid.

This is probably because of my background but I found the section on evolution really interesting and broadening the scope of the paper quite a lot. I wonder if the authors could not push further their analysis for instance by analyzing the polymorphism data available for 100s of strains in S. cerevisiae, for instance by looking at the frequency spectrum of mutations that would enhance the repressive effects of uORFs. Mutational bias could also be considered. With this part, it would also be interesting to know whether there are interactions between uORFs and the main ORFs because changes in magnitude or even signs of uORFs effects could be compensated by other regulatory changes, in a coevolution akin to what the same authors have reported on before regarding transcription and translation.

Reviewer #2 (Recommendations for the authors):

– They have not verified that a random sampling of reporter mRNAs generally have 5' ends corresponding to those predicted by using the ENO2 promoter in their library design. This is important because the position of uORFs from the 5' end is claimed to be an important determinant of uORF function, and represents one of the most novel findings of the study.

– They have not tested their conclusions about the importance of distance of the uORF from the mRNA cap on uORF function by follow-up experiments on a few individual repressive uORFs to examine whether increasing the distance of the uORF ATG from the cap by insertion of unstructured sequences (eg. CAA repeats) reduces inhibition by the uORF; or whether deleting sequences to move a uORF closer to the 5' end increases its inhibitory effect. This is important because the conclusion is based only on correlation analysis and hence could be influenced by other features of the mRNA that vary in parallel with distance of the uORF from the cap.

– Regarding the distance from the cap effect, it seems possible that repression by an uORF would be diminished by a location further downstream from the cap owing to inclusion of other AUG or near-cognate start sites located upstream of the uORF, which would reduce translation initiation at the uORF of interest. This possibility should be addressed bioinformatically, and also by examining individual reporters in which all AUG or near-cognate triplets are removed upstream of the uORF in question to determine if this increases repression by the uORF without changing its position relative to the cap.

– A point of major confusion: Most of the plots and supplementary tables list the reporter expression ratios as log2(AAG/WT); however, I believe that this incorrect and the log2(WT/AAG) ratios have been plotted instead, as the values for the majority of uORFs, which are repressive, are <0.

­– p. 13: The sentence: "In general, repressor uORFs were less repressive in the upf1∆ strain, including 92% of AUG-uORFs and 59% of non-AUG uORFs." requires statistical analysis to bolster the claims, particularly for the small subset of repressive non-AUG uORFs

– p.14: The sentence "Consistent with this, we found median %NMD was higher for uORFs terminating with UGA (37.5%) than those terminating with UAA (35.3%) or UAG (33.2%) (Figure 3D)." is not justified, as the median values for the three stop codons in Figure 3D do not appear to differ significantly. Moreover, assuming it was valid, is there any way to rationalize it based on known termination efficiencies at the three stop codons?

– Regarding the claim on p. 14 that "Unexpectedly, the location of the stop codon relative to the transcript leader cap was positively correlated with the %NMD, such that uORFs that terminate further from the cap were more likely to induce NMD than those that terminate adjacent to the cap (Figure 3F; R^2 = 0.065; P = 7.44x10^-8)", it should be noted that this is a very weak trend that explains only ~7% of the variance in %NMD values. As such, the sentence in the Discussion "We found the opposite relationship among uORF stop codons, such that stop codons were less likely to induce decay the closer they were located to the 5' cap" appears to be an overstatement. Also, isn't it possible that the trend can be explained as originating from uORF length effects shown in panel F, as longer uORFs will have greater cap to stop codon separations? (Note also that panels F and G were incorrectly cited in text.)

– pp. 16-17 and Figure 4D: The description of the parameters included in the ENR model is wholly inadequate. How was Kozak context quantified and for what sequence interval around the AUG? How was uORF Start and Stop and CDS sequence conservation quantified (and for what species)? What sequence interval around the uORF Start was employed to calculate the deltaG folding energies, and how were the calculations made? How far downstream was %AU calculated. In general sufficient information has to provided in the legends or Methods to allow the analysis to be repeated in full by other workers. A related comment is that the authors cite no literature to justify their analyses of these different parameters which they seem to pull out of the hat, eg. why Pro and Gly codons?

– p.19 and Figure 5A: the claim that "In general, uORFs were more repressive when they were closer to the TSS" is not convincing, as many uORFs shown in blue in Figure 5A show the opposite trend; and there are only a few outliers that conform to the stated trend. No statistical analysis of the trend was provided. As such, it is an overinterpretation of the data to claim that these results independently support the importance of uORF distance from the TSS, indicated by the ENR analysis. It also seems important to provide the YFP expression for the different leaders with WT and mutant uORFs, rather than just the WT/AGG ratios, in order to evaluate whether there are other sequences besides uORFs in the longer 5'UTRs that are affecting expression. This information should be added to Figure 5B in particular.

– p.20-21" Regarding the text: "For example, an S. cerevisiae oORF in SEC1 was 1.5 to 2-times more repressive than its S. paradoxus homolog, potentially owing to a deletion in S. paradoxus that results in an earlier stop codon that shortens the oORF. In another case, an S. paradoxus oORF in the AIM22 leader was approximately four-fold more repressive than its S. cerevisiae homolog, possibly due to the presence of more adenosines in its Kozak sequence." The words "potentially" and "possibly" in these sentences presumably reflect the fact that there are other sequence differences in the 5'UTRs between the two species that contribute to the differences in uORF function. These interpretations should be tested by mutational analysis of the reporters for these genes to determine whether shortening the oORF in S.c. SEC1 and improving the Kozak context of the S.c AIM22 oORF are sufficient to confer the altered repressive functions of the orthologous oORFs in S.p.

–

Figure 6D and related text: It is not convincing that conserved uORFs have a statistically significant poorer AUG context compared to nonconserved uORFs, even if one focuses (as they do) on only the -3 position rather than calculating the context score for the entire sequence interval surrounding the AUG. This is being overinterpreted.

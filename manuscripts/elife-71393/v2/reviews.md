# Peer review - Round 1

Editors:
- Sarel Jacob Fleishman, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71393.sa1](https://doi.org/10.7554/eLife.71393.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

CR6261 and CR9114 are two antibodies that bind to the conserved stem of influenza hemagglutinin (HA) through their VH regions and differ by 14-18 mutations from their inferred germline sequences. The authors constructed large combinatorial libraries containing combinations of 11 and 16 mutations for CR6261 and CR9114, respectively. These were used in yeast surface display titrations to infer individual and epistatic contributions to binding diverse HAs and to infer possible evolutionary trajectories going from germline to the mature antibodies. The study provides a wealth of knowledge on amino acid contributions to binding affinity. The study informs our understanding of biochemical epistasis, and could potentially serve as a starting point for a more detailed understanding of antibody affinity maturation more generally.

Decision letter after peer review:

Thank you for submitting your article "Binding affinity landscapes constrain the evolution of broadly neutralizing anti-influenza antibodies" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Satyajit Rath as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jesse D Bloom (Reviewer #2); Nicholas C Wu (Reviewer #4).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Following are a number of factors that may confound or limit the interpretation of the results. The authors should mention these factors and the limits they place on the analysis of evolutionary paths during antibody selection. They should also tone down the language regarding the relevance to vaccine design.

– Unlike other studies where antibodies were isolated from single-cell sorting of memory B-cells, the present bNAbs were isolated from phage display libraries. These libraries (Throsby et al., 2008; Dreyfus et al., 2012) were constructed from pooled IgM+ from 10 (not 3 as incorrectly stated in manuscript) (CR6261) or 3 (CR9114) healthy donors and scFv fragments were cloned and screened using phage display against H5HA for CR6261 (Throsby et al., 2008) and against sequential panning against Has from H1, H3 and both B lineages for CR9114 (Dreyfus et al., 2012) respectively. Use of phage display methodology which involves multiple rounds of PCR as well as panning means that mutations can be introduced during library construction. Hence the resulting sequences isolated need not accurately reflect antibody gene sequences present in the donors. Further, the multi-round panning process with diverse HAs (especially for CR9114) biases the resulting sequences selected, altering the order of the panning steps might result in a different selected sequence.

– Additionally, it is unclear what the natural selection pressures are. It is likely that they would be for increased neutralization breadth and potency which is not straightforwardly related to improved breadth of binding to soluble HA where the stem accessibility is much higher than it is in the viral context.

– The known polyreactivity of many bNAbs including stem-directed bNAbs (PMID: 33049994) is another confounding factor.

– Unlike studies with bNAbs isolated from elite neutralizers in the case of HIV-1, there is no evidence that the individuals from whom the pooled phage libaries were made had significant breadth of serum neutralizing activity and so it remains possible that the breadth of the final isolated antibodies arose from mutations introduced during the PCR amplifications and enriched through the panning steps.

2. CR6261 was selected by panning against H5 HA whereas the vaccinated individuals presumably primarily had experienced H1. Since the antibody binds to the conserved stem of HA what is relevant to interpret the mutational landscapes is not the overall antigenic diversity of HA (Figure 1B) but the diversity of the stem epitopic region. If these regions are similar in H1 and H9 HA that would explain the observation that multiple mutations in the antibody are tolerated in both cases. In the case of CR9114, the mature antibody binds best to H1, less well to H3 and weakest to B HA. Unsurprisingly the same pattern is reflected in the mutational data. Given the greater diversity in HA stem epitope sequence between H1, H3 and B relative to that between H1 and H9 it is also unsurprising that there should be the sequential acquisition of breadth in the latter CR9114 case (see also 1 above).

3. In lines 69-70, "bnAbs tend to have many more mutations than specific antibodies". This statement is mostly true for HIV bnAbs but not for influenza bnAbs. As described by Lingwood et al., (PMID: 22932267), "Influenza IGHV1-69-based broadly neutralizing antibodies undergo a relatively low degree of somatic mutation (an average of 14 amino acids in the heavy chain, n = 9)". In fact, many influenza antibodies have similar number of somatic mutations as CR9114 and CR6261 (PMID: 30795982).

4. It is surprising to see significant second-order effects at relatively large distances (Figure 2F). What is the suggested explanation?

5. It is never clearly stated in results whether it's single chain (scFv) antibody, and if the HA is trimeric. If so, is there a potential for avidity so that the measurements are Kd,apparent for the multivalent interaction rather than monomeric Kd?

Other comments:

In both the abstract and beginning of results, it would be helpful to describe the libraries a bit more clearly: all combinations of mutations separating the germline and mature antibody in the VH domain among sites contacting the epitope.

Avnir et al., PLoS Pathog 2014 (PMID: 24788925) has analyzed the somatic mutation pattern in IGHV1-69 influenza bnAbs. The authors should cite Avnir et al., to further substantiate the findings in this study. For example, Arnir et al., identified several commonly occurring somatic mutations in IGHV1-69 influenza bnAbs, including T29P, S35R, and S83F (i.e. T28P, S30R, S74F, respectively, in Kabat numbering), which have strong additive effect in CR6261 (Figure 2B).

Since evolution proceeds through single-nucleotide rather than amino acid exchanges, the germline and mature antibody nucleotide sequences should be presented (if known). The authors may consider adding a comment that evolution may not move directly through amino acid exchanges if the DNA sequence does not permit such a change through a single-nucleotide mutation.

I personally was very curious how the specific epistasis models the authors used compare to global epistasis models. This is well explained in the appendix, but might be helpful to mention in another sentence or two in main text as well.

In the non-global-epistasis model, is anything done to handle the censoring of the data at the high and low end of the affinity scale? I was confused by this because line 115 says values outside the range are pinned to the boundaries, but then in Appendix (line 1282) it seems to suggest censoring isn't an issue.

The interactive browser is cool! Would be nice if mutations were either labeled by the amino acids, or there was clearer explanation which amino acid identity is 0 and which is 1 for the violin plots. Also, might be worth adding text explaining the browser is only available for CR9114.

Line 41: I think there are actually now a lot of broadly neutralizing antibodies, so I'm not sure how accurate "a handful" is here.

Line 70: "less broad" might be better than "specific" because even bNAbs are specific (for flu HA for instance) rather than "sticky" to everything.

I had a hard time understanding the numbers in Figure 1A.

I found Figure 1G confusing, mostly because I didn't (and still don't) really understand all the boxes with solid and dotted black lines labeled with various HAs.

Line 288-289: I think we can be virtually certain that the person wasn't infected with H9 since it's not a human virus subtype.

It would be useful to list the surface area each residue in the paratope for both antibodies contributes to binding where such information is available.

Is it possible to convert the effect scores into a free energy of binding contribution? Are there error estimates for the effect scores that would allow one to assess whether apparent differences in effect scores are statistically significant?

Larger epistatic effect scores occur between residues with the largest contributions to binding. Is this expected?

The authors may consider changing "CR-9114" and "CR-6261" to "CR9114" and "CR6261", respectively, which are the more commonly used nomenclatures for these two antibodies in the field.

It is unclear to me which antibody numbering scheme (e.g. Kabat, Chothia, IMGT) is being used for numbering amino acid residues in this study. Also, naming a position as "112.1" in CR6261 seems a bit odd. Should that be "112a"?

In panel B of Figure 1—figure supplement 5, the correlation between Tite-Seq mean expression and isogenic expression fluorescence is quite high for CR9114 variants but low for CR6261 variants. Is there a reason for that discrepancy?

In lines 224-225, "In contrast, a specific set of many mutations with strong synergistic interactions is required to bind H3, and to an even greater extent, influenza B". It is not very clear to me which analysis supports this claim. Can the authors clarify a bit?

In caption of Figure 5, while the meaning of "R" is described (random mixed scenario), the meaning of "O" and "A" should also be explained.

Among the somatic mutations in CR9114, I57S, K82I, and S83F are particularly important for binding to H3 (lines 182-183 and Figure 2D). Can the author provide a plausible structural explanation?

Similar to the comment above, it is interesting to see that T29P almost exclusively occurs as the first mutation under various selection scenarios (Figure 5J and Figure 5—figure supplement 3C-D). Can the author provide a plausible structural explanation?

Reviewer #1 Recommendations for the authors:

The interactive browser is cool! It would be nice if mutations were either labeled by the amino acids, or if there was a clearer explanation which amino acid identity is 0 and which is 1 for the violin plots. Also, might be worth adding text explaining the browser is only available for CR9114.

Line 41: I think there are actually now a lot of broadly neutralizing antibodies, so I'm not sure how accurate "a handful" is here.

Line 70: "less broad" might be better than "specific" because even bNAbs are specific (for flu HA for instance) rather than "sticky" to everything.

I had a hard time understanding the numbers in Figure 1A.

I found Figure 1G confusing, mostly because I didn't (and still don't) really understand all the boxes with solid and dotted black lines labeled with various HAs.

Line 288-289: I think we can be virtually certain that the person wasn't infected with H9 since it's not a human virus subtype.

Reviewer #4 Recommendations for the authors:

1. The authors may consider changing "CR-9114" and "CR-6261" to "CR9114" and "CR6261", respectively, which are the more commonly used nomenclatures for these two antibodies in the field.

2. It is unclear to me which antibody numbering scheme (e.g. Kabat, Chothia, IMGT) is being used for numbering amino acid residues in this study. Also, naming a position as "112.1" in CR6261 seems a bit odd. Should that be "112a"?

3. In lines 69-70, "bnAbs tend to have many more mutations than specific antibodies". This statement is mostly true for HIV bnAbs but not for influenza bnAbs. As described by Lingwood et al., (PMID: 22932267), "Influenza IGHV1-69-based broadly neutralizing antibodies undergo a relatively low degree of somatic mutation (an average of 14 amino acids in the heavy chain, n = 9)". In fact, many influenza antibodies have similar number of somatic mutations as CR9114 and CR6261 (PMID: 30795982).

4. In panel B of Figure 1—figure supplement 5, the correlation between Tite-Seq mean expression and isogenic expression fluorescence is quite high for CR9114 variants but low for CR6261 variants. Is there a reason for that discrepancy?

5. In lines 224-225, "In contrast, a specific set of many mutations with strong synergistic interactions is required to bind H3, and to an even greater extent, influenza B". It is not very clear to me which analysis supports this claim. Can the authors clarify a bit?

6. In caption of Figure 5, while the meaning of "R" is described (random mixed scenario), the meaning of "O" and "A" should also be explained.

7. Among the somatic mutations in CR9114, I57S, K82I, and S83F are particularly important for binding to H3 (lines 182-183 and Figure 2D). Can the author provide a plausible structural explanation?

8. Similar to the comment above, it is interesting to see that T29P almost exclusively occurs as the first mutation under various selection scenarios (Figure 5J and Figure 5—figure supplement 3C-D). Can the author provide a plausible structural explanation?

9. Avnir et al., PLoS Pathog 2014 (PMID: 24788925) has analyzed the somatic mutation pattern in IGHV1-69 influenza bnAbs. The authors should cite Avnir et al., to further substantiate the findings in this study. For example, Arnir et al., identified several commonly occurring somatic mutations in IGHV1-69 influenza bnAbs, including T29P, S35R, and S83F (i.e. T28P, S30R, S74F, respectively, in Kabat numbering), which have strong additive effect in CR6261 (Figure 2B).

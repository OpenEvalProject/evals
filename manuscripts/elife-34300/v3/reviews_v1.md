# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34300.028](https://doi.org/10.7554/eLife.34300.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Inferring amino acid interactions underlying protein function" for consideration by eLife. Your article has been reviewed by three peer reviewers, evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nir Ben-Tal (Reviewer #1); Amnon Horovitz (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript presents deep sequencing study of the ligand-binding helix of 5 homologous PDZ domains. The data is analyzed, using double-mutant thermodynamics couplings, to estimate energetic couplings between the 9 amino acid positions of the helix. The results are correlated with calculated evolutionary couplings using both the SCA method, developed by the authors, and the DCA method used to infer direct couplings. The conclusion is that while DCA detects direct couplings, useful within the context of structure prediction, SCA appears to detect 'functional', allosteric couplings.

Opinion:

Assuming that it was done well, the deep sequencing data itself, regardless of the analysis and interpretations, can be very handy and useful for other studies. Its interpretation using the double-mutant cycle is insightful (but raises several open questions), and the comparison to the evolutionary couplings is questionable.

Essential revisions:

The energetic couplings:

1) A single Gaussian appears to fit well to many (perhaps most) of the energetic couplings in Figure 2, but the description in the main text (subsection “A deep coupling scan in the PDZ family”, second paragraph) refers to double-Gaussian. The energetic couplings of the rest of the PDZ domains (S3-S6) has even fewer double-Gaussians. Thus, the description is confusing.

2) The proposed explanation for the double-Gaussian are two conformations, which is surprising for a helix. Which conformations would these be? The model in S8 is too abstract and does not explain.

3) The analysis considers all the mutation types to be equal but that's not the case. Mutations to glycine or proline, for example, are more likely to disrupt the helix structure whereas mutations to alanine are more likely to be non-disruptive. Given that a helix was studied here, special consideration should be given to helix disrupting mutations. Some re-analysis according to mutation types and discussion of this issue is needed. Perhaps, the bimodal distributions (double-Gaussians) are due to mutation types?

4) Given that this study focuses on an α-helix, certain couplings (both energetic and evolutionary) such as between i,i+3,4 are expected. These couplings may have little to do with the PDZ fold and simply reflect helix properties and solvent exposure. A previous analysis of correlated mutations in the helices of many unrelated proteins did indeed reveal enrichment at positions i,i+3,4 (Noivirt et al. PEDS 2005). Such couplings are detected essentially only along one face of the helix. On the one hand we wonder why it is missing in others. On the other hand, the observed coupling should be discussed in view of this anticipation. That is, maybe the 1-4 and 1-5 couplings (Figure 2) simply reflect an α-helix.

5) What is the mechanics of energy transduction between the amino acids? Which forces are involved? This is particularly interesting for amino acids that are not in direct contact with each other.

6) The mechanistic and biological implications of the couplings should be discussed further. Why is allostery needed in PDZ domains? Why is it not completely shared by all 5 homologues? How does the specific coupling observed for each homologue serve its unique function?

7) Why limiting the analysis to a single helix? It would have been much more insightful to cover the whole domain. Especially given that it's so small.

8) The deep sequencing data should be made publicly available and easily accessible.

Coevolution:

9) We have some concern about the correlations in Figure 5. To what extent are the differences meaningful given that most of the data points are clustered together and the differences between plots appear to be due to a few outliers?

10) With so many homologous sequences, it should be possible to examine the robustness of the results using k-fold tests. For example, how does evolutionary coupling computed using (randomly chosen) half of the taxa compare to the values obtained with the other half? And how do the couplings in each set correlate with the energetic couplings?

11) Regarding the previous point, it would be insightful to examine the robustness of the two methods used to estimate coevolution. Both DCA, used to detect direct couplings, and SCA, used to suggest 'functional couplings'. Hopefully both will be equally robust in k-fold tests.

12) "Extracting the coevolution pattern in the top eigenmode for just the α2 helix (Figure 5C), we find that coevolution as defined by SCA in fact nearly quantitatively recapitulates the homolog averaged experimental couplings collected here (𝑟2 = 0.82, 𝑝 = 10;<= by F-test, Figure 5D)." r2 = 0.82 is fair correlation at most. This sentence should be tuned down considerably.

13) The statement in the sentence before the Discussion that non-contact couplings in the DCA model represent noise is at odds with Anishchenko et al., 2017. This discrepancy requires some discussion.

14) When comparing the two coevolution methods the authors should make the most of each. For some reason they use a very small alignment in DCA. About one tenth of all possible sequences.

15) DCA (and a full evolutionary study) takes into account both direct and indirect couplings between all residues. SCA on the other hand, takes into account only couplings between amino acid pairs. Thus, the energetic couplings work, via the double-mutant cycle, is more similar in spirit to SCA. The authors should refer to this point when correlating the two evolutionary coupling methods to the energetic coupling analysis.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Coevolution-based inference of amino acid interactions underlying protein function" for further consideration at eLife. Your revised article has been favorably evaluated by Detlef Weigel (Senior Editor), a Reviewing Editor, and outside reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

This paper is important in two regards. First, it describes a high-throughput approach to mutant cycle analyses. Second, it shows the relative strengths and weaknesses of DCA and SCA. Nevertheless, there still are some concerns after the revision. The main one is that the equation in Figure 4 seems wrong. This may be a typo but if not, then the analysis in the paper based on this equation is also wrong. The correct form should be:

Kxapp = Kx(1+Kc*α)/(1 + Kc)

Other comments:

1) Averaging over mutation types is better than some arbitrary choice but, under favorable circumstances, mutations to alanine are preferred as a reference because with this substitution interactions are mostly removed without new ones being introduced.

2) In previous work (Cell 2009), the authors attributed the top eigenmode to evolutionary noise but not in this paper. This needs explaining.

3) We still think that the coincidence of the pattern of couplings observed in this paper with i, i+3,4 periodicity in helices suggests that maybe they reflect secondary structure and not allostery.

4) It should be noted that correlated mutations between distant residues can also reflect negative design (Noivirt PLoS Comp. Biol. 2009).

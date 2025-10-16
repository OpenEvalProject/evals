# Peer review - Round 1

Editors:
- Joseph T Wade, Wadsworth Center, New York State Department of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54655.sa1](https://doi.org/10.7554/eLife.54655.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study uses a genome-scale approach, CLASH, to identify many RNA-RNA interactions in Escherichia coli. The interacting RNA pairs identified in this work represent a valuable resource for groups studying RNA-based regulation in bacteria. Moreover, the data reveal many interacting pairs of small, regulatory RNAs (sRNAs), suggesting complex regulatory cross-talk among sRNAs.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Hfq CLASH uncovers sRNA-target interaction networks involved in adaptation to nutrient availability" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ben F Luisi (Reviewer #2).

Our decision has been reached after consultation between the reviewers and the Reviewing Editor. Based on these discussions and the individual reviews below, we regret to inform you that your work cannot be considered further for publication in eLife.

While the reviewers are enthusiastic about the potential of the resource that the CLASH data represent, concerns were raised about the validation of these data. Additionally, the reviewers felt that the follow-up studies are interesting, but that some of the conclusions need to be softened. With additional validation of the CLASH data, the manuscript would likely be suitable for publication in eLife, without the need for much in the way of new experimental data. Nonetheless, the required analyses will likely take some time. We encourage you to resubmit if you can make a more compelling case that the CLASH data represent physiological RNA-RNA interactions.

The major concern is that there is currently insufficient evidence to conclude that the RNA-RNA pairs identified by CLASH represent bona fide RNA-RNA pairs inside cells. Many of the reported RNA-RNA pairs appear to have been identified only once, and many include highly abundant RNAs (i.e. tRNA, rRNA). Moreover, overlap with RIL-seq data is fairly limited. While the discussion clearly lays out why overlap with RIL-seq data might be low, this also raises the bar for validating the RNA-RNA pairs not found by RIL-seq. It should be possible to use bioinformatic analyses to further test whether the novel RNA-RNA pairs are genuine. For example, are novel sRNA targets enriched for sequences complementary to the sRNA seeds? Are known sRNA-regulated genes enriched for sRNA-mRNA pairs, and vice versa? These analyses are most important for the novel RNA-RNA pairs identified by CLASH (i.e. not found by RIL-seq).

Reviewer #1:

Overall, this is very interesting work, and the manuscript obviously represents a great deal of effort. My major criticisms of the work are two-fold. First, the manuscript seems very diffuse – touching on too many topics at a rather surface level. Second, the biological implications of the experimental results are overstated. I hope my comments will be useful to the authors as they consider how to revise their manuscript.

1) The title of the manuscript is misleading. The main functional characterization of MdoR and its targets is intriguing and hints at a physiological function related to carbon source adaptation, but there is a long way to go to say that this is truly the function of this sRNA.

2) ArcZ-CyaR experiment in the middle is not well connected to the rest of the manuscript. The inclusion in the model figure doesn't really help shed light on the biological role for this interaction.

3) Subsection “Hfq CLASH predicts sRNA-sRNA interactions as a widespread layer of post transcriptional regulation”, third paragraph. Figure 5D, the wild-type ArcZ still affects mutant CyaR levels. The authors provide a hand-waving explanation that could be tested. Moreover, the authors state that ArcZ promotes CyaR degradation, but there is no direct evidence for this. It could be tested. Not sure it's the highest priority for this manuscript, given that this experiment in general is not well integrated. But at least the authors should modulate their statement to reflect the actual data.

4) Abstract – there is no direct evidence that MdoR enhances maltose uptake.

5) I did not understand the logic behind the analyses in Figure 2. The authors state that it was "logical to assume that changes in Hfq binding would also be reflected in changes in sRNA steady state levels." However, there are numerous studies showing that different sRNAs bind Hfq via different modes, and that there is a great deal of variability regarding the role of Hfq in stabilizing sRNAs. Moreover, the competition among RNAs for binding to a limiting pool of Hfq will certainly change over time, and be influenced by the total sRNA abundance and any given sRNA's proportion of the total RNA pool. There seems to be no overall conclusion from the figure, and no follow up, so I would recommend deleting it.

6) Subsection “MdoR directly regulates the expression of major outer membrane porins and represses the envelope stress response pathway”, fourth paragraph: The authors state hypotheses in this section that are not further tested, and are not supported by data shown. These are more appropriate for modest speculation in the Discussion.

7) Figure 7F: Is the effect of MdoR SM on MicA significant?

8) The only MdoR-target interaction that was definitively demonstrated was MdoR-ompC, and indeed, the authors went above and beyond with evidence here. It is interesting that ompC levels are reduced in maltose (Figure 8B), but this is clearly NOT MdoR-dependent (Figure 8D). The differences in MicA and lamB RNA levels in the mdoR mutant grown in maltose are intriguing, but these effects can't be linked to a specific MdoR-target regulation. Minimally, the authors should try to make the link between molecular interaction of MdoR and a target (rpoE?) and the differences in MicA/lamB more clear.

9) Subsection “MdoR enhances maltoporin expression during maltose fermentation”, last paragraph: It would be very exciting if the data directly supported this statement. However, the experiments presented fall short. More physiological evidence is needed – growth phenotypes, maltose uptake assays, etc. In the absence of these, the authors must tone down their claims.

10) Because there is so little investigation of the physiology, the discussion of the physiological relevance of these findings is very superficial. The transition from exponential to stationary phase growth has been studied in E. coli growing in LB. What becomes limiting? The authors say very generically "the most favorable nutrients" become limiting. The finding that malEFG and MdoR are specifically expressed during a very narrow window of time in LB grown cells is very interesting. There must be more to the story of their regulation than malT-dependent maltose-inducible expression given this expression pattern in LB given that the main carbon source in LB is peptides/amino acids. The authors should work on improving the quality of the discussion of these issues, and be up front about the limitations of their study in this regard.

11) One key issue that should be addressed in the Discussion is the fact that these global approaches have so little overlap. I did appreciate the thorough description of the relative advantages provided by the Hfq-CLASH method as compared to RIL-seq. However, I think the field as a whole needs to find a way to discern direct, physiologically-relevant interactions from those that may be transient, weaker, and stochastic. I don't expect the authors to solve this issue, but it should be acknowledged. The sensitivity and accuracy of various methods needs a thorough investigation. At least, the authors could consider their Hfq-CLASH results in light of their total expression profiles (RNA-seq) of well characterized sRNAs and their regulons. What's the false negative rate for known interactions?

Reviewer #2:

This manuscript analyses the RNAs associated with the RNA chaperone Hfq in Escherchia coli at different growth stages, and in particular during the transition between stages. There has been other work published in this topic, but the new aspect of the work presented here is the depth of analysis of the transitions and the in depth characterisation of the associated RNAs. One important finding from this study is that sRNA expression does not correlate strongly with Hfq binding profile – suggesting that there must be context dependent binding of the RNA to Hfq. Another is the model for the regulatory network involving the processed transcript from the mal operon. The experimental work is extensive and there are many interesting new findings reported. There are several comments listed below that will hopefully be useful for the authors to consider:

1) Hfq for CLASH has two large tags on C-terminus. As the C-terminus has been proposed to participate in RNA/protein partners binding and Hfq autoinhibition (work from the Woodson group), have the authors done any controls to make sure this does not interfere with RNA banding/introduce false results?

2) "Hfq binds to sRNA-target RNA duplexes" – are RNA duplexes the only Hfq targets? For example, sRNAs were shown to cycle on Hfq, therefore one can imagine a situation in which one sRNA is not fully displaced and the second one already bound. Could some of the sRNA hybrids represent such state?

3) 'tRNA-tRNA and rRNA-rRNA chimeras originating from different coding regions were removed' why?

4) Can the authors please comment on other chimeras isolated, others than sRNA-mRNA and mRNA-mRNA? Would these represent Hfq targets in the cell?

5) Figure 3 – it is not clear what the enriched motifs are showing, 5' end of the chimera? 5' end of both RNAs in the chimera? Only mRNAs?

6) Explain in more detail what is meant by scrambled RNA.

7) Figure 4 – as only mutations in ArcZ cause disruption of the regulation, can it be an indirect effect, not the result of direct sRNA-sRNA regulation?

8) Figure 5B – It is difficult to see expression of ygaM (or YgaN, which the blot may be showing). Where is MdoR on the blot? If it is labelled malG it is somewhat confusing, as the blot presumably shows the sRNA fragments, not the whole mRNAs?

9) The signal for RyhB on Figure 5B is quite strong for OD 1.2 and 1.8, however on Figure 6C it is very weak. Can the authors explain? MdoR intensities seem to match, so presumably the RNAs quantities used are similar?

10) Is there an evidence that RyhB is in the cell as 5'PPP RNA? Perhaps it is not processed, but has the possibility of it harbouring a different 5' end has been excluded?

11) Figure 7C – It is confusing that the authors label 5' and 3' ends which are not real ends, and are different for each panel for MdoR. Could they mark, e.g. with dots, that these are not real ends of RNAs? Or indicate positions of the nucleotides shown? It would make analysing the results much easier.

12) Figure 7D- If an empty plasmid is used as a control and the blot probed for MdoR, can the authors explain what is being expressed in their control after 20 minutes? There may be a typo in the legend as it states that the samples were harvested 15 minutes after induction, but the blot shows the results for 20. What is the meaning of the red rectangle over the 15 minutes into MdoR expression?

13) Figure 7F – explain MdoR SM, it also isn't introduced in the text. Why does the seed mutation cause higher target levels? For RyeA it doesn't seem like the seed mutation has abolished regulation. Is RybB regulating MicA as well?

14) Have the authors tested how their substantial MdoR seed mutation influences RNA structure? Is it possible that, as the seed seems internal, the overall structure of the sRNA is disrupted and therefore the regulation lost? Can the mutant still bind to Hfq? The structure change would also explain problems with RNase E processing.

15) 'Notably, the fully-processed mutant MdoR sRNA is less abundant than the wild-type (Figure 9C) and longer (unprocessed) fragments that contain upstream malG regions could be readily detected (Figure 9E) '- should be 8C and 8E

16) 'We conclude that the dynamics of sRNA expression and binding to Hfq are not always highly correlated.' Any thoughts why?

17) Polysome preps used cyclohexamide, but this acts but blocking the peptide exit channel in the ribosome and may not trap polysomes except by blocking the last ribosome on the assembly. Another antibiotic or non-hydrolysable GTP might be better.

18) These references have related information that may be useful to comment on in the manuscript: de Mets, van Melderen and Gottesman, 2018; Miyakoshi et al., 2018.

Also, Hfq has been known to be involved in nutrient uptake regulation in Pseudomonas aeruginosa, where it inhibits translation of certain mRNAs depending on which nutrients are available. Pei et al., 2019, have solved high resolution structures of Hfq in complex with a target mRNA and other effector molecules to show how this Hfq based regulatory complex works. This research may be related to the theme of the report here and it might be helpful to comment on these findings.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Hfq CLASH uncovers sRNA-target interaction networks linked to nutrient availability adaptation" for further consideration by eLife. Your revised article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by James Manley as the Senior Editor.

All the reviewers were enthusiastic about the manuscript and recommend acceptance pending some edits to the text. In particular, the reviewers felt that the new analyses of the CLASH data make a strong case that the identified RNA-RNA interactions are real, and thus greatly expand the known set of interactions for E. coli, and reveal important insights such as the abundance of sRNA-sRNA interactions. To better focus the manuscript, we recommend removing the section on MdoR. While the reviewers found this work to be of interest, they also felt that it was peripheral to the main theme of the study, and would be better suited to an independent publication in a more specialized journal. This would free up some space in the paper to move some of the supplementary figure panels into the main figures, improving readability. Reviewer 3 has some specific suggestions for supplementary figure panels that could be moved into the main set of figures. The detailed reviews are listed below:

Reviewer #1:

The authors have provided further experimental data and analysis and made compelling response to most of the points raised in the review. The manuscript has been improved and the support for the conclusions strengthened considerably.

One minor issue is the Figure 2E legend does not explain the figure very clearly.

Reviewer #2:

This is a much improved revised version of a manuscript describing a global method for characterization of RNA-RNA interactions. The authors have nicely addressed my previous concerns and I have no additional major issues.

Reviewer #3 – :

The new analyses of the CLASH data make a very convincing case that the novel RNA-RNA pairs reflect real in vivo interactions. My preference would be to remove the MdoR story, which is interesting but peripheral to the main theme of the paper, and does not look at a novel sRNA (MdoR was identified previously by RIL-seq). Moreover, I suggest moving some of the more important supplementary figure panels into the main part of the paper.

Figure 2—figure supplement 1C. The "distance from sRNA seed" numbers appear to be similar to the length of the sRNAs. The authors should indicate the sRNA lengths.

Figure 2—figure supplement 6 (predicted base-pairing strength for identified interactions). This is an important analysis and should be moved to the main figures.

Figure 2—figure supplement 7 (number of enriched sequence motifs from mRNA targets that match the paired sRNA) also belongs in the main figures. I suggest combining this with a couple of the most interesting examples of newly found motifs (i.e. unique to this study).

Figure 2—figure supplement 7. The criteria used to make the yes/no calls should be described in the legend.

Figure 3—figure supplement 3. This could be moved to the main figures. The legend needs to be expanded for panel C.

Figure 4—figure supplement 4. I would not expect to see sufficient overlap in regulation between E. coli and Salmonella for this analysis to be informative. I suggest removing this figure.

Figure 4—figure supplement 8. Panel labels are wrong in the legend.

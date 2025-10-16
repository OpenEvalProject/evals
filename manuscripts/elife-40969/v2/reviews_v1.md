# Peer review - Round 1

Editors:
- Antonis Rokas, Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40969.034](https://doi.org/10.7554/eLife.40969.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Bacterium-triggered remodeling of chromatin identifies BasR, a novel regulator of fungal natural product biosynthesis" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work in its current form will not be considered further for publication in eLife. Nevertheless, we appreciate the topic and find the work in principle very interesting. Thus, if you choose not to send the work as is elsewhere, but rather revise the study, eLife would be prepared to review the work again. It would, however, be treated as a new submission, although we would try to retain the same reviewers.

Summary:

This manuscript presents three connected "stories". The first story is the generation of genome-wide H3K9 and H3K14 acetylation maps in A. nidulans in the absence and presence of the actinobacterium, S. rapamycinicus. The second story is on the regulation of specific biosynthetic gene clusters (BGCs), where the authors focus again on the orsellinic BGC, which was the subject matter of three previous publications by the same group. The third story includes the truly novel part of the manuscript but unfortunately gets the least amount of space. This is the interesting finding that the (supposedly intimate) contact, shown in a previous paper, of the actinobacterium with Aspergillus hyphae somehow decrease the available nitrogen, causing an imbalance in amino acid uptake or utilization which triggers the "General Control" or "Cross-Pathway Control" system, regulated by Gcn4/CpcA- and Bas-type TFs. The authors argue that one of the putative Bas1-related TFs, now named BasR, is responsible for the bacterium-induced control.

Essential revisions:

In general, all reviewers were concerned about the novelty of this study as written and deliberated extensively on whether to "reject" or "revise". In the first story, the novelty of the study lies in the genome-wide chromatin maps generated in the presence of the bacterium, whereas previously only small regions were studied. However, the general features of chromatin regulation by themselves (i.e., upregulation by increased H3K9ac and some increase in H3K14ac) are nothing new as similar studies have been done in other fungi (yeast, Fusarium), plants and animals, both in the presence or absence of stressors. In the second story, the connection between S. rapamycinicus, acetylation, and orsellinic acid production has previously been reported, and the authors do not report incisive analyses on novel clusters. Instead they focus, quite unaccountably, on the one cluster that is down- instead of up-regulated (eas); so no new products are identified or characterized here. The third story, which has the potential to be the most novel, unfortunately gets the least amount of space and what the authors report is a phenomenological description of the pathway uncovered with no mechanistic studies other than genetic deletion analysis.

Thus, the reviewers' general recommendation is that the authors should focus their manuscript and substantially expand either the second story or the third story (in conjunction with the first). If the authors decide to expand the second story, they should describe the effects on novel BGCs and compounds. If the authors decide to expand on the third story, they should further describe the BasR pathway and how it may be activated.

1) The authors show that one of the putative Bas1-related TFs, now named BasR, is responsible for the bacterium-induced control but they completely disregard potential function of the second TF, AN8377, based on the apparently unchanged level of H3K9ac in the gene (which is not specifically shown). While AN7174 (BasR) has very restricted distribution in fungi (although there seem to be homologs in Saprolegnia, Malassezia and Ustilago; also according to FungiDB), AN8377 is the more wide-spread factor. The authors do not mention anything about this Myb/SANT domain protein and its function at all. What is shown is a phenomenological description of the pathway uncovered with no mechanistic studies other than genetic deletion analysis. For example, instead of using a rapamycin-deficient mutant of a Streptomyces species that presumably did not cause induction of Gcn5, why wasn't rapamycin simply added to the medium to test whether it was required to elicit the outcome (especially since yeast gcn5 mutants are sensitive to rapamycin). Perhaps this had been done before but then the logic of the experiment with the mutant of an unrelated species is unclear. There is also not direct evidence for BasR regulating either the genes in amino acid metabolism affected by cross-pathway control or the final target genes in clusters, e.g. by binding to motifs in their promoters.

2) If the authors focus their manuscript on the identification of circuits that regulate amino acid availability in Aspergillus, they should give their manuscript a new title. "Chromatin remodeling" specifically refers to the movement of nucleosomes, either sliding, removal or replacement, by a group of large ATPases. The authors are discussing "chromatin modifications" by a lysine acetyltransferase. This is not the same thing as "remodeling". These changes in modifications did not per se result in the identification of BasR, and that BasR directly "regulates" natural product biosynthesis also has not been shown, though it may very well affect this indirectly. Also, BasR is not novel, but distantly related to Bas1/2 in S. cerevisiae.

3) The reviewers appreciate the authors wanting to get good ChIP data on this interaction which really is where the field needs to move. However, the pulldown with antibodies against histone should not pick up any bacterial DNA. Unfortunately, it brought down lots of bacterial DNA. One possibility is that their bacteria have something like Protein A, which would indiscriminately bind the IgG heavy chain. The "fused genome" designation is basically accounting for this contamination which has to have some impact on the results. The reviewers wonder if the authors could have mixed the fungus with cell fragments of the bacterium or some other method to reduce this contamination. The reviewers like the idea of DCA, but are not sure how one can use the data, because of the contamination from the bacterial DNA. We presume that the fungal information is still viable, but would worry that you're introducing biases in library prep, etc., especially when comparing to the fungal samples where 100% of the reads map to Aspergillus. More controls might help. Would this ChIP approach bring down bacterial contamination if other bacteria were used? Maybe some focus on methods would be good to work out a cleaner result.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Chromatin mapping identifies BasR, the regulatory node of bacteria-triggered production of fungal secondary metabolites" for further consideration at eLife. Your revised article has been favorably evaluated by Detlef Weigel as the Senior Editor, and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Title: change "the regulatory node" to "a key regulatory node" since there are likely other regulatory nodes that contribute to S. rapaminicus-induced SM cluster activation (your data supports this hypothesis: 3/8 differentially acetylated SM gene clusters were not differentially transcribed in response to basR overexpression).

2) The phylogenies of basR depicted on Figure 6 and Figure 6—figure supplement 1 look different. Please explain why.

3) “The changes of H3K14ac in Figure 1 are therefore likely due to nucleosome rearrangements towards the translation start sites (TSS) rather than increased amounts of this modification”: Why does this hypothesis only apply to H3K14ac but not H3K9ac as well?

4) The authors start the Abstract and Introduction in such a way that suggests that S. rapamycinicus is directly targeting the epigenetic machinery in A. nidulans. Particularly when you say "In line…" in the Abstract, as well as give examples of the secretion of methyltransferases. Is this how you believe the change in chromatin is occurring? There is not enough data presented in this work to support this.

5) Abstract, last sentence: I believe you are missing the word "the" between "as…regulatory node".

6)Subsection “Genome-wide profiles of H3K9 and H3K14 acetylation in A. nidulans change upon co-cultivation with S. rapamycinicus”, last paragraph: Could you define what you mean by "chromatin domain" (approx. size)?

7) Subsection “The transcription factor BasR is the central regulatory node of bacteria-triggered SM gene cluster regulation”, fourth paragraph: You performed an RNAseq experiment with the overexpression of basR, and describe the changes in secondary metabolite gene cluster expression. Do you see any changes in the other phenotypes observed in the co-culture with S. rapamycinicus? It would be nice to know if there is a decrease in genes associated with nitrogen metabolism and mitochondrial function (Figure 3). This would expand the role of basR. Also, does deletion or overexpression of basR influence gcnE or other members of the Saga/Ada complex expression?

8) Figure 5: Here you illustrate the levels of expression of the ors cluster and basR, as well as the relative levels of the ors cluster products. You mention the "leakiness" of the tetOn promoter, and we can see an increase in expression of basR grown without doxycycline. This level of expression looks similar to that in the co-culture, and yet do not see an increase above what is typically seen of the ors cluster. Do you have a hypothesis as to why this is?

9) Subsection “The presence of BasR in fungal species allows forecasting the inducibility of ors-like gene clusters by S. rapamycinicus”: Earlier in the manuscript you mention the "leakiness" of the tetOn promoter when overexpressing basR in A. nidulans. Is this the case in A. sydowii? If not, it would be really nice to see the loss of ors products in the co-culture of S. rapacycinicus and A. sydowii tetOn-basR without doxycycline, demonstrating the conserved role of basR in the interaction of the two microbes.

10) How was the anti-H3 antibody validated? This particular antibody is great for western blots but does not always work for ChIP (see ENCODE histone antibody database, http://compbio.med.harvard.edu/antibodies/targets/12 and the histone validation service by the Strahl lab and company: http://www.histoneantibodies.com/). In our hands this H3 antibody does not work for ChIP. The same concern applies to the anti-H3K9ac and anti-H3K914ac antibodies; Active Motif 39161 does not show up as a validated ChIP antibody in either database, and no catalog number is given for the second antibody.

11) The model figure is interesting but some of the interactions shown have not been established. The authors show arrows implying that BasR directly regulates the clusters but that has not been shown by experiment. Are binding sites found in the promoters of cluster genes?

12) There is still relatively little mechanistic information about the regulatory cascade from stressor to induction of cluster transcription. How the switch from normal to imbalanced or depleted nitrogen occurs in presence of Streptomyces is the big question, and how GcnE and BasR are linked in Aspergillus is still not clear.

13) Subsection “Increased gene expression directly correlates with histone H3K9 acetylation”: The low correlation between active gene transcription and acetylation at H3K14 confirmed earlier results – a citation is needed here.

14) "did not affect the induction of the ors gene cluster, but on the other hand the artificial inducer of the CPC system 3-AT DOES (Sachs, 1996), it…" – this sentence needs a "does" or something similar to make it clear.

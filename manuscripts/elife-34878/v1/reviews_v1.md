# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34878.033](https://doi.org/10.7554/eLife.34878.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Organisms with alternative genetic codes resolve unassigned codons via mistranslation and ribosomal rescue" for consideration by eLife. Your article has been reviewed by Gisela Storz as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Kenneth Keiler (Reviewer #1); Yitzhak Pilpel (Reviewer #2); Alexander Mankin (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this manuscript, Ma et al. investigate how bacteria contend with unassigned codons by expressing genes with a UAG stop codon in a genetically recoded E. coli strain lacking UAG codons and RF1. This question is important because there are a number of examples in nature of codon reassignment, but it is not clear how organisms would make the transition from a canonical code if there is a large penalty for having an unassigned codon. It has also been suggested that reassignment might limit transfer of foreign DNA. The authors used mass spectrometry to identify the proteins produced from a reporter gene with a UAG codon and find that multiple mechanisms help cells deal with the unassigned codon, including suppression, frameshifting, and general mistranslation. The authors also tested the effect of inactivation of three ribosome rescue systems (tmRNA, ArfA and ArfB) on the reporter expression and on propagation of conjugative plasmids or phages that have genes terminating in UAG. These data suggested that tmRNA accounts for the resistance of their E. coli mutant strain to horizontal gene transfer.

This is an interesting study that expands our knowledge of how cells deal with difficult-to-translate codons. It is also useful for the future use of genetically recoded organisms.

Essential revisions:

1) The manuscript consistently refers to unassigned codons, implying that the work addresses this general issue. For example, in the Introduction: "Our work reveals mechanistic details into how cells rescue ribosomes stalled at unassigned codons". However, the effects observed when ribosome rescue pathways are deleted are almost certainly unique to unassigned stop codons. Trans-translation activity on ribosomes stalled at unassigned stop codons will remove the protein, but when ssrA is deleted, ArfA will release a complete polypeptide identical to what would be produced by RF1. If a sense codon were unassigned, neither trans-translation nor ArfA activity could produce active proteins. The authors should either provide an explanation for why the ribosome rescue pathways would have the same impact on unassigned codons within a gene, or they should clarify that their interpretation is restricted to unassigned stop codons.

2) For the experiment in Figure 2, the basis for some of the assignments are unclear. For example, how is it known that LEHHHHHHMVR results from a +19 skip instead of from loss of fidelity like LEHHHHHHYQR? The presence of two additional His residues in the His-tail of the GFP-His6 reporter may indeed indicate a -6 frameshift, as the authors propose, but may also indicate two consecutive -3 frameshifting events. Authors do not discuss the second possibility and suggest that they have detected "the furthest frameshift backward". Without strong evidence that they are indeed dealing with a -6 frameshift, instead of two -3 frameshifts, this seems to be an overstatement. Some of the peptides could also result from transcription errors rather than translation mistakes. A more quantitative summary of the types of peptides found in the mass spec, including the types of peptides found in the strain expressing the UAA-containing construct, would be very useful.

3) Were the experiments in Figure 3 and Figure 4 done with strains containing ssrA-DD (as in Figure 2) or wild-type ssrA? This is critical for the interpretation. All strains and plasmids need to be described at a level of detail that would allow others to reproduce the work.

4) Figure 3A is completely not clear and perhaps even misleading since it shows the effect of the different mutations on the ratio between the expressed and non-expressed constructs. It is hard to know whether the effects shown are due to effects of the mutations on the expressed or non-expressed construct. To resolve this issue, the authors should show the effects of the different mutations on the actual max OD600 and doubling time values of each strain separately (i.e. not just on the ratio).

5) The results shown for some of the strains (Figure 3) are surprising and not expected (for example, the large decrease in max OD600 ratio of the ssrA arfB double mutant – Figure 3A, the opposite trend in GFP values shown for the ssrA arfB compared to arfB and ssrA alone – Figure 3C etc.). There is no clear explanation to these peculiarities in the text. A more elaborate discussion in the context of epistatic interactions shown is needed, such a discussion could address the effects of double mutations compare to single ones. Likewise, the authors should try to comment on the observation that knockout of arfA increases GFP production (Figure 3C), whereas ArfA is expected to facilitate termination of the GFP translation at the UAG codon.

6) In Figure 4B, the authors interpreted the change in doubling time as an indication for the ability of RK2 plasmid to replicate – some explanation to this should be added to text.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Organisms with alternative genetic codes resolve unassigned codons via mistranslation and ribosomal rescue" for further consideration at eLife. Your revised article has been favorably evaluated by Gisela Storz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) For the experiments in Figure 3 and Figure 4, explain whether the replicates are biological replicates or technical replicates and at what step the replication occurred. From the source data, it appears that all of the growth data is from a single 96 well plate. Were replicate wells in the plate inoculated from independent overnight cultures or from the same culture? This distinction is important to determine if the small changes observed are likely to be physiologically relevant. It is confusing that there are 3 plates of data in the source file, but data in the figure all seems to come from a single plate. Likewise, for the conjugation experiments, do the data come from one mating that was plated three times, from three matings made with the same cultures, or from three matings performed with independently grown cultures?

2) Figure 3C shows negative protein concentration, and the explanation is that the band was quantified, and the value was plugged into a formula from a standard curve, giving a negative result. Because it is physically impossible to have negative protein concentration and there is quite clearly a band on the blot, the explanation provided suggests that the standard curve was not accurate. From the source data, it appears that the standard curves are derived from two points at 1 ng and 100 ng fit to a line. Unfortunately, almost all of the samples are outside the 1-100 ng range. It appears the negative value is the result of a large negative number from blot 3 which also seems to have an anomalously low value for 100 ng in the standard curve. The differences in protein production from the different samples are clear, but the quantification is clearly inaccurate. This problem could potentially be addressed by running another replicate of the experiment or reporting the data normalized to one of the samples such as GRO.AA [pUAG-GFP]. We will not publish a negative concentration.

Text clarifications:a) In subsection “Suppression, ribosomal frameshifting, and ssrA tagging occur at unassigned codons”: Spontaneous termination of translation could refer to untemplated termination by RF2 or to spontaneous (nonenzymatic) hydrolysis of the peptidyl-tRNA.

b) In subsection “ssrA and arfB mediate degradation of proteins containing unassigned UAG codons”: Fitness is best used in relation to competitive growth experiments because it is possible for a strain to grow to a lower OD600 in monoculture but outcompete other strains and therefore have higher fitness. It would be clearer here to refer to growth rate or OD600 instead of fitness.

c) In subsection “ssrA and arfB mediate degradation of proteins containing unassigned UAG codons”: What is the knockout of arfB being compared to here? In Figure 3A, the induced/uninduced ratio for the arfB strain looks very similar to that for the isogenic arfA+ strain, which would seem to suggest that ArfB does not play a role.

d) The sentence in the last paragraph of subsection “ssrA and arfB mediate degradation of proteins containing unassigned UAG codons” is unclear: "Interestingly, a single knockout of arfB significantly reduced production of protein from UAG-GFP to low levels similar to those mapped to quantified GFP standards."

e) In subsection “ssrA and arfB mediate degradation of proteins containing unassigned UAG codons”, the comparison for "fully restore protein expression from UAG-ending transcripts" appears to be GRO.AA[pUAA-GFP] instead of ECNR2[pUAG-GFP], but "restore" suggests it should be the latter. The comparison and the meaning behind which strain is used for the comparison should be clarified.

f) In subsection “Deletion of ssrA restores conjugative plasmid propagation and viral infection in the GRO”, it is not clear what comparison was used for the 2.4-fold increase in doubling time. The graph in Figure 4B shows a 38% increase for the arfA strain versus 28% for the isogenic wild type.

g) Discussion section: What is the evidence supporting the demonstration of ribosome stalling? It seems that ribosome stalling was assumed based on the addition of the SsrA tag. Experiments such as ribosome profiling could demonstrate ribosome stalling, but these were not done. I think stalling is part of the model here but has not been demonstrated.

h) Discussion section: Similar to (g) above, the regulatory relationship between tmRNA and ArfA was used to explain the data, so it would be circular reasoning to then use this explanation to validate the regulatory relationship.

i) Discussion section: "extensive" suggests there is a large amount of frameshifting, but the frameshifting events cannot be quantified using the techniques in this work. Perhaps something like "a wide variety of frameshifting events" would be more accurate.

j) Figure 1: The cartoon shows the SsrA-tagged protein going into the protease N terminus first, but all the proteases recognize the tag and start at the C terminus (this is not critical). In the legend, the word "hypothesized" should be removed from the last sentence – the lack of modification has been observed.

k) Figure 3 legend: For panels A and B, the legend does not match the labels. A is doubling time and B is max OD.

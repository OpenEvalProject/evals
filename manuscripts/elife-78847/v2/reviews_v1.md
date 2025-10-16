# Peer review - Round 1

Editors:
- Nils Brose, https://ror.org/04a7f6w43 Max Planck Institute of Experimental Medicine Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78847.sa0](https://doi.org/10.7554/eLife.78847.sa0)

Knowledge of the protein composition of defined subcellular compartments is of key importance for the characterization of protein machines that mediate defined cellular functionalities. The current paper presents a novel mouse line that will serve as a tool of fundamental value in this context – a Cre-inducible APEX2 reporter mouse line for acute ex-vivo proximity biotinylation. The authors provide compelling evidence documenting the usefulness of the novel reporter line, describing circuit-specific proteomes and phosphoproteomes in the corticostriatal system of the mouse brain during development. The biological insights deduced from bioinformatic analyses of the proteomic data are convincing. The new APEX2 reporter mouse line will be of substantial interest to researchers in many fields of mammalian biology.


---

# Peer review - Round 1

Editors:
- Nils Brose, https://ror.org/04a7f6w43 Max Planck Institute of Experimental Medicine Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78847.sa1](https://doi.org/10.7554/eLife.78847.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Dynamic proteomic and phosphoproteomic atlas of corticostriatal axon neurodevelopment" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alexandros Poulopoulos (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this letter to help you prepare a revised submission.

Essential revisions:

All three reviewers regard this manuscript to be a strong eLife candidate. The reviewers and editors propose to transfer the article from the 'Regular Article' to the 'Tools and Resources' section. The main reason is that all reviewers found the 'new biology' provided by the paper to be limited. Further, and as outlined below, the reviewers see a series of critical issues that need to be addressed by the authors before the manuscript could be accepted.

Essential Changes – Possibly Requiring Additional Experiments

1. For sample preparation for mass spectrometry, the authors follow the interesting concept of first enriching the phosphopeptides from the pool of TMT-labeled tryptic peptides and then using the unbound fraction from that step for further peptide fractionation, followed by mass spectrometric protein quantification. While this strategy looks very straightforward in principle, one would expect that the phosphopeptide enrichment comes with an unspecific loss of other peptides in general, and with a semi-specific loss of acidic peptides in particular. Was this potential issue investigated by comparison with samples that were fractionated directly without prior phosphopeptide enrichment? Or with other words: the rationale for this sequential procedure is compelling – quantification of both protein and phosphopeptide abundance from the same (limited) sample, but what is the price for it as to peptide loss? A control experiment regarding the serial phospho-enrichment and peptide fractionation procedure might be helpful here. The reviewers thought of a sample that is biotin-enriched, digested, and TMT labeled (see workflow in Figure 3C). To keep it simple, this can come from pooled brain slices so that limited material is not an issue and it does not necessarily need to have a complex multiplexing design. This sample is split into two: one half is directly going to high pH reverse-phase peptide fractionation, followed by LC-MS; the other half is going through serial phospho-enrichment and peptide fractionation and LC-MS according to the workflow presented. The idea would be to compare the two proteomes obtained, i.e. original input material (half 1) vs. unbound fraction (half 2), eventually by combining the results from the unbound and bound fraction of the phospho-enrichment. This is a suggestion to further corroborate the applicability of the serial procedure, which may be of interest to the phosphoproteomics field in general. However, if the authors can cite cases showing applicability or have similar own data already available from the setup phase of their workflow, the reviewers will not insist on additional experiments as outlined above, as long as the issue is properly addressed.

Essential Changes – Requiring Further Data Analysis

2. The proteomic and phosphoproteomic analysis of corticostriatal axons is interesting but somewhat incomplete. To validate that the approach reliably reports key developmental stages of corticostriatal axons, one should also look at presynapse maturation and map at what time point presynaptic adhesion proteins, vesicle proteins, active zone proteins, and components of the endocytosis machinery appear. The SynGO database might help in such an analysis. What would generally be helpful would be a more systematic presentation of expected proteins in different developmental phases (axon outgrowth, steering*guidance, synaptogenesis, synapse function) vs. the actual findings.

3. Although both male and female animals were used in the study, the authors do not discuss sex differences in the proteome or phosphoproteome during development. If such data are available, seeing differences in proteomics and phosphoproteomics between sexes during development would be very interesting. If there are no observed differences, adding a sentence to clarify this issue would be helpful.

Essential Changes – Material Availability

4. The novel mouse line described here will become a sought-after tool for many fields of mammalian biology. To make this work, the authors must formally state that the line will be made available to all members of the academic research community upon reasonable request, and describe how exactly to obtain it.

Essential Changes – Changes to Text

5. The APEX2 reporter mouse line is a novel tool with broad applicability for proximity labeling approaches and, understandably, the authors advertise its advantages, mainly via the suitability for short temporal windows. However, the discussion on the limitations of the approach falls short. The authors should make clear that the APEX method in general is limited to ex vivo approaches such as the acute brain slices used here due to the limitation that potentially toxic reagents (i.e. low membrane-permeable biotin-phenol and H2O2) have to be delivered to the target tissue. Although treatment with H2O2 is rather short, undesired oxidative stress signaling may have to be taken into account, particularly when protein phosphorylation rather than protein abundance is assessed. It would also be important to discuss the pros and cons of perfusing the mice prior to preparation of brain slices; e.g., in the context of removal of catalases/endogenous peroxidases or potential for substrate delivery (like recently shown in heart, doi 10.1038/s41586-020-1947-z).

6. In line 122, authors may want to change the term "knock-in line" to "reporter line", as Rosa26 was used as a transgene landing-pad locus, rather than for any endogenous regulatory properties of a specific locus, as knock-in may imply to some readers.

7. The authors claim that they "modified published APEX-mediated biotinylation protocols to optimize protein labeling in thick brain tissue (Dumrongprechachan et al., 2021)" (line 150-151), which implies considerable technical advancements in comparison to their earlier work. At first glance, however, it seems that only the incubation time with H2O2 was doubled. The author should expand on their claim – or specify or remove it.

8. As it is essential for understanding the design of the proximity labeling approach, particularly for the non-expert reader, the Rbp4Cre mouse line should be introduced with a few words, instead of just citing the resource paper on GENSAT BAC Cre-recombinase driver lines.

9. Proteins with q-value < 0.05 and log2FC > 0 were considered axonally enriched. Given that the authors handle their data otherwise with highest stringency, is there a special reason not to apply a more stringent/empirically defined threshold on log2FC?

10. When establishing proteins that are enriched in somata vs. axons, a soma prep from the same APEX mouse line would have been more appropriate as a control compared to the virally ovrexpressed Histone 2B-APEX control used, which would label proteins sequestered only to the nucleus. The authors should qualify in the text that proteome differences they see in these two datasets do not arise solely from somatic versus axonal enrichment, but also from the confounding differences of viral versus Rosa26-locus expression levels, and cytosolic versus histone-fused Apex.

11. While there is a series of novelties in this work, overt "first ever" statements in the text (e.g. lines 94-96, 348-349) are redundant and inherently ambiguous in their factuality. The work's novelty is better served speaking for itself.

12. In line 109, the authors should rephrase "revealing proline-directed kinases and phosphosites as major regulators for corticostriatal projection development" to something more closely fitting the observation that proline-directed kinases and phosphosites are dynamically regulated in corticostriatal projections during development. The current phrase infers that the functional component has been determined in this study, which would need further experimental determination (e.g. knockouts). The data provided in the manuscript only point to these proteins being highly dynamic, in both abundance and phosphorylation throughout development.

13. In line 163, authors should change the phrase "differential pattern of protein labeling" to "reduced protein abundance", as there are no obvious ratiometric changes in band intensity patterns in the western blot shown in Figure 2 supplement 1B. If the authors want to make a claim on that, they should provide a GFP blot to normalize to the amount of cells that express APEX in the region to determine if changes in protein abundance are due to the number of VGAT vs VGLUT cells, or due to differential protein abundance.

14. The discussion requires a few additional thoughts: (i) The authors do not properly reflect the involvement of proline-directed kinases in the development of corticostriatal projections, which stands in contrast to the fact that they sell this as one of their major findings throughout the manuscript. (ii) An obvious future research target based on the present study is the role of Fyn in the development of corticostriatal connectivity. Here, a discussion of the Fyn KO phenotype might be informative (as I did not find evidence for changes in corticostriatal connectivity in the Fyn KO). (iii) It is striking that a Gria1-Dlg1-Dlg4 network was discovered in the corticostriatal axon proteomics. This is unexpected – a postsynaptic network in an axonal dataset. The authors should discuss what this might mean for their new mouse line (e.g. leakiness of the APEX2 reporter, transfer of APEX2 etc.). (iv) The discussion on the Netrin1-DCC pathway is not particularly strong, while aspects of the data are stronger. The authors might want to consider either getting rid of this discussion point, or putting Figure 4F in a supplemental figure. The data provided only show phosphorylation events, not activity of a specific pathway, as Fyn is involved in a lot of different processes. Figure 4 supplement 1B may be a more important panel to have in Figure 4.

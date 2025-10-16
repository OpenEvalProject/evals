# Peer review - Round 1

Editors:
- Deborah Bourc'his, Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68312.sa1](https://doi.org/10.7554/eLife.68312.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper describes a novel regulatory mechanism coupling RNA m6A modification to polyadenylation site selection and transcriptional termination, which is shared between apicomplexan parasites (Toxoplasma gondii) and plants (Arabidopsis thaliana). The data are supported by multi-angle approaches (biochemistry, structural biology, functional genetics and genomics) and are of wide interest to audience studying gene and RNA regulation, but also communities who develop parasite-targeting strategies. These findings highlight how transcription barriers are maintained upon intense replication of a parasitic gene-dense genome and may explain how these organisms quickly adapt to external stimuli.

Decision letter after peer review:

Thank you for submitting your article "A plant-like mechanism coupling m6A reading to polyadenylation safeguards transcriptome integrity and developmental genes partitioning in Toxoplasma" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Dominique Soldati-Favre as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) Regarding the connection between m6A RNA methylation and transcriptional readthrough: please provide accurate quantifications, as listed by reviewer #1 and comment 12 from reviewer#3.

2) Quantifications are also needed in the knock down experiments: please provide quantitative WB rather than IF. Also refer to reviewer#3 comments to try to improve detection of m6A changes, beyond poorly quantifiable IF data (m6A ELISA could also be attempted?).

3) Similarly, quantitative measures should be provided to describe the phenotypic overlap between the METTL3 KD and CPSF4 KD (Comment 13 reviewer #3) and the pulldown overlap between the different protein complexes (comment 14 reviewer #3).

4) Do you have evidence to support that m6A is developmentally regulated in T. gondii?

5) Reviewers raised similar comments about the writing: sentences are often too lengthy, too internally convoluted and deploy sesquipedalian vocabulary, rendering their meaning unclear and the message the authors want to convey difficult to understand. The text should be simplified and streamlined wherever possible.

6) Provide explanations to specific questions raised by the different reviewers.

Reviewer #1:

In this rich and multidimensional manuscript, Farhat et al. report a role for m6A in controlling transcriptional termination in T. gondii. The authors combine biochemistry, structural biology, genetic and genomic approaches to characterize CPSF4, a protein forming part of the cleavage and polyadenylation complex in T. gondii. The authors demonstrate that using its YTH binding domain it selectively binds m6A-harboring targets. Using genetic disruption of this protein or m6A-machinery components, the authors demonstrate that loss of m6A leads to widespread levels of transcriptional readthrough.

In general, we very much enjoyed this manuscript. It establishes a novel mode of regulation mediated by m6A, and demonstrates how such a mode of regulation (which is not present in human) can evolve, namely by the fusion of an m6A binding domain to an RNA binding protein.

Key comments refer to the genomic aspects of the paper. In this section the authors seek to ascribe a causal role for m6A in controlling transcriptional termination. This section is rich in qualitative descriptions and accompanying figure panels (figures 6 to 10 and many supplementaries are nearly entirely based on screenshots). However, it lacks quantitations of the signal and statistics that are critical in order to evaluate the weight of the evidence in favor of the proposed model. Specifically, is remains unclear :

– In how many genes is transcriptional readthrough observed, in each of the three mutants?

– What is the extent of overlap between the three? Is it statistically significant, taking into account the fact that the nanopore based approach is heavily dependent on expression levels?

– How many m6A sites are identified by the authors? How are they distributed within genes? Other than the reported enrichment in 3' UTR, are they also enriched near the stop codons as has been reported in mammals?

– What fraction of the m6A sites are in genes with evidence for transcriptional readthrough? and in genes without evidence for transcriptional read-through? Is the overlap between m6A and readthrough statistically significant?

– Are genes that are methylated at higher levels also subject to more readthrough upon loss of the methylation machinery?

– At the single molecule level (via nanopore): can the authors distinguish between the methylated and unmethylated molecules, and assess whether readthrough is only observed in the latter molecules?

In our view it is critical to quantitatively address these questions, to provide the extent of support for a direct relationship between m6A and termination.

Reviewer #2:

Although the function of m6A in mRNA stability and translation has been well established, the implication of m6A in the control of polyadenylation site selection remains obscure. Dayana C. Farhat et al. first identified the components of the core CPSF complex within T. gondii, an obligate parasite who can turn into major thread to the unborn and to immunocompromised people. Then they used biochemistry and structural methods to prove that CPSF4 was an m6A reader, coupling m6A modification directly to APA events. Finally, they detected transcriptional readthrough events upon CPSF4 or Mettl3 KD using Nanopore DRS. Most importantly, they detected m6A-dependent PAS was an efficient transcriptional barrier, that preventing aberrant readthrough of highly expressed genes into the downstream repressed ones in the high gene density genome. And this will make the parasites to reproduce more quickly.

The conclusions of this paper are mostly well support by the data, and this study opens up new insights about this ancient APA regulation. It helps us to understand how parasites and plants adjust themselves quickly under external stimuli.

The conclusions of this paper are mostly well support by the data, but some aspects need to be clarified.

1. What's the relationship between ZnF recognition and YTH recognition of m6A within CPSF4? Because ZnF of CPSF4 in human is found to recognize AAUAA site directly, but AAUAA site was also reported to be m6A modified, which is recognized by YTH domain of CPSF4.Do you have evidence to show PAS binding by these two domains within one protein are competing or assisting each other?

2. Knocking down of CPSF4 or Mettl3 would have some indirect side effects since these two proteins might involve in other biological processes, I'm wondering if you could test the 3'-end profiling using CPSF4-m6A-binding-defective mutants.

3. In the paper cited by the authors (doi: 10.7554/eLife.49658), nanopore DSR was also used to map the mRNA profiling in the m6A writer(vir-1) defective background in Arabidopsis, but opposite conclusions were reached: could the authors comment on this inconsistency?

4. As you compared the structure of TgYTH-m6A RNA with other complexes, and identified RNA bound within a clearly charged groove as seen in other structures. What's the point of a potential secondary binding groove as stated in the text? What do you mean by referring to "multiple binding modes" in line724?

Reviewer #3:

In this paper, Farhat et al. demonstrate that m6A on mRNA in Toxoplasma gondii interacts with a cleavage and polyadenylation factor protein (CPSF4). This interaction is mediated via the YTH-domain and is characterized using high resolution crystal structures and isothermal calorimetry. The authors have identified the CPSF4 complex using reciprocal IP-MS. The also carried out an IP-MS for the m6A writer machinery – namely METTL3, METTL14, and WTAP homologs to reflect the m6A writer machinery. The main findings for this paper relate to the fact that a loss of or CPSF4 YTH reader protein results in the production of chimeric mRNAs as a result of aberrant transcriptional termination in T. gondii and Arabidopsis thaliana. This phenomenon is also phenocopied in the loss of METTL3 writer protein. Of interest, transcripts which are reliant upon this m6A-dependent recruitment of CPSF4 are generally upstream of otherwise repressed developmental stage-governed transcripts.

While the paper presents a large amount of data, some of excellent quality, there are critical issues that need to be addressed. Of importance, the implication that METTL3 or CPSF4 KD is involved in developmental regulation requires a clear demonstration of a phenotype where this is impaired and that m6A site is dynamically regulated at the boundary of these transcripts. This involves demonstrating stage transition is impaired in the knockdowns and also using nanopore or other technologies demonstrate that the m6A site is "dynamic" despite not possessing known demethylases.

The effort to combine multiple strands of work ranging from polyadenylation and transcript termination, the role of m6A in this process and alternative splicing in aberrant transcripts and finally development made the story confusing and often detracted from the important message that could be conveyed. Also, it meant that some conclusions were not well supported by the data.

Here is a list of some of the essential issues to address:

1. It is essential to show quantifiable western blot data that shows the downregulation of the different target proteins in the knock down cell lines.

2. m6A quantification cannot be carried out using IFAs. If using antibodies – show specificity as well. M6A occurs in the host cell as well – why is this not reflected in the staining Figure 3A? I would suggest to either selectively enrich for TG mRNA and then carry out dot blots or mass spectrometry or perhaps even sequencing based approaches. This is critical since none of the IFA data presented is quantifiable.

3. The link between developmental regulation and m6A is poorly supported. As a minimum it would be necessary to show that m6A levels are developmentally regulated.

4. Also, there is a significant challenge on how the knock down data can be interpreted. The m6A knockdown would have a global impact of this modification in all mRNA locations. So it is not clear on whether the impact observed is a direct or indirect result.

5. "Of the CPSF complex, the T. gondii CPSF4 subunit can be distinguished as one holding a unique architecture which interestingly is shared with the plant CPSF4 family, and it constitutes of a co-occurrence of three zinc fingers and a conserved YTH domain" – Which YTH domain? DC or DF?

6. In this context I could imagine that the replacement of CPSF4 with a version lacking the YTH domain may be a way to clearly demonstrate the importance of the YTH domain.

7. Binding affinities using ITC – TG CPSF4 with m6A has a Kd at 5uM for the modified oligo and Arabidopsis CPSF4 shows close to a Kd 6uM for the non-m6A modified oligo. Could the authors explain this judgement on what constitutes good/bad binding?

8. In addition, the specificity of YTH binding to m6A is based on a single oligonucleotide sequence. At least a scrambled version of this should be used.

9. Based on the crystallization results where CPSF4 does not show RNA context specificity, except for m6A residue, how do the authors predict that this recruitment IS context specific? There exist other m6A sites in regions that do not constitute the 3' UTR (Line 612).

10. Figure 7A -An IFA is not sufficient. A western blot is needed in the very least to validate the KD.

11. Figure 7B – Are these adjusted p-values. Then these would not be a relatively low number of differentially expressed genes then as per Line 457.

12. Line 480 – There must be a way to quantify these readthrough events. A statement like this requires substantiation in the form of data.

13. Please provide a quantitative methodology to depict how METTL3 KD phenocopies CPSF4 KD. How many transcripts display aberrant splicing and which of these are common to both KDs?

14. Line 209 – Could you draw a venn diagram or similar representation to see the overlapping proteins identified in the complex in each pulldown?

15. Since you identified Val522 as an additional amino acid for the binding cage of m6A when compared to its counterparts, I suggest you to test the binding affinity towards m6A-modified RNA using V522 mutation by ITC.

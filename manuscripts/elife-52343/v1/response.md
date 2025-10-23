# Author response - Round 1

Authors:
- Jonathan M Philpott ([ORCID: 0000-0002-0793-0193](https://orcid.org/0000-0002-0793-0193))
- Rajesh Narasimamurthy ([ORCID: 0000-0003-4224-3791](https://orcid.org/0000-0003-4224-3791))
- Clarisse G Ricci ([ORCID: 0000-0002-3289-2248](https://orcid.org/0000-0002-3289-2248))
- Alfred M Freeberg ([ORCID: 0000-0003-0365-5769](https://orcid.org/0000-0003-0365-5769))
- Sabrina R Hunt
- Lauren E Yee ([ORCID: 0000-0002-4278-6115](https://orcid.org/0000-0002-4278-6115))
- Rebecca S Pelofsky ([ORCID: 0000-0001-7944-3880](https://orcid.org/0000-0001-7944-3880))
- Sarvind Tripathi ([ORCID: 0000-0002-6959-0577](https://orcid.org/0000-0002-6959-0577))
- David M Virshup ([ORCID: 0000-0001-6976-850X](https://orcid.org/0000-0001-6976-850X))
- Carrie L Partch ([ORCID: 0000-0002-4677-2861](https://orcid.org/0000-0002-4677-2861))

## Response text

DOI: [10.7554/eLife.52343.sa2](https://doi.org/10.7554/eLife.52343.sa2)

Essential revisions:

1) It is clear from the kinase assays that CK1 (WT or tau) activity on PER2 depends on phosphorylation of PER2 priming site. Have the authors modeled the changes in terms of the secondary structure of the peptide upon phosphorylation at the priming site Ser569? The chemical shift of the peptide upon Ser569 phosphorylation can be used to inform the modeling and to explain why the priming is required.

To address this concretely, we measured chemical shifts for the Cα and Cβ atoms from a 13C/15N/1H HNCACB spectrum of the phosphorylated FASP and compared these to the Chemical Shift Index (CSI), which reports quantitatively on the propensity for secondary structure (Noor et al., 2015, NAR). Our CSI analysis suggests a modest increase in the propensity for β-strand structure localized within the phosphorylated FASP region (S659-S665 in red, Author response image 1). However, there is recent literature showing that the CSI is biased towards the prediction of secondary structure propensity within phosphorylated regions due to phospho-dependent chemical shift changes (Hendus-Altenburger et al., 2019, J Biomol NMR). In particular, we noted that changes in secondary structure propensity map exclusively to the phosphorylated serine residues within the peptide, with only marginal changes in neighboring residues. Based on these factors and the limited dispersion of proton chemical shifts in the 15N/1H HSQC spectra, it is highly unlikely that the FASP peptide studied here (33 residues) takes on secondary structure in the presence or absence of phosphorylation.

The larger question of why priming is required for high efficiency activity by CK1 remains to be addressed in future work. We believe that our analysis of the K224D mutant, which likely disrupts anion binding at Site 1 without altering the allosteric regulation at the activation loop like tau, suggests that primed peptides likely dock into the anion binding pocket at Site 1 to position the downstream sites. We are actively pursuing modeling and experimental structure determination to probe this model in more detail.

2) It remains unexplained how the altered activation loop conformational dynamics in tau favors degron phosphorylation. Does this study suggest that there are substrate-specific active conformations of CK1? The reviewers suggest a docking study of the degron peptide on CK1 to help understand the underlying mechanism.

We agree with reviewers that the exact mechanism by which altered dynamics of the activation loop favor degron phosphorylation by CK1 remains to be determined. We do believe that our study suggests that there are substrate-specific conformations of CK1. Obviously, obtaining a mechanistic understanding of this will require more in-depth structural studies and/or MD simulations. At the reviewer’s suggestion, we began a series of docking studies of the degron with the wild-type kinase in its loop up or down conformation and have some provocative initial results. We thank the reviewers for their suggestion, but we feel that significantly more work will be needed to validate these initial findings, putting it outside the scope of this study.

3) In the presence of both FASP and degron peptide in vitro, does tau still phosphorylate the degron sequence more than WT? What degron residues are crucial to the tau propensity for the degron. A kinase assay with peptides that are variants of the degron sequence may help explain why tau prefers the degron over FASP. Has the affinity of the degron and FASP peptides been measured for CK1?

We also think this is an interesting question! Thanks to our NMR-based kinase assay, we can unambiguously resolve phosphorylation on both the FASP and degron substrates in one assay. We ran this experiment in response to the reviewer’s question and found that WT and tau CK1 maintain their distinct preferential activity even in the presence of both substrates. These data are described subsection “tau exhibits a gain of function on the Degron” and in Figure 1—figure supplement 1G-H.

With regards to the question about the exact specificity determinants on the degron, this is an area of ongoing study in our labs. We are currently working to identify the molecular determinants of CK1 activity on the non-consensus FASP priming site and the degron. We feel that this work is best suited for a more comprehensive report in the future. The affinity of both peptides for the kinase has not been explicitly measured, but we have estimates of the Kms in the ~10-500 µM range, similar to other kinases.

4) Perhaps a missed opportunity for the authors is the discussion of the Y225 during structural and MD simulation analysis. This side chain seem to adapt different poses in the loop up and loop down conformations and seem to be a direct structural bridge forming a network consisting (R178-K224) -L173. The reviewers suggest the authors to analyze the motion of Y225 and its coupling to the motion of the activation loop in WT and tau simulations. If a strong coupling signal was found, perhaps mutational analysis of this residue could help establish the full molecular allosteric network.

We completely agree with the reviewers and we thank you for pointing out this interesting observation. In going back through our MD simulations, we found that the conformation and mobility of Y225 was indeed different in the tau mutant compared to the WT enzyme. We have included some text in subsection “tau stabilizes the rare ‘loop up’ conformation of the CK1 activation loop” to describe this observation and a figure panel in Figure 4—figure supplement 1. In our analysis, we also found evidence that the conformation of Y225 was coupled to the Site 1 anion binding pocket and is therefore potentially in a position to control the equilibrium between the ‘up’ and ‘down’ conformations of the activation loop. However, we feel that a full dissection of the role of Y225 with mutational analysis and functional characterization, as well as a more comprehensive description of the allosteric communication in CK1δ, is beyond the scope of the current study.

5) This manuscript has room for improvement in terms of readability. The article is wordy and a lot of literature information and previous discussions are presented throughout the whole manuscript due to perhaps authors strong sense of due diligence. By trying to move as much indirect material as possible to the supplementary and balancing the discussion of the previous literature to the more through atomistic detail analysis of the allosteric network, the manuscript can become more readable. Some key terms are not explicitly introduced in the Introduction. For instance, the background of the tau mutation is not described in the Introduction, although it is later in the Results.

We agree that the manuscript is wordy. It was a bit challenging presenting the first mechanistic study on this kinase and trying to integrate several decades’ worth of genetics and cell biology that laid the framework for our understanding. We trimmed a significant amount of text where we felt we could without sacrificing scientific rigor.

We also note the reviewers’ point about waiting until the Results section to introduce the tau allele. To satisfy this concern, we moved some of general info about the tau mutant to the Introduction and shortened its description in the Results section.

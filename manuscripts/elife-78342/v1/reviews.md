# Peer review - Round 1

Editors:
- Paola Bovolenta, https://ror.org/02gfc7t72 CSIC-UAM Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78342.sa0](https://doi.org/10.7554/eLife.78342.sa0)

This study dissects the complex Shh pathway to explain the phenotypic similarity between Lhx2 and Shh retinal knock-out mice. The authors use multiple converging experimental strategies to show Lhx2 activates the Shh pathway, mainly by up-regulating co-receptors Gas1 and Cdon in retinal progenitor cells. The experiments are creative, and the findings provide evidence that Lhx2 acts in a contextual manner and integrates signalling pathways, conferring enhanced Retinal Progenitor Cells with the competence to respond to Shh. The study provides novel and interesting views on retinal development.


---

# Peer review - Round 1

Editors:
- Paola Bovolenta, https://ror.org/02gfc7t72 CSIC-UAM Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78342.sa1](https://doi.org/10.7554/eLife.78342.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors' note: this paper was reviewed by Review Commons.]

Decision letter after peer review:

Thank you for submitting your article "Lhx2 is a progenitor-intrinsic modulator of Sonic Hedgehog signaling during early retinal neurogenesis" for consideration by eLife. Your article has been reviewed by 2 peer reviewers at Review Commons along with an additional peer reviewer at eLife, and the evaluation has been overseen by a Reviewing Editor and Claude Desplan as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tom Glaser (Reviewer #3).

Based on your manuscript, the reviews and your responses, we invite you to submit a revised version incorporating the revisions as outlined in your response to the reviews.

Please also address all the main point raised by the additional reviewer of your manuscript as they will help increasing the clarity of your message. The additional comments points to additional details of the manuscript that need your attention.

Reviewer #3:

The Lhx2 LIM homeodomain transcription factor plays multiple key roles in vertebrate eye development - specifying regions of the eye field, patterning the optic cup, maintaining the pool of mitotic retinal progenitor cells (RPC), modulating retinal cell fate determination (histogenesis), and integrating signaling pathways. In germline Lhx2 mutants, morphogenesis arrests at the optic vesicle stage.

All paracrine signals have two parts - the sending and responding cells. In this study, Li, Gordon et al. explore how neural progenitors acquire the competence to receive and transduce sonic hedgehog signals - via expression of coreceptors and other pathway components, regulated in large part by Lhx2.

They deeply explore the mechanism of Lhx2 action in RPCs. They offer plausible explanations for the phenotypic similarity between Lhx2 and Shh retinal CKO (conditional knockout) mice. To test their central hypothesis - that Lhx2 confers RPCs with enhanced competence to respond to Shh signaling by positively regulating expression of Gas1 and Cdon coreceptors - they push and pull the Shh pathway at multiple levels. They employ informative mutants, Hes1-CreERT temporal loss-of-function mice (to delete Lhx2 in all RPCs at the onset of histogenesis, from embryonic day E11.5), pharmacological treatment (N-Shh, PMA agonist), bypass experiments, and creative bioassays (e. g. retinal explant cocultures with apposed open-loop NIH3T3 fluorescent Shh reporter cells). They assess molecular effects of Lhx2 deletion on mRNA (bulk RNA-seq, qPCR) and protein abundance, chromatin accessibility, and informative reporter expression (e. g. Gli1-lacZ knock-in allele) and evaluate Lhx2 genomic targets (ChIP-seq). The various data converge. The authors apply standard pathway logic (molecular epistasis) to define the major steps and general mechanisms through which Lhx2 modulates Shh signaling.

The results are complicated and do not fully explain all phenotypes. Lhx2 is neither necessary nor sufficient for Shh action. Signaling is attenuated but not eliminated in mutant RPCs. Despite this complexity, the study advances understanding and provides a basis to explore how signaling pathways are integrated and finely tuned.

1. The initial data are presented in a confusing order. After noting similarity between Lhx2 and Shh retinal CKO phenotypes, the authors show in situ hybridization images (Fig 1) suggesting that Shh signaling (Gli1) - but not Shh ligand - is downregulated in Lhx2 CKO retina. This is the major premise for the study - and title of the first Results section. However, the ISH data are not quantitative (or persuasive), and the CKO histological phenotype does not obviously differ from control at E14 ('cell type profiles' in line 132, a bit vague), so the manuscript does not start with a strong foundation. However, the Gli1 and Shh qPCR data (Fig 6B) are convincing and do support ISH findings - and should be presented early, before the Gli1 immunoblot (Fig 1C). Most readers will look for these quantitative mRNA data in Fig 1. They belong here, logically, since Gli1 is a well-established, sensitive readout of Shh signaling.

Likewise, the Lhx2 RNA-seq data in Fig. 2C-E are confusing. Knowing the structure of the conditional allele in advance, the authors should quantify mRNA isoform reads with WT (ex 1/2, 2/3 or 3/4 junctions), deleted (ex 1/2 junction) or unknown (reads lacking ex 1-3) splicing patterns separately, in their existing dataset. Rather than the simple schema in Fig 1E, they should show 6K WT and CKO reads aligned to the mm10 reference genome, along with the AUG and qPCR amplicon, and note whether deleted isoforms are predicted to undergo NMD and should thus have lower mRNA abundance a priori (in Methods or legend).

How much is Lhx2 mRNA downregulated within 48 hr of Tam treatment (line 130)? What are 'other' features in Fig 2B?

2. The bioinformatic rationale for exploring Lhx2 regulation of Shh pathway genes (Fig 3) is logical but presented in a jumbled way. Two orthogonal strategies are applied (three, including ATAC-seq) - and only one pathway (Hh) emerged with statistical significance in both. One approach (RNA-seq of dissected CKO retinas, with KEGG pathway topology analysis of DEGs) tests altered mRNA expression - direct and indirect regulation - whereas the ChiP-seq data (from flow-sorted wild-type RPCs in an earlier study, analyzed via clusterProfiler) tests Lhx2 chromatin occupancy - expected for direct regulation. The logic for this overlapping strategy is buried in the text, and obscured by interspersed panels in Fig 3, forcing the reader to carefully dissect the legend to understand what kind of (highly derived) data are presented. Label panels 3AB better so these methods are obvious.

3. The appositional explant assay is a compelling functional measure of bioactive Shh (Fig 5). Likewise, the Lhx2 and Ptch1 CKO and dCKO data (Fig 7) are creative and instructive, showing that Lhx2 acts upstream but that Shh signaling remains intact (attenuated) in Lhx2 CKO RPCs.

However, the qPCR normalization (Fig 7A) does not make sense (to me) - each control value should be set to 1.0 +/- SE (or SD). There is a similar normalization concern in Fig 10 (lines 701 ff notwithstanding).

Does the increased abundance of Cyclin D1+ cells (Fig 7) reflect an increase in bioactive Shh mitogen (Fig 5B)?

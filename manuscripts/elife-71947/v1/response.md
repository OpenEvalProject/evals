# Author response - Round 1

Authors:
- Chidiebere Akusobi ([ORCID: 0000-0002-1611-0015](https://orcid.org/0000-0002-1611-0015))
- Bouchra S Benghomari
- Junhao Zhu ([ORCID: 0000-0002-3301-5677](https://orcid.org/0000-0002-3301-5677))
- Ian D Wolf
- Shreya Singhvi
- Charles L Dulberger ([ORCID: 0000-0002-1334-5468](https://orcid.org/0000-0002-1334-5468))
- Thomas R Ioerger
- Eric J Rubin ([ORCID: 0000-0001-5120-962X](https://orcid.org/0000-0001-5120-962X))

## Response text

DOI: [10.7554/eLife.71947.sa2](https://doi.org/10.7554/eLife.71947.sa2)

Essential revisions:

1. There is no evidence that PBP-lipo is a lipoprotein although the authors presented this as a certainty (lines 143-144). Several PBPs have a cysteine residue within or near the end of the N-terminal TM region, but these are not lipoproteins. For example, E. coli PBP3 has a cysteine at position 30 shortly after the TM region, but it does not appear to be a lipoprotein. The authors should either prove that PBP-lipo is a lipoprotein, which has been achieved for lipoproteins in other species by mass spectrometry and/or labelling with radioactive palmitate. If such evidence cannot be provided, they should rename the enzyme, removing 'lipo' from the name, and refrain from presenting the protein as a lipoprotein.

PBP-lipo has previously been identified computationally as a lipoprotein though, as the reviewers point out, these predictions are not always reliable. To determine if it truly is acylated, we performed an extraction and found that PBP-lipo segregates into the lipoprotein fraction (Figure 3 —figure supplement 3).

2. There appears to be a problem with the mRFP-PBP-lipo construct in which mRFP is tagged at the N-terminus of PBP-lipo (line 210). If PBP-lipo is indeed a lipoprotein, as assumed by the authors and perhaps confirmed in the above-mentioned point, then this N-terminal tagging may not be the best approach. Lipoproteins are typically cleaved at the N-terminus of the cysteine residue, which would remove the mRFP tag from the protein and make the cellular localization experiments meaningless. Considering these concerns, the authors should:

a. Prove that the construct is functional and can complement cells depleted of WT PBP-lipo, and

b. Subject cell extracts with Bocillin labelling and confirm the presence of an mRFP-PBP-lipo band or

c. Detect mRFP-PBP-lipo in cell extracts with an antibody against mRFP.

(A is essential and either b or c would be acceptable)

Also, in line 211 they should state whether mRFP-PBP-lipo was expressed in the presence (or not) of WT PBP-lipo.

Created Figure 5 —figure supplement 1 to address these revisions.

– S Figure 5 —figure supplement 1A shows a schematic of the mRFP-PBP-lipo fusion protein. mRFP was inserted after the Cysteine residue and attached to linkers on the 5’ and 3’ region. The site of the single sgRNA binding site that was mutated to produce a recoded version of the construct is depicted as well

– Figure 5 —figure supplement 1B depicts a fluorescent Western Blot against 2 strains, one expressing mRFP-PBP-lipo and the other expressing PBP-lipo. Both constructs were strep-tagged. The anti-strep Western Blot shows the mRFP-PBP-lipo fusion protein runs at the expected molecular weight if both proteins were fused

– Figure 5 —figure supplement 1C is a growth curve showing that both the recoded and non-recoded versions of mRFP-PBP-lipo complements the growth defect caused by the native PBP-lipo knockdown. The recoded construct fully complements the phenotype while the non-recoded version partially complements

Added text to explain that the mRFP-PBP-lipo fusions are expressed in the context of native PBP-lipo expression that is either unrepressed or repressed with ATc. Also we explicitly mentioned in lines 227-228 that the fusion protein is expressed in the presence of the native PBP-lipo protein

3. Reviewers appreciated the experiments to investigate the PG networks in Mab and other mycobacteria which revealed, for example, the genetic interactions between the PBP-lipo gene and the dacB1, pbpB and MAB_0519 genes. However, to support the appending conclusions, the authors need to confirm that DacB1 and PBPB were depleted by the CRISPR technology to similar extent in Mab and Msm, to exclude the possibility that differences in genetic interactions were due to different efficiency in the CRISPR gene depletion in the two species. This is particularly important for Msm, as there were no genetic interactions (lines 270-2760). Hence, they should perform Bocillin assays and quantify the depletion of DacB1 and PBPB in both species.

We performed qPCR to measure level of repression of pbpB, dacB1, and MAB_0519 in both the Mab double knockdown and Msm PBP-lipo knockout strains (Figure 6 —figure supplement 5A). The level of knockdown in both species for all three genes were comparable and not statistically significantly different from each other. Since the CRISPR system we use acts at the level of transcriptional repression, this provides better quantitation than protein methods such as Bocillin labeling.

4. Control experiments to show that the DacB1-GFPmut3 fusion is functional should be added

We performed a Western Blot on the DacB1-GFPmut3-strep protein and detected the presence of a band ~70kDa, which is the predicted size of the fusion protein (Figure 6 —figure supplement 4A). Since DacB1 is redundant and non-essential, there is no real assay for function so there is no way to prove that it is functional.

5. To strengthen their model, the authors should co-localize PBPlipo with another divisome component

We performed a co-localization experiment with mRFP-PBP-lipo and FtsZ-mNeonGreen (mNG). Figure 5A shows co-localization of PBP-lipo and FtsZ in representative cells. In total, we analyzed a total of 100+ cells for each strain. We then used software developed in the lab (Junhao et al., 2022) to plot the septal fluorescence signal as a function of cell length for both PBP-lipo and FtsZ (Figure 6B).

This experiment showed that both FtsZ and PBP-lipo localize to the septum, with FtsZ localizing to the septum first. This result has been published in several bacteria. Finally, we showed that knockdown of PBP-lipo leads to the disruption of FtsZ localization, with cells forming multiple FtsZ rings spread throughout the length of the cell

6. The authors should Colocalise mRFP-PBP-lipo (if functional) with DacB1-GFP (if functional).

Figure 6 —figure supplement 4C shows co-localization of mRFP-PBP-lipo and DacB1-mNeonGreen Due to the toxicity of co-expressing dual tagged PBPs with fluorescent proteins, DacB1-mNeonGreen was expressed of a weak promoter to allow for the co-localization experiments to be performed

7. It is known that several bacteria have homologous PBPs that cannot fully replace each other and have specific roles under different growth conditions. The authors don't present or discuss such examples in their Discussion. The discussion should be expanded beyond mycobacteria to include examples from other species, such as:

– Salmonella has a dedicated class B PBP3 homologue (called PBP3-SAL) next to its 'normal' PBP3 required for cell division. PBP3-SAL is specifically required for cell division in acidified phagosomes (mBio. 2017 Dec 19;8(6):e01685-17. doi: 10.1128/mBio.01685-17).

– E. coli uses a specialised DD-CPase PBP6B to maintain cell morphology when growing under acidic conditions (mBio. 2016 Jun 21;7(3):e00819-16. doi: 10.1128/mBio.00819-16.).

Such examples can use used todiscuss whether PBP-lipo and its homologue might not be essential under certain growth conditions at which the homologue is highly active.

Thank you. We have added these points to the Discussion section.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Reviewers remain concerns about the experiments supporting the annotation of PBP-Lipo as a lipoprotein:

1. Please provide sufficient detail on the lipoprotein extraction procedure. The information is not available in Ref 26, which also appears to focus on Vibrio, rather than Mycobacteria.

The reference that details the lipoprotein extraction procedure is Ref 29, Armbruster and Meredith, 2018 (L193). The protocol details steps to generally extract bacterial lipoprotein without any specific focus on a bacterial species. A similar lipoprotein protocol extraction protocol was applied to mycobacteria (see reference 30 which is referred to below).

Included a brief description of the protocol was described in the Results section (L194-196) and a full description of the protocol was added in the Materials and methods (L787-805).

2. Results of the attempts to verify that PBP-lipo has a lipid modification are shown in Figure 3 —figure supplement 3B. However, this figure shows that the majority of PBP-lipo (>90%?) seems to segregate into the non-LP fraction. Quantification is not possible because the non-LP lane is overloaded but the results suggest the absence of a lipoprotein modification. The Methods section lacks sufficient information about this experiment (how were the LP and non-LP fractions obtained?), and there is no positive or negative control of a verified lipoprotein or non-lipoprotein. As a result, reviewers indicate that this experiment does not address the issue of the Lipo modification. You should either rename the enzyme, removing "lipo" from the name, or state very clearly in the manuscript that the lipo modification is hypothetical.

– Added ‘lipoprotein extraction’ section in the Methods section that details how the lipoprotein and non-lipoprotein fractions were obtained.

– Included a reference by Young and Garbe (Ref 30) where lipoproteins extracted from Mycobacterium tuberculosis were present both in the lipoprotein and non-lipoprotein fractions

– Given the valid critiques of the experiment, we have stated clearly in the manuscript, both in the abstract and during the first mentions of MAB_3167c in the introduction and Results sections, that the gene encodes a ‘penicillin binding protein and hypothetical lipoprotein’ (PBP-lipo). Furthermore, we added language stating that future experiments are needed to confirm if the protein is indeed lipidated.

– Edited the title of the manuscript by removing PBP-lipo. Title now reads “High-density transposon mutagenesis in Mycobacterium abscessus identifies an essential penicillin-binding protein involved in septal peptidoglycan synthesis and antibiotic sensitivity”

Other concerns:

L. 273: insert "genetic" in front of "PG network" in the heading.

Change made

L. 309: format problem.

Problem fixed

Figure 6 —figure supplement 5A. the y-axis should read "log (or ln?) fold change mRNA expression" instead of "fold change mRNA expression".

These changes were not plotted on a log scale, and so we have kept the y-axis title as ‘fold change mRNA expression.’ The same y-axis legend is used in Figure 3 —figure supplement 1B

L507: PbpB is 4-3 crosslinking enzyme. It does not necessarily follow that PBP-lipo must have the same activity. The ectopic complementation could be due to other crosslinks that also stabilize PG. Please reconsider this statement.

Changed language to “investigating the unique yet overlapping functions of PbpB and PBP-lipo at the Mab septum is an intriguing area of future research.” (L521-522)

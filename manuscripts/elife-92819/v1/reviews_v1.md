# Peer review - Round 1

Editors:
- Jennifer G DeLuca, Colorado State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92819.3.sa0](https://doi.org/10.7554/eLife.92819.3.sa0)

In this study, the authors develop a strategy for fluorophore-tagging endogenous proteins in human induced pluripotent stem cells (iPSCs) using a split mNeonGreen approach, and they conclude that the system will be appropriate for performing live imaging studies of highly dynamic cellular processes such as cytokinesis in iPSCs. Experimentally, the methods are solid, and the data presented support the authors' conclusions. Overall, these methodologies should be useful to a wide audience of cell biologists who want to study protein localization and dynamics at endogenous levels in iPSCs.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92819.3.sa1](https://doi.org/10.7554/eLife.92819.3.sa1)

Summary:

In this manuscript the authors have applied an asymmetric split mNeonGreen2 (mNG2) system to human iPSCs. By integrating a constitutively expressed long fragment of mNG2 at the AAVS1 locus, this allows other proteins to be tagged through the use of available ssODN donors. This removes the need to generate long AAV donors for tagging, thus greatly facilitating high-throughput tagging efforts. The authors then demonstrate the feasibility of the method by successfully tagging 9 markers expressed in iPSC at various, and one expressed upon endoderm differentiation. Several additional differentiation markers were also successfully tagged but not subsequently tested for expression/visibility. As one might expect for high-throughput tagging, a few proteins, while successfully tagged at the genomic level, failed to be visible. Finally, to demonstrate the utility of the tagged cells, the authors isolated clones with genes relevant to cytokinesis tagged, and together with an AI to enhance signal to noise ratios, monitored their localization over cell division.

Strengths

Reviewer Comment: Characterization of the mNG2 tagged parental iPSC line was well and carefully done including validation of a single integration, the presence of markers for continued pluripotency, selected off-target analysis and G-banding-based structural rearrangement detection.

The ability to tag proteins with simple ssODNs in iPSC capable of multi-lineage differentiation will undoubtedly be useful for localization tracking and reporter line generation.

Validation of clone genotypes was carefully performed and highlights the continued need for caution with regards to editing outcomes.

Weaknesses

Reviewer Comment: IF and flow cytometry figures lack quantification and information on replication. How consistent is the brightness and localization of the markers? How representative are the specific images? Stability is mentioned in the text but data on the stability of expression/brightness is not shown.

Author Response: To address this comment, we have quantified the mean fluorescence intensity of the tagged cell populations in Fig. S3B-T. This data correlates well with the expected expression levels of each gene relative to the others (Fig. S3A), apart from CDH1 and RACGAP1, which are described in the discussion.

Reviewer Reply: Great, thanks.

Reviewer Comment: The localization of markers, while consistent with expectations, is not validated by a second technique such as antibody staining, and in many cases not even with Hoechst to show nuclear vs cytoplasmic.

Author Response: We find that the localization of each protein is distinct and consistent with previous studies. To address this comment, we have added an overlay of the green fluorescence images with brightfield images to better show the location of the tagged protein relative to the nuclei and cytoplasm. We have also added references to other studies that showed the same localization patterns for these proteins in iPSCs and other relevant cell lines.

Reviewer Reply: There was no question that the localization fit with expectations, however, this still doesn't show that in the same cell the tag is in the same spot. It would have been fairly simple to do for at least a handful of markers, image, fix and stain to demonstrate unequivocally the tag and protein are co-localized. Of course, this isn't damning by any means, it just would have been nice.

Reviewer Comment: For the multi-germ layer differentiation validation, NCAM is also expressed by ectoderm, so isn't a good solo marker for mesoderm as it was used. Indeed, the kit used for the differentiation suggests Brachyury combined with either NCAM or CXCR4, not NCAM alone.

Author Response: Since Brachyury is the most common mesodermal marker, we first tested differentiation using anti-Brachyury antibodies, but they did not work well for flow cytometry. We then switched to anti-NCAM antibodies. Since we used a kit for directed differentiation of iPSCs into the mesodermal lineage, NCAM staining should still report for successful differentiation. In the context of mixed differentiation experiments (embryoid body formation or teratoma assay), NCAM would not differentiate between ectoderm and mesoderm. The parental cells (201B7) have also been edited at the AAVS1 locus in multiple other studies, with no effect on their differentiation potential.

Reviewer Reply: This is placing a lot of trust in the kit that it only makes what it says it makes. It could have been measured by options other than flow such as qPCR, Western blot, or imaging, but fine.

Reviewer Comment: Only a single female parental line has been generated and characterized. It would have been useful to have several lines and both male and female to allow sex differences to be explored.

Author Response: We agree that it would be interesting (and important) to study differences in protein localization between female and male cell types, and from different individuals with different genetic backgrounds. We see our tool as opening a door for cell biology to move away from randomly collected, transformed, differentiated cell types to more directed comparative studies of distinct normal cell types. Since few studies of cell biological processes have been done in normal cells, a first step is to understand how processes compare in an isogenic background, then future studies can reveal how they compare with other individuals and sexes. We hope that either our group or others will continue to build similar lines so that these studies can be done.

Reviewer Reply: Fair enough.

Reviewer Comment: The AI-based signal to noise enhancement needs more details and testing. Such models can introduce strong assumptions and thus artefacts into the resolved data. Was the model trained on all markers or were multiple models trained on a single marker each? For example, if trained to enhance a single marker (or co-localized group of markers), it could introduce artefacts where it forces signal localization to those areas even for others. What happens if you feed in images with scrambled pixel locations, does it still say the structures are where the training data says they should be? What about markers with different localization from the training set. If you feed those in, does it force them to the location expected by the training data or does it retain their differential true localization and simply enhance the signal?

Author Response: The image restoration neural network was used as in Weigert et al., 2018. The model was trained independently for each marker. Each trained model was used only on the corresponding marker and with the same imaging conditions as the training images. From visual inspection, the fluorescent signal in the restored images was consistent with the signal in the raw images, both for interphase and mitotic cells. We found very few artefacts of the restoration (small bright or dark areas) that were discarded. We did not try to restore scrambled images or images of mismatched markers.

Reviewer Reply: I understand. What I'm saying is that for the restoration technique to be useful you need to know that it won't introduce artefacts if you have an unexpected localization. Think of it this way, if you already know the localization, then there's no point measuring it. If you don't, or there's a possibility that it is somewhere unexpected, then you need to know with confidence that your algorithm will be able to accurately detect that unexpected localization. As such, it would be extremely important to validate that your restoration algorithm will not bias the results to the expected localization if the true localization is unexpected/not seen in the training dataset. It would have been extremely trivial to run this analysis and I do not feel this comment has been in any way adequately addressed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92819.3.sa2](https://doi.org/10.7554/eLife.92819.3.sa2)

Summary:

The authors have generated human iPSC cells constitutively expressing the mNG21-10 and tested them by endogenous tagging multiple genes with mNG211 (several tagged iPS cell lines clones were isolated). With this tool they have explored several weakly expressed cytokinesis genes gained insights into how cytokinesis occurs.

Strengths:

(i) Human iPSC cells are used

Weaknesses:

(i) The manuscript is extremely incremental, no improvements are present in the split-Fluorescent (split-FP) protein variant used nor in the approach for endogenous tagging with split-FPs (both of them are already very well established and used in literature as well as in different cell types).

(ii) The fluorescence intensity of the split mNeonGreen appears rather low, for example in Figure 2C the H2BC11, ANLN, SOX2 and TUBB3 signals are very noisy (differences between the structures observed are almost absent). For low expression targets this is an important limitation. This is also stated by the authors but image restoration could not be the best solution since a lot of biologically relevant information will be lost anyway.

(iii) there is no comparison with other existing split-FP variants, methods, or imaging and it is unclear what the advantages of the system are.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92819.3.sa3](https://doi.org/10.7554/eLife.92819.3.sa3)

The authors report on the engineering of an induced Pluripotent Stem Cell (iPSC) line that harbours a single copy of a split mNeonGreen, mNG2(1-10). This cell line is subsequently used to take endogenous protein with a smaller part of mNeonGreen, mNG2(11), enabling complementation of mNG into a fluorescent protein that is then used to visualize the protein. The parental cell is validated and used to construct several iPSC line with endogenously tagged proteins. These are used to visualize and quantify endogenous protein localisation during mitosis.

I see the advantage of tagging endogenous loci with small fragments, but the complementation strategy has disadvantages that deserve some attention. One potential issue is the level of the mNG2(1-10). In addition, this may probably not work for organelle-resident proteins, where the mNG2(11) tag is localised in a membrane enclosed compartment.

Overall the tools and resources reported in this paper will be valuable for the community that aims to study proteins at endogenous levels.

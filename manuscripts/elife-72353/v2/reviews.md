# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72353.sa0](https://doi.org/10.7554/eLife.72353.sa0)

This study uses CryoEM and biochemical studies to uncover a new and potentially important conformational off-state of a key regulatory multi-subunit protein kinase, SMG1. The study was enabled by applying a small molecule ATP-site inhibitor to capture the structure. The work will be of wide interest to the signaling and structural biology communities.


---

# Peer review - Round 1

Editors:
- Philip A Cole, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72353.sa1](https://doi.org/10.7554/eLife.72353.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Cryo-EM reconstructions of inhibitor-bound SMG1 kinase reveal an autoinhibitory state dependent on SMG8" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Reviewing/Senior Editor (Philip Cole). The following individual involved in review of your submission has agreed to reveal their identity: Kacper B Rogala (Reviewer #1).

The Reviewing Editor has drafted this to help you prepare a revised submission. Although there are a substantial number of points listed below, the vast majority relate to manuscript presentation and writing issues rather than requested additional experimentation.

Essential revisions:

1. A significant concern with the manuscript is that there is no clear way to test the autoinhibition model. UPF1 binding itself is proposed to relieve autoinhibition, meaning that activity towards UPF1 would not be a readout of autoinhibition. One possible prediction of the model would be that activity of the complex toward a short peptide including the UPF1 phosphorylation sites should be low due to occlusion of the SMG1 catalytic cleft. Addition of an UPF1 truncation mutant lacking the C-terminal tail would be expected to activate the SMG1 complex toward phosphorylation of a peptide substrate. The SMG1-SMG9 dimer is modestly more active on UPF1 than the full SMG1-SMG8-SMG9 heterotrimer (see the Deniaud et al. paper cited in the text). However, using a peptide substrate, that difference in activity would be expected to us to be much larger. It would make the model more powerful if such ancillary enzymatic evidence were included.

2. Figure 1. Phosphorylation assays presented in this figure are missing an important control. And that is the reaction without the enzymes – for both SMG1 and mTOR. It is difficult to judge the extent of SMG1i inhibition if we cannot see the baseline with and without the enzymes. In general, monitoring of the AKT1 peptide phosphorylation with this method seems rather noisy, and this reviewer is unsure how relevant that specificity data is in the absence of proper controls. The same method presented in the authors' earlier paper (Gat et al., 2019, PMID: 31792449) seemed to be of higher quality.

3. Figure 1 is presented as providing evidence that SMG1i is selective for SMG1 over mTOR, and that it works by an ATP competitive mechanism. None of the experiments in Figure 1 or the associated supplementary figures actually investigate whether the compound is ATP-competitive; this was established later by the cryo-EM structure. It is worth noting that a non-selective analog bound at the ATP binding site when co-crystallized with PI3K-γ (reported in the paper that described SMG1i). Furthermore, in that original work, SMG1i was reported to be >400-fold selective for SMG1 over mTOR, and it was also tested against a number of other kinases. From this standpoint Figure 1 should be acknowledged as being confirmatory to that prior work rather than a new result, and it could be moved to a supplemental figure. There are also some technical issues with those experiments – the mTOR kinase assays used for replicates cover only a narrow concentration range and have high background; it's not clear why the full dose response shown in Figure 1 S2A wasn't simply repeated three times. The SMG1 activity assays were also performed at high kinase concentration, so the true potency of the compound cannot be determined. The original paper reported sub-nM inhibition of SMG1.

4. PRD density in the apo vs inhibitor/AMPPNP-bound mode of the SMG1-8-9 complex. The authors do not seem to offer any visual cues or thoughts to better understand why the PRD density would only rigidify in the presence of the inhibitor or ATP analogs. And within that group – why would the PRD density be more pronounced in the presence of the inhibitor versus the ATP analog? Are there any conformational changes in the SMG1-8-9 complex upon binding of the inhibitor/AMPPNP? Can the authors trace any specific residue/domain movement and rationalize this observation?

5. Methods. For the references cited in the methods, please use the primary articles on which the technique is developed rather than a subsequent paper that cites the original reference.

6. The presented structural data is clearly of high quality but additional figure panels covering the process of cryo-EM data processing in greater detail should be produced:

a. Representative micrograph of collected cryo-EM data.

b. 2D classes of their cryo-EM data.

c. Angular distribution plot for each deposited reconstruction in addition to their 3D FSC plot.

d. FSC plots for map vs. model.

7. Crosslinking-MS analysis on the SMG1-SMG8-SMG9 complex (as well as the complex including UPF1) was also previously done, and provided largely similar results to those reported in Figure 4B. Though not the intention of the authors, the use of bold lines for the highlighted crosslinks suggests that those specific interactions were identified at higher confidence or provided a higher signal; just keeping with the color scheme would be sufficient for the purpose of drawing attention to those crosslinks. In addition to the groove that approaches the IP6 binding site where additional density is seen in the inhibitor bound complex, the C-terminus of the insert region also crosslinks at multiple points within the catalytic domain itself. Can the authors reconcile the observed crosslinks to both regions?Reviewer #1 (Recommendations for the authors):

Claims/Observations:

(1) The SMG1i compound is specific to SMG1 because it engages unique residues in the active site (unique to SMG1 versus other PIKKs). Beyond the structural rationale provided by solid cryo-EM work, the authors attempted to strengthen this claim with in vitro kinase assays.

This reviewer believes that this data is of high value, but some controls for the in vitro kinase assays are missing and should be addressed to support this claim. Please see the detailed comments section.

(2) Structural rationale for the autoinhibitory function of the insertion domain of SMG1 and the C-terminal section of SMG8 – on the overall activity of the SMG1-8-9 complex.

Putative density belonging to the insertion domain (specifically its N-terminal section) is found in the active site of SMG1 – occluding the previously-mapped SQ substrate binding site, and explaining the previously-reported autoinhibitory function of this domain. Corresponding density has been observed in other PIKKs, and is normally referred to as PRD for PIKK regulatory domain. The authors were unable to unambiguously assign the amino-acid register for the putative PRD density due to its rather weak resolution. Their cross-linking mass spectrometry work confirmed that the insertion domain makes many contacts with the FATKIN domain of SMG1, and an extra few cross-links with the C-terminus of SMG8. in vitro binding assays with purified SMG1-insertion-domain and SMG8-C-terminus confirmed direct binding between these two regions of the complex, offering an explanation as to why the PRD section of the insertion domain is only rigidified in the context of the full SMG1-8-9 complex, and not the sub-complex lacking SMG8. They conclude that SMG8 stabilizes the PRD inside the SMG1 substrate binding site.

Given the wide range of methods applied to support this claim, this reviewer finds the evidence rather compelling. There are some points that should be addressed – either to clarify some statements or to expand on them. Please see the detailed comments section.Reviewer #2 (Recommendations for the authors):

Langer et al., present cryo-EM reconstructions of the PIKK family SMG1-9 and SMG1-8-9 kinase complexes bound to a SMG1 inhibitor or to an ATP analogue at sub-4 Å resolutions. Together, these structures show (1) the molecular interactions that define the specificity of a SMG inhibitor and (2) reveal an autoinhibitory function of the SMG1 insertion domain. Additional biochemical and cross-linking mass spectrometry work shows interactions between the SMG1 insertion domain and the SMG8 C-terminus. It clarifies how the SMG1 insertion domain and the SMG8 mediate autoinhibition of SMG1. Additionally, the authors show that the employed inhibitor has a high specificity for the inhibition of SMG1 in vitro.

The manuscript is written very clearly. The authors' data is overall well-presented and represents the first structure of SMG1 bound to an inhibitor. The presented structural data is of high quality and appears plausible. Together, the authors' claims are supported by the presented data but additional figures and expansion of the methods section to present their cryo-EM data analysis in greater detail will increase overall clarity.

Reviewer #3 (Recommendations for the authors):

The SMG1-SMG8-SMG9 kinase complex phosphorylates the protein UPF1 to promote nonsense-mediated mRNA decay, an essential co-translational quality control mechanism for degradation of messages with premature stop codons. This manuscript from Langer et al. describes cryo-EM structures of the SMG1-SMG8-SMG9 complex bound to a selective ATP-competitive small molecule inhibitor. The structure provides a rationale for why the compound is selective for SMG1 over related kinases such as mTOR and DNA-PK, which should prove useful in furthering inhibitor design and development for this class of kinases. Intriguingly, the inhibitor bound structure revealed additional density absent from prior reconstructions of the complex arising from am "SMG1 insertion region" C-terminal to its catalytic domain. While this density could not be fit to an atomic model, a portion of it occludes the catalytic cleft, suggesting that it mediates cis-autoinhibitory regulation of the kinase. Furthermore, this region appears to contact the SMG8 subunit, and the added density is absent from cryo-EM reconstructions of an SMG1-SMG9 complex lacking SMG8. Both the SMG1 intramolecular contacts and SMG1-SMG8 intermolecular contacts were supported by crosslinking-mass spectrometry analysis, which appeared largely similar to a previously reported analysis using the same method. These observations support a model by which SMG8, through direct interactions with the SMG1 insertion region, has a key role in autoinhibition of the kinase. These studies are important for the field in that how the SMG1 complex is regulated has previously been obscure. A weakness of the study is this structural hypothesis could not be independently tested. Indeed, given that the SMG1 insertion region was not observed at high resolution, it would not be possible to design mutants to disrupt key interactions and examine their impact on SMG1 kinase activity. The authors hypothesize that these autoinhibitory interactions are relieved by substrate binding, which is consistent with prior cryo-EM characterization of the SMG1-SMG8-SMG9-UPF1 complex. However, this potential substrate activation mechanism, while plausible, is not directly addressed in the manuscript.

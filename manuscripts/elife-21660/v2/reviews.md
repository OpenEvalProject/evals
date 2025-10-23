# Peer review - Round 1

Editors:
- Lothar Schermelleh, University of Oxford , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21660.021](https://doi.org/10.7554/eLife.21660.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Super-resolution imaging of a 2.5-kb non-repetitive DNA in situ in human genome using molecular beacon probes" for consideration by eLife. Your article has been reviewed by four peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lothar Schermelleh (Reviewer #1).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While all reviewer found the presented method of potential value for the community, they also agree that detection of an endogenous locus is an absolute requirement for showing the utility and the specificity of the method. There was also a common concern about the lack of detail on the efficiency of the approach and the protocol itself.

Whilst we are rejecting the paper for now due to the amount of work that needs done, we would be happy to receive a revised paper as a new submission once all the reviewers' concerns have been addressed. Please note that in this case eLife cannot guarantee that a resubmitted paper will be accepted and that it is the authors' choice whether to submit their manuscript to another journal instead of performing the additional work.

Reviewer #1:

Ni et al. present a novel "molecular beacon" fluorescence in situ hybridization (MB-FISH) method, that reduces genomic target size down to 2.5 kb, about half of the previously best DNA-FISH approaches. They achieve this by tailoring synthetic oligonucleotide probes with a quencher – fluorophore pair at opposite ends flanked by short complementary sequences. By this smart trick, probes only fluoresce upon hybridisation with the target sequence, while unbound probes remain largely non-fluorescent, thus reducing unspecific background and improving signal to noise.

As the method was developed with super-resolution 3D-STORM imaging in mind, the authors also devise an improved protocol for STORM imaging of sparse target labeling, which is a very useful add-on to this paper.

The presented MB-FISH method will without doubt generate considerable interest in the field. The experimental logic, technical execution, data quality and conclusions are largely sound. The manuscript itself is clearly presented and written concisely. However, I feel that the following issues need to be addressed first to firmly justify publication in eLife's Tools & Resources section.

Major comments:

As proof-of-principle the authors use their MB-FISH approach to detect a randomly integrated transgenic sequence encoding for eGFP linked to a strong constitutive CMV promoter. While this is a very suitable approach to have a clean negative control to compare with, it does not show how reliable the method is in detecting true endogenous sequences. Furthermore, CMV-driven constitutive expression will likely render the underlying chromatin highly decondensed and accessible. What is the ability of MB-FISH to detect non-expressed sequences of the same size?

Hence, in order to convey full confidence in this new method, the authors need to demonstrate the detection of one, or preferably a few, endogenous target sequences, ideally representative for different classes (genic, intergenic, expressed, non-expressed).

Reviewer #2:

This paper describes the application of molecular beacon probes to super-resolution imaging by STORM. The authors optimised hybridisation temperature in solution using complementary sequence. They optimised imaging conditions by exposing fixed and permeabilised cells to Alexa 647-tagged 10nt oligos followed by wash and fix to leave sparse Alexa 647 signals for imaging and establishment of the resolution achieved. Finally they present example STORM images of the transfected viral sequences.

This is a straightforward technical paper describing the smallest unique sequence yet detected by super-resolution imaging, and as such the method deserves to be published. I do have suggestions however that will hopefully improve the manuscript. I do not have the expertise to properly assess the home-built STORM system and image reconstruction – hopefully another reviewer will address this.

Major Comments

The target DNA of 2.5kb is not endogenous human but viral CMV plus eGFP. This will minimize the background. It would be helpful to include detection of a human sequence to indicate sensitivity within a more likely experimental situation.

Similarly, I was surprised that the imaging optimisation was done on the 'sparse Alexa 647' preps rather than hybridized signal and it would be helpful to have some rationale here. What was the 10nt sequence used and why? Does each cluster imaged represent a single fluorophore? The images should be presented.

I would like to see more examples of the MB signals (I could not access the repository) and more discussion of how true signals were distinguished from unbound/off target signal. For example, comparing the yellow signals in Figure 4B and Figure 5A, 3rd row – how were they distinguished as non-specific or specific signal?

Controls other than the blank cells should be included e.g. scrambled oligos.

I felt that the Discussion lacked depth. There was disappointingly no discussion of the nanostructures imaged. Are any of these cells in G2? Some more discussion of appropriate fluors and schemes for multi-colour analysis would also be appreciated.

The paper does need to be overhauled by a native English speaker. There are several points of confusion, for example at the end of the Discussion on reference to Hogan et al., 2015. Do they mean that Hogan used molecular beacons or that this would be a suitable application?

Finally (and this is an observation directed not only at this paper), how can the authors be certain that nanostructures imaged after cycles of freeze-thaw will accurately represent three-dimensional chromatin conformation in the nucleus?

Reviewer #3:

Chromatin topology within the nucleus plays an important role in many biological processes such as enhancer-promoter contacts during gene expression. In this manuscript, the authors developed a super-resolution imaging method to visualize a 2.5-kb non-repetitive DNA in situ in human cells using molecular beacon (MB) probes. They first analyzed the efficiency of 29 MB probes targeting a 2.5-kb exogenous DNA fragment by comparing the probe fluorescence with excessive amount of complementary sequences or non-complementary sequences under different conditions. Second, they optimized conventional STORM imaging conditions to identify signals of sparse Alexa-647 from the background. Finally, they reconstructed nano-structures of the 2.5-kb non-repetitive DNA in situ in the human genome. To be useful for investigating chromatin looping contacts, at least two DNA elements need to be visualized at the same time. Nevertheless, this is a significant study, if true, may represent the shortest DNA fragment visualized to date in the human genome.

My major concern is that whether the method could truly detect nano-structures of the 2.5-kb endogenous non-repetitive DNA in situ in the human genome. Because the viral DNA could be randomly integrated into the human genome, it is not clear how the authors could use PCR to detect single copy insertions. In theory, DNA could be integrated in multiple tandem copies in random loci, there is not enough information how the authors designed PCR primers. A PCR band of around 3.3 kb rather than folds of the size is not strong evidence for single-copy insertion.

Major points:

1) Whether the non-complementary sequences could mimic the true off-targets in MB binding? It is difficult to design non-complementary sequences sharing 5-15 nucleotides with individual MBs to mimic many possible off-target MB bindings.

2) Whether the frame rate of 85 Hz and power of 0.5 mW 405-nm laser and 29 mW 641-nm laser are the best optimized condition since the values of blank cells are very low for calculating FDR? In addition, in Figure 2D, 0.04 ± 0.02 basically means there is no auto-fluorescence.

3) It would be useful if the authors could show that the method could be used to study an enhancer-promoter or promoter-promoter looping contact as a proof-of-principle.

Reviewer #4:

In their manuscript, Zhang et al. develop a FISH approach based on molecular beacons that can be used to label short (2.5kb) non-repetitive regions of genomic loci for 3D super-resolution imaging. The approach is interesting and can provide a simpler method of labeling non-repetitive sequences compared to Oligopaint approach. However, I have major concerns about the specificity of the probes and the validity of the method (see comments below):

Major comments:

1) The major weakness of the manuscript is the use of cells with random integration instead of a more controlled system. This choice makes it difficult to truly assess the specificity of the approach. The authors should have used a system of site specific integration (for example: CRISPR-Cas9, FlpIn recombination, Integrations in R26 locus). Alternatively, the authors could have targeted an endogenous region and use as control the knockout counterpart. Wild type vs KO cell lines are available for a variety of genes or can be generated with CRISPR-Cas9. In these systems the authors should detect a number of loci compatible with the ploidy of the cell. In addition, in such a system the authors can confirm the specificity of the molecular beacons by labeling the same genomic locus with an alternative method such as regular FISH. In the absence of these experiments, the specificity of the molecular beacons remains unconfirmed and not convincing from the provided data.

2) The manuscript is also largely descriptive and lacking quantitative information to back up the major claims. For example, was the viral MOI (multiplicity of infection) assessed? From this value at least a range of expected integration sites could be estimated and compared to the super-resolution data.

The authors should also provide more information regarding the efficiency of their approach:

– what is the percentage of GFP positive cells with detectable loci?

– what is the average number of detected loci? Is this number in line with the viral MOI used?

– what is the average and range of detected localisations per locus?

In general, representative images should be supported with more quantitative data based on the complete dataset of cells imaged. It would also be useful to provide unzoomed images to appreciate the general signal to noise ratio in the whole ROI.

3) When comparing MB-FISH to Oligopaints, the authors should further discuss the differences/similarities between the two approaches:

– can MB-FISH provide allele specificity and is it sensitive to SNPs.?

– what is the optimal probe density required for MB-FISH?

– are there specific requirements in terms of spacing between probes, strand specific orientation, etc?

– would this approach be compatible with live imaging?

4) The usage of English language in the manuscript needs substantial improvement. The grammatical errors and awkward sentences are far too many to point out one by one in this review.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Super-resolution imaging of a 2.5 kb non-repetitive DNA in situ in the nuclear genome using molecular beacon probes" for further consideration at eLife. Your revised article has been favorably evaluated by Jessica Tyler (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #1:

The authors addressed most issues raised in my first review. However to meet the highest standards of eLife, a few minor issues still need to be resolved:

1) Sections of the manuscript have become somewhat cluttered and difficult to digest, in part by addressing the reviewers' additional requests. For instance, experimental details in the Results section (e.g. cloning controls) could potentially be moved to the Methods section. Also the Discussion could be streamlined (see also point 3). Generally I feel the manuscript would benefit from another round of decluttering/shortening to present this excellent work in the most concise and clearest way.

2) I am still not entirely clear how to interpret the success rate of 21/78 and 14/92 cells with detected nanostructures. Does this reflect the limitation of the STORM imaging method to be able of imaging only a sub-volume of a mammalian nucleus? Or does is reflect (also) a lowered detection efficiency of the FISH method. Or is it a combination of both? What is the chance of detecting positive cells, if one assumes one, two (or more) loci, if the detection would be 100% efficient? The authors may still need to clarify this better.

3) The use of language needs improvement (particular in the revised Discussion).

Reviewer #2:

The majority of my questions have been answered, in particular the authors have analysed an endogenous locus. However there remain outstanding issues that require explanation and/or addressing in the text for me to feel confident of the validity of the signals presented. Criteria for image analysis and some of the data produced do not appear to be presented fully.

1) Response to Reviewer 2 Point 6: In fact the Markaki 2012 paper clearly states (page 415, last paragraph): "In agreement with our visual impression, the IC space was reduced in 3D-FISH-treated nuclei and a shift toward higher intensity classes. […] We also consider the possibility that some swelling or dispersal of chromatin, in particular as a result of the heat denaturation step [18], resulted in an improved accessibility of DNA to this fluorophore." Please could the authors clarify this point in the Discussion.

2) Results and Figure 4: I wondered why the beads (F8810 580/605) were visible at 405nm and occasionally at 641nm?

3) Results subsection “Super-resolution visualization of 2.5 kb enhancer in situ in Nanog locus of mouse ESCs” and Figure 5—figure supplement 1: It is not clear what point the authors are making about the nuclear periphery sitting close to the cell surface. Please clarify.

4) Figure 4: What is the blue dot in Cell I E?

5) Figure 5 Panel C Cell V: The position of the nanostructure in the box in C at low resolution does not appear to be the same as in D. Please explain.

6) Results: The authors provide statistical data on larger series than the 14/92 ESCs and the 21/78EGFP cells. Why are the numbers in the larger series not provided?

7) Discussion paragraph three: Please give the limits in localisation number and area that were used as criteria for defining nanostructures.

8) Discussion paragraph five: This explanation could perhaps be clarified.

9) Discussion paragraph six: The authors could perhaps refer to Ricci et al. here (PMID: 25768910).

Reviewer #3:

In the revision, the authors have performed additional experiments to show the proof-of-principle usage of their MB-FISH method. First, they have visualized a 2.5 kb non-repetitive endogenous DNA in situ in the human genome. Second, they have tested the method on a 2.5 kb super-enhancer at -45 kb upstream within the Nanog locus in mouse embryonic stem cells. As super-enhancers are clusters of enhancers which are located physically close in a 3D genome, the MB-FISH may be useful to study gene expression in the future. Finally, they applied CRISPR/Cas9-mediated knockout in mESCs to generate the homozygous knockout (HoKO) cells for the negative control experiments of the super-enhancer MB-FISH, in which a 3 kb region covering the super-enhancer target is deleted from both mouse alleles. Thus, the authors have largely addressed my concerns.

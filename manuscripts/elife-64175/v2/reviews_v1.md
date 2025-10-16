# Peer review - Round 1

Editors:
- Brandon K Harvey, NIDA/NIH United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64175.sa1](https://doi.org/10.7554/eLife.64175.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The study entitled "scAAVengr, a transcriptome-based pipeline for quantitative ranking of engineered AAVs with single-cell resolution" by Öztürk et al. describes a method of engineering and identifying adeno-associated viral vectors capable of delivering a transgene to a desired tissue of interest. Using the simian retina as a model, the authors detail their "pipeline" that relies on single cell transcriptome analyses of AAV-transduced cells identified by AAV-encoded green fluorescent protein. The "scAAVengr" technique has the potential to further broaden the available tissue and cell-specific AAV vectors and aid studies developing gene-based therapeutics.

Decision letter after peer review:

Thank you for submitting your article "scAAVengr, a transcriptome-based pipeline for quantitative ranking of engineered AAVs with single-cell resolution" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Huda Zoghbi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The study entitled "scAAVengr, a transcriptome-based pipeline for quantitative ranking of engineered AAVs with single-cell resolution" by Öztürk et al. describes an approach of engineering and identifying the most efficient AAV capsid/s within a small-scale rAAV library using a barcoded GFP reporter. The approach ("pipeline") relies on a single cell transcriptome analysis of GFP(+), rAAV-transduced cells in simian retina. The analysis assigns a particular internal barcode (capsid's identity) to a particular cell type (external barcodes) constituting retina tissue. The frequency of the respective NGS reads is directly corelated to the capsid transduction efficiency. The approach is indeed a significant technological step forward allowing a reduction in animal use while advancing bioinformatics as a viable and less expensive alternative. The former argument, however, if taken to its extreme, could be counter-productive since, as authors themselves noted (lines 65-66), animals vary, and reducing their number may skew the outcome in favor of a particular animal idiosyncrasies. This paper is of potential interest to a broad audience of investigators studying AAV vectors for therapeutic uses. The scAAVengr technique described is promising, although has not been completely characterized with regard to the number of AAV vectors that can be accurately tested or the use of the approach to study AAV transduction of other organs or tissues beyond the retina.

Essential revisions:

1) Although the technique described is promising, additional characterization is needed to know the number of AAV vectors that can be accurately tested as well as how useful the system is for targeting other tissues beyond retina. For example, the authors suggest that the 17 pooled AAV vectors did not compete with each other to transduce retinal cells, and cite the finding that a small number of sequenced cells were infected with multiple AAVs to support this hypothesis, as shown in Figure 5. But, Figure 5 also shows that the great majority of retinal cells sequenced were infected with a single AAV serotype. Thus, it is not clear that AAVs did not compete. Or does this indicate that most of the "single serotype cells" are the result of a transduction event with a single viral genome? Or that most transduced cells are specifically selective for a specific capsid? Further studies using different numbers of AAV serotypes are needed to address this issue. Similarly, testing scAAVengr in another tissue/organ type would be helpful to demonstrate the potential application of scAAVengr to studies beyond the retina. Alternatively, the paper could be modified to refocus on the use in the retina and data acquired from this focused approach.

(2) One of the major concerns is the description of the pooled, "titer-matched" GFP-barcode libraries (line 506). If, after deep sequencing of the control injected mixture the "relative abundance" of the pool was between ~2.65E+11 – 6.58E+11 vg/ml (~2.5-fold difference, not robust, but within experimental titering error), the resulting "dilution factors" were determined to be in the range of ~14-fold (AAV9 to AAV1). Which of these is correct? If appears the actual NGS read data were normalized by the factor of 14 for AAV1/NHP9 in order to compare them to AAV9. If this was how the data was corrected, is it valid? Once can envision several scenarios (e.g. titer-dependent capsid concentration gradient across the vitreous) for the data misinterpretation.

(3) The manuscript is focused on the scAAVengr method and evaluation of the data described regarding the transduction of retinal cell types with the AAV vectors tested needs to be included in the discussion. For example, why did the K912 vector identified through the DE experiment performed in dogs outperform the NHP vectors in transducing outer retinal cells in the primate experiments reported? Further, what does the finding that the best AAV vectors derived from DE experiments designed to identify vectors that can transduce retinal photoreceptor cells transduced only a small fraction of these cells in the experiments reported? Does it suggest that the barriers to retinal penetration by AAV vectors cannot be overcome by modification of the AAV capsid alone? These are important topics that can inform readers regarding the potential uses of the scAAVengr method and need to be included in the discussion.

(4) There were multiple differences between results obtained in marmoset vs. macaque eyes. For example, more cells were infected in marmoset retinas compared to macaque retina, and fewer "co-infections" with multiple AAVs were detected in macaque retinal cells than marmoset cells. It would be helpful for the authors to discuss the reasons for this, and the related implications for using the scAAVengr method in other organs.

(5) The main combinatorial library, 10-mer amino acid insertion at ~588, is not consistent with several instances describing it as a 7-mer insertion (lines 406, 417, 462 etc). This discrepancy needs addressed.

(6) Normalizing frequencies of the DE-evolving variants to the starting plasmid library (line 107) does not seem to be the best way to follow the enrichment due to the noise from the dead-end non-packaged variants. The original packaged library (Round 0) may be the better common denominator to follow DE enrichment.

(7) The figures used in the manuscript are helpful for presenting the complex data described, but took significant effort to interpret. Inclusion of more complete descriptions of how to "read" the figures in the legends would be helpful.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "scAAVengr, a transcriptome-based pipeline for quantitative ranking of engineered AAVs with single-cell resolution" for consideration by eLife. Your article has been reviewed by 1 peer reviewer, and the evaluation has been overseen by a Reviewing Editor and Lu Chen as the Senior Editor. The reviewer has opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) It is not clear that the newly added experiments in 5B address transduction-competition related to K912. See Reviewer comment 1 for more details.

(2) Ensure consistency in referencing "pools, libraries, mixes" for clarity. See Reviewer comment for more details.

(3) Ensure consistency in referencing "barcodes". See Reviewer comment for more details.

Reviewers comments for the authors:

(1) The newly added experiments described in figure 5B do not really address transduction-competition in a context that is relevant to the main story (the intravitreal injection environment), and does not quantify the transduction events produced by the serotypes relevant to the main story (ie K912).

Example: if K912 was evolved for transduction (TD) of cells in the intravitreal environment, it may no longer be fit to TD HEK293. Therefore quantifying of the TD-efficiency of the would-be competitors is also warranted in order to demonstrate that the model is relevant. Please address this concern by further stating caveats/limitations of this data.

Without testing these variants singly, these experiments do not address whether AAV2's poor performance in the intravitreal environment in the context of the mixed library was due to direct (binding) competition by serotypes that were "more fit", or just AAV2 lack of suitability altogether.

(2) The overall body of work deals with many layers of "mixes, pools, libraries, etc." Phrasing and references to these various entities seemed inconsistent or ambiguous at times leading to significant confusion for this reviewer. I recommend that some space be given to explicitly defining the various groups/mixes/pools, and then maintaining that vocabulary throughout the text. (see line 824, 825. please provide definition of "cloned AAV library" vs "packaged library")

(3) Likewise, this work deals with several layers of "barcoding" (sorted cell barcode, mRNA unique molecular identifier, and viral payload (GFP barcode)). Again, phrasing and references to these various entities seemed inconsistent or ambiguous at times leading to significant confusion for this reviewer. Again, I recommend that some more space be given to definition and graphic representation.

One example of barcode related confusion: It appears that the "GFP barcoding" for variant serotypes do not allow for quantification of multiple infections by the same serotype. (That is for example: all K912 TD events are binned by the same unique barcode associated with the GFP payload, see line 471). This is different from the description of the barcoding of AAV2 in Figure 5C.

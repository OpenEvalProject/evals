# Author response - Round 1

Authors:
- Yangyu Wu ([ORCID: 0000-0001-8064-6132](https://orcid.org/0000-0001-8064-6132))
- Zhuyuan Chen
- Fred J Sigworth ([ORCID: 0000-0002-7178-8494](https://orcid.org/0000-0002-7178-8494))
- Cecilia M Canessa ([ORCID: 0000-0001-7316-5082](https://orcid.org/0000-0001-7316-5082))

## Response text

DOI: [10.7554/eLife.67115.sa2](https://doi.org/10.7554/eLife.67115.sa2)

Essential revisions:

1) Authors should evaluate the current quality of the model (bonds, angles, C-β deviations, etc), perhaps use web servers like MolProbity for inspection. It is important to carry out these analyses until satisfactory model statistics are obtained. In addition, the authors should provide a detailed table of statistics of data collection and model refinement, as it provides one simple reference that readers can easily access. The table also serves as a guide for readers to assess the limitations of the presented data.

Thank you for the suggestions, we have carried out the improved refinement and evaluation. We have added the table as a Figure 2-Table supplement 2.

2) The current coordinate file is of one protomer with no symmetry operators to generate the other two protomers around the three-fold axis of symmetry. The authors described that RELION was used for 3D classification and refinement (C3 symmetry). Please provide symmetry operators.

The symmetry operators are listed below.

3) For the parts of the manuscript where molecular interactions at the nanobody/channel interface are described, the authors should show maps, at least as a figure supplement.

We have added to Figure 3C the map density of the interface between Nb.C1 and hASIC1a. See Figure 3-C.

4) For the data described in Table 1: some example raw traces and pH-response curves should be shown. In addition, some description should be provided of for variance in replicate measurements of pH dependence or the Hill coefficient.

i) We have added representative examples of hASIC1a with Nb-GFP (control Nb directed against GFP) and hASIC1a with 10 nM Nb-C1 showing response to proton activation and steady state desensitization: Figure 3—figure supplement 5.

ii) Table I shows mean± SD values for all measurements. The original data is included in an Excel file as Source Data 2.

iii) Also added are representative traces and results of pH50a and pH50ssd of hASIC1a wildtype and hASIC1a-DDL and cASIC wildtype and cASIC+DL. The purpose of these experiments was to test whether residues DL have any functional effect on ASICs. The results show that deletion of DL in hASIC1a produces a shift of 0.08 pH units of the pH50ssd to more alkaline value (t-test p=0.008) whereas adding DL to cASIC shifts the pH50ssd by 0.07 pH units (p=0.005) to more acid value (Sherwood and Askwith, 2008). The raw data has been included in Source Data 2.

5) All reviewers agreed that it would be helpful to the narrative of the manuscript to compare and contrast the binding sites for Nb.C1, MitTX, and PcTx1, perhaps by adding an additional figure. It would be helpful to add some discussion providing a structural rationalization of why Nb.C1 can bind hASIC1a in an overlapping binding site, but not alter function.

i) We have added new paragraphs to the text (Lines 162-178) comparing the binding sites.

ii) We have added a new paragraph discussing the lack of functional changes (lines 293-296).

6) Data is not shown for certain assertions, such as that the signal for the hASIC1 with a deletion is decreased in ELISA assays (this was shown in immunofluorescence microscopy), or that the mouse ASIC1a shows weak interactions with the nanobody. Lines 139 and 189 refers to rat and mouse ASIC1a but that data is not shown.

In the first submission we showed IF with strong signal for hASIC1a wildtype but no signal when residues DL are deleted, and no signal with cASIC1. We have added to Figure 3—figure supplement 3 new IF confocal images of mASIC1a, mASIC2a and mASIC3 with Nb.C1. The new images show no reactivity with any of those channels, indicating high specificity of Nb.C1 to hASIC1a.

The sentence mentioning ELISA has been removed because we didn’t conduct purification of cASIC, mASIC1a, ASIC2a or mASIC3 proteins that are necessary for the respective ELISA assays. Instead, we used IF to demonstrate specificity of the Nbs.

We include results of ELISA in Source Data 1: raw data from 96-well plate readings that include Nbs C1 to H10.

7) Although recovery from the PcTx1 toxin is described as being more rapid than recovery from the fusion protein, the time constants of these processes are within 2-fold of each other (Figure 4K). The main difference between the recoveries is the plateau. One possible interpretation of this is that some of the fusion protein has been proteolyzed so that the recovery represents the behavior of two sub-populations: one of toxin without fused nanobody, and one with the fusion protein. Perhaps in agreement with this, the gel from the purification has lower molecular weight bands that may correspond to nanobody or toxin alone. The authors should discuss this possibility, and comment on whether any experiments were done to control for this.

The interpretation provided by the reviewers is very likely. In addition, it is possible that a fraction of PcTx is not well folded i.e., pairing of the six cysteines is incorrect diminishing toxin binding affinity of the fusion protein. We have added an explanation to the text starting at line 224.

8) The authors do not indicate whether the PcTx1-nanobody fusion is from multiple biochemical preparations or just a single protein prep. It is important to reproduce these results for toxin-fusions from multiple biochemical preps in order to understand the prep-to-prep reproducibility for measurements like the recovery plateau.

We were aware of this problem. Because our limited resources, the purification of each fusion protein was conducted only once. The amount of purified fusion proteins was sufficient for the functional experiments. This caveat is mentioned in the legend of Figure 5.

9) The authors focus on the C1 nanobody, but also mention results obtained with other nanobodies (the ones in the tree in Figure 1E). The authors state "Nb.C1 was selected on the basis of high-affinity, absence of modification of channel function and a profile of monodisperse hASIC1a protein in size exclusion…. (lines 106-108)". This suggests other nanobodies were screened for affinity, channel modification and peak dispersion. Also, lines 91-93, the authors mention other nanobodies which required permeabilization to bind. The data relating to affinity, channel modulation, SEC and immuno from other nanobodies should be included, not simply mentioned but never shown.

Actually, we did not screen all isolated clones by all the criteria listed above, that approach would have taken a lot of time and resources.

After the third panning, we used ELISA to identify the strongest positive phages. As indicated in Figure 1D, an arbitrary threshold was set to examine only phages with high intensity signal, others were not considered for the next step. Several dozens of clones highly positive in ELISA were selected for DNA sequencing. Most of the sequenced clones were repeats or they had very similar sequences; i.e., there were not dozens of different clones rather a few clones repeated many times. This result is expected and represents a successful selection by our panning strategy of high affinity clones versus weak binders. Some of the sequenced clones were eliminated because they did not produce high amount of protein. The finalist clones are shown in Figure 1E. We next used IF to select clones with reactivity to hASIC1a and low background. The group in blue gave the cleanest signal. The group in green was also very clean but because the epitope(s) is intracellular we did not pursue further characterization in this study. If one looks at the sequences of the blue group (Figure 1 supp 2), they are almost identical, they differ by only one or two residues. Members of this group were tested on channels expressed in cells by TEVC. We used first C1 and later D10 in hASIC1a purification. Both Nbs were very good for this task, so we settled for C1 for the rest of the study.

The original sentence has been modified to convey a correct summary of the criteria that finally selected Nb.C1 though is not an exact sequence of events in the selection process:

“Among the best binders initially screened, Nb.C1 was selected on the basis of high-affinity, low background, and absence of modification of channel function. Subsequently, Nb.C1 was added to large scale preparations of crude membranes…”

It is entirely possible, indeed very likely, that the library contains more ‘good nanobodies’ for other purposes; they could be isolated by modifying the panning strategy.

Regarding Nbs in the green group, we are pursuing other applications, but for this publication is irrelevant. For the moment the library remains in the freezer until we obtain funds to continue the work.

10) The authors should describe what criteria they use to identify nanobody Nb.C1 as "high affinity." Reporting a Kd value would be useful.

As explained in the answer to the previous question, a good strategy for screening the phage library is the best way to isolate high affinity and specific binders. We have conducted measurements of binding kinetics of Nb.C1 using SPR with a Biacore instrument (Figure 5-supplement 1)

11) Lines 102-104, the authors mention hASIC1a tends to give low yields and aggregates, thus making cryo em sample prep difficult. The C1 nanobody is presented as a solution to this. The authors should include some data of hASIC1a alone (gels, chromatographs, etc.) to illustrate that this was a problem. As it stands, the nanobody is a solution to a problem we never actually see. Also, it is unclear how the Sun 2020 hASIC1a structure paper was able to overcome this without the benefit of nanobodies. Do the authors have thoughts on this?

In our hands, purification of high quality hASIC1a expressed in HEK293F cells was challenging owing to aggregation, and when placed on grids, displayed strong orientation bias. Nb.C1 solve both problems. Representative examples of SEC profiles using 1% DDM or 1% Fos-choline14 are shown, along with a Western blot of hASIC1a protein from the three peaks as Figure 2—figure supplement 1. In the figure legend we note the differences between a well-behaved protein of Sun et al. and our protein.

12) The authors noted that SH-SY5Y was used for imaging as it contains endogenous hASIC1a. A figure is shown (Figure 4G) to demonstrate an inward current is elicited upon application of pH 6.0. Is this current amiloride-sensitive?

Yes. Noted in the figure legend.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. In Figure 5K, the datapoints obtained from the two constructs (rigid and flexible linker) should not be combined, since the reader cannot evaluate whether the constructs behave similarly. These should be shown as separate datasets in Figure 5K.

2. Performing a second biochemical purification of the nanobody/toxin fusion is important to evaluate the prep-to-prep reproducibility of the quantitative values reported for Figure 5J and 5K (point #8 in the original review). It needs to be established whether the fraction of current that is recovered is something that is consistent (and may be a property of the chimeric molecule being tested), or variable from prep-to-prep (and may be due to contaminating toxin not covalently linked to monobody). Related to point #1, separating the data obtained from the rigid and flexible linker could help address whether similar time constants and plateaus are observed for toxin-nanobody chimeras that have been prepared in independent batches (with the caveat that the constructs are not exactly the same). As an alternative, these data could be removed from the manuscript.

Answer to the above two comments. We made new preparations of fusion proteins (Nb.C1-FlexLinker-PcTx and Nb.C1-RigidLinker-PcTx) and repeated the koff measurements in oocytes with TEVC. The new data are presented in Figure 5K-L. There is a difference in the maximal inhibition (16% and 14%) between the two constructs. The Coomassie blue SDS-PAGE shows (Figure 5J) a small fraction of cleaved protein -more prominent in the flexible linker fusion- that we believe may account for the more rapid than expected koff, as it generates free toxin. Though we optimized the purification protocol for these preps (lower temperature during induction, shorter incubation, addition of protease inhibitors and small concentration of reducing agents, indicated in methods), the cleavage was not completely eliminated. This issue could be solved by trying different sequences of linkers resistant to proteolysis, though at the expense of significant additional time. We provide here stronger evidence that the fusions potentiate the effect of PcTx1 by producing a large non-recovering fraction.

3. The newly presented Biacore data for the binding of the nanobody to the channels (shown in Figure 5-S1) is not well fit by the two-site binding model that is used. This fit leads to an exceptionally low 1 pM binding affinity, which is likely an overestimate of the binding affinity. (As a frame of reference, "tight" antibody-antigen complexes are usually closer to 1 nM binding affinity, with some as low as 100 pM). These data should not be used to estimate a Kd value if issues with protein quality make these curves unfittable by plausible binding models.

We have removed the figure of the Biacore binding kinetics of Nb.C1, as we agree that the fit to the unbinding time-course is very unreliable. The following paragraph has been added describing how we derived a rough estimate of the KD value of Nb.C1 (lines 214-222):

“To estimate the nanobody binding affinity, we first measured binding of Nb.1C to immobilized, detergent-solubilized hASIC1a protein using surface plasmon resonance. From experiments with two different Nb and hASIC1a protein preparations, global fits to association time courses with nanobody concentrations from 0.4 to 100nM yielded association rate constants kon ranging from 6.8x104 to 2.2x105 M-1 s-1. […] Taking the smallest kon value as a lower bound on association rate yields the equilibrium constant Kd ≲ 0.2 nM.”

This value is in the range of llama monomeric nanobodies (doi.org/10.1038/s42586-021-03676-z).

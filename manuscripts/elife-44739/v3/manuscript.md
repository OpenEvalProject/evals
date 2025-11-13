# Brain-specific Drp1 regulates postsynaptic endocytosis and dendrite formation independently of mitochondrial division

## Authors

- Kie Itoh<sup>1</sup> ([ORCID: 0000-0003-4379-400X](https://orcid.org/0000-0003-4379-400X))
- Daisuke Murata<sup>1</sup>
- Takashi Kato<sup>1</sup>
- Tatsuya Yamada<sup>1</sup>
- Yoichi Araki<sup>2</sup>
- Atsushi Saito<sup>3</sup>
- Yoshihiro Adachi<sup>1</sup>
- Atsushi Igarashi<sup>1</sup>
- Shuo Li<sup>1</sup>
- Mikhail Pletnikov<sup>2</sup>
- Richard L Huganir<sup>2</sup>
- Shigeki Watanabe<sup>1</sup>
- Atsushi Kamiya<sup>3</sup>
- Miho Iijima<sup>1</sup> †
- Hiromi Sesaki<sup>1</sup> ([ORCID: 0000-0002-6877-3929](https://orcid.org/0000-0002-6877-3929)) †

### Affiliations

1. Department of Cell Biology Johns Hopkins University School of Medicine Baltimore United States
2. Solomon H. Snyder Department of Neuroscience Johns Hopkins University School of Medicine Baltimore United States
3. Department of Psychiatry and Behavioral Sciences Johns Hopkins University School of Medicine Baltimore United States

† Corresponding author

## Abstract

Dynamin-related protein 1 (Drp1) divides mitochondria as a mechano-chemical GTPase. However, the function of Drp1 beyond mitochondrial division is largely unknown. Multiple Drp1 isoforms are produced through mRNA splicing. One such isoform, Drp1ABCD, contains all four alternative exons and is specifically expressed in the brain. Here, we studied the function of Drp1ABCD in mouse neurons in both culture and animal systems using isoform-specific knockdown by shRNA and isoform-specific knockout by CRISPR/Cas9. We found that the expression of Drp1ABCD is induced during postnatal brain development. Drp1ABCD is enriched in dendritic spines and regulates postsynaptic clathrin-mediated endocytosis by positioning the endocytic zone at the postsynaptic density, independently of mitochondrial division. Drp1ABCD loss promotes the formation of ectopic dendrites in neurons and enhanced sensorimotor gating behavior in mice. These data reveal that Drp1ABCD controls postsynaptic endocytosis, neuronal morphology and brain function.

## Introduction

The major function of Drp1, which is encoded by the Dnm1l gene, is to control mitochondrial division as a mechano-chemical GTPase (Kameoka et al., 2018; Kraus and Ryan, 2017; Pernas and Scorrano, 2016; Prudent and McBride, 2017; Ramachandran, 2018; Tamura et al., 2011; van der Bliek et al., 2013). During mitochondrial division, Drp1 is assembled into helical filaments around the surface of mitochondria. Through GTP hydrolysis and interactions with receptors, the Drp1 filaments change their conformation and constrict the mitochondrial membrane. Mitochondrial division is important for human health: hyper- or hypo-division caused by the mis-regulation of Drp1 has been linked to many neurological disorders, such as Alzheimer's, Parkinson's, and Huntington's diseases (Cho et al., 2010; Itoh et al., 2013; Kandimalla and Reddy, 2016; Roy et al., 2015; Serasinghe and Chipuk, 2017). Notably, human Drp1 mutations also lead to neurodevelopmental defects with post-neonatal lethality, developmental delay, late-onset neurological decline, or optic atrophy (Fahrner et al., 2016; Gerber et al., 2017; Vanstone et al., 2016; Waterham et al., 2007); however, our current understanding of Drp1’s function outside of mitochondrial division is limited.

To study the function of Drp1, complete and tissue-specific knockout (KO) mice for Drp1 have been characterized. The loss of Drp1 results in mitochondrial elongation and enlargement due to unopposed mitochondrial fusion in the absence of mitochondrial division in many cells (Friedman and Nunnari, 2014; Kashatus, 2018; Widlansky and Hill, 2018; Youle and van der Bliek, 2012). Complete loss causes embryonic lethality (Ishihara et al., 2009; Wakabayashi et al., 2009), whereas neuron-specific KO leads to a wide range of phenotypes, depending on the types of neurons and the timings when Drp1 is knocked out. For example, the loss of Drp1 in cerebellar Purkinje cells results in developmental defects when knocked out in embryos and progressive degeneration when knocked out in post-mitotic adult Purkinje cells (Kageyama et al., 2012; Wakabayashi et al., 2009). Similar to Purkinje cells, the loss of Drp1 induces massive death in dopaminergic neurons (Berthet et al., 2014). In contrast, hippocampal neurons are more resistant to the loss of Drp1; hippocampal neurons that lack Drp1 or express dominant negative Drp1, do not die but instead show deficits in bioenergetic and synaptic functions (Divakaruni et al., 2018; Shields et al., 2015). Similarly, Drp1-KO hypothalamic pro-opiomelanocortin neurons are also viable and show increased glucose and leptin sensing (Santoro et al., 2017).

Drp1 is encoded by a single gene and produces multiple isoforms through alternative splicing of mRNAs. There are four alternative exons in Drp1 in mice (termed A, B, C, and D) (Figure 1A). These alternative exons are located in either the GTPase domain (A and B) or the variable domain (C and D), which is mainly intrinsically disordered and contains regulatory phosphorylation sites (Itoh et al., 2018). All of the Drp1 isoforms are located at mitochondria and function in mitochondrial division (Itoh et al., 2018). Interestingly, a subset of these isoforms is also located at additional sites. For example, Drp1D and Drp1BD are associated with and regulate the dynamics of microtubules (Itoh et al., 2018; Strack et al., 2013). We recently identified a novel isoform of Drp1 (termed Drp1ABCD) that is exclusively expressed in the brain (Itoh et al., 2018). Drp1ABCD, which contains all of the alternative exons, is the only isoform that is associated with lysosomes, late endosomes, and the plasma membrane when this isoform is expressed in Drp1-KO mouse embryonic fibroblasts (MEFs) (Itoh et al., 2018). Analysis of transcripts and proteins showed that Drp1ABCD is expressed at low levels; Drp1ABCD constitutes less than 5% of all the Drp1 isoforms expressed in the brain (Itoh et al., 2018).

![Figure 1.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig1-v3.jpg)

**Figure 1.:** (A) Domain architecture of Drp1ABCD. Alternative exons A and B are present in the 80-loop inside the GTPase domain while alternative exons C and D are located in the variable domain. (B) Different mouse organs were analyzed by Immunoblotting using antibodies to Drp1ABCD (AB), pan-Drp1, the mitochondrial protein PDH, and GAPDH. 60 µg (AB and pan-Drp1) and 12.5 µg (PDH and GAPDH) of proteins were loaded per lane. (C) Whole brains and hippocampi were analyzed at the indicated ages by Immunoblotting with antibodies to Drp1ABCD, postsynaptic density protein 95 (Psd-95), pan-Drp1, and actin. (D) Hippocampal neurons were cultured in vitro for 1, 2, 3 and 4 weeks and analyzed by immunoblotting. (E) Cultured hippocampal neurons were co-transfected at 3 weeks with plasmids carrying HA-Drp1ABCD or HA-Drp1BCD, along with plasmids carrying a cytosolic marker, tdTomato. Three days after transfection, neurons were analyzed by immunofluorescence microscopy with antibodies to RFP (which recognizes tdTomato) and HA. Boxed regions are enlarged. Bar, 20 µm. (F) Intensity of tdTomato (red) and HA (green) signals in dendritic shafts and spines were quantified along the lines shown in Figure 1E. Intensity was normalized to the highest value. (G) Ratios of signal intensity in spines relative to those in dendritic shafts were analyzed for HA-Drp1ABCD and HA-Drp1BCD. As a control, the tdTomato signal was used. Bars are mean ± SD (n = 176 spines in 10 neurons expressing HA-Drp1ABCD and 163 spines in 10 neurons expressing HA-Drp1BCD). (H) Cultured hippocampal neurons were co-transfected at 3 weeks with plasmids carrying tdTomato and HA-Drp1ABCD or HA-Drp1BCD and subjected to immunofluorescence microscopy with antibodies to HA and vesicular glutamate transporter 1 (VGLUT1). Boxed regions are enlarged. Bar, 5 µm. (I) Postsynaptic density fractions were isolated from the whole brains of wild-type mice and analyzed by Immunoblotting. Brain, whole brain; P2, membrane fraction; S2, cytosolic fraction; Syn, total synaptosomal fraction; Syn/Tx, Triton-soluble synaptosomal fraction; PSD, postsynaptic density fraction. (J) Band intensity of total Drp1 (pan-Drp1) and Drp1ABCD (AB) in the postsynaptic density fraction was quantified relative to the whole brain. Bars are mean ± SD (n = 3). Statistical analysis was performed using Mann–Whitney U test (G) and Student’s t-test (J). n.s., not significant.

The unique localization of Drp1ABCD suggests that this brain-specific isoform may play a role in membrane trafficking in neurons; however, its function remains to be determined because of the lack of tools to specifically assess its function without affecting other isoforms. In this study, we have developed isoform-specific knockdown by shRNA and knockout by CRISPR/Cas9. Using these new approaches, we found that Drp1ABCD controls postsynaptic endocytosis and dendrite growth in neurons independently of mitochondrial division.

## Results and discussion

### Drp1ABCD expression is induced during postnatal brain development

Since Drp1ABCD is the only isoform that contains both the alternative exons A and B (Figure 1A), we raised antibodies that specifically recognize Drp1ABCD using the amino acid sequence that corresponds to the junction of exons A and B as an antigen (Itoh et al., 2018). The expression of Drp1ABCD was spatially controlled and specific to the brain (Itoh et al., 2018) (Figure 1B). In the brain, Drp1ABCD was ubiquitously expressed in multiple subregions, including the hippocampus, cortex, midbrain, striatum, and cerebellum (Itoh et al., 2018).

To test whether the expression of Drp1ABCD is temporarily regulated in the brain, we performed Immunoblotting of whole brain and hippocampus tissues that were harvested from mice at the ages of P0, P8, 1 month, and 2 months. We found that the expression of Drp1ABCD is postnatally induced in both tissues later in neural development compared to that of postsynaptic density protein 95 (Psd-95), which is a synaptic protein required for glutamate receptor organization (Figure 1C). In contrast, anti-pan-Drp1 antibodies, which recognize all Drp1 isoforms, showed similar levels of Drp1 at different stages of postnatal brain development (Figure 1C). Consistent with the in vivo data, immunoblotting of hippocampal neurons cultured in vitro showed that the expression of Drp1ABCD gradually increases and reaches a plateau around 3 weeks (Figure 1D).

### Drp1ABCD is enriched in postsynaptic terminals

To examine the subcellular localization of Drp1ABCD in neurons, we expressed HA-Drp1ABCD along with a cytosolic marker, tdTomato, in cultured hippocampal neurons. For a comparison, we tested HA-Drp1BCD, the most abundant brain Drp1 isoform (Itoh et al., 2018). In the soma, both HA-Drp1ABCD and HA-Drp1BCD appeared to be uniformly distributed (Figure 1E). We did not observe a clear association between these HA-tagged Drp1 isoforms and mitochondria, lysosomes, or the plasma membrane, likely due to their overexpression and therefore high levels in the cytoplasm. Interestingly, however, we found that HA-Drp1ABCD is enriched in postsynaptic regions, compared to HA-Drp1BCD (Figure 1E). Line scanning analysis of their fluorescence showed a significant increase in the signal ratio of HA-Drp1ABCD (spine vs dendritic shaft), compared to HA-Drp1BCD (Figure 1F and G). Analysis of HA-Drp1ABCD and HA-Drp1BCD in synapses at high magnification suggested its preferential localization of HA-Drp1ABCD around the postsynaptic density, which is in a close apposition to the pre-synaptic marker vesicular glutamate transporter 1 (Figure 1H).

To test the localization of endogenous Drp1ABCD at the postsynaptic density, we biochemically obtained postsynaptic density fractions from the brains of mice (Araki et al., 2015) since anti-Drp1ABCD antibodies do not work in immunofluorescence of the endogenous protein. Consistent with the immunofluorescence data, increased levels of Drp1ABCD were co-fractionated with the postsynaptic density, compared to total Drp1 detected by pan-Drp1 antibodies (Figure 1I and J).

### The loss of Drp1ABCD inhibits endocytosis at postsynaptic terminals

To examine the function of Drp1ABCD at the postsynaptic density, we homozygously deleted exon A using the CRISPR/Cas9 genome editing system (termed Drp1exonA-KO mice) since Drp1ABCD is the only isoform that contains this exon (Itoh et al., 2018) (Figure 2A). We confirmed the lack of Drp1ABCD proteins in Drp1exonA-KO mice using Immunoblotting (Figure 2B). Consistent with a low expression level of Drp1ABCD (compared to that of other isoforms, such as Drp1BCD) (Itoh et al., 2018), we found no gross changes in the total amount of Drp1 in Immunoblotting using anti-pan-Drp1 antibodies (Figure 2B). Drp1exonA-KO mice were born at an expected Mendelian ratio with normal weights of the body and brain (Figure 2C–E). H and E staining of sagittal brain sections showed that the histology of the cerebellum appears to be normal in Drp1exonA-KO mice (Figure 2F). DAPI staining also showed similar nuclear patterns of neurons and the thickness of the CA1 layer in the hippocampus in control and Drp1exonA-KO mice (Figure 2G). These data suggest that the loss of Drp1ABCD does not change the overall structure of the brain.

![Figure 2.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig2-v3.jpg)

**Figure 2.:** (A) Two guide RNAs were used to cut the genome at two positions (red arrowheads) to remove the majority of exon A and part of the following intron using CRISPR/Cas9. This deletion introduced a stop codon 20 residues downstream from the deletion site (STOP). (B) The indicated tissues were harvested from control and Drp1exonA-KO mice and analyzed by immunoblotting using antibodies to Drp1ABCD (AB), pan-Drp1, the mitochondrial protein PDH, and GAPDH. (C and D) Weights of the whole body (C) and brain (D) were measured. Bars are mean ± SD (n = 4 in C and 5 in D). (E) Images of the whole brain. Bar, 1 cm. (F) H and E staining of cerebella of control and Drp1exonA-KO mice. Sagittal sections were cut in the midline. Bar, 1 mm. (G) Frozen sections of the hippocampus in control and Drp1exonA-KO mice were stained with DAPI. Bar, 0.5 mm. The thickness of the CA1 layer was measured. Bars are mean ± SD (n = 3). (H) Control and Drp1exonA-KO hippocampal neurons were cultured for 3 weeks and subjected to transmission electron microscopy. An arrowhead indicates a clathrin-coated pit (CCP) at a postsynaptic terminal. Bar, 100 nm. (I and J) Quantification of the number of CCPs at postsynaptic and presynaptic terminals. Bars are mean ± SD (n = 4 experiments, in which 167, 196, 172, 191 control and 158, 161, 169, 221 Drp1exonA-KO synapses were analyzed). (K and L) The numbers of CCPs with three different morphologies (shallow, U-shaped, and Omega-shaped) were measured. Bar, 100 nm. (M–P) Control and Drp1exonA-KO hippocampal neurons were treated with 80 µM of dynasore for 30 min and analyzed by electron microscopy (M and O). Bar, 500 nm. The number of CCPs (N) and the size of mitochondria (P) were determined. Bars are mean ± SD (n = 159, 182, 172 -/control, 152, 163, 143 +/control, 176, 163, 129 -/KO, and 162, 146, 145 +/KO synapses) (N) and (n = 30–32 mitochondria analyzed in each group) (P). (Q and R) Chemical long-term depression (NMDA/Gly) was induced by NMDA for 3 min in the presence or absence dynasore (80 µM). Neurons were then fixed, and CCPs at postsynaptic and presynaptic terminals were analyzed by electron microscopy. Bars are mean ± SD (n = 3–4 experiments. In each experiment, more than 100 synapses were analyzed). Statistical analysis was performed using Student’s t-test (C, D, G, I, J, L and N) and One-way ANOVA with post-hoc Tukey (P, Q and R). (S) Summary of the data.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (A–C) Cultured control and Drp1exonA-KO neurons were incubated with 80 µM of dynasore for 30 min and analyzed using immunofluorescence microscopy with anti-PDH antibodies. Boxed regions are enlarged: a, proximal dendritic regions and b, distal dendritic regions. Bar, 20 µm. Mitochondrial length was determined in the proximal (B) and distal dendritic regions (C). Bars are mean ± SD (n = 10 neurons analyzed in each group; 99–121 mitochondria were measured in each neuron). The statistical analysis was performed using the Student’s t-test. (D) WT MEFs were treated with 80 µM of dynasore for 1 hr and analyzed by immunofluorescence microscopy with anti-Tom20 antibodies (BD Biosciences, 61278). As a control for the loss of Drp1 function, Drp1-KO MEFs were also examined. Bar, 20 µm. (E) Mitochondrial shape is quantified (n = 30 cells).

We isolated hippocampal neurons from E18.5 mouse embryos and cultured them in vitro for 3 weeks. We then examined synapses by transmission electron microscopy. In both control and Drp1exonA-KO neurons, we observed matured synaptic contacts (Figure 2H). However, remarkably, the number of clathrin-coated pits (CCPs) was significantly different in these neurons—Drp1exonA-KO neurons showed more CCPs in postsynaptic terminals compared with control neurons (Figure 2H and I). In contrast, the number of CCPs in presynaptic terminals was indistinguishable (Figure 2H and J). We then divided the morphologies of CCPs in postsynaptic terminals into three categories: shallow, U-shaped and omega-shaped pits. We found an increased frequency of shallow and U-shaped CCPs, which likely represent early stages during endocytosis, in Drp1exonA-KO neurons (Figure 2K and L). The frequencies of omega-shaped CCPs were similar in control and Drp1exonA-KO neurons (Figure 2K and L).

The observed increase in the number of CCPs could be explained by either activation or inhibition of endocytosis. First, the rate of clathrin-mediated endocytosis may be enhanced in Drp1exonA-KO neurons and therefore shallow and U-shaped CCPs were observed at a higher frequency. Alternatively, clathrin-mediated endocytosis may be slowed at early stages after the initiation of endocytosis perhaps in Drp1exonA-KO neurons and thereby the intermediates were accumulated. To distinguish between these two possibilities, we treated control and Drp1exonA-KO neurons with dynasore, a dynamin inhibitor that blocks the final step of endocytosis (Macia et al., 2006), for 30 min prior to chemical fixation for electron microscopy. As expected, dynasore significantly increased the number of CCPs at postsynaptic terminals in control neurons (Figure 2M and N). In contrast, when we treated Drp1exonA-KO neurons with dynasore, we found no increase in the number of CCPs (Figure 2M and N). Thus, it is likely that the rate of clathrin-mediated endocytosis is decreased in Drp1exonA-KO neurons. The accumulation of shallow and U-shaped CCPs, but not omega-shaped ones, suggest that Drp1ABCD may function at an early step upstream of the constriction and severing of the neck of coated pits that is mediated by dynamin (Figure 2S). We confirmed that dynasore did not inhibit Drp1 by examining mitochondrial morphology in neurons and mouse embryonic fibroblasts using electron microscopy and immunofluorescence microscopy with antibodies to a mitochondrial protein (pyruvate dehydrogenase, PDH)(Figure 2O and P; Figure 2—figure supplement 1).

To further examine the consequence of Drp1ABCD loss in clathrin-mediated endocytosis, we stimulated WT and KO neurons with N-methyl-D-aspartic acid (NMDA) for a short period of time (3 min) and analyzed the number of CCPs at the postsypatic terminal. When we stimulated neurons in the presence of dynasore, the number of postsynaptic clathrin-coated pits increased in control neurons. This is due to stimulation of endocytosis by NMDA and inhibition of its completion by dynasore. In contrast, the number of CCPs remained unchanged in Drp1exonA-KO neurons (Figure 2Q). These phenotypes of Drp1ABCD loss were only observed at the postsynaptic region and not the presynaptic region (Figure 2R). These data further support the notion that postsynaptic clathrin-mediated endocytosis is slow in Drp1exonA-KO neurons even when stimulated by NMDA (Figure 2S). Interestingly, when stimulated by NMDA in the absence of dynasore, the number of CCPs was decreased in Drp1exonA-KO neurons (Figure 2Q). It appears that NMDA induces internalization of some endocytic vesicles in Drp1exonA-KO neurons. We suggest that Drp1exonA-KO neurons have slow kinetics of endocytosis but do not completely block it (Figure 2S).

To understand how Drp1ABCD loss results in changes in CCPs, we tested postsynaptic positioning of the endocytic zone using mCherry-clathrin light chain (mCherry-CLC) and Psd-95-Fibronectin intrabodies (Gross et al., 2013; Lu et al., 2007). As previously reported (Lu et al., 2007), the majority of mCherry-CLC signals are localized next to Psd-95 signals in control neurons (Figure 3A and B). In contrast, we found a higher frequency of dissociation of mCherry-CLC signals from Psd-95 signals in Drp1exonA-KO neurons (Figure 3A and B). We speculate that decreased levels of clathrin in the synapses in Drp1exonA-KO neurons slow the progression of endocytosis. In these synapses, the formation of CCPs is initiated; however, the maturation of CCPs is likely decreased due to the limited availability of clathrin molecules. As a result, CCPs accumulate during relatively early stages of endocytosis (e.g., shallow and U-shaped CCPs) (Figure 2L). These data suggest that Drp1ABCD, unlike dynamin, does not play a role in the scission of the neck of coated pits.

![Figure 3.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig3-v3.jpg)

**Figure 3.:** (A and B) Hippocampal neurons were cultured and transfected with plasmids expressing Psd-95.FingR-GFP and mCherry-CLC. Two days after transfection, neurons were subjected to chemical LTD stimulation (NMDA/Gly), fixed and analyzed by laser scanning confocal microscopy. Bar, 5 µm. The number of Psd-95.FingR-GFP signals that are not associated with mCherry-CLC was scored. Bars are mean ± SD (n = 14–15 neurons were analyzed in each group). (C) Cell surface proteins were biotinylated with sulfo-NHS-SS-biotin in cultured control and Drp1exonA-KO hippocampal neurons. The neurons were lysed and incubated with NeutrAvidin agarose. Total cell lysates and precipitated proteins (Surface) were separated by immunoblotting to antibodies to GluR1, GluR2, GluR3 and GAPDH. (D) Band intensity was determined. Bars are mean ± SD (n = 5). (E) Cultured neurons were co-transfected with plasmids carrying Psd-95-mCherry and GFP-GluR1. Two days after transfection, the neurons were treated with chemical LTD (NMDA/Gly) and subjected to immunofluorescence microscopy with anti-GFP antibodies without permeabilization of the plasma membrane. Images were acquired using identical settings. (F) The relative intensity of the signal from the anti-GFP antibodies (surface GFP-GluR1) compared with the GFP signal (total GFP-GluR1) was determined. Bars are mean ± SD (n = 50). (G) Model for the function of Drp1ABCD in the postsynaptic terminal. (H–J) Control and Drp1exonA-KO hippocampal neurons were subjected to immunofluorescence microscopy with antibodies against the mitochondrial protein PDH. Boxed regions are enlarged: a, proximal dendritic regions and b, distal dendritic regions. Bar, 20 µm. The length of mitochondria was determined in proximal (I) and distal dendritic regions (J). Bars are mean ± SD (n = 10 neurons analyzed in each group. 70–120 mitochondria measured in each neuron). Statistical analysis was performed using Kruskal-Wallis test with Dunn’s multiple comparisons test (B), Mann–Whitney U test (I) and Student’s t-test (D, F and J).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (A) Cultured control and Drp1exonA-KO neurons were incubated with 50 µg/ml FITC-transferrin for 15 min at 4°C or 37°C. Cells were washed with cold PBS, fixed with paraformaldehyde and viewed by confocal microscopy. Intensity of FITC signals was quantified (n = 10 control neurons and 6 KO neurons). Statistical analysis was performed using Student’s t-test. (B) Drp1-KO MEFs expressing no Drp1, Drp1ABCD or Drp1BCD were incubated with 5 µg/ml of Alexa-Fluor-647-transferrin for 30 min at 4°C or 37°C. After fixation, cells were visualized by confocal microscopy. Intensity of Alexa-Fluor-647 signals was quantified. Bars are mean ± SD (n = 15–25 cells analyzed in each group). Statistical analysis was performed using one-way ANOVA with post-hoc Tukey. (F) The localization of Drp1ABCD at the plasma membrane is insensitive to dynasore treatment. Drp1-KO MEFs were transduced with lentiviruses expressing Drp1ABCD, treated with 80 µM dynasore for 1 hr and analyzed by immunofluorescence microscopy with antibodies to Drp1 and Tom20. Bar, 20 µm. The number of cells that show the localization of Drp1ABCD at the plasma membrane was quantified (n = 3 experiments. 30–60 cells were analyzed in each experiment). Statistical analysis was performed using Student’s t-test.

The extent of the dissociation of the postsynaptic density from the endocytic zone in Drp1exonA-KO synapses is similar to that reported for the disruption of Homer, an adaptor protein that connects the postsynaptic density and endocytic zone (Lu et al., 2007). Like Homer defective neurons, the uptake of FITC-transferrin was not affected in Drp1exonA-KO neurons (Figure 3—figure supplement 1). In contrast to the Homer pathway, however, we found that AMPA receptors, such as GluR1, GluR2 and GluR3, are normally expressed on the plasma membrane of Drp1exonA-KO neurons in surface biotinylation experiments (Figure 3C and D). Furthermore, endocytosis of GFP-GluR1 in response to NMDA stimulation was not perturbed in Drp1exonA-KO neurons (Figure 3E and F). These data suggest that the Drp1ABCD pathway has cargos that differ from those of the Homer pathway (Figure 3G).

Using immunofluorescence microscopy, we observed no gross changes in the morphology of mitochondria in proximal and distal regions along with dendrites in Drp1exonA-KO neurons (Figure 3H–J). Therefore, inhibition of endocytosis does not appear to be the result of defects in mitochondrial morphology. It is likely that other Drp1 isoforms, such as Drp1BCD and Drp1CD, which together constitute the majority of Drp1 isoforms in the brain (Itoh et al., 2018), mainly control mitochondrial division and morphology.

A previous study reported that Drp1 regulates endocytosis for synaptic vesicle recycling at presynaptic terminals in hippocampal neurons through interactions with a Drp1 receptor protein, Mff (Li et al., 2013). Since we found endocytic defects only at postsynaptic terminals in Drp1exonA-KO neurons, distinct Drp1 isoforms may function separately in endocytosis at pre- and postsynaptic terminals.

### The loss of Drp1ABCD induces the extension of ectopic dendrites in cultured neurons

Intriguingly, during analysis of the morphology of cultured hippocampal neurons, we noticed that Drp1exonA-KO neurons significantly increased the number of primary dendrites with dendritic spines (e.g., dendrites that directly emerged from the soma), compared to control neurons (Figure 4A and B). The number of axons that lack spines remained unchanged (one axon per neuron). The effect of Drp1ABCD loss was specific to the number of primary dendrites. We observed no significant difference in the number of dendritic branches between control and Drp1exonA-KO neurons (Figure 4C) or the density of dendritic spines (Figure 4D).

![Figure 4.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig4-v3.jpg)

**Figure 4.:** (A) Control and Drp1exonA-KO hippocampal neurons were cultured and transfected with plasmids expressing GFP at 3 weeks. Boxed regions are enlarged. Arrowheads indicate axons that lack dendritic spines. Bar, 20 µm. (B and C) The numbers of primary dendrites (B) and dendritic branches (C) were quantified. Bars are mean ± SD (n = 60 control and 59 KO neurons). (D) The number of spines was quantified (n = 10 control and 10 KO neurons). (E) The DNA sequence that is targeted to knock down Drp1ABCD is shown. (F) HEK293 cells were co-transfected with plasmids carrying the indicated GFP-Drp1 and shRNAs. Whole-cell extracts were analyzed by Immunoblotting using the indicated antibodies. (G) Mouse hippocampal neurons were cultured for 2 or 3 weeks and transfected with plasmids expressing the indicated shRNAs and GFP as a cytosolic marker. Images of 3 week cultured neurons are presented. Boxed regions are enlarged. Arrowheads indicate axons that lack dendritic spines. Bar, 20 µm. (H) The number of primary dendrites were quantified. Bars are mean ± SD (n = 29–30 neurons at 2 weeks and 50 neurons at 3 weeks). (I) Cultured neurons were transfected at 3 weeks with the plasmid expressing AB-targeted shRNA and GFP along with another plasmid carrying shRNA-resistant Drp1ABCD. The number of primary dendrites was quantified. Bars are mean ± SD (n = 60 neurons for empty plasmid and 52 for Drp1ABCD). (J) Cultured hippocampal neurons were transfected with the indicated shRNA plasmids that co-express GFP in the presence or absence of 2 µM tetrodotoxin (TTX). The number of primary dendrites was quantified (n = 60 for -TTX/scramble, 75 for +TTX/scramble, 79 for -TTX/AB and 57 for +TTX/AB). (K and L) Control and Drp1exonA-KO mice were crossed with a mouse line expressing cytosolic GFP from the neuron-specific Thy1 promoter. We analyzed the number of neurites in the hippocampus (K) and cortex (L) at the age of 3–4 months. Bars are mean ± SD (n = 90 neurons in three mice for each genotype). Bar, 10 µm. (M) Plasmids carrying the indicated shRNAs were introduced into the hippocampi of E15.5 mouse embryos, along with plasmids carrying GFP, by electroporation in utero. (N) Hippocampi were analyzed at an age of 7 weeks using laser confocal microscopy of frozen brain sections. Bar, 20 µm. The number of neurites that directly emerge from the soma was quantified. Bars are mean ± SD (n = 51 neurons for scramble and 56 for AB-targeted). (O and P) Startle response (O) and PPI tests (P). Bars are mean ± SD (n = 12 control and 14 KO mice). Statistical analysis was performed using Student’s t-test (B, C, D. H-3 weeks, I, K, N and P), Mann–Whitney U test (H-2 weeks, L and O) and One-way ANOVA with post-hoc Tukey (J).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Cultured hippocampal neurons were transfected at 3 weeks with the indicated shRNA plasmids carrying GFP as a cytosolic marker. Cells were subjected to immunofluorescence microscopy with anti-MAP2 antibodies. Arrowheads indicate axons, and arrows indicate dendrites. Bar, 20 µm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Frozen section of the hippocampus (A) and cortex (B) in control and Drp1exonA-KO mice expressing cytosolic GFP from the neuron-specific Thy1 promoter are shown. Bar, 100 µm.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/44739/elife-44739-fig4-figsupp3-v3.jpg)

**Figure 4—figure supplement 3.:** (A) Open field test. Total activity (Locomotor activity) and percentage time spent in the central and peripheral regions (Anxiety). (B) Y-maze tests. Number of arm entries (Locomotor activity), spontaneous alternation (Working memory), and time in novel arm (Spatial recognition memory) were determined. (C) Rotarod test. (D) Elevated plus maze tests. Bars are mean ± SD (n = 26 control and 26 Drp1exonA-KO mice). Statistical analysis was performed using Student’s t-test. Source Data File List for Figures (file name).

To further test whether Drp1ABCD controls dendrite formation in neurons in a cell-autonomous fashion, we specifically knocked down Drp1ABCD in cultured hippocampal neurons using shRNAs. To target Drp1ABCD, we used an mRNA sequence that corresponds to the junction between exon A and exon B, which is unique to Drp1ABCD (Figure 4E). First, the specificity of this knockdown construct was confirmed. We individually expressed each of GFP-Drp1ACD, GFP-Drp1BCD, and GFP-Drp1ABCD in separate HEK293 cells. We found that AB-targeted shRNA specifically knocked down GFP-Drp1ABCD, but not GFP-Drp1ACD or GFP-Drp1BCD (Figure 4F, AB shRNA). As a negative control, scramble shRNA was used (Figure 4F, Scramble). As a positive control, we targeted an mRNA sequence that is common in all Drp1 isoforms (Figure 4F, Pan-Drp1).

Supporting the data from the above experiments using Drp1exonA-KO neurons, AB-targeted shRNA significantly increased the number of primary dendrites in cultured neurons at both 2 and 3 weeks compared to scramble shRNA (Figure 4G and H). Ectopic dendrites extended within a short period of time (3 days) after knockdown of Drp1ABCD in mature neurons with developed dendrites. The number of axons did not change (one axon per neuron) as assessed by immunofluorescence microscopy with anti-MAP2 antibodies, which label dendrites but not axons (Figure 4—figure supplement 1). To confirm that the induction of dendrite formation results from the knockdown of Drp1ABCD, we co-expressed plasmids carrying a knockdown-resistant form of Drp1ABCD along with AB-targeted shRNAs. The Drp1ABCD plasmid, but not the empty plasmid, significantly rescued the effect of AB-targeted shRNAs (Figure 4I). These data further support the notion that Drp1ABCD is important for controlling the number of primary dendrites in neurons.

Dendrite growth is regulated by neuronal activity-dependent and -independent mechanisms (Wong and Ghosh, 2002). To understand the mechanism underlying the ectopic dendrite formation in AB-targeted neurons, we treated hippocampal neurons during knockdown with tetrodotoxin, a sodium channel inhibitor that blocks action potentials. We found that tetrodotoxin significantly blocked the effect of Drp1ABCD knockdown on ectopic dendrite formation, but did not affect the number of dendrites in control neurons (Figure 4J). These data suggest that the formation of primary dendrites induced by Drp1ABCD depletion requires neuronal activity.

### Loss of Drp1ABCD induces the formation of ectopic primary dendrites in vivo

To test the function of Drp1ABCD in the morphology of neurons in vivo, we analyzed the morphology of neurons in Drp1exonA-KO mice. To achieve this goal, it was critical to sparsely label individual neurons because the density of neurons is too high to faithfully visualize the morphology of each neuron if all of the neurons are labeled. We crossed Drp1exonA-KO mice with a mouse line that expresses a cytosolic GFP in a small number of neurons driven by the neuron-specific Thy1 promoter (Feng et al., 2000) (Figure 4—figure supplement 2). We counted the number of neurites using z stacks of laser confocal microscopy of frozen brain sections. We found a significant increase in the number of neurites in the CA1 and CA2 layers in the dorsal hippocampus (Figure 4K) consistent with the data from the in vitro experiments. The effect of Drp1ABCD loss on primary dendrites was also evident in the cortex (Figure 4L).

To further test the effect of Drp1ABCD knockdown during brain development in vivo, we performed in utero electroporation of shRNAs. We injected plasmids carrying scramble or AB-targeted shRNA, along with plasmids carrying cytosolic GFP, into the lateral ventricles of E15.5 embryos in timed pregnant mice using a glass micropipette (Figure 4M). We then performed electroporation to introduce the plasmids into the hippocampus, after which the embryos were returned to the abdomen. At 7 weeks after birth, mice were fixed using cardiac perfusion of paraformaldehyde (Figure 4M). Coronal cryosections of the CA1 and 2 layers in the dorsal hippocampus were cut and the neuronal morphology was analyzed using z stacks of laser confocal microscopy images. Since the cytosolic GFP labels both dendrites and axons, we counted the number of neurites (including both dendrites and axons) that directly emerged from the soma. Consistent with the knockout results, we found that knockdown of Drp1ABCD significantly increased the number of neurites, compared to the scramble control, in the hippocampus in vivo (Figure 4N).

### The loss of Drp1ABCD increases sensorimotor gating function

To test whether the loss of Drp1ABCD affects brain function, behavioral phenotypes were systematically characterized in control and Drp1exonA-KO mice. We observed normal general locomotor activities in Drp1exonA-KO mice in open field test (Figure 4—figure supplement 3A). Intriguingly, KO mice exhibited significantly increased prepulse inhibition (PPI) of the acoustic startle without alterations in the startle response (Figure 4O and P). PPI, as a measure of sensorimotor gating, involves several brain regions (including the hippocampus, medial prefrontal cortex, amygdala, and nucleus accumbens) (Lee and Davis, 1997; Swerdlow et al., 2001). Sensorimotor gating function enables selective attention that distinguishes or separates critical information from background noise. In humans, sensorimotor gating function is often referred to as the cocktail party effect, which allows one to talk with someone even in a crowded party environment (Lee and Davis, 1997; Swerdlow et al., 2001). This gating function is important for human health and its defects have been associated with mental illness, such as schizophrenia and autism spectrum disorders (Lee and Davis, 1997; Swerdlow et al., 2001). At this moment, we do not know the exact mechanistic basis underlying this enhanced sensorimotor gating in Drp1exonA-KO mice; however, the increased number of dendrites or the decreased postsynaptic endocytosis in Drp1exonA-KO mice may contribute to the enhancement in sensorimotor gating function. Behavioral changes in Drp1exonA-KO mice appeared to be specific to sensorimotor gating since we observed no alterations in spatial working and recognition memory tasks in Y-maze tests (Figure 4—figure supplement 3B), motor coordination in rotarod test (Figure 4—figure supplement 3C), and anxiety level in elevated plus maze test (Figure 4—figure supplement 3D).

In summary, we found, for the first time, that the novel brain-specific isoform Drp1ABCD controls postsynaptic endocytosis independently of mitochondrial division. It would be important to test if this, in turn, results in the accumulation of cargoes on the postsynaptic surface and leads to ectopic formation of dendrites in future studies. Since the expression of Drp1ABCD is induced during the postnatal period, Drp1ABCD may control the number of dendrites by suppressing unwanted, excess dendrite formation in neuronal network wiring during postnatal brain development.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Wild-type mice</td>
      <td>This paper</td>
      <td></td>
      <td>Materials and methods: Generation of Drp1exonA-KO mice using CRISPR/Cas9</td>
    </tr>
    <tr>
      <td>Genetic reagent(M. musculus)</td>
      <td>Drp1exonA-KO mice</td>
      <td>This paper</td>
      <td></td>
      <td>Materials and methods: Generation of Drp1exonA-KO mice using CRISPR/Cas9</td>
    </tr>
    <tr>
      <td>Genetic reagent(M. musculus)</td>
      <td>Thy1-GFP-M transgenic mice</td>
      <td>Jackson Laboratory</td>
      <td>Stock #: 007788</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent(M. musculus)</td>
      <td>C57BL/6J mice</td>
      <td>JacksonLaboratory</td>
      <td>Stock #: 000664</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>WT and Drp1-KO MEFs</td>
      <td>Kageyama et al. (2014)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-exon AB</td>
      <td>Itoh et al. (2018)</td>
      <td></td>
      <td>WB (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Psd-95</td>
      <td>EMD Millipore</td>
      <td>Cat #: MABN68</td>
      <td>WB (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-pan-Drp1</td>
      <td>BD Biosciences</td>
      <td>Cat #: 611113</td>
      <td>WB (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-PDH subunit E2/E3bp</td>
      <td>Abcam</td>
      <td>Cat #: ab110333</td>
      <td>IF (1:300)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>HA-Drp1ABCD</td>
      <td>Itoh et al. (2018)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>HA-Drp1BCD</td>
      <td>Itoh et al. (2018)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Psd95.FingR-GFP</td>
      <td>Addgene</td>
      <td>Cat #: 46295</td>
      <td>Gross et al. (2013)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>mCherry-Clathrin (CLC)</td>
      <td>Addgene</td>
      <td>Cat #: 27680</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Psd-95-mCherry</td>
      <td>Blanpied et al. (2008)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>GFP-GluR1</td>
      <td>Hussain et al. (2014)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSUPER-Scramble</td>
      <td>This paper</td>
      <td></td>
      <td>Materials and methods: Plasmids</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSUPER-AB</td>
      <td>This paper</td>
      <td></td>
      <td>Materials and methods: Plasmids</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSUPER-GFP-Scramble</td>
      <td>This paper</td>
      <td></td>
      <td>Materials and methods: Plasmids</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSUPER-GFP-AB</td>
      <td>This paper</td>
      <td></td>
      <td>Materials and methods: Plasmids</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCAGGS1-Drp1ABCD(resistant form)</td>
      <td>This paper</td>
      <td></td>
      <td>Materials andmethods: Plasmids</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dynasore hydrate</td>
      <td>Sigma-Aldrich</td>
      <td>Cat #: D7693</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NMDA</td>
      <td>Tocris</td>
      <td>Cat #: 0114</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glycine</td>
      <td>Tocris</td>
      <td>Cat #: 0219</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tetrodotoxin (TTX)</td>
      <td>Tocris</td>
      <td>Cat #: 1078</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Generation of Drp1exonA-KO mice using CRISPR/Cas9

All animal work was conducted according to the guidelines established by the Johns Hopkins University Committee on Animal Care and Use. To engineer the mouse Dnm1l gene that encodes Drp1, sgRNA-encoding sequences (5’- AAAATGGTAAATTTCAGAGC- 3’ to target inside the A exon and 5’-TAAAAAGTTGATTGGTGAAT- 3’ to target downstream of the A exon) were cloned into the BbsI site of pX330-T7 and amplified from pX330-T7 with a leading T7 promoter by PCR (Igarashi et al., 2018). These sgRNAs were in vitro transcribed using the HiScribe T7 Quick High Yield RNA Synthesis Kit (New England Biolabs) and purified using the MEGAclear Kit (Ambion). Cas9 mRNA was in vitro transcribed using NotI-linearized pX330-T7 and the mMESSAGE mMACHINE T7 Ultra Kit (Ambion) and purified by LiCl precipitation. Pronuclear injections of zygotes from B6SJLF1/J mice (Jackson Laboratory, stock no. 100012) were performed at the Johns Hopkins University Transgenic Facility using a mix of Cas9 mRNA and two sgRNA-encoding sequences in injection buffer (10 mM Tris-HCl, 0.1 mM EDTA filtered with 0.2 µm pore size). Three combinations of concentrations were used: 100 ng/µl of Cas9 mRNA and 50 ng/µl of each sgRNA, 100 ng/µl Cas9 of mRNA and 25 ng/µl of each sgRNA, and 25 ng/µl of Cas9 mRNA and 12.5 ng/µl of each sgRNA. The embryos were cultured at 37°C in the CO2 incubator for 2 hr and then transferred into the oviducts of pseudopregnant ICR females (25 embryos per mouse) (Envigo). Sixteen pups were obtained and their genotypes were analyzed by PCR using the following primers: 5’-AGACCTCTCATTCTGCAGCT-3’ and 5’-GTGGATGGTCGCTGAGTTTG-3’. We identified one founder mouse that truncated 96 bp to remove the A exon, resulting in A knock out. The A exon (KFQSWN) was replaced with 20 amino acids (KWEIIAIAKSEIFRIGINI) and a stop codon. By breeding with the Thy1-GFP-M transgenic mouse line (Jackson Laboratory, stock no. 007788), we generated Thy1-GFP/homozygous Drp1exonA-KO mice and Thy1-GFP/wild-type mice.

### Plasmids

To create the HA-Drp1BCD plasmid, Drp1ABCD in the HA-Drp1ABCD plasmid (Itoh et al., 2018) was replaced with the full length of Drp1BCD at the BamHI/NotI sites. To create the GFP-Drp1ABCD plasmid, (SAGG)5 linker sequence and full-length Drp1ABCD were cloned into the BglII/EcoRI sites and the XhoI/SmaI sites of pEGFP-C1 (Clontech), respectively. Drp1ABCD was replaced with Drp1ACD and Drp1BCD to create the GFP-Drp1ACD and GFP-Drp1BCD plasmids. To generate the shRNA plasmids, the following target sequences were cloned into pSUPER (Oligoengine, VEC-PBS-0002) or pSUPER-GFP (Yamada et al., 2018). Scramble: CCTAAGGTTAAGTCGCCCTCGttcaagagaCGAGGGCGACTTAACCTTAGG, AB: ATTTCAGAGCTGGAACCCTGCttcaagagaGCAGGGTTCCAGCTCTGAAAT, and pan-Drp1: GCTTCAGATCAGAGAACTTATttcaagagaATAAGTTCTCTGATCTGAAGC. To generate a knockdown-resistant Drp1ABCD plasmid, both target sequences for AB and pan-Drp1 were replaced to the following resistant form. AB: ATTTCAGAGCTGGAACCCTGC to GTTCCAAAGTTGGAATCCAGC, and pan-Drp1: GCTTCAGATCAGAGAACTTAT to GTTGCAAATTCGCGAGCTGAT. Underlined cases are the added silent mutations. Full length of Drp1ABCD with silent mutations was cloned into the XhoI/NotI sites of pCAGGS1 vector.

### Immunoblotting

Mouse tissues were harvested, flash-frozen in liquid nitrogen, and homogenized in RIPA buffer (Cell Signaling Technology, 9806) that contained cOmplete Mini Protease Inhibitor (Roche, 11836170001). Lysates were centrifuged at 14,000 x g for 10 min at 4°C and the supernatants were collected. Proteins were separated by SDS–PAGE and transferred onto Immobilon-FL membranes (Millipore). The antibodies used were exon AB (Itoh et al., 2018), pan-Drp1 (BD Biosciences, 611113), PDH subunit E2/E3bp (Abcam, ab110333), GAPDH (Thermo, MA5-15738), actin (Santa Cruz Biotechnology, sc-1615), Psd-95 (EMD Millipore, MABN68), clathrin (BD Biosciences, 610499), beta-III tubulin (Abcam, ab18207), GFP (Molecular probe, A11121), GluR1 (EMD Millipore, MAB397), GluR2 (Araki et al., 2010) and GluR3 (Araki et al., 2010). Immunocomplexes were visualized using fluorescently-labeled secondary antibodies and detected using a PharosFX Plus Molecular Imager (Bio-Rad).

### Neuronal cultures and immunofluorescence microscopy

Hippocampal neurons were isolated and cultured in vitro as previously described (Araki et al., 2015). In brief, E18.5 embryos were decapitated, and brains were quickly removed and transferred in cold Dissection media [1 x HBSS (Gibco, 14185052), 1 mM sodium pyruvate (Gibco, 11360070), 10 mM HEPES (Gibco, 15630080), 30 mM glucose, 100 U/ml penicillin, and 100 µg/ml streptomycin]. Hippocampi were dissected under a binocular microscope and incubated in Dissection medium supplemented with 0.5 mg/ml papain (Worthington, LS003119) and 0.01% DNase (Sigma, DN25) for 20 min at 37°C. Hippocampi were washed once with warm Neurobasal medium (Gibco, 21103049) supplemented with 100 U/ml penicillin, 100 µg/ml streptomycin, 2 mM GlutaMax (Gibco, 35050061), 2% B-27 (Gibco, 17504044) and 5% horse serum (Gibco, 26050088). Neurons were triturated and plated on 18 mm poly-L-lysine-coated coverslips at a density of 160,000 cells/well in 12-well tissue culture plates in 1 ml of the Neurobasal medium supplemented with 100 U/ml penicillin, 100 µg/ml streptomycin, 2 mM GlutaMax, 2% B-27% and 5% horse serum. After 24 hr, neurons were switched and maintained thereafter in Neurobasal media with 2 mM GlutaMax and 2% B-27. Cultured neurons were fed with half-media changes once per week. Cells were transfected with Lipofectamin 2000 (Invitrogen) in accordance with the manufacturer’s manual. After 2–3 days, neurons were fixed using PBS containing 4% paraformaldehyde, washed in PBS, permeabilized with 0.2% Triton X-100/PBS, and blocked in 0.5% BSA/PBS (Adachi et al., 2016). The cells were incubated with antibodies to pan-Drp1, HA (Novus Biologicals, NB600-362), RFP (antibodies-online, ABIN129578), VGLUT1 (Synaptic systems, 135304), MAP2 (Thermo Fisher, MA5-12826) and PDH subunit E2/E3bp, followed by the appropriate secondary antibodies. Samples were mounted in Prolong Gold Antifade Reagent (Cell Signaling, 9071) and viewed using Zeiss LSM510-Meta, LSM700 FCS, and LSM800 GaAsP laser scanning confocal microscopes. To determine the size of the mitochondria in the dendrites, we first examined serial confocal images along the Z-axis to identify individual mitochondria and then measured their length using ImageJ.

### PSD fractionation

Fractionation of post-synaptic density was performed as described previously (Araki et al., 2015). In brief, mouse whole brain was dissected and homogenized by a dounce homogenizer 30 times in Buffer A (0.32 M sucrose, 10 mM Hepes, pH7.4, with cOmplete Mini Protease Inhibitor). The homogenate was centrifuged at 1000 x g for 10 min at 4°C. The post-nuclear supernatant was collected and centrifuged at 13,800 x g for 20 min at 4°C. The supernatant was kept as S2 fraction. The pellet was resuspended in 3 volumes of Buffer A (P2 fraction). The P2 fraction was layered onto a discontinuous sucrose gradient (0.85, 1.0, and 1.4 M) in 10 mM Hepes (pH7.4) with cOmplete Mini Protease Inhibitor and centrifuged at 82,500 x g for 2 hr at 4°C. The interface between 1.0 and 1.4 M sucrose was collected as the synaptosome fraction (Syn) and diluted with 80 mM Tris-HCl (pH 8.0). An equal volume of 1% Triton X-100 was added and rotated for 10 min at 4°C, then centrifuged at 32,000 x g for 20 min. The supernatant was collected as Triton-soluble synaptosome (Syn/Tx) fraction, and the pellet was resuspended in 80 mM Tris-HCl (pH 8.0) (PSD fraction).

### Electron microscopy

Cultured neurons were fixed with 2% glutaraldehyde, 3 mM CaCl2, and 0.1 M cacodylate buffer, pH 7.4, for 1 hr. After washes, samples were post-fixed in 2.7% OsO4 and 167 mM cacodylate, pH 7.4, for 1 hr on ice (Kageyama et al., 2014; Wakabayashi et al., 2009). After washes in water, samples were incubated in 2% uranyl acetate for 30 min. After dehydration using 50, 70, 90, and 100% ethanol, samples were embedded in EPON resin. Ultrathin sections were obtained using a Reichert-Jung ultracut E, stained with 2% uranyl acetate and 0.3% lead citrate, and viewed using a transmission electron microscope (H-7600; Hitachi) equipped with a dual CCD camera (Advanced Microscopy Techniques).

For dynasore treatment, cells were incubated with 80 µM of dynasore (Sigma-Aldrich, D7693) in culture medium for different times, then fixed and further processed for electron microscopy as described above. To stimulate endocytosis through chemical long-term depression (chemical LTD), neurons were incubated with 20 µM of NMDA (Tocris, 0114), 10 µM of glycine (Tocris, 0219), 0.3 mM of MgCl2, 2 mM of CaCl2 and 1 µM of TTX (Tocris, 1078) in Base buffer (10 mM HEPES, pH 7.4, 140 mM NaCl, 2.4 mM KCl, 10 mM glucose) for 4 min. As a control, Base buffer containing 2 mM of MgCl2, 2 mM of CaCl2 and 1 µM of TTX was used. To induce chemical LTD in the presence of dynasore, neurons were first incubated for 1 min with 80 µM of dynasore in the culture medium and followed by a 3 min chemical LTD treatment in the presence of dynasore (80 µM). Neurons were then fixed and processed as described above.

### Analysis of endocytic zone

Hippocampal neurons (DIV22) were transfected with 1 µg of Psd-95.FingR-GFP plasmids (Addgene, 46295) and 250 ng of mCherry-clathrin light chain plasmids (Addgene, 27680) per coverslip in 12-well plates. Two days after transfection, neurons were treated with chemical LTD stimulation, fixed in PBS containing 4% formaldehyde and 4% sucrose for 20 min, washed with PBS and mounted. Neurons were selected based on GFP fluorescence, and mCherry/GFP images were taken. Images were acquired with LSM800 GaAsP laser scanning confocal microscopes and analyzed using ImageJ.

### Surface biotinylation assay

Cultured neurons were washed once with Base buffer containing 2 mM MgCl2 and 2 mM CaCl2 at room temperature; they were then washed twice with an ice-cold version of the same buffer. Cell-surface proteins were biotinylated with 1 mg/mL sulfo-NHS-SS-biotin (Pierce, 21331) in the same buffer for 20 min on ice. The remaining biotin was quenched by washing the cells two times for 5 min each with ice-cold PBS containing 20 mM glycine, 2 mM MgCl2 and 2 mM CaCl2. Immediately after quenching, the neurons were washed twice with PBS containing 2 mM MgCl2 and 2 mM CaCl2 and then lysed with RIPA buffer that contained cOmplete Mini Protease Inhibitor. The biotinylated cell surface proteins were precipitated using NeutrAvidin agarose (Pierce, 29200). The precipitated proteins and total cell lysates were separated by SDS-PAGE and blotted with antibodies to GluR1, GluR2, GluR3 and GAPDH.

### GluR1 internalization assay

Cultured neurons were transfected with 1 µg of Psd-95-mCherry plasmids (Blanpied et al., 2008) and 1 µg of GFP-GluR1 plasmids (Hussain et al., 2014) per coverslip in 12-well plates. Two days after transfection, the neurons were treated with chemical LTD stimulation, fixed in PBS containing 4% formaldehyde and 4% sucrose for 8 min, washed with PBS and blocked in 1% BSA/PBS for 30 min. To label surface GFP-GluR1, the cells were incubated with GFP antibody (Senoo et al., 2019) at 4°C overnight and then treated with Alexa Fluor 647-conjugated secondary antibodies. Images were acquired using LSM800 GaAsP laser scanning confocal microscopes and analyzed using ImageJ. Identical settings were used to acquire each image within an experiment.

### Transferrin uptake

MEFs were incubated with 5 µg/ml of Alexa-Fluor-647-transferrin (Thermo, T23366) in the culture medium for 30 min at 4°C or 37°C. Cells were washed twice with cold PBS, fixed using PBS containing 4% paraformaldehyde, washed in PBS and visualized by confocal microscopy. Mean fluorescent signals in each cell were measured using Image J. Cultured neurons were incubated with 50 µg/ml of FITC-transferrin (Thermo, T2871) in the culture medium for 15 min at 4°C or 37°C. Cells were washed twice with cold PBS, fixed using PBS containing 4% paraformaldehyde and 4% sucrose, washed in PBS and then visualized by confocal microscopy. Mean fluorescent intensity was measured along dendrites (100 µm in length) using Image J.

### In utero electroporation

In utero electroporation that targeted the dorsal hippocampus region was performed according to our published protocol with some modifications (Saito et al., 2016). Pregnant mice (C57BL/6J, The Jackson Laboratory, stock no. 000664) were anesthetized at embryonic day 15.5 (E15.5) by intraperitoneal administration of a mixed solution of ketamine HCl (100 mg/kg), xylazine HCl (7.5 mg/kg), and buprenorphine HCl (0.05 mg/kg). After the uterine horn was exposed by laparotomy, the CAG promoter-driven eGFP expression plasmid, pCAGGS1-eGFP (1 µg/µl), together with the Drp1ABCD knockdown plasmid, pSUPER-AB (1 µg/µl), was injected (1–2 µl) into the lateral ventricles with a glass micropipette made from a microcapillary tube (Narishige, Cat #GD-1). Using a ø3mm electrode (Nepagene #CUY650P3), the plasmids were delivered into the dorsal hippocampus by electric pulses (40V; 50 ms), which were charged four times at intervals of 950 ms with an electroporator (Nepagene #CUY21EDIT). After electroporation, the uterine horn was replaced in the abdominal cavity to allow the embryos to continue to develop.

### Behavioral analysis

All of the behavior tests were performed in mice of 2–5 months of age at the Behavior Core of the Johns Hopkins University School of Medicine. For open field tests, mice were placed in a Photo-beam Activity System Open Field (San Diego Instruments, CA, USA) and their movement was recorded for 30 min (Breu et al., 2016). The open field chamber consisted of a clear Plexiglas box (40 × 40 × 37 cm) with 16 horizontal and 16 vertical photo-beams to assess locomotion and location tendency. Activity parameters were quantified as the number of beam breaks.

For PPI tests, mice were put in a clear Plexiglas cylinder (3.8 cm in diameter) within a startle chamber (San Diego Instruments) and tested for their sensorimotor gating function using SR-LAB software (Nasu et al., 2014; Saito et al., 2016) (Startle Response System, San Diego Instruments, CA, USA). A loudspeaker mounted 24 cm above the cylinder provided acoustic stimuli and background noise (70 dB) and controlled the delivery of all stimuli to the animal by SR-LAB software and the interface system. A maximum voltage during the 100 ms period beginning at the stimulus onset was measured as a startle amplitude. To initiate the test, mice were given a 5 min acclimation period with 70 dB background noise; this background noise was present throughout the entire session. After acclimation, mice were exposed to a pulse (a 120 dB, 40 ms) 10 times and then the background-only session 10 times at a 20 s inter-stimuli interval (habituation session). In experimental sessions, mice were exposed to the following types of trials: pulse alone trial (a 120 dB, 100 ms broadband burst); the omission of stimuli (no pulse, only background noise); and five prepulse-pulse combination trials. Broadband bursts (20 ms) were individually presented as prepulses for 80 ms before the pulse (120 dB, 100 ms broadband pulse). Each session consisted of six presentations of each type of trial presented at a 20 s inter-stimulus interval in a pseudorandom order. PPI was defined as a reduced percentage of startle amplitude in prepulse-pulse trials compared to the startle amplitude in startle-alone trials.

For the Y-maze test, mice were placed in a Y-shaped maze with three arms (38 × 7.5 × 12 cm) at 120-degree angles from each other. After introduction to the center of the maze, mice are allowed to freely explore the three arms and are video-recorded for 10 min. The number of arm entries and the time spent in each arm were scored in order to calculate the percentage of alternation.

For rotarod tests, mice were placed on the rod spindle assembly (3.0 cm in diameter) of the Rotamex-5 system (Kageyama et al., 2012) (Columbus Instruments, OH, USA). Mice were first trained at 4.0 rpm for 5 min. After this training session, the rotarod was accelerated with a 1.0 rpm increase in rotational speed every 5 s. The time elapsed before falling was recorded for each mouse. Three consecutive trials were performed and the results were averaged in each mouse.

For the elevated plus maze test, a mouse was placed on the starting platform in the plus maze (San Diego Instruments Inc, San Diego, CA, USA) and the mouse's behaviors were video-recorded for 5 min. We scored the numbers of entries into the closed and open arms and the time spent in the closed and open arms.

### MEFs and lentiviruses

Drp1-KO MEFs were cultured in Iscove’s modified Dulbecco’s medium supplemented with 10% fetal bovine serum as described previously (Kageyama et al., 2014). Genotypes of MEFs were confirmed by PCR as described (Kageyama et al., 2014). No contamination of mycoplasma has been confirmed. Lentiviruses were produced as described previously (Itoh et al., 2018).
